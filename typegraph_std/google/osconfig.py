from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_osconfig():
    osconfig = HTTPRuntime("https://osconfig.googleapis.com/")

    renames = {
        "ErrorResponse": "_osconfig_1_ErrorResponse",
        "AptSettingsIn": "_osconfig_2_AptSettingsIn",
        "AptSettingsOut": "_osconfig_3_AptSettingsOut",
        "OSPolicyResourceRepositoryResourceGooRepositoryIn": "_osconfig_4_OSPolicyResourceRepositoryResourceGooRepositoryIn",
        "OSPolicyResourceRepositoryResourceGooRepositoryOut": "_osconfig_5_OSPolicyResourceRepositoryResourceGooRepositoryOut",
        "OSPolicyAssignmentLabelSetIn": "_osconfig_6_OSPolicyAssignmentLabelSetIn",
        "OSPolicyAssignmentLabelSetOut": "_osconfig_7_OSPolicyAssignmentLabelSetOut",
        "PatchDeploymentIn": "_osconfig_8_PatchDeploymentIn",
        "PatchDeploymentOut": "_osconfig_9_PatchDeploymentOut",
        "InventoryWindowsUpdatePackageWindowsUpdateCategoryIn": "_osconfig_10_InventoryWindowsUpdatePackageWindowsUpdateCategoryIn",
        "InventoryWindowsUpdatePackageWindowsUpdateCategoryOut": "_osconfig_11_InventoryWindowsUpdatePackageWindowsUpdateCategoryOut",
        "OSPolicyResourceRepositoryResourceYumRepositoryIn": "_osconfig_12_OSPolicyResourceRepositoryResourceYumRepositoryIn",
        "OSPolicyResourceRepositoryResourceYumRepositoryOut": "_osconfig_13_OSPolicyResourceRepositoryResourceYumRepositoryOut",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputIn": "_osconfig_14_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputIn",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputOut": "_osconfig_15_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputOut",
        "TimeZoneIn": "_osconfig_16_TimeZoneIn",
        "TimeZoneOut": "_osconfig_17_TimeZoneOut",
        "RecurringScheduleIn": "_osconfig_18_RecurringScheduleIn",
        "RecurringScheduleOut": "_osconfig_19_RecurringScheduleOut",
        "PatchConfigIn": "_osconfig_20_PatchConfigIn",
        "PatchConfigOut": "_osconfig_21_PatchConfigOut",
        "InventoryWindowsUpdatePackageIn": "_osconfig_22_InventoryWindowsUpdatePackageIn",
        "InventoryWindowsUpdatePackageOut": "_osconfig_23_InventoryWindowsUpdatePackageOut",
        "VulnerabilityReportVulnerabilityIn": "_osconfig_24_VulnerabilityReportVulnerabilityIn",
        "VulnerabilityReportVulnerabilityOut": "_osconfig_25_VulnerabilityReportVulnerabilityOut",
        "VulnerabilityReportIn": "_osconfig_26_VulnerabilityReportIn",
        "VulnerabilityReportOut": "_osconfig_27_VulnerabilityReportOut",
        "OSPolicyResourceRepositoryResourceAptRepositoryIn": "_osconfig_28_OSPolicyResourceRepositoryResourceAptRepositoryIn",
        "OSPolicyResourceRepositoryResourceAptRepositoryOut": "_osconfig_29_OSPolicyResourceRepositoryResourceAptRepositoryOut",
        "GooSettingsIn": "_osconfig_30_GooSettingsIn",
        "GooSettingsOut": "_osconfig_31_GooSettingsOut",
        "ExecutePatchJobRequestIn": "_osconfig_32_ExecutePatchJobRequestIn",
        "ExecutePatchJobRequestOut": "_osconfig_33_ExecutePatchJobRequestOut",
        "InventoryItemIn": "_osconfig_34_InventoryItemIn",
        "InventoryItemOut": "_osconfig_35_InventoryItemOut",
        "MonthlyScheduleIn": "_osconfig_36_MonthlyScheduleIn",
        "MonthlyScheduleOut": "_osconfig_37_MonthlyScheduleOut",
        "TimeOfDayIn": "_osconfig_38_TimeOfDayIn",
        "TimeOfDayOut": "_osconfig_39_TimeOfDayOut",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceIn": "_osconfig_40_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceIn",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOut": "_osconfig_41_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOut",
        "OSPolicyAssignmentOperationMetadataIn": "_osconfig_42_OSPolicyAssignmentOperationMetadataIn",
        "OSPolicyAssignmentOperationMetadataOut": "_osconfig_43_OSPolicyAssignmentOperationMetadataOut",
        "OSPolicyResourcePackageResourceDebIn": "_osconfig_44_OSPolicyResourcePackageResourceDebIn",
        "OSPolicyResourcePackageResourceDebOut": "_osconfig_45_OSPolicyResourcePackageResourceDebOut",
        "OperationIn": "_osconfig_46_OperationIn",
        "OperationOut": "_osconfig_47_OperationOut",
        "OSPolicyResourcePackageResourceZypperIn": "_osconfig_48_OSPolicyResourcePackageResourceZypperIn",
        "OSPolicyResourcePackageResourceZypperOut": "_osconfig_49_OSPolicyResourcePackageResourceZypperOut",
        "ExecStepConfigIn": "_osconfig_50_ExecStepConfigIn",
        "ExecStepConfigOut": "_osconfig_51_ExecStepConfigOut",
        "InventoryOsInfoIn": "_osconfig_52_InventoryOsInfoIn",
        "InventoryOsInfoOut": "_osconfig_53_InventoryOsInfoOut",
        "OSPolicyResourceExecResourceExecIn": "_osconfig_54_OSPolicyResourceExecResourceExecIn",
        "OSPolicyResourceExecResourceExecOut": "_osconfig_55_OSPolicyResourceExecResourceExecOut",
        "OSPolicyResourceFileRemoteIn": "_osconfig_56_OSPolicyResourceFileRemoteIn",
        "OSPolicyResourceFileRemoteOut": "_osconfig_57_OSPolicyResourceFileRemoteOut",
        "ListPatchJobInstanceDetailsResponseIn": "_osconfig_58_ListPatchJobInstanceDetailsResponseIn",
        "ListPatchJobInstanceDetailsResponseOut": "_osconfig_59_ListPatchJobInstanceDetailsResponseOut",
        "OSPolicyResourceRepositoryResourceIn": "_osconfig_60_OSPolicyResourceRepositoryResourceIn",
        "OSPolicyResourceRepositoryResourceOut": "_osconfig_61_OSPolicyResourceRepositoryResourceOut",
        "ListPatchJobsResponseIn": "_osconfig_62_ListPatchJobsResponseIn",
        "ListPatchJobsResponseOut": "_osconfig_63_ListPatchJobsResponseOut",
        "OSPolicyResourcePackageResourceGooGetIn": "_osconfig_64_OSPolicyResourcePackageResourceGooGetIn",
        "OSPolicyResourcePackageResourceGooGetOut": "_osconfig_65_OSPolicyResourcePackageResourceGooGetOut",
        "PausePatchDeploymentRequestIn": "_osconfig_66_PausePatchDeploymentRequestIn",
        "PausePatchDeploymentRequestOut": "_osconfig_67_PausePatchDeploymentRequestOut",
        "OSPolicyIn": "_osconfig_68_OSPolicyIn",
        "OSPolicyOut": "_osconfig_69_OSPolicyOut",
        "WeeklyScheduleIn": "_osconfig_70_WeeklyScheduleIn",
        "WeeklyScheduleOut": "_osconfig_71_WeeklyScheduleOut",
        "InventoryWindowsApplicationIn": "_osconfig_72_InventoryWindowsApplicationIn",
        "InventoryWindowsApplicationOut": "_osconfig_73_InventoryWindowsApplicationOut",
        "InventoryIn": "_osconfig_74_InventoryIn",
        "InventoryOut": "_osconfig_75_InventoryOut",
        "InventoryZypperPatchIn": "_osconfig_76_InventoryZypperPatchIn",
        "InventoryZypperPatchOut": "_osconfig_77_InventoryZypperPatchOut",
        "ListInventoriesResponseIn": "_osconfig_78_ListInventoriesResponseIn",
        "ListInventoriesResponseOut": "_osconfig_79_ListInventoriesResponseOut",
        "EmptyIn": "_osconfig_80_EmptyIn",
        "EmptyOut": "_osconfig_81_EmptyOut",
        "ListOSPolicyAssignmentsResponseIn": "_osconfig_82_ListOSPolicyAssignmentsResponseIn",
        "ListOSPolicyAssignmentsResponseOut": "_osconfig_83_ListOSPolicyAssignmentsResponseOut",
        "VulnerabilityReportVulnerabilityItemIn": "_osconfig_84_VulnerabilityReportVulnerabilityItemIn",
        "VulnerabilityReportVulnerabilityItemOut": "_osconfig_85_VulnerabilityReportVulnerabilityItemOut",
        "YumSettingsIn": "_osconfig_86_YumSettingsIn",
        "YumSettingsOut": "_osconfig_87_YumSettingsOut",
        "WeekDayOfMonthIn": "_osconfig_88_WeekDayOfMonthIn",
        "WeekDayOfMonthOut": "_osconfig_89_WeekDayOfMonthOut",
        "OSPolicyAssignmentInstanceFilterIn": "_osconfig_90_OSPolicyAssignmentInstanceFilterIn",
        "OSPolicyAssignmentInstanceFilterOut": "_osconfig_91_OSPolicyAssignmentInstanceFilterOut",
        "OSPolicyAssignmentReportIn": "_osconfig_92_OSPolicyAssignmentReportIn",
        "OSPolicyAssignmentReportOut": "_osconfig_93_OSPolicyAssignmentReportOut",
        "OSPolicyResourceFileIn": "_osconfig_94_OSPolicyResourceFileIn",
        "OSPolicyResourceFileOut": "_osconfig_95_OSPolicyResourceFileOut",
        "DateIn": "_osconfig_96_DateIn",
        "DateOut": "_osconfig_97_DateOut",
        "OSPolicyResourceIn": "_osconfig_98_OSPolicyResourceIn",
        "OSPolicyResourceOut": "_osconfig_99_OSPolicyResourceOut",
        "ListOSPolicyAssignmentReportsResponseIn": "_osconfig_100_ListOSPolicyAssignmentReportsResponseIn",
        "ListOSPolicyAssignmentReportsResponseOut": "_osconfig_101_ListOSPolicyAssignmentReportsResponseOut",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepIn": "_osconfig_102_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepIn",
        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepOut": "_osconfig_103_OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepOut",
        "OSPolicyAssignmentRolloutIn": "_osconfig_104_OSPolicyAssignmentRolloutIn",
        "OSPolicyAssignmentRolloutOut": "_osconfig_105_OSPolicyAssignmentRolloutOut",
        "OSPolicyResourceFileResourceIn": "_osconfig_106_OSPolicyResourceFileResourceIn",
        "OSPolicyResourceFileResourceOut": "_osconfig_107_OSPolicyResourceFileResourceOut",
        "ResumePatchDeploymentRequestIn": "_osconfig_108_ResumePatchDeploymentRequestIn",
        "ResumePatchDeploymentRequestOut": "_osconfig_109_ResumePatchDeploymentRequestOut",
        "ListPatchDeploymentsResponseIn": "_osconfig_110_ListPatchDeploymentsResponseIn",
        "ListPatchDeploymentsResponseOut": "_osconfig_111_ListPatchDeploymentsResponseOut",
        "InventoryVersionedPackageIn": "_osconfig_112_InventoryVersionedPackageIn",
        "InventoryVersionedPackageOut": "_osconfig_113_InventoryVersionedPackageOut",
        "PatchJobInstanceDetailsIn": "_osconfig_114_PatchJobInstanceDetailsIn",
        "PatchJobInstanceDetailsOut": "_osconfig_115_PatchJobInstanceDetailsOut",
        "PatchInstanceFilterIn": "_osconfig_116_PatchInstanceFilterIn",
        "PatchInstanceFilterOut": "_osconfig_117_PatchInstanceFilterOut",
        "OSPolicyResourcePackageResourceIn": "_osconfig_118_OSPolicyResourcePackageResourceIn",
        "OSPolicyResourcePackageResourceOut": "_osconfig_119_OSPolicyResourcePackageResourceOut",
        "ZypperSettingsIn": "_osconfig_120_ZypperSettingsIn",
        "ZypperSettingsOut": "_osconfig_121_ZypperSettingsOut",
        "PatchRolloutIn": "_osconfig_122_PatchRolloutIn",
        "PatchRolloutOut": "_osconfig_123_PatchRolloutOut",
        "ListVulnerabilityReportsResponseIn": "_osconfig_124_ListVulnerabilityReportsResponseIn",
        "ListVulnerabilityReportsResponseOut": "_osconfig_125_ListVulnerabilityReportsResponseOut",
        "WindowsUpdateSettingsIn": "_osconfig_126_WindowsUpdateSettingsIn",
        "WindowsUpdateSettingsOut": "_osconfig_127_WindowsUpdateSettingsOut",
        "OSPolicyResourceExecResourceIn": "_osconfig_128_OSPolicyResourceExecResourceIn",
        "OSPolicyResourceExecResourceOut": "_osconfig_129_OSPolicyResourceExecResourceOut",
        "OneTimeScheduleIn": "_osconfig_130_OneTimeScheduleIn",
        "OneTimeScheduleOut": "_osconfig_131_OneTimeScheduleOut",
        "PatchInstanceFilterGroupLabelIn": "_osconfig_132_PatchInstanceFilterGroupLabelIn",
        "PatchInstanceFilterGroupLabelOut": "_osconfig_133_PatchInstanceFilterGroupLabelOut",
        "OSPolicyResourceGroupIn": "_osconfig_134_OSPolicyResourceGroupIn",
        "OSPolicyResourceGroupOut": "_osconfig_135_OSPolicyResourceGroupOut",
        "PatchJobIn": "_osconfig_136_PatchJobIn",
        "PatchJobOut": "_osconfig_137_PatchJobOut",
        "ListOSPolicyAssignmentRevisionsResponseIn": "_osconfig_138_ListOSPolicyAssignmentRevisionsResponseIn",
        "ListOSPolicyAssignmentRevisionsResponseOut": "_osconfig_139_ListOSPolicyAssignmentRevisionsResponseOut",
        "GcsObjectIn": "_osconfig_140_GcsObjectIn",
        "GcsObjectOut": "_osconfig_141_GcsObjectOut",
        "OSPolicyResourcePackageResourceAPTIn": "_osconfig_142_OSPolicyResourcePackageResourceAPTIn",
        "OSPolicyResourcePackageResourceAPTOut": "_osconfig_143_OSPolicyResourcePackageResourceAPTOut",
        "OSPolicyResourcePackageResourceRPMIn": "_osconfig_144_OSPolicyResourcePackageResourceRPMIn",
        "OSPolicyResourcePackageResourceRPMOut": "_osconfig_145_OSPolicyResourcePackageResourceRPMOut",
        "GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataIn": "_osconfig_146_GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataIn",
        "GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataOut": "_osconfig_147_GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataOut",
        "OSPolicyAssignmentInstanceFilterInventoryIn": "_osconfig_148_OSPolicyAssignmentInstanceFilterInventoryIn",
        "OSPolicyAssignmentInstanceFilterInventoryOut": "_osconfig_149_OSPolicyAssignmentInstanceFilterInventoryOut",
        "FixedOrPercentIn": "_osconfig_150_FixedOrPercentIn",
        "FixedOrPercentOut": "_osconfig_151_FixedOrPercentOut",
        "OSPolicyAssignmentIn": "_osconfig_152_OSPolicyAssignmentIn",
        "OSPolicyAssignmentOut": "_osconfig_153_OSPolicyAssignmentOut",
        "StatusIn": "_osconfig_154_StatusIn",
        "StatusOut": "_osconfig_155_StatusOut",
        "CancelPatchJobRequestIn": "_osconfig_156_CancelPatchJobRequestIn",
        "CancelPatchJobRequestOut": "_osconfig_157_CancelPatchJobRequestOut",
        "InventoryWindowsQuickFixEngineeringPackageIn": "_osconfig_158_InventoryWindowsQuickFixEngineeringPackageIn",
        "InventoryWindowsQuickFixEngineeringPackageOut": "_osconfig_159_InventoryWindowsQuickFixEngineeringPackageOut",
        "OSPolicyAssignmentReportOSPolicyComplianceIn": "_osconfig_160_OSPolicyAssignmentReportOSPolicyComplianceIn",
        "OSPolicyAssignmentReportOSPolicyComplianceOut": "_osconfig_161_OSPolicyAssignmentReportOSPolicyComplianceOut",
        "InventorySoftwarePackageIn": "_osconfig_162_InventorySoftwarePackageIn",
        "InventorySoftwarePackageOut": "_osconfig_163_InventorySoftwarePackageOut",
        "OSPolicyResourcePackageResourceMSIIn": "_osconfig_164_OSPolicyResourcePackageResourceMSIIn",
        "OSPolicyResourcePackageResourceMSIOut": "_osconfig_165_OSPolicyResourcePackageResourceMSIOut",
        "PatchJobInstanceDetailsSummaryIn": "_osconfig_166_PatchJobInstanceDetailsSummaryIn",
        "PatchJobInstanceDetailsSummaryOut": "_osconfig_167_PatchJobInstanceDetailsSummaryOut",
        "VulnerabilityReportVulnerabilityDetailsIn": "_osconfig_168_VulnerabilityReportVulnerabilityDetailsIn",
        "VulnerabilityReportVulnerabilityDetailsOut": "_osconfig_169_VulnerabilityReportVulnerabilityDetailsOut",
        "OSPolicyResourceRepositoryResourceZypperRepositoryIn": "_osconfig_170_OSPolicyResourceRepositoryResourceZypperRepositoryIn",
        "OSPolicyResourceRepositoryResourceZypperRepositoryOut": "_osconfig_171_OSPolicyResourceRepositoryResourceZypperRepositoryOut",
        "OSPolicyResourcePackageResourceYUMIn": "_osconfig_172_OSPolicyResourcePackageResourceYUMIn",
        "OSPolicyResourcePackageResourceYUMOut": "_osconfig_173_OSPolicyResourcePackageResourceYUMOut",
        "VulnerabilityReportVulnerabilityDetailsReferenceIn": "_osconfig_174_VulnerabilityReportVulnerabilityDetailsReferenceIn",
        "VulnerabilityReportVulnerabilityDetailsReferenceOut": "_osconfig_175_VulnerabilityReportVulnerabilityDetailsReferenceOut",
        "CancelOperationRequestIn": "_osconfig_176_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_osconfig_177_CancelOperationRequestOut",
        "CVSSv3In": "_osconfig_178_CVSSv3In",
        "CVSSv3Out": "_osconfig_179_CVSSv3Out",
        "ExecStepIn": "_osconfig_180_ExecStepIn",
        "ExecStepOut": "_osconfig_181_ExecStepOut",
        "OSPolicyInventoryFilterIn": "_osconfig_182_OSPolicyInventoryFilterIn",
        "OSPolicyInventoryFilterOut": "_osconfig_183_OSPolicyInventoryFilterOut",
        "OSPolicyResourceFileGcsIn": "_osconfig_184_OSPolicyResourceFileGcsIn",
        "OSPolicyResourceFileGcsOut": "_osconfig_185_OSPolicyResourceFileGcsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AptSettingsIn"] = t.struct(
        {
            "excludes": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "exclusivePackages": t.array(t.string()).optional(),
        }
    ).named(renames["AptSettingsIn"])
    types["AptSettingsOut"] = t.struct(
        {
            "excludes": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "exclusivePackages": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AptSettingsOut"])
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
    types["OSPolicyAssignmentLabelSetIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["OSPolicyAssignmentLabelSetIn"])
    types["OSPolicyAssignmentLabelSetOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentLabelSetOut"])
    types["PatchDeploymentIn"] = t.struct(
        {
            "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
            "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
            "description": t.string().optional(),
            "recurringSchedule": t.proxy(renames["RecurringScheduleIn"]),
            "name": t.string().optional(),
            "oneTimeSchedule": t.proxy(renames["OneTimeScheduleIn"]),
            "duration": t.string().optional(),
        }
    ).named(renames["PatchDeploymentIn"])
    types["PatchDeploymentOut"] = t.struct(
        {
            "patchConfig": t.proxy(renames["PatchConfigOut"]).optional(),
            "rollout": t.proxy(renames["PatchRolloutOut"]).optional(),
            "lastExecuteTime": t.string().optional(),
            "state": t.string().optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterOut"]),
            "description": t.string().optional(),
            "recurringSchedule": t.proxy(renames["RecurringScheduleOut"]),
            "name": t.string().optional(),
            "oneTimeSchedule": t.proxy(renames["OneTimeScheduleOut"]),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchDeploymentOut"])
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
    types["OSPolicyResourceRepositoryResourceYumRepositoryIn"] = t.struct(
        {
            "baseUrl": t.string(),
            "gpgKeys": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "id": t.string(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceYumRepositoryIn"])
    types["OSPolicyResourceRepositoryResourceYumRepositoryOut"] = t.struct(
        {
            "baseUrl": t.string(),
            "gpgKeys": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceYumRepositoryOut"])
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
    types["RecurringScheduleIn"] = t.struct(
        {
            "frequency": t.string(),
            "startTime": t.string().optional(),
            "monthly": t.proxy(renames["MonthlyScheduleIn"]),
            "endTime": t.string().optional(),
            "timeOfDay": t.proxy(renames["TimeOfDayIn"]),
            "timeZone": t.proxy(renames["TimeZoneIn"]),
            "weekly": t.proxy(renames["WeeklyScheduleIn"]),
        }
    ).named(renames["RecurringScheduleIn"])
    types["RecurringScheduleOut"] = t.struct(
        {
            "frequency": t.string(),
            "nextExecuteTime": t.string().optional(),
            "startTime": t.string().optional(),
            "monthly": t.proxy(renames["MonthlyScheduleOut"]),
            "endTime": t.string().optional(),
            "timeOfDay": t.proxy(renames["TimeOfDayOut"]),
            "lastExecuteTime": t.string().optional(),
            "timeZone": t.proxy(renames["TimeZoneOut"]),
            "weekly": t.proxy(renames["WeeklyScheduleOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecurringScheduleOut"])
    types["PatchConfigIn"] = t.struct(
        {
            "goo": t.proxy(renames["GooSettingsIn"]).optional(),
            "migInstancesAllowed": t.boolean().optional(),
            "zypper": t.proxy(renames["ZypperSettingsIn"]).optional(),
            "preStep": t.proxy(renames["ExecStepIn"]).optional(),
            "rebootConfig": t.string().optional(),
            "windowsUpdate": t.proxy(renames["WindowsUpdateSettingsIn"]).optional(),
            "apt": t.proxy(renames["AptSettingsIn"]).optional(),
            "yum": t.proxy(renames["YumSettingsIn"]).optional(),
            "postStep": t.proxy(renames["ExecStepIn"]).optional(),
        }
    ).named(renames["PatchConfigIn"])
    types["PatchConfigOut"] = t.struct(
        {
            "goo": t.proxy(renames["GooSettingsOut"]).optional(),
            "migInstancesAllowed": t.boolean().optional(),
            "zypper": t.proxy(renames["ZypperSettingsOut"]).optional(),
            "preStep": t.proxy(renames["ExecStepOut"]).optional(),
            "rebootConfig": t.string().optional(),
            "windowsUpdate": t.proxy(renames["WindowsUpdateSettingsOut"]).optional(),
            "apt": t.proxy(renames["AptSettingsOut"]).optional(),
            "yum": t.proxy(renames["YumSettingsOut"]).optional(),
            "postStep": t.proxy(renames["ExecStepOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchConfigOut"])
    types["InventoryWindowsUpdatePackageIn"] = t.struct(
        {
            "description": t.string().optional(),
            "updateId": t.string().optional(),
            "categories": t.array(
                t.proxy(renames["InventoryWindowsUpdatePackageWindowsUpdateCategoryIn"])
            ).optional(),
            "moreInfoUrls": t.array(t.string()).optional(),
            "supportUrl": t.string().optional(),
            "lastDeploymentChangeTime": t.string().optional(),
            "kbArticleIds": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "revisionNumber": t.integer().optional(),
        }
    ).named(renames["InventoryWindowsUpdatePackageIn"])
    types["InventoryWindowsUpdatePackageOut"] = t.struct(
        {
            "description": t.string().optional(),
            "updateId": t.string().optional(),
            "categories": t.array(
                t.proxy(
                    renames["InventoryWindowsUpdatePackageWindowsUpdateCategoryOut"]
                )
            ).optional(),
            "moreInfoUrls": t.array(t.string()).optional(),
            "supportUrl": t.string().optional(),
            "lastDeploymentChangeTime": t.string().optional(),
            "kbArticleIds": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "revisionNumber": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryWindowsUpdatePackageOut"])
    types["VulnerabilityReportVulnerabilityIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "items": t.array(
                t.proxy(renames["VulnerabilityReportVulnerabilityItemIn"])
            ).optional(),
            "updateTime": t.string().optional(),
            "availableInventoryItemIds": t.array(t.string()).optional(),
            "details": t.proxy(
                renames["VulnerabilityReportVulnerabilityDetailsIn"]
            ).optional(),
            "installedInventoryItemIds": t.array(t.string()).optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityIn"])
    types["VulnerabilityReportVulnerabilityOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "items": t.array(
                t.proxy(renames["VulnerabilityReportVulnerabilityItemOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "availableInventoryItemIds": t.array(t.string()).optional(),
            "details": t.proxy(
                renames["VulnerabilityReportVulnerabilityDetailsOut"]
            ).optional(),
            "installedInventoryItemIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityOut"])
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
    types["OSPolicyResourceRepositoryResourceAptRepositoryIn"] = t.struct(
        {
            "distribution": t.string(),
            "components": t.array(t.string()),
            "archiveType": t.string(),
            "gpgKey": t.string().optional(),
            "uri": t.string(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceAptRepositoryIn"])
    types["OSPolicyResourceRepositoryResourceAptRepositoryOut"] = t.struct(
        {
            "distribution": t.string(),
            "components": t.array(t.string()),
            "archiveType": t.string(),
            "gpgKey": t.string().optional(),
            "uri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceAptRepositoryOut"])
    types["GooSettingsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GooSettingsIn"]
    )
    types["GooSettingsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooSettingsOut"])
    types["ExecutePatchJobRequestIn"] = t.struct(
        {
            "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "duration": t.string().optional(),
            "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
            "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
            "dryRun": t.boolean().optional(),
        }
    ).named(renames["ExecutePatchJobRequestIn"])
    types["ExecutePatchJobRequestOut"] = t.struct(
        {
            "instanceFilter": t.proxy(renames["PatchInstanceFilterOut"]),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "duration": t.string().optional(),
            "rollout": t.proxy(renames["PatchRolloutOut"]).optional(),
            "patchConfig": t.proxy(renames["PatchConfigOut"]).optional(),
            "dryRun": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutePatchJobRequestOut"])
    types["InventoryItemIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "id": t.string().optional(),
            "availablePackage": t.proxy(
                renames["InventorySoftwarePackageIn"]
            ).optional(),
            "type": t.string().optional(),
            "installedPackage": t.proxy(
                renames["InventorySoftwarePackageIn"]
            ).optional(),
            "originType": t.string().optional(),
        }
    ).named(renames["InventoryItemIn"])
    types["InventoryItemOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "id": t.string().optional(),
            "availablePackage": t.proxy(
                renames["InventorySoftwarePackageOut"]
            ).optional(),
            "type": t.string().optional(),
            "installedPackage": t.proxy(
                renames["InventorySoftwarePackageOut"]
            ).optional(),
            "originType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryItemOut"])
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
    types["TimeOfDayIn"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
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
            "complianceStateReason": t.string().optional(),
            "osPolicyResourceId": t.string().optional(),
            "execResourceOutput": t.proxy(
                renames[
                    "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputIn"
                ]
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
            "configSteps": t.array(
                t.proxy(
                    renames[
                        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStepOut"
                    ]
                )
            ).optional(),
            "complianceStateReason": t.string().optional(),
            "osPolicyResourceId": t.string().optional(),
            "execResourceOutput": t.proxy(
                renames[
                    "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutputOut"
                ]
            ).optional(),
            "complianceState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOut"
        ]
    )
    types["OSPolicyAssignmentOperationMetadataIn"] = t.struct(
        {
            "rolloutStartTime": t.string().optional(),
            "osPolicyAssignment": t.string().optional(),
            "apiMethod": t.string().optional(),
            "rolloutState": t.string().optional(),
            "rolloutUpdateTime": t.string().optional(),
        }
    ).named(renames["OSPolicyAssignmentOperationMetadataIn"])
    types["OSPolicyAssignmentOperationMetadataOut"] = t.struct(
        {
            "rolloutStartTime": t.string().optional(),
            "osPolicyAssignment": t.string().optional(),
            "apiMethod": t.string().optional(),
            "rolloutState": t.string().optional(),
            "rolloutUpdateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentOperationMetadataOut"])
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
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["OSPolicyResourcePackageResourceZypperIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["OSPolicyResourcePackageResourceZypperIn"])
    types["OSPolicyResourcePackageResourceZypperOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OSPolicyResourcePackageResourceZypperOut"])
    types["ExecStepConfigIn"] = t.struct(
        {
            "interpreter": t.string().optional(),
            "gcsObject": t.proxy(renames["GcsObjectIn"]).optional(),
            "allowedSuccessCodes": t.array(t.integer()).optional(),
            "localPath": t.string().optional(),
        }
    ).named(renames["ExecStepConfigIn"])
    types["ExecStepConfigOut"] = t.struct(
        {
            "interpreter": t.string().optional(),
            "gcsObject": t.proxy(renames["GcsObjectOut"]).optional(),
            "allowedSuccessCodes": t.array(t.integer()).optional(),
            "localPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecStepConfigOut"])
    types["InventoryOsInfoIn"] = t.struct(
        {
            "shortName": t.string().optional(),
            "architecture": t.string().optional(),
            "hostname": t.string().optional(),
            "longName": t.string().optional(),
            "osconfigAgentVersion": t.string().optional(),
            "kernelVersion": t.string().optional(),
            "version": t.string().optional(),
            "kernelRelease": t.string().optional(),
        }
    ).named(renames["InventoryOsInfoIn"])
    types["InventoryOsInfoOut"] = t.struct(
        {
            "shortName": t.string().optional(),
            "architecture": t.string().optional(),
            "hostname": t.string().optional(),
            "longName": t.string().optional(),
            "osconfigAgentVersion": t.string().optional(),
            "kernelVersion": t.string().optional(),
            "version": t.string().optional(),
            "kernelRelease": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryOsInfoOut"])
    types["OSPolicyResourceExecResourceExecIn"] = t.struct(
        {
            "outputFilePath": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "script": t.string().optional(),
            "file": t.proxy(renames["OSPolicyResourceFileIn"]).optional(),
            "interpreter": t.string(),
        }
    ).named(renames["OSPolicyResourceExecResourceExecIn"])
    types["OSPolicyResourceExecResourceExecOut"] = t.struct(
        {
            "outputFilePath": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "script": t.string().optional(),
            "file": t.proxy(renames["OSPolicyResourceFileOut"]).optional(),
            "interpreter": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceExecResourceExecOut"])
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
    types["OSPolicyResourceRepositoryResourceIn"] = t.struct(
        {
            "zypper": t.proxy(
                renames["OSPolicyResourceRepositoryResourceZypperRepositoryIn"]
            ).optional(),
            "yum": t.proxy(
                renames["OSPolicyResourceRepositoryResourceYumRepositoryIn"]
            ).optional(),
            "apt": t.proxy(
                renames["OSPolicyResourceRepositoryResourceAptRepositoryIn"]
            ).optional(),
            "goo": t.proxy(
                renames["OSPolicyResourceRepositoryResourceGooRepositoryIn"]
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
            "apt": t.proxy(
                renames["OSPolicyResourceRepositoryResourceAptRepositoryOut"]
            ).optional(),
            "goo": t.proxy(
                renames["OSPolicyResourceRepositoryResourceGooRepositoryOut"]
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
    types["OSPolicyResourcePackageResourceGooGetIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["OSPolicyResourcePackageResourceGooGetIn"])
    types["OSPolicyResourcePackageResourceGooGetOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OSPolicyResourcePackageResourceGooGetOut"])
    types["PausePatchDeploymentRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["PausePatchDeploymentRequestIn"])
    types["PausePatchDeploymentRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PausePatchDeploymentRequestOut"])
    types["OSPolicyIn"] = t.struct(
        {
            "description": t.string().optional(),
            "mode": t.string(),
            "resourceGroups": t.array(t.proxy(renames["OSPolicyResourceGroupIn"])),
            "allowNoResourceGroupMatch": t.boolean().optional(),
            "id": t.string(),
        }
    ).named(renames["OSPolicyIn"])
    types["OSPolicyOut"] = t.struct(
        {
            "description": t.string().optional(),
            "mode": t.string(),
            "resourceGroups": t.array(t.proxy(renames["OSPolicyResourceGroupOut"])),
            "allowNoResourceGroupMatch": t.boolean().optional(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyOut"])
    types["WeeklyScheduleIn"] = t.struct({"dayOfWeek": t.string()}).named(
        renames["WeeklyScheduleIn"]
    )
    types["WeeklyScheduleOut"] = t.struct(
        {"dayOfWeek": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WeeklyScheduleOut"])
    types["InventoryWindowsApplicationIn"] = t.struct(
        {
            "helpLink": t.string().optional(),
            "installDate": t.proxy(renames["DateIn"]).optional(),
            "displayVersion": t.string().optional(),
            "displayName": t.string().optional(),
            "publisher": t.string().optional(),
        }
    ).named(renames["InventoryWindowsApplicationIn"])
    types["InventoryWindowsApplicationOut"] = t.struct(
        {
            "helpLink": t.string().optional(),
            "installDate": t.proxy(renames["DateOut"]).optional(),
            "displayVersion": t.string().optional(),
            "displayName": t.string().optional(),
            "publisher": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryWindowsApplicationOut"])
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
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryOut"])
    types["InventoryZypperPatchIn"] = t.struct(
        {
            "patchName": t.string().optional(),
            "summary": t.string().optional(),
            "category": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["InventoryZypperPatchIn"])
    types["InventoryZypperPatchOut"] = t.struct(
        {
            "patchName": t.string().optional(),
            "summary": t.string().optional(),
            "category": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryZypperPatchOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["VulnerabilityReportVulnerabilityItemIn"] = t.struct(
        {
            "fixedCpeUri": t.string().optional(),
            "upstreamFix": t.string().optional(),
            "installedInventoryItemId": t.string().optional(),
            "availableInventoryItemId": t.string().optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityItemIn"])
    types["VulnerabilityReportVulnerabilityItemOut"] = t.struct(
        {
            "fixedCpeUri": t.string().optional(),
            "upstreamFix": t.string().optional(),
            "installedInventoryItemId": t.string().optional(),
            "availableInventoryItemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityItemOut"])
    types["YumSettingsIn"] = t.struct(
        {
            "minimal": t.boolean().optional(),
            "security": t.boolean().optional(),
            "exclusivePackages": t.array(t.string()).optional(),
            "excludes": t.array(t.string()).optional(),
        }
    ).named(renames["YumSettingsIn"])
    types["YumSettingsOut"] = t.struct(
        {
            "minimal": t.boolean().optional(),
            "security": t.boolean().optional(),
            "exclusivePackages": t.array(t.string()).optional(),
            "excludes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YumSettingsOut"])
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
    types["OSPolicyAssignmentInstanceFilterIn"] = t.struct(
        {
            "all": t.boolean().optional(),
            "inventories": t.array(
                t.proxy(renames["OSPolicyAssignmentInstanceFilterInventoryIn"])
            ).optional(),
            "exclusionLabels": t.array(
                t.proxy(renames["OSPolicyAssignmentLabelSetIn"])
            ).optional(),
            "inclusionLabels": t.array(
                t.proxy(renames["OSPolicyAssignmentLabelSetIn"])
            ).optional(),
        }
    ).named(renames["OSPolicyAssignmentInstanceFilterIn"])
    types["OSPolicyAssignmentInstanceFilterOut"] = t.struct(
        {
            "all": t.boolean().optional(),
            "inventories": t.array(
                t.proxy(renames["OSPolicyAssignmentInstanceFilterInventoryOut"])
            ).optional(),
            "exclusionLabels": t.array(
                t.proxy(renames["OSPolicyAssignmentLabelSetOut"])
            ).optional(),
            "inclusionLabels": t.array(
                t.proxy(renames["OSPolicyAssignmentLabelSetOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentInstanceFilterOut"])
    types["OSPolicyAssignmentReportIn"] = t.struct(
        {
            "lastRunId": t.string().optional(),
            "osPolicyAssignment": t.string().optional(),
            "osPolicyCompliances": t.array(
                t.proxy(renames["OSPolicyAssignmentReportOSPolicyComplianceIn"])
            ).optional(),
            "instance": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["OSPolicyAssignmentReportIn"])
    types["OSPolicyAssignmentReportOut"] = t.struct(
        {
            "lastRunId": t.string().optional(),
            "osPolicyAssignment": t.string().optional(),
            "osPolicyCompliances": t.array(
                t.proxy(renames["OSPolicyAssignmentReportOSPolicyComplianceOut"])
            ).optional(),
            "instance": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentReportOut"])
    types["OSPolicyResourceFileIn"] = t.struct(
        {
            "remote": t.proxy(renames["OSPolicyResourceFileRemoteIn"]).optional(),
            "allowInsecure": t.boolean().optional(),
            "localPath": t.string().optional(),
            "gcs": t.proxy(renames["OSPolicyResourceFileGcsIn"]).optional(),
        }
    ).named(renames["OSPolicyResourceFileIn"])
    types["OSPolicyResourceFileOut"] = t.struct(
        {
            "remote": t.proxy(renames["OSPolicyResourceFileRemoteOut"]).optional(),
            "allowInsecure": t.boolean().optional(),
            "localPath": t.string().optional(),
            "gcs": t.proxy(renames["OSPolicyResourceFileGcsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceFileOut"])
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["OSPolicyResourceIn"] = t.struct(
        {
            "file": t.proxy(renames["OSPolicyResourceFileResourceIn"]).optional(),
            "id": t.string(),
            "exec": t.proxy(renames["OSPolicyResourceExecResourceIn"]).optional(),
            "repository": t.proxy(
                renames["OSPolicyResourceRepositoryResourceIn"]
            ).optional(),
            "pkg": t.proxy(renames["OSPolicyResourcePackageResourceIn"]).optional(),
        }
    ).named(renames["OSPolicyResourceIn"])
    types["OSPolicyResourceOut"] = t.struct(
        {
            "file": t.proxy(renames["OSPolicyResourceFileResourceOut"]).optional(),
            "id": t.string(),
            "exec": t.proxy(renames["OSPolicyResourceExecResourceOut"]).optional(),
            "repository": t.proxy(
                renames["OSPolicyResourceRepositoryResourceOut"]
            ).optional(),
            "pkg": t.proxy(renames["OSPolicyResourcePackageResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceOut"])
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
    types["OSPolicyResourceFileResourceIn"] = t.struct(
        {
            "path": t.string(),
            "state": t.string(),
            "file": t.proxy(renames["OSPolicyResourceFileIn"]).optional(),
            "permissions": t.string().optional(),
            "content": t.string().optional(),
        }
    ).named(renames["OSPolicyResourceFileResourceIn"])
    types["OSPolicyResourceFileResourceOut"] = t.struct(
        {
            "path": t.string(),
            "state": t.string(),
            "file": t.proxy(renames["OSPolicyResourceFileOut"]).optional(),
            "permissions": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceFileResourceOut"])
    types["ResumePatchDeploymentRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResumePatchDeploymentRequestIn"])
    types["ResumePatchDeploymentRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumePatchDeploymentRequestOut"])
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
    types["PatchJobInstanceDetailsIn"] = t.struct(
        {
            "state": t.string().optional(),
            "attemptCount": t.string().optional(),
            "failureReason": t.string().optional(),
            "name": t.string().optional(),
            "instanceSystemId": t.string().optional(),
        }
    ).named(renames["PatchJobInstanceDetailsIn"])
    types["PatchJobInstanceDetailsOut"] = t.struct(
        {
            "state": t.string().optional(),
            "attemptCount": t.string().optional(),
            "failureReason": t.string().optional(),
            "name": t.string().optional(),
            "instanceSystemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchJobInstanceDetailsOut"])
    types["PatchInstanceFilterIn"] = t.struct(
        {
            "instances": t.array(t.string()).optional(),
            "zones": t.array(t.string()).optional(),
            "instanceNamePrefixes": t.array(t.string()).optional(),
            "all": t.boolean().optional(),
            "groupLabels": t.array(
                t.proxy(renames["PatchInstanceFilterGroupLabelIn"])
            ).optional(),
        }
    ).named(renames["PatchInstanceFilterIn"])
    types["PatchInstanceFilterOut"] = t.struct(
        {
            "instances": t.array(t.string()).optional(),
            "zones": t.array(t.string()).optional(),
            "instanceNamePrefixes": t.array(t.string()).optional(),
            "all": t.boolean().optional(),
            "groupLabels": t.array(
                t.proxy(renames["PatchInstanceFilterGroupLabelOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchInstanceFilterOut"])
    types["OSPolicyResourcePackageResourceIn"] = t.struct(
        {
            "apt": t.proxy(renames["OSPolicyResourcePackageResourceAPTIn"]).optional(),
            "deb": t.proxy(renames["OSPolicyResourcePackageResourceDebIn"]).optional(),
            "msi": t.proxy(renames["OSPolicyResourcePackageResourceMSIIn"]).optional(),
            "rpm": t.proxy(renames["OSPolicyResourcePackageResourceRPMIn"]).optional(),
            "zypper": t.proxy(
                renames["OSPolicyResourcePackageResourceZypperIn"]
            ).optional(),
            "desiredState": t.string(),
            "googet": t.proxy(
                renames["OSPolicyResourcePackageResourceGooGetIn"]
            ).optional(),
            "yum": t.proxy(renames["OSPolicyResourcePackageResourceYUMIn"]).optional(),
        }
    ).named(renames["OSPolicyResourcePackageResourceIn"])
    types["OSPolicyResourcePackageResourceOut"] = t.struct(
        {
            "apt": t.proxy(renames["OSPolicyResourcePackageResourceAPTOut"]).optional(),
            "deb": t.proxy(renames["OSPolicyResourcePackageResourceDebOut"]).optional(),
            "msi": t.proxy(renames["OSPolicyResourcePackageResourceMSIOut"]).optional(),
            "rpm": t.proxy(renames["OSPolicyResourcePackageResourceRPMOut"]).optional(),
            "zypper": t.proxy(
                renames["OSPolicyResourcePackageResourceZypperOut"]
            ).optional(),
            "desiredState": t.string(),
            "googet": t.proxy(
                renames["OSPolicyResourcePackageResourceGooGetOut"]
            ).optional(),
            "yum": t.proxy(renames["OSPolicyResourcePackageResourceYUMOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourcePackageResourceOut"])
    types["ZypperSettingsIn"] = t.struct(
        {
            "excludes": t.array(t.string()).optional(),
            "exclusivePatches": t.array(t.string()).optional(),
            "withOptional": t.boolean().optional(),
            "severities": t.array(t.string()).optional(),
            "categories": t.array(t.string()).optional(),
            "withUpdate": t.boolean().optional(),
        }
    ).named(renames["ZypperSettingsIn"])
    types["ZypperSettingsOut"] = t.struct(
        {
            "excludes": t.array(t.string()).optional(),
            "exclusivePatches": t.array(t.string()).optional(),
            "withOptional": t.boolean().optional(),
            "severities": t.array(t.string()).optional(),
            "categories": t.array(t.string()).optional(),
            "withUpdate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZypperSettingsOut"])
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
    types["ListVulnerabilityReportsResponseIn"] = t.struct(
        {
            "vulnerabilityReports": t.array(
                t.proxy(renames["VulnerabilityReportIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListVulnerabilityReportsResponseIn"])
    types["ListVulnerabilityReportsResponseOut"] = t.struct(
        {
            "vulnerabilityReports": t.array(
                t.proxy(renames["VulnerabilityReportOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVulnerabilityReportsResponseOut"])
    types["WindowsUpdateSettingsIn"] = t.struct(
        {
            "exclusivePatches": t.array(t.string()).optional(),
            "excludes": t.array(t.string()).optional(),
            "classifications": t.array(t.string()).optional(),
        }
    ).named(renames["WindowsUpdateSettingsIn"])
    types["WindowsUpdateSettingsOut"] = t.struct(
        {
            "exclusivePatches": t.array(t.string()).optional(),
            "excludes": t.array(t.string()).optional(),
            "classifications": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsUpdateSettingsOut"])
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
    types["OneTimeScheduleIn"] = t.struct({"executeTime": t.string()}).named(
        renames["OneTimeScheduleIn"]
    )
    types["OneTimeScheduleOut"] = t.struct(
        {
            "executeTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OneTimeScheduleOut"])
    types["PatchInstanceFilterGroupLabelIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["PatchInstanceFilterGroupLabelIn"])
    types["PatchInstanceFilterGroupLabelOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchInstanceFilterGroupLabelOut"])
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
    types["PatchJobIn"] = t.struct(
        {
            "name": t.string().optional(),
            "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]).optional(),
            "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
            "displayName": t.string().optional(),
            "dryRun": t.boolean().optional(),
            "errorMessage": t.string().optional(),
            "description": t.string().optional(),
            "duration": t.string().optional(),
            "percentComplete": t.number().optional(),
            "state": t.string().optional(),
            "instanceDetailsSummary": t.proxy(
                renames["PatchJobInstanceDetailsSummaryIn"]
            ).optional(),
        }
    ).named(renames["PatchJobIn"])
    types["PatchJobOut"] = t.struct(
        {
            "name": t.string().optional(),
            "patchConfig": t.proxy(renames["PatchConfigOut"]).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "instanceFilter": t.proxy(renames["PatchInstanceFilterOut"]).optional(),
            "rollout": t.proxy(renames["PatchRolloutOut"]).optional(),
            "displayName": t.string().optional(),
            "dryRun": t.boolean().optional(),
            "errorMessage": t.string().optional(),
            "description": t.string().optional(),
            "duration": t.string().optional(),
            "patchDeployment": t.string().optional(),
            "percentComplete": t.number().optional(),
            "state": t.string().optional(),
            "instanceDetailsSummary": t.proxy(
                renames["PatchJobInstanceDetailsSummaryOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchJobOut"])
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
    types["OSPolicyResourcePackageResourceAPTIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["OSPolicyResourcePackageResourceAPTIn"])
    types["OSPolicyResourcePackageResourceAPTOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OSPolicyResourcePackageResourceAPTOut"])
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
    types["GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataIn"] = t.struct(
        {
            "osPolicyAssignment": t.string().optional(),
            "rolloutState": t.string().optional(),
            "rolloutStartTime": t.string().optional(),
            "rolloutUpdateTime": t.string().optional(),
            "apiMethod": t.string().optional(),
        }
    ).named(renames["GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataIn"])
    types["GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataOut"] = t.struct(
        {
            "osPolicyAssignment": t.string().optional(),
            "rolloutState": t.string().optional(),
            "rolloutStartTime": t.string().optional(),
            "rolloutUpdateTime": t.string().optional(),
            "apiMethod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadataOut"])
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
    types["OSPolicyAssignmentIn"] = t.struct(
        {
            "osPolicies": t.array(t.proxy(renames["OSPolicyIn"])),
            "rollout": t.proxy(renames["OSPolicyAssignmentRolloutIn"]),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "etag": t.string().optional(),
            "instanceFilter": t.proxy(renames["OSPolicyAssignmentInstanceFilterIn"]),
        }
    ).named(renames["OSPolicyAssignmentIn"])
    types["OSPolicyAssignmentOut"] = t.struct(
        {
            "osPolicies": t.array(t.proxy(renames["OSPolicyOut"])),
            "revisionCreateTime": t.string().optional(),
            "rollout": t.proxy(renames["OSPolicyAssignmentRolloutOut"]),
            "deleted": t.boolean().optional(),
            "reconciling": t.boolean().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "uid": t.string().optional(),
            "baseline": t.boolean().optional(),
            "etag": t.string().optional(),
            "instanceFilter": t.proxy(renames["OSPolicyAssignmentInstanceFilterOut"]),
            "revisionId": t.string().optional(),
            "rolloutState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentOut"])
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
    types["CancelPatchJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelPatchJobRequestIn"]
    )
    types["CancelPatchJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelPatchJobRequestOut"])
    types["InventoryWindowsQuickFixEngineeringPackageIn"] = t.struct(
        {
            "description": t.string().optional(),
            "hotFixId": t.string().optional(),
            "caption": t.string().optional(),
            "installTime": t.string().optional(),
        }
    ).named(renames["InventoryWindowsQuickFixEngineeringPackageIn"])
    types["InventoryWindowsQuickFixEngineeringPackageOut"] = t.struct(
        {
            "description": t.string().optional(),
            "hotFixId": t.string().optional(),
            "caption": t.string().optional(),
            "installTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryWindowsQuickFixEngineeringPackageOut"])
    types["OSPolicyAssignmentReportOSPolicyComplianceIn"] = t.struct(
        {
            "osPolicyResourceCompliances": t.array(
                t.proxy(
                    renames[
                        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceIn"
                    ]
                )
            ).optional(),
            "osPolicyId": t.string().optional(),
            "complianceStateReason": t.string().optional(),
            "complianceState": t.string().optional(),
        }
    ).named(renames["OSPolicyAssignmentReportOSPolicyComplianceIn"])
    types["OSPolicyAssignmentReportOSPolicyComplianceOut"] = t.struct(
        {
            "osPolicyResourceCompliances": t.array(
                t.proxy(
                    renames[
                        "OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOut"
                    ]
                )
            ).optional(),
            "osPolicyId": t.string().optional(),
            "complianceStateReason": t.string().optional(),
            "complianceState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyAssignmentReportOSPolicyComplianceOut"])
    types["InventorySoftwarePackageIn"] = t.struct(
        {
            "qfePackage": t.proxy(
                renames["InventoryWindowsQuickFixEngineeringPackageIn"]
            ).optional(),
            "cosPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
            "zypperPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
            "windowsApplication": t.proxy(
                renames["InventoryWindowsApplicationIn"]
            ).optional(),
            "aptPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
            "googetPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
            "yumPackage": t.proxy(renames["InventoryVersionedPackageIn"]).optional(),
            "zypperPatch": t.proxy(renames["InventoryZypperPatchIn"]).optional(),
            "wuaPackage": t.proxy(
                renames["InventoryWindowsUpdatePackageIn"]
            ).optional(),
        }
    ).named(renames["InventorySoftwarePackageIn"])
    types["InventorySoftwarePackageOut"] = t.struct(
        {
            "qfePackage": t.proxy(
                renames["InventoryWindowsQuickFixEngineeringPackageOut"]
            ).optional(),
            "cosPackage": t.proxy(renames["InventoryVersionedPackageOut"]).optional(),
            "zypperPackage": t.proxy(
                renames["InventoryVersionedPackageOut"]
            ).optional(),
            "windowsApplication": t.proxy(
                renames["InventoryWindowsApplicationOut"]
            ).optional(),
            "aptPackage": t.proxy(renames["InventoryVersionedPackageOut"]).optional(),
            "googetPackage": t.proxy(
                renames["InventoryVersionedPackageOut"]
            ).optional(),
            "yumPackage": t.proxy(renames["InventoryVersionedPackageOut"]).optional(),
            "zypperPatch": t.proxy(renames["InventoryZypperPatchOut"]).optional(),
            "wuaPackage": t.proxy(
                renames["InventoryWindowsUpdatePackageOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySoftwarePackageOut"])
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
    types["PatchJobInstanceDetailsSummaryIn"] = t.struct(
        {
            "downloadingPatchesInstanceCount": t.string().optional(),
            "succeededInstanceCount": t.string().optional(),
            "pendingInstanceCount": t.string().optional(),
            "prePatchStepInstanceCount": t.string().optional(),
            "inactiveInstanceCount": t.string().optional(),
            "notifiedInstanceCount": t.string().optional(),
            "rebootingInstanceCount": t.string().optional(),
            "postPatchStepInstanceCount": t.string().optional(),
            "ackedInstanceCount": t.string().optional(),
            "failedInstanceCount": t.string().optional(),
            "applyingPatchesInstanceCount": t.string().optional(),
            "succeededRebootRequiredInstanceCount": t.string().optional(),
            "startedInstanceCount": t.string().optional(),
            "timedOutInstanceCount": t.string().optional(),
            "noAgentDetectedInstanceCount": t.string().optional(),
        }
    ).named(renames["PatchJobInstanceDetailsSummaryIn"])
    types["PatchJobInstanceDetailsSummaryOut"] = t.struct(
        {
            "downloadingPatchesInstanceCount": t.string().optional(),
            "succeededInstanceCount": t.string().optional(),
            "pendingInstanceCount": t.string().optional(),
            "prePatchStepInstanceCount": t.string().optional(),
            "inactiveInstanceCount": t.string().optional(),
            "notifiedInstanceCount": t.string().optional(),
            "rebootingInstanceCount": t.string().optional(),
            "postPatchStepInstanceCount": t.string().optional(),
            "ackedInstanceCount": t.string().optional(),
            "failedInstanceCount": t.string().optional(),
            "applyingPatchesInstanceCount": t.string().optional(),
            "succeededRebootRequiredInstanceCount": t.string().optional(),
            "startedInstanceCount": t.string().optional(),
            "timedOutInstanceCount": t.string().optional(),
            "noAgentDetectedInstanceCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatchJobInstanceDetailsSummaryOut"])
    types["VulnerabilityReportVulnerabilityDetailsIn"] = t.struct(
        {
            "references": t.array(
                t.proxy(renames["VulnerabilityReportVulnerabilityDetailsReferenceIn"])
            ).optional(),
            "cvssV2Score": t.number().optional(),
            "description": t.string().optional(),
            "severity": t.string().optional(),
            "cve": t.string().optional(),
            "cvssV3": t.proxy(renames["CVSSv3In"]).optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityDetailsIn"])
    types["VulnerabilityReportVulnerabilityDetailsOut"] = t.struct(
        {
            "references": t.array(
                t.proxy(renames["VulnerabilityReportVulnerabilityDetailsReferenceOut"])
            ).optional(),
            "cvssV2Score": t.number().optional(),
            "description": t.string().optional(),
            "severity": t.string().optional(),
            "cve": t.string().optional(),
            "cvssV3": t.proxy(renames["CVSSv3Out"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityReportVulnerabilityDetailsOut"])
    types["OSPolicyResourceRepositoryResourceZypperRepositoryIn"] = t.struct(
        {
            "gpgKeys": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "id": t.string(),
            "baseUrl": t.string(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceZypperRepositoryIn"])
    types["OSPolicyResourceRepositoryResourceZypperRepositoryOut"] = t.struct(
        {
            "gpgKeys": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "id": t.string(),
            "baseUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceRepositoryResourceZypperRepositoryOut"])
    types["OSPolicyResourcePackageResourceYUMIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["OSPolicyResourcePackageResourceYUMIn"])
    types["OSPolicyResourcePackageResourceYUMOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OSPolicyResourcePackageResourceYUMOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["CVSSv3In"] = t.struct(
        {
            "scope": t.string().optional(),
            "integrityImpact": t.string().optional(),
            "privilegesRequired": t.string().optional(),
            "availabilityImpact": t.string().optional(),
            "exploitabilityScore": t.number().optional(),
            "impactScore": t.number().optional(),
            "userInteraction": t.string().optional(),
            "attackVector": t.string().optional(),
            "attackComplexity": t.string().optional(),
            "confidentialityImpact": t.string().optional(),
            "baseScore": t.number().optional(),
        }
    ).named(renames["CVSSv3In"])
    types["CVSSv3Out"] = t.struct(
        {
            "scope": t.string().optional(),
            "integrityImpact": t.string().optional(),
            "privilegesRequired": t.string().optional(),
            "availabilityImpact": t.string().optional(),
            "exploitabilityScore": t.number().optional(),
            "impactScore": t.number().optional(),
            "userInteraction": t.string().optional(),
            "attackVector": t.string().optional(),
            "attackComplexity": t.string().optional(),
            "confidentialityImpact": t.string().optional(),
            "baseScore": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CVSSv3Out"])
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
    types["OSPolicyResourceFileGcsIn"] = t.struct(
        {
            "generation": t.string().optional(),
            "object": t.string(),
            "bucket": t.string(),
        }
    ).named(renames["OSPolicyResourceFileGcsIn"])
    types["OSPolicyResourceFileGcsOut"] = t.struct(
        {
            "generation": t.string().optional(),
            "object": t.string(),
            "bucket": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSPolicyResourceFileGcsOut"])

    functions = {}
    functions["projectsPatchJobsCancel"] = osconfig.post(
        "v1/{parent}/patchJobs:execute",
        t.struct(
            {
                "parent": t.string(),
                "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "duration": t.string().optional(),
                "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
                "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
                "dryRun": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchJobsGet"] = osconfig.post(
        "v1/{parent}/patchJobs:execute",
        t.struct(
            {
                "parent": t.string(),
                "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "duration": t.string().optional(),
                "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
                "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
                "dryRun": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchJobsList"] = osconfig.post(
        "v1/{parent}/patchJobs:execute",
        t.struct(
            {
                "parent": t.string(),
                "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "duration": t.string().optional(),
                "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
                "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
                "dryRun": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PatchJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchJobsExecute"] = osconfig.post(
        "v1/{parent}/patchJobs:execute",
        t.struct(
            {
                "parent": t.string(),
                "instanceFilter": t.proxy(renames["PatchInstanceFilterIn"]),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "duration": t.string().optional(),
                "rollout": t.proxy(renames["PatchRolloutIn"]).optional(),
                "patchConfig": t.proxy(renames["PatchConfigIn"]).optional(),
                "dryRun": t.boolean().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPatchJobInstanceDetailsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsPatch"] = osconfig.get(
        "v1/{parent}/patchDeployments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPatchDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsGet"] = osconfig.get(
        "v1/{parent}/patchDeployments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPatchDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsCreate"] = osconfig.get(
        "v1/{parent}/patchDeployments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPatchDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsDelete"] = osconfig.get(
        "v1/{parent}/patchDeployments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPatchDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsPause"] = osconfig.get(
        "v1/{parent}/patchDeployments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPatchDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsResume"] = osconfig.get(
        "v1/{parent}/patchDeployments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPatchDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatchDeploymentsList"] = osconfig.get(
        "v1/{parent}/patchDeployments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPatchDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsList"] = osconfig.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsPatch"] = osconfig.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsListRevisions"] = osconfig.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsCreate"] = osconfig.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsGet"] = osconfig.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOsPolicyAssignmentsDelete"] = osconfig.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
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
    functions["projectsLocationsInstancesInventoriesGet"] = osconfig.get(
        "v1/{parent}/inventories",
        t.struct(
            {
                "parent": t.string(),
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInventoriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesInventoriesList"] = osconfig.get(
        "v1/{parent}/inventories",
        t.struct(
            {
                "parent": t.string(),
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInventoriesResponseOut"]),
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

    return Import(
        importer="osconfig", renames=renames, types=Box(types), functions=Box(functions)
    )
