from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_artifactregistry():
    artifactregistry = HTTPRuntime("https://artifactregistry.googleapis.com/")

    renames = {
        "ErrorResponse": "_artifactregistry_1_ErrorResponse",
        "UploadGoogetArtifactResponseIn": "_artifactregistry_2_UploadGoogetArtifactResponseIn",
        "UploadGoogetArtifactResponseOut": "_artifactregistry_3_UploadGoogetArtifactResponseOut",
        "AptArtifactIn": "_artifactregistry_4_AptArtifactIn",
        "AptArtifactOut": "_artifactregistry_5_AptArtifactOut",
        "ImportGoogetArtifactsErrorInfoIn": "_artifactregistry_6_ImportGoogetArtifactsErrorInfoIn",
        "ImportGoogetArtifactsErrorInfoOut": "_artifactregistry_7_ImportGoogetArtifactsErrorInfoOut",
        "ListLocationsResponseIn": "_artifactregistry_8_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_artifactregistry_9_ListLocationsResponseOut",
        "UploadGoModuleMetadataIn": "_artifactregistry_10_UploadGoModuleMetadataIn",
        "UploadGoModuleMetadataOut": "_artifactregistry_11_UploadGoModuleMetadataOut",
        "UploadKfpArtifactMetadataIn": "_artifactregistry_12_UploadKfpArtifactMetadataIn",
        "UploadKfpArtifactMetadataOut": "_artifactregistry_13_UploadKfpArtifactMetadataOut",
        "VirtualRepositoryConfigIn": "_artifactregistry_14_VirtualRepositoryConfigIn",
        "VirtualRepositoryConfigOut": "_artifactregistry_15_VirtualRepositoryConfigOut",
        "UploadKfpArtifactMediaResponseIn": "_artifactregistry_16_UploadKfpArtifactMediaResponseIn",
        "UploadKfpArtifactMediaResponseOut": "_artifactregistry_17_UploadKfpArtifactMediaResponseOut",
        "NpmRepositoryIn": "_artifactregistry_18_NpmRepositoryIn",
        "NpmRepositoryOut": "_artifactregistry_19_NpmRepositoryOut",
        "ImportYumArtifactsResponseIn": "_artifactregistry_20_ImportYumArtifactsResponseIn",
        "ImportYumArtifactsResponseOut": "_artifactregistry_21_ImportYumArtifactsResponseOut",
        "ProjectSettingsIn": "_artifactregistry_22_ProjectSettingsIn",
        "ProjectSettingsOut": "_artifactregistry_23_ProjectSettingsOut",
        "ListVersionsResponseIn": "_artifactregistry_24_ListVersionsResponseIn",
        "ListVersionsResponseOut": "_artifactregistry_25_ListVersionsResponseOut",
        "OperationIn": "_artifactregistry_26_OperationIn",
        "OperationOut": "_artifactregistry_27_OperationOut",
        "BatchDeleteVersionsMetadataIn": "_artifactregistry_28_BatchDeleteVersionsMetadataIn",
        "BatchDeleteVersionsMetadataOut": "_artifactregistry_29_BatchDeleteVersionsMetadataOut",
        "UploadKfpArtifactRequestIn": "_artifactregistry_30_UploadKfpArtifactRequestIn",
        "UploadKfpArtifactRequestOut": "_artifactregistry_31_UploadKfpArtifactRequestOut",
        "DockerImageIn": "_artifactregistry_32_DockerImageIn",
        "DockerImageOut": "_artifactregistry_33_DockerImageOut",
        "VersionIn": "_artifactregistry_34_VersionIn",
        "VersionOut": "_artifactregistry_35_VersionOut",
        "ImportAptArtifactsGcsSourceIn": "_artifactregistry_36_ImportAptArtifactsGcsSourceIn",
        "ImportAptArtifactsGcsSourceOut": "_artifactregistry_37_ImportAptArtifactsGcsSourceOut",
        "SetIamPolicyRequestIn": "_artifactregistry_38_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_artifactregistry_39_SetIamPolicyRequestOut",
        "UploadYumArtifactRequestIn": "_artifactregistry_40_UploadYumArtifactRequestIn",
        "UploadYumArtifactRequestOut": "_artifactregistry_41_UploadYumArtifactRequestOut",
        "ImportAptArtifactsMetadataIn": "_artifactregistry_42_ImportAptArtifactsMetadataIn",
        "ImportAptArtifactsMetadataOut": "_artifactregistry_43_ImportAptArtifactsMetadataOut",
        "ImportGoogetArtifactsMetadataIn": "_artifactregistry_44_ImportGoogetArtifactsMetadataIn",
        "ImportGoogetArtifactsMetadataOut": "_artifactregistry_45_ImportGoogetArtifactsMetadataOut",
        "UploadAptArtifactMediaResponseIn": "_artifactregistry_46_UploadAptArtifactMediaResponseIn",
        "UploadAptArtifactMediaResponseOut": "_artifactregistry_47_UploadAptArtifactMediaResponseOut",
        "ListPackagesResponseIn": "_artifactregistry_48_ListPackagesResponseIn",
        "ListPackagesResponseOut": "_artifactregistry_49_ListPackagesResponseOut",
        "UploadGoModuleRequestIn": "_artifactregistry_50_UploadGoModuleRequestIn",
        "UploadGoModuleRequestOut": "_artifactregistry_51_UploadGoModuleRequestOut",
        "RemoteRepositoryConfigIn": "_artifactregistry_52_RemoteRepositoryConfigIn",
        "RemoteRepositoryConfigOut": "_artifactregistry_53_RemoteRepositoryConfigOut",
        "ImportYumArtifactsMetadataIn": "_artifactregistry_54_ImportYumArtifactsMetadataIn",
        "ImportYumArtifactsMetadataOut": "_artifactregistry_55_ImportYumArtifactsMetadataOut",
        "DockerRepositoryConfigIn": "_artifactregistry_56_DockerRepositoryConfigIn",
        "DockerRepositoryConfigOut": "_artifactregistry_57_DockerRepositoryConfigOut",
        "ListTagsResponseIn": "_artifactregistry_58_ListTagsResponseIn",
        "ListTagsResponseOut": "_artifactregistry_59_ListTagsResponseOut",
        "MavenArtifactIn": "_artifactregistry_60_MavenArtifactIn",
        "MavenArtifactOut": "_artifactregistry_61_MavenArtifactOut",
        "KfpArtifactIn": "_artifactregistry_62_KfpArtifactIn",
        "KfpArtifactOut": "_artifactregistry_63_KfpArtifactOut",
        "TestIamPermissionsResponseIn": "_artifactregistry_64_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_artifactregistry_65_TestIamPermissionsResponseOut",
        "ImportYumArtifactsGcsSourceIn": "_artifactregistry_66_ImportYumArtifactsGcsSourceIn",
        "ImportYumArtifactsGcsSourceOut": "_artifactregistry_67_ImportYumArtifactsGcsSourceOut",
        "PythonPackageIn": "_artifactregistry_68_PythonPackageIn",
        "PythonPackageOut": "_artifactregistry_69_PythonPackageOut",
        "ImportGoogetArtifactsRequestIn": "_artifactregistry_70_ImportGoogetArtifactsRequestIn",
        "ImportGoogetArtifactsRequestOut": "_artifactregistry_71_ImportGoogetArtifactsRequestOut",
        "ListNpmPackagesResponseIn": "_artifactregistry_72_ListNpmPackagesResponseIn",
        "ListNpmPackagesResponseOut": "_artifactregistry_73_ListNpmPackagesResponseOut",
        "ListRepositoriesResponseIn": "_artifactregistry_74_ListRepositoriesResponseIn",
        "ListRepositoriesResponseOut": "_artifactregistry_75_ListRepositoriesResponseOut",
        "UploadAptArtifactResponseIn": "_artifactregistry_76_UploadAptArtifactResponseIn",
        "UploadAptArtifactResponseOut": "_artifactregistry_77_UploadAptArtifactResponseOut",
        "GoogleDevtoolsArtifactregistryV1FileIn": "_artifactregistry_78_GoogleDevtoolsArtifactregistryV1FileIn",
        "GoogleDevtoolsArtifactregistryV1FileOut": "_artifactregistry_79_GoogleDevtoolsArtifactregistryV1FileOut",
        "LocationIn": "_artifactregistry_80_LocationIn",
        "LocationOut": "_artifactregistry_81_LocationOut",
        "EmptyIn": "_artifactregistry_82_EmptyIn",
        "EmptyOut": "_artifactregistry_83_EmptyOut",
        "UploadGoogetArtifactMetadataIn": "_artifactregistry_84_UploadGoogetArtifactMetadataIn",
        "UploadGoogetArtifactMetadataOut": "_artifactregistry_85_UploadGoogetArtifactMetadataOut",
        "YumArtifactIn": "_artifactregistry_86_YumArtifactIn",
        "YumArtifactOut": "_artifactregistry_87_YumArtifactOut",
        "ListPythonPackagesResponseIn": "_artifactregistry_88_ListPythonPackagesResponseIn",
        "ListPythonPackagesResponseOut": "_artifactregistry_89_ListPythonPackagesResponseOut",
        "ImportGoogetArtifactsResponseIn": "_artifactregistry_90_ImportGoogetArtifactsResponseIn",
        "ImportGoogetArtifactsResponseOut": "_artifactregistry_91_ImportGoogetArtifactsResponseOut",
        "HashIn": "_artifactregistry_92_HashIn",
        "HashOut": "_artifactregistry_93_HashOut",
        "UploadYumArtifactResponseIn": "_artifactregistry_94_UploadYumArtifactResponseIn",
        "UploadYumArtifactResponseOut": "_artifactregistry_95_UploadYumArtifactResponseOut",
        "UploadAptArtifactRequestIn": "_artifactregistry_96_UploadAptArtifactRequestIn",
        "UploadAptArtifactRequestOut": "_artifactregistry_97_UploadAptArtifactRequestOut",
        "DockerRepositoryIn": "_artifactregistry_98_DockerRepositoryIn",
        "DockerRepositoryOut": "_artifactregistry_99_DockerRepositoryOut",
        "UploadGoogetArtifactRequestIn": "_artifactregistry_100_UploadGoogetArtifactRequestIn",
        "UploadGoogetArtifactRequestOut": "_artifactregistry_101_UploadGoogetArtifactRequestOut",
        "TestIamPermissionsRequestIn": "_artifactregistry_102_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_artifactregistry_103_TestIamPermissionsRequestOut",
        "UploadGoModuleMediaResponseIn": "_artifactregistry_104_UploadGoModuleMediaResponseIn",
        "UploadGoModuleMediaResponseOut": "_artifactregistry_105_UploadGoModuleMediaResponseOut",
        "UploadAptArtifactMetadataIn": "_artifactregistry_106_UploadAptArtifactMetadataIn",
        "UploadAptArtifactMetadataOut": "_artifactregistry_107_UploadAptArtifactMetadataOut",
        "PackageIn": "_artifactregistry_108_PackageIn",
        "PackageOut": "_artifactregistry_109_PackageOut",
        "UploadYumArtifactMediaResponseIn": "_artifactregistry_110_UploadYumArtifactMediaResponseIn",
        "UploadYumArtifactMediaResponseOut": "_artifactregistry_111_UploadYumArtifactMediaResponseOut",
        "ExprIn": "_artifactregistry_112_ExprIn",
        "ExprOut": "_artifactregistry_113_ExprOut",
        "ImportAptArtifactsRequestIn": "_artifactregistry_114_ImportAptArtifactsRequestIn",
        "ImportAptArtifactsRequestOut": "_artifactregistry_115_ImportAptArtifactsRequestOut",
        "ImportYumArtifactsErrorInfoIn": "_artifactregistry_116_ImportYumArtifactsErrorInfoIn",
        "ImportYumArtifactsErrorInfoOut": "_artifactregistry_117_ImportYumArtifactsErrorInfoOut",
        "ListMavenArtifactsResponseIn": "_artifactregistry_118_ListMavenArtifactsResponseIn",
        "ListMavenArtifactsResponseOut": "_artifactregistry_119_ListMavenArtifactsResponseOut",
        "ImportAptArtifactsErrorInfoIn": "_artifactregistry_120_ImportAptArtifactsErrorInfoIn",
        "ImportAptArtifactsErrorInfoOut": "_artifactregistry_121_ImportAptArtifactsErrorInfoOut",
        "ImportGoogetArtifactsGcsSourceIn": "_artifactregistry_122_ImportGoogetArtifactsGcsSourceIn",
        "ImportGoogetArtifactsGcsSourceOut": "_artifactregistry_123_ImportGoogetArtifactsGcsSourceOut",
        "ImportYumArtifactsRequestIn": "_artifactregistry_124_ImportYumArtifactsRequestIn",
        "ImportYumArtifactsRequestOut": "_artifactregistry_125_ImportYumArtifactsRequestOut",
        "BindingIn": "_artifactregistry_126_BindingIn",
        "BindingOut": "_artifactregistry_127_BindingOut",
        "UploadGoogetArtifactMediaResponseIn": "_artifactregistry_128_UploadGoogetArtifactMediaResponseIn",
        "UploadGoogetArtifactMediaResponseOut": "_artifactregistry_129_UploadGoogetArtifactMediaResponseOut",
        "ImportAptArtifactsResponseIn": "_artifactregistry_130_ImportAptArtifactsResponseIn",
        "ImportAptArtifactsResponseOut": "_artifactregistry_131_ImportAptArtifactsResponseOut",
        "GoModuleIn": "_artifactregistry_132_GoModuleIn",
        "GoModuleOut": "_artifactregistry_133_GoModuleOut",
        "MavenRepositoryConfigIn": "_artifactregistry_134_MavenRepositoryConfigIn",
        "MavenRepositoryConfigOut": "_artifactregistry_135_MavenRepositoryConfigOut",
        "ListDockerImagesResponseIn": "_artifactregistry_136_ListDockerImagesResponseIn",
        "ListDockerImagesResponseOut": "_artifactregistry_137_ListDockerImagesResponseOut",
        "OperationMetadataIn": "_artifactregistry_138_OperationMetadataIn",
        "OperationMetadataOut": "_artifactregistry_139_OperationMetadataOut",
        "PolicyIn": "_artifactregistry_140_PolicyIn",
        "PolicyOut": "_artifactregistry_141_PolicyOut",
        "NpmPackageIn": "_artifactregistry_142_NpmPackageIn",
        "NpmPackageOut": "_artifactregistry_143_NpmPackageOut",
        "UpstreamPolicyIn": "_artifactregistry_144_UpstreamPolicyIn",
        "UpstreamPolicyOut": "_artifactregistry_145_UpstreamPolicyOut",
        "PythonRepositoryIn": "_artifactregistry_146_PythonRepositoryIn",
        "PythonRepositoryOut": "_artifactregistry_147_PythonRepositoryOut",
        "ListFilesResponseIn": "_artifactregistry_148_ListFilesResponseIn",
        "ListFilesResponseOut": "_artifactregistry_149_ListFilesResponseOut",
        "StatusIn": "_artifactregistry_150_StatusIn",
        "StatusOut": "_artifactregistry_151_StatusOut",
        "MavenRepositoryIn": "_artifactregistry_152_MavenRepositoryIn",
        "MavenRepositoryOut": "_artifactregistry_153_MavenRepositoryOut",
        "VPCSCConfigIn": "_artifactregistry_154_VPCSCConfigIn",
        "VPCSCConfigOut": "_artifactregistry_155_VPCSCConfigOut",
        "TagIn": "_artifactregistry_156_TagIn",
        "TagOut": "_artifactregistry_157_TagOut",
        "RepositoryIn": "_artifactregistry_158_RepositoryIn",
        "RepositoryOut": "_artifactregistry_159_RepositoryOut",
        "GoogetArtifactIn": "_artifactregistry_160_GoogetArtifactIn",
        "GoogetArtifactOut": "_artifactregistry_161_GoogetArtifactOut",
        "UploadYumArtifactMetadataIn": "_artifactregistry_162_UploadYumArtifactMetadataIn",
        "UploadYumArtifactMetadataOut": "_artifactregistry_163_UploadYumArtifactMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["AptArtifactIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AptArtifactIn"]
    )
    types["AptArtifactOut"] = t.struct(
        {
            "controlFile": t.string().optional(),
            "component": t.string().optional(),
            "packageName": t.string().optional(),
            "name": t.string().optional(),
            "packageType": t.string().optional(),
            "architecture": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AptArtifactOut"])
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
    types["UploadGoModuleMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadGoModuleMetadataIn"]
    )
    types["UploadGoModuleMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadGoModuleMetadataOut"])
    types["UploadKfpArtifactMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadKfpArtifactMetadataIn"]
    )
    types["UploadKfpArtifactMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadKfpArtifactMetadataOut"])
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
    types["UploadKfpArtifactMediaResponseIn"] = t.struct(
        {"operation": t.proxy(renames["OperationIn"]).optional()}
    ).named(renames["UploadKfpArtifactMediaResponseIn"])
    types["UploadKfpArtifactMediaResponseOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadKfpArtifactMediaResponseOut"])
    types["NpmRepositoryIn"] = t.struct(
        {"publicRepository": t.string().optional()}
    ).named(renames["NpmRepositoryIn"])
    types["NpmRepositoryOut"] = t.struct(
        {
            "publicRepository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NpmRepositoryOut"])
    types["ImportYumArtifactsResponseIn"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["ImportYumArtifactsErrorInfoIn"])
            ).optional(),
            "yumArtifacts": t.array(t.proxy(renames["YumArtifactIn"])).optional(),
        }
    ).named(renames["ImportYumArtifactsResponseIn"])
    types["ImportYumArtifactsResponseOut"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["ImportYumArtifactsErrorInfoOut"])
            ).optional(),
            "yumArtifacts": t.array(t.proxy(renames["YumArtifactOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportYumArtifactsResponseOut"])
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
    types["DockerImageIn"] = t.struct(
        {
            "mediaType": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "uploadTime": t.string().optional(),
            "name": t.string(),
            "imageSizeBytes": t.string().optional(),
            "uri": t.string(),
            "buildTime": t.string().optional(),
        }
    ).named(renames["DockerImageIn"])
    types["DockerImageOut"] = t.struct(
        {
            "mediaType": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "uploadTime": t.string().optional(),
            "name": t.string(),
            "imageSizeBytes": t.string().optional(),
            "uri": t.string(),
            "buildTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DockerImageOut"])
    types["VersionIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "relatedTags": t.array(t.proxy(renames["TagIn"])).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "relatedTags": t.array(t.proxy(renames["TagOut"])).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
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
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["UploadYumArtifactRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadYumArtifactRequestIn"]
    )
    types["UploadYumArtifactRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadYumArtifactRequestOut"])
    types["ImportAptArtifactsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportAptArtifactsMetadataIn"])
    types["ImportAptArtifactsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportAptArtifactsMetadataOut"])
    types["ImportGoogetArtifactsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportGoogetArtifactsMetadataIn"])
    types["ImportGoogetArtifactsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportGoogetArtifactsMetadataOut"])
    types["UploadAptArtifactMediaResponseIn"] = t.struct(
        {"operation": t.proxy(renames["OperationIn"]).optional()}
    ).named(renames["UploadAptArtifactMediaResponseIn"])
    types["UploadAptArtifactMediaResponseOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadAptArtifactMediaResponseOut"])
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
    types["UploadGoModuleRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadGoModuleRequestIn"]
    )
    types["UploadGoModuleRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadGoModuleRequestOut"])
    types["RemoteRepositoryConfigIn"] = t.struct(
        {
            "npmRepository": t.proxy(renames["NpmRepositoryIn"]).optional(),
            "description": t.string().optional(),
            "pythonRepository": t.proxy(renames["PythonRepositoryIn"]).optional(),
            "dockerRepository": t.proxy(renames["DockerRepositoryIn"]).optional(),
            "mavenRepository": t.proxy(renames["MavenRepositoryIn"]).optional(),
        }
    ).named(renames["RemoteRepositoryConfigIn"])
    types["RemoteRepositoryConfigOut"] = t.struct(
        {
            "npmRepository": t.proxy(renames["NpmRepositoryOut"]).optional(),
            "description": t.string().optional(),
            "pythonRepository": t.proxy(renames["PythonRepositoryOut"]).optional(),
            "dockerRepository": t.proxy(renames["DockerRepositoryOut"]).optional(),
            "mavenRepository": t.proxy(renames["MavenRepositoryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoteRepositoryConfigOut"])
    types["ImportYumArtifactsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportYumArtifactsMetadataIn"])
    types["ImportYumArtifactsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportYumArtifactsMetadataOut"])
    types["DockerRepositoryConfigIn"] = t.struct(
        {"immutableTags": t.boolean().optional()}
    ).named(renames["DockerRepositoryConfigIn"])
    types["DockerRepositoryConfigOut"] = t.struct(
        {
            "immutableTags": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DockerRepositoryConfigOut"])
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
    types["MavenArtifactIn"] = t.struct(
        {
            "name": t.string(),
            "artifactId": t.string().optional(),
            "version": t.string().optional(),
            "groupId": t.string().optional(),
            "pomUri": t.string(),
        }
    ).named(renames["MavenArtifactIn"])
    types["MavenArtifactOut"] = t.struct(
        {
            "name": t.string(),
            "updateTime": t.string().optional(),
            "artifactId": t.string().optional(),
            "createTime": t.string().optional(),
            "version": t.string().optional(),
            "groupId": t.string().optional(),
            "pomUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MavenArtifactOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["PythonPackageIn"] = t.struct(
        {
            "name": t.string(),
            "uri": t.string(),
            "packageName": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["PythonPackageIn"])
    types["PythonPackageOut"] = t.struct(
        {
            "name": t.string(),
            "updateTime": t.string().optional(),
            "uri": t.string(),
            "createTime": t.string().optional(),
            "packageName": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonPackageOut"])
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
    types["ListNpmPackagesResponseIn"] = t.struct(
        {
            "npmPackages": t.array(t.proxy(renames["NpmPackageIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListNpmPackagesResponseIn"])
    types["ListNpmPackagesResponseOut"] = t.struct(
        {
            "npmPackages": t.array(t.proxy(renames["NpmPackageOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNpmPackagesResponseOut"])
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
    types["UploadAptArtifactResponseIn"] = t.struct(
        {"aptArtifacts": t.array(t.proxy(renames["AptArtifactIn"])).optional()}
    ).named(renames["UploadAptArtifactResponseIn"])
    types["UploadAptArtifactResponseOut"] = t.struct(
        {
            "aptArtifacts": t.array(t.proxy(renames["AptArtifactOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadAptArtifactResponseOut"])
    types["GoogleDevtoolsArtifactregistryV1FileIn"] = t.struct(
        {
            "hashes": t.array(t.proxy(renames["HashIn"])).optional(),
            "name": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "owner": t.string().optional(),
        }
    ).named(renames["GoogleDevtoolsArtifactregistryV1FileIn"])
    types["GoogleDevtoolsArtifactregistryV1FileOut"] = t.struct(
        {
            "hashes": t.array(t.proxy(renames["HashOut"])).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "fetchTime": t.string().optional(),
            "owner": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDevtoolsArtifactregistryV1FileOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["UploadGoogetArtifactMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UploadGoogetArtifactMetadataIn"])
    types["UploadGoogetArtifactMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadGoogetArtifactMetadataOut"])
    types["YumArtifactIn"] = t.struct({"_": t.string().optional()}).named(
        renames["YumArtifactIn"]
    )
    types["YumArtifactOut"] = t.struct(
        {
            "name": t.string().optional(),
            "packageType": t.string().optional(),
            "architecture": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YumArtifactOut"])
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
    types["UploadYumArtifactResponseIn"] = t.struct(
        {"yumArtifacts": t.array(t.proxy(renames["YumArtifactIn"])).optional()}
    ).named(renames["UploadYumArtifactResponseIn"])
    types["UploadYumArtifactResponseOut"] = t.struct(
        {
            "yumArtifacts": t.array(t.proxy(renames["YumArtifactOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadYumArtifactResponseOut"])
    types["UploadAptArtifactRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadAptArtifactRequestIn"]
    )
    types["UploadAptArtifactRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadAptArtifactRequestOut"])
    types["DockerRepositoryIn"] = t.struct(
        {"publicRepository": t.string().optional()}
    ).named(renames["DockerRepositoryIn"])
    types["DockerRepositoryOut"] = t.struct(
        {
            "publicRepository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DockerRepositoryOut"])
    types["UploadGoogetArtifactRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UploadGoogetArtifactRequestIn"])
    types["UploadGoogetArtifactRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadGoogetArtifactRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["UploadGoModuleMediaResponseIn"] = t.struct(
        {"operation": t.proxy(renames["OperationIn"]).optional()}
    ).named(renames["UploadGoModuleMediaResponseIn"])
    types["UploadGoModuleMediaResponseOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadGoModuleMediaResponseOut"])
    types["UploadAptArtifactMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadAptArtifactMetadataIn"]
    )
    types["UploadAptArtifactMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadAptArtifactMetadataOut"])
    types["PackageIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["PackageIn"])
    types["PackageOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
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
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ImportAptArtifactsRequestIn"] = t.struct(
        {"gcsSource": t.proxy(renames["ImportAptArtifactsGcsSourceIn"]).optional()}
    ).named(renames["ImportAptArtifactsRequestIn"])
    types["ImportAptArtifactsRequestOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["ImportAptArtifactsGcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportAptArtifactsRequestOut"])
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
    types["ImportYumArtifactsRequestIn"] = t.struct(
        {"gcsSource": t.proxy(renames["ImportYumArtifactsGcsSourceIn"]).optional()}
    ).named(renames["ImportYumArtifactsRequestIn"])
    types["ImportYumArtifactsRequestOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["ImportYumArtifactsGcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportYumArtifactsRequestOut"])
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
    types["UploadGoogetArtifactMediaResponseIn"] = t.struct(
        {"operation": t.proxy(renames["OperationIn"]).optional()}
    ).named(renames["UploadGoogetArtifactMediaResponseIn"])
    types["UploadGoogetArtifactMediaResponseOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadGoogetArtifactMediaResponseOut"])
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
    types["GoModuleIn"] = t.struct(
        {"version": t.string().optional(), "name": t.string().optional()}
    ).named(renames["GoModuleIn"])
    types["GoModuleOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "version": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoModuleOut"])
    types["MavenRepositoryConfigIn"] = t.struct(
        {
            "allowSnapshotOverwrites": t.boolean().optional(),
            "versionPolicy": t.string().optional(),
        }
    ).named(renames["MavenRepositoryConfigIn"])
    types["MavenRepositoryConfigOut"] = t.struct(
        {
            "allowSnapshotOverwrites": t.boolean().optional(),
            "versionPolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MavenRepositoryConfigOut"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OperationMetadataOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["NpmPackageIn"] = t.struct(
        {
            "version": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "name": t.string(),
            "packageName": t.string().optional(),
        }
    ).named(renames["NpmPackageIn"])
    types["NpmPackageOut"] = t.struct(
        {
            "version": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "name": t.string(),
            "updateTime": t.string().optional(),
            "packageName": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NpmPackageOut"])
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
    types["PythonRepositoryIn"] = t.struct(
        {"publicRepository": t.string().optional()}
    ).named(renames["PythonRepositoryIn"])
    types["PythonRepositoryOut"] = t.struct(
        {
            "publicRepository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonRepositoryOut"])
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
    types["MavenRepositoryIn"] = t.struct(
        {"publicRepository": t.string().optional()}
    ).named(renames["MavenRepositoryIn"])
    types["MavenRepositoryOut"] = t.struct(
        {
            "publicRepository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MavenRepositoryOut"])
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
    types["RepositoryIn"] = t.struct(
        {
            "dockerConfig": t.proxy(renames["DockerRepositoryConfigIn"]).optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "mavenConfig": t.proxy(renames["MavenRepositoryConfigIn"]).optional(),
            "name": t.string().optional(),
            "virtualRepositoryConfig": t.proxy(
                renames["VirtualRepositoryConfigIn"]
            ).optional(),
            "mode": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "format": t.string().optional(),
            "remoteRepositoryConfig": t.proxy(
                renames["RemoteRepositoryConfigIn"]
            ).optional(),
        }
    ).named(renames["RepositoryIn"])
    types["RepositoryOut"] = t.struct(
        {
            "satisfiesPzs": t.boolean().optional(),
            "createTime": t.string().optional(),
            "dockerConfig": t.proxy(renames["DockerRepositoryConfigOut"]).optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "mavenConfig": t.proxy(renames["MavenRepositoryConfigOut"]).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "virtualRepositoryConfig": t.proxy(
                renames["VirtualRepositoryConfigOut"]
            ).optional(),
            "sizeBytes": t.string().optional(),
            "mode": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "format": t.string().optional(),
            "remoteRepositoryConfig": t.proxy(
                renames["RemoteRepositoryConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepositoryOut"])
    types["GoogetArtifactIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogetArtifactIn"]
    )
    types["GoogetArtifactOut"] = t.struct(
        {
            "name": t.string().optional(),
            "packageName": t.string().optional(),
            "architecture": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogetArtifactOut"])
    types["UploadYumArtifactMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadYumArtifactMetadataIn"]
    )
    types["UploadYumArtifactMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadYumArtifactMetadataOut"])

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
    functions["projectsLocationsList"] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "vpcscPolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VPCSCConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGetVpcscConfig"] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "vpcscPolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VPCSCConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "vpcscPolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VPCSCConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUpdateVpcscConfig"] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "vpcscPolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VPCSCConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesTestIamPermissions"
    ] = artifactregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesGet"] = artifactregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesSetIamPolicy"] = artifactregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesGetIamPolicy"] = artifactregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesPatch"] = artifactregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesCreate"] = artifactregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesList"] = artifactregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesDelete"] = artifactregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
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
    functions["projectsLocationsRepositoriesDockerImagesList"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DockerImageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesDockerImagesGet"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DockerImageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesMavenArtifactsList"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MavenArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesMavenArtifactsGet"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MavenArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesFilesGet"] = artifactregistry.get(
        "v1/{parent}/files",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilesResponseOut"]),
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
    functions["projectsLocationsRepositoriesPackagesGet"] = artifactregistry.get(
        "v1/{parent}/packages",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPackagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesPackagesDelete"] = artifactregistry.get(
        "v1/{parent}/packages",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPackagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesPackagesList"] = artifactregistry.get(
        "v1/{parent}/packages",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPackagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesPackagesVersionsList"
    ] = artifactregistry.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesPackagesVersionsDelete"
    ] = artifactregistry.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string().optional(),
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
                "view": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesPackagesTagsCreate"
    ] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "version": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesPackagesTagsDelete"
    ] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "version": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesPackagesTagsGet"] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "version": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesPackagesTagsList"] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "version": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesPackagesTagsPatch"
    ] = artifactregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "version": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TagOut"]),
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
    functions["projectsLocationsRepositoriesGoModulesUpload"] = artifactregistry.post(
        "v1/{parent}/goModules:create",
        t.struct(
            {
                "parent": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadGoModuleMediaResponseOut"]),
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
