from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_doubleclicksearch():
    doubleclicksearch = HTTPRuntime("https://doubleclicksearch.googleapis.com/")

    renames = {
        "ErrorResponse": "_doubleclicksearch_1_ErrorResponse",
        "UpdateAvailabilityRequestIn": "_doubleclicksearch_2_UpdateAvailabilityRequestIn",
        "UpdateAvailabilityRequestOut": "_doubleclicksearch_3_UpdateAvailabilityRequestOut",
        "ReportRowIn": "_doubleclicksearch_4_ReportRowIn",
        "ReportRowOut": "_doubleclicksearch_5_ReportRowOut",
        "CustomDimensionIn": "_doubleclicksearch_6_CustomDimensionIn",
        "CustomDimensionOut": "_doubleclicksearch_7_CustomDimensionOut",
        "AvailabilityIn": "_doubleclicksearch_8_AvailabilityIn",
        "AvailabilityOut": "_doubleclicksearch_9_AvailabilityOut",
        "ConversionListIn": "_doubleclicksearch_10_ConversionListIn",
        "ConversionListOut": "_doubleclicksearch_11_ConversionListOut",
        "ReportRequestIn": "_doubleclicksearch_12_ReportRequestIn",
        "ReportRequestOut": "_doubleclicksearch_13_ReportRequestOut",
        "SavedColumnIn": "_doubleclicksearch_14_SavedColumnIn",
        "SavedColumnOut": "_doubleclicksearch_15_SavedColumnOut",
        "SavedColumnListIn": "_doubleclicksearch_16_SavedColumnListIn",
        "SavedColumnListOut": "_doubleclicksearch_17_SavedColumnListOut",
        "IdMappingFileIn": "_doubleclicksearch_18_IdMappingFileIn",
        "IdMappingFileOut": "_doubleclicksearch_19_IdMappingFileOut",
        "UpdateAvailabilityResponseIn": "_doubleclicksearch_20_UpdateAvailabilityResponseIn",
        "UpdateAvailabilityResponseOut": "_doubleclicksearch_21_UpdateAvailabilityResponseOut",
        "ReportApiColumnSpecIn": "_doubleclicksearch_22_ReportApiColumnSpecIn",
        "ReportApiColumnSpecOut": "_doubleclicksearch_23_ReportApiColumnSpecOut",
        "CustomMetricIn": "_doubleclicksearch_24_CustomMetricIn",
        "CustomMetricOut": "_doubleclicksearch_25_CustomMetricOut",
        "ReportIn": "_doubleclicksearch_26_ReportIn",
        "ReportOut": "_doubleclicksearch_27_ReportOut",
        "ConversionIn": "_doubleclicksearch_28_ConversionIn",
        "ConversionOut": "_doubleclicksearch_29_ConversionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["UpdateAvailabilityRequestIn"] = t.struct(
        {"availabilities": t.array(t.proxy(renames["AvailabilityIn"])).optional()}
    ).named(renames["UpdateAvailabilityRequestIn"])
    types["UpdateAvailabilityRequestOut"] = t.struct(
        {
            "availabilities": t.array(t.proxy(renames["AvailabilityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateAvailabilityRequestOut"])
    types["ReportRowIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReportRowIn"]
    )
    types["ReportRowOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReportRowOut"])
    types["CustomDimensionIn"] = t.struct(
        {"value": t.string().optional(), "name": t.string().optional()}
    ).named(renames["CustomDimensionIn"])
    types["CustomDimensionOut"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomDimensionOut"])
    types["AvailabilityIn"] = t.struct(
        {
            "availabilityTimestamp": t.string().optional(),
            "segmentationName": t.string().optional(),
            "customerId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "segmentationType": t.string().optional(),
            "agencyId": t.string().optional(),
            "segmentationId": t.string().optional(),
        }
    ).named(renames["AvailabilityIn"])
    types["AvailabilityOut"] = t.struct(
        {
            "availabilityTimestamp": t.string().optional(),
            "segmentationName": t.string().optional(),
            "customerId": t.string().optional(),
            "advertiserId": t.string().optional(),
            "segmentationType": t.string().optional(),
            "agencyId": t.string().optional(),
            "segmentationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AvailabilityOut"])
    types["ConversionListIn"] = t.struct(
        {
            "conversion": t.array(t.proxy(renames["ConversionIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ConversionListIn"])
    types["ConversionListOut"] = t.struct(
        {
            "conversion": t.array(t.proxy(renames["ConversionOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionListOut"])
    types["ReportRequestIn"] = t.struct(
        {
            "rowCount": t.integer().optional(),
            "filters": t.array(
                t.struct(
                    {
                        "values": t.array(
                            t.struct({"_": t.string().optional()})
                        ).optional(),
                        "column": t.proxy(renames["ReportApiColumnSpecIn"]).optional(),
                        "operator": t.string().optional(),
                    }
                )
            ).optional(),
            "downloadFormat": t.string().optional(),
            "timeRange": t.struct(
                {
                    "startDate": t.string().optional(),
                    "changedAttributesSinceTimestamp": t.string().optional(),
                    "changedMetricsSinceTimestamp": t.string().optional(),
                    "endDate": t.string().optional(),
                }
            ).optional(),
            "includeRemovedEntities": t.boolean().optional(),
            "reportType": t.string().optional(),
            "verifySingleTimeZone": t.boolean().optional(),
            "maxRowsPerFile": t.integer().optional(),
            "startRow": t.integer().optional(),
            "statisticsCurrency": t.string().optional(),
            "columns": t.array(t.proxy(renames["ReportApiColumnSpecIn"])).optional(),
            "orderBy": t.array(
                t.struct(
                    {
                        "column": t.proxy(renames["ReportApiColumnSpecIn"]).optional(),
                        "sortOrder": t.string().optional(),
                    }
                )
            ).optional(),
            "reportScope": t.struct(
                {
                    "adId": t.string().optional(),
                    "engineAccountId": t.string().optional(),
                    "agencyId": t.string().optional(),
                    "campaignId": t.string().optional(),
                    "advertiserId": t.string().optional(),
                    "keywordId": t.string().optional(),
                    "adGroupId": t.string().optional(),
                }
            ).optional(),
            "includeDeletedEntities": t.boolean().optional(),
        }
    ).named(renames["ReportRequestIn"])
    types["ReportRequestOut"] = t.struct(
        {
            "rowCount": t.integer().optional(),
            "filters": t.array(
                t.struct(
                    {
                        "values": t.array(
                            t.struct({"_": t.string().optional()})
                        ).optional(),
                        "column": t.proxy(renames["ReportApiColumnSpecOut"]).optional(),
                        "operator": t.string().optional(),
                    }
                )
            ).optional(),
            "downloadFormat": t.string().optional(),
            "timeRange": t.struct(
                {
                    "startDate": t.string().optional(),
                    "changedAttributesSinceTimestamp": t.string().optional(),
                    "changedMetricsSinceTimestamp": t.string().optional(),
                    "endDate": t.string().optional(),
                }
            ).optional(),
            "includeRemovedEntities": t.boolean().optional(),
            "reportType": t.string().optional(),
            "verifySingleTimeZone": t.boolean().optional(),
            "maxRowsPerFile": t.integer().optional(),
            "startRow": t.integer().optional(),
            "statisticsCurrency": t.string().optional(),
            "columns": t.array(t.proxy(renames["ReportApiColumnSpecOut"])).optional(),
            "orderBy": t.array(
                t.struct(
                    {
                        "column": t.proxy(renames["ReportApiColumnSpecOut"]).optional(),
                        "sortOrder": t.string().optional(),
                    }
                )
            ).optional(),
            "reportScope": t.struct(
                {
                    "adId": t.string().optional(),
                    "engineAccountId": t.string().optional(),
                    "agencyId": t.string().optional(),
                    "campaignId": t.string().optional(),
                    "advertiserId": t.string().optional(),
                    "keywordId": t.string().optional(),
                    "adGroupId": t.string().optional(),
                }
            ).optional(),
            "includeDeletedEntities": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRequestOut"])
    types["SavedColumnIn"] = t.struct(
        {
            "type": t.string().optional(),
            "savedColumnName": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SavedColumnIn"])
    types["SavedColumnOut"] = t.struct(
        {
            "type": t.string().optional(),
            "savedColumnName": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SavedColumnOut"])
    types["SavedColumnListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["SavedColumnIn"])).optional(),
        }
    ).named(renames["SavedColumnListIn"])
    types["SavedColumnListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["SavedColumnOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SavedColumnListOut"])
    types["IdMappingFileIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IdMappingFileIn"]
    )
    types["IdMappingFileOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IdMappingFileOut"])
    types["UpdateAvailabilityResponseIn"] = t.struct(
        {"availabilities": t.array(t.proxy(renames["AvailabilityIn"])).optional()}
    ).named(renames["UpdateAvailabilityResponseIn"])
    types["UpdateAvailabilityResponseOut"] = t.struct(
        {
            "availabilities": t.array(t.proxy(renames["AvailabilityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateAvailabilityResponseOut"])
    types["ReportApiColumnSpecIn"] = t.struct(
        {
            "groupByColumn": t.boolean().optional(),
            "savedColumnName": t.string().optional(),
            "columnName": t.string().optional(),
            "startDate": t.string().optional(),
            "customDimensionName": t.string().optional(),
            "platformSource": t.string().optional(),
            "headerText": t.string().optional(),
            "endDate": t.string().optional(),
            "customMetricName": t.string().optional(),
            "productReportPerspective": t.string().optional(),
        }
    ).named(renames["ReportApiColumnSpecIn"])
    types["ReportApiColumnSpecOut"] = t.struct(
        {
            "groupByColumn": t.boolean().optional(),
            "savedColumnName": t.string().optional(),
            "columnName": t.string().optional(),
            "startDate": t.string().optional(),
            "customDimensionName": t.string().optional(),
            "platformSource": t.string().optional(),
            "headerText": t.string().optional(),
            "endDate": t.string().optional(),
            "customMetricName": t.string().optional(),
            "productReportPerspective": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportApiColumnSpecOut"])
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
    types["ReportIn"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["ReportRowIn"])).optional(),
            "id": t.string().optional(),
            "rowCount": t.integer().optional(),
            "files": t.array(
                t.struct(
                    {"url": t.string().optional(), "byteCount": t.string().optional()}
                )
            ).optional(),
            "kind": t.string().optional(),
            "statisticsTimeZone": t.string().optional(),
            "statisticsCurrencyCode": t.string().optional(),
            "isReportReady": t.boolean().optional(),
            "request": t.proxy(renames["ReportRequestIn"]).optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["ReportRowOut"])).optional(),
            "id": t.string().optional(),
            "rowCount": t.integer().optional(),
            "files": t.array(
                t.struct(
                    {"url": t.string().optional(), "byteCount": t.string().optional()}
                )
            ).optional(),
            "kind": t.string().optional(),
            "statisticsTimeZone": t.string().optional(),
            "statisticsCurrencyCode": t.string().optional(),
            "isReportReady": t.boolean().optional(),
            "request": t.proxy(renames["ReportRequestOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
    types["ConversionIn"] = t.struct(
        {
            "conversionId": t.string().optional(),
            "attributionModel": t.string().optional(),
            "customMetric": t.array(t.proxy(renames["CustomMetricIn"])).optional(),
            "revenueMicros": t.string().optional(),
            "agencyId": t.string().optional(),
            "customerId": t.string().optional(),
            "deviceType": t.string().optional(),
            "criterionId": t.string().optional(),
            "segmentationId": t.string().optional(),
            "productLanguage": t.string().optional(),
            "customDimension": t.array(
                t.proxy(renames["CustomDimensionIn"])
            ).optional(),
            "segmentationName": t.string().optional(),
            "advertiserId": t.string().optional(),
            "inventoryAccountId": t.string().optional(),
            "clickId": t.string().optional(),
            "channel": t.string().optional(),
            "campaignId": t.string().optional(),
            "productCountry": t.string().optional(),
            "dsConversionId": t.string().optional(),
            "engineAccountId": t.string().optional(),
            "conversionTimestamp": t.string().optional(),
            "storeId": t.string().optional(),
            "adGroupId": t.string().optional(),
            "segmentationType": t.string().optional(),
            "productGroupId": t.string().optional(),
            "quantityMillis": t.string().optional(),
            "state": t.string().optional(),
            "adId": t.string().optional(),
            "countMillis": t.string().optional(),
            "conversionModifiedTimestamp": t.string().optional(),
            "currencyCode": t.string().optional(),
            "floodlightOrderId": t.string().optional(),
            "type": t.string().optional(),
            "productId": t.string().optional(),
        }
    ).named(renames["ConversionIn"])
    types["ConversionOut"] = t.struct(
        {
            "conversionId": t.string().optional(),
            "attributionModel": t.string().optional(),
            "customMetric": t.array(t.proxy(renames["CustomMetricOut"])).optional(),
            "revenueMicros": t.string().optional(),
            "agencyId": t.string().optional(),
            "customerId": t.string().optional(),
            "deviceType": t.string().optional(),
            "criterionId": t.string().optional(),
            "segmentationId": t.string().optional(),
            "productLanguage": t.string().optional(),
            "customDimension": t.array(
                t.proxy(renames["CustomDimensionOut"])
            ).optional(),
            "segmentationName": t.string().optional(),
            "advertiserId": t.string().optional(),
            "inventoryAccountId": t.string().optional(),
            "clickId": t.string().optional(),
            "channel": t.string().optional(),
            "campaignId": t.string().optional(),
            "productCountry": t.string().optional(),
            "dsConversionId": t.string().optional(),
            "engineAccountId": t.string().optional(),
            "conversionTimestamp": t.string().optional(),
            "storeId": t.string().optional(),
            "adGroupId": t.string().optional(),
            "segmentationType": t.string().optional(),
            "productGroupId": t.string().optional(),
            "quantityMillis": t.string().optional(),
            "state": t.string().optional(),
            "adId": t.string().optional(),
            "countMillis": t.string().optional(),
            "conversionModifiedTimestamp": t.string().optional(),
            "currencyCode": t.string().optional(),
            "floodlightOrderId": t.string().optional(),
            "type": t.string().optional(),
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionOut"])

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
    functions["conversionUpdateAvailability"] = doubleclicksearch.get(
        "doubleclicksearch/v2/agency/{agencyId}/advertiser/{advertiserId}/engine/{engineAccountId}/conversion",
        t.struct(
            {
                "agencyId": t.string().optional(),
                "adId": t.string().optional(),
                "startRow": t.integer().optional(),
                "rowCount": t.integer().optional(),
                "campaignId": t.string().optional(),
                "engineAccountId": t.string().optional(),
                "endDate": t.integer().optional(),
                "adGroupId": t.string().optional(),
                "customerId": t.string().optional(),
                "criterionId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "startDate": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConversionListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionGetByCustomerId"] = doubleclicksearch.get(
        "doubleclicksearch/v2/agency/{agencyId}/advertiser/{advertiserId}/engine/{engineAccountId}/conversion",
        t.struct(
            {
                "agencyId": t.string().optional(),
                "adId": t.string().optional(),
                "startRow": t.integer().optional(),
                "rowCount": t.integer().optional(),
                "campaignId": t.string().optional(),
                "engineAccountId": t.string().optional(),
                "endDate": t.integer().optional(),
                "adGroupId": t.string().optional(),
                "customerId": t.string().optional(),
                "criterionId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "startDate": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConversionListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionUpdate"] = doubleclicksearch.get(
        "doubleclicksearch/v2/agency/{agencyId}/advertiser/{advertiserId}/engine/{engineAccountId}/conversion",
        t.struct(
            {
                "agencyId": t.string().optional(),
                "adId": t.string().optional(),
                "startRow": t.integer().optional(),
                "rowCount": t.integer().optional(),
                "campaignId": t.string().optional(),
                "engineAccountId": t.string().optional(),
                "endDate": t.integer().optional(),
                "adGroupId": t.string().optional(),
                "customerId": t.string().optional(),
                "criterionId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "startDate": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConversionListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionInsert"] = doubleclicksearch.get(
        "doubleclicksearch/v2/agency/{agencyId}/advertiser/{advertiserId}/engine/{engineAccountId}/conversion",
        t.struct(
            {
                "agencyId": t.string().optional(),
                "adId": t.string().optional(),
                "startRow": t.integer().optional(),
                "rowCount": t.integer().optional(),
                "campaignId": t.string().optional(),
                "engineAccountId": t.string().optional(),
                "endDate": t.integer().optional(),
                "adGroupId": t.string().optional(),
                "customerId": t.string().optional(),
                "criterionId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "startDate": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConversionListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionGet"] = doubleclicksearch.get(
        "doubleclicksearch/v2/agency/{agencyId}/advertiser/{advertiserId}/engine/{engineAccountId}/conversion",
        t.struct(
            {
                "agencyId": t.string().optional(),
                "adId": t.string().optional(),
                "startRow": t.integer().optional(),
                "rowCount": t.integer().optional(),
                "campaignId": t.string().optional(),
                "engineAccountId": t.string().optional(),
                "endDate": t.integer().optional(),
                "adGroupId": t.string().optional(),
                "customerId": t.string().optional(),
                "criterionId": t.string().optional(),
                "advertiserId": t.string().optional(),
                "startDate": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConversionListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsGenerate"] = doubleclicksearch.get(
        "doubleclicksearch/v2/reports/{reportId}",
        t.struct({"reportId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsGetFile"] = doubleclicksearch.get(
        "doubleclicksearch/v2/reports/{reportId}",
        t.struct({"reportId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsGetIdMappingFile"] = doubleclicksearch.get(
        "doubleclicksearch/v2/reports/{reportId}",
        t.struct({"reportId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsRequest"] = doubleclicksearch.get(
        "doubleclicksearch/v2/reports/{reportId}",
        t.struct({"reportId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsGet"] = doubleclicksearch.get(
        "doubleclicksearch/v2/reports/{reportId}",
        t.struct({"reportId": t.string().optional(), "auth": t.string().optional()}),
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
