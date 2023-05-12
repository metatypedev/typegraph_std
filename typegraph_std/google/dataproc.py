from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_dataproc() -> Import:
    dataproc = HTTPRuntime("https://dataproc.googleapis.com/")

    renames = {
        "ErrorResponse": "_dataproc_1_ErrorResponse",
        "TemplateParameterIn": "_dataproc_2_TemplateParameterIn",
        "TemplateParameterOut": "_dataproc_3_TemplateParameterOut",
        "PolicyIn": "_dataproc_4_PolicyIn",
        "PolicyOut": "_dataproc_5_PolicyOut",
        "SoftwareConfigIn": "_dataproc_6_SoftwareConfigIn",
        "SoftwareConfigOut": "_dataproc_7_SoftwareConfigOut",
        "InstanceReferenceIn": "_dataproc_8_InstanceReferenceIn",
        "InstanceReferenceOut": "_dataproc_9_InstanceReferenceOut",
        "SparkBatchIn": "_dataproc_10_SparkBatchIn",
        "SparkBatchOut": "_dataproc_11_SparkBatchOut",
        "WorkflowGraphIn": "_dataproc_12_WorkflowGraphIn",
        "WorkflowGraphOut": "_dataproc_13_WorkflowGraphOut",
        "AcceleratorConfigIn": "_dataproc_14_AcceleratorConfigIn",
        "AcceleratorConfigOut": "_dataproc_15_AcceleratorConfigOut",
        "DiskConfigIn": "_dataproc_16_DiskConfigIn",
        "DiskConfigOut": "_dataproc_17_DiskConfigOut",
        "GkeNodePoolConfigIn": "_dataproc_18_GkeNodePoolConfigIn",
        "GkeNodePoolConfigOut": "_dataproc_19_GkeNodePoolConfigOut",
        "ResizeNodeGroupRequestIn": "_dataproc_20_ResizeNodeGroupRequestIn",
        "ResizeNodeGroupRequestOut": "_dataproc_21_ResizeNodeGroupRequestOut",
        "GkeClusterConfigIn": "_dataproc_22_GkeClusterConfigIn",
        "GkeClusterConfigOut": "_dataproc_23_GkeClusterConfigOut",
        "WorkflowMetadataIn": "_dataproc_24_WorkflowMetadataIn",
        "WorkflowMetadataOut": "_dataproc_25_WorkflowMetadataOut",
        "ValueValidationIn": "_dataproc_26_ValueValidationIn",
        "ValueValidationOut": "_dataproc_27_ValueValidationOut",
        "StartClusterRequestIn": "_dataproc_28_StartClusterRequestIn",
        "StartClusterRequestOut": "_dataproc_29_StartClusterRequestOut",
        "ClusterMetricsIn": "_dataproc_30_ClusterMetricsIn",
        "ClusterMetricsOut": "_dataproc_31_ClusterMetricsOut",
        "ParameterValidationIn": "_dataproc_32_ParameterValidationIn",
        "ParameterValidationOut": "_dataproc_33_ParameterValidationOut",
        "ManagedGroupConfigIn": "_dataproc_34_ManagedGroupConfigIn",
        "ManagedGroupConfigOut": "_dataproc_35_ManagedGroupConfigOut",
        "JobMetadataIn": "_dataproc_36_JobMetadataIn",
        "JobMetadataOut": "_dataproc_37_JobMetadataOut",
        "SetIamPolicyRequestIn": "_dataproc_38_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_dataproc_39_SetIamPolicyRequestOut",
        "NamespacedGkeDeploymentTargetIn": "_dataproc_40_NamespacedGkeDeploymentTargetIn",
        "NamespacedGkeDeploymentTargetOut": "_dataproc_41_NamespacedGkeDeploymentTargetOut",
        "SessionOperationMetadataIn": "_dataproc_42_SessionOperationMetadataIn",
        "SessionOperationMetadataOut": "_dataproc_43_SessionOperationMetadataOut",
        "DiagnoseClusterResultsIn": "_dataproc_44_DiagnoseClusterResultsIn",
        "DiagnoseClusterResultsOut": "_dataproc_45_DiagnoseClusterResultsOut",
        "KubernetesClusterConfigIn": "_dataproc_46_KubernetesClusterConfigIn",
        "KubernetesClusterConfigOut": "_dataproc_47_KubernetesClusterConfigOut",
        "HadoopJobIn": "_dataproc_48_HadoopJobIn",
        "HadoopJobOut": "_dataproc_49_HadoopJobOut",
        "InstanceGroupAutoscalingPolicyConfigIn": "_dataproc_50_InstanceGroupAutoscalingPolicyConfigIn",
        "InstanceGroupAutoscalingPolicyConfigOut": "_dataproc_51_InstanceGroupAutoscalingPolicyConfigOut",
        "ListJobsResponseIn": "_dataproc_52_ListJobsResponseIn",
        "ListJobsResponseOut": "_dataproc_53_ListJobsResponseOut",
        "RuntimeConfigIn": "_dataproc_54_RuntimeConfigIn",
        "RuntimeConfigOut": "_dataproc_55_RuntimeConfigOut",
        "SubmitJobRequestIn": "_dataproc_56_SubmitJobRequestIn",
        "SubmitJobRequestOut": "_dataproc_57_SubmitJobRequestOut",
        "BatchIn": "_dataproc_58_BatchIn",
        "BatchOut": "_dataproc_59_BatchOut",
        "GetPolicyOptionsIn": "_dataproc_60_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_dataproc_61_GetPolicyOptionsOut",
        "GkeNodeConfigIn": "_dataproc_62_GkeNodeConfigIn",
        "GkeNodeConfigOut": "_dataproc_63_GkeNodeConfigOut",
        "ClusterConfigIn": "_dataproc_64_ClusterConfigIn",
        "ClusterConfigOut": "_dataproc_65_ClusterConfigOut",
        "VirtualClusterConfigIn": "_dataproc_66_VirtualClusterConfigIn",
        "VirtualClusterConfigOut": "_dataproc_67_VirtualClusterConfigOut",
        "AuxiliaryNodeGroupIn": "_dataproc_68_AuxiliaryNodeGroupIn",
        "AuxiliaryNodeGroupOut": "_dataproc_69_AuxiliaryNodeGroupOut",
        "SparkSqlBatchIn": "_dataproc_70_SparkSqlBatchIn",
        "SparkSqlBatchOut": "_dataproc_71_SparkSqlBatchOut",
        "GetIamPolicyRequestIn": "_dataproc_72_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_dataproc_73_GetIamPolicyRequestOut",
        "EmptyIn": "_dataproc_74_EmptyIn",
        "EmptyOut": "_dataproc_75_EmptyOut",
        "ClusterOperationStatusIn": "_dataproc_76_ClusterOperationStatusIn",
        "ClusterOperationStatusOut": "_dataproc_77_ClusterOperationStatusOut",
        "ConfidentialInstanceConfigIn": "_dataproc_78_ConfidentialInstanceConfigIn",
        "ConfidentialInstanceConfigOut": "_dataproc_79_ConfidentialInstanceConfigOut",
        "BasicYarnAutoscalingConfigIn": "_dataproc_80_BasicYarnAutoscalingConfigIn",
        "BasicYarnAutoscalingConfigOut": "_dataproc_81_BasicYarnAutoscalingConfigOut",
        "ListBatchesResponseIn": "_dataproc_82_ListBatchesResponseIn",
        "ListBatchesResponseOut": "_dataproc_83_ListBatchesResponseOut",
        "JobSchedulingIn": "_dataproc_84_JobSchedulingIn",
        "JobSchedulingOut": "_dataproc_85_JobSchedulingOut",
        "InstantiateWorkflowTemplateRequestIn": "_dataproc_86_InstantiateWorkflowTemplateRequestIn",
        "InstantiateWorkflowTemplateRequestOut": "_dataproc_87_InstantiateWorkflowTemplateRequestOut",
        "InstanceGroupConfigIn": "_dataproc_88_InstanceGroupConfigIn",
        "InstanceGroupConfigOut": "_dataproc_89_InstanceGroupConfigOut",
        "MetastoreConfigIn": "_dataproc_90_MetastoreConfigIn",
        "MetastoreConfigOut": "_dataproc_91_MetastoreConfigOut",
        "KerberosConfigIn": "_dataproc_92_KerberosConfigIn",
        "KerberosConfigOut": "_dataproc_93_KerberosConfigOut",
        "PySparkBatchIn": "_dataproc_94_PySparkBatchIn",
        "PySparkBatchOut": "_dataproc_95_PySparkBatchOut",
        "ListOperationsResponseIn": "_dataproc_96_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_dataproc_97_ListOperationsResponseOut",
        "ManagedClusterIn": "_dataproc_98_ManagedClusterIn",
        "ManagedClusterOut": "_dataproc_99_ManagedClusterOut",
        "SparkSqlJobIn": "_dataproc_100_SparkSqlJobIn",
        "SparkSqlJobOut": "_dataproc_101_SparkSqlJobOut",
        "WorkflowTemplateIn": "_dataproc_102_WorkflowTemplateIn",
        "WorkflowTemplateOut": "_dataproc_103_WorkflowTemplateOut",
        "QueryListIn": "_dataproc_104_QueryListIn",
        "QueryListOut": "_dataproc_105_QueryListOut",
        "PigJobIn": "_dataproc_106_PigJobIn",
        "PigJobOut": "_dataproc_107_PigJobOut",
        "CancelJobRequestIn": "_dataproc_108_CancelJobRequestIn",
        "CancelJobRequestOut": "_dataproc_109_CancelJobRequestOut",
        "JobStatusIn": "_dataproc_110_JobStatusIn",
        "JobStatusOut": "_dataproc_111_JobStatusOut",
        "UsageMetricsIn": "_dataproc_112_UsageMetricsIn",
        "UsageMetricsOut": "_dataproc_113_UsageMetricsOut",
        "ClusterSelectorIn": "_dataproc_114_ClusterSelectorIn",
        "ClusterSelectorOut": "_dataproc_115_ClusterSelectorOut",
        "PeripheralsConfigIn": "_dataproc_116_PeripheralsConfigIn",
        "PeripheralsConfigOut": "_dataproc_117_PeripheralsConfigOut",
        "GkeNodePoolAcceleratorConfigIn": "_dataproc_118_GkeNodePoolAcceleratorConfigIn",
        "GkeNodePoolAcceleratorConfigOut": "_dataproc_119_GkeNodePoolAcceleratorConfigOut",
        "ClusterOperationMetadataIn": "_dataproc_120_ClusterOperationMetadataIn",
        "ClusterOperationMetadataOut": "_dataproc_121_ClusterOperationMetadataOut",
        "GkeNodePoolTargetIn": "_dataproc_122_GkeNodePoolTargetIn",
        "GkeNodePoolTargetOut": "_dataproc_123_GkeNodePoolTargetOut",
        "JobIn": "_dataproc_124_JobIn",
        "JobOut": "_dataproc_125_JobOut",
        "EncryptionConfigIn": "_dataproc_126_EncryptionConfigIn",
        "EncryptionConfigOut": "_dataproc_127_EncryptionConfigOut",
        "ClusterOperationIn": "_dataproc_128_ClusterOperationIn",
        "ClusterOperationOut": "_dataproc_129_ClusterOperationOut",
        "GceClusterConfigIn": "_dataproc_130_GceClusterConfigIn",
        "GceClusterConfigOut": "_dataproc_131_GceClusterConfigOut",
        "AutoscalingPolicyIn": "_dataproc_132_AutoscalingPolicyIn",
        "AutoscalingPolicyOut": "_dataproc_133_AutoscalingPolicyOut",
        "TestIamPermissionsRequestIn": "_dataproc_134_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_dataproc_135_TestIamPermissionsRequestOut",
        "StatusIn": "_dataproc_136_StatusIn",
        "StatusOut": "_dataproc_137_StatusOut",
        "WorkflowNodeIn": "_dataproc_138_WorkflowNodeIn",
        "WorkflowNodeOut": "_dataproc_139_WorkflowNodeOut",
        "BasicAutoscalingAlgorithmIn": "_dataproc_140_BasicAutoscalingAlgorithmIn",
        "BasicAutoscalingAlgorithmOut": "_dataproc_141_BasicAutoscalingAlgorithmOut",
        "PrestoJobIn": "_dataproc_142_PrestoJobIn",
        "PrestoJobOut": "_dataproc_143_PrestoJobOut",
        "StateHistoryIn": "_dataproc_144_StateHistoryIn",
        "StateHistoryOut": "_dataproc_145_StateHistoryOut",
        "NodePoolIn": "_dataproc_146_NodePoolIn",
        "NodePoolOut": "_dataproc_147_NodePoolOut",
        "NodeGroupIn": "_dataproc_148_NodeGroupIn",
        "NodeGroupOut": "_dataproc_149_NodeGroupOut",
        "WorkflowTemplatePlacementIn": "_dataproc_150_WorkflowTemplatePlacementIn",
        "WorkflowTemplatePlacementOut": "_dataproc_151_WorkflowTemplatePlacementOut",
        "AuxiliaryServicesConfigIn": "_dataproc_152_AuxiliaryServicesConfigIn",
        "AuxiliaryServicesConfigOut": "_dataproc_153_AuxiliaryServicesConfigOut",
        "UsageSnapshotIn": "_dataproc_154_UsageSnapshotIn",
        "UsageSnapshotOut": "_dataproc_155_UsageSnapshotOut",
        "DriverSchedulingConfigIn": "_dataproc_156_DriverSchedulingConfigIn",
        "DriverSchedulingConfigOut": "_dataproc_157_DriverSchedulingConfigOut",
        "SecurityConfigIn": "_dataproc_158_SecurityConfigIn",
        "SecurityConfigOut": "_dataproc_159_SecurityConfigOut",
        "KubernetesSoftwareConfigIn": "_dataproc_160_KubernetesSoftwareConfigIn",
        "KubernetesSoftwareConfigOut": "_dataproc_161_KubernetesSoftwareConfigOut",
        "IntervalIn": "_dataproc_162_IntervalIn",
        "IntervalOut": "_dataproc_163_IntervalOut",
        "TestIamPermissionsResponseIn": "_dataproc_164_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_dataproc_165_TestIamPermissionsResponseOut",
        "ExecutionConfigIn": "_dataproc_166_ExecutionConfigIn",
        "ExecutionConfigOut": "_dataproc_167_ExecutionConfigOut",
        "ListClustersResponseIn": "_dataproc_168_ListClustersResponseIn",
        "ListClustersResponseOut": "_dataproc_169_ListClustersResponseOut",
        "AutoscalingConfigIn": "_dataproc_170_AutoscalingConfigIn",
        "AutoscalingConfigOut": "_dataproc_171_AutoscalingConfigOut",
        "ListAutoscalingPoliciesResponseIn": "_dataproc_172_ListAutoscalingPoliciesResponseIn",
        "ListAutoscalingPoliciesResponseOut": "_dataproc_173_ListAutoscalingPoliciesResponseOut",
        "YarnApplicationIn": "_dataproc_174_YarnApplicationIn",
        "YarnApplicationOut": "_dataproc_175_YarnApplicationOut",
        "ExprIn": "_dataproc_176_ExprIn",
        "ExprOut": "_dataproc_177_ExprOut",
        "RuntimeInfoIn": "_dataproc_178_RuntimeInfoIn",
        "RuntimeInfoOut": "_dataproc_179_RuntimeInfoOut",
        "PySparkJobIn": "_dataproc_180_PySparkJobIn",
        "PySparkJobOut": "_dataproc_181_PySparkJobOut",
        "DiagnoseClusterRequestIn": "_dataproc_182_DiagnoseClusterRequestIn",
        "DiagnoseClusterRequestOut": "_dataproc_183_DiagnoseClusterRequestOut",
        "DataprocMetricConfigIn": "_dataproc_184_DataprocMetricConfigIn",
        "DataprocMetricConfigOut": "_dataproc_185_DataprocMetricConfigOut",
        "ListWorkflowTemplatesResponseIn": "_dataproc_186_ListWorkflowTemplatesResponseIn",
        "ListWorkflowTemplatesResponseOut": "_dataproc_187_ListWorkflowTemplatesResponseOut",
        "BatchOperationMetadataIn": "_dataproc_188_BatchOperationMetadataIn",
        "BatchOperationMetadataOut": "_dataproc_189_BatchOperationMetadataOut",
        "RepairClusterRequestIn": "_dataproc_190_RepairClusterRequestIn",
        "RepairClusterRequestOut": "_dataproc_191_RepairClusterRequestOut",
        "BindingIn": "_dataproc_192_BindingIn",
        "BindingOut": "_dataproc_193_BindingOut",
        "EndpointConfigIn": "_dataproc_194_EndpointConfigIn",
        "EndpointConfigOut": "_dataproc_195_EndpointConfigOut",
        "HiveJobIn": "_dataproc_196_HiveJobIn",
        "HiveJobOut": "_dataproc_197_HiveJobOut",
        "StopClusterRequestIn": "_dataproc_198_StopClusterRequestIn",
        "StopClusterRequestOut": "_dataproc_199_StopClusterRequestOut",
        "OrderedJobIn": "_dataproc_200_OrderedJobIn",
        "OrderedJobOut": "_dataproc_201_OrderedJobOut",
        "GkeNodePoolAutoscalingConfigIn": "_dataproc_202_GkeNodePoolAutoscalingConfigIn",
        "GkeNodePoolAutoscalingConfigOut": "_dataproc_203_GkeNodePoolAutoscalingConfigOut",
        "NodeInitializationActionIn": "_dataproc_204_NodeInitializationActionIn",
        "NodeInitializationActionOut": "_dataproc_205_NodeInitializationActionOut",
        "ClusterStatusIn": "_dataproc_206_ClusterStatusIn",
        "ClusterStatusOut": "_dataproc_207_ClusterStatusOut",
        "SparkStandaloneAutoscalingConfigIn": "_dataproc_208_SparkStandaloneAutoscalingConfigIn",
        "SparkStandaloneAutoscalingConfigOut": "_dataproc_209_SparkStandaloneAutoscalingConfigOut",
        "MetricIn": "_dataproc_210_MetricIn",
        "MetricOut": "_dataproc_211_MetricOut",
        "ReservationAffinityIn": "_dataproc_212_ReservationAffinityIn",
        "ReservationAffinityOut": "_dataproc_213_ReservationAffinityOut",
        "OperationIn": "_dataproc_214_OperationIn",
        "OperationOut": "_dataproc_215_OperationOut",
        "LoggingConfigIn": "_dataproc_216_LoggingConfigIn",
        "LoggingConfigOut": "_dataproc_217_LoggingConfigOut",
        "SparkJobIn": "_dataproc_218_SparkJobIn",
        "SparkJobOut": "_dataproc_219_SparkJobOut",
        "EnvironmentConfigIn": "_dataproc_220_EnvironmentConfigIn",
        "EnvironmentConfigOut": "_dataproc_221_EnvironmentConfigOut",
        "RegexValidationIn": "_dataproc_222_RegexValidationIn",
        "RegexValidationOut": "_dataproc_223_RegexValidationOut",
        "InjectCredentialsRequestIn": "_dataproc_224_InjectCredentialsRequestIn",
        "InjectCredentialsRequestOut": "_dataproc_225_InjectCredentialsRequestOut",
        "SparkRJobIn": "_dataproc_226_SparkRJobIn",
        "SparkRJobOut": "_dataproc_227_SparkRJobOut",
        "ClusterIn": "_dataproc_228_ClusterIn",
        "ClusterOut": "_dataproc_229_ClusterOut",
        "SparkHistoryServerConfigIn": "_dataproc_230_SparkHistoryServerConfigIn",
        "SparkHistoryServerConfigOut": "_dataproc_231_SparkHistoryServerConfigOut",
        "JobReferenceIn": "_dataproc_232_JobReferenceIn",
        "JobReferenceOut": "_dataproc_233_JobReferenceOut",
        "IdentityConfigIn": "_dataproc_234_IdentityConfigIn",
        "IdentityConfigOut": "_dataproc_235_IdentityConfigOut",
        "NodeGroupAffinityIn": "_dataproc_236_NodeGroupAffinityIn",
        "NodeGroupAffinityOut": "_dataproc_237_NodeGroupAffinityOut",
        "ShieldedInstanceConfigIn": "_dataproc_238_ShieldedInstanceConfigIn",
        "ShieldedInstanceConfigOut": "_dataproc_239_ShieldedInstanceConfigOut",
        "NodeGroupOperationMetadataIn": "_dataproc_240_NodeGroupOperationMetadataIn",
        "NodeGroupOperationMetadataOut": "_dataproc_241_NodeGroupOperationMetadataOut",
        "SparkRBatchIn": "_dataproc_242_SparkRBatchIn",
        "SparkRBatchOut": "_dataproc_243_SparkRBatchOut",
        "JobPlacementIn": "_dataproc_244_JobPlacementIn",
        "JobPlacementOut": "_dataproc_245_JobPlacementOut",
        "LifecycleConfigIn": "_dataproc_246_LifecycleConfigIn",
        "LifecycleConfigOut": "_dataproc_247_LifecycleConfigOut",
        "TrinoJobIn": "_dataproc_248_TrinoJobIn",
        "TrinoJobOut": "_dataproc_249_TrinoJobOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TemplateParameterIn"] = t.struct(
        {
            "validation": t.proxy(renames["ParameterValidationIn"]).optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "fields": t.array(t.string()),
        }
    ).named(renames["TemplateParameterIn"])
    types["TemplateParameterOut"] = t.struct(
        {
            "validation": t.proxy(renames["ParameterValidationOut"]).optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "fields": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TemplateParameterOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["InstanceReferenceIn"] = t.struct(
        {
            "instanceId": t.string().optional(),
            "publicEciesKey": t.string().optional(),
            "instanceName": t.string().optional(),
            "publicKey": t.string().optional(),
        }
    ).named(renames["InstanceReferenceIn"])
    types["InstanceReferenceOut"] = t.struct(
        {
            "instanceId": t.string().optional(),
            "publicEciesKey": t.string().optional(),
            "instanceName": t.string().optional(),
            "publicKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceReferenceOut"])
    types["SparkBatchIn"] = t.struct(
        {
            "fileUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "mainJarFileUri": t.string().optional(),
            "archiveUris": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
        }
    ).named(renames["SparkBatchIn"])
    types["SparkBatchOut"] = t.struct(
        {
            "fileUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "mainJarFileUri": t.string().optional(),
            "archiveUris": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkBatchOut"])
    types["WorkflowGraphIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WorkflowGraphIn"]
    )
    types["WorkflowGraphOut"] = t.struct(
        {
            "nodes": t.array(t.proxy(renames["WorkflowNodeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowGraphOut"])
    types["AcceleratorConfigIn"] = t.struct(
        {
            "acceleratorCount": t.integer().optional(),
            "acceleratorTypeUri": t.string().optional(),
        }
    ).named(renames["AcceleratorConfigIn"])
    types["AcceleratorConfigOut"] = t.struct(
        {
            "acceleratorCount": t.integer().optional(),
            "acceleratorTypeUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorConfigOut"])
    types["DiskConfigIn"] = t.struct(
        {
            "bootDiskType": t.string().optional(),
            "localSsdInterface": t.string().optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "numLocalSsds": t.integer().optional(),
        }
    ).named(renames["DiskConfigIn"])
    types["DiskConfigOut"] = t.struct(
        {
            "bootDiskType": t.string().optional(),
            "localSsdInterface": t.string().optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "numLocalSsds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskConfigOut"])
    types["GkeNodePoolConfigIn"] = t.struct(
        {
            "locations": t.array(t.string()).optional(),
            "config": t.proxy(renames["GkeNodeConfigIn"]).optional(),
            "autoscaling": t.proxy(
                renames["GkeNodePoolAutoscalingConfigIn"]
            ).optional(),
        }
    ).named(renames["GkeNodePoolConfigIn"])
    types["GkeNodePoolConfigOut"] = t.struct(
        {
            "locations": t.array(t.string()).optional(),
            "config": t.proxy(renames["GkeNodeConfigOut"]).optional(),
            "autoscaling": t.proxy(
                renames["GkeNodePoolAutoscalingConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNodePoolConfigOut"])
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
    types["GkeClusterConfigIn"] = t.struct(
        {
            "namespacedGkeDeploymentTarget": t.proxy(
                renames["NamespacedGkeDeploymentTargetIn"]
            ).optional(),
            "gkeClusterTarget": t.string().optional(),
            "nodePoolTarget": t.array(
                t.proxy(renames["GkeNodePoolTargetIn"])
            ).optional(),
        }
    ).named(renames["GkeClusterConfigIn"])
    types["GkeClusterConfigOut"] = t.struct(
        {
            "namespacedGkeDeploymentTarget": t.proxy(
                renames["NamespacedGkeDeploymentTargetOut"]
            ).optional(),
            "gkeClusterTarget": t.string().optional(),
            "nodePoolTarget": t.array(
                t.proxy(renames["GkeNodePoolTargetOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeClusterConfigOut"])
    types["WorkflowMetadataIn"] = t.struct(
        {"parameters": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["WorkflowMetadataIn"])
    types["WorkflowMetadataOut"] = t.struct(
        {
            "dagTimeout": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "graph": t.proxy(renames["WorkflowGraphOut"]).optional(),
            "dagEndTime": t.string().optional(),
            "startTime": t.string().optional(),
            "createCluster": t.proxy(renames["ClusterOperationOut"]).optional(),
            "dagStartTime": t.string().optional(),
            "deleteCluster": t.proxy(renames["ClusterOperationOut"]).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "clusterUuid": t.string().optional(),
            "version": t.integer().optional(),
            "template": t.string().optional(),
            "clusterName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowMetadataOut"])
    types["ValueValidationIn"] = t.struct({"values": t.array(t.string())}).named(
        renames["ValueValidationIn"]
    )
    types["ValueValidationOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueValidationOut"])
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
    types["JobMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["JobMetadataIn"]
    )
    types["JobMetadataOut"] = t.struct(
        {
            "status": t.proxy(renames["JobStatusOut"]).optional(),
            "startTime": t.string().optional(),
            "operationType": t.string().optional(),
            "jobId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobMetadataOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
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
    types["SessionOperationMetadataIn"] = t.struct(
        {
            "warnings": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "session": t.string().optional(),
            "sessionUuid": t.string().optional(),
            "operationType": t.string().optional(),
            "doneTime": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["SessionOperationMetadataIn"])
    types["SessionOperationMetadataOut"] = t.struct(
        {
            "warnings": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "session": t.string().optional(),
            "sessionUuid": t.string().optional(),
            "operationType": t.string().optional(),
            "doneTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionOperationMetadataOut"])
    types["DiagnoseClusterResultsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DiagnoseClusterResultsIn"]
    )
    types["DiagnoseClusterResultsOut"] = t.struct(
        {
            "outputUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiagnoseClusterResultsOut"])
    types["KubernetesClusterConfigIn"] = t.struct(
        {
            "gkeClusterConfig": t.proxy(renames["GkeClusterConfigIn"]),
            "kubernetesNamespace": t.string().optional(),
            "kubernetesSoftwareConfig": t.proxy(
                renames["KubernetesSoftwareConfigIn"]
            ).optional(),
        }
    ).named(renames["KubernetesClusterConfigIn"])
    types["KubernetesClusterConfigOut"] = t.struct(
        {
            "gkeClusterConfig": t.proxy(renames["GkeClusterConfigOut"]),
            "kubernetesNamespace": t.string().optional(),
            "kubernetesSoftwareConfig": t.proxy(
                renames["KubernetesSoftwareConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesClusterConfigOut"])
    types["HadoopJobIn"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "mainClass": t.string().optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "mainJarFileUri": t.string().optional(),
        }
    ).named(renames["HadoopJobIn"])
    types["HadoopJobOut"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "mainClass": t.string().optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "mainJarFileUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HadoopJobOut"])
    types["InstanceGroupAutoscalingPolicyConfigIn"] = t.struct(
        {
            "minInstances": t.integer().optional(),
            "weight": t.integer().optional(),
            "maxInstances": t.integer(),
        }
    ).named(renames["InstanceGroupAutoscalingPolicyConfigIn"])
    types["InstanceGroupAutoscalingPolicyConfigOut"] = t.struct(
        {
            "minInstances": t.integer().optional(),
            "weight": t.integer().optional(),
            "maxInstances": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceGroupAutoscalingPolicyConfigOut"])
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
    types["RuntimeConfigIn"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
            "containerImage": t.string().optional(),
        }
    ).named(renames["RuntimeConfigIn"])
    types["RuntimeConfigOut"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
            "containerImage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeConfigOut"])
    types["SubmitJobRequestIn"] = t.struct(
        {"job": t.proxy(renames["JobIn"]), "requestId": t.string().optional()}
    ).named(renames["SubmitJobRequestIn"])
    types["SubmitJobRequestOut"] = t.struct(
        {
            "job": t.proxy(renames["JobOut"]),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubmitJobRequestOut"])
    types["BatchIn"] = t.struct(
        {
            "sparkSqlBatch": t.proxy(renames["SparkSqlBatchIn"]).optional(),
            "runtimeConfig": t.proxy(renames["RuntimeConfigIn"]).optional(),
            "environmentConfig": t.proxy(renames["EnvironmentConfigIn"]).optional(),
            "pysparkBatch": t.proxy(renames["PySparkBatchIn"]).optional(),
            "sparkRBatch": t.proxy(renames["SparkRBatchIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sparkBatch": t.proxy(renames["SparkBatchIn"]).optional(),
        }
    ).named(renames["BatchIn"])
    types["BatchOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "stateTime": t.string().optional(),
            "sparkSqlBatch": t.proxy(renames["SparkSqlBatchOut"]).optional(),
            "runtimeConfig": t.proxy(renames["RuntimeConfigOut"]).optional(),
            "creator": t.string().optional(),
            "runtimeInfo": t.proxy(renames["RuntimeInfoOut"]).optional(),
            "uuid": t.string().optional(),
            "name": t.string().optional(),
            "environmentConfig": t.proxy(renames["EnvironmentConfigOut"]).optional(),
            "pysparkBatch": t.proxy(renames["PySparkBatchOut"]).optional(),
            "operation": t.string().optional(),
            "stateMessage": t.string().optional(),
            "stateHistory": t.array(t.proxy(renames["StateHistoryOut"])).optional(),
            "sparkRBatch": t.proxy(renames["SparkRBatchOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sparkBatch": t.proxy(renames["SparkBatchOut"]).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["GkeNodeConfigIn"] = t.struct(
        {
            "localSsdCount": t.integer().optional(),
            "accelerators": t.array(
                t.proxy(renames["GkeNodePoolAcceleratorConfigIn"])
            ).optional(),
            "machineType": t.string().optional(),
            "bootDiskKmsKey": t.string().optional(),
            "spot": t.boolean().optional(),
            "minCpuPlatform": t.string().optional(),
            "preemptible": t.boolean().optional(),
        }
    ).named(renames["GkeNodeConfigIn"])
    types["GkeNodeConfigOut"] = t.struct(
        {
            "localSsdCount": t.integer().optional(),
            "accelerators": t.array(
                t.proxy(renames["GkeNodePoolAcceleratorConfigOut"])
            ).optional(),
            "machineType": t.string().optional(),
            "bootDiskKmsKey": t.string().optional(),
            "spot": t.boolean().optional(),
            "minCpuPlatform": t.string().optional(),
            "preemptible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNodeConfigOut"])
    types["ClusterConfigIn"] = t.struct(
        {
            "workerConfig": t.proxy(renames["InstanceGroupConfigIn"]).optional(),
            "initializationActions": t.array(
                t.proxy(renames["NodeInitializationActionIn"])
            ).optional(),
            "metastoreConfig": t.proxy(renames["MetastoreConfigIn"]).optional(),
            "autoscalingConfig": t.proxy(renames["AutoscalingConfigIn"]).optional(),
            "securityConfig": t.proxy(renames["SecurityConfigIn"]).optional(),
            "lifecycleConfig": t.proxy(renames["LifecycleConfigIn"]).optional(),
            "tempBucket": t.string().optional(),
            "softwareConfig": t.proxy(renames["SoftwareConfigIn"]).optional(),
            "gceClusterConfig": t.proxy(renames["GceClusterConfigIn"]).optional(),
            "dataprocMetricConfig": t.proxy(
                renames["DataprocMetricConfigIn"]
            ).optional(),
            "masterConfig": t.proxy(renames["InstanceGroupConfigIn"]).optional(),
            "endpointConfig": t.proxy(renames["EndpointConfigIn"]).optional(),
            "configBucket": t.string().optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
            "secondaryWorkerConfig": t.proxy(
                renames["InstanceGroupConfigIn"]
            ).optional(),
            "gkeClusterConfig": t.proxy(renames["GkeClusterConfigIn"]).optional(),
            "auxiliaryNodeGroups": t.array(
                t.proxy(renames["AuxiliaryNodeGroupIn"])
            ).optional(),
        }
    ).named(renames["ClusterConfigIn"])
    types["ClusterConfigOut"] = t.struct(
        {
            "workerConfig": t.proxy(renames["InstanceGroupConfigOut"]).optional(),
            "initializationActions": t.array(
                t.proxy(renames["NodeInitializationActionOut"])
            ).optional(),
            "metastoreConfig": t.proxy(renames["MetastoreConfigOut"]).optional(),
            "autoscalingConfig": t.proxy(renames["AutoscalingConfigOut"]).optional(),
            "securityConfig": t.proxy(renames["SecurityConfigOut"]).optional(),
            "lifecycleConfig": t.proxy(renames["LifecycleConfigOut"]).optional(),
            "tempBucket": t.string().optional(),
            "softwareConfig": t.proxy(renames["SoftwareConfigOut"]).optional(),
            "gceClusterConfig": t.proxy(renames["GceClusterConfigOut"]).optional(),
            "dataprocMetricConfig": t.proxy(
                renames["DataprocMetricConfigOut"]
            ).optional(),
            "masterConfig": t.proxy(renames["InstanceGroupConfigOut"]).optional(),
            "endpointConfig": t.proxy(renames["EndpointConfigOut"]).optional(),
            "configBucket": t.string().optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "secondaryWorkerConfig": t.proxy(
                renames["InstanceGroupConfigOut"]
            ).optional(),
            "gkeClusterConfig": t.proxy(renames["GkeClusterConfigOut"]).optional(),
            "auxiliaryNodeGroups": t.array(
                t.proxy(renames["AuxiliaryNodeGroupOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterConfigOut"])
    types["VirtualClusterConfigIn"] = t.struct(
        {
            "kubernetesClusterConfig": t.proxy(renames["KubernetesClusterConfigIn"]),
            "stagingBucket": t.string().optional(),
            "auxiliaryServicesConfig": t.proxy(
                renames["AuxiliaryServicesConfigIn"]
            ).optional(),
        }
    ).named(renames["VirtualClusterConfigIn"])
    types["VirtualClusterConfigOut"] = t.struct(
        {
            "kubernetesClusterConfig": t.proxy(renames["KubernetesClusterConfigOut"]),
            "stagingBucket": t.string().optional(),
            "auxiliaryServicesConfig": t.proxy(
                renames["AuxiliaryServicesConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualClusterConfigOut"])
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
    types["SparkSqlBatchIn"] = t.struct(
        {
            "queryFileUri": t.string(),
            "queryVariables": t.struct({"_": t.string().optional()}).optional(),
            "jarFileUris": t.array(t.string()).optional(),
        }
    ).named(renames["SparkSqlBatchIn"])
    types["SparkSqlBatchOut"] = t.struct(
        {
            "queryFileUri": t.string(),
            "queryVariables": t.struct({"_": t.string().optional()}).optional(),
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ClusterOperationStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClusterOperationStatusIn"]
    )
    types["ClusterOperationStatusOut"] = t.struct(
        {
            "innerState": t.string().optional(),
            "state": t.string().optional(),
            "details": t.string().optional(),
            "stateStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOperationStatusOut"])
    types["ConfidentialInstanceConfigIn"] = t.struct(
        {"enableConfidentialCompute": t.boolean().optional()}
    ).named(renames["ConfidentialInstanceConfigIn"])
    types["ConfidentialInstanceConfigOut"] = t.struct(
        {
            "enableConfidentialCompute": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfidentialInstanceConfigOut"])
    types["BasicYarnAutoscalingConfigIn"] = t.struct(
        {
            "scaleUpFactor": t.number(),
            "scaleDownFactor": t.number(),
            "scaleUpMinWorkerFraction": t.number().optional(),
            "scaleDownMinWorkerFraction": t.number().optional(),
            "gracefulDecommissionTimeout": t.string(),
        }
    ).named(renames["BasicYarnAutoscalingConfigIn"])
    types["BasicYarnAutoscalingConfigOut"] = t.struct(
        {
            "scaleUpFactor": t.number(),
            "scaleDownFactor": t.number(),
            "scaleUpMinWorkerFraction": t.number().optional(),
            "scaleDownMinWorkerFraction": t.number().optional(),
            "gracefulDecommissionTimeout": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicYarnAutoscalingConfigOut"])
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
    types["InstantiateWorkflowTemplateRequestIn"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "requestId": t.string().optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["InstantiateWorkflowTemplateRequestIn"])
    types["InstantiateWorkflowTemplateRequestOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "requestId": t.string().optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstantiateWorkflowTemplateRequestOut"])
    types["InstanceGroupConfigIn"] = t.struct(
        {
            "preemptibility": t.string().optional(),
            "minCpuPlatform": t.string().optional(),
            "numInstances": t.integer().optional(),
            "imageUri": t.string().optional(),
            "diskConfig": t.proxy(renames["DiskConfigIn"]).optional(),
            "machineTypeUri": t.string().optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorConfigIn"])).optional(),
        }
    ).named(renames["InstanceGroupConfigIn"])
    types["InstanceGroupConfigOut"] = t.struct(
        {
            "preemptibility": t.string().optional(),
            "isPreemptible": t.boolean().optional(),
            "minCpuPlatform": t.string().optional(),
            "numInstances": t.integer().optional(),
            "instanceReferences": t.array(
                t.proxy(renames["InstanceReferenceOut"])
            ).optional(),
            "managedGroupConfig": t.proxy(renames["ManagedGroupConfigOut"]).optional(),
            "instanceNames": t.array(t.string()).optional(),
            "imageUri": t.string().optional(),
            "diskConfig": t.proxy(renames["DiskConfigOut"]).optional(),
            "machineTypeUri": t.string().optional(),
            "accelerators": t.array(
                t.proxy(renames["AcceleratorConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceGroupConfigOut"])
    types["MetastoreConfigIn"] = t.struct(
        {"dataprocMetastoreService": t.string()}
    ).named(renames["MetastoreConfigIn"])
    types["MetastoreConfigOut"] = t.struct(
        {
            "dataprocMetastoreService": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetastoreConfigOut"])
    types["KerberosConfigIn"] = t.struct(
        {
            "kdcDbKeyUri": t.string().optional(),
            "keystoreUri": t.string().optional(),
            "enableKerberos": t.boolean().optional(),
            "crossRealmTrustAdminServer": t.string().optional(),
            "keyPasswordUri": t.string().optional(),
            "rootPrincipalPasswordUri": t.string().optional(),
            "tgtLifetimeHours": t.integer().optional(),
            "truststorePasswordUri": t.string().optional(),
            "crossRealmTrustSharedPasswordUri": t.string().optional(),
            "crossRealmTrustRealm": t.string().optional(),
            "truststoreUri": t.string().optional(),
            "realm": t.string().optional(),
            "kmsKeyUri": t.string().optional(),
            "keystorePasswordUri": t.string().optional(),
            "crossRealmTrustKdc": t.string().optional(),
        }
    ).named(renames["KerberosConfigIn"])
    types["KerberosConfigOut"] = t.struct(
        {
            "kdcDbKeyUri": t.string().optional(),
            "keystoreUri": t.string().optional(),
            "enableKerberos": t.boolean().optional(),
            "crossRealmTrustAdminServer": t.string().optional(),
            "keyPasswordUri": t.string().optional(),
            "rootPrincipalPasswordUri": t.string().optional(),
            "tgtLifetimeHours": t.integer().optional(),
            "truststorePasswordUri": t.string().optional(),
            "crossRealmTrustSharedPasswordUri": t.string().optional(),
            "crossRealmTrustRealm": t.string().optional(),
            "truststoreUri": t.string().optional(),
            "realm": t.string().optional(),
            "kmsKeyUri": t.string().optional(),
            "keystorePasswordUri": t.string().optional(),
            "crossRealmTrustKdc": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KerberosConfigOut"])
    types["PySparkBatchIn"] = t.struct(
        {
            "jarFileUris": t.array(t.string()).optional(),
            "pythonFileUris": t.array(t.string()).optional(),
            "mainPythonFileUri": t.string(),
            "archiveUris": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
        }
    ).named(renames["PySparkBatchIn"])
    types["PySparkBatchOut"] = t.struct(
        {
            "jarFileUris": t.array(t.string()).optional(),
            "pythonFileUris": t.array(t.string()).optional(),
            "mainPythonFileUri": t.string(),
            "archiveUris": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PySparkBatchOut"])
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
    types["ManagedClusterIn"] = t.struct(
        {
            "clusterName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "config": t.proxy(renames["ClusterConfigIn"]),
        }
    ).named(renames["ManagedClusterIn"])
    types["ManagedClusterOut"] = t.struct(
        {
            "clusterName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "config": t.proxy(renames["ClusterConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedClusterOut"])
    types["SparkSqlJobIn"] = t.struct(
        {
            "jarFileUris": t.array(t.string()).optional(),
            "queryFileUri": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
        }
    ).named(renames["SparkSqlJobIn"])
    types["SparkSqlJobOut"] = t.struct(
        {
            "jarFileUris": t.array(t.string()).optional(),
            "queryFileUri": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkSqlJobOut"])
    types["WorkflowTemplateIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.array(t.proxy(renames["TemplateParameterIn"])).optional(),
            "version": t.integer().optional(),
            "placement": t.proxy(renames["WorkflowTemplatePlacementIn"]),
            "dagTimeout": t.string().optional(),
            "id": t.string(),
            "jobs": t.array(t.proxy(renames["OrderedJobIn"])),
        }
    ).named(renames["WorkflowTemplateIn"])
    types["WorkflowTemplateOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.array(t.proxy(renames["TemplateParameterOut"])).optional(),
            "updateTime": t.string().optional(),
            "version": t.integer().optional(),
            "createTime": t.string().optional(),
            "placement": t.proxy(renames["WorkflowTemplatePlacementOut"]),
            "dagTimeout": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string(),
            "jobs": t.array(t.proxy(renames["OrderedJobOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowTemplateOut"])
    types["QueryListIn"] = t.struct({"queries": t.array(t.string())}).named(
        renames["QueryListIn"]
    )
    types["QueryListOut"] = t.struct(
        {
            "queries": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryListOut"])
    types["PigJobIn"] = t.struct(
        {
            "continueOnFailure": t.boolean().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "queryFileUri": t.string().optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PigJobIn"])
    types["PigJobOut"] = t.struct(
        {
            "continueOnFailure": t.boolean().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "queryFileUri": t.string().optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PigJobOut"])
    types["CancelJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelJobRequestIn"]
    )
    types["CancelJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelJobRequestOut"])
    types["JobStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["JobStatusIn"]
    )
    types["JobStatusOut"] = t.struct(
        {
            "stateStartTime": t.string().optional(),
            "state": t.string().optional(),
            "details": t.string().optional(),
            "substate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatusOut"])
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
    types["PeripheralsConfigIn"] = t.struct(
        {
            "sparkHistoryServerConfig": t.proxy(
                renames["SparkHistoryServerConfigIn"]
            ).optional(),
            "metastoreService": t.string().optional(),
        }
    ).named(renames["PeripheralsConfigIn"])
    types["PeripheralsConfigOut"] = t.struct(
        {
            "sparkHistoryServerConfig": t.proxy(
                renames["SparkHistoryServerConfigOut"]
            ).optional(),
            "metastoreService": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PeripheralsConfigOut"])
    types["GkeNodePoolAcceleratorConfigIn"] = t.struct(
        {
            "acceleratorType": t.string().optional(),
            "gpuPartitionSize": t.string().optional(),
            "acceleratorCount": t.string().optional(),
        }
    ).named(renames["GkeNodePoolAcceleratorConfigIn"])
    types["GkeNodePoolAcceleratorConfigOut"] = t.struct(
        {
            "acceleratorType": t.string().optional(),
            "gpuPartitionSize": t.string().optional(),
            "acceleratorCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNodePoolAcceleratorConfigOut"])
    types["ClusterOperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClusterOperationMetadataIn"]
    )
    types["ClusterOperationMetadataOut"] = t.struct(
        {
            "clusterName": t.string().optional(),
            "statusHistory": t.array(
                t.proxy(renames["ClusterOperationStatusOut"])
            ).optional(),
            "operationType": t.string().optional(),
            "childOperationIds": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "clusterUuid": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "status": t.proxy(renames["ClusterOperationStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOperationMetadataOut"])
    types["GkeNodePoolTargetIn"] = t.struct(
        {
            "nodePool": t.string(),
            "nodePoolConfig": t.proxy(renames["GkeNodePoolConfigIn"]).optional(),
            "roles": t.array(t.string()),
        }
    ).named(renames["GkeNodePoolTargetIn"])
    types["GkeNodePoolTargetOut"] = t.struct(
        {
            "nodePool": t.string(),
            "nodePoolConfig": t.proxy(renames["GkeNodePoolConfigOut"]).optional(),
            "roles": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNodePoolTargetOut"])
    types["JobIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "hadoopJob": t.proxy(renames["HadoopJobIn"]).optional(),
            "sparkJob": t.proxy(renames["SparkJobIn"]).optional(),
            "placement": t.proxy(renames["JobPlacementIn"]),
            "driverSchedulingConfig": t.proxy(
                renames["DriverSchedulingConfigIn"]
            ).optional(),
            "reference": t.proxy(renames["JobReferenceIn"]).optional(),
            "scheduling": t.proxy(renames["JobSchedulingIn"]).optional(),
            "sparkRJob": t.proxy(renames["SparkRJobIn"]).optional(),
            "prestoJob": t.proxy(renames["PrestoJobIn"]).optional(),
            "sparkSqlJob": t.proxy(renames["SparkSqlJobIn"]).optional(),
            "pigJob": t.proxy(renames["PigJobIn"]).optional(),
            "trinoJob": t.proxy(renames["TrinoJobIn"]).optional(),
            "pysparkJob": t.proxy(renames["PySparkJobIn"]).optional(),
            "hiveJob": t.proxy(renames["HiveJobIn"]).optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "driverOutputResourceUri": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "hadoopJob": t.proxy(renames["HadoopJobOut"]).optional(),
            "sparkJob": t.proxy(renames["SparkJobOut"]).optional(),
            "placement": t.proxy(renames["JobPlacementOut"]),
            "yarnApplications": t.array(
                t.proxy(renames["YarnApplicationOut"])
            ).optional(),
            "driverSchedulingConfig": t.proxy(
                renames["DriverSchedulingConfigOut"]
            ).optional(),
            "jobUuid": t.string().optional(),
            "reference": t.proxy(renames["JobReferenceOut"]).optional(),
            "scheduling": t.proxy(renames["JobSchedulingOut"]).optional(),
            "sparkRJob": t.proxy(renames["SparkRJobOut"]).optional(),
            "prestoJob": t.proxy(renames["PrestoJobOut"]).optional(),
            "sparkSqlJob": t.proxy(renames["SparkSqlJobOut"]).optional(),
            "driverControlFilesUri": t.string().optional(),
            "done": t.boolean().optional(),
            "pigJob": t.proxy(renames["PigJobOut"]).optional(),
            "trinoJob": t.proxy(renames["TrinoJobOut"]).optional(),
            "pysparkJob": t.proxy(renames["PySparkJobOut"]).optional(),
            "status": t.proxy(renames["JobStatusOut"]).optional(),
            "statusHistory": t.array(t.proxy(renames["JobStatusOut"])).optional(),
            "hiveJob": t.proxy(renames["HiveJobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
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
    types["ClusterOperationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClusterOperationIn"]
    )
    types["ClusterOperationOut"] = t.struct(
        {
            "operationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["ClusterOperationOut"])
    types["GceClusterConfigIn"] = t.struct(
        {
            "confidentialInstanceConfig": t.proxy(
                renames["ConfidentialInstanceConfigIn"]
            ).optional(),
            "reservationAffinity": t.proxy(renames["ReservationAffinityIn"]).optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigIn"]
            ).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "networkUri": t.string().optional(),
            "subnetworkUri": t.string().optional(),
            "internalIpOnly": t.boolean().optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "zoneUri": t.string().optional(),
            "serviceAccountScopes": t.array(t.string()).optional(),
            "tags": t.array(t.string()).optional(),
            "nodeGroupAffinity": t.proxy(renames["NodeGroupAffinityIn"]).optional(),
        }
    ).named(renames["GceClusterConfigIn"])
    types["GceClusterConfigOut"] = t.struct(
        {
            "confidentialInstanceConfig": t.proxy(
                renames["ConfidentialInstanceConfigOut"]
            ).optional(),
            "reservationAffinity": t.proxy(
                renames["ReservationAffinityOut"]
            ).optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigOut"]
            ).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "networkUri": t.string().optional(),
            "subnetworkUri": t.string().optional(),
            "internalIpOnly": t.boolean().optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "zoneUri": t.string().optional(),
            "serviceAccountScopes": t.array(t.string()).optional(),
            "tags": t.array(t.string()).optional(),
            "nodeGroupAffinity": t.proxy(renames["NodeGroupAffinityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceClusterConfigOut"])
    types["AutoscalingPolicyIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "secondaryWorkerConfig": t.proxy(
                renames["InstanceGroupAutoscalingPolicyConfigIn"]
            ).optional(),
            "basicAlgorithm": t.proxy(renames["BasicAutoscalingAlgorithmIn"]),
            "id": t.string(),
            "workerConfig": t.proxy(renames["InstanceGroupAutoscalingPolicyConfigIn"]),
        }
    ).named(renames["AutoscalingPolicyIn"])
    types["AutoscalingPolicyOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "secondaryWorkerConfig": t.proxy(
                renames["InstanceGroupAutoscalingPolicyConfigOut"]
            ).optional(),
            "basicAlgorithm": t.proxy(renames["BasicAutoscalingAlgorithmOut"]),
            "id": t.string(),
            "workerConfig": t.proxy(renames["InstanceGroupAutoscalingPolicyConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoscalingPolicyOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["WorkflowNodeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WorkflowNodeIn"]
    )
    types["WorkflowNodeOut"] = t.struct(
        {
            "state": t.string().optional(),
            "jobId": t.string().optional(),
            "prerequisiteStepIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "stepId": t.string().optional(),
        }
    ).named(renames["WorkflowNodeOut"])
    types["BasicAutoscalingAlgorithmIn"] = t.struct(
        {
            "cooldownPeriod": t.string().optional(),
            "sparkStandaloneConfig": t.proxy(
                renames["SparkStandaloneAutoscalingConfigIn"]
            ).optional(),
            "yarnConfig": t.proxy(renames["BasicYarnAutoscalingConfigIn"]).optional(),
        }
    ).named(renames["BasicAutoscalingAlgorithmIn"])
    types["BasicAutoscalingAlgorithmOut"] = t.struct(
        {
            "cooldownPeriod": t.string().optional(),
            "sparkStandaloneConfig": t.proxy(
                renames["SparkStandaloneAutoscalingConfigOut"]
            ).optional(),
            "yarnConfig": t.proxy(renames["BasicYarnAutoscalingConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicAutoscalingAlgorithmOut"])
    types["PrestoJobIn"] = t.struct(
        {
            "clientTags": t.array(t.string()).optional(),
            "outputFormat": t.string().optional(),
            "continueOnFailure": t.boolean().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
            "queryFileUri": t.string().optional(),
        }
    ).named(renames["PrestoJobIn"])
    types["PrestoJobOut"] = t.struct(
        {
            "clientTags": t.array(t.string()).optional(),
            "outputFormat": t.string().optional(),
            "continueOnFailure": t.boolean().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "queryFileUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrestoJobOut"])
    types["StateHistoryIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StateHistoryIn"]
    )
    types["StateHistoryOut"] = t.struct(
        {
            "state": t.string().optional(),
            "stateStartTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StateHistoryOut"])
    types["NodePoolIn"] = t.struct(
        {
            "id": t.string(),
            "instanceNames": t.array(t.string()).optional(),
            "repairAction": t.string(),
        }
    ).named(renames["NodePoolIn"])
    types["NodePoolOut"] = t.struct(
        {
            "id": t.string(),
            "instanceNames": t.array(t.string()).optional(),
            "repairAction": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolOut"])
    types["NodeGroupIn"] = t.struct(
        {
            "name": t.string().optional(),
            "nodeGroupConfig": t.proxy(renames["InstanceGroupConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "roles": t.array(t.string()),
        }
    ).named(renames["NodeGroupIn"])
    types["NodeGroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "nodeGroupConfig": t.proxy(renames["InstanceGroupConfigOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "roles": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeGroupOut"])
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
    types["AuxiliaryServicesConfigIn"] = t.struct(
        {
            "sparkHistoryServerConfig": t.proxy(
                renames["SparkHistoryServerConfigIn"]
            ).optional(),
            "metastoreConfig": t.proxy(renames["MetastoreConfigIn"]).optional(),
        }
    ).named(renames["AuxiliaryServicesConfigIn"])
    types["AuxiliaryServicesConfigOut"] = t.struct(
        {
            "sparkHistoryServerConfig": t.proxy(
                renames["SparkHistoryServerConfigOut"]
            ).optional(),
            "metastoreConfig": t.proxy(renames["MetastoreConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuxiliaryServicesConfigOut"])
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
    types["DriverSchedulingConfigIn"] = t.struct(
        {"vcores": t.integer(), "memoryMb": t.integer()}
    ).named(renames["DriverSchedulingConfigIn"])
    types["DriverSchedulingConfigOut"] = t.struct(
        {
            "vcores": t.integer(),
            "memoryMb": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriverSchedulingConfigOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ExecutionConfigIn"] = t.struct(
        {
            "stagingBucket": t.string().optional(),
            "idleTtl": t.string().optional(),
            "kmsKey": t.string().optional(),
            "subnetworkUri": t.string().optional(),
            "networkUri": t.string().optional(),
            "ttl": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
        }
    ).named(renames["ExecutionConfigIn"])
    types["ExecutionConfigOut"] = t.struct(
        {
            "stagingBucket": t.string().optional(),
            "idleTtl": t.string().optional(),
            "kmsKey": t.string().optional(),
            "subnetworkUri": t.string().optional(),
            "networkUri": t.string().optional(),
            "ttl": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionConfigOut"])
    types["ListClustersResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListClustersResponseIn"]
    )
    types["ListClustersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "clusters": t.array(t.proxy(renames["ClusterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListClustersResponseOut"])
    types["AutoscalingConfigIn"] = t.struct({"policyUri": t.string().optional()}).named(
        renames["AutoscalingConfigIn"]
    )
    types["AutoscalingConfigOut"] = t.struct(
        {
            "policyUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoscalingConfigOut"])
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
    types["YarnApplicationIn"] = t.struct(
        {
            "trackingUrl": t.string().optional(),
            "state": t.string(),
            "progress": t.number(),
            "name": t.string(),
        }
    ).named(renames["YarnApplicationIn"])
    types["YarnApplicationOut"] = t.struct(
        {
            "trackingUrl": t.string().optional(),
            "state": t.string(),
            "progress": t.number(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YarnApplicationOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["RuntimeInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RuntimeInfoIn"]
    )
    types["RuntimeInfoOut"] = t.struct(
        {
            "diagnosticOutputUri": t.string().optional(),
            "currentUsage": t.proxy(renames["UsageSnapshotOut"]).optional(),
            "approximateUsage": t.proxy(renames["UsageMetricsOut"]).optional(),
            "outputUri": t.string().optional(),
            "endpoints": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeInfoOut"])
    types["PySparkJobIn"] = t.struct(
        {
            "pythonFileUris": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "args": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "mainPythonFileUri": t.string(),
        }
    ).named(renames["PySparkJobIn"])
    types["PySparkJobOut"] = t.struct(
        {
            "pythonFileUris": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "args": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "mainPythonFileUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PySparkJobOut"])
    types["DiagnoseClusterRequestIn"] = t.struct(
        {
            "jobs": t.array(t.string()).optional(),
            "diagnosisInterval": t.proxy(renames["IntervalIn"]).optional(),
            "job": t.string().optional(),
            "yarnApplicationIds": t.array(t.string()).optional(),
            "yarnApplicationId": t.string().optional(),
        }
    ).named(renames["DiagnoseClusterRequestIn"])
    types["DiagnoseClusterRequestOut"] = t.struct(
        {
            "jobs": t.array(t.string()).optional(),
            "diagnosisInterval": t.proxy(renames["IntervalOut"]).optional(),
            "job": t.string().optional(),
            "yarnApplicationIds": t.array(t.string()).optional(),
            "yarnApplicationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiagnoseClusterRequestOut"])
    types["DataprocMetricConfigIn"] = t.struct(
        {"metrics": t.array(t.proxy(renames["MetricIn"]))}
    ).named(renames["DataprocMetricConfigIn"])
    types["DataprocMetricConfigOut"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataprocMetricConfigOut"])
    types["ListWorkflowTemplatesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ListWorkflowTemplatesResponseIn"])
    types["ListWorkflowTemplatesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "templates": t.array(t.proxy(renames["WorkflowTemplateOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkflowTemplatesResponseOut"])
    types["BatchOperationMetadataIn"] = t.struct(
        {
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "operationType": t.string().optional(),
            "batchUuid": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "doneTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "batch": t.string().optional(),
        }
    ).named(renames["BatchOperationMetadataIn"])
    types["BatchOperationMetadataOut"] = t.struct(
        {
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "operationType": t.string().optional(),
            "batchUuid": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "doneTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "batch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchOperationMetadataOut"])
    types["RepairClusterRequestIn"] = t.struct(
        {
            "clusterUuid": t.string().optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolIn"])).optional(),
            "gracefulDecommissionTimeout": t.string().optional(),
            "parentOperationId": t.string().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["RepairClusterRequestIn"])
    types["RepairClusterRequestOut"] = t.struct(
        {
            "clusterUuid": t.string().optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolOut"])).optional(),
            "gracefulDecommissionTimeout": t.string().optional(),
            "parentOperationId": t.string().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepairClusterRequestOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
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
    types["HiveJobIn"] = t.struct(
        {
            "continueOnFailure": t.boolean().optional(),
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "queryFileUri": t.string().optional(),
            "jarFileUris": t.array(t.string()).optional(),
        }
    ).named(renames["HiveJobIn"])
    types["HiveJobOut"] = t.struct(
        {
            "continueOnFailure": t.boolean().optional(),
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "queryFileUri": t.string().optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HiveJobOut"])
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
    types["OrderedJobIn"] = t.struct(
        {
            "pysparkJob": t.proxy(renames["PySparkJobIn"]).optional(),
            "hiveJob": t.proxy(renames["HiveJobIn"]).optional(),
            "scheduling": t.proxy(renames["JobSchedulingIn"]).optional(),
            "sparkJob": t.proxy(renames["SparkJobIn"]).optional(),
            "sparkSqlJob": t.proxy(renames["SparkSqlJobIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "prerequisiteStepIds": t.array(t.string()).optional(),
            "sparkRJob": t.proxy(renames["SparkRJobIn"]).optional(),
            "stepId": t.string(),
            "pigJob": t.proxy(renames["PigJobIn"]).optional(),
            "trinoJob": t.proxy(renames["TrinoJobIn"]).optional(),
            "hadoopJob": t.proxy(renames["HadoopJobIn"]).optional(),
            "prestoJob": t.proxy(renames["PrestoJobIn"]).optional(),
        }
    ).named(renames["OrderedJobIn"])
    types["OrderedJobOut"] = t.struct(
        {
            "pysparkJob": t.proxy(renames["PySparkJobOut"]).optional(),
            "hiveJob": t.proxy(renames["HiveJobOut"]).optional(),
            "scheduling": t.proxy(renames["JobSchedulingOut"]).optional(),
            "sparkJob": t.proxy(renames["SparkJobOut"]).optional(),
            "sparkSqlJob": t.proxy(renames["SparkSqlJobOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "prerequisiteStepIds": t.array(t.string()).optional(),
            "sparkRJob": t.proxy(renames["SparkRJobOut"]).optional(),
            "stepId": t.string(),
            "pigJob": t.proxy(renames["PigJobOut"]).optional(),
            "trinoJob": t.proxy(renames["TrinoJobOut"]).optional(),
            "hadoopJob": t.proxy(renames["HadoopJobOut"]).optional(),
            "prestoJob": t.proxy(renames["PrestoJobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderedJobOut"])
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
    types["ClusterStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClusterStatusIn"]
    )
    types["ClusterStatusOut"] = t.struct(
        {
            "detail": t.string().optional(),
            "state": t.string().optional(),
            "substate": t.string().optional(),
            "stateStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterStatusOut"])
    types["SparkStandaloneAutoscalingConfigIn"] = t.struct(
        {
            "scaleDownMinWorkerFraction": t.number().optional(),
            "gracefulDecommissionTimeout": t.string(),
            "scaleUpFactor": t.number(),
            "scaleDownFactor": t.number(),
            "scaleUpMinWorkerFraction": t.number().optional(),
        }
    ).named(renames["SparkStandaloneAutoscalingConfigIn"])
    types["SparkStandaloneAutoscalingConfigOut"] = t.struct(
        {
            "scaleDownMinWorkerFraction": t.number().optional(),
            "gracefulDecommissionTimeout": t.string(),
            "scaleUpFactor": t.number(),
            "scaleDownFactor": t.number(),
            "scaleUpMinWorkerFraction": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkStandaloneAutoscalingConfigOut"])
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
    types["ReservationAffinityIn"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "consumeReservationType": t.string().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["ReservationAffinityIn"])
    types["ReservationAffinityOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "consumeReservationType": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReservationAffinityOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["LoggingConfigIn"] = t.struct(
        {"driverLogLevels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["LoggingConfigIn"])
    types["LoggingConfigOut"] = t.struct(
        {
            "driverLogLevels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingConfigOut"])
    types["SparkJobIn"] = t.struct(
        {
            "fileUris": t.array(t.string()).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "mainJarFileUri": t.string().optional(),
        }
    ).named(renames["SparkJobIn"])
    types["SparkJobOut"] = t.struct(
        {
            "fileUris": t.array(t.string()).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "mainJarFileUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkJobOut"])
    types["EnvironmentConfigIn"] = t.struct(
        {
            "executionConfig": t.proxy(renames["ExecutionConfigIn"]).optional(),
            "peripheralsConfig": t.proxy(renames["PeripheralsConfigIn"]).optional(),
        }
    ).named(renames["EnvironmentConfigIn"])
    types["EnvironmentConfigOut"] = t.struct(
        {
            "executionConfig": t.proxy(renames["ExecutionConfigOut"]).optional(),
            "peripheralsConfig": t.proxy(renames["PeripheralsConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentConfigOut"])
    types["RegexValidationIn"] = t.struct({"regexes": t.array(t.string())}).named(
        renames["RegexValidationIn"]
    )
    types["RegexValidationOut"] = t.struct(
        {
            "regexes": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegexValidationOut"])
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
    types["SparkRJobIn"] = t.struct(
        {
            "archiveUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "fileUris": t.array(t.string()).optional(),
            "mainRFileUri": t.string(),
        }
    ).named(renames["SparkRJobIn"])
    types["SparkRJobOut"] = t.struct(
        {
            "archiveUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "fileUris": t.array(t.string()).optional(),
            "mainRFileUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkRJobOut"])
    types["ClusterIn"] = t.struct(
        {
            "config": t.proxy(renames["ClusterConfigIn"]).optional(),
            "virtualClusterConfig": t.proxy(
                renames["VirtualClusterConfigIn"]
            ).optional(),
            "clusterName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "projectId": t.string(),
        }
    ).named(renames["ClusterIn"])
    types["ClusterOut"] = t.struct(
        {
            "statusHistory": t.array(t.proxy(renames["ClusterStatusOut"])).optional(),
            "config": t.proxy(renames["ClusterConfigOut"]).optional(),
            "virtualClusterConfig": t.proxy(
                renames["VirtualClusterConfigOut"]
            ).optional(),
            "metrics": t.proxy(renames["ClusterMetricsOut"]).optional(),
            "status": t.proxy(renames["ClusterStatusOut"]).optional(),
            "clusterName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "projectId": t.string(),
            "clusterUuid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOut"])
    types["SparkHistoryServerConfigIn"] = t.struct(
        {"dataprocCluster": t.string().optional()}
    ).named(renames["SparkHistoryServerConfigIn"])
    types["SparkHistoryServerConfigOut"] = t.struct(
        {
            "dataprocCluster": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkHistoryServerConfigOut"])
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
    types["IdentityConfigIn"] = t.struct(
        {"userServiceAccountMapping": t.struct({"_": t.string().optional()})}
    ).named(renames["IdentityConfigIn"])
    types["IdentityConfigOut"] = t.struct(
        {
            "userServiceAccountMapping": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityConfigOut"])
    types["NodeGroupAffinityIn"] = t.struct({"nodeGroupUri": t.string()}).named(
        renames["NodeGroupAffinityIn"]
    )
    types["NodeGroupAffinityOut"] = t.struct(
        {
            "nodeGroupUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeGroupAffinityOut"])
    types["ShieldedInstanceConfigIn"] = t.struct(
        {
            "enableSecureBoot": t.boolean().optional(),
            "enableIntegrityMonitoring": t.boolean().optional(),
            "enableVtpm": t.boolean().optional(),
        }
    ).named(renames["ShieldedInstanceConfigIn"])
    types["ShieldedInstanceConfigOut"] = t.struct(
        {
            "enableSecureBoot": t.boolean().optional(),
            "enableIntegrityMonitoring": t.boolean().optional(),
            "enableVtpm": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShieldedInstanceConfigOut"])
    types["NodeGroupOperationMetadataIn"] = t.struct(
        {"operationType": t.string().optional()}
    ).named(renames["NodeGroupOperationMetadataIn"])
    types["NodeGroupOperationMetadataOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "statusHistory": t.array(
                t.proxy(renames["ClusterOperationStatusOut"])
            ).optional(),
            "clusterUuid": t.string().optional(),
            "nodeGroupId": t.string().optional(),
            "status": t.proxy(renames["ClusterOperationStatusOut"]).optional(),
            "warnings": t.array(t.string()).optional(),
            "operationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeGroupOperationMetadataOut"])
    types["SparkRBatchIn"] = t.struct(
        {
            "mainRFileUri": t.string(),
            "fileUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
        }
    ).named(renames["SparkRBatchIn"])
    types["SparkRBatchOut"] = t.struct(
        {
            "mainRFileUri": t.string(),
            "fileUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkRBatchOut"])
    types["JobPlacementIn"] = t.struct(
        {
            "clusterName": t.string(),
            "clusterLabels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["JobPlacementIn"])
    types["JobPlacementOut"] = t.struct(
        {
            "clusterName": t.string(),
            "clusterUuid": t.string().optional(),
            "clusterLabels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobPlacementOut"])
    types["LifecycleConfigIn"] = t.struct(
        {
            "autoDeleteTime": t.string().optional(),
            "idleDeleteTtl": t.string().optional(),
            "autoDeleteTtl": t.string().optional(),
        }
    ).named(renames["LifecycleConfigIn"])
    types["LifecycleConfigOut"] = t.struct(
        {
            "idleStartTime": t.string().optional(),
            "autoDeleteTime": t.string().optional(),
            "idleDeleteTtl": t.string().optional(),
            "autoDeleteTtl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LifecycleConfigOut"])
    types["TrinoJobIn"] = t.struct(
        {
            "clientTags": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "queryFileUri": t.string().optional(),
            "outputFormat": t.string().optional(),
            "continueOnFailure": t.boolean().optional(),
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
        }
    ).named(renames["TrinoJobIn"])
    types["TrinoJobOut"] = t.struct(
        {
            "clientTags": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "queryFileUri": t.string().optional(),
            "outputFormat": t.string().optional(),
            "continueOnFailure": t.boolean().optional(),
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrinoJobOut"])

    functions = {}
    functions["projectsLocationsBatchesGet"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsLocationsAutoscalingPoliciesGet"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAutoscalingPoliciesSetIamPolicy"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAutoscalingPoliciesCreate"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAutoscalingPoliciesList"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAutoscalingPoliciesTestIamPermissions"
    ] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAutoscalingPoliciesUpdate"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAutoscalingPoliciesGetIamPolicy"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAutoscalingPoliciesDelete"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesDelete"] = dataproc.get(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesSetIamPolicy"] = dataproc.get(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesGet"] = dataproc.get(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesUpdate"] = dataproc.get(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesGetIamPolicy"] = dataproc.get(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesTestIamPermissions"] = dataproc.get(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesCreate"] = dataproc.get(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesInstantiate"] = dataproc.get(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesInstantiateInline"] = dataproc.get(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesList"] = dataproc.get(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesGet"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesList"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesCreate"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesGetIamPolicy"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesUpdate"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesTestIamPermissions"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesSetIamPolicy"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsAutoscalingPoliciesDelete"] = dataproc.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsRegionsJobsSubmitAsOperation"] = dataproc.post(
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
    functions["projectsRegionsJobsGetIamPolicy"] = dataproc.post(
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
    functions["projectsRegionsJobsSubmit"] = dataproc.post(
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
    functions["projectsRegionsJobsSetIamPolicy"] = dataproc.post(
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
    functions["projectsRegionsJobsGet"] = dataproc.post(
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
    functions["projectsRegionsJobsCancel"] = dataproc.post(
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
    functions["projectsRegionsJobsPatch"] = dataproc.post(
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
    functions["projectsRegionsJobsList"] = dataproc.post(
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
    functions["projectsRegionsJobsDelete"] = dataproc.post(
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
    functions["projectsRegionsJobsTestIamPermissions"] = dataproc.post(
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
    functions["projectsRegionsClustersTestIamPermissions"] = dataproc.get(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}",
        t.struct(
            {
                "region": t.string(),
                "projectId": t.string(),
                "clusterName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersRepair"] = dataproc.get(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}",
        t.struct(
            {
                "region": t.string(),
                "projectId": t.string(),
                "clusterName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersDiagnose"] = dataproc.get(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}",
        t.struct(
            {
                "region": t.string(),
                "projectId": t.string(),
                "clusterName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersCreate"] = dataproc.get(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}",
        t.struct(
            {
                "region": t.string(),
                "projectId": t.string(),
                "clusterName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersList"] = dataproc.get(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}",
        t.struct(
            {
                "region": t.string(),
                "projectId": t.string(),
                "clusterName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersSetIamPolicy"] = dataproc.get(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}",
        t.struct(
            {
                "region": t.string(),
                "projectId": t.string(),
                "clusterName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersDelete"] = dataproc.get(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}",
        t.struct(
            {
                "region": t.string(),
                "projectId": t.string(),
                "clusterName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersGetIamPolicy"] = dataproc.get(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}",
        t.struct(
            {
                "region": t.string(),
                "projectId": t.string(),
                "clusterName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersStop"] = dataproc.get(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}",
        t.struct(
            {
                "region": t.string(),
                "projectId": t.string(),
                "clusterName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersInjectCredentials"] = dataproc.get(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}",
        t.struct(
            {
                "region": t.string(),
                "projectId": t.string(),
                "clusterName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersPatch"] = dataproc.get(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}",
        t.struct(
            {
                "region": t.string(),
                "projectId": t.string(),
                "clusterName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersStart"] = dataproc.get(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}",
        t.struct(
            {
                "region": t.string(),
                "projectId": t.string(),
                "clusterName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersGet"] = dataproc.get(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}",
        t.struct(
            {
                "region": t.string(),
                "projectId": t.string(),
                "clusterName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersNodeGroupsCreate"] = dataproc.post(
        "v1/{name}:resize",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "size": t.integer(),
                "gracefulDecommissionTimeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersNodeGroupsGet"] = dataproc.post(
        "v1/{name}:resize",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "size": t.integer(),
                "gracefulDecommissionTimeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersNodeGroupsResize"] = dataproc.post(
        "v1/{name}:resize",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "size": t.integer(),
                "gracefulDecommissionTimeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="dataproc", renames=renames, types=Box(types), functions=Box(functions)
    )
