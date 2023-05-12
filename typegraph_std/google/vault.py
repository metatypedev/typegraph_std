from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_vault() -> Import:
    vault = HTTPRuntime("https://vault.googleapis.com/")

    renames = {
        "ErrorResponse": "_vault_1_ErrorResponse",
        "HangoutsChatExportOptionsIn": "_vault_2_HangoutsChatExportOptionsIn",
        "HangoutsChatExportOptionsOut": "_vault_3_HangoutsChatExportOptionsOut",
        "HangoutsChatOptionsIn": "_vault_4_HangoutsChatOptionsIn",
        "HangoutsChatOptionsOut": "_vault_5_HangoutsChatOptionsOut",
        "HeldAccountIn": "_vault_6_HeldAccountIn",
        "HeldAccountOut": "_vault_7_HeldAccountOut",
        "HeldGroupsQueryIn": "_vault_8_HeldGroupsQueryIn",
        "HeldGroupsQueryOut": "_vault_9_HeldGroupsQueryOut",
        "CloseMatterResponseIn": "_vault_10_CloseMatterResponseIn",
        "CloseMatterResponseOut": "_vault_11_CloseMatterResponseOut",
        "CountArtifactsResponseIn": "_vault_12_CountArtifactsResponseIn",
        "CountArtifactsResponseOut": "_vault_13_CountArtifactsResponseOut",
        "VoiceOptionsIn": "_vault_14_VoiceOptionsIn",
        "VoiceOptionsOut": "_vault_15_VoiceOptionsOut",
        "CloudStorageFileIn": "_vault_16_CloudStorageFileIn",
        "CloudStorageFileOut": "_vault_17_CloudStorageFileOut",
        "HangoutsChatInfoIn": "_vault_18_HangoutsChatInfoIn",
        "HangoutsChatInfoOut": "_vault_19_HangoutsChatInfoOut",
        "OrgUnitInfoIn": "_vault_20_OrgUnitInfoIn",
        "OrgUnitInfoOut": "_vault_21_OrgUnitInfoOut",
        "UserInfoIn": "_vault_22_UserInfoIn",
        "UserInfoOut": "_vault_23_UserInfoOut",
        "SitesUrlInfoIn": "_vault_24_SitesUrlInfoIn",
        "SitesUrlInfoOut": "_vault_25_SitesUrlInfoOut",
        "DriveExportOptionsIn": "_vault_26_DriveExportOptionsIn",
        "DriveExportOptionsOut": "_vault_27_DriveExportOptionsOut",
        "ReopenMatterResponseIn": "_vault_28_ReopenMatterResponseIn",
        "ReopenMatterResponseOut": "_vault_29_ReopenMatterResponseOut",
        "ListExportsResponseIn": "_vault_30_ListExportsResponseIn",
        "ListExportsResponseOut": "_vault_31_ListExportsResponseOut",
        "RemoveMatterPermissionsRequestIn": "_vault_32_RemoveMatterPermissionsRequestIn",
        "RemoveMatterPermissionsRequestOut": "_vault_33_RemoveMatterPermissionsRequestOut",
        "GroupsCountResultIn": "_vault_34_GroupsCountResultIn",
        "GroupsCountResultOut": "_vault_35_GroupsCountResultOut",
        "HeldMailQueryIn": "_vault_36_HeldMailQueryIn",
        "HeldMailQueryOut": "_vault_37_HeldMailQueryOut",
        "AddHeldAccountsResponseIn": "_vault_38_AddHeldAccountsResponseIn",
        "AddHeldAccountsResponseOut": "_vault_39_AddHeldAccountsResponseOut",
        "ExportOptionsIn": "_vault_40_ExportOptionsIn",
        "ExportOptionsOut": "_vault_41_ExportOptionsOut",
        "UndeleteMatterRequestIn": "_vault_42_UndeleteMatterRequestIn",
        "UndeleteMatterRequestOut": "_vault_43_UndeleteMatterRequestOut",
        "GroupsExportOptionsIn": "_vault_44_GroupsExportOptionsIn",
        "GroupsExportOptionsOut": "_vault_45_GroupsExportOptionsOut",
        "HeldHangoutsChatQueryIn": "_vault_46_HeldHangoutsChatQueryIn",
        "HeldHangoutsChatQueryOut": "_vault_47_HeldHangoutsChatQueryOut",
        "ListMattersResponseIn": "_vault_48_ListMattersResponseIn",
        "ListMattersResponseOut": "_vault_49_ListMattersResponseOut",
        "ListHoldsResponseIn": "_vault_50_ListHoldsResponseIn",
        "ListHoldsResponseOut": "_vault_51_ListHoldsResponseOut",
        "ExportStatsIn": "_vault_52_ExportStatsIn",
        "ExportStatsOut": "_vault_53_ExportStatsOut",
        "AccountCountIn": "_vault_54_AccountCountIn",
        "AccountCountOut": "_vault_55_AccountCountOut",
        "QueryIn": "_vault_56_QueryIn",
        "QueryOut": "_vault_57_QueryOut",
        "ListHeldAccountsResponseIn": "_vault_58_ListHeldAccountsResponseIn",
        "ListHeldAccountsResponseOut": "_vault_59_ListHeldAccountsResponseOut",
        "MailOptionsIn": "_vault_60_MailOptionsIn",
        "MailOptionsOut": "_vault_61_MailOptionsOut",
        "CorpusQueryIn": "_vault_62_CorpusQueryIn",
        "CorpusQueryOut": "_vault_63_CorpusQueryOut",
        "MatterIn": "_vault_64_MatterIn",
        "MatterOut": "_vault_65_MatterOut",
        "HoldIn": "_vault_66_HoldIn",
        "HoldOut": "_vault_67_HoldOut",
        "CancelOperationRequestIn": "_vault_68_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_vault_69_CancelOperationRequestOut",
        "MatterPermissionIn": "_vault_70_MatterPermissionIn",
        "MatterPermissionOut": "_vault_71_MatterPermissionOut",
        "AddHeldAccountsRequestIn": "_vault_72_AddHeldAccountsRequestIn",
        "AddHeldAccountsRequestOut": "_vault_73_AddHeldAccountsRequestOut",
        "CountArtifactsMetadataIn": "_vault_74_CountArtifactsMetadataIn",
        "CountArtifactsMetadataOut": "_vault_75_CountArtifactsMetadataOut",
        "CloudStorageSinkIn": "_vault_76_CloudStorageSinkIn",
        "CloudStorageSinkOut": "_vault_77_CloudStorageSinkOut",
        "SharedDriveInfoIn": "_vault_78_SharedDriveInfoIn",
        "SharedDriveInfoOut": "_vault_79_SharedDriveInfoOut",
        "ReopenMatterRequestIn": "_vault_80_ReopenMatterRequestIn",
        "ReopenMatterRequestOut": "_vault_81_ReopenMatterRequestOut",
        "HeldVoiceQueryIn": "_vault_82_HeldVoiceQueryIn",
        "HeldVoiceQueryOut": "_vault_83_HeldVoiceQueryOut",
        "RemoveHeldAccountsRequestIn": "_vault_84_RemoveHeldAccountsRequestIn",
        "RemoveHeldAccountsRequestOut": "_vault_85_RemoveHeldAccountsRequestOut",
        "MailCountResultIn": "_vault_86_MailCountResultIn",
        "MailCountResultOut": "_vault_87_MailCountResultOut",
        "VoiceExportOptionsIn": "_vault_88_VoiceExportOptionsIn",
        "VoiceExportOptionsOut": "_vault_89_VoiceExportOptionsOut",
        "AddMatterPermissionsRequestIn": "_vault_90_AddMatterPermissionsRequestIn",
        "AddMatterPermissionsRequestOut": "_vault_91_AddMatterPermissionsRequestOut",
        "CloseMatterRequestIn": "_vault_92_CloseMatterRequestIn",
        "CloseMatterRequestOut": "_vault_93_CloseMatterRequestOut",
        "ListSavedQueriesResponseIn": "_vault_94_ListSavedQueriesResponseIn",
        "ListSavedQueriesResponseOut": "_vault_95_ListSavedQueriesResponseOut",
        "DriveOptionsIn": "_vault_96_DriveOptionsIn",
        "DriveOptionsOut": "_vault_97_DriveOptionsOut",
        "ExportIn": "_vault_98_ExportIn",
        "ExportOut": "_vault_99_ExportOut",
        "ListOperationsResponseIn": "_vault_100_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_vault_101_ListOperationsResponseOut",
        "AccountInfoIn": "_vault_102_AccountInfoIn",
        "AccountInfoOut": "_vault_103_AccountInfoOut",
        "TeamDriveInfoIn": "_vault_104_TeamDriveInfoIn",
        "TeamDriveInfoOut": "_vault_105_TeamDriveInfoOut",
        "AccountCountErrorIn": "_vault_106_AccountCountErrorIn",
        "AccountCountErrorOut": "_vault_107_AccountCountErrorOut",
        "SavedQueryIn": "_vault_108_SavedQueryIn",
        "SavedQueryOut": "_vault_109_SavedQueryOut",
        "MailExportOptionsIn": "_vault_110_MailExportOptionsIn",
        "MailExportOptionsOut": "_vault_111_MailExportOptionsOut",
        "HeldDriveQueryIn": "_vault_112_HeldDriveQueryIn",
        "HeldDriveQueryOut": "_vault_113_HeldDriveQueryOut",
        "OperationIn": "_vault_114_OperationIn",
        "OperationOut": "_vault_115_OperationOut",
        "StatusIn": "_vault_116_StatusIn",
        "StatusOut": "_vault_117_StatusOut",
        "EmptyIn": "_vault_118_EmptyIn",
        "EmptyOut": "_vault_119_EmptyOut",
        "HeldOrgUnitIn": "_vault_120_HeldOrgUnitIn",
        "HeldOrgUnitOut": "_vault_121_HeldOrgUnitOut",
        "RemoveHeldAccountsResponseIn": "_vault_122_RemoveHeldAccountsResponseIn",
        "RemoveHeldAccountsResponseOut": "_vault_123_RemoveHeldAccountsResponseOut",
        "CountArtifactsRequestIn": "_vault_124_CountArtifactsRequestIn",
        "CountArtifactsRequestOut": "_vault_125_CountArtifactsRequestOut",
        "AddHeldAccountResultIn": "_vault_126_AddHeldAccountResultIn",
        "AddHeldAccountResultOut": "_vault_127_AddHeldAccountResultOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["HangoutsChatExportOptionsIn"] = t.struct(
        {"exportFormat": t.string().optional()}
    ).named(renames["HangoutsChatExportOptionsIn"])
    types["HangoutsChatExportOptionsOut"] = t.struct(
        {
            "exportFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HangoutsChatExportOptionsOut"])
    types["HangoutsChatOptionsIn"] = t.struct(
        {"includeRooms": t.boolean().optional()}
    ).named(renames["HangoutsChatOptionsIn"])
    types["HangoutsChatOptionsOut"] = t.struct(
        {
            "includeRooms": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HangoutsChatOptionsOut"])
    types["HeldAccountIn"] = t.struct(
        {
            "lastName": t.string().optional(),
            "accountId": t.string().optional(),
            "firstName": t.string().optional(),
            "holdTime": t.string().optional(),
            "email": t.string().optional(),
        }
    ).named(renames["HeldAccountIn"])
    types["HeldAccountOut"] = t.struct(
        {
            "lastName": t.string().optional(),
            "accountId": t.string().optional(),
            "firstName": t.string().optional(),
            "holdTime": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldAccountOut"])
    types["HeldGroupsQueryIn"] = t.struct(
        {
            "terms": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["HeldGroupsQueryIn"])
    types["HeldGroupsQueryOut"] = t.struct(
        {
            "terms": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldGroupsQueryOut"])
    types["CloseMatterResponseIn"] = t.struct(
        {"matter": t.proxy(renames["MatterIn"]).optional()}
    ).named(renames["CloseMatterResponseIn"])
    types["CloseMatterResponseOut"] = t.struct(
        {
            "matter": t.proxy(renames["MatterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloseMatterResponseOut"])
    types["CountArtifactsResponseIn"] = t.struct(
        {
            "totalCount": t.string().optional(),
            "mailCountResult": t.proxy(renames["MailCountResultIn"]).optional(),
            "groupsCountResult": t.proxy(renames["GroupsCountResultIn"]).optional(),
        }
    ).named(renames["CountArtifactsResponseIn"])
    types["CountArtifactsResponseOut"] = t.struct(
        {
            "totalCount": t.string().optional(),
            "mailCountResult": t.proxy(renames["MailCountResultOut"]).optional(),
            "groupsCountResult": t.proxy(renames["GroupsCountResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountArtifactsResponseOut"])
    types["VoiceOptionsIn"] = t.struct(
        {"coveredData": t.array(t.string()).optional()}
    ).named(renames["VoiceOptionsIn"])
    types["VoiceOptionsOut"] = t.struct(
        {
            "coveredData": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceOptionsOut"])
    types["CloudStorageFileIn"] = t.struct(
        {
            "bucketName": t.string().optional(),
            "size": t.string().optional(),
            "md5Hash": t.string().optional(),
            "objectName": t.string().optional(),
        }
    ).named(renames["CloudStorageFileIn"])
    types["CloudStorageFileOut"] = t.struct(
        {
            "bucketName": t.string().optional(),
            "size": t.string().optional(),
            "md5Hash": t.string().optional(),
            "objectName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudStorageFileOut"])
    types["HangoutsChatInfoIn"] = t.struct(
        {"roomId": t.array(t.string()).optional()}
    ).named(renames["HangoutsChatInfoIn"])
    types["HangoutsChatInfoOut"] = t.struct(
        {
            "roomId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HangoutsChatInfoOut"])
    types["OrgUnitInfoIn"] = t.struct({"orgUnitId": t.string().optional()}).named(
        renames["OrgUnitInfoIn"]
    )
    types["OrgUnitInfoOut"] = t.struct(
        {
            "orgUnitId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrgUnitInfoOut"])
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
    types["SitesUrlInfoIn"] = t.struct({"urls": t.array(t.string()).optional()}).named(
        renames["SitesUrlInfoIn"]
    )
    types["SitesUrlInfoOut"] = t.struct(
        {
            "urls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SitesUrlInfoOut"])
    types["DriveExportOptionsIn"] = t.struct(
        {"includeAccessInfo": t.boolean().optional()}
    ).named(renames["DriveExportOptionsIn"])
    types["DriveExportOptionsOut"] = t.struct(
        {
            "includeAccessInfo": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveExportOptionsOut"])
    types["ReopenMatterResponseIn"] = t.struct(
        {"matter": t.proxy(renames["MatterIn"]).optional()}
    ).named(renames["ReopenMatterResponseIn"])
    types["ReopenMatterResponseOut"] = t.struct(
        {
            "matter": t.proxy(renames["MatterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReopenMatterResponseOut"])
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
    types["RemoveMatterPermissionsRequestIn"] = t.struct(
        {"accountId": t.string().optional()}
    ).named(renames["RemoveMatterPermissionsRequestIn"])
    types["RemoveMatterPermissionsRequestOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveMatterPermissionsRequestOut"])
    types["GroupsCountResultIn"] = t.struct(
        {
            "accountCounts": t.array(t.proxy(renames["AccountCountIn"])).optional(),
            "accountCountErrors": t.array(
                t.proxy(renames["AccountCountErrorIn"])
            ).optional(),
            "nonQueryableAccounts": t.array(t.string()).optional(),
            "queriedAccountsCount": t.string().optional(),
            "matchingAccountsCount": t.string().optional(),
        }
    ).named(renames["GroupsCountResultIn"])
    types["GroupsCountResultOut"] = t.struct(
        {
            "accountCounts": t.array(t.proxy(renames["AccountCountOut"])).optional(),
            "accountCountErrors": t.array(
                t.proxy(renames["AccountCountErrorOut"])
            ).optional(),
            "nonQueryableAccounts": t.array(t.string()).optional(),
            "queriedAccountsCount": t.string().optional(),
            "matchingAccountsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupsCountResultOut"])
    types["HeldMailQueryIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "terms": t.string().optional(),
        }
    ).named(renames["HeldMailQueryIn"])
    types["HeldMailQueryOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "terms": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldMailQueryOut"])
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
    types["ExportOptionsIn"] = t.struct(
        {
            "driveOptions": t.proxy(renames["DriveExportOptionsIn"]).optional(),
            "hangoutsChatOptions": t.proxy(
                renames["HangoutsChatExportOptionsIn"]
            ).optional(),
            "region": t.string().optional(),
            "voiceOptions": t.proxy(renames["VoiceExportOptionsIn"]).optional(),
            "mailOptions": t.proxy(renames["MailExportOptionsIn"]).optional(),
            "groupsOptions": t.proxy(renames["GroupsExportOptionsIn"]).optional(),
        }
    ).named(renames["ExportOptionsIn"])
    types["ExportOptionsOut"] = t.struct(
        {
            "driveOptions": t.proxy(renames["DriveExportOptionsOut"]).optional(),
            "hangoutsChatOptions": t.proxy(
                renames["HangoutsChatExportOptionsOut"]
            ).optional(),
            "region": t.string().optional(),
            "voiceOptions": t.proxy(renames["VoiceExportOptionsOut"]).optional(),
            "mailOptions": t.proxy(renames["MailExportOptionsOut"]).optional(),
            "groupsOptions": t.proxy(renames["GroupsExportOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportOptionsOut"])
    types["UndeleteMatterRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteMatterRequestIn"]
    )
    types["UndeleteMatterRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteMatterRequestOut"])
    types["GroupsExportOptionsIn"] = t.struct(
        {"exportFormat": t.string().optional()}
    ).named(renames["GroupsExportOptionsIn"])
    types["GroupsExportOptionsOut"] = t.struct(
        {
            "exportFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupsExportOptionsOut"])
    types["HeldHangoutsChatQueryIn"] = t.struct(
        {"includeRooms": t.boolean().optional()}
    ).named(renames["HeldHangoutsChatQueryIn"])
    types["HeldHangoutsChatQueryOut"] = t.struct(
        {
            "includeRooms": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldHangoutsChatQueryOut"])
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
    types["ExportStatsIn"] = t.struct(
        {
            "sizeInBytes": t.string().optional(),
            "exportedArtifactCount": t.string().optional(),
            "totalArtifactCount": t.string().optional(),
        }
    ).named(renames["ExportStatsIn"])
    types["ExportStatsOut"] = t.struct(
        {
            "sizeInBytes": t.string().optional(),
            "exportedArtifactCount": t.string().optional(),
            "totalArtifactCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportStatsOut"])
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
    types["QueryIn"] = t.struct(
        {
            "searchMethod": t.string().optional(),
            "dataScope": t.string().optional(),
            "teamDriveInfo": t.proxy(renames["TeamDriveInfoIn"]),
            "orgUnitInfo": t.proxy(renames["OrgUnitInfoIn"]),
            "driveOptions": t.proxy(renames["DriveOptionsIn"]).optional(),
            "hangoutsChatOptions": t.proxy(renames["HangoutsChatOptionsIn"]).optional(),
            "mailOptions": t.proxy(renames["MailOptionsIn"]).optional(),
            "corpus": t.string().optional(),
            "sharedDriveInfo": t.proxy(renames["SharedDriveInfoIn"]),
            "sitesUrlInfo": t.proxy(renames["SitesUrlInfoIn"]),
            "startTime": t.string().optional(),
            "hangoutsChatInfo": t.proxy(renames["HangoutsChatInfoIn"]),
            "method": t.string().optional(),
            "timeZone": t.string().optional(),
            "voiceOptions": t.proxy(renames["VoiceOptionsIn"]).optional(),
            "endTime": t.string().optional(),
            "accountInfo": t.proxy(renames["AccountInfoIn"]),
            "terms": t.string().optional(),
        }
    ).named(renames["QueryIn"])
    types["QueryOut"] = t.struct(
        {
            "searchMethod": t.string().optional(),
            "dataScope": t.string().optional(),
            "teamDriveInfo": t.proxy(renames["TeamDriveInfoOut"]),
            "orgUnitInfo": t.proxy(renames["OrgUnitInfoOut"]),
            "driveOptions": t.proxy(renames["DriveOptionsOut"]).optional(),
            "hangoutsChatOptions": t.proxy(
                renames["HangoutsChatOptionsOut"]
            ).optional(),
            "mailOptions": t.proxy(renames["MailOptionsOut"]).optional(),
            "corpus": t.string().optional(),
            "sharedDriveInfo": t.proxy(renames["SharedDriveInfoOut"]),
            "sitesUrlInfo": t.proxy(renames["SitesUrlInfoOut"]),
            "startTime": t.string().optional(),
            "hangoutsChatInfo": t.proxy(renames["HangoutsChatInfoOut"]),
            "method": t.string().optional(),
            "timeZone": t.string().optional(),
            "voiceOptions": t.proxy(renames["VoiceOptionsOut"]).optional(),
            "endTime": t.string().optional(),
            "accountInfo": t.proxy(renames["AccountInfoOut"]),
            "terms": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryOut"])
    types["ListHeldAccountsResponseIn"] = t.struct(
        {"accounts": t.array(t.proxy(renames["HeldAccountIn"])).optional()}
    ).named(renames["ListHeldAccountsResponseIn"])
    types["ListHeldAccountsResponseOut"] = t.struct(
        {
            "accounts": t.array(t.proxy(renames["HeldAccountOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListHeldAccountsResponseOut"])
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
    types["CorpusQueryIn"] = t.struct(
        {
            "groupsQuery": t.proxy(renames["HeldGroupsQueryIn"]).optional(),
            "voiceQuery": t.proxy(renames["HeldVoiceQueryIn"]).optional(),
            "hangoutsChatQuery": t.proxy(renames["HeldHangoutsChatQueryIn"]).optional(),
            "driveQuery": t.proxy(renames["HeldDriveQueryIn"]).optional(),
            "mailQuery": t.proxy(renames["HeldMailQueryIn"]).optional(),
        }
    ).named(renames["CorpusQueryIn"])
    types["CorpusQueryOut"] = t.struct(
        {
            "groupsQuery": t.proxy(renames["HeldGroupsQueryOut"]).optional(),
            "voiceQuery": t.proxy(renames["HeldVoiceQueryOut"]).optional(),
            "hangoutsChatQuery": t.proxy(
                renames["HeldHangoutsChatQueryOut"]
            ).optional(),
            "driveQuery": t.proxy(renames["HeldDriveQueryOut"]).optional(),
            "mailQuery": t.proxy(renames["HeldMailQueryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CorpusQueryOut"])
    types["MatterIn"] = t.struct(
        {
            "matterPermissions": t.array(
                t.proxy(renames["MatterPermissionIn"])
            ).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "matterId": t.string().optional(),
        }
    ).named(renames["MatterIn"])
    types["MatterOut"] = t.struct(
        {
            "matterPermissions": t.array(
                t.proxy(renames["MatterPermissionOut"])
            ).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "matterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatterOut"])
    types["HoldIn"] = t.struct(
        {
            "orgUnit": t.proxy(renames["HeldOrgUnitIn"]).optional(),
            "updateTime": t.string().optional(),
            "holdId": t.string().optional(),
            "name": t.string().optional(),
            "accounts": t.array(t.proxy(renames["HeldAccountIn"])).optional(),
            "query": t.proxy(renames["CorpusQueryIn"]).optional(),
            "corpus": t.string().optional(),
        }
    ).named(renames["HoldIn"])
    types["HoldOut"] = t.struct(
        {
            "orgUnit": t.proxy(renames["HeldOrgUnitOut"]).optional(),
            "updateTime": t.string().optional(),
            "holdId": t.string().optional(),
            "name": t.string().optional(),
            "accounts": t.array(t.proxy(renames["HeldAccountOut"])).optional(),
            "query": t.proxy(renames["CorpusQueryOut"]).optional(),
            "corpus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HoldOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["CountArtifactsMetadataIn"] = t.struct(
        {
            "matterId": t.string().optional(),
            "endTime": t.string().optional(),
            "query": t.proxy(renames["QueryIn"]).optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["CountArtifactsMetadataIn"])
    types["CountArtifactsMetadataOut"] = t.struct(
        {
            "matterId": t.string().optional(),
            "endTime": t.string().optional(),
            "query": t.proxy(renames["QueryOut"]).optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountArtifactsMetadataOut"])
    types["CloudStorageSinkIn"] = t.struct(
        {"files": t.array(t.proxy(renames["CloudStorageFileIn"])).optional()}
    ).named(renames["CloudStorageSinkIn"])
    types["CloudStorageSinkOut"] = t.struct(
        {
            "files": t.array(t.proxy(renames["CloudStorageFileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudStorageSinkOut"])
    types["SharedDriveInfoIn"] = t.struct(
        {"sharedDriveIds": t.array(t.string()).optional()}
    ).named(renames["SharedDriveInfoIn"])
    types["SharedDriveInfoOut"] = t.struct(
        {
            "sharedDriveIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SharedDriveInfoOut"])
    types["ReopenMatterRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReopenMatterRequestIn"]
    )
    types["ReopenMatterRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReopenMatterRequestOut"])
    types["HeldVoiceQueryIn"] = t.struct(
        {"coveredData": t.array(t.string()).optional()}
    ).named(renames["HeldVoiceQueryIn"])
    types["HeldVoiceQueryOut"] = t.struct(
        {
            "coveredData": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldVoiceQueryOut"])
    types["RemoveHeldAccountsRequestIn"] = t.struct(
        {"accountIds": t.array(t.string()).optional()}
    ).named(renames["RemoveHeldAccountsRequestIn"])
    types["RemoveHeldAccountsRequestOut"] = t.struct(
        {
            "accountIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveHeldAccountsRequestOut"])
    types["MailCountResultIn"] = t.struct(
        {
            "accountCounts": t.array(t.proxy(renames["AccountCountIn"])).optional(),
            "accountCountErrors": t.array(
                t.proxy(renames["AccountCountErrorIn"])
            ).optional(),
            "nonQueryableAccounts": t.array(t.string()).optional(),
            "queriedAccountsCount": t.string().optional(),
            "matchingAccountsCount": t.string().optional(),
        }
    ).named(renames["MailCountResultIn"])
    types["MailCountResultOut"] = t.struct(
        {
            "accountCounts": t.array(t.proxy(renames["AccountCountOut"])).optional(),
            "accountCountErrors": t.array(
                t.proxy(renames["AccountCountErrorOut"])
            ).optional(),
            "nonQueryableAccounts": t.array(t.string()).optional(),
            "queriedAccountsCount": t.string().optional(),
            "matchingAccountsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MailCountResultOut"])
    types["VoiceExportOptionsIn"] = t.struct(
        {"exportFormat": t.string().optional()}
    ).named(renames["VoiceExportOptionsIn"])
    types["VoiceExportOptionsOut"] = t.struct(
        {
            "exportFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceExportOptionsOut"])
    types["AddMatterPermissionsRequestIn"] = t.struct(
        {
            "matterPermission": t.proxy(renames["MatterPermissionIn"]).optional(),
            "sendEmails": t.boolean().optional(),
            "ccMe": t.boolean().optional(),
        }
    ).named(renames["AddMatterPermissionsRequestIn"])
    types["AddMatterPermissionsRequestOut"] = t.struct(
        {
            "matterPermission": t.proxy(renames["MatterPermissionOut"]).optional(),
            "sendEmails": t.boolean().optional(),
            "ccMe": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddMatterPermissionsRequestOut"])
    types["CloseMatterRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloseMatterRequestIn"]
    )
    types["CloseMatterRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloseMatterRequestOut"])
    types["ListSavedQueriesResponseIn"] = t.struct(
        {
            "savedQueries": t.array(t.proxy(renames["SavedQueryIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSavedQueriesResponseIn"])
    types["ListSavedQueriesResponseOut"] = t.struct(
        {
            "savedQueries": t.array(t.proxy(renames["SavedQueryOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSavedQueriesResponseOut"])
    types["DriveOptionsIn"] = t.struct(
        {
            "clientSideEncryptedOption": t.string().optional(),
            "versionDate": t.string().optional(),
            "includeTeamDrives": t.boolean().optional(),
            "includeSharedDrives": t.boolean().optional(),
        }
    ).named(renames["DriveOptionsIn"])
    types["DriveOptionsOut"] = t.struct(
        {
            "clientSideEncryptedOption": t.string().optional(),
            "versionDate": t.string().optional(),
            "includeTeamDrives": t.boolean().optional(),
            "includeSharedDrives": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveOptionsOut"])
    types["ExportIn"] = t.struct(
        {
            "stats": t.proxy(renames["ExportStatsIn"]).optional(),
            "matterId": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "cloudStorageSink": t.proxy(renames["CloudStorageSinkIn"]).optional(),
            "requester": t.proxy(renames["UserInfoIn"]).optional(),
            "exportOptions": t.proxy(renames["ExportOptionsIn"]).optional(),
            "query": t.proxy(renames["QueryIn"]).optional(),
            "status": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["ExportIn"])
    types["ExportOut"] = t.struct(
        {
            "stats": t.proxy(renames["ExportStatsOut"]).optional(),
            "matterId": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "cloudStorageSink": t.proxy(renames["CloudStorageSinkOut"]).optional(),
            "requester": t.proxy(renames["UserInfoOut"]).optional(),
            "exportOptions": t.proxy(renames["ExportOptionsOut"]).optional(),
            "query": t.proxy(renames["QueryOut"]).optional(),
            "status": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["AccountInfoIn"] = t.struct({"emails": t.array(t.string()).optional()}).named(
        renames["AccountInfoIn"]
    )
    types["AccountInfoOut"] = t.struct(
        {
            "emails": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountInfoOut"])
    types["TeamDriveInfoIn"] = t.struct(
        {"teamDriveIds": t.array(t.string()).optional()}
    ).named(renames["TeamDriveInfoIn"])
    types["TeamDriveInfoOut"] = t.struct(
        {
            "teamDriveIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TeamDriveInfoOut"])
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
    types["SavedQueryIn"] = t.struct(
        {
            "query": t.proxy(renames["QueryIn"]).optional(),
            "savedQueryId": t.string().optional(),
            "displayName": t.string().optional(),
            "matterId": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["SavedQueryIn"])
    types["SavedQueryOut"] = t.struct(
        {
            "query": t.proxy(renames["QueryOut"]).optional(),
            "savedQueryId": t.string().optional(),
            "displayName": t.string().optional(),
            "matterId": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SavedQueryOut"])
    types["MailExportOptionsIn"] = t.struct(
        {
            "showConfidentialModeContent": t.boolean().optional(),
            "useNewExport": t.boolean().optional(),
            "exportFormat": t.string().optional(),
        }
    ).named(renames["MailExportOptionsIn"])
    types["MailExportOptionsOut"] = t.struct(
        {
            "showConfidentialModeContent": t.boolean().optional(),
            "useNewExport": t.boolean().optional(),
            "exportFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MailExportOptionsOut"])
    types["HeldDriveQueryIn"] = t.struct(
        {
            "includeTeamDriveFiles": t.boolean().optional(),
            "includeSharedDriveFiles": t.boolean().optional(),
        }
    ).named(renames["HeldDriveQueryIn"])
    types["HeldDriveQueryOut"] = t.struct(
        {
            "includeTeamDriveFiles": t.boolean().optional(),
            "includeSharedDriveFiles": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldDriveQueryOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["RemoveHeldAccountsResponseIn"] = t.struct(
        {"statuses": t.array(t.proxy(renames["StatusIn"])).optional()}
    ).named(renames["RemoveHeldAccountsResponseIn"])
    types["RemoveHeldAccountsResponseOut"] = t.struct(
        {
            "statuses": t.array(t.proxy(renames["StatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveHeldAccountsResponseOut"])
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
    functions["mattersSavedQueriesGet"] = vault.get(
        "v1/matters/{matterId}/savedQueries",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "matterId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSavedQueriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersSavedQueriesCreate"] = vault.get(
        "v1/matters/{matterId}/savedQueries",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "matterId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSavedQueriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersSavedQueriesDelete"] = vault.get(
        "v1/matters/{matterId}/savedQueries",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "matterId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSavedQueriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersSavedQueriesList"] = vault.get(
        "v1/matters/{matterId}/savedQueries",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "matterId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSavedQueriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsRemoveHeldAccounts"] = vault.post(
        "v1/matters/{matterId}/holds/{holdId}:addHeldAccounts",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "emails": t.array(t.string()).optional(),
                "accountIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AddHeldAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsList"] = vault.post(
        "v1/matters/{matterId}/holds/{holdId}:addHeldAccounts",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "emails": t.array(t.string()).optional(),
                "accountIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AddHeldAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsDelete"] = vault.post(
        "v1/matters/{matterId}/holds/{holdId}:addHeldAccounts",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "emails": t.array(t.string()).optional(),
                "accountIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AddHeldAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsCreate"] = vault.post(
        "v1/matters/{matterId}/holds/{holdId}:addHeldAccounts",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "emails": t.array(t.string()).optional(),
                "accountIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AddHeldAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsUpdate"] = vault.post(
        "v1/matters/{matterId}/holds/{holdId}:addHeldAccounts",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "emails": t.array(t.string()).optional(),
                "accountIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AddHeldAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsGet"] = vault.post(
        "v1/matters/{matterId}/holds/{holdId}:addHeldAccounts",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "emails": t.array(t.string()).optional(),
                "accountIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AddHeldAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsAddHeldAccounts"] = vault.post(
        "v1/matters/{matterId}/holds/{holdId}:addHeldAccounts",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "emails": t.array(t.string()).optional(),
                "accountIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AddHeldAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsAccountsList"] = vault.delete(
        "v1/matters/{matterId}/holds/{holdId}/accounts/{accountId}",
        t.struct(
            {
                "matterId": t.string().optional(),
                "accountId": t.string().optional(),
                "holdId": t.string().optional(),
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
                "matterId": t.string().optional(),
                "accountId": t.string().optional(),
                "holdId": t.string().optional(),
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
                "matterId": t.string().optional(),
                "accountId": t.string().optional(),
                "holdId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersExportsCreate"] = vault.get(
        "v1/matters/{matterId}/exports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "matterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersExportsGet"] = vault.get(
        "v1/matters/{matterId}/exports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "matterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersExportsDelete"] = vault.get(
        "v1/matters/{matterId}/exports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "matterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersExportsList"] = vault.get(
        "v1/matters/{matterId}/exports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "matterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="vault", renames=renames, types=Box(types), functions=Box(functions)
    )
