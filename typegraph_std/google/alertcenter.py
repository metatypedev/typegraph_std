from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_alertcenter() -> Import:
    alertcenter = HTTPRuntime("https://alertcenter.googleapis.com/")

    renames = {
        "ErrorResponse": "_alertcenter_1_ErrorResponse",
        "SuperAdminPasswordResetEventIn": "_alertcenter_2_SuperAdminPasswordResetEventIn",
        "SuperAdminPasswordResetEventOut": "_alertcenter_3_SuperAdminPasswordResetEventOut",
        "AppsOutageIn": "_alertcenter_4_AppsOutageIn",
        "AppsOutageOut": "_alertcenter_5_AppsOutageOut",
        "AppSettingsChangedIn": "_alertcenter_6_AppSettingsChangedIn",
        "AppSettingsChangedOut": "_alertcenter_7_AppSettingsChangedOut",
        "SettingsIn": "_alertcenter_8_SettingsIn",
        "SettingsOut": "_alertcenter_9_SettingsOut",
        "UserChangesIn": "_alertcenter_10_UserChangesIn",
        "UserChangesOut": "_alertcenter_11_UserChangesOut",
        "ResourceInfoIn": "_alertcenter_12_ResourceInfoIn",
        "ResourceInfoOut": "_alertcenter_13_ResourceInfoOut",
        "MandatoryServiceAnnouncementIn": "_alertcenter_14_MandatoryServiceAnnouncementIn",
        "MandatoryServiceAnnouncementOut": "_alertcenter_15_MandatoryServiceAnnouncementOut",
        "StateSponsoredAttackIn": "_alertcenter_16_StateSponsoredAttackIn",
        "StateSponsoredAttackOut": "_alertcenter_17_StateSponsoredAttackOut",
        "AccountSuspensionDetailsIn": "_alertcenter_18_AccountSuspensionDetailsIn",
        "AccountSuspensionDetailsOut": "_alertcenter_19_AccountSuspensionDetailsOut",
        "SuspiciousActivitySecurityDetailIn": "_alertcenter_20_SuspiciousActivitySecurityDetailIn",
        "SuspiciousActivitySecurityDetailOut": "_alertcenter_21_SuspiciousActivitySecurityDetailOut",
        "VoiceMisconfigurationIn": "_alertcenter_22_VoiceMisconfigurationIn",
        "VoiceMisconfigurationOut": "_alertcenter_23_VoiceMisconfigurationOut",
        "SSOProfileCreatedEventIn": "_alertcenter_24_SSOProfileCreatedEventIn",
        "SSOProfileCreatedEventOut": "_alertcenter_25_SSOProfileCreatedEventOut",
        "BatchDeleteAlertsResponseIn": "_alertcenter_26_BatchDeleteAlertsResponseIn",
        "BatchDeleteAlertsResponseOut": "_alertcenter_27_BatchDeleteAlertsResponseOut",
        "UserDefinedDetectorInfoIn": "_alertcenter_28_UserDefinedDetectorInfoIn",
        "UserDefinedDetectorInfoOut": "_alertcenter_29_UserDefinedDetectorInfoOut",
        "SSOProfileUpdatedEventIn": "_alertcenter_30_SSOProfileUpdatedEventIn",
        "SSOProfileUpdatedEventOut": "_alertcenter_31_SSOProfileUpdatedEventOut",
        "MailPhishingIn": "_alertcenter_32_MailPhishingIn",
        "MailPhishingOut": "_alertcenter_33_MailPhishingOut",
        "LoginDetailsIn": "_alertcenter_34_LoginDetailsIn",
        "LoginDetailsOut": "_alertcenter_35_LoginDetailsOut",
        "SSOProfileDeletedEventIn": "_alertcenter_36_SSOProfileDeletedEventIn",
        "SSOProfileDeletedEventOut": "_alertcenter_37_SSOProfileDeletedEventOut",
        "NotificationIn": "_alertcenter_38_NotificationIn",
        "NotificationOut": "_alertcenter_39_NotificationOut",
        "DeviceCompromisedSecurityDetailIn": "_alertcenter_40_DeviceCompromisedSecurityDetailIn",
        "DeviceCompromisedSecurityDetailOut": "_alertcenter_41_DeviceCompromisedSecurityDetailOut",
        "ReportingRuleIn": "_alertcenter_42_ReportingRuleIn",
        "ReportingRuleOut": "_alertcenter_43_ReportingRuleOut",
        "MaliciousEntityIn": "_alertcenter_44_MaliciousEntityIn",
        "MaliciousEntityOut": "_alertcenter_45_MaliciousEntityOut",
        "AccountWarningIn": "_alertcenter_46_AccountWarningIn",
        "AccountWarningOut": "_alertcenter_47_AccountWarningOut",
        "BadWhitelistIn": "_alertcenter_48_BadWhitelistIn",
        "BadWhitelistOut": "_alertcenter_49_BadWhitelistOut",
        "PhishingSpikeIn": "_alertcenter_50_PhishingSpikeIn",
        "PhishingSpikeOut": "_alertcenter_51_PhishingSpikeOut",
        "AlertIn": "_alertcenter_52_AlertIn",
        "AlertOut": "_alertcenter_53_AlertOut",
        "RuleViolationInfoIn": "_alertcenter_54_RuleViolationInfoIn",
        "RuleViolationInfoOut": "_alertcenter_55_RuleViolationInfoOut",
        "VoicemailMisconfigurationIn": "_alertcenter_56_VoicemailMisconfigurationIn",
        "VoicemailMisconfigurationOut": "_alertcenter_57_VoicemailMisconfigurationOut",
        "CloudPubsubTopicIn": "_alertcenter_58_CloudPubsubTopicIn",
        "CloudPubsubTopicOut": "_alertcenter_59_CloudPubsubTopicOut",
        "AlertMetadataIn": "_alertcenter_60_AlertMetadataIn",
        "AlertMetadataOut": "_alertcenter_61_AlertMetadataOut",
        "RequestInfoIn": "_alertcenter_62_RequestInfoIn",
        "RequestInfoOut": "_alertcenter_63_RequestInfoOut",
        "CsvRowIn": "_alertcenter_64_CsvRowIn",
        "CsvRowOut": "_alertcenter_65_CsvRowOut",
        "DomainIdIn": "_alertcenter_66_DomainIdIn",
        "DomainIdOut": "_alertcenter_67_DomainIdOut",
        "DomainWideTakeoutInitiatedIn": "_alertcenter_68_DomainWideTakeoutInitiatedIn",
        "DomainWideTakeoutInitiatedOut": "_alertcenter_69_DomainWideTakeoutInitiatedOut",
        "UserIn": "_alertcenter_70_UserIn",
        "UserOut": "_alertcenter_71_UserOut",
        "ListAlertsResponseIn": "_alertcenter_72_ListAlertsResponseIn",
        "ListAlertsResponseOut": "_alertcenter_73_ListAlertsResponseOut",
        "MergeInfoIn": "_alertcenter_74_MergeInfoIn",
        "MergeInfoOut": "_alertcenter_75_MergeInfoOut",
        "StatusIn": "_alertcenter_76_StatusIn",
        "StatusOut": "_alertcenter_77_StatusOut",
        "AttachmentIn": "_alertcenter_78_AttachmentIn",
        "AttachmentOut": "_alertcenter_79_AttachmentOut",
        "RuleInfoIn": "_alertcenter_80_RuleInfoIn",
        "RuleInfoOut": "_alertcenter_81_RuleInfoOut",
        "EmptyIn": "_alertcenter_82_EmptyIn",
        "EmptyOut": "_alertcenter_83_EmptyOut",
        "TransferMisconfigurationIn": "_alertcenter_84_TransferMisconfigurationIn",
        "TransferMisconfigurationOut": "_alertcenter_85_TransferMisconfigurationOut",
        "ListAlertFeedbackResponseIn": "_alertcenter_86_ListAlertFeedbackResponseIn",
        "ListAlertFeedbackResponseOut": "_alertcenter_87_ListAlertFeedbackResponseOut",
        "EntityIn": "_alertcenter_88_EntityIn",
        "EntityOut": "_alertcenter_89_EntityOut",
        "DlpRuleViolationIn": "_alertcenter_90_DlpRuleViolationIn",
        "DlpRuleViolationOut": "_alertcenter_91_DlpRuleViolationOut",
        "SuspiciousActivityIn": "_alertcenter_92_SuspiciousActivityIn",
        "SuspiciousActivityOut": "_alertcenter_93_SuspiciousActivityOut",
        "VoicemailRecipientErrorIn": "_alertcenter_94_VoicemailRecipientErrorIn",
        "VoicemailRecipientErrorOut": "_alertcenter_95_VoicemailRecipientErrorOut",
        "AlertFeedbackIn": "_alertcenter_96_AlertFeedbackIn",
        "AlertFeedbackOut": "_alertcenter_97_AlertFeedbackOut",
        "ActivityRuleIn": "_alertcenter_98_ActivityRuleIn",
        "ActivityRuleOut": "_alertcenter_99_ActivityRuleOut",
        "UndeleteAlertRequestIn": "_alertcenter_100_UndeleteAlertRequestIn",
        "UndeleteAlertRequestOut": "_alertcenter_101_UndeleteAlertRequestOut",
        "TransferErrorIn": "_alertcenter_102_TransferErrorIn",
        "TransferErrorOut": "_alertcenter_103_TransferErrorOut",
        "ActionInfoIn": "_alertcenter_104_ActionInfoIn",
        "ActionInfoOut": "_alertcenter_105_ActionInfoOut",
        "BatchDeleteAlertsRequestIn": "_alertcenter_106_BatchDeleteAlertsRequestIn",
        "BatchDeleteAlertsRequestOut": "_alertcenter_107_BatchDeleteAlertsRequestOut",
        "GmailMessageInfoIn": "_alertcenter_108_GmailMessageInfoIn",
        "GmailMessageInfoOut": "_alertcenter_109_GmailMessageInfoOut",
        "DeviceCompromisedIn": "_alertcenter_110_DeviceCompromisedIn",
        "DeviceCompromisedOut": "_alertcenter_111_DeviceCompromisedOut",
        "BatchUndeleteAlertsRequestIn": "_alertcenter_112_BatchUndeleteAlertsRequestIn",
        "BatchUndeleteAlertsRequestOut": "_alertcenter_113_BatchUndeleteAlertsRequestOut",
        "AppMakerSqlSetupNotificationIn": "_alertcenter_114_AppMakerSqlSetupNotificationIn",
        "AppMakerSqlSetupNotificationOut": "_alertcenter_115_AppMakerSqlSetupNotificationOut",
        "AbuseDetectedIn": "_alertcenter_116_AbuseDetectedIn",
        "AbuseDetectedOut": "_alertcenter_117_AbuseDetectedOut",
        "EntityListIn": "_alertcenter_118_EntityListIn",
        "EntityListOut": "_alertcenter_119_EntityListOut",
        "ApnsCertificateExpirationInfoIn": "_alertcenter_120_ApnsCertificateExpirationInfoIn",
        "ApnsCertificateExpirationInfoOut": "_alertcenter_121_ApnsCertificateExpirationInfoOut",
        "PredefinedDetectorInfoIn": "_alertcenter_122_PredefinedDetectorInfoIn",
        "PredefinedDetectorInfoOut": "_alertcenter_123_PredefinedDetectorInfoOut",
        "PrimaryAdminChangedEventIn": "_alertcenter_124_PrimaryAdminChangedEventIn",
        "PrimaryAdminChangedEventOut": "_alertcenter_125_PrimaryAdminChangedEventOut",
        "GoogleOperationsIn": "_alertcenter_126_GoogleOperationsIn",
        "GoogleOperationsOut": "_alertcenter_127_GoogleOperationsOut",
        "BatchUndeleteAlertsResponseIn": "_alertcenter_128_BatchUndeleteAlertsResponseIn",
        "BatchUndeleteAlertsResponseOut": "_alertcenter_129_BatchUndeleteAlertsResponseOut",
        "MatchInfoIn": "_alertcenter_130_MatchInfoIn",
        "MatchInfoOut": "_alertcenter_131_MatchInfoOut",
        "CsvIn": "_alertcenter_132_CsvIn",
        "CsvOut": "_alertcenter_133_CsvOut",
        "AccountSuspensionWarningIn": "_alertcenter_134_AccountSuspensionWarningIn",
        "AccountSuspensionWarningOut": "_alertcenter_135_AccountSuspensionWarningOut",
        "SensitiveAdminActionIn": "_alertcenter_136_SensitiveAdminActionIn",
        "SensitiveAdminActionOut": "_alertcenter_137_SensitiveAdminActionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SuperAdminPasswordResetEventIn"] = t.struct(
        {"userEmail": t.string().optional()}
    ).named(renames["SuperAdminPasswordResetEventIn"])
    types["SuperAdminPasswordResetEventOut"] = t.struct(
        {
            "userEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuperAdminPasswordResetEventOut"])
    types["AppsOutageIn"] = t.struct(
        {
            "dashboardUri": t.string().optional(),
            "nextUpdateTime": t.string().optional(),
            "products": t.array(t.string()).optional(),
            "resolutionTime": t.string().optional(),
            "mergeInfo": t.proxy(renames["MergeInfoIn"]).optional(),
            "incidentTrackingId": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["AppsOutageIn"])
    types["AppsOutageOut"] = t.struct(
        {
            "dashboardUri": t.string().optional(),
            "nextUpdateTime": t.string().optional(),
            "products": t.array(t.string()).optional(),
            "resolutionTime": t.string().optional(),
            "mergeInfo": t.proxy(renames["MergeInfoOut"]).optional(),
            "incidentTrackingId": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppsOutageOut"])
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
    types["SettingsIn"] = t.struct(
        {"notifications": t.array(t.proxy(renames["NotificationIn"])).optional()}
    ).named(renames["SettingsIn"])
    types["SettingsOut"] = t.struct(
        {
            "notifications": t.array(t.proxy(renames["NotificationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsOut"])
    types["UserChangesIn"] = t.struct({"name": t.string().optional()}).named(
        renames["UserChangesIn"]
    )
    types["UserChangesOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserChangesOut"])
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
    types["StateSponsoredAttackIn"] = t.struct({"email": t.string().optional()}).named(
        renames["StateSponsoredAttackIn"]
    )
    types["StateSponsoredAttackOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StateSponsoredAttackOut"])
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
    types["SuspiciousActivitySecurityDetailIn"] = t.struct(
        {
            "deviceType": t.string().optional(),
            "newValue": t.string().optional(),
            "deviceProperty": t.string().optional(),
            "serialNumber": t.string().optional(),
            "resourceId": t.string().optional(),
            "deviceModel": t.string().optional(),
            "deviceId": t.string(),
            "oldValue": t.string().optional(),
            "iosVendorId": t.string(),
        }
    ).named(renames["SuspiciousActivitySecurityDetailIn"])
    types["SuspiciousActivitySecurityDetailOut"] = t.struct(
        {
            "deviceType": t.string().optional(),
            "newValue": t.string().optional(),
            "deviceProperty": t.string().optional(),
            "serialNumber": t.string().optional(),
            "resourceId": t.string().optional(),
            "deviceModel": t.string().optional(),
            "deviceId": t.string(),
            "oldValue": t.string().optional(),
            "iosVendorId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuspiciousActivitySecurityDetailOut"])
    types["VoiceMisconfigurationIn"] = t.struct(
        {
            "voicemailMisconfiguration": t.proxy(
                renames["VoicemailMisconfigurationIn"]
            ).optional(),
            "transferMisconfiguration": t.proxy(
                renames["TransferMisconfigurationIn"]
            ).optional(),
            "entityName": t.string().optional(),
            "entityType": t.string().optional(),
            "fixUri": t.string().optional(),
            "membersMisconfiguration": t.proxy(
                renames["TransferMisconfigurationIn"]
            ).optional(),
        }
    ).named(renames["VoiceMisconfigurationIn"])
    types["VoiceMisconfigurationOut"] = t.struct(
        {
            "voicemailMisconfiguration": t.proxy(
                renames["VoicemailMisconfigurationOut"]
            ).optional(),
            "transferMisconfiguration": t.proxy(
                renames["TransferMisconfigurationOut"]
            ).optional(),
            "entityName": t.string().optional(),
            "entityType": t.string().optional(),
            "fixUri": t.string().optional(),
            "membersMisconfiguration": t.proxy(
                renames["TransferMisconfigurationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceMisconfigurationOut"])
    types["SSOProfileCreatedEventIn"] = t.struct(
        {"inboundSsoProfileName": t.string().optional()}
    ).named(renames["SSOProfileCreatedEventIn"])
    types["SSOProfileCreatedEventOut"] = t.struct(
        {
            "inboundSsoProfileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SSOProfileCreatedEventOut"])
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
    types["MailPhishingIn"] = t.struct(
        {
            "messages": t.array(t.proxy(renames["GmailMessageInfoIn"])).optional(),
            "isInternal": t.boolean().optional(),
            "domainId": t.proxy(renames["DomainIdIn"]).optional(),
            "systemActionType": t.string().optional(),
            "maliciousEntity": t.proxy(renames["MaliciousEntityIn"]).optional(),
        }
    ).named(renames["MailPhishingIn"])
    types["MailPhishingOut"] = t.struct(
        {
            "messages": t.array(t.proxy(renames["GmailMessageInfoOut"])).optional(),
            "isInternal": t.boolean().optional(),
            "domainId": t.proxy(renames["DomainIdOut"]).optional(),
            "systemActionType": t.string().optional(),
            "maliciousEntity": t.proxy(renames["MaliciousEntityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MailPhishingOut"])
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
    types["SSOProfileDeletedEventIn"] = t.struct(
        {"inboundSsoProfileName": t.string().optional()}
    ).named(renames["SSOProfileDeletedEventIn"])
    types["SSOProfileDeletedEventOut"] = t.struct(
        {
            "inboundSsoProfileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SSOProfileDeletedEventOut"])
    types["NotificationIn"] = t.struct(
        {"cloudPubsubTopic": t.proxy(renames["CloudPubsubTopicIn"]).optional()}
    ).named(renames["NotificationIn"])
    types["NotificationOut"] = t.struct(
        {
            "cloudPubsubTopic": t.proxy(renames["CloudPubsubTopicOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationOut"])
    types["DeviceCompromisedSecurityDetailIn"] = t.struct(
        {
            "deviceId": t.string(),
            "serialNumber": t.string().optional(),
            "deviceCompromisedState": t.string().optional(),
            "deviceType": t.string().optional(),
            "deviceModel": t.string().optional(),
            "resourceId": t.string().optional(),
            "iosVendorId": t.string(),
        }
    ).named(renames["DeviceCompromisedSecurityDetailIn"])
    types["DeviceCompromisedSecurityDetailOut"] = t.struct(
        {
            "deviceId": t.string(),
            "serialNumber": t.string().optional(),
            "deviceCompromisedState": t.string().optional(),
            "deviceType": t.string().optional(),
            "deviceModel": t.string().optional(),
            "resourceId": t.string().optional(),
            "iosVendorId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceCompromisedSecurityDetailOut"])
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
    types["BadWhitelistIn"] = t.struct(
        {
            "domainId": t.proxy(renames["DomainIdIn"]).optional(),
            "messages": t.array(t.proxy(renames["GmailMessageInfoIn"])).optional(),
            "maliciousEntity": t.proxy(renames["MaliciousEntityIn"]).optional(),
            "sourceIp": t.string().optional(),
        }
    ).named(renames["BadWhitelistIn"])
    types["BadWhitelistOut"] = t.struct(
        {
            "domainId": t.proxy(renames["DomainIdOut"]).optional(),
            "messages": t.array(t.proxy(renames["GmailMessageInfoOut"])).optional(),
            "maliciousEntity": t.proxy(renames["MaliciousEntityOut"]).optional(),
            "sourceIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BadWhitelistOut"])
    types["PhishingSpikeIn"] = t.struct(
        {
            "maliciousEntity": t.proxy(renames["MaliciousEntityIn"]).optional(),
            "domainId": t.proxy(renames["DomainIdIn"]).optional(),
            "messages": t.array(t.proxy(renames["GmailMessageInfoIn"])).optional(),
            "isInternal": t.boolean().optional(),
        }
    ).named(renames["PhishingSpikeIn"])
    types["PhishingSpikeOut"] = t.struct(
        {
            "maliciousEntity": t.proxy(renames["MaliciousEntityOut"]).optional(),
            "domainId": t.proxy(renames["DomainIdOut"]).optional(),
            "messages": t.array(t.proxy(renames["GmailMessageInfoOut"])).optional(),
            "isInternal": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhishingSpikeOut"])
    types["AlertIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "customerId": t.string().optional(),
            "metadata": t.proxy(renames["AlertMetadataIn"]).optional(),
            "updateTime": t.string().optional(),
            "source": t.string(),
            "startTime": t.string(),
            "alertId": t.string().optional(),
            "type": t.string(),
            "etag": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "securityInvestigationToolLink": t.string().optional(),
            "createTime": t.string().optional(),
            "deleted": t.boolean().optional(),
        }
    ).named(renames["AlertIn"])
    types["AlertOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "customerId": t.string().optional(),
            "metadata": t.proxy(renames["AlertMetadataOut"]).optional(),
            "updateTime": t.string().optional(),
            "source": t.string(),
            "startTime": t.string(),
            "alertId": t.string().optional(),
            "type": t.string(),
            "etag": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "securityInvestigationToolLink": t.string().optional(),
            "createTime": t.string().optional(),
            "deleted": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertOut"])
    types["RuleViolationInfoIn"] = t.struct(
        {
            "triggeringUserEmail": t.string().optional(),
            "triggeredActionTypes": t.array(t.string()).optional(),
            "triggeredActionInfo": t.array(t.proxy(renames["ActionInfoIn"])).optional(),
            "dataSource": t.string().optional(),
            "trigger": t.string().optional(),
            "ruleInfo": t.proxy(renames["RuleInfoIn"]).optional(),
            "resourceInfo": t.proxy(renames["ResourceInfoIn"]).optional(),
            "suppressedActionTypes": t.array(t.string()).optional(),
            "matchInfo": t.array(t.proxy(renames["MatchInfoIn"])).optional(),
            "recipients": t.array(t.string()).optional(),
        }
    ).named(renames["RuleViolationInfoIn"])
    types["RuleViolationInfoOut"] = t.struct(
        {
            "triggeringUserEmail": t.string().optional(),
            "triggeredActionTypes": t.array(t.string()).optional(),
            "triggeredActionInfo": t.array(
                t.proxy(renames["ActionInfoOut"])
            ).optional(),
            "dataSource": t.string().optional(),
            "trigger": t.string().optional(),
            "ruleInfo": t.proxy(renames["RuleInfoOut"]).optional(),
            "resourceInfo": t.proxy(renames["ResourceInfoOut"]).optional(),
            "suppressedActionTypes": t.array(t.string()).optional(),
            "matchInfo": t.array(t.proxy(renames["MatchInfoOut"])).optional(),
            "recipients": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleViolationInfoOut"])
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
    types["AlertMetadataIn"] = t.struct(
        {
            "alertId": t.string().optional(),
            "assignee": t.string().optional(),
            "etag": t.string().optional(),
            "status": t.string().optional(),
            "updateTime": t.string().optional(),
            "severity": t.string().optional(),
            "customerId": t.string().optional(),
        }
    ).named(renames["AlertMetadataIn"])
    types["AlertMetadataOut"] = t.struct(
        {
            "alertId": t.string().optional(),
            "assignee": t.string().optional(),
            "etag": t.string().optional(),
            "status": t.string().optional(),
            "updateTime": t.string().optional(),
            "severity": t.string().optional(),
            "customerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertMetadataOut"])
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
    types["CsvRowIn"] = t.struct({"entries": t.array(t.string()).optional()}).named(
        renames["CsvRowIn"]
    )
    types["CsvRowOut"] = t.struct(
        {
            "entries": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CsvRowOut"])
    types["DomainIdIn"] = t.struct(
        {"customerPrimaryDomain": t.string().optional()}
    ).named(renames["DomainIdIn"])
    types["DomainIdOut"] = t.struct(
        {
            "customerPrimaryDomain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainIdOut"])
    types["DomainWideTakeoutInitiatedIn"] = t.struct(
        {"email": t.string().optional(), "takeoutRequestId": t.string().optional()}
    ).named(renames["DomainWideTakeoutInitiatedIn"])
    types["DomainWideTakeoutInitiatedOut"] = t.struct(
        {
            "email": t.string().optional(),
            "takeoutRequestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainWideTakeoutInitiatedOut"])
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
    types["AttachmentIn"] = t.struct(
        {"csv": t.proxy(renames["CsvIn"]).optional()}
    ).named(renames["AttachmentIn"])
    types["AttachmentOut"] = t.struct(
        {
            "csv": t.proxy(renames["CsvOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TransferMisconfigurationIn"] = t.struct(
        {"errors": t.array(t.proxy(renames["TransferErrorIn"])).optional()}
    ).named(renames["TransferMisconfigurationIn"])
    types["TransferMisconfigurationOut"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["TransferErrorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferMisconfigurationOut"])
    types["ListAlertFeedbackResponseIn"] = t.struct(
        {"feedback": t.array(t.proxy(renames["AlertFeedbackIn"])).optional()}
    ).named(renames["ListAlertFeedbackResponseIn"])
    types["ListAlertFeedbackResponseOut"] = t.struct(
        {
            "feedback": t.array(t.proxy(renames["AlertFeedbackOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAlertFeedbackResponseOut"])
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
    types["DlpRuleViolationIn"] = t.struct(
        {"ruleViolationInfo": t.proxy(renames["RuleViolationInfoIn"]).optional()}
    ).named(renames["DlpRuleViolationIn"])
    types["DlpRuleViolationOut"] = t.struct(
        {
            "ruleViolationInfo": t.proxy(renames["RuleViolationInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DlpRuleViolationOut"])
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
    types["AlertFeedbackIn"] = t.struct(
        {
            "alertId": t.string().optional(),
            "type": t.string(),
            "email": t.string().optional(),
            "createTime": t.string().optional(),
            "feedbackId": t.string().optional(),
            "customerId": t.string().optional(),
        }
    ).named(renames["AlertFeedbackIn"])
    types["AlertFeedbackOut"] = t.struct(
        {
            "alertId": t.string().optional(),
            "type": t.string(),
            "email": t.string().optional(),
            "createTime": t.string().optional(),
            "feedbackId": t.string().optional(),
            "customerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertFeedbackOut"])
    types["ActivityRuleIn"] = t.struct(
        {
            "triggerSource": t.string().optional(),
            "displayName": t.string().optional(),
            "supersedingAlert": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "query": t.string().optional(),
            "actionNames": t.array(t.string()).optional(),
            "threshold": t.string().optional(),
            "name": t.string().optional(),
            "windowSize": t.string().optional(),
            "supersededAlerts": t.array(t.string()).optional(),
        }
    ).named(renames["ActivityRuleIn"])
    types["ActivityRuleOut"] = t.struct(
        {
            "triggerSource": t.string().optional(),
            "displayName": t.string().optional(),
            "supersedingAlert": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "query": t.string().optional(),
            "actionNames": t.array(t.string()).optional(),
            "threshold": t.string().optional(),
            "name": t.string().optional(),
            "windowSize": t.string().optional(),
            "supersededAlerts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityRuleOut"])
    types["UndeleteAlertRequestIn"] = t.struct(
        {"customerId": t.string().optional()}
    ).named(renames["UndeleteAlertRequestIn"])
    types["UndeleteAlertRequestOut"] = t.struct(
        {
            "customerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UndeleteAlertRequestOut"])
    types["TransferErrorIn"] = t.struct(
        {
            "id": t.string().optional(),
            "entityType": t.string().optional(),
            "invalidReason": t.string().optional(),
            "email": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TransferErrorIn"])
    types["TransferErrorOut"] = t.struct(
        {
            "id": t.string().optional(),
            "entityType": t.string().optional(),
            "invalidReason": t.string().optional(),
            "email": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferErrorOut"])
    types["ActionInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ActionInfoIn"]
    )
    types["ActionInfoOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActionInfoOut"])
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
    types["GmailMessageInfoIn"] = t.struct(
        {
            "subjectText": t.string().optional(),
            "messageId": t.string().optional(),
            "date": t.string().optional(),
            "messageBodySnippet": t.string().optional(),
            "md5HashSubject": t.string().optional(),
            "md5HashMessageBody": t.string().optional(),
            "recipient": t.string().optional(),
            "sentTime": t.string().optional(),
            "attachmentsSha256Hash": t.array(t.string()).optional(),
        }
    ).named(renames["GmailMessageInfoIn"])
    types["GmailMessageInfoOut"] = t.struct(
        {
            "subjectText": t.string().optional(),
            "messageId": t.string().optional(),
            "date": t.string().optional(),
            "messageBodySnippet": t.string().optional(),
            "md5HashSubject": t.string().optional(),
            "md5HashMessageBody": t.string().optional(),
            "recipient": t.string().optional(),
            "sentTime": t.string().optional(),
            "attachmentsSha256Hash": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GmailMessageInfoOut"])
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
    types["AppMakerSqlSetupNotificationIn"] = t.struct(
        {"requestInfo": t.array(t.proxy(renames["RequestInfoIn"])).optional()}
    ).named(renames["AppMakerSqlSetupNotificationIn"])
    types["AppMakerSqlSetupNotificationOut"] = t.struct(
        {
            "requestInfo": t.array(t.proxy(renames["RequestInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppMakerSqlSetupNotificationOut"])
    types["AbuseDetectedIn"] = t.struct(
        {
            "variationType": t.string().optional(),
            "additionalDetails": t.proxy(renames["EntityListIn"]).optional(),
            "product": t.string().optional(),
            "subAlertId": t.string().optional(),
        }
    ).named(renames["AbuseDetectedIn"])
    types["AbuseDetectedOut"] = t.struct(
        {
            "variationType": t.string().optional(),
            "additionalDetails": t.proxy(renames["EntityListOut"]).optional(),
            "product": t.string().optional(),
            "subAlertId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AbuseDetectedOut"])
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
    types["ApnsCertificateExpirationInfoIn"] = t.struct(
        {
            "appleId": t.string().optional(),
            "expirationTime": t.string().optional(),
            "uid": t.string().optional(),
        }
    ).named(renames["ApnsCertificateExpirationInfoIn"])
    types["ApnsCertificateExpirationInfoOut"] = t.struct(
        {
            "appleId": t.string().optional(),
            "expirationTime": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApnsCertificateExpirationInfoOut"])
    types["PredefinedDetectorInfoIn"] = t.struct(
        {"detectorName": t.string().optional()}
    ).named(renames["PredefinedDetectorInfoIn"])
    types["PredefinedDetectorInfoOut"] = t.struct(
        {
            "detectorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PredefinedDetectorInfoOut"])
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
    types["GoogleOperationsIn"] = t.struct(
        {
            "affectedUserEmails": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "attachmentData": t.proxy(renames["AttachmentIn"]).optional(),
            "domain": t.string().optional(),
            "description": t.string().optional(),
            "header": t.string().optional(),
        }
    ).named(renames["GoogleOperationsIn"])
    types["GoogleOperationsOut"] = t.struct(
        {
            "affectedUserEmails": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "attachmentData": t.proxy(renames["AttachmentOut"]).optional(),
            "domain": t.string().optional(),
            "description": t.string().optional(),
            "header": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleOperationsOut"])
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
    types["SensitiveAdminActionIn"] = t.struct(
        {
            "ssoProfileDeletedEvent": t.proxy(
                renames["SSOProfileDeletedEventIn"]
            ).optional(),
            "primaryAdminChangedEvent": t.proxy(
                renames["PrimaryAdminChangedEventIn"]
            ).optional(),
            "ssoProfileUpdatedEvent": t.proxy(
                renames["SSOProfileUpdatedEventIn"]
            ).optional(),
            "eventTime": t.string().optional(),
            "ssoProfileCreatedEvent": t.proxy(
                renames["SSOProfileCreatedEventIn"]
            ).optional(),
            "actorEmail": t.string().optional(),
            "superAdminPasswordResetEvent": t.proxy(
                renames["SuperAdminPasswordResetEventIn"]
            ).optional(),
        }
    ).named(renames["SensitiveAdminActionIn"])
    types["SensitiveAdminActionOut"] = t.struct(
        {
            "ssoProfileDeletedEvent": t.proxy(
                renames["SSOProfileDeletedEventOut"]
            ).optional(),
            "primaryAdminChangedEvent": t.proxy(
                renames["PrimaryAdminChangedEventOut"]
            ).optional(),
            "ssoProfileUpdatedEvent": t.proxy(
                renames["SSOProfileUpdatedEventOut"]
            ).optional(),
            "eventTime": t.string().optional(),
            "ssoProfileCreatedEvent": t.proxy(
                renames["SSOProfileCreatedEventOut"]
            ).optional(),
            "actorEmail": t.string().optional(),
            "superAdminPasswordResetEvent": t.proxy(
                renames["SuperAdminPasswordResetEventOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SensitiveAdminActionOut"])

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
