from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_securitycenter() -> Import:
    securitycenter = HTTPRuntime("https://securitycenter.googleapis.com/")

    renames = {
        "ErrorResponse": "_securitycenter_1_ErrorResponse",
        "BulkMuteFindingsRequestIn": "_securitycenter_2_BulkMuteFindingsRequestIn",
        "BulkMuteFindingsRequestOut": "_securitycenter_3_BulkMuteFindingsRequestOut",
        "RunAssetDiscoveryRequestIn": "_securitycenter_4_RunAssetDiscoveryRequestIn",
        "RunAssetDiscoveryRequestOut": "_securitycenter_5_RunAssetDiscoveryRequestOut",
        "ListNotificationConfigsResponseIn": "_securitycenter_6_ListNotificationConfigsResponseIn",
        "ListNotificationConfigsResponseOut": "_securitycenter_7_ListNotificationConfigsResponseOut",
        "GroupAssetsRequestIn": "_securitycenter_8_GroupAssetsRequestIn",
        "GroupAssetsRequestOut": "_securitycenter_9_GroupAssetsRequestOut",
        "GetIamPolicyRequestIn": "_securitycenter_10_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_securitycenter_11_GetIamPolicyRequestOut",
        "YaraRuleSignatureIn": "_securitycenter_12_YaraRuleSignatureIn",
        "YaraRuleSignatureOut": "_securitycenter_13_YaraRuleSignatureOut",
        "IamPolicyIn": "_securitycenter_14_IamPolicyIn",
        "IamPolicyOut": "_securitycenter_15_IamPolicyOut",
        "GoogleCloudSecuritycenterV1NotificationMessageIn": "_securitycenter_16_GoogleCloudSecuritycenterV1NotificationMessageIn",
        "GoogleCloudSecuritycenterV1NotificationMessageOut": "_securitycenter_17_GoogleCloudSecuritycenterV1NotificationMessageOut",
        "GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseIn": "_securitycenter_18_GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseIn",
        "GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseOut": "_securitycenter_19_GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseOut",
        "IndicatorIn": "_securitycenter_20_IndicatorIn",
        "IndicatorOut": "_securitycenter_21_IndicatorOut",
        "KubernetesIn": "_securitycenter_22_KubernetesIn",
        "KubernetesOut": "_securitycenter_23_KubernetesOut",
        "AssetIn": "_securitycenter_24_AssetIn",
        "AssetOut": "_securitycenter_25_AssetOut",
        "GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseIn": "_securitycenter_26_GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseIn",
        "GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseOut": "_securitycenter_27_GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseOut",
        "SubjectIn": "_securitycenter_28_SubjectIn",
        "SubjectOut": "_securitycenter_29_SubjectOut",
        "StatusIn": "_securitycenter_30_StatusIn",
        "StatusOut": "_securitycenter_31_StatusOut",
        "GoogleCloudSecuritycenterV1MuteConfigIn": "_securitycenter_32_GoogleCloudSecuritycenterV1MuteConfigIn",
        "GoogleCloudSecuritycenterV1MuteConfigOut": "_securitycenter_33_GoogleCloudSecuritycenterV1MuteConfigOut",
        "ExprIn": "_securitycenter_34_ExprIn",
        "ExprOut": "_securitycenter_35_ExprOut",
        "GetPolicyOptionsIn": "_securitycenter_36_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_securitycenter_37_GetPolicyOptionsOut",
        "LabelIn": "_securitycenter_38_LabelIn",
        "LabelOut": "_securitycenter_39_LabelOut",
        "GroupFindingsResponseIn": "_securitycenter_40_GroupFindingsResponseIn",
        "GroupFindingsResponseOut": "_securitycenter_41_GroupFindingsResponseOut",
        "BindingIn": "_securitycenter_42_BindingIn",
        "BindingOut": "_securitycenter_43_BindingOut",
        "KernelRootkitIn": "_securitycenter_44_KernelRootkitIn",
        "KernelRootkitOut": "_securitycenter_45_KernelRootkitOut",
        "AuditConfigIn": "_securitycenter_46_AuditConfigIn",
        "AuditConfigOut": "_securitycenter_47_AuditConfigOut",
        "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleIn": "_securitycenter_48_GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleIn",
        "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleOut": "_securitycenter_49_GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleOut",
        "ListAssetsResponseIn": "_securitycenter_50_ListAssetsResponseIn",
        "ListAssetsResponseOut": "_securitycenter_51_ListAssetsResponseOut",
        "ComplianceIn": "_securitycenter_52_ComplianceIn",
        "ComplianceOut": "_securitycenter_53_ComplianceOut",
        "ListEffectiveSecurityHealthAnalyticsCustomModulesResponseIn": "_securitycenter_54_ListEffectiveSecurityHealthAnalyticsCustomModulesResponseIn",
        "ListEffectiveSecurityHealthAnalyticsCustomModulesResponseOut": "_securitycenter_55_ListEffectiveSecurityHealthAnalyticsCustomModulesResponseOut",
        "TestIamPermissionsRequestIn": "_securitycenter_56_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_securitycenter_57_TestIamPermissionsRequestOut",
        "ContainerIn": "_securitycenter_58_ContainerIn",
        "ContainerOut": "_securitycenter_59_ContainerOut",
        "EnvironmentVariableIn": "_securitycenter_60_EnvironmentVariableIn",
        "EnvironmentVariableOut": "_securitycenter_61_EnvironmentVariableOut",
        "FileIn": "_securitycenter_62_FileIn",
        "FileOut": "_securitycenter_63_FileOut",
        "CloudDlpInspectionIn": "_securitycenter_64_CloudDlpInspectionIn",
        "CloudDlpInspectionOut": "_securitycenter_65_CloudDlpInspectionOut",
        "GeolocationIn": "_securitycenter_66_GeolocationIn",
        "GeolocationOut": "_securitycenter_67_GeolocationOut",
        "ContactIn": "_securitycenter_68_ContactIn",
        "ContactOut": "_securitycenter_69_ContactOut",
        "EmptyIn": "_securitycenter_70_EmptyIn",
        "EmptyOut": "_securitycenter_71_EmptyOut",
        "CveIn": "_securitycenter_72_CveIn",
        "CveOut": "_securitycenter_73_CveOut",
        "GoogleCloudSecuritycenterV1PropertyIn": "_securitycenter_74_GoogleCloudSecuritycenterV1PropertyIn",
        "GoogleCloudSecuritycenterV1PropertyOut": "_securitycenter_75_GoogleCloudSecuritycenterV1PropertyOut",
        "RoleIn": "_securitycenter_76_RoleIn",
        "RoleOut": "_securitycenter_77_RoleOut",
        "TestIamPermissionsResponseIn": "_securitycenter_78_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_securitycenter_79_TestIamPermissionsResponseOut",
        "StreamingConfigIn": "_securitycenter_80_StreamingConfigIn",
        "StreamingConfigOut": "_securitycenter_81_StreamingConfigOut",
        "NotificationConfigIn": "_securitycenter_82_NotificationConfigIn",
        "NotificationConfigOut": "_securitycenter_83_NotificationConfigOut",
        "ListSourcesResponseIn": "_securitycenter_84_ListSourcesResponseIn",
        "ListSourcesResponseOut": "_securitycenter_85_ListSourcesResponseOut",
        "IamBindingIn": "_securitycenter_86_IamBindingIn",
        "IamBindingOut": "_securitycenter_87_IamBindingOut",
        "SetIamPolicyRequestIn": "_securitycenter_88_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_securitycenter_89_SetIamPolicyRequestOut",
        "FindingIn": "_securitycenter_90_FindingIn",
        "FindingOut": "_securitycenter_91_FindingOut",
        "ListMuteConfigsResponseIn": "_securitycenter_92_ListMuteConfigsResponseIn",
        "ListMuteConfigsResponseOut": "_securitycenter_93_ListMuteConfigsResponseOut",
        "ListOperationsResponseIn": "_securitycenter_94_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_securitycenter_95_ListOperationsResponseOut",
        "ListBigQueryExportsResponseIn": "_securitycenter_96_ListBigQueryExportsResponseIn",
        "ListBigQueryExportsResponseOut": "_securitycenter_97_ListBigQueryExportsResponseOut",
        "Cvssv3In": "_securitycenter_98_Cvssv3In",
        "Cvssv3Out": "_securitycenter_99_Cvssv3Out",
        "AuditLogConfigIn": "_securitycenter_100_AuditLogConfigIn",
        "AuditLogConfigOut": "_securitycenter_101_AuditLogConfigOut",
        "GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleIn": "_securitycenter_102_GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleIn",
        "GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut": "_securitycenter_103_GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut",
        "FolderIn": "_securitycenter_104_FolderIn",
        "FolderOut": "_securitycenter_105_FolderOut",
        "GoogleCloudSecuritycenterV1ResourceIn": "_securitycenter_106_GoogleCloudSecuritycenterV1ResourceIn",
        "GoogleCloudSecuritycenterV1ResourceOut": "_securitycenter_107_GoogleCloudSecuritycenterV1ResourceOut",
        "ReferenceIn": "_securitycenter_108_ReferenceIn",
        "ReferenceOut": "_securitycenter_109_ReferenceOut",
        "ContactDetailsIn": "_securitycenter_110_ContactDetailsIn",
        "ContactDetailsOut": "_securitycenter_111_ContactDetailsOut",
        "AccessIn": "_securitycenter_112_AccessIn",
        "AccessOut": "_securitycenter_113_AccessOut",
        "MemoryHashSignatureIn": "_securitycenter_114_MemoryHashSignatureIn",
        "MemoryHashSignatureOut": "_securitycenter_115_MemoryHashSignatureOut",
        "GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseIn": "_securitycenter_116_GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseIn",
        "GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseOut": "_securitycenter_117_GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseOut",
        "GoogleCloudSecuritycenterV1BindingIn": "_securitycenter_118_GoogleCloudSecuritycenterV1BindingIn",
        "GoogleCloudSecuritycenterV1BindingOut": "_securitycenter_119_GoogleCloudSecuritycenterV1BindingOut",
        "OrganizationSettingsIn": "_securitycenter_120_OrganizationSettingsIn",
        "OrganizationSettingsOut": "_securitycenter_121_OrganizationSettingsOut",
        "SourceIn": "_securitycenter_122_SourceIn",
        "SourceOut": "_securitycenter_123_SourceOut",
        "GoogleCloudSecuritycenterV1ResourceSelectorIn": "_securitycenter_124_GoogleCloudSecuritycenterV1ResourceSelectorIn",
        "GoogleCloudSecuritycenterV1ResourceSelectorOut": "_securitycenter_125_GoogleCloudSecuritycenterV1ResourceSelectorOut",
        "VulnerabilityIn": "_securitycenter_126_VulnerabilityIn",
        "VulnerabilityOut": "_securitycenter_127_VulnerabilityOut",
        "PolicyIn": "_securitycenter_128_PolicyIn",
        "PolicyOut": "_securitycenter_129_PolicyOut",
        "GoogleCloudSecuritycenterV1p1beta1FindingIn": "_securitycenter_130_GoogleCloudSecuritycenterV1p1beta1FindingIn",
        "GoogleCloudSecuritycenterV1p1beta1FindingOut": "_securitycenter_131_GoogleCloudSecuritycenterV1p1beta1FindingOut",
        "SetFindingStateRequestIn": "_securitycenter_132_SetFindingStateRequestIn",
        "SetFindingStateRequestOut": "_securitycenter_133_SetFindingStateRequestOut",
        "DetectionIn": "_securitycenter_134_DetectionIn",
        "DetectionOut": "_securitycenter_135_DetectionOut",
        "MitreAttackIn": "_securitycenter_136_MitreAttackIn",
        "MitreAttackOut": "_securitycenter_137_MitreAttackOut",
        "GoogleCloudSecuritycenterV1ExternalSystemIn": "_securitycenter_138_GoogleCloudSecuritycenterV1ExternalSystemIn",
        "GoogleCloudSecuritycenterV1ExternalSystemOut": "_securitycenter_139_GoogleCloudSecuritycenterV1ExternalSystemOut",
        "GoogleCloudSecuritycenterV1BigQueryExportIn": "_securitycenter_140_GoogleCloudSecuritycenterV1BigQueryExportIn",
        "GoogleCloudSecuritycenterV1BigQueryExportOut": "_securitycenter_141_GoogleCloudSecuritycenterV1BigQueryExportOut",
        "GroupResultIn": "_securitycenter_142_GroupResultIn",
        "GroupResultOut": "_securitycenter_143_GroupResultOut",
        "DatabaseIn": "_securitycenter_144_DatabaseIn",
        "DatabaseOut": "_securitycenter_145_DatabaseOut",
        "AssetDiscoveryConfigIn": "_securitycenter_146_AssetDiscoveryConfigIn",
        "AssetDiscoveryConfigOut": "_securitycenter_147_AssetDiscoveryConfigOut",
        "ListDescendantSecurityHealthAnalyticsCustomModulesResponseIn": "_securitycenter_148_ListDescendantSecurityHealthAnalyticsCustomModulesResponseIn",
        "ListDescendantSecurityHealthAnalyticsCustomModulesResponseOut": "_securitycenter_149_ListDescendantSecurityHealthAnalyticsCustomModulesResponseOut",
        "SecurityCenterPropertiesIn": "_securitycenter_150_SecurityCenterPropertiesIn",
        "SecurityCenterPropertiesOut": "_securitycenter_151_SecurityCenterPropertiesOut",
        "GroupAssetsResponseIn": "_securitycenter_152_GroupAssetsResponseIn",
        "GroupAssetsResponseOut": "_securitycenter_153_GroupAssetsResponseOut",
        "ProcessSignatureIn": "_securitycenter_154_ProcessSignatureIn",
        "ProcessSignatureOut": "_securitycenter_155_ProcessSignatureOut",
        "NodeIn": "_securitycenter_156_NodeIn",
        "NodeOut": "_securitycenter_157_NodeOut",
        "GroupFindingsRequestIn": "_securitycenter_158_GroupFindingsRequestIn",
        "GroupFindingsRequestOut": "_securitycenter_159_GroupFindingsRequestOut",
        "OperationIn": "_securitycenter_160_OperationIn",
        "OperationOut": "_securitycenter_161_OperationOut",
        "ListFindingsResultIn": "_securitycenter_162_ListFindingsResultIn",
        "ListFindingsResultOut": "_securitycenter_163_ListFindingsResultOut",
        "CloudDlpDataProfileIn": "_securitycenter_164_CloudDlpDataProfileIn",
        "CloudDlpDataProfileOut": "_securitycenter_165_CloudDlpDataProfileOut",
        "ServiceAccountDelegationInfoIn": "_securitycenter_166_ServiceAccountDelegationInfoIn",
        "ServiceAccountDelegationInfoOut": "_securitycenter_167_ServiceAccountDelegationInfoOut",
        "GoogleCloudSecuritycenterV1CustomOutputSpecIn": "_securitycenter_168_GoogleCloudSecuritycenterV1CustomOutputSpecIn",
        "GoogleCloudSecuritycenterV1CustomOutputSpecOut": "_securitycenter_169_GoogleCloudSecuritycenterV1CustomOutputSpecOut",
        "AccessReviewIn": "_securitycenter_170_AccessReviewIn",
        "AccessReviewOut": "_securitycenter_171_AccessReviewOut",
        "ExfiltrationIn": "_securitycenter_172_ExfiltrationIn",
        "ExfiltrationOut": "_securitycenter_173_ExfiltrationOut",
        "ExfilResourceIn": "_securitycenter_174_ExfilResourceIn",
        "ExfilResourceOut": "_securitycenter_175_ExfilResourceOut",
        "SetMuteRequestIn": "_securitycenter_176_SetMuteRequestIn",
        "SetMuteRequestOut": "_securitycenter_177_SetMuteRequestOut",
        "SecurityMarksIn": "_securitycenter_178_SecurityMarksIn",
        "SecurityMarksOut": "_securitycenter_179_SecurityMarksOut",
        "GoogleCloudSecuritycenterV1p1beta1ResourceIn": "_securitycenter_180_GoogleCloudSecuritycenterV1p1beta1ResourceIn",
        "GoogleCloudSecuritycenterV1p1beta1ResourceOut": "_securitycenter_181_GoogleCloudSecuritycenterV1p1beta1ResourceOut",
        "ConnectionIn": "_securitycenter_182_ConnectionIn",
        "ConnectionOut": "_securitycenter_183_ConnectionOut",
        "GoogleCloudSecuritycenterV1p1beta1SecurityMarksIn": "_securitycenter_184_GoogleCloudSecuritycenterV1p1beta1SecurityMarksIn",
        "GoogleCloudSecuritycenterV1p1beta1SecurityMarksOut": "_securitycenter_185_GoogleCloudSecuritycenterV1p1beta1SecurityMarksOut",
        "ListFindingsResponseIn": "_securitycenter_186_ListFindingsResponseIn",
        "ListFindingsResponseOut": "_securitycenter_187_ListFindingsResponseOut",
        "GoogleCloudSecuritycenterV1p1beta1FolderIn": "_securitycenter_188_GoogleCloudSecuritycenterV1p1beta1FolderIn",
        "GoogleCloudSecuritycenterV1p1beta1FolderOut": "_securitycenter_189_GoogleCloudSecuritycenterV1p1beta1FolderOut",
        "PodIn": "_securitycenter_190_PodIn",
        "PodOut": "_securitycenter_191_PodOut",
        "ListSecurityHealthAnalyticsCustomModulesResponseIn": "_securitycenter_192_ListSecurityHealthAnalyticsCustomModulesResponseIn",
        "ListSecurityHealthAnalyticsCustomModulesResponseOut": "_securitycenter_193_ListSecurityHealthAnalyticsCustomModulesResponseOut",
        "GoogleCloudSecuritycenterV1BulkMuteFindingsResponseIn": "_securitycenter_194_GoogleCloudSecuritycenterV1BulkMuteFindingsResponseIn",
        "GoogleCloudSecuritycenterV1BulkMuteFindingsResponseOut": "_securitycenter_195_GoogleCloudSecuritycenterV1BulkMuteFindingsResponseOut",
        "GoogleCloudSecuritycenterV1p1beta1NotificationMessageIn": "_securitycenter_196_GoogleCloudSecuritycenterV1p1beta1NotificationMessageIn",
        "GoogleCloudSecuritycenterV1p1beta1NotificationMessageOut": "_securitycenter_197_GoogleCloudSecuritycenterV1p1beta1NotificationMessageOut",
        "ListAssetsResultIn": "_securitycenter_198_ListAssetsResultIn",
        "ListAssetsResultOut": "_securitycenter_199_ListAssetsResultOut",
        "ProcessIn": "_securitycenter_200_ProcessIn",
        "ProcessOut": "_securitycenter_201_ProcessOut",
        "GoogleCloudSecuritycenterV1CustomConfigIn": "_securitycenter_202_GoogleCloudSecuritycenterV1CustomConfigIn",
        "GoogleCloudSecuritycenterV1CustomConfigOut": "_securitycenter_203_GoogleCloudSecuritycenterV1CustomConfigOut",
        "ResourceIn": "_securitycenter_204_ResourceIn",
        "ResourceOut": "_securitycenter_205_ResourceOut",
        "NodePoolIn": "_securitycenter_206_NodePoolIn",
        "NodePoolOut": "_securitycenter_207_NodePoolOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ListNotificationConfigsResponseIn"] = t.struct(
        {
            "notificationConfigs": t.array(
                t.proxy(renames["NotificationConfigIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListNotificationConfigsResponseIn"])
    types["ListNotificationConfigsResponseOut"] = t.struct(
        {
            "notificationConfigs": t.array(
                t.proxy(renames["NotificationConfigOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNotificationConfigsResponseOut"])
    types["GroupAssetsRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "compareDuration": t.string().optional(),
            "readTime": t.string().optional(),
            "pageSize": t.integer().optional(),
            "groupBy": t.string(),
            "filter": t.string().optional(),
        }
    ).named(renames["GroupAssetsRequestIn"])
    types["GroupAssetsRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "compareDuration": t.string().optional(),
            "readTime": t.string().optional(),
            "pageSize": t.integer().optional(),
            "groupBy": t.string(),
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupAssetsRequestOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["YaraRuleSignatureIn"] = t.struct({"yaraRule": t.string().optional()}).named(
        renames["YaraRuleSignatureIn"]
    )
    types["YaraRuleSignatureOut"] = t.struct(
        {
            "yaraRule": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YaraRuleSignatureOut"])
    types["IamPolicyIn"] = t.struct({"policyBlob": t.string().optional()}).named(
        renames["IamPolicyIn"]
    )
    types["IamPolicyOut"] = t.struct(
        {
            "policyBlob": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyOut"])
    types["GoogleCloudSecuritycenterV1NotificationMessageIn"] = t.struct(
        {
            "resource": t.proxy(
                renames["GoogleCloudSecuritycenterV1ResourceIn"]
            ).optional(),
            "notificationConfigName": t.string().optional(),
            "finding": t.proxy(renames["FindingIn"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1NotificationMessageIn"])
    types["GoogleCloudSecuritycenterV1NotificationMessageOut"] = t.struct(
        {
            "resource": t.proxy(
                renames["GoogleCloudSecuritycenterV1ResourceOut"]
            ).optional(),
            "notificationConfigName": t.string().optional(),
            "finding": t.proxy(renames["FindingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1NotificationMessageOut"])
    types["GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseIn"] = t.struct(
        {"duration": t.string().optional(), "state": t.string().optional()}
    ).named(renames["GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseIn"])
    types["GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseOut"])
    types["IndicatorIn"] = t.struct(
        {
            "domains": t.array(t.string()).optional(),
            "signatures": t.array(t.proxy(renames["ProcessSignatureIn"])).optional(),
            "uris": t.array(t.string()).optional(),
            "ipAddresses": t.array(t.string()).optional(),
        }
    ).named(renames["IndicatorIn"])
    types["IndicatorOut"] = t.struct(
        {
            "domains": t.array(t.string()).optional(),
            "signatures": t.array(t.proxy(renames["ProcessSignatureOut"])).optional(),
            "uris": t.array(t.string()).optional(),
            "ipAddresses": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndicatorOut"])
    types["KubernetesIn"] = t.struct(
        {
            "roles": t.array(t.proxy(renames["RoleIn"])).optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolIn"])).optional(),
            "nodes": t.array(t.proxy(renames["NodeIn"])).optional(),
            "bindings": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1BindingIn"])
            ).optional(),
            "pods": t.array(t.proxy(renames["PodIn"])).optional(),
            "accessReviews": t.array(t.proxy(renames["AccessReviewIn"])).optional(),
        }
    ).named(renames["KubernetesIn"])
    types["KubernetesOut"] = t.struct(
        {
            "roles": t.array(t.proxy(renames["RoleOut"])).optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolOut"])).optional(),
            "nodes": t.array(t.proxy(renames["NodeOut"])).optional(),
            "bindings": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1BindingOut"])
            ).optional(),
            "pods": t.array(t.proxy(renames["PodOut"])).optional(),
            "accessReviews": t.array(t.proxy(renames["AccessReviewOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesOut"])
    types["AssetIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "iamPolicy": t.proxy(renames["IamPolicyIn"]).optional(),
            "securityCenterProperties": t.proxy(
                renames["SecurityCenterPropertiesIn"]
            ).optional(),
            "name": t.string().optional(),
            "canonicalName": t.string().optional(),
            "createTime": t.string().optional(),
            "resourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "securityMarks": t.proxy(renames["SecurityMarksIn"]).optional(),
        }
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "iamPolicy": t.proxy(renames["IamPolicyOut"]).optional(),
            "securityCenterProperties": t.proxy(
                renames["SecurityCenterPropertiesOut"]
            ).optional(),
            "name": t.string().optional(),
            "canonicalName": t.string().optional(),
            "createTime": t.string().optional(),
            "resourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "securityMarks": t.proxy(renames["SecurityMarksOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
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
    types["SubjectIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "ns": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SubjectIn"])
    types["SubjectOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "ns": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubjectOut"])
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
    types["GoogleCloudSecuritycenterV1MuteConfigIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "filter": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1MuteConfigIn"])
    types["GoogleCloudSecuritycenterV1MuteConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "mostRecentEditor": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "filter": t.string(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1MuteConfigOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
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
    types["GroupFindingsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "readTime": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "groupByResults": t.array(t.proxy(renames["GroupResultIn"])).optional(),
        }
    ).named(renames["GroupFindingsResponseIn"])
    types["GroupFindingsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "readTime": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "groupByResults": t.array(t.proxy(renames["GroupResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupFindingsResponseOut"])
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["KernelRootkitIn"] = t.struct(
        {
            "unexpectedInterruptHandler": t.boolean().optional(),
            "unexpectedKernelCodePages": t.boolean().optional(),
            "unexpectedReadOnlyDataModification": t.boolean().optional(),
            "unexpectedCodeModification": t.boolean().optional(),
            "unexpectedKprobeHandler": t.boolean().optional(),
            "name": t.string().optional(),
            "unexpectedFtraceHandler": t.boolean().optional(),
            "unexpectedSystemCallHandler": t.boolean().optional(),
            "unexpectedProcessesInRunqueue": t.boolean().optional(),
        }
    ).named(renames["KernelRootkitIn"])
    types["KernelRootkitOut"] = t.struct(
        {
            "unexpectedInterruptHandler": t.boolean().optional(),
            "unexpectedKernelCodePages": t.boolean().optional(),
            "unexpectedReadOnlyDataModification": t.boolean().optional(),
            "unexpectedCodeModification": t.boolean().optional(),
            "unexpectedKprobeHandler": t.boolean().optional(),
            "name": t.string().optional(),
            "unexpectedFtraceHandler": t.boolean().optional(),
            "unexpectedSystemCallHandler": t.boolean().optional(),
            "unexpectedProcessesInRunqueue": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KernelRootkitOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
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
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "enablementState": t.string().optional(),
            "customConfig": t.proxy(
                renames["GoogleCloudSecuritycenterV1CustomConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleOut"
        ]
    )
    types["ListAssetsResponseIn"] = t.struct(
        {
            "readTime": t.string().optional(),
            "totalSize": t.integer().optional(),
            "listAssetsResults": t.array(
                t.proxy(renames["ListAssetsResultIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAssetsResponseIn"])
    types["ListAssetsResponseOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "totalSize": t.integer().optional(),
            "listAssetsResults": t.array(
                t.proxy(renames["ListAssetsResultOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssetsResponseOut"])
    types["ComplianceIn"] = t.struct(
        {
            "version": t.string().optional(),
            "standard": t.string().optional(),
            "ids": t.array(t.string()).optional(),
        }
    ).named(renames["ComplianceIn"])
    types["ComplianceOut"] = t.struct(
        {
            "version": t.string().optional(),
            "standard": t.string().optional(),
            "ids": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComplianceOut"])
    types["ListEffectiveSecurityHealthAnalyticsCustomModulesResponseIn"] = t.struct(
        {
            "effectiveSecurityHealthAnalyticsCustomModules": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleIn"
                    ]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListEffectiveSecurityHealthAnalyticsCustomModulesResponseIn"])
    types["ListEffectiveSecurityHealthAnalyticsCustomModulesResponseOut"] = t.struct(
        {
            "effectiveSecurityHealthAnalyticsCustomModules": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleOut"
                    ]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEffectiveSecurityHealthAnalyticsCustomModulesResponseOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ContainerIn"] = t.struct(
        {
            "imageId": t.string().optional(),
            "uri": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelIn"])).optional(),
        }
    ).named(renames["ContainerIn"])
    types["ContainerOut"] = t.struct(
        {
            "imageId": t.string().optional(),
            "uri": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerOut"])
    types["EnvironmentVariableIn"] = t.struct(
        {"name": t.string().optional(), "val": t.string().optional()}
    ).named(renames["EnvironmentVariableIn"])
    types["EnvironmentVariableOut"] = t.struct(
        {
            "name": t.string().optional(),
            "val": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentVariableOut"])
    types["FileIn"] = t.struct(
        {
            "sha256": t.string().optional(),
            "hashedSize": t.string().optional(),
            "contents": t.string().optional(),
            "size": t.string().optional(),
            "path": t.string().optional(),
            "partiallyHashed": t.boolean().optional(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "sha256": t.string().optional(),
            "hashedSize": t.string().optional(),
            "contents": t.string().optional(),
            "size": t.string().optional(),
            "path": t.string().optional(),
            "partiallyHashed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
    types["CloudDlpInspectionIn"] = t.struct(
        {
            "inspectJob": t.string().optional(),
            "infoType": t.string().optional(),
            "fullScan": t.boolean().optional(),
            "infoTypeCount": t.string().optional(),
        }
    ).named(renames["CloudDlpInspectionIn"])
    types["CloudDlpInspectionOut"] = t.struct(
        {
            "inspectJob": t.string().optional(),
            "infoType": t.string().optional(),
            "fullScan": t.boolean().optional(),
            "infoTypeCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudDlpInspectionOut"])
    types["GeolocationIn"] = t.struct({"regionCode": t.string().optional()}).named(
        renames["GeolocationIn"]
    )
    types["GeolocationOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeolocationOut"])
    types["ContactIn"] = t.struct({"email": t.string().optional()}).named(
        renames["ContactIn"]
    )
    types["ContactOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CveIn"] = t.struct(
        {
            "references": t.array(t.proxy(renames["ReferenceIn"])).optional(),
            "upstreamFixAvailable": t.boolean().optional(),
            "id": t.string().optional(),
            "cvssv3": t.proxy(renames["Cvssv3In"]).optional(),
        }
    ).named(renames["CveIn"])
    types["CveOut"] = t.struct(
        {
            "references": t.array(t.proxy(renames["ReferenceOut"])).optional(),
            "upstreamFixAvailable": t.boolean().optional(),
            "id": t.string().optional(),
            "cvssv3": t.proxy(renames["Cvssv3Out"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CveOut"])
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
    types["RoleIn"] = t.struct(
        {
            "name": t.string().optional(),
            "ns": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["RoleIn"])
    types["RoleOut"] = t.struct(
        {
            "name": t.string().optional(),
            "ns": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoleOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["StreamingConfigIn"] = t.struct({"filter": t.string().optional()}).named(
        renames["StreamingConfigIn"]
    )
    types["StreamingConfigOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingConfigOut"])
    types["NotificationConfigIn"] = t.struct(
        {
            "pubsubTopic": t.string().optional(),
            "streamingConfig": t.proxy(renames["StreamingConfigIn"]).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["NotificationConfigIn"])
    types["NotificationConfigOut"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "pubsubTopic": t.string().optional(),
            "streamingConfig": t.proxy(renames["StreamingConfigOut"]).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationConfigOut"])
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
    types["IamBindingIn"] = t.struct(
        {
            "member": t.string().optional(),
            "action": t.string().optional(),
            "role": t.string().optional(),
        }
    ).named(renames["IamBindingIn"])
    types["IamBindingOut"] = t.struct(
        {
            "member": t.string().optional(),
            "action": t.string().optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamBindingOut"])
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
    types["FindingIn"] = t.struct(
        {
            "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
            "muteInitiator": t.string().optional(),
            "description": t.string().optional(),
            "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
            "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
            "indicator": t.proxy(renames["IndicatorIn"]).optional(),
            "resourceName": t.string().optional(),
            "category": t.string().optional(),
            "parent": t.string().optional(),
            "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
            "externalUri": t.string().optional(),
            "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
            "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
            "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
            "database": t.proxy(renames["DatabaseIn"]).optional(),
            "nextSteps": t.string().optional(),
            "cloudDlpInspection": t.proxy(renames["CloudDlpInspectionIn"]).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "moduleName": t.string().optional(),
            "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
            "state": t.string().optional(),
            "findingClass": t.string().optional(),
            "severity": t.string().optional(),
            "mute": t.string().optional(),
            "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
            "canonicalName": t.string().optional(),
            "files": t.array(t.proxy(renames["FileIn"])).optional(),
            "cloudDlpDataProfile": t.proxy(renames["CloudDlpDataProfileIn"]).optional(),
            "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
            "access": t.proxy(renames["AccessIn"]).optional(),
            "eventTime": t.string().optional(),
        }
    ).named(renames["FindingIn"])
    types["FindingOut"] = t.struct(
        {
            "processes": t.array(t.proxy(renames["ProcessOut"])).optional(),
            "muteInitiator": t.string().optional(),
            "description": t.string().optional(),
            "kernelRootkit": t.proxy(renames["KernelRootkitOut"]).optional(),
            "vulnerability": t.proxy(renames["VulnerabilityOut"]).optional(),
            "indicator": t.proxy(renames["IndicatorOut"]).optional(),
            "resourceName": t.string().optional(),
            "category": t.string().optional(),
            "parent": t.string().optional(),
            "contacts": t.struct({"_": t.string().optional()}).optional(),
            "containers": t.array(t.proxy(renames["ContainerOut"])).optional(),
            "externalSystems": t.struct({"_": t.string().optional()}).optional(),
            "externalUri": t.string().optional(),
            "kubernetes": t.proxy(renames["KubernetesOut"]).optional(),
            "connections": t.array(t.proxy(renames["ConnectionOut"])).optional(),
            "muteUpdateTime": t.string().optional(),
            "compliances": t.array(t.proxy(renames["ComplianceOut"])).optional(),
            "database": t.proxy(renames["DatabaseOut"]).optional(),
            "nextSteps": t.string().optional(),
            "cloudDlpInspection": t.proxy(renames["CloudDlpInspectionOut"]).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "moduleName": t.string().optional(),
            "mitreAttack": t.proxy(renames["MitreAttackOut"]).optional(),
            "state": t.string().optional(),
            "findingClass": t.string().optional(),
            "severity": t.string().optional(),
            "mute": t.string().optional(),
            "iamBindings": t.array(t.proxy(renames["IamBindingOut"])).optional(),
            "parentDisplayName": t.string().optional(),
            "canonicalName": t.string().optional(),
            "files": t.array(t.proxy(renames["FileOut"])).optional(),
            "cloudDlpDataProfile": t.proxy(
                renames["CloudDlpDataProfileOut"]
            ).optional(),
            "exfiltration": t.proxy(renames["ExfiltrationOut"]).optional(),
            "securityMarks": t.proxy(renames["SecurityMarksOut"]).optional(),
            "access": t.proxy(renames["AccessOut"]).optional(),
            "eventTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindingOut"])
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
    types["ListBigQueryExportsResponseIn"] = t.struct(
        {
            "bigQueryExports": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBigQueryExportsResponseIn"])
    types["ListBigQueryExportsResponseOut"] = t.struct(
        {
            "bigQueryExports": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBigQueryExportsResponseOut"])
    types["Cvssv3In"] = t.struct(
        {
            "userInteraction": t.string().optional(),
            "confidentialityImpact": t.string().optional(),
            "attackComplexity": t.string().optional(),
            "integrityImpact": t.string().optional(),
            "baseScore": t.number().optional(),
            "scope": t.string().optional(),
            "availabilityImpact": t.string().optional(),
            "privilegesRequired": t.string().optional(),
            "attackVector": t.string().optional(),
        }
    ).named(renames["Cvssv3In"])
    types["Cvssv3Out"] = t.struct(
        {
            "userInteraction": t.string().optional(),
            "confidentialityImpact": t.string().optional(),
            "attackComplexity": t.string().optional(),
            "integrityImpact": t.string().optional(),
            "baseScore": t.number().optional(),
            "scope": t.string().optional(),
            "availabilityImpact": t.string().optional(),
            "privilegesRequired": t.string().optional(),
            "attackVector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Cvssv3Out"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types[
        "GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleIn"
    ] = t.struct(
        {
            "customConfig": t.proxy(
                renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
            ).optional(),
            "enablementState": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
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
            "enablementState": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "lastEditor": t.string().optional(),
            "updateTime": t.string().optional(),
            "ancestorModule": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"]
    )
    types["FolderIn"] = t.struct(
        {
            "resourceFolder": t.string().optional(),
            "resourceFolderDisplayName": t.string().optional(),
        }
    ).named(renames["FolderIn"])
    types["FolderOut"] = t.struct(
        {
            "resourceFolder": t.string().optional(),
            "resourceFolderDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOut"])
    types["GoogleCloudSecuritycenterV1ResourceIn"] = t.struct(
        {
            "projectDisplayName": t.string().optional(),
            "parent": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "project": t.string().optional(),
            "name": t.string().optional(),
            "parentDisplayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ResourceIn"])
    types["GoogleCloudSecuritycenterV1ResourceOut"] = t.struct(
        {
            "projectDisplayName": t.string().optional(),
            "parent": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "project": t.string().optional(),
            "name": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderOut"])).optional(),
            "parentDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ResourceOut"])
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
    types["AccessIn"] = t.struct(
        {
            "userAgentFamily": t.string().optional(),
            "userName": t.string().optional(),
            "callerIp": t.string().optional(),
            "serviceAccountDelegationInfo": t.array(
                t.proxy(renames["ServiceAccountDelegationInfoIn"])
            ).optional(),
            "principalSubject": t.string().optional(),
            "callerIpGeo": t.proxy(renames["GeolocationIn"]).optional(),
            "serviceAccountKeyName": t.string().optional(),
            "principalEmail": t.string().optional(),
            "serviceName": t.string().optional(),
            "methodName": t.string().optional(),
        }
    ).named(renames["AccessIn"])
    types["AccessOut"] = t.struct(
        {
            "userAgentFamily": t.string().optional(),
            "userName": t.string().optional(),
            "callerIp": t.string().optional(),
            "serviceAccountDelegationInfo": t.array(
                t.proxy(renames["ServiceAccountDelegationInfoOut"])
            ).optional(),
            "principalSubject": t.string().optional(),
            "callerIpGeo": t.proxy(renames["GeolocationOut"]).optional(),
            "serviceAccountKeyName": t.string().optional(),
            "principalEmail": t.string().optional(),
            "serviceName": t.string().optional(),
            "methodName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessOut"])
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
    types["GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseIn"] = t.struct(
        {"duration": t.string().optional(), "state": t.string().optional()}
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseIn"])
    types["GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseOut"])
    types["GoogleCloudSecuritycenterV1BindingIn"] = t.struct(
        {
            "subjects": t.array(t.proxy(renames["SubjectIn"])).optional(),
            "role": t.proxy(renames["RoleIn"]).optional(),
            "ns": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1BindingIn"])
    types["GoogleCloudSecuritycenterV1BindingOut"] = t.struct(
        {
            "subjects": t.array(t.proxy(renames["SubjectOut"])).optional(),
            "role": t.proxy(renames["RoleOut"]).optional(),
            "ns": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1BindingOut"])
    types["OrganizationSettingsIn"] = t.struct(
        {
            "name": t.string().optional(),
            "enableAssetDiscovery": t.boolean().optional(),
            "assetDiscoveryConfig": t.proxy(
                renames["AssetDiscoveryConfigIn"]
            ).optional(),
        }
    ).named(renames["OrganizationSettingsIn"])
    types["OrganizationSettingsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "enableAssetDiscovery": t.boolean().optional(),
            "assetDiscoveryConfig": t.proxy(
                renames["AssetDiscoveryConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrganizationSettingsOut"])
    types["SourceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "canonicalName": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "canonicalName": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["GoogleCloudSecuritycenterV1ResourceSelectorIn"] = t.struct(
        {"resourceTypes": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudSecuritycenterV1ResourceSelectorIn"])
    types["GoogleCloudSecuritycenterV1ResourceSelectorOut"] = t.struct(
        {
            "resourceTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ResourceSelectorOut"])
    types["VulnerabilityIn"] = t.struct(
        {"cve": t.proxy(renames["CveIn"]).optional()}
    ).named(renames["VulnerabilityIn"])
    types["VulnerabilityOut"] = t.struct(
        {
            "cve": t.proxy(renames["CveOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["GoogleCloudSecuritycenterV1p1beta1FindingIn"] = t.struct(
        {
            "canonicalName": t.string().optional(),
            "eventTime": t.string().optional(),
            "parent": t.string().optional(),
            "severity": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "resourceName": t.string().optional(),
            "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "category": t.string().optional(),
            "externalUri": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1FindingIn"])
    types["GoogleCloudSecuritycenterV1p1beta1FindingOut"] = t.struct(
        {
            "canonicalName": t.string().optional(),
            "eventTime": t.string().optional(),
            "parent": t.string().optional(),
            "severity": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "securityMarks": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1SecurityMarksOut"]
            ).optional(),
            "resourceName": t.string().optional(),
            "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "category": t.string().optional(),
            "externalUri": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1FindingOut"])
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
    types["MitreAttackIn"] = t.struct(
        {
            "additionalTactics": t.array(t.string()).optional(),
            "version": t.string().optional(),
            "primaryTechniques": t.array(t.string()).optional(),
            "primaryTactic": t.string().optional(),
            "additionalTechniques": t.array(t.string()).optional(),
        }
    ).named(renames["MitreAttackIn"])
    types["MitreAttackOut"] = t.struct(
        {
            "additionalTactics": t.array(t.string()).optional(),
            "version": t.string().optional(),
            "primaryTechniques": t.array(t.string()).optional(),
            "primaryTactic": t.string().optional(),
            "additionalTechniques": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MitreAttackOut"])
    types["GoogleCloudSecuritycenterV1ExternalSystemIn"] = t.struct(
        {
            "assignees": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "externalSystemUpdateTime": t.string().optional(),
            "externalUid": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ExternalSystemIn"])
    types["GoogleCloudSecuritycenterV1ExternalSystemOut"] = t.struct(
        {
            "assignees": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "externalSystemUpdateTime": t.string().optional(),
            "externalUid": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ExternalSystemOut"])
    types["GoogleCloudSecuritycenterV1BigQueryExportIn"] = t.struct(
        {
            "dataset": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "filter": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1BigQueryExportIn"])
    types["GoogleCloudSecuritycenterV1BigQueryExportOut"] = t.struct(
        {
            "principal": t.string().optional(),
            "dataset": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "filter": t.string().optional(),
            "mostRecentEditor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"])
    types["GroupResultIn"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "count": t.string().optional(),
        }
    ).named(renames["GroupResultIn"])
    types["GroupResultOut"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupResultOut"])
    types["DatabaseIn"] = t.struct(
        {
            "query": t.string().optional(),
            "userName": t.string().optional(),
            "displayName": t.string().optional(),
            "grantees": t.array(t.string()).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DatabaseIn"])
    types["DatabaseOut"] = t.struct(
        {
            "query": t.string().optional(),
            "userName": t.string().optional(),
            "displayName": t.string().optional(),
            "grantees": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseOut"])
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
    types["ListDescendantSecurityHealthAnalyticsCustomModulesResponseIn"] = t.struct(
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
    ).named(renames["ListDescendantSecurityHealthAnalyticsCustomModulesResponseIn"])
    types["ListDescendantSecurityHealthAnalyticsCustomModulesResponseOut"] = t.struct(
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
    ).named(renames["ListDescendantSecurityHealthAnalyticsCustomModulesResponseOut"])
    types["SecurityCenterPropertiesIn"] = t.struct(
        {
            "resourceDisplayName": t.string().optional(),
            "resourceType": t.string().optional(),
            "resourceName": t.string().optional(),
            "resourceParentDisplayName": t.string().optional(),
            "resourceProjectDisplayName": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderIn"])).optional(),
            "resourceOwners": t.array(t.string()).optional(),
            "resourceProject": t.string().optional(),
            "resourceParent": t.string().optional(),
        }
    ).named(renames["SecurityCenterPropertiesIn"])
    types["SecurityCenterPropertiesOut"] = t.struct(
        {
            "resourceDisplayName": t.string().optional(),
            "resourceType": t.string().optional(),
            "resourceName": t.string().optional(),
            "resourceParentDisplayName": t.string().optional(),
            "resourceProjectDisplayName": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderOut"])).optional(),
            "resourceOwners": t.array(t.string()).optional(),
            "resourceProject": t.string().optional(),
            "resourceParent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecurityCenterPropertiesOut"])
    types["GroupAssetsResponseIn"] = t.struct(
        {
            "groupByResults": t.array(t.proxy(renames["GroupResultIn"])).optional(),
            "readTime": t.string().optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GroupAssetsResponseIn"])
    types["GroupAssetsResponseOut"] = t.struct(
        {
            "groupByResults": t.array(t.proxy(renames["GroupResultOut"])).optional(),
            "readTime": t.string().optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupAssetsResponseOut"])
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
    types["NodeIn"] = t.struct({"name": t.string().optional()}).named(renames["NodeIn"])
    types["NodeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeOut"])
    types["GroupFindingsRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "groupBy": t.string(),
            "filter": t.string().optional(),
            "pageToken": t.string().optional(),
            "readTime": t.string().optional(),
            "compareDuration": t.string().optional(),
        }
    ).named(renames["GroupFindingsRequestIn"])
    types["GroupFindingsRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "groupBy": t.string(),
            "filter": t.string().optional(),
            "pageToken": t.string().optional(),
            "readTime": t.string().optional(),
            "compareDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupFindingsRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ListFindingsResultIn"] = t.struct(
        {
            "stateChange": t.string().optional(),
            "finding": t.proxy(renames["FindingIn"]).optional(),
        }
    ).named(renames["ListFindingsResultIn"])
    types["ListFindingsResultOut"] = t.struct(
        {
            "stateChange": t.string().optional(),
            "finding": t.proxy(renames["FindingOut"]).optional(),
            "resource": t.proxy(renames["ResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFindingsResultOut"])
    types["CloudDlpDataProfileIn"] = t.struct(
        {"dataProfile": t.string().optional()}
    ).named(renames["CloudDlpDataProfileIn"])
    types["CloudDlpDataProfileOut"] = t.struct(
        {
            "dataProfile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudDlpDataProfileOut"])
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
    types["AccessReviewIn"] = t.struct(
        {
            "name": t.string().optional(),
            "group": t.string().optional(),
            "subresource": t.string().optional(),
            "version": t.string().optional(),
            "resource": t.string().optional(),
            "ns": t.string().optional(),
            "verb": t.string().optional(),
        }
    ).named(renames["AccessReviewIn"])
    types["AccessReviewOut"] = t.struct(
        {
            "name": t.string().optional(),
            "group": t.string().optional(),
            "subresource": t.string().optional(),
            "version": t.string().optional(),
            "resource": t.string().optional(),
            "ns": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessReviewOut"])
    types["ExfiltrationIn"] = t.struct(
        {
            "targets": t.array(t.proxy(renames["ExfilResourceIn"])).optional(),
            "sources": t.array(t.proxy(renames["ExfilResourceIn"])).optional(),
        }
    ).named(renames["ExfiltrationIn"])
    types["ExfiltrationOut"] = t.struct(
        {
            "targets": t.array(t.proxy(renames["ExfilResourceOut"])).optional(),
            "sources": t.array(t.proxy(renames["ExfilResourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExfiltrationOut"])
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
    types["SetMuteRequestIn"] = t.struct({"mute": t.string()}).named(
        renames["SetMuteRequestIn"]
    )
    types["SetMuteRequestOut"] = t.struct(
        {"mute": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SetMuteRequestOut"])
    types["SecurityMarksIn"] = t.struct(
        {
            "name": t.string().optional(),
            "canonicalName": t.string().optional(),
            "marks": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SecurityMarksIn"])
    types["SecurityMarksOut"] = t.struct(
        {
            "name": t.string().optional(),
            "canonicalName": t.string().optional(),
            "marks": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecurityMarksOut"])
    types["GoogleCloudSecuritycenterV1p1beta1ResourceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "parentDisplayName": t.string().optional(),
            "projectDisplayName": t.string().optional(),
            "project": t.string().optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1ResourceIn"])
    types["GoogleCloudSecuritycenterV1p1beta1ResourceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "parentDisplayName": t.string().optional(),
            "folders": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1p1beta1FolderOut"])
            ).optional(),
            "projectDisplayName": t.string().optional(),
            "project": t.string().optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1ResourceOut"])
    types["ConnectionIn"] = t.struct(
        {
            "destinationPort": t.integer().optional(),
            "protocol": t.string().optional(),
            "sourceIp": t.string().optional(),
            "destinationIp": t.string().optional(),
            "sourcePort": t.integer().optional(),
        }
    ).named(renames["ConnectionIn"])
    types["ConnectionOut"] = t.struct(
        {
            "destinationPort": t.integer().optional(),
            "protocol": t.string().optional(),
            "sourceIp": t.string().optional(),
            "destinationIp": t.string().optional(),
            "sourcePort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionOut"])
    types["GoogleCloudSecuritycenterV1p1beta1SecurityMarksIn"] = t.struct(
        {
            "canonicalName": t.string().optional(),
            "name": t.string().optional(),
            "marks": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1SecurityMarksIn"])
    types["GoogleCloudSecuritycenterV1p1beta1SecurityMarksOut"] = t.struct(
        {
            "canonicalName": t.string().optional(),
            "name": t.string().optional(),
            "marks": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1SecurityMarksOut"])
    types["ListFindingsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "listFindingsResults": t.array(
                t.proxy(renames["ListFindingsResultIn"])
            ).optional(),
            "totalSize": t.integer().optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["ListFindingsResponseIn"])
    types["ListFindingsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "listFindingsResults": t.array(
                t.proxy(renames["ListFindingsResultOut"])
            ).optional(),
            "totalSize": t.integer().optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFindingsResponseOut"])
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
    types["PodIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelIn"])).optional(),
            "ns": t.string().optional(),
            "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
        }
    ).named(renames["PodIn"])
    types["PodOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelOut"])).optional(),
            "ns": t.string().optional(),
            "containers": t.array(t.proxy(renames["ContainerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PodOut"])
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
    types["GoogleCloudSecuritycenterV1BulkMuteFindingsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudSecuritycenterV1BulkMuteFindingsResponseIn"])
    types["GoogleCloudSecuritycenterV1BulkMuteFindingsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudSecuritycenterV1BulkMuteFindingsResponseOut"])
    types["GoogleCloudSecuritycenterV1p1beta1NotificationMessageIn"] = t.struct(
        {
            "notificationConfigName": t.string().optional(),
            "finding": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1FindingIn"]
            ).optional(),
            "resource": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1ResourceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1NotificationMessageIn"])
    types["GoogleCloudSecuritycenterV1p1beta1NotificationMessageOut"] = t.struct(
        {
            "notificationConfigName": t.string().optional(),
            "finding": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1FindingOut"]
            ).optional(),
            "resource": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1ResourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1NotificationMessageOut"])
    types["ListAssetsResultIn"] = t.struct(
        {
            "stateChange": t.string().optional(),
            "asset": t.proxy(renames["AssetIn"]).optional(),
        }
    ).named(renames["ListAssetsResultIn"])
    types["ListAssetsResultOut"] = t.struct(
        {
            "stateChange": t.string().optional(),
            "asset": t.proxy(renames["AssetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssetsResultOut"])
    types["ProcessIn"] = t.struct(
        {
            "libraries": t.array(t.proxy(renames["FileIn"])).optional(),
            "argumentsTruncated": t.boolean().optional(),
            "pid": t.string().optional(),
            "script": t.proxy(renames["FileIn"]).optional(),
            "args": t.array(t.string()).optional(),
            "binary": t.proxy(renames["FileIn"]).optional(),
            "parentPid": t.string().optional(),
            "envVariables": t.array(
                t.proxy(renames["EnvironmentVariableIn"])
            ).optional(),
            "name": t.string().optional(),
            "envVariablesTruncated": t.boolean().optional(),
        }
    ).named(renames["ProcessIn"])
    types["ProcessOut"] = t.struct(
        {
            "libraries": t.array(t.proxy(renames["FileOut"])).optional(),
            "argumentsTruncated": t.boolean().optional(),
            "pid": t.string().optional(),
            "script": t.proxy(renames["FileOut"]).optional(),
            "args": t.array(t.string()).optional(),
            "binary": t.proxy(renames["FileOut"]).optional(),
            "parentPid": t.string().optional(),
            "envVariables": t.array(
                t.proxy(renames["EnvironmentVariableOut"])
            ).optional(),
            "name": t.string().optional(),
            "envVariablesTruncated": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProcessOut"])
    types["GoogleCloudSecuritycenterV1CustomConfigIn"] = t.struct(
        {
            "customOutput": t.proxy(
                renames["GoogleCloudSecuritycenterV1CustomOutputSpecIn"]
            ).optional(),
            "resourceSelector": t.proxy(
                renames["GoogleCloudSecuritycenterV1ResourceSelectorIn"]
            ).optional(),
            "severity": t.string().optional(),
            "predicate": t.proxy(renames["ExprIn"]).optional(),
            "recommendation": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1CustomConfigIn"])
    types["GoogleCloudSecuritycenterV1CustomConfigOut"] = t.struct(
        {
            "customOutput": t.proxy(
                renames["GoogleCloudSecuritycenterV1CustomOutputSpecOut"]
            ).optional(),
            "resourceSelector": t.proxy(
                renames["GoogleCloudSecuritycenterV1ResourceSelectorOut"]
            ).optional(),
            "severity": t.string().optional(),
            "predicate": t.proxy(renames["ExprOut"]).optional(),
            "recommendation": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1CustomConfigOut"])
    types["ResourceIn"] = t.struct(
        {
            "parentDisplayName": t.string().optional(),
            "name": t.string().optional(),
            "projectName": t.string().optional(),
            "displayName": t.string().optional(),
            "projectDisplayName": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderIn"])).optional(),
            "type": t.string().optional(),
            "parentName": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "parentDisplayName": t.string().optional(),
            "name": t.string().optional(),
            "projectName": t.string().optional(),
            "displayName": t.string().optional(),
            "projectDisplayName": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderOut"])).optional(),
            "type": t.string().optional(),
            "parentName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
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

    functions = {}
    functions["projectsAssetsList"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "startTime": t.string().optional(),
                "updateMask": t.string().optional(),
                "canonicalName": t.string().optional(),
                "marks": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecurityMarksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAssetsGroup"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "startTime": t.string().optional(),
                "updateMask": t.string().optional(),
                "canonicalName": t.string().optional(),
                "marks": t.struct({"_": t.string().optional()}).optional(),
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
                "startTime": t.string().optional(),
                "updateMask": t.string().optional(),
                "canonicalName": t.string().optional(),
                "marks": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecurityMarksOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsSecurityHealthAnalyticsSettingsCustomModulesList"
    ] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
                "enablementState": t.string().optional(),
                "displayName": t.string().optional(),
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
        "projectsSecurityHealthAnalyticsSettingsCustomModulesGet"
    ] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
                "enablementState": t.string().optional(),
                "displayName": t.string().optional(),
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
        "projectsSecurityHealthAnalyticsSettingsCustomModulesDelete"
    ] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
                "enablementState": t.string().optional(),
                "displayName": t.string().optional(),
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
        "projectsSecurityHealthAnalyticsSettingsCustomModulesListDescendant"
    ] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
                "enablementState": t.string().optional(),
                "displayName": t.string().optional(),
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
        "projectsSecurityHealthAnalyticsSettingsCustomModulesCreate"
    ] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
                "enablementState": t.string().optional(),
                "displayName": t.string().optional(),
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
        "projectsSecurityHealthAnalyticsSettingsCustomModulesPatch"
    ] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
                "enablementState": t.string().optional(),
                "displayName": t.string().optional(),
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
        "projectsSecurityHealthAnalyticsSettingsEffectiveCustomModulesList"
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
        "projectsSecurityHealthAnalyticsSettingsEffectiveCustomModulesGet"
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
    functions["projectsMuteConfigsDelete"] = securitycenter.get(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMuteConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMuteConfigsCreate"] = securitycenter.get(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMuteConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMuteConfigsGet"] = securitycenter.get(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMuteConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMuteConfigsPatch"] = securitycenter.get(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMuteConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMuteConfigsList"] = securitycenter.get(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMuteConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationConfigsDelete"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "pubsubTopic": t.string().optional(),
                "streamingConfig": t.proxy(renames["StreamingConfigIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationConfigsCreate"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "pubsubTopic": t.string().optional(),
                "streamingConfig": t.proxy(renames["StreamingConfigIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationConfigsList"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "pubsubTopic": t.string().optional(),
                "streamingConfig": t.proxy(renames["StreamingConfigIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationConfigsGet"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "pubsubTopic": t.string().optional(),
                "streamingConfig": t.proxy(renames["StreamingConfigIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationConfigsPatch"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "pubsubTopic": t.string().optional(),
                "streamingConfig": t.proxy(renames["StreamingConfigIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBigQueryExportsPatch"] = securitycenter.get(
        "v1/{parent}/bigQueryExports",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBigQueryExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBigQueryExportsCreate"] = securitycenter.get(
        "v1/{parent}/bigQueryExports",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBigQueryExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBigQueryExportsDelete"] = securitycenter.get(
        "v1/{parent}/bigQueryExports",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBigQueryExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBigQueryExportsGet"] = securitycenter.get(
        "v1/{parent}/bigQueryExports",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBigQueryExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBigQueryExportsList"] = securitycenter.get(
        "v1/{parent}/bigQueryExports",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBigQueryExportsResponseOut"]),
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
    functions["projectsSourcesList"] = securitycenter.get(
        "v1/{parent}/sources",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSourcesFindingsSetMute"] = securitycenter.post(
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
    functions["projectsSourcesFindingsList"] = securitycenter.post(
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
    functions["projectsSourcesFindingsPatch"] = securitycenter.post(
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
    functions["projectsSourcesFindingsUpdateSecurityMarks"] = securitycenter.post(
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
    functions["projectsSourcesFindingsGroup"] = securitycenter.post(
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
    functions["projectsSourcesFindingsSetState"] = securitycenter.post(
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
    functions["projectsSourcesFindingsExternalSystemsPatch"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "assignees": t.array(t.string()).optional(),
                "status": t.string().optional(),
                "externalSystemUpdateTime": t.string().optional(),
                "externalUid": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1ExternalSystemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
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
    functions[
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesDelete"
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
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesCreate"
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
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesGet"
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
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesListDescendant"
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
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesPatch"
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
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesList"
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
        "organizationsSecurityHealthAnalyticsSettingsEffectiveCustomModulesGet"
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
        "organizationsSecurityHealthAnalyticsSettingsEffectiveCustomModulesList"
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
    functions["organizationsAssetsUpdateSecurityMarks"] = securitycenter.post(
        "v1/{parent}/assets:group",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "compareDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "groupBy": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAssetsRunDiscovery"] = securitycenter.post(
        "v1/{parent}/assets:group",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "compareDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "groupBy": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAssetsList"] = securitycenter.post(
        "v1/{parent}/assets:group",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "compareDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "groupBy": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAssetsGroup"] = securitycenter.post(
        "v1/{parent}/assets:group",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "compareDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "groupBy": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesList"] = securitycenter.post(
        "v1/{parent}/sources",
        t.struct(
            {
                "parent": t.string(),
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
    functions["organizationsSourcesGet"] = securitycenter.post(
        "v1/{parent}/sources",
        t.struct(
            {
                "parent": t.string(),
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
    functions["organizationsSourcesSetIamPolicy"] = securitycenter.post(
        "v1/{parent}/sources",
        t.struct(
            {
                "parent": t.string(),
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
    functions["organizationsSourcesPatch"] = securitycenter.post(
        "v1/{parent}/sources",
        t.struct(
            {
                "parent": t.string(),
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
    functions["organizationsSourcesGetIamPolicy"] = securitycenter.post(
        "v1/{parent}/sources",
        t.struct(
            {
                "parent": t.string(),
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
    functions["organizationsSourcesTestIamPermissions"] = securitycenter.post(
        "v1/{parent}/sources",
        t.struct(
            {
                "parent": t.string(),
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
    functions["organizationsSourcesCreate"] = securitycenter.post(
        "v1/{parent}/sources",
        t.struct(
            {
                "parent": t.string(),
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
    functions["organizationsSourcesFindingsSetState"] = securitycenter.post(
        "v1/{parent}/findings",
        t.struct(
            {
                "findingId": t.string(),
                "parent": t.string().optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "muteInitiator": t.string().optional(),
                "description": t.string().optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "resourceName": t.string().optional(),
                "category": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "externalUri": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "nextSteps": t.string().optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "moduleName": t.string().optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "state": t.string().optional(),
                "findingClass": t.string().optional(),
                "severity": t.string().optional(),
                "mute": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "canonicalName": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "eventTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsList"] = securitycenter.post(
        "v1/{parent}/findings",
        t.struct(
            {
                "findingId": t.string(),
                "parent": t.string().optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "muteInitiator": t.string().optional(),
                "description": t.string().optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "resourceName": t.string().optional(),
                "category": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "externalUri": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "nextSteps": t.string().optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "moduleName": t.string().optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "state": t.string().optional(),
                "findingClass": t.string().optional(),
                "severity": t.string().optional(),
                "mute": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "canonicalName": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "eventTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsPatch"] = securitycenter.post(
        "v1/{parent}/findings",
        t.struct(
            {
                "findingId": t.string(),
                "parent": t.string().optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "muteInitiator": t.string().optional(),
                "description": t.string().optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "resourceName": t.string().optional(),
                "category": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "externalUri": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "nextSteps": t.string().optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "moduleName": t.string().optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "state": t.string().optional(),
                "findingClass": t.string().optional(),
                "severity": t.string().optional(),
                "mute": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "canonicalName": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "eventTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsUpdateSecurityMarks"] = securitycenter.post(
        "v1/{parent}/findings",
        t.struct(
            {
                "findingId": t.string(),
                "parent": t.string().optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "muteInitiator": t.string().optional(),
                "description": t.string().optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "resourceName": t.string().optional(),
                "category": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "externalUri": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "nextSteps": t.string().optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "moduleName": t.string().optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "state": t.string().optional(),
                "findingClass": t.string().optional(),
                "severity": t.string().optional(),
                "mute": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "canonicalName": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "eventTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsGroup"] = securitycenter.post(
        "v1/{parent}/findings",
        t.struct(
            {
                "findingId": t.string(),
                "parent": t.string().optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "muteInitiator": t.string().optional(),
                "description": t.string().optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "resourceName": t.string().optional(),
                "category": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "externalUri": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "nextSteps": t.string().optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "moduleName": t.string().optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "state": t.string().optional(),
                "findingClass": t.string().optional(),
                "severity": t.string().optional(),
                "mute": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "canonicalName": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "eventTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsSetMute"] = securitycenter.post(
        "v1/{parent}/findings",
        t.struct(
            {
                "findingId": t.string(),
                "parent": t.string().optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "muteInitiator": t.string().optional(),
                "description": t.string().optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "resourceName": t.string().optional(),
                "category": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "externalUri": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "nextSteps": t.string().optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "moduleName": t.string().optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "state": t.string().optional(),
                "findingClass": t.string().optional(),
                "severity": t.string().optional(),
                "mute": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "canonicalName": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "eventTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsCreate"] = securitycenter.post(
        "v1/{parent}/findings",
        t.struct(
            {
                "findingId": t.string(),
                "parent": t.string().optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "muteInitiator": t.string().optional(),
                "description": t.string().optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "resourceName": t.string().optional(),
                "category": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "externalUri": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "nextSteps": t.string().optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "moduleName": t.string().optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "state": t.string().optional(),
                "findingClass": t.string().optional(),
                "severity": t.string().optional(),
                "mute": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "canonicalName": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "eventTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
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
                "externalSystemUpdateTime": t.string().optional(),
                "externalUid": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1ExternalSystemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsOperationsDelete"] = securitycenter.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsOperationsGet"] = securitycenter.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsOperationsList"] = securitycenter.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsOperationsCancel"] = securitycenter.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsNotificationConfigsCreate"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsNotificationConfigsDelete"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsNotificationConfigsPatch"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsNotificationConfigsList"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsNotificationConfigsGet"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationConfigOut"]),
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
    functions["organizationsBigQueryExportsGet"] = securitycenter.get(
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
    functions["organizationsBigQueryExportsPatch"] = securitycenter.get(
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
    functions["organizationsBigQueryExportsCreate"] = securitycenter.get(
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
    functions["organizationsBigQueryExportsDelete"] = securitycenter.get(
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
    functions["organizationsBigQueryExportsList"] = securitycenter.get(
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
    functions["foldersMuteConfigsCreate"] = securitycenter.get(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMuteConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersMuteConfigsPatch"] = securitycenter.get(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMuteConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersMuteConfigsDelete"] = securitycenter.get(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMuteConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersMuteConfigsGet"] = securitycenter.get(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMuteConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersMuteConfigsList"] = securitycenter.get(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMuteConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersAssetsUpdateSecurityMarks"] = securitycenter.post(
        "v1/{parent}/assets:group",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "compareDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "groupBy": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersAssetsList"] = securitycenter.post(
        "v1/{parent}/assets:group",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "compareDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "groupBy": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersAssetsGroup"] = securitycenter.post(
        "v1/{parent}/assets:group",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "compareDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "groupBy": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupAssetsResponseOut"]),
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
    functions["foldersNotificationConfigsList"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersNotificationConfigsDelete"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersNotificationConfigsPatch"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersNotificationConfigsCreate"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersNotificationConfigsGet"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersBigQueryExportsCreate"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersBigQueryExportsPatch"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersBigQueryExportsGet"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersBigQueryExportsList"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersBigQueryExportsDelete"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    ] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames["GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsCustomModulesPatch"
    ] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames["GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsCustomModulesList"
    ] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames["GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsCustomModulesDelete"
    ] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames["GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsCustomModulesCreate"
    ] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames["GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsCustomModulesGet"
    ] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames["GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesList"] = securitycenter.get(
        "v1/{parent}/sources",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsGroup"] = securitycenter.get(
        "v1/{parent}/findings",
        t.struct(
            {
                "fieldMask": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "compareDuration": t.string().optional(),
                "filter": t.string().optional(),
                "readTime": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsSetState"] = securitycenter.get(
        "v1/{parent}/findings",
        t.struct(
            {
                "fieldMask": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "compareDuration": t.string().optional(),
                "filter": t.string().optional(),
                "readTime": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsUpdateSecurityMarks"] = securitycenter.get(
        "v1/{parent}/findings",
        t.struct(
            {
                "fieldMask": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "compareDuration": t.string().optional(),
                "filter": t.string().optional(),
                "readTime": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsPatch"] = securitycenter.get(
        "v1/{parent}/findings",
        t.struct(
            {
                "fieldMask": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "compareDuration": t.string().optional(),
                "filter": t.string().optional(),
                "readTime": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsSetMute"] = securitycenter.get(
        "v1/{parent}/findings",
        t.struct(
            {
                "fieldMask": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "compareDuration": t.string().optional(),
                "filter": t.string().optional(),
                "readTime": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsList"] = securitycenter.get(
        "v1/{parent}/findings",
        t.struct(
            {
                "fieldMask": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "compareDuration": t.string().optional(),
                "filter": t.string().optional(),
                "readTime": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFindingsResponseOut"]),
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
                "externalSystemUpdateTime": t.string().optional(),
                "externalUid": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1ExternalSystemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="securitycenter",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
