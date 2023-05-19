from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_keep() -> Import:
    keep = HTTPRuntime("https://keep.googleapis.com/")

    renames = {
        "ErrorResponse": "_keep_1_ErrorResponse",
        "ListContentIn": "_keep_2_ListContentIn",
        "ListContentOut": "_keep_3_ListContentOut",
        "NoteIn": "_keep_4_NoteIn",
        "NoteOut": "_keep_5_NoteOut",
        "EmptyIn": "_keep_6_EmptyIn",
        "EmptyOut": "_keep_7_EmptyOut",
        "BatchCreatePermissionsResponseIn": "_keep_8_BatchCreatePermissionsResponseIn",
        "BatchCreatePermissionsResponseOut": "_keep_9_BatchCreatePermissionsResponseOut",
        "ListItemIn": "_keep_10_ListItemIn",
        "ListItemOut": "_keep_11_ListItemOut",
        "TextContentIn": "_keep_12_TextContentIn",
        "TextContentOut": "_keep_13_TextContentOut",
        "FamilyIn": "_keep_14_FamilyIn",
        "FamilyOut": "_keep_15_FamilyOut",
        "GroupIn": "_keep_16_GroupIn",
        "GroupOut": "_keep_17_GroupOut",
        "CreatePermissionRequestIn": "_keep_18_CreatePermissionRequestIn",
        "CreatePermissionRequestOut": "_keep_19_CreatePermissionRequestOut",
        "UserIn": "_keep_20_UserIn",
        "UserOut": "_keep_21_UserOut",
        "BatchDeletePermissionsRequestIn": "_keep_22_BatchDeletePermissionsRequestIn",
        "BatchDeletePermissionsRequestOut": "_keep_23_BatchDeletePermissionsRequestOut",
        "ListNotesResponseIn": "_keep_24_ListNotesResponseIn",
        "ListNotesResponseOut": "_keep_25_ListNotesResponseOut",
        "SectionIn": "_keep_26_SectionIn",
        "SectionOut": "_keep_27_SectionOut",
        "AttachmentIn": "_keep_28_AttachmentIn",
        "AttachmentOut": "_keep_29_AttachmentOut",
        "PermissionIn": "_keep_30_PermissionIn",
        "PermissionOut": "_keep_31_PermissionOut",
        "BatchCreatePermissionsRequestIn": "_keep_32_BatchCreatePermissionsRequestIn",
        "BatchCreatePermissionsRequestOut": "_keep_33_BatchCreatePermissionsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListContentIn"] = t.struct(
        {"listItems": t.array(t.proxy(renames["ListItemIn"])).optional()}
    ).named(renames["ListContentIn"])
    types["ListContentOut"] = t.struct(
        {
            "listItems": t.array(t.proxy(renames["ListItemOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListContentOut"])
    types["NoteIn"] = t.struct(
        {
            "title": t.string().optional(),
            "body": t.proxy(renames["SectionIn"]).optional(),
        }
    ).named(renames["NoteIn"])
    types["NoteOut"] = t.struct(
        {
            "title": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "attachments": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "trashed": t.boolean().optional(),
            "body": t.proxy(renames["SectionOut"]).optional(),
            "trashTime": t.string().optional(),
            "permissions": t.array(t.proxy(renames["PermissionOut"])).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoteOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["BatchCreatePermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.proxy(renames["PermissionIn"])).optional()}
    ).named(renames["BatchCreatePermissionsResponseIn"])
    types["BatchCreatePermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.proxy(renames["PermissionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreatePermissionsResponseOut"])
    types["ListItemIn"] = t.struct(
        {
            "childListItems": t.array(t.proxy(renames["ListItemIn"])).optional(),
            "text": t.proxy(renames["TextContentIn"]).optional(),
            "checked": t.boolean().optional(),
        }
    ).named(renames["ListItemIn"])
    types["ListItemOut"] = t.struct(
        {
            "childListItems": t.array(t.proxy(renames["ListItemOut"])).optional(),
            "text": t.proxy(renames["TextContentOut"]).optional(),
            "checked": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListItemOut"])
    types["TextContentIn"] = t.struct({"text": t.string().optional()}).named(
        renames["TextContentIn"]
    )
    types["TextContentOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextContentOut"])
    types["FamilyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FamilyIn"]
    )
    types["FamilyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FamilyOut"])
    types["GroupIn"] = t.struct({"email": t.string().optional()}).named(
        renames["GroupIn"]
    )
    types["GroupOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["CreatePermissionRequestIn"] = t.struct(
        {"parent": t.string(), "permission": t.proxy(renames["PermissionIn"])}
    ).named(renames["CreatePermissionRequestIn"])
    types["CreatePermissionRequestOut"] = t.struct(
        {
            "parent": t.string(),
            "permission": t.proxy(renames["PermissionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreatePermissionRequestOut"])
    types["UserIn"] = t.struct({"email": t.string().optional()}).named(
        renames["UserIn"]
    )
    types["UserOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["BatchDeletePermissionsRequestIn"] = t.struct(
        {"names": t.array(t.string())}
    ).named(renames["BatchDeletePermissionsRequestIn"])
    types["BatchDeletePermissionsRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeletePermissionsRequestOut"])
    types["ListNotesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "notes": t.array(t.proxy(renames["NoteIn"])).optional(),
        }
    ).named(renames["ListNotesResponseIn"])
    types["ListNotesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "notes": t.array(t.proxy(renames["NoteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNotesResponseOut"])
    types["SectionIn"] = t.struct(
        {
            "text": t.proxy(renames["TextContentIn"]).optional(),
            "list": t.proxy(renames["ListContentIn"]).optional(),
        }
    ).named(renames["SectionIn"])
    types["SectionOut"] = t.struct(
        {
            "text": t.proxy(renames["TextContentOut"]).optional(),
            "list": t.proxy(renames["ListContentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SectionOut"])
    types["AttachmentIn"] = t.struct(
        {"name": t.string().optional(), "mimeType": t.array(t.string()).optional()}
    ).named(renames["AttachmentIn"])
    types["AttachmentOut"] = t.struct(
        {
            "name": t.string().optional(),
            "mimeType": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
    types["PermissionIn"] = t.struct(
        {"email": t.string().optional(), "role": t.string().optional()}
    ).named(renames["PermissionIn"])
    types["PermissionOut"] = t.struct(
        {
            "family": t.proxy(renames["FamilyOut"]).optional(),
            "group": t.proxy(renames["GroupOut"]).optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "name": t.string().optional(),
            "email": t.string().optional(),
            "role": t.string().optional(),
            "deleted": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionOut"])
    types["BatchCreatePermissionsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["CreatePermissionRequestIn"])).optional()}
    ).named(renames["BatchCreatePermissionsRequestIn"])
    types["BatchCreatePermissionsRequestOut"] = t.struct(
        {
            "requests": t.array(
                t.proxy(renames["CreatePermissionRequestOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreatePermissionsRequestOut"])

    functions = {}
    functions["notesCreate"] = keep.get(
        "v1/notes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notesDelete"] = keep.get(
        "v1/notes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notesGet"] = keep.get(
        "v1/notes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notesList"] = keep.get(
        "v1/notes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notesPermissionsBatchDelete"] = keep.post(
        "v1/{parent}/permissions:batchCreate",
        t.struct(
            {
                "parent": t.string().optional(),
                "requests": t.array(
                    t.proxy(renames["CreatePermissionRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchCreatePermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notesPermissionsBatchCreate"] = keep.post(
        "v1/{parent}/permissions:batchCreate",
        t.struct(
            {
                "parent": t.string().optional(),
                "requests": t.array(
                    t.proxy(renames["CreatePermissionRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchCreatePermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mediaDownload"] = keep.get(
        "v1/{name}",
        t.struct(
            {
                "mimeType": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttachmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="keep", renames=renames, types=Box(types), functions=Box(functions)
    )
