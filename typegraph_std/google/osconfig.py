from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_osconfig() -> Import:
    osconfig = HTTPRuntime("https://osconfig.googleapis.com/")

    renames = {
        "ErrorResponse": "_osconfig_1_ErrorResponse",
        "OSPolicyResourceFileRemoteIn": "_osconfig_2_OSPolicyResourceFileRemoteIn",
        "OSPolicyResourceFileRemoteOut": "_osconfig_3_OSPolicyResourceFileRemoteOut",
        "InventoryVersionedPackageIn": "_osconfig_4_InventoryVersionedPackageIn",
        "InventoryVersionedPackageOut": "_osconfig_5_InventoryVersionedPackageOut",
        "InventoryOsInfoIn": "_osconfig_6_InventoryOsInfoIn",
        "InventoryOsInfoOut": "_osconfig_7_InventoryOsInfoOut",
        "OSPolicyAssignmentOperationMetadataIn": "_osconfig_8_OSPolicyAssignmentOperationMetadataIn",
        "OSPolicyAssignmentOperationMetadataOut": "_osconfig_9_OSPolicyAssignmentOperationMetadataOut",
        "VulnerabilityReportIn": "_osconfig_10_VulnerabilityReportIn",
        "VulnerabilityReportOut": "_osconfig_11_VulnerabilityReportOut",
        "OSPolicyAssignmentInstanceFilterIn": "_osconfig_12_OSPolicyAssignmentInstanceFilterIn",
        "OSPolicyAssignmentInstanceFilterOut": "_osconfig_13_OSPolicyAssignmentInstanceFilterOut",
        "ListVulnerabilityReportsResponseIn": "_osconfig_14_ListVulnerabilityReportsResponseIn",
        "ListVulnerabilityReportsResponseOut": "_osconfig_15_ListVulnerabilityReportsResponseOut",
        "ListInventoriesResponseIn": "_osconfig_16_ListInventoriesResponseIn",
        "ListInventoriesResponseOut": "_osconfig_17_ListInventoriesResponseOut",
        "VulnerabilityReportVulnerabilityDetailsIn": "_osconfig_18_VulnerabilityReportVulnerabilityDetailsIn",
        "VulnerabilityReportVulnerabilityDetailsOut": "_osconfig_19_VulnerabilityReportVulnerabilityDetailsOut",
        "GcsObjectIn": "_osconfig_20_GcsObjectIn",
        "GcsObjectOut": "_osconfig_21_GcsObjectOut",
        "PatchDeploymentIn": "_osconfig_22_PatchDeploymentIn",
        "PatchDeploymentOut": "_osconfig_23_PatchDeploymentOut",
        "VulnerabilityReportVulnerabilityItemIn": "_osconfig_24_VulnerabilityReportVulnerabilityItemIn",
        "VulnerabilityReportVulnerabilityItemOut": "_osconfig_25_VulnerabilityReportVulnerabilityItemOut",
        "CancelPatchJobRequestIn": "_osconfig_26_CancelPatchJobRequestIn",
        "CancelPatchJobRequestOut": "_osconfig_27_CancelPatchJobRequestOut",
        "OSPolicyResourcePackageResourceAPTIn": "_osconfig_28_OSPolicyResourcePackageResourceAPTIn",
        "OSPolicyResourcePackageResourceAPTOut": "_osconfig_29_OSPolicyResourcePackageResourceAPTOut",
        "OSPolicyInventoryFilterIn": "_osconfig_30_OSPolicyInventoryFilterIn",
        "OSPolicyInventoryFilterOut": "_osconfig_31_OSPolicyInventoryFilterOut",
        "GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataIn": "_osconfig_32_GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataIn",
        "GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataOut": "_osconfig_33_GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataOut",
        "InventorySoftwarePackageIn": "_osconfig_34_InventorySoftwarePackageIn",
        "InventorySoftwarePackageOut": "_osconfig_35_InventorySoftwarePackageOut",
        "EmptyIn": "_osconfig_36_EmptyIn",
        "EmptyOut": "_osconfig_37_EmptyOut",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepIn": "_osconfig_38_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepIn",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepOut": "_osconfig_39_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepOut",
        "OSPolicyAssignmentIn": "_osconfig_40_OSPolicyAssignmentIn",
        "OSPolicyAssignmentOut": "_osconfig_41_OSPolicyAssignmentOut",
        "OSPolicyIn": "_osconfig_42_OSPolicyIn",
        "OSPolicyOut": "_osconfig_43_OSPolicyOut",
        "OSPolicyResourcePackageResourceIn": "_osconfig_44_OSPolicyResourcePackageResourceIn",
        "OSPolicyResourcePackageResourceOut": "_osconfig_45_OSPolicyResourcePackageResourceOut",
        "OSPolicyResourceFileResourceIn": "_osconfig_46_OSPolicyResourceFileResourceIn",
        "OSPolicyResourceFileResourceOut": "_osconfig_47_OSPolicyResourceFileResourceOut",
        "OSPolicyResourceRepositoryResourceGooRepositoryIn": "_osconfig_48_OSPolicyResourceRepositoryResourceGooRepositoryIn",
        "OSPolicyResourceRepositoryResourceGooRepositoryOut": "_osconfig_49_OSPolicyResourceRepositoryResourceGooRepositoryOut",
        "RecurringScheduleIn": "_osconfig_50_RecurringScheduleIn",
        "RecurringScheduleOut": "_osconfig_51_RecurringScheduleOut",
        "ListOSPolicyAssignmentReportsResponseIn": "_osconfig_52_ListOSPolicyAssignmentReportsResponseIn",
        "ListOSPolicyAssignmentReportsResponseOut": "_osconfig_53_ListOSPolicyAssignmentReportsResponseOut",
        "TimeZoneIn": "_osconfig_54_TimeZoneIn",
        "TimeZoneOut": "_osconfig_55_TimeZoneOut",
        "OSPolicyResourceRepositoryResourceIn": "_osconfig_56_OSPolicyResourceRepositoryResourceIn",
        "OSPolicyResourceRepositoryResourceOut": "_osconfig_57_OSPolicyResourceRepositoryResourceOut",
        "ListPatchJobsResponseIn": "_osconfig_58_ListPatchJobsResponseIn",
        "ListPatchJobsResponseOut": "_osconfig_59_ListPatchJobsResponseOut",
        "OperationIn": "_osconfig_60_OperationIn",
        "OperationOut": "_osconfig_61_OperationOut",
        "InventoryWindowsApplicationIn": "_osconfig_62_InventoryWindowsApplicationIn",
        "InventoryWindowsApplicationOut": "_osconfig_63_InventoryWindowsApplicationOut",
        "OSPolicyResourcePackageResourceDebIn": "_osconfig_64_OSPolicyResourcePackageResourceDebIn",
        "OSPolicyResourcePackageResourceDebOut": "_osconfig_65_OSPolicyResourcePackageResourceDebOut",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputIn": "_osconfig_66_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputIn",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputOut": "_osconfig_67_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputOut",
        "OSPolicyResourcePackageResourceZypperIn": "_osconfig_68_OSPolicyResourcePackageResourceZypperIn",
        "OSPolicyResourcePackageResourceZypperOut": "_osconfig_69_OSPolicyResourcePackageResourceZypperOut",
        "OneTimeScheduleIn": "_osconfig_70_OneTimeScheduleIn",
        "OneTimeScheduleOut": "_osconfig_71_OneTimeScheduleOut",
        "ResumePatchDeploymentRequestIn": "_osconfig_72_ResumePatchDeploymentRequestIn",
        "ResumePatchDeploymentRequestOut": "_osconfig_73_ResumePatchDeploymentRequestOut",
        "TimeOfDayIn": "_osconfig_74_TimeOfDayIn",
        "TimeOfDayOut": "_osconfig_75_TimeOfDayOut",
        "OSPolicyResourcePackageResourceMSIIn": "_osconfig_76_OSPolicyResourcePackageResourceMSIIn",
        "OSPolicyResourcePackageResourceMSIOut": "_osconfig_77_OSPolicyResourcePackageResourceMSIOut",
        "OSPolicyResourceExecResourceExecIn": "_osconfig_78_OSPolicyResourceExecResourceExecIn",
        "OSPolicyResourceExecResourceExecOut": "_osconfig_79_OSPolicyResourceExecResourceExecOut",
        "OSPolicyResourceRepositoryResourceZypperRepositoryIn": "_osconfig_80_OSPolicyResourceRepositoryResourceZypperRepositoryIn",
        "OSPolicyResourceRepositoryResourceZypperRepositoryOut": "_osconfig_81_OSPolicyResourceRepositoryResourceZypperRepositoryOut",
        "OSPolicyResourceExecResourceIn": "_osconfig_82_OSPolicyResourceExecResourceIn",
        "OSPolicyResourceExecResourceOut": "_osconfig_83_OSPolicyResourceExecResourceOut",
        "VulnerabilityReportVulnerabilityIn": "_osconfig_84_VulnerabilityReportVulnerabilityIn",
        "VulnerabilityReportVulnerabilityOut": "_osconfig_85_VulnerabilityReportVulnerabilityOut",
        "ListOSPolicyAssignmentsResponseIn": "_osconfig_86_ListOSPolicyAssignmentsResponseIn",
        "ListOSPolicyAssignmentsResponseOut": "_osconfig_87_ListOSPolicyAssignmentsResponseOut",
        "PatchRolloutIn": "_osconfig_88_PatchRolloutIn",
        "PatchRolloutOut": "_osconfig_89_PatchRolloutOut",
        "YumSettingsIn": "_osconfig_90_YumSettingsIn",
        "YumSettingsOut": "_osconfig_91_YumSettingsOut",
        "ListPatchDeploymentsResponseIn": "_osconfig_92_ListPatchDeploymentsResponseIn",
        "ListPatchDeploymentsResponseOut": "_osconfig_93_ListPatchDeploymentsResponseOut",
        "OSPolicyResourceRepositoryResourceAptRepositoryIn": "_osconfig_94_OSPolicyResourceRepositoryResourceAptRepositoryIn",
        "OSPolicyResourceRepositoryResourceAptRepositoryOut": "_osconfig_95_OSPolicyResourceRepositoryResourceAptRepositoryOut",
        "OSPolicyAssignmentReportIn": "_osconfig_96_OSPolicyAssignmentReportIn",
        "OSPolicyAssignmentReportOut": "_osconfig_97_OSPolicyAssignmentReportOut",
        "InventoryWindowsUpdatePackageWindowsUpdateCategoryIn": "_osconfig_98_InventoryWindowsUpdatePackageWindowsUpdateCategoryIn",
        "InventoryWindowsUpdatePackageWindowsUpdateCategoryOut": "_osconfig_99_InventoryWindowsUpdatePackageWindowsUpdateCategoryOut",
        "PatchConfigIn": "_osconfig_100_PatchConfigIn",
        "PatchConfigOut": "_osconfig_101_PatchConfigOut",
        "OSPolicyResourcePackageResourceRPMIn": "_osconfig_102_OSPolicyResourcePackageResourceRPMIn",
        "OSPolicyResourcePackageResourceRPMOut": "_osconfig_103_OSPolicyResourcePackageResourceRPMOut",
        "DateIn": "_osconfig_104_DateIn",
        "DateOut": "_osconfig_105_DateOut",
        "MonthlyScheduleIn": "_osconfig_106_MonthlyScheduleIn",
        "MonthlyScheduleOut": "_osconfig_107_MonthlyScheduleOut",
        "VulnerabilityReportVulnerabilityDetailsReferenceIn": "_osconfig_108_VulnerabilityReportVulnerabilityDetailsReferenceIn",
        "VulnerabilityReportVulnerabilityDetailsReferenceOut": "_osconfig_109_VulnerabilityReportVulnerabilityDetailsReferenceOut",
        "PatchInstanceFilterGroupLabelIn": "_osconfig_110_PatchInstanceFilterGroupLabelIn",
        "PatchInstanceFilterGroupLabelOut": "_osconfig_111_PatchInstanceFilterGroupLabelOut",
        "OSPolicyAssignmentLabelSetIn": "_osconfig_112_OSPolicyAssignmentLabelSetIn",
        "OSPolicyAssignmentLabelSetOut": "_osconfig_113_OSPolicyAssignmentLabelSetOut",
        "OSPolicyAssignmentRolloutIn": "_osconfig_114_OSPolicyAssignmentRolloutIn",
        "OSPolicyAssignmentRolloutOut": "_osconfig_115_OSPolicyAssignmentRolloutOut",
        "CancelOperationRequestIn": "_osconfig_116_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_osconfig_117_CancelOperationRequestOut",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceIn": "_osconfig_118_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceIn",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOut": "_osconfig_119_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOut",
        "FixedOrPercentIn": "_osconfig_120_FixedOrPercentIn",
        "FixedOrPercentOut": "_osconfig_121_FixedOrPercentOut",
        "ZypperSettingsIn": "_osconfig_122_ZypperSettingsIn",
        "ZypperSettingsOut": "_osconfig_123_ZypperSettingsOut",
        "WeekDayOfMonthIn": "_osconfig_124_WeekDayOfMonthIn",
        "WeekDayOfMonthOut": "_osconfig_125_WeekDayOfMonthOut",
        "PausePatchDeploymentRequestIn": "_osconfig_126_PausePatchDeploymentRequestIn",
        "PausePatchDeploymentRequestOut": "_osconfig_127_PausePatchDeploymentRequestOut",
        "OSPolicyResourceIn": "_osconfig_128_OSPolicyResourceIn",
        "OSPolicyResourceOut": "_osconfig_129_OSPolicyResourceOut",
        "OSPolicyResourceRepositoryResourceYumRepositoryIn": "_osconfig_130_OSPolicyResourceRepositoryResourceYumRepositoryIn",
        "OSPolicyResourceRepositoryResourceYumRepositoryOut": "_osconfig_131_OSPolicyResourceRepositoryResourceYumRepositoryOut",
        "OSPolicyResourceFileIn": "_osconfig_132_OSPolicyResourceFileIn",
        "OSPolicyResourceFileOut": "_osconfig_133_OSPolicyResourceFileOut",
        "PatchInstanceFilterIn": "_osconfig_134_PatchInstanceFilterIn",
        "PatchInstanceFilterOut": "_osconfig_135_PatchInstanceFilterOut",
        "ListPatchJobInstanceDetailsResponseIn": "_osconfig_136_ListPatchJobInstanceDetailsResponseIn",
        "ListPatchJobInstanceDetailsResponseOut": "_osconfig_137_ListPatchJobInstanceDetailsResponseOut",
        "StatusIn": "_osconfig_138_StatusIn",
        "StatusOut": "_osconfig_139_StatusOut",
        "InventoryZypperPatchIn": "_osconfig_140_InventoryZypperPatchIn",
        "InventoryZypperPatchOut": "_osconfig_141_InventoryZypperPatchOut",
        "ListOSPolicyAssignmentRevisionsResponseIn": "_osconfig_142_ListOSPolicyAssignmentRevisionsResponseIn",
        "ListOSPolicyAssignmentRevisionsResponseOut": "_osconfig_143_ListOSPolicyAssignmentRevisionsResponseOut",
        "InventoryIn": "_osconfig_144_InventoryIn",
        "InventoryOut": "_osconfig_145_InventoryOut",
        "PatchJobInstanceDetailsIn": "_osconfig_146_PatchJobInstanceDetailsIn",
        "PatchJobInstanceDetailsOut": "_osconfig_147_PatchJobInstanceDetailsOut",
        "WeeklyScheduleIn": "_osconfig_148_WeeklyScheduleIn",
        "WeeklyScheduleOut": "_osconfig_149_WeeklyScheduleOut",
        "OSPolicyAssignmentReportOSPolicyComplianceIn": "_osconfig_150_OSPolicyAssignmentReportOSPolicyComplianceIn",
        "OSPolicyAssignmentReportOSPolicyComplianceOut": "_osconfig_151_OSPolicyAssignmentReportOSPolicyComplianceOut",
        "OSPolicyResourceGroupIn": "_osconfig_152_OSPolicyResourceGroupIn",
        "OSPolicyResourceGroupOut": "_osconfig_153_OSPolicyResourceGroupOut",
        "AptSettingsIn": "_osconfig_154_AptSettingsIn",
        "AptSettingsOut": "_osconfig_155_AptSettingsOut",
        "OSPolicyResourceFileGcsIn": "_osconfig_156_OSPolicyResourceFileGcsIn",
        "OSPolicyResourceFileGcsOut": "_osconfig_157_OSPolicyResourceFileGcsOut",
        "ExecStepIn": "_osconfig_158_ExecStepIn",
        "ExecStepOut": "_osconfig_159_ExecStepOut",
        "OSPolicyResourcePackageResourceYUMIn": "_osconfig_160_OSPolicyResourcePackageResourceYUMIn",
        "OSPolicyResourcePackageResourceYUMOut": "_osconfig_161_OSPolicyResourcePackageResourceYUMOut",
        "OSPolicyAssignmentInstanceFilterInventoryIn": "_osconfig_162_OSPolicyAssignmentInstanceFilterInventoryIn",
        "OSPolicyAssignmentInstanceFilterInventoryOut": "_osconfig_163_OSPolicyAssignmentInstanceFilterInventoryOut",
        "GooSettingsIn": "_osconfig_164_GooSettingsIn",
        "GooSettingsOut": "_osconfig_165_GooSettingsOut",
        "InventoryWindowsQuickFixEngineeringPackageIn": "_osconfig_166_InventoryWindowsQuickFixEngineeringPackageIn",
        "InventoryWindowsQuickFixEngineeringPackageOut": "_osconfig_167_InventoryWindowsQuickFixEngineeringPackageOut",
        "PatchJobIn": "_osconfig_168_PatchJobIn",
        "PatchJobOut": "_osconfig_169_PatchJobOut",
        "InventoryWindowsUpdatePackageIn": "_osconfig_170_InventoryWindowsUpdatePackageIn",
        "InventoryWindowsUpdatePackageOut": "_osconfig_171_InventoryWindowsUpdatePackageOut",
        "ExecStepConfigIn": "_osconfig_172_ExecStepConfigIn",
        "ExecStepConfigOut": "_osconfig_173_ExecStepConfigOut",
        "CVSSv3In": "_osconfig_174_CVSSv3In",
        "CVSSv3Out": "_osconfig_175_CVSSv3Out",
        "PatchJobInstanceDetailsSummaryIn": "_osconfig_176_PatchJobInstanceDetailsSummaryIn",
        "PatchJobInstanceDetailsSummaryOut": "_osconfig_177_PatchJobInstanceDetailsSummaryOut",
        "ExecutePatchJobRequestIn": "_osconfig_178_ExecutePatchJobRequestIn",
        "ExecutePatchJobRequestOut": "_osconfig_179_ExecutePatchJobRequestOut",
        "InventoryItemIn": "_osconfig_180_InventoryItemIn",
        "InventoryItemOut": "_osconfig_181_InventoryItemOut",
        "OSPolicyResourcePackageResourceGooGetIn": "_osconfig_182_OSPolicyResourcePackageResourceGooGetIn",
        "OSPolicyResourcePackageResourceGooGetOut": "_osconfig_183_OSPolicyResourcePackageResourceGooGetOut",
        "WindowsUpdateSettingsIn": "_osconfig_184_WindowsUpdateSettingsIn",
        "WindowsUpdateSettingsOut": "_osconfig_185_WindowsUpdateSettingsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["InventoryVersionedPackageIn"] = t.struct(
        {
            "architecture": t.string().optional(),
            "version": t.string().optional(),
            "packageName": t.string().optional(),
        }
    ).named(renames["InventoryVersionedPackageIn"])
    types["InventoryVersionedPackageOut"] = t.struct(
        {
            "architecture": t.string().optional(),
            "version": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryVersionedPackageOut"])
    types["InventoryOsInfoIn"] = t.struct(
        {
            "hostname": t.string().optional(),
            "architecture": t.string().optional(),
            "kernelRelease": t.string().optional(),
            "osconfigAgentVersion": t.string().optional(),
            "kernelVersion": t.string().optional(),
            "longName": t.string().optional(),
            "shortName": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["InventoryOsInfoIn"])
    types["InventoryOsInfoOut"] = t.struct(
        {
            "hostname": t.string().optional(),
            "architecture": t.string().optional(),
            "kernelRelease": t.string().optional(),
            "osconfigAgentVersion": t.string().optional(),
            "kernelVersion": t.string().optional(),
            "longName": t.string().optional(),
            "shortName": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryOsInfoOut"])
    types["OSPolicyAssignmentOperationMetadataIn"] = t.struct(
        {
            "rolloutStartTime": t.string().optional(),
            "rolloutUpdateTime": t.string().optional(),
            "rolloutState": t.string().optional(),
            "apiMethod": t.string().optional(),
            "osPolicyAssignment": t.string().optional(),
        }
    ).named(renames["OSPolicyAssignmentOperationMetadataIn"])
    types["OSPolicyAssignmentOperationMetadataOut"] = t.struct(
        {
            "rolloutStartTime": t.string().optional(),
            "rolloutUpdateTime": t.string().optional(),
            "rolloutState": t.string().optional(),
            "apiMethod": t.string().optional(),
            "osPolicyAssignment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentOperationMetadataOut"])
    types["VulnerabilityReportIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VulnerabilityReportIn"]
    )
    types["VulnerabilityReportOut"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "vulnerabilities": t.array(
                t.proxy(renames["VulnerabilityReportVulnerabilityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityReportOut"])
    types["OSPolicyAssignmentInstanceFilterIn"] = t.struct(
        {
            "exclusionLabels": t.array(
                t.proxy(renames["OSPolicyAssignmentLabelSetIn"])
            ).optional(),
            "all": t.boolean().optional(),
            "inclusionLabels": t.array(
                t.proxy(renames["OSPolicyAssignmentLabelSetIn"])
            ).optional(),
            "inventories": t.array(
                t.proxy(renames["OSPolicyAssignmentInstanceFilterInventoryIn"])
            ).optional(),
        }
    ).named(renames["OSPolicyAssignmentInstanceFilterIn"])
    types["OSPolicyAssignmentInstanceFilterOut"] = t.struct(
        {
            "exclusionLabels": t.array(
                t.proxy(renames["OSPolicyAssignmentLabelSetOut"])
            ).optional(),
            "all": t.boolean().optional(),
            "inclusionLabels": t.array(
                t.proxy(renames["OSPolicyAssignmentLabelSetOut"])
            ).optional(),
            "inventories": t.array(
                t.proxy(renames["OSPolicyAssignmentInstanceFilterInventoryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentInstanceFilterOut"])
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
    types["ListInventoriesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "inventories": t.array(t.proxy(renames["InventoryIn"])).optional(),
        }
    ).named(renames["ListInventoriesResponseIn"])
    types["ListInventoriesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "inventories": t.array(t.proxy(renames["InventoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInventoriesResponseOut"])
    types["VulnerabilityReportVulnerabilityDetailsIn"] = t.struct(
        {
            "description": t.string().optional(),
            "references": t.array(
                t.proxy(renames["VulnerabilityReportVulnerabilityDetailsReferenceIn"])
            ).optional(),
            "severity": t.string().optional(),
            "cvssV2Score": t.number().optional(),
            "cve": t.string().optional(),
            "cvssV3": t.proxy(renames["CVSSv3In"]).optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityDetailsIn"])
    types["VulnerabilityReportVulnerabilityDetailsOut"] = t.struct(
        {
            "description": t.string().optional(),
            "references": t.array(
                t.proxy(renames["VulnerabilityReportVulnerabilityDetailsReferenceOut"])
            ).optional(),
            "severity": t.string().optional(),
            "cvssV2Score": t.number().optional(),
            "cve": t.string().optional(),
            "cvssV3": t.proxy(renames["CVSSv3Out"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityDetailsOut"])
    types["GcsObjectIn"] = t.struct(
        {"object": t.string(), "bucket": t.string(), "generationNumber": t.string()}
    ).named(renames["GcsObjectIn"])
    types["GcsObjectOut"] = t.struct(
        {
            "object": t.string(),
            "bucket": t.string(),
            "generationNumber": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsObjectOut"])
    types["PatchDeploymentIn"] = t.struct(
        {
            "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
            "oneTimeSchedule": t.proxy(renames["OneTimeScheduleIn"]),
            "name": t.string().optional(),
            "duration": t.string().optional(),
            "description": t.string().optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
            "recurringSchedule": t.proxy(renames["RecurringScheduleIn"]),
            "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
        }
    ).named(renames["PatchDeploymentIn"])
    types["PatchDeploymentOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "patchConfig": t.proxy(renames["PatchConfigOut"]).optional(),
            "lastExecuteTime": t.string().optional(),
            "oneTimeSchedule": t.proxy(renames["OneTimeScheduleOut"]),
            "name": t.string().optional(),
            "duration": t.string().optional(),
            "description": t.string().optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterOut"]),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "recurringSchedule": t.proxy(renames["RecurringScheduleOut"]),
            "rollout": t.proxy(renames["PatchRolloutOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchDeploymentOut"])
    types["VulnerabilityReportVulnerabilityItemIn"] = t.struct(
        {
            "fixedCpeUri": t.string().optional(),
            "availableInventoryItemId": t.string().optional(),
            "upstreamFix": t.string().optional(),
            "installedInventoryItemId": t.string().optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityItemIn"])
    types["VulnerabilityReportVulnerabilityItemOut"] = t.struct(
        {
            "fixedCpeUri": t.string().optional(),
            "availableInventoryItemId": t.string().optional(),
            "upstreamFix": t.string().optional(),
            "installedInventoryItemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityItemOut"])
    types["CancelPatchJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelPatchJobRequestIn"]
    )
    types["CancelPatchJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelPatchJobRequestOut"])
    types["OSPolicyResourcePackageResourceAPTIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["OSPolicyResourcePackageResourceAPTIn"])
    types["OSPolicyResourcePackageResourceAPTOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OSPolicyResourcePackageResourceAPTOut"])
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
    types["GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataIn"] = t.struct(
        {
            "rolloutUpdateTime": t.string().optional(),
            "osPolicyAssignment": t.string().optional(),
            "rolloutState": t.string().optional(),
            "apiMethod": t.string().optional(),
            "rolloutStartTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataIn"])
    types["GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataOut"] = t.struct(
        {
            "rolloutUpdateTime": t.string().optional(),
            "osPolicyAssignment": t.string().optional(),
            "rolloutState": t.string().optional(),
            "apiMethod": t.string().optional(),
            "rolloutStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataOut"])
    types["InventorySoftwarePackageIn"] = t.struct(
        {
            "aptPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
            "wuaPackage": t.proxy(
                renames["InventoryWindowsUpdatePackageIn"]
            ).optional(),
            "qfePackage": t.proxy(
                renames["InventoryWindowsQuickFixEngineeringPackageIn"]
            ).optional(),
            "googetPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
            "zypperPatch": t.proxy(renames["InventoryZypperPatchIn"]).optional(),
            "yumPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
            "cosPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
            "windowsApplication": t.proxy(
                renames["InventoryWindowsApplicationIn"]
            ).optional(),
            "zypperPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
        }
    ).named(renames["InventorySoftwarePackageIn"])
    types["InventorySoftwarePackageOut"] = t.struct(
        {
            "aptPackage": t.proxy(renames["InventoryVersionedPackageOut"]).optional(),
            "wuaPackage": t.proxy(
                renames["InventoryWindowsUpdatePackageOut"]
            ).optional(),
            "qfePackage": t.proxy(
                renames["InventoryWindowsQuickFixEngineeringPackageOut"]
            ).optional(),
            "googetPackage": t.proxy(
                renames["InventoryVersionedPackageOut"]
            ).optional(),
            "zypperPatch": t.proxy(renames["InventoryZypperPatchOut"]).optional(),
            "yumPackage": t.proxy(renames["InventoryVersionedPackageOut"]).optional(),
            "cosPackage": t.proxy(renames["InventoryVersionedPackageOut"]).optional(),
            "windowsApplication": t.proxy(
                renames["InventoryWindowsApplicationOut"]
            ).optional(),
            "zypperPackage": t.proxy(
                renames["InventoryVersionedPackageOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySoftwarePackageOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types[
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepIn"
    ] = t.struct(
        {"type": t.string().optional(), "errorMessage": t.string().optional()}
    ).named(
        renames[
            "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepIn"
        ]
    )
    types[
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepOut"
    ] = t.struct(
        {
            "type": t.string().optional(),
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepOut"
        ]
    )
    types["OSPolicyAssignmentIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "instanceFilter": t.proxy(renames["OSPolicyAssignmentInstanceFilterIn"]),
            "rollout": t.proxy(renames["OSPolicyAssignmentRolloutIn"]),
            "name": t.string().optional(),
            "osPolicies": t.array(t.proxy(renames["OSPolicyIn"])),
        }
    ).named(renames["OSPolicyAssignmentIn"])
    types["OSPolicyAssignmentOut"] = t.struct(
        {
            "baseline": t.boolean().optional(),
            "revisionCreateTime": t.string().optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "deleted": t.boolean().optional(),
            "reconciling": t.boolean().optional(),
            "instanceFilter": t.proxy(renames["OSPolicyAssignmentInstanceFilterOut"]),
            "rolloutState": t.string().optional(),
            "rollout": t.proxy(renames["OSPolicyAssignmentRolloutOut"]),
            "name": t.string().optional(),
            "osPolicies": t.array(t.proxy(renames["OSPolicyOut"])),
            "revisionId": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentOut"])
    types["OSPolicyIn"] = t.struct(
        {
            "resourceGroups": t.array(t.proxy(renames["OSPolicyResourceGroupIn"])),
            "description": t.string().optional(),
            "mode": t.string(),
            "id": t.string(),
            "allowNoResourceGroupMatch": t.boolean().optional(),
        }
    ).named(renames["OSPolicyIn"])
    types["OSPolicyOut"] = t.struct(
        {
            "resourceGroups": t.array(t.proxy(renames["OSPolicyResourceGroupOut"])),
            "description": t.string().optional(),
            "mode": t.string(),
            "id": t.string(),
            "allowNoResourceGroupMatch": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyOut"])
    types["OSPolicyResourcePackageResourceIn"] = t.struct(
        {
            "deb": t.proxy(renames["OSPolicyResourcePackageResourceDebIn"]).optional(),
            "msi": t.proxy(renames["OSPolicyResourcePackageResourceMSIIn"]).optional(),
            "desiredState": t.string(),
            "zypper": t.proxy(
                renames["OSPolicyResourcePackageResourceZypperIn"]
            ).optional(),
            "apt": t.proxy(renames["OSPolicyResourcePackageResourceAPTIn"]).optional(),
            "googet": t.proxy(
                renames["OSPolicyResourcePackageResourceGooGetIn"]
            ).optional(),
            "rpm": t.proxy(renames["OSPolicyResourcePackageResourceRPMIn"]).optional(),
            "yum": t.proxy(renames["OSPolicyResourcePackageResourceYUMIn"]).optional(),
        }
    ).named(renames["OSPolicyResourcePackageResourceIn"])
    types["OSPolicyResourcePackageResourceOut"] = t.struct(
        {
            "deb": t.proxy(renames["OSPolicyResourcePackageResourceDebOut"]).optional(),
            "msi": t.proxy(renames["OSPolicyResourcePackageResourceMSIOut"]).optional(),
            "desiredState": t.string(),
            "zypper": t.proxy(
                renames["OSPolicyResourcePackageResourceZypperOut"]
            ).optional(),
            "apt": t.proxy(renames["OSPolicyResourcePackageResourceAPTOut"]).optional(),
            "googet": t.proxy(
                renames["OSPolicyResourcePackageResourceGooGetOut"]
            ).optional(),
            "rpm": t.proxy(renames["OSPolicyResourcePackageResourceRPMOut"]).optional(),
            "yum": t.proxy(renames["OSPolicyResourcePackageResourceYUMOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourcePackageResourceOut"])
    types["OSPolicyResourceFileResourceIn"] = t.struct(
        {
            "file": t.proxy(renames["OSPolicyResourceFileIn"]).optional(),
            "state": t.string(),
            "permissions": t.string().optional(),
            "content": t.string().optional(),
            "path": t.string(),
        }
    ).named(renames["OSPolicyResourceFileResourceIn"])
    types["OSPolicyResourceFileResourceOut"] = t.struct(
        {
            "file": t.proxy(renames["OSPolicyResourceFileOut"]).optional(),
            "state": t.string(),
            "permissions": t.string().optional(),
            "content": t.string().optional(),
            "path": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceFileResourceOut"])
    types["OSPolicyResourceRepositoryResourceGooRepositoryIn"] = t.struct(
        {"url": t.string(), "name": t.string()}
    ).named(renames["OSPolicyResourceRepositoryResourceGooRepositoryIn"])
    types["OSPolicyResourceRepositoryResourceGooRepositoryOut"] = t.struct(
        {
            "url": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceGooRepositoryOut"])
    types["RecurringScheduleIn"] = t.struct(
        {
            "weekly": t.proxy(renames["WeeklyScheduleIn"]),
            "endTime": t.string().optional(),
            "timeOfDay": t.proxy(renames["TimeOfDayIn"]),
            "monthly": t.proxy(renames["MonthlyScheduleIn"]),
            "startTime": t.string().optional(),
            "timeZone": t.proxy(renames["TimeZoneIn"]),
            "frequency": t.string(),
        }
    ).named(renames["RecurringScheduleIn"])
    types["RecurringScheduleOut"] = t.struct(
        {
            "weekly": t.proxy(renames["WeeklyScheduleOut"]),
            "endTime": t.string().optional(),
            "timeOfDay": t.proxy(renames["TimeOfDayOut"]),
            "monthly": t.proxy(renames["MonthlyScheduleOut"]),
            "lastExecuteTime": t.string().optional(),
            "startTime": t.string().optional(),
            "timeZone": t.proxy(renames["TimeZoneOut"]),
            "nextExecuteTime": t.string().optional(),
            "frequency": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecurringScheduleOut"])
    types["ListOSPolicyAssignmentReportsResponseIn"] = t.struct(
        {
            "osPolicyAssignmentReports": t.array(
                t.proxy(renames["OSPolicyAssignmentReportIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOSPolicyAssignmentReportsResponseIn"])
    types["ListOSPolicyAssignmentReportsResponseOut"] = t.struct(
        {
            "osPolicyAssignmentReports": t.array(
                t.proxy(renames["OSPolicyAssignmentReportOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOSPolicyAssignmentReportsResponseOut"])
    types["TimeZoneIn"] = t.struct(
        {"version": t.string().optional(), "id": t.string().optional()}
    ).named(renames["TimeZoneIn"])
    types["TimeZoneOut"] = t.struct(
        {
            "version": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeZoneOut"])
    types["OSPolicyResourceRepositoryResourceIn"] = t.struct(
        {
            "zypper": t.proxy(
                renames["OSPolicyResourceRepositoryResourceZypperRepositoryIn"]
            ).optional(),
            "yum": t.proxy(
                renames["OSPolicyResourceRepositoryResourceYumRepositoryIn"]
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
            "zypper": t.proxy(
                renames["OSPolicyResourceRepositoryResourceZypperRepositoryOut"]
            ).optional(),
            "yum": t.proxy(
                renames["OSPolicyResourceRepositoryResourceYumRepositoryOut"]
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
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["InventoryWindowsApplicationIn"] = t.struct(
        {
            "installDate": t.proxy(renames["DateIn"]).optional(),
            "publisher": t.string().optional(),
            "displayName": t.string().optional(),
            "displayVersion": t.string().optional(),
            "helpLink": t.string().optional(),
        }
    ).named(renames["InventoryWindowsApplicationIn"])
    types["InventoryWindowsApplicationOut"] = t.struct(
        {
            "installDate": t.proxy(renames["DateOut"]).optional(),
            "publisher": t.string().optional(),
            "displayName": t.string().optional(),
            "displayVersion": t.string().optional(),
            "helpLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryWindowsApplicationOut"])
    types["OSPolicyResourcePackageResourceDebIn"] = t.struct(
        {
            "source": t.proxy(renames["OSPolicyResourceFileIn"]),
            "pullDeps": t.boolean().optional(),
        }
    ).named(renames["OSPolicyResourcePackageResourceDebIn"])
    types["OSPolicyResourcePackageResourceDebOut"] = t.struct(
        {
            "source": t.proxy(renames["OSPolicyResourceFileOut"]),
            "pullDeps": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourcePackageResourceDebOut"])
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
    types["OSPolicyResourcePackageResourceZypperIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["OSPolicyResourcePackageResourceZypperIn"])
    types["OSPolicyResourcePackageResourceZypperOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OSPolicyResourcePackageResourceZypperOut"])
    types["OneTimeScheduleIn"] = t.struct({"executeTime": t.string()}).named(
        renames["OneTimeScheduleIn"]
    )
    types["OneTimeScheduleOut"] = t.struct(
        {
            "executeTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OneTimeScheduleOut"])
    types["ResumePatchDeploymentRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResumePatchDeploymentRequestIn"])
    types["ResumePatchDeploymentRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumePatchDeploymentRequestOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
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
    types["OSPolicyResourceExecResourceExecIn"] = t.struct(
        {
            "script": t.string().optional(),
            "interpreter": t.string(),
            "outputFilePath": t.string().optional(),
            "file": t.proxy(renames["OSPolicyResourceFileIn"]).optional(),
            "args": t.array(t.string()).optional(),
        }
    ).named(renames["OSPolicyResourceExecResourceExecIn"])
    types["OSPolicyResourceExecResourceExecOut"] = t.struct(
        {
            "script": t.string().optional(),
            "interpreter": t.string(),
            "outputFilePath": t.string().optional(),
            "file": t.proxy(renames["OSPolicyResourceFileOut"]).optional(),
            "args": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceExecResourceExecOut"])
    types["OSPolicyResourceRepositoryResourceZypperRepositoryIn"] = t.struct(
        {
            "id": t.string(),
            "displayName": t.string().optional(),
            "gpgKeys": t.array(t.string()).optional(),
            "baseUrl": t.string(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceZypperRepositoryIn"])
    types["OSPolicyResourceRepositoryResourceZypperRepositoryOut"] = t.struct(
        {
            "id": t.string(),
            "displayName": t.string().optional(),
            "gpgKeys": t.array(t.string()).optional(),
            "baseUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceZypperRepositoryOut"])
    types["OSPolicyResourceExecResourceIn"] = t.struct(
        {
            "enforce": t.proxy(
                renames["OSPolicyResourceExecResourceExecIn"]
            ).optional(),
            "validate": t.proxy(renames["OSPolicyResourceExecResourceExecIn"]),
        }
    ).named(renames["OSPolicyResourceExecResourceIn"])
    types["OSPolicyResourceExecResourceOut"] = t.struct(
        {
            "enforce": t.proxy(
                renames["OSPolicyResourceExecResourceExecOut"]
            ).optional(),
            "validate": t.proxy(renames["OSPolicyResourceExecResourceExecOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceExecResourceOut"])
    types["VulnerabilityReportVulnerabilityIn"] = t.struct(
        {
            "installedInventoryItemIds": t.array(t.string()).optional(),
            "items": t.array(
                t.proxy(renames["VulnerabilityReportVulnerabilityItemIn"])
            ).optional(),
            "details": t.proxy(
                renames["VulnerabilityReportVulnerabilityDetailsIn"]
            ).optional(),
            "createTime": t.string().optional(),
            "availableInventoryItemIds": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityIn"])
    types["VulnerabilityReportVulnerabilityOut"] = t.struct(
        {
            "installedInventoryItemIds": t.array(t.string()).optional(),
            "items": t.array(
                t.proxy(renames["VulnerabilityReportVulnerabilityItemOut"])
            ).optional(),
            "details": t.proxy(
                renames["VulnerabilityReportVulnerabilityDetailsOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "availableInventoryItemIds": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityOut"])
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
    types["PatchRolloutIn"] = t.struct(
        {
            "mode": t.string().optional(),
            "disruptionBudget": t.proxy(renames["FixedOrPercentIn"]).optional(),
        }
    ).named(renames["PatchRolloutIn"])
    types["PatchRolloutOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "disruptionBudget": t.proxy(renames["FixedOrPercentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchRolloutOut"])
    types["YumSettingsIn"] = t.struct(
        {
            "security": t.boolean().optional(),
            "minimal": t.boolean().optional(),
            "exclusivePackages": t.array(t.string()).optional(),
            "excludes": t.array(t.string()).optional(),
        }
    ).named(renames["YumSettingsIn"])
    types["YumSettingsOut"] = t.struct(
        {
            "security": t.boolean().optional(),
            "minimal": t.boolean().optional(),
            "exclusivePackages": t.array(t.string()).optional(),
            "excludes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YumSettingsOut"])
    types["ListPatchDeploymentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "patchDeployments": t.array(
                t.proxy(renames["PatchDeploymentIn"])
            ).optional(),
        }
    ).named(renames["ListPatchDeploymentsResponseIn"])
    types["ListPatchDeploymentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "patchDeployments": t.array(
                t.proxy(renames["PatchDeploymentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPatchDeploymentsResponseOut"])
    types["OSPolicyResourceRepositoryResourceAptRepositoryIn"] = t.struct(
        {
            "archiveType": t.string(),
            "gpgKey": t.string().optional(),
            "distribution": t.string(),
            "uri": t.string(),
            "components": t.array(t.string()),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceAptRepositoryIn"])
    types["OSPolicyResourceRepositoryResourceAptRepositoryOut"] = t.struct(
        {
            "archiveType": t.string(),
            "gpgKey": t.string().optional(),
            "distribution": t.string(),
            "uri": t.string(),
            "components": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceAptRepositoryOut"])
    types["OSPolicyAssignmentReportIn"] = t.struct(
        {
            "instance": t.string().optional(),
            "osPolicyAssignment": t.string().optional(),
            "osPolicyCompliances": t.array(
                t.proxy(renames["OSPolicyAssignmentReportOSPolicyComplianceIn"])
            ).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "lastRunId": t.string().optional(),
        }
    ).named(renames["OSPolicyAssignmentReportIn"])
    types["OSPolicyAssignmentReportOut"] = t.struct(
        {
            "instance": t.string().optional(),
            "osPolicyAssignment": t.string().optional(),
            "osPolicyCompliances": t.array(
                t.proxy(renames["OSPolicyAssignmentReportOSPolicyComplianceOut"])
            ).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "lastRunId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentReportOut"])
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
    types["PatchConfigIn"] = t.struct(
        {
            "preStep": t.proxy(renames["ExecStepIn"]).optional(),
            "windowsUpdate": t.proxy(renames["WindowsUpdateSettingsIn"]).optional(),
            "postStep": t.proxy(renames["ExecStepIn"]).optional(),
            "migInstancesAllowed": t.boolean().optional(),
            "yum": t.proxy(renames["YumSettingsIn"]).optional(),
            "zypper": t.proxy(renames["ZypperSettingsIn"]).optional(),
            "apt": t.proxy(renames["AptSettingsIn"]).optional(),
            "rebootConfig": t.string().optional(),
            "goo": t.proxy(renames["GooSettingsIn"]).optional(),
        }
    ).named(renames["PatchConfigIn"])
    types["PatchConfigOut"] = t.struct(
        {
            "preStep": t.proxy(renames["ExecStepOut"]).optional(),
            "windowsUpdate": t.proxy(renames["WindowsUpdateSettingsOut"]).optional(),
            "postStep": t.proxy(renames["ExecStepOut"]).optional(),
            "migInstancesAllowed": t.boolean().optional(),
            "yum": t.proxy(renames["YumSettingsOut"]).optional(),
            "zypper": t.proxy(renames["ZypperSettingsOut"]).optional(),
            "apt": t.proxy(renames["AptSettingsOut"]).optional(),
            "rebootConfig": t.string().optional(),
            "goo": t.proxy(renames["GooSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchConfigOut"])
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
    types["DateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["MonthlyScheduleIn"] = t.struct(
        {
            "weekDayOfMonth": t.proxy(renames["WeekDayOfMonthIn"]),
            "monthDay": t.integer(),
        }
    ).named(renames["MonthlyScheduleIn"])
    types["MonthlyScheduleOut"] = t.struct(
        {
            "weekDayOfMonth": t.proxy(renames["WeekDayOfMonthOut"]),
            "monthDay": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonthlyScheduleOut"])
    types["VulnerabilityReportVulnerabilityDetailsReferenceIn"] = t.struct(
        {"source": t.string().optional(), "url": t.string().optional()}
    ).named(renames["VulnerabilityReportVulnerabilityDetailsReferenceIn"])
    types["VulnerabilityReportVulnerabilityDetailsReferenceOut"] = t.struct(
        {
            "source": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityDetailsReferenceOut"])
    types["PatchInstanceFilterGroupLabelIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["PatchInstanceFilterGroupLabelIn"])
    types["PatchInstanceFilterGroupLabelOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchInstanceFilterGroupLabelOut"])
    types["OSPolicyAssignmentLabelSetIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["OSPolicyAssignmentLabelSetIn"])
    types["OSPolicyAssignmentLabelSetOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentLabelSetOut"])
    types["OSPolicyAssignmentRolloutIn"] = t.struct(
        {
            "disruptionBudget": t.proxy(renames["FixedOrPercentIn"]),
            "minWaitDuration": t.string(),
        }
    ).named(renames["OSPolicyAssignmentRolloutIn"])
    types["OSPolicyAssignmentRolloutOut"] = t.struct(
        {
            "disruptionBudget": t.proxy(renames["FixedOrPercentOut"]),
            "minWaitDuration": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentRolloutOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types[
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceIn"
    ] = t.struct(
        {
            "complianceState": t.string().optional(),
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
            "complianceState": t.string().optional(),
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
            "complianceStateReason": t.string().optional(),
            "osPolicyResourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOut"
        ]
    )
    types["FixedOrPercentIn"] = t.struct(
        {"percent": t.integer().optional(), "fixed": t.integer().optional()}
    ).named(renames["FixedOrPercentIn"])
    types["FixedOrPercentOut"] = t.struct(
        {
            "percent": t.integer().optional(),
            "fixed": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FixedOrPercentOut"])
    types["ZypperSettingsIn"] = t.struct(
        {
            "excludes": t.array(t.string()).optional(),
            "categories": t.array(t.string()).optional(),
            "severities": t.array(t.string()).optional(),
            "exclusivePatches": t.array(t.string()).optional(),
            "withOptional": t.boolean().optional(),
            "withUpdate": t.boolean().optional(),
        }
    ).named(renames["ZypperSettingsIn"])
    types["ZypperSettingsOut"] = t.struct(
        {
            "excludes": t.array(t.string()).optional(),
            "categories": t.array(t.string()).optional(),
            "severities": t.array(t.string()).optional(),
            "exclusivePatches": t.array(t.string()).optional(),
            "withOptional": t.boolean().optional(),
            "withUpdate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZypperSettingsOut"])
    types["WeekDayOfMonthIn"] = t.struct(
        {
            "weekOrdinal": t.integer(),
            "dayOffset": t.integer().optional(),
            "dayOfWeek": t.string(),
        }
    ).named(renames["WeekDayOfMonthIn"])
    types["WeekDayOfMonthOut"] = t.struct(
        {
            "weekOrdinal": t.integer(),
            "dayOffset": t.integer().optional(),
            "dayOfWeek": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeekDayOfMonthOut"])
    types["PausePatchDeploymentRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["PausePatchDeploymentRequestIn"])
    types["PausePatchDeploymentRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PausePatchDeploymentRequestOut"])
    types["OSPolicyResourceIn"] = t.struct(
        {
            "repository": t.proxy(
                renames["OSPolicyResourceRepositoryResourceIn"]
            ).optional(),
            "exec": t.proxy(renames["OSPolicyResourceExecResourceIn"]).optional(),
            "file": t.proxy(renames["OSPolicyResourceFileResourceIn"]).optional(),
            "id": t.string(),
            "pkg": t.proxy(renames["OSPolicyResourcePackageResourceIn"]).optional(),
        }
    ).named(renames["OSPolicyResourceIn"])
    types["OSPolicyResourceOut"] = t.struct(
        {
            "repository": t.proxy(
                renames["OSPolicyResourceRepositoryResourceOut"]
            ).optional(),
            "exec": t.proxy(renames["OSPolicyResourceExecResourceOut"]).optional(),
            "file": t.proxy(renames["OSPolicyResourceFileResourceOut"]).optional(),
            "id": t.string(),
            "pkg": t.proxy(renames["OSPolicyResourcePackageResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceOut"])
    types["OSPolicyResourceRepositoryResourceYumRepositoryIn"] = t.struct(
        {
            "id": t.string(),
            "baseUrl": t.string(),
            "gpgKeys": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceYumRepositoryIn"])
    types["OSPolicyResourceRepositoryResourceYumRepositoryOut"] = t.struct(
        {
            "id": t.string(),
            "baseUrl": t.string(),
            "gpgKeys": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceYumRepositoryOut"])
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
    types["PatchInstanceFilterIn"] = t.struct(
        {
            "instances": t.array(t.string()).optional(),
            "all": t.boolean().optional(),
            "zones": t.array(t.string()).optional(),
            "instanceNamePrefixes": t.array(t.string()).optional(),
            "groupLabels": t.array(
                t.proxy(renames["PatchInstanceFilterGroupLabelIn"])
            ).optional(),
        }
    ).named(renames["PatchInstanceFilterIn"])
    types["PatchInstanceFilterOut"] = t.struct(
        {
            "instances": t.array(t.string()).optional(),
            "all": t.boolean().optional(),
            "zones": t.array(t.string()).optional(),
            "instanceNamePrefixes": t.array(t.string()).optional(),
            "groupLabels": t.array(
                t.proxy(renames["PatchInstanceFilterGroupLabelOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchInstanceFilterOut"])
    types["ListPatchJobInstanceDetailsResponseIn"] = t.struct(
        {
            "patchJobInstanceDetails": t.array(
                t.proxy(renames["PatchJobInstanceDetailsIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPatchJobInstanceDetailsResponseIn"])
    types["ListPatchJobInstanceDetailsResponseOut"] = t.struct(
        {
            "patchJobInstanceDetails": t.array(
                t.proxy(renames["PatchJobInstanceDetailsOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPatchJobInstanceDetailsResponseOut"])
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
    types["InventoryZypperPatchIn"] = t.struct(
        {
            "category": t.string().optional(),
            "patchName": t.string().optional(),
            "summary": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["InventoryZypperPatchIn"])
    types["InventoryZypperPatchOut"] = t.struct(
        {
            "category": t.string().optional(),
            "patchName": t.string().optional(),
            "summary": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryZypperPatchOut"])
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
    types["InventoryIn"] = t.struct(
        {
            "osInfo": t.proxy(renames["InventoryOsInfoIn"]).optional(),
            "items": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["InventoryIn"])
    types["InventoryOut"] = t.struct(
        {
            "osInfo": t.proxy(renames["InventoryOsInfoOut"]).optional(),
            "items": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryOut"])
    types["PatchJobInstanceDetailsIn"] = t.struct(
        {
            "failureReason": t.string().optional(),
            "state": t.string().optional(),
            "instanceSystemId": t.string().optional(),
            "attemptCount": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["PatchJobInstanceDetailsIn"])
    types["PatchJobInstanceDetailsOut"] = t.struct(
        {
            "failureReason": t.string().optional(),
            "state": t.string().optional(),
            "instanceSystemId": t.string().optional(),
            "attemptCount": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchJobInstanceDetailsOut"])
    types["WeeklyScheduleIn"] = t.struct({"dayOfWeek": t.string()}).named(
        renames["WeeklyScheduleIn"]
    )
    types["WeeklyScheduleOut"] = t.struct(
        {"dayOfWeek": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WeeklyScheduleOut"])
    types["OSPolicyAssignmentReportOSPolicyComplianceIn"] = t.struct(
        {
            "complianceState": t.string().optional(),
            "osPolicyResourceCompliances": t.array(
                t.proxy(
                    renames[
                        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceIn"
                    ]
                )
            ).optional(),
            "complianceStateReason": t.string().optional(),
            "osPolicyId": t.string().optional(),
        }
    ).named(renames["OSPolicyAssignmentReportOSPolicyComplianceIn"])
    types["OSPolicyAssignmentReportOSPolicyComplianceOut"] = t.struct(
        {
            "complianceState": t.string().optional(),
            "osPolicyResourceCompliances": t.array(
                t.proxy(
                    renames[
                        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOut"
                    ]
                )
            ).optional(),
            "complianceStateReason": t.string().optional(),
            "osPolicyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentReportOSPolicyComplianceOut"])
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
    types["AptSettingsIn"] = t.struct(
        {
            "exclusivePackages": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "excludes": t.array(t.string()).optional(),
        }
    ).named(renames["AptSettingsIn"])
    types["AptSettingsOut"] = t.struct(
        {
            "exclusivePackages": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "excludes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AptSettingsOut"])
    types["OSPolicyResourceFileGcsIn"] = t.struct(
        {
            "bucket": t.string(),
            "generation": t.string().optional(),
            "object": t.string(),
        }
    ).named(renames["OSPolicyResourceFileGcsIn"])
    types["OSPolicyResourceFileGcsOut"] = t.struct(
        {
            "bucket": t.string(),
            "generation": t.string().optional(),
            "object": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceFileGcsOut"])
    types["ExecStepIn"] = t.struct(
        {
            "windowsExecStepConfig": t.proxy(renames["ExecStepConfigIn"]).optional(),
            "linuxExecStepConfig": t.proxy(renames["ExecStepConfigIn"]).optional(),
        }
    ).named(renames["ExecStepIn"])
    types["ExecStepOut"] = t.struct(
        {
            "windowsExecStepConfig": t.proxy(renames["ExecStepConfigOut"]).optional(),
            "linuxExecStepConfig": t.proxy(renames["ExecStepConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecStepOut"])
    types["OSPolicyResourcePackageResourceYUMIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["OSPolicyResourcePackageResourceYUMIn"])
    types["OSPolicyResourcePackageResourceYUMOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OSPolicyResourcePackageResourceYUMOut"])
    types["OSPolicyAssignmentInstanceFilterInventoryIn"] = t.struct(
        {"osVersion": t.string().optional(), "osShortName": t.string()}
    ).named(renames["OSPolicyAssignmentInstanceFilterInventoryIn"])
    types["OSPolicyAssignmentInstanceFilterInventoryOut"] = t.struct(
        {
            "osVersion": t.string().optional(),
            "osShortName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentInstanceFilterInventoryOut"])
    types["GooSettingsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GooSettingsIn"]
    )
    types["GooSettingsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooSettingsOut"])
    types["InventoryWindowsQuickFixEngineeringPackageIn"] = t.struct(
        {
            "installTime": t.string().optional(),
            "hotFixId": t.string().optional(),
            "description": t.string().optional(),
            "caption": t.string().optional(),
        }
    ).named(renames["InventoryWindowsQuickFixEngineeringPackageIn"])
    types["InventoryWindowsQuickFixEngineeringPackageOut"] = t.struct(
        {
            "installTime": t.string().optional(),
            "hotFixId": t.string().optional(),
            "description": t.string().optional(),
            "caption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryWindowsQuickFixEngineeringPackageOut"])
    types["PatchJobIn"] = t.struct(
        {
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
            "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]).optional(),
            "errorMessage": t.string().optional(),
            "description": t.string().optional(),
            "instanceDetailsSummary": t.proxy(
                renames["PatchJobInstanceDetailsSummaryIn"]
            ).optional(),
            "percentComplete": t.number().optional(),
            "updateTime": t.string().optional(),
            "duration": t.string().optional(),
            "name": t.string().optional(),
            "dryRun": t.boolean().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["PatchJobIn"])
    types["PatchJobOut"] = t.struct(
        {
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "patchConfig": t.proxy(renames["PatchConfigOut"]).optional(),
            "rollout": t.proxy(renames["PatchRolloutOut"]).optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterOut"]).optional(),
            "errorMessage": t.string().optional(),
            "description": t.string().optional(),
            "instanceDetailsSummary": t.proxy(
                renames["PatchJobInstanceDetailsSummaryOut"]
            ).optional(),
            "percentComplete": t.number().optional(),
            "updateTime": t.string().optional(),
            "patchDeployment": t.string().optional(),
            "duration": t.string().optional(),
            "name": t.string().optional(),
            "dryRun": t.boolean().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchJobOut"])
    types["InventoryWindowsUpdatePackageIn"] = t.struct(
        {
            "kbArticleIds": t.array(t.string()).optional(),
            "revisionNumber": t.integer().optional(),
            "moreInfoUrls": t.array(t.string()).optional(),
            "updateId": t.string().optional(),
            "categories": t.array(
                t.proxy(renames["InventoryWindowsUpdatePackageWindowsUpdateCategoryIn"])
            ).optional(),
            "title": t.string().optional(),
            "lastDeploymentChangeTime": t.string().optional(),
            "description": t.string().optional(),
            "supportUrl": t.string().optional(),
        }
    ).named(renames["InventoryWindowsUpdatePackageIn"])
    types["InventoryWindowsUpdatePackageOut"] = t.struct(
        {
            "kbArticleIds": t.array(t.string()).optional(),
            "revisionNumber": t.integer().optional(),
            "moreInfoUrls": t.array(t.string()).optional(),
            "updateId": t.string().optional(),
            "categories": t.array(
                t.proxy(
                    renames["InventoryWindowsUpdatePackageWindowsUpdateCategoryOut"]
                )
            ).optional(),
            "title": t.string().optional(),
            "lastDeploymentChangeTime": t.string().optional(),
            "description": t.string().optional(),
            "supportUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryWindowsUpdatePackageOut"])
    types["ExecStepConfigIn"] = t.struct(
        {
            "gcsObject": t.proxy(renames["GcsObjectIn"]).optional(),
            "interpreter": t.string().optional(),
            "localPath": t.string().optional(),
            "allowedSuccessCodes": t.array(t.integer()).optional(),
        }
    ).named(renames["ExecStepConfigIn"])
    types["ExecStepConfigOut"] = t.struct(
        {
            "gcsObject": t.proxy(renames["GcsObjectOut"]).optional(),
            "interpreter": t.string().optional(),
            "localPath": t.string().optional(),
            "allowedSuccessCodes": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecStepConfigOut"])
    types["CVSSv3In"] = t.struct(
        {
            "attackVector": t.string().optional(),
            "confidentialityImpact": t.string().optional(),
            "scope": t.string().optional(),
            "integrityImpact": t.string().optional(),
            "privilegesRequired": t.string().optional(),
            "impactScore": t.number().optional(),
            "baseScore": t.number().optional(),
            "attackComplexity": t.string().optional(),
            "availabilityImpact": t.string().optional(),
            "userInteraction": t.string().optional(),
            "exploitabilityScore": t.number().optional(),
        }
    ).named(renames["CVSSv3In"])
    types["CVSSv3Out"] = t.struct(
        {
            "attackVector": t.string().optional(),
            "confidentialityImpact": t.string().optional(),
            "scope": t.string().optional(),
            "integrityImpact": t.string().optional(),
            "privilegesRequired": t.string().optional(),
            "impactScore": t.number().optional(),
            "baseScore": t.number().optional(),
            "attackComplexity": t.string().optional(),
            "availabilityImpact": t.string().optional(),
            "userInteraction": t.string().optional(),
            "exploitabilityScore": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CVSSv3Out"])
    types["PatchJobInstanceDetailsSummaryIn"] = t.struct(
        {
            "notifiedInstanceCount": t.string().optional(),
            "noAgentDetectedInstanceCount": t.string().optional(),
            "postPatchStepInstanceCount": t.string().optional(),
            "timedOutInstanceCount": t.string().optional(),
            "applyingPatchesInstanceCount": t.string().optional(),
            "rebootingInstanceCount": t.string().optional(),
            "succeededRebootRequiredInstanceCount": t.string().optional(),
            "downloadingPatchesInstanceCount": t.string().optional(),
            "failedInstanceCount": t.string().optional(),
            "startedInstanceCount": t.string().optional(),
            "inactiveInstanceCount": t.string().optional(),
            "ackedInstanceCount": t.string().optional(),
            "pendingInstanceCount": t.string().optional(),
            "prePatchStepInstanceCount": t.string().optional(),
            "succeededInstanceCount": t.string().optional(),
        }
    ).named(renames["PatchJobInstanceDetailsSummaryIn"])
    types["PatchJobInstanceDetailsSummaryOut"] = t.struct(
        {
            "notifiedInstanceCount": t.string().optional(),
            "noAgentDetectedInstanceCount": t.string().optional(),
            "postPatchStepInstanceCount": t.string().optional(),
            "timedOutInstanceCount": t.string().optional(),
            "applyingPatchesInstanceCount": t.string().optional(),
            "rebootingInstanceCount": t.string().optional(),
            "succeededRebootRequiredInstanceCount": t.string().optional(),
            "downloadingPatchesInstanceCount": t.string().optional(),
            "failedInstanceCount": t.string().optional(),
            "startedInstanceCount": t.string().optional(),
            "inactiveInstanceCount": t.string().optional(),
            "ackedInstanceCount": t.string().optional(),
            "pendingInstanceCount": t.string().optional(),
            "prePatchStepInstanceCount": t.string().optional(),
            "succeededInstanceCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchJobInstanceDetailsSummaryOut"])
    types["ExecutePatchJobRequestIn"] = t.struct(
        {
            "dryRun": t.boolean().optional(),
            "displayName": t.string().optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
            "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
            "description": t.string().optional(),
            "duration": t.string().optional(),
            "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
        }
    ).named(renames["ExecutePatchJobRequestIn"])
    types["ExecutePatchJobRequestOut"] = t.struct(
        {
            "dryRun": t.boolean().optional(),
            "displayName": t.string().optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterOut"]),
            "patchConfig": t.proxy(renames["PatchConfigOut"]).optional(),
            "description": t.string().optional(),
            "duration": t.string().optional(),
            "rollout": t.proxy(renames["PatchRolloutOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutePatchJobRequestOut"])
    types["InventoryItemIn"] = t.struct(
        {
            "originType": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "installedPackage": t.proxy(
                renames["InventorySoftwarePackageIn"]
            ).optional(),
            "availablePackage": t.proxy(
                renames["InventorySoftwarePackageIn"]
            ).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["InventoryItemIn"])
    types["InventoryItemOut"] = t.struct(
        {
            "originType": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "installedPackage": t.proxy(
                renames["InventorySoftwarePackageOut"]
            ).optional(),
            "availablePackage": t.proxy(
                renames["InventorySoftwarePackageOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryItemOut"])
    types["OSPolicyResourcePackageResourceGooGetIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["OSPolicyResourcePackageResourceGooGetIn"])
    types["OSPolicyResourcePackageResourceGooGetOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OSPolicyResourcePackageResourceGooGetOut"])
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

    functions = {}
    functions["projectsPatchJobsCancel"] = osconfig.get(
        "v1/{parent}/patchJobs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPatchJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchJobsGet"] = osconfig.get(
        "v1/{parent}/patchJobs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPatchJobInstanceDetailsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsPatch"] = osconfig.post(
        "v1/{parent}/patchDeployments",
        t.struct(
            {
                "patchDeploymentId": t.string(),
                "parent": t.string(),
                "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
                "oneTimeSchedule": t.proxy(renames["OneTimeScheduleIn"]),
                "name": t.string().optional(),
                "duration": t.string().optional(),
                "description": t.string().optional(),
                "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
                "recurringSchedule": t.proxy(renames["RecurringScheduleIn"]),
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
                "patchDeploymentId": t.string(),
                "parent": t.string(),
                "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
                "oneTimeSchedule": t.proxy(renames["OneTimeScheduleIn"]),
                "name": t.string().optional(),
                "duration": t.string().optional(),
                "description": t.string().optional(),
                "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
                "recurringSchedule": t.proxy(renames["RecurringScheduleIn"]),
                "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsResume"] = osconfig.post(
        "v1/{parent}/patchDeployments",
        t.struct(
            {
                "patchDeploymentId": t.string(),
                "parent": t.string(),
                "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
                "oneTimeSchedule": t.proxy(renames["OneTimeScheduleIn"]),
                "name": t.string().optional(),
                "duration": t.string().optional(),
                "description": t.string().optional(),
                "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
                "recurringSchedule": t.proxy(renames["RecurringScheduleIn"]),
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
                "patchDeploymentId": t.string(),
                "parent": t.string(),
                "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
                "oneTimeSchedule": t.proxy(renames["OneTimeScheduleIn"]),
                "name": t.string().optional(),
                "duration": t.string().optional(),
                "description": t.string().optional(),
                "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
                "recurringSchedule": t.proxy(renames["RecurringScheduleIn"]),
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
                "patchDeploymentId": t.string(),
                "parent": t.string(),
                "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
                "oneTimeSchedule": t.proxy(renames["OneTimeScheduleIn"]),
                "name": t.string().optional(),
                "duration": t.string().optional(),
                "description": t.string().optional(),
                "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
                "recurringSchedule": t.proxy(renames["RecurringScheduleIn"]),
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
                "patchDeploymentId": t.string(),
                "parent": t.string(),
                "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
                "oneTimeSchedule": t.proxy(renames["OneTimeScheduleIn"]),
                "name": t.string().optional(),
                "duration": t.string().optional(),
                "description": t.string().optional(),
                "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
                "recurringSchedule": t.proxy(renames["RecurringScheduleIn"]),
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
                "patchDeploymentId": t.string(),
                "parent": t.string(),
                "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
                "oneTimeSchedule": t.proxy(renames["OneTimeScheduleIn"]),
                "name": t.string().optional(),
                "duration": t.string().optional(),
                "description": t.string().optional(),
                "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
                "recurringSchedule": t.proxy(renames["RecurringScheduleIn"]),
                "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsListRevisions"] = osconfig.get(
        "v1/{parent}/osPolicyAssignments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOSPolicyAssignmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsCreate"] = osconfig.get(
        "v1/{parent}/osPolicyAssignments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOSPolicyAssignmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsDelete"] = osconfig.get(
        "v1/{parent}/osPolicyAssignments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOSPolicyAssignmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsPatch"] = osconfig.get(
        "v1/{parent}/osPolicyAssignments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOSPolicyAssignmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsGet"] = osconfig.get(
        "v1/{parent}/osPolicyAssignments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOSPolicyAssignmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsList"] = osconfig.get(
        "v1/{parent}/osPolicyAssignments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOSPolicyAssignmentsResponseOut"]),
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
    functions["projectsLocationsInstancesVulnerabilityReportsList"] = osconfig.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VulnerabilityReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesVulnerabilityReportsGet"] = osconfig.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VulnerabilityReportOut"]),
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
    functions["projectsLocationsInstancesOsPolicyAssignmentsReportsGet"] = osconfig.get(
        "v1/{parent}/reports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOSPolicyAssignmentReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsInstancesOsPolicyAssignmentsReportsList"
    ] = osconfig.get(
        "v1/{parent}/reports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOSPolicyAssignmentReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="osconfig", renames=renames, types=Box(types), functions=Box(functions)
    )
