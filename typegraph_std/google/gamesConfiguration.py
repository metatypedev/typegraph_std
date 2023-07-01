from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_gamesConfiguration():
    gamesConfiguration = HTTPRuntime("https://gamesconfiguration.googleapis.com/")

    renames = {
        "ErrorResponse": "_gamesConfiguration_1_ErrorResponse",
        "AchievementConfigurationIn": "_gamesConfiguration_2_AchievementConfigurationIn",
        "AchievementConfigurationOut": "_gamesConfiguration_3_AchievementConfigurationOut",
        "LocalizedStringBundleIn": "_gamesConfiguration_4_LocalizedStringBundleIn",
        "LocalizedStringBundleOut": "_gamesConfiguration_5_LocalizedStringBundleOut",
        "AchievementConfigurationListResponseIn": "_gamesConfiguration_6_AchievementConfigurationListResponseIn",
        "AchievementConfigurationListResponseOut": "_gamesConfiguration_7_AchievementConfigurationListResponseOut",
        "LeaderboardConfigurationListResponseIn": "_gamesConfiguration_8_LeaderboardConfigurationListResponseIn",
        "LeaderboardConfigurationListResponseOut": "_gamesConfiguration_9_LeaderboardConfigurationListResponseOut",
        "LeaderboardConfigurationDetailIn": "_gamesConfiguration_10_LeaderboardConfigurationDetailIn",
        "LeaderboardConfigurationDetailOut": "_gamesConfiguration_11_LeaderboardConfigurationDetailOut",
        "LocalizedStringIn": "_gamesConfiguration_12_LocalizedStringIn",
        "LocalizedStringOut": "_gamesConfiguration_13_LocalizedStringOut",
        "GamesNumberFormatConfigurationIn": "_gamesConfiguration_14_GamesNumberFormatConfigurationIn",
        "GamesNumberFormatConfigurationOut": "_gamesConfiguration_15_GamesNumberFormatConfigurationOut",
        "GamesNumberAffixConfigurationIn": "_gamesConfiguration_16_GamesNumberAffixConfigurationIn",
        "GamesNumberAffixConfigurationOut": "_gamesConfiguration_17_GamesNumberAffixConfigurationOut",
        "LeaderboardConfigurationIn": "_gamesConfiguration_18_LeaderboardConfigurationIn",
        "LeaderboardConfigurationOut": "_gamesConfiguration_19_LeaderboardConfigurationOut",
        "AchievementConfigurationDetailIn": "_gamesConfiguration_20_AchievementConfigurationDetailIn",
        "AchievementConfigurationDetailOut": "_gamesConfiguration_21_AchievementConfigurationDetailOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AchievementConfigurationIn"] = t.struct(
        {
            "initialState": t.string().optional(),
            "id": t.string().optional(),
            "achievementType": t.string().optional(),
            "kind": t.string().optional(),
            "published": t.proxy(
                renames["AchievementConfigurationDetailIn"]
            ).optional(),
            "token": t.string().optional(),
            "draft": t.proxy(renames["AchievementConfigurationDetailIn"]).optional(),
            "stepsToUnlock": t.integer().optional(),
        }
    ).named(renames["AchievementConfigurationIn"])
    types["AchievementConfigurationOut"] = t.struct(
        {
            "initialState": t.string().optional(),
            "id": t.string().optional(),
            "achievementType": t.string().optional(),
            "kind": t.string().optional(),
            "published": t.proxy(
                renames["AchievementConfigurationDetailOut"]
            ).optional(),
            "token": t.string().optional(),
            "draft": t.proxy(renames["AchievementConfigurationDetailOut"]).optional(),
            "stepsToUnlock": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementConfigurationOut"])
    types["LocalizedStringBundleIn"] = t.struct(
        {
            "translations": t.array(t.proxy(renames["LocalizedStringIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LocalizedStringBundleIn"])
    types["LocalizedStringBundleOut"] = t.struct(
        {
            "translations": t.array(t.proxy(renames["LocalizedStringOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizedStringBundleOut"])
    types["AchievementConfigurationListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["AchievementConfigurationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["AchievementConfigurationListResponseIn"])
    types["AchievementConfigurationListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(
                t.proxy(renames["AchievementConfigurationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementConfigurationListResponseOut"])
    types["LeaderboardConfigurationListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["LeaderboardConfigurationIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LeaderboardConfigurationListResponseIn"])
    types["LeaderboardConfigurationListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(
                t.proxy(renames["LeaderboardConfigurationOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaderboardConfigurationListResponseOut"])
    types["LeaderboardConfigurationDetailIn"] = t.struct(
        {
            "scoreFormat": t.proxy(
                renames["GamesNumberFormatConfigurationIn"]
            ).optional(),
            "kind": t.string().optional(),
            "iconUrl": t.string().optional(),
            "sortRank": t.integer().optional(),
            "name": t.proxy(renames["LocalizedStringBundleIn"]).optional(),
        }
    ).named(renames["LeaderboardConfigurationDetailIn"])
    types["LeaderboardConfigurationDetailOut"] = t.struct(
        {
            "scoreFormat": t.proxy(
                renames["GamesNumberFormatConfigurationOut"]
            ).optional(),
            "kind": t.string().optional(),
            "iconUrl": t.string().optional(),
            "sortRank": t.integer().optional(),
            "name": t.proxy(renames["LocalizedStringBundleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaderboardConfigurationDetailOut"])
    types["LocalizedStringIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "locale": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["LocalizedStringIn"])
    types["LocalizedStringOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "locale": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizedStringOut"])
    types["GamesNumberFormatConfigurationIn"] = t.struct(
        {
            "suffix": t.proxy(renames["GamesNumberAffixConfigurationIn"]).optional(),
            "numDecimalPlaces": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "numberFormatType": t.string().optional(),
        }
    ).named(renames["GamesNumberFormatConfigurationIn"])
    types["GamesNumberFormatConfigurationOut"] = t.struct(
        {
            "suffix": t.proxy(renames["GamesNumberAffixConfigurationOut"]).optional(),
            "numDecimalPlaces": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "numberFormatType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GamesNumberFormatConfigurationOut"])
    types["GamesNumberAffixConfigurationIn"] = t.struct(
        {
            "few": t.proxy(renames["LocalizedStringBundleIn"]).optional(),
            "many": t.proxy(renames["LocalizedStringBundleIn"]).optional(),
            "two": t.proxy(renames["LocalizedStringBundleIn"]).optional(),
            "one": t.proxy(renames["LocalizedStringBundleIn"]).optional(),
            "zero": t.proxy(renames["LocalizedStringBundleIn"]).optional(),
            "other": t.proxy(renames["LocalizedStringBundleIn"]).optional(),
        }
    ).named(renames["GamesNumberAffixConfigurationIn"])
    types["GamesNumberAffixConfigurationOut"] = t.struct(
        {
            "few": t.proxy(renames["LocalizedStringBundleOut"]).optional(),
            "many": t.proxy(renames["LocalizedStringBundleOut"]).optional(),
            "two": t.proxy(renames["LocalizedStringBundleOut"]).optional(),
            "one": t.proxy(renames["LocalizedStringBundleOut"]).optional(),
            "zero": t.proxy(renames["LocalizedStringBundleOut"]).optional(),
            "other": t.proxy(renames["LocalizedStringBundleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GamesNumberAffixConfigurationOut"])
    types["LeaderboardConfigurationIn"] = t.struct(
        {
            "draft": t.proxy(renames["LeaderboardConfigurationDetailIn"]).optional(),
            "id": t.string().optional(),
            "token": t.string().optional(),
            "scoreMin": t.string().optional(),
            "published": t.proxy(
                renames["LeaderboardConfigurationDetailIn"]
            ).optional(),
            "kind": t.string().optional(),
            "scoreMax": t.string().optional(),
            "scoreOrder": t.string(),
        }
    ).named(renames["LeaderboardConfigurationIn"])
    types["LeaderboardConfigurationOut"] = t.struct(
        {
            "draft": t.proxy(renames["LeaderboardConfigurationDetailOut"]).optional(),
            "id": t.string().optional(),
            "token": t.string().optional(),
            "scoreMin": t.string().optional(),
            "published": t.proxy(
                renames["LeaderboardConfigurationDetailOut"]
            ).optional(),
            "kind": t.string().optional(),
            "scoreMax": t.string().optional(),
            "scoreOrder": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaderboardConfigurationOut"])
    types["AchievementConfigurationDetailIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "sortRank": t.integer().optional(),
            "pointValue": t.integer().optional(),
            "description": t.proxy(renames["LocalizedStringBundleIn"]).optional(),
            "name": t.proxy(renames["LocalizedStringBundleIn"]).optional(),
            "iconUrl": t.string().optional(),
        }
    ).named(renames["AchievementConfigurationDetailIn"])
    types["AchievementConfigurationDetailOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "sortRank": t.integer().optional(),
            "pointValue": t.integer().optional(),
            "description": t.proxy(renames["LocalizedStringBundleOut"]).optional(),
            "name": t.proxy(renames["LocalizedStringBundleOut"]).optional(),
            "iconUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementConfigurationDetailOut"])

    functions = {}
    functions["leaderboardConfigurationsUpdate"] = gamesConfiguration.post(
        "games/v1configuration/applications/{applicationId}/leaderboards",
        t.struct(
            {
                "applicationId": t.string().optional(),
                "draft": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "id": t.string().optional(),
                "token": t.string().optional(),
                "scoreMin": t.string().optional(),
                "published": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "kind": t.string().optional(),
                "scoreMax": t.string().optional(),
                "scoreOrder": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["leaderboardConfigurationsList"] = gamesConfiguration.post(
        "games/v1configuration/applications/{applicationId}/leaderboards",
        t.struct(
            {
                "applicationId": t.string().optional(),
                "draft": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "id": t.string().optional(),
                "token": t.string().optional(),
                "scoreMin": t.string().optional(),
                "published": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "kind": t.string().optional(),
                "scoreMax": t.string().optional(),
                "scoreOrder": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["leaderboardConfigurationsGet"] = gamesConfiguration.post(
        "games/v1configuration/applications/{applicationId}/leaderboards",
        t.struct(
            {
                "applicationId": t.string().optional(),
                "draft": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "id": t.string().optional(),
                "token": t.string().optional(),
                "scoreMin": t.string().optional(),
                "published": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "kind": t.string().optional(),
                "scoreMax": t.string().optional(),
                "scoreOrder": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["leaderboardConfigurationsDelete"] = gamesConfiguration.post(
        "games/v1configuration/applications/{applicationId}/leaderboards",
        t.struct(
            {
                "applicationId": t.string().optional(),
                "draft": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "id": t.string().optional(),
                "token": t.string().optional(),
                "scoreMin": t.string().optional(),
                "published": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "kind": t.string().optional(),
                "scoreMax": t.string().optional(),
                "scoreOrder": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["leaderboardConfigurationsInsert"] = gamesConfiguration.post(
        "games/v1configuration/applications/{applicationId}/leaderboards",
        t.struct(
            {
                "applicationId": t.string().optional(),
                "draft": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "id": t.string().optional(),
                "token": t.string().optional(),
                "scoreMin": t.string().optional(),
                "published": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "kind": t.string().optional(),
                "scoreMax": t.string().optional(),
                "scoreOrder": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementConfigurationsGet"] = gamesConfiguration.put(
        "games/v1configuration/achievements/{achievementId}",
        t.struct(
            {
                "achievementId": t.string().optional(),
                "initialState": t.string().optional(),
                "id": t.string().optional(),
                "achievementType": t.string().optional(),
                "kind": t.string().optional(),
                "published": t.proxy(
                    renames["AchievementConfigurationDetailIn"]
                ).optional(),
                "token": t.string().optional(),
                "draft": t.proxy(
                    renames["AchievementConfigurationDetailIn"]
                ).optional(),
                "stepsToUnlock": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AchievementConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementConfigurationsList"] = gamesConfiguration.put(
        "games/v1configuration/achievements/{achievementId}",
        t.struct(
            {
                "achievementId": t.string().optional(),
                "initialState": t.string().optional(),
                "id": t.string().optional(),
                "achievementType": t.string().optional(),
                "kind": t.string().optional(),
                "published": t.proxy(
                    renames["AchievementConfigurationDetailIn"]
                ).optional(),
                "token": t.string().optional(),
                "draft": t.proxy(
                    renames["AchievementConfigurationDetailIn"]
                ).optional(),
                "stepsToUnlock": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AchievementConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementConfigurationsInsert"] = gamesConfiguration.put(
        "games/v1configuration/achievements/{achievementId}",
        t.struct(
            {
                "achievementId": t.string().optional(),
                "initialState": t.string().optional(),
                "id": t.string().optional(),
                "achievementType": t.string().optional(),
                "kind": t.string().optional(),
                "published": t.proxy(
                    renames["AchievementConfigurationDetailIn"]
                ).optional(),
                "token": t.string().optional(),
                "draft": t.proxy(
                    renames["AchievementConfigurationDetailIn"]
                ).optional(),
                "stepsToUnlock": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AchievementConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementConfigurationsDelete"] = gamesConfiguration.put(
        "games/v1configuration/achievements/{achievementId}",
        t.struct(
            {
                "achievementId": t.string().optional(),
                "initialState": t.string().optional(),
                "id": t.string().optional(),
                "achievementType": t.string().optional(),
                "kind": t.string().optional(),
                "published": t.proxy(
                    renames["AchievementConfigurationDetailIn"]
                ).optional(),
                "token": t.string().optional(),
                "draft": t.proxy(
                    renames["AchievementConfigurationDetailIn"]
                ).optional(),
                "stepsToUnlock": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AchievementConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementConfigurationsUpdate"] = gamesConfiguration.put(
        "games/v1configuration/achievements/{achievementId}",
        t.struct(
            {
                "achievementId": t.string().optional(),
                "initialState": t.string().optional(),
                "id": t.string().optional(),
                "achievementType": t.string().optional(),
                "kind": t.string().optional(),
                "published": t.proxy(
                    renames["AchievementConfigurationDetailIn"]
                ).optional(),
                "token": t.string().optional(),
                "draft": t.proxy(
                    renames["AchievementConfigurationDetailIn"]
                ).optional(),
                "stepsToUnlock": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AchievementConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="gamesConfiguration",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
