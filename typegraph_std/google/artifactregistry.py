from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_artifactregistry() -> Import:
    artifactregistry = HTTPRuntime("https://artifactregistry.googleapis.com/")

    renames = {
        "ErrorResponse": "_artifactregistry_1_ErrorResponse",
        "ListTagsResponseIn": "_artifactregistry_2_ListTagsResponseIn",
        "ListTagsResponseOut": "_artifactregistry_3_ListTagsResponseOut",
        "UploadYumArtifactMetadataIn": "_artifactregistry_4_UploadYumArtifactMetadataIn",
        "UploadYumArtifactMetadataOut": "_artifactregistry_5_UploadYumArtifactMetadataOut",
        "UploadGoogetArtifactMediaResponseIn": "_artifactregistry_6_UploadGoogetArtifactMediaResponseIn",
        "UploadGoogetArtifactMediaResponseOut": "_artifactregistry_7_UploadGoogetArtifactMediaResponseOut",
        "UploadAptArtifactMetadataIn": "_artifactregistry_8_UploadAptArtifactMetadataIn",
        "UploadAptArtifactMetadataOut": "_artifactregistry_9_UploadAptArtifactMetadataOut",
        "UploadGoogetArtifactMetadataIn": "_artifactregistry_10_UploadGoogetArtifactMetadataIn",
        "UploadGoogetArtifactMetadataOut": "_artifactregistry_11_UploadGoogetArtifactMetadataOut",
        "ImportAptArtifactsErrorInfoIn": "_artifactregistry_12_ImportAptArtifactsErrorInfoIn",
        "ImportAptArtifactsErrorInfoOut": "_artifactregistry_13_ImportAptArtifactsErrorInfoOut",
        "LocationIn": "_artifactregistry_14_LocationIn",
        "LocationOut": "_artifactregistry_15_LocationOut",
        "RemoteRepositoryConfigIn": "_artifactregistry_16_RemoteRepositoryConfigIn",
        "RemoteRepositoryConfigOut": "_artifactregistry_17_RemoteRepositoryConfigOut",
        "SetIamPolicyRequestIn": "_artifactregistry_18_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_artifactregistry_19_SetIamPolicyRequestOut",
        "ImportAptArtifactsGcsSourceIn": "_artifactregistry_20_ImportAptArtifactsGcsSourceIn",
        "ImportAptArtifactsGcsSourceOut": "_artifactregistry_21_ImportAptArtifactsGcsSourceOut",
        "ListNpmPackagesResponseIn": "_artifactregistry_22_ListNpmPackagesResponseIn",
        "ListNpmPackagesResponseOut": "_artifactregistry_23_ListNpmPackagesResponseOut",
        "UploadKfpArtifactMediaResponseIn": "_artifactregistry_24_UploadKfpArtifactMediaResponseIn",
        "UploadKfpArtifactMediaResponseOut": "_artifactregistry_25_UploadKfpArtifactMediaResponseOut",
        "GoogleDevtoolsArtifactregistryV1FileIn": "_artifactregistry_26_GoogleDevtoolsArtifactregistryV1FileIn",
        "GoogleDevtoolsArtifactregistryV1FileOut": "_artifactregistry_27_GoogleDevtoolsArtifactregistryV1FileOut",
        "ListLocationsResponseIn": "_artifactregistry_28_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_artifactregistry_29_ListLocationsResponseOut",
        "ListPackagesResponseIn": "_artifactregistry_30_ListPackagesResponseIn",
        "ListPackagesResponseOut": "_artifactregistry_31_ListPackagesResponseOut",
        "MavenRepositoryConfigIn": "_artifactregistry_32_MavenRepositoryConfigIn",
        "MavenRepositoryConfigOut": "_artifactregistry_33_MavenRepositoryConfigOut",
        "UploadGoogetArtifactResponseIn": "_artifactregistry_34_UploadGoogetArtifactResponseIn",
        "UploadGoogetArtifactResponseOut": "_artifactregistry_35_UploadGoogetArtifactResponseOut",
        "ListMavenArtifactsResponseIn": "_artifactregistry_36_ListMavenArtifactsResponseIn",
        "ListMavenArtifactsResponseOut": "_artifactregistry_37_ListMavenArtifactsResponseOut",
        "ImportYumArtifactsRequestIn": "_artifactregistry_38_ImportYumArtifactsRequestIn",
        "ImportYumArtifactsRequestOut": "_artifactregistry_39_ImportYumArtifactsRequestOut",
        "HashIn": "_artifactregistry_40_HashIn",
        "HashOut": "_artifactregistry_41_HashOut",
        "UploadAptArtifactResponseIn": "_artifactregistry_42_UploadAptArtifactResponseIn",
        "UploadAptArtifactResponseOut": "_artifactregistry_43_UploadAptArtifactResponseOut",
        "BindingIn": "_artifactregistry_44_BindingIn",
        "BindingOut": "_artifactregistry_45_BindingOut",
        "ImportAptArtifactsMetadataIn": "_artifactregistry_46_ImportAptArtifactsMetadataIn",
        "ImportAptArtifactsMetadataOut": "_artifactregistry_47_ImportAptArtifactsMetadataOut",
        "UpstreamPolicyIn": "_artifactregistry_48_UpstreamPolicyIn",
        "UpstreamPolicyOut": "_artifactregistry_49_UpstreamPolicyOut",
        "UploadAptArtifactMediaResponseIn": "_artifactregistry_50_UploadAptArtifactMediaResponseIn",
        "UploadAptArtifactMediaResponseOut": "_artifactregistry_51_UploadAptArtifactMediaResponseOut",
        "ImportAptArtifactsRequestIn": "_artifactregistry_52_ImportAptArtifactsRequestIn",
        "ImportAptArtifactsRequestOut": "_artifactregistry_53_ImportAptArtifactsRequestOut",
        "DockerImageIn": "_artifactregistry_54_DockerImageIn",
        "DockerImageOut": "_artifactregistry_55_DockerImageOut",
        "AptArtifactIn": "_artifactregistry_56_AptArtifactIn",
        "AptArtifactOut": "_artifactregistry_57_AptArtifactOut",
        "ListDockerImagesResponseIn": "_artifactregistry_58_ListDockerImagesResponseIn",
        "ListDockerImagesResponseOut": "_artifactregistry_59_ListDockerImagesResponseOut",
        "ImportGoogetArtifactsErrorInfoIn": "_artifactregistry_60_ImportGoogetArtifactsErrorInfoIn",
        "ImportGoogetArtifactsErrorInfoOut": "_artifactregistry_61_ImportGoogetArtifactsErrorInfoOut",
        "ImportGoogetArtifactsMetadataIn": "_artifactregistry_62_ImportGoogetArtifactsMetadataIn",
        "ImportGoogetArtifactsMetadataOut": "_artifactregistry_63_ImportGoogetArtifactsMetadataOut",
        "StatusIn": "_artifactregistry_64_StatusIn",
        "StatusOut": "_artifactregistry_65_StatusOut",
        "DockerRepositoryIn": "_artifactregistry_66_DockerRepositoryIn",
        "DockerRepositoryOut": "_artifactregistry_67_DockerRepositoryOut",
        "NpmRepositoryIn": "_artifactregistry_68_NpmRepositoryIn",
        "NpmRepositoryOut": "_artifactregistry_69_NpmRepositoryOut",
        "UploadKfpArtifactRequestIn": "_artifactregistry_70_UploadKfpArtifactRequestIn",
        "UploadKfpArtifactRequestOut": "_artifactregistry_71_UploadKfpArtifactRequestOut",
        "ExprIn": "_artifactregistry_72_ExprIn",
        "ExprOut": "_artifactregistry_73_ExprOut",
        "TestIamPermissionsResponseIn": "_artifactregistry_74_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_artifactregistry_75_TestIamPermissionsResponseOut",
        "NpmPackageIn": "_artifactregistry_76_NpmPackageIn",
        "NpmPackageOut": "_artifactregistry_77_NpmPackageOut",
        "ImportYumArtifactsMetadataIn": "_artifactregistry_78_ImportYumArtifactsMetadataIn",
        "ImportYumArtifactsMetadataOut": "_artifactregistry_79_ImportYumArtifactsMetadataOut",
        "ListVersionsResponseIn": "_artifactregistry_80_ListVersionsResponseIn",
        "ListVersionsResponseOut": "_artifactregistry_81_ListVersionsResponseOut",
        "TagIn": "_artifactregistry_82_TagIn",
        "TagOut": "_artifactregistry_83_TagOut",
        "VersionIn": "_artifactregistry_84_VersionIn",
        "VersionOut": "_artifactregistry_85_VersionOut",
        "DockerRepositoryConfigIn": "_artifactregistry_86_DockerRepositoryConfigIn",
        "DockerRepositoryConfigOut": "_artifactregistry_87_DockerRepositoryConfigOut",
        "MavenRepositoryIn": "_artifactregistry_88_MavenRepositoryIn",
        "MavenRepositoryOut": "_artifactregistry_89_MavenRepositoryOut",
        "ProjectSettingsIn": "_artifactregistry_90_ProjectSettingsIn",
        "ProjectSettingsOut": "_artifactregistry_91_ProjectSettingsOut",
        "PythonRepositoryIn": "_artifactregistry_92_PythonRepositoryIn",
        "PythonRepositoryOut": "_artifactregistry_93_PythonRepositoryOut",
        "KfpArtifactIn": "_artifactregistry_94_KfpArtifactIn",
        "KfpArtifactOut": "_artifactregistry_95_KfpArtifactOut",
        "BatchDeleteVersionsMetadataIn": "_artifactregistry_96_BatchDeleteVersionsMetadataIn",
        "BatchDeleteVersionsMetadataOut": "_artifactregistry_97_BatchDeleteVersionsMetadataOut",
        "MavenArtifactIn": "_artifactregistry_98_MavenArtifactIn",
        "MavenArtifactOut": "_artifactregistry_99_MavenArtifactOut",
        "UploadKfpArtifactMetadataIn": "_artifactregistry_100_UploadKfpArtifactMetadataIn",
        "UploadKfpArtifactMetadataOut": "_artifactregistry_101_UploadKfpArtifactMetadataOut",
        "ListRepositoriesResponseIn": "_artifactregistry_102_ListRepositoriesResponseIn",
        "ListRepositoriesResponseOut": "_artifactregistry_103_ListRepositoriesResponseOut",
        "PolicyIn": "_artifactregistry_104_PolicyIn",
        "PolicyOut": "_artifactregistry_105_PolicyOut",
        "ImportYumArtifactsErrorInfoIn": "_artifactregistry_106_ImportYumArtifactsErrorInfoIn",
        "ImportYumArtifactsErrorInfoOut": "_artifactregistry_107_ImportYumArtifactsErrorInfoOut",
        "ImportGoogetArtifactsGcsSourceIn": "_artifactregistry_108_ImportGoogetArtifactsGcsSourceIn",
        "ImportGoogetArtifactsGcsSourceOut": "_artifactregistry_109_ImportGoogetArtifactsGcsSourceOut",
        "TestIamPermissionsRequestIn": "_artifactregistry_110_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_artifactregistry_111_TestIamPermissionsRequestOut",
        "VirtualRepositoryConfigIn": "_artifactregistry_112_VirtualRepositoryConfigIn",
        "VirtualRepositoryConfigOut": "_artifactregistry_113_VirtualRepositoryConfigOut",
        "OperationIn": "_artifactregistry_114_OperationIn",
        "OperationOut": "_artifactregistry_115_OperationOut",
        "ImportAptArtifactsResponseIn": "_artifactregistry_116_ImportAptArtifactsResponseIn",
        "ImportAptArtifactsResponseOut": "_artifactregistry_117_ImportAptArtifactsResponseOut",
        "GoogetArtifactIn": "_artifactregistry_118_GoogetArtifactIn",
        "GoogetArtifactOut": "_artifactregistry_119_GoogetArtifactOut",
        "VPCSCConfigIn": "_artifactregistry_120_VPCSCConfigIn",
        "VPCSCConfigOut": "_artifactregistry_121_VPCSCConfigOut",
        "ListFilesResponseIn": "_artifactregistry_122_ListFilesResponseIn",
        "ListFilesResponseOut": "_artifactregistry_123_ListFilesResponseOut",
        "ImportYumArtifactsResponseIn": "_artifactregistry_124_ImportYumArtifactsResponseIn",
        "ImportYumArtifactsResponseOut": "_artifactregistry_125_ImportYumArtifactsResponseOut",
        "YumArtifactIn": "_artifactregistry_126_YumArtifactIn",
        "YumArtifactOut": "_artifactregistry_127_YumArtifactOut",
        "PackageIn": "_artifactregistry_128_PackageIn",
        "PackageOut": "_artifactregistry_129_PackageOut",
        "UploadYumArtifactMediaResponseIn": "_artifactregistry_130_UploadYumArtifactMediaResponseIn",
        "UploadYumArtifactMediaResponseOut": "_artifactregistry_131_UploadYumArtifactMediaResponseOut",
        "OperationMetadataIn": "_artifactregistry_132_OperationMetadataIn",
        "OperationMetadataOut": "_artifactregistry_133_OperationMetadataOut",
        "UploadAptArtifactRequestIn": "_artifactregistry_134_UploadAptArtifactRequestIn",
        "UploadAptArtifactRequestOut": "_artifactregistry_135_UploadAptArtifactRequestOut",
        "ImportYumArtifactsGcsSourceIn": "_artifactregistry_136_ImportYumArtifactsGcsSourceIn",
        "ImportYumArtifactsGcsSourceOut": "_artifactregistry_137_ImportYumArtifactsGcsSourceOut",
        "ImportGoogetArtifactsRequestIn": "_artifactregistry_138_ImportGoogetArtifactsRequestIn",
        "ImportGoogetArtifactsRequestOut": "_artifactregistry_139_ImportGoogetArtifactsRequestOut",
        "ListPythonPackagesResponseIn": "_artifactregistry_140_ListPythonPackagesResponseIn",
        "ListPythonPackagesResponseOut": "_artifactregistry_141_ListPythonPackagesResponseOut",
        "UploadYumArtifactResponseIn": "_artifactregistry_142_UploadYumArtifactResponseIn",
        "UploadYumArtifactResponseOut": "_artifactregistry_143_UploadYumArtifactResponseOut",
        "RepositoryIn": "_artifactregistry_144_RepositoryIn",
        "RepositoryOut": "_artifactregistry_145_RepositoryOut",
        "PythonPackageIn": "_artifactregistry_146_PythonPackageIn",
        "PythonPackageOut": "_artifactregistry_147_PythonPackageOut",
        "UploadYumArtifactRequestIn": "_artifactregistry_148_UploadYumArtifactRequestIn",
        "UploadYumArtifactRequestOut": "_artifactregistry_149_UploadYumArtifactRequestOut",
        "ImportGoogetArtifactsResponseIn": "_artifactregistry_150_ImportGoogetArtifactsResponseIn",
        "ImportGoogetArtifactsResponseOut": "_artifactregistry_151_ImportGoogetArtifactsResponseOut",
        "EmptyIn": "_artifactregistry_152_EmptyIn",
        "EmptyOut": "_artifactregistry_153_EmptyOut",
        "UploadGoogetArtifactRequestIn": "_artifactregistry_154_UploadGoogetArtifactRequestIn",
        "UploadGoogetArtifactRequestOut": "_artifactregistry_155_UploadGoogetArtifactRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListTagsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tags": t.array(t.proxy(renames["TagIn"])).optional(),
        }
    ).named(renames["ListTagsResponseIn"])
    types["ListTagsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tags": t.array(t.proxy(renames["TagOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTagsResponseOut"])
    types["UploadYumArtifactMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadYumArtifactMetadataIn"]
    )
    types["UploadYumArtifactMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadYumArtifactMetadataOut"])
    types["UploadGoogetArtifactMediaResponseIn"] = t.struct(
        {"operation": t.proxy(renames["OperationIn"]).optional()}
    ).named(renames["UploadGoogetArtifactMediaResponseIn"])
    types["UploadGoogetArtifactMediaResponseOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadGoogetArtifactMediaResponseOut"])
    types["UploadAptArtifactMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadAptArtifactMetadataIn"]
    )
    types["UploadAptArtifactMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadAptArtifactMetadataOut"])
    types["UploadGoogetArtifactMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UploadGoogetArtifactMetadataIn"])
    types["UploadGoogetArtifactMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadGoogetArtifactMetadataOut"])
    types["ImportAptArtifactsErrorInfoIn"] = t.struct(
        {
            "gcsSource": t.proxy(renames["ImportAptArtifactsGcsSourceIn"]).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["ImportAptArtifactsErrorInfoIn"])
    types["ImportAptArtifactsErrorInfoOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["ImportAptArtifactsGcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportAptArtifactsErrorInfoOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["RemoteRepositoryConfigIn"] = t.struct(
        {
            "npmRepository": t.proxy(renames["NpmRepositoryIn"]).optional(),
            "pythonRepository": t.proxy(renames["PythonRepositoryIn"]).optional(),
            "mavenRepository": t.proxy(renames["MavenRepositoryIn"]).optional(),
            "description": t.string().optional(),
            "dockerRepository": t.proxy(renames["DockerRepositoryIn"]).optional(),
        }
    ).named(renames["RemoteRepositoryConfigIn"])
    types["RemoteRepositoryConfigOut"] = t.struct(
        {
            "npmRepository": t.proxy(renames["NpmRepositoryOut"]).optional(),
            "pythonRepository": t.proxy(renames["PythonRepositoryOut"]).optional(),
            "mavenRepository": t.proxy(renames["MavenRepositoryOut"]).optional(),
            "description": t.string().optional(),
            "dockerRepository": t.proxy(renames["DockerRepositoryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoteRepositoryConfigOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["ImportAptArtifactsGcsSourceIn"] = t.struct(
        {"useWildcards": t.boolean().optional(), "uris": t.array(t.string()).optional()}
    ).named(renames["ImportAptArtifactsGcsSourceIn"])
    types["ImportAptArtifactsGcsSourceOut"] = t.struct(
        {
            "useWildcards": t.boolean().optional(),
            "uris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportAptArtifactsGcsSourceOut"])
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
    types["UploadKfpArtifactMediaResponseIn"] = t.struct(
        {"operation": t.proxy(renames["OperationIn"]).optional()}
    ).named(renames["UploadKfpArtifactMediaResponseIn"])
    types["UploadKfpArtifactMediaResponseOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadKfpArtifactMediaResponseOut"])
    types["GoogleDevtoolsArtifactregistryV1FileIn"] = t.struct(
        {
            "name": t.string().optional(),
            "owner": t.string().optional(),
            "hashes": t.array(t.proxy(renames["HashIn"])).optional(),
            "sizeBytes": t.string().optional(),
        }
    ).named(renames["GoogleDevtoolsArtifactregistryV1FileIn"])
    types["GoogleDevtoolsArtifactregistryV1FileOut"] = t.struct(
        {
            "name": t.string().optional(),
            "owner": t.string().optional(),
            "hashes": t.array(t.proxy(renames["HashOut"])).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "fetchTime": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDevtoolsArtifactregistryV1FileOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["ListPackagesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "packages": t.array(t.proxy(renames["PackageIn"])).optional(),
        }
    ).named(renames["ListPackagesResponseIn"])
    types["ListPackagesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "packages": t.array(t.proxy(renames["PackageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPackagesResponseOut"])
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
    types["ListMavenArtifactsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "mavenArtifacts": t.array(t.proxy(renames["MavenArtifactIn"])).optional(),
        }
    ).named(renames["ListMavenArtifactsResponseIn"])
    types["ListMavenArtifactsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "mavenArtifacts": t.array(t.proxy(renames["MavenArtifactOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMavenArtifactsResponseOut"])
    types["ImportYumArtifactsRequestIn"] = t.struct(
        {"gcsSource": t.proxy(renames["ImportYumArtifactsGcsSourceIn"]).optional()}
    ).named(renames["ImportYumArtifactsRequestIn"])
    types["ImportYumArtifactsRequestOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["ImportYumArtifactsGcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportYumArtifactsRequestOut"])
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
    types["UploadAptArtifactResponseIn"] = t.struct(
        {"aptArtifacts": t.array(t.proxy(renames["AptArtifactIn"])).optional()}
    ).named(renames["UploadAptArtifactResponseIn"])
    types["UploadAptArtifactResponseOut"] = t.struct(
        {
            "aptArtifacts": t.array(t.proxy(renames["AptArtifactOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadAptArtifactResponseOut"])
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["ImportAptArtifactsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportAptArtifactsMetadataIn"])
    types["ImportAptArtifactsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportAptArtifactsMetadataOut"])
    types["UpstreamPolicyIn"] = t.struct(
        {
            "repository": t.string().optional(),
            "id": t.string().optional(),
            "priority": t.integer().optional(),
        }
    ).named(renames["UpstreamPolicyIn"])
    types["UpstreamPolicyOut"] = t.struct(
        {
            "repository": t.string().optional(),
            "id": t.string().optional(),
            "priority": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpstreamPolicyOut"])
    types["UploadAptArtifactMediaResponseIn"] = t.struct(
        {"operation": t.proxy(renames["OperationIn"]).optional()}
    ).named(renames["UploadAptArtifactMediaResponseIn"])
    types["UploadAptArtifactMediaResponseOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadAptArtifactMediaResponseOut"])
    types["ImportAptArtifactsRequestIn"] = t.struct(
        {"gcsSource": t.proxy(renames["ImportAptArtifactsGcsSourceIn"]).optional()}
    ).named(renames["ImportAptArtifactsRequestIn"])
    types["ImportAptArtifactsRequestOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["ImportAptArtifactsGcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportAptArtifactsRequestOut"])
    types["DockerImageIn"] = t.struct(
        {
            "buildTime": t.string().optional(),
            "uploadTime": t.string().optional(),
            "mediaType": t.string().optional(),
            "uri": t.string(),
            "tags": t.array(t.string()).optional(),
            "name": t.string(),
            "imageSizeBytes": t.string().optional(),
        }
    ).named(renames["DockerImageIn"])
    types["DockerImageOut"] = t.struct(
        {
            "buildTime": t.string().optional(),
            "uploadTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "mediaType": t.string().optional(),
            "uri": t.string(),
            "tags": t.array(t.string()).optional(),
            "name": t.string(),
            "imageSizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DockerImageOut"])
    types["AptArtifactIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AptArtifactIn"]
    )
    types["AptArtifactOut"] = t.struct(
        {
            "packageType": t.string().optional(),
            "architecture": t.string().optional(),
            "controlFile": t.string().optional(),
            "name": t.string().optional(),
            "component": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AptArtifactOut"])
    types["ListDockerImagesResponseIn"] = t.struct(
        {
            "dockerImages": t.array(t.proxy(renames["DockerImageIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDockerImagesResponseIn"])
    types["ListDockerImagesResponseOut"] = t.struct(
        {
            "dockerImages": t.array(t.proxy(renames["DockerImageOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDockerImagesResponseOut"])
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
    types["ImportGoogetArtifactsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportGoogetArtifactsMetadataIn"])
    types["ImportGoogetArtifactsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportGoogetArtifactsMetadataOut"])
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
    types["DockerRepositoryIn"] = t.struct(
        {"publicRepository": t.string().optional()}
    ).named(renames["DockerRepositoryIn"])
    types["DockerRepositoryOut"] = t.struct(
        {
            "publicRepository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DockerRepositoryOut"])
    types["NpmRepositoryIn"] = t.struct(
        {"publicRepository": t.string().optional()}
    ).named(renames["NpmRepositoryIn"])
    types["NpmRepositoryOut"] = t.struct(
        {
            "publicRepository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NpmRepositoryOut"])
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
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["NpmPackageIn"] = t.struct(
        {
            "packageName": t.string().optional(),
            "name": t.string(),
            "tags": t.array(t.string()).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["NpmPackageIn"])
    types["NpmPackageOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "name": t.string(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NpmPackageOut"])
    types["ImportYumArtifactsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportYumArtifactsMetadataIn"])
    types["ImportYumArtifactsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportYumArtifactsMetadataOut"])
    types["ListVersionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "versions": t.array(t.proxy(renames["VersionIn"])).optional(),
        }
    ).named(renames["ListVersionsResponseIn"])
    types["ListVersionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "versions": t.array(t.proxy(renames["VersionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVersionsResponseOut"])
    types["TagIn"] = t.struct(
        {"name": t.string().optional(), "version": t.string().optional()}
    ).named(renames["TagIn"])
    types["TagOut"] = t.struct(
        {
            "name": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagOut"])
    types["VersionIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "relatedTags": t.array(t.proxy(renames["TagIn"])).optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "relatedTags": t.array(t.proxy(renames["TagOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
    types["DockerRepositoryConfigIn"] = t.struct(
        {"immutableTags": t.boolean().optional()}
    ).named(renames["DockerRepositoryConfigIn"])
    types["DockerRepositoryConfigOut"] = t.struct(
        {
            "immutableTags": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DockerRepositoryConfigOut"])
    types["MavenRepositoryIn"] = t.struct(
        {"publicRepository": t.string().optional()}
    ).named(renames["MavenRepositoryIn"])
    types["MavenRepositoryOut"] = t.struct(
        {
            "publicRepository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MavenRepositoryOut"])
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
    types["PythonRepositoryIn"] = t.struct(
        {"publicRepository": t.string().optional()}
    ).named(renames["PythonRepositoryIn"])
    types["PythonRepositoryOut"] = t.struct(
        {
            "publicRepository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonRepositoryOut"])
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
    types["BatchDeleteVersionsMetadataIn"] = t.struct(
        {"failedVersions": t.array(t.string()).optional()}
    ).named(renames["BatchDeleteVersionsMetadataIn"])
    types["BatchDeleteVersionsMetadataOut"] = t.struct(
        {
            "failedVersions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteVersionsMetadataOut"])
    types["MavenArtifactIn"] = t.struct(
        {
            "name": t.string(),
            "groupId": t.string().optional(),
            "version": t.string().optional(),
            "pomUri": t.string(),
            "artifactId": t.string().optional(),
        }
    ).named(renames["MavenArtifactIn"])
    types["MavenArtifactOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string(),
            "groupId": t.string().optional(),
            "version": t.string().optional(),
            "pomUri": t.string(),
            "artifactId": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MavenArtifactOut"])
    types["UploadKfpArtifactMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadKfpArtifactMetadataIn"]
    )
    types["UploadKfpArtifactMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadKfpArtifactMetadataOut"])
    types["ListRepositoriesResponseIn"] = t.struct(
        {
            "repositories": t.array(t.proxy(renames["RepositoryIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListRepositoriesResponseIn"])
    types["ListRepositoriesResponseOut"] = t.struct(
        {
            "repositories": t.array(t.proxy(renames["RepositoryOut"])).optional(),
            "nextPageToken": t.string().optional(),
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
    types["ImportYumArtifactsErrorInfoIn"] = t.struct(
        {
            "gcsSource": t.proxy(renames["ImportYumArtifactsGcsSourceIn"]).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["ImportYumArtifactsErrorInfoIn"])
    types["ImportYumArtifactsErrorInfoOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["ImportYumArtifactsGcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportYumArtifactsErrorInfoOut"])
    types["ImportGoogetArtifactsGcsSourceIn"] = t.struct(
        {"useWildcards": t.boolean().optional(), "uris": t.array(t.string()).optional()}
    ).named(renames["ImportGoogetArtifactsGcsSourceIn"])
    types["ImportGoogetArtifactsGcsSourceOut"] = t.struct(
        {
            "useWildcards": t.boolean().optional(),
            "uris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportGoogetArtifactsGcsSourceOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["ImportAptArtifactsResponseIn"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["ImportAptArtifactsErrorInfoIn"])
            ).optional(),
            "aptArtifacts": t.array(t.proxy(renames["AptArtifactIn"])).optional(),
        }
    ).named(renames["ImportAptArtifactsResponseIn"])
    types["ImportAptArtifactsResponseOut"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["ImportAptArtifactsErrorInfoOut"])
            ).optional(),
            "aptArtifacts": t.array(t.proxy(renames["AptArtifactOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportAptArtifactsResponseOut"])
    types["GoogetArtifactIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogetArtifactIn"]
    )
    types["GoogetArtifactOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "name": t.string().optional(),
            "architecture": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogetArtifactOut"])
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
    types["ListFilesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "files": t.array(
                t.proxy(renames["GoogleDevtoolsArtifactregistryV1FileIn"])
            ).optional(),
        }
    ).named(renames["ListFilesResponseIn"])
    types["ListFilesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "files": t.array(
                t.proxy(renames["GoogleDevtoolsArtifactregistryV1FileOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFilesResponseOut"])
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
    types["YumArtifactIn"] = t.struct({"_": t.string().optional()}).named(
        renames["YumArtifactIn"]
    )
    types["YumArtifactOut"] = t.struct(
        {
            "packageType": t.string().optional(),
            "name": t.string().optional(),
            "architecture": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YumArtifactOut"])
    types["PackageIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["PackageIn"])
    types["PackageOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageOut"])
    types["UploadYumArtifactMediaResponseIn"] = t.struct(
        {"operation": t.proxy(renames["OperationIn"]).optional()}
    ).named(renames["UploadYumArtifactMediaResponseIn"])
    types["UploadYumArtifactMediaResponseOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadYumArtifactMediaResponseOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OperationMetadataOut"])
    types["UploadAptArtifactRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadAptArtifactRequestIn"]
    )
    types["UploadAptArtifactRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadAptArtifactRequestOut"])
    types["ImportYumArtifactsGcsSourceIn"] = t.struct(
        {"useWildcards": t.boolean().optional(), "uris": t.array(t.string()).optional()}
    ).named(renames["ImportYumArtifactsGcsSourceIn"])
    types["ImportYumArtifactsGcsSourceOut"] = t.struct(
        {
            "useWildcards": t.boolean().optional(),
            "uris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportYumArtifactsGcsSourceOut"])
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
    types["ListPythonPackagesResponseIn"] = t.struct(
        {
            "pythonPackages": t.array(t.proxy(renames["PythonPackageIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPythonPackagesResponseIn"])
    types["ListPythonPackagesResponseOut"] = t.struct(
        {
            "pythonPackages": t.array(t.proxy(renames["PythonPackageOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPythonPackagesResponseOut"])
    types["UploadYumArtifactResponseIn"] = t.struct(
        {"yumArtifacts": t.array(t.proxy(renames["YumArtifactIn"])).optional()}
    ).named(renames["UploadYumArtifactResponseIn"])
    types["UploadYumArtifactResponseOut"] = t.struct(
        {
            "yumArtifacts": t.array(t.proxy(renames["YumArtifactOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadYumArtifactResponseOut"])
    types["RepositoryIn"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "format": t.string().optional(),
            "virtualRepositoryConfig": t.proxy(
                renames["VirtualRepositoryConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "remoteRepositoryConfig": t.proxy(
                renames["RemoteRepositoryConfigIn"]
            ).optional(),
            "dockerConfig": t.proxy(renames["DockerRepositoryConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "mode": t.string().optional(),
            "mavenConfig": t.proxy(renames["MavenRepositoryConfigIn"]).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["RepositoryIn"])
    types["RepositoryOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "format": t.string().optional(),
            "virtualRepositoryConfig": t.proxy(
                renames["VirtualRepositoryConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "remoteRepositoryConfig": t.proxy(
                renames["RemoteRepositoryConfigOut"]
            ).optional(),
            "dockerConfig": t.proxy(renames["DockerRepositoryConfigOut"]).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "mode": t.string().optional(),
            "mavenConfig": t.proxy(renames["MavenRepositoryConfigOut"]).optional(),
            "sizeBytes": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepositoryOut"])
    types["PythonPackageIn"] = t.struct(
        {
            "version": t.string().optional(),
            "uri": t.string(),
            "packageName": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["PythonPackageIn"])
    types["PythonPackageOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "version": t.string().optional(),
            "uri": t.string(),
            "createTime": t.string().optional(),
            "packageName": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonPackageOut"])
    types["UploadYumArtifactRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadYumArtifactRequestIn"]
    )
    types["UploadYumArtifactRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadYumArtifactRequestOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["UploadGoogetArtifactRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UploadGoogetArtifactRequestIn"])
    types["UploadGoogetArtifactRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadGoogetArtifactRequestOut"])

    functions = {}
    functions["projectsUpdateProjectSettings"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetProjectSettings"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectSettingsOut"]),
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
    functions["projectsLocationsGetVpcscConfig"] = artifactregistry.get(
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
    functions["projectsLocationsRepositoriesList"] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "format": t.string().optional(),
                "virtualRepositoryConfig": t.proxy(
                    renames["VirtualRepositoryConfigIn"]
                ).optional(),
                "remoteRepositoryConfig": t.proxy(
                    renames["RemoteRepositoryConfigIn"]
                ).optional(),
                "dockerConfig": t.proxy(renames["DockerRepositoryConfigIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mode": t.string().optional(),
                "mavenConfig": t.proxy(renames["MavenRepositoryConfigIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepositoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesCreate"] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "format": t.string().optional(),
                "virtualRepositoryConfig": t.proxy(
                    renames["VirtualRepositoryConfigIn"]
                ).optional(),
                "remoteRepositoryConfig": t.proxy(
                    renames["RemoteRepositoryConfigIn"]
                ).optional(),
                "dockerConfig": t.proxy(renames["DockerRepositoryConfigIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mode": t.string().optional(),
                "mavenConfig": t.proxy(renames["MavenRepositoryConfigIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepositoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesGetIamPolicy"] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "format": t.string().optional(),
                "virtualRepositoryConfig": t.proxy(
                    renames["VirtualRepositoryConfigIn"]
                ).optional(),
                "remoteRepositoryConfig": t.proxy(
                    renames["RemoteRepositoryConfigIn"]
                ).optional(),
                "dockerConfig": t.proxy(renames["DockerRepositoryConfigIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mode": t.string().optional(),
                "mavenConfig": t.proxy(renames["MavenRepositoryConfigIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepositoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesDelete"] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "format": t.string().optional(),
                "virtualRepositoryConfig": t.proxy(
                    renames["VirtualRepositoryConfigIn"]
                ).optional(),
                "remoteRepositoryConfig": t.proxy(
                    renames["RemoteRepositoryConfigIn"]
                ).optional(),
                "dockerConfig": t.proxy(renames["DockerRepositoryConfigIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mode": t.string().optional(),
                "mavenConfig": t.proxy(renames["MavenRepositoryConfigIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepositoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesGet"] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "format": t.string().optional(),
                "virtualRepositoryConfig": t.proxy(
                    renames["VirtualRepositoryConfigIn"]
                ).optional(),
                "remoteRepositoryConfig": t.proxy(
                    renames["RemoteRepositoryConfigIn"]
                ).optional(),
                "dockerConfig": t.proxy(renames["DockerRepositoryConfigIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mode": t.string().optional(),
                "mavenConfig": t.proxy(renames["MavenRepositoryConfigIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepositoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesSetIamPolicy"] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "format": t.string().optional(),
                "virtualRepositoryConfig": t.proxy(
                    renames["VirtualRepositoryConfigIn"]
                ).optional(),
                "remoteRepositoryConfig": t.proxy(
                    renames["RemoteRepositoryConfigIn"]
                ).optional(),
                "dockerConfig": t.proxy(renames["DockerRepositoryConfigIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mode": t.string().optional(),
                "mavenConfig": t.proxy(renames["MavenRepositoryConfigIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepositoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesTestIamPermissions"
    ] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "format": t.string().optional(),
                "virtualRepositoryConfig": t.proxy(
                    renames["VirtualRepositoryConfigIn"]
                ).optional(),
                "remoteRepositoryConfig": t.proxy(
                    renames["RemoteRepositoryConfigIn"]
                ).optional(),
                "dockerConfig": t.proxy(renames["DockerRepositoryConfigIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mode": t.string().optional(),
                "mavenConfig": t.proxy(renames["MavenRepositoryConfigIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepositoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesPatch"] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "format": t.string().optional(),
                "virtualRepositoryConfig": t.proxy(
                    renames["VirtualRepositoryConfigIn"]
                ).optional(),
                "remoteRepositoryConfig": t.proxy(
                    renames["RemoteRepositoryConfigIn"]
                ).optional(),
                "dockerConfig": t.proxy(renames["DockerRepositoryConfigIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mode": t.string().optional(),
                "mavenConfig": t.proxy(renames["MavenRepositoryConfigIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepositoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesYumArtifactsUpload"
    ] = artifactregistry.post(
        "v1/{parent}/yumArtifacts:import",
        t.struct(
            {
                "parent": t.string().optional(),
                "gcsSource": t.proxy(
                    renames["ImportYumArtifactsGcsSourceIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesYumArtifactsImport"
    ] = artifactregistry.post(
        "v1/{parent}/yumArtifacts:import",
        t.struct(
            {
                "parent": t.string().optional(),
                "gcsSource": t.proxy(
                    renames["ImportYumArtifactsGcsSourceIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesDockerImagesGet"] = artifactregistry.get(
        "v1/{parent}/dockerImages",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDockerImagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesNpmPackagesGet"] = artifactregistry.get(
        "v1/{parent}/npmPackages",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNpmPackagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesPythonPackagesGet"] = artifactregistry.get(
        "v1/{parent}/pythonPackages",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPythonPackagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesPythonPackagesList"] = artifactregistry.get(
        "v1/{parent}/pythonPackages",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPythonPackagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesMavenArtifactsGet"] = artifactregistry.get(
        "v1/{parent}/mavenArtifacts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMavenArtifactsResponseOut"]),
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
    functions["projectsLocationsRepositoriesPackagesDelete"] = artifactregistry.get(
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
    functions["projectsLocationsRepositoriesPackagesTagsGet"] = artifactregistry.delete(
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
        "projectsLocationsRepositoriesPackagesTagsCreate"
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
    functions[
        "projectsLocationsRepositoriesPackagesVersionsGet"
    ] = artifactregistry.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesPackagesVersionsDelete"
    ] = artifactregistry.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesPackagesVersionsList"
    ] = artifactregistry.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVersionsResponseOut"]),
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
    functions["projectsLocationsRepositoriesFilesGet"] = artifactregistry.get(
        "v1/{parent}/files",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
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
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesGoogetArtifactsUpload"
    ] = artifactregistry.post(
        "v1/{parent}/googetArtifacts:import",
        t.struct(
            {
                "parent": t.string().optional(),
                "gcsSource": t.proxy(
                    renames["ImportGoogetArtifactsGcsSourceIn"]
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
        "v1/{parent}/googetArtifacts:import",
        t.struct(
            {
                "parent": t.string().optional(),
                "gcsSource": t.proxy(
                    renames["ImportGoogetArtifactsGcsSourceIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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

    return Import(
        importer="artifactregistry",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
