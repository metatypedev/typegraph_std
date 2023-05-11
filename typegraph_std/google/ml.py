from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_ml() -> Import:
    ml = HTTPRuntime("https://ml.googleapis.com/")

    renames = {
        "ErrorResponse": "_ml_1_ErrorResponse",
        "GoogleCloudMlV1__AutomatedStoppingConfigIn": "_ml_2_GoogleCloudMlV1__AutomatedStoppingConfigIn",
        "GoogleCloudMlV1__AutomatedStoppingConfigOut": "_ml_3_GoogleCloudMlV1__AutomatedStoppingConfigOut",
        "GoogleApi__HttpBodyIn": "_ml_4_GoogleApi__HttpBodyIn",
        "GoogleApi__HttpBodyOut": "_ml_5_GoogleApi__HttpBodyOut",
        "GoogleCloudMlV1_Trial_ParameterIn": "_ml_6_GoogleCloudMlV1_Trial_ParameterIn",
        "GoogleCloudMlV1_Trial_ParameterOut": "_ml_7_GoogleCloudMlV1_Trial_ParameterOut",
        "GoogleCloudMlV1__MeasurementIn": "_ml_8_GoogleCloudMlV1__MeasurementIn",
        "GoogleCloudMlV1__MeasurementOut": "_ml_9_GoogleCloudMlV1__MeasurementOut",
        "GoogleCloudMlV1__CheckTrialEarlyStoppingStateResponseIn": "_ml_10_GoogleCloudMlV1__CheckTrialEarlyStoppingStateResponseIn",
        "GoogleCloudMlV1__CheckTrialEarlyStoppingStateResponseOut": "_ml_11_GoogleCloudMlV1__CheckTrialEarlyStoppingStateResponseOut",
        "GoogleCloudMlV1__RouteMapIn": "_ml_12_GoogleCloudMlV1__RouteMapIn",
        "GoogleCloudMlV1__RouteMapOut": "_ml_13_GoogleCloudMlV1__RouteMapOut",
        "GoogleCloudMlV1_StudyConfigParameterSpec_DoubleValueSpecIn": "_ml_14_GoogleCloudMlV1_StudyConfigParameterSpec_DoubleValueSpecIn",
        "GoogleCloudMlV1_StudyConfigParameterSpec_DoubleValueSpecOut": "_ml_15_GoogleCloudMlV1_StudyConfigParameterSpec_DoubleValueSpecOut",
        "GoogleIamV1__AuditLogConfigIn": "_ml_16_GoogleIamV1__AuditLogConfigIn",
        "GoogleIamV1__AuditLogConfigOut": "_ml_17_GoogleIamV1__AuditLogConfigOut",
        "GoogleCloudMlV1__GetConfigResponseIn": "_ml_18_GoogleCloudMlV1__GetConfigResponseIn",
        "GoogleCloudMlV1__GetConfigResponseOut": "_ml_19_GoogleCloudMlV1__GetConfigResponseOut",
        "GoogleCloudMlV1__ExplanationConfigIn": "_ml_20_GoogleCloudMlV1__ExplanationConfigIn",
        "GoogleCloudMlV1__ExplanationConfigOut": "_ml_21_GoogleCloudMlV1__ExplanationConfigOut",
        "GoogleCloudMlV1__ListJobsResponseIn": "_ml_22_GoogleCloudMlV1__ListJobsResponseIn",
        "GoogleCloudMlV1__ListJobsResponseOut": "_ml_23_GoogleCloudMlV1__ListJobsResponseOut",
        "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentDiscreteValueSpecIn": "_ml_24_GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentDiscreteValueSpecIn",
        "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentDiscreteValueSpecOut": "_ml_25_GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentDiscreteValueSpecOut",
        "GoogleCloudMlV1__JobIn": "_ml_26_GoogleCloudMlV1__JobIn",
        "GoogleCloudMlV1__JobOut": "_ml_27_GoogleCloudMlV1__JobOut",
        "GoogleLongrunning__OperationIn": "_ml_28_GoogleLongrunning__OperationIn",
        "GoogleLongrunning__OperationOut": "_ml_29_GoogleLongrunning__OperationOut",
        "GoogleIamV1__BindingIn": "_ml_30_GoogleIamV1__BindingIn",
        "GoogleIamV1__BindingOut": "_ml_31_GoogleIamV1__BindingOut",
        "GoogleCloudMlV1__DiskConfigIn": "_ml_32_GoogleCloudMlV1__DiskConfigIn",
        "GoogleCloudMlV1__DiskConfigOut": "_ml_33_GoogleCloudMlV1__DiskConfigOut",
        "GoogleCloudMlV1__ListTrialsResponseIn": "_ml_34_GoogleCloudMlV1__ListTrialsResponseIn",
        "GoogleCloudMlV1__ListTrialsResponseOut": "_ml_35_GoogleCloudMlV1__ListTrialsResponseOut",
        "GoogleCloudMlV1_AutomatedStoppingConfig_DecayCurveAutomatedStoppingConfigIn": "_ml_36_GoogleCloudMlV1_AutomatedStoppingConfig_DecayCurveAutomatedStoppingConfigIn",
        "GoogleCloudMlV1_AutomatedStoppingConfig_DecayCurveAutomatedStoppingConfigOut": "_ml_37_GoogleCloudMlV1_AutomatedStoppingConfig_DecayCurveAutomatedStoppingConfigOut",
        "GoogleCloudMlV1__CompleteTrialRequestIn": "_ml_38_GoogleCloudMlV1__CompleteTrialRequestIn",
        "GoogleCloudMlV1__CompleteTrialRequestOut": "_ml_39_GoogleCloudMlV1__CompleteTrialRequestOut",
        "GoogleCloudMlV1__SampledShapleyAttributionIn": "_ml_40_GoogleCloudMlV1__SampledShapleyAttributionIn",
        "GoogleCloudMlV1__SampledShapleyAttributionOut": "_ml_41_GoogleCloudMlV1__SampledShapleyAttributionOut",
        "GoogleIamV1__TestIamPermissionsRequestIn": "_ml_42_GoogleIamV1__TestIamPermissionsRequestIn",
        "GoogleIamV1__TestIamPermissionsRequestOut": "_ml_43_GoogleIamV1__TestIamPermissionsRequestOut",
        "GoogleCloudMlV1__HyperparameterOutputIn": "_ml_44_GoogleCloudMlV1__HyperparameterOutputIn",
        "GoogleCloudMlV1__HyperparameterOutputOut": "_ml_45_GoogleCloudMlV1__HyperparameterOutputOut",
        "GoogleCloudMlV1__ListVersionsResponseIn": "_ml_46_GoogleCloudMlV1__ListVersionsResponseIn",
        "GoogleCloudMlV1__ListVersionsResponseOut": "_ml_47_GoogleCloudMlV1__ListVersionsResponseOut",
        "GoogleProtobuf__EmptyIn": "_ml_48_GoogleProtobuf__EmptyIn",
        "GoogleProtobuf__EmptyOut": "_ml_49_GoogleProtobuf__EmptyOut",
        "GoogleCloudMlV1__SuggestTrialsRequestIn": "_ml_50_GoogleCloudMlV1__SuggestTrialsRequestIn",
        "GoogleCloudMlV1__SuggestTrialsRequestOut": "_ml_51_GoogleCloudMlV1__SuggestTrialsRequestOut",
        "GoogleCloudMlV1__SchedulingIn": "_ml_52_GoogleCloudMlV1__SchedulingIn",
        "GoogleCloudMlV1__SchedulingOut": "_ml_53_GoogleCloudMlV1__SchedulingOut",
        "GoogleCloudMlV1__ListStudiesResponseIn": "_ml_54_GoogleCloudMlV1__ListStudiesResponseIn",
        "GoogleCloudMlV1__ListStudiesResponseOut": "_ml_55_GoogleCloudMlV1__ListStudiesResponseOut",
        "GoogleCloudMlV1__ReplicaConfigIn": "_ml_56_GoogleCloudMlV1__ReplicaConfigIn",
        "GoogleCloudMlV1__ReplicaConfigOut": "_ml_57_GoogleCloudMlV1__ReplicaConfigOut",
        "GoogleType__ExprIn": "_ml_58_GoogleType__ExprIn",
        "GoogleType__ExprOut": "_ml_59_GoogleType__ExprOut",
        "GoogleCloudMlV1__ModelIn": "_ml_60_GoogleCloudMlV1__ModelIn",
        "GoogleCloudMlV1__ModelOut": "_ml_61_GoogleCloudMlV1__ModelOut",
        "GoogleCloudMlV1__SuggestTrialsResponseIn": "_ml_62_GoogleCloudMlV1__SuggestTrialsResponseIn",
        "GoogleCloudMlV1__SuggestTrialsResponseOut": "_ml_63_GoogleCloudMlV1__SuggestTrialsResponseOut",
        "GoogleCloudMlV1__SetDefaultVersionRequestIn": "_ml_64_GoogleCloudMlV1__SetDefaultVersionRequestIn",
        "GoogleCloudMlV1__SetDefaultVersionRequestOut": "_ml_65_GoogleCloudMlV1__SetDefaultVersionRequestOut",
        "GoogleCloudMlV1__XraiAttributionIn": "_ml_66_GoogleCloudMlV1__XraiAttributionIn",
        "GoogleCloudMlV1__XraiAttributionOut": "_ml_67_GoogleCloudMlV1__XraiAttributionOut",
        "GoogleCloudMlV1_StudyConfigParameterSpec_IntegerValueSpecIn": "_ml_68_GoogleCloudMlV1_StudyConfigParameterSpec_IntegerValueSpecIn",
        "GoogleCloudMlV1_StudyConfigParameterSpec_IntegerValueSpecOut": "_ml_69_GoogleCloudMlV1_StudyConfigParameterSpec_IntegerValueSpecOut",
        "GoogleCloudMlV1__MetricSpecIn": "_ml_70_GoogleCloudMlV1__MetricSpecIn",
        "GoogleCloudMlV1__MetricSpecOut": "_ml_71_GoogleCloudMlV1__MetricSpecOut",
        "GoogleCloudMlV1_AutomatedStoppingConfig_MedianAutomatedStoppingConfigIn": "_ml_72_GoogleCloudMlV1_AutomatedStoppingConfig_MedianAutomatedStoppingConfigIn",
        "GoogleCloudMlV1_AutomatedStoppingConfig_MedianAutomatedStoppingConfigOut": "_ml_73_GoogleCloudMlV1_AutomatedStoppingConfig_MedianAutomatedStoppingConfigOut",
        "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentIntValueSpecIn": "_ml_74_GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentIntValueSpecIn",
        "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentIntValueSpecOut": "_ml_75_GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentIntValueSpecOut",
        "GoogleRpc__StatusIn": "_ml_76_GoogleRpc__StatusIn",
        "GoogleRpc__StatusOut": "_ml_77_GoogleRpc__StatusOut",
        "GoogleCloudMlV1__TrainingInputIn": "_ml_78_GoogleCloudMlV1__TrainingInputIn",
        "GoogleCloudMlV1__TrainingInputOut": "_ml_79_GoogleCloudMlV1__TrainingInputOut",
        "GoogleCloudMlV1__IntegratedGradientsAttributionIn": "_ml_80_GoogleCloudMlV1__IntegratedGradientsAttributionIn",
        "GoogleCloudMlV1__IntegratedGradientsAttributionOut": "_ml_81_GoogleCloudMlV1__IntegratedGradientsAttributionOut",
        "GoogleCloudMlV1__ListOptimalTrialsRequestIn": "_ml_82_GoogleCloudMlV1__ListOptimalTrialsRequestIn",
        "GoogleCloudMlV1__ListOptimalTrialsRequestOut": "_ml_83_GoogleCloudMlV1__ListOptimalTrialsRequestOut",
        "GoogleCloudMlV1_Measurement_MetricIn": "_ml_84_GoogleCloudMlV1_Measurement_MetricIn",
        "GoogleCloudMlV1_Measurement_MetricOut": "_ml_85_GoogleCloudMlV1_Measurement_MetricOut",
        "GoogleCloudMlV1__ParameterSpecIn": "_ml_86_GoogleCloudMlV1__ParameterSpecIn",
        "GoogleCloudMlV1__ParameterSpecOut": "_ml_87_GoogleCloudMlV1__ParameterSpecOut",
        "GoogleCloudMlV1_StudyConfig_ParameterSpecIn": "_ml_88_GoogleCloudMlV1_StudyConfig_ParameterSpecIn",
        "GoogleCloudMlV1_StudyConfig_ParameterSpecOut": "_ml_89_GoogleCloudMlV1_StudyConfig_ParameterSpecOut",
        "GoogleCloudMlV1__AcceleratorConfigIn": "_ml_90_GoogleCloudMlV1__AcceleratorConfigIn",
        "GoogleCloudMlV1__AcceleratorConfigOut": "_ml_91_GoogleCloudMlV1__AcceleratorConfigOut",
        "GoogleCloudMlV1__LocationIn": "_ml_92_GoogleCloudMlV1__LocationIn",
        "GoogleCloudMlV1__LocationOut": "_ml_93_GoogleCloudMlV1__LocationOut",
        "GoogleCloudMlV1__HyperparameterSpecIn": "_ml_94_GoogleCloudMlV1__HyperparameterSpecIn",
        "GoogleCloudMlV1__HyperparameterSpecOut": "_ml_95_GoogleCloudMlV1__HyperparameterSpecOut",
        "GoogleCloudMlV1__StudyConfigIn": "_ml_96_GoogleCloudMlV1__StudyConfigIn",
        "GoogleCloudMlV1__StudyConfigOut": "_ml_97_GoogleCloudMlV1__StudyConfigOut",
        "GoogleCloudMlV1__SuggestTrialsMetadataIn": "_ml_98_GoogleCloudMlV1__SuggestTrialsMetadataIn",
        "GoogleCloudMlV1__SuggestTrialsMetadataOut": "_ml_99_GoogleCloudMlV1__SuggestTrialsMetadataOut",
        "GoogleCloudMlV1__TrainingOutputIn": "_ml_100_GoogleCloudMlV1__TrainingOutputIn",
        "GoogleCloudMlV1__TrainingOutputOut": "_ml_101_GoogleCloudMlV1__TrainingOutputOut",
        "GoogleCloudMlV1__VersionIn": "_ml_102_GoogleCloudMlV1__VersionIn",
        "GoogleCloudMlV1__VersionOut": "_ml_103_GoogleCloudMlV1__VersionOut",
        "GoogleCloudMlV1__ConfigIn": "_ml_104_GoogleCloudMlV1__ConfigIn",
        "GoogleCloudMlV1__ConfigOut": "_ml_105_GoogleCloudMlV1__ConfigOut",
        "GoogleCloudMlV1__ListLocationsResponseIn": "_ml_106_GoogleCloudMlV1__ListLocationsResponseIn",
        "GoogleCloudMlV1__ListLocationsResponseOut": "_ml_107_GoogleCloudMlV1__ListLocationsResponseOut",
        "GoogleCloudMlV1__AddTrialMeasurementRequestIn": "_ml_108_GoogleCloudMlV1__AddTrialMeasurementRequestIn",
        "GoogleCloudMlV1__AddTrialMeasurementRequestOut": "_ml_109_GoogleCloudMlV1__AddTrialMeasurementRequestOut",
        "GoogleCloudMlV1__StopTrialRequestIn": "_ml_110_GoogleCloudMlV1__StopTrialRequestIn",
        "GoogleCloudMlV1__StopTrialRequestOut": "_ml_111_GoogleCloudMlV1__StopTrialRequestOut",
        "GoogleCloudMlV1__OperationMetadataIn": "_ml_112_GoogleCloudMlV1__OperationMetadataIn",
        "GoogleCloudMlV1__OperationMetadataOut": "_ml_113_GoogleCloudMlV1__OperationMetadataOut",
        "GoogleCloudMlV1__TrialIn": "_ml_114_GoogleCloudMlV1__TrialIn",
        "GoogleCloudMlV1__TrialOut": "_ml_115_GoogleCloudMlV1__TrialOut",
        "GoogleCloudMlV1__ContainerSpecIn": "_ml_116_GoogleCloudMlV1__ContainerSpecIn",
        "GoogleCloudMlV1__ContainerSpecOut": "_ml_117_GoogleCloudMlV1__ContainerSpecOut",
        "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentCategoricalValueSpecIn": "_ml_118_GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentCategoricalValueSpecIn",
        "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentCategoricalValueSpecOut": "_ml_119_GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentCategoricalValueSpecOut",
        "GoogleCloudMlV1__CheckTrialEarlyStoppingStateRequestIn": "_ml_120_GoogleCloudMlV1__CheckTrialEarlyStoppingStateRequestIn",
        "GoogleCloudMlV1__CheckTrialEarlyStoppingStateRequestOut": "_ml_121_GoogleCloudMlV1__CheckTrialEarlyStoppingStateRequestOut",
        "GoogleIamV1__TestIamPermissionsResponseIn": "_ml_122_GoogleIamV1__TestIamPermissionsResponseIn",
        "GoogleIamV1__TestIamPermissionsResponseOut": "_ml_123_GoogleIamV1__TestIamPermissionsResponseOut",
        "GoogleCloudMlV1_StudyConfigParameterSpec_CategoricalValueSpecIn": "_ml_124_GoogleCloudMlV1_StudyConfigParameterSpec_CategoricalValueSpecIn",
        "GoogleCloudMlV1_StudyConfigParameterSpec_CategoricalValueSpecOut": "_ml_125_GoogleCloudMlV1_StudyConfigParameterSpec_CategoricalValueSpecOut",
        "GoogleCloudMlV1_HyperparameterOutput_HyperparameterMetricIn": "_ml_126_GoogleCloudMlV1_HyperparameterOutput_HyperparameterMetricIn",
        "GoogleCloudMlV1_HyperparameterOutput_HyperparameterMetricOut": "_ml_127_GoogleCloudMlV1_HyperparameterOutput_HyperparameterMetricOut",
        "GoogleIamV1__SetIamPolicyRequestIn": "_ml_128_GoogleIamV1__SetIamPolicyRequestIn",
        "GoogleIamV1__SetIamPolicyRequestOut": "_ml_129_GoogleIamV1__SetIamPolicyRequestOut",
        "GoogleCloudMlV1__PredictionOutputIn": "_ml_130_GoogleCloudMlV1__PredictionOutputIn",
        "GoogleCloudMlV1__PredictionOutputOut": "_ml_131_GoogleCloudMlV1__PredictionOutputOut",
        "GoogleIamV1__AuditConfigIn": "_ml_132_GoogleIamV1__AuditConfigIn",
        "GoogleIamV1__AuditConfigOut": "_ml_133_GoogleIamV1__AuditConfigOut",
        "GoogleCloudMlV1__CapabilityIn": "_ml_134_GoogleCloudMlV1__CapabilityIn",
        "GoogleCloudMlV1__CapabilityOut": "_ml_135_GoogleCloudMlV1__CapabilityOut",
        "GoogleCloudMlV1__RequestLoggingConfigIn": "_ml_136_GoogleCloudMlV1__RequestLoggingConfigIn",
        "GoogleCloudMlV1__RequestLoggingConfigOut": "_ml_137_GoogleCloudMlV1__RequestLoggingConfigOut",
        "GoogleCloudMlV1__CheckTrialEarlyStoppingStateMetatdataIn": "_ml_138_GoogleCloudMlV1__CheckTrialEarlyStoppingStateMetatdataIn",
        "GoogleCloudMlV1__CheckTrialEarlyStoppingStateMetatdataOut": "_ml_139_GoogleCloudMlV1__CheckTrialEarlyStoppingStateMetatdataOut",
        "GoogleCloudMlV1__PredictionInputIn": "_ml_140_GoogleCloudMlV1__PredictionInputIn",
        "GoogleCloudMlV1__PredictionInputOut": "_ml_141_GoogleCloudMlV1__PredictionInputOut",
        "GoogleCloudMlV1_StudyConfigParameterSpec_DiscreteValueSpecIn": "_ml_142_GoogleCloudMlV1_StudyConfigParameterSpec_DiscreteValueSpecIn",
        "GoogleCloudMlV1_StudyConfigParameterSpec_DiscreteValueSpecOut": "_ml_143_GoogleCloudMlV1_StudyConfigParameterSpec_DiscreteValueSpecOut",
        "GoogleCloudMlV1__ManualScalingIn": "_ml_144_GoogleCloudMlV1__ManualScalingIn",
        "GoogleCloudMlV1__ManualScalingOut": "_ml_145_GoogleCloudMlV1__ManualScalingOut",
        "GoogleCloudMlV1__StudyIn": "_ml_146_GoogleCloudMlV1__StudyIn",
        "GoogleCloudMlV1__StudyOut": "_ml_147_GoogleCloudMlV1__StudyOut",
        "GoogleCloudMlV1_StudyConfig_MetricSpecIn": "_ml_148_GoogleCloudMlV1_StudyConfig_MetricSpecIn",
        "GoogleCloudMlV1_StudyConfig_MetricSpecOut": "_ml_149_GoogleCloudMlV1_StudyConfig_MetricSpecOut",
        "GoogleCloudMlV1__EncryptionConfigIn": "_ml_150_GoogleCloudMlV1__EncryptionConfigIn",
        "GoogleCloudMlV1__EncryptionConfigOut": "_ml_151_GoogleCloudMlV1__EncryptionConfigOut",
        "GoogleCloudMlV1__CancelJobRequestIn": "_ml_152_GoogleCloudMlV1__CancelJobRequestIn",
        "GoogleCloudMlV1__CancelJobRequestOut": "_ml_153_GoogleCloudMlV1__CancelJobRequestOut",
        "GoogleCloudMlV1__PredictRequestIn": "_ml_154_GoogleCloudMlV1__PredictRequestIn",
        "GoogleCloudMlV1__PredictRequestOut": "_ml_155_GoogleCloudMlV1__PredictRequestOut",
        "GoogleCloudMlV1__ListOptimalTrialsResponseIn": "_ml_156_GoogleCloudMlV1__ListOptimalTrialsResponseIn",
        "GoogleCloudMlV1__ListOptimalTrialsResponseOut": "_ml_157_GoogleCloudMlV1__ListOptimalTrialsResponseOut",
        "GoogleIamV1__PolicyIn": "_ml_158_GoogleIamV1__PolicyIn",
        "GoogleIamV1__PolicyOut": "_ml_159_GoogleIamV1__PolicyOut",
        "GoogleCloudMlV1__BuiltInAlgorithmOutputIn": "_ml_160_GoogleCloudMlV1__BuiltInAlgorithmOutputIn",
        "GoogleCloudMlV1__BuiltInAlgorithmOutputOut": "_ml_161_GoogleCloudMlV1__BuiltInAlgorithmOutputOut",
        "GoogleCloudMlV1__AutoScalingIn": "_ml_162_GoogleCloudMlV1__AutoScalingIn",
        "GoogleCloudMlV1__AutoScalingOut": "_ml_163_GoogleCloudMlV1__AutoScalingOut",
        "GoogleCloudMlV1__ContainerPortIn": "_ml_164_GoogleCloudMlV1__ContainerPortIn",
        "GoogleCloudMlV1__ContainerPortOut": "_ml_165_GoogleCloudMlV1__ContainerPortOut",
        "GoogleLongrunning__ListOperationsResponseIn": "_ml_166_GoogleLongrunning__ListOperationsResponseIn",
        "GoogleLongrunning__ListOperationsResponseOut": "_ml_167_GoogleLongrunning__ListOperationsResponseOut",
        "GoogleCloudMlV1__ListModelsResponseIn": "_ml_168_GoogleCloudMlV1__ListModelsResponseIn",
        "GoogleCloudMlV1__ListModelsResponseOut": "_ml_169_GoogleCloudMlV1__ListModelsResponseOut",
        "GoogleCloudMlV1__ExplainRequestIn": "_ml_170_GoogleCloudMlV1__ExplainRequestIn",
        "GoogleCloudMlV1__ExplainRequestOut": "_ml_171_GoogleCloudMlV1__ExplainRequestOut",
        "GoogleCloudMlV1__EnvVarIn": "_ml_172_GoogleCloudMlV1__EnvVarIn",
        "GoogleCloudMlV1__EnvVarOut": "_ml_173_GoogleCloudMlV1__EnvVarOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudMlV1__AutomatedStoppingConfigIn"] = t.struct(
        {
            "decayCurveStoppingConfig": t.proxy(
                renames[
                    "GoogleCloudMlV1_AutomatedStoppingConfig_DecayCurveAutomatedStoppingConfigIn"
                ]
            ),
            "medianAutomatedStoppingConfig": t.proxy(
                renames[
                    "GoogleCloudMlV1_AutomatedStoppingConfig_MedianAutomatedStoppingConfigIn"
                ]
            ),
        }
    ).named(renames["GoogleCloudMlV1__AutomatedStoppingConfigIn"])
    types["GoogleCloudMlV1__AutomatedStoppingConfigOut"] = t.struct(
        {
            "decayCurveStoppingConfig": t.proxy(
                renames[
                    "GoogleCloudMlV1_AutomatedStoppingConfig_DecayCurveAutomatedStoppingConfigOut"
                ]
            ),
            "medianAutomatedStoppingConfig": t.proxy(
                renames[
                    "GoogleCloudMlV1_AutomatedStoppingConfig_MedianAutomatedStoppingConfigOut"
                ]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__AutomatedStoppingConfigOut"])
    types["GoogleApi__HttpBodyIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "data": t.string().optional(),
        }
    ).named(renames["GoogleApi__HttpBodyIn"])
    types["GoogleApi__HttpBodyOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApi__HttpBodyOut"])
    types["GoogleCloudMlV1_Trial_ParameterIn"] = t.struct(
        {
            "parameter": t.string().optional(),
            "intValue": t.string().optional(),
            "stringValue": t.string().optional(),
            "floatValue": t.number().optional(),
        }
    ).named(renames["GoogleCloudMlV1_Trial_ParameterIn"])
    types["GoogleCloudMlV1_Trial_ParameterOut"] = t.struct(
        {
            "parameter": t.string().optional(),
            "intValue": t.string().optional(),
            "stringValue": t.string().optional(),
            "floatValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1_Trial_ParameterOut"])
    types["GoogleCloudMlV1__MeasurementIn"] = t.struct(
        {
            "elapsedTime": t.string().optional(),
            "stepCount": t.string().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudMlV1_Measurement_MetricIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudMlV1__MeasurementIn"])
    types["GoogleCloudMlV1__MeasurementOut"] = t.struct(
        {
            "elapsedTime": t.string().optional(),
            "stepCount": t.string().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudMlV1_Measurement_MetricOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__MeasurementOut"])
    types["GoogleCloudMlV1__CheckTrialEarlyStoppingStateResponseIn"] = t.struct(
        {
            "shouldStop": t.boolean().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudMlV1__CheckTrialEarlyStoppingStateResponseIn"])
    types["GoogleCloudMlV1__CheckTrialEarlyStoppingStateResponseOut"] = t.struct(
        {
            "shouldStop": t.boolean().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__CheckTrialEarlyStoppingStateResponseOut"])
    types["GoogleCloudMlV1__RouteMapIn"] = t.struct(
        {"health": t.string().optional(), "predict": t.string().optional()}
    ).named(renames["GoogleCloudMlV1__RouteMapIn"])
    types["GoogleCloudMlV1__RouteMapOut"] = t.struct(
        {
            "health": t.string().optional(),
            "predict": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__RouteMapOut"])
    types["GoogleCloudMlV1_StudyConfigParameterSpec_DoubleValueSpecIn"] = t.struct(
        {"maxValue": t.number().optional(), "minValue": t.number().optional()}
    ).named(renames["GoogleCloudMlV1_StudyConfigParameterSpec_DoubleValueSpecIn"])
    types["GoogleCloudMlV1_StudyConfigParameterSpec_DoubleValueSpecOut"] = t.struct(
        {
            "maxValue": t.number().optional(),
            "minValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1_StudyConfigParameterSpec_DoubleValueSpecOut"])
    types["GoogleIamV1__AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamV1__AuditLogConfigIn"])
    types["GoogleIamV1__AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1__AuditLogConfigOut"])
    types["GoogleCloudMlV1__GetConfigResponseIn"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "config": t.proxy(renames["GoogleCloudMlV1__ConfigIn"]),
            "serviceAccountProject": t.string().optional(),
        }
    ).named(renames["GoogleCloudMlV1__GetConfigResponseIn"])
    types["GoogleCloudMlV1__GetConfigResponseOut"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "config": t.proxy(renames["GoogleCloudMlV1__ConfigOut"]),
            "serviceAccountProject": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__GetConfigResponseOut"])
    types["GoogleCloudMlV1__ExplanationConfigIn"] = t.struct(
        {
            "xraiAttribution": t.proxy(
                renames["GoogleCloudMlV1__XraiAttributionIn"]
            ).optional(),
            "sampledShapleyAttribution": t.proxy(
                renames["GoogleCloudMlV1__SampledShapleyAttributionIn"]
            ).optional(),
            "integratedGradientsAttribution": t.proxy(
                renames["GoogleCloudMlV1__IntegratedGradientsAttributionIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ExplanationConfigIn"])
    types["GoogleCloudMlV1__ExplanationConfigOut"] = t.struct(
        {
            "xraiAttribution": t.proxy(
                renames["GoogleCloudMlV1__XraiAttributionOut"]
            ).optional(),
            "sampledShapleyAttribution": t.proxy(
                renames["GoogleCloudMlV1__SampledShapleyAttributionOut"]
            ).optional(),
            "integratedGradientsAttribution": t.proxy(
                renames["GoogleCloudMlV1__IntegratedGradientsAttributionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ExplanationConfigOut"])
    types["GoogleCloudMlV1__ListJobsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobs": t.array(t.proxy(renames["GoogleCloudMlV1__JobIn"])).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ListJobsResponseIn"])
    types["GoogleCloudMlV1__ListJobsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobs": t.array(t.proxy(renames["GoogleCloudMlV1__JobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ListJobsResponseOut"])
    types[
        "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentDiscreteValueSpecIn"
    ] = t.struct({"values": t.array(t.number()).optional()}).named(
        renames[
            "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentDiscreteValueSpecIn"
        ]
    )
    types[
        "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentDiscreteValueSpecOut"
    ] = t.struct(
        {
            "values": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentDiscreteValueSpecOut"
        ]
    )
    types["GoogleCloudMlV1__JobIn"] = t.struct(
        {
            "jobId": t.string(),
            "predictionInput": t.proxy(
                renames["GoogleCloudMlV1__PredictionInputIn"]
            ).optional(),
            "state": t.string().optional(),
            "predictionOutput": t.proxy(
                renames["GoogleCloudMlV1__PredictionOutputIn"]
            ).optional(),
            "startTime": t.string().optional(),
            "trainingInput": t.proxy(
                renames["GoogleCloudMlV1__TrainingInputIn"]
            ).optional(),
            "etag": t.string().optional(),
            "errorMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "endTime": t.string().optional(),
            "trainingOutput": t.proxy(
                renames["GoogleCloudMlV1__TrainingOutputIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudMlV1__JobIn"])
    types["GoogleCloudMlV1__JobOut"] = t.struct(
        {
            "jobId": t.string(),
            "predictionInput": t.proxy(
                renames["GoogleCloudMlV1__PredictionInputOut"]
            ).optional(),
            "state": t.string().optional(),
            "predictionOutput": t.proxy(
                renames["GoogleCloudMlV1__PredictionOutputOut"]
            ).optional(),
            "jobPosition": t.string().optional(),
            "startTime": t.string().optional(),
            "trainingInput": t.proxy(
                renames["GoogleCloudMlV1__TrainingInputOut"]
            ).optional(),
            "etag": t.string().optional(),
            "errorMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "endTime": t.string().optional(),
            "trainingOutput": t.proxy(
                renames["GoogleCloudMlV1__TrainingOutputOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__JobOut"])
    types["GoogleLongrunning__OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["GoogleRpc__StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunning__OperationIn"])
    types["GoogleLongrunning__OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunning__OperationOut"])
    types["GoogleIamV1__BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["GoogleType__ExprIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["GoogleIamV1__BindingIn"])
    types["GoogleIamV1__BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["GoogleType__ExprOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1__BindingOut"])
    types["GoogleCloudMlV1__DiskConfigIn"] = t.struct(
        {
            "bootDiskSizeGb": t.integer().optional(),
            "bootDiskType": t.string().optional(),
        }
    ).named(renames["GoogleCloudMlV1__DiskConfigIn"])
    types["GoogleCloudMlV1__DiskConfigOut"] = t.struct(
        {
            "bootDiskSizeGb": t.integer().optional(),
            "bootDiskType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__DiskConfigOut"])
    types["GoogleCloudMlV1__ListTrialsResponseIn"] = t.struct(
        {"trials": t.array(t.proxy(renames["GoogleCloudMlV1__TrialIn"])).optional()}
    ).named(renames["GoogleCloudMlV1__ListTrialsResponseIn"])
    types["GoogleCloudMlV1__ListTrialsResponseOut"] = t.struct(
        {
            "trials": t.array(t.proxy(renames["GoogleCloudMlV1__TrialOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ListTrialsResponseOut"])
    types[
        "GoogleCloudMlV1_AutomatedStoppingConfig_DecayCurveAutomatedStoppingConfigIn"
    ] = t.struct({"useElapsedTime": t.boolean().optional()}).named(
        renames[
            "GoogleCloudMlV1_AutomatedStoppingConfig_DecayCurveAutomatedStoppingConfigIn"
        ]
    )
    types[
        "GoogleCloudMlV1_AutomatedStoppingConfig_DecayCurveAutomatedStoppingConfigOut"
    ] = t.struct(
        {
            "useElapsedTime": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudMlV1_AutomatedStoppingConfig_DecayCurveAutomatedStoppingConfigOut"
        ]
    )
    types["GoogleCloudMlV1__CompleteTrialRequestIn"] = t.struct(
        {
            "finalMeasurement": t.proxy(
                renames["GoogleCloudMlV1__MeasurementIn"]
            ).optional(),
            "trialInfeasible": t.boolean().optional(),
            "infeasibleReason": t.string().optional(),
        }
    ).named(renames["GoogleCloudMlV1__CompleteTrialRequestIn"])
    types["GoogleCloudMlV1__CompleteTrialRequestOut"] = t.struct(
        {
            "finalMeasurement": t.proxy(
                renames["GoogleCloudMlV1__MeasurementOut"]
            ).optional(),
            "trialInfeasible": t.boolean().optional(),
            "infeasibleReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__CompleteTrialRequestOut"])
    types["GoogleCloudMlV1__SampledShapleyAttributionIn"] = t.struct(
        {"numPaths": t.integer().optional()}
    ).named(renames["GoogleCloudMlV1__SampledShapleyAttributionIn"])
    types["GoogleCloudMlV1__SampledShapleyAttributionOut"] = t.struct(
        {
            "numPaths": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__SampledShapleyAttributionOut"])
    types["GoogleIamV1__TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1__TestIamPermissionsRequestIn"])
    types["GoogleIamV1__TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1__TestIamPermissionsRequestOut"])
    types["GoogleCloudMlV1__HyperparameterOutputIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "allMetrics": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudMlV1_HyperparameterOutput_HyperparameterMetricIn"
                    ]
                )
            ).optional(),
            "trialId": t.string().optional(),
            "isTrialStoppedEarly": t.boolean().optional(),
            "builtInAlgorithmOutput": t.proxy(
                renames["GoogleCloudMlV1__BuiltInAlgorithmOutputIn"]
            ).optional(),
            "state": t.string().optional(),
            "webAccessUris": t.struct({"_": t.string().optional()}).optional(),
            "finalMetric": t.proxy(
                renames["GoogleCloudMlV1_HyperparameterOutput_HyperparameterMetricIn"]
            ).optional(),
            "hyperparameters": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudMlV1__HyperparameterOutputIn"])
    types["GoogleCloudMlV1__HyperparameterOutputOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "allMetrics": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudMlV1_HyperparameterOutput_HyperparameterMetricOut"
                    ]
                )
            ).optional(),
            "trialId": t.string().optional(),
            "isTrialStoppedEarly": t.boolean().optional(),
            "builtInAlgorithmOutput": t.proxy(
                renames["GoogleCloudMlV1__BuiltInAlgorithmOutputOut"]
            ).optional(),
            "state": t.string().optional(),
            "webAccessUris": t.struct({"_": t.string().optional()}).optional(),
            "finalMetric": t.proxy(
                renames["GoogleCloudMlV1_HyperparameterOutput_HyperparameterMetricOut"]
            ).optional(),
            "hyperparameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__HyperparameterOutputOut"])
    types["GoogleCloudMlV1__ListVersionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "versions": t.array(
                t.proxy(renames["GoogleCloudMlV1__VersionIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ListVersionsResponseIn"])
    types["GoogleCloudMlV1__ListVersionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "versions": t.array(
                t.proxy(renames["GoogleCloudMlV1__VersionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ListVersionsResponseOut"])
    types["GoogleProtobuf__EmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobuf__EmptyIn"]
    )
    types["GoogleProtobuf__EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobuf__EmptyOut"])
    types["GoogleCloudMlV1__SuggestTrialsRequestIn"] = t.struct(
        {"suggestionCount": t.integer(), "clientId": t.string()}
    ).named(renames["GoogleCloudMlV1__SuggestTrialsRequestIn"])
    types["GoogleCloudMlV1__SuggestTrialsRequestOut"] = t.struct(
        {
            "suggestionCount": t.integer(),
            "clientId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__SuggestTrialsRequestOut"])
    types["GoogleCloudMlV1__SchedulingIn"] = t.struct(
        {
            "priority": t.integer().optional(),
            "maxRunningTime": t.string().optional(),
            "maxWaitTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudMlV1__SchedulingIn"])
    types["GoogleCloudMlV1__SchedulingOut"] = t.struct(
        {
            "priority": t.integer().optional(),
            "maxRunningTime": t.string().optional(),
            "maxWaitTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__SchedulingOut"])
    types["GoogleCloudMlV1__ListStudiesResponseIn"] = t.struct(
        {"studies": t.array(t.proxy(renames["GoogleCloudMlV1__StudyIn"])).optional()}
    ).named(renames["GoogleCloudMlV1__ListStudiesResponseIn"])
    types["GoogleCloudMlV1__ListStudiesResponseOut"] = t.struct(
        {
            "studies": t.array(
                t.proxy(renames["GoogleCloudMlV1__StudyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ListStudiesResponseOut"])
    types["GoogleCloudMlV1__ReplicaConfigIn"] = t.struct(
        {
            "diskConfig": t.proxy(renames["GoogleCloudMlV1__DiskConfigIn"]).optional(),
            "containerArgs": t.array(t.string()).optional(),
            "tpuTfVersion": t.string().optional(),
            "imageUri": t.string().optional(),
            "acceleratorConfig": t.proxy(
                renames["GoogleCloudMlV1__AcceleratorConfigIn"]
            ).optional(),
            "containerCommand": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ReplicaConfigIn"])
    types["GoogleCloudMlV1__ReplicaConfigOut"] = t.struct(
        {
            "diskConfig": t.proxy(renames["GoogleCloudMlV1__DiskConfigOut"]).optional(),
            "containerArgs": t.array(t.string()).optional(),
            "tpuTfVersion": t.string().optional(),
            "imageUri": t.string().optional(),
            "acceleratorConfig": t.proxy(
                renames["GoogleCloudMlV1__AcceleratorConfigOut"]
            ).optional(),
            "containerCommand": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ReplicaConfigOut"])
    types["GoogleType__ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["GoogleType__ExprIn"])
    types["GoogleType__ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleType__ExprOut"])
    types["GoogleCloudMlV1__ModelIn"] = t.struct(
        {
            "description": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "defaultVersion": t.proxy(renames["GoogleCloudMlV1__VersionIn"]).optional(),
            "onlinePredictionLogging": t.boolean().optional(),
            "onlinePredictionConsoleLogging": t.boolean().optional(),
            "regions": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ModelIn"])
    types["GoogleCloudMlV1__ModelOut"] = t.struct(
        {
            "description": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "defaultVersion": t.proxy(
                renames["GoogleCloudMlV1__VersionOut"]
            ).optional(),
            "onlinePredictionLogging": t.boolean().optional(),
            "onlinePredictionConsoleLogging": t.boolean().optional(),
            "regions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ModelOut"])
    types["GoogleCloudMlV1__SuggestTrialsResponseIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "trials": t.array(t.proxy(renames["GoogleCloudMlV1__TrialIn"])).optional(),
            "studyState": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudMlV1__SuggestTrialsResponseIn"])
    types["GoogleCloudMlV1__SuggestTrialsResponseOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "trials": t.array(t.proxy(renames["GoogleCloudMlV1__TrialOut"])).optional(),
            "studyState": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__SuggestTrialsResponseOut"])
    types["GoogleCloudMlV1__SetDefaultVersionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudMlV1__SetDefaultVersionRequestIn"])
    types["GoogleCloudMlV1__SetDefaultVersionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudMlV1__SetDefaultVersionRequestOut"])
    types["GoogleCloudMlV1__XraiAttributionIn"] = t.struct(
        {"numIntegralSteps": t.integer().optional()}
    ).named(renames["GoogleCloudMlV1__XraiAttributionIn"])
    types["GoogleCloudMlV1__XraiAttributionOut"] = t.struct(
        {
            "numIntegralSteps": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__XraiAttributionOut"])
    types["GoogleCloudMlV1_StudyConfigParameterSpec_IntegerValueSpecIn"] = t.struct(
        {"maxValue": t.string().optional(), "minValue": t.string().optional()}
    ).named(renames["GoogleCloudMlV1_StudyConfigParameterSpec_IntegerValueSpecIn"])
    types["GoogleCloudMlV1_StudyConfigParameterSpec_IntegerValueSpecOut"] = t.struct(
        {
            "maxValue": t.string().optional(),
            "minValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1_StudyConfigParameterSpec_IntegerValueSpecOut"])
    types["GoogleCloudMlV1__MetricSpecIn"] = t.struct(
        {"name": t.string().optional(), "target": t.integer().optional()}
    ).named(renames["GoogleCloudMlV1__MetricSpecIn"])
    types["GoogleCloudMlV1__MetricSpecOut"] = t.struct(
        {
            "name": t.string().optional(),
            "target": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__MetricSpecOut"])
    types[
        "GoogleCloudMlV1_AutomatedStoppingConfig_MedianAutomatedStoppingConfigIn"
    ] = t.struct({"useElapsedTime": t.boolean().optional()}).named(
        renames[
            "GoogleCloudMlV1_AutomatedStoppingConfig_MedianAutomatedStoppingConfigIn"
        ]
    )
    types[
        "GoogleCloudMlV1_AutomatedStoppingConfig_MedianAutomatedStoppingConfigOut"
    ] = t.struct(
        {
            "useElapsedTime": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudMlV1_AutomatedStoppingConfig_MedianAutomatedStoppingConfigOut"
        ]
    )
    types[
        "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentIntValueSpecIn"
    ] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames["GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentIntValueSpecIn"]
    )
    types[
        "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentIntValueSpecOut"
    ] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentIntValueSpecOut"
        ]
    )
    types["GoogleRpc__StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleRpc__StatusIn"])
    types["GoogleRpc__StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpc__StatusOut"])
    types["GoogleCloudMlV1__TrainingInputIn"] = t.struct(
        {
            "region": t.string(),
            "useChiefInTfConfig": t.boolean().optional(),
            "runtimeVersion": t.string().optional(),
            "parameterServerConfig": t.proxy(
                renames["GoogleCloudMlV1__ReplicaConfigIn"]
            ).optional(),
            "network": t.string().optional(),
            "workerConfig": t.proxy(
                renames["GoogleCloudMlV1__ReplicaConfigIn"]
            ).optional(),
            "encryptionConfig": t.proxy(
                renames["GoogleCloudMlV1__EncryptionConfigIn"]
            ).optional(),
            "enableWebAccess": t.boolean().optional(),
            "pythonModule": t.string(),
            "pythonVersion": t.string().optional(),
            "evaluatorType": t.string().optional(),
            "workerType": t.string().optional(),
            "jobDir": t.string().optional(),
            "parameterServerType": t.string().optional(),
            "masterType": t.string().optional(),
            "workerCount": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "hyperparameters": t.proxy(
                renames["GoogleCloudMlV1__HyperparameterSpecIn"]
            ).optional(),
            "evaluatorConfig": t.proxy(
                renames["GoogleCloudMlV1__ReplicaConfigIn"]
            ).optional(),
            "args": t.array(t.string()).optional(),
            "packageUris": t.array(t.string()),
            "evaluatorCount": t.string().optional(),
            "scheduling": t.proxy(renames["GoogleCloudMlV1__SchedulingIn"]).optional(),
            "masterConfig": t.proxy(
                renames["GoogleCloudMlV1__ReplicaConfigIn"]
            ).optional(),
            "parameterServerCount": t.string().optional(),
            "scaleTier": t.string(),
        }
    ).named(renames["GoogleCloudMlV1__TrainingInputIn"])
    types["GoogleCloudMlV1__TrainingInputOut"] = t.struct(
        {
            "region": t.string(),
            "useChiefInTfConfig": t.boolean().optional(),
            "runtimeVersion": t.string().optional(),
            "parameterServerConfig": t.proxy(
                renames["GoogleCloudMlV1__ReplicaConfigOut"]
            ).optional(),
            "network": t.string().optional(),
            "workerConfig": t.proxy(
                renames["GoogleCloudMlV1__ReplicaConfigOut"]
            ).optional(),
            "encryptionConfig": t.proxy(
                renames["GoogleCloudMlV1__EncryptionConfigOut"]
            ).optional(),
            "enableWebAccess": t.boolean().optional(),
            "pythonModule": t.string(),
            "pythonVersion": t.string().optional(),
            "evaluatorType": t.string().optional(),
            "workerType": t.string().optional(),
            "jobDir": t.string().optional(),
            "parameterServerType": t.string().optional(),
            "masterType": t.string().optional(),
            "workerCount": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "hyperparameters": t.proxy(
                renames["GoogleCloudMlV1__HyperparameterSpecOut"]
            ).optional(),
            "evaluatorConfig": t.proxy(
                renames["GoogleCloudMlV1__ReplicaConfigOut"]
            ).optional(),
            "args": t.array(t.string()).optional(),
            "packageUris": t.array(t.string()),
            "evaluatorCount": t.string().optional(),
            "scheduling": t.proxy(renames["GoogleCloudMlV1__SchedulingOut"]).optional(),
            "masterConfig": t.proxy(
                renames["GoogleCloudMlV1__ReplicaConfigOut"]
            ).optional(),
            "parameterServerCount": t.string().optional(),
            "scaleTier": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__TrainingInputOut"])
    types["GoogleCloudMlV1__IntegratedGradientsAttributionIn"] = t.struct(
        {"numIntegralSteps": t.integer().optional()}
    ).named(renames["GoogleCloudMlV1__IntegratedGradientsAttributionIn"])
    types["GoogleCloudMlV1__IntegratedGradientsAttributionOut"] = t.struct(
        {
            "numIntegralSteps": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__IntegratedGradientsAttributionOut"])
    types["GoogleCloudMlV1__ListOptimalTrialsRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudMlV1__ListOptimalTrialsRequestIn"])
    types["GoogleCloudMlV1__ListOptimalTrialsRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudMlV1__ListOptimalTrialsRequestOut"])
    types["GoogleCloudMlV1_Measurement_MetricIn"] = t.struct(
        {"value": t.number(), "metric": t.string()}
    ).named(renames["GoogleCloudMlV1_Measurement_MetricIn"])
    types["GoogleCloudMlV1_Measurement_MetricOut"] = t.struct(
        {
            "value": t.number(),
            "metric": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1_Measurement_MetricOut"])
    types["GoogleCloudMlV1__ParameterSpecIn"] = t.struct(
        {
            "type": t.string(),
            "maxValue": t.number(),
            "categoricalValues": t.array(t.string()),
            "parameterName": t.string(),
            "discreteValues": t.array(t.number()),
            "minValue": t.number(),
            "scaleType": t.string().optional(),
        }
    ).named(renames["GoogleCloudMlV1__ParameterSpecIn"])
    types["GoogleCloudMlV1__ParameterSpecOut"] = t.struct(
        {
            "type": t.string(),
            "maxValue": t.number(),
            "categoricalValues": t.array(t.string()),
            "parameterName": t.string(),
            "discreteValues": t.array(t.number()),
            "minValue": t.number(),
            "scaleType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ParameterSpecOut"])
    types["GoogleCloudMlV1_StudyConfig_ParameterSpecIn"] = t.struct(
        {
            "scaleType": t.string().optional(),
            "categoricalValueSpec": t.proxy(
                renames[
                    "GoogleCloudMlV1_StudyConfigParameterSpec_CategoricalValueSpecIn"
                ]
            ).optional(),
            "childParameterSpecs": t.array(
                t.proxy(renames["GoogleCloudMlV1_StudyConfig_ParameterSpecIn"])
            ).optional(),
            "integerValueSpec": t.proxy(
                renames["GoogleCloudMlV1_StudyConfigParameterSpec_IntegerValueSpecIn"]
            ).optional(),
            "type": t.string(),
            "parentCategoricalValues": t.proxy(
                renames[
                    "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentCategoricalValueSpecIn"
                ]
            ),
            "parentDiscreteValues": t.proxy(
                renames[
                    "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentDiscreteValueSpecIn"
                ]
            ),
            "discreteValueSpec": t.proxy(
                renames["GoogleCloudMlV1_StudyConfigParameterSpec_DiscreteValueSpecIn"]
            ).optional(),
            "parentIntValues": t.proxy(
                renames[
                    "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentIntValueSpecIn"
                ]
            ),
            "doubleValueSpec": t.proxy(
                renames["GoogleCloudMlV1_StudyConfigParameterSpec_DoubleValueSpecIn"]
            ).optional(),
            "parameter": t.string(),
        }
    ).named(renames["GoogleCloudMlV1_StudyConfig_ParameterSpecIn"])
    types["GoogleCloudMlV1_StudyConfig_ParameterSpecOut"] = t.struct(
        {
            "scaleType": t.string().optional(),
            "categoricalValueSpec": t.proxy(
                renames[
                    "GoogleCloudMlV1_StudyConfigParameterSpec_CategoricalValueSpecOut"
                ]
            ).optional(),
            "childParameterSpecs": t.array(
                t.proxy(renames["GoogleCloudMlV1_StudyConfig_ParameterSpecOut"])
            ).optional(),
            "integerValueSpec": t.proxy(
                renames["GoogleCloudMlV1_StudyConfigParameterSpec_IntegerValueSpecOut"]
            ).optional(),
            "type": t.string(),
            "parentCategoricalValues": t.proxy(
                renames[
                    "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentCategoricalValueSpecOut"
                ]
            ),
            "parentDiscreteValues": t.proxy(
                renames[
                    "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentDiscreteValueSpecOut"
                ]
            ),
            "discreteValueSpec": t.proxy(
                renames["GoogleCloudMlV1_StudyConfigParameterSpec_DiscreteValueSpecOut"]
            ).optional(),
            "parentIntValues": t.proxy(
                renames[
                    "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentIntValueSpecOut"
                ]
            ),
            "doubleValueSpec": t.proxy(
                renames["GoogleCloudMlV1_StudyConfigParameterSpec_DoubleValueSpecOut"]
            ).optional(),
            "parameter": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1_StudyConfig_ParameterSpecOut"])
    types["GoogleCloudMlV1__AcceleratorConfigIn"] = t.struct(
        {"type": t.string().optional(), "count": t.string().optional()}
    ).named(renames["GoogleCloudMlV1__AcceleratorConfigIn"])
    types["GoogleCloudMlV1__AcceleratorConfigOut"] = t.struct(
        {
            "type": t.string().optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__AcceleratorConfigOut"])
    types["GoogleCloudMlV1__LocationIn"] = t.struct(
        {
            "name": t.string(),
            "capabilities": t.array(
                t.proxy(renames["GoogleCloudMlV1__CapabilityIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudMlV1__LocationIn"])
    types["GoogleCloudMlV1__LocationOut"] = t.struct(
        {
            "name": t.string(),
            "capabilities": t.array(
                t.proxy(renames["GoogleCloudMlV1__CapabilityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__LocationOut"])
    types["GoogleCloudMlV1__HyperparameterSpecIn"] = t.struct(
        {
            "params": t.array(t.proxy(renames["GoogleCloudMlV1__ParameterSpecIn"])),
            "resumePreviousJobId": t.string().optional(),
            "goal": t.string(),
            "maxParallelTrials": t.integer().optional(),
            "maxFailedTrials": t.integer().optional(),
            "enableTrialEarlyStopping": t.boolean().optional(),
            "hyperparameterMetricTag": t.string().optional(),
            "algorithm": t.string().optional(),
            "maxTrials": t.integer().optional(),
        }
    ).named(renames["GoogleCloudMlV1__HyperparameterSpecIn"])
    types["GoogleCloudMlV1__HyperparameterSpecOut"] = t.struct(
        {
            "params": t.array(t.proxy(renames["GoogleCloudMlV1__ParameterSpecOut"])),
            "resumePreviousJobId": t.string().optional(),
            "goal": t.string(),
            "maxParallelTrials": t.integer().optional(),
            "maxFailedTrials": t.integer().optional(),
            "enableTrialEarlyStopping": t.boolean().optional(),
            "hyperparameterMetricTag": t.string().optional(),
            "algorithm": t.string().optional(),
            "maxTrials": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__HyperparameterSpecOut"])
    types["GoogleCloudMlV1__StudyConfigIn"] = t.struct(
        {
            "metrics": t.array(
                t.proxy(renames["GoogleCloudMlV1_StudyConfig_MetricSpecIn"])
            ).optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudMlV1_StudyConfig_ParameterSpecIn"])
            ),
            "algorithm": t.string().optional(),
            "automatedStoppingConfig": t.proxy(
                renames["GoogleCloudMlV1__AutomatedStoppingConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudMlV1__StudyConfigIn"])
    types["GoogleCloudMlV1__StudyConfigOut"] = t.struct(
        {
            "metrics": t.array(
                t.proxy(renames["GoogleCloudMlV1_StudyConfig_MetricSpecOut"])
            ).optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudMlV1_StudyConfig_ParameterSpecOut"])
            ),
            "algorithm": t.string().optional(),
            "automatedStoppingConfig": t.proxy(
                renames["GoogleCloudMlV1__AutomatedStoppingConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__StudyConfigOut"])
    types["GoogleCloudMlV1__SuggestTrialsMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "suggestionCount": t.integer().optional(),
            "study": t.string().optional(),
            "clientId": t.string().optional(),
        }
    ).named(renames["GoogleCloudMlV1__SuggestTrialsMetadataIn"])
    types["GoogleCloudMlV1__SuggestTrialsMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "suggestionCount": t.integer().optional(),
            "study": t.string().optional(),
            "clientId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__SuggestTrialsMetadataOut"])
    types["GoogleCloudMlV1__TrainingOutputIn"] = t.struct(
        {
            "completedTrialCount": t.string().optional(),
            "isHyperparameterTuningJob": t.boolean().optional(),
            "trials": t.array(
                t.proxy(renames["GoogleCloudMlV1__HyperparameterOutputIn"])
            ).optional(),
            "hyperparameterMetricTag": t.string().optional(),
            "consumedMLUnits": t.number().optional(),
            "isBuiltInAlgorithmJob": t.boolean().optional(),
            "builtInAlgorithmOutput": t.proxy(
                renames["GoogleCloudMlV1__BuiltInAlgorithmOutputIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudMlV1__TrainingOutputIn"])
    types["GoogleCloudMlV1__TrainingOutputOut"] = t.struct(
        {
            "completedTrialCount": t.string().optional(),
            "isHyperparameterTuningJob": t.boolean().optional(),
            "trials": t.array(
                t.proxy(renames["GoogleCloudMlV1__HyperparameterOutputOut"])
            ).optional(),
            "hyperparameterMetricTag": t.string().optional(),
            "consumedMLUnits": t.number().optional(),
            "isBuiltInAlgorithmJob": t.boolean().optional(),
            "webAccessUris": t.struct({"_": t.string().optional()}).optional(),
            "builtInAlgorithmOutput": t.proxy(
                renames["GoogleCloudMlV1__BuiltInAlgorithmOutputOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__TrainingOutputOut"])
    types["GoogleCloudMlV1__VersionIn"] = t.struct(
        {
            "deploymentUri": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "pythonVersion": t.string(),
            "predictionClass": t.string().optional(),
            "runtimeVersion": t.string(),
            "machineType": t.string().optional(),
            "autoScaling": t.proxy(
                renames["GoogleCloudMlV1__AutoScalingIn"]
            ).optional(),
            "state": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "routes": t.proxy(renames["GoogleCloudMlV1__RouteMapIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "manualScaling": t.proxy(
                renames["GoogleCloudMlV1__ManualScalingIn"]
            ).optional(),
            "acceleratorConfig": t.proxy(
                renames["GoogleCloudMlV1__AcceleratorConfigIn"]
            ).optional(),
            "createTime": t.string().optional(),
            "lastUseTime": t.string().optional(),
            "requestLoggingConfig": t.proxy(
                renames["GoogleCloudMlV1__RequestLoggingConfigIn"]
            ).optional(),
            "container": t.proxy(
                renames["GoogleCloudMlV1__ContainerSpecIn"]
            ).optional(),
            "isDefault": t.boolean().optional(),
            "errorMessage": t.string().optional(),
            "etag": t.string().optional(),
            "framework": t.string().optional(),
            "explanationConfig": t.proxy(
                renames["GoogleCloudMlV1__ExplanationConfigIn"]
            ).optional(),
            "packageUris": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudMlV1__VersionIn"])
    types["GoogleCloudMlV1__VersionOut"] = t.struct(
        {
            "lastMigrationModelId": t.string().optional(),
            "deploymentUri": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "pythonVersion": t.string(),
            "predictionClass": t.string().optional(),
            "runtimeVersion": t.string(),
            "lastMigrationTime": t.string().optional(),
            "machineType": t.string().optional(),
            "autoScaling": t.proxy(
                renames["GoogleCloudMlV1__AutoScalingOut"]
            ).optional(),
            "state": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "routes": t.proxy(renames["GoogleCloudMlV1__RouteMapOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "manualScaling": t.proxy(
                renames["GoogleCloudMlV1__ManualScalingOut"]
            ).optional(),
            "acceleratorConfig": t.proxy(
                renames["GoogleCloudMlV1__AcceleratorConfigOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "lastUseTime": t.string().optional(),
            "requestLoggingConfig": t.proxy(
                renames["GoogleCloudMlV1__RequestLoggingConfigOut"]
            ).optional(),
            "container": t.proxy(
                renames["GoogleCloudMlV1__ContainerSpecOut"]
            ).optional(),
            "isDefault": t.boolean().optional(),
            "errorMessage": t.string().optional(),
            "etag": t.string().optional(),
            "framework": t.string().optional(),
            "explanationConfig": t.proxy(
                renames["GoogleCloudMlV1__ExplanationConfigOut"]
            ).optional(),
            "packageUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__VersionOut"])
    types["GoogleCloudMlV1__ConfigIn"] = t.struct(
        {"tpuServiceAccount": t.string().optional()}
    ).named(renames["GoogleCloudMlV1__ConfigIn"])
    types["GoogleCloudMlV1__ConfigOut"] = t.struct(
        {
            "tpuServiceAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ConfigOut"])
    types["GoogleCloudMlV1__ListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(
                t.proxy(renames["GoogleCloudMlV1__LocationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudMlV1__ListLocationsResponseIn"])
    types["GoogleCloudMlV1__ListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(
                t.proxy(renames["GoogleCloudMlV1__LocationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ListLocationsResponseOut"])
    types["GoogleCloudMlV1__AddTrialMeasurementRequestIn"] = t.struct(
        {"measurement": t.proxy(renames["GoogleCloudMlV1__MeasurementIn"])}
    ).named(renames["GoogleCloudMlV1__AddTrialMeasurementRequestIn"])
    types["GoogleCloudMlV1__AddTrialMeasurementRequestOut"] = t.struct(
        {
            "measurement": t.proxy(renames["GoogleCloudMlV1__MeasurementOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__AddTrialMeasurementRequestOut"])
    types["GoogleCloudMlV1__StopTrialRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudMlV1__StopTrialRequestIn"])
    types["GoogleCloudMlV1__StopTrialRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudMlV1__StopTrialRequestOut"])
    types["GoogleCloudMlV1__OperationMetadataIn"] = t.struct(
        {
            "projectNumber": t.string().optional(),
            "endTime": t.string().optional(),
            "isCancellationRequested": t.boolean().optional(),
            "version": t.proxy(renames["GoogleCloudMlV1__VersionIn"]).optional(),
            "operationType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "modelName": t.string().optional(),
            "createTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudMlV1__OperationMetadataIn"])
    types["GoogleCloudMlV1__OperationMetadataOut"] = t.struct(
        {
            "projectNumber": t.string().optional(),
            "endTime": t.string().optional(),
            "isCancellationRequested": t.boolean().optional(),
            "version": t.proxy(renames["GoogleCloudMlV1__VersionOut"]).optional(),
            "operationType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "modelName": t.string().optional(),
            "createTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__OperationMetadataOut"])
    types["GoogleCloudMlV1__TrialIn"] = t.struct(
        {
            "measurements": t.array(
                t.proxy(renames["GoogleCloudMlV1__MeasurementIn"])
            ).optional(),
            "finalMeasurement": t.proxy(
                renames["GoogleCloudMlV1__MeasurementIn"]
            ).optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudMlV1_Trial_ParameterIn"])
            ).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudMlV1__TrialIn"])
    types["GoogleCloudMlV1__TrialOut"] = t.struct(
        {
            "measurements": t.array(
                t.proxy(renames["GoogleCloudMlV1__MeasurementOut"])
            ).optional(),
            "infeasibleReason": t.string().optional(),
            "finalMeasurement": t.proxy(
                renames["GoogleCloudMlV1__MeasurementOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudMlV1_Trial_ParameterOut"])
            ).optional(),
            "clientId": t.string().optional(),
            "trialInfeasible": t.boolean().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__TrialOut"])
    types["GoogleCloudMlV1__ContainerSpecIn"] = t.struct(
        {
            "image": t.string().optional(),
            "env": t.array(t.proxy(renames["GoogleCloudMlV1__EnvVarIn"])).optional(),
            "ports": t.array(
                t.proxy(renames["GoogleCloudMlV1__ContainerPortIn"])
            ).optional(),
            "command": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ContainerSpecIn"])
    types["GoogleCloudMlV1__ContainerSpecOut"] = t.struct(
        {
            "image": t.string().optional(),
            "env": t.array(t.proxy(renames["GoogleCloudMlV1__EnvVarOut"])).optional(),
            "ports": t.array(
                t.proxy(renames["GoogleCloudMlV1__ContainerPortOut"])
            ).optional(),
            "command": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ContainerSpecOut"])
    types[
        "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentCategoricalValueSpecIn"
    ] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames[
            "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentCategoricalValueSpecIn"
        ]
    )
    types[
        "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentCategoricalValueSpecOut"
    ] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentCategoricalValueSpecOut"
        ]
    )
    types["GoogleCloudMlV1__CheckTrialEarlyStoppingStateRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudMlV1__CheckTrialEarlyStoppingStateRequestIn"])
    types["GoogleCloudMlV1__CheckTrialEarlyStoppingStateRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudMlV1__CheckTrialEarlyStoppingStateRequestOut"])
    types["GoogleIamV1__TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1__TestIamPermissionsResponseIn"])
    types["GoogleIamV1__TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1__TestIamPermissionsResponseOut"])
    types["GoogleCloudMlV1_StudyConfigParameterSpec_CategoricalValueSpecIn"] = t.struct(
        {"values": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudMlV1_StudyConfigParameterSpec_CategoricalValueSpecIn"])
    types[
        "GoogleCloudMlV1_StudyConfigParameterSpec_CategoricalValueSpecOut"
    ] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudMlV1_StudyConfigParameterSpec_CategoricalValueSpecOut"]
    )
    types["GoogleCloudMlV1_HyperparameterOutput_HyperparameterMetricIn"] = t.struct(
        {"trainingStep": t.string().optional(), "objectiveValue": t.number().optional()}
    ).named(renames["GoogleCloudMlV1_HyperparameterOutput_HyperparameterMetricIn"])
    types["GoogleCloudMlV1_HyperparameterOutput_HyperparameterMetricOut"] = t.struct(
        {
            "trainingStep": t.string().optional(),
            "objectiveValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1_HyperparameterOutput_HyperparameterMetricOut"])
    types["GoogleIamV1__SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["GoogleIamV1__PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["GoogleIamV1__SetIamPolicyRequestIn"])
    types["GoogleIamV1__SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["GoogleIamV1__PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1__SetIamPolicyRequestOut"])
    types["GoogleCloudMlV1__PredictionOutputIn"] = t.struct(
        {
            "outputPath": t.string().optional(),
            "errorCount": t.string().optional(),
            "predictionCount": t.string().optional(),
            "nodeHours": t.number().optional(),
        }
    ).named(renames["GoogleCloudMlV1__PredictionOutputIn"])
    types["GoogleCloudMlV1__PredictionOutputOut"] = t.struct(
        {
            "outputPath": t.string().optional(),
            "errorCount": t.string().optional(),
            "predictionCount": t.string().optional(),
            "nodeHours": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__PredictionOutputOut"])
    types["GoogleIamV1__AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1__AuditLogConfigIn"])
            ).optional(),
        }
    ).named(renames["GoogleIamV1__AuditConfigIn"])
    types["GoogleIamV1__AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1__AuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1__AuditConfigOut"])
    types["GoogleCloudMlV1__CapabilityIn"] = t.struct(
        {"availableAccelerators": t.array(t.string()).optional(), "type": t.string()}
    ).named(renames["GoogleCloudMlV1__CapabilityIn"])
    types["GoogleCloudMlV1__CapabilityOut"] = t.struct(
        {
            "availableAccelerators": t.array(t.string()).optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__CapabilityOut"])
    types["GoogleCloudMlV1__RequestLoggingConfigIn"] = t.struct(
        {"bigqueryTableName": t.string(), "samplingPercentage": t.number().optional()}
    ).named(renames["GoogleCloudMlV1__RequestLoggingConfigIn"])
    types["GoogleCloudMlV1__RequestLoggingConfigOut"] = t.struct(
        {
            "bigqueryTableName": t.string(),
            "samplingPercentage": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__RequestLoggingConfigOut"])
    types["GoogleCloudMlV1__CheckTrialEarlyStoppingStateMetatdataIn"] = t.struct(
        {
            "trial": t.string().optional(),
            "study": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudMlV1__CheckTrialEarlyStoppingStateMetatdataIn"])
    types["GoogleCloudMlV1__CheckTrialEarlyStoppingStateMetatdataOut"] = t.struct(
        {
            "trial": t.string().optional(),
            "study": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__CheckTrialEarlyStoppingStateMetatdataOut"])
    types["GoogleCloudMlV1__PredictionInputIn"] = t.struct(
        {
            "outputPath": t.string(),
            "dataFormat": t.string(),
            "region": t.string(),
            "signatureName": t.string().optional(),
            "maxWorkerCount": t.string().optional(),
            "runtimeVersion": t.string().optional(),
            "inputPaths": t.array(t.string()),
            "versionName": t.string().optional(),
            "uri": t.string().optional(),
            "outputDataFormat": t.string().optional(),
            "modelName": t.string().optional(),
            "batchSize": t.string().optional(),
        }
    ).named(renames["GoogleCloudMlV1__PredictionInputIn"])
    types["GoogleCloudMlV1__PredictionInputOut"] = t.struct(
        {
            "outputPath": t.string(),
            "dataFormat": t.string(),
            "region": t.string(),
            "signatureName": t.string().optional(),
            "maxWorkerCount": t.string().optional(),
            "runtimeVersion": t.string().optional(),
            "inputPaths": t.array(t.string()),
            "versionName": t.string().optional(),
            "uri": t.string().optional(),
            "outputDataFormat": t.string().optional(),
            "modelName": t.string().optional(),
            "batchSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__PredictionInputOut"])
    types["GoogleCloudMlV1_StudyConfigParameterSpec_DiscreteValueSpecIn"] = t.struct(
        {"values": t.array(t.number()).optional()}
    ).named(renames["GoogleCloudMlV1_StudyConfigParameterSpec_DiscreteValueSpecIn"])
    types["GoogleCloudMlV1_StudyConfigParameterSpec_DiscreteValueSpecOut"] = t.struct(
        {
            "values": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1_StudyConfigParameterSpec_DiscreteValueSpecOut"])
    types["GoogleCloudMlV1__ManualScalingIn"] = t.struct(
        {"nodes": t.integer().optional()}
    ).named(renames["GoogleCloudMlV1__ManualScalingIn"])
    types["GoogleCloudMlV1__ManualScalingOut"] = t.struct(
        {
            "nodes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ManualScalingOut"])
    types["GoogleCloudMlV1__StudyIn"] = t.struct(
        {"studyConfig": t.proxy(renames["GoogleCloudMlV1__StudyConfigIn"])}
    ).named(renames["GoogleCloudMlV1__StudyIn"])
    types["GoogleCloudMlV1__StudyOut"] = t.struct(
        {
            "studyConfig": t.proxy(renames["GoogleCloudMlV1__StudyConfigOut"]),
            "name": t.string().optional(),
            "inactiveReason": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__StudyOut"])
    types["GoogleCloudMlV1_StudyConfig_MetricSpecIn"] = t.struct(
        {"metric": t.string(), "goal": t.string()}
    ).named(renames["GoogleCloudMlV1_StudyConfig_MetricSpecIn"])
    types["GoogleCloudMlV1_StudyConfig_MetricSpecOut"] = t.struct(
        {
            "metric": t.string(),
            "goal": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1_StudyConfig_MetricSpecOut"])
    types["GoogleCloudMlV1__EncryptionConfigIn"] = t.struct(
        {"kmsKeyName": t.string().optional()}
    ).named(renames["GoogleCloudMlV1__EncryptionConfigIn"])
    types["GoogleCloudMlV1__EncryptionConfigOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__EncryptionConfigOut"])
    types["GoogleCloudMlV1__CancelJobRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudMlV1__CancelJobRequestIn"])
    types["GoogleCloudMlV1__CancelJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudMlV1__CancelJobRequestOut"])
    types["GoogleCloudMlV1__PredictRequestIn"] = t.struct(
        {"httpBody": t.proxy(renames["GoogleApi__HttpBodyIn"]).optional()}
    ).named(renames["GoogleCloudMlV1__PredictRequestIn"])
    types["GoogleCloudMlV1__PredictRequestOut"] = t.struct(
        {
            "httpBody": t.proxy(renames["GoogleApi__HttpBodyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__PredictRequestOut"])
    types["GoogleCloudMlV1__ListOptimalTrialsResponseIn"] = t.struct(
        {"trials": t.array(t.proxy(renames["GoogleCloudMlV1__TrialIn"])).optional()}
    ).named(renames["GoogleCloudMlV1__ListOptimalTrialsResponseIn"])
    types["GoogleCloudMlV1__ListOptimalTrialsResponseOut"] = t.struct(
        {
            "trials": t.array(t.proxy(renames["GoogleCloudMlV1__TrialOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ListOptimalTrialsResponseOut"])
    types["GoogleIamV1__PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["GoogleIamV1__BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1__AuditConfigIn"])
            ).optional(),
        }
    ).named(renames["GoogleIamV1__PolicyIn"])
    types["GoogleIamV1__PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["GoogleIamV1__BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1__AuditConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1__PolicyOut"])
    types["GoogleCloudMlV1__BuiltInAlgorithmOutputIn"] = t.struct(
        {
            "framework": t.string().optional(),
            "runtimeVersion": t.string().optional(),
            "pythonVersion": t.string().optional(),
            "modelPath": t.string().optional(),
        }
    ).named(renames["GoogleCloudMlV1__BuiltInAlgorithmOutputIn"])
    types["GoogleCloudMlV1__BuiltInAlgorithmOutputOut"] = t.struct(
        {
            "framework": t.string().optional(),
            "runtimeVersion": t.string().optional(),
            "pythonVersion": t.string().optional(),
            "modelPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__BuiltInAlgorithmOutputOut"])
    types["GoogleCloudMlV1__AutoScalingIn"] = t.struct(
        {
            "maxNodes": t.integer().optional(),
            "minNodes": t.integer().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudMlV1__MetricSpecIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudMlV1__AutoScalingIn"])
    types["GoogleCloudMlV1__AutoScalingOut"] = t.struct(
        {
            "maxNodes": t.integer().optional(),
            "minNodes": t.integer().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudMlV1__MetricSpecOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__AutoScalingOut"])
    types["GoogleCloudMlV1__ContainerPortIn"] = t.struct(
        {"containerPort": t.integer().optional()}
    ).named(renames["GoogleCloudMlV1__ContainerPortIn"])
    types["GoogleCloudMlV1__ContainerPortOut"] = t.struct(
        {
            "containerPort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ContainerPortOut"])
    types["GoogleLongrunning__ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunning__OperationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleLongrunning__ListOperationsResponseIn"])
    types["GoogleLongrunning__ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunning__OperationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunning__ListOperationsResponseOut"])
    types["GoogleCloudMlV1__ListModelsResponseIn"] = t.struct(
        {
            "models": t.array(t.proxy(renames["GoogleCloudMlV1__ModelIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudMlV1__ListModelsResponseIn"])
    types["GoogleCloudMlV1__ListModelsResponseOut"] = t.struct(
        {
            "models": t.array(t.proxy(renames["GoogleCloudMlV1__ModelOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ListModelsResponseOut"])
    types["GoogleCloudMlV1__ExplainRequestIn"] = t.struct(
        {"httpBody": t.proxy(renames["GoogleApi__HttpBodyIn"])}
    ).named(renames["GoogleCloudMlV1__ExplainRequestIn"])
    types["GoogleCloudMlV1__ExplainRequestOut"] = t.struct(
        {
            "httpBody": t.proxy(renames["GoogleApi__HttpBodyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__ExplainRequestOut"])
    types["GoogleCloudMlV1__EnvVarIn"] = t.struct(
        {"name": t.string().optional(), "value": t.string().optional()}
    ).named(renames["GoogleCloudMlV1__EnvVarIn"])
    types["GoogleCloudMlV1__EnvVarOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMlV1__EnvVarOut"])

    functions = {}
    functions["projectsGetConfig"] = ml.post(
        "v1/{name}:predict",
        t.struct(
            {
                "name": t.string(),
                "httpBody": t.proxy(renames["GoogleApi__HttpBodyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleApi__HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExplain"] = ml.post(
        "v1/{name}:predict",
        t.struct(
            {
                "name": t.string(),
                "httpBody": t.proxy(renames["GoogleApi__HttpBodyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleApi__HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPredict"] = ml.post(
        "v1/{name}:predict",
        t.struct(
            {
                "name": t.string(),
                "httpBody": t.proxy(renames["GoogleApi__HttpBodyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleApi__HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsGet"] = ml.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobuf__EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsList"] = ml.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobuf__EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsCancel"] = ml.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobuf__EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsModelsGetIamPolicy"] = ml.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1__PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1__PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsModelsCreate"] = ml.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1__PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1__PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsModelsDelete"] = ml.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1__PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1__PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsModelsTestIamPermissions"] = ml.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1__PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1__PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsModelsList"] = ml.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1__PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1__PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsModelsPatch"] = ml.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1__PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1__PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsModelsGet"] = ml.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1__PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1__PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsModelsSetIamPolicy"] = ml.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1__PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1__PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsModelsVersionsDelete"] = ml.post(
        "v1/{parent}/versions",
        t.struct(
            {
                "parent": t.string(),
                "deploymentUri": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string(),
                "pythonVersion": t.string(),
                "predictionClass": t.string().optional(),
                "runtimeVersion": t.string(),
                "machineType": t.string().optional(),
                "autoScaling": t.proxy(
                    renames["GoogleCloudMlV1__AutoScalingIn"]
                ).optional(),
                "state": t.string().optional(),
                "serviceAccount": t.string().optional(),
                "routes": t.proxy(renames["GoogleCloudMlV1__RouteMapIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "manualScaling": t.proxy(
                    renames["GoogleCloudMlV1__ManualScalingIn"]
                ).optional(),
                "acceleratorConfig": t.proxy(
                    renames["GoogleCloudMlV1__AcceleratorConfigIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "lastUseTime": t.string().optional(),
                "requestLoggingConfig": t.proxy(
                    renames["GoogleCloudMlV1__RequestLoggingConfigIn"]
                ).optional(),
                "container": t.proxy(
                    renames["GoogleCloudMlV1__ContainerSpecIn"]
                ).optional(),
                "isDefault": t.boolean().optional(),
                "errorMessage": t.string().optional(),
                "etag": t.string().optional(),
                "framework": t.string().optional(),
                "explanationConfig": t.proxy(
                    renames["GoogleCloudMlV1__ExplanationConfigIn"]
                ).optional(),
                "packageUris": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning__OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsModelsVersionsGet"] = ml.post(
        "v1/{parent}/versions",
        t.struct(
            {
                "parent": t.string(),
                "deploymentUri": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string(),
                "pythonVersion": t.string(),
                "predictionClass": t.string().optional(),
                "runtimeVersion": t.string(),
                "machineType": t.string().optional(),
                "autoScaling": t.proxy(
                    renames["GoogleCloudMlV1__AutoScalingIn"]
                ).optional(),
                "state": t.string().optional(),
                "serviceAccount": t.string().optional(),
                "routes": t.proxy(renames["GoogleCloudMlV1__RouteMapIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "manualScaling": t.proxy(
                    renames["GoogleCloudMlV1__ManualScalingIn"]
                ).optional(),
                "acceleratorConfig": t.proxy(
                    renames["GoogleCloudMlV1__AcceleratorConfigIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "lastUseTime": t.string().optional(),
                "requestLoggingConfig": t.proxy(
                    renames["GoogleCloudMlV1__RequestLoggingConfigIn"]
                ).optional(),
                "container": t.proxy(
                    renames["GoogleCloudMlV1__ContainerSpecIn"]
                ).optional(),
                "isDefault": t.boolean().optional(),
                "errorMessage": t.string().optional(),
                "etag": t.string().optional(),
                "framework": t.string().optional(),
                "explanationConfig": t.proxy(
                    renames["GoogleCloudMlV1__ExplanationConfigIn"]
                ).optional(),
                "packageUris": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning__OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsModelsVersionsList"] = ml.post(
        "v1/{parent}/versions",
        t.struct(
            {
                "parent": t.string(),
                "deploymentUri": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string(),
                "pythonVersion": t.string(),
                "predictionClass": t.string().optional(),
                "runtimeVersion": t.string(),
                "machineType": t.string().optional(),
                "autoScaling": t.proxy(
                    renames["GoogleCloudMlV1__AutoScalingIn"]
                ).optional(),
                "state": t.string().optional(),
                "serviceAccount": t.string().optional(),
                "routes": t.proxy(renames["GoogleCloudMlV1__RouteMapIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "manualScaling": t.proxy(
                    renames["GoogleCloudMlV1__ManualScalingIn"]
                ).optional(),
                "acceleratorConfig": t.proxy(
                    renames["GoogleCloudMlV1__AcceleratorConfigIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "lastUseTime": t.string().optional(),
                "requestLoggingConfig": t.proxy(
                    renames["GoogleCloudMlV1__RequestLoggingConfigIn"]
                ).optional(),
                "container": t.proxy(
                    renames["GoogleCloudMlV1__ContainerSpecIn"]
                ).optional(),
                "isDefault": t.boolean().optional(),
                "errorMessage": t.string().optional(),
                "etag": t.string().optional(),
                "framework": t.string().optional(),
                "explanationConfig": t.proxy(
                    renames["GoogleCloudMlV1__ExplanationConfigIn"]
                ).optional(),
                "packageUris": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning__OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsModelsVersionsPatch"] = ml.post(
        "v1/{parent}/versions",
        t.struct(
            {
                "parent": t.string(),
                "deploymentUri": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string(),
                "pythonVersion": t.string(),
                "predictionClass": t.string().optional(),
                "runtimeVersion": t.string(),
                "machineType": t.string().optional(),
                "autoScaling": t.proxy(
                    renames["GoogleCloudMlV1__AutoScalingIn"]
                ).optional(),
                "state": t.string().optional(),
                "serviceAccount": t.string().optional(),
                "routes": t.proxy(renames["GoogleCloudMlV1__RouteMapIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "manualScaling": t.proxy(
                    renames["GoogleCloudMlV1__ManualScalingIn"]
                ).optional(),
                "acceleratorConfig": t.proxy(
                    renames["GoogleCloudMlV1__AcceleratorConfigIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "lastUseTime": t.string().optional(),
                "requestLoggingConfig": t.proxy(
                    renames["GoogleCloudMlV1__RequestLoggingConfigIn"]
                ).optional(),
                "container": t.proxy(
                    renames["GoogleCloudMlV1__ContainerSpecIn"]
                ).optional(),
                "isDefault": t.boolean().optional(),
                "errorMessage": t.string().optional(),
                "etag": t.string().optional(),
                "framework": t.string().optional(),
                "explanationConfig": t.proxy(
                    renames["GoogleCloudMlV1__ExplanationConfigIn"]
                ).optional(),
                "packageUris": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning__OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsModelsVersionsSetDefault"] = ml.post(
        "v1/{parent}/versions",
        t.struct(
            {
                "parent": t.string(),
                "deploymentUri": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string(),
                "pythonVersion": t.string(),
                "predictionClass": t.string().optional(),
                "runtimeVersion": t.string(),
                "machineType": t.string().optional(),
                "autoScaling": t.proxy(
                    renames["GoogleCloudMlV1__AutoScalingIn"]
                ).optional(),
                "state": t.string().optional(),
                "serviceAccount": t.string().optional(),
                "routes": t.proxy(renames["GoogleCloudMlV1__RouteMapIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "manualScaling": t.proxy(
                    renames["GoogleCloudMlV1__ManualScalingIn"]
                ).optional(),
                "acceleratorConfig": t.proxy(
                    renames["GoogleCloudMlV1__AcceleratorConfigIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "lastUseTime": t.string().optional(),
                "requestLoggingConfig": t.proxy(
                    renames["GoogleCloudMlV1__RequestLoggingConfigIn"]
                ).optional(),
                "container": t.proxy(
                    renames["GoogleCloudMlV1__ContainerSpecIn"]
                ).optional(),
                "isDefault": t.boolean().optional(),
                "errorMessage": t.string().optional(),
                "etag": t.string().optional(),
                "framework": t.string().optional(),
                "explanationConfig": t.proxy(
                    renames["GoogleCloudMlV1__ExplanationConfigIn"]
                ).optional(),
                "packageUris": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning__OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsModelsVersionsCreate"] = ml.post(
        "v1/{parent}/versions",
        t.struct(
            {
                "parent": t.string(),
                "deploymentUri": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string(),
                "pythonVersion": t.string(),
                "predictionClass": t.string().optional(),
                "runtimeVersion": t.string(),
                "machineType": t.string().optional(),
                "autoScaling": t.proxy(
                    renames["GoogleCloudMlV1__AutoScalingIn"]
                ).optional(),
                "state": t.string().optional(),
                "serviceAccount": t.string().optional(),
                "routes": t.proxy(renames["GoogleCloudMlV1__RouteMapIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "manualScaling": t.proxy(
                    renames["GoogleCloudMlV1__ManualScalingIn"]
                ).optional(),
                "acceleratorConfig": t.proxy(
                    renames["GoogleCloudMlV1__AcceleratorConfigIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "lastUseTime": t.string().optional(),
                "requestLoggingConfig": t.proxy(
                    renames["GoogleCloudMlV1__RequestLoggingConfigIn"]
                ).optional(),
                "container": t.proxy(
                    renames["GoogleCloudMlV1__ContainerSpecIn"]
                ).optional(),
                "isDefault": t.boolean().optional(),
                "errorMessage": t.string().optional(),
                "etag": t.string().optional(),
                "framework": t.string().optional(),
                "explanationConfig": t.proxy(
                    renames["GoogleCloudMlV1__ExplanationConfigIn"]
                ).optional(),
                "packageUris": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning__OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = ml.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudMlV1__LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = ml.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudMlV1__LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = ml.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobuf__EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = ml.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobuf__EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStudiesGet"] = ml.post(
        "v1/{parent}/studies",
        t.struct(
            {
                "parent": t.string(),
                "studyId": t.string(),
                "studyConfig": t.proxy(renames["GoogleCloudMlV1__StudyConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudMlV1__StudyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStudiesList"] = ml.post(
        "v1/{parent}/studies",
        t.struct(
            {
                "parent": t.string(),
                "studyId": t.string(),
                "studyConfig": t.proxy(renames["GoogleCloudMlV1__StudyConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudMlV1__StudyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStudiesDelete"] = ml.post(
        "v1/{parent}/studies",
        t.struct(
            {
                "parent": t.string(),
                "studyId": t.string(),
                "studyConfig": t.proxy(renames["GoogleCloudMlV1__StudyConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudMlV1__StudyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStudiesCreate"] = ml.post(
        "v1/{parent}/studies",
        t.struct(
            {
                "parent": t.string(),
                "studyId": t.string(),
                "studyConfig": t.proxy(renames["GoogleCloudMlV1__StudyConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudMlV1__StudyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStudiesTrialsAddMeasurement"] = ml.post(
        "v1/{parent}/trials:suggest",
        t.struct(
            {
                "parent": t.string(),
                "suggestionCount": t.integer(),
                "clientId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning__OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStudiesTrialsCheckEarlyStoppingState"] = ml.post(
        "v1/{parent}/trials:suggest",
        t.struct(
            {
                "parent": t.string(),
                "suggestionCount": t.integer(),
                "clientId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning__OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStudiesTrialsStop"] = ml.post(
        "v1/{parent}/trials:suggest",
        t.struct(
            {
                "parent": t.string(),
                "suggestionCount": t.integer(),
                "clientId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning__OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStudiesTrialsDelete"] = ml.post(
        "v1/{parent}/trials:suggest",
        t.struct(
            {
                "parent": t.string(),
                "suggestionCount": t.integer(),
                "clientId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning__OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStudiesTrialsGet"] = ml.post(
        "v1/{parent}/trials:suggest",
        t.struct(
            {
                "parent": t.string(),
                "suggestionCount": t.integer(),
                "clientId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning__OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStudiesTrialsComplete"] = ml.post(
        "v1/{parent}/trials:suggest",
        t.struct(
            {
                "parent": t.string(),
                "suggestionCount": t.integer(),
                "clientId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning__OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStudiesTrialsCreate"] = ml.post(
        "v1/{parent}/trials:suggest",
        t.struct(
            {
                "parent": t.string(),
                "suggestionCount": t.integer(),
                "clientId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning__OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStudiesTrialsList"] = ml.post(
        "v1/{parent}/trials:suggest",
        t.struct(
            {
                "parent": t.string(),
                "suggestionCount": t.integer(),
                "clientId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning__OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStudiesTrialsListOptimalTrials"] = ml.post(
        "v1/{parent}/trials:suggest",
        t.struct(
            {
                "parent": t.string(),
                "suggestionCount": t.integer(),
                "clientId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning__OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStudiesTrialsSuggest"] = ml.post(
        "v1/{parent}/trials:suggest",
        t.struct(
            {
                "parent": t.string(),
                "suggestionCount": t.integer(),
                "clientId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunning__OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsGetIamPolicy"] = ml.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudMlV1__ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsPatch"] = ml.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudMlV1__ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsCancel"] = ml.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudMlV1__ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsGet"] = ml.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudMlV1__ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsTestIamPermissions"] = ml.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudMlV1__ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsSetIamPolicy"] = ml.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudMlV1__ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsCreate"] = ml.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudMlV1__ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsList"] = ml.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudMlV1__ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="ml", renames=renames, types=types, functions=functions)
