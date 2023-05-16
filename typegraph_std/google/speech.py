from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_speech() -> Import:
    speech = HTTPRuntime("https://speech.googleapis.com/")

    renames = {
        "ErrorResponse": "_speech_1_ErrorResponse",
        "StatusIn": "_speech_2_StatusIn",
        "StatusOut": "_speech_3_StatusOut",
        "RecognitionMetadataIn": "_speech_4_RecognitionMetadataIn",
        "RecognitionMetadataOut": "_speech_5_RecognitionMetadataOut",
        "ListPhraseSetResponseIn": "_speech_6_ListPhraseSetResponseIn",
        "ListPhraseSetResponseOut": "_speech_7_ListPhraseSetResponseOut",
        "TranscriptOutputConfigIn": "_speech_8_TranscriptOutputConfigIn",
        "TranscriptOutputConfigOut": "_speech_9_TranscriptOutputConfigOut",
        "EmptyIn": "_speech_10_EmptyIn",
        "EmptyOut": "_speech_11_EmptyOut",
        "RecognitionConfigIn": "_speech_12_RecognitionConfigIn",
        "RecognitionConfigOut": "_speech_13_RecognitionConfigOut",
        "PhraseIn": "_speech_14_PhraseIn",
        "PhraseOut": "_speech_15_PhraseOut",
        "SpeechRecognitionResultIn": "_speech_16_SpeechRecognitionResultIn",
        "SpeechRecognitionResultOut": "_speech_17_SpeechRecognitionResultOut",
        "ListOperationsResponseIn": "_speech_18_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_speech_19_ListOperationsResponseOut",
        "OperationIn": "_speech_20_OperationIn",
        "OperationOut": "_speech_21_OperationOut",
        "SpeechContextIn": "_speech_22_SpeechContextIn",
        "SpeechContextOut": "_speech_23_SpeechContextOut",
        "SpeechRecognitionAlternativeIn": "_speech_24_SpeechRecognitionAlternativeIn",
        "SpeechRecognitionAlternativeOut": "_speech_25_SpeechRecognitionAlternativeOut",
        "LongRunningRecognizeRequestIn": "_speech_26_LongRunningRecognizeRequestIn",
        "LongRunningRecognizeRequestOut": "_speech_27_LongRunningRecognizeRequestOut",
        "ABNFGrammarIn": "_speech_28_ABNFGrammarIn",
        "ABNFGrammarOut": "_speech_29_ABNFGrammarOut",
        "WordInfoIn": "_speech_30_WordInfoIn",
        "WordInfoOut": "_speech_31_WordInfoOut",
        "LongRunningRecognizeMetadataIn": "_speech_32_LongRunningRecognizeMetadataIn",
        "LongRunningRecognizeMetadataOut": "_speech_33_LongRunningRecognizeMetadataOut",
        "RecognitionAudioIn": "_speech_34_RecognitionAudioIn",
        "RecognitionAudioOut": "_speech_35_RecognitionAudioOut",
        "CreatePhraseSetRequestIn": "_speech_36_CreatePhraseSetRequestIn",
        "CreatePhraseSetRequestOut": "_speech_37_CreatePhraseSetRequestOut",
        "SpeakerDiarizationConfigIn": "_speech_38_SpeakerDiarizationConfigIn",
        "SpeakerDiarizationConfigOut": "_speech_39_SpeakerDiarizationConfigOut",
        "RecognizeResponseIn": "_speech_40_RecognizeResponseIn",
        "RecognizeResponseOut": "_speech_41_RecognizeResponseOut",
        "RecognizeRequestIn": "_speech_42_RecognizeRequestIn",
        "RecognizeRequestOut": "_speech_43_RecognizeRequestOut",
        "CustomClassIn": "_speech_44_CustomClassIn",
        "CustomClassOut": "_speech_45_CustomClassOut",
        "PhraseSetIn": "_speech_46_PhraseSetIn",
        "PhraseSetOut": "_speech_47_PhraseSetOut",
        "CreateCustomClassRequestIn": "_speech_48_CreateCustomClassRequestIn",
        "CreateCustomClassRequestOut": "_speech_49_CreateCustomClassRequestOut",
        "LongRunningRecognizeResponseIn": "_speech_50_LongRunningRecognizeResponseIn",
        "LongRunningRecognizeResponseOut": "_speech_51_LongRunningRecognizeResponseOut",
        "SpeechAdaptationIn": "_speech_52_SpeechAdaptationIn",
        "SpeechAdaptationOut": "_speech_53_SpeechAdaptationOut",
        "SpeechAdaptationInfoIn": "_speech_54_SpeechAdaptationInfoIn",
        "SpeechAdaptationInfoOut": "_speech_55_SpeechAdaptationInfoOut",
        "ClassItemIn": "_speech_56_ClassItemIn",
        "ClassItemOut": "_speech_57_ClassItemOut",
        "ListCustomClassesResponseIn": "_speech_58_ListCustomClassesResponseIn",
        "ListCustomClassesResponseOut": "_speech_59_ListCustomClassesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["RecognitionMetadataIn"] = t.struct(
        {
            "microphoneDistance": t.string().optional(),
            "recordingDeviceName": t.string().optional(),
            "recordingDeviceType": t.string().optional(),
            "audioTopic": t.string().optional(),
            "industryNaicsCodeOfAudio": t.integer().optional(),
            "originalMediaType": t.string().optional(),
            "interactionType": t.string().optional(),
            "originalMimeType": t.string().optional(),
        }
    ).named(renames["RecognitionMetadataIn"])
    types["RecognitionMetadataOut"] = t.struct(
        {
            "microphoneDistance": t.string().optional(),
            "recordingDeviceName": t.string().optional(),
            "recordingDeviceType": t.string().optional(),
            "audioTopic": t.string().optional(),
            "industryNaicsCodeOfAudio": t.integer().optional(),
            "originalMediaType": t.string().optional(),
            "interactionType": t.string().optional(),
            "originalMimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecognitionMetadataOut"])
    types["ListPhraseSetResponseIn"] = t.struct(
        {
            "phraseSets": t.array(t.proxy(renames["PhraseSetIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPhraseSetResponseIn"])
    types["ListPhraseSetResponseOut"] = t.struct(
        {
            "phraseSets": t.array(t.proxy(renames["PhraseSetOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPhraseSetResponseOut"])
    types["TranscriptOutputConfigIn"] = t.struct(
        {"gcsUri": t.string().optional()}
    ).named(renames["TranscriptOutputConfigIn"])
    types["TranscriptOutputConfigOut"] = t.struct(
        {
            "gcsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranscriptOutputConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["RecognitionConfigIn"] = t.struct(
        {
            "diarizationConfig": t.proxy(
                renames["SpeakerDiarizationConfigIn"]
            ).optional(),
            "profanityFilter": t.boolean().optional(),
            "adaptation": t.proxy(renames["SpeechAdaptationIn"]).optional(),
            "audioChannelCount": t.integer().optional(),
            "enableWordConfidence": t.boolean().optional(),
            "enableSeparateRecognitionPerChannel": t.boolean().optional(),
            "languageCode": t.string(),
            "useEnhanced": t.boolean().optional(),
            "enableAutomaticPunctuation": t.boolean().optional(),
            "enableSpokenPunctuation": t.boolean().optional(),
            "metadata": t.proxy(renames["RecognitionMetadataIn"]).optional(),
            "sampleRateHertz": t.integer().optional(),
            "enableSpokenEmojis": t.boolean().optional(),
            "encoding": t.string().optional(),
            "alternativeLanguageCodes": t.array(t.string()).optional(),
            "enableWordTimeOffsets": t.boolean().optional(),
            "maxAlternatives": t.integer().optional(),
            "speechContexts": t.array(t.proxy(renames["SpeechContextIn"])).optional(),
            "model": t.string().optional(),
        }
    ).named(renames["RecognitionConfigIn"])
    types["RecognitionConfigOut"] = t.struct(
        {
            "diarizationConfig": t.proxy(
                renames["SpeakerDiarizationConfigOut"]
            ).optional(),
            "profanityFilter": t.boolean().optional(),
            "adaptation": t.proxy(renames["SpeechAdaptationOut"]).optional(),
            "audioChannelCount": t.integer().optional(),
            "enableWordConfidence": t.boolean().optional(),
            "enableSeparateRecognitionPerChannel": t.boolean().optional(),
            "languageCode": t.string(),
            "useEnhanced": t.boolean().optional(),
            "enableAutomaticPunctuation": t.boolean().optional(),
            "enableSpokenPunctuation": t.boolean().optional(),
            "metadata": t.proxy(renames["RecognitionMetadataOut"]).optional(),
            "sampleRateHertz": t.integer().optional(),
            "enableSpokenEmojis": t.boolean().optional(),
            "encoding": t.string().optional(),
            "alternativeLanguageCodes": t.array(t.string()).optional(),
            "enableWordTimeOffsets": t.boolean().optional(),
            "maxAlternatives": t.integer().optional(),
            "speechContexts": t.array(t.proxy(renames["SpeechContextOut"])).optional(),
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecognitionConfigOut"])
    types["PhraseIn"] = t.struct(
        {"value": t.string().optional(), "boost": t.number().optional()}
    ).named(renames["PhraseIn"])
    types["PhraseOut"] = t.struct(
        {
            "value": t.string().optional(),
            "boost": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhraseOut"])
    types["SpeechRecognitionResultIn"] = t.struct(
        {
            "alternatives": t.array(
                t.proxy(renames["SpeechRecognitionAlternativeIn"])
            ).optional(),
            "resultEndTime": t.string().optional(),
            "channelTag": t.integer().optional(),
        }
    ).named(renames["SpeechRecognitionResultIn"])
    types["SpeechRecognitionResultOut"] = t.struct(
        {
            "alternatives": t.array(
                t.proxy(renames["SpeechRecognitionAlternativeOut"])
            ).optional(),
            "resultEndTime": t.string().optional(),
            "channelTag": t.integer().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpeechRecognitionResultOut"])
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
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["SpeechContextIn"] = t.struct(
        {"boost": t.number().optional(), "phrases": t.array(t.string()).optional()}
    ).named(renames["SpeechContextIn"])
    types["SpeechContextOut"] = t.struct(
        {
            "boost": t.number().optional(),
            "phrases": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpeechContextOut"])
    types["SpeechRecognitionAlternativeIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "words": t.array(t.proxy(renames["WordInfoIn"])).optional(),
            "transcript": t.string().optional(),
        }
    ).named(renames["SpeechRecognitionAlternativeIn"])
    types["SpeechRecognitionAlternativeOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "words": t.array(t.proxy(renames["WordInfoOut"])).optional(),
            "transcript": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpeechRecognitionAlternativeOut"])
    types["LongRunningRecognizeRequestIn"] = t.struct(
        {
            "outputConfig": t.proxy(renames["TranscriptOutputConfigIn"]).optional(),
            "audio": t.proxy(renames["RecognitionAudioIn"]),
            "config": t.proxy(renames["RecognitionConfigIn"]),
        }
    ).named(renames["LongRunningRecognizeRequestIn"])
    types["LongRunningRecognizeRequestOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["TranscriptOutputConfigOut"]).optional(),
            "audio": t.proxy(renames["RecognitionAudioOut"]),
            "config": t.proxy(renames["RecognitionConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningRecognizeRequestOut"])
    types["ABNFGrammarIn"] = t.struct(
        {"abnfStrings": t.array(t.string()).optional()}
    ).named(renames["ABNFGrammarIn"])
    types["ABNFGrammarOut"] = t.struct(
        {
            "abnfStrings": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ABNFGrammarOut"])
    types["WordInfoIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "word": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["WordInfoIn"])
    types["WordInfoOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "word": t.string().optional(),
            "startTime": t.string().optional(),
            "speakerLabel": t.string().optional(),
            "endTime": t.string().optional(),
            "speakerTag": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WordInfoOut"])
    types["LongRunningRecognizeMetadataIn"] = t.struct(
        {
            "lastUpdateTime": t.string().optional(),
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
        }
    ).named(renames["LongRunningRecognizeMetadataIn"])
    types["LongRunningRecognizeMetadataOut"] = t.struct(
        {
            "lastUpdateTime": t.string().optional(),
            "startTime": t.string().optional(),
            "uri": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningRecognizeMetadataOut"])
    types["RecognitionAudioIn"] = t.struct(
        {"content": t.string().optional(), "uri": t.string().optional()}
    ).named(renames["RecognitionAudioIn"])
    types["RecognitionAudioOut"] = t.struct(
        {
            "content": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecognitionAudioOut"])
    types["CreatePhraseSetRequestIn"] = t.struct(
        {"phraseSetId": t.string(), "phraseSet": t.proxy(renames["PhraseSetIn"])}
    ).named(renames["CreatePhraseSetRequestIn"])
    types["CreatePhraseSetRequestOut"] = t.struct(
        {
            "phraseSetId": t.string(),
            "phraseSet": t.proxy(renames["PhraseSetOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreatePhraseSetRequestOut"])
    types["SpeakerDiarizationConfigIn"] = t.struct(
        {
            "maxSpeakerCount": t.integer().optional(),
            "minSpeakerCount": t.integer().optional(),
            "enableSpeakerDiarization": t.boolean().optional(),
        }
    ).named(renames["SpeakerDiarizationConfigIn"])
    types["SpeakerDiarizationConfigOut"] = t.struct(
        {
            "speakerTag": t.integer().optional(),
            "maxSpeakerCount": t.integer().optional(),
            "minSpeakerCount": t.integer().optional(),
            "enableSpeakerDiarization": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpeakerDiarizationConfigOut"])
    types["RecognizeResponseIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "totalBilledTime": t.string().optional(),
            "results": t.array(
                t.proxy(renames["SpeechRecognitionResultIn"])
            ).optional(),
            "speechAdaptationInfo": t.proxy(
                renames["SpeechAdaptationInfoIn"]
            ).optional(),
        }
    ).named(renames["RecognizeResponseIn"])
    types["RecognizeResponseOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "totalBilledTime": t.string().optional(),
            "results": t.array(
                t.proxy(renames["SpeechRecognitionResultOut"])
            ).optional(),
            "speechAdaptationInfo": t.proxy(
                renames["SpeechAdaptationInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecognizeResponseOut"])
    types["RecognizeRequestIn"] = t.struct(
        {
            "audio": t.proxy(renames["RecognitionAudioIn"]),
            "config": t.proxy(renames["RecognitionConfigIn"]),
        }
    ).named(renames["RecognizeRequestIn"])
    types["RecognizeRequestOut"] = t.struct(
        {
            "audio": t.proxy(renames["RecognitionAudioOut"]),
            "config": t.proxy(renames["RecognitionConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecognizeRequestOut"])
    types["CustomClassIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ClassItemIn"])).optional(),
            "name": t.string().optional(),
            "customClassId": t.string().optional(),
        }
    ).named(renames["CustomClassIn"])
    types["CustomClassOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ClassItemOut"])).optional(),
            "name": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "kmsKeyVersionName": t.string().optional(),
            "customClassId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomClassOut"])
    types["PhraseSetIn"] = t.struct(
        {
            "name": t.string().optional(),
            "boost": t.number().optional(),
            "phrases": t.array(t.proxy(renames["PhraseIn"])).optional(),
        }
    ).named(renames["PhraseSetIn"])
    types["PhraseSetOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "name": t.string().optional(),
            "boost": t.number().optional(),
            "kmsKeyVersionName": t.string().optional(),
            "phrases": t.array(t.proxy(renames["PhraseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhraseSetOut"])
    types["CreateCustomClassRequestIn"] = t.struct(
        {"customClass": t.proxy(renames["CustomClassIn"]), "customClassId": t.string()}
    ).named(renames["CreateCustomClassRequestIn"])
    types["CreateCustomClassRequestOut"] = t.struct(
        {
            "customClass": t.proxy(renames["CustomClassOut"]),
            "customClassId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateCustomClassRequestOut"])
    types["LongRunningRecognizeResponseIn"] = t.struct(
        {
            "outputError": t.proxy(renames["StatusIn"]).optional(),
            "totalBilledTime": t.string().optional(),
            "requestId": t.string().optional(),
            "outputConfig": t.proxy(renames["TranscriptOutputConfigIn"]).optional(),
            "speechAdaptationInfo": t.proxy(
                renames["SpeechAdaptationInfoIn"]
            ).optional(),
            "results": t.array(
                t.proxy(renames["SpeechRecognitionResultIn"])
            ).optional(),
        }
    ).named(renames["LongRunningRecognizeResponseIn"])
    types["LongRunningRecognizeResponseOut"] = t.struct(
        {
            "outputError": t.proxy(renames["StatusOut"]).optional(),
            "totalBilledTime": t.string().optional(),
            "requestId": t.string().optional(),
            "outputConfig": t.proxy(renames["TranscriptOutputConfigOut"]).optional(),
            "speechAdaptationInfo": t.proxy(
                renames["SpeechAdaptationInfoOut"]
            ).optional(),
            "results": t.array(
                t.proxy(renames["SpeechRecognitionResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningRecognizeResponseOut"])
    types["SpeechAdaptationIn"] = t.struct(
        {
            "customClasses": t.array(t.proxy(renames["CustomClassIn"])).optional(),
            "abnfGrammar": t.proxy(renames["ABNFGrammarIn"]).optional(),
            "phraseSets": t.array(t.proxy(renames["PhraseSetIn"])).optional(),
            "phraseSetReferences": t.array(t.string()).optional(),
        }
    ).named(renames["SpeechAdaptationIn"])
    types["SpeechAdaptationOut"] = t.struct(
        {
            "customClasses": t.array(t.proxy(renames["CustomClassOut"])).optional(),
            "abnfGrammar": t.proxy(renames["ABNFGrammarOut"]).optional(),
            "phraseSets": t.array(t.proxy(renames["PhraseSetOut"])).optional(),
            "phraseSetReferences": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpeechAdaptationOut"])
    types["SpeechAdaptationInfoIn"] = t.struct(
        {
            "adaptationTimeout": t.boolean().optional(),
            "timeoutMessage": t.string().optional(),
        }
    ).named(renames["SpeechAdaptationInfoIn"])
    types["SpeechAdaptationInfoOut"] = t.struct(
        {
            "adaptationTimeout": t.boolean().optional(),
            "timeoutMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpeechAdaptationInfoOut"])
    types["ClassItemIn"] = t.struct({"value": t.string().optional()}).named(
        renames["ClassItemIn"]
    )
    types["ClassItemOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClassItemOut"])
    types["ListCustomClassesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customClasses": t.array(t.proxy(renames["CustomClassIn"])).optional(),
        }
    ).named(renames["ListCustomClassesResponseIn"])
    types["ListCustomClassesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customClasses": t.array(t.proxy(renames["CustomClassOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCustomClassesResponseOut"])

    functions = {}
    functions["projectsLocationsCustomClassesDelete"] = speech.get(
        "v1/{parent}/customClasses",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomClassesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCustomClassesCreate"] = speech.get(
        "v1/{parent}/customClasses",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomClassesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCustomClassesGet"] = speech.get(
        "v1/{parent}/customClasses",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomClassesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCustomClassesPatch"] = speech.get(
        "v1/{parent}/customClasses",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomClassesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCustomClassesList"] = speech.get(
        "v1/{parent}/customClasses",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomClassesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPhraseSetsCreate"] = speech.get(
        "v1/{parent}/phraseSets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPhraseSetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPhraseSetsDelete"] = speech.get(
        "v1/{parent}/phraseSets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPhraseSetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPhraseSetsPatch"] = speech.get(
        "v1/{parent}/phraseSets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPhraseSetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPhraseSetsGet"] = speech.get(
        "v1/{parent}/phraseSets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPhraseSetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPhraseSetsList"] = speech.get(
        "v1/{parent}/phraseSets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPhraseSetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["speechRecognize"] = speech.post(
        "v1/speech:longrunningrecognize",
        t.struct(
            {
                "outputConfig": t.proxy(renames["TranscriptOutputConfigIn"]).optional(),
                "audio": t.proxy(renames["RecognitionAudioIn"]),
                "config": t.proxy(renames["RecognitionConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["speechLongrunningrecognize"] = speech.post(
        "v1/speech:longrunningrecognize",
        t.struct(
            {
                "outputConfig": t.proxy(renames["TranscriptOutputConfigIn"]).optional(),
                "audio": t.proxy(renames["RecognitionAudioIn"]),
                "config": t.proxy(renames["RecognitionConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = speech.get(
        "v1/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = speech.get(
        "v1/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
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
        importer="speech", renames=renames, types=Box(types), functions=Box(functions)
    )
