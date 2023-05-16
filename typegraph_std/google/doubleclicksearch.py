from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_doubleclicksearch() -> Import:
    doubleclicksearch = HTTPRuntime("https://doubleclicksearch.googleapis.com/")

    renames = {
        "ErrorResponse": "_doubleclicksearch_1_ErrorResponse",
        "SavedColumnListIn": "_doubleclicksearch_2_SavedColumnListIn",
        "SavedColumnListOut": "_doubleclicksearch_3_SavedColumnListOut",
        "UpdateAvailabilityResponseIn": "_doubleclicksearch_4_UpdateAvailabilityResponseIn",
        "UpdateAvailabilityResponseOut": "_doubleclicksearch_5_UpdateAvailabilityResponseOut",
        "CustomDimensionIn": "_doubleclicksearch_6_CustomDimensionIn",
        "CustomDimensionOut": "_doubleclicksearch_7_CustomDimensionOut",
        "AvailabilityIn": "_doubleclicksearch_8_AvailabilityIn",
        "AvailabilityOut": "_doubleclicksearch_9_AvailabilityOut",
        "CustomMetricIn": "_doubleclicksearch_10_CustomMetricIn",
        "CustomMetricOut": "_doubleclicksearch_11_CustomMetricOut",
        "ConversionIn": "_doubleclicksearch_12_ConversionIn",
        "ConversionOut": "_doubleclicksearch_13_ConversionOut",
        "ReportRowIn": "_doubleclicksearch_14_ReportRowIn",
        "ReportRowOut": "_doubleclicksearch_15_ReportRowOut",
        "ConversionListIn": "_doubleclicksearch_16_ConversionListIn",
        "ConversionListOut": "_doubleclicksearch_17_ConversionListOut",
        "ReportIn": "_doubleclicksearch_18_ReportIn",
        "ReportOut": "_doubleclicksearch_19_ReportOut",
        "ReportApiColumnSpecIn": "_doubleclicksearch_20_ReportApiColumnSpecIn",
        "ReportApiColumnSpecOut": "_doubleclicksearch_21_ReportApiColumnSpecOut",
        "ReportRequestIn": "_doubleclicksearch_22_ReportRequestIn",
        "ReportRequestOut": "_doubleclicksearch_23_ReportRequestOut",
        "IdMappingFileIn": "_doubleclicksearch_24_IdMappingFileIn",
        "IdMappingFileOut": "_doubleclicksearch_25_IdMappingFileOut",
        "SavedColumnIn": "_doubleclicksearch_26_SavedColumnIn",
        "SavedColumnOut": "_doubleclicksearch_27_SavedColumnOut",
        "UpdateAvailabilityRequestIn": "_doubleclicksearch_28_UpdateAvailabilityRequestIn",
        "UpdateAvailabilityRequestOut": "_doubleclicksearch_29_UpdateAvailabilityRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SavedColumnListIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["SavedColumnIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SavedColumnListIn"])
    types["SavedColumnListOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["SavedColumnOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SavedColumnListOut"])
    types["UpdateAvailabilityResponseIn"] = t.struct(
        {"availabilities": t.array(t.proxy(renames["AvailabilityIn"])).optional()}
    ).named(renames["UpdateAvailabilityResponseIn"])
    types["UpdateAvailabilityResponseOut"] = t.struct(
        {
            "availabilities": t.array(t.proxy(renames["AvailabilityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateAvailabilityResponseOut"])
    types["CustomDimensionIn"] = t.struct(
        {"name": t.string().optional(), "value": t.string().optional()}
    ).named(renames["CustomDimensionIn"])
    types["CustomDimensionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomDimensionOut"])
    types["AvailabilityIn"] = t.struct(
        {
            "segmentationId": t.string().optional(),
            "segmentationName": t.string().optional(),
            "customerId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "agencyId": t.string().optional(),
            "segmentationType": t.string().optional(),
            "availabilityTimestamp": t.string().optional(),
        }
    ).named(renames["AvailabilityIn"])
    types["AvailabilityOut"] = t.struct(
        {
            "segmentationId": t.string().optional(),
            "segmentationName": t.string().optional(),
            "customerId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "agencyId": t.string().optional(),
            "segmentationType": t.string().optional(),
            "availabilityTimestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AvailabilityOut"])
    types["CustomMetricIn"] = t.struct(
        {"name": t.string().optional(), "value": t.number().optional()}
    ).named(renames["CustomMetricIn"])
    types["CustomMetricOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomMetricOut"])
    types["ConversionIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "customDimension": t.array(
                t.proxy(renames["CustomDimensionIn"])
            ).optional(),
            "advertiserId": t.string().optional(),
            "campaignId": t.string().optional(),
            "conversionTimestamp": t.string().optional(),
            "state": t.string().optional(),
            "deviceType": t.string().optional(),
            "customerId": t.string().optional(),
            "adGroupId": t.string().optional(),
            "storeId": t.string().optional(),
            "adId": t.string().optional(),
            "quantityMillis": t.string().optional(),
            "productGroupId": t.string().optional(),
            "currencyCode": t.string().optional(),
            "revenueMicros": t.string().optional(),
            "clickId": t.string().optional(),
            "segmentationName": t.string().optional(),
            "dsConversionId": t.string().optional(),
            "conversionId": t.string().optional(),
            "agencyId": t.string().optional(),
            "floodlightOrderId": t.string().optional(),
            "attributionModel": t.string().optional(),
            "engineAccountId": t.string().optional(),
            "productCountry": t.string().optional(),
            "segmentationType": t.string().optional(),
            "customMetric": t.array(t.proxy(renames["CustomMetricIn"])).optional(),
            "type": t.string().optional(),
            "channel": t.string().optional(),
            "criterionId": t.string().optional(),
            "conversionModifiedTimestamp": t.string().optional(),
            "productLanguage": t.string().optional(),
            "inventoryAccountId": t.string().optional(),
            "countMillis": t.string().optional(),
            "segmentationId": t.string().optional(),
        }
    ).named(renames["ConversionIn"])
    types["ConversionOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "customDimension": t.array(
                t.proxy(renames["CustomDimensionOut"])
            ).optional(),
            "advertiserId": t.string().optional(),
            "campaignId": t.string().optional(),
            "conversionTimestamp": t.string().optional(),
            "state": t.string().optional(),
            "deviceType": t.string().optional(),
            "customerId": t.string().optional(),
            "adGroupId": t.string().optional(),
            "storeId": t.string().optional(),
            "adId": t.string().optional(),
            "quantityMillis": t.string().optional(),
            "productGroupId": t.string().optional(),
            "currencyCode": t.string().optional(),
            "revenueMicros": t.string().optional(),
            "clickId": t.string().optional(),
            "segmentationName": t.string().optional(),
            "dsConversionId": t.string().optional(),
            "conversionId": t.string().optional(),
            "agencyId": t.string().optional(),
            "floodlightOrderId": t.string().optional(),
            "attributionModel": t.string().optional(),
            "engineAccountId": t.string().optional(),
            "productCountry": t.string().optional(),
            "segmentationType": t.string().optional(),
            "customMetric": t.array(t.proxy(renames["CustomMetricOut"])).optional(),
            "type": t.string().optional(),
            "channel": t.string().optional(),
            "criterionId": t.string().optional(),
            "conversionModifiedTimestamp": t.string().optional(),
            "productLanguage": t.string().optional(),
            "inventoryAccountId": t.string().optional(),
            "countMillis": t.string().optional(),
            "segmentationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionOut"])
    types["ReportRowIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReportRowIn"]
    )
    types["ReportRowOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReportRowOut"])
    types["ConversionListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "conversion": t.array(t.proxy(renames["ConversionIn"])).optional(),
        }
    ).named(renames["ConversionListIn"])
    types["ConversionListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "conversion": t.array(t.proxy(renames["ConversionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionListOut"])
    types["ReportIn"] = t.struct(
        {
            "statisticsCurrencyCode": t.string().optional(),
            "isReportReady": t.boolean().optional(),
            "statisticsTimeZone": t.string().optional(),
            "rows": t.array(t.proxy(renames["ReportRowIn"])).optional(),
            "files": t.array(
                t.struct(
                    {"url": t.string().optional(), "byteCount": t.string().optional()}
                )
            ).optional(),
            "rowCount": t.integer().optional(),
            "id": t.string().optional(),
            "request": t.proxy(renames["ReportRequestIn"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "statisticsCurrencyCode": t.string().optional(),
            "isReportReady": t.boolean().optional(),
            "statisticsTimeZone": t.string().optional(),
            "rows": t.array(t.proxy(renames["ReportRowOut"])).optional(),
            "files": t.array(
                t.struct(
                    {"url": t.string().optional(), "byteCount": t.string().optional()}
                )
            ).optional(),
            "rowCount": t.integer().optional(),
            "id": t.string().optional(),
            "request": t.proxy(renames["ReportRequestOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
    types["ReportApiColumnSpecIn"] = t.struct(
        {
            "savedColumnName": t.string().optional(),
            "groupByColumn": t.boolean().optional(),
            "endDate": t.string().optional(),
            "startDate": t.string().optional(),
            "customMetricName": t.string().optional(),
            "platformSource": t.string().optional(),
            "customDimensionName": t.string().optional(),
            "columnName": t.string().optional(),
            "productReportPerspective": t.string().optional(),
            "headerText": t.string().optional(),
        }
    ).named(renames["ReportApiColumnSpecIn"])
    types["ReportApiColumnSpecOut"] = t.struct(
        {
            "savedColumnName": t.string().optional(),
            "groupByColumn": t.boolean().optional(),
            "endDate": t.string().optional(),
            "startDate": t.string().optional(),
            "customMetricName": t.string().optional(),
            "platformSource": t.string().optional(),
            "customDimensionName": t.string().optional(),
            "columnName": t.string().optional(),
            "productReportPerspective": t.string().optional(),
            "headerText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportApiColumnSpecOut"])
    types["ReportRequestIn"] = t.struct(
        {
            "includeRemovedEntities": t.boolean().optional(),
            "timeRange": t.struct(
                {
                    "changedAttributesSinceTimestamp": t.string().optional(),
                    "changedMetricsSinceTimestamp": t.string().optional(),
                    "endDate": t.string().optional(),
                    "startDate": t.string().optional(),
                }
            ).optional(),
            "reportScope": t.struct(
                {
                    "adGroupId": t.string().optional(),
                    "keywordId": t.string().optional(),
                    "campaignId": t.string().optional(),
                    "advertiserId": t.string().optional(),
                    "adId": t.string().optional(),
                    "engineAccountId": t.string().optional(),
                    "agencyId": t.string().optional(),
                }
            ).optional(),
            "startRow": t.integer().optional(),
            "reportType": t.string().optional(),
            "rowCount": t.integer().optional(),
            "columns": t.array(t.proxy(renames["ReportApiColumnSpecIn"])).optional(),
            "maxRowsPerFile": t.integer().optional(),
            "statisticsCurrency": t.string().optional(),
            "verifySingleTimeZone": t.boolean().optional(),
            "includeDeletedEntities": t.boolean().optional(),
            "orderBy": t.array(
                t.struct(
                    {
                        "column": t.proxy(renames["ReportApiColumnSpecIn"]).optional(),
                        "sortOrder": t.string().optional(),
                    }
                )
            ).optional(),
            "downloadFormat": t.string().optional(),
            "filters": t.array(
                t.struct(
                    {
                        "operator": t.string().optional(),
                        "values": t.array(
                            t.struct({"_": t.string().optional()})
                        ).optional(),
                        "column": t.proxy(renames["ReportApiColumnSpecIn"]).optional(),
                    }
                )
            ).optional(),
        }
    ).named(renames["ReportRequestIn"])
    types["ReportRequestOut"] = t.struct(
        {
            "includeRemovedEntities": t.boolean().optional(),
            "timeRange": t.struct(
                {
                    "changedAttributesSinceTimestamp": t.string().optional(),
                    "changedMetricsSinceTimestamp": t.string().optional(),
                    "endDate": t.string().optional(),
                    "startDate": t.string().optional(),
                }
            ).optional(),
            "reportScope": t.struct(
                {
                    "adGroupId": t.string().optional(),
                    "keywordId": t.string().optional(),
                    "campaignId": t.string().optional(),
                    "advertiserId": t.string().optional(),
                    "adId": t.string().optional(),
                    "engineAccountId": t.string().optional(),
                    "agencyId": t.string().optional(),
                }
            ).optional(),
            "startRow": t.integer().optional(),
            "reportType": t.string().optional(),
            "rowCount": t.integer().optional(),
            "columns": t.array(t.proxy(renames["ReportApiColumnSpecOut"])).optional(),
            "maxRowsPerFile": t.integer().optional(),
            "statisticsCurrency": t.string().optional(),
            "verifySingleTimeZone": t.boolean().optional(),
            "includeDeletedEntities": t.boolean().optional(),
            "orderBy": t.array(
                t.struct(
                    {
                        "column": t.proxy(renames["ReportApiColumnSpecOut"]).optional(),
                        "sortOrder": t.string().optional(),
                    }
                )
            ).optional(),
            "downloadFormat": t.string().optional(),
            "filters": t.array(
                t.struct(
                    {
                        "operator": t.string().optional(),
                        "values": t.array(
                            t.struct({"_": t.string().optional()})
                        ).optional(),
                        "column": t.proxy(renames["ReportApiColumnSpecOut"]).optional(),
                    }
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRequestOut"])
    types["IdMappingFileIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IdMappingFileIn"]
    )
    types["IdMappingFileOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IdMappingFileOut"])
    types["SavedColumnIn"] = t.struct(
        {
            "savedColumnName": t.string().optional(),
            "type": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SavedColumnIn"])
    types["SavedColumnOut"] = t.struct(
        {
            "savedColumnName": t.string().optional(),
            "type": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SavedColumnOut"])
    types["UpdateAvailabilityRequestIn"] = t.struct(
        {"availabilities": t.array(t.proxy(renames["AvailabilityIn"])).optional()}
    ).named(renames["UpdateAvailabilityRequestIn"])
    types["UpdateAvailabilityRequestOut"] = t.struct(
        {
            "availabilities": t.array(t.proxy(renames["AvailabilityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateAvailabilityRequestOut"])

    functions = {}
    functions["savedColumnsList"] = doubleclicksearch.get(
        "doubleclicksearch/v2/agency/{agencyId}/advertiser/{advertiserId}/savedcolumns",
        t.struct(
            {
                "agencyId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedColumnListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionUpdate"] = doubleclicksearch.post(
        "doubleclicksearch/v2/conversion/updateAvailability",
        t.struct(
            {
                "availabilities": t.array(
                    t.proxy(renames["AvailabilityIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UpdateAvailabilityResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionGetByCustomerId"] = doubleclicksearch.post(
        "doubleclicksearch/v2/conversion/updateAvailability",
        t.struct(
            {
                "availabilities": t.array(
                    t.proxy(renames["AvailabilityIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UpdateAvailabilityResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionGet"] = doubleclicksearch.post(
        "doubleclicksearch/v2/conversion/updateAvailability",
        t.struct(
            {
                "availabilities": t.array(
                    t.proxy(renames["AvailabilityIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UpdateAvailabilityResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionInsert"] = doubleclicksearch.post(
        "doubleclicksearch/v2/conversion/updateAvailability",
        t.struct(
            {
                "availabilities": t.array(
                    t.proxy(renames["AvailabilityIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UpdateAvailabilityResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionUpdateAvailability"] = doubleclicksearch.post(
        "doubleclicksearch/v2/conversion/updateAvailability",
        t.struct(
            {
                "availabilities": t.array(
                    t.proxy(renames["AvailabilityIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UpdateAvailabilityResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsGetFile"] = doubleclicksearch.post(
        "doubleclicksearch/v2/reports/generate",
        t.struct(
            {
                "includeRemovedEntities": t.boolean().optional(),
                "timeRange": t.struct(
                    {
                        "changedAttributesSinceTimestamp": t.string().optional(),
                        "changedMetricsSinceTimestamp": t.string().optional(),
                        "endDate": t.string().optional(),
                        "startDate": t.string().optional(),
                    }
                ).optional(),
                "reportScope": t.struct(
                    {
                        "adGroupId": t.string().optional(),
                        "keywordId": t.string().optional(),
                        "campaignId": t.string().optional(),
                        "advertiserId": t.string().optional(),
                        "adId": t.string().optional(),
                        "engineAccountId": t.string().optional(),
                        "agencyId": t.string().optional(),
                    }
                ).optional(),
                "startRow": t.integer().optional(),
                "reportType": t.string().optional(),
                "rowCount": t.integer().optional(),
                "columns": t.array(
                    t.proxy(renames["ReportApiColumnSpecIn"])
                ).optional(),
                "maxRowsPerFile": t.integer().optional(),
                "statisticsCurrency": t.string().optional(),
                "verifySingleTimeZone": t.boolean().optional(),
                "includeDeletedEntities": t.boolean().optional(),
                "orderBy": t.array(
                    t.struct(
                        {
                            "column": t.proxy(
                                renames["ReportApiColumnSpecIn"]
                            ).optional(),
                            "sortOrder": t.string().optional(),
                        }
                    )
                ).optional(),
                "downloadFormat": t.string().optional(),
                "filters": t.array(
                    t.struct(
                        {
                            "operator": t.string().optional(),
                            "values": t.array(
                                t.struct({"_": t.string().optional()})
                            ).optional(),
                            "column": t.proxy(
                                renames["ReportApiColumnSpecIn"]
                            ).optional(),
                        }
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsRequest"] = doubleclicksearch.post(
        "doubleclicksearch/v2/reports/generate",
        t.struct(
            {
                "includeRemovedEntities": t.boolean().optional(),
                "timeRange": t.struct(
                    {
                        "changedAttributesSinceTimestamp": t.string().optional(),
                        "changedMetricsSinceTimestamp": t.string().optional(),
                        "endDate": t.string().optional(),
                        "startDate": t.string().optional(),
                    }
                ).optional(),
                "reportScope": t.struct(
                    {
                        "adGroupId": t.string().optional(),
                        "keywordId": t.string().optional(),
                        "campaignId": t.string().optional(),
                        "advertiserId": t.string().optional(),
                        "adId": t.string().optional(),
                        "engineAccountId": t.string().optional(),
                        "agencyId": t.string().optional(),
                    }
                ).optional(),
                "startRow": t.integer().optional(),
                "reportType": t.string().optional(),
                "rowCount": t.integer().optional(),
                "columns": t.array(
                    t.proxy(renames["ReportApiColumnSpecIn"])
                ).optional(),
                "maxRowsPerFile": t.integer().optional(),
                "statisticsCurrency": t.string().optional(),
                "verifySingleTimeZone": t.boolean().optional(),
                "includeDeletedEntities": t.boolean().optional(),
                "orderBy": t.array(
                    t.struct(
                        {
                            "column": t.proxy(
                                renames["ReportApiColumnSpecIn"]
                            ).optional(),
                            "sortOrder": t.string().optional(),
                        }
                    )
                ).optional(),
                "downloadFormat": t.string().optional(),
                "filters": t.array(
                    t.struct(
                        {
                            "operator": t.string().optional(),
                            "values": t.array(
                                t.struct({"_": t.string().optional()})
                            ).optional(),
                            "column": t.proxy(
                                renames["ReportApiColumnSpecIn"]
                            ).optional(),
                        }
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsGetIdMappingFile"] = doubleclicksearch.post(
        "doubleclicksearch/v2/reports/generate",
        t.struct(
            {
                "includeRemovedEntities": t.boolean().optional(),
                "timeRange": t.struct(
                    {
                        "changedAttributesSinceTimestamp": t.string().optional(),
                        "changedMetricsSinceTimestamp": t.string().optional(),
                        "endDate": t.string().optional(),
                        "startDate": t.string().optional(),
                    }
                ).optional(),
                "reportScope": t.struct(
                    {
                        "adGroupId": t.string().optional(),
                        "keywordId": t.string().optional(),
                        "campaignId": t.string().optional(),
                        "advertiserId": t.string().optional(),
                        "adId": t.string().optional(),
                        "engineAccountId": t.string().optional(),
                        "agencyId": t.string().optional(),
                    }
                ).optional(),
                "startRow": t.integer().optional(),
                "reportType": t.string().optional(),
                "rowCount": t.integer().optional(),
                "columns": t.array(
                    t.proxy(renames["ReportApiColumnSpecIn"])
                ).optional(),
                "maxRowsPerFile": t.integer().optional(),
                "statisticsCurrency": t.string().optional(),
                "verifySingleTimeZone": t.boolean().optional(),
                "includeDeletedEntities": t.boolean().optional(),
                "orderBy": t.array(
                    t.struct(
                        {
                            "column": t.proxy(
                                renames["ReportApiColumnSpecIn"]
                            ).optional(),
                            "sortOrder": t.string().optional(),
                        }
                    )
                ).optional(),
                "downloadFormat": t.string().optional(),
                "filters": t.array(
                    t.struct(
                        {
                            "operator": t.string().optional(),
                            "values": t.array(
                                t.struct({"_": t.string().optional()})
                            ).optional(),
                            "column": t.proxy(
                                renames["ReportApiColumnSpecIn"]
                            ).optional(),
                        }
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsGet"] = doubleclicksearch.post(
        "doubleclicksearch/v2/reports/generate",
        t.struct(
            {
                "includeRemovedEntities": t.boolean().optional(),
                "timeRange": t.struct(
                    {
                        "changedAttributesSinceTimestamp": t.string().optional(),
                        "changedMetricsSinceTimestamp": t.string().optional(),
                        "endDate": t.string().optional(),
                        "startDate": t.string().optional(),
                    }
                ).optional(),
                "reportScope": t.struct(
                    {
                        "adGroupId": t.string().optional(),
                        "keywordId": t.string().optional(),
                        "campaignId": t.string().optional(),
                        "advertiserId": t.string().optional(),
                        "adId": t.string().optional(),
                        "engineAccountId": t.string().optional(),
                        "agencyId": t.string().optional(),
                    }
                ).optional(),
                "startRow": t.integer().optional(),
                "reportType": t.string().optional(),
                "rowCount": t.integer().optional(),
                "columns": t.array(
                    t.proxy(renames["ReportApiColumnSpecIn"])
                ).optional(),
                "maxRowsPerFile": t.integer().optional(),
                "statisticsCurrency": t.string().optional(),
                "verifySingleTimeZone": t.boolean().optional(),
                "includeDeletedEntities": t.boolean().optional(),
                "orderBy": t.array(
                    t.struct(
                        {
                            "column": t.proxy(
                                renames["ReportApiColumnSpecIn"]
                            ).optional(),
                            "sortOrder": t.string().optional(),
                        }
                    )
                ).optional(),
                "downloadFormat": t.string().optional(),
                "filters": t.array(
                    t.struct(
                        {
                            "operator": t.string().optional(),
                            "values": t.array(
                                t.struct({"_": t.string().optional()})
                            ).optional(),
                            "column": t.proxy(
                                renames["ReportApiColumnSpecIn"]
                            ).optional(),
                        }
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsGenerate"] = doubleclicksearch.post(
        "doubleclicksearch/v2/reports/generate",
        t.struct(
            {
                "includeRemovedEntities": t.boolean().optional(),
                "timeRange": t.struct(
                    {
                        "changedAttributesSinceTimestamp": t.string().optional(),
                        "changedMetricsSinceTimestamp": t.string().optional(),
                        "endDate": t.string().optional(),
                        "startDate": t.string().optional(),
                    }
                ).optional(),
                "reportScope": t.struct(
                    {
                        "adGroupId": t.string().optional(),
                        "keywordId": t.string().optional(),
                        "campaignId": t.string().optional(),
                        "advertiserId": t.string().optional(),
                        "adId": t.string().optional(),
                        "engineAccountId": t.string().optional(),
                        "agencyId": t.string().optional(),
                    }
                ).optional(),
                "startRow": t.integer().optional(),
                "reportType": t.string().optional(),
                "rowCount": t.integer().optional(),
                "columns": t.array(
                    t.proxy(renames["ReportApiColumnSpecIn"])
                ).optional(),
                "maxRowsPerFile": t.integer().optional(),
                "statisticsCurrency": t.string().optional(),
                "verifySingleTimeZone": t.boolean().optional(),
                "includeDeletedEntities": t.boolean().optional(),
                "orderBy": t.array(
                    t.struct(
                        {
                            "column": t.proxy(
                                renames["ReportApiColumnSpecIn"]
                            ).optional(),
                            "sortOrder": t.string().optional(),
                        }
                    )
                ).optional(),
                "downloadFormat": t.string().optional(),
                "filters": t.array(
                    t.struct(
                        {
                            "operator": t.string().optional(),
                            "values": t.array(
                                t.struct({"_": t.string().optional()})
                            ).optional(),
                            "column": t.proxy(
                                renames["ReportApiColumnSpecIn"]
                            ).optional(),
                        }
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="doubleclicksearch",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
