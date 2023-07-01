from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_discoveryengine():
    discoveryengine = HTTPRuntime("https://discoveryengine.googleapis.com/")

    renames = {
        "ErrorResponse": "_discoveryengine_1_ErrorResponse",
        "GoogleCloudDiscoveryengineV1betaPanelInfoIn": "_discoveryengine_2_GoogleCloudDiscoveryengineV1betaPanelInfoIn",
        "GoogleCloudDiscoveryengineV1betaPanelInfoOut": "_discoveryengine_3_GoogleCloudDiscoveryengineV1betaPanelInfoOut",
        "GoogleCloudDiscoveryengineV1alphaPurgeUserEventsResponseIn": "_discoveryengine_4_GoogleCloudDiscoveryengineV1alphaPurgeUserEventsResponseIn",
        "GoogleCloudDiscoveryengineV1alphaPurgeUserEventsResponseOut": "_discoveryengine_5_GoogleCloudDiscoveryengineV1alphaPurgeUserEventsResponseOut",
        "GoogleCloudDiscoveryengineV1betaUserEventIn": "_discoveryengine_6_GoogleCloudDiscoveryengineV1betaUserEventIn",
        "GoogleCloudDiscoveryengineV1betaUserEventOut": "_discoveryengine_7_GoogleCloudDiscoveryengineV1betaUserEventOut",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestIn": "_discoveryengine_8_GoogleCloudDiscoveryengineV1betaImportUserEventsRequestIn",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestOut": "_discoveryengine_9_GoogleCloudDiscoveryengineV1betaImportUserEventsRequestOut",
        "GoogleCloudDiscoveryengineV1alphaTargetSiteIn": "_discoveryengine_10_GoogleCloudDiscoveryengineV1alphaTargetSiteIn",
        "GoogleCloudDiscoveryengineV1alphaTargetSiteOut": "_discoveryengine_11_GoogleCloudDiscoveryengineV1alphaTargetSiteOut",
        "GoogleCloudDiscoveryengineV1ImportErrorConfigIn": "_discoveryengine_12_GoogleCloudDiscoveryengineV1ImportErrorConfigIn",
        "GoogleCloudDiscoveryengineV1ImportErrorConfigOut": "_discoveryengine_13_GoogleCloudDiscoveryengineV1ImportErrorConfigOut",
        "GoogleCloudDiscoveryengineV1betaUserInfoIn": "_discoveryengine_14_GoogleCloudDiscoveryengineV1betaUserInfoIn",
        "GoogleCloudDiscoveryengineV1betaUserInfoOut": "_discoveryengine_15_GoogleCloudDiscoveryengineV1betaUserInfoOut",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataIn": "_discoveryengine_16_GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataIn",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataOut": "_discoveryengine_17_GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataOut",
        "GoogleCloudDiscoveryengineV1ImportUserEventsMetadataIn": "_discoveryengine_18_GoogleCloudDiscoveryengineV1ImportUserEventsMetadataIn",
        "GoogleCloudDiscoveryengineV1ImportUserEventsMetadataOut": "_discoveryengine_19_GoogleCloudDiscoveryengineV1ImportUserEventsMetadataOut",
        "GoogleCloudDiscoveryengineV1SchemaIn": "_discoveryengine_20_GoogleCloudDiscoveryengineV1SchemaIn",
        "GoogleCloudDiscoveryengineV1SchemaOut": "_discoveryengine_21_GoogleCloudDiscoveryengineV1SchemaOut",
        "GoogleCloudDiscoveryengineV1betaSchemaIn": "_discoveryengine_22_GoogleCloudDiscoveryengineV1betaSchemaIn",
        "GoogleCloudDiscoveryengineV1betaSchemaOut": "_discoveryengine_23_GoogleCloudDiscoveryengineV1betaSchemaOut",
        "GoogleCloudDiscoveryengineV1ImportUserEventsResponseIn": "_discoveryengine_24_GoogleCloudDiscoveryengineV1ImportUserEventsResponseIn",
        "GoogleCloudDiscoveryengineV1ImportUserEventsResponseOut": "_discoveryengine_25_GoogleCloudDiscoveryengineV1ImportUserEventsResponseOut",
        "GoogleCloudDiscoveryengineV1betaDocumentInfoIn": "_discoveryengine_26_GoogleCloudDiscoveryengineV1betaDocumentInfoIn",
        "GoogleCloudDiscoveryengineV1betaDocumentInfoOut": "_discoveryengine_27_GoogleCloudDiscoveryengineV1betaDocumentInfoOut",
        "GoogleCloudDiscoveryengineV1betaImportErrorConfigIn": "_discoveryengine_28_GoogleCloudDiscoveryengineV1betaImportErrorConfigIn",
        "GoogleCloudDiscoveryengineV1betaImportErrorConfigOut": "_discoveryengine_29_GoogleCloudDiscoveryengineV1betaImportErrorConfigOut",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseIn": "_discoveryengine_30_GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseOut": "_discoveryengine_31_GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1betaListDocumentsResponseIn": "_discoveryengine_32_GoogleCloudDiscoveryengineV1betaListDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut": "_discoveryengine_33_GoogleCloudDiscoveryengineV1betaListDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn": "_discoveryengine_34_GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn",
        "GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut": "_discoveryengine_35_GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut",
        "GoogleCloudDiscoveryengineV1betaTransactionInfoIn": "_discoveryengine_36_GoogleCloudDiscoveryengineV1betaTransactionInfoIn",
        "GoogleCloudDiscoveryengineV1betaTransactionInfoOut": "_discoveryengine_37_GoogleCloudDiscoveryengineV1betaTransactionInfoOut",
        "GoogleCloudDiscoveryengineV1betaBigQuerySourceIn": "_discoveryengine_38_GoogleCloudDiscoveryengineV1betaBigQuerySourceIn",
        "GoogleCloudDiscoveryengineV1betaBigQuerySourceOut": "_discoveryengine_39_GoogleCloudDiscoveryengineV1betaBigQuerySourceOut",
        "GoogleCloudDiscoveryengineV1ImportDocumentsResponseIn": "_discoveryengine_40_GoogleCloudDiscoveryengineV1ImportDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1ImportDocumentsResponseOut": "_discoveryengine_41_GoogleCloudDiscoveryengineV1ImportDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseIn": "_discoveryengine_42_GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseIn",
        "GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseOut": "_discoveryengine_43_GoogleCloudDiscoveryengineV1alphaImportUserEventsResponseOut",
        "GoogleCloudDiscoveryengineLoggingHttpRequestContextIn": "_discoveryengine_44_GoogleCloudDiscoveryengineLoggingHttpRequestContextIn",
        "GoogleCloudDiscoveryengineLoggingHttpRequestContextOut": "_discoveryengine_45_GoogleCloudDiscoveryengineLoggingHttpRequestContextOut",
        "GoogleTypeDateIn": "_discoveryengine_46_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_discoveryengine_47_GoogleTypeDateOut",
        "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultIn": "_discoveryengine_48_GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultIn",
        "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultOut": "_discoveryengine_49_GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultOut",
        "GoogleCloudDiscoveryengineV1betaPageInfoIn": "_discoveryengine_50_GoogleCloudDiscoveryengineV1betaPageInfoIn",
        "GoogleCloudDiscoveryengineV1betaPageInfoOut": "_discoveryengine_51_GoogleCloudDiscoveryengineV1betaPageInfoOut",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestIn": "_discoveryengine_52_GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestIn",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestOut": "_discoveryengine_53_GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequestOut",
        "GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseIn": "_discoveryengine_54_GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseOut": "_discoveryengine_55_GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseOut",
        "GoogleCloudDiscoveryengineLoggingServiceContextIn": "_discoveryengine_56_GoogleCloudDiscoveryengineLoggingServiceContextIn",
        "GoogleCloudDiscoveryengineLoggingServiceContextOut": "_discoveryengine_57_GoogleCloudDiscoveryengineLoggingServiceContextOut",
        "GoogleCloudDiscoveryengineV1betaCustomAttributeIn": "_discoveryengine_58_GoogleCloudDiscoveryengineV1betaCustomAttributeIn",
        "GoogleCloudDiscoveryengineV1betaCustomAttributeOut": "_discoveryengine_59_GoogleCloudDiscoveryengineV1betaCustomAttributeOut",
        "GoogleCloudDiscoveryengineV1alphaPurgeUserEventsMetadataIn": "_discoveryengine_60_GoogleCloudDiscoveryengineV1alphaPurgeUserEventsMetadataIn",
        "GoogleCloudDiscoveryengineV1alphaPurgeUserEventsMetadataOut": "_discoveryengine_61_GoogleCloudDiscoveryengineV1alphaPurgeUserEventsMetadataOut",
        "GoogleCloudDiscoveryengineV1alphaSchemaIn": "_discoveryengine_62_GoogleCloudDiscoveryengineV1alphaSchemaIn",
        "GoogleCloudDiscoveryengineV1alphaSchemaOut": "_discoveryengine_63_GoogleCloudDiscoveryengineV1alphaSchemaOut",
        "GoogleCloudDiscoveryengineV1betaRecommendRequestIn": "_discoveryengine_64_GoogleCloudDiscoveryengineV1betaRecommendRequestIn",
        "GoogleCloudDiscoveryengineV1betaRecommendRequestOut": "_discoveryengine_65_GoogleCloudDiscoveryengineV1betaRecommendRequestOut",
        "GoogleCloudDiscoveryengineLoggingErrorLogIn": "_discoveryengine_66_GoogleCloudDiscoveryengineLoggingErrorLogIn",
        "GoogleCloudDiscoveryengineLoggingErrorLogOut": "_discoveryengine_67_GoogleCloudDiscoveryengineLoggingErrorLogOut",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsResponseIn": "_discoveryengine_68_GoogleCloudDiscoveryengineV1betaImportUserEventsResponseIn",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsResponseOut": "_discoveryengine_69_GoogleCloudDiscoveryengineV1betaImportUserEventsResponseOut",
        "GoogleCloudDiscoveryengineV1betaDocumentIn": "_discoveryengine_70_GoogleCloudDiscoveryengineV1betaDocumentIn",
        "GoogleCloudDiscoveryengineV1betaDocumentOut": "_discoveryengine_71_GoogleCloudDiscoveryengineV1betaDocumentOut",
        "GoogleRpcStatusIn": "_discoveryengine_72_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_discoveryengine_73_GoogleRpcStatusOut",
        "GoogleCloudDiscoveryengineV1PurgeDocumentsMetadataIn": "_discoveryengine_74_GoogleCloudDiscoveryengineV1PurgeDocumentsMetadataIn",
        "GoogleCloudDiscoveryengineV1PurgeDocumentsMetadataOut": "_discoveryengine_75_GoogleCloudDiscoveryengineV1PurgeDocumentsMetadataOut",
        "GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataIn": "_discoveryengine_76_GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataIn",
        "GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataOut": "_discoveryengine_77_GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataOut",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataIn": "_discoveryengine_78_GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataIn",
        "GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataOut": "_discoveryengine_79_GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataOut",
        "GoogleCloudDiscoveryengineLoggingSourceLocationIn": "_discoveryengine_80_GoogleCloudDiscoveryengineLoggingSourceLocationIn",
        "GoogleCloudDiscoveryengineLoggingSourceLocationOut": "_discoveryengine_81_GoogleCloudDiscoveryengineLoggingSourceLocationOut",
        "GoogleLongrunningOperationIn": "_discoveryengine_82_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_discoveryengine_83_GoogleLongrunningOperationOut",
        "GoogleCloudDiscoveryengineV1betaMediaInfoIn": "_discoveryengine_84_GoogleCloudDiscoveryengineV1betaMediaInfoIn",
        "GoogleCloudDiscoveryengineV1betaMediaInfoOut": "_discoveryengine_85_GoogleCloudDiscoveryengineV1betaMediaInfoOut",
        "GoogleCloudDiscoveryengineV1PurgeDocumentsResponseIn": "_discoveryengine_86_GoogleCloudDiscoveryengineV1PurgeDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1PurgeDocumentsResponseOut": "_discoveryengine_87_GoogleCloudDiscoveryengineV1PurgeDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestIn": "_discoveryengine_88_GoogleCloudDiscoveryengineV1betaImportDocumentsRequestIn",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestOut": "_discoveryengine_89_GoogleCloudDiscoveryengineV1betaImportDocumentsRequestOut",
        "GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSitesResponseIn": "_discoveryengine_90_GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSitesResponseIn",
        "GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSitesResponseOut": "_discoveryengine_91_GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSitesResponseOut",
        "GoogleCloudDiscoveryengineV1ImportDocumentsMetadataIn": "_discoveryengine_92_GoogleCloudDiscoveryengineV1ImportDocumentsMetadataIn",
        "GoogleCloudDiscoveryengineV1ImportDocumentsMetadataOut": "_discoveryengine_93_GoogleCloudDiscoveryengineV1ImportDocumentsMetadataOut",
        "GoogleCloudDiscoveryengineV1betaGcsSourceIn": "_discoveryengine_94_GoogleCloudDiscoveryengineV1betaGcsSourceIn",
        "GoogleCloudDiscoveryengineV1betaGcsSourceOut": "_discoveryengine_95_GoogleCloudDiscoveryengineV1betaGcsSourceOut",
        "GoogleCloudDiscoveryengineV1betaCompletionInfoIn": "_discoveryengine_96_GoogleCloudDiscoveryengineV1betaCompletionInfoIn",
        "GoogleCloudDiscoveryengineV1betaCompletionInfoOut": "_discoveryengine_97_GoogleCloudDiscoveryengineV1betaCompletionInfoOut",
        "GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataIn": "_discoveryengine_98_GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataIn",
        "GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataOut": "_discoveryengine_99_GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataOut",
        "GoogleLongrunningListOperationsResponseIn": "_discoveryengine_100_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_discoveryengine_101_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsResponseIn": "_discoveryengine_102_GoogleCloudDiscoveryengineV1betaImportDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsResponseOut": "_discoveryengine_103_GoogleCloudDiscoveryengineV1betaImportDocumentsResponseOut",
        "GoogleCloudDiscoveryengineV1betaRecommendResponseIn": "_discoveryengine_104_GoogleCloudDiscoveryengineV1betaRecommendResponseIn",
        "GoogleCloudDiscoveryengineV1betaRecommendResponseOut": "_discoveryengine_105_GoogleCloudDiscoveryengineV1betaRecommendResponseOut",
        "GoogleCloudDiscoveryengineLoggingErrorContextIn": "_discoveryengine_106_GoogleCloudDiscoveryengineLoggingErrorContextIn",
        "GoogleCloudDiscoveryengineLoggingErrorContextOut": "_discoveryengine_107_GoogleCloudDiscoveryengineLoggingErrorContextOut",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceIn": "_discoveryengine_108_GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceIn",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceOut": "_discoveryengine_109_GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSourceOut",
        "GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataIn": "_discoveryengine_110_GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataIn",
        "GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataOut": "_discoveryengine_111_GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataOut",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn": "_discoveryengine_112_GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn",
        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceOut": "_discoveryengine_113_GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceOut",
        "GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseIn": "_discoveryengine_114_GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseIn",
        "GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseOut": "_discoveryengine_115_GoogleCloudDiscoveryengineV1alphaImportDocumentsResponseOut",
        "GoogleProtobufEmptyIn": "_discoveryengine_116_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_discoveryengine_117_GoogleProtobufEmptyOut",
        "GoogleCloudDiscoveryengineV1betaSearchInfoIn": "_discoveryengine_118_GoogleCloudDiscoveryengineV1betaSearchInfoIn",
        "GoogleCloudDiscoveryengineV1betaSearchInfoOut": "_discoveryengine_119_GoogleCloudDiscoveryengineV1betaSearchInfoOut",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataIn": "_discoveryengine_120_GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataIn",
        "GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataOut": "_discoveryengine_121_GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataOut",
        "GoogleCloudDiscoveryengineLoggingImportErrorContextIn": "_discoveryengine_122_GoogleCloudDiscoveryengineLoggingImportErrorContextIn",
        "GoogleCloudDiscoveryengineLoggingImportErrorContextOut": "_discoveryengine_123_GoogleCloudDiscoveryengineLoggingImportErrorContextOut",
        "GoogleApiHttpBodyIn": "_discoveryengine_124_GoogleApiHttpBodyIn",
        "GoogleApiHttpBodyOut": "_discoveryengine_125_GoogleApiHttpBodyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudDiscoveryengineV1betaPanelInfoIn"] = t.struct(
        {
            "totalPanels": t.integer().optional(),
            "panelPosition": t.integer().optional(),
            "displayName": t.string().optional(),
            "panelId": t.string(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPanelInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaPanelInfoOut"] = t.struct(
        {
            "totalPanels": t.integer().optional(),
            "panelPosition": t.integer().optional(),
            "displayName": t.string().optional(),
            "panelId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPanelInfoOut"])
    types["GoogleCloudDiscoveryengineV1alphaPurgeUserEventsResponseIn"] = t.struct(
        {"purgeCount": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineV1alphaPurgeUserEventsResponseIn"])
    types["GoogleCloudDiscoveryengineV1alphaPurgeUserEventsResponseOut"] = t.struct(
        {
            "purgeCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaPurgeUserEventsResponseOut"])
    types["GoogleCloudDiscoveryengineV1betaUserEventIn"] = t.struct(
        {
            "pageInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaPageInfoIn"]
            ).optional(),
            "promotionIds": t.array(t.string()).optional(),
            "completionInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaCompletionInfoIn"]
            ).optional(),
            "filter": t.string().optional(),
            "tagIds": t.array(t.string()).optional(),
            "panel": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaPanelInfoIn"]
            ).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "searchInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaSearchInfoIn"]
            ).optional(),
            "userPseudoId": t.string(),
            "documents": t.array(
                t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoIn"])
            ).optional(),
            "eventType": t.string(),
            "attributionToken": t.string().optional(),
            "mediaInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaMediaInfoIn"]
            ).optional(),
            "sessionId": t.string().optional(),
            "userInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaUserInfoIn"]
            ).optional(),
            "eventTime": t.string().optional(),
            "transactionInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaTransactionInfoIn"]
            ).optional(),
            "directUserRequest": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaUserEventIn"])
    types["GoogleCloudDiscoveryengineV1betaUserEventOut"] = t.struct(
        {
            "pageInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaPageInfoOut"]
            ).optional(),
            "promotionIds": t.array(t.string()).optional(),
            "completionInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaCompletionInfoOut"]
            ).optional(),
            "filter": t.string().optional(),
            "tagIds": t.array(t.string()).optional(),
            "panel": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaPanelInfoOut"]
            ).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "searchInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaSearchInfoOut"]
            ).optional(),
            "userPseudoId": t.string(),
            "documents": t.array(
                t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoOut"])
            ).optional(),
            "eventType": t.string(),
            "attributionToken": t.string().optional(),
            "mediaInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaMediaInfoOut"]
            ).optional(),
            "sessionId": t.string().optional(),
            "userInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaUserInfoOut"]
            ).optional(),
            "eventTime": t.string().optional(),
            "transactionInfo": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaTransactionInfoOut"]
            ).optional(),
            "directUserRequest": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaUserEventOut"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsRequestIn"] = t.struct(
        {
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
            ).optional(),
            "inlineSource": t.proxy(
                renames[
                    "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                ]
            ).optional(),
            "bigquerySource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
            ).optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
            ).optional(),
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
            ).optional(),
            "bigquerySource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceOut"]
            ).optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaGcsSourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsRequestOut"])
    types["GoogleCloudDiscoveryengineV1alphaTargetSiteIn"] = t.struct(
        {
            "providedUriPattern": t.string(),
            "exactMatch": t.boolean().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaTargetSiteIn"])
    types["GoogleCloudDiscoveryengineV1alphaTargetSiteOut"] = t.struct(
        {
            "providedUriPattern": t.string(),
            "exactMatch": t.boolean().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "generatedUriPattern": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaTargetSiteOut"])
    types["GoogleCloudDiscoveryengineV1ImportErrorConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineV1ImportErrorConfigIn"])
    types["GoogleCloudDiscoveryengineV1ImportErrorConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1ImportErrorConfigOut"])
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
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsMetadataOut"])
    types["GoogleCloudDiscoveryengineV1ImportUserEventsMetadataIn"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1ImportUserEventsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1ImportUserEventsMetadataOut"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1ImportUserEventsMetadataOut"])
    types["GoogleCloudDiscoveryengineV1SchemaIn"] = t.struct(
        {
            "jsonSchema": t.string().optional(),
            "name": t.string().optional(),
            "structSchema": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1SchemaIn"])
    types["GoogleCloudDiscoveryengineV1SchemaOut"] = t.struct(
        {
            "jsonSchema": t.string().optional(),
            "name": t.string().optional(),
            "structSchema": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1SchemaOut"])
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
    types["GoogleCloudDiscoveryengineV1ImportUserEventsResponseIn"] = t.struct(
        {
            "joinedEventsCount": t.string().optional(),
            "unjoinedEventsCount": t.string().optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1ImportErrorConfigIn"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1ImportUserEventsResponseIn"])
    types["GoogleCloudDiscoveryengineV1ImportUserEventsResponseOut"] = t.struct(
        {
            "joinedEventsCount": t.string().optional(),
            "unjoinedEventsCount": t.string().optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1ImportErrorConfigOut"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1ImportUserEventsResponseOut"])
    types["GoogleCloudDiscoveryengineV1betaDocumentInfoIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "quantity": t.integer().optional(),
            "promotionIds": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaDocumentInfoOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "quantity": t.integer().optional(),
            "promotionIds": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoOut"])
    types["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"])
    types["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"])
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
    types["GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportErrorConfigIn"])
    types["GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportErrorConfigOut"])
    types["GoogleCloudDiscoveryengineV1betaTransactionInfoIn"] = t.struct(
        {
            "value": t.number(),
            "currency": t.string(),
            "discountValue": t.number().optional(),
            "cost": t.number().optional(),
            "tax": t.number().optional(),
            "transactionId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaTransactionInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaTransactionInfoOut"] = t.struct(
        {
            "value": t.number(),
            "currency": t.string(),
            "discountValue": t.number().optional(),
            "cost": t.number().optional(),
            "tax": t.number().optional(),
            "transactionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaTransactionInfoOut"])
    types["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"] = t.struct(
        {
            "dataSchema": t.string().optional(),
            "partitionDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "datasetId": t.string(),
            "gcsStagingDir": t.string().optional(),
            "tableId": t.string(),
            "projectId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"])
    types["GoogleCloudDiscoveryengineV1betaBigQuerySourceOut"] = t.struct(
        {
            "dataSchema": t.string().optional(),
            "partitionDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "datasetId": t.string(),
            "gcsStagingDir": t.string().optional(),
            "tableId": t.string(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceOut"])
    types["GoogleCloudDiscoveryengineV1ImportDocumentsResponseIn"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1ImportErrorConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1ImportDocumentsResponseIn"])
    types["GoogleCloudDiscoveryengineV1ImportDocumentsResponseOut"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1ImportErrorConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1ImportDocumentsResponseOut"])
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
    types["GoogleCloudDiscoveryengineLoggingHttpRequestContextIn"] = t.struct(
        {"responseStatusCode": t.integer().optional()}
    ).named(renames["GoogleCloudDiscoveryengineLoggingHttpRequestContextIn"])
    types["GoogleCloudDiscoveryengineLoggingHttpRequestContextOut"] = t.struct(
        {
            "responseStatusCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingHttpRequestContextOut"])
    types["GoogleTypeDateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])
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
    types["GoogleCloudDiscoveryengineV1betaPageInfoIn"] = t.struct(
        {
            "pageviewId": t.string().optional(),
            "referrerUri": t.string().optional(),
            "uri": t.string().optional(),
            "pageCategory": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPageInfoIn"])
    types["GoogleCloudDiscoveryengineV1betaPageInfoOut"] = t.struct(
        {
            "pageviewId": t.string().optional(),
            "referrerUri": t.string().optional(),
            "uri": t.string().optional(),
            "pageCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPageInfoOut"])
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
    types["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseIn"] = t.struct(
        {
            "purgeSample": t.array(t.string()).optional(),
            "purgeCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseIn"])
    types["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseOut"] = t.struct(
        {
            "purgeSample": t.array(t.string()).optional(),
            "purgeCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponseOut"])
    types["GoogleCloudDiscoveryengineLoggingServiceContextIn"] = t.struct(
        {"service": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineLoggingServiceContextIn"])
    types["GoogleCloudDiscoveryengineLoggingServiceContextOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingServiceContextOut"])
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
    types["GoogleCloudDiscoveryengineV1alphaPurgeUserEventsMetadataIn"] = t.struct(
        {
            "successCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaPurgeUserEventsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1alphaPurgeUserEventsMetadataOut"] = t.struct(
        {
            "successCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaPurgeUserEventsMetadataOut"])
    types["GoogleCloudDiscoveryengineV1alphaSchemaIn"] = t.struct(
        {
            "structSchema": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "jsonSchema": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaSchemaIn"])
    types["GoogleCloudDiscoveryengineV1alphaSchemaOut"] = t.struct(
        {
            "structSchema": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "jsonSchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaSchemaOut"])
    types["GoogleCloudDiscoveryengineV1betaRecommendRequestIn"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "filter": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "userEvent": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaUserEventIn"]
            ),
            "pageSize": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaRecommendRequestIn"])
    types["GoogleCloudDiscoveryengineV1betaRecommendRequestOut"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "filter": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "userEvent": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaUserEventOut"]
            ),
            "pageSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaRecommendRequestOut"])
    types["GoogleCloudDiscoveryengineLoggingErrorLogIn"] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "context": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingErrorContextIn"]
            ).optional(),
            "message": t.string().optional(),
            "serviceContext": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingServiceContextIn"]
            ).optional(),
            "responsePayload": t.struct({"_": t.string().optional()}).optional(),
            "importPayload": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingImportErrorContextIn"]
            ).optional(),
            "requestPayload": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingErrorLogIn"])
    types["GoogleCloudDiscoveryengineLoggingErrorLogOut"] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "context": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingErrorContextOut"]
            ).optional(),
            "message": t.string().optional(),
            "serviceContext": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingServiceContextOut"]
            ).optional(),
            "responsePayload": t.struct({"_": t.string().optional()}).optional(),
            "importPayload": t.proxy(
                renames["GoogleCloudDiscoveryengineLoggingImportErrorContextOut"]
            ).optional(),
            "requestPayload": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingErrorLogOut"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsResponseIn"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "joinedEventsCount": t.string().optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigIn"]
            ).optional(),
            "unjoinedEventsCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsResponseIn"])
    types["GoogleCloudDiscoveryengineV1betaImportUserEventsResponseOut"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "joinedEventsCount": t.string().optional(),
            "errorConfig": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaImportErrorConfigOut"]
            ).optional(),
            "unjoinedEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportUserEventsResponseOut"])
    types["GoogleCloudDiscoveryengineV1betaDocumentIn"] = t.struct(
        {
            "parentDocumentId": t.string().optional(),
            "id": t.string().optional(),
            "jsonData": t.string().optional(),
            "schemaId": t.string().optional(),
            "name": t.string().optional(),
            "structData": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaDocumentIn"])
    types["GoogleCloudDiscoveryengineV1betaDocumentOut"] = t.struct(
        {
            "parentDocumentId": t.string().optional(),
            "id": t.string().optional(),
            "jsonData": t.string().optional(),
            "schemaId": t.string().optional(),
            "name": t.string().optional(),
            "structData": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaDocumentOut"])
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
    types["GoogleCloudDiscoveryengineV1PurgeDocumentsMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "successCount": t.string().optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1PurgeDocumentsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1PurgeDocumentsMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "successCount": t.string().optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1PurgeDocumentsMetadataOut"])
    types["GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "successCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "successCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadataOut"])
    types["GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadataOut"])
    types["GoogleCloudDiscoveryengineLoggingSourceLocationIn"] = t.struct(
        {"functionName": t.string().optional()}
    ).named(renames["GoogleCloudDiscoveryengineLoggingSourceLocationIn"])
    types["GoogleCloudDiscoveryengineLoggingSourceLocationOut"] = t.struct(
        {
            "functionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingSourceLocationOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
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
    types["GoogleCloudDiscoveryengineV1PurgeDocumentsResponseIn"] = t.struct(
        {
            "purgeSample": t.array(t.string()).optional(),
            "purgeCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1PurgeDocumentsResponseIn"])
    types["GoogleCloudDiscoveryengineV1PurgeDocumentsResponseOut"] = t.struct(
        {
            "purgeSample": t.array(t.string()).optional(),
            "purgeCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1PurgeDocumentsResponseOut"])
    types["GoogleCloudDiscoveryengineV1betaImportDocumentsRequestIn"] = t.struct(
        {
            "autoGenerateIds": t.boolean().optional(),
            "idField": t.string().optional(),
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
            "gcsSource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
            ).optional(),
            "reconciliationMode": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportDocumentsRequestIn"])
    types["GoogleCloudDiscoveryengineV1betaImportDocumentsRequestOut"] = t.struct(
        {
            "autoGenerateIds": t.boolean().optional(),
            "idField": t.string().optional(),
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
            "gcsSource": t.proxy(
                renames["GoogleCloudDiscoveryengineV1betaGcsSourceOut"]
            ).optional(),
            "reconciliationMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportDocumentsRequestOut"])
    types[
        "GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSitesResponseIn"
    ] = t.struct(
        {
            "targetSites": t.array(
                t.proxy(renames["GoogleCloudDiscoveryengineV1alphaTargetSiteIn"])
            ).optional()
        }
    ).named(
        renames["GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSitesResponseIn"]
    )
    types[
        "GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSitesResponseOut"
    ] = t.struct(
        {
            "targetSites": t.array(
                t.proxy(renames["GoogleCloudDiscoveryengineV1alphaTargetSiteOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSitesResponseOut"]
    )
    types["GoogleCloudDiscoveryengineV1ImportDocumentsMetadataIn"] = t.struct(
        {
            "successCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1ImportDocumentsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1ImportDocumentsMetadataOut"] = t.struct(
        {
            "successCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1ImportDocumentsMetadataOut"])
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
    types["GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadataOut"])
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
    types["GoogleCloudDiscoveryengineV1betaRecommendResponseIn"] = t.struct(
        {
            "results": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResultIn"
                    ]
                )
            ).optional(),
            "missingIds": t.array(t.string()).optional(),
            "validateOnly": t.boolean().optional(),
            "attributionToken": t.string().optional(),
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
            "missingIds": t.array(t.string()).optional(),
            "validateOnly": t.boolean().optional(),
            "attributionToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaRecommendResponseOut"])
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
    types["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataIn"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "successCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataOut"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "successCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadataOut"])
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
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
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
    types["GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataIn"] = t.struct(
        {
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataIn"])
    types["GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataOut"] = t.struct(
        {
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineV1betaImportDocumentsMetadataOut"])
    types["GoogleCloudDiscoveryengineLoggingImportErrorContextIn"] = t.struct(
        {
            "operation": t.string().optional(),
            "document": t.string().optional(),
            "gcsPath": t.string().optional(),
            "lineNumber": t.string().optional(),
            "userEvent": t.string().optional(),
        }
    ).named(renames["GoogleCloudDiscoveryengineLoggingImportErrorContextIn"])
    types["GoogleCloudDiscoveryengineLoggingImportErrorContextOut"] = t.struct(
        {
            "operation": t.string().optional(),
            "document": t.string().optional(),
            "gcsPath": t.string().optional(),
            "lineNumber": t.string().optional(),
            "userEvent": t.string().optional(),
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
                "userEvent": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaUserEventIn"]
                ),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaRecommendResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresBranchesDocumentsGet"] = discoveryengine.post(
        "v1beta/{parent}/documents:import",
        t.struct(
            {
                "parent": t.string(),
                "autoGenerateIds": t.boolean().optional(),
                "idField": t.string().optional(),
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
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ).optional(),
                "reconciliationMode": t.string().optional(),
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
        "v1beta/{parent}/documents:import",
        t.struct(
            {
                "parent": t.string(),
                "autoGenerateIds": t.boolean().optional(),
                "idField": t.string().optional(),
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
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ).optional(),
                "reconciliationMode": t.string().optional(),
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
        "v1beta/{parent}/documents:import",
        t.struct(
            {
                "parent": t.string(),
                "autoGenerateIds": t.boolean().optional(),
                "idField": t.string().optional(),
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
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ).optional(),
                "reconciliationMode": t.string().optional(),
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
        "v1beta/{parent}/documents:import",
        t.struct(
            {
                "parent": t.string(),
                "autoGenerateIds": t.boolean().optional(),
                "idField": t.string().optional(),
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
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ).optional(),
                "reconciliationMode": t.string().optional(),
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
        "v1beta/{parent}/documents:import",
        t.struct(
            {
                "parent": t.string(),
                "autoGenerateIds": t.boolean().optional(),
                "idField": t.string().optional(),
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
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ).optional(),
                "reconciliationMode": t.string().optional(),
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
        "v1beta/{parent}/documents:import",
        t.struct(
            {
                "parent": t.string(),
                "autoGenerateIds": t.boolean().optional(),
                "idField": t.string().optional(),
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
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ).optional(),
                "reconciliationMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataStoresBranchesDocumentsImport"
    ] = discoveryengine.post(
        "v1beta/{parent}/documents:import",
        t.struct(
            {
                "parent": t.string(),
                "autoGenerateIds": t.boolean().optional(),
                "idField": t.string().optional(),
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
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ).optional(),
                "reconciliationMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
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
    functions["projectsLocationsDataStoresUserEventsImport"] = discoveryengine.post(
        "v1beta/{parent}/userEvents:write",
        t.struct(
            {
                "parent": t.string(),
                "pageInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaPageInfoIn"]
                ).optional(),
                "promotionIds": t.array(t.string()).optional(),
                "completionInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaCompletionInfoIn"]
                ).optional(),
                "filter": t.string().optional(),
                "tagIds": t.array(t.string()).optional(),
                "panel": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaPanelInfoIn"]
                ).optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "searchInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaSearchInfoIn"]
                ).optional(),
                "userPseudoId": t.string(),
                "documents": t.array(
                    t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoIn"])
                ).optional(),
                "eventType": t.string(),
                "attributionToken": t.string().optional(),
                "mediaInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaMediaInfoIn"]
                ).optional(),
                "sessionId": t.string().optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaUserInfoIn"]
                ).optional(),
                "eventTime": t.string().optional(),
                "transactionInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaTransactionInfoIn"]
                ).optional(),
                "directUserRequest": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaUserEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresUserEventsCollect"] = discoveryengine.post(
        "v1beta/{parent}/userEvents:write",
        t.struct(
            {
                "parent": t.string(),
                "pageInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaPageInfoIn"]
                ).optional(),
                "promotionIds": t.array(t.string()).optional(),
                "completionInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaCompletionInfoIn"]
                ).optional(),
                "filter": t.string().optional(),
                "tagIds": t.array(t.string()).optional(),
                "panel": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaPanelInfoIn"]
                ).optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "searchInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaSearchInfoIn"]
                ).optional(),
                "userPseudoId": t.string(),
                "documents": t.array(
                    t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoIn"])
                ).optional(),
                "eventType": t.string(),
                "attributionToken": t.string().optional(),
                "mediaInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaMediaInfoIn"]
                ).optional(),
                "sessionId": t.string().optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaUserInfoIn"]
                ).optional(),
                "eventTime": t.string().optional(),
                "transactionInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaTransactionInfoIn"]
                ).optional(),
                "directUserRequest": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaUserEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataStoresUserEventsWrite"] = discoveryengine.post(
        "v1beta/{parent}/userEvents:write",
        t.struct(
            {
                "parent": t.string(),
                "pageInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaPageInfoIn"]
                ).optional(),
                "promotionIds": t.array(t.string()).optional(),
                "completionInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaCompletionInfoIn"]
                ).optional(),
                "filter": t.string().optional(),
                "tagIds": t.array(t.string()).optional(),
                "panel": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaPanelInfoIn"]
                ).optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "searchInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaSearchInfoIn"]
                ).optional(),
                "userPseudoId": t.string(),
                "documents": t.array(
                    t.proxy(renames["GoogleCloudDiscoveryengineV1betaDocumentInfoIn"])
                ).optional(),
                "eventType": t.string(),
                "attributionToken": t.string().optional(),
                "mediaInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaMediaInfoIn"]
                ).optional(),
                "sessionId": t.string().optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaUserInfoIn"]
                ).optional(),
                "eventTime": t.string().optional(),
                "transactionInfo": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaTransactionInfoIn"]
                ).optional(),
                "directUserRequest": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaUserEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCollectionsOperationsGet"] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
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
        "projectsLocationsCollectionsDataStoresBranchesDocumentsPurge"
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
        "projectsLocationsCollectionsDataStoresBranchesDocumentsList"
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
        "projectsLocationsCollectionsDataStoresBranchesDocumentsDelete"
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
        "projectsLocationsCollectionsDataStoresBranchesOperationsList"
    ] = discoveryengine.get(
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
        "projectsLocationsCollectionsDataStoresSchemasOperationsGet"
    ] = discoveryengine.get(
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
    functions[
        "projectsLocationsCollectionsDataStoresSchemasOperationsList"
    ] = discoveryengine.get(
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
                "userEvent": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaUserEventIn"]
                ),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDiscoveryengineV1betaRecommendResponseOut"]),
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
                "inlineSource": t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                    ]
                ).optional(),
                "bigquerySource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
                ).optional(),
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ).optional(),
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
                "inlineSource": t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                    ]
                ).optional(),
                "bigquerySource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
                ).optional(),
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ).optional(),
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
                "inlineSource": t.proxy(
                    renames[
                        "GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSourceIn"
                    ]
                ).optional(),
                "bigquerySource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaBigQuerySourceIn"]
                ).optional(),
                "gcsSource": t.proxy(
                    renames["GoogleCloudDiscoveryengineV1betaGcsSourceIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsGet"] = discoveryengine.get(
        "v1beta/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
