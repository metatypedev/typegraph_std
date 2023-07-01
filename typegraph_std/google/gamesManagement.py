from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_gamesManagement():
    gamesManagement = HTTPRuntime("https://gamesmanagement.googleapis.com/")

    renames = {
        "ErrorResponse": "_gamesManagement_1_ErrorResponse",
        "PlayerIn": "_gamesManagement_2_PlayerIn",
        "PlayerOut": "_gamesManagement_3_PlayerOut",
        "AchievementResetMultipleForAllRequestIn": "_gamesManagement_4_AchievementResetMultipleForAllRequestIn",
        "AchievementResetMultipleForAllRequestOut": "_gamesManagement_5_AchievementResetMultipleForAllRequestOut",
        "PlayerScoreResetResponseIn": "_gamesManagement_6_PlayerScoreResetResponseIn",
        "PlayerScoreResetResponseOut": "_gamesManagement_7_PlayerScoreResetResponseOut",
        "ScoresResetMultipleForAllRequestIn": "_gamesManagement_8_ScoresResetMultipleForAllRequestIn",
        "ScoresResetMultipleForAllRequestOut": "_gamesManagement_9_ScoresResetMultipleForAllRequestOut",
        "AchievementResetResponseIn": "_gamesManagement_10_AchievementResetResponseIn",
        "AchievementResetResponseOut": "_gamesManagement_11_AchievementResetResponseOut",
        "EventsResetMultipleForAllRequestIn": "_gamesManagement_12_EventsResetMultipleForAllRequestIn",
        "EventsResetMultipleForAllRequestOut": "_gamesManagement_13_EventsResetMultipleForAllRequestOut",
        "HiddenPlayerIn": "_gamesManagement_14_HiddenPlayerIn",
        "HiddenPlayerOut": "_gamesManagement_15_HiddenPlayerOut",
        "GamesPlayerLevelResourceIn": "_gamesManagement_16_GamesPlayerLevelResourceIn",
        "GamesPlayerLevelResourceOut": "_gamesManagement_17_GamesPlayerLevelResourceOut",
        "PlayerScoreResetAllResponseIn": "_gamesManagement_18_PlayerScoreResetAllResponseIn",
        "PlayerScoreResetAllResponseOut": "_gamesManagement_19_PlayerScoreResetAllResponseOut",
        "HiddenPlayerListIn": "_gamesManagement_20_HiddenPlayerListIn",
        "HiddenPlayerListOut": "_gamesManagement_21_HiddenPlayerListOut",
        "AchievementResetAllResponseIn": "_gamesManagement_22_AchievementResetAllResponseIn",
        "AchievementResetAllResponseOut": "_gamesManagement_23_AchievementResetAllResponseOut",
        "GamesPlayerExperienceInfoResourceIn": "_gamesManagement_24_GamesPlayerExperienceInfoResourceIn",
        "GamesPlayerExperienceInfoResourceOut": "_gamesManagement_25_GamesPlayerExperienceInfoResourceOut",
        "ProfileSettingsIn": "_gamesManagement_26_ProfileSettingsIn",
        "ProfileSettingsOut": "_gamesManagement_27_ProfileSettingsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PlayerIn"] = t.struct(
        {
            "profileSettings": t.proxy(renames["ProfileSettingsIn"]).optional(),
            "experienceInfo": t.proxy(
                renames["GamesPlayerExperienceInfoResourceIn"]
            ).optional(),
            "bannerUrlPortrait": t.string().optional(),
            "name": t.struct(
                {
                    "familyName": t.string().optional(),
                    "givenName": t.string().optional(),
                }
            ).optional(),
            "originalPlayerId": t.string().optional(),
            "kind": t.string().optional(),
            "displayName": t.string().optional(),
            "playerId": t.string().optional(),
            "avatarImageUrl": t.string().optional(),
            "title": t.string().optional(),
            "bannerUrlLandscape": t.string().optional(),
        }
    ).named(renames["PlayerIn"])
    types["PlayerOut"] = t.struct(
        {
            "profileSettings": t.proxy(renames["ProfileSettingsOut"]).optional(),
            "experienceInfo": t.proxy(
                renames["GamesPlayerExperienceInfoResourceOut"]
            ).optional(),
            "bannerUrlPortrait": t.string().optional(),
            "name": t.struct(
                {
                    "familyName": t.string().optional(),
                    "givenName": t.string().optional(),
                }
            ).optional(),
            "originalPlayerId": t.string().optional(),
            "kind": t.string().optional(),
            "displayName": t.string().optional(),
            "playerId": t.string().optional(),
            "avatarImageUrl": t.string().optional(),
            "title": t.string().optional(),
            "bannerUrlLandscape": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerOut"])
    types["AchievementResetMultipleForAllRequestIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "achievement_ids": t.array(t.string()).optional(),
        }
    ).named(renames["AchievementResetMultipleForAllRequestIn"])
    types["AchievementResetMultipleForAllRequestOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "achievement_ids": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementResetMultipleForAllRequestOut"])
    types["PlayerScoreResetResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "resetScoreTimeSpans": t.array(t.string()).optional(),
            "definitionId": t.string().optional(),
        }
    ).named(renames["PlayerScoreResetResponseIn"])
    types["PlayerScoreResetResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "resetScoreTimeSpans": t.array(t.string()).optional(),
            "definitionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerScoreResetResponseOut"])
    types["ScoresResetMultipleForAllRequestIn"] = t.struct(
        {
            "leaderboard_ids": t.array(t.string()).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ScoresResetMultipleForAllRequestIn"])
    types["ScoresResetMultipleForAllRequestOut"] = t.struct(
        {
            "leaderboard_ids": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScoresResetMultipleForAllRequestOut"])
    types["AchievementResetResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "currentState": t.string().optional(),
            "definitionId": t.string().optional(),
            "updateOccurred": t.boolean().optional(),
        }
    ).named(renames["AchievementResetResponseIn"])
    types["AchievementResetResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "currentState": t.string().optional(),
            "definitionId": t.string().optional(),
            "updateOccurred": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementResetResponseOut"])
    types["EventsResetMultipleForAllRequestIn"] = t.struct(
        {"event_ids": t.array(t.string()).optional(), "kind": t.string().optional()}
    ).named(renames["EventsResetMultipleForAllRequestIn"])
    types["EventsResetMultipleForAllRequestOut"] = t.struct(
        {
            "event_ids": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventsResetMultipleForAllRequestOut"])
    types["HiddenPlayerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["HiddenPlayerIn"]
    )
    types["HiddenPlayerOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "hiddenTimeMillis": t.string().optional(),
            "player": t.proxy(renames["PlayerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HiddenPlayerOut"])
    types["GamesPlayerLevelResourceIn"] = t.struct(
        {
            "maxExperiencePoints": t.string().optional(),
            "level": t.integer().optional(),
            "minExperiencePoints": t.string().optional(),
        }
    ).named(renames["GamesPlayerLevelResourceIn"])
    types["GamesPlayerLevelResourceOut"] = t.struct(
        {
            "maxExperiencePoints": t.string().optional(),
            "level": t.integer().optional(),
            "minExperiencePoints": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GamesPlayerLevelResourceOut"])
    types["PlayerScoreResetAllResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "results": t.array(
                t.proxy(renames["PlayerScoreResetResponseIn"])
            ).optional(),
        }
    ).named(renames["PlayerScoreResetAllResponseIn"])
    types["PlayerScoreResetAllResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "results": t.array(
                t.proxy(renames["PlayerScoreResetResponseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerScoreResetAllResponseOut"])
    types["HiddenPlayerListIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["HiddenPlayerIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["HiddenPlayerListIn"])
    types["HiddenPlayerListOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["HiddenPlayerOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HiddenPlayerListOut"])
    types["AchievementResetAllResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "results": t.array(
                t.proxy(renames["AchievementResetResponseIn"])
            ).optional(),
        }
    ).named(renames["AchievementResetAllResponseIn"])
    types["AchievementResetAllResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "results": t.array(
                t.proxy(renames["AchievementResetResponseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementResetAllResponseOut"])
    types["GamesPlayerExperienceInfoResourceIn"] = t.struct(
        {
            "lastLevelUpTimestampMillis": t.string().optional(),
            "currentExperiencePoints": t.string().optional(),
            "currentLevel": t.proxy(renames["GamesPlayerLevelResourceIn"]).optional(),
            "nextLevel": t.proxy(renames["GamesPlayerLevelResourceIn"]).optional(),
        }
    ).named(renames["GamesPlayerExperienceInfoResourceIn"])
    types["GamesPlayerExperienceInfoResourceOut"] = t.struct(
        {
            "lastLevelUpTimestampMillis": t.string().optional(),
            "currentExperiencePoints": t.string().optional(),
            "currentLevel": t.proxy(renames["GamesPlayerLevelResourceOut"]).optional(),
            "nextLevel": t.proxy(renames["GamesPlayerLevelResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GamesPlayerExperienceInfoResourceOut"])
    types["ProfileSettingsIn"] = t.struct(
        {"kind": t.string().optional(), "profileVisible": t.boolean()}
    ).named(renames["ProfileSettingsIn"])
    types["ProfileSettingsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "profileVisible": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileSettingsOut"])

    functions = {}
    functions["playersUnhide"] = gamesManagement.post(
        "games/v1management/applications/{applicationId}/players/hidden/{playerId}",
        t.struct(
            {
                "playerId": t.string().optional(),
                "applicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["playersHide"] = gamesManagement.post(
        "games/v1management/applications/{applicationId}/players/hidden/{playerId}",
        t.struct(
            {
                "playerId": t.string().optional(),
                "applicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsResetForAllPlayers"] = gamesManagement.post(
        "games/v1management/events/resetAllForAllPlayers",
        t.struct({"auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsResetAll"] = gamesManagement.post(
        "games/v1management/events/resetAllForAllPlayers",
        t.struct({"auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsResetMultipleForAllPlayers"] = gamesManagement.post(
        "games/v1management/events/resetAllForAllPlayers",
        t.struct({"auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsReset"] = gamesManagement.post(
        "games/v1management/events/resetAllForAllPlayers",
        t.struct({"auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsResetAllForAllPlayers"] = gamesManagement.post(
        "games/v1management/events/resetAllForAllPlayers",
        t.struct({"auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsResetForAllPlayers"] = gamesManagement.post(
        "games/v1management/achievements/{achievementId}/reset",
        t.struct(
            {"achievementId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["AchievementResetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsResetAll"] = gamesManagement.post(
        "games/v1management/achievements/{achievementId}/reset",
        t.struct(
            {"achievementId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["AchievementResetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsResetMultipleForAllPlayers"] = gamesManagement.post(
        "games/v1management/achievements/{achievementId}/reset",
        t.struct(
            {"achievementId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["AchievementResetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsResetAllForAllPlayers"] = gamesManagement.post(
        "games/v1management/achievements/{achievementId}/reset",
        t.struct(
            {"achievementId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["AchievementResetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsReset"] = gamesManagement.post(
        "games/v1management/achievements/{achievementId}/reset",
        t.struct(
            {"achievementId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["AchievementResetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["applicationsListHidden"] = gamesManagement.get(
        "games/v1management/applications/{applicationId}/players/hidden",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "applicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HiddenPlayerListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresResetAllForAllPlayers"] = gamesManagement.post(
        "games/v1management/scores/reset",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["PlayerScoreResetAllResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresResetMultipleForAllPlayers"] = gamesManagement.post(
        "games/v1management/scores/reset",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["PlayerScoreResetAllResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresResetForAllPlayers"] = gamesManagement.post(
        "games/v1management/scores/reset",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["PlayerScoreResetAllResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresReset"] = gamesManagement.post(
        "games/v1management/scores/reset",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["PlayerScoreResetAllResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresResetAll"] = gamesManagement.post(
        "games/v1management/scores/reset",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["PlayerScoreResetAllResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="gamesManagement",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
