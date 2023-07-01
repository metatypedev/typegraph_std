from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    AchievementConfigurationIn: t.typedef = ...
    AchievementConfigurationOut: t.typedef = ...
    LocalizedStringBundleIn: t.typedef = ...
    LocalizedStringBundleOut: t.typedef = ...
    AchievementConfigurationListResponseIn: t.typedef = ...
    AchievementConfigurationListResponseOut: t.typedef = ...
    LeaderboardConfigurationListResponseIn: t.typedef = ...
    LeaderboardConfigurationListResponseOut: t.typedef = ...
    LeaderboardConfigurationDetailIn: t.typedef = ...
    LeaderboardConfigurationDetailOut: t.typedef = ...
    LocalizedStringIn: t.typedef = ...
    LocalizedStringOut: t.typedef = ...
    GamesNumberFormatConfigurationIn: t.typedef = ...
    GamesNumberFormatConfigurationOut: t.typedef = ...
    GamesNumberAffixConfigurationIn: t.typedef = ...
    GamesNumberAffixConfigurationOut: t.typedef = ...
    LeaderboardConfigurationIn: t.typedef = ...
    LeaderboardConfigurationOut: t.typedef = ...
    AchievementConfigurationDetailIn: t.typedef = ...
    AchievementConfigurationDetailOut: t.typedef = ...

class FuncList:
    leaderboardConfigurationsUpdate: t.func = ...
    leaderboardConfigurationsList: t.func = ...
    leaderboardConfigurationsGet: t.func = ...
    leaderboardConfigurationsDelete: t.func = ...
    leaderboardConfigurationsInsert: t.func = ...
    achievementConfigurationsGet: t.func = ...
    achievementConfigurationsList: t.func = ...
    achievementConfigurationsInsert: t.func = ...
    achievementConfigurationsDelete: t.func = ...
    achievementConfigurationsUpdate: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_gamesConfiguration() -> Import: ...
