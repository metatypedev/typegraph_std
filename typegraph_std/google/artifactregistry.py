from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_artifactregistry() -> Import:
    artifactregistry = HTTPRuntime("https://artifactregistry.googleapis.com/")

    renames = {
        "ErrorResponse": "_artifactregistry_1_ErrorResponse",
        "EmptyIn": "_artifactregistry_2_EmptyIn",
        "EmptyOut": "_artifactregistry_3_EmptyOut",
        "PythonPackageIn": "_artifactregistry_4_PythonPackageIn",
        "PythonPackageOut": "_artifactregistry_5_PythonPackageOut",
        "TestIamPermissionsRequestIn": "_artifactregistry_6_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_artifactregistry_7_TestIamPermissionsRequestOut",
        "BindingIn": "_artifactregistry_8_BindingIn",
        "BindingOut": "_artifactregistry_9_BindingOut",
        "UploadKfpArtifactMetadataIn": "_artifactregistry_10_UploadKfpArtifactMetadataIn",
        "UploadKfpArtifactMetadataOut": "_artifactregistry_11_UploadKfpArtifactMetadataOut",
        "YumArtifactIn": "_artifactregistry_12_YumArtifactIn",
        "YumArtifactOut": "_artifactregistry_13_YumArtifactOut",
        "UploadYumArtifactMetadataIn": "_artifactregistry_14_UploadYumArtifactMetadataIn",
        "UploadYumArtifactMetadataOut": "_artifactregistry_15_UploadYumArtifactMetadataOut",
        "ImportGoogetArtifactsErrorInfoIn": "_artifactregistry_16_ImportGoogetArtifactsErrorInfoIn",
        "ImportGoogetArtifactsErrorInfoOut": "_artifactregistry_17_ImportGoogetArtifactsErrorInfoOut",
        "UploadKfpArtifactMediaResponseIn": "_artifactregistry_18_UploadKfpArtifactMediaResponseIn",
        "UploadKfpArtifactMediaResponseOut": "_artifactregistry_19_UploadKfpArtifactMediaResponseOut",
        "UploadAptArtifactMetadataIn": "_artifactregistry_20_UploadAptArtifactMetadataIn",
        "UploadAptArtifactMetadataOut": "_artifactregistry_21_UploadAptArtifactMetadataOut",
        "ImportYumArtifactsGcsSourceIn": "_artifactregistry_22_ImportYumArtifactsGcsSourceIn",
        "ImportYumArtifactsGcsSourceOut": "_artifactregistry_23_ImportYumArtifactsGcsSourceOut",
        "OperationMetadataIn": "_artifactregistry_24_OperationMetadataIn",
        "OperationMetadataOut": "_artifactregistry_25_OperationMetadataOut",
        "VirtualRepositoryConfigIn": "_artifactregistry_26_VirtualRepositoryConfigIn",
        "VirtualRepositoryConfigOut": "_artifactregistry_27_VirtualRepositoryConfigOut",
        "ListDockerImagesResponseIn": "_artifactregistry_28_ListDockerImagesResponseIn",
        "ListDockerImagesResponseOut": "_artifactregistry_29_ListDockerImagesResponseOut",
        "PolicyIn": "_artifactregistry_30_PolicyIn",
        "PolicyOut": "_artifactregistry_31_PolicyOut",
        "PythonRepositoryIn": "_artifactregistry_32_PythonRepositoryIn",
        "PythonRepositoryOut": "_artifactregistry_33_PythonRepositoryOut",
        "TagIn": "_artifactregistry_34_TagIn",
        "TagOut": "_artifactregistry_35_TagOut",
        "ImportAptArtifactsRequestIn": "_artifactregistry_36_ImportAptArtifactsRequestIn",
        "ImportAptArtifactsRequestOut": "_artifactregistry_37_ImportAptArtifactsRequestOut",
        "ImportYumArtifactsResponseIn": "_artifactregistry_38_ImportYumArtifactsResponseIn",
        "ImportYumArtifactsResponseOut": "_artifactregistry_39_ImportYumArtifactsResponseOut",
        "ProjectSettingsIn": "_artifactregistry_40_ProjectSettingsIn",
        "ProjectSettingsOut": "_artifactregistry_41_ProjectSettingsOut",
        "ListPythonPackagesResponseIn": "_artifactregistry_42_ListPythonPackagesResponseIn",
        "ListPythonPackagesResponseOut": "_artifactregistry_43_ListPythonPackagesResponseOut",
        "ListLocationsResponseIn": "_artifactregistry_44_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_artifactregistry_45_ListLocationsResponseOut",
        "ListNpmPackagesResponseIn": "_artifactregistry_46_ListNpmPackagesResponseIn",
        "ListNpmPackagesResponseOut": "_artifactregistry_47_ListNpmPackagesResponseOut",
        "AptArtifactIn": "_artifactregistry_48_AptArtifactIn",
        "AptArtifactOut": "_artifactregistry_49_AptArtifactOut",
        "StatusIn": "_artifactregistry_50_StatusIn",
        "StatusOut": "_artifactregistry_51_StatusOut",
        "ImportYumArtifactsMetadataIn": "_artifactregistry_52_ImportYumArtifactsMetadataIn",
        "ImportYumArtifactsMetadataOut": "_artifactregistry_53_ImportYumArtifactsMetadataOut",
        "HashIn": "_artifactregistry_54_HashIn",
        "HashOut": "_artifactregistry_55_HashOut",
        "UploadKfpArtifactRequestIn": "_artifactregistry_56_UploadKfpArtifactRequestIn",
        "UploadKfpArtifactRequestOut": "_artifactregistry_57_UploadKfpArtifactRequestOut",
        "NpmPackageIn": "_artifactregistry_58_NpmPackageIn",
        "NpmPackageOut": "_artifactregistry_59_NpmPackageOut",
        "KfpArtifactIn": "_artifactregistry_60_KfpArtifactIn",
        "KfpArtifactOut": "_artifactregistry_61_KfpArtifactOut",
        "ListTagsResponseIn": "_artifactregistry_62_ListTagsResponseIn",
        "ListTagsResponseOut": "_artifactregistry_63_ListTagsResponseOut",
        "MavenRepositoryIn": "_artifactregistry_64_MavenRepositoryIn",
        "MavenRepositoryOut": "_artifactregistry_65_MavenRepositoryOut",
        "MavenArtifactIn": "_artifactregistry_66_MavenArtifactIn",
        "MavenArtifactOut": "_artifactregistry_67_MavenArtifactOut",
        "ListMavenArtifactsResponseIn": "_artifactregistry_68_ListMavenArtifactsResponseIn",
        "ListMavenArtifactsResponseOut": "_artifactregistry_69_ListMavenArtifactsResponseOut",
        "ImportAptArtifactsGcsSourceIn": "_artifactregistry_70_ImportAptArtifactsGcsSourceIn",
        "ImportAptArtifactsGcsSourceOut": "_artifactregistry_71_ImportAptArtifactsGcsSourceOut",
        "ListPackagesResponseIn": "_artifactregistry_72_ListPackagesResponseIn",
        "ListPackagesResponseOut": "_artifactregistry_73_ListPackagesResponseOut",
        "LocationIn": "_artifactregistry_74_LocationIn",
        "LocationOut": "_artifactregistry_75_LocationOut",
        "UploadYumArtifactRequestIn": "_artifactregistry_76_UploadYumArtifactRequestIn",
        "UploadYumArtifactRequestOut": "_artifactregistry_77_UploadYumArtifactRequestOut",
        "UploadGoogetArtifactResponseIn": "_artifactregistry_78_UploadGoogetArtifactResponseIn",
        "UploadGoogetArtifactResponseOut": "_artifactregistry_79_UploadGoogetArtifactResponseOut",
        "VPCSCConfigIn": "_artifactregistry_80_VPCSCConfigIn",
        "VPCSCConfigOut": "_artifactregistry_81_VPCSCConfigOut",
        "UploadYumArtifactResponseIn": "_artifactregistry_82_UploadYumArtifactResponseIn",
        "UploadYumArtifactResponseOut": "_artifactregistry_83_UploadYumArtifactResponseOut",
        "TestIamPermissionsResponseIn": "_artifactregistry_84_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_artifactregistry_85_TestIamPermissionsResponseOut",
        "UploadAptArtifactMediaResponseIn": "_artifactregistry_86_UploadAptArtifactMediaResponseIn",
        "UploadAptArtifactMediaResponseOut": "_artifactregistry_87_UploadAptArtifactMediaResponseOut",
        "UpstreamPolicyIn": "_artifactregistry_88_UpstreamPolicyIn",
        "UpstreamPolicyOut": "_artifactregistry_89_UpstreamPolicyOut",
        "ExprIn": "_artifactregistry_90_ExprIn",
        "ExprOut": "_artifactregistry_91_ExprOut",
        "RepositoryIn": "_artifactregistry_92_RepositoryIn",
        "RepositoryOut": "_artifactregistry_93_RepositoryOut",
        "DockerRepositoryIn": "_artifactregistry_94_DockerRepositoryIn",
        "DockerRepositoryOut": "_artifactregistry_95_DockerRepositoryOut",
        "ImportGoogetArtifactsMetadataIn": "_artifactregistry_96_ImportGoogetArtifactsMetadataIn",
        "ImportGoogetArtifactsMetadataOut": "_artifactregistry_97_ImportGoogetArtifactsMetadataOut",
        "VersionIn": "_artifactregistry_98_VersionIn",
        "VersionOut": "_artifactregistry_99_VersionOut",
        "PackageIn": "_artifactregistry_100_PackageIn",
        "PackageOut": "_artifactregistry_101_PackageOut",
        "DockerRepositoryConfigIn": "_artifactregistry_102_DockerRepositoryConfigIn",
        "DockerRepositoryConfigOut": "_artifactregistry_103_DockerRepositoryConfigOut",
        "ListRepositoriesResponseIn": "_artifactregistry_104_ListRepositoriesResponseIn",
        "ListRepositoriesResponseOut": "_artifactregistry_105_ListRepositoriesResponseOut",
        "ImportYumArtifactsRequestIn": "_artifactregistry_106_ImportYumArtifactsRequestIn",
        "ImportYumArtifactsRequestOut": "_artifactregistry_107_ImportYumArtifactsRequestOut",
        "ListFilesResponseIn": "_artifactregistry_108_ListFilesResponseIn",
        "ListFilesResponseOut": "_artifactregistry_109_ListFilesResponseOut",
        "BatchDeleteVersionsMetadataIn": "_artifactregistry_110_BatchDeleteVersionsMetadataIn",
        "BatchDeleteVersionsMetadataOut": "_artifactregistry_111_BatchDeleteVersionsMetadataOut",
        "ImportGoogetArtifactsGcsSourceIn": "_artifactregistry_112_ImportGoogetArtifactsGcsSourceIn",
        "ImportGoogetArtifactsGcsSourceOut": "_artifactregistry_113_ImportGoogetArtifactsGcsSourceOut",
        "ListVersionsResponseIn": "_artifactregistry_114_ListVersionsResponseIn",
        "ListVersionsResponseOut": "_artifactregistry_115_ListVersionsResponseOut",
        "ImportAptArtifactsResponseIn": "_artifactregistry_116_ImportAptArtifactsResponseIn",
        "ImportAptArtifactsResponseOut": "_artifactregistry_117_ImportAptArtifactsResponseOut",
        "ImportAptArtifactsErrorInfoIn": "_artifactregistry_118_ImportAptArtifactsErrorInfoIn",
        "ImportAptArtifactsErrorInfoOut": "_artifactregistry_119_ImportAptArtifactsErrorInfoOut",
        "DockerImageIn": "_artifactregistry_120_DockerImageIn",
        "DockerImageOut": "_artifactregistry_121_DockerImageOut",
        "UploadAptArtifactRequestIn": "_artifactregistry_122_UploadAptArtifactRequestIn",
        "UploadAptArtifactRequestOut": "_artifactregistry_123_UploadAptArtifactRequestOut",
        "SetIamPolicyRequestIn": "_artifactregistry_124_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_artifactregistry_125_SetIamPolicyRequestOut",
        "OperationIn": "_artifactregistry_126_OperationIn",
        "OperationOut": "_artifactregistry_127_OperationOut",
        "GoogetArtifactIn": "_artifactregistry_128_GoogetArtifactIn",
        "GoogetArtifactOut": "_artifactregistry_129_GoogetArtifactOut",
        "MavenRepositoryConfigIn": "_artifactregistry_130_MavenRepositoryConfigIn",
        "MavenRepositoryConfigOut": "_artifactregistry_131_MavenRepositoryConfigOut",
        "ImportYumArtifactsErrorInfoIn": "_artifactregistry_132_ImportYumArtifactsErrorInfoIn",
        "ImportYumArtifactsErrorInfoOut": "_artifactregistry_133_ImportYumArtifactsErrorInfoOut",
        "RemoteRepositoryConfigIn": "_artifactregistry_134_RemoteRepositoryConfigIn",
        "RemoteRepositoryConfigOut": "_artifactregistry_135_RemoteRepositoryConfigOut",
        "UploadYumArtifactMediaResponseIn": "_artifactregistry_136_UploadYumArtifactMediaResponseIn",
        "UploadYumArtifactMediaResponseOut": "_artifactregistry_137_UploadYumArtifactMediaResponseOut",
        "ImportGoogetArtifactsRequestIn": "_artifactregistry_138_ImportGoogetArtifactsRequestIn",
        "ImportGoogetArtifactsRequestOut": "_artifactregistry_139_ImportGoogetArtifactsRequestOut",
        "ImportAptArtifactsMetadataIn": "_artifactregistry_140_ImportAptArtifactsMetadataIn",
        "ImportAptArtifactsMetadataOut": "_artifactregistry_141_ImportAptArtifactsMetadataOut",
        "ImportGoogetArtifactsResponseIn": "_artifactregistry_142_ImportGoogetArtifactsResponseIn",
        "ImportGoogetArtifactsResponseOut": "_artifactregistry_143_ImportGoogetArtifactsResponseOut",
        "NpmRepositoryIn": "_artifactregistry_144_NpmRepositoryIn",
        "NpmRepositoryOut": "_artifactregistry_145_NpmRepositoryOut",
        "UploadGoogetArtifactRequestIn": "_artifactregistry_146_UploadGoogetArtifactRequestIn",
        "UploadGoogetArtifactRequestOut": "_artifactregistry_147_UploadGoogetArtifactRequestOut",
        "UploadGoogetArtifactMediaResponseIn": "_artifactregistry_148_UploadGoogetArtifactMediaResponseIn",
        "UploadGoogetArtifactMediaResponseOut": "_artifactregistry_149_UploadGoogetArtifactMediaResponseOut",
        "UploadGoogetArtifactMetadataIn": "_artifactregistry_150_UploadGoogetArtifactMetadataIn",
        "UploadGoogetArtifactMetadataOut": "_artifactregistry_151_UploadGoogetArtifactMetadataOut",
        "UploadAptArtifactResponseIn": "_artifactregistry_152_UploadAptArtifactResponseIn",
        "UploadAptArtifactResponseOut": "_artifactregistry_153_UploadAptArtifactResponseOut",
        "GoogleDevtoolsArtifactregistryV1FileIn": "_artifactregistry_154_GoogleDevtoolsArtifactregistryV1FileIn",
        "GoogleDevtoolsArtifactregistryV1FileOut": "_artifactregistry_155_GoogleDevtoolsArtifactregistryV1FileOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["PythonPackageIn"] = t.struct(
        {
            "packageName": t.string().optional(),
            "name": t.string(),
            "uri": t.string(),
            "version": t.string().optional(),
        }
    ).named(renames["PythonPackageIn"])
    types["PythonPackageOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "name": t.string(),
            "uri": t.string(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonPackageOut"])
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
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["UploadKfpArtifactMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadKfpArtifactMetadataIn"]
    )
    types["UploadKfpArtifactMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadKfpArtifactMetadataOut"])
    types["YumArtifactIn"] = t.struct({"_": t.string().optional()}).named(
        renames["YumArtifactIn"]
    )
    types["YumArtifactOut"] = t.struct(
        {
            "packageType": t.string().optional(),
            "packageName": t.string().optional(),
            "name": t.string().optional(),
            "architecture": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["YumArtifactOut"])
    types["UploadYumArtifactMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadYumArtifactMetadataIn"]
    )
    types["UploadYumArtifactMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadYumArtifactMetadataOut"])
    types["ImportGoogetArtifactsErrorInfoIn"] = t.struct(
        {
            "gcsSource": t.proxy(
                renames["ImportGoogetArtifactsGcsSourceIn"]
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["ImportGoogetArtifactsErrorInfoIn"])
    types["ImportGoogetArtifactsErrorInfoOut"] = t.struct(
        {
            "gcsSource": t.proxy(
                renames["ImportGoogetArtifactsGcsSourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportGoogetArtifactsErrorInfoOut"])
    types["UploadKfpArtifactMediaResponseIn"] = t.struct(
        {"operation": t.proxy(renames["OperationIn"]).optional()}
    ).named(renames["UploadKfpArtifactMediaResponseIn"])
    types["UploadKfpArtifactMediaResponseOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadKfpArtifactMediaResponseOut"])
    types["UploadAptArtifactMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadAptArtifactMetadataIn"]
    )
    types["UploadAptArtifactMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadAptArtifactMetadataOut"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OperationMetadataOut"])
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
    types["PythonRepositoryIn"] = t.struct(
        {"publicRepository": t.string().optional()}
    ).named(renames["PythonRepositoryIn"])
    types["PythonRepositoryOut"] = t.struct(
        {
            "publicRepository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonRepositoryOut"])
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
    types["ImportAptArtifactsRequestIn"] = t.struct(
        {"gcsSource": t.proxy(renames["ImportAptArtifactsGcsSourceIn"]).optional()}
    ).named(renames["ImportAptArtifactsRequestIn"])
    types["ImportAptArtifactsRequestOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["ImportAptArtifactsGcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportAptArtifactsRequestOut"])
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
        {"legacyRedirectionState": t.string().optional(), "name": t.string().optional()}
    ).named(renames["ProjectSettingsIn"])
    types["ProjectSettingsOut"] = t.struct(
        {
            "legacyRedirectionState": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectSettingsOut"])
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
    types["AptArtifactIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AptArtifactIn"]
    )
    types["AptArtifactOut"] = t.struct(
        {
            "name": t.string().optional(),
            "controlFile": t.string().optional(),
            "packageType": t.string().optional(),
            "component": t.string().optional(),
            "packageName": t.string().optional(),
            "architecture": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AptArtifactOut"])
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
    types["ImportYumArtifactsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportYumArtifactsMetadataIn"])
    types["ImportYumArtifactsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportYumArtifactsMetadataOut"])
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
    types["UploadKfpArtifactRequestIn"] = t.struct(
        {"tags": t.array(t.string()).optional(), "description": t.string().optional()}
    ).named(renames["UploadKfpArtifactRequestIn"])
    types["UploadKfpArtifactRequestOut"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadKfpArtifactRequestOut"])
    types["NpmPackageIn"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "name": t.string(),
            "packageName": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["NpmPackageIn"])
    types["NpmPackageOut"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "name": t.string(),
            "createTime": t.string().optional(),
            "packageName": t.string().optional(),
            "updateTime": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NpmPackageOut"])
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
    types["MavenRepositoryIn"] = t.struct(
        {"publicRepository": t.string().optional()}
    ).named(renames["MavenRepositoryIn"])
    types["MavenRepositoryOut"] = t.struct(
        {
            "publicRepository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MavenRepositoryOut"])
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
            "artifactId": t.string().optional(),
            "version": t.string().optional(),
            "createTime": t.string().optional(),
            "groupId": t.string().optional(),
            "pomUri": t.string(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MavenArtifactOut"])
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
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["UploadYumArtifactRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadYumArtifactRequestIn"]
    )
    types["UploadYumArtifactRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadYumArtifactRequestOut"])
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
    types["VPCSCConfigIn"] = t.struct(
        {"name": t.string().optional(), "vpcscPolicy": t.string().optional()}
    ).named(renames["VPCSCConfigIn"])
    types["VPCSCConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "vpcscPolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VPCSCConfigOut"])
    types["UploadYumArtifactResponseIn"] = t.struct(
        {"yumArtifacts": t.array(t.proxy(renames["YumArtifactIn"])).optional()}
    ).named(renames["UploadYumArtifactResponseIn"])
    types["UploadYumArtifactResponseOut"] = t.struct(
        {
            "yumArtifacts": t.array(t.proxy(renames["YumArtifactOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadYumArtifactResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["UploadAptArtifactMediaResponseIn"] = t.struct(
        {"operation": t.proxy(renames["OperationIn"]).optional()}
    ).named(renames["UploadAptArtifactMediaResponseIn"])
    types["UploadAptArtifactMediaResponseOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadAptArtifactMediaResponseOut"])
    types["UpstreamPolicyIn"] = t.struct(
        {
            "id": t.string().optional(),
            "priority": t.integer().optional(),
            "repository": t.string().optional(),
        }
    ).named(renames["UpstreamPolicyIn"])
    types["UpstreamPolicyOut"] = t.struct(
        {
            "id": t.string().optional(),
            "priority": t.integer().optional(),
            "repository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpstreamPolicyOut"])
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
    types["RepositoryIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "mode": t.string().optional(),
            "mavenConfig": t.proxy(renames["MavenRepositoryConfigIn"]).optional(),
            "description": t.string().optional(),
            "remoteRepositoryConfig": t.proxy(
                renames["RemoteRepositoryConfigIn"]
            ).optional(),
            "format": t.string().optional(),
            "virtualRepositoryConfig": t.proxy(
                renames["VirtualRepositoryConfigIn"]
            ).optional(),
            "kmsKeyName": t.string().optional(),
            "dockerConfig": t.proxy(renames["DockerRepositoryConfigIn"]).optional(),
        }
    ).named(renames["RepositoryIn"])
    types["RepositoryOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "mode": t.string().optional(),
            "mavenConfig": t.proxy(renames["MavenRepositoryConfigOut"]).optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "remoteRepositoryConfig": t.proxy(
                renames["RemoteRepositoryConfigOut"]
            ).optional(),
            "sizeBytes": t.string().optional(),
            "format": t.string().optional(),
            "virtualRepositoryConfig": t.proxy(
                renames["VirtualRepositoryConfigOut"]
            ).optional(),
            "kmsKeyName": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "dockerConfig": t.proxy(renames["DockerRepositoryConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepositoryOut"])
    types["DockerRepositoryIn"] = t.struct(
        {"publicRepository": t.string().optional()}
    ).named(renames["DockerRepositoryIn"])
    types["DockerRepositoryOut"] = t.struct(
        {
            "publicRepository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DockerRepositoryOut"])
    types["ImportGoogetArtifactsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportGoogetArtifactsMetadataIn"])
    types["ImportGoogetArtifactsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportGoogetArtifactsMetadataOut"])
    types["VersionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "relatedTags": t.array(t.proxy(renames["TagIn"])).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "relatedTags": t.array(t.proxy(renames["TagOut"])).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
    types["PackageIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["PackageIn"])
    types["PackageOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageOut"])
    types["DockerRepositoryConfigIn"] = t.struct(
        {"immutableTags": t.boolean().optional()}
    ).named(renames["DockerRepositoryConfigIn"])
    types["DockerRepositoryConfigOut"] = t.struct(
        {
            "immutableTags": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DockerRepositoryConfigOut"])
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
    types["ImportYumArtifactsRequestIn"] = t.struct(
        {"gcsSource": t.proxy(renames["ImportYumArtifactsGcsSourceIn"]).optional()}
    ).named(renames["ImportYumArtifactsRequestIn"])
    types["ImportYumArtifactsRequestOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["ImportYumArtifactsGcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportYumArtifactsRequestOut"])
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
    types["BatchDeleteVersionsMetadataIn"] = t.struct(
        {"failedVersions": t.array(t.string()).optional()}
    ).named(renames["BatchDeleteVersionsMetadataIn"])
    types["BatchDeleteVersionsMetadataOut"] = t.struct(
        {
            "failedVersions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteVersionsMetadataOut"])
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
    types["DockerImageIn"] = t.struct(
        {
            "buildTime": t.string().optional(),
            "uploadTime": t.string().optional(),
            "imageSizeBytes": t.string().optional(),
            "uri": t.string(),
            "mediaType": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "name": t.string(),
        }
    ).named(renames["DockerImageIn"])
    types["DockerImageOut"] = t.struct(
        {
            "buildTime": t.string().optional(),
            "uploadTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "imageSizeBytes": t.string().optional(),
            "uri": t.string(),
            "mediaType": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DockerImageOut"])
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
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["RemoteRepositoryConfigIn"] = t.struct(
        {
            "mavenRepository": t.proxy(renames["MavenRepositoryIn"]).optional(),
            "dockerRepository": t.proxy(renames["DockerRepositoryIn"]).optional(),
            "npmRepository": t.proxy(renames["NpmRepositoryIn"]).optional(),
            "description": t.string().optional(),
            "pythonRepository": t.proxy(renames["PythonRepositoryIn"]).optional(),
        }
    ).named(renames["RemoteRepositoryConfigIn"])
    types["RemoteRepositoryConfigOut"] = t.struct(
        {
            "mavenRepository": t.proxy(renames["MavenRepositoryOut"]).optional(),
            "dockerRepository": t.proxy(renames["DockerRepositoryOut"]).optional(),
            "npmRepository": t.proxy(renames["NpmRepositoryOut"]).optional(),
            "description": t.string().optional(),
            "pythonRepository": t.proxy(renames["PythonRepositoryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoteRepositoryConfigOut"])
    types["UploadYumArtifactMediaResponseIn"] = t.struct(
        {"operation": t.proxy(renames["OperationIn"]).optional()}
    ).named(renames["UploadYumArtifactMediaResponseIn"])
    types["UploadYumArtifactMediaResponseOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadYumArtifactMediaResponseOut"])
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
    types["ImportAptArtifactsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportAptArtifactsMetadataIn"])
    types["ImportAptArtifactsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportAptArtifactsMetadataOut"])
    types["ImportGoogetArtifactsResponseIn"] = t.struct(
        {
            "googetArtifacts": t.array(t.proxy(renames["GoogetArtifactIn"])).optional(),
            "errors": t.array(
                t.proxy(renames["ImportGoogetArtifactsErrorInfoIn"])
            ).optional(),
        }
    ).named(renames["ImportGoogetArtifactsResponseIn"])
    types["ImportGoogetArtifactsResponseOut"] = t.struct(
        {
            "googetArtifacts": t.array(
                t.proxy(renames["GoogetArtifactOut"])
            ).optional(),
            "errors": t.array(
                t.proxy(renames["ImportGoogetArtifactsErrorInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportGoogetArtifactsResponseOut"])
    types["NpmRepositoryIn"] = t.struct(
        {"publicRepository": t.string().optional()}
    ).named(renames["NpmRepositoryIn"])
    types["NpmRepositoryOut"] = t.struct(
        {
            "publicRepository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NpmRepositoryOut"])
    types["UploadGoogetArtifactRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UploadGoogetArtifactRequestIn"])
    types["UploadGoogetArtifactRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadGoogetArtifactRequestOut"])
    types["UploadGoogetArtifactMediaResponseIn"] = t.struct(
        {"operation": t.proxy(renames["OperationIn"]).optional()}
    ).named(renames["UploadGoogetArtifactMediaResponseIn"])
    types["UploadGoogetArtifactMediaResponseOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadGoogetArtifactMediaResponseOut"])
    types["UploadGoogetArtifactMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UploadGoogetArtifactMetadataIn"])
    types["UploadGoogetArtifactMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadGoogetArtifactMetadataOut"])
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
            "sizeBytes": t.string().optional(),
            "owner": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleDevtoolsArtifactregistryV1FileIn"])
    types["GoogleDevtoolsArtifactregistryV1FileOut"] = t.struct(
        {
            "hashes": t.array(t.proxy(renames["HashOut"])).optional(),
            "sizeBytes": t.string().optional(),
            "owner": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "fetchTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDevtoolsArtifactregistryV1FileOut"])

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
    functions["projectsLocationsList"] = artifactregistry.get(
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
    functions["projectsLocationsOperationsGet"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
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
    functions["projectsLocationsRepositoriesList"] = artifactregistry.delete(
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
    functions[
        "projectsLocationsRepositoriesTestIamPermissions"
    ] = artifactregistry.delete(
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
    functions["projectsLocationsRepositoriesDelete"] = artifactregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
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
    functions[
        "projectsLocationsRepositoriesKfpArtifactsUpload"
    ] = artifactregistry.post(
        "v1/{parent}/kfpArtifacts:create",
        t.struct(
            {
                "parent": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadKfpArtifactMediaResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesNpmPackagesList"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NpmPackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesNpmPackagesGet"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NpmPackageOut"]),
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
    functions["projectsLocationsRepositoriesPackagesDelete"] = artifactregistry.get(
        "v1/{parent}/packages",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPackagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesPackagesGet"] = artifactregistry.get(
        "v1/{parent}/packages",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPackagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesPackagesVersionsList"
    ] = artifactregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesPackagesVersionsGet"
    ] = artifactregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRepositoriesPackagesVersionsDelete"
    ] = artifactregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
    functions["projectsLocationsRepositoriesFilesList"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleDevtoolsArtifactregistryV1FileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRepositoriesFilesGet"] = artifactregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleDevtoolsArtifactregistryV1FileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="artifactregistry",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
