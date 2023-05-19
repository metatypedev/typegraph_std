from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_versionhistory() -> Import:
    versionhistory = HTTPRuntime("https://versionhistory.googleapis.com/")

    renames = {
        "ErrorResponse": "_versionhistory_1_ErrorResponse",
        "ChannelIn": "_versionhistory_2_ChannelIn",
        "ChannelOut": "_versionhistory_3_ChannelOut",
        "ListChannelsResponseIn": "_versionhistory_4_ListChannelsResponseIn",
        "ListChannelsResponseOut": "_versionhistory_5_ListChannelsResponseOut",
        "PlatformIn": "_versionhistory_6_PlatformIn",
        "PlatformOut": "_versionhistory_7_PlatformOut",
        "ListPlatformsResponseIn": "_versionhistory_8_ListPlatformsResponseIn",
        "ListPlatformsResponseOut": "_versionhistory_9_ListPlatformsResponseOut",
        "IntervalIn": "_versionhistory_10_IntervalIn",
        "IntervalOut": "_versionhistory_11_IntervalOut",
        "VersionIn": "_versionhistory_12_VersionIn",
        "VersionOut": "_versionhistory_13_VersionOut",
        "ListReleasesResponseIn": "_versionhistory_14_ListReleasesResponseIn",
        "ListReleasesResponseOut": "_versionhistory_15_ListReleasesResponseOut",
        "ListVersionsResponseIn": "_versionhistory_16_ListVersionsResponseIn",
        "ListVersionsResponseOut": "_versionhistory_17_ListVersionsResponseOut",
        "ReleaseIn": "_versionhistory_18_ReleaseIn",
        "ReleaseOut": "_versionhistory_19_ReleaseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ChannelIn"] = t.struct(
        {"channelType": t.string().optional(), "name": t.string().optional()}
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "channelType": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
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
    types["ListPlatformsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "platforms": t.array(t.proxy(renames["PlatformIn"])).optional(),
        }
    ).named(renames["ListPlatformsResponseIn"])
    types["ListPlatformsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "platforms": t.array(t.proxy(renames["PlatformOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPlatformsResponseOut"])
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
    types["ListReleasesResponseIn"] = t.struct(
        {
            "releases": t.array(t.proxy(renames["ReleaseIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListReleasesResponseIn"])
    types["ListReleasesResponseOut"] = t.struct(
        {
            "releases": t.array(t.proxy(renames["ReleaseOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReleasesResponseOut"])
    types["ListVersionsResponseIn"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["VersionIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListVersionsResponseIn"])
    types["ListVersionsResponseOut"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["VersionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVersionsResponseOut"])
    types["ReleaseIn"] = t.struct(
        {
            "fractionGroup": t.string().optional(),
            "serving": t.proxy(renames["IntervalIn"]).optional(),
            "name": t.string().optional(),
            "version": t.string().optional(),
            "fraction": t.number().optional(),
        }
    ).named(renames["ReleaseIn"])
    types["ReleaseOut"] = t.struct(
        {
            "fractionGroup": t.string().optional(),
            "serving": t.proxy(renames["IntervalOut"]).optional(),
            "name": t.string().optional(),
            "version": t.string().optional(),
            "fraction": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseOut"])

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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
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
