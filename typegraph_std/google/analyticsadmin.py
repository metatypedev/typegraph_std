from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_analyticsadmin() -> Import:
    analyticsadmin = HTTPRuntime("https://analyticsadmin.googleapis.com/")

    renames = {
        "ErrorResponse": "_analyticsadmin_1_ErrorResponse",
        "GoogleAnalyticsAdminV1betaAccessStringFilterIn": "_analyticsadmin_2_GoogleAnalyticsAdminV1betaAccessStringFilterIn",
        "GoogleAnalyticsAdminV1betaAccessStringFilterOut": "_analyticsadmin_3_GoogleAnalyticsAdminV1betaAccessStringFilterOut",
        "GoogleAnalyticsAdminV1betaListFirebaseLinksResponseIn": "_analyticsadmin_4_GoogleAnalyticsAdminV1betaListFirebaseLinksResponseIn",
        "GoogleAnalyticsAdminV1betaListFirebaseLinksResponseOut": "_analyticsadmin_5_GoogleAnalyticsAdminV1betaListFirebaseLinksResponseOut",
        "GoogleAnalyticsAdminV1betaAccessDimensionValueIn": "_analyticsadmin_6_GoogleAnalyticsAdminV1betaAccessDimensionValueIn",
        "GoogleAnalyticsAdminV1betaAccessDimensionValueOut": "_analyticsadmin_7_GoogleAnalyticsAdminV1betaAccessDimensionValueOut",
        "GoogleAnalyticsAdminV1betaListConversionEventsResponseIn": "_analyticsadmin_8_GoogleAnalyticsAdminV1betaListConversionEventsResponseIn",
        "GoogleAnalyticsAdminV1betaListConversionEventsResponseOut": "_analyticsadmin_9_GoogleAnalyticsAdminV1betaListConversionEventsResponseOut",
        "GoogleAnalyticsAdminV1betaAccessDateRangeIn": "_analyticsadmin_10_GoogleAnalyticsAdminV1betaAccessDateRangeIn",
        "GoogleAnalyticsAdminV1betaAccessDateRangeOut": "_analyticsadmin_11_GoogleAnalyticsAdminV1betaAccessDateRangeOut",
        "GoogleAnalyticsAdminV1betaAccessDimensionIn": "_analyticsadmin_12_GoogleAnalyticsAdminV1betaAccessDimensionIn",
        "GoogleAnalyticsAdminV1betaAccessDimensionOut": "_analyticsadmin_13_GoogleAnalyticsAdminV1betaAccessDimensionOut",
        "GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequestIn": "_analyticsadmin_14_GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequestIn",
        "GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequestOut": "_analyticsadmin_15_GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequestOut",
        "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceIn": "_analyticsadmin_16_GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceIn",
        "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceOut": "_analyticsadmin_17_GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceOut",
        "GoogleAnalyticsAdminV1betaListPropertiesResponseIn": "_analyticsadmin_18_GoogleAnalyticsAdminV1betaListPropertiesResponseIn",
        "GoogleAnalyticsAdminV1betaListPropertiesResponseOut": "_analyticsadmin_19_GoogleAnalyticsAdminV1betaListPropertiesResponseOut",
        "GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestIn": "_analyticsadmin_20_GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestIn",
        "GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestOut": "_analyticsadmin_21_GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestOut",
        "GoogleAnalyticsAdminV1betaAccessRowIn": "_analyticsadmin_22_GoogleAnalyticsAdminV1betaAccessRowIn",
        "GoogleAnalyticsAdminV1betaAccessRowOut": "_analyticsadmin_23_GoogleAnalyticsAdminV1betaAccessRowOut",
        "GoogleAnalyticsAdminV1betaChangeHistoryChangeIn": "_analyticsadmin_24_GoogleAnalyticsAdminV1betaChangeHistoryChangeIn",
        "GoogleAnalyticsAdminV1betaChangeHistoryChangeOut": "_analyticsadmin_25_GoogleAnalyticsAdminV1betaChangeHistoryChangeOut",
        "GoogleAnalyticsAdminV1betaAccessOrderByIn": "_analyticsadmin_26_GoogleAnalyticsAdminV1betaAccessOrderByIn",
        "GoogleAnalyticsAdminV1betaAccessOrderByOut": "_analyticsadmin_27_GoogleAnalyticsAdminV1betaAccessOrderByOut",
        "GoogleAnalyticsAdminV1betaConversionEventIn": "_analyticsadmin_28_GoogleAnalyticsAdminV1betaConversionEventIn",
        "GoogleAnalyticsAdminV1betaConversionEventOut": "_analyticsadmin_29_GoogleAnalyticsAdminV1betaConversionEventOut",
        "GoogleProtobufEmptyIn": "_analyticsadmin_30_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_analyticsadmin_31_GoogleProtobufEmptyOut",
        "GoogleAnalyticsAdminV1betaFirebaseLinkIn": "_analyticsadmin_32_GoogleAnalyticsAdminV1betaFirebaseLinkIn",
        "GoogleAnalyticsAdminV1betaFirebaseLinkOut": "_analyticsadmin_33_GoogleAnalyticsAdminV1betaFirebaseLinkOut",
        "GoogleAnalyticsAdminV1betaAccessMetricValueIn": "_analyticsadmin_34_GoogleAnalyticsAdminV1betaAccessMetricValueIn",
        "GoogleAnalyticsAdminV1betaAccessMetricValueOut": "_analyticsadmin_35_GoogleAnalyticsAdminV1betaAccessMetricValueOut",
        "GoogleAnalyticsAdminV1betaChangeHistoryEventIn": "_analyticsadmin_36_GoogleAnalyticsAdminV1betaChangeHistoryEventIn",
        "GoogleAnalyticsAdminV1betaChangeHistoryEventOut": "_analyticsadmin_37_GoogleAnalyticsAdminV1betaChangeHistoryEventOut",
        "GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseIn": "_analyticsadmin_38_GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseIn",
        "GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseOut": "_analyticsadmin_39_GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseOut",
        "GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn": "_analyticsadmin_40_GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn",
        "GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataOut": "_analyticsadmin_41_GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataOut",
        "GoogleAnalyticsAdminV1betaGoogleAdsLinkIn": "_analyticsadmin_42_GoogleAnalyticsAdminV1betaGoogleAdsLinkIn",
        "GoogleAnalyticsAdminV1betaGoogleAdsLinkOut": "_analyticsadmin_43_GoogleAnalyticsAdminV1betaGoogleAdsLinkOut",
        "GoogleAnalyticsAdminV1betaListAccountsResponseIn": "_analyticsadmin_44_GoogleAnalyticsAdminV1betaListAccountsResponseIn",
        "GoogleAnalyticsAdminV1betaListAccountsResponseOut": "_analyticsadmin_45_GoogleAnalyticsAdminV1betaListAccountsResponseOut",
        "GoogleAnalyticsAdminV1betaListDataStreamsResponseIn": "_analyticsadmin_46_GoogleAnalyticsAdminV1betaListDataStreamsResponseIn",
        "GoogleAnalyticsAdminV1betaListDataStreamsResponseOut": "_analyticsadmin_47_GoogleAnalyticsAdminV1betaListDataStreamsResponseOut",
        "GoogleAnalyticsAdminV1betaNumericValueIn": "_analyticsadmin_48_GoogleAnalyticsAdminV1betaNumericValueIn",
        "GoogleAnalyticsAdminV1betaNumericValueOut": "_analyticsadmin_49_GoogleAnalyticsAdminV1betaNumericValueOut",
        "GoogleAnalyticsAdminV1betaAccessDimensionHeaderIn": "_analyticsadmin_50_GoogleAnalyticsAdminV1betaAccessDimensionHeaderIn",
        "GoogleAnalyticsAdminV1betaAccessDimensionHeaderOut": "_analyticsadmin_51_GoogleAnalyticsAdminV1betaAccessDimensionHeaderOut",
        "GoogleAnalyticsAdminV1betaListCustomMetricsResponseIn": "_analyticsadmin_52_GoogleAnalyticsAdminV1betaListCustomMetricsResponseIn",
        "GoogleAnalyticsAdminV1betaListCustomMetricsResponseOut": "_analyticsadmin_53_GoogleAnalyticsAdminV1betaListCustomMetricsResponseOut",
        "GoogleAnalyticsAdminV1betaCustomDimensionIn": "_analyticsadmin_54_GoogleAnalyticsAdminV1betaCustomDimensionIn",
        "GoogleAnalyticsAdminV1betaCustomDimensionOut": "_analyticsadmin_55_GoogleAnalyticsAdminV1betaCustomDimensionOut",
        "GoogleAnalyticsAdminV1betaAccessMetricHeaderIn": "_analyticsadmin_56_GoogleAnalyticsAdminV1betaAccessMetricHeaderIn",
        "GoogleAnalyticsAdminV1betaAccessMetricHeaderOut": "_analyticsadmin_57_GoogleAnalyticsAdminV1betaAccessMetricHeaderOut",
        "GoogleAnalyticsAdminV1betaAccessNumericFilterIn": "_analyticsadmin_58_GoogleAnalyticsAdminV1betaAccessNumericFilterIn",
        "GoogleAnalyticsAdminV1betaAccessNumericFilterOut": "_analyticsadmin_59_GoogleAnalyticsAdminV1betaAccessNumericFilterOut",
        "GoogleAnalyticsAdminV1betaCustomMetricIn": "_analyticsadmin_60_GoogleAnalyticsAdminV1betaCustomMetricIn",
        "GoogleAnalyticsAdminV1betaCustomMetricOut": "_analyticsadmin_61_GoogleAnalyticsAdminV1betaCustomMetricOut",
        "GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseIn": "_analyticsadmin_62_GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseIn",
        "GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut": "_analyticsadmin_63_GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut",
        "GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByIn": "_analyticsadmin_64_GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByIn",
        "GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByOut": "_analyticsadmin_65_GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByOut",
        "GoogleAnalyticsAdminV1betaAccessFilterExpressionListIn": "_analyticsadmin_66_GoogleAnalyticsAdminV1betaAccessFilterExpressionListIn",
        "GoogleAnalyticsAdminV1betaAccessFilterExpressionListOut": "_analyticsadmin_67_GoogleAnalyticsAdminV1betaAccessFilterExpressionListOut",
        "GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn": "_analyticsadmin_68_GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn",
        "GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataOut": "_analyticsadmin_69_GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataOut",
        "GoogleAnalyticsAdminV1betaDataStreamIn": "_analyticsadmin_70_GoogleAnalyticsAdminV1betaDataStreamIn",
        "GoogleAnalyticsAdminV1betaDataStreamOut": "_analyticsadmin_71_GoogleAnalyticsAdminV1betaDataStreamOut",
        "GoogleAnalyticsAdminV1betaAccessInListFilterIn": "_analyticsadmin_72_GoogleAnalyticsAdminV1betaAccessInListFilterIn",
        "GoogleAnalyticsAdminV1betaAccessInListFilterOut": "_analyticsadmin_73_GoogleAnalyticsAdminV1betaAccessInListFilterOut",
        "GoogleAnalyticsAdminV1betaAccessBetweenFilterIn": "_analyticsadmin_74_GoogleAnalyticsAdminV1betaAccessBetweenFilterIn",
        "GoogleAnalyticsAdminV1betaAccessBetweenFilterOut": "_analyticsadmin_75_GoogleAnalyticsAdminV1betaAccessBetweenFilterOut",
        "GoogleAnalyticsAdminV1betaAccountSummaryIn": "_analyticsadmin_76_GoogleAnalyticsAdminV1betaAccountSummaryIn",
        "GoogleAnalyticsAdminV1betaAccountSummaryOut": "_analyticsadmin_77_GoogleAnalyticsAdminV1betaAccountSummaryOut",
        "GoogleAnalyticsAdminV1betaListCustomDimensionsResponseIn": "_analyticsadmin_78_GoogleAnalyticsAdminV1betaListCustomDimensionsResponseIn",
        "GoogleAnalyticsAdminV1betaListCustomDimensionsResponseOut": "_analyticsadmin_79_GoogleAnalyticsAdminV1betaListCustomDimensionsResponseOut",
        "GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByIn": "_analyticsadmin_80_GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByIn",
        "GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByOut": "_analyticsadmin_81_GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByOut",
        "GoogleAnalyticsAdminV1betaAccessQuotaIn": "_analyticsadmin_82_GoogleAnalyticsAdminV1betaAccessQuotaIn",
        "GoogleAnalyticsAdminV1betaAccessQuotaOut": "_analyticsadmin_83_GoogleAnalyticsAdminV1betaAccessQuotaOut",
        "GoogleAnalyticsAdminV1betaRunAccessReportRequestIn": "_analyticsadmin_84_GoogleAnalyticsAdminV1betaRunAccessReportRequestIn",
        "GoogleAnalyticsAdminV1betaRunAccessReportRequestOut": "_analyticsadmin_85_GoogleAnalyticsAdminV1betaRunAccessReportRequestOut",
        "GoogleAnalyticsAdminV1betaAccessFilterIn": "_analyticsadmin_86_GoogleAnalyticsAdminV1betaAccessFilterIn",
        "GoogleAnalyticsAdminV1betaAccessFilterOut": "_analyticsadmin_87_GoogleAnalyticsAdminV1betaAccessFilterOut",
        "GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponseIn": "_analyticsadmin_88_GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponseIn",
        "GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponseOut": "_analyticsadmin_89_GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponseOut",
        "GoogleAnalyticsAdminV1betaAccessQuotaStatusIn": "_analyticsadmin_90_GoogleAnalyticsAdminV1betaAccessQuotaStatusIn",
        "GoogleAnalyticsAdminV1betaAccessQuotaStatusOut": "_analyticsadmin_91_GoogleAnalyticsAdminV1betaAccessQuotaStatusOut",
        "GoogleAnalyticsAdminV1betaAccessFilterExpressionIn": "_analyticsadmin_92_GoogleAnalyticsAdminV1betaAccessFilterExpressionIn",
        "GoogleAnalyticsAdminV1betaAccessFilterExpressionOut": "_analyticsadmin_93_GoogleAnalyticsAdminV1betaAccessFilterExpressionOut",
        "GoogleAnalyticsAdminV1betaPropertyIn": "_analyticsadmin_94_GoogleAnalyticsAdminV1betaPropertyIn",
        "GoogleAnalyticsAdminV1betaPropertyOut": "_analyticsadmin_95_GoogleAnalyticsAdminV1betaPropertyOut",
        "GoogleAnalyticsAdminV1betaAccessMetricIn": "_analyticsadmin_96_GoogleAnalyticsAdminV1betaAccessMetricIn",
        "GoogleAnalyticsAdminV1betaAccessMetricOut": "_analyticsadmin_97_GoogleAnalyticsAdminV1betaAccessMetricOut",
        "GoogleAnalyticsAdminV1betaDataRetentionSettingsIn": "_analyticsadmin_98_GoogleAnalyticsAdminV1betaDataRetentionSettingsIn",
        "GoogleAnalyticsAdminV1betaDataRetentionSettingsOut": "_analyticsadmin_99_GoogleAnalyticsAdminV1betaDataRetentionSettingsOut",
        "GoogleAnalyticsAdminV1betaDataSharingSettingsIn": "_analyticsadmin_100_GoogleAnalyticsAdminV1betaDataSharingSettingsIn",
        "GoogleAnalyticsAdminV1betaDataSharingSettingsOut": "_analyticsadmin_101_GoogleAnalyticsAdminV1betaDataSharingSettingsOut",
        "GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseIn": "_analyticsadmin_102_GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseIn",
        "GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseOut": "_analyticsadmin_103_GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseOut",
        "GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestIn": "_analyticsadmin_104_GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestIn",
        "GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestOut": "_analyticsadmin_105_GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestOut",
        "GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestIn": "_analyticsadmin_106_GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestIn",
        "GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestOut": "_analyticsadmin_107_GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestOut",
        "GoogleAnalyticsAdminV1betaAccountIn": "_analyticsadmin_108_GoogleAnalyticsAdminV1betaAccountIn",
        "GoogleAnalyticsAdminV1betaAccountOut": "_analyticsadmin_109_GoogleAnalyticsAdminV1betaAccountOut",
        "GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseIn": "_analyticsadmin_110_GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseIn",
        "GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseOut": "_analyticsadmin_111_GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseOut",
        "GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn": "_analyticsadmin_112_GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn",
        "GoogleAnalyticsAdminV1betaDataStreamWebStreamDataOut": "_analyticsadmin_113_GoogleAnalyticsAdminV1betaDataStreamWebStreamDataOut",
        "GoogleAnalyticsAdminV1betaMeasurementProtocolSecretIn": "_analyticsadmin_114_GoogleAnalyticsAdminV1betaMeasurementProtocolSecretIn",
        "GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut": "_analyticsadmin_115_GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut",
        "GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestIn": "_analyticsadmin_116_GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestIn",
        "GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestOut": "_analyticsadmin_117_GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestOut",
        "GoogleAnalyticsAdminV1betaRunAccessReportResponseIn": "_analyticsadmin_118_GoogleAnalyticsAdminV1betaRunAccessReportResponseIn",
        "GoogleAnalyticsAdminV1betaRunAccessReportResponseOut": "_analyticsadmin_119_GoogleAnalyticsAdminV1betaRunAccessReportResponseOut",
        "GoogleAnalyticsAdminV1betaPropertySummaryIn": "_analyticsadmin_120_GoogleAnalyticsAdminV1betaPropertySummaryIn",
        "GoogleAnalyticsAdminV1betaPropertySummaryOut": "_analyticsadmin_121_GoogleAnalyticsAdminV1betaPropertySummaryOut",
        "GoogleAnalyticsAdminV1betaListAccountSummariesResponseIn": "_analyticsadmin_122_GoogleAnalyticsAdminV1betaListAccountSummariesResponseIn",
        "GoogleAnalyticsAdminV1betaListAccountSummariesResponseOut": "_analyticsadmin_123_GoogleAnalyticsAdminV1betaListAccountSummariesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleAnalyticsAdminV1betaAccessStringFilterIn"] = t.struct(
        {
            "value": t.string().optional(),
            "matchType": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessStringFilterIn"])
    types["GoogleAnalyticsAdminV1betaAccessStringFilterOut"] = t.struct(
        {
            "value": t.string().optional(),
            "matchType": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessStringFilterOut"])
    types["GoogleAnalyticsAdminV1betaListFirebaseLinksResponseIn"] = t.struct(
        {
            "firebaseLinks": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaFirebaseLinkIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListFirebaseLinksResponseIn"])
    types["GoogleAnalyticsAdminV1betaListFirebaseLinksResponseOut"] = t.struct(
        {
            "firebaseLinks": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaFirebaseLinkOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListFirebaseLinksResponseOut"])
    types["GoogleAnalyticsAdminV1betaAccessDimensionValueIn"] = t.struct(
        {"value": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDimensionValueIn"])
    types["GoogleAnalyticsAdminV1betaAccessDimensionValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDimensionValueOut"])
    types["GoogleAnalyticsAdminV1betaListConversionEventsResponseIn"] = t.struct(
        {
            "conversionEvents": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaConversionEventIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListConversionEventsResponseIn"])
    types["GoogleAnalyticsAdminV1betaListConversionEventsResponseOut"] = t.struct(
        {
            "conversionEvents": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaConversionEventOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListConversionEventsResponseOut"])
    types["GoogleAnalyticsAdminV1betaAccessDateRangeIn"] = t.struct(
        {"endDate": t.string().optional(), "startDate": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
    types["GoogleAnalyticsAdminV1betaAccessDateRangeOut"] = t.struct(
        {
            "endDate": t.string().optional(),
            "startDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDateRangeOut"])
    types["GoogleAnalyticsAdminV1betaAccessDimensionIn"] = t.struct(
        {"dimensionName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
    types["GoogleAnalyticsAdminV1betaAccessDimensionOut"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDimensionOut"])
    types[
        "GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequestIn"
    ] = t.struct({"acknowledgement": t.string()}).named(
        renames["GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequestIn"]
    )
    types[
        "GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequestOut"
    ] = t.struct(
        {
            "acknowledgement": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequestOut"]
    )
    types[
        "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceIn"
    ] = t.struct(
        {
            "account": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccountIn"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleAnalyticsAdminV1betaPropertyIn"]
            ).optional(),
            "firebaseLink": t.proxy(
                renames["GoogleAnalyticsAdminV1betaFirebaseLinkIn"]
            ).optional(),
            "conversionEvent": t.proxy(
                renames["GoogleAnalyticsAdminV1betaConversionEventIn"]
            ).optional(),
            "dataStream": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamIn"]
            ).optional(),
            "googleAdsLink": t.proxy(
                renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkIn"]
            ).optional(),
            "dataRetentionSettings": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsIn"]
            ).optional(),
            "measurementProtocolSecret": t.proxy(
                renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretIn"]
            ).optional(),
        }
    ).named(
        renames["GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceIn"]
    )
    types[
        "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceOut"
    ] = t.struct(
        {
            "account": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccountOut"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleAnalyticsAdminV1betaPropertyOut"]
            ).optional(),
            "firebaseLink": t.proxy(
                renames["GoogleAnalyticsAdminV1betaFirebaseLinkOut"]
            ).optional(),
            "conversionEvent": t.proxy(
                renames["GoogleAnalyticsAdminV1betaConversionEventOut"]
            ).optional(),
            "dataStream": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamOut"]
            ).optional(),
            "googleAdsLink": t.proxy(
                renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"]
            ).optional(),
            "dataRetentionSettings": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsOut"]
            ).optional(),
            "measurementProtocolSecret": t.proxy(
                renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceOut"]
    )
    types["GoogleAnalyticsAdminV1betaListPropertiesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaPropertyIn"])
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListPropertiesResponseIn"])
    types["GoogleAnalyticsAdminV1betaListPropertiesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaPropertyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListPropertiesResponseOut"])
    types["GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestIn"])
    types["GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestOut"])
    types["GoogleAnalyticsAdminV1betaAccessRowIn"] = t.struct(
        {
            "metricValues": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricValueIn"])
            ).optional(),
            "dimensionValues": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionValueIn"])
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessRowIn"])
    types["GoogleAnalyticsAdminV1betaAccessRowOut"] = t.struct(
        {
            "metricValues": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricValueOut"])
            ).optional(),
            "dimensionValues": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionValueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessRowOut"])
    types["GoogleAnalyticsAdminV1betaChangeHistoryChangeIn"] = t.struct(
        {
            "resourceBeforeChange": t.proxy(
                renames[
                    "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceIn"
                ]
            ).optional(),
            "action": t.string().optional(),
            "resourceAfterChange": t.proxy(
                renames[
                    "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceIn"
                ]
            ).optional(),
            "resource": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaChangeHistoryChangeIn"])
    types["GoogleAnalyticsAdminV1betaChangeHistoryChangeOut"] = t.struct(
        {
            "resourceBeforeChange": t.proxy(
                renames[
                    "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceOut"
                ]
            ).optional(),
            "action": t.string().optional(),
            "resourceAfterChange": t.proxy(
                renames[
                    "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceOut"
                ]
            ).optional(),
            "resource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaChangeHistoryChangeOut"])
    types["GoogleAnalyticsAdminV1betaAccessOrderByIn"] = t.struct(
        {
            "metric": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByIn"]
            ).optional(),
            "desc": t.boolean().optional(),
            "dimension": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByIn"]
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
    types["GoogleAnalyticsAdminV1betaAccessOrderByOut"] = t.struct(
        {
            "metric": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByOut"]
            ).optional(),
            "desc": t.boolean().optional(),
            "dimension": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessOrderByOut"])
    types["GoogleAnalyticsAdminV1betaConversionEventIn"] = t.struct(
        {"eventName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaConversionEventIn"])
    types["GoogleAnalyticsAdminV1betaConversionEventOut"] = t.struct(
        {
            "name": t.string().optional(),
            "eventName": t.string().optional(),
            "deletable": t.boolean().optional(),
            "createTime": t.string().optional(),
            "custom": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaConversionEventOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleAnalyticsAdminV1betaFirebaseLinkIn"] = t.struct(
        {"project": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaFirebaseLinkIn"])
    types["GoogleAnalyticsAdminV1betaFirebaseLinkOut"] = t.struct(
        {
            "name": t.string().optional(),
            "project": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaFirebaseLinkOut"])
    types["GoogleAnalyticsAdminV1betaAccessMetricValueIn"] = t.struct(
        {"value": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessMetricValueIn"])
    types["GoogleAnalyticsAdminV1betaAccessMetricValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessMetricValueOut"])
    types["GoogleAnalyticsAdminV1betaChangeHistoryEventIn"] = t.struct(
        {
            "changesFiltered": t.boolean().optional(),
            "id": t.string().optional(),
            "userActorEmail": t.string().optional(),
            "changes": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaChangeHistoryChangeIn"])
            ).optional(),
            "actorType": t.string().optional(),
            "changeTime": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaChangeHistoryEventIn"])
    types["GoogleAnalyticsAdminV1betaChangeHistoryEventOut"] = t.struct(
        {
            "changesFiltered": t.boolean().optional(),
            "id": t.string().optional(),
            "userActorEmail": t.string().optional(),
            "changes": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaChangeHistoryChangeOut"])
            ).optional(),
            "actorType": t.string().optional(),
            "changeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaChangeHistoryEventOut"])
    types["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "changeHistoryEvents": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaChangeHistoryEventIn"])
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseIn"])
    types["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "changeHistoryEvents": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaChangeHistoryEventOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseOut"])
    types["GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn"] = t.struct(
        {"packageName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn"])
    types["GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataOut"] = t.struct(
        {
            "firebaseAppId": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataOut"])
    types["GoogleAnalyticsAdminV1betaGoogleAdsLinkIn"] = t.struct(
        {
            "adsPersonalizationEnabled": t.boolean().optional(),
            "customerId": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkIn"])
    types["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"] = t.struct(
        {
            "canManageClients": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "adsPersonalizationEnabled": t.boolean().optional(),
            "createTime": t.string().optional(),
            "creatorEmailAddress": t.string().optional(),
            "customerId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"])
    types["GoogleAnalyticsAdminV1betaListAccountsResponseIn"] = t.struct(
        {
            "accounts": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccountIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListAccountsResponseIn"])
    types["GoogleAnalyticsAdminV1betaListAccountsResponseOut"] = t.struct(
        {
            "accounts": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccountOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListAccountsResponseOut"])
    types["GoogleAnalyticsAdminV1betaListDataStreamsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dataStreams": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaDataStreamIn"])
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListDataStreamsResponseIn"])
    types["GoogleAnalyticsAdminV1betaListDataStreamsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dataStreams": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaDataStreamOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListDataStreamsResponseOut"])
    types["GoogleAnalyticsAdminV1betaNumericValueIn"] = t.struct(
        {"doubleValue": t.number().optional(), "int64Value": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaNumericValueIn"])
    types["GoogleAnalyticsAdminV1betaNumericValueOut"] = t.struct(
        {
            "doubleValue": t.number().optional(),
            "int64Value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaNumericValueOut"])
    types["GoogleAnalyticsAdminV1betaAccessDimensionHeaderIn"] = t.struct(
        {"dimensionName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDimensionHeaderIn"])
    types["GoogleAnalyticsAdminV1betaAccessDimensionHeaderOut"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDimensionHeaderOut"])
    types["GoogleAnalyticsAdminV1betaListCustomMetricsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customMetrics": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaCustomMetricIn"])
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListCustomMetricsResponseIn"])
    types["GoogleAnalyticsAdminV1betaListCustomMetricsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customMetrics": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaCustomMetricOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListCustomMetricsResponseOut"])
    types["GoogleAnalyticsAdminV1betaCustomDimensionIn"] = t.struct(
        {
            "description": t.string().optional(),
            "scope": t.string(),
            "displayName": t.string(),
            "parameterName": t.string(),
            "disallowAdsPersonalization": t.boolean().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaCustomDimensionIn"])
    types["GoogleAnalyticsAdminV1betaCustomDimensionOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "scope": t.string(),
            "displayName": t.string(),
            "parameterName": t.string(),
            "disallowAdsPersonalization": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaCustomDimensionOut"])
    types["GoogleAnalyticsAdminV1betaAccessMetricHeaderIn"] = t.struct(
        {"metricName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessMetricHeaderIn"])
    types["GoogleAnalyticsAdminV1betaAccessMetricHeaderOut"] = t.struct(
        {
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessMetricHeaderOut"])
    types["GoogleAnalyticsAdminV1betaAccessNumericFilterIn"] = t.struct(
        {
            "value": t.proxy(
                renames["GoogleAnalyticsAdminV1betaNumericValueIn"]
            ).optional(),
            "operation": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessNumericFilterIn"])
    types["GoogleAnalyticsAdminV1betaAccessNumericFilterOut"] = t.struct(
        {
            "value": t.proxy(
                renames["GoogleAnalyticsAdminV1betaNumericValueOut"]
            ).optional(),
            "operation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessNumericFilterOut"])
    types["GoogleAnalyticsAdminV1betaCustomMetricIn"] = t.struct(
        {
            "measurementUnit": t.string(),
            "restrictedMetricType": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "scope": t.string(),
            "parameterName": t.string(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaCustomMetricIn"])
    types["GoogleAnalyticsAdminV1betaCustomMetricOut"] = t.struct(
        {
            "measurementUnit": t.string(),
            "restrictedMetricType": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "scope": t.string(),
            "parameterName": t.string(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaCustomMetricOut"])
    types["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseIn"] = t.struct(
        {"accountTicketId": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseIn"])
    types["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut"] = t.struct(
        {
            "accountTicketId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut"])
    types["GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByIn"] = t.struct(
        {"orderType": t.string().optional(), "dimensionName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByIn"])
    types["GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByOut"] = t.struct(
        {
            "orderType": t.string().optional(),
            "dimensionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByOut"])
    types["GoogleAnalyticsAdminV1betaAccessFilterExpressionListIn"] = t.struct(
        {
            "expressions": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"])
            ).optional()
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionListIn"])
    types["GoogleAnalyticsAdminV1betaAccessFilterExpressionListOut"] = t.struct(
        {
            "expressions": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionListOut"])
    types["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn"] = t.struct(
        {"bundleId": t.string()}
    ).named(renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn"])
    types["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataOut"] = t.struct(
        {
            "firebaseAppId": t.string().optional(),
            "bundleId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataOut"])
    types["GoogleAnalyticsAdminV1betaDataStreamIn"] = t.struct(
        {
            "iosAppStreamData": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "androidAppStreamData": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn"]
            ).optional(),
            "type": t.string(),
            "webStreamData": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn"]
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataStreamIn"])
    types["GoogleAnalyticsAdminV1betaDataStreamOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "iosAppStreamData": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "androidAppStreamData": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataOut"]
            ).optional(),
            "name": t.string().optional(),
            "type": t.string(),
            "webStreamData": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataStreamOut"])
    types["GoogleAnalyticsAdminV1betaAccessInListFilterIn"] = t.struct(
        {
            "caseSensitive": t.boolean().optional(),
            "values": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessInListFilterIn"])
    types["GoogleAnalyticsAdminV1betaAccessInListFilterOut"] = t.struct(
        {
            "caseSensitive": t.boolean().optional(),
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessInListFilterOut"])
    types["GoogleAnalyticsAdminV1betaAccessBetweenFilterIn"] = t.struct(
        {
            "toValue": t.proxy(
                renames["GoogleAnalyticsAdminV1betaNumericValueIn"]
            ).optional(),
            "fromValue": t.proxy(
                renames["GoogleAnalyticsAdminV1betaNumericValueIn"]
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessBetweenFilterIn"])
    types["GoogleAnalyticsAdminV1betaAccessBetweenFilterOut"] = t.struct(
        {
            "toValue": t.proxy(
                renames["GoogleAnalyticsAdminV1betaNumericValueOut"]
            ).optional(),
            "fromValue": t.proxy(
                renames["GoogleAnalyticsAdminV1betaNumericValueOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessBetweenFilterOut"])
    types["GoogleAnalyticsAdminV1betaAccountSummaryIn"] = t.struct(
        {
            "propertySummaries": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaPropertySummaryIn"])
            ).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "account": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccountSummaryIn"])
    types["GoogleAnalyticsAdminV1betaAccountSummaryOut"] = t.struct(
        {
            "propertySummaries": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaPropertySummaryOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "account": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccountSummaryOut"])
    types["GoogleAnalyticsAdminV1betaListCustomDimensionsResponseIn"] = t.struct(
        {
            "customDimensions": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaCustomDimensionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListCustomDimensionsResponseIn"])
    types["GoogleAnalyticsAdminV1betaListCustomDimensionsResponseOut"] = t.struct(
        {
            "customDimensions": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaCustomDimensionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListCustomDimensionsResponseOut"])
    types["GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByIn"] = t.struct(
        {"metricName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByIn"])
    types["GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByOut"] = t.struct(
        {
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByOut"])
    types["GoogleAnalyticsAdminV1betaAccessQuotaIn"] = t.struct(
        {
            "tokensPerProjectPerHour": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusIn"]
            ).optional(),
            "concurrentRequests": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusIn"]
            ).optional(),
            "tokensPerHour": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusIn"]
            ).optional(),
            "serverErrorsPerProjectPerHour": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusIn"]
            ).optional(),
            "tokensPerDay": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusIn"]
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessQuotaIn"])
    types["GoogleAnalyticsAdminV1betaAccessQuotaOut"] = t.struct(
        {
            "tokensPerProjectPerHour": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusOut"]
            ).optional(),
            "concurrentRequests": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusOut"]
            ).optional(),
            "tokensPerHour": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusOut"]
            ).optional(),
            "serverErrorsPerProjectPerHour": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusOut"]
            ).optional(),
            "tokensPerDay": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessQuotaOut"])
    types["GoogleAnalyticsAdminV1betaRunAccessReportRequestIn"] = t.struct(
        {
            "metrics": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
            ).optional(),
            "dimensionFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
            ).optional(),
            "timeZone": t.string().optional(),
            "dateRanges": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
            ).optional(),
            "limit": t.string().optional(),
            "returnEntityQuota": t.boolean().optional(),
            "metricFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
            ).optional(),
            "orderBys": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
            ).optional(),
            "dimensions": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
            ).optional(),
            "offset": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaRunAccessReportRequestIn"])
    types["GoogleAnalyticsAdminV1betaRunAccessReportRequestOut"] = t.struct(
        {
            "metrics": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricOut"])
            ).optional(),
            "dimensionFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionOut"]
            ).optional(),
            "timeZone": t.string().optional(),
            "dateRanges": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeOut"])
            ).optional(),
            "limit": t.string().optional(),
            "returnEntityQuota": t.boolean().optional(),
            "metricFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionOut"]
            ).optional(),
            "orderBys": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByOut"])
            ).optional(),
            "dimensions": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionOut"])
            ).optional(),
            "offset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaRunAccessReportRequestOut"])
    types["GoogleAnalyticsAdminV1betaAccessFilterIn"] = t.struct(
        {
            "numericFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessNumericFilterIn"]
            ).optional(),
            "stringFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessStringFilterIn"]
            ).optional(),
            "fieldName": t.string().optional(),
            "inListFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessInListFilterIn"]
            ).optional(),
            "betweenFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessBetweenFilterIn"]
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessFilterIn"])
    types["GoogleAnalyticsAdminV1betaAccessFilterOut"] = t.struct(
        {
            "numericFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessNumericFilterOut"]
            ).optional(),
            "stringFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessStringFilterOut"]
            ).optional(),
            "fieldName": t.string().optional(),
            "inListFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessInListFilterOut"]
            ).optional(),
            "betweenFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessBetweenFilterOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessFilterOut"])
    types[
        "GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponseIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponseIn"]
    )
    types[
        "GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponseOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponseOut"]
    )
    types["GoogleAnalyticsAdminV1betaAccessQuotaStatusIn"] = t.struct(
        {"consumed": t.integer().optional(), "remaining": t.integer().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusIn"])
    types["GoogleAnalyticsAdminV1betaAccessQuotaStatusOut"] = t.struct(
        {
            "consumed": t.integer().optional(),
            "remaining": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusOut"])
    types["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"] = t.struct(
        {
            "orGroup": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionListIn"]
            ).optional(),
            "notExpression": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
            ).optional(),
            "andGroup": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionListIn"]
            ).optional(),
            "accessFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterIn"]
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"])
    types["GoogleAnalyticsAdminV1betaAccessFilterExpressionOut"] = t.struct(
        {
            "orGroup": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionListOut"]
            ).optional(),
            "notExpression": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionOut"]
            ).optional(),
            "andGroup": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionListOut"]
            ).optional(),
            "accessFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionOut"])
    types["GoogleAnalyticsAdminV1betaPropertyIn"] = t.struct(
        {
            "timeZone": t.string(),
            "account": t.string().optional(),
            "propertyType": t.string().optional(),
            "parent": t.string().optional(),
            "displayName": t.string(),
            "industryCategory": t.string().optional(),
            "currencyCode": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaPropertyIn"])
    types["GoogleAnalyticsAdminV1betaPropertyOut"] = t.struct(
        {
            "timeZone": t.string(),
            "deleteTime": t.string().optional(),
            "serviceLevel": t.string().optional(),
            "account": t.string().optional(),
            "propertyType": t.string().optional(),
            "parent": t.string().optional(),
            "displayName": t.string(),
            "industryCategory": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "currencyCode": t.string().optional(),
            "name": t.string().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaPropertyOut"])
    types["GoogleAnalyticsAdminV1betaAccessMetricIn"] = t.struct(
        {"metricName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
    types["GoogleAnalyticsAdminV1betaAccessMetricOut"] = t.struct(
        {
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessMetricOut"])
    types["GoogleAnalyticsAdminV1betaDataRetentionSettingsIn"] = t.struct(
        {
            "resetUserDataOnNewActivity": t.boolean().optional(),
            "eventDataRetention": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsIn"])
    types["GoogleAnalyticsAdminV1betaDataRetentionSettingsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "resetUserDataOnNewActivity": t.boolean().optional(),
            "eventDataRetention": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsOut"])
    types["GoogleAnalyticsAdminV1betaDataSharingSettingsIn"] = t.struct(
        {
            "sharingWithGoogleProductsEnabled": t.boolean().optional(),
            "sharingWithGoogleSupportEnabled": t.boolean().optional(),
            "sharingWithGoogleAssignedSalesEnabled": t.boolean().optional(),
            "sharingWithGoogleAnySalesEnabled": t.boolean().optional(),
            "sharingWithOthersEnabled": t.boolean().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataSharingSettingsIn"])
    types["GoogleAnalyticsAdminV1betaDataSharingSettingsOut"] = t.struct(
        {
            "sharingWithGoogleProductsEnabled": t.boolean().optional(),
            "sharingWithGoogleSupportEnabled": t.boolean().optional(),
            "sharingWithGoogleAssignedSalesEnabled": t.boolean().optional(),
            "sharingWithGoogleAnySalesEnabled": t.boolean().optional(),
            "name": t.string().optional(),
            "sharingWithOthersEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataSharingSettingsOut"])
    types["GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseIn"] = t.struct(
        {
            "googleAdsLinks": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseIn"])
    types["GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseOut"] = t.struct(
        {
            "googleAdsLinks": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseOut"])
    types["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestIn"] = t.struct(
        {
            "latestChangeTime": t.string().optional(),
            "pageSize": t.integer().optional(),
            "property": t.string().optional(),
            "resourceType": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "earliestChangeTime": t.string().optional(),
            "action": t.array(t.string()).optional(),
            "actorEmail": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestIn"])
    types["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestOut"] = t.struct(
        {
            "latestChangeTime": t.string().optional(),
            "pageSize": t.integer().optional(),
            "property": t.string().optional(),
            "resourceType": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "earliestChangeTime": t.string().optional(),
            "action": t.array(t.string()).optional(),
            "actorEmail": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestOut"])
    types["GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestIn"])
    types["GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestOut"])
    types["GoogleAnalyticsAdminV1betaAccountIn"] = t.struct(
        {"displayName": t.string(), "regionCode": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccountIn"])
    types["GoogleAnalyticsAdminV1betaAccountOut"] = t.struct(
        {
            "name": t.string().optional(),
            "deleted": t.boolean().optional(),
            "displayName": t.string(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccountOut"])
    types[
        "GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "measurementProtocolSecrets": t.array(
                t.proxy(
                    renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretIn"]
                )
            ).optional(),
        }
    ).named(
        renames["GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseIn"]
    )
    types[
        "GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "measurementProtocolSecrets": t.array(
                t.proxy(
                    renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseOut"]
    )
    types["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn"] = t.struct(
        {"defaultUri": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn"])
    types["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataOut"] = t.struct(
        {
            "measurementId": t.string().optional(),
            "firebaseAppId": t.string().optional(),
            "defaultUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataOut"])
    types["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretIn"] = t.struct(
        {"displayName": t.string()}
    ).named(renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretIn"])
    types["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"] = t.struct(
        {
            "secretValue": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"])
    types["GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestIn"] = t.struct(
        {
            "redirectUri": t.string().optional(),
            "account": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccountIn"]
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestIn"])
    types["GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestOut"] = t.struct(
        {
            "redirectUri": t.string().optional(),
            "account": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccountOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestOut"])
    types["GoogleAnalyticsAdminV1betaRunAccessReportResponseIn"] = t.struct(
        {
            "dimensionHeaders": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionHeaderIn"])
            ).optional(),
            "metricHeaders": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricHeaderIn"])
            ).optional(),
            "rows": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessRowIn"])
            ).optional(),
            "rowCount": t.integer().optional(),
            "quota": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaIn"]
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseIn"])
    types["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"] = t.struct(
        {
            "dimensionHeaders": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionHeaderOut"])
            ).optional(),
            "metricHeaders": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricHeaderOut"])
            ).optional(),
            "rows": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessRowOut"])
            ).optional(),
            "rowCount": t.integer().optional(),
            "quota": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"])
    types["GoogleAnalyticsAdminV1betaPropertySummaryIn"] = t.struct(
        {
            "propertyType": t.string().optional(),
            "displayName": t.string().optional(),
            "parent": t.string().optional(),
            "property": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaPropertySummaryIn"])
    types["GoogleAnalyticsAdminV1betaPropertySummaryOut"] = t.struct(
        {
            "propertyType": t.string().optional(),
            "displayName": t.string().optional(),
            "parent": t.string().optional(),
            "property": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaPropertySummaryOut"])
    types["GoogleAnalyticsAdminV1betaListAccountSummariesResponseIn"] = t.struct(
        {
            "accountSummaries": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccountSummaryIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListAccountSummariesResponseIn"])
    types["GoogleAnalyticsAdminV1betaListAccountSummariesResponseOut"] = t.struct(
        {
            "accountSummaries": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccountSummaryOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListAccountSummariesResponseOut"])

    functions = {}
    functions["propertiesAcknowledgeUserDataCollection"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesDelete"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesList"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesPatch"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCreate"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesUpdateDataRetentionSettings"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesRunAccessReport"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGet"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGetDataRetentionSettings"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomDimensionsGet"] = analyticsadmin.post(
        "v1beta/{name}:archive",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomDimensionsPatch"] = analyticsadmin.post(
        "v1beta/{name}:archive",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomDimensionsCreate"] = analyticsadmin.post(
        "v1beta/{name}:archive",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomDimensionsList"] = analyticsadmin.post(
        "v1beta/{name}:archive",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomDimensionsArchive"] = analyticsadmin.post(
        "v1beta/{name}:archive",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGoogleAdsLinksDelete"] = analyticsadmin.post(
        "v1beta/{parent}/googleAdsLinks",
        t.struct(
            {
                "parent": t.string(),
                "adsPersonalizationEnabled": t.boolean().optional(),
                "customerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGoogleAdsLinksPatch"] = analyticsadmin.post(
        "v1beta/{parent}/googleAdsLinks",
        t.struct(
            {
                "parent": t.string(),
                "adsPersonalizationEnabled": t.boolean().optional(),
                "customerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGoogleAdsLinksList"] = analyticsadmin.post(
        "v1beta/{parent}/googleAdsLinks",
        t.struct(
            {
                "parent": t.string(),
                "adsPersonalizationEnabled": t.boolean().optional(),
                "customerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGoogleAdsLinksCreate"] = analyticsadmin.post(
        "v1beta/{parent}/googleAdsLinks",
        t.struct(
            {
                "parent": t.string(),
                "adsPersonalizationEnabled": t.boolean().optional(),
                "customerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesDataStreamsGet"] = analyticsadmin.patch(
        "v1beta/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "iosAppStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "androidAppStreamData": t.proxy(
                    renames[
                        "GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn"
                    ]
                ).optional(),
                "type": t.string(),
                "webStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaDataStreamOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesDataStreamsDelete"] = analyticsadmin.patch(
        "v1beta/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "iosAppStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "androidAppStreamData": t.proxy(
                    renames[
                        "GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn"
                    ]
                ).optional(),
                "type": t.string(),
                "webStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaDataStreamOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesDataStreamsCreate"] = analyticsadmin.patch(
        "v1beta/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "iosAppStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "androidAppStreamData": t.proxy(
                    renames[
                        "GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn"
                    ]
                ).optional(),
                "type": t.string(),
                "webStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaDataStreamOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesDataStreamsList"] = analyticsadmin.patch(
        "v1beta/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "iosAppStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "androidAppStreamData": t.proxy(
                    renames[
                        "GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn"
                    ]
                ).optional(),
                "type": t.string(),
                "webStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaDataStreamOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesDataStreamsPatch"] = analyticsadmin.patch(
        "v1beta/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "iosAppStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "androidAppStreamData": t.proxy(
                    renames[
                        "GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn"
                    ]
                ).optional(),
                "type": t.string(),
                "webStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaDataStreamOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "propertiesDataStreamsMeasurementProtocolSecretsGet"
    ] = analyticsadmin.get(
        "v1beta/{parent}/measurementProtocolSecrets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "propertiesDataStreamsMeasurementProtocolSecretsPatch"
    ] = analyticsadmin.get(
        "v1beta/{parent}/measurementProtocolSecrets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "propertiesDataStreamsMeasurementProtocolSecretsDelete"
    ] = analyticsadmin.get(
        "v1beta/{parent}/measurementProtocolSecrets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "propertiesDataStreamsMeasurementProtocolSecretsCreate"
    ] = analyticsadmin.get(
        "v1beta/{parent}/measurementProtocolSecrets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "propertiesDataStreamsMeasurementProtocolSecretsList"
    ] = analyticsadmin.get(
        "v1beta/{parent}/measurementProtocolSecrets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomMetricsGet"] = analyticsadmin.post(
        "v1beta/{name}:archive",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomMetricsList"] = analyticsadmin.post(
        "v1beta/{name}:archive",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomMetricsPatch"] = analyticsadmin.post(
        "v1beta/{name}:archive",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomMetricsCreate"] = analyticsadmin.post(
        "v1beta/{name}:archive",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomMetricsArchive"] = analyticsadmin.post(
        "v1beta/{name}:archive",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesFirebaseLinksList"] = analyticsadmin.post(
        "v1beta/{parent}/firebaseLinks",
        t.struct(
            {
                "parent": t.string(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaFirebaseLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesFirebaseLinksDelete"] = analyticsadmin.post(
        "v1beta/{parent}/firebaseLinks",
        t.struct(
            {
                "parent": t.string(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaFirebaseLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesFirebaseLinksCreate"] = analyticsadmin.post(
        "v1beta/{parent}/firebaseLinks",
        t.struct(
            {
                "parent": t.string(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaFirebaseLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesConversionEventsCreate"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaConversionEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesConversionEventsDelete"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaConversionEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesConversionEventsList"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaConversionEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesConversionEventsGet"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaConversionEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsSearchChangeHistoryEvents"] = analyticsadmin.post(
        "v1beta/accounts:provisionAccountTicket",
        t.struct(
            {
                "redirectUri": t.string().optional(),
                "account": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccountIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsGetDataSharingSettings"] = analyticsadmin.post(
        "v1beta/accounts:provisionAccountTicket",
        t.struct(
            {
                "redirectUri": t.string().optional(),
                "account": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccountIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsPatch"] = analyticsadmin.post(
        "v1beta/accounts:provisionAccountTicket",
        t.struct(
            {
                "redirectUri": t.string().optional(),
                "account": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccountIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsGet"] = analyticsadmin.post(
        "v1beta/accounts:provisionAccountTicket",
        t.struct(
            {
                "redirectUri": t.string().optional(),
                "account": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccountIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsRunAccessReport"] = analyticsadmin.post(
        "v1beta/accounts:provisionAccountTicket",
        t.struct(
            {
                "redirectUri": t.string().optional(),
                "account": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccountIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsDelete"] = analyticsadmin.post(
        "v1beta/accounts:provisionAccountTicket",
        t.struct(
            {
                "redirectUri": t.string().optional(),
                "account": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccountIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsList"] = analyticsadmin.post(
        "v1beta/accounts:provisionAccountTicket",
        t.struct(
            {
                "redirectUri": t.string().optional(),
                "account": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccountIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProvisionAccountTicket"] = analyticsadmin.post(
        "v1beta/accounts:provisionAccountTicket",
        t.struct(
            {
                "redirectUri": t.string().optional(),
                "account": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccountIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountSummariesList"] = analyticsadmin.get(
        "v1beta/accountSummaries",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaListAccountSummariesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="analyticsadmin",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
