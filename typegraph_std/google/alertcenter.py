from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_alertcenter() -> Import:
    alertcenter = HTTPRuntime("https://alertcenter.googleapis.com/")

    renames = {
        "ErrorResponse": "_alertcenter_1_ErrorResponse",
        "ReportingRuleIn": "_alertcenter_2_ReportingRuleIn",
        "ReportingRuleOut": "_alertcenter_3_ReportingRuleOut",
        "CloudPubsubTopicIn": "_alertcenter_4_CloudPubsubTopicIn",
        "CloudPubsubTopicOut": "_alertcenter_5_CloudPubsubTopicOut",
        "AbuseDetectedIn": "_alertcenter_6_AbuseDetectedIn",
        "AbuseDetectedOut": "_alertcenter_7_AbuseDetectedOut",
        "SSOProfileDeletedEventIn": "_alertcenter_8_SSOProfileDeletedEventIn",
        "SSOProfileDeletedEventOut": "_alertcenter_9_SSOProfileDeletedEventOut",
        "ListAlertsResponseIn": "_alertcenter_10_ListAlertsResponseIn",
        "ListAlertsResponseOut": "_alertcenter_11_ListAlertsResponseOut",
        "AccountWarningIn": "_alertcenter_12_AccountWarningIn",
        "AccountWarningOut": "_alertcenter_13_AccountWarningOut",
        "GoogleOperationsIn": "_alertcenter_14_GoogleOperationsIn",
        "GoogleOperationsOut": "_alertcenter_15_GoogleOperationsOut",
        "SSOProfileUpdatedEventIn": "_alertcenter_16_SSOProfileUpdatedEventIn",
        "SSOProfileUpdatedEventOut": "_alertcenter_17_SSOProfileUpdatedEventOut",
        "LoginDetailsIn": "_alertcenter_18_LoginDetailsIn",
        "LoginDetailsOut": "_alertcenter_19_LoginDetailsOut",
        "BatchUndeleteAlertsRequestIn": "_alertcenter_20_BatchUndeleteAlertsRequestIn",
        "BatchUndeleteAlertsRequestOut": "_alertcenter_21_BatchUndeleteAlertsRequestOut",
        "AlertFeedbackIn": "_alertcenter_22_AlertFeedbackIn",
        "AlertFeedbackOut": "_alertcenter_23_AlertFeedbackOut",
        "ActionInfoIn": "_alertcenter_24_ActionInfoIn",
        "ActionInfoOut": "_alertcenter_25_ActionInfoOut",
        "StatusIn": "_alertcenter_26_StatusIn",
        "StatusOut": "_alertcenter_27_StatusOut",
        "SSOProfileCreatedEventIn": "_alertcenter_28_SSOProfileCreatedEventIn",
        "SSOProfileCreatedEventOut": "_alertcenter_29_SSOProfileCreatedEventOut",
        "VoiceMisconfigurationIn": "_alertcenter_30_VoiceMisconfigurationIn",
        "VoiceMisconfigurationOut": "_alertcenter_31_VoiceMisconfigurationOut",
        "EntityIn": "_alertcenter_32_EntityIn",
        "EntityOut": "_alertcenter_33_EntityOut",
        "BatchUndeleteAlertsResponseIn": "_alertcenter_34_BatchUndeleteAlertsResponseIn",
        "BatchUndeleteAlertsResponseOut": "_alertcenter_35_BatchUndeleteAlertsResponseOut",
        "RequestInfoIn": "_alertcenter_36_RequestInfoIn",
        "RequestInfoOut": "_alertcenter_37_RequestInfoOut",
        "SuspiciousActivitySecurityDetailIn": "_alertcenter_38_SuspiciousActivitySecurityDetailIn",
        "SuspiciousActivitySecurityDetailOut": "_alertcenter_39_SuspiciousActivitySecurityDetailOut",
        "PhishingSpikeIn": "_alertcenter_40_PhishingSpikeIn",
        "PhishingSpikeOut": "_alertcenter_41_PhishingSpikeOut",
        "SuperAdminPasswordResetEventIn": "_alertcenter_42_SuperAdminPasswordResetEventIn",
        "SuperAdminPasswordResetEventOut": "_alertcenter_43_SuperAdminPasswordResetEventOut",
        "DeviceCompromisedIn": "_alertcenter_44_DeviceCompromisedIn",
        "DeviceCompromisedOut": "_alertcenter_45_DeviceCompromisedOut",
        "MaliciousEntityIn": "_alertcenter_46_MaliciousEntityIn",
        "MaliciousEntityOut": "_alertcenter_47_MaliciousEntityOut",
        "UndeleteAlertRequestIn": "_alertcenter_48_UndeleteAlertRequestIn",
        "UndeleteAlertRequestOut": "_alertcenter_49_UndeleteAlertRequestOut",
        "DeviceCompromisedSecurityDetailIn": "_alertcenter_50_DeviceCompromisedSecurityDetailIn",
        "DeviceCompromisedSecurityDetailOut": "_alertcenter_51_DeviceCompromisedSecurityDetailOut",
        "ListAlertFeedbackResponseIn": "_alertcenter_52_ListAlertFeedbackResponseIn",
        "ListAlertFeedbackResponseOut": "_alertcenter_53_ListAlertFeedbackResponseOut",
        "GmailMessageInfoIn": "_alertcenter_54_GmailMessageInfoIn",
        "GmailMessageInfoOut": "_alertcenter_55_GmailMessageInfoOut",
        "BatchDeleteAlertsResponseIn": "_alertcenter_56_BatchDeleteAlertsResponseIn",
        "BatchDeleteAlertsResponseOut": "_alertcenter_57_BatchDeleteAlertsResponseOut",
        "CsvRowIn": "_alertcenter_58_CsvRowIn",
        "CsvRowOut": "_alertcenter_59_CsvRowOut",
        "SettingsIn": "_alertcenter_60_SettingsIn",
        "SettingsOut": "_alertcenter_61_SettingsOut",
        "AccountSuspensionWarningIn": "_alertcenter_62_AccountSuspensionWarningIn",
        "AccountSuspensionWarningOut": "_alertcenter_63_AccountSuspensionWarningOut",
        "TransferErrorIn": "_alertcenter_64_TransferErrorIn",
        "TransferErrorOut": "_alertcenter_65_TransferErrorOut",
        "PredefinedDetectorInfoIn": "_alertcenter_66_PredefinedDetectorInfoIn",
        "PredefinedDetectorInfoOut": "_alertcenter_67_PredefinedDetectorInfoOut",
        "UserIn": "_alertcenter_68_UserIn",
        "UserOut": "_alertcenter_69_UserOut",
        "CsvIn": "_alertcenter_70_CsvIn",
        "CsvOut": "_alertcenter_71_CsvOut",
        "AccountSuspensionDetailsIn": "_alertcenter_72_AccountSuspensionDetailsIn",
        "AccountSuspensionDetailsOut": "_alertcenter_73_AccountSuspensionDetailsOut",
        "AppSettingsChangedIn": "_alertcenter_74_AppSettingsChangedIn",
        "AppSettingsChangedOut": "_alertcenter_75_AppSettingsChangedOut",
        "ApnsCertificateExpirationInfoIn": "_alertcenter_76_ApnsCertificateExpirationInfoIn",
        "ApnsCertificateExpirationInfoOut": "_alertcenter_77_ApnsCertificateExpirationInfoOut",
        "StateSponsoredAttackIn": "_alertcenter_78_StateSponsoredAttackIn",
        "StateSponsoredAttackOut": "_alertcenter_79_StateSponsoredAttackOut",
        "RuleViolationInfoIn": "_alertcenter_80_RuleViolationInfoIn",
        "RuleViolationInfoOut": "_alertcenter_81_RuleViolationInfoOut",
        "BatchDeleteAlertsRequestIn": "_alertcenter_82_BatchDeleteAlertsRequestIn",
        "BatchDeleteAlertsRequestOut": "_alertcenter_83_BatchDeleteAlertsRequestOut",
        "NotificationIn": "_alertcenter_84_NotificationIn",
        "NotificationOut": "_alertcenter_85_NotificationOut",
        "VoicemailMisconfigurationIn": "_alertcenter_86_VoicemailMisconfigurationIn",
        "VoicemailMisconfigurationOut": "_alertcenter_87_VoicemailMisconfigurationOut",
        "AttachmentIn": "_alertcenter_88_AttachmentIn",
        "AttachmentOut": "_alertcenter_89_AttachmentOut",
        "TransferMisconfigurationIn": "_alertcenter_90_TransferMisconfigurationIn",
        "TransferMisconfigurationOut": "_alertcenter_91_TransferMisconfigurationOut",
        "AlertIn": "_alertcenter_92_AlertIn",
        "AlertOut": "_alertcenter_93_AlertOut",
        "PrimaryAdminChangedEventIn": "_alertcenter_94_PrimaryAdminChangedEventIn",
        "PrimaryAdminChangedEventOut": "_alertcenter_95_PrimaryAdminChangedEventOut",
        "DlpRuleViolationIn": "_alertcenter_96_DlpRuleViolationIn",
        "DlpRuleViolationOut": "_alertcenter_97_DlpRuleViolationOut",
        "DomainIdIn": "_alertcenter_98_DomainIdIn",
        "DomainIdOut": "_alertcenter_99_DomainIdOut",
        "EmptyIn": "_alertcenter_100_EmptyIn",
        "EmptyOut": "_alertcenter_101_EmptyOut",
        "MatchInfoIn": "_alertcenter_102_MatchInfoIn",
        "MatchInfoOut": "_alertcenter_103_MatchInfoOut",
        "BadWhitelistIn": "_alertcenter_104_BadWhitelistIn",
        "BadWhitelistOut": "_alertcenter_105_BadWhitelistOut",
        "DomainWideTakeoutInitiatedIn": "_alertcenter_106_DomainWideTakeoutInitiatedIn",
        "DomainWideTakeoutInitiatedOut": "_alertcenter_107_DomainWideTakeoutInitiatedOut",
        "SensitiveAdminActionIn": "_alertcenter_108_SensitiveAdminActionIn",
        "SensitiveAdminActionOut": "_alertcenter_109_SensitiveAdminActionOut",
        "UserDefinedDetectorInfoIn": "_alertcenter_110_UserDefinedDetectorInfoIn",
        "UserDefinedDetectorInfoOut": "_alertcenter_111_UserDefinedDetectorInfoOut",
        "UserChangesIn": "_alertcenter_112_UserChangesIn",
        "UserChangesOut": "_alertcenter_113_UserChangesOut",
        "AppMakerSqlSetupNotificationIn": "_alertcenter_114_AppMakerSqlSetupNotificationIn",
        "AppMakerSqlSetupNotificationOut": "_alertcenter_115_AppMakerSqlSetupNotificationOut",
        "ResourceInfoIn": "_alertcenter_116_ResourceInfoIn",
        "ResourceInfoOut": "_alertcenter_117_ResourceInfoOut",
        "MailPhishingIn": "_alertcenter_118_MailPhishingIn",
        "MailPhishingOut": "_alertcenter_119_MailPhishingOut",
        "SuspiciousActivityIn": "_alertcenter_120_SuspiciousActivityIn",
        "SuspiciousActivityOut": "_alertcenter_121_SuspiciousActivityOut",
        "AppsOutageIn": "_alertcenter_122_AppsOutageIn",
        "AppsOutageOut": "_alertcenter_123_AppsOutageOut",
        "VoicemailRecipientErrorIn": "_alertcenter_124_VoicemailRecipientErrorIn",
        "VoicemailRecipientErrorOut": "_alertcenter_125_VoicemailRecipientErrorOut",
        "MergeInfoIn": "_alertcenter_126_MergeInfoIn",
        "MergeInfoOut": "_alertcenter_127_MergeInfoOut",
        "AlertMetadataIn": "_alertcenter_128_AlertMetadataIn",
        "AlertMetadataOut": "_alertcenter_129_AlertMetadataOut",
        "MandatoryServiceAnnouncementIn": "_alertcenter_130_MandatoryServiceAnnouncementIn",
        "MandatoryServiceAnnouncementOut": "_alertcenter_131_MandatoryServiceAnnouncementOut",
        "ActivityRuleIn": "_alertcenter_132_ActivityRuleIn",
        "ActivityRuleOut": "_alertcenter_133_ActivityRuleOut",
        "EntityListIn": "_alertcenter_134_EntityListIn",
        "EntityListOut": "_alertcenter_135_EntityListOut",
        "RuleInfoIn": "_alertcenter_136_RuleInfoIn",
        "RuleInfoOut": "_alertcenter_137_RuleInfoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ReportingRuleIn"] = t.struct(
        {
            "name": t.string().optional(),
            "query": t.string().optional(),
            "alertDetails": t.string().optional(),
        }
    ).named(renames["ReportingRuleIn"])
    types["ReportingRuleOut"] = t.struct(
        {
            "name": t.string().optional(),
            "query": t.string().optional(),
            "alertDetails": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportingRuleOut"])
    types["CloudPubsubTopicIn"] = t.struct(
        {"payloadFormat": t.string().optional(), "topicName": t.string().optional()}
    ).named(renames["CloudPubsubTopicIn"])
    types["CloudPubsubTopicOut"] = t.struct(
        {
            "payloadFormat": t.string().optional(),
            "topicName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudPubsubTopicOut"])
    types["AbuseDetectedIn"] = t.struct(
        {
            "subAlertId": t.string().optional(),
            "additionalDetails": t.proxy(renames["EntityListIn"]).optional(),
            "variationType": t.string().optional(),
            "product": t.string().optional(),
        }
    ).named(renames["AbuseDetectedIn"])
    types["AbuseDetectedOut"] = t.struct(
        {
            "subAlertId": t.string().optional(),
            "additionalDetails": t.proxy(renames["EntityListOut"]).optional(),
            "variationType": t.string().optional(),
            "product": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AbuseDetectedOut"])
    types["SSOProfileDeletedEventIn"] = t.struct(
        {"inboundSsoProfileName": t.string().optional()}
    ).named(renames["SSOProfileDeletedEventIn"])
    types["SSOProfileDeletedEventOut"] = t.struct(
        {
            "inboundSsoProfileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SSOProfileDeletedEventOut"])
    types["ListAlertsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "alerts": t.array(t.proxy(renames["AlertIn"])).optional(),
        }
    ).named(renames["ListAlertsResponseIn"])
    types["ListAlertsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "alerts": t.array(t.proxy(renames["AlertOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAlertsResponseOut"])
    types["AccountWarningIn"] = t.struct(
        {
            "email": t.string(),
            "loginDetails": t.proxy(renames["LoginDetailsIn"]).optional(),
        }
    ).named(renames["AccountWarningIn"])
    types["AccountWarningOut"] = t.struct(
        {
            "email": t.string(),
            "loginDetails": t.proxy(renames["LoginDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountWarningOut"])
    types["GoogleOperationsIn"] = t.struct(
        {
            "affectedUserEmails": t.array(t.string()).optional(),
            "domain": t.string().optional(),
            "attachmentData": t.proxy(renames["AttachmentIn"]).optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "header": t.string().optional(),
        }
    ).named(renames["GoogleOperationsIn"])
    types["GoogleOperationsOut"] = t.struct(
        {
            "affectedUserEmails": t.array(t.string()).optional(),
            "domain": t.string().optional(),
            "attachmentData": t.proxy(renames["AttachmentOut"]).optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "header": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleOperationsOut"])
    types["SSOProfileUpdatedEventIn"] = t.struct(
        {
            "inboundSsoProfileChanges": t.string().optional(),
            "inboundSsoProfileName": t.string().optional(),
        }
    ).named(renames["SSOProfileUpdatedEventIn"])
    types["SSOProfileUpdatedEventOut"] = t.struct(
        {
            "inboundSsoProfileChanges": t.string().optional(),
            "inboundSsoProfileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SSOProfileUpdatedEventOut"])
    types["LoginDetailsIn"] = t.struct(
        {"loginTime": t.string().optional(), "ipAddress": t.string().optional()}
    ).named(renames["LoginDetailsIn"])
    types["LoginDetailsOut"] = t.struct(
        {
            "loginTime": t.string().optional(),
            "ipAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoginDetailsOut"])
    types["BatchUndeleteAlertsRequestIn"] = t.struct(
        {"customerId": t.string().optional(), "alertId": t.array(t.string())}
    ).named(renames["BatchUndeleteAlertsRequestIn"])
    types["BatchUndeleteAlertsRequestOut"] = t.struct(
        {
            "customerId": t.string().optional(),
            "alertId": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUndeleteAlertsRequestOut"])
    types["AlertFeedbackIn"] = t.struct(
        {
            "alertId": t.string().optional(),
            "customerId": t.string().optional(),
            "email": t.string().optional(),
            "type": t.string(),
            "createTime": t.string().optional(),
            "feedbackId": t.string().optional(),
        }
    ).named(renames["AlertFeedbackIn"])
    types["AlertFeedbackOut"] = t.struct(
        {
            "alertId": t.string().optional(),
            "customerId": t.string().optional(),
            "email": t.string().optional(),
            "type": t.string(),
            "createTime": t.string().optional(),
            "feedbackId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertFeedbackOut"])
    types["ActionInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ActionInfoIn"]
    )
    types["ActionInfoOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActionInfoOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["SSOProfileCreatedEventIn"] = t.struct(
        {"inboundSsoProfileName": t.string().optional()}
    ).named(renames["SSOProfileCreatedEventIn"])
    types["SSOProfileCreatedEventOut"] = t.struct(
        {
            "inboundSsoProfileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SSOProfileCreatedEventOut"])
    types["VoiceMisconfigurationIn"] = t.struct(
        {
            "entityName": t.string().optional(),
            "membersMisconfiguration": t.proxy(
                renames["TransferMisconfigurationIn"]
            ).optional(),
            "voicemailMisconfiguration": t.proxy(
                renames["VoicemailMisconfigurationIn"]
            ).optional(),
            "entityType": t.string().optional(),
            "transferMisconfiguration": t.proxy(
                renames["TransferMisconfigurationIn"]
            ).optional(),
            "fixUri": t.string().optional(),
        }
    ).named(renames["VoiceMisconfigurationIn"])
    types["VoiceMisconfigurationOut"] = t.struct(
        {
            "entityName": t.string().optional(),
            "membersMisconfiguration": t.proxy(
                renames["TransferMisconfigurationOut"]
            ).optional(),
            "voicemailMisconfiguration": t.proxy(
                renames["VoicemailMisconfigurationOut"]
            ).optional(),
            "entityType": t.string().optional(),
            "transferMisconfiguration": t.proxy(
                renames["TransferMisconfigurationOut"]
            ).optional(),
            "fixUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceMisconfigurationOut"])
    types["EntityIn"] = t.struct(
        {
            "link": t.string().optional(),
            "name": t.string().optional(),
            "values": t.array(t.string()).optional(),
        }
    ).named(renames["EntityIn"])
    types["EntityOut"] = t.struct(
        {
            "link": t.string().optional(),
            "name": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityOut"])
    types["BatchUndeleteAlertsResponseIn"] = t.struct(
        {
            "successAlertIds": t.array(t.string()).optional(),
            "failedAlertStatus": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["BatchUndeleteAlertsResponseIn"])
    types["BatchUndeleteAlertsResponseOut"] = t.struct(
        {
            "successAlertIds": t.array(t.string()).optional(),
            "failedAlertStatus": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUndeleteAlertsResponseOut"])
    types["RequestInfoIn"] = t.struct(
        {
            "appKey": t.string(),
            "appDeveloperEmail": t.array(t.string()).optional(),
            "numberOfRequests": t.string(),
        }
    ).named(renames["RequestInfoIn"])
    types["RequestInfoOut"] = t.struct(
        {
            "appKey": t.string(),
            "appDeveloperEmail": t.array(t.string()).optional(),
            "numberOfRequests": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestInfoOut"])
    types["SuspiciousActivitySecurityDetailIn"] = t.struct(
        {
            "serialNumber": t.string().optional(),
            "resourceId": t.string().optional(),
            "oldValue": t.string().optional(),
            "deviceModel": t.string().optional(),
            "deviceType": t.string().optional(),
            "newValue": t.string().optional(),
            "deviceProperty": t.string().optional(),
            "deviceId": t.string(),
            "iosVendorId": t.string(),
        }
    ).named(renames["SuspiciousActivitySecurityDetailIn"])
    types["SuspiciousActivitySecurityDetailOut"] = t.struct(
        {
            "serialNumber": t.string().optional(),
            "resourceId": t.string().optional(),
            "oldValue": t.string().optional(),
            "deviceModel": t.string().optional(),
            "deviceType": t.string().optional(),
            "newValue": t.string().optional(),
            "deviceProperty": t.string().optional(),
            "deviceId": t.string(),
            "iosVendorId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuspiciousActivitySecurityDetailOut"])
    types["PhishingSpikeIn"] = t.struct(
        {
            "maliciousEntity": t.proxy(renames["MaliciousEntityIn"]).optional(),
            "isInternal": t.boolean().optional(),
            "messages": t.array(t.proxy(renames["GmailMessageInfoIn"])).optional(),
            "domainId": t.proxy(renames["DomainIdIn"]).optional(),
        }
    ).named(renames["PhishingSpikeIn"])
    types["PhishingSpikeOut"] = t.struct(
        {
            "maliciousEntity": t.proxy(renames["MaliciousEntityOut"]).optional(),
            "isInternal": t.boolean().optional(),
            "messages": t.array(t.proxy(renames["GmailMessageInfoOut"])).optional(),
            "domainId": t.proxy(renames["DomainIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhishingSpikeOut"])
    types["SuperAdminPasswordResetEventIn"] = t.struct(
        {"userEmail": t.string().optional()}
    ).named(renames["SuperAdminPasswordResetEventIn"])
    types["SuperAdminPasswordResetEventOut"] = t.struct(
        {
            "userEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuperAdminPasswordResetEventOut"])
    types["DeviceCompromisedIn"] = t.struct(
        {
            "email": t.string().optional(),
            "events": t.array(t.proxy(renames["DeviceCompromisedSecurityDetailIn"])),
        }
    ).named(renames["DeviceCompromisedIn"])
    types["DeviceCompromisedOut"] = t.struct(
        {
            "email": t.string().optional(),
            "events": t.array(t.proxy(renames["DeviceCompromisedSecurityDetailOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceCompromisedOut"])
    types["MaliciousEntityIn"] = t.struct(
        {
            "entity": t.proxy(renames["UserIn"]).optional(),
            "displayName": t.string().optional(),
            "fromHeader": t.string().optional(),
        }
    ).named(renames["MaliciousEntityIn"])
    types["MaliciousEntityOut"] = t.struct(
        {
            "entity": t.proxy(renames["UserOut"]).optional(),
            "displayName": t.string().optional(),
            "fromHeader": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaliciousEntityOut"])
    types["UndeleteAlertRequestIn"] = t.struct(
        {"customerId": t.string().optional()}
    ).named(renames["UndeleteAlertRequestIn"])
    types["UndeleteAlertRequestOut"] = t.struct(
        {
            "customerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UndeleteAlertRequestOut"])
    types["DeviceCompromisedSecurityDetailIn"] = t.struct(
        {
            "deviceCompromisedState": t.string().optional(),
            "iosVendorId": t.string(),
            "serialNumber": t.string().optional(),
            "deviceType": t.string().optional(),
            "deviceId": t.string(),
            "resourceId": t.string().optional(),
            "deviceModel": t.string().optional(),
        }
    ).named(renames["DeviceCompromisedSecurityDetailIn"])
    types["DeviceCompromisedSecurityDetailOut"] = t.struct(
        {
            "deviceCompromisedState": t.string().optional(),
            "iosVendorId": t.string(),
            "serialNumber": t.string().optional(),
            "deviceType": t.string().optional(),
            "deviceId": t.string(),
            "resourceId": t.string().optional(),
            "deviceModel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceCompromisedSecurityDetailOut"])
    types["ListAlertFeedbackResponseIn"] = t.struct(
        {"feedback": t.array(t.proxy(renames["AlertFeedbackIn"])).optional()}
    ).named(renames["ListAlertFeedbackResponseIn"])
    types["ListAlertFeedbackResponseOut"] = t.struct(
        {
            "feedback": t.array(t.proxy(renames["AlertFeedbackOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAlertFeedbackResponseOut"])
    types["GmailMessageInfoIn"] = t.struct(
        {
            "recipient": t.string().optional(),
            "date": t.string().optional(),
            "md5HashMessageBody": t.string().optional(),
            "messageBodySnippet": t.string().optional(),
            "sentTime": t.string().optional(),
            "subjectText": t.string().optional(),
            "messageId": t.string().optional(),
            "md5HashSubject": t.string().optional(),
            "attachmentsSha256Hash": t.array(t.string()).optional(),
        }
    ).named(renames["GmailMessageInfoIn"])
    types["GmailMessageInfoOut"] = t.struct(
        {
            "recipient": t.string().optional(),
            "date": t.string().optional(),
            "md5HashMessageBody": t.string().optional(),
            "messageBodySnippet": t.string().optional(),
            "sentTime": t.string().optional(),
            "subjectText": t.string().optional(),
            "messageId": t.string().optional(),
            "md5HashSubject": t.string().optional(),
            "attachmentsSha256Hash": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GmailMessageInfoOut"])
    types["BatchDeleteAlertsResponseIn"] = t.struct(
        {
            "failedAlertStatus": t.struct({"_": t.string().optional()}).optional(),
            "successAlertIds": t.array(t.string()).optional(),
        }
    ).named(renames["BatchDeleteAlertsResponseIn"])
    types["BatchDeleteAlertsResponseOut"] = t.struct(
        {
            "failedAlertStatus": t.struct({"_": t.string().optional()}).optional(),
            "successAlertIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteAlertsResponseOut"])
    types["CsvRowIn"] = t.struct({"entries": t.array(t.string()).optional()}).named(
        renames["CsvRowIn"]
    )
    types["CsvRowOut"] = t.struct(
        {
            "entries": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CsvRowOut"])
    types["SettingsIn"] = t.struct(
        {"notifications": t.array(t.proxy(renames["NotificationIn"])).optional()}
    ).named(renames["SettingsIn"])
    types["SettingsOut"] = t.struct(
        {
            "notifications": t.array(t.proxy(renames["NotificationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsOut"])
    types["AccountSuspensionWarningIn"] = t.struct(
        {
            "suspensionDetails": t.array(
                t.proxy(renames["AccountSuspensionDetailsIn"])
            ).optional(),
            "state": t.string().optional(),
            "appealWindow": t.string().optional(),
        }
    ).named(renames["AccountSuspensionWarningIn"])
    types["AccountSuspensionWarningOut"] = t.struct(
        {
            "suspensionDetails": t.array(
                t.proxy(renames["AccountSuspensionDetailsOut"])
            ).optional(),
            "state": t.string().optional(),
            "appealWindow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountSuspensionWarningOut"])
    types["TransferErrorIn"] = t.struct(
        {
            "invalidReason": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "email": t.string().optional(),
            "entityType": t.string().optional(),
        }
    ).named(renames["TransferErrorIn"])
    types["TransferErrorOut"] = t.struct(
        {
            "invalidReason": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "email": t.string().optional(),
            "entityType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferErrorOut"])
    types["PredefinedDetectorInfoIn"] = t.struct(
        {"detectorName": t.string().optional()}
    ).named(renames["PredefinedDetectorInfoIn"])
    types["PredefinedDetectorInfoOut"] = t.struct(
        {
            "detectorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PredefinedDetectorInfoOut"])
    types["UserIn"] = t.struct(
        {"emailAddress": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "emailAddress": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["CsvIn"] = t.struct(
        {
            "headers": t.array(t.string()).optional(),
            "dataRows": t.array(t.proxy(renames["CsvRowIn"])).optional(),
        }
    ).named(renames["CsvIn"])
    types["CsvOut"] = t.struct(
        {
            "headers": t.array(t.string()).optional(),
            "dataRows": t.array(t.proxy(renames["CsvRowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CsvOut"])
    types["AccountSuspensionDetailsIn"] = t.struct(
        {"abuseReason": t.string().optional(), "productName": t.string().optional()}
    ).named(renames["AccountSuspensionDetailsIn"])
    types["AccountSuspensionDetailsOut"] = t.struct(
        {
            "abuseReason": t.string().optional(),
            "productName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountSuspensionDetailsOut"])
    types["AppSettingsChangedIn"] = t.struct(
        {"name": t.string().optional(), "alertDetails": t.string().optional()}
    ).named(renames["AppSettingsChangedIn"])
    types["AppSettingsChangedOut"] = t.struct(
        {
            "name": t.string().optional(),
            "alertDetails": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppSettingsChangedOut"])
    types["ApnsCertificateExpirationInfoIn"] = t.struct(
        {
            "appleId": t.string().optional(),
            "uid": t.string().optional(),
            "expirationTime": t.string().optional(),
        }
    ).named(renames["ApnsCertificateExpirationInfoIn"])
    types["ApnsCertificateExpirationInfoOut"] = t.struct(
        {
            "appleId": t.string().optional(),
            "uid": t.string().optional(),
            "expirationTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApnsCertificateExpirationInfoOut"])
    types["StateSponsoredAttackIn"] = t.struct({"email": t.string().optional()}).named(
        renames["StateSponsoredAttackIn"]
    )
    types["StateSponsoredAttackOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StateSponsoredAttackOut"])
    types["RuleViolationInfoIn"] = t.struct(
        {
            "triggeringUserEmail": t.string().optional(),
            "resourceInfo": t.proxy(renames["ResourceInfoIn"]).optional(),
            "matchInfo": t.array(t.proxy(renames["MatchInfoIn"])).optional(),
            "suppressedActionTypes": t.array(t.string()).optional(),
            "trigger": t.string().optional(),
            "triggeredActionTypes": t.array(t.string()).optional(),
            "recipients": t.array(t.string()).optional(),
            "triggeredActionInfo": t.array(t.proxy(renames["ActionInfoIn"])).optional(),
            "ruleInfo": t.proxy(renames["RuleInfoIn"]).optional(),
            "dataSource": t.string().optional(),
        }
    ).named(renames["RuleViolationInfoIn"])
    types["RuleViolationInfoOut"] = t.struct(
        {
            "triggeringUserEmail": t.string().optional(),
            "resourceInfo": t.proxy(renames["ResourceInfoOut"]).optional(),
            "matchInfo": t.array(t.proxy(renames["MatchInfoOut"])).optional(),
            "suppressedActionTypes": t.array(t.string()).optional(),
            "trigger": t.string().optional(),
            "triggeredActionTypes": t.array(t.string()).optional(),
            "recipients": t.array(t.string()).optional(),
            "triggeredActionInfo": t.array(
                t.proxy(renames["ActionInfoOut"])
            ).optional(),
            "ruleInfo": t.proxy(renames["RuleInfoOut"]).optional(),
            "dataSource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleViolationInfoOut"])
    types["BatchDeleteAlertsRequestIn"] = t.struct(
        {"customerId": t.string().optional(), "alertId": t.array(t.string())}
    ).named(renames["BatchDeleteAlertsRequestIn"])
    types["BatchDeleteAlertsRequestOut"] = t.struct(
        {
            "customerId": t.string().optional(),
            "alertId": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteAlertsRequestOut"])
    types["NotificationIn"] = t.struct(
        {"cloudPubsubTopic": t.proxy(renames["CloudPubsubTopicIn"]).optional()}
    ).named(renames["NotificationIn"])
    types["NotificationOut"] = t.struct(
        {
            "cloudPubsubTopic": t.proxy(renames["CloudPubsubTopicOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationOut"])
    types["VoicemailMisconfigurationIn"] = t.struct(
        {"errors": t.array(t.proxy(renames["VoicemailRecipientErrorIn"])).optional()}
    ).named(renames["VoicemailMisconfigurationIn"])
    types["VoicemailMisconfigurationOut"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["VoicemailRecipientErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoicemailMisconfigurationOut"])
    types["AttachmentIn"] = t.struct(
        {"csv": t.proxy(renames["CsvIn"]).optional()}
    ).named(renames["AttachmentIn"])
    types["AttachmentOut"] = t.struct(
        {
            "csv": t.proxy(renames["CsvOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
    types["TransferMisconfigurationIn"] = t.struct(
        {"errors": t.array(t.proxy(renames["TransferErrorIn"])).optional()}
    ).named(renames["TransferMisconfigurationIn"])
    types["TransferMisconfigurationOut"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["TransferErrorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferMisconfigurationOut"])
    types["AlertIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "startTime": t.string(),
            "updateTime": t.string().optional(),
            "alertId": t.string().optional(),
            "source": t.string(),
            "customerId": t.string().optional(),
            "deleted": t.boolean().optional(),
            "endTime": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "securityInvestigationToolLink": t.string().optional(),
            "metadata": t.proxy(renames["AlertMetadataIn"]).optional(),
            "type": t.string(),
        }
    ).named(renames["AlertIn"])
    types["AlertOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "startTime": t.string(),
            "updateTime": t.string().optional(),
            "alertId": t.string().optional(),
            "source": t.string(),
            "customerId": t.string().optional(),
            "deleted": t.boolean().optional(),
            "endTime": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "securityInvestigationToolLink": t.string().optional(),
            "metadata": t.proxy(renames["AlertMetadataOut"]).optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertOut"])
    types["PrimaryAdminChangedEventIn"] = t.struct(
        {
            "previousAdminEmail": t.string().optional(),
            "domain": t.string().optional(),
            "updatedAdminEmail": t.string().optional(),
        }
    ).named(renames["PrimaryAdminChangedEventIn"])
    types["PrimaryAdminChangedEventOut"] = t.struct(
        {
            "previousAdminEmail": t.string().optional(),
            "domain": t.string().optional(),
            "updatedAdminEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrimaryAdminChangedEventOut"])
    types["DlpRuleViolationIn"] = t.struct(
        {"ruleViolationInfo": t.proxy(renames["RuleViolationInfoIn"]).optional()}
    ).named(renames["DlpRuleViolationIn"])
    types["DlpRuleViolationOut"] = t.struct(
        {
            "ruleViolationInfo": t.proxy(renames["RuleViolationInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DlpRuleViolationOut"])
    types["DomainIdIn"] = t.struct(
        {"customerPrimaryDomain": t.string().optional()}
    ).named(renames["DomainIdIn"])
    types["DomainIdOut"] = t.struct(
        {
            "customerPrimaryDomain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainIdOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["MatchInfoIn"] = t.struct(
        {
            "predefinedDetector": t.proxy(
                renames["PredefinedDetectorInfoIn"]
            ).optional(),
            "userDefinedDetector": t.proxy(
                renames["UserDefinedDetectorInfoIn"]
            ).optional(),
        }
    ).named(renames["MatchInfoIn"])
    types["MatchInfoOut"] = t.struct(
        {
            "predefinedDetector": t.proxy(
                renames["PredefinedDetectorInfoOut"]
            ).optional(),
            "userDefinedDetector": t.proxy(
                renames["UserDefinedDetectorInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatchInfoOut"])
    types["BadWhitelistIn"] = t.struct(
        {
            "domainId": t.proxy(renames["DomainIdIn"]).optional(),
            "messages": t.array(t.proxy(renames["GmailMessageInfoIn"])).optional(),
            "sourceIp": t.string().optional(),
            "maliciousEntity": t.proxy(renames["MaliciousEntityIn"]).optional(),
        }
    ).named(renames["BadWhitelistIn"])
    types["BadWhitelistOut"] = t.struct(
        {
            "domainId": t.proxy(renames["DomainIdOut"]).optional(),
            "messages": t.array(t.proxy(renames["GmailMessageInfoOut"])).optional(),
            "sourceIp": t.string().optional(),
            "maliciousEntity": t.proxy(renames["MaliciousEntityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BadWhitelistOut"])
    types["DomainWideTakeoutInitiatedIn"] = t.struct(
        {"takeoutRequestId": t.string().optional(), "email": t.string().optional()}
    ).named(renames["DomainWideTakeoutInitiatedIn"])
    types["DomainWideTakeoutInitiatedOut"] = t.struct(
        {
            "takeoutRequestId": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainWideTakeoutInitiatedOut"])
    types["SensitiveAdminActionIn"] = t.struct(
        {
            "primaryAdminChangedEvent": t.proxy(
                renames["PrimaryAdminChangedEventIn"]
            ).optional(),
            "ssoProfileDeletedEvent": t.proxy(
                renames["SSOProfileDeletedEventIn"]
            ).optional(),
            "actorEmail": t.string().optional(),
            "ssoProfileUpdatedEvent": t.proxy(
                renames["SSOProfileUpdatedEventIn"]
            ).optional(),
            "ssoProfileCreatedEvent": t.proxy(
                renames["SSOProfileCreatedEventIn"]
            ).optional(),
            "eventTime": t.string().optional(),
            "superAdminPasswordResetEvent": t.proxy(
                renames["SuperAdminPasswordResetEventIn"]
            ).optional(),
        }
    ).named(renames["SensitiveAdminActionIn"])
    types["SensitiveAdminActionOut"] = t.struct(
        {
            "primaryAdminChangedEvent": t.proxy(
                renames["PrimaryAdminChangedEventOut"]
            ).optional(),
            "ssoProfileDeletedEvent": t.proxy(
                renames["SSOProfileDeletedEventOut"]
            ).optional(),
            "actorEmail": t.string().optional(),
            "ssoProfileUpdatedEvent": t.proxy(
                renames["SSOProfileUpdatedEventOut"]
            ).optional(),
            "ssoProfileCreatedEvent": t.proxy(
                renames["SSOProfileCreatedEventOut"]
            ).optional(),
            "eventTime": t.string().optional(),
            "superAdminPasswordResetEvent": t.proxy(
                renames["SuperAdminPasswordResetEventOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SensitiveAdminActionOut"])
    types["UserDefinedDetectorInfoIn"] = t.struct(
        {"resourceName": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["UserDefinedDetectorInfoIn"])
    types["UserDefinedDetectorInfoOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserDefinedDetectorInfoOut"])
    types["UserChangesIn"] = t.struct({"name": t.string().optional()}).named(
        renames["UserChangesIn"]
    )
    types["UserChangesOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserChangesOut"])
    types["AppMakerSqlSetupNotificationIn"] = t.struct(
        {"requestInfo": t.array(t.proxy(renames["RequestInfoIn"])).optional()}
    ).named(renames["AppMakerSqlSetupNotificationIn"])
    types["AppMakerSqlSetupNotificationOut"] = t.struct(
        {
            "requestInfo": t.array(t.proxy(renames["RequestInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppMakerSqlSetupNotificationOut"])
    types["ResourceInfoIn"] = t.struct(
        {"resourceTitle": t.string().optional(), "documentId": t.string().optional()}
    ).named(renames["ResourceInfoIn"])
    types["ResourceInfoOut"] = t.struct(
        {
            "resourceTitle": t.string().optional(),
            "documentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceInfoOut"])
    types["MailPhishingIn"] = t.struct(
        {
            "systemActionType": t.string().optional(),
            "isInternal": t.boolean().optional(),
            "maliciousEntity": t.proxy(renames["MaliciousEntityIn"]).optional(),
            "domainId": t.proxy(renames["DomainIdIn"]).optional(),
            "messages": t.array(t.proxy(renames["GmailMessageInfoIn"])).optional(),
        }
    ).named(renames["MailPhishingIn"])
    types["MailPhishingOut"] = t.struct(
        {
            "systemActionType": t.string().optional(),
            "isInternal": t.boolean().optional(),
            "maliciousEntity": t.proxy(renames["MaliciousEntityOut"]).optional(),
            "domainId": t.proxy(renames["DomainIdOut"]).optional(),
            "messages": t.array(t.proxy(renames["GmailMessageInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MailPhishingOut"])
    types["SuspiciousActivityIn"] = t.struct(
        {
            "email": t.string().optional(),
            "events": t.array(t.proxy(renames["SuspiciousActivitySecurityDetailIn"])),
        }
    ).named(renames["SuspiciousActivityIn"])
    types["SuspiciousActivityOut"] = t.struct(
        {
            "email": t.string().optional(),
            "events": t.array(t.proxy(renames["SuspiciousActivitySecurityDetailOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuspiciousActivityOut"])
    types["AppsOutageIn"] = t.struct(
        {
            "dashboardUri": t.string().optional(),
            "products": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "mergeInfo": t.proxy(renames["MergeInfoIn"]).optional(),
            "nextUpdateTime": t.string().optional(),
            "resolutionTime": t.string().optional(),
            "incidentTrackingId": t.string().optional(),
        }
    ).named(renames["AppsOutageIn"])
    types["AppsOutageOut"] = t.struct(
        {
            "dashboardUri": t.string().optional(),
            "products": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "mergeInfo": t.proxy(renames["MergeInfoOut"]).optional(),
            "nextUpdateTime": t.string().optional(),
            "resolutionTime": t.string().optional(),
            "incidentTrackingId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsOutageOut"])
    types["VoicemailRecipientErrorIn"] = t.struct(
        {"invalidReason": t.string().optional(), "email": t.string().optional()}
    ).named(renames["VoicemailRecipientErrorIn"])
    types["VoicemailRecipientErrorOut"] = t.struct(
        {
            "invalidReason": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoicemailRecipientErrorOut"])
    types["MergeInfoIn"] = t.struct(
        {
            "newIncidentTrackingId": t.string().optional(),
            "newAlertId": t.string().optional(),
        }
    ).named(renames["MergeInfoIn"])
    types["MergeInfoOut"] = t.struct(
        {
            "newIncidentTrackingId": t.string().optional(),
            "newAlertId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MergeInfoOut"])
    types["AlertMetadataIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "assignee": t.string().optional(),
            "alertId": t.string().optional(),
            "customerId": t.string().optional(),
            "status": t.string().optional(),
            "etag": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["AlertMetadataIn"])
    types["AlertMetadataOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "assignee": t.string().optional(),
            "alertId": t.string().optional(),
            "customerId": t.string().optional(),
            "status": t.string().optional(),
            "etag": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertMetadataOut"])
    types["MandatoryServiceAnnouncementIn"] = t.struct(
        {"title": t.string().optional(), "description": t.string().optional()}
    ).named(renames["MandatoryServiceAnnouncementIn"])
    types["MandatoryServiceAnnouncementOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MandatoryServiceAnnouncementOut"])
    types["ActivityRuleIn"] = t.struct(
        {
            "threshold": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "supersededAlerts": t.array(t.string()).optional(),
            "windowSize": t.string().optional(),
            "actionNames": t.array(t.string()).optional(),
            "supersedingAlert": t.string().optional(),
            "displayName": t.string().optional(),
            "query": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "triggerSource": t.string().optional(),
        }
    ).named(renames["ActivityRuleIn"])
    types["ActivityRuleOut"] = t.struct(
        {
            "threshold": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "supersededAlerts": t.array(t.string()).optional(),
            "windowSize": t.string().optional(),
            "actionNames": t.array(t.string()).optional(),
            "supersedingAlert": t.string().optional(),
            "displayName": t.string().optional(),
            "query": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "triggerSource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityRuleOut"])
    types["EntityListIn"] = t.struct(
        {
            "headers": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "entities": t.array(t.proxy(renames["EntityIn"])).optional(),
        }
    ).named(renames["EntityListIn"])
    types["EntityListOut"] = t.struct(
        {
            "headers": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "entities": t.array(t.proxy(renames["EntityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityListOut"])
    types["RuleInfoIn"] = t.struct(
        {"displayName": t.string().optional(), "resourceName": t.string().optional()}
    ).named(renames["RuleInfoIn"])
    types["RuleInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleInfoOut"])

    functions = {}
    functions["v1beta1GetSettings"] = alertcenter.patch(
        "v1beta1/settings",
        t.struct(
            {
                "customerId": t.string().optional(),
                "notifications": t.array(t.proxy(renames["NotificationIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1beta1UpdateSettings"] = alertcenter.patch(
        "v1beta1/settings",
        t.struct(
            {
                "customerId": t.string().optional(),
                "notifications": t.array(t.proxy(renames["NotificationIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsList"] = alertcenter.post(
        "v1beta1/alerts/{alertId}:undelete",
        t.struct(
            {
                "alertId": t.string(),
                "customerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AlertOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsDelete"] = alertcenter.post(
        "v1beta1/alerts/{alertId}:undelete",
        t.struct(
            {
                "alertId": t.string(),
                "customerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AlertOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsGet"] = alertcenter.post(
        "v1beta1/alerts/{alertId}:undelete",
        t.struct(
            {
                "alertId": t.string(),
                "customerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AlertOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsBatchUndelete"] = alertcenter.post(
        "v1beta1/alerts/{alertId}:undelete",
        t.struct(
            {
                "alertId": t.string(),
                "customerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AlertOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsGetMetadata"] = alertcenter.post(
        "v1beta1/alerts/{alertId}:undelete",
        t.struct(
            {
                "alertId": t.string(),
                "customerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AlertOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsBatchDelete"] = alertcenter.post(
        "v1beta1/alerts/{alertId}:undelete",
        t.struct(
            {
                "alertId": t.string(),
                "customerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AlertOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsUndelete"] = alertcenter.post(
        "v1beta1/alerts/{alertId}:undelete",
        t.struct(
            {
                "alertId": t.string(),
                "customerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AlertOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsFeedbackCreate"] = alertcenter.get(
        "v1beta1/alerts/{alertId}/feedback",
        t.struct(
            {
                "alertId": t.string(),
                "customerId": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAlertFeedbackResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsFeedbackList"] = alertcenter.get(
        "v1beta1/alerts/{alertId}/feedback",
        t.struct(
            {
                "alertId": t.string(),
                "customerId": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAlertFeedbackResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="alertcenter",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
