from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_games():
    games = HTTPRuntime("https://games.googleapis.com/")

    renames = {
        "ErrorResponse": "_games_1_ErrorResponse",
        "EventUpdateResponseIn": "_games_2_EventUpdateResponseIn",
        "EventUpdateResponseOut": "_games_3_EventUpdateResponseOut",
        "StatsResponseIn": "_games_4_StatsResponseIn",
        "StatsResponseOut": "_games_5_StatsResponseOut",
        "AchievementUpdateRequestIn": "_games_6_AchievementUpdateRequestIn",
        "AchievementUpdateRequestOut": "_games_7_AchievementUpdateRequestOut",
        "AchievementDefinitionsListResponseIn": "_games_8_AchievementDefinitionsListResponseIn",
        "AchievementDefinitionsListResponseOut": "_games_9_AchievementDefinitionsListResponseOut",
        "PlayerExperienceInfoIn": "_games_10_PlayerExperienceInfoIn",
        "PlayerExperienceInfoOut": "_games_11_PlayerExperienceInfoOut",
        "LeaderboardEntryIn": "_games_12_LeaderboardEntryIn",
        "LeaderboardEntryOut": "_games_13_LeaderboardEntryOut",
        "PlayerIn": "_games_14_PlayerIn",
        "PlayerOut": "_games_15_PlayerOut",
        "ScopedPlayerIdsIn": "_games_16_ScopedPlayerIdsIn",
        "ScopedPlayerIdsOut": "_games_17_ScopedPlayerIdsOut",
        "AchievementSetStepsAtLeastResponseIn": "_games_18_AchievementSetStepsAtLeastResponseIn",
        "AchievementSetStepsAtLeastResponseOut": "_games_19_AchievementSetStepsAtLeastResponseOut",
        "PlayerListResponseIn": "_games_20_PlayerListResponseIn",
        "PlayerListResponseOut": "_games_21_PlayerListResponseOut",
        "LeaderboardIn": "_games_22_LeaderboardIn",
        "LeaderboardOut": "_games_23_LeaderboardOut",
        "ApplicationCategoryIn": "_games_24_ApplicationCategoryIn",
        "ApplicationCategoryOut": "_games_25_ApplicationCategoryOut",
        "MetagameConfigIn": "_games_26_MetagameConfigIn",
        "MetagameConfigOut": "_games_27_MetagameConfigOut",
        "AchievementRevealResponseIn": "_games_28_AchievementRevealResponseIn",
        "AchievementRevealResponseOut": "_games_29_AchievementRevealResponseOut",
        "PlayerScoreResponseIn": "_games_30_PlayerScoreResponseIn",
        "PlayerScoreResponseOut": "_games_31_PlayerScoreResponseOut",
        "AchievementUnlockResponseIn": "_games_32_AchievementUnlockResponseIn",
        "AchievementUnlockResponseOut": "_games_33_AchievementUnlockResponseOut",
        "ApplicationVerifyResponseIn": "_games_34_ApplicationVerifyResponseIn",
        "ApplicationVerifyResponseOut": "_games_35_ApplicationVerifyResponseOut",
        "PlayerScoreIn": "_games_36_PlayerScoreIn",
        "PlayerScoreOut": "_games_37_PlayerScoreOut",
        "EndPointIn": "_games_38_EndPointIn",
        "EndPointOut": "_games_39_EndPointOut",
        "EventPeriodUpdateIn": "_games_40_EventPeriodUpdateIn",
        "EventPeriodUpdateOut": "_games_41_EventPeriodUpdateOut",
        "PlayerAchievementIn": "_games_42_PlayerAchievementIn",
        "PlayerAchievementOut": "_games_43_PlayerAchievementOut",
        "EventDefinitionIn": "_games_44_EventDefinitionIn",
        "EventDefinitionOut": "_games_45_EventDefinitionOut",
        "InstanceWebDetailsIn": "_games_46_InstanceWebDetailsIn",
        "InstanceWebDetailsOut": "_games_47_InstanceWebDetailsOut",
        "CategoryListResponseIn": "_games_48_CategoryListResponseIn",
        "CategoryListResponseOut": "_games_49_CategoryListResponseOut",
        "AchievementUpdateResponseIn": "_games_50_AchievementUpdateResponseIn",
        "AchievementUpdateResponseOut": "_games_51_AchievementUpdateResponseOut",
        "GetMultipleApplicationPlayerIdsResponseIn": "_games_52_GetMultipleApplicationPlayerIdsResponseIn",
        "GetMultipleApplicationPlayerIdsResponseOut": "_games_53_GetMultipleApplicationPlayerIdsResponseOut",
        "EventRecordRequestIn": "_games_54_EventRecordRequestIn",
        "EventRecordRequestOut": "_games_55_EventRecordRequestOut",
        "InstanceIosDetailsIn": "_games_56_InstanceIosDetailsIn",
        "InstanceIosDetailsOut": "_games_57_InstanceIosDetailsOut",
        "InstanceAndroidDetailsIn": "_games_58_InstanceAndroidDetailsIn",
        "InstanceAndroidDetailsOut": "_games_59_InstanceAndroidDetailsOut",
        "AchievementIncrementResponseIn": "_games_60_AchievementIncrementResponseIn",
        "AchievementIncrementResponseOut": "_games_61_AchievementIncrementResponseOut",
        "SnapshotImageIn": "_games_62_SnapshotImageIn",
        "SnapshotImageOut": "_games_63_SnapshotImageOut",
        "LeaderboardListResponseIn": "_games_64_LeaderboardListResponseIn",
        "LeaderboardListResponseOut": "_games_65_LeaderboardListResponseOut",
        "SnapshotListResponseIn": "_games_66_SnapshotListResponseIn",
        "SnapshotListResponseOut": "_games_67_SnapshotListResponseOut",
        "LeaderboardScoreRankIn": "_games_68_LeaderboardScoreRankIn",
        "LeaderboardScoreRankOut": "_games_69_LeaderboardScoreRankOut",
        "PlayerLeaderboardScoreListResponseIn": "_games_70_PlayerLeaderboardScoreListResponseIn",
        "PlayerLeaderboardScoreListResponseOut": "_games_71_PlayerLeaderboardScoreListResponseOut",
        "ApplicationPlayerIdIn": "_games_72_ApplicationPlayerIdIn",
        "ApplicationPlayerIdOut": "_games_73_ApplicationPlayerIdOut",
        "PlayerLevelIn": "_games_74_PlayerLevelIn",
        "PlayerLevelOut": "_games_75_PlayerLevelOut",
        "EventUpdateRequestIn": "_games_76_EventUpdateRequestIn",
        "EventUpdateRequestOut": "_games_77_EventUpdateRequestOut",
        "AchievementUpdateMultipleResponseIn": "_games_78_AchievementUpdateMultipleResponseIn",
        "AchievementUpdateMultipleResponseOut": "_games_79_AchievementUpdateMultipleResponseOut",
        "PlayerLeaderboardScoreIn": "_games_80_PlayerLeaderboardScoreIn",
        "PlayerLeaderboardScoreOut": "_games_81_PlayerLeaderboardScoreOut",
        "PlayerAchievementListResponseIn": "_games_82_PlayerAchievementListResponseIn",
        "PlayerAchievementListResponseOut": "_games_83_PlayerAchievementListResponseOut",
        "AchievementDefinitionIn": "_games_84_AchievementDefinitionIn",
        "AchievementDefinitionOut": "_games_85_AchievementDefinitionOut",
        "ScoreSubmissionIn": "_games_86_ScoreSubmissionIn",
        "ScoreSubmissionOut": "_games_87_ScoreSubmissionOut",
        "RevisionCheckResponseIn": "_games_88_RevisionCheckResponseIn",
        "RevisionCheckResponseOut": "_games_89_RevisionCheckResponseOut",
        "GamesAchievementSetStepsAtLeastIn": "_games_90_GamesAchievementSetStepsAtLeastIn",
        "GamesAchievementSetStepsAtLeastOut": "_games_91_GamesAchievementSetStepsAtLeastOut",
        "PlayerScoreSubmissionListIn": "_games_92_PlayerScoreSubmissionListIn",
        "PlayerScoreSubmissionListOut": "_games_93_PlayerScoreSubmissionListOut",
        "SnapshotIn": "_games_94_SnapshotIn",
        "SnapshotOut": "_games_95_SnapshotOut",
        "PlayerScoreListResponseIn": "_games_96_PlayerScoreListResponseIn",
        "PlayerScoreListResponseOut": "_games_97_PlayerScoreListResponseOut",
        "GamesAchievementIncrementIn": "_games_98_GamesAchievementIncrementIn",
        "GamesAchievementIncrementOut": "_games_99_GamesAchievementIncrementOut",
        "PlayerEventListResponseIn": "_games_100_PlayerEventListResponseIn",
        "PlayerEventListResponseOut": "_games_101_PlayerEventListResponseOut",
        "EventChildIn": "_games_102_EventChildIn",
        "EventChildOut": "_games_103_EventChildOut",
        "ProfileSettingsIn": "_games_104_ProfileSettingsIn",
        "ProfileSettingsOut": "_games_105_ProfileSettingsOut",
        "EventRecordFailureIn": "_games_106_EventRecordFailureIn",
        "EventRecordFailureOut": "_games_107_EventRecordFailureOut",
        "PlayerEventIn": "_games_108_PlayerEventIn",
        "PlayerEventOut": "_games_109_PlayerEventOut",
        "EventPeriodRangeIn": "_games_110_EventPeriodRangeIn",
        "EventPeriodRangeOut": "_games_111_EventPeriodRangeOut",
        "AchievementUpdateMultipleRequestIn": "_games_112_AchievementUpdateMultipleRequestIn",
        "AchievementUpdateMultipleRequestOut": "_games_113_AchievementUpdateMultipleRequestOut",
        "EventBatchRecordFailureIn": "_games_114_EventBatchRecordFailureIn",
        "EventBatchRecordFailureOut": "_games_115_EventBatchRecordFailureOut",
        "InstanceIn": "_games_116_InstanceIn",
        "InstanceOut": "_games_117_InstanceOut",
        "EventDefinitionListResponseIn": "_games_118_EventDefinitionListResponseIn",
        "EventDefinitionListResponseOut": "_games_119_EventDefinitionListResponseOut",
        "ImageAssetIn": "_games_120_ImageAssetIn",
        "ImageAssetOut": "_games_121_ImageAssetOut",
        "ApplicationIn": "_games_122_ApplicationIn",
        "ApplicationOut": "_games_123_ApplicationOut",
        "CategoryIn": "_games_124_CategoryIn",
        "CategoryOut": "_games_125_CategoryOut",
        "LeaderboardScoresIn": "_games_126_LeaderboardScoresIn",
        "LeaderboardScoresOut": "_games_127_LeaderboardScoresOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EventUpdateResponseIn"] = t.struct(
        {
            "eventFailures": t.array(
                t.proxy(renames["EventRecordFailureIn"])
            ).optional(),
            "playerEvents": t.array(t.proxy(renames["PlayerEventIn"])).optional(),
            "kind": t.string().optional(),
            "batchFailures": t.array(
                t.proxy(renames["EventBatchRecordFailureIn"])
            ).optional(),
        }
    ).named(renames["EventUpdateResponseIn"])
    types["EventUpdateResponseOut"] = t.struct(
        {
            "eventFailures": t.array(
                t.proxy(renames["EventRecordFailureOut"])
            ).optional(),
            "playerEvents": t.array(t.proxy(renames["PlayerEventOut"])).optional(),
            "kind": t.string().optional(),
            "batchFailures": t.array(
                t.proxy(renames["EventBatchRecordFailureOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventUpdateResponseOut"])
    types["StatsResponseIn"] = t.struct(
        {
            "avg_session_length_minutes": t.number().optional(),
            "spend_probability": t.number().optional(),
            "num_purchases": t.integer().optional(),
            "days_since_last_played": t.integer().optional(),
            "num_sessions_percentile": t.number().optional(),
            "high_spender_probability": t.number().optional(),
            "kind": t.string().optional(),
            "num_sessions": t.integer().optional(),
            "churn_probability": t.number().optional(),
            "spend_percentile": t.number().optional(),
            "total_spend_next_28_days": t.number().optional(),
        }
    ).named(renames["StatsResponseIn"])
    types["StatsResponseOut"] = t.struct(
        {
            "avg_session_length_minutes": t.number().optional(),
            "spend_probability": t.number().optional(),
            "num_purchases": t.integer().optional(),
            "days_since_last_played": t.integer().optional(),
            "num_sessions_percentile": t.number().optional(),
            "high_spender_probability": t.number().optional(),
            "kind": t.string().optional(),
            "num_sessions": t.integer().optional(),
            "churn_probability": t.number().optional(),
            "spend_percentile": t.number().optional(),
            "total_spend_next_28_days": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatsResponseOut"])
    types["AchievementUpdateRequestIn"] = t.struct(
        {
            "achievementId": t.string().optional(),
            "updateType": t.string().optional(),
            "kind": t.string().optional(),
            "incrementPayload": t.proxy(
                renames["GamesAchievementIncrementIn"]
            ).optional(),
            "setStepsAtLeastPayload": t.proxy(
                renames["GamesAchievementSetStepsAtLeastIn"]
            ).optional(),
        }
    ).named(renames["AchievementUpdateRequestIn"])
    types["AchievementUpdateRequestOut"] = t.struct(
        {
            "achievementId": t.string().optional(),
            "updateType": t.string().optional(),
            "kind": t.string().optional(),
            "incrementPayload": t.proxy(
                renames["GamesAchievementIncrementOut"]
            ).optional(),
            "setStepsAtLeastPayload": t.proxy(
                renames["GamesAchievementSetStepsAtLeastOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementUpdateRequestOut"])
    types["AchievementDefinitionsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["AchievementDefinitionIn"])).optional(),
        }
    ).named(renames["AchievementDefinitionsListResponseIn"])
    types["AchievementDefinitionsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["AchievementDefinitionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementDefinitionsListResponseOut"])
    types["PlayerExperienceInfoIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "lastLevelUpTimestampMillis": t.string().optional(),
            "currentExperiencePoints": t.string().optional(),
            "currentLevel": t.proxy(renames["PlayerLevelIn"]).optional(),
            "nextLevel": t.proxy(renames["PlayerLevelIn"]).optional(),
        }
    ).named(renames["PlayerExperienceInfoIn"])
    types["PlayerExperienceInfoOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "lastLevelUpTimestampMillis": t.string().optional(),
            "currentExperiencePoints": t.string().optional(),
            "currentLevel": t.proxy(renames["PlayerLevelOut"]).optional(),
            "nextLevel": t.proxy(renames["PlayerLevelOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerExperienceInfoOut"])
    types["LeaderboardEntryIn"] = t.struct(
        {
            "formattedScore": t.string().optional(),
            "scoreRank": t.string().optional(),
            "formattedScoreRank": t.string().optional(),
            "scoreTag": t.string().optional(),
            "writeTimestampMillis": t.string().optional(),
            "player": t.proxy(renames["PlayerIn"]).optional(),
            "kind": t.string().optional(),
            "scoreValue": t.string().optional(),
            "timeSpan": t.string().optional(),
        }
    ).named(renames["LeaderboardEntryIn"])
    types["LeaderboardEntryOut"] = t.struct(
        {
            "formattedScore": t.string().optional(),
            "scoreRank": t.string().optional(),
            "formattedScoreRank": t.string().optional(),
            "scoreTag": t.string().optional(),
            "writeTimestampMillis": t.string().optional(),
            "player": t.proxy(renames["PlayerOut"]).optional(),
            "kind": t.string().optional(),
            "scoreValue": t.string().optional(),
            "timeSpan": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaderboardEntryOut"])
    types["PlayerIn"] = t.struct(
        {
            "profileSettings": t.proxy(renames["ProfileSettingsIn"]).optional(),
            "name": t.struct(
                {
                    "familyName": t.string().optional(),
                    "givenName": t.string().optional(),
                }
            ).optional(),
            "experienceInfo": t.proxy(renames["PlayerExperienceInfoIn"]).optional(),
            "originalPlayerId": t.string().optional(),
            "title": t.string().optional(),
            "gamePlayerId": t.string().optional(),
            "displayName": t.string().optional(),
            "avatarImageUrl": t.string().optional(),
            "bannerUrlLandscape": t.string().optional(),
            "bannerUrlPortrait": t.string().optional(),
            "friendStatus": t.string().optional(),
            "playerId": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PlayerIn"])
    types["PlayerOut"] = t.struct(
        {
            "profileSettings": t.proxy(renames["ProfileSettingsOut"]).optional(),
            "name": t.struct(
                {
                    "familyName": t.string().optional(),
                    "givenName": t.string().optional(),
                }
            ).optional(),
            "experienceInfo": t.proxy(renames["PlayerExperienceInfoOut"]).optional(),
            "originalPlayerId": t.string().optional(),
            "title": t.string().optional(),
            "gamePlayerId": t.string().optional(),
            "displayName": t.string().optional(),
            "avatarImageUrl": t.string().optional(),
            "bannerUrlLandscape": t.string().optional(),
            "bannerUrlPortrait": t.string().optional(),
            "friendStatus": t.string().optional(),
            "playerId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerOut"])
    types["ScopedPlayerIdsIn"] = t.struct(
        {
            "gamePlayerId": t.string().optional(),
            "developerPlayerKey": t.string().optional(),
        }
    ).named(renames["ScopedPlayerIdsIn"])
    types["ScopedPlayerIdsOut"] = t.struct(
        {
            "gamePlayerId": t.string().optional(),
            "developerPlayerKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScopedPlayerIdsOut"])
    types["AchievementSetStepsAtLeastResponseIn"] = t.struct(
        {
            "currentSteps": t.integer().optional(),
            "kind": t.string().optional(),
            "newlyUnlocked": t.boolean().optional(),
        }
    ).named(renames["AchievementSetStepsAtLeastResponseIn"])
    types["AchievementSetStepsAtLeastResponseOut"] = t.struct(
        {
            "currentSteps": t.integer().optional(),
            "kind": t.string().optional(),
            "newlyUnlocked": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementSetStepsAtLeastResponseOut"])
    types["PlayerListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["PlayerIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PlayerListResponseIn"])
    types["PlayerListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["PlayerOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerListResponseOut"])
    types["LeaderboardIn"] = t.struct(
        {
            "order": t.string().optional(),
            "isIconUrlDefault": t.boolean().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "iconUrl": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LeaderboardIn"])
    types["LeaderboardOut"] = t.struct(
        {
            "order": t.string().optional(),
            "isIconUrlDefault": t.boolean().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "iconUrl": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaderboardOut"])
    types["ApplicationCategoryIn"] = t.struct(
        {
            "primary": t.string().optional(),
            "secondary": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ApplicationCategoryIn"])
    types["ApplicationCategoryOut"] = t.struct(
        {
            "primary": t.string().optional(),
            "secondary": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationCategoryOut"])
    types["MetagameConfigIn"] = t.struct(
        {
            "currentVersion": t.integer().optional(),
            "kind": t.string().optional(),
            "playerLevels": t.array(t.proxy(renames["PlayerLevelIn"])).optional(),
        }
    ).named(renames["MetagameConfigIn"])
    types["MetagameConfigOut"] = t.struct(
        {
            "currentVersion": t.integer().optional(),
            "kind": t.string().optional(),
            "playerLevels": t.array(t.proxy(renames["PlayerLevelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetagameConfigOut"])
    types["AchievementRevealResponseIn"] = t.struct(
        {"kind": t.string().optional(), "currentState": t.string().optional()}
    ).named(renames["AchievementRevealResponseIn"])
    types["AchievementRevealResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "currentState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementRevealResponseOut"])
    types["PlayerScoreResponseIn"] = t.struct(
        {
            "beatenScoreTimeSpans": t.array(t.string()).optional(),
            "unbeatenScores": t.array(t.proxy(renames["PlayerScoreIn"])).optional(),
            "formattedScore": t.string().optional(),
            "leaderboardId": t.string().optional(),
            "scoreTag": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PlayerScoreResponseIn"])
    types["PlayerScoreResponseOut"] = t.struct(
        {
            "beatenScoreTimeSpans": t.array(t.string()).optional(),
            "unbeatenScores": t.array(t.proxy(renames["PlayerScoreOut"])).optional(),
            "formattedScore": t.string().optional(),
            "leaderboardId": t.string().optional(),
            "scoreTag": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerScoreResponseOut"])
    types["AchievementUnlockResponseIn"] = t.struct(
        {"newlyUnlocked": t.boolean().optional(), "kind": t.string().optional()}
    ).named(renames["AchievementUnlockResponseIn"])
    types["AchievementUnlockResponseOut"] = t.struct(
        {
            "newlyUnlocked": t.boolean().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementUnlockResponseOut"])
    types["ApplicationVerifyResponseIn"] = t.struct(
        {
            "alternate_player_id": t.string().optional(),
            "kind": t.string().optional(),
            "player_id": t.string().optional(),
        }
    ).named(renames["ApplicationVerifyResponseIn"])
    types["ApplicationVerifyResponseOut"] = t.struct(
        {
            "alternate_player_id": t.string().optional(),
            "kind": t.string().optional(),
            "player_id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationVerifyResponseOut"])
    types["PlayerScoreIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "formattedScore": t.string().optional(),
            "score": t.string().optional(),
            "scoreTag": t.string().optional(),
            "timeSpan": t.string().optional(),
        }
    ).named(renames["PlayerScoreIn"])
    types["PlayerScoreOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "formattedScore": t.string().optional(),
            "score": t.string().optional(),
            "scoreTag": t.string().optional(),
            "timeSpan": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerScoreOut"])
    types["EndPointIn"] = t.struct({"url": t.string().optional()}).named(
        renames["EndPointIn"]
    )
    types["EndPointOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndPointOut"])
    types["EventPeriodUpdateIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "updates": t.array(t.proxy(renames["EventUpdateRequestIn"])).optional(),
            "timePeriod": t.proxy(renames["EventPeriodRangeIn"]).optional(),
        }
    ).named(renames["EventPeriodUpdateIn"])
    types["EventPeriodUpdateOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "updates": t.array(t.proxy(renames["EventUpdateRequestOut"])).optional(),
            "timePeriod": t.proxy(renames["EventPeriodRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventPeriodUpdateOut"])
    types["PlayerAchievementIn"] = t.struct(
        {
            "experiencePoints": t.string().optional(),
            "id": t.string().optional(),
            "achievementState": t.string().optional(),
            "lastUpdatedTimestamp": t.string().optional(),
            "kind": t.string().optional(),
            "currentSteps": t.integer().optional(),
            "formattedCurrentStepsString": t.string().optional(),
        }
    ).named(renames["PlayerAchievementIn"])
    types["PlayerAchievementOut"] = t.struct(
        {
            "experiencePoints": t.string().optional(),
            "id": t.string().optional(),
            "achievementState": t.string().optional(),
            "lastUpdatedTimestamp": t.string().optional(),
            "kind": t.string().optional(),
            "currentSteps": t.integer().optional(),
            "formattedCurrentStepsString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerAchievementOut"])
    types["EventDefinitionIn"] = t.struct(
        {
            "isDefaultImageUrl": t.boolean().optional(),
            "visibility": t.string().optional(),
            "childEvents": t.array(t.proxy(renames["EventChildIn"])).optional(),
            "kind": t.string().optional(),
            "displayName": t.string().optional(),
            "imageUrl": t.string().optional(),
            "description": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["EventDefinitionIn"])
    types["EventDefinitionOut"] = t.struct(
        {
            "isDefaultImageUrl": t.boolean().optional(),
            "visibility": t.string().optional(),
            "childEvents": t.array(t.proxy(renames["EventChildOut"])).optional(),
            "kind": t.string().optional(),
            "displayName": t.string().optional(),
            "imageUrl": t.string().optional(),
            "description": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventDefinitionOut"])
    types["InstanceWebDetailsIn"] = t.struct(
        {
            "preferred": t.boolean().optional(),
            "launchUrl": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["InstanceWebDetailsIn"])
    types["InstanceWebDetailsOut"] = t.struct(
        {
            "preferred": t.boolean().optional(),
            "launchUrl": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceWebDetailsOut"])
    types["CategoryListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["CategoryIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["CategoryListResponseIn"])
    types["CategoryListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryListResponseOut"])
    types["AchievementUpdateResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "currentSteps": t.integer().optional(),
            "achievementId": t.string().optional(),
            "updateOccurred": t.boolean().optional(),
            "newlyUnlocked": t.boolean().optional(),
            "currentState": t.string().optional(),
        }
    ).named(renames["AchievementUpdateResponseIn"])
    types["AchievementUpdateResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "currentSteps": t.integer().optional(),
            "achievementId": t.string().optional(),
            "updateOccurred": t.boolean().optional(),
            "newlyUnlocked": t.boolean().optional(),
            "currentState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementUpdateResponseOut"])
    types["GetMultipleApplicationPlayerIdsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GetMultipleApplicationPlayerIdsResponseIn"])
    types["GetMultipleApplicationPlayerIdsResponseOut"] = t.struct(
        {
            "playerIds": t.array(t.proxy(renames["ApplicationPlayerIdOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetMultipleApplicationPlayerIdsResponseOut"])
    types["EventRecordRequestIn"] = t.struct(
        {
            "currentTimeMillis": t.string().optional(),
            "timePeriods": t.array(t.proxy(renames["EventPeriodUpdateIn"])).optional(),
            "requestId": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["EventRecordRequestIn"])
    types["EventRecordRequestOut"] = t.struct(
        {
            "currentTimeMillis": t.string().optional(),
            "timePeriods": t.array(t.proxy(renames["EventPeriodUpdateOut"])).optional(),
            "requestId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventRecordRequestOut"])
    types["InstanceIosDetailsIn"] = t.struct(
        {
            "preferredForIpad": t.boolean().optional(),
            "supportIpad": t.boolean().optional(),
            "bundleIdentifier": t.string().optional(),
            "supportIphone": t.boolean().optional(),
            "itunesAppId": t.string().optional(),
            "preferredForIphone": t.boolean().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["InstanceIosDetailsIn"])
    types["InstanceIosDetailsOut"] = t.struct(
        {
            "preferredForIpad": t.boolean().optional(),
            "supportIpad": t.boolean().optional(),
            "bundleIdentifier": t.string().optional(),
            "supportIphone": t.boolean().optional(),
            "itunesAppId": t.string().optional(),
            "preferredForIphone": t.boolean().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceIosDetailsOut"])
    types["InstanceAndroidDetailsIn"] = t.struct(
        {
            "enablePiracyCheck": t.boolean().optional(),
            "preferred": t.boolean().optional(),
            "kind": t.string().optional(),
            "packageName": t.string().optional(),
        }
    ).named(renames["InstanceAndroidDetailsIn"])
    types["InstanceAndroidDetailsOut"] = t.struct(
        {
            "enablePiracyCheck": t.boolean().optional(),
            "preferred": t.boolean().optional(),
            "kind": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceAndroidDetailsOut"])
    types["AchievementIncrementResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "currentSteps": t.integer().optional(),
            "newlyUnlocked": t.boolean().optional(),
        }
    ).named(renames["AchievementIncrementResponseIn"])
    types["AchievementIncrementResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "currentSteps": t.integer().optional(),
            "newlyUnlocked": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementIncrementResponseOut"])
    types["SnapshotImageIn"] = t.struct(
        {
            "mime_type": t.string().optional(),
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "kind": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["SnapshotImageIn"])
    types["SnapshotImageOut"] = t.struct(
        {
            "mime_type": t.string().optional(),
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "kind": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotImageOut"])
    types["LeaderboardListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["LeaderboardIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["LeaderboardListResponseIn"])
    types["LeaderboardListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["LeaderboardOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaderboardListResponseOut"])
    types["SnapshotListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["SnapshotIn"])).optional(),
        }
    ).named(renames["SnapshotListResponseIn"])
    types["SnapshotListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["SnapshotOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotListResponseOut"])
    types["LeaderboardScoreRankIn"] = t.struct(
        {
            "formattedNumScores": t.string().optional(),
            "rank": t.string().optional(),
            "formattedRank": t.string().optional(),
            "numScores": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LeaderboardScoreRankIn"])
    types["LeaderboardScoreRankOut"] = t.struct(
        {
            "formattedNumScores": t.string().optional(),
            "rank": t.string().optional(),
            "formattedRank": t.string().optional(),
            "numScores": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaderboardScoreRankOut"])
    types["PlayerLeaderboardScoreListResponseIn"] = t.struct(
        {
            "player": t.proxy(renames["PlayerIn"]).optional(),
            "items": t.array(t.proxy(renames["PlayerLeaderboardScoreIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["PlayerLeaderboardScoreListResponseIn"])
    types["PlayerLeaderboardScoreListResponseOut"] = t.struct(
        {
            "player": t.proxy(renames["PlayerOut"]).optional(),
            "items": t.array(t.proxy(renames["PlayerLeaderboardScoreOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerLeaderboardScoreListResponseOut"])
    types["ApplicationPlayerIdIn"] = t.struct(
        {"applicationId": t.string().optional(), "playerId": t.string().optional()}
    ).named(renames["ApplicationPlayerIdIn"])
    types["ApplicationPlayerIdOut"] = t.struct(
        {
            "applicationId": t.string().optional(),
            "playerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationPlayerIdOut"])
    types["PlayerLevelIn"] = t.struct(
        {
            "minExperiencePoints": t.string().optional(),
            "kind": t.string().optional(),
            "maxExperiencePoints": t.string().optional(),
            "level": t.integer().optional(),
        }
    ).named(renames["PlayerLevelIn"])
    types["PlayerLevelOut"] = t.struct(
        {
            "minExperiencePoints": t.string().optional(),
            "kind": t.string().optional(),
            "maxExperiencePoints": t.string().optional(),
            "level": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerLevelOut"])
    types["EventUpdateRequestIn"] = t.struct(
        {
            "definitionId": t.string().optional(),
            "kind": t.string().optional(),
            "updateCount": t.string().optional(),
        }
    ).named(renames["EventUpdateRequestIn"])
    types["EventUpdateRequestOut"] = t.struct(
        {
            "definitionId": t.string().optional(),
            "kind": t.string().optional(),
            "updateCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventUpdateRequestOut"])
    types["AchievementUpdateMultipleResponseIn"] = t.struct(
        {
            "updatedAchievements": t.array(
                t.proxy(renames["AchievementUpdateResponseIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AchievementUpdateMultipleResponseIn"])
    types["AchievementUpdateMultipleResponseOut"] = t.struct(
        {
            "updatedAchievements": t.array(
                t.proxy(renames["AchievementUpdateResponseOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementUpdateMultipleResponseOut"])
    types["PlayerLeaderboardScoreIn"] = t.struct(
        {
            "scoreTag": t.string().optional(),
            "scoreString": t.string().optional(),
            "leaderboard_id": t.string().optional(),
            "socialRank": t.proxy(renames["LeaderboardScoreRankIn"]).optional(),
            "scoreValue": t.string().optional(),
            "timeSpan": t.string().optional(),
            "writeTimestamp": t.string().optional(),
            "kind": t.string().optional(),
            "publicRank": t.proxy(renames["LeaderboardScoreRankIn"]).optional(),
            "friendsRank": t.proxy(renames["LeaderboardScoreRankIn"]).optional(),
        }
    ).named(renames["PlayerLeaderboardScoreIn"])
    types["PlayerLeaderboardScoreOut"] = t.struct(
        {
            "scoreTag": t.string().optional(),
            "scoreString": t.string().optional(),
            "leaderboard_id": t.string().optional(),
            "socialRank": t.proxy(renames["LeaderboardScoreRankOut"]).optional(),
            "scoreValue": t.string().optional(),
            "timeSpan": t.string().optional(),
            "writeTimestamp": t.string().optional(),
            "kind": t.string().optional(),
            "publicRank": t.proxy(renames["LeaderboardScoreRankOut"]).optional(),
            "friendsRank": t.proxy(renames["LeaderboardScoreRankOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerLeaderboardScoreOut"])
    types["PlayerAchievementListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["PlayerAchievementIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PlayerAchievementListResponseIn"])
    types["PlayerAchievementListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["PlayerAchievementOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerAchievementListResponseOut"])
    types["AchievementDefinitionIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "initialState": t.string().optional(),
            "description": t.string().optional(),
            "totalSteps": t.integer().optional(),
            "unlockedIconUrl": t.string().optional(),
            "id": t.string().optional(),
            "formattedTotalSteps": t.string().optional(),
            "achievementType": t.string().optional(),
            "isRevealedIconUrlDefault": t.boolean().optional(),
            "experiencePoints": t.string().optional(),
            "revealedIconUrl": t.string().optional(),
            "name": t.string().optional(),
            "isUnlockedIconUrlDefault": t.boolean().optional(),
        }
    ).named(renames["AchievementDefinitionIn"])
    types["AchievementDefinitionOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "initialState": t.string().optional(),
            "description": t.string().optional(),
            "totalSteps": t.integer().optional(),
            "unlockedIconUrl": t.string().optional(),
            "id": t.string().optional(),
            "formattedTotalSteps": t.string().optional(),
            "achievementType": t.string().optional(),
            "isRevealedIconUrlDefault": t.boolean().optional(),
            "experiencePoints": t.string().optional(),
            "revealedIconUrl": t.string().optional(),
            "name": t.string().optional(),
            "isUnlockedIconUrlDefault": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementDefinitionOut"])
    types["ScoreSubmissionIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "leaderboardId": t.string().optional(),
            "score": t.string().optional(),
            "signature": t.string().optional(),
            "scoreTag": t.string().optional(),
        }
    ).named(renames["ScoreSubmissionIn"])
    types["ScoreSubmissionOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "leaderboardId": t.string().optional(),
            "score": t.string().optional(),
            "signature": t.string().optional(),
            "scoreTag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScoreSubmissionOut"])
    types["RevisionCheckResponseIn"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "kind": t.string().optional(),
            "revisionStatus": t.string().optional(),
        }
    ).named(renames["RevisionCheckResponseIn"])
    types["RevisionCheckResponseOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "kind": t.string().optional(),
            "revisionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevisionCheckResponseOut"])
    types["GamesAchievementSetStepsAtLeastIn"] = t.struct(
        {"kind": t.string().optional(), "steps": t.integer().optional()}
    ).named(renames["GamesAchievementSetStepsAtLeastIn"])
    types["GamesAchievementSetStepsAtLeastOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "steps": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GamesAchievementSetStepsAtLeastOut"])
    types["PlayerScoreSubmissionListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "scores": t.array(t.proxy(renames["ScoreSubmissionIn"])).optional(),
        }
    ).named(renames["PlayerScoreSubmissionListIn"])
    types["PlayerScoreSubmissionListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "scores": t.array(t.proxy(renames["ScoreSubmissionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerScoreSubmissionListOut"])
    types["SnapshotIn"] = t.struct(
        {
            "lastModifiedMillis": t.string().optional(),
            "description": t.string().optional(),
            "id": t.string().optional(),
            "durationMillis": t.string().optional(),
            "driveId": t.string().optional(),
            "type": t.string().optional(),
            "uniqueName": t.string().optional(),
            "title": t.string().optional(),
            "progressValue": t.string().optional(),
            "kind": t.string().optional(),
            "coverImage": t.proxy(renames["SnapshotImageIn"]).optional(),
        }
    ).named(renames["SnapshotIn"])
    types["SnapshotOut"] = t.struct(
        {
            "lastModifiedMillis": t.string().optional(),
            "description": t.string().optional(),
            "id": t.string().optional(),
            "durationMillis": t.string().optional(),
            "driveId": t.string().optional(),
            "type": t.string().optional(),
            "uniqueName": t.string().optional(),
            "title": t.string().optional(),
            "progressValue": t.string().optional(),
            "kind": t.string().optional(),
            "coverImage": t.proxy(renames["SnapshotImageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotOut"])
    types["PlayerScoreListResponseIn"] = t.struct(
        {
            "submittedScores": t.array(
                t.proxy(renames["PlayerScoreResponseIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PlayerScoreListResponseIn"])
    types["PlayerScoreListResponseOut"] = t.struct(
        {
            "submittedScores": t.array(
                t.proxy(renames["PlayerScoreResponseOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerScoreListResponseOut"])
    types["GamesAchievementIncrementIn"] = t.struct(
        {
            "steps": t.integer().optional(),
            "kind": t.string().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["GamesAchievementIncrementIn"])
    types["GamesAchievementIncrementOut"] = t.struct(
        {
            "steps": t.integer().optional(),
            "kind": t.string().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GamesAchievementIncrementOut"])
    types["PlayerEventListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["PlayerEventIn"])).optional(),
        }
    ).named(renames["PlayerEventListResponseIn"])
    types["PlayerEventListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["PlayerEventOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerEventListResponseOut"])
    types["EventChildIn"] = t.struct(
        {"kind": t.string().optional(), "childId": t.string().optional()}
    ).named(renames["EventChildIn"])
    types["EventChildOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "childId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventChildOut"])
    types["ProfileSettingsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "profileVisible": t.boolean().optional(),
            "friendsListVisibility": t.string(),
        }
    ).named(renames["ProfileSettingsIn"])
    types["ProfileSettingsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "profileVisible": t.boolean().optional(),
            "friendsListVisibility": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileSettingsOut"])
    types["EventRecordFailureIn"] = t.struct(
        {
            "failureCause": t.string().optional(),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
        }
    ).named(renames["EventRecordFailureIn"])
    types["EventRecordFailureOut"] = t.struct(
        {
            "failureCause": t.string().optional(),
            "kind": t.string().optional(),
            "eventId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventRecordFailureOut"])
    types["PlayerEventIn"] = t.struct(
        {
            "playerId": t.string().optional(),
            "definitionId": t.string().optional(),
            "kind": t.string().optional(),
            "formattedNumEvents": t.string().optional(),
            "numEvents": t.string().optional(),
        }
    ).named(renames["PlayerEventIn"])
    types["PlayerEventOut"] = t.struct(
        {
            "playerId": t.string().optional(),
            "definitionId": t.string().optional(),
            "kind": t.string().optional(),
            "formattedNumEvents": t.string().optional(),
            "numEvents": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerEventOut"])
    types["EventPeriodRangeIn"] = t.struct(
        {
            "periodEndMillis": t.string().optional(),
            "periodStartMillis": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["EventPeriodRangeIn"])
    types["EventPeriodRangeOut"] = t.struct(
        {
            "periodEndMillis": t.string().optional(),
            "periodStartMillis": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventPeriodRangeOut"])
    types["AchievementUpdateMultipleRequestIn"] = t.struct(
        {
            "updates": t.array(
                t.proxy(renames["AchievementUpdateRequestIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AchievementUpdateMultipleRequestIn"])
    types["AchievementUpdateMultipleRequestOut"] = t.struct(
        {
            "updates": t.array(
                t.proxy(renames["AchievementUpdateRequestOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementUpdateMultipleRequestOut"])
    types["EventBatchRecordFailureIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "failureCause": t.string().optional(),
            "range": t.proxy(renames["EventPeriodRangeIn"]).optional(),
        }
    ).named(renames["EventBatchRecordFailureIn"])
    types["EventBatchRecordFailureOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "failureCause": t.string().optional(),
            "range": t.proxy(renames["EventPeriodRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventBatchRecordFailureOut"])
    types["InstanceIn"] = t.struct(
        {
            "iosInstance": t.proxy(renames["InstanceIosDetailsIn"]).optional(),
            "realtimePlay": t.boolean().optional(),
            "kind": t.string().optional(),
            "androidInstance": t.proxy(renames["InstanceAndroidDetailsIn"]).optional(),
            "acquisitionUri": t.string().optional(),
            "platformType": t.string().optional(),
            "webInstance": t.proxy(renames["InstanceWebDetailsIn"]).optional(),
            "name": t.string().optional(),
            "turnBasedPlay": t.boolean().optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "iosInstance": t.proxy(renames["InstanceIosDetailsOut"]).optional(),
            "realtimePlay": t.boolean().optional(),
            "kind": t.string().optional(),
            "androidInstance": t.proxy(renames["InstanceAndroidDetailsOut"]).optional(),
            "acquisitionUri": t.string().optional(),
            "platformType": t.string().optional(),
            "webInstance": t.proxy(renames["InstanceWebDetailsOut"]).optional(),
            "name": t.string().optional(),
            "turnBasedPlay": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["EventDefinitionListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["EventDefinitionIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["EventDefinitionListResponseIn"])
    types["EventDefinitionListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["EventDefinitionOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventDefinitionListResponseOut"])
    types["ImageAssetIn"] = t.struct(
        {
            "name": t.string().optional(),
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "kind": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["ImageAssetIn"])
    types["ImageAssetOut"] = t.struct(
        {
            "name": t.string().optional(),
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "kind": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageAssetOut"])
    types["ApplicationIn"] = t.struct(
        {
            "assets": t.array(t.proxy(renames["ImageAssetIn"])).optional(),
            "leaderboard_count": t.integer().optional(),
            "name": t.string().optional(),
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
            "lastUpdatedTimestamp": t.string().optional(),
            "kind": t.string().optional(),
            "themeColor": t.string().optional(),
            "enabledFeatures": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "author": t.string().optional(),
            "achievement_count": t.integer().optional(),
            "id": t.string().optional(),
            "category": t.proxy(renames["ApplicationCategoryIn"]).optional(),
        }
    ).named(renames["ApplicationIn"])
    types["ApplicationOut"] = t.struct(
        {
            "assets": t.array(t.proxy(renames["ImageAssetOut"])).optional(),
            "leaderboard_count": t.integer().optional(),
            "name": t.string().optional(),
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "lastUpdatedTimestamp": t.string().optional(),
            "kind": t.string().optional(),
            "themeColor": t.string().optional(),
            "enabledFeatures": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "author": t.string().optional(),
            "achievement_count": t.integer().optional(),
            "id": t.string().optional(),
            "category": t.proxy(renames["ApplicationCategoryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationOut"])
    types["CategoryIn"] = t.struct(
        {
            "experiencePoints": t.string().optional(),
            "category": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["CategoryIn"])
    types["CategoryOut"] = t.struct(
        {
            "experiencePoints": t.string().optional(),
            "category": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryOut"])
    types["LeaderboardScoresIn"] = t.struct(
        {
            "playerScore": t.proxy(renames["LeaderboardEntryIn"]).optional(),
            "kind": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "numScores": t.string().optional(),
            "items": t.array(t.proxy(renames["LeaderboardEntryIn"])).optional(),
        }
    ).named(renames["LeaderboardScoresIn"])
    types["LeaderboardScoresOut"] = t.struct(
        {
            "playerScore": t.proxy(renames["LeaderboardEntryOut"]).optional(),
            "kind": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "numScores": t.string().optional(),
            "items": t.array(t.proxy(renames["LeaderboardEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaderboardScoresOut"])

    functions = {}
    functions["metagameListCategoriesByPlayer"] = games.get(
        "games/v1/metagameConfig",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["MetagameConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["metagameGetMetagameConfig"] = games.get(
        "games/v1/metagameConfig",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["MetagameConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresGet"] = games.get(
        "games/v1/leaderboards/{leaderboardId}/scores/{collection}",
        t.struct(
            {
                "language": t.string().optional(),
                "timeSpan": t.string().optional(),
                "maxResults": t.integer().optional(),
                "leaderboardId": t.string().optional(),
                "collection": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardScoresOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresSubmitMultiple"] = games.get(
        "games/v1/leaderboards/{leaderboardId}/scores/{collection}",
        t.struct(
            {
                "language": t.string().optional(),
                "timeSpan": t.string().optional(),
                "maxResults": t.integer().optional(),
                "leaderboardId": t.string().optional(),
                "collection": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardScoresOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresListWindow"] = games.get(
        "games/v1/leaderboards/{leaderboardId}/scores/{collection}",
        t.struct(
            {
                "language": t.string().optional(),
                "timeSpan": t.string().optional(),
                "maxResults": t.integer().optional(),
                "leaderboardId": t.string().optional(),
                "collection": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardScoresOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresSubmit"] = games.get(
        "games/v1/leaderboards/{leaderboardId}/scores/{collection}",
        t.struct(
            {
                "language": t.string().optional(),
                "timeSpan": t.string().optional(),
                "maxResults": t.integer().optional(),
                "leaderboardId": t.string().optional(),
                "collection": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardScoresOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresList"] = games.get(
        "games/v1/leaderboards/{leaderboardId}/scores/{collection}",
        t.struct(
            {
                "language": t.string().optional(),
                "timeSpan": t.string().optional(),
                "maxResults": t.integer().optional(),
                "leaderboardId": t.string().optional(),
                "collection": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardScoresOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["leaderboardsList"] = games.get(
        "games/v1/leaderboards/{leaderboardId}",
        t.struct(
            {
                "leaderboardId": t.string().optional(),
                "language": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["leaderboardsGet"] = games.get(
        "games/v1/leaderboards/{leaderboardId}",
        t.struct(
            {
                "leaderboardId": t.string().optional(),
                "language": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["applicationsPlayed"] = games.post(
        "games/v1/applications/getEndPoint",
        t.struct(
            {
                "endPointType": t.string().optional(),
                "applicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EndPointOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["applicationsGet"] = games.post(
        "games/v1/applications/getEndPoint",
        t.struct(
            {
                "endPointType": t.string().optional(),
                "applicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EndPointOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["applicationsVerify"] = games.post(
        "games/v1/applications/getEndPoint",
        t.struct(
            {
                "endPointType": t.string().optional(),
                "applicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EndPointOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["applicationsGetEndPoint"] = games.post(
        "games/v1/applications/getEndPoint",
        t.struct(
            {
                "endPointType": t.string().optional(),
                "applicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EndPointOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["snapshotsList"] = games.get(
        "games/v1/snapshots/{snapshotId}",
        t.struct(
            {
                "language": t.string().optional(),
                "snapshotId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["snapshotsGet"] = games.get(
        "games/v1/snapshots/{snapshotId}",
        t.struct(
            {
                "language": t.string().optional(),
                "snapshotId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsUnlock"] = games.post(
        "games/v1/achievements/{achievementId}/reveal",
        t.struct(
            {"achievementId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["AchievementRevealResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsSetStepsAtLeast"] = games.post(
        "games/v1/achievements/{achievementId}/reveal",
        t.struct(
            {"achievementId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["AchievementRevealResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsIncrement"] = games.post(
        "games/v1/achievements/{achievementId}/reveal",
        t.struct(
            {"achievementId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["AchievementRevealResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsList"] = games.post(
        "games/v1/achievements/{achievementId}/reveal",
        t.struct(
            {"achievementId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["AchievementRevealResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsUpdateMultiple"] = games.post(
        "games/v1/achievements/{achievementId}/reveal",
        t.struct(
            {"achievementId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["AchievementRevealResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsReveal"] = games.post(
        "games/v1/achievements/{achievementId}/reveal",
        t.struct(
            {"achievementId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["AchievementRevealResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playersList"] = games.get(
        "games/v1/players/me/multipleApplicationPlayerIds",
        t.struct({"applicationIds": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GetMultipleApplicationPlayerIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playersGetScopedPlayerIds"] = games.get(
        "games/v1/players/me/multipleApplicationPlayerIds",
        t.struct({"applicationIds": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GetMultipleApplicationPlayerIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playersGet"] = games.get(
        "games/v1/players/me/multipleApplicationPlayerIds",
        t.struct({"applicationIds": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GetMultipleApplicationPlayerIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playersGetMultipleApplicationPlayerIds"] = games.get(
        "games/v1/players/me/multipleApplicationPlayerIds",
        t.struct({"applicationIds": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GetMultipleApplicationPlayerIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementDefinitionsList"] = games.get(
        "games/v1/achievements",
        t.struct(
            {
                "language": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AchievementDefinitionsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["revisionsCheck"] = games.get(
        "games/v1/revisions/check",
        t.struct(
            {"clientRevision": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["RevisionCheckResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGet"] = games.get(
        "games/v1/stats",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["StatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsListByPlayer"] = games.get(
        "games/v1/eventDefinitions",
        t.struct(
            {
                "language": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventDefinitionListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsRecord"] = games.get(
        "games/v1/eventDefinitions",
        t.struct(
            {
                "language": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventDefinitionListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsListDefinitions"] = games.get(
        "games/v1/eventDefinitions",
        t.struct(
            {
                "language": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventDefinitionListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="games", renames=renames, types=Box(types), functions=Box(functions)
    )
