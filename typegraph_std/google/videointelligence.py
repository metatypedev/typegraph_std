from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_videointelligence() -> Import:
    videointelligence = HTTPRuntime("https://videointelligence.googleapis.com/")

    renames = {
        "ErrorResponse": "_videointelligence_1_ErrorResponse",
        "GoogleCloudVideointelligenceV1p3beta1_TextFrameIn": "_videointelligence_2_GoogleCloudVideointelligenceV1p3beta1_TextFrameIn",
        "GoogleCloudVideointelligenceV1p3beta1_TextFrameOut": "_videointelligence_3_GoogleCloudVideointelligenceV1p3beta1_TextFrameOut",
        "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationIn": "_videointelligence_4_GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationIn",
        "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationOut": "_videointelligence_5_GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponseIn": "_videointelligence_6_GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponseIn",
        "GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponseOut": "_videointelligence_7_GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoResponseOut",
        "GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxIn": "_videointelligence_8_GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxIn",
        "GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxOut": "_videointelligence_9_GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxOut",
        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationIn": "_videointelligence_10_GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationIn",
        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationOut": "_videointelligence_11_GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationOut",
        "GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationIn": "_videointelligence_12_GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationIn",
        "GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationOut": "_videointelligence_13_GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_FaceSegmentIn": "_videointelligence_14_GoogleCloudVideointelligenceV1p2beta1_FaceSegmentIn",
        "GoogleCloudVideointelligenceV1p2beta1_FaceSegmentOut": "_videointelligence_15_GoogleCloudVideointelligenceV1p2beta1_FaceSegmentOut",
        "GoogleCloudVideointelligenceV1p3beta1_LabelFrameIn": "_videointelligence_16_GoogleCloudVideointelligenceV1p3beta1_LabelFrameIn",
        "GoogleCloudVideointelligenceV1p3beta1_LabelFrameOut": "_videointelligence_17_GoogleCloudVideointelligenceV1p3beta1_LabelFrameOut",
        "GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxIn": "_videointelligence_18_GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxIn",
        "GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxOut": "_videointelligence_19_GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxOut",
        "GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeIn": "_videointelligence_20_GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeIn",
        "GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeOut": "_videointelligence_21_GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeOut",
        "GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkIn": "_videointelligence_22_GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkIn",
        "GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkOut": "_videointelligence_23_GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkOut",
        "GoogleCloudVideointelligenceV1p2beta1_TrackIn": "_videointelligence_24_GoogleCloudVideointelligenceV1p2beta1_TrackIn",
        "GoogleCloudVideointelligenceV1p2beta1_TrackOut": "_videointelligence_25_GoogleCloudVideointelligenceV1p2beta1_TrackOut",
        "GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrityIn": "_videointelligence_26_GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrityIn",
        "GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrityOut": "_videointelligence_27_GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrityOut",
        "GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkIn": "_videointelligence_28_GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkIn",
        "GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkOut": "_videointelligence_29_GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkOut",
        "GoogleCloudVideointelligenceV1_NormalizedVertexIn": "_videointelligence_30_GoogleCloudVideointelligenceV1_NormalizedVertexIn",
        "GoogleCloudVideointelligenceV1_NormalizedVertexOut": "_videointelligence_31_GoogleCloudVideointelligenceV1_NormalizedVertexOut",
        "GoogleCloudVideointelligenceV1p3beta1_TextAnnotationIn": "_videointelligence_32_GoogleCloudVideointelligenceV1p3beta1_TextAnnotationIn",
        "GoogleCloudVideointelligenceV1p3beta1_TextAnnotationOut": "_videointelligence_33_GoogleCloudVideointelligenceV1p3beta1_TextAnnotationOut",
        "GoogleCloudVideointelligenceV1_TextDetectionConfigIn": "_videointelligence_34_GoogleCloudVideointelligenceV1_TextDetectionConfigIn",
        "GoogleCloudVideointelligenceV1_TextDetectionConfigOut": "_videointelligence_35_GoogleCloudVideointelligenceV1_TextDetectionConfigOut",
        "GoogleCloudVideointelligenceV1p3beta1_CelebrityIn": "_videointelligence_36_GoogleCloudVideointelligenceV1p3beta1_CelebrityIn",
        "GoogleCloudVideointelligenceV1p3beta1_CelebrityOut": "_videointelligence_37_GoogleCloudVideointelligenceV1p3beta1_CelebrityOut",
        "GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationIn": "_videointelligence_38_GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationIn",
        "GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationOut": "_videointelligence_39_GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationOut",
        "GoogleCloudVideointelligenceV1p1beta1_TextAnnotationIn": "_videointelligence_40_GoogleCloudVideointelligenceV1p1beta1_TextAnnotationIn",
        "GoogleCloudVideointelligenceV1p1beta1_TextAnnotationOut": "_videointelligence_41_GoogleCloudVideointelligenceV1p1beta1_TextAnnotationOut",
        "GoogleCloudVideointelligenceV1_WordInfoIn": "_videointelligence_42_GoogleCloudVideointelligenceV1_WordInfoIn",
        "GoogleCloudVideointelligenceV1_WordInfoOut": "_videointelligence_43_GoogleCloudVideointelligenceV1_WordInfoOut",
        "GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationIn": "_videointelligence_44_GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationOut": "_videointelligence_45_GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1_DetectedLandmarkIn": "_videointelligence_46_GoogleCloudVideointelligenceV1_DetectedLandmarkIn",
        "GoogleCloudVideointelligenceV1_DetectedLandmarkOut": "_videointelligence_47_GoogleCloudVideointelligenceV1_DetectedLandmarkOut",
        "GoogleCloudVideointelligenceV1p2beta1_LabelFrameIn": "_videointelligence_48_GoogleCloudVideointelligenceV1p2beta1_LabelFrameIn",
        "GoogleCloudVideointelligenceV1p2beta1_LabelFrameOut": "_videointelligence_49_GoogleCloudVideointelligenceV1p2beta1_LabelFrameOut",
        "GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResultsIn": "_videointelligence_50_GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResultsIn",
        "GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResultsOut": "_videointelligence_51_GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResultsOut",
        "GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgressIn": "_videointelligence_52_GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgressIn",
        "GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgressOut": "_videointelligence_53_GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoProgressOut",
        "GoogleCloudVideointelligenceV1_FaceFrameIn": "_videointelligence_54_GoogleCloudVideointelligenceV1_FaceFrameIn",
        "GoogleCloudVideointelligenceV1_FaceFrameOut": "_videointelligence_55_GoogleCloudVideointelligenceV1_FaceFrameOut",
        "GoogleCloudVideointelligenceV1p3beta1_TrackIn": "_videointelligence_56_GoogleCloudVideointelligenceV1p3beta1_TrackIn",
        "GoogleCloudVideointelligenceV1p3beta1_TrackOut": "_videointelligence_57_GoogleCloudVideointelligenceV1p3beta1_TrackOut",
        "GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotationIn": "_videointelligence_58_GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotationIn",
        "GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotationOut": "_videointelligence_59_GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotationOut",
        "GoogleCloudVideointelligenceV1_ObjectTrackingFrameIn": "_videointelligence_60_GoogleCloudVideointelligenceV1_ObjectTrackingFrameIn",
        "GoogleCloudVideointelligenceV1_ObjectTrackingFrameOut": "_videointelligence_61_GoogleCloudVideointelligenceV1_ObjectTrackingFrameOut",
        "GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgressIn": "_videointelligence_62_GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgressIn",
        "GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgressOut": "_videointelligence_63_GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgressOut",
        "GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigIn": "_videointelligence_64_GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigIn",
        "GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigOut": "_videointelligence_65_GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigOut",
        "GoogleCloudVideointelligenceV1p3beta1_NormalizedVertexIn": "_videointelligence_66_GoogleCloudVideointelligenceV1p3beta1_NormalizedVertexIn",
        "GoogleCloudVideointelligenceV1p3beta1_NormalizedVertexOut": "_videointelligence_67_GoogleCloudVideointelligenceV1p3beta1_NormalizedVertexOut",
        "GoogleCloudVideointelligenceV1_FaceDetectionConfigIn": "_videointelligence_68_GoogleCloudVideointelligenceV1_FaceDetectionConfigIn",
        "GoogleCloudVideointelligenceV1_FaceDetectionConfigOut": "_videointelligence_69_GoogleCloudVideointelligenceV1_FaceDetectionConfigOut",
        "GoogleCloudVideointelligenceV1_LabelSegmentIn": "_videointelligence_70_GoogleCloudVideointelligenceV1_LabelSegmentIn",
        "GoogleCloudVideointelligenceV1_LabelSegmentOut": "_videointelligence_71_GoogleCloudVideointelligenceV1_LabelSegmentOut",
        "GoogleCloudVideointelligenceV1beta2_TimestampedObjectIn": "_videointelligence_72_GoogleCloudVideointelligenceV1beta2_TimestampedObjectIn",
        "GoogleCloudVideointelligenceV1beta2_TimestampedObjectOut": "_videointelligence_73_GoogleCloudVideointelligenceV1beta2_TimestampedObjectOut",
        "GoogleCloudVideointelligenceV1beta2_NormalizedVertexIn": "_videointelligence_74_GoogleCloudVideointelligenceV1beta2_NormalizedVertexIn",
        "GoogleCloudVideointelligenceV1beta2_NormalizedVertexOut": "_videointelligence_75_GoogleCloudVideointelligenceV1beta2_NormalizedVertexOut",
        "GoogleCloudVideointelligenceV1_EntityIn": "_videointelligence_76_GoogleCloudVideointelligenceV1_EntityIn",
        "GoogleCloudVideointelligenceV1_EntityOut": "_videointelligence_77_GoogleCloudVideointelligenceV1_EntityOut",
        "GoogleCloudVideointelligenceV1p1beta1_TimestampedObjectIn": "_videointelligence_78_GoogleCloudVideointelligenceV1p1beta1_TimestampedObjectIn",
        "GoogleCloudVideointelligenceV1p1beta1_TimestampedObjectOut": "_videointelligence_79_GoogleCloudVideointelligenceV1p1beta1_TimestampedObjectOut",
        "GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponseIn": "_videointelligence_80_GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponseIn",
        "GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponseOut": "_videointelligence_81_GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoResponseOut",
        "GoogleCloudVideointelligenceV1_DetectedAttributeIn": "_videointelligence_82_GoogleCloudVideointelligenceV1_DetectedAttributeIn",
        "GoogleCloudVideointelligenceV1_DetectedAttributeOut": "_videointelligence_83_GoogleCloudVideointelligenceV1_DetectedAttributeOut",
        "GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternativeIn": "_videointelligence_84_GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternativeIn",
        "GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternativeOut": "_videointelligence_85_GoogleCloudVideointelligenceV1p2beta1_SpeechRecognitionAlternativeOut",
        "GoogleCloudVideointelligenceV1_VideoAnnotationResultsIn": "_videointelligence_86_GoogleCloudVideointelligenceV1_VideoAnnotationResultsIn",
        "GoogleCloudVideointelligenceV1_VideoAnnotationResultsOut": "_videointelligence_87_GoogleCloudVideointelligenceV1_VideoAnnotationResultsOut",
        "GoogleCloudVideointelligenceV1p2beta1_FaceFrameIn": "_videointelligence_88_GoogleCloudVideointelligenceV1p2beta1_FaceFrameIn",
        "GoogleCloudVideointelligenceV1p2beta1_FaceFrameOut": "_videointelligence_89_GoogleCloudVideointelligenceV1p2beta1_FaceFrameOut",
        "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameIn": "_videointelligence_90_GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameIn",
        "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameOut": "_videointelligence_91_GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameOut",
        "GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationIn": "_videointelligence_92_GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationIn",
        "GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationOut": "_videointelligence_93_GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationOut",
        "GoogleCloudVideointelligenceV1p3beta1_FaceSegmentIn": "_videointelligence_94_GoogleCloudVideointelligenceV1p3beta1_FaceSegmentIn",
        "GoogleCloudVideointelligenceV1p3beta1_FaceSegmentOut": "_videointelligence_95_GoogleCloudVideointelligenceV1p3beta1_FaceSegmentOut",
        "GoogleCloudVideointelligenceV1beta2_TextAnnotationIn": "_videointelligence_96_GoogleCloudVideointelligenceV1beta2_TextAnnotationIn",
        "GoogleCloudVideointelligenceV1beta2_TextAnnotationOut": "_videointelligence_97_GoogleCloudVideointelligenceV1beta2_TextAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeIn": "_videointelligence_98_GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeIn",
        "GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeOut": "_videointelligence_99_GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeOut",
        "GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgressIn": "_videointelligence_100_GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgressIn",
        "GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgressOut": "_videointelligence_101_GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgressOut",
        "GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotationIn": "_videointelligence_102_GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotationOut": "_videointelligence_103_GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPolyIn": "_videointelligence_104_GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPolyIn",
        "GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPolyOut": "_videointelligence_105_GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPolyOut",
        "GoogleCloudVideointelligenceV1_FaceDetectionAnnotationIn": "_videointelligence_106_GoogleCloudVideointelligenceV1_FaceDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1_FaceDetectionAnnotationOut": "_videointelligence_107_GoogleCloudVideointelligenceV1_FaceDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotationIn": "_videointelligence_108_GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotationOut": "_videointelligence_109_GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationIn": "_videointelligence_110_GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationIn",
        "GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationOut": "_videointelligence_111_GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationOut",
        "GoogleCloudVideointelligenceV1beta2_EntityIn": "_videointelligence_112_GoogleCloudVideointelligenceV1beta2_EntityIn",
        "GoogleCloudVideointelligenceV1beta2_EntityOut": "_videointelligence_113_GoogleCloudVideointelligenceV1beta2_EntityOut",
        "GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotationIn": "_videointelligence_114_GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotationIn",
        "GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotationOut": "_videointelligence_115_GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotationOut",
        "GoogleCloudVideointelligenceV1_SpeechTranscriptionIn": "_videointelligence_116_GoogleCloudVideointelligenceV1_SpeechTranscriptionIn",
        "GoogleCloudVideointelligenceV1_SpeechTranscriptionOut": "_videointelligence_117_GoogleCloudVideointelligenceV1_SpeechTranscriptionOut",
        "GoogleCloudVideointelligenceV1_LabelDetectionConfigIn": "_videointelligence_118_GoogleCloudVideointelligenceV1_LabelDetectionConfigIn",
        "GoogleCloudVideointelligenceV1_LabelDetectionConfigOut": "_videointelligence_119_GoogleCloudVideointelligenceV1_LabelDetectionConfigOut",
        "GoogleCloudVideointelligenceV1p3beta1_LabelSegmentIn": "_videointelligence_120_GoogleCloudVideointelligenceV1p3beta1_LabelSegmentIn",
        "GoogleCloudVideointelligenceV1p3beta1_LabelSegmentOut": "_videointelligence_121_GoogleCloudVideointelligenceV1p3beta1_LabelSegmentOut",
        "GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexIn": "_videointelligence_122_GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexIn",
        "GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexOut": "_videointelligence_123_GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexOut",
        "GoogleCloudVideointelligenceV1p1beta1_FaceSegmentIn": "_videointelligence_124_GoogleCloudVideointelligenceV1p1beta1_FaceSegmentIn",
        "GoogleCloudVideointelligenceV1p1beta1_FaceSegmentOut": "_videointelligence_125_GoogleCloudVideointelligenceV1p1beta1_FaceSegmentOut",
        "GoogleProtobuf_EmptyIn": "_videointelligence_126_GoogleProtobuf_EmptyIn",
        "GoogleProtobuf_EmptyOut": "_videointelligence_127_GoogleProtobuf_EmptyOut",
        "GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackIn": "_videointelligence_128_GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackIn",
        "GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackOut": "_videointelligence_129_GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackOut",
        "GoogleCloudVideointelligenceV1_TextSegmentIn": "_videointelligence_130_GoogleCloudVideointelligenceV1_TextSegmentIn",
        "GoogleCloudVideointelligenceV1_TextSegmentOut": "_videointelligence_131_GoogleCloudVideointelligenceV1_TextSegmentOut",
        "GoogleCloudVideointelligenceV1beta2_TextSegmentIn": "_videointelligence_132_GoogleCloudVideointelligenceV1beta2_TextSegmentIn",
        "GoogleCloudVideointelligenceV1beta2_TextSegmentOut": "_videointelligence_133_GoogleCloudVideointelligenceV1beta2_TextSegmentOut",
        "GoogleLongrunning_CancelOperationRequestIn": "_videointelligence_134_GoogleLongrunning_CancelOperationRequestIn",
        "GoogleLongrunning_CancelOperationRequestOut": "_videointelligence_135_GoogleLongrunning_CancelOperationRequestOut",
        "GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn": "_videointelligence_136_GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn",
        "GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut": "_videointelligence_137_GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut",
        "GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResultsIn": "_videointelligence_138_GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResultsIn",
        "GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResultsOut": "_videointelligence_139_GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResultsOut",
        "GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgressIn": "_videointelligence_140_GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgressIn",
        "GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgressOut": "_videointelligence_141_GoogleCloudVideointelligenceV1p2beta1_AnnotateVideoProgressOut",
        "GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameIn": "_videointelligence_142_GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameIn",
        "GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameOut": "_videointelligence_143_GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameOut",
        "GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn": "_videointelligence_144_GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn",
        "GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut": "_videointelligence_145_GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut",
        "GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkIn": "_videointelligence_146_GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkIn",
        "GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkOut": "_videointelligence_147_GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkOut",
        "GoogleCloudVideointelligenceV1beta2_VideoAnnotationResultsIn": "_videointelligence_148_GoogleCloudVideointelligenceV1beta2_VideoAnnotationResultsIn",
        "GoogleCloudVideointelligenceV1beta2_VideoAnnotationResultsOut": "_videointelligence_149_GoogleCloudVideointelligenceV1beta2_VideoAnnotationResultsOut",
        "GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationIn": "_videointelligence_150_GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationOut": "_videointelligence_151_GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_TimestampedObjectIn": "_videointelligence_152_GoogleCloudVideointelligenceV1p2beta1_TimestampedObjectIn",
        "GoogleCloudVideointelligenceV1p2beta1_TimestampedObjectOut": "_videointelligence_153_GoogleCloudVideointelligenceV1p2beta1_TimestampedObjectOut",
        "GoogleCloudVideointelligenceV1p2beta1_SpeechTranscriptionIn": "_videointelligence_154_GoogleCloudVideointelligenceV1p2beta1_SpeechTranscriptionIn",
        "GoogleCloudVideointelligenceV1p2beta1_SpeechTranscriptionOut": "_videointelligence_155_GoogleCloudVideointelligenceV1p2beta1_SpeechTranscriptionOut",
        "GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponseIn": "_videointelligence_156_GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponseIn",
        "GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponseOut": "_videointelligence_157_GoogleCloudVideointelligenceV1beta2_AnnotateVideoResponseOut",
        "GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeIn": "_videointelligence_158_GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeIn",
        "GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeOut": "_videointelligence_159_GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeOut",
        "GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgressIn": "_videointelligence_160_GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgressIn",
        "GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgressOut": "_videointelligence_161_GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgressOut",
        "GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn": "_videointelligence_162_GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn",
        "GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut": "_videointelligence_163_GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut",
        "GoogleLongrunning_OperationIn": "_videointelligence_164_GoogleLongrunning_OperationIn",
        "GoogleLongrunning_OperationOut": "_videointelligence_165_GoogleLongrunning_OperationOut",
        "GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn": "_videointelligence_166_GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn",
        "GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut": "_videointelligence_167_GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut",
        "GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPolyIn": "_videointelligence_168_GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPolyIn",
        "GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPolyOut": "_videointelligence_169_GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingPolyOut",
        "GoogleCloudVideointelligenceV1_TrackIn": "_videointelligence_170_GoogleCloudVideointelligenceV1_TrackIn",
        "GoogleCloudVideointelligenceV1_TrackOut": "_videointelligence_171_GoogleCloudVideointelligenceV1_TrackOut",
        "GoogleCloudVideointelligenceV1p2beta1_EntityIn": "_videointelligence_172_GoogleCloudVideointelligenceV1p2beta1_EntityIn",
        "GoogleCloudVideointelligenceV1p2beta1_EntityOut": "_videointelligence_173_GoogleCloudVideointelligenceV1p2beta1_EntityOut",
        "GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotationIn": "_videointelligence_174_GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotationOut": "_videointelligence_175_GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternativeIn": "_videointelligence_176_GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternativeIn",
        "GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternativeOut": "_videointelligence_177_GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternativeOut",
        "GoogleCloudVideointelligenceV1beta2_FaceFrameIn": "_videointelligence_178_GoogleCloudVideointelligenceV1beta2_FaceFrameIn",
        "GoogleCloudVideointelligenceV1beta2_FaceFrameOut": "_videointelligence_179_GoogleCloudVideointelligenceV1beta2_FaceFrameOut",
        "GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgressIn": "_videointelligence_180_GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgressIn",
        "GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgressOut": "_videointelligence_181_GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoProgressOut",
        "GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgressIn": "_videointelligence_182_GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgressIn",
        "GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgressOut": "_videointelligence_183_GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgressOut",
        "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrameIn": "_videointelligence_184_GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrameIn",
        "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrameOut": "_videointelligence_185_GoogleCloudVideointelligenceV1p3beta1_ExplicitContentFrameOut",
        "GoogleCloudVideointelligenceV1p3beta1_TextSegmentIn": "_videointelligence_186_GoogleCloudVideointelligenceV1p3beta1_TextSegmentIn",
        "GoogleCloudVideointelligenceV1p3beta1_TextSegmentOut": "_videointelligence_187_GoogleCloudVideointelligenceV1p3beta1_TextSegmentOut",
        "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationIn": "_videointelligence_188_GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationIn",
        "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationOut": "_videointelligence_189_GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_LabelSegmentIn": "_videointelligence_190_GoogleCloudVideointelligenceV1p2beta1_LabelSegmentIn",
        "GoogleCloudVideointelligenceV1p2beta1_LabelSegmentOut": "_videointelligence_191_GoogleCloudVideointelligenceV1p2beta1_LabelSegmentOut",
        "GoogleCloudVideointelligenceV1_TimestampedObjectIn": "_videointelligence_192_GoogleCloudVideointelligenceV1_TimestampedObjectIn",
        "GoogleCloudVideointelligenceV1_TimestampedObjectOut": "_videointelligence_193_GoogleCloudVideointelligenceV1_TimestampedObjectOut",
        "GoogleCloudVideointelligenceV1_VideoAnnotationProgressIn": "_videointelligence_194_GoogleCloudVideointelligenceV1_VideoAnnotationProgressIn",
        "GoogleCloudVideointelligenceV1_VideoAnnotationProgressOut": "_videointelligence_195_GoogleCloudVideointelligenceV1_VideoAnnotationProgressOut",
        "GoogleCloudVideointelligenceV1p3beta1_WordInfoIn": "_videointelligence_196_GoogleCloudVideointelligenceV1p3beta1_WordInfoIn",
        "GoogleCloudVideointelligenceV1p3beta1_WordInfoOut": "_videointelligence_197_GoogleCloudVideointelligenceV1p3beta1_WordInfoOut",
        "GoogleCloudVideointelligenceV1p1beta1_LabelFrameIn": "_videointelligence_198_GoogleCloudVideointelligenceV1p1beta1_LabelFrameIn",
        "GoogleCloudVideointelligenceV1p1beta1_LabelFrameOut": "_videointelligence_199_GoogleCloudVideointelligenceV1p1beta1_LabelFrameOut",
        "GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationIn": "_videointelligence_200_GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationIn",
        "GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationOut": "_videointelligence_201_GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationOut",
        "GoogleCloudVideointelligenceV1_AnnotateVideoResponseIn": "_videointelligence_202_GoogleCloudVideointelligenceV1_AnnotateVideoResponseIn",
        "GoogleCloudVideointelligenceV1_AnnotateVideoResponseOut": "_videointelligence_203_GoogleCloudVideointelligenceV1_AnnotateVideoResponseOut",
        "GoogleCloudVideointelligenceV1beta2_WordInfoIn": "_videointelligence_204_GoogleCloudVideointelligenceV1beta2_WordInfoIn",
        "GoogleCloudVideointelligenceV1beta2_WordInfoOut": "_videointelligence_205_GoogleCloudVideointelligenceV1beta2_WordInfoOut",
        "GoogleCloudVideointelligenceV1p2beta1_TextFrameIn": "_videointelligence_206_GoogleCloudVideointelligenceV1p2beta1_TextFrameIn",
        "GoogleCloudVideointelligenceV1p2beta1_TextFrameOut": "_videointelligence_207_GoogleCloudVideointelligenceV1p2beta1_TextFrameOut",
        "GoogleCloudVideointelligenceV1p1beta1_FaceFrameIn": "_videointelligence_208_GoogleCloudVideointelligenceV1p1beta1_FaceFrameIn",
        "GoogleCloudVideointelligenceV1p1beta1_FaceFrameOut": "_videointelligence_209_GoogleCloudVideointelligenceV1p1beta1_FaceFrameOut",
        "GoogleCloudVideointelligenceV1p1beta1_TextSegmentIn": "_videointelligence_210_GoogleCloudVideointelligenceV1p1beta1_TextSegmentIn",
        "GoogleCloudVideointelligenceV1p1beta1_TextSegmentOut": "_videointelligence_211_GoogleCloudVideointelligenceV1p1beta1_TextSegmentOut",
        "GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotationIn": "_videointelligence_212_GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotationIn",
        "GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotationOut": "_videointelligence_213_GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotationOut",
        "GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotationIn": "_videointelligence_214_GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotationIn",
        "GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotationOut": "_videointelligence_215_GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotationOut",
        "GoogleCloudVideointelligenceV1_ExplicitContentFrameIn": "_videointelligence_216_GoogleCloudVideointelligenceV1_ExplicitContentFrameIn",
        "GoogleCloudVideointelligenceV1_ExplicitContentFrameOut": "_videointelligence_217_GoogleCloudVideointelligenceV1_ExplicitContentFrameOut",
        "GoogleCloudVideointelligenceV1_PersonDetectionConfigIn": "_videointelligence_218_GoogleCloudVideointelligenceV1_PersonDetectionConfigIn",
        "GoogleCloudVideointelligenceV1_PersonDetectionConfigOut": "_videointelligence_219_GoogleCloudVideointelligenceV1_PersonDetectionConfigOut",
        "GoogleCloudVideointelligenceV1_FaceSegmentIn": "_videointelligence_220_GoogleCloudVideointelligenceV1_FaceSegmentIn",
        "GoogleCloudVideointelligenceV1_FaceSegmentOut": "_videointelligence_221_GoogleCloudVideointelligenceV1_FaceSegmentOut",
        "GoogleCloudVideointelligenceV1_AnnotateVideoProgressIn": "_videointelligence_222_GoogleCloudVideointelligenceV1_AnnotateVideoProgressIn",
        "GoogleCloudVideointelligenceV1_AnnotateVideoProgressOut": "_videointelligence_223_GoogleCloudVideointelligenceV1_AnnotateVideoProgressOut",
        "GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrameIn": "_videointelligence_224_GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrameIn",
        "GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrameOut": "_videointelligence_225_GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrameOut",
        "GoogleLongrunning_ListOperationsResponseIn": "_videointelligence_226_GoogleLongrunning_ListOperationsResponseIn",
        "GoogleLongrunning_ListOperationsResponseOut": "_videointelligence_227_GoogleLongrunning_ListOperationsResponseOut",
        "GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationIn": "_videointelligence_228_GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationIn",
        "GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationOut": "_videointelligence_229_GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationOut",
        "GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionIn": "_videointelligence_230_GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionIn",
        "GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionOut": "_videointelligence_231_GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionOut",
        "GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxIn": "_videointelligence_232_GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxIn",
        "GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxOut": "_videointelligence_233_GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxOut",
        "GoogleCloudVideointelligenceV1_SpeechRecognitionAlternativeIn": "_videointelligence_234_GoogleCloudVideointelligenceV1_SpeechRecognitionAlternativeIn",
        "GoogleCloudVideointelligenceV1_SpeechRecognitionAlternativeOut": "_videointelligence_235_GoogleCloudVideointelligenceV1_SpeechRecognitionAlternativeOut",
        "GoogleRpc_StatusIn": "_videointelligence_236_GoogleRpc_StatusIn",
        "GoogleRpc_StatusOut": "_videointelligence_237_GoogleRpc_StatusOut",
        "GoogleCloudVideointelligenceV1p2beta1_WordInfoIn": "_videointelligence_238_GoogleCloudVideointelligenceV1p2beta1_WordInfoIn",
        "GoogleCloudVideointelligenceV1p2beta1_WordInfoOut": "_videointelligence_239_GoogleCloudVideointelligenceV1p2beta1_WordInfoOut",
        "GoogleCloudVideointelligenceV1p2beta1_TextSegmentIn": "_videointelligence_240_GoogleCloudVideointelligenceV1p2beta1_TextSegmentIn",
        "GoogleCloudVideointelligenceV1p2beta1_TextSegmentOut": "_videointelligence_241_GoogleCloudVideointelligenceV1p2beta1_TextSegmentOut",
        "GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationIn": "_videointelligence_242_GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationIn",
        "GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationOut": "_videointelligence_243_GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationOut",
        "GoogleCloudVideointelligenceV1_ExplicitContentAnnotationIn": "_videointelligence_244_GoogleCloudVideointelligenceV1_ExplicitContentAnnotationIn",
        "GoogleCloudVideointelligenceV1_ExplicitContentAnnotationOut": "_videointelligence_245_GoogleCloudVideointelligenceV1_ExplicitContentAnnotationOut",
        "GoogleCloudVideointelligenceV1p3beta1_EntityIn": "_videointelligence_246_GoogleCloudVideointelligenceV1p3beta1_EntityIn",
        "GoogleCloudVideointelligenceV1p3beta1_EntityOut": "_videointelligence_247_GoogleCloudVideointelligenceV1p3beta1_EntityOut",
        "GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResultsIn": "_videointelligence_248_GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResultsIn",
        "GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResultsOut": "_videointelligence_249_GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResultsOut",
        "GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationIn": "_videointelligence_250_GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationOut": "_videointelligence_251_GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1_NormalizedBoundingPolyIn": "_videointelligence_252_GoogleCloudVideointelligenceV1_NormalizedBoundingPolyIn",
        "GoogleCloudVideointelligenceV1_NormalizedBoundingPolyOut": "_videointelligence_253_GoogleCloudVideointelligenceV1_NormalizedBoundingPolyOut",
        "GoogleCloudVideointelligenceV1_ExplicitContentDetectionConfigIn": "_videointelligence_254_GoogleCloudVideointelligenceV1_ExplicitContentDetectionConfigIn",
        "GoogleCloudVideointelligenceV1_ExplicitContentDetectionConfigOut": "_videointelligence_255_GoogleCloudVideointelligenceV1_ExplicitContentDetectionConfigOut",
        "GoogleCloudVideointelligenceV1beta2_ExplicitContentFrameIn": "_videointelligence_256_GoogleCloudVideointelligenceV1beta2_ExplicitContentFrameIn",
        "GoogleCloudVideointelligenceV1beta2_ExplicitContentFrameOut": "_videointelligence_257_GoogleCloudVideointelligenceV1beta2_ExplicitContentFrameOut",
        "GoogleCloudVideointelligenceV1p1beta1_LabelSegmentIn": "_videointelligence_258_GoogleCloudVideointelligenceV1p1beta1_LabelSegmentIn",
        "GoogleCloudVideointelligenceV1p1beta1_LabelSegmentOut": "_videointelligence_259_GoogleCloudVideointelligenceV1p1beta1_LabelSegmentOut",
        "GoogleCloudVideointelligenceV1beta2_LabelSegmentIn": "_videointelligence_260_GoogleCloudVideointelligenceV1beta2_LabelSegmentIn",
        "GoogleCloudVideointelligenceV1beta2_LabelSegmentOut": "_videointelligence_261_GoogleCloudVideointelligenceV1beta2_LabelSegmentOut",
        "GoogleCloudVideointelligenceV1p3beta1_FaceFrameIn": "_videointelligence_262_GoogleCloudVideointelligenceV1p3beta1_FaceFrameIn",
        "GoogleCloudVideointelligenceV1p3beta1_FaceFrameOut": "_videointelligence_263_GoogleCloudVideointelligenceV1p3beta1_FaceFrameOut",
        "GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPolyIn": "_videointelligence_264_GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPolyIn",
        "GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPolyOut": "_videointelligence_265_GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPolyOut",
        "GoogleCloudVideointelligenceV1_TextFrameIn": "_videointelligence_266_GoogleCloudVideointelligenceV1_TextFrameIn",
        "GoogleCloudVideointelligenceV1_TextFrameOut": "_videointelligence_267_GoogleCloudVideointelligenceV1_TextFrameOut",
        "GoogleCloudVideointelligenceV1_VideoContextIn": "_videointelligence_268_GoogleCloudVideointelligenceV1_VideoContextIn",
        "GoogleCloudVideointelligenceV1_VideoContextOut": "_videointelligence_269_GoogleCloudVideointelligenceV1_VideoContextOut",
        "GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationIn": "_videointelligence_270_GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationIn",
        "GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationOut": "_videointelligence_271_GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationOut",
        "GoogleCloudVideointelligenceV1beta2_FaceAnnotationIn": "_videointelligence_272_GoogleCloudVideointelligenceV1beta2_FaceAnnotationIn",
        "GoogleCloudVideointelligenceV1beta2_FaceAnnotationOut": "_videointelligence_273_GoogleCloudVideointelligenceV1beta2_FaceAnnotationOut",
        "GoogleCloudVideointelligenceV1_TextAnnotationIn": "_videointelligence_274_GoogleCloudVideointelligenceV1_TextAnnotationIn",
        "GoogleCloudVideointelligenceV1_TextAnnotationOut": "_videointelligence_275_GoogleCloudVideointelligenceV1_TextAnnotationOut",
        "GoogleCloudVideointelligenceV1_SpeechContextIn": "_videointelligence_276_GoogleCloudVideointelligenceV1_SpeechContextIn",
        "GoogleCloudVideointelligenceV1_SpeechContextOut": "_videointelligence_277_GoogleCloudVideointelligenceV1_SpeechContextOut",
        "GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotationIn": "_videointelligence_278_GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotationOut": "_videointelligence_279_GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1_VideoSegmentIn": "_videointelligence_280_GoogleCloudVideointelligenceV1_VideoSegmentIn",
        "GoogleCloudVideointelligenceV1_VideoSegmentOut": "_videointelligence_281_GoogleCloudVideointelligenceV1_VideoSegmentOut",
        "GoogleCloudVideointelligenceV1p1beta1_TrackIn": "_videointelligence_282_GoogleCloudVideointelligenceV1p1beta1_TrackIn",
        "GoogleCloudVideointelligenceV1p1beta1_TrackOut": "_videointelligence_283_GoogleCloudVideointelligenceV1p1beta1_TrackOut",
        "GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResultsIn": "_videointelligence_284_GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResultsIn",
        "GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResultsOut": "_videointelligence_285_GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResultsOut",
        "GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponseIn": "_videointelligence_286_GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponseIn",
        "GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponseOut": "_videointelligence_287_GoogleCloudVideointelligenceV1p3beta1_StreamingAnnotateVideoResponseOut",
        "GoogleCloudVideointelligenceV1p3beta1_TimestampedObjectIn": "_videointelligence_288_GoogleCloudVideointelligenceV1p3beta1_TimestampedObjectIn",
        "GoogleCloudVideointelligenceV1p3beta1_TimestampedObjectOut": "_videointelligence_289_GoogleCloudVideointelligenceV1p3beta1_TimestampedObjectOut",
        "GoogleCloudVideointelligenceV1p1beta1_WordInfoIn": "_videointelligence_290_GoogleCloudVideointelligenceV1p1beta1_WordInfoIn",
        "GoogleCloudVideointelligenceV1p1beta1_WordInfoOut": "_videointelligence_291_GoogleCloudVideointelligenceV1p1beta1_WordInfoOut",
        "GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternativeIn": "_videointelligence_292_GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternativeIn",
        "GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternativeOut": "_videointelligence_293_GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternativeOut",
        "GoogleCloudVideointelligenceV1beta2_TrackIn": "_videointelligence_294_GoogleCloudVideointelligenceV1beta2_TrackIn",
        "GoogleCloudVideointelligenceV1beta2_TrackOut": "_videointelligence_295_GoogleCloudVideointelligenceV1beta2_TrackOut",
        "GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationIn": "_videointelligence_296_GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationOut": "_videointelligence_297_GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrameIn": "_videointelligence_298_GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrameIn",
        "GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrameOut": "_videointelligence_299_GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrameOut",
        "GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionIn": "_videointelligence_300_GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionIn",
        "GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionOut": "_videointelligence_301_GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionOut",
        "GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrameIn": "_videointelligence_302_GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrameIn",
        "GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrameOut": "_videointelligence_303_GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrameOut",
        "GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPolyIn": "_videointelligence_304_GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPolyIn",
        "GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPolyOut": "_videointelligence_305_GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingPolyOut",
        "GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponseIn": "_videointelligence_306_GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponseIn",
        "GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponseOut": "_videointelligence_307_GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoResponseOut",
        "GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationIn": "_videointelligence_308_GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationIn",
        "GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationOut": "_videointelligence_309_GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationOut",
        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrameIn": "_videointelligence_310_GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrameIn",
        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrameOut": "_videointelligence_311_GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrameOut",
        "GoogleCloudVideointelligenceV1beta2_LabelFrameIn": "_videointelligence_312_GoogleCloudVideointelligenceV1beta2_LabelFrameIn",
        "GoogleCloudVideointelligenceV1beta2_LabelFrameOut": "_videointelligence_313_GoogleCloudVideointelligenceV1beta2_LabelFrameOut",
        "GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgressIn": "_videointelligence_314_GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgressIn",
        "GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgressOut": "_videointelligence_315_GoogleCloudVideointelligenceV1beta2_AnnotateVideoProgressOut",
        "GoogleCloudVideointelligenceV1_NormalizedBoundingBoxIn": "_videointelligence_316_GoogleCloudVideointelligenceV1_NormalizedBoundingBoxIn",
        "GoogleCloudVideointelligenceV1_NormalizedBoundingBoxOut": "_videointelligence_317_GoogleCloudVideointelligenceV1_NormalizedBoundingBoxOut",
        "GoogleCloudVideointelligenceV1beta2_DetectedLandmarkIn": "_videointelligence_318_GoogleCloudVideointelligenceV1beta2_DetectedLandmarkIn",
        "GoogleCloudVideointelligenceV1beta2_DetectedLandmarkOut": "_videointelligence_319_GoogleCloudVideointelligenceV1beta2_DetectedLandmarkOut",
        "GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotationIn": "_videointelligence_320_GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotationIn",
        "GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotationOut": "_videointelligence_321_GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotationOut",
        "GoogleCloudVideointelligenceV1_FaceAnnotationIn": "_videointelligence_322_GoogleCloudVideointelligenceV1_FaceAnnotationIn",
        "GoogleCloudVideointelligenceV1_FaceAnnotationOut": "_videointelligence_323_GoogleCloudVideointelligenceV1_FaceAnnotationOut",
        "GoogleCloudVideointelligenceV1_PersonDetectionAnnotationIn": "_videointelligence_324_GoogleCloudVideointelligenceV1_PersonDetectionAnnotationIn",
        "GoogleCloudVideointelligenceV1_PersonDetectionAnnotationOut": "_videointelligence_325_GoogleCloudVideointelligenceV1_PersonDetectionAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_NormalizedVertexIn": "_videointelligence_326_GoogleCloudVideointelligenceV1p2beta1_NormalizedVertexIn",
        "GoogleCloudVideointelligenceV1p2beta1_NormalizedVertexOut": "_videointelligence_327_GoogleCloudVideointelligenceV1p2beta1_NormalizedVertexOut",
        "GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeIn": "_videointelligence_328_GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeIn",
        "GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeOut": "_videointelligence_329_GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeOut",
        "GoogleCloudVideointelligenceV1beta2_LabelAnnotationIn": "_videointelligence_330_GoogleCloudVideointelligenceV1beta2_LabelAnnotationIn",
        "GoogleCloudVideointelligenceV1beta2_LabelAnnotationOut": "_videointelligence_331_GoogleCloudVideointelligenceV1beta2_LabelAnnotationOut",
        "GoogleCloudVideointelligenceV1_LabelAnnotationIn": "_videointelligence_332_GoogleCloudVideointelligenceV1_LabelAnnotationIn",
        "GoogleCloudVideointelligenceV1_LabelAnnotationOut": "_videointelligence_333_GoogleCloudVideointelligenceV1_LabelAnnotationOut",
        "GoogleCloudVideointelligenceV1_AnnotateVideoRequestIn": "_videointelligence_334_GoogleCloudVideointelligenceV1_AnnotateVideoRequestIn",
        "GoogleCloudVideointelligenceV1_AnnotateVideoRequestOut": "_videointelligence_335_GoogleCloudVideointelligenceV1_AnnotateVideoRequestOut",
        "GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxIn": "_videointelligence_336_GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxIn",
        "GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxOut": "_videointelligence_337_GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxOut",
        "GoogleCloudVideointelligenceV1beta2_VideoSegmentIn": "_videointelligence_338_GoogleCloudVideointelligenceV1beta2_VideoSegmentIn",
        "GoogleCloudVideointelligenceV1beta2_VideoSegmentOut": "_videointelligence_339_GoogleCloudVideointelligenceV1beta2_VideoSegmentOut",
        "GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationIn": "_videointelligence_340_GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationIn",
        "GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationOut": "_videointelligence_341_GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationOut",
        "GoogleCloudVideointelligenceV1_LogoRecognitionAnnotationIn": "_videointelligence_342_GoogleCloudVideointelligenceV1_LogoRecognitionAnnotationIn",
        "GoogleCloudVideointelligenceV1_LogoRecognitionAnnotationOut": "_videointelligence_343_GoogleCloudVideointelligenceV1_LogoRecognitionAnnotationOut",
        "GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigIn": "_videointelligence_344_GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigIn",
        "GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigOut": "_videointelligence_345_GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigOut",
        "GoogleCloudVideointelligenceV1_ObjectTrackingConfigIn": "_videointelligence_346_GoogleCloudVideointelligenceV1_ObjectTrackingConfigIn",
        "GoogleCloudVideointelligenceV1_ObjectTrackingConfigOut": "_videointelligence_347_GoogleCloudVideointelligenceV1_ObjectTrackingConfigOut",
        "GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotationIn": "_videointelligence_348_GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotationIn",
        "GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotationOut": "_videointelligence_349_GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotationOut",
        "GoogleCloudVideointelligenceV1p2beta1_TextAnnotationIn": "_videointelligence_350_GoogleCloudVideointelligenceV1p2beta1_TextAnnotationIn",
        "GoogleCloudVideointelligenceV1p2beta1_TextAnnotationOut": "_videointelligence_351_GoogleCloudVideointelligenceV1p2beta1_TextAnnotationOut",
        "GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionIn": "_videointelligence_352_GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionIn",
        "GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionOut": "_videointelligence_353_GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionOut",
        "GoogleCloudVideointelligenceV1_LabelFrameIn": "_videointelligence_354_GoogleCloudVideointelligenceV1_LabelFrameIn",
        "GoogleCloudVideointelligenceV1_LabelFrameOut": "_videointelligence_355_GoogleCloudVideointelligenceV1_LabelFrameOut",
        "GoogleCloudVideointelligenceV1beta2_FaceSegmentIn": "_videointelligence_356_GoogleCloudVideointelligenceV1beta2_FaceSegmentIn",
        "GoogleCloudVideointelligenceV1beta2_FaceSegmentOut": "_videointelligence_357_GoogleCloudVideointelligenceV1beta2_FaceSegmentOut",
        "GoogleCloudVideointelligenceV1beta2_TextFrameIn": "_videointelligence_358_GoogleCloudVideointelligenceV1beta2_TextFrameIn",
        "GoogleCloudVideointelligenceV1beta2_TextFrameOut": "_videointelligence_359_GoogleCloudVideointelligenceV1beta2_TextFrameOut",
        "GoogleCloudVideointelligenceV1p1beta1_TextFrameIn": "_videointelligence_360_GoogleCloudVideointelligenceV1p1beta1_TextFrameIn",
        "GoogleCloudVideointelligenceV1p1beta1_TextFrameOut": "_videointelligence_361_GoogleCloudVideointelligenceV1p1beta1_TextFrameOut",
        "GoogleCloudVideointelligenceV1p1beta1_EntityIn": "_videointelligence_362_GoogleCloudVideointelligenceV1p1beta1_EntityIn",
        "GoogleCloudVideointelligenceV1p1beta1_EntityOut": "_videointelligence_363_GoogleCloudVideointelligenceV1p1beta1_EntityOut",
        "GoogleCloudVideointelligenceV1beta2_DetectedAttributeIn": "_videointelligence_364_GoogleCloudVideointelligenceV1beta2_DetectedAttributeIn",
        "GoogleCloudVideointelligenceV1beta2_DetectedAttributeOut": "_videointelligence_365_GoogleCloudVideointelligenceV1beta2_DetectedAttributeOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types[
        "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationIn"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameIn"
                    ]
                )
            ).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationOut"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationOut"]
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
    types["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxIn"] = t.struct(
        {
            "top": t.number().optional(),
            "bottom": t.number().optional(),
            "right": t.number().optional(),
            "left": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxIn"])
    types["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxOut"] = t.struct(
        {
            "top": t.number().optional(),
            "bottom": t.number().optional(),
            "right": t.number().optional(),
            "left": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxOut"])
    types[
        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationIn"
    ] = t.struct(
        {
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_EntityIn"]
            ).optional(),
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrameIn"
                    ]
                )
            ).optional(),
            "confidence": t.number().optional(),
            "trackId": t.string().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"]
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationOut"
    ] = t.struct(
        {
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_EntityOut"]
            ).optional(),
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingFrameOut"
                    ]
                )
            ).optional(),
            "confidence": t.number().optional(),
            "trackId": t.string().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"]
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationIn"] = t.struct(
        {
            "thumbnail": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_FaceSegmentIn"])
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_FaceFrameIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationOut"] = t.struct(
        {
            "thumbnail": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_FaceSegmentOut"])
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_FaceFrameOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationOut"])
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
    types["GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxIn"] = t.struct(
        {
            "right": t.number().optional(),
            "left": t.number().optional(),
            "bottom": t.number().optional(),
            "top": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxOut"] = t.struct(
        {
            "right": t.number().optional(),
            "left": t.number().optional(),
            "bottom": t.number().optional(),
            "top": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "name": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "name": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkIn"] = t.struct(
        {
            "point": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_NormalizedVertexIn"]
            ).optional(),
            "name": t.string().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkOut"] = t.struct(
        {
            "point": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_NormalizedVertexOut"]
            ).optional(),
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_TrackIn"] = t.struct(
        {
            "timestampedObjects": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_TimestampedObjectIn"]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"]
            ).optional(),
            "attributes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeIn"]
                )
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TrackIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_TrackOut"] = t.struct(
        {
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
            "attributes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeOut"
                    ]
                )
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TrackOut"])
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
    types["GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkIn"] = t.struct(
        {
            "point": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkOut"] = t.struct(
        {
            "point": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkOut"])
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
    types["GoogleCloudVideointelligenceV1p3beta1_CelebrityIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_CelebrityIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_CelebrityOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_CelebrityOut"])
    types["GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationIn"] = t.struct(
        {
            "frames": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameIn"]
                )
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_EntityIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "version": t.string().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"]
            ).optional(),
            "trackId": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationIn"])
    types["GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationOut"] = t.struct(
        {
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameOut"
                    ]
                )
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_EntityOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "version": t.string().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"]
            ).optional(),
            "trackId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_TextAnnotationIn"] = t.struct(
        {
            "version": t.string().optional(),
            "text": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TextSegmentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_TextAnnotationIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_TextAnnotationOut"] = t.struct(
        {
            "version": t.string().optional(),
            "text": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TextSegmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_TextAnnotationOut"])
    types["GoogleCloudVideointelligenceV1_WordInfoIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "word": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_WordInfoIn"])
    types["GoogleCloudVideointelligenceV1_WordInfoOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "endTime": t.string().optional(),
            "word": t.string().optional(),
            "speakerTag": t.integer().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_WordInfoOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationIn"] = t.struct(
        {
            "thumbnail": t.string().optional(),
            "version": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_TrackIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationIn"])
    types[
        "GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationOut"
    ] = t.struct(
        {
            "thumbnail": t.string().optional(),
            "version": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_TrackOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationOut"]
    )
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
    types[
        "GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResultsIn"
    ] = t.struct(
        {
            "frameTimestamp": t.string().optional(),
            "shotAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"])
            ).optional(),
            "labelAnnotations": t.array(
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
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationIn"
                ]
            ).optional(),
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
            "frameTimestamp": t.string().optional(),
            "shotAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"]
                )
            ).optional(),
            "labelAnnotations": t.array(
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
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudVideointelligenceV1p3beta1_StreamingVideoAnnotationResultsOut"
        ]
    )
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
    types["GoogleCloudVideointelligenceV1_FaceFrameIn"] = t.struct(
        {
            "normalizedBoundingBoxes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_NormalizedBoundingBoxIn"]
                )
            ).optional(),
            "timeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_FaceFrameIn"])
    types["GoogleCloudVideointelligenceV1_FaceFrameOut"] = t.struct(
        {
            "normalizedBoundingBoxes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_NormalizedBoundingBoxOut"]
                )
            ).optional(),
            "timeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_FaceFrameOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_TrackIn"] = t.struct(
        {
            "timestampedObjects": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_TimestampedObjectIn"]
                )
            ).optional(),
            "attributes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeIn"]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"]
            ).optional(),
            "confidence": t.number().optional(),
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
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_TrackOut"])
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
    types["GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgressIn"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"]
            ).optional(),
            "inputUri": t.string().optional(),
            "feature": t.string().optional(),
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgressIn"])
    types[
        "GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgressOut"
    ] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"]
            ).optional(),
            "inputUri": t.string().optional(),
            "feature": t.string().optional(),
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationProgressOut"]
    )
    types["GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigIn"] = t.struct(
        {
            "languageCode": t.string(),
            "enableAutomaticPunctuation": t.boolean().optional(),
            "maxAlternatives": t.integer().optional(),
            "filterProfanity": t.boolean().optional(),
            "audioTracks": t.array(t.integer()).optional(),
            "enableWordConfidence": t.boolean().optional(),
            "speechContexts": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_SpeechContextIn"])
            ).optional(),
            "diarizationSpeakerCount": t.integer().optional(),
            "enableSpeakerDiarization": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigIn"])
    types["GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigOut"] = t.struct(
        {
            "languageCode": t.string(),
            "enableAutomaticPunctuation": t.boolean().optional(),
            "maxAlternatives": t.integer().optional(),
            "filterProfanity": t.boolean().optional(),
            "audioTracks": t.array(t.integer()).optional(),
            "enableWordConfidence": t.boolean().optional(),
            "speechContexts": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_SpeechContextOut"])
            ).optional(),
            "diarizationSpeakerCount": t.integer().optional(),
            "enableSpeakerDiarization": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigOut"])
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
    types["GoogleCloudVideointelligenceV1_FaceDetectionConfigIn"] = t.struct(
        {
            "model": t.string().optional(),
            "includeAttributes": t.boolean().optional(),
            "includeBoundingBoxes": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_FaceDetectionConfigIn"])
    types["GoogleCloudVideointelligenceV1_FaceDetectionConfigOut"] = t.struct(
        {
            "model": t.string().optional(),
            "includeAttributes": t.boolean().optional(),
            "includeBoundingBoxes": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_FaceDetectionConfigOut"])
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
    types["GoogleCloudVideointelligenceV1p1beta1_TimestampedObjectIn"] = t.struct(
        {
            "attributes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeIn"]
                )
            ).optional(),
            "landmarks": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkIn"]
                )
            ).optional(),
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxIn"]
            ).optional(),
            "timeOffset": t.string().optional(),
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
            "landmarks": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_DetectedLandmarkOut"]
                )
            ).optional(),
            "normalizedBoundingBox": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxOut"
                ]
            ).optional(),
            "timeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_TimestampedObjectOut"])
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
    types["GoogleCloudVideointelligenceV1_DetectedAttributeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_DetectedAttributeIn"])
    types["GoogleCloudVideointelligenceV1_DetectedAttributeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_DetectedAttributeOut"])
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
    types["GoogleCloudVideointelligenceV1_VideoAnnotationResultsIn"] = t.struct(
        {
            "speechTranscriptions": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_SpeechTranscriptionIn"])
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames["GoogleCloudVideointelligenceV1_ExplicitContentAnnotationIn"]
            ).optional(),
            "frameLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationIn"])
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_FaceAnnotationIn"])
            ).optional(),
            "segmentLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationIn"])
            ).optional(),
            "inputUri": t.string().optional(),
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationIn"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TextAnnotationIn"])
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationIn"]
                )
            ).optional(),
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationIn"])
            ).optional(),
            "personDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1_PersonDetectionAnnotationIn"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["GoogleRpc_StatusIn"]).optional(),
            "shotAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_VideoSegmentIn"])
            ).optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1_LogoRecognitionAnnotationIn"
                    ]
                )
            ).optional(),
            "shotLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationIn"])
            ).optional(),
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_FaceDetectionAnnotationIn"]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_VideoAnnotationResultsIn"])
    types["GoogleCloudVideointelligenceV1_VideoAnnotationResultsOut"] = t.struct(
        {
            "speechTranscriptions": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_SpeechTranscriptionOut"]
                )
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames["GoogleCloudVideointelligenceV1_ExplicitContentAnnotationOut"]
            ).optional(),
            "frameLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationOut"])
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_FaceAnnotationOut"])
            ).optional(),
            "segmentLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationOut"])
            ).optional(),
            "inputUri": t.string().optional(),
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationOut"])
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TextAnnotationOut"])
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationOut"
                    ]
                )
            ).optional(),
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationOut"])
            ).optional(),
            "personDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1_PersonDetectionAnnotationOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "shotAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_VideoSegmentOut"])
            ).optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1_LogoRecognitionAnnotationOut"
                    ]
                )
            ).optional(),
            "shotLabelAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelAnnotationOut"])
            ).optional(),
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_FaceDetectionAnnotationOut"]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_VideoAnnotationResultsOut"])
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
    types["GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameIn"] = t.struct(
        {
            "pornographyLikelihood": t.string().optional(),
            "timeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameOut"] = t.struct(
        {
            "pornographyLikelihood": t.string().optional(),
            "timeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_ExplicitContentFrameOut"])
    types["GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentIn"]
            ).optional(),
            "trackId": t.string().optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_ObjectTrackingFrameIn"])
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1_EntityIn"]
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationIn"])
    types["GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentOut"]
            ).optional(),
            "trackId": t.string().optional(),
            "frames": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1_ObjectTrackingFrameOut"]
                )
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1_EntityOut"]
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_ObjectTrackingAnnotationOut"])
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
    types["GoogleCloudVideointelligenceV1beta2_TextAnnotationIn"] = t.struct(
        {
            "text": t.string().optional(),
            "version": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TextSegmentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_TextAnnotationIn"])
    types["GoogleCloudVideointelligenceV1beta2_TextAnnotationOut"] = t.struct(
        {
            "text": t.string().optional(),
            "version": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TextSegmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_TextAnnotationOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_DetectedAttributeOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgressIn"] = t.struct(
        {
            "inputUri": t.string().optional(),
            "feature": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "startTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgressIn"])
    types[
        "GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgressOut"
    ] = t.struct(
        {
            "inputUri": t.string().optional(),
            "feature": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "startTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationProgressOut"]
    )
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
    types["GoogleCloudVideointelligenceV1_FaceDetectionAnnotationIn"] = t.struct(
        {
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TrackIn"])
            ).optional(),
            "thumbnail": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_FaceDetectionAnnotationIn"])
    types["GoogleCloudVideointelligenceV1_FaceDetectionAnnotationOut"] = t.struct(
        {
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TrackOut"])
            ).optional(),
            "thumbnail": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_FaceDetectionAnnotationOut"])
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
    types[
        "GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationIn"
    ] = t.struct(
        {
            "trackId": t.string().optional(),
            "confidence": t.number().optional(),
            "version": t.string().optional(),
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
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_EntityIn"]
            ).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationOut"
    ] = t.struct(
        {
            "trackId": t.string().optional(),
            "confidence": t.number().optional(),
            "version": t.string().optional(),
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
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_EntityOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1beta2_EntityIn"] = t.struct(
        {
            "entityId": t.string().optional(),
            "languageCode": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_EntityIn"])
    types["GoogleCloudVideointelligenceV1beta2_EntityOut"] = t.struct(
        {
            "entityId": t.string().optional(),
            "languageCode": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_EntityOut"])
    types[
        "GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotationIn"
    ] = t.struct(
        {
            "celebrityTracks": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackIn"]
                )
            ).optional(),
            "version": t.string().optional(),
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
            "celebrityTracks": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackOut"]
                )
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotationOut"
        ]
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
    types["GoogleCloudVideointelligenceV1_LabelDetectionConfigIn"] = t.struct(
        {
            "model": t.string().optional(),
            "videoConfidenceThreshold": t.number().optional(),
            "frameConfidenceThreshold": t.number().optional(),
            "stationaryCamera": t.boolean().optional(),
            "labelDetectionMode": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_LabelDetectionConfigIn"])
    types["GoogleCloudVideointelligenceV1_LabelDetectionConfigOut"] = t.struct(
        {
            "model": t.string().optional(),
            "videoConfidenceThreshold": t.number().optional(),
            "frameConfidenceThreshold": t.number().optional(),
            "stationaryCamera": t.boolean().optional(),
            "labelDetectionMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_LabelDetectionConfigOut"])
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
    types["GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexIn"] = t.struct(
        {"y": t.number().optional(), "x": t.number().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexOut"] = t.struct(
        {
            "y": t.number().optional(),
            "x": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedVertexOut"])
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
    types["GoogleProtobuf_EmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobuf_EmptyIn"]
    )
    types["GoogleProtobuf_EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobuf_EmptyOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackIn"] = t.struct(
        {
            "celebrities": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrityIn"
                    ]
                )
            ).optional(),
            "faceTrack": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_TrackIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackOut"] = t.struct(
        {
            "celebrities": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_RecognizedCelebrityOut"
                    ]
                )
            ).optional(),
            "faceTrack": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_TrackOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_CelebrityTrackOut"])
    types["GoogleCloudVideointelligenceV1_TextSegmentIn"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TextFrameIn"])
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentIn"]
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TextSegmentIn"])
    types["GoogleCloudVideointelligenceV1_TextSegmentOut"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TextFrameOut"])
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TextSegmentOut"])
    types["GoogleCloudVideointelligenceV1beta2_TextSegmentIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TextFrameIn"])
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_TextSegmentIn"])
    types["GoogleCloudVideointelligenceV1beta2_TextSegmentOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TextFrameOut"])
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_TextSegmentOut"])
    types["GoogleLongrunning_CancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunning_CancelOperationRequestIn"])
    types["GoogleLongrunning_CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunning_CancelOperationRequestOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "endTimeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "endTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResultsIn"] = t.struct(
        {
            "frameLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "error": t.proxy(renames["GoogleRpc_StatusIn"]).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotationIn"
                    ]
                )
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotationIn"
                ]
            ).optional(),
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationIn"
                    ]
                )
            ).optional(),
            "speechTranscriptions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionIn"
                    ]
                )
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
            "textAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_TextAnnotationIn"]
                )
            ).optional(),
            "shotLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotationIn"
                    ]
                )
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationIn"]
                )
            ).optional(),
            "personDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationIn"
                    ]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"]
            ).optional(),
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResultsIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResultsOut"] = t.struct(
        {
            "frameLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotationOut"
                    ]
                )
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p1beta1_ExplicitContentAnnotationOut"
                ]
            ).optional(),
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationOut"
                    ]
                )
            ).optional(),
            "speechTranscriptions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionOut"
                    ]
                )
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
            "textAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_TextAnnotationOut"]
                )
            ).optional(),
            "shotLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotationOut"
                    ]
                )
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_FaceAnnotationOut"]
                )
            ).optional(),
            "personDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationOut"
                    ]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"]
            ).optional(),
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationOut"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_VideoAnnotationResultsOut"])
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
    types["GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameIn"])
    types["GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingBoxOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_ObjectTrackingFrameOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_LabelFrameIn"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_LabelSegmentIn"])
            ).optional(),
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_EntityIn"])
            ).optional(),
            "version": t.string().optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_EntityIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_LabelFrameOut"])
            ).optional(),
            "segments": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelSegmentOut"]
                )
            ).optional(),
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_EntityOut"])
            ).optional(),
            "version": t.string().optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_EntityOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkIn"] = t.struct(
        {
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "point": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_NormalizedVertexIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkOut"] = t.struct(
        {
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "point": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_NormalizedVertexOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkOut"])
    types["GoogleCloudVideointelligenceV1beta2_VideoAnnotationResultsIn"] = t.struct(
        {
            "shotLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationIn"]
                )
            ).optional(),
            "segmentLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationIn"]
                )
            ).optional(),
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationIn"]
                )
            ).optional(),
            "inputUri": t.string().optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationIn"
                    ]
                )
            ).optional(),
            "shotAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"])
            ).optional(),
            "speechTranscriptions": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionIn"]
                )
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotationIn"
                ]
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TextAnnotationIn"])
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_FaceAnnotationIn"])
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationIn"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["GoogleRpc_StatusIn"]).optional(),
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationIn"]
                )
            ).optional(),
            "frameLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationIn"]
                )
            ).optional(),
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotationIn"
                    ]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"]
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
            "shotLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationOut"]
                )
            ).optional(),
            "segmentLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationOut"]
                )
            ).optional(),
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationOut"]
                )
            ).optional(),
            "inputUri": t.string().optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationOut"
                    ]
                )
            ).optional(),
            "shotAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"])
            ).optional(),
            "speechTranscriptions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionOut"
                    ]
                )
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1beta2_ExplicitContentAnnotationOut"
                ]
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_TextAnnotationOut"]
                )
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_FaceAnnotationOut"]
                )
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_ObjectTrackingAnnotationOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationOut"]
                )
            ).optional(),
            "frameLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationOut"]
                )
            ).optional(),
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1beta2_FaceDetectionAnnotationOut"
                    ]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"]
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
    types["GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationIn"] = t.struct(
        {
            "version": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TrackIn"])
            ).optional(),
            "thumbnail": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationIn"])
    types[
        "GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationOut"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TrackOut"])
            ).optional(),
            "thumbnail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_FaceDetectionAnnotationOut"]
    )
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
            "timeOffset": t.string().optional(),
            "landmarks": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkIn"]
                )
            ).optional(),
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
            "timeOffset": t.string().optional(),
            "landmarks": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_DetectedLandmarkOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TimestampedObjectOut"])
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
    types["GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgressIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"]
            ).optional(),
            "updateTime": t.string().optional(),
            "inputUri": t.string().optional(),
            "feature": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgressIn"])
    types[
        "GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgressOut"
    ] = t.struct(
        {
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "inputUri": t.string().optional(),
            "feature": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationProgressOut"]
    )
    types["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"] = t.struct(
        {
            "endTimeOffset": t.string().optional(),
            "startTimeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"] = t.struct(
        {
            "endTimeOffset": t.string().optional(),
            "startTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"])
    types["GoogleLongrunning_OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["GoogleRpc_StatusIn"]).optional(),
        }
    ).named(renames["GoogleLongrunning_OperationIn"])
    types["GoogleLongrunning_OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunning_OperationOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"] = t.struct(
        {
            "endTimeOffset": t.string().optional(),
            "startTimeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"] = t.struct(
        {
            "endTimeOffset": t.string().optional(),
            "startTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"])
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
    types["GoogleCloudVideointelligenceV1_TrackIn"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentIn"]
            ).optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_DetectedAttributeIn"])
            ).optional(),
            "confidence": t.number().optional(),
            "timestampedObjects": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TimestampedObjectIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TrackIn"])
    types["GoogleCloudVideointelligenceV1_TrackOut"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentOut"]
            ).optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_DetectedAttributeOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "timestampedObjects": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TimestampedObjectOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TrackOut"])
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
        "GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternativeIn"
    ] = t.struct({"transcript": t.string().optional()}).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternativeIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternativeOut"
    ] = t.struct(
        {
            "words": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_WordInfoOut"])
            ).optional(),
            "transcript": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_SpeechRecognitionAlternativeOut"]
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
    types["GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgressIn"] = t.struct(
        {
            "inputUri": t.string().optional(),
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "updateTime": t.string().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"]
            ).optional(),
            "feature": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgressIn"])
    types["GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgressOut"] = t.struct(
        {
            "inputUri": t.string().optional(),
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "updateTime": t.string().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"]
            ).optional(),
            "feature": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_VideoAnnotationProgressOut"])
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
    types["GoogleCloudVideointelligenceV1p3beta1_TextSegmentIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_TextFrameIn"])
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_TextSegmentIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_TextSegmentOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_TextFrameOut"])
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_TextSegmentOut"])
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
    types["GoogleCloudVideointelligenceV1p2beta1_LabelSegmentIn"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"]
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_LabelSegmentIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_LabelSegmentOut"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_LabelSegmentOut"])
    types["GoogleCloudVideointelligenceV1_TimestampedObjectIn"] = t.struct(
        {
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1_NormalizedBoundingBoxIn"]
            ).optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_DetectedLandmarkIn"])
            ).optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_DetectedAttributeIn"])
            ).optional(),
            "timeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TimestampedObjectIn"])
    types["GoogleCloudVideointelligenceV1_TimestampedObjectOut"] = t.struct(
        {
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1_NormalizedBoundingBoxOut"]
            ).optional(),
            "landmarks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_DetectedLandmarkOut"])
            ).optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_DetectedAttributeOut"])
            ).optional(),
            "timeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TimestampedObjectOut"])
    types["GoogleCloudVideointelligenceV1_VideoAnnotationProgressIn"] = t.struct(
        {
            "inputUri": t.string().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentIn"]
            ).optional(),
            "progressPercent": t.integer().optional(),
            "feature": t.string().optional(),
            "updateTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_VideoAnnotationProgressIn"])
    types["GoogleCloudVideointelligenceV1_VideoAnnotationProgressOut"] = t.struct(
        {
            "inputUri": t.string().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoSegmentOut"]
            ).optional(),
            "progressPercent": t.integer().optional(),
            "feature": t.string().optional(),
            "updateTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_VideoAnnotationProgressOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_WordInfoIn"] = t.struct(
        {
            "word": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_WordInfoIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_WordInfoOut"] = t.struct(
        {
            "speakerTag": t.integer().optional(),
            "word": t.string().optional(),
            "startTime": t.string().optional(),
            "confidence": t.number().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_WordInfoOut"])
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
    types["GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationIn"] = t.struct(
        {
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_FaceSegmentIn"])
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_FaceFrameIn"])
            ).optional(),
            "thumbnail": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationOut"] = t.struct(
        {
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_FaceSegmentOut"])
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_FaceFrameOut"])
            ).optional(),
            "thumbnail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationOut"])
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
    types["GoogleCloudVideointelligenceV1beta2_WordInfoIn"] = t.struct(
        {
            "word": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_WordInfoIn"])
    types["GoogleCloudVideointelligenceV1beta2_WordInfoOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "word": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "speakerTag": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_WordInfoOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_TextFrameIn"] = t.struct(
        {
            "rotatedBoundingBox": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPolyIn"
                ]
            ).optional(),
            "timeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TextFrameIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_TextFrameOut"] = t.struct(
        {
            "rotatedBoundingBox": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingPolyOut"
                ]
            ).optional(),
            "timeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TextFrameOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_FaceFrameIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "normalizedBoundingBoxes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_FaceFrameIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_FaceFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "normalizedBoundingBoxes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_FaceFrameOut"])
    types["GoogleCloudVideointelligenceV1p1beta1_TextSegmentIn"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TextFrameIn"])
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"]
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_TextSegmentIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_TextSegmentOut"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TextFrameOut"])
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_TextSegmentOut"])
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
            "confidence": t.number().optional(),
            "trackId": t.string().optional(),
            "version": t.string().optional(),
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrameIn"
                    ]
                )
            ).optional(),
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
            "confidence": t.number().optional(),
            "trackId": t.string().optional(),
            "version": t.string().optional(),
            "frames": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingFrameOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingAnnotationOut"]
    )
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
    types["GoogleCloudVideointelligenceV1_PersonDetectionConfigIn"] = t.struct(
        {
            "includePoseLandmarks": t.boolean().optional(),
            "includeBoundingBoxes": t.boolean().optional(),
            "includeAttributes": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_PersonDetectionConfigIn"])
    types["GoogleCloudVideointelligenceV1_PersonDetectionConfigOut"] = t.struct(
        {
            "includePoseLandmarks": t.boolean().optional(),
            "includeBoundingBoxes": t.boolean().optional(),
            "includeAttributes": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_PersonDetectionConfigOut"])
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
    types["GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrameIn"] = t.struct(
        {
            "pornographyLikelihood": t.string().optional(),
            "timeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrameIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrameOut"] = t.struct(
        {
            "pornographyLikelihood": t.string().optional(),
            "timeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_ExplicitContentFrameOut"])
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
    types["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationIn"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_LabelFrameIn"])
            ).optional(),
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_EntityIn"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_LabelSegmentIn"])
            ).optional(),
            "version": t.string().optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_EntityIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationOut"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_LabelFrameOut"])
            ).optional(),
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_EntityOut"])
            ).optional(),
            "segments": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_LabelSegmentOut"]
                )
            ).optional(),
            "version": t.string().optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_EntityOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_LabelAnnotationOut"])
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
    types["GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxIn"] = t.struct(
        {
            "bottom": t.number().optional(),
            "left": t.number().optional(),
            "right": t.number().optional(),
            "top": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxOut"] = t.struct(
        {
            "bottom": t.number().optional(),
            "left": t.number().optional(),
            "right": t.number().optional(),
            "top": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_NormalizedBoundingBoxOut"])
    types["GoogleCloudVideointelligenceV1_SpeechRecognitionAlternativeIn"] = t.struct(
        {"transcript": t.string().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1_SpeechRecognitionAlternativeIn"])
    types["GoogleCloudVideointelligenceV1_SpeechRecognitionAlternativeOut"] = t.struct(
        {
            "words": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_WordInfoOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "transcript": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_SpeechRecognitionAlternativeOut"])
    types["GoogleRpc_StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleRpc_StatusIn"])
    types["GoogleRpc_StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpc_StatusOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_WordInfoIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "word": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_WordInfoIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_WordInfoOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "word": t.string().optional(),
            "endTime": t.string().optional(),
            "confidence": t.number().optional(),
            "speakerTag": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_WordInfoOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_TextSegmentIn"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_TextFrameIn"])
            ).optional(),
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TextSegmentIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_TextSegmentOut"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_TextFrameOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TextSegmentOut"])
    types["GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationIn"] = t.struct(
        {
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_EntityIn"]
            ).optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TrackIn"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationIn"])
    types[
        "GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationOut"
    ] = t.struct(
        {
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_EntityOut"]
            ).optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TrackOut"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1beta2_LogoRecognitionAnnotationOut"]
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
    types["GoogleCloudVideointelligenceV1p3beta1_EntityIn"] = t.struct(
        {
            "entityId": t.string().optional(),
            "languageCode": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_EntityIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_EntityOut"] = t.struct(
        {
            "entityId": t.string().optional(),
            "languageCode": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_EntityOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResultsIn"] = t.struct(
        {
            "faceAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationIn"]
                )
            ).optional(),
            "error": t.proxy(renames["GoogleRpc_StatusIn"]).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationIn"
                    ]
                )
            ).optional(),
            "celebrityRecognitionAnnotations": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotationIn"
                ]
            ).optional(),
            "personDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationIn"
                    ]
                )
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_TextAnnotationIn"]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"]
            ).optional(),
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "segmentLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "speechTranscriptions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionIn"
                    ]
                )
            ).optional(),
            "shotLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationIn"
                ]
            ).optional(),
            "inputUri": t.string().optional(),
            "frameLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "shotAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentIn"])
            ).optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotationIn"
                    ]
                )
            ).optional(),
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotationIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResultsIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResultsOut"] = t.struct(
        {
            "faceAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_ObjectTrackingAnnotationOut"
                    ]
                )
            ).optional(),
            "celebrityRecognitionAnnotations": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p3beta1_CelebrityRecognitionAnnotationOut"
                ]
            ).optional(),
            "personDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationOut"
                    ]
                )
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_TextAnnotationOut"]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"]
            ).optional(),
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "segmentLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "speechTranscriptions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_SpeechTranscriptionOut"
                    ]
                )
            ).optional(),
            "shotLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p3beta1_ExplicitContentAnnotationOut"
                ]
            ).optional(),
            "inputUri": t.string().optional(),
            "frameLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "shotAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_VideoSegmentOut"]
                )
            ).optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_LogoRecognitionAnnotationOut"
                    ]
                )
            ).optional(),
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_FaceDetectionAnnotationOut"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_VideoAnnotationResultsOut"])
    types[
        "GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationIn"
    ] = t.struct(
        {
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TrackIn"])
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationOut"
    ] = t.struct(
        {
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TrackOut"])
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_PersonDetectionAnnotationOut"]
    )
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
    types["GoogleCloudVideointelligenceV1p1beta1_LabelSegmentIn"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"]
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_LabelSegmentIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_LabelSegmentOut"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_LabelSegmentOut"])
    types["GoogleCloudVideointelligenceV1beta2_LabelSegmentIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_LabelSegmentIn"])
    types["GoogleCloudVideointelligenceV1beta2_LabelSegmentOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_LabelSegmentOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_FaceFrameIn"] = t.struct(
        {
            "normalizedBoundingBoxes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxIn"
                    ]
                )
            ).optional(),
            "timeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_FaceFrameIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_FaceFrameOut"] = t.struct(
        {
            "normalizedBoundingBoxes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxOut"
                    ]
                )
            ).optional(),
            "timeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_FaceFrameOut"])
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
    types["GoogleCloudVideointelligenceV1_TextFrameIn"] = t.struct(
        {
            "rotatedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1_NormalizedBoundingPolyIn"]
            ).optional(),
            "timeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TextFrameIn"])
    types["GoogleCloudVideointelligenceV1_TextFrameOut"] = t.struct(
        {
            "rotatedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1_NormalizedBoundingPolyOut"]
            ).optional(),
            "timeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TextFrameOut"])
    types["GoogleCloudVideointelligenceV1_VideoContextIn"] = t.struct(
        {
            "labelDetectionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_LabelDetectionConfigIn"]
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_VideoSegmentIn"])
            ).optional(),
            "speechTranscriptionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigIn"]
            ).optional(),
            "shotChangeDetectionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigIn"]
            ).optional(),
            "objectTrackingConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_ObjectTrackingConfigIn"]
            ).optional(),
            "textDetectionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_TextDetectionConfigIn"]
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
        }
    ).named(renames["GoogleCloudVideointelligenceV1_VideoContextIn"])
    types["GoogleCloudVideointelligenceV1_VideoContextOut"] = t.struct(
        {
            "labelDetectionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_LabelDetectionConfigOut"]
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_VideoSegmentOut"])
            ).optional(),
            "speechTranscriptionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_SpeechTranscriptionConfigOut"]
            ).optional(),
            "shotChangeDetectionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigOut"]
            ).optional(),
            "objectTrackingConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_ObjectTrackingConfigOut"]
            ).optional(),
            "textDetectionConfig": t.proxy(
                renames["GoogleCloudVideointelligenceV1_TextDetectionConfigOut"]
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
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_VideoContextOut"])
    types["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationIn"] = t.struct(
        {
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_EntityIn"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_LabelSegmentIn"])
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_LabelFrameIn"])
            ).optional(),
            "version": t.string().optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_EntityIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationOut"] = t.struct(
        {
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_EntityOut"])
            ).optional(),
            "segments": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelSegmentOut"]
                )
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_LabelFrameOut"])
            ).optional(),
            "version": t.string().optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_EntityOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationOut"])
    types["GoogleCloudVideointelligenceV1beta2_FaceAnnotationIn"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_FaceFrameIn"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_FaceSegmentIn"])
            ).optional(),
            "thumbnail": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_FaceAnnotationIn"])
    types["GoogleCloudVideointelligenceV1beta2_FaceAnnotationOut"] = t.struct(
        {
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_FaceFrameOut"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_FaceSegmentOut"])
            ).optional(),
            "thumbnail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_FaceAnnotationOut"])
    types["GoogleCloudVideointelligenceV1_TextAnnotationIn"] = t.struct(
        {
            "version": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TextSegmentIn"])
            ).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TextAnnotationIn"])
    types["GoogleCloudVideointelligenceV1_TextAnnotationOut"] = t.struct(
        {
            "version": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TextSegmentOut"])
            ).optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_TextAnnotationOut"])
    types["GoogleCloudVideointelligenceV1_SpeechContextIn"] = t.struct(
        {"phrases": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudVideointelligenceV1_SpeechContextIn"])
    types["GoogleCloudVideointelligenceV1_SpeechContextOut"] = t.struct(
        {
            "phrases": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_SpeechContextOut"])
    types["GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotationIn"] = t.struct(
        {
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TrackIn"])
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotationIn"])
    types[
        "GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotationOut"
    ] = t.struct(
        {
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_TrackOut"])
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1beta2_PersonDetectionAnnotationOut"]
    )
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
    types["GoogleCloudVideointelligenceV1p1beta1_TrackIn"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "attributes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeIn"]
                )
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
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "attributes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_DetectedAttributeOut"
                    ]
                )
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
    types["GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResultsIn"] = t.struct(
        {
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationIn"
                    ]
                )
            ).optional(),
            "shotAnnotations": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"])
            ).optional(),
            "personDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotationIn"
                    ]
                )
            ).optional(),
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_TextAnnotationIn"]
                )
            ).optional(),
            "shotLabelAnnotations": t.array(
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
            "error": t.proxy(renames["GoogleRpc_StatusIn"]).optional(),
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "segmentLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationIn"
                    ]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"]
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationIn"]
                )
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationIn"
                ]
            ).optional(),
            "frameLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationIn"]
                )
            ).optional(),
            "inputUri": t.string().optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResultsIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResultsOut"] = t.struct(
        {
            "faceDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_FaceDetectionAnnotationOut"
                    ]
                )
            ).optional(),
            "shotAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"]
                )
            ).optional(),
            "personDetectionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_PersonDetectionAnnotationOut"
                    ]
                )
            ).optional(),
            "segmentPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "textAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_TextAnnotationOut"]
                )
            ).optional(),
            "shotLabelAnnotations": t.array(
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
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "shotPresenceLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "segmentLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "objectAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingAnnotationOut"
                    ]
                )
            ).optional(),
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"]
            ).optional(),
            "faceAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_FaceAnnotationOut"]
                )
            ).optional(),
            "explicitAnnotation": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p2beta1_ExplicitContentAnnotationOut"
                ]
            ).optional(),
            "frameLabelAnnotations": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_LabelAnnotationOut"]
                )
            ).optional(),
            "inputUri": t.string().optional(),
            "logoRecognitionAnnotations": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationOut"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_VideoAnnotationResultsOut"])
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
    types["GoogleCloudVideointelligenceV1p3beta1_TimestampedObjectIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "attributes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeIn"]
                )
            ).optional(),
            "landmarks": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkIn"]
                )
            ).optional(),
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_TimestampedObjectIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_TimestampedObjectOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "attributes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p3beta1_DetectedAttributeOut"
                    ]
                )
            ).optional(),
            "landmarks": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p3beta1_DetectedLandmarkOut"]
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
    types["GoogleCloudVideointelligenceV1p1beta1_WordInfoIn"] = t.struct(
        {
            "word": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_WordInfoIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_WordInfoOut"] = t.struct(
        {
            "word": t.string().optional(),
            "speakerTag": t.integer().optional(),
            "endTime": t.string().optional(),
            "confidence": t.number().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_WordInfoOut"])
    types[
        "GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternativeIn"
    ] = t.struct({"transcript": t.string().optional()}).named(
        renames["GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternativeIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternativeOut"
    ] = t.struct(
        {
            "transcript": t.string().optional(),
            "words": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_WordInfoOut"])
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1beta2_SpeechRecognitionAlternativeOut"]
    )
    types["GoogleCloudVideointelligenceV1beta2_TrackIn"] = t.struct(
        {
            "segment": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"]
            ).optional(),
            "attributes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_DetectedAttributeIn"]
                )
            ).optional(),
            "timestampedObjects": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_TimestampedObjectIn"]
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
            "attributes": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_DetectedAttributeOut"]
                )
            ).optional(),
            "timestampedObjects": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1beta2_TimestampedObjectOut"]
                )
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_TrackOut"])
    types[
        "GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationIn"
    ] = t.struct(
        {
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_TrackIn"])
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationOut"
    ] = t.struct(
        {
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_TrackOut"])
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p3beta1_PersonDetectionAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrameIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "normalizedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrameIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "normalizedBoundingBox": t.proxy(
                renames[
                    "GoogleCloudVideointelligenceV1p2beta1_NormalizedBoundingBoxOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_ObjectTrackingFrameOut"])
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
            "languageCode": t.string().optional(),
            "alternatives": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionOut"])
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
    types[
        "GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationIn"
    ] = t.struct(
        {
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentIn"])
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_EntityIn"]
            ).optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_TrackIn"])
            ).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationOut"
    ] = t.struct(
        {
            "segments": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p2beta1_VideoSegmentOut"]
                )
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p2beta1_EntityOut"]
            ).optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_TrackOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p2beta1_LogoRecognitionAnnotationOut"]
    )
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
    types["GoogleCloudVideointelligenceV1_NormalizedBoundingBoxIn"] = t.struct(
        {
            "top": t.number().optional(),
            "bottom": t.number().optional(),
            "right": t.number().optional(),
            "left": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_NormalizedBoundingBoxIn"])
    types["GoogleCloudVideointelligenceV1_NormalizedBoundingBoxOut"] = t.struct(
        {
            "top": t.number().optional(),
            "bottom": t.number().optional(),
            "right": t.number().optional(),
            "left": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_NormalizedBoundingBoxOut"])
    types["GoogleCloudVideointelligenceV1beta2_DetectedLandmarkIn"] = t.struct(
        {
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "point": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_NormalizedVertexIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_DetectedLandmarkIn"])
    types["GoogleCloudVideointelligenceV1beta2_DetectedLandmarkOut"] = t.struct(
        {
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "point": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_NormalizedVertexOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_DetectedLandmarkOut"])
    types[
        "GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotationIn"
    ] = t.struct(
        {
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1p1beta1_EntityIn"]
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentIn"])
            ).optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TrackIn"])
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
            "segments": t.array(
                t.proxy(
                    renames["GoogleCloudVideointelligenceV1p1beta1_VideoSegmentOut"]
                )
            ).optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_TrackOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_LogoRecognitionAnnotationOut"]
    )
    types["GoogleCloudVideointelligenceV1_FaceAnnotationIn"] = t.struct(
        {
            "thumbnail": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_FaceSegmentIn"])
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_FaceFrameIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_FaceAnnotationIn"])
    types["GoogleCloudVideointelligenceV1_FaceAnnotationOut"] = t.struct(
        {
            "thumbnail": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_FaceSegmentOut"])
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_FaceFrameOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_FaceAnnotationOut"])
    types["GoogleCloudVideointelligenceV1_PersonDetectionAnnotationIn"] = t.struct(
        {
            "version": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TrackIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_PersonDetectionAnnotationIn"])
    types["GoogleCloudVideointelligenceV1_PersonDetectionAnnotationOut"] = t.struct(
        {
            "version": t.string().optional(),
            "tracks": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_TrackOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_PersonDetectionAnnotationOut"])
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
        "GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeIn"
    ] = t.struct({"transcript": t.string().optional()}).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeIn"]
    )
    types[
        "GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeOut"
    ] = t.struct(
        {
            "words": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p1beta1_WordInfoOut"])
            ).optional(),
            "transcript": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudVideointelligenceV1p1beta1_SpeechRecognitionAlternativeOut"]
    )
    types["GoogleCloudVideointelligenceV1beta2_LabelAnnotationIn"] = t.struct(
        {
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_LabelSegmentIn"])
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_EntityIn"]
            ).optional(),
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_EntityIn"])
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_LabelFrameIn"])
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationIn"])
    types["GoogleCloudVideointelligenceV1beta2_LabelAnnotationOut"] = t.struct(
        {
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_LabelSegmentOut"])
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_EntityOut"]
            ).optional(),
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_EntityOut"])
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1beta2_LabelFrameOut"])
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_LabelAnnotationOut"])
    types["GoogleCloudVideointelligenceV1_LabelAnnotationIn"] = t.struct(
        {
            "version": t.string().optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1_EntityIn"]
            ).optional(),
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_EntityIn"])
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelFrameIn"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelSegmentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_LabelAnnotationIn"])
    types["GoogleCloudVideointelligenceV1_LabelAnnotationOut"] = t.struct(
        {
            "version": t.string().optional(),
            "entity": t.proxy(
                renames["GoogleCloudVideointelligenceV1_EntityOut"]
            ).optional(),
            "categoryEntities": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_EntityOut"])
            ).optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelFrameOut"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1_LabelSegmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_LabelAnnotationOut"])
    types["GoogleCloudVideointelligenceV1_AnnotateVideoRequestIn"] = t.struct(
        {
            "outputUri": t.string().optional(),
            "locationId": t.string().optional(),
            "features": t.array(t.string()),
            "inputUri": t.string().optional(),
            "inputContent": t.string().optional(),
            "videoContext": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoContextIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_AnnotateVideoRequestIn"])
    types["GoogleCloudVideointelligenceV1_AnnotateVideoRequestOut"] = t.struct(
        {
            "outputUri": t.string().optional(),
            "locationId": t.string().optional(),
            "features": t.array(t.string()),
            "inputUri": t.string().optional(),
            "inputContent": t.string().optional(),
            "videoContext": t.proxy(
                renames["GoogleCloudVideointelligenceV1_VideoContextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_AnnotateVideoRequestOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxIn"] = t.struct(
        {
            "right": t.number().optional(),
            "bottom": t.number().optional(),
            "top": t.number().optional(),
            "left": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxOut"] = t.struct(
        {
            "right": t.number().optional(),
            "bottom": t.number().optional(),
            "top": t.number().optional(),
            "left": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_NormalizedBoundingBoxOut"])
    types["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "endTimeOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentIn"])
    types["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"] = t.struct(
        {
            "startTimeOffset": t.string().optional(),
            "endTimeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_VideoSegmentOut"])
    types["GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationIn"] = t.struct(
        {
            "thumbnail": t.string().optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_FaceFrameIn"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_FaceSegmentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationIn"])
    types["GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationOut"] = t.struct(
        {
            "thumbnail": t.string().optional(),
            "frames": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_FaceFrameOut"])
            ).optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p3beta1_FaceSegmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p3beta1_FaceAnnotationOut"])
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
    types["GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigIn"] = t.struct(
        {"model": t.string().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigIn"])
    types["GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigOut"] = t.struct(
        {
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_ShotChangeDetectionConfigOut"])
    types["GoogleCloudVideointelligenceV1_ObjectTrackingConfigIn"] = t.struct(
        {"model": t.string().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1_ObjectTrackingConfigIn"])
    types["GoogleCloudVideointelligenceV1_ObjectTrackingConfigOut"] = t.struct(
        {
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_ObjectTrackingConfigOut"])
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
    types["GoogleCloudVideointelligenceV1p2beta1_TextAnnotationIn"] = t.struct(
        {
            "version": t.string().optional(),
            "text": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_TextSegmentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TextAnnotationIn"])
    types["GoogleCloudVideointelligenceV1p2beta1_TextAnnotationOut"] = t.struct(
        {
            "version": t.string().optional(),
            "text": t.string().optional(),
            "segments": t.array(
                t.proxy(renames["GoogleCloudVideointelligenceV1p2beta1_TextSegmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p2beta1_TextAnnotationOut"])
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
    types["GoogleCloudVideointelligenceV1_LabelFrameIn"] = t.struct(
        {"confidence": t.number().optional(), "timeOffset": t.string().optional()}
    ).named(renames["GoogleCloudVideointelligenceV1_LabelFrameIn"])
    types["GoogleCloudVideointelligenceV1_LabelFrameOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "timeOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1_LabelFrameOut"])
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
    types["GoogleCloudVideointelligenceV1beta2_TextFrameIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "rotatedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_TextFrameIn"])
    types["GoogleCloudVideointelligenceV1beta2_TextFrameOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "rotatedBoundingBox": t.proxy(
                renames["GoogleCloudVideointelligenceV1beta2_NormalizedBoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_TextFrameOut"])
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
    types["GoogleCloudVideointelligenceV1p1beta1_EntityIn"] = t.struct(
        {
            "description": t.string().optional(),
            "languageCode": t.string().optional(),
            "entityId": t.string().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_EntityIn"])
    types["GoogleCloudVideointelligenceV1p1beta1_EntityOut"] = t.struct(
        {
            "description": t.string().optional(),
            "languageCode": t.string().optional(),
            "entityId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1p1beta1_EntityOut"])
    types["GoogleCloudVideointelligenceV1beta2_DetectedAttributeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_DetectedAttributeIn"])
    types["GoogleCloudVideointelligenceV1beta2_DetectedAttributeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudVideointelligenceV1beta2_DetectedAttributeOut"])

    functions = {}
    functions["operationsProjectsLocationsOperationsDelete"] = videointelligence.get(
        "v1/operations/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunning_OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsProjectsLocationsOperationsCancel"] = videointelligence.get(
        "v1/operations/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunning_OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsProjectsLocationsOperationsGet"] = videointelligence.get(
        "v1/operations/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunning_OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = videointelligence.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobuf_EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = videointelligence.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobuf_EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = videointelligence.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobuf_EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = videointelligence.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobuf_EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["videosAnnotate"] = videointelligence.post(
        "v1/videos:annotate",
        t.struct(
            {
                "outputUri": t.string().optional(),
                "locationId": t.string().optional(),
                "features": t.array(t.string()),
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

    return Import(
        importer="videointelligence",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
