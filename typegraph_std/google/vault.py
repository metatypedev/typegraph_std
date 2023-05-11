from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_vault() -> Import:
    vault = HTTPRuntime("https://vault.googleapis.com/")

    renames = {
        "ErrorResponse": "_vault_1_ErrorResponse",
        "HeldOrgUnitIn": "_vault_2_HeldOrgUnitIn",
        "HeldOrgUnitOut": "_vault_3_HeldOrgUnitOut",
        "CountArtifactsRequestIn": "_vault_4_CountArtifactsRequestIn",
        "CountArtifactsRequestOut": "_vault_5_CountArtifactsRequestOut",
        "CloseMatterResponseIn": "_vault_6_CloseMatterResponseIn",
        "CloseMatterResponseOut": "_vault_7_CloseMatterResponseOut",
        "DriveExportOptionsIn": "_vault_8_DriveExportOptionsIn",
        "DriveExportOptionsOut": "_vault_9_DriveExportOptionsOut",
        "QueryIn": "_vault_10_QueryIn",
        "QueryOut": "_vault_11_QueryOut",
        "CountArtifactsMetadataIn": "_vault_12_CountArtifactsMetadataIn",
        "CountArtifactsMetadataOut": "_vault_13_CountArtifactsMetadataOut",
        "HeldVoiceQueryIn": "_vault_14_HeldVoiceQueryIn",
        "HeldVoiceQueryOut": "_vault_15_HeldVoiceQueryOut",
        "AccountCountErrorIn": "_vault_16_AccountCountErrorIn",
        "AccountCountErrorOut": "_vault_17_AccountCountErrorOut",
        "AddHeldAccountResultIn": "_vault_18_AddHeldAccountResultIn",
        "AddHeldAccountResultOut": "_vault_19_AddHeldAccountResultOut",
        "RemoveMatterPermissionsRequestIn": "_vault_20_RemoveMatterPermissionsRequestIn",
        "RemoveMatterPermissionsRequestOut": "_vault_21_RemoveMatterPermissionsRequestOut",
        "ListExportsResponseIn": "_vault_22_ListExportsResponseIn",
        "ListExportsResponseOut": "_vault_23_ListExportsResponseOut",
        "ExportIn": "_vault_24_ExportIn",
        "ExportOut": "_vault_25_ExportOut",
        "ListHoldsResponseIn": "_vault_26_ListHoldsResponseIn",
        "ListHoldsResponseOut": "_vault_27_ListHoldsResponseOut",
        "GroupsExportOptionsIn": "_vault_28_GroupsExportOptionsIn",
        "GroupsExportOptionsOut": "_vault_29_GroupsExportOptionsOut",
        "ListSavedQueriesResponseIn": "_vault_30_ListSavedQueriesResponseIn",
        "ListSavedQueriesResponseOut": "_vault_31_ListSavedQueriesResponseOut",
        "HangoutsChatExportOptionsIn": "_vault_32_HangoutsChatExportOptionsIn",
        "HangoutsChatExportOptionsOut": "_vault_33_HangoutsChatExportOptionsOut",
        "TeamDriveInfoIn": "_vault_34_TeamDriveInfoIn",
        "TeamDriveInfoOut": "_vault_35_TeamDriveInfoOut",
        "CancelOperationRequestIn": "_vault_36_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_vault_37_CancelOperationRequestOut",
        "ReopenMatterRequestIn": "_vault_38_ReopenMatterRequestIn",
        "ReopenMatterRequestOut": "_vault_39_ReopenMatterRequestOut",
        "GroupsCountResultIn": "_vault_40_GroupsCountResultIn",
        "GroupsCountResultOut": "_vault_41_GroupsCountResultOut",
        "HeldAccountIn": "_vault_42_HeldAccountIn",
        "HeldAccountOut": "_vault_43_HeldAccountOut",
        "ListHeldAccountsResponseIn": "_vault_44_ListHeldAccountsResponseIn",
        "ListHeldAccountsResponseOut": "_vault_45_ListHeldAccountsResponseOut",
        "UndeleteMatterRequestIn": "_vault_46_UndeleteMatterRequestIn",
        "UndeleteMatterRequestOut": "_vault_47_UndeleteMatterRequestOut",
        "RemoveHeldAccountsRequestIn": "_vault_48_RemoveHeldAccountsRequestIn",
        "RemoveHeldAccountsRequestOut": "_vault_49_RemoveHeldAccountsRequestOut",
        "HangoutsChatOptionsIn": "_vault_50_HangoutsChatOptionsIn",
        "HangoutsChatOptionsOut": "_vault_51_HangoutsChatOptionsOut",
        "HeldGroupsQueryIn": "_vault_52_HeldGroupsQueryIn",
        "HeldGroupsQueryOut": "_vault_53_HeldGroupsQueryOut",
        "AddHeldAccountsRequestIn": "_vault_54_AddHeldAccountsRequestIn",
        "AddHeldAccountsRequestOut": "_vault_55_AddHeldAccountsRequestOut",
        "VoiceOptionsIn": "_vault_56_VoiceOptionsIn",
        "VoiceOptionsOut": "_vault_57_VoiceOptionsOut",
        "HoldIn": "_vault_58_HoldIn",
        "HoldOut": "_vault_59_HoldOut",
        "MatterPermissionIn": "_vault_60_MatterPermissionIn",
        "MatterPermissionOut": "_vault_61_MatterPermissionOut",
        "UserInfoIn": "_vault_62_UserInfoIn",
        "UserInfoOut": "_vault_63_UserInfoOut",
        "HeldHangoutsChatQueryIn": "_vault_64_HeldHangoutsChatQueryIn",
        "HeldHangoutsChatQueryOut": "_vault_65_HeldHangoutsChatQueryOut",
        "ListMattersResponseIn": "_vault_66_ListMattersResponseIn",
        "ListMattersResponseOut": "_vault_67_ListMattersResponseOut",
        "AccountCountIn": "_vault_68_AccountCountIn",
        "AccountCountOut": "_vault_69_AccountCountOut",
        "CloseMatterRequestIn": "_vault_70_CloseMatterRequestIn",
        "CloseMatterRequestOut": "_vault_71_CloseMatterRequestOut",
        "StatusIn": "_vault_72_StatusIn",
        "StatusOut": "_vault_73_StatusOut",
        "CloudStorageSinkIn": "_vault_74_CloudStorageSinkIn",
        "CloudStorageSinkOut": "_vault_75_CloudStorageSinkOut",
        "MailExportOptionsIn": "_vault_76_MailExportOptionsIn",
        "MailExportOptionsOut": "_vault_77_MailExportOptionsOut",
        "HangoutsChatInfoIn": "_vault_78_HangoutsChatInfoIn",
        "HangoutsChatInfoOut": "_vault_79_HangoutsChatInfoOut",
        "SharedDriveInfoIn": "_vault_80_SharedDriveInfoIn",
        "SharedDriveInfoOut": "_vault_81_SharedDriveInfoOut",
        "CorpusQueryIn": "_vault_82_CorpusQueryIn",
        "CorpusQueryOut": "_vault_83_CorpusQueryOut",
        "MatterIn": "_vault_84_MatterIn",
        "MatterOut": "_vault_85_MatterOut",
        "MailOptionsIn": "_vault_86_MailOptionsIn",
        "MailOptionsOut": "_vault_87_MailOptionsOut",
        "OrgUnitInfoIn": "_vault_88_OrgUnitInfoIn",
        "OrgUnitInfoOut": "_vault_89_OrgUnitInfoOut",
        "CountArtifactsResponseIn": "_vault_90_CountArtifactsResponseIn",
        "CountArtifactsResponseOut": "_vault_91_CountArtifactsResponseOut",
        "HeldMailQueryIn": "_vault_92_HeldMailQueryIn",
        "HeldMailQueryOut": "_vault_93_HeldMailQueryOut",
        "ListOperationsResponseIn": "_vault_94_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_vault_95_ListOperationsResponseOut",
        "AccountInfoIn": "_vault_96_AccountInfoIn",
        "AccountInfoOut": "_vault_97_AccountInfoOut",
        "EmptyIn": "_vault_98_EmptyIn",
        "EmptyOut": "_vault_99_EmptyOut",
        "ReopenMatterResponseIn": "_vault_100_ReopenMatterResponseIn",
        "ReopenMatterResponseOut": "_vault_101_ReopenMatterResponseOut",
        "OperationIn": "_vault_102_OperationIn",
        "OperationOut": "_vault_103_OperationOut",
        "AddMatterPermissionsRequestIn": "_vault_104_AddMatterPermissionsRequestIn",
        "AddMatterPermissionsRequestOut": "_vault_105_AddMatterPermissionsRequestOut",
        "RemoveHeldAccountsResponseIn": "_vault_106_RemoveHeldAccountsResponseIn",
        "RemoveHeldAccountsResponseOut": "_vault_107_RemoveHeldAccountsResponseOut",
        "SitesUrlInfoIn": "_vault_108_SitesUrlInfoIn",
        "SitesUrlInfoOut": "_vault_109_SitesUrlInfoOut",
        "SavedQueryIn": "_vault_110_SavedQueryIn",
        "SavedQueryOut": "_vault_111_SavedQueryOut",
        "CloudStorageFileIn": "_vault_112_CloudStorageFileIn",
        "CloudStorageFileOut": "_vault_113_CloudStorageFileOut",
        "ExportStatsIn": "_vault_114_ExportStatsIn",
        "ExportStatsOut": "_vault_115_ExportStatsOut",
        "HeldDriveQueryIn": "_vault_116_HeldDriveQueryIn",
        "HeldDriveQueryOut": "_vault_117_HeldDriveQueryOut",
        "DriveOptionsIn": "_vault_118_DriveOptionsIn",
        "DriveOptionsOut": "_vault_119_DriveOptionsOut",
        "VoiceExportOptionsIn": "_vault_120_VoiceExportOptionsIn",
        "VoiceExportOptionsOut": "_vault_121_VoiceExportOptionsOut",
        "MailCountResultIn": "_vault_122_MailCountResultIn",
        "MailCountResultOut": "_vault_123_MailCountResultOut",
        "AddHeldAccountsResponseIn": "_vault_124_AddHeldAccountsResponseIn",
        "AddHeldAccountsResponseOut": "_vault_125_AddHeldAccountsResponseOut",
        "ExportOptionsIn": "_vault_126_ExportOptionsIn",
        "ExportOptionsOut": "_vault_127_ExportOptionsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["CloseMatterResponseIn"] = t.struct(
        {"matter": t.proxy(renames["MatterIn"]).optional()}
    ).named(renames["CloseMatterResponseIn"])
    types["CloseMatterResponseOut"] = t.struct(
        {
            "matter": t.proxy(renames["MatterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloseMatterResponseOut"])
    types["DriveExportOptionsIn"] = t.struct(
        {"includeAccessInfo": t.boolean().optional()}
    ).named(renames["DriveExportOptionsIn"])
    types["DriveExportOptionsOut"] = t.struct(
        {
            "includeAccessInfo": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveExportOptionsOut"])
    types["QueryIn"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "dataScope": t.string().optional(),
            "orgUnitInfo": t.proxy(renames["OrgUnitInfoIn"]),
            "teamDriveInfo": t.proxy(renames["TeamDriveInfoIn"]),
            "searchMethod": t.string().optional(),
            "hangoutsChatInfo": t.proxy(renames["HangoutsChatInfoIn"]),
            "accountInfo": t.proxy(renames["AccountInfoIn"]),
            "method": t.string().optional(),
            "corpus": t.string().optional(),
            "sitesUrlInfo": t.proxy(renames["SitesUrlInfoIn"]),
            "hangoutsChatOptions": t.proxy(renames["HangoutsChatOptionsIn"]).optional(),
            "startTime": t.string().optional(),
            "terms": t.string().optional(),
            "driveOptions": t.proxy(renames["DriveOptionsIn"]).optional(),
            "endTime": t.string().optional(),
            "sharedDriveInfo": t.proxy(renames["SharedDriveInfoIn"]),
            "mailOptions": t.proxy(renames["MailOptionsIn"]).optional(),
            "voiceOptions": t.proxy(renames["VoiceOptionsIn"]).optional(),
        }
    ).named(renames["QueryIn"])
    types["QueryOut"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "dataScope": t.string().optional(),
            "orgUnitInfo": t.proxy(renames["OrgUnitInfoOut"]),
            "teamDriveInfo": t.proxy(renames["TeamDriveInfoOut"]),
            "searchMethod": t.string().optional(),
            "hangoutsChatInfo": t.proxy(renames["HangoutsChatInfoOut"]),
            "accountInfo": t.proxy(renames["AccountInfoOut"]),
            "method": t.string().optional(),
            "corpus": t.string().optional(),
            "sitesUrlInfo": t.proxy(renames["SitesUrlInfoOut"]),
            "hangoutsChatOptions": t.proxy(
                renames["HangoutsChatOptionsOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "terms": t.string().optional(),
            "driveOptions": t.proxy(renames["DriveOptionsOut"]).optional(),
            "endTime": t.string().optional(),
            "sharedDriveInfo": t.proxy(renames["SharedDriveInfoOut"]),
            "mailOptions": t.proxy(renames["MailOptionsOut"]).optional(),
            "voiceOptions": t.proxy(renames["VoiceOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryOut"])
    types["CountArtifactsMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "matterId": t.string().optional(),
            "query": t.proxy(renames["QueryIn"]).optional(),
        }
    ).named(renames["CountArtifactsMetadataIn"])
    types["CountArtifactsMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "matterId": t.string().optional(),
            "query": t.proxy(renames["QueryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountArtifactsMetadataOut"])
    types["HeldVoiceQueryIn"] = t.struct(
        {"coveredData": t.array(t.string()).optional()}
    ).named(renames["HeldVoiceQueryIn"])
    types["HeldVoiceQueryOut"] = t.struct(
        {
            "coveredData": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldVoiceQueryOut"])
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
    types["RemoveMatterPermissionsRequestIn"] = t.struct(
        {"accountId": t.string().optional()}
    ).named(renames["RemoveMatterPermissionsRequestIn"])
    types["RemoveMatterPermissionsRequestOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveMatterPermissionsRequestOut"])
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
    types["ExportIn"] = t.struct(
        {
            "name": t.string().optional(),
            "exportOptions": t.proxy(renames["ExportOptionsIn"]).optional(),
            "query": t.proxy(renames["QueryIn"]).optional(),
            "stats": t.proxy(renames["ExportStatsIn"]).optional(),
            "matterId": t.string().optional(),
            "status": t.string().optional(),
            "id": t.string().optional(),
            "requester": t.proxy(renames["UserInfoIn"]).optional(),
            "cloudStorageSink": t.proxy(renames["CloudStorageSinkIn"]).optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["ExportIn"])
    types["ExportOut"] = t.struct(
        {
            "name": t.string().optional(),
            "exportOptions": t.proxy(renames["ExportOptionsOut"]).optional(),
            "query": t.proxy(renames["QueryOut"]).optional(),
            "stats": t.proxy(renames["ExportStatsOut"]).optional(),
            "matterId": t.string().optional(),
            "status": t.string().optional(),
            "id": t.string().optional(),
            "requester": t.proxy(renames["UserInfoOut"]).optional(),
            "cloudStorageSink": t.proxy(renames["CloudStorageSinkOut"]).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportOut"])
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
    types["GroupsExportOptionsIn"] = t.struct(
        {"exportFormat": t.string().optional()}
    ).named(renames["GroupsExportOptionsIn"])
    types["GroupsExportOptionsOut"] = t.struct(
        {
            "exportFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupsExportOptionsOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ReopenMatterRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReopenMatterRequestIn"]
    )
    types["ReopenMatterRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReopenMatterRequestOut"])
    types["GroupsCountResultIn"] = t.struct(
        {
            "queriedAccountsCount": t.string().optional(),
            "matchingAccountsCount": t.string().optional(),
            "accountCounts": t.array(t.proxy(renames["AccountCountIn"])).optional(),
            "accountCountErrors": t.array(
                t.proxy(renames["AccountCountErrorIn"])
            ).optional(),
            "nonQueryableAccounts": t.array(t.string()).optional(),
        }
    ).named(renames["GroupsCountResultIn"])
    types["GroupsCountResultOut"] = t.struct(
        {
            "queriedAccountsCount": t.string().optional(),
            "matchingAccountsCount": t.string().optional(),
            "accountCounts": t.array(t.proxy(renames["AccountCountOut"])).optional(),
            "accountCountErrors": t.array(
                t.proxy(renames["AccountCountErrorOut"])
            ).optional(),
            "nonQueryableAccounts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupsCountResultOut"])
    types["HeldAccountIn"] = t.struct(
        {
            "firstName": t.string().optional(),
            "email": t.string().optional(),
            "lastName": t.string().optional(),
            "accountId": t.string().optional(),
            "holdTime": t.string().optional(),
        }
    ).named(renames["HeldAccountIn"])
    types["HeldAccountOut"] = t.struct(
        {
            "firstName": t.string().optional(),
            "email": t.string().optional(),
            "lastName": t.string().optional(),
            "accountId": t.string().optional(),
            "holdTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldAccountOut"])
    types["ListHeldAccountsResponseIn"] = t.struct(
        {"accounts": t.array(t.proxy(renames["HeldAccountIn"])).optional()}
    ).named(renames["ListHeldAccountsResponseIn"])
    types["ListHeldAccountsResponseOut"] = t.struct(
        {
            "accounts": t.array(t.proxy(renames["HeldAccountOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListHeldAccountsResponseOut"])
    types["UndeleteMatterRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteMatterRequestIn"]
    )
    types["UndeleteMatterRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteMatterRequestOut"])
    types["RemoveHeldAccountsRequestIn"] = t.struct(
        {"accountIds": t.array(t.string()).optional()}
    ).named(renames["RemoveHeldAccountsRequestIn"])
    types["RemoveHeldAccountsRequestOut"] = t.struct(
        {
            "accountIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveHeldAccountsRequestOut"])
    types["HangoutsChatOptionsIn"] = t.struct(
        {"includeRooms": t.boolean().optional()}
    ).named(renames["HangoutsChatOptionsIn"])
    types["HangoutsChatOptionsOut"] = t.struct(
        {
            "includeRooms": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HangoutsChatOptionsOut"])
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
    types["VoiceOptionsIn"] = t.struct(
        {"coveredData": t.array(t.string()).optional()}
    ).named(renames["VoiceOptionsIn"])
    types["VoiceOptionsOut"] = t.struct(
        {
            "coveredData": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceOptionsOut"])
    types["HoldIn"] = t.struct(
        {
            "holdId": t.string().optional(),
            "accounts": t.array(t.proxy(renames["HeldAccountIn"])).optional(),
            "updateTime": t.string().optional(),
            "query": t.proxy(renames["CorpusQueryIn"]).optional(),
            "name": t.string().optional(),
            "corpus": t.string().optional(),
            "orgUnit": t.proxy(renames["HeldOrgUnitIn"]).optional(),
        }
    ).named(renames["HoldIn"])
    types["HoldOut"] = t.struct(
        {
            "holdId": t.string().optional(),
            "accounts": t.array(t.proxy(renames["HeldAccountOut"])).optional(),
            "updateTime": t.string().optional(),
            "query": t.proxy(renames["CorpusQueryOut"]).optional(),
            "name": t.string().optional(),
            "corpus": t.string().optional(),
            "orgUnit": t.proxy(renames["HeldOrgUnitOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HoldOut"])
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
    types["CloseMatterRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloseMatterRequestIn"]
    )
    types["CloseMatterRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloseMatterRequestOut"])
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
    types["CloudStorageSinkIn"] = t.struct(
        {"files": t.array(t.proxy(renames["CloudStorageFileIn"])).optional()}
    ).named(renames["CloudStorageSinkIn"])
    types["CloudStorageSinkOut"] = t.struct(
        {
            "files": t.array(t.proxy(renames["CloudStorageFileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudStorageSinkOut"])
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
    types["HangoutsChatInfoIn"] = t.struct(
        {"roomId": t.array(t.string()).optional()}
    ).named(renames["HangoutsChatInfoIn"])
    types["HangoutsChatInfoOut"] = t.struct(
        {
            "roomId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HangoutsChatInfoOut"])
    types["SharedDriveInfoIn"] = t.struct(
        {"sharedDriveIds": t.array(t.string()).optional()}
    ).named(renames["SharedDriveInfoIn"])
    types["SharedDriveInfoOut"] = t.struct(
        {
            "sharedDriveIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SharedDriveInfoOut"])
    types["CorpusQueryIn"] = t.struct(
        {
            "mailQuery": t.proxy(renames["HeldMailQueryIn"]).optional(),
            "hangoutsChatQuery": t.proxy(renames["HeldHangoutsChatQueryIn"]).optional(),
            "voiceQuery": t.proxy(renames["HeldVoiceQueryIn"]).optional(),
            "groupsQuery": t.proxy(renames["HeldGroupsQueryIn"]).optional(),
            "driveQuery": t.proxy(renames["HeldDriveQueryIn"]).optional(),
        }
    ).named(renames["CorpusQueryIn"])
    types["CorpusQueryOut"] = t.struct(
        {
            "mailQuery": t.proxy(renames["HeldMailQueryOut"]).optional(),
            "hangoutsChatQuery": t.proxy(
                renames["HeldHangoutsChatQueryOut"]
            ).optional(),
            "voiceQuery": t.proxy(renames["HeldVoiceQueryOut"]).optional(),
            "groupsQuery": t.proxy(renames["HeldGroupsQueryOut"]).optional(),
            "driveQuery": t.proxy(renames["HeldDriveQueryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CorpusQueryOut"])
    types["MatterIn"] = t.struct(
        {
            "matterPermissions": t.array(
                t.proxy(renames["MatterPermissionIn"])
            ).optional(),
            "description": t.string().optional(),
            "matterId": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["MatterIn"])
    types["MatterOut"] = t.struct(
        {
            "matterPermissions": t.array(
                t.proxy(renames["MatterPermissionOut"])
            ).optional(),
            "description": t.string().optional(),
            "matterId": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatterOut"])
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
    types["OrgUnitInfoIn"] = t.struct({"orgUnitId": t.string().optional()}).named(
        renames["OrgUnitInfoIn"]
    )
    types["OrgUnitInfoOut"] = t.struct(
        {
            "orgUnitId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrgUnitInfoOut"])
    types["CountArtifactsResponseIn"] = t.struct(
        {
            "mailCountResult": t.proxy(renames["MailCountResultIn"]).optional(),
            "totalCount": t.string().optional(),
            "groupsCountResult": t.proxy(renames["GroupsCountResultIn"]).optional(),
        }
    ).named(renames["CountArtifactsResponseIn"])
    types["CountArtifactsResponseOut"] = t.struct(
        {
            "mailCountResult": t.proxy(renames["MailCountResultOut"]).optional(),
            "totalCount": t.string().optional(),
            "groupsCountResult": t.proxy(renames["GroupsCountResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountArtifactsResponseOut"])
    types["HeldMailQueryIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "terms": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["HeldMailQueryIn"])
    types["HeldMailQueryOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "terms": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeldMailQueryOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ReopenMatterResponseIn"] = t.struct(
        {"matter": t.proxy(renames["MatterIn"]).optional()}
    ).named(renames["ReopenMatterResponseIn"])
    types["ReopenMatterResponseOut"] = t.struct(
        {
            "matter": t.proxy(renames["MatterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReopenMatterResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["AddMatterPermissionsRequestIn"] = t.struct(
        {
            "sendEmails": t.boolean().optional(),
            "ccMe": t.boolean().optional(),
            "matterPermission": t.proxy(renames["MatterPermissionIn"]).optional(),
        }
    ).named(renames["AddMatterPermissionsRequestIn"])
    types["AddMatterPermissionsRequestOut"] = t.struct(
        {
            "sendEmails": t.boolean().optional(),
            "ccMe": t.boolean().optional(),
            "matterPermission": t.proxy(renames["MatterPermissionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddMatterPermissionsRequestOut"])
    types["RemoveHeldAccountsResponseIn"] = t.struct(
        {"statuses": t.array(t.proxy(renames["StatusIn"])).optional()}
    ).named(renames["RemoveHeldAccountsResponseIn"])
    types["RemoveHeldAccountsResponseOut"] = t.struct(
        {
            "statuses": t.array(t.proxy(renames["StatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveHeldAccountsResponseOut"])
    types["SitesUrlInfoIn"] = t.struct({"urls": t.array(t.string()).optional()}).named(
        renames["SitesUrlInfoIn"]
    )
    types["SitesUrlInfoOut"] = t.struct(
        {
            "urls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SitesUrlInfoOut"])
    types["SavedQueryIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "query": t.proxy(renames["QueryIn"]).optional(),
            "matterId": t.string().optional(),
            "savedQueryId": t.string().optional(),
        }
    ).named(renames["SavedQueryIn"])
    types["SavedQueryOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "query": t.proxy(renames["QueryOut"]).optional(),
            "matterId": t.string().optional(),
            "savedQueryId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SavedQueryOut"])
    types["CloudStorageFileIn"] = t.struct(
        {
            "md5Hash": t.string().optional(),
            "bucketName": t.string().optional(),
            "size": t.string().optional(),
            "objectName": t.string().optional(),
        }
    ).named(renames["CloudStorageFileIn"])
    types["CloudStorageFileOut"] = t.struct(
        {
            "md5Hash": t.string().optional(),
            "bucketName": t.string().optional(),
            "size": t.string().optional(),
            "objectName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudStorageFileOut"])
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
    types["VoiceExportOptionsIn"] = t.struct(
        {"exportFormat": t.string().optional()}
    ).named(renames["VoiceExportOptionsIn"])
    types["VoiceExportOptionsOut"] = t.struct(
        {
            "exportFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceExportOptionsOut"])
    types["MailCountResultIn"] = t.struct(
        {
            "matchingAccountsCount": t.string().optional(),
            "queriedAccountsCount": t.string().optional(),
            "accountCounts": t.array(t.proxy(renames["AccountCountIn"])).optional(),
            "accountCountErrors": t.array(
                t.proxy(renames["AccountCountErrorIn"])
            ).optional(),
            "nonQueryableAccounts": t.array(t.string()).optional(),
        }
    ).named(renames["MailCountResultIn"])
    types["MailCountResultOut"] = t.struct(
        {
            "matchingAccountsCount": t.string().optional(),
            "queriedAccountsCount": t.string().optional(),
            "accountCounts": t.array(t.proxy(renames["AccountCountOut"])).optional(),
            "accountCountErrors": t.array(
                t.proxy(renames["AccountCountErrorOut"])
            ).optional(),
            "nonQueryableAccounts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MailCountResultOut"])
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
            "voiceOptions": t.proxy(renames["VoiceExportOptionsIn"]).optional(),
            "region": t.string().optional(),
            "hangoutsChatOptions": t.proxy(
                renames["HangoutsChatExportOptionsIn"]
            ).optional(),
            "groupsOptions": t.proxy(renames["GroupsExportOptionsIn"]).optional(),
            "mailOptions": t.proxy(renames["MailExportOptionsIn"]).optional(),
            "driveOptions": t.proxy(renames["DriveExportOptionsIn"]).optional(),
        }
    ).named(renames["ExportOptionsIn"])
    types["ExportOptionsOut"] = t.struct(
        {
            "voiceOptions": t.proxy(renames["VoiceExportOptionsOut"]).optional(),
            "region": t.string().optional(),
            "hangoutsChatOptions": t.proxy(
                renames["HangoutsChatExportOptionsOut"]
            ).optional(),
            "groupsOptions": t.proxy(renames["GroupsExportOptionsOut"]).optional(),
            "mailOptions": t.proxy(renames["MailExportOptionsOut"]).optional(),
            "driveOptions": t.proxy(renames["DriveExportOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportOptionsOut"])

    functions = {}
    functions["operationsList"] = vault.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = vault.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = vault.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = vault.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersList"] = vault.delete(
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
    functions["mattersCreate"] = vault.delete(
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
    functions["mattersUpdate"] = vault.delete(
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
    functions["mattersClose"] = vault.delete(
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
    functions["mattersAddPermissions"] = vault.delete(
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
    functions["mattersDelete"] = vault.delete(
        "v1/matters/{matterId}",
        t.struct({"matterId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MatterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsList"] = vault.delete(
        "v1/matters/{matterId}/holds/{holdId}",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsAddHeldAccounts"] = vault.delete(
        "v1/matters/{matterId}/holds/{holdId}",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsCreate"] = vault.delete(
        "v1/matters/{matterId}/holds/{holdId}",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsGet"] = vault.delete(
        "v1/matters/{matterId}/holds/{holdId}",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsUpdate"] = vault.delete(
        "v1/matters/{matterId}/holds/{holdId}",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsRemoveHeldAccounts"] = vault.delete(
        "v1/matters/{matterId}/holds/{holdId}",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsDelete"] = vault.delete(
        "v1/matters/{matterId}/holds/{holdId}",
        t.struct(
            {
                "holdId": t.string().optional(),
                "matterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersHoldsAccountsList"] = vault.delete(
        "v1/matters/{matterId}/holds/{holdId}/accounts/{accountId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "matterId": t.string().optional(),
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
                "accountId": t.string().optional(),
                "matterId": t.string().optional(),
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
                "accountId": t.string().optional(),
                "matterId": t.string().optional(),
                "holdId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersSavedQueriesDelete"] = vault.get(
        "v1/matters/{matterId}/savedQueries/{savedQueryId}",
        t.struct(
            {
                "matterId": t.string().optional(),
                "savedQueryId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersSavedQueriesList"] = vault.get(
        "v1/matters/{matterId}/savedQueries/{savedQueryId}",
        t.struct(
            {
                "matterId": t.string().optional(),
                "savedQueryId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersSavedQueriesCreate"] = vault.get(
        "v1/matters/{matterId}/savedQueries/{savedQueryId}",
        t.struct(
            {
                "matterId": t.string().optional(),
                "savedQueryId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersSavedQueriesGet"] = vault.get(
        "v1/matters/{matterId}/savedQueries/{savedQueryId}",
        t.struct(
            {
                "matterId": t.string().optional(),
                "savedQueryId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mattersExportsCreate"] = vault.get(
        "v1/matters/{matterId}/exports",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "matterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="vault", renames=renames, types=types, functions=functions)
