from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_osconfig() -> Import:
    osconfig = HTTPRuntime("https://osconfig.googleapis.com/")

    renames = {
        "ErrorResponse": "_osconfig_1_ErrorResponse",
        "OperationIn": "_osconfig_2_OperationIn",
        "OperationOut": "_osconfig_3_OperationOut",
        "PatchJobInstanceDetailsIn": "_osconfig_4_PatchJobInstanceDetailsIn",
        "PatchJobInstanceDetailsOut": "_osconfig_5_PatchJobInstanceDetailsOut",
        "VulnerabilityReportVulnerabilityIn": "_osconfig_6_VulnerabilityReportVulnerabilityIn",
        "VulnerabilityReportVulnerabilityOut": "_osconfig_7_VulnerabilityReportVulnerabilityOut",
        "InventoryWindowsQuickFixEngineeringPackageIn": "_osconfig_8_InventoryWindowsQuickFixEngineeringPackageIn",
        "InventoryWindowsQuickFixEngineeringPackageOut": "_osconfig_9_InventoryWindowsQuickFixEngineeringPackageOut",
        "InventoryItemIn": "_osconfig_10_InventoryItemIn",
        "InventoryItemOut": "_osconfig_11_InventoryItemOut",
        "OSPolicyAssignmentReportIn": "_osconfig_12_OSPolicyAssignmentReportIn",
        "OSPolicyAssignmentReportOut": "_osconfig_13_OSPolicyAssignmentReportOut",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputIn": "_osconfig_14_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputIn",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputOut": "_osconfig_15_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputOut",
        "OSPolicyAssignmentIn": "_osconfig_16_OSPolicyAssignmentIn",
        "OSPolicyAssignmentOut": "_osconfig_17_OSPolicyAssignmentOut",
        "ListInventoriesResponseIn": "_osconfig_18_ListInventoriesResponseIn",
        "ListInventoriesResponseOut": "_osconfig_19_ListInventoriesResponseOut",
        "ListPatchJobsResponseIn": "_osconfig_20_ListPatchJobsResponseIn",
        "ListPatchJobsResponseOut": "_osconfig_21_ListPatchJobsResponseOut",
        "ResumePatchDeploymentRequestIn": "_osconfig_22_ResumePatchDeploymentRequestIn",
        "ResumePatchDeploymentRequestOut": "_osconfig_23_ResumePatchDeploymentRequestOut",
        "OSPolicyResourcePackageResourceDebIn": "_osconfig_24_OSPolicyResourcePackageResourceDebIn",
        "OSPolicyResourcePackageResourceDebOut": "_osconfig_25_OSPolicyResourcePackageResourceDebOut",
        "OSPolicyResourceFileResourceIn": "_osconfig_26_OSPolicyResourceFileResourceIn",
        "OSPolicyResourceFileResourceOut": "_osconfig_27_OSPolicyResourceFileResourceOut",
        "OSPolicyResourceGroupIn": "_osconfig_28_OSPolicyResourceGroupIn",
        "OSPolicyResourceGroupOut": "_osconfig_29_OSPolicyResourceGroupOut",
        "ListOSPolicyAssignmentReportsResponseIn": "_osconfig_30_ListOSPolicyAssignmentReportsResponseIn",
        "ListOSPolicyAssignmentReportsResponseOut": "_osconfig_31_ListOSPolicyAssignmentReportsResponseOut",
        "PatchJobInstanceDetailsSummaryIn": "_osconfig_32_PatchJobInstanceDetailsSummaryIn",
        "PatchJobInstanceDetailsSummaryOut": "_osconfig_33_PatchJobInstanceDetailsSummaryOut",
        "TimeZoneIn": "_osconfig_34_TimeZoneIn",
        "TimeZoneOut": "_osconfig_35_TimeZoneOut",
        "OSPolicyAssignmentOperationMetadataIn": "_osconfig_36_OSPolicyAssignmentOperationMetadataIn",
        "OSPolicyAssignmentOperationMetadataOut": "_osconfig_37_OSPolicyAssignmentOperationMetadataOut",
        "OSPolicyResourcePackageResourceAPTIn": "_osconfig_38_OSPolicyResourcePackageResourceAPTIn",
        "OSPolicyResourcePackageResourceAPTOut": "_osconfig_39_OSPolicyResourcePackageResourceAPTOut",
        "ExecStepIn": "_osconfig_40_ExecStepIn",
        "ExecStepOut": "_osconfig_41_ExecStepOut",
        "OSPolicyResourceRepositoryResourceZypperRepositoryIn": "_osconfig_42_OSPolicyResourceRepositoryResourceZypperRepositoryIn",
        "OSPolicyResourceRepositoryResourceZypperRepositoryOut": "_osconfig_43_OSPolicyResourceRepositoryResourceZypperRepositoryOut",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceIn": "_osconfig_44_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceIn",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOut": "_osconfig_45_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOut",
        "InventoryWindowsUpdatePackageIn": "_osconfig_46_InventoryWindowsUpdatePackageIn",
        "InventoryWindowsUpdatePackageOut": "_osconfig_47_InventoryWindowsUpdatePackageOut",
        "OSPolicyAssignmentRolloutIn": "_osconfig_48_OSPolicyAssignmentRolloutIn",
        "OSPolicyAssignmentRolloutOut": "_osconfig_49_OSPolicyAssignmentRolloutOut",
        "WeekDayOfMonthIn": "_osconfig_50_WeekDayOfMonthIn",
        "WeekDayOfMonthOut": "_osconfig_51_WeekDayOfMonthOut",
        "AptSettingsIn": "_osconfig_52_AptSettingsIn",
        "AptSettingsOut": "_osconfig_53_AptSettingsOut",
        "ExecStepConfigIn": "_osconfig_54_ExecStepConfigIn",
        "ExecStepConfigOut": "_osconfig_55_ExecStepConfigOut",
        "ZypperSettingsIn": "_osconfig_56_ZypperSettingsIn",
        "ZypperSettingsOut": "_osconfig_57_ZypperSettingsOut",
        "StatusIn": "_osconfig_58_StatusIn",
        "StatusOut": "_osconfig_59_StatusOut",
        "DateIn": "_osconfig_60_DateIn",
        "DateOut": "_osconfig_61_DateOut",
        "GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataIn": "_osconfig_62_GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataIn",
        "GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataOut": "_osconfig_63_GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataOut",
        "GooSettingsIn": "_osconfig_64_GooSettingsIn",
        "GooSettingsOut": "_osconfig_65_GooSettingsOut",
        "ListPatchDeploymentsResponseIn": "_osconfig_66_ListPatchDeploymentsResponseIn",
        "ListPatchDeploymentsResponseOut": "_osconfig_67_ListPatchDeploymentsResponseOut",
        "PatchInstanceFilterIn": "_osconfig_68_PatchInstanceFilterIn",
        "PatchInstanceFilterOut": "_osconfig_69_PatchInstanceFilterOut",
        "OSPolicyResourceIn": "_osconfig_70_OSPolicyResourceIn",
        "OSPolicyResourceOut": "_osconfig_71_OSPolicyResourceOut",
        "InventoryZypperPatchIn": "_osconfig_72_InventoryZypperPatchIn",
        "InventoryZypperPatchOut": "_osconfig_73_InventoryZypperPatchOut",
        "OSPolicyResourcePackageResourceRPMIn": "_osconfig_74_OSPolicyResourcePackageResourceRPMIn",
        "OSPolicyResourcePackageResourceRPMOut": "_osconfig_75_OSPolicyResourcePackageResourceRPMOut",
        "ListOSPolicyAssignmentsResponseIn": "_osconfig_76_ListOSPolicyAssignmentsResponseIn",
        "ListOSPolicyAssignmentsResponseOut": "_osconfig_77_ListOSPolicyAssignmentsResponseOut",
        "PatchDeploymentIn": "_osconfig_78_PatchDeploymentIn",
        "PatchDeploymentOut": "_osconfig_79_PatchDeploymentOut",
        "ExecutePatchJobRequestIn": "_osconfig_80_ExecutePatchJobRequestIn",
        "ExecutePatchJobRequestOut": "_osconfig_81_ExecutePatchJobRequestOut",
        "VulnerabilityReportVulnerabilityItemIn": "_osconfig_82_VulnerabilityReportVulnerabilityItemIn",
        "VulnerabilityReportVulnerabilityItemOut": "_osconfig_83_VulnerabilityReportVulnerabilityItemOut",
        "WeeklyScheduleIn": "_osconfig_84_WeeklyScheduleIn",
        "WeeklyScheduleOut": "_osconfig_85_WeeklyScheduleOut",
        "GcsObjectIn": "_osconfig_86_GcsObjectIn",
        "GcsObjectOut": "_osconfig_87_GcsObjectOut",
        "OSPolicyAssignmentLabelSetIn": "_osconfig_88_OSPolicyAssignmentLabelSetIn",
        "OSPolicyAssignmentLabelSetOut": "_osconfig_89_OSPolicyAssignmentLabelSetOut",
        "WindowsUpdateSettingsIn": "_osconfig_90_WindowsUpdateSettingsIn",
        "WindowsUpdateSettingsOut": "_osconfig_91_WindowsUpdateSettingsOut",
        "CVSSv3In": "_osconfig_92_CVSSv3In",
        "CVSSv3Out": "_osconfig_93_CVSSv3Out",
        "OSPolicyResourcePackageResourceZypperIn": "_osconfig_94_OSPolicyResourcePackageResourceZypperIn",
        "OSPolicyResourcePackageResourceZypperOut": "_osconfig_95_OSPolicyResourcePackageResourceZypperOut",
        "ListVulnerabilityReportsResponseIn": "_osconfig_96_ListVulnerabilityReportsResponseIn",
        "ListVulnerabilityReportsResponseOut": "_osconfig_97_ListVulnerabilityReportsResponseOut",
        "YumSettingsIn": "_osconfig_98_YumSettingsIn",
        "YumSettingsOut": "_osconfig_99_YumSettingsOut",
        "PatchInstanceFilterGroupLabelIn": "_osconfig_100_PatchInstanceFilterGroupLabelIn",
        "PatchInstanceFilterGroupLabelOut": "_osconfig_101_PatchInstanceFilterGroupLabelOut",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepIn": "_osconfig_102_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepIn",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepOut": "_osconfig_103_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepOut",
        "VulnerabilityReportVulnerabilityDetailsIn": "_osconfig_104_VulnerabilityReportVulnerabilityDetailsIn",
        "VulnerabilityReportVulnerabilityDetailsOut": "_osconfig_105_VulnerabilityReportVulnerabilityDetailsOut",
        "RecurringScheduleIn": "_osconfig_106_RecurringScheduleIn",
        "RecurringScheduleOut": "_osconfig_107_RecurringScheduleOut",
        "OSPolicyAssignmentInstanceFilterInventoryIn": "_osconfig_108_OSPolicyAssignmentInstanceFilterInventoryIn",
        "OSPolicyAssignmentInstanceFilterInventoryOut": "_osconfig_109_OSPolicyAssignmentInstanceFilterInventoryOut",
        "InventorySoftwarePackageIn": "_osconfig_110_InventorySoftwarePackageIn",
        "InventorySoftwarePackageOut": "_osconfig_111_InventorySoftwarePackageOut",
        "OSPolicyResourcePackageResourceYUMIn": "_osconfig_112_OSPolicyResourcePackageResourceYUMIn",
        "OSPolicyResourcePackageResourceYUMOut": "_osconfig_113_OSPolicyResourcePackageResourceYUMOut",
        "OSPolicyResourceExecResourceIn": "_osconfig_114_OSPolicyResourceExecResourceIn",
        "OSPolicyResourceExecResourceOut": "_osconfig_115_OSPolicyResourceExecResourceOut",
        "OSPolicyResourceFileGcsIn": "_osconfig_116_OSPolicyResourceFileGcsIn",
        "OSPolicyResourceFileGcsOut": "_osconfig_117_OSPolicyResourceFileGcsOut",
        "ListPatchJobInstanceDetailsResponseIn": "_osconfig_118_ListPatchJobInstanceDetailsResponseIn",
        "ListPatchJobInstanceDetailsResponseOut": "_osconfig_119_ListPatchJobInstanceDetailsResponseOut",
        "OSPolicyIn": "_osconfig_120_OSPolicyIn",
        "OSPolicyOut": "_osconfig_121_OSPolicyOut",
        "OSPolicyResourcePackageResourceIn": "_osconfig_122_OSPolicyResourcePackageResourceIn",
        "OSPolicyResourcePackageResourceOut": "_osconfig_123_OSPolicyResourcePackageResourceOut",
        "OSPolicyResourceExecResourceExecIn": "_osconfig_124_OSPolicyResourceExecResourceExecIn",
        "OSPolicyResourceExecResourceExecOut": "_osconfig_125_OSPolicyResourceExecResourceExecOut",
        "ListOSPolicyAssignmentRevisionsResponseIn": "_osconfig_126_ListOSPolicyAssignmentRevisionsResponseIn",
        "ListOSPolicyAssignmentRevisionsResponseOut": "_osconfig_127_ListOSPolicyAssignmentRevisionsResponseOut",
        "FixedOrPercentIn": "_osconfig_128_FixedOrPercentIn",
        "FixedOrPercentOut": "_osconfig_129_FixedOrPercentOut",
        "OSPolicyResourceRepositoryResourceIn": "_osconfig_130_OSPolicyResourceRepositoryResourceIn",
        "OSPolicyResourceRepositoryResourceOut": "_osconfig_131_OSPolicyResourceRepositoryResourceOut",
        "InventoryWindowsUpdatePackageWindowsUpdateCategoryIn": "_osconfig_132_InventoryWindowsUpdatePackageWindowsUpdateCategoryIn",
        "InventoryWindowsUpdatePackageWindowsUpdateCategoryOut": "_osconfig_133_InventoryWindowsUpdatePackageWindowsUpdateCategoryOut",
        "OSPolicyAssignmentInstanceFilterIn": "_osconfig_134_OSPolicyAssignmentInstanceFilterIn",
        "OSPolicyAssignmentInstanceFilterOut": "_osconfig_135_OSPolicyAssignmentInstanceFilterOut",
        "InventoryOsInfoIn": "_osconfig_136_InventoryOsInfoIn",
        "InventoryOsInfoOut": "_osconfig_137_InventoryOsInfoOut",
        "EmptyIn": "_osconfig_138_EmptyIn",
        "EmptyOut": "_osconfig_139_EmptyOut",
        "OSPolicyResourceRepositoryResourceYumRepositoryIn": "_osconfig_140_OSPolicyResourceRepositoryResourceYumRepositoryIn",
        "OSPolicyResourceRepositoryResourceYumRepositoryOut": "_osconfig_141_OSPolicyResourceRepositoryResourceYumRepositoryOut",
        "OSPolicyResourcePackageResourceGooGetIn": "_osconfig_142_OSPolicyResourcePackageResourceGooGetIn",
        "OSPolicyResourcePackageResourceGooGetOut": "_osconfig_143_OSPolicyResourcePackageResourceGooGetOut",
        "PatchConfigIn": "_osconfig_144_PatchConfigIn",
        "PatchConfigOut": "_osconfig_145_PatchConfigOut",
        "InventoryIn": "_osconfig_146_InventoryIn",
        "InventoryOut": "_osconfig_147_InventoryOut",
        "InventoryVersionedPackageIn": "_osconfig_148_InventoryVersionedPackageIn",
        "InventoryVersionedPackageOut": "_osconfig_149_InventoryVersionedPackageOut",
        "CancelPatchJobRequestIn": "_osconfig_150_CancelPatchJobRequestIn",
        "CancelPatchJobRequestOut": "_osconfig_151_CancelPatchJobRequestOut",
        "VulnerabilityReportIn": "_osconfig_152_VulnerabilityReportIn",
        "VulnerabilityReportOut": "_osconfig_153_VulnerabilityReportOut",
        "OSPolicyResourceFileIn": "_osconfig_154_OSPolicyResourceFileIn",
        "OSPolicyResourceFileOut": "_osconfig_155_OSPolicyResourceFileOut",
        "InventoryWindowsApplicationIn": "_osconfig_156_InventoryWindowsApplicationIn",
        "InventoryWindowsApplicationOut": "_osconfig_157_InventoryWindowsApplicationOut",
        "PausePatchDeploymentRequestIn": "_osconfig_158_PausePatchDeploymentRequestIn",
        "PausePatchDeploymentRequestOut": "_osconfig_159_PausePatchDeploymentRequestOut",
        "MonthlyScheduleIn": "_osconfig_160_MonthlyScheduleIn",
        "MonthlyScheduleOut": "_osconfig_161_MonthlyScheduleOut",
        "OSPolicyResourceRepositoryResourceGooRepositoryIn": "_osconfig_162_OSPolicyResourceRepositoryResourceGooRepositoryIn",
        "OSPolicyResourceRepositoryResourceGooRepositoryOut": "_osconfig_163_OSPolicyResourceRepositoryResourceGooRepositoryOut",
        "OneTimeScheduleIn": "_osconfig_164_OneTimeScheduleIn",
        "OneTimeScheduleOut": "_osconfig_165_OneTimeScheduleOut",
        "TimeOfDayIn": "_osconfig_166_TimeOfDayIn",
        "TimeOfDayOut": "_osconfig_167_TimeOfDayOut",
        "CancelOperationRequestIn": "_osconfig_168_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_osconfig_169_CancelOperationRequestOut",
        "VulnerabilityReportVulnerabilityDetailsReferenceIn": "_osconfig_170_VulnerabilityReportVulnerabilityDetailsReferenceIn",
        "VulnerabilityReportVulnerabilityDetailsReferenceOut": "_osconfig_171_VulnerabilityReportVulnerabilityDetailsReferenceOut",
        "OSPolicyResourceRepositoryResourceAptRepositoryIn": "_osconfig_172_OSPolicyResourceRepositoryResourceAptRepositoryIn",
        "OSPolicyResourceRepositoryResourceAptRepositoryOut": "_osconfig_173_OSPolicyResourceRepositoryResourceAptRepositoryOut",
        "PatchJobIn": "_osconfig_174_PatchJobIn",
        "PatchJobOut": "_osconfig_175_PatchJobOut",
        "OSPolicyResourceFileRemoteIn": "_osconfig_176_OSPolicyResourceFileRemoteIn",
        "OSPolicyResourceFileRemoteOut": "_osconfig_177_OSPolicyResourceFileRemoteOut",
        "OSPolicyResourcePackageResourceMSIIn": "_osconfig_178_OSPolicyResourcePackageResourceMSIIn",
        "OSPolicyResourcePackageResourceMSIOut": "_osconfig_179_OSPolicyResourcePackageResourceMSIOut",
        "OSPolicyInventoryFilterIn": "_osconfig_180_OSPolicyInventoryFilterIn",
        "OSPolicyInventoryFilterOut": "_osconfig_181_OSPolicyInventoryFilterOut",
        "PatchRolloutIn": "_osconfig_182_PatchRolloutIn",
        "PatchRolloutOut": "_osconfig_183_PatchRolloutOut",
        "OSPolicyAssignmentReportOSPolicyComplianceIn": "_osconfig_184_OSPolicyAssignmentReportOSPolicyComplianceIn",
        "OSPolicyAssignmentReportOSPolicyComplianceOut": "_osconfig_185_OSPolicyAssignmentReportOSPolicyComplianceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["PatchJobInstanceDetailsIn"] = t.struct(
        {
            "failureReason": t.string().optional(),
            "instanceSystemId": t.string().optional(),
            "attemptCount": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["PatchJobInstanceDetailsIn"])
    types["PatchJobInstanceDetailsOut"] = t.struct(
        {
            "failureReason": t.string().optional(),
            "instanceSystemId": t.string().optional(),
            "attemptCount": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchJobInstanceDetailsOut"])
    types["VulnerabilityReportVulnerabilityIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "items": t.array(
                t.proxy(renames["VulnerabilityReportVulnerabilityItemIn"])
            ).optional(),
            "installedInventoryItemIds": t.array(t.string()).optional(),
            "details": t.proxy(
                renames["VulnerabilityReportVulnerabilityDetailsIn"]
            ).optional(),
            "availableInventoryItemIds": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityIn"])
    types["VulnerabilityReportVulnerabilityOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "items": t.array(
                t.proxy(renames["VulnerabilityReportVulnerabilityItemOut"])
            ).optional(),
            "installedInventoryItemIds": t.array(t.string()).optional(),
            "details": t.proxy(
                renames["VulnerabilityReportVulnerabilityDetailsOut"]
            ).optional(),
            "availableInventoryItemIds": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityOut"])
    types["InventoryWindowsQuickFixEngineeringPackageIn"] = t.struct(
        {
            "description": t.string().optional(),
            "caption": t.string().optional(),
            "hotFixId": t.string().optional(),
            "installTime": t.string().optional(),
        }
    ).named(renames["InventoryWindowsQuickFixEngineeringPackageIn"])
    types["InventoryWindowsQuickFixEngineeringPackageOut"] = t.struct(
        {
            "description": t.string().optional(),
            "caption": t.string().optional(),
            "hotFixId": t.string().optional(),
            "installTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryWindowsQuickFixEngineeringPackageOut"])
    types["InventoryItemIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "type": t.string().optional(),
            "originType": t.string().optional(),
            "id": t.string().optional(),
            "installedPackage": t.proxy(
                renames["InventorySoftwarePackageIn"]
            ).optional(),
            "createTime": t.string().optional(),
            "availablePackage": t.proxy(
                renames["InventorySoftwarePackageIn"]
            ).optional(),
        }
    ).named(renames["InventoryItemIn"])
    types["InventoryItemOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "type": t.string().optional(),
            "originType": t.string().optional(),
            "id": t.string().optional(),
            "installedPackage": t.proxy(
                renames["InventorySoftwarePackageOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "availablePackage": t.proxy(
                renames["InventorySoftwarePackageOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryItemOut"])
    types["OSPolicyAssignmentReportIn"] = t.struct(
        {
            "osPolicyCompliances": t.array(
                t.proxy(renames["OSPolicyAssignmentReportOSPolicyComplianceIn"])
            ).optional(),
            "osPolicyAssignment": t.string().optional(),
            "name": t.string().optional(),
            "lastRunId": t.string().optional(),
            "instance": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["OSPolicyAssignmentReportIn"])
    types["OSPolicyAssignmentReportOut"] = t.struct(
        {
            "osPolicyCompliances": t.array(
                t.proxy(renames["OSPolicyAssignmentReportOSPolicyComplianceOut"])
            ).optional(),
            "osPolicyAssignment": t.string().optional(),
            "name": t.string().optional(),
            "lastRunId": t.string().optional(),
            "instance": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentReportOut"])
    types[
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputIn"
    ] = t.struct({"enforcementOutput": t.string().optional()}).named(
        renames[
            "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputIn"
        ]
    )
    types[
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputOut"
    ] = t.struct(
        {
            "enforcementOutput": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputOut"
        ]
    )
    types["OSPolicyAssignmentIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "osPolicies": t.array(t.proxy(renames["OSPolicyIn"])),
            "instanceFilter": t.proxy(renames["OSPolicyAssignmentInstanceFilterIn"]),
            "rollout": t.proxy(renames["OSPolicyAssignmentRolloutIn"]),
        }
    ).named(renames["OSPolicyAssignmentIn"])
    types["OSPolicyAssignmentOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "revisionCreateTime": t.string().optional(),
            "deleted": t.boolean().optional(),
            "uid": t.string().optional(),
            "revisionId": t.string().optional(),
            "osPolicies": t.array(t.proxy(renames["OSPolicyOut"])),
            "rolloutState": t.string().optional(),
            "baseline": t.boolean().optional(),
            "instanceFilter": t.proxy(renames["OSPolicyAssignmentInstanceFilterOut"]),
            "rollout": t.proxy(renames["OSPolicyAssignmentRolloutOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentOut"])
    types["ListInventoriesResponseIn"] = t.struct(
        {
            "inventories": t.array(t.proxy(renames["InventoryIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListInventoriesResponseIn"])
    types["ListInventoriesResponseOut"] = t.struct(
        {
            "inventories": t.array(t.proxy(renames["InventoryOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInventoriesResponseOut"])
    types["ListPatchJobsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "patchJobs": t.array(t.proxy(renames["PatchJobIn"])).optional(),
        }
    ).named(renames["ListPatchJobsResponseIn"])
    types["ListPatchJobsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "patchJobs": t.array(t.proxy(renames["PatchJobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPatchJobsResponseOut"])
    types["ResumePatchDeploymentRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResumePatchDeploymentRequestIn"])
    types["ResumePatchDeploymentRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumePatchDeploymentRequestOut"])
    types["OSPolicyResourcePackageResourceDebIn"] = t.struct(
        {
            "pullDeps": t.boolean().optional(),
            "source": t.proxy(renames["OSPolicyResourceFileIn"]),
        }
    ).named(renames["OSPolicyResourcePackageResourceDebIn"])
    types["OSPolicyResourcePackageResourceDebOut"] = t.struct(
        {
            "pullDeps": t.boolean().optional(),
            "source": t.proxy(renames["OSPolicyResourceFileOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourcePackageResourceDebOut"])
    types["OSPolicyResourceFileResourceIn"] = t.struct(
        {
            "permissions": t.string().optional(),
            "state": t.string(),
            "file": t.proxy(renames["OSPolicyResourceFileIn"]).optional(),
            "content": t.string().optional(),
            "path": t.string(),
        }
    ).named(renames["OSPolicyResourceFileResourceIn"])
    types["OSPolicyResourceFileResourceOut"] = t.struct(
        {
            "permissions": t.string().optional(),
            "state": t.string(),
            "file": t.proxy(renames["OSPolicyResourceFileOut"]).optional(),
            "content": t.string().optional(),
            "path": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceFileResourceOut"])
    types["OSPolicyResourceGroupIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["OSPolicyResourceIn"])),
            "inventoryFilters": t.array(
                t.proxy(renames["OSPolicyInventoryFilterIn"])
            ).optional(),
        }
    ).named(renames["OSPolicyResourceGroupIn"])
    types["OSPolicyResourceGroupOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["OSPolicyResourceOut"])),
            "inventoryFilters": t.array(
                t.proxy(renames["OSPolicyInventoryFilterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceGroupOut"])
    types["ListOSPolicyAssignmentReportsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "osPolicyAssignmentReports": t.array(
                t.proxy(renames["OSPolicyAssignmentReportIn"])
            ).optional(),
        }
    ).named(renames["ListOSPolicyAssignmentReportsResponseIn"])
    types["ListOSPolicyAssignmentReportsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "osPolicyAssignmentReports": t.array(
                t.proxy(renames["OSPolicyAssignmentReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOSPolicyAssignmentReportsResponseOut"])
    types["PatchJobInstanceDetailsSummaryIn"] = t.struct(
        {
            "failedInstanceCount": t.string().optional(),
            "noAgentDetectedInstanceCount": t.string().optional(),
            "startedInstanceCount": t.string().optional(),
            "timedOutInstanceCount": t.string().optional(),
            "downloadingPatchesInstanceCount": t.string().optional(),
            "rebootingInstanceCount": t.string().optional(),
            "pendingInstanceCount": t.string().optional(),
            "postPatchStepInstanceCount": t.string().optional(),
            "applyingPatchesInstanceCount": t.string().optional(),
            "ackedInstanceCount": t.string().optional(),
            "inactiveInstanceCount": t.string().optional(),
            "notifiedInstanceCount": t.string().optional(),
            "prePatchStepInstanceCount": t.string().optional(),
            "succeededInstanceCount": t.string().optional(),
            "succeededRebootRequiredInstanceCount": t.string().optional(),
        }
    ).named(renames["PatchJobInstanceDetailsSummaryIn"])
    types["PatchJobInstanceDetailsSummaryOut"] = t.struct(
        {
            "failedInstanceCount": t.string().optional(),
            "noAgentDetectedInstanceCount": t.string().optional(),
            "startedInstanceCount": t.string().optional(),
            "timedOutInstanceCount": t.string().optional(),
            "downloadingPatchesInstanceCount": t.string().optional(),
            "rebootingInstanceCount": t.string().optional(),
            "pendingInstanceCount": t.string().optional(),
            "postPatchStepInstanceCount": t.string().optional(),
            "applyingPatchesInstanceCount": t.string().optional(),
            "ackedInstanceCount": t.string().optional(),
            "inactiveInstanceCount": t.string().optional(),
            "notifiedInstanceCount": t.string().optional(),
            "prePatchStepInstanceCount": t.string().optional(),
            "succeededInstanceCount": t.string().optional(),
            "succeededRebootRequiredInstanceCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchJobInstanceDetailsSummaryOut"])
    types["TimeZoneIn"] = t.struct(
        {"id": t.string().optional(), "version": t.string().optional()}
    ).named(renames["TimeZoneIn"])
    types["TimeZoneOut"] = t.struct(
        {
            "id": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeZoneOut"])
    types["OSPolicyAssignmentOperationMetadataIn"] = t.struct(
        {
            "rolloutUpdateTime": t.string().optional(),
            "osPolicyAssignment": t.string().optional(),
            "apiMethod": t.string().optional(),
            "rolloutState": t.string().optional(),
            "rolloutStartTime": t.string().optional(),
        }
    ).named(renames["OSPolicyAssignmentOperationMetadataIn"])
    types["OSPolicyAssignmentOperationMetadataOut"] = t.struct(
        {
            "rolloutUpdateTime": t.string().optional(),
            "osPolicyAssignment": t.string().optional(),
            "apiMethod": t.string().optional(),
            "rolloutState": t.string().optional(),
            "rolloutStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentOperationMetadataOut"])
    types["OSPolicyResourcePackageResourceAPTIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["OSPolicyResourcePackageResourceAPTIn"])
    types["OSPolicyResourcePackageResourceAPTOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OSPolicyResourcePackageResourceAPTOut"])
    types["ExecStepIn"] = t.struct(
        {
            "linuxExecStepConfig": t.proxy(renames["ExecStepConfigIn"]).optional(),
            "windowsExecStepConfig": t.proxy(renames["ExecStepConfigIn"]).optional(),
        }
    ).named(renames["ExecStepIn"])
    types["ExecStepOut"] = t.struct(
        {
            "linuxExecStepConfig": t.proxy(renames["ExecStepConfigOut"]).optional(),
            "windowsExecStepConfig": t.proxy(renames["ExecStepConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecStepOut"])
    types["OSPolicyResourceRepositoryResourceZypperRepositoryIn"] = t.struct(
        {
            "id": t.string(),
            "displayName": t.string().optional(),
            "baseUrl": t.string(),
            "gpgKeys": t.array(t.string()).optional(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceZypperRepositoryIn"])
    types["OSPolicyResourceRepositoryResourceZypperRepositoryOut"] = t.struct(
        {
            "id": t.string(),
            "displayName": t.string().optional(),
            "baseUrl": t.string(),
            "gpgKeys": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceZypperRepositoryOut"])
    types[
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceIn"
    ] = t.struct(
        {
            "configSteps": t.array(
                t.proxy(
                    renames[
                        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepIn"
                    ]
                )
            ).optional(),
            "execResourceOutput": t.proxy(
                renames[
                    "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputIn"
                ]
            ).optional(),
            "complianceState": t.string().optional(),
            "complianceStateReason": t.string().optional(),
            "osPolicyResourceId": t.string().optional(),
        }
    ).named(
        renames[
            "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceIn"
        ]
    )
    types[
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOut"
    ] = t.struct(
        {
            "configSteps": t.array(
                t.proxy(
                    renames[
                        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepOut"
                    ]
                )
            ).optional(),
            "execResourceOutput": t.proxy(
                renames[
                    "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputOut"
                ]
            ).optional(),
            "complianceState": t.string().optional(),
            "complianceStateReason": t.string().optional(),
            "osPolicyResourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOut"
        ]
    )
    types["InventoryWindowsUpdatePackageIn"] = t.struct(
        {
            "supportUrl": t.string().optional(),
            "description": t.string().optional(),
            "moreInfoUrls": t.array(t.string()).optional(),
            "updateId": t.string().optional(),
            "categories": t.array(
                t.proxy(renames["InventoryWindowsUpdatePackageWindowsUpdateCategoryIn"])
            ).optional(),
            "title": t.string().optional(),
            "kbArticleIds": t.array(t.string()).optional(),
            "lastDeploymentChangeTime": t.string().optional(),
            "revisionNumber": t.integer().optional(),
        }
    ).named(renames["InventoryWindowsUpdatePackageIn"])
    types["InventoryWindowsUpdatePackageOut"] = t.struct(
        {
            "supportUrl": t.string().optional(),
            "description": t.string().optional(),
            "moreInfoUrls": t.array(t.string()).optional(),
            "updateId": t.string().optional(),
            "categories": t.array(
                t.proxy(
                    renames["InventoryWindowsUpdatePackageWindowsUpdateCategoryOut"]
                )
            ).optional(),
            "title": t.string().optional(),
            "kbArticleIds": t.array(t.string()).optional(),
            "lastDeploymentChangeTime": t.string().optional(),
            "revisionNumber": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryWindowsUpdatePackageOut"])
    types["OSPolicyAssignmentRolloutIn"] = t.struct(
        {
            "minWaitDuration": t.string(),
            "disruptionBudget": t.proxy(renames["FixedOrPercentIn"]),
        }
    ).named(renames["OSPolicyAssignmentRolloutIn"])
    types["OSPolicyAssignmentRolloutOut"] = t.struct(
        {
            "minWaitDuration": t.string(),
            "disruptionBudget": t.proxy(renames["FixedOrPercentOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentRolloutOut"])
    types["WeekDayOfMonthIn"] = t.struct(
        {
            "weekOrdinal": t.integer(),
            "dayOfWeek": t.string(),
            "dayOffset": t.integer().optional(),
        }
    ).named(renames["WeekDayOfMonthIn"])
    types["WeekDayOfMonthOut"] = t.struct(
        {
            "weekOrdinal": t.integer(),
            "dayOfWeek": t.string(),
            "dayOffset": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeekDayOfMonthOut"])
    types["AptSettingsIn"] = t.struct(
        {
            "excludes": t.array(t.string()).optional(),
            "exclusivePackages": t.array(t.string()).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["AptSettingsIn"])
    types["AptSettingsOut"] = t.struct(
        {
            "excludes": t.array(t.string()).optional(),
            "exclusivePackages": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AptSettingsOut"])
    types["ExecStepConfigIn"] = t.struct(
        {
            "gcsObject": t.proxy(renames["GcsObjectIn"]).optional(),
            "localPath": t.string().optional(),
            "allowedSuccessCodes": t.array(t.integer()).optional(),
            "interpreter": t.string().optional(),
        }
    ).named(renames["ExecStepConfigIn"])
    types["ExecStepConfigOut"] = t.struct(
        {
            "gcsObject": t.proxy(renames["GcsObjectOut"]).optional(),
            "localPath": t.string().optional(),
            "allowedSuccessCodes": t.array(t.integer()).optional(),
            "interpreter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecStepConfigOut"])
    types["ZypperSettingsIn"] = t.struct(
        {
            "excludes": t.array(t.string()).optional(),
            "categories": t.array(t.string()).optional(),
            "severities": t.array(t.string()).optional(),
            "withUpdate": t.boolean().optional(),
            "withOptional": t.boolean().optional(),
            "exclusivePatches": t.array(t.string()).optional(),
        }
    ).named(renames["ZypperSettingsIn"])
    types["ZypperSettingsOut"] = t.struct(
        {
            "excludes": t.array(t.string()).optional(),
            "categories": t.array(t.string()).optional(),
            "severities": t.array(t.string()).optional(),
            "withUpdate": t.boolean().optional(),
            "withOptional": t.boolean().optional(),
            "exclusivePatches": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZypperSettingsOut"])
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
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataIn"] = t.struct(
        {
            "rolloutStartTime": t.string().optional(),
            "rolloutState": t.string().optional(),
            "osPolicyAssignment": t.string().optional(),
            "apiMethod": t.string().optional(),
            "rolloutUpdateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataIn"])
    types["GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataOut"] = t.struct(
        {
            "rolloutStartTime": t.string().optional(),
            "rolloutState": t.string().optional(),
            "osPolicyAssignment": t.string().optional(),
            "apiMethod": t.string().optional(),
            "rolloutUpdateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataOut"])
    types["GooSettingsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GooSettingsIn"]
    )
    types["GooSettingsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooSettingsOut"])
    types["ListPatchDeploymentsResponseIn"] = t.struct(
        {
            "patchDeployments": t.array(
                t.proxy(renames["PatchDeploymentIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPatchDeploymentsResponseIn"])
    types["ListPatchDeploymentsResponseOut"] = t.struct(
        {
            "patchDeployments": t.array(
                t.proxy(renames["PatchDeploymentOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPatchDeploymentsResponseOut"])
    types["PatchInstanceFilterIn"] = t.struct(
        {
            "zones": t.array(t.string()).optional(),
            "groupLabels": t.array(
                t.proxy(renames["PatchInstanceFilterGroupLabelIn"])
            ).optional(),
            "instanceNamePrefixes": t.array(t.string()).optional(),
            "instances": t.array(t.string()).optional(),
            "all": t.boolean().optional(),
        }
    ).named(renames["PatchInstanceFilterIn"])
    types["PatchInstanceFilterOut"] = t.struct(
        {
            "zones": t.array(t.string()).optional(),
            "groupLabels": t.array(
                t.proxy(renames["PatchInstanceFilterGroupLabelOut"])
            ).optional(),
            "instanceNamePrefixes": t.array(t.string()).optional(),
            "instances": t.array(t.string()).optional(),
            "all": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchInstanceFilterOut"])
    types["OSPolicyResourceIn"] = t.struct(
        {
            "file": t.proxy(renames["OSPolicyResourceFileResourceIn"]).optional(),
            "id": t.string(),
            "repository": t.proxy(
                renames["OSPolicyResourceRepositoryResourceIn"]
            ).optional(),
            "exec": t.proxy(renames["OSPolicyResourceExecResourceIn"]).optional(),
            "pkg": t.proxy(renames["OSPolicyResourcePackageResourceIn"]).optional(),
        }
    ).named(renames["OSPolicyResourceIn"])
    types["OSPolicyResourceOut"] = t.struct(
        {
            "file": t.proxy(renames["OSPolicyResourceFileResourceOut"]).optional(),
            "id": t.string(),
            "repository": t.proxy(
                renames["OSPolicyResourceRepositoryResourceOut"]
            ).optional(),
            "exec": t.proxy(renames["OSPolicyResourceExecResourceOut"]).optional(),
            "pkg": t.proxy(renames["OSPolicyResourcePackageResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceOut"])
    types["InventoryZypperPatchIn"] = t.struct(
        {
            "patchName": t.string().optional(),
            "category": t.string().optional(),
            "summary": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["InventoryZypperPatchIn"])
    types["InventoryZypperPatchOut"] = t.struct(
        {
            "patchName": t.string().optional(),
            "category": t.string().optional(),
            "summary": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryZypperPatchOut"])
    types["OSPolicyResourcePackageResourceRPMIn"] = t.struct(
        {
            "source": t.proxy(renames["OSPolicyResourceFileIn"]),
            "pullDeps": t.boolean().optional(),
        }
    ).named(renames["OSPolicyResourcePackageResourceRPMIn"])
    types["OSPolicyResourcePackageResourceRPMOut"] = t.struct(
        {
            "source": t.proxy(renames["OSPolicyResourceFileOut"]),
            "pullDeps": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourcePackageResourceRPMOut"])
    types["ListOSPolicyAssignmentsResponseIn"] = t.struct(
        {
            "osPolicyAssignments": t.array(
                t.proxy(renames["OSPolicyAssignmentIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOSPolicyAssignmentsResponseIn"])
    types["ListOSPolicyAssignmentsResponseOut"] = t.struct(
        {
            "osPolicyAssignments": t.array(
                t.proxy(renames["OSPolicyAssignmentOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOSPolicyAssignmentsResponseOut"])
    types["PatchDeploymentIn"] = t.struct(
        {
            "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
            "description": t.string().optional(),
            "recurringSchedule": t.proxy(renames["RecurringScheduleIn"]),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
            "duration": t.string().optional(),
            "oneTimeSchedule": t.proxy(renames["OneTimeScheduleIn"]),
            "name": t.string().optional(),
            "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
        }
    ).named(renames["PatchDeploymentIn"])
    types["PatchDeploymentOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "patchConfig": t.proxy(renames["PatchConfigOut"]).optional(),
            "description": t.string().optional(),
            "recurringSchedule": t.proxy(renames["RecurringScheduleOut"]),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterOut"]),
            "duration": t.string().optional(),
            "oneTimeSchedule": t.proxy(renames["OneTimeScheduleOut"]),
            "state": t.string().optional(),
            "lastExecuteTime": t.string().optional(),
            "name": t.string().optional(),
            "rollout": t.proxy(renames["PatchRolloutOut"]).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchDeploymentOut"])
    types["ExecutePatchJobRequestIn"] = t.struct(
        {
            "description": t.string().optional(),
            "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
            "duration": t.string().optional(),
            "displayName": t.string().optional(),
            "dryRun": t.boolean().optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
            "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
        }
    ).named(renames["ExecutePatchJobRequestIn"])
    types["ExecutePatchJobRequestOut"] = t.struct(
        {
            "description": t.string().optional(),
            "rollout": t.proxy(renames["PatchRolloutOut"]).optional(),
            "duration": t.string().optional(),
            "displayName": t.string().optional(),
            "dryRun": t.boolean().optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterOut"]),
            "patchConfig": t.proxy(renames["PatchConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutePatchJobRequestOut"])
    types["VulnerabilityReportVulnerabilityItemIn"] = t.struct(
        {
            "installedInventoryItemId": t.string().optional(),
            "upstreamFix": t.string().optional(),
            "availableInventoryItemId": t.string().optional(),
            "fixedCpeUri": t.string().optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityItemIn"])
    types["VulnerabilityReportVulnerabilityItemOut"] = t.struct(
        {
            "installedInventoryItemId": t.string().optional(),
            "upstreamFix": t.string().optional(),
            "availableInventoryItemId": t.string().optional(),
            "fixedCpeUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityItemOut"])
    types["WeeklyScheduleIn"] = t.struct({"dayOfWeek": t.string()}).named(
        renames["WeeklyScheduleIn"]
    )
    types["WeeklyScheduleOut"] = t.struct(
        {"dayOfWeek": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WeeklyScheduleOut"])
    types["GcsObjectIn"] = t.struct(
        {"bucket": t.string(), "object": t.string(), "generationNumber": t.string()}
    ).named(renames["GcsObjectIn"])
    types["GcsObjectOut"] = t.struct(
        {
            "bucket": t.string(),
            "object": t.string(),
            "generationNumber": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsObjectOut"])
    types["OSPolicyAssignmentLabelSetIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["OSPolicyAssignmentLabelSetIn"])
    types["OSPolicyAssignmentLabelSetOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentLabelSetOut"])
    types["WindowsUpdateSettingsIn"] = t.struct(
        {
            "classifications": t.array(t.string()).optional(),
            "exclusivePatches": t.array(t.string()).optional(),
            "excludes": t.array(t.string()).optional(),
        }
    ).named(renames["WindowsUpdateSettingsIn"])
    types["WindowsUpdateSettingsOut"] = t.struct(
        {
            "classifications": t.array(t.string()).optional(),
            "exclusivePatches": t.array(t.string()).optional(),
            "excludes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsUpdateSettingsOut"])
    types["CVSSv3In"] = t.struct(
        {
            "availabilityImpact": t.string().optional(),
            "baseScore": t.number().optional(),
            "attackComplexity": t.string().optional(),
            "attackVector": t.string().optional(),
            "confidentialityImpact": t.string().optional(),
            "exploitabilityScore": t.number().optional(),
            "scope": t.string().optional(),
            "impactScore": t.number().optional(),
            "userInteraction": t.string().optional(),
            "integrityImpact": t.string().optional(),
            "privilegesRequired": t.string().optional(),
        }
    ).named(renames["CVSSv3In"])
    types["CVSSv3Out"] = t.struct(
        {
            "availabilityImpact": t.string().optional(),
            "baseScore": t.number().optional(),
            "attackComplexity": t.string().optional(),
            "attackVector": t.string().optional(),
            "confidentialityImpact": t.string().optional(),
            "exploitabilityScore": t.number().optional(),
            "scope": t.string().optional(),
            "impactScore": t.number().optional(),
            "userInteraction": t.string().optional(),
            "integrityImpact": t.string().optional(),
            "privilegesRequired": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CVSSv3Out"])
    types["OSPolicyResourcePackageResourceZypperIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["OSPolicyResourcePackageResourceZypperIn"])
    types["OSPolicyResourcePackageResourceZypperOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OSPolicyResourcePackageResourceZypperOut"])
    types["ListVulnerabilityReportsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "vulnerabilityReports": t.array(
                t.proxy(renames["VulnerabilityReportIn"])
            ).optional(),
        }
    ).named(renames["ListVulnerabilityReportsResponseIn"])
    types["ListVulnerabilityReportsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "vulnerabilityReports": t.array(
                t.proxy(renames["VulnerabilityReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVulnerabilityReportsResponseOut"])
    types["YumSettingsIn"] = t.struct(
        {
            "minimal": t.boolean().optional(),
            "exclusivePackages": t.array(t.string()).optional(),
            "excludes": t.array(t.string()).optional(),
            "security": t.boolean().optional(),
        }
    ).named(renames["YumSettingsIn"])
    types["YumSettingsOut"] = t.struct(
        {
            "minimal": t.boolean().optional(),
            "exclusivePackages": t.array(t.string()).optional(),
            "excludes": t.array(t.string()).optional(),
            "security": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YumSettingsOut"])
    types["PatchInstanceFilterGroupLabelIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["PatchInstanceFilterGroupLabelIn"])
    types["PatchInstanceFilterGroupLabelOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchInstanceFilterGroupLabelOut"])
    types[
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepIn"
    ] = t.struct(
        {"errorMessage": t.string().optional(), "type": t.string().optional()}
    ).named(
        renames[
            "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepIn"
        ]
    )
    types[
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepOut"
    ] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepOut"
        ]
    )
    types["VulnerabilityReportVulnerabilityDetailsIn"] = t.struct(
        {
            "cvssV2Score": t.number().optional(),
            "severity": t.string().optional(),
            "description": t.string().optional(),
            "references": t.array(
                t.proxy(renames["VulnerabilityReportVulnerabilityDetailsReferenceIn"])
            ).optional(),
            "cvssV3": t.proxy(renames["CVSSv3In"]).optional(),
            "cve": t.string().optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityDetailsIn"])
    types["VulnerabilityReportVulnerabilityDetailsOut"] = t.struct(
        {
            "cvssV2Score": t.number().optional(),
            "severity": t.string().optional(),
            "description": t.string().optional(),
            "references": t.array(
                t.proxy(renames["VulnerabilityReportVulnerabilityDetailsReferenceOut"])
            ).optional(),
            "cvssV3": t.proxy(renames["CVSSv3Out"]).optional(),
            "cve": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityDetailsOut"])
    types["RecurringScheduleIn"] = t.struct(
        {
            "timeZone": t.proxy(renames["TimeZoneIn"]),
            "timeOfDay": t.proxy(renames["TimeOfDayIn"]),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "frequency": t.string(),
            "monthly": t.proxy(renames["MonthlyScheduleIn"]),
            "weekly": t.proxy(renames["WeeklyScheduleIn"]),
        }
    ).named(renames["RecurringScheduleIn"])
    types["RecurringScheduleOut"] = t.struct(
        {
            "timeZone": t.proxy(renames["TimeZoneOut"]),
            "timeOfDay": t.proxy(renames["TimeOfDayOut"]),
            "nextExecuteTime": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "frequency": t.string(),
            "monthly": t.proxy(renames["MonthlyScheduleOut"]),
            "lastExecuteTime": t.string().optional(),
            "weekly": t.proxy(renames["WeeklyScheduleOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecurringScheduleOut"])
    types["OSPolicyAssignmentInstanceFilterInventoryIn"] = t.struct(
        {"osShortName": t.string(), "osVersion": t.string().optional()}
    ).named(renames["OSPolicyAssignmentInstanceFilterInventoryIn"])
    types["OSPolicyAssignmentInstanceFilterInventoryOut"] = t.struct(
        {
            "osShortName": t.string(),
            "osVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentInstanceFilterInventoryOut"])
    types["InventorySoftwarePackageIn"] = t.struct(
        {
            "aptPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
            "windowsApplication": t.proxy(
                renames["InventoryWindowsApplicationIn"]
            ).optional(),
            "yumPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
            "wuaPackage": t.proxy(
                renames["InventoryWindowsUpdatePackageIn"]
            ).optional(),
            "qfePackage": t.proxy(
                renames["InventoryWindowsQuickFixEngineeringPackageIn"]
            ).optional(),
            "googetPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
            "zypperPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
            "cosPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
            "zypperPatch": t.proxy(renames["InventoryZypperPatchIn"]).optional(),
        }
    ).named(renames["InventorySoftwarePackageIn"])
    types["InventorySoftwarePackageOut"] = t.struct(
        {
            "aptPackage": t.proxy(renames["InventoryVersionedPackageOut"]).optional(),
            "windowsApplication": t.proxy(
                renames["InventoryWindowsApplicationOut"]
            ).optional(),
            "yumPackage": t.proxy(renames["InventoryVersionedPackageOut"]).optional(),
            "wuaPackage": t.proxy(
                renames["InventoryWindowsUpdatePackageOut"]
            ).optional(),
            "qfePackage": t.proxy(
                renames["InventoryWindowsQuickFixEngineeringPackageOut"]
            ).optional(),
            "googetPackage": t.proxy(
                renames["InventoryVersionedPackageOut"]
            ).optional(),
            "zypperPackage": t.proxy(
                renames["InventoryVersionedPackageOut"]
            ).optional(),
            "cosPackage": t.proxy(renames["InventoryVersionedPackageOut"]).optional(),
            "zypperPatch": t.proxy(renames["InventoryZypperPatchOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySoftwarePackageOut"])
    types["OSPolicyResourcePackageResourceYUMIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["OSPolicyResourcePackageResourceYUMIn"])
    types["OSPolicyResourcePackageResourceYUMOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OSPolicyResourcePackageResourceYUMOut"])
    types["OSPolicyResourceExecResourceIn"] = t.struct(
        {
            "validate": t.proxy(renames["OSPolicyResourceExecResourceExecIn"]),
            "enforce": t.proxy(
                renames["OSPolicyResourceExecResourceExecIn"]
            ).optional(),
        }
    ).named(renames["OSPolicyResourceExecResourceIn"])
    types["OSPolicyResourceExecResourceOut"] = t.struct(
        {
            "validate": t.proxy(renames["OSPolicyResourceExecResourceExecOut"]),
            "enforce": t.proxy(
                renames["OSPolicyResourceExecResourceExecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceExecResourceOut"])
    types["OSPolicyResourceFileGcsIn"] = t.struct(
        {
            "generation": t.string().optional(),
            "bucket": t.string(),
            "object": t.string(),
        }
    ).named(renames["OSPolicyResourceFileGcsIn"])
    types["OSPolicyResourceFileGcsOut"] = t.struct(
        {
            "generation": t.string().optional(),
            "bucket": t.string(),
            "object": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceFileGcsOut"])
    types["ListPatchJobInstanceDetailsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "patchJobInstanceDetails": t.array(
                t.proxy(renames["PatchJobInstanceDetailsIn"])
            ).optional(),
        }
    ).named(renames["ListPatchJobInstanceDetailsResponseIn"])
    types["ListPatchJobInstanceDetailsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "patchJobInstanceDetails": t.array(
                t.proxy(renames["PatchJobInstanceDetailsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPatchJobInstanceDetailsResponseOut"])
    types["OSPolicyIn"] = t.struct(
        {
            "mode": t.string(),
            "description": t.string().optional(),
            "resourceGroups": t.array(t.proxy(renames["OSPolicyResourceGroupIn"])),
            "allowNoResourceGroupMatch": t.boolean().optional(),
            "id": t.string(),
        }
    ).named(renames["OSPolicyIn"])
    types["OSPolicyOut"] = t.struct(
        {
            "mode": t.string(),
            "description": t.string().optional(),
            "resourceGroups": t.array(t.proxy(renames["OSPolicyResourceGroupOut"])),
            "allowNoResourceGroupMatch": t.boolean().optional(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyOut"])
    types["OSPolicyResourcePackageResourceIn"] = t.struct(
        {
            "msi": t.proxy(renames["OSPolicyResourcePackageResourceMSIIn"]).optional(),
            "yum": t.proxy(renames["OSPolicyResourcePackageResourceYUMIn"]).optional(),
            "zypper": t.proxy(
                renames["OSPolicyResourcePackageResourceZypperIn"]
            ).optional(),
            "deb": t.proxy(renames["OSPolicyResourcePackageResourceDebIn"]).optional(),
            "apt": t.proxy(renames["OSPolicyResourcePackageResourceAPTIn"]).optional(),
            "googet": t.proxy(
                renames["OSPolicyResourcePackageResourceGooGetIn"]
            ).optional(),
            "desiredState": t.string(),
            "rpm": t.proxy(renames["OSPolicyResourcePackageResourceRPMIn"]).optional(),
        }
    ).named(renames["OSPolicyResourcePackageResourceIn"])
    types["OSPolicyResourcePackageResourceOut"] = t.struct(
        {
            "msi": t.proxy(renames["OSPolicyResourcePackageResourceMSIOut"]).optional(),
            "yum": t.proxy(renames["OSPolicyResourcePackageResourceYUMOut"]).optional(),
            "zypper": t.proxy(
                renames["OSPolicyResourcePackageResourceZypperOut"]
            ).optional(),
            "deb": t.proxy(renames["OSPolicyResourcePackageResourceDebOut"]).optional(),
            "apt": t.proxy(renames["OSPolicyResourcePackageResourceAPTOut"]).optional(),
            "googet": t.proxy(
                renames["OSPolicyResourcePackageResourceGooGetOut"]
            ).optional(),
            "desiredState": t.string(),
            "rpm": t.proxy(renames["OSPolicyResourcePackageResourceRPMOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourcePackageResourceOut"])
    types["OSPolicyResourceExecResourceExecIn"] = t.struct(
        {
            "outputFilePath": t.string().optional(),
            "script": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "file": t.proxy(renames["OSPolicyResourceFileIn"]).optional(),
            "interpreter": t.string(),
        }
    ).named(renames["OSPolicyResourceExecResourceExecIn"])
    types["OSPolicyResourceExecResourceExecOut"] = t.struct(
        {
            "outputFilePath": t.string().optional(),
            "script": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "file": t.proxy(renames["OSPolicyResourceFileOut"]).optional(),
            "interpreter": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceExecResourceExecOut"])
    types["ListOSPolicyAssignmentRevisionsResponseIn"] = t.struct(
        {
            "osPolicyAssignments": t.array(
                t.proxy(renames["OSPolicyAssignmentIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOSPolicyAssignmentRevisionsResponseIn"])
    types["ListOSPolicyAssignmentRevisionsResponseOut"] = t.struct(
        {
            "osPolicyAssignments": t.array(
                t.proxy(renames["OSPolicyAssignmentOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOSPolicyAssignmentRevisionsResponseOut"])
    types["FixedOrPercentIn"] = t.struct(
        {"fixed": t.integer().optional(), "percent": t.integer().optional()}
    ).named(renames["FixedOrPercentIn"])
    types["FixedOrPercentOut"] = t.struct(
        {
            "fixed": t.integer().optional(),
            "percent": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FixedOrPercentOut"])
    types["OSPolicyResourceRepositoryResourceIn"] = t.struct(
        {
            "yum": t.proxy(
                renames["OSPolicyResourceRepositoryResourceYumRepositoryIn"]
            ).optional(),
            "zypper": t.proxy(
                renames["OSPolicyResourceRepositoryResourceZypperRepositoryIn"]
            ).optional(),
            "goo": t.proxy(
                renames["OSPolicyResourceRepositoryResourceGooRepositoryIn"]
            ).optional(),
            "apt": t.proxy(
                renames["OSPolicyResourceRepositoryResourceAptRepositoryIn"]
            ).optional(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceIn"])
    types["OSPolicyResourceRepositoryResourceOut"] = t.struct(
        {
            "yum": t.proxy(
                renames["OSPolicyResourceRepositoryResourceYumRepositoryOut"]
            ).optional(),
            "zypper": t.proxy(
                renames["OSPolicyResourceRepositoryResourceZypperRepositoryOut"]
            ).optional(),
            "goo": t.proxy(
                renames["OSPolicyResourceRepositoryResourceGooRepositoryOut"]
            ).optional(),
            "apt": t.proxy(
                renames["OSPolicyResourceRepositoryResourceAptRepositoryOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceOut"])
    types["InventoryWindowsUpdatePackageWindowsUpdateCategoryIn"] = t.struct(
        {"name": t.string().optional(), "id": t.string().optional()}
    ).named(renames["InventoryWindowsUpdatePackageWindowsUpdateCategoryIn"])
    types["InventoryWindowsUpdatePackageWindowsUpdateCategoryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryWindowsUpdatePackageWindowsUpdateCategoryOut"])
    types["OSPolicyAssignmentInstanceFilterIn"] = t.struct(
        {
            "inventories": t.array(
                t.proxy(renames["OSPolicyAssignmentInstanceFilterInventoryIn"])
            ).optional(),
            "exclusionLabels": t.array(
                t.proxy(renames["OSPolicyAssignmentLabelSetIn"])
            ).optional(),
            "all": t.boolean().optional(),
            "inclusionLabels": t.array(
                t.proxy(renames["OSPolicyAssignmentLabelSetIn"])
            ).optional(),
        }
    ).named(renames["OSPolicyAssignmentInstanceFilterIn"])
    types["OSPolicyAssignmentInstanceFilterOut"] = t.struct(
        {
            "inventories": t.array(
                t.proxy(renames["OSPolicyAssignmentInstanceFilterInventoryOut"])
            ).optional(),
            "exclusionLabels": t.array(
                t.proxy(renames["OSPolicyAssignmentLabelSetOut"])
            ).optional(),
            "all": t.boolean().optional(),
            "inclusionLabels": t.array(
                t.proxy(renames["OSPolicyAssignmentLabelSetOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentInstanceFilterOut"])
    types["InventoryOsInfoIn"] = t.struct(
        {
            "kernelRelease": t.string().optional(),
            "architecture": t.string().optional(),
            "osconfigAgentVersion": t.string().optional(),
            "hostname": t.string().optional(),
            "longName": t.string().optional(),
            "version": t.string().optional(),
            "shortName": t.string().optional(),
            "kernelVersion": t.string().optional(),
        }
    ).named(renames["InventoryOsInfoIn"])
    types["InventoryOsInfoOut"] = t.struct(
        {
            "kernelRelease": t.string().optional(),
            "architecture": t.string().optional(),
            "osconfigAgentVersion": t.string().optional(),
            "hostname": t.string().optional(),
            "longName": t.string().optional(),
            "version": t.string().optional(),
            "shortName": t.string().optional(),
            "kernelVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryOsInfoOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["OSPolicyResourceRepositoryResourceYumRepositoryIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "baseUrl": t.string(),
            "gpgKeys": t.array(t.string()).optional(),
            "id": t.string(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceYumRepositoryIn"])
    types["OSPolicyResourceRepositoryResourceYumRepositoryOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "baseUrl": t.string(),
            "gpgKeys": t.array(t.string()).optional(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceYumRepositoryOut"])
    types["OSPolicyResourcePackageResourceGooGetIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["OSPolicyResourcePackageResourceGooGetIn"])
    types["OSPolicyResourcePackageResourceGooGetOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OSPolicyResourcePackageResourceGooGetOut"])
    types["PatchConfigIn"] = t.struct(
        {
            "apt": t.proxy(renames["AptSettingsIn"]).optional(),
            "windowsUpdate": t.proxy(renames["WindowsUpdateSettingsIn"]).optional(),
            "yum": t.proxy(renames["YumSettingsIn"]).optional(),
            "zypper": t.proxy(renames["ZypperSettingsIn"]).optional(),
            "rebootConfig": t.string().optional(),
            "migInstancesAllowed": t.boolean().optional(),
            "postStep": t.proxy(renames["ExecStepIn"]).optional(),
            "preStep": t.proxy(renames["ExecStepIn"]).optional(),
            "goo": t.proxy(renames["GooSettingsIn"]).optional(),
        }
    ).named(renames["PatchConfigIn"])
    types["PatchConfigOut"] = t.struct(
        {
            "apt": t.proxy(renames["AptSettingsOut"]).optional(),
            "windowsUpdate": t.proxy(renames["WindowsUpdateSettingsOut"]).optional(),
            "yum": t.proxy(renames["YumSettingsOut"]).optional(),
            "zypper": t.proxy(renames["ZypperSettingsOut"]).optional(),
            "rebootConfig": t.string().optional(),
            "migInstancesAllowed": t.boolean().optional(),
            "postStep": t.proxy(renames["ExecStepOut"]).optional(),
            "preStep": t.proxy(renames["ExecStepOut"]).optional(),
            "goo": t.proxy(renames["GooSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchConfigOut"])
    types["InventoryIn"] = t.struct(
        {
            "items": t.struct({"_": t.string().optional()}).optional(),
            "osInfo": t.proxy(renames["InventoryOsInfoIn"]).optional(),
        }
    ).named(renames["InventoryIn"])
    types["InventoryOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "items": t.struct({"_": t.string().optional()}).optional(),
            "osInfo": t.proxy(renames["InventoryOsInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryOut"])
    types["InventoryVersionedPackageIn"] = t.struct(
        {
            "packageName": t.string().optional(),
            "version": t.string().optional(),
            "architecture": t.string().optional(),
        }
    ).named(renames["InventoryVersionedPackageIn"])
    types["InventoryVersionedPackageOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "version": t.string().optional(),
            "architecture": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryVersionedPackageOut"])
    types["CancelPatchJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelPatchJobRequestIn"]
    )
    types["CancelPatchJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelPatchJobRequestOut"])
    types["VulnerabilityReportIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VulnerabilityReportIn"]
    )
    types["VulnerabilityReportOut"] = t.struct(
        {
            "name": t.string().optional(),
            "vulnerabilities": t.array(
                t.proxy(renames["VulnerabilityReportVulnerabilityOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityReportOut"])
    types["OSPolicyResourceFileIn"] = t.struct(
        {
            "localPath": t.string().optional(),
            "remote": t.proxy(renames["OSPolicyResourceFileRemoteIn"]).optional(),
            "allowInsecure": t.boolean().optional(),
            "gcs": t.proxy(renames["OSPolicyResourceFileGcsIn"]).optional(),
        }
    ).named(renames["OSPolicyResourceFileIn"])
    types["OSPolicyResourceFileOut"] = t.struct(
        {
            "localPath": t.string().optional(),
            "remote": t.proxy(renames["OSPolicyResourceFileRemoteOut"]).optional(),
            "allowInsecure": t.boolean().optional(),
            "gcs": t.proxy(renames["OSPolicyResourceFileGcsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceFileOut"])
    types["InventoryWindowsApplicationIn"] = t.struct(
        {
            "publisher": t.string().optional(),
            "displayVersion": t.string().optional(),
            "installDate": t.proxy(renames["DateIn"]).optional(),
            "displayName": t.string().optional(),
            "helpLink": t.string().optional(),
        }
    ).named(renames["InventoryWindowsApplicationIn"])
    types["InventoryWindowsApplicationOut"] = t.struct(
        {
            "publisher": t.string().optional(),
            "displayVersion": t.string().optional(),
            "installDate": t.proxy(renames["DateOut"]).optional(),
            "displayName": t.string().optional(),
            "helpLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryWindowsApplicationOut"])
    types["PausePatchDeploymentRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["PausePatchDeploymentRequestIn"])
    types["PausePatchDeploymentRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PausePatchDeploymentRequestOut"])
    types["MonthlyScheduleIn"] = t.struct(
        {
            "monthDay": t.integer(),
            "weekDayOfMonth": t.proxy(renames["WeekDayOfMonthIn"]),
        }
    ).named(renames["MonthlyScheduleIn"])
    types["MonthlyScheduleOut"] = t.struct(
        {
            "monthDay": t.integer(),
            "weekDayOfMonth": t.proxy(renames["WeekDayOfMonthOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonthlyScheduleOut"])
    types["OSPolicyResourceRepositoryResourceGooRepositoryIn"] = t.struct(
        {"name": t.string(), "url": t.string()}
    ).named(renames["OSPolicyResourceRepositoryResourceGooRepositoryIn"])
    types["OSPolicyResourceRepositoryResourceGooRepositoryOut"] = t.struct(
        {
            "name": t.string(),
            "url": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceGooRepositoryOut"])
    types["OneTimeScheduleIn"] = t.struct({"executeTime": t.string()}).named(
        renames["OneTimeScheduleIn"]
    )
    types["OneTimeScheduleOut"] = t.struct(
        {
            "executeTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OneTimeScheduleOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["VulnerabilityReportVulnerabilityDetailsReferenceIn"] = t.struct(
        {"url": t.string().optional(), "source": t.string().optional()}
    ).named(renames["VulnerabilityReportVulnerabilityDetailsReferenceIn"])
    types["VulnerabilityReportVulnerabilityDetailsReferenceOut"] = t.struct(
        {
            "url": t.string().optional(),
            "source": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityDetailsReferenceOut"])
    types["OSPolicyResourceRepositoryResourceAptRepositoryIn"] = t.struct(
        {
            "components": t.array(t.string()),
            "gpgKey": t.string().optional(),
            "distribution": t.string(),
            "archiveType": t.string(),
            "uri": t.string(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceAptRepositoryIn"])
    types["OSPolicyResourceRepositoryResourceAptRepositoryOut"] = t.struct(
        {
            "components": t.array(t.string()),
            "gpgKey": t.string().optional(),
            "distribution": t.string(),
            "archiveType": t.string(),
            "uri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceAptRepositoryOut"])
    types["PatchJobIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "dryRun": t.boolean().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
            "description": t.string().optional(),
            "errorMessage": t.string().optional(),
            "duration": t.string().optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]).optional(),
            "instanceDetailsSummary": t.proxy(
                renames["PatchJobInstanceDetailsSummaryIn"]
            ).optional(),
            "name": t.string().optional(),
            "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
            "percentComplete": t.number().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["PatchJobIn"])
    types["PatchJobOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "dryRun": t.boolean().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "patchConfig": t.proxy(renames["PatchConfigOut"]).optional(),
            "description": t.string().optional(),
            "errorMessage": t.string().optional(),
            "duration": t.string().optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterOut"]).optional(),
            "instanceDetailsSummary": t.proxy(
                renames["PatchJobInstanceDetailsSummaryOut"]
            ).optional(),
            "name": t.string().optional(),
            "rollout": t.proxy(renames["PatchRolloutOut"]).optional(),
            "patchDeployment": t.string().optional(),
            "percentComplete": t.number().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchJobOut"])
    types["OSPolicyResourceFileRemoteIn"] = t.struct(
        {"uri": t.string(), "sha256Checksum": t.string().optional()}
    ).named(renames["OSPolicyResourceFileRemoteIn"])
    types["OSPolicyResourceFileRemoteOut"] = t.struct(
        {
            "uri": t.string(),
            "sha256Checksum": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceFileRemoteOut"])
    types["OSPolicyResourcePackageResourceMSIIn"] = t.struct(
        {
            "properties": t.array(t.string()).optional(),
            "source": t.proxy(renames["OSPolicyResourceFileIn"]),
        }
    ).named(renames["OSPolicyResourcePackageResourceMSIIn"])
    types["OSPolicyResourcePackageResourceMSIOut"] = t.struct(
        {
            "properties": t.array(t.string()).optional(),
            "source": t.proxy(renames["OSPolicyResourceFileOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourcePackageResourceMSIOut"])
    types["OSPolicyInventoryFilterIn"] = t.struct(
        {"osVersion": t.string().optional(), "osShortName": t.string()}
    ).named(renames["OSPolicyInventoryFilterIn"])
    types["OSPolicyInventoryFilterOut"] = t.struct(
        {
            "osVersion": t.string().optional(),
            "osShortName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyInventoryFilterOut"])
    types["PatchRolloutIn"] = t.struct(
        {
            "disruptionBudget": t.proxy(renames["FixedOrPercentIn"]).optional(),
            "mode": t.string().optional(),
        }
    ).named(renames["PatchRolloutIn"])
    types["PatchRolloutOut"] = t.struct(
        {
            "disruptionBudget": t.proxy(renames["FixedOrPercentOut"]).optional(),
            "mode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchRolloutOut"])
    types["OSPolicyAssignmentReportOSPolicyComplianceIn"] = t.struct(
        {
            "complianceStateReason": t.string().optional(),
            "osPolicyResourceCompliances": t.array(
                t.proxy(
                    renames[
                        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceIn"
                    ]
                )
            ).optional(),
            "osPolicyId": t.string().optional(),
            "complianceState": t.string().optional(),
        }
    ).named(renames["OSPolicyAssignmentReportOSPolicyComplianceIn"])
    types["OSPolicyAssignmentReportOSPolicyComplianceOut"] = t.struct(
        {
            "complianceStateReason": t.string().optional(),
            "osPolicyResourceCompliances": t.array(
                t.proxy(
                    renames[
                        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOut"
                    ]
                )
            ).optional(),
            "osPolicyId": t.string().optional(),
            "complianceState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentReportOSPolicyComplianceOut"])

    functions = {}
    functions["projectsPatchDeploymentsResume"] = osconfig.post(
        "v1/{parent}/patchDeployments",
        t.struct(
            {
                "parent": t.string(),
                "patchDeploymentId": t.string(),
                "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
                "description": t.string().optional(),
                "recurringSchedule": t.proxy(renames["RecurringScheduleIn"]),
                "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
                "duration": t.string().optional(),
                "oneTimeSchedule": t.proxy(renames["OneTimeScheduleIn"]),
                "name": t.string().optional(),
                "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsGet"] = osconfig.post(
        "v1/{parent}/patchDeployments",
        t.struct(
            {
                "parent": t.string(),
                "patchDeploymentId": t.string(),
                "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
                "description": t.string().optional(),
                "recurringSchedule": t.proxy(renames["RecurringScheduleIn"]),
                "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
                "duration": t.string().optional(),
                "oneTimeSchedule": t.proxy(renames["OneTimeScheduleIn"]),
                "name": t.string().optional(),
                "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsList"] = osconfig.post(
        "v1/{parent}/patchDeployments",
        t.struct(
            {
                "parent": t.string(),
                "patchDeploymentId": t.string(),
                "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
                "description": t.string().optional(),
                "recurringSchedule": t.proxy(renames["RecurringScheduleIn"]),
                "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
                "duration": t.string().optional(),
                "oneTimeSchedule": t.proxy(renames["OneTimeScheduleIn"]),
                "name": t.string().optional(),
                "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsPause"] = osconfig.post(
        "v1/{parent}/patchDeployments",
        t.struct(
            {
                "parent": t.string(),
                "patchDeploymentId": t.string(),
                "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
                "description": t.string().optional(),
                "recurringSchedule": t.proxy(renames["RecurringScheduleIn"]),
                "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
                "duration": t.string().optional(),
                "oneTimeSchedule": t.proxy(renames["OneTimeScheduleIn"]),
                "name": t.string().optional(),
                "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsDelete"] = osconfig.post(
        "v1/{parent}/patchDeployments",
        t.struct(
            {
                "parent": t.string(),
                "patchDeploymentId": t.string(),
                "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
                "description": t.string().optional(),
                "recurringSchedule": t.proxy(renames["RecurringScheduleIn"]),
                "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
                "duration": t.string().optional(),
                "oneTimeSchedule": t.proxy(renames["OneTimeScheduleIn"]),
                "name": t.string().optional(),
                "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsPatch"] = osconfig.post(
        "v1/{parent}/patchDeployments",
        t.struct(
            {
                "parent": t.string(),
                "patchDeploymentId": t.string(),
                "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
                "description": t.string().optional(),
                "recurringSchedule": t.proxy(renames["RecurringScheduleIn"]),
                "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
                "duration": t.string().optional(),
                "oneTimeSchedule": t.proxy(renames["OneTimeScheduleIn"]),
                "name": t.string().optional(),
                "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsCreate"] = osconfig.post(
        "v1/{parent}/patchDeployments",
        t.struct(
            {
                "parent": t.string(),
                "patchDeploymentId": t.string(),
                "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
                "description": t.string().optional(),
                "recurringSchedule": t.proxy(renames["RecurringScheduleIn"]),
                "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
                "duration": t.string().optional(),
                "oneTimeSchedule": t.proxy(renames["OneTimeScheduleIn"]),
                "name": t.string().optional(),
                "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesVulnerabilityReportsGet"] = osconfig.get(
        "v1/{parent}/vulnerabilityReports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVulnerabilityReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesVulnerabilityReportsList"] = osconfig.get(
        "v1/{parent}/vulnerabilityReports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVulnerabilityReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsInstancesOsPolicyAssignmentsReportsList"
    ] = osconfig.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OSPolicyAssignmentReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesOsPolicyAssignmentsReportsGet"] = osconfig.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OSPolicyAssignmentReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesInventoriesList"] = osconfig.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesInventoriesGet"] = osconfig.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InventoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsPatch"] = osconfig.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOSPolicyAssignmentRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsList"] = osconfig.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOSPolicyAssignmentRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsCreate"] = osconfig.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOSPolicyAssignmentRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsDelete"] = osconfig.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOSPolicyAssignmentRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsGet"] = osconfig.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOSPolicyAssignmentRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsListRevisions"] = osconfig.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOSPolicyAssignmentRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsOperationsCancel"] = osconfig.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsOperationsGet"] = osconfig.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchJobsGet"] = osconfig.get(
        "v1/{parent}/patchJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPatchJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchJobsExecute"] = osconfig.get(
        "v1/{parent}/patchJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPatchJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchJobsCancel"] = osconfig.get(
        "v1/{parent}/patchJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPatchJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchJobsList"] = osconfig.get(
        "v1/{parent}/patchJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPatchJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchJobsInstanceDetailsList"] = osconfig.get(
        "v1/{parent}/instanceDetails",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPatchJobInstanceDetailsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="osconfig", renames=renames, types=Box(types), functions=Box(functions)
    )
