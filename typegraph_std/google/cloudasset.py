from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_cloudasset() -> Import:
    cloudasset = HTTPRuntime("https://cloudasset.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudasset_1_ErrorResponse",
        "ConditionEvaluationIn": "_cloudasset_2_ConditionEvaluationIn",
        "ConditionEvaluationOut": "_cloudasset_3_ConditionEvaluationOut",
        "GoogleCloudAssetV1ResourceIn": "_cloudasset_4_GoogleCloudAssetV1ResourceIn",
        "GoogleCloudAssetV1ResourceOut": "_cloudasset_5_GoogleCloudAssetV1ResourceOut",
        "GoogleIdentityAccesscontextmanagerV1MethodSelectorIn": "_cloudasset_6_GoogleIdentityAccesscontextmanagerV1MethodSelectorIn",
        "GoogleIdentityAccesscontextmanagerV1MethodSelectorOut": "_cloudasset_7_GoogleIdentityAccesscontextmanagerV1MethodSelectorOut",
        "IamPolicyAnalysisQueryIn": "_cloudasset_8_IamPolicyAnalysisQueryIn",
        "IamPolicyAnalysisQueryOut": "_cloudasset_9_IamPolicyAnalysisQueryOut",
        "GoogleCloudOrgpolicyV1RestoreDefaultIn": "_cloudasset_10_GoogleCloudOrgpolicyV1RestoreDefaultIn",
        "GoogleCloudOrgpolicyV1RestoreDefaultOut": "_cloudasset_11_GoogleCloudOrgpolicyV1RestoreDefaultOut",
        "BigQueryDestinationIn": "_cloudasset_12_BigQueryDestinationIn",
        "BigQueryDestinationOut": "_cloudasset_13_BigQueryDestinationOut",
        "AccessSelectorIn": "_cloudasset_14_AccessSelectorIn",
        "AccessSelectorOut": "_cloudasset_15_AccessSelectorOut",
        "MoveImpactIn": "_cloudasset_16_MoveImpactIn",
        "MoveImpactOut": "_cloudasset_17_MoveImpactOut",
        "ResourceSearchResultIn": "_cloudasset_18_ResourceSearchResultIn",
        "ResourceSearchResultOut": "_cloudasset_19_ResourceSearchResultOut",
        "PolicyInfoIn": "_cloudasset_20_PolicyInfoIn",
        "PolicyInfoOut": "_cloudasset_21_PolicyInfoOut",
        "AssetIn": "_cloudasset_22_AssetIn",
        "AssetOut": "_cloudasset_23_AssetOut",
        "GoogleIdentityAccesscontextmanagerV1BasicLevelIn": "_cloudasset_24_GoogleIdentityAccesscontextmanagerV1BasicLevelIn",
        "GoogleIdentityAccesscontextmanagerV1BasicLevelOut": "_cloudasset_25_GoogleIdentityAccesscontextmanagerV1BasicLevelOut",
        "CreateFeedRequestIn": "_cloudasset_26_CreateFeedRequestIn",
        "CreateFeedRequestOut": "_cloudasset_27_CreateFeedRequestOut",
        "GoogleIdentityAccesscontextmanagerV1EgressToIn": "_cloudasset_28_GoogleIdentityAccesscontextmanagerV1EgressToIn",
        "GoogleIdentityAccesscontextmanagerV1EgressToOut": "_cloudasset_29_GoogleIdentityAccesscontextmanagerV1EgressToOut",
        "FeedOutputConfigIn": "_cloudasset_30_FeedOutputConfigIn",
        "FeedOutputConfigOut": "_cloudasset_31_FeedOutputConfigOut",
        "TemporalAssetIn": "_cloudasset_32_TemporalAssetIn",
        "TemporalAssetOut": "_cloudasset_33_TemporalAssetOut",
        "GoogleIdentityAccesscontextmanagerV1OsConstraintIn": "_cloudasset_34_GoogleIdentityAccesscontextmanagerV1OsConstraintIn",
        "GoogleIdentityAccesscontextmanagerV1OsConstraintOut": "_cloudasset_35_GoogleIdentityAccesscontextmanagerV1OsConstraintOut",
        "IamPolicyAnalysisOutputConfigIn": "_cloudasset_36_IamPolicyAnalysisOutputConfigIn",
        "IamPolicyAnalysisOutputConfigOut": "_cloudasset_37_IamPolicyAnalysisOutputConfigOut",
        "SearchAllIamPoliciesResponseIn": "_cloudasset_38_SearchAllIamPoliciesResponseIn",
        "SearchAllIamPoliciesResponseOut": "_cloudasset_39_SearchAllIamPoliciesResponseOut",
        "GoogleCloudAssetV1BooleanConstraintIn": "_cloudasset_40_GoogleCloudAssetV1BooleanConstraintIn",
        "GoogleCloudAssetV1BooleanConstraintOut": "_cloudasset_41_GoogleCloudAssetV1BooleanConstraintOut",
        "GoogleIamV2DenyRuleIn": "_cloudasset_42_GoogleIamV2DenyRuleIn",
        "GoogleIamV2DenyRuleOut": "_cloudasset_43_GoogleIamV2DenyRuleOut",
        "GoogleIdentityAccesscontextmanagerV1AccessLevelIn": "_cloudasset_44_GoogleIdentityAccesscontextmanagerV1AccessLevelIn",
        "GoogleIdentityAccesscontextmanagerV1AccessLevelOut": "_cloudasset_45_GoogleIdentityAccesscontextmanagerV1AccessLevelOut",
        "IamPolicySearchResultIn": "_cloudasset_46_IamPolicySearchResultIn",
        "IamPolicySearchResultOut": "_cloudasset_47_IamPolicySearchResultOut",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetIn": "_cloudasset_48_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetIn",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetOut": "_cloudasset_49_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetOut",
        "GoogleIdentityAccesscontextmanagerV1IngressPolicyIn": "_cloudasset_50_GoogleIdentityAccesscontextmanagerV1IngressPolicyIn",
        "GoogleIdentityAccesscontextmanagerV1IngressPolicyOut": "_cloudasset_51_GoogleIdentityAccesscontextmanagerV1IngressPolicyOut",
        "GoogleIdentityAccesscontextmanagerV1IngressSourceIn": "_cloudasset_52_GoogleIdentityAccesscontextmanagerV1IngressSourceIn",
        "GoogleIdentityAccesscontextmanagerV1IngressSourceOut": "_cloudasset_53_GoogleIdentityAccesscontextmanagerV1IngressSourceOut",
        "IamPolicyAnalysisIn": "_cloudasset_54_IamPolicyAnalysisIn",
        "IamPolicyAnalysisOut": "_cloudasset_55_IamPolicyAnalysisOut",
        "EffectiveIamPolicyIn": "_cloudasset_56_EffectiveIamPolicyIn",
        "EffectiveIamPolicyOut": "_cloudasset_57_EffectiveIamPolicyOut",
        "FeedIn": "_cloudasset_58_FeedIn",
        "FeedOut": "_cloudasset_59_FeedOut",
        "OutputConfigIn": "_cloudasset_60_OutputConfigIn",
        "OutputConfigOut": "_cloudasset_61_OutputConfigOut",
        "WindowsUpdatePackageIn": "_cloudasset_62_WindowsUpdatePackageIn",
        "WindowsUpdatePackageOut": "_cloudasset_63_WindowsUpdatePackageOut",
        "GoogleCloudAssetV1AccessIn": "_cloudasset_64_GoogleCloudAssetV1AccessIn",
        "GoogleCloudAssetV1AccessOut": "_cloudasset_65_GoogleCloudAssetV1AccessOut",
        "OsInfoIn": "_cloudasset_66_OsInfoIn",
        "OsInfoOut": "_cloudasset_67_OsInfoOut",
        "AnalyzeOrgPolicyGovernedContainersResponseIn": "_cloudasset_68_AnalyzeOrgPolicyGovernedContainersResponseIn",
        "AnalyzeOrgPolicyGovernedContainersResponseOut": "_cloudasset_69_AnalyzeOrgPolicyGovernedContainersResponseOut",
        "GcsDestinationIn": "_cloudasset_70_GcsDestinationIn",
        "GcsDestinationOut": "_cloudasset_71_GcsDestinationOut",
        "GoogleIdentityAccesscontextmanagerV1IngressFromIn": "_cloudasset_72_GoogleIdentityAccesscontextmanagerV1IngressFromIn",
        "GoogleIdentityAccesscontextmanagerV1IngressFromOut": "_cloudasset_73_GoogleIdentityAccesscontextmanagerV1IngressFromOut",
        "ExplanationIn": "_cloudasset_74_ExplanationIn",
        "ExplanationOut": "_cloudasset_75_ExplanationOut",
        "SavedQueryIn": "_cloudasset_76_SavedQueryIn",
        "SavedQueryOut": "_cloudasset_77_SavedQueryOut",
        "PermissionsIn": "_cloudasset_78_PermissionsIn",
        "PermissionsOut": "_cloudasset_79_PermissionsOut",
        "BatchGetEffectiveIamPoliciesResponseIn": "_cloudasset_80_BatchGetEffectiveIamPoliciesResponseIn",
        "BatchGetEffectiveIamPoliciesResponseOut": "_cloudasset_81_BatchGetEffectiveIamPoliciesResponseOut",
        "VersionedPackageIn": "_cloudasset_82_VersionedPackageIn",
        "VersionedPackageOut": "_cloudasset_83_VersionedPackageOut",
        "RelatedAssetIn": "_cloudasset_84_RelatedAssetIn",
        "RelatedAssetOut": "_cloudasset_85_RelatedAssetOut",
        "PolicyIn": "_cloudasset_86_PolicyIn",
        "PolicyOut": "_cloudasset_87_PolicyOut",
        "QueryAssetsResponseIn": "_cloudasset_88_QueryAssetsResponseIn",
        "QueryAssetsResponseOut": "_cloudasset_89_QueryAssetsResponseOut",
        "GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationIn": "_cloudasset_90_GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationIn",
        "GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationOut": "_cloudasset_91_GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationOut",
        "ItemIn": "_cloudasset_92_ItemIn",
        "ItemOut": "_cloudasset_93_ItemOut",
        "MoveAnalysisResultIn": "_cloudasset_94_MoveAnalysisResultIn",
        "MoveAnalysisResultOut": "_cloudasset_95_MoveAnalysisResultOut",
        "ListAssetsResponseIn": "_cloudasset_96_ListAssetsResponseIn",
        "ListAssetsResponseOut": "_cloudasset_97_ListAssetsResponseOut",
        "MoveAnalysisIn": "_cloudasset_98_MoveAnalysisIn",
        "MoveAnalysisOut": "_cloudasset_99_MoveAnalysisOut",
        "GoogleIdentityAccesscontextmanagerV1AccessPolicyIn": "_cloudasset_100_GoogleIdentityAccesscontextmanagerV1AccessPolicyIn",
        "GoogleIdentityAccesscontextmanagerV1AccessPolicyOut": "_cloudasset_101_GoogleIdentityAccesscontextmanagerV1AccessPolicyOut",
        "GoogleIdentityAccesscontextmanagerV1IngressToIn": "_cloudasset_102_GoogleIdentityAccesscontextmanagerV1IngressToIn",
        "GoogleIdentityAccesscontextmanagerV1IngressToOut": "_cloudasset_103_GoogleIdentityAccesscontextmanagerV1IngressToOut",
        "GoogleCloudOrgpolicyV1BooleanPolicyIn": "_cloudasset_104_GoogleCloudOrgpolicyV1BooleanPolicyIn",
        "GoogleCloudOrgpolicyV1BooleanPolicyOut": "_cloudasset_105_GoogleCloudOrgpolicyV1BooleanPolicyOut",
        "EmptyIn": "_cloudasset_106_EmptyIn",
        "EmptyOut": "_cloudasset_107_EmptyOut",
        "QueryContentIn": "_cloudasset_108_QueryContentIn",
        "QueryContentOut": "_cloudasset_109_QueryContentOut",
        "GoogleCloudAssetV1p7beta1RelationshipAttributesIn": "_cloudasset_110_GoogleCloudAssetV1p7beta1RelationshipAttributesIn",
        "GoogleCloudAssetV1p7beta1RelationshipAttributesOut": "_cloudasset_111_GoogleCloudAssetV1p7beta1RelationshipAttributesOut",
        "PartitionSpecIn": "_cloudasset_112_PartitionSpecIn",
        "PartitionSpecOut": "_cloudasset_113_PartitionSpecOut",
        "GoogleCloudAssetV1GovernedContainerIn": "_cloudasset_114_GoogleCloudAssetV1GovernedContainerIn",
        "GoogleCloudAssetV1GovernedContainerOut": "_cloudasset_115_GoogleCloudAssetV1GovernedContainerOut",
        "AnalyzeIamPolicyLongrunningResponseIn": "_cloudasset_116_AnalyzeIamPolicyLongrunningResponseIn",
        "AnalyzeIamPolicyLongrunningResponseOut": "_cloudasset_117_AnalyzeIamPolicyLongrunningResponseOut",
        "ExportAssetsRequestIn": "_cloudasset_118_ExportAssetsRequestIn",
        "ExportAssetsRequestOut": "_cloudasset_119_ExportAssetsRequestOut",
        "WindowsApplicationIn": "_cloudasset_120_WindowsApplicationIn",
        "WindowsApplicationOut": "_cloudasset_121_WindowsApplicationOut",
        "OperationIn": "_cloudasset_122_OperationIn",
        "OperationOut": "_cloudasset_123_OperationOut",
        "ExprIn": "_cloudasset_124_ExprIn",
        "ExprOut": "_cloudasset_125_ExprOut",
        "AnalyzerOrgPolicyConstraintIn": "_cloudasset_126_AnalyzerOrgPolicyConstraintIn",
        "AnalyzerOrgPolicyConstraintOut": "_cloudasset_127_AnalyzerOrgPolicyConstraintOut",
        "GoogleCloudAssetV1AccessControlListIn": "_cloudasset_128_GoogleCloudAssetV1AccessControlListIn",
        "GoogleCloudAssetV1AccessControlListOut": "_cloudasset_129_GoogleCloudAssetV1AccessControlListOut",
        "GoogleCloudAssetV1p7beta1AssetIn": "_cloudasset_130_GoogleCloudAssetV1p7beta1AssetIn",
        "GoogleCloudAssetV1p7beta1AssetOut": "_cloudasset_131_GoogleCloudAssetV1p7beta1AssetOut",
        "AttachedResourceIn": "_cloudasset_132_AttachedResourceIn",
        "AttachedResourceOut": "_cloudasset_133_AttachedResourceOut",
        "GoogleCloudAssetV1DeniedAccessAccessTupleIn": "_cloudasset_134_GoogleCloudAssetV1DeniedAccessAccessTupleIn",
        "GoogleCloudAssetV1DeniedAccessAccessTupleOut": "_cloudasset_135_GoogleCloudAssetV1DeniedAccessAccessTupleOut",
        "GoogleCloudAssetV1p7beta1RelatedAssetIn": "_cloudasset_136_GoogleCloudAssetV1p7beta1RelatedAssetIn",
        "GoogleCloudAssetV1p7beta1RelatedAssetOut": "_cloudasset_137_GoogleCloudAssetV1p7beta1RelatedAssetOut",
        "GoogleCloudAssetV1GcsDestinationIn": "_cloudasset_138_GoogleCloudAssetV1GcsDestinationIn",
        "GoogleCloudAssetV1GcsDestinationOut": "_cloudasset_139_GoogleCloudAssetV1GcsDestinationOut",
        "GoogleCloudAssetV1IdentityIn": "_cloudasset_140_GoogleCloudAssetV1IdentityIn",
        "GoogleCloudAssetV1IdentityOut": "_cloudasset_141_GoogleCloudAssetV1IdentityOut",
        "GoogleIdentityAccesscontextmanagerV1EgressPolicyIn": "_cloudasset_142_GoogleIdentityAccesscontextmanagerV1EgressPolicyIn",
        "GoogleIdentityAccesscontextmanagerV1EgressPolicyOut": "_cloudasset_143_GoogleIdentityAccesscontextmanagerV1EgressPolicyOut",
        "GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn": "_cloudasset_144_GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn",
        "GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut": "_cloudasset_145_GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut",
        "GoogleCloudAssetV1p7beta1ResourceIn": "_cloudasset_146_GoogleCloudAssetV1p7beta1ResourceIn",
        "GoogleCloudAssetV1p7beta1ResourceOut": "_cloudasset_147_GoogleCloudAssetV1p7beta1ResourceOut",
        "GoogleCloudAssetV1ConstraintIn": "_cloudasset_148_GoogleCloudAssetV1ConstraintIn",
        "GoogleCloudAssetV1ConstraintOut": "_cloudasset_149_GoogleCloudAssetV1ConstraintOut",
        "GoogleCloudOrgpolicyV1PolicyIn": "_cloudasset_150_GoogleCloudOrgpolicyV1PolicyIn",
        "GoogleCloudOrgpolicyV1PolicyOut": "_cloudasset_151_GoogleCloudOrgpolicyV1PolicyOut",
        "PubsubDestinationIn": "_cloudasset_152_PubsubDestinationIn",
        "PubsubDestinationOut": "_cloudasset_153_PubsubDestinationOut",
        "GoogleCloudAssetV1EdgeIn": "_cloudasset_154_GoogleCloudAssetV1EdgeIn",
        "GoogleCloudAssetV1EdgeOut": "_cloudasset_155_GoogleCloudAssetV1EdgeOut",
        "BindingIn": "_cloudasset_156_BindingIn",
        "BindingOut": "_cloudasset_157_BindingOut",
        "IamPolicyAnalysisStateIn": "_cloudasset_158_IamPolicyAnalysisStateIn",
        "IamPolicyAnalysisStateOut": "_cloudasset_159_IamPolicyAnalysisStateOut",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyIn": "_cloudasset_160_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyIn",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyOut": "_cloudasset_161_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyOut",
        "AnalyzeIamPolicyResponseIn": "_cloudasset_162_AnalyzeIamPolicyResponseIn",
        "AnalyzeIamPolicyResponseOut": "_cloudasset_163_AnalyzeIamPolicyResponseOut",
        "RelatedResourceIn": "_cloudasset_164_RelatedResourceIn",
        "RelatedResourceOut": "_cloudasset_165_RelatedResourceOut",
        "DeniedAccessIn": "_cloudasset_166_DeniedAccessIn",
        "DeniedAccessOut": "_cloudasset_167_DeniedAccessOut",
        "GoogleIdentityAccesscontextmanagerV1ApiOperationIn": "_cloudasset_168_GoogleIdentityAccesscontextmanagerV1ApiOperationIn",
        "GoogleIdentityAccesscontextmanagerV1ApiOperationOut": "_cloudasset_169_GoogleIdentityAccesscontextmanagerV1ApiOperationOut",
        "GoogleIdentityAccesscontextmanagerV1CustomLevelIn": "_cloudasset_170_GoogleIdentityAccesscontextmanagerV1CustomLevelIn",
        "GoogleIdentityAccesscontextmanagerV1CustomLevelOut": "_cloudasset_171_GoogleIdentityAccesscontextmanagerV1CustomLevelOut",
        "GoogleCloudOrgpolicyV1ListPolicyIn": "_cloudasset_172_GoogleCloudOrgpolicyV1ListPolicyIn",
        "GoogleCloudOrgpolicyV1ListPolicyOut": "_cloudasset_173_GoogleCloudOrgpolicyV1ListPolicyOut",
        "IamPolicyAnalysisResultIn": "_cloudasset_174_IamPolicyAnalysisResultIn",
        "IamPolicyAnalysisResultOut": "_cloudasset_175_IamPolicyAnalysisResultOut",
        "GoogleCloudAssetV1IdentityListIn": "_cloudasset_176_GoogleCloudAssetV1IdentityListIn",
        "GoogleCloudAssetV1IdentityListOut": "_cloudasset_177_GoogleCloudAssetV1IdentityListOut",
        "GoogleIdentityAccesscontextmanagerV1ConditionIn": "_cloudasset_178_GoogleIdentityAccesscontextmanagerV1ConditionIn",
        "GoogleIdentityAccesscontextmanagerV1ConditionOut": "_cloudasset_179_GoogleIdentityAccesscontextmanagerV1ConditionOut",
        "ResourceSelectorIn": "_cloudasset_180_ResourceSelectorIn",
        "ResourceSelectorOut": "_cloudasset_181_ResourceSelectorOut",
        "GoogleCloudAssetV1CustomConstraintIn": "_cloudasset_182_GoogleCloudAssetV1CustomConstraintIn",
        "GoogleCloudAssetV1CustomConstraintOut": "_cloudasset_183_GoogleCloudAssetV1CustomConstraintOut",
        "AnalyzerOrgPolicyIn": "_cloudasset_184_AnalyzerOrgPolicyIn",
        "AnalyzerOrgPolicyOut": "_cloudasset_185_AnalyzerOrgPolicyOut",
        "QueryAssetsRequestIn": "_cloudasset_186_QueryAssetsRequestIn",
        "QueryAssetsRequestOut": "_cloudasset_187_QueryAssetsRequestOut",
        "ListSavedQueriesResponseIn": "_cloudasset_188_ListSavedQueriesResponseIn",
        "ListSavedQueriesResponseOut": "_cloudasset_189_ListSavedQueriesResponseOut",
        "QueryResultIn": "_cloudasset_190_QueryResultIn",
        "QueryResultOut": "_cloudasset_191_QueryResultOut",
        "GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesIn": "_cloudasset_192_GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesIn",
        "GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesOut": "_cloudasset_193_GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesOut",
        "UpdateFeedRequestIn": "_cloudasset_194_UpdateFeedRequestIn",
        "UpdateFeedRequestOut": "_cloudasset_195_UpdateFeedRequestOut",
        "InventoryIn": "_cloudasset_196_InventoryIn",
        "InventoryOut": "_cloudasset_197_InventoryOut",
        "QueryAssetsOutputConfigIn": "_cloudasset_198_QueryAssetsOutputConfigIn",
        "QueryAssetsOutputConfigOut": "_cloudasset_199_QueryAssetsOutputConfigOut",
        "AuditConfigIn": "_cloudasset_200_AuditConfigIn",
        "AuditConfigOut": "_cloudasset_201_AuditConfigOut",
        "DateIn": "_cloudasset_202_DateIn",
        "DateOut": "_cloudasset_203_DateOut",
        "WindowsUpdateCategoryIn": "_cloudasset_204_WindowsUpdateCategoryIn",
        "WindowsUpdateCategoryOut": "_cloudasset_205_WindowsUpdateCategoryOut",
        "IdentitySelectorIn": "_cloudasset_206_IdentitySelectorIn",
        "IdentitySelectorOut": "_cloudasset_207_IdentitySelectorOut",
        "ResourceIn": "_cloudasset_208_ResourceIn",
        "ResourceOut": "_cloudasset_209_ResourceOut",
        "AuditLogConfigIn": "_cloudasset_210_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudasset_211_AuditLogConfigOut",
        "AnalyzeIamPolicyLongrunningRequestIn": "_cloudasset_212_AnalyzeIamPolicyLongrunningRequestIn",
        "AnalyzeIamPolicyLongrunningRequestOut": "_cloudasset_213_AnalyzeIamPolicyLongrunningRequestOut",
        "OrgPolicyResultIn": "_cloudasset_214_OrgPolicyResultIn",
        "OrgPolicyResultOut": "_cloudasset_215_OrgPolicyResultOut",
        "GoogleCloudAssetV1p7beta1RelatedAssetsIn": "_cloudasset_216_GoogleCloudAssetV1p7beta1RelatedAssetsIn",
        "GoogleCloudAssetV1p7beta1RelatedAssetsOut": "_cloudasset_217_GoogleCloudAssetV1p7beta1RelatedAssetsOut",
        "VersionedResourceIn": "_cloudasset_218_VersionedResourceIn",
        "VersionedResourceOut": "_cloudasset_219_VersionedResourceOut",
        "ConditionContextIn": "_cloudasset_220_ConditionContextIn",
        "ConditionContextOut": "_cloudasset_221_ConditionContextOut",
        "SoftwarePackageIn": "_cloudasset_222_SoftwarePackageIn",
        "SoftwarePackageOut": "_cloudasset_223_SoftwarePackageOut",
        "GoogleCloudAssetV1DeniedAccessDenyDetailIn": "_cloudasset_224_GoogleCloudAssetV1DeniedAccessDenyDetailIn",
        "GoogleCloudAssetV1DeniedAccessDenyDetailOut": "_cloudasset_225_GoogleCloudAssetV1DeniedAccessDenyDetailOut",
        "RelatedAssetsIn": "_cloudasset_226_RelatedAssetsIn",
        "RelatedAssetsOut": "_cloudasset_227_RelatedAssetsOut",
        "RelatedResourcesIn": "_cloudasset_228_RelatedResourcesIn",
        "RelatedResourcesOut": "_cloudasset_229_RelatedResourcesOut",
        "TableFieldSchemaIn": "_cloudasset_230_TableFieldSchemaIn",
        "TableFieldSchemaOut": "_cloudasset_231_TableFieldSchemaOut",
        "AnalyzeOrgPolicyGovernedAssetsResponseIn": "_cloudasset_232_AnalyzeOrgPolicyGovernedAssetsResponseIn",
        "AnalyzeOrgPolicyGovernedAssetsResponseOut": "_cloudasset_233_AnalyzeOrgPolicyGovernedAssetsResponseOut",
        "StatusIn": "_cloudasset_234_StatusIn",
        "StatusOut": "_cloudasset_235_StatusOut",
        "TimeWindowIn": "_cloudasset_236_TimeWindowIn",
        "TimeWindowOut": "_cloudasset_237_TimeWindowOut",
        "GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn": "_cloudasset_238_GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn",
        "GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut": "_cloudasset_239_GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut",
        "GoogleIdentityAccesscontextmanagerV1EgressFromIn": "_cloudasset_240_GoogleIdentityAccesscontextmanagerV1EgressFromIn",
        "GoogleIdentityAccesscontextmanagerV1EgressFromOut": "_cloudasset_241_GoogleIdentityAccesscontextmanagerV1EgressFromOut",
        "ZypperPatchIn": "_cloudasset_242_ZypperPatchIn",
        "ZypperPatchOut": "_cloudasset_243_ZypperPatchOut",
        "OptionsIn": "_cloudasset_244_OptionsIn",
        "OptionsOut": "_cloudasset_245_OptionsOut",
        "GoogleIdentityAccesscontextmanagerV1DevicePolicyIn": "_cloudasset_246_GoogleIdentityAccesscontextmanagerV1DevicePolicyIn",
        "GoogleIdentityAccesscontextmanagerV1DevicePolicyOut": "_cloudasset_247_GoogleIdentityAccesscontextmanagerV1DevicePolicyOut",
        "GoogleCloudAssetV1DeniedAccessAccessIn": "_cloudasset_248_GoogleCloudAssetV1DeniedAccessAccessIn",
        "GoogleCloudAssetV1DeniedAccessAccessOut": "_cloudasset_249_GoogleCloudAssetV1DeniedAccessAccessOut",
        "GoogleCloudAssetV1StringValuesIn": "_cloudasset_250_GoogleCloudAssetV1StringValuesIn",
        "GoogleCloudAssetV1StringValuesOut": "_cloudasset_251_GoogleCloudAssetV1StringValuesOut",
        "AnalyzeOrgPoliciesResponseIn": "_cloudasset_252_AnalyzeOrgPoliciesResponseIn",
        "AnalyzeOrgPoliciesResponseOut": "_cloudasset_253_AnalyzeOrgPoliciesResponseOut",
        "AnalyzeIamPolicyLongrunningMetadataIn": "_cloudasset_254_AnalyzeIamPolicyLongrunningMetadataIn",
        "AnalyzeIamPolicyLongrunningMetadataOut": "_cloudasset_255_AnalyzeIamPolicyLongrunningMetadataOut",
        "SearchAllResourcesResponseIn": "_cloudasset_256_SearchAllResourcesResponseIn",
        "SearchAllResourcesResponseOut": "_cloudasset_257_SearchAllResourcesResponseOut",
        "ListFeedsResponseIn": "_cloudasset_258_ListFeedsResponseIn",
        "ListFeedsResponseOut": "_cloudasset_259_ListFeedsResponseOut",
        "AnalyzeMoveResponseIn": "_cloudasset_260_AnalyzeMoveResponseIn",
        "AnalyzeMoveResponseOut": "_cloudasset_261_AnalyzeMoveResponseOut",
        "BatchGetAssetsHistoryResponseIn": "_cloudasset_262_BatchGetAssetsHistoryResponseIn",
        "BatchGetAssetsHistoryResponseOut": "_cloudasset_263_BatchGetAssetsHistoryResponseOut",
        "TableSchemaIn": "_cloudasset_264_TableSchemaIn",
        "TableSchemaOut": "_cloudasset_265_TableSchemaOut",
        "GoogleCloudAssetV1ListConstraintIn": "_cloudasset_266_GoogleCloudAssetV1ListConstraintIn",
        "GoogleCloudAssetV1ListConstraintOut": "_cloudasset_267_GoogleCloudAssetV1ListConstraintOut",
        "GoogleCloudAssetV1RuleIn": "_cloudasset_268_GoogleCloudAssetV1RuleIn",
        "GoogleCloudAssetV1RuleOut": "_cloudasset_269_GoogleCloudAssetV1RuleOut",
        "RelationshipAttributesIn": "_cloudasset_270_RelationshipAttributesIn",
        "RelationshipAttributesOut": "_cloudasset_271_RelationshipAttributesOut",
        "GoogleCloudAssetV1BigQueryDestinationIn": "_cloudasset_272_GoogleCloudAssetV1BigQueryDestinationIn",
        "GoogleCloudAssetV1BigQueryDestinationOut": "_cloudasset_273_GoogleCloudAssetV1BigQueryDestinationOut",
        "GoogleCloudAssetV1DeniedAccessResourceIn": "_cloudasset_274_GoogleCloudAssetV1DeniedAccessResourceIn",
        "GoogleCloudAssetV1DeniedAccessResourceOut": "_cloudasset_275_GoogleCloudAssetV1DeniedAccessResourceOut",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceIn": "_cloudasset_276_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceIn",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceOut": "_cloudasset_277_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceOut",
        "WindowsQuickFixEngineeringPackageIn": "_cloudasset_278_WindowsQuickFixEngineeringPackageIn",
        "WindowsQuickFixEngineeringPackageOut": "_cloudasset_279_WindowsQuickFixEngineeringPackageOut",
        "GoogleCloudAssetV1DeniedAccessIdentityIn": "_cloudasset_280_GoogleCloudAssetV1DeniedAccessIdentityIn",
        "GoogleCloudAssetV1DeniedAccessIdentityOut": "_cloudasset_281_GoogleCloudAssetV1DeniedAccessIdentityOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ConditionEvaluationIn"] = t.struct(
        {"evaluationValue": t.string().optional()}
    ).named(renames["ConditionEvaluationIn"])
    types["ConditionEvaluationOut"] = t.struct(
        {
            "evaluationValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionEvaluationOut"])
    types["GoogleCloudAssetV1ResourceIn"] = t.struct(
        {
            "analysisState": t.proxy(renames["IamPolicyAnalysisStateIn"]).optional(),
            "fullResourceName": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1ResourceIn"])
    types["GoogleCloudAssetV1ResourceOut"] = t.struct(
        {
            "analysisState": t.proxy(renames["IamPolicyAnalysisStateOut"]).optional(),
            "fullResourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1ResourceOut"])
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
    types["IamPolicyAnalysisQueryIn"] = t.struct(
        {
            "options": t.proxy(renames["OptionsIn"]).optional(),
            "conditionContext": t.proxy(renames["ConditionContextIn"]).optional(),
            "identitySelector": t.proxy(renames["IdentitySelectorIn"]).optional(),
            "resourceSelector": t.proxy(renames["ResourceSelectorIn"]).optional(),
            "scope": t.string(),
            "accessSelector": t.proxy(renames["AccessSelectorIn"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisQueryIn"])
    types["IamPolicyAnalysisQueryOut"] = t.struct(
        {
            "options": t.proxy(renames["OptionsOut"]).optional(),
            "conditionContext": t.proxy(renames["ConditionContextOut"]).optional(),
            "identitySelector": t.proxy(renames["IdentitySelectorOut"]).optional(),
            "resourceSelector": t.proxy(renames["ResourceSelectorOut"]).optional(),
            "scope": t.string(),
            "accessSelector": t.proxy(renames["AccessSelectorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisQueryOut"])
    types["GoogleCloudOrgpolicyV1RestoreDefaultIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudOrgpolicyV1RestoreDefaultIn"])
    types["GoogleCloudOrgpolicyV1RestoreDefaultOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudOrgpolicyV1RestoreDefaultOut"])
    types["BigQueryDestinationIn"] = t.struct(
        {
            "force": t.boolean().optional(),
            "dataset": t.string(),
            "separateTablesPerAssetType": t.boolean().optional(),
            "table": t.string(),
            "partitionSpec": t.proxy(renames["PartitionSpecIn"]).optional(),
        }
    ).named(renames["BigQueryDestinationIn"])
    types["BigQueryDestinationOut"] = t.struct(
        {
            "force": t.boolean().optional(),
            "dataset": t.string(),
            "separateTablesPerAssetType": t.boolean().optional(),
            "table": t.string(),
            "partitionSpec": t.proxy(renames["PartitionSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDestinationOut"])
    types["AccessSelectorIn"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "roles": t.array(t.string()).optional(),
        }
    ).named(renames["AccessSelectorIn"])
    types["AccessSelectorOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "roles": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessSelectorOut"])
    types["MoveImpactIn"] = t.struct({"detail": t.string().optional()}).named(
        renames["MoveImpactIn"]
    )
    types["MoveImpactOut"] = t.struct(
        {
            "detail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveImpactOut"])
    types["ResourceSearchResultIn"] = t.struct(
        {
            "versionedResources": t.array(
                t.proxy(renames["VersionedResourceIn"])
            ).optional(),
            "tagValueIds": t.array(t.string()).optional(),
            "tagKeys": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "parentFullResourceName": t.string().optional(),
            "createTime": t.string().optional(),
            "organization": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "project": t.string().optional(),
            "updateTime": t.string().optional(),
            "kmsKeys": t.array(t.string()).optional(),
            "tagValues": t.array(t.string()).optional(),
            "kmsKey": t.string().optional(),
            "location": t.string().optional(),
            "relationships": t.struct({"_": t.string().optional()}).optional(),
            "attachedResources": t.array(
                t.proxy(renames["AttachedResourceIn"])
            ).optional(),
            "additionalAttributes": t.struct({"_": t.string().optional()}).optional(),
            "assetType": t.string().optional(),
            "folders": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "parentAssetType": t.string().optional(),
        }
    ).named(renames["ResourceSearchResultIn"])
    types["ResourceSearchResultOut"] = t.struct(
        {
            "versionedResources": t.array(
                t.proxy(renames["VersionedResourceOut"])
            ).optional(),
            "tagValueIds": t.array(t.string()).optional(),
            "tagKeys": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "parentFullResourceName": t.string().optional(),
            "createTime": t.string().optional(),
            "organization": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "project": t.string().optional(),
            "updateTime": t.string().optional(),
            "kmsKeys": t.array(t.string()).optional(),
            "tagValues": t.array(t.string()).optional(),
            "kmsKey": t.string().optional(),
            "location": t.string().optional(),
            "relationships": t.struct({"_": t.string().optional()}).optional(),
            "attachedResources": t.array(
                t.proxy(renames["AttachedResourceOut"])
            ).optional(),
            "additionalAttributes": t.struct({"_": t.string().optional()}).optional(),
            "assetType": t.string().optional(),
            "folders": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "parentAssetType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceSearchResultOut"])
    types["PolicyInfoIn"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "attachedResource": t.string().optional(),
        }
    ).named(renames["PolicyInfoIn"])
    types["PolicyInfoOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "attachedResource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyInfoOut"])
    types["AssetIn"] = t.struct(
        {
            "osInventory": t.proxy(renames["InventoryIn"]).optional(),
            "name": t.string().optional(),
            "resource": t.proxy(renames["ResourceIn"]).optional(),
            "ancestors": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "accessLevel": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessLevelIn"]
            ).optional(),
            "assetType": t.string().optional(),
            "orgPolicy": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV1PolicyIn"])
            ).optional(),
            "accessPolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyIn"]
            ).optional(),
            "servicePerimeter": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn"]
            ).optional(),
            "relatedAssets": t.proxy(renames["RelatedAssetsIn"]).optional(),
            "iamPolicy": t.proxy(renames["PolicyIn"]).optional(),
            "relatedAsset": t.proxy(renames["RelatedAssetIn"]).optional(),
        }
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "osInventory": t.proxy(renames["InventoryOut"]).optional(),
            "name": t.string().optional(),
            "resource": t.proxy(renames["ResourceOut"]).optional(),
            "ancestors": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "accessLevel": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessLevelOut"]
            ).optional(),
            "assetType": t.string().optional(),
            "orgPolicy": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV1PolicyOut"])
            ).optional(),
            "accessPolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyOut"]
            ).optional(),
            "servicePerimeter": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut"]
            ).optional(),
            "relatedAssets": t.proxy(renames["RelatedAssetsOut"]).optional(),
            "iamPolicy": t.proxy(renames["PolicyOut"]).optional(),
            "relatedAsset": t.proxy(renames["RelatedAssetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
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
    types["CreateFeedRequestIn"] = t.struct(
        {"feedId": t.string(), "feed": t.proxy(renames["FeedIn"])}
    ).named(renames["CreateFeedRequestIn"])
    types["CreateFeedRequestOut"] = t.struct(
        {
            "feedId": t.string(),
            "feed": t.proxy(renames["FeedOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateFeedRequestOut"])
    types["GoogleIdentityAccesscontextmanagerV1EgressToIn"] = t.struct(
        {
            "externalResources": t.array(t.string()).optional(),
            "resources": t.array(t.string()).optional(),
            "operations": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1ApiOperationIn"])
            ).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1EgressToIn"])
    types["GoogleIdentityAccesscontextmanagerV1EgressToOut"] = t.struct(
        {
            "externalResources": t.array(t.string()).optional(),
            "resources": t.array(t.string()).optional(),
            "operations": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1ApiOperationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1EgressToOut"])
    types["FeedOutputConfigIn"] = t.struct(
        {"pubsubDestination": t.proxy(renames["PubsubDestinationIn"]).optional()}
    ).named(renames["FeedOutputConfigIn"])
    types["FeedOutputConfigOut"] = t.struct(
        {
            "pubsubDestination": t.proxy(renames["PubsubDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeedOutputConfigOut"])
    types["TemporalAssetIn"] = t.struct(
        {
            "priorAssetState": t.string().optional(),
            "window": t.proxy(renames["TimeWindowIn"]).optional(),
            "asset": t.proxy(renames["AssetIn"]).optional(),
            "deleted": t.boolean().optional(),
            "priorAsset": t.proxy(renames["AssetIn"]).optional(),
        }
    ).named(renames["TemporalAssetIn"])
    types["TemporalAssetOut"] = t.struct(
        {
            "priorAssetState": t.string().optional(),
            "window": t.proxy(renames["TimeWindowOut"]).optional(),
            "asset": t.proxy(renames["AssetOut"]).optional(),
            "deleted": t.boolean().optional(),
            "priorAsset": t.proxy(renames["AssetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TemporalAssetOut"])
    types["GoogleIdentityAccesscontextmanagerV1OsConstraintIn"] = t.struct(
        {
            "minimumVersion": t.string().optional(),
            "osType": t.string(),
            "requireVerifiedChromeOs": t.boolean().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1OsConstraintIn"])
    types["GoogleIdentityAccesscontextmanagerV1OsConstraintOut"] = t.struct(
        {
            "minimumVersion": t.string().optional(),
            "osType": t.string(),
            "requireVerifiedChromeOs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1OsConstraintOut"])
    types["IamPolicyAnalysisOutputConfigIn"] = t.struct(
        {
            "bigqueryDestination": t.proxy(
                renames["GoogleCloudAssetV1BigQueryDestinationIn"]
            ).optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudAssetV1GcsDestinationIn"]
            ).optional(),
        }
    ).named(renames["IamPolicyAnalysisOutputConfigIn"])
    types["IamPolicyAnalysisOutputConfigOut"] = t.struct(
        {
            "bigqueryDestination": t.proxy(
                renames["GoogleCloudAssetV1BigQueryDestinationOut"]
            ).optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudAssetV1GcsDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisOutputConfigOut"])
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
    types["GoogleCloudAssetV1BooleanConstraintIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudAssetV1BooleanConstraintIn"])
    types["GoogleCloudAssetV1BooleanConstraintOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudAssetV1BooleanConstraintOut"])
    types["GoogleIamV2DenyRuleIn"] = t.struct(
        {
            "exceptionPrincipals": t.array(t.string()).optional(),
            "exceptionPermissions": t.array(t.string()).optional(),
            "deniedPermissions": t.array(t.string()).optional(),
            "deniedPrincipals": t.array(t.string()).optional(),
            "denialCondition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["GoogleIamV2DenyRuleIn"])
    types["GoogleIamV2DenyRuleOut"] = t.struct(
        {
            "exceptionPrincipals": t.array(t.string()).optional(),
            "exceptionPermissions": t.array(t.string()).optional(),
            "deniedPermissions": t.array(t.string()).optional(),
            "deniedPrincipals": t.array(t.string()).optional(),
            "denialCondition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2DenyRuleOut"])
    types["GoogleIdentityAccesscontextmanagerV1AccessLevelIn"] = t.struct(
        {
            "basic": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1BasicLevelIn"]
            ).optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "custom": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1CustomLevelIn"]
            ).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1AccessLevelIn"])
    types["GoogleIdentityAccesscontextmanagerV1AccessLevelOut"] = t.struct(
        {
            "basic": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1BasicLevelOut"]
            ).optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "custom": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1CustomLevelOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1AccessLevelOut"])
    types["IamPolicySearchResultIn"] = t.struct(
        {
            "project": t.string().optional(),
            "explanation": t.proxy(renames["ExplanationIn"]).optional(),
            "resource": t.string().optional(),
            "folders": t.array(t.string()).optional(),
            "assetType": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "organization": t.string().optional(),
        }
    ).named(renames["IamPolicySearchResultIn"])
    types["IamPolicySearchResultOut"] = t.struct(
        {
            "project": t.string().optional(),
            "explanation": t.proxy(renames["ExplanationOut"]).optional(),
            "resource": t.string().optional(),
            "folders": t.array(t.string()).optional(),
            "assetType": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "organization": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicySearchResultOut"])
    types[
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetIn"
    ] = t.struct(
        {
            "policyBundle": t.array(t.proxy(renames["AnalyzerOrgPolicyIn"])).optional(),
            "governedResource": t.proxy(
                renames[
                    "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceIn"
                ]
            ).optional(),
            "governedIamPolicy": t.proxy(
                renames[
                    "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyIn"
                ]
            ).optional(),
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyIn"]).optional(),
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
            "policyBundle": t.array(
                t.proxy(renames["AnalyzerOrgPolicyOut"])
            ).optional(),
            "governedResource": t.proxy(
                renames[
                    "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceOut"
                ]
            ).optional(),
            "governedIamPolicy": t.proxy(
                renames[
                    "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyOut"
                ]
            ).optional(),
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetOut"
        ]
    )
    types["GoogleIdentityAccesscontextmanagerV1IngressPolicyIn"] = t.struct(
        {
            "ingressFrom": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1IngressFromIn"]
            ).optional(),
            "ingressTo": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1IngressToIn"]
            ).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1IngressPolicyIn"])
    types["GoogleIdentityAccesscontextmanagerV1IngressPolicyOut"] = t.struct(
        {
            "ingressFrom": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1IngressFromOut"]
            ).optional(),
            "ingressTo": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1IngressToOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1IngressPolicyOut"])
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
    types["IamPolicyAnalysisIn"] = t.struct(
        {
            "analysisQuery": t.proxy(renames["IamPolicyAnalysisQueryIn"]).optional(),
            "analysisResults": t.array(
                t.proxy(renames["IamPolicyAnalysisResultIn"])
            ).optional(),
            "nonCriticalErrors": t.array(
                t.proxy(renames["IamPolicyAnalysisStateIn"])
            ).optional(),
            "fullyExplored": t.boolean().optional(),
            "deniedAccesses": t.array(t.proxy(renames["DeniedAccessIn"])).optional(),
        }
    ).named(renames["IamPolicyAnalysisIn"])
    types["IamPolicyAnalysisOut"] = t.struct(
        {
            "analysisQuery": t.proxy(renames["IamPolicyAnalysisQueryOut"]).optional(),
            "analysisResults": t.array(
                t.proxy(renames["IamPolicyAnalysisResultOut"])
            ).optional(),
            "nonCriticalErrors": t.array(
                t.proxy(renames["IamPolicyAnalysisStateOut"])
            ).optional(),
            "fullyExplored": t.boolean().optional(),
            "deniedAccesses": t.array(t.proxy(renames["DeniedAccessOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisOut"])
    types["EffectiveIamPolicyIn"] = t.struct(
        {
            "fullResourceName": t.string().optional(),
            "policies": t.array(t.proxy(renames["PolicyInfoIn"])).optional(),
        }
    ).named(renames["EffectiveIamPolicyIn"])
    types["EffectiveIamPolicyOut"] = t.struct(
        {
            "fullResourceName": t.string().optional(),
            "policies": t.array(t.proxy(renames["PolicyInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EffectiveIamPolicyOut"])
    types["FeedIn"] = t.struct(
        {
            "name": t.string(),
            "contentType": t.string().optional(),
            "relationshipTypes": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "feedOutputConfig": t.proxy(renames["FeedOutputConfigIn"]),
            "assetTypes": t.array(t.string()).optional(),
            "assetNames": t.array(t.string()).optional(),
        }
    ).named(renames["FeedIn"])
    types["FeedOut"] = t.struct(
        {
            "name": t.string(),
            "contentType": t.string().optional(),
            "relationshipTypes": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "feedOutputConfig": t.proxy(renames["FeedOutputConfigOut"]),
            "assetTypes": t.array(t.string()).optional(),
            "assetNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeedOut"])
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
    types["WindowsUpdatePackageIn"] = t.struct(
        {
            "kbArticleIds": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "moreInfoUrls": t.array(t.string()).optional(),
            "lastDeploymentChangeTime": t.string().optional(),
            "revisionNumber": t.integer().optional(),
            "supportUrl": t.string().optional(),
            "updateId": t.string().optional(),
            "description": t.string().optional(),
            "categories": t.array(
                t.proxy(renames["WindowsUpdateCategoryIn"])
            ).optional(),
        }
    ).named(renames["WindowsUpdatePackageIn"])
    types["WindowsUpdatePackageOut"] = t.struct(
        {
            "kbArticleIds": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "moreInfoUrls": t.array(t.string()).optional(),
            "lastDeploymentChangeTime": t.string().optional(),
            "revisionNumber": t.integer().optional(),
            "supportUrl": t.string().optional(),
            "updateId": t.string().optional(),
            "description": t.string().optional(),
            "categories": t.array(
                t.proxy(renames["WindowsUpdateCategoryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsUpdatePackageOut"])
    types["GoogleCloudAssetV1AccessIn"] = t.struct(
        {
            "role": t.string().optional(),
            "permission": t.string().optional(),
            "analysisState": t.proxy(renames["IamPolicyAnalysisStateIn"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1AccessIn"])
    types["GoogleCloudAssetV1AccessOut"] = t.struct(
        {
            "role": t.string().optional(),
            "permission": t.string().optional(),
            "analysisState": t.proxy(renames["IamPolicyAnalysisStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1AccessOut"])
    types["OsInfoIn"] = t.struct(
        {
            "kernelVersion": t.string().optional(),
            "kernelRelease": t.string().optional(),
            "version": t.string().optional(),
            "hostname": t.string().optional(),
            "shortName": t.string().optional(),
            "longName": t.string().optional(),
            "osconfigAgentVersion": t.string().optional(),
            "architecture": t.string().optional(),
        }
    ).named(renames["OsInfoIn"])
    types["OsInfoOut"] = t.struct(
        {
            "kernelVersion": t.string().optional(),
            "kernelRelease": t.string().optional(),
            "version": t.string().optional(),
            "hostname": t.string().optional(),
            "shortName": t.string().optional(),
            "longName": t.string().optional(),
            "osconfigAgentVersion": t.string().optional(),
            "architecture": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OsInfoOut"])
    types["AnalyzeOrgPolicyGovernedContainersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "governedContainers": t.array(
                t.proxy(renames["GoogleCloudAssetV1GovernedContainerIn"])
            ).optional(),
            "constraint": t.proxy(renames["AnalyzerOrgPolicyConstraintIn"]).optional(),
        }
    ).named(renames["AnalyzeOrgPolicyGovernedContainersResponseIn"])
    types["AnalyzeOrgPolicyGovernedContainersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "governedContainers": t.array(
                t.proxy(renames["GoogleCloudAssetV1GovernedContainerOut"])
            ).optional(),
            "constraint": t.proxy(renames["AnalyzerOrgPolicyConstraintOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeOrgPolicyGovernedContainersResponseOut"])
    types["GcsDestinationIn"] = t.struct(
        {"uriPrefix": t.string().optional(), "uri": t.string().optional()}
    ).named(renames["GcsDestinationIn"])
    types["GcsDestinationOut"] = t.struct(
        {
            "uriPrefix": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsDestinationOut"])
    types["GoogleIdentityAccesscontextmanagerV1IngressFromIn"] = t.struct(
        {
            "identities": t.array(t.string()).optional(),
            "sources": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1IngressSourceIn"])
            ).optional(),
            "identityType": t.string().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1IngressFromIn"])
    types["GoogleIdentityAccesscontextmanagerV1IngressFromOut"] = t.struct(
        {
            "identities": t.array(t.string()).optional(),
            "sources": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1IngressSourceOut"])
            ).optional(),
            "identityType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1IngressFromOut"])
    types["ExplanationIn"] = t.struct(
        {"matchedPermissions": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ExplanationIn"])
    types["ExplanationOut"] = t.struct(
        {
            "matchedPermissions": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExplanationOut"])
    types["SavedQueryIn"] = t.struct(
        {
            "content": t.proxy(renames["QueryContentIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["SavedQueryIn"])
    types["SavedQueryOut"] = t.struct(
        {
            "content": t.proxy(renames["QueryContentOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "lastUpdater": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "creator": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SavedQueryOut"])
    types["PermissionsIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["PermissionsIn"])
    types["PermissionsOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionsOut"])
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
    types["VersionedPackageIn"] = t.struct(
        {
            "architecture": t.string().optional(),
            "packageName": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["VersionedPackageIn"])
    types["VersionedPackageOut"] = t.struct(
        {
            "architecture": t.string().optional(),
            "packageName": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionedPackageOut"])
    types["RelatedAssetIn"] = t.struct(
        {
            "asset": t.string().optional(),
            "ancestors": t.array(t.string()).optional(),
            "assetType": t.string().optional(),
            "relationshipType": t.string().optional(),
        }
    ).named(renames["RelatedAssetIn"])
    types["RelatedAssetOut"] = t.struct(
        {
            "asset": t.string().optional(),
            "ancestors": t.array(t.string()).optional(),
            "assetType": t.string().optional(),
            "relationshipType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelatedAssetOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["QueryAssetsResponseIn"] = t.struct(
        {
            "outputConfig": t.proxy(renames["QueryAssetsOutputConfigIn"]).optional(),
            "queryResult": t.proxy(renames["QueryResultIn"]).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "jobReference": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["QueryAssetsResponseIn"])
    types["QueryAssetsResponseOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["QueryAssetsOutputConfigOut"]).optional(),
            "queryResult": t.proxy(renames["QueryResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "jobReference": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["QueryAssetsResponseOut"])
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
    types["ItemIn"] = t.struct(
        {
            "id": t.string().optional(),
            "updateTime": t.string().optional(),
            "installedPackage": t.proxy(renames["SoftwarePackageIn"]).optional(),
            "originType": t.string().optional(),
            "availablePackage": t.proxy(renames["SoftwarePackageIn"]).optional(),
            "type": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["ItemIn"])
    types["ItemOut"] = t.struct(
        {
            "id": t.string().optional(),
            "updateTime": t.string().optional(),
            "installedPackage": t.proxy(renames["SoftwarePackageOut"]).optional(),
            "originType": t.string().optional(),
            "availablePackage": t.proxy(renames["SoftwarePackageOut"]).optional(),
            "type": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemOut"])
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
    types["ListAssetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "readTime": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetIn"])).optional(),
        }
    ).named(renames["ListAssetsResponseIn"])
    types["ListAssetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "readTime": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssetsResponseOut"])
    types["MoveAnalysisIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "analysis": t.proxy(renames["MoveAnalysisResultIn"]).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["MoveAnalysisIn"])
    types["MoveAnalysisOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "analysis": t.proxy(renames["MoveAnalysisResultOut"]).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["MoveAnalysisOut"])
    types["GoogleIdentityAccesscontextmanagerV1AccessPolicyIn"] = t.struct(
        {
            "title": t.string(),
            "etag": t.string().optional(),
            "parent": t.string(),
            "name": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyIn"])
    types["GoogleIdentityAccesscontextmanagerV1AccessPolicyOut"] = t.struct(
        {
            "title": t.string(),
            "etag": t.string().optional(),
            "parent": t.string(),
            "name": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyOut"])
    types["GoogleIdentityAccesscontextmanagerV1IngressToIn"] = t.struct(
        {
            "resources": t.array(t.string()).optional(),
            "operations": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1ApiOperationIn"])
            ).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1IngressToIn"])
    types["GoogleIdentityAccesscontextmanagerV1IngressToOut"] = t.struct(
        {
            "resources": t.array(t.string()).optional(),
            "operations": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1ApiOperationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1IngressToOut"])
    types["GoogleCloudOrgpolicyV1BooleanPolicyIn"] = t.struct(
        {"enforced": t.boolean().optional()}
    ).named(renames["GoogleCloudOrgpolicyV1BooleanPolicyIn"])
    types["GoogleCloudOrgpolicyV1BooleanPolicyOut"] = t.struct(
        {
            "enforced": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1BooleanPolicyOut"])
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
    types["GoogleCloudAssetV1p7beta1RelationshipAttributesIn"] = t.struct(
        {
            "sourceResourceType": t.string().optional(),
            "targetResourceType": t.string().optional(),
            "action": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1RelationshipAttributesIn"])
    types["GoogleCloudAssetV1p7beta1RelationshipAttributesOut"] = t.struct(
        {
            "sourceResourceType": t.string().optional(),
            "targetResourceType": t.string().optional(),
            "action": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1RelationshipAttributesOut"])
    types["PartitionSpecIn"] = t.struct({"partitionKey": t.string().optional()}).named(
        renames["PartitionSpecIn"]
    )
    types["PartitionSpecOut"] = t.struct(
        {
            "partitionKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionSpecOut"])
    types["GoogleCloudAssetV1GovernedContainerIn"] = t.struct(
        {
            "fullResourceName": t.string().optional(),
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyIn"]).optional(),
            "parent": t.string().optional(),
            "policyBundle": t.array(t.proxy(renames["AnalyzerOrgPolicyIn"])).optional(),
        }
    ).named(renames["GoogleCloudAssetV1GovernedContainerIn"])
    types["GoogleCloudAssetV1GovernedContainerOut"] = t.struct(
        {
            "fullResourceName": t.string().optional(),
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyOut"]).optional(),
            "parent": t.string().optional(),
            "policyBundle": t.array(
                t.proxy(renames["AnalyzerOrgPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1GovernedContainerOut"])
    types["AnalyzeIamPolicyLongrunningResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AnalyzeIamPolicyLongrunningResponseIn"])
    types["AnalyzeIamPolicyLongrunningResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AnalyzeIamPolicyLongrunningResponseOut"])
    types["ExportAssetsRequestIn"] = t.struct(
        {
            "relationshipTypes": t.array(t.string()).optional(),
            "readTime": t.string().optional(),
            "assetTypes": t.array(t.string()).optional(),
            "outputConfig": t.proxy(renames["OutputConfigIn"]),
            "contentType": t.string().optional(),
        }
    ).named(renames["ExportAssetsRequestIn"])
    types["ExportAssetsRequestOut"] = t.struct(
        {
            "relationshipTypes": t.array(t.string()).optional(),
            "readTime": t.string().optional(),
            "assetTypes": t.array(t.string()).optional(),
            "outputConfig": t.proxy(renames["OutputConfigOut"]),
            "contentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportAssetsRequestOut"])
    types["WindowsApplicationIn"] = t.struct(
        {
            "installDate": t.proxy(renames["DateIn"]).optional(),
            "helpLink": t.string().optional(),
            "displayName": t.string().optional(),
            "publisher": t.string().optional(),
            "displayVersion": t.string().optional(),
        }
    ).named(renames["WindowsApplicationIn"])
    types["WindowsApplicationOut"] = t.struct(
        {
            "installDate": t.proxy(renames["DateOut"]).optional(),
            "helpLink": t.string().optional(),
            "displayName": t.string().optional(),
            "publisher": t.string().optional(),
            "displayVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsApplicationOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["GoogleCloudAssetV1AccessControlListIn"] = t.struct(
        {
            "accesses": t.array(
                t.proxy(renames["GoogleCloudAssetV1AccessIn"])
            ).optional(),
            "conditionEvaluation": t.proxy(renames["ConditionEvaluationIn"]).optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudAssetV1ResourceIn"])
            ).optional(),
            "resourceEdges": t.array(
                t.proxy(renames["GoogleCloudAssetV1EdgeIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudAssetV1AccessControlListIn"])
    types["GoogleCloudAssetV1AccessControlListOut"] = t.struct(
        {
            "accesses": t.array(
                t.proxy(renames["GoogleCloudAssetV1AccessOut"])
            ).optional(),
            "conditionEvaluation": t.proxy(
                renames["ConditionEvaluationOut"]
            ).optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudAssetV1ResourceOut"])
            ).optional(),
            "resourceEdges": t.array(
                t.proxy(renames["GoogleCloudAssetV1EdgeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1AccessControlListOut"])
    types["GoogleCloudAssetV1p7beta1AssetIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "iamPolicy": t.proxy(renames["PolicyIn"]).optional(),
            "relatedAssets": t.proxy(
                renames["GoogleCloudAssetV1p7beta1RelatedAssetsIn"]
            ).optional(),
            "name": t.string().optional(),
            "resource": t.proxy(
                renames["GoogleCloudAssetV1p7beta1ResourceIn"]
            ).optional(),
            "servicePerimeter": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn"]
            ).optional(),
            "ancestors": t.array(t.string()).optional(),
            "accessPolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyIn"]
            ).optional(),
            "assetType": t.string().optional(),
            "orgPolicy": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV1PolicyIn"])
            ).optional(),
            "accessLevel": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessLevelIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1AssetIn"])
    types["GoogleCloudAssetV1p7beta1AssetOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "iamPolicy": t.proxy(renames["PolicyOut"]).optional(),
            "relatedAssets": t.proxy(
                renames["GoogleCloudAssetV1p7beta1RelatedAssetsOut"]
            ).optional(),
            "name": t.string().optional(),
            "resource": t.proxy(
                renames["GoogleCloudAssetV1p7beta1ResourceOut"]
            ).optional(),
            "servicePerimeter": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut"]
            ).optional(),
            "ancestors": t.array(t.string()).optional(),
            "accessPolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyOut"]
            ).optional(),
            "assetType": t.string().optional(),
            "orgPolicy": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV1PolicyOut"])
            ).optional(),
            "accessLevel": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessLevelOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1AssetOut"])
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
    types["GoogleCloudAssetV1DeniedAccessAccessTupleIn"] = t.struct(
        {
            "access": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessAccessIn"]
            ).optional(),
            "resource": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessResourceIn"]
            ).optional(),
            "identity": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessIdentityIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessAccessTupleIn"])
    types["GoogleCloudAssetV1DeniedAccessAccessTupleOut"] = t.struct(
        {
            "access": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessAccessOut"]
            ).optional(),
            "resource": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessResourceOut"]
            ).optional(),
            "identity": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessIdentityOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessAccessTupleOut"])
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
    types["GoogleCloudAssetV1GcsDestinationIn"] = t.struct({"uri": t.string()}).named(
        renames["GoogleCloudAssetV1GcsDestinationIn"]
    )
    types["GoogleCloudAssetV1GcsDestinationOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudAssetV1GcsDestinationOut"])
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
    types["GoogleIdentityAccesscontextmanagerV1EgressPolicyIn"] = t.struct(
        {
            "egressTo": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1EgressToIn"]
            ).optional(),
            "egressFrom": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1EgressFromIn"]
            ).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1EgressPolicyIn"])
    types["GoogleIdentityAccesscontextmanagerV1EgressPolicyOut"] = t.struct(
        {
            "egressTo": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1EgressToOut"]
            ).optional(),
            "egressFrom": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1EgressFromOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1EgressPolicyOut"])
    types["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn"] = t.struct(
        {
            "ingressPolicies": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1IngressPolicyIn"])
            ).optional(),
            "resources": t.array(t.string()).optional(),
            "egressPolicies": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1EgressPolicyIn"])
            ).optional(),
            "accessLevels": t.array(t.string()).optional(),
            "restrictedServices": t.array(t.string()).optional(),
            "vpcAccessibleServices": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesIn"]
            ).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn"])
    types["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut"] = t.struct(
        {
            "ingressPolicies": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1IngressPolicyOut"])
            ).optional(),
            "resources": t.array(t.string()).optional(),
            "egressPolicies": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1EgressPolicyOut"])
            ).optional(),
            "accessLevels": t.array(t.string()).optional(),
            "restrictedServices": t.array(t.string()).optional(),
            "vpcAccessibleServices": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut"])
    types["GoogleCloudAssetV1p7beta1ResourceIn"] = t.struct(
        {
            "discoveryName": t.string().optional(),
            "resourceUrl": t.string().optional(),
            "parent": t.string().optional(),
            "version": t.string().optional(),
            "location": t.string().optional(),
            "discoveryDocumentUri": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1ResourceIn"])
    types["GoogleCloudAssetV1p7beta1ResourceOut"] = t.struct(
        {
            "discoveryName": t.string().optional(),
            "resourceUrl": t.string().optional(),
            "parent": t.string().optional(),
            "version": t.string().optional(),
            "location": t.string().optional(),
            "discoveryDocumentUri": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1ResourceOut"])
    types["GoogleCloudAssetV1ConstraintIn"] = t.struct(
        {
            "listConstraint": t.proxy(
                renames["GoogleCloudAssetV1ListConstraintIn"]
            ).optional(),
            "name": t.string().optional(),
            "constraintDefault": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "booleanConstraint": t.proxy(
                renames["GoogleCloudAssetV1BooleanConstraintIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudAssetV1ConstraintIn"])
    types["GoogleCloudAssetV1ConstraintOut"] = t.struct(
        {
            "listConstraint": t.proxy(
                renames["GoogleCloudAssetV1ListConstraintOut"]
            ).optional(),
            "name": t.string().optional(),
            "constraintDefault": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "booleanConstraint": t.proxy(
                renames["GoogleCloudAssetV1BooleanConstraintOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1ConstraintOut"])
    types["GoogleCloudOrgpolicyV1PolicyIn"] = t.struct(
        {
            "listPolicy": t.proxy(
                renames["GoogleCloudOrgpolicyV1ListPolicyIn"]
            ).optional(),
            "restoreDefault": t.proxy(
                renames["GoogleCloudOrgpolicyV1RestoreDefaultIn"]
            ).optional(),
            "version": t.integer().optional(),
            "constraint": t.string().optional(),
            "etag": t.string().optional(),
            "updateTime": t.string().optional(),
            "booleanPolicy": t.proxy(
                renames["GoogleCloudOrgpolicyV1BooleanPolicyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1PolicyIn"])
    types["GoogleCloudOrgpolicyV1PolicyOut"] = t.struct(
        {
            "listPolicy": t.proxy(
                renames["GoogleCloudOrgpolicyV1ListPolicyOut"]
            ).optional(),
            "restoreDefault": t.proxy(
                renames["GoogleCloudOrgpolicyV1RestoreDefaultOut"]
            ).optional(),
            "version": t.integer().optional(),
            "constraint": t.string().optional(),
            "etag": t.string().optional(),
            "updateTime": t.string().optional(),
            "booleanPolicy": t.proxy(
                renames["GoogleCloudOrgpolicyV1BooleanPolicyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1PolicyOut"])
    types["PubsubDestinationIn"] = t.struct({"topic": t.string().optional()}).named(
        renames["PubsubDestinationIn"]
    )
    types["PubsubDestinationOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubDestinationOut"])
    types["GoogleCloudAssetV1EdgeIn"] = t.struct(
        {"targetNode": t.string().optional(), "sourceNode": t.string().optional()}
    ).named(renames["GoogleCloudAssetV1EdgeIn"])
    types["GoogleCloudAssetV1EdgeOut"] = t.struct(
        {
            "targetNode": t.string().optional(),
            "sourceNode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1EdgeOut"])
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
    types["IamPolicyAnalysisStateIn"] = t.struct(
        {"code": t.string().optional(), "cause": t.string().optional()}
    ).named(renames["IamPolicyAnalysisStateIn"])
    types["IamPolicyAnalysisStateOut"] = t.struct(
        {
            "code": t.string().optional(),
            "cause": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisStateOut"])
    types[
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyIn"
    ] = t.struct(
        {
            "folders": t.array(t.string()).optional(),
            "attachedResource": t.string().optional(),
            "organization": t.string().optional(),
            "project": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
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
            "attachedResource": t.string().optional(),
            "organization": t.string().optional(),
            "project": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyOut"
        ]
    )
    types["AnalyzeIamPolicyResponseIn"] = t.struct(
        {
            "mainAnalysis": t.proxy(renames["IamPolicyAnalysisIn"]).optional(),
            "fullyExplored": t.boolean().optional(),
            "serviceAccountImpersonationAnalysis": t.array(
                t.proxy(renames["IamPolicyAnalysisIn"])
            ).optional(),
        }
    ).named(renames["AnalyzeIamPolicyResponseIn"])
    types["AnalyzeIamPolicyResponseOut"] = t.struct(
        {
            "mainAnalysis": t.proxy(renames["IamPolicyAnalysisOut"]).optional(),
            "fullyExplored": t.boolean().optional(),
            "serviceAccountImpersonationAnalysis": t.array(
                t.proxy(renames["IamPolicyAnalysisOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeIamPolicyResponseOut"])
    types["RelatedResourceIn"] = t.struct(
        {"fullResourceName": t.string().optional(), "assetType": t.string().optional()}
    ).named(renames["RelatedResourceIn"])
    types["RelatedResourceOut"] = t.struct(
        {
            "fullResourceName": t.string().optional(),
            "assetType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelatedResourceOut"])
    types["DeniedAccessIn"] = t.struct(
        {
            "deniedAccessTuple": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessAccessTupleIn"]
            ).optional(),
            "denyDetails": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessDenyDetailIn"])
            ).optional(),
        }
    ).named(renames["DeniedAccessIn"])
    types["DeniedAccessOut"] = t.struct(
        {
            "deniedAccessTuple": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessAccessTupleOut"]
            ).optional(),
            "denyDetails": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessDenyDetailOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeniedAccessOut"])
    types["GoogleIdentityAccesscontextmanagerV1ApiOperationIn"] = t.struct(
        {
            "methodSelectors": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1MethodSelectorIn"])
            ).optional(),
            "serviceName": t.string().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ApiOperationIn"])
    types["GoogleIdentityAccesscontextmanagerV1ApiOperationOut"] = t.struct(
        {
            "methodSelectors": t.array(
                t.proxy(
                    renames["GoogleIdentityAccesscontextmanagerV1MethodSelectorOut"]
                )
            ).optional(),
            "serviceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ApiOperationOut"])
    types["GoogleIdentityAccesscontextmanagerV1CustomLevelIn"] = t.struct(
        {"expr": t.proxy(renames["ExprIn"])}
    ).named(renames["GoogleIdentityAccesscontextmanagerV1CustomLevelIn"])
    types["GoogleIdentityAccesscontextmanagerV1CustomLevelOut"] = t.struct(
        {
            "expr": t.proxy(renames["ExprOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1CustomLevelOut"])
    types["GoogleCloudOrgpolicyV1ListPolicyIn"] = t.struct(
        {
            "allValues": t.string().optional(),
            "deniedValues": t.array(t.string()).optional(),
            "inheritFromParent": t.boolean().optional(),
            "allowedValues": t.array(t.string()).optional(),
            "suggestedValue": t.string().optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1ListPolicyIn"])
    types["GoogleCloudOrgpolicyV1ListPolicyOut"] = t.struct(
        {
            "allValues": t.string().optional(),
            "deniedValues": t.array(t.string()).optional(),
            "inheritFromParent": t.boolean().optional(),
            "allowedValues": t.array(t.string()).optional(),
            "suggestedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1ListPolicyOut"])
    types["IamPolicyAnalysisResultIn"] = t.struct(
        {
            "fullyExplored": t.boolean().optional(),
            "iamBinding": t.proxy(renames["BindingIn"]).optional(),
            "accessControlLists": t.array(
                t.proxy(renames["GoogleCloudAssetV1AccessControlListIn"])
            ).optional(),
            "identityList": t.proxy(
                renames["GoogleCloudAssetV1IdentityListIn"]
            ).optional(),
            "attachedResourceFullName": t.string().optional(),
        }
    ).named(renames["IamPolicyAnalysisResultIn"])
    types["IamPolicyAnalysisResultOut"] = t.struct(
        {
            "fullyExplored": t.boolean().optional(),
            "iamBinding": t.proxy(renames["BindingOut"]).optional(),
            "accessControlLists": t.array(
                t.proxy(renames["GoogleCloudAssetV1AccessControlListOut"])
            ).optional(),
            "identityList": t.proxy(
                renames["GoogleCloudAssetV1IdentityListOut"]
            ).optional(),
            "attachedResourceFullName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisResultOut"])
    types["GoogleCloudAssetV1IdentityListIn"] = t.struct(
        {
            "identities": t.array(
                t.proxy(renames["GoogleCloudAssetV1IdentityIn"])
            ).optional(),
            "groupEdges": t.array(
                t.proxy(renames["GoogleCloudAssetV1EdgeIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudAssetV1IdentityListIn"])
    types["GoogleCloudAssetV1IdentityListOut"] = t.struct(
        {
            "identities": t.array(
                t.proxy(renames["GoogleCloudAssetV1IdentityOut"])
            ).optional(),
            "groupEdges": t.array(
                t.proxy(renames["GoogleCloudAssetV1EdgeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1IdentityListOut"])
    types["GoogleIdentityAccesscontextmanagerV1ConditionIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "regions": t.array(t.string()).optional(),
            "devicePolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1DevicePolicyIn"]
            ).optional(),
            "requiredAccessLevels": t.array(t.string()).optional(),
            "negate": t.boolean().optional(),
            "ipSubnetworks": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ConditionIn"])
    types["GoogleIdentityAccesscontextmanagerV1ConditionOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "regions": t.array(t.string()).optional(),
            "devicePolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1DevicePolicyOut"]
            ).optional(),
            "requiredAccessLevels": t.array(t.string()).optional(),
            "negate": t.boolean().optional(),
            "ipSubnetworks": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ConditionOut"])
    types["ResourceSelectorIn"] = t.struct({"fullResourceName": t.string()}).named(
        renames["ResourceSelectorIn"]
    )
    types["ResourceSelectorOut"] = t.struct(
        {
            "fullResourceName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceSelectorOut"])
    types["GoogleCloudAssetV1CustomConstraintIn"] = t.struct(
        {
            "description": t.string().optional(),
            "condition": t.string().optional(),
            "methodTypes": t.array(t.string()).optional(),
            "resourceTypes": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "actionType": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1CustomConstraintIn"])
    types["GoogleCloudAssetV1CustomConstraintOut"] = t.struct(
        {
            "description": t.string().optional(),
            "condition": t.string().optional(),
            "methodTypes": t.array(t.string()).optional(),
            "resourceTypes": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "actionType": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1CustomConstraintOut"])
    types["AnalyzerOrgPolicyIn"] = t.struct(
        {
            "reset": t.boolean().optional(),
            "rules": t.array(t.proxy(renames["GoogleCloudAssetV1RuleIn"])).optional(),
            "attachedResource": t.string().optional(),
            "appliedResource": t.string().optional(),
            "inheritFromParent": t.boolean().optional(),
        }
    ).named(renames["AnalyzerOrgPolicyIn"])
    types["AnalyzerOrgPolicyOut"] = t.struct(
        {
            "reset": t.boolean().optional(),
            "rules": t.array(t.proxy(renames["GoogleCloudAssetV1RuleOut"])).optional(),
            "attachedResource": t.string().optional(),
            "appliedResource": t.string().optional(),
            "inheritFromParent": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzerOrgPolicyOut"])
    types["QueryAssetsRequestIn"] = t.struct(
        {
            "statement": t.string().optional(),
            "timeout": t.string().optional(),
            "readTime": t.string().optional(),
            "outputConfig": t.proxy(renames["QueryAssetsOutputConfigIn"]).optional(),
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "jobReference": t.string().optional(),
            "readTimeWindow": t.proxy(renames["TimeWindowIn"]).optional(),
        }
    ).named(renames["QueryAssetsRequestIn"])
    types["QueryAssetsRequestOut"] = t.struct(
        {
            "statement": t.string().optional(),
            "timeout": t.string().optional(),
            "readTime": t.string().optional(),
            "outputConfig": t.proxy(renames["QueryAssetsOutputConfigOut"]).optional(),
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "jobReference": t.string().optional(),
            "readTimeWindow": t.proxy(renames["TimeWindowOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryAssetsRequestOut"])
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
    types["QueryResultIn"] = t.struct(
        {
            "totalRows": t.string().optional(),
            "rows": t.array(t.struct({"_": t.string().optional()})).optional(),
            "nextPageToken": t.string().optional(),
            "schema": t.proxy(renames["TableSchemaIn"]).optional(),
        }
    ).named(renames["QueryResultIn"])
    types["QueryResultOut"] = t.struct(
        {
            "totalRows": t.string().optional(),
            "rows": t.array(t.struct({"_": t.string().optional()})).optional(),
            "nextPageToken": t.string().optional(),
            "schema": t.proxy(renames["TableSchemaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResultOut"])
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
    types["InventoryIn"] = t.struct(
        {
            "items": t.struct({"_": t.string().optional()}).optional(),
            "osInfo": t.proxy(renames["OsInfoIn"]).optional(),
        }
    ).named(renames["InventoryIn"])
    types["InventoryOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "items": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "osInfo": t.proxy(renames["OsInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryOut"])
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
    types["AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
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
    types["IdentitySelectorIn"] = t.struct({"identity": t.string()}).named(
        renames["IdentitySelectorIn"]
    )
    types["IdentitySelectorOut"] = t.struct(
        {"identity": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IdentitySelectorOut"])
    types["ResourceIn"] = t.struct(
        {
            "version": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "resourceUrl": t.string().optional(),
            "discoveryDocumentUri": t.string().optional(),
            "discoveryName": t.string().optional(),
            "location": t.string().optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "version": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "resourceUrl": t.string().optional(),
            "discoveryDocumentUri": t.string().optional(),
            "discoveryName": t.string().optional(),
            "location": t.string().optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["AnalyzeIamPolicyLongrunningRequestIn"] = t.struct(
        {
            "analysisQuery": t.proxy(renames["IamPolicyAnalysisQueryIn"]),
            "savedAnalysisQuery": t.string().optional(),
            "outputConfig": t.proxy(renames["IamPolicyAnalysisOutputConfigIn"]),
        }
    ).named(renames["AnalyzeIamPolicyLongrunningRequestIn"])
    types["AnalyzeIamPolicyLongrunningRequestOut"] = t.struct(
        {
            "analysisQuery": t.proxy(renames["IamPolicyAnalysisQueryOut"]),
            "savedAnalysisQuery": t.string().optional(),
            "outputConfig": t.proxy(renames["IamPolicyAnalysisOutputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeIamPolicyLongrunningRequestOut"])
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
    types["GoogleCloudAssetV1p7beta1RelatedAssetsIn"] = t.struct(
        {
            "assets": t.array(
                t.proxy(renames["GoogleCloudAssetV1p7beta1RelatedAssetIn"])
            ).optional(),
            "relationshipAttributes": t.proxy(
                renames["GoogleCloudAssetV1p7beta1RelationshipAttributesIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1RelatedAssetsIn"])
    types["GoogleCloudAssetV1p7beta1RelatedAssetsOut"] = t.struct(
        {
            "assets": t.array(
                t.proxy(renames["GoogleCloudAssetV1p7beta1RelatedAssetOut"])
            ).optional(),
            "relationshipAttributes": t.proxy(
                renames["GoogleCloudAssetV1p7beta1RelationshipAttributesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1RelatedAssetsOut"])
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
    types["ConditionContextIn"] = t.struct({"accessTime": t.string().optional()}).named(
        renames["ConditionContextIn"]
    )
    types["ConditionContextOut"] = t.struct(
        {
            "accessTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionContextOut"])
    types["SoftwarePackageIn"] = t.struct(
        {
            "zypperPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
            "googetPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
            "qfePackage": t.proxy(
                renames["WindowsQuickFixEngineeringPackageIn"]
            ).optional(),
            "yumPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
            "wuaPackage": t.proxy(renames["WindowsUpdatePackageIn"]).optional(),
            "windowsApplication": t.proxy(renames["WindowsApplicationIn"]).optional(),
            "cosPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
            "zypperPatch": t.proxy(renames["ZypperPatchIn"]).optional(),
            "aptPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
        }
    ).named(renames["SoftwarePackageIn"])
    types["SoftwarePackageOut"] = t.struct(
        {
            "zypperPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "googetPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "qfePackage": t.proxy(
                renames["WindowsQuickFixEngineeringPackageOut"]
            ).optional(),
            "yumPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "wuaPackage": t.proxy(renames["WindowsUpdatePackageOut"]).optional(),
            "windowsApplication": t.proxy(renames["WindowsApplicationOut"]).optional(),
            "cosPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "zypperPatch": t.proxy(renames["ZypperPatchOut"]).optional(),
            "aptPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SoftwarePackageOut"])
    types["GoogleCloudAssetV1DeniedAccessDenyDetailIn"] = t.struct(
        {
            "denyRule": t.proxy(renames["GoogleIamV2DenyRuleIn"]).optional(),
            "identities": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessIdentityIn"])
            ).optional(),
            "accesses": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessAccessIn"])
            ).optional(),
            "fullyDenied": t.boolean().optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessResourceIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessDenyDetailIn"])
    types["GoogleCloudAssetV1DeniedAccessDenyDetailOut"] = t.struct(
        {
            "denyRule": t.proxy(renames["GoogleIamV2DenyRuleOut"]).optional(),
            "identities": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessIdentityOut"])
            ).optional(),
            "accesses": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessAccessOut"])
            ).optional(),
            "fullyDenied": t.boolean().optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessResourceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessDenyDetailOut"])
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
    types["TableFieldSchemaIn"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["TableFieldSchemaIn"])).optional(),
            "mode": t.string().optional(),
            "type": t.string().optional(),
            "field": t.string().optional(),
        }
    ).named(renames["TableFieldSchemaIn"])
    types["TableFieldSchemaOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["TableFieldSchemaOut"])).optional(),
            "mode": t.string().optional(),
            "type": t.string().optional(),
            "field": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableFieldSchemaOut"])
    types["AnalyzeOrgPolicyGovernedAssetsResponseIn"] = t.struct(
        {
            "governedAssets": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetIn"
                    ]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "constraint": t.proxy(renames["AnalyzerOrgPolicyConstraintIn"]).optional(),
        }
    ).named(renames["AnalyzeOrgPolicyGovernedAssetsResponseIn"])
    types["AnalyzeOrgPolicyGovernedAssetsResponseOut"] = t.struct(
        {
            "governedAssets": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetOut"
                    ]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "constraint": t.proxy(renames["AnalyzerOrgPolicyConstraintOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeOrgPolicyGovernedAssetsResponseOut"])
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
    types["TimeWindowIn"] = t.struct(
        {"startTime": t.string().optional(), "endTime": t.string().optional()}
    ).named(renames["TimeWindowIn"])
    types["TimeWindowOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeWindowOut"])
    types["GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn"] = t.struct(
        {
            "status": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn"]
            ).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "spec": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn"]
            ).optional(),
            "perimeterType": t.string().optional(),
            "useExplicitDryRunSpec": t.boolean().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn"])
    types["GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut"] = t.struct(
        {
            "status": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut"]
            ).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "spec": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut"]
            ).optional(),
            "perimeterType": t.string().optional(),
            "useExplicitDryRunSpec": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut"])
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
    types["ZypperPatchIn"] = t.struct(
        {
            "summary": t.string().optional(),
            "severity": t.string().optional(),
            "category": t.string().optional(),
            "patchName": t.string().optional(),
        }
    ).named(renames["ZypperPatchIn"])
    types["ZypperPatchOut"] = t.struct(
        {
            "summary": t.string().optional(),
            "severity": t.string().optional(),
            "category": t.string().optional(),
            "patchName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZypperPatchOut"])
    types["OptionsIn"] = t.struct(
        {
            "includeDenyPolicyAnalysis": t.boolean().optional(),
            "analyzeServiceAccountImpersonation": t.boolean().optional(),
            "expandResources": t.boolean().optional(),
            "outputResourceEdges": t.boolean().optional(),
            "expandGroups": t.boolean().optional(),
            "outputGroupEdges": t.boolean().optional(),
            "expandRoles": t.boolean().optional(),
        }
    ).named(renames["OptionsIn"])
    types["OptionsOut"] = t.struct(
        {
            "includeDenyPolicyAnalysis": t.boolean().optional(),
            "analyzeServiceAccountImpersonation": t.boolean().optional(),
            "expandResources": t.boolean().optional(),
            "outputResourceEdges": t.boolean().optional(),
            "expandGroups": t.boolean().optional(),
            "outputGroupEdges": t.boolean().optional(),
            "expandRoles": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionsOut"])
    types["GoogleIdentityAccesscontextmanagerV1DevicePolicyIn"] = t.struct(
        {
            "allowedEncryptionStatuses": t.array(t.string()).optional(),
            "requireCorpOwned": t.boolean().optional(),
            "osConstraints": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1OsConstraintIn"])
            ).optional(),
            "allowedDeviceManagementLevels": t.array(t.string()).optional(),
            "requireAdminApproval": t.boolean().optional(),
            "requireScreenlock": t.boolean().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1DevicePolicyIn"])
    types["GoogleIdentityAccesscontextmanagerV1DevicePolicyOut"] = t.struct(
        {
            "allowedEncryptionStatuses": t.array(t.string()).optional(),
            "requireCorpOwned": t.boolean().optional(),
            "osConstraints": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1OsConstraintOut"])
            ).optional(),
            "allowedDeviceManagementLevels": t.array(t.string()).optional(),
            "requireAdminApproval": t.boolean().optional(),
            "requireScreenlock": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1DevicePolicyOut"])
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
    types["AnalyzeOrgPoliciesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "constraint": t.proxy(renames["AnalyzerOrgPolicyConstraintIn"]).optional(),
            "orgPolicyResults": t.array(
                t.proxy(renames["OrgPolicyResultIn"])
            ).optional(),
        }
    ).named(renames["AnalyzeOrgPoliciesResponseIn"])
    types["AnalyzeOrgPoliciesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "constraint": t.proxy(renames["AnalyzerOrgPolicyConstraintOut"]).optional(),
            "orgPolicyResults": t.array(
                t.proxy(renames["OrgPolicyResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeOrgPoliciesResponseOut"])
    types["AnalyzeIamPolicyLongrunningMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AnalyzeIamPolicyLongrunningMetadataIn"])
    types["AnalyzeIamPolicyLongrunningMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeIamPolicyLongrunningMetadataOut"])
    types["SearchAllResourcesResponseIn"] = t.struct(
        {
            "results": t.array(t.proxy(renames["ResourceSearchResultIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchAllResourcesResponseIn"])
    types["SearchAllResourcesResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["ResourceSearchResultOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchAllResourcesResponseOut"])
    types["ListFeedsResponseIn"] = t.struct(
        {"feeds": t.array(t.proxy(renames["FeedIn"])).optional()}
    ).named(renames["ListFeedsResponseIn"])
    types["ListFeedsResponseOut"] = t.struct(
        {
            "feeds": t.array(t.proxy(renames["FeedOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFeedsResponseOut"])
    types["AnalyzeMoveResponseIn"] = t.struct(
        {"moveAnalysis": t.array(t.proxy(renames["MoveAnalysisIn"])).optional()}
    ).named(renames["AnalyzeMoveResponseIn"])
    types["AnalyzeMoveResponseOut"] = t.struct(
        {
            "moveAnalysis": t.array(t.proxy(renames["MoveAnalysisOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeMoveResponseOut"])
    types["BatchGetAssetsHistoryResponseIn"] = t.struct(
        {"assets": t.array(t.proxy(renames["TemporalAssetIn"])).optional()}
    ).named(renames["BatchGetAssetsHistoryResponseIn"])
    types["BatchGetAssetsHistoryResponseOut"] = t.struct(
        {
            "assets": t.array(t.proxy(renames["TemporalAssetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetAssetsHistoryResponseOut"])
    types["TableSchemaIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["TableFieldSchemaIn"])).optional()}
    ).named(renames["TableSchemaIn"])
    types["TableSchemaOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["TableFieldSchemaOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableSchemaOut"])
    types["GoogleCloudAssetV1ListConstraintIn"] = t.struct(
        {"supportsUnder": t.boolean().optional(), "supportsIn": t.boolean().optional()}
    ).named(renames["GoogleCloudAssetV1ListConstraintIn"])
    types["GoogleCloudAssetV1ListConstraintOut"] = t.struct(
        {
            "supportsUnder": t.boolean().optional(),
            "supportsIn": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1ListConstraintOut"])
    types["GoogleCloudAssetV1RuleIn"] = t.struct(
        {
            "enforce": t.boolean().optional(),
            "denyAll": t.boolean().optional(),
            "values": t.proxy(renames["GoogleCloudAssetV1StringValuesIn"]).optional(),
            "allowAll": t.boolean().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1RuleIn"])
    types["GoogleCloudAssetV1RuleOut"] = t.struct(
        {
            "enforce": t.boolean().optional(),
            "denyAll": t.boolean().optional(),
            "values": t.proxy(renames["GoogleCloudAssetV1StringValuesOut"]).optional(),
            "allowAll": t.boolean().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1RuleOut"])
    types["RelationshipAttributesIn"] = t.struct(
        {
            "sourceResourceType": t.string().optional(),
            "targetResourceType": t.string().optional(),
            "action": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["RelationshipAttributesIn"])
    types["RelationshipAttributesOut"] = t.struct(
        {
            "sourceResourceType": t.string().optional(),
            "targetResourceType": t.string().optional(),
            "action": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationshipAttributesOut"])
    types["GoogleCloudAssetV1BigQueryDestinationIn"] = t.struct(
        {
            "partitionKey": t.string().optional(),
            "dataset": t.string(),
            "tablePrefix": t.string(),
            "writeDisposition": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1BigQueryDestinationIn"])
    types["GoogleCloudAssetV1BigQueryDestinationOut"] = t.struct(
        {
            "partitionKey": t.string().optional(),
            "dataset": t.string(),
            "tablePrefix": t.string(),
            "writeDisposition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1BigQueryDestinationOut"])
    types["GoogleCloudAssetV1DeniedAccessResourceIn"] = t.struct(
        {"fullResourceName": t.string().optional()}
    ).named(renames["GoogleCloudAssetV1DeniedAccessResourceIn"])
    types["GoogleCloudAssetV1DeniedAccessResourceOut"] = t.struct(
        {
            "fullResourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessResourceOut"])
    types[
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceIn"
    ] = t.struct(
        {
            "project": t.string().optional(),
            "organization": t.string().optional(),
            "folders": t.array(t.string()).optional(),
            "parent": t.string().optional(),
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
            "project": t.string().optional(),
            "organization": t.string().optional(),
            "folders": t.array(t.string()).optional(),
            "parent": t.string().optional(),
            "fullResourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceOut"
        ]
    )
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
    types["GoogleCloudAssetV1DeniedAccessIdentityIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["GoogleCloudAssetV1DeniedAccessIdentityIn"])
    types["GoogleCloudAssetV1DeniedAccessIdentityOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessIdentityOut"])

    functions = {}
    functions["savedQueriesPatch"] = cloudasset.get(
        "v1/{parent}/savedQueries",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSavedQueriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["savedQueriesGet"] = cloudasset.get(
        "v1/{parent}/savedQueries",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSavedQueriesResponseOut"]),
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
    functions["v1SearchAllIamPolicies"] = cloudasset.post(
        "v1/{parent}:queryAssets",
        t.struct(
            {
                "parent": t.string(),
                "statement": t.string().optional(),
                "timeout": t.string().optional(),
                "readTime": t.string().optional(),
                "outputConfig": t.proxy(
                    renames["QueryAssetsOutputConfigIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "jobReference": t.string().optional(),
                "readTimeWindow": t.proxy(renames["TimeWindowIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeOrgPolicyGovernedContainers"] = cloudasset.post(
        "v1/{parent}:queryAssets",
        t.struct(
            {
                "parent": t.string(),
                "statement": t.string().optional(),
                "timeout": t.string().optional(),
                "readTime": t.string().optional(),
                "outputConfig": t.proxy(
                    renames["QueryAssetsOutputConfigIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "jobReference": t.string().optional(),
                "readTimeWindow": t.proxy(renames["TimeWindowIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeIamPolicyLongrunning"] = cloudasset.post(
        "v1/{parent}:queryAssets",
        t.struct(
            {
                "parent": t.string(),
                "statement": t.string().optional(),
                "timeout": t.string().optional(),
                "readTime": t.string().optional(),
                "outputConfig": t.proxy(
                    renames["QueryAssetsOutputConfigIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "jobReference": t.string().optional(),
                "readTimeWindow": t.proxy(renames["TimeWindowIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1ExportAssets"] = cloudasset.post(
        "v1/{parent}:queryAssets",
        t.struct(
            {
                "parent": t.string(),
                "statement": t.string().optional(),
                "timeout": t.string().optional(),
                "readTime": t.string().optional(),
                "outputConfig": t.proxy(
                    renames["QueryAssetsOutputConfigIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "jobReference": t.string().optional(),
                "readTimeWindow": t.proxy(renames["TimeWindowIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeMove"] = cloudasset.post(
        "v1/{parent}:queryAssets",
        t.struct(
            {
                "parent": t.string(),
                "statement": t.string().optional(),
                "timeout": t.string().optional(),
                "readTime": t.string().optional(),
                "outputConfig": t.proxy(
                    renames["QueryAssetsOutputConfigIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "jobReference": t.string().optional(),
                "readTimeWindow": t.proxy(renames["TimeWindowIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeOrgPolicies"] = cloudasset.post(
        "v1/{parent}:queryAssets",
        t.struct(
            {
                "parent": t.string(),
                "statement": t.string().optional(),
                "timeout": t.string().optional(),
                "readTime": t.string().optional(),
                "outputConfig": t.proxy(
                    renames["QueryAssetsOutputConfigIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "jobReference": t.string().optional(),
                "readTimeWindow": t.proxy(renames["TimeWindowIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1SearchAllResources"] = cloudasset.post(
        "v1/{parent}:queryAssets",
        t.struct(
            {
                "parent": t.string(),
                "statement": t.string().optional(),
                "timeout": t.string().optional(),
                "readTime": t.string().optional(),
                "outputConfig": t.proxy(
                    renames["QueryAssetsOutputConfigIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "jobReference": t.string().optional(),
                "readTimeWindow": t.proxy(renames["TimeWindowIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeIamPolicy"] = cloudasset.post(
        "v1/{parent}:queryAssets",
        t.struct(
            {
                "parent": t.string(),
                "statement": t.string().optional(),
                "timeout": t.string().optional(),
                "readTime": t.string().optional(),
                "outputConfig": t.proxy(
                    renames["QueryAssetsOutputConfigIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "jobReference": t.string().optional(),
                "readTimeWindow": t.proxy(renames["TimeWindowIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1BatchGetAssetsHistory"] = cloudasset.post(
        "v1/{parent}:queryAssets",
        t.struct(
            {
                "parent": t.string(),
                "statement": t.string().optional(),
                "timeout": t.string().optional(),
                "readTime": t.string().optional(),
                "outputConfig": t.proxy(
                    renames["QueryAssetsOutputConfigIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "jobReference": t.string().optional(),
                "readTimeWindow": t.proxy(renames["TimeWindowIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeOrgPolicyGovernedAssets"] = cloudasset.post(
        "v1/{parent}:queryAssets",
        t.struct(
            {
                "parent": t.string(),
                "statement": t.string().optional(),
                "timeout": t.string().optional(),
                "readTime": t.string().optional(),
                "outputConfig": t.proxy(
                    renames["QueryAssetsOutputConfigIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "jobReference": t.string().optional(),
                "readTimeWindow": t.proxy(renames["TimeWindowIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1QueryAssets"] = cloudasset.post(
        "v1/{parent}:queryAssets",
        t.struct(
            {
                "parent": t.string(),
                "statement": t.string().optional(),
                "timeout": t.string().optional(),
                "readTime": t.string().optional(),
                "outputConfig": t.proxy(
                    renames["QueryAssetsOutputConfigIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "jobReference": t.string().optional(),
                "readTimeWindow": t.proxy(renames["TimeWindowIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryAssetsResponseOut"]),
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
    functions["feedsGet"] = cloudasset.delete(
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
    functions["feedsList"] = cloudasset.delete(
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
    functions["assetsList"] = cloudasset.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "parent": t.string(),
                "readTime": t.string().optional(),
                "relationshipTypes": t.string().optional(),
                "pageSize": t.integer().optional(),
                "assetTypes": t.string().optional(),
                "pageToken": t.string().optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
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

    return Import(
        importer="cloudasset", renames=renames, types=types, functions=functions
    )
