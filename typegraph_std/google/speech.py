from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_speech():
    speech = HTTPRuntime("https://speech.googleapis.com/")

    renames = {
        "ErrorResponse": "_speech_1_ErrorResponse",
        "LongRunningRecognizeMetadataIn": "_speech_2_LongRunningRecognizeMetadataIn",
        "LongRunningRecognizeMetadataOut": "_speech_3_LongRunningRecognizeMetadataOut",
        "PhraseIn": "_speech_4_PhraseIn",
        "PhraseOut": "_speech_5_PhraseOut",
        "TranscriptOutputConfigIn": "_speech_6_TranscriptOutputConfigIn",
        "TranscriptOutputConfigOut": "_speech_7_TranscriptOutputConfigOut",
        "CreateCustomClassRequestIn": "_speech_8_CreateCustomClassRequestIn",
        "CreateCustomClassRequestOut": "_speech_9_CreateCustomClassRequestOut",
        "SpeechRecognitionAlternativeIn": "_speech_10_SpeechRecognitionAlternativeIn",
        "SpeechRecognitionAlternativeOut": "_speech_11_SpeechRecognitionAlternativeOut",
        "SpeechContextIn": "_speech_12_SpeechContextIn",
        "SpeechContextOut": "_speech_13_SpeechContextOut",
        "ListPhraseSetResponseIn": "_speech_14_ListPhraseSetResponseIn",
        "ListPhraseSetResponseOut": "_speech_15_ListPhraseSetResponseOut",
        "LongRunningRecognizeResponseIn": "_speech_16_LongRunningRecognizeResponseIn",
        "LongRunningRecognizeResponseOut": "_speech_17_LongRunningRecognizeResponseOut",
        "RecognizeResponseIn": "_speech_18_RecognizeResponseIn",
        "RecognizeResponseOut": "_speech_19_RecognizeResponseOut",
        "CreatePhraseSetRequestIn": "_speech_20_CreatePhraseSetRequestIn",
        "CreatePhraseSetRequestOut": "_speech_21_CreatePhraseSetRequestOut",
        "SpeechAdaptationIn": "_speech_22_SpeechAdaptationIn",
        "SpeechAdaptationOut": "_speech_23_SpeechAdaptationOut",
        "SpeechRecognitionResultIn": "_speech_24_SpeechRecognitionResultIn",
        "SpeechRecognitionResultOut": "_speech_25_SpeechRecognitionResultOut",
        "RecognitionAudioIn": "_speech_26_RecognitionAudioIn",
        "RecognitionAudioOut": "_speech_27_RecognitionAudioOut",
        "SpeechAdaptationInfoIn": "_speech_28_SpeechAdaptationInfoIn",
        "SpeechAdaptationInfoOut": "_speech_29_SpeechAdaptationInfoOut",
        "CustomClassIn": "_speech_30_CustomClassIn",
        "CustomClassOut": "_speech_31_CustomClassOut",
        "RecognitionMetadataIn": "_speech_32_RecognitionMetadataIn",
        "RecognitionMetadataOut": "_speech_33_RecognitionMetadataOut",
        "StatusIn": "_speech_34_StatusIn",
        "StatusOut": "_speech_35_StatusOut",
        "ClassItemIn": "_speech_36_ClassItemIn",
        "ClassItemOut": "_speech_37_ClassItemOut",
        "SpeakerDiarizationConfigIn": "_speech_38_SpeakerDiarizationConfigIn",
        "SpeakerDiarizationConfigOut": "_speech_39_SpeakerDiarizationConfigOut",
        "EmptyIn": "_speech_40_EmptyIn",
        "EmptyOut": "_speech_41_EmptyOut",
        "OperationIn": "_speech_42_OperationIn",
        "OperationOut": "_speech_43_OperationOut",
        "ListOperationsResponseIn": "_speech_44_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_speech_45_ListOperationsResponseOut",
        "RecognizeRequestIn": "_speech_46_RecognizeRequestIn",
        "RecognizeRequestOut": "_speech_47_RecognizeRequestOut",
        "ListCustomClassesResponseIn": "_speech_48_ListCustomClassesResponseIn",
        "ListCustomClassesResponseOut": "_speech_49_ListCustomClassesResponseOut",
        "PhraseSetIn": "_speech_50_PhraseSetIn",
        "PhraseSetOut": "_speech_51_PhraseSetOut",
        "LongRunningRecognizeRequestIn": "_speech_52_LongRunningRecognizeRequestIn",
        "LongRunningRecognizeRequestOut": "_speech_53_LongRunningRecognizeRequestOut",
        "ABNFGrammarIn": "_speech_54_ABNFGrammarIn",
        "ABNFGrammarOut": "_speech_55_ABNFGrammarOut",
        "WordInfoIn": "_speech_56_WordInfoIn",
        "WordInfoOut": "_speech_57_WordInfoOut",
        "RecognitionConfigIn": "_speech_58_RecognitionConfigIn",
        "RecognitionConfigOut": "_speech_59_RecognitionConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LongRunningRecognizeMetadataIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "lastUpdateTime": t.string().optional(),
        }
    ).named(renames["LongRunningRecognizeMetadataIn"])
    types["LongRunningRecognizeMetadataOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "lastUpdateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningRecognizeMetadataOut"])
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
    types["TranscriptOutputConfigIn"] = t.struct(
        {"gcsUri": t.string().optional()}
    ).named(renames["TranscriptOutputConfigIn"])
    types["TranscriptOutputConfigOut"] = t.struct(
        {
            "gcsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TranscriptOutputConfigOut"])
    types["CreateCustomClassRequestIn"] = t.struct(
        {"customClassId": t.string(), "customClass": t.proxy(renames["CustomClassIn"])}
    ).named(renames["CreateCustomClassRequestIn"])
    types["CreateCustomClassRequestOut"] = t.struct(
        {
            "customClassId": t.string(),
            "customClass": t.proxy(renames["CustomClassOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateCustomClassRequestOut"])
    types["SpeechRecognitionAlternativeIn"] = t.struct(
        {
            "words": t.array(t.proxy(renames["WordInfoIn"])).optional(),
            "confidence": t.number().optional(),
            "transcript": t.string().optional(),
        }
    ).named(renames["SpeechRecognitionAlternativeIn"])
    types["SpeechRecognitionAlternativeOut"] = t.struct(
        {
            "words": t.array(t.proxy(renames["WordInfoOut"])).optional(),
            "confidence": t.number().optional(),
            "transcript": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpeechRecognitionAlternativeOut"])
    types["SpeechContextIn"] = t.struct(
        {"phrases": t.array(t.string()).optional(), "boost": t.number().optional()}
    ).named(renames["SpeechContextIn"])
    types["SpeechContextOut"] = t.struct(
        {
            "phrases": t.array(t.string()).optional(),
            "boost": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpeechContextOut"])
    types["ListPhraseSetResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "phraseSets": t.array(t.proxy(renames["PhraseSetIn"])).optional(),
        }
    ).named(renames["ListPhraseSetResponseIn"])
    types["ListPhraseSetResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "phraseSets": t.array(t.proxy(renames["PhraseSetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPhraseSetResponseOut"])
    types["LongRunningRecognizeResponseIn"] = t.struct(
        {
            "speechAdaptationInfo": t.proxy(
                renames["SpeechAdaptationInfoIn"]
            ).optional(),
            "results": t.array(
                t.proxy(renames["SpeechRecognitionResultIn"])
            ).optional(),
            "outputError": t.proxy(renames["StatusIn"]).optional(),
            "totalBilledTime": t.string().optional(),
            "requestId": t.string().optional(),
            "outputConfig": t.proxy(renames["TranscriptOutputConfigIn"]).optional(),
        }
    ).named(renames["LongRunningRecognizeResponseIn"])
    types["LongRunningRecognizeResponseOut"] = t.struct(
        {
            "speechAdaptationInfo": t.proxy(
                renames["SpeechAdaptationInfoOut"]
            ).optional(),
            "results": t.array(
                t.proxy(renames["SpeechRecognitionResultOut"])
            ).optional(),
            "outputError": t.proxy(renames["StatusOut"]).optional(),
            "totalBilledTime": t.string().optional(),
            "requestId": t.string().optional(),
            "outputConfig": t.proxy(renames["TranscriptOutputConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningRecognizeResponseOut"])
    types["RecognizeResponseIn"] = t.struct(
        {
            "results": t.array(
                t.proxy(renames["SpeechRecognitionResultIn"])
            ).optional(),
            "speechAdaptationInfo": t.proxy(
                renames["SpeechAdaptationInfoIn"]
            ).optional(),
            "requestId": t.string().optional(),
            "totalBilledTime": t.string().optional(),
        }
    ).named(renames["RecognizeResponseIn"])
    types["RecognizeResponseOut"] = t.struct(
        {
            "results": t.array(
                t.proxy(renames["SpeechRecognitionResultOut"])
            ).optional(),
            "speechAdaptationInfo": t.proxy(
                renames["SpeechAdaptationInfoOut"]
            ).optional(),
            "requestId": t.string().optional(),
            "totalBilledTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecognizeResponseOut"])
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
    types["SpeechAdaptationIn"] = t.struct(
        {
            "phraseSets": t.array(t.proxy(renames["PhraseSetIn"])).optional(),
            "customClasses": t.array(t.proxy(renames["CustomClassIn"])).optional(),
            "phraseSetReferences": t.array(t.string()).optional(),
            "abnfGrammar": t.proxy(renames["ABNFGrammarIn"]).optional(),
        }
    ).named(renames["SpeechAdaptationIn"])
    types["SpeechAdaptationOut"] = t.struct(
        {
            "phraseSets": t.array(t.proxy(renames["PhraseSetOut"])).optional(),
            "customClasses": t.array(t.proxy(renames["CustomClassOut"])).optional(),
            "phraseSetReferences": t.array(t.string()).optional(),
            "abnfGrammar": t.proxy(renames["ABNFGrammarOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpeechAdaptationOut"])
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
            "languageCode": t.string().optional(),
            "resultEndTime": t.string().optional(),
            "channelTag": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpeechRecognitionResultOut"])
    types["RecognitionAudioIn"] = t.struct(
        {"uri": t.string().optional(), "content": t.string().optional()}
    ).named(renames["RecognitionAudioIn"])
    types["RecognitionAudioOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecognitionAudioOut"])
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
    types["CustomClassIn"] = t.struct(
        {
            "name": t.string().optional(),
            "customClassId": t.string().optional(),
            "items": t.array(t.proxy(renames["ClassItemIn"])).optional(),
        }
    ).named(renames["CustomClassIn"])
    types["CustomClassOut"] = t.struct(
        {
            "name": t.string().optional(),
            "kmsKeyVersionName": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "customClassId": t.string().optional(),
            "items": t.array(t.proxy(renames["ClassItemOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomClassOut"])
    types["RecognitionMetadataIn"] = t.struct(
        {
            "recordingDeviceType": t.string().optional(),
            "originalMediaType": t.string().optional(),
            "interactionType": t.string().optional(),
            "originalMimeType": t.string().optional(),
            "audioTopic": t.string().optional(),
            "recordingDeviceName": t.string().optional(),
            "microphoneDistance": t.string().optional(),
            "industryNaicsCodeOfAudio": t.integer().optional(),
        }
    ).named(renames["RecognitionMetadataIn"])
    types["RecognitionMetadataOut"] = t.struct(
        {
            "recordingDeviceType": t.string().optional(),
            "originalMediaType": t.string().optional(),
            "interactionType": t.string().optional(),
            "originalMimeType": t.string().optional(),
            "audioTopic": t.string().optional(),
            "recordingDeviceName": t.string().optional(),
            "microphoneDistance": t.string().optional(),
            "industryNaicsCodeOfAudio": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecognitionMetadataOut"])
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
    types["ClassItemIn"] = t.struct({"value": t.string().optional()}).named(
        renames["ClassItemIn"]
    )
    types["ClassItemOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClassItemOut"])
    types["SpeakerDiarizationConfigIn"] = t.struct(
        {
            "minSpeakerCount": t.integer().optional(),
            "enableSpeakerDiarization": t.boolean().optional(),
            "maxSpeakerCount": t.integer().optional(),
        }
    ).named(renames["SpeakerDiarizationConfigIn"])
    types["SpeakerDiarizationConfigOut"] = t.struct(
        {
            "minSpeakerCount": t.integer().optional(),
            "speakerTag": t.integer().optional(),
            "enableSpeakerDiarization": t.boolean().optional(),
            "maxSpeakerCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpeakerDiarizationConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
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
    types["PhraseSetIn"] = t.struct(
        {
            "name": t.string().optional(),
            "boost": t.number().optional(),
            "phrases": t.array(t.proxy(renames["PhraseIn"])).optional(),
        }
    ).named(renames["PhraseSetIn"])
    types["PhraseSetOut"] = t.struct(
        {
            "name": t.string().optional(),
            "boost": t.number().optional(),
            "phrases": t.array(t.proxy(renames["PhraseOut"])).optional(),
            "kmsKeyName": t.string().optional(),
            "kmsKeyVersionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhraseSetOut"])
    types["LongRunningRecognizeRequestIn"] = t.struct(
        {
            "audio": t.proxy(renames["RecognitionAudioIn"]),
            "outputConfig": t.proxy(renames["TranscriptOutputConfigIn"]).optional(),
            "config": t.proxy(renames["RecognitionConfigIn"]),
        }
    ).named(renames["LongRunningRecognizeRequestIn"])
    types["LongRunningRecognizeRequestOut"] = t.struct(
        {
            "audio": t.proxy(renames["RecognitionAudioOut"]),
            "outputConfig": t.proxy(renames["TranscriptOutputConfigOut"]).optional(),
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
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "word": t.string().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["WordInfoIn"])
    types["WordInfoOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "word": t.string().optional(),
            "confidence": t.number().optional(),
            "speakerTag": t.integer().optional(),
            "speakerLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WordInfoOut"])
    types["RecognitionConfigIn"] = t.struct(
        {
            "sampleRateHertz": t.integer().optional(),
            "enableAutomaticPunctuation": t.boolean().optional(),
            "profanityFilter": t.boolean().optional(),
            "alternativeLanguageCodes": t.array(t.string()).optional(),
            "model": t.string().optional(),
            "encoding": t.string().optional(),
            "enableWordTimeOffsets": t.boolean().optional(),
            "adaptation": t.proxy(renames["SpeechAdaptationIn"]).optional(),
            "useEnhanced": t.boolean().optional(),
            "maxAlternatives": t.integer().optional(),
            "diarizationConfig": t.proxy(
                renames["SpeakerDiarizationConfigIn"]
            ).optional(),
            "enableSpokenEmojis": t.boolean().optional(),
            "audioChannelCount": t.integer().optional(),
            "enableSpokenPunctuation": t.boolean().optional(),
            "enableWordConfidence": t.boolean().optional(),
            "speechContexts": t.array(t.proxy(renames["SpeechContextIn"])).optional(),
            "metadata": t.proxy(renames["RecognitionMetadataIn"]).optional(),
            "languageCode": t.string(),
            "enableSeparateRecognitionPerChannel": t.boolean().optional(),
        }
    ).named(renames["RecognitionConfigIn"])
    types["RecognitionConfigOut"] = t.struct(
        {
            "sampleRateHertz": t.integer().optional(),
            "enableAutomaticPunctuation": t.boolean().optional(),
            "profanityFilter": t.boolean().optional(),
            "alternativeLanguageCodes": t.array(t.string()).optional(),
            "model": t.string().optional(),
            "encoding": t.string().optional(),
            "enableWordTimeOffsets": t.boolean().optional(),
            "adaptation": t.proxy(renames["SpeechAdaptationOut"]).optional(),
            "useEnhanced": t.boolean().optional(),
            "maxAlternatives": t.integer().optional(),
            "diarizationConfig": t.proxy(
                renames["SpeakerDiarizationConfigOut"]
            ).optional(),
            "enableSpokenEmojis": t.boolean().optional(),
            "audioChannelCount": t.integer().optional(),
            "enableSpokenPunctuation": t.boolean().optional(),
            "enableWordConfidence": t.boolean().optional(),
            "speechContexts": t.array(t.proxy(renames["SpeechContextOut"])).optional(),
            "metadata": t.proxy(renames["RecognitionMetadataOut"]).optional(),
            "languageCode": t.string(),
            "enableSeparateRecognitionPerChannel": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecognitionConfigOut"])

    functions = {}
    functions["operationsList"] = speech.get(
        "v1/operations/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = speech.get(
        "v1/operations/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPhraseSetsPatch"] = speech.post(
        "v1/{parent}/phraseSets",
        t.struct(
            {
                "parent": t.string(),
                "phraseSetId": t.string(),
                "phraseSet": t.proxy(renames["PhraseSetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhraseSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPhraseSetsDelete"] = speech.post(
        "v1/{parent}/phraseSets",
        t.struct(
            {
                "parent": t.string(),
                "phraseSetId": t.string(),
                "phraseSet": t.proxy(renames["PhraseSetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhraseSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPhraseSetsGet"] = speech.post(
        "v1/{parent}/phraseSets",
        t.struct(
            {
                "parent": t.string(),
                "phraseSetId": t.string(),
                "phraseSet": t.proxy(renames["PhraseSetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhraseSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPhraseSetsList"] = speech.post(
        "v1/{parent}/phraseSets",
        t.struct(
            {
                "parent": t.string(),
                "phraseSetId": t.string(),
                "phraseSet": t.proxy(renames["PhraseSetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhraseSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPhraseSetsCreate"] = speech.post(
        "v1/{parent}/phraseSets",
        t.struct(
            {
                "parent": t.string(),
                "phraseSetId": t.string(),
                "phraseSet": t.proxy(renames["PhraseSetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhraseSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCustomClassesCreate"] = speech.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCustomClassesList"] = speech.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCustomClassesPatch"] = speech.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCustomClassesGet"] = speech.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCustomClassesDelete"] = speech.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["speechLongrunningrecognize"] = speech.post(
        "v1/speech:recognize",
        t.struct(
            {
                "audio": t.proxy(renames["RecognitionAudioIn"]),
                "config": t.proxy(renames["RecognitionConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RecognizeResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["speechRecognize"] = speech.post(
        "v1/speech:recognize",
        t.struct(
            {
                "audio": t.proxy(renames["RecognitionAudioIn"]),
                "config": t.proxy(renames["RecognitionConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RecognizeResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="speech", renames=renames, types=Box(types), functions=Box(functions)
    )
