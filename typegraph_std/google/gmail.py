from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_gmail() -> Import:
    gmail = HTTPRuntime("https://gmail.googleapis.com/")

    renames = {
        "ErrorResponse": "_gmail_1_ErrorResponse",
        "ModifyThreadRequestIn": "_gmail_2_ModifyThreadRequestIn",
        "ModifyThreadRequestOut": "_gmail_3_ModifyThreadRequestOut",
        "ListDelegatesResponseIn": "_gmail_4_ListDelegatesResponseIn",
        "ListDelegatesResponseOut": "_gmail_5_ListDelegatesResponseOut",
        "DisableCseKeyPairRequestIn": "_gmail_6_DisableCseKeyPairRequestIn",
        "DisableCseKeyPairRequestOut": "_gmail_7_DisableCseKeyPairRequestOut",
        "BatchDeleteMessagesRequestIn": "_gmail_8_BatchDeleteMessagesRequestIn",
        "BatchDeleteMessagesRequestOut": "_gmail_9_BatchDeleteMessagesRequestOut",
        "MessageIn": "_gmail_10_MessageIn",
        "MessageOut": "_gmail_11_MessageOut",
        "VacationSettingsIn": "_gmail_12_VacationSettingsIn",
        "VacationSettingsOut": "_gmail_13_VacationSettingsOut",
        "FilterIn": "_gmail_14_FilterIn",
        "FilterOut": "_gmail_15_FilterOut",
        "ListThreadsResponseIn": "_gmail_16_ListThreadsResponseIn",
        "ListThreadsResponseOut": "_gmail_17_ListThreadsResponseOut",
        "LabelIn": "_gmail_18_LabelIn",
        "LabelOut": "_gmail_19_LabelOut",
        "ListLabelsResponseIn": "_gmail_20_ListLabelsResponseIn",
        "ListLabelsResponseOut": "_gmail_21_ListLabelsResponseOut",
        "ForwardingAddressIn": "_gmail_22_ForwardingAddressIn",
        "ForwardingAddressOut": "_gmail_23_ForwardingAddressOut",
        "WatchResponseIn": "_gmail_24_WatchResponseIn",
        "WatchResponseOut": "_gmail_25_WatchResponseOut",
        "BatchModifyMessagesRequestIn": "_gmail_26_BatchModifyMessagesRequestIn",
        "BatchModifyMessagesRequestOut": "_gmail_27_BatchModifyMessagesRequestOut",
        "LanguageSettingsIn": "_gmail_28_LanguageSettingsIn",
        "LanguageSettingsOut": "_gmail_29_LanguageSettingsOut",
        "EnableCseKeyPairRequestIn": "_gmail_30_EnableCseKeyPairRequestIn",
        "EnableCseKeyPairRequestOut": "_gmail_31_EnableCseKeyPairRequestOut",
        "SmtpMsaIn": "_gmail_32_SmtpMsaIn",
        "SmtpMsaOut": "_gmail_33_SmtpMsaOut",
        "HistoryMessageAddedIn": "_gmail_34_HistoryMessageAddedIn",
        "HistoryMessageAddedOut": "_gmail_35_HistoryMessageAddedOut",
        "WatchRequestIn": "_gmail_36_WatchRequestIn",
        "WatchRequestOut": "_gmail_37_WatchRequestOut",
        "MessagePartBodyIn": "_gmail_38_MessagePartBodyIn",
        "MessagePartBodyOut": "_gmail_39_MessagePartBodyOut",
        "CseIdentityIn": "_gmail_40_CseIdentityIn",
        "CseIdentityOut": "_gmail_41_CseIdentityOut",
        "MessagePartIn": "_gmail_42_MessagePartIn",
        "MessagePartOut": "_gmail_43_MessagePartOut",
        "ListDraftsResponseIn": "_gmail_44_ListDraftsResponseIn",
        "ListDraftsResponseOut": "_gmail_45_ListDraftsResponseOut",
        "ListCseKeyPairsResponseIn": "_gmail_46_ListCseKeyPairsResponseIn",
        "ListCseKeyPairsResponseOut": "_gmail_47_ListCseKeyPairsResponseOut",
        "ListCseIdentitiesResponseIn": "_gmail_48_ListCseIdentitiesResponseIn",
        "ListCseIdentitiesResponseOut": "_gmail_49_ListCseIdentitiesResponseOut",
        "DelegateIn": "_gmail_50_DelegateIn",
        "DelegateOut": "_gmail_51_DelegateOut",
        "AutoForwardingIn": "_gmail_52_AutoForwardingIn",
        "AutoForwardingOut": "_gmail_53_AutoForwardingOut",
        "HistoryLabelRemovedIn": "_gmail_54_HistoryLabelRemovedIn",
        "HistoryLabelRemovedOut": "_gmail_55_HistoryLabelRemovedOut",
        "MessagePartHeaderIn": "_gmail_56_MessagePartHeaderIn",
        "MessagePartHeaderOut": "_gmail_57_MessagePartHeaderOut",
        "ListFiltersResponseIn": "_gmail_58_ListFiltersResponseIn",
        "ListFiltersResponseOut": "_gmail_59_ListFiltersResponseOut",
        "ThreadIn": "_gmail_60_ThreadIn",
        "ThreadOut": "_gmail_61_ThreadOut",
        "ModifyMessageRequestIn": "_gmail_62_ModifyMessageRequestIn",
        "ModifyMessageRequestOut": "_gmail_63_ModifyMessageRequestOut",
        "KaclsKeyMetadataIn": "_gmail_64_KaclsKeyMetadataIn",
        "KaclsKeyMetadataOut": "_gmail_65_KaclsKeyMetadataOut",
        "ListForwardingAddressesResponseIn": "_gmail_66_ListForwardingAddressesResponseIn",
        "ListForwardingAddressesResponseOut": "_gmail_67_ListForwardingAddressesResponseOut",
        "ListSendAsResponseIn": "_gmail_68_ListSendAsResponseIn",
        "ListSendAsResponseOut": "_gmail_69_ListSendAsResponseOut",
        "CsePrivateKeyMetadataIn": "_gmail_70_CsePrivateKeyMetadataIn",
        "CsePrivateKeyMetadataOut": "_gmail_71_CsePrivateKeyMetadataOut",
        "ProfileIn": "_gmail_72_ProfileIn",
        "ProfileOut": "_gmail_73_ProfileOut",
        "LabelColorIn": "_gmail_74_LabelColorIn",
        "LabelColorOut": "_gmail_75_LabelColorOut",
        "ListMessagesResponseIn": "_gmail_76_ListMessagesResponseIn",
        "ListMessagesResponseOut": "_gmail_77_ListMessagesResponseOut",
        "FilterCriteriaIn": "_gmail_78_FilterCriteriaIn",
        "FilterCriteriaOut": "_gmail_79_FilterCriteriaOut",
        "FilterActionIn": "_gmail_80_FilterActionIn",
        "FilterActionOut": "_gmail_81_FilterActionOut",
        "ObliterateCseKeyPairRequestIn": "_gmail_82_ObliterateCseKeyPairRequestIn",
        "ObliterateCseKeyPairRequestOut": "_gmail_83_ObliterateCseKeyPairRequestOut",
        "SmimeInfoIn": "_gmail_84_SmimeInfoIn",
        "SmimeInfoOut": "_gmail_85_SmimeInfoOut",
        "HistoryLabelAddedIn": "_gmail_86_HistoryLabelAddedIn",
        "HistoryLabelAddedOut": "_gmail_87_HistoryLabelAddedOut",
        "HistoryMessageDeletedIn": "_gmail_88_HistoryMessageDeletedIn",
        "HistoryMessageDeletedOut": "_gmail_89_HistoryMessageDeletedOut",
        "SendAsIn": "_gmail_90_SendAsIn",
        "SendAsOut": "_gmail_91_SendAsOut",
        "CseKeyPairIn": "_gmail_92_CseKeyPairIn",
        "CseKeyPairOut": "_gmail_93_CseKeyPairOut",
        "DraftIn": "_gmail_94_DraftIn",
        "DraftOut": "_gmail_95_DraftOut",
        "HistoryIn": "_gmail_96_HistoryIn",
        "HistoryOut": "_gmail_97_HistoryOut",
        "PopSettingsIn": "_gmail_98_PopSettingsIn",
        "PopSettingsOut": "_gmail_99_PopSettingsOut",
        "ListSmimeInfoResponseIn": "_gmail_100_ListSmimeInfoResponseIn",
        "ListSmimeInfoResponseOut": "_gmail_101_ListSmimeInfoResponseOut",
        "ImapSettingsIn": "_gmail_102_ImapSettingsIn",
        "ImapSettingsOut": "_gmail_103_ImapSettingsOut",
        "ListHistoryResponseIn": "_gmail_104_ListHistoryResponseIn",
        "ListHistoryResponseOut": "_gmail_105_ListHistoryResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ModifyThreadRequestIn"] = t.struct(
        {
            "addLabelIds": t.array(t.string()).optional(),
            "removeLabelIds": t.array(t.string()).optional(),
        }
    ).named(renames["ModifyThreadRequestIn"])
    types["ModifyThreadRequestOut"] = t.struct(
        {
            "addLabelIds": t.array(t.string()).optional(),
            "removeLabelIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyThreadRequestOut"])
    types["ListDelegatesResponseIn"] = t.struct(
        {"delegates": t.array(t.proxy(renames["DelegateIn"])).optional()}
    ).named(renames["ListDelegatesResponseIn"])
    types["ListDelegatesResponseOut"] = t.struct(
        {
            "delegates": t.array(t.proxy(renames["DelegateOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDelegatesResponseOut"])
    types["DisableCseKeyPairRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DisableCseKeyPairRequestIn"]
    )
    types["DisableCseKeyPairRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DisableCseKeyPairRequestOut"])
    types["BatchDeleteMessagesRequestIn"] = t.struct(
        {"ids": t.array(t.string()).optional()}
    ).named(renames["BatchDeleteMessagesRequestIn"])
    types["BatchDeleteMessagesRequestOut"] = t.struct(
        {
            "ids": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteMessagesRequestOut"])
    types["MessageIn"] = t.struct(
        {
            "labelIds": t.array(t.string()).optional(),
            "historyId": t.string().optional(),
            "internalDate": t.string().optional(),
            "threadId": t.string().optional(),
            "raw": t.string().optional(),
            "payload": t.proxy(renames["MessagePartIn"]).optional(),
            "sizeEstimate": t.integer().optional(),
            "snippet": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "labelIds": t.array(t.string()).optional(),
            "historyId": t.string().optional(),
            "internalDate": t.string().optional(),
            "threadId": t.string().optional(),
            "raw": t.string().optional(),
            "payload": t.proxy(renames["MessagePartOut"]).optional(),
            "sizeEstimate": t.integer().optional(),
            "snippet": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["VacationSettingsIn"] = t.struct(
        {
            "responseBodyHtml": t.string().optional(),
            "restrictToContacts": t.boolean().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "responseSubject": t.string().optional(),
            "restrictToDomain": t.boolean().optional(),
            "enableAutoReply": t.boolean().optional(),
            "responseBodyPlainText": t.string().optional(),
        }
    ).named(renames["VacationSettingsIn"])
    types["VacationSettingsOut"] = t.struct(
        {
            "responseBodyHtml": t.string().optional(),
            "restrictToContacts": t.boolean().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "responseSubject": t.string().optional(),
            "restrictToDomain": t.boolean().optional(),
            "enableAutoReply": t.boolean().optional(),
            "responseBodyPlainText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VacationSettingsOut"])
    types["FilterIn"] = t.struct(
        {
            "criteria": t.proxy(renames["FilterCriteriaIn"]).optional(),
            "id": t.string().optional(),
            "action": t.proxy(renames["FilterActionIn"]).optional(),
        }
    ).named(renames["FilterIn"])
    types["FilterOut"] = t.struct(
        {
            "criteria": t.proxy(renames["FilterCriteriaOut"]).optional(),
            "id": t.string().optional(),
            "action": t.proxy(renames["FilterActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])
    types["ListThreadsResponseIn"] = t.struct(
        {
            "resultSizeEstimate": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "threads": t.array(t.proxy(renames["ThreadIn"])).optional(),
        }
    ).named(renames["ListThreadsResponseIn"])
    types["ListThreadsResponseOut"] = t.struct(
        {
            "resultSizeEstimate": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "threads": t.array(t.proxy(renames["ThreadOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListThreadsResponseOut"])
    types["LabelIn"] = t.struct(
        {
            "messageListVisibility": t.string().optional(),
            "messagesUnread": t.integer().optional(),
            "labelListVisibility": t.string().optional(),
            "type": t.string().optional(),
            "threadsTotal": t.integer().optional(),
            "threadsUnread": t.integer().optional(),
            "color": t.proxy(renames["LabelColorIn"]).optional(),
            "name": t.string().optional(),
            "messagesTotal": t.integer().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["LabelIn"])
    types["LabelOut"] = t.struct(
        {
            "messageListVisibility": t.string().optional(),
            "messagesUnread": t.integer().optional(),
            "labelListVisibility": t.string().optional(),
            "type": t.string().optional(),
            "threadsTotal": t.integer().optional(),
            "threadsUnread": t.integer().optional(),
            "color": t.proxy(renames["LabelColorOut"]).optional(),
            "name": t.string().optional(),
            "messagesTotal": t.integer().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelOut"])
    types["ListLabelsResponseIn"] = t.struct(
        {"labels": t.array(t.proxy(renames["LabelIn"])).optional()}
    ).named(renames["ListLabelsResponseIn"])
    types["ListLabelsResponseOut"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLabelsResponseOut"])
    types["ForwardingAddressIn"] = t.struct(
        {
            "forwardingEmail": t.string().optional(),
            "verificationStatus": t.string().optional(),
        }
    ).named(renames["ForwardingAddressIn"])
    types["ForwardingAddressOut"] = t.struct(
        {
            "forwardingEmail": t.string().optional(),
            "verificationStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForwardingAddressOut"])
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
    types["BatchModifyMessagesRequestIn"] = t.struct(
        {
            "removeLabelIds": t.array(t.string()).optional(),
            "addLabelIds": t.array(t.string()).optional(),
            "ids": t.array(t.string()).optional(),
        }
    ).named(renames["BatchModifyMessagesRequestIn"])
    types["BatchModifyMessagesRequestOut"] = t.struct(
        {
            "removeLabelIds": t.array(t.string()).optional(),
            "addLabelIds": t.array(t.string()).optional(),
            "ids": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchModifyMessagesRequestOut"])
    types["LanguageSettingsIn"] = t.struct(
        {"displayLanguage": t.string().optional()}
    ).named(renames["LanguageSettingsIn"])
    types["LanguageSettingsOut"] = t.struct(
        {
            "displayLanguage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageSettingsOut"])
    types["EnableCseKeyPairRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EnableCseKeyPairRequestIn"]
    )
    types["EnableCseKeyPairRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EnableCseKeyPairRequestOut"])
    types["SmtpMsaIn"] = t.struct(
        {
            "port": t.integer().optional(),
            "password": t.string().optional(),
            "username": t.string().optional(),
            "host": t.string().optional(),
            "securityMode": t.string().optional(),
        }
    ).named(renames["SmtpMsaIn"])
    types["SmtpMsaOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "password": t.string().optional(),
            "username": t.string().optional(),
            "host": t.string().optional(),
            "securityMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SmtpMsaOut"])
    types["HistoryMessageAddedIn"] = t.struct(
        {"message": t.proxy(renames["MessageIn"])}
    ).named(renames["HistoryMessageAddedIn"])
    types["HistoryMessageAddedOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryMessageAddedOut"])
    types["WatchRequestIn"] = t.struct(
        {
            "topicName": t.string().optional(),
            "labelFilterAction": t.string().optional(),
            "labelIds": t.array(t.string()).optional(),
        }
    ).named(renames["WatchRequestIn"])
    types["WatchRequestOut"] = t.struct(
        {
            "topicName": t.string().optional(),
            "labelFilterAction": t.string().optional(),
            "labelIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchRequestOut"])
    types["MessagePartBodyIn"] = t.struct(
        {
            "attachmentId": t.string().optional(),
            "data": t.string().optional(),
            "size": t.integer().optional(),
        }
    ).named(renames["MessagePartBodyIn"])
    types["MessagePartBodyOut"] = t.struct(
        {
            "attachmentId": t.string().optional(),
            "data": t.string().optional(),
            "size": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessagePartBodyOut"])
    types["CseIdentityIn"] = t.struct(
        {
            "primaryKeyPairId": t.string().optional(),
            "emailAddress": t.string().optional(),
        }
    ).named(renames["CseIdentityIn"])
    types["CseIdentityOut"] = t.struct(
        {
            "primaryKeyPairId": t.string().optional(),
            "emailAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CseIdentityOut"])
    types["MessagePartIn"] = t.struct(
        {
            "body": t.proxy(renames["MessagePartBodyIn"]).optional(),
            "filename": t.string().optional(),
            "partId": t.string().optional(),
            "mimeType": t.string().optional(),
            "parts": t.array(t.proxy(renames["MessagePartIn"])).optional(),
            "headers": t.array(t.proxy(renames["MessagePartHeaderIn"])).optional(),
        }
    ).named(renames["MessagePartIn"])
    types["MessagePartOut"] = t.struct(
        {
            "body": t.proxy(renames["MessagePartBodyOut"]).optional(),
            "filename": t.string().optional(),
            "partId": t.string().optional(),
            "mimeType": t.string().optional(),
            "parts": t.array(t.proxy(renames["MessagePartOut"])).optional(),
            "headers": t.array(t.proxy(renames["MessagePartHeaderOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessagePartOut"])
    types["ListDraftsResponseIn"] = t.struct(
        {
            "resultSizeEstimate": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "drafts": t.array(t.proxy(renames["DraftIn"])).optional(),
        }
    ).named(renames["ListDraftsResponseIn"])
    types["ListDraftsResponseOut"] = t.struct(
        {
            "resultSizeEstimate": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "drafts": t.array(t.proxy(renames["DraftOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDraftsResponseOut"])
    types["ListCseKeyPairsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "cseKeyPairs": t.array(t.proxy(renames["CseKeyPairIn"])).optional(),
        }
    ).named(renames["ListCseKeyPairsResponseIn"])
    types["ListCseKeyPairsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "cseKeyPairs": t.array(t.proxy(renames["CseKeyPairOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCseKeyPairsResponseOut"])
    types["ListCseIdentitiesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "cseIdentities": t.array(t.proxy(renames["CseIdentityIn"])).optional(),
        }
    ).named(renames["ListCseIdentitiesResponseIn"])
    types["ListCseIdentitiesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "cseIdentities": t.array(t.proxy(renames["CseIdentityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCseIdentitiesResponseOut"])
    types["DelegateIn"] = t.struct(
        {
            "delegateEmail": t.string().optional(),
            "verificationStatus": t.string().optional(),
        }
    ).named(renames["DelegateIn"])
    types["DelegateOut"] = t.struct(
        {
            "delegateEmail": t.string().optional(),
            "verificationStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DelegateOut"])
    types["AutoForwardingIn"] = t.struct(
        {
            "disposition": t.string().optional(),
            "enabled": t.boolean().optional(),
            "emailAddress": t.string().optional(),
        }
    ).named(renames["AutoForwardingIn"])
    types["AutoForwardingOut"] = t.struct(
        {
            "disposition": t.string().optional(),
            "enabled": t.boolean().optional(),
            "emailAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoForwardingOut"])
    types["HistoryLabelRemovedIn"] = t.struct(
        {
            "labelIds": t.array(t.string()).optional(),
            "message": t.proxy(renames["MessageIn"]),
        }
    ).named(renames["HistoryLabelRemovedIn"])
    types["HistoryLabelRemovedOut"] = t.struct(
        {
            "labelIds": t.array(t.string()).optional(),
            "message": t.proxy(renames["MessageOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryLabelRemovedOut"])
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
    types["ListFiltersResponseIn"] = t.struct(
        {"filter": t.array(t.proxy(renames["FilterIn"])).optional()}
    ).named(renames["ListFiltersResponseIn"])
    types["ListFiltersResponseOut"] = t.struct(
        {
            "filter": t.array(t.proxy(renames["FilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFiltersResponseOut"])
    types["ThreadIn"] = t.struct(
        {
            "messages": t.array(t.proxy(renames["MessageIn"])).optional(),
            "snippet": t.string().optional(),
            "id": t.string().optional(),
            "historyId": t.string().optional(),
        }
    ).named(renames["ThreadIn"])
    types["ThreadOut"] = t.struct(
        {
            "messages": t.array(t.proxy(renames["MessageOut"])).optional(),
            "snippet": t.string().optional(),
            "id": t.string().optional(),
            "historyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThreadOut"])
    types["ModifyMessageRequestIn"] = t.struct(
        {
            "addLabelIds": t.array(t.string()).optional(),
            "removeLabelIds": t.array(t.string()).optional(),
        }
    ).named(renames["ModifyMessageRequestIn"])
    types["ModifyMessageRequestOut"] = t.struct(
        {
            "addLabelIds": t.array(t.string()).optional(),
            "removeLabelIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyMessageRequestOut"])
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
    types["ListSendAsResponseIn"] = t.struct(
        {"sendAs": t.array(t.proxy(renames["SendAsIn"])).optional()}
    ).named(renames["ListSendAsResponseIn"])
    types["ListSendAsResponseOut"] = t.struct(
        {
            "sendAs": t.array(t.proxy(renames["SendAsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSendAsResponseOut"])
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
    types["ProfileIn"] = t.struct(
        {
            "threadsTotal": t.integer().optional(),
            "emailAddress": t.string().optional(),
            "historyId": t.string().optional(),
            "messagesTotal": t.integer().optional(),
        }
    ).named(renames["ProfileIn"])
    types["ProfileOut"] = t.struct(
        {
            "threadsTotal": t.integer().optional(),
            "emailAddress": t.string().optional(),
            "historyId": t.string().optional(),
            "messagesTotal": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileOut"])
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
    types["ListMessagesResponseIn"] = t.struct(
        {
            "resultSizeEstimate": t.integer().optional(),
            "messages": t.array(t.proxy(renames["MessageIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListMessagesResponseIn"])
    types["ListMessagesResponseOut"] = t.struct(
        {
            "resultSizeEstimate": t.integer().optional(),
            "messages": t.array(t.proxy(renames["MessageOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMessagesResponseOut"])
    types["FilterCriteriaIn"] = t.struct(
        {
            "sizeComparison": t.string().optional(),
            "query": t.string().optional(),
            "negatedQuery": t.string().optional(),
            "from": t.string().optional(),
            "hasAttachment": t.boolean().optional(),
            "excludeChats": t.boolean().optional(),
            "to": t.string().optional(),
            "size": t.integer().optional(),
            "subject": t.string().optional(),
        }
    ).named(renames["FilterCriteriaIn"])
    types["FilterCriteriaOut"] = t.struct(
        {
            "sizeComparison": t.string().optional(),
            "query": t.string().optional(),
            "negatedQuery": t.string().optional(),
            "from": t.string().optional(),
            "hasAttachment": t.boolean().optional(),
            "excludeChats": t.boolean().optional(),
            "to": t.string().optional(),
            "size": t.integer().optional(),
            "subject": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterCriteriaOut"])
    types["FilterActionIn"] = t.struct(
        {
            "addLabelIds": t.array(t.string()).optional(),
            "forward": t.string().optional(),
            "removeLabelIds": t.array(t.string()).optional(),
        }
    ).named(renames["FilterActionIn"])
    types["FilterActionOut"] = t.struct(
        {
            "addLabelIds": t.array(t.string()).optional(),
            "forward": t.string().optional(),
            "removeLabelIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterActionOut"])
    types["ObliterateCseKeyPairRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ObliterateCseKeyPairRequestIn"])
    types["ObliterateCseKeyPairRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ObliterateCseKeyPairRequestOut"])
    types["SmimeInfoIn"] = t.struct(
        {
            "pkcs12": t.string().optional(),
            "expiration": t.string().optional(),
            "isDefault": t.boolean().optional(),
            "id": t.string().optional(),
            "issuerCn": t.string().optional(),
            "pem": t.string().optional(),
            "encryptedKeyPassword": t.string().optional(),
        }
    ).named(renames["SmimeInfoIn"])
    types["SmimeInfoOut"] = t.struct(
        {
            "pkcs12": t.string().optional(),
            "expiration": t.string().optional(),
            "isDefault": t.boolean().optional(),
            "id": t.string().optional(),
            "issuerCn": t.string().optional(),
            "pem": t.string().optional(),
            "encryptedKeyPassword": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SmimeInfoOut"])
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
    types["HistoryMessageDeletedIn"] = t.struct(
        {"message": t.proxy(renames["MessageIn"])}
    ).named(renames["HistoryMessageDeletedIn"])
    types["HistoryMessageDeletedOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryMessageDeletedOut"])
    types["SendAsIn"] = t.struct(
        {
            "isDefault": t.boolean().optional(),
            "treatAsAlias": t.boolean().optional(),
            "sendAsEmail": t.string().optional(),
            "smtpMsa": t.proxy(renames["SmtpMsaIn"]).optional(),
            "signature": t.string().optional(),
            "isPrimary": t.boolean().optional(),
            "replyToAddress": t.string().optional(),
            "verificationStatus": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["SendAsIn"])
    types["SendAsOut"] = t.struct(
        {
            "isDefault": t.boolean().optional(),
            "treatAsAlias": t.boolean().optional(),
            "sendAsEmail": t.string().optional(),
            "smtpMsa": t.proxy(renames["SmtpMsaOut"]).optional(),
            "signature": t.string().optional(),
            "isPrimary": t.boolean().optional(),
            "replyToAddress": t.string().optional(),
            "verificationStatus": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SendAsOut"])
    types["CseKeyPairIn"] = t.struct(
        {
            "pkcs7": t.string().optional(),
            "privateKeyMetadata": t.array(
                t.proxy(renames["CsePrivateKeyMetadataIn"])
            ).optional(),
        }
    ).named(renames["CseKeyPairIn"])
    types["CseKeyPairOut"] = t.struct(
        {
            "pem": t.string().optional(),
            "keyPairId": t.string().optional(),
            "pkcs7": t.string().optional(),
            "subjectEmailAddresses": t.array(t.string()).optional(),
            "privateKeyMetadata": t.array(
                t.proxy(renames["CsePrivateKeyMetadataOut"])
            ).optional(),
            "disableTime": t.string().optional(),
            "enablementState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CseKeyPairOut"])
    types["DraftIn"] = t.struct(
        {
            "message": t.proxy(renames["MessageIn"]).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["DraftIn"])
    types["DraftOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DraftOut"])
    types["HistoryIn"] = t.struct(
        {
            "id": t.string().optional(),
            "messages": t.array(t.proxy(renames["MessageIn"])).optional(),
            "labelsAdded": t.array(t.proxy(renames["HistoryLabelAddedIn"])).optional(),
            "messagesDeleted": t.array(
                t.proxy(renames["HistoryMessageDeletedIn"])
            ).optional(),
            "labelsRemoved": t.array(
                t.proxy(renames["HistoryLabelRemovedIn"])
            ).optional(),
            "messagesAdded": t.array(
                t.proxy(renames["HistoryMessageAddedIn"])
            ).optional(),
        }
    ).named(renames["HistoryIn"])
    types["HistoryOut"] = t.struct(
        {
            "id": t.string().optional(),
            "messages": t.array(t.proxy(renames["MessageOut"])).optional(),
            "labelsAdded": t.array(t.proxy(renames["HistoryLabelAddedOut"])).optional(),
            "messagesDeleted": t.array(
                t.proxy(renames["HistoryMessageDeletedOut"])
            ).optional(),
            "labelsRemoved": t.array(
                t.proxy(renames["HistoryLabelRemovedOut"])
            ).optional(),
            "messagesAdded": t.array(
                t.proxy(renames["HistoryMessageAddedOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryOut"])
    types["PopSettingsIn"] = t.struct(
        {"disposition": t.string().optional(), "accessWindow": t.string().optional()}
    ).named(renames["PopSettingsIn"])
    types["PopSettingsOut"] = t.struct(
        {
            "disposition": t.string().optional(),
            "accessWindow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PopSettingsOut"])
    types["ListSmimeInfoResponseIn"] = t.struct(
        {"smimeInfo": t.array(t.proxy(renames["SmimeInfoIn"])).optional()}
    ).named(renames["ListSmimeInfoResponseIn"])
    types["ListSmimeInfoResponseOut"] = t.struct(
        {
            "smimeInfo": t.array(t.proxy(renames["SmimeInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSmimeInfoResponseOut"])
    types["ImapSettingsIn"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "maxFolderSize": t.integer().optional(),
            "autoExpunge": t.boolean().optional(),
            "expungeBehavior": t.string().optional(),
        }
    ).named(renames["ImapSettingsIn"])
    types["ImapSettingsOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "maxFolderSize": t.integer().optional(),
            "autoExpunge": t.boolean().optional(),
            "expungeBehavior": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImapSettingsOut"])
    types["ListHistoryResponseIn"] = t.struct(
        {
            "history": t.array(t.proxy(renames["HistoryIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "historyId": t.string().optional(),
        }
    ).named(renames["ListHistoryResponseIn"])
    types["ListHistoryResponseOut"] = t.struct(
        {
            "history": t.array(t.proxy(renames["HistoryOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "historyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListHistoryResponseOut"])

    functions = {}
    functions["usersGetProfile"] = gmail.post(
        "gmail/v1/users/{userId}/watch",
        t.struct(
            {
                "userId": t.string().optional(),
                "topicName": t.string().optional(),
                "labelFilterAction": t.string().optional(),
                "labelIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersStop"] = gmail.post(
        "gmail/v1/users/{userId}/watch",
        t.struct(
            {
                "userId": t.string().optional(),
                "topicName": t.string().optional(),
                "labelFilterAction": t.string().optional(),
                "labelIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersWatch"] = gmail.post(
        "gmail/v1/users/{userId}/watch",
        t.struct(
            {
                "userId": t.string().optional(),
                "topicName": t.string().optional(),
                "labelFilterAction": t.string().optional(),
                "labelIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDraftsDelete"] = gmail.put(
        "gmail/v1/users/{userId}/drafts/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "message": t.proxy(renames["MessageIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DraftOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDraftsCreate"] = gmail.put(
        "gmail/v1/users/{userId}/drafts/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "message": t.proxy(renames["MessageIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DraftOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDraftsGet"] = gmail.put(
        "gmail/v1/users/{userId}/drafts/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "message": t.proxy(renames["MessageIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DraftOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDraftsSend"] = gmail.put(
        "gmail/v1/users/{userId}/drafts/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "message": t.proxy(renames["MessageIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DraftOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDraftsList"] = gmail.put(
        "gmail/v1/users/{userId}/drafts/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "message": t.proxy(renames["MessageIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DraftOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDraftsUpdate"] = gmail.put(
        "gmail/v1/users/{userId}/drafts/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "message": t.proxy(renames["MessageIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DraftOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersThreadsList"] = gmail.post(
        "gmail/v1/users/{userId}/threads/{id}/untrash",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThreadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersThreadsDelete"] = gmail.post(
        "gmail/v1/users/{userId}/threads/{id}/untrash",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThreadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersThreadsTrash"] = gmail.post(
        "gmail/v1/users/{userId}/threads/{id}/untrash",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThreadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersThreadsGet"] = gmail.post(
        "gmail/v1/users/{userId}/threads/{id}/untrash",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThreadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersThreadsModify"] = gmail.post(
        "gmail/v1/users/{userId}/threads/{id}/untrash",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThreadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersThreadsUntrash"] = gmail.post(
        "gmail/v1/users/{userId}/threads/{id}/untrash",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ThreadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesBatchDelete"] = gmail.post(
        "gmail/v1/users/{userId}/messages/send",
        t.struct(
            {
                "userId": t.string().optional(),
                "labelIds": t.array(t.string()).optional(),
                "historyId": t.string().optional(),
                "internalDate": t.string().optional(),
                "threadId": t.string().optional(),
                "raw": t.string().optional(),
                "payload": t.proxy(renames["MessagePartIn"]).optional(),
                "sizeEstimate": t.integer().optional(),
                "snippet": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesTrash"] = gmail.post(
        "gmail/v1/users/{userId}/messages/send",
        t.struct(
            {
                "userId": t.string().optional(),
                "labelIds": t.array(t.string()).optional(),
                "historyId": t.string().optional(),
                "internalDate": t.string().optional(),
                "threadId": t.string().optional(),
                "raw": t.string().optional(),
                "payload": t.proxy(renames["MessagePartIn"]).optional(),
                "sizeEstimate": t.integer().optional(),
                "snippet": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesInsert"] = gmail.post(
        "gmail/v1/users/{userId}/messages/send",
        t.struct(
            {
                "userId": t.string().optional(),
                "labelIds": t.array(t.string()).optional(),
                "historyId": t.string().optional(),
                "internalDate": t.string().optional(),
                "threadId": t.string().optional(),
                "raw": t.string().optional(),
                "payload": t.proxy(renames["MessagePartIn"]).optional(),
                "sizeEstimate": t.integer().optional(),
                "snippet": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesDelete"] = gmail.post(
        "gmail/v1/users/{userId}/messages/send",
        t.struct(
            {
                "userId": t.string().optional(),
                "labelIds": t.array(t.string()).optional(),
                "historyId": t.string().optional(),
                "internalDate": t.string().optional(),
                "threadId": t.string().optional(),
                "raw": t.string().optional(),
                "payload": t.proxy(renames["MessagePartIn"]).optional(),
                "sizeEstimate": t.integer().optional(),
                "snippet": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesList"] = gmail.post(
        "gmail/v1/users/{userId}/messages/send",
        t.struct(
            {
                "userId": t.string().optional(),
                "labelIds": t.array(t.string()).optional(),
                "historyId": t.string().optional(),
                "internalDate": t.string().optional(),
                "threadId": t.string().optional(),
                "raw": t.string().optional(),
                "payload": t.proxy(renames["MessagePartIn"]).optional(),
                "sizeEstimate": t.integer().optional(),
                "snippet": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesModify"] = gmail.post(
        "gmail/v1/users/{userId}/messages/send",
        t.struct(
            {
                "userId": t.string().optional(),
                "labelIds": t.array(t.string()).optional(),
                "historyId": t.string().optional(),
                "internalDate": t.string().optional(),
                "threadId": t.string().optional(),
                "raw": t.string().optional(),
                "payload": t.proxy(renames["MessagePartIn"]).optional(),
                "sizeEstimate": t.integer().optional(),
                "snippet": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesImport"] = gmail.post(
        "gmail/v1/users/{userId}/messages/send",
        t.struct(
            {
                "userId": t.string().optional(),
                "labelIds": t.array(t.string()).optional(),
                "historyId": t.string().optional(),
                "internalDate": t.string().optional(),
                "threadId": t.string().optional(),
                "raw": t.string().optional(),
                "payload": t.proxy(renames["MessagePartIn"]).optional(),
                "sizeEstimate": t.integer().optional(),
                "snippet": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesUntrash"] = gmail.post(
        "gmail/v1/users/{userId}/messages/send",
        t.struct(
            {
                "userId": t.string().optional(),
                "labelIds": t.array(t.string()).optional(),
                "historyId": t.string().optional(),
                "internalDate": t.string().optional(),
                "threadId": t.string().optional(),
                "raw": t.string().optional(),
                "payload": t.proxy(renames["MessagePartIn"]).optional(),
                "sizeEstimate": t.integer().optional(),
                "snippet": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesBatchModify"] = gmail.post(
        "gmail/v1/users/{userId}/messages/send",
        t.struct(
            {
                "userId": t.string().optional(),
                "labelIds": t.array(t.string()).optional(),
                "historyId": t.string().optional(),
                "internalDate": t.string().optional(),
                "threadId": t.string().optional(),
                "raw": t.string().optional(),
                "payload": t.proxy(renames["MessagePartIn"]).optional(),
                "sizeEstimate": t.integer().optional(),
                "snippet": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesGet"] = gmail.post(
        "gmail/v1/users/{userId}/messages/send",
        t.struct(
            {
                "userId": t.string().optional(),
                "labelIds": t.array(t.string()).optional(),
                "historyId": t.string().optional(),
                "internalDate": t.string().optional(),
                "threadId": t.string().optional(),
                "raw": t.string().optional(),
                "payload": t.proxy(renames["MessagePartIn"]).optional(),
                "sizeEstimate": t.integer().optional(),
                "snippet": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesSend"] = gmail.post(
        "gmail/v1/users/{userId}/messages/send",
        t.struct(
            {
                "userId": t.string().optional(),
                "labelIds": t.array(t.string()).optional(),
                "historyId": t.string().optional(),
                "internalDate": t.string().optional(),
                "threadId": t.string().optional(),
                "raw": t.string().optional(),
                "payload": t.proxy(renames["MessagePartIn"]).optional(),
                "sizeEstimate": t.integer().optional(),
                "snippet": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersMessagesAttachmentsGet"] = gmail.get(
        "gmail/v1/users/{userId}/messages/{messageId}/attachments/{id}",
        t.struct(
            {
                "messageId": t.string().optional(),
                "userId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessagePartBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersLabelsCreate"] = gmail.put(
        "gmail/v1/users/{userId}/labels/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "messageListVisibility": t.string().optional(),
                "messagesUnread": t.integer().optional(),
                "labelListVisibility": t.string().optional(),
                "type": t.string().optional(),
                "threadsTotal": t.integer().optional(),
                "threadsUnread": t.integer().optional(),
                "color": t.proxy(renames["LabelColorIn"]).optional(),
                "name": t.string().optional(),
                "messagesTotal": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersLabelsPatch"] = gmail.put(
        "gmail/v1/users/{userId}/labels/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "messageListVisibility": t.string().optional(),
                "messagesUnread": t.integer().optional(),
                "labelListVisibility": t.string().optional(),
                "type": t.string().optional(),
                "threadsTotal": t.integer().optional(),
                "threadsUnread": t.integer().optional(),
                "color": t.proxy(renames["LabelColorIn"]).optional(),
                "name": t.string().optional(),
                "messagesTotal": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersLabelsDelete"] = gmail.put(
        "gmail/v1/users/{userId}/labels/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "messageListVisibility": t.string().optional(),
                "messagesUnread": t.integer().optional(),
                "labelListVisibility": t.string().optional(),
                "type": t.string().optional(),
                "threadsTotal": t.integer().optional(),
                "threadsUnread": t.integer().optional(),
                "color": t.proxy(renames["LabelColorIn"]).optional(),
                "name": t.string().optional(),
                "messagesTotal": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersLabelsGet"] = gmail.put(
        "gmail/v1/users/{userId}/labels/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "messageListVisibility": t.string().optional(),
                "messagesUnread": t.integer().optional(),
                "labelListVisibility": t.string().optional(),
                "type": t.string().optional(),
                "threadsTotal": t.integer().optional(),
                "threadsUnread": t.integer().optional(),
                "color": t.proxy(renames["LabelColorIn"]).optional(),
                "name": t.string().optional(),
                "messagesTotal": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersLabelsList"] = gmail.put(
        "gmail/v1/users/{userId}/labels/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "messageListVisibility": t.string().optional(),
                "messagesUnread": t.integer().optional(),
                "labelListVisibility": t.string().optional(),
                "type": t.string().optional(),
                "threadsTotal": t.integer().optional(),
                "threadsUnread": t.integer().optional(),
                "color": t.proxy(renames["LabelColorIn"]).optional(),
                "name": t.string().optional(),
                "messagesTotal": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersLabelsUpdate"] = gmail.put(
        "gmail/v1/users/{userId}/labels/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "userId": t.string().optional(),
                "messageListVisibility": t.string().optional(),
                "messagesUnread": t.integer().optional(),
                "labelListVisibility": t.string().optional(),
                "type": t.string().optional(),
                "threadsTotal": t.integer().optional(),
                "threadsUnread": t.integer().optional(),
                "color": t.proxy(renames["LabelColorIn"]).optional(),
                "name": t.string().optional(),
                "messagesTotal": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LabelOut"]),
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
    functions["usersSettingsUpdateImap"] = gmail.get(
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
    functions["usersSettingsUpdateLanguage"] = gmail.get(
        "gmail/v1/users/{userId}/settings/imap",
        t.struct({"userId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ImapSettingsOut"]),
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
    functions["usersSettingsUpdateVacation"] = gmail.get(
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
    functions["usersSettingsGetAutoForwarding"] = gmail.get(
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
    functions["usersSettingsDelegatesCreate"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/delegates/{delegateEmail}",
        t.struct(
            {
                "delegateEmail": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsDelegatesGet"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/delegates/{delegateEmail}",
        t.struct(
            {
                "delegateEmail": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsDelegatesList"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/delegates/{delegateEmail}",
        t.struct(
            {
                "delegateEmail": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsDelegatesDelete"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/delegates/{delegateEmail}",
        t.struct(
            {
                "delegateEmail": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsFiltersList"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/filters/{id}",
        t.struct(
            {
                "userId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsFiltersCreate"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/filters/{id}",
        t.struct(
            {
                "userId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsFiltersGet"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/filters/{id}",
        t.struct(
            {
                "userId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsFiltersDelete"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/filters/{id}",
        t.struct(
            {
                "userId": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsPatch"] = gmail.post(
        "gmail/v1/users/{userId}/settings/sendAs",
        t.struct(
            {
                "userId": t.string().optional(),
                "isDefault": t.boolean().optional(),
                "treatAsAlias": t.boolean().optional(),
                "sendAsEmail": t.string().optional(),
                "smtpMsa": t.proxy(renames["SmtpMsaIn"]).optional(),
                "signature": t.string().optional(),
                "isPrimary": t.boolean().optional(),
                "replyToAddress": t.string().optional(),
                "verificationStatus": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SendAsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsGet"] = gmail.post(
        "gmail/v1/users/{userId}/settings/sendAs",
        t.struct(
            {
                "userId": t.string().optional(),
                "isDefault": t.boolean().optional(),
                "treatAsAlias": t.boolean().optional(),
                "sendAsEmail": t.string().optional(),
                "smtpMsa": t.proxy(renames["SmtpMsaIn"]).optional(),
                "signature": t.string().optional(),
                "isPrimary": t.boolean().optional(),
                "replyToAddress": t.string().optional(),
                "verificationStatus": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SendAsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsDelete"] = gmail.post(
        "gmail/v1/users/{userId}/settings/sendAs",
        t.struct(
            {
                "userId": t.string().optional(),
                "isDefault": t.boolean().optional(),
                "treatAsAlias": t.boolean().optional(),
                "sendAsEmail": t.string().optional(),
                "smtpMsa": t.proxy(renames["SmtpMsaIn"]).optional(),
                "signature": t.string().optional(),
                "isPrimary": t.boolean().optional(),
                "replyToAddress": t.string().optional(),
                "verificationStatus": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SendAsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsList"] = gmail.post(
        "gmail/v1/users/{userId}/settings/sendAs",
        t.struct(
            {
                "userId": t.string().optional(),
                "isDefault": t.boolean().optional(),
                "treatAsAlias": t.boolean().optional(),
                "sendAsEmail": t.string().optional(),
                "smtpMsa": t.proxy(renames["SmtpMsaIn"]).optional(),
                "signature": t.string().optional(),
                "isPrimary": t.boolean().optional(),
                "replyToAddress": t.string().optional(),
                "verificationStatus": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SendAsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsUpdate"] = gmail.post(
        "gmail/v1/users/{userId}/settings/sendAs",
        t.struct(
            {
                "userId": t.string().optional(),
                "isDefault": t.boolean().optional(),
                "treatAsAlias": t.boolean().optional(),
                "sendAsEmail": t.string().optional(),
                "smtpMsa": t.proxy(renames["SmtpMsaIn"]).optional(),
                "signature": t.string().optional(),
                "isPrimary": t.boolean().optional(),
                "replyToAddress": t.string().optional(),
                "verificationStatus": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SendAsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsVerify"] = gmail.post(
        "gmail/v1/users/{userId}/settings/sendAs",
        t.struct(
            {
                "userId": t.string().optional(),
                "isDefault": t.boolean().optional(),
                "treatAsAlias": t.boolean().optional(),
                "sendAsEmail": t.string().optional(),
                "smtpMsa": t.proxy(renames["SmtpMsaIn"]).optional(),
                "signature": t.string().optional(),
                "isPrimary": t.boolean().optional(),
                "replyToAddress": t.string().optional(),
                "verificationStatus": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SendAsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsCreate"] = gmail.post(
        "gmail/v1/users/{userId}/settings/sendAs",
        t.struct(
            {
                "userId": t.string().optional(),
                "isDefault": t.boolean().optional(),
                "treatAsAlias": t.boolean().optional(),
                "sendAsEmail": t.string().optional(),
                "smtpMsa": t.proxy(renames["SmtpMsaIn"]).optional(),
                "signature": t.string().optional(),
                "isPrimary": t.boolean().optional(),
                "replyToAddress": t.string().optional(),
                "verificationStatus": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SendAsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsSmimeInfoSetDefault"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/sendAs/{sendAsEmail}/smimeInfo/{id}",
        t.struct(
            {
                "userId": t.string().optional(),
                "sendAsEmail": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsSmimeInfoGet"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/sendAs/{sendAsEmail}/smimeInfo/{id}",
        t.struct(
            {
                "userId": t.string().optional(),
                "sendAsEmail": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsSmimeInfoList"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/sendAs/{sendAsEmail}/smimeInfo/{id}",
        t.struct(
            {
                "userId": t.string().optional(),
                "sendAsEmail": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsSmimeInfoInsert"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/sendAs/{sendAsEmail}/smimeInfo/{id}",
        t.struct(
            {
                "userId": t.string().optional(),
                "sendAsEmail": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsSendAsSmimeInfoDelete"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/sendAs/{sendAsEmail}/smimeInfo/{id}",
        t.struct(
            {
                "userId": t.string().optional(),
                "sendAsEmail": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsForwardingAddressesGet"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/forwardingAddresses/{forwardingEmail}",
        t.struct(
            {
                "forwardingEmail": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsForwardingAddressesList"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/forwardingAddresses/{forwardingEmail}",
        t.struct(
            {
                "forwardingEmail": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsForwardingAddressesCreate"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/forwardingAddresses/{forwardingEmail}",
        t.struct(
            {
                "forwardingEmail": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSettingsForwardingAddressesDelete"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/forwardingAddresses/{forwardingEmail}",
        t.struct(
            {
                "forwardingEmail": t.string().optional(),
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
    functions["usersSettingsCseIdentitiesPatch"] = gmail.delete(
        "gmail/v1/users/{userId}/settings/cse/identities/{cseEmailAddress}",
        t.struct(
            {
                "userId": t.string().optional(),
                "cseEmailAddress": t.string().optional(),
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
                "userId": t.string().optional(),
                "cseEmailAddress": t.string().optional(),
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
                "userId": t.string().optional(),
                "cseEmailAddress": t.string().optional(),
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
                "userId": t.string().optional(),
                "cseEmailAddress": t.string().optional(),
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
                "userId": t.string().optional(),
                "cseEmailAddress": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersHistoryList"] = gmail.get(
        "gmail/v1/users/{userId}/history",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "labelId": t.string().optional(),
                "userId": t.string().optional(),
                "startHistoryId": t.string(),
                "historyTypes": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListHistoryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="gmail", renames=renames, types=Box(types), functions=Box(functions)
    )
