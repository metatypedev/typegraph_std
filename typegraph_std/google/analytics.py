from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_analytics():
    analytics = HTTPRuntime("https://analytics.googleapis.com/")

    renames = {
        "ErrorResponse": "_analytics_1_ErrorResponse",
        "RealtimeDataIn": "_analytics_2_RealtimeDataIn",
        "RealtimeDataOut": "_analytics_3_RealtimeDataOut",
        "ColumnIn": "_analytics_4_ColumnIn",
        "ColumnOut": "_analytics_5_ColumnOut",
        "McfDataIn": "_analytics_6_McfDataIn",
        "McfDataOut": "_analytics_7_McfDataOut",
        "ProfilesIn": "_analytics_8_ProfilesIn",
        "ProfilesOut": "_analytics_9_ProfilesOut",
        "GoalsIn": "_analytics_10_GoalsIn",
        "GoalsOut": "_analytics_11_GoalsOut",
        "EntityAdWordsLinkIn": "_analytics_12_EntityAdWordsLinkIn",
        "EntityAdWordsLinkOut": "_analytics_13_EntityAdWordsLinkOut",
        "GaDataIn": "_analytics_14_GaDataIn",
        "GaDataOut": "_analytics_15_GaDataOut",
        "GoalIn": "_analytics_16_GoalIn",
        "GoalOut": "_analytics_17_GoalOut",
        "AccountRefIn": "_analytics_18_AccountRefIn",
        "AccountRefOut": "_analytics_19_AccountRefOut",
        "RemarketingAudienceIn": "_analytics_20_RemarketingAudienceIn",
        "RemarketingAudienceOut": "_analytics_21_RemarketingAudienceOut",
        "AdWordsAccountIn": "_analytics_22_AdWordsAccountIn",
        "AdWordsAccountOut": "_analytics_23_AdWordsAccountOut",
        "CustomDataSourceIn": "_analytics_24_CustomDataSourceIn",
        "CustomDataSourceOut": "_analytics_25_CustomDataSourceOut",
        "ColumnsIn": "_analytics_26_ColumnsIn",
        "ColumnsOut": "_analytics_27_ColumnsOut",
        "SegmentIn": "_analytics_28_SegmentIn",
        "SegmentOut": "_analytics_29_SegmentOut",
        "SegmentsIn": "_analytics_30_SegmentsIn",
        "SegmentsOut": "_analytics_31_SegmentsOut",
        "AccountTicketIn": "_analytics_32_AccountTicketIn",
        "AccountTicketOut": "_analytics_33_AccountTicketOut",
        "FiltersIn": "_analytics_34_FiltersIn",
        "FiltersOut": "_analytics_35_FiltersOut",
        "EntityUserLinkIn": "_analytics_36_EntityUserLinkIn",
        "EntityUserLinkOut": "_analytics_37_EntityUserLinkOut",
        "UploadIn": "_analytics_38_UploadIn",
        "UploadOut": "_analytics_39_UploadOut",
        "AccountsIn": "_analytics_40_AccountsIn",
        "AccountsOut": "_analytics_41_AccountsOut",
        "ExperimentIn": "_analytics_42_ExperimentIn",
        "ExperimentOut": "_analytics_43_ExperimentOut",
        "EntityUserLinksIn": "_analytics_44_EntityUserLinksIn",
        "EntityUserLinksOut": "_analytics_45_EntityUserLinksOut",
        "FilterRefIn": "_analytics_46_FilterRefIn",
        "FilterRefOut": "_analytics_47_FilterRefOut",
        "WebpropertiesIn": "_analytics_48_WebpropertiesIn",
        "WebpropertiesOut": "_analytics_49_WebpropertiesOut",
        "RemarketingAudiencesIn": "_analytics_50_RemarketingAudiencesIn",
        "RemarketingAudiencesOut": "_analytics_51_RemarketingAudiencesOut",
        "ProfileSummaryIn": "_analytics_52_ProfileSummaryIn",
        "ProfileSummaryOut": "_analytics_53_ProfileSummaryOut",
        "HashClientIdRequestIn": "_analytics_54_HashClientIdRequestIn",
        "HashClientIdRequestOut": "_analytics_55_HashClientIdRequestOut",
        "FilterExpressionIn": "_analytics_56_FilterExpressionIn",
        "FilterExpressionOut": "_analytics_57_FilterExpressionOut",
        "AccountIn": "_analytics_58_AccountIn",
        "AccountOut": "_analytics_59_AccountOut",
        "UserDeletionRequestIn": "_analytics_60_UserDeletionRequestIn",
        "UserDeletionRequestOut": "_analytics_61_UserDeletionRequestOut",
        "EntityAdWordsLinksIn": "_analytics_62_EntityAdWordsLinksIn",
        "EntityAdWordsLinksOut": "_analytics_63_EntityAdWordsLinksOut",
        "AnalyticsDataimportDeleteUploadDataRequestIn": "_analytics_64_AnalyticsDataimportDeleteUploadDataRequestIn",
        "AnalyticsDataimportDeleteUploadDataRequestOut": "_analytics_65_AnalyticsDataimportDeleteUploadDataRequestOut",
        "AccountSummaryIn": "_analytics_66_AccountSummaryIn",
        "AccountSummaryOut": "_analytics_67_AccountSummaryOut",
        "HashClientIdResponseIn": "_analytics_68_HashClientIdResponseIn",
        "HashClientIdResponseOut": "_analytics_69_HashClientIdResponseOut",
        "WebPropertySummaryIn": "_analytics_70_WebPropertySummaryIn",
        "WebPropertySummaryOut": "_analytics_71_WebPropertySummaryOut",
        "UnsampledReportsIn": "_analytics_72_UnsampledReportsIn",
        "UnsampledReportsOut": "_analytics_73_UnsampledReportsOut",
        "ExperimentsIn": "_analytics_74_ExperimentsIn",
        "ExperimentsOut": "_analytics_75_ExperimentsOut",
        "AccountSummariesIn": "_analytics_76_AccountSummariesIn",
        "AccountSummariesOut": "_analytics_77_AccountSummariesOut",
        "ProfileFilterLinkIn": "_analytics_78_ProfileFilterLinkIn",
        "ProfileFilterLinkOut": "_analytics_79_ProfileFilterLinkOut",
        "CustomDimensionsIn": "_analytics_80_CustomDimensionsIn",
        "CustomDimensionsOut": "_analytics_81_CustomDimensionsOut",
        "LinkedForeignAccountIn": "_analytics_82_LinkedForeignAccountIn",
        "LinkedForeignAccountOut": "_analytics_83_LinkedForeignAccountOut",
        "ProfileFilterLinksIn": "_analytics_84_ProfileFilterLinksIn",
        "ProfileFilterLinksOut": "_analytics_85_ProfileFilterLinksOut",
        "AccountTreeRequestIn": "_analytics_86_AccountTreeRequestIn",
        "AccountTreeRequestOut": "_analytics_87_AccountTreeRequestOut",
        "FilterIn": "_analytics_88_FilterIn",
        "FilterOut": "_analytics_89_FilterOut",
        "CustomMetricIn": "_analytics_90_CustomMetricIn",
        "CustomMetricOut": "_analytics_91_CustomMetricOut",
        "CustomDataSourcesIn": "_analytics_92_CustomDataSourcesIn",
        "CustomDataSourcesOut": "_analytics_93_CustomDataSourcesOut",
        "WebPropertyRefIn": "_analytics_94_WebPropertyRefIn",
        "WebPropertyRefOut": "_analytics_95_WebPropertyRefOut",
        "ProfileRefIn": "_analytics_96_ProfileRefIn",
        "ProfileRefOut": "_analytics_97_ProfileRefOut",
        "UserRefIn": "_analytics_98_UserRefIn",
        "UserRefOut": "_analytics_99_UserRefOut",
        "UnsampledReportIn": "_analytics_100_UnsampledReportIn",
        "UnsampledReportOut": "_analytics_101_UnsampledReportOut",
        "WebpropertyIn": "_analytics_102_WebpropertyIn",
        "WebpropertyOut": "_analytics_103_WebpropertyOut",
        "IncludeConditionsIn": "_analytics_104_IncludeConditionsIn",
        "IncludeConditionsOut": "_analytics_105_IncludeConditionsOut",
        "ProfileIn": "_analytics_106_ProfileIn",
        "ProfileOut": "_analytics_107_ProfileOut",
        "UploadsIn": "_analytics_108_UploadsIn",
        "UploadsOut": "_analytics_109_UploadsOut",
        "CustomDimensionIn": "_analytics_110_CustomDimensionIn",
        "CustomDimensionOut": "_analytics_111_CustomDimensionOut",
        "AccountTreeResponseIn": "_analytics_112_AccountTreeResponseIn",
        "AccountTreeResponseOut": "_analytics_113_AccountTreeResponseOut",
        "CustomMetricsIn": "_analytics_114_CustomMetricsIn",
        "CustomMetricsOut": "_analytics_115_CustomMetricsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RealtimeDataIn"] = t.struct(
        {
            "rows": t.array(t.array(t.string())).optional(),
            "totalsForAllResults": t.struct({"_": t.string().optional()}).optional(),
            "selfLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "columnHeaders": t.array(
                t.struct(
                    {
                        "columnType": t.string().optional(),
                        "name": t.string().optional(),
                        "dataType": t.string().optional(),
                    }
                )
            ).optional(),
            "kind": t.string().optional(),
            "query": t.struct(
                {
                    "filters": t.string().optional(),
                    "sort": t.array(t.string()).optional(),
                    "dimensions": t.string().optional(),
                    "max-results": t.integer().optional(),
                    "ids": t.string().optional(),
                    "metrics": t.array(t.string()).optional(),
                }
            ).optional(),
            "profileInfo": t.struct(
                {
                    "webPropertyId": t.string().optional(),
                    "tableId": t.string().optional(),
                    "accountId": t.string().optional(),
                    "internalWebPropertyId": t.string().optional(),
                    "profileName": t.string().optional(),
                    "profileId": t.string().optional(),
                }
            ).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["RealtimeDataIn"])
    types["RealtimeDataOut"] = t.struct(
        {
            "rows": t.array(t.array(t.string())).optional(),
            "totalsForAllResults": t.struct({"_": t.string().optional()}).optional(),
            "selfLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "columnHeaders": t.array(
                t.struct(
                    {
                        "columnType": t.string().optional(),
                        "name": t.string().optional(),
                        "dataType": t.string().optional(),
                    }
                )
            ).optional(),
            "kind": t.string().optional(),
            "query": t.struct(
                {
                    "filters": t.string().optional(),
                    "sort": t.array(t.string()).optional(),
                    "dimensions": t.string().optional(),
                    "max-results": t.integer().optional(),
                    "ids": t.string().optional(),
                    "metrics": t.array(t.string()).optional(),
                }
            ).optional(),
            "profileInfo": t.struct(
                {
                    "webPropertyId": t.string().optional(),
                    "tableId": t.string().optional(),
                    "accountId": t.string().optional(),
                    "internalWebPropertyId": t.string().optional(),
                    "profileName": t.string().optional(),
                    "profileId": t.string().optional(),
                }
            ).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RealtimeDataOut"])
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
    types["McfDataIn"] = t.struct(
        {
            "query": t.struct(
                {
                    "max-results": t.integer().optional(),
                    "filters": t.string().optional(),
                    "dimensions": t.string().optional(),
                    "end-date": t.string().optional(),
                    "sort": t.array(t.string()).optional(),
                    "samplingLevel": t.string().optional(),
                    "ids": t.string().optional(),
                    "metrics": t.array(t.string()).optional(),
                    "segment": t.string().optional(),
                    "start-date": t.string().optional(),
                    "start-index": t.integer().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "columnHeaders": t.array(
                t.struct(
                    {
                        "dataType": t.string().optional(),
                        "columnType": t.string().optional(),
                        "name": t.string().optional(),
                    }
                )
            ).optional(),
            "sampleSpace": t.string().optional(),
            "sampleSize": t.string().optional(),
            "totalResults": t.integer().optional(),
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
            "previousLink": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "totalsForAllResults": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "profileInfo": t.struct(
                {
                    "tableId": t.string().optional(),
                    "profileId": t.string().optional(),
                    "webPropertyId": t.string().optional(),
                    "accountId": t.string().optional(),
                    "profileName": t.string().optional(),
                    "internalWebPropertyId": t.string().optional(),
                }
            ).optional(),
            "containsSampledData": t.boolean().optional(),
            "selfLink": t.string().optional(),
            "nextLink": t.string().optional(),
        }
    ).named(renames["McfDataIn"])
    types["McfDataOut"] = t.struct(
        {
            "query": t.struct(
                {
                    "max-results": t.integer().optional(),
                    "filters": t.string().optional(),
                    "dimensions": t.string().optional(),
                    "end-date": t.string().optional(),
                    "sort": t.array(t.string()).optional(),
                    "samplingLevel": t.string().optional(),
                    "ids": t.string().optional(),
                    "metrics": t.array(t.string()).optional(),
                    "segment": t.string().optional(),
                    "start-date": t.string().optional(),
                    "start-index": t.integer().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "columnHeaders": t.array(
                t.struct(
                    {
                        "dataType": t.string().optional(),
                        "columnType": t.string().optional(),
                        "name": t.string().optional(),
                    }
                )
            ).optional(),
            "sampleSpace": t.string().optional(),
            "sampleSize": t.string().optional(),
            "totalResults": t.integer().optional(),
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
            "previousLink": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "totalsForAllResults": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "profileInfo": t.struct(
                {
                    "tableId": t.string().optional(),
                    "profileId": t.string().optional(),
                    "webPropertyId": t.string().optional(),
                    "accountId": t.string().optional(),
                    "profileName": t.string().optional(),
                    "internalWebPropertyId": t.string().optional(),
                }
            ).optional(),
            "containsSampledData": t.boolean().optional(),
            "selfLink": t.string().optional(),
            "nextLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["McfDataOut"])
    types["ProfilesIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "totalResults": t.integer().optional(),
            "username": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "items": t.array(t.proxy(renames["ProfileIn"])).optional(),
            "previousLink": t.string().optional(),
            "nextLink": t.string().optional(),
        }
    ).named(renames["ProfilesIn"])
    types["ProfilesOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "totalResults": t.integer().optional(),
            "username": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "items": t.array(t.proxy(renames["ProfileOut"])).optional(),
            "previousLink": t.string().optional(),
            "nextLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfilesOut"])
    types["GoalsIn"] = t.struct(
        {
            "previousLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "items": t.array(t.proxy(renames["GoalIn"])).optional(),
            "startIndex": t.integer().optional(),
            "kind": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "nextLink": t.string().optional(),
            "username": t.string().optional(),
        }
    ).named(renames["GoalsIn"])
    types["GoalsOut"] = t.struct(
        {
            "previousLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "items": t.array(t.proxy(renames["GoalOut"])).optional(),
            "startIndex": t.integer().optional(),
            "kind": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "nextLink": t.string().optional(),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoalsOut"])
    types["EntityAdWordsLinkIn"] = t.struct(
        {
            "name": t.string().optional(),
            "adWordsAccounts": t.array(t.proxy(renames["AdWordsAccountIn"])).optional(),
            "profileIds": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "entity": t.struct(
                {"webPropertyRef": t.proxy(renames["WebPropertyRefIn"])}
            ).optional(),
            "id": t.string().optional(),
            "selfLink": t.string().optional(),
        }
    ).named(renames["EntityAdWordsLinkIn"])
    types["EntityAdWordsLinkOut"] = t.struct(
        {
            "name": t.string().optional(),
            "adWordsAccounts": t.array(
                t.proxy(renames["AdWordsAccountOut"])
            ).optional(),
            "profileIds": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "entity": t.struct(
                {"webPropertyRef": t.proxy(renames["WebPropertyRefOut"])}
            ).optional(),
            "id": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityAdWordsLinkOut"])
    types["GaDataIn"] = t.struct(
        {
            "profileInfo": t.struct(
                {
                    "profileName": t.string().optional(),
                    "webPropertyId": t.string().optional(),
                    "tableId": t.string().optional(),
                    "internalWebPropertyId": t.string().optional(),
                    "profileId": t.string().optional(),
                    "accountId": t.string().optional(),
                }
            ).optional(),
            "rows": t.array(t.array(t.string())).optional(),
            "columnHeaders": t.array(
                t.struct(
                    {
                        "columnType": t.string().optional(),
                        "name": t.string().optional(),
                        "dataType": t.string().optional(),
                    }
                )
            ).optional(),
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
            "containsSampledData": t.boolean().optional(),
            "totalResults": t.integer().optional(),
            "sampleSpace": t.string().optional(),
            "totalsForAllResults": t.struct({"_": t.string().optional()}).optional(),
            "dataLastRefreshed": t.string().optional(),
            "selfLink": t.string().optional(),
            "sampleSize": t.string().optional(),
            "kind": t.string().optional(),
            "query": t.struct(
                {
                    "ids": t.string().optional(),
                    "samplingLevel": t.string().optional(),
                    "end-date": t.string().optional(),
                    "max-results": t.integer().optional(),
                    "sort": t.array(t.string()).optional(),
                    "filters": t.string().optional(),
                    "start-index": t.integer().optional(),
                    "metrics": t.array(t.string()).optional(),
                    "dimensions": t.string().optional(),
                    "segment": t.string().optional(),
                    "start-date": t.string().optional(),
                }
            ).optional(),
            "itemsPerPage": t.integer().optional(),
            "id": t.string().optional(),
            "previousLink": t.string().optional(),
            "nextLink": t.string().optional(),
        }
    ).named(renames["GaDataIn"])
    types["GaDataOut"] = t.struct(
        {
            "profileInfo": t.struct(
                {
                    "profileName": t.string().optional(),
                    "webPropertyId": t.string().optional(),
                    "tableId": t.string().optional(),
                    "internalWebPropertyId": t.string().optional(),
                    "profileId": t.string().optional(),
                    "accountId": t.string().optional(),
                }
            ).optional(),
            "rows": t.array(t.array(t.string())).optional(),
            "columnHeaders": t.array(
                t.struct(
                    {
                        "columnType": t.string().optional(),
                        "name": t.string().optional(),
                        "dataType": t.string().optional(),
                    }
                )
            ).optional(),
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
            "containsSampledData": t.boolean().optional(),
            "totalResults": t.integer().optional(),
            "sampleSpace": t.string().optional(),
            "totalsForAllResults": t.struct({"_": t.string().optional()}).optional(),
            "dataLastRefreshed": t.string().optional(),
            "selfLink": t.string().optional(),
            "sampleSize": t.string().optional(),
            "kind": t.string().optional(),
            "query": t.struct(
                {
                    "ids": t.string().optional(),
                    "samplingLevel": t.string().optional(),
                    "end-date": t.string().optional(),
                    "max-results": t.integer().optional(),
                    "sort": t.array(t.string()).optional(),
                    "filters": t.string().optional(),
                    "start-index": t.integer().optional(),
                    "metrics": t.array(t.string()).optional(),
                    "dimensions": t.string().optional(),
                    "segment": t.string().optional(),
                    "start-date": t.string().optional(),
                }
            ).optional(),
            "itemsPerPage": t.integer().optional(),
            "id": t.string().optional(),
            "previousLink": t.string().optional(),
            "nextLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GaDataOut"])
    types["GoalIn"] = t.struct(
        {
            "updated": t.string().optional(),
            "type": t.string().optional(),
            "urlDestinationDetails": t.struct(
                {
                    "firstStepRequired": t.boolean().optional(),
                    "matchType": t.string().optional(),
                    "url": t.string().optional(),
                    "caseSensitive": t.boolean().optional(),
                    "steps": t.array(
                        t.struct(
                            {
                                "name": t.string().optional(),
                                "url": t.string().optional(),
                                "number": t.integer().optional(),
                            }
                        )
                    ).optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "profileId": t.string().optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "created": t.string().optional(),
            "parentLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "visitTimeOnSiteDetails": t.struct(
                {
                    "comparisonType": t.string().optional(),
                    "comparisonValue": t.string().optional(),
                }
            ).optional(),
            "active": t.boolean().optional(),
            "internalWebPropertyId": t.string().optional(),
            "eventDetails": t.struct(
                {
                    "eventConditions": t.array(
                        t.struct(
                            {
                                "matchType": t.string().optional(),
                                "comparisonType": t.string().optional(),
                                "type": t.string().optional(),
                                "comparisonValue": t.string().optional(),
                                "expression": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "useEventValue": t.boolean().optional(),
                }
            ).optional(),
            "value": t.number().optional(),
            "visitNumPagesDetails": t.struct(
                {
                    "comparisonValue": t.string().optional(),
                    "comparisonType": t.string().optional(),
                }
            ).optional(),
            "webPropertyId": t.string().optional(),
            "selfLink": t.string().optional(),
        }
    ).named(renames["GoalIn"])
    types["GoalOut"] = t.struct(
        {
            "updated": t.string().optional(),
            "type": t.string().optional(),
            "urlDestinationDetails": t.struct(
                {
                    "firstStepRequired": t.boolean().optional(),
                    "matchType": t.string().optional(),
                    "url": t.string().optional(),
                    "caseSensitive": t.boolean().optional(),
                    "steps": t.array(
                        t.struct(
                            {
                                "name": t.string().optional(),
                                "url": t.string().optional(),
                                "number": t.integer().optional(),
                            }
                        )
                    ).optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "profileId": t.string().optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "created": t.string().optional(),
            "parentLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "visitTimeOnSiteDetails": t.struct(
                {
                    "comparisonType": t.string().optional(),
                    "comparisonValue": t.string().optional(),
                }
            ).optional(),
            "active": t.boolean().optional(),
            "internalWebPropertyId": t.string().optional(),
            "eventDetails": t.struct(
                {
                    "eventConditions": t.array(
                        t.struct(
                            {
                                "matchType": t.string().optional(),
                                "comparisonType": t.string().optional(),
                                "type": t.string().optional(),
                                "comparisonValue": t.string().optional(),
                                "expression": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "useEventValue": t.boolean().optional(),
                }
            ).optional(),
            "value": t.number().optional(),
            "visitNumPagesDetails": t.struct(
                {
                    "comparisonValue": t.string().optional(),
                    "comparisonType": t.string().optional(),
                }
            ).optional(),
            "webPropertyId": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoalOut"])
    types["AccountRefIn"] = t.struct(
        {
            "href": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["AccountRefIn"])
    types["AccountRefOut"] = t.struct(
        {
            "href": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountRefOut"])
    types["RemarketingAudienceIn"] = t.struct(
        {
            "audienceType": t.string().optional(),
            "accountId": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "audienceDefinition": t.struct(
                {
                    "includeConditions": t.proxy(
                        renames["IncludeConditionsIn"]
                    ).optional()
                }
            ).optional(),
            "linkedAdAccounts": t.array(
                t.proxy(renames["LinkedForeignAccountIn"])
            ).optional(),
            "stateBasedAudienceDefinition": t.struct(
                {
                    "includeConditions": t.proxy(
                        renames["IncludeConditionsIn"]
                    ).optional(),
                    "excludeConditions": t.struct(
                        {
                            "segment": t.string().optional(),
                            "exclusionDuration": t.string().optional(),
                        }
                    ).optional(),
                }
            ).optional(),
            "linkedViews": t.array(t.string()).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["RemarketingAudienceIn"])
    types["RemarketingAudienceOut"] = t.struct(
        {
            "audienceType": t.string().optional(),
            "accountId": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "description": t.string().optional(),
            "kind": t.string().optional(),
            "updated": t.string().optional(),
            "created": t.string().optional(),
            "id": t.string().optional(),
            "audienceDefinition": t.struct(
                {
                    "includeConditions": t.proxy(
                        renames["IncludeConditionsOut"]
                    ).optional()
                }
            ).optional(),
            "linkedAdAccounts": t.array(
                t.proxy(renames["LinkedForeignAccountOut"])
            ).optional(),
            "internalWebPropertyId": t.string().optional(),
            "stateBasedAudienceDefinition": t.struct(
                {
                    "includeConditions": t.proxy(
                        renames["IncludeConditionsOut"]
                    ).optional(),
                    "excludeConditions": t.struct(
                        {
                            "segment": t.string().optional(),
                            "exclusionDuration": t.string().optional(),
                        }
                    ).optional(),
                }
            ).optional(),
            "linkedViews": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemarketingAudienceOut"])
    types["AdWordsAccountIn"] = t.struct(
        {
            "autoTaggingEnabled": t.boolean().optional(),
            "kind": t.string().optional(),
            "customerId": t.string().optional(),
        }
    ).named(renames["AdWordsAccountIn"])
    types["AdWordsAccountOut"] = t.struct(
        {
            "autoTaggingEnabled": t.boolean().optional(),
            "kind": t.string().optional(),
            "customerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdWordsAccountOut"])
    types["CustomDataSourceIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "childLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ),
            "type": t.string().optional(),
            "parentLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "description": t.string().optional(),
            "selfLink": t.string().optional(),
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "updated": t.string().optional(),
            "created": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "id": t.string().optional(),
            "schema": t.array(t.string()).optional(),
            "uploadType": t.string().optional(),
            "profilesLinked": t.array(t.string()).optional(),
            "importBehavior": t.string(),
        }
    ).named(renames["CustomDataSourceIn"])
    types["CustomDataSourceOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "childLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ),
            "type": t.string().optional(),
            "parentLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "description": t.string().optional(),
            "selfLink": t.string().optional(),
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "updated": t.string().optional(),
            "created": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "id": t.string().optional(),
            "schema": t.array(t.string()).optional(),
            "uploadType": t.string().optional(),
            "profilesLinked": t.array(t.string()).optional(),
            "importBehavior": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomDataSourceOut"])
    types["ColumnsIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ColumnIn"])).optional(),
            "etag": t.string().optional(),
            "attributeNames": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "totalResults": t.integer().optional(),
        }
    ).named(renames["ColumnsIn"])
    types["ColumnsOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ColumnOut"])).optional(),
            "etag": t.string().optional(),
            "attributeNames": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "totalResults": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnsOut"])
    types["SegmentIn"] = t.struct(
        {
            "definition": t.string().optional(),
            "name": t.string().optional(),
            "created": t.string().optional(),
            "updated": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "type": t.string().optional(),
            "selfLink": t.string().optional(),
            "segmentId": t.string().optional(),
        }
    ).named(renames["SegmentIn"])
    types["SegmentOut"] = t.struct(
        {
            "definition": t.string().optional(),
            "name": t.string().optional(),
            "created": t.string().optional(),
            "updated": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "type": t.string().optional(),
            "selfLink": t.string().optional(),
            "segmentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentOut"])
    types["SegmentsIn"] = t.struct(
        {
            "itemsPerPage": t.integer().optional(),
            "kind": t.string().optional(),
            "totalResults": t.integer().optional(),
            "previousLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "nextLink": t.string().optional(),
            "username": t.string().optional(),
            "items": t.array(t.proxy(renames["SegmentIn"])).optional(),
        }
    ).named(renames["SegmentsIn"])
    types["SegmentsOut"] = t.struct(
        {
            "itemsPerPage": t.integer().optional(),
            "kind": t.string().optional(),
            "totalResults": t.integer().optional(),
            "previousLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "nextLink": t.string().optional(),
            "username": t.string().optional(),
            "items": t.array(t.proxy(renames["SegmentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentsOut"])
    types["AccountTicketIn"] = t.struct(
        {
            "id": t.string().optional(),
            "profile": t.proxy(renames["ProfileIn"]).optional(),
            "redirectUri": t.string().optional(),
            "account": t.proxy(renames["AccountIn"]).optional(),
            "webproperty": t.proxy(renames["WebpropertyIn"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AccountTicketIn"])
    types["AccountTicketOut"] = t.struct(
        {
            "id": t.string().optional(),
            "profile": t.proxy(renames["ProfileOut"]).optional(),
            "redirectUri": t.string().optional(),
            "account": t.proxy(renames["AccountOut"]).optional(),
            "webproperty": t.proxy(renames["WebpropertyOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountTicketOut"])
    types["FiltersIn"] = t.struct(
        {
            "itemsPerPage": t.integer().optional(),
            "username": t.string().optional(),
            "totalResults": t.integer().optional(),
            "kind": t.string().optional(),
            "startIndex": t.integer().optional(),
            "items": t.array(t.proxy(renames["FilterIn"])).optional(),
            "previousLink": t.string().optional(),
            "nextLink": t.string().optional(),
        }
    ).named(renames["FiltersIn"])
    types["FiltersOut"] = t.struct(
        {
            "itemsPerPage": t.integer().optional(),
            "username": t.string().optional(),
            "totalResults": t.integer().optional(),
            "kind": t.string().optional(),
            "startIndex": t.integer().optional(),
            "items": t.array(t.proxy(renames["FilterOut"])).optional(),
            "previousLink": t.string().optional(),
            "nextLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FiltersOut"])
    types["EntityUserLinkIn"] = t.struct(
        {
            "id": t.string().optional(),
            "entity": t.struct(
                {
                    "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                    "accountRef": t.proxy(renames["AccountRefIn"]).optional(),
                    "webPropertyRef": t.proxy(renames["WebPropertyRefIn"]).optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "selfLink": t.string().optional(),
            "permissions": t.struct(
                {"local": t.array(t.string()).optional()}
            ).optional(),
            "userRef": t.proxy(renames["UserRefIn"]).optional(),
        }
    ).named(renames["EntityUserLinkIn"])
    types["EntityUserLinkOut"] = t.struct(
        {
            "id": t.string().optional(),
            "entity": t.struct(
                {
                    "profileRef": t.proxy(renames["ProfileRefOut"]).optional(),
                    "accountRef": t.proxy(renames["AccountRefOut"]).optional(),
                    "webPropertyRef": t.proxy(renames["WebPropertyRefOut"]).optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "selfLink": t.string().optional(),
            "permissions": t.struct(
                {
                    "local": t.array(t.string()).optional(),
                    "effective": t.array(t.string()).optional(),
                }
            ).optional(),
            "userRef": t.proxy(renames["UserRefOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityUserLinkOut"])
    types["UploadIn"] = t.struct(
        {
            "status": t.string().optional(),
            "id": t.string().optional(),
            "errors": t.array(t.string()).optional(),
            "uploadTime": t.string().optional(),
            "customDataSourceId": t.string().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["UploadIn"])
    types["UploadOut"] = t.struct(
        {
            "status": t.string().optional(),
            "id": t.string().optional(),
            "errors": t.array(t.string()).optional(),
            "uploadTime": t.string().optional(),
            "customDataSourceId": t.string().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadOut"])
    types["AccountsIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["AccountIn"])).optional(),
            "username": t.string().optional(),
            "previousLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "nextLink": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AccountsIn"])
    types["AccountsOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["AccountOut"])).optional(),
            "username": t.string().optional(),
            "previousLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "nextLink": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsOut"])
    types["ExperimentIn"] = t.struct(
        {
            "variations": t.array(
                t.struct(
                    {
                        "won": t.boolean().optional(),
                        "name": t.string().optional(),
                        "status": t.string().optional(),
                        "url": t.string().optional(),
                        "weight": t.number().optional(),
                    }
                )
            ).optional(),
            "profileId": t.string().optional(),
            "snippet": t.string().optional(),
            "winnerFound": t.boolean().optional(),
            "optimizationType": t.string().optional(),
            "id": t.string().optional(),
            "reasonExperimentEnded": t.string().optional(),
            "kind": t.string().optional(),
            "minimumExperimentLengthInDays": t.integer().optional(),
            "rewriteVariationUrlsAsOriginal": t.boolean().optional(),
            "selfLink": t.string().optional(),
            "accountId": t.string().optional(),
            "trafficCoverage": t.number().optional(),
            "objectiveMetric": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
            "created": t.string().optional(),
            "winnerConfidenceLevel": t.number().optional(),
            "equalWeighting": t.boolean().optional(),
            "startTime": t.string().optional(),
            "servingFramework": t.string().optional(),
            "parentLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "description": t.string().optional(),
            "updated": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "editableInGaUi": t.boolean().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["ExperimentIn"])
    types["ExperimentOut"] = t.struct(
        {
            "variations": t.array(
                t.struct(
                    {
                        "won": t.boolean().optional(),
                        "name": t.string().optional(),
                        "status": t.string().optional(),
                        "url": t.string().optional(),
                        "weight": t.number().optional(),
                    }
                )
            ).optional(),
            "profileId": t.string().optional(),
            "snippet": t.string().optional(),
            "winnerFound": t.boolean().optional(),
            "optimizationType": t.string().optional(),
            "id": t.string().optional(),
            "reasonExperimentEnded": t.string().optional(),
            "kind": t.string().optional(),
            "minimumExperimentLengthInDays": t.integer().optional(),
            "rewriteVariationUrlsAsOriginal": t.boolean().optional(),
            "selfLink": t.string().optional(),
            "accountId": t.string().optional(),
            "trafficCoverage": t.number().optional(),
            "objectiveMetric": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
            "created": t.string().optional(),
            "winnerConfidenceLevel": t.number().optional(),
            "equalWeighting": t.boolean().optional(),
            "startTime": t.string().optional(),
            "servingFramework": t.string().optional(),
            "parentLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "description": t.string().optional(),
            "updated": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "editableInGaUi": t.boolean().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExperimentOut"])
    types["EntityUserLinksIn"] = t.struct(
        {
            "totalResults": t.integer().optional(),
            "previousLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "nextLink": t.string().optional(),
            "kind": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "items": t.array(t.proxy(renames["EntityUserLinkIn"])).optional(),
        }
    ).named(renames["EntityUserLinksIn"])
    types["EntityUserLinksOut"] = t.struct(
        {
            "totalResults": t.integer().optional(),
            "previousLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "nextLink": t.string().optional(),
            "kind": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "items": t.array(t.proxy(renames["EntityUserLinkOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityUserLinksOut"])
    types["FilterRefIn"] = t.struct(
        {
            "href": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["FilterRefIn"])
    types["FilterRefOut"] = t.struct(
        {
            "name": t.string().optional(),
            "href": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterRefOut"])
    types["WebpropertiesIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "startIndex": t.integer().optional(),
            "previousLink": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "totalResults": t.integer().optional(),
            "nextLink": t.string().optional(),
            "items": t.array(t.proxy(renames["WebpropertyIn"])).optional(),
            "username": t.string().optional(),
        }
    ).named(renames["WebpropertiesIn"])
    types["WebpropertiesOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "startIndex": t.integer().optional(),
            "previousLink": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "totalResults": t.integer().optional(),
            "nextLink": t.string().optional(),
            "items": t.array(t.proxy(renames["WebpropertyOut"])).optional(),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebpropertiesOut"])
    types["RemarketingAudiencesIn"] = t.struct(
        {
            "previousLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "nextLink": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["RemarketingAudienceIn"])).optional(),
            "username": t.string().optional(),
        }
    ).named(renames["RemarketingAudiencesIn"])
    types["RemarketingAudiencesOut"] = t.struct(
        {
            "previousLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "nextLink": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["RemarketingAudienceOut"])).optional(),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemarketingAudiencesOut"])
    types["ProfileSummaryIn"] = t.struct(
        {
            "starred": t.boolean().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ProfileSummaryIn"])
    types["ProfileSummaryOut"] = t.struct(
        {
            "starred": t.boolean().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileSummaryOut"])
    types["HashClientIdRequestIn"] = t.struct(
        {"kind": t.string(), "clientId": t.string(), "webPropertyId": t.string()}
    ).named(renames["HashClientIdRequestIn"])
    types["HashClientIdRequestOut"] = t.struct(
        {
            "kind": t.string(),
            "clientId": t.string(),
            "webPropertyId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HashClientIdRequestOut"])
    types["FilterExpressionIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "matchType": t.string().optional(),
            "field": t.string().optional(),
            "expressionValue": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "fieldIndex": t.integer().optional(),
        }
    ).named(renames["FilterExpressionIn"])
    types["FilterExpressionOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "matchType": t.string().optional(),
            "field": t.string().optional(),
            "expressionValue": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "fieldIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterExpressionOut"])
    types["AccountIn"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "updated": t.string().optional(),
            "starred": t.boolean().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "permissions": t.struct({"_": t.string().optional()}).optional(),
            "childLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "created": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "updated": t.string().optional(),
            "starred": t.boolean().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "permissions": t.struct(
                {"effective": t.array(t.string()).optional()}
            ).optional(),
            "childLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "created": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
    types["UserDeletionRequestIn"] = t.struct(
        {
            "firebaseProjectId": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.struct(
                {"type": t.string().optional(), "userId": t.string().optional()}
            ).optional(),
            "propertyId": t.string().optional(),
            "webPropertyId": t.string().optional(),
        }
    ).named(renames["UserDeletionRequestIn"])
    types["UserDeletionRequestOut"] = t.struct(
        {
            "firebaseProjectId": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.struct(
                {"type": t.string().optional(), "userId": t.string().optional()}
            ).optional(),
            "propertyId": t.string().optional(),
            "deletionRequestTime": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserDeletionRequestOut"])
    types["EntityAdWordsLinksIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextLink": t.string().optional(),
            "previousLink": t.string().optional(),
            "items": t.array(t.proxy(renames["EntityAdWordsLinkIn"])).optional(),
            "startIndex": t.integer().optional(),
            "itemsPerPage": t.integer().optional(),
            "totalResults": t.integer().optional(),
        }
    ).named(renames["EntityAdWordsLinksIn"])
    types["EntityAdWordsLinksOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextLink": t.string().optional(),
            "previousLink": t.string().optional(),
            "items": t.array(t.proxy(renames["EntityAdWordsLinkOut"])).optional(),
            "startIndex": t.integer().optional(),
            "itemsPerPage": t.integer().optional(),
            "totalResults": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityAdWordsLinksOut"])
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
            "name": t.string().optional(),
            "id": t.string().optional(),
            "webProperties": t.array(
                t.proxy(renames["WebPropertySummaryIn"])
            ).optional(),
            "kind": t.string().optional(),
            "starred": t.boolean().optional(),
        }
    ).named(renames["AccountSummaryIn"])
    types["AccountSummaryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "webProperties": t.array(
                t.proxy(renames["WebPropertySummaryOut"])
            ).optional(),
            "kind": t.string().optional(),
            "starred": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountSummaryOut"])
    types["HashClientIdResponseIn"] = t.struct(
        {
            "kind": t.string(),
            "clientId": t.string(),
            "webPropertyId": t.string(),
            "hashedClientId": t.string(),
        }
    ).named(renames["HashClientIdResponseIn"])
    types["HashClientIdResponseOut"] = t.struct(
        {
            "kind": t.string(),
            "clientId": t.string(),
            "webPropertyId": t.string(),
            "hashedClientId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HashClientIdResponseOut"])
    types["WebPropertySummaryIn"] = t.struct(
        {
            "id": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "profiles": t.array(t.proxy(renames["ProfileSummaryIn"])).optional(),
            "kind": t.string().optional(),
            "starred": t.boolean().optional(),
            "name": t.string().optional(),
            "level": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
        }
    ).named(renames["WebPropertySummaryIn"])
    types["WebPropertySummaryOut"] = t.struct(
        {
            "id": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "profiles": t.array(t.proxy(renames["ProfileSummaryOut"])).optional(),
            "kind": t.string().optional(),
            "starred": t.boolean().optional(),
            "name": t.string().optional(),
            "level": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebPropertySummaryOut"])
    types["UnsampledReportsIn"] = t.struct(
        {
            "username": t.string().optional(),
            "kind": t.string().optional(),
            "nextLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "items": t.array(t.proxy(renames["UnsampledReportIn"])).optional(),
            "previousLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "itemsPerPage": t.integer().optional(),
        }
    ).named(renames["UnsampledReportsIn"])
    types["UnsampledReportsOut"] = t.struct(
        {
            "username": t.string().optional(),
            "kind": t.string().optional(),
            "nextLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "items": t.array(t.proxy(renames["UnsampledReportOut"])).optional(),
            "previousLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "itemsPerPage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnsampledReportsOut"])
    types["ExperimentsIn"] = t.struct(
        {
            "username": t.string().optional(),
            "startIndex": t.integer().optional(),
            "totalResults": t.integer().optional(),
            "previousLink": t.string().optional(),
            "items": t.array(t.proxy(renames["ExperimentIn"])).optional(),
            "nextLink": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ExperimentsIn"])
    types["ExperimentsOut"] = t.struct(
        {
            "username": t.string().optional(),
            "startIndex": t.integer().optional(),
            "totalResults": t.integer().optional(),
            "previousLink": t.string().optional(),
            "items": t.array(t.proxy(renames["ExperimentOut"])).optional(),
            "nextLink": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExperimentsOut"])
    types["AccountSummariesIn"] = t.struct(
        {
            "itemsPerPage": t.integer().optional(),
            "items": t.array(t.proxy(renames["AccountSummaryIn"])).optional(),
            "nextLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "kind": t.string().optional(),
            "previousLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "username": t.string().optional(),
        }
    ).named(renames["AccountSummariesIn"])
    types["AccountSummariesOut"] = t.struct(
        {
            "itemsPerPage": t.integer().optional(),
            "items": t.array(t.proxy(renames["AccountSummaryOut"])).optional(),
            "nextLink": t.string().optional(),
            "startIndex": t.integer().optional(),
            "kind": t.string().optional(),
            "previousLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountSummariesOut"])
    types["ProfileFilterLinkIn"] = t.struct(
        {
            "rank": t.integer().optional(),
            "filterRef": t.proxy(renames["FilterRefIn"]).optional(),
            "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["ProfileFilterLinkIn"])
    types["ProfileFilterLinkOut"] = t.struct(
        {
            "rank": t.integer().optional(),
            "filterRef": t.proxy(renames["FilterRefOut"]).optional(),
            "profileRef": t.proxy(renames["ProfileRefOut"]).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileFilterLinkOut"])
    types["CustomDimensionsIn"] = t.struct(
        {
            "totalResults": t.integer().optional(),
            "kind": t.string().optional(),
            "startIndex": t.integer().optional(),
            "itemsPerPage": t.integer().optional(),
            "previousLink": t.string().optional(),
            "nextLink": t.string().optional(),
            "items": t.array(t.proxy(renames["CustomDimensionIn"])).optional(),
            "username": t.string().optional(),
        }
    ).named(renames["CustomDimensionsIn"])
    types["CustomDimensionsOut"] = t.struct(
        {
            "totalResults": t.integer().optional(),
            "kind": t.string().optional(),
            "startIndex": t.integer().optional(),
            "itemsPerPage": t.integer().optional(),
            "previousLink": t.string().optional(),
            "nextLink": t.string().optional(),
            "items": t.array(t.proxy(renames["CustomDimensionOut"])).optional(),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomDimensionsOut"])
    types["LinkedForeignAccountIn"] = t.struct(
        {
            "type": t.string().optional(),
            "remarketingAudienceId": t.string().optional(),
            "accountId": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "linkedAccountId": t.string().optional(),
        }
    ).named(renames["LinkedForeignAccountIn"])
    types["LinkedForeignAccountOut"] = t.struct(
        {
            "type": t.string().optional(),
            "remarketingAudienceId": t.string().optional(),
            "accountId": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "kind": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "eligibleForSearch": t.boolean().optional(),
            "linkedAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedForeignAccountOut"])
    types["ProfileFilterLinksIn"] = t.struct(
        {
            "nextLink": t.string().optional(),
            "previousLink": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "items": t.array(t.proxy(renames["ProfileFilterLinkIn"])).optional(),
            "startIndex": t.integer().optional(),
            "username": t.string().optional(),
            "totalResults": t.integer().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ProfileFilterLinksIn"])
    types["ProfileFilterLinksOut"] = t.struct(
        {
            "nextLink": t.string().optional(),
            "previousLink": t.string().optional(),
            "itemsPerPage": t.integer().optional(),
            "items": t.array(t.proxy(renames["ProfileFilterLinkOut"])).optional(),
            "startIndex": t.integer().optional(),
            "username": t.string().optional(),
            "totalResults": t.integer().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileFilterLinksOut"])
    types["AccountTreeRequestIn"] = t.struct(
        {
            "profileName": t.string(),
            "kind": t.string().optional(),
            "accountName": t.string(),
            "websiteUrl": t.string(),
            "webpropertyName": t.string(),
            "timezone": t.string(),
        }
    ).named(renames["AccountTreeRequestIn"])
    types["AccountTreeRequestOut"] = t.struct(
        {
            "profileName": t.string(),
            "kind": t.string().optional(),
            "accountName": t.string(),
            "websiteUrl": t.string(),
            "webpropertyName": t.string(),
            "timezone": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountTreeRequestOut"])
    types["FilterIn"] = t.struct(
        {
            "searchAndReplaceDetails": t.struct(
                {
                    "fieldIndex": t.integer().optional(),
                    "replaceString": t.string().optional(),
                    "searchString": t.string().optional(),
                    "field": t.string().optional(),
                    "caseSensitive": t.boolean().optional(),
                }
            ).optional(),
            "advancedDetails": t.struct(
                {
                    "caseSensitive": t.boolean().optional(),
                    "outputConstructor": t.string().optional(),
                    "fieldA": t.string().optional(),
                    "fieldAIndex": t.integer().optional(),
                    "outputToField": t.string().optional(),
                    "outputToFieldIndex": t.integer().optional(),
                    "extractB": t.string().optional(),
                    "fieldB": t.string().optional(),
                    "fieldBIndex": t.integer().optional(),
                    "extractA": t.string().optional(),
                    "fieldARequired": t.boolean().optional(),
                    "overrideOutputField": t.boolean().optional(),
                    "fieldBRequired": t.boolean().optional(),
                }
            ).optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "lowercaseDetails": t.struct(
                {"fieldIndex": t.integer().optional(), "field": t.string().optional()}
            ).optional(),
            "accountId": t.string().optional(),
            "parentLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "includeDetails": t.proxy(renames["FilterExpressionIn"]).optional(),
            "uppercaseDetails": t.struct(
                {"field": t.string().optional(), "fieldIndex": t.integer().optional()}
            ).optional(),
            "id": t.string().optional(),
            "excludeDetails": t.proxy(renames["FilterExpressionIn"]).optional(),
        }
    ).named(renames["FilterIn"])
    types["FilterOut"] = t.struct(
        {
            "searchAndReplaceDetails": t.struct(
                {
                    "fieldIndex": t.integer().optional(),
                    "replaceString": t.string().optional(),
                    "searchString": t.string().optional(),
                    "field": t.string().optional(),
                    "caseSensitive": t.boolean().optional(),
                }
            ).optional(),
            "created": t.string().optional(),
            "advancedDetails": t.struct(
                {
                    "caseSensitive": t.boolean().optional(),
                    "outputConstructor": t.string().optional(),
                    "fieldA": t.string().optional(),
                    "fieldAIndex": t.integer().optional(),
                    "outputToField": t.string().optional(),
                    "outputToFieldIndex": t.integer().optional(),
                    "extractB": t.string().optional(),
                    "fieldB": t.string().optional(),
                    "fieldBIndex": t.integer().optional(),
                    "extractA": t.string().optional(),
                    "fieldARequired": t.boolean().optional(),
                    "overrideOutputField": t.boolean().optional(),
                    "fieldBRequired": t.boolean().optional(),
                }
            ).optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "lowercaseDetails": t.struct(
                {"fieldIndex": t.integer().optional(), "field": t.string().optional()}
            ).optional(),
            "accountId": t.string().optional(),
            "parentLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "selfLink": t.string().optional(),
            "includeDetails": t.proxy(renames["FilterExpressionOut"]).optional(),
            "uppercaseDetails": t.struct(
                {"field": t.string().optional(), "fieldIndex": t.integer().optional()}
            ).optional(),
            "updated": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "excludeDetails": t.proxy(renames["FilterExpressionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])
    types["CustomMetricIn"] = t.struct(
        {
            "max_value": t.string().optional(),
            "id": t.string().optional(),
            "min_value": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "type": t.string().optional(),
            "active": t.boolean().optional(),
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "scope": t.string().optional(),
            "parentLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
        }
    ).named(renames["CustomMetricIn"])
    types["CustomMetricOut"] = t.struct(
        {
            "max_value": t.string().optional(),
            "id": t.string().optional(),
            "selfLink": t.string().optional(),
            "min_value": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "type": t.string().optional(),
            "updated": t.string().optional(),
            "active": t.boolean().optional(),
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "index": t.integer().optional(),
            "scope": t.string().optional(),
            "parentLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "created": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomMetricOut"])
    types["CustomDataSourcesIn"] = t.struct(
        {
            "nextLink": t.string().optional(),
            "username": t.string().optional(),
            "previousLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "itemsPerPage": t.integer().optional(),
            "kind": t.string().optional(),
            "startIndex": t.integer().optional(),
            "items": t.array(t.proxy(renames["CustomDataSourceIn"])).optional(),
        }
    ).named(renames["CustomDataSourcesIn"])
    types["CustomDataSourcesOut"] = t.struct(
        {
            "nextLink": t.string().optional(),
            "username": t.string().optional(),
            "previousLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "itemsPerPage": t.integer().optional(),
            "kind": t.string().optional(),
            "startIndex": t.integer().optional(),
            "items": t.array(t.proxy(renames["CustomDataSourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomDataSourcesOut"])
    types["WebPropertyRefIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
            "accountId": t.string().optional(),
            "href": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["WebPropertyRefIn"])
    types["WebPropertyRefOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
            "accountId": t.string().optional(),
            "href": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebPropertyRefOut"])
    types["ProfileRefIn"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "href": t.string().optional(),
            "accountId": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ProfileRefIn"])
    types["ProfileRefOut"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "href": t.string().optional(),
            "accountId": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileRefOut"])
    types["UserRefIn"] = t.struct(
        {
            "email": t.string().optional(),
            "kind": t.string(),
            "id": t.string().optional(),
        }
    ).named(renames["UserRefIn"])
    types["UserRefOut"] = t.struct(
        {
            "email": t.string().optional(),
            "kind": t.string(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserRefOut"])
    types["UnsampledReportIn"] = t.struct(
        {
            "metrics": t.string().optional(),
            "title": t.string().optional(),
            "accountId": t.string().optional(),
            "end-date": t.string().optional(),
            "id": t.string().optional(),
            "segment": t.string().optional(),
            "profileId": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "dimensions": t.string().optional(),
            "start-date": t.string().optional(),
            "filters": t.string().optional(),
        }
    ).named(renames["UnsampledReportIn"])
    types["UnsampledReportOut"] = t.struct(
        {
            "metrics": t.string().optional(),
            "title": t.string().optional(),
            "accountId": t.string().optional(),
            "end-date": t.string().optional(),
            "created": t.string().optional(),
            "id": t.string().optional(),
            "segment": t.string().optional(),
            "cloudStorageDownloadDetails": t.struct(
                {"bucketId": t.string().optional(), "objectId": t.string().optional()}
            ).optional(),
            "profileId": t.string().optional(),
            "kind": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "driveDownloadDetails": t.struct(
                {"documentId": t.string().optional()}
            ).optional(),
            "dimensions": t.string().optional(),
            "start-date": t.string().optional(),
            "updated": t.string().optional(),
            "filters": t.string().optional(),
            "selfLink": t.string().optional(),
            "downloadType": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnsampledReportOut"])
    types["WebpropertyIn"] = t.struct(
        {
            "starred": t.boolean().optional(),
            "defaultProfileId": t.string().optional(),
            "permissions": t.struct({"_": t.string().optional()}).optional(),
            "childLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "industryVertical": t.string().optional(),
            "parentLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "accountId": t.string().optional(),
            "dataRetentionResetOnNewActivity": t.boolean().optional(),
            "dataRetentionTtl": t.string().optional(),
            "id": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["WebpropertyIn"])
    types["WebpropertyOut"] = t.struct(
        {
            "starred": t.boolean().optional(),
            "selfLink": t.string().optional(),
            "defaultProfileId": t.string().optional(),
            "permissions": t.struct(
                {"effective": t.array(t.string()).optional()}
            ).optional(),
            "childLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "industryVertical": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
            "parentLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "created": t.string().optional(),
            "accountId": t.string().optional(),
            "level": t.string().optional(),
            "dataRetentionResetOnNewActivity": t.boolean().optional(),
            "dataRetentionTtl": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "profileCount": t.integer().optional(),
            "name": t.string().optional(),
            "updated": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebpropertyOut"])
    types["IncludeConditionsIn"] = t.struct(
        {
            "membershipDurationDays": t.integer().optional(),
            "kind": t.string().optional(),
            "daysToLookBack": t.integer().optional(),
            "isSmartList": t.boolean().optional(),
            "segment": t.string().optional(),
        }
    ).named(renames["IncludeConditionsIn"])
    types["IncludeConditionsOut"] = t.struct(
        {
            "membershipDurationDays": t.integer().optional(),
            "kind": t.string().optional(),
            "daysToLookBack": t.integer().optional(),
            "isSmartList": t.boolean().optional(),
            "segment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IncludeConditionsOut"])
    types["ProfileIn"] = t.struct(
        {
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "id": t.string().optional(),
            "stripSiteSearchCategoryParameters": t.boolean().optional(),
            "excludeQueryParameters": t.string().optional(),
            "eCommerceTracking": t.boolean().optional(),
            "stripSiteSearchQueryParameters": t.boolean().optional(),
            "permissions": t.struct({"_": t.string().optional()}).optional(),
            "botFilteringEnabled": t.boolean().optional(),
            "websiteUrl": t.string().optional(),
            "type": t.string().optional(),
            "childLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "enhancedECommerceTracking": t.boolean().optional(),
            "parentLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "siteSearchQueryParameters": t.string().optional(),
            "timezone": t.string().optional(),
            "currency": t.string().optional(),
            "siteSearchCategoryParameters": t.string().optional(),
            "defaultPage": t.string().optional(),
            "starred": t.boolean().optional(),
        }
    ).named(renames["ProfileIn"])
    types["ProfileOut"] = t.struct(
        {
            "updated": t.string().optional(),
            "created": t.string().optional(),
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "id": t.string().optional(),
            "stripSiteSearchCategoryParameters": t.boolean().optional(),
            "selfLink": t.string().optional(),
            "excludeQueryParameters": t.string().optional(),
            "internalWebPropertyId": t.string().optional(),
            "eCommerceTracking": t.boolean().optional(),
            "stripSiteSearchQueryParameters": t.boolean().optional(),
            "permissions": t.struct(
                {"effective": t.array(t.string()).optional()}
            ).optional(),
            "botFilteringEnabled": t.boolean().optional(),
            "websiteUrl": t.string().optional(),
            "type": t.string().optional(),
            "childLink": t.struct(
                {"href": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "webPropertyId": t.string().optional(),
            "enhancedECommerceTracking": t.boolean().optional(),
            "parentLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "siteSearchQueryParameters": t.string().optional(),
            "timezone": t.string().optional(),
            "currency": t.string().optional(),
            "siteSearchCategoryParameters": t.string().optional(),
            "defaultPage": t.string().optional(),
            "kind": t.string().optional(),
            "starred": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileOut"])
    types["UploadsIn"] = t.struct(
        {
            "nextLink": t.string().optional(),
            "previousLink": t.string().optional(),
            "items": t.array(t.proxy(renames["UploadIn"])).optional(),
            "totalResults": t.integer().optional(),
            "kind": t.string().optional(),
            "startIndex": t.integer().optional(),
            "itemsPerPage": t.integer().optional(),
        }
    ).named(renames["UploadsIn"])
    types["UploadsOut"] = t.struct(
        {
            "nextLink": t.string().optional(),
            "previousLink": t.string().optional(),
            "items": t.array(t.proxy(renames["UploadOut"])).optional(),
            "totalResults": t.integer().optional(),
            "kind": t.string().optional(),
            "startIndex": t.integer().optional(),
            "itemsPerPage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadsOut"])
    types["CustomDimensionIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "active": t.boolean().optional(),
            "scope": t.string().optional(),
            "name": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "id": t.string().optional(),
            "parentLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
        }
    ).named(renames["CustomDimensionIn"])
    types["CustomDimensionOut"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "accountId": t.string().optional(),
            "index": t.integer().optional(),
            "active": t.boolean().optional(),
            "created": t.string().optional(),
            "updated": t.string().optional(),
            "scope": t.string().optional(),
            "name": t.string().optional(),
            "webPropertyId": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "parentLink": t.struct(
                {"type": t.string().optional(), "href": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomDimensionOut"])
    types["AccountTreeResponseIn"] = t.struct(
        {
            "profile": t.proxy(renames["ProfileIn"]).optional(),
            "webproperty": t.proxy(renames["WebpropertyIn"]).optional(),
            "kind": t.string().optional(),
            "account": t.proxy(renames["AccountIn"]).optional(),
        }
    ).named(renames["AccountTreeResponseIn"])
    types["AccountTreeResponseOut"] = t.struct(
        {
            "profile": t.proxy(renames["ProfileOut"]).optional(),
            "webproperty": t.proxy(renames["WebpropertyOut"]).optional(),
            "kind": t.string().optional(),
            "account": t.proxy(renames["AccountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountTreeResponseOut"])
    types["CustomMetricsIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["CustomMetricIn"])).optional(),
            "kind": t.string().optional(),
            "startIndex": t.integer().optional(),
            "username": t.string().optional(),
            "previousLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "itemsPerPage": t.integer().optional(),
            "nextLink": t.string().optional(),
        }
    ).named(renames["CustomMetricsIn"])
    types["CustomMetricsOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["CustomMetricOut"])).optional(),
            "kind": t.string().optional(),
            "startIndex": t.integer().optional(),
            "username": t.string().optional(),
            "previousLink": t.string().optional(),
            "totalResults": t.integer().optional(),
            "itemsPerPage": t.integer().optional(),
            "nextLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomMetricsOut"])

    functions = {}
    functions["dataMcfGet"] = analytics.get(
        "data/mcf",
        t.struct(
            {
                "metrics": t.string().optional(),
                "sort": t.string().optional(),
                "filters": t.string().optional(),
                "ids": t.string().optional(),
                "samplingLevel": t.string().optional(),
                "max-results": t.integer().optional(),
                "dimensions": t.string().optional(),
                "start-date": t.string().optional(),
                "end-date": t.string().optional(),
                "start-index": t.integer().optional(),
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
                "max-results": t.integer().optional(),
                "sort": t.string().optional(),
                "metrics": t.string().optional(),
                "dimensions": t.string().optional(),
                "ids": t.string().optional(),
                "filters": t.string().optional(),
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
                "include-empty-rows": t.boolean().optional(),
                "dimensions": t.string().optional(),
                "end-date": t.string().optional(),
                "segment": t.string().optional(),
                "metrics": t.string().optional(),
                "ids": t.string().optional(),
                "sort": t.string().optional(),
                "samplingLevel": t.string().optional(),
                "output": t.string().optional(),
                "max-results": t.integer().optional(),
                "start-index": t.integer().optional(),
                "start-date": t.string().optional(),
                "filters": t.string().optional(),
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
    functions["userDeletionUserDeletionRequestUpsert"] = analytics.post(
        "userDeletion/userDeletionRequests:upsert",
        t.struct(
            {
                "firebaseProjectId": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.struct(
                    {"type": t.string().optional(), "userId": t.string().optional()}
                ).optional(),
                "propertyId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserDeletionRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["provisioningCreateAccountTree"] = analytics.post(
        "provisioning/createAccountTicket",
        t.struct(
            {
                "id": t.string().optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "redirectUri": t.string().optional(),
                "account": t.proxy(renames["AccountIn"]).optional(),
                "webproperty": t.proxy(renames["WebpropertyIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountTicketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["provisioningCreateAccountTicket"] = analytics.post(
        "provisioning/createAccountTicket",
        t.struct(
            {
                "id": t.string().optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "redirectUri": t.string().optional(),
                "account": t.proxy(renames["AccountIn"]).optional(),
                "webproperty": t.proxy(renames["WebpropertyIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountTicketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomDimensionsInsert"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDimensions/{customDimensionId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "customDimensionId": t.string().optional(),
                "accountId": t.string().optional(),
                "ignoreCustomDataSourceLinks": t.boolean().optional(),
                "active": t.boolean().optional(),
                "scope": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "parentLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomDimensionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomDimensionsList"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDimensions/{customDimensionId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "customDimensionId": t.string().optional(),
                "accountId": t.string().optional(),
                "ignoreCustomDataSourceLinks": t.boolean().optional(),
                "active": t.boolean().optional(),
                "scope": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "parentLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomDimensionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomDimensionsPatch"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDimensions/{customDimensionId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "customDimensionId": t.string().optional(),
                "accountId": t.string().optional(),
                "ignoreCustomDataSourceLinks": t.boolean().optional(),
                "active": t.boolean().optional(),
                "scope": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "parentLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomDimensionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomDimensionsGet"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDimensions/{customDimensionId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "customDimensionId": t.string().optional(),
                "accountId": t.string().optional(),
                "ignoreCustomDataSourceLinks": t.boolean().optional(),
                "active": t.boolean().optional(),
                "scope": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "parentLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomDimensionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomDimensionsUpdate"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDimensions/{customDimensionId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "customDimensionId": t.string().optional(),
                "accountId": t.string().optional(),
                "ignoreCustomDataSourceLinks": t.boolean().optional(),
                "active": t.boolean().optional(),
                "scope": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "parentLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomDimensionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementFiltersPatch"] = analytics.delete(
        "management/accounts/{accountId}/filters/{filterId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "filterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FilterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementFiltersGet"] = analytics.delete(
        "management/accounts/{accountId}/filters/{filterId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "filterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FilterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementFiltersInsert"] = analytics.delete(
        "management/accounts/{accountId}/filters/{filterId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "filterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FilterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementFiltersList"] = analytics.delete(
        "management/accounts/{accountId}/filters/{filterId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "filterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FilterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementFiltersUpdate"] = analytics.delete(
        "management/accounts/{accountId}/filters/{filterId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "filterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FilterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementFiltersDelete"] = analytics.delete(
        "management/accounts/{accountId}/filters/{filterId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "filterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FilterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebpropertiesList"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "starred": t.boolean().optional(),
                "defaultProfileId": t.string().optional(),
                "permissions": t.struct({"_": t.string().optional()}).optional(),
                "childLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "industryVertical": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "dataRetentionResetOnNewActivity": t.boolean().optional(),
                "dataRetentionTtl": t.string().optional(),
                "id": t.string().optional(),
                "websiteUrl": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebpropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebpropertiesGet"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "starred": t.boolean().optional(),
                "defaultProfileId": t.string().optional(),
                "permissions": t.struct({"_": t.string().optional()}).optional(),
                "childLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "industryVertical": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "dataRetentionResetOnNewActivity": t.boolean().optional(),
                "dataRetentionTtl": t.string().optional(),
                "id": t.string().optional(),
                "websiteUrl": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebpropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebpropertiesInsert"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "starred": t.boolean().optional(),
                "defaultProfileId": t.string().optional(),
                "permissions": t.struct({"_": t.string().optional()}).optional(),
                "childLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "industryVertical": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "dataRetentionResetOnNewActivity": t.boolean().optional(),
                "dataRetentionTtl": t.string().optional(),
                "id": t.string().optional(),
                "websiteUrl": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebpropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebpropertiesPatch"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "starred": t.boolean().optional(),
                "defaultProfileId": t.string().optional(),
                "permissions": t.struct({"_": t.string().optional()}).optional(),
                "childLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "industryVertical": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "dataRetentionResetOnNewActivity": t.boolean().optional(),
                "dataRetentionTtl": t.string().optional(),
                "id": t.string().optional(),
                "websiteUrl": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebpropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebpropertiesUpdate"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "starred": t.boolean().optional(),
                "defaultProfileId": t.string().optional(),
                "permissions": t.struct({"_": t.string().optional()}).optional(),
                "childLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "industryVertical": t.string().optional(),
                "parentLink": t.struct(
                    {"href": t.string().optional(), "type": t.string().optional()}
                ).optional(),
                "dataRetentionResetOnNewActivity": t.boolean().optional(),
                "dataRetentionTtl": t.string().optional(),
                "id": t.string().optional(),
                "websiteUrl": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebpropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfilesUpdate"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles",
        t.struct(
            {
                "start-index": t.integer().optional(),
                "webPropertyId": t.string().optional(),
                "max-results": t.integer().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProfilesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfilesInsert"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles",
        t.struct(
            {
                "start-index": t.integer().optional(),
                "webPropertyId": t.string().optional(),
                "max-results": t.integer().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProfilesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfilesGet"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles",
        t.struct(
            {
                "start-index": t.integer().optional(),
                "webPropertyId": t.string().optional(),
                "max-results": t.integer().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProfilesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfilesPatch"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles",
        t.struct(
            {
                "start-index": t.integer().optional(),
                "webPropertyId": t.string().optional(),
                "max-results": t.integer().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProfilesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfilesDelete"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles",
        t.struct(
            {
                "start-index": t.integer().optional(),
                "webPropertyId": t.string().optional(),
                "max-results": t.integer().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProfilesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfilesList"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles",
        t.struct(
            {
                "start-index": t.integer().optional(),
                "webPropertyId": t.string().optional(),
                "max-results": t.integer().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProfilesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileUserLinksInsert"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/entityUserLinks/{linkId}",
        t.struct(
            {
                "linkId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "id": t.string().optional(),
                "entity": t.struct(
                    {
                        "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                        "accountRef": t.proxy(renames["AccountRefIn"]).optional(),
                        "webPropertyRef": t.proxy(
                            renames["WebPropertyRefIn"]
                        ).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "permissions": t.struct(
                    {"local": t.array(t.string()).optional()}
                ).optional(),
                "userRef": t.proxy(renames["UserRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityUserLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileUserLinksDelete"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/entityUserLinks/{linkId}",
        t.struct(
            {
                "linkId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "id": t.string().optional(),
                "entity": t.struct(
                    {
                        "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                        "accountRef": t.proxy(renames["AccountRefIn"]).optional(),
                        "webPropertyRef": t.proxy(
                            renames["WebPropertyRefIn"]
                        ).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "permissions": t.struct(
                    {"local": t.array(t.string()).optional()}
                ).optional(),
                "userRef": t.proxy(renames["UserRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityUserLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileUserLinksList"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/entityUserLinks/{linkId}",
        t.struct(
            {
                "linkId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "id": t.string().optional(),
                "entity": t.struct(
                    {
                        "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                        "accountRef": t.proxy(renames["AccountRefIn"]).optional(),
                        "webPropertyRef": t.proxy(
                            renames["WebPropertyRefIn"]
                        ).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "permissions": t.struct(
                    {"local": t.array(t.string()).optional()}
                ).optional(),
                "userRef": t.proxy(renames["UserRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityUserLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileUserLinksUpdate"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/entityUserLinks/{linkId}",
        t.struct(
            {
                "linkId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "id": t.string().optional(),
                "entity": t.struct(
                    {
                        "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                        "accountRef": t.proxy(renames["AccountRefIn"]).optional(),
                        "webPropertyRef": t.proxy(
                            renames["WebPropertyRefIn"]
                        ).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "permissions": t.struct(
                    {"local": t.array(t.string()).optional()}
                ).optional(),
                "userRef": t.proxy(renames["UserRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityUserLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomMetricsInsert"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customMetrics/{customMetricId}",
        t.struct(
            {
                "customMetricId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomMetricsPatch"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customMetrics/{customMetricId}",
        t.struct(
            {
                "customMetricId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomMetricsList"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customMetrics/{customMetricId}",
        t.struct(
            {
                "customMetricId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomMetricsUpdate"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customMetrics/{customMetricId}",
        t.struct(
            {
                "customMetricId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomMetricsGet"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customMetrics/{customMetricId}",
        t.struct(
            {
                "customMetricId": t.string().optional(),
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementExperimentsList"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/experiments/{experimentId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "experimentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementExperimentsInsert"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/experiments/{experimentId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "experimentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementExperimentsDelete"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/experiments/{experimentId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "experimentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementExperimentsUpdate"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/experiments/{experimentId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "experimentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementExperimentsPatch"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/experiments/{experimentId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "experimentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementExperimentsGet"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/experiments/{experimentId}",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "experimentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExperimentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementGoalsUpdate"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/goals",
        t.struct(
            {
                "profileId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "updated": t.string().optional(),
                "type": t.string().optional(),
                "urlDestinationDetails": t.struct(
                    {
                        "firstStepRequired": t.boolean().optional(),
                        "matchType": t.string().optional(),
                        "url": t.string().optional(),
                        "caseSensitive": t.boolean().optional(),
                        "steps": t.array(
                            t.struct(
                                {
                                    "name": t.string().optional(),
                                    "url": t.string().optional(),
                                    "number": t.integer().optional(),
                                }
                            )
                        ).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "created": t.string().optional(),
                "parentLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "visitTimeOnSiteDetails": t.struct(
                    {
                        "comparisonType": t.string().optional(),
                        "comparisonValue": t.string().optional(),
                    }
                ).optional(),
                "active": t.boolean().optional(),
                "internalWebPropertyId": t.string().optional(),
                "eventDetails": t.struct(
                    {
                        "eventConditions": t.array(
                            t.struct(
                                {
                                    "matchType": t.string().optional(),
                                    "comparisonType": t.string().optional(),
                                    "type": t.string().optional(),
                                    "comparisonValue": t.string().optional(),
                                    "expression": t.string().optional(),
                                }
                            )
                        ).optional(),
                        "useEventValue": t.boolean().optional(),
                    }
                ).optional(),
                "value": t.number().optional(),
                "visitNumPagesDetails": t.struct(
                    {
                        "comparisonValue": t.string().optional(),
                        "comparisonType": t.string().optional(),
                    }
                ).optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementGoalsGet"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/goals",
        t.struct(
            {
                "profileId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "updated": t.string().optional(),
                "type": t.string().optional(),
                "urlDestinationDetails": t.struct(
                    {
                        "firstStepRequired": t.boolean().optional(),
                        "matchType": t.string().optional(),
                        "url": t.string().optional(),
                        "caseSensitive": t.boolean().optional(),
                        "steps": t.array(
                            t.struct(
                                {
                                    "name": t.string().optional(),
                                    "url": t.string().optional(),
                                    "number": t.integer().optional(),
                                }
                            )
                        ).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "created": t.string().optional(),
                "parentLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "visitTimeOnSiteDetails": t.struct(
                    {
                        "comparisonType": t.string().optional(),
                        "comparisonValue": t.string().optional(),
                    }
                ).optional(),
                "active": t.boolean().optional(),
                "internalWebPropertyId": t.string().optional(),
                "eventDetails": t.struct(
                    {
                        "eventConditions": t.array(
                            t.struct(
                                {
                                    "matchType": t.string().optional(),
                                    "comparisonType": t.string().optional(),
                                    "type": t.string().optional(),
                                    "comparisonValue": t.string().optional(),
                                    "expression": t.string().optional(),
                                }
                            )
                        ).optional(),
                        "useEventValue": t.boolean().optional(),
                    }
                ).optional(),
                "value": t.number().optional(),
                "visitNumPagesDetails": t.struct(
                    {
                        "comparisonValue": t.string().optional(),
                        "comparisonType": t.string().optional(),
                    }
                ).optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementGoalsList"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/goals",
        t.struct(
            {
                "profileId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "updated": t.string().optional(),
                "type": t.string().optional(),
                "urlDestinationDetails": t.struct(
                    {
                        "firstStepRequired": t.boolean().optional(),
                        "matchType": t.string().optional(),
                        "url": t.string().optional(),
                        "caseSensitive": t.boolean().optional(),
                        "steps": t.array(
                            t.struct(
                                {
                                    "name": t.string().optional(),
                                    "url": t.string().optional(),
                                    "number": t.integer().optional(),
                                }
                            )
                        ).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "created": t.string().optional(),
                "parentLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "visitTimeOnSiteDetails": t.struct(
                    {
                        "comparisonType": t.string().optional(),
                        "comparisonValue": t.string().optional(),
                    }
                ).optional(),
                "active": t.boolean().optional(),
                "internalWebPropertyId": t.string().optional(),
                "eventDetails": t.struct(
                    {
                        "eventConditions": t.array(
                            t.struct(
                                {
                                    "matchType": t.string().optional(),
                                    "comparisonType": t.string().optional(),
                                    "type": t.string().optional(),
                                    "comparisonValue": t.string().optional(),
                                    "expression": t.string().optional(),
                                }
                            )
                        ).optional(),
                        "useEventValue": t.boolean().optional(),
                    }
                ).optional(),
                "value": t.number().optional(),
                "visitNumPagesDetails": t.struct(
                    {
                        "comparisonValue": t.string().optional(),
                        "comparisonType": t.string().optional(),
                    }
                ).optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementGoalsPatch"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/goals",
        t.struct(
            {
                "profileId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "updated": t.string().optional(),
                "type": t.string().optional(),
                "urlDestinationDetails": t.struct(
                    {
                        "firstStepRequired": t.boolean().optional(),
                        "matchType": t.string().optional(),
                        "url": t.string().optional(),
                        "caseSensitive": t.boolean().optional(),
                        "steps": t.array(
                            t.struct(
                                {
                                    "name": t.string().optional(),
                                    "url": t.string().optional(),
                                    "number": t.integer().optional(),
                                }
                            )
                        ).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "created": t.string().optional(),
                "parentLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "visitTimeOnSiteDetails": t.struct(
                    {
                        "comparisonType": t.string().optional(),
                        "comparisonValue": t.string().optional(),
                    }
                ).optional(),
                "active": t.boolean().optional(),
                "internalWebPropertyId": t.string().optional(),
                "eventDetails": t.struct(
                    {
                        "eventConditions": t.array(
                            t.struct(
                                {
                                    "matchType": t.string().optional(),
                                    "comparisonType": t.string().optional(),
                                    "type": t.string().optional(),
                                    "comparisonValue": t.string().optional(),
                                    "expression": t.string().optional(),
                                }
                            )
                        ).optional(),
                        "useEventValue": t.boolean().optional(),
                    }
                ).optional(),
                "value": t.number().optional(),
                "visitNumPagesDetails": t.struct(
                    {
                        "comparisonValue": t.string().optional(),
                        "comparisonType": t.string().optional(),
                    }
                ).optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementGoalsInsert"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/goals",
        t.struct(
            {
                "profileId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "updated": t.string().optional(),
                "type": t.string().optional(),
                "urlDestinationDetails": t.struct(
                    {
                        "firstStepRequired": t.boolean().optional(),
                        "matchType": t.string().optional(),
                        "url": t.string().optional(),
                        "caseSensitive": t.boolean().optional(),
                        "steps": t.array(
                            t.struct(
                                {
                                    "name": t.string().optional(),
                                    "url": t.string().optional(),
                                    "number": t.integer().optional(),
                                }
                            )
                        ).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "created": t.string().optional(),
                "parentLink": t.struct(
                    {"type": t.string().optional(), "href": t.string().optional()}
                ).optional(),
                "visitTimeOnSiteDetails": t.struct(
                    {
                        "comparisonType": t.string().optional(),
                        "comparisonValue": t.string().optional(),
                    }
                ).optional(),
                "active": t.boolean().optional(),
                "internalWebPropertyId": t.string().optional(),
                "eventDetails": t.struct(
                    {
                        "eventConditions": t.array(
                            t.struct(
                                {
                                    "matchType": t.string().optional(),
                                    "comparisonType": t.string().optional(),
                                    "type": t.string().optional(),
                                    "comparisonValue": t.string().optional(),
                                    "expression": t.string().optional(),
                                }
                            )
                        ).optional(),
                        "useEventValue": t.boolean().optional(),
                    }
                ).optional(),
                "value": t.number().optional(),
                "visitNumPagesDetails": t.struct(
                    {
                        "comparisonValue": t.string().optional(),
                        "comparisonType": t.string().optional(),
                    }
                ).optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileFilterLinksList"] = analytics.delete(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/profileFilterLinks/{linkId}",
        t.struct(
            {
                "linkId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileFilterLinksInsert"] = analytics.delete(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/profileFilterLinks/{linkId}",
        t.struct(
            {
                "linkId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileFilterLinksPatch"] = analytics.delete(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/profileFilterLinks/{linkId}",
        t.struct(
            {
                "linkId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileFilterLinksGet"] = analytics.delete(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/profileFilterLinks/{linkId}",
        t.struct(
            {
                "linkId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileFilterLinksUpdate"] = analytics.delete(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/profileFilterLinks/{linkId}",
        t.struct(
            {
                "linkId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementProfileFilterLinksDelete"] = analytics.delete(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/profileFilterLinks/{linkId}",
        t.struct(
            {
                "linkId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "profileId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
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
    functions["managementAccountsList"] = analytics.get(
        "management/accounts",
        t.struct(
            {
                "start-index": t.integer().optional(),
                "max-results": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementClientIdHashClientId"] = analytics.post(
        "management/clientId:hashClientId",
        t.struct(
            {
                "kind": t.string(),
                "clientId": t.string(),
                "webPropertyId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HashClientIdResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementAccountSummariesList"] = analytics.get(
        "management/accountSummaries",
        t.struct(
            {
                "start-index": t.integer().optional(),
                "max-results": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountSummariesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementUploadsDeleteUploadData"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDataSources/{customDataSourceId}/uploads/{uploadId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "customDataSourceId": t.string().optional(),
                "uploadId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementUploadsList"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDataSources/{customDataSourceId}/uploads/{uploadId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "customDataSourceId": t.string().optional(),
                "uploadId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementUploadsUploadData"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDataSources/{customDataSourceId}/uploads/{uploadId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "customDataSourceId": t.string().optional(),
                "uploadId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementUploadsGet"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDataSources/{customDataSourceId}/uploads/{uploadId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "customDataSourceId": t.string().optional(),
                "uploadId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementCustomDataSourcesList"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/customDataSources",
        t.struct(
            {
                "start-index": t.integer().optional(),
                "accountId": t.string().optional(),
                "max-results": t.integer().optional(),
                "webPropertyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomDataSourcesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebPropertyAdWordsLinksUpdate"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/entityAdWordsLinks",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "max-results": t.integer().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityAdWordsLinksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebPropertyAdWordsLinksGet"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/entityAdWordsLinks",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "max-results": t.integer().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityAdWordsLinksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebPropertyAdWordsLinksPatch"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/entityAdWordsLinks",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "max-results": t.integer().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityAdWordsLinksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebPropertyAdWordsLinksInsert"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/entityAdWordsLinks",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "max-results": t.integer().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityAdWordsLinksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebPropertyAdWordsLinksDelete"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/entityAdWordsLinks",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "max-results": t.integer().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityAdWordsLinksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementWebPropertyAdWordsLinksList"] = analytics.get(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/entityAdWordsLinks",
        t.struct(
            {
                "webPropertyId": t.string().optional(),
                "accountId": t.string().optional(),
                "max-results": t.integer().optional(),
                "start-index": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityAdWordsLinksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementUnsampledReportsList"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/unsampledReports",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "profileId": t.string().optional(),
                "metrics": t.string().optional(),
                "title": t.string().optional(),
                "end-date": t.string().optional(),
                "id": t.string().optional(),
                "segment": t.string().optional(),
                "dimensions": t.string().optional(),
                "start-date": t.string().optional(),
                "filters": t.string().optional(),
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
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "profileId": t.string().optional(),
                "metrics": t.string().optional(),
                "title": t.string().optional(),
                "end-date": t.string().optional(),
                "id": t.string().optional(),
                "segment": t.string().optional(),
                "dimensions": t.string().optional(),
                "start-date": t.string().optional(),
                "filters": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UnsampledReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementUnsampledReportsGet"] = analytics.post(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/unsampledReports",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "profileId": t.string().optional(),
                "metrics": t.string().optional(),
                "title": t.string().optional(),
                "end-date": t.string().optional(),
                "id": t.string().optional(),
                "segment": t.string().optional(),
                "dimensions": t.string().optional(),
                "start-date": t.string().optional(),
                "filters": t.string().optional(),
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
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "profileId": t.string().optional(),
                "metrics": t.string().optional(),
                "title": t.string().optional(),
                "end-date": t.string().optional(),
                "id": t.string().optional(),
                "segment": t.string().optional(),
                "dimensions": t.string().optional(),
                "start-date": t.string().optional(),
                "filters": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UnsampledReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementRemarketingAudiencePatch"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/remarketingAudiences/{remarketingAudienceId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "remarketingAudienceId": t.string().optional(),
                "audienceType": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "audienceDefinition": t.struct(
                    {
                        "includeConditions": t.proxy(
                            renames["IncludeConditionsIn"]
                        ).optional()
                    }
                ).optional(),
                "linkedAdAccounts": t.array(
                    t.proxy(renames["LinkedForeignAccountIn"])
                ).optional(),
                "stateBasedAudienceDefinition": t.struct(
                    {
                        "includeConditions": t.proxy(
                            renames["IncludeConditionsIn"]
                        ).optional(),
                        "excludeConditions": t.struct(
                            {
                                "segment": t.string().optional(),
                                "exclusionDuration": t.string().optional(),
                            }
                        ).optional(),
                    }
                ).optional(),
                "linkedViews": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementRemarketingAudienceDelete"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/remarketingAudiences/{remarketingAudienceId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "remarketingAudienceId": t.string().optional(),
                "audienceType": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "audienceDefinition": t.struct(
                    {
                        "includeConditions": t.proxy(
                            renames["IncludeConditionsIn"]
                        ).optional()
                    }
                ).optional(),
                "linkedAdAccounts": t.array(
                    t.proxy(renames["LinkedForeignAccountIn"])
                ).optional(),
                "stateBasedAudienceDefinition": t.struct(
                    {
                        "includeConditions": t.proxy(
                            renames["IncludeConditionsIn"]
                        ).optional(),
                        "excludeConditions": t.struct(
                            {
                                "segment": t.string().optional(),
                                "exclusionDuration": t.string().optional(),
                            }
                        ).optional(),
                    }
                ).optional(),
                "linkedViews": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementRemarketingAudienceInsert"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/remarketingAudiences/{remarketingAudienceId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "remarketingAudienceId": t.string().optional(),
                "audienceType": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "audienceDefinition": t.struct(
                    {
                        "includeConditions": t.proxy(
                            renames["IncludeConditionsIn"]
                        ).optional()
                    }
                ).optional(),
                "linkedAdAccounts": t.array(
                    t.proxy(renames["LinkedForeignAccountIn"])
                ).optional(),
                "stateBasedAudienceDefinition": t.struct(
                    {
                        "includeConditions": t.proxy(
                            renames["IncludeConditionsIn"]
                        ).optional(),
                        "excludeConditions": t.struct(
                            {
                                "segment": t.string().optional(),
                                "exclusionDuration": t.string().optional(),
                            }
                        ).optional(),
                    }
                ).optional(),
                "linkedViews": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementRemarketingAudienceGet"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/remarketingAudiences/{remarketingAudienceId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "remarketingAudienceId": t.string().optional(),
                "audienceType": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "audienceDefinition": t.struct(
                    {
                        "includeConditions": t.proxy(
                            renames["IncludeConditionsIn"]
                        ).optional()
                    }
                ).optional(),
                "linkedAdAccounts": t.array(
                    t.proxy(renames["LinkedForeignAccountIn"])
                ).optional(),
                "stateBasedAudienceDefinition": t.struct(
                    {
                        "includeConditions": t.proxy(
                            renames["IncludeConditionsIn"]
                        ).optional(),
                        "excludeConditions": t.struct(
                            {
                                "segment": t.string().optional(),
                                "exclusionDuration": t.string().optional(),
                            }
                        ).optional(),
                    }
                ).optional(),
                "linkedViews": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementRemarketingAudienceList"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/remarketingAudiences/{remarketingAudienceId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "remarketingAudienceId": t.string().optional(),
                "audienceType": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "audienceDefinition": t.struct(
                    {
                        "includeConditions": t.proxy(
                            renames["IncludeConditionsIn"]
                        ).optional()
                    }
                ).optional(),
                "linkedAdAccounts": t.array(
                    t.proxy(renames["LinkedForeignAccountIn"])
                ).optional(),
                "stateBasedAudienceDefinition": t.struct(
                    {
                        "includeConditions": t.proxy(
                            renames["IncludeConditionsIn"]
                        ).optional(),
                        "excludeConditions": t.struct(
                            {
                                "segment": t.string().optional(),
                                "exclusionDuration": t.string().optional(),
                            }
                        ).optional(),
                    }
                ).optional(),
                "linkedViews": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementRemarketingAudienceUpdate"] = analytics.put(
        "management/accounts/{accountId}/webproperties/{webPropertyId}/remarketingAudiences/{remarketingAudienceId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "webPropertyId": t.string().optional(),
                "remarketingAudienceId": t.string().optional(),
                "audienceType": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "audienceDefinition": t.struct(
                    {
                        "includeConditions": t.proxy(
                            renames["IncludeConditionsIn"]
                        ).optional()
                    }
                ).optional(),
                "linkedAdAccounts": t.array(
                    t.proxy(renames["LinkedForeignAccountIn"])
                ).optional(),
                "stateBasedAudienceDefinition": t.struct(
                    {
                        "includeConditions": t.proxy(
                            renames["IncludeConditionsIn"]
                        ).optional(),
                        "excludeConditions": t.struct(
                            {
                                "segment": t.string().optional(),
                                "exclusionDuration": t.string().optional(),
                            }
                        ).optional(),
                    }
                ).optional(),
                "linkedViews": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RemarketingAudienceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementAccountUserLinksDelete"] = analytics.put(
        "management/accounts/{accountId}/entityUserLinks/{linkId}",
        t.struct(
            {
                "linkId": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "entity": t.struct(
                    {
                        "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                        "accountRef": t.proxy(renames["AccountRefIn"]).optional(),
                        "webPropertyRef": t.proxy(
                            renames["WebPropertyRefIn"]
                        ).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "permissions": t.struct(
                    {"local": t.array(t.string()).optional()}
                ).optional(),
                "userRef": t.proxy(renames["UserRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityUserLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementAccountUserLinksInsert"] = analytics.put(
        "management/accounts/{accountId}/entityUserLinks/{linkId}",
        t.struct(
            {
                "linkId": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "entity": t.struct(
                    {
                        "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                        "accountRef": t.proxy(renames["AccountRefIn"]).optional(),
                        "webPropertyRef": t.proxy(
                            renames["WebPropertyRefIn"]
                        ).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "permissions": t.struct(
                    {"local": t.array(t.string()).optional()}
                ).optional(),
                "userRef": t.proxy(renames["UserRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityUserLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementAccountUserLinksList"] = analytics.put(
        "management/accounts/{accountId}/entityUserLinks/{linkId}",
        t.struct(
            {
                "linkId": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "entity": t.struct(
                    {
                        "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                        "accountRef": t.proxy(renames["AccountRefIn"]).optional(),
                        "webPropertyRef": t.proxy(
                            renames["WebPropertyRefIn"]
                        ).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "permissions": t.struct(
                    {"local": t.array(t.string()).optional()}
                ).optional(),
                "userRef": t.proxy(renames["UserRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityUserLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managementAccountUserLinksUpdate"] = analytics.put(
        "management/accounts/{accountId}/entityUserLinks/{linkId}",
        t.struct(
            {
                "linkId": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "entity": t.struct(
                    {
                        "profileRef": t.proxy(renames["ProfileRefIn"]).optional(),
                        "accountRef": t.proxy(renames["AccountRefIn"]).optional(),
                        "webPropertyRef": t.proxy(
                            renames["WebPropertyRefIn"]
                        ).optional(),
                    }
                ).optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "permissions": t.struct(
                    {"local": t.array(t.string()).optional()}
                ).optional(),
                "userRef": t.proxy(renames["UserRefIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityUserLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="analytics",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
