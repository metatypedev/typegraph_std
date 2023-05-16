from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_classroom() -> Import:
    classroom = HTTPRuntime("https://classroom.googleapis.com/")

    renames = {
        "ErrorResponse": "_classroom_1_ErrorResponse",
        "RegistrationIn": "_classroom_2_RegistrationIn",
        "RegistrationOut": "_classroom_3_RegistrationOut",
        "EmptyIn": "_classroom_4_EmptyIn",
        "EmptyOut": "_classroom_5_EmptyOut",
        "FormIn": "_classroom_6_FormIn",
        "FormOut": "_classroom_7_FormOut",
        "TurnInStudentSubmissionRequestIn": "_classroom_8_TurnInStudentSubmissionRequestIn",
        "TurnInStudentSubmissionRequestOut": "_classroom_9_TurnInStudentSubmissionRequestOut",
        "AttachmentIn": "_classroom_10_AttachmentIn",
        "AttachmentOut": "_classroom_11_AttachmentOut",
        "GuardianIn": "_classroom_12_GuardianIn",
        "GuardianOut": "_classroom_13_GuardianOut",
        "CourseWorkChangesInfoIn": "_classroom_14_CourseWorkChangesInfoIn",
        "CourseWorkChangesInfoOut": "_classroom_15_CourseWorkChangesInfoOut",
        "ListCourseAliasesResponseIn": "_classroom_16_ListCourseAliasesResponseIn",
        "ListCourseAliasesResponseOut": "_classroom_17_ListCourseAliasesResponseOut",
        "ListStudentSubmissionsResponseIn": "_classroom_18_ListStudentSubmissionsResponseIn",
        "ListStudentSubmissionsResponseOut": "_classroom_19_ListStudentSubmissionsResponseOut",
        "ListGuardiansResponseIn": "_classroom_20_ListGuardiansResponseIn",
        "ListGuardiansResponseOut": "_classroom_21_ListGuardiansResponseOut",
        "TopicIn": "_classroom_22_TopicIn",
        "TopicOut": "_classroom_23_TopicOut",
        "YouTubeVideoIn": "_classroom_24_YouTubeVideoIn",
        "YouTubeVideoOut": "_classroom_25_YouTubeVideoOut",
        "MultipleChoiceQuestionIn": "_classroom_26_MultipleChoiceQuestionIn",
        "MultipleChoiceQuestionOut": "_classroom_27_MultipleChoiceQuestionOut",
        "ListCoursesResponseIn": "_classroom_28_ListCoursesResponseIn",
        "ListCoursesResponseOut": "_classroom_29_ListCoursesResponseOut",
        "ModifyCourseWorkAssigneesRequestIn": "_classroom_30_ModifyCourseWorkAssigneesRequestIn",
        "ModifyCourseWorkAssigneesRequestOut": "_classroom_31_ModifyCourseWorkAssigneesRequestOut",
        "MultipleChoiceSubmissionIn": "_classroom_32_MultipleChoiceSubmissionIn",
        "MultipleChoiceSubmissionOut": "_classroom_33_MultipleChoiceSubmissionOut",
        "ReturnStudentSubmissionRequestIn": "_classroom_34_ReturnStudentSubmissionRequestIn",
        "ReturnStudentSubmissionRequestOut": "_classroom_35_ReturnStudentSubmissionRequestOut",
        "GradebookSettingsIn": "_classroom_36_GradebookSettingsIn",
        "GradebookSettingsOut": "_classroom_37_GradebookSettingsOut",
        "ListTopicResponseIn": "_classroom_38_ListTopicResponseIn",
        "ListTopicResponseOut": "_classroom_39_ListTopicResponseOut",
        "GlobalPermissionIn": "_classroom_40_GlobalPermissionIn",
        "GlobalPermissionOut": "_classroom_41_GlobalPermissionOut",
        "FeedIn": "_classroom_42_FeedIn",
        "FeedOut": "_classroom_43_FeedOut",
        "InvitationIn": "_classroom_44_InvitationIn",
        "InvitationOut": "_classroom_45_InvitationOut",
        "CloudPubsubTopicIn": "_classroom_46_CloudPubsubTopicIn",
        "CloudPubsubTopicOut": "_classroom_47_CloudPubsubTopicOut",
        "IndividualStudentsOptionsIn": "_classroom_48_IndividualStudentsOptionsIn",
        "IndividualStudentsOptionsOut": "_classroom_49_IndividualStudentsOptionsOut",
        "CourseAliasIn": "_classroom_50_CourseAliasIn",
        "CourseAliasOut": "_classroom_51_CourseAliasOut",
        "StudentIn": "_classroom_52_StudentIn",
        "StudentOut": "_classroom_53_StudentOut",
        "DateIn": "_classroom_54_DateIn",
        "DateOut": "_classroom_55_DateOut",
        "CourseWorkIn": "_classroom_56_CourseWorkIn",
        "CourseWorkOut": "_classroom_57_CourseWorkOut",
        "AssignmentSubmissionIn": "_classroom_58_AssignmentSubmissionIn",
        "AssignmentSubmissionOut": "_classroom_59_AssignmentSubmissionOut",
        "ShortAnswerSubmissionIn": "_classroom_60_ShortAnswerSubmissionIn",
        "ShortAnswerSubmissionOut": "_classroom_61_ShortAnswerSubmissionOut",
        "SharedDriveFileIn": "_classroom_62_SharedDriveFileIn",
        "SharedDriveFileOut": "_classroom_63_SharedDriveFileOut",
        "ListStudentsResponseIn": "_classroom_64_ListStudentsResponseIn",
        "ListStudentsResponseOut": "_classroom_65_ListStudentsResponseOut",
        "CourseWorkMaterialIn": "_classroom_66_CourseWorkMaterialIn",
        "CourseWorkMaterialOut": "_classroom_67_CourseWorkMaterialOut",
        "ListGuardianInvitationsResponseIn": "_classroom_68_ListGuardianInvitationsResponseIn",
        "ListGuardianInvitationsResponseOut": "_classroom_69_ListGuardianInvitationsResponseOut",
        "DriveFolderIn": "_classroom_70_DriveFolderIn",
        "DriveFolderOut": "_classroom_71_DriveFolderOut",
        "TeacherIn": "_classroom_72_TeacherIn",
        "TeacherOut": "_classroom_73_TeacherOut",
        "ListCourseWorkMaterialResponseIn": "_classroom_74_ListCourseWorkMaterialResponseIn",
        "ListCourseWorkMaterialResponseOut": "_classroom_75_ListCourseWorkMaterialResponseOut",
        "ModifyIndividualStudentsOptionsIn": "_classroom_76_ModifyIndividualStudentsOptionsIn",
        "ModifyIndividualStudentsOptionsOut": "_classroom_77_ModifyIndividualStudentsOptionsOut",
        "AnnouncementIn": "_classroom_78_AnnouncementIn",
        "AnnouncementOut": "_classroom_79_AnnouncementOut",
        "TimeOfDayIn": "_classroom_80_TimeOfDayIn",
        "TimeOfDayOut": "_classroom_81_TimeOfDayOut",
        "ModifyAnnouncementAssigneesRequestIn": "_classroom_82_ModifyAnnouncementAssigneesRequestIn",
        "ModifyAnnouncementAssigneesRequestOut": "_classroom_83_ModifyAnnouncementAssigneesRequestOut",
        "CourseIn": "_classroom_84_CourseIn",
        "CourseOut": "_classroom_85_CourseOut",
        "CourseRosterChangesInfoIn": "_classroom_86_CourseRosterChangesInfoIn",
        "CourseRosterChangesInfoOut": "_classroom_87_CourseRosterChangesInfoOut",
        "ModifyAttachmentsRequestIn": "_classroom_88_ModifyAttachmentsRequestIn",
        "ModifyAttachmentsRequestOut": "_classroom_89_ModifyAttachmentsRequestOut",
        "LinkIn": "_classroom_90_LinkIn",
        "LinkOut": "_classroom_91_LinkOut",
        "GradeCategoryIn": "_classroom_92_GradeCategoryIn",
        "GradeCategoryOut": "_classroom_93_GradeCategoryOut",
        "ListCourseWorkResponseIn": "_classroom_94_ListCourseWorkResponseIn",
        "ListCourseWorkResponseOut": "_classroom_95_ListCourseWorkResponseOut",
        "AssignmentIn": "_classroom_96_AssignmentIn",
        "AssignmentOut": "_classroom_97_AssignmentOut",
        "ReclaimStudentSubmissionRequestIn": "_classroom_98_ReclaimStudentSubmissionRequestIn",
        "ReclaimStudentSubmissionRequestOut": "_classroom_99_ReclaimStudentSubmissionRequestOut",
        "NameIn": "_classroom_100_NameIn",
        "NameOut": "_classroom_101_NameOut",
        "CourseMaterialIn": "_classroom_102_CourseMaterialIn",
        "CourseMaterialOut": "_classroom_103_CourseMaterialOut",
        "StateHistoryIn": "_classroom_104_StateHistoryIn",
        "StateHistoryOut": "_classroom_105_StateHistoryOut",
        "ListInvitationsResponseIn": "_classroom_106_ListInvitationsResponseIn",
        "ListInvitationsResponseOut": "_classroom_107_ListInvitationsResponseOut",
        "MaterialIn": "_classroom_108_MaterialIn",
        "MaterialOut": "_classroom_109_MaterialOut",
        "SubmissionHistoryIn": "_classroom_110_SubmissionHistoryIn",
        "SubmissionHistoryOut": "_classroom_111_SubmissionHistoryOut",
        "ListTeachersResponseIn": "_classroom_112_ListTeachersResponseIn",
        "ListTeachersResponseOut": "_classroom_113_ListTeachersResponseOut",
        "GradeHistoryIn": "_classroom_114_GradeHistoryIn",
        "GradeHistoryOut": "_classroom_115_GradeHistoryOut",
        "ListAnnouncementsResponseIn": "_classroom_116_ListAnnouncementsResponseIn",
        "ListAnnouncementsResponseOut": "_classroom_117_ListAnnouncementsResponseOut",
        "StudentSubmissionIn": "_classroom_118_StudentSubmissionIn",
        "StudentSubmissionOut": "_classroom_119_StudentSubmissionOut",
        "UserProfileIn": "_classroom_120_UserProfileIn",
        "UserProfileOut": "_classroom_121_UserProfileOut",
        "GuardianInvitationIn": "_classroom_122_GuardianInvitationIn",
        "GuardianInvitationOut": "_classroom_123_GuardianInvitationOut",
        "CourseMaterialSetIn": "_classroom_124_CourseMaterialSetIn",
        "CourseMaterialSetOut": "_classroom_125_CourseMaterialSetOut",
        "DriveFileIn": "_classroom_126_DriveFileIn",
        "DriveFileOut": "_classroom_127_DriveFileOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RegistrationIn"] = t.struct(
        {
            "registrationId": t.string().optional(),
            "expiryTime": t.string().optional(),
            "cloudPubsubTopic": t.proxy(renames["CloudPubsubTopicIn"]).optional(),
            "feed": t.proxy(renames["FeedIn"]).optional(),
        }
    ).named(renames["RegistrationIn"])
    types["RegistrationOut"] = t.struct(
        {
            "registrationId": t.string().optional(),
            "expiryTime": t.string().optional(),
            "cloudPubsubTopic": t.proxy(renames["CloudPubsubTopicOut"]).optional(),
            "feed": t.proxy(renames["FeedOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegistrationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["FormIn"] = t.struct(
        {
            "responseUrl": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "title": t.string().optional(),
            "formUrl": t.string().optional(),
        }
    ).named(renames["FormIn"])
    types["FormOut"] = t.struct(
        {
            "responseUrl": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "title": t.string().optional(),
            "formUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormOut"])
    types["TurnInStudentSubmissionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["TurnInStudentSubmissionRequestIn"])
    types["TurnInStudentSubmissionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TurnInStudentSubmissionRequestOut"])
    types["AttachmentIn"] = t.struct(
        {
            "driveFile": t.proxy(renames["DriveFileIn"]).optional(),
            "youTubeVideo": t.proxy(renames["YouTubeVideoIn"]).optional(),
            "form": t.proxy(renames["FormIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
        }
    ).named(renames["AttachmentIn"])
    types["AttachmentOut"] = t.struct(
        {
            "driveFile": t.proxy(renames["DriveFileOut"]).optional(),
            "youTubeVideo": t.proxy(renames["YouTubeVideoOut"]).optional(),
            "form": t.proxy(renames["FormOut"]).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
    types["GuardianIn"] = t.struct(
        {
            "guardianProfile": t.proxy(renames["UserProfileIn"]).optional(),
            "guardianId": t.string().optional(),
            "studentId": t.string().optional(),
            "invitedEmailAddress": t.string().optional(),
        }
    ).named(renames["GuardianIn"])
    types["GuardianOut"] = t.struct(
        {
            "guardianProfile": t.proxy(renames["UserProfileOut"]).optional(),
            "guardianId": t.string().optional(),
            "studentId": t.string().optional(),
            "invitedEmailAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuardianOut"])
    types["CourseWorkChangesInfoIn"] = t.struct(
        {"courseId": t.string().optional()}
    ).named(renames["CourseWorkChangesInfoIn"])
    types["CourseWorkChangesInfoOut"] = t.struct(
        {
            "courseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CourseWorkChangesInfoOut"])
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
    types["ListStudentSubmissionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "studentSubmissions": t.array(
                t.proxy(renames["StudentSubmissionIn"])
            ).optional(),
        }
    ).named(renames["ListStudentSubmissionsResponseIn"])
    types["ListStudentSubmissionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "studentSubmissions": t.array(
                t.proxy(renames["StudentSubmissionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListStudentSubmissionsResponseOut"])
    types["ListGuardiansResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "guardians": t.array(t.proxy(renames["GuardianIn"])).optional(),
        }
    ).named(renames["ListGuardiansResponseIn"])
    types["ListGuardiansResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "guardians": t.array(t.proxy(renames["GuardianOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGuardiansResponseOut"])
    types["TopicIn"] = t.struct(
        {
            "topicId": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "courseId": t.string().optional(),
        }
    ).named(renames["TopicIn"])
    types["TopicOut"] = t.struct(
        {
            "topicId": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "courseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicOut"])
    types["YouTubeVideoIn"] = t.struct(
        {
            "id": t.string().optional(),
            "alternateLink": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["YouTubeVideoIn"])
    types["YouTubeVideoOut"] = t.struct(
        {
            "id": t.string().optional(),
            "alternateLink": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YouTubeVideoOut"])
    types["MultipleChoiceQuestionIn"] = t.struct(
        {"choices": t.array(t.string()).optional()}
    ).named(renames["MultipleChoiceQuestionIn"])
    types["MultipleChoiceQuestionOut"] = t.struct(
        {
            "choices": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultipleChoiceQuestionOut"])
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
    types["ModifyCourseWorkAssigneesRequestIn"] = t.struct(
        {
            "modifyIndividualStudentsOptions": t.proxy(
                renames["ModifyIndividualStudentsOptionsIn"]
            ).optional(),
            "assigneeMode": t.string().optional(),
        }
    ).named(renames["ModifyCourseWorkAssigneesRequestIn"])
    types["ModifyCourseWorkAssigneesRequestOut"] = t.struct(
        {
            "modifyIndividualStudentsOptions": t.proxy(
                renames["ModifyIndividualStudentsOptionsOut"]
            ).optional(),
            "assigneeMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyCourseWorkAssigneesRequestOut"])
    types["MultipleChoiceSubmissionIn"] = t.struct(
        {"answer": t.string().optional()}
    ).named(renames["MultipleChoiceSubmissionIn"])
    types["MultipleChoiceSubmissionOut"] = t.struct(
        {
            "answer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultipleChoiceSubmissionOut"])
    types["ReturnStudentSubmissionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ReturnStudentSubmissionRequestIn"])
    types["ReturnStudentSubmissionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReturnStudentSubmissionRequestOut"])
    types["GradebookSettingsIn"] = t.struct(
        {
            "displaySetting": t.string().optional(),
            "calculationType": t.string().optional(),
            "gradeCategories": t.array(t.proxy(renames["GradeCategoryIn"])).optional(),
        }
    ).named(renames["GradebookSettingsIn"])
    types["GradebookSettingsOut"] = t.struct(
        {
            "displaySetting": t.string().optional(),
            "calculationType": t.string().optional(),
            "gradeCategories": t.array(t.proxy(renames["GradeCategoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GradebookSettingsOut"])
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
    types["GlobalPermissionIn"] = t.struct({"permission": t.string().optional()}).named(
        renames["GlobalPermissionIn"]
    )
    types["GlobalPermissionOut"] = t.struct(
        {
            "permission": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlobalPermissionOut"])
    types["FeedIn"] = t.struct(
        {
            "feedType": t.string().optional(),
            "courseRosterChangesInfo": t.proxy(
                renames["CourseRosterChangesInfoIn"]
            ).optional(),
            "courseWorkChangesInfo": t.proxy(
                renames["CourseWorkChangesInfoIn"]
            ).optional(),
        }
    ).named(renames["FeedIn"])
    types["FeedOut"] = t.struct(
        {
            "feedType": t.string().optional(),
            "courseRosterChangesInfo": t.proxy(
                renames["CourseRosterChangesInfoOut"]
            ).optional(),
            "courseWorkChangesInfo": t.proxy(
                renames["CourseWorkChangesInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeedOut"])
    types["InvitationIn"] = t.struct(
        {
            "courseId": t.string().optional(),
            "userId": t.string().optional(),
            "id": t.string().optional(),
            "role": t.string().optional(),
        }
    ).named(renames["InvitationIn"])
    types["InvitationOut"] = t.struct(
        {
            "courseId": t.string().optional(),
            "userId": t.string().optional(),
            "id": t.string().optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvitationOut"])
    types["CloudPubsubTopicIn"] = t.struct({"topicName": t.string().optional()}).named(
        renames["CloudPubsubTopicIn"]
    )
    types["CloudPubsubTopicOut"] = t.struct(
        {
            "topicName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudPubsubTopicOut"])
    types["IndividualStudentsOptionsIn"] = t.struct(
        {"studentIds": t.array(t.string()).optional()}
    ).named(renames["IndividualStudentsOptionsIn"])
    types["IndividualStudentsOptionsOut"] = t.struct(
        {
            "studentIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndividualStudentsOptionsOut"])
    types["CourseAliasIn"] = t.struct({"alias": t.string().optional()}).named(
        renames["CourseAliasIn"]
    )
    types["CourseAliasOut"] = t.struct(
        {
            "alias": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CourseAliasOut"])
    types["StudentIn"] = t.struct(
        {
            "profile": t.proxy(renames["UserProfileIn"]).optional(),
            "userId": t.string().optional(),
            "courseId": t.string().optional(),
            "studentWorkFolder": t.proxy(renames["DriveFolderIn"]).optional(),
        }
    ).named(renames["StudentIn"])
    types["StudentOut"] = t.struct(
        {
            "profile": t.proxy(renames["UserProfileOut"]).optional(),
            "userId": t.string().optional(),
            "courseId": t.string().optional(),
            "studentWorkFolder": t.proxy(renames["DriveFolderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StudentOut"])
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["CourseWorkIn"] = t.struct(
        {
            "assignment": t.proxy(renames["AssignmentIn"]).optional(),
            "courseId": t.string().optional(),
            "individualStudentsOptions": t.proxy(
                renames["IndividualStudentsOptionsIn"]
            ).optional(),
            "workType": t.string().optional(),
            "gradeCategory": t.proxy(renames["GradeCategoryIn"]).optional(),
            "creationTime": t.string().optional(),
            "submissionModificationMode": t.string().optional(),
            "dueTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "updateTime": t.string().optional(),
            "id": t.string().optional(),
            "description": t.string().optional(),
            "associatedWithDeveloper": t.boolean().optional(),
            "maxPoints": t.number().optional(),
            "state": t.string().optional(),
            "assigneeMode": t.string().optional(),
            "alternateLink": t.string().optional(),
            "scheduledTime": t.string().optional(),
            "materials": t.array(t.proxy(renames["MaterialIn"])).optional(),
            "creatorUserId": t.string().optional(),
            "dueDate": t.proxy(renames["DateIn"]).optional(),
            "title": t.string().optional(),
            "multipleChoiceQuestion": t.proxy(
                renames["MultipleChoiceQuestionIn"]
            ).optional(),
            "topicId": t.string().optional(),
        }
    ).named(renames["CourseWorkIn"])
    types["CourseWorkOut"] = t.struct(
        {
            "assignment": t.proxy(renames["AssignmentOut"]).optional(),
            "courseId": t.string().optional(),
            "individualStudentsOptions": t.proxy(
                renames["IndividualStudentsOptionsOut"]
            ).optional(),
            "workType": t.string().optional(),
            "gradeCategory": t.proxy(renames["GradeCategoryOut"]).optional(),
            "creationTime": t.string().optional(),
            "submissionModificationMode": t.string().optional(),
            "dueTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "updateTime": t.string().optional(),
            "id": t.string().optional(),
            "description": t.string().optional(),
            "associatedWithDeveloper": t.boolean().optional(),
            "maxPoints": t.number().optional(),
            "state": t.string().optional(),
            "assigneeMode": t.string().optional(),
            "alternateLink": t.string().optional(),
            "scheduledTime": t.string().optional(),
            "materials": t.array(t.proxy(renames["MaterialOut"])).optional(),
            "creatorUserId": t.string().optional(),
            "dueDate": t.proxy(renames["DateOut"]).optional(),
            "title": t.string().optional(),
            "multipleChoiceQuestion": t.proxy(
                renames["MultipleChoiceQuestionOut"]
            ).optional(),
            "topicId": t.string().optional(),
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
    types["ShortAnswerSubmissionIn"] = t.struct(
        {"answer": t.string().optional()}
    ).named(renames["ShortAnswerSubmissionIn"])
    types["ShortAnswerSubmissionOut"] = t.struct(
        {
            "answer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShortAnswerSubmissionOut"])
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
    types["CourseWorkMaterialIn"] = t.struct(
        {
            "description": t.string().optional(),
            "id": t.string().optional(),
            "state": t.string().optional(),
            "creationTime": t.string().optional(),
            "individualStudentsOptions": t.proxy(
                renames["IndividualStudentsOptionsIn"]
            ).optional(),
            "title": t.string().optional(),
            "scheduledTime": t.string().optional(),
            "creatorUserId": t.string().optional(),
            "updateTime": t.string().optional(),
            "materials": t.array(t.proxy(renames["MaterialIn"])).optional(),
            "assigneeMode": t.string().optional(),
            "alternateLink": t.string().optional(),
            "courseId": t.string().optional(),
            "topicId": t.string().optional(),
        }
    ).named(renames["CourseWorkMaterialIn"])
    types["CourseWorkMaterialOut"] = t.struct(
        {
            "description": t.string().optional(),
            "id": t.string().optional(),
            "state": t.string().optional(),
            "creationTime": t.string().optional(),
            "individualStudentsOptions": t.proxy(
                renames["IndividualStudentsOptionsOut"]
            ).optional(),
            "title": t.string().optional(),
            "scheduledTime": t.string().optional(),
            "creatorUserId": t.string().optional(),
            "updateTime": t.string().optional(),
            "materials": t.array(t.proxy(renames["MaterialOut"])).optional(),
            "assigneeMode": t.string().optional(),
            "alternateLink": t.string().optional(),
            "courseId": t.string().optional(),
            "topicId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CourseWorkMaterialOut"])
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
    types["TeacherIn"] = t.struct(
        {
            "profile": t.proxy(renames["UserProfileIn"]).optional(),
            "courseId": t.string().optional(),
            "userId": t.string().optional(),
        }
    ).named(renames["TeacherIn"])
    types["TeacherOut"] = t.struct(
        {
            "profile": t.proxy(renames["UserProfileOut"]).optional(),
            "courseId": t.string().optional(),
            "userId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TeacherOut"])
    types["ListCourseWorkMaterialResponseIn"] = t.struct(
        {
            "courseWorkMaterial": t.array(
                t.proxy(renames["CourseWorkMaterialIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCourseWorkMaterialResponseIn"])
    types["ListCourseWorkMaterialResponseOut"] = t.struct(
        {
            "courseWorkMaterial": t.array(
                t.proxy(renames["CourseWorkMaterialOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCourseWorkMaterialResponseOut"])
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
    types["AnnouncementIn"] = t.struct(
        {
            "alternateLink": t.string().optional(),
            "state": t.string().optional(),
            "assigneeMode": t.string().optional(),
            "updateTime": t.string().optional(),
            "scheduledTime": t.string().optional(),
            "courseId": t.string().optional(),
            "individualStudentsOptions": t.proxy(
                renames["IndividualStudentsOptionsIn"]
            ).optional(),
            "creationTime": t.string().optional(),
            "text": t.string().optional(),
            "id": t.string().optional(),
            "materials": t.array(t.proxy(renames["MaterialIn"])).optional(),
            "creatorUserId": t.string().optional(),
        }
    ).named(renames["AnnouncementIn"])
    types["AnnouncementOut"] = t.struct(
        {
            "alternateLink": t.string().optional(),
            "state": t.string().optional(),
            "assigneeMode": t.string().optional(),
            "updateTime": t.string().optional(),
            "scheduledTime": t.string().optional(),
            "courseId": t.string().optional(),
            "individualStudentsOptions": t.proxy(
                renames["IndividualStudentsOptionsOut"]
            ).optional(),
            "creationTime": t.string().optional(),
            "text": t.string().optional(),
            "id": t.string().optional(),
            "materials": t.array(t.proxy(renames["MaterialOut"])).optional(),
            "creatorUserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnouncementOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
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
    types["CourseIn"] = t.struct(
        {
            "teacherGroupEmail": t.string().optional(),
            "guardiansEnabled": t.boolean().optional(),
            "ownerId": t.string().optional(),
            "alternateLink": t.string().optional(),
            "id": t.string().optional(),
            "section": t.string().optional(),
            "calendarId": t.string().optional(),
            "courseState": t.string().optional(),
            "creationTime": t.string().optional(),
            "descriptionHeading": t.string().optional(),
            "room": t.string().optional(),
            "name": t.string().optional(),
            "teacherFolder": t.proxy(renames["DriveFolderIn"]).optional(),
            "enrollmentCode": t.string().optional(),
            "description": t.string().optional(),
            "courseGroupEmail": t.string().optional(),
            "gradebookSettings": t.proxy(renames["GradebookSettingsIn"]).optional(),
            "updateTime": t.string().optional(),
            "courseMaterialSets": t.array(
                t.proxy(renames["CourseMaterialSetIn"])
            ).optional(),
        }
    ).named(renames["CourseIn"])
    types["CourseOut"] = t.struct(
        {
            "teacherGroupEmail": t.string().optional(),
            "guardiansEnabled": t.boolean().optional(),
            "ownerId": t.string().optional(),
            "alternateLink": t.string().optional(),
            "id": t.string().optional(),
            "section": t.string().optional(),
            "calendarId": t.string().optional(),
            "courseState": t.string().optional(),
            "creationTime": t.string().optional(),
            "descriptionHeading": t.string().optional(),
            "room": t.string().optional(),
            "name": t.string().optional(),
            "teacherFolder": t.proxy(renames["DriveFolderOut"]).optional(),
            "enrollmentCode": t.string().optional(),
            "description": t.string().optional(),
            "courseGroupEmail": t.string().optional(),
            "gradebookSettings": t.proxy(renames["GradebookSettingsOut"]).optional(),
            "updateTime": t.string().optional(),
            "courseMaterialSets": t.array(
                t.proxy(renames["CourseMaterialSetOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CourseOut"])
    types["CourseRosterChangesInfoIn"] = t.struct(
        {"courseId": t.string().optional()}
    ).named(renames["CourseRosterChangesInfoIn"])
    types["CourseRosterChangesInfoOut"] = t.struct(
        {
            "courseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CourseRosterChangesInfoOut"])
    types["ModifyAttachmentsRequestIn"] = t.struct(
        {"addAttachments": t.array(t.proxy(renames["AttachmentIn"])).optional()}
    ).named(renames["ModifyAttachmentsRequestIn"])
    types["ModifyAttachmentsRequestOut"] = t.struct(
        {
            "addAttachments": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyAttachmentsRequestOut"])
    types["LinkIn"] = t.struct(
        {
            "title": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "title": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["GradeCategoryIn"] = t.struct(
        {
            "id": t.string().optional(),
            "defaultGradeDenominator": t.integer().optional(),
            "name": t.string().optional(),
            "weight": t.integer().optional(),
        }
    ).named(renames["GradeCategoryIn"])
    types["GradeCategoryOut"] = t.struct(
        {
            "id": t.string().optional(),
            "defaultGradeDenominator": t.integer().optional(),
            "name": t.string().optional(),
            "weight": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GradeCategoryOut"])
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
    types["AssignmentIn"] = t.struct(
        {"studentWorkFolder": t.proxy(renames["DriveFolderIn"]).optional()}
    ).named(renames["AssignmentIn"])
    types["AssignmentOut"] = t.struct(
        {
            "studentWorkFolder": t.proxy(renames["DriveFolderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignmentOut"])
    types["ReclaimStudentSubmissionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ReclaimStudentSubmissionRequestIn"])
    types["ReclaimStudentSubmissionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReclaimStudentSubmissionRequestOut"])
    types["NameIn"] = t.struct(
        {
            "givenName": t.string().optional(),
            "familyName": t.string().optional(),
            "fullName": t.string().optional(),
        }
    ).named(renames["NameIn"])
    types["NameOut"] = t.struct(
        {
            "givenName": t.string().optional(),
            "familyName": t.string().optional(),
            "fullName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NameOut"])
    types["CourseMaterialIn"] = t.struct(
        {
            "form": t.proxy(renames["FormIn"]).optional(),
            "driveFile": t.proxy(renames["DriveFileIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "youTubeVideo": t.proxy(renames["YouTubeVideoIn"]).optional(),
        }
    ).named(renames["CourseMaterialIn"])
    types["CourseMaterialOut"] = t.struct(
        {
            "form": t.proxy(renames["FormOut"]).optional(),
            "driveFile": t.proxy(renames["DriveFileOut"]).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "youTubeVideo": t.proxy(renames["YouTubeVideoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CourseMaterialOut"])
    types["StateHistoryIn"] = t.struct(
        {
            "stateTimestamp": t.string().optional(),
            "state": t.string().optional(),
            "actorUserId": t.string().optional(),
        }
    ).named(renames["StateHistoryIn"])
    types["StateHistoryOut"] = t.struct(
        {
            "stateTimestamp": t.string().optional(),
            "state": t.string().optional(),
            "actorUserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StateHistoryOut"])
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
    types["MaterialIn"] = t.struct(
        {
            "driveFile": t.proxy(renames["SharedDriveFileIn"]).optional(),
            "form": t.proxy(renames["FormIn"]).optional(),
            "link": t.proxy(renames["LinkIn"]).optional(),
            "youtubeVideo": t.proxy(renames["YouTubeVideoIn"]).optional(),
        }
    ).named(renames["MaterialIn"])
    types["MaterialOut"] = t.struct(
        {
            "driveFile": t.proxy(renames["SharedDriveFileOut"]).optional(),
            "form": t.proxy(renames["FormOut"]).optional(),
            "link": t.proxy(renames["LinkOut"]).optional(),
            "youtubeVideo": t.proxy(renames["YouTubeVideoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaterialOut"])
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
    types["ListTeachersResponseIn"] = t.struct(
        {
            "teachers": t.array(t.proxy(renames["TeacherIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTeachersResponseIn"])
    types["ListTeachersResponseOut"] = t.struct(
        {
            "teachers": t.array(t.proxy(renames["TeacherOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTeachersResponseOut"])
    types["GradeHistoryIn"] = t.struct(
        {
            "actorUserId": t.string().optional(),
            "gradeChangeType": t.string().optional(),
            "gradeTimestamp": t.string().optional(),
            "pointsEarned": t.number().optional(),
            "maxPoints": t.number().optional(),
        }
    ).named(renames["GradeHistoryIn"])
    types["GradeHistoryOut"] = t.struct(
        {
            "actorUserId": t.string().optional(),
            "gradeChangeType": t.string().optional(),
            "gradeTimestamp": t.string().optional(),
            "pointsEarned": t.number().optional(),
            "maxPoints": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GradeHistoryOut"])
    types["ListAnnouncementsResponseIn"] = t.struct(
        {
            "announcements": t.array(t.proxy(renames["AnnouncementIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAnnouncementsResponseIn"])
    types["ListAnnouncementsResponseOut"] = t.struct(
        {
            "announcements": t.array(t.proxy(renames["AnnouncementOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAnnouncementsResponseOut"])
    types["StudentSubmissionIn"] = t.struct(
        {
            "state": t.string().optional(),
            "shortAnswerSubmission": t.proxy(
                renames["ShortAnswerSubmissionIn"]
            ).optional(),
            "draftGrade": t.number().optional(),
            "multipleChoiceSubmission": t.proxy(
                renames["MultipleChoiceSubmissionIn"]
            ).optional(),
            "assignmentSubmission": t.proxy(
                renames["AssignmentSubmissionIn"]
            ).optional(),
            "courseWorkId": t.string().optional(),
            "updateTime": t.string().optional(),
            "associatedWithDeveloper": t.boolean().optional(),
            "late": t.boolean().optional(),
            "submissionHistory": t.array(
                t.proxy(renames["SubmissionHistoryIn"])
            ).optional(),
            "id": t.string().optional(),
            "userId": t.string().optional(),
            "assignedGrade": t.number().optional(),
            "courseId": t.string().optional(),
            "creationTime": t.string().optional(),
            "alternateLink": t.string().optional(),
            "courseWorkType": t.string().optional(),
        }
    ).named(renames["StudentSubmissionIn"])
    types["StudentSubmissionOut"] = t.struct(
        {
            "state": t.string().optional(),
            "shortAnswerSubmission": t.proxy(
                renames["ShortAnswerSubmissionOut"]
            ).optional(),
            "draftGrade": t.number().optional(),
            "multipleChoiceSubmission": t.proxy(
                renames["MultipleChoiceSubmissionOut"]
            ).optional(),
            "assignmentSubmission": t.proxy(
                renames["AssignmentSubmissionOut"]
            ).optional(),
            "courseWorkId": t.string().optional(),
            "updateTime": t.string().optional(),
            "associatedWithDeveloper": t.boolean().optional(),
            "late": t.boolean().optional(),
            "submissionHistory": t.array(
                t.proxy(renames["SubmissionHistoryOut"])
            ).optional(),
            "id": t.string().optional(),
            "userId": t.string().optional(),
            "assignedGrade": t.number().optional(),
            "courseId": t.string().optional(),
            "creationTime": t.string().optional(),
            "alternateLink": t.string().optional(),
            "courseWorkType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StudentSubmissionOut"])
    types["UserProfileIn"] = t.struct(
        {
            "emailAddress": t.string().optional(),
            "permissions": t.array(t.proxy(renames["GlobalPermissionIn"])).optional(),
            "id": t.string().optional(),
            "photoUrl": t.string().optional(),
            "verifiedTeacher": t.boolean().optional(),
            "name": t.proxy(renames["NameIn"]).optional(),
        }
    ).named(renames["UserProfileIn"])
    types["UserProfileOut"] = t.struct(
        {
            "emailAddress": t.string().optional(),
            "permissions": t.array(t.proxy(renames["GlobalPermissionOut"])).optional(),
            "id": t.string().optional(),
            "photoUrl": t.string().optional(),
            "verifiedTeacher": t.boolean().optional(),
            "name": t.proxy(renames["NameOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserProfileOut"])
    types["GuardianInvitationIn"] = t.struct(
        {
            "studentId": t.string().optional(),
            "state": t.string().optional(),
            "creationTime": t.string().optional(),
            "invitedEmailAddress": t.string().optional(),
            "invitationId": t.string().optional(),
        }
    ).named(renames["GuardianInvitationIn"])
    types["GuardianInvitationOut"] = t.struct(
        {
            "studentId": t.string().optional(),
            "state": t.string().optional(),
            "creationTime": t.string().optional(),
            "invitedEmailAddress": t.string().optional(),
            "invitationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuardianInvitationOut"])
    types["CourseMaterialSetIn"] = t.struct(
        {
            "title": t.string().optional(),
            "materials": t.array(t.proxy(renames["CourseMaterialIn"])).optional(),
        }
    ).named(renames["CourseMaterialSetIn"])
    types["CourseMaterialSetOut"] = t.struct(
        {
            "title": t.string().optional(),
            "materials": t.array(t.proxy(renames["CourseMaterialOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CourseMaterialSetOut"])
    types["DriveFileIn"] = t.struct(
        {
            "thumbnailUrl": t.string().optional(),
            "id": t.string().optional(),
            "alternateLink": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["DriveFileIn"])
    types["DriveFileOut"] = t.struct(
        {
            "thumbnailUrl": t.string().optional(),
            "id": t.string().optional(),
            "alternateLink": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveFileOut"])

    functions = {}
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
                "teacherGroupEmail": t.string().optional(),
                "guardiansEnabled": t.boolean().optional(),
                "ownerId": t.string().optional(),
                "alternateLink": t.string().optional(),
                "section": t.string().optional(),
                "calendarId": t.string().optional(),
                "courseState": t.string().optional(),
                "creationTime": t.string().optional(),
                "descriptionHeading": t.string().optional(),
                "room": t.string().optional(),
                "name": t.string().optional(),
                "teacherFolder": t.proxy(renames["DriveFolderIn"]).optional(),
                "enrollmentCode": t.string().optional(),
                "description": t.string().optional(),
                "courseGroupEmail": t.string().optional(),
                "gradebookSettings": t.proxy(renames["GradebookSettingsIn"]).optional(),
                "updateTime": t.string().optional(),
                "courseMaterialSets": t.array(
                    t.proxy(renames["CourseMaterialSetIn"])
                ).optional(),
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
                "teacherGroupEmail": t.string().optional(),
                "guardiansEnabled": t.boolean().optional(),
                "ownerId": t.string().optional(),
                "alternateLink": t.string().optional(),
                "section": t.string().optional(),
                "calendarId": t.string().optional(),
                "courseState": t.string().optional(),
                "creationTime": t.string().optional(),
                "descriptionHeading": t.string().optional(),
                "room": t.string().optional(),
                "name": t.string().optional(),
                "teacherFolder": t.proxy(renames["DriveFolderIn"]).optional(),
                "enrollmentCode": t.string().optional(),
                "description": t.string().optional(),
                "courseGroupEmail": t.string().optional(),
                "gradebookSettings": t.proxy(renames["GradebookSettingsIn"]).optional(),
                "updateTime": t.string().optional(),
                "courseMaterialSets": t.array(
                    t.proxy(renames["CourseMaterialSetIn"])
                ).optional(),
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
                "teacherGroupEmail": t.string().optional(),
                "guardiansEnabled": t.boolean().optional(),
                "ownerId": t.string().optional(),
                "alternateLink": t.string().optional(),
                "section": t.string().optional(),
                "calendarId": t.string().optional(),
                "courseState": t.string().optional(),
                "creationTime": t.string().optional(),
                "descriptionHeading": t.string().optional(),
                "room": t.string().optional(),
                "name": t.string().optional(),
                "teacherFolder": t.proxy(renames["DriveFolderIn"]).optional(),
                "enrollmentCode": t.string().optional(),
                "description": t.string().optional(),
                "courseGroupEmail": t.string().optional(),
                "gradebookSettings": t.proxy(renames["GradebookSettingsIn"]).optional(),
                "updateTime": t.string().optional(),
                "courseMaterialSets": t.array(
                    t.proxy(renames["CourseMaterialSetIn"])
                ).optional(),
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
                "teacherGroupEmail": t.string().optional(),
                "guardiansEnabled": t.boolean().optional(),
                "ownerId": t.string().optional(),
                "alternateLink": t.string().optional(),
                "section": t.string().optional(),
                "calendarId": t.string().optional(),
                "courseState": t.string().optional(),
                "creationTime": t.string().optional(),
                "descriptionHeading": t.string().optional(),
                "room": t.string().optional(),
                "name": t.string().optional(),
                "teacherFolder": t.proxy(renames["DriveFolderIn"]).optional(),
                "enrollmentCode": t.string().optional(),
                "description": t.string().optional(),
                "courseGroupEmail": t.string().optional(),
                "gradebookSettings": t.proxy(renames["GradebookSettingsIn"]).optional(),
                "updateTime": t.string().optional(),
                "courseMaterialSets": t.array(
                    t.proxy(renames["CourseMaterialSetIn"])
                ).optional(),
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
                "teacherGroupEmail": t.string().optional(),
                "guardiansEnabled": t.boolean().optional(),
                "ownerId": t.string().optional(),
                "alternateLink": t.string().optional(),
                "section": t.string().optional(),
                "calendarId": t.string().optional(),
                "courseState": t.string().optional(),
                "creationTime": t.string().optional(),
                "descriptionHeading": t.string().optional(),
                "room": t.string().optional(),
                "name": t.string().optional(),
                "teacherFolder": t.proxy(renames["DriveFolderIn"]).optional(),
                "enrollmentCode": t.string().optional(),
                "description": t.string().optional(),
                "courseGroupEmail": t.string().optional(),
                "gradebookSettings": t.proxy(renames["GradebookSettingsIn"]).optional(),
                "updateTime": t.string().optional(),
                "courseMaterialSets": t.array(
                    t.proxy(renames["CourseMaterialSetIn"])
                ).optional(),
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
                "teacherGroupEmail": t.string().optional(),
                "guardiansEnabled": t.boolean().optional(),
                "ownerId": t.string().optional(),
                "alternateLink": t.string().optional(),
                "section": t.string().optional(),
                "calendarId": t.string().optional(),
                "courseState": t.string().optional(),
                "creationTime": t.string().optional(),
                "descriptionHeading": t.string().optional(),
                "room": t.string().optional(),
                "name": t.string().optional(),
                "teacherFolder": t.proxy(renames["DriveFolderIn"]).optional(),
                "enrollmentCode": t.string().optional(),
                "description": t.string().optional(),
                "courseGroupEmail": t.string().optional(),
                "gradebookSettings": t.proxy(renames["GradebookSettingsIn"]).optional(),
                "updateTime": t.string().optional(),
                "courseMaterialSets": t.array(
                    t.proxy(renames["CourseMaterialSetIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesAliasesCreate"] = classroom.delete(
        "v1/courses/{courseId}/aliases/{alias}",
        t.struct(
            {
                "courseId": t.string().optional(),
                "alias": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesAliasesList"] = classroom.delete(
        "v1/courses/{courseId}/aliases/{alias}",
        t.struct(
            {
                "courseId": t.string().optional(),
                "alias": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesAliasesDelete"] = classroom.delete(
        "v1/courses/{courseId}/aliases/{alias}",
        t.struct(
            {
                "courseId": t.string().optional(),
                "alias": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesTeachersGet"] = classroom.post(
        "v1/courses/{courseId}/teachers",
        t.struct(
            {
                "courseId": t.string().optional(),
                "profile": t.proxy(renames["UserProfileIn"]).optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TeacherOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesTeachersDelete"] = classroom.post(
        "v1/courses/{courseId}/teachers",
        t.struct(
            {
                "courseId": t.string().optional(),
                "profile": t.proxy(renames["UserProfileIn"]).optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TeacherOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesTeachersList"] = classroom.post(
        "v1/courses/{courseId}/teachers",
        t.struct(
            {
                "courseId": t.string().optional(),
                "profile": t.proxy(renames["UserProfileIn"]).optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TeacherOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesTeachersCreate"] = classroom.post(
        "v1/courses/{courseId}/teachers",
        t.struct(
            {
                "courseId": t.string().optional(),
                "profile": t.proxy(renames["UserProfileIn"]).optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TeacherOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesTopicsDelete"] = classroom.patch(
        "v1/courses/{courseId}/topics/{id}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "courseId": t.string().optional(),
                "id": t.string().optional(),
                "topicId": t.string().optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesTopicsList"] = classroom.patch(
        "v1/courses/{courseId}/topics/{id}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "courseId": t.string().optional(),
                "id": t.string().optional(),
                "topicId": t.string().optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesTopicsGet"] = classroom.patch(
        "v1/courses/{courseId}/topics/{id}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "courseId": t.string().optional(),
                "id": t.string().optional(),
                "topicId": t.string().optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesTopicsCreate"] = classroom.patch(
        "v1/courses/{courseId}/topics/{id}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "courseId": t.string().optional(),
                "id": t.string().optional(),
                "topicId": t.string().optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesTopicsPatch"] = classroom.patch(
        "v1/courses/{courseId}/topics/{id}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "courseId": t.string().optional(),
                "id": t.string().optional(),
                "topicId": t.string().optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesStudentsList"] = classroom.post(
        "v1/courses/{courseId}/students",
        t.struct(
            {
                "enrollmentCode": t.string().optional(),
                "courseId": t.string().optional(),
                "profile": t.proxy(renames["UserProfileIn"]).optional(),
                "userId": t.string().optional(),
                "studentWorkFolder": t.proxy(renames["DriveFolderIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StudentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesStudentsDelete"] = classroom.post(
        "v1/courses/{courseId}/students",
        t.struct(
            {
                "enrollmentCode": t.string().optional(),
                "courseId": t.string().optional(),
                "profile": t.proxy(renames["UserProfileIn"]).optional(),
                "userId": t.string().optional(),
                "studentWorkFolder": t.proxy(renames["DriveFolderIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StudentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesStudentsGet"] = classroom.post(
        "v1/courses/{courseId}/students",
        t.struct(
            {
                "enrollmentCode": t.string().optional(),
                "courseId": t.string().optional(),
                "profile": t.proxy(renames["UserProfileIn"]).optional(),
                "userId": t.string().optional(),
                "studentWorkFolder": t.proxy(renames["DriveFolderIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StudentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesStudentsCreate"] = classroom.post(
        "v1/courses/{courseId}/students",
        t.struct(
            {
                "enrollmentCode": t.string().optional(),
                "courseId": t.string().optional(),
                "profile": t.proxy(renames["UserProfileIn"]).optional(),
                "userId": t.string().optional(),
                "studentWorkFolder": t.proxy(renames["DriveFolderIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StudentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkMaterialsDelete"] = classroom.get(
        "v1/courses/{courseId}/courseWorkMaterials",
        t.struct(
            {
                "materialLink": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "materialDriveId": t.string().optional(),
                "courseWorkMaterialStates": t.string().optional(),
                "orderBy": t.string().optional(),
                "courseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCourseWorkMaterialResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkMaterialsGet"] = classroom.get(
        "v1/courses/{courseId}/courseWorkMaterials",
        t.struct(
            {
                "materialLink": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "materialDriveId": t.string().optional(),
                "courseWorkMaterialStates": t.string().optional(),
                "orderBy": t.string().optional(),
                "courseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCourseWorkMaterialResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkMaterialsPatch"] = classroom.get(
        "v1/courses/{courseId}/courseWorkMaterials",
        t.struct(
            {
                "materialLink": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "materialDriveId": t.string().optional(),
                "courseWorkMaterialStates": t.string().optional(),
                "orderBy": t.string().optional(),
                "courseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCourseWorkMaterialResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkMaterialsCreate"] = classroom.get(
        "v1/courses/{courseId}/courseWorkMaterials",
        t.struct(
            {
                "materialLink": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "materialDriveId": t.string().optional(),
                "courseWorkMaterialStates": t.string().optional(),
                "orderBy": t.string().optional(),
                "courseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCourseWorkMaterialResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkMaterialsList"] = classroom.get(
        "v1/courses/{courseId}/courseWorkMaterials",
        t.struct(
            {
                "materialLink": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "materialDriveId": t.string().optional(),
                "courseWorkMaterialStates": t.string().optional(),
                "orderBy": t.string().optional(),
                "courseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCourseWorkMaterialResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesAnnouncementsDelete"] = classroom.get(
        "v1/courses/{courseId}/announcements",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "courseId": t.string().optional(),
                "announcementStates": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "orderBy": t.string().optional(),
                "courseId": t.string().optional(),
                "announcementStates": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "orderBy": t.string().optional(),
                "courseId": t.string().optional(),
                "announcementStates": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "orderBy": t.string().optional(),
                "courseId": t.string().optional(),
                "announcementStates": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAnnouncementsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesAnnouncementsGet"] = classroom.get(
        "v1/courses/{courseId}/announcements",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "courseId": t.string().optional(),
                "announcementStates": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "orderBy": t.string().optional(),
                "courseId": t.string().optional(),
                "announcementStates": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAnnouncementsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkPatch"] = classroom.get(
        "v1/courses/{courseId}/courseWork/{id}",
        t.struct(
            {
                "courseId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseWorkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkDelete"] = classroom.get(
        "v1/courses/{courseId}/courseWork/{id}",
        t.struct(
            {
                "courseId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseWorkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkList"] = classroom.get(
        "v1/courses/{courseId}/courseWork/{id}",
        t.struct(
            {
                "courseId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseWorkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkModifyAssignees"] = classroom.get(
        "v1/courses/{courseId}/courseWork/{id}",
        t.struct(
            {
                "courseId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseWorkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkCreate"] = classroom.get(
        "v1/courses/{courseId}/courseWork/{id}",
        t.struct(
            {
                "courseId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseWorkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkGet"] = classroom.get(
        "v1/courses/{courseId}/courseWork/{id}",
        t.struct(
            {
                "courseId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CourseWorkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkStudentSubmissionsTurnIn"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{courseWorkId}/studentSubmissions/{id}:return",
        t.struct(
            {
                "id": t.string().optional(),
                "courseWorkId": t.string().optional(),
                "courseId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkStudentSubmissionsList"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{courseWorkId}/studentSubmissions/{id}:return",
        t.struct(
            {
                "id": t.string().optional(),
                "courseWorkId": t.string().optional(),
                "courseId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkStudentSubmissionsGet"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{courseWorkId}/studentSubmissions/{id}:return",
        t.struct(
            {
                "id": t.string().optional(),
                "courseWorkId": t.string().optional(),
                "courseId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkStudentSubmissionsReclaim"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{courseWorkId}/studentSubmissions/{id}:return",
        t.struct(
            {
                "id": t.string().optional(),
                "courseWorkId": t.string().optional(),
                "courseId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkStudentSubmissionsPatch"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{courseWorkId}/studentSubmissions/{id}:return",
        t.struct(
            {
                "id": t.string().optional(),
                "courseWorkId": t.string().optional(),
                "courseId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkStudentSubmissionsModifyAttachments"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{courseWorkId}/studentSubmissions/{id}:return",
        t.struct(
            {
                "id": t.string().optional(),
                "courseWorkId": t.string().optional(),
                "courseId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["coursesCourseWorkStudentSubmissionsReturn"] = classroom.post(
        "v1/courses/{courseId}/courseWork/{courseWorkId}/studentSubmissions/{id}:return",
        t.struct(
            {
                "id": t.string().optional(),
                "courseWorkId": t.string().optional(),
                "courseId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesGet"] = classroom.get(
        "v1/userProfiles/{userId}",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["UserProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesGuardiansList"] = classroom.get(
        "v1/userProfiles/{studentId}/guardians/{guardianId}",
        t.struct(
            {
                "studentId": t.string().optional(),
                "guardianId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GuardianOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesGuardiansDelete"] = classroom.get(
        "v1/userProfiles/{studentId}/guardians/{guardianId}",
        t.struct(
            {
                "studentId": t.string().optional(),
                "guardianId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GuardianOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesGuardiansGet"] = classroom.get(
        "v1/userProfiles/{studentId}/guardians/{guardianId}",
        t.struct(
            {
                "studentId": t.string().optional(),
                "guardianId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GuardianOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesGuardianInvitationsList"] = classroom.post(
        "v1/userProfiles/{studentId}/guardianInvitations",
        t.struct(
            {
                "studentId": t.string().optional(),
                "state": t.string().optional(),
                "creationTime": t.string().optional(),
                "invitedEmailAddress": t.string().optional(),
                "invitationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GuardianInvitationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesGuardianInvitationsPatch"] = classroom.post(
        "v1/userProfiles/{studentId}/guardianInvitations",
        t.struct(
            {
                "studentId": t.string().optional(),
                "state": t.string().optional(),
                "creationTime": t.string().optional(),
                "invitedEmailAddress": t.string().optional(),
                "invitationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GuardianInvitationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesGuardianInvitationsGet"] = classroom.post(
        "v1/userProfiles/{studentId}/guardianInvitations",
        t.struct(
            {
                "studentId": t.string().optional(),
                "state": t.string().optional(),
                "creationTime": t.string().optional(),
                "invitedEmailAddress": t.string().optional(),
                "invitationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GuardianInvitationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userProfilesGuardianInvitationsCreate"] = classroom.post(
        "v1/userProfiles/{studentId}/guardianInvitations",
        t.struct(
            {
                "studentId": t.string().optional(),
                "state": t.string().optional(),
                "creationTime": t.string().optional(),
                "invitedEmailAddress": t.string().optional(),
                "invitationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GuardianInvitationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["invitationsDelete"] = classroom.get(
        "v1/invitations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "courseId": t.string().optional(),
                "userId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["invitationsGet"] = classroom.get(
        "v1/invitations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "courseId": t.string().optional(),
                "userId": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "courseId": t.string().optional(),
                "userId": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "courseId": t.string().optional(),
                "userId": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "courseId": t.string().optional(),
                "userId": t.string().optional(),
                "pageToken": t.string().optional(),
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
