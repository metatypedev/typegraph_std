from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_texttospeech() -> Import:
    texttospeech = HTTPRuntime("https://texttospeech.googleapis.com/")

    renames = {
        "ErrorResponse": "_texttospeech_1_ErrorResponse",
        "VoiceIn": "_texttospeech_2_VoiceIn",
        "VoiceOut": "_texttospeech_3_VoiceOut",
        "OperationIn": "_texttospeech_4_OperationIn",
        "OperationOut": "_texttospeech_5_OperationOut",
        "SynthesizeSpeechResponseIn": "_texttospeech_6_SynthesizeSpeechResponseIn",
        "SynthesizeSpeechResponseOut": "_texttospeech_7_SynthesizeSpeechResponseOut",
        "VoiceSelectionParamsIn": "_texttospeech_8_VoiceSelectionParamsIn",
        "VoiceSelectionParamsOut": "_texttospeech_9_VoiceSelectionParamsOut",
        "SynthesizeLongAudioRequestIn": "_texttospeech_10_SynthesizeLongAudioRequestIn",
        "SynthesizeLongAudioRequestOut": "_texttospeech_11_SynthesizeLongAudioRequestOut",
        "ListOperationsResponseIn": "_texttospeech_12_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_texttospeech_13_ListOperationsResponseOut",
        "CustomVoiceParamsIn": "_texttospeech_14_CustomVoiceParamsIn",
        "CustomVoiceParamsOut": "_texttospeech_15_CustomVoiceParamsOut",
        "StatusIn": "_texttospeech_16_StatusIn",
        "StatusOut": "_texttospeech_17_StatusOut",
        "AudioConfigIn": "_texttospeech_18_AudioConfigIn",
        "AudioConfigOut": "_texttospeech_19_AudioConfigOut",
        "EmptyIn": "_texttospeech_20_EmptyIn",
        "EmptyOut": "_texttospeech_21_EmptyOut",
        "CancelOperationRequestIn": "_texttospeech_22_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_texttospeech_23_CancelOperationRequestOut",
        "SynthesisInputIn": "_texttospeech_24_SynthesisInputIn",
        "SynthesisInputOut": "_texttospeech_25_SynthesisInputOut",
        "SynthesizeLongAudioMetadataIn": "_texttospeech_26_SynthesizeLongAudioMetadataIn",
        "SynthesizeLongAudioMetadataOut": "_texttospeech_27_SynthesizeLongAudioMetadataOut",
        "ListVoicesResponseIn": "_texttospeech_28_ListVoicesResponseIn",
        "ListVoicesResponseOut": "_texttospeech_29_ListVoicesResponseOut",
        "SynthesizeSpeechRequestIn": "_texttospeech_30_SynthesizeSpeechRequestIn",
        "SynthesizeSpeechRequestOut": "_texttospeech_31_SynthesizeSpeechRequestOut",
        "GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataIn": "_texttospeech_32_GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataIn",
        "GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataOut": "_texttospeech_33_GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["VoiceIn"] = t.struct(
        {
            "naturalSampleRateHertz": t.integer().optional(),
            "languageCodes": t.array(t.string()).optional(),
            "ssmlGender": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["VoiceIn"])
    types["VoiceOut"] = t.struct(
        {
            "naturalSampleRateHertz": t.integer().optional(),
            "languageCodes": t.array(t.string()).optional(),
            "ssmlGender": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["SynthesizeSpeechResponseIn"] = t.struct(
        {"audioContent": t.string().optional()}
    ).named(renames["SynthesizeSpeechResponseIn"])
    types["SynthesizeSpeechResponseOut"] = t.struct(
        {
            "audioContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SynthesizeSpeechResponseOut"])
    types["VoiceSelectionParamsIn"] = t.struct(
        {
            "languageCode": t.string(),
            "name": t.string().optional(),
            "ssmlGender": t.string().optional(),
            "customVoice": t.proxy(renames["CustomVoiceParamsIn"]).optional(),
        }
    ).named(renames["VoiceSelectionParamsIn"])
    types["VoiceSelectionParamsOut"] = t.struct(
        {
            "languageCode": t.string(),
            "name": t.string().optional(),
            "ssmlGender": t.string().optional(),
            "customVoice": t.proxy(renames["CustomVoiceParamsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceSelectionParamsOut"])
    types["SynthesizeLongAudioRequestIn"] = t.struct(
        {
            "outputGcsUri": t.string(),
            "audioConfig": t.proxy(renames["AudioConfigIn"]),
            "voice": t.proxy(renames["VoiceSelectionParamsIn"]),
            "input": t.proxy(renames["SynthesisInputIn"]),
        }
    ).named(renames["SynthesizeLongAudioRequestIn"])
    types["SynthesizeLongAudioRequestOut"] = t.struct(
        {
            "outputGcsUri": t.string(),
            "audioConfig": t.proxy(renames["AudioConfigOut"]),
            "voice": t.proxy(renames["VoiceSelectionParamsOut"]),
            "input": t.proxy(renames["SynthesisInputOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SynthesizeLongAudioRequestOut"])
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
    types["AudioConfigIn"] = t.struct(
        {
            "sampleRateHertz": t.integer().optional(),
            "audioEncoding": t.string(),
            "volumeGainDb": t.number().optional(),
            "effectsProfileId": t.array(t.string()).optional(),
            "speakingRate": t.number().optional(),
            "pitch": t.number().optional(),
        }
    ).named(renames["AudioConfigIn"])
    types["AudioConfigOut"] = t.struct(
        {
            "sampleRateHertz": t.integer().optional(),
            "audioEncoding": t.string(),
            "volumeGainDb": t.number().optional(),
            "effectsProfileId": t.array(t.string()).optional(),
            "speakingRate": t.number().optional(),
            "pitch": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["ListVoicesResponseIn"] = t.struct(
        {"voices": t.array(t.proxy(renames["VoiceIn"])).optional()}
    ).named(renames["ListVoicesResponseIn"])
    types["ListVoicesResponseOut"] = t.struct(
        {
            "voices": t.array(t.proxy(renames["VoiceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVoicesResponseOut"])
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
    types["GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "progressPercentage": t.number().optional(),
        }
    ).named(renames["GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataIn"])
    types["GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "progressPercentage": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataOut"])

    functions = {}
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
                "outputGcsUri": t.string(),
                "audioConfig": t.proxy(renames["AudioConfigIn"]),
                "voice": t.proxy(renames["VoiceSelectionParamsIn"]),
                "input": t.proxy(renames["SynthesisInputIn"]),
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
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
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

    return Import(
        importer="texttospeech",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
