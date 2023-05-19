from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_cloudbuild() -> Import:
    cloudbuild = HTTPRuntime("https://cloudbuild.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudbuild_1_ErrorResponse",
        "UploadedNpmPackageIn": "_cloudbuild_2_UploadedNpmPackageIn",
        "UploadedNpmPackageOut": "_cloudbuild_3_UploadedNpmPackageOut",
        "DeleteGitHubEnterpriseConfigOperationMetadataIn": "_cloudbuild_4_DeleteGitHubEnterpriseConfigOperationMetadataIn",
        "DeleteGitHubEnterpriseConfigOperationMetadataOut": "_cloudbuild_5_DeleteGitHubEnterpriseConfigOperationMetadataOut",
        "CreateBitbucketServerConfigOperationMetadataIn": "_cloudbuild_6_CreateBitbucketServerConfigOperationMetadataIn",
        "CreateBitbucketServerConfigOperationMetadataOut": "_cloudbuild_7_CreateBitbucketServerConfigOperationMetadataOut",
        "WorkerConfigIn": "_cloudbuild_8_WorkerConfigIn",
        "WorkerConfigOut": "_cloudbuild_9_WorkerConfigOut",
        "ArtifactsIn": "_cloudbuild_10_ArtifactsIn",
        "ArtifactsOut": "_cloudbuild_11_ArtifactsOut",
        "GitRepoSourceIn": "_cloudbuild_12_GitRepoSourceIn",
        "GitRepoSourceOut": "_cloudbuild_13_GitRepoSourceOut",
        "InlineSecretIn": "_cloudbuild_14_InlineSecretIn",
        "InlineSecretOut": "_cloudbuild_15_InlineSecretOut",
        "GitLabSecretsIn": "_cloudbuild_16_GitLabSecretsIn",
        "GitLabSecretsOut": "_cloudbuild_17_GitLabSecretsOut",
        "ListBuildsResponseIn": "_cloudbuild_18_ListBuildsResponseIn",
        "ListBuildsResponseOut": "_cloudbuild_19_ListBuildsResponseOut",
        "GitHubEnterpriseConfigIn": "_cloudbuild_20_GitHubEnterpriseConfigIn",
        "GitHubEnterpriseConfigOut": "_cloudbuild_21_GitHubEnterpriseConfigOut",
        "StorageSourceManifestIn": "_cloudbuild_22_StorageSourceManifestIn",
        "StorageSourceManifestOut": "_cloudbuild_23_StorageSourceManifestOut",
        "ListGitLabConfigsResponseIn": "_cloudbuild_24_ListGitLabConfigsResponseIn",
        "ListGitLabConfigsResponseOut": "_cloudbuild_25_ListGitLabConfigsResponseOut",
        "ServiceDirectoryConfigIn": "_cloudbuild_26_ServiceDirectoryConfigIn",
        "ServiceDirectoryConfigOut": "_cloudbuild_27_ServiceDirectoryConfigOut",
        "UploadedMavenArtifactIn": "_cloudbuild_28_UploadedMavenArtifactIn",
        "UploadedMavenArtifactOut": "_cloudbuild_29_UploadedMavenArtifactOut",
        "BitbucketServerSecretsIn": "_cloudbuild_30_BitbucketServerSecretsIn",
        "BitbucketServerSecretsOut": "_cloudbuild_31_BitbucketServerSecretsOut",
        "PythonPackageIn": "_cloudbuild_32_PythonPackageIn",
        "PythonPackageOut": "_cloudbuild_33_PythonPackageOut",
        "BuildStepIn": "_cloudbuild_34_BuildStepIn",
        "BuildStepOut": "_cloudbuild_35_BuildStepOut",
        "WarningIn": "_cloudbuild_36_WarningIn",
        "WarningOut": "_cloudbuild_37_WarningOut",
        "MavenArtifactIn": "_cloudbuild_38_MavenArtifactIn",
        "MavenArtifactOut": "_cloudbuild_39_MavenArtifactOut",
        "ResultsIn": "_cloudbuild_40_ResultsIn",
        "ResultsOut": "_cloudbuild_41_ResultsOut",
        "UpdateGitLabConfigOperationMetadataIn": "_cloudbuild_42_UpdateGitLabConfigOperationMetadataIn",
        "UpdateGitLabConfigOperationMetadataOut": "_cloudbuild_43_UpdateGitLabConfigOperationMetadataOut",
        "ApprovalConfigIn": "_cloudbuild_44_ApprovalConfigIn",
        "ApprovalConfigOut": "_cloudbuild_45_ApprovalConfigOut",
        "CreateWorkerPoolOperationMetadataIn": "_cloudbuild_46_CreateWorkerPoolOperationMetadataIn",
        "CreateWorkerPoolOperationMetadataOut": "_cloudbuild_47_CreateWorkerPoolOperationMetadataOut",
        "ProcessAppManifestCallbackOperationMetadataIn": "_cloudbuild_48_ProcessAppManifestCallbackOperationMetadataIn",
        "ProcessAppManifestCallbackOperationMetadataOut": "_cloudbuild_49_ProcessAppManifestCallbackOperationMetadataOut",
        "SecretsIn": "_cloudbuild_50_SecretsIn",
        "SecretsOut": "_cloudbuild_51_SecretsOut",
        "BuiltImageIn": "_cloudbuild_52_BuiltImageIn",
        "BuiltImageOut": "_cloudbuild_53_BuiltImageOut",
        "OperationIn": "_cloudbuild_54_OperationIn",
        "OperationOut": "_cloudbuild_55_OperationOut",
        "CancelBuildRequestIn": "_cloudbuild_56_CancelBuildRequestIn",
        "CancelBuildRequestOut": "_cloudbuild_57_CancelBuildRequestOut",
        "RepoSourceIn": "_cloudbuild_58_RepoSourceIn",
        "RepoSourceOut": "_cloudbuild_59_RepoSourceOut",
        "EmptyIn": "_cloudbuild_60_EmptyIn",
        "EmptyOut": "_cloudbuild_61_EmptyOut",
        "BuildApprovalIn": "_cloudbuild_62_BuildApprovalIn",
        "BuildApprovalOut": "_cloudbuild_63_BuildApprovalOut",
        "ListBitbucketServerConfigsResponseIn": "_cloudbuild_64_ListBitbucketServerConfigsResponseIn",
        "ListBitbucketServerConfigsResponseOut": "_cloudbuild_65_ListBitbucketServerConfigsResponseOut",
        "SecretManagerSecretIn": "_cloudbuild_66_SecretManagerSecretIn",
        "SecretManagerSecretOut": "_cloudbuild_67_SecretManagerSecretOut",
        "UpdateGitHubEnterpriseConfigOperationMetadataIn": "_cloudbuild_68_UpdateGitHubEnterpriseConfigOperationMetadataIn",
        "UpdateGitHubEnterpriseConfigOperationMetadataOut": "_cloudbuild_69_UpdateGitHubEnterpriseConfigOperationMetadataOut",
        "UpdateBitbucketServerConfigOperationMetadataIn": "_cloudbuild_70_UpdateBitbucketServerConfigOperationMetadataIn",
        "UpdateBitbucketServerConfigOperationMetadataOut": "_cloudbuild_71_UpdateBitbucketServerConfigOperationMetadataOut",
        "BitbucketServerTriggerConfigIn": "_cloudbuild_72_BitbucketServerTriggerConfigIn",
        "BitbucketServerTriggerConfigOut": "_cloudbuild_73_BitbucketServerTriggerConfigOut",
        "CreateGitLabConfigOperationMetadataIn": "_cloudbuild_74_CreateGitLabConfigOperationMetadataIn",
        "CreateGitLabConfigOperationMetadataOut": "_cloudbuild_75_CreateGitLabConfigOperationMetadataOut",
        "ArtifactObjectsIn": "_cloudbuild_76_ArtifactObjectsIn",
        "ArtifactObjectsOut": "_cloudbuild_77_ArtifactObjectsOut",
        "GitLabConnectedRepositoryIn": "_cloudbuild_78_GitLabConnectedRepositoryIn",
        "GitLabConnectedRepositoryOut": "_cloudbuild_79_GitLabConnectedRepositoryOut",
        "DeleteGitLabConfigOperationMetadataIn": "_cloudbuild_80_DeleteGitLabConfigOperationMetadataIn",
        "DeleteGitLabConfigOperationMetadataOut": "_cloudbuild_81_DeleteGitLabConfigOperationMetadataOut",
        "HttpBodyIn": "_cloudbuild_82_HttpBodyIn",
        "HttpBodyOut": "_cloudbuild_83_HttpBodyOut",
        "UpdateWorkerPoolOperationMetadataIn": "_cloudbuild_84_UpdateWorkerPoolOperationMetadataIn",
        "UpdateWorkerPoolOperationMetadataOut": "_cloudbuild_85_UpdateWorkerPoolOperationMetadataOut",
        "BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataIn": "_cloudbuild_86_BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataIn",
        "BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataOut": "_cloudbuild_87_BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataOut",
        "GitSourceIn": "_cloudbuild_88_GitSourceIn",
        "GitSourceOut": "_cloudbuild_89_GitSourceOut",
        "FailureInfoIn": "_cloudbuild_90_FailureInfoIn",
        "FailureInfoOut": "_cloudbuild_91_FailureInfoOut",
        "BuildOperationMetadataIn": "_cloudbuild_92_BuildOperationMetadataIn",
        "BuildOperationMetadataOut": "_cloudbuild_93_BuildOperationMetadataOut",
        "BuildTriggerIn": "_cloudbuild_94_BuildTriggerIn",
        "BuildTriggerOut": "_cloudbuild_95_BuildTriggerOut",
        "ListBuildTriggersResponseIn": "_cloudbuild_96_ListBuildTriggersResponseIn",
        "ListBuildTriggersResponseOut": "_cloudbuild_97_ListBuildTriggersResponseOut",
        "CancelOperationRequestIn": "_cloudbuild_98_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_cloudbuild_99_CancelOperationRequestOut",
        "GitFileSourceIn": "_cloudbuild_100_GitFileSourceIn",
        "GitFileSourceOut": "_cloudbuild_101_GitFileSourceOut",
        "PushFilterIn": "_cloudbuild_102_PushFilterIn",
        "PushFilterOut": "_cloudbuild_103_PushFilterOut",
        "BatchCreateBitbucketServerConnectedRepositoriesResponseIn": "_cloudbuild_104_BatchCreateBitbucketServerConnectedRepositoriesResponseIn",
        "BatchCreateBitbucketServerConnectedRepositoriesResponseOut": "_cloudbuild_105_BatchCreateBitbucketServerConnectedRepositoriesResponseOut",
        "RetryBuildRequestIn": "_cloudbuild_106_RetryBuildRequestIn",
        "RetryBuildRequestOut": "_cloudbuild_107_RetryBuildRequestOut",
        "StatusIn": "_cloudbuild_108_StatusIn",
        "StatusOut": "_cloudbuild_109_StatusOut",
        "NetworkConfigIn": "_cloudbuild_110_NetworkConfigIn",
        "NetworkConfigOut": "_cloudbuild_111_NetworkConfigOut",
        "BitbucketServerRepositoryIdIn": "_cloudbuild_112_BitbucketServerRepositoryIdIn",
        "BitbucketServerRepositoryIdOut": "_cloudbuild_113_BitbucketServerRepositoryIdOut",
        "SecretIn": "_cloudbuild_114_SecretIn",
        "SecretOut": "_cloudbuild_115_SecretOut",
        "BatchCreateGitLabConnectedRepositoriesResponseIn": "_cloudbuild_116_BatchCreateGitLabConnectedRepositoriesResponseIn",
        "BatchCreateGitLabConnectedRepositoriesResponseOut": "_cloudbuild_117_BatchCreateGitLabConnectedRepositoriesResponseOut",
        "BatchCreateGitLabConnectedRepositoriesRequestIn": "_cloudbuild_118_BatchCreateGitLabConnectedRepositoriesRequestIn",
        "BatchCreateGitLabConnectedRepositoriesRequestOut": "_cloudbuild_119_BatchCreateGitLabConnectedRepositoriesRequestOut",
        "WebhookConfigIn": "_cloudbuild_120_WebhookConfigIn",
        "WebhookConfigOut": "_cloudbuild_121_WebhookConfigOut",
        "SourceIn": "_cloudbuild_122_SourceIn",
        "SourceOut": "_cloudbuild_123_SourceOut",
        "ListGithubEnterpriseConfigsResponseIn": "_cloudbuild_124_ListGithubEnterpriseConfigsResponseIn",
        "ListGithubEnterpriseConfigsResponseOut": "_cloudbuild_125_ListGithubEnterpriseConfigsResponseOut",
        "GitHubEnterpriseSecretsIn": "_cloudbuild_126_GitHubEnterpriseSecretsIn",
        "GitHubEnterpriseSecretsOut": "_cloudbuild_127_GitHubEnterpriseSecretsOut",
        "BitbucketServerConnectedRepositoryIn": "_cloudbuild_128_BitbucketServerConnectedRepositoryIn",
        "BitbucketServerConnectedRepositoryOut": "_cloudbuild_129_BitbucketServerConnectedRepositoryOut",
        "RemoveBitbucketServerConnectedRepositoryRequestIn": "_cloudbuild_130_RemoveBitbucketServerConnectedRepositoryRequestIn",
        "RemoveBitbucketServerConnectedRepositoryRequestOut": "_cloudbuild_131_RemoveBitbucketServerConnectedRepositoryRequestOut",
        "ListGitLabRepositoriesResponseIn": "_cloudbuild_132_ListGitLabRepositoriesResponseIn",
        "ListGitLabRepositoriesResponseOut": "_cloudbuild_133_ListGitLabRepositoriesResponseOut",
        "NpmPackageIn": "_cloudbuild_134_NpmPackageIn",
        "NpmPackageOut": "_cloudbuild_135_NpmPackageOut",
        "OperationMetadataIn": "_cloudbuild_136_OperationMetadataIn",
        "OperationMetadataOut": "_cloudbuild_137_OperationMetadataOut",
        "PullRequestFilterIn": "_cloudbuild_138_PullRequestFilterIn",
        "PullRequestFilterOut": "_cloudbuild_139_PullRequestFilterOut",
        "DeleteWorkerPoolOperationMetadataIn": "_cloudbuild_140_DeleteWorkerPoolOperationMetadataIn",
        "DeleteWorkerPoolOperationMetadataOut": "_cloudbuild_141_DeleteWorkerPoolOperationMetadataOut",
        "FileHashesIn": "_cloudbuild_142_FileHashesIn",
        "FileHashesOut": "_cloudbuild_143_FileHashesOut",
        "DeleteBitbucketServerConfigOperationMetadataIn": "_cloudbuild_144_DeleteBitbucketServerConfigOperationMetadataIn",
        "DeleteBitbucketServerConfigOperationMetadataOut": "_cloudbuild_145_DeleteBitbucketServerConfigOperationMetadataOut",
        "BatchCreateGitLabConnectedRepositoriesResponseMetadataIn": "_cloudbuild_146_BatchCreateGitLabConnectedRepositoriesResponseMetadataIn",
        "BatchCreateGitLabConnectedRepositoriesResponseMetadataOut": "_cloudbuild_147_BatchCreateGitLabConnectedRepositoriesResponseMetadataOut",
        "BitbucketServerRepositoryIn": "_cloudbuild_148_BitbucketServerRepositoryIn",
        "BitbucketServerRepositoryOut": "_cloudbuild_149_BitbucketServerRepositoryOut",
        "StorageSourceIn": "_cloudbuild_150_StorageSourceIn",
        "StorageSourceOut": "_cloudbuild_151_StorageSourceOut",
        "RemoveGitLabConnectedRepositoryRequestIn": "_cloudbuild_152_RemoveGitLabConnectedRepositoryRequestIn",
        "RemoveGitLabConnectedRepositoryRequestOut": "_cloudbuild_153_RemoveGitLabConnectedRepositoryRequestOut",
        "HashIn": "_cloudbuild_154_HashIn",
        "HashOut": "_cloudbuild_155_HashOut",
        "CreateBitbucketServerConnectedRepositoryRequestIn": "_cloudbuild_156_CreateBitbucketServerConnectedRepositoryRequestIn",
        "CreateBitbucketServerConnectedRepositoryRequestOut": "_cloudbuild_157_CreateBitbucketServerConnectedRepositoryRequestOut",
        "GitLabConfigIn": "_cloudbuild_158_GitLabConfigIn",
        "GitLabConfigOut": "_cloudbuild_159_GitLabConfigOut",
        "CreateGitLabConnectedRepositoryRequestIn": "_cloudbuild_160_CreateGitLabConnectedRepositoryRequestIn",
        "CreateGitLabConnectedRepositoryRequestOut": "_cloudbuild_161_CreateGitLabConnectedRepositoryRequestOut",
        "ListWorkerPoolsResponseIn": "_cloudbuild_162_ListWorkerPoolsResponseIn",
        "ListWorkerPoolsResponseOut": "_cloudbuild_163_ListWorkerPoolsResponseOut",
        "GitLabEnterpriseConfigIn": "_cloudbuild_164_GitLabEnterpriseConfigIn",
        "GitLabEnterpriseConfigOut": "_cloudbuild_165_GitLabEnterpriseConfigOut",
        "UploadedPythonPackageIn": "_cloudbuild_166_UploadedPythonPackageIn",
        "UploadedPythonPackageOut": "_cloudbuild_167_UploadedPythonPackageOut",
        "SourceProvenanceIn": "_cloudbuild_168_SourceProvenanceIn",
        "SourceProvenanceOut": "_cloudbuild_169_SourceProvenanceOut",
        "TimeSpanIn": "_cloudbuild_170_TimeSpanIn",
        "TimeSpanOut": "_cloudbuild_171_TimeSpanOut",
        "WorkerPoolIn": "_cloudbuild_172_WorkerPoolIn",
        "WorkerPoolOut": "_cloudbuild_173_WorkerPoolOut",
        "BuildIn": "_cloudbuild_174_BuildIn",
        "BuildOut": "_cloudbuild_175_BuildOut",
        "GitLabRepositoryIn": "_cloudbuild_176_GitLabRepositoryIn",
        "GitLabRepositoryOut": "_cloudbuild_177_GitLabRepositoryOut",
        "RunBuildTriggerRequestIn": "_cloudbuild_178_RunBuildTriggerRequestIn",
        "RunBuildTriggerRequestOut": "_cloudbuild_179_RunBuildTriggerRequestOut",
        "ListBitbucketServerRepositoriesResponseIn": "_cloudbuild_180_ListBitbucketServerRepositoriesResponseIn",
        "ListBitbucketServerRepositoriesResponseOut": "_cloudbuild_181_ListBitbucketServerRepositoriesResponseOut",
        "CreateGitHubEnterpriseConfigOperationMetadataIn": "_cloudbuild_182_CreateGitHubEnterpriseConfigOperationMetadataIn",
        "CreateGitHubEnterpriseConfigOperationMetadataOut": "_cloudbuild_183_CreateGitHubEnterpriseConfigOperationMetadataOut",
        "GitLabEventsConfigIn": "_cloudbuild_184_GitLabEventsConfigIn",
        "GitLabEventsConfigOut": "_cloudbuild_185_GitLabEventsConfigOut",
        "VolumeIn": "_cloudbuild_186_VolumeIn",
        "VolumeOut": "_cloudbuild_187_VolumeOut",
        "ApproveBuildRequestIn": "_cloudbuild_188_ApproveBuildRequestIn",
        "ApproveBuildRequestOut": "_cloudbuild_189_ApproveBuildRequestOut",
        "BuildOptionsIn": "_cloudbuild_190_BuildOptionsIn",
        "BuildOptionsOut": "_cloudbuild_191_BuildOptionsOut",
        "ArtifactResultIn": "_cloudbuild_192_ArtifactResultIn",
        "ArtifactResultOut": "_cloudbuild_193_ArtifactResultOut",
        "BatchCreateBitbucketServerConnectedRepositoriesRequestIn": "_cloudbuild_194_BatchCreateBitbucketServerConnectedRepositoriesRequestIn",
        "BatchCreateBitbucketServerConnectedRepositoriesRequestOut": "_cloudbuild_195_BatchCreateBitbucketServerConnectedRepositoriesRequestOut",
        "ReceiveTriggerWebhookResponseIn": "_cloudbuild_196_ReceiveTriggerWebhookResponseIn",
        "ReceiveTriggerWebhookResponseOut": "_cloudbuild_197_ReceiveTriggerWebhookResponseOut",
        "PrivatePoolV1ConfigIn": "_cloudbuild_198_PrivatePoolV1ConfigIn",
        "PrivatePoolV1ConfigOut": "_cloudbuild_199_PrivatePoolV1ConfigOut",
        "PoolOptionIn": "_cloudbuild_200_PoolOptionIn",
        "PoolOptionOut": "_cloudbuild_201_PoolOptionOut",
        "GitHubEventsConfigIn": "_cloudbuild_202_GitHubEventsConfigIn",
        "GitHubEventsConfigOut": "_cloudbuild_203_GitHubEventsConfigOut",
        "GitLabRepositoryIdIn": "_cloudbuild_204_GitLabRepositoryIdIn",
        "GitLabRepositoryIdOut": "_cloudbuild_205_GitLabRepositoryIdOut",
        "RepositoryEventConfigIn": "_cloudbuild_206_RepositoryEventConfigIn",
        "RepositoryEventConfigOut": "_cloudbuild_207_RepositoryEventConfigOut",
        "BitbucketServerConfigIn": "_cloudbuild_208_BitbucketServerConfigIn",
        "BitbucketServerConfigOut": "_cloudbuild_209_BitbucketServerConfigOut",
        "ApprovalResultIn": "_cloudbuild_210_ApprovalResultIn",
        "ApprovalResultOut": "_cloudbuild_211_ApprovalResultOut",
        "PubsubConfigIn": "_cloudbuild_212_PubsubConfigIn",
        "PubsubConfigOut": "_cloudbuild_213_PubsubConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["UploadedNpmPackageIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "fileHashes": t.proxy(renames["FileHashesIn"]).optional(),
        }
    ).named(renames["UploadedNpmPackageIn"])
    types["UploadedNpmPackageOut"] = t.struct(
        {
            "pushTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "uri": t.string().optional(),
            "fileHashes": t.proxy(renames["FileHashesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadedNpmPackageOut"])
    types["DeleteGitHubEnterpriseConfigOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
        }
    ).named(renames["DeleteGitHubEnterpriseConfigOperationMetadataIn"])
    types["DeleteGitHubEnterpriseConfigOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteGitHubEnterpriseConfigOperationMetadataOut"])
    types["CreateBitbucketServerConfigOperationMetadataIn"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["CreateBitbucketServerConfigOperationMetadataIn"])
    types["CreateBitbucketServerConfigOperationMetadataOut"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateBitbucketServerConfigOperationMetadataOut"])
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
    types["ArtifactsIn"] = t.struct(
        {
            "npmPackages": t.array(t.proxy(renames["NpmPackageIn"])).optional(),
            "images": t.array(t.string()).optional(),
            "objects": t.proxy(renames["ArtifactObjectsIn"]).optional(),
            "mavenArtifacts": t.array(t.proxy(renames["MavenArtifactIn"])).optional(),
            "pythonPackages": t.array(t.proxy(renames["PythonPackageIn"])).optional(),
        }
    ).named(renames["ArtifactsIn"])
    types["ArtifactsOut"] = t.struct(
        {
            "npmPackages": t.array(t.proxy(renames["NpmPackageOut"])).optional(),
            "images": t.array(t.string()).optional(),
            "objects": t.proxy(renames["ArtifactObjectsOut"]).optional(),
            "mavenArtifacts": t.array(t.proxy(renames["MavenArtifactOut"])).optional(),
            "pythonPackages": t.array(t.proxy(renames["PythonPackageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArtifactsOut"])
    types["GitRepoSourceIn"] = t.struct(
        {
            "ref": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "repository": t.string().optional(),
            "uri": t.string().optional(),
            "repoType": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
        }
    ).named(renames["GitRepoSourceIn"])
    types["GitRepoSourceOut"] = t.struct(
        {
            "ref": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "repository": t.string().optional(),
            "uri": t.string().optional(),
            "repoType": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitRepoSourceOut"])
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
    types["GitLabSecretsIn"] = t.struct(
        {
            "apiKeyVersion": t.string(),
            "webhookSecretVersion": t.string(),
            "apiAccessTokenVersion": t.string(),
            "readAccessTokenVersion": t.string(),
        }
    ).named(renames["GitLabSecretsIn"])
    types["GitLabSecretsOut"] = t.struct(
        {
            "apiKeyVersion": t.string(),
            "webhookSecretVersion": t.string(),
            "apiAccessTokenVersion": t.string(),
            "readAccessTokenVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabSecretsOut"])
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
    types["GitHubEnterpriseConfigIn"] = t.struct(
        {
            "appId": t.string(),
            "secrets": t.proxy(renames["GitHubEnterpriseSecretsIn"]).optional(),
            "sslCa": t.string().optional(),
            "name": t.string().optional(),
            "hostUrl": t.string().optional(),
            "peeredNetwork": t.string().optional(),
            "displayName": t.string().optional(),
            "webhookKey": t.string().optional(),
        }
    ).named(renames["GitHubEnterpriseConfigIn"])
    types["GitHubEnterpriseConfigOut"] = t.struct(
        {
            "appId": t.string(),
            "secrets": t.proxy(renames["GitHubEnterpriseSecretsOut"]).optional(),
            "sslCa": t.string().optional(),
            "name": t.string().optional(),
            "hostUrl": t.string().optional(),
            "createTime": t.string().optional(),
            "peeredNetwork": t.string().optional(),
            "displayName": t.string().optional(),
            "webhookKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitHubEnterpriseConfigOut"])
    types["StorageSourceManifestIn"] = t.struct(
        {
            "generation": t.string().optional(),
            "object": t.string().optional(),
            "bucket": t.string().optional(),
        }
    ).named(renames["StorageSourceManifestIn"])
    types["StorageSourceManifestOut"] = t.struct(
        {
            "generation": t.string().optional(),
            "object": t.string().optional(),
            "bucket": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StorageSourceManifestOut"])
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
    types["ServiceDirectoryConfigIn"] = t.struct(
        {"service": t.string().optional()}
    ).named(renames["ServiceDirectoryConfigIn"])
    types["ServiceDirectoryConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceDirectoryConfigOut"])
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
    types["BitbucketServerSecretsIn"] = t.struct(
        {
            "adminAccessTokenVersionName": t.string(),
            "readAccessTokenVersionName": t.string(),
            "webhookSecretVersionName": t.string(),
        }
    ).named(renames["BitbucketServerSecretsIn"])
    types["BitbucketServerSecretsOut"] = t.struct(
        {
            "adminAccessTokenVersionName": t.string(),
            "readAccessTokenVersionName": t.string(),
            "webhookSecretVersionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerSecretsOut"])
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
    types["BuildStepIn"] = t.struct(
        {
            "allowExitCodes": t.array(t.integer()).optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "args": t.array(t.string()).optional(),
            "entrypoint": t.string().optional(),
            "allowFailure": t.boolean().optional(),
            "name": t.string(),
            "dir": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "timeout": t.string().optional(),
            "script": t.string().optional(),
            "secretEnv": t.array(t.string()).optional(),
        }
    ).named(renames["BuildStepIn"])
    types["BuildStepOut"] = t.struct(
        {
            "allowExitCodes": t.array(t.integer()).optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "args": t.array(t.string()).optional(),
            "entrypoint": t.string().optional(),
            "status": t.string().optional(),
            "allowFailure": t.boolean().optional(),
            "name": t.string(),
            "dir": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "exitCode": t.integer().optional(),
            "waitFor": t.array(t.string()).optional(),
            "pullTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "timeout": t.string().optional(),
            "script": t.string().optional(),
            "timing": t.proxy(renames["TimeSpanOut"]).optional(),
            "secretEnv": t.array(t.string()).optional(),
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
    types["MavenArtifactIn"] = t.struct(
        {
            "groupId": t.string().optional(),
            "repository": t.string().optional(),
            "version": t.string().optional(),
            "artifactId": t.string().optional(),
            "path": t.string().optional(),
        }
    ).named(renames["MavenArtifactIn"])
    types["MavenArtifactOut"] = t.struct(
        {
            "groupId": t.string().optional(),
            "repository": t.string().optional(),
            "version": t.string().optional(),
            "artifactId": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MavenArtifactOut"])
    types["ResultsIn"] = t.struct(
        {
            "mavenArtifacts": t.array(
                t.proxy(renames["UploadedMavenArtifactIn"])
            ).optional(),
            "buildStepImages": t.array(t.string()).optional(),
            "numArtifacts": t.string().optional(),
            "pythonPackages": t.array(
                t.proxy(renames["UploadedPythonPackageIn"])
            ).optional(),
            "images": t.array(t.proxy(renames["BuiltImageIn"])).optional(),
            "npmPackages": t.array(t.proxy(renames["UploadedNpmPackageIn"])).optional(),
            "artifactTiming": t.proxy(renames["TimeSpanIn"]).optional(),
            "artifactManifest": t.string().optional(),
            "buildStepOutputs": t.array(t.string()).optional(),
        }
    ).named(renames["ResultsIn"])
    types["ResultsOut"] = t.struct(
        {
            "mavenArtifacts": t.array(
                t.proxy(renames["UploadedMavenArtifactOut"])
            ).optional(),
            "buildStepImages": t.array(t.string()).optional(),
            "numArtifacts": t.string().optional(),
            "pythonPackages": t.array(
                t.proxy(renames["UploadedPythonPackageOut"])
            ).optional(),
            "images": t.array(t.proxy(renames["BuiltImageOut"])).optional(),
            "npmPackages": t.array(
                t.proxy(renames["UploadedNpmPackageOut"])
            ).optional(),
            "artifactTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "artifactManifest": t.string().optional(),
            "buildStepOutputs": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultsOut"])
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
    types["ApprovalConfigIn"] = t.struct(
        {"approvalRequired": t.boolean().optional()}
    ).named(renames["ApprovalConfigIn"])
    types["ApprovalConfigOut"] = t.struct(
        {
            "approvalRequired": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApprovalConfigOut"])
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
    types["ProcessAppManifestCallbackOperationMetadataIn"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
        }
    ).named(renames["ProcessAppManifestCallbackOperationMetadataIn"])
    types["ProcessAppManifestCallbackOperationMetadataOut"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProcessAppManifestCallbackOperationMetadataOut"])
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
    types["BuiltImageIn"] = t.struct(
        {"digest": t.string().optional(), "name": t.string().optional()}
    ).named(renames["BuiltImageIn"])
    types["BuiltImageOut"] = t.struct(
        {
            "digest": t.string().optional(),
            "pushTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuiltImageOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["RepoSourceIn"] = t.struct(
        {
            "dir": t.string().optional(),
            "tagName": t.string().optional(),
            "branchName": t.string().optional(),
            "projectId": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "commitSha": t.string().optional(),
            "repoName": t.string().optional(),
        }
    ).named(renames["RepoSourceIn"])
    types["RepoSourceOut"] = t.struct(
        {
            "dir": t.string().optional(),
            "tagName": t.string().optional(),
            "branchName": t.string().optional(),
            "projectId": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "commitSha": t.string().optional(),
            "repoName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepoSourceOut"])
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
    types["UpdateGitHubEnterpriseConfigOperationMetadataIn"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
        }
    ).named(renames["UpdateGitHubEnterpriseConfigOperationMetadataIn"])
    types["UpdateGitHubEnterpriseConfigOperationMetadataOut"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateGitHubEnterpriseConfigOperationMetadataOut"])
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
    types["BitbucketServerTriggerConfigIn"] = t.struct(
        {
            "bitbucketServerConfigResource": t.string(),
            "pullRequest": t.proxy(renames["PullRequestFilterIn"]).optional(),
            "repoSlug": t.string(),
            "projectKey": t.string(),
            "push": t.proxy(renames["PushFilterIn"]).optional(),
        }
    ).named(renames["BitbucketServerTriggerConfigIn"])
    types["BitbucketServerTriggerConfigOut"] = t.struct(
        {
            "bitbucketServerConfigResource": t.string(),
            "bitbucketServerConfig": t.proxy(
                renames["BitbucketServerConfigOut"]
            ).optional(),
            "pullRequest": t.proxy(renames["PullRequestFilterOut"]).optional(),
            "repoSlug": t.string(),
            "projectKey": t.string(),
            "push": t.proxy(renames["PushFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerTriggerConfigOut"])
    types["CreateGitLabConfigOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "gitlabConfig": t.string().optional(),
            "completeTime": t.string().optional(),
        }
    ).named(renames["CreateGitLabConfigOperationMetadataIn"])
    types["CreateGitLabConfigOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "gitlabConfig": t.string().optional(),
            "completeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateGitLabConfigOperationMetadataOut"])
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
    types["HttpBodyIn"] = t.struct(
        {
            "data": t.string().optional(),
            "contentType": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["HttpBodyIn"])
    types["HttpBodyOut"] = t.struct(
        {
            "data": t.string().optional(),
            "contentType": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpBodyOut"])
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
    types[
        "BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataIn"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "config": t.string().optional(),
            "completeTime": t.string().optional(),
        }
    ).named(
        renames["BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataIn"]
    )
    types[
        "BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataOut"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "config": t.string().optional(),
            "completeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["BatchCreateBitbucketServerConnectedRepositoriesResponseMetadataOut"]
    )
    types["GitSourceIn"] = t.struct(
        {
            "dir": t.string().optional(),
            "url": t.string().optional(),
            "revision": t.string().optional(),
        }
    ).named(renames["GitSourceIn"])
    types["GitSourceOut"] = t.struct(
        {
            "dir": t.string().optional(),
            "url": t.string().optional(),
            "revision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitSourceOut"])
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
    types["BuildOperationMetadataIn"] = t.struct(
        {"build": t.proxy(renames["BuildIn"]).optional()}
    ).named(renames["BuildOperationMetadataIn"])
    types["BuildOperationMetadataOut"] = t.struct(
        {
            "build": t.proxy(renames["BuildOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOperationMetadataOut"])
    types["BuildTriggerIn"] = t.struct(
        {
            "filename": t.string().optional(),
            "build": t.proxy(renames["BuildIn"]).optional(),
            "sourceToBuild": t.proxy(renames["GitRepoSourceIn"]).optional(),
            "github": t.proxy(renames["GitHubEventsConfigIn"]).optional(),
            "triggerTemplate": t.proxy(renames["RepoSourceIn"]).optional(),
            "approvalConfig": t.proxy(renames["ApprovalConfigIn"]).optional(),
            "includedFiles": t.array(t.string()).optional(),
            "pubsubConfig": t.proxy(renames["PubsubConfigIn"]).optional(),
            "disabled": t.boolean().optional(),
            "gitFileSource": t.proxy(renames["GitFileSourceIn"]).optional(),
            "repositoryEventConfig": t.proxy(
                renames["RepositoryEventConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "ignoredFiles": t.array(t.string()).optional(),
            "bitbucketServerTriggerConfig": t.proxy(
                renames["BitbucketServerTriggerConfigIn"]
            ).optional(),
            "autodetect": t.boolean().optional(),
            "serviceAccount": t.string().optional(),
            "gitlabEnterpriseEventsConfig": t.proxy(
                renames["GitLabEventsConfigIn"]
            ).optional(),
            "filter": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "eventType": t.string().optional(),
            "description": t.string().optional(),
            "includeBuildLogs": t.string().optional(),
            "webhookConfig": t.proxy(renames["WebhookConfigIn"]).optional(),
            "resourceName": t.string().optional(),
        }
    ).named(renames["BuildTriggerIn"])
    types["BuildTriggerOut"] = t.struct(
        {
            "filename": t.string().optional(),
            "build": t.proxy(renames["BuildOut"]).optional(),
            "createTime": t.string().optional(),
            "sourceToBuild": t.proxy(renames["GitRepoSourceOut"]).optional(),
            "github": t.proxy(renames["GitHubEventsConfigOut"]).optional(),
            "triggerTemplate": t.proxy(renames["RepoSourceOut"]).optional(),
            "approvalConfig": t.proxy(renames["ApprovalConfigOut"]).optional(),
            "includedFiles": t.array(t.string()).optional(),
            "pubsubConfig": t.proxy(renames["PubsubConfigOut"]).optional(),
            "disabled": t.boolean().optional(),
            "gitFileSource": t.proxy(renames["GitFileSourceOut"]).optional(),
            "repositoryEventConfig": t.proxy(
                renames["RepositoryEventConfigOut"]
            ).optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "ignoredFiles": t.array(t.string()).optional(),
            "bitbucketServerTriggerConfig": t.proxy(
                renames["BitbucketServerTriggerConfigOut"]
            ).optional(),
            "autodetect": t.boolean().optional(),
            "serviceAccount": t.string().optional(),
            "gitlabEnterpriseEventsConfig": t.proxy(
                renames["GitLabEventsConfigOut"]
            ).optional(),
            "filter": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "eventType": t.string().optional(),
            "description": t.string().optional(),
            "includeBuildLogs": t.string().optional(),
            "webhookConfig": t.proxy(renames["WebhookConfigOut"]).optional(),
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildTriggerOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["GitFileSourceIn"] = t.struct(
        {
            "repository": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "uri": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "revision": t.string().optional(),
            "path": t.string().optional(),
            "repoType": t.string().optional(),
        }
    ).named(renames["GitFileSourceIn"])
    types["GitFileSourceOut"] = t.struct(
        {
            "repository": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "uri": t.string().optional(),
            "bitbucketServerConfig": t.string().optional(),
            "revision": t.string().optional(),
            "path": t.string().optional(),
            "repoType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitFileSourceOut"])
    types["PushFilterIn"] = t.struct(
        {
            "invertRegex": t.boolean().optional(),
            "tag": t.string().optional(),
            "branch": t.string().optional(),
        }
    ).named(renames["PushFilterIn"])
    types["PushFilterOut"] = t.struct(
        {
            "invertRegex": t.boolean().optional(),
            "tag": t.string().optional(),
            "branch": t.string().optional(),
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
    types["RetryBuildRequestIn"] = t.struct(
        {"projectId": t.string(), "id": t.string(), "name": t.string().optional()}
    ).named(renames["RetryBuildRequestIn"])
    types["RetryBuildRequestOut"] = t.struct(
        {
            "projectId": t.string(),
            "id": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetryBuildRequestOut"])
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
    types["BitbucketServerRepositoryIdIn"] = t.struct(
        {"repoSlug": t.string(), "projectKey": t.string()}
    ).named(renames["BitbucketServerRepositoryIdIn"])
    types["BitbucketServerRepositoryIdOut"] = t.struct(
        {
            "repoSlug": t.string(),
            "projectKey": t.string(),
            "webhookId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerRepositoryIdOut"])
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
            "storageSource": t.proxy(renames["StorageSourceIn"]).optional(),
            "repoSource": t.proxy(renames["RepoSourceIn"]).optional(),
            "gitSource": t.proxy(renames["GitSourceIn"]).optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "storageSourceManifest": t.proxy(
                renames["StorageSourceManifestOut"]
            ).optional(),
            "storageSource": t.proxy(renames["StorageSourceOut"]).optional(),
            "repoSource": t.proxy(renames["RepoSourceOut"]).optional(),
            "gitSource": t.proxy(renames["GitSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
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
    types["GitHubEnterpriseSecretsIn"] = t.struct(
        {
            "oauthClientIdName": t.string().optional(),
            "webhookSecretName": t.string().optional(),
            "privateKeyVersionName": t.string().optional(),
            "oauthSecretVersionName": t.string().optional(),
            "privateKeyName": t.string().optional(),
            "oauthSecretName": t.string().optional(),
            "webhookSecretVersionName": t.string().optional(),
            "oauthClientIdVersionName": t.string().optional(),
        }
    ).named(renames["GitHubEnterpriseSecretsIn"])
    types["GitHubEnterpriseSecretsOut"] = t.struct(
        {
            "oauthClientIdName": t.string().optional(),
            "webhookSecretName": t.string().optional(),
            "privateKeyVersionName": t.string().optional(),
            "oauthSecretVersionName": t.string().optional(),
            "privateKeyName": t.string().optional(),
            "oauthSecretName": t.string().optional(),
            "webhookSecretVersionName": t.string().optional(),
            "oauthClientIdVersionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitHubEnterpriseSecretsOut"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["PullRequestFilterIn"] = t.struct(
        {
            "branch": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "commentControl": t.string().optional(),
        }
    ).named(renames["PullRequestFilterIn"])
    types["PullRequestFilterOut"] = t.struct(
        {
            "branch": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "commentControl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PullRequestFilterOut"])
    types["DeleteWorkerPoolOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "workerPool": t.string().optional(),
            "completeTime": t.string().optional(),
        }
    ).named(renames["DeleteWorkerPoolOperationMetadataIn"])
    types["DeleteWorkerPoolOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "workerPool": t.string().optional(),
            "completeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteWorkerPoolOperationMetadataOut"])
    types["FileHashesIn"] = t.struct(
        {"fileHash": t.array(t.proxy(renames["HashIn"])).optional()}
    ).named(renames["FileHashesIn"])
    types["FileHashesOut"] = t.struct(
        {
            "fileHash": t.array(t.proxy(renames["HashOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileHashesOut"])
    types["DeleteBitbucketServerConfigOperationMetadataIn"] = t.struct(
        {
            "bitbucketServerConfig": t.string().optional(),
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
        }
    ).named(renames["DeleteBitbucketServerConfigOperationMetadataIn"])
    types["DeleteBitbucketServerConfigOperationMetadataOut"] = t.struct(
        {
            "bitbucketServerConfig": t.string().optional(),
            "createTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteBitbucketServerConfigOperationMetadataOut"])
    types["BatchCreateGitLabConnectedRepositoriesResponseMetadataIn"] = t.struct(
        {
            "config": t.string().optional(),
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["BatchCreateGitLabConnectedRepositoriesResponseMetadataIn"])
    types["BatchCreateGitLabConnectedRepositoriesResponseMetadataOut"] = t.struct(
        {
            "config": t.string().optional(),
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateGitLabConnectedRepositoriesResponseMetadataOut"])
    types["BitbucketServerRepositoryIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "browseUri": t.string().optional(),
            "name": t.string().optional(),
            "repoId": t.proxy(renames["BitbucketServerRepositoryIdIn"]).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["BitbucketServerRepositoryIn"])
    types["BitbucketServerRepositoryOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "browseUri": t.string().optional(),
            "name": t.string().optional(),
            "repoId": t.proxy(renames["BitbucketServerRepositoryIdOut"]).optional(),
            "description": t.string().optional(),
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
    types["RemoveGitLabConnectedRepositoryRequestIn"] = t.struct(
        {"connectedRepository": t.proxy(renames["GitLabRepositoryIdIn"]).optional()}
    ).named(renames["RemoveGitLabConnectedRepositoryRequestIn"])
    types["RemoveGitLabConnectedRepositoryRequestOut"] = t.struct(
        {
            "connectedRepository": t.proxy(renames["GitLabRepositoryIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveGitLabConnectedRepositoryRequestOut"])
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
    types["GitLabConfigIn"] = t.struct(
        {
            "username": t.string().optional(),
            "connectedRepositories": t.array(
                t.proxy(renames["GitLabRepositoryIdIn"])
            ).optional(),
            "name": t.string().optional(),
            "enterpriseConfig": t.proxy(renames["GitLabEnterpriseConfigIn"]).optional(),
            "secrets": t.proxy(renames["GitLabSecretsIn"]),
        }
    ).named(renames["GitLabConfigIn"])
    types["GitLabConfigOut"] = t.struct(
        {
            "username": t.string().optional(),
            "createTime": t.string().optional(),
            "connectedRepositories": t.array(
                t.proxy(renames["GitLabRepositoryIdOut"])
            ).optional(),
            "name": t.string().optional(),
            "webhookKey": t.string().optional(),
            "enterpriseConfig": t.proxy(
                renames["GitLabEnterpriseConfigOut"]
            ).optional(),
            "secrets": t.proxy(renames["GitLabSecretsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabConfigOut"])
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
    types["GitLabEnterpriseConfigIn"] = t.struct(
        {
            "hostUri": t.string().optional(),
            "serviceDirectoryConfig": t.proxy(
                renames["ServiceDirectoryConfigIn"]
            ).optional(),
            "sslCa": t.string().optional(),
        }
    ).named(renames["GitLabEnterpriseConfigIn"])
    types["GitLabEnterpriseConfigOut"] = t.struct(
        {
            "hostUri": t.string().optional(),
            "serviceDirectoryConfig": t.proxy(
                renames["ServiceDirectoryConfigOut"]
            ).optional(),
            "sslCa": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabEnterpriseConfigOut"])
    types["UploadedPythonPackageIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "fileHashes": t.proxy(renames["FileHashesIn"]).optional(),
        }
    ).named(renames["UploadedPythonPackageIn"])
    types["UploadedPythonPackageOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "fileHashes": t.proxy(renames["FileHashesOut"]).optional(),
            "pushTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadedPythonPackageOut"])
    types["SourceProvenanceIn"] = t.struct(
        {
            "resolvedStorageSource": t.proxy(renames["StorageSourceIn"]).optional(),
            "resolvedRepoSource": t.proxy(renames["RepoSourceIn"]).optional(),
            "resolvedStorageSourceManifest": t.proxy(
                renames["StorageSourceManifestIn"]
            ).optional(),
        }
    ).named(renames["SourceProvenanceIn"])
    types["SourceProvenanceOut"] = t.struct(
        {
            "resolvedStorageSource": t.proxy(renames["StorageSourceOut"]).optional(),
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "resolvedRepoSource": t.proxy(renames["RepoSourceOut"]).optional(),
            "resolvedStorageSourceManifest": t.proxy(
                renames["StorageSourceManifestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceProvenanceOut"])
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
    types["WorkerPoolIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "privatePoolV1Config": t.proxy(renames["PrivatePoolV1ConfigIn"]).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["WorkerPoolIn"])
    types["WorkerPoolOut"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "privatePoolV1Config": t.proxy(
                renames["PrivatePoolV1ConfigOut"]
            ).optional(),
            "deleteTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerPoolOut"])
    types["BuildIn"] = t.struct(
        {
            "availableSecrets": t.proxy(renames["SecretsIn"]).optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
            "artifacts": t.proxy(renames["ArtifactsIn"]).optional(),
            "steps": t.array(t.proxy(renames["BuildStepIn"])),
            "queueTtl": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "options": t.proxy(renames["BuildOptionsIn"]).optional(),
            "images": t.array(t.string()).optional(),
            "secrets": t.array(t.proxy(renames["SecretIn"])).optional(),
            "logsBucket": t.string().optional(),
            "timeout": t.string().optional(),
            "tags": t.array(t.string()).optional(),
        }
    ).named(renames["BuildIn"])
    types["BuildOut"] = t.struct(
        {
            "availableSecrets": t.proxy(renames["SecretsOut"]).optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "name": t.string().optional(),
            "approval": t.proxy(renames["BuildApprovalOut"]).optional(),
            "statusDetail": t.string().optional(),
            "artifacts": t.proxy(renames["ArtifactsOut"]).optional(),
            "steps": t.array(t.proxy(renames["BuildStepOut"])),
            "createTime": t.string().optional(),
            "finishTime": t.string().optional(),
            "failureInfo": t.proxy(renames["FailureInfoOut"]).optional(),
            "queueTtl": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "options": t.proxy(renames["BuildOptionsOut"]).optional(),
            "id": t.string().optional(),
            "images": t.array(t.string()).optional(),
            "warnings": t.array(t.proxy(renames["WarningOut"])).optional(),
            "logUrl": t.string().optional(),
            "startTime": t.string().optional(),
            "secrets": t.array(t.proxy(renames["SecretOut"])).optional(),
            "logsBucket": t.string().optional(),
            "status": t.string().optional(),
            "timing": t.struct({"_": t.string().optional()}).optional(),
            "sourceProvenance": t.proxy(renames["SourceProvenanceOut"]).optional(),
            "timeout": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "results": t.proxy(renames["ResultsOut"]).optional(),
            "projectId": t.string().optional(),
            "buildTriggerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOut"])
    types["GitLabRepositoryIn"] = t.struct(
        {
            "browseUri": t.string().optional(),
            "description": t.string().optional(),
            "repositoryId": t.proxy(renames["GitLabRepositoryIdIn"]).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GitLabRepositoryIn"])
    types["GitLabRepositoryOut"] = t.struct(
        {
            "browseUri": t.string().optional(),
            "description": t.string().optional(),
            "repositoryId": t.proxy(renames["GitLabRepositoryIdOut"]).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabRepositoryOut"])
    types["RunBuildTriggerRequestIn"] = t.struct(
        {
            "triggerId": t.string(),
            "source": t.proxy(renames["RepoSourceIn"]).optional(),
            "projectId": t.string(),
        }
    ).named(renames["RunBuildTriggerRequestIn"])
    types["RunBuildTriggerRequestOut"] = t.struct(
        {
            "triggerId": t.string(),
            "source": t.proxy(renames["RepoSourceOut"]).optional(),
            "projectId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunBuildTriggerRequestOut"])
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
    types["CreateGitHubEnterpriseConfigOperationMetadataIn"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
        }
    ).named(renames["CreateGitHubEnterpriseConfigOperationMetadataIn"])
    types["CreateGitHubEnterpriseConfigOperationMetadataOut"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "githubEnterpriseConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateGitHubEnterpriseConfigOperationMetadataOut"])
    types["GitLabEventsConfigIn"] = t.struct(
        {
            "projectNamespace": t.string().optional(),
            "pullRequest": t.proxy(renames["PullRequestFilterIn"]).optional(),
            "push": t.proxy(renames["PushFilterIn"]).optional(),
            "gitlabConfigResource": t.string().optional(),
        }
    ).named(renames["GitLabEventsConfigIn"])
    types["GitLabEventsConfigOut"] = t.struct(
        {
            "projectNamespace": t.string().optional(),
            "pullRequest": t.proxy(renames["PullRequestFilterOut"]).optional(),
            "gitlabConfig": t.proxy(renames["GitLabConfigOut"]).optional(),
            "push": t.proxy(renames["PushFilterOut"]).optional(),
            "gitlabConfigResource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabEventsConfigOut"])
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
    types["ApproveBuildRequestIn"] = t.struct(
        {"approvalResult": t.proxy(renames["ApprovalResultIn"]).optional()}
    ).named(renames["ApproveBuildRequestIn"])
    types["ApproveBuildRequestOut"] = t.struct(
        {
            "approvalResult": t.proxy(renames["ApprovalResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproveBuildRequestOut"])
    types["BuildOptionsIn"] = t.struct(
        {
            "secretEnv": t.array(t.string()).optional(),
            "dynamicSubstitutions": t.boolean().optional(),
            "workerPool": t.string().optional(),
            "substitutionOption": t.string().optional(),
            "logStreamingOption": t.string().optional(),
            "diskSizeGb": t.string().optional(),
            "requestedVerifyOption": t.string().optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "env": t.array(t.string()).optional(),
            "logging": t.string().optional(),
            "machineType": t.string().optional(),
            "pool": t.proxy(renames["PoolOptionIn"]).optional(),
            "sourceProvenanceHash": t.array(t.string()).optional(),
            "defaultLogsBucketBehavior": t.string().optional(),
        }
    ).named(renames["BuildOptionsIn"])
    types["BuildOptionsOut"] = t.struct(
        {
            "secretEnv": t.array(t.string()).optional(),
            "dynamicSubstitutions": t.boolean().optional(),
            "workerPool": t.string().optional(),
            "substitutionOption": t.string().optional(),
            "logStreamingOption": t.string().optional(),
            "diskSizeGb": t.string().optional(),
            "requestedVerifyOption": t.string().optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "env": t.array(t.string()).optional(),
            "logging": t.string().optional(),
            "machineType": t.string().optional(),
            "pool": t.proxy(renames["PoolOptionOut"]).optional(),
            "sourceProvenanceHash": t.array(t.string()).optional(),
            "defaultLogsBucketBehavior": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOptionsOut"])
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
    types["ReceiveTriggerWebhookResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ReceiveTriggerWebhookResponseIn"])
    types["ReceiveTriggerWebhookResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReceiveTriggerWebhookResponseOut"])
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
    types["PoolOptionIn"] = t.struct({"name": t.string().optional()}).named(
        renames["PoolOptionIn"]
    )
    types["PoolOptionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoolOptionOut"])
    types["GitHubEventsConfigIn"] = t.struct(
        {
            "push": t.proxy(renames["PushFilterIn"]).optional(),
            "name": t.string().optional(),
            "owner": t.string().optional(),
            "enterpriseConfigResourceName": t.string().optional(),
            "installationId": t.string().optional(),
            "pullRequest": t.proxy(renames["PullRequestFilterIn"]).optional(),
        }
    ).named(renames["GitHubEventsConfigIn"])
    types["GitHubEventsConfigOut"] = t.struct(
        {
            "push": t.proxy(renames["PushFilterOut"]).optional(),
            "name": t.string().optional(),
            "owner": t.string().optional(),
            "enterpriseConfigResourceName": t.string().optional(),
            "installationId": t.string().optional(),
            "pullRequest": t.proxy(renames["PullRequestFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitHubEventsConfigOut"])
    types["GitLabRepositoryIdIn"] = t.struct({"id": t.string()}).named(
        renames["GitLabRepositoryIdIn"]
    )
    types["GitLabRepositoryIdOut"] = t.struct(
        {
            "webhookId": t.integer().optional(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitLabRepositoryIdOut"])
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
    types["BitbucketServerConfigIn"] = t.struct(
        {
            "apiKey": t.string(),
            "username": t.string().optional(),
            "name": t.string().optional(),
            "sslCa": t.string().optional(),
            "hostUri": t.string(),
            "createTime": t.string().optional(),
            "secrets": t.proxy(renames["BitbucketServerSecretsIn"]),
            "peeredNetwork": t.string().optional(),
        }
    ).named(renames["BitbucketServerConfigIn"])
    types["BitbucketServerConfigOut"] = t.struct(
        {
            "connectedRepositories": t.array(
                t.proxy(renames["BitbucketServerRepositoryIdOut"])
            ).optional(),
            "apiKey": t.string(),
            "username": t.string().optional(),
            "name": t.string().optional(),
            "webhookKey": t.string().optional(),
            "sslCa": t.string().optional(),
            "hostUri": t.string(),
            "createTime": t.string().optional(),
            "secrets": t.proxy(renames["BitbucketServerSecretsOut"]),
            "peeredNetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitbucketServerConfigOut"])
    types["ApprovalResultIn"] = t.struct(
        {
            "comment": t.string().optional(),
            "url": t.string().optional(),
            "decision": t.string(),
        }
    ).named(renames["ApprovalResultIn"])
    types["ApprovalResultOut"] = t.struct(
        {
            "approverAccount": t.string().optional(),
            "approvalTime": t.string().optional(),
            "comment": t.string().optional(),
            "url": t.string().optional(),
            "decision": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApprovalResultOut"])
    types["PubsubConfigIn"] = t.struct(
        {
            "state": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "topic": t.string().optional(),
        }
    ).named(renames["PubsubConfigIn"])
    types["PubsubConfigOut"] = t.struct(
        {
            "state": t.string().optional(),
            "subscription": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubConfigOut"])

    functions = {}
    functions["locationsRegionalWebhook"] = cloudbuild.post(
        "v1/{location}/regionalWebhook",
        t.struct(
            {
                "webhookKey": t.string().optional(),
                "location": t.string(),
                "data": t.string().optional(),
                "contentType": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
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
                "contentType": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
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
                "data": t.string().optional(),
                "contentType": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsLocationsBitbucketServerConfigsCreate"] = cloudbuild.delete(
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
    functions["projectsLocationsWorkerPoolsGet"] = cloudbuild.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
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
                "etag": t.string().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
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
                "etag": t.string().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
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
                "etag": t.string().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
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
                "etag": t.string().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsGet"] = cloudbuild.get(
        "v1/{parent}/builds",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "projectId": t.string(),
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
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "projectId": t.string(),
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
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBuildsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBuildsCreate"] = cloudbuild.get(
        "v1/{parent}/builds",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "projectId": t.string(),
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
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "projectId": t.string(),
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
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBuildsResponseOut"]),
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
    functions["projectsLocationsGithubEnterpriseConfigsList"] = cloudbuild.get(
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
    functions["projectsLocationsGithubEnterpriseConfigsDelete"] = cloudbuild.get(
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
    functions["projectsLocationsGithubEnterpriseConfigsPatch"] = cloudbuild.get(
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
    functions["projectsLocationsGithubEnterpriseConfigsCreate"] = cloudbuild.get(
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
    functions["projectsLocationsGithubEnterpriseConfigsGet"] = cloudbuild.get(
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
    functions["projectsLocationsTriggersRun"] = cloudbuild.post(
        "v1/{parent}/triggers",
        t.struct(
            {
                "projectId": t.string(),
                "parent": t.string().optional(),
                "filename": t.string().optional(),
                "build": t.proxy(renames["BuildIn"]).optional(),
                "sourceToBuild": t.proxy(renames["GitRepoSourceIn"]).optional(),
                "github": t.proxy(renames["GitHubEventsConfigIn"]).optional(),
                "triggerTemplate": t.proxy(renames["RepoSourceIn"]).optional(),
                "approvalConfig": t.proxy(renames["ApprovalConfigIn"]).optional(),
                "includedFiles": t.array(t.string()).optional(),
                "pubsubConfig": t.proxy(renames["PubsubConfigIn"]).optional(),
                "disabled": t.boolean().optional(),
                "gitFileSource": t.proxy(renames["GitFileSourceIn"]).optional(),
                "repositoryEventConfig": t.proxy(
                    renames["RepositoryEventConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "ignoredFiles": t.array(t.string()).optional(),
                "bitbucketServerTriggerConfig": t.proxy(
                    renames["BitbucketServerTriggerConfigIn"]
                ).optional(),
                "autodetect": t.boolean().optional(),
                "serviceAccount": t.string().optional(),
                "gitlabEnterpriseEventsConfig": t.proxy(
                    renames["GitLabEventsConfigIn"]
                ).optional(),
                "filter": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "eventType": t.string().optional(),
                "description": t.string().optional(),
                "includeBuildLogs": t.string().optional(),
                "webhookConfig": t.proxy(renames["WebhookConfigIn"]).optional(),
                "resourceName": t.string().optional(),
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
                "projectId": t.string(),
                "parent": t.string().optional(),
                "filename": t.string().optional(),
                "build": t.proxy(renames["BuildIn"]).optional(),
                "sourceToBuild": t.proxy(renames["GitRepoSourceIn"]).optional(),
                "github": t.proxy(renames["GitHubEventsConfigIn"]).optional(),
                "triggerTemplate": t.proxy(renames["RepoSourceIn"]).optional(),
                "approvalConfig": t.proxy(renames["ApprovalConfigIn"]).optional(),
                "includedFiles": t.array(t.string()).optional(),
                "pubsubConfig": t.proxy(renames["PubsubConfigIn"]).optional(),
                "disabled": t.boolean().optional(),
                "gitFileSource": t.proxy(renames["GitFileSourceIn"]).optional(),
                "repositoryEventConfig": t.proxy(
                    renames["RepositoryEventConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "ignoredFiles": t.array(t.string()).optional(),
                "bitbucketServerTriggerConfig": t.proxy(
                    renames["BitbucketServerTriggerConfigIn"]
                ).optional(),
                "autodetect": t.boolean().optional(),
                "serviceAccount": t.string().optional(),
                "gitlabEnterpriseEventsConfig": t.proxy(
                    renames["GitLabEventsConfigIn"]
                ).optional(),
                "filter": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "eventType": t.string().optional(),
                "description": t.string().optional(),
                "includeBuildLogs": t.string().optional(),
                "webhookConfig": t.proxy(renames["WebhookConfigIn"]).optional(),
                "resourceName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersWebhook"] = cloudbuild.post(
        "v1/{parent}/triggers",
        t.struct(
            {
                "projectId": t.string(),
                "parent": t.string().optional(),
                "filename": t.string().optional(),
                "build": t.proxy(renames["BuildIn"]).optional(),
                "sourceToBuild": t.proxy(renames["GitRepoSourceIn"]).optional(),
                "github": t.proxy(renames["GitHubEventsConfigIn"]).optional(),
                "triggerTemplate": t.proxy(renames["RepoSourceIn"]).optional(),
                "approvalConfig": t.proxy(renames["ApprovalConfigIn"]).optional(),
                "includedFiles": t.array(t.string()).optional(),
                "pubsubConfig": t.proxy(renames["PubsubConfigIn"]).optional(),
                "disabled": t.boolean().optional(),
                "gitFileSource": t.proxy(renames["GitFileSourceIn"]).optional(),
                "repositoryEventConfig": t.proxy(
                    renames["RepositoryEventConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "ignoredFiles": t.array(t.string()).optional(),
                "bitbucketServerTriggerConfig": t.proxy(
                    renames["BitbucketServerTriggerConfigIn"]
                ).optional(),
                "autodetect": t.boolean().optional(),
                "serviceAccount": t.string().optional(),
                "gitlabEnterpriseEventsConfig": t.proxy(
                    renames["GitLabEventsConfigIn"]
                ).optional(),
                "filter": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "eventType": t.string().optional(),
                "description": t.string().optional(),
                "includeBuildLogs": t.string().optional(),
                "webhookConfig": t.proxy(renames["WebhookConfigIn"]).optional(),
                "resourceName": t.string().optional(),
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
                "projectId": t.string(),
                "parent": t.string().optional(),
                "filename": t.string().optional(),
                "build": t.proxy(renames["BuildIn"]).optional(),
                "sourceToBuild": t.proxy(renames["GitRepoSourceIn"]).optional(),
                "github": t.proxy(renames["GitHubEventsConfigIn"]).optional(),
                "triggerTemplate": t.proxy(renames["RepoSourceIn"]).optional(),
                "approvalConfig": t.proxy(renames["ApprovalConfigIn"]).optional(),
                "includedFiles": t.array(t.string()).optional(),
                "pubsubConfig": t.proxy(renames["PubsubConfigIn"]).optional(),
                "disabled": t.boolean().optional(),
                "gitFileSource": t.proxy(renames["GitFileSourceIn"]).optional(),
                "repositoryEventConfig": t.proxy(
                    renames["RepositoryEventConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "ignoredFiles": t.array(t.string()).optional(),
                "bitbucketServerTriggerConfig": t.proxy(
                    renames["BitbucketServerTriggerConfigIn"]
                ).optional(),
                "autodetect": t.boolean().optional(),
                "serviceAccount": t.string().optional(),
                "gitlabEnterpriseEventsConfig": t.proxy(
                    renames["GitLabEventsConfigIn"]
                ).optional(),
                "filter": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "eventType": t.string().optional(),
                "description": t.string().optional(),
                "includeBuildLogs": t.string().optional(),
                "webhookConfig": t.proxy(renames["WebhookConfigIn"]).optional(),
                "resourceName": t.string().optional(),
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
                "projectId": t.string(),
                "parent": t.string().optional(),
                "filename": t.string().optional(),
                "build": t.proxy(renames["BuildIn"]).optional(),
                "sourceToBuild": t.proxy(renames["GitRepoSourceIn"]).optional(),
                "github": t.proxy(renames["GitHubEventsConfigIn"]).optional(),
                "triggerTemplate": t.proxy(renames["RepoSourceIn"]).optional(),
                "approvalConfig": t.proxy(renames["ApprovalConfigIn"]).optional(),
                "includedFiles": t.array(t.string()).optional(),
                "pubsubConfig": t.proxy(renames["PubsubConfigIn"]).optional(),
                "disabled": t.boolean().optional(),
                "gitFileSource": t.proxy(renames["GitFileSourceIn"]).optional(),
                "repositoryEventConfig": t.proxy(
                    renames["RepositoryEventConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "ignoredFiles": t.array(t.string()).optional(),
                "bitbucketServerTriggerConfig": t.proxy(
                    renames["BitbucketServerTriggerConfigIn"]
                ).optional(),
                "autodetect": t.boolean().optional(),
                "serviceAccount": t.string().optional(),
                "gitlabEnterpriseEventsConfig": t.proxy(
                    renames["GitLabEventsConfigIn"]
                ).optional(),
                "filter": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "eventType": t.string().optional(),
                "description": t.string().optional(),
                "includeBuildLogs": t.string().optional(),
                "webhookConfig": t.proxy(renames["WebhookConfigIn"]).optional(),
                "resourceName": t.string().optional(),
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
                "projectId": t.string(),
                "parent": t.string().optional(),
                "filename": t.string().optional(),
                "build": t.proxy(renames["BuildIn"]).optional(),
                "sourceToBuild": t.proxy(renames["GitRepoSourceIn"]).optional(),
                "github": t.proxy(renames["GitHubEventsConfigIn"]).optional(),
                "triggerTemplate": t.proxy(renames["RepoSourceIn"]).optional(),
                "approvalConfig": t.proxy(renames["ApprovalConfigIn"]).optional(),
                "includedFiles": t.array(t.string()).optional(),
                "pubsubConfig": t.proxy(renames["PubsubConfigIn"]).optional(),
                "disabled": t.boolean().optional(),
                "gitFileSource": t.proxy(renames["GitFileSourceIn"]).optional(),
                "repositoryEventConfig": t.proxy(
                    renames["RepositoryEventConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "ignoredFiles": t.array(t.string()).optional(),
                "bitbucketServerTriggerConfig": t.proxy(
                    renames["BitbucketServerTriggerConfigIn"]
                ).optional(),
                "autodetect": t.boolean().optional(),
                "serviceAccount": t.string().optional(),
                "gitlabEnterpriseEventsConfig": t.proxy(
                    renames["GitLabEventsConfigIn"]
                ).optional(),
                "filter": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "eventType": t.string().optional(),
                "description": t.string().optional(),
                "includeBuildLogs": t.string().optional(),
                "webhookConfig": t.proxy(renames["WebhookConfigIn"]).optional(),
                "resourceName": t.string().optional(),
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
                "projectId": t.string(),
                "parent": t.string().optional(),
                "filename": t.string().optional(),
                "build": t.proxy(renames["BuildIn"]).optional(),
                "sourceToBuild": t.proxy(renames["GitRepoSourceIn"]).optional(),
                "github": t.proxy(renames["GitHubEventsConfigIn"]).optional(),
                "triggerTemplate": t.proxy(renames["RepoSourceIn"]).optional(),
                "approvalConfig": t.proxy(renames["ApprovalConfigIn"]).optional(),
                "includedFiles": t.array(t.string()).optional(),
                "pubsubConfig": t.proxy(renames["PubsubConfigIn"]).optional(),
                "disabled": t.boolean().optional(),
                "gitFileSource": t.proxy(renames["GitFileSourceIn"]).optional(),
                "repositoryEventConfig": t.proxy(
                    renames["RepositoryEventConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "ignoredFiles": t.array(t.string()).optional(),
                "bitbucketServerTriggerConfig": t.proxy(
                    renames["BitbucketServerTriggerConfigIn"]
                ).optional(),
                "autodetect": t.boolean().optional(),
                "serviceAccount": t.string().optional(),
                "gitlabEnterpriseEventsConfig": t.proxy(
                    renames["GitLabEventsConfigIn"]
                ).optional(),
                "filter": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "eventType": t.string().optional(),
                "description": t.string().optional(),
                "includeBuildLogs": t.string().optional(),
                "webhookConfig": t.proxy(renames["WebhookConfigIn"]).optional(),
                "resourceName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersGet"] = cloudbuild.post(
        "v1/projects/{projectId}/triggers/{triggerId}:run",
        t.struct(
            {
                "triggerId": t.string(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "dir": t.string().optional(),
                "tagName": t.string().optional(),
                "branchName": t.string().optional(),
                "invertRegex": t.boolean().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "commitSha": t.string().optional(),
                "repoName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersDelete"] = cloudbuild.post(
        "v1/projects/{projectId}/triggers/{triggerId}:run",
        t.struct(
            {
                "triggerId": t.string(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "dir": t.string().optional(),
                "tagName": t.string().optional(),
                "branchName": t.string().optional(),
                "invertRegex": t.boolean().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "commitSha": t.string().optional(),
                "repoName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersPatch"] = cloudbuild.post(
        "v1/projects/{projectId}/triggers/{triggerId}:run",
        t.struct(
            {
                "triggerId": t.string(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "dir": t.string().optional(),
                "tagName": t.string().optional(),
                "branchName": t.string().optional(),
                "invertRegex": t.boolean().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "commitSha": t.string().optional(),
                "repoName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersCreate"] = cloudbuild.post(
        "v1/projects/{projectId}/triggers/{triggerId}:run",
        t.struct(
            {
                "triggerId": t.string(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "dir": t.string().optional(),
                "tagName": t.string().optional(),
                "branchName": t.string().optional(),
                "invertRegex": t.boolean().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "commitSha": t.string().optional(),
                "repoName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersWebhook"] = cloudbuild.post(
        "v1/projects/{projectId}/triggers/{triggerId}:run",
        t.struct(
            {
                "triggerId": t.string(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "dir": t.string().optional(),
                "tagName": t.string().optional(),
                "branchName": t.string().optional(),
                "invertRegex": t.boolean().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "commitSha": t.string().optional(),
                "repoName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersList"] = cloudbuild.post(
        "v1/projects/{projectId}/triggers/{triggerId}:run",
        t.struct(
            {
                "triggerId": t.string(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "dir": t.string().optional(),
                "tagName": t.string().optional(),
                "branchName": t.string().optional(),
                "invertRegex": t.boolean().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "commitSha": t.string().optional(),
                "repoName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTriggersRun"] = cloudbuild.post(
        "v1/projects/{projectId}/triggers/{triggerId}:run",
        t.struct(
            {
                "triggerId": t.string(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "dir": t.string().optional(),
                "tagName": t.string().optional(),
                "branchName": t.string().optional(),
                "invertRegex": t.boolean().optional(),
                "substitutions": t.struct({"_": t.string().optional()}).optional(),
                "commitSha": t.string().optional(),
                "repoName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsGet"] = cloudbuild.post(
        "v1/projects/{projectId}/builds/{id}:cancel",
        t.struct(
            {
                "projectId": t.string(),
                "id": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBuildsApprove"] = cloudbuild.post(
        "v1/projects/{projectId}/builds/{id}:cancel",
        t.struct(
            {
                "projectId": t.string(),
                "id": t.string(),
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
                "projectId": t.string(),
                "id": t.string(),
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
                "projectId": t.string(),
                "id": t.string(),
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
                "projectId": t.string(),
                "id": t.string(),
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
                "projectId": t.string(),
                "id": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuildOut"]),
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

    return Import(
        importer="cloudbuild",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
