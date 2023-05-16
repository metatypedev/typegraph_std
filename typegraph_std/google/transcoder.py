from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_transcoder() -> Import:
    transcoder = HTTPRuntime("https://transcoder.googleapis.com/")

    renames = {
        "ErrorResponse": "_transcoder_1_ErrorResponse",
        "InputIn": "_transcoder_2_InputIn",
        "InputOut": "_transcoder_3_InputOut",
        "OutputIn": "_transcoder_4_OutputIn",
        "OutputOut": "_transcoder_5_OutputOut",
        "SpriteSheetIn": "_transcoder_6_SpriteSheetIn",
        "SpriteSheetOut": "_transcoder_7_SpriteSheetOut",
        "OverlayIn": "_transcoder_8_OverlayIn",
        "OverlayOut": "_transcoder_9_OverlayOut",
        "AnimationStaticIn": "_transcoder_10_AnimationStaticIn",
        "AnimationStaticOut": "_transcoder_11_AnimationStaticOut",
        "ListJobTemplatesResponseIn": "_transcoder_12_ListJobTemplatesResponseIn",
        "ListJobTemplatesResponseOut": "_transcoder_13_ListJobTemplatesResponseOut",
        "JobIn": "_transcoder_14_JobIn",
        "JobOut": "_transcoder_15_JobOut",
        "ManifestIn": "_transcoder_16_ManifestIn",
        "ManifestOut": "_transcoder_17_ManifestOut",
        "H264CodecSettingsIn": "_transcoder_18_H264CodecSettingsIn",
        "H264CodecSettingsOut": "_transcoder_19_H264CodecSettingsOut",
        "DeblockIn": "_transcoder_20_DeblockIn",
        "DeblockOut": "_transcoder_21_DeblockOut",
        "TextStreamIn": "_transcoder_22_TextStreamIn",
        "TextStreamOut": "_transcoder_23_TextStreamOut",
        "BwdifConfigIn": "_transcoder_24_BwdifConfigIn",
        "BwdifConfigOut": "_transcoder_25_BwdifConfigOut",
        "EditAtomIn": "_transcoder_26_EditAtomIn",
        "EditAtomOut": "_transcoder_27_EditAtomOut",
        "TextMappingIn": "_transcoder_28_TextMappingIn",
        "TextMappingOut": "_transcoder_29_TextMappingOut",
        "JobTemplateIn": "_transcoder_30_JobTemplateIn",
        "JobTemplateOut": "_transcoder_31_JobTemplateOut",
        "AudioMappingIn": "_transcoder_32_AudioMappingIn",
        "AudioMappingOut": "_transcoder_33_AudioMappingOut",
        "AudioIn": "_transcoder_34_AudioIn",
        "AudioOut": "_transcoder_35_AudioOut",
        "MuxStreamIn": "_transcoder_36_MuxStreamIn",
        "MuxStreamOut": "_transcoder_37_MuxStreamOut",
        "SegmentSettingsIn": "_transcoder_38_SegmentSettingsIn",
        "SegmentSettingsOut": "_transcoder_39_SegmentSettingsOut",
        "ColorIn": "_transcoder_40_ColorIn",
        "ColorOut": "_transcoder_41_ColorOut",
        "DeinterlaceIn": "_transcoder_42_DeinterlaceIn",
        "DeinterlaceOut": "_transcoder_43_DeinterlaceOut",
        "PubsubDestinationIn": "_transcoder_44_PubsubDestinationIn",
        "PubsubDestinationOut": "_transcoder_45_PubsubDestinationOut",
        "AudioStreamIn": "_transcoder_46_AudioStreamIn",
        "AudioStreamOut": "_transcoder_47_AudioStreamOut",
        "JobConfigIn": "_transcoder_48_JobConfigIn",
        "JobConfigOut": "_transcoder_49_JobConfigOut",
        "H265CodecSettingsIn": "_transcoder_50_H265CodecSettingsIn",
        "H265CodecSettingsOut": "_transcoder_51_H265CodecSettingsOut",
        "CropIn": "_transcoder_52_CropIn",
        "CropOut": "_transcoder_53_CropOut",
        "VideoStreamIn": "_transcoder_54_VideoStreamIn",
        "VideoStreamOut": "_transcoder_55_VideoStreamOut",
        "AnimationIn": "_transcoder_56_AnimationIn",
        "AnimationOut": "_transcoder_57_AnimationOut",
        "EmptyIn": "_transcoder_58_EmptyIn",
        "EmptyOut": "_transcoder_59_EmptyOut",
        "StatusIn": "_transcoder_60_StatusIn",
        "StatusOut": "_transcoder_61_StatusOut",
        "PadIn": "_transcoder_62_PadIn",
        "PadOut": "_transcoder_63_PadOut",
        "ListJobsResponseIn": "_transcoder_64_ListJobsResponseIn",
        "ListJobsResponseOut": "_transcoder_65_ListJobsResponseOut",
        "YadifConfigIn": "_transcoder_66_YadifConfigIn",
        "YadifConfigOut": "_transcoder_67_YadifConfigOut",
        "ImageIn": "_transcoder_68_ImageIn",
        "ImageOut": "_transcoder_69_ImageOut",
        "AnimationEndIn": "_transcoder_70_AnimationEndIn",
        "AnimationEndOut": "_transcoder_71_AnimationEndOut",
        "AnimationFadeIn": "_transcoder_72_AnimationFadeIn",
        "AnimationFadeOut": "_transcoder_73_AnimationFadeOut",
        "Vp9CodecSettingsIn": "_transcoder_74_Vp9CodecSettingsIn",
        "Vp9CodecSettingsOut": "_transcoder_75_Vp9CodecSettingsOut",
        "PreprocessingConfigIn": "_transcoder_76_PreprocessingConfigIn",
        "PreprocessingConfigOut": "_transcoder_77_PreprocessingConfigOut",
        "AdBreakIn": "_transcoder_78_AdBreakIn",
        "AdBreakOut": "_transcoder_79_AdBreakOut",
        "DenoiseIn": "_transcoder_80_DenoiseIn",
        "DenoiseOut": "_transcoder_81_DenoiseOut",
        "ElementaryStreamIn": "_transcoder_82_ElementaryStreamIn",
        "ElementaryStreamOut": "_transcoder_83_ElementaryStreamOut",
        "NormalizedCoordinateIn": "_transcoder_84_NormalizedCoordinateIn",
        "NormalizedCoordinateOut": "_transcoder_85_NormalizedCoordinateOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["InputIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "preprocessingConfig": t.proxy(renames["PreprocessingConfigIn"]).optional(),
            "key": t.string().optional(),
        }
    ).named(renames["InputIn"])
    types["InputOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "preprocessingConfig": t.proxy(
                renames["PreprocessingConfigOut"]
            ).optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputOut"])
    types["OutputIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["OutputIn"]
    )
    types["OutputOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutputOut"])
    types["SpriteSheetIn"] = t.struct(
        {
            "columnCount": t.integer().optional(),
            "format": t.string().optional(),
            "rowCount": t.integer().optional(),
            "interval": t.string().optional(),
            "spriteWidthPixels": t.integer(),
            "quality": t.integer().optional(),
            "startTimeOffset": t.string().optional(),
            "filePrefix": t.string(),
            "endTimeOffset": t.string().optional(),
            "spriteHeightPixels": t.integer(),
            "totalCount": t.integer().optional(),
        }
    ).named(renames["SpriteSheetIn"])
    types["SpriteSheetOut"] = t.struct(
        {
            "columnCount": t.integer().optional(),
            "format": t.string().optional(),
            "rowCount": t.integer().optional(),
            "interval": t.string().optional(),
            "spriteWidthPixels": t.integer(),
            "quality": t.integer().optional(),
            "startTimeOffset": t.string().optional(),
            "filePrefix": t.string(),
            "endTimeOffset": t.string().optional(),
            "spriteHeightPixels": t.integer(),
            "totalCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpriteSheetOut"])
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
    types["ListJobTemplatesResponseIn"] = t.struct(
        {
            "jobTemplates": t.array(t.proxy(renames["JobTemplateIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListJobTemplatesResponseIn"])
    types["ListJobTemplatesResponseOut"] = t.struct(
        {
            "jobTemplates": t.array(t.proxy(renames["JobTemplateOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobTemplatesResponseOut"])
    types["JobIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "ttlAfterCompletionDays": t.integer().optional(),
            "inputUri": t.string().optional(),
            "name": t.string().optional(),
            "mode": t.string().optional(),
            "config": t.proxy(renames["JobConfigIn"]).optional(),
            "outputUri": t.string().optional(),
            "templateId": t.string().optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "ttlAfterCompletionDays": t.integer().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "inputUri": t.string().optional(),
            "name": t.string().optional(),
            "startTime": t.string().optional(),
            "createTime": t.string().optional(),
            "mode": t.string().optional(),
            "config": t.proxy(renames["JobConfigOut"]).optional(),
            "outputUri": t.string().optional(),
            "templateId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
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
    types["H264CodecSettingsIn"] = t.struct(
        {
            "preset": t.string().optional(),
            "bitrateBps": t.integer(),
            "allowOpenGop": t.boolean().optional(),
            "aqStrength": t.number().optional(),
            "widthPixels": t.integer().optional(),
            "vbvFullnessBits": t.integer().optional(),
            "entropyCoder": t.string().optional(),
            "rateControlMode": t.string().optional(),
            "frameRate": t.number(),
            "vbvSizeBits": t.integer().optional(),
            "pixelFormat": t.string().optional(),
            "enableTwoPass": t.boolean().optional(),
            "gopDuration": t.string().optional(),
            "bPyramid": t.boolean().optional(),
            "tune": t.string().optional(),
            "crfLevel": t.integer().optional(),
            "heightPixels": t.integer().optional(),
            "profile": t.string().optional(),
            "bFrameCount": t.integer().optional(),
            "gopFrameCount": t.integer().optional(),
        }
    ).named(renames["H264CodecSettingsIn"])
    types["H264CodecSettingsOut"] = t.struct(
        {
            "preset": t.string().optional(),
            "bitrateBps": t.integer(),
            "allowOpenGop": t.boolean().optional(),
            "aqStrength": t.number().optional(),
            "widthPixels": t.integer().optional(),
            "vbvFullnessBits": t.integer().optional(),
            "entropyCoder": t.string().optional(),
            "rateControlMode": t.string().optional(),
            "frameRate": t.number(),
            "vbvSizeBits": t.integer().optional(),
            "pixelFormat": t.string().optional(),
            "enableTwoPass": t.boolean().optional(),
            "gopDuration": t.string().optional(),
            "bPyramid": t.boolean().optional(),
            "tune": t.string().optional(),
            "crfLevel": t.integer().optional(),
            "heightPixels": t.integer().optional(),
            "profile": t.string().optional(),
            "bFrameCount": t.integer().optional(),
            "gopFrameCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["H264CodecSettingsOut"])
    types["DeblockIn"] = t.struct(
        {"strength": t.number().optional(), "enabled": t.boolean().optional()}
    ).named(renames["DeblockIn"])
    types["DeblockOut"] = t.struct(
        {
            "strength": t.number().optional(),
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeblockOut"])
    types["TextStreamIn"] = t.struct(
        {
            "mapping": t.array(t.proxy(renames["TextMappingIn"])).optional(),
            "languageCode": t.string().optional(),
            "codec": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["TextStreamIn"])
    types["TextStreamOut"] = t.struct(
        {
            "mapping": t.array(t.proxy(renames["TextMappingOut"])).optional(),
            "languageCode": t.string().optional(),
            "codec": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextStreamOut"])
    types["BwdifConfigIn"] = t.struct(
        {
            "parity": t.string().optional(),
            "mode": t.string().optional(),
            "deinterlaceAllFrames": t.boolean().optional(),
        }
    ).named(renames["BwdifConfigIn"])
    types["BwdifConfigOut"] = t.struct(
        {
            "parity": t.string().optional(),
            "mode": t.string().optional(),
            "deinterlaceAllFrames": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BwdifConfigOut"])
    types["EditAtomIn"] = t.struct(
        {
            "endTimeOffset": t.string().optional(),
            "startTimeOffset": t.string().optional(),
            "key": t.string().optional(),
            "inputs": t.array(t.string()).optional(),
        }
    ).named(renames["EditAtomIn"])
    types["EditAtomOut"] = t.struct(
        {
            "endTimeOffset": t.string().optional(),
            "startTimeOffset": t.string().optional(),
            "key": t.string().optional(),
            "inputs": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EditAtomOut"])
    types["TextMappingIn"] = t.struct(
        {"atomKey": t.string(), "inputKey": t.string(), "inputTrack": t.integer()}
    ).named(renames["TextMappingIn"])
    types["TextMappingOut"] = t.struct(
        {
            "atomKey": t.string(),
            "inputKey": t.string(),
            "inputTrack": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextMappingOut"])
    types["JobTemplateIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "config": t.proxy(renames["JobConfigIn"]).optional(),
        }
    ).named(renames["JobTemplateIn"])
    types["JobTemplateOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "config": t.proxy(renames["JobConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobTemplateOut"])
    types["AudioMappingIn"] = t.struct(
        {
            "atomKey": t.string(),
            "inputKey": t.string(),
            "inputChannel": t.integer(),
            "inputTrack": t.integer(),
            "gainDb": t.number().optional(),
            "outputChannel": t.integer(),
        }
    ).named(renames["AudioMappingIn"])
    types["AudioMappingOut"] = t.struct(
        {
            "atomKey": t.string(),
            "inputKey": t.string(),
            "inputChannel": t.integer(),
            "inputTrack": t.integer(),
            "gainDb": t.number().optional(),
            "outputChannel": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioMappingOut"])
    types["AudioIn"] = t.struct(
        {
            "highBoost": t.boolean().optional(),
            "lufs": t.number().optional(),
            "lowBoost": t.boolean().optional(),
        }
    ).named(renames["AudioIn"])
    types["AudioOut"] = t.struct(
        {
            "highBoost": t.boolean().optional(),
            "lufs": t.number().optional(),
            "lowBoost": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioOut"])
    types["MuxStreamIn"] = t.struct(
        {
            "segmentSettings": t.proxy(renames["SegmentSettingsIn"]).optional(),
            "fileName": t.string().optional(),
            "elementaryStreams": t.array(t.string()).optional(),
            "container": t.string().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["MuxStreamIn"])
    types["MuxStreamOut"] = t.struct(
        {
            "segmentSettings": t.proxy(renames["SegmentSettingsOut"]).optional(),
            "fileName": t.string().optional(),
            "elementaryStreams": t.array(t.string()).optional(),
            "container": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MuxStreamOut"])
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
            "bitrateBps": t.integer(),
            "mapping": t.array(t.proxy(renames["AudioMappingIn"])).optional(),
            "languageCode": t.string().optional(),
            "sampleRateHertz": t.integer().optional(),
            "channelLayout": t.array(t.string()).optional(),
            "channelCount": t.integer().optional(),
            "displayName": t.string().optional(),
            "codec": t.string().optional(),
        }
    ).named(renames["AudioStreamIn"])
    types["AudioStreamOut"] = t.struct(
        {
            "bitrateBps": t.integer(),
            "mapping": t.array(t.proxy(renames["AudioMappingOut"])).optional(),
            "languageCode": t.string().optional(),
            "sampleRateHertz": t.integer().optional(),
            "channelLayout": t.array(t.string()).optional(),
            "channelCount": t.integer().optional(),
            "displayName": t.string().optional(),
            "codec": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AudioStreamOut"])
    types["JobConfigIn"] = t.struct(
        {
            "editList": t.array(t.proxy(renames["EditAtomIn"])).optional(),
            "pubsubDestination": t.proxy(renames["PubsubDestinationIn"]).optional(),
            "muxStreams": t.array(t.proxy(renames["MuxStreamIn"])).optional(),
            "inputs": t.array(t.proxy(renames["InputIn"])).optional(),
            "output": t.proxy(renames["OutputIn"]).optional(),
            "adBreaks": t.array(t.proxy(renames["AdBreakIn"])).optional(),
            "overlays": t.array(t.proxy(renames["OverlayIn"])).optional(),
            "manifests": t.array(t.proxy(renames["ManifestIn"])).optional(),
            "elementaryStreams": t.array(
                t.proxy(renames["ElementaryStreamIn"])
            ).optional(),
            "spriteSheets": t.array(t.proxy(renames["SpriteSheetIn"])).optional(),
        }
    ).named(renames["JobConfigIn"])
    types["JobConfigOut"] = t.struct(
        {
            "editList": t.array(t.proxy(renames["EditAtomOut"])).optional(),
            "pubsubDestination": t.proxy(renames["PubsubDestinationOut"]).optional(),
            "muxStreams": t.array(t.proxy(renames["MuxStreamOut"])).optional(),
            "inputs": t.array(t.proxy(renames["InputOut"])).optional(),
            "output": t.proxy(renames["OutputOut"]).optional(),
            "adBreaks": t.array(t.proxy(renames["AdBreakOut"])).optional(),
            "overlays": t.array(t.proxy(renames["OverlayOut"])).optional(),
            "manifests": t.array(t.proxy(renames["ManifestOut"])).optional(),
            "elementaryStreams": t.array(
                t.proxy(renames["ElementaryStreamOut"])
            ).optional(),
            "spriteSheets": t.array(t.proxy(renames["SpriteSheetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobConfigOut"])
    types["H265CodecSettingsIn"] = t.struct(
        {
            "vbvFullnessBits": t.integer().optional(),
            "enableTwoPass": t.boolean().optional(),
            "crfLevel": t.integer().optional(),
            "gopDuration": t.string().optional(),
            "preset": t.string().optional(),
            "tune": t.string().optional(),
            "bFrameCount": t.integer().optional(),
            "pixelFormat": t.string().optional(),
            "allowOpenGop": t.boolean().optional(),
            "frameRate": t.number(),
            "rateControlMode": t.string().optional(),
            "aqStrength": t.number().optional(),
            "bPyramid": t.boolean().optional(),
            "bitrateBps": t.integer(),
            "vbvSizeBits": t.integer().optional(),
            "heightPixels": t.integer().optional(),
            "widthPixels": t.integer().optional(),
            "gopFrameCount": t.integer().optional(),
            "profile": t.string().optional(),
        }
    ).named(renames["H265CodecSettingsIn"])
    types["H265CodecSettingsOut"] = t.struct(
        {
            "vbvFullnessBits": t.integer().optional(),
            "enableTwoPass": t.boolean().optional(),
            "crfLevel": t.integer().optional(),
            "gopDuration": t.string().optional(),
            "preset": t.string().optional(),
            "tune": t.string().optional(),
            "bFrameCount": t.integer().optional(),
            "pixelFormat": t.string().optional(),
            "allowOpenGop": t.boolean().optional(),
            "frameRate": t.number(),
            "rateControlMode": t.string().optional(),
            "aqStrength": t.number().optional(),
            "bPyramid": t.boolean().optional(),
            "bitrateBps": t.integer(),
            "vbvSizeBits": t.integer().optional(),
            "heightPixels": t.integer().optional(),
            "widthPixels": t.integer().optional(),
            "gopFrameCount": t.integer().optional(),
            "profile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["H265CodecSettingsOut"])
    types["CropIn"] = t.struct(
        {
            "rightPixels": t.integer().optional(),
            "leftPixels": t.integer().optional(),
            "bottomPixels": t.integer().optional(),
            "topPixels": t.integer().optional(),
        }
    ).named(renames["CropIn"])
    types["CropOut"] = t.struct(
        {
            "rightPixels": t.integer().optional(),
            "leftPixels": t.integer().optional(),
            "bottomPixels": t.integer().optional(),
            "topPixels": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CropOut"])
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
    types["AnimationIn"] = t.struct(
        {
            "animationEnd": t.proxy(renames["AnimationEndIn"]).optional(),
            "animationFade": t.proxy(renames["AnimationFadeIn"]).optional(),
            "animationStatic": t.proxy(renames["AnimationStaticIn"]).optional(),
        }
    ).named(renames["AnimationIn"])
    types["AnimationOut"] = t.struct(
        {
            "animationEnd": t.proxy(renames["AnimationEndOut"]).optional(),
            "animationFade": t.proxy(renames["AnimationFadeOut"]).optional(),
            "animationStatic": t.proxy(renames["AnimationStaticOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnimationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["PadIn"] = t.struct(
        {
            "leftPixels": t.integer().optional(),
            "rightPixels": t.integer().optional(),
            "topPixels": t.integer().optional(),
            "bottomPixels": t.integer().optional(),
        }
    ).named(renames["PadIn"])
    types["PadOut"] = t.struct(
        {
            "leftPixels": t.integer().optional(),
            "rightPixels": t.integer().optional(),
            "topPixels": t.integer().optional(),
            "bottomPixels": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PadOut"])
    types["ListJobsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "jobs": t.array(t.proxy(renames["JobIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListJobsResponseIn"])
    types["ListJobsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "jobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobsResponseOut"])
    types["YadifConfigIn"] = t.struct(
        {
            "parity": t.string().optional(),
            "disableSpatialInterlacing": t.boolean().optional(),
            "deinterlaceAllFrames": t.boolean().optional(),
            "mode": t.string().optional(),
        }
    ).named(renames["YadifConfigIn"])
    types["YadifConfigOut"] = t.struct(
        {
            "parity": t.string().optional(),
            "disableSpatialInterlacing": t.boolean().optional(),
            "deinterlaceAllFrames": t.boolean().optional(),
            "mode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YadifConfigOut"])
    types["ImageIn"] = t.struct(
        {
            "resolution": t.proxy(renames["NormalizedCoordinateIn"]).optional(),
            "uri": t.string(),
            "alpha": t.number().optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "resolution": t.proxy(renames["NormalizedCoordinateOut"]).optional(),
            "uri": t.string(),
            "alpha": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["AnimationEndIn"] = t.struct(
        {"startTimeOffset": t.string().optional()}
    ).named(renames["AnimationEndIn"])
    types["AnimationEndOut"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnimationEndOut"])
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
    types["Vp9CodecSettingsIn"] = t.struct(
        {
            "pixelFormat": t.string().optional(),
            "frameRate": t.number(),
            "crfLevel": t.integer().optional(),
            "heightPixels": t.integer().optional(),
            "rateControlMode": t.string().optional(),
            "widthPixels": t.integer().optional(),
            "gopFrameCount": t.integer().optional(),
            "bitrateBps": t.integer(),
            "profile": t.string().optional(),
            "gopDuration": t.string().optional(),
        }
    ).named(renames["Vp9CodecSettingsIn"])
    types["Vp9CodecSettingsOut"] = t.struct(
        {
            "pixelFormat": t.string().optional(),
            "frameRate": t.number(),
            "crfLevel": t.integer().optional(),
            "heightPixels": t.integer().optional(),
            "rateControlMode": t.string().optional(),
            "widthPixels": t.integer().optional(),
            "gopFrameCount": t.integer().optional(),
            "bitrateBps": t.integer(),
            "profile": t.string().optional(),
            "gopDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Vp9CodecSettingsOut"])
    types["PreprocessingConfigIn"] = t.struct(
        {
            "deblock": t.proxy(renames["DeblockIn"]).optional(),
            "audio": t.proxy(renames["AudioIn"]).optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "deinterlace": t.proxy(renames["DeinterlaceIn"]).optional(),
            "denoise": t.proxy(renames["DenoiseIn"]).optional(),
            "pad": t.proxy(renames["PadIn"]).optional(),
            "crop": t.proxy(renames["CropIn"]).optional(),
        }
    ).named(renames["PreprocessingConfigIn"])
    types["PreprocessingConfigOut"] = t.struct(
        {
            "deblock": t.proxy(renames["DeblockOut"]).optional(),
            "audio": t.proxy(renames["AudioOut"]).optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "deinterlace": t.proxy(renames["DeinterlaceOut"]).optional(),
            "denoise": t.proxy(renames["DenoiseOut"]).optional(),
            "pad": t.proxy(renames["PadOut"]).optional(),
            "crop": t.proxy(renames["CropOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PreprocessingConfigOut"])
    types["AdBreakIn"] = t.struct({"startTimeOffset": t.string().optional()}).named(
        renames["AdBreakIn"]
    )
    types["AdBreakOut"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdBreakOut"])
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
    types["ElementaryStreamIn"] = t.struct(
        {
            "videoStream": t.proxy(renames["VideoStreamIn"]).optional(),
            "audioStream": t.proxy(renames["AudioStreamIn"]).optional(),
            "key": t.string().optional(),
            "textStream": t.proxy(renames["TextStreamIn"]).optional(),
        }
    ).named(renames["ElementaryStreamIn"])
    types["ElementaryStreamOut"] = t.struct(
        {
            "videoStream": t.proxy(renames["VideoStreamOut"]).optional(),
            "audioStream": t.proxy(renames["AudioStreamOut"]).optional(),
            "key": t.string().optional(),
            "textStream": t.proxy(renames["TextStreamOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ElementaryStreamOut"])
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

    functions = {}
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
    functions["projectsLocationsJobTemplatesCreate"] = transcoder.get(
        "v1/{parent}/jobTemplates",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="transcoder",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
