from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_transcoder():
    transcoder = HTTPRuntime("https://transcoder.googleapis.com/")

    renames = {
        "ErrorResponse": "_transcoder_1_ErrorResponse",
        "BwdifConfigIn": "_transcoder_2_BwdifConfigIn",
        "BwdifConfigOut": "_transcoder_3_BwdifConfigOut",
        "AnimationEndIn": "_transcoder_4_AnimationEndIn",
        "AnimationEndOut": "_transcoder_5_AnimationEndOut",
        "H265CodecSettingsIn": "_transcoder_6_H265CodecSettingsIn",
        "H265CodecSettingsOut": "_transcoder_7_H265CodecSettingsOut",
        "EmptyIn": "_transcoder_8_EmptyIn",
        "EmptyOut": "_transcoder_9_EmptyOut",
        "Aes128EncryptionIn": "_transcoder_10_Aes128EncryptionIn",
        "Aes128EncryptionOut": "_transcoder_11_Aes128EncryptionOut",
        "AudioIn": "_transcoder_12_AudioIn",
        "AudioOut": "_transcoder_13_AudioOut",
        "JobConfigIn": "_transcoder_14_JobConfigIn",
        "JobConfigOut": "_transcoder_15_JobConfigOut",
        "MpegCommonEncryptionIn": "_transcoder_16_MpegCommonEncryptionIn",
        "MpegCommonEncryptionOut": "_transcoder_17_MpegCommonEncryptionOut",
        "AdBreakIn": "_transcoder_18_AdBreakIn",
        "AdBreakOut": "_transcoder_19_AdBreakOut",
        "AnimationIn": "_transcoder_20_AnimationIn",
        "AnimationOut": "_transcoder_21_AnimationOut",
        "OverlayIn": "_transcoder_22_OverlayIn",
        "OverlayOut": "_transcoder_23_OverlayOut",
        "PadIn": "_transcoder_24_PadIn",
        "PadOut": "_transcoder_25_PadOut",
        "JobIn": "_transcoder_26_JobIn",
        "JobOut": "_transcoder_27_JobOut",
        "DenoiseIn": "_transcoder_28_DenoiseIn",
        "DenoiseOut": "_transcoder_29_DenoiseOut",
        "PubsubDestinationIn": "_transcoder_30_PubsubDestinationIn",
        "PubsubDestinationOut": "_transcoder_31_PubsubDestinationOut",
        "AudioStreamIn": "_transcoder_32_AudioStreamIn",
        "AudioStreamOut": "_transcoder_33_AudioStreamOut",
        "ClearkeyIn": "_transcoder_34_ClearkeyIn",
        "ClearkeyOut": "_transcoder_35_ClearkeyOut",
        "DeblockIn": "_transcoder_36_DeblockIn",
        "DeblockOut": "_transcoder_37_DeblockOut",
        "EditAtomIn": "_transcoder_38_EditAtomIn",
        "EditAtomOut": "_transcoder_39_EditAtomOut",
        "ElementaryStreamIn": "_transcoder_40_ElementaryStreamIn",
        "ElementaryStreamOut": "_transcoder_41_ElementaryStreamOut",
        "EncryptionIn": "_transcoder_42_EncryptionIn",
        "EncryptionOut": "_transcoder_43_EncryptionOut",
        "JobTemplateIn": "_transcoder_44_JobTemplateIn",
        "JobTemplateOut": "_transcoder_45_JobTemplateOut",
        "ListJobTemplatesResponseIn": "_transcoder_46_ListJobTemplatesResponseIn",
        "ListJobTemplatesResponseOut": "_transcoder_47_ListJobTemplatesResponseOut",
        "InputIn": "_transcoder_48_InputIn",
        "InputOut": "_transcoder_49_InputOut",
        "AudioMappingIn": "_transcoder_50_AudioMappingIn",
        "AudioMappingOut": "_transcoder_51_AudioMappingOut",
        "SpriteSheetIn": "_transcoder_52_SpriteSheetIn",
        "SpriteSheetOut": "_transcoder_53_SpriteSheetOut",
        "ListJobsResponseIn": "_transcoder_54_ListJobsResponseIn",
        "ListJobsResponseOut": "_transcoder_55_ListJobsResponseOut",
        "WidevineIn": "_transcoder_56_WidevineIn",
        "WidevineOut": "_transcoder_57_WidevineOut",
        "TextMappingIn": "_transcoder_58_TextMappingIn",
        "TextMappingOut": "_transcoder_59_TextMappingOut",
        "PlayreadyIn": "_transcoder_60_PlayreadyIn",
        "PlayreadyOut": "_transcoder_61_PlayreadyOut",
        "ManifestIn": "_transcoder_62_ManifestIn",
        "ManifestOut": "_transcoder_63_ManifestOut",
        "CropIn": "_transcoder_64_CropIn",
        "CropOut": "_transcoder_65_CropOut",
        "ColorIn": "_transcoder_66_ColorIn",
        "ColorOut": "_transcoder_67_ColorOut",
        "SecretManagerSourceIn": "_transcoder_68_SecretManagerSourceIn",
        "SecretManagerSourceOut": "_transcoder_69_SecretManagerSourceOut",
        "Vp9CodecSettingsIn": "_transcoder_70_Vp9CodecSettingsIn",
        "Vp9CodecSettingsOut": "_transcoder_71_Vp9CodecSettingsOut",
        "SegmentSettingsIn": "_transcoder_72_SegmentSettingsIn",
        "SegmentSettingsOut": "_transcoder_73_SegmentSettingsOut",
        "StatusIn": "_transcoder_74_StatusIn",
        "StatusOut": "_transcoder_75_StatusOut",
        "NormalizedCoordinateIn": "_transcoder_76_NormalizedCoordinateIn",
        "NormalizedCoordinateOut": "_transcoder_77_NormalizedCoordinateOut",
        "FairplayIn": "_transcoder_78_FairplayIn",
        "FairplayOut": "_transcoder_79_FairplayOut",
        "OutputIn": "_transcoder_80_OutputIn",
        "OutputOut": "_transcoder_81_OutputOut",
        "DrmSystemsIn": "_transcoder_82_DrmSystemsIn",
        "DrmSystemsOut": "_transcoder_83_DrmSystemsOut",
        "VideoStreamIn": "_transcoder_84_VideoStreamIn",
        "VideoStreamOut": "_transcoder_85_VideoStreamOut",
        "YadifConfigIn": "_transcoder_86_YadifConfigIn",
        "YadifConfigOut": "_transcoder_87_YadifConfigOut",
        "DashConfigIn": "_transcoder_88_DashConfigIn",
        "DashConfigOut": "_transcoder_89_DashConfigOut",
        "TextStreamIn": "_transcoder_90_TextStreamIn",
        "TextStreamOut": "_transcoder_91_TextStreamOut",
        "DeinterlaceIn": "_transcoder_92_DeinterlaceIn",
        "DeinterlaceOut": "_transcoder_93_DeinterlaceOut",
        "AnimationFadeIn": "_transcoder_94_AnimationFadeIn",
        "AnimationFadeOut": "_transcoder_95_AnimationFadeOut",
        "ImageIn": "_transcoder_96_ImageIn",
        "ImageOut": "_transcoder_97_ImageOut",
        "MuxStreamIn": "_transcoder_98_MuxStreamIn",
        "MuxStreamOut": "_transcoder_99_MuxStreamOut",
        "PreprocessingConfigIn": "_transcoder_100_PreprocessingConfigIn",
        "PreprocessingConfigOut": "_transcoder_101_PreprocessingConfigOut",
        "SampleAesEncryptionIn": "_transcoder_102_SampleAesEncryptionIn",
        "SampleAesEncryptionOut": "_transcoder_103_SampleAesEncryptionOut",
        "H264CodecSettingsIn": "_transcoder_104_H264CodecSettingsIn",
        "H264CodecSettingsOut": "_transcoder_105_H264CodecSettingsOut",
        "AnimationStaticIn": "_transcoder_106_AnimationStaticIn",
        "AnimationStaticOut": "_transcoder_107_AnimationStaticOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BwdifConfigIn"] = t.struct(
        {
            "mode": t.string().optional(),
            "deinterlaceAllFrames": t.boolean().optional(),
            "parity": t.string().optional(),
        }
    ).named(renames["BwdifConfigIn"])
    types["BwdifConfigOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "deinterlaceAllFrames": t.boolean().optional(),
            "parity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BwdifConfigOut"])
    types["AnimationEndIn"] = t.struct(
        {"startTimeOffset": t.string().optional()}
    ).named(renames["AnimationEndIn"])
    types["AnimationEndOut"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnimationEndOut"])
    types["H265CodecSettingsIn"] = t.struct(
        {
            "bitrateBps": t.integer(),
            "widthPixels": t.integer().optional(),
            "tune": t.string().optional(),
            "vbvSizeBits": t.integer().optional(),
            "gopFrameCount": t.integer().optional(),
            "aqStrength": t.number().optional(),
            "preset": t.string().optional(),
            "pixelFormat": t.string().optional(),
            "bFrameCount": t.integer().optional(),
            "vbvFullnessBits": t.integer().optional(),
            "enableTwoPass": t.boolean().optional(),
            "frameRate": t.number(),
            "bPyramid": t.boolean().optional(),
            "allowOpenGop": t.boolean().optional(),
            "heightPixels": t.integer().optional(),
            "profile": t.string().optional(),
            "rateControlMode": t.string().optional(),
            "crfLevel": t.integer().optional(),
            "gopDuration": t.string().optional(),
        }
    ).named(renames["H265CodecSettingsIn"])
    types["H265CodecSettingsOut"] = t.struct(
        {
            "bitrateBps": t.integer(),
            "widthPixels": t.integer().optional(),
            "tune": t.string().optional(),
            "vbvSizeBits": t.integer().optional(),
            "gopFrameCount": t.integer().optional(),
            "aqStrength": t.number().optional(),
            "preset": t.string().optional(),
            "pixelFormat": t.string().optional(),
            "bFrameCount": t.integer().optional(),
            "vbvFullnessBits": t.integer().optional(),
            "enableTwoPass": t.boolean().optional(),
            "frameRate": t.number(),
            "bPyramid": t.boolean().optional(),
            "allowOpenGop": t.boolean().optional(),
            "heightPixels": t.integer().optional(),
            "profile": t.string().optional(),
            "rateControlMode": t.string().optional(),
            "crfLevel": t.integer().optional(),
            "gopDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["H265CodecSettingsOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["Aes128EncryptionIn"] = t.struct({"_": t.string().optional()}).named(
        renames["Aes128EncryptionIn"]
    )
    types["Aes128EncryptionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["Aes128EncryptionOut"])
    types["AudioIn"] = t.struct(
        {
            "lufs": t.number().optional(),
            "highBoost": t.boolean().optional(),
            "lowBoost": t.boolean().optional(),
        }
    ).named(renames["AudioIn"])
    types["AudioOut"] = t.struct(
        {
            "lufs": t.number().optional(),
            "highBoost": t.boolean().optional(),
            "lowBoost": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioOut"])
    types["JobConfigIn"] = t.struct(
        {
            "muxStreams": t.array(t.proxy(renames["MuxStreamIn"])).optional(),
            "inputs": t.array(t.proxy(renames["InputIn"])).optional(),
            "editList": t.array(t.proxy(renames["EditAtomIn"])).optional(),
            "manifests": t.array(t.proxy(renames["ManifestIn"])).optional(),
            "overlays": t.array(t.proxy(renames["OverlayIn"])).optional(),
            "encryptions": t.array(t.proxy(renames["EncryptionIn"])).optional(),
            "elementaryStreams": t.array(
                t.proxy(renames["ElementaryStreamIn"])
            ).optional(),
            "output": t.proxy(renames["OutputIn"]).optional(),
            "spriteSheets": t.array(t.proxy(renames["SpriteSheetIn"])).optional(),
            "adBreaks": t.array(t.proxy(renames["AdBreakIn"])).optional(),
            "pubsubDestination": t.proxy(renames["PubsubDestinationIn"]).optional(),
        }
    ).named(renames["JobConfigIn"])
    types["JobConfigOut"] = t.struct(
        {
            "muxStreams": t.array(t.proxy(renames["MuxStreamOut"])).optional(),
            "inputs": t.array(t.proxy(renames["InputOut"])).optional(),
            "editList": t.array(t.proxy(renames["EditAtomOut"])).optional(),
            "manifests": t.array(t.proxy(renames["ManifestOut"])).optional(),
            "overlays": t.array(t.proxy(renames["OverlayOut"])).optional(),
            "encryptions": t.array(t.proxy(renames["EncryptionOut"])).optional(),
            "elementaryStreams": t.array(
                t.proxy(renames["ElementaryStreamOut"])
            ).optional(),
            "output": t.proxy(renames["OutputOut"]).optional(),
            "spriteSheets": t.array(t.proxy(renames["SpriteSheetOut"])).optional(),
            "adBreaks": t.array(t.proxy(renames["AdBreakOut"])).optional(),
            "pubsubDestination": t.proxy(renames["PubsubDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobConfigOut"])
    types["MpegCommonEncryptionIn"] = t.struct({"scheme": t.string()}).named(
        renames["MpegCommonEncryptionIn"]
    )
    types["MpegCommonEncryptionOut"] = t.struct(
        {"scheme": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MpegCommonEncryptionOut"])
    types["AdBreakIn"] = t.struct({"startTimeOffset": t.string().optional()}).named(
        renames["AdBreakIn"]
    )
    types["AdBreakOut"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdBreakOut"])
    types["AnimationIn"] = t.struct(
        {
            "animationStatic": t.proxy(renames["AnimationStaticIn"]).optional(),
            "animationEnd": t.proxy(renames["AnimationEndIn"]).optional(),
            "animationFade": t.proxy(renames["AnimationFadeIn"]).optional(),
        }
    ).named(renames["AnimationIn"])
    types["AnimationOut"] = t.struct(
        {
            "animationStatic": t.proxy(renames["AnimationStaticOut"]).optional(),
            "animationEnd": t.proxy(renames["AnimationEndOut"]).optional(),
            "animationFade": t.proxy(renames["AnimationFadeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnimationOut"])
    types["OverlayIn"] = t.struct(
        {
            "image": t.proxy(renames["ImageIn"]).optional(),
            "animations": t.array(t.proxy(renames["AnimationIn"])).optional(),
        }
    ).named(renames["OverlayIn"])
    types["OverlayOut"] = t.struct(
        {
            "image": t.proxy(renames["ImageOut"]).optional(),
            "animations": t.array(t.proxy(renames["AnimationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OverlayOut"])
    types["PadIn"] = t.struct(
        {
            "bottomPixels": t.integer().optional(),
            "topPixels": t.integer().optional(),
            "rightPixels": t.integer().optional(),
            "leftPixels": t.integer().optional(),
        }
    ).named(renames["PadIn"])
    types["PadOut"] = t.struct(
        {
            "bottomPixels": t.integer().optional(),
            "topPixels": t.integer().optional(),
            "rightPixels": t.integer().optional(),
            "leftPixels": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PadOut"])
    types["JobIn"] = t.struct(
        {
            "ttlAfterCompletionDays": t.integer().optional(),
            "optimization": t.string().optional(),
            "batchModePriority": t.integer().optional(),
            "config": t.proxy(renames["JobConfigIn"]).optional(),
            "mode": t.string().optional(),
            "inputUri": t.string().optional(),
            "outputUri": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "templateId": t.string().optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "ttlAfterCompletionDays": t.integer().optional(),
            "optimization": t.string().optional(),
            "batchModePriority": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "endTime": t.string().optional(),
            "config": t.proxy(renames["JobConfigOut"]).optional(),
            "createTime": t.string().optional(),
            "mode": t.string().optional(),
            "inputUri": t.string().optional(),
            "outputUri": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "templateId": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["JobOut"])
    types["DenoiseIn"] = t.struct(
        {"strength": t.number().optional(), "tune": t.string().optional()}
    ).named(renames["DenoiseIn"])
    types["DenoiseOut"] = t.struct(
        {
            "strength": t.number().optional(),
            "tune": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DenoiseOut"])
    types["PubsubDestinationIn"] = t.struct({"topic": t.string().optional()}).named(
        renames["PubsubDestinationIn"]
    )
    types["PubsubDestinationOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubDestinationOut"])
    types["AudioStreamIn"] = t.struct(
        {
            "sampleRateHertz": t.integer().optional(),
            "mapping": t.array(t.proxy(renames["AudioMappingIn"])).optional(),
            "channelLayout": t.array(t.string()).optional(),
            "languageCode": t.string().optional(),
            "codec": t.string().optional(),
            "bitrateBps": t.integer(),
            "channelCount": t.integer().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["AudioStreamIn"])
    types["AudioStreamOut"] = t.struct(
        {
            "sampleRateHertz": t.integer().optional(),
            "mapping": t.array(t.proxy(renames["AudioMappingOut"])).optional(),
            "channelLayout": t.array(t.string()).optional(),
            "languageCode": t.string().optional(),
            "codec": t.string().optional(),
            "bitrateBps": t.integer(),
            "channelCount": t.integer().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioStreamOut"])
    types["ClearkeyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClearkeyIn"]
    )
    types["ClearkeyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ClearkeyOut"])
    types["DeblockIn"] = t.struct(
        {"enabled": t.boolean().optional(), "strength": t.number().optional()}
    ).named(renames["DeblockIn"])
    types["DeblockOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "strength": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeblockOut"])
    types["EditAtomIn"] = t.struct(
        {
            "inputs": t.array(t.string()).optional(),
            "key": t.string().optional(),
            "startTimeOffset": t.string().optional(),
            "endTimeOffset": t.string().optional(),
        }
    ).named(renames["EditAtomIn"])
    types["EditAtomOut"] = t.struct(
        {
            "inputs": t.array(t.string()).optional(),
            "key": t.string().optional(),
            "startTimeOffset": t.string().optional(),
            "endTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditAtomOut"])
    types["ElementaryStreamIn"] = t.struct(
        {
            "textStream": t.proxy(renames["TextStreamIn"]).optional(),
            "key": t.string().optional(),
            "videoStream": t.proxy(renames["VideoStreamIn"]).optional(),
            "audioStream": t.proxy(renames["AudioStreamIn"]).optional(),
        }
    ).named(renames["ElementaryStreamIn"])
    types["ElementaryStreamOut"] = t.struct(
        {
            "textStream": t.proxy(renames["TextStreamOut"]).optional(),
            "key": t.string().optional(),
            "videoStream": t.proxy(renames["VideoStreamOut"]).optional(),
            "audioStream": t.proxy(renames["AudioStreamOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ElementaryStreamOut"])
    types["EncryptionIn"] = t.struct(
        {
            "aes128": t.proxy(renames["Aes128EncryptionIn"]).optional(),
            "mpegCenc": t.proxy(renames["MpegCommonEncryptionIn"]).optional(),
            "id": t.string(),
            "secretManagerKeySource": t.proxy(
                renames["SecretManagerSourceIn"]
            ).optional(),
            "sampleAes": t.proxy(renames["SampleAesEncryptionIn"]).optional(),
            "drmSystems": t.proxy(renames["DrmSystemsIn"]),
        }
    ).named(renames["EncryptionIn"])
    types["EncryptionOut"] = t.struct(
        {
            "aes128": t.proxy(renames["Aes128EncryptionOut"]).optional(),
            "mpegCenc": t.proxy(renames["MpegCommonEncryptionOut"]).optional(),
            "id": t.string(),
            "secretManagerKeySource": t.proxy(
                renames["SecretManagerSourceOut"]
            ).optional(),
            "sampleAes": t.proxy(renames["SampleAesEncryptionOut"]).optional(),
            "drmSystems": t.proxy(renames["DrmSystemsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionOut"])
    types["JobTemplateIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "config": t.proxy(renames["JobConfigIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["JobTemplateIn"])
    types["JobTemplateOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "config": t.proxy(renames["JobConfigOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobTemplateOut"])
    types["ListJobTemplatesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "jobTemplates": t.array(t.proxy(renames["JobTemplateIn"])).optional(),
        }
    ).named(renames["ListJobTemplatesResponseIn"])
    types["ListJobTemplatesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "jobTemplates": t.array(t.proxy(renames["JobTemplateOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobTemplatesResponseOut"])
    types["InputIn"] = t.struct(
        {
            "preprocessingConfig": t.proxy(renames["PreprocessingConfigIn"]).optional(),
            "uri": t.string().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["InputIn"])
    types["InputOut"] = t.struct(
        {
            "preprocessingConfig": t.proxy(
                renames["PreprocessingConfigOut"]
            ).optional(),
            "uri": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputOut"])
    types["AudioMappingIn"] = t.struct(
        {
            "gainDb": t.number().optional(),
            "inputChannel": t.integer(),
            "inputTrack": t.integer(),
            "outputChannel": t.integer(),
            "inputKey": t.string(),
            "atomKey": t.string(),
        }
    ).named(renames["AudioMappingIn"])
    types["AudioMappingOut"] = t.struct(
        {
            "gainDb": t.number().optional(),
            "inputChannel": t.integer(),
            "inputTrack": t.integer(),
            "outputChannel": t.integer(),
            "inputKey": t.string(),
            "atomKey": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioMappingOut"])
    types["SpriteSheetIn"] = t.struct(
        {
            "quality": t.integer().optional(),
            "columnCount": t.integer().optional(),
            "startTimeOffset": t.string().optional(),
            "totalCount": t.integer().optional(),
            "rowCount": t.integer().optional(),
            "interval": t.string().optional(),
            "spriteHeightPixels": t.integer(),
            "format": t.string().optional(),
            "endTimeOffset": t.string().optional(),
            "spriteWidthPixels": t.integer(),
            "filePrefix": t.string(),
        }
    ).named(renames["SpriteSheetIn"])
    types["SpriteSheetOut"] = t.struct(
        {
            "quality": t.integer().optional(),
            "columnCount": t.integer().optional(),
            "startTimeOffset": t.string().optional(),
            "totalCount": t.integer().optional(),
            "rowCount": t.integer().optional(),
            "interval": t.string().optional(),
            "spriteHeightPixels": t.integer(),
            "format": t.string().optional(),
            "endTimeOffset": t.string().optional(),
            "spriteWidthPixels": t.integer(),
            "filePrefix": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpriteSheetOut"])
    types["ListJobsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobs": t.array(t.proxy(renames["JobIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListJobsResponseIn"])
    types["ListJobsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobsResponseOut"])
    types["WidevineIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WidevineIn"]
    )
    types["WidevineOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WidevineOut"])
    types["TextMappingIn"] = t.struct(
        {"inputKey": t.string(), "atomKey": t.string(), "inputTrack": t.integer()}
    ).named(renames["TextMappingIn"])
    types["TextMappingOut"] = t.struct(
        {
            "inputKey": t.string(),
            "atomKey": t.string(),
            "inputTrack": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextMappingOut"])
    types["PlayreadyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PlayreadyIn"]
    )
    types["PlayreadyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PlayreadyOut"])
    types["ManifestIn"] = t.struct(
        {
            "fileName": t.string().optional(),
            "muxStreams": t.array(t.string()),
            "type": t.string(),
            "dash": t.proxy(renames["DashConfigIn"]).optional(),
        }
    ).named(renames["ManifestIn"])
    types["ManifestOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "muxStreams": t.array(t.string()),
            "type": t.string(),
            "dash": t.proxy(renames["DashConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManifestOut"])
    types["CropIn"] = t.struct(
        {
            "bottomPixels": t.integer().optional(),
            "leftPixels": t.integer().optional(),
            "topPixels": t.integer().optional(),
            "rightPixels": t.integer().optional(),
        }
    ).named(renames["CropIn"])
    types["CropOut"] = t.struct(
        {
            "bottomPixels": t.integer().optional(),
            "leftPixels": t.integer().optional(),
            "topPixels": t.integer().optional(),
            "rightPixels": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropOut"])
    types["ColorIn"] = t.struct(
        {
            "saturation": t.number().optional(),
            "contrast": t.number().optional(),
            "brightness": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "saturation": t.number().optional(),
            "contrast": t.number().optional(),
            "brightness": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["SecretManagerSourceIn"] = t.struct({"secretVersion": t.string()}).named(
        renames["SecretManagerSourceIn"]
    )
    types["SecretManagerSourceOut"] = t.struct(
        {
            "secretVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretManagerSourceOut"])
    types["Vp9CodecSettingsIn"] = t.struct(
        {
            "pixelFormat": t.string().optional(),
            "widthPixels": t.integer().optional(),
            "gopDuration": t.string().optional(),
            "crfLevel": t.integer().optional(),
            "profile": t.string().optional(),
            "frameRate": t.number(),
            "bitrateBps": t.integer(),
            "gopFrameCount": t.integer().optional(),
            "heightPixels": t.integer().optional(),
            "rateControlMode": t.string().optional(),
        }
    ).named(renames["Vp9CodecSettingsIn"])
    types["Vp9CodecSettingsOut"] = t.struct(
        {
            "pixelFormat": t.string().optional(),
            "widthPixels": t.integer().optional(),
            "gopDuration": t.string().optional(),
            "crfLevel": t.integer().optional(),
            "profile": t.string().optional(),
            "frameRate": t.number(),
            "bitrateBps": t.integer(),
            "gopFrameCount": t.integer().optional(),
            "heightPixels": t.integer().optional(),
            "rateControlMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Vp9CodecSettingsOut"])
    types["SegmentSettingsIn"] = t.struct(
        {"segmentDuration": t.string().optional(), "individualSegments": t.boolean()}
    ).named(renames["SegmentSettingsIn"])
    types["SegmentSettingsOut"] = t.struct(
        {
            "segmentDuration": t.string().optional(),
            "individualSegments": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentSettingsOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["NormalizedCoordinateIn"] = t.struct(
        {"x": t.number().optional(), "y": t.number().optional()}
    ).named(renames["NormalizedCoordinateIn"])
    types["NormalizedCoordinateOut"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NormalizedCoordinateOut"])
    types["FairplayIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FairplayIn"]
    )
    types["FairplayOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FairplayOut"])
    types["OutputIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["OutputIn"]
    )
    types["OutputOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutputOut"])
    types["DrmSystemsIn"] = t.struct(
        {
            "clearkey": t.proxy(renames["ClearkeyIn"]).optional(),
            "playready": t.proxy(renames["PlayreadyIn"]).optional(),
            "widevine": t.proxy(renames["WidevineIn"]).optional(),
            "fairplay": t.proxy(renames["FairplayIn"]).optional(),
        }
    ).named(renames["DrmSystemsIn"])
    types["DrmSystemsOut"] = t.struct(
        {
            "clearkey": t.proxy(renames["ClearkeyOut"]).optional(),
            "playready": t.proxy(renames["PlayreadyOut"]).optional(),
            "widevine": t.proxy(renames["WidevineOut"]).optional(),
            "fairplay": t.proxy(renames["FairplayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DrmSystemsOut"])
    types["VideoStreamIn"] = t.struct(
        {
            "h265": t.proxy(renames["H265CodecSettingsIn"]).optional(),
            "vp9": t.proxy(renames["Vp9CodecSettingsIn"]).optional(),
            "h264": t.proxy(renames["H264CodecSettingsIn"]).optional(),
        }
    ).named(renames["VideoStreamIn"])
    types["VideoStreamOut"] = t.struct(
        {
            "h265": t.proxy(renames["H265CodecSettingsOut"]).optional(),
            "vp9": t.proxy(renames["Vp9CodecSettingsOut"]).optional(),
            "h264": t.proxy(renames["H264CodecSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoStreamOut"])
    types["YadifConfigIn"] = t.struct(
        {
            "deinterlaceAllFrames": t.boolean().optional(),
            "mode": t.string().optional(),
            "parity": t.string().optional(),
            "disableSpatialInterlacing": t.boolean().optional(),
        }
    ).named(renames["YadifConfigIn"])
    types["YadifConfigOut"] = t.struct(
        {
            "deinterlaceAllFrames": t.boolean().optional(),
            "mode": t.string().optional(),
            "parity": t.string().optional(),
            "disableSpatialInterlacing": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YadifConfigOut"])
    types["DashConfigIn"] = t.struct(
        {"segmentReferenceScheme": t.string().optional()}
    ).named(renames["DashConfigIn"])
    types["DashConfigOut"] = t.struct(
        {
            "segmentReferenceScheme": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DashConfigOut"])
    types["TextStreamIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "codec": t.string().optional(),
            "mapping": t.array(t.proxy(renames["TextMappingIn"])).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["TextStreamIn"])
    types["TextStreamOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "codec": t.string().optional(),
            "mapping": t.array(t.proxy(renames["TextMappingOut"])).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextStreamOut"])
    types["DeinterlaceIn"] = t.struct(
        {
            "bwdif": t.proxy(renames["BwdifConfigIn"]).optional(),
            "yadif": t.proxy(renames["YadifConfigIn"]).optional(),
        }
    ).named(renames["DeinterlaceIn"])
    types["DeinterlaceOut"] = t.struct(
        {
            "bwdif": t.proxy(renames["BwdifConfigOut"]).optional(),
            "yadif": t.proxy(renames["YadifConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeinterlaceOut"])
    types["AnimationFadeIn"] = t.struct(
        {
            "endTimeOffset": t.string().optional(),
            "fadeType": t.string(),
            "xy": t.proxy(renames["NormalizedCoordinateIn"]).optional(),
            "startTimeOffset": t.string().optional(),
        }
    ).named(renames["AnimationFadeIn"])
    types["AnimationFadeOut"] = t.struct(
        {
            "endTimeOffset": t.string().optional(),
            "fadeType": t.string(),
            "xy": t.proxy(renames["NormalizedCoordinateOut"]).optional(),
            "startTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnimationFadeOut"])
    types["ImageIn"] = t.struct(
        {
            "resolution": t.proxy(renames["NormalizedCoordinateIn"]).optional(),
            "alpha": t.number().optional(),
            "uri": t.string(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "resolution": t.proxy(renames["NormalizedCoordinateOut"]).optional(),
            "alpha": t.number().optional(),
            "uri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["MuxStreamIn"] = t.struct(
        {
            "fileName": t.string().optional(),
            "container": t.string().optional(),
            "elementaryStreams": t.array(t.string()).optional(),
            "encryptionId": t.string().optional(),
            "segmentSettings": t.proxy(renames["SegmentSettingsIn"]).optional(),
            "key": t.string().optional(),
        }
    ).named(renames["MuxStreamIn"])
    types["MuxStreamOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "container": t.string().optional(),
            "elementaryStreams": t.array(t.string()).optional(),
            "encryptionId": t.string().optional(),
            "segmentSettings": t.proxy(renames["SegmentSettingsOut"]).optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MuxStreamOut"])
    types["PreprocessingConfigIn"] = t.struct(
        {
            "color": t.proxy(renames["ColorIn"]).optional(),
            "deinterlace": t.proxy(renames["DeinterlaceIn"]).optional(),
            "crop": t.proxy(renames["CropIn"]).optional(),
            "deblock": t.proxy(renames["DeblockIn"]).optional(),
            "denoise": t.proxy(renames["DenoiseIn"]).optional(),
            "audio": t.proxy(renames["AudioIn"]).optional(),
            "pad": t.proxy(renames["PadIn"]).optional(),
        }
    ).named(renames["PreprocessingConfigIn"])
    types["PreprocessingConfigOut"] = t.struct(
        {
            "color": t.proxy(renames["ColorOut"]).optional(),
            "deinterlace": t.proxy(renames["DeinterlaceOut"]).optional(),
            "crop": t.proxy(renames["CropOut"]).optional(),
            "deblock": t.proxy(renames["DeblockOut"]).optional(),
            "denoise": t.proxy(renames["DenoiseOut"]).optional(),
            "audio": t.proxy(renames["AudioOut"]).optional(),
            "pad": t.proxy(renames["PadOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PreprocessingConfigOut"])
    types["SampleAesEncryptionIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SampleAesEncryptionIn"]
    )
    types["SampleAesEncryptionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SampleAesEncryptionOut"])
    types["H264CodecSettingsIn"] = t.struct(
        {
            "vbvFullnessBits": t.integer().optional(),
            "crfLevel": t.integer().optional(),
            "pixelFormat": t.string().optional(),
            "profile": t.string().optional(),
            "gopFrameCount": t.integer().optional(),
            "tune": t.string().optional(),
            "rateControlMode": t.string().optional(),
            "entropyCoder": t.string().optional(),
            "heightPixels": t.integer().optional(),
            "vbvSizeBits": t.integer().optional(),
            "frameRate": t.number(),
            "bPyramid": t.boolean().optional(),
            "allowOpenGop": t.boolean().optional(),
            "gopDuration": t.string().optional(),
            "preset": t.string().optional(),
            "bFrameCount": t.integer().optional(),
            "bitrateBps": t.integer(),
            "aqStrength": t.number().optional(),
            "enableTwoPass": t.boolean().optional(),
            "widthPixels": t.integer().optional(),
        }
    ).named(renames["H264CodecSettingsIn"])
    types["H264CodecSettingsOut"] = t.struct(
        {
            "vbvFullnessBits": t.integer().optional(),
            "crfLevel": t.integer().optional(),
            "pixelFormat": t.string().optional(),
            "profile": t.string().optional(),
            "gopFrameCount": t.integer().optional(),
            "tune": t.string().optional(),
            "rateControlMode": t.string().optional(),
            "entropyCoder": t.string().optional(),
            "heightPixels": t.integer().optional(),
            "vbvSizeBits": t.integer().optional(),
            "frameRate": t.number(),
            "bPyramid": t.boolean().optional(),
            "allowOpenGop": t.boolean().optional(),
            "gopDuration": t.string().optional(),
            "preset": t.string().optional(),
            "bFrameCount": t.integer().optional(),
            "bitrateBps": t.integer(),
            "aqStrength": t.number().optional(),
            "enableTwoPass": t.boolean().optional(),
            "widthPixels": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["H264CodecSettingsOut"])
    types["AnimationStaticIn"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "xy": t.proxy(renames["NormalizedCoordinateIn"]).optional(),
        }
    ).named(renames["AnimationStaticIn"])
    types["AnimationStaticOut"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "xy": t.proxy(renames["NormalizedCoordinateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnimationStaticOut"])

    functions = {}
    functions["projectsLocationsJobTemplatesGet"] = transcoder.get(
        "v1/{parent}/jobTemplates",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobTemplatesDelete"] = transcoder.get(
        "v1/{parent}/jobTemplates",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobTemplatesCreate"] = transcoder.get(
        "v1/{parent}/jobTemplates",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobTemplatesList"] = transcoder.get(
        "v1/{parent}/jobTemplates",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsCreate"] = transcoder.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGet"] = transcoder.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsDelete"] = transcoder.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsList"] = transcoder.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="transcoder",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
