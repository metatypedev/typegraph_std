from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_resourcesettings() -> Import:
    resourcesettings = HTTPRuntime("https://resourcesettings.googleapis.com/")

    renames = {
        "ErrorResponse": "_resourcesettings_1_ErrorResponse",
        "GoogleCloudResourcesettingsV1SettingIn": "_resourcesettings_2_GoogleCloudResourcesettingsV1SettingIn",
        "GoogleCloudResourcesettingsV1SettingOut": "_resourcesettings_3_GoogleCloudResourcesettingsV1SettingOut",
        "GoogleCloudResourcesettingsV1ValueStringMapIn": "_resourcesettings_4_GoogleCloudResourcesettingsV1ValueStringMapIn",
        "GoogleCloudResourcesettingsV1ValueStringMapOut": "_resourcesettings_5_GoogleCloudResourcesettingsV1ValueStringMapOut",
        "GoogleCloudResourcesettingsV1ValueIn": "_resourcesettings_6_GoogleCloudResourcesettingsV1ValueIn",
        "GoogleCloudResourcesettingsV1ValueOut": "_resourcesettings_7_GoogleCloudResourcesettingsV1ValueOut",
        "GoogleCloudResourcesettingsV1SettingMetadataIn": "_resourcesettings_8_GoogleCloudResourcesettingsV1SettingMetadataIn",
        "GoogleCloudResourcesettingsV1SettingMetadataOut": "_resourcesettings_9_GoogleCloudResourcesettingsV1SettingMetadataOut",
        "GoogleCloudResourcesettingsV1ValueEnumValueIn": "_resourcesettings_10_GoogleCloudResourcesettingsV1ValueEnumValueIn",
        "GoogleCloudResourcesettingsV1ValueEnumValueOut": "_resourcesettings_11_GoogleCloudResourcesettingsV1ValueEnumValueOut",
        "GoogleCloudResourcesettingsV1ValueStringSetIn": "_resourcesettings_12_GoogleCloudResourcesettingsV1ValueStringSetIn",
        "GoogleCloudResourcesettingsV1ValueStringSetOut": "_resourcesettings_13_GoogleCloudResourcesettingsV1ValueStringSetOut",
        "GoogleCloudResourcesettingsV1ListSettingsResponseIn": "_resourcesettings_14_GoogleCloudResourcesettingsV1ListSettingsResponseIn",
        "GoogleCloudResourcesettingsV1ListSettingsResponseOut": "_resourcesettings_15_GoogleCloudResourcesettingsV1ListSettingsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudResourcesettingsV1SettingIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "localValue": t.proxy(
                renames["GoogleCloudResourcesettingsV1ValueIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudResourcesettingsV1SettingIn"])
    types["GoogleCloudResourcesettingsV1SettingOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.proxy(
                renames["GoogleCloudResourcesettingsV1SettingMetadataOut"]
            ).optional(),
            "localValue": t.proxy(
                renames["GoogleCloudResourcesettingsV1ValueOut"]
            ).optional(),
            "effectiveValue": t.proxy(
                renames["GoogleCloudResourcesettingsV1ValueOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudResourcesettingsV1SettingOut"])
    types["GoogleCloudResourcesettingsV1ValueStringMapIn"] = t.struct(
        {"mappings": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudResourcesettingsV1ValueStringMapIn"])
    types["GoogleCloudResourcesettingsV1ValueStringMapOut"] = t.struct(
        {
            "mappings": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudResourcesettingsV1ValueStringMapOut"])
    types["GoogleCloudResourcesettingsV1ValueIn"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "stringMapValue": t.proxy(
                renames["GoogleCloudResourcesettingsV1ValueStringMapIn"]
            ).optional(),
            "enumValue": t.proxy(
                renames["GoogleCloudResourcesettingsV1ValueEnumValueIn"]
            ).optional(),
            "durationValue": t.string().optional(),
            "stringSetValue": t.proxy(
                renames["GoogleCloudResourcesettingsV1ValueStringSetIn"]
            ).optional(),
            "booleanValue": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudResourcesettingsV1ValueIn"])
    types["GoogleCloudResourcesettingsV1ValueOut"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "stringMapValue": t.proxy(
                renames["GoogleCloudResourcesettingsV1ValueStringMapOut"]
            ).optional(),
            "enumValue": t.proxy(
                renames["GoogleCloudResourcesettingsV1ValueEnumValueOut"]
            ).optional(),
            "durationValue": t.string().optional(),
            "stringSetValue": t.proxy(
                renames["GoogleCloudResourcesettingsV1ValueStringSetOut"]
            ).optional(),
            "booleanValue": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudResourcesettingsV1ValueOut"])
    types["GoogleCloudResourcesettingsV1SettingMetadataIn"] = t.struct(
        {
            "readOnly": t.boolean().optional(),
            "defaultValue": t.proxy(
                renames["GoogleCloudResourcesettingsV1ValueIn"]
            ).optional(),
            "dataType": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudResourcesettingsV1SettingMetadataIn"])
    types["GoogleCloudResourcesettingsV1SettingMetadataOut"] = t.struct(
        {
            "readOnly": t.boolean().optional(),
            "defaultValue": t.proxy(
                renames["GoogleCloudResourcesettingsV1ValueOut"]
            ).optional(),
            "dataType": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudResourcesettingsV1SettingMetadataOut"])
    types["GoogleCloudResourcesettingsV1ValueEnumValueIn"] = t.struct(
        {"value": t.string().optional()}
    ).named(renames["GoogleCloudResourcesettingsV1ValueEnumValueIn"])
    types["GoogleCloudResourcesettingsV1ValueEnumValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudResourcesettingsV1ValueEnumValueOut"])
    types["GoogleCloudResourcesettingsV1ValueStringSetIn"] = t.struct(
        {"values": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudResourcesettingsV1ValueStringSetIn"])
    types["GoogleCloudResourcesettingsV1ValueStringSetOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudResourcesettingsV1ValueStringSetOut"])
    types["GoogleCloudResourcesettingsV1ListSettingsResponseIn"] = t.struct(
        {
            "settings": t.array(
                t.proxy(renames["GoogleCloudResourcesettingsV1SettingIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudResourcesettingsV1ListSettingsResponseIn"])
    types["GoogleCloudResourcesettingsV1ListSettingsResponseOut"] = t.struct(
        {
            "settings": t.array(
                t.proxy(renames["GoogleCloudResourcesettingsV1SettingOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudResourcesettingsV1ListSettingsResponseOut"])

    functions = {}
    functions["organizationsSettingsPatch"] = resourcesettings.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudResourcesettingsV1SettingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSettingsList"] = resourcesettings.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudResourcesettingsV1SettingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSettingsGet"] = resourcesettings.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudResourcesettingsV1SettingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSettingsGet"] = resourcesettings.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "localValue": t.proxy(
                    renames["GoogleCloudResourcesettingsV1ValueIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudResourcesettingsV1SettingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSettingsList"] = resourcesettings.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "localValue": t.proxy(
                    renames["GoogleCloudResourcesettingsV1ValueIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudResourcesettingsV1SettingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSettingsPatch"] = resourcesettings.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "localValue": t.proxy(
                    renames["GoogleCloudResourcesettingsV1ValueIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudResourcesettingsV1SettingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSettingsPatch"] = resourcesettings.get(
        "v1/{parent}/settings",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudResourcesettingsV1ListSettingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSettingsGet"] = resourcesettings.get(
        "v1/{parent}/settings",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudResourcesettingsV1ListSettingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSettingsList"] = resourcesettings.get(
        "v1/{parent}/settings",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudResourcesettingsV1ListSettingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="resourcesettings",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
