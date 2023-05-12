from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_transcoder() -> Import:
    transcoder = HTTPRuntime("https://transcoder.googleapis.com/")

    renames = {
        "ErrorResponse": "_transcoder_1_ErrorResponse",
        "DeinterlaceIn": "_transcoder_2_DeinterlaceIn",
        "DeinterlaceOut": "_transcoder_3_DeinterlaceOut",
        "AudioIn": "_transcoder_4_AudioIn",
        "AudioOut": "_transcoder_5_AudioOut",
        "SpriteSheetIn": "_transcoder_6_SpriteSheetIn",
        "SpriteSheetOut": "_transcoder_7_SpriteSheetOut",
        "AudioMappingIn": "_transcoder_8_AudioMappingIn",
        "AudioMappingOut": "_transcoder_9_AudioMappingOut",
        "ImageIn": "_transcoder_10_ImageIn",
        "ImageOut": "_transcoder_11_ImageOut",
        "AdBreakIn": "_transcoder_12_AdBreakIn",
        "AdBreakOut": "_transcoder_13_AdBreakOut",
        "YadifConfigIn": "_transcoder_14_YadifConfigIn",
        "YadifConfigOut": "_transcoder_15_YadifConfigOut",
        "ColorIn": "_transcoder_16_ColorIn",
        "ColorOut": "_transcoder_17_ColorOut",
        "H265CodecSettingsIn": "_transcoder_18_H265CodecSettingsIn",
        "H265CodecSettingsOut": "_transcoder_19_H265CodecSettingsOut",
        "EmptyIn": "_transcoder_20_EmptyIn",
        "EmptyOut": "_transcoder_21_EmptyOut",
        "PadIn": "_transcoder_22_PadIn",
        "PadOut": "_transcoder_23_PadOut",
        "ManifestIn": "_transcoder_24_ManifestIn",
        "ManifestOut": "_transcoder_25_ManifestOut",
        "OutputIn": "_transcoder_26_OutputIn",
        "OutputOut": "_transcoder_27_OutputOut",
        "JobTemplateIn": "_transcoder_28_JobTemplateIn",
        "JobTemplateOut": "_transcoder_29_JobTemplateOut",
        "MuxStreamIn": "_transcoder_30_MuxStreamIn",
        "MuxStreamOut": "_transcoder_31_MuxStreamOut",
        "AudioStreamIn": "_transcoder_32_AudioStreamIn",
        "AudioStreamOut": "_transcoder_33_AudioStreamOut",
        "ElementaryStreamIn": "_transcoder_34_ElementaryStreamIn",
        "ElementaryStreamOut": "_transcoder_35_ElementaryStreamOut",
        "AnimationFadeIn": "_transcoder_36_AnimationFadeIn",
        "AnimationFadeOut": "_transcoder_37_AnimationFadeOut",
        "VideoStreamIn": "_transcoder_38_VideoStreamIn",
        "VideoStreamOut": "_transcoder_39_VideoStreamOut",
        "BwdifConfigIn": "_transcoder_40_BwdifConfigIn",
        "BwdifConfigOut": "_transcoder_41_BwdifConfigOut",
        "OverlayIn": "_transcoder_42_OverlayIn",
        "OverlayOut": "_transcoder_43_OverlayOut",
        "NormalizedCoordinateIn": "_transcoder_44_NormalizedCoordinateIn",
        "NormalizedCoordinateOut": "_transcoder_45_NormalizedCoordinateOut",
        "H264CodecSettingsIn": "_transcoder_46_H264CodecSettingsIn",
        "H264CodecSettingsOut": "_transcoder_47_H264CodecSettingsOut",
        "AnimationStaticIn": "_transcoder_48_AnimationStaticIn",
        "AnimationStaticOut": "_transcoder_49_AnimationStaticOut",
        "StatusIn": "_transcoder_50_StatusIn",
        "StatusOut": "_transcoder_51_StatusOut",
        "EditAtomIn": "_transcoder_52_EditAtomIn",
        "EditAtomOut": "_transcoder_53_EditAtomOut",
        "PubsubDestinationIn": "_transcoder_54_PubsubDestinationIn",
        "PubsubDestinationOut": "_transcoder_55_PubsubDestinationOut",
        "PreprocessingConfigIn": "_transcoder_56_PreprocessingConfigIn",
        "PreprocessingConfigOut": "_transcoder_57_PreprocessingConfigOut",
        "InputIn": "_transcoder_58_InputIn",
        "InputOut": "_transcoder_59_InputOut",
        "ListJobsResponseIn": "_transcoder_60_ListJobsResponseIn",
        "ListJobsResponseOut": "_transcoder_61_ListJobsResponseOut",
        "ListJobTemplatesResponseIn": "_transcoder_62_ListJobTemplatesResponseIn",
        "ListJobTemplatesResponseOut": "_transcoder_63_ListJobTemplatesResponseOut",
        "TextMappingIn": "_transcoder_64_TextMappingIn",
        "TextMappingOut": "_transcoder_65_TextMappingOut",
        "JobConfigIn": "_transcoder_66_JobConfigIn",
        "JobConfigOut": "_transcoder_67_JobConfigOut",
        "AnimationIn": "_transcoder_68_AnimationIn",
        "AnimationOut": "_transcoder_69_AnimationOut",
        "SegmentSettingsIn": "_transcoder_70_SegmentSettingsIn",
        "SegmentSettingsOut": "_transcoder_71_SegmentSettingsOut",
        "CropIn": "_transcoder_72_CropIn",
        "CropOut": "_transcoder_73_CropOut",
        "Vp9CodecSettingsIn": "_transcoder_74_Vp9CodecSettingsIn",
        "Vp9CodecSettingsOut": "_transcoder_75_Vp9CodecSettingsOut",
        "DenoiseIn": "_transcoder_76_DenoiseIn",
        "DenoiseOut": "_transcoder_77_DenoiseOut",
        "TextStreamIn": "_transcoder_78_TextStreamIn",
        "TextStreamOut": "_transcoder_79_TextStreamOut",
        "DeblockIn": "_transcoder_80_DeblockIn",
        "DeblockOut": "_transcoder_81_DeblockOut",
        "AnimationEndIn": "_transcoder_82_AnimationEndIn",
        "AnimationEndOut": "_transcoder_83_AnimationEndOut",
        "JobIn": "_transcoder_84_JobIn",
        "JobOut": "_transcoder_85_JobOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["AudioIn"] = t.struct(
        {
            "lowBoost": t.boolean().optional(),
            "lufs": t.number().optional(),
            "highBoost": t.boolean().optional(),
        }
    ).named(renames["AudioIn"])
    types["AudioOut"] = t.struct(
        {
            "lowBoost": t.boolean().optional(),
            "lufs": t.number().optional(),
            "highBoost": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioOut"])
    types["SpriteSheetIn"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "quality": t.integer().optional(),
            "endTimeOffset": t.string().optional(),
            "spriteHeightPixels": t.integer(),
            "interval": t.string().optional(),
            "totalCount": t.integer().optional(),
            "format": t.string().optional(),
            "columnCount": t.integer().optional(),
            "rowCount": t.integer().optional(),
            "spriteWidthPixels": t.integer(),
            "filePrefix": t.string(),
        }
    ).named(renames["SpriteSheetIn"])
    types["SpriteSheetOut"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "quality": t.integer().optional(),
            "endTimeOffset": t.string().optional(),
            "spriteHeightPixels": t.integer(),
            "interval": t.string().optional(),
            "totalCount": t.integer().optional(),
            "format": t.string().optional(),
            "columnCount": t.integer().optional(),
            "rowCount": t.integer().optional(),
            "spriteWidthPixels": t.integer(),
            "filePrefix": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpriteSheetOut"])
    types["AudioMappingIn"] = t.struct(
        {
            "outputChannel": t.integer(),
            "gainDb": t.number().optional(),
            "inputTrack": t.integer(),
            "atomKey": t.string(),
            "inputChannel": t.integer(),
            "inputKey": t.string(),
        }
    ).named(renames["AudioMappingIn"])
    types["AudioMappingOut"] = t.struct(
        {
            "outputChannel": t.integer(),
            "gainDb": t.number().optional(),
            "inputTrack": t.integer(),
            "atomKey": t.string(),
            "inputChannel": t.integer(),
            "inputKey": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioMappingOut"])
    types["ImageIn"] = t.struct(
        {
            "alpha": t.number().optional(),
            "uri": t.string(),
            "resolution": t.proxy(renames["NormalizedCoordinateIn"]).optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "alpha": t.number().optional(),
            "uri": t.string(),
            "resolution": t.proxy(renames["NormalizedCoordinateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["AdBreakIn"] = t.struct({"startTimeOffset": t.string().optional()}).named(
        renames["AdBreakIn"]
    )
    types["AdBreakOut"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdBreakOut"])
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
    types["ColorIn"] = t.struct(
        {
            "brightness": t.number().optional(),
            "contrast": t.number().optional(),
            "saturation": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "brightness": t.number().optional(),
            "contrast": t.number().optional(),
            "saturation": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["H265CodecSettingsIn"] = t.struct(
        {
            "enableTwoPass": t.boolean().optional(),
            "pixelFormat": t.string().optional(),
            "gopDuration": t.string().optional(),
            "aqStrength": t.number().optional(),
            "rateControlMode": t.string().optional(),
            "vbvFullnessBits": t.integer().optional(),
            "heightPixels": t.integer().optional(),
            "gopFrameCount": t.integer().optional(),
            "widthPixels": t.integer().optional(),
            "vbvSizeBits": t.integer().optional(),
            "bitrateBps": t.integer(),
            "profile": t.string().optional(),
            "bPyramid": t.boolean().optional(),
            "tune": t.string().optional(),
            "bFrameCount": t.integer().optional(),
            "allowOpenGop": t.boolean().optional(),
            "crfLevel": t.integer().optional(),
            "frameRate": t.number(),
            "preset": t.string().optional(),
        }
    ).named(renames["H265CodecSettingsIn"])
    types["H265CodecSettingsOut"] = t.struct(
        {
            "enableTwoPass": t.boolean().optional(),
            "pixelFormat": t.string().optional(),
            "gopDuration": t.string().optional(),
            "aqStrength": t.number().optional(),
            "rateControlMode": t.string().optional(),
            "vbvFullnessBits": t.integer().optional(),
            "heightPixels": t.integer().optional(),
            "gopFrameCount": t.integer().optional(),
            "widthPixels": t.integer().optional(),
            "vbvSizeBits": t.integer().optional(),
            "bitrateBps": t.integer(),
            "profile": t.string().optional(),
            "bPyramid": t.boolean().optional(),
            "tune": t.string().optional(),
            "bFrameCount": t.integer().optional(),
            "allowOpenGop": t.boolean().optional(),
            "crfLevel": t.integer().optional(),
            "frameRate": t.number(),
            "preset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["H265CodecSettingsOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["PadIn"] = t.struct(
        {
            "topPixels": t.integer().optional(),
            "leftPixels": t.integer().optional(),
            "rightPixels": t.integer().optional(),
            "bottomPixels": t.integer().optional(),
        }
    ).named(renames["PadIn"])
    types["PadOut"] = t.struct(
        {
            "topPixels": t.integer().optional(),
            "leftPixels": t.integer().optional(),
            "rightPixels": t.integer().optional(),
            "bottomPixels": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PadOut"])
    types["ManifestIn"] = t.struct(
        {
            "fileName": t.string().optional(),
            "type": t.string(),
            "muxStreams": t.array(t.string()),
        }
    ).named(renames["ManifestIn"])
    types["ManifestOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "type": t.string(),
            "muxStreams": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManifestOut"])
    types["OutputIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["OutputIn"]
    )
    types["OutputOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutputOut"])
    types["JobTemplateIn"] = t.struct(
        {
            "config": t.proxy(renames["JobConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["JobTemplateIn"])
    types["JobTemplateOut"] = t.struct(
        {
            "config": t.proxy(renames["JobConfigOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobTemplateOut"])
    types["MuxStreamIn"] = t.struct(
        {
            "elementaryStreams": t.array(t.string()).optional(),
            "key": t.string().optional(),
            "fileName": t.string().optional(),
            "segmentSettings": t.proxy(renames["SegmentSettingsIn"]).optional(),
            "container": t.string().optional(),
        }
    ).named(renames["MuxStreamIn"])
    types["MuxStreamOut"] = t.struct(
        {
            "elementaryStreams": t.array(t.string()).optional(),
            "key": t.string().optional(),
            "fileName": t.string().optional(),
            "segmentSettings": t.proxy(renames["SegmentSettingsOut"]).optional(),
            "container": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MuxStreamOut"])
    types["AudioStreamIn"] = t.struct(
        {
            "channelLayout": t.array(t.string()).optional(),
            "languageCode": t.string().optional(),
            "channelCount": t.integer().optional(),
            "bitrateBps": t.integer(),
            "displayName": t.string().optional(),
            "codec": t.string().optional(),
            "sampleRateHertz": t.integer().optional(),
            "mapping": t.array(t.proxy(renames["AudioMappingIn"])).optional(),
        }
    ).named(renames["AudioStreamIn"])
    types["AudioStreamOut"] = t.struct(
        {
            "channelLayout": t.array(t.string()).optional(),
            "languageCode": t.string().optional(),
            "channelCount": t.integer().optional(),
            "bitrateBps": t.integer(),
            "displayName": t.string().optional(),
            "codec": t.string().optional(),
            "sampleRateHertz": t.integer().optional(),
            "mapping": t.array(t.proxy(renames["AudioMappingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioStreamOut"])
    types["ElementaryStreamIn"] = t.struct(
        {
            "videoStream": t.proxy(renames["VideoStreamIn"]).optional(),
            "textStream": t.proxy(renames["TextStreamIn"]).optional(),
            "audioStream": t.proxy(renames["AudioStreamIn"]).optional(),
            "key": t.string().optional(),
        }
    ).named(renames["ElementaryStreamIn"])
    types["ElementaryStreamOut"] = t.struct(
        {
            "videoStream": t.proxy(renames["VideoStreamOut"]).optional(),
            "textStream": t.proxy(renames["TextStreamOut"]).optional(),
            "audioStream": t.proxy(renames["AudioStreamOut"]).optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ElementaryStreamOut"])
    types["AnimationFadeIn"] = t.struct(
        {
            "fadeType": t.string(),
            "xy": t.proxy(renames["NormalizedCoordinateIn"]).optional(),
            "endTimeOffset": t.string().optional(),
            "startTimeOffset": t.string().optional(),
        }
    ).named(renames["AnimationFadeIn"])
    types["AnimationFadeOut"] = t.struct(
        {
            "fadeType": t.string(),
            "xy": t.proxy(renames["NormalizedCoordinateOut"]).optional(),
            "endTimeOffset": t.string().optional(),
            "startTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnimationFadeOut"])
    types["VideoStreamIn"] = t.struct(
        {
            "vp9": t.proxy(renames["Vp9CodecSettingsIn"]).optional(),
            "h265": t.proxy(renames["H265CodecSettingsIn"]).optional(),
            "h264": t.proxy(renames["H264CodecSettingsIn"]).optional(),
        }
    ).named(renames["VideoStreamIn"])
    types["VideoStreamOut"] = t.struct(
        {
            "vp9": t.proxy(renames["Vp9CodecSettingsOut"]).optional(),
            "h265": t.proxy(renames["H265CodecSettingsOut"]).optional(),
            "h264": t.proxy(renames["H264CodecSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoStreamOut"])
    types["BwdifConfigIn"] = t.struct(
        {
            "deinterlaceAllFrames": t.boolean().optional(),
            "parity": t.string().optional(),
            "mode": t.string().optional(),
        }
    ).named(renames["BwdifConfigIn"])
    types["BwdifConfigOut"] = t.struct(
        {
            "deinterlaceAllFrames": t.boolean().optional(),
            "parity": t.string().optional(),
            "mode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BwdifConfigOut"])
    types["OverlayIn"] = t.struct(
        {
            "animations": t.array(t.proxy(renames["AnimationIn"])).optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
        }
    ).named(renames["OverlayIn"])
    types["OverlayOut"] = t.struct(
        {
            "animations": t.array(t.proxy(renames["AnimationOut"])).optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OverlayOut"])
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
    types["H264CodecSettingsIn"] = t.struct(
        {
            "gopFrameCount": t.integer().optional(),
            "bitrateBps": t.integer(),
            "crfLevel": t.integer().optional(),
            "profile": t.string().optional(),
            "preset": t.string().optional(),
            "bPyramid": t.boolean().optional(),
            "allowOpenGop": t.boolean().optional(),
            "widthPixels": t.integer().optional(),
            "bFrameCount": t.integer().optional(),
            "heightPixels": t.integer().optional(),
            "vbvSizeBits": t.integer().optional(),
            "entropyCoder": t.string().optional(),
            "tune": t.string().optional(),
            "vbvFullnessBits": t.integer().optional(),
            "pixelFormat": t.string().optional(),
            "gopDuration": t.string().optional(),
            "frameRate": t.number(),
            "enableTwoPass": t.boolean().optional(),
            "rateControlMode": t.string().optional(),
            "aqStrength": t.number().optional(),
        }
    ).named(renames["H264CodecSettingsIn"])
    types["H264CodecSettingsOut"] = t.struct(
        {
            "gopFrameCount": t.integer().optional(),
            "bitrateBps": t.integer(),
            "crfLevel": t.integer().optional(),
            "profile": t.string().optional(),
            "preset": t.string().optional(),
            "bPyramid": t.boolean().optional(),
            "allowOpenGop": t.boolean().optional(),
            "widthPixels": t.integer().optional(),
            "bFrameCount": t.integer().optional(),
            "heightPixels": t.integer().optional(),
            "vbvSizeBits": t.integer().optional(),
            "entropyCoder": t.string().optional(),
            "tune": t.string().optional(),
            "vbvFullnessBits": t.integer().optional(),
            "pixelFormat": t.string().optional(),
            "gopDuration": t.string().optional(),
            "frameRate": t.number(),
            "enableTwoPass": t.boolean().optional(),
            "rateControlMode": t.string().optional(),
            "aqStrength": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["H264CodecSettingsOut"])
    types["AnimationStaticIn"] = t.struct(
        {
            "xy": t.proxy(renames["NormalizedCoordinateIn"]).optional(),
            "startTimeOffset": t.string().optional(),
        }
    ).named(renames["AnimationStaticIn"])
    types["AnimationStaticOut"] = t.struct(
        {
            "xy": t.proxy(renames["NormalizedCoordinateOut"]).optional(),
            "startTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnimationStaticOut"])
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
    types["EditAtomIn"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "key": t.string().optional(),
            "endTimeOffset": t.string().optional(),
            "inputs": t.array(t.string()).optional(),
        }
    ).named(renames["EditAtomIn"])
    types["EditAtomOut"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "key": t.string().optional(),
            "endTimeOffset": t.string().optional(),
            "inputs": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditAtomOut"])
    types["PubsubDestinationIn"] = t.struct({"topic": t.string().optional()}).named(
        renames["PubsubDestinationIn"]
    )
    types["PubsubDestinationOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubDestinationOut"])
    types["PreprocessingConfigIn"] = t.struct(
        {
            "crop": t.proxy(renames["CropIn"]).optional(),
            "deinterlace": t.proxy(renames["DeinterlaceIn"]).optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "audio": t.proxy(renames["AudioIn"]).optional(),
            "deblock": t.proxy(renames["DeblockIn"]).optional(),
            "pad": t.proxy(renames["PadIn"]).optional(),
            "denoise": t.proxy(renames["DenoiseIn"]).optional(),
        }
    ).named(renames["PreprocessingConfigIn"])
    types["PreprocessingConfigOut"] = t.struct(
        {
            "crop": t.proxy(renames["CropOut"]).optional(),
            "deinterlace": t.proxy(renames["DeinterlaceOut"]).optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "audio": t.proxy(renames["AudioOut"]).optional(),
            "deblock": t.proxy(renames["DeblockOut"]).optional(),
            "pad": t.proxy(renames["PadOut"]).optional(),
            "denoise": t.proxy(renames["DenoiseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PreprocessingConfigOut"])
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
    types["ListJobsResponseIn"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["JobIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListJobsResponseIn"])
    types["ListJobsResponseOut"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobsResponseOut"])
    types["ListJobTemplatesResponseIn"] = t.struct(
        {
            "jobTemplates": t.array(t.proxy(renames["JobTemplateIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListJobTemplatesResponseIn"])
    types["ListJobTemplatesResponseOut"] = t.struct(
        {
            "jobTemplates": t.array(t.proxy(renames["JobTemplateOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobTemplatesResponseOut"])
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
    types["JobConfigIn"] = t.struct(
        {
            "pubsubDestination": t.proxy(renames["PubsubDestinationIn"]).optional(),
            "overlays": t.array(t.proxy(renames["OverlayIn"])).optional(),
            "output": t.proxy(renames["OutputIn"]).optional(),
            "spriteSheets": t.array(t.proxy(renames["SpriteSheetIn"])).optional(),
            "inputs": t.array(t.proxy(renames["InputIn"])).optional(),
            "elementaryStreams": t.array(
                t.proxy(renames["ElementaryStreamIn"])
            ).optional(),
            "manifests": t.array(t.proxy(renames["ManifestIn"])).optional(),
            "adBreaks": t.array(t.proxy(renames["AdBreakIn"])).optional(),
            "muxStreams": t.array(t.proxy(renames["MuxStreamIn"])).optional(),
            "editList": t.array(t.proxy(renames["EditAtomIn"])).optional(),
        }
    ).named(renames["JobConfigIn"])
    types["JobConfigOut"] = t.struct(
        {
            "pubsubDestination": t.proxy(renames["PubsubDestinationOut"]).optional(),
            "overlays": t.array(t.proxy(renames["OverlayOut"])).optional(),
            "output": t.proxy(renames["OutputOut"]).optional(),
            "spriteSheets": t.array(t.proxy(renames["SpriteSheetOut"])).optional(),
            "inputs": t.array(t.proxy(renames["InputOut"])).optional(),
            "elementaryStreams": t.array(
                t.proxy(renames["ElementaryStreamOut"])
            ).optional(),
            "manifests": t.array(t.proxy(renames["ManifestOut"])).optional(),
            "adBreaks": t.array(t.proxy(renames["AdBreakOut"])).optional(),
            "muxStreams": t.array(t.proxy(renames["MuxStreamOut"])).optional(),
            "editList": t.array(t.proxy(renames["EditAtomOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobConfigOut"])
    types["AnimationIn"] = t.struct(
        {
            "animationFade": t.proxy(renames["AnimationFadeIn"]).optional(),
            "animationStatic": t.proxy(renames["AnimationStaticIn"]).optional(),
            "animationEnd": t.proxy(renames["AnimationEndIn"]).optional(),
        }
    ).named(renames["AnimationIn"])
    types["AnimationOut"] = t.struct(
        {
            "animationFade": t.proxy(renames["AnimationFadeOut"]).optional(),
            "animationStatic": t.proxy(renames["AnimationStaticOut"]).optional(),
            "animationEnd": t.proxy(renames["AnimationEndOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnimationOut"])
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
    types["Vp9CodecSettingsIn"] = t.struct(
        {
            "crfLevel": t.integer().optional(),
            "bitrateBps": t.integer(),
            "profile": t.string().optional(),
            "gopFrameCount": t.integer().optional(),
            "widthPixels": t.integer().optional(),
            "rateControlMode": t.string().optional(),
            "heightPixels": t.integer().optional(),
            "frameRate": t.number(),
            "pixelFormat": t.string().optional(),
            "gopDuration": t.string().optional(),
        }
    ).named(renames["Vp9CodecSettingsIn"])
    types["Vp9CodecSettingsOut"] = t.struct(
        {
            "crfLevel": t.integer().optional(),
            "bitrateBps": t.integer(),
            "profile": t.string().optional(),
            "gopFrameCount": t.integer().optional(),
            "widthPixels": t.integer().optional(),
            "rateControlMode": t.string().optional(),
            "heightPixels": t.integer().optional(),
            "frameRate": t.number(),
            "pixelFormat": t.string().optional(),
            "gopDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Vp9CodecSettingsOut"])
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
    types["TextStreamIn"] = t.struct(
        {
            "codec": t.string().optional(),
            "mapping": t.array(t.proxy(renames["TextMappingIn"])).optional(),
            "displayName": t.string().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["TextStreamIn"])
    types["TextStreamOut"] = t.struct(
        {
            "codec": t.string().optional(),
            "mapping": t.array(t.proxy(renames["TextMappingOut"])).optional(),
            "displayName": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextStreamOut"])
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
    types["AnimationEndIn"] = t.struct(
        {"startTimeOffset": t.string().optional()}
    ).named(renames["AnimationEndIn"])
    types["AnimationEndOut"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnimationEndOut"])
    types["JobIn"] = t.struct(
        {
            "ttlAfterCompletionDays": t.integer().optional(),
            "config": t.proxy(renames["JobConfigIn"]).optional(),
            "inputUri": t.string().optional(),
            "mode": t.string().optional(),
            "templateId": t.string().optional(),
            "outputUri": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "ttlAfterCompletionDays": t.integer().optional(),
            "config": t.proxy(renames["JobConfigOut"]).optional(),
            "inputUri": t.string().optional(),
            "mode": t.string().optional(),
            "templateId": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "outputUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["JobOut"])

    functions = {}
    functions["projectsLocationsJobsList"] = transcoder.post(
        "v1/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "ttlAfterCompletionDays": t.integer().optional(),
                "config": t.proxy(renames["JobConfigIn"]).optional(),
                "inputUri": t.string().optional(),
                "mode": t.string().optional(),
                "templateId": t.string().optional(),
                "outputUri": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsDelete"] = transcoder.post(
        "v1/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "ttlAfterCompletionDays": t.integer().optional(),
                "config": t.proxy(renames["JobConfigIn"]).optional(),
                "inputUri": t.string().optional(),
                "mode": t.string().optional(),
                "templateId": t.string().optional(),
                "outputUri": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGet"] = transcoder.post(
        "v1/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "ttlAfterCompletionDays": t.integer().optional(),
                "config": t.proxy(renames["JobConfigIn"]).optional(),
                "inputUri": t.string().optional(),
                "mode": t.string().optional(),
                "templateId": t.string().optional(),
                "outputUri": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsCreate"] = transcoder.post(
        "v1/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "ttlAfterCompletionDays": t.integer().optional(),
                "config": t.proxy(renames["JobConfigIn"]).optional(),
                "inputUri": t.string().optional(),
                "mode": t.string().optional(),
                "templateId": t.string().optional(),
                "outputUri": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobTemplatesList"] = transcoder.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobTemplatesCreate"] = transcoder.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobTemplatesGet"] = transcoder.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobTemplatesDelete"] = transcoder.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="transcoder",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
