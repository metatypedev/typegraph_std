from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_discoveryengine() -> Import:
    discoveryengine = HTTPRuntime("https://discoveryengine.googleapis.com/")

    renames = {
        "ErrorResponse": "_discoveryengine_1_ErrorResponse",
        "GoogleApiHttpBodyIn": "_discoveryengine_2_GoogleApiHttpBodyIn",
        "GoogleApiHttpBodyOut": "_discoveryengine_3_GoogleApiHttpBodyOut",
        "GoogleCloudDiscoveryengineV1betaDocumentIn": "_discoveryengine_4_GoogleCloudDiscoveryengineV1betaDocumentIn",
        "GoogleCloudDiscoveryengineV1betaDocumentOut": "_discoveryengine_5_GoogleCloudDiscoveryengineV1betaDocumentOut",
        "GoogleCloudDiscoveryengineV1betaMediaInfoIn": "_discoveryengine_6_GoogleCloudDiscoveryengineV1betaMediaInfoIn",
        "GoogleCloudDiscoveryengineV1betaMediaInfoOut": "_discoveryengine_7_GoogleCloudDiscoveryengineV1betaMediaInfoOut",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceIn": "_discoveryengine_8_GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceIn",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceOut": "_discoveryengine_9_GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceOut",
        "GoogleCloudDiscoveryengineV1betaPageInfoIn": "_discoveryengine_10_GoogleCloudDiscoveryengineV1betaPageInfoIn",
        "GoogleCloudDiscoveryengineV1betaPageInfoOut": "_discoveryengine_11_GoogleCloudDiscoveryengineV1betaPageInfoOut",
        "GoogleTypeDateIn": "_discoveryengine_12_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_discoveryengine_13_GoogleTypeDateOut",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataIn": "_discoveryengine_14_GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataIn",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataOut": "_discoveryengine_15_GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataOut",
        "GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataIn": "_discoveryengine_16_GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataIn",
        "GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataOut": "_discoveryengine_17_GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataOut",
        "GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseIn": "_discoveryengine_18_GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseOut": "_discoveryengine_19_GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1betaDocumentInfoIn": "_discoveryengine_20_GoogleCloudDiscoveryengineV1betaDocumentInfoIn",
        "GoogleCloudDiscoveryengineV1betaDocumentInfoOut": "_discoveryengine_21_GoogleCloudDiscoveryengineV1betaDocumentInfoOut",
        "GoogleCloudDiscoveryengineV1betaCustomAttributeIn": "_discoveryengine_22_GoogleCloudDiscoveryengineV1betaCustomAttributeIn",
        "GoogleCloudDiscoveryengineV1betaCustomAttributeOut": "_discoveryengine_23_GoogleCloudDiscoveryengineV1betaCustomAttributeOut",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestIn": "_discoveryengine_24_GoogleCloudDiscoveryengineV1betaImportDocumentsRequestIn",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestOut": "_discoveryengine_25_GoogleCloudDiscoveryengineV1betaImportDocumentsRequestOut",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestIn": "_discoveryengine_26_GoogleCloudDiscoveryengineV1betaImportUserEventsRequestIn",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestOut": "_discoveryengine_27_GoogleCloudDiscoveryengineV1betaImportUserEventsRequestOut",
        "GoogleCloudDiscoveryengineV1betaUserEventIn": "_discoveryengine_28_GoogleCloudDiscoveryengineV1betaUserEventIn",
        "GoogleCloudDiscoveryengineV1betaUserEventOut": "_discoveryengine_29_GoogleCloudDiscoveryengineV1betaUserEventOut",
        "GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataIn": "_discoveryengine_30_GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataIn",
        "GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataOut": "_discoveryengine_31_GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataOut",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataIn": "_discoveryengine_32_GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataIn",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataOut": "_discoveryengine_33_GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataOut",
        "GoogleCloudDiscoveryengineLoggingServiceContextIn": "_discoveryengine_34_GoogleCloudDiscoveryengineLoggingServiceContextIn",
        "GoogleCloudDiscoveryengineLoggingServiceContextOut": "_discoveryengine_35_GoogleCloudDiscoveryengineLoggingServiceContextOut",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn": "_discoveryengine_36_GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceOut": "_discoveryengine_37_GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceOut",
        "GoogleCloudDiscoveryengineLoggingHttpRequestContextIn": "_discoveryengine_38_GoogleCloudDiscoveryengineLoggingHttpRequestContextIn",
        "GoogleCloudDiscoveryengineLoggingHttpRequestContextOut": "_discoveryengine_39_GoogleCloudDiscoveryengineLoggingHttpRequestContextOut",
        "GoogleCloudDiscoveryengineV1betaSearchInfoIn": "_discoveryengine_40_GoogleCloudDiscoveryengineV1betaSearchInfoIn",
        "GoogleCloudDiscoveryengineV1betaSearchInfoOut": "_discoveryengine_41_GoogleCloudDiscoveryengineV1betaSearchInfoOut",
        "GoogleCloudDiscoveryengineV1betaGcsSourceIn": "_discoveryengine_42_GoogleCloudDiscoveryengineV1betaGcsSourceIn",
        "GoogleCloudDiscoveryengineV1betaGcsSourceOut": "_discoveryengine_43_GoogleCloudDiscoveryengineV1betaGcsSourceOut",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsResponseIn": "_discoveryengine_44_GoogleCloudDiscoveryengineV1betaImportDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsResponseOut": "_discoveryengine_45_GoogleCloudDiscoveryengineV1betaImportDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1betaPanelInfoIn": "_discoveryengine_46_GoogleCloudDiscoveryengineV1betaPanelInfoIn",
        "GoogleCloudDiscoveryengineV1betaPanelInfoOut": "_discoveryengine_47_GoogleCloudDiscoveryengineV1betaPanelInfoOut",
        "GoogleCloudDiscoveryengineLoggingSourceLocationIn": "_discoveryengine_48_GoogleCloudDiscoveryengineLoggingSourceLocationIn",
        "GoogleCloudDiscoveryengineLoggingSourceLocationOut": "_discoveryengine_49_GoogleCloudDiscoveryengineLoggingSourceLocationOut",
        "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultIn": "_discoveryengine_50_GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultIn",
        "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultOut": "_discoveryengine_51_GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultOut",
        "GoogleCloudDiscoveryengineV1betaSchemaIn": "_discoveryengine_52_GoogleCloudDiscoveryengineV1betaSchemaIn",
        "GoogleCloudDiscoveryengineV1betaSchemaOut": "_discoveryengine_53_GoogleCloudDiscoveryengineV1betaSchemaOut",
        "GoogleCloudDiscoveryengineLoggingErrorLogIn": "_discoveryengine_54_GoogleCloudDiscoveryengineLoggingErrorLogIn",
        "GoogleCloudDiscoveryengineLoggingErrorLogOut": "_discoveryengine_55_GoogleCloudDiscoveryengineLoggingErrorLogOut",
        "GoogleCloudDiscoveryengineV1betaListDocumentsResponseIn": "_discoveryengine_56_GoogleCloudDiscoveryengineV1betaListDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut": "_discoveryengine_57_GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1betaImportErrorConfigIn": "_discoveryengine_58_GoogleCloudDiscoveryengineV1betaImportErrorConfigIn",
        "GoogleCloudDiscoveryengineV1betaImportErrorConfigOut": "_discoveryengine_59_GoogleCloudDiscoveryengineV1betaImportErrorConfigOut",
        "GoogleCloudDiscoveryengineLoggingErrorContextIn": "_discoveryengine_60_GoogleCloudDiscoveryengineLoggingErrorContextIn",
        "GoogleCloudDiscoveryengineLoggingErrorContextOut": "_discoveryengine_61_GoogleCloudDiscoveryengineLoggingErrorContextOut",
        "GoogleCloudDiscoveryengineV1betaUserInfoIn": "_discoveryengine_62_GoogleCloudDiscoveryengineV1betaUserInfoIn",
        "GoogleCloudDiscoveryengineV1betaUserInfoOut": "_discoveryengine_63_GoogleCloudDiscoveryengineV1betaUserInfoOut",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseIn": "_discoveryengine_64_GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseOut": "_discoveryengine_65_GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseOut",
        "GoogleCloudDiscoveryengineLoggingImportErrorContextIn": "_discoveryengine_66_GoogleCloudDiscoveryengineLoggingImportErrorContextIn",
        "GoogleCloudDiscoveryengineLoggingImportErrorContextOut": "_discoveryengine_67_GoogleCloudDiscoveryengineLoggingImportErrorContextOut",
        "GoogleCloudDiscoveryengineV1betaCompletionInfoIn": "_discoveryengine_68_GoogleCloudDiscoveryengineV1betaCompletionInfoIn",
        "GoogleCloudDiscoveryengineV1betaCompletionInfoOut": "_discoveryengine_69_GoogleCloudDiscoveryengineV1betaCompletionInfoOut",
        "GoogleCloudDiscoveryengineV1betaRecommendRequestIn": "_discoveryengine_70_GoogleCloudDiscoveryengineV1betaRecommendRequestIn",
        "GoogleCloudDiscoveryengineV1betaRecommendRequestOut": "_discoveryengine_71_GoogleCloudDiscoveryengineV1betaRecommendRequestOut",
        "GoogleCloudDiscoveryengineV1alphaSchemaIn": "_discoveryengine_72_GoogleCloudDiscoveryengineV1alphaSchemaIn",
        "GoogleCloudDiscoveryengineV1alphaSchemaOut": "_discoveryengine_73_GoogleCloudDiscoveryengineV1alphaSchemaOut",
        "GoogleCloudDiscoveryengineV1betaBigQuerySourceIn": "_discoveryengine_74_GoogleCloudDiscoveryengineV1betaBigQuerySourceIn",
        "GoogleCloudDiscoveryengineV1betaBigQuerySourceOut": "_discoveryengine_75_GoogleCloudDiscoveryengineV1betaBigQuerySourceOut",
        "GoogleProtobufEmptyIn": "_discoveryengine_76_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_discoveryengine_77_GoogleProtobufEmptyOut",
        "GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseIn": "_discoveryengine_78_GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseIn",
        "GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseOut": "_discoveryengine_79_GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseOut",
        "GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataIn": "_discoveryengine_80_GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataIn",
        "GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataOut": "_discoveryengine_81_GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataOut",
        "GoogleLongrunningListOperationsResponseIn": "_discoveryengine_82_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_discoveryengine_83_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn": "_discoveryengine_84_GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn",
        "GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut": "_discoveryengine_85_GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut",
        "GoogleRpcStatusIn": "_discoveryengine_86_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_discoveryengine_87_GoogleRpcStatusOut",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsResponseIn": "_discoveryengine_88_GoogleCloudDiscoveryengineV1betaImportUserEventsResponseIn",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsResponseOut": "_discoveryengine_89_GoogleCloudDiscoveryengineV1betaImportUserEventsResponseOut",
        "GoogleCloudDiscoveryengineV1betaTransactionInfoIn": "_discoveryengine_90_GoogleCloudDiscoveryengineV1betaTransactionInfoIn",
        "GoogleCloudDiscoveryengineV1betaTransactionInfoOut": "_discoveryengine_91_GoogleCloudDiscoveryengineV1betaTransactionInfoOut",
        "GoogleLongrunningOperationIn": "_discoveryengine_92_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_discoveryengine_93_GoogleLongrunningOperationOut",
        "GoogleCloudDiscoveryengineV1betaRecommendResponseIn": "_discoveryengine_94_GoogleCloudDiscoveryengineV1betaRecommendResponseIn",
        "GoogleCloudDiscoveryengineV1betaRecommendResponseOut": "_discoveryengine_95_GoogleCloudDiscoveryengineV1betaRecommendResponseOut",
        "GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseIn": "_discoveryengine_96_GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseOut": "_discoveryengine_97_GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataIn": "_discoveryengine_98_GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataIn",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataOut": "_discoveryengine_99_GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataOut",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestIn": "_discoveryengine_100_GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestIn",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestOut": "_discoveryengine_101_GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleApiHttpBodyIn"] = t.struct(
        {
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "data": t.string().optional(),
            "contentType": t.string().optional(),
        }
    ).named(renames["GoogleApiHttpBodyIn"])
    types["GoogleApiHttpBodyOut"] = t.struct(
        {
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "data": t.string().optional(),
            "contentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiHttpBodyOut"])
    types["GoogleCloudDiscoveryengineV1betaDocumentIn"] = t.struct(
        {
            "jsonData": t.string().optional(),
            "id": t.string().optional(),
            "schemaId": t.string().optional(),
            "name": t.string().optional(),
            "structData": t.struct({"_": t.string().optional()}).optional(),
            "parentDocumentId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaDocumentIn"])
    types["GoogleCloudDiscoveryengineV1betaDocumentOut"] = t.struct(
        {
            "jsonData": t.string().optional(),
            "id": t.string().optional(),
            "schemaId": t.string().optional(),
            "name": t.string().optional(),
            "structData": t.struct({"_": t.string().optional()}).optional(),
            "parentDocumentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"])
    types["GoogleCloudDiscoveryengineV1betaMediaInfoIn"] = t.struct(
        {
            "mediaProgressDuration": t.string().optional(),
            "mediaProgressPercentage": t.number().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaMediaInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaMediaInfoOut"] = t.struct(
        {
            "mediaProgressDuration": t.string().optional(),
            "mediaProgressPercentage": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaMediaInfoOut"])
    types[
        "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceIn"
    ] = t.struct(
        {
            "documents": t.array(
                t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentIn"])
            )
        }
    ).named(
        renames["GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceIn"]
    )
    types[
        "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceOut"
    ] = t.struct(
        {
            "documents": t.array(
                t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceOut"]
    )
    types["GoogleCloudDiscoveryengineV1betaPageInfoIn"] = t.struct(
        {
            "referrerUri": t.string().optional(),
            "uri": t.string().optional(),
            "pageCategory": t.string().optional(),
            "pageviewId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPageInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaPageInfoOut"] = t.struct(
        {
            "referrerUri": t.string().optional(),
            "uri": t.string().optional(),
            "pageCategory": t.string().optional(),
            "pageviewId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPageInfoOut"])
    types["GoogleTypeDateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])
    types["GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataIn"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataOut"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataOut"])
    types["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "successCount": t.string().optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "successCount": t.string().optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataOut"])
    types["GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseIn"] = t.struct(
        {
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseIn"])
    types["GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseOut"] = t.struct(
        {
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseOut"])
    types["GoogleCloudDiscoveryengineV1betaDocumentInfoIn"] = t.struct(
        {
            "quantity": t.integer().optional(),
            "uri": t.string(),
            "promotionIds": t.array(t.string()).optional(),
            "id": t.string(),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaDocumentInfoOut"] = t.struct(
        {
            "quantity": t.integer().optional(),
            "uri": t.string(),
            "promotionIds": t.array(t.string()).optional(),
            "id": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoOut"])
    types["GoogleCloudDiscoveryengineV1betaCustomAttributeIn"] = t.struct(
        {
            "text": t.array(t.string()).optional(),
            "numbers": t.array(t.number()).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaCustomAttributeIn"])
    types["GoogleCloudDiscoveryengineV1betaCustomAttributeOut"] = t.struct(
        {
            "text": t.array(t.string()).optional(),
            "numbers": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaCustomAttributeOut"])
    types["GoogleCloudDiscoveryengineV1betaImportDocumentsRequestIn"] = t.struct(
        {
            "bigquerySource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
            ).optional(),
            "reconciliationMode": t.string().optional(),
            "inlineSource": t.proxy(
                renames[
                    "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceIn"
                ]
            ).optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
            ).optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportDocumentsRequestIn"])
    types["GoogleCloudDiscoveryengineV1betaImportDocumentsRequestOut"] = t.struct(
        {
            "bigquerySource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceOut"]
            ).optional(),
            "reconciliationMode": t.string().optional(),
            "inlineSource": t.proxy(
                renames[
                    "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceOut"
                ]
            ).optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"]
            ).optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaGcsSourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportDocumentsRequestOut"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsRequestIn"] = t.struct(
        {
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
            ).optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
            ),
            "inlineSource": t.proxy(
                renames[
                    "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                ]
            ),
            "bigquerySource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
            ),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsRequestIn"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsRequestOut"] = t.struct(
        {
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"]
            ).optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaGcsSourceOut"]
            ),
            "inlineSource": t.proxy(
                renames[
                    "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceOut"
                ]
            ),
            "bigquerySource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsRequestOut"])
    types["GoogleCloudDiscoveryengineV1betaUserEventIn"] = t.struct(
        {
            "eventType": t.string(),
            "attributionToken": t.string().optional(),
            "filter": t.string().optional(),
            "searchInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaSearchInfoIn"]
            ).optional(),
            "completionInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaCompletionInfoIn"]
            ).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "promotionIds": t.array(t.string()).optional(),
            "sessionId": t.string().optional(),
            "directUserRequest": t.boolean().optional(),
            "mediaInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaMediaInfoIn"]
            ).optional(),
            "transactionInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaTransactionInfoIn"]
            ).optional(),
            "panel": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaPanelInfoIn"]
            ).optional(),
            "documents": t.array(
                t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoIn"])
            ).optional(),
            "userInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaUserInfoIn"]
            ).optional(),
            "userPseudoId": t.string(),
            "eventTime": t.string().optional(),
            "tagIds": t.array(t.string()).optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaPageInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaUserEventIn"])
    types["GoogleCloudDiscoveryengineV1betaUserEventOut"] = t.struct(
        {
            "eventType": t.string(),
            "attributionToken": t.string().optional(),
            "filter": t.string().optional(),
            "searchInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaSearchInfoOut"]
            ).optional(),
            "completionInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaCompletionInfoOut"]
            ).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "promotionIds": t.array(t.string()).optional(),
            "sessionId": t.string().optional(),
            "directUserRequest": t.boolean().optional(),
            "mediaInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaMediaInfoOut"]
            ).optional(),
            "transactionInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaTransactionInfoOut"]
            ).optional(),
            "panel": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaPanelInfoOut"]
            ).optional(),
            "documents": t.array(
                t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoOut"])
            ).optional(),
            "userInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaUserInfoOut"]
            ).optional(),
            "userPseudoId": t.string(),
            "eventTime": t.string().optional(),
            "tagIds": t.array(t.string()).optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaPageInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaUserEventOut"])
    types["GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataIn"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "successCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataOut"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "successCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataOut"])
    types["GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataIn"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "successCount": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataOut"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "successCount": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataOut"])
    types["GoogleCloudDiscoveryengineLoggingServiceContextIn"] = t.struct(
        {"service": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineLoggingServiceContextIn"])
    types["GoogleCloudDiscoveryengineLoggingServiceContextOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingServiceContextOut"])
    types[
        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
    ] = t.struct(
        {
            "userEvents": t.array(
                t.proxy(renames["GoogleCloudDiscoveryengineV1betaUserEventIn"])
            )
        }
    ).named(
        renames["GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"]
    )
    types[
        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceOut"
    ] = t.struct(
        {
            "userEvents": t.array(
                t.proxy(renames["GoogleCloudDiscoveryengineV1betaUserEventOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceOut"
        ]
    )
    types["GoogleCloudDiscoveryengineLoggingHttpRequestContextIn"] = t.struct(
        {"responseStatusCode": t.integer().optional()}
    ).named(renames["GoogleCloudDiscoveryengineLoggingHttpRequestContextIn"])
    types["GoogleCloudDiscoveryengineLoggingHttpRequestContextOut"] = t.struct(
        {
            "responseStatusCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingHttpRequestContextOut"])
    types["GoogleCloudDiscoveryengineV1betaSearchInfoIn"] = t.struct(
        {
            "offset": t.integer().optional(),
            "searchQuery": t.string().optional(),
            "orderBy": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaSearchInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaSearchInfoOut"] = t.struct(
        {
            "offset": t.integer().optional(),
            "searchQuery": t.string().optional(),
            "orderBy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaSearchInfoOut"])
    types["GoogleCloudDiscoveryengineV1betaGcsSourceIn"] = t.struct(
        {"dataSchema": t.string().optional(), "inputUris": t.array(t.string())}
    ).named(renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"])
    types["GoogleCloudDiscoveryengineV1betaGcsSourceOut"] = t.struct(
        {
            "dataSchema": t.string().optional(),
            "inputUris": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaGcsSourceOut"])
    types["GoogleCloudDiscoveryengineV1betaImportDocumentsResponseIn"] = t.struct(
        {
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportDocumentsResponseIn"])
    types["GoogleCloudDiscoveryengineV1betaImportDocumentsResponseOut"] = t.struct(
        {
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportDocumentsResponseOut"])
    types["GoogleCloudDiscoveryengineV1betaPanelInfoIn"] = t.struct(
        {
            "panelId": t.string(),
            "totalPanels": t.integer().optional(),
            "displayName": t.string().optional(),
            "panelPosition": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPanelInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaPanelInfoOut"] = t.struct(
        {
            "panelId": t.string(),
            "totalPanels": t.integer().optional(),
            "displayName": t.string().optional(),
            "panelPosition": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPanelInfoOut"])
    types["GoogleCloudDiscoveryengineLoggingSourceLocationIn"] = t.struct(
        {"functionName": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineLoggingSourceLocationIn"])
    types["GoogleCloudDiscoveryengineLoggingSourceLocationOut"] = t.struct(
        {
            "functionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingSourceLocationOut"])
    types[
        "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultIn"
    ] = t.struct(
        {
            "document": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaDocumentIn"]
            ).optional(),
            "id": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultIn"
        ]
    )
    types[
        "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultOut"
    ] = t.struct(
        {
            "document": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]
            ).optional(),
            "id": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultOut"
        ]
    )
    types["GoogleCloudDiscoveryengineV1betaSchemaIn"] = t.struct(
        {
            "structSchema": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "jsonSchema": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaSchemaIn"])
    types["GoogleCloudDiscoveryengineV1betaSchemaOut"] = t.struct(
        {
            "structSchema": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "jsonSchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaSchemaOut"])
    types["GoogleCloudDiscoveryengineLoggingErrorLogIn"] = t.struct(
        {
            "responsePayload": t.struct({"_": t.string().optional()}).optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "importPayload": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingImportErrorContextIn"]
            ).optional(),
            "requestPayload": t.struct({"_": t.string().optional()}).optional(),
            "message": t.string().optional(),
            "serviceContext": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingServiceContextIn"]
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingErrorContextIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingErrorLogIn"])
    types["GoogleCloudDiscoveryengineLoggingErrorLogOut"] = t.struct(
        {
            "responsePayload": t.struct({"_": t.string().optional()}).optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "importPayload": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingImportErrorContextOut"]
            ).optional(),
            "requestPayload": t.struct({"_": t.string().optional()}).optional(),
            "message": t.string().optional(),
            "serviceContext": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingServiceContextOut"]
            ).optional(),
            "context": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingErrorContextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingErrorLogOut"])
    types["GoogleCloudDiscoveryengineV1betaListDocumentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "documents": t.array(
                t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaListDocumentsResponseIn"])
    types["GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "documents": t.array(
                t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut"])
    types["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"])
    types["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"])
    types["GoogleCloudDiscoveryengineLoggingErrorContextIn"] = t.struct(
        {
            "reportLocation": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingSourceLocationIn"]
            ).optional(),
            "httpRequest": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingHttpRequestContextIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingErrorContextIn"])
    types["GoogleCloudDiscoveryengineLoggingErrorContextOut"] = t.struct(
        {
            "reportLocation": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingSourceLocationOut"]
            ).optional(),
            "httpRequest": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingHttpRequestContextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingErrorContextOut"])
    types["GoogleCloudDiscoveryengineV1betaUserInfoIn"] = t.struct(
        {"userId": t.string().optional(), "userAgent": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineV1betaUserInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaUserInfoOut"] = t.struct(
        {
            "userId": t.string().optional(),
            "userAgent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaUserInfoOut"])
    types["GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseIn"] = t.struct(
        {
            "purgeCount": t.string().optional(),
            "purgeSample": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseIn"])
    types["GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseOut"] = t.struct(
        {
            "purgeCount": t.string().optional(),
            "purgeSample": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseOut"])
    types["GoogleCloudDiscoveryengineLoggingImportErrorContextIn"] = t.struct(
        {
            "lineNumber": t.string().optional(),
            "gcsPath": t.string().optional(),
            "operation": t.string().optional(),
            "userEvent": t.string().optional(),
            "document": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingImportErrorContextIn"])
    types["GoogleCloudDiscoveryengineLoggingImportErrorContextOut"] = t.struct(
        {
            "lineNumber": t.string().optional(),
            "gcsPath": t.string().optional(),
            "operation": t.string().optional(),
            "userEvent": t.string().optional(),
            "document": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingImportErrorContextOut"])
    types["GoogleCloudDiscoveryengineV1betaCompletionInfoIn"] = t.struct(
        {
            "selectedSuggestion": t.string().optional(),
            "selectedPosition": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaCompletionInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaCompletionInfoOut"] = t.struct(
        {
            "selectedSuggestion": t.string().optional(),
            "selectedPosition": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaCompletionInfoOut"])
    types["GoogleCloudDiscoveryengineV1betaRecommendRequestIn"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "pageSize": t.integer().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "userEvent": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaUserEventIn"]
            ),
            "filter": t.string().optional(),
            "validateOnly": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaRecommendRequestIn"])
    types["GoogleCloudDiscoveryengineV1betaRecommendRequestOut"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "pageSize": t.integer().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "userEvent": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaUserEventOut"]
            ),
            "filter": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaRecommendRequestOut"])
    types["GoogleCloudDiscoveryengineV1alphaSchemaIn"] = t.struct(
        {
            "structSchema": t.struct({"_": t.string().optional()}).optional(),
            "jsonSchema": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaSchemaIn"])
    types["GoogleCloudDiscoveryengineV1alphaSchemaOut"] = t.struct(
        {
            "structSchema": t.struct({"_": t.string().optional()}).optional(),
            "jsonSchema": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaSchemaOut"])
    types["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"] = t.struct(
        {
            "datasetId": t.string(),
            "tableId": t.string(),
            "projectId": t.string().optional(),
            "partitionDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "dataSchema": t.string().optional(),
            "gcsStagingDir": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"])
    types["GoogleCloudDiscoveryengineV1betaBigQuerySourceOut"] = t.struct(
        {
            "datasetId": t.string(),
            "tableId": t.string(),
            "projectId": t.string().optional(),
            "partitionDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "dataSchema": t.string().optional(),
            "gcsStagingDir": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseIn"] = t.struct(
        {
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn"]
            ).optional(),
            "unjoinedEventsCount": t.string().optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "joinedEventsCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseIn"])
    types["GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseOut"] = t.struct(
        {
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut"]
            ).optional(),
            "unjoinedEventsCount": t.string().optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "joinedEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseOut"])
    types["GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataOut"])
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
    types["GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn"])
    types["GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsResponseIn"] = t.struct(
        {
            "joinedEventsCount": t.string().optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "unjoinedEventsCount": t.string().optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsResponseIn"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsResponseOut"] = t.struct(
        {
            "joinedEventsCount": t.string().optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "unjoinedEventsCount": t.string().optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsResponseOut"])
    types["GoogleCloudDiscoveryengineV1betaTransactionInfoIn"] = t.struct(
        {
            "cost": t.number().optional(),
            "currency": t.string(),
            "discountValue": t.number().optional(),
            "transactionId": t.string().optional(),
            "value": t.number(),
            "tax": t.number().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaTransactionInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaTransactionInfoOut"] = t.struct(
        {
            "cost": t.number().optional(),
            "currency": t.string(),
            "discountValue": t.number().optional(),
            "transactionId": t.string().optional(),
            "value": t.number(),
            "tax": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaTransactionInfoOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleCloudDiscoveryengineV1betaRecommendResponseIn"] = t.struct(
        {
            "results": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultIn"
                    ]
                )
            ).optional(),
            "validateOnly": t.boolean().optional(),
            "attributionToken": t.string().optional(),
            "missingIds": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaRecommendResponseIn"])
    types["GoogleCloudDiscoveryengineV1betaRecommendResponseOut"] = t.struct(
        {
            "results": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultOut"
                    ]
                )
            ).optional(),
            "validateOnly": t.boolean().optional(),
            "attributionToken": t.string().optional(),
            "missingIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaRecommendResponseOut"])
    types["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseIn"] = t.struct(
        {
            "purgeCount": t.string().optional(),
            "purgeSample": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseIn"])
    types["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseOut"] = t.struct(
        {
            "purgeCount": t.string().optional(),
            "purgeSample": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseOut"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataIn"] = t.struct(
        {
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataOut"] = t.struct(
        {
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataOut"])
    types["GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestIn"] = t.struct(
        {"filter": t.string(), "force": t.boolean().optional()}
    ).named(renames["GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestIn"])
    types["GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestOut"] = t.struct(
        {
            "filter": t.string(),
            "force": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestOut"])

    functions = {}
    functions["projectsLocationsOperationsList"] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresOperationsGet"] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresOperationsList"] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataStoresServingConfigsRecommend"
    ] = discoveryengine.post(
        "v1beta/{servingConfig}:recommend",
        t.struct(
            {
                "servingConfig": t.string(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "pageSize": t.integer().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "userEvent": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaUserEventIn"]
                ),
                "filter": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaRecommendResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresModelsOperationsList"] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresModelsOperationsGet"] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresUserEventsImport"] = discoveryengine.get(
        "v1beta/{parent}/userEvents:collect",
        t.struct(
            {
                "userEvent": t.string(),
                "uri": t.string().optional(),
                "ets": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresUserEventsWrite"] = discoveryengine.get(
        "v1beta/{parent}/userEvents:collect",
        t.struct(
            {
                "userEvent": t.string(),
                "uri": t.string().optional(),
                "ets": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresUserEventsCollect"] = discoveryengine.get(
        "v1beta/{parent}/userEvents:collect",
        t.struct(
            {
                "userEvent": t.string(),
                "uri": t.string().optional(),
                "ets": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataStoresBranchesDocumentsImport"
    ] = discoveryengine.get(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresBranchesDocumentsGet"] = discoveryengine.get(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataStoresBranchesDocumentsCreate"
    ] = discoveryengine.get(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataStoresBranchesDocumentsDelete"
    ] = discoveryengine.get(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataStoresBranchesDocumentsPurge"
    ] = discoveryengine.get(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataStoresBranchesDocumentsPatch"
    ] = discoveryengine.get(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresBranchesDocumentsList"] = discoveryengine.get(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresBranchesOperationsGet"] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataStoresBranchesOperationsList"
    ] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCollectionsOperationsGet"] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCollectionsOperationsList"] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresModelsOperationsList"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresModelsOperationsGet"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresOperationsList"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresOperationsGet"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresUserEventsCollect"
    ] = discoveryengine.post(
        "v1beta/{parent}/userEvents:import",
        t.struct(
            {
                "parent": t.string(),
                "errorConfig": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
                ).optional(),
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ),
                "inlineSource": t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                    ]
                ),
                "bigquerySource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresUserEventsWrite"
    ] = discoveryengine.post(
        "v1beta/{parent}/userEvents:import",
        t.struct(
            {
                "parent": t.string(),
                "errorConfig": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
                ).optional(),
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ),
                "inlineSource": t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                    ]
                ),
                "bigquerySource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresUserEventsImport"
    ] = discoveryengine.post(
        "v1beta/{parent}/userEvents:import",
        t.struct(
            {
                "parent": t.string(),
                "errorConfig": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
                ).optional(),
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ),
                "inlineSource": t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                    ]
                ),
                "bigquerySource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresServingConfigsRecommend"
    ] = discoveryengine.post(
        "v1beta/{servingConfig}:recommend",
        t.struct(
            {
                "servingConfig": t.string(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "pageSize": t.integer().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "userEvent": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaUserEventIn"]
                ),
                "filter": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaRecommendResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsDelete"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsImport"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsCreate"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsPatch"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsList"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsPurge"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsGet"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesOperationsGet"
    ] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesOperationsList"
    ] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCollectionsEnginesOperationsGet"] = discoveryengine.get(
        "v1beta/{name}/operations",
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
        "projectsLocationsCollectionsEnginesOperationsList"
    ] = discoveryengine.get(
        "v1beta/{name}/operations",
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
    functions["projectsOperationsList"] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsGet"] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="discoveryengine",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
