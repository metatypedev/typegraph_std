from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_drive() -> Import:
    drive = HTTPRuntime("https://www.googleapis.com/")

    renames = {
        "ErrorResponse": "_drive_1_ErrorResponse",
        "AboutIn": "_drive_2_AboutIn",
        "AboutOut": "_drive_3_AboutOut",
        "ChangeIn": "_drive_4_ChangeIn",
        "ChangeOut": "_drive_5_ChangeOut",
        "ChangeListIn": "_drive_6_ChangeListIn",
        "ChangeListOut": "_drive_7_ChangeListOut",
        "ChannelIn": "_drive_8_ChannelIn",
        "ChannelOut": "_drive_9_ChannelOut",
        "CommentIn": "_drive_10_CommentIn",
        "CommentOut": "_drive_11_CommentOut",
        "CommentListIn": "_drive_12_CommentListIn",
        "CommentListOut": "_drive_13_CommentListOut",
        "ContentRestrictionIn": "_drive_14_ContentRestrictionIn",
        "ContentRestrictionOut": "_drive_15_ContentRestrictionOut",
        "DriveIn": "_drive_16_DriveIn",
        "DriveOut": "_drive_17_DriveOut",
        "DriveListIn": "_drive_18_DriveListIn",
        "DriveListOut": "_drive_19_DriveListOut",
        "FileIn": "_drive_20_FileIn",
        "FileOut": "_drive_21_FileOut",
        "FileListIn": "_drive_22_FileListIn",
        "FileListOut": "_drive_23_FileListOut",
        "GeneratedIdsIn": "_drive_24_GeneratedIdsIn",
        "GeneratedIdsOut": "_drive_25_GeneratedIdsOut",
        "LabelIn": "_drive_26_LabelIn",
        "LabelOut": "_drive_27_LabelOut",
        "LabelFieldIn": "_drive_28_LabelFieldIn",
        "LabelFieldOut": "_drive_29_LabelFieldOut",
        "LabelFieldModificationIn": "_drive_30_LabelFieldModificationIn",
        "LabelFieldModificationOut": "_drive_31_LabelFieldModificationOut",
        "LabelListIn": "_drive_32_LabelListIn",
        "LabelListOut": "_drive_33_LabelListOut",
        "LabelModificationIn": "_drive_34_LabelModificationIn",
        "LabelModificationOut": "_drive_35_LabelModificationOut",
        "ModifyLabelsRequestIn": "_drive_36_ModifyLabelsRequestIn",
        "ModifyLabelsRequestOut": "_drive_37_ModifyLabelsRequestOut",
        "ModifyLabelsResponseIn": "_drive_38_ModifyLabelsResponseIn",
        "ModifyLabelsResponseOut": "_drive_39_ModifyLabelsResponseOut",
        "PermissionIn": "_drive_40_PermissionIn",
        "PermissionOut": "_drive_41_PermissionOut",
        "PermissionListIn": "_drive_42_PermissionListIn",
        "PermissionListOut": "_drive_43_PermissionListOut",
        "ReplyIn": "_drive_44_ReplyIn",
        "ReplyOut": "_drive_45_ReplyOut",
        "ReplyListIn": "_drive_46_ReplyListIn",
        "ReplyListOut": "_drive_47_ReplyListOut",
        "RevisionIn": "_drive_48_RevisionIn",
        "RevisionOut": "_drive_49_RevisionOut",
        "RevisionListIn": "_drive_50_RevisionListIn",
        "RevisionListOut": "_drive_51_RevisionListOut",
        "StartPageTokenIn": "_drive_52_StartPageTokenIn",
        "StartPageTokenOut": "_drive_53_StartPageTokenOut",
        "TeamDriveIn": "_drive_54_TeamDriveIn",
        "TeamDriveOut": "_drive_55_TeamDriveOut",
        "TeamDriveListIn": "_drive_56_TeamDriveListIn",
        "TeamDriveListOut": "_drive_57_TeamDriveListOut",
        "UserIn": "_drive_58_UserIn",
        "UserOut": "_drive_59_UserOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AboutIn"] = t.struct(
        {
            "appInstalled": t.boolean().optional(),
            "canCreateDrives": t.boolean().optional(),
            "canCreateTeamDrives": t.boolean().optional(),
            "driveThemes": t.array(
                t.struct(
                    {
                        "backgroundImageLink": t.string().optional(),
                        "colorRgb": t.string().optional(),
                        "id": t.string().optional(),
                    }
                )
            ).optional(),
            "exportFormats": t.struct({"_": t.string().optional()}).optional(),
            "folderColorPalette": t.array(t.string()).optional(),
            "importFormats": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "maxImportSizes": t.struct({"_": t.string().optional()}).optional(),
            "maxUploadSize": t.string().optional(),
            "storageQuota": t.struct(
                {
                    "limit": t.string().optional(),
                    "usage": t.string().optional(),
                    "usageInDrive": t.string().optional(),
                    "usageInDriveTrash": t.string().optional(),
                }
            ).optional(),
            "teamDriveThemes": t.array(
                t.struct(
                    {
                        "backgroundImageLink": t.string().optional(),
                        "colorRgb": t.string().optional(),
                        "id": t.string().optional(),
                    }
                )
            ).optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
        }
    ).named(renames["AboutIn"])
    types["AboutOut"] = t.struct(
        {
            "appInstalled": t.boolean().optional(),
            "canCreateDrives": t.boolean().optional(),
            "canCreateTeamDrives": t.boolean().optional(),
            "driveThemes": t.array(
                t.struct(
                    {
                        "backgroundImageLink": t.string().optional(),
                        "colorRgb": t.string().optional(),
                        "id": t.string().optional(),
                    }
                )
            ).optional(),
            "exportFormats": t.struct({"_": t.string().optional()}).optional(),
            "folderColorPalette": t.array(t.string()).optional(),
            "importFormats": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "maxImportSizes": t.struct({"_": t.string().optional()}).optional(),
            "maxUploadSize": t.string().optional(),
            "storageQuota": t.struct(
                {
                    "limit": t.string().optional(),
                    "usage": t.string().optional(),
                    "usageInDrive": t.string().optional(),
                    "usageInDriveTrash": t.string().optional(),
                }
            ).optional(),
            "teamDriveThemes": t.array(
                t.struct(
                    {
                        "backgroundImageLink": t.string().optional(),
                        "colorRgb": t.string().optional(),
                        "id": t.string().optional(),
                    }
                )
            ).optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AboutOut"])
    types["ChangeIn"] = t.struct(
        {
            "changeType": t.string().optional(),
            "drive": t.proxy(renames["DriveIn"]).optional(),
            "driveId": t.string().optional(),
            "file": t.proxy(renames["FileIn"]).optional(),
            "fileId": t.string().optional(),
            "kind": t.string().optional(),
            "removed": t.boolean().optional(),
            "teamDrive": t.proxy(renames["TeamDriveIn"]).optional(),
            "teamDriveId": t.string().optional(),
            "time": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ChangeIn"])
    types["ChangeOut"] = t.struct(
        {
            "changeType": t.string().optional(),
            "drive": t.proxy(renames["DriveOut"]).optional(),
            "driveId": t.string().optional(),
            "file": t.proxy(renames["FileOut"]).optional(),
            "fileId": t.string().optional(),
            "kind": t.string().optional(),
            "removed": t.boolean().optional(),
            "teamDrive": t.proxy(renames["TeamDriveOut"]).optional(),
            "teamDriveId": t.string().optional(),
            "time": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChangeOut"])
    types["ChangeListIn"] = t.struct(
        {
            "changes": t.array(t.proxy(renames["ChangeIn"])).optional(),
            "kind": t.string().optional(),
            "newStartPageToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ChangeListIn"])
    types["ChangeListOut"] = t.struct(
        {
            "changes": t.array(t.proxy(renames["ChangeOut"])).optional(),
            "kind": t.string().optional(),
            "newStartPageToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChangeListOut"])
    types["ChannelIn"] = t.struct(
        {
            "address": t.string().optional(),
            "expiration": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "payload": t.boolean().optional(),
            "resourceId": t.string().optional(),
            "resourceUri": t.string().optional(),
            "token": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "address": t.string().optional(),
            "expiration": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "payload": t.boolean().optional(),
            "resourceId": t.string().optional(),
            "resourceUri": t.string().optional(),
            "token": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
    types["CommentIn"] = t.struct(
        {
            "anchor": t.string().optional(),
            "author": t.proxy(renames["UserIn"]).optional(),
            "content": t.string().optional(),
            "createdTime": t.string().optional(),
            "deleted": t.boolean().optional(),
            "htmlContent": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "modifiedTime": t.string().optional(),
            "quotedFileContent": t.struct(
                {"mimeType": t.string().optional(), "value": t.string().optional()}
            ).optional(),
            "replies": t.array(t.proxy(renames["ReplyIn"])).optional(),
            "resolved": t.boolean().optional(),
        }
    ).named(renames["CommentIn"])
    types["CommentOut"] = t.struct(
        {
            "anchor": t.string().optional(),
            "author": t.proxy(renames["UserOut"]).optional(),
            "content": t.string().optional(),
            "createdTime": t.string().optional(),
            "deleted": t.boolean().optional(),
            "htmlContent": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "modifiedTime": t.string().optional(),
            "quotedFileContent": t.struct(
                {"mimeType": t.string().optional(), "value": t.string().optional()}
            ).optional(),
            "replies": t.array(t.proxy(renames["ReplyOut"])).optional(),
            "resolved": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentOut"])
    types["CommentListIn"] = t.struct(
        {
            "comments": t.array(t.proxy(renames["CommentIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["CommentListIn"])
    types["CommentListOut"] = t.struct(
        {
            "comments": t.array(t.proxy(renames["CommentOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentListOut"])
    types["ContentRestrictionIn"] = t.struct(
        {
            "readOnly": t.boolean().optional(),
            "reason": t.string().optional(),
            "restrictingUser": t.proxy(renames["UserIn"]).optional(),
            "restrictionTime": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ContentRestrictionIn"])
    types["ContentRestrictionOut"] = t.struct(
        {
            "readOnly": t.boolean().optional(),
            "reason": t.string().optional(),
            "restrictingUser": t.proxy(renames["UserOut"]).optional(),
            "restrictionTime": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentRestrictionOut"])
    types["DriveIn"] = t.struct(
        {
            "backgroundImageFile": t.struct(
                {
                    "id": t.string().optional(),
                    "width": t.number().optional(),
                    "xCoordinate": t.number().optional(),
                    "yCoordinate": t.number().optional(),
                }
            ).optional(),
            "backgroundImageLink": t.string().optional(),
            "capabilities": t.struct(
                {
                    "canAddChildren": t.boolean().optional(),
                    "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                    "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                    "canChangeDriveBackground": t.boolean().optional(),
                    "canChangeDriveMembersOnlyRestriction": t.boolean().optional(),
                    "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                    "canComment": t.boolean().optional(),
                    "canCopy": t.boolean().optional(),
                    "canDeleteChildren": t.boolean().optional(),
                    "canDeleteDrive": t.boolean().optional(),
                    "canDownload": t.boolean().optional(),
                    "canEdit": t.boolean().optional(),
                    "canListChildren": t.boolean().optional(),
                    "canManageMembers": t.boolean().optional(),
                    "canReadRevisions": t.boolean().optional(),
                    "canRename": t.boolean().optional(),
                    "canRenameDrive": t.boolean().optional(),
                    "canResetDriveRestrictions": t.boolean().optional(),
                    "canShare": t.boolean().optional(),
                    "canTrashChildren": t.boolean().optional(),
                }
            ).optional(),
            "colorRgb": t.string().optional(),
            "createdTime": t.string().optional(),
            "hidden": t.boolean().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "orgUnitId": t.string().optional(),
            "restrictions": t.struct(
                {
                    "adminManagedRestrictions": t.boolean().optional(),
                    "copyRequiresWriterPermission": t.boolean().optional(),
                    "domainUsersOnly": t.boolean().optional(),
                    "driveMembersOnly": t.boolean().optional(),
                    "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                }
            ).optional(),
            "themeId": t.string().optional(),
        }
    ).named(renames["DriveIn"])
    types["DriveOut"] = t.struct(
        {
            "backgroundImageFile": t.struct(
                {
                    "id": t.string().optional(),
                    "width": t.number().optional(),
                    "xCoordinate": t.number().optional(),
                    "yCoordinate": t.number().optional(),
                }
            ).optional(),
            "backgroundImageLink": t.string().optional(),
            "capabilities": t.struct(
                {
                    "canAddChildren": t.boolean().optional(),
                    "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                    "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                    "canChangeDriveBackground": t.boolean().optional(),
                    "canChangeDriveMembersOnlyRestriction": t.boolean().optional(),
                    "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                    "canComment": t.boolean().optional(),
                    "canCopy": t.boolean().optional(),
                    "canDeleteChildren": t.boolean().optional(),
                    "canDeleteDrive": t.boolean().optional(),
                    "canDownload": t.boolean().optional(),
                    "canEdit": t.boolean().optional(),
                    "canListChildren": t.boolean().optional(),
                    "canManageMembers": t.boolean().optional(),
                    "canReadRevisions": t.boolean().optional(),
                    "canRename": t.boolean().optional(),
                    "canRenameDrive": t.boolean().optional(),
                    "canResetDriveRestrictions": t.boolean().optional(),
                    "canShare": t.boolean().optional(),
                    "canTrashChildren": t.boolean().optional(),
                }
            ).optional(),
            "colorRgb": t.string().optional(),
            "createdTime": t.string().optional(),
            "hidden": t.boolean().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "orgUnitId": t.string().optional(),
            "restrictions": t.struct(
                {
                    "adminManagedRestrictions": t.boolean().optional(),
                    "copyRequiresWriterPermission": t.boolean().optional(),
                    "domainUsersOnly": t.boolean().optional(),
                    "driveMembersOnly": t.boolean().optional(),
                    "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                }
            ).optional(),
            "themeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveOut"])
    types["DriveListIn"] = t.struct(
        {
            "drives": t.array(t.proxy(renames["DriveIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["DriveListIn"])
    types["DriveListOut"] = t.struct(
        {
            "drives": t.array(t.proxy(renames["DriveOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveListOut"])
    types["FileIn"] = t.struct(
        {
            "appProperties": t.struct({"_": t.string().optional()}).optional(),
            "capabilities": t.struct(
                {
                    "canAcceptOwnership": t.boolean().optional(),
                    "canAddChildren": t.boolean().optional(),
                    "canAddFolderFromAnotherDrive": t.boolean().optional(),
                    "canAddMyDriveParent": t.boolean().optional(),
                    "canChangeCopyRequiresWriterPermission": t.boolean().optional(),
                    "canChangeSecurityUpdateEnabled": t.boolean().optional(),
                    "canChangeViewersCanCopyContent": t.boolean().optional(),
                    "canComment": t.boolean().optional(),
                    "canCopy": t.boolean().optional(),
                    "canDelete": t.boolean().optional(),
                    "canDeleteChildren": t.boolean().optional(),
                    "canDownload": t.boolean().optional(),
                    "canEdit": t.boolean().optional(),
                    "canListChildren": t.boolean().optional(),
                    "canModifyContent": t.boolean().optional(),
                    "canModifyContentRestriction": t.boolean().optional(),
                    "canModifyLabels": t.boolean().optional(),
                    "canMoveChildrenOutOfDrive": t.boolean().optional(),
                    "canMoveChildrenOutOfTeamDrive": t.boolean().optional(),
                    "canMoveChildrenWithinDrive": t.boolean().optional(),
                    "canMoveChildrenWithinTeamDrive": t.boolean().optional(),
                    "canMoveItemIntoTeamDrive": t.boolean().optional(),
                    "canMoveItemOutOfDrive": t.boolean().optional(),
                    "canMoveItemOutOfTeamDrive": t.boolean().optional(),
                    "canMoveItemWithinDrive": t.boolean().optional(),
                    "canMoveItemWithinTeamDrive": t.boolean().optional(),
                    "canMoveTeamDriveItem": t.boolean().optional(),
                    "canReadDrive": t.boolean().optional(),
                    "canReadLabels": t.boolean().optional(),
                    "canReadRevisions": t.boolean().optional(),
                    "canReadTeamDrive": t.boolean().optional(),
                    "canRemoveChildren": t.boolean().optional(),
                    "canRemoveMyDriveParent": t.boolean().optional(),
                    "canRename": t.boolean().optional(),
                    "canShare": t.boolean().optional(),
                    "canTrash": t.boolean().optional(),
                    "canTrashChildren": t.boolean().optional(),
                    "canUntrash": t.boolean().optional(),
                }
            ).optional(),
            "contentHints": t.struct(
                {
                    "indexableText": t.string().optional(),
                    "thumbnail": t.struct(
                        {
                            "image": t.string().optional(),
                            "mimeType": t.string().optional(),
                        }
                    ).optional(),
                }
            ).optional(),
            "contentRestrictions": t.array(
                t.proxy(renames["ContentRestrictionIn"])
            ).optional(),
            "copyRequiresWriterPermission": t.boolean().optional(),
            "createdTime": t.string().optional(),
            "description": t.string().optional(),
            "driveId": t.string().optional(),
            "explicitlyTrashed": t.boolean().optional(),
            "fileExtension": t.string().optional(),
            "folderColorRgb": t.string().optional(),
            "fullFileExtension": t.string().optional(),
            "hasAugmentedPermissions": t.boolean().optional(),
            "hasThumbnail": t.boolean().optional(),
            "headRevisionId": t.string().optional(),
            "iconLink": t.string().optional(),
            "id": t.string().optional(),
            "imageMediaMetadata": t.struct(
                {
                    "aperture": t.number().optional(),
                    "cameraMake": t.string().optional(),
                    "cameraModel": t.string().optional(),
                    "colorSpace": t.string().optional(),
                    "exposureBias": t.number().optional(),
                    "exposureMode": t.string().optional(),
                    "exposureTime": t.number().optional(),
                    "flashUsed": t.boolean().optional(),
                    "focalLength": t.number().optional(),
                    "height": t.integer().optional(),
                    "isoSpeed": t.integer().optional(),
                    "lens": t.string().optional(),
                    "location": t.struct(
                        {
                            "altitude": t.number().optional(),
                            "latitude": t.number().optional(),
                            "longitude": t.number().optional(),
                        }
                    ).optional(),
                    "maxApertureValue": t.number().optional(),
                    "meteringMode": t.string().optional(),
                    "rotation": t.integer().optional(),
                    "sensor": t.string().optional(),
                    "subjectDistance": t.integer().optional(),
                    "time": t.string().optional(),
                    "whiteBalance": t.string().optional(),
                    "width": t.integer().optional(),
                }
            ).optional(),
            "isAppAuthorized": t.boolean().optional(),
            "kind": t.string().optional(),
            "labelInfo": t.struct(
                {"labels": t.array(t.proxy(renames["LabelIn"])).optional()}
            ).optional(),
            "lastModifyingUser": t.proxy(renames["UserIn"]).optional(),
            "linkShareMetadata": t.struct(
                {
                    "securityUpdateEligible": t.boolean().optional(),
                    "securityUpdateEnabled": t.boolean().optional(),
                }
            ).optional(),
            "md5Checksum": t.string().optional(),
            "mimeType": t.string().optional(),
            "modifiedByMe": t.boolean().optional(),
            "modifiedByMeTime": t.string().optional(),
            "modifiedTime": t.string().optional(),
            "name": t.string().optional(),
            "originalFilename": t.string().optional(),
            "ownedByMe": t.boolean().optional(),
            "owners": t.array(t.proxy(renames["UserIn"])).optional(),
            "parents": t.array(t.string()).optional(),
            "permissionIds": t.array(t.string()).optional(),
            "permissions": t.array(t.proxy(renames["PermissionIn"])).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "quotaBytesUsed": t.string().optional(),
            "resourceKey": t.string().optional(),
            "sha1Checksum": t.string().optional(),
            "sha256Checksum": t.string().optional(),
            "shared": t.boolean().optional(),
            "sharedWithMeTime": t.string().optional(),
            "sharingUser": t.proxy(renames["UserIn"]).optional(),
            "shortcutDetails": t.struct(
                {
                    "targetId": t.string().optional(),
                    "targetMimeType": t.string().optional(),
                    "targetResourceKey": t.string().optional(),
                }
            ).optional(),
            "size": t.string().optional(),
            "spaces": t.array(t.string()).optional(),
            "starred": t.boolean().optional(),
            "teamDriveId": t.string().optional(),
            "thumbnailLink": t.string().optional(),
            "thumbnailVersion": t.string().optional(),
            "trashed": t.boolean().optional(),
            "trashedTime": t.string().optional(),
            "trashingUser": t.proxy(renames["UserIn"]).optional(),
            "version": t.string().optional(),
            "videoMediaMetadata": t.struct(
                {
                    "durationMillis": t.string().optional(),
                    "height": t.integer().optional(),
                    "width": t.integer().optional(),
                }
            ).optional(),
            "viewedByMe": t.boolean().optional(),
            "viewedByMeTime": t.string().optional(),
            "viewersCanCopyContent": t.boolean().optional(),
            "webContentLink": t.string().optional(),
            "webViewLink": t.string().optional(),
            "writersCanShare": t.boolean().optional(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "appProperties": t.struct({"_": t.string().optional()}).optional(),
            "capabilities": t.struct(
                {
                    "canAcceptOwnership": t.boolean().optional(),
                    "canAddChildren": t.boolean().optional(),
                    "canAddFolderFromAnotherDrive": t.boolean().optional(),
                    "canAddMyDriveParent": t.boolean().optional(),
                    "canChangeCopyRequiresWriterPermission": t.boolean().optional(),
                    "canChangeSecurityUpdateEnabled": t.boolean().optional(),
                    "canChangeViewersCanCopyContent": t.boolean().optional(),
                    "canComment": t.boolean().optional(),
                    "canCopy": t.boolean().optional(),
                    "canDelete": t.boolean().optional(),
                    "canDeleteChildren": t.boolean().optional(),
                    "canDownload": t.boolean().optional(),
                    "canEdit": t.boolean().optional(),
                    "canListChildren": t.boolean().optional(),
                    "canModifyContent": t.boolean().optional(),
                    "canModifyContentRestriction": t.boolean().optional(),
                    "canModifyLabels": t.boolean().optional(),
                    "canMoveChildrenOutOfDrive": t.boolean().optional(),
                    "canMoveChildrenOutOfTeamDrive": t.boolean().optional(),
                    "canMoveChildrenWithinDrive": t.boolean().optional(),
                    "canMoveChildrenWithinTeamDrive": t.boolean().optional(),
                    "canMoveItemIntoTeamDrive": t.boolean().optional(),
                    "canMoveItemOutOfDrive": t.boolean().optional(),
                    "canMoveItemOutOfTeamDrive": t.boolean().optional(),
                    "canMoveItemWithinDrive": t.boolean().optional(),
                    "canMoveItemWithinTeamDrive": t.boolean().optional(),
                    "canMoveTeamDriveItem": t.boolean().optional(),
                    "canReadDrive": t.boolean().optional(),
                    "canReadLabels": t.boolean().optional(),
                    "canReadRevisions": t.boolean().optional(),
                    "canReadTeamDrive": t.boolean().optional(),
                    "canRemoveChildren": t.boolean().optional(),
                    "canRemoveMyDriveParent": t.boolean().optional(),
                    "canRename": t.boolean().optional(),
                    "canShare": t.boolean().optional(),
                    "canTrash": t.boolean().optional(),
                    "canTrashChildren": t.boolean().optional(),
                    "canUntrash": t.boolean().optional(),
                }
            ).optional(),
            "contentHints": t.struct(
                {
                    "indexableText": t.string().optional(),
                    "thumbnail": t.struct(
                        {
                            "image": t.string().optional(),
                            "mimeType": t.string().optional(),
                        }
                    ).optional(),
                }
            ).optional(),
            "contentRestrictions": t.array(
                t.proxy(renames["ContentRestrictionOut"])
            ).optional(),
            "copyRequiresWriterPermission": t.boolean().optional(),
            "createdTime": t.string().optional(),
            "description": t.string().optional(),
            "driveId": t.string().optional(),
            "explicitlyTrashed": t.boolean().optional(),
            "exportLinks": t.struct({"_": t.string().optional()}).optional(),
            "fileExtension": t.string().optional(),
            "folderColorRgb": t.string().optional(),
            "fullFileExtension": t.string().optional(),
            "hasAugmentedPermissions": t.boolean().optional(),
            "hasThumbnail": t.boolean().optional(),
            "headRevisionId": t.string().optional(),
            "iconLink": t.string().optional(),
            "id": t.string().optional(),
            "imageMediaMetadata": t.struct(
                {
                    "aperture": t.number().optional(),
                    "cameraMake": t.string().optional(),
                    "cameraModel": t.string().optional(),
                    "colorSpace": t.string().optional(),
                    "exposureBias": t.number().optional(),
                    "exposureMode": t.string().optional(),
                    "exposureTime": t.number().optional(),
                    "flashUsed": t.boolean().optional(),
                    "focalLength": t.number().optional(),
                    "height": t.integer().optional(),
                    "isoSpeed": t.integer().optional(),
                    "lens": t.string().optional(),
                    "location": t.struct(
                        {
                            "altitude": t.number().optional(),
                            "latitude": t.number().optional(),
                            "longitude": t.number().optional(),
                        }
                    ).optional(),
                    "maxApertureValue": t.number().optional(),
                    "meteringMode": t.string().optional(),
                    "rotation": t.integer().optional(),
                    "sensor": t.string().optional(),
                    "subjectDistance": t.integer().optional(),
                    "time": t.string().optional(),
                    "whiteBalance": t.string().optional(),
                    "width": t.integer().optional(),
                }
            ).optional(),
            "isAppAuthorized": t.boolean().optional(),
            "kind": t.string().optional(),
            "labelInfo": t.struct(
                {"labels": t.array(t.proxy(renames["LabelOut"])).optional()}
            ).optional(),
            "lastModifyingUser": t.proxy(renames["UserOut"]).optional(),
            "linkShareMetadata": t.struct(
                {
                    "securityUpdateEligible": t.boolean().optional(),
                    "securityUpdateEnabled": t.boolean().optional(),
                }
            ).optional(),
            "md5Checksum": t.string().optional(),
            "mimeType": t.string().optional(),
            "modifiedByMe": t.boolean().optional(),
            "modifiedByMeTime": t.string().optional(),
            "modifiedTime": t.string().optional(),
            "name": t.string().optional(),
            "originalFilename": t.string().optional(),
            "ownedByMe": t.boolean().optional(),
            "owners": t.array(t.proxy(renames["UserOut"])).optional(),
            "parents": t.array(t.string()).optional(),
            "permissionIds": t.array(t.string()).optional(),
            "permissions": t.array(t.proxy(renames["PermissionOut"])).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "quotaBytesUsed": t.string().optional(),
            "resourceKey": t.string().optional(),
            "sha1Checksum": t.string().optional(),
            "sha256Checksum": t.string().optional(),
            "shared": t.boolean().optional(),
            "sharedWithMeTime": t.string().optional(),
            "sharingUser": t.proxy(renames["UserOut"]).optional(),
            "shortcutDetails": t.struct(
                {
                    "targetId": t.string().optional(),
                    "targetMimeType": t.string().optional(),
                    "targetResourceKey": t.string().optional(),
                }
            ).optional(),
            "size": t.string().optional(),
            "spaces": t.array(t.string()).optional(),
            "starred": t.boolean().optional(),
            "teamDriveId": t.string().optional(),
            "thumbnailLink": t.string().optional(),
            "thumbnailVersion": t.string().optional(),
            "trashed": t.boolean().optional(),
            "trashedTime": t.string().optional(),
            "trashingUser": t.proxy(renames["UserOut"]).optional(),
            "version": t.string().optional(),
            "videoMediaMetadata": t.struct(
                {
                    "durationMillis": t.string().optional(),
                    "height": t.integer().optional(),
                    "width": t.integer().optional(),
                }
            ).optional(),
            "viewedByMe": t.boolean().optional(),
            "viewedByMeTime": t.string().optional(),
            "viewersCanCopyContent": t.boolean().optional(),
            "webContentLink": t.string().optional(),
            "webViewLink": t.string().optional(),
            "writersCanShare": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
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
    types["GeneratedIdsIn"] = t.struct(
        {
            "ids": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "space": t.string().optional(),
        }
    ).named(renames["GeneratedIdsIn"])
    types["GeneratedIdsOut"] = t.struct(
        {
            "ids": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "space": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeneratedIdsOut"])
    types["LabelIn"] = t.struct(
        {
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "revisionId": t.string().optional(),
        }
    ).named(renames["LabelIn"])
    types["LabelOut"] = t.struct(
        {
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "revisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelOut"])
    types["LabelFieldIn"] = t.struct(
        {
            "dateString": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "integer": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "selection": t.array(t.string()).optional(),
            "text": t.array(t.string()).optional(),
            "user": t.array(t.proxy(renames["UserIn"])).optional(),
            "valueType": t.string().optional(),
        }
    ).named(renames["LabelFieldIn"])
    types["LabelFieldOut"] = t.struct(
        {
            "dateString": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "integer": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "selection": t.array(t.string()).optional(),
            "text": t.array(t.string()).optional(),
            "user": t.array(t.proxy(renames["UserOut"])).optional(),
            "valueType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelFieldOut"])
    types["LabelFieldModificationIn"] = t.struct(
        {
            "fieldId": t.string().optional(),
            "kind": t.string().optional(),
            "setDateValues": t.array(t.string()).optional(),
            "setIntegerValues": t.array(t.string()).optional(),
            "setSelectionValues": t.array(t.string()).optional(),
            "setTextValues": t.array(t.string()).optional(),
            "setUserValues": t.array(t.string()).optional(),
            "unsetValues": t.boolean().optional(),
        }
    ).named(renames["LabelFieldModificationIn"])
    types["LabelFieldModificationOut"] = t.struct(
        {
            "fieldId": t.string().optional(),
            "kind": t.string().optional(),
            "setDateValues": t.array(t.string()).optional(),
            "setIntegerValues": t.array(t.string()).optional(),
            "setSelectionValues": t.array(t.string()).optional(),
            "setTextValues": t.array(t.string()).optional(),
            "setUserValues": t.array(t.string()).optional(),
            "unsetValues": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelFieldModificationOut"])
    types["LabelListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["LabelListIn"])
    types["LabelListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelListOut"])
    types["LabelModificationIn"] = t.struct(
        {
            "fieldModifications": t.array(
                t.proxy(renames["LabelFieldModificationIn"])
            ).optional(),
            "kind": t.string().optional(),
            "labelId": t.string().optional(),
            "removeLabel": t.boolean().optional(),
        }
    ).named(renames["LabelModificationIn"])
    types["LabelModificationOut"] = t.struct(
        {
            "fieldModifications": t.array(
                t.proxy(renames["LabelFieldModificationOut"])
            ).optional(),
            "kind": t.string().optional(),
            "labelId": t.string().optional(),
            "removeLabel": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelModificationOut"])
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
    types["ModifyLabelsResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "modifiedLabels": t.array(t.proxy(renames["LabelIn"])).optional(),
        }
    ).named(renames["ModifyLabelsResponseIn"])
    types["ModifyLabelsResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "modifiedLabels": t.array(t.proxy(renames["LabelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyLabelsResponseOut"])
    types["PermissionIn"] = t.struct(
        {
            "allowFileDiscovery": t.boolean().optional(),
            "deleted": t.boolean().optional(),
            "displayName": t.string().optional(),
            "domain": t.string().optional(),
            "emailAddress": t.string().optional(),
            "expirationTime": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "pendingOwner": t.boolean().optional(),
            "photoLink": t.string().optional(),
            "role": t.string().optional(),
            "type": t.string().optional(),
            "view": t.string().optional(),
        }
    ).named(renames["PermissionIn"])
    types["PermissionOut"] = t.struct(
        {
            "allowFileDiscovery": t.boolean().optional(),
            "deleted": t.boolean().optional(),
            "displayName": t.string().optional(),
            "domain": t.string().optional(),
            "emailAddress": t.string().optional(),
            "expirationTime": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "pendingOwner": t.boolean().optional(),
            "permissionDetails": t.array(
                t.struct(
                    {
                        "inherited": t.boolean().optional(),
                        "inheritedFrom": t.string().optional(),
                        "permissionType": t.string().optional(),
                        "role": t.string().optional(),
                    }
                )
            ).optional(),
            "photoLink": t.string().optional(),
            "role": t.string().optional(),
            "teamDrivePermissionDetails": t.array(
                t.struct(
                    {
                        "inherited": t.boolean().optional(),
                        "inheritedFrom": t.string().optional(),
                        "role": t.string().optional(),
                        "teamDrivePermissionType": t.string().optional(),
                    }
                )
            ).optional(),
            "type": t.string().optional(),
            "view": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionOut"])
    types["PermissionListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "permissions": t.array(t.proxy(renames["PermissionIn"])).optional(),
        }
    ).named(renames["PermissionListIn"])
    types["PermissionListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "permissions": t.array(t.proxy(renames["PermissionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionListOut"])
    types["ReplyIn"] = t.struct(
        {
            "action": t.string().optional(),
            "author": t.proxy(renames["UserIn"]).optional(),
            "content": t.string().optional(),
            "createdTime": t.string().optional(),
            "deleted": t.boolean().optional(),
            "htmlContent": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "modifiedTime": t.string().optional(),
        }
    ).named(renames["ReplyIn"])
    types["ReplyOut"] = t.struct(
        {
            "action": t.string().optional(),
            "author": t.proxy(renames["UserOut"]).optional(),
            "content": t.string().optional(),
            "createdTime": t.string().optional(),
            "deleted": t.boolean().optional(),
            "htmlContent": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "modifiedTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplyOut"])
    types["ReplyListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "replies": t.array(t.proxy(renames["ReplyIn"])).optional(),
        }
    ).named(renames["ReplyListIn"])
    types["ReplyListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "replies": t.array(t.proxy(renames["ReplyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplyListOut"])
    types["RevisionIn"] = t.struct(
        {
            "exportLinks": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "keepForever": t.boolean().optional(),
            "kind": t.string().optional(),
            "lastModifyingUser": t.proxy(renames["UserIn"]).optional(),
            "md5Checksum": t.string().optional(),
            "mimeType": t.string().optional(),
            "modifiedTime": t.string().optional(),
            "originalFilename": t.string().optional(),
            "publishAuto": t.boolean().optional(),
            "published": t.boolean().optional(),
            "publishedLink": t.string().optional(),
            "publishedOutsideDomain": t.boolean().optional(),
            "size": t.string().optional(),
        }
    ).named(renames["RevisionIn"])
    types["RevisionOut"] = t.struct(
        {
            "exportLinks": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "keepForever": t.boolean().optional(),
            "kind": t.string().optional(),
            "lastModifyingUser": t.proxy(renames["UserOut"]).optional(),
            "md5Checksum": t.string().optional(),
            "mimeType": t.string().optional(),
            "modifiedTime": t.string().optional(),
            "originalFilename": t.string().optional(),
            "publishAuto": t.boolean().optional(),
            "published": t.boolean().optional(),
            "publishedLink": t.string().optional(),
            "publishedOutsideDomain": t.boolean().optional(),
            "size": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevisionOut"])
    types["RevisionListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "revisions": t.array(t.proxy(renames["RevisionIn"])).optional(),
        }
    ).named(renames["RevisionListIn"])
    types["RevisionListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "revisions": t.array(t.proxy(renames["RevisionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevisionListOut"])
    types["StartPageTokenIn"] = t.struct(
        {"kind": t.string().optional(), "startPageToken": t.string().optional()}
    ).named(renames["StartPageTokenIn"])
    types["StartPageTokenOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "startPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartPageTokenOut"])
    types["TeamDriveIn"] = t.struct(
        {
            "backgroundImageFile": t.struct(
                {
                    "id": t.string().optional(),
                    "width": t.number().optional(),
                    "xCoordinate": t.number().optional(),
                    "yCoordinate": t.number().optional(),
                }
            ).optional(),
            "backgroundImageLink": t.string().optional(),
            "capabilities": t.struct(
                {
                    "canAddChildren": t.boolean().optional(),
                    "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                    "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                    "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                    "canChangeTeamDriveBackground": t.boolean().optional(),
                    "canChangeTeamMembersOnlyRestriction": t.boolean().optional(),
                    "canComment": t.boolean().optional(),
                    "canCopy": t.boolean().optional(),
                    "canDeleteChildren": t.boolean().optional(),
                    "canDeleteTeamDrive": t.boolean().optional(),
                    "canDownload": t.boolean().optional(),
                    "canEdit": t.boolean().optional(),
                    "canListChildren": t.boolean().optional(),
                    "canManageMembers": t.boolean().optional(),
                    "canReadRevisions": t.boolean().optional(),
                    "canRemoveChildren": t.boolean().optional(),
                    "canRename": t.boolean().optional(),
                    "canRenameTeamDrive": t.boolean().optional(),
                    "canResetTeamDriveRestrictions": t.boolean().optional(),
                    "canShare": t.boolean().optional(),
                    "canTrashChildren": t.boolean().optional(),
                }
            ).optional(),
            "colorRgb": t.string().optional(),
            "createdTime": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "orgUnitId": t.string().optional(),
            "restrictions": t.struct(
                {
                    "adminManagedRestrictions": t.boolean().optional(),
                    "copyRequiresWriterPermission": t.boolean().optional(),
                    "domainUsersOnly": t.boolean().optional(),
                    "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                    "teamMembersOnly": t.boolean().optional(),
                }
            ).optional(),
            "themeId": t.string().optional(),
        }
    ).named(renames["TeamDriveIn"])
    types["TeamDriveOut"] = t.struct(
        {
            "backgroundImageFile": t.struct(
                {
                    "id": t.string().optional(),
                    "width": t.number().optional(),
                    "xCoordinate": t.number().optional(),
                    "yCoordinate": t.number().optional(),
                }
            ).optional(),
            "backgroundImageLink": t.string().optional(),
            "capabilities": t.struct(
                {
                    "canAddChildren": t.boolean().optional(),
                    "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                    "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                    "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                    "canChangeTeamDriveBackground": t.boolean().optional(),
                    "canChangeTeamMembersOnlyRestriction": t.boolean().optional(),
                    "canComment": t.boolean().optional(),
                    "canCopy": t.boolean().optional(),
                    "canDeleteChildren": t.boolean().optional(),
                    "canDeleteTeamDrive": t.boolean().optional(),
                    "canDownload": t.boolean().optional(),
                    "canEdit": t.boolean().optional(),
                    "canListChildren": t.boolean().optional(),
                    "canManageMembers": t.boolean().optional(),
                    "canReadRevisions": t.boolean().optional(),
                    "canRemoveChildren": t.boolean().optional(),
                    "canRename": t.boolean().optional(),
                    "canRenameTeamDrive": t.boolean().optional(),
                    "canResetTeamDriveRestrictions": t.boolean().optional(),
                    "canShare": t.boolean().optional(),
                    "canTrashChildren": t.boolean().optional(),
                }
            ).optional(),
            "colorRgb": t.string().optional(),
            "createdTime": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "orgUnitId": t.string().optional(),
            "restrictions": t.struct(
                {
                    "adminManagedRestrictions": t.boolean().optional(),
                    "copyRequiresWriterPermission": t.boolean().optional(),
                    "domainUsersOnly": t.boolean().optional(),
                    "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                    "teamMembersOnly": t.boolean().optional(),
                }
            ).optional(),
            "themeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TeamDriveOut"])
    types["TeamDriveListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "teamDrives": t.array(t.proxy(renames["TeamDriveIn"])).optional(),
        }
    ).named(renames["TeamDriveListIn"])
    types["TeamDriveListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "teamDrives": t.array(t.proxy(renames["TeamDriveOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TeamDriveListOut"])
    types["UserIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "emailAddress": t.string().optional(),
            "kind": t.string().optional(),
            "me": t.boolean().optional(),
            "permissionId": t.string().optional(),
            "photoLink": t.string().optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "emailAddress": t.string().optional(),
            "kind": t.string().optional(),
            "me": t.boolean().optional(),
            "permissionId": t.string().optional(),
            "photoLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])

    functions = {}
    functions["aboutGet"] = drive.get(
        "about",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["AboutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["changesGetStartPageToken"] = drive.post(
        "changes/watch",
        t.struct(
            {
                "driveId": t.string().optional(),
                "includeCorpusRemovals": t.boolean().optional(),
                "includeItemsFromAllDrives": t.boolean().optional(),
                "includeLabels": t.string().optional(),
                "includePermissionsForView": t.string().optional(),
                "includeRemoved": t.boolean().optional(),
                "includeTeamDriveItems": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "restrictToMyDrive": t.boolean().optional(),
                "spaces": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "teamDriveId": t.string().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["changesList"] = drive.post(
        "changes/watch",
        t.struct(
            {
                "driveId": t.string().optional(),
                "includeCorpusRemovals": t.boolean().optional(),
                "includeItemsFromAllDrives": t.boolean().optional(),
                "includeLabels": t.string().optional(),
                "includePermissionsForView": t.string().optional(),
                "includeRemoved": t.boolean().optional(),
                "includeTeamDriveItems": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "restrictToMyDrive": t.boolean().optional(),
                "spaces": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "teamDriveId": t.string().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["changesWatch"] = drive.post(
        "changes/watch",
        t.struct(
            {
                "driveId": t.string().optional(),
                "includeCorpusRemovals": t.boolean().optional(),
                "includeItemsFromAllDrives": t.boolean().optional(),
                "includeLabels": t.string().optional(),
                "includePermissionsForView": t.string().optional(),
                "includeRemoved": t.boolean().optional(),
                "includeTeamDriveItems": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "restrictToMyDrive": t.boolean().optional(),
                "spaces": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "teamDriveId": t.string().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["channelsStop"] = drive.post(
        "channels/stop",
        t.struct(
            {
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsCreate"] = drive.patch(
        "files/{fileId}/comments/{commentId}",
        t.struct(
            {
                "commentId": t.string().optional(),
                "fileId": t.string().optional(),
                "anchor": t.string().optional(),
                "author": t.proxy(renames["UserIn"]).optional(),
                "content": t.string().optional(),
                "createdTime": t.string().optional(),
                "deleted": t.boolean().optional(),
                "htmlContent": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "quotedFileContent": t.struct(
                    {"mimeType": t.string().optional(), "value": t.string().optional()}
                ).optional(),
                "replies": t.array(t.proxy(renames["ReplyIn"])).optional(),
                "resolved": t.boolean().optional(),
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
                "commentId": t.string().optional(),
                "fileId": t.string().optional(),
                "anchor": t.string().optional(),
                "author": t.proxy(renames["UserIn"]).optional(),
                "content": t.string().optional(),
                "createdTime": t.string().optional(),
                "deleted": t.boolean().optional(),
                "htmlContent": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "quotedFileContent": t.struct(
                    {"mimeType": t.string().optional(), "value": t.string().optional()}
                ).optional(),
                "replies": t.array(t.proxy(renames["ReplyIn"])).optional(),
                "resolved": t.boolean().optional(),
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
                "commentId": t.string().optional(),
                "fileId": t.string().optional(),
                "anchor": t.string().optional(),
                "author": t.proxy(renames["UserIn"]).optional(),
                "content": t.string().optional(),
                "createdTime": t.string().optional(),
                "deleted": t.boolean().optional(),
                "htmlContent": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "quotedFileContent": t.struct(
                    {"mimeType": t.string().optional(), "value": t.string().optional()}
                ).optional(),
                "replies": t.array(t.proxy(renames["ReplyIn"])).optional(),
                "resolved": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsList"] = drive.patch(
        "files/{fileId}/comments/{commentId}",
        t.struct(
            {
                "commentId": t.string().optional(),
                "fileId": t.string().optional(),
                "anchor": t.string().optional(),
                "author": t.proxy(renames["UserIn"]).optional(),
                "content": t.string().optional(),
                "createdTime": t.string().optional(),
                "deleted": t.boolean().optional(),
                "htmlContent": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "quotedFileContent": t.struct(
                    {"mimeType": t.string().optional(), "value": t.string().optional()}
                ).optional(),
                "replies": t.array(t.proxy(renames["ReplyIn"])).optional(),
                "resolved": t.boolean().optional(),
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
                "commentId": t.string().optional(),
                "fileId": t.string().optional(),
                "anchor": t.string().optional(),
                "author": t.proxy(renames["UserIn"]).optional(),
                "content": t.string().optional(),
                "createdTime": t.string().optional(),
                "deleted": t.boolean().optional(),
                "htmlContent": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "quotedFileContent": t.struct(
                    {"mimeType": t.string().optional(), "value": t.string().optional()}
                ).optional(),
                "replies": t.array(t.proxy(renames["ReplyIn"])).optional(),
                "resolved": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["drivesCreate"] = drive.patch(
        "drives/{driveId}",
        t.struct(
            {
                "driveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "backgroundImageFile": t.struct(
                    {
                        "id": t.string().optional(),
                        "width": t.number().optional(),
                        "xCoordinate": t.number().optional(),
                        "yCoordinate": t.number().optional(),
                    }
                ).optional(),
                "backgroundImageLink": t.string().optional(),
                "capabilities": t.struct(
                    {
                        "canAddChildren": t.boolean().optional(),
                        "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                        "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                        "canChangeDriveBackground": t.boolean().optional(),
                        "canChangeDriveMembersOnlyRestriction": t.boolean().optional(),
                        "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                        "canComment": t.boolean().optional(),
                        "canCopy": t.boolean().optional(),
                        "canDeleteChildren": t.boolean().optional(),
                        "canDeleteDrive": t.boolean().optional(),
                        "canDownload": t.boolean().optional(),
                        "canEdit": t.boolean().optional(),
                        "canListChildren": t.boolean().optional(),
                        "canManageMembers": t.boolean().optional(),
                        "canReadRevisions": t.boolean().optional(),
                        "canRename": t.boolean().optional(),
                        "canRenameDrive": t.boolean().optional(),
                        "canResetDriveRestrictions": t.boolean().optional(),
                        "canShare": t.boolean().optional(),
                        "canTrashChildren": t.boolean().optional(),
                    }
                ).optional(),
                "colorRgb": t.string().optional(),
                "createdTime": t.string().optional(),
                "hidden": t.boolean().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "orgUnitId": t.string().optional(),
                "restrictions": t.struct(
                    {
                        "adminManagedRestrictions": t.boolean().optional(),
                        "copyRequiresWriterPermission": t.boolean().optional(),
                        "domainUsersOnly": t.boolean().optional(),
                        "driveMembersOnly": t.boolean().optional(),
                        "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                    }
                ).optional(),
                "themeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["drivesDelete"] = drive.patch(
        "drives/{driveId}",
        t.struct(
            {
                "driveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "backgroundImageFile": t.struct(
                    {
                        "id": t.string().optional(),
                        "width": t.number().optional(),
                        "xCoordinate": t.number().optional(),
                        "yCoordinate": t.number().optional(),
                    }
                ).optional(),
                "backgroundImageLink": t.string().optional(),
                "capabilities": t.struct(
                    {
                        "canAddChildren": t.boolean().optional(),
                        "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                        "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                        "canChangeDriveBackground": t.boolean().optional(),
                        "canChangeDriveMembersOnlyRestriction": t.boolean().optional(),
                        "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                        "canComment": t.boolean().optional(),
                        "canCopy": t.boolean().optional(),
                        "canDeleteChildren": t.boolean().optional(),
                        "canDeleteDrive": t.boolean().optional(),
                        "canDownload": t.boolean().optional(),
                        "canEdit": t.boolean().optional(),
                        "canListChildren": t.boolean().optional(),
                        "canManageMembers": t.boolean().optional(),
                        "canReadRevisions": t.boolean().optional(),
                        "canRename": t.boolean().optional(),
                        "canRenameDrive": t.boolean().optional(),
                        "canResetDriveRestrictions": t.boolean().optional(),
                        "canShare": t.boolean().optional(),
                        "canTrashChildren": t.boolean().optional(),
                    }
                ).optional(),
                "colorRgb": t.string().optional(),
                "createdTime": t.string().optional(),
                "hidden": t.boolean().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "orgUnitId": t.string().optional(),
                "restrictions": t.struct(
                    {
                        "adminManagedRestrictions": t.boolean().optional(),
                        "copyRequiresWriterPermission": t.boolean().optional(),
                        "domainUsersOnly": t.boolean().optional(),
                        "driveMembersOnly": t.boolean().optional(),
                        "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                    }
                ).optional(),
                "themeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["drivesGet"] = drive.patch(
        "drives/{driveId}",
        t.struct(
            {
                "driveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "backgroundImageFile": t.struct(
                    {
                        "id": t.string().optional(),
                        "width": t.number().optional(),
                        "xCoordinate": t.number().optional(),
                        "yCoordinate": t.number().optional(),
                    }
                ).optional(),
                "backgroundImageLink": t.string().optional(),
                "capabilities": t.struct(
                    {
                        "canAddChildren": t.boolean().optional(),
                        "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                        "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                        "canChangeDriveBackground": t.boolean().optional(),
                        "canChangeDriveMembersOnlyRestriction": t.boolean().optional(),
                        "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                        "canComment": t.boolean().optional(),
                        "canCopy": t.boolean().optional(),
                        "canDeleteChildren": t.boolean().optional(),
                        "canDeleteDrive": t.boolean().optional(),
                        "canDownload": t.boolean().optional(),
                        "canEdit": t.boolean().optional(),
                        "canListChildren": t.boolean().optional(),
                        "canManageMembers": t.boolean().optional(),
                        "canReadRevisions": t.boolean().optional(),
                        "canRename": t.boolean().optional(),
                        "canRenameDrive": t.boolean().optional(),
                        "canResetDriveRestrictions": t.boolean().optional(),
                        "canShare": t.boolean().optional(),
                        "canTrashChildren": t.boolean().optional(),
                    }
                ).optional(),
                "colorRgb": t.string().optional(),
                "createdTime": t.string().optional(),
                "hidden": t.boolean().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "orgUnitId": t.string().optional(),
                "restrictions": t.struct(
                    {
                        "adminManagedRestrictions": t.boolean().optional(),
                        "copyRequiresWriterPermission": t.boolean().optional(),
                        "domainUsersOnly": t.boolean().optional(),
                        "driveMembersOnly": t.boolean().optional(),
                        "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                    }
                ).optional(),
                "themeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["drivesHide"] = drive.patch(
        "drives/{driveId}",
        t.struct(
            {
                "driveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "backgroundImageFile": t.struct(
                    {
                        "id": t.string().optional(),
                        "width": t.number().optional(),
                        "xCoordinate": t.number().optional(),
                        "yCoordinate": t.number().optional(),
                    }
                ).optional(),
                "backgroundImageLink": t.string().optional(),
                "capabilities": t.struct(
                    {
                        "canAddChildren": t.boolean().optional(),
                        "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                        "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                        "canChangeDriveBackground": t.boolean().optional(),
                        "canChangeDriveMembersOnlyRestriction": t.boolean().optional(),
                        "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                        "canComment": t.boolean().optional(),
                        "canCopy": t.boolean().optional(),
                        "canDeleteChildren": t.boolean().optional(),
                        "canDeleteDrive": t.boolean().optional(),
                        "canDownload": t.boolean().optional(),
                        "canEdit": t.boolean().optional(),
                        "canListChildren": t.boolean().optional(),
                        "canManageMembers": t.boolean().optional(),
                        "canReadRevisions": t.boolean().optional(),
                        "canRename": t.boolean().optional(),
                        "canRenameDrive": t.boolean().optional(),
                        "canResetDriveRestrictions": t.boolean().optional(),
                        "canShare": t.boolean().optional(),
                        "canTrashChildren": t.boolean().optional(),
                    }
                ).optional(),
                "colorRgb": t.string().optional(),
                "createdTime": t.string().optional(),
                "hidden": t.boolean().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "orgUnitId": t.string().optional(),
                "restrictions": t.struct(
                    {
                        "adminManagedRestrictions": t.boolean().optional(),
                        "copyRequiresWriterPermission": t.boolean().optional(),
                        "domainUsersOnly": t.boolean().optional(),
                        "driveMembersOnly": t.boolean().optional(),
                        "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                    }
                ).optional(),
                "themeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["drivesList"] = drive.patch(
        "drives/{driveId}",
        t.struct(
            {
                "driveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "backgroundImageFile": t.struct(
                    {
                        "id": t.string().optional(),
                        "width": t.number().optional(),
                        "xCoordinate": t.number().optional(),
                        "yCoordinate": t.number().optional(),
                    }
                ).optional(),
                "backgroundImageLink": t.string().optional(),
                "capabilities": t.struct(
                    {
                        "canAddChildren": t.boolean().optional(),
                        "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                        "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                        "canChangeDriveBackground": t.boolean().optional(),
                        "canChangeDriveMembersOnlyRestriction": t.boolean().optional(),
                        "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                        "canComment": t.boolean().optional(),
                        "canCopy": t.boolean().optional(),
                        "canDeleteChildren": t.boolean().optional(),
                        "canDeleteDrive": t.boolean().optional(),
                        "canDownload": t.boolean().optional(),
                        "canEdit": t.boolean().optional(),
                        "canListChildren": t.boolean().optional(),
                        "canManageMembers": t.boolean().optional(),
                        "canReadRevisions": t.boolean().optional(),
                        "canRename": t.boolean().optional(),
                        "canRenameDrive": t.boolean().optional(),
                        "canResetDriveRestrictions": t.boolean().optional(),
                        "canShare": t.boolean().optional(),
                        "canTrashChildren": t.boolean().optional(),
                    }
                ).optional(),
                "colorRgb": t.string().optional(),
                "createdTime": t.string().optional(),
                "hidden": t.boolean().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "orgUnitId": t.string().optional(),
                "restrictions": t.struct(
                    {
                        "adminManagedRestrictions": t.boolean().optional(),
                        "copyRequiresWriterPermission": t.boolean().optional(),
                        "domainUsersOnly": t.boolean().optional(),
                        "driveMembersOnly": t.boolean().optional(),
                        "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                    }
                ).optional(),
                "themeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["drivesUnhide"] = drive.patch(
        "drives/{driveId}",
        t.struct(
            {
                "driveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "backgroundImageFile": t.struct(
                    {
                        "id": t.string().optional(),
                        "width": t.number().optional(),
                        "xCoordinate": t.number().optional(),
                        "yCoordinate": t.number().optional(),
                    }
                ).optional(),
                "backgroundImageLink": t.string().optional(),
                "capabilities": t.struct(
                    {
                        "canAddChildren": t.boolean().optional(),
                        "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                        "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                        "canChangeDriveBackground": t.boolean().optional(),
                        "canChangeDriveMembersOnlyRestriction": t.boolean().optional(),
                        "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                        "canComment": t.boolean().optional(),
                        "canCopy": t.boolean().optional(),
                        "canDeleteChildren": t.boolean().optional(),
                        "canDeleteDrive": t.boolean().optional(),
                        "canDownload": t.boolean().optional(),
                        "canEdit": t.boolean().optional(),
                        "canListChildren": t.boolean().optional(),
                        "canManageMembers": t.boolean().optional(),
                        "canReadRevisions": t.boolean().optional(),
                        "canRename": t.boolean().optional(),
                        "canRenameDrive": t.boolean().optional(),
                        "canResetDriveRestrictions": t.boolean().optional(),
                        "canShare": t.boolean().optional(),
                        "canTrashChildren": t.boolean().optional(),
                    }
                ).optional(),
                "colorRgb": t.string().optional(),
                "createdTime": t.string().optional(),
                "hidden": t.boolean().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "orgUnitId": t.string().optional(),
                "restrictions": t.struct(
                    {
                        "adminManagedRestrictions": t.boolean().optional(),
                        "copyRequiresWriterPermission": t.boolean().optional(),
                        "domainUsersOnly": t.boolean().optional(),
                        "driveMembersOnly": t.boolean().optional(),
                        "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                    }
                ).optional(),
                "themeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["drivesUpdate"] = drive.patch(
        "drives/{driveId}",
        t.struct(
            {
                "driveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "backgroundImageFile": t.struct(
                    {
                        "id": t.string().optional(),
                        "width": t.number().optional(),
                        "xCoordinate": t.number().optional(),
                        "yCoordinate": t.number().optional(),
                    }
                ).optional(),
                "backgroundImageLink": t.string().optional(),
                "capabilities": t.struct(
                    {
                        "canAddChildren": t.boolean().optional(),
                        "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                        "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                        "canChangeDriveBackground": t.boolean().optional(),
                        "canChangeDriveMembersOnlyRestriction": t.boolean().optional(),
                        "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                        "canComment": t.boolean().optional(),
                        "canCopy": t.boolean().optional(),
                        "canDeleteChildren": t.boolean().optional(),
                        "canDeleteDrive": t.boolean().optional(),
                        "canDownload": t.boolean().optional(),
                        "canEdit": t.boolean().optional(),
                        "canListChildren": t.boolean().optional(),
                        "canManageMembers": t.boolean().optional(),
                        "canReadRevisions": t.boolean().optional(),
                        "canRename": t.boolean().optional(),
                        "canRenameDrive": t.boolean().optional(),
                        "canResetDriveRestrictions": t.boolean().optional(),
                        "canShare": t.boolean().optional(),
                        "canTrashChildren": t.boolean().optional(),
                    }
                ).optional(),
                "colorRgb": t.string().optional(),
                "createdTime": t.string().optional(),
                "hidden": t.boolean().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "orgUnitId": t.string().optional(),
                "restrictions": t.struct(
                    {
                        "adminManagedRestrictions": t.boolean().optional(),
                        "copyRequiresWriterPermission": t.boolean().optional(),
                        "domainUsersOnly": t.boolean().optional(),
                        "driveMembersOnly": t.boolean().optional(),
                        "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                    }
                ).optional(),
                "themeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesCopy"] = drive.post(
        "files/{fileId}/watch",
        t.struct(
            {
                "acknowledgeAbuse": t.boolean().optional(),
                "fileId": t.string().optional(),
                "includeLabels": t.string().optional(),
                "includePermissionsForView": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesCreate"] = drive.post(
        "files/{fileId}/watch",
        t.struct(
            {
                "acknowledgeAbuse": t.boolean().optional(),
                "fileId": t.string().optional(),
                "includeLabels": t.string().optional(),
                "includePermissionsForView": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesDelete"] = drive.post(
        "files/{fileId}/watch",
        t.struct(
            {
                "acknowledgeAbuse": t.boolean().optional(),
                "fileId": t.string().optional(),
                "includeLabels": t.string().optional(),
                "includePermissionsForView": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesEmptyTrash"] = drive.post(
        "files/{fileId}/watch",
        t.struct(
            {
                "acknowledgeAbuse": t.boolean().optional(),
                "fileId": t.string().optional(),
                "includeLabels": t.string().optional(),
                "includePermissionsForView": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesExport"] = drive.post(
        "files/{fileId}/watch",
        t.struct(
            {
                "acknowledgeAbuse": t.boolean().optional(),
                "fileId": t.string().optional(),
                "includeLabels": t.string().optional(),
                "includePermissionsForView": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesGenerateIds"] = drive.post(
        "files/{fileId}/watch",
        t.struct(
            {
                "acknowledgeAbuse": t.boolean().optional(),
                "fileId": t.string().optional(),
                "includeLabels": t.string().optional(),
                "includePermissionsForView": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesGet"] = drive.post(
        "files/{fileId}/watch",
        t.struct(
            {
                "acknowledgeAbuse": t.boolean().optional(),
                "fileId": t.string().optional(),
                "includeLabels": t.string().optional(),
                "includePermissionsForView": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesList"] = drive.post(
        "files/{fileId}/watch",
        t.struct(
            {
                "acknowledgeAbuse": t.boolean().optional(),
                "fileId": t.string().optional(),
                "includeLabels": t.string().optional(),
                "includePermissionsForView": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesListLabels"] = drive.post(
        "files/{fileId}/watch",
        t.struct(
            {
                "acknowledgeAbuse": t.boolean().optional(),
                "fileId": t.string().optional(),
                "includeLabels": t.string().optional(),
                "includePermissionsForView": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesModifyLabels"] = drive.post(
        "files/{fileId}/watch",
        t.struct(
            {
                "acknowledgeAbuse": t.boolean().optional(),
                "fileId": t.string().optional(),
                "includeLabels": t.string().optional(),
                "includePermissionsForView": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesUpdate"] = drive.post(
        "files/{fileId}/watch",
        t.struct(
            {
                "acknowledgeAbuse": t.boolean().optional(),
                "fileId": t.string().optional(),
                "includeLabels": t.string().optional(),
                "includePermissionsForView": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["filesWatch"] = drive.post(
        "files/{fileId}/watch",
        t.struct(
            {
                "acknowledgeAbuse": t.boolean().optional(),
                "fileId": t.string().optional(),
                "includeLabels": t.string().optional(),
                "includePermissionsForView": t.string().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["permissionsCreate"] = drive.patch(
        "files/{fileId}/permissions/{permissionId}",
        t.struct(
            {
                "fileId": t.string().optional(),
                "permissionId": t.string().optional(),
                "removeExpiration": t.boolean().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "transferOwnership": t.boolean().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "allowFileDiscovery": t.boolean().optional(),
                "deleted": t.boolean().optional(),
                "displayName": t.string().optional(),
                "domain": t.string().optional(),
                "emailAddress": t.string().optional(),
                "expirationTime": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "pendingOwner": t.boolean().optional(),
                "photoLink": t.string().optional(),
                "role": t.string().optional(),
                "type": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["permissionsDelete"] = drive.patch(
        "files/{fileId}/permissions/{permissionId}",
        t.struct(
            {
                "fileId": t.string().optional(),
                "permissionId": t.string().optional(),
                "removeExpiration": t.boolean().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "transferOwnership": t.boolean().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "allowFileDiscovery": t.boolean().optional(),
                "deleted": t.boolean().optional(),
                "displayName": t.string().optional(),
                "domain": t.string().optional(),
                "emailAddress": t.string().optional(),
                "expirationTime": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "pendingOwner": t.boolean().optional(),
                "photoLink": t.string().optional(),
                "role": t.string().optional(),
                "type": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["permissionsGet"] = drive.patch(
        "files/{fileId}/permissions/{permissionId}",
        t.struct(
            {
                "fileId": t.string().optional(),
                "permissionId": t.string().optional(),
                "removeExpiration": t.boolean().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "transferOwnership": t.boolean().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "allowFileDiscovery": t.boolean().optional(),
                "deleted": t.boolean().optional(),
                "displayName": t.string().optional(),
                "domain": t.string().optional(),
                "emailAddress": t.string().optional(),
                "expirationTime": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "pendingOwner": t.boolean().optional(),
                "photoLink": t.string().optional(),
                "role": t.string().optional(),
                "type": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["permissionsList"] = drive.patch(
        "files/{fileId}/permissions/{permissionId}",
        t.struct(
            {
                "fileId": t.string().optional(),
                "permissionId": t.string().optional(),
                "removeExpiration": t.boolean().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "transferOwnership": t.boolean().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "allowFileDiscovery": t.boolean().optional(),
                "deleted": t.boolean().optional(),
                "displayName": t.string().optional(),
                "domain": t.string().optional(),
                "emailAddress": t.string().optional(),
                "expirationTime": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "pendingOwner": t.boolean().optional(),
                "photoLink": t.string().optional(),
                "role": t.string().optional(),
                "type": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["permissionsUpdate"] = drive.patch(
        "files/{fileId}/permissions/{permissionId}",
        t.struct(
            {
                "fileId": t.string().optional(),
                "permissionId": t.string().optional(),
                "removeExpiration": t.boolean().optional(),
                "supportsAllDrives": t.boolean().optional(),
                "supportsTeamDrives": t.boolean().optional(),
                "transferOwnership": t.boolean().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "allowFileDiscovery": t.boolean().optional(),
                "deleted": t.boolean().optional(),
                "displayName": t.string().optional(),
                "domain": t.string().optional(),
                "emailAddress": t.string().optional(),
                "expirationTime": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "pendingOwner": t.boolean().optional(),
                "photoLink": t.string().optional(),
                "role": t.string().optional(),
                "type": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repliesCreate"] = drive.patch(
        "files/{fileId}/comments/{commentId}/replies/{replyId}",
        t.struct(
            {
                "commentId": t.string().optional(),
                "fileId": t.string().optional(),
                "replyId": t.string().optional(),
                "action": t.string().optional(),
                "author": t.proxy(renames["UserIn"]).optional(),
                "content": t.string().optional(),
                "createdTime": t.string().optional(),
                "deleted": t.boolean().optional(),
                "htmlContent": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReplyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repliesDelete"] = drive.patch(
        "files/{fileId}/comments/{commentId}/replies/{replyId}",
        t.struct(
            {
                "commentId": t.string().optional(),
                "fileId": t.string().optional(),
                "replyId": t.string().optional(),
                "action": t.string().optional(),
                "author": t.proxy(renames["UserIn"]).optional(),
                "content": t.string().optional(),
                "createdTime": t.string().optional(),
                "deleted": t.boolean().optional(),
                "htmlContent": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReplyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repliesGet"] = drive.patch(
        "files/{fileId}/comments/{commentId}/replies/{replyId}",
        t.struct(
            {
                "commentId": t.string().optional(),
                "fileId": t.string().optional(),
                "replyId": t.string().optional(),
                "action": t.string().optional(),
                "author": t.proxy(renames["UserIn"]).optional(),
                "content": t.string().optional(),
                "createdTime": t.string().optional(),
                "deleted": t.boolean().optional(),
                "htmlContent": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReplyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repliesList"] = drive.patch(
        "files/{fileId}/comments/{commentId}/replies/{replyId}",
        t.struct(
            {
                "commentId": t.string().optional(),
                "fileId": t.string().optional(),
                "replyId": t.string().optional(),
                "action": t.string().optional(),
                "author": t.proxy(renames["UserIn"]).optional(),
                "content": t.string().optional(),
                "createdTime": t.string().optional(),
                "deleted": t.boolean().optional(),
                "htmlContent": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReplyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repliesUpdate"] = drive.patch(
        "files/{fileId}/comments/{commentId}/replies/{replyId}",
        t.struct(
            {
                "commentId": t.string().optional(),
                "fileId": t.string().optional(),
                "replyId": t.string().optional(),
                "action": t.string().optional(),
                "author": t.proxy(renames["UserIn"]).optional(),
                "content": t.string().optional(),
                "createdTime": t.string().optional(),
                "deleted": t.boolean().optional(),
                "htmlContent": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReplyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["revisionsDelete"] = drive.patch(
        "files/{fileId}/revisions/{revisionId}",
        t.struct(
            {
                "fileId": t.string().optional(),
                "revisionId": t.string().optional(),
                "exportLinks": t.struct({"_": t.string().optional()}).optional(),
                "id": t.string().optional(),
                "keepForever": t.boolean().optional(),
                "kind": t.string().optional(),
                "lastModifyingUser": t.proxy(renames["UserIn"]).optional(),
                "md5Checksum": t.string().optional(),
                "mimeType": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "originalFilename": t.string().optional(),
                "publishAuto": t.boolean().optional(),
                "published": t.boolean().optional(),
                "publishedLink": t.string().optional(),
                "publishedOutsideDomain": t.boolean().optional(),
                "size": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevisionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["revisionsGet"] = drive.patch(
        "files/{fileId}/revisions/{revisionId}",
        t.struct(
            {
                "fileId": t.string().optional(),
                "revisionId": t.string().optional(),
                "exportLinks": t.struct({"_": t.string().optional()}).optional(),
                "id": t.string().optional(),
                "keepForever": t.boolean().optional(),
                "kind": t.string().optional(),
                "lastModifyingUser": t.proxy(renames["UserIn"]).optional(),
                "md5Checksum": t.string().optional(),
                "mimeType": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "originalFilename": t.string().optional(),
                "publishAuto": t.boolean().optional(),
                "published": t.boolean().optional(),
                "publishedLink": t.string().optional(),
                "publishedOutsideDomain": t.boolean().optional(),
                "size": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevisionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["revisionsList"] = drive.patch(
        "files/{fileId}/revisions/{revisionId}",
        t.struct(
            {
                "fileId": t.string().optional(),
                "revisionId": t.string().optional(),
                "exportLinks": t.struct({"_": t.string().optional()}).optional(),
                "id": t.string().optional(),
                "keepForever": t.boolean().optional(),
                "kind": t.string().optional(),
                "lastModifyingUser": t.proxy(renames["UserIn"]).optional(),
                "md5Checksum": t.string().optional(),
                "mimeType": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "originalFilename": t.string().optional(),
                "publishAuto": t.boolean().optional(),
                "published": t.boolean().optional(),
                "publishedLink": t.string().optional(),
                "publishedOutsideDomain": t.boolean().optional(),
                "size": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevisionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["revisionsUpdate"] = drive.patch(
        "files/{fileId}/revisions/{revisionId}",
        t.struct(
            {
                "fileId": t.string().optional(),
                "revisionId": t.string().optional(),
                "exportLinks": t.struct({"_": t.string().optional()}).optional(),
                "id": t.string().optional(),
                "keepForever": t.boolean().optional(),
                "kind": t.string().optional(),
                "lastModifyingUser": t.proxy(renames["UserIn"]).optional(),
                "md5Checksum": t.string().optional(),
                "mimeType": t.string().optional(),
                "modifiedTime": t.string().optional(),
                "originalFilename": t.string().optional(),
                "publishAuto": t.boolean().optional(),
                "published": t.boolean().optional(),
                "publishedLink": t.string().optional(),
                "publishedOutsideDomain": t.boolean().optional(),
                "size": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RevisionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["teamdrivesCreate"] = drive.patch(
        "teamdrives/{teamDriveId}",
        t.struct(
            {
                "teamDriveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "backgroundImageFile": t.struct(
                    {
                        "id": t.string().optional(),
                        "width": t.number().optional(),
                        "xCoordinate": t.number().optional(),
                        "yCoordinate": t.number().optional(),
                    }
                ).optional(),
                "backgroundImageLink": t.string().optional(),
                "capabilities": t.struct(
                    {
                        "canAddChildren": t.boolean().optional(),
                        "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                        "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                        "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                        "canChangeTeamDriveBackground": t.boolean().optional(),
                        "canChangeTeamMembersOnlyRestriction": t.boolean().optional(),
                        "canComment": t.boolean().optional(),
                        "canCopy": t.boolean().optional(),
                        "canDeleteChildren": t.boolean().optional(),
                        "canDeleteTeamDrive": t.boolean().optional(),
                        "canDownload": t.boolean().optional(),
                        "canEdit": t.boolean().optional(),
                        "canListChildren": t.boolean().optional(),
                        "canManageMembers": t.boolean().optional(),
                        "canReadRevisions": t.boolean().optional(),
                        "canRemoveChildren": t.boolean().optional(),
                        "canRename": t.boolean().optional(),
                        "canRenameTeamDrive": t.boolean().optional(),
                        "canResetTeamDriveRestrictions": t.boolean().optional(),
                        "canShare": t.boolean().optional(),
                        "canTrashChildren": t.boolean().optional(),
                    }
                ).optional(),
                "colorRgb": t.string().optional(),
                "createdTime": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "orgUnitId": t.string().optional(),
                "restrictions": t.struct(
                    {
                        "adminManagedRestrictions": t.boolean().optional(),
                        "copyRequiresWriterPermission": t.boolean().optional(),
                        "domainUsersOnly": t.boolean().optional(),
                        "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                        "teamMembersOnly": t.boolean().optional(),
                    }
                ).optional(),
                "themeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TeamDriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["teamdrivesDelete"] = drive.patch(
        "teamdrives/{teamDriveId}",
        t.struct(
            {
                "teamDriveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "backgroundImageFile": t.struct(
                    {
                        "id": t.string().optional(),
                        "width": t.number().optional(),
                        "xCoordinate": t.number().optional(),
                        "yCoordinate": t.number().optional(),
                    }
                ).optional(),
                "backgroundImageLink": t.string().optional(),
                "capabilities": t.struct(
                    {
                        "canAddChildren": t.boolean().optional(),
                        "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                        "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                        "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                        "canChangeTeamDriveBackground": t.boolean().optional(),
                        "canChangeTeamMembersOnlyRestriction": t.boolean().optional(),
                        "canComment": t.boolean().optional(),
                        "canCopy": t.boolean().optional(),
                        "canDeleteChildren": t.boolean().optional(),
                        "canDeleteTeamDrive": t.boolean().optional(),
                        "canDownload": t.boolean().optional(),
                        "canEdit": t.boolean().optional(),
                        "canListChildren": t.boolean().optional(),
                        "canManageMembers": t.boolean().optional(),
                        "canReadRevisions": t.boolean().optional(),
                        "canRemoveChildren": t.boolean().optional(),
                        "canRename": t.boolean().optional(),
                        "canRenameTeamDrive": t.boolean().optional(),
                        "canResetTeamDriveRestrictions": t.boolean().optional(),
                        "canShare": t.boolean().optional(),
                        "canTrashChildren": t.boolean().optional(),
                    }
                ).optional(),
                "colorRgb": t.string().optional(),
                "createdTime": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "orgUnitId": t.string().optional(),
                "restrictions": t.struct(
                    {
                        "adminManagedRestrictions": t.boolean().optional(),
                        "copyRequiresWriterPermission": t.boolean().optional(),
                        "domainUsersOnly": t.boolean().optional(),
                        "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                        "teamMembersOnly": t.boolean().optional(),
                    }
                ).optional(),
                "themeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TeamDriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["teamdrivesGet"] = drive.patch(
        "teamdrives/{teamDriveId}",
        t.struct(
            {
                "teamDriveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "backgroundImageFile": t.struct(
                    {
                        "id": t.string().optional(),
                        "width": t.number().optional(),
                        "xCoordinate": t.number().optional(),
                        "yCoordinate": t.number().optional(),
                    }
                ).optional(),
                "backgroundImageLink": t.string().optional(),
                "capabilities": t.struct(
                    {
                        "canAddChildren": t.boolean().optional(),
                        "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                        "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                        "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                        "canChangeTeamDriveBackground": t.boolean().optional(),
                        "canChangeTeamMembersOnlyRestriction": t.boolean().optional(),
                        "canComment": t.boolean().optional(),
                        "canCopy": t.boolean().optional(),
                        "canDeleteChildren": t.boolean().optional(),
                        "canDeleteTeamDrive": t.boolean().optional(),
                        "canDownload": t.boolean().optional(),
                        "canEdit": t.boolean().optional(),
                        "canListChildren": t.boolean().optional(),
                        "canManageMembers": t.boolean().optional(),
                        "canReadRevisions": t.boolean().optional(),
                        "canRemoveChildren": t.boolean().optional(),
                        "canRename": t.boolean().optional(),
                        "canRenameTeamDrive": t.boolean().optional(),
                        "canResetTeamDriveRestrictions": t.boolean().optional(),
                        "canShare": t.boolean().optional(),
                        "canTrashChildren": t.boolean().optional(),
                    }
                ).optional(),
                "colorRgb": t.string().optional(),
                "createdTime": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "orgUnitId": t.string().optional(),
                "restrictions": t.struct(
                    {
                        "adminManagedRestrictions": t.boolean().optional(),
                        "copyRequiresWriterPermission": t.boolean().optional(),
                        "domainUsersOnly": t.boolean().optional(),
                        "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                        "teamMembersOnly": t.boolean().optional(),
                    }
                ).optional(),
                "themeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TeamDriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["teamdrivesList"] = drive.patch(
        "teamdrives/{teamDriveId}",
        t.struct(
            {
                "teamDriveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "backgroundImageFile": t.struct(
                    {
                        "id": t.string().optional(),
                        "width": t.number().optional(),
                        "xCoordinate": t.number().optional(),
                        "yCoordinate": t.number().optional(),
                    }
                ).optional(),
                "backgroundImageLink": t.string().optional(),
                "capabilities": t.struct(
                    {
                        "canAddChildren": t.boolean().optional(),
                        "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                        "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                        "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                        "canChangeTeamDriveBackground": t.boolean().optional(),
                        "canChangeTeamMembersOnlyRestriction": t.boolean().optional(),
                        "canComment": t.boolean().optional(),
                        "canCopy": t.boolean().optional(),
                        "canDeleteChildren": t.boolean().optional(),
                        "canDeleteTeamDrive": t.boolean().optional(),
                        "canDownload": t.boolean().optional(),
                        "canEdit": t.boolean().optional(),
                        "canListChildren": t.boolean().optional(),
                        "canManageMembers": t.boolean().optional(),
                        "canReadRevisions": t.boolean().optional(),
                        "canRemoveChildren": t.boolean().optional(),
                        "canRename": t.boolean().optional(),
                        "canRenameTeamDrive": t.boolean().optional(),
                        "canResetTeamDriveRestrictions": t.boolean().optional(),
                        "canShare": t.boolean().optional(),
                        "canTrashChildren": t.boolean().optional(),
                    }
                ).optional(),
                "colorRgb": t.string().optional(),
                "createdTime": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "orgUnitId": t.string().optional(),
                "restrictions": t.struct(
                    {
                        "adminManagedRestrictions": t.boolean().optional(),
                        "copyRequiresWriterPermission": t.boolean().optional(),
                        "domainUsersOnly": t.boolean().optional(),
                        "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                        "teamMembersOnly": t.boolean().optional(),
                    }
                ).optional(),
                "themeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TeamDriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["teamdrivesUpdate"] = drive.patch(
        "teamdrives/{teamDriveId}",
        t.struct(
            {
                "teamDriveId": t.string().optional(),
                "useDomainAdminAccess": t.boolean().optional(),
                "backgroundImageFile": t.struct(
                    {
                        "id": t.string().optional(),
                        "width": t.number().optional(),
                        "xCoordinate": t.number().optional(),
                        "yCoordinate": t.number().optional(),
                    }
                ).optional(),
                "backgroundImageLink": t.string().optional(),
                "capabilities": t.struct(
                    {
                        "canAddChildren": t.boolean().optional(),
                        "canChangeCopyRequiresWriterPermissionRestriction": t.boolean().optional(),
                        "canChangeDomainUsersOnlyRestriction": t.boolean().optional(),
                        "canChangeSharingFoldersRequiresOrganizerPermissionRestriction": t.boolean().optional(),
                        "canChangeTeamDriveBackground": t.boolean().optional(),
                        "canChangeTeamMembersOnlyRestriction": t.boolean().optional(),
                        "canComment": t.boolean().optional(),
                        "canCopy": t.boolean().optional(),
                        "canDeleteChildren": t.boolean().optional(),
                        "canDeleteTeamDrive": t.boolean().optional(),
                        "canDownload": t.boolean().optional(),
                        "canEdit": t.boolean().optional(),
                        "canListChildren": t.boolean().optional(),
                        "canManageMembers": t.boolean().optional(),
                        "canReadRevisions": t.boolean().optional(),
                        "canRemoveChildren": t.boolean().optional(),
                        "canRename": t.boolean().optional(),
                        "canRenameTeamDrive": t.boolean().optional(),
                        "canResetTeamDriveRestrictions": t.boolean().optional(),
                        "canShare": t.boolean().optional(),
                        "canTrashChildren": t.boolean().optional(),
                    }
                ).optional(),
                "colorRgb": t.string().optional(),
                "createdTime": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "orgUnitId": t.string().optional(),
                "restrictions": t.struct(
                    {
                        "adminManagedRestrictions": t.boolean().optional(),
                        "copyRequiresWriterPermission": t.boolean().optional(),
                        "domainUsersOnly": t.boolean().optional(),
                        "sharingFoldersRequiresOrganizerPermission": t.boolean().optional(),
                        "teamMembersOnly": t.boolean().optional(),
                    }
                ).optional(),
                "themeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TeamDriveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="drive", renames=renames, types=Box(types), functions=Box(functions)
    )
