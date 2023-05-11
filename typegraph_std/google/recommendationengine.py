from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_recommendationengine() -> Import:
    recommendationengine = HTTPRuntime("https://recommendationengine.googleapis.com/")

    renames = {
        "ErrorResponse": "_recommendationengine_1_ErrorResponse",
        "GoogleCloudRecommendationengineV1beta1PurchaseTransactionIn": "_recommendationengine_2_GoogleCloudRecommendationengineV1beta1PurchaseTransactionIn",
        "GoogleCloudRecommendationengineV1beta1PurchaseTransactionOut": "_recommendationengine_3_GoogleCloudRecommendationengineV1beta1PurchaseTransactionOut",
        "GoogleCloudRecommendationengineV1beta1RejoinUserEventsRequestIn": "_recommendationengine_4_GoogleCloudRecommendationengineV1beta1RejoinUserEventsRequestIn",
        "GoogleCloudRecommendationengineV1beta1RejoinUserEventsRequestOut": "_recommendationengine_5_GoogleCloudRecommendationengineV1beta1RejoinUserEventsRequestOut",
        "GoogleCloudRecommendationengineV1beta1RejoinUserEventsResponseIn": "_recommendationengine_6_GoogleCloudRecommendationengineV1beta1RejoinUserEventsResponseIn",
        "GoogleCloudRecommendationengineV1beta1RejoinUserEventsResponseOut": "_recommendationengine_7_GoogleCloudRecommendationengineV1beta1RejoinUserEventsResponseOut",
        "GoogleRpcStatusIn": "_recommendationengine_8_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_recommendationengine_9_GoogleRpcStatusOut",
        "GoogleCloudRecommendationengineV1beta1FeatureMapStringListIn": "_recommendationengine_10_GoogleCloudRecommendationengineV1beta1FeatureMapStringListIn",
        "GoogleCloudRecommendationengineV1beta1FeatureMapStringListOut": "_recommendationengine_11_GoogleCloudRecommendationengineV1beta1FeatureMapStringListOut",
        "GoogleCloudRecommendationengineV1beta1UserEventIn": "_recommendationengine_12_GoogleCloudRecommendationengineV1beta1UserEventIn",
        "GoogleCloudRecommendationengineV1beta1UserEventOut": "_recommendationengine_13_GoogleCloudRecommendationengineV1beta1UserEventOut",
        "GoogleCloudRecommendationengineV1beta1RejoinUserEventsMetadataIn": "_recommendationengine_14_GoogleCloudRecommendationengineV1beta1RejoinUserEventsMetadataIn",
        "GoogleCloudRecommendationengineV1beta1RejoinUserEventsMetadataOut": "_recommendationengine_15_GoogleCloudRecommendationengineV1beta1RejoinUserEventsMetadataOut",
        "GoogleCloudRecommendationengineV1beta1ImportErrorsConfigIn": "_recommendationengine_16_GoogleCloudRecommendationengineV1beta1ImportErrorsConfigIn",
        "GoogleCloudRecommendationengineV1beta1ImportErrorsConfigOut": "_recommendationengine_17_GoogleCloudRecommendationengineV1beta1ImportErrorsConfigOut",
        "GoogleCloudRecommendationengineV1beta1ImageIn": "_recommendationengine_18_GoogleCloudRecommendationengineV1beta1ImageIn",
        "GoogleCloudRecommendationengineV1beta1ImageOut": "_recommendationengine_19_GoogleCloudRecommendationengineV1beta1ImageOut",
        "GoogleCloudRecommendationengineV1beta1PurgeUserEventsResponseIn": "_recommendationengine_20_GoogleCloudRecommendationengineV1beta1PurgeUserEventsResponseIn",
        "GoogleCloudRecommendationengineV1beta1PurgeUserEventsResponseOut": "_recommendationengine_21_GoogleCloudRecommendationengineV1beta1PurgeUserEventsResponseOut",
        "GoogleCloudRecommendationengineV1alphaTuningMetadataIn": "_recommendationengine_22_GoogleCloudRecommendationengineV1alphaTuningMetadataIn",
        "GoogleCloudRecommendationengineV1alphaTuningMetadataOut": "_recommendationengine_23_GoogleCloudRecommendationengineV1alphaTuningMetadataOut",
        "GoogleCloudRecommendationengineV1beta1UserInfoIn": "_recommendationengine_24_GoogleCloudRecommendationengineV1beta1UserInfoIn",
        "GoogleCloudRecommendationengineV1beta1UserInfoOut": "_recommendationengine_25_GoogleCloudRecommendationengineV1beta1UserInfoOut",
        "GoogleCloudRecommendationengineV1beta1UserEventInlineSourceIn": "_recommendationengine_26_GoogleCloudRecommendationengineV1beta1UserEventInlineSourceIn",
        "GoogleCloudRecommendationengineV1beta1UserEventInlineSourceOut": "_recommendationengine_27_GoogleCloudRecommendationengineV1beta1UserEventInlineSourceOut",
        "GoogleCloudRecommendationengineV1beta1FeatureMapIn": "_recommendationengine_28_GoogleCloudRecommendationengineV1beta1FeatureMapIn",
        "GoogleCloudRecommendationengineV1beta1FeatureMapOut": "_recommendationengine_29_GoogleCloudRecommendationengineV1beta1FeatureMapOut",
        "GoogleApiHttpBodyIn": "_recommendationengine_30_GoogleApiHttpBodyIn",
        "GoogleApiHttpBodyOut": "_recommendationengine_31_GoogleApiHttpBodyOut",
        "GoogleCloudRecommendationengineV1beta1PredictResponsePredictionResultIn": "_recommendationengine_32_GoogleCloudRecommendationengineV1beta1PredictResponsePredictionResultIn",
        "GoogleCloudRecommendationengineV1beta1PredictResponsePredictionResultOut": "_recommendationengine_33_GoogleCloudRecommendationengineV1beta1PredictResponsePredictionResultOut",
        "GoogleCloudRecommendationengineV1beta1CatalogIn": "_recommendationengine_34_GoogleCloudRecommendationengineV1beta1CatalogIn",
        "GoogleCloudRecommendationengineV1beta1CatalogOut": "_recommendationengine_35_GoogleCloudRecommendationengineV1beta1CatalogOut",
        "GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistrationIn": "_recommendationengine_36_GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistrationIn",
        "GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistrationOut": "_recommendationengine_37_GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistrationOut",
        "GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchyIn": "_recommendationengine_38_GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchyIn",
        "GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchyOut": "_recommendationengine_39_GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchyOut",
        "GoogleCloudRecommendationengineV1beta1FeatureMapFloatListIn": "_recommendationengine_40_GoogleCloudRecommendationengineV1beta1FeatureMapFloatListIn",
        "GoogleCloudRecommendationengineV1beta1FeatureMapFloatListOut": "_recommendationengine_41_GoogleCloudRecommendationengineV1beta1FeatureMapFloatListOut",
        "GoogleCloudRecommendationengineV1alphaRejoinCatalogMetadataIn": "_recommendationengine_42_GoogleCloudRecommendationengineV1alphaRejoinCatalogMetadataIn",
        "GoogleCloudRecommendationengineV1alphaRejoinCatalogMetadataOut": "_recommendationengine_43_GoogleCloudRecommendationengineV1alphaRejoinCatalogMetadataOut",
        "GoogleCloudRecommendationengineV1beta1CatalogInlineSourceIn": "_recommendationengine_44_GoogleCloudRecommendationengineV1beta1CatalogInlineSourceIn",
        "GoogleCloudRecommendationengineV1beta1CatalogInlineSourceOut": "_recommendationengine_45_GoogleCloudRecommendationengineV1beta1CatalogInlineSourceOut",
        "GoogleCloudRecommendationengineV1beta1EventDetailIn": "_recommendationengine_46_GoogleCloudRecommendationengineV1beta1EventDetailIn",
        "GoogleCloudRecommendationengineV1beta1EventDetailOut": "_recommendationengine_47_GoogleCloudRecommendationengineV1beta1EventDetailOut",
        "GoogleCloudRecommendationengineV1beta1PurgeUserEventsRequestIn": "_recommendationengine_48_GoogleCloudRecommendationengineV1beta1PurgeUserEventsRequestIn",
        "GoogleCloudRecommendationengineV1beta1PurgeUserEventsRequestOut": "_recommendationengine_49_GoogleCloudRecommendationengineV1beta1PurgeUserEventsRequestOut",
        "GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRangeIn": "_recommendationengine_50_GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRangeIn",
        "GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRangeOut": "_recommendationengine_51_GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRangeOut",
        "GoogleLongrunningOperationIn": "_recommendationengine_52_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_recommendationengine_53_GoogleLongrunningOperationOut",
        "GoogleCloudRecommendationengineV1beta1ImportCatalogItemsResponseIn": "_recommendationengine_54_GoogleCloudRecommendationengineV1beta1ImportCatalogItemsResponseIn",
        "GoogleCloudRecommendationengineV1beta1ImportCatalogItemsResponseOut": "_recommendationengine_55_GoogleCloudRecommendationengineV1beta1ImportCatalogItemsResponseOut",
        "GoogleCloudRecommendationengineV1beta1UserEventImportSummaryIn": "_recommendationengine_56_GoogleCloudRecommendationengineV1beta1UserEventImportSummaryIn",
        "GoogleCloudRecommendationengineV1beta1UserEventImportSummaryOut": "_recommendationengine_57_GoogleCloudRecommendationengineV1beta1UserEventImportSummaryOut",
        "GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponseIn": "_recommendationengine_58_GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponseIn",
        "GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponseOut": "_recommendationengine_59_GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponseOut",
        "GoogleCloudRecommendationengineV1alphaTuningResponseIn": "_recommendationengine_60_GoogleCloudRecommendationengineV1alphaTuningResponseIn",
        "GoogleCloudRecommendationengineV1alphaTuningResponseOut": "_recommendationengine_61_GoogleCloudRecommendationengineV1alphaTuningResponseOut",
        "GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPriceIn": "_recommendationengine_62_GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPriceIn",
        "GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPriceOut": "_recommendationengine_63_GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPriceOut",
        "GoogleCloudRecommendationengineV1beta1ImportUserEventsResponseIn": "_recommendationengine_64_GoogleCloudRecommendationengineV1beta1ImportUserEventsResponseIn",
        "GoogleCloudRecommendationengineV1beta1ImportUserEventsResponseOut": "_recommendationengine_65_GoogleCloudRecommendationengineV1beta1ImportUserEventsResponseOut",
        "GoogleCloudRecommendationengineV1beta1PredictRequestIn": "_recommendationengine_66_GoogleCloudRecommendationengineV1beta1PredictRequestIn",
        "GoogleCloudRecommendationengineV1beta1PredictRequestOut": "_recommendationengine_67_GoogleCloudRecommendationengineV1beta1PredictRequestOut",
        "GoogleLongrunningListOperationsResponseIn": "_recommendationengine_68_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_recommendationengine_69_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponseIn": "_recommendationengine_70_GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponseIn",
        "GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponseOut": "_recommendationengine_71_GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponseOut",
        "GoogleCloudRecommendationengineV1beta1ImportCatalogItemsRequestIn": "_recommendationengine_72_GoogleCloudRecommendationengineV1beta1ImportCatalogItemsRequestIn",
        "GoogleCloudRecommendationengineV1beta1ImportCatalogItemsRequestOut": "_recommendationengine_73_GoogleCloudRecommendationengineV1beta1ImportCatalogItemsRequestOut",
        "GoogleCloudRecommendationengineV1beta1CatalogItemLevelConfigIn": "_recommendationengine_74_GoogleCloudRecommendationengineV1beta1CatalogItemLevelConfigIn",
        "GoogleCloudRecommendationengineV1beta1CatalogItemLevelConfigOut": "_recommendationengine_75_GoogleCloudRecommendationengineV1beta1CatalogItemLevelConfigOut",
        "GoogleCloudRecommendationengineV1alphaRejoinCatalogResponseIn": "_recommendationengine_76_GoogleCloudRecommendationengineV1alphaRejoinCatalogResponseIn",
        "GoogleCloudRecommendationengineV1alphaRejoinCatalogResponseOut": "_recommendationengine_77_GoogleCloudRecommendationengineV1alphaRejoinCatalogResponseOut",
        "GoogleCloudRecommendationengineV1beta1ListUserEventsResponseIn": "_recommendationengine_78_GoogleCloudRecommendationengineV1beta1ListUserEventsResponseIn",
        "GoogleCloudRecommendationengineV1beta1ListUserEventsResponseOut": "_recommendationengine_79_GoogleCloudRecommendationengineV1beta1ListUserEventsResponseOut",
        "GoogleCloudRecommendationengineV1beta1ImportMetadataIn": "_recommendationengine_80_GoogleCloudRecommendationengineV1beta1ImportMetadataIn",
        "GoogleCloudRecommendationengineV1beta1ImportMetadataOut": "_recommendationengine_81_GoogleCloudRecommendationengineV1beta1ImportMetadataOut",
        "GoogleCloudRecommendationengineV1beta1ImportUserEventsRequestIn": "_recommendationengine_82_GoogleCloudRecommendationengineV1beta1ImportUserEventsRequestIn",
        "GoogleCloudRecommendationengineV1beta1ImportUserEventsRequestOut": "_recommendationengine_83_GoogleCloudRecommendationengineV1beta1ImportUserEventsRequestOut",
        "GoogleCloudRecommendationengineV1beta1BigQuerySourceIn": "_recommendationengine_84_GoogleCloudRecommendationengineV1beta1BigQuerySourceIn",
        "GoogleCloudRecommendationengineV1beta1BigQuerySourceOut": "_recommendationengine_85_GoogleCloudRecommendationengineV1beta1BigQuerySourceOut",
        "GoogleCloudRecommendationengineV1beta1CreatePredictionApiKeyRegistrationRequestIn": "_recommendationengine_86_GoogleCloudRecommendationengineV1beta1CreatePredictionApiKeyRegistrationRequestIn",
        "GoogleCloudRecommendationengineV1beta1CreatePredictionApiKeyRegistrationRequestOut": "_recommendationengine_87_GoogleCloudRecommendationengineV1beta1CreatePredictionApiKeyRegistrationRequestOut",
        "GoogleProtobufEmptyIn": "_recommendationengine_88_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_recommendationengine_89_GoogleProtobufEmptyOut",
        "GoogleCloudRecommendationengineV1beta1PredictResponseIn": "_recommendationengine_90_GoogleCloudRecommendationengineV1beta1PredictResponseIn",
        "GoogleCloudRecommendationengineV1beta1PredictResponseOut": "_recommendationengine_91_GoogleCloudRecommendationengineV1beta1PredictResponseOut",
        "GoogleCloudRecommendationengineV1beta1ListCatalogsResponseIn": "_recommendationengine_92_GoogleCloudRecommendationengineV1beta1ListCatalogsResponseIn",
        "GoogleCloudRecommendationengineV1beta1ListCatalogsResponseOut": "_recommendationengine_93_GoogleCloudRecommendationengineV1beta1ListCatalogsResponseOut",
        "GoogleCloudRecommendationengineV1beta1InputConfigIn": "_recommendationengine_94_GoogleCloudRecommendationengineV1beta1InputConfigIn",
        "GoogleCloudRecommendationengineV1beta1InputConfigOut": "_recommendationengine_95_GoogleCloudRecommendationengineV1beta1InputConfigOut",
        "GoogleCloudRecommendationengineV1beta1CatalogItemIn": "_recommendationengine_96_GoogleCloudRecommendationengineV1beta1CatalogItemIn",
        "GoogleCloudRecommendationengineV1beta1CatalogItemOut": "_recommendationengine_97_GoogleCloudRecommendationengineV1beta1CatalogItemOut",
        "GoogleCloudRecommendationengineV1beta1GcsSourceIn": "_recommendationengine_98_GoogleCloudRecommendationengineV1beta1GcsSourceIn",
        "GoogleCloudRecommendationengineV1beta1GcsSourceOut": "_recommendationengine_99_GoogleCloudRecommendationengineV1beta1GcsSourceOut",
        "GoogleCloudRecommendationengineV1beta1ProductEventDetailIn": "_recommendationengine_100_GoogleCloudRecommendationengineV1beta1ProductEventDetailIn",
        "GoogleCloudRecommendationengineV1beta1ProductEventDetailOut": "_recommendationengine_101_GoogleCloudRecommendationengineV1beta1ProductEventDetailOut",
        "GoogleCloudRecommendationengineV1beta1ProductDetailIn": "_recommendationengine_102_GoogleCloudRecommendationengineV1beta1ProductDetailIn",
        "GoogleCloudRecommendationengineV1beta1ProductDetailOut": "_recommendationengine_103_GoogleCloudRecommendationengineV1beta1ProductDetailOut",
        "GoogleCloudRecommendationengineV1beta1ProductCatalogItemIn": "_recommendationengine_104_GoogleCloudRecommendationengineV1beta1ProductCatalogItemIn",
        "GoogleCloudRecommendationengineV1beta1ProductCatalogItemOut": "_recommendationengine_105_GoogleCloudRecommendationengineV1beta1ProductCatalogItemOut",
        "GoogleCloudRecommendationengineV1beta1PurgeUserEventsMetadataIn": "_recommendationengine_106_GoogleCloudRecommendationengineV1beta1PurgeUserEventsMetadataIn",
        "GoogleCloudRecommendationengineV1beta1PurgeUserEventsMetadataOut": "_recommendationengine_107_GoogleCloudRecommendationengineV1beta1PurgeUserEventsMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudRecommendationengineV1beta1PurchaseTransactionIn"] = t.struct(
        {
            "taxes": t.struct({"_": t.string().optional()}).optional(),
            "currencyCode": t.string(),
            "id": t.string().optional(),
            "costs": t.struct({"_": t.string().optional()}).optional(),
            "revenue": t.number(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1PurchaseTransactionIn"])
    types["GoogleCloudRecommendationengineV1beta1PurchaseTransactionOut"] = t.struct(
        {
            "taxes": t.struct({"_": t.string().optional()}).optional(),
            "currencyCode": t.string(),
            "id": t.string().optional(),
            "costs": t.struct({"_": t.string().optional()}).optional(),
            "revenue": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1PurchaseTransactionOut"])
    types["GoogleCloudRecommendationengineV1beta1RejoinUserEventsRequestIn"] = t.struct(
        {"userEventRejoinScope": t.string()}
    ).named(renames["GoogleCloudRecommendationengineV1beta1RejoinUserEventsRequestIn"])
    types[
        "GoogleCloudRecommendationengineV1beta1RejoinUserEventsRequestOut"
    ] = t.struct(
        {
            "userEventRejoinScope": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecommendationengineV1beta1RejoinUserEventsRequestOut"]
    )
    types[
        "GoogleCloudRecommendationengineV1beta1RejoinUserEventsResponseIn"
    ] = t.struct({"rejoinedUserEventsCount": t.string().optional()}).named(
        renames["GoogleCloudRecommendationengineV1beta1RejoinUserEventsResponseIn"]
    )
    types[
        "GoogleCloudRecommendationengineV1beta1RejoinUserEventsResponseOut"
    ] = t.struct(
        {
            "rejoinedUserEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecommendationengineV1beta1RejoinUserEventsResponseOut"]
    )
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleCloudRecommendationengineV1beta1FeatureMapStringListIn"] = t.struct(
        {"value": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRecommendationengineV1beta1FeatureMapStringListIn"])
    types["GoogleCloudRecommendationengineV1beta1FeatureMapStringListOut"] = t.struct(
        {
            "value": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1FeatureMapStringListOut"])
    types["GoogleCloudRecommendationengineV1beta1UserEventIn"] = t.struct(
        {
            "eventDetail": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1EventDetailIn"]
            ).optional(),
            "userInfo": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1UserInfoIn"]
            ),
            "productEventDetail": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1ProductEventDetailIn"]
            ).optional(),
            "eventSource": t.string().optional(),
            "eventType": t.string(),
            "eventTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1UserEventIn"])
    types["GoogleCloudRecommendationengineV1beta1UserEventOut"] = t.struct(
        {
            "eventDetail": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1EventDetailOut"]
            ).optional(),
            "userInfo": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1UserInfoOut"]
            ),
            "productEventDetail": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1ProductEventDetailOut"]
            ).optional(),
            "eventSource": t.string().optional(),
            "eventType": t.string(),
            "eventTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1UserEventOut"])
    types[
        "GoogleCloudRecommendationengineV1beta1RejoinUserEventsMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudRecommendationengineV1beta1RejoinUserEventsMetadataIn"]
    )
    types[
        "GoogleCloudRecommendationengineV1beta1RejoinUserEventsMetadataOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleCloudRecommendationengineV1beta1RejoinUserEventsMetadataOut"]
    )
    types["GoogleCloudRecommendationengineV1beta1ImportErrorsConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudRecommendationengineV1beta1ImportErrorsConfigIn"])
    types["GoogleCloudRecommendationengineV1beta1ImportErrorsConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1ImportErrorsConfigOut"])
    types["GoogleCloudRecommendationengineV1beta1ImageIn"] = t.struct(
        {
            "uri": t.string(),
            "width": t.integer().optional(),
            "height": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1ImageIn"])
    types["GoogleCloudRecommendationengineV1beta1ImageOut"] = t.struct(
        {
            "uri": t.string(),
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1ImageOut"])
    types["GoogleCloudRecommendationengineV1beta1PurgeUserEventsResponseIn"] = t.struct(
        {
            "userEventsSample": t.array(
                t.proxy(renames["GoogleCloudRecommendationengineV1beta1UserEventIn"])
            ).optional(),
            "purgedEventsCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1PurgeUserEventsResponseIn"])
    types[
        "GoogleCloudRecommendationengineV1beta1PurgeUserEventsResponseOut"
    ] = t.struct(
        {
            "userEventsSample": t.array(
                t.proxy(renames["GoogleCloudRecommendationengineV1beta1UserEventOut"])
            ).optional(),
            "purgedEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecommendationengineV1beta1PurgeUserEventsResponseOut"]
    )
    types["GoogleCloudRecommendationengineV1alphaTuningMetadataIn"] = t.struct(
        {"recommendationModel": t.string().optional()}
    ).named(renames["GoogleCloudRecommendationengineV1alphaTuningMetadataIn"])
    types["GoogleCloudRecommendationengineV1alphaTuningMetadataOut"] = t.struct(
        {
            "recommendationModel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1alphaTuningMetadataOut"])
    types["GoogleCloudRecommendationengineV1beta1UserInfoIn"] = t.struct(
        {
            "directUserRequest": t.boolean().optional(),
            "userAgent": t.string().optional(),
            "visitorId": t.string(),
            "userId": t.string().optional(),
            "ipAddress": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1UserInfoIn"])
    types["GoogleCloudRecommendationengineV1beta1UserInfoOut"] = t.struct(
        {
            "directUserRequest": t.boolean().optional(),
            "userAgent": t.string().optional(),
            "visitorId": t.string(),
            "userId": t.string().optional(),
            "ipAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1UserInfoOut"])
    types["GoogleCloudRecommendationengineV1beta1UserEventInlineSourceIn"] = t.struct(
        {
            "userEvents": t.array(
                t.proxy(renames["GoogleCloudRecommendationengineV1beta1UserEventIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1UserEventInlineSourceIn"])
    types["GoogleCloudRecommendationengineV1beta1UserEventInlineSourceOut"] = t.struct(
        {
            "userEvents": t.array(
                t.proxy(renames["GoogleCloudRecommendationengineV1beta1UserEventOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1UserEventInlineSourceOut"])
    types["GoogleCloudRecommendationengineV1beta1FeatureMapIn"] = t.struct(
        {
            "categoricalFeatures": t.struct({"_": t.string().optional()}).optional(),
            "numericalFeatures": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1FeatureMapIn"])
    types["GoogleCloudRecommendationengineV1beta1FeatureMapOut"] = t.struct(
        {
            "categoricalFeatures": t.struct({"_": t.string().optional()}).optional(),
            "numericalFeatures": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1FeatureMapOut"])
    types["GoogleApiHttpBodyIn"] = t.struct(
        {
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "contentType": t.string().optional(),
            "data": t.string().optional(),
        }
    ).named(renames["GoogleApiHttpBodyIn"])
    types["GoogleApiHttpBodyOut"] = t.struct(
        {
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "contentType": t.string().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiHttpBodyOut"])
    types[
        "GoogleCloudRecommendationengineV1beta1PredictResponsePredictionResultIn"
    ] = t.struct(
        {
            "id": t.string().optional(),
            "itemMetadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRecommendationengineV1beta1PredictResponsePredictionResultIn"
        ]
    )
    types[
        "GoogleCloudRecommendationengineV1beta1PredictResponsePredictionResultOut"
    ] = t.struct(
        {
            "id": t.string().optional(),
            "itemMetadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRecommendationengineV1beta1PredictResponsePredictionResultOut"
        ]
    )
    types["GoogleCloudRecommendationengineV1beta1CatalogIn"] = t.struct(
        {
            "catalogItemLevelConfig": t.proxy(
                renames[
                    "GoogleCloudRecommendationengineV1beta1CatalogItemLevelConfigIn"
                ]
            ),
            "displayName": t.string(),
            "defaultEventStoreId": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1CatalogIn"])
    types["GoogleCloudRecommendationengineV1beta1CatalogOut"] = t.struct(
        {
            "catalogItemLevelConfig": t.proxy(
                renames[
                    "GoogleCloudRecommendationengineV1beta1CatalogItemLevelConfigOut"
                ]
            ),
            "displayName": t.string(),
            "defaultEventStoreId": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1CatalogOut"])
    types[
        "GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistrationIn"
    ] = t.struct({"apiKey": t.string().optional()}).named(
        renames["GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistrationIn"]
    )
    types[
        "GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistrationOut"
    ] = t.struct(
        {
            "apiKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistrationOut"]
    )
    types[
        "GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchyIn"
    ] = t.struct({"categories": t.array(t.string())}).named(
        renames["GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchyIn"]
    )
    types[
        "GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchyOut"
    ] = t.struct(
        {
            "categories": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchyOut"]
    )
    types["GoogleCloudRecommendationengineV1beta1FeatureMapFloatListIn"] = t.struct(
        {"value": t.array(t.number()).optional()}
    ).named(renames["GoogleCloudRecommendationengineV1beta1FeatureMapFloatListIn"])
    types["GoogleCloudRecommendationengineV1beta1FeatureMapFloatListOut"] = t.struct(
        {
            "value": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1FeatureMapFloatListOut"])
    types["GoogleCloudRecommendationengineV1alphaRejoinCatalogMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRecommendationengineV1alphaRejoinCatalogMetadataIn"])
    types["GoogleCloudRecommendationengineV1alphaRejoinCatalogMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecommendationengineV1alphaRejoinCatalogMetadataOut"])
    types["GoogleCloudRecommendationengineV1beta1CatalogInlineSourceIn"] = t.struct(
        {
            "catalogItems": t.array(
                t.proxy(renames["GoogleCloudRecommendationengineV1beta1CatalogItemIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1CatalogInlineSourceIn"])
    types["GoogleCloudRecommendationengineV1beta1CatalogInlineSourceOut"] = t.struct(
        {
            "catalogItems": t.array(
                t.proxy(renames["GoogleCloudRecommendationengineV1beta1CatalogItemOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1CatalogInlineSourceOut"])
    types["GoogleCloudRecommendationengineV1beta1EventDetailIn"] = t.struct(
        {
            "referrerUri": t.string().optional(),
            "eventAttributes": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1FeatureMapIn"]
            ).optional(),
            "recommendationToken": t.string().optional(),
            "pageViewId": t.string().optional(),
            "uri": t.string().optional(),
            "experimentIds": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1EventDetailIn"])
    types["GoogleCloudRecommendationengineV1beta1EventDetailOut"] = t.struct(
        {
            "referrerUri": t.string().optional(),
            "eventAttributes": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1FeatureMapOut"]
            ).optional(),
            "recommendationToken": t.string().optional(),
            "pageViewId": t.string().optional(),
            "uri": t.string().optional(),
            "experimentIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1EventDetailOut"])
    types["GoogleCloudRecommendationengineV1beta1PurgeUserEventsRequestIn"] = t.struct(
        {"force": t.boolean().optional(), "filter": t.string()}
    ).named(renames["GoogleCloudRecommendationengineV1beta1PurgeUserEventsRequestIn"])
    types["GoogleCloudRecommendationengineV1beta1PurgeUserEventsRequestOut"] = t.struct(
        {
            "force": t.boolean().optional(),
            "filter": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1PurgeUserEventsRequestOut"])
    types[
        "GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRangeIn"
    ] = t.struct({"max": t.number(), "min": t.number()}).named(
        renames["GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRangeIn"]
    )
    types[
        "GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRangeOut"
    ] = t.struct(
        {
            "max": t.number(),
            "min": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRangeOut"]
    )
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types[
        "GoogleCloudRecommendationengineV1beta1ImportCatalogItemsResponseIn"
    ] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1ImportErrorsConfigIn"]
            ).optional(),
        }
    ).named(
        renames["GoogleCloudRecommendationengineV1beta1ImportCatalogItemsResponseIn"]
    )
    types[
        "GoogleCloudRecommendationengineV1beta1ImportCatalogItemsResponseOut"
    ] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1ImportErrorsConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecommendationengineV1beta1ImportCatalogItemsResponseOut"]
    )
    types["GoogleCloudRecommendationengineV1beta1UserEventImportSummaryIn"] = t.struct(
        {
            "unjoinedEventsCount": t.string().optional(),
            "joinedEventsCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1UserEventImportSummaryIn"])
    types["GoogleCloudRecommendationengineV1beta1UserEventImportSummaryOut"] = t.struct(
        {
            "unjoinedEventsCount": t.string().optional(),
            "joinedEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1UserEventImportSummaryOut"])
    types[
        "GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "predictionApiKeyRegistrations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistrationIn"
                    ]
                )
            ).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponseIn"
        ]
    )
    types[
        "GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "predictionApiKeyRegistrations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistrationOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponseOut"
        ]
    )
    types["GoogleCloudRecommendationengineV1alphaTuningResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRecommendationengineV1alphaTuningResponseIn"])
    types["GoogleCloudRecommendationengineV1alphaTuningResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecommendationengineV1alphaTuningResponseOut"])
    types[
        "GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPriceIn"
    ] = t.struct(
        {"displayPrice": t.number().optional(), "originalPrice": t.number().optional()}
    ).named(
        renames["GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPriceIn"]
    )
    types[
        "GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPriceOut"
    ] = t.struct(
        {
            "displayPrice": t.number().optional(),
            "originalPrice": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPriceOut"]
    )
    types[
        "GoogleCloudRecommendationengineV1beta1ImportUserEventsResponseIn"
    ] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "importSummary": t.proxy(
                renames[
                    "GoogleCloudRecommendationengineV1beta1UserEventImportSummaryIn"
                ]
            ).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1ImportErrorsConfigIn"]
            ).optional(),
        }
    ).named(
        renames["GoogleCloudRecommendationengineV1beta1ImportUserEventsResponseIn"]
    )
    types[
        "GoogleCloudRecommendationengineV1beta1ImportUserEventsResponseOut"
    ] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "importSummary": t.proxy(
                renames[
                    "GoogleCloudRecommendationengineV1beta1UserEventImportSummaryOut"
                ]
            ).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1ImportErrorsConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecommendationengineV1beta1ImportUserEventsResponseOut"]
    )
    types["GoogleCloudRecommendationengineV1beta1PredictRequestIn"] = t.struct(
        {
            "dryRun": t.boolean().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "pageSize": t.integer().optional(),
            "filter": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pageToken": t.string().optional(),
            "userEvent": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1UserEventIn"]
            ),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1PredictRequestIn"])
    types["GoogleCloudRecommendationengineV1beta1PredictRequestOut"] = t.struct(
        {
            "dryRun": t.boolean().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "pageSize": t.integer().optional(),
            "filter": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pageToken": t.string().optional(),
            "userEvent": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1UserEventOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1PredictRequestOut"])
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
    types[
        "GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponseIn"
    ] = t.struct(
        {
            "catalogItems": t.array(
                t.proxy(renames["GoogleCloudRecommendationengineV1beta1CatalogItemIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponseIn"]
    )
    types[
        "GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponseOut"
    ] = t.struct(
        {
            "catalogItems": t.array(
                t.proxy(renames["GoogleCloudRecommendationengineV1beta1CatalogItemOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponseOut"]
    )
    types[
        "GoogleCloudRecommendationengineV1beta1ImportCatalogItemsRequestIn"
    ] = t.struct(
        {
            "requestId": t.string().optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1InputConfigIn"]
            ),
            "updateMask": t.string().optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1ImportErrorsConfigIn"]
            ).optional(),
        }
    ).named(
        renames["GoogleCloudRecommendationengineV1beta1ImportCatalogItemsRequestIn"]
    )
    types[
        "GoogleCloudRecommendationengineV1beta1ImportCatalogItemsRequestOut"
    ] = t.struct(
        {
            "requestId": t.string().optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1InputConfigOut"]
            ),
            "updateMask": t.string().optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1ImportErrorsConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecommendationengineV1beta1ImportCatalogItemsRequestOut"]
    )
    types["GoogleCloudRecommendationengineV1beta1CatalogItemLevelConfigIn"] = t.struct(
        {
            "predictItemLevel": t.string().optional(),
            "eventItemLevel": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1CatalogItemLevelConfigIn"])
    types["GoogleCloudRecommendationengineV1beta1CatalogItemLevelConfigOut"] = t.struct(
        {
            "predictItemLevel": t.string().optional(),
            "eventItemLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1CatalogItemLevelConfigOut"])
    types["GoogleCloudRecommendationengineV1alphaRejoinCatalogResponseIn"] = t.struct(
        {"rejoinedUserEventsCount": t.string().optional()}
    ).named(renames["GoogleCloudRecommendationengineV1alphaRejoinCatalogResponseIn"])
    types["GoogleCloudRecommendationengineV1alphaRejoinCatalogResponseOut"] = t.struct(
        {
            "rejoinedUserEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1alphaRejoinCatalogResponseOut"])
    types["GoogleCloudRecommendationengineV1beta1ListUserEventsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "userEvents": t.array(
                t.proxy(renames["GoogleCloudRecommendationengineV1beta1UserEventIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1ListUserEventsResponseIn"])
    types["GoogleCloudRecommendationengineV1beta1ListUserEventsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "userEvents": t.array(
                t.proxy(renames["GoogleCloudRecommendationengineV1beta1UserEventOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1ListUserEventsResponseOut"])
    types["GoogleCloudRecommendationengineV1beta1ImportMetadataIn"] = t.struct(
        {
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
            "createTime": t.string().optional(),
            "requestId": t.string().optional(),
            "operationName": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1ImportMetadataIn"])
    types["GoogleCloudRecommendationengineV1beta1ImportMetadataOut"] = t.struct(
        {
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
            "createTime": t.string().optional(),
            "requestId": t.string().optional(),
            "operationName": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1ImportMetadataOut"])
    types["GoogleCloudRecommendationengineV1beta1ImportUserEventsRequestIn"] = t.struct(
        {
            "errorsConfig": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1ImportErrorsConfigIn"]
            ).optional(),
            "requestId": t.string().optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1InputConfigIn"]
            ),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1ImportUserEventsRequestIn"])
    types[
        "GoogleCloudRecommendationengineV1beta1ImportUserEventsRequestOut"
    ] = t.struct(
        {
            "errorsConfig": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1ImportErrorsConfigOut"]
            ).optional(),
            "requestId": t.string().optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1InputConfigOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecommendationengineV1beta1ImportUserEventsRequestOut"]
    )
    types["GoogleCloudRecommendationengineV1beta1BigQuerySourceIn"] = t.struct(
        {
            "datasetId": t.string(),
            "tableId": t.string(),
            "projectId": t.string().optional(),
            "gcsStagingDir": t.string().optional(),
            "dataSchema": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1BigQuerySourceIn"])
    types["GoogleCloudRecommendationengineV1beta1BigQuerySourceOut"] = t.struct(
        {
            "datasetId": t.string(),
            "tableId": t.string(),
            "projectId": t.string().optional(),
            "gcsStagingDir": t.string().optional(),
            "dataSchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1BigQuerySourceOut"])
    types[
        "GoogleCloudRecommendationengineV1beta1CreatePredictionApiKeyRegistrationRequestIn"
    ] = t.struct(
        {
            "predictionApiKeyRegistration": t.proxy(
                renames[
                    "GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistrationIn"
                ]
            )
        }
    ).named(
        renames[
            "GoogleCloudRecommendationengineV1beta1CreatePredictionApiKeyRegistrationRequestIn"
        ]
    )
    types[
        "GoogleCloudRecommendationengineV1beta1CreatePredictionApiKeyRegistrationRequestOut"
    ] = t.struct(
        {
            "predictionApiKeyRegistration": t.proxy(
                renames[
                    "GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistrationOut"
                ]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRecommendationengineV1beta1CreatePredictionApiKeyRegistrationRequestOut"
        ]
    )
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudRecommendationengineV1beta1PredictResponseIn"] = t.struct(
        {
            "dryRun": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "recommendationToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "itemsMissingInCatalog": t.array(t.string()).optional(),
            "results": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecommendationengineV1beta1PredictResponsePredictionResultIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1PredictResponseIn"])
    types["GoogleCloudRecommendationengineV1beta1PredictResponseOut"] = t.struct(
        {
            "dryRun": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "recommendationToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "itemsMissingInCatalog": t.array(t.string()).optional(),
            "results": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecommendationengineV1beta1PredictResponsePredictionResultOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1PredictResponseOut"])
    types["GoogleCloudRecommendationengineV1beta1ListCatalogsResponseIn"] = t.struct(
        {"nextPageToken": t.string().optional()}
    ).named(renames["GoogleCloudRecommendationengineV1beta1ListCatalogsResponseIn"])
    types["GoogleCloudRecommendationengineV1beta1ListCatalogsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "catalogs": t.array(
                t.proxy(renames["GoogleCloudRecommendationengineV1beta1CatalogOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1ListCatalogsResponseOut"])
    types["GoogleCloudRecommendationengineV1beta1InputConfigIn"] = t.struct(
        {
            "userEventInlineSource": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1UserEventInlineSourceIn"]
            ).optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1GcsSourceIn"]
            ).optional(),
            "bigQuerySource": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1BigQuerySourceIn"]
            ).optional(),
            "catalogInlineSource": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1CatalogInlineSourceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1InputConfigIn"])
    types["GoogleCloudRecommendationengineV1beta1InputConfigOut"] = t.struct(
        {
            "userEventInlineSource": t.proxy(
                renames[
                    "GoogleCloudRecommendationengineV1beta1UserEventInlineSourceOut"
                ]
            ).optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1GcsSourceOut"]
            ).optional(),
            "bigQuerySource": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1BigQuerySourceOut"]
            ).optional(),
            "catalogInlineSource": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1CatalogInlineSourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1InputConfigOut"])
    types["GoogleCloudRecommendationengineV1beta1CatalogItemIn"] = t.struct(
        {
            "title": t.string(),
            "id": t.string(),
            "itemGroupId": t.string().optional(),
            "productMetadata": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1ProductCatalogItemIn"]
            ).optional(),
            "tags": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "languageCode": t.string().optional(),
            "categoryHierarchies": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchyIn"
                    ]
                )
            ),
            "itemAttributes": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1FeatureMapIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1CatalogItemIn"])
    types["GoogleCloudRecommendationengineV1beta1CatalogItemOut"] = t.struct(
        {
            "title": t.string(),
            "id": t.string(),
            "itemGroupId": t.string().optional(),
            "productMetadata": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1ProductCatalogItemOut"]
            ).optional(),
            "tags": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "languageCode": t.string().optional(),
            "categoryHierarchies": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchyOut"
                    ]
                )
            ),
            "itemAttributes": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1FeatureMapOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1CatalogItemOut"])
    types["GoogleCloudRecommendationengineV1beta1GcsSourceIn"] = t.struct(
        {"inputUris": t.array(t.string()), "jsonSchema": t.string().optional()}
    ).named(renames["GoogleCloudRecommendationengineV1beta1GcsSourceIn"])
    types["GoogleCloudRecommendationengineV1beta1GcsSourceOut"] = t.struct(
        {
            "inputUris": t.array(t.string()),
            "jsonSchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1GcsSourceOut"])
    types["GoogleCloudRecommendationengineV1beta1ProductEventDetailIn"] = t.struct(
        {
            "searchQuery": t.string().optional(),
            "purchaseTransaction": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1PurchaseTransactionIn"]
            ).optional(),
            "listId": t.string(),
            "productDetails": t.array(
                t.proxy(
                    renames["GoogleCloudRecommendationengineV1beta1ProductDetailIn"]
                )
            ).optional(),
            "cartId": t.string().optional(),
            "pageCategories": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchyIn"
                    ]
                )
            ),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1ProductEventDetailIn"])
    types["GoogleCloudRecommendationengineV1beta1ProductEventDetailOut"] = t.struct(
        {
            "searchQuery": t.string().optional(),
            "purchaseTransaction": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1PurchaseTransactionOut"]
            ).optional(),
            "listId": t.string(),
            "productDetails": t.array(
                t.proxy(
                    renames["GoogleCloudRecommendationengineV1beta1ProductDetailOut"]
                )
            ).optional(),
            "cartId": t.string().optional(),
            "pageCategories": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchyOut"
                    ]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1ProductEventDetailOut"])
    types["GoogleCloudRecommendationengineV1beta1ProductDetailIn"] = t.struct(
        {
            "stockState": t.string().optional(),
            "id": t.string(),
            "itemAttributes": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1FeatureMapIn"]
            ).optional(),
            "displayPrice": t.number().optional(),
            "quantity": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "originalPrice": t.number().optional(),
            "availableQuantity": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1ProductDetailIn"])
    types["GoogleCloudRecommendationengineV1beta1ProductDetailOut"] = t.struct(
        {
            "stockState": t.string().optional(),
            "id": t.string(),
            "itemAttributes": t.proxy(
                renames["GoogleCloudRecommendationengineV1beta1FeatureMapOut"]
            ).optional(),
            "displayPrice": t.number().optional(),
            "quantity": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "originalPrice": t.number().optional(),
            "availableQuantity": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1ProductDetailOut"])
    types["GoogleCloudRecommendationengineV1beta1ProductCatalogItemIn"] = t.struct(
        {
            "images": t.array(
                t.proxy(renames["GoogleCloudRecommendationengineV1beta1ImageIn"])
            ).optional(),
            "costs": t.struct({"_": t.string().optional()}).optional(),
            "priceRange": t.proxy(
                renames[
                    "GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRangeIn"
                ]
            ).optional(),
            "canonicalProductUri": t.string().optional(),
            "availableQuantity": t.string().optional(),
            "currencyCode": t.string().optional(),
            "exactPrice": t.proxy(
                renames[
                    "GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPriceIn"
                ]
            ).optional(),
            "stockState": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1ProductCatalogItemIn"])
    types["GoogleCloudRecommendationengineV1beta1ProductCatalogItemOut"] = t.struct(
        {
            "images": t.array(
                t.proxy(renames["GoogleCloudRecommendationengineV1beta1ImageOut"])
            ).optional(),
            "costs": t.struct({"_": t.string().optional()}).optional(),
            "priceRange": t.proxy(
                renames[
                    "GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRangeOut"
                ]
            ).optional(),
            "canonicalProductUri": t.string().optional(),
            "availableQuantity": t.string().optional(),
            "currencyCode": t.string().optional(),
            "exactPrice": t.proxy(
                renames[
                    "GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPriceOut"
                ]
            ).optional(),
            "stockState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommendationengineV1beta1ProductCatalogItemOut"])
    types["GoogleCloudRecommendationengineV1beta1PurgeUserEventsMetadataIn"] = t.struct(
        {"createTime": t.string().optional(), "operationName": t.string().optional()}
    ).named(renames["GoogleCloudRecommendationengineV1beta1PurgeUserEventsMetadataIn"])
    types[
        "GoogleCloudRecommendationengineV1beta1PurgeUserEventsMetadataOut"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "operationName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecommendationengineV1beta1PurgeUserEventsMetadataOut"]
    )

    functions = {}
    functions["projectsLocationsCatalogsPatch"] = recommendationengine.get(
        "v1beta1/{parent}/catalogs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudRecommendationengineV1beta1ListCatalogsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsList"] = recommendationengine.get(
        "v1beta1/{parent}/catalogs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudRecommendationengineV1beta1ListCatalogsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsEventStoresPredictionApiKeyRegistrationsDelete"
    ] = recommendationengine.get(
        "v1beta1/{parent}/predictionApiKeyRegistrations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsEventStoresPredictionApiKeyRegistrationsCreate"
    ] = recommendationengine.get(
        "v1beta1/{parent}/predictionApiKeyRegistrations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsEventStoresPredictionApiKeyRegistrationsList"
    ] = recommendationengine.get(
        "v1beta1/{parent}/predictionApiKeyRegistrations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsEventStoresUserEventsList"
    ] = recommendationengine.post(
        "v1beta1/{parent}/userEvents:write",
        t.struct(
            {
                "parent": t.string(),
                "eventDetail": t.proxy(
                    renames["GoogleCloudRecommendationengineV1beta1EventDetailIn"]
                ).optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudRecommendationengineV1beta1UserInfoIn"]
                ),
                "productEventDetail": t.proxy(
                    renames[
                        "GoogleCloudRecommendationengineV1beta1ProductEventDetailIn"
                    ]
                ).optional(),
                "eventSource": t.string().optional(),
                "eventType": t.string(),
                "eventTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommendationengineV1beta1UserEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsEventStoresUserEventsImport"
    ] = recommendationengine.post(
        "v1beta1/{parent}/userEvents:write",
        t.struct(
            {
                "parent": t.string(),
                "eventDetail": t.proxy(
                    renames["GoogleCloudRecommendationengineV1beta1EventDetailIn"]
                ).optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudRecommendationengineV1beta1UserInfoIn"]
                ),
                "productEventDetail": t.proxy(
                    renames[
                        "GoogleCloudRecommendationengineV1beta1ProductEventDetailIn"
                    ]
                ).optional(),
                "eventSource": t.string().optional(),
                "eventType": t.string(),
                "eventTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommendationengineV1beta1UserEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsEventStoresUserEventsCollect"
    ] = recommendationengine.post(
        "v1beta1/{parent}/userEvents:write",
        t.struct(
            {
                "parent": t.string(),
                "eventDetail": t.proxy(
                    renames["GoogleCloudRecommendationengineV1beta1EventDetailIn"]
                ).optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudRecommendationengineV1beta1UserInfoIn"]
                ),
                "productEventDetail": t.proxy(
                    renames[
                        "GoogleCloudRecommendationengineV1beta1ProductEventDetailIn"
                    ]
                ).optional(),
                "eventSource": t.string().optional(),
                "eventType": t.string(),
                "eventTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommendationengineV1beta1UserEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsEventStoresUserEventsPurge"
    ] = recommendationengine.post(
        "v1beta1/{parent}/userEvents:write",
        t.struct(
            {
                "parent": t.string(),
                "eventDetail": t.proxy(
                    renames["GoogleCloudRecommendationengineV1beta1EventDetailIn"]
                ).optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudRecommendationengineV1beta1UserInfoIn"]
                ),
                "productEventDetail": t.proxy(
                    renames[
                        "GoogleCloudRecommendationengineV1beta1ProductEventDetailIn"
                    ]
                ).optional(),
                "eventSource": t.string().optional(),
                "eventType": t.string(),
                "eventTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommendationengineV1beta1UserEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsEventStoresUserEventsRejoin"
    ] = recommendationengine.post(
        "v1beta1/{parent}/userEvents:write",
        t.struct(
            {
                "parent": t.string(),
                "eventDetail": t.proxy(
                    renames["GoogleCloudRecommendationengineV1beta1EventDetailIn"]
                ).optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudRecommendationengineV1beta1UserInfoIn"]
                ),
                "productEventDetail": t.proxy(
                    renames[
                        "GoogleCloudRecommendationengineV1beta1ProductEventDetailIn"
                    ]
                ).optional(),
                "eventSource": t.string().optional(),
                "eventType": t.string(),
                "eventTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommendationengineV1beta1UserEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsEventStoresUserEventsWrite"
    ] = recommendationengine.post(
        "v1beta1/{parent}/userEvents:write",
        t.struct(
            {
                "parent": t.string(),
                "eventDetail": t.proxy(
                    renames["GoogleCloudRecommendationengineV1beta1EventDetailIn"]
                ).optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudRecommendationengineV1beta1UserInfoIn"]
                ),
                "productEventDetail": t.proxy(
                    renames[
                        "GoogleCloudRecommendationengineV1beta1ProductEventDetailIn"
                    ]
                ).optional(),
                "eventSource": t.string().optional(),
                "eventType": t.string(),
                "eventTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommendationengineV1beta1UserEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsEventStoresPlacementsPredict"
    ] = recommendationengine.post(
        "v1beta1/{name}:predict",
        t.struct(
            {
                "name": t.string(),
                "dryRun": t.boolean().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "userEvent": t.proxy(
                    renames["GoogleCloudRecommendationengineV1beta1UserEventIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommendationengineV1beta1PredictResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsEventStoresOperationsGet"
    ] = recommendationengine.get(
        "v1beta1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsEventStoresOperationsList"
    ] = recommendationengine.get(
        "v1beta1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsOperationsGet"] = recommendationengine.get(
        "v1beta1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsOperationsList"] = recommendationengine.get(
        "v1beta1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsCatalogItemsList"
    ] = recommendationengine.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsCatalogItemsImport"
    ] = recommendationengine.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsCatalogItemsCreate"
    ] = recommendationengine.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsCatalogItemsGet"] = recommendationengine.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsCatalogItemsPatch"
    ] = recommendationengine.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsCatalogItemsDelete"
    ] = recommendationengine.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="recommendationengine",
        renames=renames,
        types=types,
        functions=functions,
    )
