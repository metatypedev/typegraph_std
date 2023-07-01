from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_analyticsadmin():
    analyticsadmin = HTTPRuntime("https://analyticsadmin.googleapis.com/")

    renames = {
        "ErrorResponse": "_analyticsadmin_1_ErrorResponse",
        "GoogleAnalyticsAdminV1betaAccessFilterIn": "_analyticsadmin_2_GoogleAnalyticsAdminV1betaAccessFilterIn",
        "GoogleAnalyticsAdminV1betaAccessFilterOut": "_analyticsadmin_3_GoogleAnalyticsAdminV1betaAccessFilterOut",
        "GoogleAnalyticsAdminV1betaDataSharingSettingsIn": "_analyticsadmin_4_GoogleAnalyticsAdminV1betaDataSharingSettingsIn",
        "GoogleAnalyticsAdminV1betaDataSharingSettingsOut": "_analyticsadmin_5_GoogleAnalyticsAdminV1betaDataSharingSettingsOut",
        "GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn": "_analyticsadmin_6_GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn",
        "GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataOut": "_analyticsadmin_7_GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataOut",
        "GoogleAnalyticsAdminV1betaCustomMetricIn": "_analyticsadmin_8_GoogleAnalyticsAdminV1betaCustomMetricIn",
        "GoogleAnalyticsAdminV1betaCustomMetricOut": "_analyticsadmin_9_GoogleAnalyticsAdminV1betaCustomMetricOut",
        "GoogleProtobufEmptyIn": "_analyticsadmin_10_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_analyticsadmin_11_GoogleProtobufEmptyOut",
        "GoogleAnalyticsAdminV1betaAccessFilterExpressionListIn": "_analyticsadmin_12_GoogleAnalyticsAdminV1betaAccessFilterExpressionListIn",
        "GoogleAnalyticsAdminV1betaAccessFilterExpressionListOut": "_analyticsadmin_13_GoogleAnalyticsAdminV1betaAccessFilterExpressionListOut",
        "GoogleAnalyticsAdminV1betaFirebaseLinkIn": "_analyticsadmin_14_GoogleAnalyticsAdminV1betaFirebaseLinkIn",
        "GoogleAnalyticsAdminV1betaFirebaseLinkOut": "_analyticsadmin_15_GoogleAnalyticsAdminV1betaFirebaseLinkOut",
        "GoogleAnalyticsAdminV1betaListCustomDimensionsResponseIn": "_analyticsadmin_16_GoogleAnalyticsAdminV1betaListCustomDimensionsResponseIn",
        "GoogleAnalyticsAdminV1betaListCustomDimensionsResponseOut": "_analyticsadmin_17_GoogleAnalyticsAdminV1betaListCustomDimensionsResponseOut",
        "GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestIn": "_analyticsadmin_18_GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestIn",
        "GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestOut": "_analyticsadmin_19_GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestOut",
        "GoogleAnalyticsAdminV1betaListAccountSummariesResponseIn": "_analyticsadmin_20_GoogleAnalyticsAdminV1betaListAccountSummariesResponseIn",
        "GoogleAnalyticsAdminV1betaListAccountSummariesResponseOut": "_analyticsadmin_21_GoogleAnalyticsAdminV1betaListAccountSummariesResponseOut",
        "GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn": "_analyticsadmin_22_GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn",
        "GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataOut": "_analyticsadmin_23_GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataOut",
        "GoogleAnalyticsAdminV1betaListPropertiesResponseIn": "_analyticsadmin_24_GoogleAnalyticsAdminV1betaListPropertiesResponseIn",
        "GoogleAnalyticsAdminV1betaListPropertiesResponseOut": "_analyticsadmin_25_GoogleAnalyticsAdminV1betaListPropertiesResponseOut",
        "GoogleAnalyticsAdminV1betaAccessQuotaStatusIn": "_analyticsadmin_26_GoogleAnalyticsAdminV1betaAccessQuotaStatusIn",
        "GoogleAnalyticsAdminV1betaAccessQuotaStatusOut": "_analyticsadmin_27_GoogleAnalyticsAdminV1betaAccessQuotaStatusOut",
        "GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseIn": "_analyticsadmin_28_GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseIn",
        "GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseOut": "_analyticsadmin_29_GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseOut",
        "GoogleAnalyticsAdminV1betaListConversionEventsResponseIn": "_analyticsadmin_30_GoogleAnalyticsAdminV1betaListConversionEventsResponseIn",
        "GoogleAnalyticsAdminV1betaListConversionEventsResponseOut": "_analyticsadmin_31_GoogleAnalyticsAdminV1betaListConversionEventsResponseOut",
        "GoogleAnalyticsAdminV1betaChangeHistoryChangeIn": "_analyticsadmin_32_GoogleAnalyticsAdminV1betaChangeHistoryChangeIn",
        "GoogleAnalyticsAdminV1betaChangeHistoryChangeOut": "_analyticsadmin_33_GoogleAnalyticsAdminV1betaChangeHistoryChangeOut",
        "GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestIn": "_analyticsadmin_34_GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestIn",
        "GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestOut": "_analyticsadmin_35_GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestOut",
        "GoogleAnalyticsAdminV1betaAccessInListFilterIn": "_analyticsadmin_36_GoogleAnalyticsAdminV1betaAccessInListFilterIn",
        "GoogleAnalyticsAdminV1betaAccessInListFilterOut": "_analyticsadmin_37_GoogleAnalyticsAdminV1betaAccessInListFilterOut",
        "GoogleAnalyticsAdminV1betaChangeHistoryEventIn": "_analyticsadmin_38_GoogleAnalyticsAdminV1betaChangeHistoryEventIn",
        "GoogleAnalyticsAdminV1betaChangeHistoryEventOut": "_analyticsadmin_39_GoogleAnalyticsAdminV1betaChangeHistoryEventOut",
        "GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponseIn": "_analyticsadmin_40_GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponseIn",
        "GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponseOut": "_analyticsadmin_41_GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponseOut",
        "GoogleAnalyticsAdminV1betaNumericValueIn": "_analyticsadmin_42_GoogleAnalyticsAdminV1betaNumericValueIn",
        "GoogleAnalyticsAdminV1betaNumericValueOut": "_analyticsadmin_43_GoogleAnalyticsAdminV1betaNumericValueOut",
        "GoogleAnalyticsAdminV1betaListDataStreamsResponseIn": "_analyticsadmin_44_GoogleAnalyticsAdminV1betaListDataStreamsResponseIn",
        "GoogleAnalyticsAdminV1betaListDataStreamsResponseOut": "_analyticsadmin_45_GoogleAnalyticsAdminV1betaListDataStreamsResponseOut",
        "GoogleAnalyticsAdminV1betaRunAccessReportResponseIn": "_analyticsadmin_46_GoogleAnalyticsAdminV1betaRunAccessReportResponseIn",
        "GoogleAnalyticsAdminV1betaRunAccessReportResponseOut": "_analyticsadmin_47_GoogleAnalyticsAdminV1betaRunAccessReportResponseOut",
        "GoogleAnalyticsAdminV1betaAccountIn": "_analyticsadmin_48_GoogleAnalyticsAdminV1betaAccountIn",
        "GoogleAnalyticsAdminV1betaAccountOut": "_analyticsadmin_49_GoogleAnalyticsAdminV1betaAccountOut",
        "GoogleAnalyticsAdminV1betaAccessQuotaIn": "_analyticsadmin_50_GoogleAnalyticsAdminV1betaAccessQuotaIn",
        "GoogleAnalyticsAdminV1betaAccessQuotaOut": "_analyticsadmin_51_GoogleAnalyticsAdminV1betaAccessQuotaOut",
        "GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn": "_analyticsadmin_52_GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn",
        "GoogleAnalyticsAdminV1betaDataStreamWebStreamDataOut": "_analyticsadmin_53_GoogleAnalyticsAdminV1betaDataStreamWebStreamDataOut",
        "GoogleAnalyticsAdminV1betaAccessRowIn": "_analyticsadmin_54_GoogleAnalyticsAdminV1betaAccessRowIn",
        "GoogleAnalyticsAdminV1betaAccessRowOut": "_analyticsadmin_55_GoogleAnalyticsAdminV1betaAccessRowOut",
        "GoogleAnalyticsAdminV1betaAccessDateRangeIn": "_analyticsadmin_56_GoogleAnalyticsAdminV1betaAccessDateRangeIn",
        "GoogleAnalyticsAdminV1betaAccessDateRangeOut": "_analyticsadmin_57_GoogleAnalyticsAdminV1betaAccessDateRangeOut",
        "GoogleAnalyticsAdminV1betaAccessNumericFilterIn": "_analyticsadmin_58_GoogleAnalyticsAdminV1betaAccessNumericFilterIn",
        "GoogleAnalyticsAdminV1betaAccessNumericFilterOut": "_analyticsadmin_59_GoogleAnalyticsAdminV1betaAccessNumericFilterOut",
        "GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestIn": "_analyticsadmin_60_GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestIn",
        "GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestOut": "_analyticsadmin_61_GoogleAnalyticsAdminV1betaProvisionAccountTicketRequestOut",
        "GoogleAnalyticsAdminV1betaAccessMetricValueIn": "_analyticsadmin_62_GoogleAnalyticsAdminV1betaAccessMetricValueIn",
        "GoogleAnalyticsAdminV1betaAccessMetricValueOut": "_analyticsadmin_63_GoogleAnalyticsAdminV1betaAccessMetricValueOut",
        "GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseIn": "_analyticsadmin_64_GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseIn",
        "GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseOut": "_analyticsadmin_65_GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseOut",
        "GoogleAnalyticsAdminV1betaListAccountsResponseIn": "_analyticsadmin_66_GoogleAnalyticsAdminV1betaListAccountsResponseIn",
        "GoogleAnalyticsAdminV1betaListAccountsResponseOut": "_analyticsadmin_67_GoogleAnalyticsAdminV1betaListAccountsResponseOut",
        "GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByIn": "_analyticsadmin_68_GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByIn",
        "GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByOut": "_analyticsadmin_69_GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByOut",
        "GoogleAnalyticsAdminV1betaAccessMetricHeaderIn": "_analyticsadmin_70_GoogleAnalyticsAdminV1betaAccessMetricHeaderIn",
        "GoogleAnalyticsAdminV1betaAccessMetricHeaderOut": "_analyticsadmin_71_GoogleAnalyticsAdminV1betaAccessMetricHeaderOut",
        "GoogleAnalyticsAdminV1betaPropertyIn": "_analyticsadmin_72_GoogleAnalyticsAdminV1betaPropertyIn",
        "GoogleAnalyticsAdminV1betaPropertyOut": "_analyticsadmin_73_GoogleAnalyticsAdminV1betaPropertyOut",
        "GoogleAnalyticsAdminV1betaMeasurementProtocolSecretIn": "_analyticsadmin_74_GoogleAnalyticsAdminV1betaMeasurementProtocolSecretIn",
        "GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut": "_analyticsadmin_75_GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut",
        "GoogleAnalyticsAdminV1betaDataStreamIn": "_analyticsadmin_76_GoogleAnalyticsAdminV1betaDataStreamIn",
        "GoogleAnalyticsAdminV1betaDataStreamOut": "_analyticsadmin_77_GoogleAnalyticsAdminV1betaDataStreamOut",
        "GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseIn": "_analyticsadmin_78_GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseIn",
        "GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseOut": "_analyticsadmin_79_GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseOut",
        "GoogleAnalyticsAdminV1betaAccountSummaryIn": "_analyticsadmin_80_GoogleAnalyticsAdminV1betaAccountSummaryIn",
        "GoogleAnalyticsAdminV1betaAccountSummaryOut": "_analyticsadmin_81_GoogleAnalyticsAdminV1betaAccountSummaryOut",
        "GoogleAnalyticsAdminV1betaAccessFilterExpressionIn": "_analyticsadmin_82_GoogleAnalyticsAdminV1betaAccessFilterExpressionIn",
        "GoogleAnalyticsAdminV1betaAccessFilterExpressionOut": "_analyticsadmin_83_GoogleAnalyticsAdminV1betaAccessFilterExpressionOut",
        "GoogleAnalyticsAdminV1betaPropertySummaryIn": "_analyticsadmin_84_GoogleAnalyticsAdminV1betaPropertySummaryIn",
        "GoogleAnalyticsAdminV1betaPropertySummaryOut": "_analyticsadmin_85_GoogleAnalyticsAdminV1betaPropertySummaryOut",
        "GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestIn": "_analyticsadmin_86_GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestIn",
        "GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestOut": "_analyticsadmin_87_GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestOut",
        "GoogleAnalyticsAdminV1betaListCustomMetricsResponseIn": "_analyticsadmin_88_GoogleAnalyticsAdminV1betaListCustomMetricsResponseIn",
        "GoogleAnalyticsAdminV1betaListCustomMetricsResponseOut": "_analyticsadmin_89_GoogleAnalyticsAdminV1betaListCustomMetricsResponseOut",
        "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceIn": "_analyticsadmin_90_GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceIn",
        "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceOut": "_analyticsadmin_91_GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceOut",
        "GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByIn": "_analyticsadmin_92_GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByIn",
        "GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByOut": "_analyticsadmin_93_GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderByOut",
        "GoogleAnalyticsAdminV1betaAccessOrderByIn": "_analyticsadmin_94_GoogleAnalyticsAdminV1betaAccessOrderByIn",
        "GoogleAnalyticsAdminV1betaAccessOrderByOut": "_analyticsadmin_95_GoogleAnalyticsAdminV1betaAccessOrderByOut",
        "GoogleAnalyticsAdminV1betaConversionEventIn": "_analyticsadmin_96_GoogleAnalyticsAdminV1betaConversionEventIn",
        "GoogleAnalyticsAdminV1betaConversionEventOut": "_analyticsadmin_97_GoogleAnalyticsAdminV1betaConversionEventOut",
        "GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequestIn": "_analyticsadmin_98_GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequestIn",
        "GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequestOut": "_analyticsadmin_99_GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequestOut",
        "GoogleAnalyticsAdminV1betaRunAccessReportRequestIn": "_analyticsadmin_100_GoogleAnalyticsAdminV1betaRunAccessReportRequestIn",
        "GoogleAnalyticsAdminV1betaRunAccessReportRequestOut": "_analyticsadmin_101_GoogleAnalyticsAdminV1betaRunAccessReportRequestOut",
        "GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseIn": "_analyticsadmin_102_GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseIn",
        "GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut": "_analyticsadmin_103_GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut",
        "GoogleAnalyticsAdminV1betaAccessDimensionValueIn": "_analyticsadmin_104_GoogleAnalyticsAdminV1betaAccessDimensionValueIn",
        "GoogleAnalyticsAdminV1betaAccessDimensionValueOut": "_analyticsadmin_105_GoogleAnalyticsAdminV1betaAccessDimensionValueOut",
        "GoogleAnalyticsAdminV1betaDataRetentionSettingsIn": "_analyticsadmin_106_GoogleAnalyticsAdminV1betaDataRetentionSettingsIn",
        "GoogleAnalyticsAdminV1betaDataRetentionSettingsOut": "_analyticsadmin_107_GoogleAnalyticsAdminV1betaDataRetentionSettingsOut",
        "GoogleAnalyticsAdminV1betaAccessBetweenFilterIn": "_analyticsadmin_108_GoogleAnalyticsAdminV1betaAccessBetweenFilterIn",
        "GoogleAnalyticsAdminV1betaAccessBetweenFilterOut": "_analyticsadmin_109_GoogleAnalyticsAdminV1betaAccessBetweenFilterOut",
        "GoogleAnalyticsAdminV1betaAccessStringFilterIn": "_analyticsadmin_110_GoogleAnalyticsAdminV1betaAccessStringFilterIn",
        "GoogleAnalyticsAdminV1betaAccessStringFilterOut": "_analyticsadmin_111_GoogleAnalyticsAdminV1betaAccessStringFilterOut",
        "GoogleAnalyticsAdminV1betaAccessDimensionHeaderIn": "_analyticsadmin_112_GoogleAnalyticsAdminV1betaAccessDimensionHeaderIn",
        "GoogleAnalyticsAdminV1betaAccessDimensionHeaderOut": "_analyticsadmin_113_GoogleAnalyticsAdminV1betaAccessDimensionHeaderOut",
        "GoogleAnalyticsAdminV1betaListFirebaseLinksResponseIn": "_analyticsadmin_114_GoogleAnalyticsAdminV1betaListFirebaseLinksResponseIn",
        "GoogleAnalyticsAdminV1betaListFirebaseLinksResponseOut": "_analyticsadmin_115_GoogleAnalyticsAdminV1betaListFirebaseLinksResponseOut",
        "GoogleAnalyticsAdminV1betaAccessMetricIn": "_analyticsadmin_116_GoogleAnalyticsAdminV1betaAccessMetricIn",
        "GoogleAnalyticsAdminV1betaAccessMetricOut": "_analyticsadmin_117_GoogleAnalyticsAdminV1betaAccessMetricOut",
        "GoogleAnalyticsAdminV1betaAccessDimensionIn": "_analyticsadmin_118_GoogleAnalyticsAdminV1betaAccessDimensionIn",
        "GoogleAnalyticsAdminV1betaAccessDimensionOut": "_analyticsadmin_119_GoogleAnalyticsAdminV1betaAccessDimensionOut",
        "GoogleAnalyticsAdminV1betaCustomDimensionIn": "_analyticsadmin_120_GoogleAnalyticsAdminV1betaCustomDimensionIn",
        "GoogleAnalyticsAdminV1betaCustomDimensionOut": "_analyticsadmin_121_GoogleAnalyticsAdminV1betaCustomDimensionOut",
        "GoogleAnalyticsAdminV1betaGoogleAdsLinkIn": "_analyticsadmin_122_GoogleAnalyticsAdminV1betaGoogleAdsLinkIn",
        "GoogleAnalyticsAdminV1betaGoogleAdsLinkOut": "_analyticsadmin_123_GoogleAnalyticsAdminV1betaGoogleAdsLinkOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleAnalyticsAdminV1betaAccessFilterIn"] = t.struct(
        {
            "inListFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessInListFilterIn"]
            ).optional(),
            "betweenFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessBetweenFilterIn"]
            ).optional(),
            "stringFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessStringFilterIn"]
            ).optional(),
            "numericFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessNumericFilterIn"]
            ).optional(),
            "fieldName": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessFilterIn"])
    types["GoogleAnalyticsAdminV1betaAccessFilterOut"] = t.struct(
        {
            "inListFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessInListFilterOut"]
            ).optional(),
            "betweenFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessBetweenFilterOut"]
            ).optional(),
            "stringFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessStringFilterOut"]
            ).optional(),
            "numericFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessNumericFilterOut"]
            ).optional(),
            "fieldName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessFilterOut"])
    types["GoogleAnalyticsAdminV1betaDataSharingSettingsIn"] = t.struct(
        {
            "sharingWithGoogleSupportEnabled": t.boolean().optional(),
            "sharingWithOthersEnabled": t.boolean().optional(),
            "sharingWithGoogleAnySalesEnabled": t.boolean().optional(),
            "sharingWithGoogleProductsEnabled": t.boolean().optional(),
            "sharingWithGoogleAssignedSalesEnabled": t.boolean().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataSharingSettingsIn"])
    types["GoogleAnalyticsAdminV1betaDataSharingSettingsOut"] = t.struct(
        {
            "sharingWithGoogleSupportEnabled": t.boolean().optional(),
            "name": t.string().optional(),
            "sharingWithOthersEnabled": t.boolean().optional(),
            "sharingWithGoogleAnySalesEnabled": t.boolean().optional(),
            "sharingWithGoogleProductsEnabled": t.boolean().optional(),
            "sharingWithGoogleAssignedSalesEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataSharingSettingsOut"])
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
    types["GoogleAnalyticsAdminV1betaCustomMetricIn"] = t.struct(
        {
            "parameterName": t.string(),
            "displayName": t.string(),
            "restrictedMetricType": t.array(t.string()).optional(),
            "scope": t.string(),
            "measurementUnit": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaCustomMetricIn"])
    types["GoogleAnalyticsAdminV1betaCustomMetricOut"] = t.struct(
        {
            "parameterName": t.string(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "restrictedMetricType": t.array(t.string()).optional(),
            "scope": t.string(),
            "measurementUnit": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaCustomMetricOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
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
    types["GoogleAnalyticsAdminV1betaFirebaseLinkIn"] = t.struct(
        {"project": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaFirebaseLinkIn"])
    types["GoogleAnalyticsAdminV1betaFirebaseLinkOut"] = t.struct(
        {
            "project": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaFirebaseLinkOut"])
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
    types["GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestIn"])
    types["GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequestOut"])
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
    types["GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn"] = t.struct(
        {"packageName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn"])
    types["GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "firebaseAppId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataOut"])
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
    types["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseIn"] = t.struct(
        {
            "changeHistoryEvents": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaChangeHistoryEventIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseIn"])
    types["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseOut"] = t.struct(
        {
            "changeHistoryEvents": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaChangeHistoryEventOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseOut"])
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
    types["GoogleAnalyticsAdminV1betaChangeHistoryChangeIn"] = t.struct(
        {
            "resource": t.string().optional(),
            "action": t.string().optional(),
            "resourceAfterChange": t.proxy(
                renames[
                    "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceIn"
                ]
            ).optional(),
            "resourceBeforeChange": t.proxy(
                renames[
                    "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaChangeHistoryChangeIn"])
    types["GoogleAnalyticsAdminV1betaChangeHistoryChangeOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "action": t.string().optional(),
            "resourceAfterChange": t.proxy(
                renames[
                    "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceOut"
                ]
            ).optional(),
            "resourceBeforeChange": t.proxy(
                renames[
                    "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaChangeHistoryChangeOut"])
    types["GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestIn"])
    types["GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaArchiveCustomMetricRequestOut"])
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
    types["GoogleAnalyticsAdminV1betaChangeHistoryEventIn"] = t.struct(
        {
            "changes": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaChangeHistoryChangeIn"])
            ).optional(),
            "changeTime": t.string().optional(),
            "actorType": t.string().optional(),
            "changesFiltered": t.boolean().optional(),
            "userActorEmail": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaChangeHistoryEventIn"])
    types["GoogleAnalyticsAdminV1betaChangeHistoryEventOut"] = t.struct(
        {
            "changes": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaChangeHistoryChangeOut"])
            ).optional(),
            "changeTime": t.string().optional(),
            "actorType": t.string().optional(),
            "changesFiltered": t.boolean().optional(),
            "userActorEmail": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaChangeHistoryEventOut"])
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
    types["GoogleAnalyticsAdminV1betaRunAccessReportResponseIn"] = t.struct(
        {
            "metricHeaders": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricHeaderIn"])
            ).optional(),
            "rows": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessRowIn"])
            ).optional(),
            "quota": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaIn"]
            ).optional(),
            "rowCount": t.integer().optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionHeaderIn"])
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseIn"])
    types["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"] = t.struct(
        {
            "metricHeaders": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricHeaderOut"])
            ).optional(),
            "rows": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessRowOut"])
            ).optional(),
            "quota": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaOut"]
            ).optional(),
            "rowCount": t.integer().optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionHeaderOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"])
    types["GoogleAnalyticsAdminV1betaAccountIn"] = t.struct(
        {"displayName": t.string(), "regionCode": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccountIn"])
    types["GoogleAnalyticsAdminV1betaAccountOut"] = t.struct(
        {
            "displayName": t.string(),
            "regionCode": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "deleted": t.boolean().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccountOut"])
    types["GoogleAnalyticsAdminV1betaAccessQuotaIn"] = t.struct(
        {
            "tokensPerDay": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusIn"]
            ).optional(),
            "concurrentRequests": t.proxy(
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
            "tokensPerDay": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessQuotaStatusOut"]
            ).optional(),
            "concurrentRequests": t.proxy(
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
    types["GoogleAnalyticsAdminV1betaAccessMetricValueIn"] = t.struct(
        {"value": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessMetricValueIn"])
    types["GoogleAnalyticsAdminV1betaAccessMetricValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessMetricValueOut"])
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
    types["GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByIn"] = t.struct(
        {"metricName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByIn"])
    types["GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByOut"] = t.struct(
        {
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderByOut"])
    types["GoogleAnalyticsAdminV1betaAccessMetricHeaderIn"] = t.struct(
        {"metricName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessMetricHeaderIn"])
    types["GoogleAnalyticsAdminV1betaAccessMetricHeaderOut"] = t.struct(
        {
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessMetricHeaderOut"])
    types["GoogleAnalyticsAdminV1betaPropertyIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "parent": t.string().optional(),
            "industryCategory": t.string().optional(),
            "displayName": t.string(),
            "account": t.string().optional(),
            "propertyType": t.string().optional(),
            "timeZone": t.string(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaPropertyIn"])
    types["GoogleAnalyticsAdminV1betaPropertyOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "parent": t.string().optional(),
            "industryCategory": t.string().optional(),
            "createTime": t.string().optional(),
            "expireTime": t.string().optional(),
            "displayName": t.string(),
            "account": t.string().optional(),
            "updateTime": t.string().optional(),
            "serviceLevel": t.string().optional(),
            "name": t.string().optional(),
            "propertyType": t.string().optional(),
            "timeZone": t.string(),
            "deleteTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaPropertyOut"])
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
    types["GoogleAnalyticsAdminV1betaDataStreamIn"] = t.struct(
        {
            "type": t.string(),
            "androidAppStreamData": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "iosAppStreamData": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataIn"]
            ).optional(),
            "webStreamData": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataIn"]
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataStreamIn"])
    types["GoogleAnalyticsAdminV1betaDataStreamOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "type": t.string(),
            "androidAppStreamData": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamDataOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "iosAppStreamData": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamIosAppStreamDataOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "webStreamData": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamWebStreamDataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataStreamOut"])
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
    types["GoogleAnalyticsAdminV1betaAccountSummaryIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "account": t.string().optional(),
            "name": t.string().optional(),
            "propertySummaries": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaPropertySummaryIn"])
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccountSummaryIn"])
    types["GoogleAnalyticsAdminV1betaAccountSummaryOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "account": t.string().optional(),
            "name": t.string().optional(),
            "propertySummaries": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaPropertySummaryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccountSummaryOut"])
    types["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"] = t.struct(
        {
            "andGroup": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionListIn"]
            ).optional(),
            "accessFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterIn"]
            ).optional(),
            "orGroup": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionListIn"]
            ).optional(),
            "notExpression": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"])
    types["GoogleAnalyticsAdminV1betaAccessFilterExpressionOut"] = t.struct(
        {
            "andGroup": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionListOut"]
            ).optional(),
            "accessFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterOut"]
            ).optional(),
            "orGroup": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionListOut"]
            ).optional(),
            "notExpression": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionOut"]
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
    types["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "resourceType": t.array(t.string()).optional(),
            "latestChangeTime": t.string().optional(),
            "action": t.array(t.string()).optional(),
            "actorEmail": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "earliestChangeTime": t.string().optional(),
            "property": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestIn"])
    types["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "resourceType": t.array(t.string()).optional(),
            "latestChangeTime": t.string().optional(),
            "action": t.array(t.string()).optional(),
            "actorEmail": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "earliestChangeTime": t.string().optional(),
            "property": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequestOut"])
    types["GoogleAnalyticsAdminV1betaListCustomMetricsResponseIn"] = t.struct(
        {
            "customMetrics": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaCustomMetricIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListCustomMetricsResponseIn"])
    types["GoogleAnalyticsAdminV1betaListCustomMetricsResponseOut"] = t.struct(
        {
            "customMetrics": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaCustomMetricOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListCustomMetricsResponseOut"])
    types[
        "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceIn"
    ] = t.struct(
        {
            "firebaseLink": t.proxy(
                renames["GoogleAnalyticsAdminV1betaFirebaseLinkIn"]
            ).optional(),
            "dataRetentionSettings": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsIn"]
            ).optional(),
            "measurementProtocolSecret": t.proxy(
                renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretIn"]
            ).optional(),
            "dataStream": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamIn"]
            ).optional(),
            "account": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccountIn"]
            ).optional(),
            "conversionEvent": t.proxy(
                renames["GoogleAnalyticsAdminV1betaConversionEventIn"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleAnalyticsAdminV1betaPropertyIn"]
            ).optional(),
            "googleAdsLink": t.proxy(
                renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkIn"]
            ).optional(),
        }
    ).named(
        renames["GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceIn"]
    )
    types[
        "GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceOut"
    ] = t.struct(
        {
            "firebaseLink": t.proxy(
                renames["GoogleAnalyticsAdminV1betaFirebaseLinkOut"]
            ).optional(),
            "dataRetentionSettings": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsOut"]
            ).optional(),
            "measurementProtocolSecret": t.proxy(
                renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"]
            ).optional(),
            "dataStream": t.proxy(
                renames["GoogleAnalyticsAdminV1betaDataStreamOut"]
            ).optional(),
            "account": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccountOut"]
            ).optional(),
            "conversionEvent": t.proxy(
                renames["GoogleAnalyticsAdminV1betaConversionEventOut"]
            ).optional(),
            "property": t.proxy(
                renames["GoogleAnalyticsAdminV1betaPropertyOut"]
            ).optional(),
            "googleAdsLink": t.proxy(
                renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResourceOut"]
    )
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
            "eventName": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "custom": t.boolean().optional(),
            "deletable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaConversionEventOut"])
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
    types["GoogleAnalyticsAdminV1betaRunAccessReportRequestIn"] = t.struct(
        {
            "limit": t.string().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
            ).optional(),
            "dimensionFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
            ).optional(),
            "metricFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
            ).optional(),
            "orderBys": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
            ).optional(),
            "offset": t.string().optional(),
            "timeZone": t.string().optional(),
            "returnEntityQuota": t.boolean().optional(),
            "dimensions": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
            ).optional(),
            "dateRanges": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaRunAccessReportRequestIn"])
    types["GoogleAnalyticsAdminV1betaRunAccessReportRequestOut"] = t.struct(
        {
            "limit": t.string().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricOut"])
            ).optional(),
            "dimensionFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionOut"]
            ).optional(),
            "metricFilter": t.proxy(
                renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionOut"]
            ).optional(),
            "orderBys": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByOut"])
            ).optional(),
            "offset": t.string().optional(),
            "timeZone": t.string().optional(),
            "returnEntityQuota": t.boolean().optional(),
            "dimensions": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionOut"])
            ).optional(),
            "dateRanges": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaRunAccessReportRequestOut"])
    types["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseIn"] = t.struct(
        {"accountTicketId": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseIn"])
    types["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut"] = t.struct(
        {
            "accountTicketId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseOut"])
    types["GoogleAnalyticsAdminV1betaAccessDimensionValueIn"] = t.struct(
        {"value": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDimensionValueIn"])
    types["GoogleAnalyticsAdminV1betaAccessDimensionValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDimensionValueOut"])
    types["GoogleAnalyticsAdminV1betaDataRetentionSettingsIn"] = t.struct(
        {
            "resetUserDataOnNewActivity": t.boolean().optional(),
            "eventDataRetention": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsIn"])
    types["GoogleAnalyticsAdminV1betaDataRetentionSettingsOut"] = t.struct(
        {
            "resetUserDataOnNewActivity": t.boolean().optional(),
            "eventDataRetention": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaDataRetentionSettingsOut"])
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
    types["GoogleAnalyticsAdminV1betaAccessStringFilterIn"] = t.struct(
        {
            "caseSensitive": t.boolean().optional(),
            "matchType": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessStringFilterIn"])
    types["GoogleAnalyticsAdminV1betaAccessStringFilterOut"] = t.struct(
        {
            "caseSensitive": t.boolean().optional(),
            "matchType": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessStringFilterOut"])
    types["GoogleAnalyticsAdminV1betaAccessDimensionHeaderIn"] = t.struct(
        {"dimensionName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDimensionHeaderIn"])
    types["GoogleAnalyticsAdminV1betaAccessDimensionHeaderOut"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDimensionHeaderOut"])
    types["GoogleAnalyticsAdminV1betaListFirebaseLinksResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "firebaseLinks": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaFirebaseLinkIn"])
            ).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListFirebaseLinksResponseIn"])
    types["GoogleAnalyticsAdminV1betaListFirebaseLinksResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "firebaseLinks": t.array(
                t.proxy(renames["GoogleAnalyticsAdminV1betaFirebaseLinkOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaListFirebaseLinksResponseOut"])
    types["GoogleAnalyticsAdminV1betaAccessMetricIn"] = t.struct(
        {"metricName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
    types["GoogleAnalyticsAdminV1betaAccessMetricOut"] = t.struct(
        {
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessMetricOut"])
    types["GoogleAnalyticsAdminV1betaAccessDimensionIn"] = t.struct(
        {"dimensionName": t.string().optional()}
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
    types["GoogleAnalyticsAdminV1betaAccessDimensionOut"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaAccessDimensionOut"])
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
            "scope": t.string(),
            "displayName": t.string(),
            "parameterName": t.string(),
            "name": t.string().optional(),
            "disallowAdsPersonalization": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaCustomDimensionOut"])
    types["GoogleAnalyticsAdminV1betaGoogleAdsLinkIn"] = t.struct(
        {
            "customerId": t.string().optional(),
            "adsPersonalizationEnabled": t.boolean().optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkIn"])
    types["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"] = t.struct(
        {
            "customerId": t.string().optional(),
            "updateTime": t.string().optional(),
            "adsPersonalizationEnabled": t.boolean().optional(),
            "canManageClients": t.boolean().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "creatorEmailAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsAdminV1betaGoogleAdsLinkOut"])

    functions = {}
    functions["accountsDelete"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsSearchChangeHistoryEvents"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsList"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsRunAccessReport"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProvisionAccountTicket"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsPatch"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsGetDataSharingSettings"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsGet"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesPatch"] = analyticsadmin.post(
        "v1beta/{entity}:runAccessReport",
        t.struct(
            {
                "entity": t.string().optional(),
                "limit": t.string().optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
                ).optional(),
                "dimensionFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "metricFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "orderBys": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
                ).optional(),
                "offset": t.string().optional(),
                "timeZone": t.string().optional(),
                "returnEntityQuota": t.boolean().optional(),
                "dimensions": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
                ).optional(),
                "dateRanges": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGet"] = analyticsadmin.post(
        "v1beta/{entity}:runAccessReport",
        t.struct(
            {
                "entity": t.string().optional(),
                "limit": t.string().optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
                ).optional(),
                "dimensionFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "metricFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "orderBys": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
                ).optional(),
                "offset": t.string().optional(),
                "timeZone": t.string().optional(),
                "returnEntityQuota": t.boolean().optional(),
                "dimensions": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
                ).optional(),
                "dateRanges": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGetDataRetentionSettings"] = analyticsadmin.post(
        "v1beta/{entity}:runAccessReport",
        t.struct(
            {
                "entity": t.string().optional(),
                "limit": t.string().optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
                ).optional(),
                "dimensionFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "metricFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "orderBys": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
                ).optional(),
                "offset": t.string().optional(),
                "timeZone": t.string().optional(),
                "returnEntityQuota": t.boolean().optional(),
                "dimensions": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
                ).optional(),
                "dateRanges": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesUpdateDataRetentionSettings"] = analyticsadmin.post(
        "v1beta/{entity}:runAccessReport",
        t.struct(
            {
                "entity": t.string().optional(),
                "limit": t.string().optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
                ).optional(),
                "dimensionFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "metricFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "orderBys": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
                ).optional(),
                "offset": t.string().optional(),
                "timeZone": t.string().optional(),
                "returnEntityQuota": t.boolean().optional(),
                "dimensions": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
                ).optional(),
                "dateRanges": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesList"] = analyticsadmin.post(
        "v1beta/{entity}:runAccessReport",
        t.struct(
            {
                "entity": t.string().optional(),
                "limit": t.string().optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
                ).optional(),
                "dimensionFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "metricFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "orderBys": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
                ).optional(),
                "offset": t.string().optional(),
                "timeZone": t.string().optional(),
                "returnEntityQuota": t.boolean().optional(),
                "dimensions": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
                ).optional(),
                "dateRanges": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCreate"] = analyticsadmin.post(
        "v1beta/{entity}:runAccessReport",
        t.struct(
            {
                "entity": t.string().optional(),
                "limit": t.string().optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
                ).optional(),
                "dimensionFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "metricFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "orderBys": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
                ).optional(),
                "offset": t.string().optional(),
                "timeZone": t.string().optional(),
                "returnEntityQuota": t.boolean().optional(),
                "dimensions": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
                ).optional(),
                "dateRanges": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesDelete"] = analyticsadmin.post(
        "v1beta/{entity}:runAccessReport",
        t.struct(
            {
                "entity": t.string().optional(),
                "limit": t.string().optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
                ).optional(),
                "dimensionFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "metricFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "orderBys": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
                ).optional(),
                "offset": t.string().optional(),
                "timeZone": t.string().optional(),
                "returnEntityQuota": t.boolean().optional(),
                "dimensions": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
                ).optional(),
                "dateRanges": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesAcknowledgeUserDataCollection"] = analyticsadmin.post(
        "v1beta/{entity}:runAccessReport",
        t.struct(
            {
                "entity": t.string().optional(),
                "limit": t.string().optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
                ).optional(),
                "dimensionFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "metricFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "orderBys": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
                ).optional(),
                "offset": t.string().optional(),
                "timeZone": t.string().optional(),
                "returnEntityQuota": t.boolean().optional(),
                "dimensions": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
                ).optional(),
                "dateRanges": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesRunAccessReport"] = analyticsadmin.post(
        "v1beta/{entity}:runAccessReport",
        t.struct(
            {
                "entity": t.string().optional(),
                "limit": t.string().optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessMetricIn"])
                ).optional(),
                "dimensionFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "metricFilter": t.proxy(
                    renames["GoogleAnalyticsAdminV1betaAccessFilterExpressionIn"]
                ).optional(),
                "orderBys": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessOrderByIn"])
                ).optional(),
                "offset": t.string().optional(),
                "timeZone": t.string().optional(),
                "returnEntityQuota": t.boolean().optional(),
                "dimensions": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDimensionIn"])
                ).optional(),
                "dateRanges": t.array(
                    t.proxy(renames["GoogleAnalyticsAdminV1betaAccessDateRangeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaRunAccessReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomDimensionsPatch"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaCustomDimensionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomDimensionsCreate"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaCustomDimensionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomDimensionsArchive"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaCustomDimensionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomDimensionsList"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaCustomDimensionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomDimensionsGet"] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaCustomDimensionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesFirebaseLinksDelete"] = analyticsadmin.get(
        "v1beta/{parent}/firebaseLinks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaListFirebaseLinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesFirebaseLinksCreate"] = analyticsadmin.get(
        "v1beta/{parent}/firebaseLinks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaListFirebaseLinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesFirebaseLinksList"] = analyticsadmin.get(
        "v1beta/{parent}/firebaseLinks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaListFirebaseLinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGoogleAdsLinksCreate"] = analyticsadmin.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGoogleAdsLinksList"] = analyticsadmin.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGoogleAdsLinksPatch"] = analyticsadmin.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGoogleAdsLinksDelete"] = analyticsadmin.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesDataStreamsList"] = analyticsadmin.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesDataStreamsPatch"] = analyticsadmin.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesDataStreamsGet"] = analyticsadmin.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesDataStreamsCreate"] = analyticsadmin.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesDataStreamsDelete"] = analyticsadmin.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "propertiesDataStreamsMeasurementProtocolSecretsCreate"
    ] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "propertiesDataStreamsMeasurementProtocolSecretsList"
    ] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "propertiesDataStreamsMeasurementProtocolSecretsPatch"
    ] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "propertiesDataStreamsMeasurementProtocolSecretsDelete"
    ] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "propertiesDataStreamsMeasurementProtocolSecretsGet"
    ] = analyticsadmin.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAnalyticsAdminV1betaMeasurementProtocolSecretOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesConversionEventsGet"] = analyticsadmin.get(
        "v1beta/{parent}/conversionEvents",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaListConversionEventsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomMetricsPatch"] = analyticsadmin.get(
        "v1beta/{parent}/customMetrics",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaListCustomMetricsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomMetricsGet"] = analyticsadmin.get(
        "v1beta/{parent}/customMetrics",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaListCustomMetricsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomMetricsCreate"] = analyticsadmin.get(
        "v1beta/{parent}/customMetrics",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaListCustomMetricsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomMetricsArchive"] = analyticsadmin.get(
        "v1beta/{parent}/customMetrics",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaListCustomMetricsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCustomMetricsList"] = analyticsadmin.get(
        "v1beta/{parent}/customMetrics",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAnalyticsAdminV1betaListCustomMetricsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountSummariesList"] = analyticsadmin.get(
        "v1beta/accountSummaries",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
