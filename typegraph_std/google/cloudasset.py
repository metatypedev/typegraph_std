from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_cloudasset() -> Import:
    cloudasset = HTTPRuntime("https://cloudasset.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudasset_1_ErrorResponse",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceIn": "_cloudasset_2_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceIn",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceOut": "_cloudasset_3_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceOut",
        "GoogleCloudAssetV1GcsDestinationIn": "_cloudasset_4_GoogleCloudAssetV1GcsDestinationIn",
        "GoogleCloudAssetV1GcsDestinationOut": "_cloudasset_5_GoogleCloudAssetV1GcsDestinationOut",
        "EffectiveIamPolicyIn": "_cloudasset_6_EffectiveIamPolicyIn",
        "EffectiveIamPolicyOut": "_cloudasset_7_EffectiveIamPolicyOut",
        "GoogleCloudOrgpolicyV1RestoreDefaultIn": "_cloudasset_8_GoogleCloudOrgpolicyV1RestoreDefaultIn",
        "GoogleCloudOrgpolicyV1RestoreDefaultOut": "_cloudasset_9_GoogleCloudOrgpolicyV1RestoreDefaultOut",
        "GoogleCloudAssetV1GovernedContainerIn": "_cloudasset_10_GoogleCloudAssetV1GovernedContainerIn",
        "GoogleCloudAssetV1GovernedContainerOut": "_cloudasset_11_GoogleCloudAssetV1GovernedContainerOut",
        "GoogleCloudAssetV1DeniedAccessAccessTupleIn": "_cloudasset_12_GoogleCloudAssetV1DeniedAccessAccessTupleIn",
        "GoogleCloudAssetV1DeniedAccessAccessTupleOut": "_cloudasset_13_GoogleCloudAssetV1DeniedAccessAccessTupleOut",
        "AccessSelectorIn": "_cloudasset_14_AccessSelectorIn",
        "AccessSelectorOut": "_cloudasset_15_AccessSelectorOut",
        "GoogleIdentityAccesscontextmanagerV1DevicePolicyIn": "_cloudasset_16_GoogleIdentityAccesscontextmanagerV1DevicePolicyIn",
        "GoogleIdentityAccesscontextmanagerV1DevicePolicyOut": "_cloudasset_17_GoogleIdentityAccesscontextmanagerV1DevicePolicyOut",
        "RelationshipAttributesIn": "_cloudasset_18_RelationshipAttributesIn",
        "RelationshipAttributesOut": "_cloudasset_19_RelationshipAttributesOut",
        "AnalyzeIamPolicyResponseIn": "_cloudasset_20_AnalyzeIamPolicyResponseIn",
        "AnalyzeIamPolicyResponseOut": "_cloudasset_21_AnalyzeIamPolicyResponseOut",
        "GoogleIdentityAccesscontextmanagerV1IngressPolicyIn": "_cloudasset_22_GoogleIdentityAccesscontextmanagerV1IngressPolicyIn",
        "GoogleIdentityAccesscontextmanagerV1IngressPolicyOut": "_cloudasset_23_GoogleIdentityAccesscontextmanagerV1IngressPolicyOut",
        "AuditConfigIn": "_cloudasset_24_AuditConfigIn",
        "AuditConfigOut": "_cloudasset_25_AuditConfigOut",
        "GcsDestinationIn": "_cloudasset_26_GcsDestinationIn",
        "GcsDestinationOut": "_cloudasset_27_GcsDestinationOut",
        "SearchAllIamPoliciesResponseIn": "_cloudasset_28_SearchAllIamPoliciesResponseIn",
        "SearchAllIamPoliciesResponseOut": "_cloudasset_29_SearchAllIamPoliciesResponseOut",
        "TimeWindowIn": "_cloudasset_30_TimeWindowIn",
        "TimeWindowOut": "_cloudasset_31_TimeWindowOut",
        "InventoryIn": "_cloudasset_32_InventoryIn",
        "InventoryOut": "_cloudasset_33_InventoryOut",
        "AnalyzeIamPolicyLongrunningMetadataIn": "_cloudasset_34_AnalyzeIamPolicyLongrunningMetadataIn",
        "AnalyzeIamPolicyLongrunningMetadataOut": "_cloudasset_35_AnalyzeIamPolicyLongrunningMetadataOut",
        "GoogleIdentityAccesscontextmanagerV1ConditionIn": "_cloudasset_36_GoogleIdentityAccesscontextmanagerV1ConditionIn",
        "GoogleIdentityAccesscontextmanagerV1ConditionOut": "_cloudasset_37_GoogleIdentityAccesscontextmanagerV1ConditionOut",
        "AnalyzeOrgPoliciesResponseIn": "_cloudasset_38_AnalyzeOrgPoliciesResponseIn",
        "AnalyzeOrgPoliciesResponseOut": "_cloudasset_39_AnalyzeOrgPoliciesResponseOut",
        "AuditLogConfigIn": "_cloudasset_40_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudasset_41_AuditLogConfigOut",
        "RelatedAssetIn": "_cloudasset_42_RelatedAssetIn",
        "RelatedAssetOut": "_cloudasset_43_RelatedAssetOut",
        "StatusIn": "_cloudasset_44_StatusIn",
        "StatusOut": "_cloudasset_45_StatusOut",
        "GoogleCloudAssetV1DeniedAccessIdentityIn": "_cloudasset_46_GoogleCloudAssetV1DeniedAccessIdentityIn",
        "GoogleCloudAssetV1DeniedAccessIdentityOut": "_cloudasset_47_GoogleCloudAssetV1DeniedAccessIdentityOut",
        "RelatedResourcesIn": "_cloudasset_48_RelatedResourcesIn",
        "RelatedResourcesOut": "_cloudasset_49_RelatedResourcesOut",
        "QueryAssetsResponseIn": "_cloudasset_50_QueryAssetsResponseIn",
        "QueryAssetsResponseOut": "_cloudasset_51_QueryAssetsResponseOut",
        "GoogleCloudAssetV1p7beta1RelationshipAttributesIn": "_cloudasset_52_GoogleCloudAssetV1p7beta1RelationshipAttributesIn",
        "GoogleCloudAssetV1p7beta1RelationshipAttributesOut": "_cloudasset_53_GoogleCloudAssetV1p7beta1RelationshipAttributesOut",
        "GoogleCloudAssetV1RuleIn": "_cloudasset_54_GoogleCloudAssetV1RuleIn",
        "GoogleCloudAssetV1RuleOut": "_cloudasset_55_GoogleCloudAssetV1RuleOut",
        "RelatedAssetsIn": "_cloudasset_56_RelatedAssetsIn",
        "RelatedAssetsOut": "_cloudasset_57_RelatedAssetsOut",
        "GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationIn": "_cloudasset_58_GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationIn",
        "GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationOut": "_cloudasset_59_GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationOut",
        "OrgPolicyResultIn": "_cloudasset_60_OrgPolicyResultIn",
        "OrgPolicyResultOut": "_cloudasset_61_OrgPolicyResultOut",
        "GoogleCloudAssetV1p7beta1ResourceIn": "_cloudasset_62_GoogleCloudAssetV1p7beta1ResourceIn",
        "GoogleCloudAssetV1p7beta1ResourceOut": "_cloudasset_63_GoogleCloudAssetV1p7beta1ResourceOut",
        "AnalyzeOrgPolicyGovernedAssetsResponseIn": "_cloudasset_64_AnalyzeOrgPolicyGovernedAssetsResponseIn",
        "AnalyzeOrgPolicyGovernedAssetsResponseOut": "_cloudasset_65_AnalyzeOrgPolicyGovernedAssetsResponseOut",
        "PubsubDestinationIn": "_cloudasset_66_PubsubDestinationIn",
        "PubsubDestinationOut": "_cloudasset_67_PubsubDestinationOut",
        "TemporalAssetIn": "_cloudasset_68_TemporalAssetIn",
        "TemporalAssetOut": "_cloudasset_69_TemporalAssetOut",
        "QueryAssetsRequestIn": "_cloudasset_70_QueryAssetsRequestIn",
        "QueryAssetsRequestOut": "_cloudasset_71_QueryAssetsRequestOut",
        "PolicyIn": "_cloudasset_72_PolicyIn",
        "PolicyOut": "_cloudasset_73_PolicyOut",
        "MoveAnalysisResultIn": "_cloudasset_74_MoveAnalysisResultIn",
        "MoveAnalysisResultOut": "_cloudasset_75_MoveAnalysisResultOut",
        "QueryAssetsOutputConfigIn": "_cloudasset_76_QueryAssetsOutputConfigIn",
        "QueryAssetsOutputConfigOut": "_cloudasset_77_QueryAssetsOutputConfigOut",
        "TableFieldSchemaIn": "_cloudasset_78_TableFieldSchemaIn",
        "TableFieldSchemaOut": "_cloudasset_79_TableFieldSchemaOut",
        "GoogleIdentityAccesscontextmanagerV1EgressToIn": "_cloudasset_80_GoogleIdentityAccesscontextmanagerV1EgressToIn",
        "GoogleIdentityAccesscontextmanagerV1EgressToOut": "_cloudasset_81_GoogleIdentityAccesscontextmanagerV1EgressToOut",
        "GoogleCloudAssetV1p7beta1AssetIn": "_cloudasset_82_GoogleCloudAssetV1p7beta1AssetIn",
        "GoogleCloudAssetV1p7beta1AssetOut": "_cloudasset_83_GoogleCloudAssetV1p7beta1AssetOut",
        "GoogleIdentityAccesscontextmanagerV1MethodSelectorIn": "_cloudasset_84_GoogleIdentityAccesscontextmanagerV1MethodSelectorIn",
        "GoogleIdentityAccesscontextmanagerV1MethodSelectorOut": "_cloudasset_85_GoogleIdentityAccesscontextmanagerV1MethodSelectorOut",
        "SearchAllResourcesResponseIn": "_cloudasset_86_SearchAllResourcesResponseIn",
        "SearchAllResourcesResponseOut": "_cloudasset_87_SearchAllResourcesResponseOut",
        "IamPolicyAnalysisOutputConfigIn": "_cloudasset_88_IamPolicyAnalysisOutputConfigIn",
        "IamPolicyAnalysisOutputConfigOut": "_cloudasset_89_IamPolicyAnalysisOutputConfigOut",
        "AnalyzeIamPolicyLongrunningRequestIn": "_cloudasset_90_AnalyzeIamPolicyLongrunningRequestIn",
        "AnalyzeIamPolicyLongrunningRequestOut": "_cloudasset_91_AnalyzeIamPolicyLongrunningRequestOut",
        "GoogleCloudOrgpolicyV1ListPolicyIn": "_cloudasset_92_GoogleCloudOrgpolicyV1ListPolicyIn",
        "GoogleCloudOrgpolicyV1ListPolicyOut": "_cloudasset_93_GoogleCloudOrgpolicyV1ListPolicyOut",
        "AnalyzeIamPolicyLongrunningResponseIn": "_cloudasset_94_AnalyzeIamPolicyLongrunningResponseIn",
        "AnalyzeIamPolicyLongrunningResponseOut": "_cloudasset_95_AnalyzeIamPolicyLongrunningResponseOut",
        "GoogleCloudAssetV1p7beta1RelatedAssetsIn": "_cloudasset_96_GoogleCloudAssetV1p7beta1RelatedAssetsIn",
        "GoogleCloudAssetV1p7beta1RelatedAssetsOut": "_cloudasset_97_GoogleCloudAssetV1p7beta1RelatedAssetsOut",
        "GoogleCloudAssetV1AccessControlListIn": "_cloudasset_98_GoogleCloudAssetV1AccessControlListIn",
        "GoogleCloudAssetV1AccessControlListOut": "_cloudasset_99_GoogleCloudAssetV1AccessControlListOut",
        "GoogleCloudAssetV1DeniedAccessAccessIn": "_cloudasset_100_GoogleCloudAssetV1DeniedAccessAccessIn",
        "GoogleCloudAssetV1DeniedAccessAccessOut": "_cloudasset_101_GoogleCloudAssetV1DeniedAccessAccessOut",
        "GoogleCloudOrgpolicyV1PolicyIn": "_cloudasset_102_GoogleCloudOrgpolicyV1PolicyIn",
        "GoogleCloudOrgpolicyV1PolicyOut": "_cloudasset_103_GoogleCloudOrgpolicyV1PolicyOut",
        "WindowsUpdatePackageIn": "_cloudasset_104_WindowsUpdatePackageIn",
        "WindowsUpdatePackageOut": "_cloudasset_105_WindowsUpdatePackageOut",
        "GoogleIdentityAccesscontextmanagerV1IngressSourceIn": "_cloudasset_106_GoogleIdentityAccesscontextmanagerV1IngressSourceIn",
        "GoogleIdentityAccesscontextmanagerV1IngressSourceOut": "_cloudasset_107_GoogleIdentityAccesscontextmanagerV1IngressSourceOut",
        "PermissionsIn": "_cloudasset_108_PermissionsIn",
        "PermissionsOut": "_cloudasset_109_PermissionsOut",
        "GoogleIdentityAccesscontextmanagerV1ApiOperationIn": "_cloudasset_110_GoogleIdentityAccesscontextmanagerV1ApiOperationIn",
        "GoogleIdentityAccesscontextmanagerV1ApiOperationOut": "_cloudasset_111_GoogleIdentityAccesscontextmanagerV1ApiOperationOut",
        "DeniedAccessIn": "_cloudasset_112_DeniedAccessIn",
        "DeniedAccessOut": "_cloudasset_113_DeniedAccessOut",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetIn": "_cloudasset_114_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetIn",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetOut": "_cloudasset_115_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetOut",
        "SoftwarePackageIn": "_cloudasset_116_SoftwarePackageIn",
        "SoftwarePackageOut": "_cloudasset_117_SoftwarePackageOut",
        "OutputConfigIn": "_cloudasset_118_OutputConfigIn",
        "OutputConfigOut": "_cloudasset_119_OutputConfigOut",
        "WindowsQuickFixEngineeringPackageIn": "_cloudasset_120_WindowsQuickFixEngineeringPackageIn",
        "WindowsQuickFixEngineeringPackageOut": "_cloudasset_121_WindowsQuickFixEngineeringPackageOut",
        "BatchGetEffectiveIamPoliciesResponseIn": "_cloudasset_122_BatchGetEffectiveIamPoliciesResponseIn",
        "BatchGetEffectiveIamPoliciesResponseOut": "_cloudasset_123_BatchGetEffectiveIamPoliciesResponseOut",
        "GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn": "_cloudasset_124_GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn",
        "GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut": "_cloudasset_125_GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut",
        "QueryResultIn": "_cloudasset_126_QueryResultIn",
        "QueryResultOut": "_cloudasset_127_QueryResultOut",
        "GoogleCloudAssetV1DeniedAccessResourceIn": "_cloudasset_128_GoogleCloudAssetV1DeniedAccessResourceIn",
        "GoogleCloudAssetV1DeniedAccessResourceOut": "_cloudasset_129_GoogleCloudAssetV1DeniedAccessResourceOut",
        "GoogleCloudAssetV1BooleanConstraintIn": "_cloudasset_130_GoogleCloudAssetV1BooleanConstraintIn",
        "GoogleCloudAssetV1BooleanConstraintOut": "_cloudasset_131_GoogleCloudAssetV1BooleanConstraintOut",
        "IamPolicyAnalysisResultIn": "_cloudasset_132_IamPolicyAnalysisResultIn",
        "IamPolicyAnalysisResultOut": "_cloudasset_133_IamPolicyAnalysisResultOut",
        "GoogleIdentityAccesscontextmanagerV1IngressFromIn": "_cloudasset_134_GoogleIdentityAccesscontextmanagerV1IngressFromIn",
        "GoogleIdentityAccesscontextmanagerV1IngressFromOut": "_cloudasset_135_GoogleIdentityAccesscontextmanagerV1IngressFromOut",
        "FeedOutputConfigIn": "_cloudasset_136_FeedOutputConfigIn",
        "FeedOutputConfigOut": "_cloudasset_137_FeedOutputConfigOut",
        "PolicyInfoIn": "_cloudasset_138_PolicyInfoIn",
        "PolicyInfoOut": "_cloudasset_139_PolicyInfoOut",
        "OptionsIn": "_cloudasset_140_OptionsIn",
        "OptionsOut": "_cloudasset_141_OptionsOut",
        "IdentitySelectorIn": "_cloudasset_142_IdentitySelectorIn",
        "IdentitySelectorOut": "_cloudasset_143_IdentitySelectorOut",
        "UpdateFeedRequestIn": "_cloudasset_144_UpdateFeedRequestIn",
        "UpdateFeedRequestOut": "_cloudasset_145_UpdateFeedRequestOut",
        "VersionedPackageIn": "_cloudasset_146_VersionedPackageIn",
        "VersionedPackageOut": "_cloudasset_147_VersionedPackageOut",
        "WindowsUpdateCategoryIn": "_cloudasset_148_WindowsUpdateCategoryIn",
        "WindowsUpdateCategoryOut": "_cloudasset_149_WindowsUpdateCategoryOut",
        "AnalyzeMoveResponseIn": "_cloudasset_150_AnalyzeMoveResponseIn",
        "AnalyzeMoveResponseOut": "_cloudasset_151_AnalyzeMoveResponseOut",
        "GoogleIdentityAccesscontextmanagerV1EgressFromIn": "_cloudasset_152_GoogleIdentityAccesscontextmanagerV1EgressFromIn",
        "GoogleIdentityAccesscontextmanagerV1EgressFromOut": "_cloudasset_153_GoogleIdentityAccesscontextmanagerV1EgressFromOut",
        "CreateFeedRequestIn": "_cloudasset_154_CreateFeedRequestIn",
        "CreateFeedRequestOut": "_cloudasset_155_CreateFeedRequestOut",
        "AnalyzerOrgPolicyIn": "_cloudasset_156_AnalyzerOrgPolicyIn",
        "AnalyzerOrgPolicyOut": "_cloudasset_157_AnalyzerOrgPolicyOut",
        "GoogleCloudAssetV1p7beta1RelatedAssetIn": "_cloudasset_158_GoogleCloudAssetV1p7beta1RelatedAssetIn",
        "GoogleCloudAssetV1p7beta1RelatedAssetOut": "_cloudasset_159_GoogleCloudAssetV1p7beta1RelatedAssetOut",
        "GoogleCloudAssetV1AccessIn": "_cloudasset_160_GoogleCloudAssetV1AccessIn",
        "GoogleCloudAssetV1AccessOut": "_cloudasset_161_GoogleCloudAssetV1AccessOut",
        "GoogleCloudAssetV1IdentityListIn": "_cloudasset_162_GoogleCloudAssetV1IdentityListIn",
        "GoogleCloudAssetV1IdentityListOut": "_cloudasset_163_GoogleCloudAssetV1IdentityListOut",
        "ResourceIn": "_cloudasset_164_ResourceIn",
        "ResourceOut": "_cloudasset_165_ResourceOut",
        "ListAssetsResponseIn": "_cloudasset_166_ListAssetsResponseIn",
        "ListAssetsResponseOut": "_cloudasset_167_ListAssetsResponseOut",
        "GoogleCloudOrgpolicyV1BooleanPolicyIn": "_cloudasset_168_GoogleCloudOrgpolicyV1BooleanPolicyIn",
        "GoogleCloudOrgpolicyV1BooleanPolicyOut": "_cloudasset_169_GoogleCloudOrgpolicyV1BooleanPolicyOut",
        "IamPolicyAnalysisQueryIn": "_cloudasset_170_IamPolicyAnalysisQueryIn",
        "IamPolicyAnalysisQueryOut": "_cloudasset_171_IamPolicyAnalysisQueryOut",
        "PartitionSpecIn": "_cloudasset_172_PartitionSpecIn",
        "PartitionSpecOut": "_cloudasset_173_PartitionSpecOut",
        "ResourceSelectorIn": "_cloudasset_174_ResourceSelectorIn",
        "ResourceSelectorOut": "_cloudasset_175_ResourceSelectorOut",
        "ExprIn": "_cloudasset_176_ExprIn",
        "ExprOut": "_cloudasset_177_ExprOut",
        "GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn": "_cloudasset_178_GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn",
        "GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut": "_cloudasset_179_GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut",
        "GoogleIdentityAccesscontextmanagerV1AccessLevelIn": "_cloudasset_180_GoogleIdentityAccesscontextmanagerV1AccessLevelIn",
        "GoogleIdentityAccesscontextmanagerV1AccessLevelOut": "_cloudasset_181_GoogleIdentityAccesscontextmanagerV1AccessLevelOut",
        "ConditionEvaluationIn": "_cloudasset_182_ConditionEvaluationIn",
        "ConditionEvaluationOut": "_cloudasset_183_ConditionEvaluationOut",
        "GoogleCloudAssetV1ConstraintIn": "_cloudasset_184_GoogleCloudAssetV1ConstraintIn",
        "GoogleCloudAssetV1ConstraintOut": "_cloudasset_185_GoogleCloudAssetV1ConstraintOut",
        "GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesIn": "_cloudasset_186_GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesIn",
        "GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesOut": "_cloudasset_187_GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesOut",
        "ExportAssetsRequestIn": "_cloudasset_188_ExportAssetsRequestIn",
        "ExportAssetsRequestOut": "_cloudasset_189_ExportAssetsRequestOut",
        "IamPolicyAnalysisStateIn": "_cloudasset_190_IamPolicyAnalysisStateIn",
        "IamPolicyAnalysisStateOut": "_cloudasset_191_IamPolicyAnalysisStateOut",
        "GoogleCloudAssetV1CustomConstraintIn": "_cloudasset_192_GoogleCloudAssetV1CustomConstraintIn",
        "GoogleCloudAssetV1CustomConstraintOut": "_cloudasset_193_GoogleCloudAssetV1CustomConstraintOut",
        "AnalyzerOrgPolicyConstraintIn": "_cloudasset_194_AnalyzerOrgPolicyConstraintIn",
        "AnalyzerOrgPolicyConstraintOut": "_cloudasset_195_AnalyzerOrgPolicyConstraintOut",
        "GoogleCloudAssetV1DeniedAccessDenyDetailIn": "_cloudasset_196_GoogleCloudAssetV1DeniedAccessDenyDetailIn",
        "GoogleCloudAssetV1DeniedAccessDenyDetailOut": "_cloudasset_197_GoogleCloudAssetV1DeniedAccessDenyDetailOut",
        "GoogleIdentityAccesscontextmanagerV1AccessPolicyIn": "_cloudasset_198_GoogleIdentityAccesscontextmanagerV1AccessPolicyIn",
        "GoogleIdentityAccesscontextmanagerV1AccessPolicyOut": "_cloudasset_199_GoogleIdentityAccesscontextmanagerV1AccessPolicyOut",
        "BigQueryDestinationIn": "_cloudasset_200_BigQueryDestinationIn",
        "BigQueryDestinationOut": "_cloudasset_201_BigQueryDestinationOut",
        "OsInfoIn": "_cloudasset_202_OsInfoIn",
        "OsInfoOut": "_cloudasset_203_OsInfoOut",
        "AnalyzeOrgPolicyGovernedContainersResponseIn": "_cloudasset_204_AnalyzeOrgPolicyGovernedContainersResponseIn",
        "AnalyzeOrgPolicyGovernedContainersResponseOut": "_cloudasset_205_AnalyzeOrgPolicyGovernedContainersResponseOut",
        "FeedIn": "_cloudasset_206_FeedIn",
        "FeedOut": "_cloudasset_207_FeedOut",
        "BindingIn": "_cloudasset_208_BindingIn",
        "BindingOut": "_cloudasset_209_BindingOut",
        "GoogleIdentityAccesscontextmanagerV1CustomLevelIn": "_cloudasset_210_GoogleIdentityAccesscontextmanagerV1CustomLevelIn",
        "GoogleIdentityAccesscontextmanagerV1CustomLevelOut": "_cloudasset_211_GoogleIdentityAccesscontextmanagerV1CustomLevelOut",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyIn": "_cloudasset_212_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyIn",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyOut": "_cloudasset_213_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyOut",
        "RelatedResourceIn": "_cloudasset_214_RelatedResourceIn",
        "RelatedResourceOut": "_cloudasset_215_RelatedResourceOut",
        "AssetIn": "_cloudasset_216_AssetIn",
        "AssetOut": "_cloudasset_217_AssetOut",
        "ListSavedQueriesResponseIn": "_cloudasset_218_ListSavedQueriesResponseIn",
        "ListSavedQueriesResponseOut": "_cloudasset_219_ListSavedQueriesResponseOut",
        "GoogleCloudAssetV1ListConstraintIn": "_cloudasset_220_GoogleCloudAssetV1ListConstraintIn",
        "GoogleCloudAssetV1ListConstraintOut": "_cloudasset_221_GoogleCloudAssetV1ListConstraintOut",
        "GoogleCloudAssetV1StringValuesIn": "_cloudasset_222_GoogleCloudAssetV1StringValuesIn",
        "GoogleCloudAssetV1StringValuesOut": "_cloudasset_223_GoogleCloudAssetV1StringValuesOut",
        "ExplanationIn": "_cloudasset_224_ExplanationIn",
        "ExplanationOut": "_cloudasset_225_ExplanationOut",
        "GoogleIdentityAccesscontextmanagerV1OsConstraintIn": "_cloudasset_226_GoogleIdentityAccesscontextmanagerV1OsConstraintIn",
        "GoogleIdentityAccesscontextmanagerV1OsConstraintOut": "_cloudasset_227_GoogleIdentityAccesscontextmanagerV1OsConstraintOut",
        "GoogleCloudAssetV1BigQueryDestinationIn": "_cloudasset_228_GoogleCloudAssetV1BigQueryDestinationIn",
        "GoogleCloudAssetV1BigQueryDestinationOut": "_cloudasset_229_GoogleCloudAssetV1BigQueryDestinationOut",
        "GoogleIdentityAccesscontextmanagerV1BasicLevelIn": "_cloudasset_230_GoogleIdentityAccesscontextmanagerV1BasicLevelIn",
        "GoogleIdentityAccesscontextmanagerV1BasicLevelOut": "_cloudasset_231_GoogleIdentityAccesscontextmanagerV1BasicLevelOut",
        "AttachedResourceIn": "_cloudasset_232_AttachedResourceIn",
        "AttachedResourceOut": "_cloudasset_233_AttachedResourceOut",
        "TableSchemaIn": "_cloudasset_234_TableSchemaIn",
        "TableSchemaOut": "_cloudasset_235_TableSchemaOut",
        "ItemIn": "_cloudasset_236_ItemIn",
        "ItemOut": "_cloudasset_237_ItemOut",
        "IamPolicyAnalysisIn": "_cloudasset_238_IamPolicyAnalysisIn",
        "IamPolicyAnalysisOut": "_cloudasset_239_IamPolicyAnalysisOut",
        "MoveAnalysisIn": "_cloudasset_240_MoveAnalysisIn",
        "MoveAnalysisOut": "_cloudasset_241_MoveAnalysisOut",
        "GoogleCloudAssetV1EdgeIn": "_cloudasset_242_GoogleCloudAssetV1EdgeIn",
        "GoogleCloudAssetV1EdgeOut": "_cloudasset_243_GoogleCloudAssetV1EdgeOut",
        "VersionedResourceIn": "_cloudasset_244_VersionedResourceIn",
        "VersionedResourceOut": "_cloudasset_245_VersionedResourceOut",
        "WindowsApplicationIn": "_cloudasset_246_WindowsApplicationIn",
        "WindowsApplicationOut": "_cloudasset_247_WindowsApplicationOut",
        "EmptyIn": "_cloudasset_248_EmptyIn",
        "EmptyOut": "_cloudasset_249_EmptyOut",
        "QueryContentIn": "_cloudasset_250_QueryContentIn",
        "QueryContentOut": "_cloudasset_251_QueryContentOut",
        "MoveImpactIn": "_cloudasset_252_MoveImpactIn",
        "MoveImpactOut": "_cloudasset_253_MoveImpactOut",
        "DateIn": "_cloudasset_254_DateIn",
        "DateOut": "_cloudasset_255_DateOut",
        "GoogleCloudAssetV1IdentityIn": "_cloudasset_256_GoogleCloudAssetV1IdentityIn",
        "GoogleCloudAssetV1IdentityOut": "_cloudasset_257_GoogleCloudAssetV1IdentityOut",
        "ConditionContextIn": "_cloudasset_258_ConditionContextIn",
        "ConditionContextOut": "_cloudasset_259_ConditionContextOut",
        "ListFeedsResponseIn": "_cloudasset_260_ListFeedsResponseIn",
        "ListFeedsResponseOut": "_cloudasset_261_ListFeedsResponseOut",
        "GoogleCloudAssetV1ResourceIn": "_cloudasset_262_GoogleCloudAssetV1ResourceIn",
        "GoogleCloudAssetV1ResourceOut": "_cloudasset_263_GoogleCloudAssetV1ResourceOut",
        "OperationIn": "_cloudasset_264_OperationIn",
        "OperationOut": "_cloudasset_265_OperationOut",
        "IamPolicySearchResultIn": "_cloudasset_266_IamPolicySearchResultIn",
        "IamPolicySearchResultOut": "_cloudasset_267_IamPolicySearchResultOut",
        "BatchGetAssetsHistoryResponseIn": "_cloudasset_268_BatchGetAssetsHistoryResponseIn",
        "BatchGetAssetsHistoryResponseOut": "_cloudasset_269_BatchGetAssetsHistoryResponseOut",
        "GoogleIamV2DenyRuleIn": "_cloudasset_270_GoogleIamV2DenyRuleIn",
        "GoogleIamV2DenyRuleOut": "_cloudasset_271_GoogleIamV2DenyRuleOut",
        "SavedQueryIn": "_cloudasset_272_SavedQueryIn",
        "SavedQueryOut": "_cloudasset_273_SavedQueryOut",
        "ZypperPatchIn": "_cloudasset_274_ZypperPatchIn",
        "ZypperPatchOut": "_cloudasset_275_ZypperPatchOut",
        "GoogleIdentityAccesscontextmanagerV1EgressPolicyIn": "_cloudasset_276_GoogleIdentityAccesscontextmanagerV1EgressPolicyIn",
        "GoogleIdentityAccesscontextmanagerV1EgressPolicyOut": "_cloudasset_277_GoogleIdentityAccesscontextmanagerV1EgressPolicyOut",
        "GoogleIdentityAccesscontextmanagerV1IngressToIn": "_cloudasset_278_GoogleIdentityAccesscontextmanagerV1IngressToIn",
        "GoogleIdentityAccesscontextmanagerV1IngressToOut": "_cloudasset_279_GoogleIdentityAccesscontextmanagerV1IngressToOut",
        "ResourceSearchResultIn": "_cloudasset_280_ResourceSearchResultIn",
        "ResourceSearchResultOut": "_cloudasset_281_ResourceSearchResultOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types[
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceIn"
    ] = t.struct(
        {
            "folders": t.array(t.string()).optional(),
            "project": t.string().optional(),
            "parent": t.string().optional(),
            "organization": t.string().optional(),
            "fullResourceName": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceIn"
        ]
    )
    types[
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceOut"
    ] = t.struct(
        {
            "folders": t.array(t.string()).optional(),
            "project": t.string().optional(),
            "parent": t.string().optional(),
            "organization": t.string().optional(),
            "fullResourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceOut"
        ]
    )
    types["GoogleCloudAssetV1GcsDestinationIn"] = t.struct({"uri": t.string()}).named(
        renames["GoogleCloudAssetV1GcsDestinationIn"]
    )
    types["GoogleCloudAssetV1GcsDestinationOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudAssetV1GcsDestinationOut"])
    types["EffectiveIamPolicyIn"] = t.struct(
        {
            "policies": t.array(t.proxy(renames["PolicyInfoIn"])).optional(),
            "fullResourceName": t.string().optional(),
        }
    ).named(renames["EffectiveIamPolicyIn"])
    types["EffectiveIamPolicyOut"] = t.struct(
        {
            "policies": t.array(t.proxy(renames["PolicyInfoOut"])).optional(),
            "fullResourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EffectiveIamPolicyOut"])
    types["GoogleCloudOrgpolicyV1RestoreDefaultIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudOrgpolicyV1RestoreDefaultIn"])
    types["GoogleCloudOrgpolicyV1RestoreDefaultOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudOrgpolicyV1RestoreDefaultOut"])
    types["GoogleCloudAssetV1GovernedContainerIn"] = t.struct(
        {
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyIn"]).optional(),
            "parent": t.string().optional(),
            "fullResourceName": t.string().optional(),
            "policyBundle": t.array(t.proxy(renames["AnalyzerOrgPolicyIn"])).optional(),
        }
    ).named(renames["GoogleCloudAssetV1GovernedContainerIn"])
    types["GoogleCloudAssetV1GovernedContainerOut"] = t.struct(
        {
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyOut"]).optional(),
            "parent": t.string().optional(),
            "fullResourceName": t.string().optional(),
            "policyBundle": t.array(
                t.proxy(renames["AnalyzerOrgPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1GovernedContainerOut"])
    types["GoogleCloudAssetV1DeniedAccessAccessTupleIn"] = t.struct(
        {
            "resource": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessResourceIn"]
            ).optional(),
            "identity": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessIdentityIn"]
            ).optional(),
            "access": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessAccessIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessAccessTupleIn"])
    types["GoogleCloudAssetV1DeniedAccessAccessTupleOut"] = t.struct(
        {
            "resource": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessResourceOut"]
            ).optional(),
            "identity": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessIdentityOut"]
            ).optional(),
            "access": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessAccessOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessAccessTupleOut"])
    types["AccessSelectorIn"] = t.struct(
        {
            "roles": t.array(t.string()).optional(),
            "permissions": t.array(t.string()).optional(),
        }
    ).named(renames["AccessSelectorIn"])
    types["AccessSelectorOut"] = t.struct(
        {
            "roles": t.array(t.string()).optional(),
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessSelectorOut"])
    types["GoogleIdentityAccesscontextmanagerV1DevicePolicyIn"] = t.struct(
        {
            "allowedEncryptionStatuses": t.array(t.string()).optional(),
            "requireScreenlock": t.boolean().optional(),
            "osConstraints": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1OsConstraintIn"])
            ).optional(),
            "requireAdminApproval": t.boolean().optional(),
            "allowedDeviceManagementLevels": t.array(t.string()).optional(),
            "requireCorpOwned": t.boolean().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1DevicePolicyIn"])
    types["GoogleIdentityAccesscontextmanagerV1DevicePolicyOut"] = t.struct(
        {
            "allowedEncryptionStatuses": t.array(t.string()).optional(),
            "requireScreenlock": t.boolean().optional(),
            "osConstraints": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1OsConstraintOut"])
            ).optional(),
            "requireAdminApproval": t.boolean().optional(),
            "allowedDeviceManagementLevels": t.array(t.string()).optional(),
            "requireCorpOwned": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1DevicePolicyOut"])
    types["RelationshipAttributesIn"] = t.struct(
        {
            "sourceResourceType": t.string().optional(),
            "type": t.string().optional(),
            "targetResourceType": t.string().optional(),
            "action": t.string().optional(),
        }
    ).named(renames["RelationshipAttributesIn"])
    types["RelationshipAttributesOut"] = t.struct(
        {
            "sourceResourceType": t.string().optional(),
            "type": t.string().optional(),
            "targetResourceType": t.string().optional(),
            "action": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationshipAttributesOut"])
    types["AnalyzeIamPolicyResponseIn"] = t.struct(
        {
            "serviceAccountImpersonationAnalysis": t.array(
                t.proxy(renames["IamPolicyAnalysisIn"])
            ).optional(),
            "fullyExplored": t.boolean().optional(),
            "mainAnalysis": t.proxy(renames["IamPolicyAnalysisIn"]).optional(),
        }
    ).named(renames["AnalyzeIamPolicyResponseIn"])
    types["AnalyzeIamPolicyResponseOut"] = t.struct(
        {
            "serviceAccountImpersonationAnalysis": t.array(
                t.proxy(renames["IamPolicyAnalysisOut"])
            ).optional(),
            "fullyExplored": t.boolean().optional(),
            "mainAnalysis": t.proxy(renames["IamPolicyAnalysisOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeIamPolicyResponseOut"])
    types["GoogleIdentityAccesscontextmanagerV1IngressPolicyIn"] = t.struct(
        {
            "ingressTo": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1IngressToIn"]
            ).optional(),
            "ingressFrom": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1IngressFromIn"]
            ).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1IngressPolicyIn"])
    types["GoogleIdentityAccesscontextmanagerV1IngressPolicyOut"] = t.struct(
        {
            "ingressTo": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1IngressToOut"]
            ).optional(),
            "ingressFrom": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1IngressFromOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1IngressPolicyOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["GcsDestinationIn"] = t.struct(
        {"uri": t.string().optional(), "uriPrefix": t.string().optional()}
    ).named(renames["GcsDestinationIn"])
    types["GcsDestinationOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "uriPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsDestinationOut"])
    types["SearchAllIamPoliciesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "results": t.array(t.proxy(renames["IamPolicySearchResultIn"])).optional(),
        }
    ).named(renames["SearchAllIamPoliciesResponseIn"])
    types["SearchAllIamPoliciesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "results": t.array(t.proxy(renames["IamPolicySearchResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchAllIamPoliciesResponseOut"])
    types["TimeWindowIn"] = t.struct(
        {"endTime": t.string().optional(), "startTime": t.string().optional()}
    ).named(renames["TimeWindowIn"])
    types["TimeWindowOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeWindowOut"])
    types["InventoryIn"] = t.struct(
        {
            "items": t.struct({"_": t.string().optional()}).optional(),
            "osInfo": t.proxy(renames["OsInfoIn"]).optional(),
        }
    ).named(renames["InventoryIn"])
    types["InventoryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "items": t.struct({"_": t.string().optional()}).optional(),
            "osInfo": t.proxy(renames["OsInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryOut"])
    types["AnalyzeIamPolicyLongrunningMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AnalyzeIamPolicyLongrunningMetadataIn"])
    types["AnalyzeIamPolicyLongrunningMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeIamPolicyLongrunningMetadataOut"])
    types["GoogleIdentityAccesscontextmanagerV1ConditionIn"] = t.struct(
        {
            "ipSubnetworks": t.array(t.string()).optional(),
            "regions": t.array(t.string()).optional(),
            "devicePolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1DevicePolicyIn"]
            ).optional(),
            "negate": t.boolean().optional(),
            "members": t.array(t.string()).optional(),
            "requiredAccessLevels": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ConditionIn"])
    types["GoogleIdentityAccesscontextmanagerV1ConditionOut"] = t.struct(
        {
            "ipSubnetworks": t.array(t.string()).optional(),
            "regions": t.array(t.string()).optional(),
            "devicePolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1DevicePolicyOut"]
            ).optional(),
            "negate": t.boolean().optional(),
            "members": t.array(t.string()).optional(),
            "requiredAccessLevels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ConditionOut"])
    types["AnalyzeOrgPoliciesResponseIn"] = t.struct(
        {
            "orgPolicyResults": t.array(
                t.proxy(renames["OrgPolicyResultIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "constraint": t.proxy(renames["AnalyzerOrgPolicyConstraintIn"]).optional(),
        }
    ).named(renames["AnalyzeOrgPoliciesResponseIn"])
    types["AnalyzeOrgPoliciesResponseOut"] = t.struct(
        {
            "orgPolicyResults": t.array(
                t.proxy(renames["OrgPolicyResultOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "constraint": t.proxy(renames["AnalyzerOrgPolicyConstraintOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeOrgPoliciesResponseOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["RelatedAssetIn"] = t.struct(
        {
            "relationshipType": t.string().optional(),
            "ancestors": t.array(t.string()).optional(),
            "assetType": t.string().optional(),
            "asset": t.string().optional(),
        }
    ).named(renames["RelatedAssetIn"])
    types["RelatedAssetOut"] = t.struct(
        {
            "relationshipType": t.string().optional(),
            "ancestors": t.array(t.string()).optional(),
            "assetType": t.string().optional(),
            "asset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelatedAssetOut"])
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
    types["GoogleCloudAssetV1DeniedAccessIdentityIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["GoogleCloudAssetV1DeniedAccessIdentityIn"])
    types["GoogleCloudAssetV1DeniedAccessIdentityOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessIdentityOut"])
    types["RelatedResourcesIn"] = t.struct(
        {"relatedResources": t.array(t.proxy(renames["RelatedResourceIn"])).optional()}
    ).named(renames["RelatedResourcesIn"])
    types["RelatedResourcesOut"] = t.struct(
        {
            "relatedResources": t.array(
                t.proxy(renames["RelatedResourceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelatedResourcesOut"])
    types["QueryAssetsResponseIn"] = t.struct(
        {
            "outputConfig": t.proxy(renames["QueryAssetsOutputConfigIn"]).optional(),
            "queryResult": t.proxy(renames["QueryResultIn"]).optional(),
            "jobReference": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["QueryAssetsResponseIn"])
    types["QueryAssetsResponseOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["QueryAssetsOutputConfigOut"]).optional(),
            "queryResult": t.proxy(renames["QueryResultOut"]).optional(),
            "jobReference": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["QueryAssetsResponseOut"])
    types["GoogleCloudAssetV1p7beta1RelationshipAttributesIn"] = t.struct(
        {
            "type": t.string().optional(),
            "action": t.string().optional(),
            "targetResourceType": t.string().optional(),
            "sourceResourceType": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1RelationshipAttributesIn"])
    types["GoogleCloudAssetV1p7beta1RelationshipAttributesOut"] = t.struct(
        {
            "type": t.string().optional(),
            "action": t.string().optional(),
            "targetResourceType": t.string().optional(),
            "sourceResourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1RelationshipAttributesOut"])
    types["GoogleCloudAssetV1RuleIn"] = t.struct(
        {
            "enforce": t.boolean().optional(),
            "values": t.proxy(renames["GoogleCloudAssetV1StringValuesIn"]).optional(),
            "denyAll": t.boolean().optional(),
            "allowAll": t.boolean().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1RuleIn"])
    types["GoogleCloudAssetV1RuleOut"] = t.struct(
        {
            "enforce": t.boolean().optional(),
            "values": t.proxy(renames["GoogleCloudAssetV1StringValuesOut"]).optional(),
            "denyAll": t.boolean().optional(),
            "allowAll": t.boolean().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1RuleOut"])
    types["RelatedAssetsIn"] = t.struct(
        {
            "assets": t.array(t.proxy(renames["RelatedAssetIn"])).optional(),
            "relationshipAttributes": t.proxy(
                renames["RelationshipAttributesIn"]
            ).optional(),
        }
    ).named(renames["RelatedAssetsIn"])
    types["RelatedAssetsOut"] = t.struct(
        {
            "assets": t.array(t.proxy(renames["RelatedAssetOut"])).optional(),
            "relationshipAttributes": t.proxy(
                renames["RelationshipAttributesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelatedAssetsOut"])
    types["GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationIn"] = t.struct(
        {
            "writeDisposition": t.string().optional(),
            "table": t.string(),
            "dataset": t.string(),
        }
    ).named(renames["GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationIn"])
    types["GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationOut"] = t.struct(
        {
            "writeDisposition": t.string().optional(),
            "table": t.string(),
            "dataset": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationOut"])
    types["OrgPolicyResultIn"] = t.struct(
        {
            "policyBundle": t.array(t.proxy(renames["AnalyzerOrgPolicyIn"])).optional(),
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyIn"]).optional(),
        }
    ).named(renames["OrgPolicyResultIn"])
    types["OrgPolicyResultOut"] = t.struct(
        {
            "policyBundle": t.array(
                t.proxy(renames["AnalyzerOrgPolicyOut"])
            ).optional(),
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrgPolicyResultOut"])
    types["GoogleCloudAssetV1p7beta1ResourceIn"] = t.struct(
        {
            "parent": t.string().optional(),
            "discoveryDocumentUri": t.string().optional(),
            "location": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "resourceUrl": t.string().optional(),
            "discoveryName": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1ResourceIn"])
    types["GoogleCloudAssetV1p7beta1ResourceOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "discoveryDocumentUri": t.string().optional(),
            "location": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "resourceUrl": t.string().optional(),
            "discoveryName": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1ResourceOut"])
    types["AnalyzeOrgPolicyGovernedAssetsResponseIn"] = t.struct(
        {
            "constraint": t.proxy(renames["AnalyzerOrgPolicyConstraintIn"]).optional(),
            "governedAssets": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetIn"
                    ]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["AnalyzeOrgPolicyGovernedAssetsResponseIn"])
    types["AnalyzeOrgPolicyGovernedAssetsResponseOut"] = t.struct(
        {
            "constraint": t.proxy(renames["AnalyzerOrgPolicyConstraintOut"]).optional(),
            "governedAssets": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetOut"
                    ]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeOrgPolicyGovernedAssetsResponseOut"])
    types["PubsubDestinationIn"] = t.struct({"topic": t.string().optional()}).named(
        renames["PubsubDestinationIn"]
    )
    types["PubsubDestinationOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubDestinationOut"])
    types["TemporalAssetIn"] = t.struct(
        {
            "asset": t.proxy(renames["AssetIn"]).optional(),
            "deleted": t.boolean().optional(),
            "window": t.proxy(renames["TimeWindowIn"]).optional(),
            "priorAssetState": t.string().optional(),
            "priorAsset": t.proxy(renames["AssetIn"]).optional(),
        }
    ).named(renames["TemporalAssetIn"])
    types["TemporalAssetOut"] = t.struct(
        {
            "asset": t.proxy(renames["AssetOut"]).optional(),
            "deleted": t.boolean().optional(),
            "window": t.proxy(renames["TimeWindowOut"]).optional(),
            "priorAssetState": t.string().optional(),
            "priorAsset": t.proxy(renames["AssetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TemporalAssetOut"])
    types["QueryAssetsRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "readTime": t.string().optional(),
            "timeout": t.string().optional(),
            "statement": t.string().optional(),
            "readTimeWindow": t.proxy(renames["TimeWindowIn"]).optional(),
            "outputConfig": t.proxy(renames["QueryAssetsOutputConfigIn"]).optional(),
            "jobReference": t.string().optional(),
        }
    ).named(renames["QueryAssetsRequestIn"])
    types["QueryAssetsRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "readTime": t.string().optional(),
            "timeout": t.string().optional(),
            "statement": t.string().optional(),
            "readTimeWindow": t.proxy(renames["TimeWindowOut"]).optional(),
            "outputConfig": t.proxy(renames["QueryAssetsOutputConfigOut"]).optional(),
            "jobReference": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryAssetsRequestOut"])
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["MoveAnalysisResultIn"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["MoveImpactIn"])).optional(),
            "blockers": t.array(t.proxy(renames["MoveImpactIn"])).optional(),
        }
    ).named(renames["MoveAnalysisResultIn"])
    types["MoveAnalysisResultOut"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["MoveImpactOut"])).optional(),
            "blockers": t.array(t.proxy(renames["MoveImpactOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveAnalysisResultOut"])
    types["QueryAssetsOutputConfigIn"] = t.struct(
        {
            "bigqueryDestination": t.proxy(
                renames[
                    "GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationIn"
                ]
            ).optional()
        }
    ).named(renames["QueryAssetsOutputConfigIn"])
    types["QueryAssetsOutputConfigOut"] = t.struct(
        {
            "bigqueryDestination": t.proxy(
                renames[
                    "GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryAssetsOutputConfigOut"])
    types["TableFieldSchemaIn"] = t.struct(
        {
            "mode": t.string().optional(),
            "field": t.string().optional(),
            "type": t.string().optional(),
            "fields": t.array(t.proxy(renames["TableFieldSchemaIn"])).optional(),
        }
    ).named(renames["TableFieldSchemaIn"])
    types["TableFieldSchemaOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "field": t.string().optional(),
            "type": t.string().optional(),
            "fields": t.array(t.proxy(renames["TableFieldSchemaOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableFieldSchemaOut"])
    types["GoogleIdentityAccesscontextmanagerV1EgressToIn"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1ApiOperationIn"])
            ).optional(),
            "externalResources": t.array(t.string()).optional(),
            "resources": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1EgressToIn"])
    types["GoogleIdentityAccesscontextmanagerV1EgressToOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1ApiOperationOut"])
            ).optional(),
            "externalResources": t.array(t.string()).optional(),
            "resources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1EgressToOut"])
    types["GoogleCloudAssetV1p7beta1AssetIn"] = t.struct(
        {
            "resource": t.proxy(
                renames["GoogleCloudAssetV1p7beta1ResourceIn"]
            ).optional(),
            "orgPolicy": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV1PolicyIn"])
            ).optional(),
            "ancestors": t.array(t.string()).optional(),
            "accessLevel": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessLevelIn"]
            ).optional(),
            "updateTime": t.string().optional(),
            "iamPolicy": t.proxy(renames["PolicyIn"]).optional(),
            "accessPolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyIn"]
            ).optional(),
            "servicePerimeter": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn"]
            ).optional(),
            "name": t.string().optional(),
            "relatedAssets": t.proxy(
                renames["GoogleCloudAssetV1p7beta1RelatedAssetsIn"]
            ).optional(),
            "assetType": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1AssetIn"])
    types["GoogleCloudAssetV1p7beta1AssetOut"] = t.struct(
        {
            "resource": t.proxy(
                renames["GoogleCloudAssetV1p7beta1ResourceOut"]
            ).optional(),
            "orgPolicy": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV1PolicyOut"])
            ).optional(),
            "ancestors": t.array(t.string()).optional(),
            "accessLevel": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessLevelOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "iamPolicy": t.proxy(renames["PolicyOut"]).optional(),
            "accessPolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyOut"]
            ).optional(),
            "servicePerimeter": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut"]
            ).optional(),
            "name": t.string().optional(),
            "relatedAssets": t.proxy(
                renames["GoogleCloudAssetV1p7beta1RelatedAssetsOut"]
            ).optional(),
            "assetType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1AssetOut"])
    types["GoogleIdentityAccesscontextmanagerV1MethodSelectorIn"] = t.struct(
        {"permission": t.string().optional(), "method": t.string().optional()}
    ).named(renames["GoogleIdentityAccesscontextmanagerV1MethodSelectorIn"])
    types["GoogleIdentityAccesscontextmanagerV1MethodSelectorOut"] = t.struct(
        {
            "permission": t.string().optional(),
            "method": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1MethodSelectorOut"])
    types["SearchAllResourcesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "results": t.array(t.proxy(renames["ResourceSearchResultIn"])).optional(),
        }
    ).named(renames["SearchAllResourcesResponseIn"])
    types["SearchAllResourcesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "results": t.array(t.proxy(renames["ResourceSearchResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchAllResourcesResponseOut"])
    types["IamPolicyAnalysisOutputConfigIn"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudAssetV1GcsDestinationIn"]
            ).optional(),
            "bigqueryDestination": t.proxy(
                renames["GoogleCloudAssetV1BigQueryDestinationIn"]
            ).optional(),
        }
    ).named(renames["IamPolicyAnalysisOutputConfigIn"])
    types["IamPolicyAnalysisOutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudAssetV1GcsDestinationOut"]
            ).optional(),
            "bigqueryDestination": t.proxy(
                renames["GoogleCloudAssetV1BigQueryDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisOutputConfigOut"])
    types["AnalyzeIamPolicyLongrunningRequestIn"] = t.struct(
        {
            "outputConfig": t.proxy(renames["IamPolicyAnalysisOutputConfigIn"]),
            "savedAnalysisQuery": t.string().optional(),
            "analysisQuery": t.proxy(renames["IamPolicyAnalysisQueryIn"]),
        }
    ).named(renames["AnalyzeIamPolicyLongrunningRequestIn"])
    types["AnalyzeIamPolicyLongrunningRequestOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["IamPolicyAnalysisOutputConfigOut"]),
            "savedAnalysisQuery": t.string().optional(),
            "analysisQuery": t.proxy(renames["IamPolicyAnalysisQueryOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeIamPolicyLongrunningRequestOut"])
    types["GoogleCloudOrgpolicyV1ListPolicyIn"] = t.struct(
        {
            "allValues": t.string().optional(),
            "allowedValues": t.array(t.string()).optional(),
            "inheritFromParent": t.boolean().optional(),
            "deniedValues": t.array(t.string()).optional(),
            "suggestedValue": t.string().optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1ListPolicyIn"])
    types["GoogleCloudOrgpolicyV1ListPolicyOut"] = t.struct(
        {
            "allValues": t.string().optional(),
            "allowedValues": t.array(t.string()).optional(),
            "inheritFromParent": t.boolean().optional(),
            "deniedValues": t.array(t.string()).optional(),
            "suggestedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1ListPolicyOut"])
    types["AnalyzeIamPolicyLongrunningResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AnalyzeIamPolicyLongrunningResponseIn"])
    types["AnalyzeIamPolicyLongrunningResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AnalyzeIamPolicyLongrunningResponseOut"])
    types["GoogleCloudAssetV1p7beta1RelatedAssetsIn"] = t.struct(
        {
            "relationshipAttributes": t.proxy(
                renames["GoogleCloudAssetV1p7beta1RelationshipAttributesIn"]
            ).optional(),
            "assets": t.array(
                t.proxy(renames["GoogleCloudAssetV1p7beta1RelatedAssetIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1RelatedAssetsIn"])
    types["GoogleCloudAssetV1p7beta1RelatedAssetsOut"] = t.struct(
        {
            "relationshipAttributes": t.proxy(
                renames["GoogleCloudAssetV1p7beta1RelationshipAttributesOut"]
            ).optional(),
            "assets": t.array(
                t.proxy(renames["GoogleCloudAssetV1p7beta1RelatedAssetOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1RelatedAssetsOut"])
    types["GoogleCloudAssetV1AccessControlListIn"] = t.struct(
        {
            "resourceEdges": t.array(
                t.proxy(renames["GoogleCloudAssetV1EdgeIn"])
            ).optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudAssetV1ResourceIn"])
            ).optional(),
            "conditionEvaluation": t.proxy(renames["ConditionEvaluationIn"]).optional(),
            "accesses": t.array(
                t.proxy(renames["GoogleCloudAssetV1AccessIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudAssetV1AccessControlListIn"])
    types["GoogleCloudAssetV1AccessControlListOut"] = t.struct(
        {
            "resourceEdges": t.array(
                t.proxy(renames["GoogleCloudAssetV1EdgeOut"])
            ).optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudAssetV1ResourceOut"])
            ).optional(),
            "conditionEvaluation": t.proxy(
                renames["ConditionEvaluationOut"]
            ).optional(),
            "accesses": t.array(
                t.proxy(renames["GoogleCloudAssetV1AccessOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1AccessControlListOut"])
    types["GoogleCloudAssetV1DeniedAccessAccessIn"] = t.struct(
        {"role": t.string().optional(), "permission": t.string().optional()}
    ).named(renames["GoogleCloudAssetV1DeniedAccessAccessIn"])
    types["GoogleCloudAssetV1DeniedAccessAccessOut"] = t.struct(
        {
            "role": t.string().optional(),
            "permission": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessAccessOut"])
    types["GoogleCloudOrgpolicyV1PolicyIn"] = t.struct(
        {
            "restoreDefault": t.proxy(
                renames["GoogleCloudOrgpolicyV1RestoreDefaultIn"]
            ).optional(),
            "constraint": t.string().optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "listPolicy": t.proxy(
                renames["GoogleCloudOrgpolicyV1ListPolicyIn"]
            ).optional(),
            "updateTime": t.string().optional(),
            "booleanPolicy": t.proxy(
                renames["GoogleCloudOrgpolicyV1BooleanPolicyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1PolicyIn"])
    types["GoogleCloudOrgpolicyV1PolicyOut"] = t.struct(
        {
            "restoreDefault": t.proxy(
                renames["GoogleCloudOrgpolicyV1RestoreDefaultOut"]
            ).optional(),
            "constraint": t.string().optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "listPolicy": t.proxy(
                renames["GoogleCloudOrgpolicyV1ListPolicyOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "booleanPolicy": t.proxy(
                renames["GoogleCloudOrgpolicyV1BooleanPolicyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1PolicyOut"])
    types["WindowsUpdatePackageIn"] = t.struct(
        {
            "kbArticleIds": t.array(t.string()).optional(),
            "moreInfoUrls": t.array(t.string()).optional(),
            "updateId": t.string().optional(),
            "description": t.string().optional(),
            "lastDeploymentChangeTime": t.string().optional(),
            "revisionNumber": t.integer().optional(),
            "supportUrl": t.string().optional(),
            "categories": t.array(
                t.proxy(renames["WindowsUpdateCategoryIn"])
            ).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["WindowsUpdatePackageIn"])
    types["WindowsUpdatePackageOut"] = t.struct(
        {
            "kbArticleIds": t.array(t.string()).optional(),
            "moreInfoUrls": t.array(t.string()).optional(),
            "updateId": t.string().optional(),
            "description": t.string().optional(),
            "lastDeploymentChangeTime": t.string().optional(),
            "revisionNumber": t.integer().optional(),
            "supportUrl": t.string().optional(),
            "categories": t.array(
                t.proxy(renames["WindowsUpdateCategoryOut"])
            ).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsUpdatePackageOut"])
    types["GoogleIdentityAccesscontextmanagerV1IngressSourceIn"] = t.struct(
        {"resource": t.string().optional(), "accessLevel": t.string().optional()}
    ).named(renames["GoogleIdentityAccesscontextmanagerV1IngressSourceIn"])
    types["GoogleIdentityAccesscontextmanagerV1IngressSourceOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "accessLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1IngressSourceOut"])
    types["PermissionsIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["PermissionsIn"])
    types["PermissionsOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionsOut"])
    types["GoogleIdentityAccesscontextmanagerV1ApiOperationIn"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "methodSelectors": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1MethodSelectorIn"])
            ).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ApiOperationIn"])
    types["GoogleIdentityAccesscontextmanagerV1ApiOperationOut"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "methodSelectors": t.array(
                t.proxy(
                    renames["GoogleIdentityAccesscontextmanagerV1MethodSelectorOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ApiOperationOut"])
    types["DeniedAccessIn"] = t.struct(
        {
            "denyDetails": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessDenyDetailIn"])
            ).optional(),
            "deniedAccessTuple": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessAccessTupleIn"]
            ).optional(),
        }
    ).named(renames["DeniedAccessIn"])
    types["DeniedAccessOut"] = t.struct(
        {
            "denyDetails": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessDenyDetailOut"])
            ).optional(),
            "deniedAccessTuple": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessAccessTupleOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeniedAccessOut"])
    types[
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetIn"
    ] = t.struct(
        {
            "governedResource": t.proxy(
                renames[
                    "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceIn"
                ]
            ).optional(),
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyIn"]).optional(),
            "governedIamPolicy": t.proxy(
                renames[
                    "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyIn"
                ]
            ).optional(),
            "policyBundle": t.array(t.proxy(renames["AnalyzerOrgPolicyIn"])).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetIn"
        ]
    )
    types[
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetOut"
    ] = t.struct(
        {
            "governedResource": t.proxy(
                renames[
                    "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceOut"
                ]
            ).optional(),
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyOut"]).optional(),
            "governedIamPolicy": t.proxy(
                renames[
                    "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyOut"
                ]
            ).optional(),
            "policyBundle": t.array(
                t.proxy(renames["AnalyzerOrgPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetOut"
        ]
    )
    types["SoftwarePackageIn"] = t.struct(
        {
            "aptPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
            "googetPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
            "windowsApplication": t.proxy(renames["WindowsApplicationIn"]).optional(),
            "zypperPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
            "zypperPatch": t.proxy(renames["ZypperPatchIn"]).optional(),
            "qfePackage": t.proxy(
                renames["WindowsQuickFixEngineeringPackageIn"]
            ).optional(),
            "yumPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
            "wuaPackage": t.proxy(renames["WindowsUpdatePackageIn"]).optional(),
            "cosPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
        }
    ).named(renames["SoftwarePackageIn"])
    types["SoftwarePackageOut"] = t.struct(
        {
            "aptPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "googetPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "windowsApplication": t.proxy(renames["WindowsApplicationOut"]).optional(),
            "zypperPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "zypperPatch": t.proxy(renames["ZypperPatchOut"]).optional(),
            "qfePackage": t.proxy(
                renames["WindowsQuickFixEngineeringPackageOut"]
            ).optional(),
            "yumPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "wuaPackage": t.proxy(renames["WindowsUpdatePackageOut"]).optional(),
            "cosPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SoftwarePackageOut"])
    types["OutputConfigIn"] = t.struct(
        {
            "bigqueryDestination": t.proxy(renames["BigQueryDestinationIn"]).optional(),
            "gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional(),
        }
    ).named(renames["OutputConfigIn"])
    types["OutputConfigOut"] = t.struct(
        {
            "bigqueryDestination": t.proxy(
                renames["BigQueryDestinationOut"]
            ).optional(),
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutputConfigOut"])
    types["WindowsQuickFixEngineeringPackageIn"] = t.struct(
        {
            "description": t.string().optional(),
            "hotFixId": t.string().optional(),
            "caption": t.string().optional(),
            "installTime": t.string().optional(),
        }
    ).named(renames["WindowsQuickFixEngineeringPackageIn"])
    types["WindowsQuickFixEngineeringPackageOut"] = t.struct(
        {
            "description": t.string().optional(),
            "hotFixId": t.string().optional(),
            "caption": t.string().optional(),
            "installTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsQuickFixEngineeringPackageOut"])
    types["BatchGetEffectiveIamPoliciesResponseIn"] = t.struct(
        {"policyResults": t.array(t.proxy(renames["EffectiveIamPolicyIn"])).optional()}
    ).named(renames["BatchGetEffectiveIamPoliciesResponseIn"])
    types["BatchGetEffectiveIamPoliciesResponseOut"] = t.struct(
        {
            "policyResults": t.array(
                t.proxy(renames["EffectiveIamPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetEffectiveIamPoliciesResponseOut"])
    types["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn"] = t.struct(
        {
            "vpcAccessibleServices": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesIn"]
            ).optional(),
            "egressPolicies": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1EgressPolicyIn"])
            ).optional(),
            "restrictedServices": t.array(t.string()).optional(),
            "ingressPolicies": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1IngressPolicyIn"])
            ).optional(),
            "resources": t.array(t.string()).optional(),
            "accessLevels": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn"])
    types["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut"] = t.struct(
        {
            "vpcAccessibleServices": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesOut"]
            ).optional(),
            "egressPolicies": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1EgressPolicyOut"])
            ).optional(),
            "restrictedServices": t.array(t.string()).optional(),
            "ingressPolicies": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1IngressPolicyOut"])
            ).optional(),
            "resources": t.array(t.string()).optional(),
            "accessLevels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut"])
    types["QueryResultIn"] = t.struct(
        {
            "rows": t.array(t.struct({"_": t.string().optional()})).optional(),
            "nextPageToken": t.string().optional(),
            "totalRows": t.string().optional(),
            "schema": t.proxy(renames["TableSchemaIn"]).optional(),
        }
    ).named(renames["QueryResultIn"])
    types["QueryResultOut"] = t.struct(
        {
            "rows": t.array(t.struct({"_": t.string().optional()})).optional(),
            "nextPageToken": t.string().optional(),
            "totalRows": t.string().optional(),
            "schema": t.proxy(renames["TableSchemaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResultOut"])
    types["GoogleCloudAssetV1DeniedAccessResourceIn"] = t.struct(
        {"fullResourceName": t.string().optional()}
    ).named(renames["GoogleCloudAssetV1DeniedAccessResourceIn"])
    types["GoogleCloudAssetV1DeniedAccessResourceOut"] = t.struct(
        {
            "fullResourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessResourceOut"])
    types["GoogleCloudAssetV1BooleanConstraintIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudAssetV1BooleanConstraintIn"])
    types["GoogleCloudAssetV1BooleanConstraintOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudAssetV1BooleanConstraintOut"])
    types["IamPolicyAnalysisResultIn"] = t.struct(
        {
            "accessControlLists": t.array(
                t.proxy(renames["GoogleCloudAssetV1AccessControlListIn"])
            ).optional(),
            "fullyExplored": t.boolean().optional(),
            "attachedResourceFullName": t.string().optional(),
            "identityList": t.proxy(
                renames["GoogleCloudAssetV1IdentityListIn"]
            ).optional(),
            "iamBinding": t.proxy(renames["BindingIn"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisResultIn"])
    types["IamPolicyAnalysisResultOut"] = t.struct(
        {
            "accessControlLists": t.array(
                t.proxy(renames["GoogleCloudAssetV1AccessControlListOut"])
            ).optional(),
            "fullyExplored": t.boolean().optional(),
            "attachedResourceFullName": t.string().optional(),
            "identityList": t.proxy(
                renames["GoogleCloudAssetV1IdentityListOut"]
            ).optional(),
            "iamBinding": t.proxy(renames["BindingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisResultOut"])
    types["GoogleIdentityAccesscontextmanagerV1IngressFromIn"] = t.struct(
        {
            "sources": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1IngressSourceIn"])
            ).optional(),
            "identities": t.array(t.string()).optional(),
            "identityType": t.string().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1IngressFromIn"])
    types["GoogleIdentityAccesscontextmanagerV1IngressFromOut"] = t.struct(
        {
            "sources": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1IngressSourceOut"])
            ).optional(),
            "identities": t.array(t.string()).optional(),
            "identityType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1IngressFromOut"])
    types["FeedOutputConfigIn"] = t.struct(
        {"pubsubDestination": t.proxy(renames["PubsubDestinationIn"]).optional()}
    ).named(renames["FeedOutputConfigIn"])
    types["FeedOutputConfigOut"] = t.struct(
        {
            "pubsubDestination": t.proxy(renames["PubsubDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeedOutputConfigOut"])
    types["PolicyInfoIn"] = t.struct(
        {
            "attachedResource": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
        }
    ).named(renames["PolicyInfoIn"])
    types["PolicyInfoOut"] = t.struct(
        {
            "attachedResource": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyInfoOut"])
    types["OptionsIn"] = t.struct(
        {
            "outputResourceEdges": t.boolean().optional(),
            "expandResources": t.boolean().optional(),
            "expandRoles": t.boolean().optional(),
            "outputGroupEdges": t.boolean().optional(),
            "includeDenyPolicyAnalysis": t.boolean().optional(),
            "expandGroups": t.boolean().optional(),
            "analyzeServiceAccountImpersonation": t.boolean().optional(),
        }
    ).named(renames["OptionsIn"])
    types["OptionsOut"] = t.struct(
        {
            "outputResourceEdges": t.boolean().optional(),
            "expandResources": t.boolean().optional(),
            "expandRoles": t.boolean().optional(),
            "outputGroupEdges": t.boolean().optional(),
            "includeDenyPolicyAnalysis": t.boolean().optional(),
            "expandGroups": t.boolean().optional(),
            "analyzeServiceAccountImpersonation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionsOut"])
    types["IdentitySelectorIn"] = t.struct({"identity": t.string()}).named(
        renames["IdentitySelectorIn"]
    )
    types["IdentitySelectorOut"] = t.struct(
        {"identity": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IdentitySelectorOut"])
    types["UpdateFeedRequestIn"] = t.struct(
        {"updateMask": t.string(), "feed": t.proxy(renames["FeedIn"])}
    ).named(renames["UpdateFeedRequestIn"])
    types["UpdateFeedRequestOut"] = t.struct(
        {
            "updateMask": t.string(),
            "feed": t.proxy(renames["FeedOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateFeedRequestOut"])
    types["VersionedPackageIn"] = t.struct(
        {
            "packageName": t.string().optional(),
            "architecture": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["VersionedPackageIn"])
    types["VersionedPackageOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "architecture": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionedPackageOut"])
    types["WindowsUpdateCategoryIn"] = t.struct(
        {"name": t.string().optional(), "id": t.string().optional()}
    ).named(renames["WindowsUpdateCategoryIn"])
    types["WindowsUpdateCategoryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsUpdateCategoryOut"])
    types["AnalyzeMoveResponseIn"] = t.struct(
        {"moveAnalysis": t.array(t.proxy(renames["MoveAnalysisIn"])).optional()}
    ).named(renames["AnalyzeMoveResponseIn"])
    types["AnalyzeMoveResponseOut"] = t.struct(
        {
            "moveAnalysis": t.array(t.proxy(renames["MoveAnalysisOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeMoveResponseOut"])
    types["GoogleIdentityAccesscontextmanagerV1EgressFromIn"] = t.struct(
        {
            "identityType": t.string().optional(),
            "identities": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1EgressFromIn"])
    types["GoogleIdentityAccesscontextmanagerV1EgressFromOut"] = t.struct(
        {
            "identityType": t.string().optional(),
            "identities": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1EgressFromOut"])
    types["CreateFeedRequestIn"] = t.struct(
        {"feed": t.proxy(renames["FeedIn"]), "feedId": t.string()}
    ).named(renames["CreateFeedRequestIn"])
    types["CreateFeedRequestOut"] = t.struct(
        {
            "feed": t.proxy(renames["FeedOut"]),
            "feedId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateFeedRequestOut"])
    types["AnalyzerOrgPolicyIn"] = t.struct(
        {
            "attachedResource": t.string().optional(),
            "appliedResource": t.string().optional(),
            "rules": t.array(t.proxy(renames["GoogleCloudAssetV1RuleIn"])).optional(),
            "inheritFromParent": t.boolean().optional(),
            "reset": t.boolean().optional(),
        }
    ).named(renames["AnalyzerOrgPolicyIn"])
    types["AnalyzerOrgPolicyOut"] = t.struct(
        {
            "attachedResource": t.string().optional(),
            "appliedResource": t.string().optional(),
            "rules": t.array(t.proxy(renames["GoogleCloudAssetV1RuleOut"])).optional(),
            "inheritFromParent": t.boolean().optional(),
            "reset": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzerOrgPolicyOut"])
    types["GoogleCloudAssetV1p7beta1RelatedAssetIn"] = t.struct(
        {
            "assetType": t.string().optional(),
            "asset": t.string().optional(),
            "ancestors": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1RelatedAssetIn"])
    types["GoogleCloudAssetV1p7beta1RelatedAssetOut"] = t.struct(
        {
            "assetType": t.string().optional(),
            "asset": t.string().optional(),
            "ancestors": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1RelatedAssetOut"])
    types["GoogleCloudAssetV1AccessIn"] = t.struct(
        {
            "analysisState": t.proxy(renames["IamPolicyAnalysisStateIn"]).optional(),
            "role": t.string().optional(),
            "permission": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1AccessIn"])
    types["GoogleCloudAssetV1AccessOut"] = t.struct(
        {
            "analysisState": t.proxy(renames["IamPolicyAnalysisStateOut"]).optional(),
            "role": t.string().optional(),
            "permission": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1AccessOut"])
    types["GoogleCloudAssetV1IdentityListIn"] = t.struct(
        {
            "groupEdges": t.array(
                t.proxy(renames["GoogleCloudAssetV1EdgeIn"])
            ).optional(),
            "identities": t.array(
                t.proxy(renames["GoogleCloudAssetV1IdentityIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudAssetV1IdentityListIn"])
    types["GoogleCloudAssetV1IdentityListOut"] = t.struct(
        {
            "groupEdges": t.array(
                t.proxy(renames["GoogleCloudAssetV1EdgeOut"])
            ).optional(),
            "identities": t.array(
                t.proxy(renames["GoogleCloudAssetV1IdentityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1IdentityListOut"])
    types["ResourceIn"] = t.struct(
        {
            "parent": t.string().optional(),
            "discoveryDocumentUri": t.string().optional(),
            "version": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "discoveryName": t.string().optional(),
            "location": t.string().optional(),
            "resourceUrl": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "discoveryDocumentUri": t.string().optional(),
            "version": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "discoveryName": t.string().optional(),
            "location": t.string().optional(),
            "resourceUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
    types["ListAssetsResponseIn"] = t.struct(
        {
            "assets": t.array(t.proxy(renames["AssetIn"])).optional(),
            "readTime": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAssetsResponseIn"])
    types["ListAssetsResponseOut"] = t.struct(
        {
            "assets": t.array(t.proxy(renames["AssetOut"])).optional(),
            "readTime": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssetsResponseOut"])
    types["GoogleCloudOrgpolicyV1BooleanPolicyIn"] = t.struct(
        {"enforced": t.boolean().optional()}
    ).named(renames["GoogleCloudOrgpolicyV1BooleanPolicyIn"])
    types["GoogleCloudOrgpolicyV1BooleanPolicyOut"] = t.struct(
        {
            "enforced": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1BooleanPolicyOut"])
    types["IamPolicyAnalysisQueryIn"] = t.struct(
        {
            "identitySelector": t.proxy(renames["IdentitySelectorIn"]).optional(),
            "accessSelector": t.proxy(renames["AccessSelectorIn"]).optional(),
            "scope": t.string(),
            "conditionContext": t.proxy(renames["ConditionContextIn"]).optional(),
            "options": t.proxy(renames["OptionsIn"]).optional(),
            "resourceSelector": t.proxy(renames["ResourceSelectorIn"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisQueryIn"])
    types["IamPolicyAnalysisQueryOut"] = t.struct(
        {
            "identitySelector": t.proxy(renames["IdentitySelectorOut"]).optional(),
            "accessSelector": t.proxy(renames["AccessSelectorOut"]).optional(),
            "scope": t.string(),
            "conditionContext": t.proxy(renames["ConditionContextOut"]).optional(),
            "options": t.proxy(renames["OptionsOut"]).optional(),
            "resourceSelector": t.proxy(renames["ResourceSelectorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisQueryOut"])
    types["PartitionSpecIn"] = t.struct({"partitionKey": t.string().optional()}).named(
        renames["PartitionSpecIn"]
    )
    types["PartitionSpecOut"] = t.struct(
        {
            "partitionKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionSpecOut"])
    types["ResourceSelectorIn"] = t.struct({"fullResourceName": t.string()}).named(
        renames["ResourceSelectorIn"]
    )
    types["ResourceSelectorOut"] = t.struct(
        {
            "fullResourceName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceSelectorOut"])
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
    types["GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "perimeterType": t.string().optional(),
            "spec": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn"]
            ).optional(),
            "useExplicitDryRunSpec": t.boolean().optional(),
            "status": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn"])
    types["GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "perimeterType": t.string().optional(),
            "spec": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut"]
            ).optional(),
            "useExplicitDryRunSpec": t.boolean().optional(),
            "status": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut"])
    types["GoogleIdentityAccesscontextmanagerV1AccessLevelIn"] = t.struct(
        {
            "custom": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1CustomLevelIn"]
            ).optional(),
            "title": t.string().optional(),
            "basic": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1BasicLevelIn"]
            ).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1AccessLevelIn"])
    types["GoogleIdentityAccesscontextmanagerV1AccessLevelOut"] = t.struct(
        {
            "custom": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1CustomLevelOut"]
            ).optional(),
            "title": t.string().optional(),
            "basic": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1BasicLevelOut"]
            ).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1AccessLevelOut"])
    types["ConditionEvaluationIn"] = t.struct(
        {"evaluationValue": t.string().optional()}
    ).named(renames["ConditionEvaluationIn"])
    types["ConditionEvaluationOut"] = t.struct(
        {
            "evaluationValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionEvaluationOut"])
    types["GoogleCloudAssetV1ConstraintIn"] = t.struct(
        {
            "constraintDefault": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "listConstraint": t.proxy(
                renames["GoogleCloudAssetV1ListConstraintIn"]
            ).optional(),
            "booleanConstraint": t.proxy(
                renames["GoogleCloudAssetV1BooleanConstraintIn"]
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1ConstraintIn"])
    types["GoogleCloudAssetV1ConstraintOut"] = t.struct(
        {
            "constraintDefault": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "listConstraint": t.proxy(
                renames["GoogleCloudAssetV1ListConstraintOut"]
            ).optional(),
            "booleanConstraint": t.proxy(
                renames["GoogleCloudAssetV1BooleanConstraintOut"]
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1ConstraintOut"])
    types["GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesIn"] = t.struct(
        {
            "enableRestriction": t.boolean().optional(),
            "allowedServices": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesIn"])
    types["GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesOut"] = t.struct(
        {
            "enableRestriction": t.boolean().optional(),
            "allowedServices": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesOut"])
    types["ExportAssetsRequestIn"] = t.struct(
        {
            "outputConfig": t.proxy(renames["OutputConfigIn"]),
            "relationshipTypes": t.array(t.string()).optional(),
            "contentType": t.string().optional(),
            "readTime": t.string().optional(),
            "assetTypes": t.array(t.string()).optional(),
        }
    ).named(renames["ExportAssetsRequestIn"])
    types["ExportAssetsRequestOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["OutputConfigOut"]),
            "relationshipTypes": t.array(t.string()).optional(),
            "contentType": t.string().optional(),
            "readTime": t.string().optional(),
            "assetTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportAssetsRequestOut"])
    types["IamPolicyAnalysisStateIn"] = t.struct(
        {"cause": t.string().optional(), "code": t.string().optional()}
    ).named(renames["IamPolicyAnalysisStateIn"])
    types["IamPolicyAnalysisStateOut"] = t.struct(
        {
            "cause": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisStateOut"])
    types["GoogleCloudAssetV1CustomConstraintIn"] = t.struct(
        {
            "condition": t.string().optional(),
            "methodTypes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "actionType": t.string().optional(),
            "resourceTypes": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1CustomConstraintIn"])
    types["GoogleCloudAssetV1CustomConstraintOut"] = t.struct(
        {
            "condition": t.string().optional(),
            "methodTypes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "actionType": t.string().optional(),
            "resourceTypes": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1CustomConstraintOut"])
    types["AnalyzerOrgPolicyConstraintIn"] = t.struct(
        {
            "googleDefinedConstraint": t.proxy(
                renames["GoogleCloudAssetV1ConstraintIn"]
            ).optional(),
            "customConstraint": t.proxy(
                renames["GoogleCloudAssetV1CustomConstraintIn"]
            ).optional(),
        }
    ).named(renames["AnalyzerOrgPolicyConstraintIn"])
    types["AnalyzerOrgPolicyConstraintOut"] = t.struct(
        {
            "googleDefinedConstraint": t.proxy(
                renames["GoogleCloudAssetV1ConstraintOut"]
            ).optional(),
            "customConstraint": t.proxy(
                renames["GoogleCloudAssetV1CustomConstraintOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzerOrgPolicyConstraintOut"])
    types["GoogleCloudAssetV1DeniedAccessDenyDetailIn"] = t.struct(
        {
            "denyRule": t.proxy(renames["GoogleIamV2DenyRuleIn"]).optional(),
            "identities": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessIdentityIn"])
            ).optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessResourceIn"])
            ).optional(),
            "fullyDenied": t.boolean().optional(),
            "accesses": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessAccessIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessDenyDetailIn"])
    types["GoogleCloudAssetV1DeniedAccessDenyDetailOut"] = t.struct(
        {
            "denyRule": t.proxy(renames["GoogleIamV2DenyRuleOut"]).optional(),
            "identities": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessIdentityOut"])
            ).optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessResourceOut"])
            ).optional(),
            "fullyDenied": t.boolean().optional(),
            "accesses": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessAccessOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessDenyDetailOut"])
    types["GoogleIdentityAccesscontextmanagerV1AccessPolicyIn"] = t.struct(
        {
            "scopes": t.array(t.string()).optional(),
            "parent": t.string(),
            "etag": t.string().optional(),
            "title": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyIn"])
    types["GoogleIdentityAccesscontextmanagerV1AccessPolicyOut"] = t.struct(
        {
            "scopes": t.array(t.string()).optional(),
            "parent": t.string(),
            "etag": t.string().optional(),
            "title": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyOut"])
    types["BigQueryDestinationIn"] = t.struct(
        {
            "separateTablesPerAssetType": t.boolean().optional(),
            "partitionSpec": t.proxy(renames["PartitionSpecIn"]).optional(),
            "force": t.boolean().optional(),
            "dataset": t.string(),
            "table": t.string(),
        }
    ).named(renames["BigQueryDestinationIn"])
    types["BigQueryDestinationOut"] = t.struct(
        {
            "separateTablesPerAssetType": t.boolean().optional(),
            "partitionSpec": t.proxy(renames["PartitionSpecOut"]).optional(),
            "force": t.boolean().optional(),
            "dataset": t.string(),
            "table": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDestinationOut"])
    types["OsInfoIn"] = t.struct(
        {
            "osconfigAgentVersion": t.string().optional(),
            "shortName": t.string().optional(),
            "hostname": t.string().optional(),
            "architecture": t.string().optional(),
            "longName": t.string().optional(),
            "kernelVersion": t.string().optional(),
            "version": t.string().optional(),
            "kernelRelease": t.string().optional(),
        }
    ).named(renames["OsInfoIn"])
    types["OsInfoOut"] = t.struct(
        {
            "osconfigAgentVersion": t.string().optional(),
            "shortName": t.string().optional(),
            "hostname": t.string().optional(),
            "architecture": t.string().optional(),
            "longName": t.string().optional(),
            "kernelVersion": t.string().optional(),
            "version": t.string().optional(),
            "kernelRelease": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OsInfoOut"])
    types["AnalyzeOrgPolicyGovernedContainersResponseIn"] = t.struct(
        {
            "governedContainers": t.array(
                t.proxy(renames["GoogleCloudAssetV1GovernedContainerIn"])
            ).optional(),
            "constraint": t.proxy(renames["AnalyzerOrgPolicyConstraintIn"]).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["AnalyzeOrgPolicyGovernedContainersResponseIn"])
    types["AnalyzeOrgPolicyGovernedContainersResponseOut"] = t.struct(
        {
            "governedContainers": t.array(
                t.proxy(renames["GoogleCloudAssetV1GovernedContainerOut"])
            ).optional(),
            "constraint": t.proxy(renames["AnalyzerOrgPolicyConstraintOut"]).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeOrgPolicyGovernedContainersResponseOut"])
    types["FeedIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "relationshipTypes": t.array(t.string()).optional(),
            "name": t.string(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "assetTypes": t.array(t.string()).optional(),
            "assetNames": t.array(t.string()).optional(),
            "feedOutputConfig": t.proxy(renames["FeedOutputConfigIn"]),
        }
    ).named(renames["FeedIn"])
    types["FeedOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "relationshipTypes": t.array(t.string()).optional(),
            "name": t.string(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "assetTypes": t.array(t.string()).optional(),
            "assetNames": t.array(t.string()).optional(),
            "feedOutputConfig": t.proxy(renames["FeedOutputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeedOut"])
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
    types["GoogleIdentityAccesscontextmanagerV1CustomLevelIn"] = t.struct(
        {"expr": t.proxy(renames["ExprIn"])}
    ).named(renames["GoogleIdentityAccesscontextmanagerV1CustomLevelIn"])
    types["GoogleIdentityAccesscontextmanagerV1CustomLevelOut"] = t.struct(
        {
            "expr": t.proxy(renames["ExprOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1CustomLevelOut"])
    types[
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyIn"
    ] = t.struct(
        {
            "folders": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "project": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "attachedResource": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyIn"
        ]
    )
    types[
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyOut"
    ] = t.struct(
        {
            "folders": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "project": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "attachedResource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyOut"
        ]
    )
    types["RelatedResourceIn"] = t.struct(
        {"assetType": t.string().optional(), "fullResourceName": t.string().optional()}
    ).named(renames["RelatedResourceIn"])
    types["RelatedResourceOut"] = t.struct(
        {
            "assetType": t.string().optional(),
            "fullResourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelatedResourceOut"])
    types["AssetIn"] = t.struct(
        {
            "assetType": t.string().optional(),
            "osInventory": t.proxy(renames["InventoryIn"]).optional(),
            "accessLevel": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessLevelIn"]
            ).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "accessPolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyIn"]
            ).optional(),
            "orgPolicy": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV1PolicyIn"])
            ).optional(),
            "iamPolicy": t.proxy(renames["PolicyIn"]).optional(),
            "servicePerimeter": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn"]
            ).optional(),
            "ancestors": t.array(t.string()).optional(),
            "relatedAssets": t.proxy(renames["RelatedAssetsIn"]).optional(),
            "relatedAsset": t.proxy(renames["RelatedAssetIn"]).optional(),
            "resource": t.proxy(renames["ResourceIn"]).optional(),
        }
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "assetType": t.string().optional(),
            "osInventory": t.proxy(renames["InventoryOut"]).optional(),
            "accessLevel": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessLevelOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "accessPolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyOut"]
            ).optional(),
            "orgPolicy": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV1PolicyOut"])
            ).optional(),
            "iamPolicy": t.proxy(renames["PolicyOut"]).optional(),
            "servicePerimeter": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut"]
            ).optional(),
            "ancestors": t.array(t.string()).optional(),
            "relatedAssets": t.proxy(renames["RelatedAssetsOut"]).optional(),
            "relatedAsset": t.proxy(renames["RelatedAssetOut"]).optional(),
            "resource": t.proxy(renames["ResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
    types["ListSavedQueriesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "savedQueries": t.array(t.proxy(renames["SavedQueryIn"])).optional(),
        }
    ).named(renames["ListSavedQueriesResponseIn"])
    types["ListSavedQueriesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "savedQueries": t.array(t.proxy(renames["SavedQueryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSavedQueriesResponseOut"])
    types["GoogleCloudAssetV1ListConstraintIn"] = t.struct(
        {"supportsIn": t.boolean().optional(), "supportsUnder": t.boolean().optional()}
    ).named(renames["GoogleCloudAssetV1ListConstraintIn"])
    types["GoogleCloudAssetV1ListConstraintOut"] = t.struct(
        {
            "supportsIn": t.boolean().optional(),
            "supportsUnder": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1ListConstraintOut"])
    types["GoogleCloudAssetV1StringValuesIn"] = t.struct(
        {
            "deniedValues": t.array(t.string()).optional(),
            "allowedValues": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudAssetV1StringValuesIn"])
    types["GoogleCloudAssetV1StringValuesOut"] = t.struct(
        {
            "deniedValues": t.array(t.string()).optional(),
            "allowedValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1StringValuesOut"])
    types["ExplanationIn"] = t.struct(
        {"matchedPermissions": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ExplanationIn"])
    types["ExplanationOut"] = t.struct(
        {
            "matchedPermissions": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExplanationOut"])
    types["GoogleIdentityAccesscontextmanagerV1OsConstraintIn"] = t.struct(
        {
            "requireVerifiedChromeOs": t.boolean().optional(),
            "osType": t.string(),
            "minimumVersion": t.string().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1OsConstraintIn"])
    types["GoogleIdentityAccesscontextmanagerV1OsConstraintOut"] = t.struct(
        {
            "requireVerifiedChromeOs": t.boolean().optional(),
            "osType": t.string(),
            "minimumVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1OsConstraintOut"])
    types["GoogleCloudAssetV1BigQueryDestinationIn"] = t.struct(
        {
            "dataset": t.string(),
            "writeDisposition": t.string().optional(),
            "partitionKey": t.string().optional(),
            "tablePrefix": t.string(),
        }
    ).named(renames["GoogleCloudAssetV1BigQueryDestinationIn"])
    types["GoogleCloudAssetV1BigQueryDestinationOut"] = t.struct(
        {
            "dataset": t.string(),
            "writeDisposition": t.string().optional(),
            "partitionKey": t.string().optional(),
            "tablePrefix": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1BigQueryDestinationOut"])
    types["GoogleIdentityAccesscontextmanagerV1BasicLevelIn"] = t.struct(
        {
            "conditions": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1ConditionIn"])
            ),
            "combiningFunction": t.string().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1BasicLevelIn"])
    types["GoogleIdentityAccesscontextmanagerV1BasicLevelOut"] = t.struct(
        {
            "conditions": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1ConditionOut"])
            ),
            "combiningFunction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1BasicLevelOut"])
    types["AttachedResourceIn"] = t.struct(
        {
            "versionedResources": t.array(
                t.proxy(renames["VersionedResourceIn"])
            ).optional(),
            "assetType": t.string().optional(),
        }
    ).named(renames["AttachedResourceIn"])
    types["AttachedResourceOut"] = t.struct(
        {
            "versionedResources": t.array(
                t.proxy(renames["VersionedResourceOut"])
            ).optional(),
            "assetType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachedResourceOut"])
    types["TableSchemaIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["TableFieldSchemaIn"])).optional()}
    ).named(renames["TableSchemaIn"])
    types["TableSchemaOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["TableFieldSchemaOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableSchemaOut"])
    types["ItemIn"] = t.struct(
        {
            "type": t.string().optional(),
            "installedPackage": t.proxy(renames["SoftwarePackageIn"]).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "availablePackage": t.proxy(renames["SoftwarePackageIn"]).optional(),
            "id": t.string().optional(),
            "originType": t.string().optional(),
        }
    ).named(renames["ItemIn"])
    types["ItemOut"] = t.struct(
        {
            "type": t.string().optional(),
            "installedPackage": t.proxy(renames["SoftwarePackageOut"]).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "availablePackage": t.proxy(renames["SoftwarePackageOut"]).optional(),
            "id": t.string().optional(),
            "originType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemOut"])
    types["IamPolicyAnalysisIn"] = t.struct(
        {
            "nonCriticalErrors": t.array(
                t.proxy(renames["IamPolicyAnalysisStateIn"])
            ).optional(),
            "analysisResults": t.array(
                t.proxy(renames["IamPolicyAnalysisResultIn"])
            ).optional(),
            "fullyExplored": t.boolean().optional(),
            "analysisQuery": t.proxy(renames["IamPolicyAnalysisQueryIn"]).optional(),
            "deniedAccesses": t.array(t.proxy(renames["DeniedAccessIn"])).optional(),
        }
    ).named(renames["IamPolicyAnalysisIn"])
    types["IamPolicyAnalysisOut"] = t.struct(
        {
            "nonCriticalErrors": t.array(
                t.proxy(renames["IamPolicyAnalysisStateOut"])
            ).optional(),
            "analysisResults": t.array(
                t.proxy(renames["IamPolicyAnalysisResultOut"])
            ).optional(),
            "fullyExplored": t.boolean().optional(),
            "analysisQuery": t.proxy(renames["IamPolicyAnalysisQueryOut"]).optional(),
            "deniedAccesses": t.array(t.proxy(renames["DeniedAccessOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisOut"])
    types["MoveAnalysisIn"] = t.struct(
        {
            "analysis": t.proxy(renames["MoveAnalysisResultIn"]).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["MoveAnalysisIn"])
    types["MoveAnalysisOut"] = t.struct(
        {
            "analysis": t.proxy(renames["MoveAnalysisResultOut"]).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveAnalysisOut"])
    types["GoogleCloudAssetV1EdgeIn"] = t.struct(
        {"sourceNode": t.string().optional(), "targetNode": t.string().optional()}
    ).named(renames["GoogleCloudAssetV1EdgeIn"])
    types["GoogleCloudAssetV1EdgeOut"] = t.struct(
        {
            "sourceNode": t.string().optional(),
            "targetNode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1EdgeOut"])
    types["VersionedResourceIn"] = t.struct(
        {
            "version": t.string().optional(),
            "resource": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["VersionedResourceIn"])
    types["VersionedResourceOut"] = t.struct(
        {
            "version": t.string().optional(),
            "resource": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionedResourceOut"])
    types["WindowsApplicationIn"] = t.struct(
        {
            "displayVersion": t.string().optional(),
            "displayName": t.string().optional(),
            "publisher": t.string().optional(),
            "installDate": t.proxy(renames["DateIn"]).optional(),
            "helpLink": t.string().optional(),
        }
    ).named(renames["WindowsApplicationIn"])
    types["WindowsApplicationOut"] = t.struct(
        {
            "displayVersion": t.string().optional(),
            "displayName": t.string().optional(),
            "publisher": t.string().optional(),
            "installDate": t.proxy(renames["DateOut"]).optional(),
            "helpLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsApplicationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["QueryContentIn"] = t.struct(
        {
            "iamPolicyAnalysisQuery": t.proxy(
                renames["IamPolicyAnalysisQueryIn"]
            ).optional()
        }
    ).named(renames["QueryContentIn"])
    types["QueryContentOut"] = t.struct(
        {
            "iamPolicyAnalysisQuery": t.proxy(
                renames["IamPolicyAnalysisQueryOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryContentOut"])
    types["MoveImpactIn"] = t.struct({"detail": t.string().optional()}).named(
        renames["MoveImpactIn"]
    )
    types["MoveImpactOut"] = t.struct(
        {
            "detail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveImpactOut"])
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["GoogleCloudAssetV1IdentityIn"] = t.struct(
        {
            "analysisState": t.proxy(renames["IamPolicyAnalysisStateIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1IdentityIn"])
    types["GoogleCloudAssetV1IdentityOut"] = t.struct(
        {
            "analysisState": t.proxy(renames["IamPolicyAnalysisStateOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1IdentityOut"])
    types["ConditionContextIn"] = t.struct({"accessTime": t.string().optional()}).named(
        renames["ConditionContextIn"]
    )
    types["ConditionContextOut"] = t.struct(
        {
            "accessTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionContextOut"])
    types["ListFeedsResponseIn"] = t.struct(
        {"feeds": t.array(t.proxy(renames["FeedIn"])).optional()}
    ).named(renames["ListFeedsResponseIn"])
    types["ListFeedsResponseOut"] = t.struct(
        {
            "feeds": t.array(t.proxy(renames["FeedOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFeedsResponseOut"])
    types["GoogleCloudAssetV1ResourceIn"] = t.struct(
        {
            "fullResourceName": t.string().optional(),
            "analysisState": t.proxy(renames["IamPolicyAnalysisStateIn"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1ResourceIn"])
    types["GoogleCloudAssetV1ResourceOut"] = t.struct(
        {
            "fullResourceName": t.string().optional(),
            "analysisState": t.proxy(renames["IamPolicyAnalysisStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1ResourceOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["IamPolicySearchResultIn"] = t.struct(
        {
            "explanation": t.proxy(renames["ExplanationIn"]).optional(),
            "organization": t.string().optional(),
            "folders": t.array(t.string()).optional(),
            "resource": t.string().optional(),
            "project": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "assetType": t.string().optional(),
        }
    ).named(renames["IamPolicySearchResultIn"])
    types["IamPolicySearchResultOut"] = t.struct(
        {
            "explanation": t.proxy(renames["ExplanationOut"]).optional(),
            "organization": t.string().optional(),
            "folders": t.array(t.string()).optional(),
            "resource": t.string().optional(),
            "project": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "assetType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicySearchResultOut"])
    types["BatchGetAssetsHistoryResponseIn"] = t.struct(
        {"assets": t.array(t.proxy(renames["TemporalAssetIn"])).optional()}
    ).named(renames["BatchGetAssetsHistoryResponseIn"])
    types["BatchGetAssetsHistoryResponseOut"] = t.struct(
        {
            "assets": t.array(t.proxy(renames["TemporalAssetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetAssetsHistoryResponseOut"])
    types["GoogleIamV2DenyRuleIn"] = t.struct(
        {
            "deniedPermissions": t.array(t.string()).optional(),
            "exceptionPrincipals": t.array(t.string()).optional(),
            "exceptionPermissions": t.array(t.string()).optional(),
            "deniedPrincipals": t.array(t.string()).optional(),
            "denialCondition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["GoogleIamV2DenyRuleIn"])
    types["GoogleIamV2DenyRuleOut"] = t.struct(
        {
            "deniedPermissions": t.array(t.string()).optional(),
            "exceptionPrincipals": t.array(t.string()).optional(),
            "exceptionPermissions": t.array(t.string()).optional(),
            "deniedPrincipals": t.array(t.string()).optional(),
            "denialCondition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2DenyRuleOut"])
    types["SavedQueryIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "content": t.proxy(renames["QueryContentIn"]).optional(),
        }
    ).named(renames["SavedQueryIn"])
    types["SavedQueryOut"] = t.struct(
        {
            "creator": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "lastUpdater": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "content": t.proxy(renames["QueryContentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SavedQueryOut"])
    types["ZypperPatchIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "patchName": t.string().optional(),
            "category": t.string().optional(),
            "summary": t.string().optional(),
        }
    ).named(renames["ZypperPatchIn"])
    types["ZypperPatchOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "patchName": t.string().optional(),
            "category": t.string().optional(),
            "summary": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZypperPatchOut"])
    types["GoogleIdentityAccesscontextmanagerV1EgressPolicyIn"] = t.struct(
        {
            "egressFrom": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1EgressFromIn"]
            ).optional(),
            "egressTo": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1EgressToIn"]
            ).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1EgressPolicyIn"])
    types["GoogleIdentityAccesscontextmanagerV1EgressPolicyOut"] = t.struct(
        {
            "egressFrom": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1EgressFromOut"]
            ).optional(),
            "egressTo": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1EgressToOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1EgressPolicyOut"])
    types["GoogleIdentityAccesscontextmanagerV1IngressToIn"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1ApiOperationIn"])
            ).optional(),
            "resources": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1IngressToIn"])
    types["GoogleIdentityAccesscontextmanagerV1IngressToOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1ApiOperationOut"])
            ).optional(),
            "resources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1IngressToOut"])
    types["ResourceSearchResultIn"] = t.struct(
        {
            "additionalAttributes": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "kmsKey": t.string().optional(),
            "relationships": t.struct({"_": t.string().optional()}).optional(),
            "parentAssetType": t.string().optional(),
            "name": t.string().optional(),
            "kmsKeys": t.array(t.string()).optional(),
            "folders": t.array(t.string()).optional(),
            "networkTags": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "organization": t.string().optional(),
            "parentFullResourceName": t.string().optional(),
            "tagValues": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "attachedResources": t.array(
                t.proxy(renames["AttachedResourceIn"])
            ).optional(),
            "tagValueIds": t.array(t.string()).optional(),
            "location": t.string().optional(),
            "tagKeys": t.array(t.string()).optional(),
            "assetType": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "project": t.string().optional(),
            "versionedResources": t.array(
                t.proxy(renames["VersionedResourceIn"])
            ).optional(),
        }
    ).named(renames["ResourceSearchResultIn"])
    types["ResourceSearchResultOut"] = t.struct(
        {
            "additionalAttributes": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "kmsKey": t.string().optional(),
            "relationships": t.struct({"_": t.string().optional()}).optional(),
            "parentAssetType": t.string().optional(),
            "name": t.string().optional(),
            "kmsKeys": t.array(t.string()).optional(),
            "folders": t.array(t.string()).optional(),
            "networkTags": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "organization": t.string().optional(),
            "parentFullResourceName": t.string().optional(),
            "tagValues": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "attachedResources": t.array(
                t.proxy(renames["AttachedResourceOut"])
            ).optional(),
            "tagValueIds": t.array(t.string()).optional(),
            "location": t.string().optional(),
            "tagKeys": t.array(t.string()).optional(),
            "assetType": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "project": t.string().optional(),
            "versionedResources": t.array(
                t.proxy(renames["VersionedResourceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceSearchResultOut"])

    functions = {}
    functions["v1SearchAllResources"] = cloudasset.get(
        "v1/{parent}:batchGetAssetsHistory",
        t.struct(
            {
                "contentType": t.string().optional(),
                "relationshipTypes": t.string().optional(),
                "readTimeWindow.endTime": t.string().optional(),
                "assetNames": t.string().optional(),
                "parent": t.string(),
                "readTimeWindow.startTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetAssetsHistoryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1ExportAssets"] = cloudasset.get(
        "v1/{parent}:batchGetAssetsHistory",
        t.struct(
            {
                "contentType": t.string().optional(),
                "relationshipTypes": t.string().optional(),
                "readTimeWindow.endTime": t.string().optional(),
                "assetNames": t.string().optional(),
                "parent": t.string(),
                "readTimeWindow.startTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetAssetsHistoryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeOrgPolicyGovernedContainers"] = cloudasset.get(
        "v1/{parent}:batchGetAssetsHistory",
        t.struct(
            {
                "contentType": t.string().optional(),
                "relationshipTypes": t.string().optional(),
                "readTimeWindow.endTime": t.string().optional(),
                "assetNames": t.string().optional(),
                "parent": t.string(),
                "readTimeWindow.startTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetAssetsHistoryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeOrgPolicies"] = cloudasset.get(
        "v1/{parent}:batchGetAssetsHistory",
        t.struct(
            {
                "contentType": t.string().optional(),
                "relationshipTypes": t.string().optional(),
                "readTimeWindow.endTime": t.string().optional(),
                "assetNames": t.string().optional(),
                "parent": t.string(),
                "readTimeWindow.startTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetAssetsHistoryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeOrgPolicyGovernedAssets"] = cloudasset.get(
        "v1/{parent}:batchGetAssetsHistory",
        t.struct(
            {
                "contentType": t.string().optional(),
                "relationshipTypes": t.string().optional(),
                "readTimeWindow.endTime": t.string().optional(),
                "assetNames": t.string().optional(),
                "parent": t.string(),
                "readTimeWindow.startTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetAssetsHistoryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1QueryAssets"] = cloudasset.get(
        "v1/{parent}:batchGetAssetsHistory",
        t.struct(
            {
                "contentType": t.string().optional(),
                "relationshipTypes": t.string().optional(),
                "readTimeWindow.endTime": t.string().optional(),
                "assetNames": t.string().optional(),
                "parent": t.string(),
                "readTimeWindow.startTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetAssetsHistoryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1SearchAllIamPolicies"] = cloudasset.get(
        "v1/{parent}:batchGetAssetsHistory",
        t.struct(
            {
                "contentType": t.string().optional(),
                "relationshipTypes": t.string().optional(),
                "readTimeWindow.endTime": t.string().optional(),
                "assetNames": t.string().optional(),
                "parent": t.string(),
                "readTimeWindow.startTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetAssetsHistoryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeIamPolicy"] = cloudasset.get(
        "v1/{parent}:batchGetAssetsHistory",
        t.struct(
            {
                "contentType": t.string().optional(),
                "relationshipTypes": t.string().optional(),
                "readTimeWindow.endTime": t.string().optional(),
                "assetNames": t.string().optional(),
                "parent": t.string(),
                "readTimeWindow.startTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetAssetsHistoryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeMove"] = cloudasset.get(
        "v1/{parent}:batchGetAssetsHistory",
        t.struct(
            {
                "contentType": t.string().optional(),
                "relationshipTypes": t.string().optional(),
                "readTimeWindow.endTime": t.string().optional(),
                "assetNames": t.string().optional(),
                "parent": t.string(),
                "readTimeWindow.startTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetAssetsHistoryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeIamPolicyLongrunning"] = cloudasset.get(
        "v1/{parent}:batchGetAssetsHistory",
        t.struct(
            {
                "contentType": t.string().optional(),
                "relationshipTypes": t.string().optional(),
                "readTimeWindow.endTime": t.string().optional(),
                "assetNames": t.string().optional(),
                "parent": t.string(),
                "readTimeWindow.startTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetAssetsHistoryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1BatchGetAssetsHistory"] = cloudasset.get(
        "v1/{parent}:batchGetAssetsHistory",
        t.struct(
            {
                "contentType": t.string().optional(),
                "relationshipTypes": t.string().optional(),
                "readTimeWindow.endTime": t.string().optional(),
                "assetNames": t.string().optional(),
                "parent": t.string(),
                "readTimeWindow.startTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetAssetsHistoryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["savedQueriesGet"] = cloudasset.get(
        "v1/{parent}/savedQueries",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSavedQueriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["savedQueriesPatch"] = cloudasset.get(
        "v1/{parent}/savedQueries",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSavedQueriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["savedQueriesCreate"] = cloudasset.get(
        "v1/{parent}/savedQueries",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSavedQueriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["savedQueriesDelete"] = cloudasset.get(
        "v1/{parent}/savedQueries",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSavedQueriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["savedQueriesList"] = cloudasset.get(
        "v1/{parent}/savedQueries",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSavedQueriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["feedsGet"] = cloudasset.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["feedsCreate"] = cloudasset.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["feedsList"] = cloudasset.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["feedsPatch"] = cloudasset.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["feedsDelete"] = cloudasset.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["effectiveIamPoliciesBatchGet"] = cloudasset.get(
        "v1/{scope}/effectiveIamPolicies:batchGet",
        t.struct(
            {"scope": t.string(), "names": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["BatchGetEffectiveIamPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = cloudasset.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["assetsList"] = cloudasset.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "relationshipTypes": t.string().optional(),
                "assetTypes": t.string().optional(),
                "contentType": t.string().optional(),
                "pageSize": t.integer().optional(),
                "readTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudasset",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
