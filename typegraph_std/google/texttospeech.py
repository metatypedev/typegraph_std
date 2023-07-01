from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_texttospeech():
    texttospeech = HTTPRuntime("https://texttospeech.googleapis.com/")

    renames = {
        "ErrorResponse": "_texttospeech_1_ErrorResponse",
        "SynthesisInputIn": "_texttospeech_2_SynthesisInputIn",
        "SynthesisInputOut": "_texttospeech_3_SynthesisInputOut",
        "VoiceIn": "_texttospeech_4_VoiceIn",
        "VoiceOut": "_texttospeech_5_VoiceOut",
        "GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataIn": "_texttospeech_6_GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataIn",
        "GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataOut": "_texttospeech_7_GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataOut",
        "VoiceSelectionParamsIn": "_texttospeech_8_VoiceSelectionParamsIn",
        "VoiceSelectionParamsOut": "_texttospeech_9_VoiceSelectionParamsOut",
        "StatusIn": "_texttospeech_10_StatusIn",
        "StatusOut": "_texttospeech_11_StatusOut",
        "AudioConfigIn": "_texttospeech_12_AudioConfigIn",
        "AudioConfigOut": "_texttospeech_13_AudioConfigOut",
        "EmptyIn": "_texttospeech_14_EmptyIn",
        "EmptyOut": "_texttospeech_15_EmptyOut",
        "SynthesizeSpeechResponseIn": "_texttospeech_16_SynthesizeSpeechResponseIn",
        "SynthesizeSpeechResponseOut": "_texttospeech_17_SynthesizeSpeechResponseOut",
        "CustomVoiceParamsIn": "_texttospeech_18_CustomVoiceParamsIn",
        "CustomVoiceParamsOut": "_texttospeech_19_CustomVoiceParamsOut",
        "SynthesizeSpeechRequestIn": "_texttospeech_20_SynthesizeSpeechRequestIn",
        "SynthesizeSpeechRequestOut": "_texttospeech_21_SynthesizeSpeechRequestOut",
        "ListOperationsResponseIn": "_texttospeech_22_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_texttospeech_23_ListOperationsResponseOut",
        "SynthesizeLongAudioRequestIn": "_texttospeech_24_SynthesizeLongAudioRequestIn",
        "SynthesizeLongAudioRequestOut": "_texttospeech_25_SynthesizeLongAudioRequestOut",
        "CancelOperationRequestIn": "_texttospeech_26_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_texttospeech_27_CancelOperationRequestOut",
        "OperationIn": "_texttospeech_28_OperationIn",
        "OperationOut": "_texttospeech_29_OperationOut",
        "ListVoicesResponseIn": "_texttospeech_30_ListVoicesResponseIn",
        "ListVoicesResponseOut": "_texttospeech_31_ListVoicesResponseOut",
        "SynthesizeLongAudioMetadataIn": "_texttospeech_32_SynthesizeLongAudioMetadataIn",
        "SynthesizeLongAudioMetadataOut": "_texttospeech_33_SynthesizeLongAudioMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["VoiceIn"] = t.struct(
        {
            "naturalSampleRateHertz": t.integer().optional(),
            "ssmlGender": t.string().optional(),
            "languageCodes": t.array(t.string()).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["VoiceIn"])
    types["VoiceOut"] = t.struct(
        {
            "naturalSampleRateHertz": t.integer().optional(),
            "ssmlGender": t.string().optional(),
            "languageCodes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceOut"])
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
    types["VoiceSelectionParamsIn"] = t.struct(
        {
            "name": t.string().optional(),
            "customVoice": t.proxy(renames["CustomVoiceParamsIn"]).optional(),
            "languageCode": t.string(),
            "ssmlGender": t.string().optional(),
        }
    ).named(renames["VoiceSelectionParamsIn"])
    types["VoiceSelectionParamsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "customVoice": t.proxy(renames["CustomVoiceParamsOut"]).optional(),
            "languageCode": t.string(),
            "ssmlGender": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceSelectionParamsOut"])
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
    types["AudioConfigIn"] = t.struct(
        {
            "sampleRateHertz": t.integer().optional(),
            "speakingRate": t.number().optional(),
            "audioEncoding": t.string(),
            "volumeGainDb": t.number().optional(),
            "effectsProfileId": t.array(t.string()).optional(),
            "pitch": t.number().optional(),
        }
    ).named(renames["AudioConfigIn"])
    types["AudioConfigOut"] = t.struct(
        {
            "sampleRateHertz": t.integer().optional(),
            "speakingRate": t.number().optional(),
            "audioEncoding": t.string(),
            "volumeGainDb": t.number().optional(),
            "effectsProfileId": t.array(t.string()).optional(),
            "pitch": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["SynthesizeSpeechResponseIn"] = t.struct(
        {"audioContent": t.string().optional()}
    ).named(renames["SynthesizeSpeechResponseIn"])
    types["SynthesizeSpeechResponseOut"] = t.struct(
        {
            "audioContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SynthesizeSpeechResponseOut"])
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
    types["SynthesizeSpeechRequestIn"] = t.struct(
        {
            "voice": t.proxy(renames["VoiceSelectionParamsIn"]),
            "audioConfig": t.proxy(renames["AudioConfigIn"]),
            "input": t.proxy(renames["SynthesisInputIn"]),
        }
    ).named(renames["SynthesizeSpeechRequestIn"])
    types["SynthesizeSpeechRequestOut"] = t.struct(
        {
            "voice": t.proxy(renames["VoiceSelectionParamsOut"]),
            "audioConfig": t.proxy(renames["AudioConfigOut"]),
            "input": t.proxy(renames["SynthesisInputOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SynthesizeSpeechRequestOut"])
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
    types["SynthesizeLongAudioRequestIn"] = t.struct(
        {
            "input": t.proxy(renames["SynthesisInputIn"]),
            "voice": t.proxy(renames["VoiceSelectionParamsIn"]),
            "audioConfig": t.proxy(renames["AudioConfigIn"]),
            "outputGcsUri": t.string(),
        }
    ).named(renames["SynthesizeLongAudioRequestIn"])
    types["SynthesizeLongAudioRequestOut"] = t.struct(
        {
            "input": t.proxy(renames["SynthesisInputOut"]),
            "voice": t.proxy(renames["VoiceSelectionParamsOut"]),
            "audioConfig": t.proxy(renames["AudioConfigOut"]),
            "outputGcsUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SynthesizeLongAudioRequestOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["ListVoicesResponseIn"] = t.struct(
        {"voices": t.array(t.proxy(renames["VoiceIn"])).optional()}
    ).named(renames["ListVoicesResponseIn"])
    types["ListVoicesResponseOut"] = t.struct(
        {
            "voices": t.array(t.proxy(renames["VoiceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVoicesResponseOut"])
    types["SynthesizeLongAudioMetadataIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "progressPercentage": t.number().optional(),
        }
    ).named(renames["SynthesizeLongAudioMetadataIn"])
    types["SynthesizeLongAudioMetadataOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "progressPercentage": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SynthesizeLongAudioMetadataOut"])

    functions = {}
    functions["textSynthesize"] = texttospeech.post(
        "v1/text:synthesize",
        t.struct(
            {
                "voice": t.proxy(renames["VoiceSelectionParamsIn"]),
                "audioConfig": t.proxy(renames["AudioConfigIn"]),
                "input": t.proxy(renames["SynthesisInputIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SynthesizeSpeechResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = texttospeech.post(
        "v1/{name}:cancel",
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
    functions["operationsCancel"] = texttospeech.post(
        "v1/{name}:cancel",
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
    functions["voicesList"] = texttospeech.get(
        "v1/voices",
        t.struct(
            {"languageCode": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ListVoicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSynthesizeLongAudio"] = texttospeech.post(
        "v1/{parent}:synthesizeLongAudio",
        t.struct(
            {
                "parent": t.string().optional(),
                "input": t.proxy(renames["SynthesisInputIn"]),
                "voice": t.proxy(renames["VoiceSelectionParamsIn"]),
                "audioConfig": t.proxy(renames["AudioConfigIn"]),
                "outputGcsUri": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = texttospeech.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = texttospeech.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="texttospeech",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
