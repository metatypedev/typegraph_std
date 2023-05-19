from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_gamesManagement() -> Import:
    gamesManagement = HTTPRuntime("https://gamesmanagement.googleapis.com/")

    renames = {
        "ErrorResponse": "_gamesManagement_1_ErrorResponse",
        "PlayerScoreResetResponseIn": "_gamesManagement_2_PlayerScoreResetResponseIn",
        "PlayerScoreResetResponseOut": "_gamesManagement_3_PlayerScoreResetResponseOut",
        "AchievementResetResponseIn": "_gamesManagement_4_AchievementResetResponseIn",
        "AchievementResetResponseOut": "_gamesManagement_5_AchievementResetResponseOut",
        "PlayerIn": "_gamesManagement_6_PlayerIn",
        "PlayerOut": "_gamesManagement_7_PlayerOut",
        "EventsResetMultipleForAllRequestIn": "_gamesManagement_8_EventsResetMultipleForAllRequestIn",
        "EventsResetMultipleForAllRequestOut": "_gamesManagement_9_EventsResetMultipleForAllRequestOut",
        "HiddenPlayerIn": "_gamesManagement_10_HiddenPlayerIn",
        "HiddenPlayerOut": "_gamesManagement_11_HiddenPlayerOut",
        "PlayerScoreResetAllResponseIn": "_gamesManagement_12_PlayerScoreResetAllResponseIn",
        "PlayerScoreResetAllResponseOut": "_gamesManagement_13_PlayerScoreResetAllResponseOut",
        "ScoresResetMultipleForAllRequestIn": "_gamesManagement_14_ScoresResetMultipleForAllRequestIn",
        "ScoresResetMultipleForAllRequestOut": "_gamesManagement_15_ScoresResetMultipleForAllRequestOut",
        "AchievementResetAllResponseIn": "_gamesManagement_16_AchievementResetAllResponseIn",
        "AchievementResetAllResponseOut": "_gamesManagement_17_AchievementResetAllResponseOut",
        "GamesPlayerLevelResourceIn": "_gamesManagement_18_GamesPlayerLevelResourceIn",
        "GamesPlayerLevelResourceOut": "_gamesManagement_19_GamesPlayerLevelResourceOut",
        "ProfileSettingsIn": "_gamesManagement_20_ProfileSettingsIn",
        "ProfileSettingsOut": "_gamesManagement_21_ProfileSettingsOut",
        "GamesPlayerExperienceInfoResourceIn": "_gamesManagement_22_GamesPlayerExperienceInfoResourceIn",
        "GamesPlayerExperienceInfoResourceOut": "_gamesManagement_23_GamesPlayerExperienceInfoResourceOut",
        "AchievementResetMultipleForAllRequestIn": "_gamesManagement_24_AchievementResetMultipleForAllRequestIn",
        "AchievementResetMultipleForAllRequestOut": "_gamesManagement_25_AchievementResetMultipleForAllRequestOut",
        "HiddenPlayerListIn": "_gamesManagement_26_HiddenPlayerListIn",
        "HiddenPlayerListOut": "_gamesManagement_27_HiddenPlayerListOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PlayerScoreResetResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "definitionId": t.string().optional(),
            "resetScoreTimeSpans": t.array(t.string()).optional(),
        }
    ).named(renames["PlayerScoreResetResponseIn"])
    types["PlayerScoreResetResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "definitionId": t.string().optional(),
            "resetScoreTimeSpans": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerScoreResetResponseOut"])
    types["AchievementResetResponseIn"] = t.struct(
        {
            "definitionId": t.string().optional(),
            "currentState": t.string().optional(),
            "updateOccurred": t.boolean().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AchievementResetResponseIn"])
    types["AchievementResetResponseOut"] = t.struct(
        {
            "definitionId": t.string().optional(),
            "currentState": t.string().optional(),
            "updateOccurred": t.boolean().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementResetResponseOut"])
    types["PlayerIn"] = t.struct(
        {
            "bannerUrlPortrait": t.string().optional(),
            "originalPlayerId": t.string().optional(),
            "displayName": t.string().optional(),
            "bannerUrlLandscape": t.string().optional(),
            "playerId": t.string().optional(),
            "profileSettings": t.proxy(renames["ProfileSettingsIn"]).optional(),
            "avatarImageUrl": t.string().optional(),
            "experienceInfo": t.proxy(
                renames["GamesPlayerExperienceInfoResourceIn"]
            ).optional(),
            "title": t.string().optional(),
            "name": t.struct(
                {
                    "familyName": t.string().optional(),
                    "givenName": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PlayerIn"])
    types["PlayerOut"] = t.struct(
        {
            "bannerUrlPortrait": t.string().optional(),
            "originalPlayerId": t.string().optional(),
            "displayName": t.string().optional(),
            "bannerUrlLandscape": t.string().optional(),
            "playerId": t.string().optional(),
            "profileSettings": t.proxy(renames["ProfileSettingsOut"]).optional(),
            "avatarImageUrl": t.string().optional(),
            "experienceInfo": t.proxy(
                renames["GamesPlayerExperienceInfoResourceOut"]
            ).optional(),
            "title": t.string().optional(),
            "name": t.struct(
                {
                    "familyName": t.string().optional(),
                    "givenName": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlayerOut"])
    types["EventsResetMultipleForAllRequestIn"] = t.struct(
        {"kind": t.string().optional(), "event_ids": t.array(t.string()).optional()}
    ).named(renames["EventsResetMultipleForAllRequestIn"])
    types["EventsResetMultipleForAllRequestOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "event_ids": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventsResetMultipleForAllRequestOut"])
    types["HiddenPlayerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["HiddenPlayerIn"]
    )
    types["HiddenPlayerOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "player": t.proxy(renames["PlayerOut"]).optional(),
            "hiddenTimeMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HiddenPlayerOut"])
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
    types["ScoresResetMultipleForAllRequestIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "leaderboard_ids": t.array(t.string()).optional(),
        }
    ).named(renames["ScoresResetMultipleForAllRequestIn"])
    types["ScoresResetMultipleForAllRequestOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "leaderboard_ids": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScoresResetMultipleForAllRequestOut"])
    types["AchievementResetAllResponseIn"] = t.struct(
        {
            "results": t.array(
                t.proxy(renames["AchievementResetResponseIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AchievementResetAllResponseIn"])
    types["AchievementResetAllResponseOut"] = t.struct(
        {
            "results": t.array(
                t.proxy(renames["AchievementResetResponseOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementResetAllResponseOut"])
    types["GamesPlayerLevelResourceIn"] = t.struct(
        {
            "minExperiencePoints": t.string().optional(),
            "maxExperiencePoints": t.string().optional(),
            "level": t.integer().optional(),
        }
    ).named(renames["GamesPlayerLevelResourceIn"])
    types["GamesPlayerLevelResourceOut"] = t.struct(
        {
            "minExperiencePoints": t.string().optional(),
            "maxExperiencePoints": t.string().optional(),
            "level": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GamesPlayerLevelResourceOut"])
    types["ProfileSettingsIn"] = t.struct(
        {"profileVisible": t.boolean(), "kind": t.string().optional()}
    ).named(renames["ProfileSettingsIn"])
    types["ProfileSettingsOut"] = t.struct(
        {
            "profileVisible": t.boolean(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileSettingsOut"])
    types["GamesPlayerExperienceInfoResourceIn"] = t.struct(
        {
            "lastLevelUpTimestampMillis": t.string().optional(),
            "currentLevel": t.proxy(renames["GamesPlayerLevelResourceIn"]).optional(),
            "nextLevel": t.proxy(renames["GamesPlayerLevelResourceIn"]).optional(),
            "currentExperiencePoints": t.string().optional(),
        }
    ).named(renames["GamesPlayerExperienceInfoResourceIn"])
    types["GamesPlayerExperienceInfoResourceOut"] = t.struct(
        {
            "lastLevelUpTimestampMillis": t.string().optional(),
            "currentLevel": t.proxy(renames["GamesPlayerLevelResourceOut"]).optional(),
            "nextLevel": t.proxy(renames["GamesPlayerLevelResourceOut"]).optional(),
            "currentExperiencePoints": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GamesPlayerExperienceInfoResourceOut"])
    types["AchievementResetMultipleForAllRequestIn"] = t.struct(
        {
            "achievement_ids": t.array(t.string()).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AchievementResetMultipleForAllRequestIn"])
    types["AchievementResetMultipleForAllRequestOut"] = t.struct(
        {
            "achievement_ids": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementResetMultipleForAllRequestOut"])
    types["HiddenPlayerListIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["HiddenPlayerIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["HiddenPlayerListIn"])
    types["HiddenPlayerListOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["HiddenPlayerOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HiddenPlayerListOut"])

    functions = {}
    functions["applicationsListHidden"] = gamesManagement.get(
        "games/v1management/applications/{applicationId}/players/hidden",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "applicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HiddenPlayerListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresReset"] = gamesManagement.post(
        "games/v1management/scores/resetMultipleForAllPlayers",
        t.struct(
            {
                "kind": t.string().optional(),
                "leaderboard_ids": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresResetAllForAllPlayers"] = gamesManagement.post(
        "games/v1management/scores/resetMultipleForAllPlayers",
        t.struct(
            {
                "kind": t.string().optional(),
                "leaderboard_ids": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresResetAll"] = gamesManagement.post(
        "games/v1management/scores/resetMultipleForAllPlayers",
        t.struct(
            {
                "kind": t.string().optional(),
                "leaderboard_ids": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresResetForAllPlayers"] = gamesManagement.post(
        "games/v1management/scores/resetMultipleForAllPlayers",
        t.struct(
            {
                "kind": t.string().optional(),
                "leaderboard_ids": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scoresResetMultipleForAllPlayers"] = gamesManagement.post(
        "games/v1management/scores/resetMultipleForAllPlayers",
        t.struct(
            {
                "kind": t.string().optional(),
                "leaderboard_ids": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsResetAll"] = gamesManagement.post(
        "games/v1management/achievements/resetMultipleForAllPlayers",
        t.struct(
            {
                "achievement_ids": t.array(t.string()).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsResetForAllPlayers"] = gamesManagement.post(
        "games/v1management/achievements/resetMultipleForAllPlayers",
        t.struct(
            {
                "achievement_ids": t.array(t.string()).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsReset"] = gamesManagement.post(
        "games/v1management/achievements/resetMultipleForAllPlayers",
        t.struct(
            {
                "achievement_ids": t.array(t.string()).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsResetAllForAllPlayers"] = gamesManagement.post(
        "games/v1management/achievements/resetMultipleForAllPlayers",
        t.struct(
            {
                "achievement_ids": t.array(t.string()).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementsResetMultipleForAllPlayers"] = gamesManagement.post(
        "games/v1management/achievements/resetMultipleForAllPlayers",
        t.struct(
            {
                "achievement_ids": t.array(t.string()).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
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
    functions["eventsResetForAllPlayers"] = gamesManagement.post(
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
    functions["playersUnhide"] = gamesManagement.post(
        "games/v1management/applications/{applicationId}/players/hidden/{playerId}",
        t.struct(
            {
                "applicationId": t.string().optional(),
                "playerId": t.string().optional(),
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
                "applicationId": t.string().optional(),
                "playerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="gamesManagement",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
