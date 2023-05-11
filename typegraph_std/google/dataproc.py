from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_dataproc() -> Import:
    dataproc = HTTPRuntime("https://dataproc.googleapis.com/")

    renames = {
        "ErrorResponse": "_dataproc_1_ErrorResponse",
        "ClusterSelectorIn": "_dataproc_2_ClusterSelectorIn",
        "ClusterSelectorOut": "_dataproc_3_ClusterSelectorOut",
        "GkeNodePoolAcceleratorConfigIn": "_dataproc_4_GkeNodePoolAcceleratorConfigIn",
        "GkeNodePoolAcceleratorConfigOut": "_dataproc_5_GkeNodePoolAcceleratorConfigOut",
        "AuxiliaryNodeGroupIn": "_dataproc_6_AuxiliaryNodeGroupIn",
        "AuxiliaryNodeGroupOut": "_dataproc_7_AuxiliaryNodeGroupOut",
        "PySparkJobIn": "_dataproc_8_PySparkJobIn",
        "PySparkJobOut": "_dataproc_9_PySparkJobOut",
        "PolicyIn": "_dataproc_10_PolicyIn",
        "PolicyOut": "_dataproc_11_PolicyOut",
        "IntervalIn": "_dataproc_12_IntervalIn",
        "IntervalOut": "_dataproc_13_IntervalOut",
        "GetPolicyOptionsIn": "_dataproc_14_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_dataproc_15_GetPolicyOptionsOut",
        "RuntimeInfoIn": "_dataproc_16_RuntimeInfoIn",
        "RuntimeInfoOut": "_dataproc_17_RuntimeInfoOut",
        "ListWorkflowTemplatesResponseIn": "_dataproc_18_ListWorkflowTemplatesResponseIn",
        "ListWorkflowTemplatesResponseOut": "_dataproc_19_ListWorkflowTemplatesResponseOut",
        "ClusterConfigIn": "_dataproc_20_ClusterConfigIn",
        "ClusterConfigOut": "_dataproc_21_ClusterConfigOut",
        "GkeNodePoolAutoscalingConfigIn": "_dataproc_22_GkeNodePoolAutoscalingConfigIn",
        "GkeNodePoolAutoscalingConfigOut": "_dataproc_23_GkeNodePoolAutoscalingConfigOut",
        "PySparkBatchIn": "_dataproc_24_PySparkBatchIn",
        "PySparkBatchOut": "_dataproc_25_PySparkBatchOut",
        "ExprIn": "_dataproc_26_ExprIn",
        "ExprOut": "_dataproc_27_ExprOut",
        "InjectCredentialsRequestIn": "_dataproc_28_InjectCredentialsRequestIn",
        "InjectCredentialsRequestOut": "_dataproc_29_InjectCredentialsRequestOut",
        "ShieldedInstanceConfigIn": "_dataproc_30_ShieldedInstanceConfigIn",
        "ShieldedInstanceConfigOut": "_dataproc_31_ShieldedInstanceConfigOut",
        "RepairClusterRequestIn": "_dataproc_32_RepairClusterRequestIn",
        "RepairClusterRequestOut": "_dataproc_33_RepairClusterRequestOut",
        "ListClustersResponseIn": "_dataproc_34_ListClustersResponseIn",
        "ListClustersResponseOut": "_dataproc_35_ListClustersResponseOut",
        "DataprocMetricConfigIn": "_dataproc_36_DataprocMetricConfigIn",
        "DataprocMetricConfigOut": "_dataproc_37_DataprocMetricConfigOut",
        "GkeNodePoolConfigIn": "_dataproc_38_GkeNodePoolConfigIn",
        "GkeNodePoolConfigOut": "_dataproc_39_GkeNodePoolConfigOut",
        "WorkflowGraphIn": "_dataproc_40_WorkflowGraphIn",
        "WorkflowGraphOut": "_dataproc_41_WorkflowGraphOut",
        "WorkflowMetadataIn": "_dataproc_42_WorkflowMetadataIn",
        "WorkflowMetadataOut": "_dataproc_43_WorkflowMetadataOut",
        "ClusterOperationStatusIn": "_dataproc_44_ClusterOperationStatusIn",
        "ClusterOperationStatusOut": "_dataproc_45_ClusterOperationStatusOut",
        "ListOperationsResponseIn": "_dataproc_46_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_dataproc_47_ListOperationsResponseOut",
        "JobMetadataIn": "_dataproc_48_JobMetadataIn",
        "JobMetadataOut": "_dataproc_49_JobMetadataOut",
        "YarnApplicationIn": "_dataproc_50_YarnApplicationIn",
        "YarnApplicationOut": "_dataproc_51_YarnApplicationOut",
        "WorkflowNodeIn": "_dataproc_52_WorkflowNodeIn",
        "WorkflowNodeOut": "_dataproc_53_WorkflowNodeOut",
        "TestIamPermissionsResponseIn": "_dataproc_54_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_dataproc_55_TestIamPermissionsResponseOut",
        "SparkHistoryServerConfigIn": "_dataproc_56_SparkHistoryServerConfigIn",
        "SparkHistoryServerConfigOut": "_dataproc_57_SparkHistoryServerConfigOut",
        "KubernetesSoftwareConfigIn": "_dataproc_58_KubernetesSoftwareConfigIn",
        "KubernetesSoftwareConfigOut": "_dataproc_59_KubernetesSoftwareConfigOut",
        "InstanceGroupConfigIn": "_dataproc_60_InstanceGroupConfigIn",
        "InstanceGroupConfigOut": "_dataproc_61_InstanceGroupConfigOut",
        "RegexValidationIn": "_dataproc_62_RegexValidationIn",
        "RegexValidationOut": "_dataproc_63_RegexValidationOut",
        "SecurityConfigIn": "_dataproc_64_SecurityConfigIn",
        "SecurityConfigOut": "_dataproc_65_SecurityConfigOut",
        "SparkRJobIn": "_dataproc_66_SparkRJobIn",
        "SparkRJobOut": "_dataproc_67_SparkRJobOut",
        "ResizeNodeGroupRequestIn": "_dataproc_68_ResizeNodeGroupRequestIn",
        "ResizeNodeGroupRequestOut": "_dataproc_69_ResizeNodeGroupRequestOut",
        "AcceleratorConfigIn": "_dataproc_70_AcceleratorConfigIn",
        "AcceleratorConfigOut": "_dataproc_71_AcceleratorConfigOut",
        "SparkRBatchIn": "_dataproc_72_SparkRBatchIn",
        "SparkRBatchOut": "_dataproc_73_SparkRBatchOut",
        "AuxiliaryServicesConfigIn": "_dataproc_74_AuxiliaryServicesConfigIn",
        "AuxiliaryServicesConfigOut": "_dataproc_75_AuxiliaryServicesConfigOut",
        "ClusterIn": "_dataproc_76_ClusterIn",
        "ClusterOut": "_dataproc_77_ClusterOut",
        "KerberosConfigIn": "_dataproc_78_KerberosConfigIn",
        "KerberosConfigOut": "_dataproc_79_KerberosConfigOut",
        "NodeGroupIn": "_dataproc_80_NodeGroupIn",
        "NodeGroupOut": "_dataproc_81_NodeGroupOut",
        "SessionOperationMetadataIn": "_dataproc_82_SessionOperationMetadataIn",
        "SessionOperationMetadataOut": "_dataproc_83_SessionOperationMetadataOut",
        "WorkflowTemplatePlacementIn": "_dataproc_84_WorkflowTemplatePlacementIn",
        "WorkflowTemplatePlacementOut": "_dataproc_85_WorkflowTemplatePlacementOut",
        "UsageSnapshotIn": "_dataproc_86_UsageSnapshotIn",
        "UsageSnapshotOut": "_dataproc_87_UsageSnapshotOut",
        "JobIn": "_dataproc_88_JobIn",
        "JobOut": "_dataproc_89_JobOut",
        "ReservationAffinityIn": "_dataproc_90_ReservationAffinityIn",
        "ReservationAffinityOut": "_dataproc_91_ReservationAffinityOut",
        "ParameterValidationIn": "_dataproc_92_ParameterValidationIn",
        "ParameterValidationOut": "_dataproc_93_ParameterValidationOut",
        "SparkBatchIn": "_dataproc_94_SparkBatchIn",
        "SparkBatchOut": "_dataproc_95_SparkBatchOut",
        "ManagedClusterIn": "_dataproc_96_ManagedClusterIn",
        "ManagedClusterOut": "_dataproc_97_ManagedClusterOut",
        "RuntimeConfigIn": "_dataproc_98_RuntimeConfigIn",
        "RuntimeConfigOut": "_dataproc_99_RuntimeConfigOut",
        "AutoscalingConfigIn": "_dataproc_100_AutoscalingConfigIn",
        "AutoscalingConfigOut": "_dataproc_101_AutoscalingConfigOut",
        "BasicAutoscalingAlgorithmIn": "_dataproc_102_BasicAutoscalingAlgorithmIn",
        "BasicAutoscalingAlgorithmOut": "_dataproc_103_BasicAutoscalingAlgorithmOut",
        "StartClusterRequestIn": "_dataproc_104_StartClusterRequestIn",
        "StartClusterRequestOut": "_dataproc_105_StartClusterRequestOut",
        "StateHistoryIn": "_dataproc_106_StateHistoryIn",
        "StateHistoryOut": "_dataproc_107_StateHistoryOut",
        "PeripheralsConfigIn": "_dataproc_108_PeripheralsConfigIn",
        "PeripheralsConfigOut": "_dataproc_109_PeripheralsConfigOut",
        "MetastoreConfigIn": "_dataproc_110_MetastoreConfigIn",
        "MetastoreConfigOut": "_dataproc_111_MetastoreConfigOut",
        "PigJobIn": "_dataproc_112_PigJobIn",
        "PigJobOut": "_dataproc_113_PigJobOut",
        "NodeGroupAffinityIn": "_dataproc_114_NodeGroupAffinityIn",
        "NodeGroupAffinityOut": "_dataproc_115_NodeGroupAffinityOut",
        "SparkStandaloneAutoscalingConfigIn": "_dataproc_116_SparkStandaloneAutoscalingConfigIn",
        "SparkStandaloneAutoscalingConfigOut": "_dataproc_117_SparkStandaloneAutoscalingConfigOut",
        "CancelJobRequestIn": "_dataproc_118_CancelJobRequestIn",
        "CancelJobRequestOut": "_dataproc_119_CancelJobRequestOut",
        "ExecutionConfigIn": "_dataproc_120_ExecutionConfigIn",
        "ExecutionConfigOut": "_dataproc_121_ExecutionConfigOut",
        "SoftwareConfigIn": "_dataproc_122_SoftwareConfigIn",
        "SoftwareConfigOut": "_dataproc_123_SoftwareConfigOut",
        "ClusterOperationIn": "_dataproc_124_ClusterOperationIn",
        "ClusterOperationOut": "_dataproc_125_ClusterOperationOut",
        "JobPlacementIn": "_dataproc_126_JobPlacementIn",
        "JobPlacementOut": "_dataproc_127_JobPlacementOut",
        "JobSchedulingIn": "_dataproc_128_JobSchedulingIn",
        "JobSchedulingOut": "_dataproc_129_JobSchedulingOut",
        "IdentityConfigIn": "_dataproc_130_IdentityConfigIn",
        "IdentityConfigOut": "_dataproc_131_IdentityConfigOut",
        "GkeClusterConfigIn": "_dataproc_132_GkeClusterConfigIn",
        "GkeClusterConfigOut": "_dataproc_133_GkeClusterConfigOut",
        "LoggingConfigIn": "_dataproc_134_LoggingConfigIn",
        "LoggingConfigOut": "_dataproc_135_LoggingConfigOut",
        "GceClusterConfigIn": "_dataproc_136_GceClusterConfigIn",
        "GceClusterConfigOut": "_dataproc_137_GceClusterConfigOut",
        "PrestoJobIn": "_dataproc_138_PrestoJobIn",
        "PrestoJobOut": "_dataproc_139_PrestoJobOut",
        "QueryListIn": "_dataproc_140_QueryListIn",
        "QueryListOut": "_dataproc_141_QueryListOut",
        "SparkJobIn": "_dataproc_142_SparkJobIn",
        "SparkJobOut": "_dataproc_143_SparkJobOut",
        "NodePoolIn": "_dataproc_144_NodePoolIn",
        "NodePoolOut": "_dataproc_145_NodePoolOut",
        "InstantiateWorkflowTemplateRequestIn": "_dataproc_146_InstantiateWorkflowTemplateRequestIn",
        "InstantiateWorkflowTemplateRequestOut": "_dataproc_147_InstantiateWorkflowTemplateRequestOut",
        "BatchOperationMetadataIn": "_dataproc_148_BatchOperationMetadataIn",
        "BatchOperationMetadataOut": "_dataproc_149_BatchOperationMetadataOut",
        "GkeNodeConfigIn": "_dataproc_150_GkeNodeConfigIn",
        "GkeNodeConfigOut": "_dataproc_151_GkeNodeConfigOut",
        "SetIamPolicyRequestIn": "_dataproc_152_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_dataproc_153_SetIamPolicyRequestOut",
        "KubernetesClusterConfigIn": "_dataproc_154_KubernetesClusterConfigIn",
        "KubernetesClusterConfigOut": "_dataproc_155_KubernetesClusterConfigOut",
        "EnvironmentConfigIn": "_dataproc_156_EnvironmentConfigIn",
        "EnvironmentConfigOut": "_dataproc_157_EnvironmentConfigOut",
        "ClusterMetricsIn": "_dataproc_158_ClusterMetricsIn",
        "ClusterMetricsOut": "_dataproc_159_ClusterMetricsOut",
        "StopClusterRequestIn": "_dataproc_160_StopClusterRequestIn",
        "StopClusterRequestOut": "_dataproc_161_StopClusterRequestOut",
        "VirtualClusterConfigIn": "_dataproc_162_VirtualClusterConfigIn",
        "VirtualClusterConfigOut": "_dataproc_163_VirtualClusterConfigOut",
        "DiagnoseClusterRequestIn": "_dataproc_164_DiagnoseClusterRequestIn",
        "DiagnoseClusterRequestOut": "_dataproc_165_DiagnoseClusterRequestOut",
        "JobStatusIn": "_dataproc_166_JobStatusIn",
        "JobStatusOut": "_dataproc_167_JobStatusOut",
        "ClusterStatusIn": "_dataproc_168_ClusterStatusIn",
        "ClusterStatusOut": "_dataproc_169_ClusterStatusOut",
        "BindingIn": "_dataproc_170_BindingIn",
        "BindingOut": "_dataproc_171_BindingOut",
        "ListBatchesResponseIn": "_dataproc_172_ListBatchesResponseIn",
        "ListBatchesResponseOut": "_dataproc_173_ListBatchesResponseOut",
        "EndpointConfigIn": "_dataproc_174_EndpointConfigIn",
        "EndpointConfigOut": "_dataproc_175_EndpointConfigOut",
        "TemplateParameterIn": "_dataproc_176_TemplateParameterIn",
        "TemplateParameterOut": "_dataproc_177_TemplateParameterOut",
        "InstanceGroupAutoscalingPolicyConfigIn": "_dataproc_178_InstanceGroupAutoscalingPolicyConfigIn",
        "InstanceGroupAutoscalingPolicyConfigOut": "_dataproc_179_InstanceGroupAutoscalingPolicyConfigOut",
        "NodeInitializationActionIn": "_dataproc_180_NodeInitializationActionIn",
        "NodeInitializationActionOut": "_dataproc_181_NodeInitializationActionOut",
        "DriverSchedulingConfigIn": "_dataproc_182_DriverSchedulingConfigIn",
        "DriverSchedulingConfigOut": "_dataproc_183_DriverSchedulingConfigOut",
        "DiskConfigIn": "_dataproc_184_DiskConfigIn",
        "DiskConfigOut": "_dataproc_185_DiskConfigOut",
        "DiagnoseClusterResultsIn": "_dataproc_186_DiagnoseClusterResultsIn",
        "DiagnoseClusterResultsOut": "_dataproc_187_DiagnoseClusterResultsOut",
        "ListAutoscalingPoliciesResponseIn": "_dataproc_188_ListAutoscalingPoliciesResponseIn",
        "ListAutoscalingPoliciesResponseOut": "_dataproc_189_ListAutoscalingPoliciesResponseOut",
        "GkeNodePoolTargetIn": "_dataproc_190_GkeNodePoolTargetIn",
        "GkeNodePoolTargetOut": "_dataproc_191_GkeNodePoolTargetOut",
        "HiveJobIn": "_dataproc_192_HiveJobIn",
        "HiveJobOut": "_dataproc_193_HiveJobOut",
        "JobReferenceIn": "_dataproc_194_JobReferenceIn",
        "JobReferenceOut": "_dataproc_195_JobReferenceOut",
        "EmptyIn": "_dataproc_196_EmptyIn",
        "EmptyOut": "_dataproc_197_EmptyOut",
        "BasicYarnAutoscalingConfigIn": "_dataproc_198_BasicYarnAutoscalingConfigIn",
        "BasicYarnAutoscalingConfigOut": "_dataproc_199_BasicYarnAutoscalingConfigOut",
        "HadoopJobIn": "_dataproc_200_HadoopJobIn",
        "HadoopJobOut": "_dataproc_201_HadoopJobOut",
        "BatchIn": "_dataproc_202_BatchIn",
        "BatchOut": "_dataproc_203_BatchOut",
        "ListJobsResponseIn": "_dataproc_204_ListJobsResponseIn",
        "ListJobsResponseOut": "_dataproc_205_ListJobsResponseOut",
        "UsageMetricsIn": "_dataproc_206_UsageMetricsIn",
        "UsageMetricsOut": "_dataproc_207_UsageMetricsOut",
        "TestIamPermissionsRequestIn": "_dataproc_208_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_dataproc_209_TestIamPermissionsRequestOut",
        "OrderedJobIn": "_dataproc_210_OrderedJobIn",
        "OrderedJobOut": "_dataproc_211_OrderedJobOut",
        "ConfidentialInstanceConfigIn": "_dataproc_212_ConfidentialInstanceConfigIn",
        "ConfidentialInstanceConfigOut": "_dataproc_213_ConfidentialInstanceConfigOut",
        "EncryptionConfigIn": "_dataproc_214_EncryptionConfigIn",
        "EncryptionConfigOut": "_dataproc_215_EncryptionConfigOut",
        "SparkSqlBatchIn": "_dataproc_216_SparkSqlBatchIn",
        "SparkSqlBatchOut": "_dataproc_217_SparkSqlBatchOut",
        "GetIamPolicyRequestIn": "_dataproc_218_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_dataproc_219_GetIamPolicyRequestOut",
        "NamespacedGkeDeploymentTargetIn": "_dataproc_220_NamespacedGkeDeploymentTargetIn",
        "NamespacedGkeDeploymentTargetOut": "_dataproc_221_NamespacedGkeDeploymentTargetOut",
        "AutoscalingPolicyIn": "_dataproc_222_AutoscalingPolicyIn",
        "AutoscalingPolicyOut": "_dataproc_223_AutoscalingPolicyOut",
        "StatusIn": "_dataproc_224_StatusIn",
        "StatusOut": "_dataproc_225_StatusOut",
        "NodeGroupOperationMetadataIn": "_dataproc_226_NodeGroupOperationMetadataIn",
        "NodeGroupOperationMetadataOut": "_dataproc_227_NodeGroupOperationMetadataOut",
        "InstanceReferenceIn": "_dataproc_228_InstanceReferenceIn",
        "InstanceReferenceOut": "_dataproc_229_InstanceReferenceOut",
        "OperationIn": "_dataproc_230_OperationIn",
        "OperationOut": "_dataproc_231_OperationOut",
        "SubmitJobRequestIn": "_dataproc_232_SubmitJobRequestIn",
        "SubmitJobRequestOut": "_dataproc_233_SubmitJobRequestOut",
        "LifecycleConfigIn": "_dataproc_234_LifecycleConfigIn",
        "LifecycleConfigOut": "_dataproc_235_LifecycleConfigOut",
        "ValueValidationIn": "_dataproc_236_ValueValidationIn",
        "ValueValidationOut": "_dataproc_237_ValueValidationOut",
        "ManagedGroupConfigIn": "_dataproc_238_ManagedGroupConfigIn",
        "ManagedGroupConfigOut": "_dataproc_239_ManagedGroupConfigOut",
        "SparkSqlJobIn": "_dataproc_240_SparkSqlJobIn",
        "SparkSqlJobOut": "_dataproc_241_SparkSqlJobOut",
        "ClusterOperationMetadataIn": "_dataproc_242_ClusterOperationMetadataIn",
        "ClusterOperationMetadataOut": "_dataproc_243_ClusterOperationMetadataOut",
        "MetricIn": "_dataproc_244_MetricIn",
        "MetricOut": "_dataproc_245_MetricOut",
        "WorkflowTemplateIn": "_dataproc_246_WorkflowTemplateIn",
        "WorkflowTemplateOut": "_dataproc_247_WorkflowTemplateOut",
        "TrinoJobIn": "_dataproc_248_TrinoJobIn",
        "TrinoJobOut": "_dataproc_249_TrinoJobOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ClusterSelectorIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "clusterLabels": t.struct({"_": t.string().optional()}),
        }
    ).named(renames["ClusterSelectorIn"])
    types["ClusterSelectorOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "clusterLabels": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterSelectorOut"])
    types["GkeNodePoolAcceleratorConfigIn"] = t.struct(
        {
            "acceleratorCount": t.string().optional(),
            "acceleratorType": t.string().optional(),
            "gpuPartitionSize": t.string().optional(),
        }
    ).named(renames["GkeNodePoolAcceleratorConfigIn"])
    types["GkeNodePoolAcceleratorConfigOut"] = t.struct(
        {
            "acceleratorCount": t.string().optional(),
            "acceleratorType": t.string().optional(),
            "gpuPartitionSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNodePoolAcceleratorConfigOut"])
    types["AuxiliaryNodeGroupIn"] = t.struct(
        {
            "nodeGroupId": t.string().optional(),
            "nodeGroup": t.proxy(renames["NodeGroupIn"]),
        }
    ).named(renames["AuxiliaryNodeGroupIn"])
    types["AuxiliaryNodeGroupOut"] = t.struct(
        {
            "nodeGroupId": t.string().optional(),
            "nodeGroup": t.proxy(renames["NodeGroupOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuxiliaryNodeGroupOut"])
    types["PySparkJobIn"] = t.struct(
        {
            "pythonFileUris": t.array(t.string()).optional(),
            "mainPythonFileUri": t.string(),
            "fileUris": t.array(t.string()).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PySparkJobIn"])
    types["PySparkJobOut"] = t.struct(
        {
            "pythonFileUris": t.array(t.string()).optional(),
            "mainPythonFileUri": t.string(),
            "fileUris": t.array(t.string()).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PySparkJobOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["RuntimeInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RuntimeInfoIn"]
    )
    types["RuntimeInfoOut"] = t.struct(
        {
            "outputUri": t.string().optional(),
            "approximateUsage": t.proxy(renames["UsageMetricsOut"]).optional(),
            "diagnosticOutputUri": t.string().optional(),
            "endpoints": t.struct({"_": t.string().optional()}).optional(),
            "currentUsage": t.proxy(renames["UsageSnapshotOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeInfoOut"])
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
    types["ClusterConfigIn"] = t.struct(
        {
            "workerConfig": t.proxy(renames["InstanceGroupConfigIn"]).optional(),
            "auxiliaryNodeGroups": t.array(
                t.proxy(renames["AuxiliaryNodeGroupIn"])
            ).optional(),
            "configBucket": t.string().optional(),
            "tempBucket": t.string().optional(),
            "initializationActions": t.array(
                t.proxy(renames["NodeInitializationActionIn"])
            ).optional(),
            "endpointConfig": t.proxy(renames["EndpointConfigIn"]).optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
            "securityConfig": t.proxy(renames["SecurityConfigIn"]).optional(),
            "metastoreConfig": t.proxy(renames["MetastoreConfigIn"]).optional(),
            "autoscalingConfig": t.proxy(renames["AutoscalingConfigIn"]).optional(),
            "masterConfig": t.proxy(renames["InstanceGroupConfigIn"]).optional(),
            "softwareConfig": t.proxy(renames["SoftwareConfigIn"]).optional(),
            "lifecycleConfig": t.proxy(renames["LifecycleConfigIn"]).optional(),
            "gceClusterConfig": t.proxy(renames["GceClusterConfigIn"]).optional(),
            "dataprocMetricConfig": t.proxy(
                renames["DataprocMetricConfigIn"]
            ).optional(),
            "secondaryWorkerConfig": t.proxy(
                renames["InstanceGroupConfigIn"]
            ).optional(),
            "gkeClusterConfig": t.proxy(renames["GkeClusterConfigIn"]).optional(),
        }
    ).named(renames["ClusterConfigIn"])
    types["ClusterConfigOut"] = t.struct(
        {
            "workerConfig": t.proxy(renames["InstanceGroupConfigOut"]).optional(),
            "auxiliaryNodeGroups": t.array(
                t.proxy(renames["AuxiliaryNodeGroupOut"])
            ).optional(),
            "configBucket": t.string().optional(),
            "tempBucket": t.string().optional(),
            "initializationActions": t.array(
                t.proxy(renames["NodeInitializationActionOut"])
            ).optional(),
            "endpointConfig": t.proxy(renames["EndpointConfigOut"]).optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "securityConfig": t.proxy(renames["SecurityConfigOut"]).optional(),
            "metastoreConfig": t.proxy(renames["MetastoreConfigOut"]).optional(),
            "autoscalingConfig": t.proxy(renames["AutoscalingConfigOut"]).optional(),
            "masterConfig": t.proxy(renames["InstanceGroupConfigOut"]).optional(),
            "softwareConfig": t.proxy(renames["SoftwareConfigOut"]).optional(),
            "lifecycleConfig": t.proxy(renames["LifecycleConfigOut"]).optional(),
            "gceClusterConfig": t.proxy(renames["GceClusterConfigOut"]).optional(),
            "dataprocMetricConfig": t.proxy(
                renames["DataprocMetricConfigOut"]
            ).optional(),
            "secondaryWorkerConfig": t.proxy(
                renames["InstanceGroupConfigOut"]
            ).optional(),
            "gkeClusterConfig": t.proxy(renames["GkeClusterConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterConfigOut"])
    types["GkeNodePoolAutoscalingConfigIn"] = t.struct(
        {"maxNodeCount": t.integer().optional(), "minNodeCount": t.integer().optional()}
    ).named(renames["GkeNodePoolAutoscalingConfigIn"])
    types["GkeNodePoolAutoscalingConfigOut"] = t.struct(
        {
            "maxNodeCount": t.integer().optional(),
            "minNodeCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNodePoolAutoscalingConfigOut"])
    types["PySparkBatchIn"] = t.struct(
        {
            "args": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "pythonFileUris": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "mainPythonFileUri": t.string(),
            "jarFileUris": t.array(t.string()).optional(),
        }
    ).named(renames["PySparkBatchIn"])
    types["PySparkBatchOut"] = t.struct(
        {
            "args": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "pythonFileUris": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "mainPythonFileUri": t.string(),
            "jarFileUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PySparkBatchOut"])
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
    types["InjectCredentialsRequestIn"] = t.struct(
        {"credentialsCiphertext": t.string(), "clusterUuid": t.string()}
    ).named(renames["InjectCredentialsRequestIn"])
    types["InjectCredentialsRequestOut"] = t.struct(
        {
            "credentialsCiphertext": t.string(),
            "clusterUuid": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InjectCredentialsRequestOut"])
    types["ShieldedInstanceConfigIn"] = t.struct(
        {
            "enableSecureBoot": t.boolean().optional(),
            "enableVtpm": t.boolean().optional(),
            "enableIntegrityMonitoring": t.boolean().optional(),
        }
    ).named(renames["ShieldedInstanceConfigIn"])
    types["ShieldedInstanceConfigOut"] = t.struct(
        {
            "enableSecureBoot": t.boolean().optional(),
            "enableVtpm": t.boolean().optional(),
            "enableIntegrityMonitoring": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShieldedInstanceConfigOut"])
    types["RepairClusterRequestIn"] = t.struct(
        {
            "nodePools": t.array(t.proxy(renames["NodePoolIn"])).optional(),
            "requestId": t.string().optional(),
            "clusterUuid": t.string().optional(),
            "parentOperationId": t.string().optional(),
            "gracefulDecommissionTimeout": t.string().optional(),
        }
    ).named(renames["RepairClusterRequestIn"])
    types["RepairClusterRequestOut"] = t.struct(
        {
            "nodePools": t.array(t.proxy(renames["NodePoolOut"])).optional(),
            "requestId": t.string().optional(),
            "clusterUuid": t.string().optional(),
            "parentOperationId": t.string().optional(),
            "gracefulDecommissionTimeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepairClusterRequestOut"])
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
    types["DataprocMetricConfigIn"] = t.struct(
        {"metrics": t.array(t.proxy(renames["MetricIn"]))}
    ).named(renames["DataprocMetricConfigIn"])
    types["DataprocMetricConfigOut"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataprocMetricConfigOut"])
    types["GkeNodePoolConfigIn"] = t.struct(
        {
            "config": t.proxy(renames["GkeNodeConfigIn"]).optional(),
            "locations": t.array(t.string()).optional(),
            "autoscaling": t.proxy(
                renames["GkeNodePoolAutoscalingConfigIn"]
            ).optional(),
        }
    ).named(renames["GkeNodePoolConfigIn"])
    types["GkeNodePoolConfigOut"] = t.struct(
        {
            "config": t.proxy(renames["GkeNodeConfigOut"]).optional(),
            "locations": t.array(t.string()).optional(),
            "autoscaling": t.proxy(
                renames["GkeNodePoolAutoscalingConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNodePoolConfigOut"])
    types["WorkflowGraphIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WorkflowGraphIn"]
    )
    types["WorkflowGraphOut"] = t.struct(
        {
            "nodes": t.array(t.proxy(renames["WorkflowNodeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowGraphOut"])
    types["WorkflowMetadataIn"] = t.struct(
        {"parameters": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["WorkflowMetadataIn"])
    types["WorkflowMetadataOut"] = t.struct(
        {
            "dagStartTime": t.string().optional(),
            "template": t.string().optional(),
            "dagTimeout": t.string().optional(),
            "graph": t.proxy(renames["WorkflowGraphOut"]).optional(),
            "state": t.string().optional(),
            "deleteCluster": t.proxy(renames["ClusterOperationOut"]).optional(),
            "clusterName": t.string().optional(),
            "createCluster": t.proxy(renames["ClusterOperationOut"]).optional(),
            "startTime": t.string().optional(),
            "clusterUuid": t.string().optional(),
            "version": t.integer().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "dagEndTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowMetadataOut"])
    types["ClusterOperationStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClusterOperationStatusIn"]
    )
    types["ClusterOperationStatusOut"] = t.struct(
        {
            "stateStartTime": t.string().optional(),
            "innerState": t.string().optional(),
            "details": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOperationStatusOut"])
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
    types["JobMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["JobMetadataIn"]
    )
    types["JobMetadataOut"] = t.struct(
        {
            "status": t.proxy(renames["JobStatusOut"]).optional(),
            "jobId": t.string().optional(),
            "startTime": t.string().optional(),
            "operationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobMetadataOut"])
    types["YarnApplicationIn"] = t.struct(
        {
            "progress": t.number(),
            "state": t.string(),
            "trackingUrl": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["YarnApplicationIn"])
    types["YarnApplicationOut"] = t.struct(
        {
            "progress": t.number(),
            "state": t.string(),
            "trackingUrl": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YarnApplicationOut"])
    types["WorkflowNodeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WorkflowNodeIn"]
    )
    types["WorkflowNodeOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "stepId": t.string().optional(),
            "prerequisiteStepIds": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "jobId": t.string().optional(),
        }
    ).named(renames["WorkflowNodeOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["SparkHistoryServerConfigIn"] = t.struct(
        {"dataprocCluster": t.string().optional()}
    ).named(renames["SparkHistoryServerConfigIn"])
    types["SparkHistoryServerConfigOut"] = t.struct(
        {
            "dataprocCluster": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkHistoryServerConfigOut"])
    types["KubernetesSoftwareConfigIn"] = t.struct(
        {
            "componentVersion": t.struct({"_": t.string().optional()}).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["KubernetesSoftwareConfigIn"])
    types["KubernetesSoftwareConfigOut"] = t.struct(
        {
            "componentVersion": t.struct({"_": t.string().optional()}).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesSoftwareConfigOut"])
    types["InstanceGroupConfigIn"] = t.struct(
        {
            "diskConfig": t.proxy(renames["DiskConfigIn"]).optional(),
            "imageUri": t.string().optional(),
            "preemptibility": t.string().optional(),
            "minCpuPlatform": t.string().optional(),
            "numInstances": t.integer().optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorConfigIn"])).optional(),
            "machineTypeUri": t.string().optional(),
        }
    ).named(renames["InstanceGroupConfigIn"])
    types["InstanceGroupConfigOut"] = t.struct(
        {
            "diskConfig": t.proxy(renames["DiskConfigOut"]).optional(),
            "imageUri": t.string().optional(),
            "preemptibility": t.string().optional(),
            "minCpuPlatform": t.string().optional(),
            "numInstances": t.integer().optional(),
            "instanceReferences": t.array(
                t.proxy(renames["InstanceReferenceOut"])
            ).optional(),
            "managedGroupConfig": t.proxy(renames["ManagedGroupConfigOut"]).optional(),
            "instanceNames": t.array(t.string()).optional(),
            "accelerators": t.array(
                t.proxy(renames["AcceleratorConfigOut"])
            ).optional(),
            "isPreemptible": t.boolean().optional(),
            "machineTypeUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceGroupConfigOut"])
    types["RegexValidationIn"] = t.struct({"regexes": t.array(t.string())}).named(
        renames["RegexValidationIn"]
    )
    types["RegexValidationOut"] = t.struct(
        {
            "regexes": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegexValidationOut"])
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
    types["SparkRJobIn"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "mainRFileUri": t.string(),
        }
    ).named(renames["SparkRJobIn"])
    types["SparkRJobOut"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "mainRFileUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkRJobOut"])
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
    types["SparkRBatchIn"] = t.struct(
        {
            "fileUris": t.array(t.string()).optional(),
            "mainRFileUri": t.string(),
            "args": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
        }
    ).named(renames["SparkRBatchIn"])
    types["SparkRBatchOut"] = t.struct(
        {
            "fileUris": t.array(t.string()).optional(),
            "mainRFileUri": t.string(),
            "args": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkRBatchOut"])
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
            "virtualClusterConfig": t.proxy(
                renames["VirtualClusterConfigIn"]
            ).optional(),
            "projectId": t.string(),
            "clusterName": t.string(),
            "config": t.proxy(renames["ClusterConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ClusterIn"])
    types["ClusterOut"] = t.struct(
        {
            "virtualClusterConfig": t.proxy(
                renames["VirtualClusterConfigOut"]
            ).optional(),
            "projectId": t.string(),
            "statusHistory": t.array(t.proxy(renames["ClusterStatusOut"])).optional(),
            "clusterName": t.string(),
            "config": t.proxy(renames["ClusterConfigOut"]).optional(),
            "clusterUuid": t.string().optional(),
            "status": t.proxy(renames["ClusterStatusOut"]).optional(),
            "metrics": t.proxy(renames["ClusterMetricsOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOut"])
    types["KerberosConfigIn"] = t.struct(
        {
            "keystoreUri": t.string().optional(),
            "keystorePasswordUri": t.string().optional(),
            "crossRealmTrustAdminServer": t.string().optional(),
            "kdcDbKeyUri": t.string().optional(),
            "crossRealmTrustKdc": t.string().optional(),
            "tgtLifetimeHours": t.integer().optional(),
            "keyPasswordUri": t.string().optional(),
            "kmsKeyUri": t.string().optional(),
            "crossRealmTrustRealm": t.string().optional(),
            "crossRealmTrustSharedPasswordUri": t.string().optional(),
            "rootPrincipalPasswordUri": t.string().optional(),
            "realm": t.string().optional(),
            "truststoreUri": t.string().optional(),
            "enableKerberos": t.boolean().optional(),
            "truststorePasswordUri": t.string().optional(),
        }
    ).named(renames["KerberosConfigIn"])
    types["KerberosConfigOut"] = t.struct(
        {
            "keystoreUri": t.string().optional(),
            "keystorePasswordUri": t.string().optional(),
            "crossRealmTrustAdminServer": t.string().optional(),
            "kdcDbKeyUri": t.string().optional(),
            "crossRealmTrustKdc": t.string().optional(),
            "tgtLifetimeHours": t.integer().optional(),
            "keyPasswordUri": t.string().optional(),
            "kmsKeyUri": t.string().optional(),
            "crossRealmTrustRealm": t.string().optional(),
            "crossRealmTrustSharedPasswordUri": t.string().optional(),
            "rootPrincipalPasswordUri": t.string().optional(),
            "realm": t.string().optional(),
            "truststoreUri": t.string().optional(),
            "enableKerberos": t.boolean().optional(),
            "truststorePasswordUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KerberosConfigOut"])
    types["NodeGroupIn"] = t.struct(
        {
            "nodeGroupConfig": t.proxy(renames["InstanceGroupConfigIn"]).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "roles": t.array(t.string()),
        }
    ).named(renames["NodeGroupIn"])
    types["NodeGroupOut"] = t.struct(
        {
            "nodeGroupConfig": t.proxy(renames["InstanceGroupConfigOut"]).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "roles": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeGroupOut"])
    types["SessionOperationMetadataIn"] = t.struct(
        {
            "operationType": t.string().optional(),
            "doneTime": t.string().optional(),
            "sessionUuid": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "session": t.string().optional(),
            "createTime": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
        }
    ).named(renames["SessionOperationMetadataIn"])
    types["SessionOperationMetadataOut"] = t.struct(
        {
            "operationType": t.string().optional(),
            "doneTime": t.string().optional(),
            "sessionUuid": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "session": t.string().optional(),
            "createTime": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionOperationMetadataOut"])
    types["WorkflowTemplatePlacementIn"] = t.struct(
        {
            "clusterSelector": t.proxy(renames["ClusterSelectorIn"]).optional(),
            "managedCluster": t.proxy(renames["ManagedClusterIn"]).optional(),
        }
    ).named(renames["WorkflowTemplatePlacementIn"])
    types["WorkflowTemplatePlacementOut"] = t.struct(
        {
            "clusterSelector": t.proxy(renames["ClusterSelectorOut"]).optional(),
            "managedCluster": t.proxy(renames["ManagedClusterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowTemplatePlacementOut"])
    types["UsageSnapshotIn"] = t.struct(
        {
            "shuffleStorageGb": t.string().optional(),
            "milliDcu": t.string().optional(),
            "snapshotTime": t.string().optional(),
        }
    ).named(renames["UsageSnapshotIn"])
    types["UsageSnapshotOut"] = t.struct(
        {
            "shuffleStorageGb": t.string().optional(),
            "milliDcu": t.string().optional(),
            "snapshotTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageSnapshotOut"])
    types["JobIn"] = t.struct(
        {
            "hadoopJob": t.proxy(renames["HadoopJobIn"]).optional(),
            "prestoJob": t.proxy(renames["PrestoJobIn"]).optional(),
            "driverSchedulingConfig": t.proxy(
                renames["DriverSchedulingConfigIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pigJob": t.proxy(renames["PigJobIn"]).optional(),
            "pysparkJob": t.proxy(renames["PySparkJobIn"]).optional(),
            "sparkSqlJob": t.proxy(renames["SparkSqlJobIn"]).optional(),
            "sparkRJob": t.proxy(renames["SparkRJobIn"]).optional(),
            "reference": t.proxy(renames["JobReferenceIn"]).optional(),
            "hiveJob": t.proxy(renames["HiveJobIn"]).optional(),
            "sparkJob": t.proxy(renames["SparkJobIn"]).optional(),
            "trinoJob": t.proxy(renames["TrinoJobIn"]).optional(),
            "scheduling": t.proxy(renames["JobSchedulingIn"]).optional(),
            "placement": t.proxy(renames["JobPlacementIn"]),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "hadoopJob": t.proxy(renames["HadoopJobOut"]).optional(),
            "done": t.boolean().optional(),
            "prestoJob": t.proxy(renames["PrestoJobOut"]).optional(),
            "driverSchedulingConfig": t.proxy(
                renames["DriverSchedulingConfigOut"]
            ).optional(),
            "status": t.proxy(renames["JobStatusOut"]).optional(),
            "jobUuid": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pigJob": t.proxy(renames["PigJobOut"]).optional(),
            "yarnApplications": t.array(
                t.proxy(renames["YarnApplicationOut"])
            ).optional(),
            "pysparkJob": t.proxy(renames["PySparkJobOut"]).optional(),
            "sparkSqlJob": t.proxy(renames["SparkSqlJobOut"]).optional(),
            "sparkRJob": t.proxy(renames["SparkRJobOut"]).optional(),
            "driverOutputResourceUri": t.string().optional(),
            "reference": t.proxy(renames["JobReferenceOut"]).optional(),
            "hiveJob": t.proxy(renames["HiveJobOut"]).optional(),
            "statusHistory": t.array(t.proxy(renames["JobStatusOut"])).optional(),
            "sparkJob": t.proxy(renames["SparkJobOut"]).optional(),
            "trinoJob": t.proxy(renames["TrinoJobOut"]).optional(),
            "scheduling": t.proxy(renames["JobSchedulingOut"]).optional(),
            "placement": t.proxy(renames["JobPlacementOut"]),
            "driverControlFilesUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["ReservationAffinityIn"] = t.struct(
        {
            "key": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "consumeReservationType": t.string().optional(),
        }
    ).named(renames["ReservationAffinityIn"])
    types["ReservationAffinityOut"] = t.struct(
        {
            "key": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "consumeReservationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReservationAffinityOut"])
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
    types["SparkBatchIn"] = t.struct(
        {
            "mainClass": t.string().optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "mainJarFileUri": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
        }
    ).named(renames["SparkBatchIn"])
    types["SparkBatchOut"] = t.struct(
        {
            "mainClass": t.string().optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "mainJarFileUri": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkBatchOut"])
    types["ManagedClusterIn"] = t.struct(
        {
            "clusterName": t.string(),
            "config": t.proxy(renames["ClusterConfigIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ManagedClusterIn"])
    types["ManagedClusterOut"] = t.struct(
        {
            "clusterName": t.string(),
            "config": t.proxy(renames["ClusterConfigOut"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedClusterOut"])
    types["RuntimeConfigIn"] = t.struct(
        {
            "version": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "containerImage": t.string().optional(),
        }
    ).named(renames["RuntimeConfigIn"])
    types["RuntimeConfigOut"] = t.struct(
        {
            "version": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "containerImage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeConfigOut"])
    types["AutoscalingConfigIn"] = t.struct({"policyUri": t.string().optional()}).named(
        renames["AutoscalingConfigIn"]
    )
    types["AutoscalingConfigOut"] = t.struct(
        {
            "policyUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoscalingConfigOut"])
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
    types["StartClusterRequestIn"] = t.struct(
        {"clusterUuid": t.string().optional(), "requestId": t.string().optional()}
    ).named(renames["StartClusterRequestIn"])
    types["StartClusterRequestOut"] = t.struct(
        {
            "clusterUuid": t.string().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartClusterRequestOut"])
    types["StateHistoryIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StateHistoryIn"]
    )
    types["StateHistoryOut"] = t.struct(
        {
            "stateStartTime": t.string().optional(),
            "state": t.string().optional(),
            "stateMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StateHistoryOut"])
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
    types["MetastoreConfigIn"] = t.struct(
        {"dataprocMetastoreService": t.string()}
    ).named(renames["MetastoreConfigIn"])
    types["MetastoreConfigOut"] = t.struct(
        {
            "dataprocMetastoreService": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetastoreConfigOut"])
    types["PigJobIn"] = t.struct(
        {
            "continueOnFailure": t.boolean().optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "queryFileUri": t.string().optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PigJobIn"])
    types["PigJobOut"] = t.struct(
        {
            "continueOnFailure": t.boolean().optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "queryFileUri": t.string().optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PigJobOut"])
    types["NodeGroupAffinityIn"] = t.struct({"nodeGroupUri": t.string()}).named(
        renames["NodeGroupAffinityIn"]
    )
    types["NodeGroupAffinityOut"] = t.struct(
        {
            "nodeGroupUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeGroupAffinityOut"])
    types["SparkStandaloneAutoscalingConfigIn"] = t.struct(
        {
            "scaleUpMinWorkerFraction": t.number().optional(),
            "scaleUpFactor": t.number(),
            "scaleDownFactor": t.number(),
            "gracefulDecommissionTimeout": t.string(),
            "scaleDownMinWorkerFraction": t.number().optional(),
        }
    ).named(renames["SparkStandaloneAutoscalingConfigIn"])
    types["SparkStandaloneAutoscalingConfigOut"] = t.struct(
        {
            "scaleUpMinWorkerFraction": t.number().optional(),
            "scaleUpFactor": t.number(),
            "scaleDownFactor": t.number(),
            "gracefulDecommissionTimeout": t.string(),
            "scaleDownMinWorkerFraction": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkStandaloneAutoscalingConfigOut"])
    types["CancelJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelJobRequestIn"]
    )
    types["CancelJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelJobRequestOut"])
    types["ExecutionConfigIn"] = t.struct(
        {
            "idleTtl": t.string().optional(),
            "stagingBucket": t.string().optional(),
            "subnetworkUri": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "ttl": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "kmsKey": t.string().optional(),
            "networkUri": t.string().optional(),
        }
    ).named(renames["ExecutionConfigIn"])
    types["ExecutionConfigOut"] = t.struct(
        {
            "idleTtl": t.string().optional(),
            "stagingBucket": t.string().optional(),
            "subnetworkUri": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "ttl": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "kmsKey": t.string().optional(),
            "networkUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionConfigOut"])
    types["SoftwareConfigIn"] = t.struct(
        {
            "imageVersion": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "optionalComponents": t.array(t.string()).optional(),
        }
    ).named(renames["SoftwareConfigIn"])
    types["SoftwareConfigOut"] = t.struct(
        {
            "imageVersion": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "optionalComponents": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SoftwareConfigOut"])
    types["ClusterOperationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClusterOperationIn"]
    )
    types["ClusterOperationOut"] = t.struct(
        {
            "operationId": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOperationOut"])
    types["JobPlacementIn"] = t.struct(
        {
            "clusterName": t.string(),
            "clusterLabels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["JobPlacementIn"])
    types["JobPlacementOut"] = t.struct(
        {
            "clusterName": t.string(),
            "clusterLabels": t.struct({"_": t.string().optional()}).optional(),
            "clusterUuid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobPlacementOut"])
    types["JobSchedulingIn"] = t.struct(
        {
            "maxFailuresTotal": t.integer().optional(),
            "maxFailuresPerHour": t.integer().optional(),
        }
    ).named(renames["JobSchedulingIn"])
    types["JobSchedulingOut"] = t.struct(
        {
            "maxFailuresTotal": t.integer().optional(),
            "maxFailuresPerHour": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobSchedulingOut"])
    types["IdentityConfigIn"] = t.struct(
        {"userServiceAccountMapping": t.struct({"_": t.string().optional()})}
    ).named(renames["IdentityConfigIn"])
    types["IdentityConfigOut"] = t.struct(
        {
            "userServiceAccountMapping": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityConfigOut"])
    types["GkeClusterConfigIn"] = t.struct(
        {
            "gkeClusterTarget": t.string().optional(),
            "nodePoolTarget": t.array(
                t.proxy(renames["GkeNodePoolTargetIn"])
            ).optional(),
            "namespacedGkeDeploymentTarget": t.proxy(
                renames["NamespacedGkeDeploymentTargetIn"]
            ).optional(),
        }
    ).named(renames["GkeClusterConfigIn"])
    types["GkeClusterConfigOut"] = t.struct(
        {
            "gkeClusterTarget": t.string().optional(),
            "nodePoolTarget": t.array(
                t.proxy(renames["GkeNodePoolTargetOut"])
            ).optional(),
            "namespacedGkeDeploymentTarget": t.proxy(
                renames["NamespacedGkeDeploymentTargetOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeClusterConfigOut"])
    types["LoggingConfigIn"] = t.struct(
        {"driverLogLevels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["LoggingConfigIn"])
    types["LoggingConfigOut"] = t.struct(
        {
            "driverLogLevels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingConfigOut"])
    types["GceClusterConfigIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "reservationAffinity": t.proxy(renames["ReservationAffinityIn"]).optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "internalIpOnly": t.boolean().optional(),
            "networkUri": t.string().optional(),
            "nodeGroupAffinity": t.proxy(renames["NodeGroupAffinityIn"]).optional(),
            "serviceAccount": t.string().optional(),
            "zoneUri": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "confidentialInstanceConfig": t.proxy(
                renames["ConfidentialInstanceConfigIn"]
            ).optional(),
            "serviceAccountScopes": t.array(t.string()).optional(),
            "subnetworkUri": t.string().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigIn"]
            ).optional(),
        }
    ).named(renames["GceClusterConfigIn"])
    types["GceClusterConfigOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "reservationAffinity": t.proxy(
                renames["ReservationAffinityOut"]
            ).optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "internalIpOnly": t.boolean().optional(),
            "networkUri": t.string().optional(),
            "nodeGroupAffinity": t.proxy(renames["NodeGroupAffinityOut"]).optional(),
            "serviceAccount": t.string().optional(),
            "zoneUri": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "confidentialInstanceConfig": t.proxy(
                renames["ConfidentialInstanceConfigOut"]
            ).optional(),
            "serviceAccountScopes": t.array(t.string()).optional(),
            "subnetworkUri": t.string().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceClusterConfigOut"])
    types["PrestoJobIn"] = t.struct(
        {
            "continueOnFailure": t.boolean().optional(),
            "outputFormat": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "clientTags": t.array(t.string()).optional(),
            "queryFileUri": t.string().optional(),
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
        }
    ).named(renames["PrestoJobIn"])
    types["PrestoJobOut"] = t.struct(
        {
            "continueOnFailure": t.boolean().optional(),
            "outputFormat": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "clientTags": t.array(t.string()).optional(),
            "queryFileUri": t.string().optional(),
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrestoJobOut"])
    types["QueryListIn"] = t.struct({"queries": t.array(t.string())}).named(
        renames["QueryListIn"]
    )
    types["QueryListOut"] = t.struct(
        {
            "queries": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryListOut"])
    types["SparkJobIn"] = t.struct(
        {
            "mainJarFileUri": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "fileUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
        }
    ).named(renames["SparkJobIn"])
    types["SparkJobOut"] = t.struct(
        {
            "mainJarFileUri": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "fileUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkJobOut"])
    types["NodePoolIn"] = t.struct(
        {
            "instanceNames": t.array(t.string()).optional(),
            "id": t.string(),
            "repairAction": t.string(),
        }
    ).named(renames["NodePoolIn"])
    types["NodePoolOut"] = t.struct(
        {
            "instanceNames": t.array(t.string()).optional(),
            "id": t.string(),
            "repairAction": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolOut"])
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
    types["BatchOperationMetadataIn"] = t.struct(
        {
            "batch": t.string().optional(),
            "description": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "operationType": t.string().optional(),
            "createTime": t.string().optional(),
            "batchUuid": t.string().optional(),
            "doneTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["BatchOperationMetadataIn"])
    types["BatchOperationMetadataOut"] = t.struct(
        {
            "batch": t.string().optional(),
            "description": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "operationType": t.string().optional(),
            "createTime": t.string().optional(),
            "batchUuid": t.string().optional(),
            "doneTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchOperationMetadataOut"])
    types["GkeNodeConfigIn"] = t.struct(
        {
            "spot": t.boolean().optional(),
            "localSsdCount": t.integer().optional(),
            "minCpuPlatform": t.string().optional(),
            "accelerators": t.array(
                t.proxy(renames["GkeNodePoolAcceleratorConfigIn"])
            ).optional(),
            "machineType": t.string().optional(),
            "bootDiskKmsKey": t.string().optional(),
            "preemptible": t.boolean().optional(),
        }
    ).named(renames["GkeNodeConfigIn"])
    types["GkeNodeConfigOut"] = t.struct(
        {
            "spot": t.boolean().optional(),
            "localSsdCount": t.integer().optional(),
            "minCpuPlatform": t.string().optional(),
            "accelerators": t.array(
                t.proxy(renames["GkeNodePoolAcceleratorConfigOut"])
            ).optional(),
            "machineType": t.string().optional(),
            "bootDiskKmsKey": t.string().optional(),
            "preemptible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNodeConfigOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["KubernetesClusterConfigIn"] = t.struct(
        {
            "gkeClusterConfig": t.proxy(renames["GkeClusterConfigIn"]),
            "kubernetesSoftwareConfig": t.proxy(
                renames["KubernetesSoftwareConfigIn"]
            ).optional(),
            "kubernetesNamespace": t.string().optional(),
        }
    ).named(renames["KubernetesClusterConfigIn"])
    types["KubernetesClusterConfigOut"] = t.struct(
        {
            "gkeClusterConfig": t.proxy(renames["GkeClusterConfigOut"]),
            "kubernetesSoftwareConfig": t.proxy(
                renames["KubernetesSoftwareConfigOut"]
            ).optional(),
            "kubernetesNamespace": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesClusterConfigOut"])
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
    types["StopClusterRequestIn"] = t.struct(
        {"clusterUuid": t.string().optional(), "requestId": t.string().optional()}
    ).named(renames["StopClusterRequestIn"])
    types["StopClusterRequestOut"] = t.struct(
        {
            "clusterUuid": t.string().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StopClusterRequestOut"])
    types["VirtualClusterConfigIn"] = t.struct(
        {
            "stagingBucket": t.string().optional(),
            "kubernetesClusterConfig": t.proxy(renames["KubernetesClusterConfigIn"]),
            "auxiliaryServicesConfig": t.proxy(
                renames["AuxiliaryServicesConfigIn"]
            ).optional(),
        }
    ).named(renames["VirtualClusterConfigIn"])
    types["VirtualClusterConfigOut"] = t.struct(
        {
            "stagingBucket": t.string().optional(),
            "kubernetesClusterConfig": t.proxy(renames["KubernetesClusterConfigOut"]),
            "auxiliaryServicesConfig": t.proxy(
                renames["AuxiliaryServicesConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualClusterConfigOut"])
    types["DiagnoseClusterRequestIn"] = t.struct(
        {
            "jobs": t.array(t.string()).optional(),
            "diagnosisInterval": t.proxy(renames["IntervalIn"]).optional(),
            "yarnApplicationId": t.string().optional(),
            "job": t.string().optional(),
            "yarnApplicationIds": t.array(t.string()).optional(),
        }
    ).named(renames["DiagnoseClusterRequestIn"])
    types["DiagnoseClusterRequestOut"] = t.struct(
        {
            "jobs": t.array(t.string()).optional(),
            "diagnosisInterval": t.proxy(renames["IntervalOut"]).optional(),
            "yarnApplicationId": t.string().optional(),
            "job": t.string().optional(),
            "yarnApplicationIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiagnoseClusterRequestOut"])
    types["JobStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["JobStatusIn"]
    )
    types["JobStatusOut"] = t.struct(
        {
            "substate": t.string().optional(),
            "stateStartTime": t.string().optional(),
            "state": t.string().optional(),
            "details": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatusOut"])
    types["ClusterStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClusterStatusIn"]
    )
    types["ClusterStatusOut"] = t.struct(
        {
            "detail": t.string().optional(),
            "stateStartTime": t.string().optional(),
            "state": t.string().optional(),
            "substate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterStatusOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
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
    types["EndpointConfigIn"] = t.struct(
        {"enableHttpPortAccess": t.boolean().optional()}
    ).named(renames["EndpointConfigIn"])
    types["EndpointConfigOut"] = t.struct(
        {
            "enableHttpPortAccess": t.boolean().optional(),
            "httpPorts": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointConfigOut"])
    types["TemplateParameterIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string(),
            "fields": t.array(t.string()),
            "validation": t.proxy(renames["ParameterValidationIn"]).optional(),
        }
    ).named(renames["TemplateParameterIn"])
    types["TemplateParameterOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string(),
            "fields": t.array(t.string()),
            "validation": t.proxy(renames["ParameterValidationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TemplateParameterOut"])
    types["InstanceGroupAutoscalingPolicyConfigIn"] = t.struct(
        {
            "maxInstances": t.integer(),
            "weight": t.integer().optional(),
            "minInstances": t.integer().optional(),
        }
    ).named(renames["InstanceGroupAutoscalingPolicyConfigIn"])
    types["InstanceGroupAutoscalingPolicyConfigOut"] = t.struct(
        {
            "maxInstances": t.integer(),
            "weight": t.integer().optional(),
            "minInstances": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceGroupAutoscalingPolicyConfigOut"])
    types["NodeInitializationActionIn"] = t.struct(
        {"executableFile": t.string(), "executionTimeout": t.string().optional()}
    ).named(renames["NodeInitializationActionIn"])
    types["NodeInitializationActionOut"] = t.struct(
        {
            "executableFile": t.string(),
            "executionTimeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeInitializationActionOut"])
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
    types["DiskConfigIn"] = t.struct(
        {
            "localSsdInterface": t.string().optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "numLocalSsds": t.integer().optional(),
            "bootDiskType": t.string().optional(),
        }
    ).named(renames["DiskConfigIn"])
    types["DiskConfigOut"] = t.struct(
        {
            "localSsdInterface": t.string().optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "numLocalSsds": t.integer().optional(),
            "bootDiskType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskConfigOut"])
    types["DiagnoseClusterResultsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DiagnoseClusterResultsIn"]
    )
    types["DiagnoseClusterResultsOut"] = t.struct(
        {
            "outputUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiagnoseClusterResultsOut"])
    types["ListAutoscalingPoliciesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ListAutoscalingPoliciesResponseIn"])
    types["ListAutoscalingPoliciesResponseOut"] = t.struct(
        {
            "policies": t.array(t.proxy(renames["AutoscalingPolicyOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAutoscalingPoliciesResponseOut"])
    types["GkeNodePoolTargetIn"] = t.struct(
        {
            "roles": t.array(t.string()),
            "nodePool": t.string(),
            "nodePoolConfig": t.proxy(renames["GkeNodePoolConfigIn"]).optional(),
        }
    ).named(renames["GkeNodePoolTargetIn"])
    types["GkeNodePoolTargetOut"] = t.struct(
        {
            "roles": t.array(t.string()),
            "nodePool": t.string(),
            "nodePoolConfig": t.proxy(renames["GkeNodePoolConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNodePoolTargetOut"])
    types["HiveJobIn"] = t.struct(
        {
            "queryFileUri": t.string().optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "continueOnFailure": t.boolean().optional(),
        }
    ).named(renames["HiveJobIn"])
    types["HiveJobOut"] = t.struct(
        {
            "queryFileUri": t.string().optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "continueOnFailure": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HiveJobOut"])
    types["JobReferenceIn"] = t.struct(
        {"jobId": t.string().optional(), "projectId": t.string().optional()}
    ).named(renames["JobReferenceIn"])
    types["JobReferenceOut"] = t.struct(
        {
            "jobId": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobReferenceOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["BasicYarnAutoscalingConfigIn"] = t.struct(
        {
            "gracefulDecommissionTimeout": t.string(),
            "scaleDownMinWorkerFraction": t.number().optional(),
            "scaleDownFactor": t.number(),
            "scaleUpMinWorkerFraction": t.number().optional(),
            "scaleUpFactor": t.number(),
        }
    ).named(renames["BasicYarnAutoscalingConfigIn"])
    types["BasicYarnAutoscalingConfigOut"] = t.struct(
        {
            "gracefulDecommissionTimeout": t.string(),
            "scaleDownMinWorkerFraction": t.number().optional(),
            "scaleDownFactor": t.number(),
            "scaleUpMinWorkerFraction": t.number().optional(),
            "scaleUpFactor": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicYarnAutoscalingConfigOut"])
    types["HadoopJobIn"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "args": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
            "mainJarFileUri": t.string().optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
        }
    ).named(renames["HadoopJobIn"])
    types["HadoopJobOut"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "args": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
            "mainJarFileUri": t.string().optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HadoopJobOut"])
    types["BatchIn"] = t.struct(
        {
            "runtimeConfig": t.proxy(renames["RuntimeConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pysparkBatch": t.proxy(renames["PySparkBatchIn"]).optional(),
            "sparkRBatch": t.proxy(renames["SparkRBatchIn"]).optional(),
            "sparkSqlBatch": t.proxy(renames["SparkSqlBatchIn"]).optional(),
            "sparkBatch": t.proxy(renames["SparkBatchIn"]).optional(),
            "environmentConfig": t.proxy(renames["EnvironmentConfigIn"]).optional(),
        }
    ).named(renames["BatchIn"])
    types["BatchOut"] = t.struct(
        {
            "runtimeConfig": t.proxy(renames["RuntimeConfigOut"]).optional(),
            "stateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "runtimeInfo": t.proxy(renames["RuntimeInfoOut"]).optional(),
            "stateHistory": t.array(t.proxy(renames["StateHistoryOut"])).optional(),
            "uuid": t.string().optional(),
            "name": t.string().optional(),
            "creator": t.string().optional(),
            "createTime": t.string().optional(),
            "pysparkBatch": t.proxy(renames["PySparkBatchOut"]).optional(),
            "stateMessage": t.string().optional(),
            "operation": t.string().optional(),
            "sparkRBatch": t.proxy(renames["SparkRBatchOut"]).optional(),
            "sparkSqlBatch": t.proxy(renames["SparkSqlBatchOut"]).optional(),
            "sparkBatch": t.proxy(renames["SparkBatchOut"]).optional(),
            "environmentConfig": t.proxy(renames["EnvironmentConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchOut"])
    types["ListJobsResponseIn"] = t.struct(
        {"nextPageToken": t.string().optional()}
    ).named(renames["ListJobsResponseIn"])
    types["ListJobsResponseOut"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobsResponseOut"])
    types["UsageMetricsIn"] = t.struct(
        {
            "shuffleStorageGbSeconds": t.string().optional(),
            "milliDcuSeconds": t.string().optional(),
        }
    ).named(renames["UsageMetricsIn"])
    types["UsageMetricsOut"] = t.struct(
        {
            "shuffleStorageGbSeconds": t.string().optional(),
            "milliDcuSeconds": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageMetricsOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["OrderedJobIn"] = t.struct(
        {
            "hadoopJob": t.proxy(renames["HadoopJobIn"]).optional(),
            "hiveJob": t.proxy(renames["HiveJobIn"]).optional(),
            "pysparkJob": t.proxy(renames["PySparkJobIn"]).optional(),
            "prestoJob": t.proxy(renames["PrestoJobIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sparkRJob": t.proxy(renames["SparkRJobIn"]).optional(),
            "scheduling": t.proxy(renames["JobSchedulingIn"]).optional(),
            "sparkSqlJob": t.proxy(renames["SparkSqlJobIn"]).optional(),
            "prerequisiteStepIds": t.array(t.string()).optional(),
            "pigJob": t.proxy(renames["PigJobIn"]).optional(),
            "sparkJob": t.proxy(renames["SparkJobIn"]).optional(),
            "stepId": t.string(),
            "trinoJob": t.proxy(renames["TrinoJobIn"]).optional(),
        }
    ).named(renames["OrderedJobIn"])
    types["OrderedJobOut"] = t.struct(
        {
            "hadoopJob": t.proxy(renames["HadoopJobOut"]).optional(),
            "hiveJob": t.proxy(renames["HiveJobOut"]).optional(),
            "pysparkJob": t.proxy(renames["PySparkJobOut"]).optional(),
            "prestoJob": t.proxy(renames["PrestoJobOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sparkRJob": t.proxy(renames["SparkRJobOut"]).optional(),
            "scheduling": t.proxy(renames["JobSchedulingOut"]).optional(),
            "sparkSqlJob": t.proxy(renames["SparkSqlJobOut"]).optional(),
            "prerequisiteStepIds": t.array(t.string()).optional(),
            "pigJob": t.proxy(renames["PigJobOut"]).optional(),
            "sparkJob": t.proxy(renames["SparkJobOut"]).optional(),
            "stepId": t.string(),
            "trinoJob": t.proxy(renames["TrinoJobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderedJobOut"])
    types["ConfidentialInstanceConfigIn"] = t.struct(
        {"enableConfidentialCompute": t.boolean().optional()}
    ).named(renames["ConfidentialInstanceConfigIn"])
    types["ConfidentialInstanceConfigOut"] = t.struct(
        {
            "enableConfidentialCompute": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfidentialInstanceConfigOut"])
    types["EncryptionConfigIn"] = t.struct(
        {"kmsKey": t.string().optional(), "gcePdKmsKeyName": t.string().optional()}
    ).named(renames["EncryptionConfigIn"])
    types["EncryptionConfigOut"] = t.struct(
        {
            "kmsKey": t.string().optional(),
            "gcePdKmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
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
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["NamespacedGkeDeploymentTargetIn"] = t.struct(
        {
            "targetGkeCluster": t.string().optional(),
            "clusterNamespace": t.string().optional(),
        }
    ).named(renames["NamespacedGkeDeploymentTargetIn"])
    types["NamespacedGkeDeploymentTargetOut"] = t.struct(
        {
            "targetGkeCluster": t.string().optional(),
            "clusterNamespace": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamespacedGkeDeploymentTargetOut"])
    types["AutoscalingPolicyIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string(),
            "secondaryWorkerConfig": t.proxy(
                renames["InstanceGroupAutoscalingPolicyConfigIn"]
            ).optional(),
            "workerConfig": t.proxy(renames["InstanceGroupAutoscalingPolicyConfigIn"]),
            "basicAlgorithm": t.proxy(renames["BasicAutoscalingAlgorithmIn"]),
        }
    ).named(renames["AutoscalingPolicyIn"])
    types["AutoscalingPolicyOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string(),
            "secondaryWorkerConfig": t.proxy(
                renames["InstanceGroupAutoscalingPolicyConfigOut"]
            ).optional(),
            "workerConfig": t.proxy(renames["InstanceGroupAutoscalingPolicyConfigOut"]),
            "basicAlgorithm": t.proxy(renames["BasicAutoscalingAlgorithmOut"]),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoscalingPolicyOut"])
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
    types["NodeGroupOperationMetadataIn"] = t.struct(
        {"operationType": t.string().optional()}
    ).named(renames["NodeGroupOperationMetadataIn"])
    types["NodeGroupOperationMetadataOut"] = t.struct(
        {
            "status": t.proxy(renames["ClusterOperationStatusOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "warnings": t.array(t.string()).optional(),
            "operationType": t.string().optional(),
            "nodeGroupId": t.string().optional(),
            "clusterUuid": t.string().optional(),
            "description": t.string().optional(),
            "statusHistory": t.array(
                t.proxy(renames["ClusterOperationStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeGroupOperationMetadataOut"])
    types["InstanceReferenceIn"] = t.struct(
        {
            "instanceName": t.string().optional(),
            "publicKey": t.string().optional(),
            "instanceId": t.string().optional(),
            "publicEciesKey": t.string().optional(),
        }
    ).named(renames["InstanceReferenceIn"])
    types["InstanceReferenceOut"] = t.struct(
        {
            "instanceName": t.string().optional(),
            "publicKey": t.string().optional(),
            "instanceId": t.string().optional(),
            "publicEciesKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceReferenceOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["LifecycleConfigIn"] = t.struct(
        {
            "autoDeleteTime": t.string().optional(),
            "idleDeleteTtl": t.string().optional(),
            "autoDeleteTtl": t.string().optional(),
        }
    ).named(renames["LifecycleConfigIn"])
    types["LifecycleConfigOut"] = t.struct(
        {
            "autoDeleteTime": t.string().optional(),
            "idleStartTime": t.string().optional(),
            "idleDeleteTtl": t.string().optional(),
            "autoDeleteTtl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LifecycleConfigOut"])
    types["ValueValidationIn"] = t.struct({"values": t.array(t.string())}).named(
        renames["ValueValidationIn"]
    )
    types["ValueValidationOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueValidationOut"])
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
    types["SparkSqlJobIn"] = t.struct(
        {
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "queryFileUri": t.string().optional(),
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
            "jarFileUris": t.array(t.string()).optional(),
        }
    ).named(renames["SparkSqlJobIn"])
    types["SparkSqlJobOut"] = t.struct(
        {
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "queryFileUri": t.string().optional(),
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkSqlJobOut"])
    types["ClusterOperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClusterOperationMetadataIn"]
    )
    types["ClusterOperationMetadataOut"] = t.struct(
        {
            "clusterName": t.string().optional(),
            "statusHistory": t.array(
                t.proxy(renames["ClusterOperationStatusOut"])
            ).optional(),
            "childOperationIds": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "warnings": t.array(t.string()).optional(),
            "status": t.proxy(renames["ClusterOperationStatusOut"]).optional(),
            "operationType": t.string().optional(),
            "clusterUuid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOperationMetadataOut"])
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
    types["WorkflowTemplateIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "dagTimeout": t.string().optional(),
            "jobs": t.array(t.proxy(renames["OrderedJobIn"])),
            "placement": t.proxy(renames["WorkflowTemplatePlacementIn"]),
            "parameters": t.array(t.proxy(renames["TemplateParameterIn"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string(),
        }
    ).named(renames["WorkflowTemplateIn"])
    types["WorkflowTemplateOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "version": t.integer().optional(),
            "dagTimeout": t.string().optional(),
            "updateTime": t.string().optional(),
            "jobs": t.array(t.proxy(renames["OrderedJobOut"])),
            "placement": t.proxy(renames["WorkflowTemplatePlacementOut"]),
            "name": t.string().optional(),
            "parameters": t.array(t.proxy(renames["TemplateParameterOut"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowTemplateOut"])
    types["TrinoJobIn"] = t.struct(
        {
            "continueOnFailure": t.boolean().optional(),
            "queryFileUri": t.string().optional(),
            "clientTags": t.array(t.string()).optional(),
            "outputFormat": t.string().optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
        }
    ).named(renames["TrinoJobIn"])
    types["TrinoJobOut"] = t.struct(
        {
            "continueOnFailure": t.boolean().optional(),
            "queryFileUri": t.string().optional(),
            "clientTags": t.array(t.string()).optional(),
            "outputFormat": t.string().optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrinoJobOut"])

    functions = {}
    functions["projectsRegionsJobsCancel"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsSubmitAsOperation"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsTestIamPermissions"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsDelete"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsSubmit"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsGet"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsList"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsGetIamPolicy"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsPatch"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsSetIamPolicy"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesGet"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesDelete"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesGetIamPolicy"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesUpdate"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesTestIamPermissions"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesCreate"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesList"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesSetIamPolicy"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersRepair"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:stop",
        t.struct(
            {
                "projectId": t.string(),
                "region": t.string(),
                "clusterName": t.string(),
                "clusterUuid": t.string().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersStart"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:stop",
        t.struct(
            {
                "projectId": t.string(),
                "region": t.string(),
                "clusterName": t.string(),
                "clusterUuid": t.string().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersGet"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:stop",
        t.struct(
            {
                "projectId": t.string(),
                "region": t.string(),
                "clusterName": t.string(),
                "clusterUuid": t.string().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersGetIamPolicy"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:stop",
        t.struct(
            {
                "projectId": t.string(),
                "region": t.string(),
                "clusterName": t.string(),
                "clusterUuid": t.string().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersInjectCredentials"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:stop",
        t.struct(
            {
                "projectId": t.string(),
                "region": t.string(),
                "clusterName": t.string(),
                "clusterUuid": t.string().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersSetIamPolicy"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:stop",
        t.struct(
            {
                "projectId": t.string(),
                "region": t.string(),
                "clusterName": t.string(),
                "clusterUuid": t.string().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersDelete"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:stop",
        t.struct(
            {
                "projectId": t.string(),
                "region": t.string(),
                "clusterName": t.string(),
                "clusterUuid": t.string().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersTestIamPermissions"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:stop",
        t.struct(
            {
                "projectId": t.string(),
                "region": t.string(),
                "clusterName": t.string(),
                "clusterUuid": t.string().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersList"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:stop",
        t.struct(
            {
                "projectId": t.string(),
                "region": t.string(),
                "clusterName": t.string(),
                "clusterUuid": t.string().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersPatch"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:stop",
        t.struct(
            {
                "projectId": t.string(),
                "region": t.string(),
                "clusterName": t.string(),
                "clusterUuid": t.string().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersDiagnose"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:stop",
        t.struct(
            {
                "projectId": t.string(),
                "region": t.string(),
                "clusterName": t.string(),
                "clusterUuid": t.string().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersCreate"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:stop",
        t.struct(
            {
                "projectId": t.string(),
                "region": t.string(),
                "clusterName": t.string(),
                "clusterUuid": t.string().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersStop"] = dataproc.post(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:stop",
        t.struct(
            {
                "projectId": t.string(),
                "region": t.string(),
                "clusterName": t.string(),
                "clusterUuid": t.string().optional(),
                "requestId": t.string().optional(),
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
                "nodeGroupConfig": t.proxy(renames["InstanceGroupConfigIn"]).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "roles": t.array(t.string()),
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
                "nodeGroupConfig": t.proxy(renames["InstanceGroupConfigIn"]).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "roles": t.array(t.string()),
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
                "nodeGroupConfig": t.proxy(renames["InstanceGroupConfigIn"]).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "roles": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsTestIamPermissions"] = dataproc.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsGetIamPolicy"] = dataproc.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsDelete"] = dataproc.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsGet"] = dataproc.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsCancel"] = dataproc.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsSetIamPolicy"] = dataproc.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsList"] = dataproc.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesUpdate"] = dataproc.post(
        "v1/{name}:instantiate",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "version": t.integer().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesCreate"] = dataproc.post(
        "v1/{name}:instantiate",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "version": t.integer().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesList"] = dataproc.post(
        "v1/{name}:instantiate",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "version": t.integer().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesSetIamPolicy"] = dataproc.post(
        "v1/{name}:instantiate",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "version": t.integer().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesTestIamPermissions"] = dataproc.post(
        "v1/{name}:instantiate",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "version": t.integer().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesInstantiateInline"] = dataproc.post(
        "v1/{name}:instantiate",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "version": t.integer().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesGetIamPolicy"] = dataproc.post(
        "v1/{name}:instantiate",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "version": t.integer().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesGet"] = dataproc.post(
        "v1/{name}:instantiate",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "version": t.integer().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesDelete"] = dataproc.post(
        "v1/{name}:instantiate",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "version": t.integer().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesInstantiate"] = dataproc.post(
        "v1/{name}:instantiate",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "version": t.integer().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesTestIamPermissions"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesDelete"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesUpdate"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesInstantiateInline"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesCreate"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesList"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesGet"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesInstantiate"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesGetIamPolicy"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesSetIamPolicy"] = dataproc.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBatchesCreate"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBatchesGet"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBatchesList"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBatchesDelete"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = dataproc.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = dataproc.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = dataproc.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = dataproc.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAutoscalingPoliciesDelete"] = dataproc.post(
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
    functions["projectsLocationsAutoscalingPoliciesGet"] = dataproc.post(
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
    functions["projectsLocationsAutoscalingPoliciesUpdate"] = dataproc.post(
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
    functions["projectsLocationsAutoscalingPoliciesList"] = dataproc.post(
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
    functions["projectsLocationsAutoscalingPoliciesGetIamPolicy"] = dataproc.post(
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
    functions["projectsLocationsAutoscalingPoliciesCreate"] = dataproc.post(
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
    functions["projectsLocationsAutoscalingPoliciesSetIamPolicy"] = dataproc.post(
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
    functions["projectsLocationsAutoscalingPoliciesTestIamPermissions"] = dataproc.post(
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

    return Import(
        importer="dataproc", renames=renames, types=types, functions=functions
    )
