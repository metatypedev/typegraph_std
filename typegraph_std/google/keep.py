from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_keep():
    keep = HTTPRuntime("https://keep.googleapis.com/")

    renames = {
        "ErrorResponse": "_keep_1_ErrorResponse",
        "PermissionIn": "_keep_2_PermissionIn",
        "PermissionOut": "_keep_3_PermissionOut",
        "CreatePermissionRequestIn": "_keep_4_CreatePermissionRequestIn",
        "CreatePermissionRequestOut": "_keep_5_CreatePermissionRequestOut",
        "TextContentIn": "_keep_6_TextContentIn",
        "TextContentOut": "_keep_7_TextContentOut",
        "BatchCreatePermissionsRequestIn": "_keep_8_BatchCreatePermissionsRequestIn",
        "BatchCreatePermissionsRequestOut": "_keep_9_BatchCreatePermissionsRequestOut",
        "ListItemIn": "_keep_10_ListItemIn",
        "ListItemOut": "_keep_11_ListItemOut",
        "FamilyIn": "_keep_12_FamilyIn",
        "FamilyOut": "_keep_13_FamilyOut",
        "ListContentIn": "_keep_14_ListContentIn",
        "ListContentOut": "_keep_15_ListContentOut",
        "EmptyIn": "_keep_16_EmptyIn",
        "EmptyOut": "_keep_17_EmptyOut",
        "GroupIn": "_keep_18_GroupIn",
        "GroupOut": "_keep_19_GroupOut",
        "BatchCreatePermissionsResponseIn": "_keep_20_BatchCreatePermissionsResponseIn",
        "BatchCreatePermissionsResponseOut": "_keep_21_BatchCreatePermissionsResponseOut",
        "AttachmentIn": "_keep_22_AttachmentIn",
        "AttachmentOut": "_keep_23_AttachmentOut",
        "NoteIn": "_keep_24_NoteIn",
        "NoteOut": "_keep_25_NoteOut",
        "ListNotesResponseIn": "_keep_26_ListNotesResponseIn",
        "ListNotesResponseOut": "_keep_27_ListNotesResponseOut",
        "BatchDeletePermissionsRequestIn": "_keep_28_BatchDeletePermissionsRequestIn",
        "BatchDeletePermissionsRequestOut": "_keep_29_BatchDeletePermissionsRequestOut",
        "UserIn": "_keep_30_UserIn",
        "UserOut": "_keep_31_UserOut",
        "SectionIn": "_keep_32_SectionIn",
        "SectionOut": "_keep_33_SectionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PermissionIn"] = t.struct(
        {"email": t.string().optional(), "role": t.string().optional()}
    ).named(renames["PermissionIn"])
    types["PermissionOut"] = t.struct(
        {
            "deleted": t.boolean().optional(),
            "email": t.string().optional(),
            "family": t.proxy(renames["FamilyOut"]).optional(),
            "role": t.string().optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "group": t.proxy(renames["GroupOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionOut"])
    types["CreatePermissionRequestIn"] = t.struct(
        {"permission": t.proxy(renames["PermissionIn"]), "parent": t.string()}
    ).named(renames["CreatePermissionRequestIn"])
    types["CreatePermissionRequestOut"] = t.struct(
        {
            "permission": t.proxy(renames["PermissionOut"]),
            "parent": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreatePermissionRequestOut"])
    types["TextContentIn"] = t.struct({"text": t.string().optional()}).named(
        renames["TextContentIn"]
    )
    types["TextContentOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextContentOut"])
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
    types["ListItemIn"] = t.struct(
        {
            "text": t.proxy(renames["TextContentIn"]).optional(),
            "childListItems": t.array(t.proxy(renames["ListItemIn"])).optional(),
            "checked": t.boolean().optional(),
        }
    ).named(renames["ListItemIn"])
    types["ListItemOut"] = t.struct(
        {
            "text": t.proxy(renames["TextContentOut"]).optional(),
            "childListItems": t.array(t.proxy(renames["ListItemOut"])).optional(),
            "checked": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListItemOut"])
    types["FamilyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FamilyIn"]
    )
    types["FamilyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FamilyOut"])
    types["ListContentIn"] = t.struct(
        {"listItems": t.array(t.proxy(renames["ListItemIn"])).optional()}
    ).named(renames["ListContentIn"])
    types["ListContentOut"] = t.struct(
        {
            "listItems": t.array(t.proxy(renames["ListItemOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListContentOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GroupIn"] = t.struct({"email": t.string().optional()}).named(
        renames["GroupIn"]
    )
    types["GroupOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["BatchCreatePermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.proxy(renames["PermissionIn"])).optional()}
    ).named(renames["BatchCreatePermissionsResponseIn"])
    types["BatchCreatePermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.proxy(renames["PermissionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreatePermissionsResponseOut"])
    types["AttachmentIn"] = t.struct(
        {"mimeType": t.array(t.string()).optional(), "name": t.string().optional()}
    ).named(renames["AttachmentIn"])
    types["AttachmentOut"] = t.struct(
        {
            "mimeType": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
    types["NoteIn"] = t.struct(
        {
            "title": t.string().optional(),
            "body": t.proxy(renames["SectionIn"]).optional(),
        }
    ).named(renames["NoteIn"])
    types["NoteOut"] = t.struct(
        {
            "permissions": t.array(t.proxy(renames["PermissionOut"])).optional(),
            "updateTime": t.string().optional(),
            "trashTime": t.string().optional(),
            "attachments": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "createTime": t.string().optional(),
            "title": t.string().optional(),
            "body": t.proxy(renames["SectionOut"]).optional(),
            "trashed": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoteOut"])
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
    types["BatchDeletePermissionsRequestIn"] = t.struct(
        {"names": t.array(t.string())}
    ).named(renames["BatchDeletePermissionsRequestIn"])
    types["BatchDeletePermissionsRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeletePermissionsRequestOut"])
    types["UserIn"] = t.struct({"email": t.string().optional()}).named(
        renames["UserIn"]
    )
    types["UserOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
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

    functions = {}
    functions["notesList"] = keep.post(
        "v1/notes",
        t.struct(
            {
                "title": t.string().optional(),
                "body": t.proxy(renames["SectionIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notesDelete"] = keep.post(
        "v1/notes",
        t.struct(
            {
                "title": t.string().optional(),
                "body": t.proxy(renames["SectionIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notesGet"] = keep.post(
        "v1/notes",
        t.struct(
            {
                "title": t.string().optional(),
                "body": t.proxy(renames["SectionIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notesCreate"] = keep.post(
        "v1/notes",
        t.struct(
            {
                "title": t.string().optional(),
                "body": t.proxy(renames["SectionIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notesPermissionsBatchCreate"] = keep.post(
        "v1/{parent}/permissions:batchDelete",
        t.struct(
            {
                "parent": t.string().optional(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notesPermissionsBatchDelete"] = keep.post(
        "v1/{parent}/permissions:batchDelete",
        t.struct(
            {
                "parent": t.string().optional(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
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
