from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_securitycenter() -> Import:
    securitycenter = HTTPRuntime("https://securitycenter.googleapis.com/")

    renames = {
        "ErrorResponse": "_securitycenter_1_ErrorResponse",
        "AssetDiscoveryConfigIn": "_securitycenter_2_AssetDiscoveryConfigIn",
        "AssetDiscoveryConfigOut": "_securitycenter_3_AssetDiscoveryConfigOut",
        "GroupAssetsRequestIn": "_securitycenter_4_GroupAssetsRequestIn",
        "GroupAssetsRequestOut": "_securitycenter_5_GroupAssetsRequestOut",
        "TestIamPermissionsResponseIn": "_securitycenter_6_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_securitycenter_7_TestIamPermissionsResponseOut",
        "GoogleCloudSecuritycenterV1NotificationMessageIn": "_securitycenter_8_GoogleCloudSecuritycenterV1NotificationMessageIn",
        "GoogleCloudSecuritycenterV1NotificationMessageOut": "_securitycenter_9_GoogleCloudSecuritycenterV1NotificationMessageOut",
        "OrganizationSettingsIn": "_securitycenter_10_OrganizationSettingsIn",
        "OrganizationSettingsOut": "_securitycenter_11_OrganizationSettingsOut",
        "MemoryHashSignatureIn": "_securitycenter_12_MemoryHashSignatureIn",
        "MemoryHashSignatureOut": "_securitycenter_13_MemoryHashSignatureOut",
        "GoogleCloudSecuritycenterV1BigQueryExportIn": "_securitycenter_14_GoogleCloudSecuritycenterV1BigQueryExportIn",
        "GoogleCloudSecuritycenterV1BigQueryExportOut": "_securitycenter_15_GoogleCloudSecuritycenterV1BigQueryExportOut",
        "PodIn": "_securitycenter_16_PodIn",
        "PodOut": "_securitycenter_17_PodOut",
        "VulnerabilityIn": "_securitycenter_18_VulnerabilityIn",
        "VulnerabilityOut": "_securitycenter_19_VulnerabilityOut",
        "AuditLogConfigIn": "_securitycenter_20_AuditLogConfigIn",
        "AuditLogConfigOut": "_securitycenter_21_AuditLogConfigOut",
        "RoleIn": "_securitycenter_22_RoleIn",
        "RoleOut": "_securitycenter_23_RoleOut",
        "GoogleCloudSecuritycenterV1ResourceSelectorIn": "_securitycenter_24_GoogleCloudSecuritycenterV1ResourceSelectorIn",
        "GoogleCloudSecuritycenterV1ResourceSelectorOut": "_securitycenter_25_GoogleCloudSecuritycenterV1ResourceSelectorOut",
        "GoogleCloudSecuritycenterV1MuteConfigIn": "_securitycenter_26_GoogleCloudSecuritycenterV1MuteConfigIn",
        "GoogleCloudSecuritycenterV1MuteConfigOut": "_securitycenter_27_GoogleCloudSecuritycenterV1MuteConfigOut",
        "GroupResultIn": "_securitycenter_28_GroupResultIn",
        "GroupResultOut": "_securitycenter_29_GroupResultOut",
        "StreamingConfigIn": "_securitycenter_30_StreamingConfigIn",
        "StreamingConfigOut": "_securitycenter_31_StreamingConfigOut",
        "GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseIn": "_securitycenter_32_GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseIn",
        "GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseOut": "_securitycenter_33_GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseOut",
        "ListEffectiveSecurityHealthAnalyticsCustomModulesResponseIn": "_securitycenter_34_ListEffectiveSecurityHealthAnalyticsCustomModulesResponseIn",
        "ListEffectiveSecurityHealthAnalyticsCustomModulesResponseOut": "_securitycenter_35_ListEffectiveSecurityHealthAnalyticsCustomModulesResponseOut",
        "ContactIn": "_securitycenter_36_ContactIn",
        "ContactOut": "_securitycenter_37_ContactOut",
        "IndicatorIn": "_securitycenter_38_IndicatorIn",
        "IndicatorOut": "_securitycenter_39_IndicatorOut",
        "GetIamPolicyRequestIn": "_securitycenter_40_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_securitycenter_41_GetIamPolicyRequestOut",
        "CveIn": "_securitycenter_42_CveIn",
        "CveOut": "_securitycenter_43_CveOut",
        "PolicyIn": "_securitycenter_44_PolicyIn",
        "PolicyOut": "_securitycenter_45_PolicyOut",
        "ContactDetailsIn": "_securitycenter_46_ContactDetailsIn",
        "ContactDetailsOut": "_securitycenter_47_ContactDetailsOut",
        "SetIamPolicyRequestIn": "_securitycenter_48_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_securitycenter_49_SetIamPolicyRequestOut",
        "GoogleCloudSecuritycenterV1p1beta1FolderIn": "_securitycenter_50_GoogleCloudSecuritycenterV1p1beta1FolderIn",
        "GoogleCloudSecuritycenterV1p1beta1FolderOut": "_securitycenter_51_GoogleCloudSecuritycenterV1p1beta1FolderOut",
        "AccessReviewIn": "_securitycenter_52_AccessReviewIn",
        "AccessReviewOut": "_securitycenter_53_AccessReviewOut",
        "DetectionIn": "_securitycenter_54_DetectionIn",
        "DetectionOut": "_securitycenter_55_DetectionOut",
        "EmptyIn": "_securitycenter_56_EmptyIn",
        "EmptyOut": "_securitycenter_57_EmptyOut",
        "LabelIn": "_securitycenter_58_LabelIn",
        "LabelOut": "_securitycenter_59_LabelOut",
        "ReferenceIn": "_securitycenter_60_ReferenceIn",
        "ReferenceOut": "_securitycenter_61_ReferenceOut",
        "GetPolicyOptionsIn": "_securitycenter_62_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_securitycenter_63_GetPolicyOptionsOut",
        "GoogleCloudSecuritycenterV1ExternalSystemIn": "_securitycenter_64_GoogleCloudSecuritycenterV1ExternalSystemIn",
        "GoogleCloudSecuritycenterV1ExternalSystemOut": "_securitycenter_65_GoogleCloudSecuritycenterV1ExternalSystemOut",
        "RunAssetDiscoveryRequestIn": "_securitycenter_66_RunAssetDiscoveryRequestIn",
        "RunAssetDiscoveryRequestOut": "_securitycenter_67_RunAssetDiscoveryRequestOut",
        "GroupFindingsResponseIn": "_securitycenter_68_GroupFindingsResponseIn",
        "GroupFindingsResponseOut": "_securitycenter_69_GroupFindingsResponseOut",
        "SecurityCenterPropertiesIn": "_securitycenter_70_SecurityCenterPropertiesIn",
        "SecurityCenterPropertiesOut": "_securitycenter_71_SecurityCenterPropertiesOut",
        "ContainerIn": "_securitycenter_72_ContainerIn",
        "ContainerOut": "_securitycenter_73_ContainerOut",
        "NotificationConfigIn": "_securitycenter_74_NotificationConfigIn",
        "NotificationConfigOut": "_securitycenter_75_NotificationConfigOut",
        "NodeIn": "_securitycenter_76_NodeIn",
        "NodeOut": "_securitycenter_77_NodeOut",
        "ExfilResourceIn": "_securitycenter_78_ExfilResourceIn",
        "ExfilResourceOut": "_securitycenter_79_ExfilResourceOut",
        "GoogleCloudSecuritycenterV1PropertyIn": "_securitycenter_80_GoogleCloudSecuritycenterV1PropertyIn",
        "GoogleCloudSecuritycenterV1PropertyOut": "_securitycenter_81_GoogleCloudSecuritycenterV1PropertyOut",
        "SetMuteRequestIn": "_securitycenter_82_SetMuteRequestIn",
        "SetMuteRequestOut": "_securitycenter_83_SetMuteRequestOut",
        "GroupFindingsRequestIn": "_securitycenter_84_GroupFindingsRequestIn",
        "GroupFindingsRequestOut": "_securitycenter_85_GroupFindingsRequestOut",
        "ComplianceIn": "_securitycenter_86_ComplianceIn",
        "ComplianceOut": "_securitycenter_87_ComplianceOut",
        "SetFindingStateRequestIn": "_securitycenter_88_SetFindingStateRequestIn",
        "SetFindingStateRequestOut": "_securitycenter_89_SetFindingStateRequestOut",
        "GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleIn": "_securitycenter_90_GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleIn",
        "GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut": "_securitycenter_91_GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut",
        "Cvssv3In": "_securitycenter_92_Cvssv3In",
        "Cvssv3Out": "_securitycenter_93_Cvssv3Out",
        "ListAssetsResponseIn": "_securitycenter_94_ListAssetsResponseIn",
        "ListAssetsResponseOut": "_securitycenter_95_ListAssetsResponseOut",
        "AccessIn": "_securitycenter_96_AccessIn",
        "AccessOut": "_securitycenter_97_AccessOut",
        "FileIn": "_securitycenter_98_FileIn",
        "FileOut": "_securitycenter_99_FileOut",
        "GoogleCloudSecuritycenterV1BindingIn": "_securitycenter_100_GoogleCloudSecuritycenterV1BindingIn",
        "GoogleCloudSecuritycenterV1BindingOut": "_securitycenter_101_GoogleCloudSecuritycenterV1BindingOut",
        "SubjectIn": "_securitycenter_102_SubjectIn",
        "SubjectOut": "_securitycenter_103_SubjectOut",
        "GoogleCloudSecuritycenterV1p1beta1SecurityMarksIn": "_securitycenter_104_GoogleCloudSecuritycenterV1p1beta1SecurityMarksIn",
        "GoogleCloudSecuritycenterV1p1beta1SecurityMarksOut": "_securitycenter_105_GoogleCloudSecuritycenterV1p1beta1SecurityMarksOut",
        "SourceIn": "_securitycenter_106_SourceIn",
        "SourceOut": "_securitycenter_107_SourceOut",
        "CloudDlpDataProfileIn": "_securitycenter_108_CloudDlpDataProfileIn",
        "CloudDlpDataProfileOut": "_securitycenter_109_CloudDlpDataProfileOut",
        "ExfiltrationIn": "_securitycenter_110_ExfiltrationIn",
        "ExfiltrationOut": "_securitycenter_111_ExfiltrationOut",
        "ProcessSignatureIn": "_securitycenter_112_ProcessSignatureIn",
        "ProcessSignatureOut": "_securitycenter_113_ProcessSignatureOut",
        "IamPolicyIn": "_securitycenter_114_IamPolicyIn",
        "IamPolicyOut": "_securitycenter_115_IamPolicyOut",
        "DatabaseIn": "_securitycenter_116_DatabaseIn",
        "DatabaseOut": "_securitycenter_117_DatabaseOut",
        "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleIn": "_securitycenter_118_GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleIn",
        "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleOut": "_securitycenter_119_GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleOut",
        "OperationIn": "_securitycenter_120_OperationIn",
        "OperationOut": "_securitycenter_121_OperationOut",
        "ListMuteConfigsResponseIn": "_securitycenter_122_ListMuteConfigsResponseIn",
        "ListMuteConfigsResponseOut": "_securitycenter_123_ListMuteConfigsResponseOut",
        "KernelRootkitIn": "_securitycenter_124_KernelRootkitIn",
        "KernelRootkitOut": "_securitycenter_125_KernelRootkitOut",
        "BulkMuteFindingsRequestIn": "_securitycenter_126_BulkMuteFindingsRequestIn",
        "BulkMuteFindingsRequestOut": "_securitycenter_127_BulkMuteFindingsRequestOut",
        "GroupAssetsResponseIn": "_securitycenter_128_GroupAssetsResponseIn",
        "GroupAssetsResponseOut": "_securitycenter_129_GroupAssetsResponseOut",
        "StatusIn": "_securitycenter_130_StatusIn",
        "StatusOut": "_securitycenter_131_StatusOut",
        "GoogleCloudSecuritycenterV1BulkMuteFindingsResponseIn": "_securitycenter_132_GoogleCloudSecuritycenterV1BulkMuteFindingsResponseIn",
        "GoogleCloudSecuritycenterV1BulkMuteFindingsResponseOut": "_securitycenter_133_GoogleCloudSecuritycenterV1BulkMuteFindingsResponseOut",
        "EnvironmentVariableIn": "_securitycenter_134_EnvironmentVariableIn",
        "EnvironmentVariableOut": "_securitycenter_135_EnvironmentVariableOut",
        "SecurityMarksIn": "_securitycenter_136_SecurityMarksIn",
        "SecurityMarksOut": "_securitycenter_137_SecurityMarksOut",
        "ListDescendantSecurityHealthAnalyticsCustomModulesResponseIn": "_securitycenter_138_ListDescendantSecurityHealthAnalyticsCustomModulesResponseIn",
        "ListDescendantSecurityHealthAnalyticsCustomModulesResponseOut": "_securitycenter_139_ListDescendantSecurityHealthAnalyticsCustomModulesResponseOut",
        "ListNotificationConfigsResponseIn": "_securitycenter_140_ListNotificationConfigsResponseIn",
        "ListNotificationConfigsResponseOut": "_securitycenter_141_ListNotificationConfigsResponseOut",
        "GoogleCloudSecuritycenterV1p1beta1NotificationMessageIn": "_securitycenter_142_GoogleCloudSecuritycenterV1p1beta1NotificationMessageIn",
        "GoogleCloudSecuritycenterV1p1beta1NotificationMessageOut": "_securitycenter_143_GoogleCloudSecuritycenterV1p1beta1NotificationMessageOut",
        "GoogleCloudSecuritycenterV1p1beta1FindingIn": "_securitycenter_144_GoogleCloudSecuritycenterV1p1beta1FindingIn",
        "GoogleCloudSecuritycenterV1p1beta1FindingOut": "_securitycenter_145_GoogleCloudSecuritycenterV1p1beta1FindingOut",
        "ExprIn": "_securitycenter_146_ExprIn",
        "ExprOut": "_securitycenter_147_ExprOut",
        "ResourceIn": "_securitycenter_148_ResourceIn",
        "ResourceOut": "_securitycenter_149_ResourceOut",
        "ListAssetsResultIn": "_securitycenter_150_ListAssetsResultIn",
        "ListAssetsResultOut": "_securitycenter_151_ListAssetsResultOut",
        "GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseIn": "_securitycenter_152_GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseIn",
        "GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseOut": "_securitycenter_153_GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseOut",
        "BindingIn": "_securitycenter_154_BindingIn",
        "BindingOut": "_securitycenter_155_BindingOut",
        "GoogleCloudSecuritycenterV1CustomConfigIn": "_securitycenter_156_GoogleCloudSecuritycenterV1CustomConfigIn",
        "GoogleCloudSecuritycenterV1CustomConfigOut": "_securitycenter_157_GoogleCloudSecuritycenterV1CustomConfigOut",
        "GoogleCloudSecuritycenterV1ResourceIn": "_securitycenter_158_GoogleCloudSecuritycenterV1ResourceIn",
        "GoogleCloudSecuritycenterV1ResourceOut": "_securitycenter_159_GoogleCloudSecuritycenterV1ResourceOut",
        "AssetIn": "_securitycenter_160_AssetIn",
        "AssetOut": "_securitycenter_161_AssetOut",
        "YaraRuleSignatureIn": "_securitycenter_162_YaraRuleSignatureIn",
        "YaraRuleSignatureOut": "_securitycenter_163_YaraRuleSignatureOut",
        "KubernetesIn": "_securitycenter_164_KubernetesIn",
        "KubernetesOut": "_securitycenter_165_KubernetesOut",
        "GeolocationIn": "_securitycenter_166_GeolocationIn",
        "GeolocationOut": "_securitycenter_167_GeolocationOut",
        "ListFindingsResponseIn": "_securitycenter_168_ListFindingsResponseIn",
        "ListFindingsResponseOut": "_securitycenter_169_ListFindingsResponseOut",
        "ListSecurityHealthAnalyticsCustomModulesResponseIn": "_securitycenter_170_ListSecurityHealthAnalyticsCustomModulesResponseIn",
        "ListSecurityHealthAnalyticsCustomModulesResponseOut": "_securitycenter_171_ListSecurityHealthAnalyticsCustomModulesResponseOut",
        "MitreAttackIn": "_securitycenter_172_MitreAttackIn",
        "MitreAttackOut": "_securitycenter_173_MitreAttackOut",
        "ListOperationsResponseIn": "_securitycenter_174_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_securitycenter_175_ListOperationsResponseOut",
        "ListSourcesResponseIn": "_securitycenter_176_ListSourcesResponseIn",
        "ListSourcesResponseOut": "_securitycenter_177_ListSourcesResponseOut",
        "GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseIn": "_securitycenter_178_GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseIn",
        "GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseOut": "_securitycenter_179_GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseOut",
        "ProcessIn": "_securitycenter_180_ProcessIn",
        "ProcessOut": "_securitycenter_181_ProcessOut",
        "AuditConfigIn": "_securitycenter_182_AuditConfigIn",
        "AuditConfigOut": "_securitycenter_183_AuditConfigOut",
        "GoogleCloudSecuritycenterV1p1beta1ResourceIn": "_securitycenter_184_GoogleCloudSecuritycenterV1p1beta1ResourceIn",
        "GoogleCloudSecuritycenterV1p1beta1ResourceOut": "_securitycenter_185_GoogleCloudSecuritycenterV1p1beta1ResourceOut",
        "NodePoolIn": "_securitycenter_186_NodePoolIn",
        "NodePoolOut": "_securitycenter_187_NodePoolOut",
        "ServiceAccountDelegationInfoIn": "_securitycenter_188_ServiceAccountDelegationInfoIn",
        "ServiceAccountDelegationInfoOut": "_securitycenter_189_ServiceAccountDelegationInfoOut",
        "ConnectionIn": "_securitycenter_190_ConnectionIn",
        "ConnectionOut": "_securitycenter_191_ConnectionOut",
        "FolderIn": "_securitycenter_192_FolderIn",
        "FolderOut": "_securitycenter_193_FolderOut",
        "ListBigQueryExportsResponseIn": "_securitycenter_194_ListBigQueryExportsResponseIn",
        "ListBigQueryExportsResponseOut": "_securitycenter_195_ListBigQueryExportsResponseOut",
        "TestIamPermissionsRequestIn": "_securitycenter_196_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_securitycenter_197_TestIamPermissionsRequestOut",
        "IamBindingIn": "_securitycenter_198_IamBindingIn",
        "IamBindingOut": "_securitycenter_199_IamBindingOut",
        "GoogleCloudSecuritycenterV1CustomOutputSpecIn": "_securitycenter_200_GoogleCloudSecuritycenterV1CustomOutputSpecIn",
        "GoogleCloudSecuritycenterV1CustomOutputSpecOut": "_securitycenter_201_GoogleCloudSecuritycenterV1CustomOutputSpecOut",
        "FindingIn": "_securitycenter_202_FindingIn",
        "FindingOut": "_securitycenter_203_FindingOut",
        "ListFindingsResultIn": "_securitycenter_204_ListFindingsResultIn",
        "ListFindingsResultOut": "_securitycenter_205_ListFindingsResultOut",
        "CloudDlpInspectionIn": "_securitycenter_206_CloudDlpInspectionIn",
        "CloudDlpInspectionOut": "_securitycenter_207_CloudDlpInspectionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AssetDiscoveryConfigIn"] = t.struct(
        {
            "folderIds": t.array(t.string()).optional(),
            "projectIds": t.array(t.string()).optional(),
            "inclusionMode": t.string().optional(),
        }
    ).named(renames["AssetDiscoveryConfigIn"])
    types["AssetDiscoveryConfigOut"] = t.struct(
        {
            "folderIds": t.array(t.string()).optional(),
            "projectIds": t.array(t.string()).optional(),
            "inclusionMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetDiscoveryConfigOut"])
    types["GroupAssetsRequestIn"] = t.struct(
        {
            "compareDuration": t.string().optional(),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "filter": t.string().optional(),
            "groupBy": t.string(),
            "readTime": t.string().optional(),
        }
    ).named(renames["GroupAssetsRequestIn"])
    types["GroupAssetsRequestOut"] = t.struct(
        {
            "compareDuration": t.string().optional(),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "filter": t.string().optional(),
            "groupBy": t.string(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupAssetsRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["GoogleCloudSecuritycenterV1NotificationMessageIn"] = t.struct(
        {
            "notificationConfigName": t.string().optional(),
            "resource": t.proxy(
                renames["GoogleCloudSecuritycenterV1ResourceIn"]
            ).optional(),
            "finding": t.proxy(renames["FindingIn"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1NotificationMessageIn"])
    types["GoogleCloudSecuritycenterV1NotificationMessageOut"] = t.struct(
        {
            "notificationConfigName": t.string().optional(),
            "resource": t.proxy(
                renames["GoogleCloudSecuritycenterV1ResourceOut"]
            ).optional(),
            "finding": t.proxy(renames["FindingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1NotificationMessageOut"])
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
    types["MemoryHashSignatureIn"] = t.struct(
        {
            "binaryFamily": t.string().optional(),
            "detections": t.array(t.proxy(renames["DetectionIn"])).optional(),
        }
    ).named(renames["MemoryHashSignatureIn"])
    types["MemoryHashSignatureOut"] = t.struct(
        {
            "binaryFamily": t.string().optional(),
            "detections": t.array(t.proxy(renames["DetectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemoryHashSignatureOut"])
    types["GoogleCloudSecuritycenterV1BigQueryExportIn"] = t.struct(
        {
            "filter": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "dataset": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1BigQueryExportIn"])
    types["GoogleCloudSecuritycenterV1BigQueryExportOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "dataset": t.string().optional(),
            "createTime": t.string().optional(),
            "principal": t.string().optional(),
            "updateTime": t.string().optional(),
            "mostRecentEditor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"])
    types["PodIn"] = t.struct(
        {
            "ns": t.string().optional(),
            "name": t.string().optional(),
            "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
            "labels": t.array(t.proxy(renames["LabelIn"])).optional(),
        }
    ).named(renames["PodIn"])
    types["PodOut"] = t.struct(
        {
            "ns": t.string().optional(),
            "name": t.string().optional(),
            "containers": t.array(t.proxy(renames["ContainerOut"])).optional(),
            "labels": t.array(t.proxy(renames["LabelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PodOut"])
    types["VulnerabilityIn"] = t.struct(
        {"cve": t.proxy(renames["CveIn"]).optional()}
    ).named(renames["VulnerabilityIn"])
    types["VulnerabilityOut"] = t.struct(
        {
            "cve": t.proxy(renames["CveOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityOut"])
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
    types["RoleIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "ns": t.string().optional(),
        }
    ).named(renames["RoleIn"])
    types["RoleOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "ns": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoleOut"])
    types["GoogleCloudSecuritycenterV1ResourceSelectorIn"] = t.struct(
        {"resourceTypes": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudSecuritycenterV1ResourceSelectorIn"])
    types["GoogleCloudSecuritycenterV1ResourceSelectorOut"] = t.struct(
        {
            "resourceTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ResourceSelectorOut"])
    types["GoogleCloudSecuritycenterV1MuteConfigIn"] = t.struct(
        {
            "filter": t.string(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1MuteConfigIn"])
    types["GoogleCloudSecuritycenterV1MuteConfigOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "filter": t.string(),
            "displayName": t.string().optional(),
            "mostRecentEditor": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1MuteConfigOut"])
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
    types["StreamingConfigIn"] = t.struct({"filter": t.string().optional()}).named(
        renames["StreamingConfigIn"]
    )
    types["StreamingConfigOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingConfigOut"])
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
    types["ContactIn"] = t.struct({"email": t.string().optional()}).named(
        renames["ContactIn"]
    )
    types["ContactOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactOut"])
    types["IndicatorIn"] = t.struct(
        {
            "domains": t.array(t.string()).optional(),
            "ipAddresses": t.array(t.string()).optional(),
            "uris": t.array(t.string()).optional(),
            "signatures": t.array(t.proxy(renames["ProcessSignatureIn"])).optional(),
        }
    ).named(renames["IndicatorIn"])
    types["IndicatorOut"] = t.struct(
        {
            "domains": t.array(t.string()).optional(),
            "ipAddresses": t.array(t.string()).optional(),
            "uris": t.array(t.string()).optional(),
            "signatures": t.array(t.proxy(renames["ProcessSignatureOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndicatorOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["CveIn"] = t.struct(
        {
            "id": t.string().optional(),
            "cvssv3": t.proxy(renames["Cvssv3In"]).optional(),
            "references": t.array(t.proxy(renames["ReferenceIn"])).optional(),
            "upstreamFixAvailable": t.boolean().optional(),
        }
    ).named(renames["CveIn"])
    types["CveOut"] = t.struct(
        {
            "id": t.string().optional(),
            "cvssv3": t.proxy(renames["Cvssv3Out"]).optional(),
            "references": t.array(t.proxy(renames["ReferenceOut"])).optional(),
            "upstreamFixAvailable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CveOut"])
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ContactDetailsIn"] = t.struct(
        {"contacts": t.array(t.proxy(renames["ContactIn"])).optional()}
    ).named(renames["ContactDetailsIn"])
    types["ContactDetailsOut"] = t.struct(
        {
            "contacts": t.array(t.proxy(renames["ContactOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactDetailsOut"])
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
    types["AccessReviewIn"] = t.struct(
        {
            "verb": t.string().optional(),
            "version": t.string().optional(),
            "resource": t.string().optional(),
            "subresource": t.string().optional(),
            "group": t.string().optional(),
            "ns": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AccessReviewIn"])
    types["AccessReviewOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "version": t.string().optional(),
            "resource": t.string().optional(),
            "subresource": t.string().optional(),
            "group": t.string().optional(),
            "ns": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessReviewOut"])
    types["DetectionIn"] = t.struct(
        {"binary": t.string().optional(), "percentPagesMatched": t.number().optional()}
    ).named(renames["DetectionIn"])
    types["DetectionOut"] = t.struct(
        {
            "binary": t.string().optional(),
            "percentPagesMatched": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetectionOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["LabelIn"] = t.struct(
        {"value": t.string().optional(), "name": t.string().optional()}
    ).named(renames["LabelIn"])
    types["LabelOut"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelOut"])
    types["ReferenceIn"] = t.struct(
        {"source": t.string().optional(), "uri": t.string().optional()}
    ).named(renames["ReferenceIn"])
    types["ReferenceOut"] = t.struct(
        {
            "source": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReferenceOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["GoogleCloudSecuritycenterV1ExternalSystemIn"] = t.struct(
        {
            "status": t.string().optional(),
            "name": t.string().optional(),
            "externalSystemUpdateTime": t.string().optional(),
            "assignees": t.array(t.string()).optional(),
            "externalUid": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ExternalSystemIn"])
    types["GoogleCloudSecuritycenterV1ExternalSystemOut"] = t.struct(
        {
            "status": t.string().optional(),
            "name": t.string().optional(),
            "externalSystemUpdateTime": t.string().optional(),
            "assignees": t.array(t.string()).optional(),
            "externalUid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ExternalSystemOut"])
    types["RunAssetDiscoveryRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RunAssetDiscoveryRequestIn"]
    )
    types["RunAssetDiscoveryRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RunAssetDiscoveryRequestOut"])
    types["GroupFindingsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "groupByResults": t.array(t.proxy(renames["GroupResultIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["GroupFindingsResponseIn"])
    types["GroupFindingsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "groupByResults": t.array(t.proxy(renames["GroupResultOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupFindingsResponseOut"])
    types["SecurityCenterPropertiesIn"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "resourceParent": t.string().optional(),
            "resourceOwners": t.array(t.string()).optional(),
            "folders": t.array(t.proxy(renames["FolderIn"])).optional(),
            "resourceProject": t.string().optional(),
            "resourceProjectDisplayName": t.string().optional(),
            "resourceDisplayName": t.string().optional(),
            "resourceName": t.string().optional(),
            "resourceParentDisplayName": t.string().optional(),
        }
    ).named(renames["SecurityCenterPropertiesIn"])
    types["SecurityCenterPropertiesOut"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "resourceParent": t.string().optional(),
            "resourceOwners": t.array(t.string()).optional(),
            "folders": t.array(t.proxy(renames["FolderOut"])).optional(),
            "resourceProject": t.string().optional(),
            "resourceProjectDisplayName": t.string().optional(),
            "resourceDisplayName": t.string().optional(),
            "resourceName": t.string().optional(),
            "resourceParentDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecurityCenterPropertiesOut"])
    types["ContainerIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelIn"])).optional(),
            "imageId": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["ContainerIn"])
    types["ContainerOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelOut"])).optional(),
            "imageId": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerOut"])
    types["NotificationConfigIn"] = t.struct(
        {
            "pubsubTopic": t.string().optional(),
            "description": t.string().optional(),
            "streamingConfig": t.proxy(renames["StreamingConfigIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["NotificationConfigIn"])
    types["NotificationConfigOut"] = t.struct(
        {
            "pubsubTopic": t.string().optional(),
            "description": t.string().optional(),
            "streamingConfig": t.proxy(renames["StreamingConfigOut"]).optional(),
            "name": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationConfigOut"])
    types["NodeIn"] = t.struct({"name": t.string().optional()}).named(renames["NodeIn"])
    types["NodeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeOut"])
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
    types["SetMuteRequestIn"] = t.struct({"mute": t.string()}).named(
        renames["SetMuteRequestIn"]
    )
    types["SetMuteRequestOut"] = t.struct(
        {"mute": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SetMuteRequestOut"])
    types["GroupFindingsRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "readTime": t.string().optional(),
            "groupBy": t.string(),
            "filter": t.string().optional(),
            "compareDuration": t.string().optional(),
        }
    ).named(renames["GroupFindingsRequestIn"])
    types["GroupFindingsRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "readTime": t.string().optional(),
            "groupBy": t.string(),
            "filter": t.string().optional(),
            "compareDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupFindingsRequestOut"])
    types["ComplianceIn"] = t.struct(
        {
            "ids": t.array(t.string()).optional(),
            "version": t.string().optional(),
            "standard": t.string().optional(),
        }
    ).named(renames["ComplianceIn"])
    types["ComplianceOut"] = t.struct(
        {
            "ids": t.array(t.string()).optional(),
            "version": t.string().optional(),
            "standard": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComplianceOut"])
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
    types[
        "GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleIn"
    ] = t.struct(
        {
            "enablementState": t.string().optional(),
            "customConfig": t.proxy(
                renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleIn"]
    )
    types[
        "GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"
    ] = t.struct(
        {
            "enablementState": t.string().optional(),
            "lastEditor": t.string().optional(),
            "customConfig": t.proxy(
                renames["GoogleCloudSecuritycenterV1CustomConfigOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "ancestorModule": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"]
    )
    types["Cvssv3In"] = t.struct(
        {
            "privilegesRequired": t.string().optional(),
            "userInteraction": t.string().optional(),
            "confidentialityImpact": t.string().optional(),
            "availabilityImpact": t.string().optional(),
            "integrityImpact": t.string().optional(),
            "scope": t.string().optional(),
            "attackComplexity": t.string().optional(),
            "attackVector": t.string().optional(),
            "baseScore": t.number().optional(),
        }
    ).named(renames["Cvssv3In"])
    types["Cvssv3Out"] = t.struct(
        {
            "privilegesRequired": t.string().optional(),
            "userInteraction": t.string().optional(),
            "confidentialityImpact": t.string().optional(),
            "availabilityImpact": t.string().optional(),
            "integrityImpact": t.string().optional(),
            "scope": t.string().optional(),
            "attackComplexity": t.string().optional(),
            "attackVector": t.string().optional(),
            "baseScore": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Cvssv3Out"])
    types["ListAssetsResponseIn"] = t.struct(
        {
            "readTime": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "listAssetsResults": t.array(
                t.proxy(renames["ListAssetsResultIn"])
            ).optional(),
        }
    ).named(renames["ListAssetsResponseIn"])
    types["ListAssetsResponseOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "listAssetsResults": t.array(
                t.proxy(renames["ListAssetsResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssetsResponseOut"])
    types["AccessIn"] = t.struct(
        {
            "callerIp": t.string().optional(),
            "serviceAccountKeyName": t.string().optional(),
            "serviceName": t.string().optional(),
            "serviceAccountDelegationInfo": t.array(
                t.proxy(renames["ServiceAccountDelegationInfoIn"])
            ).optional(),
            "callerIpGeo": t.proxy(renames["GeolocationIn"]).optional(),
            "userName": t.string().optional(),
            "principalSubject": t.string().optional(),
            "methodName": t.string().optional(),
            "principalEmail": t.string().optional(),
            "userAgentFamily": t.string().optional(),
        }
    ).named(renames["AccessIn"])
    types["AccessOut"] = t.struct(
        {
            "callerIp": t.string().optional(),
            "serviceAccountKeyName": t.string().optional(),
            "serviceName": t.string().optional(),
            "serviceAccountDelegationInfo": t.array(
                t.proxy(renames["ServiceAccountDelegationInfoOut"])
            ).optional(),
            "callerIpGeo": t.proxy(renames["GeolocationOut"]).optional(),
            "userName": t.string().optional(),
            "principalSubject": t.string().optional(),
            "methodName": t.string().optional(),
            "principalEmail": t.string().optional(),
            "userAgentFamily": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessOut"])
    types["FileIn"] = t.struct(
        {
            "sha256": t.string().optional(),
            "path": t.string().optional(),
            "partiallyHashed": t.boolean().optional(),
            "size": t.string().optional(),
            "hashedSize": t.string().optional(),
            "contents": t.string().optional(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "sha256": t.string().optional(),
            "path": t.string().optional(),
            "partiallyHashed": t.boolean().optional(),
            "size": t.string().optional(),
            "hashedSize": t.string().optional(),
            "contents": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
    types["GoogleCloudSecuritycenterV1BindingIn"] = t.struct(
        {
            "name": t.string().optional(),
            "ns": t.string().optional(),
            "role": t.proxy(renames["RoleIn"]).optional(),
            "subjects": t.array(t.proxy(renames["SubjectIn"])).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1BindingIn"])
    types["GoogleCloudSecuritycenterV1BindingOut"] = t.struct(
        {
            "name": t.string().optional(),
            "ns": t.string().optional(),
            "role": t.proxy(renames["RoleOut"]).optional(),
            "subjects": t.array(t.proxy(renames["SubjectOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1BindingOut"])
    types["SubjectIn"] = t.struct(
        {
            "name": t.string().optional(),
            "ns": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SubjectIn"])
    types["SubjectOut"] = t.struct(
        {
            "name": t.string().optional(),
            "ns": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubjectOut"])
    types["GoogleCloudSecuritycenterV1p1beta1SecurityMarksIn"] = t.struct(
        {
            "name": t.string().optional(),
            "marks": t.struct({"_": t.string().optional()}).optional(),
            "canonicalName": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1SecurityMarksIn"])
    types["GoogleCloudSecuritycenterV1p1beta1SecurityMarksOut"] = t.struct(
        {
            "name": t.string().optional(),
            "marks": t.struct({"_": t.string().optional()}).optional(),
            "canonicalName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1SecurityMarksOut"])
    types["SourceIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "canonicalName": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "canonicalName": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["CloudDlpDataProfileIn"] = t.struct(
        {"dataProfile": t.string().optional()}
    ).named(renames["CloudDlpDataProfileIn"])
    types["CloudDlpDataProfileOut"] = t.struct(
        {
            "dataProfile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudDlpDataProfileOut"])
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
    types["ProcessSignatureIn"] = t.struct(
        {
            "yaraRuleSignature": t.proxy(renames["YaraRuleSignatureIn"]).optional(),
            "memoryHashSignature": t.proxy(renames["MemoryHashSignatureIn"]).optional(),
        }
    ).named(renames["ProcessSignatureIn"])
    types["ProcessSignatureOut"] = t.struct(
        {
            "yaraRuleSignature": t.proxy(renames["YaraRuleSignatureOut"]).optional(),
            "memoryHashSignature": t.proxy(
                renames["MemoryHashSignatureOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProcessSignatureOut"])
    types["IamPolicyIn"] = t.struct({"policyBlob": t.string().optional()}).named(
        renames["IamPolicyIn"]
    )
    types["IamPolicyOut"] = t.struct(
        {
            "policyBlob": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyOut"])
    types["DatabaseIn"] = t.struct(
        {
            "grantees": t.array(t.string()).optional(),
            "query": t.string().optional(),
            "userName": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["DatabaseIn"])
    types["DatabaseOut"] = t.struct(
        {
            "grantees": t.array(t.string()).optional(),
            "query": t.string().optional(),
            "userName": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseOut"])
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
            "customConfig": t.proxy(
                renames["GoogleCloudSecuritycenterV1CustomConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "enablementState": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleOut"
        ]
    )
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["KernelRootkitIn"] = t.struct(
        {
            "unexpectedKprobeHandler": t.boolean().optional(),
            "unexpectedSystemCallHandler": t.boolean().optional(),
            "unexpectedProcessesInRunqueue": t.boolean().optional(),
            "unexpectedInterruptHandler": t.boolean().optional(),
            "unexpectedKernelCodePages": t.boolean().optional(),
            "unexpectedReadOnlyDataModification": t.boolean().optional(),
            "unexpectedFtraceHandler": t.boolean().optional(),
            "name": t.string().optional(),
            "unexpectedCodeModification": t.boolean().optional(),
        }
    ).named(renames["KernelRootkitIn"])
    types["KernelRootkitOut"] = t.struct(
        {
            "unexpectedKprobeHandler": t.boolean().optional(),
            "unexpectedSystemCallHandler": t.boolean().optional(),
            "unexpectedProcessesInRunqueue": t.boolean().optional(),
            "unexpectedInterruptHandler": t.boolean().optional(),
            "unexpectedKernelCodePages": t.boolean().optional(),
            "unexpectedReadOnlyDataModification": t.boolean().optional(),
            "unexpectedFtraceHandler": t.boolean().optional(),
            "name": t.string().optional(),
            "unexpectedCodeModification": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KernelRootkitOut"])
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
    types["GroupAssetsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "groupByResults": t.array(t.proxy(renames["GroupResultIn"])).optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["GroupAssetsResponseIn"])
    types["GroupAssetsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "groupByResults": t.array(t.proxy(renames["GroupResultOut"])).optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupAssetsResponseOut"])
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
    types["GoogleCloudSecuritycenterV1BulkMuteFindingsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudSecuritycenterV1BulkMuteFindingsResponseIn"])
    types["GoogleCloudSecuritycenterV1BulkMuteFindingsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudSecuritycenterV1BulkMuteFindingsResponseOut"])
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
    types["GoogleCloudSecuritycenterV1p1beta1NotificationMessageIn"] = t.struct(
        {
            "finding": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1FindingIn"]
            ).optional(),
            "notificationConfigName": t.string().optional(),
            "resource": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1ResourceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1NotificationMessageIn"])
    types["GoogleCloudSecuritycenterV1p1beta1NotificationMessageOut"] = t.struct(
        {
            "finding": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1FindingOut"]
            ).optional(),
            "notificationConfigName": t.string().optional(),
            "resource": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1ResourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1NotificationMessageOut"])
    types["GoogleCloudSecuritycenterV1p1beta1FindingIn"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "externalUri": t.string().optional(),
            "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "category": t.string().optional(),
            "canonicalName": t.string().optional(),
            "name": t.string().optional(),
            "parent": t.string().optional(),
            "state": t.string().optional(),
            "eventTime": t.string().optional(),
            "createTime": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1FindingIn"])
    types["GoogleCloudSecuritycenterV1p1beta1FindingOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "externalUri": t.string().optional(),
            "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "securityMarks": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1SecurityMarksOut"]
            ).optional(),
            "category": t.string().optional(),
            "canonicalName": t.string().optional(),
            "name": t.string().optional(),
            "parent": t.string().optional(),
            "state": t.string().optional(),
            "eventTime": t.string().optional(),
            "createTime": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1FindingOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ResourceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "projectDisplayName": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderIn"])).optional(),
            "parentDisplayName": t.string().optional(),
            "parentName": t.string().optional(),
            "projectName": t.string().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "projectDisplayName": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderOut"])).optional(),
            "parentDisplayName": t.string().optional(),
            "parentName": t.string().optional(),
            "projectName": t.string().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
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
    types["GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseIn"] = t.struct(
        {"duration": t.string().optional(), "state": t.string().optional()}
    ).named(renames["GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseIn"])
    types["GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseOut"])
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
    types["GoogleCloudSecuritycenterV1CustomConfigIn"] = t.struct(
        {
            "recommendation": t.string().optional(),
            "description": t.string().optional(),
            "predicate": t.proxy(renames["ExprIn"]).optional(),
            "resourceSelector": t.proxy(
                renames["GoogleCloudSecuritycenterV1ResourceSelectorIn"]
            ).optional(),
            "severity": t.string().optional(),
            "customOutput": t.proxy(
                renames["GoogleCloudSecuritycenterV1CustomOutputSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1CustomConfigIn"])
    types["GoogleCloudSecuritycenterV1CustomConfigOut"] = t.struct(
        {
            "recommendation": t.string().optional(),
            "description": t.string().optional(),
            "predicate": t.proxy(renames["ExprOut"]).optional(),
            "resourceSelector": t.proxy(
                renames["GoogleCloudSecuritycenterV1ResourceSelectorOut"]
            ).optional(),
            "severity": t.string().optional(),
            "customOutput": t.proxy(
                renames["GoogleCloudSecuritycenterV1CustomOutputSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1CustomConfigOut"])
    types["GoogleCloudSecuritycenterV1ResourceIn"] = t.struct(
        {
            "parent": t.string().optional(),
            "projectDisplayName": t.string().optional(),
            "name": t.string().optional(),
            "parentDisplayName": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "project": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ResourceIn"])
    types["GoogleCloudSecuritycenterV1ResourceOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "projectDisplayName": t.string().optional(),
            "name": t.string().optional(),
            "parentDisplayName": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderOut"])).optional(),
            "project": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ResourceOut"])
    types["AssetIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "securityMarks": t.proxy(renames["SecurityMarksIn"]).optional(),
            "resourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "securityCenterProperties": t.proxy(
                renames["SecurityCenterPropertiesIn"]
            ).optional(),
            "name": t.string().optional(),
            "canonicalName": t.string().optional(),
            "iamPolicy": t.proxy(renames["IamPolicyIn"]).optional(),
        }
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "securityMarks": t.proxy(renames["SecurityMarksOut"]).optional(),
            "resourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "securityCenterProperties": t.proxy(
                renames["SecurityCenterPropertiesOut"]
            ).optional(),
            "name": t.string().optional(),
            "canonicalName": t.string().optional(),
            "iamPolicy": t.proxy(renames["IamPolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
    types["YaraRuleSignatureIn"] = t.struct({"yaraRule": t.string().optional()}).named(
        renames["YaraRuleSignatureIn"]
    )
    types["YaraRuleSignatureOut"] = t.struct(
        {
            "yaraRule": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YaraRuleSignatureOut"])
    types["KubernetesIn"] = t.struct(
        {
            "nodes": t.array(t.proxy(renames["NodeIn"])).optional(),
            "roles": t.array(t.proxy(renames["RoleIn"])).optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolIn"])).optional(),
            "pods": t.array(t.proxy(renames["PodIn"])).optional(),
            "bindings": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1BindingIn"])
            ).optional(),
            "accessReviews": t.array(t.proxy(renames["AccessReviewIn"])).optional(),
        }
    ).named(renames["KubernetesIn"])
    types["KubernetesOut"] = t.struct(
        {
            "nodes": t.array(t.proxy(renames["NodeOut"])).optional(),
            "roles": t.array(t.proxy(renames["RoleOut"])).optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolOut"])).optional(),
            "pods": t.array(t.proxy(renames["PodOut"])).optional(),
            "bindings": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1BindingOut"])
            ).optional(),
            "accessReviews": t.array(t.proxy(renames["AccessReviewOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesOut"])
    types["GeolocationIn"] = t.struct({"regionCode": t.string().optional()}).named(
        renames["GeolocationIn"]
    )
    types["GeolocationOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeolocationOut"])
    types["ListFindingsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "listFindingsResults": t.array(
                t.proxy(renames["ListFindingsResultIn"])
            ).optional(),
            "readTime": t.string().optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListFindingsResponseIn"])
    types["ListFindingsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "listFindingsResults": t.array(
                t.proxy(renames["ListFindingsResultOut"])
            ).optional(),
            "readTime": t.string().optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFindingsResponseOut"])
    types["ListSecurityHealthAnalyticsCustomModulesResponseIn"] = t.struct(
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
    ).named(renames["ListSecurityHealthAnalyticsCustomModulesResponseIn"])
    types["ListSecurityHealthAnalyticsCustomModulesResponseOut"] = t.struct(
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
    ).named(renames["ListSecurityHealthAnalyticsCustomModulesResponseOut"])
    types["MitreAttackIn"] = t.struct(
        {
            "primaryTechniques": t.array(t.string()).optional(),
            "additionalTechniques": t.array(t.string()).optional(),
            "version": t.string().optional(),
            "additionalTactics": t.array(t.string()).optional(),
            "primaryTactic": t.string().optional(),
        }
    ).named(renames["MitreAttackIn"])
    types["MitreAttackOut"] = t.struct(
        {
            "primaryTechniques": t.array(t.string()).optional(),
            "additionalTechniques": t.array(t.string()).optional(),
            "version": t.string().optional(),
            "additionalTactics": t.array(t.string()).optional(),
            "primaryTactic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MitreAttackOut"])
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
    types["ProcessIn"] = t.struct(
        {
            "envVariables": t.array(
                t.proxy(renames["EnvironmentVariableIn"])
            ).optional(),
            "argumentsTruncated": t.boolean().optional(),
            "name": t.string().optional(),
            "script": t.proxy(renames["FileIn"]).optional(),
            "envVariablesTruncated": t.boolean().optional(),
            "parentPid": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "pid": t.string().optional(),
            "libraries": t.array(t.proxy(renames["FileIn"])).optional(),
            "binary": t.proxy(renames["FileIn"]).optional(),
        }
    ).named(renames["ProcessIn"])
    types["ProcessOut"] = t.struct(
        {
            "envVariables": t.array(
                t.proxy(renames["EnvironmentVariableOut"])
            ).optional(),
            "argumentsTruncated": t.boolean().optional(),
            "name": t.string().optional(),
            "script": t.proxy(renames["FileOut"]).optional(),
            "envVariablesTruncated": t.boolean().optional(),
            "parentPid": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "pid": t.string().optional(),
            "libraries": t.array(t.proxy(renames["FileOut"])).optional(),
            "binary": t.proxy(renames["FileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProcessOut"])
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
    types["GoogleCloudSecuritycenterV1p1beta1ResourceIn"] = t.struct(
        {
            "projectDisplayName": t.string().optional(),
            "name": t.string().optional(),
            "project": t.string().optional(),
            "parentDisplayName": t.string().optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1ResourceIn"])
    types["GoogleCloudSecuritycenterV1p1beta1ResourceOut"] = t.struct(
        {
            "projectDisplayName": t.string().optional(),
            "folders": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1p1beta1FolderOut"])
            ).optional(),
            "name": t.string().optional(),
            "project": t.string().optional(),
            "parentDisplayName": t.string().optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1ResourceOut"])
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
    types["ConnectionIn"] = t.struct(
        {
            "protocol": t.string().optional(),
            "sourcePort": t.integer().optional(),
            "sourceIp": t.string().optional(),
            "destinationPort": t.integer().optional(),
            "destinationIp": t.string().optional(),
        }
    ).named(renames["ConnectionIn"])
    types["ConnectionOut"] = t.struct(
        {
            "protocol": t.string().optional(),
            "sourcePort": t.integer().optional(),
            "sourceIp": t.string().optional(),
            "destinationPort": t.integer().optional(),
            "destinationIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["IamBindingIn"] = t.struct(
        {
            "member": t.string().optional(),
            "role": t.string().optional(),
            "action": t.string().optional(),
        }
    ).named(renames["IamBindingIn"])
    types["IamBindingOut"] = t.struct(
        {
            "member": t.string().optional(),
            "role": t.string().optional(),
            "action": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamBindingOut"])
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
    types["FindingIn"] = t.struct(
        {
            "mute": t.string().optional(),
            "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
            "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
            "name": t.string().optional(),
            "cloudDlpInspection": t.proxy(renames["CloudDlpInspectionIn"]).optional(),
            "cloudDlpDataProfile": t.proxy(renames["CloudDlpDataProfileIn"]).optional(),
            "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
            "canonicalName": t.string().optional(),
            "nextSteps": t.string().optional(),
            "muteInitiator": t.string().optional(),
            "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
            "createTime": t.string().optional(),
            "indicator": t.proxy(renames["IndicatorIn"]).optional(),
            "description": t.string().optional(),
            "files": t.array(t.proxy(renames["FileIn"])).optional(),
            "findingClass": t.string().optional(),
            "externalUri": t.string().optional(),
            "severity": t.string().optional(),
            "eventTime": t.string().optional(),
            "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
            "state": t.string().optional(),
            "moduleName": t.string().optional(),
            "category": t.string().optional(),
            "access": t.proxy(renames["AccessIn"]).optional(),
            "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
            "resourceName": t.string().optional(),
            "database": t.proxy(renames["DatabaseIn"]).optional(),
            "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
            "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
            "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
            "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["FindingIn"])
    types["FindingOut"] = t.struct(
        {
            "mute": t.string().optional(),
            "kubernetes": t.proxy(renames["KubernetesOut"]).optional(),
            "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "connections": t.array(t.proxy(renames["ConnectionOut"])).optional(),
            "name": t.string().optional(),
            "cloudDlpInspection": t.proxy(renames["CloudDlpInspectionOut"]).optional(),
            "cloudDlpDataProfile": t.proxy(
                renames["CloudDlpDataProfileOut"]
            ).optional(),
            "compliances": t.array(t.proxy(renames["ComplianceOut"])).optional(),
            "muteUpdateTime": t.string().optional(),
            "canonicalName": t.string().optional(),
            "nextSteps": t.string().optional(),
            "muteInitiator": t.string().optional(),
            "securityMarks": t.proxy(renames["SecurityMarksOut"]).optional(),
            "containers": t.array(t.proxy(renames["ContainerOut"])).optional(),
            "createTime": t.string().optional(),
            "indicator": t.proxy(renames["IndicatorOut"]).optional(),
            "description": t.string().optional(),
            "contacts": t.struct({"_": t.string().optional()}).optional(),
            "files": t.array(t.proxy(renames["FileOut"])).optional(),
            "findingClass": t.string().optional(),
            "externalUri": t.string().optional(),
            "severity": t.string().optional(),
            "parentDisplayName": t.string().optional(),
            "eventTime": t.string().optional(),
            "iamBindings": t.array(t.proxy(renames["IamBindingOut"])).optional(),
            "state": t.string().optional(),
            "moduleName": t.string().optional(),
            "category": t.string().optional(),
            "access": t.proxy(renames["AccessOut"]).optional(),
            "processes": t.array(t.proxy(renames["ProcessOut"])).optional(),
            "resourceName": t.string().optional(),
            "database": t.proxy(renames["DatabaseOut"]).optional(),
            "kernelRootkit": t.proxy(renames["KernelRootkitOut"]).optional(),
            "vulnerability": t.proxy(renames["VulnerabilityOut"]).optional(),
            "exfiltration": t.proxy(renames["ExfiltrationOut"]).optional(),
            "mitreAttack": t.proxy(renames["MitreAttackOut"]).optional(),
            "parent": t.string().optional(),
            "externalSystems": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindingOut"])
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
    types["CloudDlpInspectionIn"] = t.struct(
        {
            "fullScan": t.boolean().optional(),
            "infoType": t.string().optional(),
            "infoTypeCount": t.string().optional(),
            "inspectJob": t.string().optional(),
        }
    ).named(renames["CloudDlpInspectionIn"])
    types["CloudDlpInspectionOut"] = t.struct(
        {
            "fullScan": t.boolean().optional(),
            "infoType": t.string().optional(),
            "infoTypeCount": t.string().optional(),
            "inspectJob": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudDlpInspectionOut"])

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
    functions["organizationsMuteConfigsDelete"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsMuteConfigsPatch"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsMuteConfigsList"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsMuteConfigsCreate"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsMuteConfigsGet"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
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
    functions["organizationsOperationsCancel"] = securitycenter.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesGet"
    ] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesPatch"
    ] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesCreate"
    ] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesList"
    ] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesListDescendant"
    ] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesDelete"
    ] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsBigQueryExportsGet"] = securitycenter.get(
        "v1/{parent}/bigQueryExports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBigQueryExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAssetsGroup"] = securitycenter.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "compareDuration": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "fieldMask": t.string().optional(),
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
                "compareDuration": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "fieldMask": t.string().optional(),
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
                "compareDuration": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "fieldMask": t.string().optional(),
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
                "compareDuration": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "fieldMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsNotificationConfigsCreate"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsNotificationConfigsGet"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsNotificationConfigsPatch"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsNotificationConfigsList"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsNotificationConfigsDelete"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesPatch"] = securitycenter.post(
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
    functions["organizationsSourcesCreate"] = securitycenter.post(
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
    functions["organizationsSourcesList"] = securitycenter.post(
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
    functions["organizationsSourcesGetIamPolicy"] = securitycenter.post(
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
    functions["organizationsSourcesSetIamPolicy"] = securitycenter.post(
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
    functions["organizationsSourcesGet"] = securitycenter.post(
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
    functions["organizationsSourcesTestIamPermissions"] = securitycenter.post(
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
    functions["organizationsSourcesFindingsSetMute"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "mute": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "canonicalName": t.string().optional(),
                "nextSteps": t.string().optional(),
                "muteInitiator": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "createTime": t.string().optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "description": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "findingClass": t.string().optional(),
                "externalUri": t.string().optional(),
                "severity": t.string().optional(),
                "eventTime": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "state": t.string().optional(),
                "moduleName": t.string().optional(),
                "category": t.string().optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "resourceName": t.string().optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsUpdateSecurityMarks"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "mute": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "canonicalName": t.string().optional(),
                "nextSteps": t.string().optional(),
                "muteInitiator": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "createTime": t.string().optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "description": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "findingClass": t.string().optional(),
                "externalUri": t.string().optional(),
                "severity": t.string().optional(),
                "eventTime": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "state": t.string().optional(),
                "moduleName": t.string().optional(),
                "category": t.string().optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "resourceName": t.string().optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsSetState"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "mute": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "canonicalName": t.string().optional(),
                "nextSteps": t.string().optional(),
                "muteInitiator": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "createTime": t.string().optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "description": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "findingClass": t.string().optional(),
                "externalUri": t.string().optional(),
                "severity": t.string().optional(),
                "eventTime": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "state": t.string().optional(),
                "moduleName": t.string().optional(),
                "category": t.string().optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "resourceName": t.string().optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsGroup"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "mute": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "canonicalName": t.string().optional(),
                "nextSteps": t.string().optional(),
                "muteInitiator": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "createTime": t.string().optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "description": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "findingClass": t.string().optional(),
                "externalUri": t.string().optional(),
                "severity": t.string().optional(),
                "eventTime": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "state": t.string().optional(),
                "moduleName": t.string().optional(),
                "category": t.string().optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "resourceName": t.string().optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsList"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "mute": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "canonicalName": t.string().optional(),
                "nextSteps": t.string().optional(),
                "muteInitiator": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "createTime": t.string().optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "description": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "findingClass": t.string().optional(),
                "externalUri": t.string().optional(),
                "severity": t.string().optional(),
                "eventTime": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "state": t.string().optional(),
                "moduleName": t.string().optional(),
                "category": t.string().optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "resourceName": t.string().optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsCreate"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "mute": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "canonicalName": t.string().optional(),
                "nextSteps": t.string().optional(),
                "muteInitiator": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "createTime": t.string().optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "description": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "findingClass": t.string().optional(),
                "externalUri": t.string().optional(),
                "severity": t.string().optional(),
                "eventTime": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "state": t.string().optional(),
                "moduleName": t.string().optional(),
                "category": t.string().optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "resourceName": t.string().optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesFindingsPatch"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "mute": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "canonicalName": t.string().optional(),
                "nextSteps": t.string().optional(),
                "muteInitiator": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "createTime": t.string().optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "description": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "findingClass": t.string().optional(),
                "externalUri": t.string().optional(),
                "severity": t.string().optional(),
                "eventTime": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "state": t.string().optional(),
                "moduleName": t.string().optional(),
                "category": t.string().optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "resourceName": t.string().optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "parent": t.string().optional(),
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
                "status": t.string().optional(),
                "externalSystemUpdateTime": t.string().optional(),
                "assignees": t.array(t.string()).optional(),
                "externalUid": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1ExternalSystemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersMuteConfigsGet"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "filter": t.string(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersMuteConfigsList"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "filter": t.string(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersMuteConfigsCreate"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "filter": t.string(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersMuteConfigsDelete"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "filter": t.string(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersMuteConfigsPatch"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "filter": t.string(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsCustomModulesCreate"
    ] = securitycenter.get(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecurityHealthAnalyticsCustomModulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsCustomModulesGet"
    ] = securitycenter.get(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecurityHealthAnalyticsCustomModulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsCustomModulesListDescendant"
    ] = securitycenter.get(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecurityHealthAnalyticsCustomModulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsCustomModulesPatch"
    ] = securitycenter.get(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecurityHealthAnalyticsCustomModulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsCustomModulesDelete"
    ] = securitycenter.get(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecurityHealthAnalyticsCustomModulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersSecurityHealthAnalyticsSettingsCustomModulesList"
    ] = securitycenter.get(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecurityHealthAnalyticsCustomModulesResponseOut"]),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["ListEffectiveSecurityHealthAnalyticsCustomModulesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersNotificationConfigsGet"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "pubsubTopic": t.string().optional(),
                "description": t.string().optional(),
                "streamingConfig": t.proxy(renames["StreamingConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersNotificationConfigsList"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "pubsubTopic": t.string().optional(),
                "description": t.string().optional(),
                "streamingConfig": t.proxy(renames["StreamingConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersNotificationConfigsDelete"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "pubsubTopic": t.string().optional(),
                "description": t.string().optional(),
                "streamingConfig": t.proxy(renames["StreamingConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersNotificationConfigsCreate"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "pubsubTopic": t.string().optional(),
                "description": t.string().optional(),
                "streamingConfig": t.proxy(renames["StreamingConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersNotificationConfigsPatch"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "pubsubTopic": t.string().optional(),
                "description": t.string().optional(),
                "streamingConfig": t.proxy(renames["StreamingConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesList"] = securitycenter.get(
        "v1/{parent}/sources",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsSetState"] = securitycenter.post(
        "v1/{parent}/findings:group",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "readTime": t.string().optional(),
                "groupBy": t.string(),
                "filter": t.string().optional(),
                "compareDuration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsSetMute"] = securitycenter.post(
        "v1/{parent}/findings:group",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "readTime": t.string().optional(),
                "groupBy": t.string(),
                "filter": t.string().optional(),
                "compareDuration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsPatch"] = securitycenter.post(
        "v1/{parent}/findings:group",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "readTime": t.string().optional(),
                "groupBy": t.string(),
                "filter": t.string().optional(),
                "compareDuration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsUpdateSecurityMarks"] = securitycenter.post(
        "v1/{parent}/findings:group",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "readTime": t.string().optional(),
                "groupBy": t.string(),
                "filter": t.string().optional(),
                "compareDuration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsList"] = securitycenter.post(
        "v1/{parent}/findings:group",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "readTime": t.string().optional(),
                "groupBy": t.string(),
                "filter": t.string().optional(),
                "compareDuration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsGroup"] = securitycenter.post(
        "v1/{parent}/findings:group",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "readTime": t.string().optional(),
                "groupBy": t.string(),
                "filter": t.string().optional(),
                "compareDuration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSourcesFindingsExternalSystemsPatch"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "status": t.string().optional(),
                "externalSystemUpdateTime": t.string().optional(),
                "assignees": t.array(t.string()).optional(),
                "externalUid": t.string().optional(),
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
    functions["foldersBigQueryExportsDelete"] = securitycenter.get(
        "v1/{parent}/bigQueryExports",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBigQueryExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersBigQueryExportsGet"] = securitycenter.get(
        "v1/{parent}/bigQueryExports",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBigQueryExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersAssetsUpdateSecurityMarks"] = securitycenter.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "fieldMask": t.string().optional(),
                "parent": t.string(),
                "compareDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersAssetsGroup"] = securitycenter.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "fieldMask": t.string().optional(),
                "parent": t.string(),
                "compareDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersAssetsList"] = securitycenter.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "fieldMask": t.string().optional(),
                "parent": t.string(),
                "compareDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMuteConfigsDelete"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMuteConfigsCreate"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMuteConfigsPatch"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMuteConfigsList"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMuteConfigsGet"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationConfigsPatch"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationConfigsDelete"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationConfigsList"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationConfigsCreate"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationConfigsGet"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSourcesFindingsSetMute"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "mute": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "canonicalName": t.string().optional(),
                "nextSteps": t.string().optional(),
                "muteInitiator": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "createTime": t.string().optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "description": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "findingClass": t.string().optional(),
                "externalUri": t.string().optional(),
                "severity": t.string().optional(),
                "eventTime": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "state": t.string().optional(),
                "moduleName": t.string().optional(),
                "category": t.string().optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "resourceName": t.string().optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSourcesFindingsUpdateSecurityMarks"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "mute": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "canonicalName": t.string().optional(),
                "nextSteps": t.string().optional(),
                "muteInitiator": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "createTime": t.string().optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "description": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "findingClass": t.string().optional(),
                "externalUri": t.string().optional(),
                "severity": t.string().optional(),
                "eventTime": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "state": t.string().optional(),
                "moduleName": t.string().optional(),
                "category": t.string().optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "resourceName": t.string().optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSourcesFindingsGroup"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "mute": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "canonicalName": t.string().optional(),
                "nextSteps": t.string().optional(),
                "muteInitiator": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "createTime": t.string().optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "description": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "findingClass": t.string().optional(),
                "externalUri": t.string().optional(),
                "severity": t.string().optional(),
                "eventTime": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "state": t.string().optional(),
                "moduleName": t.string().optional(),
                "category": t.string().optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "resourceName": t.string().optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSourcesFindingsList"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "mute": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "canonicalName": t.string().optional(),
                "nextSteps": t.string().optional(),
                "muteInitiator": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "createTime": t.string().optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "description": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "findingClass": t.string().optional(),
                "externalUri": t.string().optional(),
                "severity": t.string().optional(),
                "eventTime": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "state": t.string().optional(),
                "moduleName": t.string().optional(),
                "category": t.string().optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "resourceName": t.string().optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSourcesFindingsSetState"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "mute": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "canonicalName": t.string().optional(),
                "nextSteps": t.string().optional(),
                "muteInitiator": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "createTime": t.string().optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "description": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "findingClass": t.string().optional(),
                "externalUri": t.string().optional(),
                "severity": t.string().optional(),
                "eventTime": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "state": t.string().optional(),
                "moduleName": t.string().optional(),
                "category": t.string().optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "resourceName": t.string().optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSourcesFindingsPatch"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "mute": t.string().optional(),
                "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
                "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "cloudDlpInspection": t.proxy(
                    renames["CloudDlpInspectionIn"]
                ).optional(),
                "cloudDlpDataProfile": t.proxy(
                    renames["CloudDlpDataProfileIn"]
                ).optional(),
                "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
                "canonicalName": t.string().optional(),
                "nextSteps": t.string().optional(),
                "muteInitiator": t.string().optional(),
                "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
                "createTime": t.string().optional(),
                "indicator": t.proxy(renames["IndicatorIn"]).optional(),
                "description": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "findingClass": t.string().optional(),
                "externalUri": t.string().optional(),
                "severity": t.string().optional(),
                "eventTime": t.string().optional(),
                "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
                "state": t.string().optional(),
                "moduleName": t.string().optional(),
                "category": t.string().optional(),
                "access": t.proxy(renames["AccessIn"]).optional(),
                "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
                "resourceName": t.string().optional(),
                "database": t.proxy(renames["DatabaseIn"]).optional(),
                "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
                "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
                "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
                "parent": t.string().optional(),
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
                "status": t.string().optional(),
                "externalSystemUpdateTime": t.string().optional(),
                "assignees": t.array(t.string()).optional(),
                "externalUid": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1ExternalSystemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAssetsGroup"] = securitycenter.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "readTime": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "fieldMask": t.string().optional(),
                "filter": t.string().optional(),
                "compareDuration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAssetsUpdateSecurityMarks"] = securitycenter.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "readTime": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "fieldMask": t.string().optional(),
                "filter": t.string().optional(),
                "compareDuration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAssetsList"] = securitycenter.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "readTime": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "fieldMask": t.string().optional(),
                "filter": t.string().optional(),
                "compareDuration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsSecurityHealthAnalyticsSettingsCustomModulesListDescendant"
    ] = securitycenter.post(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "enablementState": t.string().optional(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
                "name": t.string().optional(),
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
    ] = securitycenter.post(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "enablementState": t.string().optional(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
                "name": t.string().optional(),
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
        "projectsSecurityHealthAnalyticsSettingsCustomModulesList"
    ] = securitycenter.post(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "enablementState": t.string().optional(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
                "name": t.string().optional(),
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
    ] = securitycenter.post(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "enablementState": t.string().optional(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
                "name": t.string().optional(),
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
    ] = securitycenter.post(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "enablementState": t.string().optional(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
                "name": t.string().optional(),
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
    ] = securitycenter.post(
        "v1/{parent}/customModules",
        t.struct(
            {
                "parent": t.string(),
                "enablementState": t.string().optional(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
                "name": t.string().optional(),
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

    return Import(
        importer="securitycenter",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
