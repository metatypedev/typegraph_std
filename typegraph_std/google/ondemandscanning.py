from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_ondemandscanning() -> Import:
    ondemandscanning = HTTPRuntime("https://ondemandscanning.googleapis.com/")

    renames = {
        "ErrorResponse": "_ondemandscanning_1_ErrorResponse",
        "IdentityIn": "_ondemandscanning_2_IdentityIn",
        "IdentityOut": "_ondemandscanning_3_IdentityOut",
        "LocationIn": "_ondemandscanning_4_LocationIn",
        "LocationOut": "_ondemandscanning_5_LocationOut",
        "DSSEAttestationOccurrenceIn": "_ondemandscanning_6_DSSEAttestationOccurrenceIn",
        "DSSEAttestationOccurrenceOut": "_ondemandscanning_7_DSSEAttestationOccurrenceOut",
        "MaintainerIn": "_ondemandscanning_8_MaintainerIn",
        "MaintainerOut": "_ondemandscanning_9_MaintainerOut",
        "ComplianceOccurrenceIn": "_ondemandscanning_10_ComplianceOccurrenceIn",
        "ComplianceOccurrenceOut": "_ondemandscanning_11_ComplianceOccurrenceOut",
        "JwtIn": "_ondemandscanning_12_JwtIn",
        "JwtOut": "_ondemandscanning_13_JwtOut",
        "FileLocationIn": "_ondemandscanning_14_FileLocationIn",
        "FileLocationOut": "_ondemandscanning_15_FileLocationOut",
        "GerritSourceContextIn": "_ondemandscanning_16_GerritSourceContextIn",
        "GerritSourceContextOut": "_ondemandscanning_17_GerritSourceContextOut",
        "BuildOccurrenceIn": "_ondemandscanning_18_BuildOccurrenceIn",
        "BuildOccurrenceOut": "_ondemandscanning_19_BuildOccurrenceOut",
        "UpgradeOccurrenceIn": "_ondemandscanning_20_UpgradeOccurrenceIn",
        "UpgradeOccurrenceOut": "_ondemandscanning_21_UpgradeOccurrenceOut",
        "PackageIssueIn": "_ondemandscanning_22_PackageIssueIn",
        "PackageIssueOut": "_ondemandscanning_23_PackageIssueOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn": "_ondemandscanning_24_GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut": "_ondemandscanning_25_GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut",
        "OperationIn": "_ondemandscanning_26_OperationIn",
        "OperationOut": "_ondemandscanning_27_OperationOut",
        "FileHashesIn": "_ondemandscanning_28_FileHashesIn",
        "FileHashesOut": "_ondemandscanning_29_FileHashesOut",
        "SBOMReferenceOccurrenceIn": "_ondemandscanning_30_SBOMReferenceOccurrenceIn",
        "SBOMReferenceOccurrenceOut": "_ondemandscanning_31_SBOMReferenceOccurrenceOut",
        "ListVulnerabilitiesResponseV1In": "_ondemandscanning_32_ListVulnerabilitiesResponseV1In",
        "ListVulnerabilitiesResponseV1Out": "_ondemandscanning_33_ListVulnerabilitiesResponseV1Out",
        "UpgradeDistributionIn": "_ondemandscanning_34_UpgradeDistributionIn",
        "UpgradeDistributionOut": "_ondemandscanning_35_UpgradeDistributionOut",
        "CategoryIn": "_ondemandscanning_36_CategoryIn",
        "CategoryOut": "_ondemandscanning_37_CategoryOut",
        "AnalyzePackagesResponseIn": "_ondemandscanning_38_AnalyzePackagesResponseIn",
        "AnalyzePackagesResponseOut": "_ondemandscanning_39_AnalyzePackagesResponseOut",
        "AnalysisCompletedIn": "_ondemandscanning_40_AnalysisCompletedIn",
        "AnalysisCompletedOut": "_ondemandscanning_41_AnalysisCompletedOut",
        "BuilderConfigIn": "_ondemandscanning_42_BuilderConfigIn",
        "BuilderConfigOut": "_ondemandscanning_43_BuilderConfigOut",
        "ListOperationsResponseIn": "_ondemandscanning_44_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_ondemandscanning_45_ListOperationsResponseOut",
        "SourceIn": "_ondemandscanning_46_SourceIn",
        "SourceOut": "_ondemandscanning_47_SourceOut",
        "GitSourceContextIn": "_ondemandscanning_48_GitSourceContextIn",
        "GitSourceContextOut": "_ondemandscanning_49_GitSourceContextOut",
        "AnalyzePackagesResponseV1In": "_ondemandscanning_50_AnalyzePackagesResponseV1In",
        "AnalyzePackagesResponseV1Out": "_ondemandscanning_51_AnalyzePackagesResponseV1Out",
        "SlsaProvenanceIn": "_ondemandscanning_52_SlsaProvenanceIn",
        "SlsaProvenanceOut": "_ondemandscanning_53_SlsaProvenanceOut",
        "LanguagePackageDependencyIn": "_ondemandscanning_54_LanguagePackageDependencyIn",
        "LanguagePackageDependencyOut": "_ondemandscanning_55_LanguagePackageDependencyOut",
        "RemediationIn": "_ondemandscanning_56_RemediationIn",
        "RemediationOut": "_ondemandscanning_57_RemediationOut",
        "SlsaMetadataIn": "_ondemandscanning_58_SlsaMetadataIn",
        "SlsaMetadataOut": "_ondemandscanning_59_SlsaMetadataOut",
        "AnalyzePackagesMetadataIn": "_ondemandscanning_60_AnalyzePackagesMetadataIn",
        "AnalyzePackagesMetadataOut": "_ondemandscanning_61_AnalyzePackagesMetadataOut",
        "InTotoProvenanceIn": "_ondemandscanning_62_InTotoProvenanceIn",
        "InTotoProvenanceOut": "_ondemandscanning_63_InTotoProvenanceOut",
        "CommandIn": "_ondemandscanning_64_CommandIn",
        "CommandOut": "_ondemandscanning_65_CommandOut",
        "FingerprintIn": "_ondemandscanning_66_FingerprintIn",
        "FingerprintOut": "_ondemandscanning_67_FingerprintOut",
        "RelatedUrlIn": "_ondemandscanning_68_RelatedUrlIn",
        "RelatedUrlOut": "_ondemandscanning_69_RelatedUrlOut",
        "JustificationIn": "_ondemandscanning_70_JustificationIn",
        "JustificationOut": "_ondemandscanning_71_JustificationOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn": "_ondemandscanning_72_GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut": "_ondemandscanning_73_GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn": "_ondemandscanning_74_GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut": "_ondemandscanning_75_GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut",
        "VulnerabilityOccurrenceIn": "_ondemandscanning_76_VulnerabilityOccurrenceIn",
        "VulnerabilityOccurrenceOut": "_ondemandscanning_77_VulnerabilityOccurrenceOut",
        "MetadataIn": "_ondemandscanning_78_MetadataIn",
        "MetadataOut": "_ondemandscanning_79_MetadataOut",
        "SlsaProvenanceZeroTwoIn": "_ondemandscanning_80_SlsaProvenanceZeroTwoIn",
        "SlsaProvenanceZeroTwoOut": "_ondemandscanning_81_SlsaProvenanceZeroTwoOut",
        "DeploymentOccurrenceIn": "_ondemandscanning_82_DeploymentOccurrenceIn",
        "DeploymentOccurrenceOut": "_ondemandscanning_83_DeploymentOccurrenceOut",
        "ArtifactIn": "_ondemandscanning_84_ArtifactIn",
        "ArtifactOut": "_ondemandscanning_85_ArtifactOut",
        "AttestationOccurrenceIn": "_ondemandscanning_86_AttestationOccurrenceIn",
        "AttestationOccurrenceOut": "_ondemandscanning_87_AttestationOccurrenceOut",
        "GrafeasV1FileLocationIn": "_ondemandscanning_88_GrafeasV1FileLocationIn",
        "GrafeasV1FileLocationOut": "_ondemandscanning_89_GrafeasV1FileLocationOut",
        "RecipeIn": "_ondemandscanning_90_RecipeIn",
        "RecipeOut": "_ondemandscanning_91_RecipeOut",
        "OccurrenceIn": "_ondemandscanning_92_OccurrenceIn",
        "OccurrenceOut": "_ondemandscanning_93_OccurrenceOut",
        "InTotoStatementIn": "_ondemandscanning_94_InTotoStatementIn",
        "InTotoStatementOut": "_ondemandscanning_95_InTotoStatementOut",
        "SbomReferenceIntotoPayloadIn": "_ondemandscanning_96_SbomReferenceIntotoPayloadIn",
        "SbomReferenceIntotoPayloadOut": "_ondemandscanning_97_SbomReferenceIntotoPayloadOut",
        "MaterialIn": "_ondemandscanning_98_MaterialIn",
        "MaterialOut": "_ondemandscanning_99_MaterialOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn": "_ondemandscanning_100_GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut": "_ondemandscanning_101_GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut",
        "WindowsUpdateIn": "_ondemandscanning_102_WindowsUpdateIn",
        "WindowsUpdateOut": "_ondemandscanning_103_WindowsUpdateOut",
        "DiscoveryOccurrenceIn": "_ondemandscanning_104_DiscoveryOccurrenceIn",
        "DiscoveryOccurrenceOut": "_ondemandscanning_105_DiscoveryOccurrenceOut",
        "NonCompliantFileIn": "_ondemandscanning_106_NonCompliantFileIn",
        "NonCompliantFileOut": "_ondemandscanning_107_NonCompliantFileOut",
        "VexAssessmentIn": "_ondemandscanning_108_VexAssessmentIn",
        "VexAssessmentOut": "_ondemandscanning_109_VexAssessmentOut",
        "PackageVersionIn": "_ondemandscanning_110_PackageVersionIn",
        "PackageVersionOut": "_ondemandscanning_111_PackageVersionOut",
        "PackageDataIn": "_ondemandscanning_112_PackageDataIn",
        "PackageDataOut": "_ondemandscanning_113_PackageDataOut",
        "EmptyIn": "_ondemandscanning_114_EmptyIn",
        "EmptyOut": "_ondemandscanning_115_EmptyOut",
        "SignatureIn": "_ondemandscanning_116_SignatureIn",
        "SignatureOut": "_ondemandscanning_117_SignatureOut",
        "CVSSIn": "_ondemandscanning_118_CVSSIn",
        "CVSSOut": "_ondemandscanning_119_CVSSOut",
        "VersionIn": "_ondemandscanning_120_VersionIn",
        "VersionOut": "_ondemandscanning_121_VersionOut",
        "ProjectRepoIdIn": "_ondemandscanning_122_ProjectRepoIdIn",
        "ProjectRepoIdOut": "_ondemandscanning_123_ProjectRepoIdOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn": "_ondemandscanning_124_GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut": "_ondemandscanning_125_GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut",
        "SlsaBuilderIn": "_ondemandscanning_126_SlsaBuilderIn",
        "SlsaBuilderOut": "_ondemandscanning_127_SlsaBuilderOut",
        "RepoIdIn": "_ondemandscanning_128_RepoIdIn",
        "RepoIdOut": "_ondemandscanning_129_RepoIdOut",
        "LicenseIn": "_ondemandscanning_130_LicenseIn",
        "LicenseOut": "_ondemandscanning_131_LicenseOut",
        "SourceContextIn": "_ondemandscanning_132_SourceContextIn",
        "SourceContextOut": "_ondemandscanning_133_SourceContextOut",
        "AliasContextIn": "_ondemandscanning_134_AliasContextIn",
        "AliasContextOut": "_ondemandscanning_135_AliasContextOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn": "_ondemandscanning_136_GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut": "_ondemandscanning_137_GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut",
        "AnalyzePackagesMetadataV1In": "_ondemandscanning_138_AnalyzePackagesMetadataV1In",
        "AnalyzePackagesMetadataV1Out": "_ondemandscanning_139_AnalyzePackagesMetadataV1Out",
        "AnalyzePackagesRequestV1In": "_ondemandscanning_140_AnalyzePackagesRequestV1In",
        "AnalyzePackagesRequestV1Out": "_ondemandscanning_141_AnalyzePackagesRequestV1Out",
        "EnvelopeIn": "_ondemandscanning_142_EnvelopeIn",
        "EnvelopeOut": "_ondemandscanning_143_EnvelopeOut",
        "SlsaCompletenessIn": "_ondemandscanning_144_SlsaCompletenessIn",
        "SlsaCompletenessOut": "_ondemandscanning_145_SlsaCompletenessOut",
        "ImageOccurrenceIn": "_ondemandscanning_146_ImageOccurrenceIn",
        "ImageOccurrenceOut": "_ondemandscanning_147_ImageOccurrenceOut",
        "SubjectIn": "_ondemandscanning_148_SubjectIn",
        "SubjectOut": "_ondemandscanning_149_SubjectOut",
        "LayerIn": "_ondemandscanning_150_LayerIn",
        "LayerOut": "_ondemandscanning_151_LayerOut",
        "SlsaRecipeIn": "_ondemandscanning_152_SlsaRecipeIn",
        "SlsaRecipeOut": "_ondemandscanning_153_SlsaRecipeOut",
        "CloudRepoSourceContextIn": "_ondemandscanning_154_CloudRepoSourceContextIn",
        "CloudRepoSourceContextOut": "_ondemandscanning_155_CloudRepoSourceContextOut",
        "StatusIn": "_ondemandscanning_156_StatusIn",
        "StatusOut": "_ondemandscanning_157_StatusOut",
        "EnvelopeSignatureIn": "_ondemandscanning_158_EnvelopeSignatureIn",
        "EnvelopeSignatureOut": "_ondemandscanning_159_EnvelopeSignatureOut",
        "HashIn": "_ondemandscanning_160_HashIn",
        "HashOut": "_ondemandscanning_161_HashOut",
        "CompletenessIn": "_ondemandscanning_162_CompletenessIn",
        "CompletenessOut": "_ondemandscanning_163_CompletenessOut",
        "BuildProvenanceIn": "_ondemandscanning_164_BuildProvenanceIn",
        "BuildProvenanceOut": "_ondemandscanning_165_BuildProvenanceOut",
        "SbomReferenceIntotoPredicateIn": "_ondemandscanning_166_SbomReferenceIntotoPredicateIn",
        "SbomReferenceIntotoPredicateOut": "_ondemandscanning_167_SbomReferenceIntotoPredicateOut",
        "PackageOccurrenceIn": "_ondemandscanning_168_PackageOccurrenceIn",
        "PackageOccurrenceOut": "_ondemandscanning_169_PackageOccurrenceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["LocationIn"] = t.struct(
        {
            "cpeUri": t.string().optional(),
            "version": t.proxy(renames["VersionIn"]).optional(),
            "path": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "cpeUri": t.string().optional(),
            "version": t.proxy(renames["VersionOut"]).optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["JwtIn"] = t.struct({"compactJwt": t.string().optional()}).named(
        renames["JwtIn"]
    )
    types["JwtOut"] = t.struct(
        {
            "compactJwt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtOut"])
    types["FileLocationIn"] = t.struct({"filePath": t.string().optional()}).named(
        renames["FileLocationIn"]
    )
    types["FileLocationOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileLocationOut"])
    types["GerritSourceContextIn"] = t.struct(
        {
            "gerritProject": t.string().optional(),
            "revisionId": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
            "hostUri": t.string().optional(),
        }
    ).named(renames["GerritSourceContextIn"])
    types["GerritSourceContextOut"] = t.struct(
        {
            "gerritProject": t.string().optional(),
            "revisionId": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "hostUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GerritSourceContextOut"])
    types["BuildOccurrenceIn"] = t.struct(
        {
            "provenanceBytes": t.string().optional(),
            "intotoStatement": t.proxy(renames["InTotoStatementIn"]).optional(),
            "provenance": t.proxy(renames["BuildProvenanceIn"]).optional(),
            "intotoProvenance": t.proxy(renames["InTotoProvenanceIn"]).optional(),
        }
    ).named(renames["BuildOccurrenceIn"])
    types["BuildOccurrenceOut"] = t.struct(
        {
            "provenanceBytes": t.string().optional(),
            "intotoStatement": t.proxy(renames["InTotoStatementOut"]).optional(),
            "provenance": t.proxy(renames["BuildProvenanceOut"]).optional(),
            "intotoProvenance": t.proxy(renames["InTotoProvenanceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOccurrenceOut"])
    types["UpgradeOccurrenceIn"] = t.struct(
        {
            "distribution": t.proxy(renames["UpgradeDistributionIn"]).optional(),
            "parsedVersion": t.proxy(renames["VersionIn"]),
            "package": t.string(),
            "windowsUpdate": t.proxy(renames["WindowsUpdateIn"]),
        }
    ).named(renames["UpgradeOccurrenceIn"])
    types["UpgradeOccurrenceOut"] = t.struct(
        {
            "distribution": t.proxy(renames["UpgradeDistributionOut"]).optional(),
            "parsedVersion": t.proxy(renames["VersionOut"]),
            "package": t.string(),
            "windowsUpdate": t.proxy(renames["WindowsUpdateOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeOccurrenceOut"])
    types["PackageIssueIn"] = t.struct(
        {
            "fixedPackage": t.string().optional(),
            "affectedVersion": t.proxy(renames["VersionIn"]),
            "affectedCpeUri": t.string(),
            "affectedPackage": t.string(),
            "packageType": t.string().optional(),
            "fileLocation": t.array(
                t.proxy(renames["GrafeasV1FileLocationIn"])
            ).optional(),
            "fixedVersion": t.proxy(renames["VersionIn"]),
            "fixedCpeUri": t.string().optional(),
            "fixAvailable": t.boolean().optional(),
        }
    ).named(renames["PackageIssueIn"])
    types["PackageIssueOut"] = t.struct(
        {
            "fixedPackage": t.string().optional(),
            "effectiveSeverity": t.string().optional(),
            "affectedVersion": t.proxy(renames["VersionOut"]),
            "affectedCpeUri": t.string(),
            "affectedPackage": t.string(),
            "packageType": t.string().optional(),
            "fileLocation": t.array(
                t.proxy(renames["GrafeasV1FileLocationOut"])
            ).optional(),
            "fixedVersion": t.proxy(renames["VersionOut"]),
            "fixedCpeUri": t.string().optional(),
            "fixAvailable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageIssueOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn"] = t.struct(
        {"digest": t.struct({"_": t.string().optional()}), "uri": t.string()}
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut"] = t.struct(
        {
            "digest": t.struct({"_": t.string().optional()}),
            "uri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut"])
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
    types["FileHashesIn"] = t.struct(
        {"fileHash": t.array(t.proxy(renames["HashIn"]))}
    ).named(renames["FileHashesIn"])
    types["FileHashesOut"] = t.struct(
        {
            "fileHash": t.array(t.proxy(renames["HashOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileHashesOut"])
    types["SBOMReferenceOccurrenceIn"] = t.struct(
        {
            "payloadType": t.string().optional(),
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureIn"])).optional(),
            "payload": t.proxy(renames["SbomReferenceIntotoPayloadIn"]).optional(),
        }
    ).named(renames["SBOMReferenceOccurrenceIn"])
    types["SBOMReferenceOccurrenceOut"] = t.struct(
        {
            "payloadType": t.string().optional(),
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureOut"])).optional(),
            "payload": t.proxy(renames["SbomReferenceIntotoPayloadOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SBOMReferenceOccurrenceOut"])
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
    types["UpgradeDistributionIn"] = t.struct(
        {
            "classification": t.string().optional(),
            "severity": t.string().optional(),
            "cve": t.array(t.string()).optional(),
            "cpeUri": t.string(),
        }
    ).named(renames["UpgradeDistributionIn"])
    types["UpgradeDistributionOut"] = t.struct(
        {
            "classification": t.string().optional(),
            "severity": t.string().optional(),
            "cve": t.array(t.string()).optional(),
            "cpeUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeDistributionOut"])
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
    types["AnalyzePackagesResponseIn"] = t.struct(
        {"scan": t.string().optional()}
    ).named(renames["AnalyzePackagesResponseIn"])
    types["AnalyzePackagesResponseOut"] = t.struct(
        {
            "scan": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzePackagesResponseOut"])
    types["AnalysisCompletedIn"] = t.struct(
        {"analysisType": t.array(t.string())}
    ).named(renames["AnalysisCompletedIn"])
    types["AnalysisCompletedOut"] = t.struct(
        {
            "analysisType": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalysisCompletedOut"])
    types["BuilderConfigIn"] = t.struct({"id": t.string()}).named(
        renames["BuilderConfigIn"]
    )
    types["BuilderConfigOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BuilderConfigOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["SourceIn"] = t.struct(
        {
            "additionalContexts": t.array(
                t.proxy(renames["SourceContextIn"])
            ).optional(),
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "context": t.proxy(renames["SourceContextIn"]).optional(),
            "artifactStorageSourceUri": t.string().optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "additionalContexts": t.array(
                t.proxy(renames["SourceContextOut"])
            ).optional(),
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "context": t.proxy(renames["SourceContextOut"]).optional(),
            "artifactStorageSourceUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
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
    types["AnalyzePackagesResponseV1In"] = t.struct(
        {"scan": t.string().optional()}
    ).named(renames["AnalyzePackagesResponseV1In"])
    types["AnalyzePackagesResponseV1Out"] = t.struct(
        {
            "scan": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzePackagesResponseV1Out"])
    types["SlsaProvenanceIn"] = t.struct(
        {
            "recipe": t.proxy(renames["SlsaRecipeIn"]).optional(),
            "metadata": t.proxy(renames["SlsaMetadataIn"]),
            "builder": t.proxy(renames["SlsaBuilderIn"]).optional(),
            "materials": t.array(t.proxy(renames["MaterialIn"])).optional(),
        }
    ).named(renames["SlsaProvenanceIn"])
    types["SlsaProvenanceOut"] = t.struct(
        {
            "recipe": t.proxy(renames["SlsaRecipeOut"]).optional(),
            "metadata": t.proxy(renames["SlsaMetadataOut"]),
            "builder": t.proxy(renames["SlsaBuilderOut"]).optional(),
            "materials": t.array(t.proxy(renames["MaterialOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaProvenanceOut"])
    types["LanguagePackageDependencyIn"] = t.struct(
        {"version": t.string(), "package": t.string()}
    ).named(renames["LanguagePackageDependencyIn"])
    types["LanguagePackageDependencyOut"] = t.struct(
        {
            "version": t.string(),
            "package": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguagePackageDependencyOut"])
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
            "buildFinishedOn": t.string().optional(),
            "completeness": t.proxy(renames["SlsaCompletenessIn"]).optional(),
            "reproducible": t.boolean().optional(),
            "buildInvocationId": t.string().optional(),
            "buildStartedOn": t.string().optional(),
        }
    ).named(renames["SlsaMetadataIn"])
    types["SlsaMetadataOut"] = t.struct(
        {
            "buildFinishedOn": t.string().optional(),
            "completeness": t.proxy(renames["SlsaCompletenessOut"]).optional(),
            "reproducible": t.boolean().optional(),
            "buildInvocationId": t.string().optional(),
            "buildStartedOn": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaMetadataOut"])
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
    types["InTotoProvenanceIn"] = t.struct(
        {
            "builderConfig": t.proxy(renames["BuilderConfigIn"]).optional(),
            "materials": t.array(t.string()).optional(),
            "recipe": t.proxy(renames["RecipeIn"]).optional(),
            "metadata": t.proxy(renames["MetadataIn"]),
        }
    ).named(renames["InTotoProvenanceIn"])
    types["InTotoProvenanceOut"] = t.struct(
        {
            "builderConfig": t.proxy(renames["BuilderConfigOut"]).optional(),
            "materials": t.array(t.string()).optional(),
            "recipe": t.proxy(renames["RecipeOut"]).optional(),
            "metadata": t.proxy(renames["MetadataOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InTotoProvenanceOut"])
    types["CommandIn"] = t.struct(
        {
            "env": t.array(t.string()).optional(),
            "dir": t.string().optional(),
            "name": t.string(),
            "id": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
        }
    ).named(renames["CommandIn"])
    types["CommandOut"] = t.struct(
        {
            "env": t.array(t.string()).optional(),
            "dir": t.string().optional(),
            "name": t.string(),
            "id": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommandOut"])
    types["FingerprintIn"] = t.struct(
        {
            "v2Blob": t.array(t.string()),
            "v1Name": t.string(),
            "v2Name": t.string().optional(),
        }
    ).named(renames["FingerprintIn"])
    types["FingerprintOut"] = t.struct(
        {
            "v2Blob": t.array(t.string()),
            "v1Name": t.string(),
            "v2Name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FingerprintOut"])
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
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn"] = t.struct(
        {
            "digest": t.struct({"_": t.string().optional()}),
            "uri": t.string(),
            "entryPoint": t.string(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut"] = t.struct(
        {
            "digest": t.struct({"_": t.string().optional()}),
            "uri": t.string(),
            "entryPoint": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"] = t.struct(
        {
            "buildFinishedOn": t.string(),
            "completeness": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"]
            ),
            "buildStartedOn": t.string(),
            "reproducible": t.boolean(),
            "buildInvocationId": t.string(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"] = t.struct(
        {
            "buildFinishedOn": t.string(),
            "completeness": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"]
            ),
            "buildStartedOn": t.string(),
            "reproducible": t.boolean(),
            "buildInvocationId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"])
    types["VulnerabilityOccurrenceIn"] = t.struct(
        {
            "cvssV2": t.proxy(renames["CVSSIn"]).optional(),
            "fixAvailable": t.boolean().optional(),
            "cvssVersion": t.string().optional(),
            "longDescription": t.string().optional(),
            "type": t.string().optional(),
            "effectiveSeverity": t.string().optional(),
            "cvssv3": t.proxy(renames["CVSSIn"]).optional(),
            "relatedUrls": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "vexAssessment": t.proxy(renames["VexAssessmentIn"]),
            "shortDescription": t.string().optional(),
            "packageIssue": t.array(t.proxy(renames["PackageIssueIn"])),
            "cvssScore": t.number().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["VulnerabilityOccurrenceIn"])
    types["VulnerabilityOccurrenceOut"] = t.struct(
        {
            "cvssV2": t.proxy(renames["CVSSOut"]).optional(),
            "fixAvailable": t.boolean().optional(),
            "cvssVersion": t.string().optional(),
            "longDescription": t.string().optional(),
            "type": t.string().optional(),
            "effectiveSeverity": t.string().optional(),
            "cvssv3": t.proxy(renames["CVSSOut"]).optional(),
            "relatedUrls": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "vexAssessment": t.proxy(renames["VexAssessmentOut"]),
            "shortDescription": t.string().optional(),
            "packageIssue": t.array(t.proxy(renames["PackageIssueOut"])),
            "cvssScore": t.number().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityOccurrenceOut"])
    types["MetadataIn"] = t.struct(
        {
            "buildInvocationId": t.string().optional(),
            "reproducible": t.boolean().optional(),
            "completeness": t.proxy(renames["CompletenessIn"]).optional(),
            "buildFinishedOn": t.string().optional(),
            "buildStartedOn": t.string().optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "buildInvocationId": t.string().optional(),
            "reproducible": t.boolean().optional(),
            "completeness": t.proxy(renames["CompletenessOut"]).optional(),
            "buildFinishedOn": t.string().optional(),
            "buildStartedOn": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["SlsaProvenanceZeroTwoIn"] = t.struct(
        {
            "materials": t.array(
                t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn"])
            ),
            "buildType": t.string(),
            "metadata": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"]
            ),
            "invocation": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn"]
            ),
            "buildConfig": t.struct({"_": t.string().optional()}),
            "builder": t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"]),
        }
    ).named(renames["SlsaProvenanceZeroTwoIn"])
    types["SlsaProvenanceZeroTwoOut"] = t.struct(
        {
            "materials": t.array(
                t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut"])
            ),
            "buildType": t.string(),
            "metadata": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"]
            ),
            "invocation": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut"]
            ),
            "buildConfig": t.struct({"_": t.string().optional()}),
            "builder": t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaProvenanceZeroTwoOut"])
    types["DeploymentOccurrenceIn"] = t.struct(
        {
            "address": t.string().optional(),
            "config": t.string().optional(),
            "deployTime": t.string(),
            "undeployTime": t.string().optional(),
            "platform": t.string().optional(),
            "resourceUri": t.array(t.string()).optional(),
            "userEmail": t.string().optional(),
        }
    ).named(renames["DeploymentOccurrenceIn"])
    types["DeploymentOccurrenceOut"] = t.struct(
        {
            "address": t.string().optional(),
            "config": t.string().optional(),
            "deployTime": t.string(),
            "undeployTime": t.string().optional(),
            "platform": t.string().optional(),
            "resourceUri": t.array(t.string()).optional(),
            "userEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOccurrenceOut"])
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
    types["GrafeasV1FileLocationIn"] = t.struct(
        {"filePath": t.string().optional()}
    ).named(renames["GrafeasV1FileLocationIn"])
    types["GrafeasV1FileLocationOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1FileLocationOut"])
    types["RecipeIn"] = t.struct(
        {
            "environment": t.array(t.struct({"_": t.string().optional()})).optional(),
            "definedInMaterial": t.string().optional(),
            "arguments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "entryPoint": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["RecipeIn"])
    types["RecipeOut"] = t.struct(
        {
            "environment": t.array(t.struct({"_": t.string().optional()})).optional(),
            "definedInMaterial": t.string().optional(),
            "arguments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "entryPoint": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecipeOut"])
    types["OccurrenceIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
            "dsseAttestation": t.proxy(
                renames["DSSEAttestationOccurrenceIn"]
            ).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceOccurrenceIn"]).optional(),
            "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
            "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
            "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
            "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
            "noteName": t.string(),
            "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
            "updateTime": t.string().optional(),
            "resourceUri": t.string(),
            "remediation": t.string().optional(),
            "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
            "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
            "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
            "kind": t.string().optional(),
            "vulnerability": t.proxy(renames["VulnerabilityOccurrenceIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OccurrenceIn"])
    types["OccurrenceOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "image": t.proxy(renames["ImageOccurrenceOut"]).optional(),
            "dsseAttestation": t.proxy(
                renames["DSSEAttestationOccurrenceOut"]
            ).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceOccurrenceOut"]).optional(),
            "envelope": t.proxy(renames["EnvelopeOut"]).optional(),
            "package": t.proxy(renames["PackageOccurrenceOut"]).optional(),
            "attestation": t.proxy(renames["AttestationOccurrenceOut"]).optional(),
            "deployment": t.proxy(renames["DeploymentOccurrenceOut"]).optional(),
            "noteName": t.string(),
            "upgrade": t.proxy(renames["UpgradeOccurrenceOut"]).optional(),
            "updateTime": t.string().optional(),
            "resourceUri": t.string(),
            "remediation": t.string().optional(),
            "discovery": t.proxy(renames["DiscoveryOccurrenceOut"]).optional(),
            "compliance": t.proxy(renames["ComplianceOccurrenceOut"]).optional(),
            "build": t.proxy(renames["BuildOccurrenceOut"]).optional(),
            "kind": t.string().optional(),
            "vulnerability": t.proxy(renames["VulnerabilityOccurrenceOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OccurrenceOut"])
    types["InTotoStatementIn"] = t.struct(
        {
            "provenance": t.proxy(renames["InTotoProvenanceIn"]),
            "predicateType": t.string().optional(),
            "slsaProvenance": t.proxy(renames["SlsaProvenanceIn"]),
            "subject": t.array(t.proxy(renames["SubjectIn"])),
            "slsaProvenanceZeroTwo": t.proxy(renames["SlsaProvenanceZeroTwoIn"]),
            "_type": t.string().optional(),
        }
    ).named(renames["InTotoStatementIn"])
    types["InTotoStatementOut"] = t.struct(
        {
            "provenance": t.proxy(renames["InTotoProvenanceOut"]),
            "predicateType": t.string().optional(),
            "slsaProvenance": t.proxy(renames["SlsaProvenanceOut"]),
            "subject": t.array(t.proxy(renames["SubjectOut"])),
            "slsaProvenanceZeroTwo": t.proxy(renames["SlsaProvenanceZeroTwoOut"]),
            "_type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InTotoStatementOut"])
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
    types["WindowsUpdateIn"] = t.struct(
        {
            "supportUrl": t.string().optional(),
            "categories": t.array(t.proxy(renames["CategoryIn"])).optional(),
            "lastPublishedTimestamp": t.string().optional(),
            "kbArticleIds": t.array(t.string()).optional(),
            "identity": t.proxy(renames["IdentityIn"]),
            "description": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["WindowsUpdateIn"])
    types["WindowsUpdateOut"] = t.struct(
        {
            "supportUrl": t.string().optional(),
            "categories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "lastPublishedTimestamp": t.string().optional(),
            "kbArticleIds": t.array(t.string()).optional(),
            "identity": t.proxy(renames["IdentityOut"]),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsUpdateOut"])
    types["DiscoveryOccurrenceIn"] = t.struct(
        {
            "analysisStatusError": t.proxy(renames["StatusIn"]).optional(),
            "analysisError": t.array(t.proxy(renames["StatusIn"])).optional(),
            "continuousAnalysis": t.string().optional(),
            "analysisCompleted": t.proxy(renames["AnalysisCompletedIn"]),
            "cpe": t.string().optional(),
            "lastScanTime": t.string().optional(),
            "analysisStatus": t.string().optional(),
        }
    ).named(renames["DiscoveryOccurrenceIn"])
    types["DiscoveryOccurrenceOut"] = t.struct(
        {
            "analysisStatusError": t.proxy(renames["StatusOut"]).optional(),
            "analysisError": t.array(t.proxy(renames["StatusOut"])).optional(),
            "continuousAnalysis": t.string().optional(),
            "analysisCompleted": t.proxy(renames["AnalysisCompletedOut"]),
            "archiveTime": t.string().optional(),
            "cpe": t.string().optional(),
            "lastScanTime": t.string().optional(),
            "analysisStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoveryOccurrenceOut"])
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
    types["VexAssessmentIn"] = t.struct(
        {
            "state": t.string().optional(),
            "remediations": t.array(t.proxy(renames["RemediationIn"])).optional(),
            "cve": t.string().optional(),
            "impacts": t.array(t.string()).optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "justification": t.proxy(renames["JustificationIn"]).optional(),
            "noteName": t.string().optional(),
        }
    ).named(renames["VexAssessmentIn"])
    types["VexAssessmentOut"] = t.struct(
        {
            "state": t.string().optional(),
            "remediations": t.array(t.proxy(renames["RemediationOut"])).optional(),
            "cve": t.string().optional(),
            "impacts": t.array(t.string()).optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "justification": t.proxy(renames["JustificationOut"]).optional(),
            "noteName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VexAssessmentOut"])
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
    types["PackageDataIn"] = t.struct(
        {
            "unused": t.string(),
            "dependencyChain": t.array(
                t.proxy(renames["LanguagePackageDependencyIn"])
            ).optional(),
            "osVersion": t.string().optional(),
            "sourceVersion": t.proxy(renames["PackageVersionIn"]).optional(),
            "fileLocation": t.array(t.proxy(renames["FileLocationIn"])).optional(),
            "maintainer": t.proxy(renames["MaintainerIn"]).optional(),
            "hashDigest": t.string().optional(),
            "packageType": t.string().optional(),
            "binaryVersion": t.proxy(renames["PackageVersionIn"]).optional(),
            "patchedCve": t.array(t.string()).optional(),
            "package": t.string().optional(),
            "version": t.string().optional(),
            "architecture": t.string().optional(),
            "cpeUri": t.string().optional(),
            "os": t.string().optional(),
        }
    ).named(renames["PackageDataIn"])
    types["PackageDataOut"] = t.struct(
        {
            "unused": t.string(),
            "dependencyChain": t.array(
                t.proxy(renames["LanguagePackageDependencyOut"])
            ).optional(),
            "osVersion": t.string().optional(),
            "sourceVersion": t.proxy(renames["PackageVersionOut"]).optional(),
            "fileLocation": t.array(t.proxy(renames["FileLocationOut"])).optional(),
            "maintainer": t.proxy(renames["MaintainerOut"]).optional(),
            "hashDigest": t.string().optional(),
            "packageType": t.string().optional(),
            "binaryVersion": t.proxy(renames["PackageVersionOut"]).optional(),
            "patchedCve": t.array(t.string()).optional(),
            "package": t.string().optional(),
            "version": t.string().optional(),
            "architecture": t.string().optional(),
            "cpeUri": t.string().optional(),
            "os": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageDataOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["CVSSIn"] = t.struct(
        {
            "authentication": t.string(),
            "userInteraction": t.string(),
            "confidentialityImpact": t.string(),
            "scope": t.string(),
            "baseScore": t.number().optional(),
            "integrityImpact": t.string(),
            "exploitabilityScore": t.number(),
            "attackComplexity": t.string(),
            "attackVector": t.string().optional(),
            "privilegesRequired": t.string(),
            "impactScore": t.number(),
            "availabilityImpact": t.string(),
        }
    ).named(renames["CVSSIn"])
    types["CVSSOut"] = t.struct(
        {
            "authentication": t.string(),
            "userInteraction": t.string(),
            "confidentialityImpact": t.string(),
            "scope": t.string(),
            "baseScore": t.number().optional(),
            "integrityImpact": t.string(),
            "exploitabilityScore": t.number(),
            "attackComplexity": t.string(),
            "attackVector": t.string().optional(),
            "privilegesRequired": t.string(),
            "impactScore": t.number(),
            "availabilityImpact": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CVSSOut"])
    types["VersionIn"] = t.struct(
        {
            "revision": t.string().optional(),
            "name": t.string(),
            "fullName": t.string().optional(),
            "kind": t.string(),
            "inclusive": t.boolean().optional(),
            "epoch": t.integer().optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "revision": t.string().optional(),
            "name": t.string(),
            "fullName": t.string().optional(),
            "kind": t.string(),
            "inclusive": t.boolean().optional(),
            "epoch": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
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
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"] = t.struct(
        {"id": t.string()}
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"])
    types["SlsaBuilderIn"] = t.struct({"id": t.string()}).named(
        renames["SlsaBuilderIn"]
    )
    types["SlsaBuilderOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SlsaBuilderOut"])
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
    types["LicenseIn"] = t.struct(
        {"comments": t.string().optional(), "expression": t.string().optional()}
    ).named(renames["LicenseIn"])
    types["LicenseOut"] = t.struct(
        {
            "comments": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LicenseOut"])
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
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn"] = t.struct(
        {
            "environment": t.struct({"_": t.string().optional()}),
            "configSource": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn"]
            ),
            "parameters": t.struct({"_": t.string().optional()}),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut"] = t.struct(
        {
            "environment": t.struct({"_": t.string().optional()}),
            "configSource": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut"]
            ),
            "parameters": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut"])
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
    types["AnalyzePackagesRequestV1In"] = t.struct(
        {
            "packages": t.array(t.proxy(renames["PackageDataIn"])).optional(),
            "includeOsvData": t.boolean().optional(),
            "resourceUri": t.string(),
        }
    ).named(renames["AnalyzePackagesRequestV1In"])
    types["AnalyzePackagesRequestV1Out"] = t.struct(
        {
            "packages": t.array(t.proxy(renames["PackageDataOut"])).optional(),
            "includeOsvData": t.boolean().optional(),
            "resourceUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzePackagesRequestV1Out"])
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
    types["SlsaCompletenessIn"] = t.struct(
        {
            "arguments": t.boolean().optional(),
            "materials": t.boolean().optional(),
            "environment": t.boolean().optional(),
        }
    ).named(renames["SlsaCompletenessIn"])
    types["SlsaCompletenessOut"] = t.struct(
        {
            "arguments": t.boolean().optional(),
            "materials": t.boolean().optional(),
            "environment": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaCompletenessOut"])
    types["ImageOccurrenceIn"] = t.struct(
        {
            "baseResourceUrl": t.string().optional(),
            "distance": t.integer().optional(),
            "layerInfo": t.array(t.proxy(renames["LayerIn"])).optional(),
            "fingerprint": t.proxy(renames["FingerprintIn"]),
        }
    ).named(renames["ImageOccurrenceIn"])
    types["ImageOccurrenceOut"] = t.struct(
        {
            "baseResourceUrl": t.string().optional(),
            "distance": t.integer().optional(),
            "layerInfo": t.array(t.proxy(renames["LayerOut"])).optional(),
            "fingerprint": t.proxy(renames["FingerprintOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOccurrenceOut"])
    types["SubjectIn"] = t.struct(
        {
            "name": t.string(),
            "digest": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SubjectIn"])
    types["SubjectOut"] = t.struct(
        {
            "name": t.string(),
            "digest": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubjectOut"])
    types["LayerIn"] = t.struct(
        {"directive": t.string(), "arguments": t.string().optional()}
    ).named(renames["LayerIn"])
    types["LayerOut"] = t.struct(
        {
            "directive": t.string(),
            "arguments": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LayerOut"])
    types["SlsaRecipeIn"] = t.struct(
        {
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "entryPoint": t.string().optional(),
            "definedInMaterial": t.string().optional(),
            "type": t.string().optional(),
            "arguments": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SlsaRecipeIn"])
    types["SlsaRecipeOut"] = t.struct(
        {
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "entryPoint": t.string().optional(),
            "definedInMaterial": t.string().optional(),
            "type": t.string().optional(),
            "arguments": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaRecipeOut"])
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
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["CompletenessIn"] = t.struct(
        {
            "materials": t.boolean().optional(),
            "arguments": t.boolean().optional(),
            "environment": t.boolean().optional(),
        }
    ).named(renames["CompletenessIn"])
    types["CompletenessOut"] = t.struct(
        {
            "materials": t.boolean().optional(),
            "arguments": t.boolean().optional(),
            "environment": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompletenessOut"])
    types["BuildProvenanceIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "buildOptions": t.struct({"_": t.string().optional()}).optional(),
            "projectId": t.string().optional(),
            "builtArtifacts": t.array(t.proxy(renames["ArtifactIn"])).optional(),
            "triggerId": t.string().optional(),
            "creator": t.string().optional(),
            "commands": t.array(t.proxy(renames["CommandIn"])).optional(),
            "logsUri": t.string().optional(),
            "id": t.string(),
            "sourceProvenance": t.proxy(renames["SourceIn"]).optional(),
            "startTime": t.string().optional(),
            "builderVersion": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["BuildProvenanceIn"])
    types["BuildProvenanceOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "buildOptions": t.struct({"_": t.string().optional()}).optional(),
            "projectId": t.string().optional(),
            "builtArtifacts": t.array(t.proxy(renames["ArtifactOut"])).optional(),
            "triggerId": t.string().optional(),
            "creator": t.string().optional(),
            "commands": t.array(t.proxy(renames["CommandOut"])).optional(),
            "logsUri": t.string().optional(),
            "id": t.string(),
            "sourceProvenance": t.proxy(renames["SourceOut"]).optional(),
            "startTime": t.string().optional(),
            "builderVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildProvenanceOut"])
    types["SbomReferenceIntotoPredicateIn"] = t.struct(
        {
            "location": t.string().optional(),
            "digest": t.struct({"_": t.string().optional()}).optional(),
            "referrerId": t.string().optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["SbomReferenceIntotoPredicateIn"])
    types["SbomReferenceIntotoPredicateOut"] = t.struct(
        {
            "location": t.string().optional(),
            "digest": t.struct({"_": t.string().optional()}).optional(),
            "referrerId": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SbomReferenceIntotoPredicateOut"])
    types["PackageOccurrenceIn"] = t.struct(
        {
            "license": t.proxy(renames["LicenseIn"]).optional(),
            "location": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["PackageOccurrenceIn"])
    types["PackageOccurrenceOut"] = t.struct(
        {
            "cpeUri": t.string().optional(),
            "architecture": t.string().optional(),
            "license": t.proxy(renames["LicenseOut"]).optional(),
            "version": t.proxy(renames["VersionOut"]).optional(),
            "packageType": t.string().optional(),
            "location": t.array(t.proxy(renames["LocationOut"])).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageOccurrenceOut"])

    functions = {}
    functions["projectsLocationsScansAnalyzePackages"] = ondemandscanning.post(
        "v1/{parent}/scans:analyzePackages",
        t.struct(
            {
                "parent": t.string(),
                "packages": t.array(t.proxy(renames["PackageDataIn"])).optional(),
                "includeOsvData": t.boolean().optional(),
                "resourceUri": t.string(),
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
    functions["projectsLocationsOperationsGet"] = ondemandscanning.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsWait"] = ondemandscanning.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = ondemandscanning.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = ondemandscanning.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = ondemandscanning.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="ondemandscanning", renames=renames, types=types, functions=functions
    )
