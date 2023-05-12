from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_speech() -> Import:
    speech = HTTPRuntime("https://speech.googleapis.com/")

    renames = {
        "ErrorResponse": "_speech_1_ErrorResponse",
        "ClassItemIn": "_speech_2_ClassItemIn",
        "ClassItemOut": "_speech_3_ClassItemOut",
        "PhraseSetIn": "_speech_4_PhraseSetIn",
        "PhraseSetOut": "_speech_5_PhraseSetOut",
        "LongRunningRecognizeRequestIn": "_speech_6_LongRunningRecognizeRequestIn",
        "LongRunningRecognizeRequestOut": "_speech_7_LongRunningRecognizeRequestOut",
        "SpeechRecognitionAlternativeIn": "_speech_8_SpeechRecognitionAlternativeIn",
        "SpeechRecognitionAlternativeOut": "_speech_9_SpeechRecognitionAlternativeOut",
        "SpeechContextIn": "_speech_10_SpeechContextIn",
        "SpeechContextOut": "_speech_11_SpeechContextOut",
        "CreatePhraseSetRequestIn": "_speech_12_CreatePhraseSetRequestIn",
        "CreatePhraseSetRequestOut": "_speech_13_CreatePhraseSetRequestOut",
        "PhraseIn": "_speech_14_PhraseIn",
        "PhraseOut": "_speech_15_PhraseOut",
        "LongRunningRecognizeMetadataIn": "_speech_16_LongRunningRecognizeMetadataIn",
        "LongRunningRecognizeMetadataOut": "_speech_17_LongRunningRecognizeMetadataOut",
        "RecognizeRequestIn": "_speech_18_RecognizeRequestIn",
        "RecognizeRequestOut": "_speech_19_RecognizeRequestOut",
        "SpeechRecognitionResultIn": "_speech_20_SpeechRecognitionResultIn",
        "SpeechRecognitionResultOut": "_speech_21_SpeechRecognitionResultOut",
        "TranscriptOutputConfigIn": "_speech_22_TranscriptOutputConfigIn",
        "TranscriptOutputConfigOut": "_speech_23_TranscriptOutputConfigOut",
        "EmptyIn": "_speech_24_EmptyIn",
        "EmptyOut": "_speech_25_EmptyOut",
        "CustomClassIn": "_speech_26_CustomClassIn",
        "CustomClassOut": "_speech_27_CustomClassOut",
        "SpeechAdaptationIn": "_speech_28_SpeechAdaptationIn",
        "SpeechAdaptationOut": "_speech_29_SpeechAdaptationOut",
        "SpeechAdaptationInfoIn": "_speech_30_SpeechAdaptationInfoIn",
        "SpeechAdaptationInfoOut": "_speech_31_SpeechAdaptationInfoOut",
        "SpeakerDiarizationConfigIn": "_speech_32_SpeakerDiarizationConfigIn",
        "SpeakerDiarizationConfigOut": "_speech_33_SpeakerDiarizationConfigOut",
        "ListOperationsResponseIn": "_speech_34_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_speech_35_ListOperationsResponseOut",
        "ListCustomClassesResponseIn": "_speech_36_ListCustomClassesResponseIn",
        "ListCustomClassesResponseOut": "_speech_37_ListCustomClassesResponseOut",
        "WordInfoIn": "_speech_38_WordInfoIn",
        "WordInfoOut": "_speech_39_WordInfoOut",
        "RecognitionMetadataIn": "_speech_40_RecognitionMetadataIn",
        "RecognitionMetadataOut": "_speech_41_RecognitionMetadataOut",
        "OperationIn": "_speech_42_OperationIn",
        "OperationOut": "_speech_43_OperationOut",
        "StatusIn": "_speech_44_StatusIn",
        "StatusOut": "_speech_45_StatusOut",
        "RecognizeResponseIn": "_speech_46_RecognizeResponseIn",
        "RecognizeResponseOut": "_speech_47_RecognizeResponseOut",
        "LongRunningRecognizeResponseIn": "_speech_48_LongRunningRecognizeResponseIn",
        "LongRunningRecognizeResponseOut": "_speech_49_LongRunningRecognizeResponseOut",
        "ListPhraseSetResponseIn": "_speech_50_ListPhraseSetResponseIn",
        "ListPhraseSetResponseOut": "_speech_51_ListPhraseSetResponseOut",
        "RecognitionConfigIn": "_speech_52_RecognitionConfigIn",
        "RecognitionConfigOut": "_speech_53_RecognitionConfigOut",
        "CreateCustomClassRequestIn": "_speech_54_CreateCustomClassRequestIn",
        "CreateCustomClassRequestOut": "_speech_55_CreateCustomClassRequestOut",
        "ABNFGrammarIn": "_speech_56_ABNFGrammarIn",
        "ABNFGrammarOut": "_speech_57_ABNFGrammarOut",
        "RecognitionAudioIn": "_speech_58_RecognitionAudioIn",
        "RecognitionAudioOut": "_speech_59_RecognitionAudioOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ClassItemIn"] = t.struct({"value": t.string().optional()}).named(
        renames["ClassItemIn"]
    )
    types["ClassItemOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClassItemOut"])
    types["PhraseSetIn"] = t.struct(
        {
            "name": t.string().optional(),
            "phrases": t.array(t.proxy(renames["PhraseIn"])).optional(),
            "boost": t.number().optional(),
        }
    ).named(renames["PhraseSetIn"])
    types["PhraseSetOut"] = t.struct(
        {
            "kmsKeyVersionName": t.string().optional(),
            "name": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "phrases": t.array(t.proxy(renames["PhraseOut"])).optional(),
            "boost": t.number().optional(),
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
    types["SpeechRecognitionAlternativeIn"] = t.struct(
        {
            "transcript": t.string().optional(),
            "words": t.array(t.proxy(renames["WordInfoIn"])).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["SpeechRecognitionAlternativeIn"])
    types["SpeechRecognitionAlternativeOut"] = t.struct(
        {
            "transcript": t.string().optional(),
            "words": t.array(t.proxy(renames["WordInfoOut"])).optional(),
            "confidence": t.number().optional(),
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
    types["RecognizeRequestIn"] = t.struct(
        {
            "config": t.proxy(renames["RecognitionConfigIn"]),
            "audio": t.proxy(renames["RecognitionAudioIn"]),
        }
    ).named(renames["RecognizeRequestIn"])
    types["RecognizeRequestOut"] = t.struct(
        {
            "config": t.proxy(renames["RecognitionConfigOut"]),
            "audio": t.proxy(renames["RecognitionAudioOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecognizeRequestOut"])
    types["SpeechRecognitionResultIn"] = t.struct(
        {
            "channelTag": t.integer().optional(),
            "resultEndTime": t.string().optional(),
            "alternatives": t.array(
                t.proxy(renames["SpeechRecognitionAlternativeIn"])
            ).optional(),
        }
    ).named(renames["SpeechRecognitionResultIn"])
    types["SpeechRecognitionResultOut"] = t.struct(
        {
            "channelTag": t.integer().optional(),
            "languageCode": t.string().optional(),
            "resultEndTime": t.string().optional(),
            "alternatives": t.array(
                t.proxy(renames["SpeechRecognitionAlternativeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpeechRecognitionResultOut"])
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
    types["CustomClassIn"] = t.struct(
        {
            "customClassId": t.string().optional(),
            "items": t.array(t.proxy(renames["ClassItemIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CustomClassIn"])
    types["CustomClassOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "customClassId": t.string().optional(),
            "kmsKeyVersionName": t.string().optional(),
            "items": t.array(t.proxy(renames["ClassItemOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomClassOut"])
    types["SpeechAdaptationIn"] = t.struct(
        {
            "phraseSetReferences": t.array(t.string()).optional(),
            "phraseSets": t.array(t.proxy(renames["PhraseSetIn"])).optional(),
            "abnfGrammar": t.proxy(renames["ABNFGrammarIn"]).optional(),
            "customClasses": t.array(t.proxy(renames["CustomClassIn"])).optional(),
        }
    ).named(renames["SpeechAdaptationIn"])
    types["SpeechAdaptationOut"] = t.struct(
        {
            "phraseSetReferences": t.array(t.string()).optional(),
            "phraseSets": t.array(t.proxy(renames["PhraseSetOut"])).optional(),
            "abnfGrammar": t.proxy(renames["ABNFGrammarOut"]).optional(),
            "customClasses": t.array(t.proxy(renames["CustomClassOut"])).optional(),
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
    types["SpeakerDiarizationConfigIn"] = t.struct(
        {
            "maxSpeakerCount": t.integer().optional(),
            "enableSpeakerDiarization": t.boolean().optional(),
            "minSpeakerCount": t.integer().optional(),
        }
    ).named(renames["SpeakerDiarizationConfigIn"])
    types["SpeakerDiarizationConfigOut"] = t.struct(
        {
            "speakerTag": t.integer().optional(),
            "maxSpeakerCount": t.integer().optional(),
            "enableSpeakerDiarization": t.boolean().optional(),
            "minSpeakerCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpeakerDiarizationConfigOut"])
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
    types["ListCustomClassesResponseIn"] = t.struct(
        {
            "customClasses": t.array(t.proxy(renames["CustomClassIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCustomClassesResponseIn"])
    types["ListCustomClassesResponseOut"] = t.struct(
        {
            "customClasses": t.array(t.proxy(renames["CustomClassOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCustomClassesResponseOut"])
    types["WordInfoIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "word": t.string().optional(),
        }
    ).named(renames["WordInfoIn"])
    types["WordInfoOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "startTime": t.string().optional(),
            "speakerLabel": t.string().optional(),
            "endTime": t.string().optional(),
            "word": t.string().optional(),
            "speakerTag": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WordInfoOut"])
    types["RecognitionMetadataIn"] = t.struct(
        {
            "originalMediaType": t.string().optional(),
            "interactionType": t.string().optional(),
            "industryNaicsCodeOfAudio": t.integer().optional(),
            "recordingDeviceName": t.string().optional(),
            "microphoneDistance": t.string().optional(),
            "originalMimeType": t.string().optional(),
            "audioTopic": t.string().optional(),
            "recordingDeviceType": t.string().optional(),
        }
    ).named(renames["RecognitionMetadataIn"])
    types["RecognitionMetadataOut"] = t.struct(
        {
            "originalMediaType": t.string().optional(),
            "interactionType": t.string().optional(),
            "industryNaicsCodeOfAudio": t.integer().optional(),
            "recordingDeviceName": t.string().optional(),
            "microphoneDistance": t.string().optional(),
            "originalMimeType": t.string().optional(),
            "audioTopic": t.string().optional(),
            "recordingDeviceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecognitionMetadataOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["RecognizeResponseIn"] = t.struct(
        {
            "speechAdaptationInfo": t.proxy(
                renames["SpeechAdaptationInfoIn"]
            ).optional(),
            "totalBilledTime": t.string().optional(),
            "requestId": t.string().optional(),
            "results": t.array(
                t.proxy(renames["SpeechRecognitionResultIn"])
            ).optional(),
        }
    ).named(renames["RecognizeResponseIn"])
    types["RecognizeResponseOut"] = t.struct(
        {
            "speechAdaptationInfo": t.proxy(
                renames["SpeechAdaptationInfoOut"]
            ).optional(),
            "totalBilledTime": t.string().optional(),
            "requestId": t.string().optional(),
            "results": t.array(
                t.proxy(renames["SpeechRecognitionResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecognizeResponseOut"])
    types["LongRunningRecognizeResponseIn"] = t.struct(
        {
            "speechAdaptationInfo": t.proxy(
                renames["SpeechAdaptationInfoIn"]
            ).optional(),
            "outputError": t.proxy(renames["StatusIn"]).optional(),
            "results": t.array(
                t.proxy(renames["SpeechRecognitionResultIn"])
            ).optional(),
            "outputConfig": t.proxy(renames["TranscriptOutputConfigIn"]).optional(),
            "totalBilledTime": t.string().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["LongRunningRecognizeResponseIn"])
    types["LongRunningRecognizeResponseOut"] = t.struct(
        {
            "speechAdaptationInfo": t.proxy(
                renames["SpeechAdaptationInfoOut"]
            ).optional(),
            "outputError": t.proxy(renames["StatusOut"]).optional(),
            "results": t.array(
                t.proxy(renames["SpeechRecognitionResultOut"])
            ).optional(),
            "outputConfig": t.proxy(renames["TranscriptOutputConfigOut"]).optional(),
            "totalBilledTime": t.string().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningRecognizeResponseOut"])
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
    types["RecognitionConfigIn"] = t.struct(
        {
            "sampleRateHertz": t.integer().optional(),
            "enableSeparateRecognitionPerChannel": t.boolean().optional(),
            "enableAutomaticPunctuation": t.boolean().optional(),
            "audioChannelCount": t.integer().optional(),
            "diarizationConfig": t.proxy(
                renames["SpeakerDiarizationConfigIn"]
            ).optional(),
            "model": t.string().optional(),
            "enableSpokenEmojis": t.boolean().optional(),
            "speechContexts": t.array(t.proxy(renames["SpeechContextIn"])).optional(),
            "metadata": t.proxy(renames["RecognitionMetadataIn"]).optional(),
            "enableSpokenPunctuation": t.boolean().optional(),
            "profanityFilter": t.boolean().optional(),
            "enableWordTimeOffsets": t.boolean().optional(),
            "adaptation": t.proxy(renames["SpeechAdaptationIn"]).optional(),
            "enableWordConfidence": t.boolean().optional(),
            "alternativeLanguageCodes": t.array(t.string()).optional(),
            "encoding": t.string().optional(),
            "maxAlternatives": t.integer().optional(),
            "useEnhanced": t.boolean().optional(),
            "languageCode": t.string(),
        }
    ).named(renames["RecognitionConfigIn"])
    types["RecognitionConfigOut"] = t.struct(
        {
            "sampleRateHertz": t.integer().optional(),
            "enableSeparateRecognitionPerChannel": t.boolean().optional(),
            "enableAutomaticPunctuation": t.boolean().optional(),
            "audioChannelCount": t.integer().optional(),
            "diarizationConfig": t.proxy(
                renames["SpeakerDiarizationConfigOut"]
            ).optional(),
            "model": t.string().optional(),
            "enableSpokenEmojis": t.boolean().optional(),
            "speechContexts": t.array(t.proxy(renames["SpeechContextOut"])).optional(),
            "metadata": t.proxy(renames["RecognitionMetadataOut"]).optional(),
            "enableSpokenPunctuation": t.boolean().optional(),
            "profanityFilter": t.boolean().optional(),
            "enableWordTimeOffsets": t.boolean().optional(),
            "adaptation": t.proxy(renames["SpeechAdaptationOut"]).optional(),
            "enableWordConfidence": t.boolean().optional(),
            "alternativeLanguageCodes": t.array(t.string()).optional(),
            "encoding": t.string().optional(),
            "maxAlternatives": t.integer().optional(),
            "useEnhanced": t.boolean().optional(),
            "languageCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecognitionConfigOut"])
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
    types["ABNFGrammarIn"] = t.struct(
        {"abnfStrings": t.array(t.string()).optional()}
    ).named(renames["ABNFGrammarIn"])
    types["ABNFGrammarOut"] = t.struct(
        {
            "abnfStrings": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ABNFGrammarOut"])
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
    functions["speechRecognize"] = speech.post(
        "v1/speech:longrunningrecognize",
        t.struct(
            {
                "audio": t.proxy(renames["RecognitionAudioIn"]),
                "outputConfig": t.proxy(renames["TranscriptOutputConfigIn"]).optional(),
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
                "audio": t.proxy(renames["RecognitionAudioIn"]),
                "outputConfig": t.proxy(renames["TranscriptOutputConfigIn"]).optional(),
                "config": t.proxy(renames["RecognitionConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPhraseSetsCreate"] = speech.get(
        "v1/{parent}/phraseSets",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPhraseSetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCustomClassesDelete"] = speech.get(
        "v1/{parent}/customClasses",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomClassesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="speech", renames=renames, types=Box(types), functions=Box(functions)
    )
