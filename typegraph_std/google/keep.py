from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_keep() -> Import:
    keep = HTTPRuntime("https://keep.googleapis.com/")

    renames = {
        "ErrorResponse": "_keep_1_ErrorResponse",
        "BatchDeletePermissionsRequestIn": "_keep_2_BatchDeletePermissionsRequestIn",
        "BatchDeletePermissionsRequestOut": "_keep_3_BatchDeletePermissionsRequestOut",
        "EmptyIn": "_keep_4_EmptyIn",
        "EmptyOut": "_keep_5_EmptyOut",
        "BatchCreatePermissionsResponseIn": "_keep_6_BatchCreatePermissionsResponseIn",
        "BatchCreatePermissionsResponseOut": "_keep_7_BatchCreatePermissionsResponseOut",
        "GroupIn": "_keep_8_GroupIn",
        "GroupOut": "_keep_9_GroupOut",
        "PermissionIn": "_keep_10_PermissionIn",
        "PermissionOut": "_keep_11_PermissionOut",
        "UserIn": "_keep_12_UserIn",
        "UserOut": "_keep_13_UserOut",
        "FamilyIn": "_keep_14_FamilyIn",
        "FamilyOut": "_keep_15_FamilyOut",
        "ListNotesResponseIn": "_keep_16_ListNotesResponseIn",
        "ListNotesResponseOut": "_keep_17_ListNotesResponseOut",
        "CreatePermissionRequestIn": "_keep_18_CreatePermissionRequestIn",
        "CreatePermissionRequestOut": "_keep_19_CreatePermissionRequestOut",
        "AttachmentIn": "_keep_20_AttachmentIn",
        "AttachmentOut": "_keep_21_AttachmentOut",
        "ListContentIn": "_keep_22_ListContentIn",
        "ListContentOut": "_keep_23_ListContentOut",
        "ListItemIn": "_keep_24_ListItemIn",
        "ListItemOut": "_keep_25_ListItemOut",
        "SectionIn": "_keep_26_SectionIn",
        "SectionOut": "_keep_27_SectionOut",
        "TextContentIn": "_keep_28_TextContentIn",
        "TextContentOut": "_keep_29_TextContentOut",
        "BatchCreatePermissionsRequestIn": "_keep_30_BatchCreatePermissionsRequestIn",
        "BatchCreatePermissionsRequestOut": "_keep_31_BatchCreatePermissionsRequestOut",
        "NoteIn": "_keep_32_NoteIn",
        "NoteOut": "_keep_33_NoteOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BatchDeletePermissionsRequestIn"] = t.struct(
        {"names": t.array(t.string())}
    ).named(renames["BatchDeletePermissionsRequestIn"])
    types["BatchDeletePermissionsRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeletePermissionsRequestOut"])
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
    types["GroupIn"] = t.struct({"email": t.string().optional()}).named(
        renames["GroupIn"]
    )
    types["GroupOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["PermissionIn"] = t.struct(
        {"email": t.string().optional(), "role": t.string().optional()}
    ).named(renames["PermissionIn"])
    types["PermissionOut"] = t.struct(
        {
            "group": t.proxy(renames["GroupOut"]).optional(),
            "email": t.string().optional(),
            "deleted": t.boolean().optional(),
            "role": t.string().optional(),
            "family": t.proxy(renames["FamilyOut"]).optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionOut"])
    types["UserIn"] = t.struct({"email": t.string().optional()}).named(
        renames["UserIn"]
    )
    types["UserOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["FamilyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FamilyIn"]
    )
    types["FamilyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FamilyOut"])
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
    types["ListContentIn"] = t.struct(
        {"listItems": t.array(t.proxy(renames["ListItemIn"])).optional()}
    ).named(renames["ListContentIn"])
    types["ListContentOut"] = t.struct(
        {
            "listItems": t.array(t.proxy(renames["ListItemOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListContentOut"])
    types["ListItemIn"] = t.struct(
        {
            "checked": t.boolean().optional(),
            "text": t.proxy(renames["TextContentIn"]).optional(),
            "childListItems": t.array(t.proxy(renames["ListItemIn"])).optional(),
        }
    ).named(renames["ListItemIn"])
    types["ListItemOut"] = t.struct(
        {
            "checked": t.boolean().optional(),
            "text": t.proxy(renames["TextContentOut"]).optional(),
            "childListItems": t.array(t.proxy(renames["ListItemOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListItemOut"])
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
    types["NoteIn"] = t.struct(
        {
            "body": t.proxy(renames["SectionIn"]).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["NoteIn"])
    types["NoteOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "trashTime": t.string().optional(),
            "attachments": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "updateTime": t.string().optional(),
            "permissions": t.array(t.proxy(renames["PermissionOut"])).optional(),
            "body": t.proxy(renames["SectionOut"]).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "trashed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoteOut"])

    functions = {}
    functions["mediaDownload"] = keep.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttachmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notesList"] = keep.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notesCreate"] = keep.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notesDelete"] = keep.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notesGet"] = keep.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NoteOut"]),
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

    return Import(
        importer="keep", renames=renames, types=Box(types), functions=Box(functions)
    )
