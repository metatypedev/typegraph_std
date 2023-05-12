from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_cloudbuild() -> Import:
    cloudbuild = HTTPRuntime("https://cloudbuild.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudbuild_1_ErrorResponse",
        "SecretManagerSecretIn": "_cloudbuild_2_SecretManagerSecretIn",
        "SecretManagerSecretOut": "_cloudbuild_3_SecretManagerSecretOut",
        "BuiltImageIn": "_cloudbuild_4_BuiltImageIn",
        "BuiltImageOut": "_cloudbuild_5_BuiltImageOut",
        "BatchCreateGitLabConnectedRepositoriesResponseIn": "_cloudbuild_6_BatchCreateGitLabConnectedRepositoriesResponseIn",
        "BatchCreateGitLabConnectedRepositoriesResponseOut": "_cloudbuild_7_BatchCreateGitLabConnectedRepositoriesResponseOut",
        "EmptyIn": "_cloudbuild_8_EmptyIn",
        "EmptyOut": "_cloudbuild_9_EmptyOut",
        "BuildApprovalIn": "_cloudbuild_10_BuildApprovalIn",
        "BuildApprovalOut": "_cloudbuild_11_BuildApprovalOut",
        "BitbucketServerRepositoryIn": "_cloudbuild_12_BitbucketServerRepositoryIn",
        "BitbucketServerRepositoryOut": "_cloudbuild_13_BitbucketServerRepositoryOut",
        "StorageSourceIn": "_cloudbuild_14_StorageSourceIn",
        "StorageSourceOut": "_cloudbuild_15_StorageSourceOut",
        "CreateGitLabConnectedRepositoryRequestIn": "_cloudbuild_16_CreateGitLabConnectedRepositoryRequestIn",
        "CreateGitLabConnectedRepositoryRequestOut": "_cloudbuild_17_CreateGitLabConnectedRepositoryRequestOut",
        "CreateGitHubEnterpriseConfigOperationMetadataIn": "_cloudbuild_18_CreateGitHubEnterpriseConfigOperationMetadataIn",
        "CreateGitHubEnterpriseConfigOperationMetadataOut": "_cloudbuild_19_CreateGitHubEnterpriseConfigOperationMetadataOut",
        "BatchCreateGitLabConnectedRepositoriesRequestIn": "_cloudbuild_20_BatchCreateGitLabConnectedRepositoriesRequestIn",
        "BatchCreateGitLabConnectedRepositoriesRequestOut": "_cloudbuild_21_BatchCreateGitLabConnectedRepositoriesRequestOut",
        "ListGitLabRepositoriesResponseIn": "_cloudbuild_22_ListGitLabRepositoriesResponseIn",
        "ListGitLabRepositoriesResponseOut": "_cloudbuild_23_ListGitLabRepositoriesResponseOut",
        "BatchCreateBitbucketServerConnectedRepositoriesRequestIn": "_cloudbuild_24_BatchCreateBitbucketServerConnectedRepositoriesRequestIn",
        "BatchCreateBitbucketServerConnectedRepositoriesRequestOut": "_cloudbuild_25_BatchCreateBitbucketServerConnectedRepositoriesRequestOut",
        "GitRepoSourceIn": "_cloudbuild_26_GitRepoSourceIn",
        "GitRepoSourceOut": "_cloudbuild_27_GitRepoSourceOut",
        "ResultsIn": "_cloudbuild_28_ResultsIn",
        "ResultsOut": "_cloudbuild_29_ResultsOut",
        "DeleteGitLabConfigOperationMetadataIn": "_cloudbuild_30_DeleteGitLabConfigOperationMetadataIn",
        "DeleteGitLabConfigOperationMetadataOut": "_cloudbuild_31_DeleteGitLabConfigOperationMetadataOut",
        "GitLabEventsConfigIn": "_cloudbuild_32_GitLabEventsConfigIn",
        "GitLabEventsConfigOut": "_cloudbuild_33_GitLabEventsConfigOut",
        "CreateGitLabConfigOperationMetadataIn": "_cloudbuild_34_CreateGitLabConfigOperationMetadataIn",
        "CreateGitLabConfigOperationMetadataOut": "_cloudbuild_35_CreateGitLabConfigOperationMetadataOut",
        "UpdateBitbucketServerConfigOperationMetadataIn": "_cloudbuild_36_UpdateBitbucketServerConfigOperationMetadataIn",
        "UpdateBitbucketServerConfigOperationMetadataOut": "_cloudbuild_37_UpdateBitbucketServerConfigOperationMetadataOut",
        "CancelOperationRequestIn": "_cloudbuild_38_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_cloudbuild_39_CancelOperationRequestOut",
        "SourceIn": "_cloudbuild_40_SourceIn",
        "SourceOut": "_cloudbuild_41_SourceOut",
        "ListBitbucketServerConfigsResponseIn": "_cloudbuild_42_ListBitbucketServerConfigsResponseIn",
        "ListBitbucketServerConfigsResponseOut": "_cloudbuild_43_ListBitbucketServerConfigsResponseOut",
        "RunBuildTriggerRequestIn": "_cloudbuild_44_RunBuildTriggerRequestIn",
        "RunBuildTriggerRequestOut": "_cloudbuild_45_RunBuildTriggerRequestOut",
        "ServiceDirectoryConfigIn": "_cloudbuild_46_ServiceDirectoryConfigIn",
        "ServiceDirectoryConfigOut": "_cloudbuild_47_ServiceDirectoryConfigOut",
        "BuildTriggerIn": "_cloudbuild_48_BuildTriggerIn",
        "BuildTriggerOut": "_cloudbuild_49_BuildTriggerOut",
        "InlineSecretIn": "_cloudbuild_50_InlineSecretIn",
        "InlineSecretOut": "_cloudbuild_51_InlineSecretOut",
        "GitLabRepositoryIn": "_cloudbuild_52_GitLabRepositoryIn",
        "GitLabRepositoryOut": "_cloudbuild_53_GitLabRepositoryOut",
        "PubsubConfigIn": "_cloudbuild_54_PubsubConfigIn",
        "PubsubConfigOut": "_cloudbuild_55_PubsubConfigOut",
        "PrivatePoolV1ConfigIn": "_cloudbuild_56_PrivatePoolV1ConfigIn",
        "PrivatePoolV1ConfigOut": "_cloudbuild_57_PrivatePoolV1ConfigOut",
        "TimeSpanIn": "_cloudbuild_58_TimeSpanIn",
        "TimeSpanOut": "_cloudbuild_59_TimeSpanOut",
        "HttpBodyIn": "_cloudbuild_60_HttpBodyIn",
        "HttpBodyOut": "_cloudbuild_61_HttpBodyOut",
        "RemoveGitLabConnectedRepositoryRequestIn": "_cloudbuild_62_RemoveGitLabConnectedRepositoryRequestIn",
        "RemoveGitLabConnectedRepositoryRequestOut": "_cloudbuild_63_RemoveGitLabConnectedRepositoryRequestOut",
        "RemoveBitbucketServerConnectedRepositoryRequestIn": "_cloudbuild_64_RemoveBitbucketServerConnectedRepositoryRequestIn",
        "RemoveBitbucketServerConnectedRepositoryRequestOut": "_cloudbuild_65_RemoveBitbucketServerConnectedRepositoryRequestOut",
        "BuildOperationMetadataIn": "_cloudbuild_66_BuildOperationMetadataIn",
        "BuildOperationMetadataOut": "_cloudbuild_67_BuildOperationMetadataOut",
        "UploadedMavenArtifactIn": "_cloudbuild_68_UploadedMavenArtifactIn",
        "UploadedMavenArtifactOut": "_cloudbuild_69_UploadedMavenArtifactOut",
        "RepositoryEventConfigIn": "_cloudbuild_70_RepositoryEventConfigIn",
        "RepositoryEventConfigOut": "_cloudbuild_71_RepositoryEventConfigOut",
        "SecretsIn": "_cloudbuild_72_SecretsIn",
        "SecretsOut": "_cloudbuild_73_SecretsOut",
        "ListWorkerPoolsResponseIn": "_cloudbuild_74_ListWorkerPoolsResponseIn",
        "ListWorkerPoolsResponseOut": "_cloudbuild_75_ListWorkerPoolsResponseOut",
        "BuildStepIn": "_cloudbuild_76_BuildStepIn",
        "BuildStepOut": "_cloudbuild_77_BuildStepOut",
        "WarningIn": "_cloudbuild_78_WarningIn",
        "WarningOut": "_cloudbuild_79_WarningOut",
        "GitHubEnterpriseConfigIn": "_cloudbuild_80_GitHubEnterpriseConfigIn",
        "GitHubEnterpriseConfigOut": "_cloudbuild_81_GitHubEnterpriseConfigOut",
        "BitbucketServerConnectedRepositoryIn": "_cloudbuild_82_BitbucketServerConnectedRepositoryIn",
        "BitbucketServerConnectedRepositoryOut": "_cloudbuild_83_BitbucketServerConnectedRepositoryOut",
        "PoolOptionIn": "_cloudbuild_84_PoolOptionIn",
        "PoolOptionOut": "_cloudbuild_85_PoolOptionOut",
        "NetworkConfigIn": "_cloudbuild_86_NetworkConfigIn",
        "NetworkConfigOut": "_cloudbuild_87_NetworkConfigOut",
        "GitHubEnterpriseSecretsIn": "_cloudbuild_88_GitHubEnterpriseSecretsIn",
        "GitHubEnterpriseSecretsOut": "_cloudbuild_89_GitHubEnterpriseSecretsOut",
        "BitbucketServerRepositoryIdIn": "_cloudbuild_90_BitbucketServerRepositoryIdIn",
        "BitbucketServerRepositoryIdOut": "_cloudbuild_91_BitbucketServerRepositoryIdOut",
        "ListGitLabConfigsResponseIn": "_cloudbuild_92_ListGitLabConfigsResponseIn",
        "ListGitLabConfigsResponseOut": "_cloudbuild_93_ListGitLabConfigsResponseOut",
        "GitSourceIn": "_cloudbuild_94_GitSourceIn",
        "GitSourceOut": "_cloudbuild_95_GitSourceOut",
        "PushFilterIn": "_cloudbuild_96_PushFilterIn",
        "PushFilterOut": "_cloudbuild_97_PushFilterOut",
        "ApproveBuildRequestIn": "_cloudbuild_98_ApproveBuildRequestIn",
        "ApproveBuildRequestOut": "_cloudbuild_99_ApproveBuildRequestOut",
        "ArtifactResultIn": "_cloudbuild_100_ArtifactResultIn",
        "ArtifactResultOut": "_cloudbuild_101_ArtifactResultOut",
        "GitLabConfigIn": "_cloudbuild_102_GitLabConfigIn",
        "GitLabConfigOut": "_cloudbuild_103_GitLabConfigOut",
        "VolumeIn": "_cloudbuild_104_VolumeIn",
        "VolumeOut": "_cloudbuild_105_VolumeOut",
        "BatchCreateBitbucketServerConnectedRepositoriesResponseIn": "_cloudbuild_106_BatchCreateBitbucketServerConnectedRepositoriesResponseIn",
        "BatchCreateBitbucketServerConnectedRepositoriesResponseOut": "_cloudbuild_107_BatchCreateBitbucketServerConnectedRepositoriesResponseOut",
        "ListBuildsResponseIn": "_cloudbuild_108_ListBuildsResponseIn",
        "ListBuildsResponseOut": "_cloudbuild_109_ListBuildsResponseOut",
        "UpdateGitHubEnterpriseConfigOperationMetadataIn": "_cloudbuild_110_UpdateGitHubEnterpriseConfigOperationMetadataIn",
        "UpdateGitHubEnterpriseConfigOperationMetadataOut": "_cloudbuild_111_UpdateGitHubEnterpriseConfigOperationMetadataOut",
        "SecretIn": "_cloudbuild_112_SecretIn",
        "SecretOut": "_cloudbuild_113_SecretOut",
        "OperationMetadataIn": "_cloudbuild_114_OperationMetadataIn",
        "OperationMetadataOut": "_cloudbuild_115_OperationMetadataOut",
        "BitbucketServerTriggerConfigIn": "_cloudbuild_116_BitbucketServerTriggerConfigIn",
        "BitbucketServerTriggerConfigOut": "_cloudbuild_117_BitbucketServerTriggerConfigOut",
        "DeleteWorkerPoolOperationMetadataIn": "_cloudbuild_118_DeleteWorkerPoolOperationMetadataIn",
        "DeleteWorkerPoolOperationMetadataOut": "_cloudbuild_119_DeleteWorkerPoolOperationMetadataOut",
        "CreateBitbucketServerConfigOperationMetadataIn": "_cloudbuild_120_CreateBitbucketServerConfigOperationMetadataIn",
        "CreateBitbucketServerConfigOperationMetadataOut": "_cloudbuild_121_CreateBitbucketServerConfigOperationMetadataOut",
        "RepoSourceIn": "_cloudbuild_122_RepoSourceIn",
        "RepoSourceOut": "_cloudbuild_123_RepoSourceOut",
        "CreateBitbucketServerConnectedRepositoryRequestIn": "_cloudbuild_124_CreateBitbucketServerConnectedRepositoryRequestIn",
        "CreateBitbucketServerConnectedRepositoryRequestOut": "_cloudbuild_125_CreateBitbucketServerConnectedRepositoryRequestOut",
        "GitHubEventsConfigIn": "_cloudbuild_126_GitHubEventsConfigIn",
        "GitHubEventsConfigOut": "_cloudbuild_127_GitHubEventsConfigOut",
        "ReceiveTriggerWebhookResponseIn": "_cloudbuild_128_ReceiveTriggerWebhookResponseIn",
        "ReceiveTriggerWebhookResponseOut": "_cloudbuild_129_ReceiveTriggerWebhookResponseOut",
        "StatusIn": "_cloudbuild_130_StatusIn",
        "StatusOut": "_cloudbuild_131_StatusOut",
        "DeleteBitbucketServerConfigOperationMetadataIn": "_cloudbuild_132_DeleteBitbucketServerConfigOperationMetadataIn",
        "DeleteBitbucketServerConfigOperationMetadataOut": "_cloudbuild_133_DeleteBitbucketServerConfigOperationMetadataOut",
        "NpmPackageIn": "_cloudbuild_134_NpmPackageIn",
        "NpmPackageOut": "_cloudbuild_135_NpmPackageOut",
        "ProcessAppManifestCallbackOperationMetadataIn": "_cloudbuild_136_ProcessAppManifestCallbackOperationMetadataIn",
        "ProcessAppManifestCallbackOperationMetadataOut": "_cloudbuild_137_ProcessAppManifestCallbackOperationMetadataOut",
        "BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataIn": "_cloudbuild_138_BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataIn",
        "BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataOut": "_cloudbuild_139_BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataOut",
        "ApprovalResultIn": "_cloudbuild_140_ApprovalResultIn",
        "ApprovalResultOut": "_cloudbuild_141_ApprovalResultOut",
        "UploadedNpmPackageIn": "_cloudbuild_142_UploadedNpmPackageIn",
        "UploadedNpmPackageOut": "_cloudbuild_143_UploadedNpmPackageOut",
        "UpdateWorkerPoolOperationMetadataIn": "_cloudbuild_144_UpdateWorkerPoolOperationMetadataIn",
        "UpdateWorkerPoolOperationMetadataOut": "_cloudbuild_145_UpdateWorkerPoolOperationMetadataOut",
        "ListBuildTriggersResponseIn": "_cloudbuild_146_ListBuildTriggersResponseIn",
        "ListBuildTriggersResponseOut": "_cloudbuild_147_ListBuildTriggersResponseOut",
        "UploadedPythonPackageIn": "_cloudbuild_148_UploadedPythonPackageIn",
        "UploadedPythonPackageOut": "_cloudbuild_149_UploadedPythonPackageOut",
        "CreateWorkerPoolOperationMetadataIn": "_cloudbuild_150_CreateWorkerPoolOperationMetadataIn",
        "CreateWorkerPoolOperationMetadataOut": "_cloudbuild_151_CreateWorkerPoolOperationMetadataOut",
        "GitFileSourceIn": "_cloudbuild_152_GitFileSourceIn",
        "GitFileSourceOut": "_cloudbuild_153_GitFileSourceOut",
        "GitLabRepositoryIdIn": "_cloudbuild_154_GitLabRepositoryIdIn",
        "GitLabRepositoryIdOut": "_cloudbuild_155_GitLabRepositoryIdOut",
        "BitbucketServerSecretsIn": "_cloudbuild_156_BitbucketServerSecretsIn",
        "BitbucketServerSecretsOut": "_cloudbuild_157_BitbucketServerSecretsOut",
        "WorkerPoolIn": "_cloudbuild_158_WorkerPoolIn",
        "WorkerPoolOut": "_cloudbuild_159_WorkerPoolOut",
        "SourceProvenanceIn": "_cloudbuild_160_SourceProvenanceIn",
        "SourceProvenanceOut": "_cloudbuild_161_SourceProvenanceOut",
        "UpdateGitLabConfigOperationMetadataIn": "_cloudbuild_162_UpdateGitLabConfigOperationMetadataIn",
        "UpdateGitLabConfigOperationMetadataOut": "_cloudbuild_163_UpdateGitLabConfigOperationMetadataOut",
        "CancelBuildRequestIn": "_cloudbuild_164_CancelBuildRequestIn",
        "CancelBuildRequestOut": "_cloudbuild_165_CancelBuildRequestOut",
        "ListGithubEnterpriseConfigsResponseIn": "_cloudbuild_166_ListGithubEnterpriseConfigsResponseIn",
        "ListGithubEnterpriseConfigsResponseOut": "_cloudbuild_167_ListGithubEnterpriseConfigsResponseOut",
        "BatchCreateGitLabConnectedRepositoriesResponseMetadataIn": "_cloudbuild_168_BatchCreateGitLabConnectedRepositoriesResponseMetadataIn",
        "BatchCreateGitLabConnectedRepositoriesResponseMetadataOut": "_cloudbuild_169_BatchCreateGitLabConnectedRepositoriesResponseMetadataOut",
        "DeleteGitHubEnterpriseConfigOperationMetadataIn": "_cloudbuild_170_DeleteGitHubEnterpriseConfigOperationMetadataIn",
        "DeleteGitHubEnterpriseConfigOperationMetadataOut": "_cloudbuild_171_DeleteGitHubEnterpriseConfigOperationMetadataOut",
        "OperationIn": "_cloudbuild_172_OperationIn",
        "OperationOut": "_cloudbuild_173_OperationOut",
        "WebhookConfigIn": "_cloudbuild_174_WebhookConfigIn",
        "WebhookConfigOut": "_cloudbuild_175_WebhookConfigOut",
        "WorkerConfigIn": "_cloudbuild_176_WorkerConfigIn",
        "WorkerConfigOut": "_cloudbuild_177_WorkerConfigOut",
        "PullRequestFilterIn": "_cloudbuild_178_PullRequestFilterIn",
        "PullRequestFilterOut": "_cloudbuild_179_PullRequestFilterOut",
        "ArtifactsIn": "_cloudbuild_180_ArtifactsIn",
        "ArtifactsOut": "_cloudbuild_181_ArtifactsOut",
        "ListBitbucketServerRepositoriesResponseIn": "_cloudbuild_182_ListBitbucketServerRepositoriesResponseIn",
        "ListBitbucketServerRepositoriesResponseOut": "_cloudbuild_183_ListBitbucketServerRepositoriesResponseOut",
        "ArtifactObjectsIn": "_cloudbuild_184_ArtifactObjectsIn",
        "ArtifactObjectsOut": "_cloudbuild_185_ArtifactObjectsOut",
        "FileHashesIn": "_cloudbuild_186_FileHashesIn",
        "FileHashesOut": "_cloudbuild_187_FileHashesOut",
        "HashIn": "_cloudbuild_188_HashIn",
        "HashOut": "_cloudbuild_189_HashOut",
        "PythonPackageIn": "_cloudbuild_190_PythonPackageIn",
        "PythonPackageOut": "_cloudbuild_191_PythonPackageOut",
        "StorageSourceManifestIn": "_cloudbuild_192_StorageSourceManifestIn",
        "StorageSourceManifestOut": "_cloudbuild_193_StorageSourceManifestOut",
        "GitLabSecretsIn": "_cloudbuild_194_GitLabSecretsIn",
        "GitLabSecretsOut": "_cloudbuild_195_GitLabSecretsOut",
        "GitLabConnectedRepositoryIn": "_cloudbuild_196_GitLabConnectedRepositoryIn",
        "GitLabConnectedRepositoryOut": "_cloudbuild_197_GitLabConnectedRepositoryOut",
        "GitLabEnterpriseConfigIn": "_cloudbuild_198_GitLabEnterpriseConfigIn",
        "GitLabEnterpriseConfigOut": "_cloudbuild_199_GitLabEnterpriseConfigOut",
        "BuildOptionsIn": "_cloudbuild_200_BuildOptionsIn",
        "BuildOptionsOut": "_cloudbuild_201_BuildOptionsOut",
        "RetryBuildRequestIn": "_cloudbuild_202_RetryBuildRequestIn",
        "RetryBuildRequestOut": "_cloudbuild_203_RetryBuildRequestOut",
        "ApprovalConfigIn": "_cloudbuild_204_ApprovalConfigIn",
        "ApprovalConfigOut": "_cloudbuild_205_ApprovalConfigOut",
        "FailureInfoIn": "_cloudbuild_206_FailureInfoIn",
        "FailureInfoOut": "_cloudbuild_207_FailureInfoOut",
        "BitbucketServerConfigIn": "_cloudbuild_208_BitbucketServerConfigIn",
        "BitbucketServerConfigOut": "_cloudbuild_209_BitbucketServerConfigOut",
        "BuildIn": "_cloudbuild_210_BuildIn",
        "BuildOut": "_cloudbuild_211_BuildOut",
        "MavenArtifactIn": "_cloudbuild_212_MavenArtifactIn",
        "MavenArtifactOut": "_cloudbuild_213_MavenArtifactOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["BuiltImageIn"] = t.struct(
        {"digest": t.string().optional(), "name": t.string().optional()}
    ).named(renames["BuiltImageIn"])
    types["BuiltImageOut"] = t.struct(
        {
            "pushTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "digest": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuiltImageOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["BitbucketServerRepositoryIn"] = t.struct(
        {
            "browseUri": t.string().optional(),
            "description": t.string().optional(),
            "repoId": t.proxy(renames["BitbucketServerRepositoryIdIn"]).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["BitbucketServerRepositoryIn"])
    types["BitbucketServerRepositoryOut"] = t.struct(
        {
            "browseUri": t.string().optional(),
            "description": t.string().optional(),
            "repoId": t.proxy(renames["BitbucketServerRepositoryIdOut"]).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerRepositoryOut"])
    types["StorageSourceIn"] = t.struct(
        {
            "bucket": t.string().optional(),
            "generation": t.string().optional(),
            "object": t.string().optional(),
        }
    ).named(renames["StorageSourceIn"])
    types["StorageSourceOut"] = t.struct(
        {
            "bucket": t.string().optional(),
            "generation": t.string().optional(),
            "object": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StorageSourceOut"])
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
    types["CreateGitHubEnterpriseConfigOperationMetadataIn"] = t.struct(
        {
            "githubEnterpriseConfig": t.string().optional(),
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["CreateGitHubEnterpriseConfigOperationMetadataIn"])
    types["CreateGitHubEnterpriseConfigOperationMetadataOut"] = t.struct(
        {
            "githubEnterpriseConfig": t.string().optional(),
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateGitHubEnterpriseConfigOperationMetadataOut"])
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
    types["ListGitLabRepositoriesResponseIn"] = t.struct(
        {
            "gitlabRepositories": t.array(
                t.proxy(renames["GitLabRepositoryIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListGitLabRepositoriesResponseIn"])
    types["ListGitLabRepositoriesResponseOut"] = t.struct(
        {
            "gitlabRepositories": t.array(
                t.proxy(renames["GitLabRepositoryOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
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
    types["GitRepoSourceIn"] = t.struct(
        {
            "repoType": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "repository": t.string().optional(),
            "uri": t.string().optional(),
            "ref": t.string().optional(),
        }
    ).named(renames["GitRepoSourceIn"])
    types["GitRepoSourceOut"] = t.struct(
        {
            "repoType": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "repository": t.string().optional(),
            "uri": t.string().optional(),
            "ref": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitRepoSourceOut"])
    types["ResultsIn"] = t.struct(
        {
            "buildStepOutputs": t.array(t.string()).optional(),
            "numArtifacts": t.string().optional(),
            "artifactManifest": t.string().optional(),
            "mavenArtifacts": t.array(
                t.proxy(renames["UploadedMavenArtifactIn"])
            ).optional(),
            "buildStepImages": t.array(t.string()).optional(),
            "npmPackages": t.array(t.proxy(renames["UploadedNpmPackageIn"])).optional(),
            "artifactTiming": t.proxy(renames["TimeSpanIn"]).optional(),
            "pythonPackages": t.array(
                t.proxy(renames["UploadedPythonPackageIn"])
            ).optional(),
            "images": t.array(t.proxy(renames["BuiltImageIn"])).optional(),
        }
    ).named(renames["ResultsIn"])
    types["ResultsOut"] = t.struct(
        {
            "buildStepOutputs": t.array(t.string()).optional(),
            "numArtifacts": t.string().optional(),
            "artifactManifest": t.string().optional(),
            "mavenArtifacts": t.array(
                t.proxy(renames["UploadedMavenArtifactOut"])
            ).optional(),
            "buildStepImages": t.array(t.string()).optional(),
            "npmPackages": t.array(
                t.proxy(renames["UploadedNpmPackageOut"])
            ).optional(),
            "artifactTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "pythonPackages": t.array(
                t.proxy(renames["UploadedPythonPackageOut"])
            ).optional(),
            "images": t.array(t.proxy(renames["BuiltImageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultsOut"])
    types["DeleteGitLabConfigOperationMetadataIn"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "gitlabConfig": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["DeleteGitLabConfigOperationMetadataIn"])
    types["DeleteGitLabConfigOperationMetadataOut"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "gitlabConfig": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteGitLabConfigOperationMetadataOut"])
    types["GitLabEventsConfigIn"] = t.struct(
        {
            "pullRequest": t.proxy(renames["PullRequestFilterIn"]).optional(),
            "gitlabConfigResource": t.string().optional(),
            "push": t.proxy(renames["PushFilterIn"]).optional(),
            "projectNamespace": t.string().optional(),
        }
    ).named(renames["GitLabEventsConfigIn"])
    types["GitLabEventsConfigOut"] = t.struct(
        {
            "pullRequest": t.proxy(renames["PullRequestFilterOut"]).optional(),
            "gitlabConfigResource": t.string().optional(),
            "push": t.proxy(renames["PushFilterOut"]).optional(),
            "projectNamespace": t.string().optional(),
            "gitlabConfig": t.proxy(renames["GitLabConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabEventsConfigOut"])
    types["CreateGitLabConfigOperationMetadataIn"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "gitlabConfig": t.string().optional(),
        }
    ).named(renames["CreateGitLabConfigOperationMetadataIn"])
    types["CreateGitLabConfigOperationMetadataOut"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "gitlabConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateGitLabConfigOperationMetadataOut"])
    types["UpdateBitbucketServerConfigOperationMetadataIn"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["UpdateBitbucketServerConfigOperationMetadataIn"])
    types["UpdateBitbucketServerConfigOperationMetadataOut"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBitbucketServerConfigOperationMetadataOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["RunBuildTriggerRequestIn"] = t.struct(
        {
            "source": t.proxy(renames["RepoSourceIn"]).optional(),
            "projectId": t.string(),
            "triggerId": t.string(),
        }
    ).named(renames["RunBuildTriggerRequestIn"])
    types["RunBuildTriggerRequestOut"] = t.struct(
        {
            "source": t.proxy(renames["RepoSourceOut"]).optional(),
            "projectId": t.string(),
            "triggerId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunBuildTriggerRequestOut"])
    types["ServiceDirectoryConfigIn"] = t.struct(
        {"service": t.string().optional()}
    ).named(renames["ServiceDirectoryConfigIn"])
    types["ServiceDirectoryConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceDirectoryConfigOut"])
    types["BuildTriggerIn"] = t.struct(
        {
            "build": t.proxy(renames["BuildIn"]).optional(),
            "disabled": t.boolean().optional(),
            "github": t.proxy(renames["GitHubEventsConfigIn"]).optional(),
            "eventType": t.string().optional(),
            "ignoredFiles": t.array(t.string()).optional(),
            "autodetect": t.boolean().optional(),
            "filter": t.string().optional(),
            "description": t.string().optional(),
            "bitbucketServerTriggerConfig": t.proxy(
                renames["BitbucketServerTriggerConfigIn"]
            ).optional(),
            "serviceAccount": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "pubsubConfig": t.proxy(renames["PubsubConfigIn"]).optional(),
            "resourceName": t.string().optional(),
            "sourceToBuild": t.proxy(renames["GitRepoSourceIn"]).optional(),
            "triggerTemplate": t.proxy(renames["RepoSourceIn"]).optional(),
            "includedFiles": t.array(t.string()).optional(),
            "repositoryEventConfig": t.proxy(
                renames["RepositoryEventConfigIn"]
            ).optional(),
            "gitlabEnterpriseEventsConfig": t.proxy(
                renames["GitLabEventsConfigIn"]
            ).optional(),
            "webhookConfig": t.proxy(renames["WebhookConfigIn"]).optional(),
            "filename": t.string().optional(),
            "gitFileSource": t.proxy(renames["GitFileSourceIn"]).optional(),
            "includeBuildLogs": t.string().optional(),
            "approvalConfig": t.proxy(renames["ApprovalConfigIn"]).optional(),
        }
    ).named(renames["BuildTriggerIn"])
    types["BuildTriggerOut"] = t.struct(
        {
            "id": t.string().optional(),
            "build": t.proxy(renames["BuildOut"]).optional(),
            "disabled": t.boolean().optional(),
            "github": t.proxy(renames["GitHubEventsConfigOut"]).optional(),
            "eventType": t.string().optional(),
            "ignoredFiles": t.array(t.string()).optional(),
            "autodetect": t.boolean().optional(),
            "filter": t.string().optional(),
            "description": t.string().optional(),
            "bitbucketServerTriggerConfig": t.proxy(
                renames["BitbucketServerTriggerConfigOut"]
            ).optional(),
            "serviceAccount": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "pubsubConfig": t.proxy(renames["PubsubConfigOut"]).optional(),
            "createTime": t.string().optional(),
            "resourceName": t.string().optional(),
            "sourceToBuild": t.proxy(renames["GitRepoSourceOut"]).optional(),
            "triggerTemplate": t.proxy(renames["RepoSourceOut"]).optional(),
            "includedFiles": t.array(t.string()).optional(),
            "repositoryEventConfig": t.proxy(
                renames["RepositoryEventConfigOut"]
            ).optional(),
            "gitlabEnterpriseEventsConfig": t.proxy(
                renames["GitLabEventsConfigOut"]
            ).optional(),
            "webhookConfig": t.proxy(renames["WebhookConfigOut"]).optional(),
            "filename": t.string().optional(),
            "gitFileSource": t.proxy(renames["GitFileSourceOut"]).optional(),
            "includeBuildLogs": t.string().optional(),
            "approvalConfig": t.proxy(renames["ApprovalConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildTriggerOut"])
    types["InlineSecretIn"] = t.struct(
        {
            "envMap": t.struct({"_": t.string().optional()}).optional(),
            "kmsKeyName": t.string().optional(),
        }
    ).named(renames["InlineSecretIn"])
    types["InlineSecretOut"] = t.struct(
        {
            "envMap": t.struct({"_": t.string().optional()}).optional(),
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlineSecretOut"])
    types["GitLabRepositoryIn"] = t.struct(
        {
            "name": t.string().optional(),
            "browseUri": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "repositoryId": t.proxy(renames["GitLabRepositoryIdIn"]).optional(),
        }
    ).named(renames["GitLabRepositoryIn"])
    types["GitLabRepositoryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "browseUri": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "repositoryId": t.proxy(renames["GitLabRepositoryIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabRepositoryOut"])
    types["PubsubConfigIn"] = t.struct(
        {
            "topic": t.string().optional(),
            "state": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
        }
    ).named(renames["PubsubConfigIn"])
    types["PubsubConfigOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "state": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "subscription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubConfigOut"])
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
    types["HttpBodyIn"] = t.struct(
        {
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "data": t.string().optional(),
            "contentType": t.string().optional(),
        }
    ).named(renames["HttpBodyIn"])
    types["HttpBodyOut"] = t.struct(
        {
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "data": t.string().optional(),
            "contentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpBodyOut"])
    types["RemoveGitLabConnectedRepositoryRequestIn"] = t.struct(
        {"connectedRepository": t.proxy(renames["GitLabRepositoryIdIn"]).optional()}
    ).named(renames["RemoveGitLabConnectedRepositoryRequestIn"])
    types["RemoveGitLabConnectedRepositoryRequestOut"] = t.struct(
        {
            "connectedRepository": t.proxy(renames["GitLabRepositoryIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveGitLabConnectedRepositoryRequestOut"])
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
    types["BuildOperationMetadataIn"] = t.struct(
        {"build": t.proxy(renames["BuildIn"]).optional()}
    ).named(renames["BuildOperationMetadataIn"])
    types["BuildOperationMetadataOut"] = t.struct(
        {
            "build": t.proxy(renames["BuildOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOperationMetadataOut"])
    types["UploadedMavenArtifactIn"] = t.struct(
        {
            "fileHashes": t.proxy(renames["FileHashesIn"]).optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["UploadedMavenArtifactIn"])
    types["UploadedMavenArtifactOut"] = t.struct(
        {
            "pushTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "fileHashes": t.proxy(renames["FileHashesOut"]).optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadedMavenArtifactOut"])
    types["RepositoryEventConfigIn"] = t.struct(
        {
            "pullRequest": t.proxy(renames["PullRequestFilterIn"]).optional(),
            "repository": t.string().optional(),
            "push": t.proxy(renames["PushFilterIn"]).optional(),
        }
    ).named(renames["RepositoryEventConfigIn"])
    types["RepositoryEventConfigOut"] = t.struct(
        {
            "pullRequest": t.proxy(renames["PullRequestFilterOut"]).optional(),
            "repository": t.string().optional(),
            "repositoryType": t.string().optional(),
            "push": t.proxy(renames["PushFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepositoryEventConfigOut"])
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
    types["BuildStepIn"] = t.struct(
        {
            "allowExitCodes": t.array(t.integer()).optional(),
            "script": t.string().optional(),
            "entrypoint": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "name": t.string(),
            "allowFailure": t.boolean().optional(),
            "env": t.array(t.string()).optional(),
            "timeout": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "secretEnv": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "dir": t.string().optional(),
        }
    ).named(renames["BuildStepIn"])
    types["BuildStepOut"] = t.struct(
        {
            "pullTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "allowExitCodes": t.array(t.integer()).optional(),
            "exitCode": t.integer().optional(),
            "script": t.string().optional(),
            "entrypoint": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "timing": t.proxy(renames["TimeSpanOut"]).optional(),
            "name": t.string(),
            "allowFailure": t.boolean().optional(),
            "env": t.array(t.string()).optional(),
            "timeout": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "secretEnv": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "dir": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildStepOut"])
    types["WarningIn"] = t.struct(
        {"priority": t.string().optional(), "text": t.string().optional()}
    ).named(renames["WarningIn"])
    types["WarningOut"] = t.struct(
        {
            "priority": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WarningOut"])
    types["GitHubEnterpriseConfigIn"] = t.struct(
        {
            "peeredNetwork": t.string().optional(),
            "name": t.string().optional(),
            "webhookKey": t.string().optional(),
            "hostUrl": t.string().optional(),
            "sslCa": t.string().optional(),
            "displayName": t.string().optional(),
            "appId": t.string(),
            "secrets": t.proxy(renames["GitHubEnterpriseSecretsIn"]).optional(),
        }
    ).named(renames["GitHubEnterpriseConfigIn"])
    types["GitHubEnterpriseConfigOut"] = t.struct(
        {
            "peeredNetwork": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "webhookKey": t.string().optional(),
            "hostUrl": t.string().optional(),
            "sslCa": t.string().optional(),
            "displayName": t.string().optional(),
            "appId": t.string(),
            "secrets": t.proxy(renames["GitHubEnterpriseSecretsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitHubEnterpriseConfigOut"])
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
    types["PoolOptionIn"] = t.struct({"name": t.string().optional()}).named(
        renames["PoolOptionIn"]
    )
    types["PoolOptionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoolOptionOut"])
    types["NetworkConfigIn"] = t.struct(
        {
            "peeredNetworkIpRange": t.string().optional(),
            "egressOption": t.string().optional(),
            "peeredNetwork": t.string(),
        }
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "peeredNetworkIpRange": t.string().optional(),
            "egressOption": t.string().optional(),
            "peeredNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["GitHubEnterpriseSecretsIn"] = t.struct(
        {
            "oauthClientIdName": t.string().optional(),
            "oauthClientIdVersionName": t.string().optional(),
            "oauthSecretName": t.string().optional(),
            "webhookSecretName": t.string().optional(),
            "oauthSecretVersionName": t.string().optional(),
            "privateKeyVersionName": t.string().optional(),
            "privateKeyName": t.string().optional(),
            "webhookSecretVersionName": t.string().optional(),
        }
    ).named(renames["GitHubEnterpriseSecretsIn"])
    types["GitHubEnterpriseSecretsOut"] = t.struct(
        {
            "oauthClientIdName": t.string().optional(),
            "oauthClientIdVersionName": t.string().optional(),
            "oauthSecretName": t.string().optional(),
            "webhookSecretName": t.string().optional(),
            "oauthSecretVersionName": t.string().optional(),
            "privateKeyVersionName": t.string().optional(),
            "privateKeyName": t.string().optional(),
            "webhookSecretVersionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitHubEnterpriseSecretsOut"])
    types["BitbucketServerRepositoryIdIn"] = t.struct(
        {"repoSlug": t.string(), "projectKey": t.string()}
    ).named(renames["BitbucketServerRepositoryIdIn"])
    types["BitbucketServerRepositoryIdOut"] = t.struct(
        {
            "webhookId": t.integer().optional(),
            "repoSlug": t.string(),
            "projectKey": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerRepositoryIdOut"])
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
    types["GitSourceIn"] = t.struct(
        {
            "dir": t.string().optional(),
            "revision": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["GitSourceIn"])
    types["GitSourceOut"] = t.struct(
        {
            "dir": t.string().optional(),
            "revision": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitSourceOut"])
    types["PushFilterIn"] = t.struct(
        {
            "invertRegex": t.boolean().optional(),
            "branch": t.string().optional(),
            "tag": t.string().optional(),
        }
    ).named(renames["PushFilterIn"])
    types["PushFilterOut"] = t.struct(
        {
            "invertRegex": t.boolean().optional(),
            "branch": t.string().optional(),
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PushFilterOut"])
    types["ApproveBuildRequestIn"] = t.struct(
        {"approvalResult": t.proxy(renames["ApprovalResultIn"]).optional()}
    ).named(renames["ApproveBuildRequestIn"])
    types["ApproveBuildRequestOut"] = t.struct(
        {
            "approvalResult": t.proxy(renames["ApprovalResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproveBuildRequestOut"])
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
    types["GitLabConfigIn"] = t.struct(
        {
            "secrets": t.proxy(renames["GitLabSecretsIn"]),
            "name": t.string().optional(),
            "connectedRepositories": t.array(
                t.proxy(renames["GitLabRepositoryIdIn"])
            ).optional(),
            "username": t.string().optional(),
            "enterpriseConfig": t.proxy(renames["GitLabEnterpriseConfigIn"]).optional(),
        }
    ).named(renames["GitLabConfigIn"])
    types["GitLabConfigOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "webhookKey": t.string().optional(),
            "secrets": t.proxy(renames["GitLabSecretsOut"]),
            "name": t.string().optional(),
            "connectedRepositories": t.array(
                t.proxy(renames["GitLabRepositoryIdOut"])
            ).optional(),
            "username": t.string().optional(),
            "enterpriseConfig": t.proxy(
                renames["GitLabEnterpriseConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabConfigOut"])
    types["VolumeIn"] = t.struct(
        {"name": t.string().optional(), "path": t.string().optional()}
    ).named(renames["VolumeIn"])
    types["VolumeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeOut"])
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
    types["UpdateGitHubEnterpriseConfigOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
        }
    ).named(renames["UpdateGitHubEnterpriseConfigOperationMetadataIn"])
    types["UpdateGitHubEnterpriseConfigOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateGitHubEnterpriseConfigOperationMetadataOut"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["BitbucketServerTriggerConfigIn"] = t.struct(
        {
            "projectKey": t.string(),
            "push": t.proxy(renames["PushFilterIn"]).optional(),
            "repoSlug": t.string(),
            "bitbucketServerConfigResource": t.string(),
            "pullRequest": t.proxy(renames["PullRequestFilterIn"]).optional(),
        }
    ).named(renames["BitbucketServerTriggerConfigIn"])
    types["BitbucketServerTriggerConfigOut"] = t.struct(
        {
            "projectKey": t.string(),
            "push": t.proxy(renames["PushFilterOut"]).optional(),
            "repoSlug": t.string(),
            "bitbucketServerConfigResource": t.string(),
            "bitbucketServerConfig": t.proxy(
                renames["BitbucketServerConfigOut"]
            ).optional(),
            "pullRequest": t.proxy(renames["PullRequestFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerTriggerConfigOut"])
    types["DeleteWorkerPoolOperationMetadataIn"] = t.struct(
        {
            "workerPool": t.string().optional(),
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
        }
    ).named(renames["DeleteWorkerPoolOperationMetadataIn"])
    types["DeleteWorkerPoolOperationMetadataOut"] = t.struct(
        {
            "workerPool": t.string().optional(),
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteWorkerPoolOperationMetadataOut"])
    types["CreateBitbucketServerConfigOperationMetadataIn"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
        }
    ).named(renames["CreateBitbucketServerConfigOperationMetadataIn"])
    types["CreateBitbucketServerConfigOperationMetadataOut"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateBitbucketServerConfigOperationMetadataOut"])
    types["RepoSourceIn"] = t.struct(
        {
            "tagName": t.string().optional(),
            "projectId": t.string().optional(),
            "branchName": t.string().optional(),
            "dir": t.string().optional(),
            "commitSha": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "repoName": t.string().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RepoSourceIn"])
    types["RepoSourceOut"] = t.struct(
        {
            "tagName": t.string().optional(),
            "projectId": t.string().optional(),
            "branchName": t.string().optional(),
            "dir": t.string().optional(),
            "commitSha": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "repoName": t.string().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepoSourceOut"])
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
    types["GitHubEventsConfigIn"] = t.struct(
        {
            "installationId": t.string().optional(),
            "enterpriseConfigResourceName": t.string().optional(),
            "owner": t.string().optional(),
            "push": t.proxy(renames["PushFilterIn"]).optional(),
            "name": t.string().optional(),
            "pullRequest": t.proxy(renames["PullRequestFilterIn"]).optional(),
        }
    ).named(renames["GitHubEventsConfigIn"])
    types["GitHubEventsConfigOut"] = t.struct(
        {
            "installationId": t.string().optional(),
            "enterpriseConfigResourceName": t.string().optional(),
            "owner": t.string().optional(),
            "push": t.proxy(renames["PushFilterOut"]).optional(),
            "name": t.string().optional(),
            "pullRequest": t.proxy(renames["PullRequestFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitHubEventsConfigOut"])
    types["ReceiveTriggerWebhookResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ReceiveTriggerWebhookResponseIn"])
    types["ReceiveTriggerWebhookResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReceiveTriggerWebhookResponseOut"])
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
    types["DeleteBitbucketServerConfigOperationMetadataIn"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["DeleteBitbucketServerConfigOperationMetadataIn"])
    types["DeleteBitbucketServerConfigOperationMetadataOut"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteBitbucketServerConfigOperationMetadataOut"])
    types["NpmPackageIn"] = t.struct(
        {"packagePath": t.string().optional(), "repository": t.string().optional()}
    ).named(renames["NpmPackageIn"])
    types["NpmPackageOut"] = t.struct(
        {
            "packagePath": t.string().optional(),
            "repository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NpmPackageOut"])
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
    types[
        "BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataIn"
    ] = t.struct(
        {
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "config": t.string().optional(),
        }
    ).named(
        renames["BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataIn"]
    )
    types[
        "BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataOut"
    ] = t.struct(
        {
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "config": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataOut"]
    )
    types["ApprovalResultIn"] = t.struct(
        {
            "url": t.string().optional(),
            "comment": t.string().optional(),
            "decision": t.string(),
        }
    ).named(renames["ApprovalResultIn"])
    types["ApprovalResultOut"] = t.struct(
        {
            "url": t.string().optional(),
            "approverAccount": t.string().optional(),
            "comment": t.string().optional(),
            "approvalTime": t.string().optional(),
            "decision": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApprovalResultOut"])
    types["UploadedNpmPackageIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "fileHashes": t.proxy(renames["FileHashesIn"]).optional(),
        }
    ).named(renames["UploadedNpmPackageIn"])
    types["UploadedNpmPackageOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "pushTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "fileHashes": t.proxy(renames["FileHashesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadedNpmPackageOut"])
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
    types["ListBuildTriggersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "triggers": t.array(t.proxy(renames["BuildTriggerIn"])).optional(),
        }
    ).named(renames["ListBuildTriggersResponseIn"])
    types["ListBuildTriggersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "triggers": t.array(t.proxy(renames["BuildTriggerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBuildTriggersResponseOut"])
    types["UploadedPythonPackageIn"] = t.struct(
        {
            "fileHashes": t.proxy(renames["FileHashesIn"]).optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["UploadedPythonPackageIn"])
    types["UploadedPythonPackageOut"] = t.struct(
        {
            "pushTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "fileHashes": t.proxy(renames["FileHashesOut"]).optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadedPythonPackageOut"])
    types["CreateWorkerPoolOperationMetadataIn"] = t.struct(
        {
            "workerPool": t.string().optional(),
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
        }
    ).named(renames["CreateWorkerPoolOperationMetadataIn"])
    types["CreateWorkerPoolOperationMetadataOut"] = t.struct(
        {
            "workerPool": t.string().optional(),
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateWorkerPoolOperationMetadataOut"])
    types["GitFileSourceIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "path": t.string().optional(),
            "repoType": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "repository": t.string().optional(),
            "revision": t.string().optional(),
        }
    ).named(renames["GitFileSourceIn"])
    types["GitFileSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "path": t.string().optional(),
            "repoType": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "repository": t.string().optional(),
            "revision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitFileSourceOut"])
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
            "deleteTime": t.string().optional(),
            "state": t.string().optional(),
            "privatePoolV1Config": t.proxy(
                renames["PrivatePoolV1ConfigOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerPoolOut"])
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
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "resolvedStorageSource": t.proxy(renames["StorageSourceOut"]).optional(),
            "resolvedStorageSourceManifest": t.proxy(
                renames["StorageSourceManifestOut"]
            ).optional(),
            "resolvedRepoSource": t.proxy(renames["RepoSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceProvenanceOut"])
    types["UpdateGitLabConfigOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "gitlabConfig": t.string().optional(),
            "completeTime": t.string().optional(),
        }
    ).named(renames["UpdateGitLabConfigOperationMetadataIn"])
    types["UpdateGitLabConfigOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "gitlabConfig": t.string().optional(),
            "completeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateGitLabConfigOperationMetadataOut"])
    types["CancelBuildRequestIn"] = t.struct(
        {"projectId": t.string(), "id": t.string(), "name": t.string().optional()}
    ).named(renames["CancelBuildRequestIn"])
    types["CancelBuildRequestOut"] = t.struct(
        {
            "projectId": t.string(),
            "id": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CancelBuildRequestOut"])
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
    types["BatchCreateGitLabConnectedRepositoriesResponseMetadataIn"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "config": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["BatchCreateGitLabConnectedRepositoriesResponseMetadataIn"])
    types["BatchCreateGitLabConnectedRepositoriesResponseMetadataOut"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "config": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateGitLabConnectedRepositoriesResponseMetadataOut"])
    types["DeleteGitHubEnterpriseConfigOperationMetadataIn"] = t.struct(
        {
            "githubEnterpriseConfig": t.string().optional(),
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["DeleteGitHubEnterpriseConfigOperationMetadataIn"])
    types["DeleteGitHubEnterpriseConfigOperationMetadataOut"] = t.struct(
        {
            "githubEnterpriseConfig": t.string().optional(),
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteGitHubEnterpriseConfigOperationMetadataOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["ArtifactsIn"] = t.struct(
        {
            "npmPackages": t.array(t.proxy(renames["NpmPackageIn"])).optional(),
            "pythonPackages": t.array(t.proxy(renames["PythonPackageIn"])).optional(),
            "mavenArtifacts": t.array(t.proxy(renames["MavenArtifactIn"])).optional(),
            "images": t.array(t.string()).optional(),
            "objects": t.proxy(renames["ArtifactObjectsIn"]).optional(),
        }
    ).named(renames["ArtifactsIn"])
    types["ArtifactsOut"] = t.struct(
        {
            "npmPackages": t.array(t.proxy(renames["NpmPackageOut"])).optional(),
            "pythonPackages": t.array(t.proxy(renames["PythonPackageOut"])).optional(),
            "mavenArtifacts": t.array(t.proxy(renames["MavenArtifactOut"])).optional(),
            "images": t.array(t.string()).optional(),
            "objects": t.proxy(renames["ArtifactObjectsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArtifactsOut"])
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
        {"value": t.string().optional(), "type": t.string().optional()}
    ).named(renames["HashIn"])
    types["HashOut"] = t.struct(
        {
            "value": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HashOut"])
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
            "generation": t.string().optional(),
            "bucket": t.string().optional(),
            "object": t.string().optional(),
        }
    ).named(renames["StorageSourceManifestIn"])
    types["StorageSourceManifestOut"] = t.struct(
        {
            "generation": t.string().optional(),
            "bucket": t.string().optional(),
            "object": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StorageSourceManifestOut"])
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
    types["GitLabEnterpriseConfigIn"] = t.struct(
        {
            "hostUri": t.string().optional(),
            "sslCa": t.string().optional(),
            "serviceDirectoryConfig": t.proxy(
                renames["ServiceDirectoryConfigIn"]
            ).optional(),
        }
    ).named(renames["GitLabEnterpriseConfigIn"])
    types["GitLabEnterpriseConfigOut"] = t.struct(
        {
            "hostUri": t.string().optional(),
            "sslCa": t.string().optional(),
            "serviceDirectoryConfig": t.proxy(
                renames["ServiceDirectoryConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabEnterpriseConfigOut"])
    types["BuildOptionsIn"] = t.struct(
        {
            "dynamicSubstitutions": t.boolean().optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "env": t.array(t.string()).optional(),
            "machineType": t.string().optional(),
            "logStreamingOption": t.string().optional(),
            "defaultLogsBucketBehavior": t.string().optional(),
            "requestedVerifyOption": t.string().optional(),
            "secretEnv": t.array(t.string()).optional(),
            "logging": t.string().optional(),
            "workerPool": t.string().optional(),
            "substitutionOption": t.string().optional(),
            "sourceProvenanceHash": t.array(t.string()).optional(),
            "pool": t.proxy(renames["PoolOptionIn"]).optional(),
            "diskSizeGb": t.string().optional(),
        }
    ).named(renames["BuildOptionsIn"])
    types["BuildOptionsOut"] = t.struct(
        {
            "dynamicSubstitutions": t.boolean().optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "env": t.array(t.string()).optional(),
            "machineType": t.string().optional(),
            "logStreamingOption": t.string().optional(),
            "defaultLogsBucketBehavior": t.string().optional(),
            "requestedVerifyOption": t.string().optional(),
            "secretEnv": t.array(t.string()).optional(),
            "logging": t.string().optional(),
            "workerPool": t.string().optional(),
            "substitutionOption": t.string().optional(),
            "sourceProvenanceHash": t.array(t.string()).optional(),
            "pool": t.proxy(renames["PoolOptionOut"]).optional(),
            "diskSizeGb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOptionsOut"])
    types["RetryBuildRequestIn"] = t.struct(
        {"id": t.string(), "name": t.string().optional(), "projectId": t.string()}
    ).named(renames["RetryBuildRequestIn"])
    types["RetryBuildRequestOut"] = t.struct(
        {
            "id": t.string(),
            "name": t.string().optional(),
            "projectId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetryBuildRequestOut"])
    types["ApprovalConfigIn"] = t.struct(
        {"approvalRequired": t.boolean().optional()}
    ).named(renames["ApprovalConfigIn"])
    types["ApprovalConfigOut"] = t.struct(
        {
            "approvalRequired": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApprovalConfigOut"])
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
    types["BitbucketServerConfigIn"] = t.struct(
        {
            "sslCa": t.string().optional(),
            "name": t.string().optional(),
            "hostUri": t.string(),
            "secrets": t.proxy(renames["BitbucketServerSecretsIn"]),
            "createTime": t.string().optional(),
            "peeredNetwork": t.string().optional(),
            "apiKey": t.string(),
            "username": t.string().optional(),
        }
    ).named(renames["BitbucketServerConfigIn"])
    types["BitbucketServerConfigOut"] = t.struct(
        {
            "sslCa": t.string().optional(),
            "name": t.string().optional(),
            "hostUri": t.string(),
            "secrets": t.proxy(renames["BitbucketServerSecretsOut"]),
            "createTime": t.string().optional(),
            "peeredNetwork": t.string().optional(),
            "connectedRepositories": t.array(
                t.proxy(renames["BitbucketServerRepositoryIdOut"])
            ).optional(),
            "apiKey": t.string(),
            "webhookKey": t.string().optional(),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerConfigOut"])
    types["BuildIn"] = t.struct(
        {
            "options": t.proxy(renames["BuildOptionsIn"]).optional(),
            "availableSecrets": t.proxy(renames["SecretsIn"]).optional(),
            "timeout": t.string().optional(),
            "steps": t.array(t.proxy(renames["BuildStepIn"])),
            "tags": t.array(t.string()).optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
            "serviceAccount": t.string().optional(),
            "secrets": t.array(t.proxy(renames["SecretIn"])).optional(),
            "images": t.array(t.string()).optional(),
            "logsBucket": t.string().optional(),
            "artifacts": t.proxy(renames["ArtifactsIn"]).optional(),
            "queueTtl": t.string().optional(),
        }
    ).named(renames["BuildIn"])
    types["BuildOut"] = t.struct(
        {
            "sourceProvenance": t.proxy(renames["SourceProvenanceOut"]).optional(),
            "options": t.proxy(renames["BuildOptionsOut"]).optional(),
            "warnings": t.array(t.proxy(renames["WarningOut"])).optional(),
            "availableSecrets": t.proxy(renames["SecretsOut"]).optional(),
            "startTime": t.string().optional(),
            "timeout": t.string().optional(),
            "name": t.string().optional(),
            "finishTime": t.string().optional(),
            "results": t.proxy(renames["ResultsOut"]).optional(),
            "approval": t.proxy(renames["BuildApprovalOut"]).optional(),
            "steps": t.array(t.proxy(renames["BuildStepOut"])),
            "tags": t.array(t.string()).optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "projectId": t.string().optional(),
            "status": t.string().optional(),
            "timing": t.struct({"_": t.string().optional()}).optional(),
            "logUrl": t.string().optional(),
            "createTime": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "secrets": t.array(t.proxy(renames["SecretOut"])).optional(),
            "images": t.array(t.string()).optional(),
            "logsBucket": t.string().optional(),
            "artifacts": t.proxy(renames["ArtifactsOut"]).optional(),
            "statusDetail": t.string().optional(),
            "buildTriggerId": t.string().optional(),
            "queueTtl": t.string().optional(),
            "id": t.string().optional(),
            "failureInfo": t.proxy(renames["FailureInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOut"])
    types["MavenArtifactIn"] = t.struct(
        {
            "repository": t.string().optional(),
            "path": t.string().optional(),
            "version": t.string().optional(),
            "artifactId": t.string().optional(),
            "groupId": t.string().optional(),
        }
    ).named(renames["MavenArtifactIn"])
    types["MavenArtifactOut"] = t.struct(
        {
            "repository": t.string().optional(),
            "path": t.string().optional(),
            "version": t.string().optional(),
            "artifactId": t.string().optional(),
            "groupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MavenArtifactOut"])

    functions = {}
    functions["projectsTriggersCreate"] = cloudbuild.get(
        "v1/projects/{projectId}/triggers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBuildTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersDelete"] = cloudbuild.get(
        "v1/projects/{projectId}/triggers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBuildTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersWebhook"] = cloudbuild.get(
        "v1/projects/{projectId}/triggers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBuildTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersGet"] = cloudbuild.get(
        "v1/projects/{projectId}/triggers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBuildTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersPatch"] = cloudbuild.get(
        "v1/projects/{projectId}/triggers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBuildTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersRun"] = cloudbuild.get(
        "v1/projects/{projectId}/triggers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBuildTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersList"] = cloudbuild.get(
        "v1/projects/{projectId}/triggers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBuildTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsApprove"] = cloudbuild.post(
        "v1/projects/{projectId}/builds/{id}:retry",
        t.struct(
            {
                "projectId": t.string(),
                "id": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsCreate"] = cloudbuild.post(
        "v1/projects/{projectId}/builds/{id}:retry",
        t.struct(
            {
                "projectId": t.string(),
                "id": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsGet"] = cloudbuild.post(
        "v1/projects/{projectId}/builds/{id}:retry",
        t.struct(
            {
                "projectId": t.string(),
                "id": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsCancel"] = cloudbuild.post(
        "v1/projects/{projectId}/builds/{id}:retry",
        t.struct(
            {
                "projectId": t.string(),
                "id": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsList"] = cloudbuild.post(
        "v1/projects/{projectId}/builds/{id}:retry",
        t.struct(
            {
                "projectId": t.string(),
                "id": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsRetry"] = cloudbuild.post(
        "v1/projects/{projectId}/builds/{id}:retry",
        t.struct(
            {
                "projectId": t.string(),
                "id": t.string(),
                "name": t.string().optional(),
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
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "configId": t.string().optional(),
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
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "configId": t.string().optional(),
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
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "configId": t.string().optional(),
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
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "configId": t.string().optional(),
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
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "configId": t.string().optional(),
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
                "peeredNetwork": t.string().optional(),
                "webhookKey": t.string().optional(),
                "hostUrl": t.string().optional(),
                "sslCa": t.string().optional(),
                "displayName": t.string().optional(),
                "appId": t.string(),
                "secrets": t.proxy(renames["GitHubEnterpriseSecretsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGithubEnterpriseConfigsGet"] = cloudbuild.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "peeredNetwork": t.string().optional(),
                "webhookKey": t.string().optional(),
                "hostUrl": t.string().optional(),
                "sslCa": t.string().optional(),
                "displayName": t.string().optional(),
                "appId": t.string(),
                "secrets": t.proxy(renames["GitHubEnterpriseSecretsIn"]).optional(),
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
                "peeredNetwork": t.string().optional(),
                "webhookKey": t.string().optional(),
                "hostUrl": t.string().optional(),
                "sslCa": t.string().optional(),
                "displayName": t.string().optional(),
                "appId": t.string(),
                "secrets": t.proxy(renames["GitHubEnterpriseSecretsIn"]).optional(),
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
                "peeredNetwork": t.string().optional(),
                "webhookKey": t.string().optional(),
                "hostUrl": t.string().optional(),
                "sslCa": t.string().optional(),
                "displayName": t.string().optional(),
                "appId": t.string(),
                "secrets": t.proxy(renames["GitHubEnterpriseSecretsIn"]).optional(),
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
                "peeredNetwork": t.string().optional(),
                "webhookKey": t.string().optional(),
                "hostUrl": t.string().optional(),
                "sslCa": t.string().optional(),
                "displayName": t.string().optional(),
                "appId": t.string(),
                "secrets": t.proxy(renames["GitHubEnterpriseSecretsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersWebhook"] = cloudbuild.post(
        "v1/{parent}/triggers",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string(),
                "build": t.proxy(renames["BuildIn"]).optional(),
                "disabled": t.boolean().optional(),
                "github": t.proxy(renames["GitHubEventsConfigIn"]).optional(),
                "eventType": t.string().optional(),
                "ignoredFiles": t.array(t.string()).optional(),
                "autodetect": t.boolean().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "bitbucketServerTriggerConfig": t.proxy(
                    renames["BitbucketServerTriggerConfigIn"]
                ).optional(),
                "serviceAccount": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "pubsubConfig": t.proxy(renames["PubsubConfigIn"]).optional(),
                "resourceName": t.string().optional(),
                "sourceToBuild": t.proxy(renames["GitRepoSourceIn"]).optional(),
                "triggerTemplate": t.proxy(renames["RepoSourceIn"]).optional(),
                "includedFiles": t.array(t.string()).optional(),
                "repositoryEventConfig": t.proxy(
                    renames["RepositoryEventConfigIn"]
                ).optional(),
                "gitlabEnterpriseEventsConfig": t.proxy(
                    renames["GitLabEventsConfigIn"]
                ).optional(),
                "webhookConfig": t.proxy(renames["WebhookConfigIn"]).optional(),
                "filename": t.string().optional(),
                "gitFileSource": t.proxy(renames["GitFileSourceIn"]).optional(),
                "includeBuildLogs": t.string().optional(),
                "approvalConfig": t.proxy(renames["ApprovalConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersList"] = cloudbuild.post(
        "v1/{parent}/triggers",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string(),
                "build": t.proxy(renames["BuildIn"]).optional(),
                "disabled": t.boolean().optional(),
                "github": t.proxy(renames["GitHubEventsConfigIn"]).optional(),
                "eventType": t.string().optional(),
                "ignoredFiles": t.array(t.string()).optional(),
                "autodetect": t.boolean().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "bitbucketServerTriggerConfig": t.proxy(
                    renames["BitbucketServerTriggerConfigIn"]
                ).optional(),
                "serviceAccount": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "pubsubConfig": t.proxy(renames["PubsubConfigIn"]).optional(),
                "resourceName": t.string().optional(),
                "sourceToBuild": t.proxy(renames["GitRepoSourceIn"]).optional(),
                "triggerTemplate": t.proxy(renames["RepoSourceIn"]).optional(),
                "includedFiles": t.array(t.string()).optional(),
                "repositoryEventConfig": t.proxy(
                    renames["RepositoryEventConfigIn"]
                ).optional(),
                "gitlabEnterpriseEventsConfig": t.proxy(
                    renames["GitLabEventsConfigIn"]
                ).optional(),
                "webhookConfig": t.proxy(renames["WebhookConfigIn"]).optional(),
                "filename": t.string().optional(),
                "gitFileSource": t.proxy(renames["GitFileSourceIn"]).optional(),
                "includeBuildLogs": t.string().optional(),
                "approvalConfig": t.proxy(renames["ApprovalConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersPatch"] = cloudbuild.post(
        "v1/{parent}/triggers",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string(),
                "build": t.proxy(renames["BuildIn"]).optional(),
                "disabled": t.boolean().optional(),
                "github": t.proxy(renames["GitHubEventsConfigIn"]).optional(),
                "eventType": t.string().optional(),
                "ignoredFiles": t.array(t.string()).optional(),
                "autodetect": t.boolean().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "bitbucketServerTriggerConfig": t.proxy(
                    renames["BitbucketServerTriggerConfigIn"]
                ).optional(),
                "serviceAccount": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "pubsubConfig": t.proxy(renames["PubsubConfigIn"]).optional(),
                "resourceName": t.string().optional(),
                "sourceToBuild": t.proxy(renames["GitRepoSourceIn"]).optional(),
                "triggerTemplate": t.proxy(renames["RepoSourceIn"]).optional(),
                "includedFiles": t.array(t.string()).optional(),
                "repositoryEventConfig": t.proxy(
                    renames["RepositoryEventConfigIn"]
                ).optional(),
                "gitlabEnterpriseEventsConfig": t.proxy(
                    renames["GitLabEventsConfigIn"]
                ).optional(),
                "webhookConfig": t.proxy(renames["WebhookConfigIn"]).optional(),
                "filename": t.string().optional(),
                "gitFileSource": t.proxy(renames["GitFileSourceIn"]).optional(),
                "includeBuildLogs": t.string().optional(),
                "approvalConfig": t.proxy(renames["ApprovalConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersRun"] = cloudbuild.post(
        "v1/{parent}/triggers",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string(),
                "build": t.proxy(renames["BuildIn"]).optional(),
                "disabled": t.boolean().optional(),
                "github": t.proxy(renames["GitHubEventsConfigIn"]).optional(),
                "eventType": t.string().optional(),
                "ignoredFiles": t.array(t.string()).optional(),
                "autodetect": t.boolean().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "bitbucketServerTriggerConfig": t.proxy(
                    renames["BitbucketServerTriggerConfigIn"]
                ).optional(),
                "serviceAccount": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "pubsubConfig": t.proxy(renames["PubsubConfigIn"]).optional(),
                "resourceName": t.string().optional(),
                "sourceToBuild": t.proxy(renames["GitRepoSourceIn"]).optional(),
                "triggerTemplate": t.proxy(renames["RepoSourceIn"]).optional(),
                "includedFiles": t.array(t.string()).optional(),
                "repositoryEventConfig": t.proxy(
                    renames["RepositoryEventConfigIn"]
                ).optional(),
                "gitlabEnterpriseEventsConfig": t.proxy(
                    renames["GitLabEventsConfigIn"]
                ).optional(),
                "webhookConfig": t.proxy(renames["WebhookConfigIn"]).optional(),
                "filename": t.string().optional(),
                "gitFileSource": t.proxy(renames["GitFileSourceIn"]).optional(),
                "includeBuildLogs": t.string().optional(),
                "approvalConfig": t.proxy(renames["ApprovalConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersGet"] = cloudbuild.post(
        "v1/{parent}/triggers",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string(),
                "build": t.proxy(renames["BuildIn"]).optional(),
                "disabled": t.boolean().optional(),
                "github": t.proxy(renames["GitHubEventsConfigIn"]).optional(),
                "eventType": t.string().optional(),
                "ignoredFiles": t.array(t.string()).optional(),
                "autodetect": t.boolean().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "bitbucketServerTriggerConfig": t.proxy(
                    renames["BitbucketServerTriggerConfigIn"]
                ).optional(),
                "serviceAccount": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "pubsubConfig": t.proxy(renames["PubsubConfigIn"]).optional(),
                "resourceName": t.string().optional(),
                "sourceToBuild": t.proxy(renames["GitRepoSourceIn"]).optional(),
                "triggerTemplate": t.proxy(renames["RepoSourceIn"]).optional(),
                "includedFiles": t.array(t.string()).optional(),
                "repositoryEventConfig": t.proxy(
                    renames["RepositoryEventConfigIn"]
                ).optional(),
                "gitlabEnterpriseEventsConfig": t.proxy(
                    renames["GitLabEventsConfigIn"]
                ).optional(),
                "webhookConfig": t.proxy(renames["WebhookConfigIn"]).optional(),
                "filename": t.string().optional(),
                "gitFileSource": t.proxy(renames["GitFileSourceIn"]).optional(),
                "includeBuildLogs": t.string().optional(),
                "approvalConfig": t.proxy(renames["ApprovalConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersDelete"] = cloudbuild.post(
        "v1/{parent}/triggers",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string(),
                "build": t.proxy(renames["BuildIn"]).optional(),
                "disabled": t.boolean().optional(),
                "github": t.proxy(renames["GitHubEventsConfigIn"]).optional(),
                "eventType": t.string().optional(),
                "ignoredFiles": t.array(t.string()).optional(),
                "autodetect": t.boolean().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "bitbucketServerTriggerConfig": t.proxy(
                    renames["BitbucketServerTriggerConfigIn"]
                ).optional(),
                "serviceAccount": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "pubsubConfig": t.proxy(renames["PubsubConfigIn"]).optional(),
                "resourceName": t.string().optional(),
                "sourceToBuild": t.proxy(renames["GitRepoSourceIn"]).optional(),
                "triggerTemplate": t.proxy(renames["RepoSourceIn"]).optional(),
                "includedFiles": t.array(t.string()).optional(),
                "repositoryEventConfig": t.proxy(
                    renames["RepositoryEventConfigIn"]
                ).optional(),
                "gitlabEnterpriseEventsConfig": t.proxy(
                    renames["GitLabEventsConfigIn"]
                ).optional(),
                "webhookConfig": t.proxy(renames["WebhookConfigIn"]).optional(),
                "filename": t.string().optional(),
                "gitFileSource": t.proxy(renames["GitFileSourceIn"]).optional(),
                "includeBuildLogs": t.string().optional(),
                "approvalConfig": t.proxy(renames["ApprovalConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersCreate"] = cloudbuild.post(
        "v1/{parent}/triggers",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string(),
                "build": t.proxy(renames["BuildIn"]).optional(),
                "disabled": t.boolean().optional(),
                "github": t.proxy(renames["GitHubEventsConfigIn"]).optional(),
                "eventType": t.string().optional(),
                "ignoredFiles": t.array(t.string()).optional(),
                "autodetect": t.boolean().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "bitbucketServerTriggerConfig": t.proxy(
                    renames["BitbucketServerTriggerConfigIn"]
                ).optional(),
                "serviceAccount": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "pubsubConfig": t.proxy(renames["PubsubConfigIn"]).optional(),
                "resourceName": t.string().optional(),
                "sourceToBuild": t.proxy(renames["GitRepoSourceIn"]).optional(),
                "triggerTemplate": t.proxy(renames["RepoSourceIn"]).optional(),
                "includedFiles": t.array(t.string()).optional(),
                "repositoryEventConfig": t.proxy(
                    renames["RepositoryEventConfigIn"]
                ).optional(),
                "gitlabEnterpriseEventsConfig": t.proxy(
                    renames["GitLabEventsConfigIn"]
                ).optional(),
                "webhookConfig": t.proxy(renames["WebhookConfigIn"]).optional(),
                "filename": t.string().optional(),
                "gitFileSource": t.proxy(renames["GitFileSourceIn"]).optional(),
                "includeBuildLogs": t.string().optional(),
                "approvalConfig": t.proxy(renames["ApprovalConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGitLabConfigsRemoveGitLabConnectedRepository"
    ] = cloudbuild.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GitLabConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGitLabConfigsPatch"] = cloudbuild.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GitLabConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGitLabConfigsList"] = cloudbuild.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GitLabConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGitLabConfigsCreate"] = cloudbuild.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GitLabConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGitLabConfigsDelete"] = cloudbuild.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GitLabConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGitLabConfigsGet"] = cloudbuild.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GitLabConfigOut"]),
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
    functions["projectsLocationsGitLabConfigsReposList"] = cloudbuild.get(
        "v1/{parent}/repos",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGitLabRepositoriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBitbucketServerConfigsPatch"] = cloudbuild.post(
        "v1/{parent}/bitbucketServerConfigs",
        t.struct(
            {
                "bitbucketServerConfigId": t.string().optional(),
                "parent": t.string(),
                "sslCa": t.string().optional(),
                "name": t.string().optional(),
                "hostUri": t.string(),
                "secrets": t.proxy(renames["BitbucketServerSecretsIn"]),
                "createTime": t.string().optional(),
                "peeredNetwork": t.string().optional(),
                "apiKey": t.string(),
                "username": t.string().optional(),
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
                "sslCa": t.string().optional(),
                "name": t.string().optional(),
                "hostUri": t.string(),
                "secrets": t.proxy(renames["BitbucketServerSecretsIn"]),
                "createTime": t.string().optional(),
                "peeredNetwork": t.string().optional(),
                "apiKey": t.string(),
                "username": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBitbucketServerConfigsGet"] = cloudbuild.post(
        "v1/{parent}/bitbucketServerConfigs",
        t.struct(
            {
                "bitbucketServerConfigId": t.string().optional(),
                "parent": t.string(),
                "sslCa": t.string().optional(),
                "name": t.string().optional(),
                "hostUri": t.string(),
                "secrets": t.proxy(renames["BitbucketServerSecretsIn"]),
                "createTime": t.string().optional(),
                "peeredNetwork": t.string().optional(),
                "apiKey": t.string(),
                "username": t.string().optional(),
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
                "sslCa": t.string().optional(),
                "name": t.string().optional(),
                "hostUri": t.string(),
                "secrets": t.proxy(renames["BitbucketServerSecretsIn"]),
                "createTime": t.string().optional(),
                "peeredNetwork": t.string().optional(),
                "apiKey": t.string(),
                "username": t.string().optional(),
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
                "sslCa": t.string().optional(),
                "name": t.string().optional(),
                "hostUri": t.string(),
                "secrets": t.proxy(renames["BitbucketServerSecretsIn"]),
                "createTime": t.string().optional(),
                "peeredNetwork": t.string().optional(),
                "apiKey": t.string(),
                "username": t.string().optional(),
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
                "sslCa": t.string().optional(),
                "name": t.string().optional(),
                "hostUri": t.string(),
                "secrets": t.proxy(renames["BitbucketServerSecretsIn"]),
                "createTime": t.string().optional(),
                "peeredNetwork": t.string().optional(),
                "apiKey": t.string(),
                "username": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBitbucketServerRepositoriesResponseOut"]),
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
    functions["projectsLocationsBuildsRetry"] = cloudbuild.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "id": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsList"] = cloudbuild.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "id": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsCancel"] = cloudbuild.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "id": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsCreate"] = cloudbuild.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "id": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsApprove"] = cloudbuild.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "id": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsGet"] = cloudbuild.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "id": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = cloudbuild.post(
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
    functions["projectsLocationsOperationsCancel"] = cloudbuild.post(
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
    functions["projectsLocationsWorkerPoolsGet"] = cloudbuild.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkerPoolsCreate"] = cloudbuild.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkerPoolsList"] = cloudbuild.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkerPoolsPatch"] = cloudbuild.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkerPoolsDelete"] = cloudbuild.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsRegionalWebhook"] = cloudbuild.post(
        "v1/{location}/regionalWebhook",
        t.struct(
            {
                "location": t.string(),
                "webhookKey": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "data": t.string().optional(),
                "contentType": t.string().optional(),
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
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "data": t.string().optional(),
                "contentType": t.string().optional(),
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
    functions["v1Webhook"] = cloudbuild.post(
        "v1/webhook",
        t.struct(
            {
                "webhookKey": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "data": t.string().optional(),
                "contentType": t.string().optional(),
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
