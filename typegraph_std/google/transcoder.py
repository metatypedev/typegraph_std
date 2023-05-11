from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_transcoder() -> Import:
    transcoder = HTTPRuntime("https://transcoder.googleapis.com/")

    renames = {
        "ErrorResponse": "_transcoder_1_ErrorResponse",
        "JobTemplateIn": "_transcoder_2_JobTemplateIn",
        "JobTemplateOut": "_transcoder_3_JobTemplateOut",
        "ListJobsResponseIn": "_transcoder_4_ListJobsResponseIn",
        "ListJobsResponseOut": "_transcoder_5_ListJobsResponseOut",
        "AnimationEndIn": "_transcoder_6_AnimationEndIn",
        "AnimationEndOut": "_transcoder_7_AnimationEndOut",
        "PreprocessingConfigIn": "_transcoder_8_PreprocessingConfigIn",
        "PreprocessingConfigOut": "_transcoder_9_PreprocessingConfigOut",
        "ColorIn": "_transcoder_10_ColorIn",
        "ColorOut": "_transcoder_11_ColorOut",
        "VideoStreamIn": "_transcoder_12_VideoStreamIn",
        "VideoStreamOut": "_transcoder_13_VideoStreamOut",
        "AudioMappingIn": "_transcoder_14_AudioMappingIn",
        "AudioMappingOut": "_transcoder_15_AudioMappingOut",
        "AnimationStaticIn": "_transcoder_16_AnimationStaticIn",
        "AnimationStaticOut": "_transcoder_17_AnimationStaticOut",
        "ElementaryStreamIn": "_transcoder_18_ElementaryStreamIn",
        "ElementaryStreamOut": "_transcoder_19_ElementaryStreamOut",
        "TextMappingIn": "_transcoder_20_TextMappingIn",
        "TextMappingOut": "_transcoder_21_TextMappingOut",
        "SpriteSheetIn": "_transcoder_22_SpriteSheetIn",
        "SpriteSheetOut": "_transcoder_23_SpriteSheetOut",
        "EditAtomIn": "_transcoder_24_EditAtomIn",
        "EditAtomOut": "_transcoder_25_EditAtomOut",
        "YadifConfigIn": "_transcoder_26_YadifConfigIn",
        "YadifConfigOut": "_transcoder_27_YadifConfigOut",
        "DeinterlaceIn": "_transcoder_28_DeinterlaceIn",
        "DeinterlaceOut": "_transcoder_29_DeinterlaceOut",
        "OverlayIn": "_transcoder_30_OverlayIn",
        "OverlayOut": "_transcoder_31_OverlayOut",
        "H264CodecSettingsIn": "_transcoder_32_H264CodecSettingsIn",
        "H264CodecSettingsOut": "_transcoder_33_H264CodecSettingsOut",
        "SegmentSettingsIn": "_transcoder_34_SegmentSettingsIn",
        "SegmentSettingsOut": "_transcoder_35_SegmentSettingsOut",
        "JobConfigIn": "_transcoder_36_JobConfigIn",
        "JobConfigOut": "_transcoder_37_JobConfigOut",
        "AnimationIn": "_transcoder_38_AnimationIn",
        "AnimationOut": "_transcoder_39_AnimationOut",
        "TextStreamIn": "_transcoder_40_TextStreamIn",
        "TextStreamOut": "_transcoder_41_TextStreamOut",
        "ImageIn": "_transcoder_42_ImageIn",
        "ImageOut": "_transcoder_43_ImageOut",
        "InputIn": "_transcoder_44_InputIn",
        "InputOut": "_transcoder_45_InputOut",
        "StatusIn": "_transcoder_46_StatusIn",
        "StatusOut": "_transcoder_47_StatusOut",
        "MuxStreamIn": "_transcoder_48_MuxStreamIn",
        "MuxStreamOut": "_transcoder_49_MuxStreamOut",
        "JobIn": "_transcoder_50_JobIn",
        "JobOut": "_transcoder_51_JobOut",
        "ManifestIn": "_transcoder_52_ManifestIn",
        "ManifestOut": "_transcoder_53_ManifestOut",
        "AudioStreamIn": "_transcoder_54_AudioStreamIn",
        "AudioStreamOut": "_transcoder_55_AudioStreamOut",
        "NormalizedCoordinateIn": "_transcoder_56_NormalizedCoordinateIn",
        "NormalizedCoordinateOut": "_transcoder_57_NormalizedCoordinateOut",
        "ListJobTemplatesResponseIn": "_transcoder_58_ListJobTemplatesResponseIn",
        "ListJobTemplatesResponseOut": "_transcoder_59_ListJobTemplatesResponseOut",
        "AdBreakIn": "_transcoder_60_AdBreakIn",
        "AdBreakOut": "_transcoder_61_AdBreakOut",
        "OutputIn": "_transcoder_62_OutputIn",
        "OutputOut": "_transcoder_63_OutputOut",
        "PadIn": "_transcoder_64_PadIn",
        "PadOut": "_transcoder_65_PadOut",
        "DeblockIn": "_transcoder_66_DeblockIn",
        "DeblockOut": "_transcoder_67_DeblockOut",
        "PubsubDestinationIn": "_transcoder_68_PubsubDestinationIn",
        "PubsubDestinationOut": "_transcoder_69_PubsubDestinationOut",
        "AudioIn": "_transcoder_70_AudioIn",
        "AudioOut": "_transcoder_71_AudioOut",
        "BwdifConfigIn": "_transcoder_72_BwdifConfigIn",
        "BwdifConfigOut": "_transcoder_73_BwdifConfigOut",
        "CropIn": "_transcoder_74_CropIn",
        "CropOut": "_transcoder_75_CropOut",
        "EmptyIn": "_transcoder_76_EmptyIn",
        "EmptyOut": "_transcoder_77_EmptyOut",
        "H265CodecSettingsIn": "_transcoder_78_H265CodecSettingsIn",
        "H265CodecSettingsOut": "_transcoder_79_H265CodecSettingsOut",
        "AnimationFadeIn": "_transcoder_80_AnimationFadeIn",
        "AnimationFadeOut": "_transcoder_81_AnimationFadeOut",
        "DenoiseIn": "_transcoder_82_DenoiseIn",
        "DenoiseOut": "_transcoder_83_DenoiseOut",
        "Vp9CodecSettingsIn": "_transcoder_84_Vp9CodecSettingsIn",
        "Vp9CodecSettingsOut": "_transcoder_85_Vp9CodecSettingsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ListJobsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "jobs": t.array(t.proxy(renames["JobIn"])).optional(),
        }
    ).named(renames["ListJobsResponseIn"])
    types["ListJobsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "jobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobsResponseOut"])
    types["AnimationEndIn"] = t.struct(
        {"startTimeOffset": t.string().optional()}
    ).named(renames["AnimationEndIn"])
    types["AnimationEndOut"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnimationEndOut"])
    types["PreprocessingConfigIn"] = t.struct(
        {
            "pad": t.proxy(renames["PadIn"]).optional(),
            "audio": t.proxy(renames["AudioIn"]).optional(),
            "deinterlace": t.proxy(renames["DeinterlaceIn"]).optional(),
            "deblock": t.proxy(renames["DeblockIn"]).optional(),
            "denoise": t.proxy(renames["DenoiseIn"]).optional(),
            "crop": t.proxy(renames["CropIn"]).optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["PreprocessingConfigIn"])
    types["PreprocessingConfigOut"] = t.struct(
        {
            "pad": t.proxy(renames["PadOut"]).optional(),
            "audio": t.proxy(renames["AudioOut"]).optional(),
            "deinterlace": t.proxy(renames["DeinterlaceOut"]).optional(),
            "deblock": t.proxy(renames["DeblockOut"]).optional(),
            "denoise": t.proxy(renames["DenoiseOut"]).optional(),
            "crop": t.proxy(renames["CropOut"]).optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PreprocessingConfigOut"])
    types["ColorIn"] = t.struct(
        {
            "contrast": t.number().optional(),
            "saturation": t.number().optional(),
            "brightness": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "contrast": t.number().optional(),
            "saturation": t.number().optional(),
            "brightness": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["VideoStreamIn"] = t.struct(
        {
            "h265": t.proxy(renames["H265CodecSettingsIn"]).optional(),
            "h264": t.proxy(renames["H264CodecSettingsIn"]).optional(),
            "vp9": t.proxy(renames["Vp9CodecSettingsIn"]).optional(),
        }
    ).named(renames["VideoStreamIn"])
    types["VideoStreamOut"] = t.struct(
        {
            "h265": t.proxy(renames["H265CodecSettingsOut"]).optional(),
            "h264": t.proxy(renames["H264CodecSettingsOut"]).optional(),
            "vp9": t.proxy(renames["Vp9CodecSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoStreamOut"])
    types["AudioMappingIn"] = t.struct(
        {
            "inputKey": t.string(),
            "gainDb": t.number().optional(),
            "atomKey": t.string(),
            "inputTrack": t.integer(),
            "inputChannel": t.integer(),
            "outputChannel": t.integer(),
        }
    ).named(renames["AudioMappingIn"])
    types["AudioMappingOut"] = t.struct(
        {
            "inputKey": t.string(),
            "gainDb": t.number().optional(),
            "atomKey": t.string(),
            "inputTrack": t.integer(),
            "inputChannel": t.integer(),
            "outputChannel": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioMappingOut"])
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
    types["ElementaryStreamIn"] = t.struct(
        {
            "key": t.string().optional(),
            "videoStream": t.proxy(renames["VideoStreamIn"]).optional(),
            "textStream": t.proxy(renames["TextStreamIn"]).optional(),
            "audioStream": t.proxy(renames["AudioStreamIn"]).optional(),
        }
    ).named(renames["ElementaryStreamIn"])
    types["ElementaryStreamOut"] = t.struct(
        {
            "key": t.string().optional(),
            "videoStream": t.proxy(renames["VideoStreamOut"]).optional(),
            "textStream": t.proxy(renames["TextStreamOut"]).optional(),
            "audioStream": t.proxy(renames["AudioStreamOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ElementaryStreamOut"])
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
    types["SpriteSheetIn"] = t.struct(
        {
            "format": t.string().optional(),
            "rowCount": t.integer().optional(),
            "quality": t.integer().optional(),
            "startTimeOffset": t.string().optional(),
            "spriteWidthPixels": t.integer(),
            "filePrefix": t.string(),
            "totalCount": t.integer().optional(),
            "spriteHeightPixels": t.integer(),
            "endTimeOffset": t.string().optional(),
            "interval": t.string().optional(),
            "columnCount": t.integer().optional(),
        }
    ).named(renames["SpriteSheetIn"])
    types["SpriteSheetOut"] = t.struct(
        {
            "format": t.string().optional(),
            "rowCount": t.integer().optional(),
            "quality": t.integer().optional(),
            "startTimeOffset": t.string().optional(),
            "spriteWidthPixels": t.integer(),
            "filePrefix": t.string(),
            "totalCount": t.integer().optional(),
            "spriteHeightPixels": t.integer(),
            "endTimeOffset": t.string().optional(),
            "interval": t.string().optional(),
            "columnCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpriteSheetOut"])
    types["EditAtomIn"] = t.struct(
        {
            "inputs": t.array(t.string()).optional(),
            "key": t.string().optional(),
            "endTimeOffset": t.string().optional(),
            "startTimeOffset": t.string().optional(),
        }
    ).named(renames["EditAtomIn"])
    types["EditAtomOut"] = t.struct(
        {
            "inputs": t.array(t.string()).optional(),
            "key": t.string().optional(),
            "endTimeOffset": t.string().optional(),
            "startTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditAtomOut"])
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
    types["DeinterlaceIn"] = t.struct(
        {
            "yadif": t.proxy(renames["YadifConfigIn"]).optional(),
            "bwdif": t.proxy(renames["BwdifConfigIn"]).optional(),
        }
    ).named(renames["DeinterlaceIn"])
    types["DeinterlaceOut"] = t.struct(
        {
            "yadif": t.proxy(renames["YadifConfigOut"]).optional(),
            "bwdif": t.proxy(renames["BwdifConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeinterlaceOut"])
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
    types["H264CodecSettingsIn"] = t.struct(
        {
            "rateControlMode": t.string().optional(),
            "vbvFullnessBits": t.integer().optional(),
            "profile": t.string().optional(),
            "gopDuration": t.string().optional(),
            "bFrameCount": t.integer().optional(),
            "bitrateBps": t.integer(),
            "aqStrength": t.number().optional(),
            "pixelFormat": t.string().optional(),
            "widthPixels": t.integer().optional(),
            "vbvSizeBits": t.integer().optional(),
            "entropyCoder": t.string().optional(),
            "crfLevel": t.integer().optional(),
            "enableTwoPass": t.boolean().optional(),
            "heightPixels": t.integer().optional(),
            "allowOpenGop": t.boolean().optional(),
            "bPyramid": t.boolean().optional(),
            "tune": t.string().optional(),
            "preset": t.string().optional(),
            "gopFrameCount": t.integer().optional(),
            "frameRate": t.number(),
        }
    ).named(renames["H264CodecSettingsIn"])
    types["H264CodecSettingsOut"] = t.struct(
        {
            "rateControlMode": t.string().optional(),
            "vbvFullnessBits": t.integer().optional(),
            "profile": t.string().optional(),
            "gopDuration": t.string().optional(),
            "bFrameCount": t.integer().optional(),
            "bitrateBps": t.integer(),
            "aqStrength": t.number().optional(),
            "pixelFormat": t.string().optional(),
            "widthPixels": t.integer().optional(),
            "vbvSizeBits": t.integer().optional(),
            "entropyCoder": t.string().optional(),
            "crfLevel": t.integer().optional(),
            "enableTwoPass": t.boolean().optional(),
            "heightPixels": t.integer().optional(),
            "allowOpenGop": t.boolean().optional(),
            "bPyramid": t.boolean().optional(),
            "tune": t.string().optional(),
            "preset": t.string().optional(),
            "gopFrameCount": t.integer().optional(),
            "frameRate": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["H264CodecSettingsOut"])
    types["SegmentSettingsIn"] = t.struct(
        {"individualSegments": t.boolean(), "segmentDuration": t.string().optional()}
    ).named(renames["SegmentSettingsIn"])
    types["SegmentSettingsOut"] = t.struct(
        {
            "individualSegments": t.boolean(),
            "segmentDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentSettingsOut"])
    types["JobConfigIn"] = t.struct(
        {
            "muxStreams": t.array(t.proxy(renames["MuxStreamIn"])).optional(),
            "pubsubDestination": t.proxy(renames["PubsubDestinationIn"]).optional(),
            "editList": t.array(t.proxy(renames["EditAtomIn"])).optional(),
            "spriteSheets": t.array(t.proxy(renames["SpriteSheetIn"])).optional(),
            "inputs": t.array(t.proxy(renames["InputIn"])).optional(),
            "adBreaks": t.array(t.proxy(renames["AdBreakIn"])).optional(),
            "overlays": t.array(t.proxy(renames["OverlayIn"])).optional(),
            "output": t.proxy(renames["OutputIn"]).optional(),
            "manifests": t.array(t.proxy(renames["ManifestIn"])).optional(),
            "elementaryStreams": t.array(
                t.proxy(renames["ElementaryStreamIn"])
            ).optional(),
        }
    ).named(renames["JobConfigIn"])
    types["JobConfigOut"] = t.struct(
        {
            "muxStreams": t.array(t.proxy(renames["MuxStreamOut"])).optional(),
            "pubsubDestination": t.proxy(renames["PubsubDestinationOut"]).optional(),
            "editList": t.array(t.proxy(renames["EditAtomOut"])).optional(),
            "spriteSheets": t.array(t.proxy(renames["SpriteSheetOut"])).optional(),
            "inputs": t.array(t.proxy(renames["InputOut"])).optional(),
            "adBreaks": t.array(t.proxy(renames["AdBreakOut"])).optional(),
            "overlays": t.array(t.proxy(renames["OverlayOut"])).optional(),
            "output": t.proxy(renames["OutputOut"]).optional(),
            "manifests": t.array(t.proxy(renames["ManifestOut"])).optional(),
            "elementaryStreams": t.array(
                t.proxy(renames["ElementaryStreamOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobConfigOut"])
    types["AnimationIn"] = t.struct(
        {
            "animationFade": t.proxy(renames["AnimationFadeIn"]).optional(),
            "animationEnd": t.proxy(renames["AnimationEndIn"]).optional(),
            "animationStatic": t.proxy(renames["AnimationStaticIn"]).optional(),
        }
    ).named(renames["AnimationIn"])
    types["AnimationOut"] = t.struct(
        {
            "animationFade": t.proxy(renames["AnimationFadeOut"]).optional(),
            "animationEnd": t.proxy(renames["AnimationEndOut"]).optional(),
            "animationStatic": t.proxy(renames["AnimationStaticOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnimationOut"])
    types["TextStreamIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "mapping": t.array(t.proxy(renames["TextMappingIn"])).optional(),
            "displayName": t.string().optional(),
            "codec": t.string().optional(),
        }
    ).named(renames["TextStreamIn"])
    types["TextStreamOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "mapping": t.array(t.proxy(renames["TextMappingOut"])).optional(),
            "displayName": t.string().optional(),
            "codec": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextStreamOut"])
    types["ImageIn"] = t.struct(
        {
            "uri": t.string(),
            "alpha": t.number().optional(),
            "resolution": t.proxy(renames["NormalizedCoordinateIn"]).optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "uri": t.string(),
            "alpha": t.number().optional(),
            "resolution": t.proxy(renames["NormalizedCoordinateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["InputIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "key": t.string().optional(),
            "preprocessingConfig": t.proxy(renames["PreprocessingConfigIn"]).optional(),
        }
    ).named(renames["InputIn"])
    types["InputOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "key": t.string().optional(),
            "preprocessingConfig": t.proxy(
                renames["PreprocessingConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputOut"])
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
    types["MuxStreamIn"] = t.struct(
        {
            "container": t.string().optional(),
            "fileName": t.string().optional(),
            "segmentSettings": t.proxy(renames["SegmentSettingsIn"]).optional(),
            "key": t.string().optional(),
            "elementaryStreams": t.array(t.string()).optional(),
        }
    ).named(renames["MuxStreamIn"])
    types["MuxStreamOut"] = t.struct(
        {
            "container": t.string().optional(),
            "fileName": t.string().optional(),
            "segmentSettings": t.proxy(renames["SegmentSettingsOut"]).optional(),
            "key": t.string().optional(),
            "elementaryStreams": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MuxStreamOut"])
    types["JobIn"] = t.struct(
        {
            "outputUri": t.string().optional(),
            "inputUri": t.string().optional(),
            "mode": t.string().optional(),
            "templateId": t.string().optional(),
            "name": t.string().optional(),
            "config": t.proxy(renames["JobConfigIn"]).optional(),
            "ttlAfterCompletionDays": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "outputUri": t.string().optional(),
            "state": t.string().optional(),
            "inputUri": t.string().optional(),
            "mode": t.string().optional(),
            "templateId": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "config": t.proxy(renames["JobConfigOut"]).optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "ttlAfterCompletionDays": t.integer().optional(),
            "endTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["JobOut"])
    types["ManifestIn"] = t.struct(
        {
            "type": t.string(),
            "fileName": t.string().optional(),
            "muxStreams": t.array(t.string()),
        }
    ).named(renames["ManifestIn"])
    types["ManifestOut"] = t.struct(
        {
            "type": t.string(),
            "fileName": t.string().optional(),
            "muxStreams": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManifestOut"])
    types["AudioStreamIn"] = t.struct(
        {
            "sampleRateHertz": t.integer().optional(),
            "bitrateBps": t.integer(),
            "displayName": t.string().optional(),
            "mapping": t.array(t.proxy(renames["AudioMappingIn"])).optional(),
            "codec": t.string().optional(),
            "languageCode": t.string().optional(),
            "channelLayout": t.array(t.string()).optional(),
            "channelCount": t.integer().optional(),
        }
    ).named(renames["AudioStreamIn"])
    types["AudioStreamOut"] = t.struct(
        {
            "sampleRateHertz": t.integer().optional(),
            "bitrateBps": t.integer(),
            "displayName": t.string().optional(),
            "mapping": t.array(t.proxy(renames["AudioMappingOut"])).optional(),
            "codec": t.string().optional(),
            "languageCode": t.string().optional(),
            "channelLayout": t.array(t.string()).optional(),
            "channelCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioStreamOut"])
    types["NormalizedCoordinateIn"] = t.struct(
        {"y": t.number().optional(), "x": t.number().optional()}
    ).named(renames["NormalizedCoordinateIn"])
    types["NormalizedCoordinateOut"] = t.struct(
        {
            "y": t.number().optional(),
            "x": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NormalizedCoordinateOut"])
    types["ListJobTemplatesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobTemplates": t.array(t.proxy(renames["JobTemplateIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListJobTemplatesResponseIn"])
    types["ListJobTemplatesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobTemplates": t.array(t.proxy(renames["JobTemplateOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobTemplatesResponseOut"])
    types["AdBreakIn"] = t.struct({"startTimeOffset": t.string().optional()}).named(
        renames["AdBreakIn"]
    )
    types["AdBreakOut"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdBreakOut"])
    types["OutputIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["OutputIn"]
    )
    types["OutputOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutputOut"])
    types["PadIn"] = t.struct(
        {
            "leftPixels": t.integer().optional(),
            "bottomPixels": t.integer().optional(),
            "topPixels": t.integer().optional(),
            "rightPixels": t.integer().optional(),
        }
    ).named(renames["PadIn"])
    types["PadOut"] = t.struct(
        {
            "leftPixels": t.integer().optional(),
            "bottomPixels": t.integer().optional(),
            "topPixels": t.integer().optional(),
            "rightPixels": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PadOut"])
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
    types["PubsubDestinationIn"] = t.struct({"topic": t.string().optional()}).named(
        renames["PubsubDestinationIn"]
    )
    types["PubsubDestinationOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubDestinationOut"])
    types["AudioIn"] = t.struct(
        {
            "lowBoost": t.boolean().optional(),
            "highBoost": t.boolean().optional(),
            "lufs": t.number().optional(),
        }
    ).named(renames["AudioIn"])
    types["AudioOut"] = t.struct(
        {
            "lowBoost": t.boolean().optional(),
            "highBoost": t.boolean().optional(),
            "lufs": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioOut"])
    types["BwdifConfigIn"] = t.struct(
        {
            "mode": t.string().optional(),
            "parity": t.string().optional(),
            "deinterlaceAllFrames": t.boolean().optional(),
        }
    ).named(renames["BwdifConfigIn"])
    types["BwdifConfigOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "parity": t.string().optional(),
            "deinterlaceAllFrames": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BwdifConfigOut"])
    types["CropIn"] = t.struct(
        {
            "rightPixels": t.integer().optional(),
            "bottomPixels": t.integer().optional(),
            "leftPixels": t.integer().optional(),
            "topPixels": t.integer().optional(),
        }
    ).named(renames["CropIn"])
    types["CropOut"] = t.struct(
        {
            "rightPixels": t.integer().optional(),
            "bottomPixels": t.integer().optional(),
            "leftPixels": t.integer().optional(),
            "topPixels": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["H265CodecSettingsIn"] = t.struct(
        {
            "preset": t.string().optional(),
            "bFrameCount": t.integer().optional(),
            "enableTwoPass": t.boolean().optional(),
            "frameRate": t.number(),
            "crfLevel": t.integer().optional(),
            "gopDuration": t.string().optional(),
            "rateControlMode": t.string().optional(),
            "widthPixels": t.integer().optional(),
            "bPyramid": t.boolean().optional(),
            "vbvFullnessBits": t.integer().optional(),
            "vbvSizeBits": t.integer().optional(),
            "heightPixels": t.integer().optional(),
            "profile": t.string().optional(),
            "allowOpenGop": t.boolean().optional(),
            "pixelFormat": t.string().optional(),
            "gopFrameCount": t.integer().optional(),
            "aqStrength": t.number().optional(),
            "tune": t.string().optional(),
            "bitrateBps": t.integer(),
        }
    ).named(renames["H265CodecSettingsIn"])
    types["H265CodecSettingsOut"] = t.struct(
        {
            "preset": t.string().optional(),
            "bFrameCount": t.integer().optional(),
            "enableTwoPass": t.boolean().optional(),
            "frameRate": t.number(),
            "crfLevel": t.integer().optional(),
            "gopDuration": t.string().optional(),
            "rateControlMode": t.string().optional(),
            "widthPixels": t.integer().optional(),
            "bPyramid": t.boolean().optional(),
            "vbvFullnessBits": t.integer().optional(),
            "vbvSizeBits": t.integer().optional(),
            "heightPixels": t.integer().optional(),
            "profile": t.string().optional(),
            "allowOpenGop": t.boolean().optional(),
            "pixelFormat": t.string().optional(),
            "gopFrameCount": t.integer().optional(),
            "aqStrength": t.number().optional(),
            "tune": t.string().optional(),
            "bitrateBps": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["H265CodecSettingsOut"])
    types["AnimationFadeIn"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "xy": t.proxy(renames["NormalizedCoordinateIn"]).optional(),
            "endTimeOffset": t.string().optional(),
            "fadeType": t.string(),
        }
    ).named(renames["AnimationFadeIn"])
    types["AnimationFadeOut"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "xy": t.proxy(renames["NormalizedCoordinateOut"]).optional(),
            "endTimeOffset": t.string().optional(),
            "fadeType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnimationFadeOut"])
    types["DenoiseIn"] = t.struct(
        {"tune": t.string().optional(), "strength": t.number().optional()}
    ).named(renames["DenoiseIn"])
    types["DenoiseOut"] = t.struct(
        {
            "tune": t.string().optional(),
            "strength": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DenoiseOut"])
    types["Vp9CodecSettingsIn"] = t.struct(
        {
            "frameRate": t.number(),
            "rateControlMode": t.string().optional(),
            "heightPixels": t.integer().optional(),
            "crfLevel": t.integer().optional(),
            "widthPixels": t.integer().optional(),
            "gopFrameCount": t.integer().optional(),
            "bitrateBps": t.integer(),
            "pixelFormat": t.string().optional(),
            "gopDuration": t.string().optional(),
            "profile": t.string().optional(),
        }
    ).named(renames["Vp9CodecSettingsIn"])
    types["Vp9CodecSettingsOut"] = t.struct(
        {
            "frameRate": t.number(),
            "rateControlMode": t.string().optional(),
            "heightPixels": t.integer().optional(),
            "crfLevel": t.integer().optional(),
            "widthPixels": t.integer().optional(),
            "gopFrameCount": t.integer().optional(),
            "bitrateBps": t.integer(),
            "pixelFormat": t.string().optional(),
            "gopDuration": t.string().optional(),
            "profile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Vp9CodecSettingsOut"])

    functions = {}
    functions["projectsLocationsJobsList"] = transcoder.delete(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsCreate"] = transcoder.delete(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGet"] = transcoder.delete(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsDelete"] = transcoder.delete(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobTemplatesDelete"] = transcoder.get(
        "v1/{parent}/jobTemplates",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobTemplatesGet"] = transcoder.get(
        "v1/{parent}/jobTemplates",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="transcoder", renames=renames, types=types, functions=functions
    )
