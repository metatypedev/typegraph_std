from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_securitycenter() -> Import:
    securitycenter = HTTPRuntime("https://securitycenter.googleapis.com/")

    renames = {
        "ErrorResponse": "_securitycenter_1_ErrorResponse",
        "GetPolicyOptionsIn": "_securitycenter_2_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_securitycenter_3_GetPolicyOptionsOut",
        "GoogleCloudSecuritycenterV1p1beta1FolderIn": "_securitycenter_4_GoogleCloudSecuritycenterV1p1beta1FolderIn",
        "GoogleCloudSecuritycenterV1p1beta1FolderOut": "_securitycenter_5_GoogleCloudSecuritycenterV1p1beta1FolderOut",
        "KubernetesIn": "_securitycenter_6_KubernetesIn",
        "KubernetesOut": "_securitycenter_7_KubernetesOut",
        "GoogleCloudSecuritycenterV1CustomOutputSpecIn": "_securitycenter_8_GoogleCloudSecuritycenterV1CustomOutputSpecIn",
        "GoogleCloudSecuritycenterV1CustomOutputSpecOut": "_securitycenter_9_GoogleCloudSecuritycenterV1CustomOutputSpecOut",
        "ProcessSignatureIn": "_securitycenter_10_ProcessSignatureIn",
        "ProcessSignatureOut": "_securitycenter_11_ProcessSignatureOut",
        "ListNotificationConfigsResponseIn": "_securitycenter_12_ListNotificationConfigsResponseIn",
        "ListNotificationConfigsResponseOut": "_securitycenter_13_ListNotificationConfigsResponseOut",
        "KernelRootkitIn": "_securitycenter_14_KernelRootkitIn",
        "KernelRootkitOut": "_securitycenter_15_KernelRootkitOut",
        "SetIamPolicyRequestIn": "_securitycenter_16_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_securitycenter_17_SetIamPolicyRequestOut",
        "ContactIn": "_securitycenter_18_ContactIn",
        "ContactOut": "_securitycenter_19_ContactOut",
        "SecurityMarksIn": "_securitycenter_20_SecurityMarksIn",
        "SecurityMarksOut": "_securitycenter_21_SecurityMarksOut",
        "GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseIn": "_securitycenter_22_GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseIn",
        "GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseOut": "_securitycenter_23_GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseOut",
        "SetFindingStateRequestIn": "_securitycenter_24_SetFindingStateRequestIn",
        "SetFindingStateRequestOut": "_securitycenter_25_SetFindingStateRequestOut",
        "GetIamPolicyRequestIn": "_securitycenter_26_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_securitycenter_27_GetIamPolicyRequestOut",
        "ConnectionIn": "_securitycenter_28_ConnectionIn",
        "ConnectionOut": "_securitycenter_29_ConnectionOut",
        "PolicyIn": "_securitycenter_30_PolicyIn",
        "PolicyOut": "_securitycenter_31_PolicyOut",
        "NotificationConfigIn": "_securitycenter_32_NotificationConfigIn",
        "NotificationConfigOut": "_securitycenter_33_NotificationConfigOut",
        "FolderIn": "_securitycenter_34_FolderIn",
        "FolderOut": "_securitycenter_35_FolderOut",
        "AccessReviewIn": "_securitycenter_36_AccessReviewIn",
        "AccessReviewOut": "_securitycenter_37_AccessReviewOut",
        "PodIn": "_securitycenter_38_PodIn",
        "PodOut": "_securitycenter_39_PodOut",
        "MitreAttackIn": "_securitycenter_40_MitreAttackIn",
        "MitreAttackOut": "_securitycenter_41_MitreAttackOut",
        "ListFindingsResponseIn": "_securitycenter_42_ListFindingsResponseIn",
        "ListFindingsResponseOut": "_securitycenter_43_ListFindingsResponseOut",
        "BulkMuteFindingsRequestIn": "_securitycenter_44_BulkMuteFindingsRequestIn",
        "BulkMuteFindingsRequestOut": "_securitycenter_45_BulkMuteFindingsRequestOut",
        "RunAssetDiscoveryRequestIn": "_securitycenter_46_RunAssetDiscoveryRequestIn",
        "RunAssetDiscoveryRequestOut": "_securitycenter_47_RunAssetDiscoveryRequestOut",
        "ListDescendantSecurityHealthAnalyticsCustomModulesResponseIn": "_securitycenter_48_ListDescendantSecurityHealthAnalyticsCustomModulesResponseIn",
        "ListDescendantSecurityHealthAnalyticsCustomModulesResponseOut": "_securitycenter_49_ListDescendantSecurityHealthAnalyticsCustomModulesResponseOut",
        "IamPolicyIn": "_securitycenter_50_IamPolicyIn",
        "IamPolicyOut": "_securitycenter_51_IamPolicyOut",
        "ListOperationsResponseIn": "_securitycenter_52_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_securitycenter_53_ListOperationsResponseOut",
        "AssetIn": "_securitycenter_54_AssetIn",
        "AssetOut": "_securitycenter_55_AssetOut",
        "SubjectIn": "_securitycenter_56_SubjectIn",
        "SubjectOut": "_securitycenter_57_SubjectOut",
        "GoogleCloudSecuritycenterV1MuteConfigIn": "_securitycenter_58_GoogleCloudSecuritycenterV1MuteConfigIn",
        "GoogleCloudSecuritycenterV1MuteConfigOut": "_securitycenter_59_GoogleCloudSecuritycenterV1MuteConfigOut",
        "ExprIn": "_securitycenter_60_ExprIn",
        "ExprOut": "_securitycenter_61_ExprOut",
        "ResourceIn": "_securitycenter_62_ResourceIn",
        "ResourceOut": "_securitycenter_63_ResourceOut",
        "CloudDlpInspectionIn": "_securitycenter_64_CloudDlpInspectionIn",
        "CloudDlpInspectionOut": "_securitycenter_65_CloudDlpInspectionOut",
        "GoogleCloudSecuritycenterV1BindingIn": "_securitycenter_66_GoogleCloudSecuritycenterV1BindingIn",
        "GoogleCloudSecuritycenterV1BindingOut": "_securitycenter_67_GoogleCloudSecuritycenterV1BindingOut",
        "DatabaseIn": "_securitycenter_68_DatabaseIn",
        "DatabaseOut": "_securitycenter_69_DatabaseOut",
        "NodePoolIn": "_securitycenter_70_NodePoolIn",
        "NodePoolOut": "_securitycenter_71_NodePoolOut",
        "GoogleCloudSecuritycenterV1BulkMuteFindingsResponseIn": "_securitycenter_72_GoogleCloudSecuritycenterV1BulkMuteFindingsResponseIn",
        "GoogleCloudSecuritycenterV1BulkMuteFindingsResponseOut": "_securitycenter_73_GoogleCloudSecuritycenterV1BulkMuteFindingsResponseOut",
        "FileIn": "_securitycenter_74_FileIn",
        "FileOut": "_securitycenter_75_FileOut",
        "GroupFindingsResponseIn": "_securitycenter_76_GroupFindingsResponseIn",
        "GroupFindingsResponseOut": "_securitycenter_77_GroupFindingsResponseOut",
        "MemoryHashSignatureIn": "_securitycenter_78_MemoryHashSignatureIn",
        "MemoryHashSignatureOut": "_securitycenter_79_MemoryHashSignatureOut",
        "CveIn": "_securitycenter_80_CveIn",
        "CveOut": "_securitycenter_81_CveOut",
        "StatusIn": "_securitycenter_82_StatusIn",
        "StatusOut": "_securitycenter_83_StatusOut",
        "AssetDiscoveryConfigIn": "_securitycenter_84_AssetDiscoveryConfigIn",
        "AssetDiscoveryConfigOut": "_securitycenter_85_AssetDiscoveryConfigOut",
        "ListFindingsResultIn": "_securitycenter_86_ListFindingsResultIn",
        "ListFindingsResultOut": "_securitycenter_87_ListFindingsResultOut",
        "GoogleCloudSecuritycenterV1p1beta1SecurityMarksIn": "_securitycenter_88_GoogleCloudSecuritycenterV1p1beta1SecurityMarksIn",
        "GoogleCloudSecuritycenterV1p1beta1SecurityMarksOut": "_securitycenter_89_GoogleCloudSecuritycenterV1p1beta1SecurityMarksOut",
        "TestIamPermissionsResponseIn": "_securitycenter_90_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_securitycenter_91_TestIamPermissionsResponseOut",
        "ComplianceIn": "_securitycenter_92_ComplianceIn",
        "ComplianceOut": "_securitycenter_93_ComplianceOut",
        "GroupFindingsRequestIn": "_securitycenter_94_GroupFindingsRequestIn",
        "GroupFindingsRequestOut": "_securitycenter_95_GroupFindingsRequestOut",
        "AccessIn": "_securitycenter_96_AccessIn",
        "AccessOut": "_securitycenter_97_AccessOut",
        "GoogleCloudSecuritycenterV1ResourceIn": "_securitycenter_98_GoogleCloudSecuritycenterV1ResourceIn",
        "GoogleCloudSecuritycenterV1ResourceOut": "_securitycenter_99_GoogleCloudSecuritycenterV1ResourceOut",
        "ListSourcesResponseIn": "_securitycenter_100_ListSourcesResponseIn",
        "ListSourcesResponseOut": "_securitycenter_101_ListSourcesResponseOut",
        "LabelIn": "_securitycenter_102_LabelIn",
        "LabelOut": "_securitycenter_103_LabelOut",
        "GoogleCloudSecuritycenterV1p1beta1ResourceIn": "_securitycenter_104_GoogleCloudSecuritycenterV1p1beta1ResourceIn",
        "GoogleCloudSecuritycenterV1p1beta1ResourceOut": "_securitycenter_105_GoogleCloudSecuritycenterV1p1beta1ResourceOut",
        "IamBindingIn": "_securitycenter_106_IamBindingIn",
        "IamBindingOut": "_securitycenter_107_IamBindingOut",
        "ReferenceIn": "_securitycenter_108_ReferenceIn",
        "ReferenceOut": "_securitycenter_109_ReferenceOut",
        "ContactDetailsIn": "_securitycenter_110_ContactDetailsIn",
        "ContactDetailsOut": "_securitycenter_111_ContactDetailsOut",
        "SecurityCenterPropertiesIn": "_securitycenter_112_SecurityCenterPropertiesIn",
        "SecurityCenterPropertiesOut": "_securitycenter_113_SecurityCenterPropertiesOut",
        "OperationIn": "_securitycenter_114_OperationIn",
        "OperationOut": "_securitycenter_115_OperationOut",
        "Cvssv3In": "_securitycenter_116_Cvssv3In",
        "Cvssv3Out": "_securitycenter_117_Cvssv3Out",
        "GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseIn": "_securitycenter_118_GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseIn",
        "GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseOut": "_securitycenter_119_GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseOut",
        "GoogleCloudSecuritycenterV1NotificationMessageIn": "_securitycenter_120_GoogleCloudSecuritycenterV1NotificationMessageIn",
        "GoogleCloudSecuritycenterV1NotificationMessageOut": "_securitycenter_121_GoogleCloudSecuritycenterV1NotificationMessageOut",
        "GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseIn": "_securitycenter_122_GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseIn",
        "GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseOut": "_securitycenter_123_GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseOut",
        "AuditConfigIn": "_securitycenter_124_AuditConfigIn",
        "AuditConfigOut": "_securitycenter_125_AuditConfigOut",
        "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleIn": "_securitycenter_126_GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleIn",
        "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleOut": "_securitycenter_127_GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleOut",
        "IndicatorIn": "_securitycenter_128_IndicatorIn",
        "IndicatorOut": "_securitycenter_129_IndicatorOut",
        "ListSecurityHealthAnalyticsCustomModulesResponseIn": "_securitycenter_130_ListSecurityHealthAnalyticsCustomModulesResponseIn",
        "ListSecurityHealthAnalyticsCustomModulesResponseOut": "_securitycenter_131_ListSecurityHealthAnalyticsCustomModulesResponseOut",
        "ProcessIn": "_securitycenter_132_ProcessIn",
        "ProcessOut": "_securitycenter_133_ProcessOut",
        "ListBigQueryExportsResponseIn": "_securitycenter_134_ListBigQueryExportsResponseIn",
        "ListBigQueryExportsResponseOut": "_securitycenter_135_ListBigQueryExportsResponseOut",
        "ListAssetsResultIn": "_securitycenter_136_ListAssetsResultIn",
        "ListAssetsResultOut": "_securitycenter_137_ListAssetsResultOut",
        "TestIamPermissionsRequestIn": "_securitycenter_138_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_securitycenter_139_TestIamPermissionsRequestOut",
        "GoogleCloudSecuritycenterV1BigQueryExportIn": "_securitycenter_140_GoogleCloudSecuritycenterV1BigQueryExportIn",
        "GoogleCloudSecuritycenterV1BigQueryExportOut": "_securitycenter_141_GoogleCloudSecuritycenterV1BigQueryExportOut",
        "GroupAssetsResponseIn": "_securitycenter_142_GroupAssetsResponseIn",
        "GroupAssetsResponseOut": "_securitycenter_143_GroupAssetsResponseOut",
        "GeolocationIn": "_securitycenter_144_GeolocationIn",
        "GeolocationOut": "_securitycenter_145_GeolocationOut",
        "AuditLogConfigIn": "_securitycenter_146_AuditLogConfigIn",
        "AuditLogConfigOut": "_securitycenter_147_AuditLogConfigOut",
        "GoogleCloudSecuritycenterV1ResourceSelectorIn": "_securitycenter_148_GoogleCloudSecuritycenterV1ResourceSelectorIn",
        "GoogleCloudSecuritycenterV1ResourceSelectorOut": "_securitycenter_149_GoogleCloudSecuritycenterV1ResourceSelectorOut",
        "GoogleCloudSecuritycenterV1p1beta1NotificationMessageIn": "_securitycenter_150_GoogleCloudSecuritycenterV1p1beta1NotificationMessageIn",
        "GoogleCloudSecuritycenterV1p1beta1NotificationMessageOut": "_securitycenter_151_GoogleCloudSecuritycenterV1p1beta1NotificationMessageOut",
        "GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleIn": "_securitycenter_152_GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleIn",
        "GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut": "_securitycenter_153_GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut",
        "SetMuteRequestIn": "_securitycenter_154_SetMuteRequestIn",
        "SetMuteRequestOut": "_securitycenter_155_SetMuteRequestOut",
        "GoogleCloudSecuritycenterV1PropertyIn": "_securitycenter_156_GoogleCloudSecuritycenterV1PropertyIn",
        "GoogleCloudSecuritycenterV1PropertyOut": "_securitycenter_157_GoogleCloudSecuritycenterV1PropertyOut",
        "ListEffectiveSecurityHealthAnalyticsCustomModulesResponseIn": "_securitycenter_158_ListEffectiveSecurityHealthAnalyticsCustomModulesResponseIn",
        "ListEffectiveSecurityHealthAnalyticsCustomModulesResponseOut": "_securitycenter_159_ListEffectiveSecurityHealthAnalyticsCustomModulesResponseOut",
        "OrganizationSettingsIn": "_securitycenter_160_OrganizationSettingsIn",
        "OrganizationSettingsOut": "_securitycenter_161_OrganizationSettingsOut",
        "RoleIn": "_securitycenter_162_RoleIn",
        "RoleOut": "_securitycenter_163_RoleOut",
        "GoogleCloudSecuritycenterV1ExternalSystemIn": "_securitycenter_164_GoogleCloudSecuritycenterV1ExternalSystemIn",
        "GoogleCloudSecuritycenterV1ExternalSystemOut": "_securitycenter_165_GoogleCloudSecuritycenterV1ExternalSystemOut",
        "ContainerIn": "_securitycenter_166_ContainerIn",
        "ContainerOut": "_securitycenter_167_ContainerOut",
        "ExfiltrationIn": "_securitycenter_168_ExfiltrationIn",
        "ExfiltrationOut": "_securitycenter_169_ExfiltrationOut",
        "GoogleCloudSecuritycenterV1p1beta1FindingIn": "_securitycenter_170_GoogleCloudSecuritycenterV1p1beta1FindingIn",
        "GoogleCloudSecuritycenterV1p1beta1FindingOut": "_securitycenter_171_GoogleCloudSecuritycenterV1p1beta1FindingOut",
        "EnvironmentVariableIn": "_securitycenter_172_EnvironmentVariableIn",
        "EnvironmentVariableOut": "_securitycenter_173_EnvironmentVariableOut",
        "StreamingConfigIn": "_securitycenter_174_StreamingConfigIn",
        "StreamingConfigOut": "_securitycenter_175_StreamingConfigOut",
        "GroupAssetsRequestIn": "_securitycenter_176_GroupAssetsRequestIn",
        "GroupAssetsRequestOut": "_securitycenter_177_GroupAssetsRequestOut",
        "GroupResultIn": "_securitycenter_178_GroupResultIn",
        "GroupResultOut": "_securitycenter_179_GroupResultOut",
        "BindingIn": "_securitycenter_180_BindingIn",
        "BindingOut": "_securitycenter_181_BindingOut",
        "FindingIn": "_securitycenter_182_FindingIn",
        "FindingOut": "_securitycenter_183_FindingOut",
        "CloudDlpDataProfileIn": "_securitycenter_184_CloudDlpDataProfileIn",
        "CloudDlpDataProfileOut": "_securitycenter_185_CloudDlpDataProfileOut",
        "YaraRuleSignatureIn": "_securitycenter_186_YaraRuleSignatureIn",
        "YaraRuleSignatureOut": "_securitycenter_187_YaraRuleSignatureOut",
        "ExfilResourceIn": "_securitycenter_188_ExfilResourceIn",
        "ExfilResourceOut": "_securitycenter_189_ExfilResourceOut",
        "ServiceAccountDelegationInfoIn": "_securitycenter_190_ServiceAccountDelegationInfoIn",
        "ServiceAccountDelegationInfoOut": "_securitycenter_191_ServiceAccountDelegationInfoOut",
        "EmptyIn": "_securitycenter_192_EmptyIn",
        "EmptyOut": "_securitycenter_193_EmptyOut",
        "SourceIn": "_securitycenter_194_SourceIn",
        "SourceOut": "_securitycenter_195_SourceOut",
        "NodeIn": "_securitycenter_196_NodeIn",
        "NodeOut": "_securitycenter_197_NodeOut",
        "ListAssetsResponseIn": "_securitycenter_198_ListAssetsResponseIn",
        "ListAssetsResponseOut": "_securitycenter_199_ListAssetsResponseOut",
        "DetectionIn": "_securitycenter_200_DetectionIn",
        "DetectionOut": "_securitycenter_201_DetectionOut",
        "VulnerabilityIn": "_securitycenter_202_VulnerabilityIn",
        "VulnerabilityOut": "_securitycenter_203_VulnerabilityOut",
        "ListMuteConfigsResponseIn": "_securitycenter_204_ListMuteConfigsResponseIn",
        "ListMuteConfigsResponseOut": "_securitycenter_205_ListMuteConfigsResponseOut",
        "GoogleCloudSecuritycenterV1CustomConfigIn": "_securitycenter_206_GoogleCloudSecuritycenterV1CustomConfigIn",
        "GoogleCloudSecuritycenterV1CustomConfigOut": "_securitycenter_207_GoogleCloudSecuritycenterV1CustomConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["GoogleCloudSecuritycenterV1p1beta1FolderIn"] = t.struct(
        {
            "resourceFolder": t.string().optional(),
            "resourceFolderDisplayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1FolderIn"])
    types["GoogleCloudSecuritycenterV1p1beta1FolderOut"] = t.struct(
        {
            "resourceFolder": t.string().optional(),
            "resourceFolderDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1FolderOut"])
    types["KubernetesIn"] = t.struct(
        {
            "nodes": t.array(t.proxy(renames["NodeIn"])).optional(),
            "roles": t.array(t.proxy(renames["RoleIn"])).optional(),
            "accessReviews": t.array(t.proxy(renames["AccessReviewIn"])).optional(),
            "pods": t.array(t.proxy(renames["PodIn"])).optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolIn"])).optional(),
            "bindings": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1BindingIn"])
            ).optional(),
        }
    ).named(renames["KubernetesIn"])
    types["KubernetesOut"] = t.struct(
        {
            "nodes": t.array(t.proxy(renames["NodeOut"])).optional(),
            "roles": t.array(t.proxy(renames["RoleOut"])).optional(),
            "accessReviews": t.array(t.proxy(renames["AccessReviewOut"])).optional(),
            "pods": t.array(t.proxy(renames["PodOut"])).optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolOut"])).optional(),
            "bindings": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1BindingOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesOut"])
    types["GoogleCloudSecuritycenterV1CustomOutputSpecIn"] = t.struct(
        {
            "properties": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1PropertyIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudSecuritycenterV1CustomOutputSpecIn"])
    types["GoogleCloudSecuritycenterV1CustomOutputSpecOut"] = t.struct(
        {
            "properties": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1PropertyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1CustomOutputSpecOut"])
    types["ProcessSignatureIn"] = t.struct(
        {
            "memoryHashSignature": t.proxy(renames["MemoryHashSignatureIn"]).optional(),
            "yaraRuleSignature": t.proxy(renames["YaraRuleSignatureIn"]).optional(),
        }
    ).named(renames["ProcessSignatureIn"])
    types["ProcessSignatureOut"] = t.struct(
        {
            "memoryHashSignature": t.proxy(
                renames["MemoryHashSignatureOut"]
            ).optional(),
            "yaraRuleSignature": t.proxy(renames["YaraRuleSignatureOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProcessSignatureOut"])
    types["ListNotificationConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "notificationConfigs": t.array(
                t.proxy(renames["NotificationConfigIn"])
            ).optional(),
        }
    ).named(renames["ListNotificationConfigsResponseIn"])
    types["ListNotificationConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "notificationConfigs": t.array(
                t.proxy(renames["NotificationConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNotificationConfigsResponseOut"])
    types["KernelRootkitIn"] = t.struct(
        {
            "unexpectedKprobeHandler": t.boolean().optional(),
            "unexpectedSystemCallHandler": t.boolean().optional(),
            "unexpectedFtraceHandler": t.boolean().optional(),
            "unexpectedProcessesInRunqueue": t.boolean().optional(),
            "unexpectedKernelCodePages": t.boolean().optional(),
            "unexpectedCodeModification": t.boolean().optional(),
            "unexpectedInterruptHandler": t.boolean().optional(),
            "name": t.string().optional(),
            "unexpectedReadOnlyDataModification": t.boolean().optional(),
        }
    ).named(renames["KernelRootkitIn"])
    types["KernelRootkitOut"] = t.struct(
        {
            "unexpectedKprobeHandler": t.boolean().optional(),
            "unexpectedSystemCallHandler": t.boolean().optional(),
            "unexpectedFtraceHandler": t.boolean().optional(),
            "unexpectedProcessesInRunqueue": t.boolean().optional(),
            "unexpectedKernelCodePages": t.boolean().optional(),
            "unexpectedCodeModification": t.boolean().optional(),
            "unexpectedInterruptHandler": t.boolean().optional(),
            "name": t.string().optional(),
            "unexpectedReadOnlyDataModification": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KernelRootkitOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["ContactIn"] = t.struct({"email": t.string().optional()}).named(
        renames["ContactIn"]
    )
    types["ContactOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactOut"])
    types["SecurityMarksIn"] = t.struct(
        {
            "marks": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "canonicalName": t.string().optional(),
        }
    ).named(renames["SecurityMarksIn"])
    types["SecurityMarksOut"] = t.struct(
        {
            "marks": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "canonicalName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecurityMarksOut"])
    types["GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseIn"] = t.struct(
        {"state": t.string().optional(), "duration": t.string().optional()}
    ).named(renames["GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseIn"])
    types["GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseOut"] = t.struct(
        {
            "state": t.string().optional(),
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseOut"])
    types["SetFindingStateRequestIn"] = t.struct(
        {"state": t.string(), "startTime": t.string()}
    ).named(renames["SetFindingStateRequestIn"])
    types["SetFindingStateRequestOut"] = t.struct(
        {
            "state": t.string(),
            "startTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetFindingStateRequestOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["ConnectionIn"] = t.struct(
        {
            "destinationPort": t.integer().optional(),
            "sourcePort": t.integer().optional(),
            "destinationIp": t.string().optional(),
            "sourceIp": t.string().optional(),
            "protocol": t.string().optional(),
        }
    ).named(renames["ConnectionIn"])
    types["ConnectionOut"] = t.struct(
        {
            "destinationPort": t.integer().optional(),
            "sourcePort": t.integer().optional(),
            "destinationIp": t.string().optional(),
            "sourceIp": t.string().optional(),
            "protocol": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["NotificationConfigIn"] = t.struct(
        {
            "streamingConfig": t.proxy(renames["StreamingConfigIn"]).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "pubsubTopic": t.string().optional(),
        }
    ).named(renames["NotificationConfigIn"])
    types["NotificationConfigOut"] = t.struct(
        {
            "streamingConfig": t.proxy(renames["StreamingConfigOut"]).optional(),
            "name": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "description": t.string().optional(),
            "pubsubTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationConfigOut"])
    types["FolderIn"] = t.struct(
        {
            "resourceFolderDisplayName": t.string().optional(),
            "resourceFolder": t.string().optional(),
        }
    ).named(renames["FolderIn"])
    types["FolderOut"] = t.struct(
        {
            "resourceFolderDisplayName": t.string().optional(),
            "resourceFolder": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOut"])
    types["AccessReviewIn"] = t.struct(
        {
            "subresource": t.string().optional(),
            "ns": t.string().optional(),
            "version": t.string().optional(),
            "name": t.string().optional(),
            "resource": t.string().optional(),
            "group": t.string().optional(),
            "verb": t.string().optional(),
        }
    ).named(renames["AccessReviewIn"])
    types["AccessReviewOut"] = t.struct(
        {
            "subresource": t.string().optional(),
            "ns": t.string().optional(),
            "version": t.string().optional(),
            "name": t.string().optional(),
            "resource": t.string().optional(),
            "group": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessReviewOut"])
    types["PodIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelIn"])).optional(),
            "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
            "ns": t.string().optional(),
        }
    ).named(renames["PodIn"])
    types["PodOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelOut"])).optional(),
            "containers": t.array(t.proxy(renames["ContainerOut"])).optional(),
            "ns": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PodOut"])
    types["MitreAttackIn"] = t.struct(
        {
            "primaryTechniques": t.array(t.string()).optional(),
            "version": t.string().optional(),
            "additionalTactics": t.array(t.string()).optional(),
            "additionalTechniques": t.array(t.string()).optional(),
            "primaryTactic": t.string().optional(),
        }
    ).named(renames["MitreAttackIn"])
    types["MitreAttackOut"] = t.struct(
        {
            "primaryTechniques": t.array(t.string()).optional(),
            "version": t.string().optional(),
            "additionalTactics": t.array(t.string()).optional(),
            "additionalTechniques": t.array(t.string()).optional(),
            "primaryTactic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MitreAttackOut"])
    types["ListFindingsResponseIn"] = t.struct(
        {
            "readTime": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "listFindingsResults": t.array(
                t.proxy(renames["ListFindingsResultIn"])
            ).optional(),
        }
    ).named(renames["ListFindingsResponseIn"])
    types["ListFindingsResponseOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "listFindingsResults": t.array(
                t.proxy(renames["ListFindingsResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFindingsResponseOut"])
    types["BulkMuteFindingsRequestIn"] = t.struct(
        {"muteAnnotation": t.string().optional(), "filter": t.string().optional()}
    ).named(renames["BulkMuteFindingsRequestIn"])
    types["BulkMuteFindingsRequestOut"] = t.struct(
        {
            "muteAnnotation": t.string().optional(),
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkMuteFindingsRequestOut"])
    types["RunAssetDiscoveryRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RunAssetDiscoveryRequestIn"]
    )
    types["RunAssetDiscoveryRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RunAssetDiscoveryRequestOut"])
    types["ListDescendantSecurityHealthAnalyticsCustomModulesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "securityHealthAnalyticsCustomModules": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["ListDescendantSecurityHealthAnalyticsCustomModulesResponseIn"])
    types["ListDescendantSecurityHealthAnalyticsCustomModulesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "securityHealthAnalyticsCustomModules": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDescendantSecurityHealthAnalyticsCustomModulesResponseOut"])
    types["IamPolicyIn"] = t.struct({"policyBlob": t.string().optional()}).named(
        renames["IamPolicyIn"]
    )
    types["IamPolicyOut"] = t.struct(
        {
            "policyBlob": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyOut"])
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
    types["AssetIn"] = t.struct(
        {
            "securityMarks": t.proxy(renames["SecurityMarksIn"]).optional(),
            "createTime": t.string().optional(),
            "resourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "iamPolicy": t.proxy(renames["IamPolicyIn"]).optional(),
            "name": t.string().optional(),
            "securityCenterProperties": t.proxy(
                renames["SecurityCenterPropertiesIn"]
            ).optional(),
            "canonicalName": t.string().optional(),
        }
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "securityMarks": t.proxy(renames["SecurityMarksOut"]).optional(),
            "createTime": t.string().optional(),
            "resourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "iamPolicy": t.proxy(renames["IamPolicyOut"]).optional(),
            "name": t.string().optional(),
            "securityCenterProperties": t.proxy(
                renames["SecurityCenterPropertiesOut"]
            ).optional(),
            "canonicalName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
    types["SubjectIn"] = t.struct(
        {
            "ns": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SubjectIn"])
    types["SubjectOut"] = t.struct(
        {
            "ns": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubjectOut"])
    types["GoogleCloudSecuritycenterV1MuteConfigIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "filter": t.string(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1MuteConfigIn"])
    types["GoogleCloudSecuritycenterV1MuteConfigOut"] = t.struct(
        {
            "mostRecentEditor": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "filter": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1MuteConfigOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ResourceIn"] = t.struct(
        {
            "projectDisplayName": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderIn"])).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "parentDisplayName": t.string().optional(),
            "parentName": t.string().optional(),
            "displayName": t.string().optional(),
            "projectName": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "projectDisplayName": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderOut"])).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "parentDisplayName": t.string().optional(),
            "parentName": t.string().optional(),
            "displayName": t.string().optional(),
            "projectName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
    types["CloudDlpInspectionIn"] = t.struct(
        {
            "infoType": t.string().optional(),
            "inspectJob": t.string().optional(),
            "fullScan": t.boolean().optional(),
            "infoTypeCount": t.string().optional(),
        }
    ).named(renames["CloudDlpInspectionIn"])
    types["CloudDlpInspectionOut"] = t.struct(
        {
            "infoType": t.string().optional(),
            "inspectJob": t.string().optional(),
            "fullScan": t.boolean().optional(),
            "infoTypeCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudDlpInspectionOut"])
    types["GoogleCloudSecuritycenterV1BindingIn"] = t.struct(
        {
            "ns": t.string().optional(),
            "name": t.string().optional(),
            "subjects": t.array(t.proxy(renames["SubjectIn"])).optional(),
            "role": t.proxy(renames["RoleIn"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1BindingIn"])
    types["GoogleCloudSecuritycenterV1BindingOut"] = t.struct(
        {
            "ns": t.string().optional(),
            "name": t.string().optional(),
            "subjects": t.array(t.proxy(renames["SubjectOut"])).optional(),
            "role": t.proxy(renames["RoleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1BindingOut"])
    types["DatabaseIn"] = t.struct(
        {
            "userName": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "grantees": t.array(t.string()).optional(),
            "query": t.string().optional(),
        }
    ).named(renames["DatabaseIn"])
    types["DatabaseOut"] = t.struct(
        {
            "userName": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "grantees": t.array(t.string()).optional(),
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseOut"])
    types["NodePoolIn"] = t.struct(
        {
            "nodes": t.array(t.proxy(renames["NodeIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["NodePoolIn"])
    types["NodePoolOut"] = t.struct(
        {
            "nodes": t.array(t.proxy(renames["NodeOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolOut"])
    types["GoogleCloudSecuritycenterV1BulkMuteFindingsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudSecuritycenterV1BulkMuteFindingsResponseIn"])
    types["GoogleCloudSecuritycenterV1BulkMuteFindingsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudSecuritycenterV1BulkMuteFindingsResponseOut"])
    types["FileIn"] = t.struct(
        {
            "contents": t.string().optional(),
            "partiallyHashed": t.boolean().optional(),
            "size": t.string().optional(),
            "sha256": t.string().optional(),
            "path": t.string().optional(),
            "hashedSize": t.string().optional(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "contents": t.string().optional(),
            "partiallyHashed": t.boolean().optional(),
            "size": t.string().optional(),
            "sha256": t.string().optional(),
            "path": t.string().optional(),
            "hashedSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
    types["GroupFindingsResponseIn"] = t.struct(
        {
            "groupByResults": t.array(t.proxy(renames["GroupResultIn"])).optional(),
            "totalSize": t.integer().optional(),
            "readTime": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GroupFindingsResponseIn"])
    types["GroupFindingsResponseOut"] = t.struct(
        {
            "groupByResults": t.array(t.proxy(renames["GroupResultOut"])).optional(),
            "totalSize": t.integer().optional(),
            "readTime": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupFindingsResponseOut"])
    types["MemoryHashSignatureIn"] = t.struct(
        {
            "detections": t.array(t.proxy(renames["DetectionIn"])).optional(),
            "binaryFamily": t.string().optional(),
        }
    ).named(renames["MemoryHashSignatureIn"])
    types["MemoryHashSignatureOut"] = t.struct(
        {
            "detections": t.array(t.proxy(renames["DetectionOut"])).optional(),
            "binaryFamily": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemoryHashSignatureOut"])
    types["CveIn"] = t.struct(
        {
            "references": t.array(t.proxy(renames["ReferenceIn"])).optional(),
            "cvssv3": t.proxy(renames["Cvssv3In"]).optional(),
            "upstreamFixAvailable": t.boolean().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["CveIn"])
    types["CveOut"] = t.struct(
        {
            "references": t.array(t.proxy(renames["ReferenceOut"])).optional(),
            "cvssv3": t.proxy(renames["Cvssv3Out"]).optional(),
            "upstreamFixAvailable": t.boolean().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CveOut"])
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
    types["AssetDiscoveryConfigIn"] = t.struct(
        {
            "folderIds": t.array(t.string()).optional(),
            "inclusionMode": t.string().optional(),
            "projectIds": t.array(t.string()).optional(),
        }
    ).named(renames["AssetDiscoveryConfigIn"])
    types["AssetDiscoveryConfigOut"] = t.struct(
        {
            "folderIds": t.array(t.string()).optional(),
            "inclusionMode": t.string().optional(),
            "projectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetDiscoveryConfigOut"])
    types["ListFindingsResultIn"] = t.struct(
        {
            "finding": t.proxy(renames["FindingIn"]).optional(),
            "stateChange": t.string().optional(),
        }
    ).named(renames["ListFindingsResultIn"])
    types["ListFindingsResultOut"] = t.struct(
        {
            "finding": t.proxy(renames["FindingOut"]).optional(),
            "stateChange": t.string().optional(),
            "resource": t.proxy(renames["ResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFindingsResultOut"])
    types["GoogleCloudSecuritycenterV1p1beta1SecurityMarksIn"] = t.struct(
        {
            "marks": t.struct({"_": t.string().optional()}).optional(),
            "canonicalName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1SecurityMarksIn"])
    types["GoogleCloudSecuritycenterV1p1beta1SecurityMarksOut"] = t.struct(
        {
            "marks": t.struct({"_": t.string().optional()}).optional(),
            "canonicalName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1SecurityMarksOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ComplianceIn"] = t.struct(
        {
            "standard": t.string().optional(),
            "version": t.string().optional(),
            "ids": t.array(t.string()).optional(),
        }
    ).named(renames["ComplianceIn"])
    types["ComplianceOut"] = t.struct(
        {
            "standard": t.string().optional(),
            "version": t.string().optional(),
            "ids": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComplianceOut"])
    types["GroupFindingsRequestIn"] = t.struct(
        {
            "groupBy": t.string(),
            "pageSize": t.integer().optional(),
            "compareDuration": t.string().optional(),
            "readTime": t.string().optional(),
            "filter": t.string().optional(),
            "pageToken": t.string().optional(),
        }
    ).named(renames["GroupFindingsRequestIn"])
    types["GroupFindingsRequestOut"] = t.struct(
        {
            "groupBy": t.string(),
            "pageSize": t.integer().optional(),
            "compareDuration": t.string().optional(),
            "readTime": t.string().optional(),
            "filter": t.string().optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupFindingsRequestOut"])
    types["AccessIn"] = t.struct(
        {
            "principalEmail": t.string().optional(),
            "methodName": t.string().optional(),
            "callerIp": t.string().optional(),
            "serviceName": t.string().optional(),
            "userAgentFamily": t.string().optional(),
            "serviceAccountDelegationInfo": t.array(
                t.proxy(renames["ServiceAccountDelegationInfoIn"])
            ).optional(),
            "principalSubject": t.string().optional(),
            "serviceAccountKeyName": t.string().optional(),
            "userName": t.string().optional(),
            "callerIpGeo": t.proxy(renames["GeolocationIn"]).optional(),
        }
    ).named(renames["AccessIn"])
    types["AccessOut"] = t.struct(
        {
            "principalEmail": t.string().optional(),
            "methodName": t.string().optional(),
            "callerIp": t.string().optional(),
            "serviceName": t.string().optional(),
            "userAgentFamily": t.string().optional(),
            "serviceAccountDelegationInfo": t.array(
                t.proxy(renames["ServiceAccountDelegationInfoOut"])
            ).optional(),
            "principalSubject": t.string().optional(),
            "serviceAccountKeyName": t.string().optional(),
            "userName": t.string().optional(),
            "callerIpGeo": t.proxy(renames["GeolocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessOut"])
    types["GoogleCloudSecuritycenterV1ResourceIn"] = t.struct(
        {
            "project": t.string().optional(),
            "parentDisplayName": t.string().optional(),
            "parent": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "projectDisplayName": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ResourceIn"])
    types["GoogleCloudSecuritycenterV1ResourceOut"] = t.struct(
        {
            "project": t.string().optional(),
            "parentDisplayName": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderOut"])).optional(),
            "parent": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "projectDisplayName": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ResourceOut"])
    types["ListSourcesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
        }
    ).named(renames["ListSourcesResponseIn"])
    types["ListSourcesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSourcesResponseOut"])
    types["LabelIn"] = t.struct(
        {"name": t.string().optional(), "value": t.string().optional()}
    ).named(renames["LabelIn"])
    types["LabelOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelOut"])
    types["GoogleCloudSecuritycenterV1p1beta1ResourceIn"] = t.struct(
        {
            "project": t.string().optional(),
            "projectDisplayName": t.string().optional(),
            "parent": t.string().optional(),
            "parentDisplayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1ResourceIn"])
    types["GoogleCloudSecuritycenterV1p1beta1ResourceOut"] = t.struct(
        {
            "project": t.string().optional(),
            "projectDisplayName": t.string().optional(),
            "parent": t.string().optional(),
            "parentDisplayName": t.string().optional(),
            "folders": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1p1beta1FolderOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1ResourceOut"])
    types["IamBindingIn"] = t.struct(
        {
            "action": t.string().optional(),
            "role": t.string().optional(),
            "member": t.string().optional(),
        }
    ).named(renames["IamBindingIn"])
    types["IamBindingOut"] = t.struct(
        {
            "action": t.string().optional(),
            "role": t.string().optional(),
            "member": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamBindingOut"])
    types["ReferenceIn"] = t.struct(
        {"uri": t.string().optional(), "source": t.string().optional()}
    ).named(renames["ReferenceIn"])
    types["ReferenceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "source": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReferenceOut"])
    types["ContactDetailsIn"] = t.struct(
        {"contacts": t.array(t.proxy(renames["ContactIn"])).optional()}
    ).named(renames["ContactDetailsIn"])
    types["ContactDetailsOut"] = t.struct(
        {
            "contacts": t.array(t.proxy(renames["ContactOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactDetailsOut"])
    types["SecurityCenterPropertiesIn"] = t.struct(
        {
            "folders": t.array(t.proxy(renames["FolderIn"])).optional(),
            "resourceOwners": t.array(t.string()).optional(),
            "resourceParentDisplayName": t.string().optional(),
            "resourceProject": t.string().optional(),
            "resourceParent": t.string().optional(),
            "resourceName": t.string().optional(),
            "resourceProjectDisplayName": t.string().optional(),
            "resourceType": t.string().optional(),
            "resourceDisplayName": t.string().optional(),
        }
    ).named(renames["SecurityCenterPropertiesIn"])
    types["SecurityCenterPropertiesOut"] = t.struct(
        {
            "folders": t.array(t.proxy(renames["FolderOut"])).optional(),
            "resourceOwners": t.array(t.string()).optional(),
            "resourceParentDisplayName": t.string().optional(),
            "resourceProject": t.string().optional(),
            "resourceParent": t.string().optional(),
            "resourceName": t.string().optional(),
            "resourceProjectDisplayName": t.string().optional(),
            "resourceType": t.string().optional(),
            "resourceDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecurityCenterPropertiesOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["Cvssv3In"] = t.struct(
        {
            "confidentialityImpact": t.string().optional(),
            "privilegesRequired": t.string().optional(),
            "integrityImpact": t.string().optional(),
            "attackVector": t.string().optional(),
            "attackComplexity": t.string().optional(),
            "baseScore": t.number().optional(),
            "availabilityImpact": t.string().optional(),
            "userInteraction": t.string().optional(),
            "scope": t.string().optional(),
        }
    ).named(renames["Cvssv3In"])
    types["Cvssv3Out"] = t.struct(
        {
            "confidentialityImpact": t.string().optional(),
            "privilegesRequired": t.string().optional(),
            "integrityImpact": t.string().optional(),
            "attackVector": t.string().optional(),
            "attackComplexity": t.string().optional(),
            "baseScore": t.number().optional(),
            "availabilityImpact": t.string().optional(),
            "userInteraction": t.string().optional(),
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Cvssv3Out"])
    types["GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseIn"] = t.struct(
        {"state": t.string().optional(), "duration": t.string().optional()}
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseIn"])
    types["GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseOut"] = t.struct(
        {
            "state": t.string().optional(),
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseOut"])
    types["GoogleCloudSecuritycenterV1NotificationMessageIn"] = t.struct(
        {
            "finding": t.proxy(renames["FindingIn"]).optional(),
            "notificationConfigName": t.string().optional(),
            "resource": t.proxy(
                renames["GoogleCloudSecuritycenterV1ResourceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1NotificationMessageIn"])
    types["GoogleCloudSecuritycenterV1NotificationMessageOut"] = t.struct(
        {
            "finding": t.proxy(renames["FindingOut"]).optional(),
            "notificationConfigName": t.string().optional(),
            "resource": t.proxy(
                renames["GoogleCloudSecuritycenterV1ResourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1NotificationMessageOut"])
    types["GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseIn"] = t.struct(
        {"state": t.string().optional(), "duration": t.string().optional()}
    ).named(renames["GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseIn"])
    types["GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseOut"] = t.struct(
        {
            "state": t.string().optional(),
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types[
        "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames[
            "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleIn"
        ]
    )
    types[
        "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleOut"
    ] = t.struct(
        {
            "enablementState": t.string().optional(),
            "name": t.string().optional(),
            "customConfig": t.proxy(
                renames["GoogleCloudSecuritycenterV1CustomConfigOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleOut"
        ]
    )
    types["IndicatorIn"] = t.struct(
        {
            "uris": t.array(t.string()).optional(),
            "signatures": t.array(t.proxy(renames["ProcessSignatureIn"])).optional(),
            "domains": t.array(t.string()).optional(),
            "ipAddresses": t.array(t.string()).optional(),
        }
    ).named(renames["IndicatorIn"])
    types["IndicatorOut"] = t.struct(
        {
            "uris": t.array(t.string()).optional(),
            "signatures": t.array(t.proxy(renames["ProcessSignatureOut"])).optional(),
            "domains": t.array(t.string()).optional(),
            "ipAddresses": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndicatorOut"])
    types["ListSecurityHealthAnalyticsCustomModulesResponseIn"] = t.struct(
        {
            "securityHealthAnalyticsCustomModules": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleIn"
                    ]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSecurityHealthAnalyticsCustomModulesResponseIn"])
    types["ListSecurityHealthAnalyticsCustomModulesResponseOut"] = t.struct(
        {
            "securityHealthAnalyticsCustomModules": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"
                    ]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSecurityHealthAnalyticsCustomModulesResponseOut"])
    types["ProcessIn"] = t.struct(
        {
            "envVariables": t.array(
                t.proxy(renames["EnvironmentVariableIn"])
            ).optional(),
            "parentPid": t.string().optional(),
            "pid": t.string().optional(),
            "script": t.proxy(renames["FileIn"]).optional(),
            "libraries": t.array(t.proxy(renames["FileIn"])).optional(),
            "args": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "binary": t.proxy(renames["FileIn"]).optional(),
            "envVariablesTruncated": t.boolean().optional(),
            "argumentsTruncated": t.boolean().optional(),
        }
    ).named(renames["ProcessIn"])
    types["ProcessOut"] = t.struct(
        {
            "envVariables": t.array(
                t.proxy(renames["EnvironmentVariableOut"])
            ).optional(),
            "parentPid": t.string().optional(),
            "pid": t.string().optional(),
            "script": t.proxy(renames["FileOut"]).optional(),
            "libraries": t.array(t.proxy(renames["FileOut"])).optional(),
            "args": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "binary": t.proxy(renames["FileOut"]).optional(),
            "envVariablesTruncated": t.boolean().optional(),
            "argumentsTruncated": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProcessOut"])
    types["ListBigQueryExportsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "bigQueryExports": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportIn"])
            ).optional(),
        }
    ).named(renames["ListBigQueryExportsResponseIn"])
    types["ListBigQueryExportsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "bigQueryExports": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBigQueryExportsResponseOut"])
    types["ListAssetsResultIn"] = t.struct(
        {
            "asset": t.proxy(renames["AssetIn"]).optional(),
            "stateChange": t.string().optional(),
        }
    ).named(renames["ListAssetsResultIn"])
    types["ListAssetsResultOut"] = t.struct(
        {
            "asset": t.proxy(renames["AssetOut"]).optional(),
            "stateChange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssetsResultOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["GoogleCloudSecuritycenterV1BigQueryExportIn"] = t.struct(
        {
            "filter": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "dataset": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1BigQueryExportIn"])
    types["GoogleCloudSecuritycenterV1BigQueryExportOut"] = t.struct(
        {
            "mostRecentEditor": t.string().optional(),
            "filter": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "dataset": t.string().optional(),
            "principal": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"])
    types["GroupAssetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "readTime": t.string().optional(),
            "totalSize": t.integer().optional(),
            "groupByResults": t.array(t.proxy(renames["GroupResultIn"])).optional(),
        }
    ).named(renames["GroupAssetsResponseIn"])
    types["GroupAssetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "readTime": t.string().optional(),
            "totalSize": t.integer().optional(),
            "groupByResults": t.array(t.proxy(renames["GroupResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupAssetsResponseOut"])
    types["GeolocationIn"] = t.struct({"regionCode": t.string().optional()}).named(
        renames["GeolocationIn"]
    )
    types["GeolocationOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeolocationOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["GoogleCloudSecuritycenterV1ResourceSelectorIn"] = t.struct(
        {"resourceTypes": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudSecuritycenterV1ResourceSelectorIn"])
    types["GoogleCloudSecuritycenterV1ResourceSelectorOut"] = t.struct(
        {
            "resourceTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ResourceSelectorOut"])
    types["GoogleCloudSecuritycenterV1p1beta1NotificationMessageIn"] = t.struct(
        {
            "finding": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1FindingIn"]
            ).optional(),
            "resource": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1ResourceIn"]
            ).optional(),
            "notificationConfigName": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1NotificationMessageIn"])
    types["GoogleCloudSecuritycenterV1p1beta1NotificationMessageOut"] = t.struct(
        {
            "finding": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1FindingOut"]
            ).optional(),
            "resource": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1ResourceOut"]
            ).optional(),
            "notificationConfigName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1NotificationMessageOut"])
    types[
        "GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleIn"
    ] = t.struct(
        {
            "customConfig": t.proxy(
                renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "enablementState": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleIn"]
    )
    types[
        "GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"
    ] = t.struct(
        {
            "customConfig": t.proxy(
                renames["GoogleCloudSecuritycenterV1CustomConfigOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "lastEditor": t.string().optional(),
            "ancestorModule": t.string().optional(),
            "name": t.string().optional(),
            "enablementState": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"]
    )
    types["SetMuteRequestIn"] = t.struct({"mute": t.string()}).named(
        renames["SetMuteRequestIn"]
    )
    types["SetMuteRequestOut"] = t.struct(
        {"mute": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SetMuteRequestOut"])
    types["GoogleCloudSecuritycenterV1PropertyIn"] = t.struct(
        {
            "name": t.string().optional(),
            "valueExpression": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1PropertyIn"])
    types["GoogleCloudSecuritycenterV1PropertyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "valueExpression": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1PropertyOut"])
    types["ListEffectiveSecurityHealthAnalyticsCustomModulesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "effectiveSecurityHealthAnalyticsCustomModules": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["ListEffectiveSecurityHealthAnalyticsCustomModulesResponseIn"])
    types["ListEffectiveSecurityHealthAnalyticsCustomModulesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "effectiveSecurityHealthAnalyticsCustomModules": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEffectiveSecurityHealthAnalyticsCustomModulesResponseOut"])
    types["OrganizationSettingsIn"] = t.struct(
        {
            "name": t.string().optional(),
            "assetDiscoveryConfig": t.proxy(
                renames["AssetDiscoveryConfigIn"]
            ).optional(),
            "enableAssetDiscovery": t.boolean().optional(),
        }
    ).named(renames["OrganizationSettingsIn"])
    types["OrganizationSettingsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "assetDiscoveryConfig": t.proxy(
                renames["AssetDiscoveryConfigOut"]
            ).optional(),
            "enableAssetDiscovery": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrganizationSettingsOut"])
    types["RoleIn"] = t.struct(
        {
            "ns": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["RoleIn"])
    types["RoleOut"] = t.struct(
        {
            "ns": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoleOut"])
    types["GoogleCloudSecuritycenterV1ExternalSystemIn"] = t.struct(
        {
            "assignees": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "externalUid": t.string().optional(),
            "externalSystemUpdateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ExternalSystemIn"])
    types["GoogleCloudSecuritycenterV1ExternalSystemOut"] = t.struct(
        {
            "assignees": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "externalUid": t.string().optional(),
            "externalSystemUpdateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ExternalSystemOut"])
    types["ContainerIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelIn"])).optional(),
            "imageId": t.string().optional(),
        }
    ).named(renames["ContainerIn"])
    types["ContainerOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelOut"])).optional(),
            "imageId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerOut"])
    types["ExfiltrationIn"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["ExfilResourceIn"])).optional(),
            "targets": t.array(t.proxy(renames["ExfilResourceIn"])).optional(),
        }
    ).named(renames["ExfiltrationIn"])
    types["ExfiltrationOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["ExfilResourceOut"])).optional(),
            "targets": t.array(t.proxy(renames["ExfilResourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExfiltrationOut"])
    types["GoogleCloudSecuritycenterV1p1beta1FindingIn"] = t.struct(
        {
            "parent": t.string().optional(),
            "resourceName": t.string().optional(),
            "category": t.string().optional(),
            "state": t.string().optional(),
            "eventTime": t.string().optional(),
            "createTime": t.string().optional(),
            "severity": t.string().optional(),
            "externalUri": t.string().optional(),
            "canonicalName": t.string().optional(),
            "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1FindingIn"])
    types["GoogleCloudSecuritycenterV1p1beta1FindingOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "resourceName": t.string().optional(),
            "securityMarks": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1SecurityMarksOut"]
            ).optional(),
            "category": t.string().optional(),
            "state": t.string().optional(),
            "eventTime": t.string().optional(),
            "createTime": t.string().optional(),
            "severity": t.string().optional(),
            "externalUri": t.string().optional(),
            "canonicalName": t.string().optional(),
            "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1FindingOut"])
    types["EnvironmentVariableIn"] = t.struct(
        {"val": t.string().optional(), "name": t.string().optional()}
    ).named(renames["EnvironmentVariableIn"])
    types["EnvironmentVariableOut"] = t.struct(
        {
            "val": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentVariableOut"])
    types["StreamingConfigIn"] = t.struct({"filter": t.string().optional()}).named(
        renames["StreamingConfigIn"]
    )
    types["StreamingConfigOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingConfigOut"])
    types["GroupAssetsRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "readTime": t.string().optional(),
            "filter": t.string().optional(),
            "pageSize": t.integer().optional(),
            "groupBy": t.string(),
            "compareDuration": t.string().optional(),
        }
    ).named(renames["GroupAssetsRequestIn"])
    types["GroupAssetsRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "readTime": t.string().optional(),
            "filter": t.string().optional(),
            "pageSize": t.integer().optional(),
            "groupBy": t.string(),
            "compareDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupAssetsRequestOut"])
    types["GroupResultIn"] = t.struct(
        {
            "count": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GroupResultIn"])
    types["GroupResultOut"] = t.struct(
        {
            "count": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupResultOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["FindingIn"] = t.struct(
        {
            "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
            "nextSteps": t.string().optional(),
            "createTime": t.string().optional(),
            "mute": t.string().optional(),
            "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "access": t.proxy(renames["AccessIn"]).optional(),
            "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
            "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
            "canonicalName": t.string().optional(),
            "database": t.proxy(renames["DatabaseIn"]).optional(),
            "findingClass": t.string().optional(),
            "cloudDlpDataProfile": t.proxy(renames["CloudDlpDataProfileIn"]).optional(),
            "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
            "moduleName": t.string().optional(),
            "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
            "severity": t.string().optional(),
            "parent": t.string().optional(),
            "category": t.string().optional(),
            "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
            "externalUri": t.string().optional(),
            "name": t.string().optional(),
            "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
            "eventTime": t.string().optional(),
            "muteInitiator": t.string().optional(),
            "files": t.array(t.proxy(renames["FileIn"])).optional(),
            "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "resourceName": t.string().optional(),
            "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
            "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
            "indicator": t.proxy(renames["IndicatorIn"]).optional(),
            "cloudDlpInspection": t.proxy(renames["CloudDlpInspectionIn"]).optional(),
        }
    ).named(renames["FindingIn"])
    types["FindingOut"] = t.struct(
        {
            "processes": t.array(t.proxy(renames["ProcessOut"])).optional(),
            "contacts": t.struct({"_": t.string().optional()}).optional(),
            "nextSteps": t.string().optional(),
            "createTime": t.string().optional(),
            "mute": t.string().optional(),
            "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "access": t.proxy(renames["AccessOut"]).optional(),
            "exfiltration": t.proxy(renames["ExfiltrationOut"]).optional(),
            "kernelRootkit": t.proxy(renames["KernelRootkitOut"]).optional(),
            "canonicalName": t.string().optional(),
            "database": t.proxy(renames["DatabaseOut"]).optional(),
            "findingClass": t.string().optional(),
            "cloudDlpDataProfile": t.proxy(
                renames["CloudDlpDataProfileOut"]
            ).optional(),
            "connections": t.array(t.proxy(renames["ConnectionOut"])).optional(),
            "moduleName": t.string().optional(),
            "compliances": t.array(t.proxy(renames["ComplianceOut"])).optional(),
            "severity": t.string().optional(),
            "parent": t.string().optional(),
            "category": t.string().optional(),
            "iamBindings": t.array(t.proxy(renames["IamBindingOut"])).optional(),
            "externalUri": t.string().optional(),
            "name": t.string().optional(),
            "kubernetes": t.proxy(renames["KubernetesOut"]).optional(),
            "eventTime": t.string().optional(),
            "muteInitiator": t.string().optional(),
            "files": t.array(t.proxy(renames["FileOut"])).optional(),
            "externalSystems": t.struct({"_": t.string().optional()}).optional(),
            "vulnerability": t.proxy(renames["VulnerabilityOut"]).optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "resourceName": t.string().optional(),
            "muteUpdateTime": t.string().optional(),
            "securityMarks": t.proxy(renames["SecurityMarksOut"]).optional(),
            "containers": t.array(t.proxy(renames["ContainerOut"])).optional(),
            "mitreAttack": t.proxy(renames["MitreAttackOut"]).optional(),
            "parentDisplayName": t.string().optional(),
            "indicator": t.proxy(renames["IndicatorOut"]).optional(),
            "cloudDlpInspection": t.proxy(renames["CloudDlpInspectionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindingOut"])
    types["CloudDlpDataProfileIn"] = t.struct(
        {"dataProfile": t.string().optional()}
    ).named(renames["CloudDlpDataProfileIn"])
    types["CloudDlpDataProfileOut"] = t.struct(
        {
            "dataProfile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudDlpDataProfileOut"])
    types["YaraRuleSignatureIn"] = t.struct({"yaraRule": t.string().optional()}).named(
        renames["YaraRuleSignatureIn"]
    )
    types["YaraRuleSignatureOut"] = t.struct(
        {
            "yaraRule": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YaraRuleSignatureOut"])
    types["ExfilResourceIn"] = t.struct(
        {"components": t.array(t.string()).optional(), "name": t.string().optional()}
    ).named(renames["ExfilResourceIn"])
    types["ExfilResourceOut"] = t.struct(
        {
            "components": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExfilResourceOut"])
    types["ServiceAccountDelegationInfoIn"] = t.struct(
        {
            "principalEmail": t.string().optional(),
            "principalSubject": t.string().optional(),
        }
    ).named(renames["ServiceAccountDelegationInfoIn"])
    types["ServiceAccountDelegationInfoOut"] = t.struct(
        {
            "principalEmail": t.string().optional(),
            "principalSubject": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAccountDelegationInfoOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["SourceIn"] = t.struct(
        {
            "canonicalName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "canonicalName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["NodeIn"] = t.struct({"name": t.string().optional()}).named(renames["NodeIn"])
    types["NodeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeOut"])
    types["ListAssetsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "listAssetsResults": t.array(
                t.proxy(renames["ListAssetsResultIn"])
            ).optional(),
            "readTime": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAssetsResponseIn"])
    types["ListAssetsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "listAssetsResults": t.array(
                t.proxy(renames["ListAssetsResultOut"])
            ).optional(),
            "readTime": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssetsResponseOut"])
    types["DetectionIn"] = t.struct(
        {"percentPagesMatched": t.number().optional(), "binary": t.string().optional()}
    ).named(renames["DetectionIn"])
    types["DetectionOut"] = t.struct(
        {
            "percentPagesMatched": t.number().optional(),
            "binary": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetectionOut"])
    types["VulnerabilityIn"] = t.struct(
        {"cve": t.proxy(renames["CveIn"]).optional()}
    ).named(renames["VulnerabilityIn"])
    types["VulnerabilityOut"] = t.struct(
        {
            "cve": t.proxy(renames["CveOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityOut"])
    types["ListMuteConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "muteConfigs": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigIn"])
            ).optional(),
        }
    ).named(renames["ListMuteConfigsResponseIn"])
    types["ListMuteConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "muteConfigs": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMuteConfigsResponseOut"])
    types["GoogleCloudSecuritycenterV1CustomConfigIn"] = t.struct(
        {
            "customOutput": t.proxy(
                renames["GoogleCloudSecuritycenterV1CustomOutputSpecIn"]
            ).optional(),
            "severity": t.string().optional(),
            "description": t.string().optional(),
            "predicate": t.proxy(renames["ExprIn"]).optional(),
            "resourceSelector": t.proxy(
                renames["GoogleCloudSecuritycenterV1ResourceSelectorIn"]
            ).optional(),
            "recommendation": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1CustomConfigIn"])
    types["GoogleCloudSecuritycenterV1CustomConfigOut"] = t.struct(
        {
            "customOutput": t.proxy(
                renames["GoogleCloudSecuritycenterV1CustomOutputSpecOut"]
            ).optional(),
            "severity": t.string().optional(),
            "description": t.string().optional(),
            "predicate": t.proxy(renames["ExprOut"]).optional(),
            "resourceSelector": t.proxy(
                renames["GoogleCloudSecuritycenterV1ResourceSelectorOut"]
            ).optional(),
            "recommendation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1CustomConfigOut"])

    functions = {}
    functions["organizationsUpdateOrganizationSettings"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OrganizationSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetOrganizationSettings"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OrganizationSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsFindingsBulkMute"] = securitycenter.post(
        "v1/{parent}/findings:bulkMute",
        t.struct(
            {
                "parent": t.string(),
                "muteAnnotation": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsSecurityHealthAnalyticsSettingsEffectiveCustomModulesList"
    ] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames[
                "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsSecurityHealthAnalyticsSettingsEffectiveCustomModulesGet"
    ] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames[
                "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesList"
    ] = securitycenter.post(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "enablementState": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesPatch"
    ] = securitycenter.post(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "enablementState": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesListDescendant"
    ] = securitycenter.post(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "enablementState": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesDelete"
    ] = securitycenter.post(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "enablementState": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesGet"
    ] = securitycenter.post(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "enablementState": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesCreate"
    ] = securitycenter.post(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "enablementState": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAssetsGroup"] = securitycenter.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "readTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "fieldMask": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "compareDuration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAssetsUpdateSecurityMarks"] = securitycenter.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "readTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "fieldMask": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "compareDuration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAssetsRunDiscovery"] = securitycenter.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "readTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "fieldMask": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "compareDuration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAssetsList"] = securitycenter.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "readTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "fieldMask": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "compareDuration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsBigQueryExportsGet"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsBigQueryExportsCreate"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsBigQueryExportsList"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsBigQueryExportsDelete"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsBigQueryExportsPatch"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsNotificationConfigsDelete"] = securitycenter.get(
        "v1/{parent}/notificationConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotificationConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsNotificationConfigsCreate"] = securitycenter.get(
        "v1/{parent}/notificationConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotificationConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsNotificationConfigsPatch"] = securitycenter.get(
        "v1/{parent}/notificationConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotificationConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsNotificationConfigsGet"] = securitycenter.get(
        "v1/{parent}/notificationConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotificationConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsNotificationConfigsList"] = securitycenter.get(
        "v1/{parent}/notificationConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotificationConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsOperationsList"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsOperationsDelete"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsOperationsCancel"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsOperationsGet"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsMuteConfigsCreate"] = securitycenter.get(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMuteConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsMuteConfigsPatch"] = securitycenter.get(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMuteConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsMuteConfigsGet"] = securitycenter.get(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMuteConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsMuteConfigsDelete"] = securitycenter.get(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMuteConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsMuteConfigsList"] = securitycenter.get(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMuteConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesGetIamPolicy"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "canonicalName": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesList"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "canonicalName": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesCreate"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "canonicalName": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesTestIamPermissions"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "canonicalName": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesSetIamPolicy"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "canonicalName": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesGet"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "canonicalName": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesPatch"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "canonicalName": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsUpdateSecurityMarks"] = securitycenter.post(
        "v1/{parent}/findings:group",
        t.struct(
            {
                "parent": t.string(),
                "groupBy": t.string(),
                "pageSize": t.integer().optional(),
                "compareDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsList"] = securitycenter.post(
        "v1/{parent}/findings:group",
        t.struct(
            {
                "parent": t.string(),
                "groupBy": t.string(),
                "pageSize": t.integer().optional(),
                "compareDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsSetState"] = securitycenter.post(
        "v1/{parent}/findings:group",
        t.struct(
            {
                "parent": t.string(),
                "groupBy": t.string(),
                "pageSize": t.integer().optional(),
                "compareDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsPatch"] = securitycenter.post(
        "v1/{parent}/findings:group",
        t.struct(
            {
                "parent": t.string(),
                "groupBy": t.string(),
                "pageSize": t.integer().optional(),
                "compareDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsSetMute"] = securitycenter.post(
        "v1/{parent}/findings:group",
        t.struct(
            {
                "parent": t.string(),
                "groupBy": t.string(),
                "pageSize": t.integer().optional(),
                "compareDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsCreate"] = securitycenter.post(
        "v1/{parent}/findings:group",
        t.struct(
            {
                "parent": t.string(),
                "groupBy": t.string(),
                "pageSize": t.integer().optional(),
                "compareDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsGroup"] = securitycenter.post(
        "v1/{parent}/findings:group",
        t.struct(
            {
                "parent": t.string(),
                "groupBy": t.string(),
                "pageSize": t.integer().optional(),
                "compareDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsSourcesFindingsExternalSystemsPatch"
    ] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "assignees": t.array(t.string()).optional(),
                "status": t.string().optional(),
                "externalUid": t.string().optional(),
                "externalSystemUpdateTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1ExternalSystemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsFindingsBulkMute"] = securitycenter.post(
        "v1/{parent}/findings:bulkMute",
        t.struct(
            {
                "parent": t.string(),
                "muteAnnotation": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAssetsGroup"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "startTime": t.string().optional(),
                "marks": t.struct({"_": t.string().optional()}).optional(),
                "canonicalName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecurityMarksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAssetsList"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "startTime": t.string().optional(),
                "marks": t.struct({"_": t.string().optional()}).optional(),
                "canonicalName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecurityMarksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAssetsUpdateSecurityMarks"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "startTime": t.string().optional(),
                "marks": t.struct({"_": t.string().optional()}).optional(),
                "canonicalName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecurityMarksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBigQueryExportsList"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBigQueryExportsGet"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBigQueryExportsPatch"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBigQueryExportsCreate"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBigQueryExportsDelete"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSourcesList"] = securitycenter.get(
        "v1/{parent}/sources",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSourcesFindingsPatch"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "startTime": t.string().optional(),
                "name": t.string().optional(),
                "marks": t.struct({"_": t.string().optional()}).optional(),
                "canonicalName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecurityMarksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSourcesFindingsSetState"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "startTime": t.string().optional(),
                "name": t.string().optional(),
                "marks": t.struct({"_": t.string().optional()}).optional(),
                "canonicalName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecurityMarksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSourcesFindingsList"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "startTime": t.string().optional(),
                "name": t.string().optional(),
                "marks": t.struct({"_": t.string().optional()}).optional(),
                "canonicalName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecurityMarksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSourcesFindingsSetMute"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "startTime": t.string().optional(),
                "name": t.string().optional(),
                "marks": t.struct({"_": t.string().optional()}).optional(),
                "canonicalName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecurityMarksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSourcesFindingsGroup"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "startTime": t.string().optional(),
                "name": t.string().optional(),
                "marks": t.struct({"_": t.string().optional()}).optional(),
                "canonicalName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecurityMarksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSourcesFindingsUpdateSecurityMarks"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "startTime": t.string().optional(),
                "name": t.string().optional(),
                "marks": t.struct({"_": t.string().optional()}).optional(),
                "canonicalName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecurityMarksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSourcesFindingsExternalSystemsPatch"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "assignees": t.array(t.string()).optional(),
                "status": t.string().optional(),
                "externalUid": t.string().optional(),
                "externalSystemUpdateTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1ExternalSystemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationConfigsCreate"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationConfigsPatch"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationConfigsGet"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationConfigsList"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationConfigsDelete"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsSecurityHealthAnalyticsSettingsCustomModulesCreate"
    ] = securitycenter.get(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecurityHealthAnalyticsCustomModulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsSecurityHealthAnalyticsSettingsCustomModulesDelete"
    ] = securitycenter.get(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecurityHealthAnalyticsCustomModulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsSecurityHealthAnalyticsSettingsCustomModulesListDescendant"
    ] = securitycenter.get(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecurityHealthAnalyticsCustomModulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsSecurityHealthAnalyticsSettingsCustomModulesGet"
    ] = securitycenter.get(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecurityHealthAnalyticsCustomModulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsSecurityHealthAnalyticsSettingsCustomModulesPatch"
    ] = securitycenter.get(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecurityHealthAnalyticsCustomModulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsSecurityHealthAnalyticsSettingsCustomModulesList"
    ] = securitycenter.get(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecurityHealthAnalyticsCustomModulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsSecurityHealthAnalyticsSettingsEffectiveCustomModulesGet"
    ] = securitycenter.get(
        "v1/{parent}/effectiveCustomModules",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["ListEffectiveSecurityHealthAnalyticsCustomModulesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsSecurityHealthAnalyticsSettingsEffectiveCustomModulesList"
    ] = securitycenter.get(
        "v1/{parent}/effectiveCustomModules",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["ListEffectiveSecurityHealthAnalyticsCustomModulesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMuteConfigsGet"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMuteConfigsList"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMuteConfigsDelete"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMuteConfigsCreate"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMuteConfigsPatch"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersMuteConfigsCreate"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersMuteConfigsPatch"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersMuteConfigsList"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersMuteConfigsGet"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersMuteConfigsDelete"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersNotificationConfigsDelete"] = securitycenter.get(
        "v1/{parent}/notificationConfigs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotificationConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersNotificationConfigsGet"] = securitycenter.get(
        "v1/{parent}/notificationConfigs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotificationConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersNotificationConfigsCreate"] = securitycenter.get(
        "v1/{parent}/notificationConfigs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotificationConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersNotificationConfigsPatch"] = securitycenter.get(
        "v1/{parent}/notificationConfigs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotificationConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersNotificationConfigsList"] = securitycenter.get(
        "v1/{parent}/notificationConfigs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotificationConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsEffectiveCustomModulesGet"
    ] = securitycenter.get(
        "v1/{parent}/effectiveCustomModules",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["ListEffectiveSecurityHealthAnalyticsCustomModulesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsEffectiveCustomModulesList"
    ] = securitycenter.get(
        "v1/{parent}/effectiveCustomModules",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["ListEffectiveSecurityHealthAnalyticsCustomModulesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsCustomModulesListDescendant"
    ] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsCustomModulesList"
    ] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsCustomModulesPatch"
    ] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsCustomModulesGet"
    ] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsCustomModulesCreate"
    ] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsCustomModulesDelete"
    ] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersAssetsGroup"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "startTime": t.string().optional(),
                "name": t.string().optional(),
                "marks": t.struct({"_": t.string().optional()}).optional(),
                "canonicalName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecurityMarksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersAssetsList"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "startTime": t.string().optional(),
                "name": t.string().optional(),
                "marks": t.struct({"_": t.string().optional()}).optional(),
                "canonicalName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecurityMarksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersAssetsUpdateSecurityMarks"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "startTime": t.string().optional(),
                "name": t.string().optional(),
                "marks": t.struct({"_": t.string().optional()}).optional(),
                "canonicalName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecurityMarksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesList"] = securitycenter.get(
        "v1/{parent}/sources",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsUpdateSecurityMarks"] = securitycenter.post(
        "v1/{name}:setState",
        t.struct(
            {
                "name": t.string(),
                "state": t.string(),
                "startTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsSetMute"] = securitycenter.post(
        "v1/{name}:setState",
        t.struct(
            {
                "name": t.string(),
                "state": t.string(),
                "startTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsList"] = securitycenter.post(
        "v1/{name}:setState",
        t.struct(
            {
                "name": t.string(),
                "state": t.string(),
                "startTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsGroup"] = securitycenter.post(
        "v1/{name}:setState",
        t.struct(
            {
                "name": t.string(),
                "state": t.string(),
                "startTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsPatch"] = securitycenter.post(
        "v1/{name}:setState",
        t.struct(
            {
                "name": t.string(),
                "state": t.string(),
                "startTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsSetState"] = securitycenter.post(
        "v1/{name}:setState",
        t.struct(
            {
                "name": t.string(),
                "state": t.string(),
                "startTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsExternalSystemsPatch"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "assignees": t.array(t.string()).optional(),
                "status": t.string().optional(),
                "externalUid": t.string().optional(),
                "externalSystemUpdateTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1ExternalSystemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersFindingsBulkMute"] = securitycenter.post(
        "v1/{parent}/findings:bulkMute",
        t.struct(
            {
                "parent": t.string(),
                "muteAnnotation": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersBigQueryExportsGet"] = securitycenter.get(
        "v1/{parent}/bigQueryExports",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBigQueryExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersBigQueryExportsDelete"] = securitycenter.get(
        "v1/{parent}/bigQueryExports",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBigQueryExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersBigQueryExportsPatch"] = securitycenter.get(
        "v1/{parent}/bigQueryExports",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBigQueryExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersBigQueryExportsCreate"] = securitycenter.get(
        "v1/{parent}/bigQueryExports",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBigQueryExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersBigQueryExportsList"] = securitycenter.get(
        "v1/{parent}/bigQueryExports",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBigQueryExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="securitycenter", renames=renames, types=types, functions=functions
    )
