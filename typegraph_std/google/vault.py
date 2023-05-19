from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_vault() -> Import:
    vault = HTTPRuntime("https://vault.googleapis.com/")

    renames = {
        "ErrorResponse": "_vault_1_ErrorResponse",
        "ListHeldAccountsResponseIn": "_vault_2_ListHeldAccountsResponseIn",
        "ListHeldAccountsResponseOut": "_vault_3_ListHeldAccountsResponseOut",
        "HangoutsChatOptionsIn": "_vault_4_HangoutsChatOptionsIn",
        "HangoutsChatOptionsOut": "_vault_5_HangoutsChatOptionsOut",
        "UndeleteMatterRequestIn": "_vault_6_UndeleteMatterRequestIn",
        "UndeleteMatterRequestOut": "_vault_7_UndeleteMatterRequestOut",
        "SitesUrlInfoIn": "_vault_8_SitesUrlInfoIn",
        "SitesUrlInfoOut": "_vault_9_SitesUrlInfoOut",
        "CancelOperationRequestIn": "_vault_10_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_vault_11_CancelOperationRequestOut",
        "AddMatterPermissionsRequestIn": "_vault_12_AddMatterPermissionsRequestIn",
        "AddMatterPermissionsRequestOut": "_vault_13_AddMatterPermissionsRequestOut",
        "AddHeldAccountsRequestIn": "_vault_14_AddHeldAccountsRequestIn",
        "AddHeldAccountsRequestOut": "_vault_15_AddHeldAccountsRequestOut",
        "ExportIn": "_vault_16_ExportIn",
        "ExportOut": "_vault_17_ExportOut",
        "HangoutsChatInfoIn": "_vault_18_HangoutsChatInfoIn",
        "HangoutsChatInfoOut": "_vault_19_HangoutsChatInfoOut",
        "RemoveHeldAccountsResponseIn": "_vault_20_RemoveHeldAccountsResponseIn",
        "RemoveHeldAccountsResponseOut": "_vault_21_RemoveHeldAccountsResponseOut",
        "UserInfoIn": "_vault_22_UserInfoIn",
        "UserInfoOut": "_vault_23_UserInfoOut",
        "TeamDriveInfoIn": "_vault_24_TeamDriveInfoIn",
        "TeamDriveInfoOut": "_vault_25_TeamDriveInfoOut",
        "VoiceOptionsIn": "_vault_26_VoiceOptionsIn",
        "VoiceOptionsOut": "_vault_27_VoiceOptionsOut",
        "ListHoldsResponseIn": "_vault_28_ListHoldsResponseIn",
        "ListHoldsResponseOut": "_vault_29_ListHoldsResponseOut",
        "HeldGroupsQueryIn": "_vault_30_HeldGroupsQueryIn",
        "HeldGroupsQueryOut": "_vault_31_HeldGroupsQueryOut",
        "CloseMatterRequestIn": "_vault_32_CloseMatterRequestIn",
        "CloseMatterRequestOut": "_vault_33_CloseMatterRequestOut",
        "HeldVoiceQueryIn": "_vault_34_HeldVoiceQueryIn",
        "HeldVoiceQueryOut": "_vault_35_HeldVoiceQueryOut",
        "GroupsCountResultIn": "_vault_36_GroupsCountResultIn",
        "GroupsCountResultOut": "_vault_37_GroupsCountResultOut",
        "HeldDriveQueryIn": "_vault_38_HeldDriveQueryIn",
        "HeldDriveQueryOut": "_vault_39_HeldDriveQueryOut",
        "HeldAccountIn": "_vault_40_HeldAccountIn",
        "HeldAccountOut": "_vault_41_HeldAccountOut",
        "ReopenMatterResponseIn": "_vault_42_ReopenMatterResponseIn",
        "ReopenMatterResponseOut": "_vault_43_ReopenMatterResponseOut",
        "CloseMatterResponseIn": "_vault_44_CloseMatterResponseIn",
        "CloseMatterResponseOut": "_vault_45_CloseMatterResponseOut",
        "RemoveHeldAccountsRequestIn": "_vault_46_RemoveHeldAccountsRequestIn",
        "RemoveHeldAccountsRequestOut": "_vault_47_RemoveHeldAccountsRequestOut",
        "ExportStatsIn": "_vault_48_ExportStatsIn",
        "ExportStatsOut": "_vault_49_ExportStatsOut",
        "GroupsExportOptionsIn": "_vault_50_GroupsExportOptionsIn",
        "GroupsExportOptionsOut": "_vault_51_GroupsExportOptionsOut",
        "AccountCountErrorIn": "_vault_52_AccountCountErrorIn",
        "AccountCountErrorOut": "_vault_53_AccountCountErrorOut",
        "MatterPermissionIn": "_vault_54_MatterPermissionIn",
        "MatterPermissionOut": "_vault_55_MatterPermissionOut",
        "MatterIn": "_vault_56_MatterIn",
        "MatterOut": "_vault_57_MatterOut",
        "AccountCountIn": "_vault_58_AccountCountIn",
        "AccountCountOut": "_vault_59_AccountCountOut",
        "CloudStorageSinkIn": "_vault_60_CloudStorageSinkIn",
        "CloudStorageSinkOut": "_vault_61_CloudStorageSinkOut",
        "ListMattersResponseIn": "_vault_62_ListMattersResponseIn",
        "ListMattersResponseOut": "_vault_63_ListMattersResponseOut",
        "ReopenMatterRequestIn": "_vault_64_ReopenMatterRequestIn",
        "ReopenMatterRequestOut": "_vault_65_ReopenMatterRequestOut",
        "ListOperationsResponseIn": "_vault_66_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_vault_67_ListOperationsResponseOut",
        "ListSavedQueriesResponseIn": "_vault_68_ListSavedQueriesResponseIn",
        "ListSavedQueriesResponseOut": "_vault_69_ListSavedQueriesResponseOut",
        "ExportOptionsIn": "_vault_70_ExportOptionsIn",
        "ExportOptionsOut": "_vault_71_ExportOptionsOut",
        "StatusIn": "_vault_72_StatusIn",
        "StatusOut": "_vault_73_StatusOut",
        "OrgUnitInfoIn": "_vault_74_OrgUnitInfoIn",
        "OrgUnitInfoOut": "_vault_75_OrgUnitInfoOut",
        "AccountInfoIn": "_vault_76_AccountInfoIn",
        "AccountInfoOut": "_vault_77_AccountInfoOut",
        "MailOptionsIn": "_vault_78_MailOptionsIn",
        "MailOptionsOut": "_vault_79_MailOptionsOut",
        "AddHeldAccountsResponseIn": "_vault_80_AddHeldAccountsResponseIn",
        "AddHeldAccountsResponseOut": "_vault_81_AddHeldAccountsResponseOut",
        "CountArtifactsMetadataIn": "_vault_82_CountArtifactsMetadataIn",
        "CountArtifactsMetadataOut": "_vault_83_CountArtifactsMetadataOut",
        "HeldMailQueryIn": "_vault_84_HeldMailQueryIn",
        "HeldMailQueryOut": "_vault_85_HeldMailQueryOut",
        "HeldHangoutsChatQueryIn": "_vault_86_HeldHangoutsChatQueryIn",
        "HeldHangoutsChatQueryOut": "_vault_87_HeldHangoutsChatQueryOut",
        "EmptyIn": "_vault_88_EmptyIn",
        "EmptyOut": "_vault_89_EmptyOut",
        "SharedDriveInfoIn": "_vault_90_SharedDriveInfoIn",
        "SharedDriveInfoOut": "_vault_91_SharedDriveInfoOut",
        "SavedQueryIn": "_vault_92_SavedQueryIn",
        "SavedQueryOut": "_vault_93_SavedQueryOut",
        "CloudStorageFileIn": "_vault_94_CloudStorageFileIn",
        "CloudStorageFileOut": "_vault_95_CloudStorageFileOut",
        "MailExportOptionsIn": "_vault_96_MailExportOptionsIn",
        "MailExportOptionsOut": "_vault_97_MailExportOptionsOut",
        "CorpusQueryIn": "_vault_98_CorpusQueryIn",
        "CorpusQueryOut": "_vault_99_CorpusQueryOut",
        "OperationIn": "_vault_100_OperationIn",
        "OperationOut": "_vault_101_OperationOut",
        "HangoutsChatExportOptionsIn": "_vault_102_HangoutsChatExportOptionsIn",
        "HangoutsChatExportOptionsOut": "_vault_103_HangoutsChatExportOptionsOut",
        "MailCountResultIn": "_vault_104_MailCountResultIn",
        "MailCountResultOut": "_vault_105_MailCountResultOut",
        "HoldIn": "_vault_106_HoldIn",
        "HoldOut": "_vault_107_HoldOut",
        "VoiceExportOptionsIn": "_vault_108_VoiceExportOptionsIn",
        "VoiceExportOptionsOut": "_vault_109_VoiceExportOptionsOut",
        "RemoveMatterPermissionsRequestIn": "_vault_110_RemoveMatterPermissionsRequestIn",
        "RemoveMatterPermissionsRequestOut": "_vault_111_RemoveMatterPermissionsRequestOut",
        "AddHeldAccountResultIn": "_vault_112_AddHeldAccountResultIn",
        "AddHeldAccountResultOut": "_vault_113_AddHeldAccountResultOut",
        "DriveExportOptionsIn": "_vault_114_DriveExportOptionsIn",
        "DriveExportOptionsOut": "_vault_115_DriveExportOptionsOut",
        "DriveOptionsIn": "_vault_116_DriveOptionsIn",
        "DriveOptionsOut": "_vault_117_DriveOptionsOut",
        "QueryIn": "_vault_118_QueryIn",
        "QueryOut": "_vault_119_QueryOut",
        "ListExportsResponseIn": "_vault_120_ListExportsResponseIn",
        "ListExportsResponseOut": "_vault_121_ListExportsResponseOut",
        "HeldOrgUnitIn": "_vault_122_HeldOrgUnitIn",
        "HeldOrgUnitOut": "_vault_123_HeldOrgUnitOut",
        "CountArtifactsResponseIn": "_vault_124_CountArtifactsResponseIn",
        "CountArtifactsResponseOut": "_vault_125_CountArtifactsResponseOut",
        "CountArtifactsRequestIn": "_vault_126_CountArtifactsRequestIn",
        "CountArtifactsRequestOut": "_vault_127_CountArtifactsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListHeldAccountsResponseIn"] = t.struct(
        {"accounts": t.array(t.proxy(renames["HeldAccountIn"])).optional()}
    ).named(renames["ListHeldAccountsResponseIn"])
    types["ListHeldAccountsResponseOut"] = t.struct(
        {
            "accounts": t.array(t.proxy(renames["HeldAccountOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListHeldAccountsResponseOut"])
    types["HangoutsChatOptionsIn"] = t.struct(
        {"includeRooms": t.boolean().optional()}
    ).named(renames["HangoutsChatOptionsIn"])
    types["HangoutsChatOptionsOut"] = t.struct(
        {
            "includeRooms": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HangoutsChatOptionsOut"])
    types["UndeleteMatterRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteMatterRequestIn"]
    )
    types["UndeleteMatterRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteMatterRequestOut"])
    types["SitesUrlInfoIn"] = t.struct({"urls": t.array(t.string()).optional()}).named(
        renames["SitesUrlInfoIn"]
    )
    types["SitesUrlInfoOut"] = t.struct(
        {
            "urls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SitesUrlInfoOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["AddMatterPermissionsRequestIn"] = t.struct(
        {
            "sendEmails": t.boolean().optional(),
            "matterPermission": t.proxy(renames["MatterPermissionIn"]).optional(),
            "ccMe": t.boolean().optional(),
        }
    ).named(renames["AddMatterPermissionsRequestIn"])
    types["AddMatterPermissionsRequestOut"] = t.struct(
        {
            "sendEmails": t.boolean().optional(),
            "matterPermission": t.proxy(renames["MatterPermissionOut"]).optional(),
            "ccMe": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddMatterPermissionsRequestOut"])
    types["AddHeldAccountsRequestIn"] = t.struct(
        {
            "accountIds": t.array(t.string()).optional(),
            "emails": t.array(t.string()).optional(),
        }
    ).named(renames["AddHeldAccountsRequestIn"])
    types["AddHeldAccountsRequestOut"] = t.struct(
        {
            "accountIds": t.array(t.string()).optional(),
            "emails": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddHeldAccountsRequestOut"])
    types["ExportIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "query": t.proxy(renames["QueryIn"]).optional(),
            "requester": t.proxy(renames["UserInfoIn"]).optional(),
            "matterId": t.string().optional(),
            "cloudStorageSink": t.proxy(renames["CloudStorageSinkIn"]).optional(),
            "status": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "stats": t.proxy(renames["ExportStatsIn"]).optional(),
            "exportOptions": t.proxy(renames["ExportOptionsIn"]).optional(),
        }
    ).named(renames["ExportIn"])
    types["ExportOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "query": t.proxy(renames["QueryOut"]).optional(),
            "requester": t.proxy(renames["UserInfoOut"]).optional(),
            "matterId": t.string().optional(),
            "cloudStorageSink": t.proxy(renames["CloudStorageSinkOut"]).optional(),
            "status": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "stats": t.proxy(renames["ExportStatsOut"]).optional(),
            "exportOptions": t.proxy(renames["ExportOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportOut"])
    types["HangoutsChatInfoIn"] = t.struct(
        {"roomId": t.array(t.string()).optional()}
    ).named(renames["HangoutsChatInfoIn"])
    types["HangoutsChatInfoOut"] = t.struct(
        {
            "roomId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HangoutsChatInfoOut"])
    types["RemoveHeldAccountsResponseIn"] = t.struct(
        {"statuses": t.array(t.proxy(renames["StatusIn"])).optional()}
    ).named(renames["RemoveHeldAccountsResponseIn"])
    types["RemoveHeldAccountsResponseOut"] = t.struct(
        {
            "statuses": t.array(t.proxy(renames["StatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveHeldAccountsResponseOut"])
    types["UserInfoIn"] = t.struct(
        {"email": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["UserInfoIn"])
    types["UserInfoOut"] = t.struct(
        {
            "email": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserInfoOut"])
    types["TeamDriveInfoIn"] = t.struct(
        {"teamDriveIds": t.array(t.string()).optional()}
    ).named(renames["TeamDriveInfoIn"])
    types["TeamDriveInfoOut"] = t.struct(
        {
            "teamDriveIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TeamDriveInfoOut"])
    types["VoiceOptionsIn"] = t.struct(
        {"coveredData": t.array(t.string()).optional()}
    ).named(renames["VoiceOptionsIn"])
    types["VoiceOptionsOut"] = t.struct(
        {
            "coveredData": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceOptionsOut"])
    types["ListHoldsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "holds": t.array(t.proxy(renames["HoldIn"])).optional(),
        }
    ).named(renames["ListHoldsResponseIn"])
    types["ListHoldsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "holds": t.array(t.proxy(renames["HoldOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListHoldsResponseOut"])
    types["HeldGroupsQueryIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "terms": t.string().optional(),
        }
    ).named(renames["HeldGroupsQueryIn"])
    types["HeldGroupsQueryOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "terms": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldGroupsQueryOut"])
    types["CloseMatterRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloseMatterRequestIn"]
    )
    types["CloseMatterRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloseMatterRequestOut"])
    types["HeldVoiceQueryIn"] = t.struct(
        {"coveredData": t.array(t.string()).optional()}
    ).named(renames["HeldVoiceQueryIn"])
    types["HeldVoiceQueryOut"] = t.struct(
        {
            "coveredData": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldVoiceQueryOut"])
    types["GroupsCountResultIn"] = t.struct(
        {
            "nonQueryableAccounts": t.array(t.string()).optional(),
            "queriedAccountsCount": t.string().optional(),
            "matchingAccountsCount": t.string().optional(),
            "accountCounts": t.array(t.proxy(renames["AccountCountIn"])).optional(),
            "accountCountErrors": t.array(
                t.proxy(renames["AccountCountErrorIn"])
            ).optional(),
        }
    ).named(renames["GroupsCountResultIn"])
    types["GroupsCountResultOut"] = t.struct(
        {
            "nonQueryableAccounts": t.array(t.string()).optional(),
            "queriedAccountsCount": t.string().optional(),
            "matchingAccountsCount": t.string().optional(),
            "accountCounts": t.array(t.proxy(renames["AccountCountOut"])).optional(),
            "accountCountErrors": t.array(
                t.proxy(renames["AccountCountErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupsCountResultOut"])
    types["HeldDriveQueryIn"] = t.struct(
        {
            "includeSharedDriveFiles": t.boolean().optional(),
            "includeTeamDriveFiles": t.boolean().optional(),
        }
    ).named(renames["HeldDriveQueryIn"])
    types["HeldDriveQueryOut"] = t.struct(
        {
            "includeSharedDriveFiles": t.boolean().optional(),
            "includeTeamDriveFiles": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldDriveQueryOut"])
    types["HeldAccountIn"] = t.struct(
        {
            "holdTime": t.string().optional(),
            "lastName": t.string().optional(),
            "accountId": t.string().optional(),
            "firstName": t.string().optional(),
            "email": t.string().optional(),
        }
    ).named(renames["HeldAccountIn"])
    types["HeldAccountOut"] = t.struct(
        {
            "holdTime": t.string().optional(),
            "lastName": t.string().optional(),
            "accountId": t.string().optional(),
            "firstName": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldAccountOut"])
    types["ReopenMatterResponseIn"] = t.struct(
        {"matter": t.proxy(renames["MatterIn"]).optional()}
    ).named(renames["ReopenMatterResponseIn"])
    types["ReopenMatterResponseOut"] = t.struct(
        {
            "matter": t.proxy(renames["MatterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReopenMatterResponseOut"])
    types["CloseMatterResponseIn"] = t.struct(
        {"matter": t.proxy(renames["MatterIn"]).optional()}
    ).named(renames["CloseMatterResponseIn"])
    types["CloseMatterResponseOut"] = t.struct(
        {
            "matter": t.proxy(renames["MatterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloseMatterResponseOut"])
    types["RemoveHeldAccountsRequestIn"] = t.struct(
        {"accountIds": t.array(t.string()).optional()}
    ).named(renames["RemoveHeldAccountsRequestIn"])
    types["RemoveHeldAccountsRequestOut"] = t.struct(
        {
            "accountIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveHeldAccountsRequestOut"])
    types["ExportStatsIn"] = t.struct(
        {
            "totalArtifactCount": t.string().optional(),
            "exportedArtifactCount": t.string().optional(),
            "sizeInBytes": t.string().optional(),
        }
    ).named(renames["ExportStatsIn"])
    types["ExportStatsOut"] = t.struct(
        {
            "totalArtifactCount": t.string().optional(),
            "exportedArtifactCount": t.string().optional(),
            "sizeInBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportStatsOut"])
    types["GroupsExportOptionsIn"] = t.struct(
        {"exportFormat": t.string().optional()}
    ).named(renames["GroupsExportOptionsIn"])
    types["GroupsExportOptionsOut"] = t.struct(
        {
            "exportFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupsExportOptionsOut"])
    types["AccountCountErrorIn"] = t.struct(
        {
            "account": t.proxy(renames["UserInfoIn"]).optional(),
            "errorType": t.string().optional(),
        }
    ).named(renames["AccountCountErrorIn"])
    types["AccountCountErrorOut"] = t.struct(
        {
            "account": t.proxy(renames["UserInfoOut"]).optional(),
            "errorType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountCountErrorOut"])
    types["MatterPermissionIn"] = t.struct(
        {"accountId": t.string().optional(), "role": t.string().optional()}
    ).named(renames["MatterPermissionIn"])
    types["MatterPermissionOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatterPermissionOut"])
    types["MatterIn"] = t.struct(
        {
            "state": t.string().optional(),
            "name": t.string().optional(),
            "matterPermissions": t.array(
                t.proxy(renames["MatterPermissionIn"])
            ).optional(),
            "matterId": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["MatterIn"])
    types["MatterOut"] = t.struct(
        {
            "state": t.string().optional(),
            "name": t.string().optional(),
            "matterPermissions": t.array(
                t.proxy(renames["MatterPermissionOut"])
            ).optional(),
            "matterId": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatterOut"])
    types["AccountCountIn"] = t.struct(
        {
            "account": t.proxy(renames["UserInfoIn"]).optional(),
            "count": t.string().optional(),
        }
    ).named(renames["AccountCountIn"])
    types["AccountCountOut"] = t.struct(
        {
            "account": t.proxy(renames["UserInfoOut"]).optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountCountOut"])
    types["CloudStorageSinkIn"] = t.struct(
        {"files": t.array(t.proxy(renames["CloudStorageFileIn"])).optional()}
    ).named(renames["CloudStorageSinkIn"])
    types["CloudStorageSinkOut"] = t.struct(
        {
            "files": t.array(t.proxy(renames["CloudStorageFileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudStorageSinkOut"])
    types["ListMattersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "matters": t.array(t.proxy(renames["MatterIn"])).optional(),
        }
    ).named(renames["ListMattersResponseIn"])
    types["ListMattersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "matters": t.array(t.proxy(renames["MatterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMattersResponseOut"])
    types["ReopenMatterRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReopenMatterRequestIn"]
    )
    types["ReopenMatterRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReopenMatterRequestOut"])
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
    types["ListSavedQueriesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "savedQueries": t.array(t.proxy(renames["SavedQueryIn"])).optional(),
        }
    ).named(renames["ListSavedQueriesResponseIn"])
    types["ListSavedQueriesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "savedQueries": t.array(t.proxy(renames["SavedQueryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSavedQueriesResponseOut"])
    types["ExportOptionsIn"] = t.struct(
        {
            "voiceOptions": t.proxy(renames["VoiceExportOptionsIn"]).optional(),
            "region": t.string().optional(),
            "groupsOptions": t.proxy(renames["GroupsExportOptionsIn"]).optional(),
            "mailOptions": t.proxy(renames["MailExportOptionsIn"]).optional(),
            "driveOptions": t.proxy(renames["DriveExportOptionsIn"]).optional(),
            "hangoutsChatOptions": t.proxy(
                renames["HangoutsChatExportOptionsIn"]
            ).optional(),
        }
    ).named(renames["ExportOptionsIn"])
    types["ExportOptionsOut"] = t.struct(
        {
            "voiceOptions": t.proxy(renames["VoiceExportOptionsOut"]).optional(),
            "region": t.string().optional(),
            "groupsOptions": t.proxy(renames["GroupsExportOptionsOut"]).optional(),
            "mailOptions": t.proxy(renames["MailExportOptionsOut"]).optional(),
            "driveOptions": t.proxy(renames["DriveExportOptionsOut"]).optional(),
            "hangoutsChatOptions": t.proxy(
                renames["HangoutsChatExportOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportOptionsOut"])
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
    types["OrgUnitInfoIn"] = t.struct({"orgUnitId": t.string().optional()}).named(
        renames["OrgUnitInfoIn"]
    )
    types["OrgUnitInfoOut"] = t.struct(
        {
            "orgUnitId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrgUnitInfoOut"])
    types["AccountInfoIn"] = t.struct({"emails": t.array(t.string()).optional()}).named(
        renames["AccountInfoIn"]
    )
    types["AccountInfoOut"] = t.struct(
        {
            "emails": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountInfoOut"])
    types["MailOptionsIn"] = t.struct(
        {
            "clientSideEncryptedOption": t.string().optional(),
            "excludeDrafts": t.boolean().optional(),
        }
    ).named(renames["MailOptionsIn"])
    types["MailOptionsOut"] = t.struct(
        {
            "clientSideEncryptedOption": t.string().optional(),
            "excludeDrafts": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MailOptionsOut"])
    types["AddHeldAccountsResponseIn"] = t.struct(
        {"responses": t.array(t.proxy(renames["AddHeldAccountResultIn"])).optional()}
    ).named(renames["AddHeldAccountsResponseIn"])
    types["AddHeldAccountsResponseOut"] = t.struct(
        {
            "responses": t.array(
                t.proxy(renames["AddHeldAccountResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddHeldAccountsResponseOut"])
    types["CountArtifactsMetadataIn"] = t.struct(
        {
            "matterId": t.string().optional(),
            "query": t.proxy(renames["QueryIn"]).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["CountArtifactsMetadataIn"])
    types["CountArtifactsMetadataOut"] = t.struct(
        {
            "matterId": t.string().optional(),
            "query": t.proxy(renames["QueryOut"]).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountArtifactsMetadataOut"])
    types["HeldMailQueryIn"] = t.struct(
        {
            "terms": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["HeldMailQueryIn"])
    types["HeldMailQueryOut"] = t.struct(
        {
            "terms": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldMailQueryOut"])
    types["HeldHangoutsChatQueryIn"] = t.struct(
        {"includeRooms": t.boolean().optional()}
    ).named(renames["HeldHangoutsChatQueryIn"])
    types["HeldHangoutsChatQueryOut"] = t.struct(
        {
            "includeRooms": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldHangoutsChatQueryOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["SharedDriveInfoIn"] = t.struct(
        {"sharedDriveIds": t.array(t.string()).optional()}
    ).named(renames["SharedDriveInfoIn"])
    types["SharedDriveInfoOut"] = t.struct(
        {
            "sharedDriveIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SharedDriveInfoOut"])
    types["SavedQueryIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "matterId": t.string().optional(),
            "query": t.proxy(renames["QueryIn"]).optional(),
            "displayName": t.string().optional(),
            "savedQueryId": t.string().optional(),
        }
    ).named(renames["SavedQueryIn"])
    types["SavedQueryOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "matterId": t.string().optional(),
            "query": t.proxy(renames["QueryOut"]).optional(),
            "displayName": t.string().optional(),
            "savedQueryId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SavedQueryOut"])
    types["CloudStorageFileIn"] = t.struct(
        {
            "bucketName": t.string().optional(),
            "md5Hash": t.string().optional(),
            "objectName": t.string().optional(),
            "size": t.string().optional(),
        }
    ).named(renames["CloudStorageFileIn"])
    types["CloudStorageFileOut"] = t.struct(
        {
            "bucketName": t.string().optional(),
            "md5Hash": t.string().optional(),
            "objectName": t.string().optional(),
            "size": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudStorageFileOut"])
    types["MailExportOptionsIn"] = t.struct(
        {
            "exportFormat": t.string().optional(),
            "showConfidentialModeContent": t.boolean().optional(),
            "useNewExport": t.boolean().optional(),
        }
    ).named(renames["MailExportOptionsIn"])
    types["MailExportOptionsOut"] = t.struct(
        {
            "exportFormat": t.string().optional(),
            "showConfidentialModeContent": t.boolean().optional(),
            "useNewExport": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MailExportOptionsOut"])
    types["CorpusQueryIn"] = t.struct(
        {
            "driveQuery": t.proxy(renames["HeldDriveQueryIn"]).optional(),
            "groupsQuery": t.proxy(renames["HeldGroupsQueryIn"]).optional(),
            "voiceQuery": t.proxy(renames["HeldVoiceQueryIn"]).optional(),
            "hangoutsChatQuery": t.proxy(renames["HeldHangoutsChatQueryIn"]).optional(),
            "mailQuery": t.proxy(renames["HeldMailQueryIn"]).optional(),
        }
    ).named(renames["CorpusQueryIn"])
    types["CorpusQueryOut"] = t.struct(
        {
            "driveQuery": t.proxy(renames["HeldDriveQueryOut"]).optional(),
            "groupsQuery": t.proxy(renames["HeldGroupsQueryOut"]).optional(),
            "voiceQuery": t.proxy(renames["HeldVoiceQueryOut"]).optional(),
            "hangoutsChatQuery": t.proxy(
                renames["HeldHangoutsChatQueryOut"]
            ).optional(),
            "mailQuery": t.proxy(renames["HeldMailQueryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CorpusQueryOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["HangoutsChatExportOptionsIn"] = t.struct(
        {"exportFormat": t.string().optional()}
    ).named(renames["HangoutsChatExportOptionsIn"])
    types["HangoutsChatExportOptionsOut"] = t.struct(
        {
            "exportFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HangoutsChatExportOptionsOut"])
    types["MailCountResultIn"] = t.struct(
        {
            "nonQueryableAccounts": t.array(t.string()).optional(),
            "accountCounts": t.array(t.proxy(renames["AccountCountIn"])).optional(),
            "queriedAccountsCount": t.string().optional(),
            "matchingAccountsCount": t.string().optional(),
            "accountCountErrors": t.array(
                t.proxy(renames["AccountCountErrorIn"])
            ).optional(),
        }
    ).named(renames["MailCountResultIn"])
    types["MailCountResultOut"] = t.struct(
        {
            "nonQueryableAccounts": t.array(t.string()).optional(),
            "accountCounts": t.array(t.proxy(renames["AccountCountOut"])).optional(),
            "queriedAccountsCount": t.string().optional(),
            "matchingAccountsCount": t.string().optional(),
            "accountCountErrors": t.array(
                t.proxy(renames["AccountCountErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MailCountResultOut"])
    types["HoldIn"] = t.struct(
        {
            "accounts": t.array(t.proxy(renames["HeldAccountIn"])).optional(),
            "holdId": t.string().optional(),
            "corpus": t.string().optional(),
            "orgUnit": t.proxy(renames["HeldOrgUnitIn"]).optional(),
            "name": t.string().optional(),
            "query": t.proxy(renames["CorpusQueryIn"]).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["HoldIn"])
    types["HoldOut"] = t.struct(
        {
            "accounts": t.array(t.proxy(renames["HeldAccountOut"])).optional(),
            "holdId": t.string().optional(),
            "corpus": t.string().optional(),
            "orgUnit": t.proxy(renames["HeldOrgUnitOut"]).optional(),
            "name": t.string().optional(),
            "query": t.proxy(renames["CorpusQueryOut"]).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HoldOut"])
    types["VoiceExportOptionsIn"] = t.struct(
        {"exportFormat": t.string().optional()}
    ).named(renames["VoiceExportOptionsIn"])
    types["VoiceExportOptionsOut"] = t.struct(
        {
            "exportFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceExportOptionsOut"])
    types["RemoveMatterPermissionsRequestIn"] = t.struct(
        {"accountId": t.string().optional()}
    ).named(renames["RemoveMatterPermissionsRequestIn"])
    types["RemoveMatterPermissionsRequestOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveMatterPermissionsRequestOut"])
    types["AddHeldAccountResultIn"] = t.struct(
        {
            "account": t.proxy(renames["HeldAccountIn"]).optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["AddHeldAccountResultIn"])
    types["AddHeldAccountResultOut"] = t.struct(
        {
            "account": t.proxy(renames["HeldAccountOut"]).optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddHeldAccountResultOut"])
    types["DriveExportOptionsIn"] = t.struct(
        {"includeAccessInfo": t.boolean().optional()}
    ).named(renames["DriveExportOptionsIn"])
    types["DriveExportOptionsOut"] = t.struct(
        {
            "includeAccessInfo": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveExportOptionsOut"])
    types["DriveOptionsIn"] = t.struct(
        {
            "includeTeamDrives": t.boolean().optional(),
            "versionDate": t.string().optional(),
            "includeSharedDrives": t.boolean().optional(),
            "clientSideEncryptedOption": t.string().optional(),
        }
    ).named(renames["DriveOptionsIn"])
    types["DriveOptionsOut"] = t.struct(
        {
            "includeTeamDrives": t.boolean().optional(),
            "versionDate": t.string().optional(),
            "includeSharedDrives": t.boolean().optional(),
            "clientSideEncryptedOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveOptionsOut"])
    types["QueryIn"] = t.struct(
        {
            "accountInfo": t.proxy(renames["AccountInfoIn"]),
            "sharedDriveInfo": t.proxy(renames["SharedDriveInfoIn"]),
            "voiceOptions": t.proxy(renames["VoiceOptionsIn"]).optional(),
            "sitesUrlInfo": t.proxy(renames["SitesUrlInfoIn"]),
            "corpus": t.string().optional(),
            "hangoutsChatInfo": t.proxy(renames["HangoutsChatInfoIn"]),
            "driveOptions": t.proxy(renames["DriveOptionsIn"]).optional(),
            "dataScope": t.string().optional(),
            "teamDriveInfo": t.proxy(renames["TeamDriveInfoIn"]),
            "timeZone": t.string().optional(),
            "orgUnitInfo": t.proxy(renames["OrgUnitInfoIn"]),
            "hangoutsChatOptions": t.proxy(renames["HangoutsChatOptionsIn"]).optional(),
            "endTime": t.string().optional(),
            "terms": t.string().optional(),
            "mailOptions": t.proxy(renames["MailOptionsIn"]).optional(),
            "startTime": t.string().optional(),
            "searchMethod": t.string().optional(),
            "method": t.string().optional(),
        }
    ).named(renames["QueryIn"])
    types["QueryOut"] = t.struct(
        {
            "accountInfo": t.proxy(renames["AccountInfoOut"]),
            "sharedDriveInfo": t.proxy(renames["SharedDriveInfoOut"]),
            "voiceOptions": t.proxy(renames["VoiceOptionsOut"]).optional(),
            "sitesUrlInfo": t.proxy(renames["SitesUrlInfoOut"]),
            "corpus": t.string().optional(),
            "hangoutsChatInfo": t.proxy(renames["HangoutsChatInfoOut"]),
            "driveOptions": t.proxy(renames["DriveOptionsOut"]).optional(),
            "dataScope": t.string().optional(),
            "teamDriveInfo": t.proxy(renames["TeamDriveInfoOut"]),
            "timeZone": t.string().optional(),
            "orgUnitInfo": t.proxy(renames["OrgUnitInfoOut"]),
            "hangoutsChatOptions": t.proxy(
                renames["HangoutsChatOptionsOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "terms": t.string().optional(),
            "mailOptions": t.proxy(renames["MailOptionsOut"]).optional(),
            "startTime": t.string().optional(),
            "searchMethod": t.string().optional(),
            "method": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryOut"])
    types["ListExportsResponseIn"] = t.struct(
        {
            "exports": t.array(t.proxy(renames["ExportIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListExportsResponseIn"])
    types["ListExportsResponseOut"] = t.struct(
        {
            "exports": t.array(t.proxy(renames["ExportOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListExportsResponseOut"])
    types["HeldOrgUnitIn"] = t.struct(
        {"orgUnitId": t.string().optional(), "holdTime": t.string().optional()}
    ).named(renames["HeldOrgUnitIn"])
    types["HeldOrgUnitOut"] = t.struct(
        {
            "orgUnitId": t.string().optional(),
            "holdTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldOrgUnitOut"])
    types["CountArtifactsResponseIn"] = t.struct(
        {
            "groupsCountResult": t.proxy(renames["GroupsCountResultIn"]).optional(),
            "mailCountResult": t.proxy(renames["MailCountResultIn"]).optional(),
            "totalCount": t.string().optional(),
        }
    ).named(renames["CountArtifactsResponseIn"])
    types["CountArtifactsResponseOut"] = t.struct(
        {
            "groupsCountResult": t.proxy(renames["GroupsCountResultOut"]).optional(),
            "mailCountResult": t.proxy(renames["MailCountResultOut"]).optional(),
            "totalCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountArtifactsResponseOut"])
    types["CountArtifactsRequestIn"] = t.struct(
        {"view": t.string().optional(), "query": t.proxy(renames["QueryIn"]).optional()}
    ).named(renames["CountArtifactsRequestIn"])
    types["CountArtifactsRequestOut"] = t.struct(
        {
            "view": t.string().optional(),
            "query": t.proxy(renames["QueryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountArtifactsRequestOut"])

    functions = {}
    functions["mattersList"] = vault.delete(
        "v1/matters/{matterId}",
        t.struct({"matterId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MatterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersClose"] = vault.delete(
        "v1/matters/{matterId}",
        t.struct({"matterId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MatterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersReopen"] = vault.delete(
        "v1/matters/{matterId}",
        t.struct({"matterId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MatterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersUndelete"] = vault.delete(
        "v1/matters/{matterId}",
        t.struct({"matterId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MatterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersAddPermissions"] = vault.delete(
        "v1/matters/{matterId}",
        t.struct({"matterId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MatterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersCount"] = vault.delete(
        "v1/matters/{matterId}",
        t.struct({"matterId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MatterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersUpdate"] = vault.delete(
        "v1/matters/{matterId}",
        t.struct({"matterId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MatterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersRemovePermissions"] = vault.delete(
        "v1/matters/{matterId}",
        t.struct({"matterId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MatterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersGet"] = vault.delete(
        "v1/matters/{matterId}",
        t.struct({"matterId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MatterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersCreate"] = vault.delete(
        "v1/matters/{matterId}",
        t.struct({"matterId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MatterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersDelete"] = vault.delete(
        "v1/matters/{matterId}",
        t.struct({"matterId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MatterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersExportsDelete"] = vault.get(
        "v1/matters/{matterId}/exports/{exportId}",
        t.struct(
            {
                "exportId": t.string().optional(),
                "matterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersExportsCreate"] = vault.get(
        "v1/matters/{matterId}/exports/{exportId}",
        t.struct(
            {
                "exportId": t.string().optional(),
                "matterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersExportsList"] = vault.get(
        "v1/matters/{matterId}/exports/{exportId}",
        t.struct(
            {
                "exportId": t.string().optional(),
                "matterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersExportsGet"] = vault.get(
        "v1/matters/{matterId}/exports/{exportId}",
        t.struct(
            {
                "exportId": t.string().optional(),
                "matterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersSavedQueriesCreate"] = vault.delete(
        "v1/matters/{matterId}/savedQueries/{savedQueryId}",
        t.struct(
            {
                "matterId": t.string().optional(),
                "savedQueryId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersSavedQueriesGet"] = vault.delete(
        "v1/matters/{matterId}/savedQueries/{savedQueryId}",
        t.struct(
            {
                "matterId": t.string().optional(),
                "savedQueryId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersSavedQueriesList"] = vault.delete(
        "v1/matters/{matterId}/savedQueries/{savedQueryId}",
        t.struct(
            {
                "matterId": t.string().optional(),
                "savedQueryId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersSavedQueriesDelete"] = vault.delete(
        "v1/matters/{matterId}/savedQueries/{savedQueryId}",
        t.struct(
            {
                "matterId": t.string().optional(),
                "savedQueryId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsRemoveHeldAccounts"] = vault.put(
        "v1/matters/{matterId}/holds/{holdId}",
        t.struct(
            {
                "matterId": t.string().optional(),
                "holdId": t.string().optional(),
                "accounts": t.array(t.proxy(renames["HeldAccountIn"])).optional(),
                "corpus": t.string().optional(),
                "orgUnit": t.proxy(renames["HeldOrgUnitIn"]).optional(),
                "name": t.string().optional(),
                "query": t.proxy(renames["CorpusQueryIn"]).optional(),
                "updateTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HoldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsList"] = vault.put(
        "v1/matters/{matterId}/holds/{holdId}",
        t.struct(
            {
                "matterId": t.string().optional(),
                "holdId": t.string().optional(),
                "accounts": t.array(t.proxy(renames["HeldAccountIn"])).optional(),
                "corpus": t.string().optional(),
                "orgUnit": t.proxy(renames["HeldOrgUnitIn"]).optional(),
                "name": t.string().optional(),
                "query": t.proxy(renames["CorpusQueryIn"]).optional(),
                "updateTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HoldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsCreate"] = vault.put(
        "v1/matters/{matterId}/holds/{holdId}",
        t.struct(
            {
                "matterId": t.string().optional(),
                "holdId": t.string().optional(),
                "accounts": t.array(t.proxy(renames["HeldAccountIn"])).optional(),
                "corpus": t.string().optional(),
                "orgUnit": t.proxy(renames["HeldOrgUnitIn"]).optional(),
                "name": t.string().optional(),
                "query": t.proxy(renames["CorpusQueryIn"]).optional(),
                "updateTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HoldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsAddHeldAccounts"] = vault.put(
        "v1/matters/{matterId}/holds/{holdId}",
        t.struct(
            {
                "matterId": t.string().optional(),
                "holdId": t.string().optional(),
                "accounts": t.array(t.proxy(renames["HeldAccountIn"])).optional(),
                "corpus": t.string().optional(),
                "orgUnit": t.proxy(renames["HeldOrgUnitIn"]).optional(),
                "name": t.string().optional(),
                "query": t.proxy(renames["CorpusQueryIn"]).optional(),
                "updateTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HoldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsGet"] = vault.put(
        "v1/matters/{matterId}/holds/{holdId}",
        t.struct(
            {
                "matterId": t.string().optional(),
                "holdId": t.string().optional(),
                "accounts": t.array(t.proxy(renames["HeldAccountIn"])).optional(),
                "corpus": t.string().optional(),
                "orgUnit": t.proxy(renames["HeldOrgUnitIn"]).optional(),
                "name": t.string().optional(),
                "query": t.proxy(renames["CorpusQueryIn"]).optional(),
                "updateTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HoldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsDelete"] = vault.put(
        "v1/matters/{matterId}/holds/{holdId}",
        t.struct(
            {
                "matterId": t.string().optional(),
                "holdId": t.string().optional(),
                "accounts": t.array(t.proxy(renames["HeldAccountIn"])).optional(),
                "corpus": t.string().optional(),
                "orgUnit": t.proxy(renames["HeldOrgUnitIn"]).optional(),
                "name": t.string().optional(),
                "query": t.proxy(renames["CorpusQueryIn"]).optional(),
                "updateTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HoldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsUpdate"] = vault.put(
        "v1/matters/{matterId}/holds/{holdId}",
        t.struct(
            {
                "matterId": t.string().optional(),
                "holdId": t.string().optional(),
                "accounts": t.array(t.proxy(renames["HeldAccountIn"])).optional(),
                "corpus": t.string().optional(),
                "orgUnit": t.proxy(renames["HeldOrgUnitIn"]).optional(),
                "name": t.string().optional(),
                "query": t.proxy(renames["CorpusQueryIn"]).optional(),
                "updateTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HoldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsAccountsList"] = vault.delete(
        "v1/matters/{matterId}/holds/{holdId}/accounts/{accountId}",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsAccountsCreate"] = vault.delete(
        "v1/matters/{matterId}/holds/{holdId}/accounts/{accountId}",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsAccountsDelete"] = vault.delete(
        "v1/matters/{matterId}/holds/{holdId}/accounts/{accountId}",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = vault.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = vault.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = vault.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = vault.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="vault", renames=renames, types=Box(types), functions=Box(functions)
    )
