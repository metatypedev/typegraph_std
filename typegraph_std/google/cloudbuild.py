from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_cloudbuild():
    cloudbuild = HTTPRuntime("https://cloudbuild.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudbuild_1_ErrorResponse",
        "GitHubEnterpriseConfigIn": "_cloudbuild_2_GitHubEnterpriseConfigIn",
        "GitHubEnterpriseConfigOut": "_cloudbuild_3_GitHubEnterpriseConfigOut",
        "DeleteWorkerPoolOperationMetadataIn": "_cloudbuild_4_DeleteWorkerPoolOperationMetadataIn",
        "DeleteWorkerPoolOperationMetadataOut": "_cloudbuild_5_DeleteWorkerPoolOperationMetadataOut",
        "RepositoryEventConfigIn": "_cloudbuild_6_RepositoryEventConfigIn",
        "RepositoryEventConfigOut": "_cloudbuild_7_RepositoryEventConfigOut",
        "ApprovalResultIn": "_cloudbuild_8_ApprovalResultIn",
        "ApprovalResultOut": "_cloudbuild_9_ApprovalResultOut",
        "ProcessAppManifestCallbackOperationMetadataIn": "_cloudbuild_10_ProcessAppManifestCallbackOperationMetadataIn",
        "ProcessAppManifestCallbackOperationMetadataOut": "_cloudbuild_11_ProcessAppManifestCallbackOperationMetadataOut",
        "UploadedMavenArtifactIn": "_cloudbuild_12_UploadedMavenArtifactIn",
        "UploadedMavenArtifactOut": "_cloudbuild_13_UploadedMavenArtifactOut",
        "RetryBuildRequestIn": "_cloudbuild_14_RetryBuildRequestIn",
        "RetryBuildRequestOut": "_cloudbuild_15_RetryBuildRequestOut",
        "GitHubEventsConfigIn": "_cloudbuild_16_GitHubEventsConfigIn",
        "GitHubEventsConfigOut": "_cloudbuild_17_GitHubEventsConfigOut",
        "CreateGitLabConfigOperationMetadataIn": "_cloudbuild_18_CreateGitLabConfigOperationMetadataIn",
        "CreateGitLabConfigOperationMetadataOut": "_cloudbuild_19_CreateGitLabConfigOperationMetadataOut",
        "WorkerConfigIn": "_cloudbuild_20_WorkerConfigIn",
        "WorkerConfigOut": "_cloudbuild_21_WorkerConfigOut",
        "RepoSourceIn": "_cloudbuild_22_RepoSourceIn",
        "RepoSourceOut": "_cloudbuild_23_RepoSourceOut",
        "GitRepoSourceIn": "_cloudbuild_24_GitRepoSourceIn",
        "GitRepoSourceOut": "_cloudbuild_25_GitRepoSourceOut",
        "CreateBitbucketServerConnectedRepositoryRequestIn": "_cloudbuild_26_CreateBitbucketServerConnectedRepositoryRequestIn",
        "CreateBitbucketServerConnectedRepositoryRequestOut": "_cloudbuild_27_CreateBitbucketServerConnectedRepositoryRequestOut",
        "GitFileSourceIn": "_cloudbuild_28_GitFileSourceIn",
        "GitFileSourceOut": "_cloudbuild_29_GitFileSourceOut",
        "GitLabRepositoryIn": "_cloudbuild_30_GitLabRepositoryIn",
        "GitLabRepositoryOut": "_cloudbuild_31_GitLabRepositoryOut",
        "ListBitbucketServerRepositoriesResponseIn": "_cloudbuild_32_ListBitbucketServerRepositoriesResponseIn",
        "ListBitbucketServerRepositoriesResponseOut": "_cloudbuild_33_ListBitbucketServerRepositoriesResponseOut",
        "PushFilterIn": "_cloudbuild_34_PushFilterIn",
        "PushFilterOut": "_cloudbuild_35_PushFilterOut",
        "GitLabSecretsIn": "_cloudbuild_36_GitLabSecretsIn",
        "GitLabSecretsOut": "_cloudbuild_37_GitLabSecretsOut",
        "BuildIn": "_cloudbuild_38_BuildIn",
        "BuildOut": "_cloudbuild_39_BuildOut",
        "ApproveBuildRequestIn": "_cloudbuild_40_ApproveBuildRequestIn",
        "ApproveBuildRequestOut": "_cloudbuild_41_ApproveBuildRequestOut",
        "PythonPackageIn": "_cloudbuild_42_PythonPackageIn",
        "PythonPackageOut": "_cloudbuild_43_PythonPackageOut",
        "StorageSourceManifestIn": "_cloudbuild_44_StorageSourceManifestIn",
        "StorageSourceManifestOut": "_cloudbuild_45_StorageSourceManifestOut",
        "CreateGitLabConnectedRepositoryRequestIn": "_cloudbuild_46_CreateGitLabConnectedRepositoryRequestIn",
        "CreateGitLabConnectedRepositoryRequestOut": "_cloudbuild_47_CreateGitLabConnectedRepositoryRequestOut",
        "DeleteGitLabConfigOperationMetadataIn": "_cloudbuild_48_DeleteGitLabConfigOperationMetadataIn",
        "DeleteGitLabConfigOperationMetadataOut": "_cloudbuild_49_DeleteGitLabConfigOperationMetadataOut",
        "PoolOptionIn": "_cloudbuild_50_PoolOptionIn",
        "PoolOptionOut": "_cloudbuild_51_PoolOptionOut",
        "UpdateWorkerPoolOperationMetadataIn": "_cloudbuild_52_UpdateWorkerPoolOperationMetadataIn",
        "UpdateWorkerPoolOperationMetadataOut": "_cloudbuild_53_UpdateWorkerPoolOperationMetadataOut",
        "ListGitLabConfigsResponseIn": "_cloudbuild_54_ListGitLabConfigsResponseIn",
        "ListGitLabConfigsResponseOut": "_cloudbuild_55_ListGitLabConfigsResponseOut",
        "StatusIn": "_cloudbuild_56_StatusIn",
        "StatusOut": "_cloudbuild_57_StatusOut",
        "ArtifactResultIn": "_cloudbuild_58_ArtifactResultIn",
        "ArtifactResultOut": "_cloudbuild_59_ArtifactResultOut",
        "GitLabRepositoryIdIn": "_cloudbuild_60_GitLabRepositoryIdIn",
        "GitLabRepositoryIdOut": "_cloudbuild_61_GitLabRepositoryIdOut",
        "SecretIn": "_cloudbuild_62_SecretIn",
        "SecretOut": "_cloudbuild_63_SecretOut",
        "InlineSecretIn": "_cloudbuild_64_InlineSecretIn",
        "InlineSecretOut": "_cloudbuild_65_InlineSecretOut",
        "ListBitbucketServerConfigsResponseIn": "_cloudbuild_66_ListBitbucketServerConfigsResponseIn",
        "ListBitbucketServerConfigsResponseOut": "_cloudbuild_67_ListBitbucketServerConfigsResponseOut",
        "UpdateBitbucketServerConfigOperationMetadataIn": "_cloudbuild_68_UpdateBitbucketServerConfigOperationMetadataIn",
        "UpdateBitbucketServerConfigOperationMetadataOut": "_cloudbuild_69_UpdateBitbucketServerConfigOperationMetadataOut",
        "BuildApprovalIn": "_cloudbuild_70_BuildApprovalIn",
        "BuildApprovalOut": "_cloudbuild_71_BuildApprovalOut",
        "ListGitLabRepositoriesResponseIn": "_cloudbuild_72_ListGitLabRepositoriesResponseIn",
        "ListGitLabRepositoriesResponseOut": "_cloudbuild_73_ListGitLabRepositoriesResponseOut",
        "BatchCreateBitbucketServerConnectedRepositoriesRequestIn": "_cloudbuild_74_BatchCreateBitbucketServerConnectedRepositoriesRequestIn",
        "BatchCreateBitbucketServerConnectedRepositoriesRequestOut": "_cloudbuild_75_BatchCreateBitbucketServerConnectedRepositoriesRequestOut",
        "DeleteBitbucketServerConfigOperationMetadataIn": "_cloudbuild_76_DeleteBitbucketServerConfigOperationMetadataIn",
        "DeleteBitbucketServerConfigOperationMetadataOut": "_cloudbuild_77_DeleteBitbucketServerConfigOperationMetadataOut",
        "BitbucketServerRepositoryIn": "_cloudbuild_78_BitbucketServerRepositoryIn",
        "BitbucketServerRepositoryOut": "_cloudbuild_79_BitbucketServerRepositoryOut",
        "SourceProvenanceIn": "_cloudbuild_80_SourceProvenanceIn",
        "SourceProvenanceOut": "_cloudbuild_81_SourceProvenanceOut",
        "ResultsIn": "_cloudbuild_82_ResultsIn",
        "ResultsOut": "_cloudbuild_83_ResultsOut",
        "SecretManagerSecretIn": "_cloudbuild_84_SecretManagerSecretIn",
        "SecretManagerSecretOut": "_cloudbuild_85_SecretManagerSecretOut",
        "OperationIn": "_cloudbuild_86_OperationIn",
        "OperationOut": "_cloudbuild_87_OperationOut",
        "PubsubConfigIn": "_cloudbuild_88_PubsubConfigIn",
        "PubsubConfigOut": "_cloudbuild_89_PubsubConfigOut",
        "RunBuildTriggerRequestIn": "_cloudbuild_90_RunBuildTriggerRequestIn",
        "RunBuildTriggerRequestOut": "_cloudbuild_91_RunBuildTriggerRequestOut",
        "StorageSourceIn": "_cloudbuild_92_StorageSourceIn",
        "StorageSourceOut": "_cloudbuild_93_StorageSourceOut",
        "NetworkConfigIn": "_cloudbuild_94_NetworkConfigIn",
        "NetworkConfigOut": "_cloudbuild_95_NetworkConfigOut",
        "PullRequestFilterIn": "_cloudbuild_96_PullRequestFilterIn",
        "PullRequestFilterOut": "_cloudbuild_97_PullRequestFilterOut",
        "BuiltImageIn": "_cloudbuild_98_BuiltImageIn",
        "BuiltImageOut": "_cloudbuild_99_BuiltImageOut",
        "FailureInfoIn": "_cloudbuild_100_FailureInfoIn",
        "FailureInfoOut": "_cloudbuild_101_FailureInfoOut",
        "MavenArtifactIn": "_cloudbuild_102_MavenArtifactIn",
        "MavenArtifactOut": "_cloudbuild_103_MavenArtifactOut",
        "BuildOptionsIn": "_cloudbuild_104_BuildOptionsIn",
        "BuildOptionsOut": "_cloudbuild_105_BuildOptionsOut",
        "UploadedPythonPackageIn": "_cloudbuild_106_UploadedPythonPackageIn",
        "UploadedPythonPackageOut": "_cloudbuild_107_UploadedPythonPackageOut",
        "GitLabEnterpriseConfigIn": "_cloudbuild_108_GitLabEnterpriseConfigIn",
        "GitLabEnterpriseConfigOut": "_cloudbuild_109_GitLabEnterpriseConfigOut",
        "SecretsIn": "_cloudbuild_110_SecretsIn",
        "SecretsOut": "_cloudbuild_111_SecretsOut",
        "WarningIn": "_cloudbuild_112_WarningIn",
        "WarningOut": "_cloudbuild_113_WarningOut",
        "HttpBodyIn": "_cloudbuild_114_HttpBodyIn",
        "HttpBodyOut": "_cloudbuild_115_HttpBodyOut",
        "WebhookConfigIn": "_cloudbuild_116_WebhookConfigIn",
        "WebhookConfigOut": "_cloudbuild_117_WebhookConfigOut",
        "BatchCreateGitLabConnectedRepositoriesRequestIn": "_cloudbuild_118_BatchCreateGitLabConnectedRepositoriesRequestIn",
        "BatchCreateGitLabConnectedRepositoriesRequestOut": "_cloudbuild_119_BatchCreateGitLabConnectedRepositoriesRequestOut",
        "ServiceDirectoryConfigIn": "_cloudbuild_120_ServiceDirectoryConfigIn",
        "ServiceDirectoryConfigOut": "_cloudbuild_121_ServiceDirectoryConfigOut",
        "HashIn": "_cloudbuild_122_HashIn",
        "HashOut": "_cloudbuild_123_HashOut",
        "RemoveGitLabConnectedRepositoryRequestIn": "_cloudbuild_124_RemoveGitLabConnectedRepositoryRequestIn",
        "RemoveGitLabConnectedRepositoryRequestOut": "_cloudbuild_125_RemoveGitLabConnectedRepositoryRequestOut",
        "BitbucketServerRepositoryIdIn": "_cloudbuild_126_BitbucketServerRepositoryIdIn",
        "BitbucketServerRepositoryIdOut": "_cloudbuild_127_BitbucketServerRepositoryIdOut",
        "BitbucketServerTriggerConfigIn": "_cloudbuild_128_BitbucketServerTriggerConfigIn",
        "BitbucketServerTriggerConfigOut": "_cloudbuild_129_BitbucketServerTriggerConfigOut",
        "BuildStepIn": "_cloudbuild_130_BuildStepIn",
        "BuildStepOut": "_cloudbuild_131_BuildStepOut",
        "CancelBuildRequestIn": "_cloudbuild_132_CancelBuildRequestIn",
        "CancelBuildRequestOut": "_cloudbuild_133_CancelBuildRequestOut",
        "BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataIn": "_cloudbuild_134_BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataIn",
        "BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataOut": "_cloudbuild_135_BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataOut",
        "OperationMetadataIn": "_cloudbuild_136_OperationMetadataIn",
        "OperationMetadataOut": "_cloudbuild_137_OperationMetadataOut",
        "SourceIn": "_cloudbuild_138_SourceIn",
        "SourceOut": "_cloudbuild_139_SourceOut",
        "CreateWorkerPoolOperationMetadataIn": "_cloudbuild_140_CreateWorkerPoolOperationMetadataIn",
        "CreateWorkerPoolOperationMetadataOut": "_cloudbuild_141_CreateWorkerPoolOperationMetadataOut",
        "GitLabConnectedRepositoryIn": "_cloudbuild_142_GitLabConnectedRepositoryIn",
        "GitLabConnectedRepositoryOut": "_cloudbuild_143_GitLabConnectedRepositoryOut",
        "ListBuildsResponseIn": "_cloudbuild_144_ListBuildsResponseIn",
        "ListBuildsResponseOut": "_cloudbuild_145_ListBuildsResponseOut",
        "ArtifactObjectsIn": "_cloudbuild_146_ArtifactObjectsIn",
        "ArtifactObjectsOut": "_cloudbuild_147_ArtifactObjectsOut",
        "EmptyIn": "_cloudbuild_148_EmptyIn",
        "EmptyOut": "_cloudbuild_149_EmptyOut",
        "BatchCreateBitbucketServerConnectedRepositoriesResponseIn": "_cloudbuild_150_BatchCreateBitbucketServerConnectedRepositoriesResponseIn",
        "BatchCreateBitbucketServerConnectedRepositoriesResponseOut": "_cloudbuild_151_BatchCreateBitbucketServerConnectedRepositoriesResponseOut",
        "BitbucketServerSecretsIn": "_cloudbuild_152_BitbucketServerSecretsIn",
        "BitbucketServerSecretsOut": "_cloudbuild_153_BitbucketServerSecretsOut",
        "BitbucketServerConnectedRepositoryIn": "_cloudbuild_154_BitbucketServerConnectedRepositoryIn",
        "BitbucketServerConnectedRepositoryOut": "_cloudbuild_155_BitbucketServerConnectedRepositoryOut",
        "BatchCreateGitLabConnectedRepositoriesResponseIn": "_cloudbuild_156_BatchCreateGitLabConnectedRepositoriesResponseIn",
        "BatchCreateGitLabConnectedRepositoriesResponseOut": "_cloudbuild_157_BatchCreateGitLabConnectedRepositoriesResponseOut",
        "VolumeIn": "_cloudbuild_158_VolumeIn",
        "VolumeOut": "_cloudbuild_159_VolumeOut",
        "ListBuildTriggersResponseIn": "_cloudbuild_160_ListBuildTriggersResponseIn",
        "ListBuildTriggersResponseOut": "_cloudbuild_161_ListBuildTriggersResponseOut",
        "ListWorkerPoolsResponseIn": "_cloudbuild_162_ListWorkerPoolsResponseIn",
        "ListWorkerPoolsResponseOut": "_cloudbuild_163_ListWorkerPoolsResponseOut",
        "CreateBitbucketServerConfigOperationMetadataIn": "_cloudbuild_164_CreateBitbucketServerConfigOperationMetadataIn",
        "CreateBitbucketServerConfigOperationMetadataOut": "_cloudbuild_165_CreateBitbucketServerConfigOperationMetadataOut",
        "UpdateGitLabConfigOperationMetadataIn": "_cloudbuild_166_UpdateGitLabConfigOperationMetadataIn",
        "UpdateGitLabConfigOperationMetadataOut": "_cloudbuild_167_UpdateGitLabConfigOperationMetadataOut",
        "BitbucketServerConfigIn": "_cloudbuild_168_BitbucketServerConfigIn",
        "BitbucketServerConfigOut": "_cloudbuild_169_BitbucketServerConfigOut",
        "RemoveBitbucketServerConnectedRepositoryRequestIn": "_cloudbuild_170_RemoveBitbucketServerConnectedRepositoryRequestIn",
        "RemoveBitbucketServerConnectedRepositoryRequestOut": "_cloudbuild_171_RemoveBitbucketServerConnectedRepositoryRequestOut",
        "GitLabEventsConfigIn": "_cloudbuild_172_GitLabEventsConfigIn",
        "GitLabEventsConfigOut": "_cloudbuild_173_GitLabEventsConfigOut",
        "NpmPackageIn": "_cloudbuild_174_NpmPackageIn",
        "NpmPackageOut": "_cloudbuild_175_NpmPackageOut",
        "ReceiveTriggerWebhookResponseIn": "_cloudbuild_176_ReceiveTriggerWebhookResponseIn",
        "ReceiveTriggerWebhookResponseOut": "_cloudbuild_177_ReceiveTriggerWebhookResponseOut",
        "UpdateGitHubEnterpriseConfigOperationMetadataIn": "_cloudbuild_178_UpdateGitHubEnterpriseConfigOperationMetadataIn",
        "UpdateGitHubEnterpriseConfigOperationMetadataOut": "_cloudbuild_179_UpdateGitHubEnterpriseConfigOperationMetadataOut",
        "GitSourceIn": "_cloudbuild_180_GitSourceIn",
        "GitSourceOut": "_cloudbuild_181_GitSourceOut",
        "CreateGitHubEnterpriseConfigOperationMetadataIn": "_cloudbuild_182_CreateGitHubEnterpriseConfigOperationMetadataIn",
        "CreateGitHubEnterpriseConfigOperationMetadataOut": "_cloudbuild_183_CreateGitHubEnterpriseConfigOperationMetadataOut",
        "UploadedNpmPackageIn": "_cloudbuild_184_UploadedNpmPackageIn",
        "UploadedNpmPackageOut": "_cloudbuild_185_UploadedNpmPackageOut",
        "PrivatePoolV1ConfigIn": "_cloudbuild_186_PrivatePoolV1ConfigIn",
        "PrivatePoolV1ConfigOut": "_cloudbuild_187_PrivatePoolV1ConfigOut",
        "GitHubEnterpriseSecretsIn": "_cloudbuild_188_GitHubEnterpriseSecretsIn",
        "GitHubEnterpriseSecretsOut": "_cloudbuild_189_GitHubEnterpriseSecretsOut",
        "WorkerPoolIn": "_cloudbuild_190_WorkerPoolIn",
        "WorkerPoolOut": "_cloudbuild_191_WorkerPoolOut",
        "CancelOperationRequestIn": "_cloudbuild_192_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_cloudbuild_193_CancelOperationRequestOut",
        "ArtifactsIn": "_cloudbuild_194_ArtifactsIn",
        "ArtifactsOut": "_cloudbuild_195_ArtifactsOut",
        "ListGithubEnterpriseConfigsResponseIn": "_cloudbuild_196_ListGithubEnterpriseConfigsResponseIn",
        "ListGithubEnterpriseConfigsResponseOut": "_cloudbuild_197_ListGithubEnterpriseConfigsResponseOut",
        "TimeSpanIn": "_cloudbuild_198_TimeSpanIn",
        "TimeSpanOut": "_cloudbuild_199_TimeSpanOut",
        "DeleteGitHubEnterpriseConfigOperationMetadataIn": "_cloudbuild_200_DeleteGitHubEnterpriseConfigOperationMetadataIn",
        "DeleteGitHubEnterpriseConfigOperationMetadataOut": "_cloudbuild_201_DeleteGitHubEnterpriseConfigOperationMetadataOut",
        "BuildOperationMetadataIn": "_cloudbuild_202_BuildOperationMetadataIn",
        "BuildOperationMetadataOut": "_cloudbuild_203_BuildOperationMetadataOut",
        "ApprovalConfigIn": "_cloudbuild_204_ApprovalConfigIn",
        "ApprovalConfigOut": "_cloudbuild_205_ApprovalConfigOut",
        "BuildTriggerIn": "_cloudbuild_206_BuildTriggerIn",
        "BuildTriggerOut": "_cloudbuild_207_BuildTriggerOut",
        "FileHashesIn": "_cloudbuild_208_FileHashesIn",
        "FileHashesOut": "_cloudbuild_209_FileHashesOut",
        "GitLabConfigIn": "_cloudbuild_210_GitLabConfigIn",
        "GitLabConfigOut": "_cloudbuild_211_GitLabConfigOut",
        "BatchCreateGitLabConnectedRepositoriesResponseMetadataIn": "_cloudbuild_212_BatchCreateGitLabConnectedRepositoriesResponseMetadataIn",
        "BatchCreateGitLabConnectedRepositoriesResponseMetadataOut": "_cloudbuild_213_BatchCreateGitLabConnectedRepositoriesResponseMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GitHubEnterpriseConfigIn"] = t.struct(
        {
            "sslCa": t.string().optional(),
            "appId": t.string(),
            "secrets": t.proxy(renames["GitHubEnterpriseSecretsIn"]).optional(),
            "webhookKey": t.string().optional(),
            "peeredNetwork": t.string().optional(),
            "hostUrl": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GitHubEnterpriseConfigIn"])
    types["GitHubEnterpriseConfigOut"] = t.struct(
        {
            "sslCa": t.string().optional(),
            "appId": t.string(),
            "secrets": t.proxy(renames["GitHubEnterpriseSecretsOut"]).optional(),
            "webhookKey": t.string().optional(),
            "peeredNetwork": t.string().optional(),
            "hostUrl": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitHubEnterpriseConfigOut"])
    types["DeleteWorkerPoolOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "workerPool": t.string().optional(),
        }
    ).named(renames["DeleteWorkerPoolOperationMetadataIn"])
    types["DeleteWorkerPoolOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "workerPool": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteWorkerPoolOperationMetadataOut"])
    types["RepositoryEventConfigIn"] = t.struct(
        {
            "push": t.proxy(renames["PushFilterIn"]).optional(),
            "repository": t.string().optional(),
            "pullRequest": t.proxy(renames["PullRequestFilterIn"]).optional(),
        }
    ).named(renames["RepositoryEventConfigIn"])
    types["RepositoryEventConfigOut"] = t.struct(
        {
            "push": t.proxy(renames["PushFilterOut"]).optional(),
            "repositoryType": t.string().optional(),
            "repository": t.string().optional(),
            "pullRequest": t.proxy(renames["PullRequestFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepositoryEventConfigOut"])
    types["ApprovalResultIn"] = t.struct(
        {
            "comment": t.string().optional(),
            "url": t.string().optional(),
            "decision": t.string(),
        }
    ).named(renames["ApprovalResultIn"])
    types["ApprovalResultOut"] = t.struct(
        {
            "comment": t.string().optional(),
            "url": t.string().optional(),
            "approverAccount": t.string().optional(),
            "approvalTime": t.string().optional(),
            "decision": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApprovalResultOut"])
    types["ProcessAppManifestCallbackOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "completeTime": t.string().optional(),
        }
    ).named(renames["ProcessAppManifestCallbackOperationMetadataIn"])
    types["ProcessAppManifestCallbackOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "completeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProcessAppManifestCallbackOperationMetadataOut"])
    types["UploadedMavenArtifactIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "fileHashes": t.proxy(renames["FileHashesIn"]).optional(),
        }
    ).named(renames["UploadedMavenArtifactIn"])
    types["UploadedMavenArtifactOut"] = t.struct(
        {
            "pushTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "uri": t.string().optional(),
            "fileHashes": t.proxy(renames["FileHashesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadedMavenArtifactOut"])
    types["RetryBuildRequestIn"] = t.struct(
        {"name": t.string().optional(), "projectId": t.string(), "id": t.string()}
    ).named(renames["RetryBuildRequestIn"])
    types["RetryBuildRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "projectId": t.string(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetryBuildRequestOut"])
    types["GitHubEventsConfigIn"] = t.struct(
        {
            "enterpriseConfigResourceName": t.string().optional(),
            "pullRequest": t.proxy(renames["PullRequestFilterIn"]).optional(),
            "push": t.proxy(renames["PushFilterIn"]).optional(),
            "owner": t.string().optional(),
            "name": t.string().optional(),
            "installationId": t.string().optional(),
        }
    ).named(renames["GitHubEventsConfigIn"])
    types["GitHubEventsConfigOut"] = t.struct(
        {
            "enterpriseConfigResourceName": t.string().optional(),
            "pullRequest": t.proxy(renames["PullRequestFilterOut"]).optional(),
            "push": t.proxy(renames["PushFilterOut"]).optional(),
            "owner": t.string().optional(),
            "name": t.string().optional(),
            "installationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitHubEventsConfigOut"])
    types["CreateGitLabConfigOperationMetadataIn"] = t.struct(
        {
            "gitlabConfig": t.string().optional(),
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
        }
    ).named(renames["CreateGitLabConfigOperationMetadataIn"])
    types["CreateGitLabConfigOperationMetadataOut"] = t.struct(
        {
            "gitlabConfig": t.string().optional(),
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateGitLabConfigOperationMetadataOut"])
    types["WorkerConfigIn"] = t.struct(
        {"machineType": t.string().optional(), "diskSizeGb": t.string().optional()}
    ).named(renames["WorkerConfigIn"])
    types["WorkerConfigOut"] = t.struct(
        {
            "machineType": t.string().optional(),
            "diskSizeGb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerConfigOut"])
    types["RepoSourceIn"] = t.struct(
        {
            "repoName": t.string().optional(),
            "commitSha": t.string().optional(),
            "tagName": t.string().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "branchName": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "dir": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["RepoSourceIn"])
    types["RepoSourceOut"] = t.struct(
        {
            "repoName": t.string().optional(),
            "commitSha": t.string().optional(),
            "tagName": t.string().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "branchName": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "dir": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepoSourceOut"])
    types["GitRepoSourceIn"] = t.struct(
        {
            "githubEnterpriseConfig": t.string().optional(),
            "uri": t.string().optional(),
            "repository": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "repoType": t.string().optional(),
            "ref": t.string().optional(),
        }
    ).named(renames["GitRepoSourceIn"])
    types["GitRepoSourceOut"] = t.struct(
        {
            "githubEnterpriseConfig": t.string().optional(),
            "uri": t.string().optional(),
            "repository": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "repoType": t.string().optional(),
            "ref": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitRepoSourceOut"])
    types["CreateBitbucketServerConnectedRepositoryRequestIn"] = t.struct(
        {
            "bitbucketServerConnectedRepository": t.proxy(
                renames["BitbucketServerConnectedRepositoryIn"]
            ),
            "parent": t.string(),
        }
    ).named(renames["CreateBitbucketServerConnectedRepositoryRequestIn"])
    types["CreateBitbucketServerConnectedRepositoryRequestOut"] = t.struct(
        {
            "bitbucketServerConnectedRepository": t.proxy(
                renames["BitbucketServerConnectedRepositoryOut"]
            ),
            "parent": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateBitbucketServerConnectedRepositoryRequestOut"])
    types["GitFileSourceIn"] = t.struct(
        {
            "repoType": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "revision": t.string().optional(),
            "repository": t.string().optional(),
            "path": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["GitFileSourceIn"])
    types["GitFileSourceOut"] = t.struct(
        {
            "repoType": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "revision": t.string().optional(),
            "repository": t.string().optional(),
            "path": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitFileSourceOut"])
    types["GitLabRepositoryIn"] = t.struct(
        {
            "description": t.string().optional(),
            "repositoryId": t.proxy(renames["GitLabRepositoryIdIn"]).optional(),
            "browseUri": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GitLabRepositoryIn"])
    types["GitLabRepositoryOut"] = t.struct(
        {
            "description": t.string().optional(),
            "repositoryId": t.proxy(renames["GitLabRepositoryIdOut"]).optional(),
            "browseUri": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabRepositoryOut"])
    types["ListBitbucketServerRepositoriesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "bitbucketServerRepositories": t.array(
                t.proxy(renames["BitbucketServerRepositoryIn"])
            ).optional(),
        }
    ).named(renames["ListBitbucketServerRepositoriesResponseIn"])
    types["ListBitbucketServerRepositoriesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "bitbucketServerRepositories": t.array(
                t.proxy(renames["BitbucketServerRepositoryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBitbucketServerRepositoriesResponseOut"])
    types["PushFilterIn"] = t.struct(
        {
            "tag": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "branch": t.string().optional(),
        }
    ).named(renames["PushFilterIn"])
    types["PushFilterOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "branch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PushFilterOut"])
    types["GitLabSecretsIn"] = t.struct(
        {
            "apiKeyVersion": t.string(),
            "apiAccessTokenVersion": t.string(),
            "readAccessTokenVersion": t.string(),
            "webhookSecretVersion": t.string(),
        }
    ).named(renames["GitLabSecretsIn"])
    types["GitLabSecretsOut"] = t.struct(
        {
            "apiKeyVersion": t.string(),
            "apiAccessTokenVersion": t.string(),
            "readAccessTokenVersion": t.string(),
            "webhookSecretVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabSecretsOut"])
    types["BuildIn"] = t.struct(
        {
            "secrets": t.array(t.proxy(renames["SecretIn"])).optional(),
            "queueTtl": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "steps": t.array(t.proxy(renames["BuildStepIn"])),
            "options": t.proxy(renames["BuildOptionsIn"]).optional(),
            "serviceAccount": t.string().optional(),
            "artifacts": t.proxy(renames["ArtifactsIn"]).optional(),
            "logsBucket": t.string().optional(),
            "timeout": t.string().optional(),
            "availableSecrets": t.proxy(renames["SecretsIn"]).optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "images": t.array(t.string()).optional(),
        }
    ).named(renames["BuildIn"])
    types["BuildOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "warnings": t.array(t.proxy(renames["WarningOut"])).optional(),
            "logUrl": t.string().optional(),
            "timing": t.struct({"_": t.string().optional()}).optional(),
            "secrets": t.array(t.proxy(renames["SecretOut"])).optional(),
            "buildTriggerId": t.string().optional(),
            "statusDetail": t.string().optional(),
            "queueTtl": t.string().optional(),
            "status": t.string().optional(),
            "finishTime": t.string().optional(),
            "name": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "steps": t.array(t.proxy(renames["BuildStepOut"])),
            "options": t.proxy(renames["BuildOptionsOut"]).optional(),
            "serviceAccount": t.string().optional(),
            "artifacts": t.proxy(renames["ArtifactsOut"]).optional(),
            "results": t.proxy(renames["ResultsOut"]).optional(),
            "approval": t.proxy(renames["BuildApprovalOut"]).optional(),
            "logsBucket": t.string().optional(),
            "startTime": t.string().optional(),
            "timeout": t.string().optional(),
            "id": t.string().optional(),
            "availableSecrets": t.proxy(renames["SecretsOut"]).optional(),
            "projectId": t.string().optional(),
            "failureInfo": t.proxy(renames["FailureInfoOut"]).optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "sourceProvenance": t.proxy(renames["SourceProvenanceOut"]).optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "images": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOut"])
    types["ApproveBuildRequestIn"] = t.struct(
        {"approvalResult": t.proxy(renames["ApprovalResultIn"]).optional()}
    ).named(renames["ApproveBuildRequestIn"])
    types["ApproveBuildRequestOut"] = t.struct(
        {
            "approvalResult": t.proxy(renames["ApprovalResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproveBuildRequestOut"])
    types["PythonPackageIn"] = t.struct(
        {"repository": t.string().optional(), "paths": t.array(t.string()).optional()}
    ).named(renames["PythonPackageIn"])
    types["PythonPackageOut"] = t.struct(
        {
            "repository": t.string().optional(),
            "paths": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonPackageOut"])
    types["StorageSourceManifestIn"] = t.struct(
        {
            "object": t.string().optional(),
            "bucket": t.string().optional(),
            "generation": t.string().optional(),
        }
    ).named(renames["StorageSourceManifestIn"])
    types["StorageSourceManifestOut"] = t.struct(
        {
            "object": t.string().optional(),
            "bucket": t.string().optional(),
            "generation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StorageSourceManifestOut"])
    types["CreateGitLabConnectedRepositoryRequestIn"] = t.struct(
        {
            "gitlabConnectedRepository": t.proxy(
                renames["GitLabConnectedRepositoryIn"]
            ),
            "parent": t.string(),
        }
    ).named(renames["CreateGitLabConnectedRepositoryRequestIn"])
    types["CreateGitLabConnectedRepositoryRequestOut"] = t.struct(
        {
            "gitlabConnectedRepository": t.proxy(
                renames["GitLabConnectedRepositoryOut"]
            ),
            "parent": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateGitLabConnectedRepositoryRequestOut"])
    types["DeleteGitLabConfigOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "gitlabConfig": t.string().optional(),
        }
    ).named(renames["DeleteGitLabConfigOperationMetadataIn"])
    types["DeleteGitLabConfigOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "gitlabConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteGitLabConfigOperationMetadataOut"])
    types["PoolOptionIn"] = t.struct({"name": t.string().optional()}).named(
        renames["PoolOptionIn"]
    )
    types["PoolOptionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoolOptionOut"])
    types["UpdateWorkerPoolOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "workerPool": t.string().optional(),
        }
    ).named(renames["UpdateWorkerPoolOperationMetadataIn"])
    types["UpdateWorkerPoolOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "workerPool": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateWorkerPoolOperationMetadataOut"])
    types["ListGitLabConfigsResponseIn"] = t.struct(
        {
            "gitlabConfigs": t.array(t.proxy(renames["GitLabConfigIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListGitLabConfigsResponseIn"])
    types["ListGitLabConfigsResponseOut"] = t.struct(
        {
            "gitlabConfigs": t.array(t.proxy(renames["GitLabConfigOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGitLabConfigsResponseOut"])
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
    types["ArtifactResultIn"] = t.struct(
        {
            "fileHash": t.array(t.proxy(renames["FileHashesIn"])).optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ArtifactResultIn"])
    types["ArtifactResultOut"] = t.struct(
        {
            "fileHash": t.array(t.proxy(renames["FileHashesOut"])).optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArtifactResultOut"])
    types["GitLabRepositoryIdIn"] = t.struct({"id": t.string()}).named(
        renames["GitLabRepositoryIdIn"]
    )
    types["GitLabRepositoryIdOut"] = t.struct(
        {
            "id": t.string(),
            "webhookId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabRepositoryIdOut"])
    types["SecretIn"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "secretEnv": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SecretIn"])
    types["SecretOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "secretEnv": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretOut"])
    types["InlineSecretIn"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "envMap": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["InlineSecretIn"])
    types["InlineSecretOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "envMap": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlineSecretOut"])
    types["ListBitbucketServerConfigsResponseIn"] = t.struct(
        {
            "bitbucketServerConfigs": t.array(
                t.proxy(renames["BitbucketServerConfigIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBitbucketServerConfigsResponseIn"])
    types["ListBitbucketServerConfigsResponseOut"] = t.struct(
        {
            "bitbucketServerConfigs": t.array(
                t.proxy(renames["BitbucketServerConfigOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBitbucketServerConfigsResponseOut"])
    types["UpdateBitbucketServerConfigOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
        }
    ).named(renames["UpdateBitbucketServerConfigOperationMetadataIn"])
    types["UpdateBitbucketServerConfigOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBitbucketServerConfigOperationMetadataOut"])
    types["BuildApprovalIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BuildApprovalIn"]
    )
    types["BuildApprovalOut"] = t.struct(
        {
            "result": t.proxy(renames["ApprovalResultOut"]).optional(),
            "state": t.string().optional(),
            "config": t.proxy(renames["ApprovalConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildApprovalOut"])
    types["ListGitLabRepositoriesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "gitlabRepositories": t.array(
                t.proxy(renames["GitLabRepositoryIn"])
            ).optional(),
        }
    ).named(renames["ListGitLabRepositoriesResponseIn"])
    types["ListGitLabRepositoriesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "gitlabRepositories": t.array(
                t.proxy(renames["GitLabRepositoryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGitLabRepositoriesResponseOut"])
    types["BatchCreateBitbucketServerConnectedRepositoriesRequestIn"] = t.struct(
        {
            "requests": t.array(
                t.proxy(renames["CreateBitbucketServerConnectedRepositoryRequestIn"])
            )
        }
    ).named(renames["BatchCreateBitbucketServerConnectedRepositoriesRequestIn"])
    types["BatchCreateBitbucketServerConnectedRepositoriesRequestOut"] = t.struct(
        {
            "requests": t.array(
                t.proxy(renames["CreateBitbucketServerConnectedRepositoryRequestOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateBitbucketServerConnectedRepositoriesRequestOut"])
    types["DeleteBitbucketServerConfigOperationMetadataIn"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
        }
    ).named(renames["DeleteBitbucketServerConfigOperationMetadataIn"])
    types["DeleteBitbucketServerConfigOperationMetadataOut"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteBitbucketServerConfigOperationMetadataOut"])
    types["BitbucketServerRepositoryIn"] = t.struct(
        {
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "browseUri": t.string().optional(),
            "repoId": t.proxy(renames["BitbucketServerRepositoryIdIn"]).optional(),
        }
    ).named(renames["BitbucketServerRepositoryIn"])
    types["BitbucketServerRepositoryOut"] = t.struct(
        {
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "browseUri": t.string().optional(),
            "repoId": t.proxy(renames["BitbucketServerRepositoryIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerRepositoryOut"])
    types["SourceProvenanceIn"] = t.struct(
        {
            "resolvedStorageSource": t.proxy(renames["StorageSourceIn"]).optional(),
            "resolvedStorageSourceManifest": t.proxy(
                renames["StorageSourceManifestIn"]
            ).optional(),
            "resolvedRepoSource": t.proxy(renames["RepoSourceIn"]).optional(),
        }
    ).named(renames["SourceProvenanceIn"])
    types["SourceProvenanceOut"] = t.struct(
        {
            "resolvedStorageSource": t.proxy(renames["StorageSourceOut"]).optional(),
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "resolvedStorageSourceManifest": t.proxy(
                renames["StorageSourceManifestOut"]
            ).optional(),
            "resolvedRepoSource": t.proxy(renames["RepoSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceProvenanceOut"])
    types["ResultsIn"] = t.struct(
        {
            "images": t.array(t.proxy(renames["BuiltImageIn"])).optional(),
            "buildStepOutputs": t.array(t.string()).optional(),
            "npmPackages": t.array(t.proxy(renames["UploadedNpmPackageIn"])).optional(),
            "pythonPackages": t.array(
                t.proxy(renames["UploadedPythonPackageIn"])
            ).optional(),
            "mavenArtifacts": t.array(
                t.proxy(renames["UploadedMavenArtifactIn"])
            ).optional(),
            "artifactTiming": t.proxy(renames["TimeSpanIn"]).optional(),
            "buildStepImages": t.array(t.string()).optional(),
            "numArtifacts": t.string().optional(),
            "artifactManifest": t.string().optional(),
        }
    ).named(renames["ResultsIn"])
    types["ResultsOut"] = t.struct(
        {
            "images": t.array(t.proxy(renames["BuiltImageOut"])).optional(),
            "buildStepOutputs": t.array(t.string()).optional(),
            "npmPackages": t.array(
                t.proxy(renames["UploadedNpmPackageOut"])
            ).optional(),
            "pythonPackages": t.array(
                t.proxy(renames["UploadedPythonPackageOut"])
            ).optional(),
            "mavenArtifacts": t.array(
                t.proxy(renames["UploadedMavenArtifactOut"])
            ).optional(),
            "artifactTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "buildStepImages": t.array(t.string()).optional(),
            "numArtifacts": t.string().optional(),
            "artifactManifest": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultsOut"])
    types["SecretManagerSecretIn"] = t.struct(
        {"versionName": t.string().optional(), "env": t.string().optional()}
    ).named(renames["SecretManagerSecretIn"])
    types["SecretManagerSecretOut"] = t.struct(
        {
            "versionName": t.string().optional(),
            "env": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretManagerSecretOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["PubsubConfigIn"] = t.struct(
        {
            "serviceAccountEmail": t.string().optional(),
            "state": t.string().optional(),
            "topic": t.string().optional(),
        }
    ).named(renames["PubsubConfigIn"])
    types["PubsubConfigOut"] = t.struct(
        {
            "serviceAccountEmail": t.string().optional(),
            "state": t.string().optional(),
            "topic": t.string().optional(),
            "subscription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubConfigOut"])
    types["RunBuildTriggerRequestIn"] = t.struct(
        {
            "projectId": t.string(),
            "source": t.proxy(renames["RepoSourceIn"]).optional(),
            "triggerId": t.string(),
        }
    ).named(renames["RunBuildTriggerRequestIn"])
    types["RunBuildTriggerRequestOut"] = t.struct(
        {
            "projectId": t.string(),
            "source": t.proxy(renames["RepoSourceOut"]).optional(),
            "triggerId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunBuildTriggerRequestOut"])
    types["StorageSourceIn"] = t.struct(
        {
            "object": t.string().optional(),
            "bucket": t.string().optional(),
            "generation": t.string().optional(),
        }
    ).named(renames["StorageSourceIn"])
    types["StorageSourceOut"] = t.struct(
        {
            "object": t.string().optional(),
            "bucket": t.string().optional(),
            "generation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StorageSourceOut"])
    types["NetworkConfigIn"] = t.struct(
        {
            "peeredNetwork": t.string(),
            "peeredNetworkIpRange": t.string().optional(),
            "egressOption": t.string().optional(),
        }
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "peeredNetwork": t.string(),
            "peeredNetworkIpRange": t.string().optional(),
            "egressOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["PullRequestFilterIn"] = t.struct(
        {
            "invertRegex": t.boolean().optional(),
            "commentControl": t.string().optional(),
            "branch": t.string().optional(),
        }
    ).named(renames["PullRequestFilterIn"])
    types["PullRequestFilterOut"] = t.struct(
        {
            "invertRegex": t.boolean().optional(),
            "commentControl": t.string().optional(),
            "branch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PullRequestFilterOut"])
    types["BuiltImageIn"] = t.struct(
        {"name": t.string().optional(), "digest": t.string().optional()}
    ).named(renames["BuiltImageIn"])
    types["BuiltImageOut"] = t.struct(
        {
            "name": t.string().optional(),
            "pushTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "digest": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuiltImageOut"])
    types["FailureInfoIn"] = t.struct(
        {"type": t.string().optional(), "detail": t.string().optional()}
    ).named(renames["FailureInfoIn"])
    types["FailureInfoOut"] = t.struct(
        {
            "type": t.string().optional(),
            "detail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FailureInfoOut"])
    types["MavenArtifactIn"] = t.struct(
        {
            "artifactId": t.string().optional(),
            "path": t.string().optional(),
            "repository": t.string().optional(),
            "version": t.string().optional(),
            "groupId": t.string().optional(),
        }
    ).named(renames["MavenArtifactIn"])
    types["MavenArtifactOut"] = t.struct(
        {
            "artifactId": t.string().optional(),
            "path": t.string().optional(),
            "repository": t.string().optional(),
            "version": t.string().optional(),
            "groupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MavenArtifactOut"])
    types["BuildOptionsIn"] = t.struct(
        {
            "requestedVerifyOption": t.string().optional(),
            "logStreamingOption": t.string().optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "defaultLogsBucketBehavior": t.string().optional(),
            "machineType": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "sourceProvenanceHash": t.array(t.string()).optional(),
            "logging": t.string().optional(),
            "workerPool": t.string().optional(),
            "pool": t.proxy(renames["PoolOptionIn"]).optional(),
            "dynamicSubstitutions": t.boolean().optional(),
            "secretEnv": t.array(t.string()).optional(),
            "substitutionOption": t.string().optional(),
            "diskSizeGb": t.string().optional(),
        }
    ).named(renames["BuildOptionsIn"])
    types["BuildOptionsOut"] = t.struct(
        {
            "requestedVerifyOption": t.string().optional(),
            "logStreamingOption": t.string().optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "defaultLogsBucketBehavior": t.string().optional(),
            "machineType": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "sourceProvenanceHash": t.array(t.string()).optional(),
            "logging": t.string().optional(),
            "workerPool": t.string().optional(),
            "pool": t.proxy(renames["PoolOptionOut"]).optional(),
            "dynamicSubstitutions": t.boolean().optional(),
            "secretEnv": t.array(t.string()).optional(),
            "substitutionOption": t.string().optional(),
            "diskSizeGb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOptionsOut"])
    types["UploadedPythonPackageIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "fileHashes": t.proxy(renames["FileHashesIn"]).optional(),
        }
    ).named(renames["UploadedPythonPackageIn"])
    types["UploadedPythonPackageOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "pushTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "fileHashes": t.proxy(renames["FileHashesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadedPythonPackageOut"])
    types["GitLabEnterpriseConfigIn"] = t.struct(
        {
            "sslCa": t.string().optional(),
            "serviceDirectoryConfig": t.proxy(
                renames["ServiceDirectoryConfigIn"]
            ).optional(),
            "hostUri": t.string().optional(),
        }
    ).named(renames["GitLabEnterpriseConfigIn"])
    types["GitLabEnterpriseConfigOut"] = t.struct(
        {
            "sslCa": t.string().optional(),
            "serviceDirectoryConfig": t.proxy(
                renames["ServiceDirectoryConfigOut"]
            ).optional(),
            "hostUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabEnterpriseConfigOut"])
    types["SecretsIn"] = t.struct(
        {
            "secretManager": t.array(
                t.proxy(renames["SecretManagerSecretIn"])
            ).optional(),
            "inline": t.array(t.proxy(renames["InlineSecretIn"])).optional(),
        }
    ).named(renames["SecretsIn"])
    types["SecretsOut"] = t.struct(
        {
            "secretManager": t.array(
                t.proxy(renames["SecretManagerSecretOut"])
            ).optional(),
            "inline": t.array(t.proxy(renames["InlineSecretOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretsOut"])
    types["WarningIn"] = t.struct(
        {"text": t.string().optional(), "priority": t.string().optional()}
    ).named(renames["WarningIn"])
    types["WarningOut"] = t.struct(
        {
            "text": t.string().optional(),
            "priority": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WarningOut"])
    types["HttpBodyIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "data": t.string().optional(),
        }
    ).named(renames["HttpBodyIn"])
    types["HttpBodyOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpBodyOut"])
    types["WebhookConfigIn"] = t.struct(
        {"state": t.string().optional(), "secret": t.string()}
    ).named(renames["WebhookConfigIn"])
    types["WebhookConfigOut"] = t.struct(
        {
            "state": t.string().optional(),
            "secret": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebhookConfigOut"])
    types["BatchCreateGitLabConnectedRepositoriesRequestIn"] = t.struct(
        {
            "requests": t.array(
                t.proxy(renames["CreateGitLabConnectedRepositoryRequestIn"])
            )
        }
    ).named(renames["BatchCreateGitLabConnectedRepositoriesRequestIn"])
    types["BatchCreateGitLabConnectedRepositoriesRequestOut"] = t.struct(
        {
            "requests": t.array(
                t.proxy(renames["CreateGitLabConnectedRepositoryRequestOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateGitLabConnectedRepositoriesRequestOut"])
    types["ServiceDirectoryConfigIn"] = t.struct(
        {"service": t.string().optional()}
    ).named(renames["ServiceDirectoryConfigIn"])
    types["ServiceDirectoryConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceDirectoryConfigOut"])
    types["HashIn"] = t.struct(
        {"value": t.string().optional(), "type": t.string().optional()}
    ).named(renames["HashIn"])
    types["HashOut"] = t.struct(
        {
            "value": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HashOut"])
    types["RemoveGitLabConnectedRepositoryRequestIn"] = t.struct(
        {"connectedRepository": t.proxy(renames["GitLabRepositoryIdIn"]).optional()}
    ).named(renames["RemoveGitLabConnectedRepositoryRequestIn"])
    types["RemoveGitLabConnectedRepositoryRequestOut"] = t.struct(
        {
            "connectedRepository": t.proxy(renames["GitLabRepositoryIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveGitLabConnectedRepositoryRequestOut"])
    types["BitbucketServerRepositoryIdIn"] = t.struct(
        {"projectKey": t.string(), "repoSlug": t.string()}
    ).named(renames["BitbucketServerRepositoryIdIn"])
    types["BitbucketServerRepositoryIdOut"] = t.struct(
        {
            "projectKey": t.string(),
            "repoSlug": t.string(),
            "webhookId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerRepositoryIdOut"])
    types["BitbucketServerTriggerConfigIn"] = t.struct(
        {
            "push": t.proxy(renames["PushFilterIn"]).optional(),
            "projectKey": t.string(),
            "pullRequest": t.proxy(renames["PullRequestFilterIn"]).optional(),
            "bitbucketServerConfigResource": t.string(),
            "repoSlug": t.string(),
        }
    ).named(renames["BitbucketServerTriggerConfigIn"])
    types["BitbucketServerTriggerConfigOut"] = t.struct(
        {
            "push": t.proxy(renames["PushFilterOut"]).optional(),
            "bitbucketServerConfig": t.proxy(
                renames["BitbucketServerConfigOut"]
            ).optional(),
            "projectKey": t.string(),
            "pullRequest": t.proxy(renames["PullRequestFilterOut"]).optional(),
            "bitbucketServerConfigResource": t.string(),
            "repoSlug": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerTriggerConfigOut"])
    types["BuildStepIn"] = t.struct(
        {
            "name": t.string(),
            "env": t.array(t.string()).optional(),
            "dir": t.string().optional(),
            "secretEnv": t.array(t.string()).optional(),
            "allowFailure": t.boolean().optional(),
            "entrypoint": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "timeout": t.string().optional(),
            "script": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "allowExitCodes": t.array(t.integer()).optional(),
            "id": t.string().optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
        }
    ).named(renames["BuildStepIn"])
    types["BuildStepOut"] = t.struct(
        {
            "name": t.string(),
            "env": t.array(t.string()).optional(),
            "dir": t.string().optional(),
            "secretEnv": t.array(t.string()).optional(),
            "allowFailure": t.boolean().optional(),
            "entrypoint": t.string().optional(),
            "exitCode": t.integer().optional(),
            "pullTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "args": t.array(t.string()).optional(),
            "timeout": t.string().optional(),
            "script": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "allowExitCodes": t.array(t.integer()).optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "timing": t.proxy(renames["TimeSpanOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildStepOut"])
    types["CancelBuildRequestIn"] = t.struct(
        {"name": t.string().optional(), "id": t.string(), "projectId": t.string()}
    ).named(renames["CancelBuildRequestIn"])
    types["CancelBuildRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string(),
            "projectId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CancelBuildRequestOut"])
    types[
        "BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataIn"
    ] = t.struct(
        {
            "completeTime": t.string().optional(),
            "config": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(
        renames["BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataIn"]
    )
    types[
        "BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataOut"
    ] = t.struct(
        {
            "completeTime": t.string().optional(),
            "config": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataOut"]
    )
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "statusDetail": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["SourceIn"] = t.struct(
        {
            "gitSource": t.proxy(renames["GitSourceIn"]).optional(),
            "repoSource": t.proxy(renames["RepoSourceIn"]).optional(),
            "storageSourceManifest": t.proxy(
                renames["StorageSourceManifestIn"]
            ).optional(),
            "storageSource": t.proxy(renames["StorageSourceIn"]).optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "gitSource": t.proxy(renames["GitSourceOut"]).optional(),
            "repoSource": t.proxy(renames["RepoSourceOut"]).optional(),
            "storageSourceManifest": t.proxy(
                renames["StorageSourceManifestOut"]
            ).optional(),
            "storageSource": t.proxy(renames["StorageSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["CreateWorkerPoolOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "workerPool": t.string().optional(),
        }
    ).named(renames["CreateWorkerPoolOperationMetadataIn"])
    types["CreateWorkerPoolOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "workerPool": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateWorkerPoolOperationMetadataOut"])
    types["GitLabConnectedRepositoryIn"] = t.struct(
        {
            "parent": t.string().optional(),
            "repo": t.proxy(renames["GitLabRepositoryIdIn"]).optional(),
        }
    ).named(renames["GitLabConnectedRepositoryIn"])
    types["GitLabConnectedRepositoryOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "repo": t.proxy(renames["GitLabRepositoryIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabConnectedRepositoryOut"])
    types["ListBuildsResponseIn"] = t.struct(
        {
            "builds": t.array(t.proxy(renames["BuildIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBuildsResponseIn"])
    types["ListBuildsResponseOut"] = t.struct(
        {
            "builds": t.array(t.proxy(renames["BuildOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBuildsResponseOut"])
    types["ArtifactObjectsIn"] = t.struct(
        {"location": t.string().optional(), "paths": t.array(t.string()).optional()}
    ).named(renames["ArtifactObjectsIn"])
    types["ArtifactObjectsOut"] = t.struct(
        {
            "location": t.string().optional(),
            "paths": t.array(t.string()).optional(),
            "timing": t.proxy(renames["TimeSpanOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArtifactObjectsOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["BatchCreateBitbucketServerConnectedRepositoriesResponseIn"] = t.struct(
        {
            "bitbucketServerConnectedRepositories": t.array(
                t.proxy(renames["BitbucketServerConnectedRepositoryIn"])
            ).optional()
        }
    ).named(renames["BatchCreateBitbucketServerConnectedRepositoriesResponseIn"])
    types["BatchCreateBitbucketServerConnectedRepositoriesResponseOut"] = t.struct(
        {
            "bitbucketServerConnectedRepositories": t.array(
                t.proxy(renames["BitbucketServerConnectedRepositoryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateBitbucketServerConnectedRepositoriesResponseOut"])
    types["BitbucketServerSecretsIn"] = t.struct(
        {
            "webhookSecretVersionName": t.string(),
            "adminAccessTokenVersionName": t.string(),
            "readAccessTokenVersionName": t.string(),
        }
    ).named(renames["BitbucketServerSecretsIn"])
    types["BitbucketServerSecretsOut"] = t.struct(
        {
            "webhookSecretVersionName": t.string(),
            "adminAccessTokenVersionName": t.string(),
            "readAccessTokenVersionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerSecretsOut"])
    types["BitbucketServerConnectedRepositoryIn"] = t.struct(
        {
            "parent": t.string().optional(),
            "repo": t.proxy(renames["BitbucketServerRepositoryIdIn"]).optional(),
        }
    ).named(renames["BitbucketServerConnectedRepositoryIn"])
    types["BitbucketServerConnectedRepositoryOut"] = t.struct(
        {
            "status": t.proxy(renames["StatusOut"]).optional(),
            "parent": t.string().optional(),
            "repo": t.proxy(renames["BitbucketServerRepositoryIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerConnectedRepositoryOut"])
    types["BatchCreateGitLabConnectedRepositoriesResponseIn"] = t.struct(
        {
            "gitlabConnectedRepositories": t.array(
                t.proxy(renames["GitLabConnectedRepositoryIn"])
            ).optional()
        }
    ).named(renames["BatchCreateGitLabConnectedRepositoriesResponseIn"])
    types["BatchCreateGitLabConnectedRepositoriesResponseOut"] = t.struct(
        {
            "gitlabConnectedRepositories": t.array(
                t.proxy(renames["GitLabConnectedRepositoryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateGitLabConnectedRepositoriesResponseOut"])
    types["VolumeIn"] = t.struct(
        {"path": t.string().optional(), "name": t.string().optional()}
    ).named(renames["VolumeIn"])
    types["VolumeOut"] = t.struct(
        {
            "path": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeOut"])
    types["ListBuildTriggersResponseIn"] = t.struct(
        {
            "triggers": t.array(t.proxy(renames["BuildTriggerIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBuildTriggersResponseIn"])
    types["ListBuildTriggersResponseOut"] = t.struct(
        {
            "triggers": t.array(t.proxy(renames["BuildTriggerOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBuildTriggersResponseOut"])
    types["ListWorkerPoolsResponseIn"] = t.struct(
        {
            "workerPools": t.array(t.proxy(renames["WorkerPoolIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListWorkerPoolsResponseIn"])
    types["ListWorkerPoolsResponseOut"] = t.struct(
        {
            "workerPools": t.array(t.proxy(renames["WorkerPoolOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkerPoolsResponseOut"])
    types["CreateBitbucketServerConfigOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "completeTime": t.string().optional(),
        }
    ).named(renames["CreateBitbucketServerConfigOperationMetadataIn"])
    types["CreateBitbucketServerConfigOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "completeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateBitbucketServerConfigOperationMetadataOut"])
    types["UpdateGitLabConfigOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "gitlabConfig": t.string().optional(),
        }
    ).named(renames["UpdateGitLabConfigOperationMetadataIn"])
    types["UpdateGitLabConfigOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "gitlabConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateGitLabConfigOperationMetadataOut"])
    types["BitbucketServerConfigIn"] = t.struct(
        {
            "username": t.string().optional(),
            "apiKey": t.string(),
            "hostUri": t.string(),
            "name": t.string().optional(),
            "sslCa": t.string().optional(),
            "secrets": t.proxy(renames["BitbucketServerSecretsIn"]),
            "peeredNetwork": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["BitbucketServerConfigIn"])
    types["BitbucketServerConfigOut"] = t.struct(
        {
            "username": t.string().optional(),
            "apiKey": t.string(),
            "hostUri": t.string(),
            "name": t.string().optional(),
            "sslCa": t.string().optional(),
            "secrets": t.proxy(renames["BitbucketServerSecretsOut"]),
            "peeredNetwork": t.string().optional(),
            "connectedRepositories": t.array(
                t.proxy(renames["BitbucketServerRepositoryIdOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "webhookKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerConfigOut"])
    types["RemoveBitbucketServerConnectedRepositoryRequestIn"] = t.struct(
        {
            "connectedRepository": t.proxy(
                renames["BitbucketServerRepositoryIdIn"]
            ).optional()
        }
    ).named(renames["RemoveBitbucketServerConnectedRepositoryRequestIn"])
    types["RemoveBitbucketServerConnectedRepositoryRequestOut"] = t.struct(
        {
            "connectedRepository": t.proxy(
                renames["BitbucketServerRepositoryIdOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveBitbucketServerConnectedRepositoryRequestOut"])
    types["GitLabEventsConfigIn"] = t.struct(
        {
            "gitlabConfigResource": t.string().optional(),
            "projectNamespace": t.string().optional(),
            "push": t.proxy(renames["PushFilterIn"]).optional(),
            "pullRequest": t.proxy(renames["PullRequestFilterIn"]).optional(),
        }
    ).named(renames["GitLabEventsConfigIn"])
    types["GitLabEventsConfigOut"] = t.struct(
        {
            "gitlabConfigResource": t.string().optional(),
            "projectNamespace": t.string().optional(),
            "gitlabConfig": t.proxy(renames["GitLabConfigOut"]).optional(),
            "push": t.proxy(renames["PushFilterOut"]).optional(),
            "pullRequest": t.proxy(renames["PullRequestFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabEventsConfigOut"])
    types["NpmPackageIn"] = t.struct(
        {"repository": t.string().optional(), "packagePath": t.string().optional()}
    ).named(renames["NpmPackageIn"])
    types["NpmPackageOut"] = t.struct(
        {
            "repository": t.string().optional(),
            "packagePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NpmPackageOut"])
    types["ReceiveTriggerWebhookResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ReceiveTriggerWebhookResponseIn"])
    types["ReceiveTriggerWebhookResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReceiveTriggerWebhookResponseOut"])
    types["UpdateGitHubEnterpriseConfigOperationMetadataIn"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["UpdateGitHubEnterpriseConfigOperationMetadataIn"])
    types["UpdateGitHubEnterpriseConfigOperationMetadataOut"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateGitHubEnterpriseConfigOperationMetadataOut"])
    types["GitSourceIn"] = t.struct(
        {
            "revision": t.string().optional(),
            "url": t.string().optional(),
            "dir": t.string().optional(),
        }
    ).named(renames["GitSourceIn"])
    types["GitSourceOut"] = t.struct(
        {
            "revision": t.string().optional(),
            "url": t.string().optional(),
            "dir": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitSourceOut"])
    types["CreateGitHubEnterpriseConfigOperationMetadataIn"] = t.struct(
        {
            "githubEnterpriseConfig": t.string().optional(),
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
        }
    ).named(renames["CreateGitHubEnterpriseConfigOperationMetadataIn"])
    types["CreateGitHubEnterpriseConfigOperationMetadataOut"] = t.struct(
        {
            "githubEnterpriseConfig": t.string().optional(),
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateGitHubEnterpriseConfigOperationMetadataOut"])
    types["UploadedNpmPackageIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "fileHashes": t.proxy(renames["FileHashesIn"]).optional(),
        }
    ).named(renames["UploadedNpmPackageIn"])
    types["UploadedNpmPackageOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "fileHashes": t.proxy(renames["FileHashesOut"]).optional(),
            "pushTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadedNpmPackageOut"])
    types["PrivatePoolV1ConfigIn"] = t.struct(
        {
            "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
            "workerConfig": t.proxy(renames["WorkerConfigIn"]).optional(),
        }
    ).named(renames["PrivatePoolV1ConfigIn"])
    types["PrivatePoolV1ConfigOut"] = t.struct(
        {
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "workerConfig": t.proxy(renames["WorkerConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivatePoolV1ConfigOut"])
    types["GitHubEnterpriseSecretsIn"] = t.struct(
        {
            "oauthSecretVersionName": t.string().optional(),
            "oauthSecretName": t.string().optional(),
            "privateKeyVersionName": t.string().optional(),
            "oauthClientIdName": t.string().optional(),
            "oauthClientIdVersionName": t.string().optional(),
            "webhookSecretVersionName": t.string().optional(),
            "webhookSecretName": t.string().optional(),
            "privateKeyName": t.string().optional(),
        }
    ).named(renames["GitHubEnterpriseSecretsIn"])
    types["GitHubEnterpriseSecretsOut"] = t.struct(
        {
            "oauthSecretVersionName": t.string().optional(),
            "oauthSecretName": t.string().optional(),
            "privateKeyVersionName": t.string().optional(),
            "oauthClientIdName": t.string().optional(),
            "oauthClientIdVersionName": t.string().optional(),
            "webhookSecretVersionName": t.string().optional(),
            "webhookSecretName": t.string().optional(),
            "privateKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitHubEnterpriseSecretsOut"])
    types["WorkerPoolIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "privatePoolV1Config": t.proxy(renames["PrivatePoolV1ConfigIn"]).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["WorkerPoolIn"])
    types["WorkerPoolOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "uid": t.string().optional(),
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "deleteTime": t.string().optional(),
            "privatePoolV1Config": t.proxy(
                renames["PrivatePoolV1ConfigOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerPoolOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ArtifactsIn"] = t.struct(
        {
            "images": t.array(t.string()).optional(),
            "objects": t.proxy(renames["ArtifactObjectsIn"]).optional(),
            "mavenArtifacts": t.array(t.proxy(renames["MavenArtifactIn"])).optional(),
            "npmPackages": t.array(t.proxy(renames["NpmPackageIn"])).optional(),
            "pythonPackages": t.array(t.proxy(renames["PythonPackageIn"])).optional(),
        }
    ).named(renames["ArtifactsIn"])
    types["ArtifactsOut"] = t.struct(
        {
            "images": t.array(t.string()).optional(),
            "objects": t.proxy(renames["ArtifactObjectsOut"]).optional(),
            "mavenArtifacts": t.array(t.proxy(renames["MavenArtifactOut"])).optional(),
            "npmPackages": t.array(t.proxy(renames["NpmPackageOut"])).optional(),
            "pythonPackages": t.array(t.proxy(renames["PythonPackageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArtifactsOut"])
    types["ListGithubEnterpriseConfigsResponseIn"] = t.struct(
        {"configs": t.array(t.proxy(renames["GitHubEnterpriseConfigIn"])).optional()}
    ).named(renames["ListGithubEnterpriseConfigsResponseIn"])
    types["ListGithubEnterpriseConfigsResponseOut"] = t.struct(
        {
            "configs": t.array(
                t.proxy(renames["GitHubEnterpriseConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGithubEnterpriseConfigsResponseOut"])
    types["TimeSpanIn"] = t.struct(
        {"startTime": t.string().optional(), "endTime": t.string().optional()}
    ).named(renames["TimeSpanIn"])
    types["TimeSpanOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeSpanOut"])
    types["DeleteGitHubEnterpriseConfigOperationMetadataIn"] = t.struct(
        {
            "githubEnterpriseConfig": t.string().optional(),
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
        }
    ).named(renames["DeleteGitHubEnterpriseConfigOperationMetadataIn"])
    types["DeleteGitHubEnterpriseConfigOperationMetadataOut"] = t.struct(
        {
            "githubEnterpriseConfig": t.string().optional(),
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteGitHubEnterpriseConfigOperationMetadataOut"])
    types["BuildOperationMetadataIn"] = t.struct(
        {"build": t.proxy(renames["BuildIn"]).optional()}
    ).named(renames["BuildOperationMetadataIn"])
    types["BuildOperationMetadataOut"] = t.struct(
        {
            "build": t.proxy(renames["BuildOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOperationMetadataOut"])
    types["ApprovalConfigIn"] = t.struct(
        {"approvalRequired": t.boolean().optional()}
    ).named(renames["ApprovalConfigIn"])
    types["ApprovalConfigOut"] = t.struct(
        {
            "approvalRequired": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApprovalConfigOut"])
    types["BuildTriggerIn"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "disabled": t.boolean().optional(),
            "gitlabEnterpriseEventsConfig": t.proxy(
                renames["GitLabEventsConfigIn"]
            ).optional(),
            "triggerTemplate": t.proxy(renames["RepoSourceIn"]).optional(),
            "approvalConfig": t.proxy(renames["ApprovalConfigIn"]).optional(),
            "includeBuildLogs": t.string().optional(),
            "sourceToBuild": t.proxy(renames["GitRepoSourceIn"]).optional(),
            "ignoredFiles": t.array(t.string()).optional(),
            "filter": t.string().optional(),
            "pubsubConfig": t.proxy(renames["PubsubConfigIn"]).optional(),
            "build": t.proxy(renames["BuildIn"]).optional(),
            "name": t.string().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "bitbucketServerTriggerConfig": t.proxy(
                renames["BitbucketServerTriggerConfigIn"]
            ).optional(),
            "resourceName": t.string().optional(),
            "description": t.string().optional(),
            "github": t.proxy(renames["GitHubEventsConfigIn"]).optional(),
            "eventType": t.string().optional(),
            "gitFileSource": t.proxy(renames["GitFileSourceIn"]).optional(),
            "includedFiles": t.array(t.string()).optional(),
            "serviceAccount": t.string().optional(),
            "webhookConfig": t.proxy(renames["WebhookConfigIn"]).optional(),
            "filename": t.string().optional(),
            "repositoryEventConfig": t.proxy(
                renames["RepositoryEventConfigIn"]
            ).optional(),
            "autodetect": t.boolean().optional(),
        }
    ).named(renames["BuildTriggerIn"])
    types["BuildTriggerOut"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "disabled": t.boolean().optional(),
            "gitlabEnterpriseEventsConfig": t.proxy(
                renames["GitLabEventsConfigOut"]
            ).optional(),
            "triggerTemplate": t.proxy(renames["RepoSourceOut"]).optional(),
            "approvalConfig": t.proxy(renames["ApprovalConfigOut"]).optional(),
            "includeBuildLogs": t.string().optional(),
            "sourceToBuild": t.proxy(renames["GitRepoSourceOut"]).optional(),
            "ignoredFiles": t.array(t.string()).optional(),
            "filter": t.string().optional(),
            "pubsubConfig": t.proxy(renames["PubsubConfigOut"]).optional(),
            "build": t.proxy(renames["BuildOut"]).optional(),
            "name": t.string().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "bitbucketServerTriggerConfig": t.proxy(
                renames["BitbucketServerTriggerConfigOut"]
            ).optional(),
            "resourceName": t.string().optional(),
            "description": t.string().optional(),
            "id": t.string().optional(),
            "github": t.proxy(renames["GitHubEventsConfigOut"]).optional(),
            "createTime": t.string().optional(),
            "eventType": t.string().optional(),
            "gitFileSource": t.proxy(renames["GitFileSourceOut"]).optional(),
            "includedFiles": t.array(t.string()).optional(),
            "serviceAccount": t.string().optional(),
            "webhookConfig": t.proxy(renames["WebhookConfigOut"]).optional(),
            "filename": t.string().optional(),
            "repositoryEventConfig": t.proxy(
                renames["RepositoryEventConfigOut"]
            ).optional(),
            "autodetect": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildTriggerOut"])
    types["FileHashesIn"] = t.struct(
        {"fileHash": t.array(t.proxy(renames["HashIn"])).optional()}
    ).named(renames["FileHashesIn"])
    types["FileHashesOut"] = t.struct(
        {
            "fileHash": t.array(t.proxy(renames["HashOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileHashesOut"])
    types["GitLabConfigIn"] = t.struct(
        {
            "name": t.string().optional(),
            "username": t.string().optional(),
            "secrets": t.proxy(renames["GitLabSecretsIn"]),
            "enterpriseConfig": t.proxy(renames["GitLabEnterpriseConfigIn"]).optional(),
            "connectedRepositories": t.array(
                t.proxy(renames["GitLabRepositoryIdIn"])
            ).optional(),
        }
    ).named(renames["GitLabConfigIn"])
    types["GitLabConfigOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "username": t.string().optional(),
            "secrets": t.proxy(renames["GitLabSecretsOut"]),
            "webhookKey": t.string().optional(),
            "enterpriseConfig": t.proxy(
                renames["GitLabEnterpriseConfigOut"]
            ).optional(),
            "connectedRepositories": t.array(
                t.proxy(renames["GitLabRepositoryIdOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabConfigOut"])
    types["BatchCreateGitLabConnectedRepositoriesResponseMetadataIn"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "config": t.string().optional(),
        }
    ).named(renames["BatchCreateGitLabConnectedRepositoriesResponseMetadataIn"])
    types["BatchCreateGitLabConnectedRepositoriesResponseMetadataOut"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "config": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateGitLabConnectedRepositoriesResponseMetadataOut"])

    functions = {}
    functions["projectsBuildsList"] = cloudbuild.post(
        "v1/projects/{projectId}/builds",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string(),
                "secrets": t.array(t.proxy(renames["SecretIn"])).optional(),
                "queueTtl": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "steps": t.array(t.proxy(renames["BuildStepIn"])),
                "options": t.proxy(renames["BuildOptionsIn"]).optional(),
                "serviceAccount": t.string().optional(),
                "artifacts": t.proxy(renames["ArtifactsIn"]).optional(),
                "logsBucket": t.string().optional(),
                "timeout": t.string().optional(),
                "availableSecrets": t.proxy(renames["SecretsIn"]).optional(),
                "source": t.proxy(renames["SourceIn"]).optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "images": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsCancel"] = cloudbuild.post(
        "v1/projects/{projectId}/builds",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string(),
                "secrets": t.array(t.proxy(renames["SecretIn"])).optional(),
                "queueTtl": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "steps": t.array(t.proxy(renames["BuildStepIn"])),
                "options": t.proxy(renames["BuildOptionsIn"]).optional(),
                "serviceAccount": t.string().optional(),
                "artifacts": t.proxy(renames["ArtifactsIn"]).optional(),
                "logsBucket": t.string().optional(),
                "timeout": t.string().optional(),
                "availableSecrets": t.proxy(renames["SecretsIn"]).optional(),
                "source": t.proxy(renames["SourceIn"]).optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "images": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsApprove"] = cloudbuild.post(
        "v1/projects/{projectId}/builds",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string(),
                "secrets": t.array(t.proxy(renames["SecretIn"])).optional(),
                "queueTtl": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "steps": t.array(t.proxy(renames["BuildStepIn"])),
                "options": t.proxy(renames["BuildOptionsIn"]).optional(),
                "serviceAccount": t.string().optional(),
                "artifacts": t.proxy(renames["ArtifactsIn"]).optional(),
                "logsBucket": t.string().optional(),
                "timeout": t.string().optional(),
                "availableSecrets": t.proxy(renames["SecretsIn"]).optional(),
                "source": t.proxy(renames["SourceIn"]).optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "images": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsGet"] = cloudbuild.post(
        "v1/projects/{projectId}/builds",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string(),
                "secrets": t.array(t.proxy(renames["SecretIn"])).optional(),
                "queueTtl": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "steps": t.array(t.proxy(renames["BuildStepIn"])),
                "options": t.proxy(renames["BuildOptionsIn"]).optional(),
                "serviceAccount": t.string().optional(),
                "artifacts": t.proxy(renames["ArtifactsIn"]).optional(),
                "logsBucket": t.string().optional(),
                "timeout": t.string().optional(),
                "availableSecrets": t.proxy(renames["SecretsIn"]).optional(),
                "source": t.proxy(renames["SourceIn"]).optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "images": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsRetry"] = cloudbuild.post(
        "v1/projects/{projectId}/builds",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string(),
                "secrets": t.array(t.proxy(renames["SecretIn"])).optional(),
                "queueTtl": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "steps": t.array(t.proxy(renames["BuildStepIn"])),
                "options": t.proxy(renames["BuildOptionsIn"]).optional(),
                "serviceAccount": t.string().optional(),
                "artifacts": t.proxy(renames["ArtifactsIn"]).optional(),
                "logsBucket": t.string().optional(),
                "timeout": t.string().optional(),
                "availableSecrets": t.proxy(renames["SecretsIn"]).optional(),
                "source": t.proxy(renames["SourceIn"]).optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "images": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsCreate"] = cloudbuild.post(
        "v1/projects/{projectId}/builds",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string(),
                "secrets": t.array(t.proxy(renames["SecretIn"])).optional(),
                "queueTtl": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "steps": t.array(t.proxy(renames["BuildStepIn"])),
                "options": t.proxy(renames["BuildOptionsIn"]).optional(),
                "serviceAccount": t.string().optional(),
                "artifacts": t.proxy(renames["ArtifactsIn"]).optional(),
                "logsBucket": t.string().optional(),
                "timeout": t.string().optional(),
                "availableSecrets": t.proxy(renames["SecretsIn"]).optional(),
                "source": t.proxy(renames["SourceIn"]).optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "images": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGithubEnterpriseConfigsGet"] = cloudbuild.delete(
        "v1/{name}",
        t.struct(
            {
                "configId": t.string().optional(),
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGithubEnterpriseConfigsCreate"] = cloudbuild.delete(
        "v1/{name}",
        t.struct(
            {
                "configId": t.string().optional(),
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGithubEnterpriseConfigsList"] = cloudbuild.delete(
        "v1/{name}",
        t.struct(
            {
                "configId": t.string().optional(),
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGithubEnterpriseConfigsPatch"] = cloudbuild.delete(
        "v1/{name}",
        t.struct(
            {
                "configId": t.string().optional(),
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGithubEnterpriseConfigsDelete"] = cloudbuild.delete(
        "v1/{name}",
        t.struct(
            {
                "configId": t.string().optional(),
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersDelete"] = cloudbuild.post(
        "v1/projects/{projectId}/triggers/{trigger}:webhook",
        t.struct(
            {
                "trigger": t.string().optional(),
                "name": t.string().optional(),
                "secret": t.string().optional(),
                "projectId": t.string().optional(),
                "contentType": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReceiveTriggerWebhookResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersGet"] = cloudbuild.post(
        "v1/projects/{projectId}/triggers/{trigger}:webhook",
        t.struct(
            {
                "trigger": t.string().optional(),
                "name": t.string().optional(),
                "secret": t.string().optional(),
                "projectId": t.string().optional(),
                "contentType": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReceiveTriggerWebhookResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersPatch"] = cloudbuild.post(
        "v1/projects/{projectId}/triggers/{trigger}:webhook",
        t.struct(
            {
                "trigger": t.string().optional(),
                "name": t.string().optional(),
                "secret": t.string().optional(),
                "projectId": t.string().optional(),
                "contentType": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReceiveTriggerWebhookResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersRun"] = cloudbuild.post(
        "v1/projects/{projectId}/triggers/{trigger}:webhook",
        t.struct(
            {
                "trigger": t.string().optional(),
                "name": t.string().optional(),
                "secret": t.string().optional(),
                "projectId": t.string().optional(),
                "contentType": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReceiveTriggerWebhookResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersCreate"] = cloudbuild.post(
        "v1/projects/{projectId}/triggers/{trigger}:webhook",
        t.struct(
            {
                "trigger": t.string().optional(),
                "name": t.string().optional(),
                "secret": t.string().optional(),
                "projectId": t.string().optional(),
                "contentType": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReceiveTriggerWebhookResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersList"] = cloudbuild.post(
        "v1/projects/{projectId}/triggers/{trigger}:webhook",
        t.struct(
            {
                "trigger": t.string().optional(),
                "name": t.string().optional(),
                "secret": t.string().optional(),
                "projectId": t.string().optional(),
                "contentType": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReceiveTriggerWebhookResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersWebhook"] = cloudbuild.post(
        "v1/projects/{projectId}/triggers/{trigger}:webhook",
        t.struct(
            {
                "trigger": t.string().optional(),
                "name": t.string().optional(),
                "secret": t.string().optional(),
                "projectId": t.string().optional(),
                "contentType": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReceiveTriggerWebhookResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGithubEnterpriseConfigsGet"] = cloudbuild.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "sslCa": t.string().optional(),
                "appId": t.string(),
                "secrets": t.proxy(renames["GitHubEnterpriseSecretsIn"]).optional(),
                "webhookKey": t.string().optional(),
                "peeredNetwork": t.string().optional(),
                "hostUrl": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGithubEnterpriseConfigsList"] = cloudbuild.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "sslCa": t.string().optional(),
                "appId": t.string(),
                "secrets": t.proxy(renames["GitHubEnterpriseSecretsIn"]).optional(),
                "webhookKey": t.string().optional(),
                "peeredNetwork": t.string().optional(),
                "hostUrl": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGithubEnterpriseConfigsCreate"] = cloudbuild.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "sslCa": t.string().optional(),
                "appId": t.string(),
                "secrets": t.proxy(renames["GitHubEnterpriseSecretsIn"]).optional(),
                "webhookKey": t.string().optional(),
                "peeredNetwork": t.string().optional(),
                "hostUrl": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGithubEnterpriseConfigsDelete"] = cloudbuild.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "sslCa": t.string().optional(),
                "appId": t.string(),
                "secrets": t.proxy(renames["GitHubEnterpriseSecretsIn"]).optional(),
                "webhookKey": t.string().optional(),
                "peeredNetwork": t.string().optional(),
                "hostUrl": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGithubEnterpriseConfigsPatch"] = cloudbuild.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "sslCa": t.string().optional(),
                "appId": t.string(),
                "secrets": t.proxy(renames["GitHubEnterpriseSecretsIn"]).optional(),
                "webhookKey": t.string().optional(),
                "peeredNetwork": t.string().optional(),
                "hostUrl": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersWebhook"] = cloudbuild.post(
        "v1/{name}:run",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "source": t.proxy(renames["RepoSourceIn"]).optional(),
                "triggerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersGet"] = cloudbuild.post(
        "v1/{name}:run",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "source": t.proxy(renames["RepoSourceIn"]).optional(),
                "triggerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersCreate"] = cloudbuild.post(
        "v1/{name}:run",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "source": t.proxy(renames["RepoSourceIn"]).optional(),
                "triggerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersDelete"] = cloudbuild.post(
        "v1/{name}:run",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "source": t.proxy(renames["RepoSourceIn"]).optional(),
                "triggerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersList"] = cloudbuild.post(
        "v1/{name}:run",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "source": t.proxy(renames["RepoSourceIn"]).optional(),
                "triggerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersPatch"] = cloudbuild.post(
        "v1/{name}:run",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "source": t.proxy(renames["RepoSourceIn"]).optional(),
                "triggerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersRun"] = cloudbuild.post(
        "v1/{name}:run",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "source": t.proxy(renames["RepoSourceIn"]).optional(),
                "triggerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsCreate"] = cloudbuild.get(
        "v1/{parent}/builds",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "filter": t.string().optional(),
                "projectId": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBuildsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsGet"] = cloudbuild.get(
        "v1/{parent}/builds",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "filter": t.string().optional(),
                "projectId": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBuildsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsCancel"] = cloudbuild.get(
        "v1/{parent}/builds",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "filter": t.string().optional(),
                "projectId": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBuildsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsApprove"] = cloudbuild.get(
        "v1/{parent}/builds",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "filter": t.string().optional(),
                "projectId": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBuildsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsRetry"] = cloudbuild.get(
        "v1/{parent}/builds",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "filter": t.string().optional(),
                "projectId": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBuildsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsList"] = cloudbuild.get(
        "v1/{parent}/builds",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "filter": t.string().optional(),
                "projectId": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBuildsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBitbucketServerConfigsGet"] = cloudbuild.post(
        "v1/{parent}/bitbucketServerConfigs",
        t.struct(
            {
                "bitbucketServerConfigId": t.string().optional(),
                "parent": t.string(),
                "username": t.string().optional(),
                "apiKey": t.string(),
                "hostUri": t.string(),
                "name": t.string().optional(),
                "sslCa": t.string().optional(),
                "secrets": t.proxy(renames["BitbucketServerSecretsIn"]),
                "peeredNetwork": t.string().optional(),
                "createTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBitbucketServerConfigsPatch"] = cloudbuild.post(
        "v1/{parent}/bitbucketServerConfigs",
        t.struct(
            {
                "bitbucketServerConfigId": t.string().optional(),
                "parent": t.string(),
                "username": t.string().optional(),
                "apiKey": t.string(),
                "hostUri": t.string(),
                "name": t.string().optional(),
                "sslCa": t.string().optional(),
                "secrets": t.proxy(renames["BitbucketServerSecretsIn"]),
                "peeredNetwork": t.string().optional(),
                "createTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBitbucketServerConfigsDelete"] = cloudbuild.post(
        "v1/{parent}/bitbucketServerConfigs",
        t.struct(
            {
                "bitbucketServerConfigId": t.string().optional(),
                "parent": t.string(),
                "username": t.string().optional(),
                "apiKey": t.string(),
                "hostUri": t.string(),
                "name": t.string().optional(),
                "sslCa": t.string().optional(),
                "secrets": t.proxy(renames["BitbucketServerSecretsIn"]),
                "peeredNetwork": t.string().optional(),
                "createTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBitbucketServerConfigsList"] = cloudbuild.post(
        "v1/{parent}/bitbucketServerConfigs",
        t.struct(
            {
                "bitbucketServerConfigId": t.string().optional(),
                "parent": t.string(),
                "username": t.string().optional(),
                "apiKey": t.string(),
                "hostUri": t.string(),
                "name": t.string().optional(),
                "sslCa": t.string().optional(),
                "secrets": t.proxy(renames["BitbucketServerSecretsIn"]),
                "peeredNetwork": t.string().optional(),
                "createTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBitbucketServerConfigsRemoveBitbucketServerConnectedRepository"
    ] = cloudbuild.post(
        "v1/{parent}/bitbucketServerConfigs",
        t.struct(
            {
                "bitbucketServerConfigId": t.string().optional(),
                "parent": t.string(),
                "username": t.string().optional(),
                "apiKey": t.string(),
                "hostUri": t.string(),
                "name": t.string().optional(),
                "sslCa": t.string().optional(),
                "secrets": t.proxy(renames["BitbucketServerSecretsIn"]),
                "peeredNetwork": t.string().optional(),
                "createTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBitbucketServerConfigsCreate"] = cloudbuild.post(
        "v1/{parent}/bitbucketServerConfigs",
        t.struct(
            {
                "bitbucketServerConfigId": t.string().optional(),
                "parent": t.string(),
                "username": t.string().optional(),
                "apiKey": t.string(),
                "hostUri": t.string(),
                "name": t.string().optional(),
                "sslCa": t.string().optional(),
                "secrets": t.proxy(renames["BitbucketServerSecretsIn"]),
                "peeredNetwork": t.string().optional(),
                "createTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBitbucketServerConfigsConnectedRepositoriesBatchCreate"
    ] = cloudbuild.post(
        "v1/{parent}/connectedRepositories:batchCreate",
        t.struct(
            {
                "parent": t.string().optional(),
                "requests": t.array(
                    t.proxy(
                        renames["CreateBitbucketServerConnectedRepositoryRequestIn"]
                    )
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBitbucketServerConfigsReposList"] = cloudbuild.get(
        "v1/{parent}/repos",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBitbucketServerRepositoriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkerPoolsList"] = cloudbuild.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkerPoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkerPoolsPatch"] = cloudbuild.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkerPoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkerPoolsCreate"] = cloudbuild.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkerPoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkerPoolsDelete"] = cloudbuild.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkerPoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkerPoolsGet"] = cloudbuild.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkerPoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = cloudbuild.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = cloudbuild.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGitLabConfigsGet"] = cloudbuild.get(
        "v1/{parent}/gitLabConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGitLabConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGitLabConfigsPatch"] = cloudbuild.get(
        "v1/{parent}/gitLabConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGitLabConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGitLabConfigsDelete"] = cloudbuild.get(
        "v1/{parent}/gitLabConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGitLabConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGitLabConfigsCreate"] = cloudbuild.get(
        "v1/{parent}/gitLabConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGitLabConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGitLabConfigsRemoveGitLabConnectedRepository"
    ] = cloudbuild.get(
        "v1/{parent}/gitLabConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGitLabConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGitLabConfigsList"] = cloudbuild.get(
        "v1/{parent}/gitLabConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGitLabConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGitLabConfigsReposList"] = cloudbuild.get(
        "v1/{parent}/repos",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGitLabRepositoriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGitLabConfigsConnectedRepositoriesBatchCreate"
    ] = cloudbuild.post(
        "v1/{parent}/connectedRepositories:batchCreate",
        t.struct(
            {
                "parent": t.string().optional(),
                "requests": t.array(
                    t.proxy(renames["CreateGitLabConnectedRepositoryRequestIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1Webhook"] = cloudbuild.post(
        "v1/webhook",
        t.struct(
            {
                "webhookKey": t.string().optional(),
                "contentType": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = cloudbuild.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = cloudbuild.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["githubDotComWebhookReceive"] = cloudbuild.post(
        "v1/githubDotComWebhook:receive",
        t.struct(
            {
                "webhookKey": t.string().optional(),
                "contentType": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsRegionalWebhook"] = cloudbuild.post(
        "v1/{location}/regionalWebhook",
        t.struct(
            {
                "webhookKey": t.string().optional(),
                "location": t.string(),
                "contentType": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudbuild",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
