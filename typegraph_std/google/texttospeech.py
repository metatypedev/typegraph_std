from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_texttospeech() -> Import:
    texttospeech = HTTPRuntime("https://texttospeech.googleapis.com/")

    renames = {
        "ErrorResponse": "_texttospeech_1_ErrorResponse",
        "CancelOperationRequestIn": "_texttospeech_2_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_texttospeech_3_CancelOperationRequestOut",
        "StatusIn": "_texttospeech_4_StatusIn",
        "StatusOut": "_texttospeech_5_StatusOut",
        "SynthesizeLongAudioMetadataIn": "_texttospeech_6_SynthesizeLongAudioMetadataIn",
        "SynthesizeLongAudioMetadataOut": "_texttospeech_7_SynthesizeLongAudioMetadataOut",
        "VoiceSelectionParamsIn": "_texttospeech_8_VoiceSelectionParamsIn",
        "VoiceSelectionParamsOut": "_texttospeech_9_VoiceSelectionParamsOut",
        "OperationIn": "_texttospeech_10_OperationIn",
        "OperationOut": "_texttospeech_11_OperationOut",
        "ListVoicesResponseIn": "_texttospeech_12_ListVoicesResponseIn",
        "ListVoicesResponseOut": "_texttospeech_13_ListVoicesResponseOut",
        "CustomVoiceParamsIn": "_texttospeech_14_CustomVoiceParamsIn",
        "CustomVoiceParamsOut": "_texttospeech_15_CustomVoiceParamsOut",
        "ListOperationsResponseIn": "_texttospeech_16_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_texttospeech_17_ListOperationsResponseOut",
        "SynthesisInputIn": "_texttospeech_18_SynthesisInputIn",
        "SynthesisInputOut": "_texttospeech_19_SynthesisInputOut",
        "VoiceIn": "_texttospeech_20_VoiceIn",
        "VoiceOut": "_texttospeech_21_VoiceOut",
        "SynthesizeLongAudioRequestIn": "_texttospeech_22_SynthesizeLongAudioRequestIn",
        "SynthesizeLongAudioRequestOut": "_texttospeech_23_SynthesizeLongAudioRequestOut",
        "GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataIn": "_texttospeech_24_GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataIn",
        "GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataOut": "_texttospeech_25_GoogleCloudTexttospeechV1SynthesizeLongAudioMetadataOut",
        "SynthesizeSpeechResponseIn": "_texttospeech_26_SynthesizeSpeechResponseIn",
        "SynthesizeSpeechResponseOut": "_texttospeech_27_SynthesizeSpeechResponseOut",
        "EmptyIn": "_texttospeech_28_EmptyIn",
        "EmptyOut": "_texttospeech_29_EmptyOut",
        "AudioConfigIn": "_texttospeech_30_AudioConfigIn",
        "AudioConfigOut": "_texttospeech_31_AudioConfigOut",
        "SynthesizeSpeechRequestIn": "_texttospeech_32_SynthesizeSpeechRequestIn",
        "SynthesizeSpeechRequestOut": "_texttospeech_33_SynthesizeSpeechRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
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
    types["SynthesisInputIn"] = t.struct(
        {"ssml": t.string().optional(), "text": t.string().optional()}
    ).named(renames["SynthesisInputIn"])
    types["SynthesisInputOut"] = t.struct(
        {
            "ssml": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SynthesisInputOut"])
    types["VoiceIn"] = t.struct(
        {
            "languageCodes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "naturalSampleRateHertz": t.integer().optional(),
            "ssmlGender": t.string().optional(),
        }
    ).named(renames["VoiceIn"])
    types["VoiceOut"] = t.struct(
        {
            "languageCodes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "naturalSampleRateHertz": t.integer().optional(),
            "ssmlGender": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceOut"])
    types["SynthesizeLongAudioRequestIn"] = t.struct(
        {
            "input": t.proxy(renames["SynthesisInputIn"]),
            "voice": t.proxy(renames["VoiceSelectionParamsIn"]),
            "outputGcsUri": t.string(),
            "audioConfig": t.proxy(renames["AudioConfigIn"]),
        }
    ).named(renames["SynthesizeLongAudioRequestIn"])
    types["SynthesizeLongAudioRequestOut"] = t.struct(
        {
            "input": t.proxy(renames["SynthesisInputOut"]),
            "voice": t.proxy(renames["VoiceSelectionParamsOut"]),
            "outputGcsUri": t.string(),
            "audioConfig": t.proxy(renames["AudioConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SynthesizeLongAudioRequestOut"])
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
    types["SynthesizeSpeechResponseIn"] = t.struct(
        {"audioContent": t.string().optional()}
    ).named(renames["SynthesizeSpeechResponseIn"])
    types["SynthesizeSpeechResponseOut"] = t.struct(
        {
            "audioContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SynthesizeSpeechResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["AudioConfigIn"] = t.struct(
        {
            "sampleRateHertz": t.integer().optional(),
            "volumeGainDb": t.number().optional(),
            "speakingRate": t.number().optional(),
            "audioEncoding": t.string(),
            "effectsProfileId": t.array(t.string()).optional(),
            "pitch": t.number().optional(),
        }
    ).named(renames["AudioConfigIn"])
    types["AudioConfigOut"] = t.struct(
        {
            "sampleRateHertz": t.integer().optional(),
            "volumeGainDb": t.number().optional(),
            "speakingRate": t.number().optional(),
            "audioEncoding": t.string(),
            "effectsProfileId": t.array(t.string()).optional(),
            "pitch": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioConfigOut"])
    types["SynthesizeSpeechRequestIn"] = t.struct(
        {
            "audioConfig": t.proxy(renames["AudioConfigIn"]),
            "input": t.proxy(renames["SynthesisInputIn"]),
            "voice": t.proxy(renames["VoiceSelectionParamsIn"]),
        }
    ).named(renames["SynthesizeSpeechRequestIn"])
    types["SynthesizeSpeechRequestOut"] = t.struct(
        {
            "audioConfig": t.proxy(renames["AudioConfigOut"]),
            "input": t.proxy(renames["SynthesisInputOut"]),
            "voice": t.proxy(renames["VoiceSelectionParamsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SynthesizeSpeechRequestOut"])

    functions = {}
    functions["textSynthesize"] = texttospeech.post(
        "v1/text:synthesize",
        t.struct(
            {
                "audioConfig": t.proxy(renames["AudioConfigIn"]),
                "input": t.proxy(renames["SynthesisInputIn"]),
                "voice": t.proxy(renames["VoiceSelectionParamsIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SynthesizeSpeechResponseOut"]),
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
    functions["projectsLocationsSynthesizeLongAudio"] = texttospeech.post(
        "v1/{parent}:synthesizeLongAudio",
        t.struct(
            {
                "parent": t.string().optional(),
                "input": t.proxy(renames["SynthesisInputIn"]),
                "voice": t.proxy(renames["VoiceSelectionParamsIn"]),
                "outputGcsUri": t.string(),
                "audioConfig": t.proxy(renames["AudioConfigIn"]),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
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

    return Import(
        importer="texttospeech",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
