from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_dataform():
    dataform = HTTPRuntime("https://dataform.googleapis.com/")

    renames = {
        "ErrorResponse": "_dataform_1_ErrorResponse",
        "StatusIn": "_dataform_2_StatusIn",
        "StatusOut": "_dataform_3_StatusOut",
        "WriteFileResponseIn": "_dataform_4_WriteFileResponseIn",
        "WriteFileResponseOut": "_dataform_5_WriteFileResponseOut",
        "RepositoryIn": "_dataform_6_RepositoryIn",
        "RepositoryOut": "_dataform_7_RepositoryOut",
        "CodeCompilationConfigIn": "_dataform_8_CodeCompilationConfigIn",
        "CodeCompilationConfigOut": "_dataform_9_CodeCompilationConfigOut",
        "RelationDescriptorIn": "_dataform_10_RelationDescriptorIn",
        "RelationDescriptorOut": "_dataform_11_RelationDescriptorOut",
        "SetIamPolicyRequestIn": "_dataform_12_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_dataform_13_SetIamPolicyRequestOut",
        "ListWorkflowConfigsResponseIn": "_dataform_14_ListWorkflowConfigsResponseIn",
        "ListWorkflowConfigsResponseOut": "_dataform_15_ListWorkflowConfigsResponseOut",
        "QueryDirectoryContentsResponseIn": "_dataform_16_QueryDirectoryContentsResponseIn",
        "QueryDirectoryContentsResponseOut": "_dataform_17_QueryDirectoryContentsResponseOut",
        "MoveDirectoryResponseIn": "_dataform_18_MoveDirectoryResponseIn",
        "MoveDirectoryResponseOut": "_dataform_19_MoveDirectoryResponseOut",
        "TestIamPermissionsResponseIn": "_dataform_20_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_dataform_21_TestIamPermissionsResponseOut",
        "PullGitCommitsRequestIn": "_dataform_22_PullGitCommitsRequestIn",
        "PullGitCommitsRequestOut": "_dataform_23_PullGitCommitsRequestOut",
        "LocationIn": "_dataform_24_LocationIn",
        "LocationOut": "_dataform_25_LocationOut",
        "DirectoryEntryIn": "_dataform_26_DirectoryEntryIn",
        "DirectoryEntryOut": "_dataform_27_DirectoryEntryOut",
        "QueryWorkflowInvocationActionsResponseIn": "_dataform_28_QueryWorkflowInvocationActionsResponseIn",
        "QueryWorkflowInvocationActionsResponseOut": "_dataform_29_QueryWorkflowInvocationActionsResponseOut",
        "BindingIn": "_dataform_30_BindingIn",
        "BindingOut": "_dataform_31_BindingOut",
        "UncommittedFileChangeIn": "_dataform_32_UncommittedFileChangeIn",
        "UncommittedFileChangeOut": "_dataform_33_UncommittedFileChangeOut",
        "ScheduledReleaseRecordIn": "_dataform_34_ScheduledReleaseRecordIn",
        "ScheduledReleaseRecordOut": "_dataform_35_ScheduledReleaseRecordOut",
        "DeclarationIn": "_dataform_36_DeclarationIn",
        "DeclarationOut": "_dataform_37_DeclarationOut",
        "PushGitCommitsRequestIn": "_dataform_38_PushGitCommitsRequestIn",
        "PushGitCommitsRequestOut": "_dataform_39_PushGitCommitsRequestOut",
        "BigQueryActionIn": "_dataform_40_BigQueryActionIn",
        "BigQueryActionOut": "_dataform_41_BigQueryActionOut",
        "TestIamPermissionsRequestIn": "_dataform_42_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_dataform_43_TestIamPermissionsRequestOut",
        "FetchFileGitStatusesResponseIn": "_dataform_44_FetchFileGitStatusesResponseIn",
        "FetchFileGitStatusesResponseOut": "_dataform_45_FetchFileGitStatusesResponseOut",
        "IntervalIn": "_dataform_46_IntervalIn",
        "IntervalOut": "_dataform_47_IntervalOut",
        "MoveFileRequestIn": "_dataform_48_MoveFileRequestIn",
        "MoveFileRequestOut": "_dataform_49_MoveFileRequestOut",
        "QueryCompilationResultActionsResponseIn": "_dataform_50_QueryCompilationResultActionsResponseIn",
        "QueryCompilationResultActionsResponseOut": "_dataform_51_QueryCompilationResultActionsResponseOut",
        "ListRepositoriesResponseIn": "_dataform_52_ListRepositoriesResponseIn",
        "ListRepositoriesResponseOut": "_dataform_53_ListRepositoriesResponseOut",
        "PolicyIn": "_dataform_54_PolicyIn",
        "PolicyOut": "_dataform_55_PolicyOut",
        "GitRemoteSettingsIn": "_dataform_56_GitRemoteSettingsIn",
        "GitRemoteSettingsOut": "_dataform_57_GitRemoteSettingsOut",
        "OperationsIn": "_dataform_58_OperationsIn",
        "OperationsOut": "_dataform_59_OperationsOut",
        "WorkflowInvocationActionIn": "_dataform_60_WorkflowInvocationActionIn",
        "WorkflowInvocationActionOut": "_dataform_61_WorkflowInvocationActionOut",
        "CompilationResultActionIn": "_dataform_62_CompilationResultActionIn",
        "CompilationResultActionOut": "_dataform_63_CompilationResultActionOut",
        "ResetWorkspaceChangesRequestIn": "_dataform_64_ResetWorkspaceChangesRequestIn",
        "ResetWorkspaceChangesRequestOut": "_dataform_65_ResetWorkspaceChangesRequestOut",
        "CommitAuthorIn": "_dataform_66_CommitAuthorIn",
        "CommitAuthorOut": "_dataform_67_CommitAuthorOut",
        "InvocationConfigIn": "_dataform_68_InvocationConfigIn",
        "InvocationConfigOut": "_dataform_69_InvocationConfigOut",
        "ListCompilationResultsResponseIn": "_dataform_70_ListCompilationResultsResponseIn",
        "ListCompilationResultsResponseOut": "_dataform_71_ListCompilationResultsResponseOut",
        "ReadFileResponseIn": "_dataform_72_ReadFileResponseIn",
        "ReadFileResponseOut": "_dataform_73_ReadFileResponseOut",
        "TargetIn": "_dataform_74_TargetIn",
        "TargetOut": "_dataform_75_TargetOut",
        "WorkspaceCompilationOverridesIn": "_dataform_76_WorkspaceCompilationOverridesIn",
        "WorkspaceCompilationOverridesOut": "_dataform_77_WorkspaceCompilationOverridesOut",
        "ListWorkspacesResponseIn": "_dataform_78_ListWorkspacesResponseIn",
        "ListWorkspacesResponseOut": "_dataform_79_ListWorkspacesResponseOut",
        "MakeDirectoryResponseIn": "_dataform_80_MakeDirectoryResponseIn",
        "MakeDirectoryResponseOut": "_dataform_81_MakeDirectoryResponseOut",
        "CancelWorkflowInvocationRequestIn": "_dataform_82_CancelWorkflowInvocationRequestIn",
        "CancelWorkflowInvocationRequestOut": "_dataform_83_CancelWorkflowInvocationRequestOut",
        "InstallNpmPackagesResponseIn": "_dataform_84_InstallNpmPackagesResponseIn",
        "InstallNpmPackagesResponseOut": "_dataform_85_InstallNpmPackagesResponseOut",
        "ListReleaseConfigsResponseIn": "_dataform_86_ListReleaseConfigsResponseIn",
        "ListReleaseConfigsResponseOut": "_dataform_87_ListReleaseConfigsResponseOut",
        "ComputeRepositoryAccessTokenStatusResponseIn": "_dataform_88_ComputeRepositoryAccessTokenStatusResponseIn",
        "ComputeRepositoryAccessTokenStatusResponseOut": "_dataform_89_ComputeRepositoryAccessTokenStatusResponseOut",
        "ListWorkflowInvocationsResponseIn": "_dataform_90_ListWorkflowInvocationsResponseIn",
        "ListWorkflowInvocationsResponseOut": "_dataform_91_ListWorkflowInvocationsResponseOut",
        "FetchRemoteBranchesResponseIn": "_dataform_92_FetchRemoteBranchesResponseIn",
        "FetchRemoteBranchesResponseOut": "_dataform_93_FetchRemoteBranchesResponseOut",
        "RemoveFileRequestIn": "_dataform_94_RemoveFileRequestIn",
        "RemoveFileRequestOut": "_dataform_95_RemoveFileRequestOut",
        "FetchGitAheadBehindResponseIn": "_dataform_96_FetchGitAheadBehindResponseIn",
        "FetchGitAheadBehindResponseOut": "_dataform_97_FetchGitAheadBehindResponseOut",
        "MakeDirectoryRequestIn": "_dataform_98_MakeDirectoryRequestIn",
        "MakeDirectoryRequestOut": "_dataform_99_MakeDirectoryRequestOut",
        "WorkspaceIn": "_dataform_100_WorkspaceIn",
        "WorkspaceOut": "_dataform_101_WorkspaceOut",
        "ExprIn": "_dataform_102_ExprIn",
        "ExprOut": "_dataform_103_ExprOut",
        "IncrementalTableConfigIn": "_dataform_104_IncrementalTableConfigIn",
        "IncrementalTableConfigOut": "_dataform_105_IncrementalTableConfigOut",
        "InstallNpmPackagesRequestIn": "_dataform_106_InstallNpmPackagesRequestIn",
        "InstallNpmPackagesRequestOut": "_dataform_107_InstallNpmPackagesRequestOut",
        "CompilationErrorIn": "_dataform_108_CompilationErrorIn",
        "CompilationErrorOut": "_dataform_109_CompilationErrorOut",
        "ScheduledExecutionRecordIn": "_dataform_110_ScheduledExecutionRecordIn",
        "ScheduledExecutionRecordOut": "_dataform_111_ScheduledExecutionRecordOut",
        "MoveFileResponseIn": "_dataform_112_MoveFileResponseIn",
        "MoveFileResponseOut": "_dataform_113_MoveFileResponseOut",
        "WorkflowInvocationIn": "_dataform_114_WorkflowInvocationIn",
        "WorkflowInvocationOut": "_dataform_115_WorkflowInvocationOut",
        "CompilationResultIn": "_dataform_116_CompilationResultIn",
        "CompilationResultOut": "_dataform_117_CompilationResultOut",
        "WorkflowConfigIn": "_dataform_118_WorkflowConfigIn",
        "WorkflowConfigOut": "_dataform_119_WorkflowConfigOut",
        "EmptyIn": "_dataform_120_EmptyIn",
        "EmptyOut": "_dataform_121_EmptyOut",
        "ListLocationsResponseIn": "_dataform_122_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_dataform_123_ListLocationsResponseOut",
        "RemoveDirectoryRequestIn": "_dataform_124_RemoveDirectoryRequestIn",
        "RemoveDirectoryRequestOut": "_dataform_125_RemoveDirectoryRequestOut",
        "ColumnDescriptorIn": "_dataform_126_ColumnDescriptorIn",
        "ColumnDescriptorOut": "_dataform_127_ColumnDescriptorOut",
        "RelationIn": "_dataform_128_RelationIn",
        "RelationOut": "_dataform_129_RelationOut",
        "CommitWorkspaceChangesRequestIn": "_dataform_130_CommitWorkspaceChangesRequestIn",
        "CommitWorkspaceChangesRequestOut": "_dataform_131_CommitWorkspaceChangesRequestOut",
        "WriteFileRequestIn": "_dataform_132_WriteFileRequestIn",
        "WriteFileRequestOut": "_dataform_133_WriteFileRequestOut",
        "MoveDirectoryRequestIn": "_dataform_134_MoveDirectoryRequestIn",
        "MoveDirectoryRequestOut": "_dataform_135_MoveDirectoryRequestOut",
        "AssertionIn": "_dataform_136_AssertionIn",
        "AssertionOut": "_dataform_137_AssertionOut",
        "ReleaseConfigIn": "_dataform_138_ReleaseConfigIn",
        "ReleaseConfigOut": "_dataform_139_ReleaseConfigOut",
        "OperationMetadataIn": "_dataform_140_OperationMetadataIn",
        "OperationMetadataOut": "_dataform_141_OperationMetadataOut",
        "FetchFileDiffResponseIn": "_dataform_142_FetchFileDiffResponseIn",
        "FetchFileDiffResponseOut": "_dataform_143_FetchFileDiffResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["WriteFileResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WriteFileResponseIn"]
    )
    types["WriteFileResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WriteFileResponseOut"])
    types["RepositoryIn"] = t.struct(
        {
            "gitRemoteSettings": t.proxy(renames["GitRemoteSettingsIn"]).optional(),
            "npmrcEnvironmentVariablesSecretVersion": t.string().optional(),
            "workspaceCompilationOverrides": t.proxy(
                renames["WorkspaceCompilationOverridesIn"]
            ).optional(),
        }
    ).named(renames["RepositoryIn"])
    types["RepositoryOut"] = t.struct(
        {
            "gitRemoteSettings": t.proxy(renames["GitRemoteSettingsOut"]).optional(),
            "name": t.string().optional(),
            "npmrcEnvironmentVariablesSecretVersion": t.string().optional(),
            "workspaceCompilationOverrides": t.proxy(
                renames["WorkspaceCompilationOverridesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepositoryOut"])
    types["CodeCompilationConfigIn"] = t.struct(
        {
            "defaultDatabase": t.string().optional(),
            "assertionSchema": t.string().optional(),
            "schemaSuffix": t.string().optional(),
            "defaultSchema": t.string().optional(),
            "tablePrefix": t.string().optional(),
            "databaseSuffix": t.string().optional(),
            "defaultLocation": t.string().optional(),
            "vars": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CodeCompilationConfigIn"])
    types["CodeCompilationConfigOut"] = t.struct(
        {
            "defaultDatabase": t.string().optional(),
            "assertionSchema": t.string().optional(),
            "schemaSuffix": t.string().optional(),
            "defaultSchema": t.string().optional(),
            "tablePrefix": t.string().optional(),
            "databaseSuffix": t.string().optional(),
            "defaultLocation": t.string().optional(),
            "vars": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CodeCompilationConfigOut"])
    types["RelationDescriptorIn"] = t.struct(
        {
            "bigqueryLabels": t.struct({"_": t.string().optional()}).optional(),
            "columns": t.array(t.proxy(renames["ColumnDescriptorIn"])).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["RelationDescriptorIn"])
    types["RelationDescriptorOut"] = t.struct(
        {
            "bigqueryLabels": t.struct({"_": t.string().optional()}).optional(),
            "columns": t.array(t.proxy(renames["ColumnDescriptorOut"])).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationDescriptorOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["ListWorkflowConfigsResponseIn"] = t.struct(
        {
            "workflowConfigs": t.array(t.proxy(renames["WorkflowConfigIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListWorkflowConfigsResponseIn"])
    types["ListWorkflowConfigsResponseOut"] = t.struct(
        {
            "workflowConfigs": t.array(
                t.proxy(renames["WorkflowConfigOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkflowConfigsResponseOut"])
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
    types["MoveDirectoryResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MoveDirectoryResponseIn"]
    )
    types["MoveDirectoryResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MoveDirectoryResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["PullGitCommitsRequestIn"] = t.struct(
        {
            "author": t.proxy(renames["CommitAuthorIn"]),
            "remoteBranch": t.string().optional(),
        }
    ).named(renames["PullGitCommitsRequestIn"])
    types["PullGitCommitsRequestOut"] = t.struct(
        {
            "author": t.proxy(renames["CommitAuthorOut"]),
            "remoteBranch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PullGitCommitsRequestOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["DirectoryEntryIn"] = t.struct(
        {"file": t.string().optional(), "directory": t.string().optional()}
    ).named(renames["DirectoryEntryIn"])
    types["DirectoryEntryOut"] = t.struct(
        {
            "file": t.string().optional(),
            "directory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DirectoryEntryOut"])
    types["QueryWorkflowInvocationActionsResponseIn"] = t.struct(
        {
            "workflowInvocationActions": t.array(
                t.proxy(renames["WorkflowInvocationActionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["QueryWorkflowInvocationActionsResponseIn"])
    types["QueryWorkflowInvocationActionsResponseOut"] = t.struct(
        {
            "workflowInvocationActions": t.array(
                t.proxy(renames["WorkflowInvocationActionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryWorkflowInvocationActionsResponseOut"])
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
    types["UncommittedFileChangeIn"] = t.struct(
        {"path": t.string().optional(), "state": t.string().optional()}
    ).named(renames["UncommittedFileChangeIn"])
    types["UncommittedFileChangeOut"] = t.struct(
        {
            "path": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UncommittedFileChangeOut"])
    types["ScheduledReleaseRecordIn"] = t.struct(
        {
            "errorStatus": t.proxy(renames["StatusIn"]).optional(),
            "releaseTime": t.string().optional(),
            "compilationResult": t.string().optional(),
        }
    ).named(renames["ScheduledReleaseRecordIn"])
    types["ScheduledReleaseRecordOut"] = t.struct(
        {
            "errorStatus": t.proxy(renames["StatusOut"]).optional(),
            "releaseTime": t.string().optional(),
            "compilationResult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduledReleaseRecordOut"])
    types["DeclarationIn"] = t.struct(
        {"relationDescriptor": t.proxy(renames["RelationDescriptorIn"]).optional()}
    ).named(renames["DeclarationIn"])
    types["DeclarationOut"] = t.struct(
        {
            "relationDescriptor": t.proxy(renames["RelationDescriptorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeclarationOut"])
    types["PushGitCommitsRequestIn"] = t.struct(
        {"remoteBranch": t.string().optional()}
    ).named(renames["PushGitCommitsRequestIn"])
    types["PushGitCommitsRequestOut"] = t.struct(
        {
            "remoteBranch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PushGitCommitsRequestOut"])
    types["BigQueryActionIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BigQueryActionIn"]
    )
    types["BigQueryActionOut"] = t.struct(
        {
            "sqlScript": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryActionOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["IntervalIn"] = t.struct(
        {"endTime": t.string().optional(), "startTime": t.string().optional()}
    ).named(renames["IntervalIn"])
    types["IntervalOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntervalOut"])
    types["MoveFileRequestIn"] = t.struct(
        {"newPath": t.string(), "path": t.string()}
    ).named(renames["MoveFileRequestIn"])
    types["MoveFileRequestOut"] = t.struct(
        {
            "newPath": t.string(),
            "path": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveFileRequestOut"])
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
    types["ListRepositoriesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "repositories": t.array(t.proxy(renames["RepositoryIn"])).optional(),
        }
    ).named(renames["ListRepositoriesResponseIn"])
    types["ListRepositoriesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "repositories": t.array(t.proxy(renames["RepositoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRepositoriesResponseOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["GitRemoteSettingsIn"] = t.struct(
        {
            "authenticationTokenSecretVersion": t.string(),
            "url": t.string(),
            "defaultBranch": t.string(),
        }
    ).named(renames["GitRemoteSettingsIn"])
    types["GitRemoteSettingsOut"] = t.struct(
        {
            "authenticationTokenSecretVersion": t.string(),
            "tokenStatus": t.string().optional(),
            "url": t.string(),
            "defaultBranch": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitRemoteSettingsOut"])
    types["OperationsIn"] = t.struct(
        {
            "hasOutput": t.boolean().optional(),
            "relationDescriptor": t.proxy(renames["RelationDescriptorIn"]).optional(),
            "queries": t.array(t.string()).optional(),
            "disabled": t.boolean().optional(),
            "tags": t.array(t.string()).optional(),
            "dependencyTargets": t.array(t.proxy(renames["TargetIn"])).optional(),
        }
    ).named(renames["OperationsIn"])
    types["OperationsOut"] = t.struct(
        {
            "hasOutput": t.boolean().optional(),
            "relationDescriptor": t.proxy(renames["RelationDescriptorOut"]).optional(),
            "queries": t.array(t.string()).optional(),
            "disabled": t.boolean().optional(),
            "tags": t.array(t.string()).optional(),
            "dependencyTargets": t.array(t.proxy(renames["TargetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationsOut"])
    types["WorkflowInvocationActionIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WorkflowInvocationActionIn"]
    )
    types["WorkflowInvocationActionOut"] = t.struct(
        {
            "bigqueryAction": t.proxy(renames["BigQueryActionOut"]).optional(),
            "failureReason": t.string().optional(),
            "state": t.string().optional(),
            "target": t.proxy(renames["TargetOut"]).optional(),
            "canonicalTarget": t.proxy(renames["TargetOut"]).optional(),
            "invocationTiming": t.proxy(renames["IntervalOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowInvocationActionOut"])
    types["CompilationResultActionIn"] = t.struct(
        {
            "target": t.proxy(renames["TargetIn"]).optional(),
            "relation": t.proxy(renames["RelationIn"]).optional(),
            "operations": t.proxy(renames["OperationsIn"]).optional(),
            "declaration": t.proxy(renames["DeclarationIn"]).optional(),
            "canonicalTarget": t.proxy(renames["TargetIn"]).optional(),
            "filePath": t.string().optional(),
            "assertion": t.proxy(renames["AssertionIn"]).optional(),
        }
    ).named(renames["CompilationResultActionIn"])
    types["CompilationResultActionOut"] = t.struct(
        {
            "target": t.proxy(renames["TargetOut"]).optional(),
            "relation": t.proxy(renames["RelationOut"]).optional(),
            "operations": t.proxy(renames["OperationsOut"]).optional(),
            "declaration": t.proxy(renames["DeclarationOut"]).optional(),
            "canonicalTarget": t.proxy(renames["TargetOut"]).optional(),
            "filePath": t.string().optional(),
            "assertion": t.proxy(renames["AssertionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompilationResultActionOut"])
    types["ResetWorkspaceChangesRequestIn"] = t.struct(
        {"clean": t.boolean().optional(), "paths": t.array(t.string()).optional()}
    ).named(renames["ResetWorkspaceChangesRequestIn"])
    types["ResetWorkspaceChangesRequestOut"] = t.struct(
        {
            "clean": t.boolean().optional(),
            "paths": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResetWorkspaceChangesRequestOut"])
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
    types["InvocationConfigIn"] = t.struct(
        {
            "transitiveDependentsIncluded": t.boolean().optional(),
            "transitiveDependenciesIncluded": t.boolean().optional(),
            "includedTags": t.array(t.string()).optional(),
            "includedTargets": t.array(t.proxy(renames["TargetIn"])).optional(),
            "fullyRefreshIncrementalTablesEnabled": t.boolean().optional(),
        }
    ).named(renames["InvocationConfigIn"])
    types["InvocationConfigOut"] = t.struct(
        {
            "transitiveDependentsIncluded": t.boolean().optional(),
            "transitiveDependenciesIncluded": t.boolean().optional(),
            "includedTags": t.array(t.string()).optional(),
            "includedTargets": t.array(t.proxy(renames["TargetOut"])).optional(),
            "fullyRefreshIncrementalTablesEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvocationConfigOut"])
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
    types["ReadFileResponseIn"] = t.struct(
        {"fileContents": t.string().optional()}
    ).named(renames["ReadFileResponseIn"])
    types["ReadFileResponseOut"] = t.struct(
        {
            "fileContents": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadFileResponseOut"])
    types["TargetIn"] = t.struct(
        {
            "database": t.string().optional(),
            "schema": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TargetIn"])
    types["TargetOut"] = t.struct(
        {
            "database": t.string().optional(),
            "schema": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetOut"])
    types["WorkspaceCompilationOverridesIn"] = t.struct(
        {
            "defaultDatabase": t.string().optional(),
            "schemaSuffix": t.string().optional(),
            "tablePrefix": t.string().optional(),
        }
    ).named(renames["WorkspaceCompilationOverridesIn"])
    types["WorkspaceCompilationOverridesOut"] = t.struct(
        {
            "defaultDatabase": t.string().optional(),
            "schemaSuffix": t.string().optional(),
            "tablePrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkspaceCompilationOverridesOut"])
    types["ListWorkspacesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "workspaces": t.array(t.proxy(renames["WorkspaceIn"])).optional(),
        }
    ).named(renames["ListWorkspacesResponseIn"])
    types["ListWorkspacesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "workspaces": t.array(t.proxy(renames["WorkspaceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkspacesResponseOut"])
    types["MakeDirectoryResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MakeDirectoryResponseIn"]
    )
    types["MakeDirectoryResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MakeDirectoryResponseOut"])
    types["CancelWorkflowInvocationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CancelWorkflowInvocationRequestIn"])
    types["CancelWorkflowInvocationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelWorkflowInvocationRequestOut"])
    types["InstallNpmPackagesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["InstallNpmPackagesResponseIn"])
    types["InstallNpmPackagesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InstallNpmPackagesResponseOut"])
    types["ListReleaseConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "releaseConfigs": t.array(t.proxy(renames["ReleaseConfigIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListReleaseConfigsResponseIn"])
    types["ListReleaseConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "releaseConfigs": t.array(t.proxy(renames["ReleaseConfigOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReleaseConfigsResponseOut"])
    types["ComputeRepositoryAccessTokenStatusResponseIn"] = t.struct(
        {"tokenStatus": t.string().optional()}
    ).named(renames["ComputeRepositoryAccessTokenStatusResponseIn"])
    types["ComputeRepositoryAccessTokenStatusResponseOut"] = t.struct(
        {
            "tokenStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeRepositoryAccessTokenStatusResponseOut"])
    types["ListWorkflowInvocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "workflowInvocations": t.array(
                t.proxy(renames["WorkflowInvocationIn"])
            ).optional(),
        }
    ).named(renames["ListWorkflowInvocationsResponseIn"])
    types["ListWorkflowInvocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "workflowInvocations": t.array(
                t.proxy(renames["WorkflowInvocationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkflowInvocationsResponseOut"])
    types["FetchRemoteBranchesResponseIn"] = t.struct(
        {"branches": t.array(t.string()).optional()}
    ).named(renames["FetchRemoteBranchesResponseIn"])
    types["FetchRemoteBranchesResponseOut"] = t.struct(
        {
            "branches": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchRemoteBranchesResponseOut"])
    types["RemoveFileRequestIn"] = t.struct({"path": t.string()}).named(
        renames["RemoveFileRequestIn"]
    )
    types["RemoveFileRequestOut"] = t.struct(
        {"path": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveFileRequestOut"])
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
    types["MakeDirectoryRequestIn"] = t.struct({"path": t.string()}).named(
        renames["MakeDirectoryRequestIn"]
    )
    types["MakeDirectoryRequestOut"] = t.struct(
        {"path": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MakeDirectoryRequestOut"])
    types["WorkspaceIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WorkspaceIn"]
    )
    types["WorkspaceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkspaceOut"])
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
    types["IncrementalTableConfigIn"] = t.struct(
        {
            "uniqueKeyParts": t.array(t.string()).optional(),
            "incrementalPostOperations": t.array(t.string()).optional(),
            "incrementalPreOperations": t.array(t.string()).optional(),
            "updatePartitionFilter": t.string().optional(),
            "incrementalSelectQuery": t.string().optional(),
            "refreshDisabled": t.boolean().optional(),
        }
    ).named(renames["IncrementalTableConfigIn"])
    types["IncrementalTableConfigOut"] = t.struct(
        {
            "uniqueKeyParts": t.array(t.string()).optional(),
            "incrementalPostOperations": t.array(t.string()).optional(),
            "incrementalPreOperations": t.array(t.string()).optional(),
            "updatePartitionFilter": t.string().optional(),
            "incrementalSelectQuery": t.string().optional(),
            "refreshDisabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IncrementalTableConfigOut"])
    types["InstallNpmPackagesRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["InstallNpmPackagesRequestIn"]
    )
    types["InstallNpmPackagesRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InstallNpmPackagesRequestOut"])
    types["CompilationErrorIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CompilationErrorIn"]
    )
    types["CompilationErrorOut"] = t.struct(
        {
            "message": t.string().optional(),
            "path": t.string().optional(),
            "actionTarget": t.proxy(renames["TargetOut"]).optional(),
            "stack": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompilationErrorOut"])
    types["ScheduledExecutionRecordIn"] = t.struct(
        {
            "executionTime": t.string().optional(),
            "workflowInvocation": t.string().optional(),
            "errorStatus": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["ScheduledExecutionRecordIn"])
    types["ScheduledExecutionRecordOut"] = t.struct(
        {
            "executionTime": t.string().optional(),
            "workflowInvocation": t.string().optional(),
            "errorStatus": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduledExecutionRecordOut"])
    types["MoveFileResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MoveFileResponseIn"]
    )
    types["MoveFileResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MoveFileResponseOut"])
    types["WorkflowInvocationIn"] = t.struct(
        {
            "workflowConfig": t.string().optional(),
            "compilationResult": t.string().optional(),
            "invocationConfig": t.proxy(renames["InvocationConfigIn"]).optional(),
        }
    ).named(renames["WorkflowInvocationIn"])
    types["WorkflowInvocationOut"] = t.struct(
        {
            "workflowConfig": t.string().optional(),
            "compilationResult": t.string().optional(),
            "invocationTiming": t.proxy(renames["IntervalOut"]).optional(),
            "name": t.string().optional(),
            "invocationConfig": t.proxy(renames["InvocationConfigOut"]).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowInvocationOut"])
    types["CompilationResultIn"] = t.struct(
        {
            "workspace": t.string().optional(),
            "codeCompilationConfig": t.proxy(
                renames["CodeCompilationConfigIn"]
            ).optional(),
            "gitCommitish": t.string().optional(),
            "releaseConfig": t.string().optional(),
        }
    ).named(renames["CompilationResultIn"])
    types["CompilationResultOut"] = t.struct(
        {
            "compilationErrors": t.array(
                t.proxy(renames["CompilationErrorOut"])
            ).optional(),
            "name": t.string().optional(),
            "dataformCoreVersion": t.string().optional(),
            "resolvedGitCommitSha": t.string().optional(),
            "workspace": t.string().optional(),
            "codeCompilationConfig": t.proxy(
                renames["CodeCompilationConfigOut"]
            ).optional(),
            "gitCommitish": t.string().optional(),
            "releaseConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompilationResultOut"])
    types["WorkflowConfigIn"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "cronSchedule": t.string().optional(),
            "releaseConfig": t.string(),
            "invocationConfig": t.proxy(renames["InvocationConfigIn"]).optional(),
        }
    ).named(renames["WorkflowConfigIn"])
    types["WorkflowConfigOut"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "recentScheduledExecutionRecords": t.array(
                t.proxy(renames["ScheduledExecutionRecordOut"])
            ).optional(),
            "cronSchedule": t.string().optional(),
            "name": t.string().optional(),
            "releaseConfig": t.string(),
            "invocationConfig": t.proxy(renames["InvocationConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["RemoveDirectoryRequestIn"] = t.struct({"path": t.string()}).named(
        renames["RemoveDirectoryRequestIn"]
    )
    types["RemoveDirectoryRequestOut"] = t.struct(
        {"path": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveDirectoryRequestOut"])
    types["ColumnDescriptorIn"] = t.struct(
        {
            "bigqueryPolicyTags": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "path": t.array(t.string()).optional(),
        }
    ).named(renames["ColumnDescriptorIn"])
    types["ColumnDescriptorOut"] = t.struct(
        {
            "bigqueryPolicyTags": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "path": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnDescriptorOut"])
    types["RelationIn"] = t.struct(
        {
            "partitionExpression": t.string().optional(),
            "disabled": t.boolean().optional(),
            "selectQuery": t.string().optional(),
            "requirePartitionFilter": t.boolean().optional(),
            "relationDescriptor": t.proxy(renames["RelationDescriptorIn"]).optional(),
            "tags": t.array(t.string()).optional(),
            "partitionExpirationDays": t.integer().optional(),
            "preOperations": t.array(t.string()).optional(),
            "incrementalTableConfig": t.proxy(
                renames["IncrementalTableConfigIn"]
            ).optional(),
            "dependencyTargets": t.array(t.proxy(renames["TargetIn"])).optional(),
            "postOperations": t.array(t.string()).optional(),
            "additionalOptions": t.struct({"_": t.string().optional()}).optional(),
            "clusterExpressions": t.array(t.string()).optional(),
            "relationType": t.string().optional(),
        }
    ).named(renames["RelationIn"])
    types["RelationOut"] = t.struct(
        {
            "partitionExpression": t.string().optional(),
            "disabled": t.boolean().optional(),
            "selectQuery": t.string().optional(),
            "requirePartitionFilter": t.boolean().optional(),
            "relationDescriptor": t.proxy(renames["RelationDescriptorOut"]).optional(),
            "tags": t.array(t.string()).optional(),
            "partitionExpirationDays": t.integer().optional(),
            "preOperations": t.array(t.string()).optional(),
            "incrementalTableConfig": t.proxy(
                renames["IncrementalTableConfigOut"]
            ).optional(),
            "dependencyTargets": t.array(t.proxy(renames["TargetOut"])).optional(),
            "postOperations": t.array(t.string()).optional(),
            "additionalOptions": t.struct({"_": t.string().optional()}).optional(),
            "clusterExpressions": t.array(t.string()).optional(),
            "relationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationOut"])
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
    types["AssertionIn"] = t.struct(
        {
            "parentAction": t.proxy(renames["TargetIn"]).optional(),
            "selectQuery": t.string().optional(),
            "disabled": t.boolean().optional(),
            "dependencyTargets": t.array(t.proxy(renames["TargetIn"])).optional(),
            "tags": t.array(t.string()).optional(),
            "relationDescriptor": t.proxy(renames["RelationDescriptorIn"]).optional(),
        }
    ).named(renames["AssertionIn"])
    types["AssertionOut"] = t.struct(
        {
            "parentAction": t.proxy(renames["TargetOut"]).optional(),
            "selectQuery": t.string().optional(),
            "disabled": t.boolean().optional(),
            "dependencyTargets": t.array(t.proxy(renames["TargetOut"])).optional(),
            "tags": t.array(t.string()).optional(),
            "relationDescriptor": t.proxy(renames["RelationDescriptorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssertionOut"])
    types["ReleaseConfigIn"] = t.struct(
        {
            "cronSchedule": t.string().optional(),
            "timeZone": t.string().optional(),
            "gitCommitish": t.string(),
            "codeCompilationConfig": t.proxy(
                renames["CodeCompilationConfigIn"]
            ).optional(),
            "releaseCompilationResult": t.string().optional(),
        }
    ).named(renames["ReleaseConfigIn"])
    types["ReleaseConfigOut"] = t.struct(
        {
            "cronSchedule": t.string().optional(),
            "recentScheduledReleaseRecords": t.array(
                t.proxy(renames["ScheduledReleaseRecordOut"])
            ).optional(),
            "timeZone": t.string().optional(),
            "gitCommitish": t.string(),
            "codeCompilationConfig": t.proxy(
                renames["CodeCompilationConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "releaseCompilationResult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseConfigOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "statusDetail": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["FetchFileDiffResponseIn"] = t.struct(
        {"formattedDiff": t.string().optional()}
    ).named(renames["FetchFileDiffResponseIn"])
    types["FetchFileDiffResponseOut"] = t.struct(
        {
            "formattedDiff": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchFileDiffResponseOut"])

    functions = {}
    functions["projectsLocationsGet"] = dataform.get(
        "v1beta1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = dataform.get(
        "v1beta1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesDelete"] = dataform.get(
        "v1beta1/{name}:fetchRemoteBranches",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FetchRemoteBranchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesComputeAccessTokenStatus"] = dataform.get(
        "v1beta1/{name}:fetchRemoteBranches",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FetchRemoteBranchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesCreate"] = dataform.get(
        "v1beta1/{name}:fetchRemoteBranches",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FetchRemoteBranchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesSetIamPolicy"] = dataform.get(
        "v1beta1/{name}:fetchRemoteBranches",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FetchRemoteBranchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesGetIamPolicy"] = dataform.get(
        "v1beta1/{name}:fetchRemoteBranches",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FetchRemoteBranchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesGet"] = dataform.get(
        "v1beta1/{name}:fetchRemoteBranches",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FetchRemoteBranchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesTestIamPermissions"] = dataform.get(
        "v1beta1/{name}:fetchRemoteBranches",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FetchRemoteBranchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesList"] = dataform.get(
        "v1beta1/{name}:fetchRemoteBranches",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FetchRemoteBranchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesPatch"] = dataform.get(
        "v1beta1/{name}:fetchRemoteBranches",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FetchRemoteBranchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesFetchRemoteBranches"] = dataform.get(
        "v1beta1/{name}:fetchRemoteBranches",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FetchRemoteBranchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkflowConfigsPatch"] = dataform.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkflowConfigsList"] = dataform.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkflowConfigsCreate"] = dataform.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkflowConfigsGet"] = dataform.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkflowConfigsDelete"] = dataform.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesReset"] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesMoveDirectory"] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesGetIamPolicy"] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesList"] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesMoveFile"] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesRemoveFile"] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesWorkspacesFetchFileGitStatuses"
    ] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesGet"] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesReadFile"] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesDelete"] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesWorkspacesFetchGitAheadBehind"
    ] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesWorkspacesTestIamPermissions"
    ] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesCreate"] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesWorkspacesInstallNpmPackages"
    ] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesWorkspacesQueryDirectoryContents"
    ] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesFetchFileDiff"] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesSetIamPolicy"] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesWriteFile"] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesCommit"] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesMakeDirectory"] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesRemoveDirectory"] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesPush"] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkspacesPull"] = dataform.post(
        "v1beta1/{name}:pull",
        t.struct(
            {
                "name": t.string(),
                "author": t.proxy(renames["CommitAuthorIn"]),
                "remoteBranch": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesCompilationResultsCreate"] = dataform.get(
        "v1beta1/{name}:query",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "name": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryCompilationResultActionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesCompilationResultsGet"] = dataform.get(
        "v1beta1/{name}:query",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "name": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryCompilationResultActionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkflowInvocationsList"] = dataform.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesWorkflowInvocationsCreate"
    ] = dataform.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesWorkflowInvocationsCancel"
    ] = dataform.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesWorkflowInvocationsGet"] = dataform.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesWorkflowInvocationsQuery"
    ] = dataform.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesWorkflowInvocationsDelete"
    ] = dataform.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesReleaseConfigsCreate"] = dataform.get(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReleaseConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesReleaseConfigsDelete"] = dataform.get(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReleaseConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesReleaseConfigsPatch"] = dataform.get(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReleaseConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesReleaseConfigsList"] = dataform.get(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReleaseConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesReleaseConfigsGet"] = dataform.get(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReleaseConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="dataform", renames=renames, types=Box(types), functions=Box(functions)
    )
