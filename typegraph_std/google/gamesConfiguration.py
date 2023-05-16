from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_gamesConfiguration() -> Import:
    gamesConfiguration = HTTPRuntime("https://gamesconfiguration.googleapis.com/")

    renames = {
        "ErrorResponse": "_gamesConfiguration_1_ErrorResponse",
        "LeaderboardConfigurationDetailIn": "_gamesConfiguration_2_LeaderboardConfigurationDetailIn",
        "LeaderboardConfigurationDetailOut": "_gamesConfiguration_3_LeaderboardConfigurationDetailOut",
        "GamesNumberFormatConfigurationIn": "_gamesConfiguration_4_GamesNumberFormatConfigurationIn",
        "GamesNumberFormatConfigurationOut": "_gamesConfiguration_5_GamesNumberFormatConfigurationOut",
        "AchievementConfigurationDetailIn": "_gamesConfiguration_6_AchievementConfigurationDetailIn",
        "AchievementConfigurationDetailOut": "_gamesConfiguration_7_AchievementConfigurationDetailOut",
        "LeaderboardConfigurationListResponseIn": "_gamesConfiguration_8_LeaderboardConfigurationListResponseIn",
        "LeaderboardConfigurationListResponseOut": "_gamesConfiguration_9_LeaderboardConfigurationListResponseOut",
        "AchievementConfigurationIn": "_gamesConfiguration_10_AchievementConfigurationIn",
        "AchievementConfigurationOut": "_gamesConfiguration_11_AchievementConfigurationOut",
        "LocalizedStringBundleIn": "_gamesConfiguration_12_LocalizedStringBundleIn",
        "LocalizedStringBundleOut": "_gamesConfiguration_13_LocalizedStringBundleOut",
        "LocalizedStringIn": "_gamesConfiguration_14_LocalizedStringIn",
        "LocalizedStringOut": "_gamesConfiguration_15_LocalizedStringOut",
        "LeaderboardConfigurationIn": "_gamesConfiguration_16_LeaderboardConfigurationIn",
        "LeaderboardConfigurationOut": "_gamesConfiguration_17_LeaderboardConfigurationOut",
        "AchievementConfigurationListResponseIn": "_gamesConfiguration_18_AchievementConfigurationListResponseIn",
        "AchievementConfigurationListResponseOut": "_gamesConfiguration_19_AchievementConfigurationListResponseOut",
        "GamesNumberAffixConfigurationIn": "_gamesConfiguration_20_GamesNumberAffixConfigurationIn",
        "GamesNumberAffixConfigurationOut": "_gamesConfiguration_21_GamesNumberAffixConfigurationOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LeaderboardConfigurationDetailIn"] = t.struct(
        {
            "sortRank": t.integer().optional(),
            "iconUrl": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.proxy(renames["LocalizedStringBundleIn"]).optional(),
            "scoreFormat": t.proxy(
                renames["GamesNumberFormatConfigurationIn"]
            ).optional(),
        }
    ).named(renames["LeaderboardConfigurationDetailIn"])
    types["LeaderboardConfigurationDetailOut"] = t.struct(
        {
            "sortRank": t.integer().optional(),
            "iconUrl": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.proxy(renames["LocalizedStringBundleOut"]).optional(),
            "scoreFormat": t.proxy(
                renames["GamesNumberFormatConfigurationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaderboardConfigurationDetailOut"])
    types["GamesNumberFormatConfigurationIn"] = t.struct(
        {
            "numDecimalPlaces": t.integer().optional(),
            "numberFormatType": t.string().optional(),
            "currencyCode": t.string().optional(),
            "suffix": t.proxy(renames["GamesNumberAffixConfigurationIn"]).optional(),
        }
    ).named(renames["GamesNumberFormatConfigurationIn"])
    types["GamesNumberFormatConfigurationOut"] = t.struct(
        {
            "numDecimalPlaces": t.integer().optional(),
            "numberFormatType": t.string().optional(),
            "currencyCode": t.string().optional(),
            "suffix": t.proxy(renames["GamesNumberAffixConfigurationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GamesNumberFormatConfigurationOut"])
    types["AchievementConfigurationDetailIn"] = t.struct(
        {
            "name": t.proxy(renames["LocalizedStringBundleIn"]).optional(),
            "pointValue": t.integer().optional(),
            "kind": t.string().optional(),
            "iconUrl": t.string().optional(),
            "description": t.proxy(renames["LocalizedStringBundleIn"]).optional(),
            "sortRank": t.integer().optional(),
        }
    ).named(renames["AchievementConfigurationDetailIn"])
    types["AchievementConfigurationDetailOut"] = t.struct(
        {
            "name": t.proxy(renames["LocalizedStringBundleOut"]).optional(),
            "pointValue": t.integer().optional(),
            "kind": t.string().optional(),
            "iconUrl": t.string().optional(),
            "description": t.proxy(renames["LocalizedStringBundleOut"]).optional(),
            "sortRank": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementConfigurationDetailOut"])
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
    types["AchievementConfigurationIn"] = t.struct(
        {
            "initialState": t.string().optional(),
            "token": t.string().optional(),
            "stepsToUnlock": t.integer().optional(),
            "kind": t.string().optional(),
            "published": t.proxy(
                renames["AchievementConfigurationDetailIn"]
            ).optional(),
            "draft": t.proxy(renames["AchievementConfigurationDetailIn"]).optional(),
            "achievementType": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["AchievementConfigurationIn"])
    types["AchievementConfigurationOut"] = t.struct(
        {
            "initialState": t.string().optional(),
            "token": t.string().optional(),
            "stepsToUnlock": t.integer().optional(),
            "kind": t.string().optional(),
            "published": t.proxy(
                renames["AchievementConfigurationDetailOut"]
            ).optional(),
            "draft": t.proxy(renames["AchievementConfigurationDetailOut"]).optional(),
            "achievementType": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementConfigurationOut"])
    types["LocalizedStringBundleIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "translations": t.array(t.proxy(renames["LocalizedStringIn"])).optional(),
        }
    ).named(renames["LocalizedStringBundleIn"])
    types["LocalizedStringBundleOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "translations": t.array(t.proxy(renames["LocalizedStringOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizedStringBundleOut"])
    types["LocalizedStringIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "value": t.string().optional(),
            "locale": t.string().optional(),
        }
    ).named(renames["LocalizedStringIn"])
    types["LocalizedStringOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "value": t.string().optional(),
            "locale": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizedStringOut"])
    types["LeaderboardConfigurationIn"] = t.struct(
        {
            "scoreOrder": t.string(),
            "published": t.proxy(
                renames["LeaderboardConfigurationDetailIn"]
            ).optional(),
            "scoreMin": t.string().optional(),
            "draft": t.proxy(renames["LeaderboardConfigurationDetailIn"]).optional(),
            "token": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "scoreMax": t.string().optional(),
        }
    ).named(renames["LeaderboardConfigurationIn"])
    types["LeaderboardConfigurationOut"] = t.struct(
        {
            "scoreOrder": t.string(),
            "published": t.proxy(
                renames["LeaderboardConfigurationDetailOut"]
            ).optional(),
            "scoreMin": t.string().optional(),
            "draft": t.proxy(renames["LeaderboardConfigurationDetailOut"]).optional(),
            "token": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "scoreMax": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaderboardConfigurationOut"])
    types["AchievementConfigurationListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["AchievementConfigurationIn"])).optional(),
        }
    ).named(renames["AchievementConfigurationListResponseIn"])
    types["AchievementConfigurationListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(
                t.proxy(renames["AchievementConfigurationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AchievementConfigurationListResponseOut"])
    types["GamesNumberAffixConfigurationIn"] = t.struct(
        {
            "one": t.proxy(renames["LocalizedStringBundleIn"]).optional(),
            "few": t.proxy(renames["LocalizedStringBundleIn"]).optional(),
            "other": t.proxy(renames["LocalizedStringBundleIn"]).optional(),
            "many": t.proxy(renames["LocalizedStringBundleIn"]).optional(),
            "two": t.proxy(renames["LocalizedStringBundleIn"]).optional(),
            "zero": t.proxy(renames["LocalizedStringBundleIn"]).optional(),
        }
    ).named(renames["GamesNumberAffixConfigurationIn"])
    types["GamesNumberAffixConfigurationOut"] = t.struct(
        {
            "one": t.proxy(renames["LocalizedStringBundleOut"]).optional(),
            "few": t.proxy(renames["LocalizedStringBundleOut"]).optional(),
            "other": t.proxy(renames["LocalizedStringBundleOut"]).optional(),
            "many": t.proxy(renames["LocalizedStringBundleOut"]).optional(),
            "two": t.proxy(renames["LocalizedStringBundleOut"]).optional(),
            "zero": t.proxy(renames["LocalizedStringBundleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GamesNumberAffixConfigurationOut"])

    functions = {}
    functions["leaderboardConfigurationsGet"] = gamesConfiguration.put(
        "games/v1configuration/leaderboards/{leaderboardId}",
        t.struct(
            {
                "leaderboardId": t.string().optional(),
                "scoreOrder": t.string(),
                "published": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "scoreMin": t.string().optional(),
                "draft": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "token": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "scoreMax": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["leaderboardConfigurationsDelete"] = gamesConfiguration.put(
        "games/v1configuration/leaderboards/{leaderboardId}",
        t.struct(
            {
                "leaderboardId": t.string().optional(),
                "scoreOrder": t.string(),
                "published": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "scoreMin": t.string().optional(),
                "draft": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "token": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "scoreMax": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["leaderboardConfigurationsList"] = gamesConfiguration.put(
        "games/v1configuration/leaderboards/{leaderboardId}",
        t.struct(
            {
                "leaderboardId": t.string().optional(),
                "scoreOrder": t.string(),
                "published": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "scoreMin": t.string().optional(),
                "draft": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "token": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "scoreMax": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["leaderboardConfigurationsInsert"] = gamesConfiguration.put(
        "games/v1configuration/leaderboards/{leaderboardId}",
        t.struct(
            {
                "leaderboardId": t.string().optional(),
                "scoreOrder": t.string(),
                "published": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "scoreMin": t.string().optional(),
                "draft": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "token": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "scoreMax": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["leaderboardConfigurationsUpdate"] = gamesConfiguration.put(
        "games/v1configuration/leaderboards/{leaderboardId}",
        t.struct(
            {
                "leaderboardId": t.string().optional(),
                "scoreOrder": t.string(),
                "published": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "scoreMin": t.string().optional(),
                "draft": t.proxy(
                    renames["LeaderboardConfigurationDetailIn"]
                ).optional(),
                "token": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "scoreMax": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaderboardConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementConfigurationsUpdate"] = gamesConfiguration.delete(
        "games/v1configuration/achievements/{achievementId}",
        t.struct(
            {"achievementId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementConfigurationsGet"] = gamesConfiguration.delete(
        "games/v1configuration/achievements/{achievementId}",
        t.struct(
            {"achievementId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementConfigurationsInsert"] = gamesConfiguration.delete(
        "games/v1configuration/achievements/{achievementId}",
        t.struct(
            {"achievementId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementConfigurationsList"] = gamesConfiguration.delete(
        "games/v1configuration/achievements/{achievementId}",
        t.struct(
            {"achievementId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["achievementConfigurationsDelete"] = gamesConfiguration.delete(
        "games/v1configuration/achievements/{achievementId}",
        t.struct(
            {"achievementId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="gamesConfiguration",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
