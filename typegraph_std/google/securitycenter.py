from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_securitycenter():
    securitycenter = HTTPRuntime("https://securitycenter.googleapis.com/")

    renames = {
        "ErrorResponse": "_securitycenter_1_ErrorResponse",
        "GoogleCloudSecuritycenterV1p1beta1NotificationMessageIn": "_securitycenter_2_GoogleCloudSecuritycenterV1p1beta1NotificationMessageIn",
        "GoogleCloudSecuritycenterV1p1beta1NotificationMessageOut": "_securitycenter_3_GoogleCloudSecuritycenterV1p1beta1NotificationMessageOut",
        "OperationIn": "_securitycenter_4_OperationIn",
        "OperationOut": "_securitycenter_5_OperationOut",
        "FolderIn": "_securitycenter_6_FolderIn",
        "FolderOut": "_securitycenter_7_FolderOut",
        "ExprIn": "_securitycenter_8_ExprIn",
        "ExprOut": "_securitycenter_9_ExprOut",
        "GroupFindingsRequestIn": "_securitycenter_10_GroupFindingsRequestIn",
        "GroupFindingsRequestOut": "_securitycenter_11_GroupFindingsRequestOut",
        "IamBindingIn": "_securitycenter_12_IamBindingIn",
        "IamBindingOut": "_securitycenter_13_IamBindingOut",
        "LabelIn": "_securitycenter_14_LabelIn",
        "LabelOut": "_securitycenter_15_LabelOut",
        "StreamingConfigIn": "_securitycenter_16_StreamingConfigIn",
        "StreamingConfigOut": "_securitycenter_17_StreamingConfigOut",
        "FileIn": "_securitycenter_18_FileIn",
        "FileOut": "_securitycenter_19_FileOut",
        "ListEffectiveSecurityHealthAnalyticsCustomModulesResponseIn": "_securitycenter_20_ListEffectiveSecurityHealthAnalyticsCustomModulesResponseIn",
        "ListEffectiveSecurityHealthAnalyticsCustomModulesResponseOut": "_securitycenter_21_ListEffectiveSecurityHealthAnalyticsCustomModulesResponseOut",
        "ContactDetailsIn": "_securitycenter_22_ContactDetailsIn",
        "ContactDetailsOut": "_securitycenter_23_ContactDetailsOut",
        "GetPolicyOptionsIn": "_securitycenter_24_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_securitycenter_25_GetPolicyOptionsOut",
        "RunAssetDiscoveryRequestIn": "_securitycenter_26_RunAssetDiscoveryRequestIn",
        "RunAssetDiscoveryRequestOut": "_securitycenter_27_RunAssetDiscoveryRequestOut",
        "GoogleCloudSecuritycenterV1p1beta1FolderIn": "_securitycenter_28_GoogleCloudSecuritycenterV1p1beta1FolderIn",
        "GoogleCloudSecuritycenterV1p1beta1FolderOut": "_securitycenter_29_GoogleCloudSecuritycenterV1p1beta1FolderOut",
        "SetMuteRequestIn": "_securitycenter_30_SetMuteRequestIn",
        "SetMuteRequestOut": "_securitycenter_31_SetMuteRequestOut",
        "GroupAssetsResponseIn": "_securitycenter_32_GroupAssetsResponseIn",
        "GroupAssetsResponseOut": "_securitycenter_33_GroupAssetsResponseOut",
        "GoogleCloudSecuritycenterV1BigQueryExportIn": "_securitycenter_34_GoogleCloudSecuritycenterV1BigQueryExportIn",
        "GoogleCloudSecuritycenterV1BigQueryExportOut": "_securitycenter_35_GoogleCloudSecuritycenterV1BigQueryExportOut",
        "StatusIn": "_securitycenter_36_StatusIn",
        "StatusOut": "_securitycenter_37_StatusOut",
        "ResourceIn": "_securitycenter_38_ResourceIn",
        "ResourceOut": "_securitycenter_39_ResourceOut",
        "BindingIn": "_securitycenter_40_BindingIn",
        "BindingOut": "_securitycenter_41_BindingOut",
        "GoogleCloudSecuritycenterV1MuteConfigIn": "_securitycenter_42_GoogleCloudSecuritycenterV1MuteConfigIn",
        "GoogleCloudSecuritycenterV1MuteConfigOut": "_securitycenter_43_GoogleCloudSecuritycenterV1MuteConfigOut",
        "GoogleCloudSecuritycenterV1BulkMuteFindingsResponseIn": "_securitycenter_44_GoogleCloudSecuritycenterV1BulkMuteFindingsResponseIn",
        "GoogleCloudSecuritycenterV1BulkMuteFindingsResponseOut": "_securitycenter_45_GoogleCloudSecuritycenterV1BulkMuteFindingsResponseOut",
        "GoogleCloudSecuritycenterV1CustomOutputSpecIn": "_securitycenter_46_GoogleCloudSecuritycenterV1CustomOutputSpecIn",
        "GoogleCloudSecuritycenterV1CustomOutputSpecOut": "_securitycenter_47_GoogleCloudSecuritycenterV1CustomOutputSpecOut",
        "RoleIn": "_securitycenter_48_RoleIn",
        "RoleOut": "_securitycenter_49_RoleOut",
        "GoogleCloudSecuritycenterV1p1beta1FindingIn": "_securitycenter_50_GoogleCloudSecuritycenterV1p1beta1FindingIn",
        "GoogleCloudSecuritycenterV1p1beta1FindingOut": "_securitycenter_51_GoogleCloudSecuritycenterV1p1beta1FindingOut",
        "OrganizationSettingsIn": "_securitycenter_52_OrganizationSettingsIn",
        "OrganizationSettingsOut": "_securitycenter_53_OrganizationSettingsOut",
        "ListAssetsResponseIn": "_securitycenter_54_ListAssetsResponseIn",
        "ListAssetsResponseOut": "_securitycenter_55_ListAssetsResponseOut",
        "ProcessIn": "_securitycenter_56_ProcessIn",
        "ProcessOut": "_securitycenter_57_ProcessOut",
        "AccessIn": "_securitycenter_58_AccessIn",
        "AccessOut": "_securitycenter_59_AccessOut",
        "GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseIn": "_securitycenter_60_GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseIn",
        "GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseOut": "_securitycenter_61_GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponseOut",
        "MemoryHashSignatureIn": "_securitycenter_62_MemoryHashSignatureIn",
        "MemoryHashSignatureOut": "_securitycenter_63_MemoryHashSignatureOut",
        "ListFindingsResultIn": "_securitycenter_64_ListFindingsResultIn",
        "ListFindingsResultOut": "_securitycenter_65_ListFindingsResultOut",
        "TestIamPermissionsResponseIn": "_securitycenter_66_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_securitycenter_67_TestIamPermissionsResponseOut",
        "ReferenceIn": "_securitycenter_68_ReferenceIn",
        "ReferenceOut": "_securitycenter_69_ReferenceOut",
        "EmptyIn": "_securitycenter_70_EmptyIn",
        "EmptyOut": "_securitycenter_71_EmptyOut",
        "ListFindingsResponseIn": "_securitycenter_72_ListFindingsResponseIn",
        "ListFindingsResponseOut": "_securitycenter_73_ListFindingsResponseOut",
        "GoogleCloudSecuritycenterV1p1beta1ResourceIn": "_securitycenter_74_GoogleCloudSecuritycenterV1p1beta1ResourceIn",
        "GoogleCloudSecuritycenterV1p1beta1ResourceOut": "_securitycenter_75_GoogleCloudSecuritycenterV1p1beta1ResourceOut",
        "SetFindingStateRequestIn": "_securitycenter_76_SetFindingStateRequestIn",
        "SetFindingStateRequestOut": "_securitycenter_77_SetFindingStateRequestOut",
        "GoogleCloudSecuritycenterV1ResourceIn": "_securitycenter_78_GoogleCloudSecuritycenterV1ResourceIn",
        "GoogleCloudSecuritycenterV1ResourceOut": "_securitycenter_79_GoogleCloudSecuritycenterV1ResourceOut",
        "GroupFindingsResponseIn": "_securitycenter_80_GroupFindingsResponseIn",
        "GroupFindingsResponseOut": "_securitycenter_81_GroupFindingsResponseOut",
        "GoogleCloudSecuritycenterV1p1beta1SecurityMarksIn": "_securitycenter_82_GoogleCloudSecuritycenterV1p1beta1SecurityMarksIn",
        "GoogleCloudSecuritycenterV1p1beta1SecurityMarksOut": "_securitycenter_83_GoogleCloudSecuritycenterV1p1beta1SecurityMarksOut",
        "ListSourcesResponseIn": "_securitycenter_84_ListSourcesResponseIn",
        "ListSourcesResponseOut": "_securitycenter_85_ListSourcesResponseOut",
        "AssetDiscoveryConfigIn": "_securitycenter_86_AssetDiscoveryConfigIn",
        "AssetDiscoveryConfigOut": "_securitycenter_87_AssetDiscoveryConfigOut",
        "GoogleCloudSecuritycenterV1BindingIn": "_securitycenter_88_GoogleCloudSecuritycenterV1BindingIn",
        "GoogleCloudSecuritycenterV1BindingOut": "_securitycenter_89_GoogleCloudSecuritycenterV1BindingOut",
        "Cvssv3In": "_securitycenter_90_Cvssv3In",
        "Cvssv3Out": "_securitycenter_91_Cvssv3Out",
        "SourceIn": "_securitycenter_92_SourceIn",
        "SourceOut": "_securitycenter_93_SourceOut",
        "GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseIn": "_securitycenter_94_GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseIn",
        "GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseOut": "_securitycenter_95_GoogleCloudSecuritycenterV1RunAssetDiscoveryResponseOut",
        "PolicyIn": "_securitycenter_96_PolicyIn",
        "PolicyOut": "_securitycenter_97_PolicyOut",
        "ListNotificationConfigsResponseIn": "_securitycenter_98_ListNotificationConfigsResponseIn",
        "ListNotificationConfigsResponseOut": "_securitycenter_99_ListNotificationConfigsResponseOut",
        "DatabaseIn": "_securitycenter_100_DatabaseIn",
        "DatabaseOut": "_securitycenter_101_DatabaseOut",
        "ListOperationsResponseIn": "_securitycenter_102_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_securitycenter_103_ListOperationsResponseOut",
        "NodeIn": "_securitycenter_104_NodeIn",
        "NodeOut": "_securitycenter_105_NodeOut",
        "ProcessSignatureIn": "_securitycenter_106_ProcessSignatureIn",
        "ProcessSignatureOut": "_securitycenter_107_ProcessSignatureOut",
        "SecurityCenterPropertiesIn": "_securitycenter_108_SecurityCenterPropertiesIn",
        "SecurityCenterPropertiesOut": "_securitycenter_109_SecurityCenterPropertiesOut",
        "ListBigQueryExportsResponseIn": "_securitycenter_110_ListBigQueryExportsResponseIn",
        "ListBigQueryExportsResponseOut": "_securitycenter_111_ListBigQueryExportsResponseOut",
        "CloudDlpInspectionIn": "_securitycenter_112_CloudDlpInspectionIn",
        "CloudDlpInspectionOut": "_securitycenter_113_CloudDlpInspectionOut",
        "GoogleCloudSecuritycenterV1ResourceSelectorIn": "_securitycenter_114_GoogleCloudSecuritycenterV1ResourceSelectorIn",
        "GoogleCloudSecuritycenterV1ResourceSelectorOut": "_securitycenter_115_GoogleCloudSecuritycenterV1ResourceSelectorOut",
        "AuditLogConfigIn": "_securitycenter_116_AuditLogConfigIn",
        "AuditLogConfigOut": "_securitycenter_117_AuditLogConfigOut",
        "AssetIn": "_securitycenter_118_AssetIn",
        "AssetOut": "_securitycenter_119_AssetOut",
        "GoogleCloudSecuritycenterV1PropertyIn": "_securitycenter_120_GoogleCloudSecuritycenterV1PropertyIn",
        "GoogleCloudSecuritycenterV1PropertyOut": "_securitycenter_121_GoogleCloudSecuritycenterV1PropertyOut",
        "IndicatorIn": "_securitycenter_122_IndicatorIn",
        "IndicatorOut": "_securitycenter_123_IndicatorOut",
        "DetectionIn": "_securitycenter_124_DetectionIn",
        "DetectionOut": "_securitycenter_125_DetectionOut",
        "ListMuteConfigsResponseIn": "_securitycenter_126_ListMuteConfigsResponseIn",
        "ListMuteConfigsResponseOut": "_securitycenter_127_ListMuteConfigsResponseOut",
        "ServiceAccountDelegationInfoIn": "_securitycenter_128_ServiceAccountDelegationInfoIn",
        "ServiceAccountDelegationInfoOut": "_securitycenter_129_ServiceAccountDelegationInfoOut",
        "ContainerIn": "_securitycenter_130_ContainerIn",
        "ContainerOut": "_securitycenter_131_ContainerOut",
        "ExfilResourceIn": "_securitycenter_132_ExfilResourceIn",
        "ExfilResourceOut": "_securitycenter_133_ExfilResourceOut",
        "AccessReviewIn": "_securitycenter_134_AccessReviewIn",
        "AccessReviewOut": "_securitycenter_135_AccessReviewOut",
        "NodePoolIn": "_securitycenter_136_NodePoolIn",
        "NodePoolOut": "_securitycenter_137_NodePoolOut",
        "YaraRuleSignatureIn": "_securitycenter_138_YaraRuleSignatureIn",
        "YaraRuleSignatureOut": "_securitycenter_139_YaraRuleSignatureOut",
        "ContactIn": "_securitycenter_140_ContactIn",
        "ContactOut": "_securitycenter_141_ContactOut",
        "EnvironmentVariableIn": "_securitycenter_142_EnvironmentVariableIn",
        "EnvironmentVariableOut": "_securitycenter_143_EnvironmentVariableOut",
        "MitreAttackIn": "_securitycenter_144_MitreAttackIn",
        "MitreAttackOut": "_securitycenter_145_MitreAttackOut",
        "NotificationConfigIn": "_securitycenter_146_NotificationConfigIn",
        "NotificationConfigOut": "_securitycenter_147_NotificationConfigOut",
        "TestIamPermissionsRequestIn": "_securitycenter_148_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_securitycenter_149_TestIamPermissionsRequestOut",
        "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleIn": "_securitycenter_150_GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleIn",
        "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleOut": "_securitycenter_151_GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleOut",
        "GoogleCloudSecuritycenterV1NotificationMessageIn": "_securitycenter_152_GoogleCloudSecuritycenterV1NotificationMessageIn",
        "GoogleCloudSecuritycenterV1NotificationMessageOut": "_securitycenter_153_GoogleCloudSecuritycenterV1NotificationMessageOut",
        "GroupAssetsRequestIn": "_securitycenter_154_GroupAssetsRequestIn",
        "GroupAssetsRequestOut": "_securitycenter_155_GroupAssetsRequestOut",
        "FindingIn": "_securitycenter_156_FindingIn",
        "FindingOut": "_securitycenter_157_FindingOut",
        "ListDescendantSecurityHealthAnalyticsCustomModulesResponseIn": "_securitycenter_158_ListDescendantSecurityHealthAnalyticsCustomModulesResponseIn",
        "ListDescendantSecurityHealthAnalyticsCustomModulesResponseOut": "_securitycenter_159_ListDescendantSecurityHealthAnalyticsCustomModulesResponseOut",
        "BulkMuteFindingsRequestIn": "_securitycenter_160_BulkMuteFindingsRequestIn",
        "BulkMuteFindingsRequestOut": "_securitycenter_161_BulkMuteFindingsRequestOut",
        "IamPolicyIn": "_securitycenter_162_IamPolicyIn",
        "IamPolicyOut": "_securitycenter_163_IamPolicyOut",
        "CveIn": "_securitycenter_164_CveIn",
        "CveOut": "_securitycenter_165_CveOut",
        "SubjectIn": "_securitycenter_166_SubjectIn",
        "SubjectOut": "_securitycenter_167_SubjectOut",
        "GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseIn": "_securitycenter_168_GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseIn",
        "GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseOut": "_securitycenter_169_GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponseOut",
        "SetIamPolicyRequestIn": "_securitycenter_170_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_securitycenter_171_SetIamPolicyRequestOut",
        "ComplianceIn": "_securitycenter_172_ComplianceIn",
        "ComplianceOut": "_securitycenter_173_ComplianceOut",
        "GroupResultIn": "_securitycenter_174_GroupResultIn",
        "GroupResultOut": "_securitycenter_175_GroupResultOut",
        "ListSecurityHealthAnalyticsCustomModulesResponseIn": "_securitycenter_176_ListSecurityHealthAnalyticsCustomModulesResponseIn",
        "ListSecurityHealthAnalyticsCustomModulesResponseOut": "_securitycenter_177_ListSecurityHealthAnalyticsCustomModulesResponseOut",
        "GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleIn": "_securitycenter_178_GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleIn",
        "GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut": "_securitycenter_179_GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut",
        "GoogleCloudSecuritycenterV1CustomConfigIn": "_securitycenter_180_GoogleCloudSecuritycenterV1CustomConfigIn",
        "GoogleCloudSecuritycenterV1CustomConfigOut": "_securitycenter_181_GoogleCloudSecuritycenterV1CustomConfigOut",
        "CloudDlpDataProfileIn": "_securitycenter_182_CloudDlpDataProfileIn",
        "CloudDlpDataProfileOut": "_securitycenter_183_CloudDlpDataProfileOut",
        "AuditConfigIn": "_securitycenter_184_AuditConfigIn",
        "AuditConfigOut": "_securitycenter_185_AuditConfigOut",
        "GeolocationIn": "_securitycenter_186_GeolocationIn",
        "GeolocationOut": "_securitycenter_187_GeolocationOut",
        "KernelRootkitIn": "_securitycenter_188_KernelRootkitIn",
        "KernelRootkitOut": "_securitycenter_189_KernelRootkitOut",
        "ConnectionIn": "_securitycenter_190_ConnectionIn",
        "ConnectionOut": "_securitycenter_191_ConnectionOut",
        "ExfiltrationIn": "_securitycenter_192_ExfiltrationIn",
        "ExfiltrationOut": "_securitycenter_193_ExfiltrationOut",
        "ListAssetsResultIn": "_securitycenter_194_ListAssetsResultIn",
        "ListAssetsResultOut": "_securitycenter_195_ListAssetsResultOut",
        "SecurityMarksIn": "_securitycenter_196_SecurityMarksIn",
        "SecurityMarksOut": "_securitycenter_197_SecurityMarksOut",
        "PodIn": "_securitycenter_198_PodIn",
        "PodOut": "_securitycenter_199_PodOut",
        "GetIamPolicyRequestIn": "_securitycenter_200_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_securitycenter_201_GetIamPolicyRequestOut",
        "VulnerabilityIn": "_securitycenter_202_VulnerabilityIn",
        "VulnerabilityOut": "_securitycenter_203_VulnerabilityOut",
        "KubernetesIn": "_securitycenter_204_KubernetesIn",
        "KubernetesOut": "_securitycenter_205_KubernetesOut",
        "GoogleCloudSecuritycenterV1ExternalSystemIn": "_securitycenter_206_GoogleCloudSecuritycenterV1ExternalSystemIn",
        "GoogleCloudSecuritycenterV1ExternalSystemOut": "_securitycenter_207_GoogleCloudSecuritycenterV1ExternalSystemOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudSecuritycenterV1p1beta1NotificationMessageIn"] = t.struct(
        {
            "resource": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1ResourceIn"]
            ).optional(),
            "notificationConfigName": t.string().optional(),
            "finding": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1FindingIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1NotificationMessageIn"])
    types["GoogleCloudSecuritycenterV1p1beta1NotificationMessageOut"] = t.struct(
        {
            "resource": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1ResourceOut"]
            ).optional(),
            "notificationConfigName": t.string().optional(),
            "finding": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1FindingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1NotificationMessageOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["GroupFindingsRequestIn"] = t.struct(
        {
            "groupBy": t.string(),
            "filter": t.string().optional(),
            "pageSize": t.integer().optional(),
            "readTime": t.string().optional(),
            "compareDuration": t.string().optional(),
            "pageToken": t.string().optional(),
        }
    ).named(renames["GroupFindingsRequestIn"])
    types["GroupFindingsRequestOut"] = t.struct(
        {
            "groupBy": t.string(),
            "filter": t.string().optional(),
            "pageSize": t.integer().optional(),
            "readTime": t.string().optional(),
            "compareDuration": t.string().optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupFindingsRequestOut"])
    types["IamBindingIn"] = t.struct(
        {
            "action": t.string().optional(),
            "member": t.string().optional(),
            "role": t.string().optional(),
        }
    ).named(renames["IamBindingIn"])
    types["IamBindingOut"] = t.struct(
        {
            "action": t.string().optional(),
            "member": t.string().optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamBindingOut"])
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
    types["StreamingConfigIn"] = t.struct({"filter": t.string().optional()}).named(
        renames["StreamingConfigIn"]
    )
    types["StreamingConfigOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingConfigOut"])
    types["FileIn"] = t.struct(
        {
            "partiallyHashed": t.boolean().optional(),
            "size": t.string().optional(),
            "path": t.string().optional(),
            "hashedSize": t.string().optional(),
            "contents": t.string().optional(),
            "sha256": t.string().optional(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "partiallyHashed": t.boolean().optional(),
            "size": t.string().optional(),
            "path": t.string().optional(),
            "hashedSize": t.string().optional(),
            "contents": t.string().optional(),
            "sha256": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
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
    types["ContactDetailsIn"] = t.struct(
        {"contacts": t.array(t.proxy(renames["ContactIn"])).optional()}
    ).named(renames["ContactDetailsIn"])
    types["ContactDetailsOut"] = t.struct(
        {
            "contacts": t.array(t.proxy(renames["ContactOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactDetailsOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["RunAssetDiscoveryRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RunAssetDiscoveryRequestIn"]
    )
    types["RunAssetDiscoveryRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RunAssetDiscoveryRequestOut"])
    types["GoogleCloudSecuritycenterV1p1beta1FolderIn"] = t.struct(
        {
            "resourceFolderDisplayName": t.string().optional(),
            "resourceFolder": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1FolderIn"])
    types["GoogleCloudSecuritycenterV1p1beta1FolderOut"] = t.struct(
        {
            "resourceFolderDisplayName": t.string().optional(),
            "resourceFolder": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1FolderOut"])
    types["SetMuteRequestIn"] = t.struct({"mute": t.string()}).named(
        renames["SetMuteRequestIn"]
    )
    types["SetMuteRequestOut"] = t.struct(
        {"mute": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SetMuteRequestOut"])
    types["GroupAssetsResponseIn"] = t.struct(
        {
            "groupByResults": t.array(t.proxy(renames["GroupResultIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["GroupAssetsResponseIn"])
    types["GroupAssetsResponseOut"] = t.struct(
        {
            "groupByResults": t.array(t.proxy(renames["GroupResultOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupAssetsResponseOut"])
    types["GoogleCloudSecuritycenterV1BigQueryExportIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "filter": t.string().optional(),
            "dataset": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1BigQueryExportIn"])
    types["GoogleCloudSecuritycenterV1BigQueryExportOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "mostRecentEditor": t.string().optional(),
            "filter": t.string().optional(),
            "principal": t.string().optional(),
            "dataset": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"])
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
    types["ResourceIn"] = t.struct(
        {
            "parentName": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "projectDisplayName": t.string().optional(),
            "displayName": t.string().optional(),
            "projectName": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderIn"])).optional(),
            "parentDisplayName": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "parentName": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "projectDisplayName": t.string().optional(),
            "displayName": t.string().optional(),
            "projectName": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderOut"])).optional(),
            "parentDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
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
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "filter": t.string(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "mostRecentEditor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1MuteConfigOut"])
    types["GoogleCloudSecuritycenterV1BulkMuteFindingsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudSecuritycenterV1BulkMuteFindingsResponseIn"])
    types["GoogleCloudSecuritycenterV1BulkMuteFindingsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudSecuritycenterV1BulkMuteFindingsResponseOut"])
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
    types["RoleIn"] = t.struct(
        {
            "ns": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["RoleIn"])
    types["RoleOut"] = t.struct(
        {
            "ns": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoleOut"])
    types["GoogleCloudSecuritycenterV1p1beta1FindingIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "category": t.string().optional(),
            "externalUri": t.string().optional(),
            "name": t.string().optional(),
            "eventTime": t.string().optional(),
            "state": t.string().optional(),
            "parent": t.string().optional(),
            "canonicalName": t.string().optional(),
            "createTime": t.string().optional(),
            "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "resourceName": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1FindingIn"])
    types["GoogleCloudSecuritycenterV1p1beta1FindingOut"] = t.struct(
        {
            "securityMarks": t.proxy(
                renames["GoogleCloudSecuritycenterV1p1beta1SecurityMarksOut"]
            ).optional(),
            "severity": t.string().optional(),
            "category": t.string().optional(),
            "externalUri": t.string().optional(),
            "name": t.string().optional(),
            "eventTime": t.string().optional(),
            "state": t.string().optional(),
            "parent": t.string().optional(),
            "canonicalName": t.string().optional(),
            "createTime": t.string().optional(),
            "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1FindingOut"])
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
    types["ListAssetsResponseIn"] = t.struct(
        {
            "readTime": t.string().optional(),
            "listAssetsResults": t.array(
                t.proxy(renames["ListAssetsResultIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListAssetsResponseIn"])
    types["ListAssetsResponseOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "listAssetsResults": t.array(
                t.proxy(renames["ListAssetsResultOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssetsResponseOut"])
    types["ProcessIn"] = t.struct(
        {
            "argumentsTruncated": t.boolean().optional(),
            "name": t.string().optional(),
            "script": t.proxy(renames["FileIn"]).optional(),
            "parentPid": t.string().optional(),
            "pid": t.string().optional(),
            "envVariablesTruncated": t.boolean().optional(),
            "binary": t.proxy(renames["FileIn"]).optional(),
            "args": t.array(t.string()).optional(),
            "envVariables": t.array(
                t.proxy(renames["EnvironmentVariableIn"])
            ).optional(),
            "libraries": t.array(t.proxy(renames["FileIn"])).optional(),
        }
    ).named(renames["ProcessIn"])
    types["ProcessOut"] = t.struct(
        {
            "argumentsTruncated": t.boolean().optional(),
            "name": t.string().optional(),
            "script": t.proxy(renames["FileOut"]).optional(),
            "parentPid": t.string().optional(),
            "pid": t.string().optional(),
            "envVariablesTruncated": t.boolean().optional(),
            "binary": t.proxy(renames["FileOut"]).optional(),
            "args": t.array(t.string()).optional(),
            "envVariables": t.array(
                t.proxy(renames["EnvironmentVariableOut"])
            ).optional(),
            "libraries": t.array(t.proxy(renames["FileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProcessOut"])
    types["AccessIn"] = t.struct(
        {
            "serviceAccountKeyName": t.string().optional(),
            "callerIpGeo": t.proxy(renames["GeolocationIn"]).optional(),
            "principalEmail": t.string().optional(),
            "callerIp": t.string().optional(),
            "methodName": t.string().optional(),
            "principalSubject": t.string().optional(),
            "userAgent": t.string().optional(),
            "userName": t.string().optional(),
            "serviceAccountDelegationInfo": t.array(
                t.proxy(renames["ServiceAccountDelegationInfoIn"])
            ).optional(),
            "userAgentFamily": t.string().optional(),
            "serviceName": t.string().optional(),
        }
    ).named(renames["AccessIn"])
    types["AccessOut"] = t.struct(
        {
            "serviceAccountKeyName": t.string().optional(),
            "callerIpGeo": t.proxy(renames["GeolocationOut"]).optional(),
            "principalEmail": t.string().optional(),
            "callerIp": t.string().optional(),
            "methodName": t.string().optional(),
            "principalSubject": t.string().optional(),
            "userAgent": t.string().optional(),
            "userName": t.string().optional(),
            "serviceAccountDelegationInfo": t.array(
                t.proxy(renames["ServiceAccountDelegationInfoOut"])
            ).optional(),
            "userAgentFamily": t.string().optional(),
            "serviceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListFindingsResponseIn"] = t.struct(
        {
            "readTime": t.string().optional(),
            "totalSize": t.integer().optional(),
            "listFindingsResults": t.array(
                t.proxy(renames["ListFindingsResultIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListFindingsResponseIn"])
    types["ListFindingsResponseOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "totalSize": t.integer().optional(),
            "listFindingsResults": t.array(
                t.proxy(renames["ListFindingsResultOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFindingsResponseOut"])
    types["GoogleCloudSecuritycenterV1p1beta1ResourceIn"] = t.struct(
        {
            "projectDisplayName": t.string().optional(),
            "project": t.string().optional(),
            "name": t.string().optional(),
            "parentDisplayName": t.string().optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1ResourceIn"])
    types["GoogleCloudSecuritycenterV1p1beta1ResourceOut"] = t.struct(
        {
            "projectDisplayName": t.string().optional(),
            "project": t.string().optional(),
            "name": t.string().optional(),
            "parentDisplayName": t.string().optional(),
            "folders": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1p1beta1FolderOut"])
            ).optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1p1beta1ResourceOut"])
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
    types["GoogleCloudSecuritycenterV1ResourceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "parent": t.string().optional(),
            "parentDisplayName": t.string().optional(),
            "project": t.string().optional(),
            "projectDisplayName": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ResourceIn"])
    types["GoogleCloudSecuritycenterV1ResourceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderOut"])).optional(),
            "parent": t.string().optional(),
            "parentDisplayName": t.string().optional(),
            "project": t.string().optional(),
            "projectDisplayName": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ResourceOut"])
    types["GroupFindingsResponseIn"] = t.struct(
        {
            "readTime": t.string().optional(),
            "groupByResults": t.array(t.proxy(renames["GroupResultIn"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GroupFindingsResponseIn"])
    types["GroupFindingsResponseOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "groupByResults": t.array(t.proxy(renames["GroupResultOut"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupFindingsResponseOut"])
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
    types["ListSourcesResponseIn"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSourcesResponseIn"])
    types["ListSourcesResponseOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSourcesResponseOut"])
    types["AssetDiscoveryConfigIn"] = t.struct(
        {
            "inclusionMode": t.string().optional(),
            "projectIds": t.array(t.string()).optional(),
            "folderIds": t.array(t.string()).optional(),
        }
    ).named(renames["AssetDiscoveryConfigIn"])
    types["AssetDiscoveryConfigOut"] = t.struct(
        {
            "inclusionMode": t.string().optional(),
            "projectIds": t.array(t.string()).optional(),
            "folderIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetDiscoveryConfigOut"])
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
    types["Cvssv3In"] = t.struct(
        {
            "attackComplexity": t.string().optional(),
            "attackVector": t.string().optional(),
            "scope": t.string().optional(),
            "integrityImpact": t.string().optional(),
            "userInteraction": t.string().optional(),
            "confidentialityImpact": t.string().optional(),
            "privilegesRequired": t.string().optional(),
            "availabilityImpact": t.string().optional(),
            "baseScore": t.number().optional(),
        }
    ).named(renames["Cvssv3In"])
    types["Cvssv3Out"] = t.struct(
        {
            "attackComplexity": t.string().optional(),
            "attackVector": t.string().optional(),
            "scope": t.string().optional(),
            "integrityImpact": t.string().optional(),
            "userInteraction": t.string().optional(),
            "confidentialityImpact": t.string().optional(),
            "privilegesRequired": t.string().optional(),
            "availabilityImpact": t.string().optional(),
            "baseScore": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Cvssv3Out"])
    types["SourceIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "canonicalName": t.string().optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "canonicalName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["DatabaseIn"] = t.struct(
        {
            "userName": t.string().optional(),
            "grantees": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "query": t.string().optional(),
        }
    ).named(renames["DatabaseIn"])
    types["DatabaseOut"] = t.struct(
        {
            "userName": t.string().optional(),
            "grantees": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseOut"])
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
    types["NodeIn"] = t.struct({"name": t.string().optional()}).named(renames["NodeIn"])
    types["NodeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeOut"])
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
    types["SecurityCenterPropertiesIn"] = t.struct(
        {
            "resourceProject": t.string().optional(),
            "resourceParent": t.string().optional(),
            "resourceName": t.string().optional(),
            "resourceDisplayName": t.string().optional(),
            "resourceType": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderIn"])).optional(),
            "resourceParentDisplayName": t.string().optional(),
            "resourceProjectDisplayName": t.string().optional(),
            "resourceOwners": t.array(t.string()).optional(),
        }
    ).named(renames["SecurityCenterPropertiesIn"])
    types["SecurityCenterPropertiesOut"] = t.struct(
        {
            "resourceProject": t.string().optional(),
            "resourceParent": t.string().optional(),
            "resourceName": t.string().optional(),
            "resourceDisplayName": t.string().optional(),
            "resourceType": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderOut"])).optional(),
            "resourceParentDisplayName": t.string().optional(),
            "resourceProjectDisplayName": t.string().optional(),
            "resourceOwners": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecurityCenterPropertiesOut"])
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
    types["CloudDlpInspectionIn"] = t.struct(
        {
            "infoType": t.string().optional(),
            "infoTypeCount": t.string().optional(),
            "inspectJob": t.string().optional(),
            "fullScan": t.boolean().optional(),
        }
    ).named(renames["CloudDlpInspectionIn"])
    types["CloudDlpInspectionOut"] = t.struct(
        {
            "infoType": t.string().optional(),
            "infoTypeCount": t.string().optional(),
            "inspectJob": t.string().optional(),
            "fullScan": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudDlpInspectionOut"])
    types["GoogleCloudSecuritycenterV1ResourceSelectorIn"] = t.struct(
        {"resourceTypes": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudSecuritycenterV1ResourceSelectorIn"])
    types["GoogleCloudSecuritycenterV1ResourceSelectorOut"] = t.struct(
        {
            "resourceTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ResourceSelectorOut"])
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
    types["AssetIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "securityCenterProperties": t.proxy(
                renames["SecurityCenterPropertiesIn"]
            ).optional(),
            "securityMarks": t.proxy(renames["SecurityMarksIn"]).optional(),
            "name": t.string().optional(),
            "canonicalName": t.string().optional(),
            "iamPolicy": t.proxy(renames["IamPolicyIn"]).optional(),
            "createTime": t.string().optional(),
            "resourceProperties": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "securityCenterProperties": t.proxy(
                renames["SecurityCenterPropertiesOut"]
            ).optional(),
            "securityMarks": t.proxy(renames["SecurityMarksOut"]).optional(),
            "name": t.string().optional(),
            "canonicalName": t.string().optional(),
            "iamPolicy": t.proxy(renames["IamPolicyOut"]).optional(),
            "createTime": t.string().optional(),
            "resourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
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
    types["IndicatorIn"] = t.struct(
        {
            "signatures": t.array(t.proxy(renames["ProcessSignatureIn"])).optional(),
            "ipAddresses": t.array(t.string()).optional(),
            "uris": t.array(t.string()).optional(),
            "domains": t.array(t.string()).optional(),
        }
    ).named(renames["IndicatorIn"])
    types["IndicatorOut"] = t.struct(
        {
            "signatures": t.array(t.proxy(renames["ProcessSignatureOut"])).optional(),
            "ipAddresses": t.array(t.string()).optional(),
            "uris": t.array(t.string()).optional(),
            "domains": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndicatorOut"])
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
    types["ListMuteConfigsResponseIn"] = t.struct(
        {
            "muteConfigs": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListMuteConfigsResponseIn"])
    types["ListMuteConfigsResponseOut"] = t.struct(
        {
            "muteConfigs": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMuteConfigsResponseOut"])
    types["ServiceAccountDelegationInfoIn"] = t.struct(
        {
            "principalSubject": t.string().optional(),
            "principalEmail": t.string().optional(),
        }
    ).named(renames["ServiceAccountDelegationInfoIn"])
    types["ServiceAccountDelegationInfoOut"] = t.struct(
        {
            "principalSubject": t.string().optional(),
            "principalEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAccountDelegationInfoOut"])
    types["ContainerIn"] = t.struct(
        {
            "name": t.string().optional(),
            "imageId": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelIn"])).optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["ContainerIn"])
    types["ContainerOut"] = t.struct(
        {
            "name": t.string().optional(),
            "imageId": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelOut"])).optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerOut"])
    types["ExfilResourceIn"] = t.struct(
        {"name": t.string().optional(), "components": t.array(t.string()).optional()}
    ).named(renames["ExfilResourceIn"])
    types["ExfilResourceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "components": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExfilResourceOut"])
    types["AccessReviewIn"] = t.struct(
        {
            "verb": t.string().optional(),
            "name": t.string().optional(),
            "subresource": t.string().optional(),
            "ns": t.string().optional(),
            "resource": t.string().optional(),
            "version": t.string().optional(),
            "group": t.string().optional(),
        }
    ).named(renames["AccessReviewIn"])
    types["AccessReviewOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "name": t.string().optional(),
            "subresource": t.string().optional(),
            "ns": t.string().optional(),
            "resource": t.string().optional(),
            "version": t.string().optional(),
            "group": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessReviewOut"])
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
    types["YaraRuleSignatureIn"] = t.struct({"yaraRule": t.string().optional()}).named(
        renames["YaraRuleSignatureIn"]
    )
    types["YaraRuleSignatureOut"] = t.struct(
        {
            "yaraRule": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YaraRuleSignatureOut"])
    types["ContactIn"] = t.struct({"email": t.string().optional()}).named(
        renames["ContactIn"]
    )
    types["ContactOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactOut"])
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
    types["MitreAttackIn"] = t.struct(
        {
            "additionalTactics": t.array(t.string()).optional(),
            "additionalTechniques": t.array(t.string()).optional(),
            "primaryTechniques": t.array(t.string()).optional(),
            "primaryTactic": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["MitreAttackIn"])
    types["MitreAttackOut"] = t.struct(
        {
            "additionalTactics": t.array(t.string()).optional(),
            "additionalTechniques": t.array(t.string()).optional(),
            "primaryTechniques": t.array(t.string()).optional(),
            "primaryTactic": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MitreAttackOut"])
    types["NotificationConfigIn"] = t.struct(
        {
            "streamingConfig": t.proxy(renames["StreamingConfigIn"]).optional(),
            "pubsubTopic": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["NotificationConfigIn"])
    types["NotificationConfigOut"] = t.struct(
        {
            "streamingConfig": t.proxy(renames["StreamingConfigOut"]).optional(),
            "pubsubTopic": t.string().optional(),
            "name": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationConfigOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "enablementState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleOut"
        ]
    )
    types["GoogleCloudSecuritycenterV1NotificationMessageIn"] = t.struct(
        {
            "resource": t.proxy(
                renames["GoogleCloudSecuritycenterV1ResourceIn"]
            ).optional(),
            "finding": t.proxy(renames["FindingIn"]).optional(),
            "notificationConfigName": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1NotificationMessageIn"])
    types["GoogleCloudSecuritycenterV1NotificationMessageOut"] = t.struct(
        {
            "resource": t.proxy(
                renames["GoogleCloudSecuritycenterV1ResourceOut"]
            ).optional(),
            "finding": t.proxy(renames["FindingOut"]).optional(),
            "notificationConfigName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1NotificationMessageOut"])
    types["GroupAssetsRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "compareDuration": t.string().optional(),
            "groupBy": t.string(),
            "readTime": t.string().optional(),
            "pageSize": t.integer().optional(),
            "filter": t.string().optional(),
        }
    ).named(renames["GroupAssetsRequestIn"])
    types["GroupAssetsRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "compareDuration": t.string().optional(),
            "groupBy": t.string(),
            "readTime": t.string().optional(),
            "pageSize": t.integer().optional(),
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupAssetsRequestOut"])
    types["FindingIn"] = t.struct(
        {
            "externalUri": t.string().optional(),
            "indicator": t.proxy(renames["IndicatorIn"]).optional(),
            "state": t.string().optional(),
            "exfiltration": t.proxy(renames["ExfiltrationIn"]).optional(),
            "kernelRootkit": t.proxy(renames["KernelRootkitIn"]).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "kubernetes": t.proxy(renames["KubernetesIn"]).optional(),
            "mute": t.string().optional(),
            "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "iamBindings": t.array(t.proxy(renames["IamBindingIn"])).optional(),
            "moduleName": t.string().optional(),
            "cloudDlpInspection": t.proxy(renames["CloudDlpInspectionIn"]).optional(),
            "compliances": t.array(t.proxy(renames["ComplianceIn"])).optional(),
            "parent": t.string().optional(),
            "canonicalName": t.string().optional(),
            "muteInitiator": t.string().optional(),
            "findingClass": t.string().optional(),
            "vulnerability": t.proxy(renames["VulnerabilityIn"]).optional(),
            "category": t.string().optional(),
            "nextSteps": t.string().optional(),
            "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
            "createTime": t.string().optional(),
            "resourceName": t.string().optional(),
            "files": t.array(t.proxy(renames["FileIn"])).optional(),
            "access": t.proxy(renames["AccessIn"]).optional(),
            "eventTime": t.string().optional(),
            "severity": t.string().optional(),
            "mitreAttack": t.proxy(renames["MitreAttackIn"]).optional(),
            "containers": t.array(t.proxy(renames["ContainerIn"])).optional(),
            "processes": t.array(t.proxy(renames["ProcessIn"])).optional(),
            "cloudDlpDataProfile": t.proxy(renames["CloudDlpDataProfileIn"]).optional(),
            "database": t.proxy(renames["DatabaseIn"]).optional(),
        }
    ).named(renames["FindingIn"])
    types["FindingOut"] = t.struct(
        {
            "muteUpdateTime": t.string().optional(),
            "externalUri": t.string().optional(),
            "indicator": t.proxy(renames["IndicatorOut"]).optional(),
            "state": t.string().optional(),
            "exfiltration": t.proxy(renames["ExfiltrationOut"]).optional(),
            "kernelRootkit": t.proxy(renames["KernelRootkitOut"]).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "kubernetes": t.proxy(renames["KubernetesOut"]).optional(),
            "mute": t.string().optional(),
            "sourceProperties": t.struct({"_": t.string().optional()}).optional(),
            "iamBindings": t.array(t.proxy(renames["IamBindingOut"])).optional(),
            "moduleName": t.string().optional(),
            "cloudDlpInspection": t.proxy(renames["CloudDlpInspectionOut"]).optional(),
            "compliances": t.array(t.proxy(renames["ComplianceOut"])).optional(),
            "parent": t.string().optional(),
            "canonicalName": t.string().optional(),
            "muteInitiator": t.string().optional(),
            "findingClass": t.string().optional(),
            "vulnerability": t.proxy(renames["VulnerabilityOut"]).optional(),
            "category": t.string().optional(),
            "nextSteps": t.string().optional(),
            "connections": t.array(t.proxy(renames["ConnectionOut"])).optional(),
            "createTime": t.string().optional(),
            "externalSystems": t.struct({"_": t.string().optional()}).optional(),
            "resourceName": t.string().optional(),
            "securityMarks": t.proxy(renames["SecurityMarksOut"]).optional(),
            "files": t.array(t.proxy(renames["FileOut"])).optional(),
            "access": t.proxy(renames["AccessOut"]).optional(),
            "eventTime": t.string().optional(),
            "severity": t.string().optional(),
            "mitreAttack": t.proxy(renames["MitreAttackOut"]).optional(),
            "contacts": t.struct({"_": t.string().optional()}).optional(),
            "containers": t.array(t.proxy(renames["ContainerOut"])).optional(),
            "processes": t.array(t.proxy(renames["ProcessOut"])).optional(),
            "cloudDlpDataProfile": t.proxy(
                renames["CloudDlpDataProfileOut"]
            ).optional(),
            "parentDisplayName": t.string().optional(),
            "database": t.proxy(renames["DatabaseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindingOut"])
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
    types["IamPolicyIn"] = t.struct({"policyBlob": t.string().optional()}).named(
        renames["IamPolicyIn"]
    )
    types["IamPolicyOut"] = t.struct(
        {
            "policyBlob": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyOut"])
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
    types["SubjectIn"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "ns": t.string().optional(),
        }
    ).named(renames["SubjectIn"])
    types["SubjectOut"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "ns": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubjectOut"])
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
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
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
    types[
        "GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleIn"
    ] = t.struct(
        {
            "enablementState": t.string().optional(),
            "displayName": t.string().optional(),
            "customConfig": t.proxy(
                renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
            ).optional(),
            "name": t.string().optional(),
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
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "customConfig": t.proxy(
                renames["GoogleCloudSecuritycenterV1CustomConfigOut"]
            ).optional(),
            "ancestorModule": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleOut"]
    )
    types["GoogleCloudSecuritycenterV1CustomConfigIn"] = t.struct(
        {
            "description": t.string().optional(),
            "recommendation": t.string().optional(),
            "customOutput": t.proxy(
                renames["GoogleCloudSecuritycenterV1CustomOutputSpecIn"]
            ).optional(),
            "resourceSelector": t.proxy(
                renames["GoogleCloudSecuritycenterV1ResourceSelectorIn"]
            ).optional(),
            "severity": t.string().optional(),
            "predicate": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1CustomConfigIn"])
    types["GoogleCloudSecuritycenterV1CustomConfigOut"] = t.struct(
        {
            "description": t.string().optional(),
            "recommendation": t.string().optional(),
            "customOutput": t.proxy(
                renames["GoogleCloudSecuritycenterV1CustomOutputSpecOut"]
            ).optional(),
            "resourceSelector": t.proxy(
                renames["GoogleCloudSecuritycenterV1ResourceSelectorOut"]
            ).optional(),
            "severity": t.string().optional(),
            "predicate": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1CustomConfigOut"])
    types["CloudDlpDataProfileIn"] = t.struct(
        {"dataProfile": t.string().optional(), "parentType": t.string().optional()}
    ).named(renames["CloudDlpDataProfileIn"])
    types["CloudDlpDataProfileOut"] = t.struct(
        {
            "dataProfile": t.string().optional(),
            "parentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudDlpDataProfileOut"])
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
    types["GeolocationIn"] = t.struct({"regionCode": t.string().optional()}).named(
        renames["GeolocationIn"]
    )
    types["GeolocationOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeolocationOut"])
    types["KernelRootkitIn"] = t.struct(
        {
            "unexpectedReadOnlyDataModification": t.boolean().optional(),
            "name": t.string().optional(),
            "unexpectedFtraceHandler": t.boolean().optional(),
            "unexpectedKprobeHandler": t.boolean().optional(),
            "unexpectedProcessesInRunqueue": t.boolean().optional(),
            "unexpectedKernelCodePages": t.boolean().optional(),
            "unexpectedCodeModification": t.boolean().optional(),
            "unexpectedInterruptHandler": t.boolean().optional(),
            "unexpectedSystemCallHandler": t.boolean().optional(),
        }
    ).named(renames["KernelRootkitIn"])
    types["KernelRootkitOut"] = t.struct(
        {
            "unexpectedReadOnlyDataModification": t.boolean().optional(),
            "name": t.string().optional(),
            "unexpectedFtraceHandler": t.boolean().optional(),
            "unexpectedKprobeHandler": t.boolean().optional(),
            "unexpectedProcessesInRunqueue": t.boolean().optional(),
            "unexpectedKernelCodePages": t.boolean().optional(),
            "unexpectedCodeModification": t.boolean().optional(),
            "unexpectedInterruptHandler": t.boolean().optional(),
            "unexpectedSystemCallHandler": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KernelRootkitOut"])
    types["ConnectionIn"] = t.struct(
        {
            "sourcePort": t.integer().optional(),
            "destinationPort": t.integer().optional(),
            "destinationIp": t.string().optional(),
            "sourceIp": t.string().optional(),
            "protocol": t.string().optional(),
        }
    ).named(renames["ConnectionIn"])
    types["ConnectionOut"] = t.struct(
        {
            "sourcePort": t.integer().optional(),
            "destinationPort": t.integer().optional(),
            "destinationIp": t.string().optional(),
            "sourceIp": t.string().optional(),
            "protocol": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionOut"])
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
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["VulnerabilityIn"] = t.struct(
        {"cve": t.proxy(renames["CveIn"]).optional()}
    ).named(renames["VulnerabilityIn"])
    types["VulnerabilityOut"] = t.struct(
        {
            "cve": t.proxy(renames["CveOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityOut"])
    types["KubernetesIn"] = t.struct(
        {
            "pods": t.array(t.proxy(renames["PodIn"])).optional(),
            "roles": t.array(t.proxy(renames["RoleIn"])).optional(),
            "nodes": t.array(t.proxy(renames["NodeIn"])).optional(),
            "accessReviews": t.array(t.proxy(renames["AccessReviewIn"])).optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolIn"])).optional(),
            "bindings": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1BindingIn"])
            ).optional(),
        }
    ).named(renames["KubernetesIn"])
    types["KubernetesOut"] = t.struct(
        {
            "pods": t.array(t.proxy(renames["PodOut"])).optional(),
            "roles": t.array(t.proxy(renames["RoleOut"])).optional(),
            "nodes": t.array(t.proxy(renames["NodeOut"])).optional(),
            "accessReviews": t.array(t.proxy(renames["AccessReviewOut"])).optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolOut"])).optional(),
            "bindings": t.array(
                t.proxy(renames["GoogleCloudSecuritycenterV1BindingOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesOut"])
    types["GoogleCloudSecuritycenterV1ExternalSystemIn"] = t.struct(
        {
            "status": t.string().optional(),
            "name": t.string().optional(),
            "assignees": t.array(t.string()).optional(),
            "externalSystemUpdateTime": t.string().optional(),
            "externalUid": t.string().optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ExternalSystemIn"])
    types["GoogleCloudSecuritycenterV1ExternalSystemOut"] = t.struct(
        {
            "status": t.string().optional(),
            "name": t.string().optional(),
            "assignees": t.array(t.string()).optional(),
            "externalSystemUpdateTime": t.string().optional(),
            "externalUid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSecuritycenterV1ExternalSystemOut"])

    functions = {}
    functions["projectsMuteConfigsList"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMuteConfigsCreate"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMuteConfigsGet"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMuteConfigsPatch"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMuteConfigsDelete"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsBigQueryExportsCreate"] = securitycenter.delete(
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
                "status": t.string().optional(),
                "assignees": t.array(t.string()).optional(),
                "externalSystemUpdateTime": t.string().optional(),
                "externalUid": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1ExternalSystemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAssetsList"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
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
    functions["projectsAssetsGroup"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
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
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
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
    functions["projectsNotificationConfigsGet"] = securitycenter.get(
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
    functions["projectsNotificationConfigsCreate"] = securitycenter.get(
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
    functions["projectsNotificationConfigsDelete"] = securitycenter.get(
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
    functions["projectsNotificationConfigsPatch"] = securitycenter.get(
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
    functions["projectsNotificationConfigsList"] = securitycenter.get(
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
        "projectsSecurityHealthAnalyticsSettingsCustomModulesList"
    ] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "enablementState": t.string().optional(),
                "displayName": t.string().optional(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
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
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "enablementState": t.string().optional(),
                "displayName": t.string().optional(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
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
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "enablementState": t.string().optional(),
                "displayName": t.string().optional(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
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
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "enablementState": t.string().optional(),
                "displayName": t.string().optional(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
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
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "enablementState": t.string().optional(),
                "displayName": t.string().optional(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
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
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "enablementState": t.string().optional(),
                "displayName": t.string().optional(),
                "customConfig": t.proxy(
                    renames["GoogleCloudSecuritycenterV1CustomConfigIn"]
                ).optional(),
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
    functions["foldersSourcesFindingsGroup"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
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
    functions["foldersSourcesFindingsSetMute"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
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
    functions["foldersSourcesFindingsSetState"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
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
    functions["foldersSourcesFindingsPatch"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
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
    functions["foldersSourcesFindingsList"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
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
    functions["foldersSourcesFindingsUpdateSecurityMarks"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
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
    functions["foldersSourcesFindingsExternalSystemsPatch"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "status": t.string().optional(),
                "assignees": t.array(t.string()).optional(),
                "externalSystemUpdateTime": t.string().optional(),
                "externalUid": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1ExternalSystemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersNotificationConfigsCreate"] = securitycenter.get(
        "v1/{parent}/notificationConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotificationConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersNotificationConfigsDelete"] = securitycenter.get(
        "v1/{parent}/notificationConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotificationConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersBigQueryExportsCreate"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersBigQueryExportsList"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersBigQueryExportsPatch"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersBigQueryExportsDelete"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersBigQueryExportsGet"] = securitycenter.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"]),
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
                "groupBy": t.string(),
                "readTime": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "groupBy": t.string(),
                "readTime": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "groupBy": t.string(),
                "readTime": t.string().optional(),
                "pageSize": t.integer().optional(),
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
    functions[
        "foldersSecurityHealthAnalyticsSettingsEffectiveCustomModulesList"
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
        "foldersSecurityHealthAnalyticsSettingsEffectiveCustomModulesGet"
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
    functions["foldersMuteConfigsPatch"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["foldersMuteConfigsDelete"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetOrganizationSettings"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "assetDiscoveryConfig": t.proxy(
                    renames["AssetDiscoveryConfigIn"]
                ).optional(),
                "enableAssetDiscovery": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrganizationSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsUpdateOrganizationSettings"] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "assetDiscoveryConfig": t.proxy(
                    renames["AssetDiscoveryConfigIn"]
                ).optional(),
                "enableAssetDiscovery": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrganizationSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesPatch"
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
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesListDescendant"
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
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesCreate"
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
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesDelete"
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
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesList"
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
        "organizationsSecurityHealthAnalyticsSettingsCustomModulesGet"
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
    functions["organizationsOperationsList"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsOperationsCancel"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsOperationsGet"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsOperationsDelete"] = securitycenter.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsMuteConfigsDelete"] = securitycenter.post(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "parent": t.string(),
                "muteConfigId": t.string(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "filter": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsMuteConfigsList"] = securitycenter.post(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "parent": t.string(),
                "muteConfigId": t.string(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "filter": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsMuteConfigsPatch"] = securitycenter.post(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "parent": t.string(),
                "muteConfigId": t.string(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "filter": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsMuteConfigsGet"] = securitycenter.post(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "parent": t.string(),
                "muteConfigId": t.string(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "filter": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsMuteConfigsCreate"] = securitycenter.post(
        "v1/{parent}/muteConfigs",
        t.struct(
            {
                "parent": t.string(),
                "muteConfigId": t.string(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "filter": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1MuteConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsBigQueryExportsPatch"] = securitycenter.post(
        "v1/{parent}/bigQueryExports",
        t.struct(
            {
                "parent": t.string(),
                "bigQueryExportId": t.string(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsBigQueryExportsDelete"] = securitycenter.post(
        "v1/{parent}/bigQueryExports",
        t.struct(
            {
                "parent": t.string(),
                "bigQueryExportId": t.string(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsBigQueryExportsList"] = securitycenter.post(
        "v1/{parent}/bigQueryExports",
        t.struct(
            {
                "parent": t.string(),
                "bigQueryExportId": t.string(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsBigQueryExportsGet"] = securitycenter.post(
        "v1/{parent}/bigQueryExports",
        t.struct(
            {
                "parent": t.string(),
                "bigQueryExportId": t.string(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsBigQueryExportsCreate"] = securitycenter.post(
        "v1/{parent}/bigQueryExports",
        t.struct(
            {
                "parent": t.string(),
                "bigQueryExportId": t.string(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1BigQueryExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSourcesPatch"] = securitycenter.get(
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
    functions["organizationsSourcesTestIamPermissions"] = securitycenter.get(
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
    functions["organizationsSourcesGetIamPolicy"] = securitycenter.get(
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
    functions["organizationsSourcesSetIamPolicy"] = securitycenter.get(
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
    functions["organizationsSourcesCreate"] = securitycenter.get(
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
    functions["organizationsSourcesGet"] = securitycenter.get(
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
    functions["organizationsSourcesList"] = securitycenter.get(
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
    functions["organizationsSourcesFindingsSetMute"] = securitycenter.post(
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
    functions["organizationsSourcesFindingsPatch"] = securitycenter.post(
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
    functions["organizationsSourcesFindingsGroup"] = securitycenter.post(
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
    functions["organizationsSourcesFindingsCreate"] = securitycenter.post(
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
    functions["organizationsSourcesFindingsUpdateSecurityMarks"] = securitycenter.post(
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
    functions["organizationsSourcesFindingsList"] = securitycenter.post(
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
    functions["organizationsSourcesFindingsSetState"] = securitycenter.post(
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
    functions[
        "organizationsSourcesFindingsExternalSystemsPatch"
    ] = securitycenter.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "status": t.string().optional(),
                "assignees": t.array(t.string()).optional(),
                "externalSystemUpdateTime": t.string().optional(),
                "externalUid": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudSecuritycenterV1ExternalSystemOut"]),
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
    functions["organizationsNotificationConfigsCreate"] = securitycenter.get(
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
    functions["organizationsAssetsUpdateSecurityMarks"] = securitycenter.post(
        "v1/{parent}/assets:runDiscovery",
        t.struct(
            {
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAssetsGroup"] = securitycenter.post(
        "v1/{parent}/assets:runDiscovery",
        t.struct(
            {
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAssetsList"] = securitycenter.post(
        "v1/{parent}/assets:runDiscovery",
        t.struct(
            {
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAssetsRunDiscovery"] = securitycenter.post(
        "v1/{parent}/assets:runDiscovery",
        t.struct(
            {
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="securitycenter",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
