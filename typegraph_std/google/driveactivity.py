from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_driveactivity() -> Import:
    driveactivity = HTTPRuntime("https://driveactivity.googleapis.com/")

    renames = {
        "ErrorResponse": "_driveactivity_1_ErrorResponse",
        "UploadIn": "_driveactivity_2_UploadIn",
        "UploadOut": "_driveactivity_3_UploadOut",
        "AdministratorIn": "_driveactivity_4_AdministratorIn",
        "AdministratorOut": "_driveactivity_5_AdministratorOut",
        "CommentIn": "_driveactivity_6_CommentIn",
        "CommentOut": "_driveactivity_7_CommentOut",
        "FileCommentIn": "_driveactivity_8_FileCommentIn",
        "FileCommentOut": "_driveactivity_9_FileCommentOut",
        "GroupIn": "_driveactivity_10_GroupIn",
        "GroupOut": "_driveactivity_11_GroupOut",
        "EditIn": "_driveactivity_12_EditIn",
        "EditOut": "_driveactivity_13_EditOut",
        "RestrictionChangeIn": "_driveactivity_14_RestrictionChangeIn",
        "RestrictionChangeOut": "_driveactivity_15_RestrictionChangeOut",
        "DeleteIn": "_driveactivity_16_DeleteIn",
        "DeleteOut": "_driveactivity_17_DeleteOut",
        "CopyIn": "_driveactivity_18_CopyIn",
        "CopyOut": "_driveactivity_19_CopyOut",
        "FolderIn": "_driveactivity_20_FolderIn",
        "FolderOut": "_driveactivity_21_FolderOut",
        "AssignmentIn": "_driveactivity_22_AssignmentIn",
        "AssignmentOut": "_driveactivity_23_AssignmentOut",
        "RenameIn": "_driveactivity_24_RenameIn",
        "RenameOut": "_driveactivity_25_RenameOut",
        "DriveItemIn": "_driveactivity_26_DriveItemIn",
        "DriveItemOut": "_driveactivity_27_DriveItemOut",
        "DomainIn": "_driveactivity_28_DomainIn",
        "DomainOut": "_driveactivity_29_DomainOut",
        "NewIn": "_driveactivity_30_NewIn",
        "NewOut": "_driveactivity_31_NewOut",
        "TextIn": "_driveactivity_32_TextIn",
        "TextOut": "_driveactivity_33_TextOut",
        "DriveReferenceIn": "_driveactivity_34_DriveReferenceIn",
        "DriveReferenceOut": "_driveactivity_35_DriveReferenceOut",
        "MoveIn": "_driveactivity_36_MoveIn",
        "MoveOut": "_driveactivity_37_MoveOut",
        "OwnerIn": "_driveactivity_38_OwnerIn",
        "OwnerOut": "_driveactivity_39_OwnerOut",
        "DeletedUserIn": "_driveactivity_40_DeletedUserIn",
        "DeletedUserOut": "_driveactivity_41_DeletedUserOut",
        "KnownUserIn": "_driveactivity_42_KnownUserIn",
        "KnownUserOut": "_driveactivity_43_KnownUserOut",
        "UnknownUserIn": "_driveactivity_44_UnknownUserIn",
        "UnknownUserOut": "_driveactivity_45_UnknownUserOut",
        "FieldValueChangeIn": "_driveactivity_46_FieldValueChangeIn",
        "FieldValueChangeOut": "_driveactivity_47_FieldValueChangeOut",
        "FileIn": "_driveactivity_48_FileIn",
        "FileOut": "_driveactivity_49_FileOut",
        "AnonymousUserIn": "_driveactivity_50_AnonymousUserIn",
        "AnonymousUserOut": "_driveactivity_51_AnonymousUserOut",
        "CreateIn": "_driveactivity_52_CreateIn",
        "CreateOut": "_driveactivity_53_CreateOut",
        "ApplicationReferenceIn": "_driveactivity_54_ApplicationReferenceIn",
        "ApplicationReferenceOut": "_driveactivity_55_ApplicationReferenceOut",
        "RestoreIn": "_driveactivity_56_RestoreIn",
        "RestoreOut": "_driveactivity_57_RestoreOut",
        "ConsolidationStrategyIn": "_driveactivity_58_ConsolidationStrategyIn",
        "ConsolidationStrategyOut": "_driveactivity_59_ConsolidationStrategyOut",
        "DriveItemReferenceIn": "_driveactivity_60_DriveItemReferenceIn",
        "DriveItemReferenceOut": "_driveactivity_61_DriveItemReferenceOut",
        "DriveActivityIn": "_driveactivity_62_DriveActivityIn",
        "DriveActivityOut": "_driveactivity_63_DriveActivityOut",
        "SettingsChangeIn": "_driveactivity_64_SettingsChangeIn",
        "SettingsChangeOut": "_driveactivity_65_SettingsChangeOut",
        "TargetIn": "_driveactivity_66_TargetIn",
        "TargetOut": "_driveactivity_67_TargetOut",
        "QueryDriveActivityResponseIn": "_driveactivity_68_QueryDriveActivityResponseIn",
        "QueryDriveActivityResponseOut": "_driveactivity_69_QueryDriveActivityResponseOut",
        "QueryDriveActivityRequestIn": "_driveactivity_70_QueryDriveActivityRequestIn",
        "QueryDriveActivityRequestOut": "_driveactivity_71_QueryDriveActivityRequestOut",
        "ActorIn": "_driveactivity_72_ActorIn",
        "ActorOut": "_driveactivity_73_ActorOut",
        "DriveFolderIn": "_driveactivity_74_DriveFolderIn",
        "DriveFolderOut": "_driveactivity_75_DriveFolderOut",
        "ActionIn": "_driveactivity_76_ActionIn",
        "ActionOut": "_driveactivity_77_ActionOut",
        "SelectionListIn": "_driveactivity_78_SelectionListIn",
        "SelectionListOut": "_driveactivity_79_SelectionListOut",
        "TeamDriveReferenceIn": "_driveactivity_80_TeamDriveReferenceIn",
        "TeamDriveReferenceOut": "_driveactivity_81_TeamDriveReferenceOut",
        "DataLeakPreventionChangeIn": "_driveactivity_82_DataLeakPreventionChangeIn",
        "DataLeakPreventionChangeOut": "_driveactivity_83_DataLeakPreventionChangeOut",
        "SuggestionIn": "_driveactivity_84_SuggestionIn",
        "SuggestionOut": "_driveactivity_85_SuggestionOut",
        "AppliedLabelChangeIn": "_driveactivity_86_AppliedLabelChangeIn",
        "AppliedLabelChangeOut": "_driveactivity_87_AppliedLabelChangeOut",
        "TimeRangeIn": "_driveactivity_88_TimeRangeIn",
        "TimeRangeOut": "_driveactivity_89_TimeRangeOut",
        "DateIn": "_driveactivity_90_DateIn",
        "DateOut": "_driveactivity_91_DateOut",
        "ImpersonationIn": "_driveactivity_92_ImpersonationIn",
        "ImpersonationOut": "_driveactivity_93_ImpersonationOut",
        "PostIn": "_driveactivity_94_PostIn",
        "PostOut": "_driveactivity_95_PostOut",
        "UserIn": "_driveactivity_96_UserIn",
        "UserOut": "_driveactivity_97_UserOut",
        "NoConsolidationIn": "_driveactivity_98_NoConsolidationIn",
        "NoConsolidationOut": "_driveactivity_99_NoConsolidationOut",
        "AnyoneIn": "_driveactivity_100_AnyoneIn",
        "AnyoneOut": "_driveactivity_101_AnyoneOut",
        "PermissionChangeIn": "_driveactivity_102_PermissionChangeIn",
        "PermissionChangeOut": "_driveactivity_103_PermissionChangeOut",
        "AppliedLabelChangeDetailIn": "_driveactivity_104_AppliedLabelChangeDetailIn",
        "AppliedLabelChangeDetailOut": "_driveactivity_105_AppliedLabelChangeDetailOut",
        "TeamDriveIn": "_driveactivity_106_TeamDriveIn",
        "TeamDriveOut": "_driveactivity_107_TeamDriveOut",
        "PermissionIn": "_driveactivity_108_PermissionIn",
        "PermissionOut": "_driveactivity_109_PermissionOut",
        "TextListIn": "_driveactivity_110_TextListIn",
        "TextListOut": "_driveactivity_111_TextListOut",
        "LegacyIn": "_driveactivity_112_LegacyIn",
        "LegacyOut": "_driveactivity_113_LegacyOut",
        "ActionDetailIn": "_driveactivity_114_ActionDetailIn",
        "ActionDetailOut": "_driveactivity_115_ActionDetailOut",
        "DriveFileIn": "_driveactivity_116_DriveFileIn",
        "DriveFileOut": "_driveactivity_117_DriveFileOut",
        "DriveIn": "_driveactivity_118_DriveIn",
        "DriveOut": "_driveactivity_119_DriveOut",
        "SystemEventIn": "_driveactivity_120_SystemEventIn",
        "SystemEventOut": "_driveactivity_121_SystemEventOut",
        "TargetReferenceIn": "_driveactivity_122_TargetReferenceIn",
        "TargetReferenceOut": "_driveactivity_123_TargetReferenceOut",
        "UserListIn": "_driveactivity_124_UserListIn",
        "UserListOut": "_driveactivity_125_UserListOut",
        "FieldValueIn": "_driveactivity_126_FieldValueIn",
        "FieldValueOut": "_driveactivity_127_FieldValueOut",
        "IntegerIn": "_driveactivity_128_IntegerIn",
        "IntegerOut": "_driveactivity_129_IntegerOut",
        "SelectionIn": "_driveactivity_130_SelectionIn",
        "SelectionOut": "_driveactivity_131_SelectionOut",
        "SingleUserIn": "_driveactivity_132_SingleUserIn",
        "SingleUserOut": "_driveactivity_133_SingleUserOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["UploadIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadIn"]
    )
    types["UploadOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadOut"])
    types["AdministratorIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdministratorIn"]
    )
    types["AdministratorOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdministratorOut"])
    types["CommentIn"] = t.struct(
        {
            "assignment": t.proxy(renames["AssignmentIn"]).optional(),
            "suggestion": t.proxy(renames["SuggestionIn"]).optional(),
            "mentionedUsers": t.array(t.proxy(renames["UserIn"])).optional(),
            "post": t.proxy(renames["PostIn"]).optional(),
        }
    ).named(renames["CommentIn"])
    types["CommentOut"] = t.struct(
        {
            "assignment": t.proxy(renames["AssignmentOut"]).optional(),
            "suggestion": t.proxy(renames["SuggestionOut"]).optional(),
            "mentionedUsers": t.array(t.proxy(renames["UserOut"])).optional(),
            "post": t.proxy(renames["PostOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentOut"])
    types["FileCommentIn"] = t.struct(
        {
            "legacyCommentId": t.string().optional(),
            "linkToDiscussion": t.string().optional(),
            "legacyDiscussionId": t.string().optional(),
            "parent": t.proxy(renames["DriveItemIn"]).optional(),
        }
    ).named(renames["FileCommentIn"])
    types["FileCommentOut"] = t.struct(
        {
            "legacyCommentId": t.string().optional(),
            "linkToDiscussion": t.string().optional(),
            "legacyDiscussionId": t.string().optional(),
            "parent": t.proxy(renames["DriveItemOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileCommentOut"])
    types["GroupIn"] = t.struct(
        {"title": t.string().optional(), "email": t.string().optional()}
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "title": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["EditIn"] = t.struct({"_": t.string().optional()}).named(renames["EditIn"])
    types["EditOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EditOut"])
    types["RestrictionChangeIn"] = t.struct(
        {"feature": t.string().optional(), "newRestriction": t.string().optional()}
    ).named(renames["RestrictionChangeIn"])
    types["RestrictionChangeOut"] = t.struct(
        {
            "feature": t.string().optional(),
            "newRestriction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestrictionChangeOut"])
    types["DeleteIn"] = t.struct({"type": t.string().optional()}).named(
        renames["DeleteIn"]
    )
    types["DeleteOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteOut"])
    types["CopyIn"] = t.struct(
        {"originalObject": t.proxy(renames["TargetReferenceIn"]).optional()}
    ).named(renames["CopyIn"])
    types["CopyOut"] = t.struct(
        {
            "originalObject": t.proxy(renames["TargetReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyOut"])
    types["FolderIn"] = t.struct({"type": t.string().optional()}).named(
        renames["FolderIn"]
    )
    types["FolderOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOut"])
    types["AssignmentIn"] = t.struct(
        {
            "subtype": t.string().optional(),
            "assignedUser": t.proxy(renames["UserIn"]).optional(),
        }
    ).named(renames["AssignmentIn"])
    types["AssignmentOut"] = t.struct(
        {
            "subtype": t.string().optional(),
            "assignedUser": t.proxy(renames["UserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignmentOut"])
    types["RenameIn"] = t.struct(
        {"oldTitle": t.string().optional(), "newTitle": t.string().optional()}
    ).named(renames["RenameIn"])
    types["RenameOut"] = t.struct(
        {
            "oldTitle": t.string().optional(),
            "newTitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RenameOut"])
    types["DriveItemIn"] = t.struct(
        {
            "folder": t.proxy(renames["FolderIn"]).optional(),
            "driveFolder": t.proxy(renames["DriveFolderIn"]).optional(),
            "owner": t.proxy(renames["OwnerIn"]).optional(),
            "mimeType": t.string().optional(),
            "file": t.proxy(renames["FileIn"]).optional(),
            "name": t.string().optional(),
            "driveFile": t.proxy(renames["DriveFileIn"]).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["DriveItemIn"])
    types["DriveItemOut"] = t.struct(
        {
            "folder": t.proxy(renames["FolderOut"]).optional(),
            "driveFolder": t.proxy(renames["DriveFolderOut"]).optional(),
            "owner": t.proxy(renames["OwnerOut"]).optional(),
            "mimeType": t.string().optional(),
            "file": t.proxy(renames["FileOut"]).optional(),
            "name": t.string().optional(),
            "driveFile": t.proxy(renames["DriveFileOut"]).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveItemOut"])
    types["DomainIn"] = t.struct(
        {"legacyId": t.string().optional(), "name": t.string().optional()}
    ).named(renames["DomainIn"])
    types["DomainOut"] = t.struct(
        {
            "legacyId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainOut"])
    types["NewIn"] = t.struct({"_": t.string().optional()}).named(renames["NewIn"])
    types["NewOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["NewOut"])
    types["TextIn"] = t.struct({"value": t.string().optional()}).named(
        renames["TextIn"]
    )
    types["TextOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextOut"])
    types["DriveReferenceIn"] = t.struct(
        {"name": t.string().optional(), "title": t.string().optional()}
    ).named(renames["DriveReferenceIn"])
    types["DriveReferenceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveReferenceOut"])
    types["MoveIn"] = t.struct(
        {
            "removedParents": t.array(t.proxy(renames["TargetReferenceIn"])).optional(),
            "addedParents": t.array(t.proxy(renames["TargetReferenceIn"])).optional(),
        }
    ).named(renames["MoveIn"])
    types["MoveOut"] = t.struct(
        {
            "removedParents": t.array(
                t.proxy(renames["TargetReferenceOut"])
            ).optional(),
            "addedParents": t.array(t.proxy(renames["TargetReferenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveOut"])
    types["OwnerIn"] = t.struct(
        {
            "domain": t.proxy(renames["DomainIn"]).optional(),
            "drive": t.proxy(renames["DriveReferenceIn"]).optional(),
            "teamDrive": t.proxy(renames["TeamDriveReferenceIn"]).optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
        }
    ).named(renames["OwnerIn"])
    types["OwnerOut"] = t.struct(
        {
            "domain": t.proxy(renames["DomainOut"]).optional(),
            "drive": t.proxy(renames["DriveReferenceOut"]).optional(),
            "teamDrive": t.proxy(renames["TeamDriveReferenceOut"]).optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OwnerOut"])
    types["DeletedUserIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeletedUserIn"]
    )
    types["DeletedUserOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeletedUserOut"])
    types["KnownUserIn"] = t.struct(
        {"isCurrentUser": t.boolean().optional(), "personName": t.string().optional()}
    ).named(renames["KnownUserIn"])
    types["KnownUserOut"] = t.struct(
        {
            "isCurrentUser": t.boolean().optional(),
            "personName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KnownUserOut"])
    types["UnknownUserIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UnknownUserIn"]
    )
    types["UnknownUserOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UnknownUserOut"])
    types["FieldValueChangeIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "fieldId": t.string().optional(),
            "oldValue": t.proxy(renames["FieldValueIn"]).optional(),
            "newValue": t.proxy(renames["FieldValueIn"]).optional(),
        }
    ).named(renames["FieldValueChangeIn"])
    types["FieldValueChangeOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "fieldId": t.string().optional(),
            "oldValue": t.proxy(renames["FieldValueOut"]).optional(),
            "newValue": t.proxy(renames["FieldValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldValueChangeOut"])
    types["FileIn"] = t.struct({"_": t.string().optional()}).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FileOut"])
    types["AnonymousUserIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AnonymousUserIn"]
    )
    types["AnonymousUserOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AnonymousUserOut"])
    types["CreateIn"] = t.struct(
        {
            "upload": t.proxy(renames["UploadIn"]).optional(),
            "copy": t.proxy(renames["CopyIn"]).optional(),
            "new": t.proxy(renames["NewIn"]).optional(),
        }
    ).named(renames["CreateIn"])
    types["CreateOut"] = t.struct(
        {
            "upload": t.proxy(renames["UploadOut"]).optional(),
            "copy": t.proxy(renames["CopyOut"]).optional(),
            "new": t.proxy(renames["NewOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateOut"])
    types["ApplicationReferenceIn"] = t.struct({"type": t.string().optional()}).named(
        renames["ApplicationReferenceIn"]
    )
    types["ApplicationReferenceOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationReferenceOut"])
    types["RestoreIn"] = t.struct({"type": t.string().optional()}).named(
        renames["RestoreIn"]
    )
    types["RestoreOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreOut"])
    types["ConsolidationStrategyIn"] = t.struct(
        {
            "legacy": t.proxy(renames["LegacyIn"]).optional(),
            "none": t.proxy(renames["NoConsolidationIn"]).optional(),
        }
    ).named(renames["ConsolidationStrategyIn"])
    types["ConsolidationStrategyOut"] = t.struct(
        {
            "legacy": t.proxy(renames["LegacyOut"]).optional(),
            "none": t.proxy(renames["NoConsolidationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsolidationStrategyOut"])
    types["DriveItemReferenceIn"] = t.struct(
        {
            "driveFolder": t.proxy(renames["DriveFolderIn"]).optional(),
            "name": t.string().optional(),
            "driveFile": t.proxy(renames["DriveFileIn"]).optional(),
            "title": t.string().optional(),
            "folder": t.proxy(renames["FolderIn"]).optional(),
            "file": t.proxy(renames["FileIn"]).optional(),
        }
    ).named(renames["DriveItemReferenceIn"])
    types["DriveItemReferenceOut"] = t.struct(
        {
            "driveFolder": t.proxy(renames["DriveFolderOut"]).optional(),
            "name": t.string().optional(),
            "driveFile": t.proxy(renames["DriveFileOut"]).optional(),
            "title": t.string().optional(),
            "folder": t.proxy(renames["FolderOut"]).optional(),
            "file": t.proxy(renames["FileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveItemReferenceOut"])
    types["DriveActivityIn"] = t.struct(
        {
            "targets": t.array(t.proxy(renames["TargetIn"])).optional(),
            "timeRange": t.proxy(renames["TimeRangeIn"]).optional(),
            "primaryActionDetail": t.proxy(renames["ActionDetailIn"]).optional(),
            "actions": t.array(t.proxy(renames["ActionIn"])).optional(),
            "timestamp": t.string().optional(),
            "actors": t.array(t.proxy(renames["ActorIn"])).optional(),
        }
    ).named(renames["DriveActivityIn"])
    types["DriveActivityOut"] = t.struct(
        {
            "targets": t.array(t.proxy(renames["TargetOut"])).optional(),
            "timeRange": t.proxy(renames["TimeRangeOut"]).optional(),
            "primaryActionDetail": t.proxy(renames["ActionDetailOut"]).optional(),
            "actions": t.array(t.proxy(renames["ActionOut"])).optional(),
            "timestamp": t.string().optional(),
            "actors": t.array(t.proxy(renames["ActorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveActivityOut"])
    types["SettingsChangeIn"] = t.struct(
        {
            "restrictionChanges": t.array(
                t.proxy(renames["RestrictionChangeIn"])
            ).optional()
        }
    ).named(renames["SettingsChangeIn"])
    types["SettingsChangeOut"] = t.struct(
        {
            "restrictionChanges": t.array(
                t.proxy(renames["RestrictionChangeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsChangeOut"])
    types["TargetIn"] = t.struct(
        {
            "driveItem": t.proxy(renames["DriveItemIn"]).optional(),
            "teamDrive": t.proxy(renames["TeamDriveIn"]).optional(),
            "drive": t.proxy(renames["DriveIn"]).optional(),
            "fileComment": t.proxy(renames["FileCommentIn"]).optional(),
        }
    ).named(renames["TargetIn"])
    types["TargetOut"] = t.struct(
        {
            "driveItem": t.proxy(renames["DriveItemOut"]).optional(),
            "teamDrive": t.proxy(renames["TeamDriveOut"]).optional(),
            "drive": t.proxy(renames["DriveOut"]).optional(),
            "fileComment": t.proxy(renames["FileCommentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetOut"])
    types["QueryDriveActivityResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "activities": t.array(t.proxy(renames["DriveActivityIn"])).optional(),
        }
    ).named(renames["QueryDriveActivityResponseIn"])
    types["QueryDriveActivityResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "activities": t.array(t.proxy(renames["DriveActivityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryDriveActivityResponseOut"])
    types["QueryDriveActivityRequestIn"] = t.struct(
        {
            "consolidationStrategy": t.proxy(
                renames["ConsolidationStrategyIn"]
            ).optional(),
            "itemName": t.string().optional(),
            "pageToken": t.string().optional(),
            "filter": t.string().optional(),
            "pageSize": t.integer().optional(),
            "ancestorName": t.string().optional(),
        }
    ).named(renames["QueryDriveActivityRequestIn"])
    types["QueryDriveActivityRequestOut"] = t.struct(
        {
            "consolidationStrategy": t.proxy(
                renames["ConsolidationStrategyOut"]
            ).optional(),
            "itemName": t.string().optional(),
            "pageToken": t.string().optional(),
            "filter": t.string().optional(),
            "pageSize": t.integer().optional(),
            "ancestorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryDriveActivityRequestOut"])
    types["ActorIn"] = t.struct(
        {
            "user": t.proxy(renames["UserIn"]).optional(),
            "impersonation": t.proxy(renames["ImpersonationIn"]).optional(),
            "anonymous": t.proxy(renames["AnonymousUserIn"]).optional(),
            "system": t.proxy(renames["SystemEventIn"]).optional(),
            "administrator": t.proxy(renames["AdministratorIn"]).optional(),
        }
    ).named(renames["ActorIn"])
    types["ActorOut"] = t.struct(
        {
            "user": t.proxy(renames["UserOut"]).optional(),
            "impersonation": t.proxy(renames["ImpersonationOut"]).optional(),
            "anonymous": t.proxy(renames["AnonymousUserOut"]).optional(),
            "system": t.proxy(renames["SystemEventOut"]).optional(),
            "administrator": t.proxy(renames["AdministratorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActorOut"])
    types["DriveFolderIn"] = t.struct({"type": t.string().optional()}).named(
        renames["DriveFolderIn"]
    )
    types["DriveFolderOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveFolderOut"])
    types["ActionIn"] = t.struct(
        {
            "target": t.proxy(renames["TargetIn"]).optional(),
            "actor": t.proxy(renames["ActorIn"]).optional(),
            "timeRange": t.proxy(renames["TimeRangeIn"]).optional(),
            "timestamp": t.string().optional(),
            "detail": t.proxy(renames["ActionDetailIn"]).optional(),
        }
    ).named(renames["ActionIn"])
    types["ActionOut"] = t.struct(
        {
            "target": t.proxy(renames["TargetOut"]).optional(),
            "actor": t.proxy(renames["ActorOut"]).optional(),
            "timeRange": t.proxy(renames["TimeRangeOut"]).optional(),
            "timestamp": t.string().optional(),
            "detail": t.proxy(renames["ActionDetailOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionOut"])
    types["SelectionListIn"] = t.struct(
        {"values": t.array(t.proxy(renames["SelectionIn"])).optional()}
    ).named(renames["SelectionListIn"])
    types["SelectionListOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["SelectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SelectionListOut"])
    types["TeamDriveReferenceIn"] = t.struct(
        {"name": t.string().optional(), "title": t.string().optional()}
    ).named(renames["TeamDriveReferenceIn"])
    types["TeamDriveReferenceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TeamDriveReferenceOut"])
    types["DataLeakPreventionChangeIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["DataLeakPreventionChangeIn"])
    types["DataLeakPreventionChangeOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataLeakPreventionChangeOut"])
    types["SuggestionIn"] = t.struct({"subtype": t.string().optional()}).named(
        renames["SuggestionIn"]
    )
    types["SuggestionOut"] = t.struct(
        {
            "subtype": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestionOut"])
    types["AppliedLabelChangeIn"] = t.struct(
        {"changes": t.array(t.proxy(renames["AppliedLabelChangeDetailIn"])).optional()}
    ).named(renames["AppliedLabelChangeIn"])
    types["AppliedLabelChangeOut"] = t.struct(
        {
            "changes": t.array(
                t.proxy(renames["AppliedLabelChangeDetailOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppliedLabelChangeOut"])
    types["TimeRangeIn"] = t.struct(
        {"endTime": t.string().optional(), "startTime": t.string().optional()}
    ).named(renames["TimeRangeIn"])
    types["TimeRangeOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeRangeOut"])
    types["DateIn"] = t.struct({"value": t.string().optional()}).named(
        renames["DateIn"]
    )
    types["DateOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["ImpersonationIn"] = t.struct(
        {"impersonatedUser": t.proxy(renames["UserIn"]).optional()}
    ).named(renames["ImpersonationIn"])
    types["ImpersonationOut"] = t.struct(
        {
            "impersonatedUser": t.proxy(renames["UserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImpersonationOut"])
    types["PostIn"] = t.struct({"subtype": t.string().optional()}).named(
        renames["PostIn"]
    )
    types["PostOut"] = t.struct(
        {
            "subtype": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostOut"])
    types["UserIn"] = t.struct(
        {
            "unknownUser": t.proxy(renames["UnknownUserIn"]).optional(),
            "deletedUser": t.proxy(renames["DeletedUserIn"]).optional(),
            "knownUser": t.proxy(renames["KnownUserIn"]).optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "unknownUser": t.proxy(renames["UnknownUserOut"]).optional(),
            "deletedUser": t.proxy(renames["DeletedUserOut"]).optional(),
            "knownUser": t.proxy(renames["KnownUserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["NoConsolidationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["NoConsolidationIn"]
    )
    types["NoConsolidationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["NoConsolidationOut"])
    types["AnyoneIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AnyoneIn"]
    )
    types["AnyoneOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AnyoneOut"])
    types["PermissionChangeIn"] = t.struct(
        {
            "addedPermissions": t.array(t.proxy(renames["PermissionIn"])).optional(),
            "removedPermissions": t.array(t.proxy(renames["PermissionIn"])).optional(),
        }
    ).named(renames["PermissionChangeIn"])
    types["PermissionChangeOut"] = t.struct(
        {
            "addedPermissions": t.array(t.proxy(renames["PermissionOut"])).optional(),
            "removedPermissions": t.array(t.proxy(renames["PermissionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionChangeOut"])
    types["AppliedLabelChangeDetailIn"] = t.struct(
        {
            "fieldChanges": t.array(t.proxy(renames["FieldValueChangeIn"])).optional(),
            "label": t.string().optional(),
            "types": t.array(t.string()).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["AppliedLabelChangeDetailIn"])
    types["AppliedLabelChangeDetailOut"] = t.struct(
        {
            "fieldChanges": t.array(t.proxy(renames["FieldValueChangeOut"])).optional(),
            "label": t.string().optional(),
            "types": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppliedLabelChangeDetailOut"])
    types["TeamDriveIn"] = t.struct(
        {
            "name": t.string().optional(),
            "title": t.string().optional(),
            "root": t.proxy(renames["DriveItemIn"]).optional(),
        }
    ).named(renames["TeamDriveIn"])
    types["TeamDriveOut"] = t.struct(
        {
            "name": t.string().optional(),
            "title": t.string().optional(),
            "root": t.proxy(renames["DriveItemOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TeamDriveOut"])
    types["PermissionIn"] = t.struct(
        {
            "role": t.string().optional(),
            "anyone": t.proxy(renames["AnyoneIn"]).optional(),
            "domain": t.proxy(renames["DomainIn"]).optional(),
            "allowDiscovery": t.boolean().optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "group": t.proxy(renames["GroupIn"]).optional(),
        }
    ).named(renames["PermissionIn"])
    types["PermissionOut"] = t.struct(
        {
            "role": t.string().optional(),
            "anyone": t.proxy(renames["AnyoneOut"]).optional(),
            "domain": t.proxy(renames["DomainOut"]).optional(),
            "allowDiscovery": t.boolean().optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "group": t.proxy(renames["GroupOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionOut"])
    types["TextListIn"] = t.struct(
        {"values": t.array(t.proxy(renames["TextIn"])).optional()}
    ).named(renames["TextListIn"])
    types["TextListOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["TextOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextListOut"])
    types["LegacyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LegacyIn"]
    )
    types["LegacyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LegacyOut"])
    types["ActionDetailIn"] = t.struct(
        {
            "rename": t.proxy(renames["RenameIn"]).optional(),
            "restore": t.proxy(renames["RestoreIn"]).optional(),
            "move": t.proxy(renames["MoveIn"]).optional(),
            "appliedLabelChange": t.proxy(renames["AppliedLabelChangeIn"]).optional(),
            "permissionChange": t.proxy(renames["PermissionChangeIn"]).optional(),
            "reference": t.proxy(renames["ApplicationReferenceIn"]).optional(),
            "create": t.proxy(renames["CreateIn"]).optional(),
            "comment": t.proxy(renames["CommentIn"]).optional(),
            "delete": t.proxy(renames["DeleteIn"]).optional(),
            "settingsChange": t.proxy(renames["SettingsChangeIn"]).optional(),
            "dlpChange": t.proxy(renames["DataLeakPreventionChangeIn"]).optional(),
            "edit": t.proxy(renames["EditIn"]).optional(),
        }
    ).named(renames["ActionDetailIn"])
    types["ActionDetailOut"] = t.struct(
        {
            "rename": t.proxy(renames["RenameOut"]).optional(),
            "restore": t.proxy(renames["RestoreOut"]).optional(),
            "move": t.proxy(renames["MoveOut"]).optional(),
            "appliedLabelChange": t.proxy(renames["AppliedLabelChangeOut"]).optional(),
            "permissionChange": t.proxy(renames["PermissionChangeOut"]).optional(),
            "reference": t.proxy(renames["ApplicationReferenceOut"]).optional(),
            "create": t.proxy(renames["CreateOut"]).optional(),
            "comment": t.proxy(renames["CommentOut"]).optional(),
            "delete": t.proxy(renames["DeleteOut"]).optional(),
            "settingsChange": t.proxy(renames["SettingsChangeOut"]).optional(),
            "dlpChange": t.proxy(renames["DataLeakPreventionChangeOut"]).optional(),
            "edit": t.proxy(renames["EditOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionDetailOut"])
    types["DriveFileIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DriveFileIn"]
    )
    types["DriveFileOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveFileOut"])
    types["DriveIn"] = t.struct(
        {
            "root": t.proxy(renames["DriveItemIn"]).optional(),
            "title": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DriveIn"])
    types["DriveOut"] = t.struct(
        {
            "root": t.proxy(renames["DriveItemOut"]).optional(),
            "title": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveOut"])
    types["SystemEventIn"] = t.struct({"type": t.string().optional()}).named(
        renames["SystemEventIn"]
    )
    types["SystemEventOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemEventOut"])
    types["TargetReferenceIn"] = t.struct(
        {
            "drive": t.proxy(renames["DriveReferenceIn"]).optional(),
            "driveItem": t.proxy(renames["DriveItemReferenceIn"]).optional(),
            "teamDrive": t.proxy(renames["TeamDriveReferenceIn"]).optional(),
        }
    ).named(renames["TargetReferenceIn"])
    types["TargetReferenceOut"] = t.struct(
        {
            "drive": t.proxy(renames["DriveReferenceOut"]).optional(),
            "driveItem": t.proxy(renames["DriveItemReferenceOut"]).optional(),
            "teamDrive": t.proxy(renames["TeamDriveReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetReferenceOut"])
    types["UserListIn"] = t.struct(
        {"values": t.array(t.proxy(renames["SingleUserIn"])).optional()}
    ).named(renames["UserListIn"])
    types["UserListOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["SingleUserOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserListOut"])
    types["FieldValueIn"] = t.struct(
        {
            "userList": t.proxy(renames["UserListIn"]).optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "user": t.proxy(renames["SingleUserIn"]).optional(),
            "integer": t.proxy(renames["IntegerIn"]).optional(),
            "selection": t.proxy(renames["SelectionIn"]).optional(),
            "textList": t.proxy(renames["TextListIn"]).optional(),
            "selectionList": t.proxy(renames["SelectionListIn"]).optional(),
            "text": t.proxy(renames["TextIn"]).optional(),
        }
    ).named(renames["FieldValueIn"])
    types["FieldValueOut"] = t.struct(
        {
            "userList": t.proxy(renames["UserListOut"]).optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "user": t.proxy(renames["SingleUserOut"]).optional(),
            "integer": t.proxy(renames["IntegerOut"]).optional(),
            "selection": t.proxy(renames["SelectionOut"]).optional(),
            "textList": t.proxy(renames["TextListOut"]).optional(),
            "selectionList": t.proxy(renames["SelectionListOut"]).optional(),
            "text": t.proxy(renames["TextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldValueOut"])
    types["IntegerIn"] = t.struct({"value": t.string().optional()}).named(
        renames["IntegerIn"]
    )
    types["IntegerOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerOut"])
    types["SelectionIn"] = t.struct(
        {"value": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["SelectionIn"])
    types["SelectionOut"] = t.struct(
        {
            "value": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SelectionOut"])
    types["SingleUserIn"] = t.struct({"value": t.string().optional()}).named(
        renames["SingleUserIn"]
    )
    types["SingleUserOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SingleUserOut"])

    functions = {}
    functions["activityQuery"] = driveactivity.post(
        "v2/activity:query",
        t.struct(
            {
                "consolidationStrategy": t.proxy(
                    renames["ConsolidationStrategyIn"]
                ).optional(),
                "itemName": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "ancestorName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryDriveActivityResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="driveactivity",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
