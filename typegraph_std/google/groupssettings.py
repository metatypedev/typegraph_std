from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_groupssettings():
    groupssettings = HTTPRuntime("https://www.googleapis.com/")

    renames = {
        "ErrorResponse": "_groupssettings_1_ErrorResponse",
        "GroupsIn": "_groupssettings_2_GroupsIn",
        "GroupsOut": "_groupssettings_3_GroupsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GroupsIn"] = t.struct(
        {
            "membersCanPostAsTheGroup": t.string().optional(),
            "whoCanMoveTopicsIn": t.string().optional(),
            "whoCanLockTopics": t.string().optional(),
            "kind": t.string().optional(),
            "whoCanMoveTopicsOut": t.string().optional(),
            "whoCanMarkNoResponseNeeded": t.string().optional(),
            "whoCanUnassignTopic": t.string().optional(),
            "allowGoogleCommunication": t.string().optional(),
            "whoCanModerateContent": t.string().optional(),
            "whoCanAddReferences": t.string().optional(),
            "whoCanContactOwner": t.string().optional(),
            "replyTo": t.string().optional(),
            "whoCanBanUsers": t.string().optional(),
            "whoCanMarkDuplicate": t.string().optional(),
            "whoCanHideAbuse": t.string().optional(),
            "customRolesEnabledForSettingsToBeMerged": t.string().optional(),
            "whoCanAssistContent": t.string().optional(),
            "customReplyTo": t.string().optional(),
            "customFooterText": t.string().optional(),
            "showInGroupDirectory": t.string().optional(),
            "primaryLanguage": t.string().optional(),
            "whoCanPostAnnouncements": t.string().optional(),
            "whoCanEnterFreeFormTags": t.string().optional(),
            "whoCanApproveMembers": t.string().optional(),
            "whoCanMakeTopicsSticky": t.string().optional(),
            "spamModerationLevel": t.string().optional(),
            "whoCanMarkFavoriteReplyOnAnyTopic": t.string().optional(),
            "whoCanModifyMembers": t.string().optional(),
            "archiveOnly": t.string().optional(),
            "whoCanModifyTagsAndCategories": t.string().optional(),
            "allowExternalMembers": t.string().optional(),
            "maxMessageBytes": t.integer().optional(),
            "whoCanPostMessage": t.string().optional(),
            "enableCollaborativeInbox": t.string().optional(),
            "whoCanModerateMembers": t.string().optional(),
            "description": t.string().optional(),
            "whoCanAdd": t.string().optional(),
            "whoCanUnmarkFavoriteReplyOnAnyTopic": t.string().optional(),
            "messageDisplayFont": t.string().optional(),
            "name": t.string().optional(),
            "allowWebPosting": t.string().optional(),
            "messageModerationLevel": t.string().optional(),
            "whoCanDeleteAnyPost": t.string().optional(),
            "defaultMessageDenyNotificationText": t.string().optional(),
            "whoCanAssignTopics": t.string().optional(),
            "includeCustomFooter": t.string().optional(),
            "whoCanInvite": t.string().optional(),
            "favoriteRepliesOnTop": t.string().optional(),
            "whoCanViewGroup": t.string().optional(),
            "whoCanTakeTopics": t.string().optional(),
            "whoCanViewMembership": t.string().optional(),
            "whoCanDeleteTopics": t.string().optional(),
            "whoCanLeaveGroup": t.string().optional(),
            "default_sender": t.string().optional(),
            "whoCanDiscoverGroup": t.string().optional(),
            "isArchived": t.string().optional(),
            "includeInGlobalAddressList": t.string().optional(),
            "whoCanJoin": t.string().optional(),
            "sendMessageDenyNotification": t.string().optional(),
            "whoCanMarkFavoriteReplyOnOwnTopic": t.string().optional(),
            "email": t.string().optional(),
            "whoCanApproveMessages": t.string().optional(),
        }
    ).named(renames["GroupsIn"])
    types["GroupsOut"] = t.struct(
        {
            "membersCanPostAsTheGroup": t.string().optional(),
            "whoCanMoveTopicsIn": t.string().optional(),
            "whoCanLockTopics": t.string().optional(),
            "kind": t.string().optional(),
            "whoCanMoveTopicsOut": t.string().optional(),
            "whoCanMarkNoResponseNeeded": t.string().optional(),
            "whoCanUnassignTopic": t.string().optional(),
            "allowGoogleCommunication": t.string().optional(),
            "whoCanModerateContent": t.string().optional(),
            "whoCanAddReferences": t.string().optional(),
            "whoCanContactOwner": t.string().optional(),
            "replyTo": t.string().optional(),
            "whoCanBanUsers": t.string().optional(),
            "whoCanMarkDuplicate": t.string().optional(),
            "whoCanHideAbuse": t.string().optional(),
            "customRolesEnabledForSettingsToBeMerged": t.string().optional(),
            "whoCanAssistContent": t.string().optional(),
            "customReplyTo": t.string().optional(),
            "customFooterText": t.string().optional(),
            "showInGroupDirectory": t.string().optional(),
            "primaryLanguage": t.string().optional(),
            "whoCanPostAnnouncements": t.string().optional(),
            "whoCanEnterFreeFormTags": t.string().optional(),
            "whoCanApproveMembers": t.string().optional(),
            "whoCanMakeTopicsSticky": t.string().optional(),
            "spamModerationLevel": t.string().optional(),
            "whoCanMarkFavoriteReplyOnAnyTopic": t.string().optional(),
            "whoCanModifyMembers": t.string().optional(),
            "archiveOnly": t.string().optional(),
            "whoCanModifyTagsAndCategories": t.string().optional(),
            "allowExternalMembers": t.string().optional(),
            "maxMessageBytes": t.integer().optional(),
            "whoCanPostMessage": t.string().optional(),
            "enableCollaborativeInbox": t.string().optional(),
            "whoCanModerateMembers": t.string().optional(),
            "description": t.string().optional(),
            "whoCanAdd": t.string().optional(),
            "whoCanUnmarkFavoriteReplyOnAnyTopic": t.string().optional(),
            "messageDisplayFont": t.string().optional(),
            "name": t.string().optional(),
            "allowWebPosting": t.string().optional(),
            "messageModerationLevel": t.string().optional(),
            "whoCanDeleteAnyPost": t.string().optional(),
            "defaultMessageDenyNotificationText": t.string().optional(),
            "whoCanAssignTopics": t.string().optional(),
            "includeCustomFooter": t.string().optional(),
            "whoCanInvite": t.string().optional(),
            "favoriteRepliesOnTop": t.string().optional(),
            "whoCanViewGroup": t.string().optional(),
            "whoCanTakeTopics": t.string().optional(),
            "whoCanViewMembership": t.string().optional(),
            "whoCanDeleteTopics": t.string().optional(),
            "whoCanLeaveGroup": t.string().optional(),
            "default_sender": t.string().optional(),
            "whoCanDiscoverGroup": t.string().optional(),
            "isArchived": t.string().optional(),
            "includeInGlobalAddressList": t.string().optional(),
            "whoCanJoin": t.string().optional(),
            "sendMessageDenyNotification": t.string().optional(),
            "whoCanMarkFavoriteReplyOnOwnTopic": t.string().optional(),
            "email": t.string().optional(),
            "whoCanApproveMessages": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupsOut"])

    functions = {}
    functions["groupsPatch"] = groupssettings.put(
        "{groupUniqueId}",
        t.struct(
            {
                "groupUniqueId": t.string().optional(),
                "membersCanPostAsTheGroup": t.string().optional(),
                "whoCanMoveTopicsIn": t.string().optional(),
                "whoCanLockTopics": t.string().optional(),
                "kind": t.string().optional(),
                "whoCanMoveTopicsOut": t.string().optional(),
                "whoCanMarkNoResponseNeeded": t.string().optional(),
                "whoCanUnassignTopic": t.string().optional(),
                "allowGoogleCommunication": t.string().optional(),
                "whoCanModerateContent": t.string().optional(),
                "whoCanAddReferences": t.string().optional(),
                "whoCanContactOwner": t.string().optional(),
                "replyTo": t.string().optional(),
                "whoCanBanUsers": t.string().optional(),
                "whoCanMarkDuplicate": t.string().optional(),
                "whoCanHideAbuse": t.string().optional(),
                "customRolesEnabledForSettingsToBeMerged": t.string().optional(),
                "whoCanAssistContent": t.string().optional(),
                "customReplyTo": t.string().optional(),
                "customFooterText": t.string().optional(),
                "showInGroupDirectory": t.string().optional(),
                "primaryLanguage": t.string().optional(),
                "whoCanPostAnnouncements": t.string().optional(),
                "whoCanEnterFreeFormTags": t.string().optional(),
                "whoCanApproveMembers": t.string().optional(),
                "whoCanMakeTopicsSticky": t.string().optional(),
                "spamModerationLevel": t.string().optional(),
                "whoCanMarkFavoriteReplyOnAnyTopic": t.string().optional(),
                "whoCanModifyMembers": t.string().optional(),
                "archiveOnly": t.string().optional(),
                "whoCanModifyTagsAndCategories": t.string().optional(),
                "allowExternalMembers": t.string().optional(),
                "maxMessageBytes": t.integer().optional(),
                "whoCanPostMessage": t.string().optional(),
                "enableCollaborativeInbox": t.string().optional(),
                "whoCanModerateMembers": t.string().optional(),
                "description": t.string().optional(),
                "whoCanAdd": t.string().optional(),
                "whoCanUnmarkFavoriteReplyOnAnyTopic": t.string().optional(),
                "messageDisplayFont": t.string().optional(),
                "name": t.string().optional(),
                "allowWebPosting": t.string().optional(),
                "messageModerationLevel": t.string().optional(),
                "whoCanDeleteAnyPost": t.string().optional(),
                "defaultMessageDenyNotificationText": t.string().optional(),
                "whoCanAssignTopics": t.string().optional(),
                "includeCustomFooter": t.string().optional(),
                "whoCanInvite": t.string().optional(),
                "favoriteRepliesOnTop": t.string().optional(),
                "whoCanViewGroup": t.string().optional(),
                "whoCanTakeTopics": t.string().optional(),
                "whoCanViewMembership": t.string().optional(),
                "whoCanDeleteTopics": t.string().optional(),
                "whoCanLeaveGroup": t.string().optional(),
                "default_sender": t.string().optional(),
                "whoCanDiscoverGroup": t.string().optional(),
                "isArchived": t.string().optional(),
                "includeInGlobalAddressList": t.string().optional(),
                "whoCanJoin": t.string().optional(),
                "sendMessageDenyNotification": t.string().optional(),
                "whoCanMarkFavoriteReplyOnOwnTopic": t.string().optional(),
                "email": t.string().optional(),
                "whoCanApproveMessages": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsGet"] = groupssettings.put(
        "{groupUniqueId}",
        t.struct(
            {
                "groupUniqueId": t.string().optional(),
                "membersCanPostAsTheGroup": t.string().optional(),
                "whoCanMoveTopicsIn": t.string().optional(),
                "whoCanLockTopics": t.string().optional(),
                "kind": t.string().optional(),
                "whoCanMoveTopicsOut": t.string().optional(),
                "whoCanMarkNoResponseNeeded": t.string().optional(),
                "whoCanUnassignTopic": t.string().optional(),
                "allowGoogleCommunication": t.string().optional(),
                "whoCanModerateContent": t.string().optional(),
                "whoCanAddReferences": t.string().optional(),
                "whoCanContactOwner": t.string().optional(),
                "replyTo": t.string().optional(),
                "whoCanBanUsers": t.string().optional(),
                "whoCanMarkDuplicate": t.string().optional(),
                "whoCanHideAbuse": t.string().optional(),
                "customRolesEnabledForSettingsToBeMerged": t.string().optional(),
                "whoCanAssistContent": t.string().optional(),
                "customReplyTo": t.string().optional(),
                "customFooterText": t.string().optional(),
                "showInGroupDirectory": t.string().optional(),
                "primaryLanguage": t.string().optional(),
                "whoCanPostAnnouncements": t.string().optional(),
                "whoCanEnterFreeFormTags": t.string().optional(),
                "whoCanApproveMembers": t.string().optional(),
                "whoCanMakeTopicsSticky": t.string().optional(),
                "spamModerationLevel": t.string().optional(),
                "whoCanMarkFavoriteReplyOnAnyTopic": t.string().optional(),
                "whoCanModifyMembers": t.string().optional(),
                "archiveOnly": t.string().optional(),
                "whoCanModifyTagsAndCategories": t.string().optional(),
                "allowExternalMembers": t.string().optional(),
                "maxMessageBytes": t.integer().optional(),
                "whoCanPostMessage": t.string().optional(),
                "enableCollaborativeInbox": t.string().optional(),
                "whoCanModerateMembers": t.string().optional(),
                "description": t.string().optional(),
                "whoCanAdd": t.string().optional(),
                "whoCanUnmarkFavoriteReplyOnAnyTopic": t.string().optional(),
                "messageDisplayFont": t.string().optional(),
                "name": t.string().optional(),
                "allowWebPosting": t.string().optional(),
                "messageModerationLevel": t.string().optional(),
                "whoCanDeleteAnyPost": t.string().optional(),
                "defaultMessageDenyNotificationText": t.string().optional(),
                "whoCanAssignTopics": t.string().optional(),
                "includeCustomFooter": t.string().optional(),
                "whoCanInvite": t.string().optional(),
                "favoriteRepliesOnTop": t.string().optional(),
                "whoCanViewGroup": t.string().optional(),
                "whoCanTakeTopics": t.string().optional(),
                "whoCanViewMembership": t.string().optional(),
                "whoCanDeleteTopics": t.string().optional(),
                "whoCanLeaveGroup": t.string().optional(),
                "default_sender": t.string().optional(),
                "whoCanDiscoverGroup": t.string().optional(),
                "isArchived": t.string().optional(),
                "includeInGlobalAddressList": t.string().optional(),
                "whoCanJoin": t.string().optional(),
                "sendMessageDenyNotification": t.string().optional(),
                "whoCanMarkFavoriteReplyOnOwnTopic": t.string().optional(),
                "email": t.string().optional(),
                "whoCanApproveMessages": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsUpdate"] = groupssettings.put(
        "{groupUniqueId}",
        t.struct(
            {
                "groupUniqueId": t.string().optional(),
                "membersCanPostAsTheGroup": t.string().optional(),
                "whoCanMoveTopicsIn": t.string().optional(),
                "whoCanLockTopics": t.string().optional(),
                "kind": t.string().optional(),
                "whoCanMoveTopicsOut": t.string().optional(),
                "whoCanMarkNoResponseNeeded": t.string().optional(),
                "whoCanUnassignTopic": t.string().optional(),
                "allowGoogleCommunication": t.string().optional(),
                "whoCanModerateContent": t.string().optional(),
                "whoCanAddReferences": t.string().optional(),
                "whoCanContactOwner": t.string().optional(),
                "replyTo": t.string().optional(),
                "whoCanBanUsers": t.string().optional(),
                "whoCanMarkDuplicate": t.string().optional(),
                "whoCanHideAbuse": t.string().optional(),
                "customRolesEnabledForSettingsToBeMerged": t.string().optional(),
                "whoCanAssistContent": t.string().optional(),
                "customReplyTo": t.string().optional(),
                "customFooterText": t.string().optional(),
                "showInGroupDirectory": t.string().optional(),
                "primaryLanguage": t.string().optional(),
                "whoCanPostAnnouncements": t.string().optional(),
                "whoCanEnterFreeFormTags": t.string().optional(),
                "whoCanApproveMembers": t.string().optional(),
                "whoCanMakeTopicsSticky": t.string().optional(),
                "spamModerationLevel": t.string().optional(),
                "whoCanMarkFavoriteReplyOnAnyTopic": t.string().optional(),
                "whoCanModifyMembers": t.string().optional(),
                "archiveOnly": t.string().optional(),
                "whoCanModifyTagsAndCategories": t.string().optional(),
                "allowExternalMembers": t.string().optional(),
                "maxMessageBytes": t.integer().optional(),
                "whoCanPostMessage": t.string().optional(),
                "enableCollaborativeInbox": t.string().optional(),
                "whoCanModerateMembers": t.string().optional(),
                "description": t.string().optional(),
                "whoCanAdd": t.string().optional(),
                "whoCanUnmarkFavoriteReplyOnAnyTopic": t.string().optional(),
                "messageDisplayFont": t.string().optional(),
                "name": t.string().optional(),
                "allowWebPosting": t.string().optional(),
                "messageModerationLevel": t.string().optional(),
                "whoCanDeleteAnyPost": t.string().optional(),
                "defaultMessageDenyNotificationText": t.string().optional(),
                "whoCanAssignTopics": t.string().optional(),
                "includeCustomFooter": t.string().optional(),
                "whoCanInvite": t.string().optional(),
                "favoriteRepliesOnTop": t.string().optional(),
                "whoCanViewGroup": t.string().optional(),
                "whoCanTakeTopics": t.string().optional(),
                "whoCanViewMembership": t.string().optional(),
                "whoCanDeleteTopics": t.string().optional(),
                "whoCanLeaveGroup": t.string().optional(),
                "default_sender": t.string().optional(),
                "whoCanDiscoverGroup": t.string().optional(),
                "isArchived": t.string().optional(),
                "includeInGlobalAddressList": t.string().optional(),
                "whoCanJoin": t.string().optional(),
                "sendMessageDenyNotification": t.string().optional(),
                "whoCanMarkFavoriteReplyOnOwnTopic": t.string().optional(),
                "email": t.string().optional(),
                "whoCanApproveMessages": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="groupssettings",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
