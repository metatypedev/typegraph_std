from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_texttospeech() -> Import:
    texttospeech = HTTPRuntime("https://texttospeech.googleapis.com/")

    renames = {
        "ErrorResponse": "_texttospeech_1_ErrorResponse",
        "CustomVoiceParamsIn": "_texttospeech_2_CustomVoiceParamsIn",
        "CustomVoiceParamsOut": "_texttospeech_3_CustomVoiceParamsOut",
        "GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataIn": "_texttospeech_4_GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataIn",
        "GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataOut": "_texttospeech_5_GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataOut",
        "SynthesizeSpeechRequestIn": "_texttospeech_6_SynthesizeSpeechRequestIn",
        "SynthesizeSpeechRequestOut": "_texttospeech_7_SynthesizeSpeechRequestOut",
        "SynthesizeSpeechResponseIn": "_texttospeech_8_SynthesizeSpeechResponseIn",
        "SynthesizeSpeechResponseOut": "_texttospeech_9_SynthesizeSpeechResponseOut",
        "ListOperationsResponseIn": "_texttospeech_10_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_texttospeech_11_ListOperationsResponseOut",
        "AudioConfigIn": "_texttospeech_12_AudioConfigIn",
        "AudioConfigOut": "_texttospeech_13_AudioConfigOut",
        "VoiceIn": "_texttospeech_14_VoiceIn",
        "VoiceOut": "_texttospeech_15_VoiceOut",
        "OperationIn": "_texttospeech_16_OperationIn",
        "OperationOut": "_texttospeech_17_OperationOut",
        "EmptyIn": "_texttospeech_18_EmptyIn",
        "EmptyOut": "_texttospeech_19_EmptyOut",
        "SynthesizeLongAudioRequestIn": "_texttospeech_20_SynthesizeLongAudioRequestIn",
        "SynthesizeLongAudioRequestOut": "_texttospeech_21_SynthesizeLongAudioRequestOut",
        "StatusIn": "_texttospeech_22_StatusIn",
        "StatusOut": "_texttospeech_23_StatusOut",
        "SynthesisInputIn": "_texttospeech_24_SynthesisInputIn",
        "SynthesisInputOut": "_texttospeech_25_SynthesisInputOut",
        "CancelOperationRequestIn": "_texttospeech_26_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_texttospeech_27_CancelOperationRequestOut",
        "ListVoicesResponseIn": "_texttospeech_28_ListVoicesResponseIn",
        "ListVoicesResponseOut": "_texttospeech_29_ListVoicesResponseOut",
        "VoiceSelectionParamsIn": "_texttospeech_30_VoiceSelectionParamsIn",
        "VoiceSelectionParamsOut": "_texttospeech_31_VoiceSelectionParamsOut",
        "SynthesizeLongAudioMetadataIn": "_texttospeech_32_SynthesizeLongAudioMetadataIn",
        "SynthesizeLongAudioMetadataOut": "_texttospeech_33_SynthesizeLongAudioMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CustomVoiceParamsIn"] = t.struct(
        {"model": t.string(), "reportedUsage": t.string().optional()}
    ).named(renames["CustomVoiceParamsIn"])
    types["CustomVoiceParamsOut"] = t.struct(
        {
            "model": t.string(),
            "reportedUsage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomVoiceParamsOut"])
    types["GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataIn"] = t.struct(
        {
            "progressPercentage": t.number().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataIn"])
    types["GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataOut"] = t.struct(
        {
            "progressPercentage": t.number().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataOut"])
    types["SynthesizeSpeechRequestIn"] = t.struct(
        {
            "voice": t.proxy(renames["VoiceSelectionParamsIn"]),
            "input": t.proxy(renames["SynthesisInputIn"]),
            "audioConfig": t.proxy(renames["AudioConfigIn"]),
        }
    ).named(renames["SynthesizeSpeechRequestIn"])
    types["SynthesizeSpeechRequestOut"] = t.struct(
        {
            "voice": t.proxy(renames["VoiceSelectionParamsOut"]),
            "input": t.proxy(renames["SynthesisInputOut"]),
            "audioConfig": t.proxy(renames["AudioConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SynthesizeSpeechRequestOut"])
    types["SynthesizeSpeechResponseIn"] = t.struct(
        {"audioContent": t.string().optional()}
    ).named(renames["SynthesizeSpeechResponseIn"])
    types["SynthesizeSpeechResponseOut"] = t.struct(
        {
            "audioContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SynthesizeSpeechResponseOut"])
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
    types["AudioConfigIn"] = t.struct(
        {
            "sampleRateHertz": t.integer().optional(),
            "audioEncoding": t.string(),
            "volumeGainDb": t.number().optional(),
            "pitch": t.number().optional(),
            "speakingRate": t.number().optional(),
            "effectsProfileId": t.array(t.string()).optional(),
        }
    ).named(renames["AudioConfigIn"])
    types["AudioConfigOut"] = t.struct(
        {
            "sampleRateHertz": t.integer().optional(),
            "audioEncoding": t.string(),
            "volumeGainDb": t.number().optional(),
            "pitch": t.number().optional(),
            "speakingRate": t.number().optional(),
            "effectsProfileId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioConfigOut"])
    types["VoiceIn"] = t.struct(
        {
            "naturalSampleRateHertz": t.integer().optional(),
            "languageCodes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "ssmlGender": t.string().optional(),
        }
    ).named(renames["VoiceIn"])
    types["VoiceOut"] = t.struct(
        {
            "naturalSampleRateHertz": t.integer().optional(),
            "languageCodes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "ssmlGender": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["SynthesizeLongAudioRequestIn"] = t.struct(
        {
            "audioConfig": t.proxy(renames["AudioConfigIn"]),
            "voice": t.proxy(renames["VoiceSelectionParamsIn"]),
            "input": t.proxy(renames["SynthesisInputIn"]),
            "outputGcsUri": t.string(),
        }
    ).named(renames["SynthesizeLongAudioRequestIn"])
    types["SynthesizeLongAudioRequestOut"] = t.struct(
        {
            "audioConfig": t.proxy(renames["AudioConfigOut"]),
            "voice": t.proxy(renames["VoiceSelectionParamsOut"]),
            "input": t.proxy(renames["SynthesisInputOut"]),
            "outputGcsUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SynthesizeLongAudioRequestOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["SynthesisInputIn"] = t.struct(
        {"text": t.string().optional(), "ssml": t.string().optional()}
    ).named(renames["SynthesisInputIn"])
    types["SynthesisInputOut"] = t.struct(
        {
            "text": t.string().optional(),
            "ssml": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SynthesisInputOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ListVoicesResponseIn"] = t.struct(
        {"voices": t.array(t.proxy(renames["VoiceIn"])).optional()}
    ).named(renames["ListVoicesResponseIn"])
    types["ListVoicesResponseOut"] = t.struct(
        {
            "voices": t.array(t.proxy(renames["VoiceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVoicesResponseOut"])
    types["VoiceSelectionParamsIn"] = t.struct(
        {
            "ssmlGender": t.string().optional(),
            "customVoice": t.proxy(renames["CustomVoiceParamsIn"]).optional(),
            "name": t.string().optional(),
            "languageCode": t.string(),
        }
    ).named(renames["VoiceSelectionParamsIn"])
    types["VoiceSelectionParamsOut"] = t.struct(
        {
            "ssmlGender": t.string().optional(),
            "customVoice": t.proxy(renames["CustomVoiceParamsOut"]).optional(),
            "name": t.string().optional(),
            "languageCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceSelectionParamsOut"])
    types["SynthesizeLongAudioMetadataIn"] = t.struct(
        {
            "progressPercentage": t.number().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["SynthesizeLongAudioMetadataIn"])
    types["SynthesizeLongAudioMetadataOut"] = t.struct(
        {
            "progressPercentage": t.number().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SynthesizeLongAudioMetadataOut"])

    functions = {}
    functions["projectsLocationsSynthesizeLongAudio"] = texttospeech.post(
        "v1/{parent}:synthesizeLongAudio",
        t.struct(
            {
                "parent": t.string().optional(),
                "audioConfig": t.proxy(renames["AudioConfigIn"]),
                "voice": t.proxy(renames["VoiceSelectionParamsIn"]),
                "input": t.proxy(renames["SynthesisInputIn"]),
                "outputGcsUri": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = texttospeech.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = texttospeech.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = texttospeech.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = texttospeech.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["voicesList"] = texttospeech.get(
        "v1/voices",
        t.struct(
            {"languageCode": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ListVoicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["textSynthesize"] = texttospeech.post(
        "v1/text:synthesize",
        t.struct(
            {
                "voice": t.proxy(renames["VoiceSelectionParamsIn"]),
                "input": t.proxy(renames["SynthesisInputIn"]),
                "audioConfig": t.proxy(renames["AudioConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SynthesizeSpeechResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="texttospeech", renames=renames, types=types, functions=functions
    )
