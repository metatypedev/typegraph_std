from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_containeranalysis():
    containeranalysis = HTTPRuntime("https://containeranalysis.googleapis.com/")

    renames = {
        "ErrorResponse": "_containeranalysis_1_ErrorResponse",
        "BatchCreateOccurrencesRequestIn": "_containeranalysis_2_BatchCreateOccurrencesRequestIn",
        "BatchCreateOccurrencesRequestOut": "_containeranalysis_3_BatchCreateOccurrencesRequestOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigIn": "_containeranalysis_4_ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigOut": "_containeranalysis_5_ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigOut",
        "PackageIssueIn": "_containeranalysis_6_PackageIssueIn",
        "PackageIssueOut": "_containeranalysis_7_PackageIssueOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn": "_containeranalysis_8_ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut": "_containeranalysis_9_ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut",
        "DeploymentOccurrenceIn": "_containeranalysis_10_DeploymentOccurrenceIn",
        "DeploymentOccurrenceOut": "_containeranalysis_11_DeploymentOccurrenceOut",
        "ExprIn": "_containeranalysis_12_ExprIn",
        "ExprOut": "_containeranalysis_13_ExprOut",
        "SubjectIn": "_containeranalysis_14_SubjectIn",
        "SubjectOut": "_containeranalysis_15_SubjectOut",
        "BatchCreateOccurrencesResponseIn": "_containeranalysis_16_BatchCreateOccurrencesResponseIn",
        "BatchCreateOccurrencesResponseOut": "_containeranalysis_17_BatchCreateOccurrencesResponseOut",
        "WindowsDetailIn": "_containeranalysis_18_WindowsDetailIn",
        "WindowsDetailOut": "_containeranalysis_19_WindowsDetailOut",
        "GrafeasV1FileLocationIn": "_containeranalysis_20_GrafeasV1FileLocationIn",
        "GrafeasV1FileLocationOut": "_containeranalysis_21_GrafeasV1FileLocationOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactIn": "_containeranalysis_22_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactOut": "_containeranalysis_23_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactOut",
        "AliasContextIn": "_containeranalysis_24_AliasContextIn",
        "AliasContextOut": "_containeranalysis_25_AliasContextOut",
        "GerritSourceContextIn": "_containeranalysis_26_GerritSourceContextIn",
        "GerritSourceContextOut": "_containeranalysis_27_GerritSourceContextOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsIn": "_containeranalysis_28_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsOut": "_containeranalysis_29_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjectsOut",
        "SourceIn": "_containeranalysis_30_SourceIn",
        "SourceOut": "_containeranalysis_31_SourceOut",
        "ListNotesResponseIn": "_containeranalysis_32_ListNotesResponseIn",
        "ListNotesResponseOut": "_containeranalysis_33_ListNotesResponseOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionIn": "_containeranalysis_34_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionOut": "_containeranalysis_35_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionOut",
        "JwtIn": "_containeranalysis_36_JwtIn",
        "JwtOut": "_containeranalysis_37_JwtOut",
        "ComplianceOccurrenceIn": "_containeranalysis_38_ComplianceOccurrenceIn",
        "ComplianceOccurrenceOut": "_containeranalysis_39_ComplianceOccurrenceOut",
        "EnvelopeSignatureIn": "_containeranalysis_40_EnvelopeSignatureIn",
        "EnvelopeSignatureOut": "_containeranalysis_41_EnvelopeSignatureOut",
        "BatchCreateNotesResponseIn": "_containeranalysis_42_BatchCreateNotesResponseIn",
        "BatchCreateNotesResponseOut": "_containeranalysis_43_BatchCreateNotesResponseOut",
        "ComplianceVersionIn": "_containeranalysis_44_ComplianceVersionIn",
        "ComplianceVersionOut": "_containeranalysis_45_ComplianceVersionOut",
        "VulnerabilityOccurrencesSummaryIn": "_containeranalysis_46_VulnerabilityOccurrencesSummaryIn",
        "VulnerabilityOccurrencesSummaryOut": "_containeranalysis_47_VulnerabilityOccurrencesSummaryOut",
        "LocationIn": "_containeranalysis_48_LocationIn",
        "LocationOut": "_containeranalysis_49_LocationOut",
        "CVSSIn": "_containeranalysis_50_CVSSIn",
        "CVSSOut": "_containeranalysis_51_CVSSOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretIn": "_containeranalysis_52_ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretOut": "_containeranalysis_53_ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecretOut",
        "IdentityIn": "_containeranalysis_54_IdentityIn",
        "IdentityOut": "_containeranalysis_55_IdentityOut",
        "DSSEAttestationOccurrenceIn": "_containeranalysis_56_DSSEAttestationOccurrenceIn",
        "DSSEAttestationOccurrenceOut": "_containeranalysis_57_DSSEAttestationOccurrenceOut",
        "AssessmentIn": "_containeranalysis_58_AssessmentIn",
        "AssessmentOut": "_containeranalysis_59_AssessmentOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageIn": "_containeranalysis_60_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageOut": "_containeranalysis_61_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanIn": "_containeranalysis_62_ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut": "_containeranalysis_63_ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceIn": "_containeranalysis_64_ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut": "_containeranalysis_65_ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn": "_containeranalysis_66_GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut": "_containeranalysis_67_GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut",
        "SlsaProvenanceZeroTwoIn": "_containeranalysis_68_SlsaProvenanceZeroTwoIn",
        "SlsaProvenanceZeroTwoOut": "_containeranalysis_69_SlsaProvenanceZeroTwoOut",
        "ArtifactIn": "_containeranalysis_70_ArtifactIn",
        "ArtifactOut": "_containeranalysis_71_ArtifactOut",
        "DSSEAttestationNoteIn": "_containeranalysis_72_DSSEAttestationNoteIn",
        "DSSEAttestationNoteOut": "_containeranalysis_73_DSSEAttestationNoteOut",
        "TimeSpanIn": "_containeranalysis_74_TimeSpanIn",
        "TimeSpanOut": "_containeranalysis_75_TimeSpanOut",
        "UpgradeNoteIn": "_containeranalysis_76_UpgradeNoteIn",
        "UpgradeNoteOut": "_containeranalysis_77_UpgradeNoteOut",
        "SlsaBuilderIn": "_containeranalysis_78_SlsaBuilderIn",
        "SlsaBuilderOut": "_containeranalysis_79_SlsaBuilderOut",
        "OccurrenceIn": "_containeranalysis_80_OccurrenceIn",
        "OccurrenceOut": "_containeranalysis_81_OccurrenceOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn": "_containeranalysis_82_ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut": "_containeranalysis_83_ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut",
        "StatusIn": "_containeranalysis_84_StatusIn",
        "StatusOut": "_containeranalysis_85_StatusOut",
        "DigestIn": "_containeranalysis_86_DigestIn",
        "DigestOut": "_containeranalysis_87_DigestOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn": "_containeranalysis_88_GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut": "_containeranalysis_89_GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut",
        "SbomReferenceIntotoPredicateIn": "_containeranalysis_90_SbomReferenceIntotoPredicateIn",
        "SbomReferenceIntotoPredicateOut": "_containeranalysis_91_SbomReferenceIntotoPredicateOut",
        "HashIn": "_containeranalysis_92_HashIn",
        "HashOut": "_containeranalysis_93_HashOut",
        "DiscoveryNoteIn": "_containeranalysis_94_DiscoveryNoteIn",
        "DiscoveryNoteOut": "_containeranalysis_95_DiscoveryNoteOut",
        "RelatedUrlIn": "_containeranalysis_96_RelatedUrlIn",
        "RelatedUrlOut": "_containeranalysis_97_RelatedUrlOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretIn": "_containeranalysis_98_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretOut": "_containeranalysis_99_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecretOut",
        "RemediationIn": "_containeranalysis_100_RemediationIn",
        "RemediationOut": "_containeranalysis_101_RemediationOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn": "_containeranalysis_102_GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut": "_containeranalysis_103_GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSourceOut",
        "GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataIn": "_containeranalysis_104_GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataIn",
        "GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataOut": "_containeranalysis_105_GoogleDevtoolsContaineranalysisV1alpha1OperationMetadataOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn": "_containeranalysis_106_GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut": "_containeranalysis_107_GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut",
        "MetadataIn": "_containeranalysis_108_MetadataIn",
        "MetadataOut": "_containeranalysis_109_MetadataOut",
        "SignatureIn": "_containeranalysis_110_SignatureIn",
        "SignatureOut": "_containeranalysis_111_SignatureOut",
        "CisBenchmarkIn": "_containeranalysis_112_CisBenchmarkIn",
        "CisBenchmarkOut": "_containeranalysis_113_CisBenchmarkOut",
        "DistributionIn": "_containeranalysis_114_DistributionIn",
        "DistributionOut": "_containeranalysis_115_DistributionOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn": "_containeranalysis_116_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut": "_containeranalysis_117_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut",
        "BindingIn": "_containeranalysis_118_BindingIn",
        "BindingOut": "_containeranalysis_119_BindingOut",
        "DeploymentNoteIn": "_containeranalysis_120_DeploymentNoteIn",
        "DeploymentNoteOut": "_containeranalysis_121_DeploymentNoteOut",
        "ImageNoteIn": "_containeranalysis_122_ImageNoteIn",
        "ImageNoteOut": "_containeranalysis_123_ImageNoteOut",
        "DSSEHintIn": "_containeranalysis_124_DSSEHintIn",
        "DSSEHintOut": "_containeranalysis_125_DSSEHintOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn": "_containeranalysis_126_ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut": "_containeranalysis_127_ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut",
        "VexAssessmentIn": "_containeranalysis_128_VexAssessmentIn",
        "VexAssessmentOut": "_containeranalysis_129_VexAssessmentOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceIn": "_containeranalysis_130_ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut": "_containeranalysis_131_ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut",
        "BuildProvenanceIn": "_containeranalysis_132_BuildProvenanceIn",
        "BuildProvenanceOut": "_containeranalysis_133_BuildProvenanceOut",
        "UpgradeDistributionIn": "_containeranalysis_134_UpgradeDistributionIn",
        "UpgradeDistributionOut": "_containeranalysis_135_UpgradeDistributionOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoIn": "_containeranalysis_136_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoOut": "_containeranalysis_137_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoOut",
        "WindowsUpdateIn": "_containeranalysis_138_WindowsUpdateIn",
        "WindowsUpdateOut": "_containeranalysis_139_WindowsUpdateOut",
        "VolumeIn": "_containeranalysis_140_VolumeIn",
        "VolumeOut": "_containeranalysis_141_VolumeOut",
        "TestIamPermissionsResponseIn": "_containeranalysis_142_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_containeranalysis_143_TestIamPermissionsResponseOut",
        "CloudRepoSourceContextIn": "_containeranalysis_144_CloudRepoSourceContextIn",
        "CloudRepoSourceContextOut": "_containeranalysis_145_CloudRepoSourceContextOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageIn": "_containeranalysis_146_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageOut": "_containeranalysis_147_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsIn": "_containeranalysis_148_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOut": "_containeranalysis_149_ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsIn": "_containeranalysis_150_ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut": "_containeranalysis_151_ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut",
        "VulnerabilityAssessmentNoteIn": "_containeranalysis_152_VulnerabilityAssessmentNoteIn",
        "VulnerabilityAssessmentNoteOut": "_containeranalysis_153_VulnerabilityAssessmentNoteOut",
        "VulnerabilityNoteIn": "_containeranalysis_154_VulnerabilityNoteIn",
        "VulnerabilityNoteOut": "_containeranalysis_155_VulnerabilityNoteOut",
        "PackageNoteIn": "_containeranalysis_156_PackageNoteIn",
        "PackageNoteOut": "_containeranalysis_157_PackageNoteOut",
        "GitSourceContextIn": "_containeranalysis_158_GitSourceContextIn",
        "GitSourceContextOut": "_containeranalysis_159_GitSourceContextOut",
        "NonCompliantFileIn": "_containeranalysis_160_NonCompliantFileIn",
        "NonCompliantFileOut": "_containeranalysis_161_NonCompliantFileOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1HashIn": "_containeranalysis_162_ContaineranalysisGoogleDevtoolsCloudbuildV1HashIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1HashOut": "_containeranalysis_163_ContaineranalysisGoogleDevtoolsCloudbuildV1HashOut",
        "CategoryIn": "_containeranalysis_164_CategoryIn",
        "CategoryOut": "_containeranalysis_165_CategoryOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultIn": "_containeranalysis_166_ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultOut": "_containeranalysis_167_ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultOut",
        "NoteIn": "_containeranalysis_168_NoteIn",
        "NoteOut": "_containeranalysis_169_NoteOut",
        "EmptyIn": "_containeranalysis_170_EmptyIn",
        "EmptyOut": "_containeranalysis_171_EmptyOut",
        "PackageOccurrenceIn": "_containeranalysis_172_PackageOccurrenceIn",
        "PackageOccurrenceOut": "_containeranalysis_173_PackageOccurrenceOut",
        "SetIamPolicyRequestIn": "_containeranalysis_174_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_containeranalysis_175_SetIamPolicyRequestOut",
        "SBOMReferenceOccurrenceIn": "_containeranalysis_176_SBOMReferenceOccurrenceIn",
        "SBOMReferenceOccurrenceOut": "_containeranalysis_177_SBOMReferenceOccurrenceOut",
        "SlsaProvenanceIn": "_containeranalysis_178_SlsaProvenanceIn",
        "SlsaProvenanceOut": "_containeranalysis_179_SlsaProvenanceOut",
        "PolicyIn": "_containeranalysis_180_PolicyIn",
        "PolicyOut": "_containeranalysis_181_PolicyOut",
        "LicenseIn": "_containeranalysis_182_LicenseIn",
        "LicenseOut": "_containeranalysis_183_LicenseOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageIn": "_containeranalysis_184_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageOut": "_containeranalysis_185_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageOut",
        "SlsaRecipeIn": "_containeranalysis_186_SlsaRecipeIn",
        "SlsaRecipeOut": "_containeranalysis_187_SlsaRecipeOut",
        "InTotoStatementIn": "_containeranalysis_188_InTotoStatementIn",
        "InTotoStatementOut": "_containeranalysis_189_InTotoStatementOut",
        "EnvelopeIn": "_containeranalysis_190_EnvelopeIn",
        "EnvelopeOut": "_containeranalysis_191_EnvelopeOut",
        "AnalysisCompletedIn": "_containeranalysis_192_AnalysisCompletedIn",
        "AnalysisCompletedOut": "_containeranalysis_193_AnalysisCompletedOut",
        "CommandIn": "_containeranalysis_194_CommandIn",
        "CommandOut": "_containeranalysis_195_CommandOut",
        "FileHashesIn": "_containeranalysis_196_FileHashesIn",
        "FileHashesOut": "_containeranalysis_197_FileHashesOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsIn": "_containeranalysis_198_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsOut": "_containeranalysis_199_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsOut",
        "ProjectRepoIdIn": "_containeranalysis_200_ProjectRepoIdIn",
        "ProjectRepoIdOut": "_containeranalysis_201_ProjectRepoIdOut",
        "FixableTotalByDigestIn": "_containeranalysis_202_FixableTotalByDigestIn",
        "FixableTotalByDigestOut": "_containeranalysis_203_FixableTotalByDigestOut",
        "HintIn": "_containeranalysis_204_HintIn",
        "HintOut": "_containeranalysis_205_HintOut",
        "GetPolicyOptionsIn": "_containeranalysis_206_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_containeranalysis_207_GetPolicyOptionsOut",
        "ProductIn": "_containeranalysis_208_ProductIn",
        "ProductOut": "_containeranalysis_209_ProductOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceIn": "_containeranalysis_210_ContaineranalysisGoogleDevtoolsCloudbuildV1SourceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceOut": "_containeranalysis_211_ContaineranalysisGoogleDevtoolsCloudbuildV1SourceOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningIn": "_containeranalysis_212_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningOut": "_containeranalysis_213_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn": "_containeranalysis_214_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut": "_containeranalysis_215_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildIn": "_containeranalysis_216_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOut": "_containeranalysis_217_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOut",
        "SlsaMetadataIn": "_containeranalysis_218_SlsaMetadataIn",
        "SlsaMetadataOut": "_containeranalysis_219_SlsaMetadataOut",
        "ComplianceNoteIn": "_containeranalysis_220_ComplianceNoteIn",
        "ComplianceNoteOut": "_containeranalysis_221_ComplianceNoteOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactIn": "_containeranalysis_222_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactOut": "_containeranalysis_223_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactOut",
        "LayerIn": "_containeranalysis_224_LayerIn",
        "LayerOut": "_containeranalysis_225_LayerOut",
        "SlsaCompletenessIn": "_containeranalysis_226_SlsaCompletenessIn",
        "SlsaCompletenessOut": "_containeranalysis_227_SlsaCompletenessOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretIn": "_containeranalysis_228_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1SecretOut": "_containeranalysis_229_ContaineranalysisGoogleDevtoolsCloudbuildV1SecretOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageIn": "_containeranalysis_230_ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageOut": "_containeranalysis_231_ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageOut",
        "GetIamPolicyRequestIn": "_containeranalysis_232_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_containeranalysis_233_GetIamPolicyRequestOut",
        "BuildOccurrenceIn": "_containeranalysis_234_BuildOccurrenceIn",
        "BuildOccurrenceOut": "_containeranalysis_235_BuildOccurrenceOut",
        "RecipeIn": "_containeranalysis_236_RecipeIn",
        "RecipeOut": "_containeranalysis_237_RecipeOut",
        "ImageOccurrenceIn": "_containeranalysis_238_ImageOccurrenceIn",
        "ImageOccurrenceOut": "_containeranalysis_239_ImageOccurrenceOut",
        "CompletenessIn": "_containeranalysis_240_CompletenessIn",
        "CompletenessOut": "_containeranalysis_241_CompletenessOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageIn": "_containeranalysis_242_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageOut": "_containeranalysis_243_ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackageOut",
        "DetailIn": "_containeranalysis_244_DetailIn",
        "DetailOut": "_containeranalysis_245_DetailOut",
        "ListOccurrencesResponseIn": "_containeranalysis_246_ListOccurrencesResponseIn",
        "ListOccurrencesResponseOut": "_containeranalysis_247_ListOccurrencesResponseOut",
        "UpgradeOccurrenceIn": "_containeranalysis_248_UpgradeOccurrenceIn",
        "UpgradeOccurrenceOut": "_containeranalysis_249_UpgradeOccurrenceOut",
        "TestIamPermissionsRequestIn": "_containeranalysis_250_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_containeranalysis_251_TestIamPermissionsRequestOut",
        "ListNoteOccurrencesResponseIn": "_containeranalysis_252_ListNoteOccurrencesResponseIn",
        "ListNoteOccurrencesResponseOut": "_containeranalysis_253_ListNoteOccurrencesResponseOut",
        "BatchCreateNotesRequestIn": "_containeranalysis_254_BatchCreateNotesRequestIn",
        "BatchCreateNotesRequestOut": "_containeranalysis_255_BatchCreateNotesRequestOut",
        "InTotoProvenanceIn": "_containeranalysis_256_InTotoProvenanceIn",
        "InTotoProvenanceOut": "_containeranalysis_257_InTotoProvenanceOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesIn": "_containeranalysis_258_ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesOut": "_containeranalysis_259_ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesOut",
        "MaterialIn": "_containeranalysis_260_MaterialIn",
        "MaterialOut": "_containeranalysis_261_MaterialOut",
        "AttestationNoteIn": "_containeranalysis_262_AttestationNoteIn",
        "AttestationNoteOut": "_containeranalysis_263_AttestationNoteOut",
        "SBOMReferenceNoteIn": "_containeranalysis_264_SBOMReferenceNoteIn",
        "SBOMReferenceNoteOut": "_containeranalysis_265_SBOMReferenceNoteOut",
        "FingerprintIn": "_containeranalysis_266_FingerprintIn",
        "FingerprintOut": "_containeranalysis_267_FingerprintOut",
        "BuildNoteIn": "_containeranalysis_268_BuildNoteIn",
        "BuildNoteOut": "_containeranalysis_269_BuildNoteOut",
        "CVSSv3In": "_containeranalysis_270_CVSSv3In",
        "CVSSv3Out": "_containeranalysis_271_CVSSv3Out",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalIn": "_containeranalysis_272_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalOut": "_containeranalysis_273_ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalOut",
        "JustificationIn": "_containeranalysis_274_JustificationIn",
        "JustificationOut": "_containeranalysis_275_JustificationOut",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn": "_containeranalysis_276_ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn",
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut": "_containeranalysis_277_ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut",
        "SbomReferenceIntotoPayloadIn": "_containeranalysis_278_SbomReferenceIntotoPayloadIn",
        "SbomReferenceIntotoPayloadOut": "_containeranalysis_279_SbomReferenceIntotoPayloadOut",
        "RepoIdIn": "_containeranalysis_280_RepoIdIn",
        "RepoIdOut": "_containeranalysis_281_RepoIdOut",
        "KnowledgeBaseIn": "_containeranalysis_282_KnowledgeBaseIn",
        "KnowledgeBaseOut": "_containeranalysis_283_KnowledgeBaseOut",
        "BuildStepIn": "_containeranalysis_284_BuildStepIn",
        "BuildStepOut": "_containeranalysis_285_BuildStepOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn": "_containeranalysis_286_GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut": "_containeranalysis_287_GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut",
        "VulnerabilityOccurrenceIn": "_containeranalysis_288_VulnerabilityOccurrenceIn",
        "VulnerabilityOccurrenceOut": "_containeranalysis_289_VulnerabilityOccurrenceOut",
        "PublisherIn": "_containeranalysis_290_PublisherIn",
        "PublisherOut": "_containeranalysis_291_PublisherOut",
        "SourceContextIn": "_containeranalysis_292_SourceContextIn",
        "SourceContextOut": "_containeranalysis_293_SourceContextOut",
        "DiscoveryOccurrenceIn": "_containeranalysis_294_DiscoveryOccurrenceIn",
        "DiscoveryOccurrenceOut": "_containeranalysis_295_DiscoveryOccurrenceOut",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn": "_containeranalysis_296_GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn",
        "GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut": "_containeranalysis_297_GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut",
        "VersionIn": "_containeranalysis_298_VersionIn",
        "VersionOut": "_containeranalysis_299_VersionOut",
        "BuilderConfigIn": "_containeranalysis_300_BuilderConfigIn",
        "BuilderConfigOut": "_containeranalysis_301_BuilderConfigOut",
        "AttestationOccurrenceIn": "_containeranalysis_302_AttestationOccurrenceIn",
        "AttestationOccurrenceOut": "_containeranalysis_303_AttestationOccurrenceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BatchCreateOccurrencesRequestIn"] = t.struct(
        {"occurrences": t.array(t.proxy(renames["OccurrenceIn"]))}
    ).named(renames["BatchCreateOccurrencesRequestIn"])
    types["BatchCreateOccurrencesRequestOut"] = t.struct(
        {
            "occurrences": t.array(t.proxy(renames["OccurrenceOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateOccurrencesRequestOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigIn"] = t.struct(
        {"approvalRequired": t.boolean().optional()}
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigOut"] = t.struct(
        {
            "approvalRequired": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfigOut"])
    types["PackageIssueIn"] = t.struct(
        {
            "fixedPackage": t.string().optional(),
            "fixedVersion": t.proxy(renames["VersionIn"]),
            "affectedCpeUri": t.string(),
            "packageType": t.string().optional(),
            "affectedPackage": t.string(),
            "fileLocation": t.array(
                t.proxy(renames["GrafeasV1FileLocationIn"])
            ).optional(),
            "fixAvailable": t.boolean().optional(),
            "affectedVersion": t.proxy(renames["VersionIn"]),
            "fixedCpeUri": t.string().optional(),
        }
    ).named(renames["PackageIssueIn"])
    types["PackageIssueOut"] = t.struct(
        {
            "fixedPackage": t.string().optional(),
            "fixedVersion": t.proxy(renames["VersionOut"]),
            "affectedCpeUri": t.string(),
            "packageType": t.string().optional(),
            "affectedPackage": t.string(),
            "fileLocation": t.array(
                t.proxy(renames["GrafeasV1FileLocationOut"])
            ).optional(),
            "fixAvailable": t.boolean().optional(),
            "affectedVersion": t.proxy(renames["VersionOut"]),
            "effectiveSeverity": t.string().optional(),
            "fixedCpeUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageIssueOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn"] = t.struct(
        {
            "tagName": t.string().optional(),
            "branchName": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "projectId": t.string().optional(),
            "repoName": t.string().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "dir": t.string().optional(),
            "commitSha": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut"] = t.struct(
        {
            "tagName": t.string().optional(),
            "branchName": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "projectId": t.string().optional(),
            "repoName": t.string().optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "dir": t.string().optional(),
            "commitSha": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut"])
    types["DeploymentOccurrenceIn"] = t.struct(
        {
            "undeployTime": t.string().optional(),
            "config": t.string().optional(),
            "deployTime": t.string(),
            "resourceUri": t.array(t.string()).optional(),
            "platform": t.string().optional(),
            "userEmail": t.string().optional(),
            "address": t.string().optional(),
        }
    ).named(renames["DeploymentOccurrenceIn"])
    types["DeploymentOccurrenceOut"] = t.struct(
        {
            "undeployTime": t.string().optional(),
            "config": t.string().optional(),
            "deployTime": t.string(),
            "resourceUri": t.array(t.string()).optional(),
            "platform": t.string().optional(),
            "userEmail": t.string().optional(),
            "address": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOccurrenceOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["BatchCreateOccurrencesResponseIn"] = t.struct(
        {"occurrences": t.array(t.proxy(renames["OccurrenceIn"])).optional()}
    ).named(renames["BatchCreateOccurrencesResponseIn"])
    types["BatchCreateOccurrencesResponseOut"] = t.struct(
        {
            "occurrences": t.array(t.proxy(renames["OccurrenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateOccurrencesResponseOut"])
    types["WindowsDetailIn"] = t.struct(
        {
            "name": t.string(),
            "description": t.string().optional(),
            "cpeUri": t.string(),
            "fixingKbs": t.array(t.proxy(renames["KnowledgeBaseIn"])),
        }
    ).named(renames["WindowsDetailIn"])
    types["WindowsDetailOut"] = t.struct(
        {
            "name": t.string(),
            "description": t.string().optional(),
            "cpeUri": t.string(),
            "fixingKbs": t.array(t.proxy(renames["KnowledgeBaseOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsDetailOut"])
    types["GrafeasV1FileLocationIn"] = t.struct(
        {"filePath": t.string().optional()}
    ).named(renames["GrafeasV1FileLocationIn"])
    types["GrafeasV1FileLocationOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1FileLocationOut"])
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactIn"
    ] = t.struct(
        {
            "version": t.string().optional(),
            "artifactId": t.string().optional(),
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
            "version": t.string().optional(),
            "artifactId": t.string().optional(),
            "groupId": t.string().optional(),
            "repository": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactOut"]
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
    types["GerritSourceContextIn"] = t.struct(
        {
            "gerritProject": t.string().optional(),
            "revisionId": t.string().optional(),
            "hostUri": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
        }
    ).named(renames["GerritSourceContextIn"])
    types["GerritSourceContextOut"] = t.struct(
        {
            "gerritProject": t.string().optional(),
            "revisionId": t.string().optional(),
            "hostUri": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GerritSourceContextOut"])
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
    types["SourceIn"] = t.struct(
        {
            "context": t.proxy(renames["SourceContextIn"]).optional(),
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "artifactStorageSourceUri": t.string().optional(),
            "additionalContexts": t.array(
                t.proxy(renames["SourceContextIn"])
            ).optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "context": t.proxy(renames["SourceContextOut"]).optional(),
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "artifactStorageSourceUri": t.string().optional(),
            "additionalContexts": t.array(
                t.proxy(renames["SourceContextOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
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
    types["JwtIn"] = t.struct({"compactJwt": t.string().optional()}).named(
        renames["JwtIn"]
    )
    types["JwtOut"] = t.struct(
        {
            "compactJwt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtOut"])
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
    types["BatchCreateNotesResponseIn"] = t.struct(
        {"notes": t.array(t.proxy(renames["NoteIn"])).optional()}
    ).named(renames["BatchCreateNotesResponseIn"])
    types["BatchCreateNotesResponseOut"] = t.struct(
        {
            "notes": t.array(t.proxy(renames["NoteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateNotesResponseOut"])
    types["ComplianceVersionIn"] = t.struct(
        {
            "cpeUri": t.string().optional(),
            "benchmarkDocument": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["ComplianceVersionIn"])
    types["ComplianceVersionOut"] = t.struct(
        {
            "cpeUri": t.string().optional(),
            "benchmarkDocument": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComplianceVersionOut"])
    types["VulnerabilityOccurrencesSummaryIn"] = t.struct(
        {"counts": t.array(t.proxy(renames["FixableTotalByDigestIn"])).optional()}
    ).named(renames["VulnerabilityOccurrencesSummaryIn"])
    types["VulnerabilityOccurrencesSummaryOut"] = t.struct(
        {
            "counts": t.array(t.proxy(renames["FixableTotalByDigestOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityOccurrencesSummaryOut"])
    types["LocationIn"] = t.struct(
        {
            "path": t.string().optional(),
            "cpeUri": t.string().optional(),
            "version": t.proxy(renames["VersionIn"]).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "path": t.string().optional(),
            "cpeUri": t.string().optional(),
            "version": t.proxy(renames["VersionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["CVSSIn"] = t.struct(
        {
            "baseScore": t.number().optional(),
            "privilegesRequired": t.string(),
            "scope": t.string(),
            "attackComplexity": t.string(),
            "exploitabilityScore": t.number(),
            "authentication": t.string(),
            "confidentialityImpact": t.string(),
            "impactScore": t.number(),
            "availabilityImpact": t.string(),
            "attackVector": t.string().optional(),
            "integrityImpact": t.string(),
            "userInteraction": t.string(),
        }
    ).named(renames["CVSSIn"])
    types["CVSSOut"] = t.struct(
        {
            "baseScore": t.number().optional(),
            "privilegesRequired": t.string(),
            "scope": t.string(),
            "attackComplexity": t.string(),
            "exploitabilityScore": t.number(),
            "authentication": t.string(),
            "confidentialityImpact": t.string(),
            "impactScore": t.number(),
            "availabilityImpact": t.string(),
            "attackVector": t.string().optional(),
            "integrityImpact": t.string(),
            "userInteraction": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CVSSOut"])
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
    types["AssessmentIn"] = t.struct(
        {
            "state": t.string().optional(),
            "shortDescription": t.string().optional(),
            "justification": t.proxy(renames["JustificationIn"]).optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "impacts": t.array(t.string()).optional(),
            "remediations": t.array(t.proxy(renames["RemediationIn"])).optional(),
            "longDescription": t.string().optional(),
            "cve": t.string().optional(),
        }
    ).named(renames["AssessmentIn"])
    types["AssessmentOut"] = t.struct(
        {
            "state": t.string().optional(),
            "shortDescription": t.string().optional(),
            "justification": t.proxy(renames["JustificationOut"]).optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "impacts": t.array(t.string()).optional(),
            "remediations": t.array(t.proxy(renames["RemediationOut"])).optional(),
            "longDescription": t.string().optional(),
            "cve": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssessmentOut"])
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageIn"
    ] = t.struct(
        {"packagePath": t.string().optional(), "repository": t.string().optional()}
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageOut"
    ] = t.struct(
        {
            "packagePath": t.string().optional(),
            "repository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackageOut"]
    )
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceIn"] = t.struct(
        {
            "revision": t.string().optional(),
            "url": t.string().optional(),
            "dir": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut"] = t.struct(
        {
            "revision": t.string().optional(),
            "url": t.string().optional(),
            "dir": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1GitSourceOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"] = t.struct(
        {
            "reproducible": t.boolean(),
            "completeness": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessIn"]
            ),
            "buildInvocationId": t.string(),
            "buildFinishedOn": t.string(),
            "buildStartedOn": t.string(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"] = t.struct(
        {
            "reproducible": t.boolean(),
            "completeness": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaCompletenessOut"]
            ),
            "buildInvocationId": t.string(),
            "buildFinishedOn": t.string(),
            "buildStartedOn": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"])
    types["SlsaProvenanceZeroTwoIn"] = t.struct(
        {
            "buildConfig": t.struct({"_": t.string().optional()}),
            "builder": t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"]),
            "invocation": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationIn"]
            ),
            "buildType": t.string(),
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
            "buildConfig": t.struct({"_": t.string().optional()}),
            "builder": t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"]),
            "invocation": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaInvocationOut"]
            ),
            "buildType": t.string(),
            "metadata": t.proxy(
                renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMetadataOut"]
            ),
            "materials": t.array(
                t.proxy(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaMaterialOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaProvenanceZeroTwoOut"])
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
    types["DSSEAttestationNoteIn"] = t.struct(
        {"hint": t.proxy(renames["DSSEHintIn"]).optional()}
    ).named(renames["DSSEAttestationNoteIn"])
    types["DSSEAttestationNoteOut"] = t.struct(
        {
            "hint": t.proxy(renames["DSSEHintOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DSSEAttestationNoteOut"])
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
    types["UpgradeNoteIn"] = t.struct(
        {
            "package": t.string(),
            "distributions": t.array(
                t.proxy(renames["UpgradeDistributionIn"])
            ).optional(),
            "windowsUpdate": t.proxy(renames["WindowsUpdateIn"]),
            "version": t.proxy(renames["VersionIn"]),
        }
    ).named(renames["UpgradeNoteIn"])
    types["UpgradeNoteOut"] = t.struct(
        {
            "package": t.string(),
            "distributions": t.array(
                t.proxy(renames["UpgradeDistributionOut"])
            ).optional(),
            "windowsUpdate": t.proxy(renames["WindowsUpdateOut"]),
            "version": t.proxy(renames["VersionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeNoteOut"])
    types["SlsaBuilderIn"] = t.struct({"id": t.string()}).named(
        renames["SlsaBuilderIn"]
    )
    types["SlsaBuilderOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SlsaBuilderOut"])
    types["OccurrenceIn"] = t.struct(
        {
            "attestation": t.proxy(renames["AttestationOccurrenceIn"]).optional(),
            "kind": t.string().optional(),
            "vulnerability": t.proxy(renames["VulnerabilityOccurrenceIn"]).optional(),
            "package": t.proxy(renames["PackageOccurrenceIn"]).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "deployment": t.proxy(renames["DeploymentOccurrenceIn"]).optional(),
            "upgrade": t.proxy(renames["UpgradeOccurrenceIn"]).optional(),
            "image": t.proxy(renames["ImageOccurrenceIn"]).optional(),
            "envelope": t.proxy(renames["EnvelopeIn"]).optional(),
            "remediation": t.string().optional(),
            "name": t.string().optional(),
            "dsseAttestation": t.proxy(
                renames["DSSEAttestationOccurrenceIn"]
            ).optional(),
            "discovery": t.proxy(renames["DiscoveryOccurrenceIn"]).optional(),
            "compliance": t.proxy(renames["ComplianceOccurrenceIn"]).optional(),
            "build": t.proxy(renames["BuildOccurrenceIn"]).optional(),
            "resourceUri": t.string(),
            "sbomReference": t.proxy(renames["SBOMReferenceOccurrenceIn"]).optional(),
            "noteName": t.string(),
        }
    ).named(renames["OccurrenceIn"])
    types["OccurrenceOut"] = t.struct(
        {
            "attestation": t.proxy(renames["AttestationOccurrenceOut"]).optional(),
            "kind": t.string().optional(),
            "vulnerability": t.proxy(renames["VulnerabilityOccurrenceOut"]).optional(),
            "package": t.proxy(renames["PackageOccurrenceOut"]).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "deployment": t.proxy(renames["DeploymentOccurrenceOut"]).optional(),
            "upgrade": t.proxy(renames["UpgradeOccurrenceOut"]).optional(),
            "image": t.proxy(renames["ImageOccurrenceOut"]).optional(),
            "envelope": t.proxy(renames["EnvelopeOut"]).optional(),
            "remediation": t.string().optional(),
            "name": t.string().optional(),
            "dsseAttestation": t.proxy(
                renames["DSSEAttestationOccurrenceOut"]
            ).optional(),
            "discovery": t.proxy(renames["DiscoveryOccurrenceOut"]).optional(),
            "compliance": t.proxy(renames["ComplianceOccurrenceOut"]).optional(),
            "build": t.proxy(renames["BuildOccurrenceOut"]).optional(),
            "resourceUri": t.string(),
            "sbomReference": t.proxy(renames["SBOMReferenceOccurrenceOut"]).optional(),
            "noteName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OccurrenceOut"])
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
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["DiscoveryNoteIn"] = t.struct({"analysisKind": t.string()}).named(
        renames["DiscoveryNoteIn"]
    )
    types["DiscoveryNoteOut"] = t.struct(
        {
            "analysisKind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoveryNoteOut"])
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
    types["RemediationIn"] = t.struct(
        {
            "remediationType": t.string().optional(),
            "remediationUri": t.proxy(renames["RelatedUrlIn"]).optional(),
            "details": t.string().optional(),
        }
    ).named(renames["RemediationIn"])
    types["RemediationOut"] = t.struct(
        {
            "remediationType": t.string().optional(),
            "remediationUri": t.proxy(renames["RelatedUrlOut"]).optional(),
            "details": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemediationOut"])
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
    types["MetadataIn"] = t.struct(
        {
            "reproducible": t.boolean().optional(),
            "buildFinishedOn": t.string().optional(),
            "completeness": t.proxy(renames["CompletenessIn"]).optional(),
            "buildStartedOn": t.string().optional(),
            "buildInvocationId": t.string().optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "reproducible": t.boolean().optional(),
            "buildFinishedOn": t.string().optional(),
            "completeness": t.proxy(renames["CompletenessOut"]).optional(),
            "buildStartedOn": t.string().optional(),
            "buildInvocationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["SignatureIn"] = t.struct(
        {"publicKeyId": t.string().optional(), "signature": t.string().optional()}
    ).named(renames["SignatureIn"])
    types["SignatureOut"] = t.struct(
        {
            "publicKeyId": t.string().optional(),
            "signature": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignatureOut"])
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
    types["DistributionIn"] = t.struct(
        {
            "description": t.string().optional(),
            "latestVersion": t.proxy(renames["VersionIn"]).optional(),
            "architecture": t.string().optional(),
            "url": t.string().optional(),
            "maintainer": t.string().optional(),
            "cpeUri": t.string(),
        }
    ).named(renames["DistributionIn"])
    types["DistributionOut"] = t.struct(
        {
            "description": t.string().optional(),
            "latestVersion": t.proxy(renames["VersionOut"]).optional(),
            "architecture": t.string().optional(),
            "url": t.string().optional(),
            "maintainer": t.string().optional(),
            "cpeUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DistributionOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn"] = t.struct(
        {
            "script": t.string().optional(),
            "name": t.string(),
            "dir": t.string().optional(),
            "allowFailure": t.boolean().optional(),
            "entrypoint": t.string().optional(),
            "id": t.string().optional(),
            "volumes": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn"])
            ).optional(),
            "allowExitCodes": t.array(t.integer()).optional(),
            "timeout": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "env": t.array(t.string()).optional(),
            "secretEnv": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut"] = t.struct(
        {
            "exitCode": t.integer().optional(),
            "script": t.string().optional(),
            "name": t.string(),
            "dir": t.string().optional(),
            "allowFailure": t.boolean().optional(),
            "entrypoint": t.string().optional(),
            "id": t.string().optional(),
            "volumes": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut"])
            ).optional(),
            "allowExitCodes": t.array(t.integer()).optional(),
            "status": t.string().optional(),
            "timeout": t.string().optional(),
            "waitFor": t.array(t.string()).optional(),
            "env": t.array(t.string()).optional(),
            "secretEnv": t.array(t.string()).optional(),
            "timing": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "args": t.array(t.string()).optional(),
            "pullTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut"])
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
    types["DeploymentNoteIn"] = t.struct({"resourceUri": t.array(t.string())}).named(
        renames["DeploymentNoteIn"]
    )
    types["DeploymentNoteOut"] = t.struct(
        {
            "resourceUri": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentNoteOut"])
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
            "bucket": t.string().optional(),
            "object": t.string().optional(),
            "generation": t.string().optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn"]
    )
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut"
    ] = t.struct(
        {
            "bucket": t.string().optional(),
            "object": t.string().optional(),
            "generation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut"]
    )
    types["VexAssessmentIn"] = t.struct(
        {
            "cve": t.string().optional(),
            "state": t.string().optional(),
            "impacts": t.array(t.string()).optional(),
            "justification": t.proxy(renames["JustificationIn"]).optional(),
            "remediations": t.array(t.proxy(renames["RemediationIn"])).optional(),
            "noteName": t.string().optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
        }
    ).named(renames["VexAssessmentIn"])
    types["VexAssessmentOut"] = t.struct(
        {
            "cve": t.string().optional(),
            "state": t.string().optional(),
            "impacts": t.array(t.string()).optional(),
            "justification": t.proxy(renames["JustificationOut"]).optional(),
            "remediations": t.array(t.proxy(renames["RemediationOut"])).optional(),
            "noteName": t.string().optional(),
            "relatedUris": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VexAssessmentOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceIn"] = t.struct(
        {
            "resolvedStorageSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn"]
            ).optional(),
            "resolvedRepoSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceIn"]
            ).optional(),
            "resolvedStorageSourceManifest": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestIn"
                ]
            ).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut"] = t.struct(
        {
            "resolvedStorageSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut"]
            ).optional(),
            "fileHashes": t.struct({"_": t.string().optional()}).optional(),
            "resolvedRepoSource": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSourceOut"]
            ).optional(),
            "resolvedStorageSourceManifest": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifestOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut"])
    types["BuildProvenanceIn"] = t.struct(
        {
            "commands": t.array(t.proxy(renames["CommandIn"])).optional(),
            "startTime": t.string().optional(),
            "projectId": t.string().optional(),
            "sourceProvenance": t.proxy(renames["SourceIn"]).optional(),
            "createTime": t.string().optional(),
            "builderVersion": t.string().optional(),
            "buildOptions": t.struct({"_": t.string().optional()}).optional(),
            "builtArtifacts": t.array(t.proxy(renames["ArtifactIn"])).optional(),
            "creator": t.string().optional(),
            "id": t.string(),
            "endTime": t.string().optional(),
            "triggerId": t.string().optional(),
            "logsUri": t.string().optional(),
        }
    ).named(renames["BuildProvenanceIn"])
    types["BuildProvenanceOut"] = t.struct(
        {
            "commands": t.array(t.proxy(renames["CommandOut"])).optional(),
            "startTime": t.string().optional(),
            "projectId": t.string().optional(),
            "sourceProvenance": t.proxy(renames["SourceOut"]).optional(),
            "createTime": t.string().optional(),
            "builderVersion": t.string().optional(),
            "buildOptions": t.struct({"_": t.string().optional()}).optional(),
            "builtArtifacts": t.array(t.proxy(renames["ArtifactOut"])).optional(),
            "creator": t.string().optional(),
            "id": t.string(),
            "endTime": t.string().optional(),
            "triggerId": t.string().optional(),
            "logsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildProvenanceOut"])
    types["UpgradeDistributionIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "classification": t.string().optional(),
            "cpeUri": t.string(),
            "cve": t.array(t.string()).optional(),
        }
    ).named(renames["UpgradeDistributionIn"])
    types["UpgradeDistributionOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "classification": t.string().optional(),
            "cpeUri": t.string(),
            "cve": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeDistributionOut"])
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
    types["WindowsUpdateIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "lastPublishedTimestamp": t.string().optional(),
            "categories": t.array(t.proxy(renames["CategoryIn"])).optional(),
            "kbArticleIds": t.array(t.string()).optional(),
            "identity": t.proxy(renames["IdentityIn"]),
            "supportUrl": t.string().optional(),
        }
    ).named(renames["WindowsUpdateIn"])
    types["WindowsUpdateOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "lastPublishedTimestamp": t.string().optional(),
            "categories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "kbArticleIds": t.array(t.string()).optional(),
            "identity": t.proxy(renames["IdentityOut"]),
            "supportUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsUpdateOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsIn"] = t.struct(
        {
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
            "pythonPackages": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageIn"
                    ]
                )
            ).optional(),
            "mavenArtifacts": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactIn"
                    ]
                )
            ).optional(),
            "images": t.array(t.string()).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOut"] = t.struct(
        {
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
            "pythonPackages": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackageOut"
                    ]
                )
            ).optional(),
            "mavenArtifacts": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifactOut"
                    ]
                )
            ).optional(),
            "images": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsIn"] = t.struct(
        {
            "buildStepImages": t.array(t.string()).optional(),
            "mavenArtifacts": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactIn"
                    ]
                )
            ).optional(),
            "npmPackages": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageIn"
                    ]
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
            "images": t.array(
                t.proxy(
                    renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageIn"]
                )
            ).optional(),
            "buildStepOutputs": t.array(t.string()).optional(),
            "artifactTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanIn"]
            ).optional(),
            "artifactManifest": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut"] = t.struct(
        {
            "buildStepImages": t.array(t.string()).optional(),
            "mavenArtifacts": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifactOut"
                    ]
                )
            ).optional(),
            "npmPackages": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageOut"
                    ]
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
            "images": t.array(
                t.proxy(
                    renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImageOut"]
                )
            ).optional(),
            "buildStepOutputs": t.array(t.string()).optional(),
            "artifactTiming": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpanOut"]
            ).optional(),
            "artifactManifest": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut"])
    types["VulnerabilityAssessmentNoteIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "publisher": t.proxy(renames["PublisherIn"]).optional(),
            "assessment": t.proxy(renames["AssessmentIn"]).optional(),
            "product": t.proxy(renames["ProductIn"]).optional(),
            "title": t.string().optional(),
            "longDescription": t.string().optional(),
            "shortDescription": t.string().optional(),
        }
    ).named(renames["VulnerabilityAssessmentNoteIn"])
    types["VulnerabilityAssessmentNoteOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "publisher": t.proxy(renames["PublisherOut"]).optional(),
            "assessment": t.proxy(renames["AssessmentOut"]).optional(),
            "product": t.proxy(renames["ProductOut"]).optional(),
            "title": t.string().optional(),
            "longDescription": t.string().optional(),
            "shortDescription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityAssessmentNoteOut"])
    types["VulnerabilityNoteIn"] = t.struct(
        {
            "cvssV3": t.proxy(renames["CVSSv3In"]).optional(),
            "sourceUpdateTime": t.string().optional(),
            "cvssV2": t.proxy(renames["CVSSIn"]).optional(),
            "cvssVersion": t.string().optional(),
            "cvssScore": t.number().optional(),
            "windowsDetails": t.array(t.proxy(renames["WindowsDetailIn"])).optional(),
            "details": t.array(t.proxy(renames["DetailIn"])).optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["VulnerabilityNoteIn"])
    types["VulnerabilityNoteOut"] = t.struct(
        {
            "cvssV3": t.proxy(renames["CVSSv3Out"]).optional(),
            "sourceUpdateTime": t.string().optional(),
            "cvssV2": t.proxy(renames["CVSSOut"]).optional(),
            "cvssVersion": t.string().optional(),
            "cvssScore": t.number().optional(),
            "windowsDetails": t.array(t.proxy(renames["WindowsDetailOut"])).optional(),
            "details": t.array(t.proxy(renames["DetailOut"])).optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityNoteOut"])
    types["PackageNoteIn"] = t.struct(
        {
            "cpeUri": t.string().optional(),
            "distribution": t.array(t.proxy(renames["DistributionIn"])).optional(),
            "maintainer": t.string().optional(),
            "name": t.string(),
            "architecture": t.string().optional(),
            "version": t.proxy(renames["VersionIn"]).optional(),
            "url": t.string().optional(),
            "digest": t.array(t.proxy(renames["DigestIn"])).optional(),
            "license": t.proxy(renames["LicenseIn"]).optional(),
            "description": t.string().optional(),
            "packageType": t.string().optional(),
        }
    ).named(renames["PackageNoteIn"])
    types["PackageNoteOut"] = t.struct(
        {
            "cpeUri": t.string().optional(),
            "distribution": t.array(t.proxy(renames["DistributionOut"])).optional(),
            "maintainer": t.string().optional(),
            "name": t.string(),
            "architecture": t.string().optional(),
            "version": t.proxy(renames["VersionOut"]).optional(),
            "url": t.string().optional(),
            "digest": t.array(t.proxy(renames["DigestOut"])).optional(),
            "license": t.proxy(renames["LicenseOut"]).optional(),
            "description": t.string().optional(),
            "packageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageNoteOut"])
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
    types["NonCompliantFileIn"] = t.struct(
        {
            "displayCommand": t.string().optional(),
            "reason": t.string().optional(),
            "path": t.string().optional(),
        }
    ).named(renames["NonCompliantFileIn"])
    types["NonCompliantFileOut"] = t.struct(
        {
            "displayCommand": t.string().optional(),
            "reason": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonCompliantFileOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultIn"] = t.struct(
        {
            "decision": t.string(),
            "comment": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultOut"] = t.struct(
        {
            "approvalTime": t.string().optional(),
            "decision": t.string(),
            "comment": t.string().optional(),
            "approverAccount": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResultOut"])
    types["NoteIn"] = t.struct(
        {
            "build": t.proxy(renames["BuildNoteIn"]).optional(),
            "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
            "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
            "longDescription": t.string().optional(),
            "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
            "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
            "relatedNoteNames": t.array(t.string()).optional(),
            "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
            "expirationTime": t.string().optional(),
            "vulnerabilityAssessment": t.proxy(
                renames["VulnerabilityAssessmentNoteIn"]
            ).optional(),
            "shortDescription": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "package": t.proxy(renames["PackageNoteIn"]).optional(),
            "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
            "image": t.proxy(renames["ImageNoteIn"]).optional(),
            "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["NoteIn"])
    types["NoteOut"] = t.struct(
        {
            "build": t.proxy(renames["BuildNoteOut"]).optional(),
            "attestation": t.proxy(renames["AttestationNoteOut"]).optional(),
            "upgrade": t.proxy(renames["UpgradeNoteOut"]).optional(),
            "longDescription": t.string().optional(),
            "dsseAttestation": t.proxy(renames["DSSEAttestationNoteOut"]).optional(),
            "compliance": t.proxy(renames["ComplianceNoteOut"]).optional(),
            "relatedNoteNames": t.array(t.string()).optional(),
            "relatedUrl": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "discovery": t.proxy(renames["DiscoveryNoteOut"]).optional(),
            "sbomReference": t.proxy(renames["SBOMReferenceNoteOut"]).optional(),
            "expirationTime": t.string().optional(),
            "vulnerabilityAssessment": t.proxy(
                renames["VulnerabilityAssessmentNoteOut"]
            ).optional(),
            "shortDescription": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "package": t.proxy(renames["PackageNoteOut"]).optional(),
            "deployment": t.proxy(renames["DeploymentNoteOut"]).optional(),
            "image": t.proxy(renames["ImageNoteOut"]).optional(),
            "vulnerability": t.proxy(renames["VulnerabilityNoteOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoteOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["PackageOccurrenceIn"] = t.struct(
        {
            "location": t.array(t.proxy(renames["LocationIn"])).optional(),
            "license": t.proxy(renames["LicenseIn"]).optional(),
        }
    ).named(renames["PackageOccurrenceIn"])
    types["PackageOccurrenceOut"] = t.struct(
        {
            "packageType": t.string().optional(),
            "version": t.proxy(renames["VersionOut"]).optional(),
            "cpeUri": t.string().optional(),
            "architecture": t.string().optional(),
            "name": t.string(),
            "location": t.array(t.proxy(renames["LocationOut"])).optional(),
            "license": t.proxy(renames["LicenseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageOccurrenceOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["SBOMReferenceOccurrenceIn"] = t.struct(
        {
            "payloadType": t.string().optional(),
            "payload": t.proxy(renames["SbomReferenceIntotoPayloadIn"]).optional(),
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureIn"])).optional(),
        }
    ).named(renames["SBOMReferenceOccurrenceIn"])
    types["SBOMReferenceOccurrenceOut"] = t.struct(
        {
            "payloadType": t.string().optional(),
            "payload": t.proxy(renames["SbomReferenceIntotoPayloadOut"]).optional(),
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SBOMReferenceOccurrenceOut"])
    types["SlsaProvenanceIn"] = t.struct(
        {
            "recipe": t.proxy(renames["SlsaRecipeIn"]).optional(),
            "materials": t.array(t.proxy(renames["MaterialIn"])).optional(),
            "metadata": t.proxy(renames["SlsaMetadataIn"]),
            "builder": t.proxy(renames["SlsaBuilderIn"]).optional(),
        }
    ).named(renames["SlsaProvenanceIn"])
    types["SlsaProvenanceOut"] = t.struct(
        {
            "recipe": t.proxy(renames["SlsaRecipeOut"]).optional(),
            "materials": t.array(t.proxy(renames["MaterialOut"])).optional(),
            "metadata": t.proxy(renames["SlsaMetadataOut"]),
            "builder": t.proxy(renames["SlsaBuilderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaProvenanceOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "fileHashes": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashesIn"]
            ).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageIn"])
    types[
        "ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageOut"
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
        renames["ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackageOut"]
    )
    types["SlsaRecipeIn"] = t.struct(
        {
            "arguments": t.struct({"_": t.string().optional()}).optional(),
            "definedInMaterial": t.string().optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "entryPoint": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["SlsaRecipeIn"])
    types["SlsaRecipeOut"] = t.struct(
        {
            "arguments": t.struct({"_": t.string().optional()}).optional(),
            "definedInMaterial": t.string().optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "entryPoint": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaRecipeOut"])
    types["InTotoStatementIn"] = t.struct(
        {
            "_type": t.string().optional(),
            "predicateType": t.string().optional(),
            "subject": t.array(t.proxy(renames["SubjectIn"])),
            "slsaProvenanceZeroTwo": t.proxy(renames["SlsaProvenanceZeroTwoIn"]),
            "provenance": t.proxy(renames["InTotoProvenanceIn"]),
            "slsaProvenance": t.proxy(renames["SlsaProvenanceIn"]),
        }
    ).named(renames["InTotoStatementIn"])
    types["InTotoStatementOut"] = t.struct(
        {
            "_type": t.string().optional(),
            "predicateType": t.string().optional(),
            "subject": t.array(t.proxy(renames["SubjectOut"])),
            "slsaProvenanceZeroTwo": t.proxy(renames["SlsaProvenanceZeroTwoOut"]),
            "provenance": t.proxy(renames["InTotoProvenanceOut"]),
            "slsaProvenance": t.proxy(renames["SlsaProvenanceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InTotoStatementOut"])
    types["EnvelopeIn"] = t.struct(
        {
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureIn"])),
            "payloadType": t.string(),
            "payload": t.string(),
        }
    ).named(renames["EnvelopeIn"])
    types["EnvelopeOut"] = t.struct(
        {
            "signatures": t.array(t.proxy(renames["EnvelopeSignatureOut"])),
            "payloadType": t.string(),
            "payload": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvelopeOut"])
    types["AnalysisCompletedIn"] = t.struct(
        {"analysisType": t.array(t.string())}
    ).named(renames["AnalysisCompletedIn"])
    types["AnalysisCompletedOut"] = t.struct(
        {
            "analysisType": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalysisCompletedOut"])
    types["CommandIn"] = t.struct(
        {
            "args": t.array(t.string()).optional(),
            "env": t.array(t.string()).optional(),
            "dir": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string(),
            "waitFor": t.array(t.string()).optional(),
        }
    ).named(renames["CommandIn"])
    types["CommandOut"] = t.struct(
        {
            "args": t.array(t.string()).optional(),
            "env": t.array(t.string()).optional(),
            "dir": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string(),
            "waitFor": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommandOut"])
    types["FileHashesIn"] = t.struct(
        {"fileHash": t.array(t.proxy(renames["HashIn"]))}
    ).named(renames["FileHashesIn"])
    types["FileHashesOut"] = t.struct(
        {
            "fileHash": t.array(t.proxy(renames["HashOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileHashesOut"])
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
    types["FixableTotalByDigestIn"] = t.struct(
        {
            "fixableCount": t.string().optional(),
            "totalCount": t.string().optional(),
            "resourceUri": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["FixableTotalByDigestIn"])
    types["FixableTotalByDigestOut"] = t.struct(
        {
            "fixableCount": t.string().optional(),
            "totalCount": t.string().optional(),
            "resourceUri": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FixableTotalByDigestOut"])
    types["HintIn"] = t.struct({"humanReadableName": t.string()}).named(
        renames["HintIn"]
    )
    types["HintOut"] = t.struct(
        {
            "humanReadableName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HintOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["ProductIn"] = t.struct(
        {
            "id": t.string().optional(),
            "genericUri": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ProductIn"])
    types["ProductOut"] = t.struct(
        {
            "id": t.string().optional(),
            "genericUri": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductOut"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn"] = t.struct(
        {
            "substitutionOption": t.string().optional(),
            "logging": t.string().optional(),
            "pool": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionIn"
                ]
            ).optional(),
            "env": t.array(t.string()).optional(),
            "defaultLogsBucketBehavior": t.string().optional(),
            "requestedVerifyOption": t.string().optional(),
            "sourceProvenanceHash": t.array(t.string()).optional(),
            "dynamicSubstitutions": t.boolean().optional(),
            "diskSizeGb": t.string().optional(),
            "logStreamingOption": t.string().optional(),
            "volumes": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeIn"])
            ).optional(),
            "secretEnv": t.array(t.string()).optional(),
            "workerPool": t.string().optional(),
            "machineType": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut"] = t.struct(
        {
            "substitutionOption": t.string().optional(),
            "logging": t.string().optional(),
            "pool": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOptionOut"
                ]
            ).optional(),
            "env": t.array(t.string()).optional(),
            "defaultLogsBucketBehavior": t.string().optional(),
            "requestedVerifyOption": t.string().optional(),
            "sourceProvenanceHash": t.array(t.string()).optional(),
            "dynamicSubstitutions": t.boolean().optional(),
            "diskSizeGb": t.string().optional(),
            "logStreamingOption": t.string().optional(),
            "volumes": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1VolumeOut"])
            ).optional(),
            "secretEnv": t.array(t.string()).optional(),
            "workerPool": t.string().optional(),
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildIn"] = t.struct(
        {
            "source": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceIn"]
            ).optional(),
            "images": t.array(t.string()).optional(),
            "tags": t.array(t.string()).optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "secrets": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretIn"])
            ).optional(),
            "serviceAccount": t.string().optional(),
            "availableSecrets": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsIn"]
            ).optional(),
            "queueTtl": t.string().optional(),
            "artifacts": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsIn"]
            ).optional(),
            "steps": t.array(
                t.proxy(
                    renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepIn"]
                )
            ),
            "options": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsIn"]
            ).optional(),
            "logsBucket": t.string().optional(),
            "timeout": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "sourceProvenance": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenanceOut"
                ]
            ).optional(),
            "source": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SourceOut"]
            ).optional(),
            "id": t.string().optional(),
            "approval": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApprovalOut"]
            ).optional(),
            "results": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ResultsOut"]
            ).optional(),
            "status": t.string().optional(),
            "timing": t.struct({"_": t.string().optional()}).optional(),
            "buildTriggerId": t.string().optional(),
            "images": t.array(t.string()).optional(),
            "tags": t.array(t.string()).optional(),
            "substitutions": t.struct({"_": t.string().optional()}).optional(),
            "startTime": t.string().optional(),
            "secrets": t.array(
                t.proxy(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretOut"])
            ).optional(),
            "serviceAccount": t.string().optional(),
            "statusDetail": t.string().optional(),
            "logUrl": t.string().optional(),
            "availableSecrets": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1SecretsOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "finishTime": t.string().optional(),
            "queueTtl": t.string().optional(),
            "warnings": t.array(
                t.proxy(
                    renames[
                        "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarningOut"
                    ]
                )
            ).optional(),
            "artifacts": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOut"]
            ).optional(),
            "steps": t.array(
                t.proxy(
                    renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepOut"]
                )
            ),
            "name": t.string().optional(),
            "options": t.proxy(
                renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsOut"]
            ).optional(),
            "logsBucket": t.string().optional(),
            "failureInfo": t.proxy(
                renames[
                    "ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfoOut"
                ]
            ).optional(),
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOut"])
    types["SlsaMetadataIn"] = t.struct(
        {
            "buildFinishedOn": t.string().optional(),
            "reproducible": t.boolean().optional(),
            "completeness": t.proxy(renames["SlsaCompletenessIn"]).optional(),
            "buildStartedOn": t.string().optional(),
            "buildInvocationId": t.string().optional(),
        }
    ).named(renames["SlsaMetadataIn"])
    types["SlsaMetadataOut"] = t.struct(
        {
            "buildFinishedOn": t.string().optional(),
            "reproducible": t.boolean().optional(),
            "completeness": t.proxy(renames["SlsaCompletenessOut"]).optional(),
            "buildStartedOn": t.string().optional(),
            "buildInvocationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlsaMetadataOut"])
    types["ComplianceNoteIn"] = t.struct(
        {
            "description": t.string().optional(),
            "scanInstructions": t.string().optional(),
            "version": t.array(t.proxy(renames["ComplianceVersionIn"])).optional(),
            "title": t.string().optional(),
            "cisBenchmark": t.proxy(renames["CisBenchmarkIn"]),
            "remediation": t.string().optional(),
            "rationale": t.string().optional(),
        }
    ).named(renames["ComplianceNoteIn"])
    types["ComplianceNoteOut"] = t.struct(
        {
            "description": t.string().optional(),
            "scanInstructions": t.string().optional(),
            "version": t.array(t.proxy(renames["ComplianceVersionOut"])).optional(),
            "title": t.string().optional(),
            "cisBenchmark": t.proxy(renames["CisBenchmarkOut"]),
            "remediation": t.string().optional(),
            "rationale": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComplianceNoteOut"])
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
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["BuildOccurrenceIn"] = t.struct(
        {
            "provenanceBytes": t.string().optional(),
            "intotoProvenance": t.proxy(renames["InTotoProvenanceIn"]).optional(),
            "provenance": t.proxy(renames["BuildProvenanceIn"]).optional(),
            "intotoStatement": t.proxy(renames["InTotoStatementIn"]).optional(),
        }
    ).named(renames["BuildOccurrenceIn"])
    types["BuildOccurrenceOut"] = t.struct(
        {
            "provenanceBytes": t.string().optional(),
            "intotoProvenance": t.proxy(renames["InTotoProvenanceOut"]).optional(),
            "provenance": t.proxy(renames["BuildProvenanceOut"]).optional(),
            "intotoStatement": t.proxy(renames["InTotoStatementOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOccurrenceOut"])
    types["RecipeIn"] = t.struct(
        {
            "type": t.string().optional(),
            "environment": t.array(t.struct({"_": t.string().optional()})).optional(),
            "entryPoint": t.string().optional(),
            "arguments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "definedInMaterial": t.string().optional(),
        }
    ).named(renames["RecipeIn"])
    types["RecipeOut"] = t.struct(
        {
            "type": t.string().optional(),
            "environment": t.array(t.struct({"_": t.string().optional()})).optional(),
            "entryPoint": t.string().optional(),
            "arguments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "definedInMaterial": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecipeOut"])
    types["ImageOccurrenceIn"] = t.struct(
        {
            "baseResourceUrl": t.string().optional(),
            "fingerprint": t.proxy(renames["FingerprintIn"]),
            "distance": t.integer().optional(),
            "layerInfo": t.array(t.proxy(renames["LayerIn"])).optional(),
        }
    ).named(renames["ImageOccurrenceIn"])
    types["ImageOccurrenceOut"] = t.struct(
        {
            "baseResourceUrl": t.string().optional(),
            "fingerprint": t.proxy(renames["FingerprintOut"]),
            "distance": t.integer().optional(),
            "layerInfo": t.array(t.proxy(renames["LayerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOccurrenceOut"])
    types["CompletenessIn"] = t.struct(
        {
            "environment": t.boolean().optional(),
            "materials": t.boolean().optional(),
            "arguments": t.boolean().optional(),
        }
    ).named(renames["CompletenessIn"])
    types["CompletenessOut"] = t.struct(
        {
            "environment": t.boolean().optional(),
            "materials": t.boolean().optional(),
            "arguments": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompletenessOut"])
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
    types["DetailIn"] = t.struct(
        {
            "affectedVersionEnd": t.proxy(renames["VersionIn"]).optional(),
            "description": t.string().optional(),
            "vendor": t.string().optional(),
            "fixedCpeUri": t.string().optional(),
            "source": t.string().optional(),
            "isObsolete": t.boolean().optional(),
            "affectedPackage": t.string(),
            "sourceUpdateTime": t.string().optional(),
            "affectedVersionStart": t.proxy(renames["VersionIn"]).optional(),
            "affectedCpeUri": t.string(),
            "fixedPackage": t.string().optional(),
            "severityName": t.string().optional(),
            "fixedVersion": t.proxy(renames["VersionIn"]).optional(),
            "packageType": t.string().optional(),
        }
    ).named(renames["DetailIn"])
    types["DetailOut"] = t.struct(
        {
            "affectedVersionEnd": t.proxy(renames["VersionOut"]).optional(),
            "description": t.string().optional(),
            "vendor": t.string().optional(),
            "fixedCpeUri": t.string().optional(),
            "source": t.string().optional(),
            "isObsolete": t.boolean().optional(),
            "affectedPackage": t.string(),
            "sourceUpdateTime": t.string().optional(),
            "affectedVersionStart": t.proxy(renames["VersionOut"]).optional(),
            "affectedCpeUri": t.string(),
            "fixedPackage": t.string().optional(),
            "severityName": t.string().optional(),
            "fixedVersion": t.proxy(renames["VersionOut"]).optional(),
            "packageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetailOut"])
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
    types["UpgradeOccurrenceIn"] = t.struct(
        {
            "parsedVersion": t.proxy(renames["VersionIn"]),
            "windowsUpdate": t.proxy(renames["WindowsUpdateIn"]),
            "package": t.string(),
            "distribution": t.proxy(renames["UpgradeDistributionIn"]).optional(),
        }
    ).named(renames["UpgradeOccurrenceIn"])
    types["UpgradeOccurrenceOut"] = t.struct(
        {
            "parsedVersion": t.proxy(renames["VersionOut"]),
            "windowsUpdate": t.proxy(renames["WindowsUpdateOut"]),
            "package": t.string(),
            "distribution": t.proxy(renames["UpgradeDistributionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeOccurrenceOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ListNoteOccurrencesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "occurrences": t.array(t.proxy(renames["OccurrenceIn"])).optional(),
        }
    ).named(renames["ListNoteOccurrencesResponseIn"])
    types["ListNoteOccurrencesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "occurrences": t.array(t.proxy(renames["OccurrenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNoteOccurrencesResponseOut"])
    types["BatchCreateNotesRequestIn"] = t.struct(
        {"notes": t.struct({"_": t.string().optional()})}
    ).named(renames["BatchCreateNotesRequestIn"])
    types["BatchCreateNotesRequestOut"] = t.struct(
        {
            "notes": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateNotesRequestOut"])
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
    types["AttestationNoteIn"] = t.struct(
        {"hint": t.proxy(renames["HintIn"]).optional()}
    ).named(renames["AttestationNoteIn"])
    types["AttestationNoteOut"] = t.struct(
        {
            "hint": t.proxy(renames["HintOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestationNoteOut"])
    types["SBOMReferenceNoteIn"] = t.struct(
        {"version": t.string().optional(), "format": t.string().optional()}
    ).named(renames["SBOMReferenceNoteIn"])
    types["SBOMReferenceNoteOut"] = t.struct(
        {
            "version": t.string().optional(),
            "format": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SBOMReferenceNoteOut"])
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
    types["BuildNoteIn"] = t.struct({"builderVersion": t.string()}).named(
        renames["BuildNoteIn"]
    )
    types["BuildNoteOut"] = t.struct(
        {
            "builderVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildNoteOut"])
    types["CVSSv3In"] = t.struct(
        {
            "privilegesRequired": t.string(),
            "scope": t.string(),
            "exploitabilityScore": t.number(),
            "attackComplexity": t.string(),
            "integrityImpact": t.string(),
            "userInteraction": t.string(),
            "baseScore": t.number().optional(),
            "impactScore": t.number(),
            "availabilityImpact": t.string(),
            "attackVector": t.string().optional(),
            "confidentialityImpact": t.string(),
        }
    ).named(renames["CVSSv3In"])
    types["CVSSv3Out"] = t.struct(
        {
            "privilegesRequired": t.string(),
            "scope": t.string(),
            "exploitabilityScore": t.number(),
            "attackComplexity": t.string(),
            "integrityImpact": t.string(),
            "userInteraction": t.string(),
            "baseScore": t.number().optional(),
            "impactScore": t.number(),
            "availabilityImpact": t.string(),
            "attackVector": t.string().optional(),
            "confidentialityImpact": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CVSSv3Out"])
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
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn"] = t.struct(
        {
            "object": t.string().optional(),
            "bucket": t.string().optional(),
            "generation": t.string().optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceIn"])
    types["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut"] = t.struct(
        {
            "object": t.string().optional(),
            "bucket": t.string().optional(),
            "generation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceOut"])
    types["SbomReferenceIntotoPayloadIn"] = t.struct(
        {
            "_type": t.string().optional(),
            "subject": t.array(t.proxy(renames["SubjectIn"])).optional(),
            "predicateType": t.string().optional(),
            "predicate": t.proxy(renames["SbomReferenceIntotoPredicateIn"]).optional(),
        }
    ).named(renames["SbomReferenceIntotoPayloadIn"])
    types["SbomReferenceIntotoPayloadOut"] = t.struct(
        {
            "_type": t.string().optional(),
            "subject": t.array(t.proxy(renames["SubjectOut"])).optional(),
            "predicateType": t.string().optional(),
            "predicate": t.proxy(renames["SbomReferenceIntotoPredicateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SbomReferenceIntotoPayloadOut"])
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
    types["BuildStepIn"] = t.struct(
        {
            "allowExitCodes": t.array(t.integer()).optional(),
            "exitCode": t.integer().optional(),
            "args": t.array(t.string()).optional(),
            "timing": t.proxy(renames["TimeSpanIn"]).optional(),
            "secretEnv": t.array(t.string()).optional(),
            "script": t.string().optional(),
            "allowFailure": t.boolean().optional(),
            "waitFor": t.array(t.string()).optional(),
            "pullTiming": t.proxy(renames["TimeSpanIn"]).optional(),
            "env": t.array(t.string()).optional(),
            "timeout": t.string().optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "name": t.string(),
            "dir": t.string().optional(),
            "entrypoint": t.string().optional(),
        }
    ).named(renames["BuildStepIn"])
    types["BuildStepOut"] = t.struct(
        {
            "allowExitCodes": t.array(t.integer()).optional(),
            "exitCode": t.integer().optional(),
            "args": t.array(t.string()).optional(),
            "timing": t.proxy(renames["TimeSpanOut"]).optional(),
            "secretEnv": t.array(t.string()).optional(),
            "script": t.string().optional(),
            "allowFailure": t.boolean().optional(),
            "waitFor": t.array(t.string()).optional(),
            "pullTiming": t.proxy(renames["TimeSpanOut"]).optional(),
            "env": t.array(t.string()).optional(),
            "timeout": t.string().optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "name": t.string(),
            "dir": t.string().optional(),
            "entrypoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildStepOut"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"] = t.struct(
        {"id": t.string()}
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderIn"])
    types["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GrafeasV1SlsaProvenanceZeroTwoSlsaBuilderOut"])
    types["VulnerabilityOccurrenceIn"] = t.struct(
        {
            "packageIssue": t.array(t.proxy(renames["PackageIssueIn"])),
            "relatedUrls": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
            "type": t.string().optional(),
            "shortDescription": t.string().optional(),
            "severity": t.string().optional(),
            "longDescription": t.string().optional(),
            "effectiveSeverity": t.string().optional(),
            "cvssV2": t.proxy(renames["CVSSIn"]).optional(),
            "cvssScore": t.number().optional(),
            "fixAvailable": t.boolean().optional(),
            "cvssVersion": t.string().optional(),
            "vexAssessment": t.proxy(renames["VexAssessmentIn"]),
            "cvssv3": t.proxy(renames["CVSSIn"]).optional(),
        }
    ).named(renames["VulnerabilityOccurrenceIn"])
    types["VulnerabilityOccurrenceOut"] = t.struct(
        {
            "packageIssue": t.array(t.proxy(renames["PackageIssueOut"])),
            "relatedUrls": t.array(t.proxy(renames["RelatedUrlOut"])).optional(),
            "type": t.string().optional(),
            "shortDescription": t.string().optional(),
            "severity": t.string().optional(),
            "longDescription": t.string().optional(),
            "effectiveSeverity": t.string().optional(),
            "cvssV2": t.proxy(renames["CVSSOut"]).optional(),
            "cvssScore": t.number().optional(),
            "fixAvailable": t.boolean().optional(),
            "cvssVersion": t.string().optional(),
            "vexAssessment": t.proxy(renames["VexAssessmentOut"]),
            "cvssv3": t.proxy(renames["CVSSOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerabilityOccurrenceOut"])
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
    types["SourceContextIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "cloudRepo": t.proxy(renames["CloudRepoSourceContextIn"]).optional(),
            "git": t.proxy(renames["GitSourceContextIn"]).optional(),
            "gerrit": t.proxy(renames["GerritSourceContextIn"]).optional(),
        }
    ).named(renames["SourceContextIn"])
    types["SourceContextOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "cloudRepo": t.proxy(renames["CloudRepoSourceContextOut"]).optional(),
            "git": t.proxy(renames["GitSourceContextOut"]).optional(),
            "gerrit": t.proxy(renames["GerritSourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["DiscoveryOccurrenceIn"] = t.struct(
        {
            "analysisError": t.array(t.proxy(renames["StatusIn"])).optional(),
            "lastScanTime": t.string().optional(),
            "analysisStatus": t.string().optional(),
            "cpe": t.string().optional(),
            "continuousAnalysis": t.string().optional(),
            "analysisStatusError": t.proxy(renames["StatusIn"]).optional(),
            "analysisCompleted": t.proxy(renames["AnalysisCompletedIn"]),
        }
    ).named(renames["DiscoveryOccurrenceIn"])
    types["DiscoveryOccurrenceOut"] = t.struct(
        {
            "analysisError": t.array(t.proxy(renames["StatusOut"])).optional(),
            "lastScanTime": t.string().optional(),
            "analysisStatus": t.string().optional(),
            "cpe": t.string().optional(),
            "continuousAnalysis": t.string().optional(),
            "analysisStatusError": t.proxy(renames["StatusOut"]).optional(),
            "archiveTime": t.string().optional(),
            "analysisCompleted": t.proxy(renames["AnalysisCompletedOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoveryOccurrenceOut"])
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
    types["VersionIn"] = t.struct(
        {
            "fullName": t.string().optional(),
            "epoch": t.integer().optional(),
            "kind": t.string(),
            "inclusive": t.boolean().optional(),
            "revision": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "fullName": t.string().optional(),
            "epoch": t.integer().optional(),
            "kind": t.string(),
            "inclusive": t.boolean().optional(),
            "revision": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
    types["BuilderConfigIn"] = t.struct({"id": t.string()}).named(
        renames["BuilderConfigIn"]
    )
    types["BuilderConfigOut"] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BuilderConfigOut"])
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

    functions = {}
    functions["projectsOccurrencesSetIamPolicy"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesGet"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesGetIamPolicy"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesList"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesBatchCreate"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesCreate"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesGetNotes"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesGetVulnerabilitySummary"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesPatch"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesTestIamPermissions"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOccurrencesDelete"] = containeranalysis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesTestIamPermissions"] = containeranalysis.post(
        "v1/{parent}/notes",
        t.struct(
            {
                "parent": t.string(),
                "noteId": t.string(),
                "build": t.proxy(renames["BuildNoteIn"]).optional(),
                "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
                "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
                "longDescription": t.string().optional(),
                "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
                "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
                "relatedNoteNames": t.array(t.string()).optional(),
                "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
                "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
                "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
                "expirationTime": t.string().optional(),
                "vulnerabilityAssessment": t.proxy(
                    renames["VulnerabilityAssessmentNoteIn"]
                ).optional(),
                "shortDescription": t.string().optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "updateTime": t.string().optional(),
                "package": t.proxy(renames["PackageNoteIn"]).optional(),
                "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
                "image": t.proxy(renames["ImageNoteIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
                "kind": t.string().optional(),
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
                "parent": t.string(),
                "noteId": t.string(),
                "build": t.proxy(renames["BuildNoteIn"]).optional(),
                "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
                "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
                "longDescription": t.string().optional(),
                "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
                "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
                "relatedNoteNames": t.array(t.string()).optional(),
                "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
                "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
                "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
                "expirationTime": t.string().optional(),
                "vulnerabilityAssessment": t.proxy(
                    renames["VulnerabilityAssessmentNoteIn"]
                ).optional(),
                "shortDescription": t.string().optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "updateTime": t.string().optional(),
                "package": t.proxy(renames["PackageNoteIn"]).optional(),
                "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
                "image": t.proxy(renames["ImageNoteIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
                "kind": t.string().optional(),
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
                "parent": t.string(),
                "noteId": t.string(),
                "build": t.proxy(renames["BuildNoteIn"]).optional(),
                "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
                "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
                "longDescription": t.string().optional(),
                "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
                "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
                "relatedNoteNames": t.array(t.string()).optional(),
                "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
                "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
                "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
                "expirationTime": t.string().optional(),
                "vulnerabilityAssessment": t.proxy(
                    renames["VulnerabilityAssessmentNoteIn"]
                ).optional(),
                "shortDescription": t.string().optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "updateTime": t.string().optional(),
                "package": t.proxy(renames["PackageNoteIn"]).optional(),
                "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
                "image": t.proxy(renames["ImageNoteIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
                "kind": t.string().optional(),
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
                "parent": t.string(),
                "noteId": t.string(),
                "build": t.proxy(renames["BuildNoteIn"]).optional(),
                "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
                "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
                "longDescription": t.string().optional(),
                "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
                "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
                "relatedNoteNames": t.array(t.string()).optional(),
                "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
                "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
                "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
                "expirationTime": t.string().optional(),
                "vulnerabilityAssessment": t.proxy(
                    renames["VulnerabilityAssessmentNoteIn"]
                ).optional(),
                "shortDescription": t.string().optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "updateTime": t.string().optional(),
                "package": t.proxy(renames["PackageNoteIn"]).optional(),
                "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
                "image": t.proxy(renames["ImageNoteIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
                "kind": t.string().optional(),
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
                "parent": t.string(),
                "noteId": t.string(),
                "build": t.proxy(renames["BuildNoteIn"]).optional(),
                "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
                "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
                "longDescription": t.string().optional(),
                "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
                "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
                "relatedNoteNames": t.array(t.string()).optional(),
                "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
                "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
                "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
                "expirationTime": t.string().optional(),
                "vulnerabilityAssessment": t.proxy(
                    renames["VulnerabilityAssessmentNoteIn"]
                ).optional(),
                "shortDescription": t.string().optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "updateTime": t.string().optional(),
                "package": t.proxy(renames["PackageNoteIn"]).optional(),
                "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
                "image": t.proxy(renames["ImageNoteIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
                "kind": t.string().optional(),
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
                "parent": t.string(),
                "noteId": t.string(),
                "build": t.proxy(renames["BuildNoteIn"]).optional(),
                "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
                "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
                "longDescription": t.string().optional(),
                "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
                "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
                "relatedNoteNames": t.array(t.string()).optional(),
                "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
                "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
                "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
                "expirationTime": t.string().optional(),
                "vulnerabilityAssessment": t.proxy(
                    renames["VulnerabilityAssessmentNoteIn"]
                ).optional(),
                "shortDescription": t.string().optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "updateTime": t.string().optional(),
                "package": t.proxy(renames["PackageNoteIn"]).optional(),
                "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
                "image": t.proxy(renames["ImageNoteIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
                "kind": t.string().optional(),
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
                "parent": t.string(),
                "noteId": t.string(),
                "build": t.proxy(renames["BuildNoteIn"]).optional(),
                "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
                "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
                "longDescription": t.string().optional(),
                "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
                "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
                "relatedNoteNames": t.array(t.string()).optional(),
                "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
                "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
                "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
                "expirationTime": t.string().optional(),
                "vulnerabilityAssessment": t.proxy(
                    renames["VulnerabilityAssessmentNoteIn"]
                ).optional(),
                "shortDescription": t.string().optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "updateTime": t.string().optional(),
                "package": t.proxy(renames["PackageNoteIn"]).optional(),
                "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
                "image": t.proxy(renames["ImageNoteIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotesSetIamPolicy"] = containeranalysis.post(
        "v1/{parent}/notes",
        t.struct(
            {
                "parent": t.string(),
                "noteId": t.string(),
                "build": t.proxy(renames["BuildNoteIn"]).optional(),
                "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
                "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
                "longDescription": t.string().optional(),
                "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
                "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
                "relatedNoteNames": t.array(t.string()).optional(),
                "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
                "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
                "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
                "expirationTime": t.string().optional(),
                "vulnerabilityAssessment": t.proxy(
                    renames["VulnerabilityAssessmentNoteIn"]
                ).optional(),
                "shortDescription": t.string().optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "updateTime": t.string().optional(),
                "package": t.proxy(renames["PackageNoteIn"]).optional(),
                "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
                "image": t.proxy(renames["ImageNoteIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
                "kind": t.string().optional(),
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
                "parent": t.string(),
                "noteId": t.string(),
                "build": t.proxy(renames["BuildNoteIn"]).optional(),
                "attestation": t.proxy(renames["AttestationNoteIn"]).optional(),
                "upgrade": t.proxy(renames["UpgradeNoteIn"]).optional(),
                "longDescription": t.string().optional(),
                "dsseAttestation": t.proxy(renames["DSSEAttestationNoteIn"]).optional(),
                "compliance": t.proxy(renames["ComplianceNoteIn"]).optional(),
                "relatedNoteNames": t.array(t.string()).optional(),
                "relatedUrl": t.array(t.proxy(renames["RelatedUrlIn"])).optional(),
                "discovery": t.proxy(renames["DiscoveryNoteIn"]).optional(),
                "sbomReference": t.proxy(renames["SBOMReferenceNoteIn"]).optional(),
                "expirationTime": t.string().optional(),
                "vulnerabilityAssessment": t.proxy(
                    renames["VulnerabilityAssessmentNoteIn"]
                ).optional(),
                "shortDescription": t.string().optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "updateTime": t.string().optional(),
                "package": t.proxy(renames["PackageNoteIn"]).optional(),
                "deployment": t.proxy(renames["DeploymentNoteIn"]).optional(),
                "image": t.proxy(renames["ImageNoteIn"]).optional(),
                "vulnerability": t.proxy(renames["VulnerabilityNoteIn"]).optional(),
                "kind": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string(),
                "pageSize": t.integer().optional(),
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
