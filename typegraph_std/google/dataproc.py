from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_dataproc():
    dataproc = HTTPRuntime("https://dataproc.googleapis.com/")

    renames = {
        "ErrorResponse": "_dataproc_1_ErrorResponse",
        "WorkflowTemplatePlacementIn": "_dataproc_2_WorkflowTemplatePlacementIn",
        "WorkflowTemplatePlacementOut": "_dataproc_3_WorkflowTemplatePlacementOut",
        "RegexValidationIn": "_dataproc_4_RegexValidationIn",
        "RegexValidationOut": "_dataproc_5_RegexValidationOut",
        "ParameterValidationIn": "_dataproc_6_ParameterValidationIn",
        "ParameterValidationOut": "_dataproc_7_ParameterValidationOut",
        "YarnApplicationIn": "_dataproc_8_YarnApplicationIn",
        "YarnApplicationOut": "_dataproc_9_YarnApplicationOut",
        "WorkflowNodeIn": "_dataproc_10_WorkflowNodeIn",
        "WorkflowNodeOut": "_dataproc_11_WorkflowNodeOut",
        "GceClusterConfigIn": "_dataproc_12_GceClusterConfigIn",
        "GceClusterConfigOut": "_dataproc_13_GceClusterConfigOut",
        "ListOperationsResponseIn": "_dataproc_14_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_dataproc_15_ListOperationsResponseOut",
        "VirtualClusterConfigIn": "_dataproc_16_VirtualClusterConfigIn",
        "VirtualClusterConfigOut": "_dataproc_17_VirtualClusterConfigOut",
        "GkeNodePoolConfigIn": "_dataproc_18_GkeNodePoolConfigIn",
        "GkeNodePoolConfigOut": "_dataproc_19_GkeNodePoolConfigOut",
        "NodeGroupAffinityIn": "_dataproc_20_NodeGroupAffinityIn",
        "NodeGroupAffinityOut": "_dataproc_21_NodeGroupAffinityOut",
        "ManagedClusterIn": "_dataproc_22_ManagedClusterIn",
        "ManagedClusterOut": "_dataproc_23_ManagedClusterOut",
        "ClusterSelectorIn": "_dataproc_24_ClusterSelectorIn",
        "ClusterSelectorOut": "_dataproc_25_ClusterSelectorOut",
        "StopClusterRequestIn": "_dataproc_26_StopClusterRequestIn",
        "StopClusterRequestOut": "_dataproc_27_StopClusterRequestOut",
        "TrinoJobIn": "_dataproc_28_TrinoJobIn",
        "TrinoJobOut": "_dataproc_29_TrinoJobOut",
        "BindingIn": "_dataproc_30_BindingIn",
        "BindingOut": "_dataproc_31_BindingOut",
        "ClusterOperationStatusIn": "_dataproc_32_ClusterOperationStatusIn",
        "ClusterOperationStatusOut": "_dataproc_33_ClusterOperationStatusOut",
        "SubmitJobRequestIn": "_dataproc_34_SubmitJobRequestIn",
        "SubmitJobRequestOut": "_dataproc_35_SubmitJobRequestOut",
        "PrestoJobIn": "_dataproc_36_PrestoJobIn",
        "PrestoJobOut": "_dataproc_37_PrestoJobOut",
        "TestIamPermissionsRequestIn": "_dataproc_38_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_dataproc_39_TestIamPermissionsRequestOut",
        "AutoscalingPolicyIn": "_dataproc_40_AutoscalingPolicyIn",
        "AutoscalingPolicyOut": "_dataproc_41_AutoscalingPolicyOut",
        "OperationIn": "_dataproc_42_OperationIn",
        "OperationOut": "_dataproc_43_OperationOut",
        "SparkStandaloneAutoscalingConfigIn": "_dataproc_44_SparkStandaloneAutoscalingConfigIn",
        "SparkStandaloneAutoscalingConfigOut": "_dataproc_45_SparkStandaloneAutoscalingConfigOut",
        "SparkRJobIn": "_dataproc_46_SparkRJobIn",
        "SparkRJobOut": "_dataproc_47_SparkRJobOut",
        "ShieldedInstanceConfigIn": "_dataproc_48_ShieldedInstanceConfigIn",
        "ShieldedInstanceConfigOut": "_dataproc_49_ShieldedInstanceConfigOut",
        "DiskConfigIn": "_dataproc_50_DiskConfigIn",
        "DiskConfigOut": "_dataproc_51_DiskConfigOut",
        "DiagnoseClusterRequestIn": "_dataproc_52_DiagnoseClusterRequestIn",
        "DiagnoseClusterRequestOut": "_dataproc_53_DiagnoseClusterRequestOut",
        "EndpointConfigIn": "_dataproc_54_EndpointConfigIn",
        "EndpointConfigOut": "_dataproc_55_EndpointConfigOut",
        "MetricIn": "_dataproc_56_MetricIn",
        "MetricOut": "_dataproc_57_MetricOut",
        "HiveJobIn": "_dataproc_58_HiveJobIn",
        "HiveJobOut": "_dataproc_59_HiveJobOut",
        "EncryptionConfigIn": "_dataproc_60_EncryptionConfigIn",
        "EncryptionConfigOut": "_dataproc_61_EncryptionConfigOut",
        "AuxiliaryNodeGroupIn": "_dataproc_62_AuxiliaryNodeGroupIn",
        "AuxiliaryNodeGroupOut": "_dataproc_63_AuxiliaryNodeGroupOut",
        "SparkBatchIn": "_dataproc_64_SparkBatchIn",
        "SparkBatchOut": "_dataproc_65_SparkBatchOut",
        "JobIn": "_dataproc_66_JobIn",
        "JobOut": "_dataproc_67_JobOut",
        "SparkJobIn": "_dataproc_68_SparkJobIn",
        "SparkJobOut": "_dataproc_69_SparkJobOut",
        "SetIamPolicyRequestIn": "_dataproc_70_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_dataproc_71_SetIamPolicyRequestOut",
        "PySparkBatchIn": "_dataproc_72_PySparkBatchIn",
        "PySparkBatchOut": "_dataproc_73_PySparkBatchOut",
        "KubernetesClusterConfigIn": "_dataproc_74_KubernetesClusterConfigIn",
        "KubernetesClusterConfigOut": "_dataproc_75_KubernetesClusterConfigOut",
        "ClusterOperationIn": "_dataproc_76_ClusterOperationIn",
        "ClusterOperationOut": "_dataproc_77_ClusterOperationOut",
        "NodeInitializationActionIn": "_dataproc_78_NodeInitializationActionIn",
        "NodeInitializationActionOut": "_dataproc_79_NodeInitializationActionOut",
        "ClusterStatusIn": "_dataproc_80_ClusterStatusIn",
        "ClusterStatusOut": "_dataproc_81_ClusterStatusOut",
        "PolicyIn": "_dataproc_82_PolicyIn",
        "PolicyOut": "_dataproc_83_PolicyOut",
        "CancelJobRequestIn": "_dataproc_84_CancelJobRequestIn",
        "CancelJobRequestOut": "_dataproc_85_CancelJobRequestOut",
        "InjectCredentialsRequestIn": "_dataproc_86_InjectCredentialsRequestIn",
        "InjectCredentialsRequestOut": "_dataproc_87_InjectCredentialsRequestOut",
        "ValueValidationIn": "_dataproc_88_ValueValidationIn",
        "ValueValidationOut": "_dataproc_89_ValueValidationOut",
        "JobStatusIn": "_dataproc_90_JobStatusIn",
        "JobStatusOut": "_dataproc_91_JobStatusOut",
        "UsageMetricsIn": "_dataproc_92_UsageMetricsIn",
        "UsageMetricsOut": "_dataproc_93_UsageMetricsOut",
        "QueryListIn": "_dataproc_94_QueryListIn",
        "QueryListOut": "_dataproc_95_QueryListOut",
        "PigJobIn": "_dataproc_96_PigJobIn",
        "PigJobOut": "_dataproc_97_PigJobOut",
        "AcceleratorConfigIn": "_dataproc_98_AcceleratorConfigIn",
        "AcceleratorConfigOut": "_dataproc_99_AcceleratorConfigOut",
        "StateHistoryIn": "_dataproc_100_StateHistoryIn",
        "StateHistoryOut": "_dataproc_101_StateHistoryOut",
        "WorkflowMetadataIn": "_dataproc_102_WorkflowMetadataIn",
        "WorkflowMetadataOut": "_dataproc_103_WorkflowMetadataOut",
        "EmptyIn": "_dataproc_104_EmptyIn",
        "EmptyOut": "_dataproc_105_EmptyOut",
        "DataprocMetricConfigIn": "_dataproc_106_DataprocMetricConfigIn",
        "DataprocMetricConfigOut": "_dataproc_107_DataprocMetricConfigOut",
        "IntervalIn": "_dataproc_108_IntervalIn",
        "IntervalOut": "_dataproc_109_IntervalOut",
        "ExecutionConfigIn": "_dataproc_110_ExecutionConfigIn",
        "ExecutionConfigOut": "_dataproc_111_ExecutionConfigOut",
        "ReservationAffinityIn": "_dataproc_112_ReservationAffinityIn",
        "ReservationAffinityOut": "_dataproc_113_ReservationAffinityOut",
        "RepairClusterRequestIn": "_dataproc_114_RepairClusterRequestIn",
        "RepairClusterRequestOut": "_dataproc_115_RepairClusterRequestOut",
        "SoftwareConfigIn": "_dataproc_116_SoftwareConfigIn",
        "SoftwareConfigOut": "_dataproc_117_SoftwareConfigOut",
        "ClusterConfigIn": "_dataproc_118_ClusterConfigIn",
        "ClusterConfigOut": "_dataproc_119_ClusterConfigOut",
        "AutoscalingConfigIn": "_dataproc_120_AutoscalingConfigIn",
        "AutoscalingConfigOut": "_dataproc_121_AutoscalingConfigOut",
        "ConfidentialInstanceConfigIn": "_dataproc_122_ConfidentialInstanceConfigIn",
        "ConfidentialInstanceConfigOut": "_dataproc_123_ConfidentialInstanceConfigOut",
        "WorkflowGraphIn": "_dataproc_124_WorkflowGraphIn",
        "WorkflowGraphOut": "_dataproc_125_WorkflowGraphOut",
        "UsageSnapshotIn": "_dataproc_126_UsageSnapshotIn",
        "UsageSnapshotOut": "_dataproc_127_UsageSnapshotOut",
        "LifecycleConfigIn": "_dataproc_128_LifecycleConfigIn",
        "LifecycleConfigOut": "_dataproc_129_LifecycleConfigOut",
        "InstantiateWorkflowTemplateRequestIn": "_dataproc_130_InstantiateWorkflowTemplateRequestIn",
        "InstantiateWorkflowTemplateRequestOut": "_dataproc_131_InstantiateWorkflowTemplateRequestOut",
        "ClusterIn": "_dataproc_132_ClusterIn",
        "ClusterOut": "_dataproc_133_ClusterOut",
        "InstanceGroupAutoscalingPolicyConfigIn": "_dataproc_134_InstanceGroupAutoscalingPolicyConfigIn",
        "InstanceGroupAutoscalingPolicyConfigOut": "_dataproc_135_InstanceGroupAutoscalingPolicyConfigOut",
        "ResizeNodeGroupRequestIn": "_dataproc_136_ResizeNodeGroupRequestIn",
        "ResizeNodeGroupRequestOut": "_dataproc_137_ResizeNodeGroupRequestOut",
        "StartClusterRequestIn": "_dataproc_138_StartClusterRequestIn",
        "StartClusterRequestOut": "_dataproc_139_StartClusterRequestOut",
        "GkeNodePoolTargetIn": "_dataproc_140_GkeNodePoolTargetIn",
        "GkeNodePoolTargetOut": "_dataproc_141_GkeNodePoolTargetOut",
        "GkeNodePoolAutoscalingConfigIn": "_dataproc_142_GkeNodePoolAutoscalingConfigIn",
        "GkeNodePoolAutoscalingConfigOut": "_dataproc_143_GkeNodePoolAutoscalingConfigOut",
        "NodePoolIn": "_dataproc_144_NodePoolIn",
        "NodePoolOut": "_dataproc_145_NodePoolOut",
        "HadoopJobIn": "_dataproc_146_HadoopJobIn",
        "HadoopJobOut": "_dataproc_147_HadoopJobOut",
        "KerberosConfigIn": "_dataproc_148_KerberosConfigIn",
        "KerberosConfigOut": "_dataproc_149_KerberosConfigOut",
        "BasicAutoscalingAlgorithmIn": "_dataproc_150_BasicAutoscalingAlgorithmIn",
        "BasicAutoscalingAlgorithmOut": "_dataproc_151_BasicAutoscalingAlgorithmOut",
        "ListAutoscalingPoliciesResponseIn": "_dataproc_152_ListAutoscalingPoliciesResponseIn",
        "ListAutoscalingPoliciesResponseOut": "_dataproc_153_ListAutoscalingPoliciesResponseOut",
        "SparkRBatchIn": "_dataproc_154_SparkRBatchIn",
        "SparkRBatchOut": "_dataproc_155_SparkRBatchOut",
        "BatchOperationMetadataIn": "_dataproc_156_BatchOperationMetadataIn",
        "BatchOperationMetadataOut": "_dataproc_157_BatchOperationMetadataOut",
        "PySparkJobIn": "_dataproc_158_PySparkJobIn",
        "PySparkJobOut": "_dataproc_159_PySparkJobOut",
        "GkeNodePoolAcceleratorConfigIn": "_dataproc_160_GkeNodePoolAcceleratorConfigIn",
        "GkeNodePoolAcceleratorConfigOut": "_dataproc_161_GkeNodePoolAcceleratorConfigOut",
        "WorkflowTemplateIn": "_dataproc_162_WorkflowTemplateIn",
        "WorkflowTemplateOut": "_dataproc_163_WorkflowTemplateOut",
        "GkeClusterConfigIn": "_dataproc_164_GkeClusterConfigIn",
        "GkeClusterConfigOut": "_dataproc_165_GkeClusterConfigOut",
        "StatusIn": "_dataproc_166_StatusIn",
        "StatusOut": "_dataproc_167_StatusOut",
        "TemplateParameterIn": "_dataproc_168_TemplateParameterIn",
        "TemplateParameterOut": "_dataproc_169_TemplateParameterOut",
        "PeripheralsConfigIn": "_dataproc_170_PeripheralsConfigIn",
        "PeripheralsConfigOut": "_dataproc_171_PeripheralsConfigOut",
        "ListClustersResponseIn": "_dataproc_172_ListClustersResponseIn",
        "ListClustersResponseOut": "_dataproc_173_ListClustersResponseOut",
        "DriverSchedulingConfigIn": "_dataproc_174_DriverSchedulingConfigIn",
        "DriverSchedulingConfigOut": "_dataproc_175_DriverSchedulingConfigOut",
        "OrderedJobIn": "_dataproc_176_OrderedJobIn",
        "OrderedJobOut": "_dataproc_177_OrderedJobOut",
        "GetIamPolicyRequestIn": "_dataproc_178_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_dataproc_179_GetIamPolicyRequestOut",
        "InstanceGroupConfigIn": "_dataproc_180_InstanceGroupConfigIn",
        "InstanceGroupConfigOut": "_dataproc_181_InstanceGroupConfigOut",
        "ClusterOperationMetadataIn": "_dataproc_182_ClusterOperationMetadataIn",
        "ClusterOperationMetadataOut": "_dataproc_183_ClusterOperationMetadataOut",
        "SparkSqlBatchIn": "_dataproc_184_SparkSqlBatchIn",
        "SparkSqlBatchOut": "_dataproc_185_SparkSqlBatchOut",
        "SparkSqlJobIn": "_dataproc_186_SparkSqlJobIn",
        "SparkSqlJobOut": "_dataproc_187_SparkSqlJobOut",
        "SessionOperationMetadataIn": "_dataproc_188_SessionOperationMetadataIn",
        "SessionOperationMetadataOut": "_dataproc_189_SessionOperationMetadataOut",
        "JobMetadataIn": "_dataproc_190_JobMetadataIn",
        "JobMetadataOut": "_dataproc_191_JobMetadataOut",
        "TestIamPermissionsResponseIn": "_dataproc_192_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_dataproc_193_TestIamPermissionsResponseOut",
        "ListBatchesResponseIn": "_dataproc_194_ListBatchesResponseIn",
        "ListBatchesResponseOut": "_dataproc_195_ListBatchesResponseOut",
        "BasicYarnAutoscalingConfigIn": "_dataproc_196_BasicYarnAutoscalingConfigIn",
        "BasicYarnAutoscalingConfigOut": "_dataproc_197_BasicYarnAutoscalingConfigOut",
        "EnvironmentConfigIn": "_dataproc_198_EnvironmentConfigIn",
        "EnvironmentConfigOut": "_dataproc_199_EnvironmentConfigOut",
        "SparkHistoryServerConfigIn": "_dataproc_200_SparkHistoryServerConfigIn",
        "SparkHistoryServerConfigOut": "_dataproc_201_SparkHistoryServerConfigOut",
        "BatchIn": "_dataproc_202_BatchIn",
        "BatchOut": "_dataproc_203_BatchOut",
        "JobReferenceIn": "_dataproc_204_JobReferenceIn",
        "JobReferenceOut": "_dataproc_205_JobReferenceOut",
        "LoggingConfigIn": "_dataproc_206_LoggingConfigIn",
        "LoggingConfigOut": "_dataproc_207_LoggingConfigOut",
        "InstanceReferenceIn": "_dataproc_208_InstanceReferenceIn",
        "InstanceReferenceOut": "_dataproc_209_InstanceReferenceOut",
        "RuntimeConfigIn": "_dataproc_210_RuntimeConfigIn",
        "RuntimeConfigOut": "_dataproc_211_RuntimeConfigOut",
        "JobPlacementIn": "_dataproc_212_JobPlacementIn",
        "JobPlacementOut": "_dataproc_213_JobPlacementOut",
        "ExprIn": "_dataproc_214_ExprIn",
        "ExprOut": "_dataproc_215_ExprOut",
        "ManagedGroupConfigIn": "_dataproc_216_ManagedGroupConfigIn",
        "ManagedGroupConfigOut": "_dataproc_217_ManagedGroupConfigOut",
        "KubernetesSoftwareConfigIn": "_dataproc_218_KubernetesSoftwareConfigIn",
        "KubernetesSoftwareConfigOut": "_dataproc_219_KubernetesSoftwareConfigOut",
        "DiagnoseClusterResultsIn": "_dataproc_220_DiagnoseClusterResultsIn",
        "DiagnoseClusterResultsOut": "_dataproc_221_DiagnoseClusterResultsOut",
        "GkeNodeConfigIn": "_dataproc_222_GkeNodeConfigIn",
        "GkeNodeConfigOut": "_dataproc_223_GkeNodeConfigOut",
        "NodeGroupOperationMetadataIn": "_dataproc_224_NodeGroupOperationMetadataIn",
        "NodeGroupOperationMetadataOut": "_dataproc_225_NodeGroupOperationMetadataOut",
        "AuxiliaryServicesConfigIn": "_dataproc_226_AuxiliaryServicesConfigIn",
        "AuxiliaryServicesConfigOut": "_dataproc_227_AuxiliaryServicesConfigOut",
        "JobSchedulingIn": "_dataproc_228_JobSchedulingIn",
        "JobSchedulingOut": "_dataproc_229_JobSchedulingOut",
        "RuntimeInfoIn": "_dataproc_230_RuntimeInfoIn",
        "RuntimeInfoOut": "_dataproc_231_RuntimeInfoOut",
        "GetPolicyOptionsIn": "_dataproc_232_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_dataproc_233_GetPolicyOptionsOut",
        "SecurityConfigIn": "_dataproc_234_SecurityConfigIn",
        "SecurityConfigOut": "_dataproc_235_SecurityConfigOut",
        "NamespacedGkeDeploymentTargetIn": "_dataproc_236_NamespacedGkeDeploymentTargetIn",
        "NamespacedGkeDeploymentTargetOut": "_dataproc_237_NamespacedGkeDeploymentTargetOut",
        "ListJobsResponseIn": "_dataproc_238_ListJobsResponseIn",
        "ListJobsResponseOut": "_dataproc_239_ListJobsResponseOut",
        "ListWorkflowTemplatesResponseIn": "_dataproc_240_ListWorkflowTemplatesResponseIn",
        "ListWorkflowTemplatesResponseOut": "_dataproc_241_ListWorkflowTemplatesResponseOut",
        "MetastoreConfigIn": "_dataproc_242_MetastoreConfigIn",
        "MetastoreConfigOut": "_dataproc_243_MetastoreConfigOut",
        "ClusterMetricsIn": "_dataproc_244_ClusterMetricsIn",
        "ClusterMetricsOut": "_dataproc_245_ClusterMetricsOut",
        "NodeGroupIn": "_dataproc_246_NodeGroupIn",
        "NodeGroupOut": "_dataproc_247_NodeGroupOut",
        "IdentityConfigIn": "_dataproc_248_IdentityConfigIn",
        "IdentityConfigOut": "_dataproc_249_IdentityConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["RegexValidationIn"] = t.struct({"regexes": t.array(t.string())}).named(
        renames["RegexValidationIn"]
    )
    types["RegexValidationOut"] = t.struct(
        {
            "regexes": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegexValidationOut"])
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
    types["YarnApplicationIn"] = t.struct(
        {
            "name": t.string(),
            "progress": t.number(),
            "trackingUrl": t.string().optional(),
            "state": t.string(),
        }
    ).named(renames["YarnApplicationIn"])
    types["YarnApplicationOut"] = t.struct(
        {
            "name": t.string(),
            "progress": t.number(),
            "trackingUrl": t.string().optional(),
            "state": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YarnApplicationOut"])
    types["WorkflowNodeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WorkflowNodeIn"]
    )
    types["WorkflowNodeOut"] = t.struct(
        {
            "stepId": t.string().optional(),
            "state": t.string().optional(),
            "jobId": t.string().optional(),
            "prerequisiteStepIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowNodeOut"])
    types["GceClusterConfigIn"] = t.struct(
        {
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigIn"]
            ).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "networkUri": t.string().optional(),
            "reservationAffinity": t.proxy(renames["ReservationAffinityIn"]).optional(),
            "subnetworkUri": t.string().optional(),
            "zoneUri": t.string().optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "nodeGroupAffinity": t.proxy(renames["NodeGroupAffinityIn"]).optional(),
            "serviceAccount": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "serviceAccountScopes": t.array(t.string()).optional(),
            "internalIpOnly": t.boolean().optional(),
            "confidentialInstanceConfig": t.proxy(
                renames["ConfidentialInstanceConfigIn"]
            ).optional(),
        }
    ).named(renames["GceClusterConfigIn"])
    types["GceClusterConfigOut"] = t.struct(
        {
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigOut"]
            ).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "networkUri": t.string().optional(),
            "reservationAffinity": t.proxy(
                renames["ReservationAffinityOut"]
            ).optional(),
            "subnetworkUri": t.string().optional(),
            "zoneUri": t.string().optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "nodeGroupAffinity": t.proxy(renames["NodeGroupAffinityOut"]).optional(),
            "serviceAccount": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "serviceAccountScopes": t.array(t.string()).optional(),
            "internalIpOnly": t.boolean().optional(),
            "confidentialInstanceConfig": t.proxy(
                renames["ConfidentialInstanceConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceClusterConfigOut"])
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
    types["NodeGroupAffinityIn"] = t.struct({"nodeGroupUri": t.string()}).named(
        renames["NodeGroupAffinityIn"]
    )
    types["NodeGroupAffinityOut"] = t.struct(
        {
            "nodeGroupUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeGroupAffinityOut"])
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
    types["TrinoJobIn"] = t.struct(
        {
            "queryFileUri": t.string().optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "outputFormat": t.string().optional(),
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "clientTags": t.array(t.string()).optional(),
            "continueOnFailure": t.boolean().optional(),
        }
    ).named(renames["TrinoJobIn"])
    types["TrinoJobOut"] = t.struct(
        {
            "queryFileUri": t.string().optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "outputFormat": t.string().optional(),
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "clientTags": t.array(t.string()).optional(),
            "continueOnFailure": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrinoJobOut"])
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
    types["ClusterOperationStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClusterOperationStatusIn"]
    )
    types["ClusterOperationStatusOut"] = t.struct(
        {
            "innerState": t.string().optional(),
            "details": t.string().optional(),
            "state": t.string().optional(),
            "stateStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOperationStatusOut"])
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
    types["PrestoJobIn"] = t.struct(
        {
            "queryFileUri": t.string().optional(),
            "continueOnFailure": t.boolean().optional(),
            "outputFormat": t.string().optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
            "clientTags": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PrestoJobIn"])
    types["PrestoJobOut"] = t.struct(
        {
            "queryFileUri": t.string().optional(),
            "continueOnFailure": t.boolean().optional(),
            "outputFormat": t.string().optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "clientTags": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrestoJobOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["AutoscalingPolicyIn"] = t.struct(
        {
            "basicAlgorithm": t.proxy(renames["BasicAutoscalingAlgorithmIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "secondaryWorkerConfig": t.proxy(
                renames["InstanceGroupAutoscalingPolicyConfigIn"]
            ).optional(),
            "workerConfig": t.proxy(renames["InstanceGroupAutoscalingPolicyConfigIn"]),
            "id": t.string(),
        }
    ).named(renames["AutoscalingPolicyIn"])
    types["AutoscalingPolicyOut"] = t.struct(
        {
            "basicAlgorithm": t.proxy(renames["BasicAutoscalingAlgorithmOut"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "secondaryWorkerConfig": t.proxy(
                renames["InstanceGroupAutoscalingPolicyConfigOut"]
            ).optional(),
            "workerConfig": t.proxy(renames["InstanceGroupAutoscalingPolicyConfigOut"]),
            "name": t.string().optional(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoscalingPolicyOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["SparkStandaloneAutoscalingConfigIn"] = t.struct(
        {
            "scaleDownMinWorkerFraction": t.number().optional(),
            "gracefulDecommissionTimeout": t.string(),
            "scaleDownFactor": t.number(),
            "scaleUpMinWorkerFraction": t.number().optional(),
            "scaleUpFactor": t.number(),
        }
    ).named(renames["SparkStandaloneAutoscalingConfigIn"])
    types["SparkStandaloneAutoscalingConfigOut"] = t.struct(
        {
            "scaleDownMinWorkerFraction": t.number().optional(),
            "gracefulDecommissionTimeout": t.string(),
            "scaleDownFactor": t.number(),
            "scaleUpMinWorkerFraction": t.number().optional(),
            "scaleUpFactor": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkStandaloneAutoscalingConfigOut"])
    types["SparkRJobIn"] = t.struct(
        {
            "args": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "fileUris": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "mainRFileUri": t.string(),
        }
    ).named(renames["SparkRJobIn"])
    types["SparkRJobOut"] = t.struct(
        {
            "args": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "fileUris": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "mainRFileUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkRJobOut"])
    types["ShieldedInstanceConfigIn"] = t.struct(
        {
            "enableIntegrityMonitoring": t.boolean().optional(),
            "enableVtpm": t.boolean().optional(),
            "enableSecureBoot": t.boolean().optional(),
        }
    ).named(renames["ShieldedInstanceConfigIn"])
    types["ShieldedInstanceConfigOut"] = t.struct(
        {
            "enableIntegrityMonitoring": t.boolean().optional(),
            "enableVtpm": t.boolean().optional(),
            "enableSecureBoot": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShieldedInstanceConfigOut"])
    types["DiskConfigIn"] = t.struct(
        {
            "bootDiskType": t.string().optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "localSsdInterface": t.string().optional(),
            "numLocalSsds": t.integer().optional(),
        }
    ).named(renames["DiskConfigIn"])
    types["DiskConfigOut"] = t.struct(
        {
            "bootDiskType": t.string().optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "localSsdInterface": t.string().optional(),
            "numLocalSsds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskConfigOut"])
    types["DiagnoseClusterRequestIn"] = t.struct(
        {
            "diagnosisInterval": t.proxy(renames["IntervalIn"]).optional(),
            "yarnApplicationIds": t.array(t.string()).optional(),
            "jobs": t.array(t.string()).optional(),
            "job": t.string().optional(),
            "yarnApplicationId": t.string().optional(),
        }
    ).named(renames["DiagnoseClusterRequestIn"])
    types["DiagnoseClusterRequestOut"] = t.struct(
        {
            "diagnosisInterval": t.proxy(renames["IntervalOut"]).optional(),
            "yarnApplicationIds": t.array(t.string()).optional(),
            "jobs": t.array(t.string()).optional(),
            "job": t.string().optional(),
            "yarnApplicationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiagnoseClusterRequestOut"])
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
    types["HiveJobIn"] = t.struct(
        {
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "continueOnFailure": t.boolean().optional(),
            "queryFileUri": t.string().optional(),
        }
    ).named(renames["HiveJobIn"])
    types["HiveJobOut"] = t.struct(
        {
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "continueOnFailure": t.boolean().optional(),
            "queryFileUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HiveJobOut"])
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
    types["SparkBatchIn"] = t.struct(
        {
            "args": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
            "fileUris": t.array(t.string()).optional(),
            "mainJarFileUri": t.string().optional(),
            "jarFileUris": t.array(t.string()).optional(),
        }
    ).named(renames["SparkBatchIn"])
    types["SparkBatchOut"] = t.struct(
        {
            "args": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
            "fileUris": t.array(t.string()).optional(),
            "mainJarFileUri": t.string().optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkBatchOut"])
    types["JobIn"] = t.struct(
        {
            "pigJob": t.proxy(renames["PigJobIn"]).optional(),
            "prestoJob": t.proxy(renames["PrestoJobIn"]).optional(),
            "sparkSqlJob": t.proxy(renames["SparkSqlJobIn"]).optional(),
            "reference": t.proxy(renames["JobReferenceIn"]).optional(),
            "trinoJob": t.proxy(renames["TrinoJobIn"]).optional(),
            "driverSchedulingConfig": t.proxy(
                renames["DriverSchedulingConfigIn"]
            ).optional(),
            "hiveJob": t.proxy(renames["HiveJobIn"]).optional(),
            "sparkJob": t.proxy(renames["SparkJobIn"]).optional(),
            "pysparkJob": t.proxy(renames["PySparkJobIn"]).optional(),
            "placement": t.proxy(renames["JobPlacementIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sparkRJob": t.proxy(renames["SparkRJobIn"]).optional(),
            "scheduling": t.proxy(renames["JobSchedulingIn"]).optional(),
            "hadoopJob": t.proxy(renames["HadoopJobIn"]).optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "pigJob": t.proxy(renames["PigJobOut"]).optional(),
            "prestoJob": t.proxy(renames["PrestoJobOut"]).optional(),
            "sparkSqlJob": t.proxy(renames["SparkSqlJobOut"]).optional(),
            "reference": t.proxy(renames["JobReferenceOut"]).optional(),
            "statusHistory": t.array(t.proxy(renames["JobStatusOut"])).optional(),
            "trinoJob": t.proxy(renames["TrinoJobOut"]).optional(),
            "driverSchedulingConfig": t.proxy(
                renames["DriverSchedulingConfigOut"]
            ).optional(),
            "yarnApplications": t.array(
                t.proxy(renames["YarnApplicationOut"])
            ).optional(),
            "hiveJob": t.proxy(renames["HiveJobOut"]).optional(),
            "sparkJob": t.proxy(renames["SparkJobOut"]).optional(),
            "pysparkJob": t.proxy(renames["PySparkJobOut"]).optional(),
            "placement": t.proxy(renames["JobPlacementOut"]),
            "jobUuid": t.string().optional(),
            "driverControlFilesUri": t.string().optional(),
            "done": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "status": t.proxy(renames["JobStatusOut"]).optional(),
            "sparkRJob": t.proxy(renames["SparkRJobOut"]).optional(),
            "scheduling": t.proxy(renames["JobSchedulingOut"]).optional(),
            "hadoopJob": t.proxy(renames["HadoopJobOut"]).optional(),
            "driverOutputResourceUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["SparkJobIn"] = t.struct(
        {
            "fileUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "mainJarFileUri": t.string().optional(),
            "archiveUris": t.array(t.string()).optional(),
        }
    ).named(renames["SparkJobIn"])
    types["SparkJobOut"] = t.struct(
        {
            "fileUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "mainJarFileUri": t.string().optional(),
            "archiveUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkJobOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["PySparkBatchIn"] = t.struct(
        {
            "args": t.array(t.string()).optional(),
            "pythonFileUris": t.array(t.string()).optional(),
            "mainPythonFileUri": t.string(),
            "fileUris": t.array(t.string()).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
        }
    ).named(renames["PySparkBatchIn"])
    types["PySparkBatchOut"] = t.struct(
        {
            "args": t.array(t.string()).optional(),
            "pythonFileUris": t.array(t.string()).optional(),
            "mainPythonFileUri": t.string(),
            "fileUris": t.array(t.string()).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PySparkBatchOut"])
    types["KubernetesClusterConfigIn"] = t.struct(
        {
            "kubernetesNamespace": t.string().optional(),
            "kubernetesSoftwareConfig": t.proxy(
                renames["KubernetesSoftwareConfigIn"]
            ).optional(),
            "gkeClusterConfig": t.proxy(renames["GkeClusterConfigIn"]),
        }
    ).named(renames["KubernetesClusterConfigIn"])
    types["KubernetesClusterConfigOut"] = t.struct(
        {
            "kubernetesNamespace": t.string().optional(),
            "kubernetesSoftwareConfig": t.proxy(
                renames["KubernetesSoftwareConfigOut"]
            ).optional(),
            "gkeClusterConfig": t.proxy(renames["GkeClusterConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesClusterConfigOut"])
    types["ClusterOperationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClusterOperationIn"]
    )
    types["ClusterOperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "operationId": t.string().optional(),
        }
    ).named(renames["ClusterOperationOut"])
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
    types["ClusterStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClusterStatusIn"]
    )
    types["ClusterStatusOut"] = t.struct(
        {
            "stateStartTime": t.string().optional(),
            "substate": t.string().optional(),
            "detail": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterStatusOut"])
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
    types["CancelJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelJobRequestIn"]
    )
    types["CancelJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelJobRequestOut"])
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
    types["ValueValidationIn"] = t.struct({"values": t.array(t.string())}).named(
        renames["ValueValidationIn"]
    )
    types["ValueValidationOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueValidationOut"])
    types["JobStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["JobStatusIn"]
    )
    types["JobStatusOut"] = t.struct(
        {
            "details": t.string().optional(),
            "stateStartTime": t.string().optional(),
            "substate": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatusOut"])
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
            "jarFileUris": t.array(t.string()).optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "queryFileUri": t.string().optional(),
            "continueOnFailure": t.boolean().optional(),
        }
    ).named(renames["PigJobIn"])
    types["PigJobOut"] = t.struct(
        {
            "jarFileUris": t.array(t.string()).optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "queryFileUri": t.string().optional(),
            "continueOnFailure": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PigJobOut"])
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
    types["WorkflowMetadataIn"] = t.struct(
        {"parameters": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["WorkflowMetadataIn"])
    types["WorkflowMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "dagTimeout": t.string().optional(),
            "graph": t.proxy(renames["WorkflowGraphOut"]).optional(),
            "endTime": t.string().optional(),
            "clusterUuid": t.string().optional(),
            "deleteCluster": t.proxy(renames["ClusterOperationOut"]).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "clusterName": t.string().optional(),
            "template": t.string().optional(),
            "version": t.integer().optional(),
            "dagStartTime": t.string().optional(),
            "createCluster": t.proxy(renames["ClusterOperationOut"]).optional(),
            "startTime": t.string().optional(),
            "dagEndTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowMetadataOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DataprocMetricConfigIn"] = t.struct(
        {"metrics": t.array(t.proxy(renames["MetricIn"]))}
    ).named(renames["DataprocMetricConfigIn"])
    types["DataprocMetricConfigOut"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataprocMetricConfigOut"])
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
    types["ExecutionConfigIn"] = t.struct(
        {
            "networkUri": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "subnetworkUri": t.string().optional(),
            "ttl": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "idleTtl": t.string().optional(),
            "stagingBucket": t.string().optional(),
            "kmsKey": t.string().optional(),
        }
    ).named(renames["ExecutionConfigIn"])
    types["ExecutionConfigOut"] = t.struct(
        {
            "networkUri": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "subnetworkUri": t.string().optional(),
            "ttl": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "idleTtl": t.string().optional(),
            "stagingBucket": t.string().optional(),
            "kmsKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionConfigOut"])
    types["ReservationAffinityIn"] = t.struct(
        {
            "consumeReservationType": t.string().optional(),
            "key": t.string().optional(),
            "values": t.array(t.string()).optional(),
        }
    ).named(renames["ReservationAffinityIn"])
    types["ReservationAffinityOut"] = t.struct(
        {
            "consumeReservationType": t.string().optional(),
            "key": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReservationAffinityOut"])
    types["RepairClusterRequestIn"] = t.struct(
        {
            "clusterUuid": t.string().optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolIn"])).optional(),
            "requestId": t.string().optional(),
            "gracefulDecommissionTimeout": t.string().optional(),
            "parentOperationId": t.string().optional(),
        }
    ).named(renames["RepairClusterRequestIn"])
    types["RepairClusterRequestOut"] = t.struct(
        {
            "clusterUuid": t.string().optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolOut"])).optional(),
            "requestId": t.string().optional(),
            "gracefulDecommissionTimeout": t.string().optional(),
            "parentOperationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepairClusterRequestOut"])
    types["SoftwareConfigIn"] = t.struct(
        {
            "optionalComponents": t.array(t.string()).optional(),
            "imageVersion": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SoftwareConfigIn"])
    types["SoftwareConfigOut"] = t.struct(
        {
            "optionalComponents": t.array(t.string()).optional(),
            "imageVersion": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SoftwareConfigOut"])
    types["ClusterConfigIn"] = t.struct(
        {
            "gceClusterConfig": t.proxy(renames["GceClusterConfigIn"]).optional(),
            "lifecycleConfig": t.proxy(renames["LifecycleConfigIn"]).optional(),
            "dataprocMetricConfig": t.proxy(
                renames["DataprocMetricConfigIn"]
            ).optional(),
            "secondaryWorkerConfig": t.proxy(
                renames["InstanceGroupConfigIn"]
            ).optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
            "gkeClusterConfig": t.proxy(renames["GkeClusterConfigIn"]).optional(),
            "tempBucket": t.string().optional(),
            "metastoreConfig": t.proxy(renames["MetastoreConfigIn"]).optional(),
            "masterConfig": t.proxy(renames["InstanceGroupConfigIn"]).optional(),
            "securityConfig": t.proxy(renames["SecurityConfigIn"]).optional(),
            "autoscalingConfig": t.proxy(renames["AutoscalingConfigIn"]).optional(),
            "workerConfig": t.proxy(renames["InstanceGroupConfigIn"]).optional(),
            "auxiliaryNodeGroups": t.array(
                t.proxy(renames["AuxiliaryNodeGroupIn"])
            ).optional(),
            "configBucket": t.string().optional(),
            "endpointConfig": t.proxy(renames["EndpointConfigIn"]).optional(),
            "initializationActions": t.array(
                t.proxy(renames["NodeInitializationActionIn"])
            ).optional(),
            "softwareConfig": t.proxy(renames["SoftwareConfigIn"]).optional(),
        }
    ).named(renames["ClusterConfigIn"])
    types["ClusterConfigOut"] = t.struct(
        {
            "gceClusterConfig": t.proxy(renames["GceClusterConfigOut"]).optional(),
            "lifecycleConfig": t.proxy(renames["LifecycleConfigOut"]).optional(),
            "dataprocMetricConfig": t.proxy(
                renames["DataprocMetricConfigOut"]
            ).optional(),
            "secondaryWorkerConfig": t.proxy(
                renames["InstanceGroupConfigOut"]
            ).optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "gkeClusterConfig": t.proxy(renames["GkeClusterConfigOut"]).optional(),
            "tempBucket": t.string().optional(),
            "metastoreConfig": t.proxy(renames["MetastoreConfigOut"]).optional(),
            "masterConfig": t.proxy(renames["InstanceGroupConfigOut"]).optional(),
            "securityConfig": t.proxy(renames["SecurityConfigOut"]).optional(),
            "autoscalingConfig": t.proxy(renames["AutoscalingConfigOut"]).optional(),
            "workerConfig": t.proxy(renames["InstanceGroupConfigOut"]).optional(),
            "auxiliaryNodeGroups": t.array(
                t.proxy(renames["AuxiliaryNodeGroupOut"])
            ).optional(),
            "configBucket": t.string().optional(),
            "endpointConfig": t.proxy(renames["EndpointConfigOut"]).optional(),
            "initializationActions": t.array(
                t.proxy(renames["NodeInitializationActionOut"])
            ).optional(),
            "softwareConfig": t.proxy(renames["SoftwareConfigOut"]).optional(),
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
    types["ConfidentialInstanceConfigIn"] = t.struct(
        {"enableConfidentialCompute": t.boolean().optional()}
    ).named(renames["ConfidentialInstanceConfigIn"])
    types["ConfidentialInstanceConfigOut"] = t.struct(
        {
            "enableConfidentialCompute": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfidentialInstanceConfigOut"])
    types["WorkflowGraphIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WorkflowGraphIn"]
    )
    types["WorkflowGraphOut"] = t.struct(
        {
            "nodes": t.array(t.proxy(renames["WorkflowNodeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowGraphOut"])
    types["UsageSnapshotIn"] = t.struct(
        {
            "shuffleStorageGb": t.string().optional(),
            "snapshotTime": t.string().optional(),
            "milliDcu": t.string().optional(),
        }
    ).named(renames["UsageSnapshotIn"])
    types["UsageSnapshotOut"] = t.struct(
        {
            "shuffleStorageGb": t.string().optional(),
            "snapshotTime": t.string().optional(),
            "milliDcu": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageSnapshotOut"])
    types["LifecycleConfigIn"] = t.struct(
        {
            "autoDeleteTtl": t.string().optional(),
            "autoDeleteTime": t.string().optional(),
            "idleDeleteTtl": t.string().optional(),
        }
    ).named(renames["LifecycleConfigIn"])
    types["LifecycleConfigOut"] = t.struct(
        {
            "idleStartTime": t.string().optional(),
            "autoDeleteTtl": t.string().optional(),
            "autoDeleteTime": t.string().optional(),
            "idleDeleteTtl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LifecycleConfigOut"])
    types["InstantiateWorkflowTemplateRequestIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["InstantiateWorkflowTemplateRequestIn"])
    types["InstantiateWorkflowTemplateRequestOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstantiateWorkflowTemplateRequestOut"])
    types["ClusterIn"] = t.struct(
        {
            "projectId": t.string(),
            "config": t.proxy(renames["ClusterConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "clusterName": t.string(),
            "virtualClusterConfig": t.proxy(
                renames["VirtualClusterConfigIn"]
            ).optional(),
        }
    ).named(renames["ClusterIn"])
    types["ClusterOut"] = t.struct(
        {
            "projectId": t.string(),
            "config": t.proxy(renames["ClusterConfigOut"]).optional(),
            "status": t.proxy(renames["ClusterStatusOut"]).optional(),
            "metrics": t.proxy(renames["ClusterMetricsOut"]).optional(),
            "statusHistory": t.array(t.proxy(renames["ClusterStatusOut"])).optional(),
            "clusterUuid": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "clusterName": t.string(),
            "virtualClusterConfig": t.proxy(
                renames["VirtualClusterConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOut"])
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
    types["ResizeNodeGroupRequestIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "gracefulDecommissionTimeout": t.string().optional(),
            "size": t.integer(),
        }
    ).named(renames["ResizeNodeGroupRequestIn"])
    types["ResizeNodeGroupRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "gracefulDecommissionTimeout": t.string().optional(),
            "size": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResizeNodeGroupRequestOut"])
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
    types["GkeNodePoolTargetIn"] = t.struct(
        {
            "roles": t.array(t.string()),
            "nodePoolConfig": t.proxy(renames["GkeNodePoolConfigIn"]).optional(),
            "nodePool": t.string(),
        }
    ).named(renames["GkeNodePoolTargetIn"])
    types["GkeNodePoolTargetOut"] = t.struct(
        {
            "roles": t.array(t.string()),
            "nodePoolConfig": t.proxy(renames["GkeNodePoolConfigOut"]).optional(),
            "nodePool": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNodePoolTargetOut"])
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
    types["NodePoolIn"] = t.struct(
        {
            "id": t.string(),
            "repairAction": t.string(),
            "instanceNames": t.array(t.string()).optional(),
        }
    ).named(renames["NodePoolIn"])
    types["NodePoolOut"] = t.struct(
        {
            "id": t.string(),
            "repairAction": t.string(),
            "instanceNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolOut"])
    types["HadoopJobIn"] = t.struct(
        {
            "jarFileUris": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "args": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "mainJarFileUri": t.string().optional(),
        }
    ).named(renames["HadoopJobIn"])
    types["HadoopJobOut"] = t.struct(
        {
            "jarFileUris": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "args": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "mainJarFileUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HadoopJobOut"])
    types["KerberosConfigIn"] = t.struct(
        {
            "keystoreUri": t.string().optional(),
            "tgtLifetimeHours": t.integer().optional(),
            "keystorePasswordUri": t.string().optional(),
            "truststoreUri": t.string().optional(),
            "realm": t.string().optional(),
            "crossRealmTrustKdc": t.string().optional(),
            "truststorePasswordUri": t.string().optional(),
            "crossRealmTrustSharedPasswordUri": t.string().optional(),
            "keyPasswordUri": t.string().optional(),
            "enableKerberos": t.boolean().optional(),
            "kdcDbKeyUri": t.string().optional(),
            "kmsKeyUri": t.string().optional(),
            "crossRealmTrustAdminServer": t.string().optional(),
            "rootPrincipalPasswordUri": t.string().optional(),
            "crossRealmTrustRealm": t.string().optional(),
        }
    ).named(renames["KerberosConfigIn"])
    types["KerberosConfigOut"] = t.struct(
        {
            "keystoreUri": t.string().optional(),
            "tgtLifetimeHours": t.integer().optional(),
            "keystorePasswordUri": t.string().optional(),
            "truststoreUri": t.string().optional(),
            "realm": t.string().optional(),
            "crossRealmTrustKdc": t.string().optional(),
            "truststorePasswordUri": t.string().optional(),
            "crossRealmTrustSharedPasswordUri": t.string().optional(),
            "keyPasswordUri": t.string().optional(),
            "enableKerberos": t.boolean().optional(),
            "kdcDbKeyUri": t.string().optional(),
            "kmsKeyUri": t.string().optional(),
            "crossRealmTrustAdminServer": t.string().optional(),
            "rootPrincipalPasswordUri": t.string().optional(),
            "crossRealmTrustRealm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KerberosConfigOut"])
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
    types["SparkRBatchIn"] = t.struct(
        {
            "args": t.array(t.string()).optional(),
            "mainRFileUri": t.string(),
            "archiveUris": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
        }
    ).named(renames["SparkRBatchIn"])
    types["SparkRBatchOut"] = t.struct(
        {
            "args": t.array(t.string()).optional(),
            "mainRFileUri": t.string(),
            "archiveUris": t.array(t.string()).optional(),
            "fileUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkRBatchOut"])
    types["BatchOperationMetadataIn"] = t.struct(
        {
            "batchUuid": t.string().optional(),
            "batch": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "warnings": t.array(t.string()).optional(),
            "doneTime": t.string().optional(),
            "operationType": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["BatchOperationMetadataIn"])
    types["BatchOperationMetadataOut"] = t.struct(
        {
            "batchUuid": t.string().optional(),
            "batch": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "warnings": t.array(t.string()).optional(),
            "doneTime": t.string().optional(),
            "operationType": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchOperationMetadataOut"])
    types["PySparkJobIn"] = t.struct(
        {
            "archiveUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "pythonFileUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "fileUris": t.array(t.string()).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "mainPythonFileUri": t.string(),
        }
    ).named(renames["PySparkJobIn"])
    types["PySparkJobOut"] = t.struct(
        {
            "archiveUris": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "pythonFileUris": t.array(t.string()).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "fileUris": t.array(t.string()).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "mainPythonFileUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PySparkJobOut"])
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
    types["WorkflowTemplateIn"] = t.struct(
        {
            "id": t.string(),
            "version": t.integer().optional(),
            "placement": t.proxy(renames["WorkflowTemplatePlacementIn"]),
            "jobs": t.array(t.proxy(renames["OrderedJobIn"])),
            "dagTimeout": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.array(t.proxy(renames["TemplateParameterIn"])).optional(),
        }
    ).named(renames["WorkflowTemplateIn"])
    types["WorkflowTemplateOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "id": t.string(),
            "version": t.integer().optional(),
            "createTime": t.string().optional(),
            "placement": t.proxy(renames["WorkflowTemplatePlacementOut"]),
            "jobs": t.array(t.proxy(renames["OrderedJobOut"])),
            "dagTimeout": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "parameters": t.array(t.proxy(renames["TemplateParameterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowTemplateOut"])
    types["GkeClusterConfigIn"] = t.struct(
        {
            "nodePoolTarget": t.array(
                t.proxy(renames["GkeNodePoolTargetIn"])
            ).optional(),
            "namespacedGkeDeploymentTarget": t.proxy(
                renames["NamespacedGkeDeploymentTargetIn"]
            ).optional(),
            "gkeClusterTarget": t.string().optional(),
        }
    ).named(renames["GkeClusterConfigIn"])
    types["GkeClusterConfigOut"] = t.struct(
        {
            "nodePoolTarget": t.array(
                t.proxy(renames["GkeNodePoolTargetOut"])
            ).optional(),
            "namespacedGkeDeploymentTarget": t.proxy(
                renames["NamespacedGkeDeploymentTargetOut"]
            ).optional(),
            "gkeClusterTarget": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeClusterConfigOut"])
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
    types["TemplateParameterIn"] = t.struct(
        {
            "fields": t.array(t.string()),
            "name": t.string(),
            "description": t.string().optional(),
            "validation": t.proxy(renames["ParameterValidationIn"]).optional(),
        }
    ).named(renames["TemplateParameterIn"])
    types["TemplateParameterOut"] = t.struct(
        {
            "fields": t.array(t.string()),
            "name": t.string(),
            "description": t.string().optional(),
            "validation": t.proxy(renames["ParameterValidationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TemplateParameterOut"])
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
    types["OrderedJobIn"] = t.struct(
        {
            "sparkRJob": t.proxy(renames["SparkRJobIn"]).optional(),
            "stepId": t.string(),
            "trinoJob": t.proxy(renames["TrinoJobIn"]).optional(),
            "sparkJob": t.proxy(renames["SparkJobIn"]).optional(),
            "hadoopJob": t.proxy(renames["HadoopJobIn"]).optional(),
            "pigJob": t.proxy(renames["PigJobIn"]).optional(),
            "scheduling": t.proxy(renames["JobSchedulingIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "hiveJob": t.proxy(renames["HiveJobIn"]).optional(),
            "prestoJob": t.proxy(renames["PrestoJobIn"]).optional(),
            "prerequisiteStepIds": t.array(t.string()).optional(),
            "sparkSqlJob": t.proxy(renames["SparkSqlJobIn"]).optional(),
            "pysparkJob": t.proxy(renames["PySparkJobIn"]).optional(),
        }
    ).named(renames["OrderedJobIn"])
    types["OrderedJobOut"] = t.struct(
        {
            "sparkRJob": t.proxy(renames["SparkRJobOut"]).optional(),
            "stepId": t.string(),
            "trinoJob": t.proxy(renames["TrinoJobOut"]).optional(),
            "sparkJob": t.proxy(renames["SparkJobOut"]).optional(),
            "hadoopJob": t.proxy(renames["HadoopJobOut"]).optional(),
            "pigJob": t.proxy(renames["PigJobOut"]).optional(),
            "scheduling": t.proxy(renames["JobSchedulingOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "hiveJob": t.proxy(renames["HiveJobOut"]).optional(),
            "prestoJob": t.proxy(renames["PrestoJobOut"]).optional(),
            "prerequisiteStepIds": t.array(t.string()).optional(),
            "sparkSqlJob": t.proxy(renames["SparkSqlJobOut"]).optional(),
            "pysparkJob": t.proxy(renames["PySparkJobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderedJobOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["InstanceGroupConfigIn"] = t.struct(
        {
            "machineTypeUri": t.string().optional(),
            "minCpuPlatform": t.string().optional(),
            "imageUri": t.string().optional(),
            "numInstances": t.integer().optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorConfigIn"])).optional(),
            "diskConfig": t.proxy(renames["DiskConfigIn"]).optional(),
            "preemptibility": t.string().optional(),
        }
    ).named(renames["InstanceGroupConfigIn"])
    types["InstanceGroupConfigOut"] = t.struct(
        {
            "machineTypeUri": t.string().optional(),
            "minCpuPlatform": t.string().optional(),
            "managedGroupConfig": t.proxy(renames["ManagedGroupConfigOut"]).optional(),
            "instanceReferences": t.array(
                t.proxy(renames["InstanceReferenceOut"])
            ).optional(),
            "imageUri": t.string().optional(),
            "isPreemptible": t.boolean().optional(),
            "numInstances": t.integer().optional(),
            "accelerators": t.array(
                t.proxy(renames["AcceleratorConfigOut"])
            ).optional(),
            "diskConfig": t.proxy(renames["DiskConfigOut"]).optional(),
            "instanceNames": t.array(t.string()).optional(),
            "preemptibility": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceGroupConfigOut"])
    types["ClusterOperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClusterOperationMetadataIn"]
    )
    types["ClusterOperationMetadataOut"] = t.struct(
        {
            "childOperationIds": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "statusHistory": t.array(
                t.proxy(renames["ClusterOperationStatusOut"])
            ).optional(),
            "status": t.proxy(renames["ClusterOperationStatusOut"]).optional(),
            "clusterName": t.string().optional(),
            "clusterUuid": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "operationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOperationMetadataOut"])
    types["SparkSqlBatchIn"] = t.struct(
        {
            "jarFileUris": t.array(t.string()).optional(),
            "queryVariables": t.struct({"_": t.string().optional()}).optional(),
            "queryFileUri": t.string(),
        }
    ).named(renames["SparkSqlBatchIn"])
    types["SparkSqlBatchOut"] = t.struct(
        {
            "jarFileUris": t.array(t.string()).optional(),
            "queryVariables": t.struct({"_": t.string().optional()}).optional(),
            "queryFileUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkSqlBatchOut"])
    types["SparkSqlJobIn"] = t.struct(
        {
            "queryList": t.proxy(renames["QueryListIn"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "queryFileUri": t.string().optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
        }
    ).named(renames["SparkSqlJobIn"])
    types["SparkSqlJobOut"] = t.struct(
        {
            "queryList": t.proxy(renames["QueryListOut"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "jarFileUris": t.array(t.string()).optional(),
            "queryFileUri": t.string().optional(),
            "scriptVariables": t.struct({"_": t.string().optional()}).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkSqlJobOut"])
    types["SessionOperationMetadataIn"] = t.struct(
        {
            "session": t.string().optional(),
            "doneTime": t.string().optional(),
            "createTime": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "sessionUuid": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "operationType": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["SessionOperationMetadataIn"])
    types["SessionOperationMetadataOut"] = t.struct(
        {
            "session": t.string().optional(),
            "doneTime": t.string().optional(),
            "createTime": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "sessionUuid": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "operationType": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionOperationMetadataOut"])
    types["JobMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["JobMetadataIn"]
    )
    types["JobMetadataOut"] = t.struct(
        {
            "status": t.proxy(renames["JobStatusOut"]).optional(),
            "startTime": t.string().optional(),
            "jobId": t.string().optional(),
            "operationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobMetadataOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ListBatchesResponseIn"] = t.struct(
        {"nextPageToken": t.string().optional()}
    ).named(renames["ListBatchesResponseIn"])
    types["ListBatchesResponseOut"] = t.struct(
        {
            "batches": t.array(t.proxy(renames["BatchOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBatchesResponseOut"])
    types["BasicYarnAutoscalingConfigIn"] = t.struct(
        {
            "scaleUpFactor": t.number(),
            "gracefulDecommissionTimeout": t.string(),
            "scaleDownFactor": t.number(),
            "scaleUpMinWorkerFraction": t.number().optional(),
            "scaleDownMinWorkerFraction": t.number().optional(),
        }
    ).named(renames["BasicYarnAutoscalingConfigIn"])
    types["BasicYarnAutoscalingConfigOut"] = t.struct(
        {
            "scaleUpFactor": t.number(),
            "gracefulDecommissionTimeout": t.string(),
            "scaleDownFactor": t.number(),
            "scaleUpMinWorkerFraction": t.number().optional(),
            "scaleDownMinWorkerFraction": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicYarnAutoscalingConfigOut"])
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
    types["SparkHistoryServerConfigIn"] = t.struct(
        {"dataprocCluster": t.string().optional()}
    ).named(renames["SparkHistoryServerConfigIn"])
    types["SparkHistoryServerConfigOut"] = t.struct(
        {
            "dataprocCluster": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkHistoryServerConfigOut"])
    types["BatchIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "environmentConfig": t.proxy(renames["EnvironmentConfigIn"]).optional(),
            "sparkSqlBatch": t.proxy(renames["SparkSqlBatchIn"]).optional(),
            "runtimeConfig": t.proxy(renames["RuntimeConfigIn"]).optional(),
            "sparkBatch": t.proxy(renames["SparkBatchIn"]).optional(),
            "pysparkBatch": t.proxy(renames["PySparkBatchIn"]).optional(),
            "sparkRBatch": t.proxy(renames["SparkRBatchIn"]).optional(),
        }
    ).named(renames["BatchIn"])
    types["BatchOut"] = t.struct(
        {
            "stateHistory": t.array(t.proxy(renames["StateHistoryOut"])).optional(),
            "stateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "creator": t.string().optional(),
            "runtimeInfo": t.proxy(renames["RuntimeInfoOut"]).optional(),
            "name": t.string().optional(),
            "operation": t.string().optional(),
            "environmentConfig": t.proxy(renames["EnvironmentConfigOut"]).optional(),
            "sparkSqlBatch": t.proxy(renames["SparkSqlBatchOut"]).optional(),
            "stateMessage": t.string().optional(),
            "runtimeConfig": t.proxy(renames["RuntimeConfigOut"]).optional(),
            "sparkBatch": t.proxy(renames["SparkBatchOut"]).optional(),
            "uuid": t.string().optional(),
            "pysparkBatch": t.proxy(renames["PySparkBatchOut"]).optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "sparkRBatch": t.proxy(renames["SparkRBatchOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchOut"])
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
    types["LoggingConfigIn"] = t.struct(
        {"driverLogLevels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["LoggingConfigIn"])
    types["LoggingConfigOut"] = t.struct(
        {
            "driverLogLevels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingConfigOut"])
    types["InstanceReferenceIn"] = t.struct(
        {
            "publicEciesKey": t.string().optional(),
            "instanceId": t.string().optional(),
            "publicKey": t.string().optional(),
            "instanceName": t.string().optional(),
        }
    ).named(renames["InstanceReferenceIn"])
    types["InstanceReferenceOut"] = t.struct(
        {
            "publicEciesKey": t.string().optional(),
            "instanceId": t.string().optional(),
            "publicKey": t.string().optional(),
            "instanceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceReferenceOut"])
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
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["DiagnoseClusterResultsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DiagnoseClusterResultsIn"]
    )
    types["DiagnoseClusterResultsOut"] = t.struct(
        {
            "outputUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiagnoseClusterResultsOut"])
    types["GkeNodeConfigIn"] = t.struct(
        {
            "preemptible": t.boolean().optional(),
            "localSsdCount": t.integer().optional(),
            "spot": t.boolean().optional(),
            "bootDiskKmsKey": t.string().optional(),
            "accelerators": t.array(
                t.proxy(renames["GkeNodePoolAcceleratorConfigIn"])
            ).optional(),
            "minCpuPlatform": t.string().optional(),
            "machineType": t.string().optional(),
        }
    ).named(renames["GkeNodeConfigIn"])
    types["GkeNodeConfigOut"] = t.struct(
        {
            "preemptible": t.boolean().optional(),
            "localSsdCount": t.integer().optional(),
            "spot": t.boolean().optional(),
            "bootDiskKmsKey": t.string().optional(),
            "accelerators": t.array(
                t.proxy(renames["GkeNodePoolAcceleratorConfigOut"])
            ).optional(),
            "minCpuPlatform": t.string().optional(),
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNodeConfigOut"])
    types["NodeGroupOperationMetadataIn"] = t.struct(
        {"operationType": t.string().optional()}
    ).named(renames["NodeGroupOperationMetadataIn"])
    types["NodeGroupOperationMetadataOut"] = t.struct(
        {
            "statusHistory": t.array(
                t.proxy(renames["ClusterOperationStatusOut"])
            ).optional(),
            "clusterUuid": t.string().optional(),
            "description": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "nodeGroupId": t.string().optional(),
            "operationType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "status": t.proxy(renames["ClusterOperationStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeGroupOperationMetadataOut"])
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
    types["RuntimeInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RuntimeInfoIn"]
    )
    types["RuntimeInfoOut"] = t.struct(
        {
            "currentUsage": t.proxy(renames["UsageSnapshotOut"]).optional(),
            "approximateUsage": t.proxy(renames["UsageMetricsOut"]).optional(),
            "outputUri": t.string().optional(),
            "diagnosticOutputUri": t.string().optional(),
            "endpoints": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeInfoOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
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
    types["MetastoreConfigIn"] = t.struct(
        {"dataprocMetastoreService": t.string()}
    ).named(renames["MetastoreConfigIn"])
    types["MetastoreConfigOut"] = t.struct(
        {
            "dataprocMetastoreService": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetastoreConfigOut"])
    types["ClusterMetricsIn"] = t.struct(
        {
            "yarnMetrics": t.struct({"_": t.string().optional()}).optional(),
            "hdfsMetrics": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ClusterMetricsIn"])
    types["ClusterMetricsOut"] = t.struct(
        {
            "yarnMetrics": t.struct({"_": t.string().optional()}).optional(),
            "hdfsMetrics": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterMetricsOut"])
    types["NodeGroupIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "roles": t.array(t.string()),
            "nodeGroupConfig": t.proxy(renames["InstanceGroupConfigIn"]).optional(),
        }
    ).named(renames["NodeGroupIn"])
    types["NodeGroupOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "roles": t.array(t.string()),
            "nodeGroupConfig": t.proxy(renames["InstanceGroupConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeGroupOut"])
    types["IdentityConfigIn"] = t.struct(
        {"userServiceAccountMapping": t.struct({"_": t.string().optional()})}
    ).named(renames["IdentityConfigIn"])
    types["IdentityConfigOut"] = t.struct(
        {
            "userServiceAccountMapping": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityConfigOut"])

    functions = {}
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
    functions["projectsLocationsOperationsDelete"] = dataproc.post(
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
    functions["projectsLocationsBatchesGet"] = dataproc.get(
        "v1/{parent}/batches",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBatchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBatchesDelete"] = dataproc.get(
        "v1/{parent}/batches",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBatchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBatchesCreate"] = dataproc.get(
        "v1/{parent}/batches",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBatchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBatchesList"] = dataproc.get(
        "v1/{parent}/batches",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBatchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAutoscalingPoliciesDelete"] = dataproc.post(
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
    functions["projectsLocationsAutoscalingPoliciesList"] = dataproc.post(
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
    functions["projectsLocationsAutoscalingPoliciesTestIamPermissions"] = dataproc.post(
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
    functions["projectsLocationsAutoscalingPoliciesUpdate"] = dataproc.post(
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
    functions["projectsLocationsAutoscalingPoliciesCreate"] = dataproc.post(
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
    functions["projectsLocationsAutoscalingPoliciesGetIamPolicy"] = dataproc.post(
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
    functions["projectsLocationsAutoscalingPoliciesGet"] = dataproc.post(
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
    functions["projectsLocationsAutoscalingPoliciesSetIamPolicy"] = dataproc.post(
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
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "parent": t.string(),
                "id": t.string(),
                "version": t.integer().optional(),
                "placement": t.proxy(renames["WorkflowTemplatePlacementIn"]),
                "jobs": t.array(t.proxy(renames["OrderedJobIn"])),
                "dagTimeout": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parameters": t.array(
                    t.proxy(renames["TemplateParameterIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WorkflowTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesList"] = dataproc.post(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "parent": t.string(),
                "id": t.string(),
                "version": t.integer().optional(),
                "placement": t.proxy(renames["WorkflowTemplatePlacementIn"]),
                "jobs": t.array(t.proxy(renames["OrderedJobIn"])),
                "dagTimeout": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parameters": t.array(
                    t.proxy(renames["TemplateParameterIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WorkflowTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesSetIamPolicy"] = dataproc.post(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "parent": t.string(),
                "id": t.string(),
                "version": t.integer().optional(),
                "placement": t.proxy(renames["WorkflowTemplatePlacementIn"]),
                "jobs": t.array(t.proxy(renames["OrderedJobIn"])),
                "dagTimeout": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parameters": t.array(
                    t.proxy(renames["TemplateParameterIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WorkflowTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesGetIamPolicy"] = dataproc.post(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "parent": t.string(),
                "id": t.string(),
                "version": t.integer().optional(),
                "placement": t.proxy(renames["WorkflowTemplatePlacementIn"]),
                "jobs": t.array(t.proxy(renames["OrderedJobIn"])),
                "dagTimeout": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parameters": t.array(
                    t.proxy(renames["TemplateParameterIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WorkflowTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesGet"] = dataproc.post(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "parent": t.string(),
                "id": t.string(),
                "version": t.integer().optional(),
                "placement": t.proxy(renames["WorkflowTemplatePlacementIn"]),
                "jobs": t.array(t.proxy(renames["OrderedJobIn"])),
                "dagTimeout": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parameters": t.array(
                    t.proxy(renames["TemplateParameterIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WorkflowTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesUpdate"] = dataproc.post(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "parent": t.string(),
                "id": t.string(),
                "version": t.integer().optional(),
                "placement": t.proxy(renames["WorkflowTemplatePlacementIn"]),
                "jobs": t.array(t.proxy(renames["OrderedJobIn"])),
                "dagTimeout": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parameters": t.array(
                    t.proxy(renames["TemplateParameterIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WorkflowTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesInstantiate"] = dataproc.post(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "parent": t.string(),
                "id": t.string(),
                "version": t.integer().optional(),
                "placement": t.proxy(renames["WorkflowTemplatePlacementIn"]),
                "jobs": t.array(t.proxy(renames["OrderedJobIn"])),
                "dagTimeout": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parameters": t.array(
                    t.proxy(renames["TemplateParameterIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WorkflowTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesTestIamPermissions"] = dataproc.post(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "parent": t.string(),
                "id": t.string(),
                "version": t.integer().optional(),
                "placement": t.proxy(renames["WorkflowTemplatePlacementIn"]),
                "jobs": t.array(t.proxy(renames["OrderedJobIn"])),
                "dagTimeout": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parameters": t.array(
                    t.proxy(renames["TemplateParameterIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WorkflowTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesInstantiateInline"] = dataproc.post(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "parent": t.string(),
                "id": t.string(),
                "version": t.integer().optional(),
                "placement": t.proxy(renames["WorkflowTemplatePlacementIn"]),
                "jobs": t.array(t.proxy(renames["OrderedJobIn"])),
                "dagTimeout": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parameters": t.array(
                    t.proxy(renames["TemplateParameterIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WorkflowTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowTemplatesCreate"] = dataproc.post(
        "v1/{parent}/workflowTemplates",
        t.struct(
            {
                "parent": t.string(),
                "id": t.string(),
                "version": t.integer().optional(),
                "placement": t.proxy(renames["WorkflowTemplatePlacementIn"]),
                "jobs": t.array(t.proxy(renames["OrderedJobIn"])),
                "dagTimeout": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parameters": t.array(
                    t.proxy(renames["TemplateParameterIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WorkflowTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsList"] = dataproc.delete(
        "v1/projects/{projectId}/regions/{region}/jobs/{jobId}",
        t.struct(
            {
                "jobId": t.string(),
                "projectId": t.string(),
                "region": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsGetIamPolicy"] = dataproc.delete(
        "v1/projects/{projectId}/regions/{region}/jobs/{jobId}",
        t.struct(
            {
                "jobId": t.string(),
                "projectId": t.string(),
                "region": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsSetIamPolicy"] = dataproc.delete(
        "v1/projects/{projectId}/regions/{region}/jobs/{jobId}",
        t.struct(
            {
                "jobId": t.string(),
                "projectId": t.string(),
                "region": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsGet"] = dataproc.delete(
        "v1/projects/{projectId}/regions/{region}/jobs/{jobId}",
        t.struct(
            {
                "jobId": t.string(),
                "projectId": t.string(),
                "region": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsSubmitAsOperation"] = dataproc.delete(
        "v1/projects/{projectId}/regions/{region}/jobs/{jobId}",
        t.struct(
            {
                "jobId": t.string(),
                "projectId": t.string(),
                "region": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsTestIamPermissions"] = dataproc.delete(
        "v1/projects/{projectId}/regions/{region}/jobs/{jobId}",
        t.struct(
            {
                "jobId": t.string(),
                "projectId": t.string(),
                "region": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsPatch"] = dataproc.delete(
        "v1/projects/{projectId}/regions/{region}/jobs/{jobId}",
        t.struct(
            {
                "jobId": t.string(),
                "projectId": t.string(),
                "region": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsCancel"] = dataproc.delete(
        "v1/projects/{projectId}/regions/{region}/jobs/{jobId}",
        t.struct(
            {
                "jobId": t.string(),
                "projectId": t.string(),
                "region": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsSubmit"] = dataproc.delete(
        "v1/projects/{projectId}/regions/{region}/jobs/{jobId}",
        t.struct(
            {
                "jobId": t.string(),
                "projectId": t.string(),
                "region": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsJobsDelete"] = dataproc.delete(
        "v1/projects/{projectId}/regions/{region}/jobs/{jobId}",
        t.struct(
            {
                "jobId": t.string(),
                "projectId": t.string(),
                "region": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsCancel"] = dataproc.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsGetIamPolicy"] = dataproc.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsTestIamPermissions"] = dataproc.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsList"] = dataproc.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsSetIamPolicy"] = dataproc.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsDelete"] = dataproc.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsOperationsGet"] = dataproc.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersList"] = dataproc.get(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}",
        t.struct(
            {
                "clusterName": t.string(),
                "region": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsClustersTestIamPermissions"] = dataproc.get(
        "v1/projects/{projectId}/regions/{region}/clusters/{clusterName}",
        t.struct(
            {
                "clusterName": t.string(),
                "region": t.string(),
                "projectId": t.string(),
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
                "clusterName": t.string(),
                "region": t.string(),
                "projectId": t.string(),
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
                "clusterName": t.string(),
                "region": t.string(),
                "projectId": t.string(),
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
                "clusterName": t.string(),
                "region": t.string(),
                "projectId": t.string(),
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
                "clusterName": t.string(),
                "region": t.string(),
                "projectId": t.string(),
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
                "clusterName": t.string(),
                "region": t.string(),
                "projectId": t.string(),
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
                "clusterName": t.string(),
                "region": t.string(),
                "projectId": t.string(),
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
                "clusterName": t.string(),
                "region": t.string(),
                "projectId": t.string(),
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
                "clusterName": t.string(),
                "region": t.string(),
                "projectId": t.string(),
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
                "clusterName": t.string(),
                "region": t.string(),
                "projectId": t.string(),
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
                "clusterName": t.string(),
                "region": t.string(),
                "projectId": t.string(),
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
                "clusterName": t.string(),
                "region": t.string(),
                "projectId": t.string(),
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
                "gracefulDecommissionTimeout": t.string().optional(),
                "size": t.integer(),
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
                "gracefulDecommissionTimeout": t.string().optional(),
                "size": t.integer(),
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
                "gracefulDecommissionTimeout": t.string().optional(),
                "size": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRegionsWorkflowTemplatesList"] = dataproc.post(
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
    functions["projectsRegionsWorkflowTemplatesCreate"] = dataproc.post(
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
    functions["projectsRegionsWorkflowTemplatesUpdate"] = dataproc.post(
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
    functions["projectsRegionsWorkflowTemplatesDelete"] = dataproc.post(
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
    functions["projectsRegionsWorkflowTemplatesGetIamPolicy"] = dataproc.post(
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
    functions["projectsRegionsWorkflowTemplatesInstantiate"] = dataproc.post(
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
    functions["projectsRegionsWorkflowTemplatesInstantiateInline"] = dataproc.post(
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
    functions["projectsRegionsWorkflowTemplatesGet"] = dataproc.post(
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
    functions["projectsRegionsWorkflowTemplatesTestIamPermissions"] = dataproc.post(
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
    functions["projectsRegionsWorkflowTemplatesSetIamPolicy"] = dataproc.post(
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
    functions["projectsRegionsAutoscalingPoliciesUpdate"] = dataproc.post(
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
    functions["projectsRegionsAutoscalingPoliciesSetIamPolicy"] = dataproc.post(
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
    functions["projectsRegionsAutoscalingPoliciesList"] = dataproc.post(
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
    functions["projectsRegionsAutoscalingPoliciesCreate"] = dataproc.post(
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
    functions["projectsRegionsAutoscalingPoliciesGet"] = dataproc.post(
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
    functions["projectsRegionsAutoscalingPoliciesTestIamPermissions"] = dataproc.post(
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
    functions["projectsRegionsAutoscalingPoliciesGetIamPolicy"] = dataproc.post(
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

    return Import(
        importer="dataproc", renames=renames, types=Box(types), functions=Box(functions)
    )
