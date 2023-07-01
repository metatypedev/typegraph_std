from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_ondemandscanning():
    ondemandscanning = HTTPRuntime("https://ondemandscanning.googleapis.com/")

    renames = {
        "ErrorResponse": "_ondemandscanning_1_ErrorResponse",
        "UpgradeDistributionIn": "_ondemandscanning_2_UpgradeDistributionIn",
        "UpgradeDistributionOut": "_ondemandscanning_3_UpgradeDistributionOut",
        "DeploymentOccurrenceIn": "_ondemandscanning_4_DeploymentOccurrenceIn",
        "DeploymentOccurrenceOut": "_ondemandscanning_5_DeploymentOccurrenceOut",
        "ImageOccurrenceIn": "_ondemandscanning_6_ImageOccurrenceIn",
        "ImageOccurrenceOut": "_ondemandscanning_7_ImageOccurrenceOut",
        "ArtifactIn": "_ondemandscanning_8_ArtifactIn",
        "ArtifactOut": "_ondemandscanning_9_ArtifactOut",
        "FileHashesIn": "_ondemandscanning_10_FileHashesIn",
        "FileHashesOut": "_ondemandscanning_11_FileHashesOut",
        "MaterialIn": "_ondemandscanning_12_MaterialIn",
        "MaterialOut": "_ondemandscanning_13_MaterialOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn": "_ondemandscanning_14_GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut": "_ondemandscanning_15_GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn": "_ondemandscanning_16_GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut": "_ondemandscanning_17_GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut",
        "SubjectIn": "_ondemandscanning_18_SubjectIn",
        "SubjectOut": "_ondemandscanning_19_SubjectOut",
        "EnvelopeIn": "_ondemandscanning_20_EnvelopeIn",
        "EnvelopeOut": "_ondemandscanning_21_EnvelopeOut",
        "CompletenessIn": "_ondemandscanning_22_CompletenessIn",
        "CompletenessOut": "_ondemandscanning_23_CompletenessOut",
        "SlsaRecipeIn": "_ondemandscanning_24_SlsaRecipeIn",
        "SlsaRecipeOut": "_ondemandscanning_25_SlsaRecipeOut",
        "AnalyzePackagesMetadataIn": "_ondemandscanning_26_AnalyzePackagesMetadataIn",
        "AnalyzePackagesMetadataOut": "_ondemandscanning_27_AnalyzePackagesMetadataOut",
        "AliasContextIn": "_ondemandscanning_28_AliasContextIn",
        "AliasContextOut": "_ondemandscanning_29_AliasContextOut",
        "SlsaCompletenessIn": "_ondemandscanning_30_SlsaCompletenessIn",
        "SlsaCompletenessOut": "_ondemandscanning_31_SlsaCompletenessOut",
        "ListOperationsResponseIn": "_ondemandscanning_32_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_ondemandscanning_33_ListOperationsResponseOut",
        "RepoIdIn": "_ondemandscanning_34_RepoIdIn",
        "RepoIdOut": "_ondemandscanning_35_RepoIdOut",
        "SlsaMetadataIn": "_ondemandscanning_36_SlsaMetadataIn",
        "SlsaMetadataOut": "_ondemandscanning_37_SlsaMetadataOut",
        "LanguagePackageDependencyIn": "_ondemandscanning_38_LanguagePackageDependencyIn",
        "LanguagePackageDependencyOut": "_ondemandscanning_39_LanguagePackageDependencyOut",
        "AnalyzePackagesRequestV1In": "_ondemandscanning_40_AnalyzePackagesRequestV1In",
        "AnalyzePackagesRequestV1Out": "_ondemandscanning_41_AnalyzePackagesRequestV1Out",
        "VulnerabilityOccurrenceIn": "_ondemandscanning_42_VulnerabilityOccurrenceIn",
        "VulnerabilityOccurrenceOut": "_ondemandscanning_43_VulnerabilityOccurrenceOut",
        "BuildProvenanceIn": "_ondemandscanning_44_BuildProvenanceIn",
        "BuildProvenanceOut": "_ondemandscanning_45_BuildProvenanceOut",
        "FileLocationIn": "_ondemandscanning_46_FileLocationIn",
        "FileLocationOut": "_ondemandscanning_47_FileLocationOut",
        "SourceIn": "_ondemandscanning_48_SourceIn",
        "SourceOut": "_ondemandscanning_49_SourceOut",
        "RecipeIn": "_ondemandscanning_50_RecipeIn",
        "RecipeOut": "_ondemandscanning_51_RecipeOut",
        "MetadataIn": "_ondemandscanning_52_MetadataIn",
        "MetadataOut": "_ondemandscanning_53_MetadataOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn": "_ondemandscanning_54_GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut": "_ondemandscanning_55_GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut",
        "ProjectRepoIdIn": "_ondemandscanning_56_ProjectRepoIdIn",
        "ProjectRepoIdOut": "_ondemandscanning_57_ProjectRepoIdOut",
        "StatusIn": "_ondemandscanning_58_StatusIn",
        "StatusOut": "_ondemandscanning_59_StatusOut",
        "IdentityIn": "_ondemandscanning_60_IdentityIn",
        "IdentityOut": "_ondemandscanning_61_IdentityOut",
        "FingerprintIn": "_ondemandscanning_62_FingerprintIn",
        "FingerprintOut": "_ondemandscanning_63_FingerprintOut",
        "UpgradeOccurrenceIn": "_ondemandscanning_64_UpgradeOccurrenceIn",
        "UpgradeOccurrenceOut": "_ondemandscanning_65_UpgradeOccurrenceOut",
        "LayerIn": "_ondemandscanning_66_LayerIn",
        "LayerOut": "_ondemandscanning_67_LayerOut",
        "PackageVersionIn": "_ondemandscanning_68_PackageVersionIn",
        "PackageVersionOut": "_ondemandscanning_69_PackageVersionOut",
        "AttestationOccurrenceIn": "_ondemandscanning_70_AttestationOccurrenceIn",
        "AttestationOccurrenceOut": "_ondemandscanning_71_AttestationOccurrenceOut",
        "JwtIn": "_ondemandscanning_72_JwtIn",
        "JwtOut": "_ondemandscanning_73_JwtOut",
        "BinarySourceInfoIn": "_ondemandscanning_74_BinarySourceInfoIn",
        "BinarySourceInfoOut": "_ondemandscanning_75_BinarySourceInfoOut",
        "SlsaProvenanceIn": "_ondemandscanning_76_SlsaProvenanceIn",
        "SlsaProvenanceOut": "_ondemandscanning_77_SlsaProvenanceOut",
        "SBOMReferenceOccurrenceIn": "_ondemandscanning_78_SBOMReferenceOccurrenceIn",
        "SBOMReferenceOccurrenceOut": "_ondemandscanning_79_SBOMReferenceOccurrenceOut",
        "HashIn": "_ondemandscanning_80_HashIn",
        "HashOut": "_ondemandscanning_81_HashOut",
        "NonCompliantFileIn": "_ondemandscanning_82_NonCompliantFileIn",
        "NonCompliantFileOut": "_ondemandscanning_83_NonCompliantFileOut",
        "CommandIn": "_ondemandscanning_84_CommandIn",
        "CommandOut": "_ondemandscanning_85_CommandOut",
        "EmptyIn": "_ondemandscanning_86_EmptyIn",
        "EmptyOut": "_ondemandscanning_87_EmptyOut",
        "AnalyzePackagesResponseV1In": "_ondemandscanning_88_AnalyzePackagesResponseV1In",
        "AnalyzePackagesResponseV1Out": "_ondemandscanning_89_AnalyzePackagesResponseV1Out",
        "CloudRepoSourceContextIn": "_ondemandscanning_90_CloudRepoSourceContextIn",
        "CloudRepoSourceContextOut": "_ondemandscanning_91_CloudRepoSourceContextOut",
        "WindowsUpdateIn": "_ondemandscanning_92_WindowsUpdateIn",
        "WindowsUpdateOut": "_ondemandscanning_93_WindowsUpdateOut",
        "LicenseIn": "_ondemandscanning_94_LicenseIn",
        "LicenseOut": "_ondemandscanning_95_LicenseOut",
        "BuilderConfigIn": "_ondemandscanning_96_BuilderConfigIn",
        "BuilderConfigOut": "_ondemandscanning_97_BuilderConfigOut",
        "DSSEAttestationOccurrenceIn": "_ondemandscanning_98_DSSEAttestationOccurrenceIn",
        "DSSEAttestationOccurrenceOut": "_ondemandscanning_99_DSSEAttestationOccurrenceOut",
        "SourceContextIn": "_ondemandscanning_100_SourceContextIn",
        "SourceContextOut": "_ondemandscanning_101_SourceContextOut",
        "DiscoveryOccurrenceIn": "_ondemandscanning_102_DiscoveryOccurrenceIn",
        "DiscoveryOccurrenceOut": "_ondemandscanning_103_DiscoveryOccurrenceOut",
        "GitSourceContextIn": "_ondemandscanning_104_GitSourceContextIn",
        "GitSourceContextOut": "_ondemandscanning_105_GitSourceContextOut",
        "LocationIn": "_ondemandscanning_106_LocationIn",
        "LocationOut": "_ondemandscanning_107_LocationOut",
        "SbomReferenceIntotoPayloadIn": "_ondemandscanning_108_SbomReferenceIntotoPayloadIn",
        "SbomReferenceIntotoPayloadOut": "_ondemandscanning_109_SbomReferenceIntotoPayloadOut",
        "ListVulnerabilitiesResponseV1In": "_ondemandscanning_110_ListVulnerabilitiesResponseV1In",
        "ListVulnerabilitiesResponseV1Out": "_ondemandscanning_111_ListVulnerabilitiesResponseV1Out",
        "SlsaBuilderIn": "_ondemandscanning_112_SlsaBuilderIn",
        "SlsaBuilderOut": "_ondemandscanning_113_SlsaBuilderOut",
        "OccurrenceIn": "_ondemandscanning_114_OccurrenceIn",
        "OccurrenceOut": "_ondemandscanning_115_OccurrenceOut",
        "PackageDataIn": "_ondemandscanning_116_PackageDataIn",
        "PackageDataOut": "_ondemandscanning_117_PackageDataOut",
        "RemediationIn": "_ondemandscanning_118_RemediationIn",
        "RemediationOut": "_ondemandscanning_119_RemediationOut",
        "AnalyzePackagesResponseIn": "_ondemandscanning_120_AnalyzePackagesResponseIn",
        "AnalyzePackagesResponseOut": "_ondemandscanning_121_AnalyzePackagesResponseOut",
        "SignatureIn": "_ondemandscanning_122_SignatureIn",
        "SignatureOut": "_ondemandscanning_123_SignatureOut",
        "JustificationIn": "_ondemandscanning_124_JustificationIn",
        "JustificationOut": "_ondemandscanning_125_JustificationOut",
        "OperationIn": "_ondemandscanning_126_OperationIn",
        "OperationOut": "_ondemandscanning_127_OperationOut",
        "VersionIn": "_ondemandscanning_128_VersionIn",
        "VersionOut": "_ondemandscanning_129_VersionOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn": "_ondemandscanning_130_GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut": "_ondemandscanning_131_GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut",
        "VexAssessmentIn": "_ondemandscanning_132_VexAssessmentIn",
        "VexAssessmentOut": "_ondemandscanning_133_VexAssessmentOut",
        "PackageIssueIn": "_ondemandscanning_134_PackageIssueIn",
        "PackageIssueOut": "_ondemandscanning_135_PackageIssueOut",
        "AnalysisCompletedIn": "_ondemandscanning_136_AnalysisCompletedIn",
        "AnalysisCompletedOut": "_ondemandscanning_137_AnalysisCompletedOut",
        "CVSSIn": "_ondemandscanning_138_CVSSIn",
        "CVSSOut": "_ondemandscanning_139_CVSSOut",
        "AnalyzePackagesMetadataV1In": "_ondemandscanning_140_AnalyzePackagesMetadataV1In",
        "AnalyzePackagesMetadataV1Out": "_ondemandscanning_141_AnalyzePackagesMetadataV1Out",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn": "_ondemandscanning_142_GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut": "_ondemandscanning_143_GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut",
        "PackageOccurrenceIn": "_ondemandscanning_144_PackageOccurrenceIn",
        "PackageOccurrenceOut": "_ondemandscanning_145_PackageOccurrenceOut",
        "SlsaProvenanceZeroTwoIn": "_ondemandscanning_146_SlsaProvenanceZeroTwoIn",
        "SlsaProvenanceZeroTwoOut": "_ondemandscanning_147_SlsaProvenanceZeroTwoOut",
        "ComplianceOccurrenceIn": "_ondemandscanning_148_ComplianceOccurrenceIn",
        "ComplianceOccurrenceOut": "_ondemandscanning_149_ComplianceOccurrenceOut",
        "RelatedUrlIn": "_ondemandscanning_150_RelatedUrlIn",
        "RelatedUrlOut": "_ondemandscanning_151_RelatedUrlOut",
        "GrafeasV1FileLocationIn": "_ondemandscanning_152_GrafeasV1FileLocationIn",
        "GrafeasV1FileLocationOut": "_ondemandscanning_153_GrafeasV1FileLocationOut",
        "SbomReferenceIntotoPredicateIn": "_ondemandscanning_154_SbomReferenceIntotoPredicateIn",
        "SbomReferenceIntotoPredicateOut": "_ondemandscanning_155_SbomReferenceIntotoPredicateOut",
        "MaintainerIn": "_ondemandscanning_156_MaintainerIn",
        "MaintainerOut": "_ondemandscanning_157_MaintainerOut",
        "InTotoStatementIn": "_ondemandscanning_158_InTotoStatementIn",
        "InTotoStatementOut": "_ondemandscanning_159_InTotoStatementOut",
        "EnvelopeSignatureIn": "_ondemandscanning_160_EnvelopeSignatureIn",
        "EnvelopeSignatureOut": "_ondemandscanning_161_EnvelopeSignatureOut",
        "InTotoProvenanceIn": "_ondemandscanning_162_InTotoProvenanceIn",
        "InTotoProvenanceOut": "_ondemandscanning_163_InTotoProvenanceOut",
        "GerritSourceContextIn": "_ondemandscanning_164_GerritSourceContextIn",
        "GerritSourceContextOut": "_ondemandscanning_165_GerritSourceContextOut",
        "CategoryIn": "_ondemandscanning_166_CategoryIn",
        "CategoryOut": "_ondemandscanning_167_CategoryOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn": "_ondemandscanning_168_GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut": "_ondemandscanning_169_GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut",
        "BuildOccurrenceIn": "_ondemandscanning_170_BuildOccurrenceIn",
        "BuildOccurrenceOut": "_ondemandscanning_171_BuildOccurrenceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["UpgradeDistributionIn"] = t.struct(
        {
            "cpeUri": t.string(),
            "severity": t.string().optional(),
            "classification": t.string().optional(),
            "cve": t.array(t.string()).optional(),
        }
    ).named(renames["UpgradeDistributionIn"])
    types["UpgradeDistributionOut"] = t.struct(
        {
            "cpeUri": t.string(),
            "severity": t.string().optional(),
            "classification": t.string().optional(),
            "cve": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeDistributionOut"])
    types["DeploymentOccurrenceIn"] = t.struct(
        {
            "address": t.string().optional(),
            "config": t.string().optional(),
            "deployTime": t.string(),
            "undeployTime": t.string().optional(),
            "userEmail": t.string().optional(),
            "resourceUri": t.array(t.string()).optional(),
            "platform": t.string().optional(),
        }
    ).named(renames["DeploymentOccurrenceIn"])
    types["DeploymentOccurrenceOut"] = t.struct(
        {
            "address": t.string().optional(),
            "config": t.string().optional(),
            "deployTime": t.string(),
            "undeployTime": t.string().optional(),
            "userEmail": t.string().optional(),
            "resourceUri": t.array(t.string()).optional(),
            "platform": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOccurrenceOut"])
    types["ImageOccurrenceIn"] = t.struct(
        {
            "fingerprint": t.proxy(renames["FingerprintIn"]),
            "distance": t.integer().optional(),
            "layerInfo": t.array(t.proxy(renames["LayerIn"])).optional(),
            "baseResourceUrl": t.string().optional(),
        }
    ).named(renames["ImageOccurrenceIn"])
    types["ImageOccurrenceOut"] = t.struct(
        {
            "fingerprint": t.proxy(renames["FingerprintOut"]),
            "distance": t.integer().optional(),
            "layerInfo": t.array(t.proxy(renames["LayerOut"])).optional(),
            "baseResourceUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOccurrenceOut"])
    types["ArtifactIn"] = t.struct(
        {
            "checksum": t.string().optional(),
            "names": t.array(t.string()).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["ArtifactIn"])
    types["ArtifactOut"] = t.struct(
        {
            "checksum": t.string().optional(),
            "names": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArtifactOut"])
    types["FileHashesIn"] = t.struct(
        {"fileHash": t.array(t.proxy(renames["HashIn"]))}
    ).named(renames["FileHashesIn"])
    types["FileHashesOut"] = t.struct(
        {
            "fileHash": t.array(t.proxy(renames["HashOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileHashesOut"])
    types["MaterialIn"] = t.struct(
        {"digest": t.struct({"_": t.string().optional()}), "uri": t.string()}
    ).named(renames["MaterialIn"])
    types["MaterialOut"] = t.struct(
        {
            "digest": t.struct({"_": t.string().optional()}),
            "uri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaterialOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"] = t.struct(
        {"id": t.string()}
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"] = t.struct(
        {
            "buildInvocationId": t.string(),
            "completeness": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"]
            ),
            "buildFinishedOn": t.string(),
            "buildStartedOn": t.string(),
            "reproducible": t.boolean(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"] = t.struct(
        {
            "buildInvocationId": t.string(),
            "completeness": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"]
            ),
            "buildFinishedOn": t.string(),
            "buildStartedOn": t.string(),
            "reproducible": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"])
    types["SubjectIn"] = t.struct(
        {
            "digest": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
        }
    ).named(renames["SubjectIn"])
    types["SubjectOut"] = t.struct(
        {
            "digest": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubjectOut"])
    types["EnvelopeIn"] = t.struct(
        {
            "payload": t.string(),
            "payloadType": t.string(),
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureIn"])),
        }
    ).named(renames["EnvelopeIn"])
    types["EnvelopeOut"] = t.struct(
        {
            "payload": t.string(),
            "payloadType": t.string(),
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvelopeOut"])
    types["CompletenessIn"] = t.struct(
        {
            "arguments": t.boolean().optional(),
            "environment": t.boolean().optional(),
            "materials": t.boolean().optional(),
        }
    ).named(renames["CompletenessIn"])
    types["CompletenessOut"] = t.struct(
        {
            "arguments": t.boolean().optional(),
            "environment": t.boolean().optional(),
            "materials": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompletenessOut"])
    types["SlsaRecipeIn"] = t.struct(
        {
            "arguments": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "definedInMaterial": t.string().optional(),
            "entryPoint": t.string().optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SlsaRecipeIn"])
    types["SlsaRecipeOut"] = t.struct(
        {
            "arguments": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "definedInMaterial": t.string().optional(),
            "entryPoint": t.string().optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaRecipeOut"])
    types["AnalyzePackagesMetadataIn"] = t.struct(
        {"createTime": t.string().optional(), "resourceUri": t.string().optional()}
    ).named(renames["AnalyzePackagesMetadataIn"])
    types["AnalyzePackagesMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "resourceUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzePackagesMetadataOut"])
    types["AliasContextIn"] = t.struct(
        {"kind": t.string().optional(), "name": t.string().optional()}
    ).named(renames["AliasContextIn"])
    types["AliasContextOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AliasContextOut"])
    types["SlsaCompletenessIn"] = t.struct(
        {
            "environment": t.boolean().optional(),
            "arguments": t.boolean().optional(),
            "materials": t.boolean().optional(),
        }
    ).named(renames["SlsaCompletenessIn"])
    types["SlsaCompletenessOut"] = t.struct(
        {
            "environment": t.boolean().optional(),
            "arguments": t.boolean().optional(),
            "materials": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaCompletenessOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["RepoIdIn"] = t.struct(
        {
            "uid": t.string().optional(),
            "projectRepoId": t.proxy(renames["ProjectRepoIdIn"]).optional(),
        }
    ).named(renames["RepoIdIn"])
    types["RepoIdOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "projectRepoId": t.proxy(renames["ProjectRepoIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepoIdOut"])
    types["SlsaMetadataIn"] = t.struct(
        {
            "completeness": t.proxy(renames["SlsaCompletenessIn"]).optional(),
            "buildFinishedOn": t.string().optional(),
            "reproducible": t.boolean().optional(),
            "buildInvocationId": t.string().optional(),
            "buildStartedOn": t.string().optional(),
        }
    ).named(renames["SlsaMetadataIn"])
    types["SlsaMetadataOut"] = t.struct(
        {
            "completeness": t.proxy(renames["SlsaCompletenessOut"]).optional(),
            "buildFinishedOn": t.string().optional(),
            "reproducible": t.boolean().optional(),
            "buildInvocationId": t.string().optional(),
            "buildStartedOn": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaMetadataOut"])
    types["LanguagePackageDependencyIn"] = t.struct(
        {"package": t.string(), "version": t.string()}
    ).named(renames["LanguagePackageDependencyIn"])
    types["LanguagePackageDependencyOut"] = t.struct(
        {
            "package": t.string(),
            "version": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguagePackageDependencyOut"])
    types["AnalyzePackagesRequestV1In"] = t.struct(
        {
            "includeOsvData": t.boolean().optional(),
            "resourceUri": t.string(),
            "packages": t.array(t.proxy(renames["PackageDataIn"])).optional(),
        }
    ).named(renames["AnalyzePackagesRequestV1In"])
    types["AnalyzePackagesRequestV1Out"] = t.struct(
        {
            "includeOsvData": t.boolean().optional(),
            "resourceUri": t.string(),
            "packages": t.array(t.proxy(renames["PackageDataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzePackagesRequestV1Out"])
    types["VulnerabilityOccurrenceIn"] = t.struct(
        {
            "cvssVersion": t.string().optional(),
            "longDescription": t.string().optional(),
            "shortDescription": t.string().optional(),
            "vexAssessment": t.proxy(renames["VexAssessmentIn"]),
            "type": t.string().optional(),
            "effectiveSeverity": t.string().optional(),
            "severity": t.string().optional(),
            "relatedUrls": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "fixAvailable": t.boolean().optional(),
            "cvssV2": t.proxy(renames["CVSSIn"]).optional(),
            "cvssv3": t.proxy(renames["CVSSIn"]).optional(),
            "packageIssue": t.array(t.proxy(renames["PackageIssueIn"])),
            "cvssScore": t.number().optional(),
        }
    ).named(renames["VulnerabilityOccurrenceIn"])
    types["VulnerabilityOccurrenceOut"] = t.struct(
        {
            "cvssVersion": t.string().optional(),
            "longDescription": t.string().optional(),
            "shortDescription": t.string().optional(),
            "vexAssessment": t.proxy(renames["VexAssessmentOut"]),
            "type": t.string().optional(),
            "effectiveSeverity": t.string().optional(),
            "severity": t.string().optional(),
            "relatedUrls": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "fixAvailable": t.boolean().optional(),
            "cvssV2": t.proxy(renames["CVSSOut"]).optional(),
            "cvssv3": t.proxy(renames["CVSSOut"]).optional(),
            "packageIssue": t.array(t.proxy(renames["PackageIssueOut"])),
            "cvssScore": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityOccurrenceOut"])
    types["BuildProvenanceIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "startTime": t.string().optional(),
            "sourceProvenance": t.proxy(renames["SourceIn"]).optional(),
            "creator": t.string().optional(),
            "builderVersion": t.string().optional(),
            "logsUri": t.string().optional(),
            "buildOptions": t.struct({"_": t.string().optional()}).optional(),
            "triggerId": t.string().optional(),
            "endTime": t.string().optional(),
            "id": t.string(),
            "builtArtifacts": t.array(t.proxy(renames["ArtifactIn"])).optional(),
            "commands": t.array(t.proxy(renames["CommandIn"])).optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["BuildProvenanceIn"])
    types["BuildProvenanceOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "startTime": t.string().optional(),
            "sourceProvenance": t.proxy(renames["SourceOut"]).optional(),
            "creator": t.string().optional(),
            "builderVersion": t.string().optional(),
            "logsUri": t.string().optional(),
            "buildOptions": t.struct({"_": t.string().optional()}).optional(),
            "triggerId": t.string().optional(),
            "endTime": t.string().optional(),
            "id": t.string(),
            "builtArtifacts": t.array(t.proxy(renames["ArtifactOut"])).optional(),
            "commands": t.array(t.proxy(renames["CommandOut"])).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildProvenanceOut"])
    types["FileLocationIn"] = t.struct({"filePath": t.string().optional()}).named(
        renames["FileLocationIn"]
    )
    types["FileLocationOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileLocationOut"])
    types["SourceIn"] = t.struct(
        {
            "additionalContexts": t.array(
                t.proxy(renames["SourceContextIn"])
            ).optional(),
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "artifactStorageSourceUri": t.string().optional(),
            "context": t.proxy(renames["SourceContextIn"]).optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "additionalContexts": t.array(
                t.proxy(renames["SourceContextOut"])
            ).optional(),
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "artifactStorageSourceUri": t.string().optional(),
            "context": t.proxy(renames["SourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["RecipeIn"] = t.struct(
        {
            "definedInMaterial": t.string().optional(),
            "environment": t.array(t.struct({"_": t.string().optional()})).optional(),
            "type": t.string().optional(),
            "entryPoint": t.string().optional(),
            "arguments": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["RecipeIn"])
    types["RecipeOut"] = t.struct(
        {
            "definedInMaterial": t.string().optional(),
            "environment": t.array(t.struct({"_": t.string().optional()})).optional(),
            "type": t.string().optional(),
            "entryPoint": t.string().optional(),
            "arguments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecipeOut"])
    types["MetadataIn"] = t.struct(
        {
            "completeness": t.proxy(renames["CompletenessIn"]).optional(),
            "buildStartedOn": t.string().optional(),
            "buildInvocationId": t.string().optional(),
            "buildFinishedOn": t.string().optional(),
            "reproducible": t.boolean().optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "completeness": t.proxy(renames["CompletenessOut"]).optional(),
            "buildStartedOn": t.string().optional(),
            "buildInvocationId": t.string().optional(),
            "buildFinishedOn": t.string().optional(),
            "reproducible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}),
            "environment": t.struct({"_": t.string().optional()}),
            "configSource": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn"]
            ),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}),
            "environment": t.struct({"_": t.string().optional()}),
            "configSource": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut"])
    types["ProjectRepoIdIn"] = t.struct(
        {"repoName": t.string().optional(), "projectId": t.string().optional()}
    ).named(renames["ProjectRepoIdIn"])
    types["ProjectRepoIdOut"] = t.struct(
        {
            "repoName": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectRepoIdOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["IdentityIn"] = t.struct(
        {"revision": t.integer().optional(), "updateId": t.string().optional()}
    ).named(renames["IdentityIn"])
    types["IdentityOut"] = t.struct(
        {
            "revision": t.integer().optional(),
            "updateId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityOut"])
    types["FingerprintIn"] = t.struct(
        {
            "v1Name": t.string(),
            "v2Name": t.string().optional(),
            "v2Blob": t.array(t.string()),
        }
    ).named(renames["FingerprintIn"])
    types["FingerprintOut"] = t.struct(
        {
            "v1Name": t.string(),
            "v2Name": t.string().optional(),
            "v2Blob": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FingerprintOut"])
    types["UpgradeOccurrenceIn"] = t.struct(
        {
            "parsedVersion": t.proxy(renames["VersionIn"]),
            "windowsUpdate": t.proxy(renames["WindowsUpdateIn"]),
            "distribution": t.proxy(renames["UpgradeDistributionIn"]).optional(),
            "package": t.string(),
        }
    ).named(renames["UpgradeOccurrenceIn"])
    types["UpgradeOccurrenceOut"] = t.struct(
        {
            "parsedVersion": t.proxy(renames["VersionOut"]),
            "windowsUpdate": t.proxy(renames["WindowsUpdateOut"]),
            "distribution": t.proxy(renames["UpgradeDistributionOut"]).optional(),
            "package": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeOccurrenceOut"])
    types["LayerIn"] = t.struct(
        {"arguments": t.string().optional(), "directive": t.string()}
    ).named(renames["LayerIn"])
    types["LayerOut"] = t.struct(
        {
            "arguments": t.string().optional(),
            "directive": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LayerOut"])
    types["PackageVersionIn"] = t.struct(
        {"name": t.string(), "version": t.string()}
    ).named(renames["PackageVersionIn"])
    types["PackageVersionOut"] = t.struct(
        {
            "name": t.string(),
            "version": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageVersionOut"])
    types["AttestationOccurrenceIn"] = t.struct(
        {
            "signatures": t.array(t.proxy(renames["SignatureIn"])).optional(),
            "jwts": t.array(t.proxy(renames["JwtIn"])).optional(),
            "serializedPayload": t.string(),
        }
    ).named(renames["AttestationOccurrenceIn"])
    types["AttestationOccurrenceOut"] = t.struct(
        {
            "signatures": t.array(t.proxy(renames["SignatureOut"])).optional(),
            "jwts": t.array(t.proxy(renames["JwtOut"])).optional(),
            "serializedPayload": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestationOccurrenceOut"])
    types["JwtIn"] = t.struct({"compactJwt": t.string().optional()}).named(
        renames["JwtIn"]
    )
    types["JwtOut"] = t.struct(
        {
            "compactJwt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtOut"])
    types["BinarySourceInfoIn"] = t.struct(
        {
            "sourceVersion": t.proxy(renames["PackageVersionIn"]).optional(),
            "binaryVersion": t.proxy(renames["PackageVersionIn"]).optional(),
        }
    ).named(renames["BinarySourceInfoIn"])
    types["BinarySourceInfoOut"] = t.struct(
        {
            "sourceVersion": t.proxy(renames["PackageVersionOut"]).optional(),
            "binaryVersion": t.proxy(renames["PackageVersionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BinarySourceInfoOut"])
    types["SlsaProvenanceIn"] = t.struct(
        {
            "metadata": t.proxy(renames["SlsaMetadataIn"]),
            "builder": t.proxy(renames["SlsaBuilderIn"]).optional(),
            "recipe": t.proxy(renames["SlsaRecipeIn"]).optional(),
            "materials": t.array(t.proxy(renames["MaterialIn"])).optional(),
        }
    ).named(renames["SlsaProvenanceIn"])
    types["SlsaProvenanceOut"] = t.struct(
        {
            "metadata": t.proxy(renames["SlsaMetadataOut"]),
            "builder": t.proxy(renames["SlsaBuilderOut"]).optional(),
            "recipe": t.proxy(renames["SlsaRecipeOut"]).optional(),
            "materials": t.array(t.proxy(renames["MaterialOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaProvenanceOut"])
    types["SBOMReferenceOccurrenceIn"] = t.struct(
        {
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureIn"])).optional(),
            "payload": t.proxy(renames["SbomReferenceIntotoPayloadIn"]).optional(),
            "payloadType": t.string().optional(),
        }
    ).named(renames["SBOMReferenceOccurrenceIn"])
    types["SBOMReferenceOccurrenceOut"] = t.struct(
        {
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureOut"])).optional(),
            "payload": t.proxy(renames["SbomReferenceIntotoPayloadOut"]).optional(),
            "payloadType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SBOMReferenceOccurrenceOut"])
    types["HashIn"] = t.struct({"type": t.string(), "value": t.string()}).named(
        renames["HashIn"]
    )
    types["HashOut"] = t.struct(
        {
            "type": t.string(),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HashOut"])
    types["NonCompliantFileIn"] = t.struct(
        {
            "displayCommand": t.string().optional(),
            "path": t.string().optional(),
            "reason": t.string().optional(),
        }
    ).named(renames["NonCompliantFileIn"])
    types["NonCompliantFileOut"] = t.struct(
        {
            "displayCommand": t.string().optional(),
            "path": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonCompliantFileOut"])
    types["CommandIn"] = t.struct(
        {
            "args": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "name": t.string(),
            "waitFor": t.array(t.string()).optional(),
            "env": t.array(t.string()).optional(),
            "dir": t.string().optional(),
        }
    ).named(renames["CommandIn"])
    types["CommandOut"] = t.struct(
        {
            "args": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "name": t.string(),
            "waitFor": t.array(t.string()).optional(),
            "env": t.array(t.string()).optional(),
            "dir": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommandOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["AnalyzePackagesResponseV1In"] = t.struct(
        {"scan": t.string().optional()}
    ).named(renames["AnalyzePackagesResponseV1In"])
    types["AnalyzePackagesResponseV1Out"] = t.struct(
        {
            "scan": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzePackagesResponseV1Out"])
    types["CloudRepoSourceContextIn"] = t.struct(
        {
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
            "revisionId": t.string().optional(),
            "repoId": t.proxy(renames["RepoIdIn"]).optional(),
        }
    ).named(renames["CloudRepoSourceContextIn"])
    types["CloudRepoSourceContextOut"] = t.struct(
        {
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "revisionId": t.string().optional(),
            "repoId": t.proxy(renames["RepoIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRepoSourceContextOut"])
    types["WindowsUpdateIn"] = t.struct(
        {
            "kbArticleIds": t.array(t.string()).optional(),
            "supportUrl": t.string().optional(),
            "title": t.string().optional(),
            "lastPublishedTimestamp": t.string().optional(),
            "identity": t.proxy(renames["IdentityIn"]),
            "categories": t.array(t.proxy(renames["CategoryIn"])).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["WindowsUpdateIn"])
    types["WindowsUpdateOut"] = t.struct(
        {
            "kbArticleIds": t.array(t.string()).optional(),
            "supportUrl": t.string().optional(),
            "title": t.string().optional(),
            "lastPublishedTimestamp": t.string().optional(),
            "identity": t.proxy(renames["IdentityOut"]),
            "categories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsUpdateOut"])
    types["LicenseIn"] = t.struct(
        {"expression": t.string().optional(), "comments": t.string().optional()}
    ).named(renames["LicenseIn"])
    types["LicenseOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "comments": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LicenseOut"])
    types["BuilderConfigIn"] = t.struct({"id": t.string()}).named(
        renames["BuilderConfigIn"]
    )
    types["BuilderConfigOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BuilderConfigOut"])
    types["DSSEAttestationOccurrenceIn"] = t.struct(
        {
            "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
            "statement": t.proxy(renames["InTotoStatementIn"]),
        }
    ).named(renames["DSSEAttestationOccurrenceIn"])
    types["DSSEAttestationOccurrenceOut"] = t.struct(
        {
            "envelope": t.proxy(renames["EnvelopeOut"]).optional(),
            "statement": t.proxy(renames["InTotoStatementOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DSSEAttestationOccurrenceOut"])
    types["SourceContextIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gerrit": t.proxy(renames["GerritSourceContextIn"]).optional(),
            "git": t.proxy(renames["GitSourceContextIn"]).optional(),
            "cloudRepo": t.proxy(renames["CloudRepoSourceContextIn"]).optional(),
        }
    ).named(renames["SourceContextIn"])
    types["SourceContextOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gerrit": t.proxy(renames["GerritSourceContextOut"]).optional(),
            "git": t.proxy(renames["GitSourceContextOut"]).optional(),
            "cloudRepo": t.proxy(renames["CloudRepoSourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["DiscoveryOccurrenceIn"] = t.struct(
        {
            "cpe": t.string().optional(),
            "analysisStatus": t.string().optional(),
            "continuousAnalysis": t.string().optional(),
            "analysisCompleted": t.proxy(renames["AnalysisCompletedIn"]),
            "analysisError": t.array(t.proxy(renames["StatusIn"])).optional(),
            "lastScanTime": t.string().optional(),
            "analysisStatusError": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["DiscoveryOccurrenceIn"])
    types["DiscoveryOccurrenceOut"] = t.struct(
        {
            "cpe": t.string().optional(),
            "analysisStatus": t.string().optional(),
            "continuousAnalysis": t.string().optional(),
            "analysisCompleted": t.proxy(renames["AnalysisCompletedOut"]),
            "analysisError": t.array(t.proxy(renames["StatusOut"])).optional(),
            "archiveTime": t.string().optional(),
            "lastScanTime": t.string().optional(),
            "analysisStatusError": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoveryOccurrenceOut"])
    types["GitSourceContextIn"] = t.struct(
        {"revisionId": t.string().optional(), "url": t.string().optional()}
    ).named(renames["GitSourceContextIn"])
    types["GitSourceContextOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitSourceContextOut"])
    types["LocationIn"] = t.struct(
        {
            "cpeUri": t.string().optional(),
            "path": t.string().optional(),
            "version": t.proxy(renames["VersionIn"]).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "cpeUri": t.string().optional(),
            "path": t.string().optional(),
            "version": t.proxy(renames["VersionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["SbomReferenceIntotoPayloadIn"] = t.struct(
        {
            "predicateType": t.string().optional(),
            "subject": t.array(t.proxy(renames["SubjectIn"])).optional(),
            "_type": t.string().optional(),
            "predicate": t.proxy(renames["SbomReferenceIntotoPredicateIn"]).optional(),
        }
    ).named(renames["SbomReferenceIntotoPayloadIn"])
    types["SbomReferenceIntotoPayloadOut"] = t.struct(
        {
            "predicateType": t.string().optional(),
            "subject": t.array(t.proxy(renames["SubjectOut"])).optional(),
            "_type": t.string().optional(),
            "predicate": t.proxy(renames["SbomReferenceIntotoPredicateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SbomReferenceIntotoPayloadOut"])
    types["ListVulnerabilitiesResponseV1In"] = t.struct(
        {
            "occurrences": t.array(t.proxy(renames["OccurrenceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListVulnerabilitiesResponseV1In"])
    types["ListVulnerabilitiesResponseV1Out"] = t.struct(
        {
            "occurrences": t.array(t.proxy(renames["OccurrenceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVulnerabilitiesResponseV1Out"])
    types["SlsaBuilderIn"] = t.struct({"id": t.string()}).named(
        renames["SlsaBuilderIn"]
    )
    types["SlsaBuilderOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SlsaBuilderOut"])
    types["OccurrenceIn"] = t.struct(
        {
            "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
            "vulnerability": t.proxy(renames["VulnerabilityOccurrenceIn"]).optional(),
            "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
            "kind": t.string().optional(),
            "remediation": t.string().optional(),
            "dsseAttestation": t.proxy(
                renames["DSSEAttestationOccurrenceIn"]
            ).optional(),
            "resourceUri": t.string(),
            "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
            "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
            "name": t.string().optional(),
            "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
            "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
            "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
            "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceOccurrenceIn"]).optional(),
            "noteName": t.string(),
            "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["OccurrenceIn"])
    types["OccurrenceOut"] = t.struct(
        {
            "build": t.proxy(renames["BuildOccurrenceOut"]).optional(),
            "vulnerability": t.proxy(renames["VulnerabilityOccurrenceOut"]).optional(),
            "image": t.proxy(renames["ImageOccurrenceOut"]).optional(),
            "kind": t.string().optional(),
            "remediation": t.string().optional(),
            "dsseAttestation": t.proxy(
                renames["DSSEAttestationOccurrenceOut"]
            ).optional(),
            "resourceUri": t.string(),
            "package": t.proxy(renames["PackageOccurrenceOut"]).optional(),
            "compliance": t.proxy(renames["ComplianceOccurrenceOut"]).optional(),
            "name": t.string().optional(),
            "deployment": t.proxy(renames["DeploymentOccurrenceOut"]).optional(),
            "envelope": t.proxy(renames["EnvelopeOut"]).optional(),
            "upgrade": t.proxy(renames["UpgradeOccurrenceOut"]).optional(),
            "attestation": t.proxy(renames["AttestationOccurrenceOut"]).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceOccurrenceOut"]).optional(),
            "noteName": t.string(),
            "discovery": t.proxy(renames["DiscoveryOccurrenceOut"]).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OccurrenceOut"])
    types["PackageDataIn"] = t.struct(
        {
            "dependencyChain": t.array(
                t.proxy(renames["LanguagePackageDependencyIn"])
            ).optional(),
            "version": t.string().optional(),
            "hashDigest": t.string().optional(),
            "os": t.string().optional(),
            "binarySourceInfo": t.array(
                t.proxy(renames["BinarySourceInfoIn"])
            ).optional(),
            "fileLocation": t.array(t.proxy(renames["FileLocationIn"])).optional(),
            "unused": t.string(),
            "packageType": t.string().optional(),
            "package": t.string().optional(),
            "binaryVersion": t.proxy(renames["PackageVersionIn"]).optional(),
            "osVersion": t.string().optional(),
            "sourceVersion": t.proxy(renames["PackageVersionIn"]).optional(),
            "cpeUri": t.string().optional(),
            "architecture": t.string().optional(),
            "maintainer": t.proxy(renames["MaintainerIn"]).optional(),
            "patchedCve": t.array(t.string()).optional(),
        }
    ).named(renames["PackageDataIn"])
    types["PackageDataOut"] = t.struct(
        {
            "dependencyChain": t.array(
                t.proxy(renames["LanguagePackageDependencyOut"])
            ).optional(),
            "version": t.string().optional(),
            "hashDigest": t.string().optional(),
            "os": t.string().optional(),
            "binarySourceInfo": t.array(
                t.proxy(renames["BinarySourceInfoOut"])
            ).optional(),
            "fileLocation": t.array(t.proxy(renames["FileLocationOut"])).optional(),
            "unused": t.string(),
            "packageType": t.string().optional(),
            "package": t.string().optional(),
            "binaryVersion": t.proxy(renames["PackageVersionOut"]).optional(),
            "osVersion": t.string().optional(),
            "sourceVersion": t.proxy(renames["PackageVersionOut"]).optional(),
            "cpeUri": t.string().optional(),
            "architecture": t.string().optional(),
            "maintainer": t.proxy(renames["MaintainerOut"]).optional(),
            "patchedCve": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageDataOut"])
    types["RemediationIn"] = t.struct(
        {
            "remediationType": t.string().optional(),
            "details": t.string().optional(),
            "remediationUri": t.proxy(renames["RelatedUrlIn"]).optional(),
        }
    ).named(renames["RemediationIn"])
    types["RemediationOut"] = t.struct(
        {
            "remediationType": t.string().optional(),
            "details": t.string().optional(),
            "remediationUri": t.proxy(renames["RelatedUrlOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemediationOut"])
    types["AnalyzePackagesResponseIn"] = t.struct(
        {"scan": t.string().optional()}
    ).named(renames["AnalyzePackagesResponseIn"])
    types["AnalyzePackagesResponseOut"] = t.struct(
        {
            "scan": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzePackagesResponseOut"])
    types["SignatureIn"] = t.struct(
        {"signature": t.string().optional(), "publicKeyId": t.string().optional()}
    ).named(renames["SignatureIn"])
    types["SignatureOut"] = t.struct(
        {
            "signature": t.string().optional(),
            "publicKeyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignatureOut"])
    types["JustificationIn"] = t.struct(
        {"details": t.string().optional(), "justificationType": t.string().optional()}
    ).named(renames["JustificationIn"])
    types["JustificationOut"] = t.struct(
        {
            "details": t.string().optional(),
            "justificationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JustificationOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["VersionIn"] = t.struct(
        {
            "epoch": t.integer().optional(),
            "name": t.string(),
            "fullName": t.string().optional(),
            "kind": t.string(),
            "inclusive": t.boolean().optional(),
            "revision": t.string().optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "epoch": t.integer().optional(),
            "name": t.string(),
            "fullName": t.string().optional(),
            "kind": t.string(),
            "inclusive": t.boolean().optional(),
            "revision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"] = t.struct(
        {
            "materials": t.boolean(),
            "environment": t.boolean(),
            "parameters": t.boolean(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"] = t.struct(
        {
            "materials": t.boolean(),
            "environment": t.boolean(),
            "parameters": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"])
    types["VexAssessmentIn"] = t.struct(
        {
            "remediations": t.array(t.proxy(renames["RemediationIn"])).optional(),
            "impacts": t.array(t.string()).optional(),
            "noteName": t.string().optional(),
            "state": t.string().optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "cve": t.string().optional(),
            "justification": t.proxy(renames["JustificationIn"]).optional(),
        }
    ).named(renames["VexAssessmentIn"])
    types["VexAssessmentOut"] = t.struct(
        {
            "remediations": t.array(t.proxy(renames["RemediationOut"])).optional(),
            "impacts": t.array(t.string()).optional(),
            "noteName": t.string().optional(),
            "state": t.string().optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "cve": t.string().optional(),
            "justification": t.proxy(renames["JustificationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VexAssessmentOut"])
    types["PackageIssueIn"] = t.struct(
        {
            "fixedVersion": t.proxy(renames["VersionIn"]),
            "affectedVersion": t.proxy(renames["VersionIn"]),
            "affectedPackage": t.string(),
            "packageType": t.string().optional(),
            "affectedCpeUri": t.string(),
            "fixedPackage": t.string().optional(),
            "fileLocation": t.array(
                t.proxy(renames["GrafeasV1FileLocationIn"])
            ).optional(),
            "fixedCpeUri": t.string().optional(),
            "fixAvailable": t.boolean().optional(),
        }
    ).named(renames["PackageIssueIn"])
    types["PackageIssueOut"] = t.struct(
        {
            "fixedVersion": t.proxy(renames["VersionOut"]),
            "affectedVersion": t.proxy(renames["VersionOut"]),
            "affectedPackage": t.string(),
            "packageType": t.string().optional(),
            "affectedCpeUri": t.string(),
            "fixedPackage": t.string().optional(),
            "fileLocation": t.array(
                t.proxy(renames["GrafeasV1FileLocationOut"])
            ).optional(),
            "fixedCpeUri": t.string().optional(),
            "fixAvailable": t.boolean().optional(),
            "effectiveSeverity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageIssueOut"])
    types["AnalysisCompletedIn"] = t.struct(
        {"analysisType": t.array(t.string())}
    ).named(renames["AnalysisCompletedIn"])
    types["AnalysisCompletedOut"] = t.struct(
        {
            "analysisType": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalysisCompletedOut"])
    types["CVSSIn"] = t.struct(
        {
            "exploitabilityScore": t.number(),
            "userInteraction": t.string(),
            "baseScore": t.number().optional(),
            "authentication": t.string(),
            "availabilityImpact": t.string(),
            "confidentialityImpact": t.string(),
            "privilegesRequired": t.string(),
            "attackVector": t.string().optional(),
            "integrityImpact": t.string(),
            "scope": t.string(),
            "attackComplexity": t.string(),
            "impactScore": t.number(),
        }
    ).named(renames["CVSSIn"])
    types["CVSSOut"] = t.struct(
        {
            "exploitabilityScore": t.number(),
            "userInteraction": t.string(),
            "baseScore": t.number().optional(),
            "authentication": t.string(),
            "availabilityImpact": t.string(),
            "confidentialityImpact": t.string(),
            "privilegesRequired": t.string(),
            "attackVector": t.string().optional(),
            "integrityImpact": t.string(),
            "scope": t.string(),
            "attackComplexity": t.string(),
            "impactScore": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CVSSOut"])
    types["AnalyzePackagesMetadataV1In"] = t.struct(
        {"createTime": t.string().optional(), "resourceUri": t.string().optional()}
    ).named(renames["AnalyzePackagesMetadataV1In"])
    types["AnalyzePackagesMetadataV1Out"] = t.struct(
        {
            "createTime": t.string().optional(),
            "resourceUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzePackagesMetadataV1Out"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn"] = t.struct(
        {"uri": t.string(), "digest": t.struct({"_": t.string().optional()})}
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut"] = t.struct(
        {
            "uri": t.string(),
            "digest": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut"])
    types["PackageOccurrenceIn"] = t.struct(
        {
            "license": t.proxy(renames["LicenseIn"]).optional(),
            "location": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["PackageOccurrenceIn"])
    types["PackageOccurrenceOut"] = t.struct(
        {
            "license": t.proxy(renames["LicenseOut"]).optional(),
            "location": t.array(t.proxy(renames["LocationOut"])).optional(),
            "version": t.proxy(renames["VersionOut"]).optional(),
            "cpeUri": t.string().optional(),
            "packageType": t.string().optional(),
            "architecture": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageOccurrenceOut"])
    types["SlsaProvenanceZeroTwoIn"] = t.struct(
        {
            "metadata": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"]
            ),
            "builder": t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"]),
            "buildConfig": t.struct({"_": t.string().optional()}),
            "invocation": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn"]
            ),
            "materials": t.array(
                t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn"])
            ),
            "buildType": t.string(),
        }
    ).named(renames["SlsaProvenanceZeroTwoIn"])
    types["SlsaProvenanceZeroTwoOut"] = t.struct(
        {
            "metadata": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"]
            ),
            "builder": t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"]),
            "buildConfig": t.struct({"_": t.string().optional()}),
            "invocation": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut"]
            ),
            "materials": t.array(
                t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut"])
            ),
            "buildType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaProvenanceZeroTwoOut"])
    types["ComplianceOccurrenceIn"] = t.struct(
        {
            "nonCompliantFiles": t.array(t.proxy(renames["NonCompliantFileIn"])),
            "nonComplianceReason": t.string(),
        }
    ).named(renames["ComplianceOccurrenceIn"])
    types["ComplianceOccurrenceOut"] = t.struct(
        {
            "nonCompliantFiles": t.array(t.proxy(renames["NonCompliantFileOut"])),
            "nonComplianceReason": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComplianceOccurrenceOut"])
    types["RelatedUrlIn"] = t.struct(
        {"label": t.string().optional(), "url": t.string().optional()}
    ).named(renames["RelatedUrlIn"])
    types["RelatedUrlOut"] = t.struct(
        {
            "label": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelatedUrlOut"])
    types["GrafeasV1FileLocationIn"] = t.struct(
        {"filePath": t.string().optional()}
    ).named(renames["GrafeasV1FileLocationIn"])
    types["GrafeasV1FileLocationOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1FileLocationOut"])
    types["SbomReferenceIntotoPredicateIn"] = t.struct(
        {
            "location": t.string().optional(),
            "digest": t.struct({"_": t.string().optional()}).optional(),
            "mimeType": t.string().optional(),
            "referrerId": t.string().optional(),
        }
    ).named(renames["SbomReferenceIntotoPredicateIn"])
    types["SbomReferenceIntotoPredicateOut"] = t.struct(
        {
            "location": t.string().optional(),
            "digest": t.struct({"_": t.string().optional()}).optional(),
            "mimeType": t.string().optional(),
            "referrerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SbomReferenceIntotoPredicateOut"])
    types["MaintainerIn"] = t.struct({"name": t.string(), "kind": t.string()}).named(
        renames["MaintainerIn"]
    )
    types["MaintainerOut"] = t.struct(
        {
            "name": t.string(),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintainerOut"])
    types["InTotoStatementIn"] = t.struct(
        {
            "slsaProvenanceZeroTwo": t.proxy(renames["SlsaProvenanceZeroTwoIn"]),
            "_type": t.string().optional(),
            "slsaProvenance": t.proxy(renames["SlsaProvenanceIn"]),
            "provenance": t.proxy(renames["InTotoProvenanceIn"]),
            "predicateType": t.string().optional(),
            "subject": t.array(t.proxy(renames["SubjectIn"])),
        }
    ).named(renames["InTotoStatementIn"])
    types["InTotoStatementOut"] = t.struct(
        {
            "slsaProvenanceZeroTwo": t.proxy(renames["SlsaProvenanceZeroTwoOut"]),
            "_type": t.string().optional(),
            "slsaProvenance": t.proxy(renames["SlsaProvenanceOut"]),
            "provenance": t.proxy(renames["InTotoProvenanceOut"]),
            "predicateType": t.string().optional(),
            "subject": t.array(t.proxy(renames["SubjectOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InTotoStatementOut"])
    types["EnvelopeSignatureIn"] = t.struct(
        {"sig": t.string(), "keyid": t.string()}
    ).named(renames["EnvelopeSignatureIn"])
    types["EnvelopeSignatureOut"] = t.struct(
        {
            "sig": t.string(),
            "keyid": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvelopeSignatureOut"])
    types["InTotoProvenanceIn"] = t.struct(
        {
            "recipe": t.proxy(renames["RecipeIn"]).optional(),
            "builderConfig": t.proxy(renames["BuilderConfigIn"]).optional(),
            "materials": t.array(t.string()).optional(),
            "metadata": t.proxy(renames["MetadataIn"]),
        }
    ).named(renames["InTotoProvenanceIn"])
    types["InTotoProvenanceOut"] = t.struct(
        {
            "recipe": t.proxy(renames["RecipeOut"]).optional(),
            "builderConfig": t.proxy(renames["BuilderConfigOut"]).optional(),
            "materials": t.array(t.string()).optional(),
            "metadata": t.proxy(renames["MetadataOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InTotoProvenanceOut"])
    types["GerritSourceContextIn"] = t.struct(
        {
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
            "hostUri": t.string().optional(),
            "gerritProject": t.string().optional(),
            "revisionId": t.string().optional(),
        }
    ).named(renames["GerritSourceContextIn"])
    types["GerritSourceContextOut"] = t.struct(
        {
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "hostUri": t.string().optional(),
            "gerritProject": t.string().optional(),
            "revisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GerritSourceContextOut"])
    types["CategoryIn"] = t.struct(
        {"name": t.string().optional(), "categoryId": t.string().optional()}
    ).named(renames["CategoryIn"])
    types["CategoryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "categoryId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn"] = t.struct(
        {
            "uri": t.string(),
            "entryPoint": t.string(),
            "digest": t.struct({"_": t.string().optional()}),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut"] = t.struct(
        {
            "uri": t.string(),
            "entryPoint": t.string(),
            "digest": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut"])
    types["BuildOccurrenceIn"] = t.struct(
        {
            "provenanceBytes": t.string().optional(),
            "intotoStatement": t.proxy(renames["InTotoStatementIn"]).optional(),
            "intotoProvenance": t.proxy(renames["InTotoProvenanceIn"]).optional(),
            "provenance": t.proxy(renames["BuildProvenanceIn"]).optional(),
        }
    ).named(renames["BuildOccurrenceIn"])
    types["BuildOccurrenceOut"] = t.struct(
        {
            "provenanceBytes": t.string().optional(),
            "intotoStatement": t.proxy(renames["InTotoStatementOut"]).optional(),
            "intotoProvenance": t.proxy(renames["InTotoProvenanceOut"]).optional(),
            "provenance": t.proxy(renames["BuildProvenanceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOccurrenceOut"])

    functions = {}
    functions["projectsLocationsOperationsGet"] = ondemandscanning.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsWait"] = ondemandscanning.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = ondemandscanning.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = ondemandscanning.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = ondemandscanning.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsScansAnalyzePackages"] = ondemandscanning.post(
        "v1/{parent}/scans:analyzePackages",
        t.struct(
            {
                "parent": t.string(),
                "includeOsvData": t.boolean().optional(),
                "resourceUri": t.string(),
                "packages": t.array(t.proxy(renames["PackageDataIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsScansVulnerabilitiesList"] = ondemandscanning.get(
        "v1/{parent}/vulnerabilities",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVulnerabilitiesResponseV1Out"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="ondemandscanning",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
