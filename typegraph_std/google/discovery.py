from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_discovery():
    discovery = HTTPRuntime("https://www.googleapis.com/")

    renames = {
        "ErrorResponse": "_discovery_1_ErrorResponse",
        "JsonSchemaIn": "_discovery_2_JsonSchemaIn",
        "JsonSchemaOut": "_discovery_3_JsonSchemaOut",
        "RestResourceIn": "_discovery_4_RestResourceIn",
        "RestResourceOut": "_discovery_5_RestResourceOut",
        "RestMethodIn": "_discovery_6_RestMethodIn",
        "RestMethodOut": "_discovery_7_RestMethodOut",
        "RestDescriptionIn": "_discovery_8_RestDescriptionIn",
        "RestDescriptionOut": "_discovery_9_RestDescriptionOut",
        "DirectoryListIn": "_discovery_10_DirectoryListIn",
        "DirectoryListOut": "_discovery_11_DirectoryListOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["JsonSchemaIn"] = t.struct(
        {
            "annotations": t.struct(
                {"required": t.array(t.string()).optional()}
            ).optional(),
            "enum": t.array(t.string()).optional(),
            "maximum": t.string().optional(),
            "pattern": t.string().optional(),
            "location": t.string().optional(),
            "id": t.string().optional(),
            "enumDescriptions": t.array(t.string()).optional(),
            "default": t.string().optional(),
            "description": t.string().optional(),
            "variant": t.struct(
                {
                    "discriminant": t.string().optional(),
                    "map": t.array(
                        t.struct({"$ref": t.string(), "type_value": t.string()})
                    ).optional(),
                }
            ).optional(),
            "required": t.boolean().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "repeated": t.boolean().optional(),
            "items": t.proxy(renames["JsonSchemaIn"]).optional(),
            "additionalProperties": t.proxy(renames["JsonSchemaIn"]).optional(),
            "type": t.string().optional(),
            "$ref": t.string().optional(),
            "minimum": t.string().optional(),
            "format": t.string().optional(),
            "readOnly": t.boolean().optional(),
        }
    ).named(renames["JsonSchemaIn"])
    types["JsonSchemaOut"] = t.struct(
        {
            "annotations": t.struct(
                {"required": t.array(t.string()).optional()}
            ).optional(),
            "enum": t.array(t.string()).optional(),
            "maximum": t.string().optional(),
            "pattern": t.string().optional(),
            "location": t.string().optional(),
            "id": t.string().optional(),
            "enumDescriptions": t.array(t.string()).optional(),
            "default": t.string().optional(),
            "description": t.string().optional(),
            "variant": t.struct(
                {
                    "discriminant": t.string().optional(),
                    "map": t.array(
                        t.struct({"$ref": t.string(), "type_value": t.string()})
                    ).optional(),
                }
            ).optional(),
            "required": t.boolean().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "repeated": t.boolean().optional(),
            "items": t.proxy(renames["JsonSchemaOut"]).optional(),
            "additionalProperties": t.proxy(renames["JsonSchemaOut"]).optional(),
            "type": t.string().optional(),
            "$ref": t.string().optional(),
            "minimum": t.string().optional(),
            "format": t.string().optional(),
            "readOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JsonSchemaOut"])
    types["RestResourceIn"] = t.struct(
        {
            "methods": t.struct({"_": t.string().optional()}).optional(),
            "resources": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RestResourceIn"])
    types["RestResourceOut"] = t.struct(
        {
            "methods": t.struct({"_": t.string().optional()}).optional(),
            "resources": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestResourceOut"])
    types["RestMethodIn"] = t.struct(
        {
            "id": t.string().optional(),
            "etagRequired": t.boolean().optional(),
            "scopes": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "parameterOrder": t.array(t.string()).optional(),
            "supportsMediaDownload": t.boolean().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "supportsSubscription": t.boolean().optional(),
            "httpMethod": t.string().optional(),
            "flatPath": t.string().optional(),
            "path": t.string().optional(),
            "useMediaDownloadService": t.boolean().optional(),
            "mediaUpload": t.struct(
                {
                    "protocols": t.struct(
                        {
                            "simple": t.struct(
                                {
                                    "path": t.string().optional(),
                                    "multipart": t.boolean().optional(),
                                }
                            ).optional(),
                            "resumable": t.struct(
                                {
                                    "multipart": t.boolean().optional(),
                                    "path": t.string().optional(),
                                }
                            ).optional(),
                        }
                    ).optional(),
                    "maxSize": t.string().optional(),
                    "accept": t.array(t.string()).optional(),
                }
            ).optional(),
            "request": t.struct(
                {"$ref": t.string().optional(), "parameterName": t.string().optional()}
            ).optional(),
            "response": t.struct({"$ref": t.string().optional()}).optional(),
            "supportsMediaUpload": t.boolean().optional(),
        }
    ).named(renames["RestMethodIn"])
    types["RestMethodOut"] = t.struct(
        {
            "id": t.string().optional(),
            "etagRequired": t.boolean().optional(),
            "scopes": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "parameterOrder": t.array(t.string()).optional(),
            "supportsMediaDownload": t.boolean().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "supportsSubscription": t.boolean().optional(),
            "httpMethod": t.string().optional(),
            "flatPath": t.string().optional(),
            "path": t.string().optional(),
            "useMediaDownloadService": t.boolean().optional(),
            "mediaUpload": t.struct(
                {
                    "protocols": t.struct(
                        {
                            "simple": t.struct(
                                {
                                    "path": t.string().optional(),
                                    "multipart": t.boolean().optional(),
                                }
                            ).optional(),
                            "resumable": t.struct(
                                {
                                    "multipart": t.boolean().optional(),
                                    "path": t.string().optional(),
                                }
                            ).optional(),
                        }
                    ).optional(),
                    "maxSize": t.string().optional(),
                    "accept": t.array(t.string()).optional(),
                }
            ).optional(),
            "request": t.struct(
                {"$ref": t.string().optional(), "parameterName": t.string().optional()}
            ).optional(),
            "response": t.struct({"$ref": t.string().optional()}).optional(),
            "supportsMediaUpload": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestMethodOut"])
    types["RestDescriptionIn"] = t.struct(
        {
            "batchPath": t.string().optional(),
            "resources": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
            "packagePath": t.string().optional(),
            "basePath": t.string().optional(),
            "kind": t.string().optional(),
            "description": t.string().optional(),
            "protocol": t.string().optional(),
            "documentationLink": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "canonicalName": t.string().optional(),
            "ownerName": t.string().optional(),
            "methods": t.struct({"_": t.string().optional()}).optional(),
            "auth": t.struct(
                {
                    "oauth2": t.struct(
                        {"scopes": t.struct({"_": t.string().optional()}).optional()}
                    ).optional()
                }
            ).optional(),
            "revision": t.string().optional(),
            "baseUrl": t.string().optional(),
            "id": t.string().optional(),
            "ownerDomain": t.string().optional(),
            "name": t.string().optional(),
            "schemas": t.struct({"_": t.string().optional()}).optional(),
            "servicePath": t.string().optional(),
            "rootUrl": t.string().optional(),
            "icons": t.struct(
                {"x32": t.string().optional(), "x16": t.string().optional()}
            ).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "version_module": t.boolean(),
            "labels": t.array(t.string()).optional(),
            "discoveryVersion": t.string().optional(),
            "version": t.string().optional(),
            "exponentialBackoffDefault": t.boolean().optional(),
        }
    ).named(renames["RestDescriptionIn"])
    types["RestDescriptionOut"] = t.struct(
        {
            "batchPath": t.string().optional(),
            "resources": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
            "packagePath": t.string().optional(),
            "basePath": t.string().optional(),
            "kind": t.string().optional(),
            "description": t.string().optional(),
            "protocol": t.string().optional(),
            "documentationLink": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "canonicalName": t.string().optional(),
            "etag": t.string().optional(),
            "ownerName": t.string().optional(),
            "methods": t.struct({"_": t.string().optional()}).optional(),
            "auth": t.struct(
                {
                    "oauth2": t.struct(
                        {"scopes": t.struct({"_": t.string().optional()}).optional()}
                    ).optional()
                }
            ).optional(),
            "revision": t.string().optional(),
            "baseUrl": t.string().optional(),
            "id": t.string().optional(),
            "ownerDomain": t.string().optional(),
            "name": t.string().optional(),
            "schemas": t.struct({"_": t.string().optional()}).optional(),
            "servicePath": t.string().optional(),
            "rootUrl": t.string().optional(),
            "icons": t.struct(
                {"x32": t.string().optional(), "x16": t.string().optional()}
            ).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "version_module": t.boolean(),
            "labels": t.array(t.string()).optional(),
            "discoveryVersion": t.string().optional(),
            "version": t.string().optional(),
            "exponentialBackoffDefault": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestDescriptionOut"])
    types["DirectoryListIn"] = t.struct(
        {
            "discoveryVersion": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(
                t.struct(
                    {
                        "discoveryLink": t.string().optional(),
                        "version": t.string().optional(),
                        "id": t.string().optional(),
                        "title": t.string().optional(),
                        "kind": t.string().optional(),
                        "icons": t.struct(
                            {"x16": t.string().optional(), "x32": t.string().optional()}
                        ).optional(),
                        "discoveryRestUrl": t.string().optional(),
                        "name": t.string().optional(),
                        "labels": t.array(t.string()).optional(),
                        "preferred": t.boolean().optional(),
                        "description": t.string().optional(),
                        "documentationLink": t.string().optional(),
                    }
                )
            ).optional(),
        }
    ).named(renames["DirectoryListIn"])
    types["DirectoryListOut"] = t.struct(
        {
            "discoveryVersion": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(
                t.struct(
                    {
                        "discoveryLink": t.string().optional(),
                        "version": t.string().optional(),
                        "id": t.string().optional(),
                        "title": t.string().optional(),
                        "kind": t.string().optional(),
                        "icons": t.struct(
                            {"x16": t.string().optional(), "x32": t.string().optional()}
                        ).optional(),
                        "discoveryRestUrl": t.string().optional(),
                        "name": t.string().optional(),
                        "labels": t.array(t.string()).optional(),
                        "preferred": t.boolean().optional(),
                        "description": t.string().optional(),
                        "documentationLink": t.string().optional(),
                    }
                )
            ).optional(),
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
