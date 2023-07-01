from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_gmail():
    gmail = HTTPRuntime("https://gmail.googleapis.com/")

    renames = {
        "ErrorResponse": "_gmail_1_ErrorResponse",
        "ModifyThreadRequestIn": "_gmail_2_ModifyThreadRequestIn",
        "ModifyThreadRequestOut": "_gmail_3_ModifyThreadRequestOut",
        "MessagePartBodyIn": "_gmail_4_MessagePartBodyIn",
        "MessagePartBodyOut": "_gmail_5_MessagePartBodyOut",
        "ImapSettingsIn": "_gmail_6_ImapSettingsIn",
        "ImapSettingsOut": "_gmail_7_ImapSettingsOut",
        "WatchResponseIn": "_gmail_8_WatchResponseIn",
        "WatchResponseOut": "_gmail_9_WatchResponseOut",
        "BatchDeleteMessagesRequestIn": "_gmail_10_BatchDeleteMessagesRequestIn",
        "BatchDeleteMessagesRequestOut": "_gmail_11_BatchDeleteMessagesRequestOut",
        "HistoryMessageAddedIn": "_gmail_12_HistoryMessageAddedIn",
        "HistoryMessageAddedOut": "_gmail_13_HistoryMessageAddedOut",
        "ListLabelsResponseIn": "_gmail_14_ListLabelsResponseIn",
        "ListLabelsResponseOut": "_gmail_15_ListLabelsResponseOut",
        "ListHistoryResponseIn": "_gmail_16_ListHistoryResponseIn",
        "ListHistoryResponseOut": "_gmail_17_ListHistoryResponseOut",
        "CseIdentityIn": "_gmail_18_CseIdentityIn",
        "CseIdentityOut": "_gmail_19_CseIdentityOut",
        "ListCseKeyPairsResponseIn": "_gmail_20_ListCseKeyPairsResponseIn",
        "ListCseKeyPairsResponseOut": "_gmail_21_ListCseKeyPairsResponseOut",
        "BatchModifyMessagesRequestIn": "_gmail_22_BatchModifyMessagesRequestIn",
        "BatchModifyMessagesRequestOut": "_gmail_23_BatchModifyMessagesRequestOut",
        "DraftIn": "_gmail_24_DraftIn",
        "DraftOut": "_gmail_25_DraftOut",
        "LabelIn": "_gmail_26_LabelIn",
        "LabelOut": "_gmail_27_LabelOut",
        "ListCseIdentitiesResponseIn": "_gmail_28_ListCseIdentitiesResponseIn",
        "ListCseIdentitiesResponseOut": "_gmail_29_ListCseIdentitiesResponseOut",
        "HistoryLabelRemovedIn": "_gmail_30_HistoryLabelRemovedIn",
        "HistoryLabelRemovedOut": "_gmail_31_HistoryLabelRemovedOut",
        "SendAsIn": "_gmail_32_SendAsIn",
        "SendAsOut": "_gmail_33_SendAsOut",
        "LanguageSettingsIn": "_gmail_34_LanguageSettingsIn",
        "LanguageSettingsOut": "_gmail_35_LanguageSettingsOut",
        "ModifyMessageRequestIn": "_gmail_36_ModifyMessageRequestIn",
        "ModifyMessageRequestOut": "_gmail_37_ModifyMessageRequestOut",
        "ListFiltersResponseIn": "_gmail_38_ListFiltersResponseIn",
        "ListFiltersResponseOut": "_gmail_39_ListFiltersResponseOut",
        "MessagePartIn": "_gmail_40_MessagePartIn",
        "MessagePartOut": "_gmail_41_MessagePartOut",
        "ForwardingAddressIn": "_gmail_42_ForwardingAddressIn",
        "ForwardingAddressOut": "_gmail_43_ForwardingAddressOut",
        "HistoryIn": "_gmail_44_HistoryIn",
        "HistoryOut": "_gmail_45_HistoryOut",
        "MessagePartHeaderIn": "_gmail_46_MessagePartHeaderIn",
        "MessagePartHeaderOut": "_gmail_47_MessagePartHeaderOut",
        "ThreadIn": "_gmail_48_ThreadIn",
        "ThreadOut": "_gmail_49_ThreadOut",
        "DelegateIn": "_gmail_50_DelegateIn",
        "DelegateOut": "_gmail_51_DelegateOut",
        "HistoryMessageDeletedIn": "_gmail_52_HistoryMessageDeletedIn",
        "HistoryMessageDeletedOut": "_gmail_53_HistoryMessageDeletedOut",
        "ObliterateCseKeyPairRequestIn": "_gmail_54_ObliterateCseKeyPairRequestIn",
        "ObliterateCseKeyPairRequestOut": "_gmail_55_ObliterateCseKeyPairRequestOut",
        "CsePrivateKeyMetadataIn": "_gmail_56_CsePrivateKeyMetadataIn",
        "CsePrivateKeyMetadataOut": "_gmail_57_CsePrivateKeyMetadataOut",
        "HistoryLabelAddedIn": "_gmail_58_HistoryLabelAddedIn",
        "HistoryLabelAddedOut": "_gmail_59_HistoryLabelAddedOut",
        "ListDraftsResponseIn": "_gmail_60_ListDraftsResponseIn",
        "ListDraftsResponseOut": "_gmail_61_ListDraftsResponseOut",
        "VacationSettingsIn": "_gmail_62_VacationSettingsIn",
        "VacationSettingsOut": "_gmail_63_VacationSettingsOut",
        "LabelColorIn": "_gmail_64_LabelColorIn",
        "LabelColorOut": "_gmail_65_LabelColorOut",
        "CseKeyPairIn": "_gmail_66_CseKeyPairIn",
        "CseKeyPairOut": "_gmail_67_CseKeyPairOut",
        "PopSettingsIn": "_gmail_68_PopSettingsIn",
        "PopSettingsOut": "_gmail_69_PopSettingsOut",
        "ListMessagesResponseIn": "_gmail_70_ListMessagesResponseIn",
        "ListMessagesResponseOut": "_gmail_71_ListMessagesResponseOut",
        "ListDelegatesResponseIn": "_gmail_72_ListDelegatesResponseIn",
        "ListDelegatesResponseOut": "_gmail_73_ListDelegatesResponseOut",
        "SmimeInfoIn": "_gmail_74_SmimeInfoIn",
        "SmimeInfoOut": "_gmail_75_SmimeInfoOut",
        "DisableCseKeyPairRequestIn": "_gmail_76_DisableCseKeyPairRequestIn",
        "DisableCseKeyPairRequestOut": "_gmail_77_DisableCseKeyPairRequestOut",
        "ListSmimeInfoResponseIn": "_gmail_78_ListSmimeInfoResponseIn",
        "ListSmimeInfoResponseOut": "_gmail_79_ListSmimeInfoResponseOut",
        "ListSendAsResponseIn": "_gmail_80_ListSendAsResponseIn",
        "ListSendAsResponseOut": "_gmail_81_ListSendAsResponseOut",
        "EnableCseKeyPairRequestIn": "_gmail_82_EnableCseKeyPairRequestIn",
        "EnableCseKeyPairRequestOut": "_gmail_83_EnableCseKeyPairRequestOut",
        "MessageIn": "_gmail_84_MessageIn",
        "MessageOut": "_gmail_85_MessageOut",
        "AutoForwardingIn": "_gmail_86_AutoForwardingIn",
        "AutoForwardingOut": "_gmail_87_AutoForwardingOut",
        "KaclsKeyMetadataIn": "_gmail_88_KaclsKeyMetadataIn",
        "KaclsKeyMetadataOut": "_gmail_89_KaclsKeyMetadataOut",
        "FilterCriteriaIn": "_gmail_90_FilterCriteriaIn",
        "FilterCriteriaOut": "_gmail_91_FilterCriteriaOut",
        "FilterActionIn": "_gmail_92_FilterActionIn",
        "FilterActionOut": "_gmail_93_FilterActionOut",
        "SmtpMsaIn": "_gmail_94_SmtpMsaIn",
        "SmtpMsaOut": "_gmail_95_SmtpMsaOut",
        "WatchRequestIn": "_gmail_96_WatchRequestIn",
        "WatchRequestOut": "_gmail_97_WatchRequestOut",
        "ListThreadsResponseIn": "_gmail_98_ListThreadsResponseIn",
        "ListThreadsResponseOut": "_gmail_99_ListThreadsResponseOut",
        "ListForwardingAddressesResponseIn": "_gmail_100_ListForwardingAddressesResponseIn",
        "ListForwardingAddressesResponseOut": "_gmail_101_ListForwardingAddressesResponseOut",
        "ProfileIn": "_gmail_102_ProfileIn",
        "ProfileOut": "_gmail_103_ProfileOut",
        "FilterIn": "_gmail_104_FilterIn",
        "FilterOut": "_gmail_105_FilterOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ModifyThreadRequestIn"] = t.struct(
        {
            "removeLabelIds": t.array(t.string()).optional(),
            "addLabelIds": t.array(t.string()).optional(),
        }
    ).named(renames["ModifyThreadRequestIn"])
    types["ModifyThreadRequestOut"] = t.struct(
        {
            "removeLabelIds": t.array(t.string()).optional(),
            "addLabelIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyThreadRequestOut"])
    types["MessagePartBodyIn"] = t.struct(
        {
            "attachmentId": t.string().optional(),
            "size": t.integer().optional(),
            "data": t.string().optional(),
        }
    ).named(renames["MessagePartBodyIn"])
    types["MessagePartBodyOut"] = t.struct(
        {
            "attachmentId": t.string().optional(),
            "size": t.integer().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessagePartBodyOut"])
    types["ImapSettingsIn"] = t.struct(
        {
            "autoExpunge": t.boolean().optional(),
            "enabled": t.boolean().optional(),
            "maxFolderSize": t.integer().optional(),
            "expungeBehavior": t.string().optional(),
        }
    ).named(renames["ImapSettingsIn"])
    types["ImapSettingsOut"] = t.struct(
        {
            "autoExpunge": t.boolean().optional(),
            "enabled": t.boolean().optional(),
            "maxFolderSize": t.integer().optional(),
            "expungeBehavior": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImapSettingsOut"])
    types["WatchResponseIn"] = t.struct(
        {"historyId": t.string().optional(), "expiration": t.string().optional()}
    ).named(renames["WatchResponseIn"])
    types["WatchResponseOut"] = t.struct(
        {
            "historyId": t.string().optional(),
            "expiration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchResponseOut"])
    types["BatchDeleteMessagesRequestIn"] = t.struct(
        {"ids": t.array(t.string()).optional()}
    ).named(renames["BatchDeleteMessagesRequestIn"])
    types["BatchDeleteMessagesRequestOut"] = t.struct(
        {
            "ids": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteMessagesRequestOut"])
    types["HistoryMessageAddedIn"] = t.struct(
        {"message": t.proxy(renames["MessageIn"])}
    ).named(renames["HistoryMessageAddedIn"])
    types["HistoryMessageAddedOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryMessageAddedOut"])
    types["ListLabelsResponseIn"] = t.struct(
        {"labels": t.array(t.proxy(renames["LabelIn"])).optional()}
    ).named(renames["ListLabelsResponseIn"])
    types["ListLabelsResponseOut"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLabelsResponseOut"])
    types["ListHistoryResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "historyId": t.string().optional(),
            "history": t.array(t.proxy(renames["HistoryIn"])).optional(),
        }
    ).named(renames["ListHistoryResponseIn"])
    types["ListHistoryResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "historyId": t.string().optional(),
            "history": t.array(t.proxy(renames["HistoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListHistoryResponseOut"])
    types["CseIdentityIn"] = t.struct(
        {
            "emailAddress": t.string().optional(),
            "primaryKeyPairId": t.string().optional(),
        }
    ).named(renames["CseIdentityIn"])
    types["CseIdentityOut"] = t.struct(
        {
            "emailAddress": t.string().optional(),
            "primaryKeyPairId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CseIdentityOut"])
    types["ListCseKeyPairsResponseIn"] = t.struct(
        {
            "cseKeyPairs": t.array(t.proxy(renames["CseKeyPairIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCseKeyPairsResponseIn"])
    types["ListCseKeyPairsResponseOut"] = t.struct(
        {
            "cseKeyPairs": t.array(t.proxy(renames["CseKeyPairOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCseKeyPairsResponseOut"])
    types["BatchModifyMessagesRequestIn"] = t.struct(
        {
            "ids": t.array(t.string()).optional(),
            "addLabelIds": t.array(t.string()).optional(),
            "removeLabelIds": t.array(t.string()).optional(),
        }
    ).named(renames["BatchModifyMessagesRequestIn"])
    types["BatchModifyMessagesRequestOut"] = t.struct(
        {
            "ids": t.array(t.string()).optional(),
            "addLabelIds": t.array(t.string()).optional(),
            "removeLabelIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchModifyMessagesRequestOut"])
    types["DraftIn"] = t.struct(
        {
            "id": t.string().optional(),
            "message": t.proxy(renames["MessageIn"]).optional(),
        }
    ).named(renames["DraftIn"])
    types["DraftOut"] = t.struct(
        {
            "id": t.string().optional(),
            "message": t.proxy(renames["MessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DraftOut"])
    types["LabelIn"] = t.struct(
        {
            "threadsTotal": t.integer().optional(),
            "color": t.proxy(renames["LabelColorIn"]).optional(),
            "type": t.string().optional(),
            "threadsUnread": t.integer().optional(),
            "labelListVisibility": t.string().optional(),
            "messagesTotal": t.integer().optional(),
            "messagesUnread": t.integer().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "messageListVisibility": t.string().optional(),
        }
    ).named(renames["LabelIn"])
    types["LabelOut"] = t.struct(
        {
            "threadsTotal": t.integer().optional(),
            "color": t.proxy(renames["LabelColorOut"]).optional(),
            "type": t.string().optional(),
            "threadsUnread": t.integer().optional(),
            "labelListVisibility": t.string().optional(),
            "messagesTotal": t.integer().optional(),
            "messagesUnread": t.integer().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "messageListVisibility": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelOut"])
    types["ListCseIdentitiesResponseIn"] = t.struct(
        {
            "cseIdentities": t.array(t.proxy(renames["CseIdentityIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCseIdentitiesResponseIn"])
    types["ListCseIdentitiesResponseOut"] = t.struct(
        {
            "cseIdentities": t.array(t.proxy(renames["CseIdentityOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCseIdentitiesResponseOut"])
    types["HistoryLabelRemovedIn"] = t.struct(
        {
            "message": t.proxy(renames["MessageIn"]),
            "labelIds": t.array(t.string()).optional(),
        }
    ).named(renames["HistoryLabelRemovedIn"])
    types["HistoryLabelRemovedOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]),
            "labelIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryLabelRemovedOut"])
    types["SendAsIn"] = t.struct(
        {
            "sendAsEmail": t.string().optional(),
            "verificationStatus": t.string().optional(),
            "isDefault": t.boolean().optional(),
            "smtpMsa": t.proxy(renames["SmtpMsaIn"]).optional(),
            "signature": t.string().optional(),
            "replyToAddress": t.string().optional(),
            "isPrimary": t.boolean().optional(),
            "displayName": t.string().optional(),
            "treatAsAlias": t.boolean().optional(),
        }
    ).named(renames["SendAsIn"])
    types["SendAsOut"] = t.struct(
        {
            "sendAsEmail": t.string().optional(),
            "verificationStatus": t.string().optional(),
            "isDefault": t.boolean().optional(),
            "smtpMsa": t.proxy(renames["SmtpMsaOut"]).optional(),
            "signature": t.string().optional(),
            "replyToAddress": t.string().optional(),
            "isPrimary": t.boolean().optional(),
            "displayName": t.string().optional(),
            "treatAsAlias": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SendAsOut"])
    types["LanguageSettingsIn"] = t.struct(
        {"displayLanguage": t.string().optional()}
    ).named(renames["LanguageSettingsIn"])
    types["LanguageSettingsOut"] = t.struct(
        {
            "displayLanguage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageSettingsOut"])
    types["ModifyMessageRequestIn"] = t.struct(
        {
            "removeLabelIds": t.array(t.string()).optional(),
            "addLabelIds": t.array(t.string()).optional(),
        }
    ).named(renames["ModifyMessageRequestIn"])
    types["ModifyMessageRequestOut"] = t.struct(
        {
            "removeLabelIds": t.array(t.string()).optional(),
            "addLabelIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyMessageRequestOut"])
    types["ListFiltersResponseIn"] = t.struct(
        {"filter": t.array(t.proxy(renames["FilterIn"])).optional()}
    ).named(renames["ListFiltersResponseIn"])
    types["ListFiltersResponseOut"] = t.struct(
        {
            "filter": t.array(t.proxy(renames["FilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFiltersResponseOut"])
    types["MessagePartIn"] = t.struct(
        {
            "body": t.proxy(renames["MessagePartBodyIn"]).optional(),
            "headers": t.array(t.proxy(renames["MessagePartHeaderIn"])).optional(),
            "parts": t.array(t.proxy(renames["MessagePartIn"])).optional(),
            "filename": t.string().optional(),
            "mimeType": t.string().optional(),
            "partId": t.string().optional(),
        }
    ).named(renames["MessagePartIn"])
    types["MessagePartOut"] = t.struct(
        {
            "body": t.proxy(renames["MessagePartBodyOut"]).optional(),
            "headers": t.array(t.proxy(renames["MessagePartHeaderOut"])).optional(),
            "parts": t.array(t.proxy(renames["MessagePartOut"])).optional(),
            "filename": t.string().optional(),
            "mimeType": t.string().optional(),
            "partId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessagePartOut"])
    types["ForwardingAddressIn"] = t.struct(
        {
            "verificationStatus": t.string().optional(),
            "forwardingEmail": t.string().optional(),
        }
    ).named(renames["ForwardingAddressIn"])
    types["ForwardingAddressOut"] = t.struct(
        {
            "verificationStatus": t.string().optional(),
            "forwardingEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForwardingAddressOut"])
    types["HistoryIn"] = t.struct(
        {
            "labelsAdded": t.array(t.proxy(renames["HistoryLabelAddedIn"])).optional(),
            "messages": t.array(t.proxy(renames["MessageIn"])).optional(),
            "messagesDeleted": t.array(
                t.proxy(renames["HistoryMessageDeletedIn"])
            ).optional(),
            "labelsRemoved": t.array(
                t.proxy(renames["HistoryLabelRemovedIn"])
            ).optional(),
            "messagesAdded": t.array(
                t.proxy(renames["HistoryMessageAddedIn"])
            ).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["HistoryIn"])
    types["HistoryOut"] = t.struct(
        {
            "labelsAdded": t.array(t.proxy(renames["HistoryLabelAddedOut"])).optional(),
            "messages": t.array(t.proxy(renames["MessageOut"])).optional(),
            "messagesDeleted": t.array(
                t.proxy(renames["HistoryMessageDeletedOut"])
            ).optional(),
            "labelsRemoved": t.array(
                t.proxy(renames["HistoryLabelRemovedOut"])
            ).optional(),
            "messagesAdded": t.array(
                t.proxy(renames["HistoryMessageAddedOut"])
            ).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryOut"])
    types["MessagePartHeaderIn"] = t.struct(
        {"name": t.string().optional(), "value": t.string().optional()}
    ).named(renames["MessagePartHeaderIn"])
    types["MessagePartHeaderOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessagePartHeaderOut"])
    types["ThreadIn"] = t.struct(
        {
            "id": t.string().optional(),
            "messages": t.array(t.proxy(renames["MessageIn"])).optional(),
            "snippet": t.string().optional(),
            "historyId": t.string().optional(),
        }
    ).named(renames["ThreadIn"])
    types["ThreadOut"] = t.struct(
        {
            "id": t.string().optional(),
            "messages": t.array(t.proxy(renames["MessageOut"])).optional(),
            "snippet": t.string().optional(),
            "historyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThreadOut"])
    types["DelegateIn"] = t.struct(
        {
            "verificationStatus": t.string().optional(),
            "delegateEmail": t.string().optional(),
        }
    ).named(renames["DelegateIn"])
    types["DelegateOut"] = t.struct(
        {
            "verificationStatus": t.string().optional(),
            "delegateEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DelegateOut"])
    types["HistoryMessageDeletedIn"] = t.struct(
        {"message": t.proxy(renames["MessageIn"])}
    ).named(renames["HistoryMessageDeletedIn"])
    types["HistoryMessageDeletedOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryMessageDeletedOut"])
    types["ObliterateCseKeyPairRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ObliterateCseKeyPairRequestIn"])
    types["ObliterateCseKeyPairRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ObliterateCseKeyPairRequestOut"])
    types["CsePrivateKeyMetadataIn"] = t.struct(
        {"kaclsKeyMetadata": t.proxy(renames["KaclsKeyMetadataIn"]).optional()}
    ).named(renames["CsePrivateKeyMetadataIn"])
    types["CsePrivateKeyMetadataOut"] = t.struct(
        {
            "kaclsKeyMetadata": t.proxy(renames["KaclsKeyMetadataOut"]).optional(),
            "privateKeyMetadataId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CsePrivateKeyMetadataOut"])
    types["HistoryLabelAddedIn"] = t.struct(
        {
            "message": t.proxy(renames["MessageIn"]),
            "labelIds": t.array(t.string()).optional(),
        }
    ).named(renames["HistoryLabelAddedIn"])
    types["HistoryLabelAddedOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]),
            "labelIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryLabelAddedOut"])
    types["ListDraftsResponseIn"] = t.struct(
        {
            "drafts": t.array(t.proxy(renames["DraftIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "resultSizeEstimate": t.integer().optional(),
        }
    ).named(renames["ListDraftsResponseIn"])
    types["ListDraftsResponseOut"] = t.struct(
        {
            "drafts": t.array(t.proxy(renames["DraftOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "resultSizeEstimate": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDraftsResponseOut"])
    types["VacationSettingsIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "restrictToDomain": t.boolean().optional(),
            "restrictToContacts": t.boolean().optional(),
            "responseSubject": t.string().optional(),
            "startTime": t.string().optional(),
            "responseBodyHtml": t.string().optional(),
            "enableAutoReply": t.boolean().optional(),
            "responseBodyPlainText": t.string().optional(),
        }
    ).named(renames["VacationSettingsIn"])
    types["VacationSettingsOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "restrictToDomain": t.boolean().optional(),
            "restrictToContacts": t.boolean().optional(),
            "responseSubject": t.string().optional(),
            "startTime": t.string().optional(),
            "responseBodyHtml": t.string().optional(),
            "enableAutoReply": t.boolean().optional(),
            "responseBodyPlainText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VacationSettingsOut"])
    types["LabelColorIn"] = t.struct(
        {"textColor": t.string().optional(), "backgroundColor": t.string().optional()}
    ).named(renames["LabelColorIn"])
    types["LabelColorOut"] = t.struct(
        {
            "textColor": t.string().optional(),
            "backgroundColor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelColorOut"])
    types["CseKeyPairIn"] = t.struct(
        {
            "privateKeyMetadata": t.array(
                t.proxy(renames["CsePrivateKeyMetadataIn"])
            ).optional(),
            "pkcs7": t.string().optional(),
        }
    ).named(renames["CseKeyPairIn"])
    types["CseKeyPairOut"] = t.struct(
        {
            "privateKeyMetadata": t.array(
                t.proxy(renames["CsePrivateKeyMetadataOut"])
            ).optional(),
            "pkcs7": t.string().optional(),
            "pem": t.string().optional(),
            "keyPairId": t.string().optional(),
            "enablementState": t.string().optional(),
            "subjectEmailAddresses": t.array(t.string()).optional(),
            "disableTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CseKeyPairOut"])
    types["PopSettingsIn"] = t.struct(
        {"accessWindow": t.string().optional(), "disposition": t.string().optional()}
    ).named(renames["PopSettingsIn"])
    types["PopSettingsOut"] = t.struct(
        {
            "accessWindow": t.string().optional(),
            "disposition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PopSettingsOut"])
    types["ListMessagesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resultSizeEstimate": t.integer().optional(),
            "messages": t.array(t.proxy(renames["MessageIn"])).optional(),
        }
    ).named(renames["ListMessagesResponseIn"])
    types["ListMessagesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resultSizeEstimate": t.integer().optional(),
            "messages": t.array(t.proxy(renames["MessageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMessagesResponseOut"])
    types["ListDelegatesResponseIn"] = t.struct(
        {"delegates": t.array(t.proxy(renames["DelegateIn"])).optional()}
    ).named(renames["ListDelegatesResponseIn"])
    types["ListDelegatesResponseOut"] = t.struct(
        {
            "delegates": t.array(t.proxy(renames["DelegateOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDelegatesResponseOut"])
    types["SmimeInfoIn"] = t.struct(
        {
            "pem": t.string().optional(),
            "id": t.string().optional(),
            "expiration": t.string().optional(),
            "issuerCn": t.string().optional(),
            "isDefault": t.boolean().optional(),
            "encryptedKeyPassword": t.string().optional(),
            "pkcs12": t.string().optional(),
        }
    ).named(renames["SmimeInfoIn"])
    types["SmimeInfoOut"] = t.struct(
        {
            "pem": t.string().optional(),
            "id": t.string().optional(),
            "expiration": t.string().optional(),
            "issuerCn": t.string().optional(),
            "isDefault": t.boolean().optional(),
            "encryptedKeyPassword": t.string().optional(),
            "pkcs12": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SmimeInfoOut"])
    types["DisableCseKeyPairRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DisableCseKeyPairRequestIn"]
    )
    types["DisableCseKeyPairRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DisableCseKeyPairRequestOut"])
    types["ListSmimeInfoResponseIn"] = t.struct(
        {"smimeInfo": t.array(t.proxy(renames["SmimeInfoIn"])).optional()}
    ).named(renames["ListSmimeInfoResponseIn"])
    types["ListSmimeInfoResponseOut"] = t.struct(
        {
            "smimeInfo": t.array(t.proxy(renames["SmimeInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSmimeInfoResponseOut"])
    types["ListSendAsResponseIn"] = t.struct(
        {"sendAs": t.array(t.proxy(renames["SendAsIn"])).optional()}
    ).named(renames["ListSendAsResponseIn"])
    types["ListSendAsResponseOut"] = t.struct(
        {
            "sendAs": t.array(t.proxy(renames["SendAsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSendAsResponseOut"])
    types["EnableCseKeyPairRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EnableCseKeyPairRequestIn"]
    )
    types["EnableCseKeyPairRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EnableCseKeyPairRequestOut"])
    types["MessageIn"] = t.struct(
        {
            "sizeEstimate": t.integer().optional(),
            "threadId": t.string().optional(),
            "id": t.string().optional(),
            "historyId": t.string().optional(),
            "raw": t.string().optional(),
            "labelIds": t.array(t.string()).optional(),
            "payload": t.proxy(renames["MessagePartIn"]).optional(),
            "internalDate": t.string().optional(),
            "snippet": t.string().optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "sizeEstimate": t.integer().optional(),
            "threadId": t.string().optional(),
            "id": t.string().optional(),
            "historyId": t.string().optional(),
            "raw": t.string().optional(),
            "labelIds": t.array(t.string()).optional(),
            "payload": t.proxy(renames["MessagePartOut"]).optional(),
            "internalDate": t.string().optional(),
            "snippet": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["AutoForwardingIn"] = t.struct(
        {
            "emailAddress": t.string().optional(),
            "enabled": t.boolean().optional(),
            "disposition": t.string().optional(),
        }
    ).named(renames["AutoForwardingIn"])
    types["AutoForwardingOut"] = t.struct(
        {
            "emailAddress": t.string().optional(),
            "enabled": t.boolean().optional(),
            "disposition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoForwardingOut"])
    types["KaclsKeyMetadataIn"] = t.struct(
        {"kaclsData": t.string().optional(), "kaclsUri": t.string().optional()}
    ).named(renames["KaclsKeyMetadataIn"])
    types["KaclsKeyMetadataOut"] = t.struct(
        {
            "kaclsData": t.string().optional(),
            "kaclsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KaclsKeyMetadataOut"])
    types["FilterCriteriaIn"] = t.struct(
        {
            "from": t.string().optional(),
            "size": t.integer().optional(),
            "sizeComparison": t.string().optional(),
            "to": t.string().optional(),
            "negatedQuery": t.string().optional(),
            "subject": t.string().optional(),
            "query": t.string().optional(),
            "excludeChats": t.boolean().optional(),
            "hasAttachment": t.boolean().optional(),
        }
    ).named(renames["FilterCriteriaIn"])
    types["FilterCriteriaOut"] = t.struct(
        {
            "from": t.string().optional(),
            "size": t.integer().optional(),
            "sizeComparison": t.string().optional(),
            "to": t.string().optional(),
            "negatedQuery": t.string().optional(),
            "subject": t.string().optional(),
            "query": t.string().optional(),
            "excludeChats": t.boolean().optional(),
            "hasAttachment": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterCriteriaOut"])
    types["FilterActionIn"] = t.struct(
        {
            "removeLabelIds": t.array(t.string()).optional(),
            "forward": t.string().optional(),
            "addLabelIds": t.array(t.string()).optional(),
        }
    ).named(renames["FilterActionIn"])
    types["FilterActionOut"] = t.struct(
        {
            "removeLabelIds": t.array(t.string()).optional(),
            "forward": t.string().optional(),
            "addLabelIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterActionOut"])
    types["SmtpMsaIn"] = t.struct(
        {
            "password": t.string().optional(),
            "username": t.string().optional(),
            "host": t.string().optional(),
            "securityMode": t.string().optional(),
            "port": t.integer().optional(),
        }
    ).named(renames["SmtpMsaIn"])
    types["SmtpMsaOut"] = t.struct(
        {
            "password": t.string().optional(),
            "username": t.string().optional(),
            "host": t.string().optional(),
            "securityMode": t.string().optional(),
            "port": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SmtpMsaOut"])
    types["WatchRequestIn"] = t.struct(
        {
            "labelFilterAction": t.string().optional(),
            "topicName": t.string().optional(),
            "labelFilterBehavior": t.string().optional(),
            "labelIds": t.array(t.string()).optional(),
        }
    ).named(renames["WatchRequestIn"])
    types["WatchRequestOut"] = t.struct(
        {
            "labelFilterAction": t.string().optional(),
            "topicName": t.string().optional(),
            "labelFilterBehavior": t.string().optional(),
            "labelIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchRequestOut"])
    types["ListThreadsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "threads": t.array(t.proxy(renames["ThreadIn"])).optional(),
            "resultSizeEstimate": t.integer().optional(),
        }
    ).named(renames["ListThreadsResponseIn"])
    types["ListThreadsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "threads": t.array(t.proxy(renames["ThreadOut"])).optional(),
            "resultSizeEstimate": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListThreadsResponseOut"])
    types["ListForwardingAddressesResponseIn"] = t.struct(
        {
            "forwardingAddresses": t.array(
                t.proxy(renames["ForwardingAddressIn"])
            ).optional()
        }
    ).named(renames["ListForwardingAddressesResponseIn"])
    types["ListForwardingAddressesResponseOut"] = t.struct(
        {
            "forwardingAddresses": t.array(
                t.proxy(renames["ForwardingAddressOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListForwardingAddressesResponseOut"])
    types["ProfileIn"] = t.struct(
        {
            "historyId": t.string().optional(),
            "threadsTotal": t.integer().optional(),
            "messagesTotal": t.integer().optional(),
            "emailAddress": t.string().optional(),
        }
    ).named(renames["ProfileIn"])
    types["ProfileOut"] = t.struct(
        {
            "historyId": t.string().optional(),
            "threadsTotal": t.integer().optional(),
            "messagesTotal": t.integer().optional(),
            "emailAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileOut"])
    types["FilterIn"] = t.struct(
        {
            "id": t.string().optional(),
            "action": t.proxy(renames["FilterActionIn"]).optional(),
            "criteria": t.proxy(renames["FilterCriteriaIn"]).optional(),
        }
    ).named(renames["FilterIn"])
    types["FilterOut"] = t.struct(
        {
            "id": t.string().optional(),
            "action": t.proxy(renames["FilterActionOut"]).optional(),
            "criteria": t.proxy(renames["FilterCriteriaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])

    functions = {}
    functions["usersWatch"] = gmail.get(
        "gmail/v1/users/{userId}/profile",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersStop"] = gmail.get(
        "gmail/v1/users/{userId}/profile",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersGetProfile"] = gmail.get(
        "gmail/v1/users/{userId}/profile",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesSend"] = gmail.get(
        "gmail/v1/users/{userId}/messages",
        t.struct(
            {
                "labelIds": t.string().optional(),
                "userId": t.string().optional(),
                "includeSpamTrash": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "q": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMessagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesModify"] = gmail.get(
        "gmail/v1/users/{userId}/messages",
        t.struct(
            {
                "labelIds": t.string().optional(),
                "userId": t.string().optional(),
                "includeSpamTrash": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "q": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMessagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesImport"] = gmail.get(
        "gmail/v1/users/{userId}/messages",
        t.struct(
            {
                "labelIds": t.string().optional(),
                "userId": t.string().optional(),
                "includeSpamTrash": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "q": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMessagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesBatchDelete"] = gmail.get(
        "gmail/v1/users/{userId}/messages",
        t.struct(
            {
                "labelIds": t.string().optional(),
                "userId": t.string().optional(),
                "includeSpamTrash": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "q": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMessagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesUntrash"] = gmail.get(
        "gmail/v1/users/{userId}/messages",
        t.struct(
            {
                "labelIds": t.string().optional(),
                "userId": t.string().optional(),
                "includeSpamTrash": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "q": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMessagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesDelete"] = gmail.get(
        "gmail/v1/users/{userId}/messages",
        t.struct(
            {
                "labelIds": t.string().optional(),
                "userId": t.string().optional(),
                "includeSpamTrash": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "q": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMessagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesInsert"] = gmail.get(
        "gmail/v1/users/{userId}/messages",
        t.struct(
            {
                "labelIds": t.string().optional(),
                "userId": t.string().optional(),
                "includeSpamTrash": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "q": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMessagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesBatchModify"] = gmail.get(
        "gmail/v1/users/{userId}/messages",
        t.struct(
            {
                "labelIds": t.string().optional(),
                "userId": t.string().optional(),
                "includeSpamTrash": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "q": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMessagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesTrash"] = gmail.get(
        "gmail/v1/users/{userId}/messages",
        t.struct(
            {
                "labelIds": t.string().optional(),
                "userId": t.string().optional(),
                "includeSpamTrash": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "q": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMessagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesGet"] = gmail.get(
        "gmail/v1/users/{userId}/messages",
        t.struct(
            {
                "labelIds": t.string().optional(),
                "userId": t.string().optional(),
                "includeSpamTrash": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "q": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMessagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesList"] = gmail.get(
        "gmail/v1/users/{userId}/messages",
        t.struct(
            {
                "labelIds": t.string().optional(),
                "userId": t.string().optional(),
                "includeSpamTrash": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "q": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMessagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesAttachmentsGet"] = gmail.get(
        "gmail/v1/users/{userId}/messages/{messageId}/attachments/{id}",
        t.struct(
            {
                "userId": t.string().optional(),
                "messageId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessagePartBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersHistoryList"] = gmail.get(
        "gmail/v1/users/{userId}/history",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "userId": t.string().optional(),
                "pageToken": t.string().optional(),
                "labelId": t.string().optional(),
                "startHistoryId": t.string(),
                "historyTypes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListHistoryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersThreadsList"] = gmail.get(
        "gmail/v1/users/{userId}/threads/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "format": t.string().optional(),
                "metadataHeaders": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThreadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersThreadsDelete"] = gmail.get(
        "gmail/v1/users/{userId}/threads/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "format": t.string().optional(),
                "metadataHeaders": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThreadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersThreadsTrash"] = gmail.get(
        "gmail/v1/users/{userId}/threads/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "format": t.string().optional(),
                "metadataHeaders": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThreadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersThreadsModify"] = gmail.get(
        "gmail/v1/users/{userId}/threads/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "format": t.string().optional(),
                "metadataHeaders": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThreadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersThreadsUntrash"] = gmail.get(
        "gmail/v1/users/{userId}/threads/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "format": t.string().optional(),
                "metadataHeaders": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThreadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersThreadsGet"] = gmail.get(
        "gmail/v1/users/{userId}/threads/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "format": t.string().optional(),
                "metadataHeaders": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThreadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDraftsDelete"] = gmail.get(
        "gmail/v1/users/{userId}/drafts/{id}",
        t.struct(
            {
                "format": t.string().optional(),
                "userId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DraftOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDraftsSend"] = gmail.get(
        "gmail/v1/users/{userId}/drafts/{id}",
        t.struct(
            {
                "format": t.string().optional(),
                "userId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DraftOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDraftsList"] = gmail.get(
        "gmail/v1/users/{userId}/drafts/{id}",
        t.struct(
            {
                "format": t.string().optional(),
                "userId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DraftOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDraftsUpdate"] = gmail.get(
        "gmail/v1/users/{userId}/drafts/{id}",
        t.struct(
            {
                "format": t.string().optional(),
                "userId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DraftOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDraftsCreate"] = gmail.get(
        "gmail/v1/users/{userId}/drafts/{id}",
        t.struct(
            {
                "format": t.string().optional(),
                "userId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DraftOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDraftsGet"] = gmail.get(
        "gmail/v1/users/{userId}/drafts/{id}",
        t.struct(
            {
                "format": t.string().optional(),
                "userId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DraftOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsGetVacation"] = gmail.get(
        "gmail/v1/users/{userId}/settings/imap",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ImapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsGetLanguage"] = gmail.get(
        "gmail/v1/users/{userId}/settings/imap",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ImapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsUpdateAutoForwarding"] = gmail.get(
        "gmail/v1/users/{userId}/settings/imap",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ImapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsUpdateVacation"] = gmail.get(
        "gmail/v1/users/{userId}/settings/imap",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ImapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsGetPop"] = gmail.get(
        "gmail/v1/users/{userId}/settings/imap",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ImapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsUpdateImap"] = gmail.get(
        "gmail/v1/users/{userId}/settings/imap",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ImapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsUpdateLanguage"] = gmail.get(
        "gmail/v1/users/{userId}/settings/imap",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ImapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsGetAutoForwarding"] = gmail.get(
        "gmail/v1/users/{userId}/settings/imap",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ImapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsUpdatePop"] = gmail.get(
        "gmail/v1/users/{userId}/settings/imap",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ImapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsGetImap"] = gmail.get(
        "gmail/v1/users/{userId}/settings/imap",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ImapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsFiltersGet"] = gmail.get(
        "gmail/v1/users/{userId}/settings/filters",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ListFiltersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsFiltersCreate"] = gmail.get(
        "gmail/v1/users/{userId}/settings/filters",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ListFiltersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsFiltersDelete"] = gmail.get(
        "gmail/v1/users/{userId}/settings/filters",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ListFiltersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsFiltersList"] = gmail.get(
        "gmail/v1/users/{userId}/settings/filters",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ListFiltersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsDelegatesCreate"] = gmail.get(
        "gmail/v1/users/{userId}/settings/delegates",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ListDelegatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsDelegatesDelete"] = gmail.get(
        "gmail/v1/users/{userId}/settings/delegates",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ListDelegatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsDelegatesGet"] = gmail.get(
        "gmail/v1/users/{userId}/settings/delegates",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ListDelegatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsDelegatesList"] = gmail.get(
        "gmail/v1/users/{userId}/settings/delegates",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ListDelegatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsForwardingAddressesList"] = gmail.post(
        "gmail/v1/users/{userId}/settings/forwardingAddresses",
        t.struct(
            {
                "userId": t.string().optional(),
                "verificationStatus": t.string().optional(),
                "forwardingEmail": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ForwardingAddressOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsForwardingAddressesDelete"] = gmail.post(
        "gmail/v1/users/{userId}/settings/forwardingAddresses",
        t.struct(
            {
                "userId": t.string().optional(),
                "verificationStatus": t.string().optional(),
                "forwardingEmail": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ForwardingAddressOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsForwardingAddressesGet"] = gmail.post(
        "gmail/v1/users/{userId}/settings/forwardingAddresses",
        t.struct(
            {
                "userId": t.string().optional(),
                "verificationStatus": t.string().optional(),
                "forwardingEmail": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ForwardingAddressOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsForwardingAddressesCreate"] = gmail.post(
        "gmail/v1/users/{userId}/settings/forwardingAddresses",
        t.struct(
            {
                "userId": t.string().optional(),
                "verificationStatus": t.string().optional(),
                "forwardingEmail": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ForwardingAddressOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsUpdate"] = gmail.post(
        "gmail/v1/users/{userId}/settings/sendAs/{sendAsEmail}/verify",
        t.struct(
            {
                "sendAsEmail": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsList"] = gmail.post(
        "gmail/v1/users/{userId}/settings/sendAs/{sendAsEmail}/verify",
        t.struct(
            {
                "sendAsEmail": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsGet"] = gmail.post(
        "gmail/v1/users/{userId}/settings/sendAs/{sendAsEmail}/verify",
        t.struct(
            {
                "sendAsEmail": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsDelete"] = gmail.post(
        "gmail/v1/users/{userId}/settings/sendAs/{sendAsEmail}/verify",
        t.struct(
            {
                "sendAsEmail": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsPatch"] = gmail.post(
        "gmail/v1/users/{userId}/settings/sendAs/{sendAsEmail}/verify",
        t.struct(
            {
                "sendAsEmail": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsCreate"] = gmail.post(
        "gmail/v1/users/{userId}/settings/sendAs/{sendAsEmail}/verify",
        t.struct(
            {
                "sendAsEmail": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsVerify"] = gmail.post(
        "gmail/v1/users/{userId}/settings/sendAs/{sendAsEmail}/verify",
        t.struct(
            {
                "sendAsEmail": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsSmimeInfoInsert"] = gmail.get(
        "gmail/v1/users/{userId}/settings/sendAs/{sendAsEmail}/smimeInfo",
        t.struct(
            {
                "userId": t.string().optional(),
                "sendAsEmail": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSmimeInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsSmimeInfoGet"] = gmail.get(
        "gmail/v1/users/{userId}/settings/sendAs/{sendAsEmail}/smimeInfo",
        t.struct(
            {
                "userId": t.string().optional(),
                "sendAsEmail": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSmimeInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsSmimeInfoSetDefault"] = gmail.get(
        "gmail/v1/users/{userId}/settings/sendAs/{sendAsEmail}/smimeInfo",
        t.struct(
            {
                "userId": t.string().optional(),
                "sendAsEmail": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSmimeInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsSmimeInfoDelete"] = gmail.get(
        "gmail/v1/users/{userId}/settings/sendAs/{sendAsEmail}/smimeInfo",
        t.struct(
            {
                "userId": t.string().optional(),
                "sendAsEmail": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSmimeInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsSmimeInfoList"] = gmail.get(
        "gmail/v1/users/{userId}/settings/sendAs/{sendAsEmail}/smimeInfo",
        t.struct(
            {
                "userId": t.string().optional(),
                "sendAsEmail": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSmimeInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsCseIdentitiesPatch"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/cse/identities/{cseEmailAddress}",
        t.struct(
            {
                "cseEmailAddress": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsCseIdentitiesCreate"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/cse/identities/{cseEmailAddress}",
        t.struct(
            {
                "cseEmailAddress": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsCseIdentitiesList"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/cse/identities/{cseEmailAddress}",
        t.struct(
            {
                "cseEmailAddress": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsCseIdentitiesGet"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/cse/identities/{cseEmailAddress}",
        t.struct(
            {
                "cseEmailAddress": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsCseIdentitiesDelete"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/cse/identities/{cseEmailAddress}",
        t.struct(
            {
                "cseEmailAddress": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsCseKeypairsCreate"] = gmail.post(
        "gmail/v1/users/{userId}/settings/cse/keypairs/{keyPairId}:enable",
        t.struct(
            {
                "keyPairId": t.string().optional(),
                "userId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CseKeyPairOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsCseKeypairsObliterate"] = gmail.post(
        "gmail/v1/users/{userId}/settings/cse/keypairs/{keyPairId}:enable",
        t.struct(
            {
                "keyPairId": t.string().optional(),
                "userId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CseKeyPairOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsCseKeypairsDisable"] = gmail.post(
        "gmail/v1/users/{userId}/settings/cse/keypairs/{keyPairId}:enable",
        t.struct(
            {
                "keyPairId": t.string().optional(),
                "userId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CseKeyPairOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsCseKeypairsList"] = gmail.post(
        "gmail/v1/users/{userId}/settings/cse/keypairs/{keyPairId}:enable",
        t.struct(
            {
                "keyPairId": t.string().optional(),
                "userId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CseKeyPairOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsCseKeypairsGet"] = gmail.post(
        "gmail/v1/users/{userId}/settings/cse/keypairs/{keyPairId}:enable",
        t.struct(
            {
                "keyPairId": t.string().optional(),
                "userId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CseKeyPairOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsCseKeypairsEnable"] = gmail.post(
        "gmail/v1/users/{userId}/settings/cse/keypairs/{keyPairId}:enable",
        t.struct(
            {
                "keyPairId": t.string().optional(),
                "userId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CseKeyPairOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersLabelsUpdate"] = gmail.get(
        "gmail/v1/users/{userId}/labels",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ListLabelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersLabelsCreate"] = gmail.get(
        "gmail/v1/users/{userId}/labels",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ListLabelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersLabelsGet"] = gmail.get(
        "gmail/v1/users/{userId}/labels",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ListLabelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersLabelsPatch"] = gmail.get(
        "gmail/v1/users/{userId}/labels",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ListLabelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersLabelsDelete"] = gmail.get(
        "gmail/v1/users/{userId}/labels",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ListLabelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersLabelsList"] = gmail.get(
        "gmail/v1/users/{userId}/labels",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ListLabelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="gmail", renames=renames, types=Box(types), functions=Box(functions)
    )
