from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_videointelligence():
    videointelligence = HTTPRuntime("https://videointelligence.googleapis.com/")

    renames = {
        "ErrorResponse": "_videointelligence_1_ErrorResponse",
        "GoogleCloudVideointelligenceV1_TextDetectionConfigIn": "_videointelligence_2_GoogleCloudVideointelligenceV1_TextDetectionConfigIn",
        "GoogleCloudVideointelligenceV1_TextDetectionConfigOut": "_videointelligence_3_GoogleCloudVideointelligenceV1_TextDetectionConfigOut",
        "GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgressIn": "_videointelligence_4_GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgressIn",
        "GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgressOut": "_videointelligence_5_GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgressOut",
        "GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn": "_videointelligence_6_GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn",
        "GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut": "_videointelligence_7_GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut",
        "GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgressIn": "_videointelligence_8_GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgressIn",
        "GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgressOut": "_videointelligence_9_GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgressOut",
        "GoogleCloudVideointelligenceV1_LabelSegmentIn": "_videointelligence_10_GoogleCloudVideointelligenceV1_LabelSegmentIn",
        "GoogleCloudVideointelligenceV1_LabelSegmentOut": "_videointelligence_11_GoogleCloudVideointelligenceV1_LabelSegmentOut",
        "GoogleCloudVideointelligenceV1p1beta1_WordInfoIn": "_videointelligence_12_GoogleCloudVideointelligenceV1p1beta1_WordInfoIn",
        "GoogleCloudVideointelligenceV1p1beta1_WordInfoOut": "_videointelligence_13_GoogleCloudVideointelligenceV1p1beta1_WordInfoOut",
        "GoogleCloudVideointelligenceV1p2beta1_TimestampedObjectIn": "_videointelligence_14_GoogleCloudVideointelligenceV1p2beta1_TimestampedObjectIn",
        "GoogleCloudVideointelligenceV1p2beta1_TimestampedObjectOut": "_videointelligence_15_GoogleCloudVideointelligenceV1p2beta1_TimestampedObjectOut",
        "GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionIn": "_videointelligence_16_GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionIn",
        "GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionOut": "_videointelligence_17_GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionOut",
        "GoogleCloudVideointelligenceV1p1beta1_FaceSegmentIn": "_videointelligence_18_GoogleCloudVideointelligenceV1p1beta1_FaceSegmentIn",
        "GoogleCloudVideointelligenceV1p1beta1_FaceSegmentOut": "_videointelligence_19_GoogleCloudVideointelligenceV1p1beta1_FaceSegmentOut",
        "GoogleCloudVideointelligenceV1p3beta1_LabelSegmentIn": "_videointelligence_20_GoogleCloudVideointelligenceV1p3beta1_LabelSegmentIn",
        "GoogleCloudVideointelligenceV1p3beta1_LabelSegmentOut": "_videointelligence_21_GoogleCloudVideointelligenceV1p3beta1_LabelSegmentOut",
        "GoogleCloudVideointelligenceV1_TimestampedObjectIn": "_videointelligence_22_GoogleCloudVideointelligenceV1_TimestampedObjectIn",
        "GoogleCloudVideointelligenceV1_TimestampedObjectOut": "_videointelligence_23_GoogleCloudVideointelligenceV1_TimestampedObjectOut",
        "GoogleCloudVideointelligenceV1p3beta1_CelebrityIn": "_videointelligence_24_GoogleCloudVideointelligenceV1p3beta1_CelebrityIn",
        "GoogleCloudVideointelligenceV1p3beta1_CelebrityOut": "_videointelligence_25_GoogleCloudVideointelligenceV1p3beta1_CelebrityOut",
        "GoogleCloudVideointelligenceV1_TrackIn": "_videointelligence_26_GoogleCloudVideointelligenceV1_TrackIn",
        "GoogleCloudVideointelligenceV1_TrackOut": "_videointelligence_27_GoogleCloudVideointelligenceV1_TrackOut",
        "GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationIn": "_videointelligence_28_GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationOut": "_videointelligence_29_GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxIn": "_videointelligence_30_GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxIn",
        "GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxOut": "_videointelligence_31_GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxOut",
        "GoogleCloudVideointelligenceV1beta2_FaceSegmentIn": "_videointelligence_32_GoogleCloudVideointelligenceV1beta2_FaceSegmentIn",
        "GoogleCloudVideointelligenceV1beta2_FaceSegmentOut": "_videointelligence_33_GoogleCloudVideointelligenceV1beta2_FaceSegmentOut",
        "GoogleCloudVideointelligenceV1beta2_TextSegmentIn": "_videointelligence_34_GoogleCloudVideointelligenceV1beta2_TextSegmentIn",
        "GoogleCloudVideointelligenceV1beta2_TextSegmentOut": "_videointelligence_35_GoogleCloudVideointelligenceV1beta2_TextSegmentOut",
        "GoogleCloudVideointelligenceV1_AnnotateVideoProgressIn": "_videointelligence_36_GoogleCloudVideointelligenceV1_AnnotateVideoProgressIn",
        "GoogleCloudVideointelligenceV1_AnnotateVideoProgressOut": "_videointelligence_37_GoogleCloudVideointelligenceV1_AnnotateVideoProgressOut",
        "GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotationIn": "_videointelligence_38_GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotationOut": "_videointelligence_39_GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1beta2_FaceFrameIn": "_videointelligence_40_GoogleCloudVideointelligenceV1beta2_FaceFrameIn",
        "GoogleCloudVideointelligenceV1beta2_FaceFrameOut": "_videointelligence_41_GoogleCloudVideointelligenceV1beta2_FaceFrameOut",
        "GoogleCloudVideointelligenceV1_DetectedLandmarkIn": "_videointelligence_42_GoogleCloudVideointelligenceV1_DetectedLandmarkIn",
        "GoogleCloudVideointelligenceV1_DetectedLandmarkOut": "_videointelligence_43_GoogleCloudVideointelligenceV1_DetectedLandmarkOut",
        "GoogleCloudVideointelligenceV1p3beta1_FaceFrameIn": "_videointelligence_44_GoogleCloudVideointelligenceV1p3beta1_FaceFrameIn",
        "GoogleCloudVideointelligenceV1p3beta1_FaceFrameOut": "_videointelligence_45_GoogleCloudVideointelligenceV1p3beta1_FaceFrameOut",
        "GoogleCloudVideointelligenceV1_FaceFrameIn": "_videointelligence_46_GoogleCloudVideointelligenceV1_FaceFrameIn",
        "GoogleCloudVideointelligenceV1_FaceFrameOut": "_videointelligence_47_GoogleCloudVideointelligenceV1_FaceFrameOut",
        "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationIn": "_videointelligence_48_GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationIn",
        "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationOut": "_videointelligence_49_GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationOut",
        "GoogleCloudVideointelligenceV1beta2_TextFrameIn": "_videointelligence_50_GoogleCloudVideointelligenceV1beta2_TextFrameIn",
        "GoogleCloudVideointelligenceV1beta2_TextFrameOut": "_videointelligence_51_GoogleCloudVideointelligenceV1beta2_TextFrameOut",
        "GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotationIn": "_videointelligence_52_GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotationOut": "_videointelligence_53_GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResultsIn": "_videointelligence_54_GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResultsIn",
        "GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResultsOut": "_videointelligence_55_GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResultsOut",
        "GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkIn": "_videointelligence_56_GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkIn",
        "GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkOut": "_videointelligence_57_GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkOut",
        "GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkIn": "_videointelligence_58_GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkIn",
        "GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkOut": "_videointelligence_59_GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkOut",
        "GoogleCloudVideointelligenceV1beta2_LabelSegmentIn": "_videointelligence_60_GoogleCloudVideointelligenceV1beta2_LabelSegmentIn",
        "GoogleCloudVideointelligenceV1beta2_LabelSegmentOut": "_videointelligence_61_GoogleCloudVideointelligenceV1beta2_LabelSegmentOut",
        "GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationIn": "_videointelligence_62_GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationIn",
        "GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationOut": "_videointelligence_63_GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationOut",
        "GoogleCloudVideointelligenceV1beta2_DetectedLandmarkIn": "_videointelligence_64_GoogleCloudVideointelligenceV1beta2_DetectedLandmarkIn",
        "GoogleCloudVideointelligenceV1beta2_DetectedLandmarkOut": "_videointelligence_65_GoogleCloudVideointelligenceV1beta2_DetectedLandmarkOut",
        "GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResultsIn": "_videointelligence_66_GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResultsIn",
        "GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResultsOut": "_videointelligence_67_GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResultsOut",
        "GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationIn": "_videointelligence_68_GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationIn",
        "GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationOut": "_videointelligence_69_GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationOut",
        "GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrityIn": "_videointelligence_70_GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrityIn",
        "GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrityOut": "_videointelligence_71_GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrityOut",
        "GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn": "_videointelligence_72_GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn",
        "GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut": "_videointelligence_73_GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut",
        "GoogleCloudVideointelligenceV1_AnnotateVideoResponseIn": "_videointelligence_74_GoogleCloudVideointelligenceV1_AnnotateVideoResponseIn",
        "GoogleCloudVideointelligenceV1_AnnotateVideoResponseOut": "_videointelligence_75_GoogleCloudVideointelligenceV1_AnnotateVideoResponseOut",
        "GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotationIn": "_videointelligence_76_GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotationIn",
        "GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotationOut": "_videointelligence_77_GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotationOut",
        "GoogleCloudVideointelligenceV1_ExplicitContentAnnotationIn": "_videointelligence_78_GoogleCloudVideointelligenceV1_ExplicitContentAnnotationIn",
        "GoogleCloudVideointelligenceV1_ExplicitContentAnnotationOut": "_videointelligence_79_GoogleCloudVideointelligenceV1_ExplicitContentAnnotationOut",
        "GoogleCloudVideointelligenceV1p1beta1_EntityIn": "_videointelligence_80_GoogleCloudVideointelligenceV1p1beta1_EntityIn",
        "GoogleCloudVideointelligenceV1p1beta1_EntityOut": "_videointelligence_81_GoogleCloudVideointelligenceV1p1beta1_EntityOut",
        "GoogleCloudVideointelligenceV1p1beta1_TextAnnotationIn": "_videointelligence_82_GoogleCloudVideointelligenceV1p1beta1_TextAnnotationIn",
        "GoogleCloudVideointelligenceV1p1beta1_TextAnnotationOut": "_videointelligence_83_GoogleCloudVideointelligenceV1p1beta1_TextAnnotationOut",
        "GoogleCloudVideointelligenceV1_EntityIn": "_videointelligence_84_GoogleCloudVideointelligenceV1_EntityIn",
        "GoogleCloudVideointelligenceV1_EntityOut": "_videointelligence_85_GoogleCloudVideointelligenceV1_EntityOut",
        "GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotationIn": "_videointelligence_86_GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotationIn",
        "GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotationOut": "_videointelligence_87_GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotationOut",
        "GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotationIn": "_videointelligence_88_GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotationIn",
        "GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotationOut": "_videointelligence_89_GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotationOut",
        "GoogleCloudVideointelligenceV1p1beta1_TrackIn": "_videointelligence_90_GoogleCloudVideointelligenceV1p1beta1_TrackIn",
        "GoogleCloudVideointelligenceV1p1beta1_TrackOut": "_videointelligence_91_GoogleCloudVideointelligenceV1p1beta1_TrackOut",
        "GoogleCloudVideointelligenceV1_FaceAnnotationIn": "_videointelligence_92_GoogleCloudVideointelligenceV1_FaceAnnotationIn",
        "GoogleCloudVideointelligenceV1_FaceAnnotationOut": "_videointelligence_93_GoogleCloudVideointelligenceV1_FaceAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_WordInfoIn": "_videointelligence_94_GoogleCloudVideointelligenceV1p2beta1_WordInfoIn",
        "GoogleCloudVideointelligenceV1p2beta1_WordInfoOut": "_videointelligence_95_GoogleCloudVideointelligenceV1p2beta1_WordInfoOut",
        "GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResultsIn": "_videointelligence_96_GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResultsIn",
        "GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResultsOut": "_videointelligence_97_GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResultsOut",
        "GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationIn": "_videointelligence_98_GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationIn",
        "GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationOut": "_videointelligence_99_GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationOut",
        "GoogleCloudVideointelligenceV1beta2_LabelAnnotationIn": "_videointelligence_100_GoogleCloudVideointelligenceV1beta2_LabelAnnotationIn",
        "GoogleCloudVideointelligenceV1beta2_LabelAnnotationOut": "_videointelligence_101_GoogleCloudVideointelligenceV1beta2_LabelAnnotationOut",
        "GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponseIn": "_videointelligence_102_GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponseIn",
        "GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponseOut": "_videointelligence_103_GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponseOut",
        "GoogleCloudVideointelligenceV1p1beta1_TextSegmentIn": "_videointelligence_104_GoogleCloudVideointelligenceV1p1beta1_TextSegmentIn",
        "GoogleCloudVideointelligenceV1p1beta1_TextSegmentOut": "_videointelligence_105_GoogleCloudVideointelligenceV1p1beta1_TextSegmentOut",
        "GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrameIn": "_videointelligence_106_GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrameIn",
        "GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrameOut": "_videointelligence_107_GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrameOut",
        "GoogleCloudVideointelligenceV1_LabelAnnotationIn": "_videointelligence_108_GoogleCloudVideointelligenceV1_LabelAnnotationIn",
        "GoogleCloudVideointelligenceV1_LabelAnnotationOut": "_videointelligence_109_GoogleCloudVideointelligenceV1_LabelAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPolyIn": "_videointelligence_110_GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPolyIn",
        "GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPolyOut": "_videointelligence_111_GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPolyOut",
        "GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponseIn": "_videointelligence_112_GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponseIn",
        "GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponseOut": "_videointelligence_113_GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponseOut",
        "GoogleCloudVideointelligenceV1p3beta1_TextSegmentIn": "_videointelligence_114_GoogleCloudVideointelligenceV1p3beta1_TextSegmentIn",
        "GoogleCloudVideointelligenceV1p3beta1_TextSegmentOut": "_videointelligence_115_GoogleCloudVideointelligenceV1p3beta1_TextSegmentOut",
        "GoogleCloudVideointelligenceV1p3beta1_TextFrameIn": "_videointelligence_116_GoogleCloudVideointelligenceV1p3beta1_TextFrameIn",
        "GoogleCloudVideointelligenceV1p3beta1_TextFrameOut": "_videointelligence_117_GoogleCloudVideointelligenceV1p3beta1_TextFrameOut",
        "GoogleCloudVideointelligenceV1_SpeechContextIn": "_videointelligence_118_GoogleCloudVideointelligenceV1_SpeechContextIn",
        "GoogleCloudVideointelligenceV1_SpeechContextOut": "_videointelligence_119_GoogleCloudVideointelligenceV1_SpeechContextOut",
        "GoogleCloudVideointelligenceV1_LabelFrameIn": "_videointelligence_120_GoogleCloudVideointelligenceV1_LabelFrameIn",
        "GoogleCloudVideointelligenceV1_LabelFrameOut": "_videointelligence_121_GoogleCloudVideointelligenceV1_LabelFrameOut",
        "GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotationIn": "_videointelligence_122_GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotationOut": "_videointelligence_123_GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackIn": "_videointelligence_124_GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackIn",
        "GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackOut": "_videointelligence_125_GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackOut",
        "GoogleCloudVideointelligenceV1_TextAnnotationIn": "_videointelligence_126_GoogleCloudVideointelligenceV1_TextAnnotationIn",
        "GoogleCloudVideointelligenceV1_TextAnnotationOut": "_videointelligence_127_GoogleCloudVideointelligenceV1_TextAnnotationOut",
        "GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPolyIn": "_videointelligence_128_GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPolyIn",
        "GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPolyOut": "_videointelligence_129_GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPolyOut",
        "GoogleCloudVideointelligenceV1p2beta1_FaceFrameIn": "_videointelligence_130_GoogleCloudVideointelligenceV1p2beta1_FaceFrameIn",
        "GoogleCloudVideointelligenceV1p2beta1_FaceFrameOut": "_videointelligence_131_GoogleCloudVideointelligenceV1p2beta1_FaceFrameOut",
        "GoogleLongrunning_ListOperationsResponseIn": "_videointelligence_132_GoogleLongrunning_ListOperationsResponseIn",
        "GoogleLongrunning_ListOperationsResponseOut": "_videointelligence_133_GoogleLongrunning_ListOperationsResponseOut",
        "GoogleLongrunning_CancelOperationRequestIn": "_videointelligence_134_GoogleLongrunning_CancelOperationRequestIn",
        "GoogleLongrunning_CancelOperationRequestOut": "_videointelligence_135_GoogleLongrunning_CancelOperationRequestOut",
        "GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeIn": "_videointelligence_136_GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeIn",
        "GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeOut": "_videointelligence_137_GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeOut",
        "GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternativeIn": "_videointelligence_138_GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternativeIn",
        "GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternativeOut": "_videointelligence_139_GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternativeOut",
        "GoogleCloudVideointelligenceV1beta2_TimestampedObjectIn": "_videointelligence_140_GoogleCloudVideointelligenceV1beta2_TimestampedObjectIn",
        "GoogleCloudVideointelligenceV1beta2_TimestampedObjectOut": "_videointelligence_141_GoogleCloudVideointelligenceV1beta2_TimestampedObjectOut",
        "GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponseIn": "_videointelligence_142_GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponseIn",
        "GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponseOut": "_videointelligence_143_GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponseOut",
        "GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgressIn": "_videointelligence_144_GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgressIn",
        "GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgressOut": "_videointelligence_145_GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgressOut",
        "GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationIn": "_videointelligence_146_GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationOut": "_videointelligence_147_GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxIn": "_videointelligence_148_GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxIn",
        "GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxOut": "_videointelligence_149_GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxOut",
        "GoogleCloudVideointelligenceV1_WordInfoIn": "_videointelligence_150_GoogleCloudVideointelligenceV1_WordInfoIn",
        "GoogleCloudVideointelligenceV1_WordInfoOut": "_videointelligence_151_GoogleCloudVideointelligenceV1_WordInfoOut",
        "GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionIn": "_videointelligence_152_GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionIn",
        "GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionOut": "_videointelligence_153_GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionOut",
        "GoogleCloudVideointelligenceV1_VideoAnnotationProgressIn": "_videointelligence_154_GoogleCloudVideointelligenceV1_VideoAnnotationProgressIn",
        "GoogleCloudVideointelligenceV1_VideoAnnotationProgressOut": "_videointelligence_155_GoogleCloudVideointelligenceV1_VideoAnnotationProgressOut",
        "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationIn": "_videointelligence_156_GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationIn",
        "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationOut": "_videointelligence_157_GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationIn": "_videointelligence_158_GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationIn",
        "GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationOut": "_videointelligence_159_GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationOut",
        "GoogleCloudVideointelligenceV1beta2_LabelFrameIn": "_videointelligence_160_GoogleCloudVideointelligenceV1beta2_LabelFrameIn",
        "GoogleCloudVideointelligenceV1beta2_LabelFrameOut": "_videointelligence_161_GoogleCloudVideointelligenceV1beta2_LabelFrameOut",
        "GoogleProtobuf_EmptyIn": "_videointelligence_162_GoogleProtobuf_EmptyIn",
        "GoogleProtobuf_EmptyOut": "_videointelligence_163_GoogleProtobuf_EmptyOut",
        "GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgressIn": "_videointelligence_164_GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgressIn",
        "GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgressOut": "_videointelligence_165_GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgressOut",
        "GoogleCloudVideointelligenceV1beta2_TextAnnotationIn": "_videointelligence_166_GoogleCloudVideointelligenceV1beta2_TextAnnotationIn",
        "GoogleCloudVideointelligenceV1beta2_TextAnnotationOut": "_videointelligence_167_GoogleCloudVideointelligenceV1beta2_TextAnnotationOut",
        "GoogleCloudVideointelligenceV1beta2_NormalizedVertexIn": "_videointelligence_168_GoogleCloudVideointelligenceV1beta2_NormalizedVertexIn",
        "GoogleCloudVideointelligenceV1beta2_NormalizedVertexOut": "_videointelligence_169_GoogleCloudVideointelligenceV1beta2_NormalizedVertexOut",
        "GoogleCloudVideointelligenceV1beta2_VideoAnnotationResultsIn": "_videointelligence_170_GoogleCloudVideointelligenceV1beta2_VideoAnnotationResultsIn",
        "GoogleCloudVideointelligenceV1beta2_VideoAnnotationResultsOut": "_videointelligence_171_GoogleCloudVideointelligenceV1beta2_VideoAnnotationResultsOut",
        "GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotationIn": "_videointelligence_172_GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotationIn",
        "GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotationOut": "_videointelligence_173_GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrameIn": "_videointelligence_174_GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrameIn",
        "GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrameOut": "_videointelligence_175_GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrameOut",
        "GoogleCloudVideointelligenceV1_NormalizedBoundingBoxIn": "_videointelligence_176_GoogleCloudVideointelligenceV1_NormalizedBoundingBoxIn",
        "GoogleCloudVideointelligenceV1_NormalizedBoundingBoxOut": "_videointelligence_177_GoogleCloudVideointelligenceV1_NormalizedBoundingBoxOut",
        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrameIn": "_videointelligence_178_GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrameIn",
        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrameOut": "_videointelligence_179_GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrameOut",
        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationIn": "_videointelligence_180_GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationIn",
        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationOut": "_videointelligence_181_GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponseIn": "_videointelligence_182_GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponseIn",
        "GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponseOut": "_videointelligence_183_GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponseOut",
        "GoogleCloudVideointelligenceV1_AnnotateVideoRequestIn": "_videointelligence_184_GoogleCloudVideointelligenceV1_AnnotateVideoRequestIn",
        "GoogleCloudVideointelligenceV1_AnnotateVideoRequestOut": "_videointelligence_185_GoogleCloudVideointelligenceV1_AnnotateVideoRequestOut",
        "GoogleCloudVideointelligenceV1p2beta1_TrackIn": "_videointelligence_186_GoogleCloudVideointelligenceV1p2beta1_TrackIn",
        "GoogleCloudVideointelligenceV1p2beta1_TrackOut": "_videointelligence_187_GoogleCloudVideointelligenceV1p2beta1_TrackOut",
        "GoogleCloudVideointelligenceV1beta2_TrackIn": "_videointelligence_188_GoogleCloudVideointelligenceV1beta2_TrackIn",
        "GoogleCloudVideointelligenceV1beta2_TrackOut": "_videointelligence_189_GoogleCloudVideointelligenceV1beta2_TrackOut",
        "GoogleCloudVideointelligenceV1p2beta1_LabelFrameIn": "_videointelligence_190_GoogleCloudVideointelligenceV1p2beta1_LabelFrameIn",
        "GoogleCloudVideointelligenceV1p2beta1_LabelFrameOut": "_videointelligence_191_GoogleCloudVideointelligenceV1p2beta1_LabelFrameOut",
        "GoogleCloudVideointelligenceV1_PersonDetectionAnnotationIn": "_videointelligence_192_GoogleCloudVideointelligenceV1_PersonDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1_PersonDetectionAnnotationOut": "_videointelligence_193_GoogleCloudVideointelligenceV1_PersonDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameIn": "_videointelligence_194_GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameIn",
        "GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameOut": "_videointelligence_195_GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameOut",
        "GoogleCloudVideointelligenceV1_PersonDetectionConfigIn": "_videointelligence_196_GoogleCloudVideointelligenceV1_PersonDetectionConfigIn",
        "GoogleCloudVideointelligenceV1_PersonDetectionConfigOut": "_videointelligence_197_GoogleCloudVideointelligenceV1_PersonDetectionConfigOut",
        "GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternativeIn": "_videointelligence_198_GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternativeIn",
        "GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternativeOut": "_videointelligence_199_GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternativeOut",
        "GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgressIn": "_videointelligence_200_GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgressIn",
        "GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgressOut": "_videointelligence_201_GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgressOut",
        "GoogleCloudVideointelligenceV1p2beta1_FaceSegmentIn": "_videointelligence_202_GoogleCloudVideointelligenceV1p2beta1_FaceSegmentIn",
        "GoogleCloudVideointelligenceV1p2beta1_FaceSegmentOut": "_videointelligence_203_GoogleCloudVideointelligenceV1p2beta1_FaceSegmentOut",
        "GoogleCloudVideointelligenceV1beta2_FaceAnnotationIn": "_videointelligence_204_GoogleCloudVideointelligenceV1beta2_FaceAnnotationIn",
        "GoogleCloudVideointelligenceV1beta2_FaceAnnotationOut": "_videointelligence_205_GoogleCloudVideointelligenceV1beta2_FaceAnnotationOut",
        "GoogleCloudVideointelligenceV1p3beta1_LabelFrameIn": "_videointelligence_206_GoogleCloudVideointelligenceV1p3beta1_LabelFrameIn",
        "GoogleCloudVideointelligenceV1p3beta1_LabelFrameOut": "_videointelligence_207_GoogleCloudVideointelligenceV1p3beta1_LabelFrameOut",
        "GoogleCloudVideointelligenceV1_TextSegmentIn": "_videointelligence_208_GoogleCloudVideointelligenceV1_TextSegmentIn",
        "GoogleCloudVideointelligenceV1_TextSegmentOut": "_videointelligence_209_GoogleCloudVideointelligenceV1_TextSegmentOut",
        "GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResultsIn": "_videointelligence_210_GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResultsIn",
        "GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResultsOut": "_videointelligence_211_GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResultsOut",
        "GoogleCloudVideointelligenceV1_LogoRecognitionAnnotationIn": "_videointelligence_212_GoogleCloudVideointelligenceV1_LogoRecognitionAnnotationIn",
        "GoogleCloudVideointelligenceV1_LogoRecognitionAnnotationOut": "_videointelligence_213_GoogleCloudVideointelligenceV1_LogoRecognitionAnnotationOut",
        "GoogleCloudVideointelligenceV1p3beta1_EntityIn": "_videointelligence_214_GoogleCloudVideointelligenceV1p3beta1_EntityIn",
        "GoogleCloudVideointelligenceV1p3beta1_EntityOut": "_videointelligence_215_GoogleCloudVideointelligenceV1p3beta1_EntityOut",
        "GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgressIn": "_videointelligence_216_GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgressIn",
        "GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgressOut": "_videointelligence_217_GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgressOut",
        "GoogleCloudVideointelligenceV1p3beta1_TimestampedObjectIn": "_videointelligence_218_GoogleCloudVideointelligenceV1p3beta1_TimestampedObjectIn",
        "GoogleCloudVideointelligenceV1p3beta1_TimestampedObjectOut": "_videointelligence_219_GoogleCloudVideointelligenceV1p3beta1_TimestampedObjectOut",
        "GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigIn": "_videointelligence_220_GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigIn",
        "GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigOut": "_videointelligence_221_GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigOut",
        "GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeIn": "_videointelligence_222_GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeIn",
        "GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeOut": "_videointelligence_223_GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeOut",
        "GoogleCloudVideointelligenceV1_FaceSegmentIn": "_videointelligence_224_GoogleCloudVideointelligenceV1_FaceSegmentIn",
        "GoogleCloudVideointelligenceV1_FaceSegmentOut": "_videointelligence_225_GoogleCloudVideointelligenceV1_FaceSegmentOut",
        "GoogleCloudVideointelligenceV1beta2_DetectedAttributeIn": "_videointelligence_226_GoogleCloudVideointelligenceV1beta2_DetectedAttributeIn",
        "GoogleCloudVideointelligenceV1beta2_DetectedAttributeOut": "_videointelligence_227_GoogleCloudVideointelligenceV1beta2_DetectedAttributeOut",
        "GoogleCloudVideointelligenceV1_VideoAnnotationResultsIn": "_videointelligence_228_GoogleCloudVideointelligenceV1_VideoAnnotationResultsIn",
        "GoogleCloudVideointelligenceV1_VideoAnnotationResultsOut": "_videointelligence_229_GoogleCloudVideointelligenceV1_VideoAnnotationResultsOut",
        "GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationIn": "_videointelligence_230_GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationIn",
        "GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationOut": "_videointelligence_231_GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationOut",
        "GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigIn": "_videointelligence_232_GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigIn",
        "GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigOut": "_videointelligence_233_GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigOut",
        "GoogleCloudVideointelligenceV1p1beta1_FaceFrameIn": "_videointelligence_234_GoogleCloudVideointelligenceV1p1beta1_FaceFrameIn",
        "GoogleCloudVideointelligenceV1p1beta1_FaceFrameOut": "_videointelligence_235_GoogleCloudVideointelligenceV1p1beta1_FaceFrameOut",
        "GoogleCloudVideointelligenceV1p2beta1_TextAnnotationIn": "_videointelligence_236_GoogleCloudVideointelligenceV1p2beta1_TextAnnotationIn",
        "GoogleCloudVideointelligenceV1p2beta1_TextAnnotationOut": "_videointelligence_237_GoogleCloudVideointelligenceV1p2beta1_TextAnnotationOut",
        "GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPolyIn": "_videointelligence_238_GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPolyIn",
        "GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPolyOut": "_videointelligence_239_GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPolyOut",
        "GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrameIn": "_videointelligence_240_GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrameIn",
        "GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrameOut": "_videointelligence_241_GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrameOut",
        "GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgressIn": "_videointelligence_242_GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgressIn",
        "GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgressOut": "_videointelligence_243_GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgressOut",
        "GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn": "_videointelligence_244_GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn",
        "GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut": "_videointelligence_245_GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationIn": "_videointelligence_246_GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationIn",
        "GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationOut": "_videointelligence_247_GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationOut",
        "GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeIn": "_videointelligence_248_GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeIn",
        "GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeOut": "_videointelligence_249_GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeOut",
        "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrameIn": "_videointelligence_250_GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrameIn",
        "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrameOut": "_videointelligence_251_GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrameOut",
        "GoogleCloudVideointelligenceV1_FaceDetectionConfigIn": "_videointelligence_252_GoogleCloudVideointelligenceV1_FaceDetectionConfigIn",
        "GoogleCloudVideointelligenceV1_FaceDetectionConfigOut": "_videointelligence_253_GoogleCloudVideointelligenceV1_FaceDetectionConfigOut",
        "GoogleCloudVideointelligenceV1_ExplicitContentDetectionConfigIn": "_videointelligence_254_GoogleCloudVideointelligenceV1_ExplicitContentDetectionConfigIn",
        "GoogleCloudVideointelligenceV1_ExplicitContentDetectionConfigOut": "_videointelligence_255_GoogleCloudVideointelligenceV1_ExplicitContentDetectionConfigOut",
        "GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxIn": "_videointelligence_256_GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxIn",
        "GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxOut": "_videointelligence_257_GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxOut",
        "GoogleLongrunning_OperationIn": "_videointelligence_258_GoogleLongrunning_OperationIn",
        "GoogleLongrunning_OperationOut": "_videointelligence_259_GoogleLongrunning_OperationOut",
        "GoogleCloudVideointelligenceV1p1beta1_TimestampedObjectIn": "_videointelligence_260_GoogleCloudVideointelligenceV1p1beta1_TimestampedObjectIn",
        "GoogleCloudVideointelligenceV1p1beta1_TimestampedObjectOut": "_videointelligence_261_GoogleCloudVideointelligenceV1p1beta1_TimestampedObjectOut",
        "GoogleRpc_StatusIn": "_videointelligence_262_GoogleRpc_StatusIn",
        "GoogleRpc_StatusOut": "_videointelligence_263_GoogleRpc_StatusOut",
        "GoogleCloudVideointelligenceV1_FaceDetectionAnnotationIn": "_videointelligence_264_GoogleCloudVideointelligenceV1_FaceDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1_FaceDetectionAnnotationOut": "_videointelligence_265_GoogleCloudVideointelligenceV1_FaceDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationIn": "_videointelligence_266_GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationIn",
        "GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationOut": "_videointelligence_267_GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_TextSegmentIn": "_videointelligence_268_GoogleCloudVideointelligenceV1p2beta1_TextSegmentIn",
        "GoogleCloudVideointelligenceV1p2beta1_TextSegmentOut": "_videointelligence_269_GoogleCloudVideointelligenceV1p2beta1_TextSegmentOut",
        "GoogleCloudVideointelligenceV1_DetectedAttributeIn": "_videointelligence_270_GoogleCloudVideointelligenceV1_DetectedAttributeIn",
        "GoogleCloudVideointelligenceV1_DetectedAttributeOut": "_videointelligence_271_GoogleCloudVideointelligenceV1_DetectedAttributeOut",
        "GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotationIn": "_videointelligence_272_GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotationOut": "_videointelligence_273_GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_LabelSegmentIn": "_videointelligence_274_GoogleCloudVideointelligenceV1p2beta1_LabelSegmentIn",
        "GoogleCloudVideointelligenceV1p2beta1_LabelSegmentOut": "_videointelligence_275_GoogleCloudVideointelligenceV1p2beta1_LabelSegmentOut",
        "GoogleCloudVideointelligenceV1p3beta1_TextAnnotationIn": "_videointelligence_276_GoogleCloudVideointelligenceV1p3beta1_TextAnnotationIn",
        "GoogleCloudVideointelligenceV1p3beta1_TextAnnotationOut": "_videointelligence_277_GoogleCloudVideointelligenceV1p3beta1_TextAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationIn": "_videointelligence_278_GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationIn",
        "GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationOut": "_videointelligence_279_GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationOut",
        "GoogleCloudVideointelligenceV1p1beta1_LabelSegmentIn": "_videointelligence_280_GoogleCloudVideointelligenceV1p1beta1_LabelSegmentIn",
        "GoogleCloudVideointelligenceV1p1beta1_LabelSegmentOut": "_videointelligence_281_GoogleCloudVideointelligenceV1p1beta1_LabelSegmentOut",
        "GoogleCloudVideointelligenceV1p3beta1_FaceSegmentIn": "_videointelligence_282_GoogleCloudVideointelligenceV1p3beta1_FaceSegmentIn",
        "GoogleCloudVideointelligenceV1p3beta1_FaceSegmentOut": "_videointelligence_283_GoogleCloudVideointelligenceV1p3beta1_FaceSegmentOut",
        "GoogleCloudVideointelligenceV1p3beta1_NormalizedVertexIn": "_videointelligence_284_GoogleCloudVideointelligenceV1p3beta1_NormalizedVertexIn",
        "GoogleCloudVideointelligenceV1p3beta1_NormalizedVertexOut": "_videointelligence_285_GoogleCloudVideointelligenceV1p3beta1_NormalizedVertexOut",
        "GoogleCloudVideointelligenceV1p3beta1_WordInfoIn": "_videointelligence_286_GoogleCloudVideointelligenceV1p3beta1_WordInfoIn",
        "GoogleCloudVideointelligenceV1p3beta1_WordInfoOut": "_videointelligence_287_GoogleCloudVideointelligenceV1p3beta1_WordInfoOut",
        "GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn": "_videointelligence_288_GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn",
        "GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut": "_videointelligence_289_GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut",
        "GoogleCloudVideointelligenceV1p2beta1_SpeechTranscriptionIn": "_videointelligence_290_GoogleCloudVideointelligenceV1p2beta1_SpeechTranscriptionIn",
        "GoogleCloudVideointelligenceV1p2beta1_SpeechTranscriptionOut": "_videointelligence_291_GoogleCloudVideointelligenceV1p2beta1_SpeechTranscriptionOut",
        "GoogleCloudVideointelligenceV1_VideoSegmentIn": "_videointelligence_292_GoogleCloudVideointelligenceV1_VideoSegmentIn",
        "GoogleCloudVideointelligenceV1_VideoSegmentOut": "_videointelligence_293_GoogleCloudVideointelligenceV1_VideoSegmentOut",
        "GoogleCloudVideointelligenceV1_ExplicitContentFrameIn": "_videointelligence_294_GoogleCloudVideointelligenceV1_ExplicitContentFrameIn",
        "GoogleCloudVideointelligenceV1_ExplicitContentFrameOut": "_videointelligence_295_GoogleCloudVideointelligenceV1_ExplicitContentFrameOut",
        "GoogleCloudVideointelligenceV1_NormalizedBoundingPolyIn": "_videointelligence_296_GoogleCloudVideointelligenceV1_NormalizedBoundingPolyIn",
        "GoogleCloudVideointelligenceV1_NormalizedBoundingPolyOut": "_videointelligence_297_GoogleCloudVideointelligenceV1_NormalizedBoundingPolyOut",
        "GoogleCloudVideointelligenceV1_SpeechRecognitionAlternativeIn": "_videointelligence_298_GoogleCloudVideointelligenceV1_SpeechRecognitionAlternativeIn",
        "GoogleCloudVideointelligenceV1_SpeechRecognitionAlternativeOut": "_videointelligence_299_GoogleCloudVideointelligenceV1_SpeechRecognitionAlternativeOut",
        "GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionIn": "_videointelligence_300_GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionIn",
        "GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionOut": "_videointelligence_301_GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionOut",
        "GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationIn": "_videointelligence_302_GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationOut": "_videointelligence_303_GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPolyIn": "_videointelligence_304_GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPolyIn",
        "GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPolyOut": "_videointelligence_305_GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPolyOut",
        "GoogleCloudVideointelligenceV1p2beta1_EntityIn": "_videointelligence_306_GoogleCloudVideointelligenceV1p2beta1_EntityIn",
        "GoogleCloudVideointelligenceV1p2beta1_EntityOut": "_videointelligence_307_GoogleCloudVideointelligenceV1p2beta1_EntityOut",
        "GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationIn": "_videointelligence_308_GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationOut": "_videointelligence_309_GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1_SpeechTranscriptionIn": "_videointelligence_310_GoogleCloudVideointelligenceV1_SpeechTranscriptionIn",
        "GoogleCloudVideointelligenceV1_SpeechTranscriptionOut": "_videointelligence_311_GoogleCloudVideointelligenceV1_SpeechTranscriptionOut",
        "GoogleCloudVideointelligenceV1beta2_ExplicitContentFrameIn": "_videointelligence_312_GoogleCloudVideointelligenceV1beta2_ExplicitContentFrameIn",
        "GoogleCloudVideointelligenceV1beta2_ExplicitContentFrameOut": "_videointelligence_313_GoogleCloudVideointelligenceV1beta2_ExplicitContentFrameOut",
        "GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkIn": "_videointelligence_314_GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkIn",
        "GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkOut": "_videointelligence_315_GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkOut",
        "GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotationIn": "_videointelligence_316_GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotationIn",
        "GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotationOut": "_videointelligence_317_GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotationOut",
        "GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponseIn": "_videointelligence_318_GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponseIn",
        "GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponseOut": "_videointelligence_319_GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponseOut",
        "GoogleCloudVideointelligenceV1_LabelDetectionConfigIn": "_videointelligence_320_GoogleCloudVideointelligenceV1_LabelDetectionConfigIn",
        "GoogleCloudVideointelligenceV1_LabelDetectionConfigOut": "_videointelligence_321_GoogleCloudVideointelligenceV1_LabelDetectionConfigOut",
        "GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationIn": "_videointelligence_322_GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationIn",
        "GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationOut": "_videointelligence_323_GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationOut",
        "GoogleCloudVideointelligenceV1_TextFrameIn": "_videointelligence_324_GoogleCloudVideointelligenceV1_TextFrameIn",
        "GoogleCloudVideointelligenceV1_TextFrameOut": "_videointelligence_325_GoogleCloudVideointelligenceV1_TextFrameOut",
        "GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationIn": "_videointelligence_326_GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationIn",
        "GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationOut": "_videointelligence_327_GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationOut",
        "GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxIn": "_videointelligence_328_GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxIn",
        "GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxOut": "_videointelligence_329_GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxOut",
        "GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgressIn": "_videointelligence_330_GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgressIn",
        "GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgressOut": "_videointelligence_331_GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgressOut",
        "GoogleCloudVideointelligenceV1_NormalizedVertexIn": "_videointelligence_332_GoogleCloudVideointelligenceV1_NormalizedVertexIn",
        "GoogleCloudVideointelligenceV1_NormalizedVertexOut": "_videointelligence_333_GoogleCloudVideointelligenceV1_NormalizedVertexOut",
        "GoogleCloudVideointelligenceV1beta2_VideoSegmentIn": "_videointelligence_334_GoogleCloudVideointelligenceV1beta2_VideoSegmentIn",
        "GoogleCloudVideointelligenceV1beta2_VideoSegmentOut": "_videointelligence_335_GoogleCloudVideointelligenceV1beta2_VideoSegmentOut",
        "GoogleCloudVideointelligenceV1_ObjectTrackingConfigIn": "_videointelligence_336_GoogleCloudVideointelligenceV1_ObjectTrackingConfigIn",
        "GoogleCloudVideointelligenceV1_ObjectTrackingConfigOut": "_videointelligence_337_GoogleCloudVideointelligenceV1_ObjectTrackingConfigOut",
        "GoogleCloudVideointelligenceV1_VideoContextIn": "_videointelligence_338_GoogleCloudVideointelligenceV1_VideoContextIn",
        "GoogleCloudVideointelligenceV1_VideoContextOut": "_videointelligence_339_GoogleCloudVideointelligenceV1_VideoContextOut",
        "GoogleCloudVideointelligenceV1p2beta1_NormalizedVertexIn": "_videointelligence_340_GoogleCloudVideointelligenceV1p2beta1_NormalizedVertexIn",
        "GoogleCloudVideointelligenceV1p2beta1_NormalizedVertexOut": "_videointelligence_341_GoogleCloudVideointelligenceV1p2beta1_NormalizedVertexOut",
        "GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternativeIn": "_videointelligence_342_GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternativeIn",
        "GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternativeOut": "_videointelligence_343_GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternativeOut",
        "GoogleCloudVideointelligenceV1p1beta1_TextFrameIn": "_videointelligence_344_GoogleCloudVideointelligenceV1p1beta1_TextFrameIn",
        "GoogleCloudVideointelligenceV1p1beta1_TextFrameOut": "_videointelligence_345_GoogleCloudVideointelligenceV1p1beta1_TextFrameOut",
        "GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeIn": "_videointelligence_346_GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeIn",
        "GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeOut": "_videointelligence_347_GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeOut",
        "GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotationIn": "_videointelligence_348_GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotationIn",
        "GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotationOut": "_videointelligence_349_GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotationOut",
        "GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexIn": "_videointelligence_350_GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexIn",
        "GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexOut": "_videointelligence_351_GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexOut",
        "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameIn": "_videointelligence_352_GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameIn",
        "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameOut": "_videointelligence_353_GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameOut",
        "GoogleCloudVideointelligenceV1p1beta1_LabelFrameIn": "_videointelligence_354_GoogleCloudVideointelligenceV1p1beta1_LabelFrameIn",
        "GoogleCloudVideointelligenceV1p1beta1_LabelFrameOut": "_videointelligence_355_GoogleCloudVideointelligenceV1p1beta1_LabelFrameOut",
        "GoogleCloudVideointelligenceV1p2beta1_TextFrameIn": "_videointelligence_356_GoogleCloudVideointelligenceV1p2beta1_TextFrameIn",
        "GoogleCloudVideointelligenceV1p2beta1_TextFrameOut": "_videointelligence_357_GoogleCloudVideointelligenceV1p2beta1_TextFrameOut",
        "GoogleCloudVideointelligenceV1p3beta1_TrackIn": "_videointelligence_358_GoogleCloudVideointelligenceV1p3beta1_TrackIn",
        "GoogleCloudVideointelligenceV1p3beta1_TrackOut": "_videointelligence_359_GoogleCloudVideointelligenceV1p3beta1_TrackOut",
        "GoogleCloudVideointelligenceV1beta2_EntityIn": "_videointelligence_360_GoogleCloudVideointelligenceV1beta2_EntityIn",
        "GoogleCloudVideointelligenceV1beta2_EntityOut": "_videointelligence_361_GoogleCloudVideointelligenceV1beta2_EntityOut",
        "GoogleCloudVideointelligenceV1_ObjectTrackingFrameIn": "_videointelligence_362_GoogleCloudVideointelligenceV1_ObjectTrackingFrameIn",
        "GoogleCloudVideointelligenceV1_ObjectTrackingFrameOut": "_videointelligence_363_GoogleCloudVideointelligenceV1_ObjectTrackingFrameOut",
        "GoogleCloudVideointelligenceV1beta2_WordInfoIn": "_videointelligence_364_GoogleCloudVideointelligenceV1beta2_WordInfoIn",
        "GoogleCloudVideointelligenceV1beta2_WordInfoOut": "_videointelligence_365_GoogleCloudVideointelligenceV1beta2_WordInfoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudVideointelligenceV1_TextDetectionConfigIn"] = t.struct(
        {
            "model": t.string().optional(),
            "languageHints": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TextDetectionConfigIn"])
    types["GoogleCloudVideointelligenceV1_TextDetectionConfigOut"] = t.struct(
        {
            "model": t.string().optional(),
            "languageHints": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TextDetectionConfigOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgressIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"]
            ).optional(),
            "progressPercent": t.integer().optional(),
            "inputUri": t.string().optional(),
            "feature": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgressIn"])
    types[
        "GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgressOut"
    ] = t.struct(
        {
            "startTime": t.string().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"]
            ).optional(),
            "progressPercent": t.integer().optional(),
            "inputUri": t.string().optional(),
            "feature": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgressOut"]
    )
    types["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"] = t.struct(
        {
            "endTimeOffset": t.string().optional(),
            "startTimeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"] = t.struct(
        {
            "endTimeOffset": t.string().optional(),
            "startTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgressIn"] = t.struct(
        {
            "annotationProgress": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgressIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgressIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgressOut"] = t.struct(
        {
            "annotationProgress": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgressOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgressOut"])
    types["GoogleCloudVideointelligenceV1_LabelSegmentIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_LabelSegmentIn"])
    types["GoogleCloudVideointelligenceV1_LabelSegmentOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_LabelSegmentOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_WordInfoIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "word": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_WordInfoIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_WordInfoOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "word": t.string().optional(),
            "speakerTag": t.integer().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_WordInfoOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_TimestampedObjectIn"] = t.struct(
        {
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxIn"]
            ).optional(),
            "attributes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeIn"]
                )
            ).optional(),
            "landmarks": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkIn"]
                )
            ).optional(),
            "timeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TimestampedObjectIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_TimestampedObjectOut"] = t.struct(
        {
            "normalizedBoundingBox": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxOut"
                ]
            ).optional(),
            "attributes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeOut"
                    ]
                )
            ).optional(),
            "landmarks": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkOut"]
                )
            ).optional(),
            "timeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TimestampedObjectOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionIn"] = t.struct(
        {
            "alternatives": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternativeIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "alternatives": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternativeOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_FaceSegmentIn"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_FaceSegmentIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_FaceSegmentOut"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_FaceSegmentOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_LabelSegmentIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_LabelSegmentIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_LabelSegmentOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_LabelSegmentOut"])
    types["GoogleCloudVideointelligenceV1_TimestampedObjectIn"] = t.struct(
        {
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1_NormalizedBoundingBoxIn"]
            ).optional(),
            "timeOffset": t.string().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_DetectedLandmarkIn"])
            ).optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_DetectedAttributeIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TimestampedObjectIn"])
    types["GoogleCloudVideointelligenceV1_TimestampedObjectOut"] = t.struct(
        {
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1_NormalizedBoundingBoxOut"]
            ).optional(),
            "timeOffset": t.string().optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_DetectedLandmarkOut"])
            ).optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_DetectedAttributeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TimestampedObjectOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_CelebrityIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_CelebrityIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_CelebrityOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_CelebrityOut"])
    types["GoogleCloudVideointelligenceV1_TrackIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_DetectedAttributeIn"])
            ).optional(),
            "timestampedObjects": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TimestampedObjectIn"])
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TrackIn"])
    types["GoogleCloudVideointelligenceV1_TrackOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_DetectedAttributeOut"])
            ).optional(),
            "timestampedObjects": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TimestampedObjectOut"])
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TrackOut"])
    types[
        "GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationIn"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TrackIn"])
            ).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationOut"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TrackOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxIn"] = t.struct(
        {
            "bottom": t.number().optional(),
            "left": t.number().optional(),
            "right": t.number().optional(),
            "top": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxOut"] = t.struct(
        {
            "bottom": t.number().optional(),
            "left": t.number().optional(),
            "right": t.number().optional(),
            "top": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxOut"])
    types["GoogleCloudVideointelligenceV1beta2_FaceSegmentIn"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_FaceSegmentIn"])
    types["GoogleCloudVideointelligenceV1beta2_FaceSegmentOut"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_FaceSegmentOut"])
    types["GoogleCloudVideointelligenceV1beta2_TextSegmentIn"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TextFrameIn"])
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"]
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_TextSegmentIn"])
    types["GoogleCloudVideointelligenceV1beta2_TextSegmentOut"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TextFrameOut"])
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_TextSegmentOut"])
    types["GoogleCloudVideointelligenceV1_AnnotateVideoProgressIn"] = t.struct(
        {
            "annotationProgress": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_VideoAnnotationProgressIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1_AnnotateVideoProgressIn"])
    types["GoogleCloudVideointelligenceV1_AnnotateVideoProgressOut"] = t.struct(
        {
            "annotationProgress": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_VideoAnnotationProgressOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_AnnotateVideoProgressOut"])
    types["GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotationIn"] = t.struct(
        {
            "version": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TrackIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotationIn"])
    types[
        "GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotationOut"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TrackOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1beta2_FaceFrameIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "normalizedBoundingBoxes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_FaceFrameIn"])
    types["GoogleCloudVideointelligenceV1beta2_FaceFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "normalizedBoundingBoxes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_FaceFrameOut"])
    types["GoogleCloudVideointelligenceV1_DetectedLandmarkIn"] = t.struct(
        {
            "point": t.proxy(
                renames["GoogleCloudVideointelligenceV1_NormalizedVertexIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_DetectedLandmarkIn"])
    types["GoogleCloudVideointelligenceV1_DetectedLandmarkOut"] = t.struct(
        {
            "point": t.proxy(
                renames["GoogleCloudVideointelligenceV1_NormalizedVertexOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_DetectedLandmarkOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_FaceFrameIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "normalizedBoundingBoxes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_FaceFrameIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_FaceFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "normalizedBoundingBoxes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_FaceFrameOut"])
    types["GoogleCloudVideointelligenceV1_FaceFrameIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "normalizedBoundingBoxes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_NormalizedBoundingBoxIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_FaceFrameIn"])
    types["GoogleCloudVideointelligenceV1_FaceFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "normalizedBoundingBoxes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_NormalizedBoundingBoxOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_FaceFrameOut"])
    types[
        "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationIn"
    ] = t.struct(
        {
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameIn"
                    ]
                )
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationOut"
    ] = t.struct(
        {
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameOut"
                    ]
                )
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1beta2_TextFrameIn"] = t.struct(
        {
            "rotatedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPolyIn"]
            ).optional(),
            "timeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_TextFrameIn"])
    types["GoogleCloudVideointelligenceV1beta2_TextFrameOut"] = t.struct(
        {
            "rotatedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPolyOut"]
            ).optional(),
            "timeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_TextFrameOut"])
    types[
        "GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotationIn"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_TrackIn"])
            ).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotationIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotationOut"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_TrackOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotationOut"]
    )
    types[
        "GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResultsIn"
    ] = t.struct(
        {
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationIn"
                ]
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationIn"
                    ]
                )
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "shotAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"])
            ).optional(),
            "frameTimestamp": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResultsIn"
        ]
    )
    types[
        "GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResultsOut"
    ] = t.struct(
        {
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationOut"
                ]
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationOut"
                    ]
                )
            ).optional(),
            "labelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "shotAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"]
                )
            ).optional(),
            "frameTimestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResultsOut"
        ]
    )
    types["GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkIn"] = t.struct(
        {
            "point": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexIn"]
            ).optional(),
            "name": t.string().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkOut"] = t.struct(
        {
            "point": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexOut"]
            ).optional(),
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkIn"] = t.struct(
        {
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "point": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_NormalizedVertexIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkOut"] = t.struct(
        {
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "point": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_NormalizedVertexOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkOut"])
    types["GoogleCloudVideointelligenceV1beta2_LabelSegmentIn"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"]
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_LabelSegmentIn"])
    types["GoogleCloudVideointelligenceV1beta2_LabelSegmentOut"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_LabelSegmentOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationIn"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_FaceFrameIn"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_FaceSegmentIn"])
            ).optional(),
            "thumbnail": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationOut"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_FaceFrameOut"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_FaceSegmentOut"])
            ).optional(),
            "thumbnail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationOut"])
    types["GoogleCloudVideointelligenceV1beta2_DetectedLandmarkIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "point": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_NormalizedVertexIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_DetectedLandmarkIn"])
    types["GoogleCloudVideointelligenceV1beta2_DetectedLandmarkOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "point": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_NormalizedVertexOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_DetectedLandmarkOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResultsIn"] = t.struct(
        {
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotationIn"
                    ]
                )
            ).optional(),
            "celebrityRecognitionAnnotations": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotationIn"
                ]
            ).optional(),
            "frameLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationIn"
                    ]
                )
            ).optional(),
            "segmentLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationIn"]
                )
            ).optional(),
            "personDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationIn"
                    ]
                )
            ).optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotationIn"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["GoogleRpc_StatusIn"]).optional(),
            "inputUri": t.string().optional(),
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "shotAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"])
            ).optional(),
            "shotLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"]
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_TextAnnotationIn"]
                )
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationIn"
                ]
            ).optional(),
            "speechTranscriptions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionIn"
                    ]
                )
            ).optional(),
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResultsIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResultsOut"] = t.struct(
        {
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotationOut"
                    ]
                )
            ).optional(),
            "celebrityRecognitionAnnotations": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotationOut"
                ]
            ).optional(),
            "frameLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationOut"
                    ]
                )
            ).optional(),
            "segmentLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationOut"]
                )
            ).optional(),
            "personDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationOut"
                    ]
                )
            ).optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotationOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "inputUri": t.string().optional(),
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "shotAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"]
                )
            ).optional(),
            "shotLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"]
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_TextAnnotationOut"]
                )
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationOut"
                ]
            ).optional(),
            "speechTranscriptions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionOut"
                    ]
                )
            ).optional(),
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResultsOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationIn"] = t.struct(
        {
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_LabelSegmentIn"])
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_LabelFrameIn"])
            ).optional(),
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_EntityIn"])
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_EntityIn"]
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationOut"] = t.struct(
        {
            "segments": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelSegmentOut"]
                )
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_LabelFrameOut"])
            ).optional(),
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_EntityOut"])
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_EntityOut"]
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrityIn"] = t.struct(
        {
            "celebrity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_CelebrityIn"]
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrityIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrityOut"] = t.struct(
        {
            "celebrity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_CelebrityOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrityOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "endTimeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "endTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"])
    types["GoogleCloudVideointelligenceV1_AnnotateVideoResponseIn"] = t.struct(
        {
            "annotationResults": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_VideoAnnotationResultsIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1_AnnotateVideoResponseIn"])
    types["GoogleCloudVideointelligenceV1_AnnotateVideoResponseOut"] = t.struct(
        {
            "annotationResults": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_VideoAnnotationResultsOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_AnnotateVideoResponseOut"])
    types[
        "GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotationIn"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "celebrityTracks": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackIn"]
                )
            ).optional(),
        }
    ).named(
        renames[
            "GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotationIn"
        ]
    )
    types[
        "GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotationOut"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "celebrityTracks": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotationOut"
        ]
    )
    types["GoogleCloudVideointelligenceV1_ExplicitContentAnnotationIn"] = t.struct(
        {
            "frames": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_ExplicitContentFrameIn"]
                )
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_ExplicitContentAnnotationIn"])
    types["GoogleCloudVideointelligenceV1_ExplicitContentAnnotationOut"] = t.struct(
        {
            "frames": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_ExplicitContentFrameOut"]
                )
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_ExplicitContentAnnotationOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_EntityIn"] = t.struct(
        {
            "entityId": t.string().optional(),
            "description": t.string().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_EntityIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_EntityOut"] = t.struct(
        {
            "entityId": t.string().optional(),
            "description": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_EntityOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_TextAnnotationIn"] = t.struct(
        {
            "text": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TextSegmentIn"])
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_TextAnnotationIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_TextAnnotationOut"] = t.struct(
        {
            "text": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TextSegmentOut"])
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_TextAnnotationOut"])
    types["GoogleCloudVideointelligenceV1_EntityIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "entityId": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_EntityIn"])
    types["GoogleCloudVideointelligenceV1_EntityOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "entityId": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_EntityOut"])
    types[
        "GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotationIn"
    ] = t.struct(
        {
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"])
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_EntityIn"]
            ).optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_TrackIn"])
            ).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotationIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotationOut"
    ] = t.struct(
        {
            "segments": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"]
                )
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_EntityOut"]
            ).optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_TrackOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotationOut"]
    )
    types[
        "GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotationIn"
    ] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"]
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_EntityIn"]
            ).optional(),
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrameIn"
                    ]
                )
            ).optional(),
            "version": t.string().optional(),
            "confidence": t.number().optional(),
            "trackId": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotationIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotationOut"
    ] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"]
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_EntityOut"]
            ).optional(),
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrameOut"
                    ]
                )
            ).optional(),
            "version": t.string().optional(),
            "confidence": t.number().optional(),
            "trackId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1p1beta1_TrackIn"] = t.struct(
        {
            "attributes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeIn"]
                )
            ).optional(),
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"]
            ).optional(),
            "timestampedObjects": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_TimestampedObjectIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_TrackIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_TrackOut"] = t.struct(
        {
            "attributes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeOut"
                    ]
                )
            ).optional(),
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"]
            ).optional(),
            "timestampedObjects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_TimestampedObjectOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_TrackOut"])
    types["GoogleCloudVideointelligenceV1_FaceAnnotationIn"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_FaceFrameIn"])
            ).optional(),
            "thumbnail": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_FaceSegmentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_FaceAnnotationIn"])
    types["GoogleCloudVideointelligenceV1_FaceAnnotationOut"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_FaceFrameOut"])
            ).optional(),
            "thumbnail": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_FaceSegmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_FaceAnnotationOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_WordInfoIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "word": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_WordInfoIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_WordInfoOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "startTime": t.string().optional(),
            "word": t.string().optional(),
            "endTime": t.string().optional(),
            "speakerTag": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_WordInfoOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResultsIn"] = t.struct(
        {
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotationIn"
                    ]
                )
            ).optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotationIn"
                    ]
                )
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_TextAnnotationIn"]
                )
            ).optional(),
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationIn"
                    ]
                )
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationIn"]
                )
            ).optional(),
            "frameLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "personDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationIn"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["GoogleRpc_StatusIn"]).optional(),
            "shotLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "speechTranscriptions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionIn"
                    ]
                )
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotationIn"
                ]
            ).optional(),
            "inputUri": t.string().optional(),
            "segmentLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "shotAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"])
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResultsIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResultsOut"] = t.struct(
        {
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotationOut"
                    ]
                )
            ).optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotationOut"
                    ]
                )
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_TextAnnotationOut"]
                )
            ).optional(),
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationOut"
                    ]
                )
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationOut"]
                )
            ).optional(),
            "frameLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "personDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "shotLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "speechTranscriptions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionOut"
                    ]
                )
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotationOut"
                ]
            ).optional(),
            "inputUri": t.string().optional(),
            "segmentLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "shotAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResultsOut"])
    types["GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1_EntityIn"]
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_ObjectTrackingFrameIn"])
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentIn"]
            ).optional(),
            "version": t.string().optional(),
            "trackId": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationIn"])
    types["GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1_EntityOut"]
            ).optional(),
            "frames": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_ObjectTrackingFrameOut"]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentOut"]
            ).optional(),
            "version": t.string().optional(),
            "trackId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationOut"])
    types["GoogleCloudVideointelligenceV1beta2_LabelAnnotationIn"] = t.struct(
        {
            "version": t.string().optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_EntityIn"]
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_LabelFrameIn"])
            ).optional(),
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_EntityIn"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_LabelSegmentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationIn"])
    types["GoogleCloudVideointelligenceV1beta2_LabelAnnotationOut"] = t.struct(
        {
            "version": t.string().optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_EntityOut"]
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_LabelFrameOut"])
            ).optional(),
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_EntityOut"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_LabelSegmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponseIn"] = t.struct(
        {
            "annotationResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResultsIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponseIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponseOut"] = t.struct(
        {
            "annotationResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResultsOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponseOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_TextSegmentIn"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TextFrameIn"])
            ).optional(),
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_TextSegmentIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_TextSegmentOut"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TextFrameOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_TextSegmentOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrameIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "pornographyLikelihood": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrameIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "pornographyLikelihood": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrameOut"])
    types["GoogleCloudVideointelligenceV1_LabelAnnotationIn"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelFrameIn"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelSegmentIn"])
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1_EntityIn"]
            ).optional(),
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_EntityIn"])
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_LabelAnnotationIn"])
    types["GoogleCloudVideointelligenceV1_LabelAnnotationOut"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelFrameOut"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelSegmentOut"])
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1_EntityOut"]
            ).optional(),
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_EntityOut"])
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_LabelAnnotationOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPolyIn"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_NormalizedVertexIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPolyIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPolyOut"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_NormalizedVertexOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPolyOut"])
    types[
        "GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponseIn"
    ] = t.struct(
        {
            "annotationResultsUri": t.string().optional(),
            "error": t.proxy(renames["GoogleRpc_StatusIn"]).optional(),
            "annotationResults": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResultsIn"
                ]
            ).optional(),
        }
    ).named(
        renames[
            "GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponseIn"
        ]
    )
    types[
        "GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponseOut"
    ] = t.struct(
        {
            "annotationResultsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "annotationResults": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResultsOut"
                ]
            ).optional(),
        }
    ).named(
        renames[
            "GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponseOut"
        ]
    )
    types["GoogleCloudVideointelligenceV1p3beta1_TextSegmentIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"]
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_TextFrameIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_TextSegmentIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_TextSegmentOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"]
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_TextFrameOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_TextSegmentOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_TextFrameIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "rotatedBoundingBox": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPolyIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_TextFrameIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_TextFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "rotatedBoundingBox": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPolyOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_TextFrameOut"])
    types["GoogleCloudVideointelligenceV1_SpeechContextIn"] = t.struct(
        {"phrases": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudVideointelligenceV1_SpeechContextIn"])
    types["GoogleCloudVideointelligenceV1_SpeechContextOut"] = t.struct(
        {
            "phrases": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_SpeechContextOut"])
    types["GoogleCloudVideointelligenceV1_LabelFrameIn"] = t.struct(
        {"timeOffset": t.string().optional(), "confidence": t.number().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1_LabelFrameIn"])
    types["GoogleCloudVideointelligenceV1_LabelFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_LabelFrameOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotationIn"] = t.struct(
        {
            "version": t.string().optional(),
            "thumbnail": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_TrackIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotationIn"])
    types[
        "GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotationOut"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "thumbnail": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_TrackOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackIn"] = t.struct(
        {
            "faceTrack": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_TrackIn"]
            ).optional(),
            "celebrities": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrityIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackOut"] = t.struct(
        {
            "faceTrack": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_TrackOut"]
            ).optional(),
            "celebrities": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrityOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackOut"])
    types["GoogleCloudVideointelligenceV1_TextAnnotationIn"] = t.struct(
        {
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TextSegmentIn"])
            ).optional(),
            "version": t.string().optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TextAnnotationIn"])
    types["GoogleCloudVideointelligenceV1_TextAnnotationOut"] = t.struct(
        {
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TextSegmentOut"])
            ).optional(),
            "version": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TextAnnotationOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPolyIn"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_NormalizedVertexIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPolyIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPolyOut"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_NormalizedVertexOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPolyOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_FaceFrameIn"] = t.struct(
        {
            "normalizedBoundingBoxes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxIn"
                    ]
                )
            ).optional(),
            "timeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_FaceFrameIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_FaceFrameOut"] = t.struct(
        {
            "normalizedBoundingBoxes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxOut"
                    ]
                )
            ).optional(),
            "timeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_FaceFrameOut"])
    types["GoogleLongrunning_ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunning_OperationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleLongrunning_ListOperationsResponseIn"])
    types["GoogleLongrunning_ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunning_OperationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunning_ListOperationsResponseOut"])
    types["GoogleLongrunning_CancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunning_CancelOperationRequestIn"])
    types["GoogleLongrunning_CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunning_CancelOperationRequestOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeOut"])
    types[
        "GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternativeIn"
    ] = t.struct({"transcript": t.string().optional()}).named(
        renames["GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternativeIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternativeOut"
    ] = t.struct(
        {
            "words": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_WordInfoOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "transcript": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternativeOut"]
    )
    types["GoogleCloudVideointelligenceV1beta2_TimestampedObjectIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "attributes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_DetectedAttributeIn"]
                )
            ).optional(),
            "landmarks": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_DetectedLandmarkIn"]
                )
            ).optional(),
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_TimestampedObjectIn"])
    types["GoogleCloudVideointelligenceV1beta2_TimestampedObjectOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "attributes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_DetectedAttributeOut"]
                )
            ).optional(),
            "landmarks": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_DetectedLandmarkOut"]
                )
            ).optional(),
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_TimestampedObjectOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponseIn"] = t.struct(
        {
            "annotationResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResultsIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponseIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponseOut"] = t.struct(
        {
            "annotationResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResultsOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponseOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgressIn"] = t.struct(
        {
            "annotationProgress": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgressIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgressIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgressOut"] = t.struct(
        {
            "annotationProgress": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgressOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgressOut"])
    types[
        "GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationIn"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_TrackIn"])
            ).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationOut"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_TrackOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxIn"] = t.struct(
        {
            "right": t.number().optional(),
            "bottom": t.number().optional(),
            "top": t.number().optional(),
            "left": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxIn"])
    types["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxOut"] = t.struct(
        {
            "right": t.number().optional(),
            "bottom": t.number().optional(),
            "top": t.number().optional(),
            "left": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxOut"])
    types["GoogleCloudVideointelligenceV1_WordInfoIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "word": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_WordInfoIn"])
    types["GoogleCloudVideointelligenceV1_WordInfoOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "word": t.string().optional(),
            "speakerTag": t.integer().optional(),
            "endTime": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_WordInfoOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionIn"] = t.struct(
        {
            "alternatives": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionOut"] = t.struct(
        {
            "alternatives": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeOut"
                    ]
                )
            ).optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionOut"])
    types["GoogleCloudVideointelligenceV1_VideoAnnotationProgressIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentIn"]
            ).optional(),
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "inputUri": t.string().optional(),
            "feature": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_VideoAnnotationProgressIn"])
    types["GoogleCloudVideointelligenceV1_VideoAnnotationProgressOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "inputUri": t.string().optional(),
            "feature": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_VideoAnnotationProgressOut"])
    types[
        "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationIn"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrameIn"
                    ]
                )
            ).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationOut"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrameOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationOut"]
    )
    types[
        "GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationIn"
    ] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"]
            ).optional(),
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrameIn"
                    ]
                )
            ).optional(),
            "version": t.string().optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_EntityIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "trackId": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationOut"
    ] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"]
            ).optional(),
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrameOut"
                    ]
                )
            ).optional(),
            "version": t.string().optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_EntityOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "trackId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1beta2_LabelFrameIn"] = t.struct(
        {"timeOffset": t.string().optional(), "confidence": t.number().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1beta2_LabelFrameIn"])
    types["GoogleCloudVideointelligenceV1beta2_LabelFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_LabelFrameOut"])
    types["GoogleProtobuf_EmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobuf_EmptyIn"]
    )
    types["GoogleProtobuf_EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobuf_EmptyOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgressIn"] = t.struct(
        {
            "inputUri": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "feature": t.string().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"]
            ).optional(),
            "startTime": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgressIn"])
    types[
        "GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgressOut"
    ] = t.struct(
        {
            "inputUri": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "feature": t.string().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgressOut"]
    )
    types["GoogleCloudVideointelligenceV1beta2_TextAnnotationIn"] = t.struct(
        {
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TextSegmentIn"])
            ).optional(),
            "version": t.string().optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_TextAnnotationIn"])
    types["GoogleCloudVideointelligenceV1beta2_TextAnnotationOut"] = t.struct(
        {
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TextSegmentOut"])
            ).optional(),
            "version": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_TextAnnotationOut"])
    types["GoogleCloudVideointelligenceV1beta2_NormalizedVertexIn"] = t.struct(
        {"y": t.number().optional(), "x": t.number().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1beta2_NormalizedVertexIn"])
    types["GoogleCloudVideointelligenceV1beta2_NormalizedVertexOut"] = t.struct(
        {
            "y": t.number().optional(),
            "x": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_NormalizedVertexOut"])
    types["GoogleCloudVideointelligenceV1beta2_VideoAnnotationResultsIn"] = t.struct(
        {
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationIn"]
                )
            ).optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationIn"
                    ]
                )
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationIn"
                    ]
                )
            ).optional(),
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotationIn"
                    ]
                )
            ).optional(),
            "frameLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationIn"]
                )
            ).optional(),
            "error": t.proxy(renames["GoogleRpc_StatusIn"]).optional(),
            "shotAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TextAnnotationIn"])
            ).optional(),
            "inputUri": t.string().optional(),
            "segmentLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationIn"]
                )
            ).optional(),
            "speechTranscriptions": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionIn"]
                )
            ).optional(),
            "shotLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationIn"]
                )
            ).optional(),
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationIn"]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"]
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotationIn"
                ]
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_FaceAnnotationIn"])
            ).optional(),
            "personDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotationIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_VideoAnnotationResultsIn"])
    types["GoogleCloudVideointelligenceV1beta2_VideoAnnotationResultsOut"] = t.struct(
        {
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationOut"]
                )
            ).optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationOut"
                    ]
                )
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationOut"
                    ]
                )
            ).optional(),
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotationOut"
                    ]
                )
            ).optional(),
            "frameLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "shotAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_TextAnnotationOut"]
                )
            ).optional(),
            "inputUri": t.string().optional(),
            "segmentLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationOut"]
                )
            ).optional(),
            "speechTranscriptions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionOut"
                    ]
                )
            ).optional(),
            "shotLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationOut"]
                )
            ).optional(),
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationOut"]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"]
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotationOut"
                ]
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_FaceAnnotationOut"]
                )
            ).optional(),
            "personDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotationOut"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_VideoAnnotationResultsOut"])
    types[
        "GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotationIn"
    ] = t.struct(
        {
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrameIn"
                    ]
                )
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotationIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotationOut"
    ] = t.struct(
        {
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrameOut"
                    ]
                )
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrameIn"] = t.struct(
        {
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxIn"]
            ).optional(),
            "timeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrameIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrameOut"] = t.struct(
        {
            "normalizedBoundingBox": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxOut"
                ]
            ).optional(),
            "timeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrameOut"])
    types["GoogleCloudVideointelligenceV1_NormalizedBoundingBoxIn"] = t.struct(
        {
            "right": t.number().optional(),
            "top": t.number().optional(),
            "left": t.number().optional(),
            "bottom": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_NormalizedBoundingBoxIn"])
    types["GoogleCloudVideointelligenceV1_NormalizedBoundingBoxOut"] = t.struct(
        {
            "right": t.number().optional(),
            "top": t.number().optional(),
            "left": t.number().optional(),
            "bottom": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_NormalizedBoundingBoxOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrameIn"] = t.struct(
        {
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxIn"]
            ).optional(),
            "timeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrameIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrameOut"] = t.struct(
        {
            "normalizedBoundingBox": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxOut"
                ]
            ).optional(),
            "timeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrameOut"])
    types[
        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationIn"
    ] = t.struct(
        {
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrameIn"
                    ]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"]
            ).optional(),
            "version": t.string().optional(),
            "trackId": t.string().optional(),
            "confidence": t.number().optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_EntityIn"]
            ).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationOut"
    ] = t.struct(
        {
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrameOut"
                    ]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"]
            ).optional(),
            "version": t.string().optional(),
            "trackId": t.string().optional(),
            "confidence": t.number().optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_EntityOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponseIn"] = t.struct(
        {
            "annotationResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResultsIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponseIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponseOut"] = t.struct(
        {
            "annotationResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResultsOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponseOut"])
    types["GoogleCloudVideointelligenceV1_AnnotateVideoRequestIn"] = t.struct(
        {
            "features": t.array(t.string()),
            "outputUri": t.string().optional(),
            "locationId": t.string().optional(),
            "inputUri": t.string().optional(),
            "inputContent": t.string().optional(),
            "videoContext": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoContextIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_AnnotateVideoRequestIn"])
    types["GoogleCloudVideointelligenceV1_AnnotateVideoRequestOut"] = t.struct(
        {
            "features": t.array(t.string()),
            "outputUri": t.string().optional(),
            "locationId": t.string().optional(),
            "inputUri": t.string().optional(),
            "inputContent": t.string().optional(),
            "videoContext": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoContextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_AnnotateVideoRequestOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_TrackIn"] = t.struct(
        {
            "attributes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeIn"]
                )
            ).optional(),
            "confidence": t.number().optional(),
            "timestampedObjects": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_TimestampedObjectIn"]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TrackIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_TrackOut"] = t.struct(
        {
            "attributes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeOut"
                    ]
                )
            ).optional(),
            "confidence": t.number().optional(),
            "timestampedObjects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_TimestampedObjectOut"
                    ]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TrackOut"])
    types["GoogleCloudVideointelligenceV1beta2_TrackIn"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"]
            ).optional(),
            "timestampedObjects": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_TimestampedObjectIn"]
                )
            ).optional(),
            "attributes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_DetectedAttributeIn"]
                )
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_TrackIn"])
    types["GoogleCloudVideointelligenceV1beta2_TrackOut"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"]
            ).optional(),
            "timestampedObjects": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_TimestampedObjectOut"]
                )
            ).optional(),
            "attributes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_DetectedAttributeOut"]
                )
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_TrackOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_LabelFrameIn"] = t.struct(
        {"timeOffset": t.string().optional(), "confidence": t.number().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_LabelFrameIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_LabelFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_LabelFrameOut"])
    types["GoogleCloudVideointelligenceV1_PersonDetectionAnnotationIn"] = t.struct(
        {
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TrackIn"])
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_PersonDetectionAnnotationIn"])
    types["GoogleCloudVideointelligenceV1_PersonDetectionAnnotationOut"] = t.struct(
        {
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TrackOut"])
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_PersonDetectionAnnotationOut"])
    types["GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameIn"] = t.struct(
        {
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxIn"]
            ).optional(),
            "timeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameIn"])
    types["GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameOut"] = t.struct(
        {
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxOut"]
            ).optional(),
            "timeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameOut"])
    types["GoogleCloudVideointelligenceV1_PersonDetectionConfigIn"] = t.struct(
        {
            "includeAttributes": t.boolean().optional(),
            "includePoseLandmarks": t.boolean().optional(),
            "includeBoundingBoxes": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_PersonDetectionConfigIn"])
    types["GoogleCloudVideointelligenceV1_PersonDetectionConfigOut"] = t.struct(
        {
            "includeAttributes": t.boolean().optional(),
            "includePoseLandmarks": t.boolean().optional(),
            "includeBoundingBoxes": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_PersonDetectionConfigOut"])
    types[
        "GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternativeIn"
    ] = t.struct({"transcript": t.string().optional()}).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternativeIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternativeOut"
    ] = t.struct(
        {
            "transcript": t.string().optional(),
            "confidence": t.number().optional(),
            "words": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_WordInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternativeOut"]
    )
    types["GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgressIn"] = t.struct(
        {
            "inputUri": t.string().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"]
            ).optional(),
            "startTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "feature": t.string().optional(),
            "progressPercent": t.integer().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgressIn"])
    types[
        "GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgressOut"
    ] = t.struct(
        {
            "inputUri": t.string().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "feature": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgressOut"]
    )
    types["GoogleCloudVideointelligenceV1p2beta1_FaceSegmentIn"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_FaceSegmentIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_FaceSegmentOut"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_FaceSegmentOut"])
    types["GoogleCloudVideointelligenceV1beta2_FaceAnnotationIn"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_FaceFrameIn"])
            ).optional(),
            "thumbnail": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_FaceSegmentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_FaceAnnotationIn"])
    types["GoogleCloudVideointelligenceV1beta2_FaceAnnotationOut"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_FaceFrameOut"])
            ).optional(),
            "thumbnail": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_FaceSegmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_FaceAnnotationOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_LabelFrameIn"] = t.struct(
        {"confidence": t.number().optional(), "timeOffset": t.string().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_LabelFrameIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_LabelFrameOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "timeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_LabelFrameOut"])
    types["GoogleCloudVideointelligenceV1_TextSegmentIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentIn"]
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TextFrameIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TextSegmentIn"])
    types["GoogleCloudVideointelligenceV1_TextSegmentOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentOut"]
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TextFrameOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TextSegmentOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResultsIn"] = t.struct(
        {
            "faceAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationIn"]
                )
            ).optional(),
            "shotAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"])
            ).optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationIn"
                    ]
                )
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_TextAnnotationIn"]
                )
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationIn"
                ]
            ).optional(),
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "speechTranscriptions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_SpeechTranscriptionIn"
                    ]
                )
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationIn"
                    ]
                )
            ).optional(),
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "frameLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "inputUri": t.string().optional(),
            "shotLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationIn"
                    ]
                )
            ).optional(),
            "segmentLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"]
            ).optional(),
            "error": t.proxy(renames["GoogleRpc_StatusIn"]).optional(),
            "personDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotationIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResultsIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResultsOut"] = t.struct(
        {
            "faceAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationOut"]
                )
            ).optional(),
            "shotAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"]
                )
            ).optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationOut"
                    ]
                )
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_TextAnnotationOut"]
                )
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationOut"
                ]
            ).optional(),
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "speechTranscriptions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_SpeechTranscriptionOut"
                    ]
                )
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationOut"
                    ]
                )
            ).optional(),
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "frameLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "inputUri": t.string().optional(),
            "shotLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationOut"
                    ]
                )
            ).optional(),
            "segmentLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "personDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotationOut"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResultsOut"])
    types["GoogleCloudVideointelligenceV1_LogoRecognitionAnnotationIn"] = t.struct(
        {
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1_EntityIn"]
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_VideoSegmentIn"])
            ).optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TrackIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_LogoRecognitionAnnotationIn"])
    types["GoogleCloudVideointelligenceV1_LogoRecognitionAnnotationOut"] = t.struct(
        {
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1_EntityOut"]
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_VideoSegmentOut"])
            ).optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TrackOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_LogoRecognitionAnnotationOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_EntityIn"] = t.struct(
        {
            "description": t.string().optional(),
            "languageCode": t.string().optional(),
            "entityId": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_EntityIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_EntityOut"] = t.struct(
        {
            "description": t.string().optional(),
            "languageCode": t.string().optional(),
            "entityId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_EntityOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgressIn"] = t.struct(
        {
            "annotationProgress": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgressIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgressIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgressOut"] = t.struct(
        {
            "annotationProgress": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgressOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgressOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_TimestampedObjectIn"] = t.struct(
        {
            "landmarks": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkIn"]
                )
            ).optional(),
            "timeOffset": t.string().optional(),
            "attributes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeIn"]
                )
            ).optional(),
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_TimestampedObjectIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_TimestampedObjectOut"] = t.struct(
        {
            "landmarks": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkOut"]
                )
            ).optional(),
            "timeOffset": t.string().optional(),
            "attributes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeOut"
                    ]
                )
            ).optional(),
            "normalizedBoundingBox": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_TimestampedObjectOut"])
    types["GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigIn"] = t.struct(
        {
            "enableSpeakerDiarization": t.boolean().optional(),
            "languageCode": t.string(),
            "speechContexts": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_SpeechContextIn"])
            ).optional(),
            "audioTracks": t.array(t.integer()).optional(),
            "maxAlternatives": t.integer().optional(),
            "filterProfanity": t.boolean().optional(),
            "enableWordConfidence": t.boolean().optional(),
            "enableAutomaticPunctuation": t.boolean().optional(),
            "diarizationSpeakerCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigIn"])
    types["GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigOut"] = t.struct(
        {
            "enableSpeakerDiarization": t.boolean().optional(),
            "languageCode": t.string(),
            "speechContexts": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_SpeechContextOut"])
            ).optional(),
            "audioTracks": t.array(t.integer()).optional(),
            "maxAlternatives": t.integer().optional(),
            "filterProfanity": t.boolean().optional(),
            "enableWordConfidence": t.boolean().optional(),
            "enableAutomaticPunctuation": t.boolean().optional(),
            "diarizationSpeakerCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigOut"])
    types[
        "GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeIn"
    ] = t.struct({"transcript": t.string().optional()}).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeOut"
    ] = t.struct(
        {
            "transcript": t.string().optional(),
            "words": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_WordInfoOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeOut"]
    )
    types["GoogleCloudVideointelligenceV1_FaceSegmentIn"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1_FaceSegmentIn"])
    types["GoogleCloudVideointelligenceV1_FaceSegmentOut"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_FaceSegmentOut"])
    types["GoogleCloudVideointelligenceV1beta2_DetectedAttributeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_DetectedAttributeIn"])
    types["GoogleCloudVideointelligenceV1beta2_DetectedAttributeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_DetectedAttributeOut"])
    types["GoogleCloudVideointelligenceV1_VideoAnnotationResultsIn"] = t.struct(
        {
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationIn"])
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationIn"]
                )
            ).optional(),
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_FaceDetectionAnnotationIn"]
                )
            ).optional(),
            "speechTranscriptions": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_SpeechTranscriptionIn"])
            ).optional(),
            "personDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1_PersonDetectionAnnotationIn"
                    ]
                )
            ).optional(),
            "shotLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationIn"])
            ).optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1_LogoRecognitionAnnotationIn"
                    ]
                )
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TextAnnotationIn"])
            ).optional(),
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationIn"])
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames["GoogleCloudVideointelligenceV1_ExplicitContentAnnotationIn"]
            ).optional(),
            "segmentLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationIn"])
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_FaceAnnotationIn"])
            ).optional(),
            "error": t.proxy(renames["GoogleRpc_StatusIn"]).optional(),
            "inputUri": t.string().optional(),
            "frameLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationIn"])
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentIn"]
            ).optional(),
            "shotAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_VideoSegmentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_VideoAnnotationResultsIn"])
    types["GoogleCloudVideointelligenceV1_VideoAnnotationResultsOut"] = t.struct(
        {
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationOut"])
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationOut"
                    ]
                )
            ).optional(),
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_FaceDetectionAnnotationOut"]
                )
            ).optional(),
            "speechTranscriptions": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_SpeechTranscriptionOut"]
                )
            ).optional(),
            "personDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1_PersonDetectionAnnotationOut"
                    ]
                )
            ).optional(),
            "shotLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationOut"])
            ).optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1_LogoRecognitionAnnotationOut"
                    ]
                )
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TextAnnotationOut"])
            ).optional(),
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationOut"])
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames["GoogleCloudVideointelligenceV1_ExplicitContentAnnotationOut"]
            ).optional(),
            "segmentLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationOut"])
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_FaceAnnotationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "inputUri": t.string().optional(),
            "frameLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationOut"])
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentOut"]
            ).optional(),
            "shotAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_VideoSegmentOut"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_VideoAnnotationResultsOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationIn"] = t.struct(
        {
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_EntityIn"]
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_LabelFrameIn"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_LabelSegmentIn"])
            ).optional(),
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_EntityIn"])
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationOut"] = t.struct(
        {
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_EntityOut"]
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_LabelFrameOut"])
            ).optional(),
            "segments": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelSegmentOut"]
                )
            ).optional(),
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_EntityOut"])
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationOut"])
    types["GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigIn"] = t.struct(
        {"model": t.string().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigIn"])
    types["GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigOut"] = t.struct(
        {
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_FaceFrameIn"] = t.struct(
        {
            "normalizedBoundingBoxes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxIn"
                    ]
                )
            ).optional(),
            "timeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_FaceFrameIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_FaceFrameOut"] = t.struct(
        {
            "normalizedBoundingBoxes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxOut"
                    ]
                )
            ).optional(),
            "timeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_FaceFrameOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_TextAnnotationIn"] = t.struct(
        {
            "text": t.string().optional(),
            "version": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_TextSegmentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TextAnnotationIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_TextAnnotationOut"] = t.struct(
        {
            "text": t.string().optional(),
            "version": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_TextSegmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TextAnnotationOut"])
    types["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPolyIn"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_NormalizedVertexIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPolyIn"])
    types["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPolyOut"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_NormalizedVertexOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPolyOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrameIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrameIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "normalizedBoundingBox": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrameOut"])
    types["GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgressIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "inputUri": t.string().optional(),
            "feature": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgressIn"])
    types["GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgressOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "inputUri": t.string().optional(),
            "feature": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgressOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn"] = t.struct(
        {
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_EntityIn"]
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_LabelFrameIn"])
            ).optional(),
            "version": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_LabelSegmentIn"])
            ).optional(),
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_EntityIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut"] = t.struct(
        {
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_EntityOut"]
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_LabelFrameOut"])
            ).optional(),
            "version": t.string().optional(),
            "segments": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelSegmentOut"]
                )
            ).optional(),
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_EntityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationIn"] = t.struct(
        {
            "thumbnail": t.string().optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_FaceFrameIn"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_FaceSegmentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationOut"] = t.struct(
        {
            "thumbnail": t.string().optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_FaceFrameOut"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_FaceSegmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrameIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "pornographyLikelihood": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrameIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "pornographyLikelihood": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrameOut"])
    types["GoogleCloudVideointelligenceV1_FaceDetectionConfigIn"] = t.struct(
        {
            "includeBoundingBoxes": t.boolean().optional(),
            "includeAttributes": t.boolean().optional(),
            "model": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_FaceDetectionConfigIn"])
    types["GoogleCloudVideointelligenceV1_FaceDetectionConfigOut"] = t.struct(
        {
            "includeBoundingBoxes": t.boolean().optional(),
            "includeAttributes": t.boolean().optional(),
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_FaceDetectionConfigOut"])
    types["GoogleCloudVideointelligenceV1_ExplicitContentDetectionConfigIn"] = t.struct(
        {"model": t.string().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1_ExplicitContentDetectionConfigIn"])
    types[
        "GoogleCloudVideointelligenceV1_ExplicitContentDetectionConfigOut"
    ] = t.struct(
        {
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1_ExplicitContentDetectionConfigOut"]
    )
    types["GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxIn"] = t.struct(
        {
            "bottom": t.number().optional(),
            "right": t.number().optional(),
            "top": t.number().optional(),
            "left": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxOut"] = t.struct(
        {
            "bottom": t.number().optional(),
            "right": t.number().optional(),
            "top": t.number().optional(),
            "left": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxOut"])
    types["GoogleLongrunning_OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["GoogleRpc_StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunning_OperationIn"])
    types["GoogleLongrunning_OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunning_OperationOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_TimestampedObjectIn"] = t.struct(
        {
            "attributes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeIn"]
                )
            ).optional(),
            "timeOffset": t.string().optional(),
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxIn"]
            ).optional(),
            "landmarks": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_TimestampedObjectIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_TimestampedObjectOut"] = t.struct(
        {
            "attributes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeOut"
                    ]
                )
            ).optional(),
            "timeOffset": t.string().optional(),
            "normalizedBoundingBox": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxOut"
                ]
            ).optional(),
            "landmarks": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_TimestampedObjectOut"])
    types["GoogleRpc_StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleRpc_StatusIn"])
    types["GoogleRpc_StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpc_StatusOut"])
    types["GoogleCloudVideointelligenceV1_FaceDetectionAnnotationIn"] = t.struct(
        {
            "thumbnail": t.string().optional(),
            "version": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TrackIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_FaceDetectionAnnotationIn"])
    types["GoogleCloudVideointelligenceV1_FaceDetectionAnnotationOut"] = t.struct(
        {
            "thumbnail": t.string().optional(),
            "version": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TrackOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_FaceDetectionAnnotationOut"])
    types["GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationIn"] = t.struct(
        {
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_EntityIn"]
            ).optional(),
            "trackId": t.string().optional(),
            "frames": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameIn"]
                )
            ).optional(),
            "version": t.string().optional(),
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationIn"])
    types["GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationOut"] = t.struct(
        {
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_EntityOut"]
            ).optional(),
            "trackId": t.string().optional(),
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameOut"
                    ]
                )
            ).optional(),
            "version": t.string().optional(),
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_TextSegmentIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"]
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_TextFrameIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TextSegmentIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_TextSegmentOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"]
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_TextFrameOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TextSegmentOut"])
    types["GoogleCloudVideointelligenceV1_DetectedAttributeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_DetectedAttributeIn"])
    types["GoogleCloudVideointelligenceV1_DetectedAttributeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_DetectedAttributeOut"])
    types["GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotationIn"] = t.struct(
        {
            "thumbnail": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TrackIn"])
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotationIn"])
    types["GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotationOut"] = t.struct(
        {
            "thumbnail": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TrackOut"])
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotationOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_LabelSegmentIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_LabelSegmentIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_LabelSegmentOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_LabelSegmentOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_TextAnnotationIn"] = t.struct(
        {
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_TextSegmentIn"])
            ).optional(),
            "version": t.string().optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_TextAnnotationIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_TextAnnotationOut"] = t.struct(
        {
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_TextSegmentOut"])
            ).optional(),
            "version": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_TextAnnotationOut"])
    types[
        "GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationIn"
    ] = t.struct(
        {
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_EntityIn"]
            ).optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_TrackIn"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"])
            ).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationOut"
    ] = t.struct(
        {
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_EntityOut"]
            ).optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_TrackOut"])
            ).optional(),
            "segments": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1p1beta1_LabelSegmentIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_LabelSegmentIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_LabelSegmentOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_LabelSegmentOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_FaceSegmentIn"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_FaceSegmentIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_FaceSegmentOut"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_FaceSegmentOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_NormalizedVertexIn"] = t.struct(
        {"x": t.number().optional(), "y": t.number().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_NormalizedVertexIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_NormalizedVertexOut"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_NormalizedVertexOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_WordInfoIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "word": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_WordInfoIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_WordInfoOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "endTime": t.string().optional(),
            "word": t.string().optional(),
            "startTime": t.string().optional(),
            "speakerTag": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_WordInfoOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "endTimeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "endTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_SpeechTranscriptionIn"] = t.struct(
        {
            "alternatives": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternativeIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_SpeechTranscriptionIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_SpeechTranscriptionOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "alternatives": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternativeOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_SpeechTranscriptionOut"])
    types["GoogleCloudVideointelligenceV1_VideoSegmentIn"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "endTimeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_VideoSegmentIn"])
    types["GoogleCloudVideointelligenceV1_VideoSegmentOut"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "endTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_VideoSegmentOut"])
    types["GoogleCloudVideointelligenceV1_ExplicitContentFrameIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "pornographyLikelihood": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_ExplicitContentFrameIn"])
    types["GoogleCloudVideointelligenceV1_ExplicitContentFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "pornographyLikelihood": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_ExplicitContentFrameOut"])
    types["GoogleCloudVideointelligenceV1_NormalizedBoundingPolyIn"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_NormalizedVertexIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1_NormalizedBoundingPolyIn"])
    types["GoogleCloudVideointelligenceV1_NormalizedBoundingPolyOut"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_NormalizedVertexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_NormalizedBoundingPolyOut"])
    types["GoogleCloudVideointelligenceV1_SpeechRecognitionAlternativeIn"] = t.struct(
        {"transcript": t.string().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1_SpeechRecognitionAlternativeIn"])
    types["GoogleCloudVideointelligenceV1_SpeechRecognitionAlternativeOut"] = t.struct(
        {
            "words": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_WordInfoOut"])
            ).optional(),
            "transcript": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_SpeechRecognitionAlternativeOut"])
    types["GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionIn"] = t.struct(
        {
            "alternatives": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternativeIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionIn"])
    types["GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "alternatives": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternativeOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationIn"] = t.struct(
        {
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_TrackIn"])
            ).optional(),
            "version": t.string().optional(),
            "thumbnail": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationIn"])
    types[
        "GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationOut"
    ] = t.struct(
        {
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_TrackOut"])
            ).optional(),
            "version": t.string().optional(),
            "thumbnail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPolyIn"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPolyIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPolyOut"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPolyOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_EntityIn"] = t.struct(
        {
            "description": t.string().optional(),
            "languageCode": t.string().optional(),
            "entityId": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_EntityIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_EntityOut"] = t.struct(
        {
            "description": t.string().optional(),
            "languageCode": t.string().optional(),
            "entityId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_EntityOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationIn"] = t.struct(
        {
            "thumbnail": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TrackIn"])
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationIn"])
    types[
        "GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationOut"
    ] = t.struct(
        {
            "thumbnail": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TrackOut"])
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1_SpeechTranscriptionIn"] = t.struct(
        {
            "alternatives": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1_SpeechRecognitionAlternativeIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1_SpeechTranscriptionIn"])
    types["GoogleCloudVideointelligenceV1_SpeechTranscriptionOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "alternatives": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1_SpeechRecognitionAlternativeOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_SpeechTranscriptionOut"])
    types["GoogleCloudVideointelligenceV1beta2_ExplicitContentFrameIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "pornographyLikelihood": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_ExplicitContentFrameIn"])
    types["GoogleCloudVideointelligenceV1beta2_ExplicitContentFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "pornographyLikelihood": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_ExplicitContentFrameOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkIn"] = t.struct(
        {
            "name": t.string().optional(),
            "point": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_NormalizedVertexIn"]
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkOut"] = t.struct(
        {
            "name": t.string().optional(),
            "point": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_NormalizedVertexOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkOut"])
    types[
        "GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotationIn"
    ] = t.struct(
        {
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_EntityIn"]
            ).optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TrackIn"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"])
            ).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotationIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotationOut"
    ] = t.struct(
        {
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_EntityOut"]
            ).optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TrackOut"])
            ).optional(),
            "segments": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponseIn"] = t.struct(
        {
            "annotationResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_VideoAnnotationResultsIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponseIn"])
    types["GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponseOut"] = t.struct(
        {
            "annotationResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_VideoAnnotationResultsOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponseOut"])
    types["GoogleCloudVideointelligenceV1_LabelDetectionConfigIn"] = t.struct(
        {
            "model": t.string().optional(),
            "stationaryCamera": t.boolean().optional(),
            "frameConfidenceThreshold": t.number().optional(),
            "labelDetectionMode": t.string().optional(),
            "videoConfidenceThreshold": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_LabelDetectionConfigIn"])
    types["GoogleCloudVideointelligenceV1_LabelDetectionConfigOut"] = t.struct(
        {
            "model": t.string().optional(),
            "stationaryCamera": t.boolean().optional(),
            "frameConfidenceThreshold": t.number().optional(),
            "labelDetectionMode": t.string().optional(),
            "videoConfidenceThreshold": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_LabelDetectionConfigOut"])
    types["GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationIn"] = t.struct(
        {
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"])
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_EntityIn"]
            ).optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TrackIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationIn"])
    types[
        "GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationOut"
    ] = t.struct(
        {
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"])
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_EntityOut"]
            ).optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TrackOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1_TextFrameIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "rotatedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1_NormalizedBoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TextFrameIn"])
    types["GoogleCloudVideointelligenceV1_TextFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "rotatedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1_NormalizedBoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TextFrameOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationIn"] = t.struct(
        {
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_FaceSegmentIn"])
            ).optional(),
            "thumbnail": t.string().optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_FaceFrameIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationOut"] = t.struct(
        {
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_FaceSegmentOut"])
            ).optional(),
            "thumbnail": t.string().optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_FaceFrameOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxIn"] = t.struct(
        {
            "left": t.number().optional(),
            "top": t.number().optional(),
            "right": t.number().optional(),
            "bottom": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxOut"] = t.struct(
        {
            "left": t.number().optional(),
            "top": t.number().optional(),
            "right": t.number().optional(),
            "bottom": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxOut"])
    types["GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgressIn"] = t.struct(
        {
            "annotationProgress": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgressIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgressIn"])
    types["GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgressOut"] = t.struct(
        {
            "annotationProgress": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgressOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgressOut"])
    types["GoogleCloudVideointelligenceV1_NormalizedVertexIn"] = t.struct(
        {"x": t.number().optional(), "y": t.number().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1_NormalizedVertexIn"])
    types["GoogleCloudVideointelligenceV1_NormalizedVertexOut"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_NormalizedVertexOut"])
    types["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"] = t.struct(
        {
            "endTimeOffset": t.string().optional(),
            "startTimeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"])
    types["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"] = t.struct(
        {
            "endTimeOffset": t.string().optional(),
            "startTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"])
    types["GoogleCloudVideointelligenceV1_ObjectTrackingConfigIn"] = t.struct(
        {"model": t.string().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1_ObjectTrackingConfigIn"])
    types["GoogleCloudVideointelligenceV1_ObjectTrackingConfigOut"] = t.struct(
        {
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_ObjectTrackingConfigOut"])
    types["GoogleCloudVideointelligenceV1_VideoContextIn"] = t.struct(
        {
            "labelDetectionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_LabelDetectionConfigIn"]
            ).optional(),
            "shotChangeDetectionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigIn"]
            ).optional(),
            "objectTrackingConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_ObjectTrackingConfigIn"]
            ).optional(),
            "personDetectionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_PersonDetectionConfigIn"]
            ).optional(),
            "explicitContentDetectionConfig": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1_ExplicitContentDetectionConfigIn"
                ]
            ).optional(),
            "faceDetectionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_FaceDetectionConfigIn"]
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_VideoSegmentIn"])
            ).optional(),
            "speechTranscriptionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigIn"]
            ).optional(),
            "textDetectionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_TextDetectionConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_VideoContextIn"])
    types["GoogleCloudVideointelligenceV1_VideoContextOut"] = t.struct(
        {
            "labelDetectionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_LabelDetectionConfigOut"]
            ).optional(),
            "shotChangeDetectionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigOut"]
            ).optional(),
            "objectTrackingConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_ObjectTrackingConfigOut"]
            ).optional(),
            "personDetectionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_PersonDetectionConfigOut"]
            ).optional(),
            "explicitContentDetectionConfig": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1_ExplicitContentDetectionConfigOut"
                ]
            ).optional(),
            "faceDetectionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_FaceDetectionConfigOut"]
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_VideoSegmentOut"])
            ).optional(),
            "speechTranscriptionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigOut"]
            ).optional(),
            "textDetectionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_TextDetectionConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_VideoContextOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_NormalizedVertexIn"] = t.struct(
        {"y": t.number().optional(), "x": t.number().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_NormalizedVertexIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_NormalizedVertexOut"] = t.struct(
        {
            "y": t.number().optional(),
            "x": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_NormalizedVertexOut"])
    types[
        "GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternativeIn"
    ] = t.struct({"transcript": t.string().optional()}).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternativeIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternativeOut"
    ] = t.struct(
        {
            "transcript": t.string().optional(),
            "words": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_WordInfoOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternativeOut"]
    )
    types["GoogleCloudVideointelligenceV1p1beta1_TextFrameIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "rotatedBoundingBox": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPolyIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_TextFrameIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_TextFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "rotatedBoundingBox": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPolyOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_TextFrameOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeIn"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeOut"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeOut"])
    types["GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotationIn"] = t.struct(
        {
            "version": t.string().optional(),
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_ExplicitContentFrameIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotationIn"])
    types[
        "GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotationOut"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_ExplicitContentFrameOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexIn"] = t.struct(
        {"x": t.number().optional(), "y": t.number().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexOut"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "pornographyLikelihood": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "pornographyLikelihood": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_LabelFrameIn"] = t.struct(
        {"timeOffset": t.string().optional(), "confidence": t.number().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_LabelFrameIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_LabelFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_LabelFrameOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_TextFrameIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "rotatedBoundingBox": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPolyIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TextFrameIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_TextFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "rotatedBoundingBox": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPolyOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TextFrameOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_TrackIn"] = t.struct(
        {
            "timestampedObjects": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_TimestampedObjectIn"]
                )
            ).optional(),
            "confidence": t.number().optional(),
            "attributes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeIn"]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_TrackIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_TrackOut"] = t.struct(
        {
            "timestampedObjects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_TimestampedObjectOut"
                    ]
                )
            ).optional(),
            "confidence": t.number().optional(),
            "attributes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeOut"
                    ]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_TrackOut"])
    types["GoogleCloudVideointelligenceV1beta2_EntityIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "entityId": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_EntityIn"])
    types["GoogleCloudVideointelligenceV1beta2_EntityOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "entityId": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_EntityOut"])
    types["GoogleCloudVideointelligenceV1_ObjectTrackingFrameIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1_NormalizedBoundingBoxIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_ObjectTrackingFrameIn"])
    types["GoogleCloudVideointelligenceV1_ObjectTrackingFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1_NormalizedBoundingBoxOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_ObjectTrackingFrameOut"])
    types["GoogleCloudVideointelligenceV1beta2_WordInfoIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "word": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_WordInfoIn"])
    types["GoogleCloudVideointelligenceV1beta2_WordInfoOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "speakerTag": t.integer().optional(),
            "confidence": t.number().optional(),
            "word": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_WordInfoOut"])

    functions = {}
    functions["operationsProjectsLocationsOperationsGet"] = videointelligence.delete(
        "v1/operations/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobuf_EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsProjectsLocationsOperationsCancel"] = videointelligence.delete(
        "v1/operations/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobuf_EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsProjectsLocationsOperationsDelete"] = videointelligence.delete(
        "v1/operations/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobuf_EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videosAnnotate"] = videointelligence.post(
        "v1/videos:annotate",
        t.struct(
            {
                "features": t.array(t.string()),
                "outputUri": t.string().optional(),
                "locationId": t.string().optional(),
                "inputUri": t.string().optional(),
                "inputContent": t.string().optional(),
                "videoContext": t.proxy(
                    renames["GoogleCloudVideointelligenceV1_VideoContextIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning_OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = videointelligence.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning_ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = videointelligence.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning_ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = videointelligence.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning_ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = videointelligence.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning_ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="videointelligence",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
