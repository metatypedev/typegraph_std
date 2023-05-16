from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_dataform() -> Import:
    dataform = HTTPRuntime("https://dataform.googleapis.com/")

    renames = {
        "ErrorResponse": "_dataform_1_ErrorResponse",
        "CancelWorkflowInvocationRequestIn": "_dataform_2_CancelWorkflowInvocationRequestIn",
        "CancelWorkflowInvocationRequestOut": "_dataform_3_CancelWorkflowInvocationRequestOut",
        "ListWorkflowConfigsResponseIn": "_dataform_4_ListWorkflowConfigsResponseIn",
        "ListWorkflowConfigsResponseOut": "_dataform_5_ListWorkflowConfigsResponseOut",
        "WorkflowInvocationActionIn": "_dataform_6_WorkflowInvocationActionIn",
        "WorkflowInvocationActionOut": "_dataform_7_WorkflowInvocationActionOut",
        "QueryDirectoryContentsResponseIn": "_dataform_8_QueryDirectoryContentsResponseIn",
        "QueryDirectoryContentsResponseOut": "_dataform_9_QueryDirectoryContentsResponseOut",
        "UncommittedFileChangeIn": "_dataform_10_UncommittedFileChangeIn",
        "UncommittedFileChangeOut": "_dataform_11_UncommittedFileChangeOut",
        "CommitWorkspaceChangesRequestIn": "_dataform_12_CommitWorkspaceChangesRequestIn",
        "CommitWorkspaceChangesRequestOut": "_dataform_13_CommitWorkspaceChangesRequestOut",
        "BindingIn": "_dataform_14_BindingIn",
        "BindingOut": "_dataform_15_BindingOut",
        "BigQueryActionIn": "_dataform_16_BigQueryActionIn",
        "BigQueryActionOut": "_dataform_17_BigQueryActionOut",
        "FetchFileDiffResponseIn": "_dataform_18_FetchFileDiffResponseIn",
        "FetchFileDiffResponseOut": "_dataform_19_FetchFileDiffResponseOut",
        "WorkflowConfigIn": "_dataform_20_WorkflowConfigIn",
        "WorkflowConfigOut": "_dataform_21_WorkflowConfigOut",
        "QueryCompilationResultActionsResponseIn": "_dataform_22_QueryCompilationResultActionsResponseIn",
        "QueryCompilationResultActionsResponseOut": "_dataform_23_QueryCompilationResultActionsResponseOut",
        "SetIamPolicyRequestIn": "_dataform_24_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_dataform_25_SetIamPolicyRequestOut",
        "MoveFileRequestIn": "_dataform_26_MoveFileRequestIn",
        "MoveFileRequestOut": "_dataform_27_MoveFileRequestOut",
        "MoveDirectoryRequestIn": "_dataform_28_MoveDirectoryRequestIn",
        "MoveDirectoryRequestOut": "_dataform_29_MoveDirectoryRequestOut",
        "DeclarationIn": "_dataform_30_DeclarationIn",
        "DeclarationOut": "_dataform_31_DeclarationOut",
        "ListRepositoriesResponseIn": "_dataform_32_ListRepositoriesResponseIn",
        "ListRepositoriesResponseOut": "_dataform_33_ListRepositoriesResponseOut",
        "ResetWorkspaceChangesRequestIn": "_dataform_34_ResetWorkspaceChangesRequestIn",
        "ResetWorkspaceChangesRequestOut": "_dataform_35_ResetWorkspaceChangesRequestOut",
        "WorkspaceIn": "_dataform_36_WorkspaceIn",
        "WorkspaceOut": "_dataform_37_WorkspaceOut",
        "WriteFileRequestIn": "_dataform_38_WriteFileRequestIn",
        "WriteFileRequestOut": "_dataform_39_WriteFileRequestOut",
        "WriteFileResponseIn": "_dataform_40_WriteFileResponseIn",
        "WriteFileResponseOut": "_dataform_41_WriteFileResponseOut",
        "CommitAuthorIn": "_dataform_42_CommitAuthorIn",
        "CommitAuthorOut": "_dataform_43_CommitAuthorOut",
        "FetchFileGitStatusesResponseIn": "_dataform_44_FetchFileGitStatusesResponseIn",
        "FetchFileGitStatusesResponseOut": "_dataform_45_FetchFileGitStatusesResponseOut",
        "MoveDirectoryResponseIn": "_dataform_46_MoveDirectoryResponseIn",
        "MoveDirectoryResponseOut": "_dataform_47_MoveDirectoryResponseOut",
        "WorkflowInvocationIn": "_dataform_48_WorkflowInvocationIn",
        "WorkflowInvocationOut": "_dataform_49_WorkflowInvocationOut",
        "FetchRemoteBranchesResponseIn": "_dataform_50_FetchRemoteBranchesResponseIn",
        "FetchRemoteBranchesResponseOut": "_dataform_51_FetchRemoteBranchesResponseOut",
        "ComputeRepositoryAccessTokenStatusResponseIn": "_dataform_52_ComputeRepositoryAccessTokenStatusResponseIn",
        "ComputeRepositoryAccessTokenStatusResponseOut": "_dataform_53_ComputeRepositoryAccessTokenStatusResponseOut",
        "EmptyIn": "_dataform_54_EmptyIn",
        "EmptyOut": "_dataform_55_EmptyOut",
        "IncrementalTableConfigIn": "_dataform_56_IncrementalTableConfigIn",
        "IncrementalTableConfigOut": "_dataform_57_IncrementalTableConfigOut",
        "InstallNpmPackagesResponseIn": "_dataform_58_InstallNpmPackagesResponseIn",
        "InstallNpmPackagesResponseOut": "_dataform_59_InstallNpmPackagesResponseOut",
        "ReadFileResponseIn": "_dataform_60_ReadFileResponseIn",
        "ReadFileResponseOut": "_dataform_61_ReadFileResponseOut",
        "CompilationErrorIn": "_dataform_62_CompilationErrorIn",
        "CompilationErrorOut": "_dataform_63_CompilationErrorOut",
        "StatusIn": "_dataform_64_StatusIn",
        "StatusOut": "_dataform_65_StatusOut",
        "QueryWorkflowInvocationActionsResponseIn": "_dataform_66_QueryWorkflowInvocationActionsResponseIn",
        "QueryWorkflowInvocationActionsResponseOut": "_dataform_67_QueryWorkflowInvocationActionsResponseOut",
        "MoveFileResponseIn": "_dataform_68_MoveFileResponseIn",
        "MoveFileResponseOut": "_dataform_69_MoveFileResponseOut",
        "ExprIn": "_dataform_70_ExprIn",
        "ExprOut": "_dataform_71_ExprOut",
        "PushGitCommitsRequestIn": "_dataform_72_PushGitCommitsRequestIn",
        "PushGitCommitsRequestOut": "_dataform_73_PushGitCommitsRequestOut",
        "CompilationResultIn": "_dataform_74_CompilationResultIn",
        "CompilationResultOut": "_dataform_75_CompilationResultOut",
        "ListWorkflowInvocationsResponseIn": "_dataform_76_ListWorkflowInvocationsResponseIn",
        "ListWorkflowInvocationsResponseOut": "_dataform_77_ListWorkflowInvocationsResponseOut",
        "OperationMetadataIn": "_dataform_78_OperationMetadataIn",
        "OperationMetadataOut": "_dataform_79_OperationMetadataOut",
        "FetchGitAheadBehindResponseIn": "_dataform_80_FetchGitAheadBehindResponseIn",
        "FetchGitAheadBehindResponseOut": "_dataform_81_FetchGitAheadBehindResponseOut",
        "LocationIn": "_dataform_82_LocationIn",
        "LocationOut": "_dataform_83_LocationOut",
        "RepositoryIn": "_dataform_84_RepositoryIn",
        "RepositoryOut": "_dataform_85_RepositoryOut",
        "ScheduledReleaseRecordIn": "_dataform_86_ScheduledReleaseRecordIn",
        "ScheduledReleaseRecordOut": "_dataform_87_ScheduledReleaseRecordOut",
        "ListWorkspacesResponseIn": "_dataform_88_ListWorkspacesResponseIn",
        "ListWorkspacesResponseOut": "_dataform_89_ListWorkspacesResponseOut",
        "GitRemoteSettingsIn": "_dataform_90_GitRemoteSettingsIn",
        "GitRemoteSettingsOut": "_dataform_91_GitRemoteSettingsOut",
        "MakeDirectoryRequestIn": "_dataform_92_MakeDirectoryRequestIn",
        "MakeDirectoryRequestOut": "_dataform_93_MakeDirectoryRequestOut",
        "ColumnDescriptorIn": "_dataform_94_ColumnDescriptorIn",
        "ColumnDescriptorOut": "_dataform_95_ColumnDescriptorOut",
        "TestIamPermissionsRequestIn": "_dataform_96_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_dataform_97_TestIamPermissionsRequestOut",
        "OperationsIn": "_dataform_98_OperationsIn",
        "OperationsOut": "_dataform_99_OperationsOut",
        "AssertionIn": "_dataform_100_AssertionIn",
        "AssertionOut": "_dataform_101_AssertionOut",
        "InvocationConfigIn": "_dataform_102_InvocationConfigIn",
        "InvocationConfigOut": "_dataform_103_InvocationConfigOut",
        "PolicyIn": "_dataform_104_PolicyIn",
        "PolicyOut": "_dataform_105_PolicyOut",
        "TestIamPermissionsResponseIn": "_dataform_106_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_dataform_107_TestIamPermissionsResponseOut",
        "ListReleaseConfigsResponseIn": "_dataform_108_ListReleaseConfigsResponseIn",
        "ListReleaseConfigsResponseOut": "_dataform_109_ListReleaseConfigsResponseOut",
        "ListLocationsResponseIn": "_dataform_110_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_dataform_111_ListLocationsResponseOut",
        "WorkspaceCompilationOverridesIn": "_dataform_112_WorkspaceCompilationOverridesIn",
        "WorkspaceCompilationOverridesOut": "_dataform_113_WorkspaceCompilationOverridesOut",
        "RemoveFileRequestIn": "_dataform_114_RemoveFileRequestIn",
        "RemoveFileRequestOut": "_dataform_115_RemoveFileRequestOut",
        "CodeCompilationConfigIn": "_dataform_116_CodeCompilationConfigIn",
        "CodeCompilationConfigOut": "_dataform_117_CodeCompilationConfigOut",
        "ListCompilationResultsResponseIn": "_dataform_118_ListCompilationResultsResponseIn",
        "ListCompilationResultsResponseOut": "_dataform_119_ListCompilationResultsResponseOut",
        "ScheduledExecutionRecordIn": "_dataform_120_ScheduledExecutionRecordIn",
        "ScheduledExecutionRecordOut": "_dataform_121_ScheduledExecutionRecordOut",
        "ReleaseConfigIn": "_dataform_122_ReleaseConfigIn",
        "ReleaseConfigOut": "_dataform_123_ReleaseConfigOut",
        "RelationDescriptorIn": "_dataform_124_RelationDescriptorIn",
        "RelationDescriptorOut": "_dataform_125_RelationDescriptorOut",
        "IntervalIn": "_dataform_126_IntervalIn",
        "IntervalOut": "_dataform_127_IntervalOut",
        "TargetIn": "_dataform_128_TargetIn",
        "TargetOut": "_dataform_129_TargetOut",
        "MakeDirectoryResponseIn": "_dataform_130_MakeDirectoryResponseIn",
        "MakeDirectoryResponseOut": "_dataform_131_MakeDirectoryResponseOut",
        "CompilationResultActionIn": "_dataform_132_CompilationResultActionIn",
        "CompilationResultActionOut": "_dataform_133_CompilationResultActionOut",
        "InstallNpmPackagesRequestIn": "_dataform_134_InstallNpmPackagesRequestIn",
        "InstallNpmPackagesRequestOut": "_dataform_135_InstallNpmPackagesRequestOut",
        "DirectoryEntryIn": "_dataform_136_DirectoryEntryIn",
        "DirectoryEntryOut": "_dataform_137_DirectoryEntryOut",
        "PullGitCommitsRequestIn": "_dataform_138_PullGitCommitsRequestIn",
        "PullGitCommitsRequestOut": "_dataform_139_PullGitCommitsRequestOut",
        "RelationIn": "_dataform_140_RelationIn",
        "RelationOut": "_dataform_141_RelationOut",
        "RemoveDirectoryRequestIn": "_dataform_142_RemoveDirectoryRequestIn",
        "RemoveDirectoryRequestOut": "_dataform_143_RemoveDirectoryRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CancelWorkflowInvocationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CancelWorkflowInvocationRequestIn"])
    types["CancelWorkflowInvocationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelWorkflowInvocationRequestOut"])
    types["ListWorkflowConfigsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "workflowConfigs": t.array(t.proxy(renames["WorkflowConfigIn"])).optional(),
        }
    ).named(renames["ListWorkflowConfigsResponseIn"])
    types["ListWorkflowConfigsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "workflowConfigs": t.array(
                t.proxy(renames["WorkflowConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkflowConfigsResponseOut"])
    types["WorkflowInvocationActionIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WorkflowInvocationActionIn"]
    )
    types["WorkflowInvocationActionOut"] = t.struct(
        {
            "bigqueryAction": t.proxy(renames["BigQueryActionOut"]).optional(),
            "target": t.proxy(renames["TargetOut"]).optional(),
            "invocationTiming": t.proxy(renames["IntervalOut"]).optional(),
            "failureReason": t.string().optional(),
            "state": t.string().optional(),
            "canonicalTarget": t.proxy(renames["TargetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowInvocationActionOut"])
    types["QueryDirectoryContentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "directoryEntries": t.array(
                t.proxy(renames["DirectoryEntryIn"])
            ).optional(),
        }
    ).named(renames["QueryDirectoryContentsResponseIn"])
    types["QueryDirectoryContentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "directoryEntries": t.array(
                t.proxy(renames["DirectoryEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryDirectoryContentsResponseOut"])
    types["UncommittedFileChangeIn"] = t.struct(
        {"state": t.string().optional(), "path": t.string().optional()}
    ).named(renames["UncommittedFileChangeIn"])
    types["UncommittedFileChangeOut"] = t.struct(
        {
            "state": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UncommittedFileChangeOut"])
    types["CommitWorkspaceChangesRequestIn"] = t.struct(
        {
            "author": t.proxy(renames["CommitAuthorIn"]),
            "commitMessage": t.string().optional(),
            "paths": t.array(t.string()).optional(),
        }
    ).named(renames["CommitWorkspaceChangesRequestIn"])
    types["CommitWorkspaceChangesRequestOut"] = t.struct(
        {
            "author": t.proxy(renames["CommitAuthorOut"]),
            "commitMessage": t.string().optional(),
            "paths": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitWorkspaceChangesRequestOut"])
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
    types["BigQueryActionIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BigQueryActionIn"]
    )
    types["BigQueryActionOut"] = t.struct(
        {
            "sqlScript": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryActionOut"])
    types["FetchFileDiffResponseIn"] = t.struct(
        {"formattedDiff": t.string().optional()}
    ).named(renames["FetchFileDiffResponseIn"])
    types["FetchFileDiffResponseOut"] = t.struct(
        {
            "formattedDiff": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchFileDiffResponseOut"])
    types["WorkflowConfigIn"] = t.struct(
        {
            "releaseConfig": t.string(),
            "timeZone": t.string().optional(),
            "invocationConfig": t.proxy(renames["InvocationConfigIn"]).optional(),
            "cronSchedule": t.string().optional(),
        }
    ).named(renames["WorkflowConfigIn"])
    types["WorkflowConfigOut"] = t.struct(
        {
            "releaseConfig": t.string(),
            "timeZone": t.string().optional(),
            "invocationConfig": t.proxy(renames["InvocationConfigOut"]).optional(),
            "cronSchedule": t.string().optional(),
            "name": t.string().optional(),
            "recentScheduledExecutionRecords": t.array(
                t.proxy(renames["ScheduledExecutionRecordOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowConfigOut"])
    types["QueryCompilationResultActionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "compilationResultActions": t.array(
                t.proxy(renames["CompilationResultActionIn"])
            ).optional(),
        }
    ).named(renames["QueryCompilationResultActionsResponseIn"])
    types["QueryCompilationResultActionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "compilationResultActions": t.array(
                t.proxy(renames["CompilationResultActionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryCompilationResultActionsResponseOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["MoveFileRequestIn"] = t.struct(
        {"path": t.string(), "newPath": t.string()}
    ).named(renames["MoveFileRequestIn"])
    types["MoveFileRequestOut"] = t.struct(
        {
            "path": t.string(),
            "newPath": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveFileRequestOut"])
    types["MoveDirectoryRequestIn"] = t.struct(
        {"path": t.string(), "newPath": t.string()}
    ).named(renames["MoveDirectoryRequestIn"])
    types["MoveDirectoryRequestOut"] = t.struct(
        {
            "path": t.string(),
            "newPath": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveDirectoryRequestOut"])
    types["DeclarationIn"] = t.struct(
        {"relationDescriptor": t.proxy(renames["RelationDescriptorIn"]).optional()}
    ).named(renames["DeclarationIn"])
    types["DeclarationOut"] = t.struct(
        {
            "relationDescriptor": t.proxy(renames["RelationDescriptorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeclarationOut"])
    types["ListRepositoriesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "repositories": t.array(t.proxy(renames["RepositoryIn"])).optional(),
        }
    ).named(renames["ListRepositoriesResponseIn"])
    types["ListRepositoriesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "repositories": t.array(t.proxy(renames["RepositoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRepositoriesResponseOut"])
    types["ResetWorkspaceChangesRequestIn"] = t.struct(
        {"paths": t.array(t.string()).optional(), "clean": t.boolean().optional()}
    ).named(renames["ResetWorkspaceChangesRequestIn"])
    types["ResetWorkspaceChangesRequestOut"] = t.struct(
        {
            "paths": t.array(t.string()).optional(),
            "clean": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResetWorkspaceChangesRequestOut"])
    types["WorkspaceIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WorkspaceIn"]
    )
    types["WorkspaceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkspaceOut"])
    types["WriteFileRequestIn"] = t.struct(
        {"path": t.string(), "contents": t.string()}
    ).named(renames["WriteFileRequestIn"])
    types["WriteFileRequestOut"] = t.struct(
        {
            "path": t.string(),
            "contents": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteFileRequestOut"])
    types["WriteFileResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WriteFileResponseIn"]
    )
    types["WriteFileResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WriteFileResponseOut"])
    types["CommitAuthorIn"] = t.struct(
        {"emailAddress": t.string(), "name": t.string()}
    ).named(renames["CommitAuthorIn"])
    types["CommitAuthorOut"] = t.struct(
        {
            "emailAddress": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitAuthorOut"])
    types["FetchFileGitStatusesResponseIn"] = t.struct(
        {
            "uncommittedFileChanges": t.array(
                t.proxy(renames["UncommittedFileChangeIn"])
            ).optional()
        }
    ).named(renames["FetchFileGitStatusesResponseIn"])
    types["FetchFileGitStatusesResponseOut"] = t.struct(
        {
            "uncommittedFileChanges": t.array(
                t.proxy(renames["UncommittedFileChangeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchFileGitStatusesResponseOut"])
    types["MoveDirectoryResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MoveDirectoryResponseIn"]
    )
    types["MoveDirectoryResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MoveDirectoryResponseOut"])
    types["WorkflowInvocationIn"] = t.struct(
        {
            "workflowConfig": t.string().optional(),
            "invocationConfig": t.proxy(renames["InvocationConfigIn"]).optional(),
            "compilationResult": t.string().optional(),
        }
    ).named(renames["WorkflowInvocationIn"])
    types["WorkflowInvocationOut"] = t.struct(
        {
            "workflowConfig": t.string().optional(),
            "name": t.string().optional(),
            "invocationTiming": t.proxy(renames["IntervalOut"]).optional(),
            "invocationConfig": t.proxy(renames["InvocationConfigOut"]).optional(),
            "state": t.string().optional(),
            "compilationResult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowInvocationOut"])
    types["FetchRemoteBranchesResponseIn"] = t.struct(
        {"branches": t.array(t.string()).optional()}
    ).named(renames["FetchRemoteBranchesResponseIn"])
    types["FetchRemoteBranchesResponseOut"] = t.struct(
        {
            "branches": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchRemoteBranchesResponseOut"])
    types["ComputeRepositoryAccessTokenStatusResponseIn"] = t.struct(
        {"tokenStatus": t.string().optional()}
    ).named(renames["ComputeRepositoryAccessTokenStatusResponseIn"])
    types["ComputeRepositoryAccessTokenStatusResponseOut"] = t.struct(
        {
            "tokenStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeRepositoryAccessTokenStatusResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["IncrementalTableConfigIn"] = t.struct(
        {
            "incrementalSelectQuery": t.string().optional(),
            "updatePartitionFilter": t.string().optional(),
            "uniqueKeyParts": t.array(t.string()).optional(),
            "incrementalPreOperations": t.array(t.string()).optional(),
            "refreshDisabled": t.boolean().optional(),
            "incrementalPostOperations": t.array(t.string()).optional(),
        }
    ).named(renames["IncrementalTableConfigIn"])
    types["IncrementalTableConfigOut"] = t.struct(
        {
            "incrementalSelectQuery": t.string().optional(),
            "updatePartitionFilter": t.string().optional(),
            "uniqueKeyParts": t.array(t.string()).optional(),
            "incrementalPreOperations": t.array(t.string()).optional(),
            "refreshDisabled": t.boolean().optional(),
            "incrementalPostOperations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IncrementalTableConfigOut"])
    types["InstallNpmPackagesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["InstallNpmPackagesResponseIn"])
    types["InstallNpmPackagesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InstallNpmPackagesResponseOut"])
    types["ReadFileResponseIn"] = t.struct(
        {"fileContents": t.string().optional()}
    ).named(renames["ReadFileResponseIn"])
    types["ReadFileResponseOut"] = t.struct(
        {
            "fileContents": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadFileResponseOut"])
    types["CompilationErrorIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CompilationErrorIn"]
    )
    types["CompilationErrorOut"] = t.struct(
        {
            "path": t.string().optional(),
            "message": t.string().optional(),
            "stack": t.string().optional(),
            "actionTarget": t.proxy(renames["TargetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompilationErrorOut"])
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
    types["QueryWorkflowInvocationActionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "workflowInvocationActions": t.array(
                t.proxy(renames["WorkflowInvocationActionIn"])
            ).optional(),
        }
    ).named(renames["QueryWorkflowInvocationActionsResponseIn"])
    types["QueryWorkflowInvocationActionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "workflowInvocationActions": t.array(
                t.proxy(renames["WorkflowInvocationActionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryWorkflowInvocationActionsResponseOut"])
    types["MoveFileResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MoveFileResponseIn"]
    )
    types["MoveFileResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MoveFileResponseOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["PushGitCommitsRequestIn"] = t.struct(
        {"remoteBranch": t.string().optional()}
    ).named(renames["PushGitCommitsRequestIn"])
    types["PushGitCommitsRequestOut"] = t.struct(
        {
            "remoteBranch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PushGitCommitsRequestOut"])
    types["CompilationResultIn"] = t.struct(
        {
            "gitCommitish": t.string().optional(),
            "releaseConfig": t.string().optional(),
            "codeCompilationConfig": t.proxy(
                renames["CodeCompilationConfigIn"]
            ).optional(),
            "workspace": t.string().optional(),
        }
    ).named(renames["CompilationResultIn"])
    types["CompilationResultOut"] = t.struct(
        {
            "resolvedGitCommitSha": t.string().optional(),
            "gitCommitish": t.string().optional(),
            "releaseConfig": t.string().optional(),
            "codeCompilationConfig": t.proxy(
                renames["CodeCompilationConfigOut"]
            ).optional(),
            "dataformCoreVersion": t.string().optional(),
            "compilationErrors": t.array(
                t.proxy(renames["CompilationErrorOut"])
            ).optional(),
            "name": t.string().optional(),
            "workspace": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompilationResultOut"])
    types["ListWorkflowInvocationsResponseIn"] = t.struct(
        {
            "workflowInvocations": t.array(
                t.proxy(renames["WorkflowInvocationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListWorkflowInvocationsResponseIn"])
    types["ListWorkflowInvocationsResponseOut"] = t.struct(
        {
            "workflowInvocations": t.array(
                t.proxy(renames["WorkflowInvocationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkflowInvocationsResponseOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "cancelRequested": t.boolean().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["FetchGitAheadBehindResponseIn"] = t.struct(
        {
            "commitsAhead": t.integer().optional(),
            "commitsBehind": t.integer().optional(),
        }
    ).named(renames["FetchGitAheadBehindResponseIn"])
    types["FetchGitAheadBehindResponseOut"] = t.struct(
        {
            "commitsAhead": t.integer().optional(),
            "commitsBehind": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchGitAheadBehindResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["RepositoryIn"] = t.struct(
        {
            "workspaceCompilationOverrides": t.proxy(
                renames["WorkspaceCompilationOverridesIn"]
            ).optional(),
            "gitRemoteSettings": t.proxy(renames["GitRemoteSettingsIn"]).optional(),
            "npmrcEnvironmentVariablesSecretVersion": t.string().optional(),
        }
    ).named(renames["RepositoryIn"])
    types["RepositoryOut"] = t.struct(
        {
            "workspaceCompilationOverrides": t.proxy(
                renames["WorkspaceCompilationOverridesOut"]
            ).optional(),
            "gitRemoteSettings": t.proxy(renames["GitRemoteSettingsOut"]).optional(),
            "npmrcEnvironmentVariablesSecretVersion": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepositoryOut"])
    types["ScheduledReleaseRecordIn"] = t.struct(
        {
            "releaseTime": t.string().optional(),
            "compilationResult": t.string().optional(),
            "errorStatus": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["ScheduledReleaseRecordIn"])
    types["ScheduledReleaseRecordOut"] = t.struct(
        {
            "releaseTime": t.string().optional(),
            "compilationResult": t.string().optional(),
            "errorStatus": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduledReleaseRecordOut"])
    types["ListWorkspacesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "workspaces": t.array(t.proxy(renames["WorkspaceIn"])).optional(),
        }
    ).named(renames["ListWorkspacesResponseIn"])
    types["ListWorkspacesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "workspaces": t.array(t.proxy(renames["WorkspaceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkspacesResponseOut"])
    types["GitRemoteSettingsIn"] = t.struct(
        {
            "authenticationTokenSecretVersion": t.string(),
            "defaultBranch": t.string(),
            "url": t.string(),
        }
    ).named(renames["GitRemoteSettingsIn"])
    types["GitRemoteSettingsOut"] = t.struct(
        {
            "tokenStatus": t.string().optional(),
            "authenticationTokenSecretVersion": t.string(),
            "defaultBranch": t.string(),
            "url": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitRemoteSettingsOut"])
    types["MakeDirectoryRequestIn"] = t.struct({"path": t.string()}).named(
        renames["MakeDirectoryRequestIn"]
    )
    types["MakeDirectoryRequestOut"] = t.struct(
        {"path": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MakeDirectoryRequestOut"])
    types["ColumnDescriptorIn"] = t.struct(
        {
            "path": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "bigqueryPolicyTags": t.array(t.string()).optional(),
        }
    ).named(renames["ColumnDescriptorIn"])
    types["ColumnDescriptorOut"] = t.struct(
        {
            "path": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "bigqueryPolicyTags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnDescriptorOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["OperationsIn"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "queries": t.array(t.string()).optional(),
            "hasOutput": t.boolean().optional(),
            "disabled": t.boolean().optional(),
            "dependencyTargets": t.array(t.proxy(renames["TargetIn"])).optional(),
            "relationDescriptor": t.proxy(renames["RelationDescriptorIn"]).optional(),
        }
    ).named(renames["OperationsIn"])
    types["OperationsOut"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "queries": t.array(t.string()).optional(),
            "hasOutput": t.boolean().optional(),
            "disabled": t.boolean().optional(),
            "dependencyTargets": t.array(t.proxy(renames["TargetOut"])).optional(),
            "relationDescriptor": t.proxy(renames["RelationDescriptorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationsOut"])
    types["AssertionIn"] = t.struct(
        {
            "parentAction": t.proxy(renames["TargetIn"]).optional(),
            "tags": t.array(t.string()).optional(),
            "disabled": t.boolean().optional(),
            "dependencyTargets": t.array(t.proxy(renames["TargetIn"])).optional(),
            "selectQuery": t.string().optional(),
            "relationDescriptor": t.proxy(renames["RelationDescriptorIn"]).optional(),
        }
    ).named(renames["AssertionIn"])
    types["AssertionOut"] = t.struct(
        {
            "parentAction": t.proxy(renames["TargetOut"]).optional(),
            "tags": t.array(t.string()).optional(),
            "disabled": t.boolean().optional(),
            "dependencyTargets": t.array(t.proxy(renames["TargetOut"])).optional(),
            "selectQuery": t.string().optional(),
            "relationDescriptor": t.proxy(renames["RelationDescriptorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssertionOut"])
    types["InvocationConfigIn"] = t.struct(
        {
            "transitiveDependenciesIncluded": t.boolean().optional(),
            "includedTags": t.array(t.string()).optional(),
            "includedTargets": t.array(t.proxy(renames["TargetIn"])).optional(),
            "fullyRefreshIncrementalTablesEnabled": t.boolean().optional(),
            "transitiveDependentsIncluded": t.boolean().optional(),
        }
    ).named(renames["InvocationConfigIn"])
    types["InvocationConfigOut"] = t.struct(
        {
            "transitiveDependenciesIncluded": t.boolean().optional(),
            "includedTags": t.array(t.string()).optional(),
            "includedTargets": t.array(t.proxy(renames["TargetOut"])).optional(),
            "fullyRefreshIncrementalTablesEnabled": t.boolean().optional(),
            "transitiveDependentsIncluded": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvocationConfigOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ListReleaseConfigsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "releaseConfigs": t.array(t.proxy(renames["ReleaseConfigIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListReleaseConfigsResponseIn"])
    types["ListReleaseConfigsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "releaseConfigs": t.array(t.proxy(renames["ReleaseConfigOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReleaseConfigsResponseOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["WorkspaceCompilationOverridesIn"] = t.struct(
        {
            "defaultDatabase": t.string().optional(),
            "tablePrefix": t.string().optional(),
            "schemaSuffix": t.string().optional(),
        }
    ).named(renames["WorkspaceCompilationOverridesIn"])
    types["WorkspaceCompilationOverridesOut"] = t.struct(
        {
            "defaultDatabase": t.string().optional(),
            "tablePrefix": t.string().optional(),
            "schemaSuffix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkspaceCompilationOverridesOut"])
    types["RemoveFileRequestIn"] = t.struct({"path": t.string()}).named(
        renames["RemoveFileRequestIn"]
    )
    types["RemoveFileRequestOut"] = t.struct(
        {"path": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveFileRequestOut"])
    types["CodeCompilationConfigIn"] = t.struct(
        {
            "tablePrefix": t.string().optional(),
            "databaseSuffix": t.string().optional(),
            "assertionSchema": t.string().optional(),
            "vars": t.struct({"_": t.string().optional()}).optional(),
            "defaultSchema": t.string().optional(),
            "defaultDatabase": t.string().optional(),
            "defaultLocation": t.string().optional(),
            "schemaSuffix": t.string().optional(),
        }
    ).named(renames["CodeCompilationConfigIn"])
    types["CodeCompilationConfigOut"] = t.struct(
        {
            "tablePrefix": t.string().optional(),
            "databaseSuffix": t.string().optional(),
            "assertionSchema": t.string().optional(),
            "vars": t.struct({"_": t.string().optional()}).optional(),
            "defaultSchema": t.string().optional(),
            "defaultDatabase": t.string().optional(),
            "defaultLocation": t.string().optional(),
            "schemaSuffix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CodeCompilationConfigOut"])
    types["ListCompilationResultsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "compilationResults": t.array(
                t.proxy(renames["CompilationResultIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListCompilationResultsResponseIn"])
    types["ListCompilationResultsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "compilationResults": t.array(
                t.proxy(renames["CompilationResultOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCompilationResultsResponseOut"])
    types["ScheduledExecutionRecordIn"] = t.struct(
        {
            "errorStatus": t.proxy(renames["StatusIn"]).optional(),
            "workflowInvocation": t.string().optional(),
            "executionTime": t.string().optional(),
        }
    ).named(renames["ScheduledExecutionRecordIn"])
    types["ScheduledExecutionRecordOut"] = t.struct(
        {
            "errorStatus": t.proxy(renames["StatusOut"]).optional(),
            "workflowInvocation": t.string().optional(),
            "executionTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduledExecutionRecordOut"])
    types["ReleaseConfigIn"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "releaseCompilationResult": t.string().optional(),
            "gitCommitish": t.string(),
            "codeCompilationConfig": t.proxy(
                renames["CodeCompilationConfigIn"]
            ).optional(),
            "cronSchedule": t.string().optional(),
        }
    ).named(renames["ReleaseConfigIn"])
    types["ReleaseConfigOut"] = t.struct(
        {
            "recentScheduledReleaseRecords": t.array(
                t.proxy(renames["ScheduledReleaseRecordOut"])
            ).optional(),
            "timeZone": t.string().optional(),
            "name": t.string().optional(),
            "releaseCompilationResult": t.string().optional(),
            "gitCommitish": t.string(),
            "codeCompilationConfig": t.proxy(
                renames["CodeCompilationConfigOut"]
            ).optional(),
            "cronSchedule": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseConfigOut"])
    types["RelationDescriptorIn"] = t.struct(
        {
            "columns": t.array(t.proxy(renames["ColumnDescriptorIn"])).optional(),
            "description": t.string().optional(),
            "bigqueryLabels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RelationDescriptorIn"])
    types["RelationDescriptorOut"] = t.struct(
        {
            "columns": t.array(t.proxy(renames["ColumnDescriptorOut"])).optional(),
            "description": t.string().optional(),
            "bigqueryLabels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationDescriptorOut"])
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
    types["TargetIn"] = t.struct(
        {
            "name": t.string().optional(),
            "schema": t.string().optional(),
            "database": t.string().optional(),
        }
    ).named(renames["TargetIn"])
    types["TargetOut"] = t.struct(
        {
            "name": t.string().optional(),
            "schema": t.string().optional(),
            "database": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetOut"])
    types["MakeDirectoryResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MakeDirectoryResponseIn"]
    )
    types["MakeDirectoryResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MakeDirectoryResponseOut"])
    types["CompilationResultActionIn"] = t.struct(
        {
            "filePath": t.string().optional(),
            "canonicalTarget": t.proxy(renames["TargetIn"]).optional(),
            "operations": t.proxy(renames["OperationsIn"]).optional(),
            "assertion": t.proxy(renames["AssertionIn"]).optional(),
            "target": t.proxy(renames["TargetIn"]).optional(),
            "declaration": t.proxy(renames["DeclarationIn"]).optional(),
            "relation": t.proxy(renames["RelationIn"]).optional(),
        }
    ).named(renames["CompilationResultActionIn"])
    types["CompilationResultActionOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "canonicalTarget": t.proxy(renames["TargetOut"]).optional(),
            "operations": t.proxy(renames["OperationsOut"]).optional(),
            "assertion": t.proxy(renames["AssertionOut"]).optional(),
            "target": t.proxy(renames["TargetOut"]).optional(),
            "declaration": t.proxy(renames["DeclarationOut"]).optional(),
            "relation": t.proxy(renames["RelationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompilationResultActionOut"])
    types["InstallNpmPackagesRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["InstallNpmPackagesRequestIn"]
    )
    types["InstallNpmPackagesRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InstallNpmPackagesRequestOut"])
    types["DirectoryEntryIn"] = t.struct(
        {"directory": t.string().optional(), "file": t.string().optional()}
    ).named(renames["DirectoryEntryIn"])
    types["DirectoryEntryOut"] = t.struct(
        {
            "directory": t.string().optional(),
            "file": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DirectoryEntryOut"])
    types["PullGitCommitsRequestIn"] = t.struct(
        {
            "remoteBranch": t.string().optional(),
            "author": t.proxy(renames["CommitAuthorIn"]),
        }
    ).named(renames["PullGitCommitsRequestIn"])
    types["PullGitCommitsRequestOut"] = t.struct(
        {
            "remoteBranch": t.string().optional(),
            "author": t.proxy(renames["CommitAuthorOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PullGitCommitsRequestOut"])
    types["RelationIn"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "preOperations": t.array(t.string()).optional(),
            "selectQuery": t.string().optional(),
            "clusterExpressions": t.array(t.string()).optional(),
            "requirePartitionFilter": t.boolean().optional(),
            "tags": t.array(t.string()).optional(),
            "additionalOptions": t.struct({"_": t.string().optional()}).optional(),
            "relationType": t.string().optional(),
            "dependencyTargets": t.array(t.proxy(renames["TargetIn"])).optional(),
            "partitionExpression": t.string().optional(),
            "incrementalTableConfig": t.proxy(
                renames["IncrementalTableConfigIn"]
            ).optional(),
            "relationDescriptor": t.proxy(renames["RelationDescriptorIn"]).optional(),
            "partitionExpirationDays": t.integer().optional(),
            "postOperations": t.array(t.string()).optional(),
        }
    ).named(renames["RelationIn"])
    types["RelationOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "preOperations": t.array(t.string()).optional(),
            "selectQuery": t.string().optional(),
            "clusterExpressions": t.array(t.string()).optional(),
            "requirePartitionFilter": t.boolean().optional(),
            "tags": t.array(t.string()).optional(),
            "additionalOptions": t.struct({"_": t.string().optional()}).optional(),
            "relationType": t.string().optional(),
            "dependencyTargets": t.array(t.proxy(renames["TargetOut"])).optional(),
            "partitionExpression": t.string().optional(),
            "incrementalTableConfig": t.proxy(
                renames["IncrementalTableConfigOut"]
            ).optional(),
            "relationDescriptor": t.proxy(renames["RelationDescriptorOut"]).optional(),
            "partitionExpirationDays": t.integer().optional(),
            "postOperations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationOut"])
    types["RemoveDirectoryRequestIn"] = t.struct({"path": t.string()}).named(
        renames["RemoveDirectoryRequestIn"]
    )
    types["RemoveDirectoryRequestOut"] = t.struct(
        {"path": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveDirectoryRequestOut"])

    functions = {}
    functions["projectsLocationsList"] = dataform.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = dataform.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesGet"] = dataform.get(
        "v1beta1/{name}:computeAccessTokenStatus",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ComputeRepositoryAccessTokenStatusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesList"] = dataform.get(
        "v1beta1/{name}:computeAccessTokenStatus",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ComputeRepositoryAccessTokenStatusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesCreate"] = dataform.get(
        "v1beta1/{name}:computeAccessTokenStatus",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ComputeRepositoryAccessTokenStatusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesSetIamPolicy"] = dataform.get(
        "v1beta1/{name}:computeAccessTokenStatus",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ComputeRepositoryAccessTokenStatusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesTestIamPermissions"] = dataform.get(
        "v1beta1/{name}:computeAccessTokenStatus",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ComputeRepositoryAccessTokenStatusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesPatch"] = dataform.get(
        "v1beta1/{name}:computeAccessTokenStatus",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ComputeRepositoryAccessTokenStatusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesFetchRemoteBranches"] = dataform.get(
        "v1beta1/{name}:computeAccessTokenStatus",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ComputeRepositoryAccessTokenStatusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesGetIamPolicy"] = dataform.get(
        "v1beta1/{name}:computeAccessTokenStatus",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ComputeRepositoryAccessTokenStatusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesDelete"] = dataform.get(
        "v1beta1/{name}:computeAccessTokenStatus",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ComputeRepositoryAccessTokenStatusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesComputeAccessTokenStatus"] = dataform.get(
        "v1beta1/{name}:computeAccessTokenStatus",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ComputeRepositoryAccessTokenStatusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkflowInvocationsGet"] = dataform.get(
        "v1beta1/{name}:query",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryWorkflowInvocationActionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkflowInvocationsList"] = dataform.get(
        "v1beta1/{name}:query",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryWorkflowInvocationActionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkflowInvocationsCreate"] = dataform.get(
        "v1beta1/{name}:query",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryWorkflowInvocationActionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkflowInvocationsCancel"] = dataform.get(
        "v1beta1/{name}:query",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryWorkflowInvocationActionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkflowInvocationsDelete"] = dataform.get(
        "v1beta1/{name}:query",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryWorkflowInvocationActionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkflowInvocationsQuery"] = dataform.get(
        "v1beta1/{name}:query",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryWorkflowInvocationActionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesCompilationResultsGet"] = dataform.get(
        "v1beta1/{name}:query",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryCompilationResultActionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesCompilationResultsList"] = dataform.get(
        "v1beta1/{name}:query",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryCompilationResultActionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesCompilationResultsCreate"] = dataform.get(
        "v1beta1/{name}:query",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryCompilationResultActionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesCompilationResultsQuery"] = dataform.get(
        "v1beta1/{name}:query",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryCompilationResultActionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkflowConfigsGet"] = dataform.get(
        "v1beta1/{parent}/workflowConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkflowConfigsDelete"] = dataform.get(
        "v1beta1/{parent}/workflowConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkflowConfigsPatch"] = dataform.get(
        "v1beta1/{parent}/workflowConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkflowConfigsCreate"] = dataform.get(
        "v1beta1/{parent}/workflowConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkflowConfigsList"] = dataform.get(
        "v1beta1/{parent}/workflowConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesMoveDirectory"] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions["projectsLocationsRepositoriesWorkspacesMakeDirectory"] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions["projectsLocationsRepositoriesWorkspacesWriteFile"] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions[
        "projectsLocationsRepositoriesWorkspacesInstallNpmPackages"
    ] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions["projectsLocationsRepositoriesWorkspacesRemoveFile"] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions[
        "projectsLocationsRepositoriesWorkspacesTestIamPermissions"
    ] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions["projectsLocationsRepositoriesWorkspacesPush"] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions["projectsLocationsRepositoriesWorkspacesGetIamPolicy"] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions["projectsLocationsRepositoriesWorkspacesPull"] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions["projectsLocationsRepositoriesWorkspacesMoveFile"] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions["projectsLocationsRepositoriesWorkspacesGet"] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions[
        "projectsLocationsRepositoriesWorkspacesQueryDirectoryContents"
    ] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions["projectsLocationsRepositoriesWorkspacesCommit"] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions["projectsLocationsRepositoriesWorkspacesList"] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions["projectsLocationsRepositoriesWorkspacesFetchFileDiff"] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions["projectsLocationsRepositoriesWorkspacesReset"] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions["projectsLocationsRepositoriesWorkspacesDelete"] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions[
        "projectsLocationsRepositoriesWorkspacesFetchGitAheadBehind"
    ] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions[
        "projectsLocationsRepositoriesWorkspacesFetchFileGitStatuses"
    ] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions["projectsLocationsRepositoriesWorkspacesReadFile"] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions["projectsLocationsRepositoriesWorkspacesRemoveDirectory"] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions["projectsLocationsRepositoriesWorkspacesCreate"] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions["projectsLocationsRepositoriesWorkspacesSetIamPolicy"] = dataform.post(
        "v1beta1/{resource}:setIamPolicy",
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
    functions["projectsLocationsRepositoriesReleaseConfigsCreate"] = dataform.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesReleaseConfigsGet"] = dataform.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesReleaseConfigsList"] = dataform.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesReleaseConfigsPatch"] = dataform.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesReleaseConfigsDelete"] = dataform.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="dataform", renames=renames, types=Box(types), functions=Box(functions)
    )
