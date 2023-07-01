from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_alertcenter():
    alertcenter = HTTPRuntime("https://alertcenter.googleapis.com/")

    renames = {
        "ErrorResponse": "_alertcenter_1_ErrorResponse",
        "AppSettingsChangedIn": "_alertcenter_2_AppSettingsChangedIn",
        "AppSettingsChangedOut": "_alertcenter_3_AppSettingsChangedOut",
        "BatchDeleteAlertsResponseIn": "_alertcenter_4_BatchDeleteAlertsResponseIn",
        "BatchDeleteAlertsResponseOut": "_alertcenter_5_BatchDeleteAlertsResponseOut",
        "MaliciousEntityIn": "_alertcenter_6_MaliciousEntityIn",
        "MaliciousEntityOut": "_alertcenter_7_MaliciousEntityOut",
        "EntityListIn": "_alertcenter_8_EntityListIn",
        "EntityListOut": "_alertcenter_9_EntityListOut",
        "AlertIn": "_alertcenter_10_AlertIn",
        "AlertOut": "_alertcenter_11_AlertOut",
        "NotificationIn": "_alertcenter_12_NotificationIn",
        "NotificationOut": "_alertcenter_13_NotificationOut",
        "ActionInfoIn": "_alertcenter_14_ActionInfoIn",
        "ActionInfoOut": "_alertcenter_15_ActionInfoOut",
        "AlertFeedbackIn": "_alertcenter_16_AlertFeedbackIn",
        "AlertFeedbackOut": "_alertcenter_17_AlertFeedbackOut",
        "PrimaryAdminChangedEventIn": "_alertcenter_18_PrimaryAdminChangedEventIn",
        "PrimaryAdminChangedEventOut": "_alertcenter_19_PrimaryAdminChangedEventOut",
        "DomainIdIn": "_alertcenter_20_DomainIdIn",
        "DomainIdOut": "_alertcenter_21_DomainIdOut",
        "CsvRowIn": "_alertcenter_22_CsvRowIn",
        "CsvRowOut": "_alertcenter_23_CsvRowOut",
        "StateSponsoredAttackIn": "_alertcenter_24_StateSponsoredAttackIn",
        "StateSponsoredAttackOut": "_alertcenter_25_StateSponsoredAttackOut",
        "RuleViolationInfoIn": "_alertcenter_26_RuleViolationInfoIn",
        "RuleViolationInfoOut": "_alertcenter_27_RuleViolationInfoOut",
        "MergeInfoIn": "_alertcenter_28_MergeInfoIn",
        "MergeInfoOut": "_alertcenter_29_MergeInfoOut",
        "VoiceMisconfigurationIn": "_alertcenter_30_VoiceMisconfigurationIn",
        "VoiceMisconfigurationOut": "_alertcenter_31_VoiceMisconfigurationOut",
        "SuspiciousActivityIn": "_alertcenter_32_SuspiciousActivityIn",
        "SuspiciousActivityOut": "_alertcenter_33_SuspiciousActivityOut",
        "ListAlertFeedbackResponseIn": "_alertcenter_34_ListAlertFeedbackResponseIn",
        "ListAlertFeedbackResponseOut": "_alertcenter_35_ListAlertFeedbackResponseOut",
        "BatchUndeleteAlertsResponseIn": "_alertcenter_36_BatchUndeleteAlertsResponseIn",
        "BatchUndeleteAlertsResponseOut": "_alertcenter_37_BatchUndeleteAlertsResponseOut",
        "AbuseDetectedIn": "_alertcenter_38_AbuseDetectedIn",
        "AbuseDetectedOut": "_alertcenter_39_AbuseDetectedOut",
        "AccountWarningIn": "_alertcenter_40_AccountWarningIn",
        "AccountWarningOut": "_alertcenter_41_AccountWarningOut",
        "ReportingRuleIn": "_alertcenter_42_ReportingRuleIn",
        "ReportingRuleOut": "_alertcenter_43_ReportingRuleOut",
        "TransferMisconfigurationIn": "_alertcenter_44_TransferMisconfigurationIn",
        "TransferMisconfigurationOut": "_alertcenter_45_TransferMisconfigurationOut",
        "LoginDetailsIn": "_alertcenter_46_LoginDetailsIn",
        "LoginDetailsOut": "_alertcenter_47_LoginDetailsOut",
        "RuleInfoIn": "_alertcenter_48_RuleInfoIn",
        "RuleInfoOut": "_alertcenter_49_RuleInfoOut",
        "AccountSuspensionWarningIn": "_alertcenter_50_AccountSuspensionWarningIn",
        "AccountSuspensionWarningOut": "_alertcenter_51_AccountSuspensionWarningOut",
        "MailPhishingIn": "_alertcenter_52_MailPhishingIn",
        "MailPhishingOut": "_alertcenter_53_MailPhishingOut",
        "AccountSuspensionDetailsIn": "_alertcenter_54_AccountSuspensionDetailsIn",
        "AccountSuspensionDetailsOut": "_alertcenter_55_AccountSuspensionDetailsOut",
        "GoogleOperationsIn": "_alertcenter_56_GoogleOperationsIn",
        "GoogleOperationsOut": "_alertcenter_57_GoogleOperationsOut",
        "ResourceInfoIn": "_alertcenter_58_ResourceInfoIn",
        "ResourceInfoOut": "_alertcenter_59_ResourceInfoOut",
        "SensitiveAdminActionIn": "_alertcenter_60_SensitiveAdminActionIn",
        "SensitiveAdminActionOut": "_alertcenter_61_SensitiveAdminActionOut",
        "SuspiciousActivitySecurityDetailIn": "_alertcenter_62_SuspiciousActivitySecurityDetailIn",
        "SuspiciousActivitySecurityDetailOut": "_alertcenter_63_SuspiciousActivitySecurityDetailOut",
        "CloudPubsubTopicIn": "_alertcenter_64_CloudPubsubTopicIn",
        "CloudPubsubTopicOut": "_alertcenter_65_CloudPubsubTopicOut",
        "AppMakerSqlSetupNotificationIn": "_alertcenter_66_AppMakerSqlSetupNotificationIn",
        "AppMakerSqlSetupNotificationOut": "_alertcenter_67_AppMakerSqlSetupNotificationOut",
        "SSOProfileDeletedEventIn": "_alertcenter_68_SSOProfileDeletedEventIn",
        "SSOProfileDeletedEventOut": "_alertcenter_69_SSOProfileDeletedEventOut",
        "DeviceCompromisedIn": "_alertcenter_70_DeviceCompromisedIn",
        "DeviceCompromisedOut": "_alertcenter_71_DeviceCompromisedOut",
        "SSOProfileUpdatedEventIn": "_alertcenter_72_SSOProfileUpdatedEventIn",
        "SSOProfileUpdatedEventOut": "_alertcenter_73_SSOProfileUpdatedEventOut",
        "DomainWideTakeoutInitiatedIn": "_alertcenter_74_DomainWideTakeoutInitiatedIn",
        "DomainWideTakeoutInitiatedOut": "_alertcenter_75_DomainWideTakeoutInitiatedOut",
        "DlpRuleViolationIn": "_alertcenter_76_DlpRuleViolationIn",
        "DlpRuleViolationOut": "_alertcenter_77_DlpRuleViolationOut",
        "MandatoryServiceAnnouncementIn": "_alertcenter_78_MandatoryServiceAnnouncementIn",
        "MandatoryServiceAnnouncementOut": "_alertcenter_79_MandatoryServiceAnnouncementOut",
        "VoicemailMisconfigurationIn": "_alertcenter_80_VoicemailMisconfigurationIn",
        "VoicemailMisconfigurationOut": "_alertcenter_81_VoicemailMisconfigurationOut",
        "ListAlertsResponseIn": "_alertcenter_82_ListAlertsResponseIn",
        "ListAlertsResponseOut": "_alertcenter_83_ListAlertsResponseOut",
        "BatchUndeleteAlertsRequestIn": "_alertcenter_84_BatchUndeleteAlertsRequestIn",
        "BatchUndeleteAlertsRequestOut": "_alertcenter_85_BatchUndeleteAlertsRequestOut",
        "EntityIn": "_alertcenter_86_EntityIn",
        "EntityOut": "_alertcenter_87_EntityOut",
        "SettingsIn": "_alertcenter_88_SettingsIn",
        "SettingsOut": "_alertcenter_89_SettingsOut",
        "ActivityRuleIn": "_alertcenter_90_ActivityRuleIn",
        "ActivityRuleOut": "_alertcenter_91_ActivityRuleOut",
        "UserIn": "_alertcenter_92_UserIn",
        "UserOut": "_alertcenter_93_UserOut",
        "BadWhitelistIn": "_alertcenter_94_BadWhitelistIn",
        "BadWhitelistOut": "_alertcenter_95_BadWhitelistOut",
        "UserChangesIn": "_alertcenter_96_UserChangesIn",
        "UserChangesOut": "_alertcenter_97_UserChangesOut",
        "CsvIn": "_alertcenter_98_CsvIn",
        "CsvOut": "_alertcenter_99_CsvOut",
        "ApnsCertificateExpirationInfoIn": "_alertcenter_100_ApnsCertificateExpirationInfoIn",
        "ApnsCertificateExpirationInfoOut": "_alertcenter_101_ApnsCertificateExpirationInfoOut",
        "AppsOutageIn": "_alertcenter_102_AppsOutageIn",
        "AppsOutageOut": "_alertcenter_103_AppsOutageOut",
        "PredefinedDetectorInfoIn": "_alertcenter_104_PredefinedDetectorInfoIn",
        "PredefinedDetectorInfoOut": "_alertcenter_105_PredefinedDetectorInfoOut",
        "BatchDeleteAlertsRequestIn": "_alertcenter_106_BatchDeleteAlertsRequestIn",
        "BatchDeleteAlertsRequestOut": "_alertcenter_107_BatchDeleteAlertsRequestOut",
        "EmptyIn": "_alertcenter_108_EmptyIn",
        "EmptyOut": "_alertcenter_109_EmptyOut",
        "UserDefinedDetectorInfoIn": "_alertcenter_110_UserDefinedDetectorInfoIn",
        "UserDefinedDetectorInfoOut": "_alertcenter_111_UserDefinedDetectorInfoOut",
        "SuperAdminPasswordResetEventIn": "_alertcenter_112_SuperAdminPasswordResetEventIn",
        "SuperAdminPasswordResetEventOut": "_alertcenter_113_SuperAdminPasswordResetEventOut",
        "UndeleteAlertRequestIn": "_alertcenter_114_UndeleteAlertRequestIn",
        "UndeleteAlertRequestOut": "_alertcenter_115_UndeleteAlertRequestOut",
        "GmailMessageInfoIn": "_alertcenter_116_GmailMessageInfoIn",
        "GmailMessageInfoOut": "_alertcenter_117_GmailMessageInfoOut",
        "TransferErrorIn": "_alertcenter_118_TransferErrorIn",
        "TransferErrorOut": "_alertcenter_119_TransferErrorOut",
        "PhishingSpikeIn": "_alertcenter_120_PhishingSpikeIn",
        "PhishingSpikeOut": "_alertcenter_121_PhishingSpikeOut",
        "AlertMetadataIn": "_alertcenter_122_AlertMetadataIn",
        "AlertMetadataOut": "_alertcenter_123_AlertMetadataOut",
        "StatusIn": "_alertcenter_124_StatusIn",
        "StatusOut": "_alertcenter_125_StatusOut",
        "MatchInfoIn": "_alertcenter_126_MatchInfoIn",
        "MatchInfoOut": "_alertcenter_127_MatchInfoOut",
        "RequestInfoIn": "_alertcenter_128_RequestInfoIn",
        "RequestInfoOut": "_alertcenter_129_RequestInfoOut",
        "DeviceCompromisedSecurityDetailIn": "_alertcenter_130_DeviceCompromisedSecurityDetailIn",
        "DeviceCompromisedSecurityDetailOut": "_alertcenter_131_DeviceCompromisedSecurityDetailOut",
        "SSOProfileCreatedEventIn": "_alertcenter_132_SSOProfileCreatedEventIn",
        "SSOProfileCreatedEventOut": "_alertcenter_133_SSOProfileCreatedEventOut",
        "AttachmentIn": "_alertcenter_134_AttachmentIn",
        "AttachmentOut": "_alertcenter_135_AttachmentOut",
        "VoicemailRecipientErrorIn": "_alertcenter_136_VoicemailRecipientErrorIn",
        "VoicemailRecipientErrorOut": "_alertcenter_137_VoicemailRecipientErrorOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["AlertIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "etag": t.string().optional(),
            "metadata": t.proxy(renames["AlertMetadataIn"]).optional(),
            "endTime": t.string().optional(),
            "deleted": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "source": t.string(),
            "startTime": t.string(),
            "customerId": t.string().optional(),
            "securityInvestigationToolLink": t.string().optional(),
            "alertId": t.string().optional(),
            "type": t.string(),
        }
    ).named(renames["AlertIn"])
    types["AlertOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "etag": t.string().optional(),
            "metadata": t.proxy(renames["AlertMetadataOut"]).optional(),
            "endTime": t.string().optional(),
            "deleted": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "source": t.string(),
            "startTime": t.string(),
            "customerId": t.string().optional(),
            "securityInvestigationToolLink": t.string().optional(),
            "alertId": t.string().optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertOut"])
    types["NotificationIn"] = t.struct(
        {"cloudPubsubTopic": t.proxy(renames["CloudPubsubTopicIn"]).optional()}
    ).named(renames["NotificationIn"])
    types["NotificationOut"] = t.struct(
        {
            "cloudPubsubTopic": t.proxy(renames["CloudPubsubTopicOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationOut"])
    types["ActionInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ActionInfoIn"]
    )
    types["ActionInfoOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActionInfoOut"])
    types["AlertFeedbackIn"] = t.struct(
        {
            "email": t.string().optional(),
            "type": t.string(),
            "alertId": t.string().optional(),
            "customerId": t.string().optional(),
            "feedbackId": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["AlertFeedbackIn"])
    types["AlertFeedbackOut"] = t.struct(
        {
            "email": t.string().optional(),
            "type": t.string(),
            "alertId": t.string().optional(),
            "customerId": t.string().optional(),
            "feedbackId": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertFeedbackOut"])
    types["PrimaryAdminChangedEventIn"] = t.struct(
        {
            "domain": t.string().optional(),
            "previousAdminEmail": t.string().optional(),
            "updatedAdminEmail": t.string().optional(),
        }
    ).named(renames["PrimaryAdminChangedEventIn"])
    types["PrimaryAdminChangedEventOut"] = t.struct(
        {
            "domain": t.string().optional(),
            "previousAdminEmail": t.string().optional(),
            "updatedAdminEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrimaryAdminChangedEventOut"])
    types["DomainIdIn"] = t.struct(
        {"customerPrimaryDomain": t.string().optional()}
    ).named(renames["DomainIdIn"])
    types["DomainIdOut"] = t.struct(
        {
            "customerPrimaryDomain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainIdOut"])
    types["CsvRowIn"] = t.struct({"entries": t.array(t.string()).optional()}).named(
        renames["CsvRowIn"]
    )
    types["CsvRowOut"] = t.struct(
        {
            "entries": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CsvRowOut"])
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
            "triggeredActionInfo": t.array(t.proxy(renames["ActionInfoIn"])).optional(),
            "trigger": t.string().optional(),
            "triggeringUserEmail": t.string().optional(),
            "triggeredActionTypes": t.array(t.string()).optional(),
            "resourceInfo": t.proxy(renames["ResourceInfoIn"]).optional(),
            "dataSource": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "ruleInfo": t.proxy(renames["RuleInfoIn"]).optional(),
            "matchInfo": t.array(t.proxy(renames["MatchInfoIn"])).optional(),
            "suppressedActionTypes": t.array(t.string()).optional(),
        }
    ).named(renames["RuleViolationInfoIn"])
    types["RuleViolationInfoOut"] = t.struct(
        {
            "triggeredActionInfo": t.array(
                t.proxy(renames["ActionInfoOut"])
            ).optional(),
            "trigger": t.string().optional(),
            "triggeringUserEmail": t.string().optional(),
            "triggeredActionTypes": t.array(t.string()).optional(),
            "resourceInfo": t.proxy(renames["ResourceInfoOut"]).optional(),
            "dataSource": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "ruleInfo": t.proxy(renames["RuleInfoOut"]).optional(),
            "matchInfo": t.array(t.proxy(renames["MatchInfoOut"])).optional(),
            "suppressedActionTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleViolationInfoOut"])
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
    types["VoiceMisconfigurationIn"] = t.struct(
        {
            "fixUri": t.string().optional(),
            "entityName": t.string().optional(),
            "transferMisconfiguration": t.proxy(
                renames["TransferMisconfigurationIn"]
            ).optional(),
            "membersMisconfiguration": t.proxy(
                renames["TransferMisconfigurationIn"]
            ).optional(),
            "entityType": t.string().optional(),
            "voicemailMisconfiguration": t.proxy(
                renames["VoicemailMisconfigurationIn"]
            ).optional(),
        }
    ).named(renames["VoiceMisconfigurationIn"])
    types["VoiceMisconfigurationOut"] = t.struct(
        {
            "fixUri": t.string().optional(),
            "entityName": t.string().optional(),
            "transferMisconfiguration": t.proxy(
                renames["TransferMisconfigurationOut"]
            ).optional(),
            "membersMisconfiguration": t.proxy(
                renames["TransferMisconfigurationOut"]
            ).optional(),
            "entityType": t.string().optional(),
            "voicemailMisconfiguration": t.proxy(
                renames["VoicemailMisconfigurationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceMisconfigurationOut"])
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
    types["ListAlertFeedbackResponseIn"] = t.struct(
        {"feedback": t.array(t.proxy(renames["AlertFeedbackIn"])).optional()}
    ).named(renames["ListAlertFeedbackResponseIn"])
    types["ListAlertFeedbackResponseOut"] = t.struct(
        {
            "feedback": t.array(t.proxy(renames["AlertFeedbackOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAlertFeedbackResponseOut"])
    types["BatchUndeleteAlertsResponseIn"] = t.struct(
        {
            "failedAlertStatus": t.struct({"_": t.string().optional()}).optional(),
            "successAlertIds": t.array(t.string()).optional(),
        }
    ).named(renames["BatchUndeleteAlertsResponseIn"])
    types["BatchUndeleteAlertsResponseOut"] = t.struct(
        {
            "failedAlertStatus": t.struct({"_": t.string().optional()}).optional(),
            "successAlertIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUndeleteAlertsResponseOut"])
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
    types["TransferMisconfigurationIn"] = t.struct(
        {"errors": t.array(t.proxy(renames["TransferErrorIn"])).optional()}
    ).named(renames["TransferMisconfigurationIn"])
    types["TransferMisconfigurationOut"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["TransferErrorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferMisconfigurationOut"])
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
    types["MailPhishingIn"] = t.struct(
        {
            "isInternal": t.boolean().optional(),
            "maliciousEntity": t.proxy(renames["MaliciousEntityIn"]).optional(),
            "domainId": t.proxy(renames["DomainIdIn"]).optional(),
            "messages": t.array(t.proxy(renames["GmailMessageInfoIn"])).optional(),
            "systemActionType": t.string().optional(),
        }
    ).named(renames["MailPhishingIn"])
    types["MailPhishingOut"] = t.struct(
        {
            "isInternal": t.boolean().optional(),
            "maliciousEntity": t.proxy(renames["MaliciousEntityOut"]).optional(),
            "domainId": t.proxy(renames["DomainIdOut"]).optional(),
            "messages": t.array(t.proxy(renames["GmailMessageInfoOut"])).optional(),
            "systemActionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MailPhishingOut"])
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
    types["GoogleOperationsIn"] = t.struct(
        {
            "description": t.string().optional(),
            "affectedUserEmails": t.array(t.string()).optional(),
            "attachmentData": t.proxy(renames["AttachmentIn"]).optional(),
            "header": t.string().optional(),
            "title": t.string().optional(),
            "domain": t.string().optional(),
        }
    ).named(renames["GoogleOperationsIn"])
    types["GoogleOperationsOut"] = t.struct(
        {
            "description": t.string().optional(),
            "affectedUserEmails": t.array(t.string()).optional(),
            "attachmentData": t.proxy(renames["AttachmentOut"]).optional(),
            "header": t.string().optional(),
            "title": t.string().optional(),
            "domain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleOperationsOut"])
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
    types["SensitiveAdminActionIn"] = t.struct(
        {
            "ssoProfileCreatedEvent": t.proxy(
                renames["SSOProfileCreatedEventIn"]
            ).optional(),
            "ssoProfileDeletedEvent": t.proxy(
                renames["SSOProfileDeletedEventIn"]
            ).optional(),
            "primaryAdminChangedEvent": t.proxy(
                renames["PrimaryAdminChangedEventIn"]
            ).optional(),
            "actorEmail": t.string().optional(),
            "eventTime": t.string().optional(),
            "superAdminPasswordResetEvent": t.proxy(
                renames["SuperAdminPasswordResetEventIn"]
            ).optional(),
            "ssoProfileUpdatedEvent": t.proxy(
                renames["SSOProfileUpdatedEventIn"]
            ).optional(),
        }
    ).named(renames["SensitiveAdminActionIn"])
    types["SensitiveAdminActionOut"] = t.struct(
        {
            "ssoProfileCreatedEvent": t.proxy(
                renames["SSOProfileCreatedEventOut"]
            ).optional(),
            "ssoProfileDeletedEvent": t.proxy(
                renames["SSOProfileDeletedEventOut"]
            ).optional(),
            "primaryAdminChangedEvent": t.proxy(
                renames["PrimaryAdminChangedEventOut"]
            ).optional(),
            "actorEmail": t.string().optional(),
            "eventTime": t.string().optional(),
            "superAdminPasswordResetEvent": t.proxy(
                renames["SuperAdminPasswordResetEventOut"]
            ).optional(),
            "ssoProfileUpdatedEvent": t.proxy(
                renames["SSOProfileUpdatedEventOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SensitiveAdminActionOut"])
    types["SuspiciousActivitySecurityDetailIn"] = t.struct(
        {
            "oldValue": t.string().optional(),
            "deviceType": t.string().optional(),
            "serialNumber": t.string().optional(),
            "deviceProperty": t.string().optional(),
            "iosVendorId": t.string(),
            "deviceId": t.string(),
            "newValue": t.string().optional(),
            "resourceId": t.string().optional(),
            "deviceModel": t.string().optional(),
        }
    ).named(renames["SuspiciousActivitySecurityDetailIn"])
    types["SuspiciousActivitySecurityDetailOut"] = t.struct(
        {
            "oldValue": t.string().optional(),
            "deviceType": t.string().optional(),
            "serialNumber": t.string().optional(),
            "deviceProperty": t.string().optional(),
            "iosVendorId": t.string(),
            "deviceId": t.string(),
            "newValue": t.string().optional(),
            "resourceId": t.string().optional(),
            "deviceModel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuspiciousActivitySecurityDetailOut"])
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
    types["AppMakerSqlSetupNotificationIn"] = t.struct(
        {"requestInfo": t.array(t.proxy(renames["RequestInfoIn"])).optional()}
    ).named(renames["AppMakerSqlSetupNotificationIn"])
    types["AppMakerSqlSetupNotificationOut"] = t.struct(
        {
            "requestInfo": t.array(t.proxy(renames["RequestInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppMakerSqlSetupNotificationOut"])
    types["SSOProfileDeletedEventIn"] = t.struct(
        {"inboundSsoProfileName": t.string().optional()}
    ).named(renames["SSOProfileDeletedEventIn"])
    types["SSOProfileDeletedEventOut"] = t.struct(
        {
            "inboundSsoProfileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SSOProfileDeletedEventOut"])
    types["DeviceCompromisedIn"] = t.struct(
        {
            "events": t.array(t.proxy(renames["DeviceCompromisedSecurityDetailIn"])),
            "email": t.string().optional(),
        }
    ).named(renames["DeviceCompromisedIn"])
    types["DeviceCompromisedOut"] = t.struct(
        {
            "events": t.array(t.proxy(renames["DeviceCompromisedSecurityDetailOut"])),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceCompromisedOut"])
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
    types["DlpRuleViolationIn"] = t.struct(
        {"ruleViolationInfo": t.proxy(renames["RuleViolationInfoIn"]).optional()}
    ).named(renames["DlpRuleViolationIn"])
    types["DlpRuleViolationOut"] = t.struct(
        {
            "ruleViolationInfo": t.proxy(renames["RuleViolationInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DlpRuleViolationOut"])
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
    types["ListAlertsResponseIn"] = t.struct(
        {
            "alerts": t.array(t.proxy(renames["AlertIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAlertsResponseIn"])
    types["ListAlertsResponseOut"] = t.struct(
        {
            "alerts": t.array(t.proxy(renames["AlertOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAlertsResponseOut"])
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
    types["EntityIn"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "link": t.string().optional(),
        }
    ).named(renames["EntityIn"])
    types["EntityOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "link": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityOut"])
    types["SettingsIn"] = t.struct(
        {"notifications": t.array(t.proxy(renames["NotificationIn"])).optional()}
    ).named(renames["SettingsIn"])
    types["SettingsOut"] = t.struct(
        {
            "notifications": t.array(t.proxy(renames["NotificationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsOut"])
    types["ActivityRuleIn"] = t.struct(
        {
            "query": t.string().optional(),
            "updateTime": t.string().optional(),
            "threshold": t.string().optional(),
            "displayName": t.string().optional(),
            "actionNames": t.array(t.string()).optional(),
            "windowSize": t.string().optional(),
            "triggerSource": t.string().optional(),
            "createTime": t.string().optional(),
            "supersededAlerts": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "supersedingAlert": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ActivityRuleIn"])
    types["ActivityRuleOut"] = t.struct(
        {
            "query": t.string().optional(),
            "updateTime": t.string().optional(),
            "threshold": t.string().optional(),
            "displayName": t.string().optional(),
            "actionNames": t.array(t.string()).optional(),
            "windowSize": t.string().optional(),
            "triggerSource": t.string().optional(),
            "createTime": t.string().optional(),
            "supersededAlerts": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "supersedingAlert": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityRuleOut"])
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
    types["BadWhitelistIn"] = t.struct(
        {
            "messages": t.array(t.proxy(renames["GmailMessageInfoIn"])).optional(),
            "domainId": t.proxy(renames["DomainIdIn"]).optional(),
            "sourceIp": t.string().optional(),
            "maliciousEntity": t.proxy(renames["MaliciousEntityIn"]).optional(),
        }
    ).named(renames["BadWhitelistIn"])
    types["BadWhitelistOut"] = t.struct(
        {
            "messages": t.array(t.proxy(renames["GmailMessageInfoOut"])).optional(),
            "domainId": t.proxy(renames["DomainIdOut"]).optional(),
            "sourceIp": t.string().optional(),
            "maliciousEntity": t.proxy(renames["MaliciousEntityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BadWhitelistOut"])
    types["UserChangesIn"] = t.struct({"name": t.string().optional()}).named(
        renames["UserChangesIn"]
    )
    types["UserChangesOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserChangesOut"])
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
    types["ApnsCertificateExpirationInfoIn"] = t.struct(
        {
            "expirationTime": t.string().optional(),
            "uid": t.string().optional(),
            "appleId": t.string().optional(),
        }
    ).named(renames["ApnsCertificateExpirationInfoIn"])
    types["ApnsCertificateExpirationInfoOut"] = t.struct(
        {
            "expirationTime": t.string().optional(),
            "uid": t.string().optional(),
            "appleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApnsCertificateExpirationInfoOut"])
    types["AppsOutageIn"] = t.struct(
        {
            "products": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "mergeInfo": t.proxy(renames["MergeInfoIn"]).optional(),
            "incidentTrackingId": t.string().optional(),
            "nextUpdateTime": t.string().optional(),
            "dashboardUri": t.string().optional(),
            "resolutionTime": t.string().optional(),
        }
    ).named(renames["AppsOutageIn"])
    types["AppsOutageOut"] = t.struct(
        {
            "products": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "mergeInfo": t.proxy(renames["MergeInfoOut"]).optional(),
            "incidentTrackingId": t.string().optional(),
            "nextUpdateTime": t.string().optional(),
            "dashboardUri": t.string().optional(),
            "resolutionTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsOutageOut"])
    types["PredefinedDetectorInfoIn"] = t.struct(
        {"detectorName": t.string().optional()}
    ).named(renames["PredefinedDetectorInfoIn"])
    types["PredefinedDetectorInfoOut"] = t.struct(
        {
            "detectorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PredefinedDetectorInfoOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["UserDefinedDetectorInfoIn"] = t.struct(
        {"displayName": t.string().optional(), "resourceName": t.string().optional()}
    ).named(renames["UserDefinedDetectorInfoIn"])
    types["UserDefinedDetectorInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserDefinedDetectorInfoOut"])
    types["SuperAdminPasswordResetEventIn"] = t.struct(
        {"userEmail": t.string().optional()}
    ).named(renames["SuperAdminPasswordResetEventIn"])
    types["SuperAdminPasswordResetEventOut"] = t.struct(
        {
            "userEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuperAdminPasswordResetEventOut"])
    types["UndeleteAlertRequestIn"] = t.struct(
        {"customerId": t.string().optional()}
    ).named(renames["UndeleteAlertRequestIn"])
    types["UndeleteAlertRequestOut"] = t.struct(
        {
            "customerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UndeleteAlertRequestOut"])
    types["GmailMessageInfoIn"] = t.struct(
        {
            "messageId": t.string().optional(),
            "sentTime": t.string().optional(),
            "date": t.string().optional(),
            "subjectText": t.string().optional(),
            "recipient": t.string().optional(),
            "attachmentsSha256Hash": t.array(t.string()).optional(),
            "md5HashMessageBody": t.string().optional(),
            "md5HashSubject": t.string().optional(),
            "messageBodySnippet": t.string().optional(),
        }
    ).named(renames["GmailMessageInfoIn"])
    types["GmailMessageInfoOut"] = t.struct(
        {
            "messageId": t.string().optional(),
            "sentTime": t.string().optional(),
            "date": t.string().optional(),
            "subjectText": t.string().optional(),
            "recipient": t.string().optional(),
            "attachmentsSha256Hash": t.array(t.string()).optional(),
            "md5HashMessageBody": t.string().optional(),
            "md5HashSubject": t.string().optional(),
            "messageBodySnippet": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GmailMessageInfoOut"])
    types["TransferErrorIn"] = t.struct(
        {
            "id": t.string().optional(),
            "email": t.string().optional(),
            "entityType": t.string().optional(),
            "invalidReason": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TransferErrorIn"])
    types["TransferErrorOut"] = t.struct(
        {
            "id": t.string().optional(),
            "email": t.string().optional(),
            "entityType": t.string().optional(),
            "invalidReason": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferErrorOut"])
    types["PhishingSpikeIn"] = t.struct(
        {
            "domainId": t.proxy(renames["DomainIdIn"]).optional(),
            "messages": t.array(t.proxy(renames["GmailMessageInfoIn"])).optional(),
            "maliciousEntity": t.proxy(renames["MaliciousEntityIn"]).optional(),
            "isInternal": t.boolean().optional(),
        }
    ).named(renames["PhishingSpikeIn"])
    types["PhishingSpikeOut"] = t.struct(
        {
            "domainId": t.proxy(renames["DomainIdOut"]).optional(),
            "messages": t.array(t.proxy(renames["GmailMessageInfoOut"])).optional(),
            "maliciousEntity": t.proxy(renames["MaliciousEntityOut"]).optional(),
            "isInternal": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhishingSpikeOut"])
    types["AlertMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "alertId": t.string().optional(),
            "status": t.string().optional(),
            "severity": t.string().optional(),
            "assignee": t.string().optional(),
            "customerId": t.string().optional(),
        }
    ).named(renames["AlertMetadataIn"])
    types["AlertMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "alertId": t.string().optional(),
            "status": t.string().optional(),
            "severity": t.string().optional(),
            "assignee": t.string().optional(),
            "customerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertMetadataOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["RequestInfoIn"] = t.struct(
        {
            "numberOfRequests": t.string(),
            "appKey": t.string(),
            "appDeveloperEmail": t.array(t.string()).optional(),
        }
    ).named(renames["RequestInfoIn"])
    types["RequestInfoOut"] = t.struct(
        {
            "numberOfRequests": t.string(),
            "appKey": t.string(),
            "appDeveloperEmail": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestInfoOut"])
    types["DeviceCompromisedSecurityDetailIn"] = t.struct(
        {
            "serialNumber": t.string().optional(),
            "deviceCompromisedState": t.string().optional(),
            "deviceModel": t.string().optional(),
            "deviceId": t.string(),
            "deviceType": t.string().optional(),
            "iosVendorId": t.string(),
            "resourceId": t.string().optional(),
        }
    ).named(renames["DeviceCompromisedSecurityDetailIn"])
    types["DeviceCompromisedSecurityDetailOut"] = t.struct(
        {
            "serialNumber": t.string().optional(),
            "deviceCompromisedState": t.string().optional(),
            "deviceModel": t.string().optional(),
            "deviceId": t.string(),
            "deviceType": t.string().optional(),
            "iosVendorId": t.string(),
            "resourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceCompromisedSecurityDetailOut"])
    types["SSOProfileCreatedEventIn"] = t.struct(
        {"inboundSsoProfileName": t.string().optional()}
    ).named(renames["SSOProfileCreatedEventIn"])
    types["SSOProfileCreatedEventOut"] = t.struct(
        {
            "inboundSsoProfileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SSOProfileCreatedEventOut"])
    types["AttachmentIn"] = t.struct(
        {"csv": t.proxy(renames["CsvIn"]).optional()}
    ).named(renames["AttachmentIn"])
    types["AttachmentOut"] = t.struct(
        {
            "csv": t.proxy(renames["CsvOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
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

    functions = {}
    functions["alertsBatchDelete"] = alertcenter.delete(
        "v1beta1/alerts/{alertId}",
        t.struct(
            {
                "customerId": t.string().optional(),
                "alertId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsList"] = alertcenter.delete(
        "v1beta1/alerts/{alertId}",
        t.struct(
            {
                "customerId": t.string().optional(),
                "alertId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsGet"] = alertcenter.delete(
        "v1beta1/alerts/{alertId}",
        t.struct(
            {
                "customerId": t.string().optional(),
                "alertId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsUndelete"] = alertcenter.delete(
        "v1beta1/alerts/{alertId}",
        t.struct(
            {
                "customerId": t.string().optional(),
                "alertId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsGetMetadata"] = alertcenter.delete(
        "v1beta1/alerts/{alertId}",
        t.struct(
            {
                "customerId": t.string().optional(),
                "alertId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsBatchUndelete"] = alertcenter.delete(
        "v1beta1/alerts/{alertId}",
        t.struct(
            {
                "customerId": t.string().optional(),
                "alertId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["alertsDelete"] = alertcenter.delete(
        "v1beta1/alerts/{alertId}",
        t.struct(
            {
                "customerId": t.string().optional(),
                "alertId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
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
    functions["v1beta1UpdateSettings"] = alertcenter.get(
        "v1beta1/settings",
        t.struct({"customerId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1beta1GetSettings"] = alertcenter.get(
        "v1beta1/settings",
        t.struct({"customerId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="alertcenter",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
