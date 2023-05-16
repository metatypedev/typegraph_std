from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_analytics() -> Import:
    analytics = HTTPRuntime("https://analytics.googleapis.com/")

    renames = {
        "ErrorResponse": "_analytics_1_ErrorResponse",
        "UserDeletionRequestIn": "_analytics_2_UserDeletionRequestIn",
        "UserDeletionRequestOut": "_analytics_3_UserDeletionRequestOut",
        "WebPropertyRefIn": "_analytics_4_WebPropertyRefIn",
        "WebPropertyRefOut": "_analytics_5_WebPropertyRefOut",
        "EntityUserLinkIn": "_analytics_6_EntityUserLinkIn",
        "EntityUserLinkOut": "_analytics_7_EntityUserLinkOut",
        "ProfileFilterLinkIn": "_analytics_8_ProfileFilterLinkIn",
        "ProfileFilterLinkOut": "_analytics_9_ProfileFilterLinkOut",
        "AccountTreeRequestIn": "_analytics_10_AccountTreeRequestIn",
        "AccountTreeRequestOut": "_analytics_11_AccountTreeRequestOut",
        "EntityUserLinksIn": "_analytics_12_EntityUserLinksIn",
        "EntityUserLinksOut": "_analytics_13_EntityUserLinksOut",
        "AnalyticsDataimportDeleteUploadDataRequestIn": "_analytics_14_AnalyticsDataimportDeleteUploadDataRequestIn",
        "AnalyticsDataimportDeleteUploadDataRequestOut": "_analytics_15_AnalyticsDataimportDeleteUploadDataRequestOut",
        "AccountSummaryIn": "_analytics_16_AccountSummaryIn",
        "AccountSummaryOut": "_analytics_17_AccountSummaryOut",
        "GoalsIn": "_analytics_18_GoalsIn",
        "GoalsOut": "_analytics_19_GoalsOut",
        "IncludeConditionsIn": "_analytics_20_IncludeConditionsIn",
        "IncludeConditionsOut": "_analytics_21_IncludeConditionsOut",
        "ExperimentsIn": "_analytics_22_ExperimentsIn",
        "ExperimentsOut": "_analytics_23_ExperimentsOut",
        "EntityAdWordsLinksIn": "_analytics_24_EntityAdWordsLinksIn",
        "EntityAdWordsLinksOut": "_analytics_25_EntityAdWordsLinksOut",
        "FilterRefIn": "_analytics_26_FilterRefIn",
        "FilterRefOut": "_analytics_27_FilterRefOut",
        "WebPropertySummaryIn": "_analytics_28_WebPropertySummaryIn",
        "WebPropertySummaryOut": "_analytics_29_WebPropertySummaryOut",
        "AccountIn": "_analytics_30_AccountIn",
        "AccountOut": "_analytics_31_AccountOut",
        "UnsampledReportsIn": "_analytics_32_UnsampledReportsIn",
        "UnsampledReportsOut": "_analytics_33_UnsampledReportsOut",
        "RemarketingAudienceIn": "_analytics_34_RemarketingAudienceIn",
        "RemarketingAudienceOut": "_analytics_35_RemarketingAudienceOut",
        "WebpropertyIn": "_analytics_36_WebpropertyIn",
        "WebpropertyOut": "_analytics_37_WebpropertyOut",
        "AccountTicketIn": "_analytics_38_AccountTicketIn",
        "AccountTicketOut": "_analytics_39_AccountTicketOut",
        "HashClientIdResponseIn": "_analytics_40_HashClientIdResponseIn",
        "HashClientIdResponseOut": "_analytics_41_HashClientIdResponseOut",
        "UserRefIn": "_analytics_42_UserRefIn",
        "UserRefOut": "_analytics_43_UserRefOut",
        "FiltersIn": "_analytics_44_FiltersIn",
        "FiltersOut": "_analytics_45_FiltersOut",
        "ProfileSummaryIn": "_analytics_46_ProfileSummaryIn",
        "ProfileSummaryOut": "_analytics_47_ProfileSummaryOut",
        "AccountSummariesIn": "_analytics_48_AccountSummariesIn",
        "AccountSummariesOut": "_analytics_49_AccountSummariesOut",
        "CustomDataSourcesIn": "_analytics_50_CustomDataSourcesIn",
        "CustomDataSourcesOut": "_analytics_51_CustomDataSourcesOut",
        "FilterIn": "_analytics_52_FilterIn",
        "FilterOut": "_analytics_53_FilterOut",
        "CustomDataSourceIn": "_analytics_54_CustomDataSourceIn",
        "CustomDataSourceOut": "_analytics_55_CustomDataSourceOut",
        "FilterExpressionIn": "_analytics_56_FilterExpressionIn",
        "FilterExpressionOut": "_analytics_57_FilterExpressionOut",
        "AccountRefIn": "_analytics_58_AccountRefIn",
        "AccountRefOut": "_analytics_59_AccountRefOut",
        "CustomDimensionIn": "_analytics_60_CustomDimensionIn",
        "CustomDimensionOut": "_analytics_61_CustomDimensionOut",
        "RealtimeDataIn": "_analytics_62_RealtimeDataIn",
        "RealtimeDataOut": "_analytics_63_RealtimeDataOut",
        "CustomMetricIn": "_analytics_64_CustomMetricIn",
        "CustomMetricOut": "_analytics_65_CustomMetricOut",
        "CustomDimensionsIn": "_analytics_66_CustomDimensionsIn",
        "CustomDimensionsOut": "_analytics_67_CustomDimensionsOut",
        "ProfilesIn": "_analytics_68_ProfilesIn",
        "ProfilesOut": "_analytics_69_ProfilesOut",
        "SegmentsIn": "_analytics_70_SegmentsIn",
        "SegmentsOut": "_analytics_71_SegmentsOut",
        "SegmentIn": "_analytics_72_SegmentIn",
        "SegmentOut": "_analytics_73_SegmentOut",
        "GaDataIn": "_analytics_74_GaDataIn",
        "GaDataOut": "_analytics_75_GaDataOut",
        "AccountsIn": "_analytics_76_AccountsIn",
        "AccountsOut": "_analytics_77_AccountsOut",
        "ProfileIn": "_analytics_78_ProfileIn",
        "ProfileOut": "_analytics_79_ProfileOut",
        "ColumnsIn": "_analytics_80_ColumnsIn",
        "ColumnsOut": "_analytics_81_ColumnsOut",
        "ColumnIn": "_analytics_82_ColumnIn",
        "ColumnOut": "_analytics_83_ColumnOut",
        "HashClientIdRequestIn": "_analytics_84_HashClientIdRequestIn",
        "HashClientIdRequestOut": "_analytics_85_HashClientIdRequestOut",
        "AccountTreeResponseIn": "_analytics_86_AccountTreeResponseIn",
        "AccountTreeResponseOut": "_analytics_87_AccountTreeResponseOut",
        "GoalIn": "_analytics_88_GoalIn",
        "GoalOut": "_analytics_89_GoalOut",
        "AdWordsAccountIn": "_analytics_90_AdWordsAccountIn",
        "AdWordsAccountOut": "_analytics_91_AdWordsAccountOut",
        "UnsampledReportIn": "_analytics_92_UnsampledReportIn",
        "UnsampledReportOut": "_analytics_93_UnsampledReportOut",
        "UploadsIn": "_analytics_94_UploadsIn",
        "UploadsOut": "_analytics_95_UploadsOut",
        "UploadIn": "_analytics_96_UploadIn",
        "UploadOut": "_analytics_97_UploadOut",
        "RemarketingAudiencesIn": "_analytics_98_RemarketingAudiencesIn",
        "RemarketingAudiencesOut": "_analytics_99_RemarketingAudiencesOut",
        "EntityAdWordsLinkIn": "_analytics_100_EntityAdWordsLinkIn",
        "EntityAdWordsLinkOut": "_analytics_101_EntityAdWordsLinkOut",
        "WebpropertiesIn": "_analytics_102_WebpropertiesIn",
        "WebpropertiesOut": "_analytics_103_WebpropertiesOut",
        "ProfileFilterLinksIn": "_analytics_104_ProfileFilterLinksIn",
        "ProfileFilterLinksOut": "_analytics_105_ProfileFilterLinksOut",
        "McfDataIn": "_analytics_106_McfDataIn",
        "McfDataOut": "_analytics_107_McfDataOut",
        "ExperimentIn": "_analytics_108_ExperimentIn",
        "ExperimentOut": "_analytics_109_ExperimentOut",
        "CustomMetricsIn": "_analytics_110_CustomMetricsIn",
        "CustomMetricsOut": "_analytics_111_CustomMetricsOut",
        "LinkedForeignAccountIn": "_analytics_112_LinkedForeignAccountIn",
        "LinkedForeignAccountOut": "_analytics_113_LinkedForeignAccountOut",
        "ProfileRefIn": "_analytics_114_ProfileRefIn",
        "ProfileRefOut": "_analytics_115_ProfileRefOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["UserDeletionRequestIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.struct(
                {"userId": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "propertyId": t.string().optional(),
            "firebaseProjectId": t.string().optional(),
            "webPropertyId": t.string().optional(),
        }
    ).named(renames["UserDeletionRequestIn"])
    types["UserDeletionRequestOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.struct(
                {"userId": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "propertyId": t.string().optional(),
            "firebaseProjectId": t.string().optional(),
            "deletionRequestTime": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserDeletionRequestOut"])
    types["WebPropertyRefIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "href": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["WebPropertyRefIn"])
    types["WebPropertyRefOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "href": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebPropertyRefOut"])
    types["EntityUserLinkIn"] = t.struct(
        {
            "permissions": t.struct(
                {"local": t.array(t.string()).optional()}
            ).optional(),
            "selfLink": t.string().optional(),
            "entity": t.struct(
                {
                    "webPropertyRef": t.proxy(renames["WebPropertyRefIn"]).optional(),
                    "accountRef": t.proxy(renames["AccountRefIn"]).optional(),
                    "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "userRef": t.proxy(renames["UserRefIn"]).optional(),
        }
    ).named(renames["EntityUserLinkIn"])
    types["EntityUserLinkOut"] = t.struct(
        {
            "permissions": t.struct(
                {
                    "effective": t.array(t.string()).optional(),
                    "local": t.array(t.string()).optional(),
                }
            ).optional(),
            "selfLink": t.string().optional(),
            "entity": t.struct(
                {
                    "webPropertyRef": t.proxy(renames["WebPropertyRefOut"]).optional(),
                    "accountRef": t.proxy(renames["AccountRefOut"]).optional(),
                    "profileRef": t.proxy(renames["ProfileRefOut"]).optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "userRef": t.proxy(renames["UserRefOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityUserLinkOut"])
    types["ProfileFilterLinkIn"] = t.struct(
        {
            "rank": t.integer().optional(),
            "id": t.string().optional(),
            "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
            "filterRef": t.proxy(renames["FilterRefIn"]).optional(),
        }
    ).named(renames["ProfileFilterLinkIn"])
    types["ProfileFilterLinkOut"] = t.struct(
        {
            "rank": t.integer().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "profileRef": t.proxy(renames["ProfileRefOut"]).optional(),
            "selfLink": t.string().optional(),
            "filterRef": t.proxy(renames["FilterRefOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileFilterLinkOut"])
    types["AccountTreeRequestIn"] = t.struct(
        {
            "webpropertyName": t.string(),
            "profileName": t.string(),
            "accountName": t.string(),
            "websiteUrl": t.string(),
            "timezone": t.string(),
            "kind": t.string().optional(),
        }
    ).named(renames["AccountTreeRequestIn"])
    types["AccountTreeRequestOut"] = t.struct(
        {
            "webpropertyName": t.string(),
            "profileName": t.string(),
            "accountName": t.string(),
            "websiteUrl": t.string(),
            "timezone": t.string(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountTreeRequestOut"])
    types["EntityUserLinksIn"] = t.struct(
        {
            "previousLink": t.string().optional(),
            "items": t.array(t.proxy(renames["EntityUserLinkIn"])).optional(),
            "totalResults": t.integer().optional(),
            "kind": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "nextLink": t.string().optional(),
            "startIndex": t.integer().optional(),
        }
    ).named(renames["EntityUserLinksIn"])
    types["EntityUserLinksOut"] = t.struct(
        {
            "previousLink": t.string().optional(),
            "items": t.array(t.proxy(renames["EntityUserLinkOut"])).optional(),
            "totalResults": t.integer().optional(),
            "kind": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "nextLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityUserLinksOut"])
    types["AnalyticsDataimportDeleteUploadDataRequestIn"] = t.struct(
        {"customDataImportUids": t.array(t.string()).optional()}
    ).named(renames["AnalyticsDataimportDeleteUploadDataRequestIn"])
    types["AnalyticsDataimportDeleteUploadDataRequestOut"] = t.struct(
        {
            "customDataImportUids": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyticsDataimportDeleteUploadDataRequestOut"])
    types["AccountSummaryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "starred": t.boolean().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "webProperties": t.array(
                t.proxy(renames["WebPropertySummaryIn"])
            ).optional(),
        }
    ).named(renames["AccountSummaryIn"])
    types["AccountSummaryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "starred": t.boolean().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "webProperties": t.array(
                t.proxy(renames["WebPropertySummaryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountSummaryOut"])
    types["GoalsIn"] = t.struct(
        {
            "username": t.string().optional(),
            "kind": t.string().optional(),
            "startIndex": t.integer().optional(),
            "itemsPerPage": t.integer().optional(),
            "previousLink": t.string().optional(),
            "nextLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "items": t.array(t.proxy(renames["GoalIn"])).optional(),
        }
    ).named(renames["GoalsIn"])
    types["GoalsOut"] = t.struct(
        {
            "username": t.string().optional(),
            "kind": t.string().optional(),
            "startIndex": t.integer().optional(),
            "itemsPerPage": t.integer().optional(),
            "previousLink": t.string().optional(),
            "nextLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "items": t.array(t.proxy(renames["GoalOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoalsOut"])
    types["IncludeConditionsIn"] = t.struct(
        {
            "segment": t.string().optional(),
            "isSmartList": t.boolean().optional(),
            "membershipDurationDays": t.integer().optional(),
            "kind": t.string().optional(),
            "daysToLookBack": t.integer().optional(),
        }
    ).named(renames["IncludeConditionsIn"])
    types["IncludeConditionsOut"] = t.struct(
        {
            "segment": t.string().optional(),
            "isSmartList": t.boolean().optional(),
            "membershipDurationDays": t.integer().optional(),
            "kind": t.string().optional(),
            "daysToLookBack": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IncludeConditionsOut"])
    types["ExperimentsIn"] = t.struct(
        {
            "totalResults": t.integer().optional(),
            "nextLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "items": t.array(t.proxy(renames["ExperimentIn"])).optional(),
            "previousLink": t.string().optional(),
            "username": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ExperimentsIn"])
    types["ExperimentsOut"] = t.struct(
        {
            "totalResults": t.integer().optional(),
            "nextLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "items": t.array(t.proxy(renames["ExperimentOut"])).optional(),
            "previousLink": t.string().optional(),
            "username": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExperimentsOut"])
    types["EntityAdWordsLinksIn"] = t.struct(
        {
            "totalResults": t.integer().optional(),
            "previousLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "kind": t.string().optional(),
            "nextLink": t.string().optional(),
            "items": t.array(t.proxy(renames["EntityAdWordsLinkIn"])).optional(),
            "itemsPerPage": t.integer().optional(),
        }
    ).named(renames["EntityAdWordsLinksIn"])
    types["EntityAdWordsLinksOut"] = t.struct(
        {
            "totalResults": t.integer().optional(),
            "previousLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "kind": t.string().optional(),
            "nextLink": t.string().optional(),
            "items": t.array(t.proxy(renames["EntityAdWordsLinkOut"])).optional(),
            "itemsPerPage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityAdWordsLinksOut"])
    types["FilterRefIn"] = t.struct(
        {
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "href": t.string().optional(),
        }
    ).named(renames["FilterRefIn"])
    types["FilterRefOut"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "accountId": t.string().optional(),
            "href": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterRefOut"])
    types["WebPropertySummaryIn"] = t.struct(
        {
            "starred": t.boolean().optional(),
            "kind": t.string().optional(),
            "level": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "name": t.string().optional(),
            "profiles": t.array(t.proxy(renames["ProfileSummaryIn"])).optional(),
            "internalWebPropertyId": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["WebPropertySummaryIn"])
    types["WebPropertySummaryOut"] = t.struct(
        {
            "starred": t.boolean().optional(),
            "kind": t.string().optional(),
            "level": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "name": t.string().optional(),
            "profiles": t.array(t.proxy(renames["ProfileSummaryOut"])).optional(),
            "internalWebPropertyId": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebPropertySummaryOut"])
    types["AccountIn"] = t.struct(
        {
            "created": t.string().optional(),
            "id": t.string().optional(),
            "childLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "permissions": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "updated": t.string().optional(),
            "starred": t.boolean().optional(),
            "name": t.string().optional(),
            "selfLink": t.string().optional(),
        }
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "created": t.string().optional(),
            "id": t.string().optional(),
            "childLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "permissions": t.struct(
                {"effective": t.array(t.string()).optional()}
            ).optional(),
            "kind": t.string().optional(),
            "updated": t.string().optional(),
            "starred": t.boolean().optional(),
            "name": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
    types["UnsampledReportsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "username": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "totalResults": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "nextLink": t.string().optional(),
            "previousLink": t.string().optional(),
            "items": t.array(t.proxy(renames["UnsampledReportIn"])).optional(),
        }
    ).named(renames["UnsampledReportsIn"])
    types["UnsampledReportsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "username": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "totalResults": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "nextLink": t.string().optional(),
            "previousLink": t.string().optional(),
            "items": t.array(t.proxy(renames["UnsampledReportOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnsampledReportsOut"])
    types["RemarketingAudienceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "linkedViews": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "linkedAdAccounts": t.array(
                t.proxy(renames["LinkedForeignAccountIn"])
            ).optional(),
            "webPropertyId": t.string().optional(),
            "audienceType": t.string().optional(),
            "kind": t.string().optional(),
            "audienceDefinition": t.struct(
                {
                    "includeConditions": t.proxy(
                        renames["IncludeConditionsIn"]
                    ).optional()
                }
            ).optional(),
            "stateBasedAudienceDefinition": t.struct(
                {
                    "includeConditions": t.proxy(
                        renames["IncludeConditionsIn"]
                    ).optional(),
                    "excludeConditions": t.struct(
                        {
                            "exclusionDuration": t.string().optional(),
                            "segment": t.string().optional(),
                        }
                    ).optional(),
                }
            ).optional(),
        }
    ).named(renames["RemarketingAudienceIn"])
    types["RemarketingAudienceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "linkedViews": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "linkedAdAccounts": t.array(
                t.proxy(renames["LinkedForeignAccountOut"])
            ).optional(),
            "webPropertyId": t.string().optional(),
            "audienceType": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
            "updated": t.string().optional(),
            "created": t.string().optional(),
            "kind": t.string().optional(),
            "description": t.string().optional(),
            "audienceDefinition": t.struct(
                {
                    "includeConditions": t.proxy(
                        renames["IncludeConditionsOut"]
                    ).optional()
                }
            ).optional(),
            "stateBasedAudienceDefinition": t.struct(
                {
                    "includeConditions": t.proxy(
                        renames["IncludeConditionsOut"]
                    ).optional(),
                    "excludeConditions": t.struct(
                        {
                            "exclusionDuration": t.string().optional(),
                            "segment": t.string().optional(),
                        }
                    ).optional(),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemarketingAudienceOut"])
    types["WebpropertyIn"] = t.struct(
        {
            "dataRetentionResetOnNewActivity": t.boolean().optional(),
            "dataRetentionTtl": t.string().optional(),
            "name": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "childLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "starred": t.boolean().optional(),
            "industryVertical": t.string().optional(),
            "id": t.string().optional(),
            "defaultProfileId": t.string().optional(),
            "parentLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "permissions": t.struct({"_": t.string().optional()}).optional(),
            "accountId": t.string().optional(),
        }
    ).named(renames["WebpropertyIn"])
    types["WebpropertyOut"] = t.struct(
        {
            "dataRetentionResetOnNewActivity": t.boolean().optional(),
            "profileCount": t.integer().optional(),
            "dataRetentionTtl": t.string().optional(),
            "name": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "level": t.string().optional(),
            "childLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "starred": t.boolean().optional(),
            "created": t.string().optional(),
            "industryVertical": t.string().optional(),
            "id": t.string().optional(),
            "defaultProfileId": t.string().optional(),
            "parentLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "kind": t.string().optional(),
            "permissions": t.struct(
                {"effective": t.array(t.string()).optional()}
            ).optional(),
            "updated": t.string().optional(),
            "accountId": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebpropertyOut"])
    types["AccountTicketIn"] = t.struct(
        {
            "webproperty": t.proxy(renames["WebpropertyIn"]).optional(),
            "profile": t.proxy(renames["ProfileIn"]).optional(),
            "redirectUri": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "account": t.proxy(renames["AccountIn"]).optional(),
        }
    ).named(renames["AccountTicketIn"])
    types["AccountTicketOut"] = t.struct(
        {
            "webproperty": t.proxy(renames["WebpropertyOut"]).optional(),
            "profile": t.proxy(renames["ProfileOut"]).optional(),
            "redirectUri": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "account": t.proxy(renames["AccountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountTicketOut"])
    types["HashClientIdResponseIn"] = t.struct(
        {
            "clientId": t.string(),
            "webPropertyId": t.string(),
            "kind": t.string(),
            "hashedClientId": t.string(),
        }
    ).named(renames["HashClientIdResponseIn"])
    types["HashClientIdResponseOut"] = t.struct(
        {
            "clientId": t.string(),
            "webPropertyId": t.string(),
            "kind": t.string(),
            "hashedClientId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HashClientIdResponseOut"])
    types["UserRefIn"] = t.struct(
        {
            "id": t.string().optional(),
            "email": t.string().optional(),
            "kind": t.string(),
        }
    ).named(renames["UserRefIn"])
    types["UserRefOut"] = t.struct(
        {
            "id": t.string().optional(),
            "email": t.string().optional(),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserRefOut"])
    types["FiltersIn"] = t.struct(
        {
            "username": t.string().optional(),
            "nextLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "kind": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "items": t.array(t.proxy(renames["FilterIn"])).optional(),
            "startIndex": t.integer().optional(),
            "previousLink": t.string().optional(),
        }
    ).named(renames["FiltersIn"])
    types["FiltersOut"] = t.struct(
        {
            "username": t.string().optional(),
            "nextLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "kind": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "items": t.array(t.proxy(renames["FilterOut"])).optional(),
            "startIndex": t.integer().optional(),
            "previousLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FiltersOut"])
    types["ProfileSummaryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "starred": t.boolean().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["ProfileSummaryIn"])
    types["ProfileSummaryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "starred": t.boolean().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileSummaryOut"])
    types["AccountSummariesIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["AccountSummaryIn"])).optional(),
            "previousLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "nextLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "username": t.string().optional(),
            "kind": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
        }
    ).named(renames["AccountSummariesIn"])
    types["AccountSummariesOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["AccountSummaryOut"])).optional(),
            "previousLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "nextLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "username": t.string().optional(),
            "kind": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountSummariesOut"])
    types["CustomDataSourcesIn"] = t.struct(
        {
            "username": t.string().optional(),
            "previousLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "itemsPerPage": t.integer().optional(),
            "nextLink": t.string().optional(),
            "items": t.array(t.proxy(renames["CustomDataSourceIn"])).optional(),
            "kind": t.string().optional(),
            "totalResults": t.integer().optional(),
        }
    ).named(renames["CustomDataSourcesIn"])
    types["CustomDataSourcesOut"] = t.struct(
        {
            "username": t.string().optional(),
            "previousLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "itemsPerPage": t.integer().optional(),
            "nextLink": t.string().optional(),
            "items": t.array(t.proxy(renames["CustomDataSourceOut"])).optional(),
            "kind": t.string().optional(),
            "totalResults": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomDataSourcesOut"])
    types["FilterIn"] = t.struct(
        {
            "lowercaseDetails": t.struct(
                {"field": t.string().optional(), "fieldIndex": t.integer().optional()}
            ).optional(),
            "advancedDetails": t.struct(
                {
                    "fieldA": t.string().optional(),
                    "outputToFieldIndex": t.integer().optional(),
                    "fieldARequired": t.boolean().optional(),
                    "outputConstructor": t.string().optional(),
                    "fieldAIndex": t.integer().optional(),
                    "fieldBRequired": t.boolean().optional(),
                    "overrideOutputField": t.boolean().optional(),
                    "fieldB": t.string().optional(),
                    "extractA": t.string().optional(),
                    "caseSensitive": t.boolean().optional(),
                    "fieldBIndex": t.integer().optional(),
                    "extractB": t.string().optional(),
                    "outputToField": t.string().optional(),
                }
            ).optional(),
            "accountId": t.string().optional(),
            "parentLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "type": t.string().optional(),
            "excludeDetails": t.proxy(renames["FilterExpressionIn"]).optional(),
            "uppercaseDetails": t.struct(
                {"field": t.string().optional(), "fieldIndex": t.integer().optional()}
            ).optional(),
            "includeDetails": t.proxy(renames["FilterExpressionIn"]).optional(),
            "searchAndReplaceDetails": t.struct(
                {
                    "replaceString": t.string().optional(),
                    "caseSensitive": t.boolean().optional(),
                    "fieldIndex": t.integer().optional(),
                    "searchString": t.string().optional(),
                    "field": t.string().optional(),
                }
            ).optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["FilterIn"])
    types["FilterOut"] = t.struct(
        {
            "lowercaseDetails": t.struct(
                {"field": t.string().optional(), "fieldIndex": t.integer().optional()}
            ).optional(),
            "selfLink": t.string().optional(),
            "advancedDetails": t.struct(
                {
                    "fieldA": t.string().optional(),
                    "outputToFieldIndex": t.integer().optional(),
                    "fieldARequired": t.boolean().optional(),
                    "outputConstructor": t.string().optional(),
                    "fieldAIndex": t.integer().optional(),
                    "fieldBRequired": t.boolean().optional(),
                    "overrideOutputField": t.boolean().optional(),
                    "fieldB": t.string().optional(),
                    "extractA": t.string().optional(),
                    "caseSensitive": t.boolean().optional(),
                    "fieldBIndex": t.integer().optional(),
                    "extractB": t.string().optional(),
                    "outputToField": t.string().optional(),
                }
            ).optional(),
            "accountId": t.string().optional(),
            "parentLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "type": t.string().optional(),
            "created": t.string().optional(),
            "excludeDetails": t.proxy(renames["FilterExpressionOut"]).optional(),
            "uppercaseDetails": t.struct(
                {"field": t.string().optional(), "fieldIndex": t.integer().optional()}
            ).optional(),
            "includeDetails": t.proxy(renames["FilterExpressionOut"]).optional(),
            "searchAndReplaceDetails": t.struct(
                {
                    "replaceString": t.string().optional(),
                    "caseSensitive": t.boolean().optional(),
                    "fieldIndex": t.integer().optional(),
                    "searchString": t.string().optional(),
                    "field": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "updated": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])
    types["CustomDataSourceIn"] = t.struct(
        {
            "importBehavior": t.string(),
            "created": t.string().optional(),
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "updated": t.string().optional(),
            "selfLink": t.string().optional(),
            "schema": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "description": t.string().optional(),
            "id": t.string().optional(),
            "parentLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "webPropertyId": t.string().optional(),
            "profilesLinked": t.array(t.string()).optional(),
            "childLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ),
            "uploadType": t.string().optional(),
        }
    ).named(renames["CustomDataSourceIn"])
    types["CustomDataSourceOut"] = t.struct(
        {
            "importBehavior": t.string(),
            "created": t.string().optional(),
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "updated": t.string().optional(),
            "selfLink": t.string().optional(),
            "schema": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "description": t.string().optional(),
            "id": t.string().optional(),
            "parentLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "webPropertyId": t.string().optional(),
            "profilesLinked": t.array(t.string()).optional(),
            "childLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ),
            "uploadType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomDataSourceOut"])
    types["FilterExpressionIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "matchType": t.string().optional(),
            "field": t.string().optional(),
            "fieldIndex": t.integer().optional(),
            "expressionValue": t.string().optional(),
        }
    ).named(renames["FilterExpressionIn"])
    types["FilterExpressionOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "matchType": t.string().optional(),
            "field": t.string().optional(),
            "fieldIndex": t.integer().optional(),
            "expressionValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterExpressionOut"])
    types["AccountRefIn"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "href": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AccountRefIn"])
    types["AccountRefOut"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "href": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountRefOut"])
    types["CustomDimensionIn"] = t.struct(
        {
            "scope": t.string().optional(),
            "active": t.boolean().optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "parentLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "webPropertyId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CustomDimensionIn"])
    types["CustomDimensionOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "active": t.boolean().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "parentLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "updated": t.string().optional(),
            "created": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "name": t.string().optional(),
            "selfLink": t.string().optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomDimensionOut"])
    types["RealtimeDataIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "columnHeaders": t.array(
                t.struct(
                    {
                        "name": t.string().optional(),
                        "columnType": t.string().optional(),
                        "dataType": t.string().optional(),
                    }
                )
            ).optional(),
            "selfLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "id": t.string().optional(),
            "totalsForAllResults": t.struct({"_": t.string().optional()}).optional(),
            "rows": t.array(t.array(t.string())).optional(),
            "query": t.struct(
                {
                    "filters": t.string().optional(),
                    "dimensions": t.string().optional(),
                    "max-results": t.integer().optional(),
                    "ids": t.string().optional(),
                    "sort": t.array(t.string()).optional(),
                    "metrics": t.array(t.string()).optional(),
                }
            ).optional(),
            "profileInfo": t.struct(
                {
                    "profileName": t.string().optional(),
                    "profileId": t.string().optional(),
                    "tableId": t.string().optional(),
                    "webPropertyId": t.string().optional(),
                    "accountId": t.string().optional(),
                    "internalWebPropertyId": t.string().optional(),
                }
            ).optional(),
        }
    ).named(renames["RealtimeDataIn"])
    types["RealtimeDataOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "columnHeaders": t.array(
                t.struct(
                    {
                        "name": t.string().optional(),
                        "columnType": t.string().optional(),
                        "dataType": t.string().optional(),
                    }
                )
            ).optional(),
            "selfLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "id": t.string().optional(),
            "totalsForAllResults": t.struct({"_": t.string().optional()}).optional(),
            "rows": t.array(t.array(t.string())).optional(),
            "query": t.struct(
                {
                    "filters": t.string().optional(),
                    "dimensions": t.string().optional(),
                    "max-results": t.integer().optional(),
                    "ids": t.string().optional(),
                    "sort": t.array(t.string()).optional(),
                    "metrics": t.array(t.string()).optional(),
                }
            ).optional(),
            "profileInfo": t.struct(
                {
                    "profileName": t.string().optional(),
                    "profileId": t.string().optional(),
                    "tableId": t.string().optional(),
                    "webPropertyId": t.string().optional(),
                    "accountId": t.string().optional(),
                    "internalWebPropertyId": t.string().optional(),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RealtimeDataOut"])
    types["CustomMetricIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "min_value": t.string().optional(),
            "scope": t.string().optional(),
            "max_value": t.string().optional(),
            "active": t.boolean().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "parentLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "webPropertyId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CustomMetricIn"])
    types["CustomMetricOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "min_value": t.string().optional(),
            "kind": t.string().optional(),
            "scope": t.string().optional(),
            "created": t.string().optional(),
            "max_value": t.string().optional(),
            "index": t.integer().optional(),
            "active": t.boolean().optional(),
            "id": t.string().optional(),
            "updated": t.string().optional(),
            "type": t.string().optional(),
            "parentLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "webPropertyId": t.string().optional(),
            "selfLink": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomMetricOut"])
    types["CustomDimensionsIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "kind": t.string().optional(),
            "nextLink": t.string().optional(),
            "items": t.array(t.proxy(renames["CustomDimensionIn"])).optional(),
            "totalResults": t.integer().optional(),
            "username": t.string().optional(),
            "previousLink": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
        }
    ).named(renames["CustomDimensionsIn"])
    types["CustomDimensionsOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "kind": t.string().optional(),
            "nextLink": t.string().optional(),
            "items": t.array(t.proxy(renames["CustomDimensionOut"])).optional(),
            "totalResults": t.integer().optional(),
            "username": t.string().optional(),
            "previousLink": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomDimensionsOut"])
    types["ProfilesIn"] = t.struct(
        {
            "totalResults": t.integer().optional(),
            "kind": t.string().optional(),
            "nextLink": t.string().optional(),
            "previousLink": t.string().optional(),
            "items": t.array(t.proxy(renames["ProfileIn"])).optional(),
            "username": t.string().optional(),
            "startIndex": t.integer().optional(),
            "itemsPerPage": t.integer().optional(),
        }
    ).named(renames["ProfilesIn"])
    types["ProfilesOut"] = t.struct(
        {
            "totalResults": t.integer().optional(),
            "kind": t.string().optional(),
            "nextLink": t.string().optional(),
            "previousLink": t.string().optional(),
            "items": t.array(t.proxy(renames["ProfileOut"])).optional(),
            "username": t.string().optional(),
            "startIndex": t.integer().optional(),
            "itemsPerPage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfilesOut"])
    types["SegmentsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "startIndex": t.integer().optional(),
            "username": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "totalResults": t.integer().optional(),
            "previousLink": t.string().optional(),
            "nextLink": t.string().optional(),
            "items": t.array(t.proxy(renames["SegmentIn"])).optional(),
        }
    ).named(renames["SegmentsIn"])
    types["SegmentsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "startIndex": t.integer().optional(),
            "username": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "totalResults": t.integer().optional(),
            "previousLink": t.string().optional(),
            "nextLink": t.string().optional(),
            "items": t.array(t.proxy(renames["SegmentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentsOut"])
    types["SegmentIn"] = t.struct(
        {
            "created": t.string().optional(),
            "updated": t.string().optional(),
            "kind": t.string().optional(),
            "segmentId": t.string().optional(),
            "selfLink": t.string().optional(),
            "definition": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SegmentIn"])
    types["SegmentOut"] = t.struct(
        {
            "created": t.string().optional(),
            "updated": t.string().optional(),
            "kind": t.string().optional(),
            "segmentId": t.string().optional(),
            "selfLink": t.string().optional(),
            "definition": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentOut"])
    types["GaDataIn"] = t.struct(
        {
            "dataTable": t.struct(
                {
                    "cols": t.array(
                        t.struct(
                            {"id": t.string(), "label": t.string(), "type": t.string()}
                        )
                    ),
                    "rows": t.array(
                        t.struct({"c": t.array(t.struct({"v": t.string()}))})
                    ),
                }
            ),
            "rows": t.array(t.array(t.string())).optional(),
            "query": t.struct(
                {
                    "segment": t.string().optional(),
                    "start-index": t.integer().optional(),
                    "filters": t.string().optional(),
                    "metrics": t.array(t.string()).optional(),
                    "ids": t.string().optional(),
                    "max-results": t.integer().optional(),
                    "sort": t.array(t.string()).optional(),
                    "samplingLevel": t.string().optional(),
                    "end-date": t.string().optional(),
                    "dimensions": t.string().optional(),
                    "start-date": t.string().optional(),
                }
            ).optional(),
            "sampleSpace": t.string().optional(),
            "selfLink": t.string().optional(),
            "id": t.string().optional(),
            "profileInfo": t.struct(
                {
                    "profileId": t.string().optional(),
                    "tableId": t.string().optional(),
                    "profileName": t.string().optional(),
                    "webPropertyId": t.string().optional(),
                    "internalWebPropertyId": t.string().optional(),
                    "accountId": t.string().optional(),
                }
            ).optional(),
            "totalResults": t.integer().optional(),
            "previousLink": t.string().optional(),
            "dataLastRefreshed": t.string().optional(),
            "sampleSize": t.string().optional(),
            "totalsForAllResults": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "columnHeaders": t.array(
                t.struct(
                    {
                        "columnType": t.string().optional(),
                        "dataType": t.string().optional(),
                        "name": t.string().optional(),
                    }
                )
            ).optional(),
            "nextLink": t.string().optional(),
            "containsSampledData": t.boolean().optional(),
            "itemsPerPage": t.integer().optional(),
        }
    ).named(renames["GaDataIn"])
    types["GaDataOut"] = t.struct(
        {
            "dataTable": t.struct(
                {
                    "cols": t.array(
                        t.struct(
                            {"id": t.string(), "label": t.string(), "type": t.string()}
                        )
                    ),
                    "rows": t.array(
                        t.struct({"c": t.array(t.struct({"v": t.string()}))})
                    ),
                }
            ),
            "rows": t.array(t.array(t.string())).optional(),
            "query": t.struct(
                {
                    "segment": t.string().optional(),
                    "start-index": t.integer().optional(),
                    "filters": t.string().optional(),
                    "metrics": t.array(t.string()).optional(),
                    "ids": t.string().optional(),
                    "max-results": t.integer().optional(),
                    "sort": t.array(t.string()).optional(),
                    "samplingLevel": t.string().optional(),
                    "end-date": t.string().optional(),
                    "dimensions": t.string().optional(),
                    "start-date": t.string().optional(),
                }
            ).optional(),
            "sampleSpace": t.string().optional(),
            "selfLink": t.string().optional(),
            "id": t.string().optional(),
            "profileInfo": t.struct(
                {
                    "profileId": t.string().optional(),
                    "tableId": t.string().optional(),
                    "profileName": t.string().optional(),
                    "webPropertyId": t.string().optional(),
                    "internalWebPropertyId": t.string().optional(),
                    "accountId": t.string().optional(),
                }
            ).optional(),
            "totalResults": t.integer().optional(),
            "previousLink": t.string().optional(),
            "dataLastRefreshed": t.string().optional(),
            "sampleSize": t.string().optional(),
            "totalsForAllResults": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "columnHeaders": t.array(
                t.struct(
                    {
                        "columnType": t.string().optional(),
                        "dataType": t.string().optional(),
                        "name": t.string().optional(),
                    }
                )
            ).optional(),
            "nextLink": t.string().optional(),
            "containsSampledData": t.boolean().optional(),
            "itemsPerPage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GaDataOut"])
    types["AccountsIn"] = t.struct(
        {
            "totalResults": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "previousLink": t.string().optional(),
            "username": t.string().optional(),
            "items": t.array(t.proxy(renames["AccountIn"])).optional(),
            "kind": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "nextLink": t.string().optional(),
        }
    ).named(renames["AccountsIn"])
    types["AccountsOut"] = t.struct(
        {
            "totalResults": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "previousLink": t.string().optional(),
            "username": t.string().optional(),
            "items": t.array(t.proxy(renames["AccountOut"])).optional(),
            "kind": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "nextLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsOut"])
    types["ProfileIn"] = t.struct(
        {
            "siteSearchCategoryParameters": t.string().optional(),
            "siteSearchQueryParameters": t.string().optional(),
            "enhancedECommerceTracking": t.boolean().optional(),
            "stripSiteSearchCategoryParameters": t.boolean().optional(),
            "excludeQueryParameters": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "eCommerceTracking": t.boolean().optional(),
            "botFilteringEnabled": t.boolean().optional(),
            "permissions": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "currency": t.string().optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "type": t.string().optional(),
            "parentLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "starred": t.boolean().optional(),
            "timezone": t.string().optional(),
            "stripSiteSearchQueryParameters": t.boolean().optional(),
            "defaultPage": t.string().optional(),
            "childLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
        }
    ).named(renames["ProfileIn"])
    types["ProfileOut"] = t.struct(
        {
            "updated": t.string().optional(),
            "siteSearchCategoryParameters": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "siteSearchQueryParameters": t.string().optional(),
            "enhancedECommerceTracking": t.boolean().optional(),
            "stripSiteSearchCategoryParameters": t.boolean().optional(),
            "excludeQueryParameters": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "eCommerceTracking": t.boolean().optional(),
            "botFilteringEnabled": t.boolean().optional(),
            "permissions": t.struct(
                {"effective": t.array(t.string()).optional()}
            ).optional(),
            "name": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
            "selfLink": t.string().optional(),
            "currency": t.string().optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "type": t.string().optional(),
            "parentLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "starred": t.boolean().optional(),
            "kind": t.string().optional(),
            "timezone": t.string().optional(),
            "stripSiteSearchQueryParameters": t.boolean().optional(),
            "defaultPage": t.string().optional(),
            "childLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "created": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileOut"])
    types["ColumnsIn"] = t.struct(
        {
            "attributeNames": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "totalResults": t.integer().optional(),
            "items": t.array(t.proxy(renames["ColumnIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["ColumnsIn"])
    types["ColumnsOut"] = t.struct(
        {
            "attributeNames": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "totalResults": t.integer().optional(),
            "items": t.array(t.proxy(renames["ColumnOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnsOut"])
    types["ColumnIn"] = t.struct(
        {
            "id": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ColumnIn"])
    types["ColumnOut"] = t.struct(
        {
            "id": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnOut"])
    types["HashClientIdRequestIn"] = t.struct(
        {"clientId": t.string(), "kind": t.string(), "webPropertyId": t.string()}
    ).named(renames["HashClientIdRequestIn"])
    types["HashClientIdRequestOut"] = t.struct(
        {
            "clientId": t.string(),
            "kind": t.string(),
            "webPropertyId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HashClientIdRequestOut"])
    types["AccountTreeResponseIn"] = t.struct(
        {
            "account": t.proxy(renames["AccountIn"]).optional(),
            "kind": t.string().optional(),
            "webproperty": t.proxy(renames["WebpropertyIn"]).optional(),
            "profile": t.proxy(renames["ProfileIn"]).optional(),
        }
    ).named(renames["AccountTreeResponseIn"])
    types["AccountTreeResponseOut"] = t.struct(
        {
            "account": t.proxy(renames["AccountOut"]).optional(),
            "kind": t.string().optional(),
            "webproperty": t.proxy(renames["WebpropertyOut"]).optional(),
            "profile": t.proxy(renames["ProfileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountTreeResponseOut"])
    types["GoalIn"] = t.struct(
        {
            "active": t.boolean().optional(),
            "webPropertyId": t.string().optional(),
            "created": t.string().optional(),
            "eventDetails": t.struct(
                {
                    "useEventValue": t.boolean().optional(),
                    "eventConditions": t.array(
                        t.struct(
                            {
                                "type": t.string().optional(),
                                "comparisonType": t.string().optional(),
                                "matchType": t.string().optional(),
                                "comparisonValue": t.string().optional(),
                                "expression": t.string().optional(),
                            }
                        )
                    ).optional(),
                }
            ).optional(),
            "accountId": t.string().optional(),
            "profileId": t.string().optional(),
            "visitTimeOnSiteDetails": t.struct(
                {
                    "comparisonType": t.string().optional(),
                    "comparisonValue": t.string().optional(),
                }
            ).optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "visitNumPagesDetails": t.struct(
                {
                    "comparisonType": t.string().optional(),
                    "comparisonValue": t.string().optional(),
                }
            ).optional(),
            "updated": t.string().optional(),
            "parentLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "urlDestinationDetails": t.struct(
                {
                    "caseSensitive": t.boolean().optional(),
                    "steps": t.array(
                        t.struct(
                            {
                                "url": t.string().optional(),
                                "name": t.string().optional(),
                                "number": t.integer().optional(),
                            }
                        )
                    ).optional(),
                    "firstStepRequired": t.boolean().optional(),
                    "matchType": t.string().optional(),
                    "url": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "value": t.number().optional(),
            "selfLink": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
        }
    ).named(renames["GoalIn"])
    types["GoalOut"] = t.struct(
        {
            "active": t.boolean().optional(),
            "webPropertyId": t.string().optional(),
            "created": t.string().optional(),
            "eventDetails": t.struct(
                {
                    "useEventValue": t.boolean().optional(),
                    "eventConditions": t.array(
                        t.struct(
                            {
                                "type": t.string().optional(),
                                "comparisonType": t.string().optional(),
                                "matchType": t.string().optional(),
                                "comparisonValue": t.string().optional(),
                                "expression": t.string().optional(),
                            }
                        )
                    ).optional(),
                }
            ).optional(),
            "accountId": t.string().optional(),
            "profileId": t.string().optional(),
            "visitTimeOnSiteDetails": t.struct(
                {
                    "comparisonType": t.string().optional(),
                    "comparisonValue": t.string().optional(),
                }
            ).optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "visitNumPagesDetails": t.struct(
                {
                    "comparisonType": t.string().optional(),
                    "comparisonValue": t.string().optional(),
                }
            ).optional(),
            "updated": t.string().optional(),
            "parentLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "urlDestinationDetails": t.struct(
                {
                    "caseSensitive": t.boolean().optional(),
                    "steps": t.array(
                        t.struct(
                            {
                                "url": t.string().optional(),
                                "name": t.string().optional(),
                                "number": t.integer().optional(),
                            }
                        )
                    ).optional(),
                    "firstStepRequired": t.boolean().optional(),
                    "matchType": t.string().optional(),
                    "url": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "value": t.number().optional(),
            "selfLink": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoalOut"])
    types["AdWordsAccountIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "autoTaggingEnabled": t.boolean().optional(),
            "customerId": t.string().optional(),
        }
    ).named(renames["AdWordsAccountIn"])
    types["AdWordsAccountOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "autoTaggingEnabled": t.boolean().optional(),
            "customerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdWordsAccountOut"])
    types["UnsampledReportIn"] = t.struct(
        {
            "metrics": t.string().optional(),
            "title": t.string().optional(),
            "start-date": t.string().optional(),
            "filters": t.string().optional(),
            "end-date": t.string().optional(),
            "profileId": t.string().optional(),
            "id": t.string().optional(),
            "segment": t.string().optional(),
            "accountId": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "dimensions": t.string().optional(),
        }
    ).named(renames["UnsampledReportIn"])
    types["UnsampledReportOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "metrics": t.string().optional(),
            "title": t.string().optional(),
            "start-date": t.string().optional(),
            "cloudStorageDownloadDetails": t.struct(
                {"objectId": t.string().optional(), "bucketId": t.string().optional()}
            ).optional(),
            "filters": t.string().optional(),
            "selfLink": t.string().optional(),
            "downloadType": t.string().optional(),
            "updated": t.string().optional(),
            "end-date": t.string().optional(),
            "profileId": t.string().optional(),
            "id": t.string().optional(),
            "driveDownloadDetails": t.struct(
                {"documentId": t.string().optional()}
            ).optional(),
            "created": t.string().optional(),
            "segment": t.string().optional(),
            "accountId": t.string().optional(),
            "status": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "dimensions": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnsampledReportOut"])
    types["UploadsIn"] = t.struct(
        {
            "nextLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "items": t.array(t.proxy(renames["UploadIn"])).optional(),
            "itemsPerPage": t.integer().optional(),
            "kind": t.string().optional(),
            "previousLink": t.string().optional(),
            "totalResults": t.integer().optional(),
        }
    ).named(renames["UploadsIn"])
    types["UploadsOut"] = t.struct(
        {
            "nextLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "items": t.array(t.proxy(renames["UploadOut"])).optional(),
            "itemsPerPage": t.integer().optional(),
            "kind": t.string().optional(),
            "previousLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadsOut"])
    types["UploadIn"] = t.struct(
        {
            "errors": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "uploadTime": t.string().optional(),
            "status": t.string().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
            "customDataSourceId": t.string().optional(),
        }
    ).named(renames["UploadIn"])
    types["UploadOut"] = t.struct(
        {
            "errors": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "uploadTime": t.string().optional(),
            "status": t.string().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
            "customDataSourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadOut"])
    types["RemarketingAudiencesIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["RemarketingAudienceIn"])).optional(),
            "username": t.string().optional(),
            "previousLink": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "totalResults": t.integer().optional(),
            "kind": t.string().optional(),
            "nextLink": t.string().optional(),
            "startIndex": t.integer().optional(),
        }
    ).named(renames["RemarketingAudiencesIn"])
    types["RemarketingAudiencesOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["RemarketingAudienceOut"])).optional(),
            "username": t.string().optional(),
            "previousLink": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "totalResults": t.integer().optional(),
            "kind": t.string().optional(),
            "nextLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemarketingAudiencesOut"])
    types["EntityAdWordsLinkIn"] = t.struct(
        {
            "adWordsAccounts": t.array(t.proxy(renames["AdWordsAccountIn"])).optional(),
            "entity": t.struct(
                {"webPropertyRef": t.proxy(renames["WebPropertyRefIn"])}
            ).optional(),
            "profileIds": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "selfLink": t.string().optional(),
        }
    ).named(renames["EntityAdWordsLinkIn"])
    types["EntityAdWordsLinkOut"] = t.struct(
        {
            "adWordsAccounts": t.array(
                t.proxy(renames["AdWordsAccountOut"])
            ).optional(),
            "entity": t.struct(
                {"webPropertyRef": t.proxy(renames["WebPropertyRefOut"])}
            ).optional(),
            "profileIds": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityAdWordsLinkOut"])
    types["WebpropertiesIn"] = t.struct(
        {
            "itemsPerPage": t.integer().optional(),
            "previousLink": t.string().optional(),
            "items": t.array(t.proxy(renames["WebpropertyIn"])).optional(),
            "username": t.string().optional(),
            "nextLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "kind": t.string().optional(),
            "startIndex": t.integer().optional(),
        }
    ).named(renames["WebpropertiesIn"])
    types["WebpropertiesOut"] = t.struct(
        {
            "itemsPerPage": t.integer().optional(),
            "previousLink": t.string().optional(),
            "items": t.array(t.proxy(renames["WebpropertyOut"])).optional(),
            "username": t.string().optional(),
            "nextLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "kind": t.string().optional(),
            "startIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebpropertiesOut"])
    types["ProfileFilterLinksIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "totalResults": t.integer().optional(),
            "nextLink": t.string().optional(),
            "items": t.array(t.proxy(renames["ProfileFilterLinkIn"])).optional(),
            "previousLink": t.string().optional(),
            "username": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ProfileFilterLinksIn"])
    types["ProfileFilterLinksOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "totalResults": t.integer().optional(),
            "nextLink": t.string().optional(),
            "items": t.array(t.proxy(renames["ProfileFilterLinkOut"])).optional(),
            "previousLink": t.string().optional(),
            "username": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileFilterLinksOut"])
    types["McfDataIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "sampleSpace": t.string().optional(),
            "totalsForAllResults": t.struct({"_": t.string().optional()}).optional(),
            "itemsPerPage": t.integer().optional(),
            "id": t.string().optional(),
            "containsSampledData": t.boolean().optional(),
            "profileInfo": t.struct(
                {
                    "profileName": t.string().optional(),
                    "accountId": t.string().optional(),
                    "internalWebPropertyId": t.string().optional(),
                    "profileId": t.string().optional(),
                    "tableId": t.string().optional(),
                    "webPropertyId": t.string().optional(),
                }
            ).optional(),
            "totalResults": t.integer().optional(),
            "query": t.struct(
                {
                    "start-index": t.integer().optional(),
                    "start-date": t.string().optional(),
                    "end-date": t.string().optional(),
                    "dimensions": t.string().optional(),
                    "segment": t.string().optional(),
                    "ids": t.string().optional(),
                    "sort": t.array(t.string()).optional(),
                    "metrics": t.array(t.string()).optional(),
                    "filters": t.string().optional(),
                    "samplingLevel": t.string().optional(),
                    "max-results": t.integer().optional(),
                }
            ).optional(),
            "rows": t.array(
                t.array(
                    t.struct(
                        {
                            "conversionPathValue": t.array(
                                t.struct(
                                    {
                                        "interactionType": t.string().optional(),
                                        "nodeValue": t.string().optional(),
                                    }
                                )
                            ).optional(),
                            "primitiveValue": t.string().optional(),
                        }
                    )
                )
            ).optional(),
            "columnHeaders": t.array(
                t.struct(
                    {
                        "dataType": t.string().optional(),
                        "columnType": t.string().optional(),
                        "name": t.string().optional(),
                    }
                )
            ).optional(),
            "previousLink": t.string().optional(),
            "sampleSize": t.string().optional(),
            "selfLink": t.string().optional(),
            "nextLink": t.string().optional(),
        }
    ).named(renames["McfDataIn"])
    types["McfDataOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "sampleSpace": t.string().optional(),
            "totalsForAllResults": t.struct({"_": t.string().optional()}).optional(),
            "itemsPerPage": t.integer().optional(),
            "id": t.string().optional(),
            "containsSampledData": t.boolean().optional(),
            "profileInfo": t.struct(
                {
                    "profileName": t.string().optional(),
                    "accountId": t.string().optional(),
                    "internalWebPropertyId": t.string().optional(),
                    "profileId": t.string().optional(),
                    "tableId": t.string().optional(),
                    "webPropertyId": t.string().optional(),
                }
            ).optional(),
            "totalResults": t.integer().optional(),
            "query": t.struct(
                {
                    "start-index": t.integer().optional(),
                    "start-date": t.string().optional(),
                    "end-date": t.string().optional(),
                    "dimensions": t.string().optional(),
                    "segment": t.string().optional(),
                    "ids": t.string().optional(),
                    "sort": t.array(t.string()).optional(),
                    "metrics": t.array(t.string()).optional(),
                    "filters": t.string().optional(),
                    "samplingLevel": t.string().optional(),
                    "max-results": t.integer().optional(),
                }
            ).optional(),
            "rows": t.array(
                t.array(
                    t.struct(
                        {
                            "conversionPathValue": t.array(
                                t.struct(
                                    {
                                        "interactionType": t.string().optional(),
                                        "nodeValue": t.string().optional(),
                                    }
                                )
                            ).optional(),
                            "primitiveValue": t.string().optional(),
                        }
                    )
                )
            ).optional(),
            "columnHeaders": t.array(
                t.struct(
                    {
                        "dataType": t.string().optional(),
                        "columnType": t.string().optional(),
                        "name": t.string().optional(),
                    }
                )
            ).optional(),
            "previousLink": t.string().optional(),
            "sampleSize": t.string().optional(),
            "selfLink": t.string().optional(),
            "nextLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["McfDataOut"])
    types["ExperimentIn"] = t.struct(
        {
            "parentLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "objectiveMetric": t.string().optional(),
            "description": t.string().optional(),
            "optimizationType": t.string().optional(),
            "reasonExperimentEnded": t.string().optional(),
            "winnerConfidenceLevel": t.number().optional(),
            "endTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "trafficCoverage": t.number().optional(),
            "variations": t.array(
                t.struct(
                    {
                        "status": t.string().optional(),
                        "weight": t.number().optional(),
                        "name": t.string().optional(),
                        "won": t.boolean().optional(),
                        "url": t.string().optional(),
                    }
                )
            ).optional(),
            "updated": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "minimumExperimentLengthInDays": t.integer().optional(),
            "internalWebPropertyId": t.string().optional(),
            "rewriteVariationUrlsAsOriginal": t.boolean().optional(),
            "snippet": t.string().optional(),
            "profileId": t.string().optional(),
            "editableInGaUi": t.boolean().optional(),
            "equalWeighting": t.boolean().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "servingFramework": t.string().optional(),
            "winnerFound": t.boolean().optional(),
            "startTime": t.string().optional(),
            "created": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["ExperimentIn"])
    types["ExperimentOut"] = t.struct(
        {
            "parentLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "objectiveMetric": t.string().optional(),
            "description": t.string().optional(),
            "optimizationType": t.string().optional(),
            "reasonExperimentEnded": t.string().optional(),
            "winnerConfidenceLevel": t.number().optional(),
            "endTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "trafficCoverage": t.number().optional(),
            "variations": t.array(
                t.struct(
                    {
                        "status": t.string().optional(),
                        "weight": t.number().optional(),
                        "name": t.string().optional(),
                        "won": t.boolean().optional(),
                        "url": t.string().optional(),
                    }
                )
            ).optional(),
            "updated": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "minimumExperimentLengthInDays": t.integer().optional(),
            "internalWebPropertyId": t.string().optional(),
            "rewriteVariationUrlsAsOriginal": t.boolean().optional(),
            "snippet": t.string().optional(),
            "profileId": t.string().optional(),
            "editableInGaUi": t.boolean().optional(),
            "equalWeighting": t.boolean().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "servingFramework": t.string().optional(),
            "winnerFound": t.boolean().optional(),
            "startTime": t.string().optional(),
            "created": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExperimentOut"])
    types["CustomMetricsIn"] = t.struct(
        {
            "nextLink": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "username": t.string().optional(),
            "items": t.array(t.proxy(renames["CustomMetricIn"])).optional(),
            "startIndex": t.integer().optional(),
            "previousLink": t.string().optional(),
            "kind": t.string().optional(),
            "totalResults": t.integer().optional(),
        }
    ).named(renames["CustomMetricsIn"])
    types["CustomMetricsOut"] = t.struct(
        {
            "nextLink": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "username": t.string().optional(),
            "items": t.array(t.proxy(renames["CustomMetricOut"])).optional(),
            "startIndex": t.integer().optional(),
            "previousLink": t.string().optional(),
            "kind": t.string().optional(),
            "totalResults": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomMetricsOut"])
    types["LinkedForeignAccountIn"] = t.struct(
        {
            "type": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "remarketingAudienceId": t.string().optional(),
            "status": t.string().optional(),
            "id": t.string().optional(),
            "linkedAccountId": t.string().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LinkedForeignAccountIn"])
    types["LinkedForeignAccountOut"] = t.struct(
        {
            "type": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "eligibleForSearch": t.boolean().optional(),
            "remarketingAudienceId": t.string().optional(),
            "status": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
            "id": t.string().optional(),
            "linkedAccountId": t.string().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedForeignAccountOut"])
    types["ProfileRefIn"] = t.struct(
        {
            "internalWebPropertyId": t.string().optional(),
            "href": t.string().optional(),
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ProfileRefIn"])
    types["ProfileRefOut"] = t.struct(
        {
            "internalWebPropertyId": t.string().optional(),
            "href": t.string().optional(),
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileRefOut"])

    functions = {}
    functions["userDeletionUserDeletionRequestUpsert"] = analytics.post(
        "userDeletion/userDeletionRequests:upsert",
        t.struct(
            {
                "kind": t.string().optional(),
                "id": t.struct(
                    {"userId": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "propertyId": t.string().optional(),
                "firebaseProjectId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserDeletionRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["provisioningCreateAccountTicket"] = analytics.post(
        "provisioning/createAccountTree",
        t.struct(
            {
                "webpropertyName": t.string(),
                "profileName": t.string(),
                "accountName": t.string(),
                "websiteUrl": t.string(),
                "timezone": t.string(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountTreeResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["provisioningCreateAccountTree"] = analytics.post(
        "provisioning/createAccountTree",
        t.struct(
            {
                "webpropertyName": t.string(),
                "profileName": t.string(),
                "accountName": t.string(),
                "websiteUrl": t.string(),
                "timezone": t.string(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountTreeResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["dataMcfGet"] = analytics.get(
        "data/mcf",
        t.struct(
            {
                "metrics": t.string().optional(),
                "dimensions": t.string().optional(),
                "ids": t.string().optional(),
                "sort": t.string().optional(),
                "start-date": t.string().optional(),
                "samplingLevel": t.string().optional(),
                "max-results": t.integer().optional(),
                "end-date": t.string().optional(),
                "start-index": t.integer().optional(),
                "filters": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["McfDataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["dataRealtimeGet"] = analytics.get(
        "data/realtime",
        t.struct(
            {
                "metrics": t.string().optional(),
                "max-results": t.integer().optional(),
                "dimensions": t.string().optional(),
                "sort": t.string().optional(),
                "filters": t.string().optional(),
                "ids": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RealtimeDataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["dataGaGet"] = analytics.get(
        "data/ga",
        t.struct(
            {
                "start-index": t.integer().optional(),
                "include-empty-rows": t.boolean().optional(),
                "max-results": t.integer().optional(),
                "segment": t.string().optional(),
                "samplingLevel": t.string().optional(),
                "output": t.string().optional(),
                "filters": t.string().optional(),
                "end-date": t.string().optional(),
                "start-date": t.string().optional(),
                "ids": t.string().optional(),
                "sort": t.string().optional(),
                "metrics": t.string().optional(),
                "dimensions": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GaDataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["metadataColumnsList"] = analytics.get(
        "metadata/{reportType}/columns",
        t.struct({"reportType": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ColumnsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementClientIdHashClientId"] = analytics.post(
        "management/clientId:hashClientId",
        t.struct(
            {
                "clientId": t.string(),
                "kind": t.string(),
                "webPropertyId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HashClientIdResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomDataSourcesList"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDataSources",
        t.struct(
            {
                "max-results": t.integer().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomDataSourcesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementAccountsList"] = analytics.get(
        "management/accounts",
        t.struct(
            {
                "max-results": t.integer().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementAccountUserLinksUpdate"] = analytics.post(
        "management/accounts/{accountId}/entityUserLinks",
        t.struct(
            {
                "accountId": t.string().optional(),
                "permissions": t.struct(
                    {"local": t.array(t.string()).optional()}
                ).optional(),
                "selfLink": t.string().optional(),
                "entity": t.struct(
                    {
                        "webPropertyRef": t.proxy(
                            renames["WebPropertyRefIn"]
                        ).optional(),
                        "accountRef": t.proxy(renames["AccountRefIn"]).optional(),
                        "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "userRef": t.proxy(renames["UserRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityUserLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementAccountUserLinksList"] = analytics.post(
        "management/accounts/{accountId}/entityUserLinks",
        t.struct(
            {
                "accountId": t.string().optional(),
                "permissions": t.struct(
                    {"local": t.array(t.string()).optional()}
                ).optional(),
                "selfLink": t.string().optional(),
                "entity": t.struct(
                    {
                        "webPropertyRef": t.proxy(
                            renames["WebPropertyRefIn"]
                        ).optional(),
                        "accountRef": t.proxy(renames["AccountRefIn"]).optional(),
                        "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "userRef": t.proxy(renames["UserRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityUserLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementAccountUserLinksDelete"] = analytics.post(
        "management/accounts/{accountId}/entityUserLinks",
        t.struct(
            {
                "accountId": t.string().optional(),
                "permissions": t.struct(
                    {"local": t.array(t.string()).optional()}
                ).optional(),
                "selfLink": t.string().optional(),
                "entity": t.struct(
                    {
                        "webPropertyRef": t.proxy(
                            renames["WebPropertyRefIn"]
                        ).optional(),
                        "accountRef": t.proxy(renames["AccountRefIn"]).optional(),
                        "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "userRef": t.proxy(renames["UserRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityUserLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementAccountUserLinksInsert"] = analytics.post(
        "management/accounts/{accountId}/entityUserLinks",
        t.struct(
            {
                "accountId": t.string().optional(),
                "permissions": t.struct(
                    {"local": t.array(t.string()).optional()}
                ).optional(),
                "selfLink": t.string().optional(),
                "entity": t.struct(
                    {
                        "webPropertyRef": t.proxy(
                            renames["WebPropertyRefIn"]
                        ).optional(),
                        "accountRef": t.proxy(renames["AccountRefIn"]).optional(),
                        "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "userRef": t.proxy(renames["UserRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityUserLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileUserLinksDelete"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/entityUserLinks",
        t.struct(
            {
                "accountId": t.string().optional(),
                "start-index": t.integer().optional(),
                "webPropertyId": t.string().optional(),
                "profileId": t.string().optional(),
                "max-results": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityUserLinksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileUserLinksInsert"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/entityUserLinks",
        t.struct(
            {
                "accountId": t.string().optional(),
                "start-index": t.integer().optional(),
                "webPropertyId": t.string().optional(),
                "profileId": t.string().optional(),
                "max-results": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityUserLinksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileUserLinksUpdate"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/entityUserLinks",
        t.struct(
            {
                "accountId": t.string().optional(),
                "start-index": t.integer().optional(),
                "webPropertyId": t.string().optional(),
                "profileId": t.string().optional(),
                "max-results": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityUserLinksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileUserLinksList"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/entityUserLinks",
        t.struct(
            {
                "accountId": t.string().optional(),
                "start-index": t.integer().optional(),
                "webPropertyId": t.string().optional(),
                "profileId": t.string().optional(),
                "max-results": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityUserLinksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementAccountSummariesList"] = analytics.get(
        "management/accountSummaries",
        t.struct(
            {
                "max-results": t.integer().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountSummariesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementFiltersDelete"] = analytics.get(
        "management/accounts/{accountId}/filters",
        t.struct(
            {
                "max-results": t.integer().optional(),
                "accountId": t.string().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FiltersOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementFiltersUpdate"] = analytics.get(
        "management/accounts/{accountId}/filters",
        t.struct(
            {
                "max-results": t.integer().optional(),
                "accountId": t.string().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FiltersOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementFiltersInsert"] = analytics.get(
        "management/accounts/{accountId}/filters",
        t.struct(
            {
                "max-results": t.integer().optional(),
                "accountId": t.string().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FiltersOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementFiltersGet"] = analytics.get(
        "management/accounts/{accountId}/filters",
        t.struct(
            {
                "max-results": t.integer().optional(),
                "accountId": t.string().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FiltersOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementFiltersPatch"] = analytics.get(
        "management/accounts/{accountId}/filters",
        t.struct(
            {
                "max-results": t.integer().optional(),
                "accountId": t.string().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FiltersOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementFiltersList"] = analytics.get(
        "management/accounts/{accountId}/filters",
        t.struct(
            {
                "max-results": t.integer().optional(),
                "accountId": t.string().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FiltersOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementGoalsInsert"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/goals/{goalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "goalId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "profileId": t.string().optional(),
                "active": t.boolean().optional(),
                "created": t.string().optional(),
                "eventDetails": t.struct(
                    {
                        "useEventValue": t.boolean().optional(),
                        "eventConditions": t.array(
                            t.struct(
                                {
                                    "type": t.string().optional(),
                                    "comparisonType": t.string().optional(),
                                    "matchType": t.string().optional(),
                                    "comparisonValue": t.string().optional(),
                                    "expression": t.string().optional(),
                                }
                            )
                        ).optional(),
                    }
                ).optional(),
                "visitTimeOnSiteDetails": t.struct(
                    {
                        "comparisonType": t.string().optional(),
                        "comparisonValue": t.string().optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "type": t.string().optional(),
                "visitNumPagesDetails": t.struct(
                    {
                        "comparisonType": t.string().optional(),
                        "comparisonValue": t.string().optional(),
                    }
                ).optional(),
                "updated": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "urlDestinationDetails": t.struct(
                    {
                        "caseSensitive": t.boolean().optional(),
                        "steps": t.array(
                            t.struct(
                                {
                                    "url": t.string().optional(),
                                    "name": t.string().optional(),
                                    "number": t.integer().optional(),
                                }
                            )
                        ).optional(),
                        "firstStepRequired": t.boolean().optional(),
                        "matchType": t.string().optional(),
                        "url": t.string().optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "value": t.number().optional(),
                "selfLink": t.string().optional(),
                "internalWebPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementGoalsGet"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/goals/{goalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "goalId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "profileId": t.string().optional(),
                "active": t.boolean().optional(),
                "created": t.string().optional(),
                "eventDetails": t.struct(
                    {
                        "useEventValue": t.boolean().optional(),
                        "eventConditions": t.array(
                            t.struct(
                                {
                                    "type": t.string().optional(),
                                    "comparisonType": t.string().optional(),
                                    "matchType": t.string().optional(),
                                    "comparisonValue": t.string().optional(),
                                    "expression": t.string().optional(),
                                }
                            )
                        ).optional(),
                    }
                ).optional(),
                "visitTimeOnSiteDetails": t.struct(
                    {
                        "comparisonType": t.string().optional(),
                        "comparisonValue": t.string().optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "type": t.string().optional(),
                "visitNumPagesDetails": t.struct(
                    {
                        "comparisonType": t.string().optional(),
                        "comparisonValue": t.string().optional(),
                    }
                ).optional(),
                "updated": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "urlDestinationDetails": t.struct(
                    {
                        "caseSensitive": t.boolean().optional(),
                        "steps": t.array(
                            t.struct(
                                {
                                    "url": t.string().optional(),
                                    "name": t.string().optional(),
                                    "number": t.integer().optional(),
                                }
                            )
                        ).optional(),
                        "firstStepRequired": t.boolean().optional(),
                        "matchType": t.string().optional(),
                        "url": t.string().optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "value": t.number().optional(),
                "selfLink": t.string().optional(),
                "internalWebPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementGoalsList"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/goals/{goalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "goalId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "profileId": t.string().optional(),
                "active": t.boolean().optional(),
                "created": t.string().optional(),
                "eventDetails": t.struct(
                    {
                        "useEventValue": t.boolean().optional(),
                        "eventConditions": t.array(
                            t.struct(
                                {
                                    "type": t.string().optional(),
                                    "comparisonType": t.string().optional(),
                                    "matchType": t.string().optional(),
                                    "comparisonValue": t.string().optional(),
                                    "expression": t.string().optional(),
                                }
                            )
                        ).optional(),
                    }
                ).optional(),
                "visitTimeOnSiteDetails": t.struct(
                    {
                        "comparisonType": t.string().optional(),
                        "comparisonValue": t.string().optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "type": t.string().optional(),
                "visitNumPagesDetails": t.struct(
                    {
                        "comparisonType": t.string().optional(),
                        "comparisonValue": t.string().optional(),
                    }
                ).optional(),
                "updated": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "urlDestinationDetails": t.struct(
                    {
                        "caseSensitive": t.boolean().optional(),
                        "steps": t.array(
                            t.struct(
                                {
                                    "url": t.string().optional(),
                                    "name": t.string().optional(),
                                    "number": t.integer().optional(),
                                }
                            )
                        ).optional(),
                        "firstStepRequired": t.boolean().optional(),
                        "matchType": t.string().optional(),
                        "url": t.string().optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "value": t.number().optional(),
                "selfLink": t.string().optional(),
                "internalWebPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementGoalsPatch"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/goals/{goalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "goalId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "profileId": t.string().optional(),
                "active": t.boolean().optional(),
                "created": t.string().optional(),
                "eventDetails": t.struct(
                    {
                        "useEventValue": t.boolean().optional(),
                        "eventConditions": t.array(
                            t.struct(
                                {
                                    "type": t.string().optional(),
                                    "comparisonType": t.string().optional(),
                                    "matchType": t.string().optional(),
                                    "comparisonValue": t.string().optional(),
                                    "expression": t.string().optional(),
                                }
                            )
                        ).optional(),
                    }
                ).optional(),
                "visitTimeOnSiteDetails": t.struct(
                    {
                        "comparisonType": t.string().optional(),
                        "comparisonValue": t.string().optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "type": t.string().optional(),
                "visitNumPagesDetails": t.struct(
                    {
                        "comparisonType": t.string().optional(),
                        "comparisonValue": t.string().optional(),
                    }
                ).optional(),
                "updated": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "urlDestinationDetails": t.struct(
                    {
                        "caseSensitive": t.boolean().optional(),
                        "steps": t.array(
                            t.struct(
                                {
                                    "url": t.string().optional(),
                                    "name": t.string().optional(),
                                    "number": t.integer().optional(),
                                }
                            )
                        ).optional(),
                        "firstStepRequired": t.boolean().optional(),
                        "matchType": t.string().optional(),
                        "url": t.string().optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "value": t.number().optional(),
                "selfLink": t.string().optional(),
                "internalWebPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementGoalsUpdate"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/goals/{goalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "goalId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "profileId": t.string().optional(),
                "active": t.boolean().optional(),
                "created": t.string().optional(),
                "eventDetails": t.struct(
                    {
                        "useEventValue": t.boolean().optional(),
                        "eventConditions": t.array(
                            t.struct(
                                {
                                    "type": t.string().optional(),
                                    "comparisonType": t.string().optional(),
                                    "matchType": t.string().optional(),
                                    "comparisonValue": t.string().optional(),
                                    "expression": t.string().optional(),
                                }
                            )
                        ).optional(),
                    }
                ).optional(),
                "visitTimeOnSiteDetails": t.struct(
                    {
                        "comparisonType": t.string().optional(),
                        "comparisonValue": t.string().optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "type": t.string().optional(),
                "visitNumPagesDetails": t.struct(
                    {
                        "comparisonType": t.string().optional(),
                        "comparisonValue": t.string().optional(),
                    }
                ).optional(),
                "updated": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "urlDestinationDetails": t.struct(
                    {
                        "caseSensitive": t.boolean().optional(),
                        "steps": t.array(
                            t.struct(
                                {
                                    "url": t.string().optional(),
                                    "name": t.string().optional(),
                                    "number": t.integer().optional(),
                                }
                            )
                        ).optional(),
                        "firstStepRequired": t.boolean().optional(),
                        "matchType": t.string().optional(),
                        "url": t.string().optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "value": t.number().optional(),
                "selfLink": t.string().optional(),
                "internalWebPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementUnsampledReportsGet"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/unsampledReports",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "metrics": t.string().optional(),
                "title": t.string().optional(),
                "start-date": t.string().optional(),
                "filters": t.string().optional(),
                "end-date": t.string().optional(),
                "id": t.string().optional(),
                "segment": t.string().optional(),
                "dimensions": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UnsampledReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementUnsampledReportsList"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/unsampledReports",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "metrics": t.string().optional(),
                "title": t.string().optional(),
                "start-date": t.string().optional(),
                "filters": t.string().optional(),
                "end-date": t.string().optional(),
                "id": t.string().optional(),
                "segment": t.string().optional(),
                "dimensions": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UnsampledReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementUnsampledReportsDelete"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/unsampledReports",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "metrics": t.string().optional(),
                "title": t.string().optional(),
                "start-date": t.string().optional(),
                "filters": t.string().optional(),
                "end-date": t.string().optional(),
                "id": t.string().optional(),
                "segment": t.string().optional(),
                "dimensions": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UnsampledReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementUnsampledReportsInsert"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/unsampledReports",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "metrics": t.string().optional(),
                "title": t.string().optional(),
                "start-date": t.string().optional(),
                "filters": t.string().optional(),
                "end-date": t.string().optional(),
                "id": t.string().optional(),
                "segment": t.string().optional(),
                "dimensions": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UnsampledReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementUploadsList"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDataSources/{customDataSourceId}/deleteUploadData",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "customDataSourceId": t.string().optional(),
                "customDataImportUids": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementUploadsGet"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDataSources/{customDataSourceId}/deleteUploadData",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "customDataSourceId": t.string().optional(),
                "customDataImportUids": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementUploadsUploadData"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDataSources/{customDataSourceId}/deleteUploadData",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "customDataSourceId": t.string().optional(),
                "customDataImportUids": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementUploadsDeleteUploadData"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDataSources/{customDataSourceId}/deleteUploadData",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "customDataSourceId": t.string().optional(),
                "customDataImportUids": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomMetricsList"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customMetrics",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "min_value": t.string().optional(),
                "scope": t.string().optional(),
                "max_value": t.string().optional(),
                "active": t.boolean().optional(),
                "id": t.string().optional(),
                "type": t.string().optional(),
                "parentLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomMetricsUpdate"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customMetrics",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "min_value": t.string().optional(),
                "scope": t.string().optional(),
                "max_value": t.string().optional(),
                "active": t.boolean().optional(),
                "id": t.string().optional(),
                "type": t.string().optional(),
                "parentLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomMetricsGet"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customMetrics",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "min_value": t.string().optional(),
                "scope": t.string().optional(),
                "max_value": t.string().optional(),
                "active": t.boolean().optional(),
                "id": t.string().optional(),
                "type": t.string().optional(),
                "parentLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomMetricsPatch"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customMetrics",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "min_value": t.string().optional(),
                "scope": t.string().optional(),
                "max_value": t.string().optional(),
                "active": t.boolean().optional(),
                "id": t.string().optional(),
                "type": t.string().optional(),
                "parentLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomMetricsInsert"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customMetrics",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "min_value": t.string().optional(),
                "scope": t.string().optional(),
                "max_value": t.string().optional(),
                "active": t.boolean().optional(),
                "id": t.string().optional(),
                "type": t.string().optional(),
                "parentLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementSegmentsList"] = analytics.get(
        "management/segments",
        t.struct(
            {
                "start-index": t.integer().optional(),
                "max-results": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SegmentsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfilesInsert"] = analytics.delete(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfilesUpdate"] = analytics.delete(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfilesPatch"] = analytics.delete(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfilesGet"] = analytics.delete(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfilesList"] = analytics.delete(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfilesDelete"] = analytics.delete(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebpropertyUserLinksInsert"] = analytics.delete(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/entityUserLinks/{linkId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "linkId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebpropertyUserLinksList"] = analytics.delete(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/entityUserLinks/{linkId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "linkId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebpropertyUserLinksUpdate"] = analytics.delete(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/entityUserLinks/{linkId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "linkId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebpropertyUserLinksDelete"] = analytics.delete(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/entityUserLinks/{linkId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "linkId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileFilterLinksUpdate"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/profileFilterLinks",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "rank": t.integer().optional(),
                "id": t.string().optional(),
                "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                "filterRef": t.proxy(renames["FilterRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProfileFilterLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileFilterLinksGet"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/profileFilterLinks",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "rank": t.integer().optional(),
                "id": t.string().optional(),
                "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                "filterRef": t.proxy(renames["FilterRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProfileFilterLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileFilterLinksPatch"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/profileFilterLinks",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "rank": t.integer().optional(),
                "id": t.string().optional(),
                "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                "filterRef": t.proxy(renames["FilterRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProfileFilterLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileFilterLinksList"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/profileFilterLinks",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "rank": t.integer().optional(),
                "id": t.string().optional(),
                "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                "filterRef": t.proxy(renames["FilterRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProfileFilterLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileFilterLinksDelete"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/profileFilterLinks",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "rank": t.integer().optional(),
                "id": t.string().optional(),
                "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                "filterRef": t.proxy(renames["FilterRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProfileFilterLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileFilterLinksInsert"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/profileFilterLinks",
        t.struct(
            {
                "profileId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "rank": t.integer().optional(),
                "id": t.string().optional(),
                "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                "filterRef": t.proxy(renames["FilterRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProfileFilterLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebPropertyAdWordsLinksPatch"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/entityAdWordsLinks/{webPropertyAdWordsLinkId}",
        t.struct(
            {
                "webPropertyAdWordsLinkId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityAdWordsLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebPropertyAdWordsLinksDelete"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/entityAdWordsLinks/{webPropertyAdWordsLinkId}",
        t.struct(
            {
                "webPropertyAdWordsLinkId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityAdWordsLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebPropertyAdWordsLinksList"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/entityAdWordsLinks/{webPropertyAdWordsLinkId}",
        t.struct(
            {
                "webPropertyAdWordsLinkId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityAdWordsLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebPropertyAdWordsLinksInsert"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/entityAdWordsLinks/{webPropertyAdWordsLinkId}",
        t.struct(
            {
                "webPropertyAdWordsLinkId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityAdWordsLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebPropertyAdWordsLinksUpdate"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/entityAdWordsLinks/{webPropertyAdWordsLinkId}",
        t.struct(
            {
                "webPropertyAdWordsLinkId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityAdWordsLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebPropertyAdWordsLinksGet"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/entityAdWordsLinks/{webPropertyAdWordsLinkId}",
        t.struct(
            {
                "webPropertyAdWordsLinkId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityAdWordsLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementRemarketingAudienceUpdate"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/remarketingAudiences/{remarketingAudienceId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "remarketingAudienceId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementRemarketingAudiencePatch"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/remarketingAudiences/{remarketingAudienceId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "remarketingAudienceId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementRemarketingAudienceList"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/remarketingAudiences/{remarketingAudienceId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "remarketingAudienceId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementRemarketingAudienceInsert"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/remarketingAudiences/{remarketingAudienceId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "remarketingAudienceId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementRemarketingAudienceDelete"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/remarketingAudiences/{remarketingAudienceId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "remarketingAudienceId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementRemarketingAudienceGet"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/remarketingAudiences/{remarketingAudienceId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "remarketingAudienceId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementExperimentsGet"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/experiments",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "objectiveMetric": t.string().optional(),
                "description": t.string().optional(),
                "optimizationType": t.string().optional(),
                "reasonExperimentEnded": t.string().optional(),
                "winnerConfidenceLevel": t.number().optional(),
                "endTime": t.string().optional(),
                "selfLink": t.string().optional(),
                "trafficCoverage": t.number().optional(),
                "variations": t.array(
                    t.struct(
                        {
                            "status": t.string().optional(),
                            "weight": t.number().optional(),
                            "name": t.string().optional(),
                            "won": t.boolean().optional(),
                            "url": t.string().optional(),
                        }
                    )
                ).optional(),
                "updated": t.string().optional(),
                "status": t.string().optional(),
                "name": t.string().optional(),
                "minimumExperimentLengthInDays": t.integer().optional(),
                "internalWebPropertyId": t.string().optional(),
                "rewriteVariationUrlsAsOriginal": t.boolean().optional(),
                "snippet": t.string().optional(),
                "editableInGaUi": t.boolean().optional(),
                "equalWeighting": t.boolean().optional(),
                "kind": t.string().optional(),
                "servingFramework": t.string().optional(),
                "winnerFound": t.boolean().optional(),
                "startTime": t.string().optional(),
                "created": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementExperimentsUpdate"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/experiments",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "objectiveMetric": t.string().optional(),
                "description": t.string().optional(),
                "optimizationType": t.string().optional(),
                "reasonExperimentEnded": t.string().optional(),
                "winnerConfidenceLevel": t.number().optional(),
                "endTime": t.string().optional(),
                "selfLink": t.string().optional(),
                "trafficCoverage": t.number().optional(),
                "variations": t.array(
                    t.struct(
                        {
                            "status": t.string().optional(),
                            "weight": t.number().optional(),
                            "name": t.string().optional(),
                            "won": t.boolean().optional(),
                            "url": t.string().optional(),
                        }
                    )
                ).optional(),
                "updated": t.string().optional(),
                "status": t.string().optional(),
                "name": t.string().optional(),
                "minimumExperimentLengthInDays": t.integer().optional(),
                "internalWebPropertyId": t.string().optional(),
                "rewriteVariationUrlsAsOriginal": t.boolean().optional(),
                "snippet": t.string().optional(),
                "editableInGaUi": t.boolean().optional(),
                "equalWeighting": t.boolean().optional(),
                "kind": t.string().optional(),
                "servingFramework": t.string().optional(),
                "winnerFound": t.boolean().optional(),
                "startTime": t.string().optional(),
                "created": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementExperimentsPatch"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/experiments",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "objectiveMetric": t.string().optional(),
                "description": t.string().optional(),
                "optimizationType": t.string().optional(),
                "reasonExperimentEnded": t.string().optional(),
                "winnerConfidenceLevel": t.number().optional(),
                "endTime": t.string().optional(),
                "selfLink": t.string().optional(),
                "trafficCoverage": t.number().optional(),
                "variations": t.array(
                    t.struct(
                        {
                            "status": t.string().optional(),
                            "weight": t.number().optional(),
                            "name": t.string().optional(),
                            "won": t.boolean().optional(),
                            "url": t.string().optional(),
                        }
                    )
                ).optional(),
                "updated": t.string().optional(),
                "status": t.string().optional(),
                "name": t.string().optional(),
                "minimumExperimentLengthInDays": t.integer().optional(),
                "internalWebPropertyId": t.string().optional(),
                "rewriteVariationUrlsAsOriginal": t.boolean().optional(),
                "snippet": t.string().optional(),
                "editableInGaUi": t.boolean().optional(),
                "equalWeighting": t.boolean().optional(),
                "kind": t.string().optional(),
                "servingFramework": t.string().optional(),
                "winnerFound": t.boolean().optional(),
                "startTime": t.string().optional(),
                "created": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementExperimentsList"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/experiments",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "objectiveMetric": t.string().optional(),
                "description": t.string().optional(),
                "optimizationType": t.string().optional(),
                "reasonExperimentEnded": t.string().optional(),
                "winnerConfidenceLevel": t.number().optional(),
                "endTime": t.string().optional(),
                "selfLink": t.string().optional(),
                "trafficCoverage": t.number().optional(),
                "variations": t.array(
                    t.struct(
                        {
                            "status": t.string().optional(),
                            "weight": t.number().optional(),
                            "name": t.string().optional(),
                            "won": t.boolean().optional(),
                            "url": t.string().optional(),
                        }
                    )
                ).optional(),
                "updated": t.string().optional(),
                "status": t.string().optional(),
                "name": t.string().optional(),
                "minimumExperimentLengthInDays": t.integer().optional(),
                "internalWebPropertyId": t.string().optional(),
                "rewriteVariationUrlsAsOriginal": t.boolean().optional(),
                "snippet": t.string().optional(),
                "editableInGaUi": t.boolean().optional(),
                "equalWeighting": t.boolean().optional(),
                "kind": t.string().optional(),
                "servingFramework": t.string().optional(),
                "winnerFound": t.boolean().optional(),
                "startTime": t.string().optional(),
                "created": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementExperimentsDelete"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/experiments",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "objectiveMetric": t.string().optional(),
                "description": t.string().optional(),
                "optimizationType": t.string().optional(),
                "reasonExperimentEnded": t.string().optional(),
                "winnerConfidenceLevel": t.number().optional(),
                "endTime": t.string().optional(),
                "selfLink": t.string().optional(),
                "trafficCoverage": t.number().optional(),
                "variations": t.array(
                    t.struct(
                        {
                            "status": t.string().optional(),
                            "weight": t.number().optional(),
                            "name": t.string().optional(),
                            "won": t.boolean().optional(),
                            "url": t.string().optional(),
                        }
                    )
                ).optional(),
                "updated": t.string().optional(),
                "status": t.string().optional(),
                "name": t.string().optional(),
                "minimumExperimentLengthInDays": t.integer().optional(),
                "internalWebPropertyId": t.string().optional(),
                "rewriteVariationUrlsAsOriginal": t.boolean().optional(),
                "snippet": t.string().optional(),
                "editableInGaUi": t.boolean().optional(),
                "equalWeighting": t.boolean().optional(),
                "kind": t.string().optional(),
                "servingFramework": t.string().optional(),
                "winnerFound": t.boolean().optional(),
                "startTime": t.string().optional(),
                "created": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementExperimentsInsert"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/experiments",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "objectiveMetric": t.string().optional(),
                "description": t.string().optional(),
                "optimizationType": t.string().optional(),
                "reasonExperimentEnded": t.string().optional(),
                "winnerConfidenceLevel": t.number().optional(),
                "endTime": t.string().optional(),
                "selfLink": t.string().optional(),
                "trafficCoverage": t.number().optional(),
                "variations": t.array(
                    t.struct(
                        {
                            "status": t.string().optional(),
                            "weight": t.number().optional(),
                            "name": t.string().optional(),
                            "won": t.boolean().optional(),
                            "url": t.string().optional(),
                        }
                    )
                ).optional(),
                "updated": t.string().optional(),
                "status": t.string().optional(),
                "name": t.string().optional(),
                "minimumExperimentLengthInDays": t.integer().optional(),
                "internalWebPropertyId": t.string().optional(),
                "rewriteVariationUrlsAsOriginal": t.boolean().optional(),
                "snippet": t.string().optional(),
                "editableInGaUi": t.boolean().optional(),
                "equalWeighting": t.boolean().optional(),
                "kind": t.string().optional(),
                "servingFramework": t.string().optional(),
                "winnerFound": t.boolean().optional(),
                "startTime": t.string().optional(),
                "created": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebpropertiesUpdate"] = analytics.patch(
        "management/accounts/{accountId}/webproperties/{webPropertyId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "dataRetentionResetOnNewActivity": t.boolean().optional(),
                "dataRetentionTtl": t.string().optional(),
                "name": t.string().optional(),
                "websiteUrl": t.string().optional(),
                "childLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "starred": t.boolean().optional(),
                "industryVertical": t.string().optional(),
                "id": t.string().optional(),
                "defaultProfileId": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "permissions": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebpropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebpropertiesGet"] = analytics.patch(
        "management/accounts/{accountId}/webproperties/{webPropertyId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "dataRetentionResetOnNewActivity": t.boolean().optional(),
                "dataRetentionTtl": t.string().optional(),
                "name": t.string().optional(),
                "websiteUrl": t.string().optional(),
                "childLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "starred": t.boolean().optional(),
                "industryVertical": t.string().optional(),
                "id": t.string().optional(),
                "defaultProfileId": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "permissions": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebpropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebpropertiesInsert"] = analytics.patch(
        "management/accounts/{accountId}/webproperties/{webPropertyId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "dataRetentionResetOnNewActivity": t.boolean().optional(),
                "dataRetentionTtl": t.string().optional(),
                "name": t.string().optional(),
                "websiteUrl": t.string().optional(),
                "childLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "starred": t.boolean().optional(),
                "industryVertical": t.string().optional(),
                "id": t.string().optional(),
                "defaultProfileId": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "permissions": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebpropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebpropertiesList"] = analytics.patch(
        "management/accounts/{accountId}/webproperties/{webPropertyId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "dataRetentionResetOnNewActivity": t.boolean().optional(),
                "dataRetentionTtl": t.string().optional(),
                "name": t.string().optional(),
                "websiteUrl": t.string().optional(),
                "childLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "starred": t.boolean().optional(),
                "industryVertical": t.string().optional(),
                "id": t.string().optional(),
                "defaultProfileId": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "permissions": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebpropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebpropertiesPatch"] = analytics.patch(
        "management/accounts/{accountId}/webproperties/{webPropertyId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "dataRetentionResetOnNewActivity": t.boolean().optional(),
                "dataRetentionTtl": t.string().optional(),
                "name": t.string().optional(),
                "websiteUrl": t.string().optional(),
                "childLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "starred": t.boolean().optional(),
                "industryVertical": t.string().optional(),
                "id": t.string().optional(),
                "defaultProfileId": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "permissions": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebpropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomDimensionsUpdate"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDimensions",
        t.struct(
            {
                "max-results": t.integer().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomDimensionsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomDimensionsGet"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDimensions",
        t.struct(
            {
                "max-results": t.integer().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomDimensionsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomDimensionsPatch"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDimensions",
        t.struct(
            {
                "max-results": t.integer().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomDimensionsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomDimensionsInsert"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDimensions",
        t.struct(
            {
                "max-results": t.integer().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomDimensionsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomDimensionsList"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDimensions",
        t.struct(
            {
                "max-results": t.integer().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomDimensionsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="analytics",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
