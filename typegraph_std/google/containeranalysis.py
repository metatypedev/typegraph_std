from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_containeranalysis() -> Import:
    containeranalysis = HTTPRuntime("https://containeranalysis.googleapis.com/")

    renames = {
        "ErrorResponse": "_containeranalysis_1_ErrorResponse",
        "TestIamPermissionsRequestIn": "_containeranalysis_2_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_containeranalysis_3_TestIamPermissionsRequestOut",
        "EnvelopeIn": "_containeranalysis_4_EnvelopeIn",
        "EnvelopeOut": "_containeranalysis_5_EnvelopeOut",
        "NoteIn": "_containeranalysis_6_NoteIn",
        "NoteOut": "_containeranalysis_7_NoteOut",
        "SourceContextIn": "_containeranalysis_8_SourceContextIn",
        "SourceContextOut": "_containeranalysis_9_SourceContextOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsIn": "_containeranalysis_10_ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut": "_containeranalysis_11_ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut",
        "AttestationOccurrenceIn": "_containeranalysis_12_AttestationOccurrenceIn",
        "AttestationOccurrenceOut": "_containeranalysis_13_AttestationOccurrenceOut",
        "FixableTotalByDigestIn": "_containeranalysis_14_FixableTotalByDigestIn",
        "FixableTotalByDigestOut": "_containeranalysis_15_FixableTotalByDigestOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigIn": "_containeranalysis_16_ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigOut": "_containeranalysis_17_ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageIn": "_containeranalysis_18_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageOut": "_containeranalysis_19_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageOut",
        "AliasContextIn": "_containeranalysis_20_AliasContextIn",
        "AliasContextOut": "_containeranalysis_21_AliasContextOut",
        "AttestationNoteIn": "_containeranalysis_22_AttestationNoteIn",
        "AttestationNoteOut": "_containeranalysis_23_AttestationNoteOut",
        "SlsaCompletenessIn": "_containeranalysis_24_SlsaCompletenessIn",
        "SlsaCompletenessOut": "_containeranalysis_25_SlsaCompletenessOut",
        "BuilderConfigIn": "_containeranalysis_26_BuilderConfigIn",
        "BuilderConfigOut": "_containeranalysis_27_BuilderConfigOut",
        "InTotoProvenanceIn": "_containeranalysis_28_InTotoProvenanceIn",
        "InTotoProvenanceOut": "_containeranalysis_29_InTotoProvenanceOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalIn": "_containeranalysis_30_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalOut": "_containeranalysis_31_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalOut",
        "OccurrenceIn": "_containeranalysis_32_OccurrenceIn",
        "OccurrenceOut": "_containeranalysis_33_OccurrenceOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn": "_containeranalysis_34_GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut": "_containeranalysis_35_GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut",
        "ListNotesResponseIn": "_containeranalysis_36_ListNotesResponseIn",
        "ListNotesResponseOut": "_containeranalysis_37_ListNotesResponseOut",
        "CompletenessIn": "_containeranalysis_38_CompletenessIn",
        "CompletenessOut": "_containeranalysis_39_CompletenessOut",
        "CloudRepoSourceContextIn": "_containeranalysis_40_CloudRepoSourceContextIn",
        "CloudRepoSourceContextOut": "_containeranalysis_41_CloudRepoSourceContextOut",
        "RelatedUrlIn": "_containeranalysis_42_RelatedUrlIn",
        "RelatedUrlOut": "_containeranalysis_43_RelatedUrlOut",
        "BuildOccurrenceIn": "_containeranalysis_44_BuildOccurrenceIn",
        "BuildOccurrenceOut": "_containeranalysis_45_BuildOccurrenceOut",
        "SlsaProvenanceIn": "_containeranalysis_46_SlsaProvenanceIn",
        "SlsaProvenanceOut": "_containeranalysis_47_SlsaProvenanceOut",
        "SignatureIn": "_containeranalysis_48_SignatureIn",
        "SignatureOut": "_containeranalysis_49_SignatureOut",
        "BuildStepIn": "_containeranalysis_50_BuildStepIn",
        "BuildStepOut": "_containeranalysis_51_BuildStepOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn": "_containeranalysis_52_GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut": "_containeranalysis_53_GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut",
        "GetPolicyOptionsIn": "_containeranalysis_54_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_containeranalysis_55_GetPolicyOptionsOut",
        "BuildNoteIn": "_containeranalysis_56_BuildNoteIn",
        "BuildNoteOut": "_containeranalysis_57_BuildNoteOut",
        "CommandIn": "_containeranalysis_58_CommandIn",
        "CommandOut": "_containeranalysis_59_CommandOut",
        "SlsaRecipeIn": "_containeranalysis_60_SlsaRecipeIn",
        "SlsaRecipeOut": "_containeranalysis_61_SlsaRecipeOut",
        "GetIamPolicyRequestIn": "_containeranalysis_62_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_containeranalysis_63_GetIamPolicyRequestOut",
        "AnalysisCompletedIn": "_containeranalysis_64_AnalysisCompletedIn",
        "AnalysisCompletedOut": "_containeranalysis_65_AnalysisCompletedOut",
        "FileHashesIn": "_containeranalysis_66_FileHashesIn",
        "FileHashesOut": "_containeranalysis_67_FileHashesOut",
        "LocationIn": "_containeranalysis_68_LocationIn",
        "LocationOut": "_containeranalysis_69_LocationOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceIn": "_containeranalysis_70_ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut": "_containeranalysis_71_ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut",
        "GrafeasV1FileLocationIn": "_containeranalysis_72_GrafeasV1FileLocationIn",
        "GrafeasV1FileLocationOut": "_containeranalysis_73_GrafeasV1FileLocationOut",
        "VulnerabilityOccurrenceIn": "_containeranalysis_74_VulnerabilityOccurrenceIn",
        "VulnerabilityOccurrenceOut": "_containeranalysis_75_VulnerabilityOccurrenceOut",
        "ArtifactIn": "_containeranalysis_76_ArtifactIn",
        "ArtifactOut": "_containeranalysis_77_ArtifactOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultIn": "_containeranalysis_78_ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultOut": "_containeranalysis_79_ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanIn": "_containeranalysis_80_ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut": "_containeranalysis_81_ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsIn": "_containeranalysis_82_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsOut": "_containeranalysis_83_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsOut",
        "CategoryIn": "_containeranalysis_84_CategoryIn",
        "CategoryOut": "_containeranalysis_85_CategoryOut",
        "RecipeIn": "_containeranalysis_86_RecipeIn",
        "RecipeOut": "_containeranalysis_87_RecipeOut",
        "SlsaBuilderIn": "_containeranalysis_88_SlsaBuilderIn",
        "SlsaBuilderOut": "_containeranalysis_89_SlsaBuilderOut",
        "UpgradeDistributionIn": "_containeranalysis_90_UpgradeDistributionIn",
        "UpgradeDistributionOut": "_containeranalysis_91_UpgradeDistributionOut",
        "DeploymentOccurrenceIn": "_containeranalysis_92_DeploymentOccurrenceIn",
        "DeploymentOccurrenceOut": "_containeranalysis_93_DeploymentOccurrenceOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn": "_containeranalysis_94_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut": "_containeranalysis_95_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut",
        "ImageOccurrenceIn": "_containeranalysis_96_ImageOccurrenceIn",
        "ImageOccurrenceOut": "_containeranalysis_97_ImageOccurrenceOut",
        "ProjectRepoIdIn": "_containeranalysis_98_ProjectRepoIdIn",
        "ProjectRepoIdOut": "_containeranalysis_99_ProjectRepoIdOut",
        "VexAssessmentIn": "_containeranalysis_100_VexAssessmentIn",
        "VexAssessmentOut": "_containeranalysis_101_VexAssessmentOut",
        "NonCompliantFileIn": "_containeranalysis_102_NonCompliantFileIn",
        "NonCompliantFileOut": "_containeranalysis_103_NonCompliantFileOut",
        "DiscoveryNoteIn": "_containeranalysis_104_DiscoveryNoteIn",
        "DiscoveryNoteOut": "_containeranalysis_105_DiscoveryNoteOut",
        "VulnerabilityAssessmentNoteIn": "_containeranalysis_106_VulnerabilityAssessmentNoteIn",
        "VulnerabilityAssessmentNoteOut": "_containeranalysis_107_VulnerabilityAssessmentNoteOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoIn": "_containeranalysis_108_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoOut": "_containeranalysis_109_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoOut",
        "GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataIn": "_containeranalysis_110_GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataIn",
        "GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataOut": "_containeranalysis_111_GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsIn": "_containeranalysis_112_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsOut": "_containeranalysis_113_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsOut",
        "PublisherIn": "_containeranalysis_114_PublisherIn",
        "PublisherOut": "_containeranalysis_115_PublisherOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretIn": "_containeranalysis_116_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretOut": "_containeranalysis_117_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretOut",
        "FingerprintIn": "_containeranalysis_118_FingerprintIn",
        "FingerprintOut": "_containeranalysis_119_FingerprintOut",
        "VulnerabilityNoteIn": "_containeranalysis_120_VulnerabilityNoteIn",
        "VulnerabilityNoteOut": "_containeranalysis_121_VulnerabilityNoteOut",
        "StatusIn": "_containeranalysis_122_StatusIn",
        "StatusOut": "_containeranalysis_123_StatusOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceIn": "_containeranalysis_124_ContaineranalysisGoogleDevtoolsCloudbuildV1SourceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceOut": "_containeranalysis_125_ContaineranalysisGoogleDevtoolsCloudbuildV1SourceOut",
        "BatchCreateOccurrencesResponseIn": "_containeranalysis_126_BatchCreateOccurrencesResponseIn",
        "BatchCreateOccurrencesResponseOut": "_containeranalysis_127_BatchCreateOccurrencesResponseOut",
        "TestIamPermissionsResponseIn": "_containeranalysis_128_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_containeranalysis_129_TestIamPermissionsResponseOut",
        "ComplianceVersionIn": "_containeranalysis_130_ComplianceVersionIn",
        "ComplianceVersionOut": "_containeranalysis_131_ComplianceVersionOut",
        "WindowsDetailIn": "_containeranalysis_132_WindowsDetailIn",
        "WindowsDetailOut": "_containeranalysis_133_WindowsDetailOut",
        "VulnerabilityOccurrencesSummaryIn": "_containeranalysis_134_VulnerabilityOccurrencesSummaryIn",
        "VulnerabilityOccurrencesSummaryOut": "_containeranalysis_135_VulnerabilityOccurrencesSummaryOut",
        "SetIamPolicyRequestIn": "_containeranalysis_136_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_containeranalysis_137_SetIamPolicyRequestOut",
        "WindowsUpdateIn": "_containeranalysis_138_WindowsUpdateIn",
        "WindowsUpdateOut": "_containeranalysis_139_WindowsUpdateOut",
        "SbomReferenceIntotoPredicateIn": "_containeranalysis_140_SbomReferenceIntotoPredicateIn",
        "SbomReferenceIntotoPredicateOut": "_containeranalysis_141_SbomReferenceIntotoPredicateOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactIn": "_containeranalysis_142_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactOut": "_containeranalysis_143_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactOut",
        "HintIn": "_containeranalysis_144_HintIn",
        "HintOut": "_containeranalysis_145_HintOut",
        "SBOMReferenceNoteIn": "_containeranalysis_146_SBOMReferenceNoteIn",
        "SBOMReferenceNoteOut": "_containeranalysis_147_SBOMReferenceNoteOut",
        "IdentityIn": "_containeranalysis_148_IdentityIn",
        "IdentityOut": "_containeranalysis_149_IdentityOut",
        "HashIn": "_containeranalysis_150_HashIn",
        "HashOut": "_containeranalysis_151_HashOut",
        "TimeSpanIn": "_containeranalysis_152_TimeSpanIn",
        "TimeSpanOut": "_containeranalysis_153_TimeSpanOut",
        "EmptyIn": "_containeranalysis_154_EmptyIn",
        "EmptyOut": "_containeranalysis_155_EmptyOut",
        "SBOMReferenceOccurrenceIn": "_containeranalysis_156_SBOMReferenceOccurrenceIn",
        "SBOMReferenceOccurrenceOut": "_containeranalysis_157_SBOMReferenceOccurrenceOut",
        "PolicyIn": "_containeranalysis_158_PolicyIn",
        "PolicyOut": "_containeranalysis_159_PolicyOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn": "_containeranalysis_160_ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut": "_containeranalysis_161_ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut",
        "DSSEAttestationNoteIn": "_containeranalysis_162_DSSEAttestationNoteIn",
        "DSSEAttestationNoteOut": "_containeranalysis_163_DSSEAttestationNoteOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageIn": "_containeranalysis_164_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageOut": "_containeranalysis_165_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageOut",
        "ComplianceNoteIn": "_containeranalysis_166_ComplianceNoteIn",
        "ComplianceNoteOut": "_containeranalysis_167_ComplianceNoteOut",
        "DigestIn": "_containeranalysis_168_DigestIn",
        "DigestOut": "_containeranalysis_169_DigestOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn": "_containeranalysis_170_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut": "_containeranalysis_171_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut",
        "MetadataIn": "_containeranalysis_172_MetadataIn",
        "MetadataOut": "_containeranalysis_173_MetadataOut",
        "MaterialIn": "_containeranalysis_174_MaterialIn",
        "MaterialOut": "_containeranalysis_175_MaterialOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn": "_containeranalysis_176_GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut": "_containeranalysis_177_GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut",
        "DSSEHintIn": "_containeranalysis_178_DSSEHintIn",
        "DSSEHintOut": "_containeranalysis_179_DSSEHintOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn": "_containeranalysis_180_ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut": "_containeranalysis_181_ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut",
        "CisBenchmarkIn": "_containeranalysis_182_CisBenchmarkIn",
        "CisBenchmarkOut": "_containeranalysis_183_CisBenchmarkOut",
        "BindingIn": "_containeranalysis_184_BindingIn",
        "BindingOut": "_containeranalysis_185_BindingOut",
        "CVSSv3In": "_containeranalysis_186_CVSSv3In",
        "CVSSv3Out": "_containeranalysis_187_CVSSv3Out",
        "GerritSourceContextIn": "_containeranalysis_188_GerritSourceContextIn",
        "GerritSourceContextOut": "_containeranalysis_189_GerritSourceContextOut",
        "VolumeIn": "_containeranalysis_190_VolumeIn",
        "VolumeOut": "_containeranalysis_191_VolumeOut",
        "EnvelopeSignatureIn": "_containeranalysis_192_EnvelopeSignatureIn",
        "EnvelopeSignatureOut": "_containeranalysis_193_EnvelopeSignatureOut",
        "DSSEAttestationOccurrenceIn": "_containeranalysis_194_DSSEAttestationOccurrenceIn",
        "DSSEAttestationOccurrenceOut": "_containeranalysis_195_DSSEAttestationOccurrenceOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningIn": "_containeranalysis_196_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningOut": "_containeranalysis_197_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1HashIn": "_containeranalysis_198_ContaineranalysisGoogleDevtoolsCloudbuildV1HashIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1HashOut": "_containeranalysis_199_ContaineranalysisGoogleDevtoolsCloudbuildV1HashOut",
        "PackageNoteIn": "_containeranalysis_200_PackageNoteIn",
        "PackageNoteOut": "_containeranalysis_201_PackageNoteOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn": "_containeranalysis_202_ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut": "_containeranalysis_203_ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut",
        "SourceIn": "_containeranalysis_204_SourceIn",
        "SourceOut": "_containeranalysis_205_SourceOut",
        "DiscoveryOccurrenceIn": "_containeranalysis_206_DiscoveryOccurrenceIn",
        "DiscoveryOccurrenceOut": "_containeranalysis_207_DiscoveryOccurrenceOut",
        "BatchCreateNotesRequestIn": "_containeranalysis_208_BatchCreateNotesRequestIn",
        "BatchCreateNotesRequestOut": "_containeranalysis_209_BatchCreateNotesRequestOut",
        "RepoIdIn": "_containeranalysis_210_RepoIdIn",
        "RepoIdOut": "_containeranalysis_211_RepoIdOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionIn": "_containeranalysis_212_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionOut": "_containeranalysis_213_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionOut",
        "SbomReferenceIntotoPayloadIn": "_containeranalysis_214_SbomReferenceIntotoPayloadIn",
        "SbomReferenceIntotoPayloadOut": "_containeranalysis_215_SbomReferenceIntotoPayloadOut",
        "BuildProvenanceIn": "_containeranalysis_216_BuildProvenanceIn",
        "BuildProvenanceOut": "_containeranalysis_217_BuildProvenanceOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn": "_containeranalysis_218_ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut": "_containeranalysis_219_ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn": "_containeranalysis_220_GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut": "_containeranalysis_221_GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretIn": "_containeranalysis_222_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretOut": "_containeranalysis_223_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretOut",
        "ImageNoteIn": "_containeranalysis_224_ImageNoteIn",
        "ImageNoteOut": "_containeranalysis_225_ImageNoteOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesIn": "_containeranalysis_226_ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesOut": "_containeranalysis_227_ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesOut",
        "SubjectIn": "_containeranalysis_228_SubjectIn",
        "SubjectOut": "_containeranalysis_229_SubjectOut",
        "ExprIn": "_containeranalysis_230_ExprIn",
        "ExprOut": "_containeranalysis_231_ExprOut",
        "PackageIssueIn": "_containeranalysis_232_PackageIssueIn",
        "PackageIssueOut": "_containeranalysis_233_PackageIssueOut",
        "CVSSIn": "_containeranalysis_234_CVSSIn",
        "CVSSOut": "_containeranalysis_235_CVSSOut",
        "UpgradeNoteIn": "_containeranalysis_236_UpgradeNoteIn",
        "UpgradeNoteOut": "_containeranalysis_237_UpgradeNoteOut",
        "JwtIn": "_containeranalysis_238_JwtIn",
        "JwtOut": "_containeranalysis_239_JwtOut",
        "ListNoteOccurrencesResponseIn": "_containeranalysis_240_ListNoteOccurrencesResponseIn",
        "ListNoteOccurrencesResponseOut": "_containeranalysis_241_ListNoteOccurrencesResponseOut",
        "UpgradeOccurrenceIn": "_containeranalysis_242_UpgradeOccurrenceIn",
        "UpgradeOccurrenceOut": "_containeranalysis_243_UpgradeOccurrenceOut",
        "ProductIn": "_containeranalysis_244_ProductIn",
        "ProductOut": "_containeranalysis_245_ProductOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn": "_containeranalysis_246_GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut": "_containeranalysis_247_GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn": "_containeranalysis_248_GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut": "_containeranalysis_249_GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceIn": "_containeranalysis_250_ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut": "_containeranalysis_251_ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsIn": "_containeranalysis_252_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOut": "_containeranalysis_253_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOut",
        "ComplianceOccurrenceIn": "_containeranalysis_254_ComplianceOccurrenceIn",
        "ComplianceOccurrenceOut": "_containeranalysis_255_ComplianceOccurrenceOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactIn": "_containeranalysis_256_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactOut": "_containeranalysis_257_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactOut",
        "JustificationIn": "_containeranalysis_258_JustificationIn",
        "JustificationOut": "_containeranalysis_259_JustificationOut",
        "GitSourceContextIn": "_containeranalysis_260_GitSourceContextIn",
        "GitSourceContextOut": "_containeranalysis_261_GitSourceContextOut",
        "DeploymentNoteIn": "_containeranalysis_262_DeploymentNoteIn",
        "DeploymentNoteOut": "_containeranalysis_263_DeploymentNoteOut",
        "InTotoStatementIn": "_containeranalysis_264_InTotoStatementIn",
        "InTotoStatementOut": "_containeranalysis_265_InTotoStatementOut",
        "SlsaMetadataIn": "_containeranalysis_266_SlsaMetadataIn",
        "SlsaMetadataOut": "_containeranalysis_267_SlsaMetadataOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageIn": "_containeranalysis_268_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageOut": "_containeranalysis_269_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageOut",
        "LayerIn": "_containeranalysis_270_LayerIn",
        "LayerOut": "_containeranalysis_271_LayerOut",
        "VersionIn": "_containeranalysis_272_VersionIn",
        "VersionOut": "_containeranalysis_273_VersionOut",
        "DetailIn": "_containeranalysis_274_DetailIn",
        "DetailOut": "_containeranalysis_275_DetailOut",
        "SlsaProvenanceZeroTwoIn": "_containeranalysis_276_SlsaProvenanceZeroTwoIn",
        "SlsaProvenanceZeroTwoOut": "_containeranalysis_277_SlsaProvenanceZeroTwoOut",
        "LicenseIn": "_containeranalysis_278_LicenseIn",
        "LicenseOut": "_containeranalysis_279_LicenseOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildIn": "_containeranalysis_280_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOut": "_containeranalysis_281_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOut",
        "ListOccurrencesResponseIn": "_containeranalysis_282_ListOccurrencesResponseIn",
        "ListOccurrencesResponseOut": "_containeranalysis_283_ListOccurrencesResponseOut",
        "AssessmentIn": "_containeranalysis_284_AssessmentIn",
        "AssessmentOut": "_containeranalysis_285_AssessmentOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageIn": "_containeranalysis_286_ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageOut": "_containeranalysis_287_ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageOut",
        "BatchCreateNotesResponseIn": "_containeranalysis_288_BatchCreateNotesResponseIn",
        "BatchCreateNotesResponseOut": "_containeranalysis_289_BatchCreateNotesResponseOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretIn": "_containeranalysis_290_ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretOut": "_containeranalysis_291_ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretOut",
        "RemediationIn": "_containeranalysis_292_RemediationIn",
        "RemediationOut": "_containeranalysis_293_RemediationOut",
        "PackageOccurrenceIn": "_containeranalysis_294_PackageOccurrenceIn",
        "PackageOccurrenceOut": "_containeranalysis_295_PackageOccurrenceOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageIn": "_containeranalysis_296_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageOut": "_containeranalysis_297_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageOut",
        "KnowledgeBaseIn": "_containeranalysis_298_KnowledgeBaseIn",
        "KnowledgeBaseOut": "_containeranalysis_299_KnowledgeBaseOut",
        "BatchCreateOccurrencesRequestIn": "_containeranalysis_300_BatchCreateOccurrencesRequestIn",
        "BatchCreateOccurrencesRequestOut": "_containeranalysis_301_BatchCreateOccurrencesRequestOut",
        "DistributionIn": "_containeranalysis_302_DistributionIn",
        "DistributionOut": "_containeranalysis_303_DistributionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["NoteIn"] = t.struct(
        {
            "build": t.proxy(renames["BuildNoteIn"]).optional(),
            "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
            "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
            "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "package": t.proxy(renames["PackageNoteIn"]).optional(),
            "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
            "kind": t.string().optional(),
            "shortDescription": t.string().optional(),
            "longDescription": t.string().optional(),
            "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
            "updateTime": t.string().optional(),
            "image": t.proxy(renames["ImageNoteIn"]).optional(),
            "name": t.string().optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
            "expirationTime": t.string().optional(),
            "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
            "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
            "createTime": t.string().optional(),
            "relatedNoteNames": t.array(t.string()).optional(),
            "vulnerabilityAssessment": t.proxy(
                renames["VulnerabilityAssessmentNoteIn"]
            ).optional(),
            "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
        }
    ).named(renames["NoteIn"])
    types["NoteOut"] = t.struct(
        {
            "build": t.proxy(renames["BuildNoteOut"]).optional(),
            "vulnerability": t.proxy(renames["VulnerabilityNoteOut"]).optional(),
            "discovery": t.proxy(renames["DiscoveryNoteOut"]).optional(),
            "relatedUrl": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "package": t.proxy(renames["PackageNoteOut"]).optional(),
            "upgrade": t.proxy(renames["UpgradeNoteOut"]).optional(),
            "kind": t.string().optional(),
            "shortDescription": t.string().optional(),
            "longDescription": t.string().optional(),
            "attestation": t.proxy(renames["AttestationNoteOut"]).optional(),
            "updateTime": t.string().optional(),
            "image": t.proxy(renames["ImageNoteOut"]).optional(),
            "name": t.string().optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceNoteOut"]).optional(),
            "expirationTime": t.string().optional(),
            "compliance": t.proxy(renames["ComplianceNoteOut"]).optional(),
            "deployment": t.proxy(renames["DeploymentNoteOut"]).optional(),
            "createTime": t.string().optional(),
            "relatedNoteNames": t.array(t.string()).optional(),
            "vulnerabilityAssessment": t.proxy(
                renames["VulnerabilityAssessmentNoteOut"]
            ).optional(),
            "dsseAttestation": t.proxy(renames["DSSEAttestationNoteOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoteOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsIn"] = t.struct(
        {
            "pythonPackages": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageIn"
                    ]
                )
            ).optional(),
            "buildStepOutputs": t.array(t.string()).optional(),
            "images": t.array(
                t.proxy(
                    renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageIn"]
                )
            ).optional(),
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
            "numArtifacts": t.string().optional(),
            "mavenArtifacts": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactIn"
                    ]
                )
            ).optional(),
            "buildStepImages": t.array(t.string()).optional(),
            "artifactManifest": t.string().optional(),
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
            "buildStepOutputs": t.array(t.string()).optional(),
            "images": t.array(
                t.proxy(
                    renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageOut"]
                )
            ).optional(),
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
            "numArtifacts": t.string().optional(),
            "mavenArtifacts": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactOut"
                    ]
                )
            ).optional(),
            "buildStepImages": t.array(t.string()).optional(),
            "artifactManifest": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut"])
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
    types["FixableTotalByDigestIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "totalCount": t.string().optional(),
            "fixableCount": t.string().optional(),
            "resourceUri": t.string().optional(),
        }
    ).named(renames["FixableTotalByDigestIn"])
    types["FixableTotalByDigestOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "totalCount": t.string().optional(),
            "fixableCount": t.string().optional(),
            "resourceUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FixableTotalByDigestOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigIn"] = t.struct(
        {"approvalRequired": t.boolean().optional()}
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigOut"] = t.struct(
        {
            "approvalRequired": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigOut"])
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
    types["AttestationNoteIn"] = t.struct(
        {"hint": t.proxy(renames["HintIn"]).optional()}
    ).named(renames["AttestationNoteIn"])
    types["AttestationNoteOut"] = t.struct(
        {
            "hint": t.proxy(renames["HintOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestationNoteOut"])
    types["SlsaCompletenessIn"] = t.struct(
        {
            "arguments": t.boolean().optional(),
            "environment": t.boolean().optional(),
            "materials": t.boolean().optional(),
        }
    ).named(renames["SlsaCompletenessIn"])
    types["SlsaCompletenessOut"] = t.struct(
        {
            "arguments": t.boolean().optional(),
            "environment": t.boolean().optional(),
            "materials": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaCompletenessOut"])
    types["BuilderConfigIn"] = t.struct({"id": t.string()}).named(
        renames["BuilderConfigIn"]
    )
    types["BuilderConfigOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BuilderConfigOut"])
    types["InTotoProvenanceIn"] = t.struct(
        {
            "builderConfig": t.proxy(renames["BuilderConfigIn"]).optional(),
            "metadata": t.proxy(renames["MetadataIn"]),
            "materials": t.array(t.string()).optional(),
            "recipe": t.proxy(renames["RecipeIn"]).optional(),
        }
    ).named(renames["InTotoProvenanceIn"])
    types["InTotoProvenanceOut"] = t.struct(
        {
            "builderConfig": t.proxy(renames["BuilderConfigOut"]).optional(),
            "metadata": t.proxy(renames["MetadataOut"]),
            "materials": t.array(t.string()).optional(),
            "recipe": t.proxy(renames["RecipeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InTotoProvenanceOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalOut"] = t.struct(
        {
            "result": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultOut"]
            ).optional(),
            "config": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigOut"]
            ).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalOut"])
    types["OccurrenceIn"] = t.struct(
        {
            "resourceUri": t.string(),
            "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceOccurrenceIn"]).optional(),
            "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
            "kind": t.string().optional(),
            "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
            "noteName": t.string(),
            "vulnerability": t.proxy(renames["VulnerabilityOccurrenceIn"]).optional(),
            "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
            "updateTime": t.string().optional(),
            "remediation": t.string().optional(),
            "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
            "dsseAttestation": t.proxy(
                renames["DSSEAttestationOccurrenceIn"]
            ).optional(),
            "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
            "createTime": t.string().optional(),
            "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
            "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
            "name": t.string().optional(),
            "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
        }
    ).named(renames["OccurrenceIn"])
    types["OccurrenceOut"] = t.struct(
        {
            "resourceUri": t.string(),
            "deployment": t.proxy(renames["DeploymentOccurrenceOut"]).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceOccurrenceOut"]).optional(),
            "attestation": t.proxy(renames["AttestationOccurrenceOut"]).optional(),
            "kind": t.string().optional(),
            "upgrade": t.proxy(renames["UpgradeOccurrenceOut"]).optional(),
            "noteName": t.string(),
            "vulnerability": t.proxy(renames["VulnerabilityOccurrenceOut"]).optional(),
            "discovery": t.proxy(renames["DiscoveryOccurrenceOut"]).optional(),
            "updateTime": t.string().optional(),
            "remediation": t.string().optional(),
            "envelope": t.proxy(renames["EnvelopeOut"]).optional(),
            "dsseAttestation": t.proxy(
                renames["DSSEAttestationOccurrenceOut"]
            ).optional(),
            "package": t.proxy(renames["PackageOccurrenceOut"]).optional(),
            "createTime": t.string().optional(),
            "image": t.proxy(renames["ImageOccurrenceOut"]).optional(),
            "build": t.proxy(renames["BuildOccurrenceOut"]).optional(),
            "name": t.string().optional(),
            "compliance": t.proxy(renames["ComplianceOccurrenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OccurrenceOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"] = t.struct(
        {
            "parameters": t.boolean(),
            "materials": t.boolean(),
            "environment": t.boolean(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"] = t.struct(
        {
            "parameters": t.boolean(),
            "materials": t.boolean(),
            "environment": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"])
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
    types["CompletenessIn"] = t.struct(
        {
            "environment": t.boolean().optional(),
            "arguments": t.boolean().optional(),
            "materials": t.boolean().optional(),
        }
    ).named(renames["CompletenessIn"])
    types["CompletenessOut"] = t.struct(
        {
            "environment": t.boolean().optional(),
            "arguments": t.boolean().optional(),
            "materials": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompletenessOut"])
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
    types["BuildStepIn"] = t.struct(
        {
            "dir": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "exitCode": t.integer().optional(),
            "allowFailure": t.boolean().optional(),
            "id": t.string().optional(),
            "timing": t.proxy(renames["TimeSpanIn"]).optional(),
            "secretEnv": t.array(t.string()).optional(),
            "entrypoint": t.string().optional(),
            "timeout": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "waitFor": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "script": t.string().optional(),
            "pullTiming": t.proxy(renames["TimeSpanIn"]).optional(),
            "allowExitCodes": t.array(t.integer()).optional(),
        }
    ).named(renames["BuildStepIn"])
    types["BuildStepOut"] = t.struct(
        {
            "dir": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "exitCode": t.integer().optional(),
            "allowFailure": t.boolean().optional(),
            "id": t.string().optional(),
            "timing": t.proxy(renames["TimeSpanOut"]).optional(),
            "secretEnv": t.array(t.string()).optional(),
            "entrypoint": t.string().optional(),
            "timeout": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "waitFor": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "script": t.string().optional(),
            "pullTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "allowExitCodes": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildStepOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"] = t.struct(
        {"id": t.string()}
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["BuildNoteIn"] = t.struct({"builderVersion": t.string()}).named(
        renames["BuildNoteIn"]
    )
    types["BuildNoteOut"] = t.struct(
        {
            "builderVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildNoteOut"])
    types["CommandIn"] = t.struct(
        {
            "env": t.array(t.string()).optional(),
            "waitFor": t.array(t.string()).optional(),
            "dir": t.string().optional(),
            "name": t.string(),
            "id": t.string().optional(),
            "args": t.array(t.string()).optional(),
        }
    ).named(renames["CommandIn"])
    types["CommandOut"] = t.struct(
        {
            "env": t.array(t.string()).optional(),
            "waitFor": t.array(t.string()).optional(),
            "dir": t.string().optional(),
            "name": t.string(),
            "id": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommandOut"])
    types["SlsaRecipeIn"] = t.struct(
        {
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "arguments": t.struct({"_": t.string().optional()}).optional(),
            "definedInMaterial": t.string().optional(),
            "type": t.string().optional(),
            "entryPoint": t.string().optional(),
        }
    ).named(renames["SlsaRecipeIn"])
    types["SlsaRecipeOut"] = t.struct(
        {
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "arguments": t.struct({"_": t.string().optional()}).optional(),
            "definedInMaterial": t.string().optional(),
            "type": t.string().optional(),
            "entryPoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaRecipeOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["AnalysisCompletedIn"] = t.struct(
        {"analysisType": t.array(t.string())}
    ).named(renames["AnalysisCompletedIn"])
    types["AnalysisCompletedOut"] = t.struct(
        {
            "analysisType": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalysisCompletedOut"])
    types["FileHashesIn"] = t.struct(
        {"fileHash": t.array(t.proxy(renames["HashIn"]))}
    ).named(renames["FileHashesIn"])
    types["FileHashesOut"] = t.struct(
        {
            "fileHash": t.array(t.proxy(renames["HashOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileHashesOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceIn"] = t.struct(
        {
            "resolvedStorageSourceManifest": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn"
                ]
            ).optional(),
            "resolvedStorageSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn"]
            ).optional(),
            "resolvedRepoSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn"]
            ).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut"] = t.struct(
        {
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "resolvedStorageSourceManifest": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut"
                ]
            ).optional(),
            "resolvedStorageSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut"]
            ).optional(),
            "resolvedRepoSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut"])
    types["GrafeasV1FileLocationIn"] = t.struct(
        {"filePath": t.string().optional()}
    ).named(renames["GrafeasV1FileLocationIn"])
    types["GrafeasV1FileLocationOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1FileLocationOut"])
    types["VulnerabilityOccurrenceIn"] = t.struct(
        {
            "fixAvailable": t.boolean().optional(),
            "relatedUrls": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "vexAssessment": t.proxy(renames["VexAssessmentIn"]),
            "type": t.string().optional(),
            "effectiveSeverity": t.string().optional(),
            "severity": t.string().optional(),
            "cvssV2": t.proxy(renames["CVSSIn"]).optional(),
            "packageIssue": t.array(t.proxy(renames["PackageIssueIn"])),
            "cvssScore": t.number().optional(),
            "cvssv3": t.proxy(renames["CVSSIn"]).optional(),
            "longDescription": t.string().optional(),
            "cvssVersion": t.string().optional(),
            "shortDescription": t.string().optional(),
        }
    ).named(renames["VulnerabilityOccurrenceIn"])
    types["VulnerabilityOccurrenceOut"] = t.struct(
        {
            "fixAvailable": t.boolean().optional(),
            "relatedUrls": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "vexAssessment": t.proxy(renames["VexAssessmentOut"]),
            "type": t.string().optional(),
            "effectiveSeverity": t.string().optional(),
            "severity": t.string().optional(),
            "cvssV2": t.proxy(renames["CVSSOut"]).optional(),
            "packageIssue": t.array(t.proxy(renames["PackageIssueOut"])),
            "cvssScore": t.number().optional(),
            "cvssv3": t.proxy(renames["CVSSOut"]).optional(),
            "longDescription": t.string().optional(),
            "cvssVersion": t.string().optional(),
            "shortDescription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityOccurrenceOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultIn"] = t.struct(
        {
            "comment": t.string().optional(),
            "decision": t.string(),
            "url": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultOut"] = t.struct(
        {
            "approverAccount": t.string().optional(),
            "comment": t.string().optional(),
            "decision": t.string(),
            "approvalTime": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultOut"])
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
    types["RecipeIn"] = t.struct(
        {
            "type": t.string().optional(),
            "environment": t.array(t.struct({"_": t.string().optional()})).optional(),
            "entryPoint": t.string().optional(),
            "definedInMaterial": t.string().optional(),
            "arguments": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["RecipeIn"])
    types["RecipeOut"] = t.struct(
        {
            "type": t.string().optional(),
            "environment": t.array(t.struct({"_": t.string().optional()})).optional(),
            "entryPoint": t.string().optional(),
            "definedInMaterial": t.string().optional(),
            "arguments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecipeOut"])
    types["SlsaBuilderIn"] = t.struct({"id": t.string()}).named(
        renames["SlsaBuilderIn"]
    )
    types["SlsaBuilderOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SlsaBuilderOut"])
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
    types["DeploymentOccurrenceIn"] = t.struct(
        {
            "platform": t.string().optional(),
            "userEmail": t.string().optional(),
            "address": t.string().optional(),
            "config": t.string().optional(),
            "undeployTime": t.string().optional(),
            "resourceUri": t.array(t.string()).optional(),
            "deployTime": t.string(),
        }
    ).named(renames["DeploymentOccurrenceIn"])
    types["DeploymentOccurrenceOut"] = t.struct(
        {
            "platform": t.string().optional(),
            "userEmail": t.string().optional(),
            "address": t.string().optional(),
            "config": t.string().optional(),
            "undeployTime": t.string().optional(),
            "resourceUri": t.array(t.string()).optional(),
            "deployTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOccurrenceOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn"] = t.struct(
        {
            "entrypoint": t.string().optional(),
            "name": t.string(),
            "id": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "secretEnv": t.array(t.string()).optional(),
            "volumes": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn"])
            ).optional(),
            "script": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "timeout": t.string().optional(),
            "allowFailure": t.boolean().optional(),
            "dir": t.string().optional(),
            "allowExitCodes": t.array(t.integer()).optional(),
            "args": t.array(t.string()).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut"] = t.struct(
        {
            "entrypoint": t.string().optional(),
            "name": t.string(),
            "id": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "timing": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "secretEnv": t.array(t.string()).optional(),
            "volumes": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut"])
            ).optional(),
            "exitCode": t.integer().optional(),
            "pullTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "script": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "timeout": t.string().optional(),
            "allowFailure": t.boolean().optional(),
            "dir": t.string().optional(),
            "allowExitCodes": t.array(t.integer()).optional(),
            "args": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut"])
    types["ImageOccurrenceIn"] = t.struct(
        {
            "fingerprint": t.proxy(renames["FingerprintIn"]),
            "baseResourceUrl": t.string().optional(),
            "distance": t.integer().optional(),
            "layerInfo": t.array(t.proxy(renames["LayerIn"])).optional(),
        }
    ).named(renames["ImageOccurrenceIn"])
    types["ImageOccurrenceOut"] = t.struct(
        {
            "fingerprint": t.proxy(renames["FingerprintOut"]),
            "baseResourceUrl": t.string().optional(),
            "distance": t.integer().optional(),
            "layerInfo": t.array(t.proxy(renames["LayerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOccurrenceOut"])
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
    types["VexAssessmentIn"] = t.struct(
        {
            "cve": t.string().optional(),
            "state": t.string().optional(),
            "noteName": t.string().optional(),
            "remediations": t.array(t.proxy(renames["RemediationIn"])).optional(),
            "impacts": t.array(t.string()).optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "justification": t.proxy(renames["JustificationIn"]).optional(),
        }
    ).named(renames["VexAssessmentIn"])
    types["VexAssessmentOut"] = t.struct(
        {
            "cve": t.string().optional(),
            "state": t.string().optional(),
            "noteName": t.string().optional(),
            "remediations": t.array(t.proxy(renames["RemediationOut"])).optional(),
            "impacts": t.array(t.string()).optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "justification": t.proxy(renames["JustificationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VexAssessmentOut"])
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
    types["DiscoveryNoteIn"] = t.struct({"analysisKind": t.string()}).named(
        renames["DiscoveryNoteIn"]
    )
    types["DiscoveryNoteOut"] = t.struct(
        {
            "analysisKind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoveryNoteOut"])
    types["VulnerabilityAssessmentNoteIn"] = t.struct(
        {
            "assessment": t.proxy(renames["AssessmentIn"]).optional(),
            "product": t.proxy(renames["ProductIn"]).optional(),
            "title": t.string().optional(),
            "languageCode": t.string().optional(),
            "longDescription": t.string().optional(),
            "shortDescription": t.string().optional(),
            "publisher": t.proxy(renames["PublisherIn"]).optional(),
        }
    ).named(renames["VulnerabilityAssessmentNoteIn"])
    types["VulnerabilityAssessmentNoteOut"] = t.struct(
        {
            "assessment": t.proxy(renames["AssessmentOut"]).optional(),
            "product": t.proxy(renames["ProductOut"]).optional(),
            "title": t.string().optional(),
            "languageCode": t.string().optional(),
            "longDescription": t.string().optional(),
            "shortDescription": t.string().optional(),
            "publisher": t.proxy(renames["PublisherOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityAssessmentNoteOut"])
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
    types["GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataIn"] = t.struct(
        {"endTime": t.string().optional(), "createTime": t.string().optional()}
    ).named(renames["GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataIn"])
    types["GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataOut"])
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
            "paths": t.array(t.string()).optional(),
            "timing": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsOut"
        ]
    )
    types["PublisherIn"] = t.struct(
        {
            "publisherNamespace": t.string().optional(),
            "name": t.string().optional(),
            "issuingAuthority": t.string().optional(),
        }
    ).named(renames["PublisherIn"])
    types["PublisherOut"] = t.struct(
        {
            "publisherNamespace": t.string().optional(),
            "name": t.string().optional(),
            "issuingAuthority": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherOut"])
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
    types["VulnerabilityNoteIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "windowsDetails": t.array(t.proxy(renames["WindowsDetailIn"])).optional(),
            "cvssScore": t.number().optional(),
            "cvssVersion": t.string().optional(),
            "cvssV2": t.proxy(renames["CVSSIn"]).optional(),
            "cvssV3": t.proxy(renames["CVSSv3In"]).optional(),
            "sourceUpdateTime": t.string().optional(),
            "details": t.array(t.proxy(renames["DetailIn"])).optional(),
        }
    ).named(renames["VulnerabilityNoteIn"])
    types["VulnerabilityNoteOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "windowsDetails": t.array(t.proxy(renames["WindowsDetailOut"])).optional(),
            "cvssScore": t.number().optional(),
            "cvssVersion": t.string().optional(),
            "cvssV2": t.proxy(renames["CVSSOut"]).optional(),
            "cvssV3": t.proxy(renames["CVSSv3Out"]).optional(),
            "sourceUpdateTime": t.string().optional(),
            "details": t.array(t.proxy(renames["DetailOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityNoteOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceIn"] = t.struct(
        {
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
            "repoSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut"]
            ).optional(),
            "storageSourceManifest": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut"
                ]
            ).optional(),
            "gitSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceOut"])
    types["BatchCreateOccurrencesResponseIn"] = t.struct(
        {"occurrences": t.array(t.proxy(renames["OccurrenceIn"])).optional()}
    ).named(renames["BatchCreateOccurrencesResponseIn"])
    types["BatchCreateOccurrencesResponseOut"] = t.struct(
        {
            "occurrences": t.array(t.proxy(renames["OccurrenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateOccurrencesResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["WindowsDetailIn"] = t.struct(
        {
            "fixingKbs": t.array(t.proxy(renames["KnowledgeBaseIn"])),
            "name": t.string(),
            "cpeUri": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["WindowsDetailIn"])
    types["WindowsDetailOut"] = t.struct(
        {
            "fixingKbs": t.array(t.proxy(renames["KnowledgeBaseOut"])),
            "name": t.string(),
            "cpeUri": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsDetailOut"])
    types["VulnerabilityOccurrencesSummaryIn"] = t.struct(
        {"counts": t.array(t.proxy(renames["FixableTotalByDigestIn"])).optional()}
    ).named(renames["VulnerabilityOccurrencesSummaryIn"])
    types["VulnerabilityOccurrencesSummaryOut"] = t.struct(
        {
            "counts": t.array(t.proxy(renames["FixableTotalByDigestOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityOccurrencesSummaryOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["WindowsUpdateIn"] = t.struct(
        {
            "categories": t.array(t.proxy(renames["CategoryIn"])).optional(),
            "description": t.string().optional(),
            "lastPublishedTimestamp": t.string().optional(),
            "supportUrl": t.string().optional(),
            "title": t.string().optional(),
            "identity": t.proxy(renames["IdentityIn"]),
            "kbArticleIds": t.array(t.string()).optional(),
        }
    ).named(renames["WindowsUpdateIn"])
    types["WindowsUpdateOut"] = t.struct(
        {
            "categories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "description": t.string().optional(),
            "lastPublishedTimestamp": t.string().optional(),
            "supportUrl": t.string().optional(),
            "title": t.string().optional(),
            "identity": t.proxy(renames["IdentityOut"]),
            "kbArticleIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsUpdateOut"])
    types["SbomReferenceIntotoPredicateIn"] = t.struct(
        {
            "digest": t.struct({"_": t.string().optional()}).optional(),
            "referrerId": t.string().optional(),
            "mimeType": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["SbomReferenceIntotoPredicateIn"])
    types["SbomReferenceIntotoPredicateOut"] = t.struct(
        {
            "digest": t.struct({"_": t.string().optional()}).optional(),
            "referrerId": t.string().optional(),
            "mimeType": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SbomReferenceIntotoPredicateOut"])
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
    types["HintIn"] = t.struct({"humanReadableName": t.string()}).named(
        renames["HintIn"]
    )
    types["HintOut"] = t.struct(
        {
            "humanReadableName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HintOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["SBOMReferenceOccurrenceIn"] = t.struct(
        {
            "payload": t.proxy(renames["SbomReferenceIntotoPayloadIn"]).optional(),
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureIn"])).optional(),
            "payloadType": t.string().optional(),
        }
    ).named(renames["SBOMReferenceOccurrenceIn"])
    types["SBOMReferenceOccurrenceOut"] = t.struct(
        {
            "payload": t.proxy(renames["SbomReferenceIntotoPayloadOut"]).optional(),
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureOut"])).optional(),
            "payloadType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SBOMReferenceOccurrenceOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn"] = t.struct(
        {
            "bucket": t.string().optional(),
            "generation": t.string().optional(),
            "object": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut"] = t.struct(
        {
            "bucket": t.string().optional(),
            "generation": t.string().optional(),
            "object": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut"])
    types["DSSEAttestationNoteIn"] = t.struct(
        {"hint": t.proxy(renames["DSSEHintIn"]).optional()}
    ).named(renames["DSSEAttestationNoteIn"])
    types["DSSEAttestationNoteOut"] = t.struct(
        {
            "hint": t.proxy(renames["DSSEHintOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DSSEAttestationNoteOut"])
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
    types["ComplianceNoteIn"] = t.struct(
        {
            "version": t.array(t.proxy(renames["ComplianceVersionIn"])).optional(),
            "scanInstructions": t.string().optional(),
            "cisBenchmark": t.proxy(renames["CisBenchmarkIn"]),
            "title": t.string().optional(),
            "rationale": t.string().optional(),
            "remediation": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ComplianceNoteIn"])
    types["ComplianceNoteOut"] = t.struct(
        {
            "version": t.array(t.proxy(renames["ComplianceVersionOut"])).optional(),
            "scanInstructions": t.string().optional(),
            "cisBenchmark": t.proxy(renames["CisBenchmarkOut"]),
            "title": t.string().optional(),
            "rationale": t.string().optional(),
            "remediation": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComplianceNoteOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn"] = t.struct(
        {
            "diskSizeGb": t.string().optional(),
            "defaultLogsBucketBehavior": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "pool": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionIn"
                ]
            ).optional(),
            "volumes": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn"])
            ).optional(),
            "requestedVerifyOption": t.string().optional(),
            "logStreamingOption": t.string().optional(),
            "sourceProvenanceHash": t.array(t.string()).optional(),
            "machineType": t.string().optional(),
            "dynamicSubstitutions": t.boolean().optional(),
            "substitutionOption": t.string().optional(),
            "workerPool": t.string().optional(),
            "secretEnv": t.array(t.string()).optional(),
            "logging": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut"] = t.struct(
        {
            "diskSizeGb": t.string().optional(),
            "defaultLogsBucketBehavior": t.string().optional(),
            "env": t.array(t.string()).optional(),
            "pool": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionOut"
                ]
            ).optional(),
            "volumes": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut"])
            ).optional(),
            "requestedVerifyOption": t.string().optional(),
            "logStreamingOption": t.string().optional(),
            "sourceProvenanceHash": t.array(t.string()).optional(),
            "machineType": t.string().optional(),
            "dynamicSubstitutions": t.boolean().optional(),
            "substitutionOption": t.string().optional(),
            "workerPool": t.string().optional(),
            "secretEnv": t.array(t.string()).optional(),
            "logging": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut"])
    types["MetadataIn"] = t.struct(
        {
            "reproducible": t.boolean().optional(),
            "buildInvocationId": t.string().optional(),
            "completeness": t.proxy(renames["CompletenessIn"]).optional(),
            "buildStartedOn": t.string().optional(),
            "buildFinishedOn": t.string().optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "reproducible": t.boolean().optional(),
            "buildInvocationId": t.string().optional(),
            "completeness": t.proxy(renames["CompletenessOut"]).optional(),
            "buildStartedOn": t.string().optional(),
            "buildFinishedOn": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
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
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"] = t.struct(
        {
            "buildFinishedOn": t.string(),
            "reproducible": t.boolean(),
            "buildStartedOn": t.string(),
            "buildInvocationId": t.string(),
            "completeness": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"]
            ),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"] = t.struct(
        {
            "buildFinishedOn": t.string(),
            "reproducible": t.boolean(),
            "buildStartedOn": t.string(),
            "buildInvocationId": t.string(),
            "completeness": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"])
    types["DSSEHintIn"] = t.struct({"humanReadableName": t.string()}).named(
        renames["DSSEHintIn"]
    )
    types["DSSEHintOut"] = t.struct(
        {
            "humanReadableName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DSSEHintOut"])
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn"
    ] = t.struct(
        {
            "generation": t.string().optional(),
            "bucket": t.string().optional(),
            "object": t.string().optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut"
    ] = t.struct(
        {
            "generation": t.string().optional(),
            "bucket": t.string().optional(),
            "object": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut"]
    )
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
    types["CVSSv3In"] = t.struct(
        {
            "baseScore": t.number().optional(),
            "exploitabilityScore": t.number(),
            "userInteraction": t.string(),
            "availabilityImpact": t.string(),
            "attackComplexity": t.string(),
            "scope": t.string(),
            "privilegesRequired": t.string(),
            "integrityImpact": t.string(),
            "impactScore": t.number(),
            "attackVector": t.string().optional(),
            "confidentialityImpact": t.string(),
        }
    ).named(renames["CVSSv3In"])
    types["CVSSv3Out"] = t.struct(
        {
            "baseScore": t.number().optional(),
            "exploitabilityScore": t.number(),
            "userInteraction": t.string(),
            "availabilityImpact": t.string(),
            "attackComplexity": t.string(),
            "scope": t.string(),
            "privilegesRequired": t.string(),
            "integrityImpact": t.string(),
            "impactScore": t.number(),
            "attackVector": t.string().optional(),
            "confidentialityImpact": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CVSSv3Out"])
    types["GerritSourceContextIn"] = t.struct(
        {
            "gerritProject": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
            "revisionId": t.string().optional(),
            "hostUri": t.string().optional(),
        }
    ).named(renames["GerritSourceContextIn"])
    types["GerritSourceContextOut"] = t.struct(
        {
            "gerritProject": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "revisionId": t.string().optional(),
            "hostUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GerritSourceContextOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1HashIn"] = t.struct(
        {"type": t.string().optional(), "value": t.string().optional()}
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1HashIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1HashOut"] = t.struct(
        {
            "type": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1HashOut"])
    types["PackageNoteIn"] = t.struct(
        {
            "maintainer": t.string().optional(),
            "digest": t.array(t.proxy(renames["DigestIn"])).optional(),
            "url": t.string().optional(),
            "version": t.proxy(renames["VersionIn"]).optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "packageType": t.string().optional(),
            "distribution": t.array(t.proxy(renames["DistributionIn"])).optional(),
            "cpeUri": t.string().optional(),
            "license": t.proxy(renames["LicenseIn"]).optional(),
            "architecture": t.string().optional(),
        }
    ).named(renames["PackageNoteIn"])
    types["PackageNoteOut"] = t.struct(
        {
            "maintainer": t.string().optional(),
            "digest": t.array(t.proxy(renames["DigestOut"])).optional(),
            "url": t.string().optional(),
            "version": t.proxy(renames["VersionOut"]).optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "packageType": t.string().optional(),
            "distribution": t.array(t.proxy(renames["DistributionOut"])).optional(),
            "cpeUri": t.string().optional(),
            "license": t.proxy(renames["LicenseOut"]).optional(),
            "architecture": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageNoteOut"])
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
    types["DiscoveryOccurrenceIn"] = t.struct(
        {
            "analysisStatusError": t.proxy(renames["StatusIn"]).optional(),
            "continuousAnalysis": t.string().optional(),
            "analysisError": t.array(t.proxy(renames["StatusIn"])).optional(),
            "analysisStatus": t.string().optional(),
            "cpe": t.string().optional(),
            "analysisCompleted": t.proxy(renames["AnalysisCompletedIn"]),
            "lastScanTime": t.string().optional(),
        }
    ).named(renames["DiscoveryOccurrenceIn"])
    types["DiscoveryOccurrenceOut"] = t.struct(
        {
            "analysisStatusError": t.proxy(renames["StatusOut"]).optional(),
            "continuousAnalysis": t.string().optional(),
            "analysisError": t.array(t.proxy(renames["StatusOut"])).optional(),
            "analysisStatus": t.string().optional(),
            "archiveTime": t.string().optional(),
            "cpe": t.string().optional(),
            "analysisCompleted": t.proxy(renames["AnalysisCompletedOut"]),
            "lastScanTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoveryOccurrenceOut"])
    types["BatchCreateNotesRequestIn"] = t.struct(
        {"notes": t.struct({"_": t.string().optional()})}
    ).named(renames["BatchCreateNotesRequestIn"])
    types["BatchCreateNotesRequestOut"] = t.struct(
        {
            "notes": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateNotesRequestOut"])
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
    types["BuildProvenanceIn"] = t.struct(
        {
            "commands": t.array(t.proxy(renames["CommandIn"])).optional(),
            "id": t.string(),
            "creator": t.string().optional(),
            "startTime": t.string().optional(),
            "builtArtifacts": t.array(t.proxy(renames["ArtifactIn"])).optional(),
            "triggerId": t.string().optional(),
            "sourceProvenance": t.proxy(renames["SourceIn"]).optional(),
            "buildOptions": t.struct({"_": t.string().optional()}).optional(),
            "builderVersion": t.string().optional(),
            "projectId": t.string().optional(),
            "endTime": t.string().optional(),
            "logsUri": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["BuildProvenanceIn"])
    types["BuildProvenanceOut"] = t.struct(
        {
            "commands": t.array(t.proxy(renames["CommandOut"])).optional(),
            "id": t.string(),
            "creator": t.string().optional(),
            "startTime": t.string().optional(),
            "builtArtifacts": t.array(t.proxy(renames["ArtifactOut"])).optional(),
            "triggerId": t.string().optional(),
            "sourceProvenance": t.proxy(renames["SourceOut"]).optional(),
            "buildOptions": t.struct({"_": t.string().optional()}).optional(),
            "builderVersion": t.string().optional(),
            "projectId": t.string().optional(),
            "endTime": t.string().optional(),
            "logsUri": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildProvenanceOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn"] = t.struct(
        {
            "dir": t.string().optional(),
            "commitSha": t.string().optional(),
            "branchName": t.string().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "projectId": t.string().optional(),
            "repoName": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "tagName": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut"] = t.struct(
        {
            "dir": t.string().optional(),
            "commitSha": t.string().optional(),
            "branchName": t.string().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "projectId": t.string().optional(),
            "repoName": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "tagName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut"])
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
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["PackageIssueIn"] = t.struct(
        {
            "fixedVersion": t.proxy(renames["VersionIn"]),
            "fixedPackage": t.string().optional(),
            "affectedCpeUri": t.string(),
            "affectedVersion": t.proxy(renames["VersionIn"]),
            "affectedPackage": t.string(),
            "fixAvailable": t.boolean().optional(),
            "fixedCpeUri": t.string().optional(),
            "fileLocation": t.array(
                t.proxy(renames["GrafeasV1FileLocationIn"])
            ).optional(),
            "packageType": t.string().optional(),
        }
    ).named(renames["PackageIssueIn"])
    types["PackageIssueOut"] = t.struct(
        {
            "effectiveSeverity": t.string().optional(),
            "fixedVersion": t.proxy(renames["VersionOut"]),
            "fixedPackage": t.string().optional(),
            "affectedCpeUri": t.string(),
            "affectedVersion": t.proxy(renames["VersionOut"]),
            "affectedPackage": t.string(),
            "fixAvailable": t.boolean().optional(),
            "fixedCpeUri": t.string().optional(),
            "fileLocation": t.array(
                t.proxy(renames["GrafeasV1FileLocationOut"])
            ).optional(),
            "packageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageIssueOut"])
    types["CVSSIn"] = t.struct(
        {
            "authentication": t.string(),
            "confidentialityImpact": t.string(),
            "scope": t.string(),
            "availabilityImpact": t.string(),
            "privilegesRequired": t.string(),
            "attackVector": t.string().optional(),
            "impactScore": t.number(),
            "integrityImpact": t.string(),
            "baseScore": t.number().optional(),
            "attackComplexity": t.string(),
            "userInteraction": t.string(),
            "exploitabilityScore": t.number(),
        }
    ).named(renames["CVSSIn"])
    types["CVSSOut"] = t.struct(
        {
            "authentication": t.string(),
            "confidentialityImpact": t.string(),
            "scope": t.string(),
            "availabilityImpact": t.string(),
            "privilegesRequired": t.string(),
            "attackVector": t.string().optional(),
            "impactScore": t.number(),
            "integrityImpact": t.string(),
            "baseScore": t.number().optional(),
            "attackComplexity": t.string(),
            "userInteraction": t.string(),
            "exploitabilityScore": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CVSSOut"])
    types["UpgradeNoteIn"] = t.struct(
        {
            "package": t.string(),
            "distributions": t.array(
                t.proxy(renames["UpgradeDistributionIn"])
            ).optional(),
            "version": t.proxy(renames["VersionIn"]),
            "windowsUpdate": t.proxy(renames["WindowsUpdateIn"]),
        }
    ).named(renames["UpgradeNoteIn"])
    types["UpgradeNoteOut"] = t.struct(
        {
            "package": t.string(),
            "distributions": t.array(
                t.proxy(renames["UpgradeDistributionOut"])
            ).optional(),
            "version": t.proxy(renames["VersionOut"]),
            "windowsUpdate": t.proxy(renames["WindowsUpdateOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeNoteOut"])
    types["JwtIn"] = t.struct({"compactJwt": t.string().optional()}).named(
        renames["JwtIn"]
    )
    types["JwtOut"] = t.struct(
        {
            "compactJwt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtOut"])
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
    types["UpgradeOccurrenceIn"] = t.struct(
        {
            "distribution": t.proxy(renames["UpgradeDistributionIn"]).optional(),
            "parsedVersion": t.proxy(renames["VersionIn"]),
            "windowsUpdate": t.proxy(renames["WindowsUpdateIn"]),
            "package": t.string(),
        }
    ).named(renames["UpgradeOccurrenceIn"])
    types["UpgradeOccurrenceOut"] = t.struct(
        {
            "distribution": t.proxy(renames["UpgradeDistributionOut"]).optional(),
            "parsedVersion": t.proxy(renames["VersionOut"]),
            "windowsUpdate": t.proxy(renames["WindowsUpdateOut"]),
            "package": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeOccurrenceOut"])
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
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn"] = t.struct(
        {
            "entryPoint": t.string(),
            "uri": t.string(),
            "digest": t.struct({"_": t.string().optional()}),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut"] = t.struct(
        {
            "entryPoint": t.string(),
            "uri": t.string(),
            "digest": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceIn"] = t.struct(
        {
            "url": t.string().optional(),
            "dir": t.string().optional(),
            "revision": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut"] = t.struct(
        {
            "url": t.string().optional(),
            "dir": t.string().optional(),
            "revision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsIn"] = t.struct(
        {
            "images": t.array(t.string()).optional(),
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
            "objects": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsIn"
                ]
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
            "images": t.array(t.string()).optional(),
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
            "objects": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsOut"
                ]
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
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactIn"
    ] = t.struct(
        {
            "artifactId": t.string().optional(),
            "version": t.string().optional(),
            "groupId": t.string().optional(),
            "repository": t.string().optional(),
            "path": t.string().optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactOut"
    ] = t.struct(
        {
            "artifactId": t.string().optional(),
            "version": t.string().optional(),
            "groupId": t.string().optional(),
            "repository": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactOut"]
    )
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
    types["DeploymentNoteIn"] = t.struct({"resourceUri": t.array(t.string())}).named(
        renames["DeploymentNoteIn"]
    )
    types["DeploymentNoteOut"] = t.struct(
        {
            "resourceUri": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentNoteOut"])
    types["InTotoStatementIn"] = t.struct(
        {
            "slsaProvenance": t.proxy(renames["SlsaProvenanceIn"]),
            "provenance": t.proxy(renames["InTotoProvenanceIn"]),
            "predicateType": t.string().optional(),
            "slsaProvenanceZeroTwo": t.proxy(renames["SlsaProvenanceZeroTwoIn"]),
            "subject": t.array(t.proxy(renames["SubjectIn"])),
            "_type": t.string().optional(),
        }
    ).named(renames["InTotoStatementIn"])
    types["InTotoStatementOut"] = t.struct(
        {
            "slsaProvenance": t.proxy(renames["SlsaProvenanceOut"]),
            "provenance": t.proxy(renames["InTotoProvenanceOut"]),
            "predicateType": t.string().optional(),
            "slsaProvenanceZeroTwo": t.proxy(renames["SlsaProvenanceZeroTwoOut"]),
            "subject": t.array(t.proxy(renames["SubjectOut"])),
            "_type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InTotoStatementOut"])
    types["SlsaMetadataIn"] = t.struct(
        {
            "buildInvocationId": t.string().optional(),
            "reproducible": t.boolean().optional(),
            "completeness": t.proxy(renames["SlsaCompletenessIn"]).optional(),
            "buildStartedOn": t.string().optional(),
            "buildFinishedOn": t.string().optional(),
        }
    ).named(renames["SlsaMetadataIn"])
    types["SlsaMetadataOut"] = t.struct(
        {
            "buildInvocationId": t.string().optional(),
            "reproducible": t.boolean().optional(),
            "completeness": t.proxy(renames["SlsaCompletenessOut"]).optional(),
            "buildStartedOn": t.string().optional(),
            "buildFinishedOn": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaMetadataOut"])
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
            "pushTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "uri": t.string().optional(),
            "fileHashes": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageOut"]
    )
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
    types["VersionIn"] = t.struct(
        {
            "fullName": t.string().optional(),
            "name": t.string(),
            "revision": t.string().optional(),
            "inclusive": t.boolean().optional(),
            "kind": t.string(),
            "epoch": t.integer().optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "fullName": t.string().optional(),
            "name": t.string(),
            "revision": t.string().optional(),
            "inclusive": t.boolean().optional(),
            "kind": t.string(),
            "epoch": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
    types["DetailIn"] = t.struct(
        {
            "affectedPackage": t.string(),
            "affectedCpeUri": t.string(),
            "affectedVersionEnd": t.proxy(renames["VersionIn"]).optional(),
            "isObsolete": t.boolean().optional(),
            "severityName": t.string().optional(),
            "packageType": t.string().optional(),
            "fixedPackage": t.string().optional(),
            "affectedVersionStart": t.proxy(renames["VersionIn"]).optional(),
            "vendor": t.string().optional(),
            "sourceUpdateTime": t.string().optional(),
            "fixedVersion": t.proxy(renames["VersionIn"]).optional(),
            "source": t.string().optional(),
            "description": t.string().optional(),
            "fixedCpeUri": t.string().optional(),
        }
    ).named(renames["DetailIn"])
    types["DetailOut"] = t.struct(
        {
            "affectedPackage": t.string(),
            "affectedCpeUri": t.string(),
            "affectedVersionEnd": t.proxy(renames["VersionOut"]).optional(),
            "isObsolete": t.boolean().optional(),
            "severityName": t.string().optional(),
            "packageType": t.string().optional(),
            "fixedPackage": t.string().optional(),
            "affectedVersionStart": t.proxy(renames["VersionOut"]).optional(),
            "vendor": t.string().optional(),
            "sourceUpdateTime": t.string().optional(),
            "fixedVersion": t.proxy(renames["VersionOut"]).optional(),
            "source": t.string().optional(),
            "description": t.string().optional(),
            "fixedCpeUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetailOut"])
    types["SlsaProvenanceZeroTwoIn"] = t.struct(
        {
            "buildType": t.string(),
            "buildConfig": t.struct({"_": t.string().optional()}),
            "materials": t.array(
                t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn"])
            ),
            "builder": t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"]),
            "metadata": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"]
            ),
            "invocation": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn"]
            ),
        }
    ).named(renames["SlsaProvenanceZeroTwoIn"])
    types["SlsaProvenanceZeroTwoOut"] = t.struct(
        {
            "buildType": t.string(),
            "buildConfig": t.struct({"_": t.string().optional()}),
            "materials": t.array(
                t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut"])
            ),
            "builder": t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"]),
            "metadata": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"]
            ),
            "invocation": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaProvenanceZeroTwoOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildIn"] = t.struct(
        {
            "artifacts": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsIn"]
            ).optional(),
            "logsBucket": t.string().optional(),
            "availableSecrets": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsIn"]
            ).optional(),
            "timeout": t.string().optional(),
            "queueTtl": t.string().optional(),
            "images": t.array(t.string()).optional(),
            "tags": t.array(t.string()).optional(),
            "secrets": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretIn"])
            ).optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "options": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn"]
            ).optional(),
            "source": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceIn"]
            ).optional(),
            "serviceAccount": t.string().optional(),
            "steps": t.array(
                t.proxy(
                    renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn"]
                )
            ),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOut"] = t.struct(
        {
            "results": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut"]
            ).optional(),
            "artifacts": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOut"]
            ).optional(),
            "logsBucket": t.string().optional(),
            "availableSecrets": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsOut"]
            ).optional(),
            "timeout": t.string().optional(),
            "queueTtl": t.string().optional(),
            "warnings": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningOut"
                    ]
                )
            ).optional(),
            "statusDetail": t.string().optional(),
            "createTime": t.string().optional(),
            "approval": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalOut"]
            ).optional(),
            "status": t.string().optional(),
            "sourceProvenance": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut"
                ]
            ).optional(),
            "projectId": t.string().optional(),
            "buildTriggerId": t.string().optional(),
            "id": t.string().optional(),
            "timing": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "startTime": t.string().optional(),
            "images": t.array(t.string()).optional(),
            "finishTime": t.string().optional(),
            "logUrl": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "secrets": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretOut"])
            ).optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "options": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut"]
            ).optional(),
            "source": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceOut"]
            ).optional(),
            "serviceAccount": t.string().optional(),
            "failureInfo": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoOut"
                ]
            ).optional(),
            "steps": t.array(
                t.proxy(
                    renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut"]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOut"])
    types["ListOccurrencesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "occurrences": t.array(t.proxy(renames["OccurrenceIn"])).optional(),
        }
    ).named(renames["ListOccurrencesResponseIn"])
    types["ListOccurrencesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "occurrences": t.array(t.proxy(renames["OccurrenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOccurrencesResponseOut"])
    types["AssessmentIn"] = t.struct(
        {
            "cve": t.string().optional(),
            "shortDescription": t.string().optional(),
            "longDescription": t.string().optional(),
            "impacts": t.array(t.string()).optional(),
            "justification": t.proxy(renames["JustificationIn"]).optional(),
            "remediations": t.array(t.proxy(renames["RemediationIn"])).optional(),
            "state": t.string().optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
        }
    ).named(renames["AssessmentIn"])
    types["AssessmentOut"] = t.struct(
        {
            "cve": t.string().optional(),
            "shortDescription": t.string().optional(),
            "longDescription": t.string().optional(),
            "impacts": t.array(t.string()).optional(),
            "justification": t.proxy(renames["JustificationOut"]).optional(),
            "remediations": t.array(t.proxy(renames["RemediationOut"])).optional(),
            "state": t.string().optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssessmentOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageIn"] = t.struct(
        {"name": t.string().optional(), "digest": t.string().optional()}
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageOut"] = t.struct(
        {
            "name": t.string().optional(),
            "pushTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "digest": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageOut"])
    types["BatchCreateNotesResponseIn"] = t.struct(
        {"notes": t.array(t.proxy(renames["NoteIn"])).optional()}
    ).named(renames["BatchCreateNotesResponseIn"])
    types["BatchCreateNotesResponseOut"] = t.struct(
        {
            "notes": t.array(t.proxy(renames["NoteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateNotesResponseOut"])
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
    types["RemediationIn"] = t.struct(
        {
            "remediationUri": t.proxy(renames["RelatedUrlIn"]).optional(),
            "details": t.string().optional(),
            "remediationType": t.string().optional(),
        }
    ).named(renames["RemediationIn"])
    types["RemediationOut"] = t.struct(
        {
            "remediationUri": t.proxy(renames["RelatedUrlOut"]).optional(),
            "details": t.string().optional(),
            "remediationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemediationOut"])
    types["PackageOccurrenceIn"] = t.struct(
        {
            "license": t.proxy(renames["LicenseIn"]).optional(),
            "location": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["PackageOccurrenceIn"])
    types["PackageOccurrenceOut"] = t.struct(
        {
            "version": t.proxy(renames["VersionOut"]).optional(),
            "license": t.proxy(renames["LicenseOut"]).optional(),
            "architecture": t.string().optional(),
            "name": t.string(),
            "cpeUri": t.string().optional(),
            "location": t.array(t.proxy(renames["LocationOut"])).optional(),
            "packageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageOccurrenceOut"])
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
    types["BatchCreateOccurrencesRequestIn"] = t.struct(
        {"occurrences": t.array(t.proxy(renames["OccurrenceIn"]))}
    ).named(renames["BatchCreateOccurrencesRequestIn"])
    types["BatchCreateOccurrencesRequestOut"] = t.struct(
        {
            "occurrences": t.array(t.proxy(renames["OccurrenceOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateOccurrencesRequestOut"])
    types["DistributionIn"] = t.struct(
        {
            "cpeUri": t.string(),
            "latestVersion": t.proxy(renames["VersionIn"]).optional(),
            "maintainer": t.string().optional(),
            "url": t.string().optional(),
            "description": t.string().optional(),
            "architecture": t.string().optional(),
        }
    ).named(renames["DistributionIn"])
    types["DistributionOut"] = t.struct(
        {
            "cpeUri": t.string(),
            "latestVersion": t.proxy(renames["VersionOut"]).optional(),
            "maintainer": t.string().optional(),
            "url": t.string().optional(),
            "description": t.string().optional(),
            "architecture": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DistributionOut"])

    functions = {}
    functions["projectsOccurrencesBatchCreate"] = containeranalysis.post(
        "v1/{parent}/occurrences",
        t.struct(
            {
                "parent": t.string(),
                "resourceUri": t.string(),
                "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
                "sbomReference": t.proxy(
                    renames["SBOMReferenceOccurrenceIn"]
                ).optional(),
                "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
                "kind": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
                "noteName": t.string(),
                "vulnerability": t.proxy(
                    renames["VulnerabilityOccurrenceIn"]
                ).optional(),
                "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
                "updateTime": t.string().optional(),
                "remediation": t.string().optional(),
                "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
                "dsseAttestation": t.proxy(
                    renames["DSSEAttestationOccurrenceIn"]
                ).optional(),
                "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
                "createTime": t.string().optional(),
                "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
                "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
                "name": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OccurrenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesGetIamPolicy"] = containeranalysis.post(
        "v1/{parent}/occurrences",
        t.struct(
            {
                "parent": t.string(),
                "resourceUri": t.string(),
                "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
                "sbomReference": t.proxy(
                    renames["SBOMReferenceOccurrenceIn"]
                ).optional(),
                "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
                "kind": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
                "noteName": t.string(),
                "vulnerability": t.proxy(
                    renames["VulnerabilityOccurrenceIn"]
                ).optional(),
                "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
                "updateTime": t.string().optional(),
                "remediation": t.string().optional(),
                "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
                "dsseAttestation": t.proxy(
                    renames["DSSEAttestationOccurrenceIn"]
                ).optional(),
                "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
                "createTime": t.string().optional(),
                "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
                "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
                "name": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OccurrenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesDelete"] = containeranalysis.post(
        "v1/{parent}/occurrences",
        t.struct(
            {
                "parent": t.string(),
                "resourceUri": t.string(),
                "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
                "sbomReference": t.proxy(
                    renames["SBOMReferenceOccurrenceIn"]
                ).optional(),
                "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
                "kind": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
                "noteName": t.string(),
                "vulnerability": t.proxy(
                    renames["VulnerabilityOccurrenceIn"]
                ).optional(),
                "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
                "updateTime": t.string().optional(),
                "remediation": t.string().optional(),
                "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
                "dsseAttestation": t.proxy(
                    renames["DSSEAttestationOccurrenceIn"]
                ).optional(),
                "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
                "createTime": t.string().optional(),
                "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
                "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
                "name": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OccurrenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesGet"] = containeranalysis.post(
        "v1/{parent}/occurrences",
        t.struct(
            {
                "parent": t.string(),
                "resourceUri": t.string(),
                "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
                "sbomReference": t.proxy(
                    renames["SBOMReferenceOccurrenceIn"]
                ).optional(),
                "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
                "kind": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
                "noteName": t.string(),
                "vulnerability": t.proxy(
                    renames["VulnerabilityOccurrenceIn"]
                ).optional(),
                "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
                "updateTime": t.string().optional(),
                "remediation": t.string().optional(),
                "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
                "dsseAttestation": t.proxy(
                    renames["DSSEAttestationOccurrenceIn"]
                ).optional(),
                "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
                "createTime": t.string().optional(),
                "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
                "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
                "name": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OccurrenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesTestIamPermissions"] = containeranalysis.post(
        "v1/{parent}/occurrences",
        t.struct(
            {
                "parent": t.string(),
                "resourceUri": t.string(),
                "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
                "sbomReference": t.proxy(
                    renames["SBOMReferenceOccurrenceIn"]
                ).optional(),
                "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
                "kind": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
                "noteName": t.string(),
                "vulnerability": t.proxy(
                    renames["VulnerabilityOccurrenceIn"]
                ).optional(),
                "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
                "updateTime": t.string().optional(),
                "remediation": t.string().optional(),
                "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
                "dsseAttestation": t.proxy(
                    renames["DSSEAttestationOccurrenceIn"]
                ).optional(),
                "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
                "createTime": t.string().optional(),
                "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
                "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
                "name": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OccurrenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesGetVulnerabilitySummary"] = containeranalysis.post(
        "v1/{parent}/occurrences",
        t.struct(
            {
                "parent": t.string(),
                "resourceUri": t.string(),
                "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
                "sbomReference": t.proxy(
                    renames["SBOMReferenceOccurrenceIn"]
                ).optional(),
                "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
                "kind": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
                "noteName": t.string(),
                "vulnerability": t.proxy(
                    renames["VulnerabilityOccurrenceIn"]
                ).optional(),
                "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
                "updateTime": t.string().optional(),
                "remediation": t.string().optional(),
                "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
                "dsseAttestation": t.proxy(
                    renames["DSSEAttestationOccurrenceIn"]
                ).optional(),
                "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
                "createTime": t.string().optional(),
                "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
                "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
                "name": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OccurrenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesList"] = containeranalysis.post(
        "v1/{parent}/occurrences",
        t.struct(
            {
                "parent": t.string(),
                "resourceUri": t.string(),
                "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
                "sbomReference": t.proxy(
                    renames["SBOMReferenceOccurrenceIn"]
                ).optional(),
                "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
                "kind": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
                "noteName": t.string(),
                "vulnerability": t.proxy(
                    renames["VulnerabilityOccurrenceIn"]
                ).optional(),
                "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
                "updateTime": t.string().optional(),
                "remediation": t.string().optional(),
                "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
                "dsseAttestation": t.proxy(
                    renames["DSSEAttestationOccurrenceIn"]
                ).optional(),
                "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
                "createTime": t.string().optional(),
                "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
                "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
                "name": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OccurrenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesPatch"] = containeranalysis.post(
        "v1/{parent}/occurrences",
        t.struct(
            {
                "parent": t.string(),
                "resourceUri": t.string(),
                "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
                "sbomReference": t.proxy(
                    renames["SBOMReferenceOccurrenceIn"]
                ).optional(),
                "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
                "kind": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
                "noteName": t.string(),
                "vulnerability": t.proxy(
                    renames["VulnerabilityOccurrenceIn"]
                ).optional(),
                "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
                "updateTime": t.string().optional(),
                "remediation": t.string().optional(),
                "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
                "dsseAttestation": t.proxy(
                    renames["DSSEAttestationOccurrenceIn"]
                ).optional(),
                "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
                "createTime": t.string().optional(),
                "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
                "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
                "name": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OccurrenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesSetIamPolicy"] = containeranalysis.post(
        "v1/{parent}/occurrences",
        t.struct(
            {
                "parent": t.string(),
                "resourceUri": t.string(),
                "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
                "sbomReference": t.proxy(
                    renames["SBOMReferenceOccurrenceIn"]
                ).optional(),
                "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
                "kind": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
                "noteName": t.string(),
                "vulnerability": t.proxy(
                    renames["VulnerabilityOccurrenceIn"]
                ).optional(),
                "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
                "updateTime": t.string().optional(),
                "remediation": t.string().optional(),
                "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
                "dsseAttestation": t.proxy(
                    renames["DSSEAttestationOccurrenceIn"]
                ).optional(),
                "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
                "createTime": t.string().optional(),
                "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
                "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
                "name": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OccurrenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesGetNotes"] = containeranalysis.post(
        "v1/{parent}/occurrences",
        t.struct(
            {
                "parent": t.string(),
                "resourceUri": t.string(),
                "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
                "sbomReference": t.proxy(
                    renames["SBOMReferenceOccurrenceIn"]
                ).optional(),
                "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
                "kind": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
                "noteName": t.string(),
                "vulnerability": t.proxy(
                    renames["VulnerabilityOccurrenceIn"]
                ).optional(),
                "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
                "updateTime": t.string().optional(),
                "remediation": t.string().optional(),
                "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
                "dsseAttestation": t.proxy(
                    renames["DSSEAttestationOccurrenceIn"]
                ).optional(),
                "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
                "createTime": t.string().optional(),
                "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
                "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
                "name": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OccurrenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesCreate"] = containeranalysis.post(
        "v1/{parent}/occurrences",
        t.struct(
            {
                "parent": t.string(),
                "resourceUri": t.string(),
                "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
                "sbomReference": t.proxy(
                    renames["SBOMReferenceOccurrenceIn"]
                ).optional(),
                "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
                "kind": t.string().optional(),
                "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
                "noteName": t.string(),
                "vulnerability": t.proxy(
                    renames["VulnerabilityOccurrenceIn"]
                ).optional(),
                "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
                "updateTime": t.string().optional(),
                "remediation": t.string().optional(),
                "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
                "dsseAttestation": t.proxy(
                    renames["DSSEAttestationOccurrenceIn"]
                ).optional(),
                "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
                "createTime": t.string().optional(),
                "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
                "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
                "name": t.string().optional(),
                "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OccurrenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesBatchCreate"] = containeranalysis.delete(
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
    functions["projectsNotesPatch"] = containeranalysis.delete(
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
    functions["projectsNotesSetIamPolicy"] = containeranalysis.delete(
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNoteOccurrencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="containeranalysis",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
