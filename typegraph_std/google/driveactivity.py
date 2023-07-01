from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_driveactivity():
    driveactivity = HTTPRuntime("https://driveactivity.googleapis.com/")

    renames = {
        "ErrorResponse": "_driveactivity_1_ErrorResponse",
        "SelectionIn": "_driveactivity_2_SelectionIn",
        "SelectionOut": "_driveactivity_3_SelectionOut",
        "SuggestionIn": "_driveactivity_4_SuggestionIn",
        "SuggestionOut": "_driveactivity_5_SuggestionOut",
        "FolderIn": "_driveactivity_6_FolderIn",
        "FolderOut": "_driveactivity_7_FolderOut",
        "DateIn": "_driveactivity_8_DateIn",
        "DateOut": "_driveactivity_9_DateOut",
        "IntegerIn": "_driveactivity_10_IntegerIn",
        "IntegerOut": "_driveactivity_11_IntegerOut",
        "CommentIn": "_driveactivity_12_CommentIn",
        "CommentOut": "_driveactivity_13_CommentOut",
        "DriveItemReferenceIn": "_driveactivity_14_DriveItemReferenceIn",
        "DriveItemReferenceOut": "_driveactivity_15_DriveItemReferenceOut",
        "AnyoneIn": "_driveactivity_16_AnyoneIn",
        "AnyoneOut": "_driveactivity_17_AnyoneOut",
        "FieldValueChangeIn": "_driveactivity_18_FieldValueChangeIn",
        "FieldValueChangeOut": "_driveactivity_19_FieldValueChangeOut",
        "DriveReferenceIn": "_driveactivity_20_DriveReferenceIn",
        "DriveReferenceOut": "_driveactivity_21_DriveReferenceOut",
        "LegacyIn": "_driveactivity_22_LegacyIn",
        "LegacyOut": "_driveactivity_23_LegacyOut",
        "QueryDriveActivityRequestIn": "_driveactivity_24_QueryDriveActivityRequestIn",
        "QueryDriveActivityRequestOut": "_driveactivity_25_QueryDriveActivityRequestOut",
        "CreateIn": "_driveactivity_26_CreateIn",
        "CreateOut": "_driveactivity_27_CreateOut",
        "NewIn": "_driveactivity_28_NewIn",
        "NewOut": "_driveactivity_29_NewOut",
        "ConsolidationStrategyIn": "_driveactivity_30_ConsolidationStrategyIn",
        "ConsolidationStrategyOut": "_driveactivity_31_ConsolidationStrategyOut",
        "TargetReferenceIn": "_driveactivity_32_TargetReferenceIn",
        "TargetReferenceOut": "_driveactivity_33_TargetReferenceOut",
        "FileCommentIn": "_driveactivity_34_FileCommentIn",
        "FileCommentOut": "_driveactivity_35_FileCommentOut",
        "SelectionListIn": "_driveactivity_36_SelectionListIn",
        "SelectionListOut": "_driveactivity_37_SelectionListOut",
        "KnownUserIn": "_driveactivity_38_KnownUserIn",
        "KnownUserOut": "_driveactivity_39_KnownUserOut",
        "FieldValueIn": "_driveactivity_40_FieldValueIn",
        "FieldValueOut": "_driveactivity_41_FieldValueOut",
        "DriveActivityIn": "_driveactivity_42_DriveActivityIn",
        "DriveActivityOut": "_driveactivity_43_DriveActivityOut",
        "CopyIn": "_driveactivity_44_CopyIn",
        "CopyOut": "_driveactivity_45_CopyOut",
        "SystemEventIn": "_driveactivity_46_SystemEventIn",
        "SystemEventOut": "_driveactivity_47_SystemEventOut",
        "ActionDetailIn": "_driveactivity_48_ActionDetailIn",
        "ActionDetailOut": "_driveactivity_49_ActionDetailOut",
        "GroupIn": "_driveactivity_50_GroupIn",
        "GroupOut": "_driveactivity_51_GroupOut",
        "SingleUserIn": "_driveactivity_52_SingleUserIn",
        "SingleUserOut": "_driveactivity_53_SingleUserOut",
        "DriveIn": "_driveactivity_54_DriveIn",
        "DriveOut": "_driveactivity_55_DriveOut",
        "NoConsolidationIn": "_driveactivity_56_NoConsolidationIn",
        "NoConsolidationOut": "_driveactivity_57_NoConsolidationOut",
        "DriveFolderIn": "_driveactivity_58_DriveFolderIn",
        "DriveFolderOut": "_driveactivity_59_DriveFolderOut",
        "UserListIn": "_driveactivity_60_UserListIn",
        "UserListOut": "_driveactivity_61_UserListOut",
        "UploadIn": "_driveactivity_62_UploadIn",
        "UploadOut": "_driveactivity_63_UploadOut",
        "TextIn": "_driveactivity_64_TextIn",
        "TextOut": "_driveactivity_65_TextOut",
        "DriveItemIn": "_driveactivity_66_DriveItemIn",
        "DriveItemOut": "_driveactivity_67_DriveItemOut",
        "ImpersonationIn": "_driveactivity_68_ImpersonationIn",
        "ImpersonationOut": "_driveactivity_69_ImpersonationOut",
        "RestoreIn": "_driveactivity_70_RestoreIn",
        "RestoreOut": "_driveactivity_71_RestoreOut",
        "PermissionIn": "_driveactivity_72_PermissionIn",
        "PermissionOut": "_driveactivity_73_PermissionOut",
        "TargetIn": "_driveactivity_74_TargetIn",
        "TargetOut": "_driveactivity_75_TargetOut",
        "OwnerIn": "_driveactivity_76_OwnerIn",
        "OwnerOut": "_driveactivity_77_OwnerOut",
        "AssignmentIn": "_driveactivity_78_AssignmentIn",
        "AssignmentOut": "_driveactivity_79_AssignmentOut",
        "DeletedUserIn": "_driveactivity_80_DeletedUserIn",
        "DeletedUserOut": "_driveactivity_81_DeletedUserOut",
        "TeamDriveIn": "_driveactivity_82_TeamDriveIn",
        "TeamDriveOut": "_driveactivity_83_TeamDriveOut",
        "MoveIn": "_driveactivity_84_MoveIn",
        "MoveOut": "_driveactivity_85_MoveOut",
        "QueryDriveActivityResponseIn": "_driveactivity_86_QueryDriveActivityResponseIn",
        "QueryDriveActivityResponseOut": "_driveactivity_87_QueryDriveActivityResponseOut",
        "AnonymousUserIn": "_driveactivity_88_AnonymousUserIn",
        "AnonymousUserOut": "_driveactivity_89_AnonymousUserOut",
        "SettingsChangeIn": "_driveactivity_90_SettingsChangeIn",
        "SettingsChangeOut": "_driveactivity_91_SettingsChangeOut",
        "AdministratorIn": "_driveactivity_92_AdministratorIn",
        "AdministratorOut": "_driveactivity_93_AdministratorOut",
        "AppliedLabelChangeIn": "_driveactivity_94_AppliedLabelChangeIn",
        "AppliedLabelChangeOut": "_driveactivity_95_AppliedLabelChangeOut",
        "PermissionChangeIn": "_driveactivity_96_PermissionChangeIn",
        "PermissionChangeOut": "_driveactivity_97_PermissionChangeOut",
        "AppliedLabelChangeDetailIn": "_driveactivity_98_AppliedLabelChangeDetailIn",
        "AppliedLabelChangeDetailOut": "_driveactivity_99_AppliedLabelChangeDetailOut",
        "EditIn": "_driveactivity_100_EditIn",
        "EditOut": "_driveactivity_101_EditOut",
        "ApplicationReferenceIn": "_driveactivity_102_ApplicationReferenceIn",
        "ApplicationReferenceOut": "_driveactivity_103_ApplicationReferenceOut",
        "DriveFileIn": "_driveactivity_104_DriveFileIn",
        "DriveFileOut": "_driveactivity_105_DriveFileOut",
        "UnknownUserIn": "_driveactivity_106_UnknownUserIn",
        "UnknownUserOut": "_driveactivity_107_UnknownUserOut",
        "DomainIn": "_driveactivity_108_DomainIn",
        "DomainOut": "_driveactivity_109_DomainOut",
        "RestrictionChangeIn": "_driveactivity_110_RestrictionChangeIn",
        "RestrictionChangeOut": "_driveactivity_111_RestrictionChangeOut",
        "UserIn": "_driveactivity_112_UserIn",
        "UserOut": "_driveactivity_113_UserOut",
        "RenameIn": "_driveactivity_114_RenameIn",
        "RenameOut": "_driveactivity_115_RenameOut",
        "DeleteIn": "_driveactivity_116_DeleteIn",
        "DeleteOut": "_driveactivity_117_DeleteOut",
        "TextListIn": "_driveactivity_118_TextListIn",
        "TextListOut": "_driveactivity_119_TextListOut",
        "FileIn": "_driveactivity_120_FileIn",
        "FileOut": "_driveactivity_121_FileOut",
        "TimeRangeIn": "_driveactivity_122_TimeRangeIn",
        "TimeRangeOut": "_driveactivity_123_TimeRangeOut",
        "PostIn": "_driveactivity_124_PostIn",
        "PostOut": "_driveactivity_125_PostOut",
        "ActionIn": "_driveactivity_126_ActionIn",
        "ActionOut": "_driveactivity_127_ActionOut",
        "DataLeakPreventionChangeIn": "_driveactivity_128_DataLeakPreventionChangeIn",
        "DataLeakPreventionChangeOut": "_driveactivity_129_DataLeakPreventionChangeOut",
        "TeamDriveReferenceIn": "_driveactivity_130_TeamDriveReferenceIn",
        "TeamDriveReferenceOut": "_driveactivity_131_TeamDriveReferenceOut",
        "ActorIn": "_driveactivity_132_ActorIn",
        "ActorOut": "_driveactivity_133_ActorOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["SuggestionIn"] = t.struct({"subtype": t.string().optional()}).named(
        renames["SuggestionIn"]
    )
    types["SuggestionOut"] = t.struct(
        {
            "subtype": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestionOut"])
    types["FolderIn"] = t.struct({"type": t.string().optional()}).named(
        renames["FolderIn"]
    )
    types["FolderOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOut"])
    types["DateIn"] = t.struct({"value": t.string().optional()}).named(
        renames["DateIn"]
    )
    types["DateOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["IntegerIn"] = t.struct({"value": t.string().optional()}).named(
        renames["IntegerIn"]
    )
    types["IntegerOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerOut"])
    types["CommentIn"] = t.struct(
        {
            "suggestion": t.proxy(renames["SuggestionIn"]).optional(),
            "mentionedUsers": t.array(t.proxy(renames["UserIn"])).optional(),
            "assignment": t.proxy(renames["AssignmentIn"]).optional(),
            "post": t.proxy(renames["PostIn"]).optional(),
        }
    ).named(renames["CommentIn"])
    types["CommentOut"] = t.struct(
        {
            "suggestion": t.proxy(renames["SuggestionOut"]).optional(),
            "mentionedUsers": t.array(t.proxy(renames["UserOut"])).optional(),
            "assignment": t.proxy(renames["AssignmentOut"]).optional(),
            "post": t.proxy(renames["PostOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentOut"])
    types["DriveItemReferenceIn"] = t.struct(
        {
            "folder": t.proxy(renames["FolderIn"]).optional(),
            "file": t.proxy(renames["FileIn"]).optional(),
            "driveFolder": t.proxy(renames["DriveFolderIn"]).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "driveFile": t.proxy(renames["DriveFileIn"]).optional(),
        }
    ).named(renames["DriveItemReferenceIn"])
    types["DriveItemReferenceOut"] = t.struct(
        {
            "folder": t.proxy(renames["FolderOut"]).optional(),
            "file": t.proxy(renames["FileOut"]).optional(),
            "driveFolder": t.proxy(renames["DriveFolderOut"]).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "driveFile": t.proxy(renames["DriveFileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveItemReferenceOut"])
    types["AnyoneIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AnyoneIn"]
    )
    types["AnyoneOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AnyoneOut"])
    types["FieldValueChangeIn"] = t.struct(
        {
            "oldValue": t.proxy(renames["FieldValueIn"]).optional(),
            "newValue": t.proxy(renames["FieldValueIn"]).optional(),
            "displayName": t.string().optional(),
            "fieldId": t.string().optional(),
        }
    ).named(renames["FieldValueChangeIn"])
    types["FieldValueChangeOut"] = t.struct(
        {
            "oldValue": t.proxy(renames["FieldValueOut"]).optional(),
            "newValue": t.proxy(renames["FieldValueOut"]).optional(),
            "displayName": t.string().optional(),
            "fieldId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldValueChangeOut"])
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
    types["LegacyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LegacyIn"]
    )
    types["LegacyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LegacyOut"])
    types["QueryDriveActivityRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "itemName": t.string().optional(),
            "consolidationStrategy": t.proxy(
                renames["ConsolidationStrategyIn"]
            ).optional(),
            "filter": t.string().optional(),
            "ancestorName": t.string().optional(),
            "pageToken": t.string().optional(),
        }
    ).named(renames["QueryDriveActivityRequestIn"])
    types["QueryDriveActivityRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "itemName": t.string().optional(),
            "consolidationStrategy": t.proxy(
                renames["ConsolidationStrategyOut"]
            ).optional(),
            "filter": t.string().optional(),
            "ancestorName": t.string().optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryDriveActivityRequestOut"])
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
    types["NewIn"] = t.struct({"_": t.string().optional()}).named(renames["NewIn"])
    types["NewOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["NewOut"])
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
    types["TargetReferenceIn"] = t.struct(
        {
            "driveItem": t.proxy(renames["DriveItemReferenceIn"]).optional(),
            "drive": t.proxy(renames["DriveReferenceIn"]).optional(),
            "teamDrive": t.proxy(renames["TeamDriveReferenceIn"]).optional(),
        }
    ).named(renames["TargetReferenceIn"])
    types["TargetReferenceOut"] = t.struct(
        {
            "driveItem": t.proxy(renames["DriveItemReferenceOut"]).optional(),
            "drive": t.proxy(renames["DriveReferenceOut"]).optional(),
            "teamDrive": t.proxy(renames["TeamDriveReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetReferenceOut"])
    types["FileCommentIn"] = t.struct(
        {
            "legacyCommentId": t.string().optional(),
            "legacyDiscussionId": t.string().optional(),
            "linkToDiscussion": t.string().optional(),
            "parent": t.proxy(renames["DriveItemIn"]).optional(),
        }
    ).named(renames["FileCommentIn"])
    types["FileCommentOut"] = t.struct(
        {
            "legacyCommentId": t.string().optional(),
            "legacyDiscussionId": t.string().optional(),
            "linkToDiscussion": t.string().optional(),
            "parent": t.proxy(renames["DriveItemOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileCommentOut"])
    types["SelectionListIn"] = t.struct(
        {"values": t.array(t.proxy(renames["SelectionIn"])).optional()}
    ).named(renames["SelectionListIn"])
    types["SelectionListOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["SelectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SelectionListOut"])
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
    types["FieldValueIn"] = t.struct(
        {
            "userList": t.proxy(renames["UserListIn"]).optional(),
            "text": t.proxy(renames["TextIn"]).optional(),
            "selectionList": t.proxy(renames["SelectionListIn"]).optional(),
            "textList": t.proxy(renames["TextListIn"]).optional(),
            "integer": t.proxy(renames["IntegerIn"]).optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "user": t.proxy(renames["SingleUserIn"]).optional(),
            "selection": t.proxy(renames["SelectionIn"]).optional(),
        }
    ).named(renames["FieldValueIn"])
    types["FieldValueOut"] = t.struct(
        {
            "userList": t.proxy(renames["UserListOut"]).optional(),
            "text": t.proxy(renames["TextOut"]).optional(),
            "selectionList": t.proxy(renames["SelectionListOut"]).optional(),
            "textList": t.proxy(renames["TextListOut"]).optional(),
            "integer": t.proxy(renames["IntegerOut"]).optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "user": t.proxy(renames["SingleUserOut"]).optional(),
            "selection": t.proxy(renames["SelectionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldValueOut"])
    types["DriveActivityIn"] = t.struct(
        {
            "targets": t.array(t.proxy(renames["TargetIn"])).optional(),
            "primaryActionDetail": t.proxy(renames["ActionDetailIn"]).optional(),
            "timeRange": t.proxy(renames["TimeRangeIn"]).optional(),
            "actors": t.array(t.proxy(renames["ActorIn"])).optional(),
            "timestamp": t.string().optional(),
            "actions": t.array(t.proxy(renames["ActionIn"])).optional(),
        }
    ).named(renames["DriveActivityIn"])
    types["DriveActivityOut"] = t.struct(
        {
            "targets": t.array(t.proxy(renames["TargetOut"])).optional(),
            "primaryActionDetail": t.proxy(renames["ActionDetailOut"]).optional(),
            "timeRange": t.proxy(renames["TimeRangeOut"]).optional(),
            "actors": t.array(t.proxy(renames["ActorOut"])).optional(),
            "timestamp": t.string().optional(),
            "actions": t.array(t.proxy(renames["ActionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveActivityOut"])
    types["CopyIn"] = t.struct(
        {"originalObject": t.proxy(renames["TargetReferenceIn"]).optional()}
    ).named(renames["CopyIn"])
    types["CopyOut"] = t.struct(
        {
            "originalObject": t.proxy(renames["TargetReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyOut"])
    types["SystemEventIn"] = t.struct({"type": t.string().optional()}).named(
        renames["SystemEventIn"]
    )
    types["SystemEventOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemEventOut"])
    types["ActionDetailIn"] = t.struct(
        {
            "restore": t.proxy(renames["RestoreIn"]).optional(),
            "appliedLabelChange": t.proxy(renames["AppliedLabelChangeIn"]).optional(),
            "permissionChange": t.proxy(renames["PermissionChangeIn"]).optional(),
            "delete": t.proxy(renames["DeleteIn"]).optional(),
            "reference": t.proxy(renames["ApplicationReferenceIn"]).optional(),
            "move": t.proxy(renames["MoveIn"]).optional(),
            "comment": t.proxy(renames["CommentIn"]).optional(),
            "dlpChange": t.proxy(renames["DataLeakPreventionChangeIn"]).optional(),
            "create": t.proxy(renames["CreateIn"]).optional(),
            "edit": t.proxy(renames["EditIn"]).optional(),
            "settingsChange": t.proxy(renames["SettingsChangeIn"]).optional(),
            "rename": t.proxy(renames["RenameIn"]).optional(),
        }
    ).named(renames["ActionDetailIn"])
    types["ActionDetailOut"] = t.struct(
        {
            "restore": t.proxy(renames["RestoreOut"]).optional(),
            "appliedLabelChange": t.proxy(renames["AppliedLabelChangeOut"]).optional(),
            "permissionChange": t.proxy(renames["PermissionChangeOut"]).optional(),
            "delete": t.proxy(renames["DeleteOut"]).optional(),
            "reference": t.proxy(renames["ApplicationReferenceOut"]).optional(),
            "move": t.proxy(renames["MoveOut"]).optional(),
            "comment": t.proxy(renames["CommentOut"]).optional(),
            "dlpChange": t.proxy(renames["DataLeakPreventionChangeOut"]).optional(),
            "create": t.proxy(renames["CreateOut"]).optional(),
            "edit": t.proxy(renames["EditOut"]).optional(),
            "settingsChange": t.proxy(renames["SettingsChangeOut"]).optional(),
            "rename": t.proxy(renames["RenameOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionDetailOut"])
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
    types["SingleUserIn"] = t.struct({"value": t.string().optional()}).named(
        renames["SingleUserIn"]
    )
    types["SingleUserOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SingleUserOut"])
    types["DriveIn"] = t.struct(
        {
            "name": t.string().optional(),
            "title": t.string().optional(),
            "root": t.proxy(renames["DriveItemIn"]).optional(),
        }
    ).named(renames["DriveIn"])
    types["DriveOut"] = t.struct(
        {
            "name": t.string().optional(),
            "title": t.string().optional(),
            "root": t.proxy(renames["DriveItemOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveOut"])
    types["NoConsolidationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["NoConsolidationIn"]
    )
    types["NoConsolidationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["NoConsolidationOut"])
    types["DriveFolderIn"] = t.struct({"type": t.string().optional()}).named(
        renames["DriveFolderIn"]
    )
    types["DriveFolderOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveFolderOut"])
    types["UserListIn"] = t.struct(
        {"values": t.array(t.proxy(renames["SingleUserIn"])).optional()}
    ).named(renames["UserListIn"])
    types["UserListOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["SingleUserOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserListOut"])
    types["UploadIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadIn"]
    )
    types["UploadOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadOut"])
    types["TextIn"] = t.struct({"value": t.string().optional()}).named(
        renames["TextIn"]
    )
    types["TextOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextOut"])
    types["DriveItemIn"] = t.struct(
        {
            "name": t.string().optional(),
            "driveFile": t.proxy(renames["DriveFileIn"]).optional(),
            "owner": t.proxy(renames["OwnerIn"]).optional(),
            "driveFolder": t.proxy(renames["DriveFolderIn"]).optional(),
            "folder": t.proxy(renames["FolderIn"]).optional(),
            "mimeType": t.string().optional(),
            "file": t.proxy(renames["FileIn"]).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["DriveItemIn"])
    types["DriveItemOut"] = t.struct(
        {
            "name": t.string().optional(),
            "driveFile": t.proxy(renames["DriveFileOut"]).optional(),
            "owner": t.proxy(renames["OwnerOut"]).optional(),
            "driveFolder": t.proxy(renames["DriveFolderOut"]).optional(),
            "folder": t.proxy(renames["FolderOut"]).optional(),
            "mimeType": t.string().optional(),
            "file": t.proxy(renames["FileOut"]).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveItemOut"])
    types["ImpersonationIn"] = t.struct(
        {"impersonatedUser": t.proxy(renames["UserIn"]).optional()}
    ).named(renames["ImpersonationIn"])
    types["ImpersonationOut"] = t.struct(
        {
            "impersonatedUser": t.proxy(renames["UserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImpersonationOut"])
    types["RestoreIn"] = t.struct({"type": t.string().optional()}).named(
        renames["RestoreIn"]
    )
    types["RestoreOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreOut"])
    types["PermissionIn"] = t.struct(
        {
            "anyone": t.proxy(renames["AnyoneIn"]).optional(),
            "allowDiscovery": t.boolean().optional(),
            "role": t.string().optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "group": t.proxy(renames["GroupIn"]).optional(),
            "domain": t.proxy(renames["DomainIn"]).optional(),
        }
    ).named(renames["PermissionIn"])
    types["PermissionOut"] = t.struct(
        {
            "anyone": t.proxy(renames["AnyoneOut"]).optional(),
            "allowDiscovery": t.boolean().optional(),
            "role": t.string().optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "group": t.proxy(renames["GroupOut"]).optional(),
            "domain": t.proxy(renames["DomainOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionOut"])
    types["TargetIn"] = t.struct(
        {
            "drive": t.proxy(renames["DriveIn"]).optional(),
            "fileComment": t.proxy(renames["FileCommentIn"]).optional(),
            "teamDrive": t.proxy(renames["TeamDriveIn"]).optional(),
            "driveItem": t.proxy(renames["DriveItemIn"]).optional(),
        }
    ).named(renames["TargetIn"])
    types["TargetOut"] = t.struct(
        {
            "drive": t.proxy(renames["DriveOut"]).optional(),
            "fileComment": t.proxy(renames["FileCommentOut"]).optional(),
            "teamDrive": t.proxy(renames["TeamDriveOut"]).optional(),
            "driveItem": t.proxy(renames["DriveItemOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetOut"])
    types["OwnerIn"] = t.struct(
        {
            "teamDrive": t.proxy(renames["TeamDriveReferenceIn"]).optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "domain": t.proxy(renames["DomainIn"]).optional(),
            "drive": t.proxy(renames["DriveReferenceIn"]).optional(),
        }
    ).named(renames["OwnerIn"])
    types["OwnerOut"] = t.struct(
        {
            "teamDrive": t.proxy(renames["TeamDriveReferenceOut"]).optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "domain": t.proxy(renames["DomainOut"]).optional(),
            "drive": t.proxy(renames["DriveReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OwnerOut"])
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
    types["DeletedUserIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeletedUserIn"]
    )
    types["DeletedUserOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeletedUserOut"])
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
    types["AnonymousUserIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AnonymousUserIn"]
    )
    types["AnonymousUserOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AnonymousUserOut"])
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
    types["AdministratorIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdministratorIn"]
    )
    types["AdministratorOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdministratorOut"])
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
    types["EditIn"] = t.struct({"_": t.string().optional()}).named(renames["EditIn"])
    types["EditOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EditOut"])
    types["ApplicationReferenceIn"] = t.struct({"type": t.string().optional()}).named(
        renames["ApplicationReferenceIn"]
    )
    types["ApplicationReferenceOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationReferenceOut"])
    types["DriveFileIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DriveFileIn"]
    )
    types["DriveFileOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveFileOut"])
    types["UnknownUserIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UnknownUserIn"]
    )
    types["UnknownUserOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UnknownUserOut"])
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
            "knownUser": t.proxy(renames["KnownUserIn"]).optional(),
            "deletedUser": t.proxy(renames["DeletedUserIn"]).optional(),
            "unknownUser": t.proxy(renames["UnknownUserIn"]).optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "knownUser": t.proxy(renames["KnownUserOut"]).optional(),
            "deletedUser": t.proxy(renames["DeletedUserOut"]).optional(),
            "unknownUser": t.proxy(renames["UnknownUserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
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
    types["DeleteIn"] = t.struct({"type": t.string().optional()}).named(
        renames["DeleteIn"]
    )
    types["DeleteOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteOut"])
    types["TextListIn"] = t.struct(
        {"values": t.array(t.proxy(renames["TextIn"])).optional()}
    ).named(renames["TextListIn"])
    types["TextListOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["TextOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextListOut"])
    types["FileIn"] = t.struct({"_": t.string().optional()}).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FileOut"])
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
    types["PostIn"] = t.struct({"subtype": t.string().optional()}).named(
        renames["PostIn"]
    )
    types["PostOut"] = t.struct(
        {
            "subtype": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostOut"])
    types["ActionIn"] = t.struct(
        {
            "detail": t.proxy(renames["ActionDetailIn"]).optional(),
            "timestamp": t.string().optional(),
            "timeRange": t.proxy(renames["TimeRangeIn"]).optional(),
            "actor": t.proxy(renames["ActorIn"]).optional(),
            "target": t.proxy(renames["TargetIn"]).optional(),
        }
    ).named(renames["ActionIn"])
    types["ActionOut"] = t.struct(
        {
            "detail": t.proxy(renames["ActionDetailOut"]).optional(),
            "timestamp": t.string().optional(),
            "timeRange": t.proxy(renames["TimeRangeOut"]).optional(),
            "actor": t.proxy(renames["ActorOut"]).optional(),
            "target": t.proxy(renames["TargetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionOut"])
    types["DataLeakPreventionChangeIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["DataLeakPreventionChangeIn"])
    types["DataLeakPreventionChangeOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataLeakPreventionChangeOut"])
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
    types["ActorIn"] = t.struct(
        {
            "user": t.proxy(renames["UserIn"]).optional(),
            "administrator": t.proxy(renames["AdministratorIn"]).optional(),
            "system": t.proxy(renames["SystemEventIn"]).optional(),
            "impersonation": t.proxy(renames["ImpersonationIn"]).optional(),
            "anonymous": t.proxy(renames["AnonymousUserIn"]).optional(),
        }
    ).named(renames["ActorIn"])
    types["ActorOut"] = t.struct(
        {
            "user": t.proxy(renames["UserOut"]).optional(),
            "administrator": t.proxy(renames["AdministratorOut"]).optional(),
            "system": t.proxy(renames["SystemEventOut"]).optional(),
            "impersonation": t.proxy(renames["ImpersonationOut"]).optional(),
            "anonymous": t.proxy(renames["AnonymousUserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActorOut"])

    functions = {}
    functions["activityQuery"] = driveactivity.post(
        "v2/activity:query",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "itemName": t.string().optional(),
                "consolidationStrategy": t.proxy(
                    renames["ConsolidationStrategyIn"]
                ).optional(),
                "filter": t.string().optional(),
                "ancestorName": t.string().optional(),
                "pageToken": t.string().optional(),
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
