from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_translate() -> Import:
    translate = HTTPRuntime("https://translation.googleapis.com/")

    renames = {
        "ErrorResponse": "_translate_1_ErrorResponse",
        "SupportedLanguagesIn": "_translate_2_SupportedLanguagesIn",
        "SupportedLanguagesOut": "_translate_3_SupportedLanguagesOut",
        "ListGlossaryEntriesResponseIn": "_translate_4_ListGlossaryEntriesResponseIn",
        "ListGlossaryEntriesResponseOut": "_translate_5_ListGlossaryEntriesResponseOut",
        "DocumentOutputConfigIn": "_translate_6_DocumentOutputConfigIn",
        "DocumentOutputConfigOut": "_translate_7_DocumentOutputConfigOut",
        "DocumentTranslationIn": "_translate_8_DocumentTranslationIn",
        "DocumentTranslationOut": "_translate_9_DocumentTranslationOut",
        "CancelOperationRequestIn": "_translate_10_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_translate_11_CancelOperationRequestOut",
        "LocationIn": "_translate_12_LocationIn",
        "LocationOut": "_translate_13_LocationOut",
        "GlossaryTermIn": "_translate_14_GlossaryTermIn",
        "GlossaryTermOut": "_translate_15_GlossaryTermOut",
        "ListLocationsResponseIn": "_translate_16_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_translate_17_ListLocationsResponseOut",
        "BatchTranslateTextRequestIn": "_translate_18_BatchTranslateTextRequestIn",
        "BatchTranslateTextRequestOut": "_translate_19_BatchTranslateTextRequestOut",
        "DetectedLanguageIn": "_translate_20_DetectedLanguageIn",
        "DetectedLanguageOut": "_translate_21_DetectedLanguageOut",
        "GcsInputSourceIn": "_translate_22_GcsInputSourceIn",
        "GcsInputSourceOut": "_translate_23_GcsInputSourceOut",
        "GcsSourceIn": "_translate_24_GcsSourceIn",
        "GcsSourceOut": "_translate_25_GcsSourceOut",
        "ListGlossariesResponseIn": "_translate_26_ListGlossariesResponseIn",
        "ListGlossariesResponseOut": "_translate_27_ListGlossariesResponseOut",
        "EmptyIn": "_translate_28_EmptyIn",
        "EmptyOut": "_translate_29_EmptyOut",
        "DatasetIn": "_translate_30_DatasetIn",
        "DatasetOut": "_translate_31_DatasetOut",
        "BatchTranslateDocumentRequestIn": "_translate_32_BatchTranslateDocumentRequestIn",
        "BatchTranslateDocumentRequestOut": "_translate_33_BatchTranslateDocumentRequestOut",
        "DetectLanguageRequestIn": "_translate_34_DetectLanguageRequestIn",
        "DetectLanguageRequestOut": "_translate_35_DetectLanguageRequestOut",
        "OutputConfigIn": "_translate_36_OutputConfigIn",
        "OutputConfigOut": "_translate_37_OutputConfigOut",
        "OperationIn": "_translate_38_OperationIn",
        "OperationOut": "_translate_39_OperationOut",
        "ListDatasetsResponseIn": "_translate_40_ListDatasetsResponseIn",
        "ListDatasetsResponseOut": "_translate_41_ListDatasetsResponseOut",
        "TranslateTextGlossaryConfigIn": "_translate_42_TranslateTextGlossaryConfigIn",
        "TranslateTextGlossaryConfigOut": "_translate_43_TranslateTextGlossaryConfigOut",
        "ModelIn": "_translate_44_ModelIn",
        "ModelOut": "_translate_45_ModelOut",
        "TranslationIn": "_translate_46_TranslationIn",
        "TranslationOut": "_translate_47_TranslationOut",
        "ImportDataRequestIn": "_translate_48_ImportDataRequestIn",
        "ImportDataRequestOut": "_translate_49_ImportDataRequestOut",
        "DetectLanguageResponseIn": "_translate_50_DetectLanguageResponseIn",
        "DetectLanguageResponseOut": "_translate_51_DetectLanguageResponseOut",
        "TranslateTextResponseIn": "_translate_52_TranslateTextResponseIn",
        "TranslateTextResponseOut": "_translate_53_TranslateTextResponseOut",
        "GlossaryTermsSetIn": "_translate_54_GlossaryTermsSetIn",
        "GlossaryTermsSetOut": "_translate_55_GlossaryTermsSetOut",
        "GlossaryIn": "_translate_56_GlossaryIn",
        "GlossaryOut": "_translate_57_GlossaryOut",
        "GcsDestinationIn": "_translate_58_GcsDestinationIn",
        "GcsDestinationOut": "_translate_59_GcsDestinationOut",
        "ListExamplesResponseIn": "_translate_60_ListExamplesResponseIn",
        "ListExamplesResponseOut": "_translate_61_ListExamplesResponseOut",
        "DatasetOutputConfigIn": "_translate_62_DatasetOutputConfigIn",
        "DatasetOutputConfigOut": "_translate_63_DatasetOutputConfigOut",
        "SupportedLanguageIn": "_translate_64_SupportedLanguageIn",
        "SupportedLanguageOut": "_translate_65_SupportedLanguageOut",
        "GcsOutputDestinationIn": "_translate_66_GcsOutputDestinationIn",
        "GcsOutputDestinationOut": "_translate_67_GcsOutputDestinationOut",
        "InputConfigIn": "_translate_68_InputConfigIn",
        "InputConfigOut": "_translate_69_InputConfigOut",
        "InputFileIn": "_translate_70_InputFileIn",
        "InputFileOut": "_translate_71_InputFileOut",
        "GlossaryEntryIn": "_translate_72_GlossaryEntryIn",
        "GlossaryEntryOut": "_translate_73_GlossaryEntryOut",
        "DocumentInputConfigIn": "_translate_74_DocumentInputConfigIn",
        "DocumentInputConfigOut": "_translate_75_DocumentInputConfigOut",
        "ExportDataRequestIn": "_translate_76_ExportDataRequestIn",
        "ExportDataRequestOut": "_translate_77_ExportDataRequestOut",
        "DatasetInputConfigIn": "_translate_78_DatasetInputConfigIn",
        "DatasetInputConfigOut": "_translate_79_DatasetInputConfigOut",
        "LanguageCodePairIn": "_translate_80_LanguageCodePairIn",
        "LanguageCodePairOut": "_translate_81_LanguageCodePairOut",
        "TranslateDocumentResponseIn": "_translate_82_TranslateDocumentResponseIn",
        "TranslateDocumentResponseOut": "_translate_83_TranslateDocumentResponseOut",
        "ListModelsResponseIn": "_translate_84_ListModelsResponseIn",
        "ListModelsResponseOut": "_translate_85_ListModelsResponseOut",
        "WaitOperationRequestIn": "_translate_86_WaitOperationRequestIn",
        "WaitOperationRequestOut": "_translate_87_WaitOperationRequestOut",
        "BatchDocumentOutputConfigIn": "_translate_88_BatchDocumentOutputConfigIn",
        "BatchDocumentOutputConfigOut": "_translate_89_BatchDocumentOutputConfigOut",
        "ListOperationsResponseIn": "_translate_90_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_translate_91_ListOperationsResponseOut",
        "TranslateTextRequestIn": "_translate_92_TranslateTextRequestIn",
        "TranslateTextRequestOut": "_translate_93_TranslateTextRequestOut",
        "LanguageCodesSetIn": "_translate_94_LanguageCodesSetIn",
        "LanguageCodesSetOut": "_translate_95_LanguageCodesSetOut",
        "StatusIn": "_translate_96_StatusIn",
        "StatusOut": "_translate_97_StatusOut",
        "GlossaryInputConfigIn": "_translate_98_GlossaryInputConfigIn",
        "GlossaryInputConfigOut": "_translate_99_GlossaryInputConfigOut",
        "ExampleIn": "_translate_100_ExampleIn",
        "ExampleOut": "_translate_101_ExampleOut",
        "BatchDocumentInputConfigIn": "_translate_102_BatchDocumentInputConfigIn",
        "BatchDocumentInputConfigOut": "_translate_103_BatchDocumentInputConfigOut",
        "TranslateDocumentRequestIn": "_translate_104_TranslateDocumentRequestIn",
        "TranslateDocumentRequestOut": "_translate_105_TranslateDocumentRequestOut",
        "GlossaryTermsPairIn": "_translate_106_GlossaryTermsPairIn",
        "GlossaryTermsPairOut": "_translate_107_GlossaryTermsPairOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SupportedLanguagesIn"] = t.struct(
        {"languages": t.array(t.proxy(renames["SupportedLanguageIn"])).optional()}
    ).named(renames["SupportedLanguagesIn"])
    types["SupportedLanguagesOut"] = t.struct(
        {
            "languages": t.array(t.proxy(renames["SupportedLanguageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SupportedLanguagesOut"])
    types["ListGlossaryEntriesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "glossaryEntries": t.array(t.proxy(renames["GlossaryEntryIn"])).optional(),
        }
    ).named(renames["ListGlossaryEntriesResponseIn"])
    types["ListGlossaryEntriesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "glossaryEntries": t.array(t.proxy(renames["GlossaryEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGlossaryEntriesResponseOut"])
    types["DocumentOutputConfigIn"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["DocumentOutputConfigIn"])
    types["DocumentOutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentOutputConfigOut"])
    types["DocumentTranslationIn"] = t.struct(
        {
            "detectedLanguageCode": t.string().optional(),
            "byteStreamOutputs": t.array(t.string()).optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["DocumentTranslationIn"])
    types["DocumentTranslationOut"] = t.struct(
        {
            "detectedLanguageCode": t.string().optional(),
            "byteStreamOutputs": t.array(t.string()).optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentTranslationOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["GlossaryTermIn"] = t.struct(
        {"languageCode": t.string().optional(), "text": t.string().optional()}
    ).named(renames["GlossaryTermIn"])
    types["GlossaryTermOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryTermOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["BatchTranslateTextRequestIn"] = t.struct(
        {
            "inputConfigs": t.array(t.proxy(renames["InputConfigIn"])),
            "sourceLanguageCode": t.string(),
            "models": t.struct({"_": t.string().optional()}).optional(),
            "glossaries": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "outputConfig": t.proxy(renames["OutputConfigIn"]),
            "targetLanguageCodes": t.array(t.string()),
        }
    ).named(renames["BatchTranslateTextRequestIn"])
    types["BatchTranslateTextRequestOut"] = t.struct(
        {
            "inputConfigs": t.array(t.proxy(renames["InputConfigOut"])),
            "sourceLanguageCode": t.string(),
            "models": t.struct({"_": t.string().optional()}).optional(),
            "glossaries": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "outputConfig": t.proxy(renames["OutputConfigOut"]),
            "targetLanguageCodes": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchTranslateTextRequestOut"])
    types["DetectedLanguageIn"] = t.struct(
        {"languageCode": t.string().optional(), "confidence": t.number().optional()}
    ).named(renames["DetectedLanguageIn"])
    types["DetectedLanguageOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetectedLanguageOut"])
    types["GcsInputSourceIn"] = t.struct({"inputUri": t.string()}).named(
        renames["GcsInputSourceIn"]
    )
    types["GcsInputSourceOut"] = t.struct(
        {"inputUri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GcsInputSourceOut"])
    types["GcsSourceIn"] = t.struct({"inputUri": t.string()}).named(
        renames["GcsSourceIn"]
    )
    types["GcsSourceOut"] = t.struct(
        {"inputUri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GcsSourceOut"])
    types["ListGlossariesResponseIn"] = t.struct(
        {
            "glossaries": t.array(t.proxy(renames["GlossaryIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListGlossariesResponseIn"])
    types["ListGlossariesResponseOut"] = t.struct(
        {
            "glossaries": t.array(t.proxy(renames["GlossaryOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGlossariesResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DatasetIn"] = t.struct(
        {
            "targetLanguageCode": t.string().optional(),
            "sourceLanguageCode": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DatasetIn"])
    types["DatasetOut"] = t.struct(
        {
            "testExampleCount": t.integer().optional(),
            "targetLanguageCode": t.string().optional(),
            "exampleCount": t.integer().optional(),
            "trainExampleCount": t.integer().optional(),
            "sourceLanguageCode": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "validateExampleCount": t.integer().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetOut"])
    types["BatchTranslateDocumentRequestIn"] = t.struct(
        {
            "enableShadowRemovalNativePdf": t.boolean().optional(),
            "targetLanguageCodes": t.array(t.string()),
            "sourceLanguageCode": t.string(),
            "customizedAttribution": t.string().optional(),
            "glossaries": t.struct({"_": t.string().optional()}).optional(),
            "formatConversions": t.struct({"_": t.string().optional()}).optional(),
            "outputConfig": t.proxy(renames["BatchDocumentOutputConfigIn"]),
            "inputConfigs": t.array(t.proxy(renames["BatchDocumentInputConfigIn"])),
            "models": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["BatchTranslateDocumentRequestIn"])
    types["BatchTranslateDocumentRequestOut"] = t.struct(
        {
            "enableShadowRemovalNativePdf": t.boolean().optional(),
            "targetLanguageCodes": t.array(t.string()),
            "sourceLanguageCode": t.string(),
            "customizedAttribution": t.string().optional(),
            "glossaries": t.struct({"_": t.string().optional()}).optional(),
            "formatConversions": t.struct({"_": t.string().optional()}).optional(),
            "outputConfig": t.proxy(renames["BatchDocumentOutputConfigOut"]),
            "inputConfigs": t.array(t.proxy(renames["BatchDocumentInputConfigOut"])),
            "models": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchTranslateDocumentRequestOut"])
    types["DetectLanguageRequestIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
            "model": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DetectLanguageRequestIn"])
    types["DetectLanguageRequestOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
            "model": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetectLanguageRequestOut"])
    types["OutputConfigIn"] = t.struct(
        {"gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional()}
    ).named(renames["OutputConfigIn"])
    types["OutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutputConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["ListDatasetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "datasets": t.array(t.proxy(renames["DatasetIn"])).optional(),
        }
    ).named(renames["ListDatasetsResponseIn"])
    types["ListDatasetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "datasets": t.array(t.proxy(renames["DatasetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDatasetsResponseOut"])
    types["TranslateTextGlossaryConfigIn"] = t.struct(
        {"ignoreCase": t.boolean().optional(), "glossary": t.string()}
    ).named(renames["TranslateTextGlossaryConfigIn"])
    types["TranslateTextGlossaryConfigOut"] = t.struct(
        {
            "ignoreCase": t.boolean().optional(),
            "glossary": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslateTextGlossaryConfigOut"])
    types["ModelIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "dataset": t.string().optional(),
        }
    ).named(renames["ModelIn"])
    types["ModelOut"] = t.struct(
        {
            "name": t.string().optional(),
            "testExampleCount": t.integer().optional(),
            "validateExampleCount": t.integer().optional(),
            "updateTime": t.string().optional(),
            "trainExampleCount": t.integer().optional(),
            "sourceLanguageCode": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "dataset": t.string().optional(),
            "targetLanguageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModelOut"])
    types["TranslationIn"] = t.struct(
        {
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigIn"]
            ).optional(),
            "model": t.string().optional(),
            "translatedText": t.string().optional(),
            "detectedLanguageCode": t.string().optional(),
        }
    ).named(renames["TranslationIn"])
    types["TranslationOut"] = t.struct(
        {
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigOut"]
            ).optional(),
            "model": t.string().optional(),
            "translatedText": t.string().optional(),
            "detectedLanguageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslationOut"])
    types["ImportDataRequestIn"] = t.struct(
        {"inputConfig": t.proxy(renames["DatasetInputConfigIn"])}
    ).named(renames["ImportDataRequestIn"])
    types["ImportDataRequestOut"] = t.struct(
        {
            "inputConfig": t.proxy(renames["DatasetInputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportDataRequestOut"])
    types["DetectLanguageResponseIn"] = t.struct(
        {"languages": t.array(t.proxy(renames["DetectedLanguageIn"])).optional()}
    ).named(renames["DetectLanguageResponseIn"])
    types["DetectLanguageResponseOut"] = t.struct(
        {
            "languages": t.array(t.proxy(renames["DetectedLanguageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetectLanguageResponseOut"])
    types["TranslateTextResponseIn"] = t.struct(
        {
            "glossaryTranslations": t.array(
                t.proxy(renames["TranslationIn"])
            ).optional(),
            "translations": t.array(t.proxy(renames["TranslationIn"])).optional(),
        }
    ).named(renames["TranslateTextResponseIn"])
    types["TranslateTextResponseOut"] = t.struct(
        {
            "glossaryTranslations": t.array(
                t.proxy(renames["TranslationOut"])
            ).optional(),
            "translations": t.array(t.proxy(renames["TranslationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslateTextResponseOut"])
    types["GlossaryTermsSetIn"] = t.struct(
        {"terms": t.array(t.proxy(renames["GlossaryTermIn"])).optional()}
    ).named(renames["GlossaryTermsSetIn"])
    types["GlossaryTermsSetOut"] = t.struct(
        {
            "terms": t.array(t.proxy(renames["GlossaryTermOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryTermsSetOut"])
    types["GlossaryIn"] = t.struct(
        {
            "inputConfig": t.proxy(renames["GlossaryInputConfigIn"]),
            "displayName": t.string().optional(),
            "name": t.string(),
            "languageCodesSet": t.proxy(renames["LanguageCodesSetIn"]).optional(),
            "languagePair": t.proxy(renames["LanguageCodePairIn"]).optional(),
        }
    ).named(renames["GlossaryIn"])
    types["GlossaryOut"] = t.struct(
        {
            "inputConfig": t.proxy(renames["GlossaryInputConfigOut"]),
            "displayName": t.string().optional(),
            "name": t.string(),
            "endTime": t.string().optional(),
            "languageCodesSet": t.proxy(renames["LanguageCodesSetOut"]).optional(),
            "submitTime": t.string().optional(),
            "languagePair": t.proxy(renames["LanguageCodePairOut"]).optional(),
            "entryCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryOut"])
    types["GcsDestinationIn"] = t.struct({"outputUriPrefix": t.string()}).named(
        renames["GcsDestinationIn"]
    )
    types["GcsDestinationOut"] = t.struct(
        {
            "outputUriPrefix": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsDestinationOut"])
    types["ListExamplesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "examples": t.array(t.proxy(renames["ExampleIn"])).optional(),
        }
    ).named(renames["ListExamplesResponseIn"])
    types["ListExamplesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "examples": t.array(t.proxy(renames["ExampleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListExamplesResponseOut"])
    types["DatasetOutputConfigIn"] = t.struct(
        {"gcsDestination": t.proxy(renames["GcsOutputDestinationIn"]).optional()}
    ).named(renames["DatasetOutputConfigIn"])
    types["DatasetOutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsOutputDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetOutputConfigOut"])
    types["SupportedLanguageIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "supportSource": t.boolean().optional(),
            "supportTarget": t.boolean().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["SupportedLanguageIn"])
    types["SupportedLanguageOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "supportSource": t.boolean().optional(),
            "supportTarget": t.boolean().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SupportedLanguageOut"])
    types["GcsOutputDestinationIn"] = t.struct({"outputUriPrefix": t.string()}).named(
        renames["GcsOutputDestinationIn"]
    )
    types["GcsOutputDestinationOut"] = t.struct(
        {
            "outputUriPrefix": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsOutputDestinationOut"])
    types["InputConfigIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "gcsSource": t.proxy(renames["GcsSourceIn"]),
        }
    ).named(renames["InputConfigIn"])
    types["InputConfigOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "gcsSource": t.proxy(renames["GcsSourceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputConfigOut"])
    types["InputFileIn"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsInputSourceIn"]).optional(),
            "usage": t.string().optional(),
        }
    ).named(renames["InputFileIn"])
    types["InputFileOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsInputSourceOut"]).optional(),
            "usage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputFileOut"])
    types["GlossaryEntryIn"] = t.struct(
        {
            "termsPair": t.proxy(renames["GlossaryTermsPairIn"]).optional(),
            "termsSet": t.proxy(renames["GlossaryTermsSetIn"]).optional(),
            "description": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["GlossaryEntryIn"])
    types["GlossaryEntryOut"] = t.struct(
        {
            "termsPair": t.proxy(renames["GlossaryTermsPairOut"]).optional(),
            "termsSet": t.proxy(renames["GlossaryTermsSetOut"]).optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryEntryOut"])
    types["DocumentInputConfigIn"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceIn"]).optional(),
            "content": t.string().optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["DocumentInputConfigIn"])
    types["DocumentInputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]).optional(),
            "content": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentInputConfigOut"])
    types["ExportDataRequestIn"] = t.struct(
        {"outputConfig": t.proxy(renames["DatasetOutputConfigIn"])}
    ).named(renames["ExportDataRequestIn"])
    types["ExportDataRequestOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["DatasetOutputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportDataRequestOut"])
    types["DatasetInputConfigIn"] = t.struct(
        {"inputFiles": t.array(t.proxy(renames["InputFileIn"])).optional()}
    ).named(renames["DatasetInputConfigIn"])
    types["DatasetInputConfigOut"] = t.struct(
        {
            "inputFiles": t.array(t.proxy(renames["InputFileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetInputConfigOut"])
    types["LanguageCodePairIn"] = t.struct(
        {"targetLanguageCode": t.string(), "sourceLanguageCode": t.string()}
    ).named(renames["LanguageCodePairIn"])
    types["LanguageCodePairOut"] = t.struct(
        {
            "targetLanguageCode": t.string(),
            "sourceLanguageCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageCodePairOut"])
    types["TranslateDocumentResponseIn"] = t.struct(
        {
            "glossaryDocumentTranslation": t.proxy(
                renames["DocumentTranslationIn"]
            ).optional(),
            "model": t.string().optional(),
            "documentTranslation": t.proxy(renames["DocumentTranslationIn"]).optional(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigIn"]
            ).optional(),
        }
    ).named(renames["TranslateDocumentResponseIn"])
    types["TranslateDocumentResponseOut"] = t.struct(
        {
            "glossaryDocumentTranslation": t.proxy(
                renames["DocumentTranslationOut"]
            ).optional(),
            "model": t.string().optional(),
            "documentTranslation": t.proxy(
                renames["DocumentTranslationOut"]
            ).optional(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslateDocumentResponseOut"])
    types["ListModelsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "models": t.array(t.proxy(renames["ModelIn"])).optional(),
        }
    ).named(renames["ListModelsResponseIn"])
    types["ListModelsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "models": t.array(t.proxy(renames["ModelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListModelsResponseOut"])
    types["WaitOperationRequestIn"] = t.struct(
        {"timeout": t.string().optional()}
    ).named(renames["WaitOperationRequestIn"])
    types["WaitOperationRequestOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaitOperationRequestOut"])
    types["BatchDocumentOutputConfigIn"] = t.struct(
        {"gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional()}
    ).named(renames["BatchDocumentOutputConfigIn"])
    types["BatchDocumentOutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDocumentOutputConfigOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["TranslateTextRequestIn"] = t.struct(
        {
            "model": t.string().optional(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigIn"]
            ).optional(),
            "contents": t.array(t.string()),
            "sourceLanguageCode": t.string().optional(),
            "mimeType": t.string().optional(),
            "targetLanguageCode": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["TranslateTextRequestIn"])
    types["TranslateTextRequestOut"] = t.struct(
        {
            "model": t.string().optional(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigOut"]
            ).optional(),
            "contents": t.array(t.string()),
            "sourceLanguageCode": t.string().optional(),
            "mimeType": t.string().optional(),
            "targetLanguageCode": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslateTextRequestOut"])
    types["LanguageCodesSetIn"] = t.struct(
        {"languageCodes": t.array(t.string()).optional()}
    ).named(renames["LanguageCodesSetIn"])
    types["LanguageCodesSetOut"] = t.struct(
        {
            "languageCodes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageCodesSetOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["GlossaryInputConfigIn"] = t.struct(
        {"gcsSource": t.proxy(renames["GcsSourceIn"])}
    ).named(renames["GlossaryInputConfigIn"])
    types["GlossaryInputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryInputConfigOut"])
    types["ExampleIn"] = t.struct(
        {"targetText": t.string().optional(), "sourceText": t.string().optional()}
    ).named(renames["ExampleIn"])
    types["ExampleOut"] = t.struct(
        {
            "name": t.string().optional(),
            "targetText": t.string().optional(),
            "sourceText": t.string().optional(),
            "usage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExampleOut"])
    types["BatchDocumentInputConfigIn"] = t.struct(
        {"gcsSource": t.proxy(renames["GcsSourceIn"]).optional()}
    ).named(renames["BatchDocumentInputConfigIn"])
    types["BatchDocumentInputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDocumentInputConfigOut"])
    types["TranslateDocumentRequestIn"] = t.struct(
        {
            "enableShadowRemovalNativePdf": t.boolean().optional(),
            "sourceLanguageCode": t.string().optional(),
            "documentInputConfig": t.proxy(renames["DocumentInputConfigIn"]),
            "enableRotationCorrection": t.boolean().optional(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigIn"]
            ).optional(),
            "isTranslateNativePdfOnly": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "customizedAttribution": t.string().optional(),
            "documentOutputConfig": t.proxy(
                renames["DocumentOutputConfigIn"]
            ).optional(),
            "model": t.string().optional(),
            "targetLanguageCode": t.string(),
        }
    ).named(renames["TranslateDocumentRequestIn"])
    types["TranslateDocumentRequestOut"] = t.struct(
        {
            "enableShadowRemovalNativePdf": t.boolean().optional(),
            "sourceLanguageCode": t.string().optional(),
            "documentInputConfig": t.proxy(renames["DocumentInputConfigOut"]),
            "enableRotationCorrection": t.boolean().optional(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigOut"]
            ).optional(),
            "isTranslateNativePdfOnly": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "customizedAttribution": t.string().optional(),
            "documentOutputConfig": t.proxy(
                renames["DocumentOutputConfigOut"]
            ).optional(),
            "model": t.string().optional(),
            "targetLanguageCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslateDocumentRequestOut"])
    types["GlossaryTermsPairIn"] = t.struct(
        {
            "targetTerm": t.proxy(renames["GlossaryTermIn"]).optional(),
            "sourceTerm": t.proxy(renames["GlossaryTermIn"]).optional(),
        }
    ).named(renames["GlossaryTermsPairIn"])
    types["GlossaryTermsPairOut"] = t.struct(
        {
            "targetTerm": t.proxy(renames["GlossaryTermOut"]).optional(),
            "sourceTerm": t.proxy(renames["GlossaryTermOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryTermsPairOut"])

    functions = {}
    functions["projectsTranslateText"] = translate.post(
        "v3/{parent}:detectLanguage",
        t.struct(
            {
                "parent": t.string(),
                "mimeType": t.string().optional(),
                "content": t.string().optional(),
                "model": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DetectLanguageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetSupportedLanguages"] = translate.post(
        "v3/{parent}:detectLanguage",
        t.struct(
            {
                "parent": t.string(),
                "mimeType": t.string().optional(),
                "content": t.string().optional(),
                "model": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DetectLanguageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDetectLanguage"] = translate.post(
        "v3/{parent}:detectLanguage",
        t.struct(
            {
                "parent": t.string(),
                "mimeType": t.string().optional(),
                "content": t.string().optional(),
                "model": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DetectLanguageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = translate.post(
        "v3/{parent}:batchTranslateDocument",
        t.struct(
            {
                "parent": t.string(),
                "enableShadowRemovalNativePdf": t.boolean().optional(),
                "targetLanguageCodes": t.array(t.string()),
                "sourceLanguageCode": t.string(),
                "customizedAttribution": t.string().optional(),
                "glossaries": t.struct({"_": t.string().optional()}).optional(),
                "formatConversions": t.struct({"_": t.string().optional()}).optional(),
                "outputConfig": t.proxy(renames["BatchDocumentOutputConfigIn"]),
                "inputConfigs": t.array(t.proxy(renames["BatchDocumentInputConfigIn"])),
                "models": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGetSupportedLanguages"] = translate.post(
        "v3/{parent}:batchTranslateDocument",
        t.struct(
            {
                "parent": t.string(),
                "enableShadowRemovalNativePdf": t.boolean().optional(),
                "targetLanguageCodes": t.array(t.string()),
                "sourceLanguageCode": t.string(),
                "customizedAttribution": t.string().optional(),
                "glossaries": t.struct({"_": t.string().optional()}).optional(),
                "formatConversions": t.struct({"_": t.string().optional()}).optional(),
                "outputConfig": t.proxy(renames["BatchDocumentOutputConfigIn"]),
                "inputConfigs": t.array(t.proxy(renames["BatchDocumentInputConfigIn"])),
                "models": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTranslateDocument"] = translate.post(
        "v3/{parent}:batchTranslateDocument",
        t.struct(
            {
                "parent": t.string(),
                "enableShadowRemovalNativePdf": t.boolean().optional(),
                "targetLanguageCodes": t.array(t.string()),
                "sourceLanguageCode": t.string(),
                "customizedAttribution": t.string().optional(),
                "glossaries": t.struct({"_": t.string().optional()}).optional(),
                "formatConversions": t.struct({"_": t.string().optional()}).optional(),
                "outputConfig": t.proxy(renames["BatchDocumentOutputConfigIn"]),
                "inputConfigs": t.array(t.proxy(renames["BatchDocumentInputConfigIn"])),
                "models": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBatchTranslateText"] = translate.post(
        "v3/{parent}:batchTranslateDocument",
        t.struct(
            {
                "parent": t.string(),
                "enableShadowRemovalNativePdf": t.boolean().optional(),
                "targetLanguageCodes": t.array(t.string()),
                "sourceLanguageCode": t.string(),
                "customizedAttribution": t.string().optional(),
                "glossaries": t.struct({"_": t.string().optional()}).optional(),
                "formatConversions": t.struct({"_": t.string().optional()}).optional(),
                "outputConfig": t.proxy(renames["BatchDocumentOutputConfigIn"]),
                "inputConfigs": t.array(t.proxy(renames["BatchDocumentInputConfigIn"])),
                "models": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDetectLanguage"] = translate.post(
        "v3/{parent}:batchTranslateDocument",
        t.struct(
            {
                "parent": t.string(),
                "enableShadowRemovalNativePdf": t.boolean().optional(),
                "targetLanguageCodes": t.array(t.string()),
                "sourceLanguageCode": t.string(),
                "customizedAttribution": t.string().optional(),
                "glossaries": t.struct({"_": t.string().optional()}).optional(),
                "formatConversions": t.struct({"_": t.string().optional()}).optional(),
                "outputConfig": t.proxy(renames["BatchDocumentOutputConfigIn"]),
                "inputConfigs": t.array(t.proxy(renames["BatchDocumentInputConfigIn"])),
                "models": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = translate.post(
        "v3/{parent}:batchTranslateDocument",
        t.struct(
            {
                "parent": t.string(),
                "enableShadowRemovalNativePdf": t.boolean().optional(),
                "targetLanguageCodes": t.array(t.string()),
                "sourceLanguageCode": t.string(),
                "customizedAttribution": t.string().optional(),
                "glossaries": t.struct({"_": t.string().optional()}).optional(),
                "formatConversions": t.struct({"_": t.string().optional()}).optional(),
                "outputConfig": t.proxy(renames["BatchDocumentOutputConfigIn"]),
                "inputConfigs": t.array(t.proxy(renames["BatchDocumentInputConfigIn"])),
                "models": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTranslateText"] = translate.post(
        "v3/{parent}:batchTranslateDocument",
        t.struct(
            {
                "parent": t.string(),
                "enableShadowRemovalNativePdf": t.boolean().optional(),
                "targetLanguageCodes": t.array(t.string()),
                "sourceLanguageCode": t.string(),
                "customizedAttribution": t.string().optional(),
                "glossaries": t.struct({"_": t.string().optional()}).optional(),
                "formatConversions": t.struct({"_": t.string().optional()}).optional(),
                "outputConfig": t.proxy(renames["BatchDocumentOutputConfigIn"]),
                "inputConfigs": t.array(t.proxy(renames["BatchDocumentInputConfigIn"])),
                "models": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBatchTranslateDocument"] = translate.post(
        "v3/{parent}:batchTranslateDocument",
        t.struct(
            {
                "parent": t.string(),
                "enableShadowRemovalNativePdf": t.boolean().optional(),
                "targetLanguageCodes": t.array(t.string()),
                "sourceLanguageCode": t.string(),
                "customizedAttribution": t.string().optional(),
                "glossaries": t.struct({"_": t.string().optional()}).optional(),
                "formatConversions": t.struct({"_": t.string().optional()}).optional(),
                "outputConfig": t.proxy(renames["BatchDocumentOutputConfigIn"]),
                "inputConfigs": t.array(t.proxy(renames["BatchDocumentInputConfigIn"])),
                "models": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = translate.post(
        "v3/{name}:wait",
        t.struct(
            {
                "name": t.string().optional(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = translate.post(
        "v3/{name}:wait",
        t.struct(
            {
                "name": t.string().optional(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = translate.post(
        "v3/{name}:wait",
        t.struct(
            {
                "name": t.string().optional(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = translate.post(
        "v3/{name}:wait",
        t.struct(
            {
                "name": t.string().optional(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsWait"] = translate.post(
        "v3/{name}:wait",
        t.struct(
            {
                "name": t.string().optional(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsModelsGet"] = translate.post(
        "v3/{parent}/models",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsModelsList"] = translate.post(
        "v3/{parent}/models",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsModelsDelete"] = translate.post(
        "v3/{parent}/models",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsModelsCreate"] = translate.post(
        "v3/{parent}/models",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesList"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GlossaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesCreate"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GlossaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesPatch"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GlossaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesDelete"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GlossaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGet"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GlossaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGlossaryEntriesList"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GlossaryEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGlossaryEntriesCreate"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GlossaryEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGlossaryEntriesPatch"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GlossaryEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGlossaryEntriesDelete"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GlossaryEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGlossaryEntriesGet"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GlossaryEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsList"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatasetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDelete"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatasetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsCreate"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatasetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsExportData"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatasetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsImportData"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatasetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsGet"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatasetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsExamplesList"] = translate.get(
        "v3/{parent}/examples",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExamplesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="translate", renames=renames, types=types, functions=functions
    )
