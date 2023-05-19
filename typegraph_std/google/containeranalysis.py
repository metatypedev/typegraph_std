from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_containeranalysis() -> Import:
    containeranalysis = HTTPRuntime("https://containeranalysis.googleapis.com/")

    renames = {
        "ErrorResponse": "_containeranalysis_1_ErrorResponse",
        "SubjectIn": "_containeranalysis_2_SubjectIn",
        "SubjectOut": "_containeranalysis_3_SubjectOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsIn": "_containeranalysis_4_ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut": "_containeranalysis_5_ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut",
        "AnalysisCompletedIn": "_containeranalysis_6_AnalysisCompletedIn",
        "AnalysisCompletedOut": "_containeranalysis_7_AnalysisCompletedOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1HashIn": "_containeranalysis_8_ContaineranalysisGoogleDevtoolsCloudbuildV1HashIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1HashOut": "_containeranalysis_9_ContaineranalysisGoogleDevtoolsCloudbuildV1HashOut",
        "BuildProvenanceIn": "_containeranalysis_10_BuildProvenanceIn",
        "BuildProvenanceOut": "_containeranalysis_11_BuildProvenanceOut",
        "SbomReferenceIntotoPayloadIn": "_containeranalysis_12_SbomReferenceIntotoPayloadIn",
        "SbomReferenceIntotoPayloadOut": "_containeranalysis_13_SbomReferenceIntotoPayloadOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigIn": "_containeranalysis_14_ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigOut": "_containeranalysis_15_ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigOut",
        "SourceIn": "_containeranalysis_16_SourceIn",
        "SourceOut": "_containeranalysis_17_SourceOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn": "_containeranalysis_18_GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut": "_containeranalysis_19_GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut",
        "DistributionIn": "_containeranalysis_20_DistributionIn",
        "DistributionOut": "_containeranalysis_21_DistributionOut",
        "ComplianceNoteIn": "_containeranalysis_22_ComplianceNoteIn",
        "ComplianceNoteOut": "_containeranalysis_23_ComplianceNoteOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn": "_containeranalysis_24_GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut": "_containeranalysis_25_GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildIn": "_containeranalysis_26_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOut": "_containeranalysis_27_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOut",
        "ExprIn": "_containeranalysis_28_ExprIn",
        "ExprOut": "_containeranalysis_29_ExprOut",
        "HashIn": "_containeranalysis_30_HashIn",
        "HashOut": "_containeranalysis_31_HashOut",
        "DeploymentOccurrenceIn": "_containeranalysis_32_DeploymentOccurrenceIn",
        "DeploymentOccurrenceOut": "_containeranalysis_33_DeploymentOccurrenceOut",
        "SlsaBuilderIn": "_containeranalysis_34_SlsaBuilderIn",
        "SlsaBuilderOut": "_containeranalysis_35_SlsaBuilderOut",
        "CommandIn": "_containeranalysis_36_CommandIn",
        "CommandOut": "_containeranalysis_37_CommandOut",
        "MetadataIn": "_containeranalysis_38_MetadataIn",
        "MetadataOut": "_containeranalysis_39_MetadataOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn": "_containeranalysis_40_GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut": "_containeranalysis_41_GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut",
        "BuildOccurrenceIn": "_containeranalysis_42_BuildOccurrenceIn",
        "BuildOccurrenceOut": "_containeranalysis_43_BuildOccurrenceOut",
        "VulnerabilityNoteIn": "_containeranalysis_44_VulnerabilityNoteIn",
        "VulnerabilityNoteOut": "_containeranalysis_45_VulnerabilityNoteOut",
        "AttestationNoteIn": "_containeranalysis_46_AttestationNoteIn",
        "AttestationNoteOut": "_containeranalysis_47_AttestationNoteOut",
        "SbomReferenceIntotoPredicateIn": "_containeranalysis_48_SbomReferenceIntotoPredicateIn",
        "SbomReferenceIntotoPredicateOut": "_containeranalysis_49_SbomReferenceIntotoPredicateOut",
        "InTotoProvenanceIn": "_containeranalysis_50_InTotoProvenanceIn",
        "InTotoProvenanceOut": "_containeranalysis_51_InTotoProvenanceOut",
        "RelatedUrlIn": "_containeranalysis_52_RelatedUrlIn",
        "RelatedUrlOut": "_containeranalysis_53_RelatedUrlOut",
        "DiscoveryOccurrenceIn": "_containeranalysis_54_DiscoveryOccurrenceIn",
        "DiscoveryOccurrenceOut": "_containeranalysis_55_DiscoveryOccurrenceOut",
        "HintIn": "_containeranalysis_56_HintIn",
        "HintOut": "_containeranalysis_57_HintOut",
        "BuildNoteIn": "_containeranalysis_58_BuildNoteIn",
        "BuildNoteOut": "_containeranalysis_59_BuildNoteOut",
        "BatchCreateNotesResponseIn": "_containeranalysis_60_BatchCreateNotesResponseIn",
        "BatchCreateNotesResponseOut": "_containeranalysis_61_BatchCreateNotesResponseOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultIn": "_containeranalysis_62_ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultOut": "_containeranalysis_63_ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultOut",
        "AliasContextIn": "_containeranalysis_64_AliasContextIn",
        "AliasContextOut": "_containeranalysis_65_AliasContextOut",
        "AssessmentIn": "_containeranalysis_66_AssessmentIn",
        "AssessmentOut": "_containeranalysis_67_AssessmentOut",
        "BindingIn": "_containeranalysis_68_BindingIn",
        "BindingOut": "_containeranalysis_69_BindingOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageIn": "_containeranalysis_70_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageOut": "_containeranalysis_71_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageOut",
        "CVSSv3In": "_containeranalysis_72_CVSSv3In",
        "CVSSv3Out": "_containeranalysis_73_CVSSv3Out",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsIn": "_containeranalysis_74_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsOut": "_containeranalysis_75_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsOut",
        "SBOMReferenceOccurrenceIn": "_containeranalysis_76_SBOMReferenceOccurrenceIn",
        "SBOMReferenceOccurrenceOut": "_containeranalysis_77_SBOMReferenceOccurrenceOut",
        "ProjectRepoIdIn": "_containeranalysis_78_ProjectRepoIdIn",
        "ProjectRepoIdOut": "_containeranalysis_79_ProjectRepoIdOut",
        "VolumeIn": "_containeranalysis_80_VolumeIn",
        "VolumeOut": "_containeranalysis_81_VolumeOut",
        "GetIamPolicyRequestIn": "_containeranalysis_82_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_containeranalysis_83_GetIamPolicyRequestOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceIn": "_containeranalysis_84_ContaineranalysisGoogleDevtoolsCloudbuildV1SourceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceOut": "_containeranalysis_85_ContaineranalysisGoogleDevtoolsCloudbuildV1SourceOut",
        "SourceContextIn": "_containeranalysis_86_SourceContextIn",
        "SourceContextOut": "_containeranalysis_87_SourceContextOut",
        "ImageOccurrenceIn": "_containeranalysis_88_ImageOccurrenceIn",
        "ImageOccurrenceOut": "_containeranalysis_89_ImageOccurrenceOut",
        "CategoryIn": "_containeranalysis_90_CategoryIn",
        "CategoryOut": "_containeranalysis_91_CategoryOut",
        "FixableTotalByDigestIn": "_containeranalysis_92_FixableTotalByDigestIn",
        "FixableTotalByDigestOut": "_containeranalysis_93_FixableTotalByDigestOut",
        "ProductIn": "_containeranalysis_94_ProductIn",
        "ProductOut": "_containeranalysis_95_ProductOut",
        "GitSourceContextIn": "_containeranalysis_96_GitSourceContextIn",
        "GitSourceContextOut": "_containeranalysis_97_GitSourceContextOut",
        "TimeSpanIn": "_containeranalysis_98_TimeSpanIn",
        "TimeSpanOut": "_containeranalysis_99_TimeSpanOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn": "_containeranalysis_100_ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut": "_containeranalysis_101_ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut",
        "DeploymentNoteIn": "_containeranalysis_102_DeploymentNoteIn",
        "DeploymentNoteOut": "_containeranalysis_103_DeploymentNoteOut",
        "BatchCreateNotesRequestIn": "_containeranalysis_104_BatchCreateNotesRequestIn",
        "BatchCreateNotesRequestOut": "_containeranalysis_105_BatchCreateNotesRequestOut",
        "DSSEHintIn": "_containeranalysis_106_DSSEHintIn",
        "DSSEHintOut": "_containeranalysis_107_DSSEHintOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceIn": "_containeranalysis_108_ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut": "_containeranalysis_109_ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageIn": "_containeranalysis_110_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageOut": "_containeranalysis_111_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageOut",
        "UpgradeOccurrenceIn": "_containeranalysis_112_UpgradeOccurrenceIn",
        "UpgradeOccurrenceOut": "_containeranalysis_113_UpgradeOccurrenceOut",
        "FingerprintIn": "_containeranalysis_114_FingerprintIn",
        "FingerprintOut": "_containeranalysis_115_FingerprintOut",
        "TestIamPermissionsRequestIn": "_containeranalysis_116_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_containeranalysis_117_TestIamPermissionsRequestOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactIn": "_containeranalysis_118_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactOut": "_containeranalysis_119_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsIn": "_containeranalysis_120_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOut": "_containeranalysis_121_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOut",
        "ComplianceOccurrenceIn": "_containeranalysis_122_ComplianceOccurrenceIn",
        "ComplianceOccurrenceOut": "_containeranalysis_123_ComplianceOccurrenceOut",
        "GrafeasV1FileLocationIn": "_containeranalysis_124_GrafeasV1FileLocationIn",
        "GrafeasV1FileLocationOut": "_containeranalysis_125_GrafeasV1FileLocationOut",
        "VulnerabilityOccurrencesSummaryIn": "_containeranalysis_126_VulnerabilityOccurrencesSummaryIn",
        "VulnerabilityOccurrencesSummaryOut": "_containeranalysis_127_VulnerabilityOccurrencesSummaryOut",
        "UpgradeDistributionIn": "_containeranalysis_128_UpgradeDistributionIn",
        "UpgradeDistributionOut": "_containeranalysis_129_UpgradeDistributionOut",
        "EmptyIn": "_containeranalysis_130_EmptyIn",
        "EmptyOut": "_containeranalysis_131_EmptyOut",
        "SlsaProvenanceZeroTwoIn": "_containeranalysis_132_SlsaProvenanceZeroTwoIn",
        "SlsaProvenanceZeroTwoOut": "_containeranalysis_133_SlsaProvenanceZeroTwoOut",
        "VexAssessmentIn": "_containeranalysis_134_VexAssessmentIn",
        "VexAssessmentOut": "_containeranalysis_135_VexAssessmentOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsIn": "_containeranalysis_136_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsOut": "_containeranalysis_137_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionIn": "_containeranalysis_138_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionOut": "_containeranalysis_139_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn": "_containeranalysis_140_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut": "_containeranalysis_141_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut",
        "JwtIn": "_containeranalysis_142_JwtIn",
        "JwtOut": "_containeranalysis_143_JwtOut",
        "VulnerabilityOccurrenceIn": "_containeranalysis_144_VulnerabilityOccurrenceIn",
        "VulnerabilityOccurrenceOut": "_containeranalysis_145_VulnerabilityOccurrenceOut",
        "SetIamPolicyRequestIn": "_containeranalysis_146_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_containeranalysis_147_SetIamPolicyRequestOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageIn": "_containeranalysis_148_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageOut": "_containeranalysis_149_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageOut",
        "TestIamPermissionsResponseIn": "_containeranalysis_150_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_containeranalysis_151_TestIamPermissionsResponseOut",
        "CisBenchmarkIn": "_containeranalysis_152_CisBenchmarkIn",
        "CisBenchmarkOut": "_containeranalysis_153_CisBenchmarkOut",
        "BuildStepIn": "_containeranalysis_154_BuildStepIn",
        "BuildStepOut": "_containeranalysis_155_BuildStepOut",
        "RepoIdIn": "_containeranalysis_156_RepoIdIn",
        "RepoIdOut": "_containeranalysis_157_RepoIdOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn": "_containeranalysis_158_ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut": "_containeranalysis_159_ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut",
        "ComplianceVersionIn": "_containeranalysis_160_ComplianceVersionIn",
        "ComplianceVersionOut": "_containeranalysis_161_ComplianceVersionOut",
        "StatusIn": "_containeranalysis_162_StatusIn",
        "StatusOut": "_containeranalysis_163_StatusOut",
        "MaterialIn": "_containeranalysis_164_MaterialIn",
        "MaterialOut": "_containeranalysis_165_MaterialOut",
        "BatchCreateOccurrencesResponseIn": "_containeranalysis_166_BatchCreateOccurrencesResponseIn",
        "BatchCreateOccurrencesResponseOut": "_containeranalysis_167_BatchCreateOccurrencesResponseOut",
        "GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataIn": "_containeranalysis_168_GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataIn",
        "GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataOut": "_containeranalysis_169_GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretIn": "_containeranalysis_170_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretOut": "_containeranalysis_171_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretOut",
        "PackageNoteIn": "_containeranalysis_172_PackageNoteIn",
        "PackageNoteOut": "_containeranalysis_173_PackageNoteOut",
        "RecipeIn": "_containeranalysis_174_RecipeIn",
        "RecipeOut": "_containeranalysis_175_RecipeOut",
        "SBOMReferenceNoteIn": "_containeranalysis_176_SBOMReferenceNoteIn",
        "SBOMReferenceNoteOut": "_containeranalysis_177_SBOMReferenceNoteOut",
        "PackageOccurrenceIn": "_containeranalysis_178_PackageOccurrenceIn",
        "PackageOccurrenceOut": "_containeranalysis_179_PackageOccurrenceOut",
        "DetailIn": "_containeranalysis_180_DetailIn",
        "DetailOut": "_containeranalysis_181_DetailOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretIn": "_containeranalysis_182_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretOut": "_containeranalysis_183_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretOut",
        "WindowsDetailIn": "_containeranalysis_184_WindowsDetailIn",
        "WindowsDetailOut": "_containeranalysis_185_WindowsDetailOut",
        "SlsaRecipeIn": "_containeranalysis_186_SlsaRecipeIn",
        "SlsaRecipeOut": "_containeranalysis_187_SlsaRecipeOut",
        "PackageIssueIn": "_containeranalysis_188_PackageIssueIn",
        "PackageIssueOut": "_containeranalysis_189_PackageIssueOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn": "_containeranalysis_190_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut": "_containeranalysis_191_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut",
        "NonCompliantFileIn": "_containeranalysis_192_NonCompliantFileIn",
        "NonCompliantFileOut": "_containeranalysis_193_NonCompliantFileOut",
        "FileHashesIn": "_containeranalysis_194_FileHashesIn",
        "FileHashesOut": "_containeranalysis_195_FileHashesOut",
        "VulnerabilityAssessmentNoteIn": "_containeranalysis_196_VulnerabilityAssessmentNoteIn",
        "VulnerabilityAssessmentNoteOut": "_containeranalysis_197_VulnerabilityAssessmentNoteOut",
        "RemediationIn": "_containeranalysis_198_RemediationIn",
        "RemediationOut": "_containeranalysis_199_RemediationOut",
        "DigestIn": "_containeranalysis_200_DigestIn",
        "DigestOut": "_containeranalysis_201_DigestOut",
        "GetPolicyOptionsIn": "_containeranalysis_202_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_containeranalysis_203_GetPolicyOptionsOut",
        "KnowledgeBaseIn": "_containeranalysis_204_KnowledgeBaseIn",
        "KnowledgeBaseOut": "_containeranalysis_205_KnowledgeBaseOut",
        "JustificationIn": "_containeranalysis_206_JustificationIn",
        "JustificationOut": "_containeranalysis_207_JustificationOut",
        "CVSSIn": "_containeranalysis_208_CVSSIn",
        "CVSSOut": "_containeranalysis_209_CVSSOut",
        "DSSEAttestationNoteIn": "_containeranalysis_210_DSSEAttestationNoteIn",
        "DSSEAttestationNoteOut": "_containeranalysis_211_DSSEAttestationNoteOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn": "_containeranalysis_212_GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut": "_containeranalysis_213_GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut",
        "LocationIn": "_containeranalysis_214_LocationIn",
        "LocationOut": "_containeranalysis_215_LocationOut",
        "PolicyIn": "_containeranalysis_216_PolicyIn",
        "PolicyOut": "_containeranalysis_217_PolicyOut",
        "UpgradeNoteIn": "_containeranalysis_218_UpgradeNoteIn",
        "UpgradeNoteOut": "_containeranalysis_219_UpgradeNoteOut",
        "VersionIn": "_containeranalysis_220_VersionIn",
        "VersionOut": "_containeranalysis_221_VersionOut",
        "GerritSourceContextIn": "_containeranalysis_222_GerritSourceContextIn",
        "GerritSourceContextOut": "_containeranalysis_223_GerritSourceContextOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn": "_containeranalysis_224_GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut": "_containeranalysis_225_GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut",
        "EnvelopeIn": "_containeranalysis_226_EnvelopeIn",
        "EnvelopeOut": "_containeranalysis_227_EnvelopeOut",
        "BatchCreateOccurrencesRequestIn": "_containeranalysis_228_BatchCreateOccurrencesRequestIn",
        "BatchCreateOccurrencesRequestOut": "_containeranalysis_229_BatchCreateOccurrencesRequestOut",
        "CloudRepoSourceContextIn": "_containeranalysis_230_CloudRepoSourceContextIn",
        "CloudRepoSourceContextOut": "_containeranalysis_231_CloudRepoSourceContextOut",
        "LicenseIn": "_containeranalysis_232_LicenseIn",
        "LicenseOut": "_containeranalysis_233_LicenseOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningIn": "_containeranalysis_234_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningOut": "_containeranalysis_235_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn": "_containeranalysis_236_GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut": "_containeranalysis_237_GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut",
        "SlsaProvenanceIn": "_containeranalysis_238_SlsaProvenanceIn",
        "SlsaProvenanceOut": "_containeranalysis_239_SlsaProvenanceOut",
        "ListNotesResponseIn": "_containeranalysis_240_ListNotesResponseIn",
        "ListNotesResponseOut": "_containeranalysis_241_ListNotesResponseOut",
        "SlsaCompletenessIn": "_containeranalysis_242_SlsaCompletenessIn",
        "SlsaCompletenessOut": "_containeranalysis_243_SlsaCompletenessOut",
        "DSSEAttestationOccurrenceIn": "_containeranalysis_244_DSSEAttestationOccurrenceIn",
        "DSSEAttestationOccurrenceOut": "_containeranalysis_245_DSSEAttestationOccurrenceOut",
        "OccurrenceIn": "_containeranalysis_246_OccurrenceIn",
        "OccurrenceOut": "_containeranalysis_247_OccurrenceOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn": "_containeranalysis_248_ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut": "_containeranalysis_249_ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut",
        "ArtifactIn": "_containeranalysis_250_ArtifactIn",
        "ArtifactOut": "_containeranalysis_251_ArtifactOut",
        "WindowsUpdateIn": "_containeranalysis_252_WindowsUpdateIn",
        "WindowsUpdateOut": "_containeranalysis_253_WindowsUpdateOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceIn": "_containeranalysis_254_ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut": "_containeranalysis_255_ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanIn": "_containeranalysis_256_ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut": "_containeranalysis_257_ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut",
        "IdentityIn": "_containeranalysis_258_IdentityIn",
        "IdentityOut": "_containeranalysis_259_IdentityOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageIn": "_containeranalysis_260_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageOut": "_containeranalysis_261_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageOut",
        "BuilderConfigIn": "_containeranalysis_262_BuilderConfigIn",
        "BuilderConfigOut": "_containeranalysis_263_BuilderConfigOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretIn": "_containeranalysis_264_ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretOut": "_containeranalysis_265_ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretOut",
        "SlsaMetadataIn": "_containeranalysis_266_SlsaMetadataIn",
        "SlsaMetadataOut": "_containeranalysis_267_SlsaMetadataOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactIn": "_containeranalysis_268_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactOut": "_containeranalysis_269_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactOut",
        "DiscoveryNoteIn": "_containeranalysis_270_DiscoveryNoteIn",
        "DiscoveryNoteOut": "_containeranalysis_271_DiscoveryNoteOut",
        "InTotoStatementIn": "_containeranalysis_272_InTotoStatementIn",
        "InTotoStatementOut": "_containeranalysis_273_InTotoStatementOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalIn": "_containeranalysis_274_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalOut": "_containeranalysis_275_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalOut",
        "SignatureIn": "_containeranalysis_276_SignatureIn",
        "SignatureOut": "_containeranalysis_277_SignatureOut",
        "ImageNoteIn": "_containeranalysis_278_ImageNoteIn",
        "ImageNoteOut": "_containeranalysis_279_ImageNoteOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesIn": "_containeranalysis_280_ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesOut": "_containeranalysis_281_ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageIn": "_containeranalysis_282_ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageOut": "_containeranalysis_283_ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageOut",
        "AttestationOccurrenceIn": "_containeranalysis_284_AttestationOccurrenceIn",
        "AttestationOccurrenceOut": "_containeranalysis_285_AttestationOccurrenceOut",
        "EnvelopeSignatureIn": "_containeranalysis_286_EnvelopeSignatureIn",
        "EnvelopeSignatureOut": "_containeranalysis_287_EnvelopeSignatureOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoIn": "_containeranalysis_288_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoOut": "_containeranalysis_289_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoOut",
        "ListOccurrencesResponseIn": "_containeranalysis_290_ListOccurrencesResponseIn",
        "ListOccurrencesResponseOut": "_containeranalysis_291_ListOccurrencesResponseOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn": "_containeranalysis_292_ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut": "_containeranalysis_293_ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut",
        "LayerIn": "_containeranalysis_294_LayerIn",
        "LayerOut": "_containeranalysis_295_LayerOut",
        "CompletenessIn": "_containeranalysis_296_CompletenessIn",
        "CompletenessOut": "_containeranalysis_297_CompletenessOut",
        "NoteIn": "_containeranalysis_298_NoteIn",
        "NoteOut": "_containeranalysis_299_NoteOut",
        "PublisherIn": "_containeranalysis_300_PublisherIn",
        "PublisherOut": "_containeranalysis_301_PublisherOut",
        "ListNoteOccurrencesResponseIn": "_containeranalysis_302_ListNoteOccurrencesResponseIn",
        "ListNoteOccurrencesResponseOut": "_containeranalysis_303_ListNoteOccurrencesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsIn"] = t.struct(
        {
            "artifactManifest": t.string().optional(),
            "artifactTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanIn"]
            ).optional(),
            "buildStepImages": t.array(t.string()).optional(),
            "npmPackages": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageIn"
                    ]
                )
            ).optional(),
            "mavenArtifacts": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactIn"
                    ]
                )
            ).optional(),
            "buildStepOutputs": t.array(t.string()).optional(),
            "images": t.array(
                t.proxy(
                    renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageIn"]
                )
            ).optional(),
            "pythonPackages": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageIn"
                    ]
                )
            ).optional(),
            "numArtifacts": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut"] = t.struct(
        {
            "artifactManifest": t.string().optional(),
            "artifactTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "buildStepImages": t.array(t.string()).optional(),
            "npmPackages": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageOut"
                    ]
                )
            ).optional(),
            "mavenArtifacts": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactOut"
                    ]
                )
            ).optional(),
            "buildStepOutputs": t.array(t.string()).optional(),
            "images": t.array(
                t.proxy(
                    renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageOut"]
                )
            ).optional(),
            "pythonPackages": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageOut"
                    ]
                )
            ).optional(),
            "numArtifacts": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut"])
    types["AnalysisCompletedIn"] = t.struct(
        {"analysisType": t.array(t.string())}
    ).named(renames["AnalysisCompletedIn"])
    types["AnalysisCompletedOut"] = t.struct(
        {
            "analysisType": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalysisCompletedOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1HashIn"] = t.struct(
        {"value": t.string().optional(), "type": t.string().optional()}
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1HashIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1HashOut"] = t.struct(
        {
            "value": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1HashOut"])
    types["BuildProvenanceIn"] = t.struct(
        {
            "creator": t.string().optional(),
            "sourceProvenance": t.proxy(renames["SourceIn"]).optional(),
            "triggerId": t.string().optional(),
            "endTime": t.string().optional(),
            "buildOptions": t.struct({"_": t.string().optional()}).optional(),
            "startTime": t.string().optional(),
            "projectId": t.string().optional(),
            "logsUri": t.string().optional(),
            "builtArtifacts": t.array(t.proxy(renames["ArtifactIn"])).optional(),
            "id": t.string(),
            "createTime": t.string().optional(),
            "commands": t.array(t.proxy(renames["CommandIn"])).optional(),
            "builderVersion": t.string().optional(),
        }
    ).named(renames["BuildProvenanceIn"])
    types["BuildProvenanceOut"] = t.struct(
        {
            "creator": t.string().optional(),
            "sourceProvenance": t.proxy(renames["SourceOut"]).optional(),
            "triggerId": t.string().optional(),
            "endTime": t.string().optional(),
            "buildOptions": t.struct({"_": t.string().optional()}).optional(),
            "startTime": t.string().optional(),
            "projectId": t.string().optional(),
            "logsUri": t.string().optional(),
            "builtArtifacts": t.array(t.proxy(renames["ArtifactOut"])).optional(),
            "id": t.string(),
            "createTime": t.string().optional(),
            "commands": t.array(t.proxy(renames["CommandOut"])).optional(),
            "builderVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildProvenanceOut"])
    types["SbomReferenceIntotoPayloadIn"] = t.struct(
        {
            "predicateType": t.string().optional(),
            "_type": t.string().optional(),
            "subject": t.array(t.proxy(renames["SubjectIn"])).optional(),
            "predicate": t.proxy(renames["SbomReferenceIntotoPredicateIn"]).optional(),
        }
    ).named(renames["SbomReferenceIntotoPayloadIn"])
    types["SbomReferenceIntotoPayloadOut"] = t.struct(
        {
            "predicateType": t.string().optional(),
            "_type": t.string().optional(),
            "subject": t.array(t.proxy(renames["SubjectOut"])).optional(),
            "predicate": t.proxy(renames["SbomReferenceIntotoPredicateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SbomReferenceIntotoPayloadOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigIn"] = t.struct(
        {"approvalRequired": t.boolean().optional()}
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigOut"] = t.struct(
        {
            "approvalRequired": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigOut"])
    types["SourceIn"] = t.struct(
        {
            "artifactStorageSourceUri": t.string().optional(),
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "context": t.proxy(renames["SourceContextIn"]).optional(),
            "additionalContexts": t.array(
                t.proxy(renames["SourceContextIn"])
            ).optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "artifactStorageSourceUri": t.string().optional(),
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "context": t.proxy(renames["SourceContextOut"]).optional(),
            "additionalContexts": t.array(
                t.proxy(renames["SourceContextOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}),
            "configSource": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn"]
            ),
            "environment": t.struct({"_": t.string().optional()}),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}),
            "configSource": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut"]
            ),
            "environment": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut"])
    types["DistributionIn"] = t.struct(
        {
            "cpeUri": t.string(),
            "maintainer": t.string().optional(),
            "architecture": t.string().optional(),
            "url": t.string().optional(),
            "description": t.string().optional(),
            "latestVersion": t.proxy(renames["VersionIn"]).optional(),
        }
    ).named(renames["DistributionIn"])
    types["DistributionOut"] = t.struct(
        {
            "cpeUri": t.string(),
            "maintainer": t.string().optional(),
            "architecture": t.string().optional(),
            "url": t.string().optional(),
            "description": t.string().optional(),
            "latestVersion": t.proxy(renames["VersionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DistributionOut"])
    types["ComplianceNoteIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "remediation": t.string().optional(),
            "cisBenchmark": t.proxy(renames["CisBenchmarkIn"]),
            "version": t.array(t.proxy(renames["ComplianceVersionIn"])).optional(),
            "rationale": t.string().optional(),
            "scanInstructions": t.string().optional(),
        }
    ).named(renames["ComplianceNoteIn"])
    types["ComplianceNoteOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "remediation": t.string().optional(),
            "cisBenchmark": t.proxy(renames["CisBenchmarkOut"]),
            "version": t.array(t.proxy(renames["ComplianceVersionOut"])).optional(),
            "rationale": t.string().optional(),
            "scanInstructions": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComplianceNoteOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildIn"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "artifacts": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsIn"]
            ).optional(),
            "source": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceIn"]
            ).optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "logsBucket": t.string().optional(),
            "images": t.array(t.string()).optional(),
            "timeout": t.string().optional(),
            "availableSecrets": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsIn"]
            ).optional(),
            "options": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn"]
            ).optional(),
            "steps": t.array(
                t.proxy(
                    renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn"]
                )
            ),
            "queueTtl": t.string().optional(),
            "secrets": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretIn"])
            ).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOut"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "timing": t.struct({"_": t.string().optional()}).optional(),
            "tags": t.array(t.string()).optional(),
            "artifacts": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOut"]
            ).optional(),
            "source": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceOut"]
            ).optional(),
            "status": t.string().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "logsBucket": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "warnings": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningOut"
                    ]
                )
            ).optional(),
            "images": t.array(t.string()).optional(),
            "finishTime": t.string().optional(),
            "timeout": t.string().optional(),
            "buildTriggerId": t.string().optional(),
            "statusDetail": t.string().optional(),
            "approval": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalOut"]
            ).optional(),
            "availableSecrets": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsOut"]
            ).optional(),
            "logUrl": t.string().optional(),
            "options": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut"]
            ).optional(),
            "steps": t.array(
                t.proxy(
                    renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut"]
                )
            ),
            "queueTtl": t.string().optional(),
            "createTime": t.string().optional(),
            "secrets": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretOut"])
            ).optional(),
            "projectId": t.string().optional(),
            "failureInfo": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoOut"
                ]
            ).optional(),
            "sourceProvenance": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut"
                ]
            ).optional(),
            "startTime": t.string().optional(),
            "results": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["SlsaBuilderIn"] = t.struct({"id": t.string()}).named(
        renames["SlsaBuilderIn"]
    )
    types["SlsaBuilderOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SlsaBuilderOut"])
    types["CommandIn"] = t.struct(
        {
            "name": t.string(),
            "env": t.array(t.string()).optional(),
            "dir": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "waitFor": t.array(t.string()).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["CommandIn"])
    types["CommandOut"] = t.struct(
        {
            "name": t.string(),
            "env": t.array(t.string()).optional(),
            "dir": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "waitFor": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommandOut"])
    types["MetadataIn"] = t.struct(
        {
            "completeness": t.proxy(renames["CompletenessIn"]).optional(),
            "buildFinishedOn": t.string().optional(),
            "buildStartedOn": t.string().optional(),
            "buildInvocationId": t.string().optional(),
            "reproducible": t.boolean().optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "completeness": t.proxy(renames["CompletenessOut"]).optional(),
            "buildFinishedOn": t.string().optional(),
            "buildStartedOn": t.string().optional(),
            "buildInvocationId": t.string().optional(),
            "reproducible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"] = t.struct(
        {
            "environment": t.boolean(),
            "parameters": t.boolean(),
            "materials": t.boolean(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"] = t.struct(
        {
            "environment": t.boolean(),
            "parameters": t.boolean(),
            "materials": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"])
    types["BuildOccurrenceIn"] = t.struct(
        {
            "intotoStatement": t.proxy(renames["InTotoStatementIn"]).optional(),
            "provenanceBytes": t.string().optional(),
            "provenance": t.proxy(renames["BuildProvenanceIn"]).optional(),
            "intotoProvenance": t.proxy(renames["InTotoProvenanceIn"]).optional(),
        }
    ).named(renames["BuildOccurrenceIn"])
    types["BuildOccurrenceOut"] = t.struct(
        {
            "intotoStatement": t.proxy(renames["InTotoStatementOut"]).optional(),
            "provenanceBytes": t.string().optional(),
            "provenance": t.proxy(renames["BuildProvenanceOut"]).optional(),
            "intotoProvenance": t.proxy(renames["InTotoProvenanceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOccurrenceOut"])
    types["VulnerabilityNoteIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "cvssVersion": t.string().optional(),
            "windowsDetails": t.array(t.proxy(renames["WindowsDetailIn"])).optional(),
            "cvssV2": t.proxy(renames["CVSSIn"]).optional(),
            "cvssV3": t.proxy(renames["CVSSv3In"]).optional(),
            "sourceUpdateTime": t.string().optional(),
            "cvssScore": t.number().optional(),
            "details": t.array(t.proxy(renames["DetailIn"])).optional(),
        }
    ).named(renames["VulnerabilityNoteIn"])
    types["VulnerabilityNoteOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "cvssVersion": t.string().optional(),
            "windowsDetails": t.array(t.proxy(renames["WindowsDetailOut"])).optional(),
            "cvssV2": t.proxy(renames["CVSSOut"]).optional(),
            "cvssV3": t.proxy(renames["CVSSv3Out"]).optional(),
            "sourceUpdateTime": t.string().optional(),
            "cvssScore": t.number().optional(),
            "details": t.array(t.proxy(renames["DetailOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityNoteOut"])
    types["AttestationNoteIn"] = t.struct(
        {"hint": t.proxy(renames["HintIn"]).optional()}
    ).named(renames["AttestationNoteIn"])
    types["AttestationNoteOut"] = t.struct(
        {
            "hint": t.proxy(renames["HintOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestationNoteOut"])
    types["SbomReferenceIntotoPredicateIn"] = t.struct(
        {
            "location": t.string().optional(),
            "referrerId": t.string().optional(),
            "digest": t.struct({"_": t.string().optional()}).optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["SbomReferenceIntotoPredicateIn"])
    types["SbomReferenceIntotoPredicateOut"] = t.struct(
        {
            "location": t.string().optional(),
            "referrerId": t.string().optional(),
            "digest": t.struct({"_": t.string().optional()}).optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SbomReferenceIntotoPredicateOut"])
    types["InTotoProvenanceIn"] = t.struct(
        {
            "metadata": t.proxy(renames["MetadataIn"]),
            "recipe": t.proxy(renames["RecipeIn"]).optional(),
            "materials": t.array(t.string()).optional(),
            "builderConfig": t.proxy(renames["BuilderConfigIn"]).optional(),
        }
    ).named(renames["InTotoProvenanceIn"])
    types["InTotoProvenanceOut"] = t.struct(
        {
            "metadata": t.proxy(renames["MetadataOut"]),
            "recipe": t.proxy(renames["RecipeOut"]).optional(),
            "materials": t.array(t.string()).optional(),
            "builderConfig": t.proxy(renames["BuilderConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InTotoProvenanceOut"])
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
    types["DiscoveryOccurrenceIn"] = t.struct(
        {
            "analysisError": t.array(t.proxy(renames["StatusIn"])).optional(),
            "analysisStatus": t.string().optional(),
            "analysisCompleted": t.proxy(renames["AnalysisCompletedIn"]),
            "analysisStatusError": t.proxy(renames["StatusIn"]).optional(),
            "lastScanTime": t.string().optional(),
            "continuousAnalysis": t.string().optional(),
            "cpe": t.string().optional(),
        }
    ).named(renames["DiscoveryOccurrenceIn"])
    types["DiscoveryOccurrenceOut"] = t.struct(
        {
            "analysisError": t.array(t.proxy(renames["StatusOut"])).optional(),
            "analysisStatus": t.string().optional(),
            "analysisCompleted": t.proxy(renames["AnalysisCompletedOut"]),
            "archiveTime": t.string().optional(),
            "analysisStatusError": t.proxy(renames["StatusOut"]).optional(),
            "lastScanTime": t.string().optional(),
            "continuousAnalysis": t.string().optional(),
            "cpe": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoveryOccurrenceOut"])
    types["HintIn"] = t.struct({"humanReadableName": t.string()}).named(
        renames["HintIn"]
    )
    types["HintOut"] = t.struct(
        {
            "humanReadableName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HintOut"])
    types["BuildNoteIn"] = t.struct({"builderVersion": t.string()}).named(
        renames["BuildNoteIn"]
    )
    types["BuildNoteOut"] = t.struct(
        {
            "builderVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildNoteOut"])
    types["BatchCreateNotesResponseIn"] = t.struct(
        {"notes": t.array(t.proxy(renames["NoteIn"])).optional()}
    ).named(renames["BatchCreateNotesResponseIn"])
    types["BatchCreateNotesResponseOut"] = t.struct(
        {
            "notes": t.array(t.proxy(renames["NoteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateNotesResponseOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultIn"] = t.struct(
        {
            "comment": t.string().optional(),
            "url": t.string().optional(),
            "decision": t.string(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultOut"] = t.struct(
        {
            "comment": t.string().optional(),
            "url": t.string().optional(),
            "decision": t.string(),
            "approverAccount": t.string().optional(),
            "approvalTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultOut"])
    types["AliasContextIn"] = t.struct(
        {"name": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["AliasContextIn"])
    types["AliasContextOut"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AliasContextOut"])
    types["AssessmentIn"] = t.struct(
        {
            "state": t.string().optional(),
            "remediations": t.array(t.proxy(renames["RemediationIn"])).optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "longDescription": t.string().optional(),
            "justification": t.proxy(renames["JustificationIn"]).optional(),
            "shortDescription": t.string().optional(),
            "cve": t.string().optional(),
            "impacts": t.array(t.string()).optional(),
        }
    ).named(renames["AssessmentIn"])
    types["AssessmentOut"] = t.struct(
        {
            "state": t.string().optional(),
            "remediations": t.array(t.proxy(renames["RemediationOut"])).optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "longDescription": t.string().optional(),
            "justification": t.proxy(renames["JustificationOut"]).optional(),
            "shortDescription": t.string().optional(),
            "cve": t.string().optional(),
            "impacts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssessmentOut"])
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
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageIn"
    ] = t.struct(
        {"paths": t.array(t.string()).optional(), "repository": t.string().optional()}
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageOut"
    ] = t.struct(
        {
            "paths": t.array(t.string()).optional(),
            "repository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageOut"]
    )
    types["CVSSv3In"] = t.struct(
        {
            "attackComplexity": t.string(),
            "impactScore": t.number(),
            "baseScore": t.number().optional(),
            "confidentialityImpact": t.string(),
            "attackVector": t.string().optional(),
            "exploitabilityScore": t.number(),
            "privilegesRequired": t.string(),
            "availabilityImpact": t.string(),
            "userInteraction": t.string(),
            "integrityImpact": t.string(),
            "scope": t.string(),
        }
    ).named(renames["CVSSv3In"])
    types["CVSSv3Out"] = t.struct(
        {
            "attackComplexity": t.string(),
            "impactScore": t.number(),
            "baseScore": t.number().optional(),
            "confidentialityImpact": t.string(),
            "attackVector": t.string().optional(),
            "exploitabilityScore": t.number(),
            "privilegesRequired": t.string(),
            "availabilityImpact": t.string(),
            "userInteraction": t.string(),
            "integrityImpact": t.string(),
            "scope": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CVSSv3Out"])
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsIn"
    ] = t.struct(
        {"location": t.string().optional(), "paths": t.array(t.string()).optional()}
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsOut"
    ] = t.struct(
        {
            "location": t.string().optional(),
            "timing": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "paths": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsOut"
        ]
    )
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
    types["VolumeIn"] = t.struct(
        {"path": t.string().optional(), "name": t.string().optional()}
    ).named(renames["VolumeIn"])
    types["VolumeOut"] = t.struct(
        {
            "path": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceIn"] = t.struct(
        {
            "storageSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn"]
            ).optional(),
            "storageSourceManifest": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn"
                ]
            ).optional(),
            "repoSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn"]
            ).optional(),
            "gitSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceIn"]
            ).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceOut"] = t.struct(
        {
            "storageSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut"]
            ).optional(),
            "storageSourceManifest": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut"
                ]
            ).optional(),
            "repoSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut"]
            ).optional(),
            "gitSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceOut"])
    types["SourceContextIn"] = t.struct(
        {
            "gerrit": t.proxy(renames["GerritSourceContextIn"]).optional(),
            "cloudRepo": t.proxy(renames["CloudRepoSourceContextIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "git": t.proxy(renames["GitSourceContextIn"]).optional(),
        }
    ).named(renames["SourceContextIn"])
    types["SourceContextOut"] = t.struct(
        {
            "gerrit": t.proxy(renames["GerritSourceContextOut"]).optional(),
            "cloudRepo": t.proxy(renames["CloudRepoSourceContextOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "git": t.proxy(renames["GitSourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["ImageOccurrenceIn"] = t.struct(
        {
            "baseResourceUrl": t.string().optional(),
            "distance": t.integer().optional(),
            "fingerprint": t.proxy(renames["FingerprintIn"]),
            "layerInfo": t.array(t.proxy(renames["LayerIn"])).optional(),
        }
    ).named(renames["ImageOccurrenceIn"])
    types["ImageOccurrenceOut"] = t.struct(
        {
            "baseResourceUrl": t.string().optional(),
            "distance": t.integer().optional(),
            "fingerprint": t.proxy(renames["FingerprintOut"]),
            "layerInfo": t.array(t.proxy(renames["LayerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOccurrenceOut"])
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
    types["FixableTotalByDigestIn"] = t.struct(
        {
            "resourceUri": t.string().optional(),
            "totalCount": t.string().optional(),
            "fixableCount": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["FixableTotalByDigestIn"])
    types["FixableTotalByDigestOut"] = t.struct(
        {
            "resourceUri": t.string().optional(),
            "totalCount": t.string().optional(),
            "fixableCount": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FixableTotalByDigestOut"])
    types["ProductIn"] = t.struct(
        {
            "name": t.string().optional(),
            "genericUri": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["ProductIn"])
    types["ProductOut"] = t.struct(
        {
            "name": t.string().optional(),
            "genericUri": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductOut"])
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
    types["TimeSpanIn"] = t.struct(
        {"startTime": t.string().optional(), "endTime": t.string().optional()}
    ).named(renames["TimeSpanIn"])
    types["TimeSpanOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeSpanOut"])
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn"
    ] = t.struct(
        {
            "object": t.string().optional(),
            "generation": t.string().optional(),
            "bucket": t.string().optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut"
    ] = t.struct(
        {
            "object": t.string().optional(),
            "generation": t.string().optional(),
            "bucket": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut"]
    )
    types["DeploymentNoteIn"] = t.struct({"resourceUri": t.array(t.string())}).named(
        renames["DeploymentNoteIn"]
    )
    types["DeploymentNoteOut"] = t.struct(
        {
            "resourceUri": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentNoteOut"])
    types["BatchCreateNotesRequestIn"] = t.struct(
        {"notes": t.struct({"_": t.string().optional()})}
    ).named(renames["BatchCreateNotesRequestIn"])
    types["BatchCreateNotesRequestOut"] = t.struct(
        {
            "notes": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateNotesRequestOut"])
    types["DSSEHintIn"] = t.struct({"humanReadableName": t.string()}).named(
        renames["DSSEHintIn"]
    )
    types["DSSEHintOut"] = t.struct(
        {
            "humanReadableName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DSSEHintOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceIn"] = t.struct(
        {
            "resolvedRepoSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn"]
            ).optional(),
            "resolvedStorageSourceManifest": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn"
                ]
            ).optional(),
            "resolvedStorageSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn"]
            ).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut"] = t.struct(
        {
            "resolvedRepoSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut"]
            ).optional(),
            "resolvedStorageSourceManifest": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut"
                ]
            ).optional(),
            "resolvedStorageSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut"]
            ).optional(),
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut"])
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageIn"
    ] = t.struct(
        {
            "uri": t.string().optional(),
            "fileHashes": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesIn"]
            ).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageOut"
    ] = t.struct(
        {
            "uri": t.string().optional(),
            "pushTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "fileHashes": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageOut"]
    )
    types["UpgradeOccurrenceIn"] = t.struct(
        {
            "package": t.string(),
            "distribution": t.proxy(renames["UpgradeDistributionIn"]).optional(),
            "parsedVersion": t.proxy(renames["VersionIn"]),
            "windowsUpdate": t.proxy(renames["WindowsUpdateIn"]),
        }
    ).named(renames["UpgradeOccurrenceIn"])
    types["UpgradeOccurrenceOut"] = t.struct(
        {
            "package": t.string(),
            "distribution": t.proxy(renames["UpgradeDistributionOut"]).optional(),
            "parsedVersion": t.proxy(renames["VersionOut"]),
            "windowsUpdate": t.proxy(renames["WindowsUpdateOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeOccurrenceOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactIn"
    ] = t.struct(
        {
            "repository": t.string().optional(),
            "path": t.string().optional(),
            "version": t.string().optional(),
            "artifactId": t.string().optional(),
            "groupId": t.string().optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactOut"
    ] = t.struct(
        {
            "repository": t.string().optional(),
            "path": t.string().optional(),
            "version": t.string().optional(),
            "artifactId": t.string().optional(),
            "groupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactOut"]
    )
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsIn"] = t.struct(
        {
            "mavenArtifacts": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactIn"
                    ]
                )
            ).optional(),
            "images": t.array(t.string()).optional(),
            "objects": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsIn"
                ]
            ).optional(),
            "pythonPackages": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageIn"
                    ]
                )
            ).optional(),
            "npmPackages": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOut"] = t.struct(
        {
            "mavenArtifacts": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactOut"
                    ]
                )
            ).optional(),
            "images": t.array(t.string()).optional(),
            "objects": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsOut"
                ]
            ).optional(),
            "pythonPackages": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageOut"
                    ]
                )
            ).optional(),
            "npmPackages": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOut"])
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
    types["GrafeasV1FileLocationIn"] = t.struct(
        {"filePath": t.string().optional()}
    ).named(renames["GrafeasV1FileLocationIn"])
    types["GrafeasV1FileLocationOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1FileLocationOut"])
    types["VulnerabilityOccurrencesSummaryIn"] = t.struct(
        {"counts": t.array(t.proxy(renames["FixableTotalByDigestIn"])).optional()}
    ).named(renames["VulnerabilityOccurrencesSummaryIn"])
    types["VulnerabilityOccurrencesSummaryOut"] = t.struct(
        {
            "counts": t.array(t.proxy(renames["FixableTotalByDigestOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityOccurrencesSummaryOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["SlsaProvenanceZeroTwoIn"] = t.struct(
        {
            "buildType": t.string(),
            "metadata": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"]
            ),
            "invocation": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn"]
            ),
            "buildConfig": t.struct({"_": t.string().optional()}),
            "builder": t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"]),
            "materials": t.array(
                t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn"])
            ),
        }
    ).named(renames["SlsaProvenanceZeroTwoIn"])
    types["SlsaProvenanceZeroTwoOut"] = t.struct(
        {
            "buildType": t.string(),
            "metadata": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"]
            ),
            "invocation": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut"]
            ),
            "buildConfig": t.struct({"_": t.string().optional()}),
            "builder": t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"]),
            "materials": t.array(
                t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaProvenanceZeroTwoOut"])
    types["VexAssessmentIn"] = t.struct(
        {
            "justification": t.proxy(renames["JustificationIn"]).optional(),
            "remediations": t.array(t.proxy(renames["RemediationIn"])).optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "noteName": t.string().optional(),
            "impacts": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "cve": t.string().optional(),
        }
    ).named(renames["VexAssessmentIn"])
    types["VexAssessmentOut"] = t.struct(
        {
            "justification": t.proxy(renames["JustificationOut"]).optional(),
            "remediations": t.array(t.proxy(renames["RemediationOut"])).optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "noteName": t.string().optional(),
            "impacts": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "cve": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VexAssessmentOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsIn"] = t.struct(
        {
            "inline": t.array(
                t.proxy(
                    renames["ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretIn"]
                )
            ).optional(),
            "secretManager": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsOut"] = t.struct(
        {
            "inline": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretOut"
                    ]
                )
            ).optional(),
            "secretManager": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsOut"])
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionIn"
    ] = t.struct({"name": t.string().optional()}).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionOut"
    ] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionOut"]
    )
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn"] = t.struct(
        {
            "dir": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "name": t.string(),
            "allowFailure": t.boolean().optional(),
            "id": t.string().optional(),
            "secretEnv": t.array(t.string()).optional(),
            "script": t.string().optional(),
            "volumes": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn"])
            ).optional(),
            "allowExitCodes": t.array(t.integer()).optional(),
            "env": t.array(t.string()).optional(),
            "timeout": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "entrypoint": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut"] = t.struct(
        {
            "dir": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "name": t.string(),
            "timing": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "allowFailure": t.boolean().optional(),
            "id": t.string().optional(),
            "pullTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "secretEnv": t.array(t.string()).optional(),
            "script": t.string().optional(),
            "volumes": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut"])
            ).optional(),
            "exitCode": t.integer().optional(),
            "allowExitCodes": t.array(t.integer()).optional(),
            "env": t.array(t.string()).optional(),
            "timeout": t.string().optional(),
            "status": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "entrypoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut"])
    types["JwtIn"] = t.struct({"compactJwt": t.string().optional()}).named(
        renames["JwtIn"]
    )
    types["JwtOut"] = t.struct(
        {
            "compactJwt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtOut"])
    types["VulnerabilityOccurrenceIn"] = t.struct(
        {
            "effectiveSeverity": t.string().optional(),
            "type": t.string().optional(),
            "cvssv3": t.proxy(renames["CVSSIn"]).optional(),
            "relatedUrls": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "cvssVersion": t.string().optional(),
            "shortDescription": t.string().optional(),
            "cvssScore": t.number().optional(),
            "longDescription": t.string().optional(),
            "severity": t.string().optional(),
            "cvssV2": t.proxy(renames["CVSSIn"]).optional(),
            "vexAssessment": t.proxy(renames["VexAssessmentIn"]),
            "fixAvailable": t.boolean().optional(),
            "packageIssue": t.array(t.proxy(renames["PackageIssueIn"])),
        }
    ).named(renames["VulnerabilityOccurrenceIn"])
    types["VulnerabilityOccurrenceOut"] = t.struct(
        {
            "effectiveSeverity": t.string().optional(),
            "type": t.string().optional(),
            "cvssv3": t.proxy(renames["CVSSOut"]).optional(),
            "relatedUrls": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "cvssVersion": t.string().optional(),
            "shortDescription": t.string().optional(),
            "cvssScore": t.number().optional(),
            "longDescription": t.string().optional(),
            "severity": t.string().optional(),
            "cvssV2": t.proxy(renames["CVSSOut"]).optional(),
            "vexAssessment": t.proxy(renames["VexAssessmentOut"]),
            "fixAvailable": t.boolean().optional(),
            "packageIssue": t.array(t.proxy(renames["PackageIssueOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityOccurrenceOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageIn"] = t.struct(
        {
            "fileHashes": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesIn"]
            ).optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageIn"])
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageOut"
    ] = t.struct(
        {
            "fileHashes": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesOut"]
            ).optional(),
            "pushTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageOut"]
    )
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["CisBenchmarkIn"] = t.struct(
        {"severity": t.string(), "profileLevel": t.integer()}
    ).named(renames["CisBenchmarkIn"])
    types["CisBenchmarkOut"] = t.struct(
        {
            "severity": t.string(),
            "profileLevel": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CisBenchmarkOut"])
    types["BuildStepIn"] = t.struct(
        {
            "name": t.string(),
            "allowExitCodes": t.array(t.integer()).optional(),
            "timing": t.proxy(renames["TimeSpanIn"]).optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "timeout": t.string().optional(),
            "allowFailure": t.boolean().optional(),
            "exitCode": t.integer().optional(),
            "waitFor": t.array(t.string()).optional(),
            "pullTiming": t.proxy(renames["TimeSpanIn"]).optional(),
            "dir": t.string().optional(),
            "script": t.string().optional(),
            "entrypoint": t.string().optional(),
            "secretEnv": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "status": t.string().optional(),
        }
    ).named(renames["BuildStepIn"])
    types["BuildStepOut"] = t.struct(
        {
            "name": t.string(),
            "allowExitCodes": t.array(t.integer()).optional(),
            "timing": t.proxy(renames["TimeSpanOut"]).optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "timeout": t.string().optional(),
            "allowFailure": t.boolean().optional(),
            "exitCode": t.integer().optional(),
            "waitFor": t.array(t.string()).optional(),
            "pullTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "dir": t.string().optional(),
            "script": t.string().optional(),
            "entrypoint": t.string().optional(),
            "secretEnv": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildStepOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn"] = t.struct(
        {
            "generation": t.string().optional(),
            "bucket": t.string().optional(),
            "object": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut"] = t.struct(
        {
            "generation": t.string().optional(),
            "bucket": t.string().optional(),
            "object": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut"])
    types["ComplianceVersionIn"] = t.struct(
        {
            "cpeUri": t.string().optional(),
            "version": t.string().optional(),
            "benchmarkDocument": t.string().optional(),
        }
    ).named(renames["ComplianceVersionIn"])
    types["ComplianceVersionOut"] = t.struct(
        {
            "cpeUri": t.string().optional(),
            "version": t.string().optional(),
            "benchmarkDocument": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComplianceVersionOut"])
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
    types["BatchCreateOccurrencesResponseIn"] = t.struct(
        {"occurrences": t.array(t.proxy(renames["OccurrenceIn"])).optional()}
    ).named(renames["BatchCreateOccurrencesResponseIn"])
    types["BatchCreateOccurrencesResponseOut"] = t.struct(
        {
            "occurrences": t.array(t.proxy(renames["OccurrenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateOccurrencesResponseOut"])
    types["GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataIn"] = t.struct(
        {"createTime": t.string().optional(), "endTime": t.string().optional()}
    ).named(renames["GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataIn"])
    types["GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataOut"])
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretIn"
    ] = t.struct(
        {"env": t.string().optional(), "versionName": t.string().optional()}
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretOut"
    ] = t.struct(
        {
            "env": t.string().optional(),
            "versionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretOut"]
    )
    types["PackageNoteIn"] = t.struct(
        {
            "license": t.proxy(renames["LicenseIn"]).optional(),
            "maintainer": t.string().optional(),
            "digest": t.array(t.proxy(renames["DigestIn"])).optional(),
            "version": t.proxy(renames["VersionIn"]).optional(),
            "url": t.string().optional(),
            "cpeUri": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "distribution": t.array(t.proxy(renames["DistributionIn"])).optional(),
            "architecture": t.string().optional(),
            "packageType": t.string().optional(),
        }
    ).named(renames["PackageNoteIn"])
    types["PackageNoteOut"] = t.struct(
        {
            "license": t.proxy(renames["LicenseOut"]).optional(),
            "maintainer": t.string().optional(),
            "digest": t.array(t.proxy(renames["DigestOut"])).optional(),
            "version": t.proxy(renames["VersionOut"]).optional(),
            "url": t.string().optional(),
            "cpeUri": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "distribution": t.array(t.proxy(renames["DistributionOut"])).optional(),
            "architecture": t.string().optional(),
            "packageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageNoteOut"])
    types["RecipeIn"] = t.struct(
        {
            "entryPoint": t.string().optional(),
            "definedInMaterial": t.string().optional(),
            "environment": t.array(t.struct({"_": t.string().optional()})).optional(),
            "arguments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["RecipeIn"])
    types["RecipeOut"] = t.struct(
        {
            "entryPoint": t.string().optional(),
            "definedInMaterial": t.string().optional(),
            "environment": t.array(t.struct({"_": t.string().optional()})).optional(),
            "arguments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecipeOut"])
    types["SBOMReferenceNoteIn"] = t.struct(
        {"format": t.string().optional(), "version": t.string().optional()}
    ).named(renames["SBOMReferenceNoteIn"])
    types["SBOMReferenceNoteOut"] = t.struct(
        {
            "format": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SBOMReferenceNoteOut"])
    types["PackageOccurrenceIn"] = t.struct(
        {
            "license": t.proxy(renames["LicenseIn"]).optional(),
            "location": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["PackageOccurrenceIn"])
    types["PackageOccurrenceOut"] = t.struct(
        {
            "packageType": t.string().optional(),
            "version": t.proxy(renames["VersionOut"]).optional(),
            "name": t.string(),
            "cpeUri": t.string().optional(),
            "architecture": t.string().optional(),
            "license": t.proxy(renames["LicenseOut"]).optional(),
            "location": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageOccurrenceOut"])
    types["DetailIn"] = t.struct(
        {
            "description": t.string().optional(),
            "affectedVersionEnd": t.proxy(renames["VersionIn"]).optional(),
            "source": t.string().optional(),
            "fixedVersion": t.proxy(renames["VersionIn"]).optional(),
            "affectedVersionStart": t.proxy(renames["VersionIn"]).optional(),
            "severityName": t.string().optional(),
            "isObsolete": t.boolean().optional(),
            "affectedCpeUri": t.string(),
            "fixedPackage": t.string().optional(),
            "vendor": t.string().optional(),
            "fixedCpeUri": t.string().optional(),
            "sourceUpdateTime": t.string().optional(),
            "affectedPackage": t.string(),
            "packageType": t.string().optional(),
        }
    ).named(renames["DetailIn"])
    types["DetailOut"] = t.struct(
        {
            "description": t.string().optional(),
            "affectedVersionEnd": t.proxy(renames["VersionOut"]).optional(),
            "source": t.string().optional(),
            "fixedVersion": t.proxy(renames["VersionOut"]).optional(),
            "affectedVersionStart": t.proxy(renames["VersionOut"]).optional(),
            "severityName": t.string().optional(),
            "isObsolete": t.boolean().optional(),
            "affectedCpeUri": t.string(),
            "fixedPackage": t.string().optional(),
            "vendor": t.string().optional(),
            "fixedCpeUri": t.string().optional(),
            "sourceUpdateTime": t.string().optional(),
            "affectedPackage": t.string(),
            "packageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetailOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretIn"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "secretEnv": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "secretEnv": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretOut"])
    types["WindowsDetailIn"] = t.struct(
        {
            "fixingKbs": t.array(t.proxy(renames["KnowledgeBaseIn"])),
            "cpeUri": t.string(),
            "description": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["WindowsDetailIn"])
    types["WindowsDetailOut"] = t.struct(
        {
            "fixingKbs": t.array(t.proxy(renames["KnowledgeBaseOut"])),
            "cpeUri": t.string(),
            "description": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsDetailOut"])
    types["SlsaRecipeIn"] = t.struct(
        {
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "entryPoint": t.string().optional(),
            "arguments": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "definedInMaterial": t.string().optional(),
        }
    ).named(renames["SlsaRecipeIn"])
    types["SlsaRecipeOut"] = t.struct(
        {
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "entryPoint": t.string().optional(),
            "arguments": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "definedInMaterial": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaRecipeOut"])
    types["PackageIssueIn"] = t.struct(
        {
            "packageType": t.string().optional(),
            "fileLocation": t.array(
                t.proxy(renames["GrafeasV1FileLocationIn"])
            ).optional(),
            "fixAvailable": t.boolean().optional(),
            "affectedVersion": t.proxy(renames["VersionIn"]),
            "affectedCpeUri": t.string(),
            "affectedPackage": t.string(),
            "fixedVersion": t.proxy(renames["VersionIn"]),
            "fixedCpeUri": t.string().optional(),
            "fixedPackage": t.string().optional(),
        }
    ).named(renames["PackageIssueIn"])
    types["PackageIssueOut"] = t.struct(
        {
            "packageType": t.string().optional(),
            "fileLocation": t.array(
                t.proxy(renames["GrafeasV1FileLocationOut"])
            ).optional(),
            "fixAvailable": t.boolean().optional(),
            "affectedVersion": t.proxy(renames["VersionOut"]),
            "effectiveSeverity": t.string().optional(),
            "affectedCpeUri": t.string(),
            "affectedPackage": t.string(),
            "fixedVersion": t.proxy(renames["VersionOut"]),
            "fixedCpeUri": t.string().optional(),
            "fixedPackage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageIssueOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn"] = t.struct(
        {
            "diskSizeGb": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "substitutionOption": t.string().optional(),
            "logging": t.string().optional(),
            "requestedVerifyOption": t.string().optional(),
            "sourceProvenanceHash": t.array(t.string()).optional(),
            "machineType": t.string().optional(),
            "volumes": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn"])
            ).optional(),
            "secretEnv": t.array(t.string()).optional(),
            "defaultLogsBucketBehavior": t.string().optional(),
            "workerPool": t.string().optional(),
            "pool": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionIn"
                ]
            ).optional(),
            "dynamicSubstitutions": t.boolean().optional(),
            "logStreamingOption": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut"] = t.struct(
        {
            "diskSizeGb": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "substitutionOption": t.string().optional(),
            "logging": t.string().optional(),
            "requestedVerifyOption": t.string().optional(),
            "sourceProvenanceHash": t.array(t.string()).optional(),
            "machineType": t.string().optional(),
            "volumes": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut"])
            ).optional(),
            "secretEnv": t.array(t.string()).optional(),
            "defaultLogsBucketBehavior": t.string().optional(),
            "workerPool": t.string().optional(),
            "pool": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionOut"
                ]
            ).optional(),
            "dynamicSubstitutions": t.boolean().optional(),
            "logStreamingOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut"])
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
    types["FileHashesIn"] = t.struct(
        {"fileHash": t.array(t.proxy(renames["HashIn"]))}
    ).named(renames["FileHashesIn"])
    types["FileHashesOut"] = t.struct(
        {
            "fileHash": t.array(t.proxy(renames["HashOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileHashesOut"])
    types["VulnerabilityAssessmentNoteIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "publisher": t.proxy(renames["PublisherIn"]).optional(),
            "longDescription": t.string().optional(),
            "assessment": t.proxy(renames["AssessmentIn"]).optional(),
            "product": t.proxy(renames["ProductIn"]).optional(),
            "shortDescription": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["VulnerabilityAssessmentNoteIn"])
    types["VulnerabilityAssessmentNoteOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "publisher": t.proxy(renames["PublisherOut"]).optional(),
            "longDescription": t.string().optional(),
            "assessment": t.proxy(renames["AssessmentOut"]).optional(),
            "product": t.proxy(renames["ProductOut"]).optional(),
            "shortDescription": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityAssessmentNoteOut"])
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
    types["DigestIn"] = t.struct(
        {"digestBytes": t.string().optional(), "algo": t.string().optional()}
    ).named(renames["DigestIn"])
    types["DigestOut"] = t.struct(
        {
            "digestBytes": t.string().optional(),
            "algo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DigestOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["KnowledgeBaseIn"] = t.struct(
        {"name": t.string().optional(), "url": t.string().optional()}
    ).named(renames["KnowledgeBaseIn"])
    types["KnowledgeBaseOut"] = t.struct(
        {
            "name": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KnowledgeBaseOut"])
    types["JustificationIn"] = t.struct(
        {"justificationType": t.string().optional(), "details": t.string().optional()}
    ).named(renames["JustificationIn"])
    types["JustificationOut"] = t.struct(
        {
            "justificationType": t.string().optional(),
            "details": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JustificationOut"])
    types["CVSSIn"] = t.struct(
        {
            "privilegesRequired": t.string(),
            "attackVector": t.string().optional(),
            "attackComplexity": t.string(),
            "baseScore": t.number().optional(),
            "exploitabilityScore": t.number(),
            "authentication": t.string(),
            "availabilityImpact": t.string(),
            "confidentialityImpact": t.string(),
            "integrityImpact": t.string(),
            "impactScore": t.number(),
            "userInteraction": t.string(),
            "scope": t.string(),
        }
    ).named(renames["CVSSIn"])
    types["CVSSOut"] = t.struct(
        {
            "privilegesRequired": t.string(),
            "attackVector": t.string().optional(),
            "attackComplexity": t.string(),
            "baseScore": t.number().optional(),
            "exploitabilityScore": t.number(),
            "authentication": t.string(),
            "availabilityImpact": t.string(),
            "confidentialityImpact": t.string(),
            "integrityImpact": t.string(),
            "impactScore": t.number(),
            "userInteraction": t.string(),
            "scope": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CVSSOut"])
    types["DSSEAttestationNoteIn"] = t.struct(
        {"hint": t.proxy(renames["DSSEHintIn"]).optional()}
    ).named(renames["DSSEAttestationNoteIn"])
    types["DSSEAttestationNoteOut"] = t.struct(
        {
            "hint": t.proxy(renames["DSSEHintOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DSSEAttestationNoteOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["UpgradeNoteIn"] = t.struct(
        {
            "package": t.string(),
            "windowsUpdate": t.proxy(renames["WindowsUpdateIn"]),
            "version": t.proxy(renames["VersionIn"]),
            "distributions": t.array(
                t.proxy(renames["UpgradeDistributionIn"])
            ).optional(),
        }
    ).named(renames["UpgradeNoteIn"])
    types["UpgradeNoteOut"] = t.struct(
        {
            "package": t.string(),
            "windowsUpdate": t.proxy(renames["WindowsUpdateOut"]),
            "version": t.proxy(renames["VersionOut"]),
            "distributions": t.array(
                t.proxy(renames["UpgradeDistributionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeNoteOut"])
    types["VersionIn"] = t.struct(
        {
            "fullName": t.string().optional(),
            "kind": t.string(),
            "epoch": t.integer().optional(),
            "revision": t.string().optional(),
            "name": t.string(),
            "inclusive": t.boolean().optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "fullName": t.string().optional(),
            "kind": t.string(),
            "epoch": t.integer().optional(),
            "revision": t.string().optional(),
            "name": t.string(),
            "inclusive": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
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
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"] = t.struct(
        {
            "buildInvocationId": t.string(),
            "completeness": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"]
            ),
            "reproducible": t.boolean(),
            "buildStartedOn": t.string(),
            "buildFinishedOn": t.string(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"] = t.struct(
        {
            "buildInvocationId": t.string(),
            "completeness": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"]
            ),
            "reproducible": t.boolean(),
            "buildStartedOn": t.string(),
            "buildFinishedOn": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"])
    types["EnvelopeIn"] = t.struct(
        {
            "payloadType": t.string(),
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureIn"])),
            "payload": t.string(),
        }
    ).named(renames["EnvelopeIn"])
    types["EnvelopeOut"] = t.struct(
        {
            "payloadType": t.string(),
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureOut"])),
            "payload": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvelopeOut"])
    types["BatchCreateOccurrencesRequestIn"] = t.struct(
        {"occurrences": t.array(t.proxy(renames["OccurrenceIn"]))}
    ).named(renames["BatchCreateOccurrencesRequestIn"])
    types["BatchCreateOccurrencesRequestOut"] = t.struct(
        {
            "occurrences": t.array(t.proxy(renames["OccurrenceOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateOccurrencesRequestOut"])
    types["CloudRepoSourceContextIn"] = t.struct(
        {
            "repoId": t.proxy(renames["RepoIdIn"]).optional(),
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
            "revisionId": t.string().optional(),
        }
    ).named(renames["CloudRepoSourceContextIn"])
    types["CloudRepoSourceContextOut"] = t.struct(
        {
            "repoId": t.proxy(renames["RepoIdOut"]).optional(),
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "revisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRepoSourceContextOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningIn"] = t.struct(
        {"text": t.string().optional(), "priority": t.string().optional()}
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningOut"] = t.struct(
        {
            "text": t.string().optional(),
            "priority": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"] = t.struct(
        {"id": t.string()}
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"])
    types["SlsaProvenanceIn"] = t.struct(
        {
            "builder": t.proxy(renames["SlsaBuilderIn"]).optional(),
            "metadata": t.proxy(renames["SlsaMetadataIn"]),
            "recipe": t.proxy(renames["SlsaRecipeIn"]).optional(),
            "materials": t.array(t.proxy(renames["MaterialIn"])).optional(),
        }
    ).named(renames["SlsaProvenanceIn"])
    types["SlsaProvenanceOut"] = t.struct(
        {
            "builder": t.proxy(renames["SlsaBuilderOut"]).optional(),
            "metadata": t.proxy(renames["SlsaMetadataOut"]),
            "recipe": t.proxy(renames["SlsaRecipeOut"]).optional(),
            "materials": t.array(t.proxy(renames["MaterialOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaProvenanceOut"])
    types["ListNotesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "notes": t.array(t.proxy(renames["NoteIn"])).optional(),
        }
    ).named(renames["ListNotesResponseIn"])
    types["ListNotesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "notes": t.array(t.proxy(renames["NoteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNotesResponseOut"])
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
    types["OccurrenceIn"] = t.struct(
        {
            "resourceUri": t.string(),
            "name": t.string().optional(),
            "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceOccurrenceIn"]).optional(),
            "updateTime": t.string().optional(),
            "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
            "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
            "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
            "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
            "vulnerability": t.proxy(renames["VulnerabilityOccurrenceIn"]).optional(),
            "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
            "createTime": t.string().optional(),
            "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
            "kind": t.string().optional(),
            "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
            "remediation": t.string().optional(),
            "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
            "noteName": t.string(),
            "dsseAttestation": t.proxy(
                renames["DSSEAttestationOccurrenceIn"]
            ).optional(),
        }
    ).named(renames["OccurrenceIn"])
    types["OccurrenceOut"] = t.struct(
        {
            "resourceUri": t.string(),
            "name": t.string().optional(),
            "discovery": t.proxy(renames["DiscoveryOccurrenceOut"]).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceOccurrenceOut"]).optional(),
            "updateTime": t.string().optional(),
            "envelope": t.proxy(renames["EnvelopeOut"]).optional(),
            "deployment": t.proxy(renames["DeploymentOccurrenceOut"]).optional(),
            "compliance": t.proxy(renames["ComplianceOccurrenceOut"]).optional(),
            "attestation": t.proxy(renames["AttestationOccurrenceOut"]).optional(),
            "vulnerability": t.proxy(renames["VulnerabilityOccurrenceOut"]).optional(),
            "build": t.proxy(renames["BuildOccurrenceOut"]).optional(),
            "createTime": t.string().optional(),
            "upgrade": t.proxy(renames["UpgradeOccurrenceOut"]).optional(),
            "kind": t.string().optional(),
            "package": t.proxy(renames["PackageOccurrenceOut"]).optional(),
            "remediation": t.string().optional(),
            "image": t.proxy(renames["ImageOccurrenceOut"]).optional(),
            "noteName": t.string(),
            "dsseAttestation": t.proxy(
                renames["DSSEAttestationOccurrenceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OccurrenceOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn"] = t.struct(
        {
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "repoName": t.string().optional(),
            "projectId": t.string().optional(),
            "tagName": t.string().optional(),
            "branchName": t.string().optional(),
            "dir": t.string().optional(),
            "commitSha": t.string().optional(),
            "invertRegex": t.boolean().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut"] = t.struct(
        {
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "repoName": t.string().optional(),
            "projectId": t.string().optional(),
            "tagName": t.string().optional(),
            "branchName": t.string().optional(),
            "dir": t.string().optional(),
            "commitSha": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut"])
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
    types["WindowsUpdateIn"] = t.struct(
        {
            "lastPublishedTimestamp": t.string().optional(),
            "description": t.string().optional(),
            "identity": t.proxy(renames["IdentityIn"]),
            "categories": t.array(t.proxy(renames["CategoryIn"])).optional(),
            "kbArticleIds": t.array(t.string()).optional(),
            "supportUrl": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["WindowsUpdateIn"])
    types["WindowsUpdateOut"] = t.struct(
        {
            "lastPublishedTimestamp": t.string().optional(),
            "description": t.string().optional(),
            "identity": t.proxy(renames["IdentityOut"]),
            "categories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "kbArticleIds": t.array(t.string()).optional(),
            "supportUrl": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsUpdateOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceIn"] = t.struct(
        {
            "revision": t.string().optional(),
            "dir": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut"] = t.struct(
        {
            "revision": t.string().optional(),
            "dir": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanIn"] = t.struct(
        {"startTime": t.string().optional(), "endTime": t.string().optional()}
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"])
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
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageIn"
    ] = t.struct(
        {"repository": t.string().optional(), "packagePath": t.string().optional()}
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageOut"
    ] = t.struct(
        {
            "repository": t.string().optional(),
            "packagePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageOut"]
    )
    types["BuilderConfigIn"] = t.struct({"id": t.string()}).named(
        renames["BuilderConfigIn"]
    )
    types["BuilderConfigOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BuilderConfigOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretIn"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "envMap": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "envMap": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretOut"])
    types["SlsaMetadataIn"] = t.struct(
        {
            "buildStartedOn": t.string().optional(),
            "buildInvocationId": t.string().optional(),
            "reproducible": t.boolean().optional(),
            "buildFinishedOn": t.string().optional(),
            "completeness": t.proxy(renames["SlsaCompletenessIn"]).optional(),
        }
    ).named(renames["SlsaMetadataIn"])
    types["SlsaMetadataOut"] = t.struct(
        {
            "buildStartedOn": t.string().optional(),
            "buildInvocationId": t.string().optional(),
            "reproducible": t.boolean().optional(),
            "buildFinishedOn": t.string().optional(),
            "completeness": t.proxy(renames["SlsaCompletenessOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaMetadataOut"])
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactIn"
    ] = t.struct(
        {
            "uri": t.string().optional(),
            "fileHashes": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesIn"]
            ).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactOut"
    ] = t.struct(
        {
            "uri": t.string().optional(),
            "fileHashes": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesOut"]
            ).optional(),
            "pushTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactOut"]
    )
    types["DiscoveryNoteIn"] = t.struct({"analysisKind": t.string()}).named(
        renames["DiscoveryNoteIn"]
    )
    types["DiscoveryNoteOut"] = t.struct(
        {
            "analysisKind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoveryNoteOut"])
    types["InTotoStatementIn"] = t.struct(
        {
            "subject": t.array(t.proxy(renames["SubjectIn"])),
            "slsaProvenanceZeroTwo": t.proxy(renames["SlsaProvenanceZeroTwoIn"]),
            "slsaProvenance": t.proxy(renames["SlsaProvenanceIn"]),
            "provenance": t.proxy(renames["InTotoProvenanceIn"]),
            "_type": t.string().optional(),
            "predicateType": t.string().optional(),
        }
    ).named(renames["InTotoStatementIn"])
    types["InTotoStatementOut"] = t.struct(
        {
            "subject": t.array(t.proxy(renames["SubjectOut"])),
            "slsaProvenanceZeroTwo": t.proxy(renames["SlsaProvenanceZeroTwoOut"]),
            "slsaProvenance": t.proxy(renames["SlsaProvenanceOut"]),
            "provenance": t.proxy(renames["InTotoProvenanceOut"]),
            "_type": t.string().optional(),
            "predicateType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InTotoStatementOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalOut"] = t.struct(
        {
            "result": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultOut"]
            ).optional(),
            "state": t.string().optional(),
            "config": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalOut"])
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
    types["ImageNoteIn"] = t.struct(
        {"resourceUrl": t.string(), "fingerprint": t.proxy(renames["FingerprintIn"])}
    ).named(renames["ImageNoteIn"])
    types["ImageNoteOut"] = t.struct(
        {
            "resourceUrl": t.string(),
            "fingerprint": t.proxy(renames["FingerprintOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageNoteOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesIn"] = t.struct(
        {
            "fileHash": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1HashIn"])
            ).optional()
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesOut"] = t.struct(
        {
            "fileHash": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1HashOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageIn"] = t.struct(
        {"name": t.string().optional(), "digest": t.string().optional()}
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageOut"] = t.struct(
        {
            "name": t.string().optional(),
            "digest": t.string().optional(),
            "pushTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageOut"])
    types["AttestationOccurrenceIn"] = t.struct(
        {
            "signatures": t.array(t.proxy(renames["SignatureIn"])).optional(),
            "serializedPayload": t.string(),
            "jwts": t.array(t.proxy(renames["JwtIn"])).optional(),
        }
    ).named(renames["AttestationOccurrenceIn"])
    types["AttestationOccurrenceOut"] = t.struct(
        {
            "signatures": t.array(t.proxy(renames["SignatureOut"])).optional(),
            "serializedPayload": t.string(),
            "jwts": t.array(t.proxy(renames["JwtOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestationOccurrenceOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoIn"] = t.struct(
        {"detail": t.string().optional(), "type": t.string().optional()}
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoOut"] = t.struct(
        {
            "detail": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoOut"])
    types["ListOccurrencesResponseIn"] = t.struct(
        {
            "occurrences": t.array(t.proxy(renames["OccurrenceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOccurrencesResponseIn"])
    types["ListOccurrencesResponseOut"] = t.struct(
        {
            "occurrences": t.array(t.proxy(renames["OccurrenceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOccurrencesResponseOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn"] = t.struct(
        {"name": t.string().optional(), "path": t.string().optional()}
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut"])
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
    types["NoteIn"] = t.struct(
        {
            "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
            "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
            "longDescription": t.string().optional(),
            "build": t.proxy(renames["BuildNoteIn"]).optional(),
            "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "relatedNoteNames": t.array(t.string()).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
            "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
            "image": t.proxy(renames["ImageNoteIn"]).optional(),
            "shortDescription": t.string().optional(),
            "name": t.string().optional(),
            "expirationTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "vulnerabilityAssessment": t.proxy(
                renames["VulnerabilityAssessmentNoteIn"]
            ).optional(),
            "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
            "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
            "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
            "package": t.proxy(renames["PackageNoteIn"]).optional(),
            "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["NoteIn"])
    types["NoteOut"] = t.struct(
        {
            "compliance": t.proxy(renames["ComplianceNoteOut"]).optional(),
            "vulnerability": t.proxy(renames["VulnerabilityNoteOut"]).optional(),
            "longDescription": t.string().optional(),
            "build": t.proxy(renames["BuildNoteOut"]).optional(),
            "relatedUrl": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "relatedNoteNames": t.array(t.string()).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceNoteOut"]).optional(),
            "upgrade": t.proxy(renames["UpgradeNoteOut"]).optional(),
            "image": t.proxy(renames["ImageNoteOut"]).optional(),
            "shortDescription": t.string().optional(),
            "name": t.string().optional(),
            "expirationTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "vulnerabilityAssessment": t.proxy(
                renames["VulnerabilityAssessmentNoteOut"]
            ).optional(),
            "discovery": t.proxy(renames["DiscoveryNoteOut"]).optional(),
            "deployment": t.proxy(renames["DeploymentNoteOut"]).optional(),
            "dsseAttestation": t.proxy(renames["DSSEAttestationNoteOut"]).optional(),
            "package": t.proxy(renames["PackageNoteOut"]).optional(),
            "attestation": t.proxy(renames["AttestationNoteOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoteOut"])
    types["PublisherIn"] = t.struct(
        {
            "publisherNamespace": t.string().optional(),
            "issuingAuthority": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["PublisherIn"])
    types["PublisherOut"] = t.struct(
        {
            "publisherNamespace": t.string().optional(),
            "issuingAuthority": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherOut"])
    types["ListNoteOccurrencesResponseIn"] = t.struct(
        {
            "occurrences": t.array(t.proxy(renames["OccurrenceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListNoteOccurrencesResponseIn"])
    types["ListNoteOccurrencesResponseOut"] = t.struct(
        {
            "occurrences": t.array(t.proxy(renames["OccurrenceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNoteOccurrencesResponseOut"])

    functions = {}
    functions["projectsNotesBatchCreate"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesSetIamPolicy"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesGet"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesPatch"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesList"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesTestIamPermissions"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesGetIamPolicy"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesCreate"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesDelete"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesOccurrencesList"] = containeranalysis.get(
        "v1/{name}/occurrences",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNoteOccurrencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesGetVulnerabilitySummary"] = containeranalysis.post(
        "v1/{parent}/occurrences:batchCreate",
        t.struct(
            {
                "parent": t.string(),
                "occurrences": t.array(t.proxy(renames["OccurrenceIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchCreateOccurrencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesGetIamPolicy"] = containeranalysis.post(
        "v1/{parent}/occurrences:batchCreate",
        t.struct(
            {
                "parent": t.string(),
                "occurrences": t.array(t.proxy(renames["OccurrenceIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchCreateOccurrencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesTestIamPermissions"] = containeranalysis.post(
        "v1/{parent}/occurrences:batchCreate",
        t.struct(
            {
                "parent": t.string(),
                "occurrences": t.array(t.proxy(renames["OccurrenceIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchCreateOccurrencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesPatch"] = containeranalysis.post(
        "v1/{parent}/occurrences:batchCreate",
        t.struct(
            {
                "parent": t.string(),
                "occurrences": t.array(t.proxy(renames["OccurrenceIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchCreateOccurrencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesSetIamPolicy"] = containeranalysis.post(
        "v1/{parent}/occurrences:batchCreate",
        t.struct(
            {
                "parent": t.string(),
                "occurrences": t.array(t.proxy(renames["OccurrenceIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchCreateOccurrencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesList"] = containeranalysis.post(
        "v1/{parent}/occurrences:batchCreate",
        t.struct(
            {
                "parent": t.string(),
                "occurrences": t.array(t.proxy(renames["OccurrenceIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchCreateOccurrencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesGet"] = containeranalysis.post(
        "v1/{parent}/occurrences:batchCreate",
        t.struct(
            {
                "parent": t.string(),
                "occurrences": t.array(t.proxy(renames["OccurrenceIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchCreateOccurrencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesGetNotes"] = containeranalysis.post(
        "v1/{parent}/occurrences:batchCreate",
        t.struct(
            {
                "parent": t.string(),
                "occurrences": t.array(t.proxy(renames["OccurrenceIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchCreateOccurrencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesDelete"] = containeranalysis.post(
        "v1/{parent}/occurrences:batchCreate",
        t.struct(
            {
                "parent": t.string(),
                "occurrences": t.array(t.proxy(renames["OccurrenceIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchCreateOccurrencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesCreate"] = containeranalysis.post(
        "v1/{parent}/occurrences:batchCreate",
        t.struct(
            {
                "parent": t.string(),
                "occurrences": t.array(t.proxy(renames["OccurrenceIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchCreateOccurrencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesBatchCreate"] = containeranalysis.post(
        "v1/{parent}/occurrences:batchCreate",
        t.struct(
            {
                "parent": t.string(),
                "occurrences": t.array(t.proxy(renames["OccurrenceIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchCreateOccurrencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="containeranalysis",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
