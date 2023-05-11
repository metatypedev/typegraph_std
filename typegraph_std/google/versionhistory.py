from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_versionhistory() -> Import:
    versionhistory = HTTPRuntime("https://versionhistory.googleapis.com/")

    renames = {
        "ErrorResponse": "_versionhistory_1_ErrorResponse",
        "VersionIn": "_versionhistory_2_VersionIn",
        "VersionOut": "_versionhistory_3_VersionOut",
        "ListReleasesResponseIn": "_versionhistory_4_ListReleasesResponseIn",
        "ListReleasesResponseOut": "_versionhistory_5_ListReleasesResponseOut",
        "PlatformIn": "_versionhistory_6_PlatformIn",
        "PlatformOut": "_versionhistory_7_PlatformOut",
        "ReleaseIn": "_versionhistory_8_ReleaseIn",
        "ReleaseOut": "_versionhistory_9_ReleaseOut",
        "ChannelIn": "_versionhistory_10_ChannelIn",
        "ChannelOut": "_versionhistory_11_ChannelOut",
        "ListPlatformsResponseIn": "_versionhistory_12_ListPlatformsResponseIn",
        "ListPlatformsResponseOut": "_versionhistory_13_ListPlatformsResponseOut",
        "IntervalIn": "_versionhistory_14_IntervalIn",
        "IntervalOut": "_versionhistory_15_IntervalOut",
        "ListVersionsResponseIn": "_versionhistory_16_ListVersionsResponseIn",
        "ListVersionsResponseOut": "_versionhistory_17_ListVersionsResponseOut",
        "ListChannelsResponseIn": "_versionhistory_18_ListChannelsResponseIn",
        "ListChannelsResponseOut": "_versionhistory_19_ListChannelsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ReleaseIn"] = t.struct(
        {
            "version": t.string().optional(),
            "fraction": t.number().optional(),
            "fractionGroup": t.string().optional(),
            "serving": t.proxy(renames["IntervalIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ReleaseIn"])
    types["ReleaseOut"] = t.struct(
        {
            "version": t.string().optional(),
            "fraction": t.number().optional(),
            "fractionGroup": t.string().optional(),
            "serving": t.proxy(renames["IntervalOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseOut"])
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
            "nextPageToken": t.string().optional(),
            "channels": t.array(t.proxy(renames["ChannelIn"])).optional(),
        }
    ).named(renames["ListChannelsResponseIn"])
    types["ListChannelsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "channels": t.array(t.proxy(renames["ChannelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListChannelsResponseOut"])

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
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
        importer="versionhistory", renames=renames, types=types, functions=functions
    )
