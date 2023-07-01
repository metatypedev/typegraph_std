from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_vault():
    vault = HTTPRuntime("https://vault.googleapis.com/")

    renames = {
        "ErrorResponse": "_vault_1_ErrorResponse",
        "MailOptionsIn": "_vault_2_MailOptionsIn",
        "MailOptionsOut": "_vault_3_MailOptionsOut",
        "UserInfoIn": "_vault_4_UserInfoIn",
        "UserInfoOut": "_vault_5_UserInfoOut",
        "CloseMatterResponseIn": "_vault_6_CloseMatterResponseIn",
        "CloseMatterResponseOut": "_vault_7_CloseMatterResponseOut",
        "CloudStorageFileIn": "_vault_8_CloudStorageFileIn",
        "CloudStorageFileOut": "_vault_9_CloudStorageFileOut",
        "HeldVoiceQueryIn": "_vault_10_HeldVoiceQueryIn",
        "HeldVoiceQueryOut": "_vault_11_HeldVoiceQueryOut",
        "ReopenMatterResponseIn": "_vault_12_ReopenMatterResponseIn",
        "ReopenMatterResponseOut": "_vault_13_ReopenMatterResponseOut",
        "MatterIn": "_vault_14_MatterIn",
        "MatterOut": "_vault_15_MatterOut",
        "HoldIn": "_vault_16_HoldIn",
        "HoldOut": "_vault_17_HoldOut",
        "CloseMatterRequestIn": "_vault_18_CloseMatterRequestIn",
        "CloseMatterRequestOut": "_vault_19_CloseMatterRequestOut",
        "DriveOptionsIn": "_vault_20_DriveOptionsIn",
        "DriveOptionsOut": "_vault_21_DriveOptionsOut",
        "CountArtifactsMetadataIn": "_vault_22_CountArtifactsMetadataIn",
        "CountArtifactsMetadataOut": "_vault_23_CountArtifactsMetadataOut",
        "HangoutsChatOptionsIn": "_vault_24_HangoutsChatOptionsIn",
        "HangoutsChatOptionsOut": "_vault_25_HangoutsChatOptionsOut",
        "ExportStatsIn": "_vault_26_ExportStatsIn",
        "ExportStatsOut": "_vault_27_ExportStatsOut",
        "ListMattersResponseIn": "_vault_28_ListMattersResponseIn",
        "ListMattersResponseOut": "_vault_29_ListMattersResponseOut",
        "AddHeldAccountResultIn": "_vault_30_AddHeldAccountResultIn",
        "AddHeldAccountResultOut": "_vault_31_AddHeldAccountResultOut",
        "HeldGroupsQueryIn": "_vault_32_HeldGroupsQueryIn",
        "HeldGroupsQueryOut": "_vault_33_HeldGroupsQueryOut",
        "HeldOrgUnitIn": "_vault_34_HeldOrgUnitIn",
        "HeldOrgUnitOut": "_vault_35_HeldOrgUnitOut",
        "ReopenMatterRequestIn": "_vault_36_ReopenMatterRequestIn",
        "ReopenMatterRequestOut": "_vault_37_ReopenMatterRequestOut",
        "CloudStorageSinkIn": "_vault_38_CloudStorageSinkIn",
        "CloudStorageSinkOut": "_vault_39_CloudStorageSinkOut",
        "EmptyIn": "_vault_40_EmptyIn",
        "EmptyOut": "_vault_41_EmptyOut",
        "AccountCountErrorIn": "_vault_42_AccountCountErrorIn",
        "AccountCountErrorOut": "_vault_43_AccountCountErrorOut",
        "ListOperationsResponseIn": "_vault_44_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_vault_45_ListOperationsResponseOut",
        "AddMatterPermissionsRequestIn": "_vault_46_AddMatterPermissionsRequestIn",
        "AddMatterPermissionsRequestOut": "_vault_47_AddMatterPermissionsRequestOut",
        "MailCountResultIn": "_vault_48_MailCountResultIn",
        "MailCountResultOut": "_vault_49_MailCountResultOut",
        "SharedDriveInfoIn": "_vault_50_SharedDriveInfoIn",
        "SharedDriveInfoOut": "_vault_51_SharedDriveInfoOut",
        "RemoveMatterPermissionsRequestIn": "_vault_52_RemoveMatterPermissionsRequestIn",
        "RemoveMatterPermissionsRequestOut": "_vault_53_RemoveMatterPermissionsRequestOut",
        "ListHoldsResponseIn": "_vault_54_ListHoldsResponseIn",
        "ListHoldsResponseOut": "_vault_55_ListHoldsResponseOut",
        "OrgUnitInfoIn": "_vault_56_OrgUnitInfoIn",
        "OrgUnitInfoOut": "_vault_57_OrgUnitInfoOut",
        "MatterPermissionIn": "_vault_58_MatterPermissionIn",
        "MatterPermissionOut": "_vault_59_MatterPermissionOut",
        "AddHeldAccountsRequestIn": "_vault_60_AddHeldAccountsRequestIn",
        "AddHeldAccountsRequestOut": "_vault_61_AddHeldAccountsRequestOut",
        "ListExportsResponseIn": "_vault_62_ListExportsResponseIn",
        "ListExportsResponseOut": "_vault_63_ListExportsResponseOut",
        "UndeleteMatterRequestIn": "_vault_64_UndeleteMatterRequestIn",
        "UndeleteMatterRequestOut": "_vault_65_UndeleteMatterRequestOut",
        "CorpusQueryIn": "_vault_66_CorpusQueryIn",
        "CorpusQueryOut": "_vault_67_CorpusQueryOut",
        "HangoutsChatExportOptionsIn": "_vault_68_HangoutsChatExportOptionsIn",
        "HangoutsChatExportOptionsOut": "_vault_69_HangoutsChatExportOptionsOut",
        "TeamDriveInfoIn": "_vault_70_TeamDriveInfoIn",
        "TeamDriveInfoOut": "_vault_71_TeamDriveInfoOut",
        "ExportIn": "_vault_72_ExportIn",
        "ExportOut": "_vault_73_ExportOut",
        "AddHeldAccountsResponseIn": "_vault_74_AddHeldAccountsResponseIn",
        "AddHeldAccountsResponseOut": "_vault_75_AddHeldAccountsResponseOut",
        "CancelOperationRequestIn": "_vault_76_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_vault_77_CancelOperationRequestOut",
        "ListHeldAccountsResponseIn": "_vault_78_ListHeldAccountsResponseIn",
        "ListHeldAccountsResponseOut": "_vault_79_ListHeldAccountsResponseOut",
        "DriveExportOptionsIn": "_vault_80_DriveExportOptionsIn",
        "DriveExportOptionsOut": "_vault_81_DriveExportOptionsOut",
        "VoiceOptionsIn": "_vault_82_VoiceOptionsIn",
        "VoiceOptionsOut": "_vault_83_VoiceOptionsOut",
        "MailExportOptionsIn": "_vault_84_MailExportOptionsIn",
        "MailExportOptionsOut": "_vault_85_MailExportOptionsOut",
        "ListSavedQueriesResponseIn": "_vault_86_ListSavedQueriesResponseIn",
        "ListSavedQueriesResponseOut": "_vault_87_ListSavedQueriesResponseOut",
        "OperationIn": "_vault_88_OperationIn",
        "OperationOut": "_vault_89_OperationOut",
        "AccountCountIn": "_vault_90_AccountCountIn",
        "AccountCountOut": "_vault_91_AccountCountOut",
        "CountArtifactsResponseIn": "_vault_92_CountArtifactsResponseIn",
        "CountArtifactsResponseOut": "_vault_93_CountArtifactsResponseOut",
        "HeldHangoutsChatQueryIn": "_vault_94_HeldHangoutsChatQueryIn",
        "HeldHangoutsChatQueryOut": "_vault_95_HeldHangoutsChatQueryOut",
        "RemoveHeldAccountsRequestIn": "_vault_96_RemoveHeldAccountsRequestIn",
        "RemoveHeldAccountsRequestOut": "_vault_97_RemoveHeldAccountsRequestOut",
        "HeldMailQueryIn": "_vault_98_HeldMailQueryIn",
        "HeldMailQueryOut": "_vault_99_HeldMailQueryOut",
        "HeldDriveQueryIn": "_vault_100_HeldDriveQueryIn",
        "HeldDriveQueryOut": "_vault_101_HeldDriveQueryOut",
        "GroupsExportOptionsIn": "_vault_102_GroupsExportOptionsIn",
        "GroupsExportOptionsOut": "_vault_103_GroupsExportOptionsOut",
        "RemoveHeldAccountsResponseIn": "_vault_104_RemoveHeldAccountsResponseIn",
        "RemoveHeldAccountsResponseOut": "_vault_105_RemoveHeldAccountsResponseOut",
        "QueryIn": "_vault_106_QueryIn",
        "QueryOut": "_vault_107_QueryOut",
        "HangoutsChatInfoIn": "_vault_108_HangoutsChatInfoIn",
        "HangoutsChatInfoOut": "_vault_109_HangoutsChatInfoOut",
        "CountArtifactsRequestIn": "_vault_110_CountArtifactsRequestIn",
        "CountArtifactsRequestOut": "_vault_111_CountArtifactsRequestOut",
        "HeldAccountIn": "_vault_112_HeldAccountIn",
        "HeldAccountOut": "_vault_113_HeldAccountOut",
        "StatusIn": "_vault_114_StatusIn",
        "StatusOut": "_vault_115_StatusOut",
        "GroupsCountResultIn": "_vault_116_GroupsCountResultIn",
        "GroupsCountResultOut": "_vault_117_GroupsCountResultOut",
        "SavedQueryIn": "_vault_118_SavedQueryIn",
        "SavedQueryOut": "_vault_119_SavedQueryOut",
        "VoiceExportOptionsIn": "_vault_120_VoiceExportOptionsIn",
        "VoiceExportOptionsOut": "_vault_121_VoiceExportOptionsOut",
        "ExportOptionsIn": "_vault_122_ExportOptionsIn",
        "ExportOptionsOut": "_vault_123_ExportOptionsOut",
        "AccountInfoIn": "_vault_124_AccountInfoIn",
        "AccountInfoOut": "_vault_125_AccountInfoOut",
        "SitesUrlInfoIn": "_vault_126_SitesUrlInfoIn",
        "SitesUrlInfoOut": "_vault_127_SitesUrlInfoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["MailOptionsIn"] = t.struct(
        {
            "excludeDrafts": t.boolean().optional(),
            "clientSideEncryptedOption": t.string().optional(),
        }
    ).named(renames["MailOptionsIn"])
    types["MailOptionsOut"] = t.struct(
        {
            "excludeDrafts": t.boolean().optional(),
            "clientSideEncryptedOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MailOptionsOut"])
    types["UserInfoIn"] = t.struct(
        {"displayName": t.string().optional(), "email": t.string().optional()}
    ).named(renames["UserInfoIn"])
    types["UserInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserInfoOut"])
    types["CloseMatterResponseIn"] = t.struct(
        {"matter": t.proxy(renames["MatterIn"]).optional()}
    ).named(renames["CloseMatterResponseIn"])
    types["CloseMatterResponseOut"] = t.struct(
        {
            "matter": t.proxy(renames["MatterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloseMatterResponseOut"])
    types["CloudStorageFileIn"] = t.struct(
        {
            "size": t.string().optional(),
            "objectName": t.string().optional(),
            "bucketName": t.string().optional(),
            "md5Hash": t.string().optional(),
        }
    ).named(renames["CloudStorageFileIn"])
    types["CloudStorageFileOut"] = t.struct(
        {
            "size": t.string().optional(),
            "objectName": t.string().optional(),
            "bucketName": t.string().optional(),
            "md5Hash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudStorageFileOut"])
    types["HeldVoiceQueryIn"] = t.struct(
        {"coveredData": t.array(t.string()).optional()}
    ).named(renames["HeldVoiceQueryIn"])
    types["HeldVoiceQueryOut"] = t.struct(
        {
            "coveredData": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldVoiceQueryOut"])
    types["ReopenMatterResponseIn"] = t.struct(
        {"matter": t.proxy(renames["MatterIn"]).optional()}
    ).named(renames["ReopenMatterResponseIn"])
    types["ReopenMatterResponseOut"] = t.struct(
        {
            "matter": t.proxy(renames["MatterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReopenMatterResponseOut"])
    types["MatterIn"] = t.struct(
        {
            "description": t.string().optional(),
            "matterId": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "matterPermissions": t.array(
                t.proxy(renames["MatterPermissionIn"])
            ).optional(),
        }
    ).named(renames["MatterIn"])
    types["MatterOut"] = t.struct(
        {
            "description": t.string().optional(),
            "matterId": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "matterPermissions": t.array(
                t.proxy(renames["MatterPermissionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatterOut"])
    types["HoldIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "orgUnit": t.proxy(renames["HeldOrgUnitIn"]).optional(),
            "corpus": t.string().optional(),
            "accounts": t.array(t.proxy(renames["HeldAccountIn"])).optional(),
            "holdId": t.string().optional(),
            "query": t.proxy(renames["CorpusQueryIn"]).optional(),
        }
    ).named(renames["HoldIn"])
    types["HoldOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "orgUnit": t.proxy(renames["HeldOrgUnitOut"]).optional(),
            "corpus": t.string().optional(),
            "accounts": t.array(t.proxy(renames["HeldAccountOut"])).optional(),
            "holdId": t.string().optional(),
            "query": t.proxy(renames["CorpusQueryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HoldOut"])
    types["CloseMatterRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloseMatterRequestIn"]
    )
    types["CloseMatterRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloseMatterRequestOut"])
    types["DriveOptionsIn"] = t.struct(
        {
            "clientSideEncryptedOption": t.string().optional(),
            "includeSharedDrives": t.boolean().optional(),
            "includeTeamDrives": t.boolean().optional(),
            "versionDate": t.string().optional(),
        }
    ).named(renames["DriveOptionsIn"])
    types["DriveOptionsOut"] = t.struct(
        {
            "clientSideEncryptedOption": t.string().optional(),
            "includeSharedDrives": t.boolean().optional(),
            "includeTeamDrives": t.boolean().optional(),
            "versionDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveOptionsOut"])
    types["CountArtifactsMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "matterId": t.string().optional(),
            "query": t.proxy(renames["QueryIn"]).optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["CountArtifactsMetadataIn"])
    types["CountArtifactsMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "matterId": t.string().optional(),
            "query": t.proxy(renames["QueryOut"]).optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountArtifactsMetadataOut"])
    types["HangoutsChatOptionsIn"] = t.struct(
        {"includeRooms": t.boolean().optional()}
    ).named(renames["HangoutsChatOptionsIn"])
    types["HangoutsChatOptionsOut"] = t.struct(
        {
            "includeRooms": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HangoutsChatOptionsOut"])
    types["ExportStatsIn"] = t.struct(
        {
            "exportedArtifactCount": t.string().optional(),
            "sizeInBytes": t.string().optional(),
            "totalArtifactCount": t.string().optional(),
        }
    ).named(renames["ExportStatsIn"])
    types["ExportStatsOut"] = t.struct(
        {
            "exportedArtifactCount": t.string().optional(),
            "sizeInBytes": t.string().optional(),
            "totalArtifactCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportStatsOut"])
    types["ListMattersResponseIn"] = t.struct(
        {
            "matters": t.array(t.proxy(renames["MatterIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListMattersResponseIn"])
    types["ListMattersResponseOut"] = t.struct(
        {
            "matters": t.array(t.proxy(renames["MatterOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMattersResponseOut"])
    types["AddHeldAccountResultIn"] = t.struct(
        {
            "status": t.proxy(renames["StatusIn"]).optional(),
            "account": t.proxy(renames["HeldAccountIn"]).optional(),
        }
    ).named(renames["AddHeldAccountResultIn"])
    types["AddHeldAccountResultOut"] = t.struct(
        {
            "status": t.proxy(renames["StatusOut"]).optional(),
            "account": t.proxy(renames["HeldAccountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddHeldAccountResultOut"])
    types["HeldGroupsQueryIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "terms": t.string().optional(),
        }
    ).named(renames["HeldGroupsQueryIn"])
    types["HeldGroupsQueryOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "terms": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldGroupsQueryOut"])
    types["HeldOrgUnitIn"] = t.struct(
        {"holdTime": t.string().optional(), "orgUnitId": t.string().optional()}
    ).named(renames["HeldOrgUnitIn"])
    types["HeldOrgUnitOut"] = t.struct(
        {
            "holdTime": t.string().optional(),
            "orgUnitId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldOrgUnitOut"])
    types["ReopenMatterRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReopenMatterRequestIn"]
    )
    types["ReopenMatterRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReopenMatterRequestOut"])
    types["CloudStorageSinkIn"] = t.struct(
        {"files": t.array(t.proxy(renames["CloudStorageFileIn"])).optional()}
    ).named(renames["CloudStorageSinkIn"])
    types["CloudStorageSinkOut"] = t.struct(
        {
            "files": t.array(t.proxy(renames["CloudStorageFileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudStorageSinkOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["AccountCountErrorIn"] = t.struct(
        {
            "errorType": t.string().optional(),
            "account": t.proxy(renames["UserInfoIn"]).optional(),
        }
    ).named(renames["AccountCountErrorIn"])
    types["AccountCountErrorOut"] = t.struct(
        {
            "errorType": t.string().optional(),
            "account": t.proxy(renames["UserInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountCountErrorOut"])
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
    types["AddMatterPermissionsRequestIn"] = t.struct(
        {
            "ccMe": t.boolean().optional(),
            "sendEmails": t.boolean().optional(),
            "matterPermission": t.proxy(renames["MatterPermissionIn"]).optional(),
        }
    ).named(renames["AddMatterPermissionsRequestIn"])
    types["AddMatterPermissionsRequestOut"] = t.struct(
        {
            "ccMe": t.boolean().optional(),
            "sendEmails": t.boolean().optional(),
            "matterPermission": t.proxy(renames["MatterPermissionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddMatterPermissionsRequestOut"])
    types["MailCountResultIn"] = t.struct(
        {
            "matchingAccountsCount": t.string().optional(),
            "accountCounts": t.array(t.proxy(renames["AccountCountIn"])).optional(),
            "nonQueryableAccounts": t.array(t.string()).optional(),
            "queriedAccountsCount": t.string().optional(),
            "accountCountErrors": t.array(
                t.proxy(renames["AccountCountErrorIn"])
            ).optional(),
        }
    ).named(renames["MailCountResultIn"])
    types["MailCountResultOut"] = t.struct(
        {
            "matchingAccountsCount": t.string().optional(),
            "accountCounts": t.array(t.proxy(renames["AccountCountOut"])).optional(),
            "nonQueryableAccounts": t.array(t.string()).optional(),
            "queriedAccountsCount": t.string().optional(),
            "accountCountErrors": t.array(
                t.proxy(renames["AccountCountErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MailCountResultOut"])
    types["SharedDriveInfoIn"] = t.struct(
        {"sharedDriveIds": t.array(t.string()).optional()}
    ).named(renames["SharedDriveInfoIn"])
    types["SharedDriveInfoOut"] = t.struct(
        {
            "sharedDriveIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SharedDriveInfoOut"])
    types["RemoveMatterPermissionsRequestIn"] = t.struct(
        {"accountId": t.string().optional()}
    ).named(renames["RemoveMatterPermissionsRequestIn"])
    types["RemoveMatterPermissionsRequestOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveMatterPermissionsRequestOut"])
    types["ListHoldsResponseIn"] = t.struct(
        {
            "holds": t.array(t.proxy(renames["HoldIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListHoldsResponseIn"])
    types["ListHoldsResponseOut"] = t.struct(
        {
            "holds": t.array(t.proxy(renames["HoldOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListHoldsResponseOut"])
    types["OrgUnitInfoIn"] = t.struct({"orgUnitId": t.string().optional()}).named(
        renames["OrgUnitInfoIn"]
    )
    types["OrgUnitInfoOut"] = t.struct(
        {
            "orgUnitId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrgUnitInfoOut"])
    types["MatterPermissionIn"] = t.struct(
        {"role": t.string().optional(), "accountId": t.string().optional()}
    ).named(renames["MatterPermissionIn"])
    types["MatterPermissionOut"] = t.struct(
        {
            "role": t.string().optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatterPermissionOut"])
    types["AddHeldAccountsRequestIn"] = t.struct(
        {
            "emails": t.array(t.string()).optional(),
            "accountIds": t.array(t.string()).optional(),
        }
    ).named(renames["AddHeldAccountsRequestIn"])
    types["AddHeldAccountsRequestOut"] = t.struct(
        {
            "emails": t.array(t.string()).optional(),
            "accountIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddHeldAccountsRequestOut"])
    types["ListExportsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "exports": t.array(t.proxy(renames["ExportIn"])).optional(),
        }
    ).named(renames["ListExportsResponseIn"])
    types["ListExportsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "exports": t.array(t.proxy(renames["ExportOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListExportsResponseOut"])
    types["UndeleteMatterRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteMatterRequestIn"]
    )
    types["UndeleteMatterRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteMatterRequestOut"])
    types["CorpusQueryIn"] = t.struct(
        {
            "hangoutsChatQuery": t.proxy(renames["HeldHangoutsChatQueryIn"]).optional(),
            "voiceQuery": t.proxy(renames["HeldVoiceQueryIn"]).optional(),
            "groupsQuery": t.proxy(renames["HeldGroupsQueryIn"]).optional(),
            "driveQuery": t.proxy(renames["HeldDriveQueryIn"]).optional(),
            "mailQuery": t.proxy(renames["HeldMailQueryIn"]).optional(),
        }
    ).named(renames["CorpusQueryIn"])
    types["CorpusQueryOut"] = t.struct(
        {
            "hangoutsChatQuery": t.proxy(
                renames["HeldHangoutsChatQueryOut"]
            ).optional(),
            "voiceQuery": t.proxy(renames["HeldVoiceQueryOut"]).optional(),
            "groupsQuery": t.proxy(renames["HeldGroupsQueryOut"]).optional(),
            "driveQuery": t.proxy(renames["HeldDriveQueryOut"]).optional(),
            "mailQuery": t.proxy(renames["HeldMailQueryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CorpusQueryOut"])
    types["HangoutsChatExportOptionsIn"] = t.struct(
        {"exportFormat": t.string().optional()}
    ).named(renames["HangoutsChatExportOptionsIn"])
    types["HangoutsChatExportOptionsOut"] = t.struct(
        {
            "exportFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HangoutsChatExportOptionsOut"])
    types["TeamDriveInfoIn"] = t.struct(
        {"teamDriveIds": t.array(t.string()).optional()}
    ).named(renames["TeamDriveInfoIn"])
    types["TeamDriveInfoOut"] = t.struct(
        {
            "teamDriveIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TeamDriveInfoOut"])
    types["ExportIn"] = t.struct(
        {
            "stats": t.proxy(renames["ExportStatsIn"]).optional(),
            "matterId": t.string().optional(),
            "exportOptions": t.proxy(renames["ExportOptionsIn"]).optional(),
            "status": t.string().optional(),
            "cloudStorageSink": t.proxy(renames["CloudStorageSinkIn"]).optional(),
            "query": t.proxy(renames["QueryIn"]).optional(),
            "requester": t.proxy(renames["UserInfoIn"]).optional(),
            "createTime": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ExportIn"])
    types["ExportOut"] = t.struct(
        {
            "stats": t.proxy(renames["ExportStatsOut"]).optional(),
            "matterId": t.string().optional(),
            "exportOptions": t.proxy(renames["ExportOptionsOut"]).optional(),
            "status": t.string().optional(),
            "cloudStorageSink": t.proxy(renames["CloudStorageSinkOut"]).optional(),
            "query": t.proxy(renames["QueryOut"]).optional(),
            "requester": t.proxy(renames["UserInfoOut"]).optional(),
            "createTime": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ListHeldAccountsResponseIn"] = t.struct(
        {"accounts": t.array(t.proxy(renames["HeldAccountIn"])).optional()}
    ).named(renames["ListHeldAccountsResponseIn"])
    types["ListHeldAccountsResponseOut"] = t.struct(
        {
            "accounts": t.array(t.proxy(renames["HeldAccountOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListHeldAccountsResponseOut"])
    types["DriveExportOptionsIn"] = t.struct(
        {"includeAccessInfo": t.boolean().optional()}
    ).named(renames["DriveExportOptionsIn"])
    types["DriveExportOptionsOut"] = t.struct(
        {
            "includeAccessInfo": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveExportOptionsOut"])
    types["VoiceOptionsIn"] = t.struct(
        {"coveredData": t.array(t.string()).optional()}
    ).named(renames["VoiceOptionsIn"])
    types["VoiceOptionsOut"] = t.struct(
        {
            "coveredData": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceOptionsOut"])
    types["MailExportOptionsIn"] = t.struct(
        {
            "useNewExport": t.boolean().optional(),
            "exportFormat": t.string().optional(),
            "showConfidentialModeContent": t.boolean().optional(),
        }
    ).named(renames["MailExportOptionsIn"])
    types["MailExportOptionsOut"] = t.struct(
        {
            "useNewExport": t.boolean().optional(),
            "exportFormat": t.string().optional(),
            "showConfidentialModeContent": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MailExportOptionsOut"])
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
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["AccountCountIn"] = t.struct(
        {
            "count": t.string().optional(),
            "account": t.proxy(renames["UserInfoIn"]).optional(),
        }
    ).named(renames["AccountCountIn"])
    types["AccountCountOut"] = t.struct(
        {
            "count": t.string().optional(),
            "account": t.proxy(renames["UserInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountCountOut"])
    types["CountArtifactsResponseIn"] = t.struct(
        {
            "groupsCountResult": t.proxy(renames["GroupsCountResultIn"]).optional(),
            "totalCount": t.string().optional(),
            "mailCountResult": t.proxy(renames["MailCountResultIn"]).optional(),
        }
    ).named(renames["CountArtifactsResponseIn"])
    types["CountArtifactsResponseOut"] = t.struct(
        {
            "groupsCountResult": t.proxy(renames["GroupsCountResultOut"]).optional(),
            "totalCount": t.string().optional(),
            "mailCountResult": t.proxy(renames["MailCountResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountArtifactsResponseOut"])
    types["HeldHangoutsChatQueryIn"] = t.struct(
        {"includeRooms": t.boolean().optional()}
    ).named(renames["HeldHangoutsChatQueryIn"])
    types["HeldHangoutsChatQueryOut"] = t.struct(
        {
            "includeRooms": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldHangoutsChatQueryOut"])
    types["RemoveHeldAccountsRequestIn"] = t.struct(
        {"accountIds": t.array(t.string()).optional()}
    ).named(renames["RemoveHeldAccountsRequestIn"])
    types["RemoveHeldAccountsRequestOut"] = t.struct(
        {
            "accountIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveHeldAccountsRequestOut"])
    types["HeldMailQueryIn"] = t.struct(
        {
            "terms": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["HeldMailQueryIn"])
    types["HeldMailQueryOut"] = t.struct(
        {
            "terms": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldMailQueryOut"])
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
    types["GroupsExportOptionsIn"] = t.struct(
        {"exportFormat": t.string().optional()}
    ).named(renames["GroupsExportOptionsIn"])
    types["GroupsExportOptionsOut"] = t.struct(
        {
            "exportFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupsExportOptionsOut"])
    types["RemoveHeldAccountsResponseIn"] = t.struct(
        {"statuses": t.array(t.proxy(renames["StatusIn"])).optional()}
    ).named(renames["RemoveHeldAccountsResponseIn"])
    types["RemoveHeldAccountsResponseOut"] = t.struct(
        {
            "statuses": t.array(t.proxy(renames["StatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveHeldAccountsResponseOut"])
    types["QueryIn"] = t.struct(
        {
            "searchMethod": t.string().optional(),
            "teamDriveInfo": t.proxy(renames["TeamDriveInfoIn"]),
            "hangoutsChatOptions": t.proxy(renames["HangoutsChatOptionsIn"]).optional(),
            "sitesUrlInfo": t.proxy(renames["SitesUrlInfoIn"]),
            "endTime": t.string().optional(),
            "accountInfo": t.proxy(renames["AccountInfoIn"]),
            "sharedDriveInfo": t.proxy(renames["SharedDriveInfoIn"]),
            "dataScope": t.string().optional(),
            "method": t.string().optional(),
            "terms": t.string().optional(),
            "voiceOptions": t.proxy(renames["VoiceOptionsIn"]).optional(),
            "startTime": t.string().optional(),
            "orgUnitInfo": t.proxy(renames["OrgUnitInfoIn"]),
            "corpus": t.string().optional(),
            "hangoutsChatInfo": t.proxy(renames["HangoutsChatInfoIn"]),
            "mailOptions": t.proxy(renames["MailOptionsIn"]).optional(),
            "timeZone": t.string().optional(),
            "driveOptions": t.proxy(renames["DriveOptionsIn"]).optional(),
        }
    ).named(renames["QueryIn"])
    types["QueryOut"] = t.struct(
        {
            "searchMethod": t.string().optional(),
            "teamDriveInfo": t.proxy(renames["TeamDriveInfoOut"]),
            "hangoutsChatOptions": t.proxy(
                renames["HangoutsChatOptionsOut"]
            ).optional(),
            "sitesUrlInfo": t.proxy(renames["SitesUrlInfoOut"]),
            "endTime": t.string().optional(),
            "accountInfo": t.proxy(renames["AccountInfoOut"]),
            "sharedDriveInfo": t.proxy(renames["SharedDriveInfoOut"]),
            "dataScope": t.string().optional(),
            "method": t.string().optional(),
            "terms": t.string().optional(),
            "voiceOptions": t.proxy(renames["VoiceOptionsOut"]).optional(),
            "startTime": t.string().optional(),
            "orgUnitInfo": t.proxy(renames["OrgUnitInfoOut"]),
            "corpus": t.string().optional(),
            "hangoutsChatInfo": t.proxy(renames["HangoutsChatInfoOut"]),
            "mailOptions": t.proxy(renames["MailOptionsOut"]).optional(),
            "timeZone": t.string().optional(),
            "driveOptions": t.proxy(renames["DriveOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryOut"])
    types["HangoutsChatInfoIn"] = t.struct(
        {"roomId": t.array(t.string()).optional()}
    ).named(renames["HangoutsChatInfoIn"])
    types["HangoutsChatInfoOut"] = t.struct(
        {
            "roomId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HangoutsChatInfoOut"])
    types["CountArtifactsRequestIn"] = t.struct(
        {"query": t.proxy(renames["QueryIn"]).optional(), "view": t.string().optional()}
    ).named(renames["CountArtifactsRequestIn"])
    types["CountArtifactsRequestOut"] = t.struct(
        {
            "query": t.proxy(renames["QueryOut"]).optional(),
            "view": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountArtifactsRequestOut"])
    types["HeldAccountIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "holdTime": t.string().optional(),
            "firstName": t.string().optional(),
            "lastName": t.string().optional(),
            "email": t.string().optional(),
        }
    ).named(renames["HeldAccountIn"])
    types["HeldAccountOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "holdTime": t.string().optional(),
            "firstName": t.string().optional(),
            "lastName": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldAccountOut"])
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
    types["GroupsCountResultIn"] = t.struct(
        {
            "accountCounts": t.array(t.proxy(renames["AccountCountIn"])).optional(),
            "nonQueryableAccounts": t.array(t.string()).optional(),
            "matchingAccountsCount": t.string().optional(),
            "queriedAccountsCount": t.string().optional(),
            "accountCountErrors": t.array(
                t.proxy(renames["AccountCountErrorIn"])
            ).optional(),
        }
    ).named(renames["GroupsCountResultIn"])
    types["GroupsCountResultOut"] = t.struct(
        {
            "accountCounts": t.array(t.proxy(renames["AccountCountOut"])).optional(),
            "nonQueryableAccounts": t.array(t.string()).optional(),
            "matchingAccountsCount": t.string().optional(),
            "queriedAccountsCount": t.string().optional(),
            "accountCountErrors": t.array(
                t.proxy(renames["AccountCountErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupsCountResultOut"])
    types["SavedQueryIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "matterId": t.string().optional(),
            "displayName": t.string().optional(),
            "savedQueryId": t.string().optional(),
            "query": t.proxy(renames["QueryIn"]).optional(),
        }
    ).named(renames["SavedQueryIn"])
    types["SavedQueryOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "matterId": t.string().optional(),
            "displayName": t.string().optional(),
            "savedQueryId": t.string().optional(),
            "query": t.proxy(renames["QueryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SavedQueryOut"])
    types["VoiceExportOptionsIn"] = t.struct(
        {"exportFormat": t.string().optional()}
    ).named(renames["VoiceExportOptionsIn"])
    types["VoiceExportOptionsOut"] = t.struct(
        {
            "exportFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceExportOptionsOut"])
    types["ExportOptionsIn"] = t.struct(
        {
            "region": t.string().optional(),
            "hangoutsChatOptions": t.proxy(
                renames["HangoutsChatExportOptionsIn"]
            ).optional(),
            "mailOptions": t.proxy(renames["MailExportOptionsIn"]).optional(),
            "groupsOptions": t.proxy(renames["GroupsExportOptionsIn"]).optional(),
            "driveOptions": t.proxy(renames["DriveExportOptionsIn"]).optional(),
            "voiceOptions": t.proxy(renames["VoiceExportOptionsIn"]).optional(),
        }
    ).named(renames["ExportOptionsIn"])
    types["ExportOptionsOut"] = t.struct(
        {
            "region": t.string().optional(),
            "hangoutsChatOptions": t.proxy(
                renames["HangoutsChatExportOptionsOut"]
            ).optional(),
            "mailOptions": t.proxy(renames["MailExportOptionsOut"]).optional(),
            "groupsOptions": t.proxy(renames["GroupsExportOptionsOut"]).optional(),
            "driveOptions": t.proxy(renames["DriveExportOptionsOut"]).optional(),
            "voiceOptions": t.proxy(renames["VoiceExportOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportOptionsOut"])
    types["AccountInfoIn"] = t.struct({"emails": t.array(t.string()).optional()}).named(
        renames["AccountInfoIn"]
    )
    types["AccountInfoOut"] = t.struct(
        {
            "emails": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountInfoOut"])
    types["SitesUrlInfoIn"] = t.struct({"urls": t.array(t.string()).optional()}).named(
        renames["SitesUrlInfoIn"]
    )
    types["SitesUrlInfoOut"] = t.struct(
        {
            "urls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SitesUrlInfoOut"])

    functions = {}
    functions["operationsGet"] = vault.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = vault.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = vault.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = vault.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersGet"] = vault.post(
        "v1/matters/{matterId}:reopen",
        t.struct(
            {
                "matterId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReopenMatterResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersDelete"] = vault.post(
        "v1/matters/{matterId}:reopen",
        t.struct(
            {
                "matterId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReopenMatterResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersList"] = vault.post(
        "v1/matters/{matterId}:reopen",
        t.struct(
            {
                "matterId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReopenMatterResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersAddPermissions"] = vault.post(
        "v1/matters/{matterId}:reopen",
        t.struct(
            {
                "matterId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReopenMatterResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersUndelete"] = vault.post(
        "v1/matters/{matterId}:reopen",
        t.struct(
            {
                "matterId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReopenMatterResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersUpdate"] = vault.post(
        "v1/matters/{matterId}:reopen",
        t.struct(
            {
                "matterId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReopenMatterResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersCount"] = vault.post(
        "v1/matters/{matterId}:reopen",
        t.struct(
            {
                "matterId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReopenMatterResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersCreate"] = vault.post(
        "v1/matters/{matterId}:reopen",
        t.struct(
            {
                "matterId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReopenMatterResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersRemovePermissions"] = vault.post(
        "v1/matters/{matterId}:reopen",
        t.struct(
            {
                "matterId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReopenMatterResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersClose"] = vault.post(
        "v1/matters/{matterId}:reopen",
        t.struct(
            {
                "matterId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReopenMatterResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersReopen"] = vault.post(
        "v1/matters/{matterId}:reopen",
        t.struct(
            {
                "matterId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReopenMatterResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsAddHeldAccounts"] = vault.post(
        "v1/matters/{matterId}/holds/{holdId}:removeHeldAccounts",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "accountIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemoveHeldAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsList"] = vault.post(
        "v1/matters/{matterId}/holds/{holdId}:removeHeldAccounts",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "accountIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemoveHeldAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsUpdate"] = vault.post(
        "v1/matters/{matterId}/holds/{holdId}:removeHeldAccounts",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "accountIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemoveHeldAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsDelete"] = vault.post(
        "v1/matters/{matterId}/holds/{holdId}:removeHeldAccounts",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "accountIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemoveHeldAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsGet"] = vault.post(
        "v1/matters/{matterId}/holds/{holdId}:removeHeldAccounts",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "accountIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemoveHeldAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsCreate"] = vault.post(
        "v1/matters/{matterId}/holds/{holdId}:removeHeldAccounts",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "accountIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemoveHeldAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsRemoveHeldAccounts"] = vault.post(
        "v1/matters/{matterId}/holds/{holdId}:removeHeldAccounts",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "accountIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemoveHeldAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsAccountsList"] = vault.post(
        "v1/matters/{matterId}/holds/{holdId}/accounts",
        t.struct(
            {
                "matterId": t.string().optional(),
                "holdId": t.string().optional(),
                "accountId": t.string().optional(),
                "holdTime": t.string().optional(),
                "firstName": t.string().optional(),
                "lastName": t.string().optional(),
                "email": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HeldAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsAccountsDelete"] = vault.post(
        "v1/matters/{matterId}/holds/{holdId}/accounts",
        t.struct(
            {
                "matterId": t.string().optional(),
                "holdId": t.string().optional(),
                "accountId": t.string().optional(),
                "holdTime": t.string().optional(),
                "firstName": t.string().optional(),
                "lastName": t.string().optional(),
                "email": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HeldAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsAccountsCreate"] = vault.post(
        "v1/matters/{matterId}/holds/{holdId}/accounts",
        t.struct(
            {
                "matterId": t.string().optional(),
                "holdId": t.string().optional(),
                "accountId": t.string().optional(),
                "holdTime": t.string().optional(),
                "firstName": t.string().optional(),
                "lastName": t.string().optional(),
                "email": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HeldAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersExportsDelete"] = vault.post(
        "v1/matters/{matterId}/exports",
        t.struct(
            {
                "matterId": t.string().optional(),
                "stats": t.proxy(renames["ExportStatsIn"]).optional(),
                "exportOptions": t.proxy(renames["ExportOptionsIn"]).optional(),
                "status": t.string().optional(),
                "cloudStorageSink": t.proxy(renames["CloudStorageSinkIn"]).optional(),
                "query": t.proxy(renames["QueryIn"]).optional(),
                "requester": t.proxy(renames["UserInfoIn"]).optional(),
                "createTime": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersExportsList"] = vault.post(
        "v1/matters/{matterId}/exports",
        t.struct(
            {
                "matterId": t.string().optional(),
                "stats": t.proxy(renames["ExportStatsIn"]).optional(),
                "exportOptions": t.proxy(renames["ExportOptionsIn"]).optional(),
                "status": t.string().optional(),
                "cloudStorageSink": t.proxy(renames["CloudStorageSinkIn"]).optional(),
                "query": t.proxy(renames["QueryIn"]).optional(),
                "requester": t.proxy(renames["UserInfoIn"]).optional(),
                "createTime": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersExportsGet"] = vault.post(
        "v1/matters/{matterId}/exports",
        t.struct(
            {
                "matterId": t.string().optional(),
                "stats": t.proxy(renames["ExportStatsIn"]).optional(),
                "exportOptions": t.proxy(renames["ExportOptionsIn"]).optional(),
                "status": t.string().optional(),
                "cloudStorageSink": t.proxy(renames["CloudStorageSinkIn"]).optional(),
                "query": t.proxy(renames["QueryIn"]).optional(),
                "requester": t.proxy(renames["UserInfoIn"]).optional(),
                "createTime": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersExportsCreate"] = vault.post(
        "v1/matters/{matterId}/exports",
        t.struct(
            {
                "matterId": t.string().optional(),
                "stats": t.proxy(renames["ExportStatsIn"]).optional(),
                "exportOptions": t.proxy(renames["ExportOptionsIn"]).optional(),
                "status": t.string().optional(),
                "cloudStorageSink": t.proxy(renames["CloudStorageSinkIn"]).optional(),
                "query": t.proxy(renames["QueryIn"]).optional(),
                "requester": t.proxy(renames["UserInfoIn"]).optional(),
                "createTime": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersSavedQueriesList"] = vault.post(
        "v1/matters/{matterId}/savedQueries",
        t.struct(
            {
                "matterId": t.string().optional(),
                "createTime": t.string().optional(),
                "displayName": t.string().optional(),
                "savedQueryId": t.string().optional(),
                "query": t.proxy(renames["QueryIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersSavedQueriesGet"] = vault.post(
        "v1/matters/{matterId}/savedQueries",
        t.struct(
            {
                "matterId": t.string().optional(),
                "createTime": t.string().optional(),
                "displayName": t.string().optional(),
                "savedQueryId": t.string().optional(),
                "query": t.proxy(renames["QueryIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersSavedQueriesDelete"] = vault.post(
        "v1/matters/{matterId}/savedQueries",
        t.struct(
            {
                "matterId": t.string().optional(),
                "createTime": t.string().optional(),
                "displayName": t.string().optional(),
                "savedQueryId": t.string().optional(),
                "query": t.proxy(renames["QueryIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersSavedQueriesCreate"] = vault.post(
        "v1/matters/{matterId}/savedQueries",
        t.struct(
            {
                "matterId": t.string().optional(),
                "createTime": t.string().optional(),
                "displayName": t.string().optional(),
                "savedQueryId": t.string().optional(),
                "query": t.proxy(renames["QueryIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="vault", renames=renames, types=Box(types), functions=Box(functions)
    )
