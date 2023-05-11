from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_discoveryengine() -> Import:
    discoveryengine = HTTPRuntime("https://discoveryengine.googleapis.com/")

    renames = {
        "ErrorResponse": "_discoveryengine_1_ErrorResponse",
        "GoogleCloudDiscoveryengineLoggingServiceContextIn": "_discoveryengine_2_GoogleCloudDiscoveryengineLoggingServiceContextIn",
        "GoogleCloudDiscoveryengineLoggingServiceContextOut": "_discoveryengine_3_GoogleCloudDiscoveryengineLoggingServiceContextOut",
        "GoogleCloudDiscoveryengineV1alphaSchemaIn": "_discoveryengine_4_GoogleCloudDiscoveryengineV1alphaSchemaIn",
        "GoogleCloudDiscoveryengineV1alphaSchemaOut": "_discoveryengine_5_GoogleCloudDiscoveryengineV1alphaSchemaOut",
        "GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseIn": "_discoveryengine_6_GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseIn",
        "GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseOut": "_discoveryengine_7_GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseOut",
        "GoogleLongrunningOperationIn": "_discoveryengine_8_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_discoveryengine_9_GoogleLongrunningOperationOut",
        "GoogleRpcStatusIn": "_discoveryengine_10_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_discoveryengine_11_GoogleRpcStatusOut",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestIn": "_discoveryengine_12_GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestIn",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestOut": "_discoveryengine_13_GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestOut",
        "GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataIn": "_discoveryengine_14_GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataIn",
        "GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataOut": "_discoveryengine_15_GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataOut",
        "GoogleCloudDiscoveryengineV1betaPanelInfoIn": "_discoveryengine_16_GoogleCloudDiscoveryengineV1betaPanelInfoIn",
        "GoogleCloudDiscoveryengineV1betaPanelInfoOut": "_discoveryengine_17_GoogleCloudDiscoveryengineV1betaPanelInfoOut",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsResponseIn": "_discoveryengine_18_GoogleCloudDiscoveryengineV1betaImportUserEventsResponseIn",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsResponseOut": "_discoveryengine_19_GoogleCloudDiscoveryengineV1betaImportUserEventsResponseOut",
        "GoogleTypeDateIn": "_discoveryengine_20_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_discoveryengine_21_GoogleTypeDateOut",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestIn": "_discoveryengine_22_GoogleCloudDiscoveryengineV1betaImportDocumentsRequestIn",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestOut": "_discoveryengine_23_GoogleCloudDiscoveryengineV1betaImportDocumentsRequestOut",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceIn": "_discoveryengine_24_GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceIn",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceOut": "_discoveryengine_25_GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceOut",
        "GoogleCloudDiscoveryengineV1betaCustomAttributeIn": "_discoveryengine_26_GoogleCloudDiscoveryengineV1betaCustomAttributeIn",
        "GoogleCloudDiscoveryengineV1betaCustomAttributeOut": "_discoveryengine_27_GoogleCloudDiscoveryengineV1betaCustomAttributeOut",
        "GoogleCloudDiscoveryengineV1betaGcsSourceIn": "_discoveryengine_28_GoogleCloudDiscoveryengineV1betaGcsSourceIn",
        "GoogleCloudDiscoveryengineV1betaGcsSourceOut": "_discoveryengine_29_GoogleCloudDiscoveryengineV1betaGcsSourceOut",
        "GoogleLongrunningListOperationsResponseIn": "_discoveryengine_30_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_discoveryengine_31_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudDiscoveryengineV1betaPageInfoIn": "_discoveryengine_32_GoogleCloudDiscoveryengineV1betaPageInfoIn",
        "GoogleCloudDiscoveryengineV1betaPageInfoOut": "_discoveryengine_33_GoogleCloudDiscoveryengineV1betaPageInfoOut",
        "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultIn": "_discoveryengine_34_GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultIn",
        "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultOut": "_discoveryengine_35_GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultOut",
        "GoogleCloudDiscoveryengineV1betaRecommendResponseIn": "_discoveryengine_36_GoogleCloudDiscoveryengineV1betaRecommendResponseIn",
        "GoogleCloudDiscoveryengineV1betaRecommendResponseOut": "_discoveryengine_37_GoogleCloudDiscoveryengineV1betaRecommendResponseOut",
        "GoogleCloudDiscoveryengineV1betaDocumentIn": "_discoveryengine_38_GoogleCloudDiscoveryengineV1betaDocumentIn",
        "GoogleCloudDiscoveryengineV1betaDocumentOut": "_discoveryengine_39_GoogleCloudDiscoveryengineV1betaDocumentOut",
        "GoogleCloudDiscoveryengineLoggingImportErrorContextIn": "_discoveryengine_40_GoogleCloudDiscoveryengineLoggingImportErrorContextIn",
        "GoogleCloudDiscoveryengineLoggingImportErrorContextOut": "_discoveryengine_41_GoogleCloudDiscoveryengineLoggingImportErrorContextOut",
        "GoogleCloudDiscoveryengineV1betaRecommendRequestIn": "_discoveryengine_42_GoogleCloudDiscoveryengineV1betaRecommendRequestIn",
        "GoogleCloudDiscoveryengineV1betaRecommendRequestOut": "_discoveryengine_43_GoogleCloudDiscoveryengineV1betaRecommendRequestOut",
        "GoogleCloudDiscoveryengineLoggingErrorContextIn": "_discoveryengine_44_GoogleCloudDiscoveryengineLoggingErrorContextIn",
        "GoogleCloudDiscoveryengineLoggingErrorContextOut": "_discoveryengine_45_GoogleCloudDiscoveryengineLoggingErrorContextOut",
        "GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataIn": "_discoveryengine_46_GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataIn",
        "GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataOut": "_discoveryengine_47_GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataOut",
        "GoogleCloudDiscoveryengineLoggingSourceLocationIn": "_discoveryengine_48_GoogleCloudDiscoveryengineLoggingSourceLocationIn",
        "GoogleCloudDiscoveryengineLoggingSourceLocationOut": "_discoveryengine_49_GoogleCloudDiscoveryengineLoggingSourceLocationOut",
        "GoogleProtobufEmptyIn": "_discoveryengine_50_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_discoveryengine_51_GoogleProtobufEmptyOut",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsResponseIn": "_discoveryengine_52_GoogleCloudDiscoveryengineV1betaImportDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsResponseOut": "_discoveryengine_53_GoogleCloudDiscoveryengineV1betaImportDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataIn": "_discoveryengine_54_GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataIn",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataOut": "_discoveryengine_55_GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataOut",
        "GoogleCloudDiscoveryengineV1betaDocumentInfoIn": "_discoveryengine_56_GoogleCloudDiscoveryengineV1betaDocumentInfoIn",
        "GoogleCloudDiscoveryengineV1betaDocumentInfoOut": "_discoveryengine_57_GoogleCloudDiscoveryengineV1betaDocumentInfoOut",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn": "_discoveryengine_58_GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceOut": "_discoveryengine_59_GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceOut",
        "GoogleApiHttpBodyIn": "_discoveryengine_60_GoogleApiHttpBodyIn",
        "GoogleApiHttpBodyOut": "_discoveryengine_61_GoogleApiHttpBodyOut",
        "GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataIn": "_discoveryengine_62_GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataIn",
        "GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataOut": "_discoveryengine_63_GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataOut",
        "GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseIn": "_discoveryengine_64_GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseOut": "_discoveryengine_65_GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseIn": "_discoveryengine_66_GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseOut": "_discoveryengine_67_GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1betaTransactionInfoIn": "_discoveryengine_68_GoogleCloudDiscoveryengineV1betaTransactionInfoIn",
        "GoogleCloudDiscoveryengineV1betaTransactionInfoOut": "_discoveryengine_69_GoogleCloudDiscoveryengineV1betaTransactionInfoOut",
        "GoogleCloudDiscoveryengineV1betaImportErrorConfigIn": "_discoveryengine_70_GoogleCloudDiscoveryengineV1betaImportErrorConfigIn",
        "GoogleCloudDiscoveryengineV1betaImportErrorConfigOut": "_discoveryengine_71_GoogleCloudDiscoveryengineV1betaImportErrorConfigOut",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataIn": "_discoveryengine_72_GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataIn",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataOut": "_discoveryengine_73_GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataOut",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestIn": "_discoveryengine_74_GoogleCloudDiscoveryengineV1betaImportUserEventsRequestIn",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestOut": "_discoveryengine_75_GoogleCloudDiscoveryengineV1betaImportUserEventsRequestOut",
        "GoogleCloudDiscoveryengineV1betaUserEventIn": "_discoveryengine_76_GoogleCloudDiscoveryengineV1betaUserEventIn",
        "GoogleCloudDiscoveryengineV1betaUserEventOut": "_discoveryengine_77_GoogleCloudDiscoveryengineV1betaUserEventOut",
        "GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn": "_discoveryengine_78_GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn",
        "GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut": "_discoveryengine_79_GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut",
        "GoogleCloudDiscoveryengineV1betaBigQuerySourceIn": "_discoveryengine_80_GoogleCloudDiscoveryengineV1betaBigQuerySourceIn",
        "GoogleCloudDiscoveryengineV1betaBigQuerySourceOut": "_discoveryengine_81_GoogleCloudDiscoveryengineV1betaBigQuerySourceOut",
        "GoogleCloudDiscoveryengineV1betaCompletionInfoIn": "_discoveryengine_82_GoogleCloudDiscoveryengineV1betaCompletionInfoIn",
        "GoogleCloudDiscoveryengineV1betaCompletionInfoOut": "_discoveryengine_83_GoogleCloudDiscoveryengineV1betaCompletionInfoOut",
        "GoogleCloudDiscoveryengineLoggingErrorLogIn": "_discoveryengine_84_GoogleCloudDiscoveryengineLoggingErrorLogIn",
        "GoogleCloudDiscoveryengineLoggingErrorLogOut": "_discoveryengine_85_GoogleCloudDiscoveryengineLoggingErrorLogOut",
        "GoogleCloudDiscoveryengineV1betaSchemaIn": "_discoveryengine_86_GoogleCloudDiscoveryengineV1betaSchemaIn",
        "GoogleCloudDiscoveryengineV1betaSchemaOut": "_discoveryengine_87_GoogleCloudDiscoveryengineV1betaSchemaOut",
        "GoogleCloudDiscoveryengineV1betaSearchInfoIn": "_discoveryengine_88_GoogleCloudDiscoveryengineV1betaSearchInfoIn",
        "GoogleCloudDiscoveryengineV1betaSearchInfoOut": "_discoveryengine_89_GoogleCloudDiscoveryengineV1betaSearchInfoOut",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataIn": "_discoveryengine_90_GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataIn",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataOut": "_discoveryengine_91_GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataOut",
        "GoogleCloudDiscoveryengineV1betaListDocumentsResponseIn": "_discoveryengine_92_GoogleCloudDiscoveryengineV1betaListDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut": "_discoveryengine_93_GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseIn": "_discoveryengine_94_GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseOut": "_discoveryengine_95_GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1betaUserInfoIn": "_discoveryengine_96_GoogleCloudDiscoveryengineV1betaUserInfoIn",
        "GoogleCloudDiscoveryengineV1betaUserInfoOut": "_discoveryengine_97_GoogleCloudDiscoveryengineV1betaUserInfoOut",
        "GoogleCloudDiscoveryengineV1betaMediaInfoIn": "_discoveryengine_98_GoogleCloudDiscoveryengineV1betaMediaInfoIn",
        "GoogleCloudDiscoveryengineV1betaMediaInfoOut": "_discoveryengine_99_GoogleCloudDiscoveryengineV1betaMediaInfoOut",
        "GoogleCloudDiscoveryengineLoggingHttpRequestContextIn": "_discoveryengine_100_GoogleCloudDiscoveryengineLoggingHttpRequestContextIn",
        "GoogleCloudDiscoveryengineLoggingHttpRequestContextOut": "_discoveryengine_101_GoogleCloudDiscoveryengineLoggingHttpRequestContextOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudDiscoveryengineLoggingServiceContextIn"] = t.struct(
        {"service": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineLoggingServiceContextIn"])
    types["GoogleCloudDiscoveryengineLoggingServiceContextOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingServiceContextOut"])
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
    types["GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseIn"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "unjoinedEventsCount": t.string().optional(),
            "joinedEventsCount": t.string().optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseIn"])
    types["GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseOut"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "unjoinedEventsCount": t.string().optional(),
            "joinedEventsCount": t.string().optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
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
    types["GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataIn"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "successCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataOut"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "successCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataOut"])
    types["GoogleCloudDiscoveryengineV1betaPanelInfoIn"] = t.struct(
        {
            "panelPosition": t.integer().optional(),
            "displayName": t.string().optional(),
            "panelId": t.string(),
            "totalPanels": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPanelInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaPanelInfoOut"] = t.struct(
        {
            "panelPosition": t.integer().optional(),
            "displayName": t.string().optional(),
            "panelId": t.string(),
            "totalPanels": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPanelInfoOut"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsResponseIn"] = t.struct(
        {
            "unjoinedEventsCount": t.string().optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "joinedEventsCount": t.string().optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsResponseIn"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsResponseOut"] = t.struct(
        {
            "unjoinedEventsCount": t.string().optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "joinedEventsCount": t.string().optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsResponseOut"])
    types["GoogleTypeDateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])
    types["GoogleCloudDiscoveryengineV1betaImportDocumentsRequestIn"] = t.struct(
        {
            "inlineSource": t.proxy(
                renames[
                    "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceIn"
                ]
            ).optional(),
            "bigquerySource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
            ).optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
            ).optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
            ).optional(),
            "reconciliationMode": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportDocumentsRequestIn"])
    types["GoogleCloudDiscoveryengineV1betaImportDocumentsRequestOut"] = t.struct(
        {
            "inlineSource": t.proxy(
                renames[
                    "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceOut"
                ]
            ).optional(),
            "bigquerySource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceOut"]
            ).optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"]
            ).optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaGcsSourceOut"]
            ).optional(),
            "reconciliationMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportDocumentsRequestOut"])
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
    types["GoogleCloudDiscoveryengineV1betaPageInfoIn"] = t.struct(
        {
            "pageviewId": t.string().optional(),
            "uri": t.string().optional(),
            "referrerUri": t.string().optional(),
            "pageCategory": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPageInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaPageInfoOut"] = t.struct(
        {
            "pageviewId": t.string().optional(),
            "uri": t.string().optional(),
            "referrerUri": t.string().optional(),
            "pageCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPageInfoOut"])
    types[
        "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultIn"
    ] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "document": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaDocumentIn"]
            ).optional(),
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
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "document": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultOut"
        ]
    )
    types["GoogleCloudDiscoveryengineV1betaRecommendResponseIn"] = t.struct(
        {
            "missingIds": t.array(t.string()).optional(),
            "attributionToken": t.string().optional(),
            "results": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultIn"
                    ]
                )
            ).optional(),
            "validateOnly": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaRecommendResponseIn"])
    types["GoogleCloudDiscoveryengineV1betaRecommendResponseOut"] = t.struct(
        {
            "missingIds": t.array(t.string()).optional(),
            "attributionToken": t.string().optional(),
            "results": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultOut"
                    ]
                )
            ).optional(),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaRecommendResponseOut"])
    types["GoogleCloudDiscoveryengineV1betaDocumentIn"] = t.struct(
        {
            "name": t.string().optional(),
            "parentDocumentId": t.string().optional(),
            "id": t.string().optional(),
            "schemaId": t.string().optional(),
            "jsonData": t.string().optional(),
            "structData": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaDocumentIn"])
    types["GoogleCloudDiscoveryengineV1betaDocumentOut"] = t.struct(
        {
            "name": t.string().optional(),
            "parentDocumentId": t.string().optional(),
            "id": t.string().optional(),
            "schemaId": t.string().optional(),
            "jsonData": t.string().optional(),
            "structData": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"])
    types["GoogleCloudDiscoveryengineLoggingImportErrorContextIn"] = t.struct(
        {
            "operation": t.string().optional(),
            "userEvent": t.string().optional(),
            "document": t.string().optional(),
            "gcsPath": t.string().optional(),
            "lineNumber": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingImportErrorContextIn"])
    types["GoogleCloudDiscoveryengineLoggingImportErrorContextOut"] = t.struct(
        {
            "operation": t.string().optional(),
            "userEvent": t.string().optional(),
            "document": t.string().optional(),
            "gcsPath": t.string().optional(),
            "lineNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingImportErrorContextOut"])
    types["GoogleCloudDiscoveryengineV1betaRecommendRequestIn"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "filter": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "pageSize": t.integer().optional(),
            "userEvent": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaUserEventIn"]
            ),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaRecommendRequestIn"])
    types["GoogleCloudDiscoveryengineV1betaRecommendRequestOut"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "filter": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "pageSize": t.integer().optional(),
            "userEvent": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaUserEventOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaRecommendRequestOut"])
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
    types["GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "successCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "successCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataOut"])
    types["GoogleCloudDiscoveryengineLoggingSourceLocationIn"] = t.struct(
        {"functionName": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineLoggingSourceLocationIn"])
    types["GoogleCloudDiscoveryengineLoggingSourceLocationOut"] = t.struct(
        {
            "functionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingSourceLocationOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
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
    types["GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataIn"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "successCount": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataOut"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "successCount": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataOut"])
    types["GoogleCloudDiscoveryengineV1betaDocumentInfoIn"] = t.struct(
        {
            "name": t.string(),
            "id": t.string(),
            "uri": t.string(),
            "quantity": t.integer().optional(),
            "promotionIds": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaDocumentInfoOut"] = t.struct(
        {
            "name": t.string(),
            "id": t.string(),
            "uri": t.string(),
            "quantity": t.integer().optional(),
            "promotionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoOut"])
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
    types["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "successCount": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "successCount": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataOut"])
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
    types["GoogleCloudDiscoveryengineV1betaTransactionInfoIn"] = t.struct(
        {
            "transactionId": t.string().optional(),
            "discountValue": t.number().optional(),
            "tax": t.number().optional(),
            "value": t.number(),
            "currency": t.string(),
            "cost": t.number().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaTransactionInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaTransactionInfoOut"] = t.struct(
        {
            "transactionId": t.string().optional(),
            "discountValue": t.number().optional(),
            "tax": t.number().optional(),
            "value": t.number(),
            "currency": t.string(),
            "cost": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaTransactionInfoOut"])
    types["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"])
    types["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataOut"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsRequestIn"] = t.struct(
        {
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
            ).optional(),
            "inlineSource": t.proxy(
                renames[
                    "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                ]
            ),
            "bigquerySource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
            ),
            "gcsSource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
            ),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsRequestIn"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsRequestOut"] = t.struct(
        {
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"]
            ).optional(),
            "inlineSource": t.proxy(
                renames[
                    "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceOut"
                ]
            ),
            "bigquerySource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceOut"]
            ),
            "gcsSource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaGcsSourceOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsRequestOut"])
    types["GoogleCloudDiscoveryengineV1betaUserEventIn"] = t.struct(
        {
            "filter": t.string().optional(),
            "searchInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaSearchInfoIn"]
            ).optional(),
            "eventTime": t.string().optional(),
            "mediaInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaMediaInfoIn"]
            ).optional(),
            "panel": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaPanelInfoIn"]
            ).optional(),
            "transactionInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaTransactionInfoIn"]
            ).optional(),
            "documents": t.array(
                t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoIn"])
            ).optional(),
            "tagIds": t.array(t.string()).optional(),
            "promotionIds": t.array(t.string()).optional(),
            "completionInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaCompletionInfoIn"]
            ).optional(),
            "sessionId": t.string().optional(),
            "userInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaUserInfoIn"]
            ).optional(),
            "userPseudoId": t.string(),
            "attributionToken": t.string().optional(),
            "directUserRequest": t.boolean().optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaPageInfoIn"]
            ).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "eventType": t.string(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaUserEventIn"])
    types["GoogleCloudDiscoveryengineV1betaUserEventOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "searchInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaSearchInfoOut"]
            ).optional(),
            "eventTime": t.string().optional(),
            "mediaInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaMediaInfoOut"]
            ).optional(),
            "panel": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaPanelInfoOut"]
            ).optional(),
            "transactionInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaTransactionInfoOut"]
            ).optional(),
            "documents": t.array(
                t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoOut"])
            ).optional(),
            "tagIds": t.array(t.string()).optional(),
            "promotionIds": t.array(t.string()).optional(),
            "completionInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaCompletionInfoOut"]
            ).optional(),
            "sessionId": t.string().optional(),
            "userInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaUserInfoOut"]
            ).optional(),
            "userPseudoId": t.string(),
            "attributionToken": t.string().optional(),
            "directUserRequest": t.boolean().optional(),
            "pageInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaPageInfoOut"]
            ).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "eventType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaUserEventOut"])
    types["GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn"])
    types["GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut"])
    types["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"] = t.struct(
        {
            "tableId": t.string(),
            "dataSchema": t.string().optional(),
            "gcsStagingDir": t.string().optional(),
            "partitionDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "projectId": t.string().optional(),
            "datasetId": t.string(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"])
    types["GoogleCloudDiscoveryengineV1betaBigQuerySourceOut"] = t.struct(
        {
            "tableId": t.string(),
            "dataSchema": t.string().optional(),
            "gcsStagingDir": t.string().optional(),
            "partitionDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "projectId": t.string().optional(),
            "datasetId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceOut"])
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
    types["GoogleCloudDiscoveryengineLoggingErrorLogIn"] = t.struct(
        {
            "responsePayload": t.struct({"_": t.string().optional()}).optional(),
            "context": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingErrorContextIn"]
            ).optional(),
            "requestPayload": t.struct({"_": t.string().optional()}).optional(),
            "message": t.string().optional(),
            "serviceContext": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingServiceContextIn"]
            ).optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "importPayload": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingImportErrorContextIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingErrorLogIn"])
    types["GoogleCloudDiscoveryengineLoggingErrorLogOut"] = t.struct(
        {
            "responsePayload": t.struct({"_": t.string().optional()}).optional(),
            "context": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingErrorContextOut"]
            ).optional(),
            "requestPayload": t.struct({"_": t.string().optional()}).optional(),
            "message": t.string().optional(),
            "serviceContext": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingServiceContextOut"]
            ).optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "importPayload": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingImportErrorContextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingErrorLogOut"])
    types["GoogleCloudDiscoveryengineV1betaSchemaIn"] = t.struct(
        {
            "name": t.string().optional(),
            "jsonSchema": t.string().optional(),
            "structSchema": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaSchemaIn"])
    types["GoogleCloudDiscoveryengineV1betaSchemaOut"] = t.struct(
        {
            "name": t.string().optional(),
            "jsonSchema": t.string().optional(),
            "structSchema": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaSchemaOut"])
    types["GoogleCloudDiscoveryengineV1betaSearchInfoIn"] = t.struct(
        {
            "searchQuery": t.string().optional(),
            "offset": t.integer().optional(),
            "orderBy": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaSearchInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaSearchInfoOut"] = t.struct(
        {
            "searchQuery": t.string().optional(),
            "offset": t.integer().optional(),
            "orderBy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaSearchInfoOut"])
    types["GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataIn"] = t.struct(
        {
            "successCount": t.string().optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataOut"] = t.struct(
        {
            "successCount": t.string().optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataOut"])
    types["GoogleCloudDiscoveryengineV1betaListDocumentsResponseIn"] = t.struct(
        {
            "documents": t.array(
                t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaListDocumentsResponseIn"])
    types["GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut"] = t.struct(
        {
            "documents": t.array(
                t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut"])
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
    types["GoogleCloudDiscoveryengineV1betaMediaInfoIn"] = t.struct(
        {
            "mediaProgressPercentage": t.number().optional(),
            "mediaProgressDuration": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaMediaInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaMediaInfoOut"] = t.struct(
        {
            "mediaProgressPercentage": t.number().optional(),
            "mediaProgressDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaMediaInfoOut"])
    types["GoogleCloudDiscoveryengineLoggingHttpRequestContextIn"] = t.struct(
        {"responseStatusCode": t.integer().optional()}
    ).named(renames["GoogleCloudDiscoveryengineLoggingHttpRequestContextIn"])
    types["GoogleCloudDiscoveryengineLoggingHttpRequestContextOut"] = t.struct(
        {
            "responseStatusCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingHttpRequestContextOut"])

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
    functions[
        "projectsLocationsDataStoresBranchesDocumentsCreate"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataStoresBranchesDocumentsDelete"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataStoresBranchesDocumentsImport"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataStoresBranchesDocumentsPurge"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataStoresBranchesDocumentsPatch"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresBranchesDocumentsList"] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresBranchesDocumentsGet"] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataStoresBranchesOperationsList"
    ] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresBranchesOperationsGet"] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresOperationsList"] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresOperationsGet"] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresUserEventsWrite"] = discoveryengine.post(
        "v1beta/{parent}/userEvents:import",
        t.struct(
            {
                "parent": t.string(),
                "errorConfig": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
                ).optional(),
                "inlineSource": t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                    ]
                ),
                "bigquerySource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
                ),
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ),
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
                "errorConfig": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
                ).optional(),
                "inlineSource": t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                    ]
                ),
                "bigquerySource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
                ),
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
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
                "errorConfig": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
                ).optional(),
                "inlineSource": t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                    ]
                ),
                "bigquerySource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
                ),
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
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
    functions["projectsLocationsDataStoresModelsOperationsList"] = discoveryengine.get(
        "v1beta/{name}/operations",
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
        "projectsLocationsDataStoresServingConfigsRecommend"
    ] = discoveryengine.post(
        "v1beta/{servingConfig}:recommend",
        t.struct(
            {
                "servingConfig": t.string(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "filter": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "pageSize": t.integer().optional(),
                "userEvent": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaUserEventIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaRecommendResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsGet"
    ] = discoveryengine.post(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "documentId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "parentDocumentId": t.string().optional(),
                "id": t.string().optional(),
                "schemaId": t.string().optional(),
                "jsonData": t.string().optional(),
                "structData": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsPatch"
    ] = discoveryengine.post(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "documentId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "parentDocumentId": t.string().optional(),
                "id": t.string().optional(),
                "schemaId": t.string().optional(),
                "jsonData": t.string().optional(),
                "structData": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsPurge"
    ] = discoveryengine.post(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "documentId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "parentDocumentId": t.string().optional(),
                "id": t.string().optional(),
                "schemaId": t.string().optional(),
                "jsonData": t.string().optional(),
                "structData": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsList"
    ] = discoveryengine.post(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "documentId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "parentDocumentId": t.string().optional(),
                "id": t.string().optional(),
                "schemaId": t.string().optional(),
                "jsonData": t.string().optional(),
                "structData": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsImport"
    ] = discoveryengine.post(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "documentId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "parentDocumentId": t.string().optional(),
                "id": t.string().optional(),
                "schemaId": t.string().optional(),
                "jsonData": t.string().optional(),
                "structData": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsDelete"
    ] = discoveryengine.post(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "documentId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "parentDocumentId": t.string().optional(),
                "id": t.string().optional(),
                "schemaId": t.string().optional(),
                "jsonData": t.string().optional(),
                "structData": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresBranchesDocumentsCreate"
    ] = discoveryengine.post(
        "v1beta/{parent}/documents",
        t.struct(
            {
                "documentId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "parentDocumentId": t.string().optional(),
                "id": t.string().optional(),
                "schemaId": t.string().optional(),
                "jsonData": t.string().optional(),
                "structData": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"]),
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
        "v1beta/{parent}/userEvents:write",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "searchInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaSearchInfoIn"]
                ).optional(),
                "eventTime": t.string().optional(),
                "mediaInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaMediaInfoIn"]
                ).optional(),
                "panel": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaPanelInfoIn"]
                ).optional(),
                "transactionInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaTransactionInfoIn"]
                ).optional(),
                "documents": t.array(
                    t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoIn"])
                ).optional(),
                "tagIds": t.array(t.string()).optional(),
                "promotionIds": t.array(t.string()).optional(),
                "completionInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaCompletionInfoIn"]
                ).optional(),
                "sessionId": t.string().optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaUserInfoIn"]
                ).optional(),
                "userPseudoId": t.string(),
                "attributionToken": t.string().optional(),
                "directUserRequest": t.boolean().optional(),
                "pageInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaPageInfoIn"]
                ).optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "eventType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaUserEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresUserEventsImport"
    ] = discoveryengine.post(
        "v1beta/{parent}/userEvents:write",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "searchInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaSearchInfoIn"]
                ).optional(),
                "eventTime": t.string().optional(),
                "mediaInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaMediaInfoIn"]
                ).optional(),
                "panel": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaPanelInfoIn"]
                ).optional(),
                "transactionInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaTransactionInfoIn"]
                ).optional(),
                "documents": t.array(
                    t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoIn"])
                ).optional(),
                "tagIds": t.array(t.string()).optional(),
                "promotionIds": t.array(t.string()).optional(),
                "completionInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaCompletionInfoIn"]
                ).optional(),
                "sessionId": t.string().optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaUserInfoIn"]
                ).optional(),
                "userPseudoId": t.string(),
                "attributionToken": t.string().optional(),
                "directUserRequest": t.boolean().optional(),
                "pageInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaPageInfoIn"]
                ).optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "eventType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaUserEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresUserEventsWrite"
    ] = discoveryengine.post(
        "v1beta/{parent}/userEvents:write",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "searchInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaSearchInfoIn"]
                ).optional(),
                "eventTime": t.string().optional(),
                "mediaInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaMediaInfoIn"]
                ).optional(),
                "panel": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaPanelInfoIn"]
                ).optional(),
                "transactionInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaTransactionInfoIn"]
                ).optional(),
                "documents": t.array(
                    t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoIn"])
                ).optional(),
                "tagIds": t.array(t.string()).optional(),
                "promotionIds": t.array(t.string()).optional(),
                "completionInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaCompletionInfoIn"]
                ).optional(),
                "sessionId": t.string().optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaUserInfoIn"]
                ).optional(),
                "userPseudoId": t.string(),
                "attributionToken": t.string().optional(),
                "directUserRequest": t.boolean().optional(),
                "pageInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaPageInfoIn"]
                ).optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "eventType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaUserEventOut"]),
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
                "filter": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "pageSize": t.integer().optional(),
                "userEvent": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaUserEventIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaRecommendResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCollectionsDataStoresModelsOperationsGet"
    ] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
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
        "v1beta/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
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
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCollectionsEnginesOperationsGet"] = discoveryengine.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
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
    functions["projectsOperationsGet"] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsList"] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="discoveryengine", renames=renames, types=types, functions=functions
    )
