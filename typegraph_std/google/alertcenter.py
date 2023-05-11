from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_alertcenter() -> Import:
    alertcenter = HTTPRuntime("https://alertcenter.googleapis.com/")

    renames = {
        "ErrorResponse": "_alertcenter_1_ErrorResponse",
        "CsvIn": "_alertcenter_2_CsvIn",
        "CsvOut": "_alertcenter_3_CsvOut",
        "MergeInfoIn": "_alertcenter_4_MergeInfoIn",
        "MergeInfoOut": "_alertcenter_5_MergeInfoOut",
        "MaliciousEntityIn": "_alertcenter_6_MaliciousEntityIn",
        "MaliciousEntityOut": "_alertcenter_7_MaliciousEntityOut",
        "RuleInfoIn": "_alertcenter_8_RuleInfoIn",
        "RuleInfoOut": "_alertcenter_9_RuleInfoOut",
        "BatchDeleteAlertsResponseIn": "_alertcenter_10_BatchDeleteAlertsResponseIn",
        "BatchDeleteAlertsResponseOut": "_alertcenter_11_BatchDeleteAlertsResponseOut",
        "AlertIn": "_alertcenter_12_AlertIn",
        "AlertOut": "_alertcenter_13_AlertOut",
        "AccountWarningIn": "_alertcenter_14_AccountWarningIn",
        "AccountWarningOut": "_alertcenter_15_AccountWarningOut",
        "SuspiciousActivityIn": "_alertcenter_16_SuspiciousActivityIn",
        "SuspiciousActivityOut": "_alertcenter_17_SuspiciousActivityOut",
        "SSOProfileUpdatedEventIn": "_alertcenter_18_SSOProfileUpdatedEventIn",
        "SSOProfileUpdatedEventOut": "_alertcenter_19_SSOProfileUpdatedEventOut",
        "GoogleOperationsIn": "_alertcenter_20_GoogleOperationsIn",
        "GoogleOperationsOut": "_alertcenter_21_GoogleOperationsOut",
        "AlertMetadataIn": "_alertcenter_22_AlertMetadataIn",
        "AlertMetadataOut": "_alertcenter_23_AlertMetadataOut",
        "PredefinedDetectorInfoIn": "_alertcenter_24_PredefinedDetectorInfoIn",
        "PredefinedDetectorInfoOut": "_alertcenter_25_PredefinedDetectorInfoOut",
        "ListAlertFeedbackResponseIn": "_alertcenter_26_ListAlertFeedbackResponseIn",
        "ListAlertFeedbackResponseOut": "_alertcenter_27_ListAlertFeedbackResponseOut",
        "MandatoryServiceAnnouncementIn": "_alertcenter_28_MandatoryServiceAnnouncementIn",
        "MandatoryServiceAnnouncementOut": "_alertcenter_29_MandatoryServiceAnnouncementOut",
        "VoicemailMisconfigurationIn": "_alertcenter_30_VoicemailMisconfigurationIn",
        "VoicemailMisconfigurationOut": "_alertcenter_31_VoicemailMisconfigurationOut",
        "BatchUndeleteAlertsRequestIn": "_alertcenter_32_BatchUndeleteAlertsRequestIn",
        "BatchUndeleteAlertsRequestOut": "_alertcenter_33_BatchUndeleteAlertsRequestOut",
        "SSOProfileDeletedEventIn": "_alertcenter_34_SSOProfileDeletedEventIn",
        "SSOProfileDeletedEventOut": "_alertcenter_35_SSOProfileDeletedEventOut",
        "AbuseDetectedIn": "_alertcenter_36_AbuseDetectedIn",
        "AbuseDetectedOut": "_alertcenter_37_AbuseDetectedOut",
        "AppMakerSqlSetupNotificationIn": "_alertcenter_38_AppMakerSqlSetupNotificationIn",
        "AppMakerSqlSetupNotificationOut": "_alertcenter_39_AppMakerSqlSetupNotificationOut",
        "AttachmentIn": "_alertcenter_40_AttachmentIn",
        "AttachmentOut": "_alertcenter_41_AttachmentOut",
        "ReportingRuleIn": "_alertcenter_42_ReportingRuleIn",
        "ReportingRuleOut": "_alertcenter_43_ReportingRuleOut",
        "DomainWideTakeoutInitiatedIn": "_alertcenter_44_DomainWideTakeoutInitiatedIn",
        "DomainWideTakeoutInitiatedOut": "_alertcenter_45_DomainWideTakeoutInitiatedOut",
        "AlertFeedbackIn": "_alertcenter_46_AlertFeedbackIn",
        "AlertFeedbackOut": "_alertcenter_47_AlertFeedbackOut",
        "CloudPubsubTopicIn": "_alertcenter_48_CloudPubsubTopicIn",
        "CloudPubsubTopicOut": "_alertcenter_49_CloudPubsubTopicOut",
        "BatchDeleteAlertsRequestIn": "_alertcenter_50_BatchDeleteAlertsRequestIn",
        "BatchDeleteAlertsRequestOut": "_alertcenter_51_BatchDeleteAlertsRequestOut",
        "EntityIn": "_alertcenter_52_EntityIn",
        "EntityOut": "_alertcenter_53_EntityOut",
        "CsvRowIn": "_alertcenter_54_CsvRowIn",
        "CsvRowOut": "_alertcenter_55_CsvRowOut",
        "DeviceCompromisedIn": "_alertcenter_56_DeviceCompromisedIn",
        "DeviceCompromisedOut": "_alertcenter_57_DeviceCompromisedOut",
        "AccountSuspensionDetailsIn": "_alertcenter_58_AccountSuspensionDetailsIn",
        "AccountSuspensionDetailsOut": "_alertcenter_59_AccountSuspensionDetailsOut",
        "BatchUndeleteAlertsResponseIn": "_alertcenter_60_BatchUndeleteAlertsResponseIn",
        "BatchUndeleteAlertsResponseOut": "_alertcenter_61_BatchUndeleteAlertsResponseOut",
        "RequestInfoIn": "_alertcenter_62_RequestInfoIn",
        "RequestInfoOut": "_alertcenter_63_RequestInfoOut",
        "SettingsIn": "_alertcenter_64_SettingsIn",
        "SettingsOut": "_alertcenter_65_SettingsOut",
        "SuspiciousActivitySecurityDetailIn": "_alertcenter_66_SuspiciousActivitySecurityDetailIn",
        "SuspiciousActivitySecurityDetailOut": "_alertcenter_67_SuspiciousActivitySecurityDetailOut",
        "ActionInfoIn": "_alertcenter_68_ActionInfoIn",
        "ActionInfoOut": "_alertcenter_69_ActionInfoOut",
        "EntityListIn": "_alertcenter_70_EntityListIn",
        "EntityListOut": "_alertcenter_71_EntityListOut",
        "PhishingSpikeIn": "_alertcenter_72_PhishingSpikeIn",
        "PhishingSpikeOut": "_alertcenter_73_PhishingSpikeOut",
        "VoiceMisconfigurationIn": "_alertcenter_74_VoiceMisconfigurationIn",
        "VoiceMisconfigurationOut": "_alertcenter_75_VoiceMisconfigurationOut",
        "GmailMessageInfoIn": "_alertcenter_76_GmailMessageInfoIn",
        "GmailMessageInfoOut": "_alertcenter_77_GmailMessageInfoOut",
        "ActivityRuleIn": "_alertcenter_78_ActivityRuleIn",
        "ActivityRuleOut": "_alertcenter_79_ActivityRuleOut",
        "TransferErrorIn": "_alertcenter_80_TransferErrorIn",
        "TransferErrorOut": "_alertcenter_81_TransferErrorOut",
        "TransferMisconfigurationIn": "_alertcenter_82_TransferMisconfigurationIn",
        "TransferMisconfigurationOut": "_alertcenter_83_TransferMisconfigurationOut",
        "VoicemailRecipientErrorIn": "_alertcenter_84_VoicemailRecipientErrorIn",
        "VoicemailRecipientErrorOut": "_alertcenter_85_VoicemailRecipientErrorOut",
        "SensitiveAdminActionIn": "_alertcenter_86_SensitiveAdminActionIn",
        "SensitiveAdminActionOut": "_alertcenter_87_SensitiveAdminActionOut",
        "RuleViolationInfoIn": "_alertcenter_88_RuleViolationInfoIn",
        "RuleViolationInfoOut": "_alertcenter_89_RuleViolationInfoOut",
        "MailPhishingIn": "_alertcenter_90_MailPhishingIn",
        "MailPhishingOut": "_alertcenter_91_MailPhishingOut",
        "UserChangesIn": "_alertcenter_92_UserChangesIn",
        "UserChangesOut": "_alertcenter_93_UserChangesOut",
        "StatusIn": "_alertcenter_94_StatusIn",
        "StatusOut": "_alertcenter_95_StatusOut",
        "ListAlertsResponseIn": "_alertcenter_96_ListAlertsResponseIn",
        "ListAlertsResponseOut": "_alertcenter_97_ListAlertsResponseOut",
        "PrimaryAdminChangedEventIn": "_alertcenter_98_PrimaryAdminChangedEventIn",
        "PrimaryAdminChangedEventOut": "_alertcenter_99_PrimaryAdminChangedEventOut",
        "BadWhitelistIn": "_alertcenter_100_BadWhitelistIn",
        "BadWhitelistOut": "_alertcenter_101_BadWhitelistOut",
        "NotificationIn": "_alertcenter_102_NotificationIn",
        "NotificationOut": "_alertcenter_103_NotificationOut",
        "MatchInfoIn": "_alertcenter_104_MatchInfoIn",
        "MatchInfoOut": "_alertcenter_105_MatchInfoOut",
        "StateSponsoredAttackIn": "_alertcenter_106_StateSponsoredAttackIn",
        "StateSponsoredAttackOut": "_alertcenter_107_StateSponsoredAttackOut",
        "AccountSuspensionWarningIn": "_alertcenter_108_AccountSuspensionWarningIn",
        "AccountSuspensionWarningOut": "_alertcenter_109_AccountSuspensionWarningOut",
        "UserDefinedDetectorInfoIn": "_alertcenter_110_UserDefinedDetectorInfoIn",
        "UserDefinedDetectorInfoOut": "_alertcenter_111_UserDefinedDetectorInfoOut",
        "AppSettingsChangedIn": "_alertcenter_112_AppSettingsChangedIn",
        "AppSettingsChangedOut": "_alertcenter_113_AppSettingsChangedOut",
        "ResourceInfoIn": "_alertcenter_114_ResourceInfoIn",
        "ResourceInfoOut": "_alertcenter_115_ResourceInfoOut",
        "SSOProfileCreatedEventIn": "_alertcenter_116_SSOProfileCreatedEventIn",
        "SSOProfileCreatedEventOut": "_alertcenter_117_SSOProfileCreatedEventOut",
        "DomainIdIn": "_alertcenter_118_DomainIdIn",
        "DomainIdOut": "_alertcenter_119_DomainIdOut",
        "EmptyIn": "_alertcenter_120_EmptyIn",
        "EmptyOut": "_alertcenter_121_EmptyOut",
        "LoginDetailsIn": "_alertcenter_122_LoginDetailsIn",
        "LoginDetailsOut": "_alertcenter_123_LoginDetailsOut",
        "UndeleteAlertRequestIn": "_alertcenter_124_UndeleteAlertRequestIn",
        "UndeleteAlertRequestOut": "_alertcenter_125_UndeleteAlertRequestOut",
        "SuperAdminPasswordResetEventIn": "_alertcenter_126_SuperAdminPasswordResetEventIn",
        "SuperAdminPasswordResetEventOut": "_alertcenter_127_SuperAdminPasswordResetEventOut",
        "DlpRuleViolationIn": "_alertcenter_128_DlpRuleViolationIn",
        "DlpRuleViolationOut": "_alertcenter_129_DlpRuleViolationOut",
        "AppsOutageIn": "_alertcenter_130_AppsOutageIn",
        "AppsOutageOut": "_alertcenter_131_AppsOutageOut",
        "ApnsCertificateExpirationInfoIn": "_alertcenter_132_ApnsCertificateExpirationInfoIn",
        "ApnsCertificateExpirationInfoOut": "_alertcenter_133_ApnsCertificateExpirationInfoOut",
        "DeviceCompromisedSecurityDetailIn": "_alertcenter_134_DeviceCompromisedSecurityDetailIn",
        "DeviceCompromisedSecurityDetailOut": "_alertcenter_135_DeviceCompromisedSecurityDetailOut",
        "UserIn": "_alertcenter_136_UserIn",
        "UserOut": "_alertcenter_137_UserOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CsvIn"] = t.struct(
        {
            "dataRows": t.array(t.proxy(renames["CsvRowIn"])).optional(),
            "headers": t.array(t.string()).optional(),
        }
    ).named(renames["CsvIn"])
    types["CsvOut"] = t.struct(
        {
            "dataRows": t.array(t.proxy(renames["CsvRowOut"])).optional(),
            "headers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CsvOut"])
    types["MergeInfoIn"] = t.struct(
        {
            "newAlertId": t.string().optional(),
            "newIncidentTrackingId": t.string().optional(),
        }
    ).named(renames["MergeInfoIn"])
    types["MergeInfoOut"] = t.struct(
        {
            "newAlertId": t.string().optional(),
            "newIncidentTrackingId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MergeInfoOut"])
    types["MaliciousEntityIn"] = t.struct(
        {
            "fromHeader": t.string().optional(),
            "displayName": t.string().optional(),
            "entity": t.proxy(renames["UserIn"]).optional(),
        }
    ).named(renames["MaliciousEntityIn"])
    types["MaliciousEntityOut"] = t.struct(
        {
            "fromHeader": t.string().optional(),
            "displayName": t.string().optional(),
            "entity": t.proxy(renames["UserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaliciousEntityOut"])
    types["RuleInfoIn"] = t.struct(
        {"resourceName": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["RuleInfoIn"])
    types["RuleInfoOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleInfoOut"])
    types["BatchDeleteAlertsResponseIn"] = t.struct(
        {
            "successAlertIds": t.array(t.string()).optional(),
            "failedAlertStatus": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["BatchDeleteAlertsResponseIn"])
    types["BatchDeleteAlertsResponseOut"] = t.struct(
        {
            "successAlertIds": t.array(t.string()).optional(),
            "failedAlertStatus": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteAlertsResponseOut"])
    types["AlertIn"] = t.struct(
        {
            "deleted": t.boolean().optional(),
            "endTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "alertId": t.string().optional(),
            "type": t.string(),
            "securityInvestigationToolLink": t.string().optional(),
            "customerId": t.string().optional(),
            "source": t.string(),
            "metadata": t.proxy(renames["AlertMetadataIn"]).optional(),
            "etag": t.string().optional(),
            "startTime": t.string(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["AlertIn"])
    types["AlertOut"] = t.struct(
        {
            "deleted": t.boolean().optional(),
            "endTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "alertId": t.string().optional(),
            "type": t.string(),
            "securityInvestigationToolLink": t.string().optional(),
            "customerId": t.string().optional(),
            "source": t.string(),
            "metadata": t.proxy(renames["AlertMetadataOut"]).optional(),
            "etag": t.string().optional(),
            "startTime": t.string(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertOut"])
    types["AccountWarningIn"] = t.struct(
        {
            "loginDetails": t.proxy(renames["LoginDetailsIn"]).optional(),
            "email": t.string(),
        }
    ).named(renames["AccountWarningIn"])
    types["AccountWarningOut"] = t.struct(
        {
            "loginDetails": t.proxy(renames["LoginDetailsOut"]).optional(),
            "email": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountWarningOut"])
    types["SuspiciousActivityIn"] = t.struct(
        {
            "events": t.array(t.proxy(renames["SuspiciousActivitySecurityDetailIn"])),
            "email": t.string().optional(),
        }
    ).named(renames["SuspiciousActivityIn"])
    types["SuspiciousActivityOut"] = t.struct(
        {
            "events": t.array(t.proxy(renames["SuspiciousActivitySecurityDetailOut"])),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuspiciousActivityOut"])
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
    types["GoogleOperationsIn"] = t.struct(
        {
            "description": t.string().optional(),
            "header": t.string().optional(),
            "domain": t.string().optional(),
            "attachmentData": t.proxy(renames["AttachmentIn"]).optional(),
            "affectedUserEmails": t.array(t.string()).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["GoogleOperationsIn"])
    types["GoogleOperationsOut"] = t.struct(
        {
            "description": t.string().optional(),
            "header": t.string().optional(),
            "domain": t.string().optional(),
            "attachmentData": t.proxy(renames["AttachmentOut"]).optional(),
            "affectedUserEmails": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleOperationsOut"])
    types["AlertMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "customerId": t.string().optional(),
            "alertId": t.string().optional(),
            "assignee": t.string().optional(),
            "etag": t.string().optional(),
            "severity": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["AlertMetadataIn"])
    types["AlertMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "customerId": t.string().optional(),
            "alertId": t.string().optional(),
            "assignee": t.string().optional(),
            "etag": t.string().optional(),
            "severity": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertMetadataOut"])
    types["PredefinedDetectorInfoIn"] = t.struct(
        {"detectorName": t.string().optional()}
    ).named(renames["PredefinedDetectorInfoIn"])
    types["PredefinedDetectorInfoOut"] = t.struct(
        {
            "detectorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PredefinedDetectorInfoOut"])
    types["ListAlertFeedbackResponseIn"] = t.struct(
        {"feedback": t.array(t.proxy(renames["AlertFeedbackIn"])).optional()}
    ).named(renames["ListAlertFeedbackResponseIn"])
    types["ListAlertFeedbackResponseOut"] = t.struct(
        {
            "feedback": t.array(t.proxy(renames["AlertFeedbackOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAlertFeedbackResponseOut"])
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
    types["BatchUndeleteAlertsRequestIn"] = t.struct(
        {"alertId": t.array(t.string()), "customerId": t.string().optional()}
    ).named(renames["BatchUndeleteAlertsRequestIn"])
    types["BatchUndeleteAlertsRequestOut"] = t.struct(
        {
            "alertId": t.array(t.string()),
            "customerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUndeleteAlertsRequestOut"])
    types["SSOProfileDeletedEventIn"] = t.struct(
        {"inboundSsoProfileName": t.string().optional()}
    ).named(renames["SSOProfileDeletedEventIn"])
    types["SSOProfileDeletedEventOut"] = t.struct(
        {
            "inboundSsoProfileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SSOProfileDeletedEventOut"])
    types["AbuseDetectedIn"] = t.struct(
        {
            "variationType": t.string().optional(),
            "subAlertId": t.string().optional(),
            "additionalDetails": t.proxy(renames["EntityListIn"]).optional(),
            "product": t.string().optional(),
        }
    ).named(renames["AbuseDetectedIn"])
    types["AbuseDetectedOut"] = t.struct(
        {
            "variationType": t.string().optional(),
            "subAlertId": t.string().optional(),
            "additionalDetails": t.proxy(renames["EntityListOut"]).optional(),
            "product": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AbuseDetectedOut"])
    types["AppMakerSqlSetupNotificationIn"] = t.struct(
        {"requestInfo": t.array(t.proxy(renames["RequestInfoIn"])).optional()}
    ).named(renames["AppMakerSqlSetupNotificationIn"])
    types["AppMakerSqlSetupNotificationOut"] = t.struct(
        {
            "requestInfo": t.array(t.proxy(renames["RequestInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppMakerSqlSetupNotificationOut"])
    types["AttachmentIn"] = t.struct(
        {"csv": t.proxy(renames["CsvIn"]).optional()}
    ).named(renames["AttachmentIn"])
    types["AttachmentOut"] = t.struct(
        {
            "csv": t.proxy(renames["CsvOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
    types["ReportingRuleIn"] = t.struct(
        {
            "alertDetails": t.string().optional(),
            "query": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ReportingRuleIn"])
    types["ReportingRuleOut"] = t.struct(
        {
            "alertDetails": t.string().optional(),
            "query": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportingRuleOut"])
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
    types["AlertFeedbackIn"] = t.struct(
        {
            "alertId": t.string().optional(),
            "email": t.string().optional(),
            "customerId": t.string().optional(),
            "feedbackId": t.string().optional(),
            "type": t.string(),
            "createTime": t.string().optional(),
        }
    ).named(renames["AlertFeedbackIn"])
    types["AlertFeedbackOut"] = t.struct(
        {
            "alertId": t.string().optional(),
            "email": t.string().optional(),
            "customerId": t.string().optional(),
            "feedbackId": t.string().optional(),
            "type": t.string(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertFeedbackOut"])
    types["CloudPubsubTopicIn"] = t.struct(
        {"topicName": t.string().optional(), "payloadFormat": t.string().optional()}
    ).named(renames["CloudPubsubTopicIn"])
    types["CloudPubsubTopicOut"] = t.struct(
        {
            "topicName": t.string().optional(),
            "payloadFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudPubsubTopicOut"])
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
    types["EntityIn"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "link": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["EntityIn"])
    types["EntityOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "link": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityOut"])
    types["CsvRowIn"] = t.struct({"entries": t.array(t.string()).optional()}).named(
        renames["CsvRowIn"]
    )
    types["CsvRowOut"] = t.struct(
        {
            "entries": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CsvRowOut"])
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
    types["AccountSuspensionDetailsIn"] = t.struct(
        {"productName": t.string().optional(), "abuseReason": t.string().optional()}
    ).named(renames["AccountSuspensionDetailsIn"])
    types["AccountSuspensionDetailsOut"] = t.struct(
        {
            "productName": t.string().optional(),
            "abuseReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountSuspensionDetailsOut"])
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
            "numberOfRequests": t.string(),
            "appDeveloperEmail": t.array(t.string()).optional(),
            "appKey": t.string(),
        }
    ).named(renames["RequestInfoIn"])
    types["RequestInfoOut"] = t.struct(
        {
            "numberOfRequests": t.string(),
            "appDeveloperEmail": t.array(t.string()).optional(),
            "appKey": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestInfoOut"])
    types["SettingsIn"] = t.struct(
        {"notifications": t.array(t.proxy(renames["NotificationIn"])).optional()}
    ).named(renames["SettingsIn"])
    types["SettingsOut"] = t.struct(
        {
            "notifications": t.array(t.proxy(renames["NotificationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsOut"])
    types["SuspiciousActivitySecurityDetailIn"] = t.struct(
        {
            "deviceModel": t.string().optional(),
            "newValue": t.string().optional(),
            "deviceType": t.string().optional(),
            "deviceProperty": t.string().optional(),
            "serialNumber": t.string().optional(),
            "resourceId": t.string().optional(),
            "oldValue": t.string().optional(),
            "deviceId": t.string(),
            "iosVendorId": t.string(),
        }
    ).named(renames["SuspiciousActivitySecurityDetailIn"])
    types["SuspiciousActivitySecurityDetailOut"] = t.struct(
        {
            "deviceModel": t.string().optional(),
            "newValue": t.string().optional(),
            "deviceType": t.string().optional(),
            "deviceProperty": t.string().optional(),
            "serialNumber": t.string().optional(),
            "resourceId": t.string().optional(),
            "oldValue": t.string().optional(),
            "deviceId": t.string(),
            "iosVendorId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuspiciousActivitySecurityDetailOut"])
    types["ActionInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ActionInfoIn"]
    )
    types["ActionInfoOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActionInfoOut"])
    types["EntityListIn"] = t.struct(
        {
            "entities": t.array(t.proxy(renames["EntityIn"])).optional(),
            "name": t.string().optional(),
            "headers": t.array(t.string()).optional(),
        }
    ).named(renames["EntityListIn"])
    types["EntityListOut"] = t.struct(
        {
            "entities": t.array(t.proxy(renames["EntityOut"])).optional(),
            "name": t.string().optional(),
            "headers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityListOut"])
    types["PhishingSpikeIn"] = t.struct(
        {
            "isInternal": t.boolean().optional(),
            "maliciousEntity": t.proxy(renames["MaliciousEntityIn"]).optional(),
            "messages": t.array(t.proxy(renames["GmailMessageInfoIn"])).optional(),
            "domainId": t.proxy(renames["DomainIdIn"]).optional(),
        }
    ).named(renames["PhishingSpikeIn"])
    types["PhishingSpikeOut"] = t.struct(
        {
            "isInternal": t.boolean().optional(),
            "maliciousEntity": t.proxy(renames["MaliciousEntityOut"]).optional(),
            "messages": t.array(t.proxy(renames["GmailMessageInfoOut"])).optional(),
            "domainId": t.proxy(renames["DomainIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhishingSpikeOut"])
    types["VoiceMisconfigurationIn"] = t.struct(
        {
            "entityName": t.string().optional(),
            "entityType": t.string().optional(),
            "membersMisconfiguration": t.proxy(
                renames["TransferMisconfigurationIn"]
            ).optional(),
            "voicemailMisconfiguration": t.proxy(
                renames["VoicemailMisconfigurationIn"]
            ).optional(),
            "transferMisconfiguration": t.proxy(
                renames["TransferMisconfigurationIn"]
            ).optional(),
            "fixUri": t.string().optional(),
        }
    ).named(renames["VoiceMisconfigurationIn"])
    types["VoiceMisconfigurationOut"] = t.struct(
        {
            "entityName": t.string().optional(),
            "entityType": t.string().optional(),
            "membersMisconfiguration": t.proxy(
                renames["TransferMisconfigurationOut"]
            ).optional(),
            "voicemailMisconfiguration": t.proxy(
                renames["VoicemailMisconfigurationOut"]
            ).optional(),
            "transferMisconfiguration": t.proxy(
                renames["TransferMisconfigurationOut"]
            ).optional(),
            "fixUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceMisconfigurationOut"])
    types["GmailMessageInfoIn"] = t.struct(
        {
            "attachmentsSha256Hash": t.array(t.string()).optional(),
            "md5HashSubject": t.string().optional(),
            "subjectText": t.string().optional(),
            "messageBodySnippet": t.string().optional(),
            "md5HashMessageBody": t.string().optional(),
            "messageId": t.string().optional(),
            "sentTime": t.string().optional(),
            "recipient": t.string().optional(),
            "date": t.string().optional(),
        }
    ).named(renames["GmailMessageInfoIn"])
    types["GmailMessageInfoOut"] = t.struct(
        {
            "attachmentsSha256Hash": t.array(t.string()).optional(),
            "md5HashSubject": t.string().optional(),
            "subjectText": t.string().optional(),
            "messageBodySnippet": t.string().optional(),
            "md5HashMessageBody": t.string().optional(),
            "messageId": t.string().optional(),
            "sentTime": t.string().optional(),
            "recipient": t.string().optional(),
            "date": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GmailMessageInfoOut"])
    types["ActivityRuleIn"] = t.struct(
        {
            "threshold": t.string().optional(),
            "query": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "supersededAlerts": t.array(t.string()).optional(),
            "windowSize": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "triggerSource": t.string().optional(),
            "actionNames": t.array(t.string()).optional(),
            "supersedingAlert": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["ActivityRuleIn"])
    types["ActivityRuleOut"] = t.struct(
        {
            "threshold": t.string().optional(),
            "query": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "supersededAlerts": t.array(t.string()).optional(),
            "windowSize": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "triggerSource": t.string().optional(),
            "actionNames": t.array(t.string()).optional(),
            "supersedingAlert": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityRuleOut"])
    types["TransferErrorIn"] = t.struct(
        {
            "entityType": t.string().optional(),
            "invalidReason": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "email": t.string().optional(),
        }
    ).named(renames["TransferErrorIn"])
    types["TransferErrorOut"] = t.struct(
        {
            "entityType": t.string().optional(),
            "invalidReason": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferErrorOut"])
    types["TransferMisconfigurationIn"] = t.struct(
        {"errors": t.array(t.proxy(renames["TransferErrorIn"])).optional()}
    ).named(renames["TransferMisconfigurationIn"])
    types["TransferMisconfigurationOut"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["TransferErrorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferMisconfigurationOut"])
    types["VoicemailRecipientErrorIn"] = t.struct(
        {"email": t.string().optional(), "invalidReason": t.string().optional()}
    ).named(renames["VoicemailRecipientErrorIn"])
    types["VoicemailRecipientErrorOut"] = t.struct(
        {
            "email": t.string().optional(),
            "invalidReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoicemailRecipientErrorOut"])
    types["SensitiveAdminActionIn"] = t.struct(
        {
            "ssoProfileCreatedEvent": t.proxy(
                renames["SSOProfileCreatedEventIn"]
            ).optional(),
            "eventTime": t.string().optional(),
            "superAdminPasswordResetEvent": t.proxy(
                renames["SuperAdminPasswordResetEventIn"]
            ).optional(),
            "ssoProfileUpdatedEvent": t.proxy(
                renames["SSOProfileUpdatedEventIn"]
            ).optional(),
            "actorEmail": t.string().optional(),
            "ssoProfileDeletedEvent": t.proxy(
                renames["SSOProfileDeletedEventIn"]
            ).optional(),
            "primaryAdminChangedEvent": t.proxy(
                renames["PrimaryAdminChangedEventIn"]
            ).optional(),
        }
    ).named(renames["SensitiveAdminActionIn"])
    types["SensitiveAdminActionOut"] = t.struct(
        {
            "ssoProfileCreatedEvent": t.proxy(
                renames["SSOProfileCreatedEventOut"]
            ).optional(),
            "eventTime": t.string().optional(),
            "superAdminPasswordResetEvent": t.proxy(
                renames["SuperAdminPasswordResetEventOut"]
            ).optional(),
            "ssoProfileUpdatedEvent": t.proxy(
                renames["SSOProfileUpdatedEventOut"]
            ).optional(),
            "actorEmail": t.string().optional(),
            "ssoProfileDeletedEvent": t.proxy(
                renames["SSOProfileDeletedEventOut"]
            ).optional(),
            "primaryAdminChangedEvent": t.proxy(
                renames["PrimaryAdminChangedEventOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SensitiveAdminActionOut"])
    types["RuleViolationInfoIn"] = t.struct(
        {
            "triggeringUserEmail": t.string().optional(),
            "ruleInfo": t.proxy(renames["RuleInfoIn"]).optional(),
            "suppressedActionTypes": t.array(t.string()).optional(),
            "triggeredActionTypes": t.array(t.string()).optional(),
            "triggeredActionInfo": t.array(t.proxy(renames["ActionInfoIn"])).optional(),
            "dataSource": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "resourceInfo": t.proxy(renames["ResourceInfoIn"]).optional(),
            "matchInfo": t.array(t.proxy(renames["MatchInfoIn"])).optional(),
            "trigger": t.string().optional(),
        }
    ).named(renames["RuleViolationInfoIn"])
    types["RuleViolationInfoOut"] = t.struct(
        {
            "triggeringUserEmail": t.string().optional(),
            "ruleInfo": t.proxy(renames["RuleInfoOut"]).optional(),
            "suppressedActionTypes": t.array(t.string()).optional(),
            "triggeredActionTypes": t.array(t.string()).optional(),
            "triggeredActionInfo": t.array(
                t.proxy(renames["ActionInfoOut"])
            ).optional(),
            "dataSource": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "resourceInfo": t.proxy(renames["ResourceInfoOut"]).optional(),
            "matchInfo": t.array(t.proxy(renames["MatchInfoOut"])).optional(),
            "trigger": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleViolationInfoOut"])
    types["MailPhishingIn"] = t.struct(
        {
            "maliciousEntity": t.proxy(renames["MaliciousEntityIn"]).optional(),
            "messages": t.array(t.proxy(renames["GmailMessageInfoIn"])).optional(),
            "isInternal": t.boolean().optional(),
            "domainId": t.proxy(renames["DomainIdIn"]).optional(),
            "systemActionType": t.string().optional(),
        }
    ).named(renames["MailPhishingIn"])
    types["MailPhishingOut"] = t.struct(
        {
            "maliciousEntity": t.proxy(renames["MaliciousEntityOut"]).optional(),
            "messages": t.array(t.proxy(renames["GmailMessageInfoOut"])).optional(),
            "isInternal": t.boolean().optional(),
            "domainId": t.proxy(renames["DomainIdOut"]).optional(),
            "systemActionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MailPhishingOut"])
    types["UserChangesIn"] = t.struct({"name": t.string().optional()}).named(
        renames["UserChangesIn"]
    )
    types["UserChangesOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserChangesOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["PrimaryAdminChangedEventIn"] = t.struct(
        {
            "updatedAdminEmail": t.string().optional(),
            "domain": t.string().optional(),
            "previousAdminEmail": t.string().optional(),
        }
    ).named(renames["PrimaryAdminChangedEventIn"])
    types["PrimaryAdminChangedEventOut"] = t.struct(
        {
            "updatedAdminEmail": t.string().optional(),
            "domain": t.string().optional(),
            "previousAdminEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrimaryAdminChangedEventOut"])
    types["BadWhitelistIn"] = t.struct(
        {
            "messages": t.array(t.proxy(renames["GmailMessageInfoIn"])).optional(),
            "sourceIp": t.string().optional(),
            "maliciousEntity": t.proxy(renames["MaliciousEntityIn"]).optional(),
            "domainId": t.proxy(renames["DomainIdIn"]).optional(),
        }
    ).named(renames["BadWhitelistIn"])
    types["BadWhitelistOut"] = t.struct(
        {
            "messages": t.array(t.proxy(renames["GmailMessageInfoOut"])).optional(),
            "sourceIp": t.string().optional(),
            "maliciousEntity": t.proxy(renames["MaliciousEntityOut"]).optional(),
            "domainId": t.proxy(renames["DomainIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BadWhitelistOut"])
    types["NotificationIn"] = t.struct(
        {"cloudPubsubTopic": t.proxy(renames["CloudPubsubTopicIn"]).optional()}
    ).named(renames["NotificationIn"])
    types["NotificationOut"] = t.struct(
        {
            "cloudPubsubTopic": t.proxy(renames["CloudPubsubTopicOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationOut"])
    types["MatchInfoIn"] = t.struct(
        {
            "userDefinedDetector": t.proxy(
                renames["UserDefinedDetectorInfoIn"]
            ).optional(),
            "predefinedDetector": t.proxy(
                renames["PredefinedDetectorInfoIn"]
            ).optional(),
        }
    ).named(renames["MatchInfoIn"])
    types["MatchInfoOut"] = t.struct(
        {
            "userDefinedDetector": t.proxy(
                renames["UserDefinedDetectorInfoOut"]
            ).optional(),
            "predefinedDetector": t.proxy(
                renames["PredefinedDetectorInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatchInfoOut"])
    types["StateSponsoredAttackIn"] = t.struct({"email": t.string().optional()}).named(
        renames["StateSponsoredAttackIn"]
    )
    types["StateSponsoredAttackOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StateSponsoredAttackOut"])
    types["AccountSuspensionWarningIn"] = t.struct(
        {
            "state": t.string().optional(),
            "suspensionDetails": t.array(
                t.proxy(renames["AccountSuspensionDetailsIn"])
            ).optional(),
            "appealWindow": t.string().optional(),
        }
    ).named(renames["AccountSuspensionWarningIn"])
    types["AccountSuspensionWarningOut"] = t.struct(
        {
            "state": t.string().optional(),
            "suspensionDetails": t.array(
                t.proxy(renames["AccountSuspensionDetailsOut"])
            ).optional(),
            "appealWindow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountSuspensionWarningOut"])
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
    types["AppSettingsChangedIn"] = t.struct(
        {"alertDetails": t.string().optional(), "name": t.string().optional()}
    ).named(renames["AppSettingsChangedIn"])
    types["AppSettingsChangedOut"] = t.struct(
        {
            "alertDetails": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppSettingsChangedOut"])
    types["ResourceInfoIn"] = t.struct(
        {"documentId": t.string().optional(), "resourceTitle": t.string().optional()}
    ).named(renames["ResourceInfoIn"])
    types["ResourceInfoOut"] = t.struct(
        {
            "documentId": t.string().optional(),
            "resourceTitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceInfoOut"])
    types["SSOProfileCreatedEventIn"] = t.struct(
        {"inboundSsoProfileName": t.string().optional()}
    ).named(renames["SSOProfileCreatedEventIn"])
    types["SSOProfileCreatedEventOut"] = t.struct(
        {
            "inboundSsoProfileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SSOProfileCreatedEventOut"])
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
    types["LoginDetailsIn"] = t.struct(
        {"ipAddress": t.string().optional(), "loginTime": t.string().optional()}
    ).named(renames["LoginDetailsIn"])
    types["LoginDetailsOut"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "loginTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoginDetailsOut"])
    types["UndeleteAlertRequestIn"] = t.struct(
        {"customerId": t.string().optional()}
    ).named(renames["UndeleteAlertRequestIn"])
    types["UndeleteAlertRequestOut"] = t.struct(
        {
            "customerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UndeleteAlertRequestOut"])
    types["SuperAdminPasswordResetEventIn"] = t.struct(
        {"userEmail": t.string().optional()}
    ).named(renames["SuperAdminPasswordResetEventIn"])
    types["SuperAdminPasswordResetEventOut"] = t.struct(
        {
            "userEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuperAdminPasswordResetEventOut"])
    types["DlpRuleViolationIn"] = t.struct(
        {"ruleViolationInfo": t.proxy(renames["RuleViolationInfoIn"]).optional()}
    ).named(renames["DlpRuleViolationIn"])
    types["DlpRuleViolationOut"] = t.struct(
        {
            "ruleViolationInfo": t.proxy(renames["RuleViolationInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DlpRuleViolationOut"])
    types["AppsOutageIn"] = t.struct(
        {
            "mergeInfo": t.proxy(renames["MergeInfoIn"]).optional(),
            "status": t.string().optional(),
            "nextUpdateTime": t.string().optional(),
            "incidentTrackingId": t.string().optional(),
            "products": t.array(t.string()).optional(),
            "dashboardUri": t.string().optional(),
            "resolutionTime": t.string().optional(),
        }
    ).named(renames["AppsOutageIn"])
    types["AppsOutageOut"] = t.struct(
        {
            "mergeInfo": t.proxy(renames["MergeInfoOut"]).optional(),
            "status": t.string().optional(),
            "nextUpdateTime": t.string().optional(),
            "incidentTrackingId": t.string().optional(),
            "products": t.array(t.string()).optional(),
            "dashboardUri": t.string().optional(),
            "resolutionTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsOutageOut"])
    types["ApnsCertificateExpirationInfoIn"] = t.struct(
        {
            "expirationTime": t.string().optional(),
            "appleId": t.string().optional(),
            "uid": t.string().optional(),
        }
    ).named(renames["ApnsCertificateExpirationInfoIn"])
    types["ApnsCertificateExpirationInfoOut"] = t.struct(
        {
            "expirationTime": t.string().optional(),
            "appleId": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApnsCertificateExpirationInfoOut"])
    types["DeviceCompromisedSecurityDetailIn"] = t.struct(
        {
            "deviceId": t.string(),
            "deviceModel": t.string().optional(),
            "deviceCompromisedState": t.string().optional(),
            "serialNumber": t.string().optional(),
            "deviceType": t.string().optional(),
            "resourceId": t.string().optional(),
            "iosVendorId": t.string(),
        }
    ).named(renames["DeviceCompromisedSecurityDetailIn"])
    types["DeviceCompromisedSecurityDetailOut"] = t.struct(
        {
            "deviceId": t.string(),
            "deviceModel": t.string().optional(),
            "deviceCompromisedState": t.string().optional(),
            "serialNumber": t.string().optional(),
            "deviceType": t.string().optional(),
            "resourceId": t.string().optional(),
            "iosVendorId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceCompromisedSecurityDetailOut"])
    types["UserIn"] = t.struct(
        {"displayName": t.string().optional(), "emailAddress": t.string().optional()}
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "emailAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])

    functions = {}
    functions["alertsGetMetadata"] = alertcenter.post(
        "v1beta1/alerts:batchDelete",
        t.struct(
            {
                "customerId": t.string().optional(),
                "alertId": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchDeleteAlertsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsUndelete"] = alertcenter.post(
        "v1beta1/alerts:batchDelete",
        t.struct(
            {
                "customerId": t.string().optional(),
                "alertId": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchDeleteAlertsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsBatchUndelete"] = alertcenter.post(
        "v1beta1/alerts:batchDelete",
        t.struct(
            {
                "customerId": t.string().optional(),
                "alertId": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchDeleteAlertsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsList"] = alertcenter.post(
        "v1beta1/alerts:batchDelete",
        t.struct(
            {
                "customerId": t.string().optional(),
                "alertId": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchDeleteAlertsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsGet"] = alertcenter.post(
        "v1beta1/alerts:batchDelete",
        t.struct(
            {
                "customerId": t.string().optional(),
                "alertId": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchDeleteAlertsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsDelete"] = alertcenter.post(
        "v1beta1/alerts:batchDelete",
        t.struct(
            {
                "customerId": t.string().optional(),
                "alertId": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchDeleteAlertsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsBatchDelete"] = alertcenter.post(
        "v1beta1/alerts:batchDelete",
        t.struct(
            {
                "customerId": t.string().optional(),
                "alertId": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchDeleteAlertsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsFeedbackCreate"] = alertcenter.get(
        "v1beta1/alerts/{alertId}/feedback",
        t.struct(
            {
                "filter": t.string().optional(),
                "customerId": t.string().optional(),
                "alertId": t.string(),
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
                "filter": t.string().optional(),
                "customerId": t.string().optional(),
                "alertId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAlertFeedbackResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
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

    return Import(
        importer="alertcenter", renames=renames, types=types, functions=functions
    )
