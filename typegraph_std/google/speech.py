from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_speech() -> Import:
    speech = HTTPRuntime("https://speech.googleapis.com/")

    renames = {
        "ErrorResponse": "_speech_1_ErrorResponse",
        "EmptyIn": "_speech_2_EmptyIn",
        "EmptyOut": "_speech_3_EmptyOut",
        "RecognitionConfigIn": "_speech_4_RecognitionConfigIn",
        "RecognitionConfigOut": "_speech_5_RecognitionConfigOut",
        "PhraseSetIn": "_speech_6_PhraseSetIn",
        "PhraseSetOut": "_speech_7_PhraseSetOut",
        "SpeechRecognitionAlternativeIn": "_speech_8_SpeechRecognitionAlternativeIn",
        "SpeechRecognitionAlternativeOut": "_speech_9_SpeechRecognitionAlternativeOut",
        "SpeechAdaptationIn": "_speech_10_SpeechAdaptationIn",
        "SpeechAdaptationOut": "_speech_11_SpeechAdaptationOut",
        "RecognitionAudioIn": "_speech_12_RecognitionAudioIn",
        "RecognitionAudioOut": "_speech_13_RecognitionAudioOut",
        "SpeechContextIn": "_speech_14_SpeechContextIn",
        "SpeechContextOut": "_speech_15_SpeechContextOut",
        "SpeakerDiarizationConfigIn": "_speech_16_SpeakerDiarizationConfigIn",
        "SpeakerDiarizationConfigOut": "_speech_17_SpeakerDiarizationConfigOut",
        "RecognizeResponseIn": "_speech_18_RecognizeResponseIn",
        "RecognizeResponseOut": "_speech_19_RecognizeResponseOut",
        "RecognizeRequestIn": "_speech_20_RecognizeRequestIn",
        "RecognizeRequestOut": "_speech_21_RecognizeRequestOut",
        "LongRunningRecognizeResponseIn": "_speech_22_LongRunningRecognizeResponseIn",
        "LongRunningRecognizeResponseOut": "_speech_23_LongRunningRecognizeResponseOut",
        "WordInfoIn": "_speech_24_WordInfoIn",
        "WordInfoOut": "_speech_25_WordInfoOut",
        "SpeechRecognitionResultIn": "_speech_26_SpeechRecognitionResultIn",
        "SpeechRecognitionResultOut": "_speech_27_SpeechRecognitionResultOut",
        "OperationIn": "_speech_28_OperationIn",
        "OperationOut": "_speech_29_OperationOut",
        "CreatePhraseSetRequestIn": "_speech_30_CreatePhraseSetRequestIn",
        "CreatePhraseSetRequestOut": "_speech_31_CreatePhraseSetRequestOut",
        "LongRunningRecognizeRequestIn": "_speech_32_LongRunningRecognizeRequestIn",
        "LongRunningRecognizeRequestOut": "_speech_33_LongRunningRecognizeRequestOut",
        "ABNFGrammarIn": "_speech_34_ABNFGrammarIn",
        "ABNFGrammarOut": "_speech_35_ABNFGrammarOut",
        "ClassItemIn": "_speech_36_ClassItemIn",
        "ClassItemOut": "_speech_37_ClassItemOut",
        "LongRunningRecognizeMetadataIn": "_speech_38_LongRunningRecognizeMetadataIn",
        "LongRunningRecognizeMetadataOut": "_speech_39_LongRunningRecognizeMetadataOut",
        "RecognitionMetadataIn": "_speech_40_RecognitionMetadataIn",
        "RecognitionMetadataOut": "_speech_41_RecognitionMetadataOut",
        "PhraseIn": "_speech_42_PhraseIn",
        "PhraseOut": "_speech_43_PhraseOut",
        "TranscriptOutputConfigIn": "_speech_44_TranscriptOutputConfigIn",
        "TranscriptOutputConfigOut": "_speech_45_TranscriptOutputConfigOut",
        "CustomClassIn": "_speech_46_CustomClassIn",
        "CustomClassOut": "_speech_47_CustomClassOut",
        "ListPhraseSetResponseIn": "_speech_48_ListPhraseSetResponseIn",
        "ListPhraseSetResponseOut": "_speech_49_ListPhraseSetResponseOut",
        "ListOperationsResponseIn": "_speech_50_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_speech_51_ListOperationsResponseOut",
        "StatusIn": "_speech_52_StatusIn",
        "StatusOut": "_speech_53_StatusOut",
        "CreateCustomClassRequestIn": "_speech_54_CreateCustomClassRequestIn",
        "CreateCustomClassRequestOut": "_speech_55_CreateCustomClassRequestOut",
        "SpeechAdaptationInfoIn": "_speech_56_SpeechAdaptationInfoIn",
        "SpeechAdaptationInfoOut": "_speech_57_SpeechAdaptationInfoOut",
        "ListCustomClassesResponseIn": "_speech_58_ListCustomClassesResponseIn",
        "ListCustomClassesResponseOut": "_speech_59_ListCustomClassesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["RecognitionConfigIn"] = t.struct(
        {
            "audioChannelCount": t.integer().optional(),
            "sampleRateHertz": t.integer().optional(),
            "enableSpokenEmojis": t.boolean().optional(),
            "encoding": t.string().optional(),
            "useEnhanced": t.boolean().optional(),
            "enableSpokenPunctuation": t.boolean().optional(),
            "profanityFilter": t.boolean().optional(),
            "speechContexts": t.array(t.proxy(renames["SpeechContextIn"])).optional(),
            "maxAlternatives": t.integer().optional(),
            "model": t.string().optional(),
            "adaptation": t.proxy(renames["SpeechAdaptationIn"]).optional(),
            "languageCode": t.string(),
            "enableWordTimeOffsets": t.boolean().optional(),
            "enableAutomaticPunctuation": t.boolean().optional(),
            "enableSeparateRecognitionPerChannel": t.boolean().optional(),
            "enableWordConfidence": t.boolean().optional(),
            "metadata": t.proxy(renames["RecognitionMetadataIn"]).optional(),
            "diarizationConfig": t.proxy(
                renames["SpeakerDiarizationConfigIn"]
            ).optional(),
            "alternativeLanguageCodes": t.array(t.string()).optional(),
        }
    ).named(renames["RecognitionConfigIn"])
    types["RecognitionConfigOut"] = t.struct(
        {
            "audioChannelCount": t.integer().optional(),
            "sampleRateHertz": t.integer().optional(),
            "enableSpokenEmojis": t.boolean().optional(),
            "encoding": t.string().optional(),
            "useEnhanced": t.boolean().optional(),
            "enableSpokenPunctuation": t.boolean().optional(),
            "profanityFilter": t.boolean().optional(),
            "speechContexts": t.array(t.proxy(renames["SpeechContextOut"])).optional(),
            "maxAlternatives": t.integer().optional(),
            "model": t.string().optional(),
            "adaptation": t.proxy(renames["SpeechAdaptationOut"]).optional(),
            "languageCode": t.string(),
            "enableWordTimeOffsets": t.boolean().optional(),
            "enableAutomaticPunctuation": t.boolean().optional(),
            "enableSeparateRecognitionPerChannel": t.boolean().optional(),
            "enableWordConfidence": t.boolean().optional(),
            "metadata": t.proxy(renames["RecognitionMetadataOut"]).optional(),
            "diarizationConfig": t.proxy(
                renames["SpeakerDiarizationConfigOut"]
            ).optional(),
            "alternativeLanguageCodes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecognitionConfigOut"])
    types["PhraseSetIn"] = t.struct(
        {
            "boost": t.number().optional(),
            "name": t.string().optional(),
            "phrases": t.array(t.proxy(renames["PhraseIn"])).optional(),
        }
    ).named(renames["PhraseSetIn"])
    types["PhraseSetOut"] = t.struct(
        {
            "kmsKeyVersionName": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "boost": t.number().optional(),
            "name": t.string().optional(),
            "phrases": t.array(t.proxy(renames["PhraseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhraseSetOut"])
    types["SpeechRecognitionAlternativeIn"] = t.struct(
        {
            "words": t.array(t.proxy(renames["WordInfoIn"])).optional(),
            "transcript": t.string().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["SpeechRecognitionAlternativeIn"])
    types["SpeechRecognitionAlternativeOut"] = t.struct(
        {
            "words": t.array(t.proxy(renames["WordInfoOut"])).optional(),
            "transcript": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpeechRecognitionAlternativeOut"])
    types["SpeechAdaptationIn"] = t.struct(
        {
            "customClasses": t.array(t.proxy(renames["CustomClassIn"])).optional(),
            "phraseSetReferences": t.array(t.string()).optional(),
            "phraseSets": t.array(t.proxy(renames["PhraseSetIn"])).optional(),
            "abnfGrammar": t.proxy(renames["ABNFGrammarIn"]).optional(),
        }
    ).named(renames["SpeechAdaptationIn"])
    types["SpeechAdaptationOut"] = t.struct(
        {
            "customClasses": t.array(t.proxy(renames["CustomClassOut"])).optional(),
            "phraseSetReferences": t.array(t.string()).optional(),
            "phraseSets": t.array(t.proxy(renames["PhraseSetOut"])).optional(),
            "abnfGrammar": t.proxy(renames["ABNFGrammarOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpeechAdaptationOut"])
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
            "enableSpeakerDiarization": t.boolean().optional(),
            "maxSpeakerCount": t.integer().optional(),
            "speakerTag": t.integer().optional(),
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
    types["LongRunningRecognizeResponseIn"] = t.struct(
        {
            "totalBilledTime": t.string().optional(),
            "outputConfig": t.proxy(renames["TranscriptOutputConfigIn"]).optional(),
            "results": t.array(
                t.proxy(renames["SpeechRecognitionResultIn"])
            ).optional(),
            "requestId": t.string().optional(),
            "outputError": t.proxy(renames["StatusIn"]).optional(),
            "speechAdaptationInfo": t.proxy(
                renames["SpeechAdaptationInfoIn"]
            ).optional(),
        }
    ).named(renames["LongRunningRecognizeResponseIn"])
    types["LongRunningRecognizeResponseOut"] = t.struct(
        {
            "totalBilledTime": t.string().optional(),
            "outputConfig": t.proxy(renames["TranscriptOutputConfigOut"]).optional(),
            "results": t.array(
                t.proxy(renames["SpeechRecognitionResultOut"])
            ).optional(),
            "requestId": t.string().optional(),
            "outputError": t.proxy(renames["StatusOut"]).optional(),
            "speechAdaptationInfo": t.proxy(
                renames["SpeechAdaptationInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningRecognizeResponseOut"])
    types["WordInfoIn"] = t.struct(
        {
            "word": t.string().optional(),
            "confidence": t.number().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["WordInfoIn"])
    types["WordInfoOut"] = t.struct(
        {
            "speakerLabel": t.string().optional(),
            "speakerTag": t.integer().optional(),
            "word": t.string().optional(),
            "confidence": t.number().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WordInfoOut"])
    types["SpeechRecognitionResultIn"] = t.struct(
        {
            "alternatives": t.array(
                t.proxy(renames["SpeechRecognitionAlternativeIn"])
            ).optional(),
            "channelTag": t.integer().optional(),
            "resultEndTime": t.string().optional(),
        }
    ).named(renames["SpeechRecognitionResultIn"])
    types["SpeechRecognitionResultOut"] = t.struct(
        {
            "alternatives": t.array(
                t.proxy(renames["SpeechRecognitionAlternativeOut"])
            ).optional(),
            "channelTag": t.integer().optional(),
            "resultEndTime": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpeechRecognitionResultOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["CreatePhraseSetRequestIn"] = t.struct(
        {"phraseSet": t.proxy(renames["PhraseSetIn"]), "phraseSetId": t.string()}
    ).named(renames["CreatePhraseSetRequestIn"])
    types["CreatePhraseSetRequestOut"] = t.struct(
        {
            "phraseSet": t.proxy(renames["PhraseSetOut"]),
            "phraseSetId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreatePhraseSetRequestOut"])
    types["LongRunningRecognizeRequestIn"] = t.struct(
        {
            "audio": t.proxy(renames["RecognitionAudioIn"]),
            "config": t.proxy(renames["RecognitionConfigIn"]),
            "outputConfig": t.proxy(renames["TranscriptOutputConfigIn"]).optional(),
        }
    ).named(renames["LongRunningRecognizeRequestIn"])
    types["LongRunningRecognizeRequestOut"] = t.struct(
        {
            "audio": t.proxy(renames["RecognitionAudioOut"]),
            "config": t.proxy(renames["RecognitionConfigOut"]),
            "outputConfig": t.proxy(renames["TranscriptOutputConfigOut"]).optional(),
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
    types["ClassItemIn"] = t.struct({"value": t.string().optional()}).named(
        renames["ClassItemIn"]
    )
    types["ClassItemOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClassItemOut"])
    types["LongRunningRecognizeMetadataIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
        }
    ).named(renames["LongRunningRecognizeMetadataIn"])
    types["LongRunningRecognizeMetadataOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningRecognizeMetadataOut"])
    types["RecognitionMetadataIn"] = t.struct(
        {
            "microphoneDistance": t.string().optional(),
            "interactionType": t.string().optional(),
            "originalMimeType": t.string().optional(),
            "industryNaicsCodeOfAudio": t.integer().optional(),
            "originalMediaType": t.string().optional(),
            "recordingDeviceName": t.string().optional(),
            "recordingDeviceType": t.string().optional(),
            "audioTopic": t.string().optional(),
        }
    ).named(renames["RecognitionMetadataIn"])
    types["RecognitionMetadataOut"] = t.struct(
        {
            "microphoneDistance": t.string().optional(),
            "interactionType": t.string().optional(),
            "originalMimeType": t.string().optional(),
            "industryNaicsCodeOfAudio": t.integer().optional(),
            "originalMediaType": t.string().optional(),
            "recordingDeviceName": t.string().optional(),
            "recordingDeviceType": t.string().optional(),
            "audioTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecognitionMetadataOut"])
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
            "customClassId": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "kmsKeyVersionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomClassOut"])
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
    functions["operationsGet"] = speech.get(
        "v1/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCustomClassesGet"] = speech.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "items": t.array(t.proxy(renames["ClassItemIn"])).optional(),
                "customClassId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomClassOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCustomClassesDelete"] = speech.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "items": t.array(t.proxy(renames["ClassItemIn"])).optional(),
                "customClassId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomClassOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCustomClassesCreate"] = speech.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "items": t.array(t.proxy(renames["ClassItemIn"])).optional(),
                "customClassId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomClassOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCustomClassesList"] = speech.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "items": t.array(t.proxy(renames["ClassItemIn"])).optional(),
                "customClassId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomClassOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCustomClassesPatch"] = speech.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "items": t.array(t.proxy(renames["ClassItemIn"])).optional(),
                "customClassId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomClassOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPhraseSetsGet"] = speech.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "boost": t.number().optional(),
                "phrases": t.array(t.proxy(renames["PhraseIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhraseSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPhraseSetsCreate"] = speech.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "boost": t.number().optional(),
                "phrases": t.array(t.proxy(renames["PhraseIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhraseSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPhraseSetsList"] = speech.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "boost": t.number().optional(),
                "phrases": t.array(t.proxy(renames["PhraseIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhraseSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPhraseSetsDelete"] = speech.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "boost": t.number().optional(),
                "phrases": t.array(t.proxy(renames["PhraseIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhraseSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPhraseSetsPatch"] = speech.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "boost": t.number().optional(),
                "phrases": t.array(t.proxy(renames["PhraseIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhraseSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="speech", renames=renames, types=types, functions=functions)
