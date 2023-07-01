from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_classroom():
    classroom = HTTPRuntime("https://classroom.googleapis.com/")

    renames = {
        "ErrorResponse": "_classroom_1_ErrorResponse",
        "StudentIn": "_classroom_2_StudentIn",
        "StudentOut": "_classroom_3_StudentOut",
        "ListGuardiansResponseIn": "_classroom_4_ListGuardiansResponseIn",
        "ListGuardiansResponseOut": "_classroom_5_ListGuardiansResponseOut",
        "StudentSubmissionIn": "_classroom_6_StudentSubmissionIn",
        "StudentSubmissionOut": "_classroom_7_StudentSubmissionOut",
        "ShortAnswerSubmissionIn": "_classroom_8_ShortAnswerSubmissionIn",
        "ShortAnswerSubmissionOut": "_classroom_9_ShortAnswerSubmissionOut",
        "ListAnnouncementsResponseIn": "_classroom_10_ListAnnouncementsResponseIn",
        "ListAnnouncementsResponseOut": "_classroom_11_ListAnnouncementsResponseOut",
        "ListInvitationsResponseIn": "_classroom_12_ListInvitationsResponseIn",
        "ListInvitationsResponseOut": "_classroom_13_ListInvitationsResponseOut",
        "ModifyIndividualStudentsOptionsIn": "_classroom_14_ModifyIndividualStudentsOptionsIn",
        "ModifyIndividualStudentsOptionsOut": "_classroom_15_ModifyIndividualStudentsOptionsOut",
        "StateHistoryIn": "_classroom_16_StateHistoryIn",
        "StateHistoryOut": "_classroom_17_StateHistoryOut",
        "UserProfileIn": "_classroom_18_UserProfileIn",
        "UserProfileOut": "_classroom_19_UserProfileOut",
        "AssignmentIn": "_classroom_20_AssignmentIn",
        "AssignmentOut": "_classroom_21_AssignmentOut",
        "ListTopicResponseIn": "_classroom_22_ListTopicResponseIn",
        "ListTopicResponseOut": "_classroom_23_ListTopicResponseOut",
        "ListCourseWorkMaterialResponseIn": "_classroom_24_ListCourseWorkMaterialResponseIn",
        "ListCourseWorkMaterialResponseOut": "_classroom_25_ListCourseWorkMaterialResponseOut",
        "CourseWorkChangesInfoIn": "_classroom_26_CourseWorkChangesInfoIn",
        "CourseWorkChangesInfoOut": "_classroom_27_CourseWorkChangesInfoOut",
        "ListGuardianInvitationsResponseIn": "_classroom_28_ListGuardianInvitationsResponseIn",
        "ListGuardianInvitationsResponseOut": "_classroom_29_ListGuardianInvitationsResponseOut",
        "CourseAliasIn": "_classroom_30_CourseAliasIn",
        "CourseAliasOut": "_classroom_31_CourseAliasOut",
        "DateIn": "_classroom_32_DateIn",
        "DateOut": "_classroom_33_DateOut",
        "ListStudentsResponseIn": "_classroom_34_ListStudentsResponseIn",
        "ListStudentsResponseOut": "_classroom_35_ListStudentsResponseOut",
        "TurnInStudentSubmissionRequestIn": "_classroom_36_TurnInStudentSubmissionRequestIn",
        "TurnInStudentSubmissionRequestOut": "_classroom_37_TurnInStudentSubmissionRequestOut",
        "FeedIn": "_classroom_38_FeedIn",
        "FeedOut": "_classroom_39_FeedOut",
        "ListCourseAliasesResponseIn": "_classroom_40_ListCourseAliasesResponseIn",
        "ListCourseAliasesResponseOut": "_classroom_41_ListCourseAliasesResponseOut",
        "AttachmentIn": "_classroom_42_AttachmentIn",
        "AttachmentOut": "_classroom_43_AttachmentOut",
        "CourseIn": "_classroom_44_CourseIn",
        "CourseOut": "_classroom_45_CourseOut",
        "ModifyAnnouncementAssigneesRequestIn": "_classroom_46_ModifyAnnouncementAssigneesRequestIn",
        "ModifyAnnouncementAssigneesRequestOut": "_classroom_47_ModifyAnnouncementAssigneesRequestOut",
        "GradebookSettingsIn": "_classroom_48_GradebookSettingsIn",
        "GradebookSettingsOut": "_classroom_49_GradebookSettingsOut",
        "GuardianInvitationIn": "_classroom_50_GuardianInvitationIn",
        "GuardianInvitationOut": "_classroom_51_GuardianInvitationOut",
        "CourseMaterialIn": "_classroom_52_CourseMaterialIn",
        "CourseMaterialOut": "_classroom_53_CourseMaterialOut",
        "ReclaimStudentSubmissionRequestIn": "_classroom_54_ReclaimStudentSubmissionRequestIn",
        "ReclaimStudentSubmissionRequestOut": "_classroom_55_ReclaimStudentSubmissionRequestOut",
        "TeacherIn": "_classroom_56_TeacherIn",
        "TeacherOut": "_classroom_57_TeacherOut",
        "CloudPubsubTopicIn": "_classroom_58_CloudPubsubTopicIn",
        "CloudPubsubTopicOut": "_classroom_59_CloudPubsubTopicOut",
        "CourseMaterialSetIn": "_classroom_60_CourseMaterialSetIn",
        "CourseMaterialSetOut": "_classroom_61_CourseMaterialSetOut",
        "NameIn": "_classroom_62_NameIn",
        "NameOut": "_classroom_63_NameOut",
        "LinkIn": "_classroom_64_LinkIn",
        "LinkOut": "_classroom_65_LinkOut",
        "SubmissionHistoryIn": "_classroom_66_SubmissionHistoryIn",
        "SubmissionHistoryOut": "_classroom_67_SubmissionHistoryOut",
        "FormIn": "_classroom_68_FormIn",
        "FormOut": "_classroom_69_FormOut",
        "TopicIn": "_classroom_70_TopicIn",
        "TopicOut": "_classroom_71_TopicOut",
        "ListTeachersResponseIn": "_classroom_72_ListTeachersResponseIn",
        "ListTeachersResponseOut": "_classroom_73_ListTeachersResponseOut",
        "CourseRosterChangesInfoIn": "_classroom_74_CourseRosterChangesInfoIn",
        "CourseRosterChangesInfoOut": "_classroom_75_CourseRosterChangesInfoOut",
        "CourseWorkIn": "_classroom_76_CourseWorkIn",
        "CourseWorkOut": "_classroom_77_CourseWorkOut",
        "AssignmentSubmissionIn": "_classroom_78_AssignmentSubmissionIn",
        "AssignmentSubmissionOut": "_classroom_79_AssignmentSubmissionOut",
        "MaterialIn": "_classroom_80_MaterialIn",
        "MaterialOut": "_classroom_81_MaterialOut",
        "DriveFileIn": "_classroom_82_DriveFileIn",
        "DriveFileOut": "_classroom_83_DriveFileOut",
        "YouTubeVideoIn": "_classroom_84_YouTubeVideoIn",
        "YouTubeVideoOut": "_classroom_85_YouTubeVideoOut",
        "GlobalPermissionIn": "_classroom_86_GlobalPermissionIn",
        "GlobalPermissionOut": "_classroom_87_GlobalPermissionOut",
        "RegistrationIn": "_classroom_88_RegistrationIn",
        "RegistrationOut": "_classroom_89_RegistrationOut",
        "MultipleChoiceQuestionIn": "_classroom_90_MultipleChoiceQuestionIn",
        "MultipleChoiceQuestionOut": "_classroom_91_MultipleChoiceQuestionOut",
        "EmptyIn": "_classroom_92_EmptyIn",
        "EmptyOut": "_classroom_93_EmptyOut",
        "GradeHistoryIn": "_classroom_94_GradeHistoryIn",
        "GradeHistoryOut": "_classroom_95_GradeHistoryOut",
        "MultipleChoiceSubmissionIn": "_classroom_96_MultipleChoiceSubmissionIn",
        "MultipleChoiceSubmissionOut": "_classroom_97_MultipleChoiceSubmissionOut",
        "SharedDriveFileIn": "_classroom_98_SharedDriveFileIn",
        "SharedDriveFileOut": "_classroom_99_SharedDriveFileOut",
        "ReturnStudentSubmissionRequestIn": "_classroom_100_ReturnStudentSubmissionRequestIn",
        "ReturnStudentSubmissionRequestOut": "_classroom_101_ReturnStudentSubmissionRequestOut",
        "InvitationIn": "_classroom_102_InvitationIn",
        "InvitationOut": "_classroom_103_InvitationOut",
        "IndividualStudentsOptionsIn": "_classroom_104_IndividualStudentsOptionsIn",
        "IndividualStudentsOptionsOut": "_classroom_105_IndividualStudentsOptionsOut",
        "ListStudentSubmissionsResponseIn": "_classroom_106_ListStudentSubmissionsResponseIn",
        "ListStudentSubmissionsResponseOut": "_classroom_107_ListStudentSubmissionsResponseOut",
        "TimeOfDayIn": "_classroom_108_TimeOfDayIn",
        "TimeOfDayOut": "_classroom_109_TimeOfDayOut",
        "DriveFolderIn": "_classroom_110_DriveFolderIn",
        "DriveFolderOut": "_classroom_111_DriveFolderOut",
        "ListCoursesResponseIn": "_classroom_112_ListCoursesResponseIn",
        "ListCoursesResponseOut": "_classroom_113_ListCoursesResponseOut",
        "GradeCategoryIn": "_classroom_114_GradeCategoryIn",
        "GradeCategoryOut": "_classroom_115_GradeCategoryOut",
        "ModifyAttachmentsRequestIn": "_classroom_116_ModifyAttachmentsRequestIn",
        "ModifyAttachmentsRequestOut": "_classroom_117_ModifyAttachmentsRequestOut",
        "ListCourseWorkResponseIn": "_classroom_118_ListCourseWorkResponseIn",
        "ListCourseWorkResponseOut": "_classroom_119_ListCourseWorkResponseOut",
        "CourseWorkMaterialIn": "_classroom_120_CourseWorkMaterialIn",
        "CourseWorkMaterialOut": "_classroom_121_CourseWorkMaterialOut",
        "ModifyCourseWorkAssigneesRequestIn": "_classroom_122_ModifyCourseWorkAssigneesRequestIn",
        "ModifyCourseWorkAssigneesRequestOut": "_classroom_123_ModifyCourseWorkAssigneesRequestOut",
        "AnnouncementIn": "_classroom_124_AnnouncementIn",
        "AnnouncementOut": "_classroom_125_AnnouncementOut",
        "GuardianIn": "_classroom_126_GuardianIn",
        "GuardianOut": "_classroom_127_GuardianOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["StudentIn"] = t.struct(
        {
            "profile": t.proxy(renames["UserProfileIn"]).optional(),
            "courseId": t.string().optional(),
            "userId": t.string().optional(),
            "studentWorkFolder": t.proxy(renames["DriveFolderIn"]).optional(),
        }
    ).named(renames["StudentIn"])
    types["StudentOut"] = t.struct(
        {
            "profile": t.proxy(renames["UserProfileOut"]).optional(),
            "courseId": t.string().optional(),
            "userId": t.string().optional(),
            "studentWorkFolder": t.proxy(renames["DriveFolderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StudentOut"])
    types["ListGuardiansResponseIn"] = t.struct(
        {
            "guardians": t.array(t.proxy(renames["GuardianIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListGuardiansResponseIn"])
    types["ListGuardiansResponseOut"] = t.struct(
        {
            "guardians": t.array(t.proxy(renames["GuardianOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGuardiansResponseOut"])
    types["StudentSubmissionIn"] = t.struct(
        {
            "id": t.string().optional(),
            "creationTime": t.string().optional(),
            "late": t.boolean().optional(),
            "courseWorkId": t.string().optional(),
            "multipleChoiceSubmission": t.proxy(
                renames["MultipleChoiceSubmissionIn"]
            ).optional(),
            "shortAnswerSubmission": t.proxy(
                renames["ShortAnswerSubmissionIn"]
            ).optional(),
            "state": t.string().optional(),
            "courseId": t.string().optional(),
            "courseWorkType": t.string().optional(),
            "submissionHistory": t.array(
                t.proxy(renames["SubmissionHistoryIn"])
            ).optional(),
            "updateTime": t.string().optional(),
            "draftGrade": t.number().optional(),
            "associatedWithDeveloper": t.boolean().optional(),
            "assignmentSubmission": t.proxy(
                renames["AssignmentSubmissionIn"]
            ).optional(),
            "userId": t.string().optional(),
            "alternateLink": t.string().optional(),
            "assignedGrade": t.number().optional(),
        }
    ).named(renames["StudentSubmissionIn"])
    types["StudentSubmissionOut"] = t.struct(
        {
            "id": t.string().optional(),
            "creationTime": t.string().optional(),
            "late": t.boolean().optional(),
            "courseWorkId": t.string().optional(),
            "multipleChoiceSubmission": t.proxy(
                renames["MultipleChoiceSubmissionOut"]
            ).optional(),
            "shortAnswerSubmission": t.proxy(
                renames["ShortAnswerSubmissionOut"]
            ).optional(),
            "state": t.string().optional(),
            "courseId": t.string().optional(),
            "courseWorkType": t.string().optional(),
            "submissionHistory": t.array(
                t.proxy(renames["SubmissionHistoryOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "draftGrade": t.number().optional(),
            "associatedWithDeveloper": t.boolean().optional(),
            "assignmentSubmission": t.proxy(
                renames["AssignmentSubmissionOut"]
            ).optional(),
            "userId": t.string().optional(),
            "alternateLink": t.string().optional(),
            "assignedGrade": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StudentSubmissionOut"])
    types["ShortAnswerSubmissionIn"] = t.struct(
        {"answer": t.string().optional()}
    ).named(renames["ShortAnswerSubmissionIn"])
    types["ShortAnswerSubmissionOut"] = t.struct(
        {
            "answer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShortAnswerSubmissionOut"])
    types["ListAnnouncementsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "announcements": t.array(t.proxy(renames["AnnouncementIn"])).optional(),
        }
    ).named(renames["ListAnnouncementsResponseIn"])
    types["ListAnnouncementsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "announcements": t.array(t.proxy(renames["AnnouncementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAnnouncementsResponseOut"])
    types["ListInvitationsResponseIn"] = t.struct(
        {
            "invitations": t.array(t.proxy(renames["InvitationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListInvitationsResponseIn"])
    types["ListInvitationsResponseOut"] = t.struct(
        {
            "invitations": t.array(t.proxy(renames["InvitationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInvitationsResponseOut"])
    types["ModifyIndividualStudentsOptionsIn"] = t.struct(
        {
            "removeStudentIds": t.array(t.string()).optional(),
            "addStudentIds": t.array(t.string()).optional(),
        }
    ).named(renames["ModifyIndividualStudentsOptionsIn"])
    types["ModifyIndividualStudentsOptionsOut"] = t.struct(
        {
            "removeStudentIds": t.array(t.string()).optional(),
            "addStudentIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyIndividualStudentsOptionsOut"])
    types["StateHistoryIn"] = t.struct(
        {
            "actorUserId": t.string().optional(),
            "stateTimestamp": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["StateHistoryIn"])
    types["StateHistoryOut"] = t.struct(
        {
            "actorUserId": t.string().optional(),
            "stateTimestamp": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StateHistoryOut"])
    types["UserProfileIn"] = t.struct(
        {
            "permissions": t.array(t.proxy(renames["GlobalPermissionIn"])).optional(),
            "photoUrl": t.string().optional(),
            "name": t.proxy(renames["NameIn"]).optional(),
            "emailAddress": t.string().optional(),
            "verifiedTeacher": t.boolean().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["UserProfileIn"])
    types["UserProfileOut"] = t.struct(
        {
            "permissions": t.array(t.proxy(renames["GlobalPermissionOut"])).optional(),
            "photoUrl": t.string().optional(),
            "name": t.proxy(renames["NameOut"]).optional(),
            "emailAddress": t.string().optional(),
            "verifiedTeacher": t.boolean().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserProfileOut"])
    types["AssignmentIn"] = t.struct(
        {"studentWorkFolder": t.proxy(renames["DriveFolderIn"]).optional()}
    ).named(renames["AssignmentIn"])
    types["AssignmentOut"] = t.struct(
        {
            "studentWorkFolder": t.proxy(renames["DriveFolderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignmentOut"])
    types["ListTopicResponseIn"] = t.struct(
        {
            "topic": t.array(t.proxy(renames["TopicIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTopicResponseIn"])
    types["ListTopicResponseOut"] = t.struct(
        {
            "topic": t.array(t.proxy(renames["TopicOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTopicResponseOut"])
    types["ListCourseWorkMaterialResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "courseWorkMaterial": t.array(
                t.proxy(renames["CourseWorkMaterialIn"])
            ).optional(),
        }
    ).named(renames["ListCourseWorkMaterialResponseIn"])
    types["ListCourseWorkMaterialResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "courseWorkMaterial": t.array(
                t.proxy(renames["CourseWorkMaterialOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCourseWorkMaterialResponseOut"])
    types["CourseWorkChangesInfoIn"] = t.struct(
        {"courseId": t.string().optional()}
    ).named(renames["CourseWorkChangesInfoIn"])
    types["CourseWorkChangesInfoOut"] = t.struct(
        {
            "courseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CourseWorkChangesInfoOut"])
    types["ListGuardianInvitationsResponseIn"] = t.struct(
        {
            "guardianInvitations": t.array(
                t.proxy(renames["GuardianInvitationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListGuardianInvitationsResponseIn"])
    types["ListGuardianInvitationsResponseOut"] = t.struct(
        {
            "guardianInvitations": t.array(
                t.proxy(renames["GuardianInvitationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGuardianInvitationsResponseOut"])
    types["CourseAliasIn"] = t.struct({"alias": t.string().optional()}).named(
        renames["CourseAliasIn"]
    )
    types["CourseAliasOut"] = t.struct(
        {
            "alias": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CourseAliasOut"])
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["ListStudentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "students": t.array(t.proxy(renames["StudentIn"])).optional(),
        }
    ).named(renames["ListStudentsResponseIn"])
    types["ListStudentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "students": t.array(t.proxy(renames["StudentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListStudentsResponseOut"])
    types["TurnInStudentSubmissionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["TurnInStudentSubmissionRequestIn"])
    types["TurnInStudentSubmissionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TurnInStudentSubmissionRequestOut"])
    types["FeedIn"] = t.struct(
        {
            "courseWorkChangesInfo": t.proxy(
                renames["CourseWorkChangesInfoIn"]
            ).optional(),
            "courseRosterChangesInfo": t.proxy(
                renames["CourseRosterChangesInfoIn"]
            ).optional(),
            "feedType": t.string().optional(),
        }
    ).named(renames["FeedIn"])
    types["FeedOut"] = t.struct(
        {
            "courseWorkChangesInfo": t.proxy(
                renames["CourseWorkChangesInfoOut"]
            ).optional(),
            "courseRosterChangesInfo": t.proxy(
                renames["CourseRosterChangesInfoOut"]
            ).optional(),
            "feedType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeedOut"])
    types["ListCourseAliasesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "aliases": t.array(t.proxy(renames["CourseAliasIn"])).optional(),
        }
    ).named(renames["ListCourseAliasesResponseIn"])
    types["ListCourseAliasesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "aliases": t.array(t.proxy(renames["CourseAliasOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCourseAliasesResponseOut"])
    types["AttachmentIn"] = t.struct(
        {
            "youTubeVideo": t.proxy(renames["YouTubeVideoIn"]).optional(),
            "driveFile": t.proxy(renames["DriveFileIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "form": t.proxy(renames["FormIn"]).optional(),
        }
    ).named(renames["AttachmentIn"])
    types["AttachmentOut"] = t.struct(
        {
            "youTubeVideo": t.proxy(renames["YouTubeVideoOut"]).optional(),
            "driveFile": t.proxy(renames["DriveFileOut"]).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "form": t.proxy(renames["FormOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
    types["CourseIn"] = t.struct(
        {
            "gradebookSettings": t.proxy(renames["GradebookSettingsIn"]).optional(),
            "id": t.string().optional(),
            "alternateLink": t.string().optional(),
            "ownerId": t.string().optional(),
            "teacherFolder": t.proxy(renames["DriveFolderIn"]).optional(),
            "guardiansEnabled": t.boolean().optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "teacherGroupEmail": t.string().optional(),
            "name": t.string().optional(),
            "enrollmentCode": t.string().optional(),
            "section": t.string().optional(),
            "creationTime": t.string().optional(),
            "descriptionHeading": t.string().optional(),
            "room": t.string().optional(),
            "courseMaterialSets": t.array(
                t.proxy(renames["CourseMaterialSetIn"])
            ).optional(),
            "courseGroupEmail": t.string().optional(),
            "calendarId": t.string().optional(),
            "courseState": t.string().optional(),
        }
    ).named(renames["CourseIn"])
    types["CourseOut"] = t.struct(
        {
            "gradebookSettings": t.proxy(renames["GradebookSettingsOut"]).optional(),
            "id": t.string().optional(),
            "alternateLink": t.string().optional(),
            "ownerId": t.string().optional(),
            "teacherFolder": t.proxy(renames["DriveFolderOut"]).optional(),
            "guardiansEnabled": t.boolean().optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "teacherGroupEmail": t.string().optional(),
            "name": t.string().optional(),
            "enrollmentCode": t.string().optional(),
            "section": t.string().optional(),
            "creationTime": t.string().optional(),
            "descriptionHeading": t.string().optional(),
            "room": t.string().optional(),
            "courseMaterialSets": t.array(
                t.proxy(renames["CourseMaterialSetOut"])
            ).optional(),
            "courseGroupEmail": t.string().optional(),
            "calendarId": t.string().optional(),
            "courseState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CourseOut"])
    types["ModifyAnnouncementAssigneesRequestIn"] = t.struct(
        {
            "modifyIndividualStudentsOptions": t.proxy(
                renames["ModifyIndividualStudentsOptionsIn"]
            ).optional(),
            "assigneeMode": t.string().optional(),
        }
    ).named(renames["ModifyAnnouncementAssigneesRequestIn"])
    types["ModifyAnnouncementAssigneesRequestOut"] = t.struct(
        {
            "modifyIndividualStudentsOptions": t.proxy(
                renames["ModifyIndividualStudentsOptionsOut"]
            ).optional(),
            "assigneeMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyAnnouncementAssigneesRequestOut"])
    types["GradebookSettingsIn"] = t.struct(
        {
            "calculationType": t.string().optional(),
            "displaySetting": t.string().optional(),
            "gradeCategories": t.array(t.proxy(renames["GradeCategoryIn"])).optional(),
        }
    ).named(renames["GradebookSettingsIn"])
    types["GradebookSettingsOut"] = t.struct(
        {
            "calculationType": t.string().optional(),
            "displaySetting": t.string().optional(),
            "gradeCategories": t.array(t.proxy(renames["GradeCategoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GradebookSettingsOut"])
    types["GuardianInvitationIn"] = t.struct(
        {
            "invitationId": t.string().optional(),
            "creationTime": t.string().optional(),
            "invitedEmailAddress": t.string().optional(),
            "studentId": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GuardianInvitationIn"])
    types["GuardianInvitationOut"] = t.struct(
        {
            "invitationId": t.string().optional(),
            "creationTime": t.string().optional(),
            "invitedEmailAddress": t.string().optional(),
            "studentId": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuardianInvitationOut"])
    types["CourseMaterialIn"] = t.struct(
        {
            "driveFile": t.proxy(renames["DriveFileIn"]).optional(),
            "form": t.proxy(renames["FormIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "youTubeVideo": t.proxy(renames["YouTubeVideoIn"]).optional(),
        }
    ).named(renames["CourseMaterialIn"])
    types["CourseMaterialOut"] = t.struct(
        {
            "driveFile": t.proxy(renames["DriveFileOut"]).optional(),
            "form": t.proxy(renames["FormOut"]).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "youTubeVideo": t.proxy(renames["YouTubeVideoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CourseMaterialOut"])
    types["ReclaimStudentSubmissionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ReclaimStudentSubmissionRequestIn"])
    types["ReclaimStudentSubmissionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReclaimStudentSubmissionRequestOut"])
    types["TeacherIn"] = t.struct(
        {
            "userId": t.string().optional(),
            "profile": t.proxy(renames["UserProfileIn"]).optional(),
            "courseId": t.string().optional(),
        }
    ).named(renames["TeacherIn"])
    types["TeacherOut"] = t.struct(
        {
            "userId": t.string().optional(),
            "profile": t.proxy(renames["UserProfileOut"]).optional(),
            "courseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TeacherOut"])
    types["CloudPubsubTopicIn"] = t.struct({"topicName": t.string().optional()}).named(
        renames["CloudPubsubTopicIn"]
    )
    types["CloudPubsubTopicOut"] = t.struct(
        {
            "topicName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudPubsubTopicOut"])
    types["CourseMaterialSetIn"] = t.struct(
        {
            "materials": t.array(t.proxy(renames["CourseMaterialIn"])).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["CourseMaterialSetIn"])
    types["CourseMaterialSetOut"] = t.struct(
        {
            "materials": t.array(t.proxy(renames["CourseMaterialOut"])).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CourseMaterialSetOut"])
    types["NameIn"] = t.struct(
        {
            "familyName": t.string().optional(),
            "givenName": t.string().optional(),
            "fullName": t.string().optional(),
        }
    ).named(renames["NameIn"])
    types["NameOut"] = t.struct(
        {
            "familyName": t.string().optional(),
            "givenName": t.string().optional(),
            "fullName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NameOut"])
    types["LinkIn"] = t.struct(
        {
            "title": t.string().optional(),
            "url": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "title": t.string().optional(),
            "url": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["SubmissionHistoryIn"] = t.struct(
        {
            "gradeHistory": t.proxy(renames["GradeHistoryIn"]).optional(),
            "stateHistory": t.proxy(renames["StateHistoryIn"]).optional(),
        }
    ).named(renames["SubmissionHistoryIn"])
    types["SubmissionHistoryOut"] = t.struct(
        {
            "gradeHistory": t.proxy(renames["GradeHistoryOut"]).optional(),
            "stateHistory": t.proxy(renames["StateHistoryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubmissionHistoryOut"])
    types["FormIn"] = t.struct(
        {
            "responseUrl": t.string().optional(),
            "formUrl": t.string().optional(),
            "title": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
        }
    ).named(renames["FormIn"])
    types["FormOut"] = t.struct(
        {
            "responseUrl": t.string().optional(),
            "formUrl": t.string().optional(),
            "title": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormOut"])
    types["TopicIn"] = t.struct(
        {
            "topicId": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "courseId": t.string().optional(),
        }
    ).named(renames["TopicIn"])
    types["TopicOut"] = t.struct(
        {
            "topicId": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "courseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicOut"])
    types["ListTeachersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "teachers": t.array(t.proxy(renames["TeacherIn"])).optional(),
        }
    ).named(renames["ListTeachersResponseIn"])
    types["ListTeachersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "teachers": t.array(t.proxy(renames["TeacherOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTeachersResponseOut"])
    types["CourseRosterChangesInfoIn"] = t.struct(
        {"courseId": t.string().optional()}
    ).named(renames["CourseRosterChangesInfoIn"])
    types["CourseRosterChangesInfoOut"] = t.struct(
        {
            "courseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CourseRosterChangesInfoOut"])
    types["CourseWorkIn"] = t.struct(
        {
            "courseId": t.string().optional(),
            "dueTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "title": t.string().optional(),
            "topicId": t.string().optional(),
            "scheduledTime": t.string().optional(),
            "alternateLink": t.string().optional(),
            "state": t.string().optional(),
            "multipleChoiceQuestion": t.proxy(
                renames["MultipleChoiceQuestionIn"]
            ).optional(),
            "gradeCategory": t.proxy(renames["GradeCategoryIn"]).optional(),
            "dueDate": t.proxy(renames["DateIn"]).optional(),
            "individualStudentsOptions": t.proxy(
                renames["IndividualStudentsOptionsIn"]
            ).optional(),
            "materials": t.array(t.proxy(renames["MaterialIn"])).optional(),
            "associatedWithDeveloper": t.boolean().optional(),
            "workType": t.string().optional(),
            "submissionModificationMode": t.string().optional(),
            "maxPoints": t.number().optional(),
            "creationTime": t.string().optional(),
            "creatorUserId": t.string().optional(),
            "updateTime": t.string().optional(),
            "id": t.string().optional(),
            "assigneeMode": t.string().optional(),
            "description": t.string().optional(),
            "assignment": t.proxy(renames["AssignmentIn"]).optional(),
        }
    ).named(renames["CourseWorkIn"])
    types["CourseWorkOut"] = t.struct(
        {
            "courseId": t.string().optional(),
            "dueTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "title": t.string().optional(),
            "topicId": t.string().optional(),
            "scheduledTime": t.string().optional(),
            "alternateLink": t.string().optional(),
            "state": t.string().optional(),
            "multipleChoiceQuestion": t.proxy(
                renames["MultipleChoiceQuestionOut"]
            ).optional(),
            "gradeCategory": t.proxy(renames["GradeCategoryOut"]).optional(),
            "dueDate": t.proxy(renames["DateOut"]).optional(),
            "individualStudentsOptions": t.proxy(
                renames["IndividualStudentsOptionsOut"]
            ).optional(),
            "materials": t.array(t.proxy(renames["MaterialOut"])).optional(),
            "associatedWithDeveloper": t.boolean().optional(),
            "workType": t.string().optional(),
            "submissionModificationMode": t.string().optional(),
            "maxPoints": t.number().optional(),
            "creationTime": t.string().optional(),
            "creatorUserId": t.string().optional(),
            "updateTime": t.string().optional(),
            "id": t.string().optional(),
            "assigneeMode": t.string().optional(),
            "description": t.string().optional(),
            "assignment": t.proxy(renames["AssignmentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CourseWorkOut"])
    types["AssignmentSubmissionIn"] = t.struct(
        {"attachments": t.array(t.proxy(renames["AttachmentIn"])).optional()}
    ).named(renames["AssignmentSubmissionIn"])
    types["AssignmentSubmissionOut"] = t.struct(
        {
            "attachments": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignmentSubmissionOut"])
    types["MaterialIn"] = t.struct(
        {
            "youtubeVideo": t.proxy(renames["YouTubeVideoIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "form": t.proxy(renames["FormIn"]).optional(),
            "driveFile": t.proxy(renames["SharedDriveFileIn"]).optional(),
        }
    ).named(renames["MaterialIn"])
    types["MaterialOut"] = t.struct(
        {
            "youtubeVideo": t.proxy(renames["YouTubeVideoOut"]).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "form": t.proxy(renames["FormOut"]).optional(),
            "driveFile": t.proxy(renames["SharedDriveFileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaterialOut"])
    types["DriveFileIn"] = t.struct(
        {
            "title": t.string().optional(),
            "id": t.string().optional(),
            "alternateLink": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
        }
    ).named(renames["DriveFileIn"])
    types["DriveFileOut"] = t.struct(
        {
            "title": t.string().optional(),
            "id": t.string().optional(),
            "alternateLink": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveFileOut"])
    types["YouTubeVideoIn"] = t.struct(
        {
            "title": t.string().optional(),
            "id": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "alternateLink": t.string().optional(),
        }
    ).named(renames["YouTubeVideoIn"])
    types["YouTubeVideoOut"] = t.struct(
        {
            "title": t.string().optional(),
            "id": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "alternateLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YouTubeVideoOut"])
    types["GlobalPermissionIn"] = t.struct({"permission": t.string().optional()}).named(
        renames["GlobalPermissionIn"]
    )
    types["GlobalPermissionOut"] = t.struct(
        {
            "permission": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlobalPermissionOut"])
    types["RegistrationIn"] = t.struct(
        {
            "cloudPubsubTopic": t.proxy(renames["CloudPubsubTopicIn"]).optional(),
            "expiryTime": t.string().optional(),
            "registrationId": t.string().optional(),
            "feed": t.proxy(renames["FeedIn"]).optional(),
        }
    ).named(renames["RegistrationIn"])
    types["RegistrationOut"] = t.struct(
        {
            "cloudPubsubTopic": t.proxy(renames["CloudPubsubTopicOut"]).optional(),
            "expiryTime": t.string().optional(),
            "registrationId": t.string().optional(),
            "feed": t.proxy(renames["FeedOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegistrationOut"])
    types["MultipleChoiceQuestionIn"] = t.struct(
        {"choices": t.array(t.string()).optional()}
    ).named(renames["MultipleChoiceQuestionIn"])
    types["MultipleChoiceQuestionOut"] = t.struct(
        {
            "choices": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultipleChoiceQuestionOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GradeHistoryIn"] = t.struct(
        {
            "actorUserId": t.string().optional(),
            "maxPoints": t.number().optional(),
            "gradeTimestamp": t.string().optional(),
            "gradeChangeType": t.string().optional(),
            "pointsEarned": t.number().optional(),
        }
    ).named(renames["GradeHistoryIn"])
    types["GradeHistoryOut"] = t.struct(
        {
            "actorUserId": t.string().optional(),
            "maxPoints": t.number().optional(),
            "gradeTimestamp": t.string().optional(),
            "gradeChangeType": t.string().optional(),
            "pointsEarned": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GradeHistoryOut"])
    types["MultipleChoiceSubmissionIn"] = t.struct(
        {"answer": t.string().optional()}
    ).named(renames["MultipleChoiceSubmissionIn"])
    types["MultipleChoiceSubmissionOut"] = t.struct(
        {
            "answer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultipleChoiceSubmissionOut"])
    types["SharedDriveFileIn"] = t.struct(
        {
            "shareMode": t.string().optional(),
            "driveFile": t.proxy(renames["DriveFileIn"]).optional(),
        }
    ).named(renames["SharedDriveFileIn"])
    types["SharedDriveFileOut"] = t.struct(
        {
            "shareMode": t.string().optional(),
            "driveFile": t.proxy(renames["DriveFileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SharedDriveFileOut"])
    types["ReturnStudentSubmissionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ReturnStudentSubmissionRequestIn"])
    types["ReturnStudentSubmissionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReturnStudentSubmissionRequestOut"])
    types["InvitationIn"] = t.struct(
        {
            "courseId": t.string().optional(),
            "userId": t.string().optional(),
            "role": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["InvitationIn"])
    types["InvitationOut"] = t.struct(
        {
            "courseId": t.string().optional(),
            "userId": t.string().optional(),
            "role": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvitationOut"])
    types["IndividualStudentsOptionsIn"] = t.struct(
        {"studentIds": t.array(t.string()).optional()}
    ).named(renames["IndividualStudentsOptionsIn"])
    types["IndividualStudentsOptionsOut"] = t.struct(
        {
            "studentIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndividualStudentsOptionsOut"])
    types["ListStudentSubmissionsResponseIn"] = t.struct(
        {
            "studentSubmissions": t.array(
                t.proxy(renames["StudentSubmissionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListStudentSubmissionsResponseIn"])
    types["ListStudentSubmissionsResponseOut"] = t.struct(
        {
            "studentSubmissions": t.array(
                t.proxy(renames["StudentSubmissionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListStudentSubmissionsResponseOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["DriveFolderIn"] = t.struct(
        {
            "id": t.string().optional(),
            "alternateLink": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["DriveFolderIn"])
    types["DriveFolderOut"] = t.struct(
        {
            "id": t.string().optional(),
            "alternateLink": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveFolderOut"])
    types["ListCoursesResponseIn"] = t.struct(
        {
            "courses": t.array(t.proxy(renames["CourseIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCoursesResponseIn"])
    types["ListCoursesResponseOut"] = t.struct(
        {
            "courses": t.array(t.proxy(renames["CourseOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCoursesResponseOut"])
    types["GradeCategoryIn"] = t.struct(
        {
            "name": t.string().optional(),
            "defaultGradeDenominator": t.integer().optional(),
            "weight": t.integer().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["GradeCategoryIn"])
    types["GradeCategoryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "defaultGradeDenominator": t.integer().optional(),
            "weight": t.integer().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GradeCategoryOut"])
    types["ModifyAttachmentsRequestIn"] = t.struct(
        {"addAttachments": t.array(t.proxy(renames["AttachmentIn"])).optional()}
    ).named(renames["ModifyAttachmentsRequestIn"])
    types["ModifyAttachmentsRequestOut"] = t.struct(
        {
            "addAttachments": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyAttachmentsRequestOut"])
    types["ListCourseWorkResponseIn"] = t.struct(
        {
            "courseWork": t.array(t.proxy(renames["CourseWorkIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCourseWorkResponseIn"])
    types["ListCourseWorkResponseOut"] = t.struct(
        {
            "courseWork": t.array(t.proxy(renames["CourseWorkOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCourseWorkResponseOut"])
    types["CourseWorkMaterialIn"] = t.struct(
        {
            "creatorUserId": t.string().optional(),
            "title": t.string().optional(),
            "topicId": t.string().optional(),
            "description": t.string().optional(),
            "assigneeMode": t.string().optional(),
            "materials": t.array(t.proxy(renames["MaterialIn"])).optional(),
            "individualStudentsOptions": t.proxy(
                renames["IndividualStudentsOptionsIn"]
            ).optional(),
            "id": t.string().optional(),
            "scheduledTime": t.string().optional(),
            "alternateLink": t.string().optional(),
            "updateTime": t.string().optional(),
            "creationTime": t.string().optional(),
            "state": t.string().optional(),
            "courseId": t.string().optional(),
        }
    ).named(renames["CourseWorkMaterialIn"])
    types["CourseWorkMaterialOut"] = t.struct(
        {
            "creatorUserId": t.string().optional(),
            "title": t.string().optional(),
            "topicId": t.string().optional(),
            "description": t.string().optional(),
            "assigneeMode": t.string().optional(),
            "materials": t.array(t.proxy(renames["MaterialOut"])).optional(),
            "individualStudentsOptions": t.proxy(
                renames["IndividualStudentsOptionsOut"]
            ).optional(),
            "id": t.string().optional(),
            "scheduledTime": t.string().optional(),
            "alternateLink": t.string().optional(),
            "updateTime": t.string().optional(),
            "creationTime": t.string().optional(),
            "state": t.string().optional(),
            "courseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CourseWorkMaterialOut"])
    types["ModifyCourseWorkAssigneesRequestIn"] = t.struct(
        {
            "assigneeMode": t.string().optional(),
            "modifyIndividualStudentsOptions": t.proxy(
                renames["ModifyIndividualStudentsOptionsIn"]
            ).optional(),
        }
    ).named(renames["ModifyCourseWorkAssigneesRequestIn"])
    types["ModifyCourseWorkAssigneesRequestOut"] = t.struct(
        {
            "assigneeMode": t.string().optional(),
            "modifyIndividualStudentsOptions": t.proxy(
                renames["ModifyIndividualStudentsOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyCourseWorkAssigneesRequestOut"])
    types["AnnouncementIn"] = t.struct(
        {
            "state": t.string().optional(),
            "text": t.string().optional(),
            "scheduledTime": t.string().optional(),
            "alternateLink": t.string().optional(),
            "materials": t.array(t.proxy(renames["MaterialIn"])).optional(),
            "creationTime": t.string().optional(),
            "individualStudentsOptions": t.proxy(
                renames["IndividualStudentsOptionsIn"]
            ).optional(),
            "updateTime": t.string().optional(),
            "id": t.string().optional(),
            "courseId": t.string().optional(),
            "assigneeMode": t.string().optional(),
            "creatorUserId": t.string().optional(),
        }
    ).named(renames["AnnouncementIn"])
    types["AnnouncementOut"] = t.struct(
        {
            "state": t.string().optional(),
            "text": t.string().optional(),
            "scheduledTime": t.string().optional(),
            "alternateLink": t.string().optional(),
            "materials": t.array(t.proxy(renames["MaterialOut"])).optional(),
            "creationTime": t.string().optional(),
            "individualStudentsOptions": t.proxy(
                renames["IndividualStudentsOptionsOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "id": t.string().optional(),
            "courseId": t.string().optional(),
            "assigneeMode": t.string().optional(),
            "creatorUserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnouncementOut"])
    types["GuardianIn"] = t.struct(
        {
            "guardianId": t.string().optional(),
            "guardianProfile": t.proxy(renames["UserProfileIn"]).optional(),
            "invitedEmailAddress": t.string().optional(),
            "studentId": t.string().optional(),
        }
    ).named(renames["GuardianIn"])
    types["GuardianOut"] = t.struct(
        {
            "guardianId": t.string().optional(),
            "guardianProfile": t.proxy(renames["UserProfileOut"]).optional(),
            "invitedEmailAddress": t.string().optional(),
            "studentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuardianOut"])

    functions = {}
    functions["userProfilesGet"] = classroom.get(
        "v1/userProfiles/{userId}",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["UserProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesGuardianInvitationsCreate"] = classroom.get(
        "v1/userProfiles/{studentId}/guardianInvitations/{invitationId}",
        t.struct(
            {
                "invitationId": t.string().optional(),
                "studentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GuardianInvitationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesGuardianInvitationsPatch"] = classroom.get(
        "v1/userProfiles/{studentId}/guardianInvitations/{invitationId}",
        t.struct(
            {
                "invitationId": t.string().optional(),
                "studentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GuardianInvitationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesGuardianInvitationsList"] = classroom.get(
        "v1/userProfiles/{studentId}/guardianInvitations/{invitationId}",
        t.struct(
            {
                "invitationId": t.string().optional(),
                "studentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GuardianInvitationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesGuardianInvitationsGet"] = classroom.get(
        "v1/userProfiles/{studentId}/guardianInvitations/{invitationId}",
        t.struct(
            {
                "invitationId": t.string().optional(),
                "studentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GuardianInvitationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesGuardiansGet"] = classroom.get(
        "v1/userProfiles/{studentId}/guardians",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "invitedEmailAddress": t.string().optional(),
                "pageSize": t.integer().optional(),
                "studentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGuardiansResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesGuardiansDelete"] = classroom.get(
        "v1/userProfiles/{studentId}/guardians",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "invitedEmailAddress": t.string().optional(),
                "pageSize": t.integer().optional(),
                "studentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGuardiansResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesGuardiansList"] = classroom.get(
        "v1/userProfiles/{studentId}/guardians",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "invitedEmailAddress": t.string().optional(),
                "pageSize": t.integer().optional(),
                "studentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGuardiansResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["registrationsCreate"] = classroom.delete(
        "v1/registrations/{registrationId}",
        t.struct(
            {"registrationId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["registrationsDelete"] = classroom.delete(
        "v1/registrations/{registrationId}",
        t.struct(
            {"registrationId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCreate"] = classroom.put(
        "v1/courses/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "gradebookSettings": t.proxy(renames["GradebookSettingsIn"]).optional(),
                "alternateLink": t.string().optional(),
                "ownerId": t.string().optional(),
                "teacherFolder": t.proxy(renames["DriveFolderIn"]).optional(),
                "guardiansEnabled": t.boolean().optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "teacherGroupEmail": t.string().optional(),
                "name": t.string().optional(),
                "enrollmentCode": t.string().optional(),
                "section": t.string().optional(),
                "creationTime": t.string().optional(),
                "descriptionHeading": t.string().optional(),
                "room": t.string().optional(),
                "courseMaterialSets": t.array(
                    t.proxy(renames["CourseMaterialSetIn"])
                ).optional(),
                "courseGroupEmail": t.string().optional(),
                "calendarId": t.string().optional(),
                "courseState": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesPatch"] = classroom.put(
        "v1/courses/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "gradebookSettings": t.proxy(renames["GradebookSettingsIn"]).optional(),
                "alternateLink": t.string().optional(),
                "ownerId": t.string().optional(),
                "teacherFolder": t.proxy(renames["DriveFolderIn"]).optional(),
                "guardiansEnabled": t.boolean().optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "teacherGroupEmail": t.string().optional(),
                "name": t.string().optional(),
                "enrollmentCode": t.string().optional(),
                "section": t.string().optional(),
                "creationTime": t.string().optional(),
                "descriptionHeading": t.string().optional(),
                "room": t.string().optional(),
                "courseMaterialSets": t.array(
                    t.proxy(renames["CourseMaterialSetIn"])
                ).optional(),
                "courseGroupEmail": t.string().optional(),
                "calendarId": t.string().optional(),
                "courseState": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesDelete"] = classroom.put(
        "v1/courses/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "gradebookSettings": t.proxy(renames["GradebookSettingsIn"]).optional(),
                "alternateLink": t.string().optional(),
                "ownerId": t.string().optional(),
                "teacherFolder": t.proxy(renames["DriveFolderIn"]).optional(),
                "guardiansEnabled": t.boolean().optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "teacherGroupEmail": t.string().optional(),
                "name": t.string().optional(),
                "enrollmentCode": t.string().optional(),
                "section": t.string().optional(),
                "creationTime": t.string().optional(),
                "descriptionHeading": t.string().optional(),
                "room": t.string().optional(),
                "courseMaterialSets": t.array(
                    t.proxy(renames["CourseMaterialSetIn"])
                ).optional(),
                "courseGroupEmail": t.string().optional(),
                "calendarId": t.string().optional(),
                "courseState": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesList"] = classroom.put(
        "v1/courses/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "gradebookSettings": t.proxy(renames["GradebookSettingsIn"]).optional(),
                "alternateLink": t.string().optional(),
                "ownerId": t.string().optional(),
                "teacherFolder": t.proxy(renames["DriveFolderIn"]).optional(),
                "guardiansEnabled": t.boolean().optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "teacherGroupEmail": t.string().optional(),
                "name": t.string().optional(),
                "enrollmentCode": t.string().optional(),
                "section": t.string().optional(),
                "creationTime": t.string().optional(),
                "descriptionHeading": t.string().optional(),
                "room": t.string().optional(),
                "courseMaterialSets": t.array(
                    t.proxy(renames["CourseMaterialSetIn"])
                ).optional(),
                "courseGroupEmail": t.string().optional(),
                "calendarId": t.string().optional(),
                "courseState": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesGet"] = classroom.put(
        "v1/courses/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "gradebookSettings": t.proxy(renames["GradebookSettingsIn"]).optional(),
                "alternateLink": t.string().optional(),
                "ownerId": t.string().optional(),
                "teacherFolder": t.proxy(renames["DriveFolderIn"]).optional(),
                "guardiansEnabled": t.boolean().optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "teacherGroupEmail": t.string().optional(),
                "name": t.string().optional(),
                "enrollmentCode": t.string().optional(),
                "section": t.string().optional(),
                "creationTime": t.string().optional(),
                "descriptionHeading": t.string().optional(),
                "room": t.string().optional(),
                "courseMaterialSets": t.array(
                    t.proxy(renames["CourseMaterialSetIn"])
                ).optional(),
                "courseGroupEmail": t.string().optional(),
                "calendarId": t.string().optional(),
                "courseState": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesUpdate"] = classroom.put(
        "v1/courses/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "gradebookSettings": t.proxy(renames["GradebookSettingsIn"]).optional(),
                "alternateLink": t.string().optional(),
                "ownerId": t.string().optional(),
                "teacherFolder": t.proxy(renames["DriveFolderIn"]).optional(),
                "guardiansEnabled": t.boolean().optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "teacherGroupEmail": t.string().optional(),
                "name": t.string().optional(),
                "enrollmentCode": t.string().optional(),
                "section": t.string().optional(),
                "creationTime": t.string().optional(),
                "descriptionHeading": t.string().optional(),
                "room": t.string().optional(),
                "courseMaterialSets": t.array(
                    t.proxy(renames["CourseMaterialSetIn"])
                ).optional(),
                "courseGroupEmail": t.string().optional(),
                "calendarId": t.string().optional(),
                "courseState": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesTopicsPatch"] = classroom.get(
        "v1/courses/{courseId}/topics",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "courseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTopicResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesTopicsDelete"] = classroom.get(
        "v1/courses/{courseId}/topics",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "courseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTopicResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesTopicsGet"] = classroom.get(
        "v1/courses/{courseId}/topics",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "courseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTopicResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesTopicsCreate"] = classroom.get(
        "v1/courses/{courseId}/topics",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "courseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTopicResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesTopicsList"] = classroom.get(
        "v1/courses/{courseId}/topics",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "courseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTopicResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesTeachersCreate"] = classroom.delete(
        "v1/courses/{courseId}/teachers/{userId}",
        t.struct(
            {
                "courseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesTeachersList"] = classroom.delete(
        "v1/courses/{courseId}/teachers/{userId}",
        t.struct(
            {
                "courseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesTeachersGet"] = classroom.delete(
        "v1/courses/{courseId}/teachers/{userId}",
        t.struct(
            {
                "courseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesTeachersDelete"] = classroom.delete(
        "v1/courses/{courseId}/teachers/{userId}",
        t.struct(
            {
                "courseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesAliasesDelete"] = classroom.post(
        "v1/courses/{courseId}/aliases",
        t.struct(
            {
                "courseId": t.string().optional(),
                "alias": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseAliasOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesAliasesList"] = classroom.post(
        "v1/courses/{courseId}/aliases",
        t.struct(
            {
                "courseId": t.string().optional(),
                "alias": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseAliasOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesAliasesCreate"] = classroom.post(
        "v1/courses/{courseId}/aliases",
        t.struct(
            {
                "courseId": t.string().optional(),
                "alias": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseAliasOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesAnnouncementsGet"] = classroom.get(
        "v1/courses/{courseId}/announcements",
        t.struct(
            {
                "courseId": t.string().optional(),
                "orderBy": t.string().optional(),
                "announcementStates": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAnnouncementsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesAnnouncementsModifyAssignees"] = classroom.get(
        "v1/courses/{courseId}/announcements",
        t.struct(
            {
                "courseId": t.string().optional(),
                "orderBy": t.string().optional(),
                "announcementStates": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAnnouncementsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesAnnouncementsDelete"] = classroom.get(
        "v1/courses/{courseId}/announcements",
        t.struct(
            {
                "courseId": t.string().optional(),
                "orderBy": t.string().optional(),
                "announcementStates": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAnnouncementsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesAnnouncementsPatch"] = classroom.get(
        "v1/courses/{courseId}/announcements",
        t.struct(
            {
                "courseId": t.string().optional(),
                "orderBy": t.string().optional(),
                "announcementStates": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAnnouncementsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesAnnouncementsCreate"] = classroom.get(
        "v1/courses/{courseId}/announcements",
        t.struct(
            {
                "courseId": t.string().optional(),
                "orderBy": t.string().optional(),
                "announcementStates": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAnnouncementsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesAnnouncementsList"] = classroom.get(
        "v1/courses/{courseId}/announcements",
        t.struct(
            {
                "courseId": t.string().optional(),
                "orderBy": t.string().optional(),
                "announcementStates": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAnnouncementsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkMaterialsGet"] = classroom.patch(
        "v1/courses/{courseId}/courseWorkMaterials/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "updateMask": t.string().optional(),
                "courseId": t.string().optional(),
                "creatorUserId": t.string().optional(),
                "title": t.string().optional(),
                "topicId": t.string().optional(),
                "description": t.string().optional(),
                "assigneeMode": t.string().optional(),
                "materials": t.array(t.proxy(renames["MaterialIn"])).optional(),
                "individualStudentsOptions": t.proxy(
                    renames["IndividualStudentsOptionsIn"]
                ).optional(),
                "scheduledTime": t.string().optional(),
                "alternateLink": t.string().optional(),
                "updateTime": t.string().optional(),
                "creationTime": t.string().optional(),
                "state": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseWorkMaterialOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkMaterialsDelete"] = classroom.patch(
        "v1/courses/{courseId}/courseWorkMaterials/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "updateMask": t.string().optional(),
                "courseId": t.string().optional(),
                "creatorUserId": t.string().optional(),
                "title": t.string().optional(),
                "topicId": t.string().optional(),
                "description": t.string().optional(),
                "assigneeMode": t.string().optional(),
                "materials": t.array(t.proxy(renames["MaterialIn"])).optional(),
                "individualStudentsOptions": t.proxy(
                    renames["IndividualStudentsOptionsIn"]
                ).optional(),
                "scheduledTime": t.string().optional(),
                "alternateLink": t.string().optional(),
                "updateTime": t.string().optional(),
                "creationTime": t.string().optional(),
                "state": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseWorkMaterialOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkMaterialsList"] = classroom.patch(
        "v1/courses/{courseId}/courseWorkMaterials/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "updateMask": t.string().optional(),
                "courseId": t.string().optional(),
                "creatorUserId": t.string().optional(),
                "title": t.string().optional(),
                "topicId": t.string().optional(),
                "description": t.string().optional(),
                "assigneeMode": t.string().optional(),
                "materials": t.array(t.proxy(renames["MaterialIn"])).optional(),
                "individualStudentsOptions": t.proxy(
                    renames["IndividualStudentsOptionsIn"]
                ).optional(),
                "scheduledTime": t.string().optional(),
                "alternateLink": t.string().optional(),
                "updateTime": t.string().optional(),
                "creationTime": t.string().optional(),
                "state": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseWorkMaterialOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkMaterialsCreate"] = classroom.patch(
        "v1/courses/{courseId}/courseWorkMaterials/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "updateMask": t.string().optional(),
                "courseId": t.string().optional(),
                "creatorUserId": t.string().optional(),
                "title": t.string().optional(),
                "topicId": t.string().optional(),
                "description": t.string().optional(),
                "assigneeMode": t.string().optional(),
                "materials": t.array(t.proxy(renames["MaterialIn"])).optional(),
                "individualStudentsOptions": t.proxy(
                    renames["IndividualStudentsOptionsIn"]
                ).optional(),
                "scheduledTime": t.string().optional(),
                "alternateLink": t.string().optional(),
                "updateTime": t.string().optional(),
                "creationTime": t.string().optional(),
                "state": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseWorkMaterialOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkMaterialsPatch"] = classroom.patch(
        "v1/courses/{courseId}/courseWorkMaterials/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "updateMask": t.string().optional(),
                "courseId": t.string().optional(),
                "creatorUserId": t.string().optional(),
                "title": t.string().optional(),
                "topicId": t.string().optional(),
                "description": t.string().optional(),
                "assigneeMode": t.string().optional(),
                "materials": t.array(t.proxy(renames["MaterialIn"])).optional(),
                "individualStudentsOptions": t.proxy(
                    renames["IndividualStudentsOptionsIn"]
                ).optional(),
                "scheduledTime": t.string().optional(),
                "alternateLink": t.string().optional(),
                "updateTime": t.string().optional(),
                "creationTime": t.string().optional(),
                "state": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseWorkMaterialOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkGet"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{id}:modifyAssignees",
        t.struct(
            {
                "id": t.string().optional(),
                "courseId": t.string().optional(),
                "assigneeMode": t.string().optional(),
                "modifyIndividualStudentsOptions": t.proxy(
                    renames["ModifyIndividualStudentsOptionsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseWorkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkPatch"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{id}:modifyAssignees",
        t.struct(
            {
                "id": t.string().optional(),
                "courseId": t.string().optional(),
                "assigneeMode": t.string().optional(),
                "modifyIndividualStudentsOptions": t.proxy(
                    renames["ModifyIndividualStudentsOptionsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseWorkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkList"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{id}:modifyAssignees",
        t.struct(
            {
                "id": t.string().optional(),
                "courseId": t.string().optional(),
                "assigneeMode": t.string().optional(),
                "modifyIndividualStudentsOptions": t.proxy(
                    renames["ModifyIndividualStudentsOptionsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseWorkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkCreate"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{id}:modifyAssignees",
        t.struct(
            {
                "id": t.string().optional(),
                "courseId": t.string().optional(),
                "assigneeMode": t.string().optional(),
                "modifyIndividualStudentsOptions": t.proxy(
                    renames["ModifyIndividualStudentsOptionsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseWorkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkDelete"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{id}:modifyAssignees",
        t.struct(
            {
                "id": t.string().optional(),
                "courseId": t.string().optional(),
                "assigneeMode": t.string().optional(),
                "modifyIndividualStudentsOptions": t.proxy(
                    renames["ModifyIndividualStudentsOptionsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseWorkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkModifyAssignees"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{id}:modifyAssignees",
        t.struct(
            {
                "id": t.string().optional(),
                "courseId": t.string().optional(),
                "assigneeMode": t.string().optional(),
                "modifyIndividualStudentsOptions": t.proxy(
                    renames["ModifyIndividualStudentsOptionsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseWorkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkStudentSubmissionsReclaim"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{courseWorkId}/studentSubmissions/{id}:modifyAttachments",
        t.struct(
            {
                "courseWorkId": t.string().optional(),
                "courseId": t.string().optional(),
                "id": t.string().optional(),
                "addAttachments": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StudentSubmissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkStudentSubmissionsPatch"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{courseWorkId}/studentSubmissions/{id}:modifyAttachments",
        t.struct(
            {
                "courseWorkId": t.string().optional(),
                "courseId": t.string().optional(),
                "id": t.string().optional(),
                "addAttachments": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StudentSubmissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkStudentSubmissionsGet"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{courseWorkId}/studentSubmissions/{id}:modifyAttachments",
        t.struct(
            {
                "courseWorkId": t.string().optional(),
                "courseId": t.string().optional(),
                "id": t.string().optional(),
                "addAttachments": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StudentSubmissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkStudentSubmissionsList"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{courseWorkId}/studentSubmissions/{id}:modifyAttachments",
        t.struct(
            {
                "courseWorkId": t.string().optional(),
                "courseId": t.string().optional(),
                "id": t.string().optional(),
                "addAttachments": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StudentSubmissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkStudentSubmissionsReturn"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{courseWorkId}/studentSubmissions/{id}:modifyAttachments",
        t.struct(
            {
                "courseWorkId": t.string().optional(),
                "courseId": t.string().optional(),
                "id": t.string().optional(),
                "addAttachments": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StudentSubmissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkStudentSubmissionsTurnIn"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{courseWorkId}/studentSubmissions/{id}:modifyAttachments",
        t.struct(
            {
                "courseWorkId": t.string().optional(),
                "courseId": t.string().optional(),
                "id": t.string().optional(),
                "addAttachments": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StudentSubmissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkStudentSubmissionsModifyAttachments"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{courseWorkId}/studentSubmissions/{id}:modifyAttachments",
        t.struct(
            {
                "courseWorkId": t.string().optional(),
                "courseId": t.string().optional(),
                "id": t.string().optional(),
                "addAttachments": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StudentSubmissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesStudentsList"] = classroom.get(
        "v1/courses/{courseId}/students/{userId}",
        t.struct(
            {
                "courseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StudentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesStudentsCreate"] = classroom.get(
        "v1/courses/{courseId}/students/{userId}",
        t.struct(
            {
                "courseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StudentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesStudentsDelete"] = classroom.get(
        "v1/courses/{courseId}/students/{userId}",
        t.struct(
            {
                "courseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StudentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesStudentsGet"] = classroom.get(
        "v1/courses/{courseId}/students/{userId}",
        t.struct(
            {
                "courseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StudentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["invitationsGet"] = classroom.get(
        "v1/invitations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "courseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["invitationsAccept"] = classroom.get(
        "v1/invitations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "courseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["invitationsCreate"] = classroom.get(
        "v1/invitations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "courseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["invitationsDelete"] = classroom.get(
        "v1/invitations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "courseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["invitationsList"] = classroom.get(
        "v1/invitations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "courseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="classroom",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
