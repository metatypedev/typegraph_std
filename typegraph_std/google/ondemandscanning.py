from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_ondemandscanning() -> Import:
    ondemandscanning = HTTPRuntime("https://ondemandscanning.googleapis.com/")

    renames = {
        "ErrorResponse": "_ondemandscanning_1_ErrorResponse",
        "SBOMReferenceOccurrenceIn": "_ondemandscanning_2_SBOMReferenceOccurrenceIn",
        "SBOMReferenceOccurrenceOut": "_ondemandscanning_3_SBOMReferenceOccurrenceOut",
        "PackageOccurrenceIn": "_ondemandscanning_4_PackageOccurrenceIn",
        "PackageOccurrenceOut": "_ondemandscanning_5_PackageOccurrenceOut",
        "GerritSourceContextIn": "_ondemandscanning_6_GerritSourceContextIn",
        "GerritSourceContextOut": "_ondemandscanning_7_GerritSourceContextOut",
        "BuildOccurrenceIn": "_ondemandscanning_8_BuildOccurrenceIn",
        "BuildOccurrenceOut": "_ondemandscanning_9_BuildOccurrenceOut",
        "RecipeIn": "_ondemandscanning_10_RecipeIn",
        "RecipeOut": "_ondemandscanning_11_RecipeOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn": "_ondemandscanning_12_GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut": "_ondemandscanning_13_GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut",
        "ComplianceOccurrenceIn": "_ondemandscanning_14_ComplianceOccurrenceIn",
        "ComplianceOccurrenceOut": "_ondemandscanning_15_ComplianceOccurrenceOut",
        "SourceContextIn": "_ondemandscanning_16_SourceContextIn",
        "SourceContextOut": "_ondemandscanning_17_SourceContextOut",
        "SlsaProvenanceIn": "_ondemandscanning_18_SlsaProvenanceIn",
        "SlsaProvenanceOut": "_ondemandscanning_19_SlsaProvenanceOut",
        "PackageIssueIn": "_ondemandscanning_20_PackageIssueIn",
        "PackageIssueOut": "_ondemandscanning_21_PackageIssueOut",
        "CloudRepoSourceContextIn": "_ondemandscanning_22_CloudRepoSourceContextIn",
        "CloudRepoSourceContextOut": "_ondemandscanning_23_CloudRepoSourceContextOut",
        "LayerIn": "_ondemandscanning_24_LayerIn",
        "LayerOut": "_ondemandscanning_25_LayerOut",
        "IdentityIn": "_ondemandscanning_26_IdentityIn",
        "IdentityOut": "_ondemandscanning_27_IdentityOut",
        "ArtifactIn": "_ondemandscanning_28_ArtifactIn",
        "ArtifactOut": "_ondemandscanning_29_ArtifactOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn": "_ondemandscanning_30_GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut": "_ondemandscanning_31_GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut",
        "DSSEAttestationOccurrenceIn": "_ondemandscanning_32_DSSEAttestationOccurrenceIn",
        "DSSEAttestationOccurrenceOut": "_ondemandscanning_33_DSSEAttestationOccurrenceOut",
        "AnalyzePackagesRequestV1In": "_ondemandscanning_34_AnalyzePackagesRequestV1In",
        "AnalyzePackagesRequestV1Out": "_ondemandscanning_35_AnalyzePackagesRequestV1Out",
        "FingerprintIn": "_ondemandscanning_36_FingerprintIn",
        "FingerprintOut": "_ondemandscanning_37_FingerprintOut",
        "LocationIn": "_ondemandscanning_38_LocationIn",
        "LocationOut": "_ondemandscanning_39_LocationOut",
        "FileHashesIn": "_ondemandscanning_40_FileHashesIn",
        "FileHashesOut": "_ondemandscanning_41_FileHashesOut",
        "AnalysisCompletedIn": "_ondemandscanning_42_AnalysisCompletedIn",
        "AnalysisCompletedOut": "_ondemandscanning_43_AnalysisCompletedOut",
        "CategoryIn": "_ondemandscanning_44_CategoryIn",
        "CategoryOut": "_ondemandscanning_45_CategoryOut",
        "UpgradeOccurrenceIn": "_ondemandscanning_46_UpgradeOccurrenceIn",
        "UpgradeOccurrenceOut": "_ondemandscanning_47_UpgradeOccurrenceOut",
        "VersionIn": "_ondemandscanning_48_VersionIn",
        "VersionOut": "_ondemandscanning_49_VersionOut",
        "RepoIdIn": "_ondemandscanning_50_RepoIdIn",
        "RepoIdOut": "_ondemandscanning_51_RepoIdOut",
        "PackageVersionIn": "_ondemandscanning_52_PackageVersionIn",
        "PackageVersionOut": "_ondemandscanning_53_PackageVersionOut",
        "HashIn": "_ondemandscanning_54_HashIn",
        "HashOut": "_ondemandscanning_55_HashOut",
        "WindowsUpdateIn": "_ondemandscanning_56_WindowsUpdateIn",
        "WindowsUpdateOut": "_ondemandscanning_57_WindowsUpdateOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn": "_ondemandscanning_58_GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut": "_ondemandscanning_59_GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut",
        "PackageDataIn": "_ondemandscanning_60_PackageDataIn",
        "PackageDataOut": "_ondemandscanning_61_PackageDataOut",
        "BuildProvenanceIn": "_ondemandscanning_62_BuildProvenanceIn",
        "BuildProvenanceOut": "_ondemandscanning_63_BuildProvenanceOut",
        "SlsaCompletenessIn": "_ondemandscanning_64_SlsaCompletenessIn",
        "SlsaCompletenessOut": "_ondemandscanning_65_SlsaCompletenessOut",
        "AliasContextIn": "_ondemandscanning_66_AliasContextIn",
        "AliasContextOut": "_ondemandscanning_67_AliasContextOut",
        "ListOperationsResponseIn": "_ondemandscanning_68_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_ondemandscanning_69_ListOperationsResponseOut",
        "NonCompliantFileIn": "_ondemandscanning_70_NonCompliantFileIn",
        "NonCompliantFileOut": "_ondemandscanning_71_NonCompliantFileOut",
        "OperationIn": "_ondemandscanning_72_OperationIn",
        "OperationOut": "_ondemandscanning_73_OperationOut",
        "FileLocationIn": "_ondemandscanning_74_FileLocationIn",
        "FileLocationOut": "_ondemandscanning_75_FileLocationOut",
        "RelatedUrlIn": "_ondemandscanning_76_RelatedUrlIn",
        "RelatedUrlOut": "_ondemandscanning_77_RelatedUrlOut",
        "JustificationIn": "_ondemandscanning_78_JustificationIn",
        "JustificationOut": "_ondemandscanning_79_JustificationOut",
        "DeploymentOccurrenceIn": "_ondemandscanning_80_DeploymentOccurrenceIn",
        "DeploymentOccurrenceOut": "_ondemandscanning_81_DeploymentOccurrenceOut",
        "JwtIn": "_ondemandscanning_82_JwtIn",
        "JwtOut": "_ondemandscanning_83_JwtOut",
        "VexAssessmentIn": "_ondemandscanning_84_VexAssessmentIn",
        "VexAssessmentOut": "_ondemandscanning_85_VexAssessmentOut",
        "ListVulnerabilitiesResponseV1In": "_ondemandscanning_86_ListVulnerabilitiesResponseV1In",
        "ListVulnerabilitiesResponseV1Out": "_ondemandscanning_87_ListVulnerabilitiesResponseV1Out",
        "EmptyIn": "_ondemandscanning_88_EmptyIn",
        "EmptyOut": "_ondemandscanning_89_EmptyOut",
        "RemediationIn": "_ondemandscanning_90_RemediationIn",
        "RemediationOut": "_ondemandscanning_91_RemediationOut",
        "SlsaMetadataIn": "_ondemandscanning_92_SlsaMetadataIn",
        "SlsaMetadataOut": "_ondemandscanning_93_SlsaMetadataOut",
        "AnalyzePackagesResponseV1In": "_ondemandscanning_94_AnalyzePackagesResponseV1In",
        "AnalyzePackagesResponseV1Out": "_ondemandscanning_95_AnalyzePackagesResponseV1Out",
        "VulnerabilityOccurrenceIn": "_ondemandscanning_96_VulnerabilityOccurrenceIn",
        "VulnerabilityOccurrenceOut": "_ondemandscanning_97_VulnerabilityOccurrenceOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn": "_ondemandscanning_98_GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut": "_ondemandscanning_99_GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut",
        "ImageOccurrenceIn": "_ondemandscanning_100_ImageOccurrenceIn",
        "ImageOccurrenceOut": "_ondemandscanning_101_ImageOccurrenceOut",
        "MaterialIn": "_ondemandscanning_102_MaterialIn",
        "MaterialOut": "_ondemandscanning_103_MaterialOut",
        "OccurrenceIn": "_ondemandscanning_104_OccurrenceIn",
        "OccurrenceOut": "_ondemandscanning_105_OccurrenceOut",
        "InTotoProvenanceIn": "_ondemandscanning_106_InTotoProvenanceIn",
        "InTotoProvenanceOut": "_ondemandscanning_107_InTotoProvenanceOut",
        "EnvelopeIn": "_ondemandscanning_108_EnvelopeIn",
        "EnvelopeOut": "_ondemandscanning_109_EnvelopeOut",
        "DiscoveryOccurrenceIn": "_ondemandscanning_110_DiscoveryOccurrenceIn",
        "DiscoveryOccurrenceOut": "_ondemandscanning_111_DiscoveryOccurrenceOut",
        "ProjectRepoIdIn": "_ondemandscanning_112_ProjectRepoIdIn",
        "ProjectRepoIdOut": "_ondemandscanning_113_ProjectRepoIdOut",
        "SbomReferenceIntotoPredicateIn": "_ondemandscanning_114_SbomReferenceIntotoPredicateIn",
        "SbomReferenceIntotoPredicateOut": "_ondemandscanning_115_SbomReferenceIntotoPredicateOut",
        "EnvelopeSignatureIn": "_ondemandscanning_116_EnvelopeSignatureIn",
        "EnvelopeSignatureOut": "_ondemandscanning_117_EnvelopeSignatureOut",
        "BuilderConfigIn": "_ondemandscanning_118_BuilderConfigIn",
        "BuilderConfigOut": "_ondemandscanning_119_BuilderConfigOut",
        "AnalyzePackagesResponseIn": "_ondemandscanning_120_AnalyzePackagesResponseIn",
        "AnalyzePackagesResponseOut": "_ondemandscanning_121_AnalyzePackagesResponseOut",
        "MaintainerIn": "_ondemandscanning_122_MaintainerIn",
        "MaintainerOut": "_ondemandscanning_123_MaintainerOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn": "_ondemandscanning_124_GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut": "_ondemandscanning_125_GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut",
        "StatusIn": "_ondemandscanning_126_StatusIn",
        "StatusOut": "_ondemandscanning_127_StatusOut",
        "SignatureIn": "_ondemandscanning_128_SignatureIn",
        "SignatureOut": "_ondemandscanning_129_SignatureOut",
        "SlsaBuilderIn": "_ondemandscanning_130_SlsaBuilderIn",
        "SlsaBuilderOut": "_ondemandscanning_131_SlsaBuilderOut",
        "SbomReferenceIntotoPayloadIn": "_ondemandscanning_132_SbomReferenceIntotoPayloadIn",
        "SbomReferenceIntotoPayloadOut": "_ondemandscanning_133_SbomReferenceIntotoPayloadOut",
        "SlsaProvenanceZeroTwoIn": "_ondemandscanning_134_SlsaProvenanceZeroTwoIn",
        "SlsaProvenanceZeroTwoOut": "_ondemandscanning_135_SlsaProvenanceZeroTwoOut",
        "SourceIn": "_ondemandscanning_136_SourceIn",
        "SourceOut": "_ondemandscanning_137_SourceOut",
        "CommandIn": "_ondemandscanning_138_CommandIn",
        "CommandOut": "_ondemandscanning_139_CommandOut",
        "SubjectIn": "_ondemandscanning_140_SubjectIn",
        "SubjectOut": "_ondemandscanning_141_SubjectOut",
        "CVSSIn": "_ondemandscanning_142_CVSSIn",
        "CVSSOut": "_ondemandscanning_143_CVSSOut",
        "GrafeasV1FileLocationIn": "_ondemandscanning_144_GrafeasV1FileLocationIn",
        "GrafeasV1FileLocationOut": "_ondemandscanning_145_GrafeasV1FileLocationOut",
        "InTotoStatementIn": "_ondemandscanning_146_InTotoStatementIn",
        "InTotoStatementOut": "_ondemandscanning_147_InTotoStatementOut",
        "MetadataIn": "_ondemandscanning_148_MetadataIn",
        "MetadataOut": "_ondemandscanning_149_MetadataOut",
        "GitSourceContextIn": "_ondemandscanning_150_GitSourceContextIn",
        "GitSourceContextOut": "_ondemandscanning_151_GitSourceContextOut",
        "LanguagePackageDependencyIn": "_ondemandscanning_152_LanguagePackageDependencyIn",
        "LanguagePackageDependencyOut": "_ondemandscanning_153_LanguagePackageDependencyOut",
        "LicenseIn": "_ondemandscanning_154_LicenseIn",
        "LicenseOut": "_ondemandscanning_155_LicenseOut",
        "AttestationOccurrenceIn": "_ondemandscanning_156_AttestationOccurrenceIn",
        "AttestationOccurrenceOut": "_ondemandscanning_157_AttestationOccurrenceOut",
        "AnalyzePackagesMetadataV1In": "_ondemandscanning_158_AnalyzePackagesMetadataV1In",
        "AnalyzePackagesMetadataV1Out": "_ondemandscanning_159_AnalyzePackagesMetadataV1Out",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn": "_ondemandscanning_160_GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut": "_ondemandscanning_161_GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut",
        "SlsaRecipeIn": "_ondemandscanning_162_SlsaRecipeIn",
        "SlsaRecipeOut": "_ondemandscanning_163_SlsaRecipeOut",
        "CompletenessIn": "_ondemandscanning_164_CompletenessIn",
        "CompletenessOut": "_ondemandscanning_165_CompletenessOut",
        "AnalyzePackagesMetadataIn": "_ondemandscanning_166_AnalyzePackagesMetadataIn",
        "AnalyzePackagesMetadataOut": "_ondemandscanning_167_AnalyzePackagesMetadataOut",
        "UpgradeDistributionIn": "_ondemandscanning_168_UpgradeDistributionIn",
        "UpgradeDistributionOut": "_ondemandscanning_169_UpgradeDistributionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["PackageOccurrenceIn"] = t.struct(
        {
            "license": t.proxy(renames["LicenseIn"]).optional(),
            "location": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["PackageOccurrenceIn"])
    types["PackageOccurrenceOut"] = t.struct(
        {
            "license": t.proxy(renames["LicenseOut"]).optional(),
            "name": t.string(),
            "packageType": t.string().optional(),
            "cpeUri": t.string().optional(),
            "architecture": t.string().optional(),
            "location": t.array(t.proxy(renames["LocationOut"])).optional(),
            "version": t.proxy(renames["VersionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageOccurrenceOut"])
    types["GerritSourceContextIn"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "gerritProject": t.string().optional(),
            "hostUri": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
        }
    ).named(renames["GerritSourceContextIn"])
    types["GerritSourceContextOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "gerritProject": t.string().optional(),
            "hostUri": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GerritSourceContextOut"])
    types["BuildOccurrenceIn"] = t.struct(
        {
            "provenanceBytes": t.string().optional(),
            "provenance": t.proxy(renames["BuildProvenanceIn"]).optional(),
            "intotoStatement": t.proxy(renames["InTotoStatementIn"]).optional(),
            "intotoProvenance": t.proxy(renames["InTotoProvenanceIn"]).optional(),
        }
    ).named(renames["BuildOccurrenceIn"])
    types["BuildOccurrenceOut"] = t.struct(
        {
            "provenanceBytes": t.string().optional(),
            "provenance": t.proxy(renames["BuildProvenanceOut"]).optional(),
            "intotoStatement": t.proxy(renames["InTotoStatementOut"]).optional(),
            "intotoProvenance": t.proxy(renames["InTotoProvenanceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOccurrenceOut"])
    types["RecipeIn"] = t.struct(
        {
            "entryPoint": t.string().optional(),
            "type": t.string().optional(),
            "definedInMaterial": t.string().optional(),
            "environment": t.array(t.struct({"_": t.string().optional()})).optional(),
            "arguments": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["RecipeIn"])
    types["RecipeOut"] = t.struct(
        {
            "entryPoint": t.string().optional(),
            "type": t.string().optional(),
            "definedInMaterial": t.string().optional(),
            "environment": t.array(t.struct({"_": t.string().optional()})).optional(),
            "arguments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecipeOut"])
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
    types["ComplianceOccurrenceIn"] = t.struct(
        {
            "nonComplianceReason": t.string(),
            "nonCompliantFiles": t.array(t.proxy(renames["NonCompliantFileIn"])),
        }
    ).named(renames["ComplianceOccurrenceIn"])
    types["ComplianceOccurrenceOut"] = t.struct(
        {
            "nonComplianceReason": t.string(),
            "nonCompliantFiles": t.array(t.proxy(renames["NonCompliantFileOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComplianceOccurrenceOut"])
    types["SourceContextIn"] = t.struct(
        {
            "cloudRepo": t.proxy(renames["CloudRepoSourceContextIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "git": t.proxy(renames["GitSourceContextIn"]).optional(),
            "gerrit": t.proxy(renames["GerritSourceContextIn"]).optional(),
        }
    ).named(renames["SourceContextIn"])
    types["SourceContextOut"] = t.struct(
        {
            "cloudRepo": t.proxy(renames["CloudRepoSourceContextOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "git": t.proxy(renames["GitSourceContextOut"]).optional(),
            "gerrit": t.proxy(renames["GerritSourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["SlsaProvenanceIn"] = t.struct(
        {
            "metadata": t.proxy(renames["SlsaMetadataIn"]),
            "materials": t.array(t.proxy(renames["MaterialIn"])).optional(),
            "builder": t.proxy(renames["SlsaBuilderIn"]).optional(),
            "recipe": t.proxy(renames["SlsaRecipeIn"]).optional(),
        }
    ).named(renames["SlsaProvenanceIn"])
    types["SlsaProvenanceOut"] = t.struct(
        {
            "metadata": t.proxy(renames["SlsaMetadataOut"]),
            "materials": t.array(t.proxy(renames["MaterialOut"])).optional(),
            "builder": t.proxy(renames["SlsaBuilderOut"]).optional(),
            "recipe": t.proxy(renames["SlsaRecipeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaProvenanceOut"])
    types["PackageIssueIn"] = t.struct(
        {
            "fixedVersion": t.proxy(renames["VersionIn"]),
            "affectedPackage": t.string(),
            "fixAvailable": t.boolean().optional(),
            "fixedPackage": t.string().optional(),
            "fixedCpeUri": t.string().optional(),
            "affectedCpeUri": t.string(),
            "fileLocation": t.array(
                t.proxy(renames["GrafeasV1FileLocationIn"])
            ).optional(),
            "affectedVersion": t.proxy(renames["VersionIn"]),
            "packageType": t.string().optional(),
        }
    ).named(renames["PackageIssueIn"])
    types["PackageIssueOut"] = t.struct(
        {
            "effectiveSeverity": t.string().optional(),
            "fixedVersion": t.proxy(renames["VersionOut"]),
            "affectedPackage": t.string(),
            "fixAvailable": t.boolean().optional(),
            "fixedPackage": t.string().optional(),
            "fixedCpeUri": t.string().optional(),
            "affectedCpeUri": t.string(),
            "fileLocation": t.array(
                t.proxy(renames["GrafeasV1FileLocationOut"])
            ).optional(),
            "affectedVersion": t.proxy(renames["VersionOut"]),
            "packageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageIssueOut"])
    types["CloudRepoSourceContextIn"] = t.struct(
        {
            "repoId": t.proxy(renames["RepoIdIn"]).optional(),
            "revisionId": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
        }
    ).named(renames["CloudRepoSourceContextIn"])
    types["CloudRepoSourceContextOut"] = t.struct(
        {
            "repoId": t.proxy(renames["RepoIdOut"]).optional(),
            "revisionId": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRepoSourceContextOut"])
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
    types["IdentityIn"] = t.struct(
        {"updateId": t.string().optional(), "revision": t.integer().optional()}
    ).named(renames["IdentityIn"])
    types["IdentityOut"] = t.struct(
        {
            "updateId": t.string().optional(),
            "revision": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityOut"])
    types["ArtifactIn"] = t.struct(
        {
            "checksum": t.string().optional(),
            "id": t.string().optional(),
            "names": t.array(t.string()).optional(),
        }
    ).named(renames["ArtifactIn"])
    types["ArtifactOut"] = t.struct(
        {
            "checksum": t.string().optional(),
            "id": t.string().optional(),
            "names": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArtifactOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn"] = t.struct(
        {
            "entryPoint": t.string(),
            "digest": t.struct({"_": t.string().optional()}),
            "uri": t.string(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut"] = t.struct(
        {
            "entryPoint": t.string(),
            "digest": t.struct({"_": t.string().optional()}),
            "uri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut"])
    types["DSSEAttestationOccurrenceIn"] = t.struct(
        {
            "statement": t.proxy(renames["InTotoStatementIn"]),
            "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
        }
    ).named(renames["DSSEAttestationOccurrenceIn"])
    types["DSSEAttestationOccurrenceOut"] = t.struct(
        {
            "statement": t.proxy(renames["InTotoStatementOut"]),
            "envelope": t.proxy(renames["EnvelopeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DSSEAttestationOccurrenceOut"])
    types["AnalyzePackagesRequestV1In"] = t.struct(
        {
            "packages": t.array(t.proxy(renames["PackageDataIn"])).optional(),
            "resourceUri": t.string(),
            "includeOsvData": t.boolean().optional(),
        }
    ).named(renames["AnalyzePackagesRequestV1In"])
    types["AnalyzePackagesRequestV1Out"] = t.struct(
        {
            "packages": t.array(t.proxy(renames["PackageDataOut"])).optional(),
            "resourceUri": t.string(),
            "includeOsvData": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzePackagesRequestV1Out"])
    types["FingerprintIn"] = t.struct(
        {
            "v1Name": t.string(),
            "v2Blob": t.array(t.string()),
            "v2Name": t.string().optional(),
        }
    ).named(renames["FingerprintIn"])
    types["FingerprintOut"] = t.struct(
        {
            "v1Name": t.string(),
            "v2Blob": t.array(t.string()),
            "v2Name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FingerprintOut"])
    types["LocationIn"] = t.struct(
        {
            "version": t.proxy(renames["VersionIn"]).optional(),
            "path": t.string().optional(),
            "cpeUri": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "version": t.proxy(renames["VersionOut"]).optional(),
            "path": t.string().optional(),
            "cpeUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["FileHashesIn"] = t.struct(
        {"fileHash": t.array(t.proxy(renames["HashIn"]))}
    ).named(renames["FileHashesIn"])
    types["FileHashesOut"] = t.struct(
        {
            "fileHash": t.array(t.proxy(renames["HashOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileHashesOut"])
    types["AnalysisCompletedIn"] = t.struct(
        {"analysisType": t.array(t.string())}
    ).named(renames["AnalysisCompletedIn"])
    types["AnalysisCompletedOut"] = t.struct(
        {
            "analysisType": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalysisCompletedOut"])
    types["CategoryIn"] = t.struct(
        {"categoryId": t.string().optional(), "name": t.string().optional()}
    ).named(renames["CategoryIn"])
    types["CategoryOut"] = t.struct(
        {
            "categoryId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryOut"])
    types["UpgradeOccurrenceIn"] = t.struct(
        {
            "windowsUpdate": t.proxy(renames["WindowsUpdateIn"]),
            "distribution": t.proxy(renames["UpgradeDistributionIn"]).optional(),
            "parsedVersion": t.proxy(renames["VersionIn"]),
            "package": t.string(),
        }
    ).named(renames["UpgradeOccurrenceIn"])
    types["UpgradeOccurrenceOut"] = t.struct(
        {
            "windowsUpdate": t.proxy(renames["WindowsUpdateOut"]),
            "distribution": t.proxy(renames["UpgradeDistributionOut"]).optional(),
            "parsedVersion": t.proxy(renames["VersionOut"]),
            "package": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeOccurrenceOut"])
    types["VersionIn"] = t.struct(
        {
            "epoch": t.integer().optional(),
            "fullName": t.string().optional(),
            "revision": t.string().optional(),
            "kind": t.string(),
            "inclusive": t.boolean().optional(),
            "name": t.string(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "epoch": t.integer().optional(),
            "fullName": t.string().optional(),
            "revision": t.string().optional(),
            "kind": t.string(),
            "inclusive": t.boolean().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
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
    types["HashIn"] = t.struct({"value": t.string(), "type": t.string()}).named(
        renames["HashIn"]
    )
    types["HashOut"] = t.struct(
        {
            "value": t.string(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HashOut"])
    types["WindowsUpdateIn"] = t.struct(
        {
            "categories": t.array(t.proxy(renames["CategoryIn"])).optional(),
            "identity": t.proxy(renames["IdentityIn"]),
            "kbArticleIds": t.array(t.string()).optional(),
            "supportUrl": t.string().optional(),
            "lastPublishedTimestamp": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["WindowsUpdateIn"])
    types["WindowsUpdateOut"] = t.struct(
        {
            "categories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "identity": t.proxy(renames["IdentityOut"]),
            "kbArticleIds": t.array(t.string()).optional(),
            "supportUrl": t.string().optional(),
            "lastPublishedTimestamp": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsUpdateOut"])
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
    types["PackageDataIn"] = t.struct(
        {
            "sourceVersion": t.proxy(renames["PackageVersionIn"]).optional(),
            "unused": t.string(),
            "maintainer": t.proxy(renames["MaintainerIn"]).optional(),
            "dependencyChain": t.array(
                t.proxy(renames["LanguagePackageDependencyIn"])
            ).optional(),
            "fileLocation": t.array(t.proxy(renames["FileLocationIn"])).optional(),
            "patchedCve": t.array(t.string()).optional(),
            "cpeUri": t.string().optional(),
            "package": t.string().optional(),
            "packageType": t.string().optional(),
            "architecture": t.string().optional(),
            "binaryVersion": t.proxy(renames["PackageVersionIn"]).optional(),
            "hashDigest": t.string().optional(),
            "version": t.string().optional(),
            "os": t.string().optional(),
            "osVersion": t.string().optional(),
        }
    ).named(renames["PackageDataIn"])
    types["PackageDataOut"] = t.struct(
        {
            "sourceVersion": t.proxy(renames["PackageVersionOut"]).optional(),
            "unused": t.string(),
            "maintainer": t.proxy(renames["MaintainerOut"]).optional(),
            "dependencyChain": t.array(
                t.proxy(renames["LanguagePackageDependencyOut"])
            ).optional(),
            "fileLocation": t.array(t.proxy(renames["FileLocationOut"])).optional(),
            "patchedCve": t.array(t.string()).optional(),
            "cpeUri": t.string().optional(),
            "package": t.string().optional(),
            "packageType": t.string().optional(),
            "architecture": t.string().optional(),
            "binaryVersion": t.proxy(renames["PackageVersionOut"]).optional(),
            "hashDigest": t.string().optional(),
            "version": t.string().optional(),
            "os": t.string().optional(),
            "osVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageDataOut"])
    types["BuildProvenanceIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "builtArtifacts": t.array(t.proxy(renames["ArtifactIn"])).optional(),
            "creator": t.string().optional(),
            "logsUri": t.string().optional(),
            "commands": t.array(t.proxy(renames["CommandIn"])).optional(),
            "startTime": t.string().optional(),
            "sourceProvenance": t.proxy(renames["SourceIn"]).optional(),
            "buildOptions": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string(),
            "endTime": t.string().optional(),
            "builderVersion": t.string().optional(),
            "triggerId": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["BuildProvenanceIn"])
    types["BuildProvenanceOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "builtArtifacts": t.array(t.proxy(renames["ArtifactOut"])).optional(),
            "creator": t.string().optional(),
            "logsUri": t.string().optional(),
            "commands": t.array(t.proxy(renames["CommandOut"])).optional(),
            "startTime": t.string().optional(),
            "sourceProvenance": t.proxy(renames["SourceOut"]).optional(),
            "buildOptions": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string(),
            "endTime": t.string().optional(),
            "builderVersion": t.string().optional(),
            "triggerId": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildProvenanceOut"])
    types["SlsaCompletenessIn"] = t.struct(
        {
            "environment": t.boolean().optional(),
            "materials": t.boolean().optional(),
            "arguments": t.boolean().optional(),
        }
    ).named(renames["SlsaCompletenessIn"])
    types["SlsaCompletenessOut"] = t.struct(
        {
            "environment": t.boolean().optional(),
            "materials": t.boolean().optional(),
            "arguments": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaCompletenessOut"])
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
    types["NonCompliantFileIn"] = t.struct(
        {
            "reason": t.string().optional(),
            "path": t.string().optional(),
            "displayCommand": t.string().optional(),
        }
    ).named(renames["NonCompliantFileIn"])
    types["NonCompliantFileOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "path": t.string().optional(),
            "displayCommand": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonCompliantFileOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["FileLocationIn"] = t.struct({"filePath": t.string().optional()}).named(
        renames["FileLocationIn"]
    )
    types["FileLocationOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileLocationOut"])
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
    types["DeploymentOccurrenceIn"] = t.struct(
        {
            "address": t.string().optional(),
            "platform": t.string().optional(),
            "resourceUri": t.array(t.string()).optional(),
            "userEmail": t.string().optional(),
            "config": t.string().optional(),
            "deployTime": t.string(),
            "undeployTime": t.string().optional(),
        }
    ).named(renames["DeploymentOccurrenceIn"])
    types["DeploymentOccurrenceOut"] = t.struct(
        {
            "address": t.string().optional(),
            "platform": t.string().optional(),
            "resourceUri": t.array(t.string()).optional(),
            "userEmail": t.string().optional(),
            "config": t.string().optional(),
            "deployTime": t.string(),
            "undeployTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOccurrenceOut"])
    types["JwtIn"] = t.struct({"compactJwt": t.string().optional()}).named(
        renames["JwtIn"]
    )
    types["JwtOut"] = t.struct(
        {
            "compactJwt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtOut"])
    types["VexAssessmentIn"] = t.struct(
        {
            "impacts": t.array(t.string()).optional(),
            "justification": t.proxy(renames["JustificationIn"]).optional(),
            "state": t.string().optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "cve": t.string().optional(),
            "noteName": t.string().optional(),
            "remediations": t.array(t.proxy(renames["RemediationIn"])).optional(),
        }
    ).named(renames["VexAssessmentIn"])
    types["VexAssessmentOut"] = t.struct(
        {
            "impacts": t.array(t.string()).optional(),
            "justification": t.proxy(renames["JustificationOut"]).optional(),
            "state": t.string().optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "cve": t.string().optional(),
            "noteName": t.string().optional(),
            "remediations": t.array(t.proxy(renames["RemediationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VexAssessmentOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["RemediationIn"] = t.struct(
        {
            "details": t.string().optional(),
            "remediationUri": t.proxy(renames["RelatedUrlIn"]).optional(),
            "remediationType": t.string().optional(),
        }
    ).named(renames["RemediationIn"])
    types["RemediationOut"] = t.struct(
        {
            "details": t.string().optional(),
            "remediationUri": t.proxy(renames["RelatedUrlOut"]).optional(),
            "remediationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemediationOut"])
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
    types["AnalyzePackagesResponseV1In"] = t.struct(
        {"scan": t.string().optional()}
    ).named(renames["AnalyzePackagesResponseV1In"])
    types["AnalyzePackagesResponseV1Out"] = t.struct(
        {
            "scan": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzePackagesResponseV1Out"])
    types["VulnerabilityOccurrenceIn"] = t.struct(
        {
            "cvssV2": t.proxy(renames["CVSSIn"]).optional(),
            "vexAssessment": t.proxy(renames["VexAssessmentIn"]),
            "shortDescription": t.string().optional(),
            "longDescription": t.string().optional(),
            "cvssScore": t.number().optional(),
            "effectiveSeverity": t.string().optional(),
            "severity": t.string().optional(),
            "packageIssue": t.array(t.proxy(renames["PackageIssueIn"])),
            "type": t.string().optional(),
            "cvssv3": t.proxy(renames["CVSSIn"]).optional(),
            "relatedUrls": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "cvssVersion": t.string().optional(),
            "fixAvailable": t.boolean().optional(),
        }
    ).named(renames["VulnerabilityOccurrenceIn"])
    types["VulnerabilityOccurrenceOut"] = t.struct(
        {
            "cvssV2": t.proxy(renames["CVSSOut"]).optional(),
            "vexAssessment": t.proxy(renames["VexAssessmentOut"]),
            "shortDescription": t.string().optional(),
            "longDescription": t.string().optional(),
            "cvssScore": t.number().optional(),
            "effectiveSeverity": t.string().optional(),
            "severity": t.string().optional(),
            "packageIssue": t.array(t.proxy(renames["PackageIssueOut"])),
            "type": t.string().optional(),
            "cvssv3": t.proxy(renames["CVSSOut"]).optional(),
            "relatedUrls": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "cvssVersion": t.string().optional(),
            "fixAvailable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityOccurrenceOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"] = t.struct(
        {
            "materials": t.boolean(),
            "parameters": t.boolean(),
            "environment": t.boolean(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"] = t.struct(
        {
            "materials": t.boolean(),
            "parameters": t.boolean(),
            "environment": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"])
    types["ImageOccurrenceIn"] = t.struct(
        {
            "baseResourceUrl": t.string().optional(),
            "fingerprint": t.proxy(renames["FingerprintIn"]),
            "layerInfo": t.array(t.proxy(renames["LayerIn"])).optional(),
            "distance": t.integer().optional(),
        }
    ).named(renames["ImageOccurrenceIn"])
    types["ImageOccurrenceOut"] = t.struct(
        {
            "baseResourceUrl": t.string().optional(),
            "fingerprint": t.proxy(renames["FingerprintOut"]),
            "layerInfo": t.array(t.proxy(renames["LayerOut"])).optional(),
            "distance": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOccurrenceOut"])
    types["MaterialIn"] = t.struct(
        {"uri": t.string(), "digest": t.struct({"_": t.string().optional()})}
    ).named(renames["MaterialIn"])
    types["MaterialOut"] = t.struct(
        {
            "uri": t.string(),
            "digest": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaterialOut"])
    types["OccurrenceIn"] = t.struct(
        {
            "noteName": t.string(),
            "vulnerability": t.proxy(renames["VulnerabilityOccurrenceIn"]).optional(),
            "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
            "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
            "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
            "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
            "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
            "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
            "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
            "dsseAttestation": t.proxy(
                renames["DSSEAttestationOccurrenceIn"]
            ).optional(),
            "kind": t.string().optional(),
            "updateTime": t.string().optional(),
            "remediation": t.string().optional(),
            "createTime": t.string().optional(),
            "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceOccurrenceIn"]).optional(),
            "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
            "name": t.string().optional(),
            "resourceUri": t.string(),
        }
    ).named(renames["OccurrenceIn"])
    types["OccurrenceOut"] = t.struct(
        {
            "noteName": t.string(),
            "vulnerability": t.proxy(renames["VulnerabilityOccurrenceOut"]).optional(),
            "discovery": t.proxy(renames["DiscoveryOccurrenceOut"]).optional(),
            "package": t.proxy(renames["PackageOccurrenceOut"]).optional(),
            "deployment": t.proxy(renames["DeploymentOccurrenceOut"]).optional(),
            "envelope": t.proxy(renames["EnvelopeOut"]).optional(),
            "build": t.proxy(renames["BuildOccurrenceOut"]).optional(),
            "upgrade": t.proxy(renames["UpgradeOccurrenceOut"]).optional(),
            "compliance": t.proxy(renames["ComplianceOccurrenceOut"]).optional(),
            "dsseAttestation": t.proxy(
                renames["DSSEAttestationOccurrenceOut"]
            ).optional(),
            "kind": t.string().optional(),
            "updateTime": t.string().optional(),
            "remediation": t.string().optional(),
            "createTime": t.string().optional(),
            "image": t.proxy(renames["ImageOccurrenceOut"]).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceOccurrenceOut"]).optional(),
            "attestation": t.proxy(renames["AttestationOccurrenceOut"]).optional(),
            "name": t.string().optional(),
            "resourceUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OccurrenceOut"])
    types["InTotoProvenanceIn"] = t.struct(
        {
            "materials": t.array(t.string()).optional(),
            "builderConfig": t.proxy(renames["BuilderConfigIn"]).optional(),
            "recipe": t.proxy(renames["RecipeIn"]).optional(),
            "metadata": t.proxy(renames["MetadataIn"]),
        }
    ).named(renames["InTotoProvenanceIn"])
    types["InTotoProvenanceOut"] = t.struct(
        {
            "materials": t.array(t.string()).optional(),
            "builderConfig": t.proxy(renames["BuilderConfigOut"]).optional(),
            "recipe": t.proxy(renames["RecipeOut"]).optional(),
            "metadata": t.proxy(renames["MetadataOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InTotoProvenanceOut"])
    types["EnvelopeIn"] = t.struct(
        {
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureIn"])),
            "payload": t.string(),
            "payloadType": t.string(),
        }
    ).named(renames["EnvelopeIn"])
    types["EnvelopeOut"] = t.struct(
        {
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureOut"])),
            "payload": t.string(),
            "payloadType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvelopeOut"])
    types["DiscoveryOccurrenceIn"] = t.struct(
        {
            "analysisStatusError": t.proxy(renames["StatusIn"]).optional(),
            "analysisCompleted": t.proxy(renames["AnalysisCompletedIn"]),
            "analysisError": t.array(t.proxy(renames["StatusIn"])).optional(),
            "lastScanTime": t.string().optional(),
            "continuousAnalysis": t.string().optional(),
            "analysisStatus": t.string().optional(),
            "cpe": t.string().optional(),
        }
    ).named(renames["DiscoveryOccurrenceIn"])
    types["DiscoveryOccurrenceOut"] = t.struct(
        {
            "analysisStatusError": t.proxy(renames["StatusOut"]).optional(),
            "analysisCompleted": t.proxy(renames["AnalysisCompletedOut"]),
            "analysisError": t.array(t.proxy(renames["StatusOut"])).optional(),
            "lastScanTime": t.string().optional(),
            "continuousAnalysis": t.string().optional(),
            "archiveTime": t.string().optional(),
            "analysisStatus": t.string().optional(),
            "cpe": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoveryOccurrenceOut"])
    types["ProjectRepoIdIn"] = t.struct(
        {"projectId": t.string().optional(), "repoName": t.string().optional()}
    ).named(renames["ProjectRepoIdIn"])
    types["ProjectRepoIdOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "repoName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectRepoIdOut"])
    types["SbomReferenceIntotoPredicateIn"] = t.struct(
        {
            "referrerId": t.string().optional(),
            "digest": t.struct({"_": t.string().optional()}).optional(),
            "location": t.string().optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["SbomReferenceIntotoPredicateIn"])
    types["SbomReferenceIntotoPredicateOut"] = t.struct(
        {
            "referrerId": t.string().optional(),
            "digest": t.struct({"_": t.string().optional()}).optional(),
            "location": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SbomReferenceIntotoPredicateOut"])
    types["EnvelopeSignatureIn"] = t.struct(
        {"keyid": t.string(), "sig": t.string()}
    ).named(renames["EnvelopeSignatureIn"])
    types["EnvelopeSignatureOut"] = t.struct(
        {
            "keyid": t.string(),
            "sig": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvelopeSignatureOut"])
    types["BuilderConfigIn"] = t.struct({"id": t.string()}).named(
        renames["BuilderConfigIn"]
    )
    types["BuilderConfigOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BuilderConfigOut"])
    types["AnalyzePackagesResponseIn"] = t.struct(
        {"scan": t.string().optional()}
    ).named(renames["AnalyzePackagesResponseIn"])
    types["AnalyzePackagesResponseOut"] = t.struct(
        {
            "scan": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzePackagesResponseOut"])
    types["MaintainerIn"] = t.struct({"kind": t.string(), "name": t.string()}).named(
        renames["MaintainerIn"]
    )
    types["MaintainerOut"] = t.struct(
        {
            "kind": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintainerOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"] = t.struct(
        {
            "reproducible": t.boolean(),
            "buildStartedOn": t.string(),
            "buildFinishedOn": t.string(),
            "buildInvocationId": t.string(),
            "completeness": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"]
            ),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"] = t.struct(
        {
            "reproducible": t.boolean(),
            "buildStartedOn": t.string(),
            "buildFinishedOn": t.string(),
            "buildInvocationId": t.string(),
            "completeness": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"])
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
    types["SlsaBuilderIn"] = t.struct({"id": t.string()}).named(
        renames["SlsaBuilderIn"]
    )
    types["SlsaBuilderOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SlsaBuilderOut"])
    types["SbomReferenceIntotoPayloadIn"] = t.struct(
        {
            "predicateType": t.string().optional(),
            "predicate": t.proxy(renames["SbomReferenceIntotoPredicateIn"]).optional(),
            "subject": t.array(t.proxy(renames["SubjectIn"])).optional(),
            "_type": t.string().optional(),
        }
    ).named(renames["SbomReferenceIntotoPayloadIn"])
    types["SbomReferenceIntotoPayloadOut"] = t.struct(
        {
            "predicateType": t.string().optional(),
            "predicate": t.proxy(renames["SbomReferenceIntotoPredicateOut"]).optional(),
            "subject": t.array(t.proxy(renames["SubjectOut"])).optional(),
            "_type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SbomReferenceIntotoPayloadOut"])
    types["SlsaProvenanceZeroTwoIn"] = t.struct(
        {
            "materials": t.array(
                t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn"])
            ),
            "builder": t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"]),
            "buildType": t.string(),
            "invocation": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn"]
            ),
            "metadata": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"]
            ),
            "buildConfig": t.struct({"_": t.string().optional()}),
        }
    ).named(renames["SlsaProvenanceZeroTwoIn"])
    types["SlsaProvenanceZeroTwoOut"] = t.struct(
        {
            "materials": t.array(
                t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut"])
            ),
            "builder": t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"]),
            "buildType": t.string(),
            "invocation": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut"]
            ),
            "metadata": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"]
            ),
            "buildConfig": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaProvenanceZeroTwoOut"])
    types["SourceIn"] = t.struct(
        {
            "context": t.proxy(renames["SourceContextIn"]).optional(),
            "additionalContexts": t.array(
                t.proxy(renames["SourceContextIn"])
            ).optional(),
            "artifactStorageSourceUri": t.string().optional(),
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "context": t.proxy(renames["SourceContextOut"]).optional(),
            "additionalContexts": t.array(
                t.proxy(renames["SourceContextOut"])
            ).optional(),
            "artifactStorageSourceUri": t.string().optional(),
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["CommandIn"] = t.struct(
        {
            "id": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "waitFor": t.array(t.string()).optional(),
            "dir": t.string().optional(),
            "name": t.string(),
            "args": t.array(t.string()).optional(),
        }
    ).named(renames["CommandIn"])
    types["CommandOut"] = t.struct(
        {
            "id": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "waitFor": t.array(t.string()).optional(),
            "dir": t.string().optional(),
            "name": t.string(),
            "args": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommandOut"])
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
    types["CVSSIn"] = t.struct(
        {
            "privilegesRequired": t.string(),
            "userInteraction": t.string(),
            "attackComplexity": t.string(),
            "baseScore": t.number().optional(),
            "confidentialityImpact": t.string(),
            "impactScore": t.number(),
            "integrityImpact": t.string(),
            "attackVector": t.string().optional(),
            "exploitabilityScore": t.number(),
            "availabilityImpact": t.string(),
            "authentication": t.string(),
            "scope": t.string(),
        }
    ).named(renames["CVSSIn"])
    types["CVSSOut"] = t.struct(
        {
            "privilegesRequired": t.string(),
            "userInteraction": t.string(),
            "attackComplexity": t.string(),
            "baseScore": t.number().optional(),
            "confidentialityImpact": t.string(),
            "impactScore": t.number(),
            "integrityImpact": t.string(),
            "attackVector": t.string().optional(),
            "exploitabilityScore": t.number(),
            "availabilityImpact": t.string(),
            "authentication": t.string(),
            "scope": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CVSSOut"])
    types["GrafeasV1FileLocationIn"] = t.struct(
        {"filePath": t.string().optional()}
    ).named(renames["GrafeasV1FileLocationIn"])
    types["GrafeasV1FileLocationOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1FileLocationOut"])
    types["InTotoStatementIn"] = t.struct(
        {
            "predicateType": t.string().optional(),
            "subject": t.array(t.proxy(renames["SubjectIn"])),
            "_type": t.string().optional(),
            "slsaProvenance": t.proxy(renames["SlsaProvenanceIn"]),
            "slsaProvenanceZeroTwo": t.proxy(renames["SlsaProvenanceZeroTwoIn"]),
            "provenance": t.proxy(renames["InTotoProvenanceIn"]),
        }
    ).named(renames["InTotoStatementIn"])
    types["InTotoStatementOut"] = t.struct(
        {
            "predicateType": t.string().optional(),
            "subject": t.array(t.proxy(renames["SubjectOut"])),
            "_type": t.string().optional(),
            "slsaProvenance": t.proxy(renames["SlsaProvenanceOut"]),
            "slsaProvenanceZeroTwo": t.proxy(renames["SlsaProvenanceZeroTwoOut"]),
            "provenance": t.proxy(renames["InTotoProvenanceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InTotoStatementOut"])
    types["MetadataIn"] = t.struct(
        {
            "buildInvocationId": t.string().optional(),
            "buildStartedOn": t.string().optional(),
            "reproducible": t.boolean().optional(),
            "buildFinishedOn": t.string().optional(),
            "completeness": t.proxy(renames["CompletenessIn"]).optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "buildInvocationId": t.string().optional(),
            "buildStartedOn": t.string().optional(),
            "reproducible": t.boolean().optional(),
            "buildFinishedOn": t.string().optional(),
            "completeness": t.proxy(renames["CompletenessOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["GitSourceContextIn"] = t.struct(
        {"url": t.string().optional(), "revisionId": t.string().optional()}
    ).named(renames["GitSourceContextIn"])
    types["GitSourceContextOut"] = t.struct(
        {
            "url": t.string().optional(),
            "revisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitSourceContextOut"])
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
    types["AttestationOccurrenceIn"] = t.struct(
        {
            "serializedPayload": t.string(),
            "jwts": t.array(t.proxy(renames["JwtIn"])).optional(),
            "signatures": t.array(t.proxy(renames["SignatureIn"])).optional(),
        }
    ).named(renames["AttestationOccurrenceIn"])
    types["AttestationOccurrenceOut"] = t.struct(
        {
            "serializedPayload": t.string(),
            "jwts": t.array(t.proxy(renames["JwtOut"])).optional(),
            "signatures": t.array(t.proxy(renames["SignatureOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestationOccurrenceOut"])
    types["AnalyzePackagesMetadataV1In"] = t.struct(
        {"resourceUri": t.string().optional(), "createTime": t.string().optional()}
    ).named(renames["AnalyzePackagesMetadataV1In"])
    types["AnalyzePackagesMetadataV1Out"] = t.struct(
        {
            "resourceUri": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzePackagesMetadataV1Out"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"] = t.struct(
        {"id": t.string()}
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"])
    types["SlsaRecipeIn"] = t.struct(
        {
            "arguments": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "definedInMaterial": t.string().optional(),
            "entryPoint": t.string().optional(),
        }
    ).named(renames["SlsaRecipeIn"])
    types["SlsaRecipeOut"] = t.struct(
        {
            "arguments": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "definedInMaterial": t.string().optional(),
            "entryPoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaRecipeOut"])
    types["CompletenessIn"] = t.struct(
        {
            "arguments": t.boolean().optional(),
            "materials": t.boolean().optional(),
            "environment": t.boolean().optional(),
        }
    ).named(renames["CompletenessIn"])
    types["CompletenessOut"] = t.struct(
        {
            "arguments": t.boolean().optional(),
            "materials": t.boolean().optional(),
            "environment": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompletenessOut"])
    types["AnalyzePackagesMetadataIn"] = t.struct(
        {"resourceUri": t.string().optional(), "createTime": t.string().optional()}
    ).named(renames["AnalyzePackagesMetadataIn"])
    types["AnalyzePackagesMetadataOut"] = t.struct(
        {
            "resourceUri": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzePackagesMetadataOut"])
    types["UpgradeDistributionIn"] = t.struct(
        {
            "classification": t.string().optional(),
            "severity": t.string().optional(),
            "cpeUri": t.string(),
            "cve": t.array(t.string()).optional(),
        }
    ).named(renames["UpgradeDistributionIn"])
    types["UpgradeDistributionOut"] = t.struct(
        {
            "classification": t.string().optional(),
            "severity": t.string().optional(),
            "cpeUri": t.string(),
            "cve": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeDistributionOut"])

    functions = {}
    functions["projectsLocationsScansAnalyzePackages"] = ondemandscanning.post(
        "v1/{parent}/scans:analyzePackages",
        t.struct(
            {
                "parent": t.string(),
                "packages": t.array(t.proxy(renames["PackageDataIn"])).optional(),
                "resourceUri": t.string(),
                "includeOsvData": t.boolean().optional(),
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
    functions["projectsLocationsOperationsList"] = ondemandscanning.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = ondemandscanning.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsWait"] = ondemandscanning.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = ondemandscanning.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = ondemandscanning.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="ondemandscanning",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
