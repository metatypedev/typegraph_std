from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_cloudbuild() -> Import:
    cloudbuild = HTTPRuntime("https://cloudbuild.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudbuild_1_ErrorResponse",
        "WarningIn": "_cloudbuild_2_WarningIn",
        "WarningOut": "_cloudbuild_3_WarningOut",
        "ListGitLabConfigsResponseIn": "_cloudbuild_4_ListGitLabConfigsResponseIn",
        "ListGitLabConfigsResponseOut": "_cloudbuild_5_ListGitLabConfigsResponseOut",
        "GitHubEventsConfigIn": "_cloudbuild_6_GitHubEventsConfigIn",
        "GitHubEventsConfigOut": "_cloudbuild_7_GitHubEventsConfigOut",
        "CreateBitbucketServerConfigOperationMetadataIn": "_cloudbuild_8_CreateBitbucketServerConfigOperationMetadataIn",
        "CreateBitbucketServerConfigOperationMetadataOut": "_cloudbuild_9_CreateBitbucketServerConfigOperationMetadataOut",
        "CreateGitHubEnterpriseConfigOperationMetadataIn": "_cloudbuild_10_CreateGitHubEnterpriseConfigOperationMetadataIn",
        "CreateGitHubEnterpriseConfigOperationMetadataOut": "_cloudbuild_11_CreateGitHubEnterpriseConfigOperationMetadataOut",
        "WorkerConfigIn": "_cloudbuild_12_WorkerConfigIn",
        "WorkerConfigOut": "_cloudbuild_13_WorkerConfigOut",
        "PushFilterIn": "_cloudbuild_14_PushFilterIn",
        "PushFilterOut": "_cloudbuild_15_PushFilterOut",
        "BatchCreateBitbucketServerConnectedRepositoriesResponseIn": "_cloudbuild_16_BatchCreateBitbucketServerConnectedRepositoriesResponseIn",
        "BatchCreateBitbucketServerConnectedRepositoriesResponseOut": "_cloudbuild_17_BatchCreateBitbucketServerConnectedRepositoriesResponseOut",
        "InlineSecretIn": "_cloudbuild_18_InlineSecretIn",
        "InlineSecretOut": "_cloudbuild_19_InlineSecretOut",
        "DeleteWorkerPoolOperationMetadataIn": "_cloudbuild_20_DeleteWorkerPoolOperationMetadataIn",
        "DeleteWorkerPoolOperationMetadataOut": "_cloudbuild_21_DeleteWorkerPoolOperationMetadataOut",
        "BatchCreateBitbucketServerConnectedRepositoriesRequestIn": "_cloudbuild_22_BatchCreateBitbucketServerConnectedRepositoriesRequestIn",
        "BatchCreateBitbucketServerConnectedRepositoriesRequestOut": "_cloudbuild_23_BatchCreateBitbucketServerConnectedRepositoriesRequestOut",
        "RemoveBitbucketServerConnectedRepositoryRequestIn": "_cloudbuild_24_RemoveBitbucketServerConnectedRepositoryRequestIn",
        "RemoveBitbucketServerConnectedRepositoryRequestOut": "_cloudbuild_25_RemoveBitbucketServerConnectedRepositoryRequestOut",
        "GitHubEnterpriseSecretsIn": "_cloudbuild_26_GitHubEnterpriseSecretsIn",
        "GitHubEnterpriseSecretsOut": "_cloudbuild_27_GitHubEnterpriseSecretsOut",
        "BuildOperationMetadataIn": "_cloudbuild_28_BuildOperationMetadataIn",
        "BuildOperationMetadataOut": "_cloudbuild_29_BuildOperationMetadataOut",
        "ResultsIn": "_cloudbuild_30_ResultsIn",
        "ResultsOut": "_cloudbuild_31_ResultsOut",
        "StorageSourceIn": "_cloudbuild_32_StorageSourceIn",
        "StorageSourceOut": "_cloudbuild_33_StorageSourceOut",
        "WorkerPoolIn": "_cloudbuild_34_WorkerPoolIn",
        "WorkerPoolOut": "_cloudbuild_35_WorkerPoolOut",
        "SecretManagerSecretIn": "_cloudbuild_36_SecretManagerSecretIn",
        "SecretManagerSecretOut": "_cloudbuild_37_SecretManagerSecretOut",
        "BatchCreateGitLabConnectedRepositoriesRequestIn": "_cloudbuild_38_BatchCreateGitLabConnectedRepositoriesRequestIn",
        "BatchCreateGitLabConnectedRepositoriesRequestOut": "_cloudbuild_39_BatchCreateGitLabConnectedRepositoriesRequestOut",
        "ListGithubEnterpriseConfigsResponseIn": "_cloudbuild_40_ListGithubEnterpriseConfigsResponseIn",
        "ListGithubEnterpriseConfigsResponseOut": "_cloudbuild_41_ListGithubEnterpriseConfigsResponseOut",
        "UpdateBitbucketServerConfigOperationMetadataIn": "_cloudbuild_42_UpdateBitbucketServerConfigOperationMetadataIn",
        "UpdateBitbucketServerConfigOperationMetadataOut": "_cloudbuild_43_UpdateBitbucketServerConfigOperationMetadataOut",
        "BitbucketServerConnectedRepositoryIn": "_cloudbuild_44_BitbucketServerConnectedRepositoryIn",
        "BitbucketServerConnectedRepositoryOut": "_cloudbuild_45_BitbucketServerConnectedRepositoryOut",
        "CreateBitbucketServerConnectedRepositoryRequestIn": "_cloudbuild_46_CreateBitbucketServerConnectedRepositoryRequestIn",
        "CreateBitbucketServerConnectedRepositoryRequestOut": "_cloudbuild_47_CreateBitbucketServerConnectedRepositoryRequestOut",
        "StorageSourceManifestIn": "_cloudbuild_48_StorageSourceManifestIn",
        "StorageSourceManifestOut": "_cloudbuild_49_StorageSourceManifestOut",
        "MavenArtifactIn": "_cloudbuild_50_MavenArtifactIn",
        "MavenArtifactOut": "_cloudbuild_51_MavenArtifactOut",
        "BitbucketServerTriggerConfigIn": "_cloudbuild_52_BitbucketServerTriggerConfigIn",
        "BitbucketServerTriggerConfigOut": "_cloudbuild_53_BitbucketServerTriggerConfigOut",
        "UpdateGitLabConfigOperationMetadataIn": "_cloudbuild_54_UpdateGitLabConfigOperationMetadataIn",
        "UpdateGitLabConfigOperationMetadataOut": "_cloudbuild_55_UpdateGitLabConfigOperationMetadataOut",
        "ApprovalResultIn": "_cloudbuild_56_ApprovalResultIn",
        "ApprovalResultOut": "_cloudbuild_57_ApprovalResultOut",
        "ListGitLabRepositoriesResponseIn": "_cloudbuild_58_ListGitLabRepositoriesResponseIn",
        "ListGitLabRepositoriesResponseOut": "_cloudbuild_59_ListGitLabRepositoriesResponseOut",
        "BitbucketServerSecretsIn": "_cloudbuild_60_BitbucketServerSecretsIn",
        "BitbucketServerSecretsOut": "_cloudbuild_61_BitbucketServerSecretsOut",
        "UploadedNpmPackageIn": "_cloudbuild_62_UploadedNpmPackageIn",
        "UploadedNpmPackageOut": "_cloudbuild_63_UploadedNpmPackageOut",
        "RunBuildTriggerRequestIn": "_cloudbuild_64_RunBuildTriggerRequestIn",
        "RunBuildTriggerRequestOut": "_cloudbuild_65_RunBuildTriggerRequestOut",
        "PullRequestFilterIn": "_cloudbuild_66_PullRequestFilterIn",
        "PullRequestFilterOut": "_cloudbuild_67_PullRequestFilterOut",
        "HttpBodyIn": "_cloudbuild_68_HttpBodyIn",
        "HttpBodyOut": "_cloudbuild_69_HttpBodyOut",
        "GitLabSecretsIn": "_cloudbuild_70_GitLabSecretsIn",
        "GitLabSecretsOut": "_cloudbuild_71_GitLabSecretsOut",
        "UploadedPythonPackageIn": "_cloudbuild_72_UploadedPythonPackageIn",
        "UploadedPythonPackageOut": "_cloudbuild_73_UploadedPythonPackageOut",
        "NpmPackageIn": "_cloudbuild_74_NpmPackageIn",
        "NpmPackageOut": "_cloudbuild_75_NpmPackageOut",
        "SourceProvenanceIn": "_cloudbuild_76_SourceProvenanceIn",
        "SourceProvenanceOut": "_cloudbuild_77_SourceProvenanceOut",
        "RepoSourceIn": "_cloudbuild_78_RepoSourceIn",
        "RepoSourceOut": "_cloudbuild_79_RepoSourceOut",
        "BuildOptionsIn": "_cloudbuild_80_BuildOptionsIn",
        "BuildOptionsOut": "_cloudbuild_81_BuildOptionsOut",
        "DeleteGitLabConfigOperationMetadataIn": "_cloudbuild_82_DeleteGitLabConfigOperationMetadataIn",
        "DeleteGitLabConfigOperationMetadataOut": "_cloudbuild_83_DeleteGitLabConfigOperationMetadataOut",
        "GitLabRepositoryIn": "_cloudbuild_84_GitLabRepositoryIn",
        "GitLabRepositoryOut": "_cloudbuild_85_GitLabRepositoryOut",
        "DeleteBitbucketServerConfigOperationMetadataIn": "_cloudbuild_86_DeleteBitbucketServerConfigOperationMetadataIn",
        "DeleteBitbucketServerConfigOperationMetadataOut": "_cloudbuild_87_DeleteBitbucketServerConfigOperationMetadataOut",
        "GitLabEnterpriseConfigIn": "_cloudbuild_88_GitLabEnterpriseConfigIn",
        "GitLabEnterpriseConfigOut": "_cloudbuild_89_GitLabEnterpriseConfigOut",
        "GitLabEventsConfigIn": "_cloudbuild_90_GitLabEventsConfigIn",
        "GitLabEventsConfigOut": "_cloudbuild_91_GitLabEventsConfigOut",
        "ProcessAppManifestCallbackOperationMetadataIn": "_cloudbuild_92_ProcessAppManifestCallbackOperationMetadataIn",
        "ProcessAppManifestCallbackOperationMetadataOut": "_cloudbuild_93_ProcessAppManifestCallbackOperationMetadataOut",
        "ArtifactsIn": "_cloudbuild_94_ArtifactsIn",
        "ArtifactsOut": "_cloudbuild_95_ArtifactsOut",
        "ApprovalConfigIn": "_cloudbuild_96_ApprovalConfigIn",
        "ApprovalConfigOut": "_cloudbuild_97_ApprovalConfigOut",
        "GitSourceIn": "_cloudbuild_98_GitSourceIn",
        "GitSourceOut": "_cloudbuild_99_GitSourceOut",
        "FileHashesIn": "_cloudbuild_100_FileHashesIn",
        "FileHashesOut": "_cloudbuild_101_FileHashesOut",
        "HashIn": "_cloudbuild_102_HashIn",
        "HashOut": "_cloudbuild_103_HashOut",
        "DeleteGitHubEnterpriseConfigOperationMetadataIn": "_cloudbuild_104_DeleteGitHubEnterpriseConfigOperationMetadataIn",
        "DeleteGitHubEnterpriseConfigOperationMetadataOut": "_cloudbuild_105_DeleteGitHubEnterpriseConfigOperationMetadataOut",
        "BuildIn": "_cloudbuild_106_BuildIn",
        "BuildOut": "_cloudbuild_107_BuildOut",
        "ArtifactResultIn": "_cloudbuild_108_ArtifactResultIn",
        "ArtifactResultOut": "_cloudbuild_109_ArtifactResultOut",
        "NetworkConfigIn": "_cloudbuild_110_NetworkConfigIn",
        "NetworkConfigOut": "_cloudbuild_111_NetworkConfigOut",
        "PoolOptionIn": "_cloudbuild_112_PoolOptionIn",
        "PoolOptionOut": "_cloudbuild_113_PoolOptionOut",
        "GitLabConfigIn": "_cloudbuild_114_GitLabConfigIn",
        "GitLabConfigOut": "_cloudbuild_115_GitLabConfigOut",
        "CancelOperationRequestIn": "_cloudbuild_116_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_cloudbuild_117_CancelOperationRequestOut",
        "BatchCreateGitLabConnectedRepositoriesResponseMetadataIn": "_cloudbuild_118_BatchCreateGitLabConnectedRepositoriesResponseMetadataIn",
        "BatchCreateGitLabConnectedRepositoriesResponseMetadataOut": "_cloudbuild_119_BatchCreateGitLabConnectedRepositoriesResponseMetadataOut",
        "UploadedMavenArtifactIn": "_cloudbuild_120_UploadedMavenArtifactIn",
        "UploadedMavenArtifactOut": "_cloudbuild_121_UploadedMavenArtifactOut",
        "GitFileSourceIn": "_cloudbuild_122_GitFileSourceIn",
        "GitFileSourceOut": "_cloudbuild_123_GitFileSourceOut",
        "BitbucketServerConfigIn": "_cloudbuild_124_BitbucketServerConfigIn",
        "BitbucketServerConfigOut": "_cloudbuild_125_BitbucketServerConfigOut",
        "PrivatePoolV1ConfigIn": "_cloudbuild_126_PrivatePoolV1ConfigIn",
        "PrivatePoolV1ConfigOut": "_cloudbuild_127_PrivatePoolV1ConfigOut",
        "VolumeIn": "_cloudbuild_128_VolumeIn",
        "VolumeOut": "_cloudbuild_129_VolumeOut",
        "StatusIn": "_cloudbuild_130_StatusIn",
        "StatusOut": "_cloudbuild_131_StatusOut",
        "GitLabConnectedRepositoryIn": "_cloudbuild_132_GitLabConnectedRepositoryIn",
        "GitLabConnectedRepositoryOut": "_cloudbuild_133_GitLabConnectedRepositoryOut",
        "RetryBuildRequestIn": "_cloudbuild_134_RetryBuildRequestIn",
        "RetryBuildRequestOut": "_cloudbuild_135_RetryBuildRequestOut",
        "ListBitbucketServerRepositoriesResponseIn": "_cloudbuild_136_ListBitbucketServerRepositoriesResponseIn",
        "ListBitbucketServerRepositoriesResponseOut": "_cloudbuild_137_ListBitbucketServerRepositoriesResponseOut",
        "RemoveGitLabConnectedRepositoryRequestIn": "_cloudbuild_138_RemoveGitLabConnectedRepositoryRequestIn",
        "RemoveGitLabConnectedRepositoryRequestOut": "_cloudbuild_139_RemoveGitLabConnectedRepositoryRequestOut",
        "ServiceDirectoryConfigIn": "_cloudbuild_140_ServiceDirectoryConfigIn",
        "ServiceDirectoryConfigOut": "_cloudbuild_141_ServiceDirectoryConfigOut",
        "ArtifactObjectsIn": "_cloudbuild_142_ArtifactObjectsIn",
        "ArtifactObjectsOut": "_cloudbuild_143_ArtifactObjectsOut",
        "CreateGitLabConfigOperationMetadataIn": "_cloudbuild_144_CreateGitLabConfigOperationMetadataIn",
        "CreateGitLabConfigOperationMetadataOut": "_cloudbuild_145_CreateGitLabConfigOperationMetadataOut",
        "CreateWorkerPoolOperationMetadataIn": "_cloudbuild_146_CreateWorkerPoolOperationMetadataIn",
        "CreateWorkerPoolOperationMetadataOut": "_cloudbuild_147_CreateWorkerPoolOperationMetadataOut",
        "OperationMetadataIn": "_cloudbuild_148_OperationMetadataIn",
        "OperationMetadataOut": "_cloudbuild_149_OperationMetadataOut",
        "BitbucketServerRepositoryIn": "_cloudbuild_150_BitbucketServerRepositoryIn",
        "BitbucketServerRepositoryOut": "_cloudbuild_151_BitbucketServerRepositoryOut",
        "GitLabRepositoryIdIn": "_cloudbuild_152_GitLabRepositoryIdIn",
        "GitLabRepositoryIdOut": "_cloudbuild_153_GitLabRepositoryIdOut",
        "FailureInfoIn": "_cloudbuild_154_FailureInfoIn",
        "FailureInfoOut": "_cloudbuild_155_FailureInfoOut",
        "GitRepoSourceIn": "_cloudbuild_156_GitRepoSourceIn",
        "GitRepoSourceOut": "_cloudbuild_157_GitRepoSourceOut",
        "EmptyIn": "_cloudbuild_158_EmptyIn",
        "EmptyOut": "_cloudbuild_159_EmptyOut",
        "GitHubEnterpriseConfigIn": "_cloudbuild_160_GitHubEnterpriseConfigIn",
        "GitHubEnterpriseConfigOut": "_cloudbuild_161_GitHubEnterpriseConfigOut",
        "TimeSpanIn": "_cloudbuild_162_TimeSpanIn",
        "TimeSpanOut": "_cloudbuild_163_TimeSpanOut",
        "PubsubConfigIn": "_cloudbuild_164_PubsubConfigIn",
        "PubsubConfigOut": "_cloudbuild_165_PubsubConfigOut",
        "SecretIn": "_cloudbuild_166_SecretIn",
        "SecretOut": "_cloudbuild_167_SecretOut",
        "ListBuildTriggersResponseIn": "_cloudbuild_168_ListBuildTriggersResponseIn",
        "ListBuildTriggersResponseOut": "_cloudbuild_169_ListBuildTriggersResponseOut",
        "UpdateWorkerPoolOperationMetadataIn": "_cloudbuild_170_UpdateWorkerPoolOperationMetadataIn",
        "UpdateWorkerPoolOperationMetadataOut": "_cloudbuild_171_UpdateWorkerPoolOperationMetadataOut",
        "OperationIn": "_cloudbuild_172_OperationIn",
        "OperationOut": "_cloudbuild_173_OperationOut",
        "BuiltImageIn": "_cloudbuild_174_BuiltImageIn",
        "BuiltImageOut": "_cloudbuild_175_BuiltImageOut",
        "BuildApprovalIn": "_cloudbuild_176_BuildApprovalIn",
        "BuildApprovalOut": "_cloudbuild_177_BuildApprovalOut",
        "ReceiveTriggerWebhookResponseIn": "_cloudbuild_178_ReceiveTriggerWebhookResponseIn",
        "ReceiveTriggerWebhookResponseOut": "_cloudbuild_179_ReceiveTriggerWebhookResponseOut",
        "ApproveBuildRequestIn": "_cloudbuild_180_ApproveBuildRequestIn",
        "ApproveBuildRequestOut": "_cloudbuild_181_ApproveBuildRequestOut",
        "UpdateGitHubEnterpriseConfigOperationMetadataIn": "_cloudbuild_182_UpdateGitHubEnterpriseConfigOperationMetadataIn",
        "UpdateGitHubEnterpriseConfigOperationMetadataOut": "_cloudbuild_183_UpdateGitHubEnterpriseConfigOperationMetadataOut",
        "PythonPackageIn": "_cloudbuild_184_PythonPackageIn",
        "PythonPackageOut": "_cloudbuild_185_PythonPackageOut",
        "BitbucketServerRepositoryIdIn": "_cloudbuild_186_BitbucketServerRepositoryIdIn",
        "BitbucketServerRepositoryIdOut": "_cloudbuild_187_BitbucketServerRepositoryIdOut",
        "RepositoryEventConfigIn": "_cloudbuild_188_RepositoryEventConfigIn",
        "RepositoryEventConfigOut": "_cloudbuild_189_RepositoryEventConfigOut",
        "BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataIn": "_cloudbuild_190_BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataIn",
        "BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataOut": "_cloudbuild_191_BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataOut",
        "CreateGitLabConnectedRepositoryRequestIn": "_cloudbuild_192_CreateGitLabConnectedRepositoryRequestIn",
        "CreateGitLabConnectedRepositoryRequestOut": "_cloudbuild_193_CreateGitLabConnectedRepositoryRequestOut",
        "BuildTriggerIn": "_cloudbuild_194_BuildTriggerIn",
        "BuildTriggerOut": "_cloudbuild_195_BuildTriggerOut",
        "WebhookConfigIn": "_cloudbuild_196_WebhookConfigIn",
        "WebhookConfigOut": "_cloudbuild_197_WebhookConfigOut",
        "SourceIn": "_cloudbuild_198_SourceIn",
        "SourceOut": "_cloudbuild_199_SourceOut",
        "SecretsIn": "_cloudbuild_200_SecretsIn",
        "SecretsOut": "_cloudbuild_201_SecretsOut",
        "BatchCreateGitLabConnectedRepositoriesResponseIn": "_cloudbuild_202_BatchCreateGitLabConnectedRepositoriesResponseIn",
        "BatchCreateGitLabConnectedRepositoriesResponseOut": "_cloudbuild_203_BatchCreateGitLabConnectedRepositoriesResponseOut",
        "CancelBuildRequestIn": "_cloudbuild_204_CancelBuildRequestIn",
        "CancelBuildRequestOut": "_cloudbuild_205_CancelBuildRequestOut",
        "BuildStepIn": "_cloudbuild_206_BuildStepIn",
        "BuildStepOut": "_cloudbuild_207_BuildStepOut",
        "ListBitbucketServerConfigsResponseIn": "_cloudbuild_208_ListBitbucketServerConfigsResponseIn",
        "ListBitbucketServerConfigsResponseOut": "_cloudbuild_209_ListBitbucketServerConfigsResponseOut",
        "ListBuildsResponseIn": "_cloudbuild_210_ListBuildsResponseIn",
        "ListBuildsResponseOut": "_cloudbuild_211_ListBuildsResponseOut",
        "ListWorkerPoolsResponseIn": "_cloudbuild_212_ListWorkerPoolsResponseIn",
        "ListWorkerPoolsResponseOut": "_cloudbuild_213_ListWorkerPoolsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ListGitLabConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "gitlabConfigs": t.array(t.proxy(renames["GitLabConfigIn"])).optional(),
        }
    ).named(renames["ListGitLabConfigsResponseIn"])
    types["ListGitLabConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "gitlabConfigs": t.array(t.proxy(renames["GitLabConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGitLabConfigsResponseOut"])
    types["GitHubEventsConfigIn"] = t.struct(
        {
            "pullRequest": t.proxy(renames["PullRequestFilterIn"]).optional(),
            "installationId": t.string().optional(),
            "name": t.string().optional(),
            "owner": t.string().optional(),
            "push": t.proxy(renames["PushFilterIn"]).optional(),
            "enterpriseConfigResourceName": t.string().optional(),
        }
    ).named(renames["GitHubEventsConfigIn"])
    types["GitHubEventsConfigOut"] = t.struct(
        {
            "pullRequest": t.proxy(renames["PullRequestFilterOut"]).optional(),
            "installationId": t.string().optional(),
            "name": t.string().optional(),
            "owner": t.string().optional(),
            "push": t.proxy(renames["PushFilterOut"]).optional(),
            "enterpriseConfigResourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitHubEventsConfigOut"])
    types["CreateBitbucketServerConfigOperationMetadataIn"] = t.struct(
        {
            "bitbucketServerConfig": t.string().optional(),
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["CreateBitbucketServerConfigOperationMetadataIn"])
    types["CreateBitbucketServerConfigOperationMetadataOut"] = t.struct(
        {
            "bitbucketServerConfig": t.string().optional(),
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateBitbucketServerConfigOperationMetadataOut"])
    types["CreateGitHubEnterpriseConfigOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
        }
    ).named(renames["CreateGitHubEnterpriseConfigOperationMetadataIn"])
    types["CreateGitHubEnterpriseConfigOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateGitHubEnterpriseConfigOperationMetadataOut"])
    types["WorkerConfigIn"] = t.struct(
        {"diskSizeGb": t.string().optional(), "machineType": t.string().optional()}
    ).named(renames["WorkerConfigIn"])
    types["WorkerConfigOut"] = t.struct(
        {
            "diskSizeGb": t.string().optional(),
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerConfigOut"])
    types["PushFilterIn"] = t.struct(
        {
            "tag": t.string().optional(),
            "branch": t.string().optional(),
            "invertRegex": t.boolean().optional(),
        }
    ).named(renames["PushFilterIn"])
    types["PushFilterOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "branch": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PushFilterOut"])
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
    types["DeleteWorkerPoolOperationMetadataIn"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "workerPool": t.string().optional(),
        }
    ).named(renames["DeleteWorkerPoolOperationMetadataIn"])
    types["DeleteWorkerPoolOperationMetadataOut"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "workerPool": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteWorkerPoolOperationMetadataOut"])
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
    types["GitHubEnterpriseSecretsIn"] = t.struct(
        {
            "oauthClientIdName": t.string().optional(),
            "webhookSecretName": t.string().optional(),
            "privateKeyVersionName": t.string().optional(),
            "webhookSecretVersionName": t.string().optional(),
            "oauthSecretVersionName": t.string().optional(),
            "oauthClientIdVersionName": t.string().optional(),
            "oauthSecretName": t.string().optional(),
            "privateKeyName": t.string().optional(),
        }
    ).named(renames["GitHubEnterpriseSecretsIn"])
    types["GitHubEnterpriseSecretsOut"] = t.struct(
        {
            "oauthClientIdName": t.string().optional(),
            "webhookSecretName": t.string().optional(),
            "privateKeyVersionName": t.string().optional(),
            "webhookSecretVersionName": t.string().optional(),
            "oauthSecretVersionName": t.string().optional(),
            "oauthClientIdVersionName": t.string().optional(),
            "oauthSecretName": t.string().optional(),
            "privateKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitHubEnterpriseSecretsOut"])
    types["BuildOperationMetadataIn"] = t.struct(
        {"build": t.proxy(renames["BuildIn"]).optional()}
    ).named(renames["BuildOperationMetadataIn"])
    types["BuildOperationMetadataOut"] = t.struct(
        {
            "build": t.proxy(renames["BuildOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOperationMetadataOut"])
    types["ResultsIn"] = t.struct(
        {
            "images": t.array(t.proxy(renames["BuiltImageIn"])).optional(),
            "numArtifacts": t.string().optional(),
            "mavenArtifacts": t.array(
                t.proxy(renames["UploadedMavenArtifactIn"])
            ).optional(),
            "buildStepOutputs": t.array(t.string()).optional(),
            "buildStepImages": t.array(t.string()).optional(),
            "artifactManifest": t.string().optional(),
            "pythonPackages": t.array(
                t.proxy(renames["UploadedPythonPackageIn"])
            ).optional(),
            "npmPackages": t.array(t.proxy(renames["UploadedNpmPackageIn"])).optional(),
            "artifactTiming": t.proxy(renames["TimeSpanIn"]).optional(),
        }
    ).named(renames["ResultsIn"])
    types["ResultsOut"] = t.struct(
        {
            "images": t.array(t.proxy(renames["BuiltImageOut"])).optional(),
            "numArtifacts": t.string().optional(),
            "mavenArtifacts": t.array(
                t.proxy(renames["UploadedMavenArtifactOut"])
            ).optional(),
            "buildStepOutputs": t.array(t.string()).optional(),
            "buildStepImages": t.array(t.string()).optional(),
            "artifactManifest": t.string().optional(),
            "pythonPackages": t.array(
                t.proxy(renames["UploadedPythonPackageOut"])
            ).optional(),
            "npmPackages": t.array(
                t.proxy(renames["UploadedNpmPackageOut"])
            ).optional(),
            "artifactTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultsOut"])
    types["StorageSourceIn"] = t.struct(
        {
            "generation": t.string().optional(),
            "object": t.string().optional(),
            "bucket": t.string().optional(),
        }
    ).named(renames["StorageSourceIn"])
    types["StorageSourceOut"] = t.struct(
        {
            "generation": t.string().optional(),
            "object": t.string().optional(),
            "bucket": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StorageSourceOut"])
    types["WorkerPoolIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "privatePoolV1Config": t.proxy(renames["PrivatePoolV1ConfigIn"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["WorkerPoolIn"])
    types["WorkerPoolOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "deleteTime": t.string().optional(),
            "privatePoolV1Config": t.proxy(
                renames["PrivatePoolV1ConfigOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "uid": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerPoolOut"])
    types["SecretManagerSecretIn"] = t.struct(
        {"env": t.string().optional(), "versionName": t.string().optional()}
    ).named(renames["SecretManagerSecretIn"])
    types["SecretManagerSecretOut"] = t.struct(
        {
            "env": t.string().optional(),
            "versionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretManagerSecretOut"])
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
    types["UpdateBitbucketServerConfigOperationMetadataIn"] = t.struct(
        {
            "bitbucketServerConfig": t.string().optional(),
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["UpdateBitbucketServerConfigOperationMetadataIn"])
    types["UpdateBitbucketServerConfigOperationMetadataOut"] = t.struct(
        {
            "bitbucketServerConfig": t.string().optional(),
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBitbucketServerConfigOperationMetadataOut"])
    types["BitbucketServerConnectedRepositoryIn"] = t.struct(
        {
            "parent": t.string().optional(),
            "repo": t.proxy(renames["BitbucketServerRepositoryIdIn"]).optional(),
        }
    ).named(renames["BitbucketServerConnectedRepositoryIn"])
    types["BitbucketServerConnectedRepositoryOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "repo": t.proxy(renames["BitbucketServerRepositoryIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerConnectedRepositoryOut"])
    types["CreateBitbucketServerConnectedRepositoryRequestIn"] = t.struct(
        {
            "parent": t.string(),
            "bitbucketServerConnectedRepository": t.proxy(
                renames["BitbucketServerConnectedRepositoryIn"]
            ),
        }
    ).named(renames["CreateBitbucketServerConnectedRepositoryRequestIn"])
    types["CreateBitbucketServerConnectedRepositoryRequestOut"] = t.struct(
        {
            "parent": t.string(),
            "bitbucketServerConnectedRepository": t.proxy(
                renames["BitbucketServerConnectedRepositoryOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateBitbucketServerConnectedRepositoryRequestOut"])
    types["StorageSourceManifestIn"] = t.struct(
        {
            "bucket": t.string().optional(),
            "generation": t.string().optional(),
            "object": t.string().optional(),
        }
    ).named(renames["StorageSourceManifestIn"])
    types["StorageSourceManifestOut"] = t.struct(
        {
            "bucket": t.string().optional(),
            "generation": t.string().optional(),
            "object": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StorageSourceManifestOut"])
    types["MavenArtifactIn"] = t.struct(
        {
            "version": t.string().optional(),
            "artifactId": t.string().optional(),
            "path": t.string().optional(),
            "repository": t.string().optional(),
            "groupId": t.string().optional(),
        }
    ).named(renames["MavenArtifactIn"])
    types["MavenArtifactOut"] = t.struct(
        {
            "version": t.string().optional(),
            "artifactId": t.string().optional(),
            "path": t.string().optional(),
            "repository": t.string().optional(),
            "groupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MavenArtifactOut"])
    types["BitbucketServerTriggerConfigIn"] = t.struct(
        {
            "projectKey": t.string(),
            "push": t.proxy(renames["PushFilterIn"]).optional(),
            "pullRequest": t.proxy(renames["PullRequestFilterIn"]).optional(),
            "repoSlug": t.string(),
            "bitbucketServerConfigResource": t.string(),
        }
    ).named(renames["BitbucketServerTriggerConfigIn"])
    types["BitbucketServerTriggerConfigOut"] = t.struct(
        {
            "projectKey": t.string(),
            "push": t.proxy(renames["PushFilterOut"]).optional(),
            "pullRequest": t.proxy(renames["PullRequestFilterOut"]).optional(),
            "bitbucketServerConfig": t.proxy(
                renames["BitbucketServerConfigOut"]
            ).optional(),
            "repoSlug": t.string(),
            "bitbucketServerConfigResource": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerTriggerConfigOut"])
    types["UpdateGitLabConfigOperationMetadataIn"] = t.struct(
        {
            "gitlabConfig": t.string().optional(),
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
        }
    ).named(renames["UpdateGitLabConfigOperationMetadataIn"])
    types["UpdateGitLabConfigOperationMetadataOut"] = t.struct(
        {
            "gitlabConfig": t.string().optional(),
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateGitLabConfigOperationMetadataOut"])
    types["ApprovalResultIn"] = t.struct(
        {
            "decision": t.string(),
            "url": t.string().optional(),
            "comment": t.string().optional(),
        }
    ).named(renames["ApprovalResultIn"])
    types["ApprovalResultOut"] = t.struct(
        {
            "approvalTime": t.string().optional(),
            "decision": t.string(),
            "url": t.string().optional(),
            "comment": t.string().optional(),
            "approverAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApprovalResultOut"])
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
    types["BitbucketServerSecretsIn"] = t.struct(
        {
            "webhookSecretVersionName": t.string(),
            "readAccessTokenVersionName": t.string(),
            "adminAccessTokenVersionName": t.string(),
        }
    ).named(renames["BitbucketServerSecretsIn"])
    types["BitbucketServerSecretsOut"] = t.struct(
        {
            "webhookSecretVersionName": t.string(),
            "readAccessTokenVersionName": t.string(),
            "adminAccessTokenVersionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerSecretsOut"])
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
    types["PullRequestFilterIn"] = t.struct(
        {
            "commentControl": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "branch": t.string().optional(),
        }
    ).named(renames["PullRequestFilterIn"])
    types["PullRequestFilterOut"] = t.struct(
        {
            "commentControl": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "branch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PullRequestFilterOut"])
    types["HttpBodyIn"] = t.struct(
        {
            "data": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "contentType": t.string().optional(),
        }
    ).named(renames["HttpBodyIn"])
    types["HttpBodyOut"] = t.struct(
        {
            "data": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "contentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpBodyOut"])
    types["GitLabSecretsIn"] = t.struct(
        {
            "apiKeyVersion": t.string(),
            "apiAccessTokenVersion": t.string(),
            "webhookSecretVersion": t.string(),
            "readAccessTokenVersion": t.string(),
        }
    ).named(renames["GitLabSecretsIn"])
    types["GitLabSecretsOut"] = t.struct(
        {
            "apiKeyVersion": t.string(),
            "apiAccessTokenVersion": t.string(),
            "webhookSecretVersion": t.string(),
            "readAccessTokenVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabSecretsOut"])
    types["UploadedPythonPackageIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "fileHashes": t.proxy(renames["FileHashesIn"]).optional(),
        }
    ).named(renames["UploadedPythonPackageIn"])
    types["UploadedPythonPackageOut"] = t.struct(
        {
            "pushTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "uri": t.string().optional(),
            "fileHashes": t.proxy(renames["FileHashesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadedPythonPackageOut"])
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
    types["SourceProvenanceIn"] = t.struct(
        {
            "resolvedStorageSourceManifest": t.proxy(
                renames["StorageSourceManifestIn"]
            ).optional(),
            "resolvedStorageSource": t.proxy(renames["StorageSourceIn"]).optional(),
            "resolvedRepoSource": t.proxy(renames["RepoSourceIn"]).optional(),
        }
    ).named(renames["SourceProvenanceIn"])
    types["SourceProvenanceOut"] = t.struct(
        {
            "resolvedStorageSourceManifest": t.proxy(
                renames["StorageSourceManifestOut"]
            ).optional(),
            "resolvedStorageSource": t.proxy(renames["StorageSourceOut"]).optional(),
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "resolvedRepoSource": t.proxy(renames["RepoSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceProvenanceOut"])
    types["RepoSourceIn"] = t.struct(
        {
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "tagName": t.string().optional(),
            "projectId": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "repoName": t.string().optional(),
            "dir": t.string().optional(),
            "commitSha": t.string().optional(),
            "branchName": t.string().optional(),
        }
    ).named(renames["RepoSourceIn"])
    types["RepoSourceOut"] = t.struct(
        {
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "tagName": t.string().optional(),
            "projectId": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "repoName": t.string().optional(),
            "dir": t.string().optional(),
            "commitSha": t.string().optional(),
            "branchName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepoSourceOut"])
    types["BuildOptionsIn"] = t.struct(
        {
            "secretEnv": t.array(t.string()).optional(),
            "logging": t.string().optional(),
            "logStreamingOption": t.string().optional(),
            "requestedVerifyOption": t.string().optional(),
            "sourceProvenanceHash": t.array(t.string()).optional(),
            "diskSizeGb": t.string().optional(),
            "defaultLogsBucketBehavior": t.string().optional(),
            "workerPool": t.string().optional(),
            "machineType": t.string().optional(),
            "pool": t.proxy(renames["PoolOptionIn"]).optional(),
            "env": t.array(t.string()).optional(),
            "substitutionOption": t.string().optional(),
            "dynamicSubstitutions": t.boolean().optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
        }
    ).named(renames["BuildOptionsIn"])
    types["BuildOptionsOut"] = t.struct(
        {
            "secretEnv": t.array(t.string()).optional(),
            "logging": t.string().optional(),
            "logStreamingOption": t.string().optional(),
            "requestedVerifyOption": t.string().optional(),
            "sourceProvenanceHash": t.array(t.string()).optional(),
            "diskSizeGb": t.string().optional(),
            "defaultLogsBucketBehavior": t.string().optional(),
            "workerPool": t.string().optional(),
            "machineType": t.string().optional(),
            "pool": t.proxy(renames["PoolOptionOut"]).optional(),
            "env": t.array(t.string()).optional(),
            "substitutionOption": t.string().optional(),
            "dynamicSubstitutions": t.boolean().optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOptionsOut"])
    types["DeleteGitLabConfigOperationMetadataIn"] = t.struct(
        {
            "gitlabConfig": t.string().optional(),
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["DeleteGitLabConfigOperationMetadataIn"])
    types["DeleteGitLabConfigOperationMetadataOut"] = t.struct(
        {
            "gitlabConfig": t.string().optional(),
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteGitLabConfigOperationMetadataOut"])
    types["GitLabRepositoryIn"] = t.struct(
        {
            "browseUri": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "repositoryId": t.proxy(renames["GitLabRepositoryIdIn"]).optional(),
        }
    ).named(renames["GitLabRepositoryIn"])
    types["GitLabRepositoryOut"] = t.struct(
        {
            "browseUri": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "repositoryId": t.proxy(renames["GitLabRepositoryIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabRepositoryOut"])
    types["DeleteBitbucketServerConfigOperationMetadataIn"] = t.struct(
        {
            "bitbucketServerConfig": t.string().optional(),
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["DeleteBitbucketServerConfigOperationMetadataIn"])
    types["DeleteBitbucketServerConfigOperationMetadataOut"] = t.struct(
        {
            "bitbucketServerConfig": t.string().optional(),
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteBitbucketServerConfigOperationMetadataOut"])
    types["GitLabEnterpriseConfigIn"] = t.struct(
        {
            "sslCa": t.string().optional(),
            "hostUri": t.string().optional(),
            "serviceDirectoryConfig": t.proxy(
                renames["ServiceDirectoryConfigIn"]
            ).optional(),
        }
    ).named(renames["GitLabEnterpriseConfigIn"])
    types["GitLabEnterpriseConfigOut"] = t.struct(
        {
            "sslCa": t.string().optional(),
            "hostUri": t.string().optional(),
            "serviceDirectoryConfig": t.proxy(
                renames["ServiceDirectoryConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabEnterpriseConfigOut"])
    types["GitLabEventsConfigIn"] = t.struct(
        {
            "push": t.proxy(renames["PushFilterIn"]).optional(),
            "gitlabConfigResource": t.string().optional(),
            "pullRequest": t.proxy(renames["PullRequestFilterIn"]).optional(),
            "projectNamespace": t.string().optional(),
        }
    ).named(renames["GitLabEventsConfigIn"])
    types["GitLabEventsConfigOut"] = t.struct(
        {
            "push": t.proxy(renames["PushFilterOut"]).optional(),
            "gitlabConfigResource": t.string().optional(),
            "pullRequest": t.proxy(renames["PullRequestFilterOut"]).optional(),
            "projectNamespace": t.string().optional(),
            "gitlabConfig": t.proxy(renames["GitLabConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabEventsConfigOut"])
    types["ProcessAppManifestCallbackOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
        }
    ).named(renames["ProcessAppManifestCallbackOperationMetadataIn"])
    types["ProcessAppManifestCallbackOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProcessAppManifestCallbackOperationMetadataOut"])
    types["ArtifactsIn"] = t.struct(
        {
            "npmPackages": t.array(t.proxy(renames["NpmPackageIn"])).optional(),
            "objects": t.proxy(renames["ArtifactObjectsIn"]).optional(),
            "pythonPackages": t.array(t.proxy(renames["PythonPackageIn"])).optional(),
            "mavenArtifacts": t.array(t.proxy(renames["MavenArtifactIn"])).optional(),
            "images": t.array(t.string()).optional(),
        }
    ).named(renames["ArtifactsIn"])
    types["ArtifactsOut"] = t.struct(
        {
            "npmPackages": t.array(t.proxy(renames["NpmPackageOut"])).optional(),
            "objects": t.proxy(renames["ArtifactObjectsOut"]).optional(),
            "pythonPackages": t.array(t.proxy(renames["PythonPackageOut"])).optional(),
            "mavenArtifacts": t.array(t.proxy(renames["MavenArtifactOut"])).optional(),
            "images": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArtifactsOut"])
    types["ApprovalConfigIn"] = t.struct(
        {"approvalRequired": t.boolean().optional()}
    ).named(renames["ApprovalConfigIn"])
    types["ApprovalConfigOut"] = t.struct(
        {
            "approvalRequired": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApprovalConfigOut"])
    types["GitSourceIn"] = t.struct(
        {
            "url": t.string().optional(),
            "revision": t.string().optional(),
            "dir": t.string().optional(),
        }
    ).named(renames["GitSourceIn"])
    types["GitSourceOut"] = t.struct(
        {
            "url": t.string().optional(),
            "revision": t.string().optional(),
            "dir": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitSourceOut"])
    types["FileHashesIn"] = t.struct(
        {"fileHash": t.array(t.proxy(renames["HashIn"])).optional()}
    ).named(renames["FileHashesIn"])
    types["FileHashesOut"] = t.struct(
        {
            "fileHash": t.array(t.proxy(renames["HashOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileHashesOut"])
    types["HashIn"] = t.struct(
        {"type": t.string().optional(), "value": t.string().optional()}
    ).named(renames["HashIn"])
    types["HashOut"] = t.struct(
        {
            "type": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HashOut"])
    types["DeleteGitHubEnterpriseConfigOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "completeTime": t.string().optional(),
        }
    ).named(renames["DeleteGitHubEnterpriseConfigOperationMetadataIn"])
    types["DeleteGitHubEnterpriseConfigOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "completeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteGitHubEnterpriseConfigOperationMetadataOut"])
    types["BuildIn"] = t.struct(
        {
            "artifacts": t.proxy(renames["ArtifactsIn"]).optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
            "serviceAccount": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "secrets": t.array(t.proxy(renames["SecretIn"])).optional(),
            "availableSecrets": t.proxy(renames["SecretsIn"]).optional(),
            "options": t.proxy(renames["BuildOptionsIn"]).optional(),
            "timeout": t.string().optional(),
            "logsBucket": t.string().optional(),
            "queueTtl": t.string().optional(),
            "steps": t.array(t.proxy(renames["BuildStepIn"])),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "images": t.array(t.string()).optional(),
        }
    ).named(renames["BuildIn"])
    types["BuildOut"] = t.struct(
        {
            "id": t.string().optional(),
            "artifacts": t.proxy(renames["ArtifactsOut"]).optional(),
            "failureInfo": t.proxy(renames["FailureInfoOut"]).optional(),
            "finishTime": t.string().optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "logUrl": t.string().optional(),
            "approval": t.proxy(renames["BuildApprovalOut"]).optional(),
            "serviceAccount": t.string().optional(),
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "buildTriggerId": t.string().optional(),
            "sourceProvenance": t.proxy(renames["SourceProvenanceOut"]).optional(),
            "secrets": t.array(t.proxy(renames["SecretOut"])).optional(),
            "timing": t.struct({"_": t.string().optional()}).optional(),
            "projectId": t.string().optional(),
            "availableSecrets": t.proxy(renames["SecretsOut"]).optional(),
            "statusDetail": t.string().optional(),
            "status": t.string().optional(),
            "warnings": t.array(t.proxy(renames["WarningOut"])).optional(),
            "options": t.proxy(renames["BuildOptionsOut"]).optional(),
            "results": t.proxy(renames["ResultsOut"]).optional(),
            "timeout": t.string().optional(),
            "createTime": t.string().optional(),
            "logsBucket": t.string().optional(),
            "queueTtl": t.string().optional(),
            "steps": t.array(t.proxy(renames["BuildStepOut"])),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "images": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOut"])
    types["ArtifactResultIn"] = t.struct(
        {
            "location": t.string().optional(),
            "fileHash": t.array(t.proxy(renames["FileHashesIn"])).optional(),
        }
    ).named(renames["ArtifactResultIn"])
    types["ArtifactResultOut"] = t.struct(
        {
            "location": t.string().optional(),
            "fileHash": t.array(t.proxy(renames["FileHashesOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArtifactResultOut"])
    types["NetworkConfigIn"] = t.struct(
        {
            "peeredNetwork": t.string(),
            "egressOption": t.string().optional(),
            "peeredNetworkIpRange": t.string().optional(),
        }
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "peeredNetwork": t.string(),
            "egressOption": t.string().optional(),
            "peeredNetworkIpRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["PoolOptionIn"] = t.struct({"name": t.string().optional()}).named(
        renames["PoolOptionIn"]
    )
    types["PoolOptionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoolOptionOut"])
    types["GitLabConfigIn"] = t.struct(
        {
            "secrets": t.proxy(renames["GitLabSecretsIn"]),
            "username": t.string().optional(),
            "enterpriseConfig": t.proxy(renames["GitLabEnterpriseConfigIn"]).optional(),
            "name": t.string().optional(),
            "connectedRepositories": t.array(
                t.proxy(renames["GitLabRepositoryIdIn"])
            ).optional(),
        }
    ).named(renames["GitLabConfigIn"])
    types["GitLabConfigOut"] = t.struct(
        {
            "secrets": t.proxy(renames["GitLabSecretsOut"]),
            "username": t.string().optional(),
            "enterpriseConfig": t.proxy(
                renames["GitLabEnterpriseConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "connectedRepositories": t.array(
                t.proxy(renames["GitLabRepositoryIdOut"])
            ).optional(),
            "webhookKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabConfigOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["UploadedMavenArtifactIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "fileHashes": t.proxy(renames["FileHashesIn"]).optional(),
        }
    ).named(renames["UploadedMavenArtifactIn"])
    types["UploadedMavenArtifactOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "fileHashes": t.proxy(renames["FileHashesOut"]).optional(),
            "pushTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadedMavenArtifactOut"])
    types["GitFileSourceIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "path": t.string().optional(),
            "repository": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "repoType": t.string().optional(),
            "revision": t.string().optional(),
        }
    ).named(renames["GitFileSourceIn"])
    types["GitFileSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "path": t.string().optional(),
            "repository": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "repoType": t.string().optional(),
            "revision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitFileSourceOut"])
    types["BitbucketServerConfigIn"] = t.struct(
        {
            "hostUri": t.string(),
            "sslCa": t.string().optional(),
            "name": t.string().optional(),
            "apiKey": t.string(),
            "createTime": t.string().optional(),
            "peeredNetwork": t.string().optional(),
            "secrets": t.proxy(renames["BitbucketServerSecretsIn"]),
            "username": t.string().optional(),
        }
    ).named(renames["BitbucketServerConfigIn"])
    types["BitbucketServerConfigOut"] = t.struct(
        {
            "hostUri": t.string(),
            "sslCa": t.string().optional(),
            "webhookKey": t.string().optional(),
            "name": t.string().optional(),
            "apiKey": t.string(),
            "createTime": t.string().optional(),
            "peeredNetwork": t.string().optional(),
            "connectedRepositories": t.array(
                t.proxy(renames["BitbucketServerRepositoryIdOut"])
            ).optional(),
            "secrets": t.proxy(renames["BitbucketServerSecretsOut"]),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerConfigOut"])
    types["PrivatePoolV1ConfigIn"] = t.struct(
        {
            "workerConfig": t.proxy(renames["WorkerConfigIn"]).optional(),
            "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
        }
    ).named(renames["PrivatePoolV1ConfigIn"])
    types["PrivatePoolV1ConfigOut"] = t.struct(
        {
            "workerConfig": t.proxy(renames["WorkerConfigOut"]).optional(),
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivatePoolV1ConfigOut"])
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
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["GitLabConnectedRepositoryIn"] = t.struct(
        {
            "repo": t.proxy(renames["GitLabRepositoryIdIn"]).optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["GitLabConnectedRepositoryIn"])
    types["GitLabConnectedRepositoryOut"] = t.struct(
        {
            "repo": t.proxy(renames["GitLabRepositoryIdOut"]).optional(),
            "parent": t.string().optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabConnectedRepositoryOut"])
    types["RetryBuildRequestIn"] = t.struct(
        {"id": t.string(), "projectId": t.string(), "name": t.string().optional()}
    ).named(renames["RetryBuildRequestIn"])
    types["RetryBuildRequestOut"] = t.struct(
        {
            "id": t.string(),
            "projectId": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetryBuildRequestOut"])
    types["ListBitbucketServerRepositoriesResponseIn"] = t.struct(
        {
            "bitbucketServerRepositories": t.array(
                t.proxy(renames["BitbucketServerRepositoryIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBitbucketServerRepositoriesResponseIn"])
    types["ListBitbucketServerRepositoriesResponseOut"] = t.struct(
        {
            "bitbucketServerRepositories": t.array(
                t.proxy(renames["BitbucketServerRepositoryOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBitbucketServerRepositoriesResponseOut"])
    types["RemoveGitLabConnectedRepositoryRequestIn"] = t.struct(
        {"connectedRepository": t.proxy(renames["GitLabRepositoryIdIn"]).optional()}
    ).named(renames["RemoveGitLabConnectedRepositoryRequestIn"])
    types["RemoveGitLabConnectedRepositoryRequestOut"] = t.struct(
        {
            "connectedRepository": t.proxy(renames["GitLabRepositoryIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveGitLabConnectedRepositoryRequestOut"])
    types["ServiceDirectoryConfigIn"] = t.struct(
        {"service": t.string().optional()}
    ).named(renames["ServiceDirectoryConfigIn"])
    types["ServiceDirectoryConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceDirectoryConfigOut"])
    types["ArtifactObjectsIn"] = t.struct(
        {"location": t.string().optional(), "paths": t.array(t.string()).optional()}
    ).named(renames["ArtifactObjectsIn"])
    types["ArtifactObjectsOut"] = t.struct(
        {
            "timing": t.proxy(renames["TimeSpanOut"]).optional(),
            "location": t.string().optional(),
            "paths": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArtifactObjectsOut"])
    types["CreateGitLabConfigOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "gitlabConfig": t.string().optional(),
        }
    ).named(renames["CreateGitLabConfigOperationMetadataIn"])
    types["CreateGitLabConfigOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "gitlabConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateGitLabConfigOperationMetadataOut"])
    types["CreateWorkerPoolOperationMetadataIn"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "workerPool": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["CreateWorkerPoolOperationMetadataIn"])
    types["CreateWorkerPoolOperationMetadataOut"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "workerPool": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateWorkerPoolOperationMetadataOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "statusDetail": t.string().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["BitbucketServerRepositoryIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "browseUri": t.string().optional(),
            "description": t.string().optional(),
            "repoId": t.proxy(renames["BitbucketServerRepositoryIdIn"]).optional(),
        }
    ).named(renames["BitbucketServerRepositoryIn"])
    types["BitbucketServerRepositoryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "browseUri": t.string().optional(),
            "description": t.string().optional(),
            "repoId": t.proxy(renames["BitbucketServerRepositoryIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerRepositoryOut"])
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
    types["GitRepoSourceIn"] = t.struct(
        {
            "githubEnterpriseConfig": t.string().optional(),
            "uri": t.string().optional(),
            "repoType": t.string().optional(),
            "ref": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "repository": t.string().optional(),
        }
    ).named(renames["GitRepoSourceIn"])
    types["GitRepoSourceOut"] = t.struct(
        {
            "githubEnterpriseConfig": t.string().optional(),
            "uri": t.string().optional(),
            "repoType": t.string().optional(),
            "ref": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "repository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitRepoSourceOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GitHubEnterpriseConfigIn"] = t.struct(
        {
            "appId": t.string(),
            "hostUrl": t.string().optional(),
            "sslCa": t.string().optional(),
            "secrets": t.proxy(renames["GitHubEnterpriseSecretsIn"]).optional(),
            "webhookKey": t.string().optional(),
            "displayName": t.string().optional(),
            "peeredNetwork": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GitHubEnterpriseConfigIn"])
    types["GitHubEnterpriseConfigOut"] = t.struct(
        {
            "appId": t.string(),
            "hostUrl": t.string().optional(),
            "createTime": t.string().optional(),
            "sslCa": t.string().optional(),
            "secrets": t.proxy(renames["GitHubEnterpriseSecretsOut"]).optional(),
            "webhookKey": t.string().optional(),
            "displayName": t.string().optional(),
            "peeredNetwork": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitHubEnterpriseConfigOut"])
    types["TimeSpanIn"] = t.struct(
        {"endTime": t.string().optional(), "startTime": t.string().optional()}
    ).named(renames["TimeSpanIn"])
    types["TimeSpanOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeSpanOut"])
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
            "subscription": t.string().optional(),
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubConfigOut"])
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
    types["UpdateWorkerPoolOperationMetadataIn"] = t.struct(
        {
            "workerPool": t.string().optional(),
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["UpdateWorkerPoolOperationMetadataIn"])
    types["UpdateWorkerPoolOperationMetadataOut"] = t.struct(
        {
            "workerPool": t.string().optional(),
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateWorkerPoolOperationMetadataOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["BuildApprovalIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BuildApprovalIn"]
    )
    types["BuildApprovalOut"] = t.struct(
        {
            "config": t.proxy(renames["ApprovalConfigOut"]).optional(),
            "result": t.proxy(renames["ApprovalResultOut"]).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildApprovalOut"])
    types["ReceiveTriggerWebhookResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ReceiveTriggerWebhookResponseIn"])
    types["ReceiveTriggerWebhookResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReceiveTriggerWebhookResponseOut"])
    types["ApproveBuildRequestIn"] = t.struct(
        {"approvalResult": t.proxy(renames["ApprovalResultIn"]).optional()}
    ).named(renames["ApproveBuildRequestIn"])
    types["ApproveBuildRequestOut"] = t.struct(
        {
            "approvalResult": t.proxy(renames["ApprovalResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproveBuildRequestOut"])
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
    types["BitbucketServerRepositoryIdIn"] = t.struct(
        {"repoSlug": t.string(), "projectKey": t.string()}
    ).named(renames["BitbucketServerRepositoryIdIn"])
    types["BitbucketServerRepositoryIdOut"] = t.struct(
        {
            "repoSlug": t.string(),
            "webhookId": t.integer().optional(),
            "projectKey": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerRepositoryIdOut"])
    types["RepositoryEventConfigIn"] = t.struct(
        {
            "pullRequest": t.proxy(renames["PullRequestFilterIn"]).optional(),
            "push": t.proxy(renames["PushFilterIn"]).optional(),
            "repository": t.string().optional(),
        }
    ).named(renames["RepositoryEventConfigIn"])
    types["RepositoryEventConfigOut"] = t.struct(
        {
            "pullRequest": t.proxy(renames["PullRequestFilterOut"]).optional(),
            "push": t.proxy(renames["PushFilterOut"]).optional(),
            "repositoryType": t.string().optional(),
            "repository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepositoryEventConfigOut"])
    types[
        "BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataIn"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "config": t.string().optional(),
        }
    ).named(
        renames["BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataIn"]
    )
    types[
        "BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataOut"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "config": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataOut"]
    )
    types["CreateGitLabConnectedRepositoryRequestIn"] = t.struct(
        {
            "parent": t.string(),
            "gitlabConnectedRepository": t.proxy(
                renames["GitLabConnectedRepositoryIn"]
            ),
        }
    ).named(renames["CreateGitLabConnectedRepositoryRequestIn"])
    types["CreateGitLabConnectedRepositoryRequestOut"] = t.struct(
        {
            "parent": t.string(),
            "gitlabConnectedRepository": t.proxy(
                renames["GitLabConnectedRepositoryOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateGitLabConnectedRepositoryRequestOut"])
    types["BuildTriggerIn"] = t.struct(
        {
            "gitlabEnterpriseEventsConfig": t.proxy(
                renames["GitLabEventsConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "eventType": t.string().optional(),
            "pubsubConfig": t.proxy(renames["PubsubConfigIn"]).optional(),
            "gitFileSource": t.proxy(renames["GitFileSourceIn"]).optional(),
            "description": t.string().optional(),
            "webhookConfig": t.proxy(renames["WebhookConfigIn"]).optional(),
            "filter": t.string().optional(),
            "triggerTemplate": t.proxy(renames["RepoSourceIn"]).optional(),
            "repositoryEventConfig": t.proxy(
                renames["RepositoryEventConfigIn"]
            ).optional(),
            "includedFiles": t.array(t.string()).optional(),
            "filename": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "bitbucketServerTriggerConfig": t.proxy(
                renames["BitbucketServerTriggerConfigIn"]
            ).optional(),
            "serviceAccount": t.string().optional(),
            "ignoredFiles": t.array(t.string()).optional(),
            "build": t.proxy(renames["BuildIn"]).optional(),
            "disabled": t.boolean().optional(),
            "approvalConfig": t.proxy(renames["ApprovalConfigIn"]).optional(),
            "autodetect": t.boolean().optional(),
            "includeBuildLogs": t.string().optional(),
            "resourceName": t.string().optional(),
            "sourceToBuild": t.proxy(renames["GitRepoSourceIn"]).optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "github": t.proxy(renames["GitHubEventsConfigIn"]).optional(),
        }
    ).named(renames["BuildTriggerIn"])
    types["BuildTriggerOut"] = t.struct(
        {
            "gitlabEnterpriseEventsConfig": t.proxy(
                renames["GitLabEventsConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "eventType": t.string().optional(),
            "pubsubConfig": t.proxy(renames["PubsubConfigOut"]).optional(),
            "gitFileSource": t.proxy(renames["GitFileSourceOut"]).optional(),
            "description": t.string().optional(),
            "webhookConfig": t.proxy(renames["WebhookConfigOut"]).optional(),
            "filter": t.string().optional(),
            "triggerTemplate": t.proxy(renames["RepoSourceOut"]).optional(),
            "repositoryEventConfig": t.proxy(
                renames["RepositoryEventConfigOut"]
            ).optional(),
            "includedFiles": t.array(t.string()).optional(),
            "filename": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "bitbucketServerTriggerConfig": t.proxy(
                renames["BitbucketServerTriggerConfigOut"]
            ).optional(),
            "serviceAccount": t.string().optional(),
            "ignoredFiles": t.array(t.string()).optional(),
            "build": t.proxy(renames["BuildOut"]).optional(),
            "disabled": t.boolean().optional(),
            "approvalConfig": t.proxy(renames["ApprovalConfigOut"]).optional(),
            "autodetect": t.boolean().optional(),
            "createTime": t.string().optional(),
            "includeBuildLogs": t.string().optional(),
            "resourceName": t.string().optional(),
            "sourceToBuild": t.proxy(renames["GitRepoSourceOut"]).optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "github": t.proxy(renames["GitHubEventsConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildTriggerOut"])
    types["WebhookConfigIn"] = t.struct(
        {"secret": t.string(), "state": t.string().optional()}
    ).named(renames["WebhookConfigIn"])
    types["WebhookConfigOut"] = t.struct(
        {
            "secret": t.string(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebhookConfigOut"])
    types["SourceIn"] = t.struct(
        {
            "storageSourceManifest": t.proxy(
                renames["StorageSourceManifestIn"]
            ).optional(),
            "repoSource": t.proxy(renames["RepoSourceIn"]).optional(),
            "storageSource": t.proxy(renames["StorageSourceIn"]).optional(),
            "gitSource": t.proxy(renames["GitSourceIn"]).optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "storageSourceManifest": t.proxy(
                renames["StorageSourceManifestOut"]
            ).optional(),
            "repoSource": t.proxy(renames["RepoSourceOut"]).optional(),
            "storageSource": t.proxy(renames["StorageSourceOut"]).optional(),
            "gitSource": t.proxy(renames["GitSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["SecretsIn"] = t.struct(
        {
            "inline": t.array(t.proxy(renames["InlineSecretIn"])).optional(),
            "secretManager": t.array(
                t.proxy(renames["SecretManagerSecretIn"])
            ).optional(),
        }
    ).named(renames["SecretsIn"])
    types["SecretsOut"] = t.struct(
        {
            "inline": t.array(t.proxy(renames["InlineSecretOut"])).optional(),
            "secretManager": t.array(
                t.proxy(renames["SecretManagerSecretOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretsOut"])
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
    types["CancelBuildRequestIn"] = t.struct(
        {"projectId": t.string(), "name": t.string().optional(), "id": t.string()}
    ).named(renames["CancelBuildRequestIn"])
    types["CancelBuildRequestOut"] = t.struct(
        {
            "projectId": t.string(),
            "name": t.string().optional(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CancelBuildRequestOut"])
    types["BuildStepIn"] = t.struct(
        {
            "secretEnv": t.array(t.string()).optional(),
            "timeout": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "name": t.string(),
            "entrypoint": t.string().optional(),
            "allowFailure": t.boolean().optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "script": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "dir": t.string().optional(),
            "allowExitCodes": t.array(t.integer()).optional(),
        }
    ).named(renames["BuildStepIn"])
    types["BuildStepOut"] = t.struct(
        {
            "pullTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "secretEnv": t.array(t.string()).optional(),
            "timeout": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "exitCode": t.integer().optional(),
            "name": t.string(),
            "entrypoint": t.string().optional(),
            "allowFailure": t.boolean().optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "script": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "dir": t.string().optional(),
            "allowExitCodes": t.array(t.integer()).optional(),
            "timing": t.proxy(renames["TimeSpanOut"]).optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildStepOut"])
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
    types["ListBuildsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "builds": t.array(t.proxy(renames["BuildIn"])).optional(),
        }
    ).named(renames["ListBuildsResponseIn"])
    types["ListBuildsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "builds": t.array(t.proxy(renames["BuildOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBuildsResponseOut"])
    types["ListWorkerPoolsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "workerPools": t.array(t.proxy(renames["WorkerPoolIn"])).optional(),
        }
    ).named(renames["ListWorkerPoolsResponseIn"])
    types["ListWorkerPoolsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "workerPools": t.array(t.proxy(renames["WorkerPoolOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkerPoolsResponseOut"])

    functions = {}
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
    functions["locationsRegionalWebhook"] = cloudbuild.post(
        "v1/{location}/regionalWebhook",
        t.struct(
            {
                "location": t.string(),
                "webhookKey": t.string().optional(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsApprove"] = cloudbuild.post(
        "v1/projects/{projectId}/builds/{id}:cancel",
        t.struct(
            {
                "id": t.string(),
                "projectId": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsRetry"] = cloudbuild.post(
        "v1/projects/{projectId}/builds/{id}:cancel",
        t.struct(
            {
                "id": t.string(),
                "projectId": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsCreate"] = cloudbuild.post(
        "v1/projects/{projectId}/builds/{id}:cancel",
        t.struct(
            {
                "id": t.string(),
                "projectId": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsList"] = cloudbuild.post(
        "v1/projects/{projectId}/builds/{id}:cancel",
        t.struct(
            {
                "id": t.string(),
                "projectId": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsGet"] = cloudbuild.post(
        "v1/projects/{projectId}/builds/{id}:cancel",
        t.struct(
            {
                "id": t.string(),
                "projectId": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsCancel"] = cloudbuild.post(
        "v1/projects/{projectId}/builds/{id}:cancel",
        t.struct(
            {
                "id": t.string(),
                "projectId": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGithubEnterpriseConfigsList"] = cloudbuild.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "configId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GitHubEnterpriseConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGithubEnterpriseConfigsDelete"] = cloudbuild.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "configId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GitHubEnterpriseConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGithubEnterpriseConfigsCreate"] = cloudbuild.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "configId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GitHubEnterpriseConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGithubEnterpriseConfigsPatch"] = cloudbuild.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "configId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GitHubEnterpriseConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGithubEnterpriseConfigsGet"] = cloudbuild.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "configId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GitHubEnterpriseConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersRun"] = cloudbuild.delete(
        "v1/projects/{projectId}/triggers/{triggerId}",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "triggerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersGet"] = cloudbuild.delete(
        "v1/projects/{projectId}/triggers/{triggerId}",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "triggerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersList"] = cloudbuild.delete(
        "v1/projects/{projectId}/triggers/{triggerId}",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "triggerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersWebhook"] = cloudbuild.delete(
        "v1/projects/{projectId}/triggers/{triggerId}",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "triggerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersCreate"] = cloudbuild.delete(
        "v1/projects/{projectId}/triggers/{triggerId}",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "triggerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersPatch"] = cloudbuild.delete(
        "v1/projects/{projectId}/triggers/{triggerId}",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "triggerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersDelete"] = cloudbuild.delete(
        "v1/projects/{projectId}/triggers/{triggerId}",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "triggerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGithubEnterpriseConfigsGet"] = cloudbuild.delete(
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
    functions["projectsLocationsGithubEnterpriseConfigsCreate"] = cloudbuild.delete(
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
    functions["projectsLocationsGithubEnterpriseConfigsList"] = cloudbuild.delete(
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
    functions["projectsLocationsGithubEnterpriseConfigsPatch"] = cloudbuild.delete(
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
    functions["projectsLocationsGithubEnterpriseConfigsDelete"] = cloudbuild.delete(
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
    functions["projectsLocationsBitbucketServerConfigsList"] = cloudbuild.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBitbucketServerConfigsGet"] = cloudbuild.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBitbucketServerConfigsRemoveBitbucketServerConnectedRepository"
    ] = cloudbuild.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBitbucketServerConfigsPatch"] = cloudbuild.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBitbucketServerConfigsCreate"] = cloudbuild.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBitbucketServerConfigsDelete"] = cloudbuild.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBitbucketServerRepositoriesResponseOut"]),
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
    functions["projectsLocationsGitLabConfigsList"] = cloudbuild.post(
        "v1/{config}:removeGitLabConnectedRepository",
        t.struct(
            {
                "config": t.string(),
                "connectedRepository": t.proxy(
                    renames["GitLabRepositoryIdIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGitLabConfigsCreate"] = cloudbuild.post(
        "v1/{config}:removeGitLabConnectedRepository",
        t.struct(
            {
                "config": t.string(),
                "connectedRepository": t.proxy(
                    renames["GitLabRepositoryIdIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGitLabConfigsDelete"] = cloudbuild.post(
        "v1/{config}:removeGitLabConnectedRepository",
        t.struct(
            {
                "config": t.string(),
                "connectedRepository": t.proxy(
                    renames["GitLabRepositoryIdIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGitLabConfigsGet"] = cloudbuild.post(
        "v1/{config}:removeGitLabConnectedRepository",
        t.struct(
            {
                "config": t.string(),
                "connectedRepository": t.proxy(
                    renames["GitLabRepositoryIdIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGitLabConfigsPatch"] = cloudbuild.post(
        "v1/{config}:removeGitLabConnectedRepository",
        t.struct(
            {
                "config": t.string(),
                "connectedRepository": t.proxy(
                    renames["GitLabRepositoryIdIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGitLabConfigsRemoveGitLabConnectedRepository"
    ] = cloudbuild.post(
        "v1/{config}:removeGitLabConnectedRepository",
        t.struct(
            {
                "config": t.string(),
                "connectedRepository": t.proxy(
                    renames["GitLabRepositoryIdIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGitLabConfigsReposList"] = cloudbuild.get(
        "v1/{parent}/repos",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
    functions["projectsLocationsTriggersDelete"] = cloudbuild.post(
        "v1/{name}:webhook",
        t.struct(
            {
                "secret": t.string().optional(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "trigger": t.string().optional(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReceiveTriggerWebhookResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersGet"] = cloudbuild.post(
        "v1/{name}:webhook",
        t.struct(
            {
                "secret": t.string().optional(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "trigger": t.string().optional(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReceiveTriggerWebhookResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersRun"] = cloudbuild.post(
        "v1/{name}:webhook",
        t.struct(
            {
                "secret": t.string().optional(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "trigger": t.string().optional(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReceiveTriggerWebhookResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersList"] = cloudbuild.post(
        "v1/{name}:webhook",
        t.struct(
            {
                "secret": t.string().optional(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "trigger": t.string().optional(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReceiveTriggerWebhookResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersCreate"] = cloudbuild.post(
        "v1/{name}:webhook",
        t.struct(
            {
                "secret": t.string().optional(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "trigger": t.string().optional(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReceiveTriggerWebhookResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersPatch"] = cloudbuild.post(
        "v1/{name}:webhook",
        t.struct(
            {
                "secret": t.string().optional(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "trigger": t.string().optional(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReceiveTriggerWebhookResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersWebhook"] = cloudbuild.post(
        "v1/{name}:webhook",
        t.struct(
            {
                "secret": t.string().optional(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "trigger": t.string().optional(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReceiveTriggerWebhookResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkerPoolsList"] = cloudbuild.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "privatePoolV1Config": t.proxy(
                    renames["PrivatePoolV1ConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkerPoolsCreate"] = cloudbuild.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "privatePoolV1Config": t.proxy(
                    renames["PrivatePoolV1ConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkerPoolsDelete"] = cloudbuild.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "privatePoolV1Config": t.proxy(
                    renames["PrivatePoolV1ConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkerPoolsGet"] = cloudbuild.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "privatePoolV1Config": t.proxy(
                    renames["PrivatePoolV1ConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkerPoolsPatch"] = cloudbuild.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "privatePoolV1Config": t.proxy(
                    renames["PrivatePoolV1ConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsApprove"] = cloudbuild.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsRetry"] = cloudbuild.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsGet"] = cloudbuild.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsList"] = cloudbuild.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsCreate"] = cloudbuild.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsCancel"] = cloudbuild.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["githubDotComWebhookReceive"] = cloudbuild.post(
        "v1/githubDotComWebhook:receive",
        t.struct(
            {
                "webhookKey": t.string().optional(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1Webhook"] = cloudbuild.post(
        "v1/webhook",
        t.struct(
            {
                "webhookKey": t.string().optional(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudbuild", renames=renames, types=types, functions=functions
    )
