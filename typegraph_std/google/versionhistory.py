from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_versionhistory() -> Import:
    versionhistory = HTTPRuntime("https://versionhistory.googleapis.com/")

    renames = {
        "ErrorResponse": "_versionhistory_1_ErrorResponse",
        "ListPlatformsResponseIn": "_versionhistory_2_ListPlatformsResponseIn",
        "ListPlatformsResponseOut": "_versionhistory_3_ListPlatformsResponseOut",
        "ListReleasesResponseIn": "_versionhistory_4_ListReleasesResponseIn",
        "ListReleasesResponseOut": "_versionhistory_5_ListReleasesResponseOut",
        "ChannelIn": "_versionhistory_6_ChannelIn",
        "ChannelOut": "_versionhistory_7_ChannelOut",
        "ListVersionsResponseIn": "_versionhistory_8_ListVersionsResponseIn",
        "ListVersionsResponseOut": "_versionhistory_9_ListVersionsResponseOut",
        "ListChannelsResponseIn": "_versionhistory_10_ListChannelsResponseIn",
        "ListChannelsResponseOut": "_versionhistory_11_ListChannelsResponseOut",
        "VersionIn": "_versionhistory_12_VersionIn",
        "VersionOut": "_versionhistory_13_VersionOut",
        "ReleaseIn": "_versionhistory_14_ReleaseIn",
        "ReleaseOut": "_versionhistory_15_ReleaseOut",
        "PlatformIn": "_versionhistory_16_PlatformIn",
        "PlatformOut": "_versionhistory_17_PlatformOut",
        "IntervalIn": "_versionhistory_18_IntervalIn",
        "IntervalOut": "_versionhistory_19_IntervalOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListPlatformsResponseIn"] = t.struct(
        {
            "platforms": t.array(t.proxy(renames["PlatformIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPlatformsResponseIn"])
    types["ListPlatformsResponseOut"] = t.struct(
        {
            "platforms": t.array(t.proxy(renames["PlatformOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPlatformsResponseOut"])
    types["ListReleasesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "releases": t.array(t.proxy(renames["ReleaseIn"])).optional(),
        }
    ).named(renames["ListReleasesResponseIn"])
    types["ListReleasesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "releases": t.array(t.proxy(renames["ReleaseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReleasesResponseOut"])
    types["ChannelIn"] = t.struct(
        {"name": t.string().optional(), "channelType": t.string().optional()}
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "name": t.string().optional(),
            "channelType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
    types["ListVersionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "versions": t.array(t.proxy(renames["VersionIn"])).optional(),
        }
    ).named(renames["ListVersionsResponseIn"])
    types["ListVersionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "versions": t.array(t.proxy(renames["VersionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVersionsResponseOut"])
    types["ListChannelsResponseIn"] = t.struct(
        {
            "channels": t.array(t.proxy(renames["ChannelIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListChannelsResponseIn"])
    types["ListChannelsResponseOut"] = t.struct(
        {
            "channels": t.array(t.proxy(renames["ChannelOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListChannelsResponseOut"])
    types["VersionIn"] = t.struct(
        {"name": t.string().optional(), "version": t.string().optional()}
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
    types["ReleaseIn"] = t.struct(
        {
            "fraction": t.number().optional(),
            "fractionGroup": t.string().optional(),
            "serving": t.proxy(renames["IntervalIn"]).optional(),
            "name": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["ReleaseIn"])
    types["ReleaseOut"] = t.struct(
        {
            "fraction": t.number().optional(),
            "fractionGroup": t.string().optional(),
            "serving": t.proxy(renames["IntervalOut"]).optional(),
            "name": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseOut"])
    types["PlatformIn"] = t.struct(
        {"name": t.string().optional(), "platformType": t.string().optional()}
    ).named(renames["PlatformIn"])
    types["PlatformOut"] = t.struct(
        {
            "name": t.string().optional(),
            "platformType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlatformOut"])
    types["IntervalIn"] = t.struct(
        {"endTime": t.string().optional(), "startTime": t.string().optional()}
    ).named(renames["IntervalIn"])
    types["IntervalOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntervalOut"])

    functions = {}
    functions["platformsList"] = versionhistory.get(
        "v1/{parent}/platforms",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPlatformsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["platformsChannelsList"] = versionhistory.get(
        "v1/{parent}/channels",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["platformsChannelsVersionsList"] = versionhistory.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["platformsChannelsVersionsReleasesList"] = versionhistory.get(
        "v1/{parent}/releases",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReleasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="versionhistory",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
