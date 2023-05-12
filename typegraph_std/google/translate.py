from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_translate() -> Import:
    translate = HTTPRuntime("https://translation.googleapis.com/")

    renames = {
        "ErrorResponse": "_translate_1_ErrorResponse",
        "LanguageCodePairIn": "_translate_2_LanguageCodePairIn",
        "LanguageCodePairOut": "_translate_3_LanguageCodePairOut",
        "InputConfigIn": "_translate_4_InputConfigIn",
        "InputConfigOut": "_translate_5_InputConfigOut",
        "ExportDataRequestIn": "_translate_6_ExportDataRequestIn",
        "ExportDataRequestOut": "_translate_7_ExportDataRequestOut",
        "OutputConfigIn": "_translate_8_OutputConfigIn",
        "OutputConfigOut": "_translate_9_OutputConfigOut",
        "ImportDataRequestIn": "_translate_10_ImportDataRequestIn",
        "ImportDataRequestOut": "_translate_11_ImportDataRequestOut",
        "GcsDestinationIn": "_translate_12_GcsDestinationIn",
        "GcsDestinationOut": "_translate_13_GcsDestinationOut",
        "BatchTranslateDocumentRequestIn": "_translate_14_BatchTranslateDocumentRequestIn",
        "BatchTranslateDocumentRequestOut": "_translate_15_BatchTranslateDocumentRequestOut",
        "ListGlossaryEntriesResponseIn": "_translate_16_ListGlossaryEntriesResponseIn",
        "ListGlossaryEntriesResponseOut": "_translate_17_ListGlossaryEntriesResponseOut",
        "TranslationIn": "_translate_18_TranslationIn",
        "TranslationOut": "_translate_19_TranslationOut",
        "TranslateDocumentRequestIn": "_translate_20_TranslateDocumentRequestIn",
        "TranslateDocumentRequestOut": "_translate_21_TranslateDocumentRequestOut",
        "ExampleIn": "_translate_22_ExampleIn",
        "ExampleOut": "_translate_23_ExampleOut",
        "GlossaryEntryIn": "_translate_24_GlossaryEntryIn",
        "GlossaryEntryOut": "_translate_25_GlossaryEntryOut",
        "GlossaryIn": "_translate_26_GlossaryIn",
        "GlossaryOut": "_translate_27_GlossaryOut",
        "SupportedLanguagesIn": "_translate_28_SupportedLanguagesIn",
        "SupportedLanguagesOut": "_translate_29_SupportedLanguagesOut",
        "DocumentOutputConfigIn": "_translate_30_DocumentOutputConfigIn",
        "DocumentOutputConfigOut": "_translate_31_DocumentOutputConfigOut",
        "DetectLanguageResponseIn": "_translate_32_DetectLanguageResponseIn",
        "DetectLanguageResponseOut": "_translate_33_DetectLanguageResponseOut",
        "TranslateTextRequestIn": "_translate_34_TranslateTextRequestIn",
        "TranslateTextRequestOut": "_translate_35_TranslateTextRequestOut",
        "GcsInputSourceIn": "_translate_36_GcsInputSourceIn",
        "GcsInputSourceOut": "_translate_37_GcsInputSourceOut",
        "ListDatasetsResponseIn": "_translate_38_ListDatasetsResponseIn",
        "ListDatasetsResponseOut": "_translate_39_ListDatasetsResponseOut",
        "DatasetInputConfigIn": "_translate_40_DatasetInputConfigIn",
        "DatasetInputConfigOut": "_translate_41_DatasetInputConfigOut",
        "GcsSourceIn": "_translate_42_GcsSourceIn",
        "GcsSourceOut": "_translate_43_GcsSourceOut",
        "ListModelsResponseIn": "_translate_44_ListModelsResponseIn",
        "ListModelsResponseOut": "_translate_45_ListModelsResponseOut",
        "EmptyIn": "_translate_46_EmptyIn",
        "EmptyOut": "_translate_47_EmptyOut",
        "TranslateTextGlossaryConfigIn": "_translate_48_TranslateTextGlossaryConfigIn",
        "TranslateTextGlossaryConfigOut": "_translate_49_TranslateTextGlossaryConfigOut",
        "DocumentTranslationIn": "_translate_50_DocumentTranslationIn",
        "DocumentTranslationOut": "_translate_51_DocumentTranslationOut",
        "OperationIn": "_translate_52_OperationIn",
        "OperationOut": "_translate_53_OperationOut",
        "ListOperationsResponseIn": "_translate_54_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_translate_55_ListOperationsResponseOut",
        "SupportedLanguageIn": "_translate_56_SupportedLanguageIn",
        "SupportedLanguageOut": "_translate_57_SupportedLanguageOut",
        "CancelOperationRequestIn": "_translate_58_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_translate_59_CancelOperationRequestOut",
        "StatusIn": "_translate_60_StatusIn",
        "StatusOut": "_translate_61_StatusOut",
        "GlossaryTermIn": "_translate_62_GlossaryTermIn",
        "GlossaryTermOut": "_translate_63_GlossaryTermOut",
        "WaitOperationRequestIn": "_translate_64_WaitOperationRequestIn",
        "WaitOperationRequestOut": "_translate_65_WaitOperationRequestOut",
        "GcsOutputDestinationIn": "_translate_66_GcsOutputDestinationIn",
        "GcsOutputDestinationOut": "_translate_67_GcsOutputDestinationOut",
        "GlossaryInputConfigIn": "_translate_68_GlossaryInputConfigIn",
        "GlossaryInputConfigOut": "_translate_69_GlossaryInputConfigOut",
        "GlossaryTermsPairIn": "_translate_70_GlossaryTermsPairIn",
        "GlossaryTermsPairOut": "_translate_71_GlossaryTermsPairOut",
        "TranslateDocumentResponseIn": "_translate_72_TranslateDocumentResponseIn",
        "TranslateDocumentResponseOut": "_translate_73_TranslateDocumentResponseOut",
        "ListLocationsResponseIn": "_translate_74_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_translate_75_ListLocationsResponseOut",
        "GlossaryTermsSetIn": "_translate_76_GlossaryTermsSetIn",
        "GlossaryTermsSetOut": "_translate_77_GlossaryTermsSetOut",
        "LocationIn": "_translate_78_LocationIn",
        "LocationOut": "_translate_79_LocationOut",
        "DetectLanguageRequestIn": "_translate_80_DetectLanguageRequestIn",
        "DetectLanguageRequestOut": "_translate_81_DetectLanguageRequestOut",
        "BatchTranslateTextRequestIn": "_translate_82_BatchTranslateTextRequestIn",
        "BatchTranslateTextRequestOut": "_translate_83_BatchTranslateTextRequestOut",
        "BatchDocumentOutputConfigIn": "_translate_84_BatchDocumentOutputConfigIn",
        "BatchDocumentOutputConfigOut": "_translate_85_BatchDocumentOutputConfigOut",
        "ListGlossariesResponseIn": "_translate_86_ListGlossariesResponseIn",
        "ListGlossariesResponseOut": "_translate_87_ListGlossariesResponseOut",
        "DatasetOutputConfigIn": "_translate_88_DatasetOutputConfigIn",
        "DatasetOutputConfigOut": "_translate_89_DatasetOutputConfigOut",
        "DatasetIn": "_translate_90_DatasetIn",
        "DatasetOut": "_translate_91_DatasetOut",
        "DocumentInputConfigIn": "_translate_92_DocumentInputConfigIn",
        "DocumentInputConfigOut": "_translate_93_DocumentInputConfigOut",
        "ModelIn": "_translate_94_ModelIn",
        "ModelOut": "_translate_95_ModelOut",
        "BatchDocumentInputConfigIn": "_translate_96_BatchDocumentInputConfigIn",
        "BatchDocumentInputConfigOut": "_translate_97_BatchDocumentInputConfigOut",
        "LanguageCodesSetIn": "_translate_98_LanguageCodesSetIn",
        "LanguageCodesSetOut": "_translate_99_LanguageCodesSetOut",
        "TranslateTextResponseIn": "_translate_100_TranslateTextResponseIn",
        "TranslateTextResponseOut": "_translate_101_TranslateTextResponseOut",
        "InputFileIn": "_translate_102_InputFileIn",
        "InputFileOut": "_translate_103_InputFileOut",
        "DetectedLanguageIn": "_translate_104_DetectedLanguageIn",
        "DetectedLanguageOut": "_translate_105_DetectedLanguageOut",
        "ListExamplesResponseIn": "_translate_106_ListExamplesResponseIn",
        "ListExamplesResponseOut": "_translate_107_ListExamplesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LanguageCodePairIn"] = t.struct(
        {"sourceLanguageCode": t.string(), "targetLanguageCode": t.string()}
    ).named(renames["LanguageCodePairIn"])
    types["LanguageCodePairOut"] = t.struct(
        {
            "sourceLanguageCode": t.string(),
            "targetLanguageCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageCodePairOut"])
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
    types["ExportDataRequestIn"] = t.struct(
        {"outputConfig": t.proxy(renames["DatasetOutputConfigIn"])}
    ).named(renames["ExportDataRequestIn"])
    types["ExportDataRequestOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["DatasetOutputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportDataRequestOut"])
    types["OutputConfigIn"] = t.struct(
        {"gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional()}
    ).named(renames["OutputConfigIn"])
    types["OutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutputConfigOut"])
    types["ImportDataRequestIn"] = t.struct(
        {"inputConfig": t.proxy(renames["DatasetInputConfigIn"])}
    ).named(renames["ImportDataRequestIn"])
    types["ImportDataRequestOut"] = t.struct(
        {
            "inputConfig": t.proxy(renames["DatasetInputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportDataRequestOut"])
    types["GcsDestinationIn"] = t.struct({"outputUriPrefix": t.string()}).named(
        renames["GcsDestinationIn"]
    )
    types["GcsDestinationOut"] = t.struct(
        {
            "outputUriPrefix": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsDestinationOut"])
    types["BatchTranslateDocumentRequestIn"] = t.struct(
        {
            "targetLanguageCodes": t.array(t.string()),
            "outputConfig": t.proxy(renames["BatchDocumentOutputConfigIn"]),
            "glossaries": t.struct({"_": t.string().optional()}).optional(),
            "sourceLanguageCode": t.string(),
            "enableShadowRemovalNativePdf": t.boolean().optional(),
            "customizedAttribution": t.string().optional(),
            "formatConversions": t.struct({"_": t.string().optional()}).optional(),
            "models": t.struct({"_": t.string().optional()}).optional(),
            "inputConfigs": t.array(t.proxy(renames["BatchDocumentInputConfigIn"])),
        }
    ).named(renames["BatchTranslateDocumentRequestIn"])
    types["BatchTranslateDocumentRequestOut"] = t.struct(
        {
            "targetLanguageCodes": t.array(t.string()),
            "outputConfig": t.proxy(renames["BatchDocumentOutputConfigOut"]),
            "glossaries": t.struct({"_": t.string().optional()}).optional(),
            "sourceLanguageCode": t.string(),
            "enableShadowRemovalNativePdf": t.boolean().optional(),
            "customizedAttribution": t.string().optional(),
            "formatConversions": t.struct({"_": t.string().optional()}).optional(),
            "models": t.struct({"_": t.string().optional()}).optional(),
            "inputConfigs": t.array(t.proxy(renames["BatchDocumentInputConfigOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchTranslateDocumentRequestOut"])
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
    types["TranslationIn"] = t.struct(
        {
            "detectedLanguageCode": t.string().optional(),
            "model": t.string().optional(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigIn"]
            ).optional(),
            "translatedText": t.string().optional(),
        }
    ).named(renames["TranslationIn"])
    types["TranslationOut"] = t.struct(
        {
            "detectedLanguageCode": t.string().optional(),
            "model": t.string().optional(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigOut"]
            ).optional(),
            "translatedText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslationOut"])
    types["TranslateDocumentRequestIn"] = t.struct(
        {
            "documentOutputConfig": t.proxy(
                renames["DocumentOutputConfigIn"]
            ).optional(),
            "enableShadowRemovalNativePdf": t.boolean().optional(),
            "customizedAttribution": t.string().optional(),
            "isTranslateNativePdfOnly": t.boolean().optional(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigIn"]
            ).optional(),
            "targetLanguageCode": t.string(),
            "model": t.string().optional(),
            "sourceLanguageCode": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "documentInputConfig": t.proxy(renames["DocumentInputConfigIn"]),
            "enableRotationCorrection": t.boolean().optional(),
        }
    ).named(renames["TranslateDocumentRequestIn"])
    types["TranslateDocumentRequestOut"] = t.struct(
        {
            "documentOutputConfig": t.proxy(
                renames["DocumentOutputConfigOut"]
            ).optional(),
            "enableShadowRemovalNativePdf": t.boolean().optional(),
            "customizedAttribution": t.string().optional(),
            "isTranslateNativePdfOnly": t.boolean().optional(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigOut"]
            ).optional(),
            "targetLanguageCode": t.string(),
            "model": t.string().optional(),
            "sourceLanguageCode": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "documentInputConfig": t.proxy(renames["DocumentInputConfigOut"]),
            "enableRotationCorrection": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslateDocumentRequestOut"])
    types["ExampleIn"] = t.struct(
        {"sourceText": t.string().optional(), "targetText": t.string().optional()}
    ).named(renames["ExampleIn"])
    types["ExampleOut"] = t.struct(
        {
            "sourceText": t.string().optional(),
            "name": t.string().optional(),
            "usage": t.string().optional(),
            "targetText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExampleOut"])
    types["GlossaryEntryIn"] = t.struct(
        {
            "termsPair": t.proxy(renames["GlossaryTermsPairIn"]).optional(),
            "description": t.string().optional(),
            "termsSet": t.proxy(renames["GlossaryTermsSetIn"]).optional(),
            "name": t.string(),
        }
    ).named(renames["GlossaryEntryIn"])
    types["GlossaryEntryOut"] = t.struct(
        {
            "termsPair": t.proxy(renames["GlossaryTermsPairOut"]).optional(),
            "description": t.string().optional(),
            "termsSet": t.proxy(renames["GlossaryTermsSetOut"]).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryEntryOut"])
    types["GlossaryIn"] = t.struct(
        {
            "languagePair": t.proxy(renames["LanguageCodePairIn"]).optional(),
            "name": t.string(),
            "inputConfig": t.proxy(renames["GlossaryInputConfigIn"]),
            "languageCodesSet": t.proxy(renames["LanguageCodesSetIn"]).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GlossaryIn"])
    types["GlossaryOut"] = t.struct(
        {
            "languagePair": t.proxy(renames["LanguageCodePairOut"]).optional(),
            "name": t.string(),
            "inputConfig": t.proxy(renames["GlossaryInputConfigOut"]),
            "submitTime": t.string().optional(),
            "endTime": t.string().optional(),
            "entryCount": t.integer().optional(),
            "languageCodesSet": t.proxy(renames["LanguageCodesSetOut"]).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryOut"])
    types["SupportedLanguagesIn"] = t.struct(
        {"languages": t.array(t.proxy(renames["SupportedLanguageIn"])).optional()}
    ).named(renames["SupportedLanguagesIn"])
    types["SupportedLanguagesOut"] = t.struct(
        {
            "languages": t.array(t.proxy(renames["SupportedLanguageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SupportedLanguagesOut"])
    types["DocumentOutputConfigIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional(),
        }
    ).named(renames["DocumentOutputConfigIn"])
    types["DocumentOutputConfigOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentOutputConfigOut"])
    types["DetectLanguageResponseIn"] = t.struct(
        {"languages": t.array(t.proxy(renames["DetectedLanguageIn"])).optional()}
    ).named(renames["DetectLanguageResponseIn"])
    types["DetectLanguageResponseOut"] = t.struct(
        {
            "languages": t.array(t.proxy(renames["DetectedLanguageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetectLanguageResponseOut"])
    types["TranslateTextRequestIn"] = t.struct(
        {
            "model": t.string().optional(),
            "sourceLanguageCode": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "contents": t.array(t.string()),
            "targetLanguageCode": t.string(),
            "mimeType": t.string().optional(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigIn"]
            ).optional(),
        }
    ).named(renames["TranslateTextRequestIn"])
    types["TranslateTextRequestOut"] = t.struct(
        {
            "model": t.string().optional(),
            "sourceLanguageCode": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "contents": t.array(t.string()),
            "targetLanguageCode": t.string(),
            "mimeType": t.string().optional(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslateTextRequestOut"])
    types["GcsInputSourceIn"] = t.struct({"inputUri": t.string()}).named(
        renames["GcsInputSourceIn"]
    )
    types["GcsInputSourceOut"] = t.struct(
        {"inputUri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GcsInputSourceOut"])
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
    types["DatasetInputConfigIn"] = t.struct(
        {"inputFiles": t.array(t.proxy(renames["InputFileIn"])).optional()}
    ).named(renames["DatasetInputConfigIn"])
    types["DatasetInputConfigOut"] = t.struct(
        {
            "inputFiles": t.array(t.proxy(renames["InputFileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetInputConfigOut"])
    types["GcsSourceIn"] = t.struct({"inputUri": t.string()}).named(
        renames["GcsSourceIn"]
    )
    types["GcsSourceOut"] = t.struct(
        {"inputUri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GcsSourceOut"])
    types["ListModelsResponseIn"] = t.struct(
        {
            "models": t.array(t.proxy(renames["ModelIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListModelsResponseIn"])
    types["ListModelsResponseOut"] = t.struct(
        {
            "models": t.array(t.proxy(renames["ModelOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListModelsResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TranslateTextGlossaryConfigIn"] = t.struct(
        {"glossary": t.string(), "ignoreCase": t.boolean().optional()}
    ).named(renames["TranslateTextGlossaryConfigIn"])
    types["TranslateTextGlossaryConfigOut"] = t.struct(
        {
            "glossary": t.string(),
            "ignoreCase": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslateTextGlossaryConfigOut"])
    types["DocumentTranslationIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "byteStreamOutputs": t.array(t.string()).optional(),
            "detectedLanguageCode": t.string().optional(),
        }
    ).named(renames["DocumentTranslationIn"])
    types["DocumentTranslationOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "byteStreamOutputs": t.array(t.string()).optional(),
            "detectedLanguageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentTranslationOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["SupportedLanguageIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "languageCode": t.string().optional(),
            "supportTarget": t.boolean().optional(),
            "supportSource": t.boolean().optional(),
        }
    ).named(renames["SupportedLanguageIn"])
    types["SupportedLanguageOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "languageCode": t.string().optional(),
            "supportTarget": t.boolean().optional(),
            "supportSource": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SupportedLanguageOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["WaitOperationRequestIn"] = t.struct(
        {"timeout": t.string().optional()}
    ).named(renames["WaitOperationRequestIn"])
    types["WaitOperationRequestOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaitOperationRequestOut"])
    types["GcsOutputDestinationIn"] = t.struct({"outputUriPrefix": t.string()}).named(
        renames["GcsOutputDestinationIn"]
    )
    types["GcsOutputDestinationOut"] = t.struct(
        {
            "outputUriPrefix": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsOutputDestinationOut"])
    types["GlossaryInputConfigIn"] = t.struct(
        {"gcsSource": t.proxy(renames["GcsSourceIn"])}
    ).named(renames["GlossaryInputConfigIn"])
    types["GlossaryInputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryInputConfigOut"])
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
    types["TranslateDocumentResponseIn"] = t.struct(
        {
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigIn"]
            ).optional(),
            "documentTranslation": t.proxy(renames["DocumentTranslationIn"]).optional(),
            "glossaryDocumentTranslation": t.proxy(
                renames["DocumentTranslationIn"]
            ).optional(),
            "model": t.string().optional(),
        }
    ).named(renames["TranslateDocumentResponseIn"])
    types["TranslateDocumentResponseOut"] = t.struct(
        {
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigOut"]
            ).optional(),
            "documentTranslation": t.proxy(
                renames["DocumentTranslationOut"]
            ).optional(),
            "glossaryDocumentTranslation": t.proxy(
                renames["DocumentTranslationOut"]
            ).optional(),
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslateDocumentResponseOut"])
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
    types["GlossaryTermsSetIn"] = t.struct(
        {"terms": t.array(t.proxy(renames["GlossaryTermIn"])).optional()}
    ).named(renames["GlossaryTermsSetIn"])
    types["GlossaryTermsSetOut"] = t.struct(
        {
            "terms": t.array(t.proxy(renames["GlossaryTermOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryTermsSetOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["DetectLanguageRequestIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "model": t.string().optional(),
        }
    ).named(renames["DetectLanguageRequestIn"])
    types["DetectLanguageRequestOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetectLanguageRequestOut"])
    types["BatchTranslateTextRequestIn"] = t.struct(
        {
            "sourceLanguageCode": t.string(),
            "glossaries": t.struct({"_": t.string().optional()}).optional(),
            "outputConfig": t.proxy(renames["OutputConfigIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "inputConfigs": t.array(t.proxy(renames["InputConfigIn"])),
            "models": t.struct({"_": t.string().optional()}).optional(),
            "targetLanguageCodes": t.array(t.string()),
        }
    ).named(renames["BatchTranslateTextRequestIn"])
    types["BatchTranslateTextRequestOut"] = t.struct(
        {
            "sourceLanguageCode": t.string(),
            "glossaries": t.struct({"_": t.string().optional()}).optional(),
            "outputConfig": t.proxy(renames["OutputConfigOut"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "inputConfigs": t.array(t.proxy(renames["InputConfigOut"])),
            "models": t.struct({"_": t.string().optional()}).optional(),
            "targetLanguageCodes": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchTranslateTextRequestOut"])
    types["BatchDocumentOutputConfigIn"] = t.struct(
        {"gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional()}
    ).named(renames["BatchDocumentOutputConfigIn"])
    types["BatchDocumentOutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDocumentOutputConfigOut"])
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
    types["DatasetOutputConfigIn"] = t.struct(
        {"gcsDestination": t.proxy(renames["GcsOutputDestinationIn"]).optional()}
    ).named(renames["DatasetOutputConfigIn"])
    types["DatasetOutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsOutputDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetOutputConfigOut"])
    types["DatasetIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "sourceLanguageCode": t.string().optional(),
            "targetLanguageCode": t.string().optional(),
        }
    ).named(renames["DatasetIn"])
    types["DatasetOut"] = t.struct(
        {
            "name": t.string().optional(),
            "validateExampleCount": t.integer().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "testExampleCount": t.integer().optional(),
            "trainExampleCount": t.integer().optional(),
            "sourceLanguageCode": t.string().optional(),
            "targetLanguageCode": t.string().optional(),
            "exampleCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetOut"])
    types["DocumentInputConfigIn"] = t.struct(
        {
            "content": t.string().optional(),
            "mimeType": t.string().optional(),
            "gcsSource": t.proxy(renames["GcsSourceIn"]).optional(),
        }
    ).named(renames["DocumentInputConfigIn"])
    types["DocumentInputConfigOut"] = t.struct(
        {
            "content": t.string().optional(),
            "mimeType": t.string().optional(),
            "gcsSource": t.proxy(renames["GcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentInputConfigOut"])
    types["ModelIn"] = t.struct(
        {
            "dataset": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ModelIn"])
    types["ModelOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "targetLanguageCode": t.string().optional(),
            "dataset": t.string().optional(),
            "testExampleCount": t.integer().optional(),
            "validateExampleCount": t.integer().optional(),
            "trainExampleCount": t.integer().optional(),
            "sourceLanguageCode": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModelOut"])
    types["BatchDocumentInputConfigIn"] = t.struct(
        {"gcsSource": t.proxy(renames["GcsSourceIn"]).optional()}
    ).named(renames["BatchDocumentInputConfigIn"])
    types["BatchDocumentInputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDocumentInputConfigOut"])
    types["LanguageCodesSetIn"] = t.struct(
        {"languageCodes": t.array(t.string()).optional()}
    ).named(renames["LanguageCodesSetIn"])
    types["LanguageCodesSetOut"] = t.struct(
        {
            "languageCodes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageCodesSetOut"])
    types["TranslateTextResponseIn"] = t.struct(
        {
            "translations": t.array(t.proxy(renames["TranslationIn"])).optional(),
            "glossaryTranslations": t.array(
                t.proxy(renames["TranslationIn"])
            ).optional(),
        }
    ).named(renames["TranslateTextResponseIn"])
    types["TranslateTextResponseOut"] = t.struct(
        {
            "translations": t.array(t.proxy(renames["TranslationOut"])).optional(),
            "glossaryTranslations": t.array(
                t.proxy(renames["TranslationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslateTextResponseOut"])
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
    types["DetectedLanguageIn"] = t.struct(
        {"confidence": t.number().optional(), "languageCode": t.string().optional()}
    ).named(renames["DetectedLanguageIn"])
    types["DetectedLanguageOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetectedLanguageOut"])
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

    functions = {}
    functions["projectsTranslateText"] = translate.post(
        "v3/{parent}:detectLanguage",
        t.struct(
            {
                "parent": t.string(),
                "mimeType": t.string().optional(),
                "content": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "model": t.string().optional(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "model": t.string().optional(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "model": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DetectLanguageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGetSupportedLanguages"] = translate.post(
        "v3/{parent}:translateText",
        t.struct(
            {
                "parent": t.string(),
                "model": t.string().optional(),
                "sourceLanguageCode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.array(t.string()),
                "targetLanguageCode": t.string(),
                "mimeType": t.string().optional(),
                "glossaryConfig": t.proxy(
                    renames["TranslateTextGlossaryConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TranslateTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBatchTranslateDocument"] = translate.post(
        "v3/{parent}:translateText",
        t.struct(
            {
                "parent": t.string(),
                "model": t.string().optional(),
                "sourceLanguageCode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.array(t.string()),
                "targetLanguageCode": t.string(),
                "mimeType": t.string().optional(),
                "glossaryConfig": t.proxy(
                    renames["TranslateTextGlossaryConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TranslateTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBatchTranslateText"] = translate.post(
        "v3/{parent}:translateText",
        t.struct(
            {
                "parent": t.string(),
                "model": t.string().optional(),
                "sourceLanguageCode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.array(t.string()),
                "targetLanguageCode": t.string(),
                "mimeType": t.string().optional(),
                "glossaryConfig": t.proxy(
                    renames["TranslateTextGlossaryConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TranslateTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTranslateDocument"] = translate.post(
        "v3/{parent}:translateText",
        t.struct(
            {
                "parent": t.string(),
                "model": t.string().optional(),
                "sourceLanguageCode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.array(t.string()),
                "targetLanguageCode": t.string(),
                "mimeType": t.string().optional(),
                "glossaryConfig": t.proxy(
                    renames["TranslateTextGlossaryConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TranslateTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = translate.post(
        "v3/{parent}:translateText",
        t.struct(
            {
                "parent": t.string(),
                "model": t.string().optional(),
                "sourceLanguageCode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.array(t.string()),
                "targetLanguageCode": t.string(),
                "mimeType": t.string().optional(),
                "glossaryConfig": t.proxy(
                    renames["TranslateTextGlossaryConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TranslateTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDetectLanguage"] = translate.post(
        "v3/{parent}:translateText",
        t.struct(
            {
                "parent": t.string(),
                "model": t.string().optional(),
                "sourceLanguageCode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.array(t.string()),
                "targetLanguageCode": t.string(),
                "mimeType": t.string().optional(),
                "glossaryConfig": t.proxy(
                    renames["TranslateTextGlossaryConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TranslateTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = translate.post(
        "v3/{parent}:translateText",
        t.struct(
            {
                "parent": t.string(),
                "model": t.string().optional(),
                "sourceLanguageCode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.array(t.string()),
                "targetLanguageCode": t.string(),
                "mimeType": t.string().optional(),
                "glossaryConfig": t.proxy(
                    renames["TranslateTextGlossaryConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TranslateTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTranslateText"] = translate.post(
        "v3/{parent}:translateText",
        t.struct(
            {
                "parent": t.string(),
                "model": t.string().optional(),
                "sourceLanguageCode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.array(t.string()),
                "targetLanguageCode": t.string(),
                "mimeType": t.string().optional(),
                "glossaryConfig": t.proxy(
                    renames["TranslateTextGlossaryConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TranslateTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsModelsCreate"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ModelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsModelsDelete"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ModelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsModelsList"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ModelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsModelsGet"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ModelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsGet"] = translate.get(
        "v3/{parent}/datasets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDatasetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsCreate"] = translate.get(
        "v3/{parent}/datasets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDatasetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDelete"] = translate.get(
        "v3/{parent}/datasets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDatasetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsImportData"] = translate.get(
        "v3/{parent}/datasets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDatasetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsExportData"] = translate.get(
        "v3/{parent}/datasets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDatasetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsList"] = translate.get(
        "v3/{parent}/datasets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDatasetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsExamplesList"] = translate.get(
        "v3/{parent}/examples",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExamplesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesList"] = translate.post(
        "v3/{parent}/glossaries",
        t.struct(
            {
                "parent": t.string(),
                "languagePair": t.proxy(renames["LanguageCodePairIn"]).optional(),
                "name": t.string(),
                "inputConfig": t.proxy(renames["GlossaryInputConfigIn"]),
                "languageCodesSet": t.proxy(renames["LanguageCodesSetIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesDelete"] = translate.post(
        "v3/{parent}/glossaries",
        t.struct(
            {
                "parent": t.string(),
                "languagePair": t.proxy(renames["LanguageCodePairIn"]).optional(),
                "name": t.string(),
                "inputConfig": t.proxy(renames["GlossaryInputConfigIn"]),
                "languageCodesSet": t.proxy(renames["LanguageCodesSetIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGet"] = translate.post(
        "v3/{parent}/glossaries",
        t.struct(
            {
                "parent": t.string(),
                "languagePair": t.proxy(renames["LanguageCodePairIn"]).optional(),
                "name": t.string(),
                "inputConfig": t.proxy(renames["GlossaryInputConfigIn"]),
                "languageCodesSet": t.proxy(renames["LanguageCodesSetIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesPatch"] = translate.post(
        "v3/{parent}/glossaries",
        t.struct(
            {
                "parent": t.string(),
                "languagePair": t.proxy(renames["LanguageCodePairIn"]).optional(),
                "name": t.string(),
                "inputConfig": t.proxy(renames["GlossaryInputConfigIn"]),
                "languageCodesSet": t.proxy(renames["LanguageCodesSetIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesCreate"] = translate.post(
        "v3/{parent}/glossaries",
        t.struct(
            {
                "parent": t.string(),
                "languagePair": t.proxy(renames["LanguageCodePairIn"]).optional(),
                "name": t.string(),
                "inputConfig": t.proxy(renames["GlossaryInputConfigIn"]),
                "languageCodesSet": t.proxy(renames["LanguageCodesSetIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGlossaryEntriesCreate"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGlossaryEntriesPatch"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGlossaryEntriesGet"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGlossaryEntriesList"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGlossaryEntriesDelete"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = translate.post(
        "v3/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = translate.post(
        "v3/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = translate.post(
        "v3/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsWait"] = translate.post(
        "v3/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = translate.post(
        "v3/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="translate",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
