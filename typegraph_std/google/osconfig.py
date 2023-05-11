from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_osconfig() -> Import:
    osconfig = HTTPRuntime("https://osconfig.googleapis.com/")

    renames = {
        "ErrorResponse": "_osconfig_1_ErrorResponse",
        "ExecStepConfigIn": "_osconfig_2_ExecStepConfigIn",
        "ExecStepConfigOut": "_osconfig_3_ExecStepConfigOut",
        "OneTimeScheduleIn": "_osconfig_4_OneTimeScheduleIn",
        "OneTimeScheduleOut": "_osconfig_5_OneTimeScheduleOut",
        "OSPolicyResourceGroupIn": "_osconfig_6_OSPolicyResourceGroupIn",
        "OSPolicyResourceGroupOut": "_osconfig_7_OSPolicyResourceGroupOut",
        "PausePatchDeploymentRequestIn": "_osconfig_8_PausePatchDeploymentRequestIn",
        "PausePatchDeploymentRequestOut": "_osconfig_9_PausePatchDeploymentRequestOut",
        "OSPolicyResourceFileRemoteIn": "_osconfig_10_OSPolicyResourceFileRemoteIn",
        "OSPolicyResourceFileRemoteOut": "_osconfig_11_OSPolicyResourceFileRemoteOut",
        "InventoryVersionedPackageIn": "_osconfig_12_InventoryVersionedPackageIn",
        "InventoryVersionedPackageOut": "_osconfig_13_InventoryVersionedPackageOut",
        "OSPolicyResourceIn": "_osconfig_14_OSPolicyResourceIn",
        "OSPolicyResourceOut": "_osconfig_15_OSPolicyResourceOut",
        "GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataIn": "_osconfig_16_GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataIn",
        "GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataOut": "_osconfig_17_GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataOut",
        "InventoryIn": "_osconfig_18_InventoryIn",
        "InventoryOut": "_osconfig_19_InventoryOut",
        "PatchJobInstanceDetailsIn": "_osconfig_20_PatchJobInstanceDetailsIn",
        "PatchJobInstanceDetailsOut": "_osconfig_21_PatchJobInstanceDetailsOut",
        "ListPatchJobsResponseIn": "_osconfig_22_ListPatchJobsResponseIn",
        "ListPatchJobsResponseOut": "_osconfig_23_ListPatchJobsResponseOut",
        "ResumePatchDeploymentRequestIn": "_osconfig_24_ResumePatchDeploymentRequestIn",
        "ResumePatchDeploymentRequestOut": "_osconfig_25_ResumePatchDeploymentRequestOut",
        "OSPolicyResourceRepositoryResourceZypperRepositoryIn": "_osconfig_26_OSPolicyResourceRepositoryResourceZypperRepositoryIn",
        "OSPolicyResourceRepositoryResourceZypperRepositoryOut": "_osconfig_27_OSPolicyResourceRepositoryResourceZypperRepositoryOut",
        "OSPolicyResourceExecResourceExecIn": "_osconfig_28_OSPolicyResourceExecResourceExecIn",
        "OSPolicyResourceExecResourceExecOut": "_osconfig_29_OSPolicyResourceExecResourceExecOut",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceIn": "_osconfig_30_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceIn",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOut": "_osconfig_31_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOut",
        "OSPolicyResourceRepositoryResourceGooRepositoryIn": "_osconfig_32_OSPolicyResourceRepositoryResourceGooRepositoryIn",
        "OSPolicyResourceRepositoryResourceGooRepositoryOut": "_osconfig_33_OSPolicyResourceRepositoryResourceGooRepositoryOut",
        "PatchConfigIn": "_osconfig_34_PatchConfigIn",
        "PatchConfigOut": "_osconfig_35_PatchConfigOut",
        "CancelPatchJobRequestIn": "_osconfig_36_CancelPatchJobRequestIn",
        "CancelPatchJobRequestOut": "_osconfig_37_CancelPatchJobRequestOut",
        "PatchJobIn": "_osconfig_38_PatchJobIn",
        "PatchJobOut": "_osconfig_39_PatchJobOut",
        "ListInventoriesResponseIn": "_osconfig_40_ListInventoriesResponseIn",
        "ListInventoriesResponseOut": "_osconfig_41_ListInventoriesResponseOut",
        "OSPolicyResourcePackageResourceYUMIn": "_osconfig_42_OSPolicyResourcePackageResourceYUMIn",
        "OSPolicyResourcePackageResourceYUMOut": "_osconfig_43_OSPolicyResourcePackageResourceYUMOut",
        "OSPolicyAssignmentLabelSetIn": "_osconfig_44_OSPolicyAssignmentLabelSetIn",
        "OSPolicyAssignmentLabelSetOut": "_osconfig_45_OSPolicyAssignmentLabelSetOut",
        "OSPolicyResourceRepositoryResourceYumRepositoryIn": "_osconfig_46_OSPolicyResourceRepositoryResourceYumRepositoryIn",
        "OSPolicyResourceRepositoryResourceYumRepositoryOut": "_osconfig_47_OSPolicyResourceRepositoryResourceYumRepositoryOut",
        "OSPolicyAssignmentInstanceFilterIn": "_osconfig_48_OSPolicyAssignmentInstanceFilterIn",
        "OSPolicyAssignmentInstanceFilterOut": "_osconfig_49_OSPolicyAssignmentInstanceFilterOut",
        "InventoryWindowsApplicationIn": "_osconfig_50_InventoryWindowsApplicationIn",
        "InventoryWindowsApplicationOut": "_osconfig_51_InventoryWindowsApplicationOut",
        "InventoryItemIn": "_osconfig_52_InventoryItemIn",
        "InventoryItemOut": "_osconfig_53_InventoryItemOut",
        "InventoryWindowsUpdatePackageWindowsUpdateCategoryIn": "_osconfig_54_InventoryWindowsUpdatePackageWindowsUpdateCategoryIn",
        "InventoryWindowsUpdatePackageWindowsUpdateCategoryOut": "_osconfig_55_InventoryWindowsUpdatePackageWindowsUpdateCategoryOut",
        "PatchRolloutIn": "_osconfig_56_PatchRolloutIn",
        "PatchRolloutOut": "_osconfig_57_PatchRolloutOut",
        "PatchJobInstanceDetailsSummaryIn": "_osconfig_58_PatchJobInstanceDetailsSummaryIn",
        "PatchJobInstanceDetailsSummaryOut": "_osconfig_59_PatchJobInstanceDetailsSummaryOut",
        "TimeZoneIn": "_osconfig_60_TimeZoneIn",
        "TimeZoneOut": "_osconfig_61_TimeZoneOut",
        "OSPolicyResourceFileIn": "_osconfig_62_OSPolicyResourceFileIn",
        "OSPolicyResourceFileOut": "_osconfig_63_OSPolicyResourceFileOut",
        "ListPatchDeploymentsResponseIn": "_osconfig_64_ListPatchDeploymentsResponseIn",
        "ListPatchDeploymentsResponseOut": "_osconfig_65_ListPatchDeploymentsResponseOut",
        "TimeOfDayIn": "_osconfig_66_TimeOfDayIn",
        "TimeOfDayOut": "_osconfig_67_TimeOfDayOut",
        "OSPolicyResourceExecResourceIn": "_osconfig_68_OSPolicyResourceExecResourceIn",
        "OSPolicyResourceExecResourceOut": "_osconfig_69_OSPolicyResourceExecResourceOut",
        "GcsObjectIn": "_osconfig_70_GcsObjectIn",
        "GcsObjectOut": "_osconfig_71_GcsObjectOut",
        "OSPolicyResourceRepositoryResourceIn": "_osconfig_72_OSPolicyResourceRepositoryResourceIn",
        "OSPolicyResourceRepositoryResourceOut": "_osconfig_73_OSPolicyResourceRepositoryResourceOut",
        "OSPolicyResourcePackageResourceGooGetIn": "_osconfig_74_OSPolicyResourcePackageResourceGooGetIn",
        "OSPolicyResourcePackageResourceGooGetOut": "_osconfig_75_OSPolicyResourcePackageResourceGooGetOut",
        "OSPolicyResourceRepositoryResourceAptRepositoryIn": "_osconfig_76_OSPolicyResourceRepositoryResourceAptRepositoryIn",
        "OSPolicyResourceRepositoryResourceAptRepositoryOut": "_osconfig_77_OSPolicyResourceRepositoryResourceAptRepositoryOut",
        "OSPolicyResourceFileGcsIn": "_osconfig_78_OSPolicyResourceFileGcsIn",
        "OSPolicyResourceFileGcsOut": "_osconfig_79_OSPolicyResourceFileGcsOut",
        "OSPolicyResourceFileResourceIn": "_osconfig_80_OSPolicyResourceFileResourceIn",
        "OSPolicyResourceFileResourceOut": "_osconfig_81_OSPolicyResourceFileResourceOut",
        "VulnerabilityReportVulnerabilityItemIn": "_osconfig_82_VulnerabilityReportVulnerabilityItemIn",
        "VulnerabilityReportVulnerabilityItemOut": "_osconfig_83_VulnerabilityReportVulnerabilityItemOut",
        "PatchDeploymentIn": "_osconfig_84_PatchDeploymentIn",
        "PatchDeploymentOut": "_osconfig_85_PatchDeploymentOut",
        "OSPolicyResourcePackageResourceMSIIn": "_osconfig_86_OSPolicyResourcePackageResourceMSIIn",
        "OSPolicyResourcePackageResourceMSIOut": "_osconfig_87_OSPolicyResourcePackageResourceMSIOut",
        "OSPolicyInventoryFilterIn": "_osconfig_88_OSPolicyInventoryFilterIn",
        "OSPolicyInventoryFilterOut": "_osconfig_89_OSPolicyInventoryFilterOut",
        "DateIn": "_osconfig_90_DateIn",
        "DateOut": "_osconfig_91_DateOut",
        "OSPolicyResourcePackageResourceRPMIn": "_osconfig_92_OSPolicyResourcePackageResourceRPMIn",
        "OSPolicyResourcePackageResourceRPMOut": "_osconfig_93_OSPolicyResourcePackageResourceRPMOut",
        "InventoryZypperPatchIn": "_osconfig_94_InventoryZypperPatchIn",
        "InventoryZypperPatchOut": "_osconfig_95_InventoryZypperPatchOut",
        "ZypperSettingsIn": "_osconfig_96_ZypperSettingsIn",
        "ZypperSettingsOut": "_osconfig_97_ZypperSettingsOut",
        "OSPolicyAssignmentInstanceFilterInventoryIn": "_osconfig_98_OSPolicyAssignmentInstanceFilterInventoryIn",
        "OSPolicyAssignmentInstanceFilterInventoryOut": "_osconfig_99_OSPolicyAssignmentInstanceFilterInventoryOut",
        "VulnerabilityReportIn": "_osconfig_100_VulnerabilityReportIn",
        "VulnerabilityReportOut": "_osconfig_101_VulnerabilityReportOut",
        "PatchInstanceFilterIn": "_osconfig_102_PatchInstanceFilterIn",
        "PatchInstanceFilterOut": "_osconfig_103_PatchInstanceFilterOut",
        "OSPolicyIn": "_osconfig_104_OSPolicyIn",
        "OSPolicyOut": "_osconfig_105_OSPolicyOut",
        "ListOSPolicyAssignmentRevisionsResponseIn": "_osconfig_106_ListOSPolicyAssignmentRevisionsResponseIn",
        "ListOSPolicyAssignmentRevisionsResponseOut": "_osconfig_107_ListOSPolicyAssignmentRevisionsResponseOut",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputIn": "_osconfig_108_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputIn",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputOut": "_osconfig_109_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputOut",
        "PatchInstanceFilterGroupLabelIn": "_osconfig_110_PatchInstanceFilterGroupLabelIn",
        "PatchInstanceFilterGroupLabelOut": "_osconfig_111_PatchInstanceFilterGroupLabelOut",
        "OSPolicyAssignmentOperationMetadataIn": "_osconfig_112_OSPolicyAssignmentOperationMetadataIn",
        "OSPolicyAssignmentOperationMetadataOut": "_osconfig_113_OSPolicyAssignmentOperationMetadataOut",
        "VulnerabilityReportVulnerabilityIn": "_osconfig_114_VulnerabilityReportVulnerabilityIn",
        "VulnerabilityReportVulnerabilityOut": "_osconfig_115_VulnerabilityReportVulnerabilityOut",
        "ListOSPolicyAssignmentsResponseIn": "_osconfig_116_ListOSPolicyAssignmentsResponseIn",
        "ListOSPolicyAssignmentsResponseOut": "_osconfig_117_ListOSPolicyAssignmentsResponseOut",
        "OSPolicyResourcePackageResourceIn": "_osconfig_118_OSPolicyResourcePackageResourceIn",
        "OSPolicyResourcePackageResourceOut": "_osconfig_119_OSPolicyResourcePackageResourceOut",
        "WindowsUpdateSettingsIn": "_osconfig_120_WindowsUpdateSettingsIn",
        "WindowsUpdateSettingsOut": "_osconfig_121_WindowsUpdateSettingsOut",
        "InventoryWindowsQuickFixEngineeringPackageIn": "_osconfig_122_InventoryWindowsQuickFixEngineeringPackageIn",
        "InventoryWindowsQuickFixEngineeringPackageOut": "_osconfig_123_InventoryWindowsQuickFixEngineeringPackageOut",
        "ExecStepIn": "_osconfig_124_ExecStepIn",
        "ExecStepOut": "_osconfig_125_ExecStepOut",
        "MonthlyScheduleIn": "_osconfig_126_MonthlyScheduleIn",
        "MonthlyScheduleOut": "_osconfig_127_MonthlyScheduleOut",
        "ListOSPolicyAssignmentReportsResponseIn": "_osconfig_128_ListOSPolicyAssignmentReportsResponseIn",
        "ListOSPolicyAssignmentReportsResponseOut": "_osconfig_129_ListOSPolicyAssignmentReportsResponseOut",
        "InventoryWindowsUpdatePackageIn": "_osconfig_130_InventoryWindowsUpdatePackageIn",
        "InventoryWindowsUpdatePackageOut": "_osconfig_131_InventoryWindowsUpdatePackageOut",
        "VulnerabilityReportVulnerabilityDetailsIn": "_osconfig_132_VulnerabilityReportVulnerabilityDetailsIn",
        "VulnerabilityReportVulnerabilityDetailsOut": "_osconfig_133_VulnerabilityReportVulnerabilityDetailsOut",
        "OSPolicyResourcePackageResourceZypperIn": "_osconfig_134_OSPolicyResourcePackageResourceZypperIn",
        "OSPolicyResourcePackageResourceZypperOut": "_osconfig_135_OSPolicyResourcePackageResourceZypperOut",
        "StatusIn": "_osconfig_136_StatusIn",
        "StatusOut": "_osconfig_137_StatusOut",
        "ListVulnerabilityReportsResponseIn": "_osconfig_138_ListVulnerabilityReportsResponseIn",
        "ListVulnerabilityReportsResponseOut": "_osconfig_139_ListVulnerabilityReportsResponseOut",
        "OSPolicyResourcePackageResourceDebIn": "_osconfig_140_OSPolicyResourcePackageResourceDebIn",
        "OSPolicyResourcePackageResourceDebOut": "_osconfig_141_OSPolicyResourcePackageResourceDebOut",
        "AptSettingsIn": "_osconfig_142_AptSettingsIn",
        "AptSettingsOut": "_osconfig_143_AptSettingsOut",
        "OSPolicyAssignmentReportIn": "_osconfig_144_OSPolicyAssignmentReportIn",
        "OSPolicyAssignmentReportOut": "_osconfig_145_OSPolicyAssignmentReportOut",
        "OSPolicyAssignmentRolloutIn": "_osconfig_146_OSPolicyAssignmentRolloutIn",
        "OSPolicyAssignmentRolloutOut": "_osconfig_147_OSPolicyAssignmentRolloutOut",
        "InventoryOsInfoIn": "_osconfig_148_InventoryOsInfoIn",
        "InventoryOsInfoOut": "_osconfig_149_InventoryOsInfoOut",
        "CancelOperationRequestIn": "_osconfig_150_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_osconfig_151_CancelOperationRequestOut",
        "VulnerabilityReportVulnerabilityDetailsReferenceIn": "_osconfig_152_VulnerabilityReportVulnerabilityDetailsReferenceIn",
        "VulnerabilityReportVulnerabilityDetailsReferenceOut": "_osconfig_153_VulnerabilityReportVulnerabilityDetailsReferenceOut",
        "RecurringScheduleIn": "_osconfig_154_RecurringScheduleIn",
        "RecurringScheduleOut": "_osconfig_155_RecurringScheduleOut",
        "WeekDayOfMonthIn": "_osconfig_156_WeekDayOfMonthIn",
        "WeekDayOfMonthOut": "_osconfig_157_WeekDayOfMonthOut",
        "OperationIn": "_osconfig_158_OperationIn",
        "OperationOut": "_osconfig_159_OperationOut",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepIn": "_osconfig_160_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepIn",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepOut": "_osconfig_161_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepOut",
        "OSPolicyAssignmentIn": "_osconfig_162_OSPolicyAssignmentIn",
        "OSPolicyAssignmentOut": "_osconfig_163_OSPolicyAssignmentOut",
        "OSPolicyResourcePackageResourceAPTIn": "_osconfig_164_OSPolicyResourcePackageResourceAPTIn",
        "OSPolicyResourcePackageResourceAPTOut": "_osconfig_165_OSPolicyResourcePackageResourceAPTOut",
        "GooSettingsIn": "_osconfig_166_GooSettingsIn",
        "GooSettingsOut": "_osconfig_167_GooSettingsOut",
        "ListPatchJobInstanceDetailsResponseIn": "_osconfig_168_ListPatchJobInstanceDetailsResponseIn",
        "ListPatchJobInstanceDetailsResponseOut": "_osconfig_169_ListPatchJobInstanceDetailsResponseOut",
        "EmptyIn": "_osconfig_170_EmptyIn",
        "EmptyOut": "_osconfig_171_EmptyOut",
        "OSPolicyAssignmentReportOSPolicyComplianceIn": "_osconfig_172_OSPolicyAssignmentReportOSPolicyComplianceIn",
        "OSPolicyAssignmentReportOSPolicyComplianceOut": "_osconfig_173_OSPolicyAssignmentReportOSPolicyComplianceOut",
        "CVSSv3In": "_osconfig_174_CVSSv3In",
        "CVSSv3Out": "_osconfig_175_CVSSv3Out",
        "ExecutePatchJobRequestIn": "_osconfig_176_ExecutePatchJobRequestIn",
        "ExecutePatchJobRequestOut": "_osconfig_177_ExecutePatchJobRequestOut",
        "YumSettingsIn": "_osconfig_178_YumSettingsIn",
        "YumSettingsOut": "_osconfig_179_YumSettingsOut",
        "WeeklyScheduleIn": "_osconfig_180_WeeklyScheduleIn",
        "WeeklyScheduleOut": "_osconfig_181_WeeklyScheduleOut",
        "InventorySoftwarePackageIn": "_osconfig_182_InventorySoftwarePackageIn",
        "InventorySoftwarePackageOut": "_osconfig_183_InventorySoftwarePackageOut",
        "FixedOrPercentIn": "_osconfig_184_FixedOrPercentIn",
        "FixedOrPercentOut": "_osconfig_185_FixedOrPercentOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ExecStepConfigIn"] = t.struct(
        {
            "allowedSuccessCodes": t.array(t.integer()).optional(),
            "interpreter": t.string().optional(),
            "gcsObject": t.proxy(renames["GcsObjectIn"]).optional(),
            "localPath": t.string().optional(),
        }
    ).named(renames["ExecStepConfigIn"])
    types["ExecStepConfigOut"] = t.struct(
        {
            "allowedSuccessCodes": t.array(t.integer()).optional(),
            "interpreter": t.string().optional(),
            "gcsObject": t.proxy(renames["GcsObjectOut"]).optional(),
            "localPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecStepConfigOut"])
    types["OneTimeScheduleIn"] = t.struct({"executeTime": t.string()}).named(
        renames["OneTimeScheduleIn"]
    )
    types["OneTimeScheduleOut"] = t.struct(
        {
            "executeTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OneTimeScheduleOut"])
    types["OSPolicyResourceGroupIn"] = t.struct(
        {
            "inventoryFilters": t.array(
                t.proxy(renames["OSPolicyInventoryFilterIn"])
            ).optional(),
            "resources": t.array(t.proxy(renames["OSPolicyResourceIn"])),
        }
    ).named(renames["OSPolicyResourceGroupIn"])
    types["OSPolicyResourceGroupOut"] = t.struct(
        {
            "inventoryFilters": t.array(
                t.proxy(renames["OSPolicyInventoryFilterOut"])
            ).optional(),
            "resources": t.array(t.proxy(renames["OSPolicyResourceOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceGroupOut"])
    types["PausePatchDeploymentRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["PausePatchDeploymentRequestIn"])
    types["PausePatchDeploymentRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PausePatchDeploymentRequestOut"])
    types["OSPolicyResourceFileRemoteIn"] = t.struct(
        {"sha256Checksum": t.string().optional(), "uri": t.string()}
    ).named(renames["OSPolicyResourceFileRemoteIn"])
    types["OSPolicyResourceFileRemoteOut"] = t.struct(
        {
            "sha256Checksum": t.string().optional(),
            "uri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceFileRemoteOut"])
    types["InventoryVersionedPackageIn"] = t.struct(
        {
            "version": t.string().optional(),
            "architecture": t.string().optional(),
            "packageName": t.string().optional(),
        }
    ).named(renames["InventoryVersionedPackageIn"])
    types["InventoryVersionedPackageOut"] = t.struct(
        {
            "version": t.string().optional(),
            "architecture": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryVersionedPackageOut"])
    types["OSPolicyResourceIn"] = t.struct(
        {
            "pkg": t.proxy(renames["OSPolicyResourcePackageResourceIn"]).optional(),
            "exec": t.proxy(renames["OSPolicyResourceExecResourceIn"]).optional(),
            "repository": t.proxy(
                renames["OSPolicyResourceRepositoryResourceIn"]
            ).optional(),
            "id": t.string(),
            "file": t.proxy(renames["OSPolicyResourceFileResourceIn"]).optional(),
        }
    ).named(renames["OSPolicyResourceIn"])
    types["OSPolicyResourceOut"] = t.struct(
        {
            "pkg": t.proxy(renames["OSPolicyResourcePackageResourceOut"]).optional(),
            "exec": t.proxy(renames["OSPolicyResourceExecResourceOut"]).optional(),
            "repository": t.proxy(
                renames["OSPolicyResourceRepositoryResourceOut"]
            ).optional(),
            "id": t.string(),
            "file": t.proxy(renames["OSPolicyResourceFileResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceOut"])
    types["GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataIn"] = t.struct(
        {
            "osPolicyAssignment": t.string().optional(),
            "rolloutStartTime": t.string().optional(),
            "rolloutState": t.string().optional(),
            "rolloutUpdateTime": t.string().optional(),
            "apiMethod": t.string().optional(),
        }
    ).named(renames["GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataIn"])
    types["GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataOut"] = t.struct(
        {
            "osPolicyAssignment": t.string().optional(),
            "rolloutStartTime": t.string().optional(),
            "rolloutState": t.string().optional(),
            "rolloutUpdateTime": t.string().optional(),
            "apiMethod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataOut"])
    types["InventoryIn"] = t.struct(
        {
            "items": t.struct({"_": t.string().optional()}).optional(),
            "osInfo": t.proxy(renames["InventoryOsInfoIn"]).optional(),
        }
    ).named(renames["InventoryIn"])
    types["InventoryOut"] = t.struct(
        {
            "items": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "osInfo": t.proxy(renames["InventoryOsInfoOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryOut"])
    types["PatchJobInstanceDetailsIn"] = t.struct(
        {
            "instanceSystemId": t.string().optional(),
            "failureReason": t.string().optional(),
            "attemptCount": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["PatchJobInstanceDetailsIn"])
    types["PatchJobInstanceDetailsOut"] = t.struct(
        {
            "instanceSystemId": t.string().optional(),
            "failureReason": t.string().optional(),
            "attemptCount": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchJobInstanceDetailsOut"])
    types["ListPatchJobsResponseIn"] = t.struct(
        {
            "patchJobs": t.array(t.proxy(renames["PatchJobIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPatchJobsResponseIn"])
    types["ListPatchJobsResponseOut"] = t.struct(
        {
            "patchJobs": t.array(t.proxy(renames["PatchJobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPatchJobsResponseOut"])
    types["ResumePatchDeploymentRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResumePatchDeploymentRequestIn"])
    types["ResumePatchDeploymentRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumePatchDeploymentRequestOut"])
    types["OSPolicyResourceRepositoryResourceZypperRepositoryIn"] = t.struct(
        {
            "id": t.string(),
            "baseUrl": t.string(),
            "gpgKeys": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceZypperRepositoryIn"])
    types["OSPolicyResourceRepositoryResourceZypperRepositoryOut"] = t.struct(
        {
            "id": t.string(),
            "baseUrl": t.string(),
            "gpgKeys": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceZypperRepositoryOut"])
    types["OSPolicyResourceExecResourceExecIn"] = t.struct(
        {
            "outputFilePath": t.string().optional(),
            "script": t.string().optional(),
            "interpreter": t.string(),
            "args": t.array(t.string()).optional(),
            "file": t.proxy(renames["OSPolicyResourceFileIn"]).optional(),
        }
    ).named(renames["OSPolicyResourceExecResourceExecIn"])
    types["OSPolicyResourceExecResourceExecOut"] = t.struct(
        {
            "outputFilePath": t.string().optional(),
            "script": t.string().optional(),
            "interpreter": t.string(),
            "args": t.array(t.string()).optional(),
            "file": t.proxy(renames["OSPolicyResourceFileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceExecResourceExecOut"])
    types[
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceIn"
    ] = t.struct(
        {
            "complianceStateReason": t.string().optional(),
            "osPolicyResourceId": t.string().optional(),
            "execResourceOutput": t.proxy(
                renames[
                    "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputIn"
                ]
            ).optional(),
            "configSteps": t.array(
                t.proxy(
                    renames[
                        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepIn"
                    ]
                )
            ).optional(),
            "complianceState": t.string().optional(),
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
            "complianceStateReason": t.string().optional(),
            "osPolicyResourceId": t.string().optional(),
            "execResourceOutput": t.proxy(
                renames[
                    "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputOut"
                ]
            ).optional(),
            "configSteps": t.array(
                t.proxy(
                    renames[
                        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepOut"
                    ]
                )
            ).optional(),
            "complianceState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOut"
        ]
    )
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
    types["PatchConfigIn"] = t.struct(
        {
            "goo": t.proxy(renames["GooSettingsIn"]).optional(),
            "preStep": t.proxy(renames["ExecStepIn"]).optional(),
            "postStep": t.proxy(renames["ExecStepIn"]).optional(),
            "migInstancesAllowed": t.boolean().optional(),
            "rebootConfig": t.string().optional(),
            "apt": t.proxy(renames["AptSettingsIn"]).optional(),
            "windowsUpdate": t.proxy(renames["WindowsUpdateSettingsIn"]).optional(),
            "zypper": t.proxy(renames["ZypperSettingsIn"]).optional(),
            "yum": t.proxy(renames["YumSettingsIn"]).optional(),
        }
    ).named(renames["PatchConfigIn"])
    types["PatchConfigOut"] = t.struct(
        {
            "goo": t.proxy(renames["GooSettingsOut"]).optional(),
            "preStep": t.proxy(renames["ExecStepOut"]).optional(),
            "postStep": t.proxy(renames["ExecStepOut"]).optional(),
            "migInstancesAllowed": t.boolean().optional(),
            "rebootConfig": t.string().optional(),
            "apt": t.proxy(renames["AptSettingsOut"]).optional(),
            "windowsUpdate": t.proxy(renames["WindowsUpdateSettingsOut"]).optional(),
            "zypper": t.proxy(renames["ZypperSettingsOut"]).optional(),
            "yum": t.proxy(renames["YumSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchConfigOut"])
    types["CancelPatchJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelPatchJobRequestIn"]
    )
    types["CancelPatchJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelPatchJobRequestOut"])
    types["PatchJobIn"] = t.struct(
        {
            "instanceDetailsSummary": t.proxy(
                renames["PatchJobInstanceDetailsSummaryIn"]
            ).optional(),
            "createTime": t.string().optional(),
            "errorMessage": t.string().optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]).optional(),
            "percentComplete": t.number().optional(),
            "description": t.string().optional(),
            "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
            "duration": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
            "dryRun": t.boolean().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["PatchJobIn"])
    types["PatchJobOut"] = t.struct(
        {
            "instanceDetailsSummary": t.proxy(
                renames["PatchJobInstanceDetailsSummaryOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "errorMessage": t.string().optional(),
            "patchDeployment": t.string().optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterOut"]).optional(),
            "percentComplete": t.number().optional(),
            "description": t.string().optional(),
            "patchConfig": t.proxy(renames["PatchConfigOut"]).optional(),
            "duration": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "rollout": t.proxy(renames["PatchRolloutOut"]).optional(),
            "dryRun": t.boolean().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchJobOut"])
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
    types["OSPolicyResourcePackageResourceYUMIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["OSPolicyResourcePackageResourceYUMIn"])
    types["OSPolicyResourcePackageResourceYUMOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OSPolicyResourcePackageResourceYUMOut"])
    types["OSPolicyAssignmentLabelSetIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["OSPolicyAssignmentLabelSetIn"])
    types["OSPolicyAssignmentLabelSetOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentLabelSetOut"])
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
    types["OSPolicyAssignmentInstanceFilterIn"] = t.struct(
        {
            "inclusionLabels": t.array(
                t.proxy(renames["OSPolicyAssignmentLabelSetIn"])
            ).optional(),
            "exclusionLabels": t.array(
                t.proxy(renames["OSPolicyAssignmentLabelSetIn"])
            ).optional(),
            "inventories": t.array(
                t.proxy(renames["OSPolicyAssignmentInstanceFilterInventoryIn"])
            ).optional(),
            "all": t.boolean().optional(),
        }
    ).named(renames["OSPolicyAssignmentInstanceFilterIn"])
    types["OSPolicyAssignmentInstanceFilterOut"] = t.struct(
        {
            "inclusionLabels": t.array(
                t.proxy(renames["OSPolicyAssignmentLabelSetOut"])
            ).optional(),
            "exclusionLabels": t.array(
                t.proxy(renames["OSPolicyAssignmentLabelSetOut"])
            ).optional(),
            "inventories": t.array(
                t.proxy(renames["OSPolicyAssignmentInstanceFilterInventoryOut"])
            ).optional(),
            "all": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentInstanceFilterOut"])
    types["InventoryWindowsApplicationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "displayVersion": t.string().optional(),
            "installDate": t.proxy(renames["DateIn"]).optional(),
            "publisher": t.string().optional(),
            "helpLink": t.string().optional(),
        }
    ).named(renames["InventoryWindowsApplicationIn"])
    types["InventoryWindowsApplicationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "displayVersion": t.string().optional(),
            "installDate": t.proxy(renames["DateOut"]).optional(),
            "publisher": t.string().optional(),
            "helpLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryWindowsApplicationOut"])
    types["InventoryItemIn"] = t.struct(
        {
            "availablePackage": t.proxy(
                renames["InventorySoftwarePackageIn"]
            ).optional(),
            "type": t.string().optional(),
            "createTime": t.string().optional(),
            "id": t.string().optional(),
            "originType": t.string().optional(),
            "installedPackage": t.proxy(
                renames["InventorySoftwarePackageIn"]
            ).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["InventoryItemIn"])
    types["InventoryItemOut"] = t.struct(
        {
            "availablePackage": t.proxy(
                renames["InventorySoftwarePackageOut"]
            ).optional(),
            "type": t.string().optional(),
            "createTime": t.string().optional(),
            "id": t.string().optional(),
            "originType": t.string().optional(),
            "installedPackage": t.proxy(
                renames["InventorySoftwarePackageOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryItemOut"])
    types["InventoryWindowsUpdatePackageWindowsUpdateCategoryIn"] = t.struct(
        {"id": t.string().optional(), "name": t.string().optional()}
    ).named(renames["InventoryWindowsUpdatePackageWindowsUpdateCategoryIn"])
    types["InventoryWindowsUpdatePackageWindowsUpdateCategoryOut"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryWindowsUpdatePackageWindowsUpdateCategoryOut"])
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
    types["PatchJobInstanceDetailsSummaryIn"] = t.struct(
        {
            "ackedInstanceCount": t.string().optional(),
            "succeededInstanceCount": t.string().optional(),
            "timedOutInstanceCount": t.string().optional(),
            "applyingPatchesInstanceCount": t.string().optional(),
            "postPatchStepInstanceCount": t.string().optional(),
            "prePatchStepInstanceCount": t.string().optional(),
            "inactiveInstanceCount": t.string().optional(),
            "startedInstanceCount": t.string().optional(),
            "succeededRebootRequiredInstanceCount": t.string().optional(),
            "noAgentDetectedInstanceCount": t.string().optional(),
            "rebootingInstanceCount": t.string().optional(),
            "notifiedInstanceCount": t.string().optional(),
            "failedInstanceCount": t.string().optional(),
            "pendingInstanceCount": t.string().optional(),
            "downloadingPatchesInstanceCount": t.string().optional(),
        }
    ).named(renames["PatchJobInstanceDetailsSummaryIn"])
    types["PatchJobInstanceDetailsSummaryOut"] = t.struct(
        {
            "ackedInstanceCount": t.string().optional(),
            "succeededInstanceCount": t.string().optional(),
            "timedOutInstanceCount": t.string().optional(),
            "applyingPatchesInstanceCount": t.string().optional(),
            "postPatchStepInstanceCount": t.string().optional(),
            "prePatchStepInstanceCount": t.string().optional(),
            "inactiveInstanceCount": t.string().optional(),
            "startedInstanceCount": t.string().optional(),
            "succeededRebootRequiredInstanceCount": t.string().optional(),
            "noAgentDetectedInstanceCount": t.string().optional(),
            "rebootingInstanceCount": t.string().optional(),
            "notifiedInstanceCount": t.string().optional(),
            "failedInstanceCount": t.string().optional(),
            "pendingInstanceCount": t.string().optional(),
            "downloadingPatchesInstanceCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchJobInstanceDetailsSummaryOut"])
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
    types["OSPolicyResourceFileIn"] = t.struct(
        {
            "remote": t.proxy(renames["OSPolicyResourceFileRemoteIn"]).optional(),
            "gcs": t.proxy(renames["OSPolicyResourceFileGcsIn"]).optional(),
            "localPath": t.string().optional(),
            "allowInsecure": t.boolean().optional(),
        }
    ).named(renames["OSPolicyResourceFileIn"])
    types["OSPolicyResourceFileOut"] = t.struct(
        {
            "remote": t.proxy(renames["OSPolicyResourceFileRemoteOut"]).optional(),
            "gcs": t.proxy(renames["OSPolicyResourceFileGcsOut"]).optional(),
            "localPath": t.string().optional(),
            "allowInsecure": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceFileOut"])
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
    types["TimeOfDayIn"] = t.struct(
        {
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
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
    types["OSPolicyResourcePackageResourceGooGetIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["OSPolicyResourcePackageResourceGooGetIn"])
    types["OSPolicyResourcePackageResourceGooGetOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OSPolicyResourcePackageResourceGooGetOut"])
    types["OSPolicyResourceRepositoryResourceAptRepositoryIn"] = t.struct(
        {
            "components": t.array(t.string()),
            "uri": t.string(),
            "gpgKey": t.string().optional(),
            "distribution": t.string(),
            "archiveType": t.string(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceAptRepositoryIn"])
    types["OSPolicyResourceRepositoryResourceAptRepositoryOut"] = t.struct(
        {
            "components": t.array(t.string()),
            "uri": t.string(),
            "gpgKey": t.string().optional(),
            "distribution": t.string(),
            "archiveType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceAptRepositoryOut"])
    types["OSPolicyResourceFileGcsIn"] = t.struct(
        {
            "object": t.string(),
            "generation": t.string().optional(),
            "bucket": t.string(),
        }
    ).named(renames["OSPolicyResourceFileGcsIn"])
    types["OSPolicyResourceFileGcsOut"] = t.struct(
        {
            "object": t.string(),
            "generation": t.string().optional(),
            "bucket": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceFileGcsOut"])
    types["OSPolicyResourceFileResourceIn"] = t.struct(
        {
            "path": t.string(),
            "state": t.string(),
            "permissions": t.string().optional(),
            "file": t.proxy(renames["OSPolicyResourceFileIn"]).optional(),
            "content": t.string().optional(),
        }
    ).named(renames["OSPolicyResourceFileResourceIn"])
    types["OSPolicyResourceFileResourceOut"] = t.struct(
        {
            "path": t.string(),
            "state": t.string(),
            "permissions": t.string().optional(),
            "file": t.proxy(renames["OSPolicyResourceFileOut"]).optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceFileResourceOut"])
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
    types["PatchDeploymentIn"] = t.struct(
        {
            "oneTimeSchedule": t.proxy(renames["OneTimeScheduleIn"]),
            "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
            "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
            "duration": t.string().optional(),
            "recurringSchedule": t.proxy(renames["RecurringScheduleIn"]),
            "description": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["PatchDeploymentIn"])
    types["PatchDeploymentOut"] = t.struct(
        {
            "oneTimeSchedule": t.proxy(renames["OneTimeScheduleOut"]),
            "lastExecuteTime": t.string().optional(),
            "patchConfig": t.proxy(renames["PatchConfigOut"]).optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterOut"]),
            "rollout": t.proxy(renames["PatchRolloutOut"]).optional(),
            "duration": t.string().optional(),
            "createTime": t.string().optional(),
            "recurringSchedule": t.proxy(renames["RecurringScheduleOut"]),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchDeploymentOut"])
    types["OSPolicyResourcePackageResourceMSIIn"] = t.struct(
        {
            "source": t.proxy(renames["OSPolicyResourceFileIn"]),
            "properties": t.array(t.string()).optional(),
        }
    ).named(renames["OSPolicyResourcePackageResourceMSIIn"])
    types["OSPolicyResourcePackageResourceMSIOut"] = t.struct(
        {
            "source": t.proxy(renames["OSPolicyResourceFileOut"]),
            "properties": t.array(t.string()).optional(),
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
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["OSPolicyResourcePackageResourceRPMIn"] = t.struct(
        {
            "pullDeps": t.boolean().optional(),
            "source": t.proxy(renames["OSPolicyResourceFileIn"]),
        }
    ).named(renames["OSPolicyResourcePackageResourceRPMIn"])
    types["OSPolicyResourcePackageResourceRPMOut"] = t.struct(
        {
            "pullDeps": t.boolean().optional(),
            "source": t.proxy(renames["OSPolicyResourceFileOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourcePackageResourceRPMOut"])
    types["InventoryZypperPatchIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "category": t.string().optional(),
            "patchName": t.string().optional(),
            "summary": t.string().optional(),
        }
    ).named(renames["InventoryZypperPatchIn"])
    types["InventoryZypperPatchOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "category": t.string().optional(),
            "patchName": t.string().optional(),
            "summary": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryZypperPatchOut"])
    types["ZypperSettingsIn"] = t.struct(
        {
            "categories": t.array(t.string()).optional(),
            "withOptional": t.boolean().optional(),
            "exclusivePatches": t.array(t.string()).optional(),
            "excludes": t.array(t.string()).optional(),
            "withUpdate": t.boolean().optional(),
            "severities": t.array(t.string()).optional(),
        }
    ).named(renames["ZypperSettingsIn"])
    types["ZypperSettingsOut"] = t.struct(
        {
            "categories": t.array(t.string()).optional(),
            "withOptional": t.boolean().optional(),
            "exclusivePatches": t.array(t.string()).optional(),
            "excludes": t.array(t.string()).optional(),
            "withUpdate": t.boolean().optional(),
            "severities": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZypperSettingsOut"])
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
    types["VulnerabilityReportIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VulnerabilityReportIn"]
    )
    types["VulnerabilityReportOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "vulnerabilities": t.array(
                t.proxy(renames["VulnerabilityReportVulnerabilityOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityReportOut"])
    types["PatchInstanceFilterIn"] = t.struct(
        {
            "groupLabels": t.array(
                t.proxy(renames["PatchInstanceFilterGroupLabelIn"])
            ).optional(),
            "instanceNamePrefixes": t.array(t.string()).optional(),
            "all": t.boolean().optional(),
            "instances": t.array(t.string()).optional(),
            "zones": t.array(t.string()).optional(),
        }
    ).named(renames["PatchInstanceFilterIn"])
    types["PatchInstanceFilterOut"] = t.struct(
        {
            "groupLabels": t.array(
                t.proxy(renames["PatchInstanceFilterGroupLabelOut"])
            ).optional(),
            "instanceNamePrefixes": t.array(t.string()).optional(),
            "all": t.boolean().optional(),
            "instances": t.array(t.string()).optional(),
            "zones": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchInstanceFilterOut"])
    types["OSPolicyIn"] = t.struct(
        {
            "mode": t.string(),
            "resourceGroups": t.array(t.proxy(renames["OSPolicyResourceGroupIn"])),
            "description": t.string().optional(),
            "id": t.string(),
            "allowNoResourceGroupMatch": t.boolean().optional(),
        }
    ).named(renames["OSPolicyIn"])
    types["OSPolicyOut"] = t.struct(
        {
            "mode": t.string(),
            "resourceGroups": t.array(t.proxy(renames["OSPolicyResourceGroupOut"])),
            "description": t.string().optional(),
            "id": t.string(),
            "allowNoResourceGroupMatch": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyOut"])
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
    types["PatchInstanceFilterGroupLabelIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["PatchInstanceFilterGroupLabelIn"])
    types["PatchInstanceFilterGroupLabelOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchInstanceFilterGroupLabelOut"])
    types["OSPolicyAssignmentOperationMetadataIn"] = t.struct(
        {
            "osPolicyAssignment": t.string().optional(),
            "rolloutStartTime": t.string().optional(),
            "apiMethod": t.string().optional(),
            "rolloutUpdateTime": t.string().optional(),
            "rolloutState": t.string().optional(),
        }
    ).named(renames["OSPolicyAssignmentOperationMetadataIn"])
    types["OSPolicyAssignmentOperationMetadataOut"] = t.struct(
        {
            "osPolicyAssignment": t.string().optional(),
            "rolloutStartTime": t.string().optional(),
            "apiMethod": t.string().optional(),
            "rolloutUpdateTime": t.string().optional(),
            "rolloutState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentOperationMetadataOut"])
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
    types["ListOSPolicyAssignmentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "osPolicyAssignments": t.array(
                t.proxy(renames["OSPolicyAssignmentIn"])
            ).optional(),
        }
    ).named(renames["ListOSPolicyAssignmentsResponseIn"])
    types["ListOSPolicyAssignmentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "osPolicyAssignments": t.array(
                t.proxy(renames["OSPolicyAssignmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOSPolicyAssignmentsResponseOut"])
    types["OSPolicyResourcePackageResourceIn"] = t.struct(
        {
            "deb": t.proxy(renames["OSPolicyResourcePackageResourceDebIn"]).optional(),
            "msi": t.proxy(renames["OSPolicyResourcePackageResourceMSIIn"]).optional(),
            "googet": t.proxy(
                renames["OSPolicyResourcePackageResourceGooGetIn"]
            ).optional(),
            "zypper": t.proxy(
                renames["OSPolicyResourcePackageResourceZypperIn"]
            ).optional(),
            "apt": t.proxy(renames["OSPolicyResourcePackageResourceAPTIn"]).optional(),
            "desiredState": t.string(),
            "yum": t.proxy(renames["OSPolicyResourcePackageResourceYUMIn"]).optional(),
            "rpm": t.proxy(renames["OSPolicyResourcePackageResourceRPMIn"]).optional(),
        }
    ).named(renames["OSPolicyResourcePackageResourceIn"])
    types["OSPolicyResourcePackageResourceOut"] = t.struct(
        {
            "deb": t.proxy(renames["OSPolicyResourcePackageResourceDebOut"]).optional(),
            "msi": t.proxy(renames["OSPolicyResourcePackageResourceMSIOut"]).optional(),
            "googet": t.proxy(
                renames["OSPolicyResourcePackageResourceGooGetOut"]
            ).optional(),
            "zypper": t.proxy(
                renames["OSPolicyResourcePackageResourceZypperOut"]
            ).optional(),
            "apt": t.proxy(renames["OSPolicyResourcePackageResourceAPTOut"]).optional(),
            "desiredState": t.string(),
            "yum": t.proxy(renames["OSPolicyResourcePackageResourceYUMOut"]).optional(),
            "rpm": t.proxy(renames["OSPolicyResourcePackageResourceRPMOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourcePackageResourceOut"])
    types["WindowsUpdateSettingsIn"] = t.struct(
        {
            "exclusivePatches": t.array(t.string()).optional(),
            "classifications": t.array(t.string()).optional(),
            "excludes": t.array(t.string()).optional(),
        }
    ).named(renames["WindowsUpdateSettingsIn"])
    types["WindowsUpdateSettingsOut"] = t.struct(
        {
            "exclusivePatches": t.array(t.string()).optional(),
            "classifications": t.array(t.string()).optional(),
            "excludes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsUpdateSettingsOut"])
    types["InventoryWindowsQuickFixEngineeringPackageIn"] = t.struct(
        {
            "description": t.string().optional(),
            "caption": t.string().optional(),
            "installTime": t.string().optional(),
            "hotFixId": t.string().optional(),
        }
    ).named(renames["InventoryWindowsQuickFixEngineeringPackageIn"])
    types["InventoryWindowsQuickFixEngineeringPackageOut"] = t.struct(
        {
            "description": t.string().optional(),
            "caption": t.string().optional(),
            "installTime": t.string().optional(),
            "hotFixId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryWindowsQuickFixEngineeringPackageOut"])
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
    types["InventoryWindowsUpdatePackageIn"] = t.struct(
        {
            "categories": t.array(
                t.proxy(renames["InventoryWindowsUpdatePackageWindowsUpdateCategoryIn"])
            ).optional(),
            "updateId": t.string().optional(),
            "lastDeploymentChangeTime": t.string().optional(),
            "description": t.string().optional(),
            "kbArticleIds": t.array(t.string()).optional(),
            "supportUrl": t.string().optional(),
            "revisionNumber": t.integer().optional(),
            "moreInfoUrls": t.array(t.string()).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["InventoryWindowsUpdatePackageIn"])
    types["InventoryWindowsUpdatePackageOut"] = t.struct(
        {
            "categories": t.array(
                t.proxy(
                    renames["InventoryWindowsUpdatePackageWindowsUpdateCategoryOut"]
                )
            ).optional(),
            "updateId": t.string().optional(),
            "lastDeploymentChangeTime": t.string().optional(),
            "description": t.string().optional(),
            "kbArticleIds": t.array(t.string()).optional(),
            "supportUrl": t.string().optional(),
            "revisionNumber": t.integer().optional(),
            "moreInfoUrls": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryWindowsUpdatePackageOut"])
    types["VulnerabilityReportVulnerabilityDetailsIn"] = t.struct(
        {
            "cvssV2Score": t.number().optional(),
            "cve": t.string().optional(),
            "severity": t.string().optional(),
            "description": t.string().optional(),
            "references": t.array(
                t.proxy(renames["VulnerabilityReportVulnerabilityDetailsReferenceIn"])
            ).optional(),
            "cvssV3": t.proxy(renames["CVSSv3In"]).optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityDetailsIn"])
    types["VulnerabilityReportVulnerabilityDetailsOut"] = t.struct(
        {
            "cvssV2Score": t.number().optional(),
            "cve": t.string().optional(),
            "severity": t.string().optional(),
            "description": t.string().optional(),
            "references": t.array(
                t.proxy(renames["VulnerabilityReportVulnerabilityDetailsReferenceOut"])
            ).optional(),
            "cvssV3": t.proxy(renames["CVSSv3Out"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityDetailsOut"])
    types["OSPolicyResourcePackageResourceZypperIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["OSPolicyResourcePackageResourceZypperIn"])
    types["OSPolicyResourcePackageResourceZypperOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OSPolicyResourcePackageResourceZypperOut"])
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
    types["OSPolicyAssignmentReportIn"] = t.struct(
        {
            "osPolicyCompliances": t.array(
                t.proxy(renames["OSPolicyAssignmentReportOSPolicyComplianceIn"])
            ).optional(),
            "lastRunId": t.string().optional(),
            "name": t.string().optional(),
            "osPolicyAssignment": t.string().optional(),
            "updateTime": t.string().optional(),
            "instance": t.string().optional(),
        }
    ).named(renames["OSPolicyAssignmentReportIn"])
    types["OSPolicyAssignmentReportOut"] = t.struct(
        {
            "osPolicyCompliances": t.array(
                t.proxy(renames["OSPolicyAssignmentReportOSPolicyComplianceOut"])
            ).optional(),
            "lastRunId": t.string().optional(),
            "name": t.string().optional(),
            "osPolicyAssignment": t.string().optional(),
            "updateTime": t.string().optional(),
            "instance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentReportOut"])
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
    types["InventoryOsInfoIn"] = t.struct(
        {
            "longName": t.string().optional(),
            "kernelRelease": t.string().optional(),
            "version": t.string().optional(),
            "architecture": t.string().optional(),
            "kernelVersion": t.string().optional(),
            "shortName": t.string().optional(),
            "osconfigAgentVersion": t.string().optional(),
            "hostname": t.string().optional(),
        }
    ).named(renames["InventoryOsInfoIn"])
    types["InventoryOsInfoOut"] = t.struct(
        {
            "longName": t.string().optional(),
            "kernelRelease": t.string().optional(),
            "version": t.string().optional(),
            "architecture": t.string().optional(),
            "kernelVersion": t.string().optional(),
            "shortName": t.string().optional(),
            "osconfigAgentVersion": t.string().optional(),
            "hostname": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryOsInfoOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["RecurringScheduleIn"] = t.struct(
        {
            "timeZone": t.proxy(renames["TimeZoneIn"]),
            "startTime": t.string().optional(),
            "monthly": t.proxy(renames["MonthlyScheduleIn"]),
            "weekly": t.proxy(renames["WeeklyScheduleIn"]),
            "frequency": t.string(),
            "timeOfDay": t.proxy(renames["TimeOfDayIn"]),
            "endTime": t.string().optional(),
        }
    ).named(renames["RecurringScheduleIn"])
    types["RecurringScheduleOut"] = t.struct(
        {
            "nextExecuteTime": t.string().optional(),
            "timeZone": t.proxy(renames["TimeZoneOut"]),
            "lastExecuteTime": t.string().optional(),
            "startTime": t.string().optional(),
            "monthly": t.proxy(renames["MonthlyScheduleOut"]),
            "weekly": t.proxy(renames["WeeklyScheduleOut"]),
            "frequency": t.string(),
            "timeOfDay": t.proxy(renames["TimeOfDayOut"]),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecurringScheduleOut"])
    types["WeekDayOfMonthIn"] = t.struct(
        {
            "dayOffset": t.integer().optional(),
            "weekOrdinal": t.integer(),
            "dayOfWeek": t.string(),
        }
    ).named(renames["WeekDayOfMonthIn"])
    types["WeekDayOfMonthOut"] = t.struct(
        {
            "dayOffset": t.integer().optional(),
            "weekOrdinal": t.integer(),
            "dayOfWeek": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeekDayOfMonthOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
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
            "name": t.string().optional(),
            "instanceFilter": t.proxy(renames["OSPolicyAssignmentInstanceFilterIn"]),
            "description": t.string().optional(),
            "rollout": t.proxy(renames["OSPolicyAssignmentRolloutIn"]),
            "etag": t.string().optional(),
            "osPolicies": t.array(t.proxy(renames["OSPolicyIn"])),
        }
    ).named(renames["OSPolicyAssignmentIn"])
    types["OSPolicyAssignmentOut"] = t.struct(
        {
            "name": t.string().optional(),
            "deleted": t.boolean().optional(),
            "reconciling": t.boolean().optional(),
            "revisionId": t.string().optional(),
            "instanceFilter": t.proxy(renames["OSPolicyAssignmentInstanceFilterOut"]),
            "description": t.string().optional(),
            "rollout": t.proxy(renames["OSPolicyAssignmentRolloutOut"]),
            "revisionCreateTime": t.string().optional(),
            "etag": t.string().optional(),
            "baseline": t.boolean().optional(),
            "rolloutState": t.string().optional(),
            "uid": t.string().optional(),
            "osPolicies": t.array(t.proxy(renames["OSPolicyOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentOut"])
    types["OSPolicyResourcePackageResourceAPTIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["OSPolicyResourcePackageResourceAPTIn"])
    types["OSPolicyResourcePackageResourceAPTOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OSPolicyResourcePackageResourceAPTOut"])
    types["GooSettingsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GooSettingsIn"]
    )
    types["GooSettingsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooSettingsOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["OSPolicyAssignmentReportOSPolicyComplianceIn"] = t.struct(
        {
            "complianceState": t.string().optional(),
            "complianceStateReason": t.string().optional(),
            "osPolicyId": t.string().optional(),
            "osPolicyResourceCompliances": t.array(
                t.proxy(
                    renames[
                        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["OSPolicyAssignmentReportOSPolicyComplianceIn"])
    types["OSPolicyAssignmentReportOSPolicyComplianceOut"] = t.struct(
        {
            "complianceState": t.string().optional(),
            "complianceStateReason": t.string().optional(),
            "osPolicyId": t.string().optional(),
            "osPolicyResourceCompliances": t.array(
                t.proxy(
                    renames[
                        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentReportOSPolicyComplianceOut"])
    types["CVSSv3In"] = t.struct(
        {
            "privilegesRequired": t.string().optional(),
            "baseScore": t.number().optional(),
            "userInteraction": t.string().optional(),
            "impactScore": t.number().optional(),
            "integrityImpact": t.string().optional(),
            "attackComplexity": t.string().optional(),
            "availabilityImpact": t.string().optional(),
            "confidentialityImpact": t.string().optional(),
            "scope": t.string().optional(),
            "attackVector": t.string().optional(),
            "exploitabilityScore": t.number().optional(),
        }
    ).named(renames["CVSSv3In"])
    types["CVSSv3Out"] = t.struct(
        {
            "privilegesRequired": t.string().optional(),
            "baseScore": t.number().optional(),
            "userInteraction": t.string().optional(),
            "impactScore": t.number().optional(),
            "integrityImpact": t.string().optional(),
            "attackComplexity": t.string().optional(),
            "availabilityImpact": t.string().optional(),
            "confidentialityImpact": t.string().optional(),
            "scope": t.string().optional(),
            "attackVector": t.string().optional(),
            "exploitabilityScore": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CVSSv3Out"])
    types["ExecutePatchJobRequestIn"] = t.struct(
        {
            "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
            "displayName": t.string().optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
            "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
            "description": t.string().optional(),
            "dryRun": t.boolean().optional(),
            "duration": t.string().optional(),
        }
    ).named(renames["ExecutePatchJobRequestIn"])
    types["ExecutePatchJobRequestOut"] = t.struct(
        {
            "patchConfig": t.proxy(renames["PatchConfigOut"]).optional(),
            "displayName": t.string().optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterOut"]),
            "rollout": t.proxy(renames["PatchRolloutOut"]).optional(),
            "description": t.string().optional(),
            "dryRun": t.boolean().optional(),
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutePatchJobRequestOut"])
    types["YumSettingsIn"] = t.struct(
        {
            "excludes": t.array(t.string()).optional(),
            "minimal": t.boolean().optional(),
            "exclusivePackages": t.array(t.string()).optional(),
            "security": t.boolean().optional(),
        }
    ).named(renames["YumSettingsIn"])
    types["YumSettingsOut"] = t.struct(
        {
            "excludes": t.array(t.string()).optional(),
            "minimal": t.boolean().optional(),
            "exclusivePackages": t.array(t.string()).optional(),
            "security": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YumSettingsOut"])
    types["WeeklyScheduleIn"] = t.struct({"dayOfWeek": t.string()}).named(
        renames["WeeklyScheduleIn"]
    )
    types["WeeklyScheduleOut"] = t.struct(
        {"dayOfWeek": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WeeklyScheduleOut"])
    types["InventorySoftwarePackageIn"] = t.struct(
        {
            "qfePackage": t.proxy(
                renames["InventoryWindowsQuickFixEngineeringPackageIn"]
            ).optional(),
            "wuaPackage": t.proxy(
                renames["InventoryWindowsUpdatePackageIn"]
            ).optional(),
            "yumPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
            "windowsApplication": t.proxy(
                renames["InventoryWindowsApplicationIn"]
            ).optional(),
            "cosPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
            "zypperPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
            "zypperPatch": t.proxy(renames["InventoryZypperPatchIn"]).optional(),
            "googetPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
            "aptPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
        }
    ).named(renames["InventorySoftwarePackageIn"])
    types["InventorySoftwarePackageOut"] = t.struct(
        {
            "qfePackage": t.proxy(
                renames["InventoryWindowsQuickFixEngineeringPackageOut"]
            ).optional(),
            "wuaPackage": t.proxy(
                renames["InventoryWindowsUpdatePackageOut"]
            ).optional(),
            "yumPackage": t.proxy(renames["InventoryVersionedPackageOut"]).optional(),
            "windowsApplication": t.proxy(
                renames["InventoryWindowsApplicationOut"]
            ).optional(),
            "cosPackage": t.proxy(renames["InventoryVersionedPackageOut"]).optional(),
            "zypperPackage": t.proxy(
                renames["InventoryVersionedPackageOut"]
            ).optional(),
            "zypperPatch": t.proxy(renames["InventoryZypperPatchOut"]).optional(),
            "googetPackage": t.proxy(
                renames["InventoryVersionedPackageOut"]
            ).optional(),
            "aptPackage": t.proxy(renames["InventoryVersionedPackageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySoftwarePackageOut"])
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

    functions = {}
    functions["projectsLocationsOsPolicyAssignmentsGet"] = osconfig.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOSPolicyAssignmentRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsPatch"] = osconfig.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
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
    functions["projectsLocationsInstancesOsPolicyAssignmentsReportsGet"] = osconfig.get(
        "v1/{parent}/reports",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOSPolicyAssignmentReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesVulnerabilityReportsGet"] = osconfig.get(
        "v1/{parent}/vulnerabilityReports",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVulnerabilityReportsResponseOut"]),
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
    functions["projectsPatchDeploymentsGet"] = osconfig.post(
        "v1/{name}:pause",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsList"] = osconfig.post(
        "v1/{name}:pause",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsResume"] = osconfig.post(
        "v1/{name}:pause",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsDelete"] = osconfig.post(
        "v1/{name}:pause",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsPatch"] = osconfig.post(
        "v1/{name}:pause",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsCreate"] = osconfig.post(
        "v1/{name}:pause",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsPause"] = osconfig.post(
        "v1/{name}:pause",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchJobsList"] = osconfig.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchJobsGet"] = osconfig.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchJobsExecute"] = osconfig.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchJobsCancel"] = osconfig.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchJobOut"]),
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
        importer="osconfig", renames=renames, types=types, functions=functions
    )
