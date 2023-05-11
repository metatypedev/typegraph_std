from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_artifactregistry() -> Import:
    artifactregistry = HTTPRuntime("https://artifactregistry.googleapis.com/")

    renames = {
        "ErrorResponse": "_artifactregistry_1_ErrorResponse",
        "StatusIn": "_artifactregistry_2_StatusIn",
        "StatusOut": "_artifactregistry_3_StatusOut",
        "MavenArtifactIn": "_artifactregistry_4_MavenArtifactIn",
        "MavenArtifactOut": "_artifactregistry_5_MavenArtifactOut",
        "ImportYumArtifactsMetadataIn": "_artifactregistry_6_ImportYumArtifactsMetadataIn",
        "ImportYumArtifactsMetadataOut": "_artifactregistry_7_ImportYumArtifactsMetadataOut",
        "ProjectSettingsIn": "_artifactregistry_8_ProjectSettingsIn",
        "ProjectSettingsOut": "_artifactregistry_9_ProjectSettingsOut",
        "GoogleDevtoolsArtifactregistryV1FileIn": "_artifactregistry_10_GoogleDevtoolsArtifactregistryV1FileIn",
        "GoogleDevtoolsArtifactregistryV1FileOut": "_artifactregistry_11_GoogleDevtoolsArtifactregistryV1FileOut",
        "DockerImageIn": "_artifactregistry_12_DockerImageIn",
        "DockerImageOut": "_artifactregistry_13_DockerImageOut",
        "UploadGoogetArtifactMediaResponseIn": "_artifactregistry_14_UploadGoogetArtifactMediaResponseIn",
        "UploadGoogetArtifactMediaResponseOut": "_artifactregistry_15_UploadGoogetArtifactMediaResponseOut",
        "UpstreamPolicyIn": "_artifactregistry_16_UpstreamPolicyIn",
        "UpstreamPolicyOut": "_artifactregistry_17_UpstreamPolicyOut",
        "ListNpmPackagesResponseIn": "_artifactregistry_18_ListNpmPackagesResponseIn",
        "ListNpmPackagesResponseOut": "_artifactregistry_19_ListNpmPackagesResponseOut",
        "UploadAptArtifactMetadataIn": "_artifactregistry_20_UploadAptArtifactMetadataIn",
        "UploadAptArtifactMetadataOut": "_artifactregistry_21_UploadAptArtifactMetadataOut",
        "UploadYumArtifactResponseIn": "_artifactregistry_22_UploadYumArtifactResponseIn",
        "UploadYumArtifactResponseOut": "_artifactregistry_23_UploadYumArtifactResponseOut",
        "ImportYumArtifactsRequestIn": "_artifactregistry_24_ImportYumArtifactsRequestIn",
        "ImportYumArtifactsRequestOut": "_artifactregistry_25_ImportYumArtifactsRequestOut",
        "ListTagsResponseIn": "_artifactregistry_26_ListTagsResponseIn",
        "ListTagsResponseOut": "_artifactregistry_27_ListTagsResponseOut",
        "PackageIn": "_artifactregistry_28_PackageIn",
        "PackageOut": "_artifactregistry_29_PackageOut",
        "NpmRepositoryIn": "_artifactregistry_30_NpmRepositoryIn",
        "NpmRepositoryOut": "_artifactregistry_31_NpmRepositoryOut",
        "ImportYumArtifactsErrorInfoIn": "_artifactregistry_32_ImportYumArtifactsErrorInfoIn",
        "ImportYumArtifactsErrorInfoOut": "_artifactregistry_33_ImportYumArtifactsErrorInfoOut",
        "GoogetArtifactIn": "_artifactregistry_34_GoogetArtifactIn",
        "GoogetArtifactOut": "_artifactregistry_35_GoogetArtifactOut",
        "ListVersionsResponseIn": "_artifactregistry_36_ListVersionsResponseIn",
        "ListVersionsResponseOut": "_artifactregistry_37_ListVersionsResponseOut",
        "ImportGoogetArtifactsErrorInfoIn": "_artifactregistry_38_ImportGoogetArtifactsErrorInfoIn",
        "ImportGoogetArtifactsErrorInfoOut": "_artifactregistry_39_ImportGoogetArtifactsErrorInfoOut",
        "ListFilesResponseIn": "_artifactregistry_40_ListFilesResponseIn",
        "ListFilesResponseOut": "_artifactregistry_41_ListFilesResponseOut",
        "OperationIn": "_artifactregistry_42_OperationIn",
        "OperationOut": "_artifactregistry_43_OperationOut",
        "ImportAptArtifactsErrorInfoIn": "_artifactregistry_44_ImportAptArtifactsErrorInfoIn",
        "ImportAptArtifactsErrorInfoOut": "_artifactregistry_45_ImportAptArtifactsErrorInfoOut",
        "ImportAptArtifactsGcsSourceIn": "_artifactregistry_46_ImportAptArtifactsGcsSourceIn",
        "ImportAptArtifactsGcsSourceOut": "_artifactregistry_47_ImportAptArtifactsGcsSourceOut",
        "ImportYumArtifactsResponseIn": "_artifactregistry_48_ImportYumArtifactsResponseIn",
        "ImportYumArtifactsResponseOut": "_artifactregistry_49_ImportYumArtifactsResponseOut",
        "OperationMetadataIn": "_artifactregistry_50_OperationMetadataIn",
        "OperationMetadataOut": "_artifactregistry_51_OperationMetadataOut",
        "ImportAptArtifactsResponseIn": "_artifactregistry_52_ImportAptArtifactsResponseIn",
        "ImportAptArtifactsResponseOut": "_artifactregistry_53_ImportAptArtifactsResponseOut",
        "RepositoryIn": "_artifactregistry_54_RepositoryIn",
        "RepositoryOut": "_artifactregistry_55_RepositoryOut",
        "ImportAptArtifactsMetadataIn": "_artifactregistry_56_ImportAptArtifactsMetadataIn",
        "ImportAptArtifactsMetadataOut": "_artifactregistry_57_ImportAptArtifactsMetadataOut",
        "UploadYumArtifactMediaResponseIn": "_artifactregistry_58_UploadYumArtifactMediaResponseIn",
        "UploadYumArtifactMediaResponseOut": "_artifactregistry_59_UploadYumArtifactMediaResponseOut",
        "ImportGoogetArtifactsGcsSourceIn": "_artifactregistry_60_ImportGoogetArtifactsGcsSourceIn",
        "ImportGoogetArtifactsGcsSourceOut": "_artifactregistry_61_ImportGoogetArtifactsGcsSourceOut",
        "BatchDeleteVersionsMetadataIn": "_artifactregistry_62_BatchDeleteVersionsMetadataIn",
        "BatchDeleteVersionsMetadataOut": "_artifactregistry_63_BatchDeleteVersionsMetadataOut",
        "UploadKfpArtifactRequestIn": "_artifactregistry_64_UploadKfpArtifactRequestIn",
        "UploadKfpArtifactRequestOut": "_artifactregistry_65_UploadKfpArtifactRequestOut",
        "TestIamPermissionsRequestIn": "_artifactregistry_66_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_artifactregistry_67_TestIamPermissionsRequestOut",
        "BindingIn": "_artifactregistry_68_BindingIn",
        "BindingOut": "_artifactregistry_69_BindingOut",
        "UploadYumArtifactRequestIn": "_artifactregistry_70_UploadYumArtifactRequestIn",
        "UploadYumArtifactRequestOut": "_artifactregistry_71_UploadYumArtifactRequestOut",
        "ListLocationsResponseIn": "_artifactregistry_72_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_artifactregistry_73_ListLocationsResponseOut",
        "UploadAptArtifactResponseIn": "_artifactregistry_74_UploadAptArtifactResponseIn",
        "UploadAptArtifactResponseOut": "_artifactregistry_75_UploadAptArtifactResponseOut",
        "KfpArtifactIn": "_artifactregistry_76_KfpArtifactIn",
        "KfpArtifactOut": "_artifactregistry_77_KfpArtifactOut",
        "DockerRepositoryConfigIn": "_artifactregistry_78_DockerRepositoryConfigIn",
        "DockerRepositoryConfigOut": "_artifactregistry_79_DockerRepositoryConfigOut",
        "NpmPackageIn": "_artifactregistry_80_NpmPackageIn",
        "NpmPackageOut": "_artifactregistry_81_NpmPackageOut",
        "ListMavenArtifactsResponseIn": "_artifactregistry_82_ListMavenArtifactsResponseIn",
        "ListMavenArtifactsResponseOut": "_artifactregistry_83_ListMavenArtifactsResponseOut",
        "VPCSCConfigIn": "_artifactregistry_84_VPCSCConfigIn",
        "VPCSCConfigOut": "_artifactregistry_85_VPCSCConfigOut",
        "PythonRepositoryIn": "_artifactregistry_86_PythonRepositoryIn",
        "PythonRepositoryOut": "_artifactregistry_87_PythonRepositoryOut",
        "UploadYumArtifactMetadataIn": "_artifactregistry_88_UploadYumArtifactMetadataIn",
        "UploadYumArtifactMetadataOut": "_artifactregistry_89_UploadYumArtifactMetadataOut",
        "ListDockerImagesResponseIn": "_artifactregistry_90_ListDockerImagesResponseIn",
        "ListDockerImagesResponseOut": "_artifactregistry_91_ListDockerImagesResponseOut",
        "UploadGoogetArtifactMetadataIn": "_artifactregistry_92_UploadGoogetArtifactMetadataIn",
        "UploadGoogetArtifactMetadataOut": "_artifactregistry_93_UploadGoogetArtifactMetadataOut",
        "ImportYumArtifactsGcsSourceIn": "_artifactregistry_94_ImportYumArtifactsGcsSourceIn",
        "ImportYumArtifactsGcsSourceOut": "_artifactregistry_95_ImportYumArtifactsGcsSourceOut",
        "ImportGoogetArtifactsResponseIn": "_artifactregistry_96_ImportGoogetArtifactsResponseIn",
        "ImportGoogetArtifactsResponseOut": "_artifactregistry_97_ImportGoogetArtifactsResponseOut",
        "UploadKfpArtifactMetadataIn": "_artifactregistry_98_UploadKfpArtifactMetadataIn",
        "UploadKfpArtifactMetadataOut": "_artifactregistry_99_UploadKfpArtifactMetadataOut",
        "MavenRepositoryConfigIn": "_artifactregistry_100_MavenRepositoryConfigIn",
        "MavenRepositoryConfigOut": "_artifactregistry_101_MavenRepositoryConfigOut",
        "UploadGoogetArtifactResponseIn": "_artifactregistry_102_UploadGoogetArtifactResponseIn",
        "UploadGoogetArtifactResponseOut": "_artifactregistry_103_UploadGoogetArtifactResponseOut",
        "ListPythonPackagesResponseIn": "_artifactregistry_104_ListPythonPackagesResponseIn",
        "ListPythonPackagesResponseOut": "_artifactregistry_105_ListPythonPackagesResponseOut",
        "TagIn": "_artifactregistry_106_TagIn",
        "TagOut": "_artifactregistry_107_TagOut",
        "ImportGoogetArtifactsMetadataIn": "_artifactregistry_108_ImportGoogetArtifactsMetadataIn",
        "ImportGoogetArtifactsMetadataOut": "_artifactregistry_109_ImportGoogetArtifactsMetadataOut",
        "LocationIn": "_artifactregistry_110_LocationIn",
        "LocationOut": "_artifactregistry_111_LocationOut",
        "VersionIn": "_artifactregistry_112_VersionIn",
        "VersionOut": "_artifactregistry_113_VersionOut",
        "HashIn": "_artifactregistry_114_HashIn",
        "HashOut": "_artifactregistry_115_HashOut",
        "PythonPackageIn": "_artifactregistry_116_PythonPackageIn",
        "PythonPackageOut": "_artifactregistry_117_PythonPackageOut",
        "DockerRepositoryIn": "_artifactregistry_118_DockerRepositoryIn",
        "DockerRepositoryOut": "_artifactregistry_119_DockerRepositoryOut",
        "ListRepositoriesResponseIn": "_artifactregistry_120_ListRepositoriesResponseIn",
        "ListRepositoriesResponseOut": "_artifactregistry_121_ListRepositoriesResponseOut",
        "UploadKfpArtifactMediaResponseIn": "_artifactregistry_122_UploadKfpArtifactMediaResponseIn",
        "UploadKfpArtifactMediaResponseOut": "_artifactregistry_123_UploadKfpArtifactMediaResponseOut",
        "UploadGoogetArtifactRequestIn": "_artifactregistry_124_UploadGoogetArtifactRequestIn",
        "UploadGoogetArtifactRequestOut": "_artifactregistry_125_UploadGoogetArtifactRequestOut",
        "ImportGoogetArtifactsRequestIn": "_artifactregistry_126_ImportGoogetArtifactsRequestIn",
        "ImportGoogetArtifactsRequestOut": "_artifactregistry_127_ImportGoogetArtifactsRequestOut",
        "YumArtifactIn": "_artifactregistry_128_YumArtifactIn",
        "YumArtifactOut": "_artifactregistry_129_YumArtifactOut",
        "MavenRepositoryIn": "_artifactregistry_130_MavenRepositoryIn",
        "MavenRepositoryOut": "_artifactregistry_131_MavenRepositoryOut",
        "VirtualRepositoryConfigIn": "_artifactregistry_132_VirtualRepositoryConfigIn",
        "VirtualRepositoryConfigOut": "_artifactregistry_133_VirtualRepositoryConfigOut",
        "EmptyIn": "_artifactregistry_134_EmptyIn",
        "EmptyOut": "_artifactregistry_135_EmptyOut",
        "ExprIn": "_artifactregistry_136_ExprIn",
        "ExprOut": "_artifactregistry_137_ExprOut",
        "RemoteRepositoryConfigIn": "_artifactregistry_138_RemoteRepositoryConfigIn",
        "RemoteRepositoryConfigOut": "_artifactregistry_139_RemoteRepositoryConfigOut",
        "PolicyIn": "_artifactregistry_140_PolicyIn",
        "PolicyOut": "_artifactregistry_141_PolicyOut",
        "AptArtifactIn": "_artifactregistry_142_AptArtifactIn",
        "AptArtifactOut": "_artifactregistry_143_AptArtifactOut",
        "ListPackagesResponseIn": "_artifactregistry_144_ListPackagesResponseIn",
        "ListPackagesResponseOut": "_artifactregistry_145_ListPackagesResponseOut",
        "UploadAptArtifactMediaResponseIn": "_artifactregistry_146_UploadAptArtifactMediaResponseIn",
        "UploadAptArtifactMediaResponseOut": "_artifactregistry_147_UploadAptArtifactMediaResponseOut",
        "UploadAptArtifactRequestIn": "_artifactregistry_148_UploadAptArtifactRequestIn",
        "UploadAptArtifactRequestOut": "_artifactregistry_149_UploadAptArtifactRequestOut",
        "SetIamPolicyRequestIn": "_artifactregistry_150_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_artifactregistry_151_SetIamPolicyRequestOut",
        "TestIamPermissionsResponseIn": "_artifactregistry_152_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_artifactregistry_153_TestIamPermissionsResponseOut",
        "ImportAptArtifactsRequestIn": "_artifactregistry_154_ImportAptArtifactsRequestIn",
        "ImportAptArtifactsRequestOut": "_artifactregistry_155_ImportAptArtifactsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["MavenArtifactIn"] = t.struct(
        {
            "groupId": t.string().optional(),
            "pomUri": t.string(),
            "version": t.string().optional(),
            "name": t.string(),
            "artifactId": t.string().optional(),
        }
    ).named(renames["MavenArtifactIn"])
    types["MavenArtifactOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "groupId": t.string().optional(),
            "pomUri": t.string(),
            "version": t.string().optional(),
            "name": t.string(),
            "artifactId": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MavenArtifactOut"])
    types["ImportYumArtifactsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportYumArtifactsMetadataIn"])
    types["ImportYumArtifactsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportYumArtifactsMetadataOut"])
    types["ProjectSettingsIn"] = t.struct(
        {"name": t.string().optional(), "legacyRedirectionState": t.string().optional()}
    ).named(renames["ProjectSettingsIn"])
    types["ProjectSettingsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "legacyRedirectionState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectSettingsOut"])
    types["GoogleDevtoolsArtifactregistryV1FileIn"] = t.struct(
        {
            "sizeBytes": t.string().optional(),
            "hashes": t.array(t.proxy(renames["HashIn"])).optional(),
            "owner": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleDevtoolsArtifactregistryV1FileIn"])
    types["GoogleDevtoolsArtifactregistryV1FileOut"] = t.struct(
        {
            "sizeBytes": t.string().optional(),
            "hashes": t.array(t.proxy(renames["HashOut"])).optional(),
            "updateTime": t.string().optional(),
            "fetchTime": t.string().optional(),
            "createTime": t.string().optional(),
            "owner": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDevtoolsArtifactregistryV1FileOut"])
    types["DockerImageIn"] = t.struct(
        {
            "uploadTime": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "mediaType": t.string().optional(),
            "buildTime": t.string().optional(),
            "name": t.string(),
            "imageSizeBytes": t.string().optional(),
            "uri": t.string(),
        }
    ).named(renames["DockerImageIn"])
    types["DockerImageOut"] = t.struct(
        {
            "uploadTime": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "mediaType": t.string().optional(),
            "buildTime": t.string().optional(),
            "name": t.string(),
            "updateTime": t.string().optional(),
            "imageSizeBytes": t.string().optional(),
            "uri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DockerImageOut"])
    types["UploadGoogetArtifactMediaResponseIn"] = t.struct(
        {"operation": t.proxy(renames["OperationIn"]).optional()}
    ).named(renames["UploadGoogetArtifactMediaResponseIn"])
    types["UploadGoogetArtifactMediaResponseOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadGoogetArtifactMediaResponseOut"])
    types["UpstreamPolicyIn"] = t.struct(
        {
            "priority": t.integer().optional(),
            "repository": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["UpstreamPolicyIn"])
    types["UpstreamPolicyOut"] = t.struct(
        {
            "priority": t.integer().optional(),
            "repository": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpstreamPolicyOut"])
    types["ListNpmPackagesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "npmPackages": t.array(t.proxy(renames["NpmPackageIn"])).optional(),
        }
    ).named(renames["ListNpmPackagesResponseIn"])
    types["ListNpmPackagesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "npmPackages": t.array(t.proxy(renames["NpmPackageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNpmPackagesResponseOut"])
    types["UploadAptArtifactMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadAptArtifactMetadataIn"]
    )
    types["UploadAptArtifactMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadAptArtifactMetadataOut"])
    types["UploadYumArtifactResponseIn"] = t.struct(
        {"yumArtifacts": t.array(t.proxy(renames["YumArtifactIn"])).optional()}
    ).named(renames["UploadYumArtifactResponseIn"])
    types["UploadYumArtifactResponseOut"] = t.struct(
        {
            "yumArtifacts": t.array(t.proxy(renames["YumArtifactOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadYumArtifactResponseOut"])
    types["ImportYumArtifactsRequestIn"] = t.struct(
        {"gcsSource": t.proxy(renames["ImportYumArtifactsGcsSourceIn"]).optional()}
    ).named(renames["ImportYumArtifactsRequestIn"])
    types["ImportYumArtifactsRequestOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["ImportYumArtifactsGcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportYumArtifactsRequestOut"])
    types["ListTagsResponseIn"] = t.struct(
        {
            "tags": t.array(t.proxy(renames["TagIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTagsResponseIn"])
    types["ListTagsResponseOut"] = t.struct(
        {
            "tags": t.array(t.proxy(renames["TagOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTagsResponseOut"])
    types["PackageIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["PackageIn"])
    types["PackageOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageOut"])
    types["NpmRepositoryIn"] = t.struct(
        {"publicRepository": t.string().optional()}
    ).named(renames["NpmRepositoryIn"])
    types["NpmRepositoryOut"] = t.struct(
        {
            "publicRepository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NpmRepositoryOut"])
    types["ImportYumArtifactsErrorInfoIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "gcsSource": t.proxy(renames["ImportYumArtifactsGcsSourceIn"]).optional(),
        }
    ).named(renames["ImportYumArtifactsErrorInfoIn"])
    types["ImportYumArtifactsErrorInfoOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "gcsSource": t.proxy(renames["ImportYumArtifactsGcsSourceOut"]).optional(),
        }
    ).named(renames["ImportYumArtifactsErrorInfoOut"])
    types["GoogetArtifactIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogetArtifactIn"]
    )
    types["GoogetArtifactOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "architecture": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogetArtifactOut"])
    types["ListVersionsResponseIn"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["VersionIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListVersionsResponseIn"])
    types["ListVersionsResponseOut"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["VersionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVersionsResponseOut"])
    types["ImportGoogetArtifactsErrorInfoIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "gcsSource": t.proxy(
                renames["ImportGoogetArtifactsGcsSourceIn"]
            ).optional(),
        }
    ).named(renames["ImportGoogetArtifactsErrorInfoIn"])
    types["ImportGoogetArtifactsErrorInfoOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "gcsSource": t.proxy(
                renames["ImportGoogetArtifactsGcsSourceOut"]
            ).optional(),
        }
    ).named(renames["ImportGoogetArtifactsErrorInfoOut"])
    types["ListFilesResponseIn"] = t.struct(
        {
            "files": t.array(
                t.proxy(renames["GoogleDevtoolsArtifactregistryV1FileIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListFilesResponseIn"])
    types["ListFilesResponseOut"] = t.struct(
        {
            "files": t.array(
                t.proxy(renames["GoogleDevtoolsArtifactregistryV1FileOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFilesResponseOut"])
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
    types["ImportAptArtifactsErrorInfoIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "gcsSource": t.proxy(renames["ImportAptArtifactsGcsSourceIn"]).optional(),
        }
    ).named(renames["ImportAptArtifactsErrorInfoIn"])
    types["ImportAptArtifactsErrorInfoOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "gcsSource": t.proxy(renames["ImportAptArtifactsGcsSourceOut"]).optional(),
        }
    ).named(renames["ImportAptArtifactsErrorInfoOut"])
    types["ImportAptArtifactsGcsSourceIn"] = t.struct(
        {"uris": t.array(t.string()).optional(), "useWildcards": t.boolean().optional()}
    ).named(renames["ImportAptArtifactsGcsSourceIn"])
    types["ImportAptArtifactsGcsSourceOut"] = t.struct(
        {
            "uris": t.array(t.string()).optional(),
            "useWildcards": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportAptArtifactsGcsSourceOut"])
    types["ImportYumArtifactsResponseIn"] = t.struct(
        {
            "yumArtifacts": t.array(t.proxy(renames["YumArtifactIn"])).optional(),
            "errors": t.array(
                t.proxy(renames["ImportYumArtifactsErrorInfoIn"])
            ).optional(),
        }
    ).named(renames["ImportYumArtifactsResponseIn"])
    types["ImportYumArtifactsResponseOut"] = t.struct(
        {
            "yumArtifacts": t.array(t.proxy(renames["YumArtifactOut"])).optional(),
            "errors": t.array(
                t.proxy(renames["ImportYumArtifactsErrorInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportYumArtifactsResponseOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OperationMetadataOut"])
    types["ImportAptArtifactsResponseIn"] = t.struct(
        {
            "aptArtifacts": t.array(t.proxy(renames["AptArtifactIn"])).optional(),
            "errors": t.array(
                t.proxy(renames["ImportAptArtifactsErrorInfoIn"])
            ).optional(),
        }
    ).named(renames["ImportAptArtifactsResponseIn"])
    types["ImportAptArtifactsResponseOut"] = t.struct(
        {
            "aptArtifacts": t.array(t.proxy(renames["AptArtifactOut"])).optional(),
            "errors": t.array(
                t.proxy(renames["ImportAptArtifactsErrorInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportAptArtifactsResponseOut"])
    types["RepositoryIn"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "mavenConfig": t.proxy(renames["MavenRepositoryConfigIn"]).optional(),
            "kmsKeyName": t.string().optional(),
            "dockerConfig": t.proxy(renames["DockerRepositoryConfigIn"]).optional(),
            "mode": t.string().optional(),
            "format": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "remoteRepositoryConfig": t.proxy(
                renames["RemoteRepositoryConfigIn"]
            ).optional(),
            "virtualRepositoryConfig": t.proxy(
                renames["VirtualRepositoryConfigIn"]
            ).optional(),
        }
    ).named(renames["RepositoryIn"])
    types["RepositoryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "mavenConfig": t.proxy(renames["MavenRepositoryConfigOut"]).optional(),
            "kmsKeyName": t.string().optional(),
            "dockerConfig": t.proxy(renames["DockerRepositoryConfigOut"]).optional(),
            "mode": t.string().optional(),
            "updateTime": t.string().optional(),
            "format": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "remoteRepositoryConfig": t.proxy(
                renames["RemoteRepositoryConfigOut"]
            ).optional(),
            "virtualRepositoryConfig": t.proxy(
                renames["VirtualRepositoryConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepositoryOut"])
    types["ImportAptArtifactsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportAptArtifactsMetadataIn"])
    types["ImportAptArtifactsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportAptArtifactsMetadataOut"])
    types["UploadYumArtifactMediaResponseIn"] = t.struct(
        {"operation": t.proxy(renames["OperationIn"]).optional()}
    ).named(renames["UploadYumArtifactMediaResponseIn"])
    types["UploadYumArtifactMediaResponseOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadYumArtifactMediaResponseOut"])
    types["ImportGoogetArtifactsGcsSourceIn"] = t.struct(
        {"uris": t.array(t.string()).optional(), "useWildcards": t.boolean().optional()}
    ).named(renames["ImportGoogetArtifactsGcsSourceIn"])
    types["ImportGoogetArtifactsGcsSourceOut"] = t.struct(
        {
            "uris": t.array(t.string()).optional(),
            "useWildcards": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportGoogetArtifactsGcsSourceOut"])
    types["BatchDeleteVersionsMetadataIn"] = t.struct(
        {"failedVersions": t.array(t.string()).optional()}
    ).named(renames["BatchDeleteVersionsMetadataIn"])
    types["BatchDeleteVersionsMetadataOut"] = t.struct(
        {
            "failedVersions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteVersionsMetadataOut"])
    types["UploadKfpArtifactRequestIn"] = t.struct(
        {"description": t.string().optional(), "tags": t.array(t.string()).optional()}
    ).named(renames["UploadKfpArtifactRequestIn"])
    types["UploadKfpArtifactRequestOut"] = t.struct(
        {
            "description": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadKfpArtifactRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["UploadYumArtifactRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadYumArtifactRequestIn"]
    )
    types["UploadYumArtifactRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadYumArtifactRequestOut"])
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
    types["UploadAptArtifactResponseIn"] = t.struct(
        {"aptArtifacts": t.array(t.proxy(renames["AptArtifactIn"])).optional()}
    ).named(renames["UploadAptArtifactResponseIn"])
    types["UploadAptArtifactResponseOut"] = t.struct(
        {
            "aptArtifacts": t.array(t.proxy(renames["AptArtifactOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadAptArtifactResponseOut"])
    types["KfpArtifactIn"] = t.struct({"version": t.string().optional()}).named(
        renames["KfpArtifactIn"]
    )
    types["KfpArtifactOut"] = t.struct(
        {
            "version": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KfpArtifactOut"])
    types["DockerRepositoryConfigIn"] = t.struct(
        {"immutableTags": t.boolean().optional()}
    ).named(renames["DockerRepositoryConfigIn"])
    types["DockerRepositoryConfigOut"] = t.struct(
        {
            "immutableTags": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DockerRepositoryConfigOut"])
    types["NpmPackageIn"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "version": t.string().optional(),
            "name": t.string(),
            "packageName": t.string().optional(),
        }
    ).named(renames["NpmPackageIn"])
    types["NpmPackageOut"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "version": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string(),
            "updateTime": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NpmPackageOut"])
    types["ListMavenArtifactsResponseIn"] = t.struct(
        {
            "mavenArtifacts": t.array(t.proxy(renames["MavenArtifactIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListMavenArtifactsResponseIn"])
    types["ListMavenArtifactsResponseOut"] = t.struct(
        {
            "mavenArtifacts": t.array(t.proxy(renames["MavenArtifactOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMavenArtifactsResponseOut"])
    types["VPCSCConfigIn"] = t.struct(
        {"vpcscPolicy": t.string().optional(), "name": t.string().optional()}
    ).named(renames["VPCSCConfigIn"])
    types["VPCSCConfigOut"] = t.struct(
        {
            "vpcscPolicy": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VPCSCConfigOut"])
    types["PythonRepositoryIn"] = t.struct(
        {"publicRepository": t.string().optional()}
    ).named(renames["PythonRepositoryIn"])
    types["PythonRepositoryOut"] = t.struct(
        {
            "publicRepository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonRepositoryOut"])
    types["UploadYumArtifactMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadYumArtifactMetadataIn"]
    )
    types["UploadYumArtifactMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadYumArtifactMetadataOut"])
    types["ListDockerImagesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dockerImages": t.array(t.proxy(renames["DockerImageIn"])).optional(),
        }
    ).named(renames["ListDockerImagesResponseIn"])
    types["ListDockerImagesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dockerImages": t.array(t.proxy(renames["DockerImageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDockerImagesResponseOut"])
    types["UploadGoogetArtifactMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UploadGoogetArtifactMetadataIn"])
    types["UploadGoogetArtifactMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadGoogetArtifactMetadataOut"])
    types["ImportYumArtifactsGcsSourceIn"] = t.struct(
        {"uris": t.array(t.string()).optional(), "useWildcards": t.boolean().optional()}
    ).named(renames["ImportYumArtifactsGcsSourceIn"])
    types["ImportYumArtifactsGcsSourceOut"] = t.struct(
        {
            "uris": t.array(t.string()).optional(),
            "useWildcards": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportYumArtifactsGcsSourceOut"])
    types["ImportGoogetArtifactsResponseIn"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["ImportGoogetArtifactsErrorInfoIn"])
            ).optional(),
            "googetArtifacts": t.array(t.proxy(renames["GoogetArtifactIn"])).optional(),
        }
    ).named(renames["ImportGoogetArtifactsResponseIn"])
    types["ImportGoogetArtifactsResponseOut"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["ImportGoogetArtifactsErrorInfoOut"])
            ).optional(),
            "googetArtifacts": t.array(
                t.proxy(renames["GoogetArtifactOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportGoogetArtifactsResponseOut"])
    types["UploadKfpArtifactMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadKfpArtifactMetadataIn"]
    )
    types["UploadKfpArtifactMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadKfpArtifactMetadataOut"])
    types["MavenRepositoryConfigIn"] = t.struct(
        {
            "versionPolicy": t.string().optional(),
            "allowSnapshotOverwrites": t.boolean().optional(),
        }
    ).named(renames["MavenRepositoryConfigIn"])
    types["MavenRepositoryConfigOut"] = t.struct(
        {
            "versionPolicy": t.string().optional(),
            "allowSnapshotOverwrites": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MavenRepositoryConfigOut"])
    types["UploadGoogetArtifactResponseIn"] = t.struct(
        {"googetArtifacts": t.array(t.proxy(renames["GoogetArtifactIn"])).optional()}
    ).named(renames["UploadGoogetArtifactResponseIn"])
    types["UploadGoogetArtifactResponseOut"] = t.struct(
        {
            "googetArtifacts": t.array(
                t.proxy(renames["GoogetArtifactOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadGoogetArtifactResponseOut"])
    types["ListPythonPackagesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "pythonPackages": t.array(t.proxy(renames["PythonPackageIn"])).optional(),
        }
    ).named(renames["ListPythonPackagesResponseIn"])
    types["ListPythonPackagesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "pythonPackages": t.array(t.proxy(renames["PythonPackageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPythonPackagesResponseOut"])
    types["TagIn"] = t.struct(
        {"version": t.string().optional(), "name": t.string().optional()}
    ).named(renames["TagIn"])
    types["TagOut"] = t.struct(
        {
            "version": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagOut"])
    types["ImportGoogetArtifactsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportGoogetArtifactsMetadataIn"])
    types["ImportGoogetArtifactsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportGoogetArtifactsMetadataOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["VersionIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "relatedTags": t.array(t.proxy(renames["TagIn"])).optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "relatedTags": t.array(t.proxy(renames["TagOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
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
    types["PythonPackageIn"] = t.struct(
        {
            "packageName": t.string().optional(),
            "name": t.string(),
            "version": t.string().optional(),
            "uri": t.string(),
        }
    ).named(renames["PythonPackageIn"])
    types["PythonPackageOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "packageName": t.string().optional(),
            "name": t.string(),
            "createTime": t.string().optional(),
            "version": t.string().optional(),
            "uri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonPackageOut"])
    types["DockerRepositoryIn"] = t.struct(
        {"publicRepository": t.string().optional()}
    ).named(renames["DockerRepositoryIn"])
    types["DockerRepositoryOut"] = t.struct(
        {
            "publicRepository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DockerRepositoryOut"])
    types["ListRepositoriesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "repositories": t.array(t.proxy(renames["RepositoryIn"])).optional(),
        }
    ).named(renames["ListRepositoriesResponseIn"])
    types["ListRepositoriesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "repositories": t.array(t.proxy(renames["RepositoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRepositoriesResponseOut"])
    types["UploadKfpArtifactMediaResponseIn"] = t.struct(
        {"operation": t.proxy(renames["OperationIn"]).optional()}
    ).named(renames["UploadKfpArtifactMediaResponseIn"])
    types["UploadKfpArtifactMediaResponseOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadKfpArtifactMediaResponseOut"])
    types["UploadGoogetArtifactRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UploadGoogetArtifactRequestIn"])
    types["UploadGoogetArtifactRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadGoogetArtifactRequestOut"])
    types["ImportGoogetArtifactsRequestIn"] = t.struct(
        {"gcsSource": t.proxy(renames["ImportGoogetArtifactsGcsSourceIn"]).optional()}
    ).named(renames["ImportGoogetArtifactsRequestIn"])
    types["ImportGoogetArtifactsRequestOut"] = t.struct(
        {
            "gcsSource": t.proxy(
                renames["ImportGoogetArtifactsGcsSourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportGoogetArtifactsRequestOut"])
    types["YumArtifactIn"] = t.struct({"_": t.string().optional()}).named(
        renames["YumArtifactIn"]
    )
    types["YumArtifactOut"] = t.struct(
        {
            "packageType": t.string().optional(),
            "name": t.string().optional(),
            "packageName": t.string().optional(),
            "architecture": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YumArtifactOut"])
    types["MavenRepositoryIn"] = t.struct(
        {"publicRepository": t.string().optional()}
    ).named(renames["MavenRepositoryIn"])
    types["MavenRepositoryOut"] = t.struct(
        {
            "publicRepository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MavenRepositoryOut"])
    types["VirtualRepositoryConfigIn"] = t.struct(
        {"upstreamPolicies": t.array(t.proxy(renames["UpstreamPolicyIn"])).optional()}
    ).named(renames["VirtualRepositoryConfigIn"])
    types["VirtualRepositoryConfigOut"] = t.struct(
        {
            "upstreamPolicies": t.array(
                t.proxy(renames["UpstreamPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualRepositoryConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["RemoteRepositoryConfigIn"] = t.struct(
        {
            "npmRepository": t.proxy(renames["NpmRepositoryIn"]).optional(),
            "description": t.string().optional(),
            "pythonRepository": t.proxy(renames["PythonRepositoryIn"]).optional(),
            "mavenRepository": t.proxy(renames["MavenRepositoryIn"]).optional(),
            "dockerRepository": t.proxy(renames["DockerRepositoryIn"]).optional(),
        }
    ).named(renames["RemoteRepositoryConfigIn"])
    types["RemoteRepositoryConfigOut"] = t.struct(
        {
            "npmRepository": t.proxy(renames["NpmRepositoryOut"]).optional(),
            "description": t.string().optional(),
            "pythonRepository": t.proxy(renames["PythonRepositoryOut"]).optional(),
            "mavenRepository": t.proxy(renames["MavenRepositoryOut"]).optional(),
            "dockerRepository": t.proxy(renames["DockerRepositoryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoteRepositoryConfigOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["AptArtifactIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AptArtifactIn"]
    )
    types["AptArtifactOut"] = t.struct(
        {
            "component": t.string().optional(),
            "packageName": t.string().optional(),
            "controlFile": t.string().optional(),
            "packageType": t.string().optional(),
            "architecture": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AptArtifactOut"])
    types["ListPackagesResponseIn"] = t.struct(
        {
            "packages": t.array(t.proxy(renames["PackageIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPackagesResponseIn"])
    types["ListPackagesResponseOut"] = t.struct(
        {
            "packages": t.array(t.proxy(renames["PackageOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPackagesResponseOut"])
    types["UploadAptArtifactMediaResponseIn"] = t.struct(
        {"operation": t.proxy(renames["OperationIn"]).optional()}
    ).named(renames["UploadAptArtifactMediaResponseIn"])
    types["UploadAptArtifactMediaResponseOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadAptArtifactMediaResponseOut"])
    types["UploadAptArtifactRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadAptArtifactRequestIn"]
    )
    types["UploadAptArtifactRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadAptArtifactRequestOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ImportAptArtifactsRequestIn"] = t.struct(
        {"gcsSource": t.proxy(renames["ImportAptArtifactsGcsSourceIn"]).optional()}
    ).named(renames["ImportAptArtifactsRequestIn"])
    types["ImportAptArtifactsRequestOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["ImportAptArtifactsGcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportAptArtifactsRequestOut"])

    functions = {}
    functions["projectsGetProjectSettings"] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "legacyRedirectionState": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUpdateProjectSettings"] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "legacyRedirectionState": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGetVpcscConfig"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUpdateVpcscConfig"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesDelete"] = artifactregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesList"] = artifactregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesCreate"] = artifactregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesGet"] = artifactregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesTestIamPermissions"] = artifactregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesPatch"] = artifactregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesSetIamPolicy"] = artifactregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesGetIamPolicy"] = artifactregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesNpmPackagesGet"] = artifactregistry.get(
        "v1/{parent}/npmPackages",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNpmPackagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesNpmPackagesList"] = artifactregistry.get(
        "v1/{parent}/npmPackages",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNpmPackagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesPythonPackagesList"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PythonPackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesPythonPackagesGet"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PythonPackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesAptArtifactsUpload"
    ] = artifactregistry.post(
        "v1/{parent}/aptArtifacts:import",
        t.struct(
            {
                "parent": t.string().optional(),
                "gcsSource": t.proxy(
                    renames["ImportAptArtifactsGcsSourceIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesAptArtifactsImport"
    ] = artifactregistry.post(
        "v1/{parent}/aptArtifacts:import",
        t.struct(
            {
                "parent": t.string().optional(),
                "gcsSource": t.proxy(
                    renames["ImportAptArtifactsGcsSourceIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesGoogetArtifactsImport"
    ] = artifactregistry.post(
        "v1/{parent}/googetArtifacts:create",
        t.struct(
            {
                "parent": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadGoogetArtifactMediaResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesGoogetArtifactsUpload"
    ] = artifactregistry.post(
        "v1/{parent}/googetArtifacts:create",
        t.struct(
            {
                "parent": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadGoogetArtifactMediaResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesDockerImagesGet"] = artifactregistry.get(
        "v1/{parent}/dockerImages",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDockerImagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesDockerImagesList"] = artifactregistry.get(
        "v1/{parent}/dockerImages",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDockerImagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesKfpArtifactsUpload"
    ] = artifactregistry.post(
        "v1/{parent}/kfpArtifacts:create",
        t.struct(
            {
                "parent": t.string().optional(),
                "description": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadKfpArtifactMediaResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesMavenArtifactsGet"] = artifactregistry.get(
        "v1/{parent}/mavenArtifacts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMavenArtifactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesMavenArtifactsList"] = artifactregistry.get(
        "v1/{parent}/mavenArtifacts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMavenArtifactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesYumArtifactsImport"
    ] = artifactregistry.post(
        "v1/{parent}/yumArtifacts:create",
        t.struct(
            {
                "parent": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadYumArtifactMediaResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesYumArtifactsUpload"
    ] = artifactregistry.post(
        "v1/{parent}/yumArtifacts:create",
        t.struct(
            {
                "parent": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadYumArtifactMediaResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesPackagesDelete"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesPackagesList"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesPackagesGet"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesPackagesVersionsDelete"
    ] = artifactregistry.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesPackagesVersionsList"
    ] = artifactregistry.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesPackagesVersionsGet"
    ] = artifactregistry.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesPackagesTagsGet"] = artifactregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesPackagesTagsCreate"
    ] = artifactregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesPackagesTagsPatch"
    ] = artifactregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesPackagesTagsList"
    ] = artifactregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesPackagesTagsDelete"
    ] = artifactregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesFilesGet"] = artifactregistry.get(
        "v1/{parent}/files",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesFilesList"] = artifactregistry.get(
        "v1/{parent}/files",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="artifactregistry", renames=renames, types=types, functions=functions
    )
