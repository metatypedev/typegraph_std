from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_discoveryengine() -> Import:
    discoveryengine = HTTPRuntime("https://discoveryengine.googleapis.com/")

    renames = {
        "ErrorResponse": "_discoveryengine_1_ErrorResponse",
        "GoogleCloudDiscoveryengineV1betaBigQuerySourceIn": "_discoveryengine_2_GoogleCloudDiscoveryengineV1betaBigQuerySourceIn",
        "GoogleCloudDiscoveryengineV1betaBigQuerySourceOut": "_discoveryengine_3_GoogleCloudDiscoveryengineV1betaBigQuerySourceOut",
        "GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataIn": "_discoveryengine_4_GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataIn",
        "GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataOut": "_discoveryengine_5_GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataOut",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataIn": "_discoveryengine_6_GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataIn",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataOut": "_discoveryengine_7_GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataOut",
        "GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataIn": "_discoveryengine_8_GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataIn",
        "GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataOut": "_discoveryengine_9_GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataOut",
        "GoogleCloudDiscoveryengineV1betaRecommendResponseIn": "_discoveryengine_10_GoogleCloudDiscoveryengineV1betaRecommendResponseIn",
        "GoogleCloudDiscoveryengineV1betaRecommendResponseOut": "_discoveryengine_11_GoogleCloudDiscoveryengineV1betaRecommendResponseOut",
        "GoogleCloudDiscoveryengineLoggingErrorLogIn": "_discoveryengine_12_GoogleCloudDiscoveryengineLoggingErrorLogIn",
        "GoogleCloudDiscoveryengineLoggingErrorLogOut": "_discoveryengine_13_GoogleCloudDiscoveryengineLoggingErrorLogOut",
        "GoogleLongrunningListOperationsResponseIn": "_discoveryengine_14_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_discoveryengine_15_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestIn": "_discoveryengine_16_GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestIn",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestOut": "_discoveryengine_17_GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestOut",
        "GoogleCloudDiscoveryengineV1betaTransactionInfoIn": "_discoveryengine_18_GoogleCloudDiscoveryengineV1betaTransactionInfoIn",
        "GoogleCloudDiscoveryengineV1betaTransactionInfoOut": "_discoveryengine_19_GoogleCloudDiscoveryengineV1betaTransactionInfoOut",
        "GoogleCloudDiscoveryengineV1betaCompletionInfoIn": "_discoveryengine_20_GoogleCloudDiscoveryengineV1betaCompletionInfoIn",
        "GoogleCloudDiscoveryengineV1betaCompletionInfoOut": "_discoveryengine_21_GoogleCloudDiscoveryengineV1betaCompletionInfoOut",
        "GoogleCloudDiscoveryengineV1betaGcsSourceIn": "_discoveryengine_22_GoogleCloudDiscoveryengineV1betaGcsSourceIn",
        "GoogleCloudDiscoveryengineV1betaGcsSourceOut": "_discoveryengine_23_GoogleCloudDiscoveryengineV1betaGcsSourceOut",
        "GoogleCloudDiscoveryengineV1betaImportErrorConfigIn": "_discoveryengine_24_GoogleCloudDiscoveryengineV1betaImportErrorConfigIn",
        "GoogleCloudDiscoveryengineV1betaImportErrorConfigOut": "_discoveryengine_25_GoogleCloudDiscoveryengineV1betaImportErrorConfigOut",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsResponseIn": "_discoveryengine_26_GoogleCloudDiscoveryengineV1betaImportUserEventsResponseIn",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsResponseOut": "_discoveryengine_27_GoogleCloudDiscoveryengineV1betaImportUserEventsResponseOut",
        "GoogleCloudDiscoveryengineLoggingImportErrorContextIn": "_discoveryengine_28_GoogleCloudDiscoveryengineLoggingImportErrorContextIn",
        "GoogleCloudDiscoveryengineLoggingImportErrorContextOut": "_discoveryengine_29_GoogleCloudDiscoveryengineLoggingImportErrorContextOut",
        "GoogleApiHttpBodyIn": "_discoveryengine_30_GoogleApiHttpBodyIn",
        "GoogleApiHttpBodyOut": "_discoveryengine_31_GoogleApiHttpBodyOut",
        "GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseIn": "_discoveryengine_32_GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseOut": "_discoveryengine_33_GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn": "_discoveryengine_34_GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceOut": "_discoveryengine_35_GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceOut",
        "GoogleCloudDiscoveryengineV1betaListDocumentsResponseIn": "_discoveryengine_36_GoogleCloudDiscoveryengineV1betaListDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut": "_discoveryengine_37_GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceIn": "_discoveryengine_38_GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceIn",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceOut": "_discoveryengine_39_GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceOut",
        "GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn": "_discoveryengine_40_GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn",
        "GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut": "_discoveryengine_41_GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestIn": "_discoveryengine_42_GoogleCloudDiscoveryengineV1betaImportDocumentsRequestIn",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestOut": "_discoveryengine_43_GoogleCloudDiscoveryengineV1betaImportDocumentsRequestOut",
        "GoogleLongrunningOperationIn": "_discoveryengine_44_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_discoveryengine_45_GoogleLongrunningOperationOut",
        "GoogleCloudDiscoveryengineV1betaDocumentInfoIn": "_discoveryengine_46_GoogleCloudDiscoveryengineV1betaDocumentInfoIn",
        "GoogleCloudDiscoveryengineV1betaDocumentInfoOut": "_discoveryengine_47_GoogleCloudDiscoveryengineV1betaDocumentInfoOut",
        "GoogleCloudDiscoveryengineV1betaPanelInfoIn": "_discoveryengine_48_GoogleCloudDiscoveryengineV1betaPanelInfoIn",
        "GoogleCloudDiscoveryengineV1betaPanelInfoOut": "_discoveryengine_49_GoogleCloudDiscoveryengineV1betaPanelInfoOut",
        "GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataIn": "_discoveryengine_50_GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataIn",
        "GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataOut": "_discoveryengine_51_GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataOut",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataIn": "_discoveryengine_52_GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataIn",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataOut": "_discoveryengine_53_GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataOut",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseIn": "_discoveryengine_54_GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseOut": "_discoveryengine_55_GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataIn": "_discoveryengine_56_GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataIn",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataOut": "_discoveryengine_57_GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataOut",
        "GoogleRpcStatusIn": "_discoveryengine_58_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_discoveryengine_59_GoogleRpcStatusOut",
        "GoogleTypeDateIn": "_discoveryengine_60_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_discoveryengine_61_GoogleTypeDateOut",
        "GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseIn": "_discoveryengine_62_GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseOut": "_discoveryengine_63_GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1betaSchemaIn": "_discoveryengine_64_GoogleCloudDiscoveryengineV1betaSchemaIn",
        "GoogleCloudDiscoveryengineV1betaSchemaOut": "_discoveryengine_65_GoogleCloudDiscoveryengineV1betaSchemaOut",
        "GoogleCloudDiscoveryengineV1betaSearchInfoIn": "_discoveryengine_66_GoogleCloudDiscoveryengineV1betaSearchInfoIn",
        "GoogleCloudDiscoveryengineV1betaSearchInfoOut": "_discoveryengine_67_GoogleCloudDiscoveryengineV1betaSearchInfoOut",
        "GoogleCloudDiscoveryengineV1betaRecommendRequestIn": "_discoveryengine_68_GoogleCloudDiscoveryengineV1betaRecommendRequestIn",
        "GoogleCloudDiscoveryengineV1betaRecommendRequestOut": "_discoveryengine_69_GoogleCloudDiscoveryengineV1betaRecommendRequestOut",
        "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultIn": "_discoveryengine_70_GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultIn",
        "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultOut": "_discoveryengine_71_GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultOut",
        "GoogleCloudDiscoveryengineV1alphaSchemaIn": "_discoveryengine_72_GoogleCloudDiscoveryengineV1alphaSchemaIn",
        "GoogleCloudDiscoveryengineV1alphaSchemaOut": "_discoveryengine_73_GoogleCloudDiscoveryengineV1alphaSchemaOut",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestIn": "_discoveryengine_74_GoogleCloudDiscoveryengineV1betaImportUserEventsRequestIn",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestOut": "_discoveryengine_75_GoogleCloudDiscoveryengineV1betaImportUserEventsRequestOut",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsResponseIn": "_discoveryengine_76_GoogleCloudDiscoveryengineV1betaImportDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsResponseOut": "_discoveryengine_77_GoogleCloudDiscoveryengineV1betaImportDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1betaCustomAttributeIn": "_discoveryengine_78_GoogleCloudDiscoveryengineV1betaCustomAttributeIn",
        "GoogleCloudDiscoveryengineV1betaCustomAttributeOut": "_discoveryengine_79_GoogleCloudDiscoveryengineV1betaCustomAttributeOut",
        "GoogleCloudDiscoveryengineLoggingServiceContextIn": "_discoveryengine_80_GoogleCloudDiscoveryengineLoggingServiceContextIn",
        "GoogleCloudDiscoveryengineLoggingServiceContextOut": "_discoveryengine_81_GoogleCloudDiscoveryengineLoggingServiceContextOut",
        "GoogleCloudDiscoveryengineV1betaMediaInfoIn": "_discoveryengine_82_GoogleCloudDiscoveryengineV1betaMediaInfoIn",
        "GoogleCloudDiscoveryengineV1betaMediaInfoOut": "_discoveryengine_83_GoogleCloudDiscoveryengineV1betaMediaInfoOut",
        "GoogleCloudDiscoveryengineV1betaUserInfoIn": "_discoveryengine_84_GoogleCloudDiscoveryengineV1betaUserInfoIn",
        "GoogleCloudDiscoveryengineV1betaUserInfoOut": "_discoveryengine_85_GoogleCloudDiscoveryengineV1betaUserInfoOut",
        "GoogleProtobufEmptyIn": "_discoveryengine_86_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_discoveryengine_87_GoogleProtobufEmptyOut",
        "GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseIn": "_discoveryengine_88_GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseIn",
        "GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseOut": "_discoveryengine_89_GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseOut",
        "GoogleCloudDiscoveryengineLoggingSourceLocationIn": "_discoveryengine_90_GoogleCloudDiscoveryengineLoggingSourceLocationIn",
        "GoogleCloudDiscoveryengineLoggingSourceLocationOut": "_discoveryengine_91_GoogleCloudDiscoveryengineLoggingSourceLocationOut",
        "GoogleCloudDiscoveryengineV1betaDocumentIn": "_discoveryengine_92_GoogleCloudDiscoveryengineV1betaDocumentIn",
        "GoogleCloudDiscoveryengineV1betaDocumentOut": "_discoveryengine_93_GoogleCloudDiscoveryengineV1betaDocumentOut",
        "GoogleCloudDiscoveryengineV1betaUserEventIn": "_discoveryengine_94_GoogleCloudDiscoveryengineV1betaUserEventIn",
        "GoogleCloudDiscoveryengineV1betaUserEventOut": "_discoveryengine_95_GoogleCloudDiscoveryengineV1betaUserEventOut",
        "GoogleCloudDiscoveryengineLoggingHttpRequestContextIn": "_discoveryengine_96_GoogleCloudDiscoveryengineLoggingHttpRequestContextIn",
        "GoogleCloudDiscoveryengineLoggingHttpRequestContextOut": "_discoveryengine_97_GoogleCloudDiscoveryengineLoggingHttpRequestContextOut",
        "GoogleCloudDiscoveryengineLoggingErrorContextIn": "_discoveryengine_98_GoogleCloudDiscoveryengineLoggingErrorContextIn",
        "GoogleCloudDiscoveryengineLoggingErrorContextOut": "_discoveryengine_99_GoogleCloudDiscoveryengineLoggingErrorContextOut",
        "GoogleCloudDiscoveryengineV1betaPageInfoIn": "_discoveryengine_100_GoogleCloudDiscoveryengineV1betaPageInfoIn",
        "GoogleCloudDiscoveryengineV1betaPageInfoOut": "_discoveryengine_101_GoogleCloudDiscoveryengineV1betaPageInfoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"] = t.struct(
        {
            "datasetId": t.string(),
            "partitionDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "dataSchema": t.string().optional(),
            "gcsStagingDir": t.string().optional(),
            "tableId": t.string(),
            "projectId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"])
    types["GoogleCloudDiscoveryengineV1betaBigQuerySourceOut"] = t.struct(
        {
            "datasetId": t.string(),
            "partitionDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "dataSchema": t.string().optional(),
            "gcsStagingDir": t.string().optional(),
            "tableId": t.string(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceOut"])
    types["GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataOut"])
    types["GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataIn"] = t.struct(
        {
            "successCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataOut"] = t.struct(
        {
            "successCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataOut"])
    types["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataOut"])
    types["GoogleCloudDiscoveryengineV1betaRecommendResponseIn"] = t.struct(
        {
            "attributionToken": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "missingIds": t.array(t.string()).optional(),
            "results": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaRecommendResponseIn"])
    types["GoogleCloudDiscoveryengineV1betaRecommendResponseOut"] = t.struct(
        {
            "attributionToken": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "missingIds": t.array(t.string()).optional(),
            "results": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaRecommendResponseOut"])
    types["GoogleCloudDiscoveryengineLoggingErrorLogIn"] = t.struct(
        {
            "responsePayload": t.struct({"_": t.string().optional()}).optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "importPayload": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingImportErrorContextIn"]
            ).optional(),
            "message": t.string().optional(),
            "context": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingErrorContextIn"]
            ).optional(),
            "serviceContext": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingServiceContextIn"]
            ).optional(),
            "requestPayload": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingErrorLogIn"])
    types["GoogleCloudDiscoveryengineLoggingErrorLogOut"] = t.struct(
        {
            "responsePayload": t.struct({"_": t.string().optional()}).optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "importPayload": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingImportErrorContextOut"]
            ).optional(),
            "message": t.string().optional(),
            "context": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingErrorContextOut"]
            ).optional(),
            "serviceContext": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingServiceContextOut"]
            ).optional(),
            "requestPayload": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingErrorLogOut"])
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
    types["GoogleCloudDiscoveryengineV1betaTransactionInfoIn"] = t.struct(
        {
            "cost": t.number().optional(),
            "discountValue": t.number().optional(),
            "transactionId": t.string().optional(),
            "value": t.number(),
            "currency": t.string(),
            "tax": t.number().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaTransactionInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaTransactionInfoOut"] = t.struct(
        {
            "cost": t.number().optional(),
            "discountValue": t.number().optional(),
            "transactionId": t.string().optional(),
            "value": t.number(),
            "currency": t.string(),
            "tax": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaTransactionInfoOut"])
    types["GoogleCloudDiscoveryengineV1betaCompletionInfoIn"] = t.struct(
        {
            "selectedPosition": t.integer().optional(),
            "selectedSuggestion": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaCompletionInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaCompletionInfoOut"] = t.struct(
        {
            "selectedPosition": t.integer().optional(),
            "selectedSuggestion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaCompletionInfoOut"])
    types["GoogleCloudDiscoveryengineV1betaGcsSourceIn"] = t.struct(
        {"inputUris": t.array(t.string()), "dataSchema": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"])
    types["GoogleCloudDiscoveryengineV1betaGcsSourceOut"] = t.struct(
        {
            "inputUris": t.array(t.string()),
            "dataSchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaGcsSourceOut"])
    types["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"])
    types["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsResponseIn"] = t.struct(
        {
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
            ).optional(),
            "unjoinedEventsCount": t.string().optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "joinedEventsCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsResponseIn"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsResponseOut"] = t.struct(
        {
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"]
            ).optional(),
            "unjoinedEventsCount": t.string().optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "joinedEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsResponseOut"])
    types["GoogleCloudDiscoveryengineLoggingImportErrorContextIn"] = t.struct(
        {
            "gcsPath": t.string().optional(),
            "operation": t.string().optional(),
            "lineNumber": t.string().optional(),
            "userEvent": t.string().optional(),
            "document": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingImportErrorContextIn"])
    types["GoogleCloudDiscoveryengineLoggingImportErrorContextOut"] = t.struct(
        {
            "gcsPath": t.string().optional(),
            "operation": t.string().optional(),
            "lineNumber": t.string().optional(),
            "userEvent": t.string().optional(),
            "document": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingImportErrorContextOut"])
    types["GoogleApiHttpBodyIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "data": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleApiHttpBodyIn"])
    types["GoogleApiHttpBodyOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "data": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiHttpBodyOut"])
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
    types["GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn"])
    types["GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut"])
    types["GoogleCloudDiscoveryengineV1betaImportDocumentsRequestIn"] = t.struct(
        {
            "gcsSource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
            ).optional(),
            "bigquerySource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
            ).optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
            ).optional(),
            "inlineSource": t.proxy(
                renames[
                    "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceIn"
                ]
            ).optional(),
            "reconciliationMode": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportDocumentsRequestIn"])
    types["GoogleCloudDiscoveryengineV1betaImportDocumentsRequestOut"] = t.struct(
        {
            "gcsSource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaGcsSourceOut"]
            ).optional(),
            "bigquerySource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceOut"]
            ).optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"]
            ).optional(),
            "inlineSource": t.proxy(
                renames[
                    "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceOut"
                ]
            ).optional(),
            "reconciliationMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportDocumentsRequestOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleCloudDiscoveryengineV1betaDocumentInfoIn"] = t.struct(
        {
            "quantity": t.integer().optional(),
            "name": t.string(),
            "promotionIds": t.array(t.string()).optional(),
            "uri": t.string(),
            "id": t.string(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaDocumentInfoOut"] = t.struct(
        {
            "quantity": t.integer().optional(),
            "name": t.string(),
            "promotionIds": t.array(t.string()).optional(),
            "uri": t.string(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoOut"])
    types["GoogleCloudDiscoveryengineV1betaPanelInfoIn"] = t.struct(
        {
            "panelPosition": t.integer().optional(),
            "totalPanels": t.integer().optional(),
            "panelId": t.string(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPanelInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaPanelInfoOut"] = t.struct(
        {
            "panelPosition": t.integer().optional(),
            "totalPanels": t.integer().optional(),
            "panelId": t.string(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPanelInfoOut"])
    types["GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataIn"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataOut"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataOut"])
    types["GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataIn"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "successCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataOut"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "successCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataOut"])
    types["GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseIn"] = t.struct(
        {
            "purgeSample": t.array(t.string()).optional(),
            "purgeCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseIn"])
    types["GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseOut"] = t.struct(
        {
            "purgeSample": t.array(t.string()).optional(),
            "purgeCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseOut"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataIn"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataOut"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleTypeDateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])
    types["GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseIn"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseIn"])
    types["GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseOut"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseOut"])
    types["GoogleCloudDiscoveryengineV1betaSchemaIn"] = t.struct(
        {
            "name": t.string().optional(),
            "structSchema": t.struct({"_": t.string().optional()}).optional(),
            "jsonSchema": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaSchemaIn"])
    types["GoogleCloudDiscoveryengineV1betaSchemaOut"] = t.struct(
        {
            "name": t.string().optional(),
            "structSchema": t.struct({"_": t.string().optional()}).optional(),
            "jsonSchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaSchemaOut"])
    types["GoogleCloudDiscoveryengineV1betaSearchInfoIn"] = t.struct(
        {
            "orderBy": t.string().optional(),
            "offset": t.integer().optional(),
            "searchQuery": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaSearchInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaSearchInfoOut"] = t.struct(
        {
            "orderBy": t.string().optional(),
            "offset": t.integer().optional(),
            "searchQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaSearchInfoOut"])
    types["GoogleCloudDiscoveryengineV1betaRecommendRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "userEvent": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaUserEventIn"]
            ),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "validateOnly": t.boolean().optional(),
            "filter": t.string().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaRecommendRequestIn"])
    types["GoogleCloudDiscoveryengineV1betaRecommendRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "userEvent": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaUserEventOut"]
            ),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "validateOnly": t.boolean().optional(),
            "filter": t.string().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaRecommendRequestOut"])
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
    types["GoogleCloudDiscoveryengineV1alphaSchemaIn"] = t.struct(
        {
            "name": t.string().optional(),
            "structSchema": t.struct({"_": t.string().optional()}).optional(),
            "jsonSchema": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaSchemaIn"])
    types["GoogleCloudDiscoveryengineV1alphaSchemaOut"] = t.struct(
        {
            "name": t.string().optional(),
            "structSchema": t.struct({"_": t.string().optional()}).optional(),
            "jsonSchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaSchemaOut"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsRequestIn"] = t.struct(
        {
            "gcsSource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
            ),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
            ).optional(),
            "bigquerySource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
            ),
            "inlineSource": t.proxy(
                renames[
                    "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                ]
            ),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsRequestIn"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsRequestOut"] = t.struct(
        {
            "gcsSource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaGcsSourceOut"]
            ),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"]
            ).optional(),
            "bigquerySource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceOut"]
            ),
            "inlineSource": t.proxy(
                renames[
                    "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceOut"
                ]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsRequestOut"])
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
    types["GoogleCloudDiscoveryengineV1betaCustomAttributeIn"] = t.struct(
        {
            "numbers": t.array(t.number()).optional(),
            "text": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaCustomAttributeIn"])
    types["GoogleCloudDiscoveryengineV1betaCustomAttributeOut"] = t.struct(
        {
            "numbers": t.array(t.number()).optional(),
            "text": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaCustomAttributeOut"])
    types["GoogleCloudDiscoveryengineLoggingServiceContextIn"] = t.struct(
        {"service": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineLoggingServiceContextIn"])
    types["GoogleCloudDiscoveryengineLoggingServiceContextOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingServiceContextOut"])
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
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseIn"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "unjoinedEventsCount": t.string().optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn"]
            ).optional(),
            "joinedEventsCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseIn"])
    types["GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseOut"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "unjoinedEventsCount": t.string().optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut"]
            ).optional(),
            "joinedEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseOut"])
    types["GoogleCloudDiscoveryengineLoggingSourceLocationIn"] = t.struct(
        {"functionName": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineLoggingSourceLocationIn"])
    types["GoogleCloudDiscoveryengineLoggingSourceLocationOut"] = t.struct(
        {
            "functionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingSourceLocationOut"])
    types["GoogleCloudDiscoveryengineV1betaDocumentIn"] = t.struct(
        {
            "structData": t.struct({"_": t.string().optional()}).optional(),
            "parentDocumentId": t.string().optional(),
            "jsonData": t.string().optional(),
            "id": t.string().optional(),
            "schemaId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaDocumentIn"])
    types["GoogleCloudDiscoveryengineV1betaDocumentOut"] = t.struct(
        {
            "structData": t.struct({"_": t.string().optional()}).optional(),
            "parentDocumentId": t.string().optional(),
            "jsonData": t.string().optional(),
            "id": t.string().optional(),
            "schemaId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"])
    types["GoogleCloudDiscoveryengineV1betaUserEventIn"] = t.struct(
        {
            "documents": t.array(
                t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoIn"])
            ).optional(),
            "transactionInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaTransactionInfoIn"]
            ).optional(),
            "eventType": t.string(),
            "completionInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaCompletionInfoIn"]
            ).optional(),
            "panel": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaPanelInfoIn"]
            ).optional(),
            "sessionId": t.string().optional(),
            "eventTime": t.string().optional(),
            "tagIds": t.array(t.string()).optional(),
            "attributionToken": t.string().optional(),
            "promotionIds": t.array(t.string()).optional(),
            "userInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaUserInfoIn"]
            ).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "directUserRequest": t.boolean().optional(),
            "userPseudoId": t.string(),
            "searchInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaSearchInfoIn"]
            ).optional(),
            "filter": t.string().optional(),
            "mediaInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaMediaInfoIn"]
            ).optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaPageInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaUserEventIn"])
    types["GoogleCloudDiscoveryengineV1betaUserEventOut"] = t.struct(
        {
            "documents": t.array(
                t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoOut"])
            ).optional(),
            "transactionInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaTransactionInfoOut"]
            ).optional(),
            "eventType": t.string(),
            "completionInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaCompletionInfoOut"]
            ).optional(),
            "panel": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaPanelInfoOut"]
            ).optional(),
            "sessionId": t.string().optional(),
            "eventTime": t.string().optional(),
            "tagIds": t.array(t.string()).optional(),
            "attributionToken": t.string().optional(),
            "promotionIds": t.array(t.string()).optional(),
            "userInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaUserInfoOut"]
            ).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "directUserRequest": t.boolean().optional(),
            "userPseudoId": t.string(),
            "searchInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaSearchInfoOut"]
            ).optional(),
            "filter": t.string().optional(),
            "mediaInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaMediaInfoOut"]
            ).optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaPageInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaUserEventOut"])
    types["GoogleCloudDiscoveryengineLoggingHttpRequestContextIn"] = t.struct(
        {"responseStatusCode": t.integer().optional()}
    ).named(renames["GoogleCloudDiscoveryengineLoggingHttpRequestContextIn"])
    types["GoogleCloudDiscoveryengineLoggingHttpRequestContextOut"] = t.struct(
        {
            "responseStatusCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingHttpRequestContextOut"])
    types["GoogleCloudDiscoveryengineLoggingErrorContextIn"] = t.struct(
        {
            "httpRequest": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingHttpRequestContextIn"]
            ).optional(),
            "reportLocation": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingSourceLocationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingErrorContextIn"])
    types["GoogleCloudDiscoveryengineLoggingErrorContextOut"] = t.struct(
        {
            "httpRequest": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingHttpRequestContextOut"]
            ).optional(),
            "reportLocation": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingSourceLocationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingErrorContextOut"])
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

    functions = {}
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
    functions[
        "projectsLocationsCollectionsDataStoresUserEventsCollect"
    ] = discoveryengine.post(
        "v1beta/{parent}/userEvents:import",
        t.struct(
            {
                "parent": t.string(),
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ),
                "errorConfig": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
                ).optional(),
                "bigquerySource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
                ),
                "inlineSource": t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                    ]
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
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ),
                "errorConfig": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
                ).optional(),
                "bigquerySource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
                ),
                "inlineSource": t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                    ]
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
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ),
                "errorConfig": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
                ).optional(),
                "bigquerySource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
                ),
                "inlineSource": t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                    ]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
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
        "projectsLocationsCollectionsDataStoresBranchesOperationsList"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesOperationsGet"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsPurge"
    ] = discoveryengine.get(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsDelete"
    ] = discoveryengine.get(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsGet"
    ] = discoveryengine.get(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsPatch"
    ] = discoveryengine.get(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsImport"
    ] = discoveryengine.get(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsCreate"
    ] = discoveryengine.get(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsList"
    ] = discoveryengine.get(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresOperationsGet"
    ] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresOperationsList"
    ] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
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
                "pageSize": t.integer().optional(),
                "userEvent": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaUserEventIn"]
                ),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "validateOnly": t.boolean().optional(),
                "filter": t.string().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaRecommendResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCollectionsOperationsList"] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCollectionsOperationsGet"] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCollectionsEnginesOperationsGet"] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
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
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresBranchesOperationsGet"] = discoveryengine.get(
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
        "projectsLocationsDataStoresBranchesOperationsList"
    ] = discoveryengine.get(
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
        "projectsLocationsDataStoresBranchesDocumentsImport"
    ] = discoveryengine.post(
        "v1beta/{parent}/documents:purge",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataStoresBranchesDocumentsDelete"
    ] = discoveryengine.post(
        "v1beta/{parent}/documents:purge",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataStoresBranchesDocumentsCreate"
    ] = discoveryengine.post(
        "v1beta/{parent}/documents:purge",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataStoresBranchesDocumentsList"
    ] = discoveryengine.post(
        "v1beta/{parent}/documents:purge",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresBranchesDocumentsGet"] = discoveryengine.post(
        "v1beta/{parent}/documents:purge",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataStoresBranchesDocumentsPatch"
    ] = discoveryengine.post(
        "v1beta/{parent}/documents:purge",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataStoresBranchesDocumentsPurge"
    ] = discoveryengine.post(
        "v1beta/{parent}/documents:purge",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresUserEventsCollect"] = discoveryengine.post(
        "v1beta/{parent}/userEvents:import",
        t.struct(
            {
                "parent": t.string(),
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ),
                "errorConfig": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
                ).optional(),
                "bigquerySource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
                ),
                "inlineSource": t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                    ]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresUserEventsWrite"] = discoveryengine.post(
        "v1beta/{parent}/userEvents:import",
        t.struct(
            {
                "parent": t.string(),
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ),
                "errorConfig": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
                ).optional(),
                "bigquerySource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
                ),
                "inlineSource": t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                    ]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresUserEventsImport"] = discoveryengine.post(
        "v1beta/{parent}/userEvents:import",
        t.struct(
            {
                "parent": t.string(),
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ),
                "errorConfig": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
                ).optional(),
                "bigquerySource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
                ),
                "inlineSource": t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                    ]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresModelsOperationsGet"] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresModelsOperationsList"] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageSize": t.integer().optional(),
                "userEvent": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaUserEventIn"]
                ),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "validateOnly": t.boolean().optional(),
                "filter": t.string().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaRecommendResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresOperationsGet"] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="discoveryengine",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
