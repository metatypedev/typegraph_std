from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_translate():
    translate = HTTPRuntime("https://translation.googleapis.com/")

    renames = {
        "ErrorResponse": "_translate_1_ErrorResponse",
        "TranslateTextResponseIn": "_translate_2_TranslateTextResponseIn",
        "TranslateTextResponseOut": "_translate_3_TranslateTextResponseOut",
        "ListOperationsResponseIn": "_translate_4_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_translate_5_ListOperationsResponseOut",
        "ListGlossariesResponseIn": "_translate_6_ListGlossariesResponseIn",
        "ListGlossariesResponseOut": "_translate_7_ListGlossariesResponseOut",
        "GlossaryEntryIn": "_translate_8_GlossaryEntryIn",
        "GlossaryEntryOut": "_translate_9_GlossaryEntryOut",
        "TranslateDocumentResponseIn": "_translate_10_TranslateDocumentResponseIn",
        "TranslateDocumentResponseOut": "_translate_11_TranslateDocumentResponseOut",
        "OutputConfigIn": "_translate_12_OutputConfigIn",
        "OutputConfigOut": "_translate_13_OutputConfigOut",
        "RomanizeTextRequestIn": "_translate_14_RomanizeTextRequestIn",
        "RomanizeTextRequestOut": "_translate_15_RomanizeTextRequestOut",
        "GlossaryTermIn": "_translate_16_GlossaryTermIn",
        "GlossaryTermOut": "_translate_17_GlossaryTermOut",
        "InputConfigIn": "_translate_18_InputConfigIn",
        "InputConfigOut": "_translate_19_InputConfigOut",
        "DocumentOutputConfigIn": "_translate_20_DocumentOutputConfigIn",
        "DocumentOutputConfigOut": "_translate_21_DocumentOutputConfigOut",
        "StatusIn": "_translate_22_StatusIn",
        "StatusOut": "_translate_23_StatusOut",
        "LocationIn": "_translate_24_LocationIn",
        "LocationOut": "_translate_25_LocationOut",
        "GlossaryIn": "_translate_26_GlossaryIn",
        "GlossaryOut": "_translate_27_GlossaryOut",
        "GcsOutputDestinationIn": "_translate_28_GcsOutputDestinationIn",
        "GcsOutputDestinationOut": "_translate_29_GcsOutputDestinationOut",
        "GcsDestinationIn": "_translate_30_GcsDestinationIn",
        "GcsDestinationOut": "_translate_31_GcsDestinationOut",
        "BatchDocumentInputConfigIn": "_translate_32_BatchDocumentInputConfigIn",
        "BatchDocumentInputConfigOut": "_translate_33_BatchDocumentInputConfigOut",
        "ListDatasetsResponseIn": "_translate_34_ListDatasetsResponseIn",
        "ListDatasetsResponseOut": "_translate_35_ListDatasetsResponseOut",
        "TranslateTextRequestIn": "_translate_36_TranslateTextRequestIn",
        "TranslateTextRequestOut": "_translate_37_TranslateTextRequestOut",
        "ListGlossaryEntriesResponseIn": "_translate_38_ListGlossaryEntriesResponseIn",
        "ListGlossaryEntriesResponseOut": "_translate_39_ListGlossaryEntriesResponseOut",
        "GcsSourceIn": "_translate_40_GcsSourceIn",
        "GcsSourceOut": "_translate_41_GcsSourceOut",
        "BatchTranslateTextRequestIn": "_translate_42_BatchTranslateTextRequestIn",
        "BatchTranslateTextRequestOut": "_translate_43_BatchTranslateTextRequestOut",
        "ExportDataRequestIn": "_translate_44_ExportDataRequestIn",
        "ExportDataRequestOut": "_translate_45_ExportDataRequestOut",
        "DetectLanguageRequestIn": "_translate_46_DetectLanguageRequestIn",
        "DetectLanguageRequestOut": "_translate_47_DetectLanguageRequestOut",
        "ListLocationsResponseIn": "_translate_48_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_translate_49_ListLocationsResponseOut",
        "DocumentTranslationIn": "_translate_50_DocumentTranslationIn",
        "DocumentTranslationOut": "_translate_51_DocumentTranslationOut",
        "DetectLanguageResponseIn": "_translate_52_DetectLanguageResponseIn",
        "DetectLanguageResponseOut": "_translate_53_DetectLanguageResponseOut",
        "TransliterationConfigIn": "_translate_54_TransliterationConfigIn",
        "TransliterationConfigOut": "_translate_55_TransliterationConfigOut",
        "EmptyIn": "_translate_56_EmptyIn",
        "EmptyOut": "_translate_57_EmptyOut",
        "DatasetIn": "_translate_58_DatasetIn",
        "DatasetOut": "_translate_59_DatasetOut",
        "LanguageCodePairIn": "_translate_60_LanguageCodePairIn",
        "LanguageCodePairOut": "_translate_61_LanguageCodePairOut",
        "LanguageCodesSetIn": "_translate_62_LanguageCodesSetIn",
        "LanguageCodesSetOut": "_translate_63_LanguageCodesSetOut",
        "DatasetInputConfigIn": "_translate_64_DatasetInputConfigIn",
        "DatasetInputConfigOut": "_translate_65_DatasetInputConfigOut",
        "DocumentInputConfigIn": "_translate_66_DocumentInputConfigIn",
        "DocumentInputConfigOut": "_translate_67_DocumentInputConfigOut",
        "DetectedLanguageIn": "_translate_68_DetectedLanguageIn",
        "DetectedLanguageOut": "_translate_69_DetectedLanguageOut",
        "ListExamplesResponseIn": "_translate_70_ListExamplesResponseIn",
        "ListExamplesResponseOut": "_translate_71_ListExamplesResponseOut",
        "RomanizeTextResponseIn": "_translate_72_RomanizeTextResponseIn",
        "RomanizeTextResponseOut": "_translate_73_RomanizeTextResponseOut",
        "GlossaryTermsPairIn": "_translate_74_GlossaryTermsPairIn",
        "GlossaryTermsPairOut": "_translate_75_GlossaryTermsPairOut",
        "TranslationIn": "_translate_76_TranslationIn",
        "TranslationOut": "_translate_77_TranslationOut",
        "BatchTranslateDocumentRequestIn": "_translate_78_BatchTranslateDocumentRequestIn",
        "BatchTranslateDocumentRequestOut": "_translate_79_BatchTranslateDocumentRequestOut",
        "InputFileIn": "_translate_80_InputFileIn",
        "InputFileOut": "_translate_81_InputFileOut",
        "RomanizationIn": "_translate_82_RomanizationIn",
        "RomanizationOut": "_translate_83_RomanizationOut",
        "SupportedLanguagesIn": "_translate_84_SupportedLanguagesIn",
        "SupportedLanguagesOut": "_translate_85_SupportedLanguagesOut",
        "GlossaryInputConfigIn": "_translate_86_GlossaryInputConfigIn",
        "GlossaryInputConfigOut": "_translate_87_GlossaryInputConfigOut",
        "WaitOperationRequestIn": "_translate_88_WaitOperationRequestIn",
        "WaitOperationRequestOut": "_translate_89_WaitOperationRequestOut",
        "BatchDocumentOutputConfigIn": "_translate_90_BatchDocumentOutputConfigIn",
        "BatchDocumentOutputConfigOut": "_translate_91_BatchDocumentOutputConfigOut",
        "TranslateTextGlossaryConfigIn": "_translate_92_TranslateTextGlossaryConfigIn",
        "TranslateTextGlossaryConfigOut": "_translate_93_TranslateTextGlossaryConfigOut",
        "GcsInputSourceIn": "_translate_94_GcsInputSourceIn",
        "GcsInputSourceOut": "_translate_95_GcsInputSourceOut",
        "CancelOperationRequestIn": "_translate_96_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_translate_97_CancelOperationRequestOut",
        "TranslateDocumentRequestIn": "_translate_98_TranslateDocumentRequestIn",
        "TranslateDocumentRequestOut": "_translate_99_TranslateDocumentRequestOut",
        "ExampleIn": "_translate_100_ExampleIn",
        "ExampleOut": "_translate_101_ExampleOut",
        "ModelIn": "_translate_102_ModelIn",
        "ModelOut": "_translate_103_ModelOut",
        "ImportDataRequestIn": "_translate_104_ImportDataRequestIn",
        "ImportDataRequestOut": "_translate_105_ImportDataRequestOut",
        "ListModelsResponseIn": "_translate_106_ListModelsResponseIn",
        "ListModelsResponseOut": "_translate_107_ListModelsResponseOut",
        "SupportedLanguageIn": "_translate_108_SupportedLanguageIn",
        "SupportedLanguageOut": "_translate_109_SupportedLanguageOut",
        "DatasetOutputConfigIn": "_translate_110_DatasetOutputConfigIn",
        "DatasetOutputConfigOut": "_translate_111_DatasetOutputConfigOut",
        "OperationIn": "_translate_112_OperationIn",
        "OperationOut": "_translate_113_OperationOut",
        "GlossaryTermsSetIn": "_translate_114_GlossaryTermsSetIn",
        "GlossaryTermsSetOut": "_translate_115_GlossaryTermsSetOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ListGlossariesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "glossaries": t.array(t.proxy(renames["GlossaryIn"])).optional(),
        }
    ).named(renames["ListGlossariesResponseIn"])
    types["ListGlossariesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "glossaries": t.array(t.proxy(renames["GlossaryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGlossariesResponseOut"])
    types["GlossaryEntryIn"] = t.struct(
        {
            "description": t.string().optional(),
            "termsSet": t.proxy(renames["GlossaryTermsSetIn"]).optional(),
            "termsPair": t.proxy(renames["GlossaryTermsPairIn"]).optional(),
            "name": t.string(),
        }
    ).named(renames["GlossaryEntryIn"])
    types["GlossaryEntryOut"] = t.struct(
        {
            "description": t.string().optional(),
            "termsSet": t.proxy(renames["GlossaryTermsSetOut"]).optional(),
            "termsPair": t.proxy(renames["GlossaryTermsPairOut"]).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryEntryOut"])
    types["TranslateDocumentResponseIn"] = t.struct(
        {
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigIn"]
            ).optional(),
            "glossaryDocumentTranslation": t.proxy(
                renames["DocumentTranslationIn"]
            ).optional(),
            "documentTranslation": t.proxy(renames["DocumentTranslationIn"]).optional(),
            "model": t.string().optional(),
        }
    ).named(renames["TranslateDocumentResponseIn"])
    types["TranslateDocumentResponseOut"] = t.struct(
        {
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigOut"]
            ).optional(),
            "glossaryDocumentTranslation": t.proxy(
                renames["DocumentTranslationOut"]
            ).optional(),
            "documentTranslation": t.proxy(
                renames["DocumentTranslationOut"]
            ).optional(),
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslateDocumentResponseOut"])
    types["OutputConfigIn"] = t.struct(
        {"gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional()}
    ).named(renames["OutputConfigIn"])
    types["OutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutputConfigOut"])
    types["RomanizeTextRequestIn"] = t.struct(
        {"sourceLanguageCode": t.string().optional(), "contents": t.array(t.string())}
    ).named(renames["RomanizeTextRequestIn"])
    types["RomanizeTextRequestOut"] = t.struct(
        {
            "sourceLanguageCode": t.string().optional(),
            "contents": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RomanizeTextRequestOut"])
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
    types["InputConfigIn"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceIn"]),
            "mimeType": t.string().optional(),
        }
    ).named(renames["InputConfigIn"])
    types["InputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputConfigOut"])
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
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["GlossaryIn"] = t.struct(
        {
            "languageCodesSet": t.proxy(renames["LanguageCodesSetIn"]).optional(),
            "displayName": t.string().optional(),
            "languagePair": t.proxy(renames["LanguageCodePairIn"]).optional(),
            "name": t.string(),
            "inputConfig": t.proxy(renames["GlossaryInputConfigIn"]),
        }
    ).named(renames["GlossaryIn"])
    types["GlossaryOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "submitTime": t.string().optional(),
            "languageCodesSet": t.proxy(renames["LanguageCodesSetOut"]).optional(),
            "displayName": t.string().optional(),
            "entryCount": t.integer().optional(),
            "languagePair": t.proxy(renames["LanguageCodePairOut"]).optional(),
            "name": t.string(),
            "inputConfig": t.proxy(renames["GlossaryInputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryOut"])
    types["GcsOutputDestinationIn"] = t.struct({"outputUriPrefix": t.string()}).named(
        renames["GcsOutputDestinationIn"]
    )
    types["GcsOutputDestinationOut"] = t.struct(
        {
            "outputUriPrefix": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsOutputDestinationOut"])
    types["GcsDestinationIn"] = t.struct({"outputUriPrefix": t.string()}).named(
        renames["GcsDestinationIn"]
    )
    types["GcsDestinationOut"] = t.struct(
        {
            "outputUriPrefix": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsDestinationOut"])
    types["BatchDocumentInputConfigIn"] = t.struct(
        {"gcsSource": t.proxy(renames["GcsSourceIn"]).optional()}
    ).named(renames["BatchDocumentInputConfigIn"])
    types["BatchDocumentInputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDocumentInputConfigOut"])
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
    types["TranslateTextRequestIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "targetLanguageCode": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "transliterationConfig": t.proxy(
                renames["TransliterationConfigIn"]
            ).optional(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigIn"]
            ).optional(),
            "model": t.string().optional(),
            "contents": t.array(t.string()),
            "sourceLanguageCode": t.string().optional(),
        }
    ).named(renames["TranslateTextRequestIn"])
    types["TranslateTextRequestOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "targetLanguageCode": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "transliterationConfig": t.proxy(
                renames["TransliterationConfigOut"]
            ).optional(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigOut"]
            ).optional(),
            "model": t.string().optional(),
            "contents": t.array(t.string()),
            "sourceLanguageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslateTextRequestOut"])
    types["ListGlossaryEntriesResponseIn"] = t.struct(
        {
            "glossaryEntries": t.array(t.proxy(renames["GlossaryEntryIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListGlossaryEntriesResponseIn"])
    types["ListGlossaryEntriesResponseOut"] = t.struct(
        {
            "glossaryEntries": t.array(t.proxy(renames["GlossaryEntryOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGlossaryEntriesResponseOut"])
    types["GcsSourceIn"] = t.struct({"inputUri": t.string()}).named(
        renames["GcsSourceIn"]
    )
    types["GcsSourceOut"] = t.struct(
        {"inputUri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GcsSourceOut"])
    types["BatchTranslateTextRequestIn"] = t.struct(
        {
            "inputConfigs": t.array(t.proxy(renames["InputConfigIn"])),
            "targetLanguageCodes": t.array(t.string()),
            "glossaries": t.struct({"_": t.string().optional()}).optional(),
            "sourceLanguageCode": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "models": t.struct({"_": t.string().optional()}).optional(),
            "outputConfig": t.proxy(renames["OutputConfigIn"]),
        }
    ).named(renames["BatchTranslateTextRequestIn"])
    types["BatchTranslateTextRequestOut"] = t.struct(
        {
            "inputConfigs": t.array(t.proxy(renames["InputConfigOut"])),
            "targetLanguageCodes": t.array(t.string()),
            "glossaries": t.struct({"_": t.string().optional()}).optional(),
            "sourceLanguageCode": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "models": t.struct({"_": t.string().optional()}).optional(),
            "outputConfig": t.proxy(renames["OutputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchTranslateTextRequestOut"])
    types["ExportDataRequestIn"] = t.struct(
        {"outputConfig": t.proxy(renames["DatasetOutputConfigIn"])}
    ).named(renames["ExportDataRequestIn"])
    types["ExportDataRequestOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["DatasetOutputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportDataRequestOut"])
    types["DetectLanguageRequestIn"] = t.struct(
        {
            "model": t.string().optional(),
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DetectLanguageRequestIn"])
    types["DetectLanguageRequestOut"] = t.struct(
        {
            "model": t.string().optional(),
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetectLanguageRequestOut"])
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
    types["DocumentTranslationIn"] = t.struct(
        {
            "byteStreamOutputs": t.array(t.string()).optional(),
            "detectedLanguageCode": t.string().optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["DocumentTranslationIn"])
    types["DocumentTranslationOut"] = t.struct(
        {
            "byteStreamOutputs": t.array(t.string()).optional(),
            "detectedLanguageCode": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentTranslationOut"])
    types["DetectLanguageResponseIn"] = t.struct(
        {"languages": t.array(t.proxy(renames["DetectedLanguageIn"])).optional()}
    ).named(renames["DetectLanguageResponseIn"])
    types["DetectLanguageResponseOut"] = t.struct(
        {
            "languages": t.array(t.proxy(renames["DetectedLanguageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetectLanguageResponseOut"])
    types["TransliterationConfigIn"] = t.struct(
        {"enableTransliteration": t.boolean().optional()}
    ).named(renames["TransliterationConfigIn"])
    types["TransliterationConfigOut"] = t.struct(
        {
            "enableTransliteration": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransliterationConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DatasetIn"] = t.struct(
        {
            "sourceLanguageCode": t.string().optional(),
            "targetLanguageCode": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DatasetIn"])
    types["DatasetOut"] = t.struct(
        {
            "exampleCount": t.integer().optional(),
            "testExampleCount": t.integer().optional(),
            "sourceLanguageCode": t.string().optional(),
            "targetLanguageCode": t.string().optional(),
            "updateTime": t.string().optional(),
            "validateExampleCount": t.integer().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "trainExampleCount": t.integer().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetOut"])
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
    types["LanguageCodesSetIn"] = t.struct(
        {"languageCodes": t.array(t.string()).optional()}
    ).named(renames["LanguageCodesSetIn"])
    types["LanguageCodesSetOut"] = t.struct(
        {
            "languageCodes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageCodesSetOut"])
    types["DatasetInputConfigIn"] = t.struct(
        {"inputFiles": t.array(t.proxy(renames["InputFileIn"])).optional()}
    ).named(renames["DatasetInputConfigIn"])
    types["DatasetInputConfigOut"] = t.struct(
        {
            "inputFiles": t.array(t.proxy(renames["InputFileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetInputConfigOut"])
    types["DocumentInputConfigIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "gcsSource": t.proxy(renames["GcsSourceIn"]).optional(),
            "content": t.string().optional(),
        }
    ).named(renames["DocumentInputConfigIn"])
    types["DocumentInputConfigOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "gcsSource": t.proxy(renames["GcsSourceOut"]).optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentInputConfigOut"])
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
    types["RomanizeTextResponseIn"] = t.struct(
        {"romanizations": t.array(t.proxy(renames["RomanizationIn"])).optional()}
    ).named(renames["RomanizeTextResponseIn"])
    types["RomanizeTextResponseOut"] = t.struct(
        {
            "romanizations": t.array(t.proxy(renames["RomanizationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RomanizeTextResponseOut"])
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
    types["BatchTranslateDocumentRequestIn"] = t.struct(
        {
            "customizedAttribution": t.string().optional(),
            "sourceLanguageCode": t.string(),
            "inputConfigs": t.array(t.proxy(renames["BatchDocumentInputConfigIn"])),
            "formatConversions": t.struct({"_": t.string().optional()}).optional(),
            "targetLanguageCodes": t.array(t.string()),
            "models": t.struct({"_": t.string().optional()}).optional(),
            "glossaries": t.struct({"_": t.string().optional()}).optional(),
            "enableShadowRemovalNativePdf": t.boolean().optional(),
            "outputConfig": t.proxy(renames["BatchDocumentOutputConfigIn"]),
        }
    ).named(renames["BatchTranslateDocumentRequestIn"])
    types["BatchTranslateDocumentRequestOut"] = t.struct(
        {
            "customizedAttribution": t.string().optional(),
            "sourceLanguageCode": t.string(),
            "inputConfigs": t.array(t.proxy(renames["BatchDocumentInputConfigOut"])),
            "formatConversions": t.struct({"_": t.string().optional()}).optional(),
            "targetLanguageCodes": t.array(t.string()),
            "models": t.struct({"_": t.string().optional()}).optional(),
            "glossaries": t.struct({"_": t.string().optional()}).optional(),
            "enableShadowRemovalNativePdf": t.boolean().optional(),
            "outputConfig": t.proxy(renames["BatchDocumentOutputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchTranslateDocumentRequestOut"])
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
    types["RomanizationIn"] = t.struct(
        {
            "detectedLanguageCode": t.string().optional(),
            "romanizedText": t.string().optional(),
        }
    ).named(renames["RomanizationIn"])
    types["RomanizationOut"] = t.struct(
        {
            "detectedLanguageCode": t.string().optional(),
            "romanizedText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RomanizationOut"])
    types["SupportedLanguagesIn"] = t.struct(
        {"languages": t.array(t.proxy(renames["SupportedLanguageIn"])).optional()}
    ).named(renames["SupportedLanguagesIn"])
    types["SupportedLanguagesOut"] = t.struct(
        {
            "languages": t.array(t.proxy(renames["SupportedLanguageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SupportedLanguagesOut"])
    types["GlossaryInputConfigIn"] = t.struct(
        {"gcsSource": t.proxy(renames["GcsSourceIn"])}
    ).named(renames["GlossaryInputConfigIn"])
    types["GlossaryInputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryInputConfigOut"])
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
    types["GcsInputSourceIn"] = t.struct({"inputUri": t.string()}).named(
        renames["GcsInputSourceIn"]
    )
    types["GcsInputSourceOut"] = t.struct(
        {"inputUri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GcsInputSourceOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["TranslateDocumentRequestIn"] = t.struct(
        {
            "documentInputConfig": t.proxy(renames["DocumentInputConfigIn"]),
            "customizedAttribution": t.string().optional(),
            "sourceLanguageCode": t.string().optional(),
            "enableShadowRemovalNativePdf": t.boolean().optional(),
            "targetLanguageCode": t.string(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigIn"]
            ).optional(),
            "documentOutputConfig": t.proxy(
                renames["DocumentOutputConfigIn"]
            ).optional(),
            "model": t.string().optional(),
            "enableRotationCorrection": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "isTranslateNativePdfOnly": t.boolean().optional(),
        }
    ).named(renames["TranslateDocumentRequestIn"])
    types["TranslateDocumentRequestOut"] = t.struct(
        {
            "documentInputConfig": t.proxy(renames["DocumentInputConfigOut"]),
            "customizedAttribution": t.string().optional(),
            "sourceLanguageCode": t.string().optional(),
            "enableShadowRemovalNativePdf": t.boolean().optional(),
            "targetLanguageCode": t.string(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigOut"]
            ).optional(),
            "documentOutputConfig": t.proxy(
                renames["DocumentOutputConfigOut"]
            ).optional(),
            "model": t.string().optional(),
            "enableRotationCorrection": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "isTranslateNativePdfOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslateDocumentRequestOut"])
    types["ExampleIn"] = t.struct(
        {"targetText": t.string().optional(), "sourceText": t.string().optional()}
    ).named(renames["ExampleIn"])
    types["ExampleOut"] = t.struct(
        {
            "targetText": t.string().optional(),
            "usage": t.string().optional(),
            "sourceText": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExampleOut"])
    types["ModelIn"] = t.struct(
        {
            "dataset": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ModelIn"])
    types["ModelOut"] = t.struct(
        {
            "dataset": t.string().optional(),
            "displayName": t.string().optional(),
            "trainExampleCount": t.integer().optional(),
            "name": t.string().optional(),
            "sourceLanguageCode": t.string().optional(),
            "targetLanguageCode": t.string().optional(),
            "createTime": t.string().optional(),
            "validateExampleCount": t.integer().optional(),
            "testExampleCount": t.integer().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModelOut"])
    types["ImportDataRequestIn"] = t.struct(
        {"inputConfig": t.proxy(renames["DatasetInputConfigIn"])}
    ).named(renames["ImportDataRequestIn"])
    types["ImportDataRequestOut"] = t.struct(
        {
            "inputConfig": t.proxy(renames["DatasetInputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportDataRequestOut"])
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
    types["SupportedLanguageIn"] = t.struct(
        {
            "supportSource": t.boolean().optional(),
            "languageCode": t.string().optional(),
            "displayName": t.string().optional(),
            "supportTarget": t.boolean().optional(),
        }
    ).named(renames["SupportedLanguageIn"])
    types["SupportedLanguageOut"] = t.struct(
        {
            "supportSource": t.boolean().optional(),
            "languageCode": t.string().optional(),
            "displayName": t.string().optional(),
            "supportTarget": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SupportedLanguageOut"])
    types["DatasetOutputConfigIn"] = t.struct(
        {"gcsDestination": t.proxy(renames["GcsOutputDestinationIn"]).optional()}
    ).named(renames["DatasetOutputConfigIn"])
    types["DatasetOutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsOutputDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetOutputConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["GlossaryTermsSetIn"] = t.struct(
        {"terms": t.array(t.proxy(renames["GlossaryTermIn"])).optional()}
    ).named(renames["GlossaryTermsSetIn"])
    types["GlossaryTermsSetOut"] = t.struct(
        {
            "terms": t.array(t.proxy(renames["GlossaryTermOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryTermsSetOut"])

    functions = {}
    functions["projectsGetSupportedLanguages"] = translate.post(
        "v3/{parent}:detectLanguage",
        t.struct(
            {
                "parent": t.string(),
                "model": t.string().optional(),
                "mimeType": t.string().optional(),
                "content": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DetectLanguageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRomanizeText"] = translate.post(
        "v3/{parent}:detectLanguage",
        t.struct(
            {
                "parent": t.string(),
                "model": t.string().optional(),
                "mimeType": t.string().optional(),
                "content": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DetectLanguageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTranslateText"] = translate.post(
        "v3/{parent}:detectLanguage",
        t.struct(
            {
                "parent": t.string(),
                "model": t.string().optional(),
                "mimeType": t.string().optional(),
                "content": t.string().optional(),
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
                "model": t.string().optional(),
                "mimeType": t.string().optional(),
                "content": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DetectLanguageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTranslateText"] = translate.post(
        "v3/{parent}:romanizeText",
        t.struct(
            {
                "parent": t.string(),
                "sourceLanguageCode": t.string().optional(),
                "contents": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RomanizeTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBatchTranslateDocument"] = translate.post(
        "v3/{parent}:romanizeText",
        t.struct(
            {
                "parent": t.string(),
                "sourceLanguageCode": t.string().optional(),
                "contents": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RomanizeTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = translate.post(
        "v3/{parent}:romanizeText",
        t.struct(
            {
                "parent": t.string(),
                "sourceLanguageCode": t.string().optional(),
                "contents": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RomanizeTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBatchTranslateText"] = translate.post(
        "v3/{parent}:romanizeText",
        t.struct(
            {
                "parent": t.string(),
                "sourceLanguageCode": t.string().optional(),
                "contents": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RomanizeTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGetSupportedLanguages"] = translate.post(
        "v3/{parent}:romanizeText",
        t.struct(
            {
                "parent": t.string(),
                "sourceLanguageCode": t.string().optional(),
                "contents": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RomanizeTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDetectLanguage"] = translate.post(
        "v3/{parent}:romanizeText",
        t.struct(
            {
                "parent": t.string(),
                "sourceLanguageCode": t.string().optional(),
                "contents": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RomanizeTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTranslateDocument"] = translate.post(
        "v3/{parent}:romanizeText",
        t.struct(
            {
                "parent": t.string(),
                "sourceLanguageCode": t.string().optional(),
                "contents": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RomanizeTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = translate.post(
        "v3/{parent}:romanizeText",
        t.struct(
            {
                "parent": t.string(),
                "sourceLanguageCode": t.string().optional(),
                "contents": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RomanizeTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRomanizeText"] = translate.post(
        "v3/{parent}:romanizeText",
        t.struct(
            {
                "parent": t.string(),
                "sourceLanguageCode": t.string().optional(),
                "contents": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RomanizeTextResponseOut"]),
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
    functions["projectsLocationsDatasetsExportData"] = translate.get(
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
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExamplesResponseOut"]),
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
    functions["projectsLocationsModelsGet"] = translate.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ModelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesCreate"] = translate.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "languageCodesSet": t.proxy(renames["LanguageCodesSetIn"]).optional(),
                "displayName": t.string().optional(),
                "languagePair": t.proxy(renames["LanguageCodePairIn"]).optional(),
                "inputConfig": t.proxy(renames["GlossaryInputConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesDelete"] = translate.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "languageCodesSet": t.proxy(renames["LanguageCodesSetIn"]).optional(),
                "displayName": t.string().optional(),
                "languagePair": t.proxy(renames["LanguageCodePairIn"]).optional(),
                "inputConfig": t.proxy(renames["GlossaryInputConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesList"] = translate.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "languageCodesSet": t.proxy(renames["LanguageCodesSetIn"]).optional(),
                "displayName": t.string().optional(),
                "languagePair": t.proxy(renames["LanguageCodePairIn"]).optional(),
                "inputConfig": t.proxy(renames["GlossaryInputConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGet"] = translate.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "languageCodesSet": t.proxy(renames["LanguageCodesSetIn"]).optional(),
                "displayName": t.string().optional(),
                "languagePair": t.proxy(renames["LanguageCodePairIn"]).optional(),
                "inputConfig": t.proxy(renames["GlossaryInputConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesPatch"] = translate.patch(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "languageCodesSet": t.proxy(renames["LanguageCodesSetIn"]).optional(),
                "displayName": t.string().optional(),
                "languagePair": t.proxy(renames["LanguageCodePairIn"]).optional(),
                "inputConfig": t.proxy(renames["GlossaryInputConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGlossaryEntriesList"] = translate.post(
        "v3/{parent}/glossaryEntries",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "termsSet": t.proxy(renames["GlossaryTermsSetIn"]).optional(),
                "termsPair": t.proxy(renames["GlossaryTermsPairIn"]).optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GlossaryEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGlossaryEntriesPatch"] = translate.post(
        "v3/{parent}/glossaryEntries",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "termsSet": t.proxy(renames["GlossaryTermsSetIn"]).optional(),
                "termsPair": t.proxy(renames["GlossaryTermsPairIn"]).optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GlossaryEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGlossaryEntriesGet"] = translate.post(
        "v3/{parent}/glossaryEntries",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "termsSet": t.proxy(renames["GlossaryTermsSetIn"]).optional(),
                "termsPair": t.proxy(renames["GlossaryTermsPairIn"]).optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GlossaryEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGlossaryEntriesDelete"] = translate.post(
        "v3/{parent}/glossaryEntries",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "termsSet": t.proxy(renames["GlossaryTermsSetIn"]).optional(),
                "termsPair": t.proxy(renames["GlossaryTermsPairIn"]).optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GlossaryEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGlossaryEntriesCreate"] = translate.post(
        "v3/{parent}/glossaryEntries",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "termsSet": t.proxy(renames["GlossaryTermsSetIn"]).optional(),
                "termsPair": t.proxy(renames["GlossaryTermsPairIn"]).optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GlossaryEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="translate",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
