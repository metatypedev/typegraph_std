from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_discovery() -> Import:
    discovery = HTTPRuntime("https://www.googleapis.com/")

    renames = {
        "ErrorResponse": "_discovery_1_ErrorResponse",
        "JsonSchemaIn": "_discovery_2_JsonSchemaIn",
        "JsonSchemaOut": "_discovery_3_JsonSchemaOut",
        "RestDescriptionIn": "_discovery_4_RestDescriptionIn",
        "RestDescriptionOut": "_discovery_5_RestDescriptionOut",
        "RestMethodIn": "_discovery_6_RestMethodIn",
        "RestMethodOut": "_discovery_7_RestMethodOut",
        "RestResourceIn": "_discovery_8_RestResourceIn",
        "RestResourceOut": "_discovery_9_RestResourceOut",
        "DirectoryListIn": "_discovery_10_DirectoryListIn",
        "DirectoryListOut": "_discovery_11_DirectoryListOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["JsonSchemaIn"] = t.struct(
        {
            "minimum": t.string().optional(),
            "$ref": t.string().optional(),
            "enum": t.array(t.string()).optional(),
            "location": t.string().optional(),
            "maximum": t.string().optional(),
            "readOnly": t.boolean().optional(),
            "description": t.string().optional(),
            "type": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "items": t.proxy(renames["JsonSchemaIn"]).optional(),
            "pattern": t.string().optional(),
            "enumDescriptions": t.array(t.string()).optional(),
            "default": t.string().optional(),
            "additionalProperties": t.proxy(renames["JsonSchemaIn"]).optional(),
            "repeated": t.boolean().optional(),
            "id": t.string().optional(),
            "format": t.string().optional(),
            "required": t.boolean().optional(),
            "variant": t.struct(
                {
                    "discriminant": t.string().optional(),
                    "map": t.array(
                        t.struct({"$ref": t.string(), "type_value": t.string()})
                    ).optional(),
                }
            ).optional(),
            "annotations": t.struct(
                {"required": t.array(t.string()).optional()}
            ).optional(),
        }
    ).named(renames["JsonSchemaIn"])
    types["JsonSchemaOut"] = t.struct(
        {
            "minimum": t.string().optional(),
            "$ref": t.string().optional(),
            "enum": t.array(t.string()).optional(),
            "location": t.string().optional(),
            "maximum": t.string().optional(),
            "readOnly": t.boolean().optional(),
            "description": t.string().optional(),
            "type": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "items": t.proxy(renames["JsonSchemaOut"]).optional(),
            "pattern": t.string().optional(),
            "enumDescriptions": t.array(t.string()).optional(),
            "default": t.string().optional(),
            "additionalProperties": t.proxy(renames["JsonSchemaOut"]).optional(),
            "repeated": t.boolean().optional(),
            "id": t.string().optional(),
            "format": t.string().optional(),
            "required": t.boolean().optional(),
            "variant": t.struct(
                {
                    "discriminant": t.string().optional(),
                    "map": t.array(
                        t.struct({"$ref": t.string(), "type_value": t.string()})
                    ).optional(),
                }
            ).optional(),
            "annotations": t.struct(
                {"required": t.array(t.string()).optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JsonSchemaOut"])
    types["RestDescriptionIn"] = t.struct(
        {
            "version": t.string().optional(),
            "batchPath": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "baseUrl": t.string().optional(),
            "discoveryVersion": t.string().optional(),
            "documentationLink": t.string().optional(),
            "kind": t.string().optional(),
            "exponentialBackoffDefault": t.boolean().optional(),
            "description": t.string().optional(),
            "packagePath": t.string().optional(),
            "resources": t.struct({"_": t.string().optional()}).optional(),
            "basePath": t.string().optional(),
            "labels": t.array(t.string()).optional(),
            "icons": t.struct(
                {"x32": t.string().optional(), "x16": t.string().optional()}
            ).optional(),
            "protocol": t.string().optional(),
            "auth": t.struct(
                {
                    "oauth2": t.struct(
                        {"scopes": t.struct({"_": t.string().optional()}).optional()}
                    ).optional()
                }
            ).optional(),
            "title": t.string().optional(),
            "revision": t.string().optional(),
            "rootUrl": t.string().optional(),
            "name": t.string().optional(),
            "canonicalName": t.string().optional(),
            "schemas": t.struct({"_": t.string().optional()}).optional(),
            "features": t.array(t.string()).optional(),
            "version_module": t.boolean(),
            "ownerDomain": t.string().optional(),
            "methods": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "ownerName": t.string().optional(),
            "servicePath": t.string().optional(),
        }
    ).named(renames["RestDescriptionIn"])
    types["RestDescriptionOut"] = t.struct(
        {
            "version": t.string().optional(),
            "batchPath": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "baseUrl": t.string().optional(),
            "discoveryVersion": t.string().optional(),
            "documentationLink": t.string().optional(),
            "kind": t.string().optional(),
            "exponentialBackoffDefault": t.boolean().optional(),
            "description": t.string().optional(),
            "packagePath": t.string().optional(),
            "resources": t.struct({"_": t.string().optional()}).optional(),
            "basePath": t.string().optional(),
            "labels": t.array(t.string()).optional(),
            "icons": t.struct(
                {"x32": t.string().optional(), "x16": t.string().optional()}
            ).optional(),
            "protocol": t.string().optional(),
            "auth": t.struct(
                {
                    "oauth2": t.struct(
                        {"scopes": t.struct({"_": t.string().optional()}).optional()}
                    ).optional()
                }
            ).optional(),
            "title": t.string().optional(),
            "revision": t.string().optional(),
            "rootUrl": t.string().optional(),
            "name": t.string().optional(),
            "canonicalName": t.string().optional(),
            "schemas": t.struct({"_": t.string().optional()}).optional(),
            "features": t.array(t.string()).optional(),
            "version_module": t.boolean(),
            "ownerDomain": t.string().optional(),
            "etag": t.string().optional(),
            "methods": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "ownerName": t.string().optional(),
            "servicePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestDescriptionOut"])
    types["RestMethodIn"] = t.struct(
        {
            "id": t.string().optional(),
            "response": t.struct({"$ref": t.string().optional()}).optional(),
            "flatPath": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "useMediaDownloadService": t.boolean().optional(),
            "etagRequired": t.boolean().optional(),
            "supportsSubscription": t.boolean().optional(),
            "mediaUpload": t.struct(
                {
                    "protocols": t.struct(
                        {
                            "resumable": t.struct(
                                {
                                    "path": t.string().optional(),
                                    "multipart": t.boolean().optional(),
                                }
                            ).optional(),
                            "simple": t.struct(
                                {
                                    "multipart": t.boolean().optional(),
                                    "path": t.string().optional(),
                                }
                            ).optional(),
                        }
                    ).optional(),
                    "accept": t.array(t.string()).optional(),
                    "maxSize": t.string().optional(),
                }
            ).optional(),
            "supportsMediaDownload": t.boolean().optional(),
            "supportsMediaUpload": t.boolean().optional(),
            "request": t.struct(
                {"parameterName": t.string().optional(), "$ref": t.string().optional()}
            ).optional(),
            "path": t.string().optional(),
            "httpMethod": t.string().optional(),
            "description": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "parameterOrder": t.array(t.string()).optional(),
        }
    ).named(renames["RestMethodIn"])
    types["RestMethodOut"] = t.struct(
        {
            "id": t.string().optional(),
            "response": t.struct({"$ref": t.string().optional()}).optional(),
            "flatPath": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "useMediaDownloadService": t.boolean().optional(),
            "etagRequired": t.boolean().optional(),
            "supportsSubscription": t.boolean().optional(),
            "mediaUpload": t.struct(
                {
                    "protocols": t.struct(
                        {
                            "resumable": t.struct(
                                {
                                    "path": t.string().optional(),
                                    "multipart": t.boolean().optional(),
                                }
                            ).optional(),
                            "simple": t.struct(
                                {
                                    "multipart": t.boolean().optional(),
                                    "path": t.string().optional(),
                                }
                            ).optional(),
                        }
                    ).optional(),
                    "accept": t.array(t.string()).optional(),
                    "maxSize": t.string().optional(),
                }
            ).optional(),
            "supportsMediaDownload": t.boolean().optional(),
            "supportsMediaUpload": t.boolean().optional(),
            "request": t.struct(
                {"parameterName": t.string().optional(), "$ref": t.string().optional()}
            ).optional(),
            "path": t.string().optional(),
            "httpMethod": t.string().optional(),
            "description": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "parameterOrder": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestMethodOut"])
    types["RestResourceIn"] = t.struct(
        {
            "resources": t.struct({"_": t.string().optional()}).optional(),
            "methods": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RestResourceIn"])
    types["RestResourceOut"] = t.struct(
        {
            "resources": t.struct({"_": t.string().optional()}).optional(),
            "methods": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestResourceOut"])
    types["DirectoryListIn"] = t.struct(
        {
            "items": t.array(
                t.struct(
                    {
                        "kind": t.string().optional(),
                        "documentationLink": t.string().optional(),
                        "description": t.string().optional(),
                        "name": t.string().optional(),
                        "preferred": t.boolean().optional(),
                        "discoveryLink": t.string().optional(),
                        "version": t.string().optional(),
                        "id": t.string().optional(),
                        "title": t.string().optional(),
                        "labels": t.array(t.string()).optional(),
                        "discoveryRestUrl": t.string().optional(),
                        "icons": t.struct(
                            {"x16": t.string().optional(), "x32": t.string().optional()}
                        ).optional(),
                    }
                )
            ).optional(),
            "discoveryVersion": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DirectoryListIn"])
    types["DirectoryListOut"] = t.struct(
        {
            "items": t.array(
                t.struct(
                    {
                        "kind": t.string().optional(),
                        "documentationLink": t.string().optional(),
                        "description": t.string().optional(),
                        "name": t.string().optional(),
                        "preferred": t.boolean().optional(),
                        "discoveryLink": t.string().optional(),
                        "version": t.string().optional(),
                        "id": t.string().optional(),
                        "title": t.string().optional(),
                        "labels": t.array(t.string()).optional(),
                        "discoveryRestUrl": t.string().optional(),
                        "icons": t.struct(
                            {"x16": t.string().optional(), "x32": t.string().optional()}
                        ).optional(),
                    }
                )
            ).optional(),
            "discoveryVersion": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DirectoryListOut"])

    functions = {}
    functions["apisGetRest"] = discovery.get(
        "apis",
        t.struct(
            {
                "preferred": t.boolean().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DirectoryListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["apisList"] = discovery.get(
        "apis",
        t.struct(
            {
                "preferred": t.boolean().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DirectoryListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="discovery",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
