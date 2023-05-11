from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_driveactivity() -> Import:
    driveactivity = HTTPRuntime("https://driveactivity.googleapis.com/")

    renames = {
        "ErrorResponse": "_driveactivity_1_ErrorResponse",
        "PermissionChangeIn": "_driveactivity_2_PermissionChangeIn",
        "PermissionChangeOut": "_driveactivity_3_PermissionChangeOut",
        "TeamDriveIn": "_driveactivity_4_TeamDriveIn",
        "TeamDriveOut": "_driveactivity_5_TeamDriveOut",
        "LegacyIn": "_driveactivity_6_LegacyIn",
        "LegacyOut": "_driveactivity_7_LegacyOut",
        "RestrictionChangeIn": "_driveactivity_8_RestrictionChangeIn",
        "RestrictionChangeOut": "_driveactivity_9_RestrictionChangeOut",
        "UserIn": "_driveactivity_10_UserIn",
        "UserOut": "_driveactivity_11_UserOut",
        "CommentIn": "_driveactivity_12_CommentIn",
        "CommentOut": "_driveactivity_13_CommentOut",
        "DriveItemReferenceIn": "_driveactivity_14_DriveItemReferenceIn",
        "DriveItemReferenceOut": "_driveactivity_15_DriveItemReferenceOut",
        "UploadIn": "_driveactivity_16_UploadIn",
        "UploadOut": "_driveactivity_17_UploadOut",
        "TextListIn": "_driveactivity_18_TextListIn",
        "TextListOut": "_driveactivity_19_TextListOut",
        "DataLeakPreventionChangeIn": "_driveactivity_20_DataLeakPreventionChangeIn",
        "DataLeakPreventionChangeOut": "_driveactivity_21_DataLeakPreventionChangeOut",
        "FieldValueIn": "_driveactivity_22_FieldValueIn",
        "FieldValueOut": "_driveactivity_23_FieldValueOut",
        "RestoreIn": "_driveactivity_24_RestoreIn",
        "RestoreOut": "_driveactivity_25_RestoreOut",
        "ActionIn": "_driveactivity_26_ActionIn",
        "ActionOut": "_driveactivity_27_ActionOut",
        "ApplicationReferenceIn": "_driveactivity_28_ApplicationReferenceIn",
        "ApplicationReferenceOut": "_driveactivity_29_ApplicationReferenceOut",
        "SuggestionIn": "_driveactivity_30_SuggestionIn",
        "SuggestionOut": "_driveactivity_31_SuggestionOut",
        "SystemEventIn": "_driveactivity_32_SystemEventIn",
        "SystemEventOut": "_driveactivity_33_SystemEventOut",
        "GroupIn": "_driveactivity_34_GroupIn",
        "GroupOut": "_driveactivity_35_GroupOut",
        "QueryDriveActivityRequestIn": "_driveactivity_36_QueryDriveActivityRequestIn",
        "QueryDriveActivityRequestOut": "_driveactivity_37_QueryDriveActivityRequestOut",
        "SettingsChangeIn": "_driveactivity_38_SettingsChangeIn",
        "SettingsChangeOut": "_driveactivity_39_SettingsChangeOut",
        "SingleUserIn": "_driveactivity_40_SingleUserIn",
        "SingleUserOut": "_driveactivity_41_SingleUserOut",
        "NoConsolidationIn": "_driveactivity_42_NoConsolidationIn",
        "NoConsolidationOut": "_driveactivity_43_NoConsolidationOut",
        "ImpersonationIn": "_driveactivity_44_ImpersonationIn",
        "ImpersonationOut": "_driveactivity_45_ImpersonationOut",
        "DomainIn": "_driveactivity_46_DomainIn",
        "DomainOut": "_driveactivity_47_DomainOut",
        "TeamDriveReferenceIn": "_driveactivity_48_TeamDriveReferenceIn",
        "TeamDriveReferenceOut": "_driveactivity_49_TeamDriveReferenceOut",
        "PostIn": "_driveactivity_50_PostIn",
        "PostOut": "_driveactivity_51_PostOut",
        "DriveIn": "_driveactivity_52_DriveIn",
        "DriveOut": "_driveactivity_53_DriveOut",
        "RenameIn": "_driveactivity_54_RenameIn",
        "RenameOut": "_driveactivity_55_RenameOut",
        "AssignmentIn": "_driveactivity_56_AssignmentIn",
        "AssignmentOut": "_driveactivity_57_AssignmentOut",
        "ActionDetailIn": "_driveactivity_58_ActionDetailIn",
        "ActionDetailOut": "_driveactivity_59_ActionDetailOut",
        "DriveActivityIn": "_driveactivity_60_DriveActivityIn",
        "DriveActivityOut": "_driveactivity_61_DriveActivityOut",
        "DriveItemIn": "_driveactivity_62_DriveItemIn",
        "DriveItemOut": "_driveactivity_63_DriveItemOut",
        "DriveReferenceIn": "_driveactivity_64_DriveReferenceIn",
        "DriveReferenceOut": "_driveactivity_65_DriveReferenceOut",
        "FolderIn": "_driveactivity_66_FolderIn",
        "FolderOut": "_driveactivity_67_FolderOut",
        "SelectionListIn": "_driveactivity_68_SelectionListIn",
        "SelectionListOut": "_driveactivity_69_SelectionListOut",
        "PermissionIn": "_driveactivity_70_PermissionIn",
        "PermissionOut": "_driveactivity_71_PermissionOut",
        "TimeRangeIn": "_driveactivity_72_TimeRangeIn",
        "TimeRangeOut": "_driveactivity_73_TimeRangeOut",
        "SelectionIn": "_driveactivity_74_SelectionIn",
        "SelectionOut": "_driveactivity_75_SelectionOut",
        "AdministratorIn": "_driveactivity_76_AdministratorIn",
        "AdministratorOut": "_driveactivity_77_AdministratorOut",
        "AppliedLabelChangeDetailIn": "_driveactivity_78_AppliedLabelChangeDetailIn",
        "AppliedLabelChangeDetailOut": "_driveactivity_79_AppliedLabelChangeDetailOut",
        "TargetIn": "_driveactivity_80_TargetIn",
        "TargetOut": "_driveactivity_81_TargetOut",
        "TargetReferenceIn": "_driveactivity_82_TargetReferenceIn",
        "TargetReferenceOut": "_driveactivity_83_TargetReferenceOut",
        "QueryDriveActivityResponseIn": "_driveactivity_84_QueryDriveActivityResponseIn",
        "QueryDriveActivityResponseOut": "_driveactivity_85_QueryDriveActivityResponseOut",
        "FieldValueChangeIn": "_driveactivity_86_FieldValueChangeIn",
        "FieldValueChangeOut": "_driveactivity_87_FieldValueChangeOut",
        "ConsolidationStrategyIn": "_driveactivity_88_ConsolidationStrategyIn",
        "ConsolidationStrategyOut": "_driveactivity_89_ConsolidationStrategyOut",
        "UnknownUserIn": "_driveactivity_90_UnknownUserIn",
        "UnknownUserOut": "_driveactivity_91_UnknownUserOut",
        "AnonymousUserIn": "_driveactivity_92_AnonymousUserIn",
        "AnonymousUserOut": "_driveactivity_93_AnonymousUserOut",
        "CopyIn": "_driveactivity_94_CopyIn",
        "CopyOut": "_driveactivity_95_CopyOut",
        "FileCommentIn": "_driveactivity_96_FileCommentIn",
        "FileCommentOut": "_driveactivity_97_FileCommentOut",
        "AnyoneIn": "_driveactivity_98_AnyoneIn",
        "AnyoneOut": "_driveactivity_99_AnyoneOut",
        "DeleteIn": "_driveactivity_100_DeleteIn",
        "DeleteOut": "_driveactivity_101_DeleteOut",
        "AppliedLabelChangeIn": "_driveactivity_102_AppliedLabelChangeIn",
        "AppliedLabelChangeOut": "_driveactivity_103_AppliedLabelChangeOut",
        "IntegerIn": "_driveactivity_104_IntegerIn",
        "IntegerOut": "_driveactivity_105_IntegerOut",
        "NewIn": "_driveactivity_106_NewIn",
        "NewOut": "_driveactivity_107_NewOut",
        "ActorIn": "_driveactivity_108_ActorIn",
        "ActorOut": "_driveactivity_109_ActorOut",
        "OwnerIn": "_driveactivity_110_OwnerIn",
        "OwnerOut": "_driveactivity_111_OwnerOut",
        "DeletedUserIn": "_driveactivity_112_DeletedUserIn",
        "DeletedUserOut": "_driveactivity_113_DeletedUserOut",
        "KnownUserIn": "_driveactivity_114_KnownUserIn",
        "KnownUserOut": "_driveactivity_115_KnownUserOut",
        "CreateIn": "_driveactivity_116_CreateIn",
        "CreateOut": "_driveactivity_117_CreateOut",
        "DriveFileIn": "_driveactivity_118_DriveFileIn",
        "DriveFileOut": "_driveactivity_119_DriveFileOut",
        "TextIn": "_driveactivity_120_TextIn",
        "TextOut": "_driveactivity_121_TextOut",
        "MoveIn": "_driveactivity_122_MoveIn",
        "MoveOut": "_driveactivity_123_MoveOut",
        "UserListIn": "_driveactivity_124_UserListIn",
        "UserListOut": "_driveactivity_125_UserListOut",
        "DateIn": "_driveactivity_126_DateIn",
        "DateOut": "_driveactivity_127_DateOut",
        "DriveFolderIn": "_driveactivity_128_DriveFolderIn",
        "DriveFolderOut": "_driveactivity_129_DriveFolderOut",
        "FileIn": "_driveactivity_130_FileIn",
        "FileOut": "_driveactivity_131_FileOut",
        "EditIn": "_driveactivity_132_EditIn",
        "EditOut": "_driveactivity_133_EditOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["TeamDriveIn"] = t.struct(
        {
            "root": t.proxy(renames["DriveItemIn"]).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["TeamDriveIn"])
    types["TeamDriveOut"] = t.struct(
        {
            "root": t.proxy(renames["DriveItemOut"]).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TeamDriveOut"])
    types["LegacyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LegacyIn"]
    )
    types["LegacyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LegacyOut"])
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
    types["UserIn"] = t.struct(
        {
            "deletedUser": t.proxy(renames["DeletedUserIn"]).optional(),
            "unknownUser": t.proxy(renames["UnknownUserIn"]).optional(),
            "knownUser": t.proxy(renames["KnownUserIn"]).optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "deletedUser": t.proxy(renames["DeletedUserOut"]).optional(),
            "unknownUser": t.proxy(renames["UnknownUserOut"]).optional(),
            "knownUser": t.proxy(renames["KnownUserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
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
    types["DriveItemReferenceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "driveFolder": t.proxy(renames["DriveFolderIn"]).optional(),
            "driveFile": t.proxy(renames["DriveFileIn"]).optional(),
            "folder": t.proxy(renames["FolderIn"]).optional(),
            "file": t.proxy(renames["FileIn"]).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["DriveItemReferenceIn"])
    types["DriveItemReferenceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "driveFolder": t.proxy(renames["DriveFolderOut"]).optional(),
            "driveFile": t.proxy(renames["DriveFileOut"]).optional(),
            "folder": t.proxy(renames["FolderOut"]).optional(),
            "file": t.proxy(renames["FileOut"]).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveItemReferenceOut"])
    types["UploadIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadIn"]
    )
    types["UploadOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadOut"])
    types["TextListIn"] = t.struct(
        {"values": t.array(t.proxy(renames["TextIn"])).optional()}
    ).named(renames["TextListIn"])
    types["TextListOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["TextOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextListOut"])
    types["DataLeakPreventionChangeIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["DataLeakPreventionChangeIn"])
    types["DataLeakPreventionChangeOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataLeakPreventionChangeOut"])
    types["FieldValueIn"] = t.struct(
        {
            "userList": t.proxy(renames["UserListIn"]).optional(),
            "user": t.proxy(renames["SingleUserIn"]).optional(),
            "text": t.proxy(renames["TextIn"]).optional(),
            "integer": t.proxy(renames["IntegerIn"]).optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "selection": t.proxy(renames["SelectionIn"]).optional(),
            "textList": t.proxy(renames["TextListIn"]).optional(),
            "selectionList": t.proxy(renames["SelectionListIn"]).optional(),
        }
    ).named(renames["FieldValueIn"])
    types["FieldValueOut"] = t.struct(
        {
            "userList": t.proxy(renames["UserListOut"]).optional(),
            "user": t.proxy(renames["SingleUserOut"]).optional(),
            "text": t.proxy(renames["TextOut"]).optional(),
            "integer": t.proxy(renames["IntegerOut"]).optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "selection": t.proxy(renames["SelectionOut"]).optional(),
            "textList": t.proxy(renames["TextListOut"]).optional(),
            "selectionList": t.proxy(renames["SelectionListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldValueOut"])
    types["RestoreIn"] = t.struct({"type": t.string().optional()}).named(
        renames["RestoreIn"]
    )
    types["RestoreOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreOut"])
    types["ActionIn"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "target": t.proxy(renames["TargetIn"]).optional(),
            "actor": t.proxy(renames["ActorIn"]).optional(),
            "timeRange": t.proxy(renames["TimeRangeIn"]).optional(),
            "detail": t.proxy(renames["ActionDetailIn"]).optional(),
        }
    ).named(renames["ActionIn"])
    types["ActionOut"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "target": t.proxy(renames["TargetOut"]).optional(),
            "actor": t.proxy(renames["ActorOut"]).optional(),
            "timeRange": t.proxy(renames["TimeRangeOut"]).optional(),
            "detail": t.proxy(renames["ActionDetailOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionOut"])
    types["ApplicationReferenceIn"] = t.struct({"type": t.string().optional()}).named(
        renames["ApplicationReferenceIn"]
    )
    types["ApplicationReferenceOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationReferenceOut"])
    types["SuggestionIn"] = t.struct({"subtype": t.string().optional()}).named(
        renames["SuggestionIn"]
    )
    types["SuggestionOut"] = t.struct(
        {
            "subtype": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestionOut"])
    types["SystemEventIn"] = t.struct({"type": t.string().optional()}).named(
        renames["SystemEventIn"]
    )
    types["SystemEventOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemEventOut"])
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
    types["QueryDriveActivityRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "ancestorName": t.string().optional(),
            "consolidationStrategy": t.proxy(
                renames["ConsolidationStrategyIn"]
            ).optional(),
            "itemName": t.string().optional(),
            "filter": t.string().optional(),
            "pageToken": t.string().optional(),
        }
    ).named(renames["QueryDriveActivityRequestIn"])
    types["QueryDriveActivityRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "ancestorName": t.string().optional(),
            "consolidationStrategy": t.proxy(
                renames["ConsolidationStrategyOut"]
            ).optional(),
            "itemName": t.string().optional(),
            "filter": t.string().optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryDriveActivityRequestOut"])
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
    types["SingleUserIn"] = t.struct({"value": t.string().optional()}).named(
        renames["SingleUserIn"]
    )
    types["SingleUserOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SingleUserOut"])
    types["NoConsolidationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["NoConsolidationIn"]
    )
    types["NoConsolidationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["NoConsolidationOut"])
    types["ImpersonationIn"] = t.struct(
        {"impersonatedUser": t.proxy(renames["UserIn"]).optional()}
    ).named(renames["ImpersonationIn"])
    types["ImpersonationOut"] = t.struct(
        {
            "impersonatedUser": t.proxy(renames["UserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImpersonationOut"])
    types["DomainIn"] = t.struct(
        {"name": t.string().optional(), "legacyId": t.string().optional()}
    ).named(renames["DomainIn"])
    types["DomainOut"] = t.struct(
        {
            "name": t.string().optional(),
            "legacyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainOut"])
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
    types["PostIn"] = t.struct({"subtype": t.string().optional()}).named(
        renames["PostIn"]
    )
    types["PostOut"] = t.struct(
        {
            "subtype": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostOut"])
    types["DriveIn"] = t.struct(
        {
            "title": t.string().optional(),
            "name": t.string().optional(),
            "root": t.proxy(renames["DriveItemIn"]).optional(),
        }
    ).named(renames["DriveIn"])
    types["DriveOut"] = t.struct(
        {
            "title": t.string().optional(),
            "name": t.string().optional(),
            "root": t.proxy(renames["DriveItemOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveOut"])
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
    types["AssignmentIn"] = t.struct(
        {
            "assignedUser": t.proxy(renames["UserIn"]).optional(),
            "subtype": t.string().optional(),
        }
    ).named(renames["AssignmentIn"])
    types["AssignmentOut"] = t.struct(
        {
            "assignedUser": t.proxy(renames["UserOut"]).optional(),
            "subtype": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignmentOut"])
    types["ActionDetailIn"] = t.struct(
        {
            "restore": t.proxy(renames["RestoreIn"]).optional(),
            "edit": t.proxy(renames["EditIn"]).optional(),
            "permissionChange": t.proxy(renames["PermissionChangeIn"]).optional(),
            "settingsChange": t.proxy(renames["SettingsChangeIn"]).optional(),
            "comment": t.proxy(renames["CommentIn"]).optional(),
            "create": t.proxy(renames["CreateIn"]).optional(),
            "move": t.proxy(renames["MoveIn"]).optional(),
            "reference": t.proxy(renames["ApplicationReferenceIn"]).optional(),
            "appliedLabelChange": t.proxy(renames["AppliedLabelChangeIn"]).optional(),
            "delete": t.proxy(renames["DeleteIn"]).optional(),
            "rename": t.proxy(renames["RenameIn"]).optional(),
            "dlpChange": t.proxy(renames["DataLeakPreventionChangeIn"]).optional(),
        }
    ).named(renames["ActionDetailIn"])
    types["ActionDetailOut"] = t.struct(
        {
            "restore": t.proxy(renames["RestoreOut"]).optional(),
            "edit": t.proxy(renames["EditOut"]).optional(),
            "permissionChange": t.proxy(renames["PermissionChangeOut"]).optional(),
            "settingsChange": t.proxy(renames["SettingsChangeOut"]).optional(),
            "comment": t.proxy(renames["CommentOut"]).optional(),
            "create": t.proxy(renames["CreateOut"]).optional(),
            "move": t.proxy(renames["MoveOut"]).optional(),
            "reference": t.proxy(renames["ApplicationReferenceOut"]).optional(),
            "appliedLabelChange": t.proxy(renames["AppliedLabelChangeOut"]).optional(),
            "delete": t.proxy(renames["DeleteOut"]).optional(),
            "rename": t.proxy(renames["RenameOut"]).optional(),
            "dlpChange": t.proxy(renames["DataLeakPreventionChangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionDetailOut"])
    types["DriveActivityIn"] = t.struct(
        {
            "primaryActionDetail": t.proxy(renames["ActionDetailIn"]).optional(),
            "targets": t.array(t.proxy(renames["TargetIn"])).optional(),
            "timeRange": t.proxy(renames["TimeRangeIn"]).optional(),
            "actors": t.array(t.proxy(renames["ActorIn"])).optional(),
            "actions": t.array(t.proxy(renames["ActionIn"])).optional(),
            "timestamp": t.string().optional(),
        }
    ).named(renames["DriveActivityIn"])
    types["DriveActivityOut"] = t.struct(
        {
            "primaryActionDetail": t.proxy(renames["ActionDetailOut"]).optional(),
            "targets": t.array(t.proxy(renames["TargetOut"])).optional(),
            "timeRange": t.proxy(renames["TimeRangeOut"]).optional(),
            "actors": t.array(t.proxy(renames["ActorOut"])).optional(),
            "actions": t.array(t.proxy(renames["ActionOut"])).optional(),
            "timestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveActivityOut"])
    types["DriveItemIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "folder": t.proxy(renames["FolderIn"]).optional(),
            "name": t.string().optional(),
            "owner": t.proxy(renames["OwnerIn"]).optional(),
            "title": t.string().optional(),
            "driveFile": t.proxy(renames["DriveFileIn"]).optional(),
            "file": t.proxy(renames["FileIn"]).optional(),
            "driveFolder": t.proxy(renames["DriveFolderIn"]).optional(),
        }
    ).named(renames["DriveItemIn"])
    types["DriveItemOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "folder": t.proxy(renames["FolderOut"]).optional(),
            "name": t.string().optional(),
            "owner": t.proxy(renames["OwnerOut"]).optional(),
            "title": t.string().optional(),
            "driveFile": t.proxy(renames["DriveFileOut"]).optional(),
            "file": t.proxy(renames["FileOut"]).optional(),
            "driveFolder": t.proxy(renames["DriveFolderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveItemOut"])
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
    types["FolderIn"] = t.struct({"type": t.string().optional()}).named(
        renames["FolderIn"]
    )
    types["FolderOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOut"])
    types["SelectionListIn"] = t.struct(
        {"values": t.array(t.proxy(renames["SelectionIn"])).optional()}
    ).named(renames["SelectionListIn"])
    types["SelectionListOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["SelectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SelectionListOut"])
    types["PermissionIn"] = t.struct(
        {
            "anyone": t.proxy(renames["AnyoneIn"]).optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "role": t.string().optional(),
            "domain": t.proxy(renames["DomainIn"]).optional(),
            "allowDiscovery": t.boolean().optional(),
            "group": t.proxy(renames["GroupIn"]).optional(),
        }
    ).named(renames["PermissionIn"])
    types["PermissionOut"] = t.struct(
        {
            "anyone": t.proxy(renames["AnyoneOut"]).optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "role": t.string().optional(),
            "domain": t.proxy(renames["DomainOut"]).optional(),
            "allowDiscovery": t.boolean().optional(),
            "group": t.proxy(renames["GroupOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionOut"])
    types["TimeRangeIn"] = t.struct(
        {"startTime": t.string().optional(), "endTime": t.string().optional()}
    ).named(renames["TimeRangeIn"])
    types["TimeRangeOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeRangeOut"])
    types["SelectionIn"] = t.struct(
        {"displayName": t.string().optional(), "value": t.string().optional()}
    ).named(renames["SelectionIn"])
    types["SelectionOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SelectionOut"])
    types["AdministratorIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdministratorIn"]
    )
    types["AdministratorOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdministratorOut"])
    types["AppliedLabelChangeDetailIn"] = t.struct(
        {
            "types": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "fieldChanges": t.array(t.proxy(renames["FieldValueChangeIn"])).optional(),
            "label": t.string().optional(),
        }
    ).named(renames["AppliedLabelChangeDetailIn"])
    types["AppliedLabelChangeDetailOut"] = t.struct(
        {
            "types": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "fieldChanges": t.array(t.proxy(renames["FieldValueChangeOut"])).optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppliedLabelChangeDetailOut"])
    types["TargetIn"] = t.struct(
        {
            "teamDrive": t.proxy(renames["TeamDriveIn"]).optional(),
            "driveItem": t.proxy(renames["DriveItemIn"]).optional(),
            "drive": t.proxy(renames["DriveIn"]).optional(),
            "fileComment": t.proxy(renames["FileCommentIn"]).optional(),
        }
    ).named(renames["TargetIn"])
    types["TargetOut"] = t.struct(
        {
            "teamDrive": t.proxy(renames["TeamDriveOut"]).optional(),
            "driveItem": t.proxy(renames["DriveItemOut"]).optional(),
            "drive": t.proxy(renames["DriveOut"]).optional(),
            "fileComment": t.proxy(renames["FileCommentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetOut"])
    types["TargetReferenceIn"] = t.struct(
        {
            "teamDrive": t.proxy(renames["TeamDriveReferenceIn"]).optional(),
            "drive": t.proxy(renames["DriveReferenceIn"]).optional(),
            "driveItem": t.proxy(renames["DriveItemReferenceIn"]).optional(),
        }
    ).named(renames["TargetReferenceIn"])
    types["TargetReferenceOut"] = t.struct(
        {
            "teamDrive": t.proxy(renames["TeamDriveReferenceOut"]).optional(),
            "drive": t.proxy(renames["DriveReferenceOut"]).optional(),
            "driveItem": t.proxy(renames["DriveItemReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetReferenceOut"])
    types["QueryDriveActivityResponseIn"] = t.struct(
        {
            "activities": t.array(t.proxy(renames["DriveActivityIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["QueryDriveActivityResponseIn"])
    types["QueryDriveActivityResponseOut"] = t.struct(
        {
            "activities": t.array(t.proxy(renames["DriveActivityOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryDriveActivityResponseOut"])
    types["FieldValueChangeIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "newValue": t.proxy(renames["FieldValueIn"]).optional(),
            "fieldId": t.string().optional(),
            "oldValue": t.proxy(renames["FieldValueIn"]).optional(),
        }
    ).named(renames["FieldValueChangeIn"])
    types["FieldValueChangeOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "newValue": t.proxy(renames["FieldValueOut"]).optional(),
            "fieldId": t.string().optional(),
            "oldValue": t.proxy(renames["FieldValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldValueChangeOut"])
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
    types["UnknownUserIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UnknownUserIn"]
    )
    types["UnknownUserOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UnknownUserOut"])
    types["AnonymousUserIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AnonymousUserIn"]
    )
    types["AnonymousUserOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AnonymousUserOut"])
    types["CopyIn"] = t.struct(
        {"originalObject": t.proxy(renames["TargetReferenceIn"]).optional()}
    ).named(renames["CopyIn"])
    types["CopyOut"] = t.struct(
        {
            "originalObject": t.proxy(renames["TargetReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyOut"])
    types["FileCommentIn"] = t.struct(
        {
            "linkToDiscussion": t.string().optional(),
            "legacyDiscussionId": t.string().optional(),
            "parent": t.proxy(renames["DriveItemIn"]).optional(),
            "legacyCommentId": t.string().optional(),
        }
    ).named(renames["FileCommentIn"])
    types["FileCommentOut"] = t.struct(
        {
            "linkToDiscussion": t.string().optional(),
            "legacyDiscussionId": t.string().optional(),
            "parent": t.proxy(renames["DriveItemOut"]).optional(),
            "legacyCommentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileCommentOut"])
    types["AnyoneIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AnyoneIn"]
    )
    types["AnyoneOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AnyoneOut"])
    types["DeleteIn"] = t.struct({"type": t.string().optional()}).named(
        renames["DeleteIn"]
    )
    types["DeleteOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteOut"])
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
    types["IntegerIn"] = t.struct({"value": t.string().optional()}).named(
        renames["IntegerIn"]
    )
    types["IntegerOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerOut"])
    types["NewIn"] = t.struct({"_": t.string().optional()}).named(renames["NewIn"])
    types["NewOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["NewOut"])
    types["ActorIn"] = t.struct(
        {
            "administrator": t.proxy(renames["AdministratorIn"]).optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "anonymous": t.proxy(renames["AnonymousUserIn"]).optional(),
            "system": t.proxy(renames["SystemEventIn"]).optional(),
            "impersonation": t.proxy(renames["ImpersonationIn"]).optional(),
        }
    ).named(renames["ActorIn"])
    types["ActorOut"] = t.struct(
        {
            "administrator": t.proxy(renames["AdministratorOut"]).optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "anonymous": t.proxy(renames["AnonymousUserOut"]).optional(),
            "system": t.proxy(renames["SystemEventOut"]).optional(),
            "impersonation": t.proxy(renames["ImpersonationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActorOut"])
    types["OwnerIn"] = t.struct(
        {
            "user": t.proxy(renames["UserIn"]).optional(),
            "teamDrive": t.proxy(renames["TeamDriveReferenceIn"]).optional(),
            "domain": t.proxy(renames["DomainIn"]).optional(),
            "drive": t.proxy(renames["DriveReferenceIn"]).optional(),
        }
    ).named(renames["OwnerIn"])
    types["OwnerOut"] = t.struct(
        {
            "user": t.proxy(renames["UserOut"]).optional(),
            "teamDrive": t.proxy(renames["TeamDriveReferenceOut"]).optional(),
            "domain": t.proxy(renames["DomainOut"]).optional(),
            "drive": t.proxy(renames["DriveReferenceOut"]).optional(),
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
    types["CreateIn"] = t.struct(
        {
            "new": t.proxy(renames["NewIn"]).optional(),
            "upload": t.proxy(renames["UploadIn"]).optional(),
            "copy": t.proxy(renames["CopyIn"]).optional(),
        }
    ).named(renames["CreateIn"])
    types["CreateOut"] = t.struct(
        {
            "new": t.proxy(renames["NewOut"]).optional(),
            "upload": t.proxy(renames["UploadOut"]).optional(),
            "copy": t.proxy(renames["CopyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateOut"])
    types["DriveFileIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DriveFileIn"]
    )
    types["DriveFileOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveFileOut"])
    types["TextIn"] = t.struct({"value": t.string().optional()}).named(
        renames["TextIn"]
    )
    types["TextOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextOut"])
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
    types["UserListIn"] = t.struct(
        {"values": t.array(t.proxy(renames["SingleUserIn"])).optional()}
    ).named(renames["UserListIn"])
    types["UserListOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["SingleUserOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserListOut"])
    types["DateIn"] = t.struct({"value": t.string().optional()}).named(
        renames["DateIn"]
    )
    types["DateOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["DriveFolderIn"] = t.struct({"type": t.string().optional()}).named(
        renames["DriveFolderIn"]
    )
    types["DriveFolderOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveFolderOut"])
    types["FileIn"] = t.struct({"_": t.string().optional()}).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FileOut"])
    types["EditIn"] = t.struct({"_": t.string().optional()}).named(renames["EditIn"])
    types["EditOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EditOut"])

    functions = {}
    functions["activityQuery"] = driveactivity.post(
        "v2/activity:query",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "ancestorName": t.string().optional(),
                "consolidationStrategy": t.proxy(
                    renames["ConsolidationStrategyIn"]
                ).optional(),
                "itemName": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryDriveActivityResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="driveactivity", renames=renames, types=types, functions=functions
    )
