from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_tagmanager() -> Import:
    tagmanager = HTTPRuntime("https://tagmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_tagmanager_1_ErrorResponse",
        "VariableFormatValueIn": "_tagmanager_2_VariableFormatValueIn",
        "VariableFormatValueOut": "_tagmanager_3_VariableFormatValueOut",
        "CreateBuiltInVariableResponseIn": "_tagmanager_4_CreateBuiltInVariableResponseIn",
        "CreateBuiltInVariableResponseOut": "_tagmanager_5_CreateBuiltInVariableResponseOut",
        "AccountIn": "_tagmanager_6_AccountIn",
        "AccountOut": "_tagmanager_7_AccountOut",
        "ListWorkspacesResponseIn": "_tagmanager_8_ListWorkspacesResponseIn",
        "ListWorkspacesResponseOut": "_tagmanager_9_ListWorkspacesResponseOut",
        "GetContainerSnippetResponseIn": "_tagmanager_10_GetContainerSnippetResponseIn",
        "GetContainerSnippetResponseOut": "_tagmanager_11_GetContainerSnippetResponseOut",
        "ClientIn": "_tagmanager_12_ClientIn",
        "ClientOut": "_tagmanager_13_ClientOut",
        "ZoneIn": "_tagmanager_14_ZoneIn",
        "ZoneOut": "_tagmanager_15_ZoneOut",
        "CustomTemplateIn": "_tagmanager_16_CustomTemplateIn",
        "CustomTemplateOut": "_tagmanager_17_CustomTemplateOut",
        "QuickPreviewResponseIn": "_tagmanager_18_QuickPreviewResponseIn",
        "QuickPreviewResponseOut": "_tagmanager_19_QuickPreviewResponseOut",
        "FolderIn": "_tagmanager_20_FolderIn",
        "FolderOut": "_tagmanager_21_FolderOut",
        "GtagConfigIn": "_tagmanager_22_GtagConfigIn",
        "GtagConfigOut": "_tagmanager_23_GtagConfigOut",
        "ListTemplatesResponseIn": "_tagmanager_24_ListTemplatesResponseIn",
        "ListTemplatesResponseOut": "_tagmanager_25_ListTemplatesResponseOut",
        "TagConsentSettingIn": "_tagmanager_26_TagConsentSettingIn",
        "TagConsentSettingOut": "_tagmanager_27_TagConsentSettingOut",
        "SetupTagIn": "_tagmanager_28_SetupTagIn",
        "SetupTagOut": "_tagmanager_29_SetupTagOut",
        "SyncWorkspaceResponseIn": "_tagmanager_30_SyncWorkspaceResponseIn",
        "SyncWorkspaceResponseOut": "_tagmanager_31_SyncWorkspaceResponseOut",
        "RevertTagResponseIn": "_tagmanager_32_RevertTagResponseIn",
        "RevertTagResponseOut": "_tagmanager_33_RevertTagResponseOut",
        "UserPermissionIn": "_tagmanager_34_UserPermissionIn",
        "UserPermissionOut": "_tagmanager_35_UserPermissionOut",
        "EntityIn": "_tagmanager_36_EntityIn",
        "EntityOut": "_tagmanager_37_EntityOut",
        "ListVariablesResponseIn": "_tagmanager_38_ListVariablesResponseIn",
        "ListVariablesResponseOut": "_tagmanager_39_ListVariablesResponseOut",
        "RevertTemplateResponseIn": "_tagmanager_40_RevertTemplateResponseIn",
        "RevertTemplateResponseOut": "_tagmanager_41_RevertTemplateResponseOut",
        "FolderEntitiesIn": "_tagmanager_42_FolderEntitiesIn",
        "FolderEntitiesOut": "_tagmanager_43_FolderEntitiesOut",
        "ListContainersResponseIn": "_tagmanager_44_ListContainersResponseIn",
        "ListContainersResponseOut": "_tagmanager_45_ListContainersResponseOut",
        "ListTagsResponseIn": "_tagmanager_46_ListTagsResponseIn",
        "ListTagsResponseOut": "_tagmanager_47_ListTagsResponseOut",
        "AccountFeaturesIn": "_tagmanager_48_AccountFeaturesIn",
        "AccountFeaturesOut": "_tagmanager_49_AccountFeaturesOut",
        "ListTriggersResponseIn": "_tagmanager_50_ListTriggersResponseIn",
        "ListTriggersResponseOut": "_tagmanager_51_ListTriggersResponseOut",
        "ListDestinationsResponseIn": "_tagmanager_52_ListDestinationsResponseIn",
        "ListDestinationsResponseOut": "_tagmanager_53_ListDestinationsResponseOut",
        "ContainerVersionIn": "_tagmanager_54_ContainerVersionIn",
        "ContainerVersionOut": "_tagmanager_55_ContainerVersionOut",
        "TagIn": "_tagmanager_56_TagIn",
        "TagOut": "_tagmanager_57_TagOut",
        "ListAccountsResponseIn": "_tagmanager_58_ListAccountsResponseIn",
        "ListAccountsResponseOut": "_tagmanager_59_ListAccountsResponseOut",
        "EnvironmentIn": "_tagmanager_60_EnvironmentIn",
        "EnvironmentOut": "_tagmanager_61_EnvironmentOut",
        "ZoneChildContainerIn": "_tagmanager_62_ZoneChildContainerIn",
        "ZoneChildContainerOut": "_tagmanager_63_ZoneChildContainerOut",
        "ListEnabledBuiltInVariablesResponseIn": "_tagmanager_64_ListEnabledBuiltInVariablesResponseIn",
        "ListEnabledBuiltInVariablesResponseOut": "_tagmanager_65_ListEnabledBuiltInVariablesResponseOut",
        "SyncStatusIn": "_tagmanager_66_SyncStatusIn",
        "SyncStatusOut": "_tagmanager_67_SyncStatusOut",
        "ZoneBoundaryIn": "_tagmanager_68_ZoneBoundaryIn",
        "ZoneBoundaryOut": "_tagmanager_69_ZoneBoundaryOut",
        "PublishContainerVersionResponseIn": "_tagmanager_70_PublishContainerVersionResponseIn",
        "PublishContainerVersionResponseOut": "_tagmanager_71_PublishContainerVersionResponseOut",
        "CreateContainerVersionRequestVersionOptionsIn": "_tagmanager_72_CreateContainerVersionRequestVersionOptionsIn",
        "CreateContainerVersionRequestVersionOptionsOut": "_tagmanager_73_CreateContainerVersionRequestVersionOptionsOut",
        "ListContainerVersionsResponseIn": "_tagmanager_74_ListContainerVersionsResponseIn",
        "ListContainerVersionsResponseOut": "_tagmanager_75_ListContainerVersionsResponseOut",
        "BuiltInVariableIn": "_tagmanager_76_BuiltInVariableIn",
        "BuiltInVariableOut": "_tagmanager_77_BuiltInVariableOut",
        "GalleryReferenceIn": "_tagmanager_78_GalleryReferenceIn",
        "GalleryReferenceOut": "_tagmanager_79_GalleryReferenceOut",
        "ListZonesResponseIn": "_tagmanager_80_ListZonesResponseIn",
        "ListZonesResponseOut": "_tagmanager_81_ListZonesResponseOut",
        "ParameterIn": "_tagmanager_82_ParameterIn",
        "ParameterOut": "_tagmanager_83_ParameterOut",
        "TriggerIn": "_tagmanager_84_TriggerIn",
        "TriggerOut": "_tagmanager_85_TriggerOut",
        "DestinationIn": "_tagmanager_86_DestinationIn",
        "DestinationOut": "_tagmanager_87_DestinationOut",
        "TeardownTagIn": "_tagmanager_88_TeardownTagIn",
        "TeardownTagOut": "_tagmanager_89_TeardownTagOut",
        "ListFoldersResponseIn": "_tagmanager_90_ListFoldersResponseIn",
        "ListFoldersResponseOut": "_tagmanager_91_ListFoldersResponseOut",
        "RevertZoneResponseIn": "_tagmanager_92_RevertZoneResponseIn",
        "RevertZoneResponseOut": "_tagmanager_93_RevertZoneResponseOut",
        "RevertBuiltInVariableResponseIn": "_tagmanager_94_RevertBuiltInVariableResponseIn",
        "RevertBuiltInVariableResponseOut": "_tagmanager_95_RevertBuiltInVariableResponseOut",
        "ListGtagConfigResponseIn": "_tagmanager_96_ListGtagConfigResponseIn",
        "ListGtagConfigResponseOut": "_tagmanager_97_ListGtagConfigResponseOut",
        "ContainerIn": "_tagmanager_98_ContainerIn",
        "ContainerOut": "_tagmanager_99_ContainerOut",
        "ListEnvironmentsResponseIn": "_tagmanager_100_ListEnvironmentsResponseIn",
        "ListEnvironmentsResponseOut": "_tagmanager_101_ListEnvironmentsResponseOut",
        "WorkspaceIn": "_tagmanager_102_WorkspaceIn",
        "WorkspaceOut": "_tagmanager_103_WorkspaceOut",
        "ListUserPermissionsResponseIn": "_tagmanager_104_ListUserPermissionsResponseIn",
        "ListUserPermissionsResponseOut": "_tagmanager_105_ListUserPermissionsResponseOut",
        "CreateContainerVersionResponseIn": "_tagmanager_106_CreateContainerVersionResponseIn",
        "CreateContainerVersionResponseOut": "_tagmanager_107_CreateContainerVersionResponseOut",
        "ZoneTypeRestrictionIn": "_tagmanager_108_ZoneTypeRestrictionIn",
        "ZoneTypeRestrictionOut": "_tagmanager_109_ZoneTypeRestrictionOut",
        "ConditionIn": "_tagmanager_110_ConditionIn",
        "ConditionOut": "_tagmanager_111_ConditionOut",
        "MergeConflictIn": "_tagmanager_112_MergeConflictIn",
        "MergeConflictOut": "_tagmanager_113_MergeConflictOut",
        "RevertFolderResponseIn": "_tagmanager_114_RevertFolderResponseIn",
        "RevertFolderResponseOut": "_tagmanager_115_RevertFolderResponseOut",
        "GetWorkspaceStatusResponseIn": "_tagmanager_116_GetWorkspaceStatusResponseIn",
        "GetWorkspaceStatusResponseOut": "_tagmanager_117_GetWorkspaceStatusResponseOut",
        "ContainerFeaturesIn": "_tagmanager_118_ContainerFeaturesIn",
        "ContainerFeaturesOut": "_tagmanager_119_ContainerFeaturesOut",
        "VariableIn": "_tagmanager_120_VariableIn",
        "VariableOut": "_tagmanager_121_VariableOut",
        "ContainerAccessIn": "_tagmanager_122_ContainerAccessIn",
        "ContainerAccessOut": "_tagmanager_123_ContainerAccessOut",
        "RevertTriggerResponseIn": "_tagmanager_124_RevertTriggerResponseIn",
        "RevertTriggerResponseOut": "_tagmanager_125_RevertTriggerResponseOut",
        "ContainerVersionHeaderIn": "_tagmanager_126_ContainerVersionHeaderIn",
        "ContainerVersionHeaderOut": "_tagmanager_127_ContainerVersionHeaderOut",
        "ListClientsResponseIn": "_tagmanager_128_ListClientsResponseIn",
        "ListClientsResponseOut": "_tagmanager_129_ListClientsResponseOut",
        "RevertVariableResponseIn": "_tagmanager_130_RevertVariableResponseIn",
        "RevertVariableResponseOut": "_tagmanager_131_RevertVariableResponseOut",
        "AccountAccessIn": "_tagmanager_132_AccountAccessIn",
        "AccountAccessOut": "_tagmanager_133_AccountAccessOut",
        "RevertClientResponseIn": "_tagmanager_134_RevertClientResponseIn",
        "RevertClientResponseOut": "_tagmanager_135_RevertClientResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["VariableFormatValueIn"] = t.struct(
        {
            "convertNullToValue": t.proxy(renames["ParameterIn"]).optional(),
            "convertTrueToValue": t.proxy(renames["ParameterIn"]).optional(),
            "convertUndefinedToValue": t.proxy(renames["ParameterIn"]).optional(),
            "convertFalseToValue": t.proxy(renames["ParameterIn"]).optional(),
            "caseConversionType": t.string().optional(),
        }
    ).named(renames["VariableFormatValueIn"])
    types["VariableFormatValueOut"] = t.struct(
        {
            "convertNullToValue": t.proxy(renames["ParameterOut"]).optional(),
            "convertTrueToValue": t.proxy(renames["ParameterOut"]).optional(),
            "convertUndefinedToValue": t.proxy(renames["ParameterOut"]).optional(),
            "convertFalseToValue": t.proxy(renames["ParameterOut"]).optional(),
            "caseConversionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VariableFormatValueOut"])
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
    types["AccountIn"] = t.struct(
        {
            "features": t.proxy(renames["AccountFeaturesIn"]).optional(),
            "accountId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "name": t.string().optional(),
            "shareData": t.boolean().optional(),
            "path": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
        }
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "features": t.proxy(renames["AccountFeaturesOut"]).optional(),
            "accountId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "name": t.string().optional(),
            "shareData": t.boolean().optional(),
            "path": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
    types["ListWorkspacesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "workspace": t.array(t.proxy(renames["WorkspaceIn"])).optional(),
        }
    ).named(renames["ListWorkspacesResponseIn"])
    types["ListWorkspacesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "workspace": t.array(t.proxy(renames["WorkspaceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkspacesResponseOut"])
    types["GetContainerSnippetResponseIn"] = t.struct(
        {"snippet": t.string().optional()}
    ).named(renames["GetContainerSnippetResponseIn"])
    types["GetContainerSnippetResponseOut"] = t.struct(
        {
            "snippet": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetContainerSnippetResponseOut"])
    types["ClientIn"] = t.struct(
        {
            "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
            "accountId": t.string().optional(),
            "parentFolderId": t.string().optional(),
            "priority": t.integer().optional(),
            "containerId": t.string().optional(),
            "notes": t.string().optional(),
            "workspaceId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "name": t.string().optional(),
            "fingerprint": t.string().optional(),
            "path": t.string().optional(),
            "clientId": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ClientIn"])
    types["ClientOut"] = t.struct(
        {
            "parameter": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "accountId": t.string().optional(),
            "parentFolderId": t.string().optional(),
            "priority": t.integer().optional(),
            "containerId": t.string().optional(),
            "notes": t.string().optional(),
            "workspaceId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "name": t.string().optional(),
            "fingerprint": t.string().optional(),
            "path": t.string().optional(),
            "clientId": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientOut"])
    types["ZoneIn"] = t.struct(
        {
            "zoneId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "typeRestriction": t.proxy(renames["ZoneTypeRestrictionIn"]).optional(),
            "path": t.string().optional(),
            "childContainer": t.array(
                t.proxy(renames["ZoneChildContainerIn"])
            ).optional(),
            "accountId": t.string().optional(),
            "notes": t.string().optional(),
            "boundary": t.proxy(renames["ZoneBoundaryIn"]).optional(),
            "name": t.string().optional(),
            "containerId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "workspaceId": t.string().optional(),
        }
    ).named(renames["ZoneIn"])
    types["ZoneOut"] = t.struct(
        {
            "zoneId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "typeRestriction": t.proxy(renames["ZoneTypeRestrictionOut"]).optional(),
            "path": t.string().optional(),
            "childContainer": t.array(
                t.proxy(renames["ZoneChildContainerOut"])
            ).optional(),
            "accountId": t.string().optional(),
            "notes": t.string().optional(),
            "boundary": t.proxy(renames["ZoneBoundaryOut"]).optional(),
            "name": t.string().optional(),
            "containerId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "workspaceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZoneOut"])
    types["CustomTemplateIn"] = t.struct(
        {
            "workspaceId": t.string().optional(),
            "path": t.string().optional(),
            "containerId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "templateId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "templateData": t.string().optional(),
            "galleryReference": t.proxy(renames["GalleryReferenceIn"]).optional(),
            "accountId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CustomTemplateIn"])
    types["CustomTemplateOut"] = t.struct(
        {
            "workspaceId": t.string().optional(),
            "path": t.string().optional(),
            "containerId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "templateId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "templateData": t.string().optional(),
            "galleryReference": t.proxy(renames["GalleryReferenceOut"]).optional(),
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomTemplateOut"])
    types["QuickPreviewResponseIn"] = t.struct(
        {
            "syncStatus": t.proxy(renames["SyncStatusIn"]).optional(),
            "compilerError": t.boolean().optional(),
            "containerVersion": t.proxy(renames["ContainerVersionIn"]).optional(),
        }
    ).named(renames["QuickPreviewResponseIn"])
    types["QuickPreviewResponseOut"] = t.struct(
        {
            "syncStatus": t.proxy(renames["SyncStatusOut"]).optional(),
            "compilerError": t.boolean().optional(),
            "containerVersion": t.proxy(renames["ContainerVersionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuickPreviewResponseOut"])
    types["FolderIn"] = t.struct(
        {
            "folderId": t.string().optional(),
            "path": t.string().optional(),
            "name": t.string().optional(),
            "notes": t.string().optional(),
            "workspaceId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "accountId": t.string().optional(),
            "containerId": t.string().optional(),
            "fingerprint": t.string().optional(),
        }
    ).named(renames["FolderIn"])
    types["FolderOut"] = t.struct(
        {
            "folderId": t.string().optional(),
            "path": t.string().optional(),
            "name": t.string().optional(),
            "notes": t.string().optional(),
            "workspaceId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "accountId": t.string().optional(),
            "containerId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOut"])
    types["GtagConfigIn"] = t.struct(
        {
            "fingerprint": t.string().optional(),
            "path": t.string().optional(),
            "type": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "accountId": t.string().optional(),
            "workspaceId": t.string().optional(),
            "containerId": t.string().optional(),
            "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
            "gtagConfigId": t.string().optional(),
        }
    ).named(renames["GtagConfigIn"])
    types["GtagConfigOut"] = t.struct(
        {
            "fingerprint": t.string().optional(),
            "path": t.string().optional(),
            "type": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "accountId": t.string().optional(),
            "workspaceId": t.string().optional(),
            "containerId": t.string().optional(),
            "parameter": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "gtagConfigId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GtagConfigOut"])
    types["ListTemplatesResponseIn"] = t.struct(
        {
            "template": t.array(t.proxy(renames["CustomTemplateIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTemplatesResponseIn"])
    types["ListTemplatesResponseOut"] = t.struct(
        {
            "template": t.array(t.proxy(renames["CustomTemplateOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTemplatesResponseOut"])
    types["TagConsentSettingIn"] = t.struct(
        {
            "consentType": t.proxy(renames["ParameterIn"]).optional(),
            "consentStatus": t.string().optional(),
        }
    ).named(renames["TagConsentSettingIn"])
    types["TagConsentSettingOut"] = t.struct(
        {
            "consentType": t.proxy(renames["ParameterOut"]).optional(),
            "consentStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagConsentSettingOut"])
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
    types["SyncWorkspaceResponseIn"] = t.struct(
        {
            "mergeConflict": t.array(t.proxy(renames["MergeConflictIn"])).optional(),
            "syncStatus": t.proxy(renames["SyncStatusIn"]).optional(),
        }
    ).named(renames["SyncWorkspaceResponseIn"])
    types["SyncWorkspaceResponseOut"] = t.struct(
        {
            "mergeConflict": t.array(t.proxy(renames["MergeConflictOut"])).optional(),
            "syncStatus": t.proxy(renames["SyncStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SyncWorkspaceResponseOut"])
    types["RevertTagResponseIn"] = t.struct(
        {"tag": t.proxy(renames["TagIn"]).optional()}
    ).named(renames["RevertTagResponseIn"])
    types["RevertTagResponseOut"] = t.struct(
        {
            "tag": t.proxy(renames["TagOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertTagResponseOut"])
    types["UserPermissionIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "containerAccess": t.array(
                t.proxy(renames["ContainerAccessIn"])
            ).optional(),
            "path": t.string().optional(),
            "accountAccess": t.proxy(renames["AccountAccessIn"]).optional(),
            "emailAddress": t.string().optional(),
        }
    ).named(renames["UserPermissionIn"])
    types["UserPermissionOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "containerAccess": t.array(
                t.proxy(renames["ContainerAccessOut"])
            ).optional(),
            "path": t.string().optional(),
            "accountAccess": t.proxy(renames["AccountAccessOut"]).optional(),
            "emailAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserPermissionOut"])
    types["EntityIn"] = t.struct(
        {
            "trigger": t.proxy(renames["TriggerIn"]).optional(),
            "changeStatus": t.string().optional(),
            "tag": t.proxy(renames["TagIn"]).optional(),
            "client": t.proxy(renames["ClientIn"]).optional(),
            "folder": t.proxy(renames["FolderIn"]).optional(),
            "variable": t.proxy(renames["VariableIn"]).optional(),
        }
    ).named(renames["EntityIn"])
    types["EntityOut"] = t.struct(
        {
            "trigger": t.proxy(renames["TriggerOut"]).optional(),
            "changeStatus": t.string().optional(),
            "tag": t.proxy(renames["TagOut"]).optional(),
            "client": t.proxy(renames["ClientOut"]).optional(),
            "folder": t.proxy(renames["FolderOut"]).optional(),
            "variable": t.proxy(renames["VariableOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityOut"])
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
    types["RevertTemplateResponseIn"] = t.struct(
        {"template": t.proxy(renames["CustomTemplateIn"]).optional()}
    ).named(renames["RevertTemplateResponseIn"])
    types["RevertTemplateResponseOut"] = t.struct(
        {
            "template": t.proxy(renames["CustomTemplateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertTemplateResponseOut"])
    types["FolderEntitiesIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "variable": t.array(t.proxy(renames["VariableIn"])).optional(),
            "trigger": t.array(t.proxy(renames["TriggerIn"])).optional(),
            "tag": t.array(t.proxy(renames["TagIn"])).optional(),
        }
    ).named(renames["FolderEntitiesIn"])
    types["FolderEntitiesOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "variable": t.array(t.proxy(renames["VariableOut"])).optional(),
            "trigger": t.array(t.proxy(renames["TriggerOut"])).optional(),
            "tag": t.array(t.proxy(renames["TagOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderEntitiesOut"])
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
    types["ListTagsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tag": t.array(t.proxy(renames["TagIn"])).optional(),
        }
    ).named(renames["ListTagsResponseIn"])
    types["ListTagsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tag": t.array(t.proxy(renames["TagOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTagsResponseOut"])
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
    types["ListDestinationsResponseIn"] = t.struct(
        {
            "destination": t.array(t.proxy(renames["DestinationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDestinationsResponseIn"])
    types["ListDestinationsResponseOut"] = t.struct(
        {
            "destination": t.array(t.proxy(renames["DestinationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDestinationsResponseOut"])
    types["ContainerVersionIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "client": t.array(t.proxy(renames["ClientIn"])).optional(),
            "builtInVariable": t.array(
                t.proxy(renames["BuiltInVariableIn"])
            ).optional(),
            "folder": t.array(t.proxy(renames["FolderIn"])).optional(),
            "trigger": t.array(t.proxy(renames["TriggerIn"])).optional(),
            "gtagConfig": t.array(t.proxy(renames["GtagConfigIn"])).optional(),
            "variable": t.array(t.proxy(renames["VariableIn"])).optional(),
            "description": t.string().optional(),
            "zone": t.array(t.proxy(renames["ZoneIn"])).optional(),
            "container": t.proxy(renames["ContainerIn"]).optional(),
            "containerVersionId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "path": t.string().optional(),
            "deleted": t.boolean().optional(),
            "tag": t.array(t.proxy(renames["TagIn"])).optional(),
            "containerId": t.string().optional(),
            "name": t.string().optional(),
            "customTemplate": t.array(t.proxy(renames["CustomTemplateIn"])).optional(),
        }
    ).named(renames["ContainerVersionIn"])
    types["ContainerVersionOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "client": t.array(t.proxy(renames["ClientOut"])).optional(),
            "builtInVariable": t.array(
                t.proxy(renames["BuiltInVariableOut"])
            ).optional(),
            "folder": t.array(t.proxy(renames["FolderOut"])).optional(),
            "trigger": t.array(t.proxy(renames["TriggerOut"])).optional(),
            "gtagConfig": t.array(t.proxy(renames["GtagConfigOut"])).optional(),
            "variable": t.array(t.proxy(renames["VariableOut"])).optional(),
            "description": t.string().optional(),
            "zone": t.array(t.proxy(renames["ZoneOut"])).optional(),
            "container": t.proxy(renames["ContainerOut"]).optional(),
            "containerVersionId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "path": t.string().optional(),
            "deleted": t.boolean().optional(),
            "tag": t.array(t.proxy(renames["TagOut"])).optional(),
            "containerId": t.string().optional(),
            "name": t.string().optional(),
            "customTemplate": t.array(t.proxy(renames["CustomTemplateOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerVersionOut"])
    types["TagIn"] = t.struct(
        {
            "priority": t.proxy(renames["ParameterIn"]).optional(),
            "tagId": t.string().optional(),
            "type": t.string().optional(),
            "parentFolderId": t.string().optional(),
            "notes": t.string().optional(),
            "consentSettings": t.proxy(renames["TagConsentSettingIn"]).optional(),
            "tagFiringOption": t.string().optional(),
            "blockingRuleId": t.array(t.string()).optional(),
            "path": t.string().optional(),
            "name": t.string().optional(),
            "blockingTriggerId": t.array(t.string()).optional(),
            "monitoringMetadataTagNameKey": t.string().optional(),
            "monitoringMetadata": t.proxy(renames["ParameterIn"]).optional(),
            "liveOnly": t.boolean().optional(),
            "fingerprint": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "containerId": t.string().optional(),
            "firingRuleId": t.array(t.string()).optional(),
            "accountId": t.string().optional(),
            "workspaceId": t.string().optional(),
            "teardownTag": t.array(t.proxy(renames["TeardownTagIn"])).optional(),
            "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
            "paused": t.boolean().optional(),
            "firingTriggerId": t.array(t.string()).optional(),
            "scheduleEndMs": t.string().optional(),
            "setupTag": t.array(t.proxy(renames["SetupTagIn"])).optional(),
            "scheduleStartMs": t.string().optional(),
        }
    ).named(renames["TagIn"])
    types["TagOut"] = t.struct(
        {
            "priority": t.proxy(renames["ParameterOut"]).optional(),
            "tagId": t.string().optional(),
            "type": t.string().optional(),
            "parentFolderId": t.string().optional(),
            "notes": t.string().optional(),
            "consentSettings": t.proxy(renames["TagConsentSettingOut"]).optional(),
            "tagFiringOption": t.string().optional(),
            "blockingRuleId": t.array(t.string()).optional(),
            "path": t.string().optional(),
            "name": t.string().optional(),
            "blockingTriggerId": t.array(t.string()).optional(),
            "monitoringMetadataTagNameKey": t.string().optional(),
            "monitoringMetadata": t.proxy(renames["ParameterOut"]).optional(),
            "liveOnly": t.boolean().optional(),
            "fingerprint": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "containerId": t.string().optional(),
            "firingRuleId": t.array(t.string()).optional(),
            "accountId": t.string().optional(),
            "workspaceId": t.string().optional(),
            "teardownTag": t.array(t.proxy(renames["TeardownTagOut"])).optional(),
            "parameter": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "paused": t.boolean().optional(),
            "firingTriggerId": t.array(t.string()).optional(),
            "scheduleEndMs": t.string().optional(),
            "setupTag": t.array(t.proxy(renames["SetupTagOut"])).optional(),
            "scheduleStartMs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagOut"])
    types["ListAccountsResponseIn"] = t.struct(
        {
            "account": t.array(t.proxy(renames["AccountIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAccountsResponseIn"])
    types["ListAccountsResponseOut"] = t.struct(
        {
            "account": t.array(t.proxy(renames["AccountOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAccountsResponseOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "environmentId": t.string().optional(),
            "description": t.string().optional(),
            "authorizationTimestamp": t.string().optional(),
            "type": t.string().optional(),
            "path": t.string().optional(),
            "workspaceId": t.string().optional(),
            "name": t.string().optional(),
            "containerId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "fingerprint": t.string().optional(),
            "url": t.string().optional(),
            "authorizationCode": t.string().optional(),
            "accountId": t.string().optional(),
            "enableDebug": t.boolean().optional(),
            "containerVersionId": t.string().optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "environmentId": t.string().optional(),
            "description": t.string().optional(),
            "authorizationTimestamp": t.string().optional(),
            "type": t.string().optional(),
            "path": t.string().optional(),
            "workspaceId": t.string().optional(),
            "name": t.string().optional(),
            "containerId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "fingerprint": t.string().optional(),
            "url": t.string().optional(),
            "authorizationCode": t.string().optional(),
            "accountId": t.string().optional(),
            "enableDebug": t.boolean().optional(),
            "containerVersionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["ZoneChildContainerIn"] = t.struct(
        {"publicId": t.string().optional(), "nickname": t.string().optional()}
    ).named(renames["ZoneChildContainerIn"])
    types["ZoneChildContainerOut"] = t.struct(
        {
            "publicId": t.string().optional(),
            "nickname": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZoneChildContainerOut"])
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
    types["SyncStatusIn"] = t.struct(
        {"syncError": t.boolean().optional(), "mergeConflict": t.boolean().optional()}
    ).named(renames["SyncStatusIn"])
    types["SyncStatusOut"] = t.struct(
        {
            "syncError": t.boolean().optional(),
            "mergeConflict": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SyncStatusOut"])
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
    types["PublishContainerVersionResponseIn"] = t.struct(
        {
            "containerVersion": t.proxy(renames["ContainerVersionIn"]).optional(),
            "compilerError": t.boolean().optional(),
        }
    ).named(renames["PublishContainerVersionResponseIn"])
    types["PublishContainerVersionResponseOut"] = t.struct(
        {
            "containerVersion": t.proxy(renames["ContainerVersionOut"]).optional(),
            "compilerError": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishContainerVersionResponseOut"])
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
    types["BuiltInVariableIn"] = t.struct(
        {
            "path": t.string().optional(),
            "accountId": t.string().optional(),
            "workspaceId": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "containerId": t.string().optional(),
        }
    ).named(renames["BuiltInVariableIn"])
    types["BuiltInVariableOut"] = t.struct(
        {
            "path": t.string().optional(),
            "accountId": t.string().optional(),
            "workspaceId": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "containerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuiltInVariableOut"])
    types["GalleryReferenceIn"] = t.struct(
        {
            "signature": t.string().optional(),
            "repository": t.string().optional(),
            "isModified": t.boolean().optional(),
            "owner": t.string().optional(),
            "version": t.string().optional(),
            "host": t.string().optional(),
        }
    ).named(renames["GalleryReferenceIn"])
    types["GalleryReferenceOut"] = t.struct(
        {
            "signature": t.string().optional(),
            "repository": t.string().optional(),
            "isModified": t.boolean().optional(),
            "owner": t.string().optional(),
            "version": t.string().optional(),
            "host": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GalleryReferenceOut"])
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
    types["ParameterIn"] = t.struct(
        {
            "type": t.string().optional(),
            "list": t.array(t.proxy(renames["ParameterIn"])).optional(),
            "map": t.array(t.proxy(renames["ParameterIn"])).optional(),
            "value": t.string().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["ParameterIn"])
    types["ParameterOut"] = t.struct(
        {
            "type": t.string().optional(),
            "list": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "map": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "value": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParameterOut"])
    types["TriggerIn"] = t.struct(
        {
            "totalTimeMinMilliseconds": t.proxy(renames["ParameterIn"]).optional(),
            "maxTimerLengthSeconds": t.proxy(renames["ParameterIn"]).optional(),
            "horizontalScrollPercentageList": t.proxy(
                renames["ParameterIn"]
            ).optional(),
            "filter": t.array(t.proxy(renames["ConditionIn"])).optional(),
            "eventName": t.proxy(renames["ParameterIn"]).optional(),
            "waitForTags": t.proxy(renames["ParameterIn"]).optional(),
            "fingerprint": t.string().optional(),
            "autoEventFilter": t.array(t.proxy(renames["ConditionIn"])).optional(),
            "accountId": t.string().optional(),
            "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
            "notes": t.string().optional(),
            "waitForTagsTimeout": t.proxy(renames["ParameterIn"]).optional(),
            "uniqueTriggerId": t.proxy(renames["ParameterIn"]).optional(),
            "workspaceId": t.string().optional(),
            "path": t.string().optional(),
            "parentFolderId": t.string().optional(),
            "visiblePercentageMax": t.proxy(renames["ParameterIn"]).optional(),
            "interval": t.proxy(renames["ParameterIn"]).optional(),
            "intervalSeconds": t.proxy(renames["ParameterIn"]).optional(),
            "checkValidation": t.proxy(renames["ParameterIn"]).optional(),
            "customEventFilter": t.array(t.proxy(renames["ConditionIn"])).optional(),
            "type": t.string().optional(),
            "triggerId": t.string().optional(),
            "visiblePercentageMin": t.proxy(renames["ParameterIn"]).optional(),
            "selector": t.proxy(renames["ParameterIn"]).optional(),
            "tagManagerUrl": t.string().optional(),
            "continuousTimeMinMilliseconds": t.proxy(renames["ParameterIn"]).optional(),
            "name": t.string().optional(),
            "visibilitySelector": t.proxy(renames["ParameterIn"]).optional(),
            "containerId": t.string().optional(),
            "verticalScrollPercentageList": t.proxy(renames["ParameterIn"]).optional(),
            "limit": t.proxy(renames["ParameterIn"]).optional(),
        }
    ).named(renames["TriggerIn"])
    types["TriggerOut"] = t.struct(
        {
            "totalTimeMinMilliseconds": t.proxy(renames["ParameterOut"]).optional(),
            "maxTimerLengthSeconds": t.proxy(renames["ParameterOut"]).optional(),
            "horizontalScrollPercentageList": t.proxy(
                renames["ParameterOut"]
            ).optional(),
            "filter": t.array(t.proxy(renames["ConditionOut"])).optional(),
            "eventName": t.proxy(renames["ParameterOut"]).optional(),
            "waitForTags": t.proxy(renames["ParameterOut"]).optional(),
            "fingerprint": t.string().optional(),
            "autoEventFilter": t.array(t.proxy(renames["ConditionOut"])).optional(),
            "accountId": t.string().optional(),
            "parameter": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "notes": t.string().optional(),
            "waitForTagsTimeout": t.proxy(renames["ParameterOut"]).optional(),
            "uniqueTriggerId": t.proxy(renames["ParameterOut"]).optional(),
            "workspaceId": t.string().optional(),
            "path": t.string().optional(),
            "parentFolderId": t.string().optional(),
            "visiblePercentageMax": t.proxy(renames["ParameterOut"]).optional(),
            "interval": t.proxy(renames["ParameterOut"]).optional(),
            "intervalSeconds": t.proxy(renames["ParameterOut"]).optional(),
            "checkValidation": t.proxy(renames["ParameterOut"]).optional(),
            "customEventFilter": t.array(t.proxy(renames["ConditionOut"])).optional(),
            "type": t.string().optional(),
            "triggerId": t.string().optional(),
            "visiblePercentageMin": t.proxy(renames["ParameterOut"]).optional(),
            "selector": t.proxy(renames["ParameterOut"]).optional(),
            "tagManagerUrl": t.string().optional(),
            "continuousTimeMinMilliseconds": t.proxy(
                renames["ParameterOut"]
            ).optional(),
            "name": t.string().optional(),
            "visibilitySelector": t.proxy(renames["ParameterOut"]).optional(),
            "containerId": t.string().optional(),
            "verticalScrollPercentageList": t.proxy(renames["ParameterOut"]).optional(),
            "limit": t.proxy(renames["ParameterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerOut"])
    types["DestinationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "destinationLinkId": t.string().optional(),
            "accountId": t.string().optional(),
            "path": t.string().optional(),
            "fingerprint": t.string().optional(),
            "destinationId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "containerId": t.string().optional(),
        }
    ).named(renames["DestinationIn"])
    types["DestinationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "destinationLinkId": t.string().optional(),
            "accountId": t.string().optional(),
            "path": t.string().optional(),
            "fingerprint": t.string().optional(),
            "destinationId": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "containerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationOut"])
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
    types["RevertZoneResponseIn"] = t.struct(
        {"zone": t.proxy(renames["ZoneIn"]).optional()}
    ).named(renames["RevertZoneResponseIn"])
    types["RevertZoneResponseOut"] = t.struct(
        {
            "zone": t.proxy(renames["ZoneOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertZoneResponseOut"])
    types["RevertBuiltInVariableResponseIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["RevertBuiltInVariableResponseIn"])
    types["RevertBuiltInVariableResponseOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertBuiltInVariableResponseOut"])
    types["ListGtagConfigResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "gtagConfig": t.array(t.proxy(renames["GtagConfigIn"])).optional(),
        }
    ).named(renames["ListGtagConfigResponseIn"])
    types["ListGtagConfigResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "gtagConfig": t.array(t.proxy(renames["GtagConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGtagConfigResponseOut"])
    types["ContainerIn"] = t.struct(
        {
            "tagManagerUrl": t.string().optional(),
            "accountId": t.string().optional(),
            "domainName": t.array(t.string()).optional(),
            "containerId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "tagIds": t.array(t.string()).optional(),
            "notes": t.string().optional(),
            "name": t.string().optional(),
            "path": t.string().optional(),
            "usageContext": t.array(t.string()).optional(),
            "features": t.proxy(renames["ContainerFeaturesIn"]).optional(),
            "publicId": t.string().optional(),
            "taggingServerUrls": t.array(t.string()).optional(),
        }
    ).named(renames["ContainerIn"])
    types["ContainerOut"] = t.struct(
        {
            "tagManagerUrl": t.string().optional(),
            "accountId": t.string().optional(),
            "domainName": t.array(t.string()).optional(),
            "containerId": t.string().optional(),
            "fingerprint": t.string().optional(),
            "tagIds": t.array(t.string()).optional(),
            "notes": t.string().optional(),
            "name": t.string().optional(),
            "path": t.string().optional(),
            "usageContext": t.array(t.string()).optional(),
            "features": t.proxy(renames["ContainerFeaturesOut"]).optional(),
            "publicId": t.string().optional(),
            "taggingServerUrls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerOut"])
    types["ListEnvironmentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "environment": t.array(t.proxy(renames["EnvironmentIn"])).optional(),
        }
    ).named(renames["ListEnvironmentsResponseIn"])
    types["ListEnvironmentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "environment": t.array(t.proxy(renames["EnvironmentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEnvironmentsResponseOut"])
    types["WorkspaceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "fingerprint": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "path": t.string().optional(),
            "containerId": t.string().optional(),
            "accountId": t.string().optional(),
            "description": t.string().optional(),
            "workspaceId": t.string().optional(),
        }
    ).named(renames["WorkspaceIn"])
    types["WorkspaceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "fingerprint": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "path": t.string().optional(),
            "containerId": t.string().optional(),
            "accountId": t.string().optional(),
            "description": t.string().optional(),
            "workspaceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkspaceOut"])
    types["ListUserPermissionsResponseIn"] = t.struct(
        {
            "userPermission": t.array(t.proxy(renames["UserPermissionIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListUserPermissionsResponseIn"])
    types["ListUserPermissionsResponseOut"] = t.struct(
        {
            "userPermission": t.array(t.proxy(renames["UserPermissionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUserPermissionsResponseOut"])
    types["CreateContainerVersionResponseIn"] = t.struct(
        {
            "containerVersion": t.proxy(renames["ContainerVersionIn"]).optional(),
            "newWorkspacePath": t.string().optional(),
            "compilerError": t.boolean().optional(),
            "syncStatus": t.proxy(renames["SyncStatusIn"]).optional(),
        }
    ).named(renames["CreateContainerVersionResponseIn"])
    types["CreateContainerVersionResponseOut"] = t.struct(
        {
            "containerVersion": t.proxy(renames["ContainerVersionOut"]).optional(),
            "newWorkspacePath": t.string().optional(),
            "compilerError": t.boolean().optional(),
            "syncStatus": t.proxy(renames["SyncStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateContainerVersionResponseOut"])
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
    types["ConditionIn"] = t.struct(
        {
            "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ConditionIn"])
    types["ConditionOut"] = t.struct(
        {
            "parameter": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionOut"])
    types["MergeConflictIn"] = t.struct(
        {
            "entityInWorkspace": t.proxy(renames["EntityIn"]).optional(),
            "entityInBaseVersion": t.proxy(renames["EntityIn"]).optional(),
        }
    ).named(renames["MergeConflictIn"])
    types["MergeConflictOut"] = t.struct(
        {
            "entityInWorkspace": t.proxy(renames["EntityOut"]).optional(),
            "entityInBaseVersion": t.proxy(renames["EntityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MergeConflictOut"])
    types["RevertFolderResponseIn"] = t.struct(
        {"folder": t.proxy(renames["FolderIn"]).optional()}
    ).named(renames["RevertFolderResponseIn"])
    types["RevertFolderResponseOut"] = t.struct(
        {
            "folder": t.proxy(renames["FolderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertFolderResponseOut"])
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
    types["ContainerFeaturesIn"] = t.struct(
        {
            "supportTags": t.boolean().optional(),
            "supportEnvironments": t.boolean().optional(),
            "supportGtagConfigs": t.boolean().optional(),
            "supportZones": t.boolean().optional(),
            "supportUserPermissions": t.boolean().optional(),
            "supportTemplates": t.boolean().optional(),
            "supportClients": t.boolean().optional(),
            "supportVersions": t.boolean().optional(),
            "supportBuiltInVariables": t.boolean().optional(),
            "supportWorkspaces": t.boolean().optional(),
            "supportFolders": t.boolean().optional(),
            "supportVariables": t.boolean().optional(),
            "supportTriggers": t.boolean().optional(),
        }
    ).named(renames["ContainerFeaturesIn"])
    types["ContainerFeaturesOut"] = t.struct(
        {
            "supportTags": t.boolean().optional(),
            "supportEnvironments": t.boolean().optional(),
            "supportGtagConfigs": t.boolean().optional(),
            "supportZones": t.boolean().optional(),
            "supportUserPermissions": t.boolean().optional(),
            "supportTemplates": t.boolean().optional(),
            "supportClients": t.boolean().optional(),
            "supportVersions": t.boolean().optional(),
            "supportBuiltInVariables": t.boolean().optional(),
            "supportWorkspaces": t.boolean().optional(),
            "supportFolders": t.boolean().optional(),
            "supportVariables": t.boolean().optional(),
            "supportTriggers": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerFeaturesOut"])
    types["VariableIn"] = t.struct(
        {
            "name": t.string().optional(),
            "notes": t.string().optional(),
            "scheduleStartMs": t.string().optional(),
            "enablingTriggerId": t.array(t.string()).optional(),
            "variableId": t.string().optional(),
            "workspaceId": t.string().optional(),
            "formatValue": t.proxy(renames["VariableFormatValueIn"]).optional(),
            "path": t.string().optional(),
            "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
            "parentFolderId": t.string().optional(),
            "type": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "scheduleEndMs": t.string().optional(),
            "disablingTriggerId": t.array(t.string()).optional(),
            "fingerprint": t.string().optional(),
            "containerId": t.string().optional(),
            "accountId": t.string().optional(),
        }
    ).named(renames["VariableIn"])
    types["VariableOut"] = t.struct(
        {
            "name": t.string().optional(),
            "notes": t.string().optional(),
            "scheduleStartMs": t.string().optional(),
            "enablingTriggerId": t.array(t.string()).optional(),
            "variableId": t.string().optional(),
            "workspaceId": t.string().optional(),
            "formatValue": t.proxy(renames["VariableFormatValueOut"]).optional(),
            "path": t.string().optional(),
            "parameter": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "parentFolderId": t.string().optional(),
            "type": t.string().optional(),
            "tagManagerUrl": t.string().optional(),
            "scheduleEndMs": t.string().optional(),
            "disablingTriggerId": t.array(t.string()).optional(),
            "fingerprint": t.string().optional(),
            "containerId": t.string().optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VariableOut"])
    types["ContainerAccessIn"] = t.struct(
        {"permission": t.string().optional(), "containerId": t.string().optional()}
    ).named(renames["ContainerAccessIn"])
    types["ContainerAccessOut"] = t.struct(
        {
            "permission": t.string().optional(),
            "containerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerAccessOut"])
    types["RevertTriggerResponseIn"] = t.struct(
        {"trigger": t.proxy(renames["TriggerIn"]).optional()}
    ).named(renames["RevertTriggerResponseIn"])
    types["RevertTriggerResponseOut"] = t.struct(
        {
            "trigger": t.proxy(renames["TriggerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertTriggerResponseOut"])
    types["ContainerVersionHeaderIn"] = t.struct(
        {
            "numZones": t.string().optional(),
            "numVariables": t.string().optional(),
            "containerVersionId": t.string().optional(),
            "numRules": t.string().optional(),
            "numTransformations": t.string().optional(),
            "numTriggers": t.string().optional(),
            "numTags": t.string().optional(),
            "name": t.string().optional(),
            "numGtagConfigs": t.string().optional(),
            "numMacros": t.string().optional(),
            "accountId": t.string().optional(),
            "path": t.string().optional(),
            "numClients": t.string().optional(),
            "deleted": t.boolean().optional(),
            "numCustomTemplates": t.string().optional(),
            "containerId": t.string().optional(),
        }
    ).named(renames["ContainerVersionHeaderIn"])
    types["ContainerVersionHeaderOut"] = t.struct(
        {
            "numZones": t.string().optional(),
            "numVariables": t.string().optional(),
            "containerVersionId": t.string().optional(),
            "numRules": t.string().optional(),
            "numTransformations": t.string().optional(),
            "numTriggers": t.string().optional(),
            "numTags": t.string().optional(),
            "name": t.string().optional(),
            "numGtagConfigs": t.string().optional(),
            "numMacros": t.string().optional(),
            "accountId": t.string().optional(),
            "path": t.string().optional(),
            "numClients": t.string().optional(),
            "deleted": t.boolean().optional(),
            "numCustomTemplates": t.string().optional(),
            "containerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerVersionHeaderOut"])
    types["ListClientsResponseIn"] = t.struct(
        {
            "client": t.array(t.proxy(renames["ClientIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListClientsResponseIn"])
    types["ListClientsResponseOut"] = t.struct(
        {
            "client": t.array(t.proxy(renames["ClientOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListClientsResponseOut"])
    types["RevertVariableResponseIn"] = t.struct(
        {"variable": t.proxy(renames["VariableIn"]).optional()}
    ).named(renames["RevertVariableResponseIn"])
    types["RevertVariableResponseOut"] = t.struct(
        {
            "variable": t.proxy(renames["VariableOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertVariableResponseOut"])
    types["AccountAccessIn"] = t.struct({"permission": t.string().optional()}).named(
        renames["AccountAccessIn"]
    )
    types["AccountAccessOut"] = t.struct(
        {
            "permission": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountAccessOut"])
    types["RevertClientResponseIn"] = t.struct(
        {"client": t.proxy(renames["ClientIn"]).optional()}
    ).named(renames["RevertClientResponseIn"])
    types["RevertClientResponseOut"] = t.struct(
        {
            "client": t.proxy(renames["ClientOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertClientResponseOut"])

    functions = {}
    functions["accountsList"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "features": t.proxy(renames["AccountFeaturesIn"]).optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "shareData": t.boolean().optional(),
                "tagManagerUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsGet"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "features": t.proxy(renames["AccountFeaturesIn"]).optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "shareData": t.boolean().optional(),
                "tagManagerUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsUpdate"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "features": t.proxy(renames["AccountFeaturesIn"]).optional(),
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "shareData": t.boolean().optional(),
                "tagManagerUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsUser_permissionsList"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "accountId": t.string().optional(),
                "containerAccess": t.array(
                    t.proxy(renames["ContainerAccessIn"])
                ).optional(),
                "accountAccess": t.proxy(renames["AccountAccessIn"]).optional(),
                "emailAddress": t.string().optional(),
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
                "containerAccess": t.array(
                    t.proxy(renames["ContainerAccessIn"])
                ).optional(),
                "accountAccess": t.proxy(renames["AccountAccessIn"]).optional(),
                "emailAddress": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsUser_permissionsGet"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "accountId": t.string().optional(),
                "containerAccess": t.array(
                    t.proxy(renames["ContainerAccessIn"])
                ).optional(),
                "accountAccess": t.proxy(renames["AccountAccessIn"]).optional(),
                "emailAddress": t.string().optional(),
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
                "containerAccess": t.array(
                    t.proxy(renames["ContainerAccessIn"])
                ).optional(),
                "accountAccess": t.proxy(renames["AccountAccessIn"]).optional(),
                "emailAddress": t.string().optional(),
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
                "containerAccess": t.array(
                    t.proxy(renames["ContainerAccessIn"])
                ).optional(),
                "accountAccess": t.proxy(renames["AccountAccessIn"]).optional(),
                "emailAddress": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersUpdate"] = tagmanager.get(
        "tagmanager/v2/{parent}/containers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContainersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersDelete"] = tagmanager.get(
        "tagmanager/v2/{parent}/containers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContainersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersCombine"] = tagmanager.get(
        "tagmanager/v2/{parent}/containers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContainersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersGet"] = tagmanager.get(
        "tagmanager/v2/{parent}/containers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContainersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersMove_tag_id"] = tagmanager.get(
        "tagmanager/v2/{parent}/containers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContainersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersSnippet"] = tagmanager.get(
        "tagmanager/v2/{parent}/containers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContainersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersCreate"] = tagmanager.get(
        "tagmanager/v2/{parent}/containers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContainersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersLookup"] = tagmanager.get(
        "tagmanager/v2/{parent}/containers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContainersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersList"] = tagmanager.get(
        "tagmanager/v2/{parent}/containers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContainersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersDestinationsList"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["DestinationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersDestinationsLink"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["DestinationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersDestinationsGet"] = tagmanager.get(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["DestinationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersVersionsPublish"] = tagmanager.delete(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersVersionsUpdate"] = tagmanager.delete(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersVersionsSet_latest"] = tagmanager.delete(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersVersionsLive"] = tagmanager.delete(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersVersionsGet"] = tagmanager.delete(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersVersionsUndelete"] = tagmanager.delete(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersVersionsDelete"] = tagmanager.delete(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersVersion_headersList"] = tagmanager.get(
        "tagmanager/v2/{parent}/version_headers:latest",
        t.struct({"parent": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ContainerVersionHeaderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersVersion_headersLatest"] = tagmanager.get(
        "tagmanager/v2/{parent}/version_headers:latest",
        t.struct({"parent": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ContainerVersionHeaderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesDelete"] = tagmanager.post(
        "tagmanager/v2/{path}:resolve_conflict",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "changeStatus": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
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
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "changeStatus": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
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
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "changeStatus": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
                "variable": t.proxy(renames["VariableIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesSync"] = tagmanager.post(
        "tagmanager/v2/{path}:resolve_conflict",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "changeStatus": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
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
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "changeStatus": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
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
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "changeStatus": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
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
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "changeStatus": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
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
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "changeStatus": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
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
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "changeStatus": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
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
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "trigger": t.proxy(renames["TriggerIn"]).optional(),
                "changeStatus": t.string().optional(),
                "tag": t.proxy(renames["TagIn"]).optional(),
                "client": t.proxy(renames["ClientIn"]).optional(),
                "folder": t.proxy(renames["FolderIn"]).optional(),
                "variable": t.proxy(renames["VariableIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesFoldersGet"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "folderId": t.string().optional(),
                "name": t.string().optional(),
                "notes": t.string().optional(),
                "workspaceId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "containerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesFoldersCreate"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "folderId": t.string().optional(),
                "name": t.string().optional(),
                "notes": t.string().optional(),
                "workspaceId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "containerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesFoldersRevert"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "folderId": t.string().optional(),
                "name": t.string().optional(),
                "notes": t.string().optional(),
                "workspaceId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "containerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesFoldersDelete"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "folderId": t.string().optional(),
                "name": t.string().optional(),
                "notes": t.string().optional(),
                "workspaceId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "containerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesFoldersEntities"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "folderId": t.string().optional(),
                "name": t.string().optional(),
                "notes": t.string().optional(),
                "workspaceId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "containerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "accountsContainersWorkspacesFoldersMove_entities_to_folder"
    ] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "folderId": t.string().optional(),
                "name": t.string().optional(),
                "notes": t.string().optional(),
                "workspaceId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "containerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesFoldersList"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "folderId": t.string().optional(),
                "name": t.string().optional(),
                "notes": t.string().optional(),
                "workspaceId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "containerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesFoldersUpdate"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "folderId": t.string().optional(),
                "name": t.string().optional(),
                "notes": t.string().optional(),
                "workspaceId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "containerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesVariablesUpdate"] = tagmanager.post(
        "tagmanager/v2/{path}:revert",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertVariableResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesVariablesGet"] = tagmanager.post(
        "tagmanager/v2/{path}:revert",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertVariableResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesVariablesDelete"] = tagmanager.post(
        "tagmanager/v2/{path}:revert",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertVariableResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesVariablesList"] = tagmanager.post(
        "tagmanager/v2/{path}:revert",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertVariableResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesVariablesCreate"] = tagmanager.post(
        "tagmanager/v2/{path}:revert",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertVariableResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesVariablesRevert"] = tagmanager.post(
        "tagmanager/v2/{path}:revert",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertVariableResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTriggersRevert"] = tagmanager.get(
        "tagmanager/v2/{parent}/triggers",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTriggersDelete"] = tagmanager.get(
        "tagmanager/v2/{parent}/triggers",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTriggersGet"] = tagmanager.get(
        "tagmanager/v2/{parent}/triggers",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTriggersCreate"] = tagmanager.get(
        "tagmanager/v2/{parent}/triggers",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTriggersUpdate"] = tagmanager.get(
        "tagmanager/v2/{parent}/triggers",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTriggersList"] = tagmanager.get(
        "tagmanager/v2/{parent}/triggers",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTriggersResponseOut"]),
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
    functions["accountsContainersWorkspacesZonesUpdate"] = tagmanager.delete(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
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
    functions["accountsContainersWorkspacesZonesList"] = tagmanager.delete(
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
    functions["accountsContainersWorkspacesZonesDelete"] = tagmanager.delete(
        "tagmanager/v2/{path}",
        t.struct({"path": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesClientsList"] = tagmanager.post(
        "tagmanager/v2/{path}:revert",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertClientResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesClientsDelete"] = tagmanager.post(
        "tagmanager/v2/{path}:revert",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertClientResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesClientsUpdate"] = tagmanager.post(
        "tagmanager/v2/{path}:revert",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertClientResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesClientsGet"] = tagmanager.post(
        "tagmanager/v2/{path}:revert",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertClientResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesClientsCreate"] = tagmanager.post(
        "tagmanager/v2/{path}:revert",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertClientResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesClientsRevert"] = tagmanager.post(
        "tagmanager/v2/{path}:revert",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertClientResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesBuilt_in_variablesDelete"] = tagmanager.post(
        "tagmanager/v2/{path}/built_in_variables:revert",
        t.struct(
            {
                "type": t.string().optional(),
                "path": t.string().optional(),
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
                "type": t.string().optional(),
                "path": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertBuiltInVariableResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesBuilt_in_variablesList"] = tagmanager.post(
        "tagmanager/v2/{path}/built_in_variables:revert",
        t.struct(
            {
                "type": t.string().optional(),
                "path": t.string().optional(),
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
                "type": t.string().optional(),
                "path": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevertBuiltInVariableResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesGtag_configList"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "type": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "workspaceId": t.string().optional(),
                "containerId": t.string().optional(),
                "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
                "gtagConfigId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GtagConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesGtag_configDelete"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "type": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "workspaceId": t.string().optional(),
                "containerId": t.string().optional(),
                "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
                "gtagConfigId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GtagConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesGtag_configGet"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "type": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "workspaceId": t.string().optional(),
                "containerId": t.string().optional(),
                "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
                "gtagConfigId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GtagConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesGtag_configCreate"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "type": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "workspaceId": t.string().optional(),
                "containerId": t.string().optional(),
                "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
                "gtagConfigId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GtagConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesGtag_configUpdate"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "type": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "accountId": t.string().optional(),
                "workspaceId": t.string().optional(),
                "containerId": t.string().optional(),
                "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
                "gtagConfigId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GtagConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTemplatesRevert"] = tagmanager.get(
        "tagmanager/v2/{parent}/templates",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTemplatesUpdate"] = tagmanager.get(
        "tagmanager/v2/{parent}/templates",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTemplatesGet"] = tagmanager.get(
        "tagmanager/v2/{parent}/templates",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTemplatesDelete"] = tagmanager.get(
        "tagmanager/v2/{parent}/templates",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTemplatesCreate"] = tagmanager.get(
        "tagmanager/v2/{parent}/templates",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTemplatesList"] = tagmanager.get(
        "tagmanager/v2/{parent}/templates",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTagsGet"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "priority": t.proxy(renames["ParameterIn"]).optional(),
                "tagId": t.string().optional(),
                "type": t.string().optional(),
                "parentFolderId": t.string().optional(),
                "notes": t.string().optional(),
                "consentSettings": t.proxy(renames["TagConsentSettingIn"]).optional(),
                "tagFiringOption": t.string().optional(),
                "blockingRuleId": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "blockingTriggerId": t.array(t.string()).optional(),
                "monitoringMetadataTagNameKey": t.string().optional(),
                "monitoringMetadata": t.proxy(renames["ParameterIn"]).optional(),
                "liveOnly": t.boolean().optional(),
                "tagManagerUrl": t.string().optional(),
                "containerId": t.string().optional(),
                "firingRuleId": t.array(t.string()).optional(),
                "accountId": t.string().optional(),
                "workspaceId": t.string().optional(),
                "teardownTag": t.array(t.proxy(renames["TeardownTagIn"])).optional(),
                "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
                "paused": t.boolean().optional(),
                "firingTriggerId": t.array(t.string()).optional(),
                "scheduleEndMs": t.string().optional(),
                "setupTag": t.array(t.proxy(renames["SetupTagIn"])).optional(),
                "scheduleStartMs": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTagsRevert"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "priority": t.proxy(renames["ParameterIn"]).optional(),
                "tagId": t.string().optional(),
                "type": t.string().optional(),
                "parentFolderId": t.string().optional(),
                "notes": t.string().optional(),
                "consentSettings": t.proxy(renames["TagConsentSettingIn"]).optional(),
                "tagFiringOption": t.string().optional(),
                "blockingRuleId": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "blockingTriggerId": t.array(t.string()).optional(),
                "monitoringMetadataTagNameKey": t.string().optional(),
                "monitoringMetadata": t.proxy(renames["ParameterIn"]).optional(),
                "liveOnly": t.boolean().optional(),
                "tagManagerUrl": t.string().optional(),
                "containerId": t.string().optional(),
                "firingRuleId": t.array(t.string()).optional(),
                "accountId": t.string().optional(),
                "workspaceId": t.string().optional(),
                "teardownTag": t.array(t.proxy(renames["TeardownTagIn"])).optional(),
                "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
                "paused": t.boolean().optional(),
                "firingTriggerId": t.array(t.string()).optional(),
                "scheduleEndMs": t.string().optional(),
                "setupTag": t.array(t.proxy(renames["SetupTagIn"])).optional(),
                "scheduleStartMs": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTagsList"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "priority": t.proxy(renames["ParameterIn"]).optional(),
                "tagId": t.string().optional(),
                "type": t.string().optional(),
                "parentFolderId": t.string().optional(),
                "notes": t.string().optional(),
                "consentSettings": t.proxy(renames["TagConsentSettingIn"]).optional(),
                "tagFiringOption": t.string().optional(),
                "blockingRuleId": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "blockingTriggerId": t.array(t.string()).optional(),
                "monitoringMetadataTagNameKey": t.string().optional(),
                "monitoringMetadata": t.proxy(renames["ParameterIn"]).optional(),
                "liveOnly": t.boolean().optional(),
                "tagManagerUrl": t.string().optional(),
                "containerId": t.string().optional(),
                "firingRuleId": t.array(t.string()).optional(),
                "accountId": t.string().optional(),
                "workspaceId": t.string().optional(),
                "teardownTag": t.array(t.proxy(renames["TeardownTagIn"])).optional(),
                "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
                "paused": t.boolean().optional(),
                "firingTriggerId": t.array(t.string()).optional(),
                "scheduleEndMs": t.string().optional(),
                "setupTag": t.array(t.proxy(renames["SetupTagIn"])).optional(),
                "scheduleStartMs": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTagsCreate"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "priority": t.proxy(renames["ParameterIn"]).optional(),
                "tagId": t.string().optional(),
                "type": t.string().optional(),
                "parentFolderId": t.string().optional(),
                "notes": t.string().optional(),
                "consentSettings": t.proxy(renames["TagConsentSettingIn"]).optional(),
                "tagFiringOption": t.string().optional(),
                "blockingRuleId": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "blockingTriggerId": t.array(t.string()).optional(),
                "monitoringMetadataTagNameKey": t.string().optional(),
                "monitoringMetadata": t.proxy(renames["ParameterIn"]).optional(),
                "liveOnly": t.boolean().optional(),
                "tagManagerUrl": t.string().optional(),
                "containerId": t.string().optional(),
                "firingRuleId": t.array(t.string()).optional(),
                "accountId": t.string().optional(),
                "workspaceId": t.string().optional(),
                "teardownTag": t.array(t.proxy(renames["TeardownTagIn"])).optional(),
                "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
                "paused": t.boolean().optional(),
                "firingTriggerId": t.array(t.string()).optional(),
                "scheduleEndMs": t.string().optional(),
                "setupTag": t.array(t.proxy(renames["SetupTagIn"])).optional(),
                "scheduleStartMs": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTagsDelete"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "priority": t.proxy(renames["ParameterIn"]).optional(),
                "tagId": t.string().optional(),
                "type": t.string().optional(),
                "parentFolderId": t.string().optional(),
                "notes": t.string().optional(),
                "consentSettings": t.proxy(renames["TagConsentSettingIn"]).optional(),
                "tagFiringOption": t.string().optional(),
                "blockingRuleId": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "blockingTriggerId": t.array(t.string()).optional(),
                "monitoringMetadataTagNameKey": t.string().optional(),
                "monitoringMetadata": t.proxy(renames["ParameterIn"]).optional(),
                "liveOnly": t.boolean().optional(),
                "tagManagerUrl": t.string().optional(),
                "containerId": t.string().optional(),
                "firingRuleId": t.array(t.string()).optional(),
                "accountId": t.string().optional(),
                "workspaceId": t.string().optional(),
                "teardownTag": t.array(t.proxy(renames["TeardownTagIn"])).optional(),
                "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
                "paused": t.boolean().optional(),
                "firingTriggerId": t.array(t.string()).optional(),
                "scheduleEndMs": t.string().optional(),
                "setupTag": t.array(t.proxy(renames["SetupTagIn"])).optional(),
                "scheduleStartMs": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersWorkspacesTagsUpdate"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "fingerprint": t.string().optional(),
                "path": t.string().optional(),
                "priority": t.proxy(renames["ParameterIn"]).optional(),
                "tagId": t.string().optional(),
                "type": t.string().optional(),
                "parentFolderId": t.string().optional(),
                "notes": t.string().optional(),
                "consentSettings": t.proxy(renames["TagConsentSettingIn"]).optional(),
                "tagFiringOption": t.string().optional(),
                "blockingRuleId": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "blockingTriggerId": t.array(t.string()).optional(),
                "monitoringMetadataTagNameKey": t.string().optional(),
                "monitoringMetadata": t.proxy(renames["ParameterIn"]).optional(),
                "liveOnly": t.boolean().optional(),
                "tagManagerUrl": t.string().optional(),
                "containerId": t.string().optional(),
                "firingRuleId": t.array(t.string()).optional(),
                "accountId": t.string().optional(),
                "workspaceId": t.string().optional(),
                "teardownTag": t.array(t.proxy(renames["TeardownTagIn"])).optional(),
                "parameter": t.array(t.proxy(renames["ParameterIn"])).optional(),
                "paused": t.boolean().optional(),
                "firingTriggerId": t.array(t.string()).optional(),
                "scheduleEndMs": t.string().optional(),
                "setupTag": t.array(t.proxy(renames["SetupTagIn"])).optional(),
                "scheduleStartMs": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersEnvironmentsGet"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "environmentId": t.string().optional(),
                "description": t.string().optional(),
                "authorizationTimestamp": t.string().optional(),
                "type": t.string().optional(),
                "workspaceId": t.string().optional(),
                "name": t.string().optional(),
                "containerId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "url": t.string().optional(),
                "authorizationCode": t.string().optional(),
                "accountId": t.string().optional(),
                "enableDebug": t.boolean().optional(),
                "containerVersionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersEnvironmentsCreate"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "environmentId": t.string().optional(),
                "description": t.string().optional(),
                "authorizationTimestamp": t.string().optional(),
                "type": t.string().optional(),
                "workspaceId": t.string().optional(),
                "name": t.string().optional(),
                "containerId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "url": t.string().optional(),
                "authorizationCode": t.string().optional(),
                "accountId": t.string().optional(),
                "enableDebug": t.boolean().optional(),
                "containerVersionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersEnvironmentsReauthorize"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "environmentId": t.string().optional(),
                "description": t.string().optional(),
                "authorizationTimestamp": t.string().optional(),
                "type": t.string().optional(),
                "workspaceId": t.string().optional(),
                "name": t.string().optional(),
                "containerId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "url": t.string().optional(),
                "authorizationCode": t.string().optional(),
                "accountId": t.string().optional(),
                "enableDebug": t.boolean().optional(),
                "containerVersionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersEnvironmentsList"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "environmentId": t.string().optional(),
                "description": t.string().optional(),
                "authorizationTimestamp": t.string().optional(),
                "type": t.string().optional(),
                "workspaceId": t.string().optional(),
                "name": t.string().optional(),
                "containerId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "url": t.string().optional(),
                "authorizationCode": t.string().optional(),
                "accountId": t.string().optional(),
                "enableDebug": t.boolean().optional(),
                "containerVersionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersEnvironmentsDelete"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "environmentId": t.string().optional(),
                "description": t.string().optional(),
                "authorizationTimestamp": t.string().optional(),
                "type": t.string().optional(),
                "workspaceId": t.string().optional(),
                "name": t.string().optional(),
                "containerId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "url": t.string().optional(),
                "authorizationCode": t.string().optional(),
                "accountId": t.string().optional(),
                "enableDebug": t.boolean().optional(),
                "containerVersionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsContainersEnvironmentsUpdate"] = tagmanager.put(
        "tagmanager/v2/{path}",
        t.struct(
            {
                "path": t.string().optional(),
                "fingerprint": t.string().optional(),
                "environmentId": t.string().optional(),
                "description": t.string().optional(),
                "authorizationTimestamp": t.string().optional(),
                "type": t.string().optional(),
                "workspaceId": t.string().optional(),
                "name": t.string().optional(),
                "containerId": t.string().optional(),
                "tagManagerUrl": t.string().optional(),
                "url": t.string().optional(),
                "authorizationCode": t.string().optional(),
                "accountId": t.string().optional(),
                "enableDebug": t.boolean().optional(),
                "containerVersionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="tagmanager",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
