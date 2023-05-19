from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_dataproc() -> Import:
    dataproc = HTTPRuntime("https://dataproc.googleapis.com/")

    renames = {
        "ErrorResponse": "_dataproc_1_ErrorResponse",
        "SparkRBatchIn": "_dataproc_2_SparkRBatchIn",
        "SparkRBatchOut": "_dataproc_3_SparkRBatchOut",
        "AcceleratorConfigIn": "_dataproc_4_AcceleratorConfigIn",
        "AcceleratorConfigOut": "_dataproc_5_AcceleratorConfigOut",
        "JobReferenceIn": "_dataproc_6_JobReferenceIn",
        "JobReferenceOut": "_dataproc_7_JobReferenceOut",
        "SparkStandaloneAutoscalingConfigIn": "_dataproc_8_SparkStandaloneAutoscalingConfigIn",
        "SparkStandaloneAutoscalingConfigOut": "_dataproc_9_SparkStandaloneAutoscalingConfigOut",
        "SparkSqlJobIn": "_dataproc_10_SparkSqlJobIn",
        "SparkSqlJobOut": "_dataproc_11_SparkSqlJobOut",
        "JobStatusIn": "_dataproc_12_JobStatusIn",
        "JobStatusOut": "_dataproc_13_JobStatusOut",
        "SparkRJobIn": "_dataproc_14_SparkRJobIn",
        "SparkRJobOut": "_dataproc_15_SparkRJobOut",
        "ShieldedInstanceConfigIn": "_dataproc_16_ShieldedInstanceConfigIn",
        "ShieldedInstanceConfigOut": "_dataproc_17_ShieldedInstanceConfigOut",
        "ListWorkflowTemplatesResponseIn": "_dataproc_18_ListWorkflowTemplatesResponseIn",
        "ListWorkflowTemplatesResponseOut": "_dataproc_19_ListWorkflowTemplatesResponseOut",
        "LoggingConfigIn": "_dataproc_20_LoggingConfigIn",
        "LoggingConfigOut": "_dataproc_21_LoggingConfigOut",
        "PySparkJobIn": "_dataproc_22_PySparkJobIn",
        "PySparkJobOut": "_dataproc_23_PySparkJobOut",
        "DiagnoseClusterResultsIn": "_dataproc_24_DiagnoseClusterResultsIn",
        "DiagnoseClusterResultsOut": "_dataproc_25_DiagnoseClusterResultsOut",
        "LifecycleConfigIn": "_dataproc_26_LifecycleConfigIn",
        "LifecycleConfigOut": "_dataproc_27_LifecycleConfigOut",
        "StatusIn": "_dataproc_28_StatusIn",
        "StatusOut": "_dataproc_29_StatusOut",
        "JobPlacementIn": "_dataproc_30_JobPlacementIn",
        "JobPlacementOut": "_dataproc_31_JobPlacementOut",
        "ClusterMetricsIn": "_dataproc_32_ClusterMetricsIn",
        "ClusterMetricsOut": "_dataproc_33_ClusterMetricsOut",
        "MetastoreConfigIn": "_dataproc_34_MetastoreConfigIn",
        "MetastoreConfigOut": "_dataproc_35_MetastoreConfigOut",
        "RuntimeConfigIn": "_dataproc_36_RuntimeConfigIn",
        "RuntimeConfigOut": "_dataproc_37_RuntimeConfigOut",
        "GkeNodePoolAcceleratorConfigIn": "_dataproc_38_GkeNodePoolAcceleratorConfigIn",
        "GkeNodePoolAcceleratorConfigOut": "_dataproc_39_GkeNodePoolAcceleratorConfigOut",
        "NodeGroupAffinityIn": "_dataproc_40_NodeGroupAffinityIn",
        "NodeGroupAffinityOut": "_dataproc_41_NodeGroupAffinityOut",
        "EnvironmentConfigIn": "_dataproc_42_EnvironmentConfigIn",
        "EnvironmentConfigOut": "_dataproc_43_EnvironmentConfigOut",
        "ClusterSelectorIn": "_dataproc_44_ClusterSelectorIn",
        "ClusterSelectorOut": "_dataproc_45_ClusterSelectorOut",
        "ConfidentialInstanceConfigIn": "_dataproc_46_ConfidentialInstanceConfigIn",
        "ConfidentialInstanceConfigOut": "_dataproc_47_ConfidentialInstanceConfigOut",
        "AuxiliaryNodeGroupIn": "_dataproc_48_AuxiliaryNodeGroupIn",
        "AuxiliaryNodeGroupOut": "_dataproc_49_AuxiliaryNodeGroupOut",
        "DataprocMetricConfigIn": "_dataproc_50_DataprocMetricConfigIn",
        "DataprocMetricConfigOut": "_dataproc_51_DataprocMetricConfigOut",
        "BatchIn": "_dataproc_52_BatchIn",
        "BatchOut": "_dataproc_53_BatchOut",
        "ManagedGroupConfigIn": "_dataproc_54_ManagedGroupConfigIn",
        "ManagedGroupConfigOut": "_dataproc_55_ManagedGroupConfigOut",
        "SparkSqlBatchIn": "_dataproc_56_SparkSqlBatchIn",
        "SparkSqlBatchOut": "_dataproc_57_SparkSqlBatchOut",
        "UsageSnapshotIn": "_dataproc_58_UsageSnapshotIn",
        "UsageSnapshotOut": "_dataproc_59_UsageSnapshotOut",
        "EndpointConfigIn": "_dataproc_60_EndpointConfigIn",
        "EndpointConfigOut": "_dataproc_61_EndpointConfigOut",
        "InjectCredentialsRequestIn": "_dataproc_62_InjectCredentialsRequestIn",
        "InjectCredentialsRequestOut": "_dataproc_63_InjectCredentialsRequestOut",
        "InstanceGroupConfigIn": "_dataproc_64_InstanceGroupConfigIn",
        "InstanceGroupConfigOut": "_dataproc_65_InstanceGroupConfigOut",
        "BasicYarnAutoscalingConfigIn": "_dataproc_66_BasicYarnAutoscalingConfigIn",
        "BasicYarnAutoscalingConfigOut": "_dataproc_67_BasicYarnAutoscalingConfigOut",
        "BatchOperationMetadataIn": "_dataproc_68_BatchOperationMetadataIn",
        "BatchOperationMetadataOut": "_dataproc_69_BatchOperationMetadataOut",
        "ReservationAffinityIn": "_dataproc_70_ReservationAffinityIn",
        "ReservationAffinityOut": "_dataproc_71_ReservationAffinityOut",
        "YarnApplicationIn": "_dataproc_72_YarnApplicationIn",
        "YarnApplicationOut": "_dataproc_73_YarnApplicationOut",
        "RegexValidationIn": "_dataproc_74_RegexValidationIn",
        "RegexValidationOut": "_dataproc_75_RegexValidationOut",
        "NodePoolIn": "_dataproc_76_NodePoolIn",
        "NodePoolOut": "_dataproc_77_NodePoolOut",
        "MetricIn": "_dataproc_78_MetricIn",
        "MetricOut": "_dataproc_79_MetricOut",
        "WorkflowGraphIn": "_dataproc_80_WorkflowGraphIn",
        "WorkflowGraphOut": "_dataproc_81_WorkflowGraphOut",
        "ResizeNodeGroupRequestIn": "_dataproc_82_ResizeNodeGroupRequestIn",
        "ResizeNodeGroupRequestOut": "_dataproc_83_ResizeNodeGroupRequestOut",
        "GkeNodePoolConfigIn": "_dataproc_84_GkeNodePoolConfigIn",
        "GkeNodePoolConfigOut": "_dataproc_85_GkeNodePoolConfigOut",
        "ManagedClusterIn": "_dataproc_86_ManagedClusterIn",
        "ManagedClusterOut": "_dataproc_87_ManagedClusterOut",
        "SoftwareConfigIn": "_dataproc_88_SoftwareConfigIn",
        "SoftwareConfigOut": "_dataproc_89_SoftwareConfigOut",
        "KubernetesSoftwareConfigIn": "_dataproc_90_KubernetesSoftwareConfigIn",
        "KubernetesSoftwareConfigOut": "_dataproc_91_KubernetesSoftwareConfigOut",
        "TemplateParameterIn": "_dataproc_92_TemplateParameterIn",
        "TemplateParameterOut": "_dataproc_93_TemplateParameterOut",
        "NodeGroupOperationMetadataIn": "_dataproc_94_NodeGroupOperationMetadataIn",
        "NodeGroupOperationMetadataOut": "_dataproc_95_NodeGroupOperationMetadataOut",
        "DiagnoseClusterRequestIn": "_dataproc_96_DiagnoseClusterRequestIn",
        "DiagnoseClusterRequestOut": "_dataproc_97_DiagnoseClusterRequestOut",
        "BindingIn": "_dataproc_98_BindingIn",
        "BindingOut": "_dataproc_99_BindingOut",
        "JobMetadataIn": "_dataproc_100_JobMetadataIn",
        "JobMetadataOut": "_dataproc_101_JobMetadataOut",
        "ListAutoscalingPoliciesResponseIn": "_dataproc_102_ListAutoscalingPoliciesResponseIn",
        "ListAutoscalingPoliciesResponseOut": "_dataproc_103_ListAutoscalingPoliciesResponseOut",
        "NodeInitializationActionIn": "_dataproc_104_NodeInitializationActionIn",
        "NodeInitializationActionOut": "_dataproc_105_NodeInitializationActionOut",
        "QueryListIn": "_dataproc_106_QueryListIn",
        "QueryListOut": "_dataproc_107_QueryListOut",
        "KubernetesClusterConfigIn": "_dataproc_108_KubernetesClusterConfigIn",
        "KubernetesClusterConfigOut": "_dataproc_109_KubernetesClusterConfigOut",
        "GkeNodeConfigIn": "_dataproc_110_GkeNodeConfigIn",
        "GkeNodeConfigOut": "_dataproc_111_GkeNodeConfigOut",
        "ExprIn": "_dataproc_112_ExprIn",
        "ExprOut": "_dataproc_113_ExprOut",
        "RepairClusterRequestIn": "_dataproc_114_RepairClusterRequestIn",
        "RepairClusterRequestOut": "_dataproc_115_RepairClusterRequestOut",
        "WorkflowTemplateIn": "_dataproc_116_WorkflowTemplateIn",
        "WorkflowTemplateOut": "_dataproc_117_WorkflowTemplateOut",
        "GetPolicyOptionsIn": "_dataproc_118_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_dataproc_119_GetPolicyOptionsOut",
        "NamespacedGkeDeploymentTargetIn": "_dataproc_120_NamespacedGkeDeploymentTargetIn",
        "NamespacedGkeDeploymentTargetOut": "_dataproc_121_NamespacedGkeDeploymentTargetOut",
        "ListBatchesResponseIn": "_dataproc_122_ListBatchesResponseIn",
        "ListBatchesResponseOut": "_dataproc_123_ListBatchesResponseOut",
        "StopClusterRequestIn": "_dataproc_124_StopClusterRequestIn",
        "StopClusterRequestOut": "_dataproc_125_StopClusterRequestOut",
        "GkeNodePoolAutoscalingConfigIn": "_dataproc_126_GkeNodePoolAutoscalingConfigIn",
        "GkeNodePoolAutoscalingConfigOut": "_dataproc_127_GkeNodePoolAutoscalingConfigOut",
        "GkeNodePoolTargetIn": "_dataproc_128_GkeNodePoolTargetIn",
        "GkeNodePoolTargetOut": "_dataproc_129_GkeNodePoolTargetOut",
        "JobIn": "_dataproc_130_JobIn",
        "JobOut": "_dataproc_131_JobOut",
        "OrderedJobIn": "_dataproc_132_OrderedJobIn",
        "OrderedJobOut": "_dataproc_133_OrderedJobOut",
        "ListJobsResponseIn": "_dataproc_134_ListJobsResponseIn",
        "ListJobsResponseOut": "_dataproc_135_ListJobsResponseOut",
        "CancelJobRequestIn": "_dataproc_136_CancelJobRequestIn",
        "CancelJobRequestOut": "_dataproc_137_CancelJobRequestOut",
        "SecurityConfigIn": "_dataproc_138_SecurityConfigIn",
        "SecurityConfigOut": "_dataproc_139_SecurityConfigOut",
        "RuntimeInfoIn": "_dataproc_140_RuntimeInfoIn",
        "RuntimeInfoOut": "_dataproc_141_RuntimeInfoOut",
        "PeripheralsConfigIn": "_dataproc_142_PeripheralsConfigIn",
        "PeripheralsConfigOut": "_dataproc_143_PeripheralsConfigOut",
        "WorkflowMetadataIn": "_dataproc_144_WorkflowMetadataIn",
        "WorkflowMetadataOut": "_dataproc_145_WorkflowMetadataOut",
        "KerberosConfigIn": "_dataproc_146_KerberosConfigIn",
        "KerberosConfigOut": "_dataproc_147_KerberosConfigOut",
        "VirtualClusterConfigIn": "_dataproc_148_VirtualClusterConfigIn",
        "VirtualClusterConfigOut": "_dataproc_149_VirtualClusterConfigOut",
        "InstanceReferenceIn": "_dataproc_150_InstanceReferenceIn",
        "InstanceReferenceOut": "_dataproc_151_InstanceReferenceOut",
        "BasicAutoscalingAlgorithmIn": "_dataproc_152_BasicAutoscalingAlgorithmIn",
        "BasicAutoscalingAlgorithmOut": "_dataproc_153_BasicAutoscalingAlgorithmOut",
        "ParameterValidationIn": "_dataproc_154_ParameterValidationIn",
        "ParameterValidationOut": "_dataproc_155_ParameterValidationOut",
        "SetIamPolicyRequestIn": "_dataproc_156_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_dataproc_157_SetIamPolicyRequestOut",
        "InstantiateWorkflowTemplateRequestIn": "_dataproc_158_InstantiateWorkflowTemplateRequestIn",
        "InstantiateWorkflowTemplateRequestOut": "_dataproc_159_InstantiateWorkflowTemplateRequestOut",
        "EncryptionConfigIn": "_dataproc_160_EncryptionConfigIn",
        "EncryptionConfigOut": "_dataproc_161_EncryptionConfigOut",
        "ClusterConfigIn": "_dataproc_162_ClusterConfigIn",
        "ClusterConfigOut": "_dataproc_163_ClusterConfigOut",
        "AutoscalingConfigIn": "_dataproc_164_AutoscalingConfigIn",
        "AutoscalingConfigOut": "_dataproc_165_AutoscalingConfigOut",
        "GceClusterConfigIn": "_dataproc_166_GceClusterConfigIn",
        "GceClusterConfigOut": "_dataproc_167_GceClusterConfigOut",
        "ClusterOperationStatusIn": "_dataproc_168_ClusterOperationStatusIn",
        "ClusterOperationStatusOut": "_dataproc_169_ClusterOperationStatusOut",
        "ListClustersResponseIn": "_dataproc_170_ListClustersResponseIn",
        "ListClustersResponseOut": "_dataproc_171_ListClustersResponseOut",
        "SparkBatchIn": "_dataproc_172_SparkBatchIn",
        "SparkBatchOut": "_dataproc_173_SparkBatchOut",
        "GetIamPolicyRequestIn": "_dataproc_174_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_dataproc_175_GetIamPolicyRequestOut",
        "PrestoJobIn": "_dataproc_176_PrestoJobIn",
        "PrestoJobOut": "_dataproc_177_PrestoJobOut",
        "PolicyIn": "_dataproc_178_PolicyIn",
        "PolicyOut": "_dataproc_179_PolicyOut",
        "WorkflowTemplatePlacementIn": "_dataproc_180_WorkflowTemplatePlacementIn",
        "WorkflowTemplatePlacementOut": "_dataproc_181_WorkflowTemplatePlacementOut",
        "ExecutionConfigIn": "_dataproc_182_ExecutionConfigIn",
        "ExecutionConfigOut": "_dataproc_183_ExecutionConfigOut",
        "OperationIn": "_dataproc_184_OperationIn",
        "OperationOut": "_dataproc_185_OperationOut",
        "AuxiliaryServicesConfigIn": "_dataproc_186_AuxiliaryServicesConfigIn",
        "AuxiliaryServicesConfigOut": "_dataproc_187_AuxiliaryServicesConfigOut",
        "ClusterIn": "_dataproc_188_ClusterIn",
        "ClusterOut": "_dataproc_189_ClusterOut",
        "ValueValidationIn": "_dataproc_190_ValueValidationIn",
        "ValueValidationOut": "_dataproc_191_ValueValidationOut",
        "JobSchedulingIn": "_dataproc_192_JobSchedulingIn",
        "JobSchedulingOut": "_dataproc_193_JobSchedulingOut",
        "HadoopJobIn": "_dataproc_194_HadoopJobIn",
        "HadoopJobOut": "_dataproc_195_HadoopJobOut",
        "ListOperationsResponseIn": "_dataproc_196_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_dataproc_197_ListOperationsResponseOut",
        "InstanceGroupAutoscalingPolicyConfigIn": "_dataproc_198_InstanceGroupAutoscalingPolicyConfigIn",
        "InstanceGroupAutoscalingPolicyConfigOut": "_dataproc_199_InstanceGroupAutoscalingPolicyConfigOut",
        "TestIamPermissionsResponseIn": "_dataproc_200_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_dataproc_201_TestIamPermissionsResponseOut",
        "StateHistoryIn": "_dataproc_202_StateHistoryIn",
        "StateHistoryOut": "_dataproc_203_StateHistoryOut",
        "TestIamPermissionsRequestIn": "_dataproc_204_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_dataproc_205_TestIamPermissionsRequestOut",
        "PySparkBatchIn": "_dataproc_206_PySparkBatchIn",
        "PySparkBatchOut": "_dataproc_207_PySparkBatchOut",
        "GkeClusterConfigIn": "_dataproc_208_GkeClusterConfigIn",
        "GkeClusterConfigOut": "_dataproc_209_GkeClusterConfigOut",
        "WorkflowNodeIn": "_dataproc_210_WorkflowNodeIn",
        "WorkflowNodeOut": "_dataproc_211_WorkflowNodeOut",
        "ClusterStatusIn": "_dataproc_212_ClusterStatusIn",
        "ClusterStatusOut": "_dataproc_213_ClusterStatusOut",
        "IdentityConfigIn": "_dataproc_214_IdentityConfigIn",
        "IdentityConfigOut": "_dataproc_215_IdentityConfigOut",
        "StartClusterRequestIn": "_dataproc_216_StartClusterRequestIn",
        "StartClusterRequestOut": "_dataproc_217_StartClusterRequestOut",
        "SparkJobIn": "_dataproc_218_SparkJobIn",
        "SparkJobOut": "_dataproc_219_SparkJobOut",
        "ClusterOperationMetadataIn": "_dataproc_220_ClusterOperationMetadataIn",
        "ClusterOperationMetadataOut": "_dataproc_221_ClusterOperationMetadataOut",
        "IntervalIn": "_dataproc_222_IntervalIn",
        "IntervalOut": "_dataproc_223_IntervalOut",
        "TrinoJobIn": "_dataproc_224_TrinoJobIn",
        "TrinoJobOut": "_dataproc_225_TrinoJobOut",
        "EmptyIn": "_dataproc_226_EmptyIn",
        "EmptyOut": "_dataproc_227_EmptyOut",
        "DiskConfigIn": "_dataproc_228_DiskConfigIn",
        "DiskConfigOut": "_dataproc_229_DiskConfigOut",
        "NodeGroupIn": "_dataproc_230_NodeGroupIn",
        "NodeGroupOut": "_dataproc_231_NodeGroupOut",
        "PigJobIn": "_dataproc_232_PigJobIn",
        "PigJobOut": "_dataproc_233_PigJobOut",
        "HiveJobIn": "_dataproc_234_HiveJobIn",
        "HiveJobOut": "_dataproc_235_HiveJobOut",
        "SparkHistoryServerConfigIn": "_dataproc_236_SparkHistoryServerConfigIn",
        "SparkHistoryServerConfigOut": "_dataproc_237_SparkHistoryServerConfigOut",
        "ClusterOperationIn": "_dataproc_238_ClusterOperationIn",
        "ClusterOperationOut": "_dataproc_239_ClusterOperationOut",
        "SubmitJobRequestIn": "_dataproc_240_SubmitJobRequestIn",
        "SubmitJobRequestOut": "_dataproc_241_SubmitJobRequestOut",
        "DriverSchedulingConfigIn": "_dataproc_242_DriverSchedulingConfigIn",
        "DriverSchedulingConfigOut": "_dataproc_243_DriverSchedulingConfigOut",
        "SessionOperationMetadataIn": "_dataproc_244_SessionOperationMetadataIn",
        "SessionOperationMetadataOut": "_dataproc_245_SessionOperationMetadataOut",
        "AutoscalingPolicyIn": "_dataproc_246_AutoscalingPolicyIn",
        "AutoscalingPolicyOut": "_dataproc_247_AutoscalingPolicyOut",
        "UsageMetricsIn": "_dataproc_248_UsageMetricsIn",
        "UsageMetricsOut": "_dataproc_249_UsageMetricsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SparkRBatchIn"] = t.struct(
        {
            "archiveUris": t.array(t.string()).optional(),
            "mainRFileUri": t.string(),
            "fileUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
        }
    ).named(renames["SparkRBatchIn"])
    types["SparkRBatchOut"] = t.struct(
        {
            "archiveUris": t.array(t.string()).optional(),
            "mainRFileUri": t.string(),
            "fileUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkRBatchOut"])
    types["AcceleratorConfigIn"] = t.struct(
        {
            "acceleratorTypeUri": t.string().optional(),
            "acceleratorCount": t.integer().optional(),
        }
    ).named(renames["AcceleratorConfigIn"])
    types["AcceleratorConfigOut"] = t.struct(
        {
            "acceleratorTypeUri": t.string().optional(),
            "acceleratorCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorConfigOut"])
    types["JobReferenceIn"] = t.struct(
        {"projectId": t.string().optional(), "jobId": t.string().optional()}
    ).named(renames["JobReferenceIn"])
    types["JobReferenceOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "jobId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobReferenceOut"])
    types["SparkStandaloneAutoscalingConfigIn"] = t.struct(
        {
            "gracefulDecommissionTimeout": t.string(),
            "scaleUpFactor": t.number(),
            "scaleDownMinWorkerFraction": t.number().optional(),
            "scaleDownFactor": t.number(),
            "scaleUpMinWorkerFraction": t.number().optional(),
        }
    ).named(renames["SparkStandaloneAutoscalingConfigIn"])
    types["SparkStandaloneAutoscalingConfigOut"] = t.struct(
        {
            "gracefulDecommissionTimeout": t.string(),
            "scaleUpFactor": t.number(),
            "scaleDownMinWorkerFraction": t.number().optional(),
            "scaleDownFactor": t.number(),
            "scaleUpMinWorkerFraction": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkStandaloneAutoscalingConfigOut"])
    types["SparkSqlJobIn"] = t.struct(
        {
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "queryFileUri": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
        }
    ).named(renames["SparkSqlJobIn"])
    types["SparkSqlJobOut"] = t.struct(
        {
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "queryFileUri": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkSqlJobOut"])
    types["JobStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["JobStatusIn"]
    )
    types["JobStatusOut"] = t.struct(
        {
            "substate": t.string().optional(),
            "state": t.string().optional(),
            "stateStartTime": t.string().optional(),
            "details": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatusOut"])
    types["SparkRJobIn"] = t.struct(
        {
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "args": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "mainRFileUri": t.string(),
            "fileUris": t.array(t.string()).optional(),
        }
    ).named(renames["SparkRJobIn"])
    types["SparkRJobOut"] = t.struct(
        {
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "args": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "mainRFileUri": t.string(),
            "fileUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkRJobOut"])
    types["ShieldedInstanceConfigIn"] = t.struct(
        {
            "enableVtpm": t.boolean().optional(),
            "enableIntegrityMonitoring": t.boolean().optional(),
            "enableSecureBoot": t.boolean().optional(),
        }
    ).named(renames["ShieldedInstanceConfigIn"])
    types["ShieldedInstanceConfigOut"] = t.struct(
        {
            "enableVtpm": t.boolean().optional(),
            "enableIntegrityMonitoring": t.boolean().optional(),
            "enableSecureBoot": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShieldedInstanceConfigOut"])
    types["ListWorkflowTemplatesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ListWorkflowTemplatesResponseIn"])
    types["ListWorkflowTemplatesResponseOut"] = t.struct(
        {
            "templates": t.array(t.proxy(renames["WorkflowTemplateOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkflowTemplatesResponseOut"])
    types["LoggingConfigIn"] = t.struct(
        {"driverLogLevels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["LoggingConfigIn"])
    types["LoggingConfigOut"] = t.struct(
        {
            "driverLogLevels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingConfigOut"])
    types["PySparkJobIn"] = t.struct(
        {
            "mainPythonFileUri": t.string(),
            "fileUris": t.array(t.string()).optional(),
            "pythonFileUris": t.array(t.string()).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "args": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "archiveUris": t.array(t.string()).optional(),
        }
    ).named(renames["PySparkJobIn"])
    types["PySparkJobOut"] = t.struct(
        {
            "mainPythonFileUri": t.string(),
            "fileUris": t.array(t.string()).optional(),
            "pythonFileUris": t.array(t.string()).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "args": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PySparkJobOut"])
    types["DiagnoseClusterResultsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DiagnoseClusterResultsIn"]
    )
    types["DiagnoseClusterResultsOut"] = t.struct(
        {
            "outputUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiagnoseClusterResultsOut"])
    types["LifecycleConfigIn"] = t.struct(
        {
            "autoDeleteTtl": t.string().optional(),
            "autoDeleteTime": t.string().optional(),
            "idleDeleteTtl": t.string().optional(),
        }
    ).named(renames["LifecycleConfigIn"])
    types["LifecycleConfigOut"] = t.struct(
        {
            "autoDeleteTtl": t.string().optional(),
            "autoDeleteTime": t.string().optional(),
            "idleStartTime": t.string().optional(),
            "idleDeleteTtl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LifecycleConfigOut"])
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
    types["JobPlacementIn"] = t.struct(
        {
            "clusterLabels": t.struct({"_": t.string().optional()}).optional(),
            "clusterName": t.string(),
        }
    ).named(renames["JobPlacementIn"])
    types["JobPlacementOut"] = t.struct(
        {
            "clusterLabels": t.struct({"_": t.string().optional()}).optional(),
            "clusterName": t.string(),
            "clusterUuid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobPlacementOut"])
    types["ClusterMetricsIn"] = t.struct(
        {
            "hdfsMetrics": t.struct({"_": t.string().optional()}).optional(),
            "yarnMetrics": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ClusterMetricsIn"])
    types["ClusterMetricsOut"] = t.struct(
        {
            "hdfsMetrics": t.struct({"_": t.string().optional()}).optional(),
            "yarnMetrics": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterMetricsOut"])
    types["MetastoreConfigIn"] = t.struct(
        {"dataprocMetastoreService": t.string()}
    ).named(renames["MetastoreConfigIn"])
    types["MetastoreConfigOut"] = t.struct(
        {
            "dataprocMetastoreService": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetastoreConfigOut"])
    types["RuntimeConfigIn"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "containerImage": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["RuntimeConfigIn"])
    types["RuntimeConfigOut"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "containerImage": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeConfigOut"])
    types["GkeNodePoolAcceleratorConfigIn"] = t.struct(
        {
            "acceleratorCount": t.string().optional(),
            "gpuPartitionSize": t.string().optional(),
            "acceleratorType": t.string().optional(),
        }
    ).named(renames["GkeNodePoolAcceleratorConfigIn"])
    types["GkeNodePoolAcceleratorConfigOut"] = t.struct(
        {
            "acceleratorCount": t.string().optional(),
            "gpuPartitionSize": t.string().optional(),
            "acceleratorType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNodePoolAcceleratorConfigOut"])
    types["NodeGroupAffinityIn"] = t.struct({"nodeGroupUri": t.string()}).named(
        renames["NodeGroupAffinityIn"]
    )
    types["NodeGroupAffinityOut"] = t.struct(
        {
            "nodeGroupUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeGroupAffinityOut"])
    types["EnvironmentConfigIn"] = t.struct(
        {
            "peripheralsConfig": t.proxy(renames["PeripheralsConfigIn"]).optional(),
            "executionConfig": t.proxy(renames["ExecutionConfigIn"]).optional(),
        }
    ).named(renames["EnvironmentConfigIn"])
    types["EnvironmentConfigOut"] = t.struct(
        {
            "peripheralsConfig": t.proxy(renames["PeripheralsConfigOut"]).optional(),
            "executionConfig": t.proxy(renames["ExecutionConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentConfigOut"])
    types["ClusterSelectorIn"] = t.struct(
        {
            "clusterLabels": t.struct({"_": t.string().optional()}),
            "zone": t.string().optional(),
        }
    ).named(renames["ClusterSelectorIn"])
    types["ClusterSelectorOut"] = t.struct(
        {
            "clusterLabels": t.struct({"_": t.string().optional()}),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterSelectorOut"])
    types["ConfidentialInstanceConfigIn"] = t.struct(
        {"enableConfidentialCompute": t.boolean().optional()}
    ).named(renames["ConfidentialInstanceConfigIn"])
    types["ConfidentialInstanceConfigOut"] = t.struct(
        {
            "enableConfidentialCompute": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfidentialInstanceConfigOut"])
    types["AuxiliaryNodeGroupIn"] = t.struct(
        {
            "nodeGroup": t.proxy(renames["NodeGroupIn"]),
            "nodeGroupId": t.string().optional(),
        }
    ).named(renames["AuxiliaryNodeGroupIn"])
    types["AuxiliaryNodeGroupOut"] = t.struct(
        {
            "nodeGroup": t.proxy(renames["NodeGroupOut"]),
            "nodeGroupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuxiliaryNodeGroupOut"])
    types["DataprocMetricConfigIn"] = t.struct(
        {"metrics": t.array(t.proxy(renames["MetricIn"]))}
    ).named(renames["DataprocMetricConfigIn"])
    types["DataprocMetricConfigOut"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataprocMetricConfigOut"])
    types["BatchIn"] = t.struct(
        {
            "environmentConfig": t.proxy(renames["EnvironmentConfigIn"]).optional(),
            "runtimeConfig": t.proxy(renames["RuntimeConfigIn"]).optional(),
            "pysparkBatch": t.proxy(renames["PySparkBatchIn"]).optional(),
            "sparkRBatch": t.proxy(renames["SparkRBatchIn"]).optional(),
            "sparkBatch": t.proxy(renames["SparkBatchIn"]).optional(),
            "sparkSqlBatch": t.proxy(renames["SparkSqlBatchIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["BatchIn"])
    types["BatchOut"] = t.struct(
        {
            "environmentConfig": t.proxy(renames["EnvironmentConfigOut"]).optional(),
            "uuid": t.string().optional(),
            "createTime": t.string().optional(),
            "stateHistory": t.array(t.proxy(renames["StateHistoryOut"])).optional(),
            "runtimeConfig": t.proxy(renames["RuntimeConfigOut"]).optional(),
            "pysparkBatch": t.proxy(renames["PySparkBatchOut"]).optional(),
            "creator": t.string().optional(),
            "sparkRBatch": t.proxy(renames["SparkRBatchOut"]).optional(),
            "sparkBatch": t.proxy(renames["SparkBatchOut"]).optional(),
            "sparkSqlBatch": t.proxy(renames["SparkSqlBatchOut"]).optional(),
            "state": t.string().optional(),
            "runtimeInfo": t.proxy(renames["RuntimeInfoOut"]).optional(),
            "stateTime": t.string().optional(),
            "name": t.string().optional(),
            "operation": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "stateMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchOut"])
    types["ManagedGroupConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ManagedGroupConfigIn"]
    )
    types["ManagedGroupConfigOut"] = t.struct(
        {
            "instanceTemplateName": t.string().optional(),
            "instanceGroupManagerName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedGroupConfigOut"])
    types["SparkSqlBatchIn"] = t.struct(
        {
            "queryVariables": t.struct({"_": t.string().optional()}).optional(),
            "queryFileUri": t.string(),
            "jarFileUris": t.array(t.string()).optional(),
        }
    ).named(renames["SparkSqlBatchIn"])
    types["SparkSqlBatchOut"] = t.struct(
        {
            "queryVariables": t.struct({"_": t.string().optional()}).optional(),
            "queryFileUri": t.string(),
            "jarFileUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkSqlBatchOut"])
    types["UsageSnapshotIn"] = t.struct(
        {
            "milliDcu": t.string().optional(),
            "shuffleStorageGb": t.string().optional(),
            "snapshotTime": t.string().optional(),
        }
    ).named(renames["UsageSnapshotIn"])
    types["UsageSnapshotOut"] = t.struct(
        {
            "milliDcu": t.string().optional(),
            "shuffleStorageGb": t.string().optional(),
            "snapshotTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageSnapshotOut"])
    types["EndpointConfigIn"] = t.struct(
        {"enableHttpPortAccess": t.boolean().optional()}
    ).named(renames["EndpointConfigIn"])
    types["EndpointConfigOut"] = t.struct(
        {
            "httpPorts": t.struct({"_": t.string().optional()}).optional(),
            "enableHttpPortAccess": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointConfigOut"])
    types["InjectCredentialsRequestIn"] = t.struct(
        {"clusterUuid": t.string(), "credentialsCiphertext": t.string()}
    ).named(renames["InjectCredentialsRequestIn"])
    types["InjectCredentialsRequestOut"] = t.struct(
        {
            "clusterUuid": t.string(),
            "credentialsCiphertext": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InjectCredentialsRequestOut"])
    types["InstanceGroupConfigIn"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "minCpuPlatform": t.string().optional(),
            "diskConfig": t.proxy(renames["DiskConfigIn"]).optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorConfigIn"])).optional(),
            "machineTypeUri": t.string().optional(),
            "numInstances": t.integer().optional(),
            "preemptibility": t.string().optional(),
        }
    ).named(renames["InstanceGroupConfigIn"])
    types["InstanceGroupConfigOut"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "minCpuPlatform": t.string().optional(),
            "diskConfig": t.proxy(renames["DiskConfigOut"]).optional(),
            "instanceReferences": t.array(
                t.proxy(renames["InstanceReferenceOut"])
            ).optional(),
            "managedGroupConfig": t.proxy(renames["ManagedGroupConfigOut"]).optional(),
            "instanceNames": t.array(t.string()).optional(),
            "isPreemptible": t.boolean().optional(),
            "accelerators": t.array(
                t.proxy(renames["AcceleratorConfigOut"])
            ).optional(),
            "machineTypeUri": t.string().optional(),
            "numInstances": t.integer().optional(),
            "preemptibility": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceGroupConfigOut"])
    types["BasicYarnAutoscalingConfigIn"] = t.struct(
        {
            "scaleDownMinWorkerFraction": t.number().optional(),
            "scaleUpFactor": t.number(),
            "gracefulDecommissionTimeout": t.string(),
            "scaleUpMinWorkerFraction": t.number().optional(),
            "scaleDownFactor": t.number(),
        }
    ).named(renames["BasicYarnAutoscalingConfigIn"])
    types["BasicYarnAutoscalingConfigOut"] = t.struct(
        {
            "scaleDownMinWorkerFraction": t.number().optional(),
            "scaleUpFactor": t.number(),
            "gracefulDecommissionTimeout": t.string(),
            "scaleUpMinWorkerFraction": t.number().optional(),
            "scaleDownFactor": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicYarnAutoscalingConfigOut"])
    types["BatchOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "batch": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "doneTime": t.string().optional(),
            "operationType": t.string().optional(),
            "batchUuid": t.string().optional(),
        }
    ).named(renames["BatchOperationMetadataIn"])
    types["BatchOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "batch": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "doneTime": t.string().optional(),
            "operationType": t.string().optional(),
            "batchUuid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchOperationMetadataOut"])
    types["ReservationAffinityIn"] = t.struct(
        {
            "consumeReservationType": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "key": t.string().optional(),
        }
    ).named(renames["ReservationAffinityIn"])
    types["ReservationAffinityOut"] = t.struct(
        {
            "consumeReservationType": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReservationAffinityOut"])
    types["YarnApplicationIn"] = t.struct(
        {
            "state": t.string(),
            "progress": t.number(),
            "name": t.string(),
            "trackingUrl": t.string().optional(),
        }
    ).named(renames["YarnApplicationIn"])
    types["YarnApplicationOut"] = t.struct(
        {
            "state": t.string(),
            "progress": t.number(),
            "name": t.string(),
            "trackingUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YarnApplicationOut"])
    types["RegexValidationIn"] = t.struct({"regexes": t.array(t.string())}).named(
        renames["RegexValidationIn"]
    )
    types["RegexValidationOut"] = t.struct(
        {
            "regexes": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegexValidationOut"])
    types["NodePoolIn"] = t.struct(
        {
            "instanceNames": t.array(t.string()).optional(),
            "repairAction": t.string(),
            "id": t.string(),
        }
    ).named(renames["NodePoolIn"])
    types["NodePoolOut"] = t.struct(
        {
            "instanceNames": t.array(t.string()).optional(),
            "repairAction": t.string(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolOut"])
    types["MetricIn"] = t.struct(
        {"metricOverrides": t.array(t.string()).optional(), "metricSource": t.string()}
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "metricOverrides": t.array(t.string()).optional(),
            "metricSource": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
    types["WorkflowGraphIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WorkflowGraphIn"]
    )
    types["WorkflowGraphOut"] = t.struct(
        {
            "nodes": t.array(t.proxy(renames["WorkflowNodeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowGraphOut"])
    types["ResizeNodeGroupRequestIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "size": t.integer(),
            "gracefulDecommissionTimeout": t.string().optional(),
        }
    ).named(renames["ResizeNodeGroupRequestIn"])
    types["ResizeNodeGroupRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "size": t.integer(),
            "gracefulDecommissionTimeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResizeNodeGroupRequestOut"])
    types["GkeNodePoolConfigIn"] = t.struct(
        {
            "autoscaling": t.proxy(
                renames["GkeNodePoolAutoscalingConfigIn"]
            ).optional(),
            "locations": t.array(t.string()).optional(),
            "config": t.proxy(renames["GkeNodeConfigIn"]).optional(),
        }
    ).named(renames["GkeNodePoolConfigIn"])
    types["GkeNodePoolConfigOut"] = t.struct(
        {
            "autoscaling": t.proxy(
                renames["GkeNodePoolAutoscalingConfigOut"]
            ).optional(),
            "locations": t.array(t.string()).optional(),
            "config": t.proxy(renames["GkeNodeConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNodePoolConfigOut"])
    types["ManagedClusterIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "config": t.proxy(renames["ClusterConfigIn"]),
            "clusterName": t.string(),
        }
    ).named(renames["ManagedClusterIn"])
    types["ManagedClusterOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "config": t.proxy(renames["ClusterConfigOut"]),
            "clusterName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedClusterOut"])
    types["SoftwareConfigIn"] = t.struct(
        {
            "imageVersion": t.string().optional(),
            "optionalComponents": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SoftwareConfigIn"])
    types["SoftwareConfigOut"] = t.struct(
        {
            "imageVersion": t.string().optional(),
            "optionalComponents": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SoftwareConfigOut"])
    types["KubernetesSoftwareConfigIn"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "componentVersion": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["KubernetesSoftwareConfigIn"])
    types["KubernetesSoftwareConfigOut"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "componentVersion": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesSoftwareConfigOut"])
    types["TemplateParameterIn"] = t.struct(
        {
            "name": t.string(),
            "validation": t.proxy(renames["ParameterValidationIn"]).optional(),
            "description": t.string().optional(),
            "fields": t.array(t.string()),
        }
    ).named(renames["TemplateParameterIn"])
    types["TemplateParameterOut"] = t.struct(
        {
            "name": t.string(),
            "validation": t.proxy(renames["ParameterValidationOut"]).optional(),
            "description": t.string().optional(),
            "fields": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TemplateParameterOut"])
    types["NodeGroupOperationMetadataIn"] = t.struct(
        {"operationType": t.string().optional()}
    ).named(renames["NodeGroupOperationMetadataIn"])
    types["NodeGroupOperationMetadataOut"] = t.struct(
        {
            "warnings": t.array(t.string()).optional(),
            "operationType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "nodeGroupId": t.string().optional(),
            "clusterUuid": t.string().optional(),
            "description": t.string().optional(),
            "statusHistory": t.array(
                t.proxy(renames["ClusterOperationStatusOut"])
            ).optional(),
            "status": t.proxy(renames["ClusterOperationStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeGroupOperationMetadataOut"])
    types["DiagnoseClusterRequestIn"] = t.struct(
        {
            "yarnApplicationIds": t.array(t.string()).optional(),
            "job": t.string().optional(),
            "diagnosisInterval": t.proxy(renames["IntervalIn"]).optional(),
            "jobs": t.array(t.string()).optional(),
            "yarnApplicationId": t.string().optional(),
        }
    ).named(renames["DiagnoseClusterRequestIn"])
    types["DiagnoseClusterRequestOut"] = t.struct(
        {
            "yarnApplicationIds": t.array(t.string()).optional(),
            "job": t.string().optional(),
            "diagnosisInterval": t.proxy(renames["IntervalOut"]).optional(),
            "jobs": t.array(t.string()).optional(),
            "yarnApplicationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiagnoseClusterRequestOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["JobMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["JobMetadataIn"]
    )
    types["JobMetadataOut"] = t.struct(
        {
            "jobId": t.string().optional(),
            "status": t.proxy(renames["JobStatusOut"]).optional(),
            "operationType": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobMetadataOut"])
    types["ListAutoscalingPoliciesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ListAutoscalingPoliciesResponseIn"])
    types["ListAutoscalingPoliciesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "policies": t.array(t.proxy(renames["AutoscalingPolicyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAutoscalingPoliciesResponseOut"])
    types["NodeInitializationActionIn"] = t.struct(
        {"executionTimeout": t.string().optional(), "executableFile": t.string()}
    ).named(renames["NodeInitializationActionIn"])
    types["NodeInitializationActionOut"] = t.struct(
        {
            "executionTimeout": t.string().optional(),
            "executableFile": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeInitializationActionOut"])
    types["QueryListIn"] = t.struct({"queries": t.array(t.string())}).named(
        renames["QueryListIn"]
    )
    types["QueryListOut"] = t.struct(
        {
            "queries": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryListOut"])
    types["KubernetesClusterConfigIn"] = t.struct(
        {
            "kubernetesSoftwareConfig": t.proxy(
                renames["KubernetesSoftwareConfigIn"]
            ).optional(),
            "gkeClusterConfig": t.proxy(renames["GkeClusterConfigIn"]),
            "kubernetesNamespace": t.string().optional(),
        }
    ).named(renames["KubernetesClusterConfigIn"])
    types["KubernetesClusterConfigOut"] = t.struct(
        {
            "kubernetesSoftwareConfig": t.proxy(
                renames["KubernetesSoftwareConfigOut"]
            ).optional(),
            "gkeClusterConfig": t.proxy(renames["GkeClusterConfigOut"]),
            "kubernetesNamespace": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesClusterConfigOut"])
    types["GkeNodeConfigIn"] = t.struct(
        {
            "localSsdCount": t.integer().optional(),
            "bootDiskKmsKey": t.string().optional(),
            "machineType": t.string().optional(),
            "preemptible": t.boolean().optional(),
            "minCpuPlatform": t.string().optional(),
            "accelerators": t.array(
                t.proxy(renames["GkeNodePoolAcceleratorConfigIn"])
            ).optional(),
            "spot": t.boolean().optional(),
        }
    ).named(renames["GkeNodeConfigIn"])
    types["GkeNodeConfigOut"] = t.struct(
        {
            "localSsdCount": t.integer().optional(),
            "bootDiskKmsKey": t.string().optional(),
            "machineType": t.string().optional(),
            "preemptible": t.boolean().optional(),
            "minCpuPlatform": t.string().optional(),
            "accelerators": t.array(
                t.proxy(renames["GkeNodePoolAcceleratorConfigOut"])
            ).optional(),
            "spot": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNodeConfigOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["RepairClusterRequestIn"] = t.struct(
        {
            "clusterUuid": t.string().optional(),
            "parentOperationId": t.string().optional(),
            "requestId": t.string().optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolIn"])).optional(),
            "gracefulDecommissionTimeout": t.string().optional(),
        }
    ).named(renames["RepairClusterRequestIn"])
    types["RepairClusterRequestOut"] = t.struct(
        {
            "clusterUuid": t.string().optional(),
            "parentOperationId": t.string().optional(),
            "requestId": t.string().optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolOut"])).optional(),
            "gracefulDecommissionTimeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepairClusterRequestOut"])
    types["WorkflowTemplateIn"] = t.struct(
        {
            "placement": t.proxy(renames["WorkflowTemplatePlacementIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "version": t.integer().optional(),
            "parameters": t.array(t.proxy(renames["TemplateParameterIn"])).optional(),
            "dagTimeout": t.string().optional(),
            "jobs": t.array(t.proxy(renames["OrderedJobIn"])),
            "id": t.string(),
        }
    ).named(renames["WorkflowTemplateIn"])
    types["WorkflowTemplateOut"] = t.struct(
        {
            "placement": t.proxy(renames["WorkflowTemplatePlacementOut"]),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "version": t.integer().optional(),
            "parameters": t.array(t.proxy(renames["TemplateParameterOut"])).optional(),
            "dagTimeout": t.string().optional(),
            "jobs": t.array(t.proxy(renames["OrderedJobOut"])),
            "id": t.string(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowTemplateOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["NamespacedGkeDeploymentTargetIn"] = t.struct(
        {
            "clusterNamespace": t.string().optional(),
            "targetGkeCluster": t.string().optional(),
        }
    ).named(renames["NamespacedGkeDeploymentTargetIn"])
    types["NamespacedGkeDeploymentTargetOut"] = t.struct(
        {
            "clusterNamespace": t.string().optional(),
            "targetGkeCluster": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamespacedGkeDeploymentTargetOut"])
    types["ListBatchesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "batches": t.array(t.proxy(renames["BatchIn"])).optional(),
        }
    ).named(renames["ListBatchesResponseIn"])
    types["ListBatchesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "batches": t.array(t.proxy(renames["BatchOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBatchesResponseOut"])
    types["StopClusterRequestIn"] = t.struct(
        {"requestId": t.string().optional(), "clusterUuid": t.string().optional()}
    ).named(renames["StopClusterRequestIn"])
    types["StopClusterRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "clusterUuid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StopClusterRequestOut"])
    types["GkeNodePoolAutoscalingConfigIn"] = t.struct(
        {"minNodeCount": t.integer().optional(), "maxNodeCount": t.integer().optional()}
    ).named(renames["GkeNodePoolAutoscalingConfigIn"])
    types["GkeNodePoolAutoscalingConfigOut"] = t.struct(
        {
            "minNodeCount": t.integer().optional(),
            "maxNodeCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNodePoolAutoscalingConfigOut"])
    types["GkeNodePoolTargetIn"] = t.struct(
        {
            "nodePool": t.string(),
            "roles": t.array(t.string()),
            "nodePoolConfig": t.proxy(renames["GkeNodePoolConfigIn"]).optional(),
        }
    ).named(renames["GkeNodePoolTargetIn"])
    types["GkeNodePoolTargetOut"] = t.struct(
        {
            "nodePool": t.string(),
            "roles": t.array(t.string()),
            "nodePoolConfig": t.proxy(renames["GkeNodePoolConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNodePoolTargetOut"])
    types["JobIn"] = t.struct(
        {
            "sparkRJob": t.proxy(renames["SparkRJobIn"]).optional(),
            "pigJob": t.proxy(renames["PigJobIn"]).optional(),
            "hiveJob": t.proxy(renames["HiveJobIn"]).optional(),
            "hadoopJob": t.proxy(renames["HadoopJobIn"]).optional(),
            "driverSchedulingConfig": t.proxy(
                renames["DriverSchedulingConfigIn"]
            ).optional(),
            "trinoJob": t.proxy(renames["TrinoJobIn"]).optional(),
            "placement": t.proxy(renames["JobPlacementIn"]),
            "pysparkJob": t.proxy(renames["PySparkJobIn"]).optional(),
            "reference": t.proxy(renames["JobReferenceIn"]).optional(),
            "scheduling": t.proxy(renames["JobSchedulingIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sparkJob": t.proxy(renames["SparkJobIn"]).optional(),
            "sparkSqlJob": t.proxy(renames["SparkSqlJobIn"]).optional(),
            "prestoJob": t.proxy(renames["PrestoJobIn"]).optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "sparkRJob": t.proxy(renames["SparkRJobOut"]).optional(),
            "pigJob": t.proxy(renames["PigJobOut"]).optional(),
            "hiveJob": t.proxy(renames["HiveJobOut"]).optional(),
            "jobUuid": t.string().optional(),
            "driverOutputResourceUri": t.string().optional(),
            "hadoopJob": t.proxy(renames["HadoopJobOut"]).optional(),
            "driverSchedulingConfig": t.proxy(
                renames["DriverSchedulingConfigOut"]
            ).optional(),
            "trinoJob": t.proxy(renames["TrinoJobOut"]).optional(),
            "placement": t.proxy(renames["JobPlacementOut"]),
            "pysparkJob": t.proxy(renames["PySparkJobOut"]).optional(),
            "reference": t.proxy(renames["JobReferenceOut"]).optional(),
            "statusHistory": t.array(t.proxy(renames["JobStatusOut"])).optional(),
            "status": t.proxy(renames["JobStatusOut"]).optional(),
            "scheduling": t.proxy(renames["JobSchedulingOut"]).optional(),
            "driverControlFilesUri": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "yarnApplications": t.array(
                t.proxy(renames["YarnApplicationOut"])
            ).optional(),
            "sparkJob": t.proxy(renames["SparkJobOut"]).optional(),
            "done": t.boolean().optional(),
            "sparkSqlJob": t.proxy(renames["SparkSqlJobOut"]).optional(),
            "prestoJob": t.proxy(renames["PrestoJobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["OrderedJobIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "hiveJob": t.proxy(renames["HiveJobIn"]).optional(),
            "scheduling": t.proxy(renames["JobSchedulingIn"]).optional(),
            "stepId": t.string(),
            "trinoJob": t.proxy(renames["TrinoJobIn"]).optional(),
            "pigJob": t.proxy(renames["PigJobIn"]).optional(),
            "sparkRJob": t.proxy(renames["SparkRJobIn"]).optional(),
            "sparkSqlJob": t.proxy(renames["SparkSqlJobIn"]).optional(),
            "hadoopJob": t.proxy(renames["HadoopJobIn"]).optional(),
            "prestoJob": t.proxy(renames["PrestoJobIn"]).optional(),
            "prerequisiteStepIds": t.array(t.string()).optional(),
            "pysparkJob": t.proxy(renames["PySparkJobIn"]).optional(),
            "sparkJob": t.proxy(renames["SparkJobIn"]).optional(),
        }
    ).named(renames["OrderedJobIn"])
    types["OrderedJobOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "hiveJob": t.proxy(renames["HiveJobOut"]).optional(),
            "scheduling": t.proxy(renames["JobSchedulingOut"]).optional(),
            "stepId": t.string(),
            "trinoJob": t.proxy(renames["TrinoJobOut"]).optional(),
            "pigJob": t.proxy(renames["PigJobOut"]).optional(),
            "sparkRJob": t.proxy(renames["SparkRJobOut"]).optional(),
            "sparkSqlJob": t.proxy(renames["SparkSqlJobOut"]).optional(),
            "hadoopJob": t.proxy(renames["HadoopJobOut"]).optional(),
            "prestoJob": t.proxy(renames["PrestoJobOut"]).optional(),
            "prerequisiteStepIds": t.array(t.string()).optional(),
            "pysparkJob": t.proxy(renames["PySparkJobOut"]).optional(),
            "sparkJob": t.proxy(renames["SparkJobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderedJobOut"])
    types["ListJobsResponseIn"] = t.struct(
        {"nextPageToken": t.string().optional()}
    ).named(renames["ListJobsResponseIn"])
    types["ListJobsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobsResponseOut"])
    types["CancelJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelJobRequestIn"]
    )
    types["CancelJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelJobRequestOut"])
    types["SecurityConfigIn"] = t.struct(
        {
            "identityConfig": t.proxy(renames["IdentityConfigIn"]).optional(),
            "kerberosConfig": t.proxy(renames["KerberosConfigIn"]).optional(),
        }
    ).named(renames["SecurityConfigIn"])
    types["SecurityConfigOut"] = t.struct(
        {
            "identityConfig": t.proxy(renames["IdentityConfigOut"]).optional(),
            "kerberosConfig": t.proxy(renames["KerberosConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecurityConfigOut"])
    types["RuntimeInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RuntimeInfoIn"]
    )
    types["RuntimeInfoOut"] = t.struct(
        {
            "outputUri": t.string().optional(),
            "currentUsage": t.proxy(renames["UsageSnapshotOut"]).optional(),
            "endpoints": t.struct({"_": t.string().optional()}).optional(),
            "diagnosticOutputUri": t.string().optional(),
            "approximateUsage": t.proxy(renames["UsageMetricsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeInfoOut"])
    types["PeripheralsConfigIn"] = t.struct(
        {
            "metastoreService": t.string().optional(),
            "sparkHistoryServerConfig": t.proxy(
                renames["SparkHistoryServerConfigIn"]
            ).optional(),
        }
    ).named(renames["PeripheralsConfigIn"])
    types["PeripheralsConfigOut"] = t.struct(
        {
            "metastoreService": t.string().optional(),
            "sparkHistoryServerConfig": t.proxy(
                renames["SparkHistoryServerConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PeripheralsConfigOut"])
    types["WorkflowMetadataIn"] = t.struct(
        {"parameters": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["WorkflowMetadataIn"])
    types["WorkflowMetadataOut"] = t.struct(
        {
            "deleteCluster": t.proxy(renames["ClusterOperationOut"]).optional(),
            "dagTimeout": t.string().optional(),
            "clusterUuid": t.string().optional(),
            "clusterName": t.string().optional(),
            "template": t.string().optional(),
            "graph": t.proxy(renames["WorkflowGraphOut"]).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "startTime": t.string().optional(),
            "version": t.integer().optional(),
            "dagStartTime": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "createCluster": t.proxy(renames["ClusterOperationOut"]).optional(),
            "dagEndTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowMetadataOut"])
    types["KerberosConfigIn"] = t.struct(
        {
            "truststorePasswordUri": t.string().optional(),
            "keyPasswordUri": t.string().optional(),
            "keystorePasswordUri": t.string().optional(),
            "kdcDbKeyUri": t.string().optional(),
            "crossRealmTrustSharedPasswordUri": t.string().optional(),
            "keystoreUri": t.string().optional(),
            "crossRealmTrustKdc": t.string().optional(),
            "enableKerberos": t.boolean().optional(),
            "truststoreUri": t.string().optional(),
            "realm": t.string().optional(),
            "tgtLifetimeHours": t.integer().optional(),
            "crossRealmTrustAdminServer": t.string().optional(),
            "kmsKeyUri": t.string().optional(),
            "crossRealmTrustRealm": t.string().optional(),
            "rootPrincipalPasswordUri": t.string().optional(),
        }
    ).named(renames["KerberosConfigIn"])
    types["KerberosConfigOut"] = t.struct(
        {
            "truststorePasswordUri": t.string().optional(),
            "keyPasswordUri": t.string().optional(),
            "keystorePasswordUri": t.string().optional(),
            "kdcDbKeyUri": t.string().optional(),
            "crossRealmTrustSharedPasswordUri": t.string().optional(),
            "keystoreUri": t.string().optional(),
            "crossRealmTrustKdc": t.string().optional(),
            "enableKerberos": t.boolean().optional(),
            "truststoreUri": t.string().optional(),
            "realm": t.string().optional(),
            "tgtLifetimeHours": t.integer().optional(),
            "crossRealmTrustAdminServer": t.string().optional(),
            "kmsKeyUri": t.string().optional(),
            "crossRealmTrustRealm": t.string().optional(),
            "rootPrincipalPasswordUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KerberosConfigOut"])
    types["VirtualClusterConfigIn"] = t.struct(
        {
            "kubernetesClusterConfig": t.proxy(renames["KubernetesClusterConfigIn"]),
            "auxiliaryServicesConfig": t.proxy(
                renames["AuxiliaryServicesConfigIn"]
            ).optional(),
            "stagingBucket": t.string().optional(),
        }
    ).named(renames["VirtualClusterConfigIn"])
    types["VirtualClusterConfigOut"] = t.struct(
        {
            "kubernetesClusterConfig": t.proxy(renames["KubernetesClusterConfigOut"]),
            "auxiliaryServicesConfig": t.proxy(
                renames["AuxiliaryServicesConfigOut"]
            ).optional(),
            "stagingBucket": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualClusterConfigOut"])
    types["InstanceReferenceIn"] = t.struct(
        {
            "instanceId": t.string().optional(),
            "instanceName": t.string().optional(),
            "publicKey": t.string().optional(),
            "publicEciesKey": t.string().optional(),
        }
    ).named(renames["InstanceReferenceIn"])
    types["InstanceReferenceOut"] = t.struct(
        {
            "instanceId": t.string().optional(),
            "instanceName": t.string().optional(),
            "publicKey": t.string().optional(),
            "publicEciesKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceReferenceOut"])
    types["BasicAutoscalingAlgorithmIn"] = t.struct(
        {
            "cooldownPeriod": t.string().optional(),
            "yarnConfig": t.proxy(renames["BasicYarnAutoscalingConfigIn"]).optional(),
            "sparkStandaloneConfig": t.proxy(
                renames["SparkStandaloneAutoscalingConfigIn"]
            ).optional(),
        }
    ).named(renames["BasicAutoscalingAlgorithmIn"])
    types["BasicAutoscalingAlgorithmOut"] = t.struct(
        {
            "cooldownPeriod": t.string().optional(),
            "yarnConfig": t.proxy(renames["BasicYarnAutoscalingConfigOut"]).optional(),
            "sparkStandaloneConfig": t.proxy(
                renames["SparkStandaloneAutoscalingConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicAutoscalingAlgorithmOut"])
    types["ParameterValidationIn"] = t.struct(
        {
            "regex": t.proxy(renames["RegexValidationIn"]).optional(),
            "values": t.proxy(renames["ValueValidationIn"]).optional(),
        }
    ).named(renames["ParameterValidationIn"])
    types["ParameterValidationOut"] = t.struct(
        {
            "regex": t.proxy(renames["RegexValidationOut"]).optional(),
            "values": t.proxy(renames["ValueValidationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParameterValidationOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["InstantiateWorkflowTemplateRequestIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "version": t.integer().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["InstantiateWorkflowTemplateRequestIn"])
    types["InstantiateWorkflowTemplateRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "version": t.integer().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstantiateWorkflowTemplateRequestOut"])
    types["EncryptionConfigIn"] = t.struct(
        {"gcePdKmsKeyName": t.string().optional(), "kmsKey": t.string().optional()}
    ).named(renames["EncryptionConfigIn"])
    types["EncryptionConfigOut"] = t.struct(
        {
            "gcePdKmsKeyName": t.string().optional(),
            "kmsKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
    types["ClusterConfigIn"] = t.struct(
        {
            "endpointConfig": t.proxy(renames["EndpointConfigIn"]).optional(),
            "securityConfig": t.proxy(renames["SecurityConfigIn"]).optional(),
            "dataprocMetricConfig": t.proxy(
                renames["DataprocMetricConfigIn"]
            ).optional(),
            "masterConfig": t.proxy(renames["InstanceGroupConfigIn"]).optional(),
            "auxiliaryNodeGroups": t.array(
                t.proxy(renames["AuxiliaryNodeGroupIn"])
            ).optional(),
            "gceClusterConfig": t.proxy(renames["GceClusterConfigIn"]).optional(),
            "initializationActions": t.array(
                t.proxy(renames["NodeInitializationActionIn"])
            ).optional(),
            "workerConfig": t.proxy(renames["InstanceGroupConfigIn"]).optional(),
            "autoscalingConfig": t.proxy(renames["AutoscalingConfigIn"]).optional(),
            "metastoreConfig": t.proxy(renames["MetastoreConfigIn"]).optional(),
            "gkeClusterConfig": t.proxy(renames["GkeClusterConfigIn"]).optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
            "lifecycleConfig": t.proxy(renames["LifecycleConfigIn"]).optional(),
            "secondaryWorkerConfig": t.proxy(
                renames["InstanceGroupConfigIn"]
            ).optional(),
            "configBucket": t.string().optional(),
            "softwareConfig": t.proxy(renames["SoftwareConfigIn"]).optional(),
            "tempBucket": t.string().optional(),
        }
    ).named(renames["ClusterConfigIn"])
    types["ClusterConfigOut"] = t.struct(
        {
            "endpointConfig": t.proxy(renames["EndpointConfigOut"]).optional(),
            "securityConfig": t.proxy(renames["SecurityConfigOut"]).optional(),
            "dataprocMetricConfig": t.proxy(
                renames["DataprocMetricConfigOut"]
            ).optional(),
            "masterConfig": t.proxy(renames["InstanceGroupConfigOut"]).optional(),
            "auxiliaryNodeGroups": t.array(
                t.proxy(renames["AuxiliaryNodeGroupOut"])
            ).optional(),
            "gceClusterConfig": t.proxy(renames["GceClusterConfigOut"]).optional(),
            "initializationActions": t.array(
                t.proxy(renames["NodeInitializationActionOut"])
            ).optional(),
            "workerConfig": t.proxy(renames["InstanceGroupConfigOut"]).optional(),
            "autoscalingConfig": t.proxy(renames["AutoscalingConfigOut"]).optional(),
            "metastoreConfig": t.proxy(renames["MetastoreConfigOut"]).optional(),
            "gkeClusterConfig": t.proxy(renames["GkeClusterConfigOut"]).optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "lifecycleConfig": t.proxy(renames["LifecycleConfigOut"]).optional(),
            "secondaryWorkerConfig": t.proxy(
                renames["InstanceGroupConfigOut"]
            ).optional(),
            "configBucket": t.string().optional(),
            "softwareConfig": t.proxy(renames["SoftwareConfigOut"]).optional(),
            "tempBucket": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterConfigOut"])
    types["AutoscalingConfigIn"] = t.struct({"policyUri": t.string().optional()}).named(
        renames["AutoscalingConfigIn"]
    )
    types["AutoscalingConfigOut"] = t.struct(
        {
            "policyUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoscalingConfigOut"])
    types["GceClusterConfigIn"] = t.struct(
        {
            "privateIpv6GoogleAccess": t.string().optional(),
            "subnetworkUri": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "nodeGroupAffinity": t.proxy(renames["NodeGroupAffinityIn"]).optional(),
            "serviceAccountScopes": t.array(t.string()).optional(),
            "zoneUri": t.string().optional(),
            "confidentialInstanceConfig": t.proxy(
                renames["ConfidentialInstanceConfigIn"]
            ).optional(),
            "reservationAffinity": t.proxy(renames["ReservationAffinityIn"]).optional(),
            "networkUri": t.string().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigIn"]
            ).optional(),
            "internalIpOnly": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "tags": t.array(t.string()).optional(),
        }
    ).named(renames["GceClusterConfigIn"])
    types["GceClusterConfigOut"] = t.struct(
        {
            "privateIpv6GoogleAccess": t.string().optional(),
            "subnetworkUri": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "nodeGroupAffinity": t.proxy(renames["NodeGroupAffinityOut"]).optional(),
            "serviceAccountScopes": t.array(t.string()).optional(),
            "zoneUri": t.string().optional(),
            "confidentialInstanceConfig": t.proxy(
                renames["ConfidentialInstanceConfigOut"]
            ).optional(),
            "reservationAffinity": t.proxy(
                renames["ReservationAffinityOut"]
            ).optional(),
            "networkUri": t.string().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigOut"]
            ).optional(),
            "internalIpOnly": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "tags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceClusterConfigOut"])
    types["ClusterOperationStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClusterOperationStatusIn"]
    )
    types["ClusterOperationStatusOut"] = t.struct(
        {
            "details": t.string().optional(),
            "innerState": t.string().optional(),
            "state": t.string().optional(),
            "stateStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOperationStatusOut"])
    types["ListClustersResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListClustersResponseIn"]
    )
    types["ListClustersResponseOut"] = t.struct(
        {
            "clusters": t.array(t.proxy(renames["ClusterOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListClustersResponseOut"])
    types["SparkBatchIn"] = t.struct(
        {
            "mainJarFileUri": t.string().optional(),
            "mainClass": t.string().optional(),
            "fileUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
        }
    ).named(renames["SparkBatchIn"])
    types["SparkBatchOut"] = t.struct(
        {
            "mainJarFileUri": t.string().optional(),
            "mainClass": t.string().optional(),
            "fileUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkBatchOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["PrestoJobIn"] = t.struct(
        {
            "clientTags": t.array(t.string()).optional(),
            "queryFileUri": t.string().optional(),
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
            "outputFormat": t.string().optional(),
            "continueOnFailure": t.boolean().optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PrestoJobIn"])
    types["PrestoJobOut"] = t.struct(
        {
            "clientTags": t.array(t.string()).optional(),
            "queryFileUri": t.string().optional(),
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "outputFormat": t.string().optional(),
            "continueOnFailure": t.boolean().optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrestoJobOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["WorkflowTemplatePlacementIn"] = t.struct(
        {
            "managedCluster": t.proxy(renames["ManagedClusterIn"]).optional(),
            "clusterSelector": t.proxy(renames["ClusterSelectorIn"]).optional(),
        }
    ).named(renames["WorkflowTemplatePlacementIn"])
    types["WorkflowTemplatePlacementOut"] = t.struct(
        {
            "managedCluster": t.proxy(renames["ManagedClusterOut"]).optional(),
            "clusterSelector": t.proxy(renames["ClusterSelectorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowTemplatePlacementOut"])
    types["ExecutionConfigIn"] = t.struct(
        {
            "stagingBucket": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "ttl": t.string().optional(),
            "idleTtl": t.string().optional(),
            "kmsKey": t.string().optional(),
            "networkUri": t.string().optional(),
            "subnetworkUri": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
        }
    ).named(renames["ExecutionConfigIn"])
    types["ExecutionConfigOut"] = t.struct(
        {
            "stagingBucket": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "ttl": t.string().optional(),
            "idleTtl": t.string().optional(),
            "kmsKey": t.string().optional(),
            "networkUri": t.string().optional(),
            "subnetworkUri": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["AuxiliaryServicesConfigIn"] = t.struct(
        {
            "metastoreConfig": t.proxy(renames["MetastoreConfigIn"]).optional(),
            "sparkHistoryServerConfig": t.proxy(
                renames["SparkHistoryServerConfigIn"]
            ).optional(),
        }
    ).named(renames["AuxiliaryServicesConfigIn"])
    types["AuxiliaryServicesConfigOut"] = t.struct(
        {
            "metastoreConfig": t.proxy(renames["MetastoreConfigOut"]).optional(),
            "sparkHistoryServerConfig": t.proxy(
                renames["SparkHistoryServerConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuxiliaryServicesConfigOut"])
    types["ClusterIn"] = t.struct(
        {
            "projectId": t.string(),
            "config": t.proxy(renames["ClusterConfigIn"]).optional(),
            "virtualClusterConfig": t.proxy(
                renames["VirtualClusterConfigIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "clusterName": t.string(),
        }
    ).named(renames["ClusterIn"])
    types["ClusterOut"] = t.struct(
        {
            "status": t.proxy(renames["ClusterStatusOut"]).optional(),
            "projectId": t.string(),
            "config": t.proxy(renames["ClusterConfigOut"]).optional(),
            "virtualClusterConfig": t.proxy(
                renames["VirtualClusterConfigOut"]
            ).optional(),
            "clusterUuid": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "clusterName": t.string(),
            "metrics": t.proxy(renames["ClusterMetricsOut"]).optional(),
            "statusHistory": t.array(t.proxy(renames["ClusterStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOut"])
    types["ValueValidationIn"] = t.struct({"values": t.array(t.string())}).named(
        renames["ValueValidationIn"]
    )
    types["ValueValidationOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueValidationOut"])
    types["JobSchedulingIn"] = t.struct(
        {
            "maxFailuresPerHour": t.integer().optional(),
            "maxFailuresTotal": t.integer().optional(),
        }
    ).named(renames["JobSchedulingIn"])
    types["JobSchedulingOut"] = t.struct(
        {
            "maxFailuresPerHour": t.integer().optional(),
            "maxFailuresTotal": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobSchedulingOut"])
    types["HadoopJobIn"] = t.struct(
        {
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
            "mainJarFileUri": t.string().optional(),
        }
    ).named(renames["HadoopJobIn"])
    types["HadoopJobOut"] = t.struct(
        {
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
            "mainJarFileUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HadoopJobOut"])
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
    types["InstanceGroupAutoscalingPolicyConfigIn"] = t.struct(
        {
            "maxInstances": t.integer(),
            "minInstances": t.integer().optional(),
            "weight": t.integer().optional(),
        }
    ).named(renames["InstanceGroupAutoscalingPolicyConfigIn"])
    types["InstanceGroupAutoscalingPolicyConfigOut"] = t.struct(
        {
            "maxInstances": t.integer(),
            "minInstances": t.integer().optional(),
            "weight": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceGroupAutoscalingPolicyConfigOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["StateHistoryIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StateHistoryIn"]
    )
    types["StateHistoryOut"] = t.struct(
        {
            "state": t.string().optional(),
            "stateMessage": t.string().optional(),
            "stateStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StateHistoryOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["PySparkBatchIn"] = t.struct(
        {
            "mainPythonFileUri": t.string(),
            "args": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "pythonFileUris": t.array(t.string()).optional(),
        }
    ).named(renames["PySparkBatchIn"])
    types["PySparkBatchOut"] = t.struct(
        {
            "mainPythonFileUri": t.string(),
            "args": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "pythonFileUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PySparkBatchOut"])
    types["GkeClusterConfigIn"] = t.struct(
        {
            "gkeClusterTarget": t.string().optional(),
            "namespacedGkeDeploymentTarget": t.proxy(
                renames["NamespacedGkeDeploymentTargetIn"]
            ).optional(),
            "nodePoolTarget": t.array(
                t.proxy(renames["GkeNodePoolTargetIn"])
            ).optional(),
        }
    ).named(renames["GkeClusterConfigIn"])
    types["GkeClusterConfigOut"] = t.struct(
        {
            "gkeClusterTarget": t.string().optional(),
            "namespacedGkeDeploymentTarget": t.proxy(
                renames["NamespacedGkeDeploymentTargetOut"]
            ).optional(),
            "nodePoolTarget": t.array(
                t.proxy(renames["GkeNodePoolTargetOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeClusterConfigOut"])
    types["WorkflowNodeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WorkflowNodeIn"]
    )
    types["WorkflowNodeOut"] = t.struct(
        {
            "jobId": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "stepId": t.string().optional(),
            "prerequisiteStepIds": t.array(t.string()).optional(),
        }
    ).named(renames["WorkflowNodeOut"])
    types["ClusterStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClusterStatusIn"]
    )
    types["ClusterStatusOut"] = t.struct(
        {
            "substate": t.string().optional(),
            "detail": t.string().optional(),
            "state": t.string().optional(),
            "stateStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterStatusOut"])
    types["IdentityConfigIn"] = t.struct(
        {"userServiceAccountMapping": t.struct({"_": t.string().optional()})}
    ).named(renames["IdentityConfigIn"])
    types["IdentityConfigOut"] = t.struct(
        {
            "userServiceAccountMapping": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityConfigOut"])
    types["StartClusterRequestIn"] = t.struct(
        {"requestId": t.string().optional(), "clusterUuid": t.string().optional()}
    ).named(renames["StartClusterRequestIn"])
    types["StartClusterRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "clusterUuid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartClusterRequestOut"])
    types["SparkJobIn"] = t.struct(
        {
            "jarFileUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "fileUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "mainClass": t.string().optional(),
            "mainJarFileUri": t.string().optional(),
            "archiveUris": t.array(t.string()).optional(),
        }
    ).named(renames["SparkJobIn"])
    types["SparkJobOut"] = t.struct(
        {
            "jarFileUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "fileUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "mainClass": t.string().optional(),
            "mainJarFileUri": t.string().optional(),
            "archiveUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkJobOut"])
    types["ClusterOperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClusterOperationMetadataIn"]
    )
    types["ClusterOperationMetadataOut"] = t.struct(
        {
            "operationType": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "status": t.proxy(renames["ClusterOperationStatusOut"]).optional(),
            "clusterName": t.string().optional(),
            "statusHistory": t.array(
                t.proxy(renames["ClusterOperationStatusOut"])
            ).optional(),
            "description": t.string().optional(),
            "clusterUuid": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "childOperationIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOperationMetadataOut"])
    types["IntervalIn"] = t.struct(
        {"startTime": t.string().optional(), "endTime": t.string().optional()}
    ).named(renames["IntervalIn"])
    types["IntervalOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntervalOut"])
    types["TrinoJobIn"] = t.struct(
        {
            "continueOnFailure": t.boolean().optional(),
            "clientTags": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "queryFileUri": t.string().optional(),
            "outputFormat": t.string().optional(),
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
        }
    ).named(renames["TrinoJobIn"])
    types["TrinoJobOut"] = t.struct(
        {
            "continueOnFailure": t.boolean().optional(),
            "clientTags": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "queryFileUri": t.string().optional(),
            "outputFormat": t.string().optional(),
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrinoJobOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DiskConfigIn"] = t.struct(
        {
            "bootDiskType": t.string().optional(),
            "numLocalSsds": t.integer().optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "localSsdInterface": t.string().optional(),
        }
    ).named(renames["DiskConfigIn"])
    types["DiskConfigOut"] = t.struct(
        {
            "bootDiskType": t.string().optional(),
            "numLocalSsds": t.integer().optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "localSsdInterface": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskConfigOut"])
    types["NodeGroupIn"] = t.struct(
        {
            "roles": t.array(t.string()),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "nodeGroupConfig": t.proxy(renames["InstanceGroupConfigIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["NodeGroupIn"])
    types["NodeGroupOut"] = t.struct(
        {
            "roles": t.array(t.string()),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "nodeGroupConfig": t.proxy(renames["InstanceGroupConfigOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeGroupOut"])
    types["PigJobIn"] = t.struct(
        {
            "jarFileUris": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
            "continueOnFailure": t.boolean().optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "queryFileUri": t.string().optional(),
        }
    ).named(renames["PigJobIn"])
    types["PigJobOut"] = t.struct(
        {
            "jarFileUris": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "continueOnFailure": t.boolean().optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "queryFileUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PigJobOut"])
    types["HiveJobIn"] = t.struct(
        {
            "jarFileUris": t.array(t.string()).optional(),
            "continueOnFailure": t.boolean().optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "queryFileUri": t.string().optional(),
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
        }
    ).named(renames["HiveJobIn"])
    types["HiveJobOut"] = t.struct(
        {
            "jarFileUris": t.array(t.string()).optional(),
            "continueOnFailure": t.boolean().optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "queryFileUri": t.string().optional(),
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HiveJobOut"])
    types["SparkHistoryServerConfigIn"] = t.struct(
        {"dataprocCluster": t.string().optional()}
    ).named(renames["SparkHistoryServerConfigIn"])
    types["SparkHistoryServerConfigOut"] = t.struct(
        {
            "dataprocCluster": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkHistoryServerConfigOut"])
    types["ClusterOperationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClusterOperationIn"]
    )
    types["ClusterOperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "operationId": t.string().optional(),
        }
    ).named(renames["ClusterOperationOut"])
    types["SubmitJobRequestIn"] = t.struct(
        {"requestId": t.string().optional(), "job": t.proxy(renames["JobIn"])}
    ).named(renames["SubmitJobRequestIn"])
    types["SubmitJobRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "job": t.proxy(renames["JobOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubmitJobRequestOut"])
    types["DriverSchedulingConfigIn"] = t.struct(
        {"memoryMb": t.integer(), "vcores": t.integer()}
    ).named(renames["DriverSchedulingConfigIn"])
    types["DriverSchedulingConfigOut"] = t.struct(
        {
            "memoryMb": t.integer(),
            "vcores": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriverSchedulingConfigOut"])
    types["SessionOperationMetadataIn"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "session": t.string().optional(),
            "operationType": t.string().optional(),
            "sessionUuid": t.string().optional(),
            "doneTime": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
        }
    ).named(renames["SessionOperationMetadataIn"])
    types["SessionOperationMetadataOut"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "session": t.string().optional(),
            "operationType": t.string().optional(),
            "sessionUuid": t.string().optional(),
            "doneTime": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionOperationMetadataOut"])
    types["AutoscalingPolicyIn"] = t.struct(
        {
            "basicAlgorithm": t.proxy(renames["BasicAutoscalingAlgorithmIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string(),
            "secondaryWorkerConfig": t.proxy(
                renames["InstanceGroupAutoscalingPolicyConfigIn"]
            ).optional(),
            "workerConfig": t.proxy(renames["InstanceGroupAutoscalingPolicyConfigIn"]),
        }
    ).named(renames["AutoscalingPolicyIn"])
    types["AutoscalingPolicyOut"] = t.struct(
        {
            "basicAlgorithm": t.proxy(renames["BasicAutoscalingAlgorithmOut"]),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string(),
            "secondaryWorkerConfig": t.proxy(
                renames["InstanceGroupAutoscalingPolicyConfigOut"]
            ).optional(),
            "workerConfig": t.proxy(renames["InstanceGroupAutoscalingPolicyConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoscalingPolicyOut"])
    types["UsageMetricsIn"] = t.struct(
        {
            "milliDcuSeconds": t.string().optional(),
            "shuffleStorageGbSeconds": t.string().optional(),
        }
    ).named(renames["UsageMetricsIn"])
    types["UsageMetricsOut"] = t.struct(
        {
            "milliDcuSeconds": t.string().optional(),
            "shuffleStorageGbSeconds": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageMetricsOut"])

    functions = {}
    functions["projectsRegionsOperationsDelete"] = dataproc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsCancel"] = dataproc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsList"] = dataproc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsGetIamPolicy"] = dataproc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsGet"] = dataproc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsSetIamPolicy"] = dataproc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsTestIamPermissions"] = dataproc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesGetIamPolicy"] = dataproc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesDelete"] = dataproc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesCreate"] = dataproc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesGet"] = dataproc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesUpdate"] = dataproc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesList"] = dataproc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesSetIamPolicy"] = dataproc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesTestIamPermissions"] = dataproc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesSetIamPolicy"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesTestIamPermissions"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesUpdate"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesGet"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesInstantiateInline"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesCreate"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesInstantiate"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesList"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesGetIamPolicy"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesDelete"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersGet"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:diagnose",
        t.struct(
            {
                "region": t.string(),
                "clusterName": t.string(),
                "projectId": t.string(),
                "yarnApplicationIds": t.array(t.string()).optional(),
                "job": t.string().optional(),
                "diagnosisInterval": t.proxy(renames["IntervalIn"]).optional(),
                "jobs": t.array(t.string()).optional(),
                "yarnApplicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersRepair"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:diagnose",
        t.struct(
            {
                "region": t.string(),
                "clusterName": t.string(),
                "projectId": t.string(),
                "yarnApplicationIds": t.array(t.string()).optional(),
                "job": t.string().optional(),
                "diagnosisInterval": t.proxy(renames["IntervalIn"]).optional(),
                "jobs": t.array(t.string()).optional(),
                "yarnApplicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersSetIamPolicy"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:diagnose",
        t.struct(
            {
                "region": t.string(),
                "clusterName": t.string(),
                "projectId": t.string(),
                "yarnApplicationIds": t.array(t.string()).optional(),
                "job": t.string().optional(),
                "diagnosisInterval": t.proxy(renames["IntervalIn"]).optional(),
                "jobs": t.array(t.string()).optional(),
                "yarnApplicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersTestIamPermissions"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:diagnose",
        t.struct(
            {
                "region": t.string(),
                "clusterName": t.string(),
                "projectId": t.string(),
                "yarnApplicationIds": t.array(t.string()).optional(),
                "job": t.string().optional(),
                "diagnosisInterval": t.proxy(renames["IntervalIn"]).optional(),
                "jobs": t.array(t.string()).optional(),
                "yarnApplicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersDelete"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:diagnose",
        t.struct(
            {
                "region": t.string(),
                "clusterName": t.string(),
                "projectId": t.string(),
                "yarnApplicationIds": t.array(t.string()).optional(),
                "job": t.string().optional(),
                "diagnosisInterval": t.proxy(renames["IntervalIn"]).optional(),
                "jobs": t.array(t.string()).optional(),
                "yarnApplicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersGetIamPolicy"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:diagnose",
        t.struct(
            {
                "region": t.string(),
                "clusterName": t.string(),
                "projectId": t.string(),
                "yarnApplicationIds": t.array(t.string()).optional(),
                "job": t.string().optional(),
                "diagnosisInterval": t.proxy(renames["IntervalIn"]).optional(),
                "jobs": t.array(t.string()).optional(),
                "yarnApplicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersCreate"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:diagnose",
        t.struct(
            {
                "region": t.string(),
                "clusterName": t.string(),
                "projectId": t.string(),
                "yarnApplicationIds": t.array(t.string()).optional(),
                "job": t.string().optional(),
                "diagnosisInterval": t.proxy(renames["IntervalIn"]).optional(),
                "jobs": t.array(t.string()).optional(),
                "yarnApplicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersList"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:diagnose",
        t.struct(
            {
                "region": t.string(),
                "clusterName": t.string(),
                "projectId": t.string(),
                "yarnApplicationIds": t.array(t.string()).optional(),
                "job": t.string().optional(),
                "diagnosisInterval": t.proxy(renames["IntervalIn"]).optional(),
                "jobs": t.array(t.string()).optional(),
                "yarnApplicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersStop"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:diagnose",
        t.struct(
            {
                "region": t.string(),
                "clusterName": t.string(),
                "projectId": t.string(),
                "yarnApplicationIds": t.array(t.string()).optional(),
                "job": t.string().optional(),
                "diagnosisInterval": t.proxy(renames["IntervalIn"]).optional(),
                "jobs": t.array(t.string()).optional(),
                "yarnApplicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersStart"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:diagnose",
        t.struct(
            {
                "region": t.string(),
                "clusterName": t.string(),
                "projectId": t.string(),
                "yarnApplicationIds": t.array(t.string()).optional(),
                "job": t.string().optional(),
                "diagnosisInterval": t.proxy(renames["IntervalIn"]).optional(),
                "jobs": t.array(t.string()).optional(),
                "yarnApplicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersInjectCredentials"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:diagnose",
        t.struct(
            {
                "region": t.string(),
                "clusterName": t.string(),
                "projectId": t.string(),
                "yarnApplicationIds": t.array(t.string()).optional(),
                "job": t.string().optional(),
                "diagnosisInterval": t.proxy(renames["IntervalIn"]).optional(),
                "jobs": t.array(t.string()).optional(),
                "yarnApplicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersPatch"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:diagnose",
        t.struct(
            {
                "region": t.string(),
                "clusterName": t.string(),
                "projectId": t.string(),
                "yarnApplicationIds": t.array(t.string()).optional(),
                "job": t.string().optional(),
                "diagnosisInterval": t.proxy(renames["IntervalIn"]).optional(),
                "jobs": t.array(t.string()).optional(),
                "yarnApplicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersDiagnose"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:diagnose",
        t.struct(
            {
                "region": t.string(),
                "clusterName": t.string(),
                "projectId": t.string(),
                "yarnApplicationIds": t.array(t.string()).optional(),
                "job": t.string().optional(),
                "diagnosisInterval": t.proxy(renames["IntervalIn"]).optional(),
                "jobs": t.array(t.string()).optional(),
                "yarnApplicationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersNodeGroupsGet"] = dataproc.post(
        "v1/{parent}/nodeGroups",
        t.struct(
            {
                "nodeGroupId": t.string().optional(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "roles": t.array(t.string()),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "nodeGroupConfig": t.proxy(renames["InstanceGroupConfigIn"]).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersNodeGroupsResize"] = dataproc.post(
        "v1/{parent}/nodeGroups",
        t.struct(
            {
                "nodeGroupId": t.string().optional(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "roles": t.array(t.string()),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "nodeGroupConfig": t.proxy(renames["InstanceGroupConfigIn"]).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersNodeGroupsCreate"] = dataproc.post(
        "v1/{parent}/nodeGroups",
        t.struct(
            {
                "nodeGroupId": t.string().optional(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "roles": t.array(t.string()),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "nodeGroupConfig": t.proxy(renames["InstanceGroupConfigIn"]).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsSetIamPolicy"] = dataproc.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsGet"] = dataproc.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsDelete"] = dataproc.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsCancel"] = dataproc.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsSubmit"] = dataproc.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsSubmitAsOperation"] = dataproc.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsTestIamPermissions"] = dataproc.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsList"] = dataproc.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsPatch"] = dataproc.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsGetIamPolicy"] = dataproc.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBatchesCreate"] = dataproc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BatchOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBatchesDelete"] = dataproc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BatchOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBatchesList"] = dataproc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BatchOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBatchesGet"] = dataproc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BatchOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesInstantiateInline"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesTestIamPermissions"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesCreate"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesGetIamPolicy"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesUpdate"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesList"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesSetIamPolicy"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesInstantiate"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesGet"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesDelete"] = dataproc.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "version": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAutoscalingPoliciesTestIamPermissions"] = dataproc.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAutoscalingPoliciesCreate"] = dataproc.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAutoscalingPoliciesUpdate"] = dataproc.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAutoscalingPoliciesDelete"] = dataproc.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAutoscalingPoliciesList"] = dataproc.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAutoscalingPoliciesSetIamPolicy"] = dataproc.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAutoscalingPoliciesGet"] = dataproc.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAutoscalingPoliciesGetIamPolicy"] = dataproc.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = dataproc.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = dataproc.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = dataproc.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = dataproc.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="dataproc", renames=renames, types=Box(types), functions=Box(functions)
    )
