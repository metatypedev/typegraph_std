from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_keep() -> Import:
    keep = HTTPRuntime("https://keep.googleapis.com/")

    renames = {
        "ErrorResponse": "_keep_1_ErrorResponse",
        "ListItemIn": "_keep_2_ListItemIn",
        "ListItemOut": "_keep_3_ListItemOut",
        "NoteIn": "_keep_4_NoteIn",
        "NoteOut": "_keep_5_NoteOut",
        "EmptyIn": "_keep_6_EmptyIn",
        "EmptyOut": "_keep_7_EmptyOut",
        "TextContentIn": "_keep_8_TextContentIn",
        "TextContentOut": "_keep_9_TextContentOut",
        "BatchCreatePermissionsResponseIn": "_keep_10_BatchCreatePermissionsResponseIn",
        "BatchCreatePermissionsResponseOut": "_keep_11_BatchCreatePermissionsResponseOut",
        "SectionIn": "_keep_12_SectionIn",
        "SectionOut": "_keep_13_SectionOut",
        "AttachmentIn": "_keep_14_AttachmentIn",
        "AttachmentOut": "_keep_15_AttachmentOut",
        "GroupIn": "_keep_16_GroupIn",
        "GroupOut": "_keep_17_GroupOut",
        "BatchDeletePermissionsRequestIn": "_keep_18_BatchDeletePermissionsRequestIn",
        "BatchDeletePermissionsRequestOut": "_keep_19_BatchDeletePermissionsRequestOut",
        "FamilyIn": "_keep_20_FamilyIn",
        "FamilyOut": "_keep_21_FamilyOut",
        "ListNotesResponseIn": "_keep_22_ListNotesResponseIn",
        "ListNotesResponseOut": "_keep_23_ListNotesResponseOut",
        "CreatePermissionRequestIn": "_keep_24_CreatePermissionRequestIn",
        "CreatePermissionRequestOut": "_keep_25_CreatePermissionRequestOut",
        "ListContentIn": "_keep_26_ListContentIn",
        "ListContentOut": "_keep_27_ListContentOut",
        "PermissionIn": "_keep_28_PermissionIn",
        "PermissionOut": "_keep_29_PermissionOut",
        "UserIn": "_keep_30_UserIn",
        "UserOut": "_keep_31_UserOut",
        "BatchCreatePermissionsRequestIn": "_keep_32_BatchCreatePermissionsRequestIn",
        "BatchCreatePermissionsRequestOut": "_keep_33_BatchCreatePermissionsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["NoteIn"] = t.struct(
        {
            "body": t.proxy(renames["SectionIn"]).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["NoteIn"])
    types["NoteOut"] = t.struct(
        {
            "body": t.proxy(renames["SectionOut"]).optional(),
            "title": t.string().optional(),
            "trashed": t.boolean().optional(),
            "permissions": t.array(t.proxy(renames["PermissionOut"])).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "attachments": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "name": t.string().optional(),
            "trashTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoteOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TextContentIn"] = t.struct({"text": t.string().optional()}).named(
        renames["TextContentIn"]
    )
    types["TextContentOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextContentOut"])
    types["BatchCreatePermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.proxy(renames["PermissionIn"])).optional()}
    ).named(renames["BatchCreatePermissionsResponseIn"])
    types["BatchCreatePermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.proxy(renames["PermissionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreatePermissionsResponseOut"])
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
    types["GroupIn"] = t.struct({"email": t.string().optional()}).named(
        renames["GroupIn"]
    )
    types["GroupOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["BatchDeletePermissionsRequestIn"] = t.struct(
        {"names": t.array(t.string())}
    ).named(renames["BatchDeletePermissionsRequestIn"])
    types["BatchDeletePermissionsRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeletePermissionsRequestOut"])
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
    types["ListContentIn"] = t.struct(
        {"listItems": t.array(t.proxy(renames["ListItemIn"])).optional()}
    ).named(renames["ListContentIn"])
    types["ListContentOut"] = t.struct(
        {
            "listItems": t.array(t.proxy(renames["ListItemOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListContentOut"])
    types["PermissionIn"] = t.struct(
        {"role": t.string().optional(), "email": t.string().optional()}
    ).named(renames["PermissionIn"])
    types["PermissionOut"] = t.struct(
        {
            "role": t.string().optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "group": t.proxy(renames["GroupOut"]).optional(),
            "email": t.string().optional(),
            "deleted": t.boolean().optional(),
            "name": t.string().optional(),
            "family": t.proxy(renames["FamilyOut"]).optional(),
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
    functions["notesList"] = keep.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notesGet"] = keep.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notesCreate"] = keep.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notesDelete"] = keep.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
                "name": t.string(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttachmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="keep", renames=renames, types=types, functions=functions)
