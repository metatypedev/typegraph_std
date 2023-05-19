from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_driveactivity() -> Import:
    driveactivity = HTTPRuntime("https://driveactivity.googleapis.com/")

    renames = {
        "ErrorResponse": "_driveactivity_1_ErrorResponse",
        "SystemEventIn": "_driveactivity_2_SystemEventIn",
        "SystemEventOut": "_driveactivity_3_SystemEventOut",
        "KnownUserIn": "_driveactivity_4_KnownUserIn",
        "KnownUserOut": "_driveactivity_5_KnownUserOut",
        "RestrictionChangeIn": "_driveactivity_6_RestrictionChangeIn",
        "RestrictionChangeOut": "_driveactivity_7_RestrictionChangeOut",
        "AnonymousUserIn": "_driveactivity_8_AnonymousUserIn",
        "AnonymousUserOut": "_driveactivity_9_AnonymousUserOut",
        "NewIn": "_driveactivity_10_NewIn",
        "NewOut": "_driveactivity_11_NewOut",
        "UserIn": "_driveactivity_12_UserIn",
        "UserOut": "_driveactivity_13_UserOut",
        "UnknownUserIn": "_driveactivity_14_UnknownUserIn",
        "UnknownUserOut": "_driveactivity_15_UnknownUserOut",
        "ActionDetailIn": "_driveactivity_16_ActionDetailIn",
        "ActionDetailOut": "_driveactivity_17_ActionDetailOut",
        "DeletedUserIn": "_driveactivity_18_DeletedUserIn",
        "DeletedUserOut": "_driveactivity_19_DeletedUserOut",
        "AssignmentIn": "_driveactivity_20_AssignmentIn",
        "AssignmentOut": "_driveactivity_21_AssignmentOut",
        "TeamDriveIn": "_driveactivity_22_TeamDriveIn",
        "TeamDriveOut": "_driveactivity_23_TeamDriveOut",
        "FieldValueChangeIn": "_driveactivity_24_FieldValueChangeIn",
        "FieldValueChangeOut": "_driveactivity_25_FieldValueChangeOut",
        "CopyIn": "_driveactivity_26_CopyIn",
        "CopyOut": "_driveactivity_27_CopyOut",
        "AdministratorIn": "_driveactivity_28_AdministratorIn",
        "AdministratorOut": "_driveactivity_29_AdministratorOut",
        "DateIn": "_driveactivity_30_DateIn",
        "DateOut": "_driveactivity_31_DateOut",
        "FileCommentIn": "_driveactivity_32_FileCommentIn",
        "FileCommentOut": "_driveactivity_33_FileCommentOut",
        "DriveReferenceIn": "_driveactivity_34_DriveReferenceIn",
        "DriveReferenceOut": "_driveactivity_35_DriveReferenceOut",
        "SelectionListIn": "_driveactivity_36_SelectionListIn",
        "SelectionListOut": "_driveactivity_37_SelectionListOut",
        "FieldValueIn": "_driveactivity_38_FieldValueIn",
        "FieldValueOut": "_driveactivity_39_FieldValueOut",
        "ConsolidationStrategyIn": "_driveactivity_40_ConsolidationStrategyIn",
        "ConsolidationStrategyOut": "_driveactivity_41_ConsolidationStrategyOut",
        "IntegerIn": "_driveactivity_42_IntegerIn",
        "IntegerOut": "_driveactivity_43_IntegerOut",
        "ImpersonationIn": "_driveactivity_44_ImpersonationIn",
        "ImpersonationOut": "_driveactivity_45_ImpersonationOut",
        "FolderIn": "_driveactivity_46_FolderIn",
        "FolderOut": "_driveactivity_47_FolderOut",
        "RestoreIn": "_driveactivity_48_RestoreIn",
        "RestoreOut": "_driveactivity_49_RestoreOut",
        "DriveItemIn": "_driveactivity_50_DriveItemIn",
        "DriveItemOut": "_driveactivity_51_DriveItemOut",
        "QueryDriveActivityRequestIn": "_driveactivity_52_QueryDriveActivityRequestIn",
        "QueryDriveActivityRequestOut": "_driveactivity_53_QueryDriveActivityRequestOut",
        "PermissionChangeIn": "_driveactivity_54_PermissionChangeIn",
        "PermissionChangeOut": "_driveactivity_55_PermissionChangeOut",
        "AppliedLabelChangeDetailIn": "_driveactivity_56_AppliedLabelChangeDetailIn",
        "AppliedLabelChangeDetailOut": "_driveactivity_57_AppliedLabelChangeDetailOut",
        "DriveItemReferenceIn": "_driveactivity_58_DriveItemReferenceIn",
        "DriveItemReferenceOut": "_driveactivity_59_DriveItemReferenceOut",
        "SingleUserIn": "_driveactivity_60_SingleUserIn",
        "SingleUserOut": "_driveactivity_61_SingleUserOut",
        "GroupIn": "_driveactivity_62_GroupIn",
        "GroupOut": "_driveactivity_63_GroupOut",
        "QueryDriveActivityResponseIn": "_driveactivity_64_QueryDriveActivityResponseIn",
        "QueryDriveActivityResponseOut": "_driveactivity_65_QueryDriveActivityResponseOut",
        "TeamDriveReferenceIn": "_driveactivity_66_TeamDriveReferenceIn",
        "TeamDriveReferenceOut": "_driveactivity_67_TeamDriveReferenceOut",
        "ActionIn": "_driveactivity_68_ActionIn",
        "ActionOut": "_driveactivity_69_ActionOut",
        "FileIn": "_driveactivity_70_FileIn",
        "FileOut": "_driveactivity_71_FileOut",
        "TargetIn": "_driveactivity_72_TargetIn",
        "TargetOut": "_driveactivity_73_TargetOut",
        "SettingsChangeIn": "_driveactivity_74_SettingsChangeIn",
        "SettingsChangeOut": "_driveactivity_75_SettingsChangeOut",
        "TextIn": "_driveactivity_76_TextIn",
        "TextOut": "_driveactivity_77_TextOut",
        "TimeRangeIn": "_driveactivity_78_TimeRangeIn",
        "TimeRangeOut": "_driveactivity_79_TimeRangeOut",
        "AnyoneIn": "_driveactivity_80_AnyoneIn",
        "AnyoneOut": "_driveactivity_81_AnyoneOut",
        "UserListIn": "_driveactivity_82_UserListIn",
        "UserListOut": "_driveactivity_83_UserListOut",
        "PostIn": "_driveactivity_84_PostIn",
        "PostOut": "_driveactivity_85_PostOut",
        "UploadIn": "_driveactivity_86_UploadIn",
        "UploadOut": "_driveactivity_87_UploadOut",
        "EditIn": "_driveactivity_88_EditIn",
        "EditOut": "_driveactivity_89_EditOut",
        "DriveIn": "_driveactivity_90_DriveIn",
        "DriveOut": "_driveactivity_91_DriveOut",
        "MoveIn": "_driveactivity_92_MoveIn",
        "MoveOut": "_driveactivity_93_MoveOut",
        "ApplicationReferenceIn": "_driveactivity_94_ApplicationReferenceIn",
        "ApplicationReferenceOut": "_driveactivity_95_ApplicationReferenceOut",
        "RenameIn": "_driveactivity_96_RenameIn",
        "RenameOut": "_driveactivity_97_RenameOut",
        "SelectionIn": "_driveactivity_98_SelectionIn",
        "SelectionOut": "_driveactivity_99_SelectionOut",
        "DriveFileIn": "_driveactivity_100_DriveFileIn",
        "DriveFileOut": "_driveactivity_101_DriveFileOut",
        "SuggestionIn": "_driveactivity_102_SuggestionIn",
        "SuggestionOut": "_driveactivity_103_SuggestionOut",
        "DeleteIn": "_driveactivity_104_DeleteIn",
        "DeleteOut": "_driveactivity_105_DeleteOut",
        "OwnerIn": "_driveactivity_106_OwnerIn",
        "OwnerOut": "_driveactivity_107_OwnerOut",
        "CreateIn": "_driveactivity_108_CreateIn",
        "CreateOut": "_driveactivity_109_CreateOut",
        "DomainIn": "_driveactivity_110_DomainIn",
        "DomainOut": "_driveactivity_111_DomainOut",
        "TextListIn": "_driveactivity_112_TextListIn",
        "TextListOut": "_driveactivity_113_TextListOut",
        "PermissionIn": "_driveactivity_114_PermissionIn",
        "PermissionOut": "_driveactivity_115_PermissionOut",
        "ActorIn": "_driveactivity_116_ActorIn",
        "ActorOut": "_driveactivity_117_ActorOut",
        "NoConsolidationIn": "_driveactivity_118_NoConsolidationIn",
        "NoConsolidationOut": "_driveactivity_119_NoConsolidationOut",
        "DataLeakPreventionChangeIn": "_driveactivity_120_DataLeakPreventionChangeIn",
        "DataLeakPreventionChangeOut": "_driveactivity_121_DataLeakPreventionChangeOut",
        "DriveFolderIn": "_driveactivity_122_DriveFolderIn",
        "DriveFolderOut": "_driveactivity_123_DriveFolderOut",
        "LegacyIn": "_driveactivity_124_LegacyIn",
        "LegacyOut": "_driveactivity_125_LegacyOut",
        "DriveActivityIn": "_driveactivity_126_DriveActivityIn",
        "DriveActivityOut": "_driveactivity_127_DriveActivityOut",
        "CommentIn": "_driveactivity_128_CommentIn",
        "CommentOut": "_driveactivity_129_CommentOut",
        "AppliedLabelChangeIn": "_driveactivity_130_AppliedLabelChangeIn",
        "AppliedLabelChangeOut": "_driveactivity_131_AppliedLabelChangeOut",
        "TargetReferenceIn": "_driveactivity_132_TargetReferenceIn",
        "TargetReferenceOut": "_driveactivity_133_TargetReferenceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SystemEventIn"] = t.struct({"type": t.string().optional()}).named(
        renames["SystemEventIn"]
    )
    types["SystemEventOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemEventOut"])
    types["KnownUserIn"] = t.struct(
        {"personName": t.string().optional(), "isCurrentUser": t.boolean().optional()}
    ).named(renames["KnownUserIn"])
    types["KnownUserOut"] = t.struct(
        {
            "personName": t.string().optional(),
            "isCurrentUser": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KnownUserOut"])
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
    types["AnonymousUserIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AnonymousUserIn"]
    )
    types["AnonymousUserOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AnonymousUserOut"])
    types["NewIn"] = t.struct({"_": t.string().optional()}).named(renames["NewIn"])
    types["NewOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["NewOut"])
    types["UserIn"] = t.struct(
        {
            "knownUser": t.proxy(renames["KnownUserIn"]).optional(),
            "unknownUser": t.proxy(renames["UnknownUserIn"]).optional(),
            "deletedUser": t.proxy(renames["DeletedUserIn"]).optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "knownUser": t.proxy(renames["KnownUserOut"]).optional(),
            "unknownUser": t.proxy(renames["UnknownUserOut"]).optional(),
            "deletedUser": t.proxy(renames["DeletedUserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["UnknownUserIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UnknownUserIn"]
    )
    types["UnknownUserOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UnknownUserOut"])
    types["ActionDetailIn"] = t.struct(
        {
            "appliedLabelChange": t.proxy(renames["AppliedLabelChangeIn"]).optional(),
            "permissionChange": t.proxy(renames["PermissionChangeIn"]).optional(),
            "reference": t.proxy(renames["ApplicationReferenceIn"]).optional(),
            "rename": t.proxy(renames["RenameIn"]).optional(),
            "move": t.proxy(renames["MoveIn"]).optional(),
            "create": t.proxy(renames["CreateIn"]).optional(),
            "delete": t.proxy(renames["DeleteIn"]).optional(),
            "dlpChange": t.proxy(renames["DataLeakPreventionChangeIn"]).optional(),
            "restore": t.proxy(renames["RestoreIn"]).optional(),
            "edit": t.proxy(renames["EditIn"]).optional(),
            "settingsChange": t.proxy(renames["SettingsChangeIn"]).optional(),
            "comment": t.proxy(renames["CommentIn"]).optional(),
        }
    ).named(renames["ActionDetailIn"])
    types["ActionDetailOut"] = t.struct(
        {
            "appliedLabelChange": t.proxy(renames["AppliedLabelChangeOut"]).optional(),
            "permissionChange": t.proxy(renames["PermissionChangeOut"]).optional(),
            "reference": t.proxy(renames["ApplicationReferenceOut"]).optional(),
            "rename": t.proxy(renames["RenameOut"]).optional(),
            "move": t.proxy(renames["MoveOut"]).optional(),
            "create": t.proxy(renames["CreateOut"]).optional(),
            "delete": t.proxy(renames["DeleteOut"]).optional(),
            "dlpChange": t.proxy(renames["DataLeakPreventionChangeOut"]).optional(),
            "restore": t.proxy(renames["RestoreOut"]).optional(),
            "edit": t.proxy(renames["EditOut"]).optional(),
            "settingsChange": t.proxy(renames["SettingsChangeOut"]).optional(),
            "comment": t.proxy(renames["CommentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionDetailOut"])
    types["DeletedUserIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeletedUserIn"]
    )
    types["DeletedUserOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeletedUserOut"])
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
    types["TeamDriveIn"] = t.struct(
        {
            "root": t.proxy(renames["DriveItemIn"]).optional(),
            "title": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TeamDriveIn"])
    types["TeamDriveOut"] = t.struct(
        {
            "root": t.proxy(renames["DriveItemOut"]).optional(),
            "title": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TeamDriveOut"])
    types["FieldValueChangeIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "oldValue": t.proxy(renames["FieldValueIn"]).optional(),
            "fieldId": t.string().optional(),
            "newValue": t.proxy(renames["FieldValueIn"]).optional(),
        }
    ).named(renames["FieldValueChangeIn"])
    types["FieldValueChangeOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "oldValue": t.proxy(renames["FieldValueOut"]).optional(),
            "fieldId": t.string().optional(),
            "newValue": t.proxy(renames["FieldValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldValueChangeOut"])
    types["CopyIn"] = t.struct(
        {"originalObject": t.proxy(renames["TargetReferenceIn"]).optional()}
    ).named(renames["CopyIn"])
    types["CopyOut"] = t.struct(
        {
            "originalObject": t.proxy(renames["TargetReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyOut"])
    types["AdministratorIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdministratorIn"]
    )
    types["AdministratorOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdministratorOut"])
    types["DateIn"] = t.struct({"value": t.string().optional()}).named(
        renames["DateIn"]
    )
    types["DateOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["FileCommentIn"] = t.struct(
        {
            "legacyDiscussionId": t.string().optional(),
            "parent": t.proxy(renames["DriveItemIn"]).optional(),
            "linkToDiscussion": t.string().optional(),
            "legacyCommentId": t.string().optional(),
        }
    ).named(renames["FileCommentIn"])
    types["FileCommentOut"] = t.struct(
        {
            "legacyDiscussionId": t.string().optional(),
            "parent": t.proxy(renames["DriveItemOut"]).optional(),
            "linkToDiscussion": t.string().optional(),
            "legacyCommentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileCommentOut"])
    types["DriveReferenceIn"] = t.struct(
        {"title": t.string().optional(), "name": t.string().optional()}
    ).named(renames["DriveReferenceIn"])
    types["DriveReferenceOut"] = t.struct(
        {
            "title": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveReferenceOut"])
    types["SelectionListIn"] = t.struct(
        {"values": t.array(t.proxy(renames["SelectionIn"])).optional()}
    ).named(renames["SelectionListIn"])
    types["SelectionListOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["SelectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SelectionListOut"])
    types["FieldValueIn"] = t.struct(
        {
            "userList": t.proxy(renames["UserListIn"]).optional(),
            "text": t.proxy(renames["TextIn"]).optional(),
            "selection": t.proxy(renames["SelectionIn"]).optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "integer": t.proxy(renames["IntegerIn"]).optional(),
            "selectionList": t.proxy(renames["SelectionListIn"]).optional(),
            "user": t.proxy(renames["SingleUserIn"]).optional(),
            "textList": t.proxy(renames["TextListIn"]).optional(),
        }
    ).named(renames["FieldValueIn"])
    types["FieldValueOut"] = t.struct(
        {
            "userList": t.proxy(renames["UserListOut"]).optional(),
            "text": t.proxy(renames["TextOut"]).optional(),
            "selection": t.proxy(renames["SelectionOut"]).optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "integer": t.proxy(renames["IntegerOut"]).optional(),
            "selectionList": t.proxy(renames["SelectionListOut"]).optional(),
            "user": t.proxy(renames["SingleUserOut"]).optional(),
            "textList": t.proxy(renames["TextListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldValueOut"])
    types["ConsolidationStrategyIn"] = t.struct(
        {
            "none": t.proxy(renames["NoConsolidationIn"]).optional(),
            "legacy": t.proxy(renames["LegacyIn"]).optional(),
        }
    ).named(renames["ConsolidationStrategyIn"])
    types["ConsolidationStrategyOut"] = t.struct(
        {
            "none": t.proxy(renames["NoConsolidationOut"]).optional(),
            "legacy": t.proxy(renames["LegacyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsolidationStrategyOut"])
    types["IntegerIn"] = t.struct({"value": t.string().optional()}).named(
        renames["IntegerIn"]
    )
    types["IntegerOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerOut"])
    types["ImpersonationIn"] = t.struct(
        {"impersonatedUser": t.proxy(renames["UserIn"]).optional()}
    ).named(renames["ImpersonationIn"])
    types["ImpersonationOut"] = t.struct(
        {
            "impersonatedUser": t.proxy(renames["UserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImpersonationOut"])
    types["FolderIn"] = t.struct({"type": t.string().optional()}).named(
        renames["FolderIn"]
    )
    types["FolderOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOut"])
    types["RestoreIn"] = t.struct({"type": t.string().optional()}).named(
        renames["RestoreIn"]
    )
    types["RestoreOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreOut"])
    types["DriveItemIn"] = t.struct(
        {
            "file": t.proxy(renames["FileIn"]).optional(),
            "title": t.string().optional(),
            "owner": t.proxy(renames["OwnerIn"]).optional(),
            "name": t.string().optional(),
            "driveFolder": t.proxy(renames["DriveFolderIn"]).optional(),
            "folder": t.proxy(renames["FolderIn"]).optional(),
            "driveFile": t.proxy(renames["DriveFileIn"]).optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["DriveItemIn"])
    types["DriveItemOut"] = t.struct(
        {
            "file": t.proxy(renames["FileOut"]).optional(),
            "title": t.string().optional(),
            "owner": t.proxy(renames["OwnerOut"]).optional(),
            "name": t.string().optional(),
            "driveFolder": t.proxy(renames["DriveFolderOut"]).optional(),
            "folder": t.proxy(renames["FolderOut"]).optional(),
            "driveFile": t.proxy(renames["DriveFileOut"]).optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveItemOut"])
    types["QueryDriveActivityRequestIn"] = t.struct(
        {
            "ancestorName": t.string().optional(),
            "itemName": t.string().optional(),
            "pageToken": t.string().optional(),
            "filter": t.string().optional(),
            "consolidationStrategy": t.proxy(
                renames["ConsolidationStrategyIn"]
            ).optional(),
            "pageSize": t.integer().optional(),
        }
    ).named(renames["QueryDriveActivityRequestIn"])
    types["QueryDriveActivityRequestOut"] = t.struct(
        {
            "ancestorName": t.string().optional(),
            "itemName": t.string().optional(),
            "pageToken": t.string().optional(),
            "filter": t.string().optional(),
            "consolidationStrategy": t.proxy(
                renames["ConsolidationStrategyOut"]
            ).optional(),
            "pageSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryDriveActivityRequestOut"])
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
            "types": t.array(t.string()).optional(),
            "fieldChanges": t.array(t.proxy(renames["FieldValueChangeIn"])).optional(),
            "label": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["AppliedLabelChangeDetailIn"])
    types["AppliedLabelChangeDetailOut"] = t.struct(
        {
            "types": t.array(t.string()).optional(),
            "fieldChanges": t.array(t.proxy(renames["FieldValueChangeOut"])).optional(),
            "label": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppliedLabelChangeDetailOut"])
    types["DriveItemReferenceIn"] = t.struct(
        {
            "file": t.proxy(renames["FileIn"]).optional(),
            "folder": t.proxy(renames["FolderIn"]).optional(),
            "title": t.string().optional(),
            "driveFile": t.proxy(renames["DriveFileIn"]).optional(),
            "driveFolder": t.proxy(renames["DriveFolderIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DriveItemReferenceIn"])
    types["DriveItemReferenceOut"] = t.struct(
        {
            "file": t.proxy(renames["FileOut"]).optional(),
            "folder": t.proxy(renames["FolderOut"]).optional(),
            "title": t.string().optional(),
            "driveFile": t.proxy(renames["DriveFileOut"]).optional(),
            "driveFolder": t.proxy(renames["DriveFolderOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveItemReferenceOut"])
    types["SingleUserIn"] = t.struct({"value": t.string().optional()}).named(
        renames["SingleUserIn"]
    )
    types["SingleUserOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SingleUserOut"])
    types["GroupIn"] = t.struct(
        {"email": t.string().optional(), "title": t.string().optional()}
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "email": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
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
    types["TeamDriveReferenceIn"] = t.struct(
        {"title": t.string().optional(), "name": t.string().optional()}
    ).named(renames["TeamDriveReferenceIn"])
    types["TeamDriveReferenceOut"] = t.struct(
        {
            "title": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TeamDriveReferenceOut"])
    types["ActionIn"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "target": t.proxy(renames["TargetIn"]).optional(),
            "timeRange": t.proxy(renames["TimeRangeIn"]).optional(),
            "actor": t.proxy(renames["ActorIn"]).optional(),
            "detail": t.proxy(renames["ActionDetailIn"]).optional(),
        }
    ).named(renames["ActionIn"])
    types["ActionOut"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "target": t.proxy(renames["TargetOut"]).optional(),
            "timeRange": t.proxy(renames["TimeRangeOut"]).optional(),
            "actor": t.proxy(renames["ActorOut"]).optional(),
            "detail": t.proxy(renames["ActionDetailOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionOut"])
    types["FileIn"] = t.struct({"_": t.string().optional()}).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FileOut"])
    types["TargetIn"] = t.struct(
        {
            "fileComment": t.proxy(renames["FileCommentIn"]).optional(),
            "teamDrive": t.proxy(renames["TeamDriveIn"]).optional(),
            "driveItem": t.proxy(renames["DriveItemIn"]).optional(),
            "drive": t.proxy(renames["DriveIn"]).optional(),
        }
    ).named(renames["TargetIn"])
    types["TargetOut"] = t.struct(
        {
            "fileComment": t.proxy(renames["FileCommentOut"]).optional(),
            "teamDrive": t.proxy(renames["TeamDriveOut"]).optional(),
            "driveItem": t.proxy(renames["DriveItemOut"]).optional(),
            "drive": t.proxy(renames["DriveOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetOut"])
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
    types["TextIn"] = t.struct({"value": t.string().optional()}).named(
        renames["TextIn"]
    )
    types["TextOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextOut"])
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
    types["AnyoneIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AnyoneIn"]
    )
    types["AnyoneOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AnyoneOut"])
    types["UserListIn"] = t.struct(
        {"values": t.array(t.proxy(renames["SingleUserIn"])).optional()}
    ).named(renames["UserListIn"])
    types["UserListOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["SingleUserOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserListOut"])
    types["PostIn"] = t.struct({"subtype": t.string().optional()}).named(
        renames["PostIn"]
    )
    types["PostOut"] = t.struct(
        {
            "subtype": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostOut"])
    types["UploadIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadIn"]
    )
    types["UploadOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadOut"])
    types["EditIn"] = t.struct({"_": t.string().optional()}).named(renames["EditIn"])
    types["EditOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EditOut"])
    types["DriveIn"] = t.struct(
        {
            "root": t.proxy(renames["DriveItemIn"]).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["DriveIn"])
    types["DriveOut"] = t.struct(
        {
            "root": t.proxy(renames["DriveItemOut"]).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveOut"])
    types["MoveIn"] = t.struct(
        {
            "addedParents": t.array(t.proxy(renames["TargetReferenceIn"])).optional(),
            "removedParents": t.array(t.proxy(renames["TargetReferenceIn"])).optional(),
        }
    ).named(renames["MoveIn"])
    types["MoveOut"] = t.struct(
        {
            "addedParents": t.array(t.proxy(renames["TargetReferenceOut"])).optional(),
            "removedParents": t.array(
                t.proxy(renames["TargetReferenceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveOut"])
    types["ApplicationReferenceIn"] = t.struct({"type": t.string().optional()}).named(
        renames["ApplicationReferenceIn"]
    )
    types["ApplicationReferenceOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationReferenceOut"])
    types["RenameIn"] = t.struct(
        {"newTitle": t.string().optional(), "oldTitle": t.string().optional()}
    ).named(renames["RenameIn"])
    types["RenameOut"] = t.struct(
        {
            "newTitle": t.string().optional(),
            "oldTitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RenameOut"])
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
    types["DriveFileIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DriveFileIn"]
    )
    types["DriveFileOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveFileOut"])
    types["SuggestionIn"] = t.struct({"subtype": t.string().optional()}).named(
        renames["SuggestionIn"]
    )
    types["SuggestionOut"] = t.struct(
        {
            "subtype": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestionOut"])
    types["DeleteIn"] = t.struct({"type": t.string().optional()}).named(
        renames["DeleteIn"]
    )
    types["DeleteOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteOut"])
    types["OwnerIn"] = t.struct(
        {
            "teamDrive": t.proxy(renames["TeamDriveReferenceIn"]).optional(),
            "drive": t.proxy(renames["DriveReferenceIn"]).optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "domain": t.proxy(renames["DomainIn"]).optional(),
        }
    ).named(renames["OwnerIn"])
    types["OwnerOut"] = t.struct(
        {
            "teamDrive": t.proxy(renames["TeamDriveReferenceOut"]).optional(),
            "drive": t.proxy(renames["DriveReferenceOut"]).optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "domain": t.proxy(renames["DomainOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OwnerOut"])
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
    types["TextListIn"] = t.struct(
        {"values": t.array(t.proxy(renames["TextIn"])).optional()}
    ).named(renames["TextListIn"])
    types["TextListOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["TextOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextListOut"])
    types["PermissionIn"] = t.struct(
        {
            "domain": t.proxy(renames["DomainIn"]).optional(),
            "anyone": t.proxy(renames["AnyoneIn"]).optional(),
            "allowDiscovery": t.boolean().optional(),
            "group": t.proxy(renames["GroupIn"]).optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["PermissionIn"])
    types["PermissionOut"] = t.struct(
        {
            "domain": t.proxy(renames["DomainOut"]).optional(),
            "anyone": t.proxy(renames["AnyoneOut"]).optional(),
            "allowDiscovery": t.boolean().optional(),
            "group": t.proxy(renames["GroupOut"]).optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionOut"])
    types["ActorIn"] = t.struct(
        {
            "impersonation": t.proxy(renames["ImpersonationIn"]).optional(),
            "anonymous": t.proxy(renames["AnonymousUserIn"]).optional(),
            "system": t.proxy(renames["SystemEventIn"]).optional(),
            "administrator": t.proxy(renames["AdministratorIn"]).optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
        }
    ).named(renames["ActorIn"])
    types["ActorOut"] = t.struct(
        {
            "impersonation": t.proxy(renames["ImpersonationOut"]).optional(),
            "anonymous": t.proxy(renames["AnonymousUserOut"]).optional(),
            "system": t.proxy(renames["SystemEventOut"]).optional(),
            "administrator": t.proxy(renames["AdministratorOut"]).optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActorOut"])
    types["NoConsolidationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["NoConsolidationIn"]
    )
    types["NoConsolidationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["NoConsolidationOut"])
    types["DataLeakPreventionChangeIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["DataLeakPreventionChangeIn"])
    types["DataLeakPreventionChangeOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataLeakPreventionChangeOut"])
    types["DriveFolderIn"] = t.struct({"type": t.string().optional()}).named(
        renames["DriveFolderIn"]
    )
    types["DriveFolderOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveFolderOut"])
    types["LegacyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LegacyIn"]
    )
    types["LegacyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LegacyOut"])
    types["DriveActivityIn"] = t.struct(
        {
            "timeRange": t.proxy(renames["TimeRangeIn"]).optional(),
            "actions": t.array(t.proxy(renames["ActionIn"])).optional(),
            "actors": t.array(t.proxy(renames["ActorIn"])).optional(),
            "primaryActionDetail": t.proxy(renames["ActionDetailIn"]).optional(),
            "targets": t.array(t.proxy(renames["TargetIn"])).optional(),
            "timestamp": t.string().optional(),
        }
    ).named(renames["DriveActivityIn"])
    types["DriveActivityOut"] = t.struct(
        {
            "timeRange": t.proxy(renames["TimeRangeOut"]).optional(),
            "actions": t.array(t.proxy(renames["ActionOut"])).optional(),
            "actors": t.array(t.proxy(renames["ActorOut"])).optional(),
            "primaryActionDetail": t.proxy(renames["ActionDetailOut"]).optional(),
            "targets": t.array(t.proxy(renames["TargetOut"])).optional(),
            "timestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveActivityOut"])
    types["CommentIn"] = t.struct(
        {
            "mentionedUsers": t.array(t.proxy(renames["UserIn"])).optional(),
            "assignment": t.proxy(renames["AssignmentIn"]).optional(),
            "suggestion": t.proxy(renames["SuggestionIn"]).optional(),
            "post": t.proxy(renames["PostIn"]).optional(),
        }
    ).named(renames["CommentIn"])
    types["CommentOut"] = t.struct(
        {
            "mentionedUsers": t.array(t.proxy(renames["UserOut"])).optional(),
            "assignment": t.proxy(renames["AssignmentOut"]).optional(),
            "suggestion": t.proxy(renames["SuggestionOut"]).optional(),
            "post": t.proxy(renames["PostOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentOut"])
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
    types["TargetReferenceIn"] = t.struct(
        {
            "teamDrive": t.proxy(renames["TeamDriveReferenceIn"]).optional(),
            "driveItem": t.proxy(renames["DriveItemReferenceIn"]).optional(),
            "drive": t.proxy(renames["DriveReferenceIn"]).optional(),
        }
    ).named(renames["TargetReferenceIn"])
    types["TargetReferenceOut"] = t.struct(
        {
            "teamDrive": t.proxy(renames["TeamDriveReferenceOut"]).optional(),
            "driveItem": t.proxy(renames["DriveItemReferenceOut"]).optional(),
            "drive": t.proxy(renames["DriveReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetReferenceOut"])

    functions = {}
    functions["activityQuery"] = driveactivity.post(
        "v2/activity:query",
        t.struct(
            {
                "ancestorName": t.string().optional(),
                "itemName": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "consolidationStrategy": t.proxy(
                    renames["ConsolidationStrategyIn"]
                ).optional(),
                "pageSize": t.integer().optional(),
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
