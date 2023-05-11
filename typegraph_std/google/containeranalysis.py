from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_containeranalysis() -> Import:
    containeranalysis = HTTPRuntime("https://containeranalysis.googleapis.com/")

    renames = {
        "ErrorResponse": "_containeranalysis_1_ErrorResponse",
        "SubjectIn": "_containeranalysis_2_SubjectIn",
        "SubjectOut": "_containeranalysis_3_SubjectOut",
        "SBOMReferenceNoteIn": "_containeranalysis_4_SBOMReferenceNoteIn",
        "SBOMReferenceNoteOut": "_containeranalysis_5_SBOMReferenceNoteOut",
        "GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataIn": "_containeranalysis_6_GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataIn",
        "GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataOut": "_containeranalysis_7_GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataOut",
        "NonCompliantFileIn": "_containeranalysis_8_NonCompliantFileIn",
        "NonCompliantFileOut": "_containeranalysis_9_NonCompliantFileOut",
        "VulnerabilityNoteIn": "_containeranalysis_10_VulnerabilityNoteIn",
        "VulnerabilityNoteOut": "_containeranalysis_11_VulnerabilityNoteOut",
        "DSSEAttestationOccurrenceIn": "_containeranalysis_12_DSSEAttestationOccurrenceIn",
        "DSSEAttestationOccurrenceOut": "_containeranalysis_13_DSSEAttestationOccurrenceOut",
        "FingerprintIn": "_containeranalysis_14_FingerprintIn",
        "FingerprintOut": "_containeranalysis_15_FingerprintOut",
        "ListNotesResponseIn": "_containeranalysis_16_ListNotesResponseIn",
        "ListNotesResponseOut": "_containeranalysis_17_ListNotesResponseOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageIn": "_containeranalysis_18_ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageOut": "_containeranalysis_19_ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageOut",
        "FileHashesIn": "_containeranalysis_20_FileHashesIn",
        "FileHashesOut": "_containeranalysis_21_FileHashesOut",
        "TimeSpanIn": "_containeranalysis_22_TimeSpanIn",
        "TimeSpanOut": "_containeranalysis_23_TimeSpanOut",
        "UpgradeOccurrenceIn": "_containeranalysis_24_UpgradeOccurrenceIn",
        "UpgradeOccurrenceOut": "_containeranalysis_25_UpgradeOccurrenceOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesIn": "_containeranalysis_26_ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesOut": "_containeranalysis_27_ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultIn": "_containeranalysis_28_ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultOut": "_containeranalysis_29_ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultOut",
        "VersionIn": "_containeranalysis_30_VersionIn",
        "VersionOut": "_containeranalysis_31_VersionOut",
        "ListOccurrencesResponseIn": "_containeranalysis_32_ListOccurrencesResponseIn",
        "ListOccurrencesResponseOut": "_containeranalysis_33_ListOccurrencesResponseOut",
        "GrafeasV1FileLocationIn": "_containeranalysis_34_GrafeasV1FileLocationIn",
        "GrafeasV1FileLocationOut": "_containeranalysis_35_GrafeasV1FileLocationOut",
        "SbomReferenceIntotoPredicateIn": "_containeranalysis_36_SbomReferenceIntotoPredicateIn",
        "SbomReferenceIntotoPredicateOut": "_containeranalysis_37_SbomReferenceIntotoPredicateOut",
        "ImageOccurrenceIn": "_containeranalysis_38_ImageOccurrenceIn",
        "ImageOccurrenceOut": "_containeranalysis_39_ImageOccurrenceOut",
        "GetPolicyOptionsIn": "_containeranalysis_40_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_containeranalysis_41_GetPolicyOptionsOut",
        "TestIamPermissionsResponseIn": "_containeranalysis_42_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_containeranalysis_43_TestIamPermissionsResponseOut",
        "BuildStepIn": "_containeranalysis_44_BuildStepIn",
        "BuildStepOut": "_containeranalysis_45_BuildStepOut",
        "UpgradeDistributionIn": "_containeranalysis_46_UpgradeDistributionIn",
        "UpgradeDistributionOut": "_containeranalysis_47_UpgradeDistributionOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretIn": "_containeranalysis_48_ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretOut": "_containeranalysis_49_ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretOut",
        "VulnerabilityOccurrenceIn": "_containeranalysis_50_VulnerabilityOccurrenceIn",
        "VulnerabilityOccurrenceOut": "_containeranalysis_51_VulnerabilityOccurrenceOut",
        "SetIamPolicyRequestIn": "_containeranalysis_52_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_containeranalysis_53_SetIamPolicyRequestOut",
        "StatusIn": "_containeranalysis_54_StatusIn",
        "StatusOut": "_containeranalysis_55_StatusOut",
        "BuildNoteIn": "_containeranalysis_56_BuildNoteIn",
        "BuildNoteOut": "_containeranalysis_57_BuildNoteOut",
        "DistributionIn": "_containeranalysis_58_DistributionIn",
        "DistributionOut": "_containeranalysis_59_DistributionOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceIn": "_containeranalysis_60_ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut": "_containeranalysis_61_ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut",
        "HashIn": "_containeranalysis_62_HashIn",
        "HashOut": "_containeranalysis_63_HashOut",
        "CloudRepoSourceContextIn": "_containeranalysis_64_CloudRepoSourceContextIn",
        "CloudRepoSourceContextOut": "_containeranalysis_65_CloudRepoSourceContextOut",
        "SlsaBuilderIn": "_containeranalysis_66_SlsaBuilderIn",
        "SlsaBuilderOut": "_containeranalysis_67_SlsaBuilderOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn": "_containeranalysis_68_GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut": "_containeranalysis_69_GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut",
        "JustificationIn": "_containeranalysis_70_JustificationIn",
        "JustificationOut": "_containeranalysis_71_JustificationOut",
        "ImageNoteIn": "_containeranalysis_72_ImageNoteIn",
        "ImageNoteOut": "_containeranalysis_73_ImageNoteOut",
        "DetailIn": "_containeranalysis_74_DetailIn",
        "DetailOut": "_containeranalysis_75_DetailOut",
        "CVSSv3In": "_containeranalysis_76_CVSSv3In",
        "CVSSv3Out": "_containeranalysis_77_CVSSv3Out",
        "ArtifactIn": "_containeranalysis_78_ArtifactIn",
        "ArtifactOut": "_containeranalysis_79_ArtifactOut",
        "RelatedUrlIn": "_containeranalysis_80_RelatedUrlIn",
        "RelatedUrlOut": "_containeranalysis_81_RelatedUrlOut",
        "ComplianceVersionIn": "_containeranalysis_82_ComplianceVersionIn",
        "ComplianceVersionOut": "_containeranalysis_83_ComplianceVersionOut",
        "EmptyIn": "_containeranalysis_84_EmptyIn",
        "EmptyOut": "_containeranalysis_85_EmptyOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn": "_containeranalysis_86_GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut": "_containeranalysis_87_GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut",
        "OccurrenceIn": "_containeranalysis_88_OccurrenceIn",
        "OccurrenceOut": "_containeranalysis_89_OccurrenceOut",
        "BatchCreateNotesResponseIn": "_containeranalysis_90_BatchCreateNotesResponseIn",
        "BatchCreateNotesResponseOut": "_containeranalysis_91_BatchCreateNotesResponseOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceIn": "_containeranalysis_92_ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut": "_containeranalysis_93_ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut",
        "CVSSIn": "_containeranalysis_94_CVSSIn",
        "CVSSOut": "_containeranalysis_95_CVSSOut",
        "FixableTotalByDigestIn": "_containeranalysis_96_FixableTotalByDigestIn",
        "FixableTotalByDigestOut": "_containeranalysis_97_FixableTotalByDigestOut",
        "CompletenessIn": "_containeranalysis_98_CompletenessIn",
        "CompletenessOut": "_containeranalysis_99_CompletenessOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsIn": "_containeranalysis_100_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsOut": "_containeranalysis_101_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn": "_containeranalysis_102_GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut": "_containeranalysis_103_GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut",
        "PackageNoteIn": "_containeranalysis_104_PackageNoteIn",
        "PackageNoteOut": "_containeranalysis_105_PackageNoteOut",
        "BuildProvenanceIn": "_containeranalysis_106_BuildProvenanceIn",
        "BuildProvenanceOut": "_containeranalysis_107_BuildProvenanceOut",
        "VulnerabilityAssessmentNoteIn": "_containeranalysis_108_VulnerabilityAssessmentNoteIn",
        "VulnerabilityAssessmentNoteOut": "_containeranalysis_109_VulnerabilityAssessmentNoteOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretIn": "_containeranalysis_110_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretOut": "_containeranalysis_111_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretOut",
        "WindowsDetailIn": "_containeranalysis_112_WindowsDetailIn",
        "WindowsDetailOut": "_containeranalysis_113_WindowsDetailOut",
        "SourceIn": "_containeranalysis_114_SourceIn",
        "SourceOut": "_containeranalysis_115_SourceOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn": "_containeranalysis_116_ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut": "_containeranalysis_117_ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut",
        "ComplianceNoteIn": "_containeranalysis_118_ComplianceNoteIn",
        "ComplianceNoteOut": "_containeranalysis_119_ComplianceNoteOut",
        "PublisherIn": "_containeranalysis_120_PublisherIn",
        "PublisherOut": "_containeranalysis_121_PublisherOut",
        "BatchCreateNotesRequestIn": "_containeranalysis_122_BatchCreateNotesRequestIn",
        "BatchCreateNotesRequestOut": "_containeranalysis_123_BatchCreateNotesRequestOut",
        "EnvelopeIn": "_containeranalysis_124_EnvelopeIn",
        "EnvelopeOut": "_containeranalysis_125_EnvelopeOut",
        "DiscoveryNoteIn": "_containeranalysis_126_DiscoveryNoteIn",
        "DiscoveryNoteOut": "_containeranalysis_127_DiscoveryNoteOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn": "_containeranalysis_128_GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut": "_containeranalysis_129_GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut",
        "VulnerabilityOccurrencesSummaryIn": "_containeranalysis_130_VulnerabilityOccurrencesSummaryIn",
        "VulnerabilityOccurrencesSummaryOut": "_containeranalysis_131_VulnerabilityOccurrencesSummaryOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactIn": "_containeranalysis_132_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactOut": "_containeranalysis_133_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactOut",
        "InTotoStatementIn": "_containeranalysis_134_InTotoStatementIn",
        "InTotoStatementOut": "_containeranalysis_135_InTotoStatementOut",
        "BatchCreateOccurrencesRequestIn": "_containeranalysis_136_BatchCreateOccurrencesRequestIn",
        "BatchCreateOccurrencesRequestOut": "_containeranalysis_137_BatchCreateOccurrencesRequestOut",
        "WindowsUpdateIn": "_containeranalysis_138_WindowsUpdateIn",
        "WindowsUpdateOut": "_containeranalysis_139_WindowsUpdateOut",
        "DeploymentNoteIn": "_containeranalysis_140_DeploymentNoteIn",
        "DeploymentNoteOut": "_containeranalysis_141_DeploymentNoteOut",
        "RecipeIn": "_containeranalysis_142_RecipeIn",
        "RecipeOut": "_containeranalysis_143_RecipeOut",
        "SlsaRecipeIn": "_containeranalysis_144_SlsaRecipeIn",
        "SlsaRecipeOut": "_containeranalysis_145_SlsaRecipeOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningIn": "_containeranalysis_146_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningOut": "_containeranalysis_147_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceIn": "_containeranalysis_148_ContaineranalysisGoogleDevtoolsCloudbuildV1SourceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceOut": "_containeranalysis_149_ContaineranalysisGoogleDevtoolsCloudbuildV1SourceOut",
        "AttestationNoteIn": "_containeranalysis_150_AttestationNoteIn",
        "AttestationNoteOut": "_containeranalysis_151_AttestationNoteOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalIn": "_containeranalysis_152_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalOut": "_containeranalysis_153_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalOut",
        "BindingIn": "_containeranalysis_154_BindingIn",
        "BindingOut": "_containeranalysis_155_BindingOut",
        "PackageOccurrenceIn": "_containeranalysis_156_PackageOccurrenceIn",
        "PackageOccurrenceOut": "_containeranalysis_157_PackageOccurrenceOut",
        "CisBenchmarkIn": "_containeranalysis_158_CisBenchmarkIn",
        "CisBenchmarkOut": "_containeranalysis_159_CisBenchmarkOut",
        "LayerIn": "_containeranalysis_160_LayerIn",
        "LayerOut": "_containeranalysis_161_LayerOut",
        "SourceContextIn": "_containeranalysis_162_SourceContextIn",
        "SourceContextOut": "_containeranalysis_163_SourceContextOut",
        "DSSEHintIn": "_containeranalysis_164_DSSEHintIn",
        "DSSEHintOut": "_containeranalysis_165_DSSEHintOut",
        "GerritSourceContextIn": "_containeranalysis_166_GerritSourceContextIn",
        "GerritSourceContextOut": "_containeranalysis_167_GerritSourceContextOut",
        "AttestationOccurrenceIn": "_containeranalysis_168_AttestationOccurrenceIn",
        "AttestationOccurrenceOut": "_containeranalysis_169_AttestationOccurrenceOut",
        "PackageIssueIn": "_containeranalysis_170_PackageIssueIn",
        "PackageIssueOut": "_containeranalysis_171_PackageIssueOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn": "_containeranalysis_172_GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut": "_containeranalysis_173_GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn": "_containeranalysis_174_ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut": "_containeranalysis_175_ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanIn": "_containeranalysis_176_ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut": "_containeranalysis_177_ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn": "_containeranalysis_178_ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut": "_containeranalysis_179_ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsIn": "_containeranalysis_180_ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut": "_containeranalysis_181_ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn": "_containeranalysis_182_GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut": "_containeranalysis_183_GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut",
        "ExprIn": "_containeranalysis_184_ExprIn",
        "ExprOut": "_containeranalysis_185_ExprOut",
        "UpgradeNoteIn": "_containeranalysis_186_UpgradeNoteIn",
        "UpgradeNoteOut": "_containeranalysis_187_UpgradeNoteOut",
        "MetadataIn": "_containeranalysis_188_MetadataIn",
        "MetadataOut": "_containeranalysis_189_MetadataOut",
        "CategoryIn": "_containeranalysis_190_CategoryIn",
        "CategoryOut": "_containeranalysis_191_CategoryOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1HashIn": "_containeranalysis_192_ContaineranalysisGoogleDevtoolsCloudbuildV1HashIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1HashOut": "_containeranalysis_193_ContaineranalysisGoogleDevtoolsCloudbuildV1HashOut",
        "SlsaCompletenessIn": "_containeranalysis_194_SlsaCompletenessIn",
        "SlsaCompletenessOut": "_containeranalysis_195_SlsaCompletenessOut",
        "LocationIn": "_containeranalysis_196_LocationIn",
        "LocationOut": "_containeranalysis_197_LocationOut",
        "ProjectRepoIdIn": "_containeranalysis_198_ProjectRepoIdIn",
        "ProjectRepoIdOut": "_containeranalysis_199_ProjectRepoIdOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretIn": "_containeranalysis_200_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretOut": "_containeranalysis_201_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretOut",
        "AliasContextIn": "_containeranalysis_202_AliasContextIn",
        "AliasContextOut": "_containeranalysis_203_AliasContextOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageIn": "_containeranalysis_204_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageOut": "_containeranalysis_205_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageOut",
        "SbomReferenceIntotoPayloadIn": "_containeranalysis_206_SbomReferenceIntotoPayloadIn",
        "SbomReferenceIntotoPayloadOut": "_containeranalysis_207_SbomReferenceIntotoPayloadOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageIn": "_containeranalysis_208_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageOut": "_containeranalysis_209_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn": "_containeranalysis_210_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut": "_containeranalysis_211_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsIn": "_containeranalysis_212_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsOut": "_containeranalysis_213_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsOut",
        "ListNoteOccurrencesResponseIn": "_containeranalysis_214_ListNoteOccurrencesResponseIn",
        "ListNoteOccurrencesResponseOut": "_containeranalysis_215_ListNoteOccurrencesResponseOut",
        "SignatureIn": "_containeranalysis_216_SignatureIn",
        "SignatureOut": "_containeranalysis_217_SignatureOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn": "_containeranalysis_218_ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut": "_containeranalysis_219_ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut",
        "VolumeIn": "_containeranalysis_220_VolumeIn",
        "VolumeOut": "_containeranalysis_221_VolumeOut",
        "DigestIn": "_containeranalysis_222_DigestIn",
        "DigestOut": "_containeranalysis_223_DigestOut",
        "NoteIn": "_containeranalysis_224_NoteIn",
        "NoteOut": "_containeranalysis_225_NoteOut",
        "PolicyIn": "_containeranalysis_226_PolicyIn",
        "PolicyOut": "_containeranalysis_227_PolicyOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageIn": "_containeranalysis_228_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageOut": "_containeranalysis_229_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageOut",
        "AssessmentIn": "_containeranalysis_230_AssessmentIn",
        "AssessmentOut": "_containeranalysis_231_AssessmentOut",
        "ProductIn": "_containeranalysis_232_ProductIn",
        "ProductOut": "_containeranalysis_233_ProductOut",
        "GetIamPolicyRequestIn": "_containeranalysis_234_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_containeranalysis_235_GetIamPolicyRequestOut",
        "BatchCreateOccurrencesResponseIn": "_containeranalysis_236_BatchCreateOccurrencesResponseIn",
        "BatchCreateOccurrencesResponseOut": "_containeranalysis_237_BatchCreateOccurrencesResponseOut",
        "InTotoProvenanceIn": "_containeranalysis_238_InTotoProvenanceIn",
        "InTotoProvenanceOut": "_containeranalysis_239_InTotoProvenanceOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsIn": "_containeranalysis_240_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOut": "_containeranalysis_241_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOut",
        "BuildOccurrenceIn": "_containeranalysis_242_BuildOccurrenceIn",
        "BuildOccurrenceOut": "_containeranalysis_243_BuildOccurrenceOut",
        "HintIn": "_containeranalysis_244_HintIn",
        "HintOut": "_containeranalysis_245_HintOut",
        "DiscoveryOccurrenceIn": "_containeranalysis_246_DiscoveryOccurrenceIn",
        "DiscoveryOccurrenceOut": "_containeranalysis_247_DiscoveryOccurrenceOut",
        "RemediationIn": "_containeranalysis_248_RemediationIn",
        "RemediationOut": "_containeranalysis_249_RemediationOut",
        "LicenseIn": "_containeranalysis_250_LicenseIn",
        "LicenseOut": "_containeranalysis_251_LicenseOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigIn": "_containeranalysis_252_ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigOut": "_containeranalysis_253_ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigOut",
        "SBOMReferenceOccurrenceIn": "_containeranalysis_254_SBOMReferenceOccurrenceIn",
        "SBOMReferenceOccurrenceOut": "_containeranalysis_255_SBOMReferenceOccurrenceOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactIn": "_containeranalysis_256_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactOut": "_containeranalysis_257_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactOut",
        "JwtIn": "_containeranalysis_258_JwtIn",
        "JwtOut": "_containeranalysis_259_JwtOut",
        "TestIamPermissionsRequestIn": "_containeranalysis_260_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_containeranalysis_261_TestIamPermissionsRequestOut",
        "CommandIn": "_containeranalysis_262_CommandIn",
        "CommandOut": "_containeranalysis_263_CommandOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionIn": "_containeranalysis_264_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionOut": "_containeranalysis_265_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionOut",
        "MaterialIn": "_containeranalysis_266_MaterialIn",
        "MaterialOut": "_containeranalysis_267_MaterialOut",
        "SlsaMetadataIn": "_containeranalysis_268_SlsaMetadataIn",
        "SlsaMetadataOut": "_containeranalysis_269_SlsaMetadataOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn": "_containeranalysis_270_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut": "_containeranalysis_271_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut",
        "EnvelopeSignatureIn": "_containeranalysis_272_EnvelopeSignatureIn",
        "EnvelopeSignatureOut": "_containeranalysis_273_EnvelopeSignatureOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageIn": "_containeranalysis_274_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageOut": "_containeranalysis_275_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageOut",
        "KnowledgeBaseIn": "_containeranalysis_276_KnowledgeBaseIn",
        "KnowledgeBaseOut": "_containeranalysis_277_KnowledgeBaseOut",
        "ComplianceOccurrenceIn": "_containeranalysis_278_ComplianceOccurrenceIn",
        "ComplianceOccurrenceOut": "_containeranalysis_279_ComplianceOccurrenceOut",
        "SlsaProvenanceIn": "_containeranalysis_280_SlsaProvenanceIn",
        "SlsaProvenanceOut": "_containeranalysis_281_SlsaProvenanceOut",
        "AnalysisCompletedIn": "_containeranalysis_282_AnalysisCompletedIn",
        "AnalysisCompletedOut": "_containeranalysis_283_AnalysisCompletedOut",
        "IdentityIn": "_containeranalysis_284_IdentityIn",
        "IdentityOut": "_containeranalysis_285_IdentityOut",
        "DSSEAttestationNoteIn": "_containeranalysis_286_DSSEAttestationNoteIn",
        "DSSEAttestationNoteOut": "_containeranalysis_287_DSSEAttestationNoteOut",
        "BuilderConfigIn": "_containeranalysis_288_BuilderConfigIn",
        "BuilderConfigOut": "_containeranalysis_289_BuilderConfigOut",
        "RepoIdIn": "_containeranalysis_290_RepoIdIn",
        "RepoIdOut": "_containeranalysis_291_RepoIdOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildIn": "_containeranalysis_292_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOut": "_containeranalysis_293_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoIn": "_containeranalysis_294_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoOut": "_containeranalysis_295_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoOut",
        "SlsaProvenanceZeroTwoIn": "_containeranalysis_296_SlsaProvenanceZeroTwoIn",
        "SlsaProvenanceZeroTwoOut": "_containeranalysis_297_SlsaProvenanceZeroTwoOut",
        "GitSourceContextIn": "_containeranalysis_298_GitSourceContextIn",
        "GitSourceContextOut": "_containeranalysis_299_GitSourceContextOut",
        "VexAssessmentIn": "_containeranalysis_300_VexAssessmentIn",
        "VexAssessmentOut": "_containeranalysis_301_VexAssessmentOut",
        "DeploymentOccurrenceIn": "_containeranalysis_302_DeploymentOccurrenceIn",
        "DeploymentOccurrenceOut": "_containeranalysis_303_DeploymentOccurrenceOut",
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
    types["VulnerabilityNoteIn"] = t.struct(
        {
            "cvssV2": t.proxy(renames["CVSSIn"]).optional(),
            "sourceUpdateTime": t.string().optional(),
            "cvssV3": t.proxy(renames["CVSSv3In"]).optional(),
            "details": t.array(t.proxy(renames["DetailIn"])).optional(),
            "windowsDetails": t.array(t.proxy(renames["WindowsDetailIn"])).optional(),
            "cvssVersion": t.string().optional(),
            "cvssScore": t.number().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["VulnerabilityNoteIn"])
    types["VulnerabilityNoteOut"] = t.struct(
        {
            "cvssV2": t.proxy(renames["CVSSOut"]).optional(),
            "sourceUpdateTime": t.string().optional(),
            "cvssV3": t.proxy(renames["CVSSv3Out"]).optional(),
            "details": t.array(t.proxy(renames["DetailOut"])).optional(),
            "windowsDetails": t.array(t.proxy(renames["WindowsDetailOut"])).optional(),
            "cvssVersion": t.string().optional(),
            "cvssScore": t.number().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityNoteOut"])
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
    types["FingerprintIn"] = t.struct(
        {
            "v2Blob": t.array(t.string()),
            "v2Name": t.string().optional(),
            "v1Name": t.string(),
        }
    ).named(renames["FingerprintIn"])
    types["FingerprintOut"] = t.struct(
        {
            "v2Blob": t.array(t.string()),
            "v2Name": t.string().optional(),
            "v1Name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FingerprintOut"])
    types["ListNotesResponseIn"] = t.struct(
        {
            "notes": t.array(t.proxy(renames["NoteIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListNotesResponseIn"])
    types["ListNotesResponseOut"] = t.struct(
        {
            "notes": t.array(t.proxy(renames["NoteOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNotesResponseOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageIn"] = t.struct(
        {"name": t.string().optional(), "digest": t.string().optional()}
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageOut"] = t.struct(
        {
            "pushTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "name": t.string().optional(),
            "digest": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageOut"])
    types["FileHashesIn"] = t.struct(
        {"fileHash": t.array(t.proxy(renames["HashIn"]))}
    ).named(renames["FileHashesIn"])
    types["FileHashesOut"] = t.struct(
        {
            "fileHash": t.array(t.proxy(renames["HashOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileHashesOut"])
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
    types["UpgradeOccurrenceIn"] = t.struct(
        {
            "windowsUpdate": t.proxy(renames["WindowsUpdateIn"]),
            "parsedVersion": t.proxy(renames["VersionIn"]),
            "distribution": t.proxy(renames["UpgradeDistributionIn"]).optional(),
            "package": t.string(),
        }
    ).named(renames["UpgradeOccurrenceIn"])
    types["UpgradeOccurrenceOut"] = t.struct(
        {
            "windowsUpdate": t.proxy(renames["WindowsUpdateOut"]),
            "parsedVersion": t.proxy(renames["VersionOut"]),
            "distribution": t.proxy(renames["UpgradeDistributionOut"]).optional(),
            "package": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeOccurrenceOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultIn"] = t.struct(
        {
            "decision": t.string(),
            "url": t.string().optional(),
            "comment": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultOut"] = t.struct(
        {
            "decision": t.string(),
            "url": t.string().optional(),
            "approverAccount": t.string().optional(),
            "approvalTime": t.string().optional(),
            "comment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultOut"])
    types["VersionIn"] = t.struct(
        {
            "epoch": t.integer().optional(),
            "name": t.string(),
            "kind": t.string(),
            "revision": t.string().optional(),
            "inclusive": t.boolean().optional(),
            "fullName": t.string().optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "epoch": t.integer().optional(),
            "name": t.string(),
            "kind": t.string(),
            "revision": t.string().optional(),
            "inclusive": t.boolean().optional(),
            "fullName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
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
            "digest": t.struct({"_": t.string().optional()}).optional(),
            "mimeType": t.string().optional(),
            "referrerId": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["SbomReferenceIntotoPredicateIn"])
    types["SbomReferenceIntotoPredicateOut"] = t.struct(
        {
            "digest": t.struct({"_": t.string().optional()}).optional(),
            "mimeType": t.string().optional(),
            "referrerId": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SbomReferenceIntotoPredicateOut"])
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
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["BuildStepIn"] = t.struct(
        {
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "exitCode": t.integer().optional(),
            "secretEnv": t.array(t.string()).optional(),
            "allowFailure": t.boolean().optional(),
            "env": t.array(t.string()).optional(),
            "entrypoint": t.string().optional(),
            "timeout": t.string().optional(),
            "script": t.string().optional(),
            "status": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "pullTiming": t.proxy(renames["TimeSpanIn"]).optional(),
            "name": t.string(),
            "allowExitCodes": t.array(t.integer()).optional(),
            "dir": t.string().optional(),
            "timing": t.proxy(renames["TimeSpanIn"]).optional(),
        }
    ).named(renames["BuildStepIn"])
    types["BuildStepOut"] = t.struct(
        {
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "exitCode": t.integer().optional(),
            "secretEnv": t.array(t.string()).optional(),
            "allowFailure": t.boolean().optional(),
            "env": t.array(t.string()).optional(),
            "entrypoint": t.string().optional(),
            "timeout": t.string().optional(),
            "script": t.string().optional(),
            "status": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "pullTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "name": t.string(),
            "allowExitCodes": t.array(t.integer()).optional(),
            "dir": t.string().optional(),
            "timing": t.proxy(renames["TimeSpanOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildStepOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretIn"] = t.struct(
        {
            "envMap": t.struct({"_": t.string().optional()}).optional(),
            "kmsKeyName": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretOut"] = t.struct(
        {
            "envMap": t.struct({"_": t.string().optional()}).optional(),
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretOut"])
    types["VulnerabilityOccurrenceIn"] = t.struct(
        {
            "effectiveSeverity": t.string().optional(),
            "cvssVersion": t.string().optional(),
            "vexAssessment": t.proxy(renames["VexAssessmentIn"]),
            "severity": t.string().optional(),
            "longDescription": t.string().optional(),
            "cvssScore": t.number().optional(),
            "type": t.string().optional(),
            "shortDescription": t.string().optional(),
            "packageIssue": t.array(t.proxy(renames["PackageIssueIn"])),
            "cvssv3": t.proxy(renames["CVSSIn"]).optional(),
            "cvssV2": t.proxy(renames["CVSSIn"]).optional(),
            "fixAvailable": t.boolean().optional(),
            "relatedUrls": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
        }
    ).named(renames["VulnerabilityOccurrenceIn"])
    types["VulnerabilityOccurrenceOut"] = t.struct(
        {
            "effectiveSeverity": t.string().optional(),
            "cvssVersion": t.string().optional(),
            "vexAssessment": t.proxy(renames["VexAssessmentOut"]),
            "severity": t.string().optional(),
            "longDescription": t.string().optional(),
            "cvssScore": t.number().optional(),
            "type": t.string().optional(),
            "shortDescription": t.string().optional(),
            "packageIssue": t.array(t.proxy(renames["PackageIssueOut"])),
            "cvssv3": t.proxy(renames["CVSSOut"]).optional(),
            "cvssV2": t.proxy(renames["CVSSOut"]).optional(),
            "fixAvailable": t.boolean().optional(),
            "relatedUrls": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
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
    types["BuildNoteIn"] = t.struct({"builderVersion": t.string()}).named(
        renames["BuildNoteIn"]
    )
    types["BuildNoteOut"] = t.struct(
        {
            "builderVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildNoteOut"])
    types["DistributionIn"] = t.struct(
        {
            "description": t.string().optional(),
            "url": t.string().optional(),
            "maintainer": t.string().optional(),
            "architecture": t.string().optional(),
            "cpeUri": t.string(),
            "latestVersion": t.proxy(renames["VersionIn"]).optional(),
        }
    ).named(renames["DistributionIn"])
    types["DistributionOut"] = t.struct(
        {
            "description": t.string().optional(),
            "url": t.string().optional(),
            "maintainer": t.string().optional(),
            "architecture": t.string().optional(),
            "cpeUri": t.string(),
            "latestVersion": t.proxy(renames["VersionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DistributionOut"])
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
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "resolvedStorageSourceManifest": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut"
                ]
            ).optional(),
            "resolvedStorageSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut"])
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
    types["CloudRepoSourceContextIn"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "repoId": t.proxy(renames["RepoIdIn"]).optional(),
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
        }
    ).named(renames["CloudRepoSourceContextIn"])
    types["CloudRepoSourceContextOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "repoId": t.proxy(renames["RepoIdOut"]).optional(),
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRepoSourceContextOut"])
    types["SlsaBuilderIn"] = t.struct({"id": t.string()}).named(
        renames["SlsaBuilderIn"]
    )
    types["SlsaBuilderOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SlsaBuilderOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"] = t.struct(
        {"id": t.string()}
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"])
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
    types["ImageNoteIn"] = t.struct(
        {"fingerprint": t.proxy(renames["FingerprintIn"]), "resourceUrl": t.string()}
    ).named(renames["ImageNoteIn"])
    types["ImageNoteOut"] = t.struct(
        {
            "fingerprint": t.proxy(renames["FingerprintOut"]),
            "resourceUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageNoteOut"])
    types["DetailIn"] = t.struct(
        {
            "affectedVersionStart": t.proxy(renames["VersionIn"]).optional(),
            "packageType": t.string().optional(),
            "source": t.string().optional(),
            "vendor": t.string().optional(),
            "isObsolete": t.boolean().optional(),
            "severityName": t.string().optional(),
            "affectedCpeUri": t.string(),
            "sourceUpdateTime": t.string().optional(),
            "fixedCpeUri": t.string().optional(),
            "affectedPackage": t.string(),
            "fixedPackage": t.string().optional(),
            "affectedVersionEnd": t.proxy(renames["VersionIn"]).optional(),
            "description": t.string().optional(),
            "fixedVersion": t.proxy(renames["VersionIn"]).optional(),
        }
    ).named(renames["DetailIn"])
    types["DetailOut"] = t.struct(
        {
            "affectedVersionStart": t.proxy(renames["VersionOut"]).optional(),
            "packageType": t.string().optional(),
            "source": t.string().optional(),
            "vendor": t.string().optional(),
            "isObsolete": t.boolean().optional(),
            "severityName": t.string().optional(),
            "affectedCpeUri": t.string(),
            "sourceUpdateTime": t.string().optional(),
            "fixedCpeUri": t.string().optional(),
            "affectedPackage": t.string(),
            "fixedPackage": t.string().optional(),
            "affectedVersionEnd": t.proxy(renames["VersionOut"]).optional(),
            "description": t.string().optional(),
            "fixedVersion": t.proxy(renames["VersionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetailOut"])
    types["CVSSv3In"] = t.struct(
        {
            "attackVector": t.string().optional(),
            "privilegesRequired": t.string(),
            "userInteraction": t.string(),
            "scope": t.string(),
            "attackComplexity": t.string(),
            "baseScore": t.number().optional(),
            "availabilityImpact": t.string(),
            "impactScore": t.number(),
            "confidentialityImpact": t.string(),
            "integrityImpact": t.string(),
            "exploitabilityScore": t.number(),
        }
    ).named(renames["CVSSv3In"])
    types["CVSSv3Out"] = t.struct(
        {
            "attackVector": t.string().optional(),
            "privilegesRequired": t.string(),
            "userInteraction": t.string(),
            "scope": t.string(),
            "attackComplexity": t.string(),
            "baseScore": t.number().optional(),
            "availabilityImpact": t.string(),
            "impactScore": t.number(),
            "confidentialityImpact": t.string(),
            "integrityImpact": t.string(),
            "exploitabilityScore": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CVSSv3Out"])
    types["ArtifactIn"] = t.struct(
        {
            "names": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "checksum": t.string().optional(),
        }
    ).named(renames["ArtifactIn"])
    types["ArtifactOut"] = t.struct(
        {
            "names": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "checksum": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArtifactOut"])
    types["RelatedUrlIn"] = t.struct(
        {"url": t.string().optional(), "label": t.string().optional()}
    ).named(renames["RelatedUrlIn"])
    types["RelatedUrlOut"] = t.struct(
        {
            "url": t.string().optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelatedUrlOut"])
    types["ComplianceVersionIn"] = t.struct(
        {
            "benchmarkDocument": t.string().optional(),
            "cpeUri": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["ComplianceVersionIn"])
    types["ComplianceVersionOut"] = t.struct(
        {
            "benchmarkDocument": t.string().optional(),
            "cpeUri": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComplianceVersionOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["OccurrenceIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
            "noteName": t.string(),
            "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
            "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
            "name": t.string().optional(),
            "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
            "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
            "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
            "dsseAttestation": t.proxy(
                renames["DSSEAttestationOccurrenceIn"]
            ).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceOccurrenceIn"]).optional(),
            "kind": t.string().optional(),
            "createTime": t.string().optional(),
            "remediation": t.string().optional(),
            "resourceUri": t.string(),
            "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
            "vulnerability": t.proxy(renames["VulnerabilityOccurrenceIn"]).optional(),
            "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
            "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
        }
    ).named(renames["OccurrenceIn"])
    types["OccurrenceOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "discovery": t.proxy(renames["DiscoveryOccurrenceOut"]).optional(),
            "noteName": t.string(),
            "upgrade": t.proxy(renames["UpgradeOccurrenceOut"]).optional(),
            "envelope": t.proxy(renames["EnvelopeOut"]).optional(),
            "name": t.string().optional(),
            "image": t.proxy(renames["ImageOccurrenceOut"]).optional(),
            "package": t.proxy(renames["PackageOccurrenceOut"]).optional(),
            "attestation": t.proxy(renames["AttestationOccurrenceOut"]).optional(),
            "dsseAttestation": t.proxy(
                renames["DSSEAttestationOccurrenceOut"]
            ).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceOccurrenceOut"]).optional(),
            "kind": t.string().optional(),
            "createTime": t.string().optional(),
            "remediation": t.string().optional(),
            "resourceUri": t.string(),
            "deployment": t.proxy(renames["DeploymentOccurrenceOut"]).optional(),
            "vulnerability": t.proxy(renames["VulnerabilityOccurrenceOut"]).optional(),
            "build": t.proxy(renames["BuildOccurrenceOut"]).optional(),
            "compliance": t.proxy(renames["ComplianceOccurrenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OccurrenceOut"])
    types["BatchCreateNotesResponseIn"] = t.struct(
        {"notes": t.array(t.proxy(renames["NoteIn"])).optional()}
    ).named(renames["BatchCreateNotesResponseIn"])
    types["BatchCreateNotesResponseOut"] = t.struct(
        {
            "notes": t.array(t.proxy(renames["NoteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateNotesResponseOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceIn"] = t.struct(
        {
            "dir": t.string().optional(),
            "url": t.string().optional(),
            "revision": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut"] = t.struct(
        {
            "dir": t.string().optional(),
            "url": t.string().optional(),
            "revision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut"])
    types["CVSSIn"] = t.struct(
        {
            "scope": t.string(),
            "impactScore": t.number(),
            "attackVector": t.string().optional(),
            "integrityImpact": t.string(),
            "baseScore": t.number().optional(),
            "availabilityImpact": t.string(),
            "privilegesRequired": t.string(),
            "authentication": t.string(),
            "exploitabilityScore": t.number(),
            "confidentialityImpact": t.string(),
            "attackComplexity": t.string(),
            "userInteraction": t.string(),
        }
    ).named(renames["CVSSIn"])
    types["CVSSOut"] = t.struct(
        {
            "scope": t.string(),
            "impactScore": t.number(),
            "attackVector": t.string().optional(),
            "integrityImpact": t.string(),
            "baseScore": t.number().optional(),
            "availabilityImpact": t.string(),
            "privilegesRequired": t.string(),
            "authentication": t.string(),
            "exploitabilityScore": t.number(),
            "confidentialityImpact": t.string(),
            "attackComplexity": t.string(),
            "userInteraction": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CVSSOut"])
    types["FixableTotalByDigestIn"] = t.struct(
        {
            "totalCount": t.string().optional(),
            "severity": t.string().optional(),
            "resourceUri": t.string().optional(),
            "fixableCount": t.string().optional(),
        }
    ).named(renames["FixableTotalByDigestIn"])
    types["FixableTotalByDigestOut"] = t.struct(
        {
            "totalCount": t.string().optional(),
            "severity": t.string().optional(),
            "resourceUri": t.string().optional(),
            "fixableCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FixableTotalByDigestOut"])
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
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsIn"
    ] = t.struct(
        {"paths": t.array(t.string()).optional(), "location": t.string().optional()}
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsOut"
    ] = t.struct(
        {
            "timing": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "paths": t.array(t.string()).optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsOut"
        ]
    )
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"] = t.struct(
        {
            "environment": t.boolean(),
            "materials": t.boolean(),
            "parameters": t.boolean(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"] = t.struct(
        {
            "environment": t.boolean(),
            "materials": t.boolean(),
            "parameters": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"])
    types["PackageNoteIn"] = t.struct(
        {
            "url": t.string().optional(),
            "packageType": t.string().optional(),
            "distribution": t.array(t.proxy(renames["DistributionIn"])).optional(),
            "version": t.proxy(renames["VersionIn"]).optional(),
            "license": t.proxy(renames["LicenseIn"]).optional(),
            "maintainer": t.string().optional(),
            "description": t.string().optional(),
            "cpeUri": t.string().optional(),
            "digest": t.array(t.proxy(renames["DigestIn"])).optional(),
            "name": t.string(),
            "architecture": t.string().optional(),
        }
    ).named(renames["PackageNoteIn"])
    types["PackageNoteOut"] = t.struct(
        {
            "url": t.string().optional(),
            "packageType": t.string().optional(),
            "distribution": t.array(t.proxy(renames["DistributionOut"])).optional(),
            "version": t.proxy(renames["VersionOut"]).optional(),
            "license": t.proxy(renames["LicenseOut"]).optional(),
            "maintainer": t.string().optional(),
            "description": t.string().optional(),
            "cpeUri": t.string().optional(),
            "digest": t.array(t.proxy(renames["DigestOut"])).optional(),
            "name": t.string(),
            "architecture": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageNoteOut"])
    types["BuildProvenanceIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "creator": t.string().optional(),
            "builtArtifacts": t.array(t.proxy(renames["ArtifactIn"])).optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "sourceProvenance": t.proxy(renames["SourceIn"]).optional(),
            "startTime": t.string().optional(),
            "triggerId": t.string().optional(),
            "logsUri": t.string().optional(),
            "commands": t.array(t.proxy(renames["CommandIn"])).optional(),
            "id": t.string(),
            "buildOptions": t.struct({"_": t.string().optional()}).optional(),
            "builderVersion": t.string().optional(),
        }
    ).named(renames["BuildProvenanceIn"])
    types["BuildProvenanceOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "creator": t.string().optional(),
            "builtArtifacts": t.array(t.proxy(renames["ArtifactOut"])).optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "sourceProvenance": t.proxy(renames["SourceOut"]).optional(),
            "startTime": t.string().optional(),
            "triggerId": t.string().optional(),
            "logsUri": t.string().optional(),
            "commands": t.array(t.proxy(renames["CommandOut"])).optional(),
            "id": t.string(),
            "buildOptions": t.struct({"_": t.string().optional()}).optional(),
            "builderVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildProvenanceOut"])
    types["VulnerabilityAssessmentNoteIn"] = t.struct(
        {
            "longDescription": t.string().optional(),
            "shortDescription": t.string().optional(),
            "assessment": t.proxy(renames["AssessmentIn"]).optional(),
            "product": t.proxy(renames["ProductIn"]).optional(),
            "languageCode": t.string().optional(),
            "title": t.string().optional(),
            "publisher": t.proxy(renames["PublisherIn"]).optional(),
        }
    ).named(renames["VulnerabilityAssessmentNoteIn"])
    types["VulnerabilityAssessmentNoteOut"] = t.struct(
        {
            "longDescription": t.string().optional(),
            "shortDescription": t.string().optional(),
            "assessment": t.proxy(renames["AssessmentOut"]).optional(),
            "product": t.proxy(renames["ProductOut"]).optional(),
            "languageCode": t.string().optional(),
            "title": t.string().optional(),
            "publisher": t.proxy(renames["PublisherOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityAssessmentNoteOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretIn"] = t.struct(
        {
            "secretEnv": t.struct({"_": t.string().optional()}).optional(),
            "kmsKeyName": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretOut"] = t.struct(
        {
            "secretEnv": t.struct({"_": t.string().optional()}).optional(),
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretOut"])
    types["WindowsDetailIn"] = t.struct(
        {
            "name": t.string(),
            "cpeUri": t.string(),
            "description": t.string().optional(),
            "fixingKbs": t.array(t.proxy(renames["KnowledgeBaseIn"])),
        }
    ).named(renames["WindowsDetailIn"])
    types["WindowsDetailOut"] = t.struct(
        {
            "name": t.string(),
            "cpeUri": t.string(),
            "description": t.string().optional(),
            "fixingKbs": t.array(t.proxy(renames["KnowledgeBaseOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsDetailOut"])
    types["SourceIn"] = t.struct(
        {
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "artifactStorageSourceUri": t.string().optional(),
            "context": t.proxy(renames["SourceContextIn"]).optional(),
            "additionalContexts": t.array(
                t.proxy(renames["SourceContextIn"])
            ).optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "artifactStorageSourceUri": t.string().optional(),
            "context": t.proxy(renames["SourceContextOut"]).optional(),
            "additionalContexts": t.array(
                t.proxy(renames["SourceContextOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn"] = t.struct(
        {"path": t.string().optional(), "name": t.string().optional()}
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut"] = t.struct(
        {
            "path": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut"])
    types["ComplianceNoteIn"] = t.struct(
        {
            "title": t.string().optional(),
            "scanInstructions": t.string().optional(),
            "cisBenchmark": t.proxy(renames["CisBenchmarkIn"]),
            "version": t.array(t.proxy(renames["ComplianceVersionIn"])).optional(),
            "rationale": t.string().optional(),
            "description": t.string().optional(),
            "remediation": t.string().optional(),
        }
    ).named(renames["ComplianceNoteIn"])
    types["ComplianceNoteOut"] = t.struct(
        {
            "title": t.string().optional(),
            "scanInstructions": t.string().optional(),
            "cisBenchmark": t.proxy(renames["CisBenchmarkOut"]),
            "version": t.array(t.proxy(renames["ComplianceVersionOut"])).optional(),
            "rationale": t.string().optional(),
            "description": t.string().optional(),
            "remediation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComplianceNoteOut"])
    types["PublisherIn"] = t.struct(
        {
            "name": t.string().optional(),
            "issuingAuthority": t.string().optional(),
            "publisherNamespace": t.string().optional(),
        }
    ).named(renames["PublisherIn"])
    types["PublisherOut"] = t.struct(
        {
            "name": t.string().optional(),
            "issuingAuthority": t.string().optional(),
            "publisherNamespace": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherOut"])
    types["BatchCreateNotesRequestIn"] = t.struct(
        {"notes": t.struct({"_": t.string().optional()})}
    ).named(renames["BatchCreateNotesRequestIn"])
    types["BatchCreateNotesRequestOut"] = t.struct(
        {
            "notes": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateNotesRequestOut"])
    types["EnvelopeIn"] = t.struct(
        {
            "payload": t.string(),
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureIn"])),
            "payloadType": t.string(),
        }
    ).named(renames["EnvelopeIn"])
    types["EnvelopeOut"] = t.struct(
        {
            "payload": t.string(),
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureOut"])),
            "payloadType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvelopeOut"])
    types["DiscoveryNoteIn"] = t.struct({"analysisKind": t.string()}).named(
        renames["DiscoveryNoteIn"]
    )
    types["DiscoveryNoteOut"] = t.struct(
        {
            "analysisKind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoveryNoteOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"] = t.struct(
        {
            "reproducible": t.boolean(),
            "completeness": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"]
            ),
            "buildFinishedOn": t.string(),
            "buildInvocationId": t.string(),
            "buildStartedOn": t.string(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"] = t.struct(
        {
            "reproducible": t.boolean(),
            "completeness": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"]
            ),
            "buildFinishedOn": t.string(),
            "buildInvocationId": t.string(),
            "buildStartedOn": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"])
    types["VulnerabilityOccurrencesSummaryIn"] = t.struct(
        {"counts": t.array(t.proxy(renames["FixableTotalByDigestIn"])).optional()}
    ).named(renames["VulnerabilityOccurrencesSummaryIn"])
    types["VulnerabilityOccurrencesSummaryOut"] = t.struct(
        {
            "counts": t.array(t.proxy(renames["FixableTotalByDigestOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityOccurrencesSummaryOut"])
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactIn"
    ] = t.struct(
        {
            "fileHashes": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesIn"]
            ).optional(),
            "uri": t.string().optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactOut"
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
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactOut"]
    )
    types["InTotoStatementIn"] = t.struct(
        {
            "slsaProvenanceZeroTwo": t.proxy(renames["SlsaProvenanceZeroTwoIn"]),
            "subject": t.array(t.proxy(renames["SubjectIn"])),
            "_type": t.string().optional(),
            "slsaProvenance": t.proxy(renames["SlsaProvenanceIn"]),
            "provenance": t.proxy(renames["InTotoProvenanceIn"]),
            "predicateType": t.string().optional(),
        }
    ).named(renames["InTotoStatementIn"])
    types["InTotoStatementOut"] = t.struct(
        {
            "slsaProvenanceZeroTwo": t.proxy(renames["SlsaProvenanceZeroTwoOut"]),
            "subject": t.array(t.proxy(renames["SubjectOut"])),
            "_type": t.string().optional(),
            "slsaProvenance": t.proxy(renames["SlsaProvenanceOut"]),
            "provenance": t.proxy(renames["InTotoProvenanceOut"]),
            "predicateType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InTotoStatementOut"])
    types["BatchCreateOccurrencesRequestIn"] = t.struct(
        {"occurrences": t.array(t.proxy(renames["OccurrenceIn"]))}
    ).named(renames["BatchCreateOccurrencesRequestIn"])
    types["BatchCreateOccurrencesRequestOut"] = t.struct(
        {
            "occurrences": t.array(t.proxy(renames["OccurrenceOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateOccurrencesRequestOut"])
    types["WindowsUpdateIn"] = t.struct(
        {
            "lastPublishedTimestamp": t.string().optional(),
            "supportUrl": t.string().optional(),
            "kbArticleIds": t.array(t.string()).optional(),
            "identity": t.proxy(renames["IdentityIn"]),
            "title": t.string().optional(),
            "categories": t.array(t.proxy(renames["CategoryIn"])).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["WindowsUpdateIn"])
    types["WindowsUpdateOut"] = t.struct(
        {
            "lastPublishedTimestamp": t.string().optional(),
            "supportUrl": t.string().optional(),
            "kbArticleIds": t.array(t.string()).optional(),
            "identity": t.proxy(renames["IdentityOut"]),
            "title": t.string().optional(),
            "categories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsUpdateOut"])
    types["DeploymentNoteIn"] = t.struct({"resourceUri": t.array(t.string())}).named(
        renames["DeploymentNoteIn"]
    )
    types["DeploymentNoteOut"] = t.struct(
        {
            "resourceUri": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentNoteOut"])
    types["RecipeIn"] = t.struct(
        {
            "entryPoint": t.string().optional(),
            "arguments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "environment": t.array(t.struct({"_": t.string().optional()})).optional(),
            "type": t.string().optional(),
            "definedInMaterial": t.string().optional(),
        }
    ).named(renames["RecipeIn"])
    types["RecipeOut"] = t.struct(
        {
            "entryPoint": t.string().optional(),
            "arguments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "environment": t.array(t.struct({"_": t.string().optional()})).optional(),
            "type": t.string().optional(),
            "definedInMaterial": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecipeOut"])
    types["SlsaRecipeIn"] = t.struct(
        {
            "type": t.string().optional(),
            "arguments": t.struct({"_": t.string().optional()}).optional(),
            "definedInMaterial": t.string().optional(),
            "entryPoint": t.string().optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SlsaRecipeIn"])
    types["SlsaRecipeOut"] = t.struct(
        {
            "type": t.string().optional(),
            "arguments": t.struct({"_": t.string().optional()}).optional(),
            "definedInMaterial": t.string().optional(),
            "entryPoint": t.string().optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaRecipeOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningIn"] = t.struct(
        {"priority": t.string().optional(), "text": t.string().optional()}
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningOut"] = t.struct(
        {
            "priority": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceIn"] = t.struct(
        {
            "gitSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceIn"]
            ).optional(),
            "storageSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn"]
            ).optional(),
            "repoSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn"]
            ).optional(),
            "storageSourceManifest": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn"
                ]
            ).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceOut"] = t.struct(
        {
            "gitSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut"]
            ).optional(),
            "storageSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut"]
            ).optional(),
            "repoSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut"]
            ).optional(),
            "storageSourceManifest": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceOut"])
    types["AttestationNoteIn"] = t.struct(
        {"hint": t.proxy(renames["HintIn"]).optional()}
    ).named(renames["AttestationNoteIn"])
    types["AttestationNoteOut"] = t.struct(
        {
            "hint": t.proxy(renames["HintOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestationNoteOut"])
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
    types["PackageOccurrenceIn"] = t.struct(
        {
            "location": t.array(t.proxy(renames["LocationIn"])).optional(),
            "license": t.proxy(renames["LicenseIn"]).optional(),
        }
    ).named(renames["PackageOccurrenceIn"])
    types["PackageOccurrenceOut"] = t.struct(
        {
            "name": t.string(),
            "architecture": t.string().optional(),
            "location": t.array(t.proxy(renames["LocationOut"])).optional(),
            "license": t.proxy(renames["LicenseOut"]).optional(),
            "version": t.proxy(renames["VersionOut"]).optional(),
            "packageType": t.string().optional(),
            "cpeUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageOccurrenceOut"])
    types["CisBenchmarkIn"] = t.struct(
        {"profileLevel": t.integer(), "severity": t.string()}
    ).named(renames["CisBenchmarkIn"])
    types["CisBenchmarkOut"] = t.struct(
        {
            "profileLevel": t.integer(),
            "severity": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CisBenchmarkOut"])
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
    types["SourceContextIn"] = t.struct(
        {
            "git": t.proxy(renames["GitSourceContextIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gerrit": t.proxy(renames["GerritSourceContextIn"]).optional(),
            "cloudRepo": t.proxy(renames["CloudRepoSourceContextIn"]).optional(),
        }
    ).named(renames["SourceContextIn"])
    types["SourceContextOut"] = t.struct(
        {
            "git": t.proxy(renames["GitSourceContextOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gerrit": t.proxy(renames["GerritSourceContextOut"]).optional(),
            "cloudRepo": t.proxy(renames["CloudRepoSourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["DSSEHintIn"] = t.struct({"humanReadableName": t.string()}).named(
        renames["DSSEHintIn"]
    )
    types["DSSEHintOut"] = t.struct(
        {
            "humanReadableName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DSSEHintOut"])
    types["GerritSourceContextIn"] = t.struct(
        {
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
            "revisionId": t.string().optional(),
            "gerritProject": t.string().optional(),
            "hostUri": t.string().optional(),
        }
    ).named(renames["GerritSourceContextIn"])
    types["GerritSourceContextOut"] = t.struct(
        {
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "revisionId": t.string().optional(),
            "gerritProject": t.string().optional(),
            "hostUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GerritSourceContextOut"])
    types["AttestationOccurrenceIn"] = t.struct(
        {
            "jwts": t.array(t.proxy(renames["JwtIn"])).optional(),
            "signatures": t.array(t.proxy(renames["SignatureIn"])).optional(),
            "serializedPayload": t.string(),
        }
    ).named(renames["AttestationOccurrenceIn"])
    types["AttestationOccurrenceOut"] = t.struct(
        {
            "jwts": t.array(t.proxy(renames["JwtOut"])).optional(),
            "signatures": t.array(t.proxy(renames["SignatureOut"])).optional(),
            "serializedPayload": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestationOccurrenceOut"])
    types["PackageIssueIn"] = t.struct(
        {
            "affectedCpeUri": t.string(),
            "affectedPackage": t.string(),
            "fixedPackage": t.string().optional(),
            "packageType": t.string().optional(),
            "affectedVersion": t.proxy(renames["VersionIn"]),
            "fixAvailable": t.boolean().optional(),
            "fixedVersion": t.proxy(renames["VersionIn"]),
            "fileLocation": t.array(
                t.proxy(renames["GrafeasV1FileLocationIn"])
            ).optional(),
            "fixedCpeUri": t.string().optional(),
        }
    ).named(renames["PackageIssueIn"])
    types["PackageIssueOut"] = t.struct(
        {
            "affectedCpeUri": t.string(),
            "affectedPackage": t.string(),
            "fixedPackage": t.string().optional(),
            "effectiveSeverity": t.string().optional(),
            "packageType": t.string().optional(),
            "affectedVersion": t.proxy(renames["VersionOut"]),
            "fixAvailable": t.boolean().optional(),
            "fixedVersion": t.proxy(renames["VersionOut"]),
            "fileLocation": t.array(
                t.proxy(renames["GrafeasV1FileLocationOut"])
            ).optional(),
            "fixedCpeUri": t.string().optional(),
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn"] = t.struct(
        {
            "invertRegex": t.boolean().optional(),
            "commitSha": t.string().optional(),
            "branchName": t.string().optional(),
            "dir": t.string().optional(),
            "projectId": t.string().optional(),
            "tagName": t.string().optional(),
            "repoName": t.string().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut"] = t.struct(
        {
            "invertRegex": t.boolean().optional(),
            "commitSha": t.string().optional(),
            "branchName": t.string().optional(),
            "dir": t.string().optional(),
            "projectId": t.string().optional(),
            "tagName": t.string().optional(),
            "repoName": t.string().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanIn"] = t.struct(
        {"endTime": t.string().optional(), "startTime": t.string().optional()}
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"])
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn"
    ] = t.struct(
        {
            "bucket": t.string().optional(),
            "generation": t.string().optional(),
            "object": t.string().optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut"
    ] = t.struct(
        {
            "bucket": t.string().optional(),
            "generation": t.string().optional(),
            "object": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut"]
    )
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsIn"] = t.struct(
        {
            "pythonPackages": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageIn"
                    ]
                )
            ).optional(),
            "images": t.array(
                t.proxy(
                    renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageIn"]
                )
            ).optional(),
            "artifactManifest": t.string().optional(),
            "buildStepImages": t.array(t.string()).optional(),
            "buildStepOutputs": t.array(t.string()).optional(),
            "mavenArtifacts": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactIn"
                    ]
                )
            ).optional(),
            "numArtifacts": t.string().optional(),
            "artifactTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanIn"]
            ).optional(),
            "npmPackages": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut"] = t.struct(
        {
            "pythonPackages": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageOut"
                    ]
                )
            ).optional(),
            "images": t.array(
                t.proxy(
                    renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageOut"]
                )
            ).optional(),
            "artifactManifest": t.string().optional(),
            "buildStepImages": t.array(t.string()).optional(),
            "buildStepOutputs": t.array(t.string()).optional(),
            "mavenArtifacts": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactOut"
                    ]
                )
            ).optional(),
            "numArtifacts": t.string().optional(),
            "artifactTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "npmPackages": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn"] = t.struct(
        {
            "configSource": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn"]
            ),
            "parameters": t.struct({"_": t.string().optional()}),
            "environment": t.struct({"_": t.string().optional()}),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut"] = t.struct(
        {
            "configSource": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut"]
            ),
            "parameters": t.struct({"_": t.string().optional()}),
            "environment": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut"])
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
    types["MetadataIn"] = t.struct(
        {
            "buildFinishedOn": t.string().optional(),
            "buildStartedOn": t.string().optional(),
            "completeness": t.proxy(renames["CompletenessIn"]).optional(),
            "buildInvocationId": t.string().optional(),
            "reproducible": t.boolean().optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "buildFinishedOn": t.string().optional(),
            "buildStartedOn": t.string().optional(),
            "completeness": t.proxy(renames["CompletenessOut"]).optional(),
            "buildInvocationId": t.string().optional(),
            "reproducible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
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
    types["SlsaCompletenessIn"] = t.struct(
        {
            "materials": t.boolean().optional(),
            "arguments": t.boolean().optional(),
            "environment": t.boolean().optional(),
        }
    ).named(renames["SlsaCompletenessIn"])
    types["SlsaCompletenessOut"] = t.struct(
        {
            "materials": t.boolean().optional(),
            "arguments": t.boolean().optional(),
            "environment": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaCompletenessOut"])
    types["LocationIn"] = t.struct(
        {
            "path": t.string().optional(),
            "version": t.proxy(renames["VersionIn"]).optional(),
            "cpeUri": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "path": t.string().optional(),
            "version": t.proxy(renames["VersionOut"]).optional(),
            "cpeUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretIn"
    ] = t.struct(
        {"versionName": t.string().optional(), "env": t.string().optional()}
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretOut"
    ] = t.struct(
        {
            "versionName": t.string().optional(),
            "env": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretOut"]
    )
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
    types["SbomReferenceIntotoPayloadIn"] = t.struct(
        {
            "_type": t.string().optional(),
            "predicateType": t.string().optional(),
            "predicate": t.proxy(renames["SbomReferenceIntotoPredicateIn"]).optional(),
            "subject": t.array(t.proxy(renames["SubjectIn"])).optional(),
        }
    ).named(renames["SbomReferenceIntotoPayloadIn"])
    types["SbomReferenceIntotoPayloadOut"] = t.struct(
        {
            "_type": t.string().optional(),
            "predicateType": t.string().optional(),
            "predicate": t.proxy(renames["SbomReferenceIntotoPredicateOut"]).optional(),
            "subject": t.array(t.proxy(renames["SubjectOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SbomReferenceIntotoPayloadOut"])
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
            "pushTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "fileHashes": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesOut"]
            ).optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageOut"]
    )
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn"] = t.struct(
        {
            "dynamicSubstitutions": t.boolean().optional(),
            "volumes": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn"])
            ).optional(),
            "workerPool": t.string().optional(),
            "sourceProvenanceHash": t.array(t.string()).optional(),
            "logStreamingOption": t.string().optional(),
            "logging": t.string().optional(),
            "pool": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionIn"
                ]
            ).optional(),
            "machineType": t.string().optional(),
            "secretEnv": t.array(t.string()).optional(),
            "defaultLogsBucketBehavior": t.string().optional(),
            "requestedVerifyOption": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "diskSizeGb": t.string().optional(),
            "substitutionOption": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut"] = t.struct(
        {
            "dynamicSubstitutions": t.boolean().optional(),
            "volumes": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut"])
            ).optional(),
            "workerPool": t.string().optional(),
            "sourceProvenanceHash": t.array(t.string()).optional(),
            "logStreamingOption": t.string().optional(),
            "logging": t.string().optional(),
            "pool": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionOut"
                ]
            ).optional(),
            "machineType": t.string().optional(),
            "secretEnv": t.array(t.string()).optional(),
            "defaultLogsBucketBehavior": t.string().optional(),
            "requestedVerifyOption": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "diskSizeGb": t.string().optional(),
            "substitutionOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn"] = t.struct(
        {
            "object": t.string().optional(),
            "generation": t.string().optional(),
            "bucket": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut"] = t.struct(
        {
            "object": t.string().optional(),
            "generation": t.string().optional(),
            "bucket": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut"])
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
    types["NoteIn"] = t.struct(
        {
            "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
            "vulnerabilityAssessment": t.proxy(
                renames["VulnerabilityAssessmentNoteIn"]
            ).optional(),
            "expirationTime": t.string().optional(),
            "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
            "image": t.proxy(renames["ImageNoteIn"]).optional(),
            "createTime": t.string().optional(),
            "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
            "relatedNoteNames": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
            "shortDescription": t.string().optional(),
            "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
            "kind": t.string().optional(),
            "package": t.proxy(renames["PackageNoteIn"]).optional(),
            "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
            "build": t.proxy(renames["BuildNoteIn"]).optional(),
            "name": t.string().optional(),
            "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
            "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
            "longDescription": t.string().optional(),
        }
    ).named(renames["NoteIn"])
    types["NoteOut"] = t.struct(
        {
            "vulnerability": t.proxy(renames["VulnerabilityNoteOut"]).optional(),
            "vulnerabilityAssessment": t.proxy(
                renames["VulnerabilityAssessmentNoteOut"]
            ).optional(),
            "expirationTime": t.string().optional(),
            "deployment": t.proxy(renames["DeploymentNoteOut"]).optional(),
            "image": t.proxy(renames["ImageNoteOut"]).optional(),
            "createTime": t.string().optional(),
            "attestation": t.proxy(renames["AttestationNoteOut"]).optional(),
            "relatedNoteNames": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "upgrade": t.proxy(renames["UpgradeNoteOut"]).optional(),
            "shortDescription": t.string().optional(),
            "compliance": t.proxy(renames["ComplianceNoteOut"]).optional(),
            "kind": t.string().optional(),
            "package": t.proxy(renames["PackageNoteOut"]).optional(),
            "dsseAttestation": t.proxy(renames["DSSEAttestationNoteOut"]).optional(),
            "build": t.proxy(renames["BuildNoteOut"]).optional(),
            "name": t.string().optional(),
            "discovery": t.proxy(renames["DiscoveryNoteOut"]).optional(),
            "relatedUrl": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceNoteOut"]).optional(),
            "longDescription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoteOut"])
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
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageIn"
    ] = t.struct(
        {"repository": t.string().optional(), "paths": t.array(t.string()).optional()}
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageOut"
    ] = t.struct(
        {
            "repository": t.string().optional(),
            "paths": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageOut"]
    )
    types["AssessmentIn"] = t.struct(
        {
            "remediations": t.array(t.proxy(renames["RemediationIn"])).optional(),
            "shortDescription": t.string().optional(),
            "impacts": t.array(t.string()).optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "justification": t.proxy(renames["JustificationIn"]).optional(),
            "state": t.string().optional(),
            "cve": t.string().optional(),
            "longDescription": t.string().optional(),
        }
    ).named(renames["AssessmentIn"])
    types["AssessmentOut"] = t.struct(
        {
            "remediations": t.array(t.proxy(renames["RemediationOut"])).optional(),
            "shortDescription": t.string().optional(),
            "impacts": t.array(t.string()).optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "justification": t.proxy(renames["JustificationOut"]).optional(),
            "state": t.string().optional(),
            "cve": t.string().optional(),
            "longDescription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssessmentOut"])
    types["ProductIn"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "genericUri": t.string().optional(),
        }
    ).named(renames["ProductIn"])
    types["ProductOut"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "genericUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["BatchCreateOccurrencesResponseIn"] = t.struct(
        {"occurrences": t.array(t.proxy(renames["OccurrenceIn"])).optional()}
    ).named(renames["BatchCreateOccurrencesResponseIn"])
    types["BatchCreateOccurrencesResponseOut"] = t.struct(
        {
            "occurrences": t.array(t.proxy(renames["OccurrenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateOccurrencesResponseOut"])
    types["InTotoProvenanceIn"] = t.struct(
        {
            "materials": t.array(t.string()).optional(),
            "metadata": t.proxy(renames["MetadataIn"]),
            "builderConfig": t.proxy(renames["BuilderConfigIn"]).optional(),
            "recipe": t.proxy(renames["RecipeIn"]).optional(),
        }
    ).named(renames["InTotoProvenanceIn"])
    types["InTotoProvenanceOut"] = t.struct(
        {
            "materials": t.array(t.string()).optional(),
            "metadata": t.proxy(renames["MetadataOut"]),
            "builderConfig": t.proxy(renames["BuilderConfigOut"]).optional(),
            "recipe": t.proxy(renames["RecipeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InTotoProvenanceOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsIn"] = t.struct(
        {
            "mavenArtifacts": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactIn"
                    ]
                )
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
            "images": t.array(t.string()).optional(),
            "objects": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsIn"
                ]
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
            "images": t.array(t.string()).optional(),
            "objects": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOut"])
    types["BuildOccurrenceIn"] = t.struct(
        {
            "intotoProvenance": t.proxy(renames["InTotoProvenanceIn"]).optional(),
            "intotoStatement": t.proxy(renames["InTotoStatementIn"]).optional(),
            "provenance": t.proxy(renames["BuildProvenanceIn"]).optional(),
            "provenanceBytes": t.string().optional(),
        }
    ).named(renames["BuildOccurrenceIn"])
    types["BuildOccurrenceOut"] = t.struct(
        {
            "intotoProvenance": t.proxy(renames["InTotoProvenanceOut"]).optional(),
            "intotoStatement": t.proxy(renames["InTotoStatementOut"]).optional(),
            "provenance": t.proxy(renames["BuildProvenanceOut"]).optional(),
            "provenanceBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOccurrenceOut"])
    types["HintIn"] = t.struct({"humanReadableName": t.string()}).named(
        renames["HintIn"]
    )
    types["HintOut"] = t.struct(
        {
            "humanReadableName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HintOut"])
    types["DiscoveryOccurrenceIn"] = t.struct(
        {
            "analysisCompleted": t.proxy(renames["AnalysisCompletedIn"]),
            "analysisStatus": t.string().optional(),
            "lastScanTime": t.string().optional(),
            "analysisError": t.array(t.proxy(renames["StatusIn"])).optional(),
            "cpe": t.string().optional(),
            "analysisStatusError": t.proxy(renames["StatusIn"]).optional(),
            "continuousAnalysis": t.string().optional(),
        }
    ).named(renames["DiscoveryOccurrenceIn"])
    types["DiscoveryOccurrenceOut"] = t.struct(
        {
            "analysisCompleted": t.proxy(renames["AnalysisCompletedOut"]),
            "analysisStatus": t.string().optional(),
            "lastScanTime": t.string().optional(),
            "archiveTime": t.string().optional(),
            "analysisError": t.array(t.proxy(renames["StatusOut"])).optional(),
            "cpe": t.string().optional(),
            "analysisStatusError": t.proxy(renames["StatusOut"]).optional(),
            "continuousAnalysis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoveryOccurrenceOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigIn"] = t.struct(
        {"approvalRequired": t.boolean().optional()}
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigOut"] = t.struct(
        {
            "approvalRequired": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigOut"])
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
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactIn"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "repository": t.string().optional(),
            "artifactId": t.string().optional(),
            "path": t.string().optional(),
            "groupId": t.string().optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactOut"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "repository": t.string().optional(),
            "artifactId": t.string().optional(),
            "path": t.string().optional(),
            "groupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactOut"]
    )
    types["JwtIn"] = t.struct({"compactJwt": t.string().optional()}).named(
        renames["JwtIn"]
    )
    types["JwtOut"] = t.struct(
        {
            "compactJwt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["CommandIn"] = t.struct(
        {
            "env": t.array(t.string()).optional(),
            "dir": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "waitFor": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["CommandIn"])
    types["CommandOut"] = t.struct(
        {
            "env": t.array(t.string()).optional(),
            "dir": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "waitFor": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommandOut"])
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
    types["SlsaMetadataIn"] = t.struct(
        {
            "buildFinishedOn": t.string().optional(),
            "buildStartedOn": t.string().optional(),
            "reproducible": t.boolean().optional(),
            "buildInvocationId": t.string().optional(),
            "completeness": t.proxy(renames["SlsaCompletenessIn"]).optional(),
        }
    ).named(renames["SlsaMetadataIn"])
    types["SlsaMetadataOut"] = t.struct(
        {
            "buildFinishedOn": t.string().optional(),
            "buildStartedOn": t.string().optional(),
            "reproducible": t.boolean().optional(),
            "buildInvocationId": t.string().optional(),
            "completeness": t.proxy(renames["SlsaCompletenessOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaMetadataOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn"] = t.struct(
        {
            "env": t.array(t.string()).optional(),
            "volumes": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn"])
            ).optional(),
            "dir": t.string().optional(),
            "script": t.string().optional(),
            "allowFailure": t.boolean().optional(),
            "args": t.array(t.string()).optional(),
            "allowExitCodes": t.array(t.integer()).optional(),
            "entrypoint": t.string().optional(),
            "id": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "name": t.string(),
            "secretEnv": t.array(t.string()).optional(),
            "timeout": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut"] = t.struct(
        {
            "env": t.array(t.string()).optional(),
            "volumes": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut"])
            ).optional(),
            "dir": t.string().optional(),
            "timing": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "script": t.string().optional(),
            "allowFailure": t.boolean().optional(),
            "pullTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "args": t.array(t.string()).optional(),
            "allowExitCodes": t.array(t.integer()).optional(),
            "entrypoint": t.string().optional(),
            "id": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "name": t.string(),
            "secretEnv": t.array(t.string()).optional(),
            "exitCode": t.integer().optional(),
            "timeout": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut"])
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
            "fileHashes": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesOut"]
            ).optional(),
            "pushTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageOut"]
    )
    types["KnowledgeBaseIn"] = t.struct(
        {"url": t.string().optional(), "name": t.string().optional()}
    ).named(renames["KnowledgeBaseIn"])
    types["KnowledgeBaseOut"] = t.struct(
        {
            "url": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KnowledgeBaseOut"])
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
    types["SlsaProvenanceIn"] = t.struct(
        {
            "builder": t.proxy(renames["SlsaBuilderIn"]).optional(),
            "materials": t.array(t.proxy(renames["MaterialIn"])).optional(),
            "metadata": t.proxy(renames["SlsaMetadataIn"]),
            "recipe": t.proxy(renames["SlsaRecipeIn"]).optional(),
        }
    ).named(renames["SlsaProvenanceIn"])
    types["SlsaProvenanceOut"] = t.struct(
        {
            "builder": t.proxy(renames["SlsaBuilderOut"]).optional(),
            "materials": t.array(t.proxy(renames["MaterialOut"])).optional(),
            "metadata": t.proxy(renames["SlsaMetadataOut"]),
            "recipe": t.proxy(renames["SlsaRecipeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaProvenanceOut"])
    types["AnalysisCompletedIn"] = t.struct(
        {"analysisType": t.array(t.string())}
    ).named(renames["AnalysisCompletedIn"])
    types["AnalysisCompletedOut"] = t.struct(
        {
            "analysisType": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalysisCompletedOut"])
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
    types["DSSEAttestationNoteIn"] = t.struct(
        {"hint": t.proxy(renames["DSSEHintIn"]).optional()}
    ).named(renames["DSSEAttestationNoteIn"])
    types["DSSEAttestationNoteOut"] = t.struct(
        {
            "hint": t.proxy(renames["DSSEHintOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DSSEAttestationNoteOut"])
    types["BuilderConfigIn"] = t.struct({"id": t.string()}).named(
        renames["BuilderConfigIn"]
    )
    types["BuilderConfigOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BuilderConfigOut"])
    types["RepoIdIn"] = t.struct(
        {
            "projectRepoId": t.proxy(renames["ProjectRepoIdIn"]).optional(),
            "uid": t.string().optional(),
        }
    ).named(renames["RepoIdIn"])
    types["RepoIdOut"] = t.struct(
        {
            "projectRepoId": t.proxy(renames["ProjectRepoIdOut"]).optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepoIdOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildIn"] = t.struct(
        {
            "timeout": t.string().optional(),
            "steps": t.array(
                t.proxy(
                    renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn"]
                )
            ),
            "options": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn"]
            ).optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "secrets": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretIn"])
            ).optional(),
            "images": t.array(t.string()).optional(),
            "logsBucket": t.string().optional(),
            "availableSecrets": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsIn"]
            ).optional(),
            "artifacts": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsIn"]
            ).optional(),
            "tags": t.array(t.string()).optional(),
            "source": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceIn"]
            ).optional(),
            "queueTtl": t.string().optional(),
            "serviceAccount": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOut"] = t.struct(
        {
            "timing": t.struct({"_": t.string().optional()}).optional(),
            "warnings": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningOut"
                    ]
                )
            ).optional(),
            "failureInfo": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoOut"
                ]
            ).optional(),
            "timeout": t.string().optional(),
            "results": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut"]
            ).optional(),
            "buildTriggerId": t.string().optional(),
            "finishTime": t.string().optional(),
            "steps": t.array(
                t.proxy(
                    renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut"]
                )
            ),
            "logUrl": t.string().optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "options": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut"]
            ).optional(),
            "approval": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalOut"]
            ).optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "secrets": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretOut"])
            ).optional(),
            "name": t.string().optional(),
            "images": t.array(t.string()).optional(),
            "sourceProvenance": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut"
                ]
            ).optional(),
            "projectId": t.string().optional(),
            "createTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "logsBucket": t.string().optional(),
            "availableSecrets": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsOut"]
            ).optional(),
            "artifacts": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "source": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceOut"]
            ).optional(),
            "queueTtl": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOut"])
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
    types["SlsaProvenanceZeroTwoIn"] = t.struct(
        {
            "buildType": t.string(),
            "builder": t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"]),
            "buildConfig": t.struct({"_": t.string().optional()}),
            "invocation": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn"]
            ),
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
            "buildType": t.string(),
            "builder": t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"]),
            "buildConfig": t.struct({"_": t.string().optional()}),
            "invocation": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut"]
            ),
            "metadata": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"]
            ),
            "materials": t.array(
                t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaProvenanceZeroTwoOut"])
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
    types["VexAssessmentIn"] = t.struct(
        {
            "relatedUris": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "state": t.string().optional(),
            "cve": t.string().optional(),
            "justification": t.proxy(renames["JustificationIn"]).optional(),
            "remediations": t.array(t.proxy(renames["RemediationIn"])).optional(),
            "impacts": t.array(t.string()).optional(),
            "noteName": t.string().optional(),
        }
    ).named(renames["VexAssessmentIn"])
    types["VexAssessmentOut"] = t.struct(
        {
            "relatedUris": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "state": t.string().optional(),
            "cve": t.string().optional(),
            "justification": t.proxy(renames["JustificationOut"]).optional(),
            "remediations": t.array(t.proxy(renames["RemediationOut"])).optional(),
            "impacts": t.array(t.string()).optional(),
            "noteName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VexAssessmentOut"])
    types["DeploymentOccurrenceIn"] = t.struct(
        {
            "address": t.string().optional(),
            "deployTime": t.string(),
            "undeployTime": t.string().optional(),
            "config": t.string().optional(),
            "platform": t.string().optional(),
            "resourceUri": t.array(t.string()).optional(),
            "userEmail": t.string().optional(),
        }
    ).named(renames["DeploymentOccurrenceIn"])
    types["DeploymentOccurrenceOut"] = t.struct(
        {
            "address": t.string().optional(),
            "deployTime": t.string(),
            "undeployTime": t.string().optional(),
            "config": t.string().optional(),
            "platform": t.string().optional(),
            "resourceUri": t.array(t.string()).optional(),
            "userEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOccurrenceOut"])

    functions = {}
    functions["projectsNotesSetIamPolicy"] = containeranalysis.post(
        "v1/{parent}/notes",
        t.struct(
            {
                "noteId": t.string(),
                "parent": t.string(),
                "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
                "vulnerabilityAssessment": t.proxy(
                    renames["VulnerabilityAssessmentNoteIn"]
                ).optional(),
                "expirationTime": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
                "image": t.proxy(renames["ImageNoteIn"]).optional(),
                "createTime": t.string().optional(),
                "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
                "relatedNoteNames": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
                "shortDescription": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
                "kind": t.string().optional(),
                "package": t.proxy(renames["PackageNoteIn"]).optional(),
                "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
                "build": t.proxy(renames["BuildNoteIn"]).optional(),
                "name": t.string().optional(),
                "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
                "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
                "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
                "longDescription": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesGetIamPolicy"] = containeranalysis.post(
        "v1/{parent}/notes",
        t.struct(
            {
                "noteId": t.string(),
                "parent": t.string(),
                "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
                "vulnerabilityAssessment": t.proxy(
                    renames["VulnerabilityAssessmentNoteIn"]
                ).optional(),
                "expirationTime": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
                "image": t.proxy(renames["ImageNoteIn"]).optional(),
                "createTime": t.string().optional(),
                "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
                "relatedNoteNames": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
                "shortDescription": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
                "kind": t.string().optional(),
                "package": t.proxy(renames["PackageNoteIn"]).optional(),
                "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
                "build": t.proxy(renames["BuildNoteIn"]).optional(),
                "name": t.string().optional(),
                "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
                "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
                "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
                "longDescription": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesBatchCreate"] = containeranalysis.post(
        "v1/{parent}/notes",
        t.struct(
            {
                "noteId": t.string(),
                "parent": t.string(),
                "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
                "vulnerabilityAssessment": t.proxy(
                    renames["VulnerabilityAssessmentNoteIn"]
                ).optional(),
                "expirationTime": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
                "image": t.proxy(renames["ImageNoteIn"]).optional(),
                "createTime": t.string().optional(),
                "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
                "relatedNoteNames": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
                "shortDescription": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
                "kind": t.string().optional(),
                "package": t.proxy(renames["PackageNoteIn"]).optional(),
                "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
                "build": t.proxy(renames["BuildNoteIn"]).optional(),
                "name": t.string().optional(),
                "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
                "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
                "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
                "longDescription": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesList"] = containeranalysis.post(
        "v1/{parent}/notes",
        t.struct(
            {
                "noteId": t.string(),
                "parent": t.string(),
                "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
                "vulnerabilityAssessment": t.proxy(
                    renames["VulnerabilityAssessmentNoteIn"]
                ).optional(),
                "expirationTime": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
                "image": t.proxy(renames["ImageNoteIn"]).optional(),
                "createTime": t.string().optional(),
                "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
                "relatedNoteNames": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
                "shortDescription": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
                "kind": t.string().optional(),
                "package": t.proxy(renames["PackageNoteIn"]).optional(),
                "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
                "build": t.proxy(renames["BuildNoteIn"]).optional(),
                "name": t.string().optional(),
                "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
                "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
                "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
                "longDescription": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesGet"] = containeranalysis.post(
        "v1/{parent}/notes",
        t.struct(
            {
                "noteId": t.string(),
                "parent": t.string(),
                "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
                "vulnerabilityAssessment": t.proxy(
                    renames["VulnerabilityAssessmentNoteIn"]
                ).optional(),
                "expirationTime": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
                "image": t.proxy(renames["ImageNoteIn"]).optional(),
                "createTime": t.string().optional(),
                "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
                "relatedNoteNames": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
                "shortDescription": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
                "kind": t.string().optional(),
                "package": t.proxy(renames["PackageNoteIn"]).optional(),
                "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
                "build": t.proxy(renames["BuildNoteIn"]).optional(),
                "name": t.string().optional(),
                "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
                "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
                "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
                "longDescription": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesDelete"] = containeranalysis.post(
        "v1/{parent}/notes",
        t.struct(
            {
                "noteId": t.string(),
                "parent": t.string(),
                "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
                "vulnerabilityAssessment": t.proxy(
                    renames["VulnerabilityAssessmentNoteIn"]
                ).optional(),
                "expirationTime": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
                "image": t.proxy(renames["ImageNoteIn"]).optional(),
                "createTime": t.string().optional(),
                "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
                "relatedNoteNames": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
                "shortDescription": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
                "kind": t.string().optional(),
                "package": t.proxy(renames["PackageNoteIn"]).optional(),
                "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
                "build": t.proxy(renames["BuildNoteIn"]).optional(),
                "name": t.string().optional(),
                "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
                "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
                "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
                "longDescription": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesPatch"] = containeranalysis.post(
        "v1/{parent}/notes",
        t.struct(
            {
                "noteId": t.string(),
                "parent": t.string(),
                "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
                "vulnerabilityAssessment": t.proxy(
                    renames["VulnerabilityAssessmentNoteIn"]
                ).optional(),
                "expirationTime": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
                "image": t.proxy(renames["ImageNoteIn"]).optional(),
                "createTime": t.string().optional(),
                "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
                "relatedNoteNames": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
                "shortDescription": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
                "kind": t.string().optional(),
                "package": t.proxy(renames["PackageNoteIn"]).optional(),
                "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
                "build": t.proxy(renames["BuildNoteIn"]).optional(),
                "name": t.string().optional(),
                "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
                "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
                "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
                "longDescription": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesTestIamPermissions"] = containeranalysis.post(
        "v1/{parent}/notes",
        t.struct(
            {
                "noteId": t.string(),
                "parent": t.string(),
                "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
                "vulnerabilityAssessment": t.proxy(
                    renames["VulnerabilityAssessmentNoteIn"]
                ).optional(),
                "expirationTime": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
                "image": t.proxy(renames["ImageNoteIn"]).optional(),
                "createTime": t.string().optional(),
                "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
                "relatedNoteNames": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
                "shortDescription": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
                "kind": t.string().optional(),
                "package": t.proxy(renames["PackageNoteIn"]).optional(),
                "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
                "build": t.proxy(renames["BuildNoteIn"]).optional(),
                "name": t.string().optional(),
                "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
                "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
                "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
                "longDescription": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesCreate"] = containeranalysis.post(
        "v1/{parent}/notes",
        t.struct(
            {
                "noteId": t.string(),
                "parent": t.string(),
                "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
                "vulnerabilityAssessment": t.proxy(
                    renames["VulnerabilityAssessmentNoteIn"]
                ).optional(),
                "expirationTime": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
                "image": t.proxy(renames["ImageNoteIn"]).optional(),
                "createTime": t.string().optional(),
                "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
                "relatedNoteNames": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
                "shortDescription": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
                "kind": t.string().optional(),
                "package": t.proxy(renames["PackageNoteIn"]).optional(),
                "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
                "build": t.proxy(renames["BuildNoteIn"]).optional(),
                "name": t.string().optional(),
                "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
                "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
                "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
                "longDescription": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
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
        importer="containeranalysis", renames=renames, types=types, functions=functions
    )
