from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_drive():
    drive = HTTPRuntime("https://www.googleapis.com/")

    renames = {
        "ErrorResponse": "_drive_1_ErrorResponse",
        "ChangeIn": "_drive_2_ChangeIn",
        "ChangeOut": "_drive_3_ChangeOut",
        "LabelFieldIn": "_drive_4_LabelFieldIn",
        "LabelFieldOut": "_drive_5_LabelFieldOut",
        "ModifyLabelsResponseIn": "_drive_6_ModifyLabelsResponseIn",
        "ModifyLabelsResponseOut": "_drive_7_ModifyLabelsResponseOut",
        "ContentRestrictionIn": "_drive_8_ContentRestrictionIn",
        "ContentRestrictionOut": "_drive_9_ContentRestrictionOut",
        "CommentIn": "_drive_10_CommentIn",
        "CommentOut": "_drive_11_CommentOut",
        "RevisionIn": "_drive_12_RevisionIn",
        "RevisionOut": "_drive_13_RevisionOut",
        "FileListIn": "_drive_14_FileListIn",
        "FileListOut": "_drive_15_FileListOut",
        "ReplyListIn": "_drive_16_ReplyListIn",
        "ReplyListOut": "_drive_17_ReplyListOut",
        "ChannelIn": "_drive_18_ChannelIn",
        "ChannelOut": "_drive_19_ChannelOut",
        "LabelListIn": "_drive_20_LabelListIn",
        "LabelListOut": "_drive_21_LabelListOut",
        "DriveIn": "_drive_22_DriveIn",
        "DriveOut": "_drive_23_DriveOut",
        "ReplyIn": "_drive_24_ReplyIn",
        "ReplyOut": "_drive_25_ReplyOut",
        "GeneratedIdsIn": "_drive_26_GeneratedIdsIn",
        "GeneratedIdsOut": "_drive_27_GeneratedIdsOut",
        "ChangeListIn": "_drive_28_ChangeListIn",
        "ChangeListOut": "_drive_29_ChangeListOut",
        "AboutIn": "_drive_30_AboutIn",
        "AboutOut": "_drive_31_AboutOut",
        "FileIn": "_drive_32_FileIn",
        "FileOut": "_drive_33_FileOut",
        "PermissionListIn": "_drive_34_PermissionListIn",
        "PermissionListOut": "_drive_35_PermissionListOut",
        "LabelIn": "_drive_36_LabelIn",
        "LabelOut": "_drive_37_LabelOut",
        "TeamDriveIn": "_drive_38_TeamDriveIn",
        "TeamDriveOut": "_drive_39_TeamDriveOut",
        "RevisionListIn": "_drive_40_RevisionListIn",
        "RevisionListOut": "_drive_41_RevisionListOut",
        "TeamDriveListIn": "_drive_42_TeamDriveListIn",
        "TeamDriveListOut": "_drive_43_TeamDriveListOut",
        "DriveListIn": "_drive_44_DriveListIn",
        "DriveListOut": "_drive_45_DriveListOut",
        "LabelModificationIn": "_drive_46_LabelModificationIn",
        "LabelModificationOut": "_drive_47_LabelModificationOut",
        "StartPageTokenIn": "_drive_48_StartPageTokenIn",
        "StartPageTokenOut": "_drive_49_StartPageTokenOut",
        "LabelFieldModificationIn": "_drive_50_LabelFieldModificationIn",
        "LabelFieldModificationOut": "_drive_51_LabelFieldModificationOut",
        "ModifyLabelsRequestIn": "_drive_52_ModifyLabelsRequestIn",
        "ModifyLabelsRequestOut": "_drive_53_ModifyLabelsRequestOut",
        "CommentListIn": "_drive_54_CommentListIn",
        "CommentListOut": "_drive_55_CommentListOut",
        "PermissionIn": "_drive_56_PermissionIn",
        "PermissionOut": "_drive_57_PermissionOut",
        "UserIn": "_drive_58_UserIn",
        "UserOut": "_drive_59_UserOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ChangeIn"] = t.struct(
        {
            "removed": t.boolean().optional(),
            "changeType": t.string().optional(),
            "kind": t.string().optional(),
            "teamDriveId": t.string().optional(),
            "driveId": t.string().optional(),
            "teamDrive": t.proxy(renames["TeamDriveIn"]).optional(),
            "fileId": t.string().optional(),
            "time": t.string().optional(),
            "type": t.string().optional(),
            "file": t.proxy(renames["FileIn"]).optional(),
            "drive": t.proxy(renames["DriveIn"]).optional(),
        }
    ).named(renames["ChangeIn"])
    types["ChangeOut"] = t.struct(
        {
            "removed": t.boolean().optional(),
            "changeType": t.string().optional(),
            "kind": t.string().optional(),
            "teamDriveId": t.string().optional(),
            "driveId": t.string().optional(),
            "teamDrive": t.proxy(renames["TeamDriveOut"]).optional(),
            "fileId": t.string().optional(),
            "time": t.string().optional(),
            "type": t.string().optional(),
            "file": t.proxy(renames["FileOut"]).optional(),
            "drive": t.proxy(renames["DriveOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChangeOut"])
    types["LabelFieldIn"] = t.struct(
        {
            "user": t.array(t.proxy(renames["UserIn"])).optional(),
            "selection": t.array(t.string()).optional(),
            "dateString": t.array(t.string()).optional(),
            "valueType": t.string().optional(),
            "integer": t.array(t.string()).optional(),
            "text": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LabelFieldIn"])
    types["LabelFieldOut"] = t.struct(
        {
            "user": t.array(t.proxy(renames["UserOut"])).optional(),
            "selection": t.array(t.string()).optional(),
            "dateString": t.array(t.string()).optional(),
            "valueType": t.string().optional(),
            "integer": t.array(t.string()).optional(),
            "text": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelFieldOut"])
    types["ModifyLabelsResponseIn"] = t.struct(
        {
            "modifiedLabels": t.array(t.proxy(renames["LabelIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ModifyLabelsResponseIn"])
    types["ModifyLabelsResponseOut"] = t.struct(
        {
            "modifiedLabels": t.array(t.proxy(renames["LabelOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyLabelsResponseOut"])
    types["ContentRestrictionIn"] = t.struct(
        {
            "reason": t.string().optional(),
            "readOnly": t.boolean().optional(),
            "restrictionTime": t.string().optional(),
            "type": t.string().optional(),
            "restrictingUser": t.proxy(renames["UserIn"]).optional(),
        }
    ).named(renames["ContentRestrictionIn"])
    types["ContentRestrictionOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "readOnly": t.boolean().optional(),
            "restrictionTime": t.string().optional(),
            "type": t.string().optional(),
            "restrictingUser": t.proxy(renames["UserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentRestrictionOut"])
    types["CommentIn"] = t.struct(
        {
            "createdTime": t.string().optional(),
            "modifiedTime": t.string().optional(),
            "quotedFileContent": t.struct(
                {"value": t.string().optional(), "mimeType": t.string().optional()}
            ).optional(),
            "deleted": t.boolean().optional(),
            "anchor": t.string().optional(),
            "content": t.string().optional(),
            "id": t.string().optional(),
            "resolved": t.boolean().optional(),
            "kind": t.string().optional(),
            "htmlContent": t.string().optional(),
            "replies": t.array(t.proxy(renames["ReplyIn"])).optional(),
            "author": t.proxy(renames["UserIn"]).optional(),
        }
    ).named(renames["CommentIn"])
    types["CommentOut"] = t.struct(
        {
            "createdTime": t.string().optional(),
            "modifiedTime": t.string().optional(),
            "quotedFileContent": t.struct(
                {"value": t.string().optional(), "mimeType": t.string().optional()}
            ).optional(),
            "deleted": t.boolean().optional(),
            "anchor": t.string().optional(),
            "content": t.string().optional(),
            "id": t.string().optional(),
            "resolved": t.boolean().optional(),
            "kind": t.string().optional(),
            "htmlContent": t.string().optional(),
            "replies": t.array(t.proxy(renames["ReplyOut"])).optional(),
            "author": t.proxy(renames["UserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentOut"])
    types["RevisionIn"] = t.struct(
        {
            "publishAuto": t.boolean().optional(),
            "lastModifyingUser": t.proxy(renames["UserIn"]).optional(),
            "originalFilename": t.string().optional(),
            "modifiedTime": t.string().optional(),
            "exportLinks": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "publishedLink": t.string().optional(),
            "size": t.string().optional(),
            "mimeType": t.string().optional(),
            "publishedOutsideDomain": t.boolean().optional(),
            "published": t.boolean().optional(),
            "keepForever": t.boolean().optional(),
            "kind": t.string().optional(),
            "md5Checksum": t.string().optional(),
        }
    ).named(renames["RevisionIn"])
    types["RevisionOut"] = t.struct(
        {
            "publishAuto": t.boolean().optional(),
            "lastModifyingUser": t.proxy(renames["UserOut"]).optional(),
            "originalFilename": t.string().optional(),
            "modifiedTime": t.string().optional(),
            "exportLinks": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "publishedLink": t.string().optional(),
            "size": t.string().optional(),
            "mimeType": t.string().optional(),
            "publishedOutsideDomain": t.boolean().optional(),
            "published": t.boolean().optional(),
            "keepForever": t.boolean().optional(),
            "kind": t.string().optional(),
            "md5Checksum": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevisionOut"])
    types["FileListIn"] = t.struct(
        {
            "files": t.array(t.proxy(renames["FileIn"])).optional(),
            "incompleteSearch": t.boolean().optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["FileListIn"])
    types["FileListOut"] = t.struct(
        {
            "files": t.array(t.proxy(renames["FileOut"])).optional(),
            "incompleteSearch": t.boolean().optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileListOut"])
    types["ReplyListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "replies": t.array(t.proxy(renames["ReplyIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ReplyListIn"])
    types["ReplyListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "replies": t.array(t.proxy(renames["ReplyOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplyListOut"])
    types["ChannelIn"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "resourceUri": t.string().optional(),
            "kind": t.string().optional(),
            "token": t.string().optional(),
            "payload": t.boolean().optional(),
            "type": t.string().optional(),
            "expiration": t.string().optional(),
            "address": t.string().optional(),
            "resourceId": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "resourceUri": t.string().optional(),
            "kind": t.string().optional(),
            "token": t.string().optional(),
            "payload": t.boolean().optional(),
            "type": t.string().optional(),
            "expiration": t.string().optional(),
            "address": t.string().optional(),
            "resourceId": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
    types["LabelListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelIn"])).optional(),
        }
    ).named(renames["LabelListIn"])
    types["LabelListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelListOut"])
    types["DriveIn"] = t.struct(
        {
            "id": t.string().optional(),
            "colorRgb": t.string().optional(),
            "name": t.string().optional(),
            "orgUnitId": t.string().optional(),
            "capabilities": t.struct(
                {
                    "canAddChildren": t.boolean().optional(),
                    "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                    "canRenameDrive": t.boolean().optional(),
                    "canComment": t.boolean().optional(),
                    "canRename": t.boolean().optional(),
                    "canListChildren": t.boolean().optional(),
                    "canResetDriveRestrictions": t.boolean().optional(),
                    "canDeleteDrive": t.boolean().optional(),
                    "canTrashChildren": t.boolean().optional(),
                    "canChangeDriveMembersOnlyRestriction": t.boolean().optional(),
                    "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                    "canManageMembers": t.boolean().optional(),
                    "canShare": t.boolean().optional(),
                    "canEdit": t.boolean().optional(),
                    "canDownload": t.boolean().optional(),
                    "canCopy": t.boolean().optional(),
                    "canReadRevisions": t.boolean().optional(),
                    "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                    "canChangeDriveBackground": t.boolean().optional(),
                    "canDeleteChildren": t.boolean().optional(),
                }
            ).optional(),
            "themeId": t.string().optional(),
            "restrictions": t.struct(
                {
                    "domainUsersOnly": t.boolean().optional(),
                    "adminManagedRestrictions": t.boolean().optional(),
                    "driveMembersOnly": t.boolean().optional(),
                    "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                    "copyRequiresWriterPermission": t.boolean().optional(),
                }
            ).optional(),
            "backgroundImageLink": t.string().optional(),
            "kind": t.string().optional(),
            "createdTime": t.string().optional(),
            "hidden": t.boolean().optional(),
            "backgroundImageFile": t.struct(
                {
                    "id": t.string().optional(),
                    "width": t.number().optional(),
                    "xCoordinate": t.number().optional(),
                    "yCoordinate": t.number().optional(),
                }
            ).optional(),
        }
    ).named(renames["DriveIn"])
    types["DriveOut"] = t.struct(
        {
            "id": t.string().optional(),
            "colorRgb": t.string().optional(),
            "name": t.string().optional(),
            "orgUnitId": t.string().optional(),
            "capabilities": t.struct(
                {
                    "canAddChildren": t.boolean().optional(),
                    "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                    "canRenameDrive": t.boolean().optional(),
                    "canComment": t.boolean().optional(),
                    "canRename": t.boolean().optional(),
                    "canListChildren": t.boolean().optional(),
                    "canResetDriveRestrictions": t.boolean().optional(),
                    "canDeleteDrive": t.boolean().optional(),
                    "canTrashChildren": t.boolean().optional(),
                    "canChangeDriveMembersOnlyRestriction": t.boolean().optional(),
                    "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                    "canManageMembers": t.boolean().optional(),
                    "canShare": t.boolean().optional(),
                    "canEdit": t.boolean().optional(),
                    "canDownload": t.boolean().optional(),
                    "canCopy": t.boolean().optional(),
                    "canReadRevisions": t.boolean().optional(),
                    "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                    "canChangeDriveBackground": t.boolean().optional(),
                    "canDeleteChildren": t.boolean().optional(),
                }
            ).optional(),
            "themeId": t.string().optional(),
            "restrictions": t.struct(
                {
                    "domainUsersOnly": t.boolean().optional(),
                    "adminManagedRestrictions": t.boolean().optional(),
                    "driveMembersOnly": t.boolean().optional(),
                    "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                    "copyRequiresWriterPermission": t.boolean().optional(),
                }
            ).optional(),
            "backgroundImageLink": t.string().optional(),
            "kind": t.string().optional(),
            "createdTime": t.string().optional(),
            "hidden": t.boolean().optional(),
            "backgroundImageFile": t.struct(
                {
                    "id": t.string().optional(),
                    "width": t.number().optional(),
                    "xCoordinate": t.number().optional(),
                    "yCoordinate": t.number().optional(),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveOut"])
    types["ReplyIn"] = t.struct(
        {
            "id": t.string().optional(),
            "content": t.string().optional(),
            "kind": t.string().optional(),
            "htmlContent": t.string().optional(),
            "action": t.string().optional(),
            "createdTime": t.string().optional(),
            "deleted": t.boolean().optional(),
            "author": t.proxy(renames["UserIn"]).optional(),
            "modifiedTime": t.string().optional(),
        }
    ).named(renames["ReplyIn"])
    types["ReplyOut"] = t.struct(
        {
            "id": t.string().optional(),
            "content": t.string().optional(),
            "kind": t.string().optional(),
            "htmlContent": t.string().optional(),
            "action": t.string().optional(),
            "createdTime": t.string().optional(),
            "deleted": t.boolean().optional(),
            "author": t.proxy(renames["UserOut"]).optional(),
            "modifiedTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplyOut"])
    types["GeneratedIdsIn"] = t.struct(
        {
            "space": t.string().optional(),
            "ids": t.array(t.string()).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["GeneratedIdsIn"])
    types["GeneratedIdsOut"] = t.struct(
        {
            "space": t.string().optional(),
            "ids": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeneratedIdsOut"])
    types["ChangeListIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "changes": t.array(t.proxy(renames["ChangeIn"])).optional(),
            "newStartPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ChangeListIn"])
    types["ChangeListOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "changes": t.array(t.proxy(renames["ChangeOut"])).optional(),
            "newStartPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChangeListOut"])
    types["AboutIn"] = t.struct(
        {
            "maxUploadSize": t.string().optional(),
            "folderColorPalette": t.array(t.string()).optional(),
            "teamDriveThemes": t.array(
                t.struct(
                    {
                        "id": t.string().optional(),
                        "backgroundImageLink": t.string().optional(),
                        "colorRgb": t.string().optional(),
                    }
                )
            ).optional(),
            "maxImportSizes": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "driveThemes": t.array(
                t.struct(
                    {
                        "colorRgb": t.string().optional(),
                        "id": t.string().optional(),
                        "backgroundImageLink": t.string().optional(),
                    }
                )
            ).optional(),
            "canCreateDrives": t.boolean().optional(),
            "storageQuota": t.struct(
                {
                    "usageInDriveTrash": t.string().optional(),
                    "usageInDrive": t.string().optional(),
                    "limit": t.string().optional(),
                    "usage": t.string().optional(),
                }
            ).optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "exportFormats": t.struct({"_": t.string().optional()}).optional(),
            "appInstalled": t.boolean().optional(),
            "importFormats": t.struct({"_": t.string().optional()}).optional(),
            "canCreateTeamDrives": t.boolean().optional(),
        }
    ).named(renames["AboutIn"])
    types["AboutOut"] = t.struct(
        {
            "maxUploadSize": t.string().optional(),
            "folderColorPalette": t.array(t.string()).optional(),
            "teamDriveThemes": t.array(
                t.struct(
                    {
                        "id": t.string().optional(),
                        "backgroundImageLink": t.string().optional(),
                        "colorRgb": t.string().optional(),
                    }
                )
            ).optional(),
            "maxImportSizes": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "driveThemes": t.array(
                t.struct(
                    {
                        "colorRgb": t.string().optional(),
                        "id": t.string().optional(),
                        "backgroundImageLink": t.string().optional(),
                    }
                )
            ).optional(),
            "canCreateDrives": t.boolean().optional(),
            "storageQuota": t.struct(
                {
                    "usageInDriveTrash": t.string().optional(),
                    "usageInDrive": t.string().optional(),
                    "limit": t.string().optional(),
                    "usage": t.string().optional(),
                }
            ).optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "exportFormats": t.struct({"_": t.string().optional()}).optional(),
            "appInstalled": t.boolean().optional(),
            "importFormats": t.struct({"_": t.string().optional()}).optional(),
            "canCreateTeamDrives": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AboutOut"])
    types["FileIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "hasAugmentedPermissions": t.boolean().optional(),
            "sharingUser": t.proxy(renames["UserIn"]).optional(),
            "id": t.string().optional(),
            "modifiedByMeTime": t.string().optional(),
            "explicitlyTrashed": t.boolean().optional(),
            "thumbnailVersion": t.string().optional(),
            "resourceKey": t.string().optional(),
            "webViewLink": t.string().optional(),
            "shortcutDetails": t.struct(
                {
                    "targetId": t.string().optional(),
                    "targetResourceKey": t.string().optional(),
                    "targetMimeType": t.string().optional(),
                }
            ).optional(),
            "thumbnailLink": t.string().optional(),
            "capabilities": t.struct(
                {
                    "canChangeSecurityUpdateEnabled": t.boolean().optional(),
                    "canReadTeamDrive": t.boolean().optional(),
                    "canMoveItemOutOfDrive": t.boolean().optional(),
                    "canTrash": t.boolean().optional(),
                    "canMoveItemIntoTeamDrive": t.boolean().optional(),
                    "canMoveItemOutOfTeamDrive": t.boolean().optional(),
                    "canModifyContent": t.boolean().optional(),
                    "canMoveChildrenWithinTeamDrive": t.boolean().optional(),
                    "canRemoveChildren": t.boolean().optional(),
                    "canMoveChildrenOutOfDrive": t.boolean().optional(),
                    "canMoveChildrenWithinDrive": t.boolean().optional(),
                    "canEdit": t.boolean().optional(),
                    "canShare": t.boolean().optional(),
                    "canDeleteChildren": t.boolean().optional(),
                    "canMoveTeamDriveItem": t.boolean().optional(),
                    "canAcceptOwnership": t.boolean().optional(),
                    "canAddChildren": t.boolean().optional(),
                    "canComment": t.boolean().optional(),
                    "canCopy": t.boolean().optional(),
                    "canMoveItemWithinTeamDrive": t.boolean().optional(),
                    "canModifyContentRestriction": t.boolean().optional(),
                    "canReadDrive": t.boolean().optional(),
                    "canReadRevisions": t.boolean().optional(),
                    "canUntrash": t.boolean().optional(),
                    "canTrashChildren": t.boolean().optional(),
                    "canDownload": t.boolean().optional(),
                    "canMoveChildrenOutOfTeamDrive": t.boolean().optional(),
                    "canRemoveMyDriveParent": t.boolean().optional(),
                    "canListChildren": t.boolean().optional(),
                    "canAddMyDriveParent": t.boolean().optional(),
                    "canChangeCopyRequiresWriterPermission": t.boolean().optional(),
                    "canDelete": t.boolean().optional(),
                    "canChangeViewersCanCopyContent": t.boolean().optional(),
                    "canReadLabels": t.boolean().optional(),
                    "canModifyLabels": t.boolean().optional(),
                    "canAddFolderFromAnotherDrive": t.boolean().optional(),
                    "canMoveItemWithinDrive": t.boolean().optional(),
                    "canRename": t.boolean().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "viewersCanCopyContent": t.boolean().optional(),
            "writersCanShare": t.boolean().optional(),
            "sha1Checksum": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "contentRestrictions": t.array(
                t.proxy(renames["ContentRestrictionIn"])
            ).optional(),
            "owners": t.array(t.proxy(renames["UserIn"])).optional(),
            "linkShareMetadata": t.struct(
                {
                    "securityUpdateEnabled": t.boolean().optional(),
                    "securityUpdateEligible": t.boolean().optional(),
                }
            ).optional(),
            "hasThumbnail": t.boolean().optional(),
            "fullFileExtension": t.string().optional(),
            "isAppAuthorized": t.boolean().optional(),
            "folderColorRgb": t.string().optional(),
            "fileExtension": t.string().optional(),
            "starred": t.boolean().optional(),
            "labelInfo": t.struct(
                {"labels": t.array(t.proxy(renames["LabelIn"])).optional()}
            ).optional(),
            "parents": t.array(t.string()).optional(),
            "sharedWithMeTime": t.string().optional(),
            "version": t.string().optional(),
            "trashed": t.boolean().optional(),
            "webContentLink": t.string().optional(),
            "viewedByMe": t.boolean().optional(),
            "appProperties": t.struct({"_": t.string().optional()}).optional(),
            "trashingUser": t.proxy(renames["UserIn"]).optional(),
            "originalFilename": t.string().optional(),
            "viewedByMeTime": t.string().optional(),
            "permissions": t.array(t.proxy(renames["PermissionIn"])).optional(),
            "sha256Checksum": t.string().optional(),
            "headRevisionId": t.string().optional(),
            "trashedTime": t.string().optional(),
            "copyRequiresWriterPermission": t.boolean().optional(),
            "videoMediaMetadata": t.struct(
                {
                    "durationMillis": t.string().optional(),
                    "width": t.integer().optional(),
                    "height": t.integer().optional(),
                }
            ).optional(),
            "spaces": t.array(t.string()).optional(),
            "contentHints": t.struct(
                {
                    "thumbnail": t.struct(
                        {
                            "image": t.string().optional(),
                            "mimeType": t.string().optional(),
                        }
                    ).optional(),
                    "indexableText": t.string().optional(),
                }
            ).optional(),
            "size": t.string().optional(),
            "md5Checksum": t.string().optional(),
            "ownedByMe": t.boolean().optional(),
            "modifiedTime": t.string().optional(),
            "createdTime": t.string().optional(),
            "shared": t.boolean().optional(),
            "mimeType": t.string().optional(),
            "imageMediaMetadata": t.struct(
                {
                    "sensor": t.string().optional(),
                    "subjectDistance": t.integer().optional(),
                    "exposureTime": t.number().optional(),
                    "focalLength": t.number().optional(),
                    "time": t.string().optional(),
                    "aperture": t.number().optional(),
                    "height": t.integer().optional(),
                    "cameraModel": t.string().optional(),
                    "whiteBalance": t.string().optional(),
                    "colorSpace": t.string().optional(),
                    "exposureMode": t.string().optional(),
                    "lens": t.string().optional(),
                    "rotation": t.integer().optional(),
                    "cameraMake": t.string().optional(),
                    "width": t.integer().optional(),
                    "location": t.struct(
                        {
                            "altitude": t.number().optional(),
                            "longitude": t.number().optional(),
                            "latitude": t.number().optional(),
                        }
                    ).optional(),
                    "meteringMode": t.string().optional(),
                    "maxApertureValue": t.number().optional(),
                    "isoSpeed": t.integer().optional(),
                    "flashUsed": t.boolean().optional(),
                    "exposureBias": t.number().optional(),
                }
            ).optional(),
            "driveId": t.string().optional(),
            "quotaBytesUsed": t.string().optional(),
            "permissionIds": t.array(t.string()).optional(),
            "lastModifyingUser": t.proxy(renames["UserIn"]).optional(),
            "teamDriveId": t.string().optional(),
            "iconLink": t.string().optional(),
            "modifiedByMe": t.boolean().optional(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "hasAugmentedPermissions": t.boolean().optional(),
            "sharingUser": t.proxy(renames["UserOut"]).optional(),
            "id": t.string().optional(),
            "modifiedByMeTime": t.string().optional(),
            "explicitlyTrashed": t.boolean().optional(),
            "thumbnailVersion": t.string().optional(),
            "resourceKey": t.string().optional(),
            "webViewLink": t.string().optional(),
            "shortcutDetails": t.struct(
                {
                    "targetId": t.string().optional(),
                    "targetResourceKey": t.string().optional(),
                    "targetMimeType": t.string().optional(),
                }
            ).optional(),
            "thumbnailLink": t.string().optional(),
            "capabilities": t.struct(
                {
                    "canChangeSecurityUpdateEnabled": t.boolean().optional(),
                    "canReadTeamDrive": t.boolean().optional(),
                    "canMoveItemOutOfDrive": t.boolean().optional(),
                    "canTrash": t.boolean().optional(),
                    "canMoveItemIntoTeamDrive": t.boolean().optional(),
                    "canMoveItemOutOfTeamDrive": t.boolean().optional(),
                    "canModifyContent": t.boolean().optional(),
                    "canMoveChildrenWithinTeamDrive": t.boolean().optional(),
                    "canRemoveChildren": t.boolean().optional(),
                    "canMoveChildrenOutOfDrive": t.boolean().optional(),
                    "canMoveChildrenWithinDrive": t.boolean().optional(),
                    "canEdit": t.boolean().optional(),
                    "canShare": t.boolean().optional(),
                    "canDeleteChildren": t.boolean().optional(),
                    "canMoveTeamDriveItem": t.boolean().optional(),
                    "canAcceptOwnership": t.boolean().optional(),
                    "canAddChildren": t.boolean().optional(),
                    "canComment": t.boolean().optional(),
                    "canCopy": t.boolean().optional(),
                    "canMoveItemWithinTeamDrive": t.boolean().optional(),
                    "canModifyContentRestriction": t.boolean().optional(),
                    "canReadDrive": t.boolean().optional(),
                    "canReadRevisions": t.boolean().optional(),
                    "canUntrash": t.boolean().optional(),
                    "canTrashChildren": t.boolean().optional(),
                    "canDownload": t.boolean().optional(),
                    "canMoveChildrenOutOfTeamDrive": t.boolean().optional(),
                    "canRemoveMyDriveParent": t.boolean().optional(),
                    "canListChildren": t.boolean().optional(),
                    "canAddMyDriveParent": t.boolean().optional(),
                    "canChangeCopyRequiresWriterPermission": t.boolean().optional(),
                    "canDelete": t.boolean().optional(),
                    "canChangeViewersCanCopyContent": t.boolean().optional(),
                    "canReadLabels": t.boolean().optional(),
                    "canModifyLabels": t.boolean().optional(),
                    "canAddFolderFromAnotherDrive": t.boolean().optional(),
                    "canMoveItemWithinDrive": t.boolean().optional(),
                    "canRename": t.boolean().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "viewersCanCopyContent": t.boolean().optional(),
            "writersCanShare": t.boolean().optional(),
            "sha1Checksum": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "contentRestrictions": t.array(
                t.proxy(renames["ContentRestrictionOut"])
            ).optional(),
            "owners": t.array(t.proxy(renames["UserOut"])).optional(),
            "linkShareMetadata": t.struct(
                {
                    "securityUpdateEnabled": t.boolean().optional(),
                    "securityUpdateEligible": t.boolean().optional(),
                }
            ).optional(),
            "hasThumbnail": t.boolean().optional(),
            "fullFileExtension": t.string().optional(),
            "isAppAuthorized": t.boolean().optional(),
            "folderColorRgb": t.string().optional(),
            "fileExtension": t.string().optional(),
            "starred": t.boolean().optional(),
            "labelInfo": t.struct(
                {"labels": t.array(t.proxy(renames["LabelOut"])).optional()}
            ).optional(),
            "parents": t.array(t.string()).optional(),
            "sharedWithMeTime": t.string().optional(),
            "version": t.string().optional(),
            "trashed": t.boolean().optional(),
            "webContentLink": t.string().optional(),
            "viewedByMe": t.boolean().optional(),
            "appProperties": t.struct({"_": t.string().optional()}).optional(),
            "trashingUser": t.proxy(renames["UserOut"]).optional(),
            "originalFilename": t.string().optional(),
            "viewedByMeTime": t.string().optional(),
            "permissions": t.array(t.proxy(renames["PermissionOut"])).optional(),
            "sha256Checksum": t.string().optional(),
            "headRevisionId": t.string().optional(),
            "trashedTime": t.string().optional(),
            "copyRequiresWriterPermission": t.boolean().optional(),
            "videoMediaMetadata": t.struct(
                {
                    "durationMillis": t.string().optional(),
                    "width": t.integer().optional(),
                    "height": t.integer().optional(),
                }
            ).optional(),
            "spaces": t.array(t.string()).optional(),
            "contentHints": t.struct(
                {
                    "thumbnail": t.struct(
                        {
                            "image": t.string().optional(),
                            "mimeType": t.string().optional(),
                        }
                    ).optional(),
                    "indexableText": t.string().optional(),
                }
            ).optional(),
            "size": t.string().optional(),
            "md5Checksum": t.string().optional(),
            "ownedByMe": t.boolean().optional(),
            "exportLinks": t.struct({"_": t.string().optional()}).optional(),
            "modifiedTime": t.string().optional(),
            "createdTime": t.string().optional(),
            "shared": t.boolean().optional(),
            "mimeType": t.string().optional(),
            "imageMediaMetadata": t.struct(
                {
                    "sensor": t.string().optional(),
                    "subjectDistance": t.integer().optional(),
                    "exposureTime": t.number().optional(),
                    "focalLength": t.number().optional(),
                    "time": t.string().optional(),
                    "aperture": t.number().optional(),
                    "height": t.integer().optional(),
                    "cameraModel": t.string().optional(),
                    "whiteBalance": t.string().optional(),
                    "colorSpace": t.string().optional(),
                    "exposureMode": t.string().optional(),
                    "lens": t.string().optional(),
                    "rotation": t.integer().optional(),
                    "cameraMake": t.string().optional(),
                    "width": t.integer().optional(),
                    "location": t.struct(
                        {
                            "altitude": t.number().optional(),
                            "longitude": t.number().optional(),
                            "latitude": t.number().optional(),
                        }
                    ).optional(),
                    "meteringMode": t.string().optional(),
                    "maxApertureValue": t.number().optional(),
                    "isoSpeed": t.integer().optional(),
                    "flashUsed": t.boolean().optional(),
                    "exposureBias": t.number().optional(),
                }
            ).optional(),
            "driveId": t.string().optional(),
            "quotaBytesUsed": t.string().optional(),
            "permissionIds": t.array(t.string()).optional(),
            "lastModifyingUser": t.proxy(renames["UserOut"]).optional(),
            "teamDriveId": t.string().optional(),
            "iconLink": t.string().optional(),
            "modifiedByMe": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
    types["PermissionListIn"] = t.struct(
        {
            "permissions": t.array(t.proxy(renames["PermissionIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PermissionListIn"])
    types["PermissionListOut"] = t.struct(
        {
            "permissions": t.array(t.proxy(renames["PermissionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionListOut"])
    types["LabelIn"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LabelIn"])
    types["LabelOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelOut"])
    types["TeamDriveIn"] = t.struct(
        {
            "restrictions": t.struct(
                {
                    "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                    "teamMembersOnly": t.boolean().optional(),
                    "adminManagedRestrictions": t.boolean().optional(),
                    "domainUsersOnly": t.boolean().optional(),
                    "copyRequiresWriterPermission": t.boolean().optional(),
                }
            ).optional(),
            "createdTime": t.string().optional(),
            "backgroundImageLink": t.string().optional(),
            "backgroundImageFile": t.struct(
                {
                    "xCoordinate": t.number().optional(),
                    "yCoordinate": t.number().optional(),
                    "id": t.string().optional(),
                    "width": t.number().optional(),
                }
            ).optional(),
            "themeId": t.string().optional(),
            "orgUnitId": t.string().optional(),
            "capabilities": t.struct(
                {
                    "canTrashChildren": t.boolean().optional(),
                    "canManageMembers": t.boolean().optional(),
                    "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                    "canEdit": t.boolean().optional(),
                    "canShare": t.boolean().optional(),
                    "canCopy": t.boolean().optional(),
                    "canChangeTeamDriveBackground": t.boolean().optional(),
                    "canResetTeamDriveRestrictions": t.boolean().optional(),
                    "canRemoveChildren": t.boolean().optional(),
                    "canDownload": t.boolean().optional(),
                    "canDeleteChildren": t.boolean().optional(),
                    "canComment": t.boolean().optional(),
                    "canRenameTeamDrive": t.boolean().optional(),
                    "canListChildren": t.boolean().optional(),
                    "canChangeTeamMembersOnlyRestriction": t.boolean().optional(),
                    "canAddChildren": t.boolean().optional(),
                    "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                    "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                    "canRename": t.boolean().optional(),
                    "canReadRevisions": t.boolean().optional(),
                    "canDeleteTeamDrive": t.boolean().optional(),
                }
            ).optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "colorRgb": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["TeamDriveIn"])
    types["TeamDriveOut"] = t.struct(
        {
            "restrictions": t.struct(
                {
                    "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                    "teamMembersOnly": t.boolean().optional(),
                    "adminManagedRestrictions": t.boolean().optional(),
                    "domainUsersOnly": t.boolean().optional(),
                    "copyRequiresWriterPermission": t.boolean().optional(),
                }
            ).optional(),
            "createdTime": t.string().optional(),
            "backgroundImageLink": t.string().optional(),
            "backgroundImageFile": t.struct(
                {
                    "xCoordinate": t.number().optional(),
                    "yCoordinate": t.number().optional(),
                    "id": t.string().optional(),
                    "width": t.number().optional(),
                }
            ).optional(),
            "themeId": t.string().optional(),
            "orgUnitId": t.string().optional(),
            "capabilities": t.struct(
                {
                    "canTrashChildren": t.boolean().optional(),
                    "canManageMembers": t.boolean().optional(),
                    "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                    "canEdit": t.boolean().optional(),
                    "canShare": t.boolean().optional(),
                    "canCopy": t.boolean().optional(),
                    "canChangeTeamDriveBackground": t.boolean().optional(),
                    "canResetTeamDriveRestrictions": t.boolean().optional(),
                    "canRemoveChildren": t.boolean().optional(),
                    "canDownload": t.boolean().optional(),
                    "canDeleteChildren": t.boolean().optional(),
                    "canComment": t.boolean().optional(),
                    "canRenameTeamDrive": t.boolean().optional(),
                    "canListChildren": t.boolean().optional(),
                    "canChangeTeamMembersOnlyRestriction": t.boolean().optional(),
                    "canAddChildren": t.boolean().optional(),
                    "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                    "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                    "canRename": t.boolean().optional(),
                    "canReadRevisions": t.boolean().optional(),
                    "canDeleteTeamDrive": t.boolean().optional(),
                }
            ).optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "colorRgb": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TeamDriveOut"])
    types["RevisionListIn"] = t.struct(
        {
            "revisions": t.array(t.proxy(renames["RevisionIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["RevisionListIn"])
    types["RevisionListOut"] = t.struct(
        {
            "revisions": t.array(t.proxy(renames["RevisionOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevisionListOut"])
    types["TeamDriveListIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "teamDrives": t.array(t.proxy(renames["TeamDriveIn"])).optional(),
        }
    ).named(renames["TeamDriveListIn"])
    types["TeamDriveListOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "teamDrives": t.array(t.proxy(renames["TeamDriveOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TeamDriveListOut"])
    types["DriveListIn"] = t.struct(
        {
            "drives": t.array(t.proxy(renames["DriveIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DriveListIn"])
    types["DriveListOut"] = t.struct(
        {
            "drives": t.array(t.proxy(renames["DriveOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveListOut"])
    types["LabelModificationIn"] = t.struct(
        {
            "labelId": t.string().optional(),
            "removeLabel": t.boolean().optional(),
            "kind": t.string().optional(),
            "fieldModifications": t.array(
                t.proxy(renames["LabelFieldModificationIn"])
            ).optional(),
        }
    ).named(renames["LabelModificationIn"])
    types["LabelModificationOut"] = t.struct(
        {
            "labelId": t.string().optional(),
            "removeLabel": t.boolean().optional(),
            "kind": t.string().optional(),
            "fieldModifications": t.array(
                t.proxy(renames["LabelFieldModificationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelModificationOut"])
    types["StartPageTokenIn"] = t.struct(
        {"startPageToken": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["StartPageTokenIn"])
    types["StartPageTokenOut"] = t.struct(
        {
            "startPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartPageTokenOut"])
    types["LabelFieldModificationIn"] = t.struct(
        {
            "setIntegerValues": t.array(t.string()).optional(),
            "setSelectionValues": t.array(t.string()).optional(),
            "setTextValues": t.array(t.string()).optional(),
            "setDateValues": t.array(t.string()).optional(),
            "setUserValues": t.array(t.string()).optional(),
            "fieldId": t.string().optional(),
            "unsetValues": t.boolean().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LabelFieldModificationIn"])
    types["LabelFieldModificationOut"] = t.struct(
        {
            "setIntegerValues": t.array(t.string()).optional(),
            "setSelectionValues": t.array(t.string()).optional(),
            "setTextValues": t.array(t.string()).optional(),
            "setDateValues": t.array(t.string()).optional(),
            "setUserValues": t.array(t.string()).optional(),
            "fieldId": t.string().optional(),
            "unsetValues": t.boolean().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelFieldModificationOut"])
    types["ModifyLabelsRequestIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "labelModifications": t.array(
                t.proxy(renames["LabelModificationIn"])
            ).optional(),
        }
    ).named(renames["ModifyLabelsRequestIn"])
    types["ModifyLabelsRequestOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "labelModifications": t.array(
                t.proxy(renames["LabelModificationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyLabelsRequestOut"])
    types["CommentListIn"] = t.struct(
        {
            "comments": t.array(t.proxy(renames["CommentIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["CommentListIn"])
    types["CommentListOut"] = t.struct(
        {
            "comments": t.array(t.proxy(renames["CommentOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentListOut"])
    types["PermissionIn"] = t.struct(
        {
            "expirationTime": t.string().optional(),
            "type": t.string().optional(),
            "domain": t.string().optional(),
            "view": t.string().optional(),
            "pendingOwner": t.boolean().optional(),
            "id": t.string().optional(),
            "photoLink": t.string().optional(),
            "role": t.string().optional(),
            "deleted": t.boolean().optional(),
            "emailAddress": t.string().optional(),
            "displayName": t.string().optional(),
            "allowFileDiscovery": t.boolean().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PermissionIn"])
    types["PermissionOut"] = t.struct(
        {
            "permissionDetails": t.array(
                t.struct(
                    {
                        "inheritedFrom": t.string().optional(),
                        "inherited": t.boolean().optional(),
                        "role": t.string().optional(),
                        "permissionType": t.string().optional(),
                    }
                )
            ).optional(),
            "expirationTime": t.string().optional(),
            "type": t.string().optional(),
            "teamDrivePermissionDetails": t.array(
                t.struct(
                    {
                        "inheritedFrom": t.string().optional(),
                        "teamDrivePermissionType": t.string().optional(),
                        "role": t.string().optional(),
                        "inherited": t.boolean().optional(),
                    }
                )
            ).optional(),
            "domain": t.string().optional(),
            "view": t.string().optional(),
            "pendingOwner": t.boolean().optional(),
            "id": t.string().optional(),
            "photoLink": t.string().optional(),
            "role": t.string().optional(),
            "deleted": t.boolean().optional(),
            "emailAddress": t.string().optional(),
            "displayName": t.string().optional(),
            "allowFileDiscovery": t.boolean().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionOut"])
    types["UserIn"] = t.struct(
        {
            "photoLink": t.string().optional(),
            "kind": t.string().optional(),
            "emailAddress": t.string().optional(),
            "displayName": t.string().optional(),
            "permissionId": t.string().optional(),
            "me": t.boolean().optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "photoLink": t.string().optional(),
            "kind": t.string().optional(),
            "emailAddress": t.string().optional(),
            "displayName": t.string().optional(),
            "permissionId": t.string().optional(),
            "me": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])

    functions = {}
    functions["channelsStop"] = drive.post(
        "channels/stop",
        t.struct(
            {
                "params": t.struct({"_": t.string().optional()}).optional(),
                "resourceUri": t.string().optional(),
                "kind": t.string().optional(),
                "token": t.string().optional(),
                "payload": t.boolean().optional(),
                "type": t.string().optional(),
                "expiration": t.string().optional(),
                "address": t.string().optional(),
                "resourceId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["permissionsCreate"] = drive.get(
        "files/{fileId}/permissions/{permissionId}",
        t.struct(
            {
                "permissionId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "fileId": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["permissionsUpdate"] = drive.get(
        "files/{fileId}/permissions/{permissionId}",
        t.struct(
            {
                "permissionId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "fileId": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["permissionsList"] = drive.get(
        "files/{fileId}/permissions/{permissionId}",
        t.struct(
            {
                "permissionId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "fileId": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["permissionsDelete"] = drive.get(
        "files/{fileId}/permissions/{permissionId}",
        t.struct(
            {
                "permissionId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "fileId": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["permissionsGet"] = drive.get(
        "files/{fileId}/permissions/{permissionId}",
        t.struct(
            {
                "permissionId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "fileId": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["aboutGet"] = drive.get(
        "about",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["AboutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesListLabels"] = drive.delete(
        "files/{fileId}",
        t.struct(
            {
                "supportsTeamDrives": t.boolean().optional(),
                "enforceSingleParent": t.boolean().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesCopy"] = drive.delete(
        "files/{fileId}",
        t.struct(
            {
                "supportsTeamDrives": t.boolean().optional(),
                "enforceSingleParent": t.boolean().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesGenerateIds"] = drive.delete(
        "files/{fileId}",
        t.struct(
            {
                "supportsTeamDrives": t.boolean().optional(),
                "enforceSingleParent": t.boolean().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesExport"] = drive.delete(
        "files/{fileId}",
        t.struct(
            {
                "supportsTeamDrives": t.boolean().optional(),
                "enforceSingleParent": t.boolean().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesEmptyTrash"] = drive.delete(
        "files/{fileId}",
        t.struct(
            {
                "supportsTeamDrives": t.boolean().optional(),
                "enforceSingleParent": t.boolean().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesGet"] = drive.delete(
        "files/{fileId}",
        t.struct(
            {
                "supportsTeamDrives": t.boolean().optional(),
                "enforceSingleParent": t.boolean().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesCreate"] = drive.delete(
        "files/{fileId}",
        t.struct(
            {
                "supportsTeamDrives": t.boolean().optional(),
                "enforceSingleParent": t.boolean().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesModifyLabels"] = drive.delete(
        "files/{fileId}",
        t.struct(
            {
                "supportsTeamDrives": t.boolean().optional(),
                "enforceSingleParent": t.boolean().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesUpdate"] = drive.delete(
        "files/{fileId}",
        t.struct(
            {
                "supportsTeamDrives": t.boolean().optional(),
                "enforceSingleParent": t.boolean().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesWatch"] = drive.delete(
        "files/{fileId}",
        t.struct(
            {
                "supportsTeamDrives": t.boolean().optional(),
                "enforceSingleParent": t.boolean().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesList"] = drive.delete(
        "files/{fileId}",
        t.struct(
            {
                "supportsTeamDrives": t.boolean().optional(),
                "enforceSingleParent": t.boolean().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesDelete"] = drive.delete(
        "files/{fileId}",
        t.struct(
            {
                "supportsTeamDrives": t.boolean().optional(),
                "enforceSingleParent": t.boolean().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["revisionsUpdate"] = drive.get(
        "files/{fileId}/revisions/{revisionId}",
        t.struct(
            {
                "acknowledgeAbuse": t.boolean().optional(),
                "fileId": t.string().optional(),
                "revisionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevisionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["revisionsList"] = drive.get(
        "files/{fileId}/revisions/{revisionId}",
        t.struct(
            {
                "acknowledgeAbuse": t.boolean().optional(),
                "fileId": t.string().optional(),
                "revisionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevisionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["revisionsDelete"] = drive.get(
        "files/{fileId}/revisions/{revisionId}",
        t.struct(
            {
                "acknowledgeAbuse": t.boolean().optional(),
                "fileId": t.string().optional(),
                "revisionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevisionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["revisionsGet"] = drive.get(
        "files/{fileId}/revisions/{revisionId}",
        t.struct(
            {
                "acknowledgeAbuse": t.boolean().optional(),
                "fileId": t.string().optional(),
                "revisionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevisionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsList"] = drive.patch(
        "files/{fileId}/comments/{commentId}",
        t.struct(
            {
                "fileId": t.string().optional(),
                "commentId": t.string().optional(),
                "createdTime": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "quotedFileContent": t.struct(
                    {"value": t.string().optional(), "mimeType": t.string().optional()}
                ).optional(),
                "deleted": t.boolean().optional(),
                "anchor": t.string().optional(),
                "content": t.string().optional(),
                "id": t.string().optional(),
                "resolved": t.boolean().optional(),
                "kind": t.string().optional(),
                "htmlContent": t.string().optional(),
                "replies": t.array(t.proxy(renames["ReplyIn"])).optional(),
                "author": t.proxy(renames["UserIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsGet"] = drive.patch(
        "files/{fileId}/comments/{commentId}",
        t.struct(
            {
                "fileId": t.string().optional(),
                "commentId": t.string().optional(),
                "createdTime": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "quotedFileContent": t.struct(
                    {"value": t.string().optional(), "mimeType": t.string().optional()}
                ).optional(),
                "deleted": t.boolean().optional(),
                "anchor": t.string().optional(),
                "content": t.string().optional(),
                "id": t.string().optional(),
                "resolved": t.boolean().optional(),
                "kind": t.string().optional(),
                "htmlContent": t.string().optional(),
                "replies": t.array(t.proxy(renames["ReplyIn"])).optional(),
                "author": t.proxy(renames["UserIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsDelete"] = drive.patch(
        "files/{fileId}/comments/{commentId}",
        t.struct(
            {
                "fileId": t.string().optional(),
                "commentId": t.string().optional(),
                "createdTime": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "quotedFileContent": t.struct(
                    {"value": t.string().optional(), "mimeType": t.string().optional()}
                ).optional(),
                "deleted": t.boolean().optional(),
                "anchor": t.string().optional(),
                "content": t.string().optional(),
                "id": t.string().optional(),
                "resolved": t.boolean().optional(),
                "kind": t.string().optional(),
                "htmlContent": t.string().optional(),
                "replies": t.array(t.proxy(renames["ReplyIn"])).optional(),
                "author": t.proxy(renames["UserIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsCreate"] = drive.patch(
        "files/{fileId}/comments/{commentId}",
        t.struct(
            {
                "fileId": t.string().optional(),
                "commentId": t.string().optional(),
                "createdTime": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "quotedFileContent": t.struct(
                    {"value": t.string().optional(), "mimeType": t.string().optional()}
                ).optional(),
                "deleted": t.boolean().optional(),
                "anchor": t.string().optional(),
                "content": t.string().optional(),
                "id": t.string().optional(),
                "resolved": t.boolean().optional(),
                "kind": t.string().optional(),
                "htmlContent": t.string().optional(),
                "replies": t.array(t.proxy(renames["ReplyIn"])).optional(),
                "author": t.proxy(renames["UserIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsUpdate"] = drive.patch(
        "files/{fileId}/comments/{commentId}",
        t.struct(
            {
                "fileId": t.string().optional(),
                "commentId": t.string().optional(),
                "createdTime": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "quotedFileContent": t.struct(
                    {"value": t.string().optional(), "mimeType": t.string().optional()}
                ).optional(),
                "deleted": t.boolean().optional(),
                "anchor": t.string().optional(),
                "content": t.string().optional(),
                "id": t.string().optional(),
                "resolved": t.boolean().optional(),
                "kind": t.string().optional(),
                "htmlContent": t.string().optional(),
                "replies": t.array(t.proxy(renames["ReplyIn"])).optional(),
                "author": t.proxy(renames["UserIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repliesList"] = drive.get(
        "files/{fileId}/comments/{commentId}/replies/{replyId}",
        t.struct(
            {
                "replyId": t.string().optional(),
                "commentId": t.string().optional(),
                "includeDeleted": t.boolean().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReplyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repliesUpdate"] = drive.get(
        "files/{fileId}/comments/{commentId}/replies/{replyId}",
        t.struct(
            {
                "replyId": t.string().optional(),
                "commentId": t.string().optional(),
                "includeDeleted": t.boolean().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReplyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repliesDelete"] = drive.get(
        "files/{fileId}/comments/{commentId}/replies/{replyId}",
        t.struct(
            {
                "replyId": t.string().optional(),
                "commentId": t.string().optional(),
                "includeDeleted": t.boolean().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReplyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repliesCreate"] = drive.get(
        "files/{fileId}/comments/{commentId}/replies/{replyId}",
        t.struct(
            {
                "replyId": t.string().optional(),
                "commentId": t.string().optional(),
                "includeDeleted": t.boolean().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReplyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repliesGet"] = drive.get(
        "files/{fileId}/comments/{commentId}/replies/{replyId}",
        t.struct(
            {
                "replyId": t.string().optional(),
                "commentId": t.string().optional(),
                "includeDeleted": t.boolean().optional(),
                "fileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReplyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["teamdrivesList"] = drive.delete(
        "teamdrives/{teamDriveId}",
        t.struct({"teamDriveId": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["teamdrivesCreate"] = drive.delete(
        "teamdrives/{teamDriveId}",
        t.struct({"teamDriveId": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["teamdrivesGet"] = drive.delete(
        "teamdrives/{teamDriveId}",
        t.struct({"teamDriveId": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["teamdrivesUpdate"] = drive.delete(
        "teamdrives/{teamDriveId}",
        t.struct({"teamDriveId": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["teamdrivesDelete"] = drive.delete(
        "teamdrives/{teamDriveId}",
        t.struct({"teamDriveId": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["drivesDelete"] = drive.get(
        "drives/{driveId}",
        t.struct(
            {
                "driveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["drivesHide"] = drive.get(
        "drives/{driveId}",
        t.struct(
            {
                "driveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["drivesUnhide"] = drive.get(
        "drives/{driveId}",
        t.struct(
            {
                "driveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["drivesList"] = drive.get(
        "drives/{driveId}",
        t.struct(
            {
                "driveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["drivesUpdate"] = drive.get(
        "drives/{driveId}",
        t.struct(
            {
                "driveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["drivesCreate"] = drive.get(
        "drives/{driveId}",
        t.struct(
            {
                "driveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["drivesGet"] = drive.get(
        "drives/{driveId}",
        t.struct(
            {
                "driveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["changesList"] = drive.get(
        "changes/startPageToken",
        t.struct(
            {
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "teamDriveId": t.string().optional(),
                "driveId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StartPageTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["changesWatch"] = drive.get(
        "changes/startPageToken",
        t.struct(
            {
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "teamDriveId": t.string().optional(),
                "driveId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StartPageTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["changesGetStartPageToken"] = drive.get(
        "changes/startPageToken",
        t.struct(
            {
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "teamDriveId": t.string().optional(),
                "driveId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StartPageTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="drive", renames=renames, types=Box(types), functions=Box(functions)
    )
