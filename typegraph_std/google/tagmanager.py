from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_tagmanager():
    tagmanager = HTTPRuntime("https://tagmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_tagmanager_1_ErrorResponse",
        "ContainerIn": "_tagmanager_2_ContainerIn",
        "ContainerOut": "_tagmanager_3_ContainerOut",
        "ContainerFeaturesIn": "_tagmanager_4_ContainerFeaturesIn",
        "ContainerFeaturesOut": "_tagmanager_5_ContainerFeaturesOut",
        "ListClientsResponseIn": "_tagmanager_6_ListClientsResponseIn",
        "ListClientsResponseOut": "_tagmanager_7_ListClientsResponseOut",
        "AccountAccessIn": "_tagmanager_8_AccountAccessIn",
        "AccountAccessOut": "_tagmanager_9_AccountAccessOut",
        "ListUserPermissionsResponseIn": "_tagmanager_10_ListUserPermissionsResponseIn",
        "ListUserPermissionsResponseOut": "_tagmanager_11_ListUserPermissionsResponseOut",
        "RevertTransformationResponseIn": "_tagmanager_12_RevertTransformationResponseIn",
        "RevertTransformationResponseOut": "_tagmanager_13_RevertTransformationResponseOut",
        "FolderEntitiesIn": "_tagmanager_14_FolderEntitiesIn",
        "FolderEntitiesOut": "_tagmanager_15_FolderEntitiesOut",
        "ParameterIn": "_tagmanager_16_ParameterIn",
        "ParameterOut": "_tagmanager_17_ParameterOut",
        "CreateContainerVersionResponseIn": "_tagmanager_18_CreateContainerVersionResponseIn",
        "CreateContainerVersionResponseOut": "_tagmanager_19_CreateContainerVersionResponseOut",
        "TransformationIn": "_tagmanager_20_TransformationIn",
        "TransformationOut": "_tagmanager_21_TransformationOut",
        "RevertTriggerResponseIn": "_tagmanager_22_RevertTriggerResponseIn",
        "RevertTriggerResponseOut": "_tagmanager_23_RevertTriggerResponseOut",
        "BuiltInVariableIn": "_tagmanager_24_BuiltInVariableIn",
        "BuiltInVariableOut": "_tagmanager_25_BuiltInVariableOut",
        "ListVariablesResponseIn": "_tagmanager_26_ListVariablesResponseIn",
        "ListVariablesResponseOut": "_tagmanager_27_ListVariablesResponseOut",
        "EntityIn": "_tagmanager_28_EntityIn",
        "EntityOut": "_tagmanager_29_EntityOut",
        "SetupTagIn": "_tagmanager_30_SetupTagIn",
        "SetupTagOut": "_tagmanager_31_SetupTagOut",
        "ContainerVersionHeaderIn": "_tagmanager_32_ContainerVersionHeaderIn",
        "ContainerVersionHeaderOut": "_tagmanager_33_ContainerVersionHeaderOut",
        "ListTagsResponseIn": "_tagmanager_34_ListTagsResponseIn",
        "ListTagsResponseOut": "_tagmanager_35_ListTagsResponseOut",
        "RevertTagResponseIn": "_tagmanager_36_RevertTagResponseIn",
        "RevertTagResponseOut": "_tagmanager_37_RevertTagResponseOut",
        "MergeConflictIn": "_tagmanager_38_MergeConflictIn",
        "MergeConflictOut": "_tagmanager_39_MergeConflictOut",
        "GetWorkspaceStatusResponseIn": "_tagmanager_40_GetWorkspaceStatusResponseIn",
        "GetWorkspaceStatusResponseOut": "_tagmanager_41_GetWorkspaceStatusResponseOut",
        "FolderIn": "_tagmanager_42_FolderIn",
        "FolderOut": "_tagmanager_43_FolderOut",
        "AccountIn": "_tagmanager_44_AccountIn",
        "AccountOut": "_tagmanager_45_AccountOut",
        "WorkspaceIn": "_tagmanager_46_WorkspaceIn",
        "WorkspaceOut": "_tagmanager_47_WorkspaceOut",
        "VariableIn": "_tagmanager_48_VariableIn",
        "VariableOut": "_tagmanager_49_VariableOut",
        "ListTriggersResponseIn": "_tagmanager_50_ListTriggersResponseIn",
        "ListTriggersResponseOut": "_tagmanager_51_ListTriggersResponseOut",
        "ListEnvironmentsResponseIn": "_tagmanager_52_ListEnvironmentsResponseIn",
        "ListEnvironmentsResponseOut": "_tagmanager_53_ListEnvironmentsResponseOut",
        "TeardownTagIn": "_tagmanager_54_TeardownTagIn",
        "TeardownTagOut": "_tagmanager_55_TeardownTagOut",
        "ListContainerVersionsResponseIn": "_tagmanager_56_ListContainerVersionsResponseIn",
        "ListContainerVersionsResponseOut": "_tagmanager_57_ListContainerVersionsResponseOut",
        "GtagConfigIn": "_tagmanager_58_GtagConfigIn",
        "GtagConfigOut": "_tagmanager_59_GtagConfigOut",
        "UserPermissionIn": "_tagmanager_60_UserPermissionIn",
        "UserPermissionOut": "_tagmanager_61_UserPermissionOut",
        "ListZonesResponseIn": "_tagmanager_62_ListZonesResponseIn",
        "ListZonesResponseOut": "_tagmanager_63_ListZonesResponseOut",
        "ListAccountsResponseIn": "_tagmanager_64_ListAccountsResponseIn",
        "ListAccountsResponseOut": "_tagmanager_65_ListAccountsResponseOut",
        "SyncStatusIn": "_tagmanager_66_SyncStatusIn",
        "SyncStatusOut": "_tagmanager_67_SyncStatusOut",
        "VariableFormatValueIn": "_tagmanager_68_VariableFormatValueIn",
        "VariableFormatValueOut": "_tagmanager_69_VariableFormatValueOut",
        "CreateContainerVersionRequestVersionOptionsIn": "_tagmanager_70_CreateContainerVersionRequestVersionOptionsIn",
        "CreateContainerVersionRequestVersionOptionsOut": "_tagmanager_71_CreateContainerVersionRequestVersionOptionsOut",
        "ListFoldersResponseIn": "_tagmanager_72_ListFoldersResponseIn",
        "ListFoldersResponseOut": "_tagmanager_73_ListFoldersResponseOut",
        "ListTransformationsResponseIn": "_tagmanager_74_ListTransformationsResponseIn",
        "ListTransformationsResponseOut": "_tagmanager_75_ListTransformationsResponseOut",
        "CustomTemplateIn": "_tagmanager_76_CustomTemplateIn",
        "CustomTemplateOut": "_tagmanager_77_CustomTemplateOut",
        "QuickPreviewResponseIn": "_tagmanager_78_QuickPreviewResponseIn",
        "QuickPreviewResponseOut": "_tagmanager_79_QuickPreviewResponseOut",
        "ListDestinationsResponseIn": "_tagmanager_80_ListDestinationsResponseIn",
        "ListDestinationsResponseOut": "_tagmanager_81_ListDestinationsResponseOut",
        "TagConsentSettingIn": "_tagmanager_82_TagConsentSettingIn",
        "TagConsentSettingOut": "_tagmanager_83_TagConsentSettingOut",
        "RevertClientResponseIn": "_tagmanager_84_RevertClientResponseIn",
        "RevertClientResponseOut": "_tagmanager_85_RevertClientResponseOut",
        "DestinationIn": "_tagmanager_86_DestinationIn",
        "DestinationOut": "_tagmanager_87_DestinationOut",
        "ContainerAccessIn": "_tagmanager_88_ContainerAccessIn",
        "ContainerAccessOut": "_tagmanager_89_ContainerAccessOut",
        "ConditionIn": "_tagmanager_90_ConditionIn",
        "ConditionOut": "_tagmanager_91_ConditionOut",
        "ZoneTypeRestrictionIn": "_tagmanager_92_ZoneTypeRestrictionIn",
        "ZoneTypeRestrictionOut": "_tagmanager_93_ZoneTypeRestrictionOut",
        "ZoneBoundaryIn": "_tagmanager_94_ZoneBoundaryIn",
        "ZoneBoundaryOut": "_tagmanager_95_ZoneBoundaryOut",
        "GalleryReferenceIn": "_tagmanager_96_GalleryReferenceIn",
        "GalleryReferenceOut": "_tagmanager_97_GalleryReferenceOut",
        "TagIn": "_tagmanager_98_TagIn",
        "TagOut": "_tagmanager_99_TagOut",
        "ListTemplatesResponseIn": "_tagmanager_100_ListTemplatesResponseIn",
        "ListTemplatesResponseOut": "_tagmanager_101_ListTemplatesResponseOut",
        "TriggerIn": "_tagmanager_102_TriggerIn",
        "TriggerOut": "_tagmanager_103_TriggerOut",
        "ContainerVersionIn": "_tagmanager_104_ContainerVersionIn",
        "ContainerVersionOut": "_tagmanager_105_ContainerVersionOut",
        "ListWorkspacesResponseIn": "_tagmanager_106_ListWorkspacesResponseIn",
        "ListWorkspacesResponseOut": "_tagmanager_107_ListWorkspacesResponseOut",
        "ListContainersResponseIn": "_tagmanager_108_ListContainersResponseIn",
        "ListContainersResponseOut": "_tagmanager_109_ListContainersResponseOut",
        "ClientIn": "_tagmanager_110_ClientIn",
        "ClientOut": "_tagmanager_111_ClientOut",
        "RevertFolderResponseIn": "_tagmanager_112_RevertFolderResponseIn",
        "RevertFolderResponseOut": "_tagmanager_113_RevertFolderResponseOut",
        "CreateBuiltInVariableResponseIn": "_tagmanager_114_CreateBuiltInVariableResponseIn",
        "CreateBuiltInVariableResponseOut": "_tagmanager_115_CreateBuiltInVariableResponseOut",
        "ZoneChildContainerIn": "_tagmanager_116_ZoneChildContainerIn",
        "ZoneChildContainerOut": "_tagmanager_117_ZoneChildContainerOut",
        "ZoneIn": "_tagmanager_118_ZoneIn",
        "ZoneOut": "_tagmanager_119_ZoneOut",
        "RevertZoneResponseIn": "_tagmanager_120_RevertZoneResponseIn",
        "RevertZoneResponseOut": "_tagmanager_121_RevertZoneResponseOut",
        "ListGtagConfigResponseIn": "_tagmanager_122_ListGtagConfigResponseIn",
        "ListGtagConfigResponseOut": "_tagmanager_123_ListGtagConfigResponseOut",
        "RevertTemplateResponseIn": "_tagmanager_124_RevertTemplateResponseIn",
        "RevertTemplateResponseOut": "_tagmanager_125_RevertTemplateResponseOut",
        "ListEnabledBuiltInVariablesResponseIn": "_tagmanager_126_ListEnabledBuiltInVariablesResponseIn",
        "ListEnabledBuiltInVariablesResponseOut": "_tagmanager_127_ListEnabledBuiltInVariablesResponseOut",
        "RevertVariableResponseIn": "_tagmanager_128_RevertVariableResponseIn",
        "RevertVariableResponseOut": "_tagmanager_129_RevertVariableResponseOut",
        "GetContainerSnippetResponseIn": "_tagmanager_130_GetContainerSnippetResponseIn",
        "GetContainerSnippetResponseOut": "_tagmanager_131_GetContainerSnippetResponseOut",
        "AccountFeaturesIn": "_tagmanager_132_AccountFeaturesIn",
        "AccountFeaturesOut": "_tagmanager_133_AccountFeaturesOut",
        "SyncWorkspaceResponseIn": "_tagmanager_134_SyncWorkspaceResponseIn",
        "SyncWorkspaceResponseOut": "_tagmanager_135_SyncWorkspaceResponseOut",
        "RevertBuiltInVariableResponseIn": "_tagmanager_136_RevertBuiltInVariableResponseIn",
        "RevertBuiltInVariableResponseOut": "_tagmanager_137_RevertBuiltInVariableResponseOut",
        "EnvironmentIn": "_tagmanager_138_EnvironmentIn",
        "EnvironmentOut": "_tagmanager_139_EnvironmentOut",
        "PublishContainerVersionResponseIn": "_tagmanager_140_PublishContainerVersionResponseIn",
        "PublishContainerVersionResponseOut": "_tagmanager_141_PublishContainerVersionResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ContainerIn"] = t.struct(
        {
            "tagManagerUrl": t.string().optional(),
            "accountId": t.string().optional(),
            "domainName": t.array(t.string()).optional(),
            "fingerprint": t.string().optional(),
            "usageContext": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "taggingServerUrls": t.array(t.string()).optional(),
            "path": t.string().optional(),
            "notes": t.string().optional(),
            "containerId": t.string().optional(),
            "tagIds": t.array(t.string()).optional(),
            "features": t.proxy(renames["ContainerFeaturesIn"]).optional(),
            "publicId": t.string().optional(),
        }
    ).named(renames["ContainerIn"])
    types["ContainerOut"] = t.struct(
        {
            "tagManagerUrl": t.string().optional(),
            "accountId": t.string().optional(),
            "domainName": t.array(t.string()).optional(),
            "fingerprint": t.string().optional(),
            "usageContext": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "taggingServerUrls": t.array(t.string()).optional(),
            "path": t.string().optional(),
            "notes": t.string().optional(),
            "containerId": t.string().optional(),
            "tagIds": t.array(t.string()).optional(),
            "features": t.proxy(renames["ContainerFeaturesOut"]).optional(),
            "publicId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerOut"])
    types["ContainerFeaturesIn"] = t.struct(
        {
            "supportEnvironments": t.boolean().optional(),
            "supportTemplates": t.boolean().optional(),
            "supportTransformations": t.boolean().optional(),
            "supportBuiltInVariables": t.boolean().optional(),
            "supportClients": t.boolean().optional(),
            "supportFolders": t.boolean().optional(),
            "supportUserPermissions": t.boolean().optional(),
            "supportTags": t.boolean().optional(),
            "supportVariables": t.boolean().optional(),
            "supportTriggers": t.boolean().optional(),
            "supportVersions": t.boolean().optional(),
            "supportWorkspaces": t.boolean().optional(),
            "supportGtagConfigs": t.boolean().optional(),
            "supportZones": t.boolean().optional(),
        }
    ).named(renames["ContainerFeaturesIn"])
    types["ContainerFeaturesOut"] = t.struct(
        {
            "supportEnvironments": t.boolean().optional(),
            "supportTemplates": t.boolean().optional(),
            "supportTransformations": t.boolean().optional(),
            "supportBuiltInVariables": t.boolean().optional(),
            "supportClients": t.boolean().optional(),
            "supportFolders": t.boolean().optional(),
            "supportUserPermissions": t.boolean().optional(),
            "supportTags": t.boolean().optional(),
            "supportVariables": t.boolean().optional(),
            "supportTriggers": t.boolean().optional(),
            "supportVersions": t.boolean().optional(),
            "supportWorkspaces": t.boolean().optional(),
            "supportGtagConfigs": t.boolean().optional(),
            "supportZones": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerFeaturesOut"])
    types["ListClientsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "client": t.array(t.proxy(renames["ClientIn"])).optional(),
        }
    ).named(renames["ListClientsResponseIn"])
    types["ListClientsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "client": t.array(t.proxy(renames["ClientOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListClientsResponseOut"])
    types["AccountAccessIn"] = t.struct({"permission": t.string().optional()}).named(
        renames["AccountAccessIn"]
    )
    types["AccountAccessOut"] = t.struct(
        {
            "permission": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountAccessOut"])
    types["ListUserPermissionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "userPermission": t.array(t.proxy(renames["UserPermissionIn"])).optional(),
        }
    ).named(renames["ListUserPermissionsResponseIn"])
    types["ListUserPermissionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "userPermission": t.array(t.proxy(renames["UserPermissionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUserPermissionsResponseOut"])
    types["RevertTransformationResponseIn"] = t.struct(
        {"transformation": t.proxy(renames["TransformationIn"]).optional()}
    ).named(renames["RevertTransformationResponseIn"])
    types["RevertTransformationResponseOut"] = t.struct(
        {
            "transformation": t.proxy(renames["TransformationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertTransformationResponseOut"])
    types["FolderEntitiesIn"] = t.struct(
        {
            "tag": t.array(t.proxy(renames["TagIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "variable": t.array(t.proxy(renames["VariableIn"])).optional(),
            "trigger": t.array(t.proxy(renames["TriggerIn"])).optional(),
        }
    ).named(renames["FolderEntitiesIn"])
    types["FolderEntitiesOut"] = t.struct(
        {
            "tag": t.array(t.proxy(renames["TagOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "variable": t.array(t.proxy(renames["VariableOut"])).optional(),
            "trigger": t.array(t.proxy(renames["TriggerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderEntitiesOut"])
    types["ParameterIn"] = t.struct(
        {
            "key": t.string().optional(),
            "map": t.array(t.proxy(renames["ParameterIn"])).optional(),
            "value": t.string().optional(),
            "list": t.array(t.proxy(renames["ParameterIn"])).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ParameterIn"])
    types["ParameterOut"] = t.struct(
        {
            "key": t.string().optional(),
            "map": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "value": t.string().optional(),
            "list": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParameterOut"])
    types["CreateContainerVersionResponseIn"] = t.struct(
        {
            "syncStatus": t.proxy(renames["SyncStatusIn"]).optional(),
            "newWorkspacePath": t.string().optional(),
            "containerVersion": t.proxy(renames["ContainerVersionIn"]).optional(),
            "compilerError": t.boolean().optional(),
        }
    ).named(renames["CreateContainerVersionResponseIn"])
    types["CreateContainerVersionResponseOut"] = t.struct(
        {
            "syncStatus": t.proxy(renames["SyncStatusOut"]).optional(),
            "newWorkspacePath": t.string().optional(),
            "containerVersion": t.proxy(renames["ContainerVersionOut"]).optional(),
            "compilerError": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateContainerVersionResponseOut"])
    types["TransformationIn"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "transformationId": t.string().optional(),
            "path": t.string().optional(),
            "parentFolderId": t.string().optional(),
            "containerId": t.string().optional(),
            "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
            "notes": t.string().optional(),
            "workspaceId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
        }
    ).named(renames["TransformationIn"])
    types["TransformationOut"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "transformationId": t.string().optional(),
            "path": t.string().optional(),
            "parentFolderId": t.string().optional(),
            "containerId": t.string().optional(),
            "parameter": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "notes": t.string().optional(),
            "workspaceId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransformationOut"])
    types["RevertTriggerResponseIn"] = t.struct(
        {"trigger": t.proxy(renames["TriggerIn"]).optional()}
    ).named(renames["RevertTriggerResponseIn"])
    types["RevertTriggerResponseOut"] = t.struct(
        {
            "trigger": t.proxy(renames["TriggerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertTriggerResponseOut"])
    types["BuiltInVariableIn"] = t.struct(
        {
            "workspaceId": t.string().optional(),
            "name": t.string().optional(),
            "containerId": t.string().optional(),
            "accountId": t.string().optional(),
            "type": t.string().optional(),
            "path": t.string().optional(),
        }
    ).named(renames["BuiltInVariableIn"])
    types["BuiltInVariableOut"] = t.struct(
        {
            "workspaceId": t.string().optional(),
            "name": t.string().optional(),
            "containerId": t.string().optional(),
            "accountId": t.string().optional(),
            "type": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuiltInVariableOut"])
    types["ListVariablesResponseIn"] = t.struct(
        {
            "variable": t.array(t.proxy(renames["VariableIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListVariablesResponseIn"])
    types["ListVariablesResponseOut"] = t.struct(
        {
            "variable": t.array(t.proxy(renames["VariableOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVariablesResponseOut"])
    types["EntityIn"] = t.struct(
        {
            "tag": t.proxy(renames["TagIn"]).optional(),
            "trigger": t.proxy(renames["TriggerIn"]).optional(),
            "client": t.proxy(renames["ClientIn"]).optional(),
            "folder": t.proxy(renames["FolderIn"]).optional(),
            "transformation": t.proxy(renames["TransformationIn"]).optional(),
            "changeStatus": t.string().optional(),
            "variable": t.proxy(renames["VariableIn"]).optional(),
        }
    ).named(renames["EntityIn"])
    types["EntityOut"] = t.struct(
        {
            "tag": t.proxy(renames["TagOut"]).optional(),
            "trigger": t.proxy(renames["TriggerOut"]).optional(),
            "client": t.proxy(renames["ClientOut"]).optional(),
            "folder": t.proxy(renames["FolderOut"]).optional(),
            "transformation": t.proxy(renames["TransformationOut"]).optional(),
            "changeStatus": t.string().optional(),
            "variable": t.proxy(renames["VariableOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityOut"])
    types["SetupTagIn"] = t.struct(
        {"tagName": t.string().optional(), "stopOnSetupFailure": t.boolean().optional()}
    ).named(renames["SetupTagIn"])
    types["SetupTagOut"] = t.struct(
        {
            "tagName": t.string().optional(),
            "stopOnSetupFailure": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetupTagOut"])
    types["ContainerVersionHeaderIn"] = t.struct(
        {
            "numTransformations": t.string().optional(),
            "numTags": t.string().optional(),
            "numCustomTemplates": t.string().optional(),
            "path": t.string().optional(),
            "name": t.string().optional(),
            "numRules": t.string().optional(),
            "numTriggers": t.string().optional(),
            "containerVersionId": t.string().optional(),
            "deleted": t.boolean().optional(),
            "numMacros": t.string().optional(),
            "numClients": t.string().optional(),
            "numVariables": t.string().optional(),
            "numGtagConfigs": t.string().optional(),
            "containerId": t.string().optional(),
            "numZones": t.string().optional(),
            "accountId": t.string().optional(),
        }
    ).named(renames["ContainerVersionHeaderIn"])
    types["ContainerVersionHeaderOut"] = t.struct(
        {
            "numTransformations": t.string().optional(),
            "numTags": t.string().optional(),
            "numCustomTemplates": t.string().optional(),
            "path": t.string().optional(),
            "name": t.string().optional(),
            "numRules": t.string().optional(),
            "numTriggers": t.string().optional(),
            "containerVersionId": t.string().optional(),
            "deleted": t.boolean().optional(),
            "numMacros": t.string().optional(),
            "numClients": t.string().optional(),
            "numVariables": t.string().optional(),
            "numGtagConfigs": t.string().optional(),
            "containerId": t.string().optional(),
            "numZones": t.string().optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerVersionHeaderOut"])
    types["ListTagsResponseIn"] = t.struct(
        {
            "tag": t.array(t.proxy(renames["TagIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTagsResponseIn"])
    types["ListTagsResponseOut"] = t.struct(
        {
            "tag": t.array(t.proxy(renames["TagOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTagsResponseOut"])
    types["RevertTagResponseIn"] = t.struct(
        {"tag": t.proxy(renames["TagIn"]).optional()}
    ).named(renames["RevertTagResponseIn"])
    types["RevertTagResponseOut"] = t.struct(
        {
            "tag": t.proxy(renames["TagOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertTagResponseOut"])
    types["MergeConflictIn"] = t.struct(
        {
            "entityInBaseVersion": t.proxy(renames["EntityIn"]).optional(),
            "entityInWorkspace": t.proxy(renames["EntityIn"]).optional(),
        }
    ).named(renames["MergeConflictIn"])
    types["MergeConflictOut"] = t.struct(
        {
            "entityInBaseVersion": t.proxy(renames["EntityOut"]).optional(),
            "entityInWorkspace": t.proxy(renames["EntityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MergeConflictOut"])
    types["GetWorkspaceStatusResponseIn"] = t.struct(
        {
            "workspaceChange": t.array(t.proxy(renames["EntityIn"])).optional(),
            "mergeConflict": t.array(t.proxy(renames["MergeConflictIn"])).optional(),
        }
    ).named(renames["GetWorkspaceStatusResponseIn"])
    types["GetWorkspaceStatusResponseOut"] = t.struct(
        {
            "workspaceChange": t.array(t.proxy(renames["EntityOut"])).optional(),
            "mergeConflict": t.array(t.proxy(renames["MergeConflictOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetWorkspaceStatusResponseOut"])
    types["FolderIn"] = t.struct(
        {
            "path": t.string().optional(),
            "fingerprint": t.string().optional(),
            "name": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "workspaceId": t.string().optional(),
            "notes": t.string().optional(),
            "containerId": t.string().optional(),
            "folderId": t.string().optional(),
            "accountId": t.string().optional(),
        }
    ).named(renames["FolderIn"])
    types["FolderOut"] = t.struct(
        {
            "path": t.string().optional(),
            "fingerprint": t.string().optional(),
            "name": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "workspaceId": t.string().optional(),
            "notes": t.string().optional(),
            "containerId": t.string().optional(),
            "folderId": t.string().optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOut"])
    types["AccountIn"] = t.struct(
        {
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "path": t.string().optional(),
            "fingerprint": t.string().optional(),
            "shareData": t.boolean().optional(),
            "tagManagerUrl": t.string().optional(),
            "features": t.proxy(renames["AccountFeaturesIn"]).optional(),
        }
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "path": t.string().optional(),
            "fingerprint": t.string().optional(),
            "shareData": t.boolean().optional(),
            "tagManagerUrl": t.string().optional(),
            "features": t.proxy(renames["AccountFeaturesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
    types["WorkspaceIn"] = t.struct(
        {
            "workspaceId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "containerId": t.string().optional(),
            "accountId": t.string().optional(),
            "path": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "fingerprint": t.string().optional(),
        }
    ).named(renames["WorkspaceIn"])
    types["WorkspaceOut"] = t.struct(
        {
            "workspaceId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "containerId": t.string().optional(),
            "accountId": t.string().optional(),
            "path": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "fingerprint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkspaceOut"])
    types["VariableIn"] = t.struct(
        {
            "workspaceId": t.string().optional(),
            "scheduleStartMs": t.string().optional(),
            "enablingTriggerId": t.array(t.string()).optional(),
            "notes": t.string().optional(),
            "fingerprint": t.string().optional(),
            "accountId": t.string().optional(),
            "formatValue": t.proxy(renames["VariableFormatValueIn"]).optional(),
            "scheduleEndMs": t.string().optional(),
            "containerId": t.string().optional(),
            "type": t.string().optional(),
            "parentFolderId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "name": t.string().optional(),
            "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
            "path": t.string().optional(),
            "variableId": t.string().optional(),
            "disablingTriggerId": t.array(t.string()).optional(),
        }
    ).named(renames["VariableIn"])
    types["VariableOut"] = t.struct(
        {
            "workspaceId": t.string().optional(),
            "scheduleStartMs": t.string().optional(),
            "enablingTriggerId": t.array(t.string()).optional(),
            "notes": t.string().optional(),
            "fingerprint": t.string().optional(),
            "accountId": t.string().optional(),
            "formatValue": t.proxy(renames["VariableFormatValueOut"]).optional(),
            "scheduleEndMs": t.string().optional(),
            "containerId": t.string().optional(),
            "type": t.string().optional(),
            "parentFolderId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "name": t.string().optional(),
            "parameter": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "path": t.string().optional(),
            "variableId": t.string().optional(),
            "disablingTriggerId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VariableOut"])
    types["ListTriggersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "trigger": t.array(t.proxy(renames["TriggerIn"])).optional(),
        }
    ).named(renames["ListTriggersResponseIn"])
    types["ListTriggersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "trigger": t.array(t.proxy(renames["TriggerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTriggersResponseOut"])
    types["ListEnvironmentsResponseIn"] = t.struct(
        {
            "environment": t.array(t.proxy(renames["EnvironmentIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListEnvironmentsResponseIn"])
    types["ListEnvironmentsResponseOut"] = t.struct(
        {
            "environment": t.array(t.proxy(renames["EnvironmentOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEnvironmentsResponseOut"])
    types["TeardownTagIn"] = t.struct(
        {
            "tagName": t.string().optional(),
            "stopTeardownOnFailure": t.boolean().optional(),
        }
    ).named(renames["TeardownTagIn"])
    types["TeardownTagOut"] = t.struct(
        {
            "tagName": t.string().optional(),
            "stopTeardownOnFailure": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TeardownTagOut"])
    types["ListContainerVersionsResponseIn"] = t.struct(
        {
            "containerVersionHeader": t.array(
                t.proxy(renames["ContainerVersionHeaderIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListContainerVersionsResponseIn"])
    types["ListContainerVersionsResponseOut"] = t.struct(
        {
            "containerVersionHeader": t.array(
                t.proxy(renames["ContainerVersionHeaderOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListContainerVersionsResponseOut"])
    types["GtagConfigIn"] = t.struct(
        {
            "tagManagerUrl": t.string().optional(),
            "containerId": t.string().optional(),
            "path": t.string().optional(),
            "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
            "gtagConfigId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "workspaceId": t.string().optional(),
            "accountId": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GtagConfigIn"])
    types["GtagConfigOut"] = t.struct(
        {
            "tagManagerUrl": t.string().optional(),
            "containerId": t.string().optional(),
            "path": t.string().optional(),
            "parameter": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "gtagConfigId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "workspaceId": t.string().optional(),
            "accountId": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GtagConfigOut"])
    types["UserPermissionIn"] = t.struct(
        {
            "path": t.string().optional(),
            "accountId": t.string().optional(),
            "emailAddress": t.string().optional(),
            "containerAccess": t.array(
                t.proxy(renames["ContainerAccessIn"])
            ).optional(),
            "accountAccess": t.proxy(renames["AccountAccessIn"]).optional(),
        }
    ).named(renames["UserPermissionIn"])
    types["UserPermissionOut"] = t.struct(
        {
            "path": t.string().optional(),
            "accountId": t.string().optional(),
            "emailAddress": t.string().optional(),
            "containerAccess": t.array(
                t.proxy(renames["ContainerAccessOut"])
            ).optional(),
            "accountAccess": t.proxy(renames["AccountAccessOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserPermissionOut"])
    types["ListZonesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "zone": t.array(t.proxy(renames["ZoneIn"])).optional(),
        }
    ).named(renames["ListZonesResponseIn"])
    types["ListZonesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "zone": t.array(t.proxy(renames["ZoneOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListZonesResponseOut"])
    types["ListAccountsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "account": t.array(t.proxy(renames["AccountIn"])).optional(),
        }
    ).named(renames["ListAccountsResponseIn"])
    types["ListAccountsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "account": t.array(t.proxy(renames["AccountOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAccountsResponseOut"])
    types["SyncStatusIn"] = t.struct(
        {"mergeConflict": t.boolean().optional(), "syncError": t.boolean().optional()}
    ).named(renames["SyncStatusIn"])
    types["SyncStatusOut"] = t.struct(
        {
            "mergeConflict": t.boolean().optional(),
            "syncError": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SyncStatusOut"])
    types["VariableFormatValueIn"] = t.struct(
        {
            "caseConversionType": t.string().optional(),
            "convertNullToValue": t.proxy(renames["ParameterIn"]).optional(),
            "convertUndefinedToValue": t.proxy(renames["ParameterIn"]).optional(),
            "convertTrueToValue": t.proxy(renames["ParameterIn"]).optional(),
            "convertFalseToValue": t.proxy(renames["ParameterIn"]).optional(),
        }
    ).named(renames["VariableFormatValueIn"])
    types["VariableFormatValueOut"] = t.struct(
        {
            "caseConversionType": t.string().optional(),
            "convertNullToValue": t.proxy(renames["ParameterOut"]).optional(),
            "convertUndefinedToValue": t.proxy(renames["ParameterOut"]).optional(),
            "convertTrueToValue": t.proxy(renames["ParameterOut"]).optional(),
            "convertFalseToValue": t.proxy(renames["ParameterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VariableFormatValueOut"])
    types["CreateContainerVersionRequestVersionOptionsIn"] = t.struct(
        {"notes": t.string().optional(), "name": t.string().optional()}
    ).named(renames["CreateContainerVersionRequestVersionOptionsIn"])
    types["CreateContainerVersionRequestVersionOptionsOut"] = t.struct(
        {
            "notes": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateContainerVersionRequestVersionOptionsOut"])
    types["ListFoldersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "folder": t.array(t.proxy(renames["FolderIn"])).optional(),
        }
    ).named(renames["ListFoldersResponseIn"])
    types["ListFoldersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "folder": t.array(t.proxy(renames["FolderOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFoldersResponseOut"])
    types["ListTransformationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "transformation": t.array(t.proxy(renames["TransformationIn"])).optional(),
        }
    ).named(renames["ListTransformationsResponseIn"])
    types["ListTransformationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "transformation": t.array(t.proxy(renames["TransformationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTransformationsResponseOut"])
    types["CustomTemplateIn"] = t.struct(
        {
            "workspaceId": t.string().optional(),
            "name": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "templateData": t.string().optional(),
            "galleryReference": t.proxy(renames["GalleryReferenceIn"]).optional(),
            "accountId": t.string().optional(),
            "path": t.string().optional(),
            "templateId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "containerId": t.string().optional(),
        }
    ).named(renames["CustomTemplateIn"])
    types["CustomTemplateOut"] = t.struct(
        {
            "workspaceId": t.string().optional(),
            "name": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "templateData": t.string().optional(),
            "galleryReference": t.proxy(renames["GalleryReferenceOut"]).optional(),
            "accountId": t.string().optional(),
            "path": t.string().optional(),
            "templateId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "containerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomTemplateOut"])
    types["QuickPreviewResponseIn"] = t.struct(
        {
            "compilerError": t.boolean().optional(),
            "containerVersion": t.proxy(renames["ContainerVersionIn"]).optional(),
            "syncStatus": t.proxy(renames["SyncStatusIn"]).optional(),
        }
    ).named(renames["QuickPreviewResponseIn"])
    types["QuickPreviewResponseOut"] = t.struct(
        {
            "compilerError": t.boolean().optional(),
            "containerVersion": t.proxy(renames["ContainerVersionOut"]).optional(),
            "syncStatus": t.proxy(renames["SyncStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuickPreviewResponseOut"])
    types["ListDestinationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "destination": t.array(t.proxy(renames["DestinationIn"])).optional(),
        }
    ).named(renames["ListDestinationsResponseIn"])
    types["ListDestinationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "destination": t.array(t.proxy(renames["DestinationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDestinationsResponseOut"])
    types["TagConsentSettingIn"] = t.struct(
        {
            "consentStatus": t.string().optional(),
            "consentType": t.proxy(renames["ParameterIn"]).optional(),
        }
    ).named(renames["TagConsentSettingIn"])
    types["TagConsentSettingOut"] = t.struct(
        {
            "consentStatus": t.string().optional(),
            "consentType": t.proxy(renames["ParameterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagConsentSettingOut"])
    types["RevertClientResponseIn"] = t.struct(
        {"client": t.proxy(renames["ClientIn"]).optional()}
    ).named(renames["RevertClientResponseIn"])
    types["RevertClientResponseOut"] = t.struct(
        {
            "client": t.proxy(renames["ClientOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertClientResponseOut"])
    types["DestinationIn"] = t.struct(
        {
            "path": t.string().optional(),
            "fingerprint": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "accountId": t.string().optional(),
            "containerId": t.string().optional(),
            "destinationId": t.string().optional(),
            "destinationLinkId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DestinationIn"])
    types["DestinationOut"] = t.struct(
        {
            "path": t.string().optional(),
            "fingerprint": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "accountId": t.string().optional(),
            "containerId": t.string().optional(),
            "destinationId": t.string().optional(),
            "destinationLinkId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationOut"])
    types["ContainerAccessIn"] = t.struct(
        {"containerId": t.string().optional(), "permission": t.string().optional()}
    ).named(renames["ContainerAccessIn"])
    types["ContainerAccessOut"] = t.struct(
        {
            "containerId": t.string().optional(),
            "permission": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerAccessOut"])
    types["ConditionIn"] = t.struct(
        {
            "type": t.string().optional(),
            "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
        }
    ).named(renames["ConditionIn"])
    types["ConditionOut"] = t.struct(
        {
            "type": t.string().optional(),
            "parameter": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionOut"])
    types["ZoneTypeRestrictionIn"] = t.struct(
        {
            "whitelistedTypeId": t.array(t.string()).optional(),
            "enable": t.boolean().optional(),
        }
    ).named(renames["ZoneTypeRestrictionIn"])
    types["ZoneTypeRestrictionOut"] = t.struct(
        {
            "whitelistedTypeId": t.array(t.string()).optional(),
            "enable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZoneTypeRestrictionOut"])
    types["ZoneBoundaryIn"] = t.struct(
        {
            "customEvaluationTriggerId": t.array(t.string()).optional(),
            "condition": t.array(t.proxy(renames["ConditionIn"])).optional(),
        }
    ).named(renames["ZoneBoundaryIn"])
    types["ZoneBoundaryOut"] = t.struct(
        {
            "customEvaluationTriggerId": t.array(t.string()).optional(),
            "condition": t.array(t.proxy(renames["ConditionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZoneBoundaryOut"])
    types["GalleryReferenceIn"] = t.struct(
        {
            "signature": t.string().optional(),
            "version": t.string().optional(),
            "owner": t.string().optional(),
            "host": t.string().optional(),
            "repository": t.string().optional(),
            "isModified": t.boolean().optional(),
        }
    ).named(renames["GalleryReferenceIn"])
    types["GalleryReferenceOut"] = t.struct(
        {
            "signature": t.string().optional(),
            "version": t.string().optional(),
            "owner": t.string().optional(),
            "host": t.string().optional(),
            "repository": t.string().optional(),
            "isModified": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GalleryReferenceOut"])
    types["TagIn"] = t.struct(
        {
            "workspaceId": t.string().optional(),
            "consentSettings": t.proxy(renames["TagConsentSettingIn"]).optional(),
            "blockingTriggerId": t.array(t.string()).optional(),
            "tagFiringOption": t.string().optional(),
            "monitoringMetadata": t.proxy(renames["ParameterIn"]).optional(),
            "tagManagerUrl": t.string().optional(),
            "teardownTag": t.array(t.proxy(renames["TeardownTagIn"])).optional(),
            "liveOnly": t.boolean().optional(),
            "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
            "priority": t.proxy(renames["ParameterIn"]).optional(),
            "name": t.string().optional(),
            "notes": t.string().optional(),
            "fingerprint": t.string().optional(),
            "firingRuleId": t.array(t.string()).optional(),
            "scheduleEndMs": t.string().optional(),
            "blockingRuleId": t.array(t.string()).optional(),
            "tagId": t.string().optional(),
            "firingTriggerId": t.array(t.string()).optional(),
            "parentFolderId": t.string().optional(),
            "paused": t.boolean().optional(),
            "setupTag": t.array(t.proxy(renames["SetupTagIn"])).optional(),
            "path": t.string().optional(),
            "type": t.string().optional(),
            "scheduleStartMs": t.string().optional(),
            "monitoringMetadataTagNameKey": t.string().optional(),
            "accountId": t.string().optional(),
            "containerId": t.string().optional(),
        }
    ).named(renames["TagIn"])
    types["TagOut"] = t.struct(
        {
            "workspaceId": t.string().optional(),
            "consentSettings": t.proxy(renames["TagConsentSettingOut"]).optional(),
            "blockingTriggerId": t.array(t.string()).optional(),
            "tagFiringOption": t.string().optional(),
            "monitoringMetadata": t.proxy(renames["ParameterOut"]).optional(),
            "tagManagerUrl": t.string().optional(),
            "teardownTag": t.array(t.proxy(renames["TeardownTagOut"])).optional(),
            "liveOnly": t.boolean().optional(),
            "parameter": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "priority": t.proxy(renames["ParameterOut"]).optional(),
            "name": t.string().optional(),
            "notes": t.string().optional(),
            "fingerprint": t.string().optional(),
            "firingRuleId": t.array(t.string()).optional(),
            "scheduleEndMs": t.string().optional(),
            "blockingRuleId": t.array(t.string()).optional(),
            "tagId": t.string().optional(),
            "firingTriggerId": t.array(t.string()).optional(),
            "parentFolderId": t.string().optional(),
            "paused": t.boolean().optional(),
            "setupTag": t.array(t.proxy(renames["SetupTagOut"])).optional(),
            "path": t.string().optional(),
            "type": t.string().optional(),
            "scheduleStartMs": t.string().optional(),
            "monitoringMetadataTagNameKey": t.string().optional(),
            "accountId": t.string().optional(),
            "containerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagOut"])
    types["ListTemplatesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "template": t.array(t.proxy(renames["CustomTemplateIn"])).optional(),
        }
    ).named(renames["ListTemplatesResponseIn"])
    types["ListTemplatesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "template": t.array(t.proxy(renames["CustomTemplateOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTemplatesResponseOut"])
    types["TriggerIn"] = t.struct(
        {
            "eventName": t.proxy(renames["ParameterIn"]).optional(),
            "visibilitySelector": t.proxy(renames["ParameterIn"]).optional(),
            "containerId": t.string().optional(),
            "interval": t.proxy(renames["ParameterIn"]).optional(),
            "verticalScrollPercentageList": t.proxy(renames["ParameterIn"]).optional(),
            "checkValidation": t.proxy(renames["ParameterIn"]).optional(),
            "parentFolderId": t.string().optional(),
            "waitForTags": t.proxy(renames["ParameterIn"]).optional(),
            "selector": t.proxy(renames["ParameterIn"]).optional(),
            "totalTimeMinMilliseconds": t.proxy(renames["ParameterIn"]).optional(),
            "customEventFilter": t.array(t.proxy(renames["ConditionIn"])).optional(),
            "filter": t.array(t.proxy(renames["ConditionIn"])).optional(),
            "workspaceId": t.string().optional(),
            "uniqueTriggerId": t.proxy(renames["ParameterIn"]).optional(),
            "continuousTimeMinMilliseconds": t.proxy(renames["ParameterIn"]).optional(),
            "maxTimerLengthSeconds": t.proxy(renames["ParameterIn"]).optional(),
            "triggerId": t.string().optional(),
            "horizontalScrollPercentageList": t.proxy(
                renames["ParameterIn"]
            ).optional(),
            "intervalSeconds": t.proxy(renames["ParameterIn"]).optional(),
            "name": t.string().optional(),
            "waitForTagsTimeout": t.proxy(renames["ParameterIn"]).optional(),
            "limit": t.proxy(renames["ParameterIn"]).optional(),
            "path": t.string().optional(),
            "accountId": t.string().optional(),
            "type": t.string().optional(),
            "visiblePercentageMin": t.proxy(renames["ParameterIn"]).optional(),
            "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
            "notes": t.string().optional(),
            "fingerprint": t.string().optional(),
            "autoEventFilter": t.array(t.proxy(renames["ConditionIn"])).optional(),
            "visiblePercentageMax": t.proxy(renames["ParameterIn"]).optional(),
            "tagManagerUrl": t.string().optional(),
        }
    ).named(renames["TriggerIn"])
    types["TriggerOut"] = t.struct(
        {
            "eventName": t.proxy(renames["ParameterOut"]).optional(),
            "visibilitySelector": t.proxy(renames["ParameterOut"]).optional(),
            "containerId": t.string().optional(),
            "interval": t.proxy(renames["ParameterOut"]).optional(),
            "verticalScrollPercentageList": t.proxy(renames["ParameterOut"]).optional(),
            "checkValidation": t.proxy(renames["ParameterOut"]).optional(),
            "parentFolderId": t.string().optional(),
            "waitForTags": t.proxy(renames["ParameterOut"]).optional(),
            "selector": t.proxy(renames["ParameterOut"]).optional(),
            "totalTimeMinMilliseconds": t.proxy(renames["ParameterOut"]).optional(),
            "customEventFilter": t.array(t.proxy(renames["ConditionOut"])).optional(),
            "filter": t.array(t.proxy(renames["ConditionOut"])).optional(),
            "workspaceId": t.string().optional(),
            "uniqueTriggerId": t.proxy(renames["ParameterOut"]).optional(),
            "continuousTimeMinMilliseconds": t.proxy(
                renames["ParameterOut"]
            ).optional(),
            "maxTimerLengthSeconds": t.proxy(renames["ParameterOut"]).optional(),
            "triggerId": t.string().optional(),
            "horizontalScrollPercentageList": t.proxy(
                renames["ParameterOut"]
            ).optional(),
            "intervalSeconds": t.proxy(renames["ParameterOut"]).optional(),
            "name": t.string().optional(),
            "waitForTagsTimeout": t.proxy(renames["ParameterOut"]).optional(),
            "limit": t.proxy(renames["ParameterOut"]).optional(),
            "path": t.string().optional(),
            "accountId": t.string().optional(),
            "type": t.string().optional(),
            "visiblePercentageMin": t.proxy(renames["ParameterOut"]).optional(),
            "parameter": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "notes": t.string().optional(),
            "fingerprint": t.string().optional(),
            "autoEventFilter": t.array(t.proxy(renames["ConditionOut"])).optional(),
            "visiblePercentageMax": t.proxy(renames["ParameterOut"]).optional(),
            "tagManagerUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerOut"])
    types["ContainerVersionIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "builtInVariable": t.array(
                t.proxy(renames["BuiltInVariableIn"])
            ).optional(),
            "trigger": t.array(t.proxy(renames["TriggerIn"])).optional(),
            "folder": t.array(t.proxy(renames["FolderIn"])).optional(),
            "zone": t.array(t.proxy(renames["ZoneIn"])).optional(),
            "containerVersionId": t.string().optional(),
            "customTemplate": t.array(t.proxy(renames["CustomTemplateIn"])).optional(),
            "variable": t.array(t.proxy(renames["VariableIn"])).optional(),
            "container": t.proxy(renames["ContainerIn"]).optional(),
            "gtagConfig": t.array(t.proxy(renames["GtagConfigIn"])).optional(),
            "tagManagerUrl": t.string().optional(),
            "containerId": t.string().optional(),
            "tag": t.array(t.proxy(renames["TagIn"])).optional(),
            "description": t.string().optional(),
            "path": t.string().optional(),
            "deleted": t.boolean().optional(),
            "name": t.string().optional(),
            "fingerprint": t.string().optional(),
            "client": t.array(t.proxy(renames["ClientIn"])).optional(),
            "transformation": t.array(t.proxy(renames["TransformationIn"])).optional(),
        }
    ).named(renames["ContainerVersionIn"])
    types["ContainerVersionOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "builtInVariable": t.array(
                t.proxy(renames["BuiltInVariableOut"])
            ).optional(),
            "trigger": t.array(t.proxy(renames["TriggerOut"])).optional(),
            "folder": t.array(t.proxy(renames["FolderOut"])).optional(),
            "zone": t.array(t.proxy(renames["ZoneOut"])).optional(),
            "containerVersionId": t.string().optional(),
            "customTemplate": t.array(t.proxy(renames["CustomTemplateOut"])).optional(),
            "variable": t.array(t.proxy(renames["VariableOut"])).optional(),
            "container": t.proxy(renames["ContainerOut"]).optional(),
            "gtagConfig": t.array(t.proxy(renames["GtagConfigOut"])).optional(),
            "tagManagerUrl": t.string().optional(),
            "containerId": t.string().optional(),
            "tag": t.array(t.proxy(renames["TagOut"])).optional(),
            "description": t.string().optional(),
            "path": t.string().optional(),
            "deleted": t.boolean().optional(),
            "name": t.string().optional(),
            "fingerprint": t.string().optional(),
            "client": t.array(t.proxy(renames["ClientOut"])).optional(),
            "transformation": t.array(t.proxy(renames["TransformationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerVersionOut"])
    types["ListWorkspacesResponseIn"] = t.struct(
        {
            "workspace": t.array(t.proxy(renames["WorkspaceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListWorkspacesResponseIn"])
    types["ListWorkspacesResponseOut"] = t.struct(
        {
            "workspace": t.array(t.proxy(renames["WorkspaceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkspacesResponseOut"])
    types["ListContainersResponseIn"] = t.struct(
        {
            "container": t.array(t.proxy(renames["ContainerIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListContainersResponseIn"])
    types["ListContainersResponseOut"] = t.struct(
        {
            "container": t.array(t.proxy(renames["ContainerOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListContainersResponseOut"])
    types["ClientIn"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "path": t.string().optional(),
            "containerId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "workspaceId": t.string().optional(),
            "parentFolderId": t.string().optional(),
            "priority": t.integer().optional(),
            "clientId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
            "notes": t.string().optional(),
        }
    ).named(renames["ClientIn"])
    types["ClientOut"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "path": t.string().optional(),
            "containerId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "workspaceId": t.string().optional(),
            "parentFolderId": t.string().optional(),
            "priority": t.integer().optional(),
            "clientId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "parameter": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "notes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientOut"])
    types["RevertFolderResponseIn"] = t.struct(
        {"folder": t.proxy(renames["FolderIn"]).optional()}
    ).named(renames["RevertFolderResponseIn"])
    types["RevertFolderResponseOut"] = t.struct(
        {
            "folder": t.proxy(renames["FolderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertFolderResponseOut"])
    types["CreateBuiltInVariableResponseIn"] = t.struct(
        {"builtInVariable": t.array(t.proxy(renames["BuiltInVariableIn"])).optional()}
    ).named(renames["CreateBuiltInVariableResponseIn"])
    types["CreateBuiltInVariableResponseOut"] = t.struct(
        {
            "builtInVariable": t.array(
                t.proxy(renames["BuiltInVariableOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateBuiltInVariableResponseOut"])
    types["ZoneChildContainerIn"] = t.struct(
        {"nickname": t.string().optional(), "publicId": t.string().optional()}
    ).named(renames["ZoneChildContainerIn"])
    types["ZoneChildContainerOut"] = t.struct(
        {
            "nickname": t.string().optional(),
            "publicId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZoneChildContainerOut"])
    types["ZoneIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "fingerprint": t.string().optional(),
            "name": t.string().optional(),
            "path": t.string().optional(),
            "containerId": t.string().optional(),
            "childContainer": t.array(
                t.proxy(renames["ZoneChildContainerIn"])
            ).optional(),
            "typeRestriction": t.proxy(renames["ZoneTypeRestrictionIn"]).optional(),
            "notes": t.string().optional(),
            "zoneId": t.string().optional(),
            "workspaceId": t.string().optional(),
            "boundary": t.proxy(renames["ZoneBoundaryIn"]).optional(),
        }
    ).named(renames["ZoneIn"])
    types["ZoneOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "fingerprint": t.string().optional(),
            "name": t.string().optional(),
            "path": t.string().optional(),
            "containerId": t.string().optional(),
            "childContainer": t.array(
                t.proxy(renames["ZoneChildContainerOut"])
            ).optional(),
            "typeRestriction": t.proxy(renames["ZoneTypeRestrictionOut"]).optional(),
            "notes": t.string().optional(),
            "zoneId": t.string().optional(),
            "workspaceId": t.string().optional(),
            "boundary": t.proxy(renames["ZoneBoundaryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZoneOut"])
    types["RevertZoneResponseIn"] = t.struct(
        {"zone": t.proxy(renames["ZoneIn"]).optional()}
    ).named(renames["RevertZoneResponseIn"])
    types["RevertZoneResponseOut"] = t.struct(
        {
            "zone": t.proxy(renames["ZoneOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertZoneResponseOut"])
    types["ListGtagConfigResponseIn"] = t.struct(
        {
            "gtagConfig": t.array(t.proxy(renames["GtagConfigIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListGtagConfigResponseIn"])
    types["ListGtagConfigResponseOut"] = t.struct(
        {
            "gtagConfig": t.array(t.proxy(renames["GtagConfigOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGtagConfigResponseOut"])
    types["RevertTemplateResponseIn"] = t.struct(
        {"template": t.proxy(renames["CustomTemplateIn"]).optional()}
    ).named(renames["RevertTemplateResponseIn"])
    types["RevertTemplateResponseOut"] = t.struct(
        {
            "template": t.proxy(renames["CustomTemplateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertTemplateResponseOut"])
    types["ListEnabledBuiltInVariablesResponseIn"] = t.struct(
        {
            "builtInVariable": t.array(
                t.proxy(renames["BuiltInVariableIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListEnabledBuiltInVariablesResponseIn"])
    types["ListEnabledBuiltInVariablesResponseOut"] = t.struct(
        {
            "builtInVariable": t.array(
                t.proxy(renames["BuiltInVariableOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEnabledBuiltInVariablesResponseOut"])
    types["RevertVariableResponseIn"] = t.struct(
        {"variable": t.proxy(renames["VariableIn"]).optional()}
    ).named(renames["RevertVariableResponseIn"])
    types["RevertVariableResponseOut"] = t.struct(
        {
            "variable": t.proxy(renames["VariableOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertVariableResponseOut"])
    types["GetContainerSnippetResponseIn"] = t.struct(
        {"snippet": t.string().optional()}
    ).named(renames["GetContainerSnippetResponseIn"])
    types["GetContainerSnippetResponseOut"] = t.struct(
        {
            "snippet": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetContainerSnippetResponseOut"])
    types["AccountFeaturesIn"] = t.struct(
        {
            "supportUserPermissions": t.boolean().optional(),
            "supportMultipleContainers": t.boolean().optional(),
        }
    ).named(renames["AccountFeaturesIn"])
    types["AccountFeaturesOut"] = t.struct(
        {
            "supportUserPermissions": t.boolean().optional(),
            "supportMultipleContainers": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountFeaturesOut"])
    types["SyncWorkspaceResponseIn"] = t.struct(
        {
            "syncStatus": t.proxy(renames["SyncStatusIn"]).optional(),
            "mergeConflict": t.array(t.proxy(renames["MergeConflictIn"])).optional(),
        }
    ).named(renames["SyncWorkspaceResponseIn"])
    types["SyncWorkspaceResponseOut"] = t.struct(
        {
            "syncStatus": t.proxy(renames["SyncStatusOut"]).optional(),
            "mergeConflict": t.array(t.proxy(renames["MergeConflictOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SyncWorkspaceResponseOut"])
    types["RevertBuiltInVariableResponseIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["RevertBuiltInVariableResponseIn"])
    types["RevertBuiltInVariableResponseOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertBuiltInVariableResponseOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "containerId": t.string().optional(),
            "path": t.string().optional(),
            "workspaceId": t.string().optional(),
            "environmentId": t.string().optional(),
            "url": t.string().optional(),
            "fingerprint": t.string().optional(),
            "authorizationCode": t.string().optional(),
            "description": t.string().optional(),
            "authorizationTimestamp": t.string().optional(),
            "enableDebug": t.boolean().optional(),
            "tagManagerUrl": t.string().optional(),
            "containerVersionId": t.string().optional(),
            "accountId": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "containerId": t.string().optional(),
            "path": t.string().optional(),
            "workspaceId": t.string().optional(),
            "environmentId": t.string().optional(),
            "url": t.string().optional(),
            "fingerprint": t.string().optional(),
            "authorizationCode": t.string().optional(),
            "description": t.string().optional(),
            "authorizationTimestamp": t.string().optional(),
            "enableDebug": t.boolean().optional(),
            "tagManagerUrl": t.string().optional(),
            "containerVersionId": t.string().optional(),
            "accountId": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["PublishContainerVersionResponseIn"] = t.struct(
        {
            "compilerError": t.boolean().optional(),
            "containerVersion": t.proxy(renames["ContainerVersionIn"]).optional(),
        }
    ).named(renames["PublishContainerVersionResponseIn"])
    types["PublishContainerVersionResponseOut"] = t.struct(
        {
            "compilerError": t.boolean().optional(),
            "containerVersion": t.proxy(renames["ContainerVersionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishContainerVersionResponseOut"])

    functions = {}
    functions["accountsGet"] = tagmanager.get(
        "tagmanager/v2/accounts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "includeGoogleTags": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsUpdate"] = tagmanager.get(
        "tagmanager/v2/accounts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "includeGoogleTags": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsList"] = tagmanager.get(
        "tagmanager/v2/accounts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "includeGoogleTags": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsUser_permissionsGet"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "accountId": t.string().optional(),
                "emailAddress": t.string().optional(),
                "containerAccess": t.array(
                    t.proxy(renames["ContainerAccessIn"])
                ).optional(),
                "accountAccess": t.proxy(renames["AccountAccessIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsUser_permissionsList"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "accountId": t.string().optional(),
                "emailAddress": t.string().optional(),
                "containerAccess": t.array(
                    t.proxy(renames["ContainerAccessIn"])
                ).optional(),
                "accountAccess": t.proxy(renames["AccountAccessIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsUser_permissionsCreate"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "accountId": t.string().optional(),
                "emailAddress": t.string().optional(),
                "containerAccess": t.array(
                    t.proxy(renames["ContainerAccessIn"])
                ).optional(),
                "accountAccess": t.proxy(renames["AccountAccessIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsUser_permissionsDelete"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "accountId": t.string().optional(),
                "emailAddress": t.string().optional(),
                "containerAccess": t.array(
                    t.proxy(renames["ContainerAccessIn"])
                ).optional(),
                "accountAccess": t.proxy(renames["AccountAccessIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsUser_permissionsUpdate"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "accountId": t.string().optional(),
                "emailAddress": t.string().optional(),
                "containerAccess": t.array(
                    t.proxy(renames["ContainerAccessIn"])
                ).optional(),
                "accountAccess": t.proxy(renames["AccountAccessIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersList"] = tagmanager.post(
        "tagmanager/v2/{parent}/containers",
        t.struct(
            {
                "parent": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "domainName": t.array(t.string()).optional(),
                "fingerprint": t.string().optional(),
                "usageContext": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "taggingServerUrls": t.array(t.string()).optional(),
                "path": t.string().optional(),
                "notes": t.string().optional(),
                "containerId": t.string().optional(),
                "tagIds": t.array(t.string()).optional(),
                "features": t.proxy(renames["ContainerFeaturesIn"]).optional(),
                "publicId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContainerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersMove_tag_id"] = tagmanager.post(
        "tagmanager/v2/{parent}/containers",
        t.struct(
            {
                "parent": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "domainName": t.array(t.string()).optional(),
                "fingerprint": t.string().optional(),
                "usageContext": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "taggingServerUrls": t.array(t.string()).optional(),
                "path": t.string().optional(),
                "notes": t.string().optional(),
                "containerId": t.string().optional(),
                "tagIds": t.array(t.string()).optional(),
                "features": t.proxy(renames["ContainerFeaturesIn"]).optional(),
                "publicId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContainerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersGet"] = tagmanager.post(
        "tagmanager/v2/{parent}/containers",
        t.struct(
            {
                "parent": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "domainName": t.array(t.string()).optional(),
                "fingerprint": t.string().optional(),
                "usageContext": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "taggingServerUrls": t.array(t.string()).optional(),
                "path": t.string().optional(),
                "notes": t.string().optional(),
                "containerId": t.string().optional(),
                "tagIds": t.array(t.string()).optional(),
                "features": t.proxy(renames["ContainerFeaturesIn"]).optional(),
                "publicId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContainerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersUpdate"] = tagmanager.post(
        "tagmanager/v2/{parent}/containers",
        t.struct(
            {
                "parent": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "domainName": t.array(t.string()).optional(),
                "fingerprint": t.string().optional(),
                "usageContext": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "taggingServerUrls": t.array(t.string()).optional(),
                "path": t.string().optional(),
                "notes": t.string().optional(),
                "containerId": t.string().optional(),
                "tagIds": t.array(t.string()).optional(),
                "features": t.proxy(renames["ContainerFeaturesIn"]).optional(),
                "publicId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContainerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersSnippet"] = tagmanager.post(
        "tagmanager/v2/{parent}/containers",
        t.struct(
            {
                "parent": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "domainName": t.array(t.string()).optional(),
                "fingerprint": t.string().optional(),
                "usageContext": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "taggingServerUrls": t.array(t.string()).optional(),
                "path": t.string().optional(),
                "notes": t.string().optional(),
                "containerId": t.string().optional(),
                "tagIds": t.array(t.string()).optional(),
                "features": t.proxy(renames["ContainerFeaturesIn"]).optional(),
                "publicId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContainerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersCombine"] = tagmanager.post(
        "tagmanager/v2/{parent}/containers",
        t.struct(
            {
                "parent": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "domainName": t.array(t.string()).optional(),
                "fingerprint": t.string().optional(),
                "usageContext": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "taggingServerUrls": t.array(t.string()).optional(),
                "path": t.string().optional(),
                "notes": t.string().optional(),
                "containerId": t.string().optional(),
                "tagIds": t.array(t.string()).optional(),
                "features": t.proxy(renames["ContainerFeaturesIn"]).optional(),
                "publicId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContainerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersDelete"] = tagmanager.post(
        "tagmanager/v2/{parent}/containers",
        t.struct(
            {
                "parent": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "domainName": t.array(t.string()).optional(),
                "fingerprint": t.string().optional(),
                "usageContext": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "taggingServerUrls": t.array(t.string()).optional(),
                "path": t.string().optional(),
                "notes": t.string().optional(),
                "containerId": t.string().optional(),
                "tagIds": t.array(t.string()).optional(),
                "features": t.proxy(renames["ContainerFeaturesIn"]).optional(),
                "publicId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContainerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersLookup"] = tagmanager.post(
        "tagmanager/v2/{parent}/containers",
        t.struct(
            {
                "parent": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "domainName": t.array(t.string()).optional(),
                "fingerprint": t.string().optional(),
                "usageContext": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "taggingServerUrls": t.array(t.string()).optional(),
                "path": t.string().optional(),
                "notes": t.string().optional(),
                "containerId": t.string().optional(),
                "tagIds": t.array(t.string()).optional(),
                "features": t.proxy(renames["ContainerFeaturesIn"]).optional(),
                "publicId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContainerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersCreate"] = tagmanager.post(
        "tagmanager/v2/{parent}/containers",
        t.struct(
            {
                "parent": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "domainName": t.array(t.string()).optional(),
                "fingerprint": t.string().optional(),
                "usageContext": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "taggingServerUrls": t.array(t.string()).optional(),
                "path": t.string().optional(),
                "notes": t.string().optional(),
                "containerId": t.string().optional(),
                "tagIds": t.array(t.string()).optional(),
                "features": t.proxy(renames["ContainerFeaturesIn"]).optional(),
                "publicId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContainerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersEnvironmentsDelete"] = tagmanager.get(
        "tagmanager/v2/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnvironmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersEnvironmentsUpdate"] = tagmanager.get(
        "tagmanager/v2/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnvironmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersEnvironmentsReauthorize"] = tagmanager.get(
        "tagmanager/v2/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnvironmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersEnvironmentsCreate"] = tagmanager.get(
        "tagmanager/v2/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnvironmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersEnvironmentsGet"] = tagmanager.get(
        "tagmanager/v2/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnvironmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersEnvironmentsList"] = tagmanager.get(
        "tagmanager/v2/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnvironmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesSync"] = tagmanager.post(
        "tagmanager/v2/{path}:resolve_conflict",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
                "transformation": t.proxy(renames["TransformationIn"]).optional(),
                "changeStatus": t.string().optional(),
                "variable": t.proxy(renames["VariableIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesCreate"] = tagmanager.post(
        "tagmanager/v2/{path}:resolve_conflict",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
                "transformation": t.proxy(renames["TransformationIn"]).optional(),
                "changeStatus": t.string().optional(),
                "variable": t.proxy(renames["VariableIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesCreate_version"] = tagmanager.post(
        "tagmanager/v2/{path}:resolve_conflict",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
                "transformation": t.proxy(renames["TransformationIn"]).optional(),
                "changeStatus": t.string().optional(),
                "variable": t.proxy(renames["VariableIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesList"] = tagmanager.post(
        "tagmanager/v2/{path}:resolve_conflict",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
                "transformation": t.proxy(renames["TransformationIn"]).optional(),
                "changeStatus": t.string().optional(),
                "variable": t.proxy(renames["VariableIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesGet"] = tagmanager.post(
        "tagmanager/v2/{path}:resolve_conflict",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
                "transformation": t.proxy(renames["TransformationIn"]).optional(),
                "changeStatus": t.string().optional(),
                "variable": t.proxy(renames["VariableIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesGetStatus"] = tagmanager.post(
        "tagmanager/v2/{path}:resolve_conflict",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
                "transformation": t.proxy(renames["TransformationIn"]).optional(),
                "changeStatus": t.string().optional(),
                "variable": t.proxy(renames["VariableIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesQuick_preview"] = tagmanager.post(
        "tagmanager/v2/{path}:resolve_conflict",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
                "transformation": t.proxy(renames["TransformationIn"]).optional(),
                "changeStatus": t.string().optional(),
                "variable": t.proxy(renames["VariableIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesDelete"] = tagmanager.post(
        "tagmanager/v2/{path}:resolve_conflict",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
                "transformation": t.proxy(renames["TransformationIn"]).optional(),
                "changeStatus": t.string().optional(),
                "variable": t.proxy(renames["VariableIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesUpdate"] = tagmanager.post(
        "tagmanager/v2/{path}:resolve_conflict",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
                "transformation": t.proxy(renames["TransformationIn"]).optional(),
                "changeStatus": t.string().optional(),
                "variable": t.proxy(renames["VariableIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesResolve_conflict"] = tagmanager.post(
        "tagmanager/v2/{path}:resolve_conflict",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
                "transformation": t.proxy(renames["TransformationIn"]).optional(),
                "changeStatus": t.string().optional(),
                "variable": t.proxy(renames["VariableIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesBuilt_in_variablesList"] = tagmanager.post(
        "tagmanager/v2/{path}/built_in_variables:revert",
        t.struct(
            {
                "path": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertBuiltInVariableResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesBuilt_in_variablesCreate"] = tagmanager.post(
        "tagmanager/v2/{path}/built_in_variables:revert",
        t.struct(
            {
                "path": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertBuiltInVariableResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesBuilt_in_variablesDelete"] = tagmanager.post(
        "tagmanager/v2/{path}/built_in_variables:revert",
        t.struct(
            {
                "path": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertBuiltInVariableResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesBuilt_in_variablesRevert"] = tagmanager.post(
        "tagmanager/v2/{path}/built_in_variables:revert",
        t.struct(
            {
                "path": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertBuiltInVariableResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTriggersUpdate"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["TriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTriggersRevert"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["TriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTriggersCreate"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["TriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTriggersList"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["TriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTriggersDelete"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["TriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTriggersGet"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["TriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTagsDelete"] = tagmanager.post(
        "tagmanager/v2/{path}:revert",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertTagResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTagsUpdate"] = tagmanager.post(
        "tagmanager/v2/{path}:revert",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertTagResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTagsList"] = tagmanager.post(
        "tagmanager/v2/{path}:revert",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertTagResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTagsGet"] = tagmanager.post(
        "tagmanager/v2/{path}:revert",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertTagResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTagsCreate"] = tagmanager.post(
        "tagmanager/v2/{path}:revert",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertTagResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTagsRevert"] = tagmanager.post(
        "tagmanager/v2/{path}:revert",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertTagResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTransformationsDelete"] = tagmanager.post(
        "tagmanager/v2/{parent}/transformations",
        t.struct(
            {
                "parent": t.string().optional(),
                "type": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "fingerprint": t.string().optional(),
                "transformationId": t.string().optional(),
                "path": t.string().optional(),
                "parentFolderId": t.string().optional(),
                "containerId": t.string().optional(),
                "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
                "notes": t.string().optional(),
                "workspaceId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransformationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTransformationsUpdate"] = tagmanager.post(
        "tagmanager/v2/{parent}/transformations",
        t.struct(
            {
                "parent": t.string().optional(),
                "type": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "fingerprint": t.string().optional(),
                "transformationId": t.string().optional(),
                "path": t.string().optional(),
                "parentFolderId": t.string().optional(),
                "containerId": t.string().optional(),
                "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
                "notes": t.string().optional(),
                "workspaceId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransformationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTransformationsRevert"] = tagmanager.post(
        "tagmanager/v2/{parent}/transformations",
        t.struct(
            {
                "parent": t.string().optional(),
                "type": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "fingerprint": t.string().optional(),
                "transformationId": t.string().optional(),
                "path": t.string().optional(),
                "parentFolderId": t.string().optional(),
                "containerId": t.string().optional(),
                "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
                "notes": t.string().optional(),
                "workspaceId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransformationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTransformationsGet"] = tagmanager.post(
        "tagmanager/v2/{parent}/transformations",
        t.struct(
            {
                "parent": t.string().optional(),
                "type": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "fingerprint": t.string().optional(),
                "transformationId": t.string().optional(),
                "path": t.string().optional(),
                "parentFolderId": t.string().optional(),
                "containerId": t.string().optional(),
                "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
                "notes": t.string().optional(),
                "workspaceId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransformationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTransformationsList"] = tagmanager.post(
        "tagmanager/v2/{parent}/transformations",
        t.struct(
            {
                "parent": t.string().optional(),
                "type": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "fingerprint": t.string().optional(),
                "transformationId": t.string().optional(),
                "path": t.string().optional(),
                "parentFolderId": t.string().optional(),
                "containerId": t.string().optional(),
                "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
                "notes": t.string().optional(),
                "workspaceId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransformationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTransformationsCreate"] = tagmanager.post(
        "tagmanager/v2/{parent}/transformations",
        t.struct(
            {
                "parent": t.string().optional(),
                "type": t.string().optional(),
                "name": t.string().optional(),
                "accountId": t.string().optional(),
                "fingerprint": t.string().optional(),
                "transformationId": t.string().optional(),
                "path": t.string().optional(),
                "parentFolderId": t.string().optional(),
                "containerId": t.string().optional(),
                "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
                "notes": t.string().optional(),
                "workspaceId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransformationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesClientsRevert"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesClientsCreate"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesClientsUpdate"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesClientsList"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesClientsDelete"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesClientsGet"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesGtag_configUpdate"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GtagConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesGtag_configList"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GtagConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesGtag_configCreate"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GtagConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesGtag_configDelete"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GtagConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesGtag_configGet"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GtagConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesZonesGet"] = tagmanager.delete(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesZonesUpdate"] = tagmanager.delete(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesZonesRevert"] = tagmanager.delete(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesZonesCreate"] = tagmanager.delete(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesZonesList"] = tagmanager.delete(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesZonesDelete"] = tagmanager.delete(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTemplatesDelete"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CustomTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTemplatesUpdate"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CustomTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTemplatesList"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CustomTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTemplatesCreate"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CustomTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTemplatesRevert"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CustomTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTemplatesGet"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CustomTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesFoldersUpdate"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesFoldersEntities"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesFoldersRevert"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesFoldersDelete"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesFoldersCreate"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesFoldersList"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "accountsContainersWorkspacesFoldersMove_entities_to_folder"
    ] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesFoldersGet"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesVariablesUpdate"] = tagmanager.get(
        "tagmanager/v2/{parent}/variables",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVariablesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesVariablesCreate"] = tagmanager.get(
        "tagmanager/v2/{parent}/variables",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVariablesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesVariablesGet"] = tagmanager.get(
        "tagmanager/v2/{parent}/variables",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVariablesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesVariablesDelete"] = tagmanager.get(
        "tagmanager/v2/{parent}/variables",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVariablesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesVariablesRevert"] = tagmanager.get(
        "tagmanager/v2/{parent}/variables",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVariablesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesVariablesList"] = tagmanager.get(
        "tagmanager/v2/{parent}/variables",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVariablesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersDestinationsGet"] = tagmanager.post(
        "tagmanager/v2/{parent}/destinations:link",
        t.struct(
            {
                "destinationId": t.string().optional(),
                "parent": t.string().optional(),
                "allowUserPermissionFeatureUpdate": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DestinationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersDestinationsList"] = tagmanager.post(
        "tagmanager/v2/{parent}/destinations:link",
        t.struct(
            {
                "destinationId": t.string().optional(),
                "parent": t.string().optional(),
                "allowUserPermissionFeatureUpdate": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DestinationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersDestinationsLink"] = tagmanager.post(
        "tagmanager/v2/{parent}/destinations:link",
        t.struct(
            {
                "destinationId": t.string().optional(),
                "parent": t.string().optional(),
                "allowUserPermissionFeatureUpdate": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DestinationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersVersion_headersLatest"] = tagmanager.get(
        "tagmanager/v2/{parent}/version_headers",
        t.struct(
            {
                "includeDeleted": t.boolean().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContainerVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersVersion_headersList"] = tagmanager.get(
        "tagmanager/v2/{parent}/version_headers",
        t.struct(
            {
                "includeDeleted": t.boolean().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContainerVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersVersionsLive"] = tagmanager.post(
        "tagmanager/v2/{path}:undelete",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ContainerVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersVersionsGet"] = tagmanager.post(
        "tagmanager/v2/{path}:undelete",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ContainerVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersVersionsPublish"] = tagmanager.post(
        "tagmanager/v2/{path}:undelete",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ContainerVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersVersionsSet_latest"] = tagmanager.post(
        "tagmanager/v2/{path}:undelete",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ContainerVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersVersionsDelete"] = tagmanager.post(
        "tagmanager/v2/{path}:undelete",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ContainerVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersVersionsUpdate"] = tagmanager.post(
        "tagmanager/v2/{path}:undelete",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ContainerVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersVersionsUndelete"] = tagmanager.post(
        "tagmanager/v2/{path}:undelete",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ContainerVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="tagmanager",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
