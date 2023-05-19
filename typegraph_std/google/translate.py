from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_translate() -> Import:
    translate = HTTPRuntime("https://translation.googleapis.com/")

    renames = {
        "ErrorResponse": "_translate_1_ErrorResponse",
        "ExampleIn": "_translate_2_ExampleIn",
        "ExampleOut": "_translate_3_ExampleOut",
        "GcsDestinationIn": "_translate_4_GcsDestinationIn",
        "GcsDestinationOut": "_translate_5_GcsDestinationOut",
        "EmptyIn": "_translate_6_EmptyIn",
        "EmptyOut": "_translate_7_EmptyOut",
        "ExportDataRequestIn": "_translate_8_ExportDataRequestIn",
        "ExportDataRequestOut": "_translate_9_ExportDataRequestOut",
        "LanguageCodePairIn": "_translate_10_LanguageCodePairIn",
        "LanguageCodePairOut": "_translate_11_LanguageCodePairOut",
        "TranslateTextGlossaryConfigIn": "_translate_12_TranslateTextGlossaryConfigIn",
        "TranslateTextGlossaryConfigOut": "_translate_13_TranslateTextGlossaryConfigOut",
        "GlossaryTermsSetIn": "_translate_14_GlossaryTermsSetIn",
        "GlossaryTermsSetOut": "_translate_15_GlossaryTermsSetOut",
        "ListLocationsResponseIn": "_translate_16_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_translate_17_ListLocationsResponseOut",
        "BatchTranslateDocumentRequestIn": "_translate_18_BatchTranslateDocumentRequestIn",
        "BatchTranslateDocumentRequestOut": "_translate_19_BatchTranslateDocumentRequestOut",
        "ListExamplesResponseIn": "_translate_20_ListExamplesResponseIn",
        "ListExamplesResponseOut": "_translate_21_ListExamplesResponseOut",
        "GlossaryTermIn": "_translate_22_GlossaryTermIn",
        "GlossaryTermOut": "_translate_23_GlossaryTermOut",
        "LocationIn": "_translate_24_LocationIn",
        "LocationOut": "_translate_25_LocationOut",
        "OutputConfigIn": "_translate_26_OutputConfigIn",
        "OutputConfigOut": "_translate_27_OutputConfigOut",
        "StatusIn": "_translate_28_StatusIn",
        "StatusOut": "_translate_29_StatusOut",
        "TranslationIn": "_translate_30_TranslationIn",
        "TranslationOut": "_translate_31_TranslationOut",
        "GlossaryIn": "_translate_32_GlossaryIn",
        "GlossaryOut": "_translate_33_GlossaryOut",
        "ListGlossariesResponseIn": "_translate_34_ListGlossariesResponseIn",
        "ListGlossariesResponseOut": "_translate_35_ListGlossariesResponseOut",
        "TranslateTextRequestIn": "_translate_36_TranslateTextRequestIn",
        "TranslateTextRequestOut": "_translate_37_TranslateTextRequestOut",
        "GcsOutputDestinationIn": "_translate_38_GcsOutputDestinationIn",
        "GcsOutputDestinationOut": "_translate_39_GcsOutputDestinationOut",
        "ListModelsResponseIn": "_translate_40_ListModelsResponseIn",
        "ListModelsResponseOut": "_translate_41_ListModelsResponseOut",
        "DetectLanguageResponseIn": "_translate_42_DetectLanguageResponseIn",
        "DetectLanguageResponseOut": "_translate_43_DetectLanguageResponseOut",
        "TranslateDocumentRequestIn": "_translate_44_TranslateDocumentRequestIn",
        "TranslateDocumentRequestOut": "_translate_45_TranslateDocumentRequestOut",
        "SupportedLanguagesIn": "_translate_46_SupportedLanguagesIn",
        "SupportedLanguagesOut": "_translate_47_SupportedLanguagesOut",
        "GlossaryEntryIn": "_translate_48_GlossaryEntryIn",
        "GlossaryEntryOut": "_translate_49_GlossaryEntryOut",
        "OperationIn": "_translate_50_OperationIn",
        "OperationOut": "_translate_51_OperationOut",
        "ListOperationsResponseIn": "_translate_52_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_translate_53_ListOperationsResponseOut",
        "ImportDataRequestIn": "_translate_54_ImportDataRequestIn",
        "ImportDataRequestOut": "_translate_55_ImportDataRequestOut",
        "GcsInputSourceIn": "_translate_56_GcsInputSourceIn",
        "GcsInputSourceOut": "_translate_57_GcsInputSourceOut",
        "ModelIn": "_translate_58_ModelIn",
        "ModelOut": "_translate_59_ModelOut",
        "GcsSourceIn": "_translate_60_GcsSourceIn",
        "GcsSourceOut": "_translate_61_GcsSourceOut",
        "TranslateTextResponseIn": "_translate_62_TranslateTextResponseIn",
        "TranslateTextResponseOut": "_translate_63_TranslateTextResponseOut",
        "BatchTranslateTextRequestIn": "_translate_64_BatchTranslateTextRequestIn",
        "BatchTranslateTextRequestOut": "_translate_65_BatchTranslateTextRequestOut",
        "DatasetInputConfigIn": "_translate_66_DatasetInputConfigIn",
        "DatasetInputConfigOut": "_translate_67_DatasetInputConfigOut",
        "DocumentTranslationIn": "_translate_68_DocumentTranslationIn",
        "DocumentTranslationOut": "_translate_69_DocumentTranslationOut",
        "BatchDocumentInputConfigIn": "_translate_70_BatchDocumentInputConfigIn",
        "BatchDocumentInputConfigOut": "_translate_71_BatchDocumentInputConfigOut",
        "DocumentInputConfigIn": "_translate_72_DocumentInputConfigIn",
        "DocumentInputConfigOut": "_translate_73_DocumentInputConfigOut",
        "InputConfigIn": "_translate_74_InputConfigIn",
        "InputConfigOut": "_translate_75_InputConfigOut",
        "SupportedLanguageIn": "_translate_76_SupportedLanguageIn",
        "SupportedLanguageOut": "_translate_77_SupportedLanguageOut",
        "TranslateDocumentResponseIn": "_translate_78_TranslateDocumentResponseIn",
        "TranslateDocumentResponseOut": "_translate_79_TranslateDocumentResponseOut",
        "ListDatasetsResponseIn": "_translate_80_ListDatasetsResponseIn",
        "ListDatasetsResponseOut": "_translate_81_ListDatasetsResponseOut",
        "DocumentOutputConfigIn": "_translate_82_DocumentOutputConfigIn",
        "DocumentOutputConfigOut": "_translate_83_DocumentOutputConfigOut",
        "LanguageCodesSetIn": "_translate_84_LanguageCodesSetIn",
        "LanguageCodesSetOut": "_translate_85_LanguageCodesSetOut",
        "GlossaryInputConfigIn": "_translate_86_GlossaryInputConfigIn",
        "GlossaryInputConfigOut": "_translate_87_GlossaryInputConfigOut",
        "CancelOperationRequestIn": "_translate_88_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_translate_89_CancelOperationRequestOut",
        "DatasetIn": "_translate_90_DatasetIn",
        "DatasetOut": "_translate_91_DatasetOut",
        "GlossaryTermsPairIn": "_translate_92_GlossaryTermsPairIn",
        "GlossaryTermsPairOut": "_translate_93_GlossaryTermsPairOut",
        "DetectLanguageRequestIn": "_translate_94_DetectLanguageRequestIn",
        "DetectLanguageRequestOut": "_translate_95_DetectLanguageRequestOut",
        "DatasetOutputConfigIn": "_translate_96_DatasetOutputConfigIn",
        "DatasetOutputConfigOut": "_translate_97_DatasetOutputConfigOut",
        "InputFileIn": "_translate_98_InputFileIn",
        "InputFileOut": "_translate_99_InputFileOut",
        "ListGlossaryEntriesResponseIn": "_translate_100_ListGlossaryEntriesResponseIn",
        "ListGlossaryEntriesResponseOut": "_translate_101_ListGlossaryEntriesResponseOut",
        "BatchDocumentOutputConfigIn": "_translate_102_BatchDocumentOutputConfigIn",
        "BatchDocumentOutputConfigOut": "_translate_103_BatchDocumentOutputConfigOut",
        "WaitOperationRequestIn": "_translate_104_WaitOperationRequestIn",
        "WaitOperationRequestOut": "_translate_105_WaitOperationRequestOut",
        "DetectedLanguageIn": "_translate_106_DetectedLanguageIn",
        "DetectedLanguageOut": "_translate_107_DetectedLanguageOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ExampleIn"] = t.struct(
        {"sourceText": t.string().optional(), "targetText": t.string().optional()}
    ).named(renames["ExampleIn"])
    types["ExampleOut"] = t.struct(
        {
            "sourceText": t.string().optional(),
            "usage": t.string().optional(),
            "name": t.string().optional(),
            "targetText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExampleOut"])
    types["GcsDestinationIn"] = t.struct({"outputUriPrefix": t.string()}).named(
        renames["GcsDestinationIn"]
    )
    types["GcsDestinationOut"] = t.struct(
        {
            "outputUriPrefix": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsDestinationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ExportDataRequestIn"] = t.struct(
        {"outputConfig": t.proxy(renames["DatasetOutputConfigIn"])}
    ).named(renames["ExportDataRequestIn"])
    types["ExportDataRequestOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["DatasetOutputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportDataRequestOut"])
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
    types["GlossaryTermsSetIn"] = t.struct(
        {"terms": t.array(t.proxy(renames["GlossaryTermIn"])).optional()}
    ).named(renames["GlossaryTermsSetIn"])
    types["GlossaryTermsSetOut"] = t.struct(
        {
            "terms": t.array(t.proxy(renames["GlossaryTermOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryTermsSetOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["BatchTranslateDocumentRequestIn"] = t.struct(
        {
            "models": t.struct({"_": t.string().optional()}).optional(),
            "outputConfig": t.proxy(renames["BatchDocumentOutputConfigIn"]),
            "enableShadowRemovalNativePdf": t.boolean().optional(),
            "inputConfigs": t.array(t.proxy(renames["BatchDocumentInputConfigIn"])),
            "glossaries": t.struct({"_": t.string().optional()}).optional(),
            "customizedAttribution": t.string().optional(),
            "formatConversions": t.struct({"_": t.string().optional()}).optional(),
            "sourceLanguageCode": t.string(),
            "targetLanguageCodes": t.array(t.string()),
        }
    ).named(renames["BatchTranslateDocumentRequestIn"])
    types["BatchTranslateDocumentRequestOut"] = t.struct(
        {
            "models": t.struct({"_": t.string().optional()}).optional(),
            "outputConfig": t.proxy(renames["BatchDocumentOutputConfigOut"]),
            "enableShadowRemovalNativePdf": t.boolean().optional(),
            "inputConfigs": t.array(t.proxy(renames["BatchDocumentInputConfigOut"])),
            "glossaries": t.struct({"_": t.string().optional()}).optional(),
            "customizedAttribution": t.string().optional(),
            "formatConversions": t.struct({"_": t.string().optional()}).optional(),
            "sourceLanguageCode": t.string(),
            "targetLanguageCodes": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchTranslateDocumentRequestOut"])
    types["ListExamplesResponseIn"] = t.struct(
        {
            "examples": t.array(t.proxy(renames["ExampleIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListExamplesResponseIn"])
    types["ListExamplesResponseOut"] = t.struct(
        {
            "examples": t.array(t.proxy(renames["ExampleOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListExamplesResponseOut"])
    types["GlossaryTermIn"] = t.struct(
        {"text": t.string().optional(), "languageCode": t.string().optional()}
    ).named(renames["GlossaryTermIn"])
    types["GlossaryTermOut"] = t.struct(
        {
            "text": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryTermOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["OutputConfigIn"] = t.struct(
        {"gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional()}
    ).named(renames["OutputConfigIn"])
    types["OutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutputConfigOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["TranslationIn"] = t.struct(
        {
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigIn"]
            ).optional(),
            "model": t.string().optional(),
            "detectedLanguageCode": t.string().optional(),
            "translatedText": t.string().optional(),
        }
    ).named(renames["TranslationIn"])
    types["TranslationOut"] = t.struct(
        {
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigOut"]
            ).optional(),
            "model": t.string().optional(),
            "detectedLanguageCode": t.string().optional(),
            "translatedText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslationOut"])
    types["GlossaryIn"] = t.struct(
        {
            "languageCodesSet": t.proxy(renames["LanguageCodesSetIn"]).optional(),
            "displayName": t.string().optional(),
            "languagePair": t.proxy(renames["LanguageCodePairIn"]).optional(),
            "inputConfig": t.proxy(renames["GlossaryInputConfigIn"]),
            "name": t.string(),
        }
    ).named(renames["GlossaryIn"])
    types["GlossaryOut"] = t.struct(
        {
            "languageCodesSet": t.proxy(renames["LanguageCodesSetOut"]).optional(),
            "displayName": t.string().optional(),
            "languagePair": t.proxy(renames["LanguageCodePairOut"]).optional(),
            "entryCount": t.integer().optional(),
            "inputConfig": t.proxy(renames["GlossaryInputConfigOut"]),
            "endTime": t.string().optional(),
            "submitTime": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryOut"])
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
    types["TranslateTextRequestIn"] = t.struct(
        {
            "sourceLanguageCode": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "mimeType": t.string().optional(),
            "model": t.string().optional(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigIn"]
            ).optional(),
            "targetLanguageCode": t.string(),
            "contents": t.array(t.string()),
        }
    ).named(renames["TranslateTextRequestIn"])
    types["TranslateTextRequestOut"] = t.struct(
        {
            "sourceLanguageCode": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "mimeType": t.string().optional(),
            "model": t.string().optional(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigOut"]
            ).optional(),
            "targetLanguageCode": t.string(),
            "contents": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslateTextRequestOut"])
    types["GcsOutputDestinationIn"] = t.struct({"outputUriPrefix": t.string()}).named(
        renames["GcsOutputDestinationIn"]
    )
    types["GcsOutputDestinationOut"] = t.struct(
        {
            "outputUriPrefix": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsOutputDestinationOut"])
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
    types["DetectLanguageResponseIn"] = t.struct(
        {"languages": t.array(t.proxy(renames["DetectedLanguageIn"])).optional()}
    ).named(renames["DetectLanguageResponseIn"])
    types["DetectLanguageResponseOut"] = t.struct(
        {
            "languages": t.array(t.proxy(renames["DetectedLanguageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetectLanguageResponseOut"])
    types["TranslateDocumentRequestIn"] = t.struct(
        {
            "targetLanguageCode": t.string(),
            "documentInputConfig": t.proxy(renames["DocumentInputConfigIn"]),
            "sourceLanguageCode": t.string().optional(),
            "enableRotationCorrection": t.boolean().optional(),
            "model": t.string().optional(),
            "isTranslateNativePdfOnly": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "customizedAttribution": t.string().optional(),
            "documentOutputConfig": t.proxy(
                renames["DocumentOutputConfigIn"]
            ).optional(),
            "enableShadowRemovalNativePdf": t.boolean().optional(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigIn"]
            ).optional(),
        }
    ).named(renames["TranslateDocumentRequestIn"])
    types["TranslateDocumentRequestOut"] = t.struct(
        {
            "targetLanguageCode": t.string(),
            "documentInputConfig": t.proxy(renames["DocumentInputConfigOut"]),
            "sourceLanguageCode": t.string().optional(),
            "enableRotationCorrection": t.boolean().optional(),
            "model": t.string().optional(),
            "isTranslateNativePdfOnly": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "customizedAttribution": t.string().optional(),
            "documentOutputConfig": t.proxy(
                renames["DocumentOutputConfigOut"]
            ).optional(),
            "enableShadowRemovalNativePdf": t.boolean().optional(),
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslateDocumentRequestOut"])
    types["SupportedLanguagesIn"] = t.struct(
        {"languages": t.array(t.proxy(renames["SupportedLanguageIn"])).optional()}
    ).named(renames["SupportedLanguagesIn"])
    types["SupportedLanguagesOut"] = t.struct(
        {
            "languages": t.array(t.proxy(renames["SupportedLanguageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SupportedLanguagesOut"])
    types["GlossaryEntryIn"] = t.struct(
        {
            "termsPair": t.proxy(renames["GlossaryTermsPairIn"]).optional(),
            "termsSet": t.proxy(renames["GlossaryTermsSetIn"]).optional(),
            "name": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["GlossaryEntryIn"])
    types["GlossaryEntryOut"] = t.struct(
        {
            "termsPair": t.proxy(renames["GlossaryTermsPairOut"]).optional(),
            "termsSet": t.proxy(renames["GlossaryTermsSetOut"]).optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryEntryOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["ImportDataRequestIn"] = t.struct(
        {"inputConfig": t.proxy(renames["DatasetInputConfigIn"])}
    ).named(renames["ImportDataRequestIn"])
    types["ImportDataRequestOut"] = t.struct(
        {
            "inputConfig": t.proxy(renames["DatasetInputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportDataRequestOut"])
    types["GcsInputSourceIn"] = t.struct({"inputUri": t.string()}).named(
        renames["GcsInputSourceIn"]
    )
    types["GcsInputSourceOut"] = t.struct(
        {"inputUri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GcsInputSourceOut"])
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
            "trainExampleCount": t.integer().optional(),
            "createTime": t.string().optional(),
            "targetLanguageCode": t.string().optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "sourceLanguageCode": t.string().optional(),
            "name": t.string().optional(),
            "testExampleCount": t.integer().optional(),
            "validateExampleCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModelOut"])
    types["GcsSourceIn"] = t.struct({"inputUri": t.string()}).named(
        renames["GcsSourceIn"]
    )
    types["GcsSourceOut"] = t.struct(
        {"inputUri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GcsSourceOut"])
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
    types["BatchTranslateTextRequestIn"] = t.struct(
        {
            "inputConfigs": t.array(t.proxy(renames["InputConfigIn"])),
            "glossaries": t.struct({"_": t.string().optional()}).optional(),
            "models": t.struct({"_": t.string().optional()}).optional(),
            "sourceLanguageCode": t.string(),
            "targetLanguageCodes": t.array(t.string()),
            "outputConfig": t.proxy(renames["OutputConfigIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["BatchTranslateTextRequestIn"])
    types["BatchTranslateTextRequestOut"] = t.struct(
        {
            "inputConfigs": t.array(t.proxy(renames["InputConfigOut"])),
            "glossaries": t.struct({"_": t.string().optional()}).optional(),
            "models": t.struct({"_": t.string().optional()}).optional(),
            "sourceLanguageCode": t.string(),
            "targetLanguageCodes": t.array(t.string()),
            "outputConfig": t.proxy(renames["OutputConfigOut"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchTranslateTextRequestOut"])
    types["DatasetInputConfigIn"] = t.struct(
        {"inputFiles": t.array(t.proxy(renames["InputFileIn"])).optional()}
    ).named(renames["DatasetInputConfigIn"])
    types["DatasetInputConfigOut"] = t.struct(
        {
            "inputFiles": t.array(t.proxy(renames["InputFileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetInputConfigOut"])
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
    types["BatchDocumentInputConfigIn"] = t.struct(
        {"gcsSource": t.proxy(renames["GcsSourceIn"]).optional()}
    ).named(renames["BatchDocumentInputConfigIn"])
    types["BatchDocumentInputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDocumentInputConfigOut"])
    types["DocumentInputConfigIn"] = t.struct(
        {
            "content": t.string().optional(),
            "gcsSource": t.proxy(renames["GcsSourceIn"]).optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["DocumentInputConfigIn"])
    types["DocumentInputConfigOut"] = t.struct(
        {
            "content": t.string().optional(),
            "gcsSource": t.proxy(renames["GcsSourceOut"]).optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentInputConfigOut"])
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
    types["SupportedLanguageIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "supportSource": t.boolean().optional(),
            "supportTarget": t.boolean().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["SupportedLanguageIn"])
    types["SupportedLanguageOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "supportSource": t.boolean().optional(),
            "supportTarget": t.boolean().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SupportedLanguageOut"])
    types["TranslateDocumentResponseIn"] = t.struct(
        {
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigIn"]
            ).optional(),
            "model": t.string().optional(),
            "documentTranslation": t.proxy(renames["DocumentTranslationIn"]).optional(),
            "glossaryDocumentTranslation": t.proxy(
                renames["DocumentTranslationIn"]
            ).optional(),
        }
    ).named(renames["TranslateDocumentResponseIn"])
    types["TranslateDocumentResponseOut"] = t.struct(
        {
            "glossaryConfig": t.proxy(
                renames["TranslateTextGlossaryConfigOut"]
            ).optional(),
            "model": t.string().optional(),
            "documentTranslation": t.proxy(
                renames["DocumentTranslationOut"]
            ).optional(),
            "glossaryDocumentTranslation": t.proxy(
                renames["DocumentTranslationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranslateDocumentResponseOut"])
    types["ListDatasetsResponseIn"] = t.struct(
        {
            "datasets": t.array(t.proxy(renames["DatasetIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDatasetsResponseIn"])
    types["ListDatasetsResponseOut"] = t.struct(
        {
            "datasets": t.array(t.proxy(renames["DatasetOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDatasetsResponseOut"])
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
    types["LanguageCodesSetIn"] = t.struct(
        {"languageCodes": t.array(t.string()).optional()}
    ).named(renames["LanguageCodesSetIn"])
    types["LanguageCodesSetOut"] = t.struct(
        {
            "languageCodes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageCodesSetOut"])
    types["GlossaryInputConfigIn"] = t.struct(
        {"gcsSource": t.proxy(renames["GcsSourceIn"])}
    ).named(renames["GlossaryInputConfigIn"])
    types["GlossaryInputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlossaryInputConfigOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["DatasetIn"] = t.struct(
        {
            "targetLanguageCode": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "sourceLanguageCode": t.string().optional(),
        }
    ).named(renames["DatasetIn"])
    types["DatasetOut"] = t.struct(
        {
            "testExampleCount": t.integer().optional(),
            "targetLanguageCode": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "exampleCount": t.integer().optional(),
            "trainExampleCount": t.integer().optional(),
            "displayName": t.string().optional(),
            "validateExampleCount": t.integer().optional(),
            "sourceLanguageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetOut"])
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
    types["DetectLanguageRequestIn"] = t.struct(
        {
            "content": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "model": t.string().optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["DetectLanguageRequestIn"])
    types["DetectLanguageRequestOut"] = t.struct(
        {
            "content": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "model": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetectLanguageRequestOut"])
    types["DatasetOutputConfigIn"] = t.struct(
        {"gcsDestination": t.proxy(renames["GcsOutputDestinationIn"]).optional()}
    ).named(renames["DatasetOutputConfigIn"])
    types["DatasetOutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsOutputDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetOutputConfigOut"])
    types["InputFileIn"] = t.struct(
        {
            "usage": t.string().optional(),
            "gcsSource": t.proxy(renames["GcsInputSourceIn"]).optional(),
        }
    ).named(renames["InputFileIn"])
    types["InputFileOut"] = t.struct(
        {
            "usage": t.string().optional(),
            "gcsSource": t.proxy(renames["GcsInputSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputFileOut"])
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
    types["BatchDocumentOutputConfigIn"] = t.struct(
        {"gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional()}
    ).named(renames["BatchDocumentOutputConfigIn"])
    types["BatchDocumentOutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDocumentOutputConfigOut"])
    types["WaitOperationRequestIn"] = t.struct(
        {"timeout": t.string().optional()}
    ).named(renames["WaitOperationRequestIn"])
    types["WaitOperationRequestOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaitOperationRequestOut"])
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

    functions = {}
    functions["projectsGetSupportedLanguages"] = translate.post(
        "v3/{parent}:detectLanguage",
        t.struct(
            {
                "parent": t.string(),
                "content": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "model": t.string().optional(),
                "mimeType": t.string().optional(),
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
                "content": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "model": t.string().optional(),
                "mimeType": t.string().optional(),
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
                "content": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "model": t.string().optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DetectLanguageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = translate.post(
        "v3/{parent}:translateText",
        t.struct(
            {
                "parent": t.string(),
                "sourceLanguageCode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "model": t.string().optional(),
                "glossaryConfig": t.proxy(
                    renames["TranslateTextGlossaryConfigIn"]
                ).optional(),
                "targetLanguageCode": t.string(),
                "contents": t.array(t.string()),
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
                "sourceLanguageCode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "model": t.string().optional(),
                "glossaryConfig": t.proxy(
                    renames["TranslateTextGlossaryConfigIn"]
                ).optional(),
                "targetLanguageCode": t.string(),
                "contents": t.array(t.string()),
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
                "sourceLanguageCode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "model": t.string().optional(),
                "glossaryConfig": t.proxy(
                    renames["TranslateTextGlossaryConfigIn"]
                ).optional(),
                "targetLanguageCode": t.string(),
                "contents": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TranslateTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGetSupportedLanguages"] = translate.post(
        "v3/{parent}:translateText",
        t.struct(
            {
                "parent": t.string(),
                "sourceLanguageCode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "model": t.string().optional(),
                "glossaryConfig": t.proxy(
                    renames["TranslateTextGlossaryConfigIn"]
                ).optional(),
                "targetLanguageCode": t.string(),
                "contents": t.array(t.string()),
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
                "sourceLanguageCode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "model": t.string().optional(),
                "glossaryConfig": t.proxy(
                    renames["TranslateTextGlossaryConfigIn"]
                ).optional(),
                "targetLanguageCode": t.string(),
                "contents": t.array(t.string()),
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
                "sourceLanguageCode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "model": t.string().optional(),
                "glossaryConfig": t.proxy(
                    renames["TranslateTextGlossaryConfigIn"]
                ).optional(),
                "targetLanguageCode": t.string(),
                "contents": t.array(t.string()),
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
                "sourceLanguageCode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "model": t.string().optional(),
                "glossaryConfig": t.proxy(
                    renames["TranslateTextGlossaryConfigIn"]
                ).optional(),
                "targetLanguageCode": t.string(),
                "contents": t.array(t.string()),
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
                "sourceLanguageCode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "model": t.string().optional(),
                "glossaryConfig": t.proxy(
                    renames["TranslateTextGlossaryConfigIn"]
                ).optional(),
                "targetLanguageCode": t.string(),
                "contents": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TranslateTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsImportData"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsList"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsExportData"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsGet"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsCreate"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDelete"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsExamplesList"] = translate.get(
        "v3/{parent}/examples",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExamplesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesList"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesGet"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesPatch"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesCreate"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlossariesDelete"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
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
    functions["projectsLocationsGlossariesGlossaryEntriesPatch"] = translate.delete(
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
    functions["projectsLocationsModelsGet"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsModelsCreate"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsModelsList"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsModelsDelete"] = translate.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = translate.get(
        "v3/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsWait"] = translate.get(
        "v3/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = translate.get(
        "v3/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = translate.get(
        "v3/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = translate.get(
        "v3/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="translate",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
