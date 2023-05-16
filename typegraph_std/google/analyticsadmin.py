from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_analyticsadmin() -> Import:
    analyticsadmin = HTTPRuntime("https://analyticsadmin.googleapis.com/")

    renames = {
        "ErrorResponse": "_analyticsadmin_1_ErrorResponse",
        "GoogleAnalyticsAdminV1betaListDataStreamsResponseIn": "_analyticsadmin_2_GoogleAnalyticsAdminV1betaListDataStreamsResponseIn",
        "GoogleAnalyticsAdminV1betaListDataStreamsResponseOut": "_analyticsadmin_3_GoogleAnalyticsAdminV1betaListDataStreamsResponseOut",
        "GoogleAnalyticsAdminV1betaChangeHistoryChangeIn": "_analyticsadmin_4_GoogleAnalyticsAdminV1betaChangeHistoryChangeIn",
        "GoogleAnalyticsAdminV1betaChangeHistoryChangeOut": "_analyticsadmin_5_GoogleAnalyticsAdminV1betaChangeHistoryChangeOut",
        "GoogleAnalyticsAdminV1betaAccessDimensionValueIn": "_analyticsadmin_6_GoogleAnalyticsAdminV1betaAccessDimensionValueIn",
        "GoogleAnalyticsAdminV1betaAccessDimensionValueOut": "_analyticsadmin_7_GoogleAnalyticsAdminV1betaAccessDimensionValueOut",
        "GoogleAnalyticsAdminV1betaAccessMetricValueIn": "_analyticsadmin_8_GoogleAnalyticsAdminV1betaAccessMetricValueIn",
        "GoogleAnalyticsAdminV1betaAccessMetricValueOut": "_analyticsadmin_9_GoogleAnalyticsAdminV1betaAccessMetricValueOut",
        "GoogleAnalyticsAdminV1betaGoogleAdsLinkIn": "_analyticsadmin_10_GoogleAnalyticsAdminV1betaGoogleAdsLinkIn",
        "GoogleAnalyticsAdminV1betaGoogleAdsLinkOut": "_analyticsadmin_11_GoogleAnalyticsAdminV1betaGoogleAdsLinkOut",
        "GoogleAnalyticsAdminV1betaAccountIn": "_analyticsadmin_12_GoogleAnalyticsAdminV1betaAccountIn",
        "GoogleAnalyticsAdminV1betaAccountOut": "_analyticsadmin_13_GoogleAnalyticsAdminV1betaAccountOut",
        "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceIn": "_analyticsadmin_14_GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceIn",
        "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceOut": "_analyticsadmin_15_GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceOut",
        "GoogleAnalyticsAdminV1betaAccessFilterIn": "_analyticsadmin_16_GoogleAnalyticsAdminV1betaAccessFilterIn",
        "GoogleAnalyticsAdminV1betaAccessFilterOut": "_analyticsadmin_17_GoogleAnalyticsAdminV1betaAccessFilterOut",
        "GoogleAnalyticsAdminV1betaRunAccessReportRequestIn": "_analyticsadmin_18_GoogleAnalyticsAdminV1betaRunAccessReportRequestIn",
        "GoogleAnalyticsAdminV1betaRunAccessReportRequestOut": "_analyticsadmin_19_GoogleAnalyticsAdminV1betaRunAccessReportRequestOut",
        "GoogleAnalyticsAdminV1betaChangeHistoryEventIn": "_analyticsadmin_20_GoogleAnalyticsAdminV1betaChangeHistoryEventIn",
        "GoogleAnalyticsAdminV1betaChangeHistoryEventOut": "_analyticsadmin_21_GoogleAnalyticsAdminV1betaChangeHistoryEventOut",
        "GoogleAnalyticsAdminV1betaAccessQuotaStatusIn": "_analyticsadmin_22_GoogleAnalyticsAdminV1betaAccessQuotaStatusIn",
        "GoogleAnalyticsAdminV1betaAccessQuotaStatusOut": "_analyticsadmin_23_GoogleAnalyticsAdminV1betaAccessQuotaStatusOut",
        "GoogleAnalyticsAdminV1betaFirebaseLinkIn": "_analyticsadmin_24_GoogleAnalyticsAdminV1betaFirebaseLinkIn",
        "GoogleAnalyticsAdminV1betaFirebaseLinkOut": "_analyticsadmin_25_GoogleAnalyticsAdminV1betaFirebaseLinkOut",
        "GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestIn": "_analyticsadmin_26_GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestIn",
        "GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestOut": "_analyticsadmin_27_GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestOut",
        "GoogleAnalyticsAdminV1betaAccessBetweenFilterIn": "_analyticsadmin_28_GoogleAnalyticsAdminV1betaAccessBetweenFilterIn",
        "GoogleAnalyticsAdminV1betaAccessBetweenFilterOut": "_analyticsadmin_29_GoogleAnalyticsAdminV1betaAccessBetweenFilterOut",
        "GoogleAnalyticsAdminV1betaCustomDimensionIn": "_analyticsadmin_30_GoogleAnalyticsAdminV1betaCustomDimensionIn",
        "GoogleAnalyticsAdminV1betaCustomDimensionOut": "_analyticsadmin_31_GoogleAnalyticsAdminV1betaCustomDimensionOut",
        "GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestIn": "_analyticsadmin_32_GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestIn",
        "GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestOut": "_analyticsadmin_33_GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestOut",
        "GoogleAnalyticsAdminV1betaAccessMetricIn": "_analyticsadmin_34_GoogleAnalyticsAdminV1betaAccessMetricIn",
        "GoogleAnalyticsAdminV1betaAccessMetricOut": "_analyticsadmin_35_GoogleAnalyticsAdminV1betaAccessMetricOut",
        "GoogleAnalyticsAdminV1betaListAccountsResponseIn": "_analyticsadmin_36_GoogleAnalyticsAdminV1betaListAccountsResponseIn",
        "GoogleAnalyticsAdminV1betaListAccountsResponseOut": "_analyticsadmin_37_GoogleAnalyticsAdminV1betaListAccountsResponseOut",
        "GoogleAnalyticsAdminV1betaPropertyIn": "_analyticsadmin_38_GoogleAnalyticsAdminV1betaPropertyIn",
        "GoogleAnalyticsAdminV1betaPropertyOut": "_analyticsadmin_39_GoogleAnalyticsAdminV1betaPropertyOut",
        "GoogleAnalyticsAdminV1betaMeasurementProtocolSecretIn": "_analyticsadmin_40_GoogleAnalyticsAdminV1betaMeasurementProtocolSecretIn",
        "GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut": "_analyticsadmin_41_GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut",
        "GoogleAnalyticsAdminV1betaListAccountSummariesResponseIn": "_analyticsadmin_42_GoogleAnalyticsAdminV1betaListAccountSummariesResponseIn",
        "GoogleAnalyticsAdminV1betaListAccountSummariesResponseOut": "_analyticsadmin_43_GoogleAnalyticsAdminV1betaListAccountSummariesResponseOut",
        "GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn": "_analyticsadmin_44_GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn",
        "GoogleAnalyticsAdminV1betaDataStreamWebStreamDataOut": "_analyticsadmin_45_GoogleAnalyticsAdminV1betaDataStreamWebStreamDataOut",
        "GoogleAnalyticsAdminV1betaConversionEventIn": "_analyticsadmin_46_GoogleAnalyticsAdminV1betaConversionEventIn",
        "GoogleAnalyticsAdminV1betaConversionEventOut": "_analyticsadmin_47_GoogleAnalyticsAdminV1betaConversionEventOut",
        "GoogleAnalyticsAdminV1betaNumericValueIn": "_analyticsadmin_48_GoogleAnalyticsAdminV1betaNumericValueIn",
        "GoogleAnalyticsAdminV1betaNumericValueOut": "_analyticsadmin_49_GoogleAnalyticsAdminV1betaNumericValueOut",
        "GoogleAnalyticsAdminV1betaAccessRowIn": "_analyticsadmin_50_GoogleAnalyticsAdminV1betaAccessRowIn",
        "GoogleAnalyticsAdminV1betaAccessRowOut": "_analyticsadmin_51_GoogleAnalyticsAdminV1betaAccessRowOut",
        "GoogleAnalyticsAdminV1betaAccessOrderByIn": "_analyticsadmin_52_GoogleAnalyticsAdminV1betaAccessOrderByIn",
        "GoogleAnalyticsAdminV1betaAccessOrderByOut": "_analyticsadmin_53_GoogleAnalyticsAdminV1betaAccessOrderByOut",
        "GoogleAnalyticsAdminV1betaAccountSummaryIn": "_analyticsadmin_54_GoogleAnalyticsAdminV1betaAccountSummaryIn",
        "GoogleAnalyticsAdminV1betaAccountSummaryOut": "_analyticsadmin_55_GoogleAnalyticsAdminV1betaAccountSummaryOut",
        "GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByIn": "_analyticsadmin_56_GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByIn",
        "GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByOut": "_analyticsadmin_57_GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByOut",
        "GoogleAnalyticsAdminV1betaAccessDimensionHeaderIn": "_analyticsadmin_58_GoogleAnalyticsAdminV1betaAccessDimensionHeaderIn",
        "GoogleAnalyticsAdminV1betaAccessDimensionHeaderOut": "_analyticsadmin_59_GoogleAnalyticsAdminV1betaAccessDimensionHeaderOut",
        "GoogleAnalyticsAdminV1betaAccessInListFilterIn": "_analyticsadmin_60_GoogleAnalyticsAdminV1betaAccessInListFilterIn",
        "GoogleAnalyticsAdminV1betaAccessInListFilterOut": "_analyticsadmin_61_GoogleAnalyticsAdminV1betaAccessInListFilterOut",
        "GoogleAnalyticsAdminV1betaAccessFilterExpressionIn": "_analyticsadmin_62_GoogleAnalyticsAdminV1betaAccessFilterExpressionIn",
        "GoogleAnalyticsAdminV1betaAccessFilterExpressionOut": "_analyticsadmin_63_GoogleAnalyticsAdminV1betaAccessFilterExpressionOut",
        "GoogleAnalyticsAdminV1betaPropertySummaryIn": "_analyticsadmin_64_GoogleAnalyticsAdminV1betaPropertySummaryIn",
        "GoogleAnalyticsAdminV1betaPropertySummaryOut": "_analyticsadmin_65_GoogleAnalyticsAdminV1betaPropertySummaryOut",
        "GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponseIn": "_analyticsadmin_66_GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponseIn",
        "GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponseOut": "_analyticsadmin_67_GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponseOut",
        "GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn": "_analyticsadmin_68_GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn",
        "GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataOut": "_analyticsadmin_69_GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataOut",
        "GoogleAnalyticsAdminV1betaListConversionEventsResponseIn": "_analyticsadmin_70_GoogleAnalyticsAdminV1betaListConversionEventsResponseIn",
        "GoogleAnalyticsAdminV1betaListConversionEventsResponseOut": "_analyticsadmin_71_GoogleAnalyticsAdminV1betaListConversionEventsResponseOut",
        "GoogleAnalyticsAdminV1betaDataSharingSettingsIn": "_analyticsadmin_72_GoogleAnalyticsAdminV1betaDataSharingSettingsIn",
        "GoogleAnalyticsAdminV1betaDataSharingSettingsOut": "_analyticsadmin_73_GoogleAnalyticsAdminV1betaDataSharingSettingsOut",
        "GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestIn": "_analyticsadmin_74_GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestIn",
        "GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestOut": "_analyticsadmin_75_GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestOut",
        "GoogleAnalyticsAdminV1betaAccessMetricHeaderIn": "_analyticsadmin_76_GoogleAnalyticsAdminV1betaAccessMetricHeaderIn",
        "GoogleAnalyticsAdminV1betaAccessMetricHeaderOut": "_analyticsadmin_77_GoogleAnalyticsAdminV1betaAccessMetricHeaderOut",
        "GoogleAnalyticsAdminV1betaAccessDimensionIn": "_analyticsadmin_78_GoogleAnalyticsAdminV1betaAccessDimensionIn",
        "GoogleAnalyticsAdminV1betaAccessDimensionOut": "_analyticsadmin_79_GoogleAnalyticsAdminV1betaAccessDimensionOut",
        "GoogleAnalyticsAdminV1betaAccessFilterExpressionListIn": "_analyticsadmin_80_GoogleAnalyticsAdminV1betaAccessFilterExpressionListIn",
        "GoogleAnalyticsAdminV1betaAccessFilterExpressionListOut": "_analyticsadmin_81_GoogleAnalyticsAdminV1betaAccessFilterExpressionListOut",
        "GoogleAnalyticsAdminV1betaAccessStringFilterIn": "_analyticsadmin_82_GoogleAnalyticsAdminV1betaAccessStringFilterIn",
        "GoogleAnalyticsAdminV1betaAccessStringFilterOut": "_analyticsadmin_83_GoogleAnalyticsAdminV1betaAccessStringFilterOut",
        "GoogleAnalyticsAdminV1betaListCustomDimensionsResponseIn": "_analyticsadmin_84_GoogleAnalyticsAdminV1betaListCustomDimensionsResponseIn",
        "GoogleAnalyticsAdminV1betaListCustomDimensionsResponseOut": "_analyticsadmin_85_GoogleAnalyticsAdminV1betaListCustomDimensionsResponseOut",
        "GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByIn": "_analyticsadmin_86_GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByIn",
        "GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByOut": "_analyticsadmin_87_GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByOut",
        "GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestIn": "_analyticsadmin_88_GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestIn",
        "GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestOut": "_analyticsadmin_89_GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestOut",
        "GoogleAnalyticsAdminV1betaAccessNumericFilterIn": "_analyticsadmin_90_GoogleAnalyticsAdminV1betaAccessNumericFilterIn",
        "GoogleAnalyticsAdminV1betaAccessNumericFilterOut": "_analyticsadmin_91_GoogleAnalyticsAdminV1betaAccessNumericFilterOut",
        "GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseIn": "_analyticsadmin_92_GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseIn",
        "GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseOut": "_analyticsadmin_93_GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseOut",
        "GoogleAnalyticsAdminV1betaAccessQuotaIn": "_analyticsadmin_94_GoogleAnalyticsAdminV1betaAccessQuotaIn",
        "GoogleAnalyticsAdminV1betaAccessQuotaOut": "_analyticsadmin_95_GoogleAnalyticsAdminV1betaAccessQuotaOut",
        "GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseIn": "_analyticsadmin_96_GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseIn",
        "GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut": "_analyticsadmin_97_GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut",
        "GoogleAnalyticsAdminV1betaListPropertiesResponseIn": "_analyticsadmin_98_GoogleAnalyticsAdminV1betaListPropertiesResponseIn",
        "GoogleAnalyticsAdminV1betaListPropertiesResponseOut": "_analyticsadmin_99_GoogleAnalyticsAdminV1betaListPropertiesResponseOut",
        "GoogleAnalyticsAdminV1betaAccessDateRangeIn": "_analyticsadmin_100_GoogleAnalyticsAdminV1betaAccessDateRangeIn",
        "GoogleAnalyticsAdminV1betaAccessDateRangeOut": "_analyticsadmin_101_GoogleAnalyticsAdminV1betaAccessDateRangeOut",
        "GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseIn": "_analyticsadmin_102_GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseIn",
        "GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseOut": "_analyticsadmin_103_GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseOut",
        "GoogleAnalyticsAdminV1betaDataStreamIn": "_analyticsadmin_104_GoogleAnalyticsAdminV1betaDataStreamIn",
        "GoogleAnalyticsAdminV1betaDataStreamOut": "_analyticsadmin_105_GoogleAnalyticsAdminV1betaDataStreamOut",
        "GoogleAnalyticsAdminV1betaDataRetentionSettingsIn": "_analyticsadmin_106_GoogleAnalyticsAdminV1betaDataRetentionSettingsIn",
        "GoogleAnalyticsAdminV1betaDataRetentionSettingsOut": "_analyticsadmin_107_GoogleAnalyticsAdminV1betaDataRetentionSettingsOut",
        "GoogleProtobufEmptyIn": "_analyticsadmin_108_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_analyticsadmin_109_GoogleProtobufEmptyOut",
        "GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn": "_analyticsadmin_110_GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn",
        "GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataOut": "_analyticsadmin_111_GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataOut",
        "GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseIn": "_analyticsadmin_112_GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseIn",
        "GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseOut": "_analyticsadmin_113_GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseOut",
        "GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequestIn": "_analyticsadmin_114_GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequestIn",
        "GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequestOut": "_analyticsadmin_115_GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequestOut",
        "GoogleAnalyticsAdminV1betaRunAccessReportResponseIn": "_analyticsadmin_116_GoogleAnalyticsAdminV1betaRunAccessReportResponseIn",
        "GoogleAnalyticsAdminV1betaRunAccessReportResponseOut": "_analyticsadmin_117_GoogleAnalyticsAdminV1betaRunAccessReportResponseOut",
        "GoogleAnalyticsAdminV1betaCustomMetricIn": "_analyticsadmin_118_GoogleAnalyticsAdminV1betaCustomMetricIn",
        "GoogleAnalyticsAdminV1betaCustomMetricOut": "_analyticsadmin_119_GoogleAnalyticsAdminV1betaCustomMetricOut",
        "GoogleAnalyticsAdminV1betaListFirebaseLinksResponseIn": "_analyticsadmin_120_GoogleAnalyticsAdminV1betaListFirebaseLinksResponseIn",
        "GoogleAnalyticsAdminV1betaListFirebaseLinksResponseOut": "_analyticsadmin_121_GoogleAnalyticsAdminV1betaListFirebaseLinksResponseOut",
        "GoogleAnalyticsAdminV1betaListCustomMetricsResponseIn": "_analyticsadmin_122_GoogleAnalyticsAdminV1betaListCustomMetricsResponseIn",
        "GoogleAnalyticsAdminV1betaListCustomMetricsResponseOut": "_analyticsadmin_123_GoogleAnalyticsAdminV1betaListCustomMetricsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleAnalyticsAdminV1betaListDataStreamsResponseIn"] = t.struct(
        {
            "dataStreams": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaDataStreamIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListDataStreamsResponseIn"])
    types["GoogleAnalyticsAdminV1betaListDataStreamsResponseOut"] = t.struct(
        {
            "dataStreams": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaDataStreamOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListDataStreamsResponseOut"])
    types["GoogleAnalyticsAdminV1betaChangeHistoryChangeIn"] = t.struct(
        {
            "resourceAfterChange": t.proxy(
                renames[
                    "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceIn"
                ]
            ).optional(),
            "action": t.string().optional(),
            "resourceBeforeChange": t.proxy(
                renames[
                    "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceIn"
                ]
            ).optional(),
            "resource": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaChangeHistoryChangeIn"])
    types["GoogleAnalyticsAdminV1betaChangeHistoryChangeOut"] = t.struct(
        {
            "resourceAfterChange": t.proxy(
                renames[
                    "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceOut"
                ]
            ).optional(),
            "action": t.string().optional(),
            "resourceBeforeChange": t.proxy(
                renames[
                    "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceOut"
                ]
            ).optional(),
            "resource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaChangeHistoryChangeOut"])
    types["GoogleAnalyticsAdminV1betaAccessDimensionValueIn"] = t.struct(
        {"value": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDimensionValueIn"])
    types["GoogleAnalyticsAdminV1betaAccessDimensionValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDimensionValueOut"])
    types["GoogleAnalyticsAdminV1betaAccessMetricValueIn"] = t.struct(
        {"value": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessMetricValueIn"])
    types["GoogleAnalyticsAdminV1betaAccessMetricValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessMetricValueOut"])
    types["GoogleAnalyticsAdminV1betaGoogleAdsLinkIn"] = t.struct(
        {
            "adsPersonalizationEnabled": t.boolean().optional(),
            "customerId": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkIn"])
    types["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "canManageClients": t.boolean().optional(),
            "creatorEmailAddress": t.string().optional(),
            "adsPersonalizationEnabled": t.boolean().optional(),
            "customerId": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"])
    types["GoogleAnalyticsAdminV1betaAccountIn"] = t.struct(
        {"displayName": t.string(), "regionCode": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccountIn"])
    types["GoogleAnalyticsAdminV1betaAccountOut"] = t.struct(
        {
            "displayName": t.string(),
            "deleted": t.boolean().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccountOut"])
    types[
        "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceIn"
    ] = t.struct(
        {
            "account": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccountIn"]
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
            "property": t.proxy(
                renames["GoogleAnalyticsAdminV1betaPropertyIn"]
            ).optional(),
            "googleAdsLink": t.proxy(
                renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkIn"]
            ).optional(),
            "measurementProtocolSecret": t.proxy(
                renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretIn"]
            ).optional(),
            "dataRetentionSettings": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsIn"]
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
            "firebaseLink": t.proxy(
                renames["GoogleAnalyticsAdminV1betaFirebaseLinkOut"]
            ).optional(),
            "conversionEvent": t.proxy(
                renames["GoogleAnalyticsAdminV1betaConversionEventOut"]
            ).optional(),
            "dataStream": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamOut"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleAnalyticsAdminV1betaPropertyOut"]
            ).optional(),
            "googleAdsLink": t.proxy(
                renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"]
            ).optional(),
            "measurementProtocolSecret": t.proxy(
                renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"]
            ).optional(),
            "dataRetentionSettings": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceOut"]
    )
    types["GoogleAnalyticsAdminV1betaAccessFilterIn"] = t.struct(
        {
            "inListFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessInListFilterIn"]
            ).optional(),
            "stringFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessStringFilterIn"]
            ).optional(),
            "fieldName": t.string().optional(),
            "betweenFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessBetweenFilterIn"]
            ).optional(),
            "numericFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessNumericFilterIn"]
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessFilterIn"])
    types["GoogleAnalyticsAdminV1betaAccessFilterOut"] = t.struct(
        {
            "inListFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessInListFilterOut"]
            ).optional(),
            "stringFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessStringFilterOut"]
            ).optional(),
            "fieldName": t.string().optional(),
            "betweenFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessBetweenFilterOut"]
            ).optional(),
            "numericFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessNumericFilterOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessFilterOut"])
    types["GoogleAnalyticsAdminV1betaRunAccessReportRequestIn"] = t.struct(
        {
            "returnEntityQuota": t.boolean().optional(),
            "dimensionFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
            ).optional(),
            "orderBys": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
            ).optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
            ).optional(),
            "dimensions": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
            ).optional(),
            "dateRanges": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
            ).optional(),
            "timeZone": t.string().optional(),
            "offset": t.string().optional(),
            "metricFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
            ).optional(),
            "limit": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaRunAccessReportRequestIn"])
    types["GoogleAnalyticsAdminV1betaRunAccessReportRequestOut"] = t.struct(
        {
            "returnEntityQuota": t.boolean().optional(),
            "dimensionFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionOut"]
            ).optional(),
            "orderBys": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByOut"])
            ).optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricOut"])
            ).optional(),
            "dimensions": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionOut"])
            ).optional(),
            "dateRanges": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeOut"])
            ).optional(),
            "timeZone": t.string().optional(),
            "offset": t.string().optional(),
            "metricFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionOut"]
            ).optional(),
            "limit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaRunAccessReportRequestOut"])
    types["GoogleAnalyticsAdminV1betaChangeHistoryEventIn"] = t.struct(
        {
            "changesFiltered": t.boolean().optional(),
            "actorType": t.string().optional(),
            "userActorEmail": t.string().optional(),
            "changes": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaChangeHistoryChangeIn"])
            ).optional(),
            "changeTime": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaChangeHistoryEventIn"])
    types["GoogleAnalyticsAdminV1betaChangeHistoryEventOut"] = t.struct(
        {
            "changesFiltered": t.boolean().optional(),
            "actorType": t.string().optional(),
            "userActorEmail": t.string().optional(),
            "changes": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaChangeHistoryChangeOut"])
            ).optional(),
            "changeTime": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaChangeHistoryEventOut"])
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
    types["GoogleAnalyticsAdminV1betaFirebaseLinkIn"] = t.struct(
        {"project": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaFirebaseLinkIn"])
    types["GoogleAnalyticsAdminV1betaFirebaseLinkOut"] = t.struct(
        {
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "project": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaFirebaseLinkOut"])
    types["GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestIn"])
    types["GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestOut"])
    types["GoogleAnalyticsAdminV1betaAccessBetweenFilterIn"] = t.struct(
        {
            "fromValue": t.proxy(
                renames["GoogleAnalyticsAdminV1betaNumericValueIn"]
            ).optional(),
            "toValue": t.proxy(
                renames["GoogleAnalyticsAdminV1betaNumericValueIn"]
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessBetweenFilterIn"])
    types["GoogleAnalyticsAdminV1betaAccessBetweenFilterOut"] = t.struct(
        {
            "fromValue": t.proxy(
                renames["GoogleAnalyticsAdminV1betaNumericValueOut"]
            ).optional(),
            "toValue": t.proxy(
                renames["GoogleAnalyticsAdminV1betaNumericValueOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessBetweenFilterOut"])
    types["GoogleAnalyticsAdminV1betaCustomDimensionIn"] = t.struct(
        {
            "parameterName": t.string(),
            "description": t.string().optional(),
            "disallowAdsPersonalization": t.boolean().optional(),
            "displayName": t.string(),
            "scope": t.string(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaCustomDimensionIn"])
    types["GoogleAnalyticsAdminV1betaCustomDimensionOut"] = t.struct(
        {
            "parameterName": t.string(),
            "description": t.string().optional(),
            "disallowAdsPersonalization": t.boolean().optional(),
            "displayName": t.string(),
            "scope": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaCustomDimensionOut"])
    types["GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestIn"] = t.struct(
        {
            "account": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccountIn"]
            ).optional(),
            "redirectUri": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestIn"])
    types["GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestOut"] = t.struct(
        {
            "account": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccountOut"]
            ).optional(),
            "redirectUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestOut"])
    types["GoogleAnalyticsAdminV1betaAccessMetricIn"] = t.struct(
        {"metricName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
    types["GoogleAnalyticsAdminV1betaAccessMetricOut"] = t.struct(
        {
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessMetricOut"])
    types["GoogleAnalyticsAdminV1betaListAccountsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "accounts": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccountIn"])
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListAccountsResponseIn"])
    types["GoogleAnalyticsAdminV1betaListAccountsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "accounts": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccountOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListAccountsResponseOut"])
    types["GoogleAnalyticsAdminV1betaPropertyIn"] = t.struct(
        {
            "propertyType": t.string().optional(),
            "currencyCode": t.string().optional(),
            "timeZone": t.string(),
            "displayName": t.string(),
            "parent": t.string().optional(),
            "account": t.string().optional(),
            "industryCategory": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaPropertyIn"])
    types["GoogleAnalyticsAdminV1betaPropertyOut"] = t.struct(
        {
            "propertyType": t.string().optional(),
            "serviceLevel": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "currencyCode": t.string().optional(),
            "timeZone": t.string(),
            "displayName": t.string(),
            "updateTime": t.string().optional(),
            "parent": t.string().optional(),
            "account": t.string().optional(),
            "deleteTime": t.string().optional(),
            "industryCategory": t.string().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaPropertyOut"])
    types["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretIn"] = t.struct(
        {"displayName": t.string()}
    ).named(renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretIn"])
    types["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"] = t.struct(
        {
            "displayName": t.string(),
            "name": t.string().optional(),
            "secretValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"])
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
    types["GoogleAnalyticsAdminV1betaConversionEventIn"] = t.struct(
        {"eventName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaConversionEventIn"])
    types["GoogleAnalyticsAdminV1betaConversionEventOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "custom": t.boolean().optional(),
            "eventName": t.string().optional(),
            "deletable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaConversionEventOut"])
    types["GoogleAnalyticsAdminV1betaNumericValueIn"] = t.struct(
        {"int64Value": t.string().optional(), "doubleValue": t.number().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaNumericValueIn"])
    types["GoogleAnalyticsAdminV1betaNumericValueOut"] = t.struct(
        {
            "int64Value": t.string().optional(),
            "doubleValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaNumericValueOut"])
    types["GoogleAnalyticsAdminV1betaAccessRowIn"] = t.struct(
        {
            "dimensionValues": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionValueIn"])
            ).optional(),
            "metricValues": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricValueIn"])
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessRowIn"])
    types["GoogleAnalyticsAdminV1betaAccessRowOut"] = t.struct(
        {
            "dimensionValues": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionValueOut"])
            ).optional(),
            "metricValues": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricValueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessRowOut"])
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
    types["GoogleAnalyticsAdminV1betaAccountSummaryIn"] = t.struct(
        {
            "account": t.string().optional(),
            "displayName": t.string().optional(),
            "propertySummaries": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaPropertySummaryIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccountSummaryIn"])
    types["GoogleAnalyticsAdminV1betaAccountSummaryOut"] = t.struct(
        {
            "account": t.string().optional(),
            "displayName": t.string().optional(),
            "propertySummaries": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaPropertySummaryOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccountSummaryOut"])
    types["GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByIn"] = t.struct(
        {"dimensionName": t.string().optional(), "orderType": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByIn"])
    types["GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByOut"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "orderType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByOut"])
    types["GoogleAnalyticsAdminV1betaAccessDimensionHeaderIn"] = t.struct(
        {"dimensionName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDimensionHeaderIn"])
    types["GoogleAnalyticsAdminV1betaAccessDimensionHeaderOut"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDimensionHeaderOut"])
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
    types["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"] = t.struct(
        {
            "orGroup": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionListIn"]
            ).optional(),
            "notExpression": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
            ).optional(),
            "accessFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterIn"]
            ).optional(),
            "andGroup": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionListIn"]
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
            "accessFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterOut"]
            ).optional(),
            "andGroup": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionListOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionOut"])
    types["GoogleAnalyticsAdminV1betaPropertySummaryIn"] = t.struct(
        {
            "property": t.string().optional(),
            "displayName": t.string().optional(),
            "propertyType": t.string().optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaPropertySummaryIn"])
    types["GoogleAnalyticsAdminV1betaPropertySummaryOut"] = t.struct(
        {
            "property": t.string().optional(),
            "displayName": t.string().optional(),
            "propertyType": t.string().optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaPropertySummaryOut"])
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
    types["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn"] = t.struct(
        {"bundleId": t.string()}
    ).named(renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn"])
    types["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataOut"] = t.struct(
        {
            "bundleId": t.string(),
            "firebaseAppId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataOut"])
    types["GoogleAnalyticsAdminV1betaListConversionEventsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "conversionEvents": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaConversionEventIn"])
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListConversionEventsResponseIn"])
    types["GoogleAnalyticsAdminV1betaListConversionEventsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "conversionEvents": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaConversionEventOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListConversionEventsResponseOut"])
    types["GoogleAnalyticsAdminV1betaDataSharingSettingsIn"] = t.struct(
        {
            "sharingWithGoogleSupportEnabled": t.boolean().optional(),
            "sharingWithGoogleAnySalesEnabled": t.boolean().optional(),
            "sharingWithOthersEnabled": t.boolean().optional(),
            "sharingWithGoogleAssignedSalesEnabled": t.boolean().optional(),
            "sharingWithGoogleProductsEnabled": t.boolean().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataSharingSettingsIn"])
    types["GoogleAnalyticsAdminV1betaDataSharingSettingsOut"] = t.struct(
        {
            "sharingWithGoogleSupportEnabled": t.boolean().optional(),
            "sharingWithGoogleAnySalesEnabled": t.boolean().optional(),
            "sharingWithOthersEnabled": t.boolean().optional(),
            "sharingWithGoogleAssignedSalesEnabled": t.boolean().optional(),
            "name": t.string().optional(),
            "sharingWithGoogleProductsEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataSharingSettingsOut"])
    types["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestIn"] = t.struct(
        {
            "earliestChangeTime": t.string().optional(),
            "actorEmail": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "resourceType": t.array(t.string()).optional(),
            "property": t.string().optional(),
            "action": t.array(t.string()).optional(),
            "latestChangeTime": t.string().optional(),
            "pageSize": t.integer().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestIn"])
    types["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestOut"] = t.struct(
        {
            "earliestChangeTime": t.string().optional(),
            "actorEmail": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "resourceType": t.array(t.string()).optional(),
            "property": t.string().optional(),
            "action": t.array(t.string()).optional(),
            "latestChangeTime": t.string().optional(),
            "pageSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestOut"])
    types["GoogleAnalyticsAdminV1betaAccessMetricHeaderIn"] = t.struct(
        {"metricName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessMetricHeaderIn"])
    types["GoogleAnalyticsAdminV1betaAccessMetricHeaderOut"] = t.struct(
        {
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessMetricHeaderOut"])
    types["GoogleAnalyticsAdminV1betaAccessDimensionIn"] = t.struct(
        {"dimensionName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
    types["GoogleAnalyticsAdminV1betaAccessDimensionOut"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDimensionOut"])
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
    types["GoogleAnalyticsAdminV1betaAccessStringFilterIn"] = t.struct(
        {
            "matchType": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessStringFilterIn"])
    types["GoogleAnalyticsAdminV1betaAccessStringFilterOut"] = t.struct(
        {
            "matchType": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessStringFilterOut"])
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
    types["GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestIn"])
    types["GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestOut"])
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
    types[
        "GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseIn"
    ] = t.struct(
        {
            "measurementProtocolSecrets": t.array(
                t.proxy(
                    renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretIn"]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(
        renames["GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseIn"]
    )
    types[
        "GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseOut"
    ] = t.struct(
        {
            "measurementProtocolSecrets": t.array(
                t.proxy(
                    renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseOut"]
    )
    types["GoogleAnalyticsAdminV1betaAccessQuotaIn"] = t.struct(
        {
            "concurrentRequests": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusIn"]
            ).optional(),
            "tokensPerDay": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusIn"]
            ).optional(),
            "serverErrorsPerProjectPerHour": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusIn"]
            ).optional(),
            "tokensPerProjectPerHour": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusIn"]
            ).optional(),
            "tokensPerHour": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusIn"]
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessQuotaIn"])
    types["GoogleAnalyticsAdminV1betaAccessQuotaOut"] = t.struct(
        {
            "concurrentRequests": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusOut"]
            ).optional(),
            "tokensPerDay": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusOut"]
            ).optional(),
            "serverErrorsPerProjectPerHour": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusOut"]
            ).optional(),
            "tokensPerProjectPerHour": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusOut"]
            ).optional(),
            "tokensPerHour": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessQuotaOut"])
    types["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseIn"] = t.struct(
        {"accountTicketId": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseIn"])
    types["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut"] = t.struct(
        {
            "accountTicketId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut"])
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
    types["GoogleAnalyticsAdminV1betaAccessDateRangeIn"] = t.struct(
        {"startDate": t.string().optional(), "endDate": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
    types["GoogleAnalyticsAdminV1betaAccessDateRangeOut"] = t.struct(
        {
            "startDate": t.string().optional(),
            "endDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDateRangeOut"])
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
    types["GoogleAnalyticsAdminV1betaDataStreamIn"] = t.struct(
        {
            "webStreamData": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "iosAppStreamData": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn"]
            ).optional(),
            "androidAppStreamData": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn"]
            ).optional(),
            "type": t.string(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataStreamIn"])
    types["GoogleAnalyticsAdminV1betaDataStreamOut"] = t.struct(
        {
            "webStreamData": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "iosAppStreamData": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataOut"]
            ).optional(),
            "androidAppStreamData": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataOut"]
            ).optional(),
            "type": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataStreamOut"])
    types["GoogleAnalyticsAdminV1betaDataRetentionSettingsIn"] = t.struct(
        {
            "eventDataRetention": t.string().optional(),
            "resetUserDataOnNewActivity": t.boolean().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsIn"])
    types["GoogleAnalyticsAdminV1betaDataRetentionSettingsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "eventDataRetention": t.string().optional(),
            "resetUserDataOnNewActivity": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
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
    types["GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "googleAdsLinks": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkIn"])
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseIn"])
    types["GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "googleAdsLinks": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseOut"])
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
    types["GoogleAnalyticsAdminV1betaRunAccessReportResponseIn"] = t.struct(
        {
            "dimensionHeaders": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionHeaderIn"])
            ).optional(),
            "quota": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaIn"]
            ).optional(),
            "rows": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessRowIn"])
            ).optional(),
            "rowCount": t.integer().optional(),
            "metricHeaders": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricHeaderIn"])
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseIn"])
    types["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"] = t.struct(
        {
            "dimensionHeaders": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionHeaderOut"])
            ).optional(),
            "quota": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaOut"]
            ).optional(),
            "rows": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessRowOut"])
            ).optional(),
            "rowCount": t.integer().optional(),
            "metricHeaders": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricHeaderOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"])
    types["GoogleAnalyticsAdminV1betaCustomMetricIn"] = t.struct(
        {
            "restrictedMetricType": t.array(t.string()).optional(),
            "parameterName": t.string(),
            "measurementUnit": t.string(),
            "scope": t.string(),
            "description": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaCustomMetricIn"])
    types["GoogleAnalyticsAdminV1betaCustomMetricOut"] = t.struct(
        {
            "restrictedMetricType": t.array(t.string()).optional(),
            "parameterName": t.string(),
            "name": t.string().optional(),
            "measurementUnit": t.string(),
            "scope": t.string(),
            "description": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaCustomMetricOut"])
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

    functions = {}
    functions["propertiesCreate"] = analyticsadmin.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaPropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesRunAccessReport"] = analyticsadmin.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaPropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesUpdateDataRetentionSettings"] = analyticsadmin.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaPropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGetDataRetentionSettings"] = analyticsadmin.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaPropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesList"] = analyticsadmin.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaPropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGet"] = analyticsadmin.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaPropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesAcknowledgeUserDataCollection"] = analyticsadmin.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaPropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesPatch"] = analyticsadmin.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaPropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesDelete"] = analyticsadmin.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaPropertyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomMetricsArchive"] = analyticsadmin.post(
        "v1beta/{parent}/customMetrics",
        t.struct(
            {
                "parent": t.string(),
                "restrictedMetricType": t.array(t.string()).optional(),
                "parameterName": t.string(),
                "measurementUnit": t.string(),
                "scope": t.string(),
                "description": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaCustomMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomMetricsPatch"] = analyticsadmin.post(
        "v1beta/{parent}/customMetrics",
        t.struct(
            {
                "parent": t.string(),
                "restrictedMetricType": t.array(t.string()).optional(),
                "parameterName": t.string(),
                "measurementUnit": t.string(),
                "scope": t.string(),
                "description": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaCustomMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomMetricsList"] = analyticsadmin.post(
        "v1beta/{parent}/customMetrics",
        t.struct(
            {
                "parent": t.string(),
                "restrictedMetricType": t.array(t.string()).optional(),
                "parameterName": t.string(),
                "measurementUnit": t.string(),
                "scope": t.string(),
                "description": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaCustomMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomMetricsGet"] = analyticsadmin.post(
        "v1beta/{parent}/customMetrics",
        t.struct(
            {
                "parent": t.string(),
                "restrictedMetricType": t.array(t.string()).optional(),
                "parameterName": t.string(),
                "measurementUnit": t.string(),
                "scope": t.string(),
                "description": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaCustomMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomMetricsCreate"] = analyticsadmin.post(
        "v1beta/{parent}/customMetrics",
        t.struct(
            {
                "parent": t.string(),
                "restrictedMetricType": t.array(t.string()).optional(),
                "parameterName": t.string(),
                "measurementUnit": t.string(),
                "scope": t.string(),
                "description": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaCustomMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesConversionEventsGet"] = analyticsadmin.get(
        "v1beta/{parent}/conversionEvents",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaListConversionEventsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesConversionEventsCreate"] = analyticsadmin.get(
        "v1beta/{parent}/conversionEvents",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaListConversionEventsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesConversionEventsDelete"] = analyticsadmin.get(
        "v1beta/{parent}/conversionEvents",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaListConversionEventsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesConversionEventsList"] = analyticsadmin.get(
        "v1beta/{parent}/conversionEvents",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaListConversionEventsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesDataStreamsCreate"] = analyticsadmin.patch(
        "v1beta/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "webStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "iosAppStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn"]
                ).optional(),
                "androidAppStreamData": t.proxy(
                    renames[
                        "GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn"
                    ]
                ).optional(),
                "type": t.string(),
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
                "webStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "iosAppStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn"]
                ).optional(),
                "androidAppStreamData": t.proxy(
                    renames[
                        "GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn"
                    ]
                ).optional(),
                "type": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaDataStreamOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesDataStreamsGet"] = analyticsadmin.patch(
        "v1beta/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "webStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "iosAppStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn"]
                ).optional(),
                "androidAppStreamData": t.proxy(
                    renames[
                        "GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn"
                    ]
                ).optional(),
                "type": t.string(),
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
                "webStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "iosAppStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn"]
                ).optional(),
                "androidAppStreamData": t.proxy(
                    renames[
                        "GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn"
                    ]
                ).optional(),
                "type": t.string(),
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
                "webStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "iosAppStreamData": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn"]
                ).optional(),
                "androidAppStreamData": t.proxy(
                    renames[
                        "GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn"
                    ]
                ).optional(),
                "type": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaDataStreamOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "propertiesDataStreamsMeasurementProtocolSecretsCreate"
    ] = analyticsadmin.patch(
        "v1beta/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "propertiesDataStreamsMeasurementProtocolSecretsList"
    ] = analyticsadmin.patch(
        "v1beta/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "propertiesDataStreamsMeasurementProtocolSecretsDelete"
    ] = analyticsadmin.patch(
        "v1beta/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "propertiesDataStreamsMeasurementProtocolSecretsGet"
    ] = analyticsadmin.patch(
        "v1beta/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "propertiesDataStreamsMeasurementProtocolSecretsPatch"
    ] = analyticsadmin.patch(
        "v1beta/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"]),
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
    functions["propertiesGoogleAdsLinksDelete"] = analyticsadmin.patch(
        "v1beta/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "adsPersonalizationEnabled": t.boolean().optional(),
                "customerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGoogleAdsLinksCreate"] = analyticsadmin.patch(
        "v1beta/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "adsPersonalizationEnabled": t.boolean().optional(),
                "customerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGoogleAdsLinksList"] = analyticsadmin.patch(
        "v1beta/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "adsPersonalizationEnabled": t.boolean().optional(),
                "customerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGoogleAdsLinksPatch"] = analyticsadmin.patch(
        "v1beta/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "adsPersonalizationEnabled": t.boolean().optional(),
                "customerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"]),
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
    functions["accountsProvisionAccountTicket"] = analyticsadmin.post(
        "v1beta/{entity}:runAccessReport",
        t.struct(
            {
                "entity": t.string().optional(),
                "returnEntityQuota": t.boolean().optional(),
                "dimensionFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "orderBys": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
                ).optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
                ).optional(),
                "dimensions": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
                ).optional(),
                "dateRanges": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
                ).optional(),
                "timeZone": t.string().optional(),
                "offset": t.string().optional(),
                "metricFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "limit": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsList"] = analyticsadmin.post(
        "v1beta/{entity}:runAccessReport",
        t.struct(
            {
                "entity": t.string().optional(),
                "returnEntityQuota": t.boolean().optional(),
                "dimensionFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "orderBys": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
                ).optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
                ).optional(),
                "dimensions": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
                ).optional(),
                "dateRanges": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
                ).optional(),
                "timeZone": t.string().optional(),
                "offset": t.string().optional(),
                "metricFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "limit": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsPatch"] = analyticsadmin.post(
        "v1beta/{entity}:runAccessReport",
        t.struct(
            {
                "entity": t.string().optional(),
                "returnEntityQuota": t.boolean().optional(),
                "dimensionFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "orderBys": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
                ).optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
                ).optional(),
                "dimensions": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
                ).optional(),
                "dateRanges": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
                ).optional(),
                "timeZone": t.string().optional(),
                "offset": t.string().optional(),
                "metricFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "limit": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsGetDataSharingSettings"] = analyticsadmin.post(
        "v1beta/{entity}:runAccessReport",
        t.struct(
            {
                "entity": t.string().optional(),
                "returnEntityQuota": t.boolean().optional(),
                "dimensionFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "orderBys": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
                ).optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
                ).optional(),
                "dimensions": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
                ).optional(),
                "dateRanges": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
                ).optional(),
                "timeZone": t.string().optional(),
                "offset": t.string().optional(),
                "metricFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "limit": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsGet"] = analyticsadmin.post(
        "v1beta/{entity}:runAccessReport",
        t.struct(
            {
                "entity": t.string().optional(),
                "returnEntityQuota": t.boolean().optional(),
                "dimensionFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "orderBys": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
                ).optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
                ).optional(),
                "dimensions": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
                ).optional(),
                "dateRanges": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
                ).optional(),
                "timeZone": t.string().optional(),
                "offset": t.string().optional(),
                "metricFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "limit": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsDelete"] = analyticsadmin.post(
        "v1beta/{entity}:runAccessReport",
        t.struct(
            {
                "entity": t.string().optional(),
                "returnEntityQuota": t.boolean().optional(),
                "dimensionFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "orderBys": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
                ).optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
                ).optional(),
                "dimensions": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
                ).optional(),
                "dateRanges": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
                ).optional(),
                "timeZone": t.string().optional(),
                "offset": t.string().optional(),
                "metricFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "limit": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsSearchChangeHistoryEvents"] = analyticsadmin.post(
        "v1beta/{entity}:runAccessReport",
        t.struct(
            {
                "entity": t.string().optional(),
                "returnEntityQuota": t.boolean().optional(),
                "dimensionFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "orderBys": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
                ).optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
                ).optional(),
                "dimensions": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
                ).optional(),
                "dateRanges": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
                ).optional(),
                "timeZone": t.string().optional(),
                "offset": t.string().optional(),
                "metricFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "limit": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsRunAccessReport"] = analyticsadmin.post(
        "v1beta/{entity}:runAccessReport",
        t.struct(
            {
                "entity": t.string().optional(),
                "returnEntityQuota": t.boolean().optional(),
                "dimensionFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "orderBys": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
                ).optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
                ).optional(),
                "dimensions": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
                ).optional(),
                "dateRanges": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
                ).optional(),
                "timeZone": t.string().optional(),
                "offset": t.string().optional(),
                "metricFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "limit": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="analyticsadmin",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
