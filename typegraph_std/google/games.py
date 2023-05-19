from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_games() -> Import:
    games = HTTPRuntime("https://games.googleapis.com/")

    renames = {
        "ErrorResponse": "_games_1_ErrorResponse",
        "AchievementIncrementResponseIn": "_games_2_AchievementIncrementResponseIn",
        "AchievementIncrementResponseOut": "_games_3_AchievementIncrementResponseOut",
        "PlayerLevelIn": "_games_4_PlayerLevelIn",
        "PlayerLevelOut": "_games_5_PlayerLevelOut",
        "ProfileSettingsIn": "_games_6_ProfileSettingsIn",
        "ProfileSettingsOut": "_games_7_ProfileSettingsOut",
        "ApplicationIn": "_games_8_ApplicationIn",
        "ApplicationOut": "_games_9_ApplicationOut",
        "EndPointIn": "_games_10_EndPointIn",
        "EndPointOut": "_games_11_EndPointOut",
        "MetagameConfigIn": "_games_12_MetagameConfigIn",
        "MetagameConfigOut": "_games_13_MetagameConfigOut",
        "EventPeriodRangeIn": "_games_14_EventPeriodRangeIn",
        "EventPeriodRangeOut": "_games_15_EventPeriodRangeOut",
        "ApplicationPlayerIdIn": "_games_16_ApplicationPlayerIdIn",
        "ApplicationPlayerIdOut": "_games_17_ApplicationPlayerIdOut",
        "SnapshotIn": "_games_18_SnapshotIn",
        "SnapshotOut": "_games_19_SnapshotOut",
        "AchievementUpdateMultipleResponseIn": "_games_20_AchievementUpdateMultipleResponseIn",
        "AchievementUpdateMultipleResponseOut": "_games_21_AchievementUpdateMultipleResponseOut",
        "AchievementUpdateMultipleRequestIn": "_games_22_AchievementUpdateMultipleRequestIn",
        "AchievementUpdateMultipleRequestOut": "_games_23_AchievementUpdateMultipleRequestOut",
        "SnapshotListResponseIn": "_games_24_SnapshotListResponseIn",
        "SnapshotListResponseOut": "_games_25_SnapshotListResponseOut",
        "StatsResponseIn": "_games_26_StatsResponseIn",
        "StatsResponseOut": "_games_27_StatsResponseOut",
        "GamesAchievementSetStepsAtLeastIn": "_games_28_GamesAchievementSetStepsAtLeastIn",
        "GamesAchievementSetStepsAtLeastOut": "_games_29_GamesAchievementSetStepsAtLeastOut",
        "EventBatchRecordFailureIn": "_games_30_EventBatchRecordFailureIn",
        "EventBatchRecordFailureOut": "_games_31_EventBatchRecordFailureOut",
        "LeaderboardScoreRankIn": "_games_32_LeaderboardScoreRankIn",
        "LeaderboardScoreRankOut": "_games_33_LeaderboardScoreRankOut",
        "AchievementUpdateRequestIn": "_games_34_AchievementUpdateRequestIn",
        "AchievementUpdateRequestOut": "_games_35_AchievementUpdateRequestOut",
        "AchievementDefinitionIn": "_games_36_AchievementDefinitionIn",
        "AchievementDefinitionOut": "_games_37_AchievementDefinitionOut",
        "ImageAssetIn": "_games_38_ImageAssetIn",
        "ImageAssetOut": "_games_39_ImageAssetOut",
        "PlayerExperienceInfoIn": "_games_40_PlayerExperienceInfoIn",
        "PlayerExperienceInfoOut": "_games_41_PlayerExperienceInfoOut",
        "PlayerScoreIn": "_games_42_PlayerScoreIn",
        "PlayerScoreOut": "_games_43_PlayerScoreOut",
        "AchievementSetStepsAtLeastResponseIn": "_games_44_AchievementSetStepsAtLeastResponseIn",
        "AchievementSetStepsAtLeastResponseOut": "_games_45_AchievementSetStepsAtLeastResponseOut",
        "PlayerEventListResponseIn": "_games_46_PlayerEventListResponseIn",
        "PlayerEventListResponseOut": "_games_47_PlayerEventListResponseOut",
        "AchievementRevealResponseIn": "_games_48_AchievementRevealResponseIn",
        "AchievementRevealResponseOut": "_games_49_AchievementRevealResponseOut",
        "EventDefinitionListResponseIn": "_games_50_EventDefinitionListResponseIn",
        "EventDefinitionListResponseOut": "_games_51_EventDefinitionListResponseOut",
        "PlayerListResponseIn": "_games_52_PlayerListResponseIn",
        "PlayerListResponseOut": "_games_53_PlayerListResponseOut",
        "GetMultipleApplicationPlayerIdsResponseIn": "_games_54_GetMultipleApplicationPlayerIdsResponseIn",
        "GetMultipleApplicationPlayerIdsResponseOut": "_games_55_GetMultipleApplicationPlayerIdsResponseOut",
        "ScopedPlayerIdsIn": "_games_56_ScopedPlayerIdsIn",
        "ScopedPlayerIdsOut": "_games_57_ScopedPlayerIdsOut",
        "EventChildIn": "_games_58_EventChildIn",
        "EventChildOut": "_games_59_EventChildOut",
        "EventRecordRequestIn": "_games_60_EventRecordRequestIn",
        "EventRecordRequestOut": "_games_61_EventRecordRequestOut",
        "PlayerEventIn": "_games_62_PlayerEventIn",
        "PlayerEventOut": "_games_63_PlayerEventOut",
        "AchievementUpdateResponseIn": "_games_64_AchievementUpdateResponseIn",
        "AchievementUpdateResponseOut": "_games_65_AchievementUpdateResponseOut",
        "InstanceAndroidDetailsIn": "_games_66_InstanceAndroidDetailsIn",
        "InstanceAndroidDetailsOut": "_games_67_InstanceAndroidDetailsOut",
        "EventUpdateResponseIn": "_games_68_EventUpdateResponseIn",
        "EventUpdateResponseOut": "_games_69_EventUpdateResponseOut",
        "PlayerLeaderboardScoreIn": "_games_70_PlayerLeaderboardScoreIn",
        "PlayerLeaderboardScoreOut": "_games_71_PlayerLeaderboardScoreOut",
        "PlayerAchievementListResponseIn": "_games_72_PlayerAchievementListResponseIn",
        "PlayerAchievementListResponseOut": "_games_73_PlayerAchievementListResponseOut",
        "PlayerIn": "_games_74_PlayerIn",
        "PlayerOut": "_games_75_PlayerOut",
        "InstanceIn": "_games_76_InstanceIn",
        "InstanceOut": "_games_77_InstanceOut",
        "GamesAchievementIncrementIn": "_games_78_GamesAchievementIncrementIn",
        "GamesAchievementIncrementOut": "_games_79_GamesAchievementIncrementOut",
        "LeaderboardEntryIn": "_games_80_LeaderboardEntryIn",
        "LeaderboardEntryOut": "_games_81_LeaderboardEntryOut",
        "ApplicationCategoryIn": "_games_82_ApplicationCategoryIn",
        "ApplicationCategoryOut": "_games_83_ApplicationCategoryOut",
        "LeaderboardIn": "_games_84_LeaderboardIn",
        "LeaderboardOut": "_games_85_LeaderboardOut",
        "ScoreSubmissionIn": "_games_86_ScoreSubmissionIn",
        "ScoreSubmissionOut": "_games_87_ScoreSubmissionOut",
        "EventRecordFailureIn": "_games_88_EventRecordFailureIn",
        "EventRecordFailureOut": "_games_89_EventRecordFailureOut",
        "PlayerScoreSubmissionListIn": "_games_90_PlayerScoreSubmissionListIn",
        "PlayerScoreSubmissionListOut": "_games_91_PlayerScoreSubmissionListOut",
        "RevisionCheckResponseIn": "_games_92_RevisionCheckResponseIn",
        "RevisionCheckResponseOut": "_games_93_RevisionCheckResponseOut",
        "SnapshotImageIn": "_games_94_SnapshotImageIn",
        "SnapshotImageOut": "_games_95_SnapshotImageOut",
        "EventUpdateRequestIn": "_games_96_EventUpdateRequestIn",
        "EventUpdateRequestOut": "_games_97_EventUpdateRequestOut",
        "EventDefinitionIn": "_games_98_EventDefinitionIn",
        "EventDefinitionOut": "_games_99_EventDefinitionOut",
        "CategoryListResponseIn": "_games_100_CategoryListResponseIn",
        "CategoryListResponseOut": "_games_101_CategoryListResponseOut",
        "LeaderboardListResponseIn": "_games_102_LeaderboardListResponseIn",
        "LeaderboardListResponseOut": "_games_103_LeaderboardListResponseOut",
        "InstanceWebDetailsIn": "_games_104_InstanceWebDetailsIn",
        "InstanceWebDetailsOut": "_games_105_InstanceWebDetailsOut",
        "PlayerLeaderboardScoreListResponseIn": "_games_106_PlayerLeaderboardScoreListResponseIn",
        "PlayerLeaderboardScoreListResponseOut": "_games_107_PlayerLeaderboardScoreListResponseOut",
        "AchievementDefinitionsListResponseIn": "_games_108_AchievementDefinitionsListResponseIn",
        "AchievementDefinitionsListResponseOut": "_games_109_AchievementDefinitionsListResponseOut",
        "ApplicationVerifyResponseIn": "_games_110_ApplicationVerifyResponseIn",
        "ApplicationVerifyResponseOut": "_games_111_ApplicationVerifyResponseOut",
        "PlayerScoreListResponseIn": "_games_112_PlayerScoreListResponseIn",
        "PlayerScoreListResponseOut": "_games_113_PlayerScoreListResponseOut",
        "EventPeriodUpdateIn": "_games_114_EventPeriodUpdateIn",
        "EventPeriodUpdateOut": "_games_115_EventPeriodUpdateOut",
        "PlayerScoreResponseIn": "_games_116_PlayerScoreResponseIn",
        "PlayerScoreResponseOut": "_games_117_PlayerScoreResponseOut",
        "InstanceIosDetailsIn": "_games_118_InstanceIosDetailsIn",
        "InstanceIosDetailsOut": "_games_119_InstanceIosDetailsOut",
        "CategoryIn": "_games_120_CategoryIn",
        "CategoryOut": "_games_121_CategoryOut",
        "AchievementUnlockResponseIn": "_games_122_AchievementUnlockResponseIn",
        "AchievementUnlockResponseOut": "_games_123_AchievementUnlockResponseOut",
        "LeaderboardScoresIn": "_games_124_LeaderboardScoresIn",
        "LeaderboardScoresOut": "_games_125_LeaderboardScoresOut",
        "PlayerAchievementIn": "_games_126_PlayerAchievementIn",
        "PlayerAchievementOut": "_games_127_PlayerAchievementOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["PlayerLevelIn"] = t.struct(
        {
            "level": t.integer().optional(),
            "maxExperiencePoints": t.string().optional(),
            "minExperiencePoints": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PlayerLevelIn"])
    types["PlayerLevelOut"] = t.struct(
        {
            "level": t.integer().optional(),
            "maxExperiencePoints": t.string().optional(),
            "minExperiencePoints": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerLevelOut"])
    types["ProfileSettingsIn"] = t.struct(
        {
            "profileVisible": t.boolean().optional(),
            "kind": t.string().optional(),
            "friendsListVisibility": t.string(),
        }
    ).named(renames["ProfileSettingsIn"])
    types["ProfileSettingsOut"] = t.struct(
        {
            "profileVisible": t.boolean().optional(),
            "kind": t.string().optional(),
            "friendsListVisibility": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileSettingsOut"])
    types["ApplicationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "category": t.proxy(renames["ApplicationCategoryIn"]).optional(),
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
            "enabledFeatures": t.array(t.string()).optional(),
            "themeColor": t.string().optional(),
            "id": t.string().optional(),
            "author": t.string().optional(),
            "description": t.string().optional(),
            "leaderboard_count": t.integer().optional(),
            "lastUpdatedTimestamp": t.string().optional(),
            "assets": t.array(t.proxy(renames["ImageAssetIn"])).optional(),
            "achievement_count": t.integer().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ApplicationIn"])
    types["ApplicationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "category": t.proxy(renames["ApplicationCategoryOut"]).optional(),
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "enabledFeatures": t.array(t.string()).optional(),
            "themeColor": t.string().optional(),
            "id": t.string().optional(),
            "author": t.string().optional(),
            "description": t.string().optional(),
            "leaderboard_count": t.integer().optional(),
            "lastUpdatedTimestamp": t.string().optional(),
            "assets": t.array(t.proxy(renames["ImageAssetOut"])).optional(),
            "achievement_count": t.integer().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationOut"])
    types["EndPointIn"] = t.struct({"url": t.string().optional()}).named(
        renames["EndPointIn"]
    )
    types["EndPointOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndPointOut"])
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
    types["EventPeriodRangeIn"] = t.struct(
        {
            "periodEndMillis": t.string().optional(),
            "kind": t.string().optional(),
            "periodStartMillis": t.string().optional(),
        }
    ).named(renames["EventPeriodRangeIn"])
    types["EventPeriodRangeOut"] = t.struct(
        {
            "periodEndMillis": t.string().optional(),
            "kind": t.string().optional(),
            "periodStartMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventPeriodRangeOut"])
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
    types["SnapshotIn"] = t.struct(
        {
            "id": t.string().optional(),
            "type": t.string().optional(),
            "title": t.string().optional(),
            "uniqueName": t.string().optional(),
            "durationMillis": t.string().optional(),
            "lastModifiedMillis": t.string().optional(),
            "driveId": t.string().optional(),
            "coverImage": t.proxy(renames["SnapshotImageIn"]).optional(),
            "description": t.string().optional(),
            "progressValue": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SnapshotIn"])
    types["SnapshotOut"] = t.struct(
        {
            "id": t.string().optional(),
            "type": t.string().optional(),
            "title": t.string().optional(),
            "uniqueName": t.string().optional(),
            "durationMillis": t.string().optional(),
            "lastModifiedMillis": t.string().optional(),
            "driveId": t.string().optional(),
            "coverImage": t.proxy(renames["SnapshotImageOut"]).optional(),
            "description": t.string().optional(),
            "progressValue": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotOut"])
    types["AchievementUpdateMultipleResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "updatedAchievements": t.array(
                t.proxy(renames["AchievementUpdateResponseIn"])
            ).optional(),
        }
    ).named(renames["AchievementUpdateMultipleResponseIn"])
    types["AchievementUpdateMultipleResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "updatedAchievements": t.array(
                t.proxy(renames["AchievementUpdateResponseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementUpdateMultipleResponseOut"])
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
    types["SnapshotListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["SnapshotIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SnapshotListResponseIn"])
    types["SnapshotListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["SnapshotOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotListResponseOut"])
    types["StatsResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "churn_probability": t.number().optional(),
            "spend_probability": t.number().optional(),
            "days_since_last_played": t.integer().optional(),
            "avg_session_length_minutes": t.number().optional(),
            "high_spender_probability": t.number().optional(),
            "num_purchases": t.integer().optional(),
            "spend_percentile": t.number().optional(),
            "num_sessions": t.integer().optional(),
            "total_spend_next_28_days": t.number().optional(),
            "num_sessions_percentile": t.number().optional(),
        }
    ).named(renames["StatsResponseIn"])
    types["StatsResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "churn_probability": t.number().optional(),
            "spend_probability": t.number().optional(),
            "days_since_last_played": t.integer().optional(),
            "avg_session_length_minutes": t.number().optional(),
            "high_spender_probability": t.number().optional(),
            "num_purchases": t.integer().optional(),
            "spend_percentile": t.number().optional(),
            "num_sessions": t.integer().optional(),
            "total_spend_next_28_days": t.number().optional(),
            "num_sessions_percentile": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatsResponseOut"])
    types["GamesAchievementSetStepsAtLeastIn"] = t.struct(
        {"steps": t.integer().optional(), "kind": t.string().optional()}
    ).named(renames["GamesAchievementSetStepsAtLeastIn"])
    types["GamesAchievementSetStepsAtLeastOut"] = t.struct(
        {
            "steps": t.integer().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GamesAchievementSetStepsAtLeastOut"])
    types["EventBatchRecordFailureIn"] = t.struct(
        {
            "failureCause": t.string().optional(),
            "kind": t.string().optional(),
            "range": t.proxy(renames["EventPeriodRangeIn"]).optional(),
        }
    ).named(renames["EventBatchRecordFailureIn"])
    types["EventBatchRecordFailureOut"] = t.struct(
        {
            "failureCause": t.string().optional(),
            "kind": t.string().optional(),
            "range": t.proxy(renames["EventPeriodRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventBatchRecordFailureOut"])
    types["LeaderboardScoreRankIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "rank": t.string().optional(),
            "formattedNumScores": t.string().optional(),
            "formattedRank": t.string().optional(),
            "numScores": t.string().optional(),
        }
    ).named(renames["LeaderboardScoreRankIn"])
    types["LeaderboardScoreRankOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "rank": t.string().optional(),
            "formattedNumScores": t.string().optional(),
            "formattedRank": t.string().optional(),
            "numScores": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaderboardScoreRankOut"])
    types["AchievementUpdateRequestIn"] = t.struct(
        {
            "setStepsAtLeastPayload": t.proxy(
                renames["GamesAchievementSetStepsAtLeastIn"]
            ).optional(),
            "achievementId": t.string().optional(),
            "incrementPayload": t.proxy(
                renames["GamesAchievementIncrementIn"]
            ).optional(),
            "kind": t.string().optional(),
            "updateType": t.string().optional(),
        }
    ).named(renames["AchievementUpdateRequestIn"])
    types["AchievementUpdateRequestOut"] = t.struct(
        {
            "setStepsAtLeastPayload": t.proxy(
                renames["GamesAchievementSetStepsAtLeastOut"]
            ).optional(),
            "achievementId": t.string().optional(),
            "incrementPayload": t.proxy(
                renames["GamesAchievementIncrementOut"]
            ).optional(),
            "kind": t.string().optional(),
            "updateType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementUpdateRequestOut"])
    types["AchievementDefinitionIn"] = t.struct(
        {
            "achievementType": t.string().optional(),
            "isUnlockedIconUrlDefault": t.boolean().optional(),
            "unlockedIconUrl": t.string().optional(),
            "totalSteps": t.integer().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "formattedTotalSteps": t.string().optional(),
            "revealedIconUrl": t.string().optional(),
            "experiencePoints": t.string().optional(),
            "description": t.string().optional(),
            "initialState": t.string().optional(),
            "isRevealedIconUrlDefault": t.boolean().optional(),
        }
    ).named(renames["AchievementDefinitionIn"])
    types["AchievementDefinitionOut"] = t.struct(
        {
            "achievementType": t.string().optional(),
            "isUnlockedIconUrlDefault": t.boolean().optional(),
            "unlockedIconUrl": t.string().optional(),
            "totalSteps": t.integer().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "formattedTotalSteps": t.string().optional(),
            "revealedIconUrl": t.string().optional(),
            "experiencePoints": t.string().optional(),
            "description": t.string().optional(),
            "initialState": t.string().optional(),
            "isRevealedIconUrlDefault": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementDefinitionOut"])
    types["ImageAssetIn"] = t.struct(
        {
            "width": t.integer().optional(),
            "url": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "height": t.integer().optional(),
        }
    ).named(renames["ImageAssetIn"])
    types["ImageAssetOut"] = t.struct(
        {
            "width": t.integer().optional(),
            "url": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "height": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageAssetOut"])
    types["PlayerExperienceInfoIn"] = t.struct(
        {
            "currentExperiencePoints": t.string().optional(),
            "nextLevel": t.proxy(renames["PlayerLevelIn"]).optional(),
            "kind": t.string().optional(),
            "lastLevelUpTimestampMillis": t.string().optional(),
            "currentLevel": t.proxy(renames["PlayerLevelIn"]).optional(),
        }
    ).named(renames["PlayerExperienceInfoIn"])
    types["PlayerExperienceInfoOut"] = t.struct(
        {
            "currentExperiencePoints": t.string().optional(),
            "nextLevel": t.proxy(renames["PlayerLevelOut"]).optional(),
            "kind": t.string().optional(),
            "lastLevelUpTimestampMillis": t.string().optional(),
            "currentLevel": t.proxy(renames["PlayerLevelOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerExperienceInfoOut"])
    types["PlayerScoreIn"] = t.struct(
        {
            "scoreTag": t.string().optional(),
            "timeSpan": t.string().optional(),
            "kind": t.string().optional(),
            "score": t.string().optional(),
            "formattedScore": t.string().optional(),
        }
    ).named(renames["PlayerScoreIn"])
    types["PlayerScoreOut"] = t.struct(
        {
            "scoreTag": t.string().optional(),
            "timeSpan": t.string().optional(),
            "kind": t.string().optional(),
            "score": t.string().optional(),
            "formattedScore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerScoreOut"])
    types["AchievementSetStepsAtLeastResponseIn"] = t.struct(
        {
            "newlyUnlocked": t.boolean().optional(),
            "kind": t.string().optional(),
            "currentSteps": t.integer().optional(),
        }
    ).named(renames["AchievementSetStepsAtLeastResponseIn"])
    types["AchievementSetStepsAtLeastResponseOut"] = t.struct(
        {
            "newlyUnlocked": t.boolean().optional(),
            "kind": t.string().optional(),
            "currentSteps": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementSetStepsAtLeastResponseOut"])
    types["PlayerEventListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["PlayerEventIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PlayerEventListResponseIn"])
    types["PlayerEventListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["PlayerEventOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerEventListResponseOut"])
    types["AchievementRevealResponseIn"] = t.struct(
        {"currentState": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["AchievementRevealResponseIn"])
    types["AchievementRevealResponseOut"] = t.struct(
        {
            "currentState": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementRevealResponseOut"])
    types["EventDefinitionListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["EventDefinitionIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["EventDefinitionListResponseIn"])
    types["EventDefinitionListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["EventDefinitionOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventDefinitionListResponseOut"])
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
    types["GetMultipleApplicationPlayerIdsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GetMultipleApplicationPlayerIdsResponseIn"])
    types["GetMultipleApplicationPlayerIdsResponseOut"] = t.struct(
        {
            "playerIds": t.array(t.proxy(renames["ApplicationPlayerIdOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetMultipleApplicationPlayerIdsResponseOut"])
    types["ScopedPlayerIdsIn"] = t.struct(
        {
            "developerPlayerKey": t.string().optional(),
            "gamePlayerId": t.string().optional(),
        }
    ).named(renames["ScopedPlayerIdsIn"])
    types["ScopedPlayerIdsOut"] = t.struct(
        {
            "developerPlayerKey": t.string().optional(),
            "gamePlayerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScopedPlayerIdsOut"])
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
    types["EventRecordRequestIn"] = t.struct(
        {
            "timePeriods": t.array(t.proxy(renames["EventPeriodUpdateIn"])).optional(),
            "currentTimeMillis": t.string().optional(),
            "kind": t.string().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["EventRecordRequestIn"])
    types["EventRecordRequestOut"] = t.struct(
        {
            "timePeriods": t.array(t.proxy(renames["EventPeriodUpdateOut"])).optional(),
            "currentTimeMillis": t.string().optional(),
            "kind": t.string().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventRecordRequestOut"])
    types["PlayerEventIn"] = t.struct(
        {
            "numEvents": t.string().optional(),
            "kind": t.string().optional(),
            "playerId": t.string().optional(),
            "definitionId": t.string().optional(),
            "formattedNumEvents": t.string().optional(),
        }
    ).named(renames["PlayerEventIn"])
    types["PlayerEventOut"] = t.struct(
        {
            "numEvents": t.string().optional(),
            "kind": t.string().optional(),
            "playerId": t.string().optional(),
            "definitionId": t.string().optional(),
            "formattedNumEvents": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerEventOut"])
    types["AchievementUpdateResponseIn"] = t.struct(
        {
            "newlyUnlocked": t.boolean().optional(),
            "currentState": t.string().optional(),
            "achievementId": t.string().optional(),
            "kind": t.string().optional(),
            "currentSteps": t.integer().optional(),
            "updateOccurred": t.boolean().optional(),
        }
    ).named(renames["AchievementUpdateResponseIn"])
    types["AchievementUpdateResponseOut"] = t.struct(
        {
            "newlyUnlocked": t.boolean().optional(),
            "currentState": t.string().optional(),
            "achievementId": t.string().optional(),
            "kind": t.string().optional(),
            "currentSteps": t.integer().optional(),
            "updateOccurred": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementUpdateResponseOut"])
    types["InstanceAndroidDetailsIn"] = t.struct(
        {
            "enablePiracyCheck": t.boolean().optional(),
            "packageName": t.string().optional(),
            "preferred": t.boolean().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["InstanceAndroidDetailsIn"])
    types["InstanceAndroidDetailsOut"] = t.struct(
        {
            "enablePiracyCheck": t.boolean().optional(),
            "packageName": t.string().optional(),
            "preferred": t.boolean().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceAndroidDetailsOut"])
    types["EventUpdateResponseIn"] = t.struct(
        {
            "playerEvents": t.array(t.proxy(renames["PlayerEventIn"])).optional(),
            "kind": t.string().optional(),
            "batchFailures": t.array(
                t.proxy(renames["EventBatchRecordFailureIn"])
            ).optional(),
            "eventFailures": t.array(
                t.proxy(renames["EventRecordFailureIn"])
            ).optional(),
        }
    ).named(renames["EventUpdateResponseIn"])
    types["EventUpdateResponseOut"] = t.struct(
        {
            "playerEvents": t.array(t.proxy(renames["PlayerEventOut"])).optional(),
            "kind": t.string().optional(),
            "batchFailures": t.array(
                t.proxy(renames["EventBatchRecordFailureOut"])
            ).optional(),
            "eventFailures": t.array(
                t.proxy(renames["EventRecordFailureOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventUpdateResponseOut"])
    types["PlayerLeaderboardScoreIn"] = t.struct(
        {
            "publicRank": t.proxy(renames["LeaderboardScoreRankIn"]).optional(),
            "kind": t.string().optional(),
            "socialRank": t.proxy(renames["LeaderboardScoreRankIn"]).optional(),
            "scoreTag": t.string().optional(),
            "friendsRank": t.proxy(renames["LeaderboardScoreRankIn"]).optional(),
            "timeSpan": t.string().optional(),
            "writeTimestamp": t.string().optional(),
            "scoreValue": t.string().optional(),
            "scoreString": t.string().optional(),
            "leaderboard_id": t.string().optional(),
        }
    ).named(renames["PlayerLeaderboardScoreIn"])
    types["PlayerLeaderboardScoreOut"] = t.struct(
        {
            "publicRank": t.proxy(renames["LeaderboardScoreRankOut"]).optional(),
            "kind": t.string().optional(),
            "socialRank": t.proxy(renames["LeaderboardScoreRankOut"]).optional(),
            "scoreTag": t.string().optional(),
            "friendsRank": t.proxy(renames["LeaderboardScoreRankOut"]).optional(),
            "timeSpan": t.string().optional(),
            "writeTimestamp": t.string().optional(),
            "scoreValue": t.string().optional(),
            "scoreString": t.string().optional(),
            "leaderboard_id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerLeaderboardScoreOut"])
    types["PlayerAchievementListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["PlayerAchievementIn"])).optional(),
        }
    ).named(renames["PlayerAchievementListResponseIn"])
    types["PlayerAchievementListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["PlayerAchievementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerAchievementListResponseOut"])
    types["PlayerIn"] = t.struct(
        {
            "gamePlayerId": t.string().optional(),
            "experienceInfo": t.proxy(renames["PlayerExperienceInfoIn"]).optional(),
            "bannerUrlPortrait": t.string().optional(),
            "kind": t.string().optional(),
            "friendStatus": t.string().optional(),
            "name": t.struct(
                {
                    "givenName": t.string().optional(),
                    "familyName": t.string().optional(),
                }
            ).optional(),
            "displayName": t.string().optional(),
            "profileSettings": t.proxy(renames["ProfileSettingsIn"]).optional(),
            "originalPlayerId": t.string().optional(),
            "avatarImageUrl": t.string().optional(),
            "title": t.string().optional(),
            "playerId": t.string().optional(),
            "bannerUrlLandscape": t.string().optional(),
        }
    ).named(renames["PlayerIn"])
    types["PlayerOut"] = t.struct(
        {
            "gamePlayerId": t.string().optional(),
            "experienceInfo": t.proxy(renames["PlayerExperienceInfoOut"]).optional(),
            "bannerUrlPortrait": t.string().optional(),
            "kind": t.string().optional(),
            "friendStatus": t.string().optional(),
            "name": t.struct(
                {
                    "givenName": t.string().optional(),
                    "familyName": t.string().optional(),
                }
            ).optional(),
            "displayName": t.string().optional(),
            "profileSettings": t.proxy(renames["ProfileSettingsOut"]).optional(),
            "originalPlayerId": t.string().optional(),
            "avatarImageUrl": t.string().optional(),
            "title": t.string().optional(),
            "playerId": t.string().optional(),
            "bannerUrlLandscape": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerOut"])
    types["InstanceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "androidInstance": t.proxy(renames["InstanceAndroidDetailsIn"]).optional(),
            "webInstance": t.proxy(renames["InstanceWebDetailsIn"]).optional(),
            "acquisitionUri": t.string().optional(),
            "platformType": t.string().optional(),
            "realtimePlay": t.boolean().optional(),
            "turnBasedPlay": t.boolean().optional(),
            "iosInstance": t.proxy(renames["InstanceIosDetailsIn"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "androidInstance": t.proxy(renames["InstanceAndroidDetailsOut"]).optional(),
            "webInstance": t.proxy(renames["InstanceWebDetailsOut"]).optional(),
            "acquisitionUri": t.string().optional(),
            "platformType": t.string().optional(),
            "realtimePlay": t.boolean().optional(),
            "turnBasedPlay": t.boolean().optional(),
            "iosInstance": t.proxy(renames["InstanceIosDetailsOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["GamesAchievementIncrementIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "steps": t.integer().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["GamesAchievementIncrementIn"])
    types["GamesAchievementIncrementOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "steps": t.integer().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GamesAchievementIncrementOut"])
    types["LeaderboardEntryIn"] = t.struct(
        {
            "writeTimestampMillis": t.string().optional(),
            "player": t.proxy(renames["PlayerIn"]).optional(),
            "formattedScore": t.string().optional(),
            "scoreRank": t.string().optional(),
            "scoreValue": t.string().optional(),
            "timeSpan": t.string().optional(),
            "kind": t.string().optional(),
            "formattedScoreRank": t.string().optional(),
            "scoreTag": t.string().optional(),
        }
    ).named(renames["LeaderboardEntryIn"])
    types["LeaderboardEntryOut"] = t.struct(
        {
            "writeTimestampMillis": t.string().optional(),
            "player": t.proxy(renames["PlayerOut"]).optional(),
            "formattedScore": t.string().optional(),
            "scoreRank": t.string().optional(),
            "scoreValue": t.string().optional(),
            "timeSpan": t.string().optional(),
            "kind": t.string().optional(),
            "formattedScoreRank": t.string().optional(),
            "scoreTag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaderboardEntryOut"])
    types["ApplicationCategoryIn"] = t.struct(
        {
            "secondary": t.string().optional(),
            "primary": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ApplicationCategoryIn"])
    types["ApplicationCategoryOut"] = t.struct(
        {
            "secondary": t.string().optional(),
            "primary": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationCategoryOut"])
    types["LeaderboardIn"] = t.struct(
        {
            "isIconUrlDefault": t.boolean().optional(),
            "id": t.string().optional(),
            "iconUrl": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "order": t.string().optional(),
        }
    ).named(renames["LeaderboardIn"])
    types["LeaderboardOut"] = t.struct(
        {
            "isIconUrlDefault": t.boolean().optional(),
            "id": t.string().optional(),
            "iconUrl": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "order": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaderboardOut"])
    types["ScoreSubmissionIn"] = t.struct(
        {
            "score": t.string().optional(),
            "scoreTag": t.string().optional(),
            "leaderboardId": t.string().optional(),
            "signature": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ScoreSubmissionIn"])
    types["ScoreSubmissionOut"] = t.struct(
        {
            "score": t.string().optional(),
            "scoreTag": t.string().optional(),
            "leaderboardId": t.string().optional(),
            "signature": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScoreSubmissionOut"])
    types["EventRecordFailureIn"] = t.struct(
        {
            "eventId": t.string().optional(),
            "kind": t.string().optional(),
            "failureCause": t.string().optional(),
        }
    ).named(renames["EventRecordFailureIn"])
    types["EventRecordFailureOut"] = t.struct(
        {
            "eventId": t.string().optional(),
            "kind": t.string().optional(),
            "failureCause": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventRecordFailureOut"])
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
    types["RevisionCheckResponseIn"] = t.struct(
        {
            "revisionStatus": t.string().optional(),
            "kind": t.string().optional(),
            "apiVersion": t.string().optional(),
        }
    ).named(renames["RevisionCheckResponseIn"])
    types["RevisionCheckResponseOut"] = t.struct(
        {
            "revisionStatus": t.string().optional(),
            "kind": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevisionCheckResponseOut"])
    types["SnapshotImageIn"] = t.struct(
        {
            "height": t.integer().optional(),
            "url": t.string().optional(),
            "kind": t.string().optional(),
            "mime_type": t.string().optional(),
            "width": t.integer().optional(),
        }
    ).named(renames["SnapshotImageIn"])
    types["SnapshotImageOut"] = t.struct(
        {
            "height": t.integer().optional(),
            "url": t.string().optional(),
            "kind": t.string().optional(),
            "mime_type": t.string().optional(),
            "width": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotImageOut"])
    types["EventUpdateRequestIn"] = t.struct(
        {
            "updateCount": t.string().optional(),
            "kind": t.string().optional(),
            "definitionId": t.string().optional(),
        }
    ).named(renames["EventUpdateRequestIn"])
    types["EventUpdateRequestOut"] = t.struct(
        {
            "updateCount": t.string().optional(),
            "kind": t.string().optional(),
            "definitionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventUpdateRequestOut"])
    types["EventDefinitionIn"] = t.struct(
        {
            "visibility": t.string().optional(),
            "isDefaultImageUrl": t.boolean().optional(),
            "kind": t.string().optional(),
            "childEvents": t.array(t.proxy(renames["EventChildIn"])).optional(),
            "id": t.string().optional(),
            "imageUrl": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["EventDefinitionIn"])
    types["EventDefinitionOut"] = t.struct(
        {
            "visibility": t.string().optional(),
            "isDefaultImageUrl": t.boolean().optional(),
            "kind": t.string().optional(),
            "childEvents": t.array(t.proxy(renames["EventChildOut"])).optional(),
            "id": t.string().optional(),
            "imageUrl": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventDefinitionOut"])
    types["CategoryListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["CategoryIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["CategoryListResponseIn"])
    types["CategoryListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryListResponseOut"])
    types["LeaderboardListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["LeaderboardIn"])).optional(),
        }
    ).named(renames["LeaderboardListResponseIn"])
    types["LeaderboardListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["LeaderboardOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaderboardListResponseOut"])
    types["InstanceWebDetailsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "preferred": t.boolean().optional(),
            "launchUrl": t.string().optional(),
        }
    ).named(renames["InstanceWebDetailsIn"])
    types["InstanceWebDetailsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "preferred": t.boolean().optional(),
            "launchUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceWebDetailsOut"])
    types["PlayerLeaderboardScoreListResponseIn"] = t.struct(
        {
            "player": t.proxy(renames["PlayerIn"]).optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["PlayerLeaderboardScoreIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["PlayerLeaderboardScoreListResponseIn"])
    types["PlayerLeaderboardScoreListResponseOut"] = t.struct(
        {
            "player": t.proxy(renames["PlayerOut"]).optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["PlayerLeaderboardScoreOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerLeaderboardScoreListResponseOut"])
    types["AchievementDefinitionsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["AchievementDefinitionIn"])).optional(),
        }
    ).named(renames["AchievementDefinitionsListResponseIn"])
    types["AchievementDefinitionsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["AchievementDefinitionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementDefinitionsListResponseOut"])
    types["ApplicationVerifyResponseIn"] = t.struct(
        {
            "alternate_player_id": t.string().optional(),
            "player_id": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ApplicationVerifyResponseIn"])
    types["ApplicationVerifyResponseOut"] = t.struct(
        {
            "alternate_player_id": t.string().optional(),
            "player_id": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationVerifyResponseOut"])
    types["PlayerScoreListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "submittedScores": t.array(
                t.proxy(renames["PlayerScoreResponseIn"])
            ).optional(),
        }
    ).named(renames["PlayerScoreListResponseIn"])
    types["PlayerScoreListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "submittedScores": t.array(
                t.proxy(renames["PlayerScoreResponseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerScoreListResponseOut"])
    types["EventPeriodUpdateIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "timePeriod": t.proxy(renames["EventPeriodRangeIn"]).optional(),
            "updates": t.array(t.proxy(renames["EventUpdateRequestIn"])).optional(),
        }
    ).named(renames["EventPeriodUpdateIn"])
    types["EventPeriodUpdateOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "timePeriod": t.proxy(renames["EventPeriodRangeOut"]).optional(),
            "updates": t.array(t.proxy(renames["EventUpdateRequestOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventPeriodUpdateOut"])
    types["PlayerScoreResponseIn"] = t.struct(
        {
            "leaderboardId": t.string().optional(),
            "unbeatenScores": t.array(t.proxy(renames["PlayerScoreIn"])).optional(),
            "beatenScoreTimeSpans": t.array(t.string()).optional(),
            "scoreTag": t.string().optional(),
            "formattedScore": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PlayerScoreResponseIn"])
    types["PlayerScoreResponseOut"] = t.struct(
        {
            "leaderboardId": t.string().optional(),
            "unbeatenScores": t.array(t.proxy(renames["PlayerScoreOut"])).optional(),
            "beatenScoreTimeSpans": t.array(t.string()).optional(),
            "scoreTag": t.string().optional(),
            "formattedScore": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerScoreResponseOut"])
    types["InstanceIosDetailsIn"] = t.struct(
        {
            "supportIphone": t.boolean().optional(),
            "bundleIdentifier": t.string().optional(),
            "itunesAppId": t.string().optional(),
            "kind": t.string().optional(),
            "preferredForIpad": t.boolean().optional(),
            "supportIpad": t.boolean().optional(),
            "preferredForIphone": t.boolean().optional(),
        }
    ).named(renames["InstanceIosDetailsIn"])
    types["InstanceIosDetailsOut"] = t.struct(
        {
            "supportIphone": t.boolean().optional(),
            "bundleIdentifier": t.string().optional(),
            "itunesAppId": t.string().optional(),
            "kind": t.string().optional(),
            "preferredForIpad": t.boolean().optional(),
            "supportIpad": t.boolean().optional(),
            "preferredForIphone": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceIosDetailsOut"])
    types["CategoryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "experiencePoints": t.string().optional(),
            "category": t.string().optional(),
        }
    ).named(renames["CategoryIn"])
    types["CategoryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "experiencePoints": t.string().optional(),
            "category": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryOut"])
    types["AchievementUnlockResponseIn"] = t.struct(
        {"kind": t.string().optional(), "newlyUnlocked": t.boolean().optional()}
    ).named(renames["AchievementUnlockResponseIn"])
    types["AchievementUnlockResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "newlyUnlocked": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementUnlockResponseOut"])
    types["LeaderboardScoresIn"] = t.struct(
        {
            "playerScore": t.proxy(renames["LeaderboardEntryIn"]).optional(),
            "nextPageToken": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "numScores": t.string().optional(),
            "items": t.array(t.proxy(renames["LeaderboardEntryIn"])).optional(),
        }
    ).named(renames["LeaderboardScoresIn"])
    types["LeaderboardScoresOut"] = t.struct(
        {
            "playerScore": t.proxy(renames["LeaderboardEntryOut"]).optional(),
            "nextPageToken": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "numScores": t.string().optional(),
            "items": t.array(t.proxy(renames["LeaderboardEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaderboardScoresOut"])
    types["PlayerAchievementIn"] = t.struct(
        {
            "experiencePoints": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "lastUpdatedTimestamp": t.string().optional(),
            "formattedCurrentStepsString": t.string().optional(),
            "currentSteps": t.integer().optional(),
            "achievementState": t.string().optional(),
        }
    ).named(renames["PlayerAchievementIn"])
    types["PlayerAchievementOut"] = t.struct(
        {
            "experiencePoints": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "lastUpdatedTimestamp": t.string().optional(),
            "formattedCurrentStepsString": t.string().optional(),
            "currentSteps": t.integer().optional(),
            "achievementState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerAchievementOut"])

    functions = {}
    functions["achievementsUnlock"] = games.post(
        "games/v1/achievements/updateMultiple",
        t.struct(
            {
                "updates": t.array(
                    t.proxy(renames["AchievementUpdateRequestIn"])
                ).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AchievementUpdateMultipleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsList"] = games.post(
        "games/v1/achievements/updateMultiple",
        t.struct(
            {
                "updates": t.array(
                    t.proxy(renames["AchievementUpdateRequestIn"])
                ).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AchievementUpdateMultipleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsReveal"] = games.post(
        "games/v1/achievements/updateMultiple",
        t.struct(
            {
                "updates": t.array(
                    t.proxy(renames["AchievementUpdateRequestIn"])
                ).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AchievementUpdateMultipleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsIncrement"] = games.post(
        "games/v1/achievements/updateMultiple",
        t.struct(
            {
                "updates": t.array(
                    t.proxy(renames["AchievementUpdateRequestIn"])
                ).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AchievementUpdateMultipleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsSetStepsAtLeast"] = games.post(
        "games/v1/achievements/updateMultiple",
        t.struct(
            {
                "updates": t.array(
                    t.proxy(renames["AchievementUpdateRequestIn"])
                ).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AchievementUpdateMultipleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsUpdateMultiple"] = games.post(
        "games/v1/achievements/updateMultiple",
        t.struct(
            {
                "updates": t.array(
                    t.proxy(renames["AchievementUpdateRequestIn"])
                ).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AchievementUpdateMultipleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["leaderboardsGet"] = games.get(
        "games/v1/leaderboards",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "language": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["leaderboardsList"] = games.get(
        "games/v1/leaderboards",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "language": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardListResponseOut"]),
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
    functions["applicationsGetEndPoint"] = games.get(
        "games/v1/applications/{applicationId}",
        t.struct(
            {
                "platformType": t.string().optional(),
                "applicationId": t.string().optional(),
                "language": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApplicationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["applicationsPlayed"] = games.get(
        "games/v1/applications/{applicationId}",
        t.struct(
            {
                "platformType": t.string().optional(),
                "applicationId": t.string().optional(),
                "language": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApplicationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["applicationsVerify"] = games.get(
        "games/v1/applications/{applicationId}",
        t.struct(
            {
                "platformType": t.string().optional(),
                "applicationId": t.string().optional(),
                "language": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApplicationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["applicationsGet"] = games.get(
        "games/v1/applications/{applicationId}",
        t.struct(
            {
                "platformType": t.string().optional(),
                "applicationId": t.string().optional(),
                "language": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApplicationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["snapshotsGet"] = games.get(
        "games/v1/players/{playerId}/snapshots",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "language": t.string().optional(),
                "pageToken": t.string().optional(),
                "playerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["snapshotsList"] = games.get(
        "games/v1/players/{playerId}/snapshots",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "language": t.string().optional(),
                "pageToken": t.string().optional(),
                "playerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playersGet"] = games.get(
        "games/v1/players/me/players/{collection}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "language": t.string().optional(),
                "collection": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlayerListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playersGetMultipleApplicationPlayerIds"] = games.get(
        "games/v1/players/me/players/{collection}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "language": t.string().optional(),
                "collection": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlayerListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playersGetScopedPlayerIds"] = games.get(
        "games/v1/players/me/players/{collection}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "language": t.string().optional(),
                "collection": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlayerListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playersList"] = games.get(
        "games/v1/players/me/players/{collection}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "language": t.string().optional(),
                "collection": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PlayerListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["metagameGetMetagameConfig"] = games.get(
        "games/v1/players/{playerId}/categories/{collection}",
        t.struct(
            {
                "playerId": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "language": t.string().optional(),
                "collection": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CategoryListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["metagameListCategoriesByPlayer"] = games.get(
        "games/v1/players/{playerId}/categories/{collection}",
        t.struct(
            {
                "playerId": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "language": t.string().optional(),
                "collection": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CategoryListResponseOut"]),
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
    functions["achievementDefinitionsList"] = games.get(
        "games/v1/achievements",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "language": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AchievementDefinitionsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsListDefinitions"] = games.post(
        "games/v1/events",
        t.struct(
            {
                "language": t.string().optional(),
                "timePeriods": t.array(
                    t.proxy(renames["EventPeriodUpdateIn"])
                ).optional(),
                "currentTimeMillis": t.string().optional(),
                "kind": t.string().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventUpdateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsListByPlayer"] = games.post(
        "games/v1/events",
        t.struct(
            {
                "language": t.string().optional(),
                "timePeriods": t.array(
                    t.proxy(renames["EventPeriodUpdateIn"])
                ).optional(),
                "currentTimeMillis": t.string().optional(),
                "kind": t.string().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventUpdateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsRecord"] = games.post(
        "games/v1/events",
        t.struct(
            {
                "language": t.string().optional(),
                "timePeriods": t.array(
                    t.proxy(renames["EventPeriodUpdateIn"])
                ).optional(),
                "currentTimeMillis": t.string().optional(),
                "kind": t.string().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventUpdateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresList"] = games.get(
        "games/v1/leaderboards/{leaderboardId}/window/{collection}",
        t.struct(
            {
                "collection": t.string().optional(),
                "returnTopIfAbsent": t.boolean().optional(),
                "leaderboardId": t.string().optional(),
                "pageToken": t.string().optional(),
                "timeSpan": t.string().optional(),
                "language": t.string().optional(),
                "maxResults": t.integer().optional(),
                "resultsAbove": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardScoresOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresSubmit"] = games.get(
        "games/v1/leaderboards/{leaderboardId}/window/{collection}",
        t.struct(
            {
                "collection": t.string().optional(),
                "returnTopIfAbsent": t.boolean().optional(),
                "leaderboardId": t.string().optional(),
                "pageToken": t.string().optional(),
                "timeSpan": t.string().optional(),
                "language": t.string().optional(),
                "maxResults": t.integer().optional(),
                "resultsAbove": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardScoresOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresSubmitMultiple"] = games.get(
        "games/v1/leaderboards/{leaderboardId}/window/{collection}",
        t.struct(
            {
                "collection": t.string().optional(),
                "returnTopIfAbsent": t.boolean().optional(),
                "leaderboardId": t.string().optional(),
                "pageToken": t.string().optional(),
                "timeSpan": t.string().optional(),
                "language": t.string().optional(),
                "maxResults": t.integer().optional(),
                "resultsAbove": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardScoresOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresGet"] = games.get(
        "games/v1/leaderboards/{leaderboardId}/window/{collection}",
        t.struct(
            {
                "collection": t.string().optional(),
                "returnTopIfAbsent": t.boolean().optional(),
                "leaderboardId": t.string().optional(),
                "pageToken": t.string().optional(),
                "timeSpan": t.string().optional(),
                "language": t.string().optional(),
                "maxResults": t.integer().optional(),
                "resultsAbove": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardScoresOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresListWindow"] = games.get(
        "games/v1/leaderboards/{leaderboardId}/window/{collection}",
        t.struct(
            {
                "collection": t.string().optional(),
                "returnTopIfAbsent": t.boolean().optional(),
                "leaderboardId": t.string().optional(),
                "pageToken": t.string().optional(),
                "timeSpan": t.string().optional(),
                "language": t.string().optional(),
                "maxResults": t.integer().optional(),
                "resultsAbove": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardScoresOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="games", renames=renames, types=Box(types), functions=Box(functions)
    )
