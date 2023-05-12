from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_ondemandscanning() -> Import:
    ondemandscanning = HTTPRuntime("https://ondemandscanning.googleapis.com/")

    renames = {
        "ErrorResponse": "_ondemandscanning_1_ErrorResponse",
        "RemediationIn": "_ondemandscanning_2_RemediationIn",
        "RemediationOut": "_ondemandscanning_3_RemediationOut",
        "ListVulnerabilitiesResponseV1In": "_ondemandscanning_4_ListVulnerabilitiesResponseV1In",
        "ListVulnerabilitiesResponseV1Out": "_ondemandscanning_5_ListVulnerabilitiesResponseV1Out",
        "FileLocationIn": "_ondemandscanning_6_FileLocationIn",
        "FileLocationOut": "_ondemandscanning_7_FileLocationOut",
        "PackageVersionIn": "_ondemandscanning_8_PackageVersionIn",
        "PackageVersionOut": "_ondemandscanning_9_PackageVersionOut",
        "StatusIn": "_ondemandscanning_10_StatusIn",
        "StatusOut": "_ondemandscanning_11_StatusOut",
        "RelatedUrlIn": "_ondemandscanning_12_RelatedUrlIn",
        "RelatedUrlOut": "_ondemandscanning_13_RelatedUrlOut",
        "CommandIn": "_ondemandscanning_14_CommandIn",
        "CommandOut": "_ondemandscanning_15_CommandOut",
        "JustificationIn": "_ondemandscanning_16_JustificationIn",
        "JustificationOut": "_ondemandscanning_17_JustificationOut",
        "EnvelopeSignatureIn": "_ondemandscanning_18_EnvelopeSignatureIn",
        "EnvelopeSignatureOut": "_ondemandscanning_19_EnvelopeSignatureOut",
        "WindowsUpdateIn": "_ondemandscanning_20_WindowsUpdateIn",
        "WindowsUpdateOut": "_ondemandscanning_21_WindowsUpdateOut",
        "BuilderConfigIn": "_ondemandscanning_22_BuilderConfigIn",
        "BuilderConfigOut": "_ondemandscanning_23_BuilderConfigOut",
        "FingerprintIn": "_ondemandscanning_24_FingerprintIn",
        "FingerprintOut": "_ondemandscanning_25_FingerprintOut",
        "CompletenessIn": "_ondemandscanning_26_CompletenessIn",
        "CompletenessOut": "_ondemandscanning_27_CompletenessOut",
        "SourceContextIn": "_ondemandscanning_28_SourceContextIn",
        "SourceContextOut": "_ondemandscanning_29_SourceContextOut",
        "SlsaCompletenessIn": "_ondemandscanning_30_SlsaCompletenessIn",
        "SlsaCompletenessOut": "_ondemandscanning_31_SlsaCompletenessOut",
        "BuildProvenanceIn": "_ondemandscanning_32_BuildProvenanceIn",
        "BuildProvenanceOut": "_ondemandscanning_33_BuildProvenanceOut",
        "SubjectIn": "_ondemandscanning_34_SubjectIn",
        "SubjectOut": "_ondemandscanning_35_SubjectOut",
        "CategoryIn": "_ondemandscanning_36_CategoryIn",
        "CategoryOut": "_ondemandscanning_37_CategoryOut",
        "AliasContextIn": "_ondemandscanning_38_AliasContextIn",
        "AliasContextOut": "_ondemandscanning_39_AliasContextOut",
        "InTotoProvenanceIn": "_ondemandscanning_40_InTotoProvenanceIn",
        "InTotoProvenanceOut": "_ondemandscanning_41_InTotoProvenanceOut",
        "OccurrenceIn": "_ondemandscanning_42_OccurrenceIn",
        "OccurrenceOut": "_ondemandscanning_43_OccurrenceOut",
        "MetadataIn": "_ondemandscanning_44_MetadataIn",
        "MetadataOut": "_ondemandscanning_45_MetadataOut",
        "IdentityIn": "_ondemandscanning_46_IdentityIn",
        "IdentityOut": "_ondemandscanning_47_IdentityOut",
        "VexAssessmentIn": "_ondemandscanning_48_VexAssessmentIn",
        "VexAssessmentOut": "_ondemandscanning_49_VexAssessmentOut",
        "AnalyzePackagesMetadataV1In": "_ondemandscanning_50_AnalyzePackagesMetadataV1In",
        "AnalyzePackagesMetadataV1Out": "_ondemandscanning_51_AnalyzePackagesMetadataV1Out",
        "UpgradeDistributionIn": "_ondemandscanning_52_UpgradeDistributionIn",
        "UpgradeDistributionOut": "_ondemandscanning_53_UpgradeDistributionOut",
        "AttestationOccurrenceIn": "_ondemandscanning_54_AttestationOccurrenceIn",
        "AttestationOccurrenceOut": "_ondemandscanning_55_AttestationOccurrenceOut",
        "DiscoveryOccurrenceIn": "_ondemandscanning_56_DiscoveryOccurrenceIn",
        "DiscoveryOccurrenceOut": "_ondemandscanning_57_DiscoveryOccurrenceOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn": "_ondemandscanning_58_GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut": "_ondemandscanning_59_GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut",
        "ArtifactIn": "_ondemandscanning_60_ArtifactIn",
        "ArtifactOut": "_ondemandscanning_61_ArtifactOut",
        "PackageIssueIn": "_ondemandscanning_62_PackageIssueIn",
        "PackageIssueOut": "_ondemandscanning_63_PackageIssueOut",
        "RecipeIn": "_ondemandscanning_64_RecipeIn",
        "RecipeOut": "_ondemandscanning_65_RecipeOut",
        "CVSSIn": "_ondemandscanning_66_CVSSIn",
        "CVSSOut": "_ondemandscanning_67_CVSSOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn": "_ondemandscanning_68_GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut": "_ondemandscanning_69_GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut",
        "OperationIn": "_ondemandscanning_70_OperationIn",
        "OperationOut": "_ondemandscanning_71_OperationOut",
        "AnalyzePackagesResponseIn": "_ondemandscanning_72_AnalyzePackagesResponseIn",
        "AnalyzePackagesResponseOut": "_ondemandscanning_73_AnalyzePackagesResponseOut",
        "LayerIn": "_ondemandscanning_74_LayerIn",
        "LayerOut": "_ondemandscanning_75_LayerOut",
        "DeploymentOccurrenceIn": "_ondemandscanning_76_DeploymentOccurrenceIn",
        "DeploymentOccurrenceOut": "_ondemandscanning_77_DeploymentOccurrenceOut",
        "EnvelopeIn": "_ondemandscanning_78_EnvelopeIn",
        "EnvelopeOut": "_ondemandscanning_79_EnvelopeOut",
        "AnalyzePackagesMetadataIn": "_ondemandscanning_80_AnalyzePackagesMetadataIn",
        "AnalyzePackagesMetadataOut": "_ondemandscanning_81_AnalyzePackagesMetadataOut",
        "FileHashesIn": "_ondemandscanning_82_FileHashesIn",
        "FileHashesOut": "_ondemandscanning_83_FileHashesOut",
        "PackageDataIn": "_ondemandscanning_84_PackageDataIn",
        "PackageDataOut": "_ondemandscanning_85_PackageDataOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn": "_ondemandscanning_86_GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut": "_ondemandscanning_87_GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut",
        "MaterialIn": "_ondemandscanning_88_MaterialIn",
        "MaterialOut": "_ondemandscanning_89_MaterialOut",
        "LicenseIn": "_ondemandscanning_90_LicenseIn",
        "LicenseOut": "_ondemandscanning_91_LicenseOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn": "_ondemandscanning_92_GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut": "_ondemandscanning_93_GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut",
        "LanguagePackageDependencyIn": "_ondemandscanning_94_LanguagePackageDependencyIn",
        "LanguagePackageDependencyOut": "_ondemandscanning_95_LanguagePackageDependencyOut",
        "InTotoStatementIn": "_ondemandscanning_96_InTotoStatementIn",
        "InTotoStatementOut": "_ondemandscanning_97_InTotoStatementOut",
        "NonCompliantFileIn": "_ondemandscanning_98_NonCompliantFileIn",
        "NonCompliantFileOut": "_ondemandscanning_99_NonCompliantFileOut",
        "SlsaProvenanceIn": "_ondemandscanning_100_SlsaProvenanceIn",
        "SlsaProvenanceOut": "_ondemandscanning_101_SlsaProvenanceOut",
        "GitSourceContextIn": "_ondemandscanning_102_GitSourceContextIn",
        "GitSourceContextOut": "_ondemandscanning_103_GitSourceContextOut",
        "SlsaRecipeIn": "_ondemandscanning_104_SlsaRecipeIn",
        "SlsaRecipeOut": "_ondemandscanning_105_SlsaRecipeOut",
        "AnalyzePackagesRequestV1In": "_ondemandscanning_106_AnalyzePackagesRequestV1In",
        "AnalyzePackagesRequestV1Out": "_ondemandscanning_107_AnalyzePackagesRequestV1Out",
        "CloudRepoSourceContextIn": "_ondemandscanning_108_CloudRepoSourceContextIn",
        "CloudRepoSourceContextOut": "_ondemandscanning_109_CloudRepoSourceContextOut",
        "MaintainerIn": "_ondemandscanning_110_MaintainerIn",
        "MaintainerOut": "_ondemandscanning_111_MaintainerOut",
        "DSSEAttestationOccurrenceIn": "_ondemandscanning_112_DSSEAttestationOccurrenceIn",
        "DSSEAttestationOccurrenceOut": "_ondemandscanning_113_DSSEAttestationOccurrenceOut",
        "ListOperationsResponseIn": "_ondemandscanning_114_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_ondemandscanning_115_ListOperationsResponseOut",
        "HashIn": "_ondemandscanning_116_HashIn",
        "HashOut": "_ondemandscanning_117_HashOut",
        "RepoIdIn": "_ondemandscanning_118_RepoIdIn",
        "RepoIdOut": "_ondemandscanning_119_RepoIdOut",
        "JwtIn": "_ondemandscanning_120_JwtIn",
        "JwtOut": "_ondemandscanning_121_JwtOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn": "_ondemandscanning_122_GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut": "_ondemandscanning_123_GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut",
        "LocationIn": "_ondemandscanning_124_LocationIn",
        "LocationOut": "_ondemandscanning_125_LocationOut",
        "SourceIn": "_ondemandscanning_126_SourceIn",
        "SourceOut": "_ondemandscanning_127_SourceOut",
        "GrafeasV1FileLocationIn": "_ondemandscanning_128_GrafeasV1FileLocationIn",
        "GrafeasV1FileLocationOut": "_ondemandscanning_129_GrafeasV1FileLocationOut",
        "AnalysisCompletedIn": "_ondemandscanning_130_AnalysisCompletedIn",
        "AnalysisCompletedOut": "_ondemandscanning_131_AnalysisCompletedOut",
        "UpgradeOccurrenceIn": "_ondemandscanning_132_UpgradeOccurrenceIn",
        "UpgradeOccurrenceOut": "_ondemandscanning_133_UpgradeOccurrenceOut",
        "PackageOccurrenceIn": "_ondemandscanning_134_PackageOccurrenceIn",
        "PackageOccurrenceOut": "_ondemandscanning_135_PackageOccurrenceOut",
        "VulnerabilityOccurrenceIn": "_ondemandscanning_136_VulnerabilityOccurrenceIn",
        "VulnerabilityOccurrenceOut": "_ondemandscanning_137_VulnerabilityOccurrenceOut",
        "AnalyzePackagesResponseV1In": "_ondemandscanning_138_AnalyzePackagesResponseV1In",
        "AnalyzePackagesResponseV1Out": "_ondemandscanning_139_AnalyzePackagesResponseV1Out",
        "GerritSourceContextIn": "_ondemandscanning_140_GerritSourceContextIn",
        "GerritSourceContextOut": "_ondemandscanning_141_GerritSourceContextOut",
        "SBOMReferenceOccurrenceIn": "_ondemandscanning_142_SBOMReferenceOccurrenceIn",
        "SBOMReferenceOccurrenceOut": "_ondemandscanning_143_SBOMReferenceOccurrenceOut",
        "ProjectRepoIdIn": "_ondemandscanning_144_ProjectRepoIdIn",
        "ProjectRepoIdOut": "_ondemandscanning_145_ProjectRepoIdOut",
        "ComplianceOccurrenceIn": "_ondemandscanning_146_ComplianceOccurrenceIn",
        "ComplianceOccurrenceOut": "_ondemandscanning_147_ComplianceOccurrenceOut",
        "SignatureIn": "_ondemandscanning_148_SignatureIn",
        "SignatureOut": "_ondemandscanning_149_SignatureOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn": "_ondemandscanning_150_GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut": "_ondemandscanning_151_GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut",
        "BuildOccurrenceIn": "_ondemandscanning_152_BuildOccurrenceIn",
        "BuildOccurrenceOut": "_ondemandscanning_153_BuildOccurrenceOut",
        "SlsaProvenanceZeroTwoIn": "_ondemandscanning_154_SlsaProvenanceZeroTwoIn",
        "SlsaProvenanceZeroTwoOut": "_ondemandscanning_155_SlsaProvenanceZeroTwoOut",
        "SbomReferenceIntotoPredicateIn": "_ondemandscanning_156_SbomReferenceIntotoPredicateIn",
        "SbomReferenceIntotoPredicateOut": "_ondemandscanning_157_SbomReferenceIntotoPredicateOut",
        "ImageOccurrenceIn": "_ondemandscanning_158_ImageOccurrenceIn",
        "ImageOccurrenceOut": "_ondemandscanning_159_ImageOccurrenceOut",
        "SbomReferenceIntotoPayloadIn": "_ondemandscanning_160_SbomReferenceIntotoPayloadIn",
        "SbomReferenceIntotoPayloadOut": "_ondemandscanning_161_SbomReferenceIntotoPayloadOut",
        "EmptyIn": "_ondemandscanning_162_EmptyIn",
        "EmptyOut": "_ondemandscanning_163_EmptyOut",
        "SlsaBuilderIn": "_ondemandscanning_164_SlsaBuilderIn",
        "SlsaBuilderOut": "_ondemandscanning_165_SlsaBuilderOut",
        "VersionIn": "_ondemandscanning_166_VersionIn",
        "VersionOut": "_ondemandscanning_167_VersionOut",
        "SlsaMetadataIn": "_ondemandscanning_168_SlsaMetadataIn",
        "SlsaMetadataOut": "_ondemandscanning_169_SlsaMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RemediationIn"] = t.struct(
        {
            "remediationUri": t.proxy(renames["RelatedUrlIn"]).optional(),
            "remediationType": t.string().optional(),
            "details": t.string().optional(),
        }
    ).named(renames["RemediationIn"])
    types["RemediationOut"] = t.struct(
        {
            "remediationUri": t.proxy(renames["RelatedUrlOut"]).optional(),
            "remediationType": t.string().optional(),
            "details": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemediationOut"])
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
    types["FileLocationIn"] = t.struct({"filePath": t.string().optional()}).named(
        renames["FileLocationIn"]
    )
    types["FileLocationOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileLocationOut"])
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
    types["CommandIn"] = t.struct(
        {
            "dir": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "name": t.string(),
            "env": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["CommandIn"])
    types["CommandOut"] = t.struct(
        {
            "dir": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "name": t.string(),
            "env": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommandOut"])
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
    types["WindowsUpdateIn"] = t.struct(
        {
            "lastPublishedTimestamp": t.string().optional(),
            "title": t.string().optional(),
            "supportUrl": t.string().optional(),
            "categories": t.array(t.proxy(renames["CategoryIn"])).optional(),
            "identity": t.proxy(renames["IdentityIn"]),
            "description": t.string().optional(),
            "kbArticleIds": t.array(t.string()).optional(),
        }
    ).named(renames["WindowsUpdateIn"])
    types["WindowsUpdateOut"] = t.struct(
        {
            "lastPublishedTimestamp": t.string().optional(),
            "title": t.string().optional(),
            "supportUrl": t.string().optional(),
            "categories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "identity": t.proxy(renames["IdentityOut"]),
            "description": t.string().optional(),
            "kbArticleIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsUpdateOut"])
    types["BuilderConfigIn"] = t.struct({"id": t.string()}).named(
        renames["BuilderConfigIn"]
    )
    types["BuilderConfigOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BuilderConfigOut"])
    types["FingerprintIn"] = t.struct(
        {
            "v2Name": t.string().optional(),
            "v1Name": t.string(),
            "v2Blob": t.array(t.string()),
        }
    ).named(renames["FingerprintIn"])
    types["FingerprintOut"] = t.struct(
        {
            "v2Name": t.string().optional(),
            "v1Name": t.string(),
            "v2Blob": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FingerprintOut"])
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
    types["SourceContextIn"] = t.struct(
        {
            "git": t.proxy(renames["GitSourceContextIn"]).optional(),
            "gerrit": t.proxy(renames["GerritSourceContextIn"]).optional(),
            "cloudRepo": t.proxy(renames["CloudRepoSourceContextIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SourceContextIn"])
    types["SourceContextOut"] = t.struct(
        {
            "git": t.proxy(renames["GitSourceContextOut"]).optional(),
            "gerrit": t.proxy(renames["GerritSourceContextOut"]).optional(),
            "cloudRepo": t.proxy(renames["CloudRepoSourceContextOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
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
    types["BuildProvenanceIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "sourceProvenance": t.proxy(renames["SourceIn"]).optional(),
            "startTime": t.string().optional(),
            "builderVersion": t.string().optional(),
            "builtArtifacts": t.array(t.proxy(renames["ArtifactIn"])).optional(),
            "projectId": t.string().optional(),
            "id": t.string(),
            "commands": t.array(t.proxy(renames["CommandIn"])).optional(),
            "triggerId": t.string().optional(),
            "buildOptions": t.struct({"_": t.string().optional()}).optional(),
            "logsUri": t.string().optional(),
            "creator": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["BuildProvenanceIn"])
    types["BuildProvenanceOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "sourceProvenance": t.proxy(renames["SourceOut"]).optional(),
            "startTime": t.string().optional(),
            "builderVersion": t.string().optional(),
            "builtArtifacts": t.array(t.proxy(renames["ArtifactOut"])).optional(),
            "projectId": t.string().optional(),
            "id": t.string(),
            "commands": t.array(t.proxy(renames["CommandOut"])).optional(),
            "triggerId": t.string().optional(),
            "buildOptions": t.struct({"_": t.string().optional()}).optional(),
            "logsUri": t.string().optional(),
            "creator": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildProvenanceOut"])
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
    types["InTotoProvenanceIn"] = t.struct(
        {
            "builderConfig": t.proxy(renames["BuilderConfigIn"]).optional(),
            "recipe": t.proxy(renames["RecipeIn"]).optional(),
            "metadata": t.proxy(renames["MetadataIn"]),
            "materials": t.array(t.string()).optional(),
        }
    ).named(renames["InTotoProvenanceIn"])
    types["InTotoProvenanceOut"] = t.struct(
        {
            "builderConfig": t.proxy(renames["BuilderConfigOut"]).optional(),
            "recipe": t.proxy(renames["RecipeOut"]).optional(),
            "metadata": t.proxy(renames["MetadataOut"]),
            "materials": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InTotoProvenanceOut"])
    types["OccurrenceIn"] = t.struct(
        {
            "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
            "resourceUri": t.string(),
            "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
            "noteName": t.string(),
            "vulnerability": t.proxy(renames["VulnerabilityOccurrenceIn"]).optional(),
            "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
            "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceOccurrenceIn"]).optional(),
            "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
            "name": t.string().optional(),
            "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
            "dsseAttestation": t.proxy(
                renames["DSSEAttestationOccurrenceIn"]
            ).optional(),
            "createTime": t.string().optional(),
            "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
            "remediation": t.string().optional(),
            "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
            "kind": t.string().optional(),
            "updateTime": t.string().optional(),
            "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
        }
    ).named(renames["OccurrenceIn"])
    types["OccurrenceOut"] = t.struct(
        {
            "package": t.proxy(renames["PackageOccurrenceOut"]).optional(),
            "resourceUri": t.string(),
            "image": t.proxy(renames["ImageOccurrenceOut"]).optional(),
            "noteName": t.string(),
            "vulnerability": t.proxy(renames["VulnerabilityOccurrenceOut"]).optional(),
            "deployment": t.proxy(renames["DeploymentOccurrenceOut"]).optional(),
            "build": t.proxy(renames["BuildOccurrenceOut"]).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceOccurrenceOut"]).optional(),
            "envelope": t.proxy(renames["EnvelopeOut"]).optional(),
            "name": t.string().optional(),
            "attestation": t.proxy(renames["AttestationOccurrenceOut"]).optional(),
            "dsseAttestation": t.proxy(
                renames["DSSEAttestationOccurrenceOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "discovery": t.proxy(renames["DiscoveryOccurrenceOut"]).optional(),
            "remediation": t.string().optional(),
            "upgrade": t.proxy(renames["UpgradeOccurrenceOut"]).optional(),
            "kind": t.string().optional(),
            "updateTime": t.string().optional(),
            "compliance": t.proxy(renames["ComplianceOccurrenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OccurrenceOut"])
    types["MetadataIn"] = t.struct(
        {
            "completeness": t.proxy(renames["CompletenessIn"]).optional(),
            "buildInvocationId": t.string().optional(),
            "buildFinishedOn": t.string().optional(),
            "buildStartedOn": t.string().optional(),
            "reproducible": t.boolean().optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "completeness": t.proxy(renames["CompletenessOut"]).optional(),
            "buildInvocationId": t.string().optional(),
            "buildFinishedOn": t.string().optional(),
            "buildStartedOn": t.string().optional(),
            "reproducible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
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
    types["VexAssessmentIn"] = t.struct(
        {
            "relatedUris": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "noteName": t.string().optional(),
            "justification": t.proxy(renames["JustificationIn"]).optional(),
            "impacts": t.array(t.string()).optional(),
            "cve": t.string().optional(),
            "remediations": t.array(t.proxy(renames["RemediationIn"])).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["VexAssessmentIn"])
    types["VexAssessmentOut"] = t.struct(
        {
            "relatedUris": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "noteName": t.string().optional(),
            "justification": t.proxy(renames["JustificationOut"]).optional(),
            "impacts": t.array(t.string()).optional(),
            "cve": t.string().optional(),
            "remediations": t.array(t.proxy(renames["RemediationOut"])).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VexAssessmentOut"])
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
    types["UpgradeDistributionIn"] = t.struct(
        {
            "classification": t.string().optional(),
            "cve": t.array(t.string()).optional(),
            "severity": t.string().optional(),
            "cpeUri": t.string(),
        }
    ).named(renames["UpgradeDistributionIn"])
    types["UpgradeDistributionOut"] = t.struct(
        {
            "classification": t.string().optional(),
            "cve": t.array(t.string()).optional(),
            "severity": t.string().optional(),
            "cpeUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeDistributionOut"])
    types["AttestationOccurrenceIn"] = t.struct(
        {
            "jwts": t.array(t.proxy(renames["JwtIn"])).optional(),
            "serializedPayload": t.string(),
            "signatures": t.array(t.proxy(renames["SignatureIn"])).optional(),
        }
    ).named(renames["AttestationOccurrenceIn"])
    types["AttestationOccurrenceOut"] = t.struct(
        {
            "jwts": t.array(t.proxy(renames["JwtOut"])).optional(),
            "serializedPayload": t.string(),
            "signatures": t.array(t.proxy(renames["SignatureOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestationOccurrenceOut"])
    types["DiscoveryOccurrenceIn"] = t.struct(
        {
            "continuousAnalysis": t.string().optional(),
            "cpe": t.string().optional(),
            "analysisStatus": t.string().optional(),
            "lastScanTime": t.string().optional(),
            "analysisCompleted": t.proxy(renames["AnalysisCompletedIn"]),
            "analysisError": t.array(t.proxy(renames["StatusIn"])).optional(),
            "analysisStatusError": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["DiscoveryOccurrenceIn"])
    types["DiscoveryOccurrenceOut"] = t.struct(
        {
            "continuousAnalysis": t.string().optional(),
            "archiveTime": t.string().optional(),
            "cpe": t.string().optional(),
            "analysisStatus": t.string().optional(),
            "lastScanTime": t.string().optional(),
            "analysisCompleted": t.proxy(renames["AnalysisCompletedOut"]),
            "analysisError": t.array(t.proxy(renames["StatusOut"])).optional(),
            "analysisStatusError": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoveryOccurrenceOut"])
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
    types["ArtifactIn"] = t.struct(
        {
            "id": t.string().optional(),
            "checksum": t.string().optional(),
            "names": t.array(t.string()).optional(),
        }
    ).named(renames["ArtifactIn"])
    types["ArtifactOut"] = t.struct(
        {
            "id": t.string().optional(),
            "checksum": t.string().optional(),
            "names": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArtifactOut"])
    types["PackageIssueIn"] = t.struct(
        {
            "affectedPackage": t.string(),
            "affectedCpeUri": t.string(),
            "packageType": t.string().optional(),
            "fixedCpeUri": t.string().optional(),
            "fixedVersion": t.proxy(renames["VersionIn"]),
            "affectedVersion": t.proxy(renames["VersionIn"]),
            "fixAvailable": t.boolean().optional(),
            "fileLocation": t.array(
                t.proxy(renames["GrafeasV1FileLocationIn"])
            ).optional(),
            "fixedPackage": t.string().optional(),
        }
    ).named(renames["PackageIssueIn"])
    types["PackageIssueOut"] = t.struct(
        {
            "affectedPackage": t.string(),
            "affectedCpeUri": t.string(),
            "effectiveSeverity": t.string().optional(),
            "packageType": t.string().optional(),
            "fixedCpeUri": t.string().optional(),
            "fixedVersion": t.proxy(renames["VersionOut"]),
            "affectedVersion": t.proxy(renames["VersionOut"]),
            "fixAvailable": t.boolean().optional(),
            "fileLocation": t.array(
                t.proxy(renames["GrafeasV1FileLocationOut"])
            ).optional(),
            "fixedPackage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageIssueOut"])
    types["RecipeIn"] = t.struct(
        {
            "entryPoint": t.string().optional(),
            "environment": t.array(t.struct({"_": t.string().optional()})).optional(),
            "definedInMaterial": t.string().optional(),
            "arguments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["RecipeIn"])
    types["RecipeOut"] = t.struct(
        {
            "entryPoint": t.string().optional(),
            "environment": t.array(t.struct({"_": t.string().optional()})).optional(),
            "definedInMaterial": t.string().optional(),
            "arguments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecipeOut"])
    types["CVSSIn"] = t.struct(
        {
            "confidentialityImpact": t.string(),
            "scope": t.string(),
            "userInteraction": t.string(),
            "exploitabilityScore": t.number(),
            "privilegesRequired": t.string(),
            "authentication": t.string(),
            "integrityImpact": t.string(),
            "attackVector": t.string().optional(),
            "impactScore": t.number(),
            "baseScore": t.number().optional(),
            "attackComplexity": t.string(),
            "availabilityImpact": t.string(),
        }
    ).named(renames["CVSSIn"])
    types["CVSSOut"] = t.struct(
        {
            "confidentialityImpact": t.string(),
            "scope": t.string(),
            "userInteraction": t.string(),
            "exploitabilityScore": t.number(),
            "privilegesRequired": t.string(),
            "authentication": t.string(),
            "integrityImpact": t.string(),
            "attackVector": t.string().optional(),
            "impactScore": t.number(),
            "baseScore": t.number().optional(),
            "attackComplexity": t.string(),
            "availabilityImpact": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CVSSOut"])
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
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["AnalyzePackagesResponseIn"] = t.struct(
        {"scan": t.string().optional()}
    ).named(renames["AnalyzePackagesResponseIn"])
    types["AnalyzePackagesResponseOut"] = t.struct(
        {
            "scan": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzePackagesResponseOut"])
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
    types["DeploymentOccurrenceIn"] = t.struct(
        {
            "platform": t.string().optional(),
            "address": t.string().optional(),
            "resourceUri": t.array(t.string()).optional(),
            "undeployTime": t.string().optional(),
            "config": t.string().optional(),
            "deployTime": t.string(),
            "userEmail": t.string().optional(),
        }
    ).named(renames["DeploymentOccurrenceIn"])
    types["DeploymentOccurrenceOut"] = t.struct(
        {
            "platform": t.string().optional(),
            "address": t.string().optional(),
            "resourceUri": t.array(t.string()).optional(),
            "undeployTime": t.string().optional(),
            "config": t.string().optional(),
            "deployTime": t.string(),
            "userEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOccurrenceOut"])
    types["EnvelopeIn"] = t.struct(
        {
            "payloadType": t.string(),
            "payload": t.string(),
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureIn"])),
        }
    ).named(renames["EnvelopeIn"])
    types["EnvelopeOut"] = t.struct(
        {
            "payloadType": t.string(),
            "payload": t.string(),
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvelopeOut"])
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
    types["FileHashesIn"] = t.struct(
        {"fileHash": t.array(t.proxy(renames["HashIn"]))}
    ).named(renames["FileHashesIn"])
    types["FileHashesOut"] = t.struct(
        {
            "fileHash": t.array(t.proxy(renames["HashOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileHashesOut"])
    types["PackageDataIn"] = t.struct(
        {
            "cpeUri": t.string().optional(),
            "unused": t.string(),
            "dependencyChain": t.array(
                t.proxy(renames["LanguagePackageDependencyIn"])
            ).optional(),
            "sourceVersion": t.proxy(renames["PackageVersionIn"]).optional(),
            "os": t.string().optional(),
            "fileLocation": t.array(t.proxy(renames["FileLocationIn"])).optional(),
            "hashDigest": t.string().optional(),
            "osVersion": t.string().optional(),
            "package": t.string().optional(),
            "maintainer": t.proxy(renames["MaintainerIn"]).optional(),
            "binaryVersion": t.proxy(renames["PackageVersionIn"]).optional(),
            "version": t.string().optional(),
            "patchedCve": t.array(t.string()).optional(),
            "packageType": t.string().optional(),
            "architecture": t.string().optional(),
        }
    ).named(renames["PackageDataIn"])
    types["PackageDataOut"] = t.struct(
        {
            "cpeUri": t.string().optional(),
            "unused": t.string(),
            "dependencyChain": t.array(
                t.proxy(renames["LanguagePackageDependencyOut"])
            ).optional(),
            "sourceVersion": t.proxy(renames["PackageVersionOut"]).optional(),
            "os": t.string().optional(),
            "fileLocation": t.array(t.proxy(renames["FileLocationOut"])).optional(),
            "hashDigest": t.string().optional(),
            "osVersion": t.string().optional(),
            "package": t.string().optional(),
            "maintainer": t.proxy(renames["MaintainerOut"]).optional(),
            "binaryVersion": t.proxy(renames["PackageVersionOut"]).optional(),
            "version": t.string().optional(),
            "patchedCve": t.array(t.string()).optional(),
            "packageType": t.string().optional(),
            "architecture": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageDataOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn"] = t.struct(
        {
            "uri": t.string(),
            "digest": t.struct({"_": t.string().optional()}),
            "entryPoint": t.string(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut"] = t.struct(
        {
            "uri": t.string(),
            "digest": t.struct({"_": t.string().optional()}),
            "entryPoint": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut"])
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
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"] = t.struct(
        {
            "buildFinishedOn": t.string(),
            "completeness": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"]
            ),
            "buildStartedOn": t.string(),
            "buildInvocationId": t.string(),
            "reproducible": t.boolean(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"] = t.struct(
        {
            "buildFinishedOn": t.string(),
            "completeness": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"]
            ),
            "buildStartedOn": t.string(),
            "buildInvocationId": t.string(),
            "reproducible": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"])
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
    types["InTotoStatementIn"] = t.struct(
        {
            "provenance": t.proxy(renames["InTotoProvenanceIn"]),
            "predicateType": t.string().optional(),
            "slsaProvenance": t.proxy(renames["SlsaProvenanceIn"]),
            "_type": t.string().optional(),
            "slsaProvenanceZeroTwo": t.proxy(renames["SlsaProvenanceZeroTwoIn"]),
            "subject": t.array(t.proxy(renames["SubjectIn"])),
        }
    ).named(renames["InTotoStatementIn"])
    types["InTotoStatementOut"] = t.struct(
        {
            "provenance": t.proxy(renames["InTotoProvenanceOut"]),
            "predicateType": t.string().optional(),
            "slsaProvenance": t.proxy(renames["SlsaProvenanceOut"]),
            "_type": t.string().optional(),
            "slsaProvenanceZeroTwo": t.proxy(renames["SlsaProvenanceZeroTwoOut"]),
            "subject": t.array(t.proxy(renames["SubjectOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InTotoStatementOut"])
    types["NonCompliantFileIn"] = t.struct(
        {
            "reason": t.string().optional(),
            "displayCommand": t.string().optional(),
            "path": t.string().optional(),
        }
    ).named(renames["NonCompliantFileIn"])
    types["NonCompliantFileOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "displayCommand": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonCompliantFileOut"])
    types["SlsaProvenanceIn"] = t.struct(
        {
            "metadata": t.proxy(renames["SlsaMetadataIn"]),
            "materials": t.array(t.proxy(renames["MaterialIn"])).optional(),
            "recipe": t.proxy(renames["SlsaRecipeIn"]).optional(),
            "builder": t.proxy(renames["SlsaBuilderIn"]).optional(),
        }
    ).named(renames["SlsaProvenanceIn"])
    types["SlsaProvenanceOut"] = t.struct(
        {
            "metadata": t.proxy(renames["SlsaMetadataOut"]),
            "materials": t.array(t.proxy(renames["MaterialOut"])).optional(),
            "recipe": t.proxy(renames["SlsaRecipeOut"]).optional(),
            "builder": t.proxy(renames["SlsaBuilderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaProvenanceOut"])
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
    types["SlsaRecipeIn"] = t.struct(
        {
            "definedInMaterial": t.string().optional(),
            "entryPoint": t.string().optional(),
            "arguments": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SlsaRecipeIn"])
    types["SlsaRecipeOut"] = t.struct(
        {
            "definedInMaterial": t.string().optional(),
            "entryPoint": t.string().optional(),
            "arguments": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaRecipeOut"])
    types["AnalyzePackagesRequestV1In"] = t.struct(
        {
            "includeOsvData": t.boolean().optional(),
            "packages": t.array(t.proxy(renames["PackageDataIn"])).optional(),
            "resourceUri": t.string(),
        }
    ).named(renames["AnalyzePackagesRequestV1In"])
    types["AnalyzePackagesRequestV1Out"] = t.struct(
        {
            "includeOsvData": t.boolean().optional(),
            "packages": t.array(t.proxy(renames["PackageDataOut"])).optional(),
            "resourceUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzePackagesRequestV1Out"])
    types["CloudRepoSourceContextIn"] = t.struct(
        {
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
            "repoId": t.proxy(renames["RepoIdIn"]).optional(),
            "revisionId": t.string().optional(),
        }
    ).named(renames["CloudRepoSourceContextIn"])
    types["CloudRepoSourceContextOut"] = t.struct(
        {
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "repoId": t.proxy(renames["RepoIdOut"]).optional(),
            "revisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRepoSourceContextOut"])
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
    types["JwtIn"] = t.struct({"compactJwt": t.string().optional()}).named(
        renames["JwtIn"]
    )
    types["JwtOut"] = t.struct(
        {
            "compactJwt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"] = t.struct(
        {
            "parameters": t.boolean(),
            "environment": t.boolean(),
            "materials": t.boolean(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"] = t.struct(
        {
            "parameters": t.boolean(),
            "environment": t.boolean(),
            "materials": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"])
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
    types["SourceIn"] = t.struct(
        {
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "context": t.proxy(renames["SourceContextIn"]).optional(),
            "additionalContexts": t.array(
                t.proxy(renames["SourceContextIn"])
            ).optional(),
            "artifactStorageSourceUri": t.string().optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "context": t.proxy(renames["SourceContextOut"]).optional(),
            "additionalContexts": t.array(
                t.proxy(renames["SourceContextOut"])
            ).optional(),
            "artifactStorageSourceUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["GrafeasV1FileLocationIn"] = t.struct(
        {"filePath": t.string().optional()}
    ).named(renames["GrafeasV1FileLocationIn"])
    types["GrafeasV1FileLocationOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1FileLocationOut"])
    types["AnalysisCompletedIn"] = t.struct(
        {"analysisType": t.array(t.string())}
    ).named(renames["AnalysisCompletedIn"])
    types["AnalysisCompletedOut"] = t.struct(
        {
            "analysisType": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalysisCompletedOut"])
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
    types["PackageOccurrenceIn"] = t.struct(
        {
            "location": t.array(t.proxy(renames["LocationIn"])).optional(),
            "license": t.proxy(renames["LicenseIn"]).optional(),
        }
    ).named(renames["PackageOccurrenceIn"])
    types["PackageOccurrenceOut"] = t.struct(
        {
            "version": t.proxy(renames["VersionOut"]).optional(),
            "architecture": t.string().optional(),
            "packageType": t.string().optional(),
            "name": t.string(),
            "location": t.array(t.proxy(renames["LocationOut"])).optional(),
            "license": t.proxy(renames["LicenseOut"]).optional(),
            "cpeUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageOccurrenceOut"])
    types["VulnerabilityOccurrenceIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "packageIssue": t.array(t.proxy(renames["PackageIssueIn"])),
            "cvssV2": t.proxy(renames["CVSSIn"]).optional(),
            "cvssVersion": t.string().optional(),
            "type": t.string().optional(),
            "cvssScore": t.number().optional(),
            "effectiveSeverity": t.string().optional(),
            "fixAvailable": t.boolean().optional(),
            "shortDescription": t.string().optional(),
            "longDescription": t.string().optional(),
            "vexAssessment": t.proxy(renames["VexAssessmentIn"]),
            "relatedUrls": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "cvssv3": t.proxy(renames["CVSSIn"]).optional(),
        }
    ).named(renames["VulnerabilityOccurrenceIn"])
    types["VulnerabilityOccurrenceOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "packageIssue": t.array(t.proxy(renames["PackageIssueOut"])),
            "cvssV2": t.proxy(renames["CVSSOut"]).optional(),
            "cvssVersion": t.string().optional(),
            "type": t.string().optional(),
            "cvssScore": t.number().optional(),
            "effectiveSeverity": t.string().optional(),
            "fixAvailable": t.boolean().optional(),
            "shortDescription": t.string().optional(),
            "longDescription": t.string().optional(),
            "vexAssessment": t.proxy(renames["VexAssessmentOut"]),
            "relatedUrls": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "cvssv3": t.proxy(renames["CVSSOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityOccurrenceOut"])
    types["AnalyzePackagesResponseV1In"] = t.struct(
        {"scan": t.string().optional()}
    ).named(renames["AnalyzePackagesResponseV1In"])
    types["AnalyzePackagesResponseV1Out"] = t.struct(
        {
            "scan": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzePackagesResponseV1Out"])
    types["GerritSourceContextIn"] = t.struct(
        {
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
            "hostUri": t.string().optional(),
            "revisionId": t.string().optional(),
            "gerritProject": t.string().optional(),
        }
    ).named(renames["GerritSourceContextIn"])
    types["GerritSourceContextOut"] = t.struct(
        {
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "hostUri": t.string().optional(),
            "revisionId": t.string().optional(),
            "gerritProject": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GerritSourceContextOut"])
    types["SBOMReferenceOccurrenceIn"] = t.struct(
        {
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureIn"])).optional(),
            "payloadType": t.string().optional(),
            "payload": t.proxy(renames["SbomReferenceIntotoPayloadIn"]).optional(),
        }
    ).named(renames["SBOMReferenceOccurrenceIn"])
    types["SBOMReferenceOccurrenceOut"] = t.struct(
        {
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureOut"])).optional(),
            "payloadType": t.string().optional(),
            "payload": t.proxy(renames["SbomReferenceIntotoPayloadOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SBOMReferenceOccurrenceOut"])
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
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"] = t.struct(
        {"id": t.string()}
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"])
    types["BuildOccurrenceIn"] = t.struct(
        {
            "provenance": t.proxy(renames["BuildProvenanceIn"]).optional(),
            "provenanceBytes": t.string().optional(),
            "intotoProvenance": t.proxy(renames["InTotoProvenanceIn"]).optional(),
            "intotoStatement": t.proxy(renames["InTotoStatementIn"]).optional(),
        }
    ).named(renames["BuildOccurrenceIn"])
    types["BuildOccurrenceOut"] = t.struct(
        {
            "provenance": t.proxy(renames["BuildProvenanceOut"]).optional(),
            "provenanceBytes": t.string().optional(),
            "intotoProvenance": t.proxy(renames["InTotoProvenanceOut"]).optional(),
            "intotoStatement": t.proxy(renames["InTotoStatementOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOccurrenceOut"])
    types["SlsaProvenanceZeroTwoIn"] = t.struct(
        {
            "invocation": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn"]
            ),
            "buildType": t.string(),
            "builder": t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"]),
            "buildConfig": t.struct({"_": t.string().optional()}),
            "metadata": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"]
            ),
            "materials": t.array(
                t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn"])
            ),
        }
    ).named(renames["SlsaProvenanceZeroTwoIn"])
    types["SlsaProvenanceZeroTwoOut"] = t.struct(
        {
            "invocation": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut"]
            ),
            "buildType": t.string(),
            "builder": t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"]),
            "buildConfig": t.struct({"_": t.string().optional()}),
            "metadata": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"]
            ),
            "materials": t.array(
                t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaProvenanceZeroTwoOut"])
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
    types["ImageOccurrenceIn"] = t.struct(
        {
            "layerInfo": t.array(t.proxy(renames["LayerIn"])).optional(),
            "distance": t.integer().optional(),
            "baseResourceUrl": t.string().optional(),
            "fingerprint": t.proxy(renames["FingerprintIn"]),
        }
    ).named(renames["ImageOccurrenceIn"])
    types["ImageOccurrenceOut"] = t.struct(
        {
            "layerInfo": t.array(t.proxy(renames["LayerOut"])).optional(),
            "distance": t.integer().optional(),
            "baseResourceUrl": t.string().optional(),
            "fingerprint": t.proxy(renames["FingerprintOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOccurrenceOut"])
    types["SbomReferenceIntotoPayloadIn"] = t.struct(
        {
            "subject": t.array(t.proxy(renames["SubjectIn"])).optional(),
            "_type": t.string().optional(),
            "predicateType": t.string().optional(),
            "predicate": t.proxy(renames["SbomReferenceIntotoPredicateIn"]).optional(),
        }
    ).named(renames["SbomReferenceIntotoPayloadIn"])
    types["SbomReferenceIntotoPayloadOut"] = t.struct(
        {
            "subject": t.array(t.proxy(renames["SubjectOut"])).optional(),
            "_type": t.string().optional(),
            "predicateType": t.string().optional(),
            "predicate": t.proxy(renames["SbomReferenceIntotoPredicateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SbomReferenceIntotoPayloadOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["SlsaBuilderIn"] = t.struct({"id": t.string()}).named(
        renames["SlsaBuilderIn"]
    )
    types["SlsaBuilderOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SlsaBuilderOut"])
    types["VersionIn"] = t.struct(
        {
            "name": t.string(),
            "inclusive": t.boolean().optional(),
            "fullName": t.string().optional(),
            "revision": t.string().optional(),
            "epoch": t.integer().optional(),
            "kind": t.string(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "name": t.string(),
            "inclusive": t.boolean().optional(),
            "fullName": t.string().optional(),
            "revision": t.string().optional(),
            "epoch": t.integer().optional(),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
    types["SlsaMetadataIn"] = t.struct(
        {
            "reproducible": t.boolean().optional(),
            "buildFinishedOn": t.string().optional(),
            "buildStartedOn": t.string().optional(),
            "completeness": t.proxy(renames["SlsaCompletenessIn"]).optional(),
            "buildInvocationId": t.string().optional(),
        }
    ).named(renames["SlsaMetadataIn"])
    types["SlsaMetadataOut"] = t.struct(
        {
            "reproducible": t.boolean().optional(),
            "buildFinishedOn": t.string().optional(),
            "buildStartedOn": t.string().optional(),
            "completeness": t.proxy(renames["SlsaCompletenessOut"]).optional(),
            "buildInvocationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaMetadataOut"])

    functions = {}
    functions["projectsLocationsOperationsDelete"] = ondemandscanning.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = ondemandscanning.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
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
                "packages": t.array(t.proxy(renames["PackageDataIn"])).optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
