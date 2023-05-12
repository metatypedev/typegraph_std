from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_cloudasset() -> Import:
    cloudasset = HTTPRuntime("https://cloudasset.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudasset_1_ErrorResponse",
        "VersionedPackageIn": "_cloudasset_2_VersionedPackageIn",
        "VersionedPackageOut": "_cloudasset_3_VersionedPackageOut",
        "BigQueryDestinationIn": "_cloudasset_4_BigQueryDestinationIn",
        "BigQueryDestinationOut": "_cloudasset_5_BigQueryDestinationOut",
        "QueryAssetsOutputConfigIn": "_cloudasset_6_QueryAssetsOutputConfigIn",
        "QueryAssetsOutputConfigOut": "_cloudasset_7_QueryAssetsOutputConfigOut",
        "ExportAssetsRequestIn": "_cloudasset_8_ExportAssetsRequestIn",
        "ExportAssetsRequestOut": "_cloudasset_9_ExportAssetsRequestOut",
        "IamPolicyAnalysisIn": "_cloudasset_10_IamPolicyAnalysisIn",
        "IamPolicyAnalysisOut": "_cloudasset_11_IamPolicyAnalysisOut",
        "ExprIn": "_cloudasset_12_ExprIn",
        "ExprOut": "_cloudasset_13_ExprOut",
        "IamPolicyAnalysisQueryIn": "_cloudasset_14_IamPolicyAnalysisQueryIn",
        "IamPolicyAnalysisQueryOut": "_cloudasset_15_IamPolicyAnalysisQueryOut",
        "BatchGetEffectiveIamPoliciesResponseIn": "_cloudasset_16_BatchGetEffectiveIamPoliciesResponseIn",
        "BatchGetEffectiveIamPoliciesResponseOut": "_cloudasset_17_BatchGetEffectiveIamPoliciesResponseOut",
        "IamPolicyAnalysisStateIn": "_cloudasset_18_IamPolicyAnalysisStateIn",
        "IamPolicyAnalysisStateOut": "_cloudasset_19_IamPolicyAnalysisStateOut",
        "RelatedResourceIn": "_cloudasset_20_RelatedResourceIn",
        "RelatedResourceOut": "_cloudasset_21_RelatedResourceOut",
        "GoogleIdentityAccesscontextmanagerV1AccessLevelIn": "_cloudasset_22_GoogleIdentityAccesscontextmanagerV1AccessLevelIn",
        "GoogleIdentityAccesscontextmanagerV1AccessLevelOut": "_cloudasset_23_GoogleIdentityAccesscontextmanagerV1AccessLevelOut",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceIn": "_cloudasset_24_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceIn",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceOut": "_cloudasset_25_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceOut",
        "VersionedResourceIn": "_cloudasset_26_VersionedResourceIn",
        "VersionedResourceOut": "_cloudasset_27_VersionedResourceOut",
        "InventoryIn": "_cloudasset_28_InventoryIn",
        "InventoryOut": "_cloudasset_29_InventoryOut",
        "WindowsUpdateCategoryIn": "_cloudasset_30_WindowsUpdateCategoryIn",
        "WindowsUpdateCategoryOut": "_cloudasset_31_WindowsUpdateCategoryOut",
        "GoogleIdentityAccesscontextmanagerV1EgressPolicyIn": "_cloudasset_32_GoogleIdentityAccesscontextmanagerV1EgressPolicyIn",
        "GoogleIdentityAccesscontextmanagerV1EgressPolicyOut": "_cloudasset_33_GoogleIdentityAccesscontextmanagerV1EgressPolicyOut",
        "GoogleCloudAssetV1DeniedAccessResourceIn": "_cloudasset_34_GoogleCloudAssetV1DeniedAccessResourceIn",
        "GoogleCloudAssetV1DeniedAccessResourceOut": "_cloudasset_35_GoogleCloudAssetV1DeniedAccessResourceOut",
        "GoogleCloudAssetV1p7beta1ResourceIn": "_cloudasset_36_GoogleCloudAssetV1p7beta1ResourceIn",
        "GoogleCloudAssetV1p7beta1ResourceOut": "_cloudasset_37_GoogleCloudAssetV1p7beta1ResourceOut",
        "DeniedAccessIn": "_cloudasset_38_DeniedAccessIn",
        "DeniedAccessOut": "_cloudasset_39_DeniedAccessOut",
        "AuditConfigIn": "_cloudasset_40_AuditConfigIn",
        "AuditConfigOut": "_cloudasset_41_AuditConfigOut",
        "AnalyzeOrgPolicyGovernedAssetsResponseIn": "_cloudasset_42_AnalyzeOrgPolicyGovernedAssetsResponseIn",
        "AnalyzeOrgPolicyGovernedAssetsResponseOut": "_cloudasset_43_AnalyzeOrgPolicyGovernedAssetsResponseOut",
        "GcsDestinationIn": "_cloudasset_44_GcsDestinationIn",
        "GcsDestinationOut": "_cloudasset_45_GcsDestinationOut",
        "GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesIn": "_cloudasset_46_GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesIn",
        "GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesOut": "_cloudasset_47_GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesOut",
        "IamPolicyAnalysisOutputConfigIn": "_cloudasset_48_IamPolicyAnalysisOutputConfigIn",
        "IamPolicyAnalysisOutputConfigOut": "_cloudasset_49_IamPolicyAnalysisOutputConfigOut",
        "GoogleCloudAssetV1IdentityIn": "_cloudasset_50_GoogleCloudAssetV1IdentityIn",
        "GoogleCloudAssetV1IdentityOut": "_cloudasset_51_GoogleCloudAssetV1IdentityOut",
        "EffectiveIamPolicyIn": "_cloudasset_52_EffectiveIamPolicyIn",
        "EffectiveIamPolicyOut": "_cloudasset_53_EffectiveIamPolicyOut",
        "AnalyzeIamPolicyResponseIn": "_cloudasset_54_AnalyzeIamPolicyResponseIn",
        "AnalyzeIamPolicyResponseOut": "_cloudasset_55_AnalyzeIamPolicyResponseOut",
        "GoogleCloudAssetV1IdentityListIn": "_cloudasset_56_GoogleCloudAssetV1IdentityListIn",
        "GoogleCloudAssetV1IdentityListOut": "_cloudasset_57_GoogleCloudAssetV1IdentityListOut",
        "GoogleCloudAssetV1ConstraintIn": "_cloudasset_58_GoogleCloudAssetV1ConstraintIn",
        "GoogleCloudAssetV1ConstraintOut": "_cloudasset_59_GoogleCloudAssetV1ConstraintOut",
        "ItemIn": "_cloudasset_60_ItemIn",
        "ItemOut": "_cloudasset_61_ItemOut",
        "GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationIn": "_cloudasset_62_GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationIn",
        "GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationOut": "_cloudasset_63_GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationOut",
        "GoogleCloudAssetV1p7beta1RelationshipAttributesIn": "_cloudasset_64_GoogleCloudAssetV1p7beta1RelationshipAttributesIn",
        "GoogleCloudAssetV1p7beta1RelationshipAttributesOut": "_cloudasset_65_GoogleCloudAssetV1p7beta1RelationshipAttributesOut",
        "AnalyzeIamPolicyLongrunningMetadataIn": "_cloudasset_66_AnalyzeIamPolicyLongrunningMetadataIn",
        "AnalyzeIamPolicyLongrunningMetadataOut": "_cloudasset_67_AnalyzeIamPolicyLongrunningMetadataOut",
        "GoogleCloudAssetV1p7beta1RelatedAssetsIn": "_cloudasset_68_GoogleCloudAssetV1p7beta1RelatedAssetsIn",
        "GoogleCloudAssetV1p7beta1RelatedAssetsOut": "_cloudasset_69_GoogleCloudAssetV1p7beta1RelatedAssetsOut",
        "RelatedAssetsIn": "_cloudasset_70_RelatedAssetsIn",
        "RelatedAssetsOut": "_cloudasset_71_RelatedAssetsOut",
        "OsInfoIn": "_cloudasset_72_OsInfoIn",
        "OsInfoOut": "_cloudasset_73_OsInfoOut",
        "QueryContentIn": "_cloudasset_74_QueryContentIn",
        "QueryContentOut": "_cloudasset_75_QueryContentOut",
        "ConditionContextIn": "_cloudasset_76_ConditionContextIn",
        "ConditionContextOut": "_cloudasset_77_ConditionContextOut",
        "TableSchemaIn": "_cloudasset_78_TableSchemaIn",
        "TableSchemaOut": "_cloudasset_79_TableSchemaOut",
        "FeedOutputConfigIn": "_cloudasset_80_FeedOutputConfigIn",
        "FeedOutputConfigOut": "_cloudasset_81_FeedOutputConfigOut",
        "SoftwarePackageIn": "_cloudasset_82_SoftwarePackageIn",
        "SoftwarePackageOut": "_cloudasset_83_SoftwarePackageOut",
        "GoogleIdentityAccesscontextmanagerV1ApiOperationIn": "_cloudasset_84_GoogleIdentityAccesscontextmanagerV1ApiOperationIn",
        "GoogleIdentityAccesscontextmanagerV1ApiOperationOut": "_cloudasset_85_GoogleIdentityAccesscontextmanagerV1ApiOperationOut",
        "QueryAssetsRequestIn": "_cloudasset_86_QueryAssetsRequestIn",
        "QueryAssetsRequestOut": "_cloudasset_87_QueryAssetsRequestOut",
        "CreateFeedRequestIn": "_cloudasset_88_CreateFeedRequestIn",
        "CreateFeedRequestOut": "_cloudasset_89_CreateFeedRequestOut",
        "GoogleCloudOrgpolicyV1PolicyIn": "_cloudasset_90_GoogleCloudOrgpolicyV1PolicyIn",
        "GoogleCloudOrgpolicyV1PolicyOut": "_cloudasset_91_GoogleCloudOrgpolicyV1PolicyOut",
        "GoogleCloudAssetV1RuleIn": "_cloudasset_92_GoogleCloudAssetV1RuleIn",
        "GoogleCloudAssetV1RuleOut": "_cloudasset_93_GoogleCloudAssetV1RuleOut",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetIn": "_cloudasset_94_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetIn",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetOut": "_cloudasset_95_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetOut",
        "GoogleIdentityAccesscontextmanagerV1ConditionIn": "_cloudasset_96_GoogleIdentityAccesscontextmanagerV1ConditionIn",
        "GoogleIdentityAccesscontextmanagerV1ConditionOut": "_cloudasset_97_GoogleIdentityAccesscontextmanagerV1ConditionOut",
        "GoogleCloudAssetV1p7beta1AssetIn": "_cloudasset_98_GoogleCloudAssetV1p7beta1AssetIn",
        "GoogleCloudAssetV1p7beta1AssetOut": "_cloudasset_99_GoogleCloudAssetV1p7beta1AssetOut",
        "GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn": "_cloudasset_100_GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn",
        "GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut": "_cloudasset_101_GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut",
        "GoogleIdentityAccesscontextmanagerV1BasicLevelIn": "_cloudasset_102_GoogleIdentityAccesscontextmanagerV1BasicLevelIn",
        "GoogleIdentityAccesscontextmanagerV1BasicLevelOut": "_cloudasset_103_GoogleIdentityAccesscontextmanagerV1BasicLevelOut",
        "ResourceIn": "_cloudasset_104_ResourceIn",
        "ResourceOut": "_cloudasset_105_ResourceOut",
        "MoveImpactIn": "_cloudasset_106_MoveImpactIn",
        "MoveImpactOut": "_cloudasset_107_MoveImpactOut",
        "PubsubDestinationIn": "_cloudasset_108_PubsubDestinationIn",
        "PubsubDestinationOut": "_cloudasset_109_PubsubDestinationOut",
        "GoogleCloudAssetV1BigQueryDestinationIn": "_cloudasset_110_GoogleCloudAssetV1BigQueryDestinationIn",
        "GoogleCloudAssetV1BigQueryDestinationOut": "_cloudasset_111_GoogleCloudAssetV1BigQueryDestinationOut",
        "RelationshipAttributesIn": "_cloudasset_112_RelationshipAttributesIn",
        "RelationshipAttributesOut": "_cloudasset_113_RelationshipAttributesOut",
        "GoogleCloudAssetV1p7beta1RelatedAssetIn": "_cloudasset_114_GoogleCloudAssetV1p7beta1RelatedAssetIn",
        "GoogleCloudAssetV1p7beta1RelatedAssetOut": "_cloudasset_115_GoogleCloudAssetV1p7beta1RelatedAssetOut",
        "GoogleIdentityAccesscontextmanagerV1EgressToIn": "_cloudasset_116_GoogleIdentityAccesscontextmanagerV1EgressToIn",
        "GoogleIdentityAccesscontextmanagerV1EgressToOut": "_cloudasset_117_GoogleIdentityAccesscontextmanagerV1EgressToOut",
        "SavedQueryIn": "_cloudasset_118_SavedQueryIn",
        "SavedQueryOut": "_cloudasset_119_SavedQueryOut",
        "ResourceSearchResultIn": "_cloudasset_120_ResourceSearchResultIn",
        "ResourceSearchResultOut": "_cloudasset_121_ResourceSearchResultOut",
        "GoogleIdentityAccesscontextmanagerV1MethodSelectorIn": "_cloudasset_122_GoogleIdentityAccesscontextmanagerV1MethodSelectorIn",
        "GoogleIdentityAccesscontextmanagerV1MethodSelectorOut": "_cloudasset_123_GoogleIdentityAccesscontextmanagerV1MethodSelectorOut",
        "OperationIn": "_cloudasset_124_OperationIn",
        "OperationOut": "_cloudasset_125_OperationOut",
        "GoogleCloudAssetV1ResourceIn": "_cloudasset_126_GoogleCloudAssetV1ResourceIn",
        "GoogleCloudAssetV1ResourceOut": "_cloudasset_127_GoogleCloudAssetV1ResourceOut",
        "AnalyzerOrgPolicyIn": "_cloudasset_128_AnalyzerOrgPolicyIn",
        "AnalyzerOrgPolicyOut": "_cloudasset_129_AnalyzerOrgPolicyOut",
        "QueryAssetsResponseIn": "_cloudasset_130_QueryAssetsResponseIn",
        "QueryAssetsResponseOut": "_cloudasset_131_QueryAssetsResponseOut",
        "GoogleCloudAssetV1StringValuesIn": "_cloudasset_132_GoogleCloudAssetV1StringValuesIn",
        "GoogleCloudAssetV1StringValuesOut": "_cloudasset_133_GoogleCloudAssetV1StringValuesOut",
        "OptionsIn": "_cloudasset_134_OptionsIn",
        "OptionsOut": "_cloudasset_135_OptionsOut",
        "PermissionsIn": "_cloudasset_136_PermissionsIn",
        "PermissionsOut": "_cloudasset_137_PermissionsOut",
        "GoogleCloudAssetV1GovernedContainerIn": "_cloudasset_138_GoogleCloudAssetV1GovernedContainerIn",
        "GoogleCloudAssetV1GovernedContainerOut": "_cloudasset_139_GoogleCloudAssetV1GovernedContainerOut",
        "AnalyzeIamPolicyLongrunningResponseIn": "_cloudasset_140_AnalyzeIamPolicyLongrunningResponseIn",
        "AnalyzeIamPolicyLongrunningResponseOut": "_cloudasset_141_AnalyzeIamPolicyLongrunningResponseOut",
        "MoveAnalysisIn": "_cloudasset_142_MoveAnalysisIn",
        "MoveAnalysisOut": "_cloudasset_143_MoveAnalysisOut",
        "GoogleIdentityAccesscontextmanagerV1IngressSourceIn": "_cloudasset_144_GoogleIdentityAccesscontextmanagerV1IngressSourceIn",
        "GoogleIdentityAccesscontextmanagerV1IngressSourceOut": "_cloudasset_145_GoogleIdentityAccesscontextmanagerV1IngressSourceOut",
        "GoogleIdentityAccesscontextmanagerV1IngressFromIn": "_cloudasset_146_GoogleIdentityAccesscontextmanagerV1IngressFromIn",
        "GoogleIdentityAccesscontextmanagerV1IngressFromOut": "_cloudasset_147_GoogleIdentityAccesscontextmanagerV1IngressFromOut",
        "ListSavedQueriesResponseIn": "_cloudasset_148_ListSavedQueriesResponseIn",
        "ListSavedQueriesResponseOut": "_cloudasset_149_ListSavedQueriesResponseOut",
        "TableFieldSchemaIn": "_cloudasset_150_TableFieldSchemaIn",
        "TableFieldSchemaOut": "_cloudasset_151_TableFieldSchemaOut",
        "QueryResultIn": "_cloudasset_152_QueryResultIn",
        "QueryResultOut": "_cloudasset_153_QueryResultOut",
        "GoogleCloudAssetV1CustomConstraintIn": "_cloudasset_154_GoogleCloudAssetV1CustomConstraintIn",
        "GoogleCloudAssetV1CustomConstraintOut": "_cloudasset_155_GoogleCloudAssetV1CustomConstraintOut",
        "GoogleCloudAssetV1DeniedAccessAccessTupleIn": "_cloudasset_156_GoogleCloudAssetV1DeniedAccessAccessTupleIn",
        "GoogleCloudAssetV1DeniedAccessAccessTupleOut": "_cloudasset_157_GoogleCloudAssetV1DeniedAccessAccessTupleOut",
        "GoogleCloudAssetV1DeniedAccessIdentityIn": "_cloudasset_158_GoogleCloudAssetV1DeniedAccessIdentityIn",
        "GoogleCloudAssetV1DeniedAccessIdentityOut": "_cloudasset_159_GoogleCloudAssetV1DeniedAccessIdentityOut",
        "IamPolicySearchResultIn": "_cloudasset_160_IamPolicySearchResultIn",
        "IamPolicySearchResultOut": "_cloudasset_161_IamPolicySearchResultOut",
        "GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn": "_cloudasset_162_GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn",
        "GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut": "_cloudasset_163_GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut",
        "OrgPolicyResultIn": "_cloudasset_164_OrgPolicyResultIn",
        "OrgPolicyResultOut": "_cloudasset_165_OrgPolicyResultOut",
        "AccessSelectorIn": "_cloudasset_166_AccessSelectorIn",
        "AccessSelectorOut": "_cloudasset_167_AccessSelectorOut",
        "GoogleCloudAssetV1ListConstraintIn": "_cloudasset_168_GoogleCloudAssetV1ListConstraintIn",
        "GoogleCloudAssetV1ListConstraintOut": "_cloudasset_169_GoogleCloudAssetV1ListConstraintOut",
        "UpdateFeedRequestIn": "_cloudasset_170_UpdateFeedRequestIn",
        "UpdateFeedRequestOut": "_cloudasset_171_UpdateFeedRequestOut",
        "ConditionEvaluationIn": "_cloudasset_172_ConditionEvaluationIn",
        "ConditionEvaluationOut": "_cloudasset_173_ConditionEvaluationOut",
        "BatchGetAssetsHistoryResponseIn": "_cloudasset_174_BatchGetAssetsHistoryResponseIn",
        "BatchGetAssetsHistoryResponseOut": "_cloudasset_175_BatchGetAssetsHistoryResponseOut",
        "GoogleIdentityAccesscontextmanagerV1DevicePolicyIn": "_cloudasset_176_GoogleIdentityAccesscontextmanagerV1DevicePolicyIn",
        "GoogleIdentityAccesscontextmanagerV1DevicePolicyOut": "_cloudasset_177_GoogleIdentityAccesscontextmanagerV1DevicePolicyOut",
        "RelatedResourcesIn": "_cloudasset_178_RelatedResourcesIn",
        "RelatedResourcesOut": "_cloudasset_179_RelatedResourcesOut",
        "PolicyInfoIn": "_cloudasset_180_PolicyInfoIn",
        "PolicyInfoOut": "_cloudasset_181_PolicyInfoOut",
        "GoogleIamV2DenyRuleIn": "_cloudasset_182_GoogleIamV2DenyRuleIn",
        "GoogleIamV2DenyRuleOut": "_cloudasset_183_GoogleIamV2DenyRuleOut",
        "ExplanationIn": "_cloudasset_184_ExplanationIn",
        "ExplanationOut": "_cloudasset_185_ExplanationOut",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyIn": "_cloudasset_186_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyIn",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyOut": "_cloudasset_187_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyOut",
        "DateIn": "_cloudasset_188_DateIn",
        "DateOut": "_cloudasset_189_DateOut",
        "AssetIn": "_cloudasset_190_AssetIn",
        "AssetOut": "_cloudasset_191_AssetOut",
        "GoogleIdentityAccesscontextmanagerV1CustomLevelIn": "_cloudasset_192_GoogleIdentityAccesscontextmanagerV1CustomLevelIn",
        "GoogleIdentityAccesscontextmanagerV1CustomLevelOut": "_cloudasset_193_GoogleIdentityAccesscontextmanagerV1CustomLevelOut",
        "GoogleIdentityAccesscontextmanagerV1EgressFromIn": "_cloudasset_194_GoogleIdentityAccesscontextmanagerV1EgressFromIn",
        "GoogleIdentityAccesscontextmanagerV1EgressFromOut": "_cloudasset_195_GoogleIdentityAccesscontextmanagerV1EgressFromOut",
        "GoogleCloudOrgpolicyV1ListPolicyIn": "_cloudasset_196_GoogleCloudOrgpolicyV1ListPolicyIn",
        "GoogleCloudOrgpolicyV1ListPolicyOut": "_cloudasset_197_GoogleCloudOrgpolicyV1ListPolicyOut",
        "AnalyzeOrgPoliciesResponseIn": "_cloudasset_198_AnalyzeOrgPoliciesResponseIn",
        "AnalyzeOrgPoliciesResponseOut": "_cloudasset_199_AnalyzeOrgPoliciesResponseOut",
        "GoogleCloudAssetV1AccessIn": "_cloudasset_200_GoogleCloudAssetV1AccessIn",
        "GoogleCloudAssetV1AccessOut": "_cloudasset_201_GoogleCloudAssetV1AccessOut",
        "GoogleCloudOrgpolicyV1RestoreDefaultIn": "_cloudasset_202_GoogleCloudOrgpolicyV1RestoreDefaultIn",
        "GoogleCloudOrgpolicyV1RestoreDefaultOut": "_cloudasset_203_GoogleCloudOrgpolicyV1RestoreDefaultOut",
        "AuditLogConfigIn": "_cloudasset_204_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudasset_205_AuditLogConfigOut",
        "GoogleCloudAssetV1AccessControlListIn": "_cloudasset_206_GoogleCloudAssetV1AccessControlListIn",
        "GoogleCloudAssetV1AccessControlListOut": "_cloudasset_207_GoogleCloudAssetV1AccessControlListOut",
        "AnalyzeOrgPolicyGovernedContainersResponseIn": "_cloudasset_208_AnalyzeOrgPolicyGovernedContainersResponseIn",
        "AnalyzeOrgPolicyGovernedContainersResponseOut": "_cloudasset_209_AnalyzeOrgPolicyGovernedContainersResponseOut",
        "GoogleIdentityAccesscontextmanagerV1AccessPolicyIn": "_cloudasset_210_GoogleIdentityAccesscontextmanagerV1AccessPolicyIn",
        "GoogleIdentityAccesscontextmanagerV1AccessPolicyOut": "_cloudasset_211_GoogleIdentityAccesscontextmanagerV1AccessPolicyOut",
        "BindingIn": "_cloudasset_212_BindingIn",
        "BindingOut": "_cloudasset_213_BindingOut",
        "ListAssetsResponseIn": "_cloudasset_214_ListAssetsResponseIn",
        "ListAssetsResponseOut": "_cloudasset_215_ListAssetsResponseOut",
        "TimeWindowIn": "_cloudasset_216_TimeWindowIn",
        "TimeWindowOut": "_cloudasset_217_TimeWindowOut",
        "GoogleCloudAssetV1DeniedAccessDenyDetailIn": "_cloudasset_218_GoogleCloudAssetV1DeniedAccessDenyDetailIn",
        "GoogleCloudAssetV1DeniedAccessDenyDetailOut": "_cloudasset_219_GoogleCloudAssetV1DeniedAccessDenyDetailOut",
        "WindowsApplicationIn": "_cloudasset_220_WindowsApplicationIn",
        "WindowsApplicationOut": "_cloudasset_221_WindowsApplicationOut",
        "SearchAllResourcesResponseIn": "_cloudasset_222_SearchAllResourcesResponseIn",
        "SearchAllResourcesResponseOut": "_cloudasset_223_SearchAllResourcesResponseOut",
        "PartitionSpecIn": "_cloudasset_224_PartitionSpecIn",
        "PartitionSpecOut": "_cloudasset_225_PartitionSpecOut",
        "GoogleIdentityAccesscontextmanagerV1OsConstraintIn": "_cloudasset_226_GoogleIdentityAccesscontextmanagerV1OsConstraintIn",
        "GoogleIdentityAccesscontextmanagerV1OsConstraintOut": "_cloudasset_227_GoogleIdentityAccesscontextmanagerV1OsConstraintOut",
        "TemporalAssetIn": "_cloudasset_228_TemporalAssetIn",
        "TemporalAssetOut": "_cloudasset_229_TemporalAssetOut",
        "IamPolicyAnalysisResultIn": "_cloudasset_230_IamPolicyAnalysisResultIn",
        "IamPolicyAnalysisResultOut": "_cloudasset_231_IamPolicyAnalysisResultOut",
        "GoogleCloudAssetV1EdgeIn": "_cloudasset_232_GoogleCloudAssetV1EdgeIn",
        "GoogleCloudAssetV1EdgeOut": "_cloudasset_233_GoogleCloudAssetV1EdgeOut",
        "SearchAllIamPoliciesResponseIn": "_cloudasset_234_SearchAllIamPoliciesResponseIn",
        "SearchAllIamPoliciesResponseOut": "_cloudasset_235_SearchAllIamPoliciesResponseOut",
        "ResourceSelectorIn": "_cloudasset_236_ResourceSelectorIn",
        "ResourceSelectorOut": "_cloudasset_237_ResourceSelectorOut",
        "FeedIn": "_cloudasset_238_FeedIn",
        "FeedOut": "_cloudasset_239_FeedOut",
        "AttachedResourceIn": "_cloudasset_240_AttachedResourceIn",
        "AttachedResourceOut": "_cloudasset_241_AttachedResourceOut",
        "PolicyIn": "_cloudasset_242_PolicyIn",
        "PolicyOut": "_cloudasset_243_PolicyOut",
        "GoogleCloudOrgpolicyV1BooleanPolicyIn": "_cloudasset_244_GoogleCloudOrgpolicyV1BooleanPolicyIn",
        "GoogleCloudOrgpolicyV1BooleanPolicyOut": "_cloudasset_245_GoogleCloudOrgpolicyV1BooleanPolicyOut",
        "GoogleCloudAssetV1GcsDestinationIn": "_cloudasset_246_GoogleCloudAssetV1GcsDestinationIn",
        "GoogleCloudAssetV1GcsDestinationOut": "_cloudasset_247_GoogleCloudAssetV1GcsDestinationOut",
        "AnalyzeMoveResponseIn": "_cloudasset_248_AnalyzeMoveResponseIn",
        "AnalyzeMoveResponseOut": "_cloudasset_249_AnalyzeMoveResponseOut",
        "IdentitySelectorIn": "_cloudasset_250_IdentitySelectorIn",
        "IdentitySelectorOut": "_cloudasset_251_IdentitySelectorOut",
        "ZypperPatchIn": "_cloudasset_252_ZypperPatchIn",
        "ZypperPatchOut": "_cloudasset_253_ZypperPatchOut",
        "WindowsUpdatePackageIn": "_cloudasset_254_WindowsUpdatePackageIn",
        "WindowsUpdatePackageOut": "_cloudasset_255_WindowsUpdatePackageOut",
        "ListFeedsResponseIn": "_cloudasset_256_ListFeedsResponseIn",
        "ListFeedsResponseOut": "_cloudasset_257_ListFeedsResponseOut",
        "GoogleCloudAssetV1DeniedAccessAccessIn": "_cloudasset_258_GoogleCloudAssetV1DeniedAccessAccessIn",
        "GoogleCloudAssetV1DeniedAccessAccessOut": "_cloudasset_259_GoogleCloudAssetV1DeniedAccessAccessOut",
        "MoveAnalysisResultIn": "_cloudasset_260_MoveAnalysisResultIn",
        "MoveAnalysisResultOut": "_cloudasset_261_MoveAnalysisResultOut",
        "OutputConfigIn": "_cloudasset_262_OutputConfigIn",
        "OutputConfigOut": "_cloudasset_263_OutputConfigOut",
        "EmptyIn": "_cloudasset_264_EmptyIn",
        "EmptyOut": "_cloudasset_265_EmptyOut",
        "WindowsQuickFixEngineeringPackageIn": "_cloudasset_266_WindowsQuickFixEngineeringPackageIn",
        "WindowsQuickFixEngineeringPackageOut": "_cloudasset_267_WindowsQuickFixEngineeringPackageOut",
        "GoogleIdentityAccesscontextmanagerV1IngressToIn": "_cloudasset_268_GoogleIdentityAccesscontextmanagerV1IngressToIn",
        "GoogleIdentityAccesscontextmanagerV1IngressToOut": "_cloudasset_269_GoogleIdentityAccesscontextmanagerV1IngressToOut",
        "GoogleIdentityAccesscontextmanagerV1IngressPolicyIn": "_cloudasset_270_GoogleIdentityAccesscontextmanagerV1IngressPolicyIn",
        "GoogleIdentityAccesscontextmanagerV1IngressPolicyOut": "_cloudasset_271_GoogleIdentityAccesscontextmanagerV1IngressPolicyOut",
        "GoogleCloudAssetV1BooleanConstraintIn": "_cloudasset_272_GoogleCloudAssetV1BooleanConstraintIn",
        "GoogleCloudAssetV1BooleanConstraintOut": "_cloudasset_273_GoogleCloudAssetV1BooleanConstraintOut",
        "AnalyzerOrgPolicyConstraintIn": "_cloudasset_274_AnalyzerOrgPolicyConstraintIn",
        "AnalyzerOrgPolicyConstraintOut": "_cloudasset_275_AnalyzerOrgPolicyConstraintOut",
        "AnalyzeIamPolicyLongrunningRequestIn": "_cloudasset_276_AnalyzeIamPolicyLongrunningRequestIn",
        "AnalyzeIamPolicyLongrunningRequestOut": "_cloudasset_277_AnalyzeIamPolicyLongrunningRequestOut",
        "StatusIn": "_cloudasset_278_StatusIn",
        "StatusOut": "_cloudasset_279_StatusOut",
        "RelatedAssetIn": "_cloudasset_280_RelatedAssetIn",
        "RelatedAssetOut": "_cloudasset_281_RelatedAssetOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["VersionedPackageIn"] = t.struct(
        {
            "version": t.string().optional(),
            "architecture": t.string().optional(),
            "packageName": t.string().optional(),
        }
    ).named(renames["VersionedPackageIn"])
    types["VersionedPackageOut"] = t.struct(
        {
            "version": t.string().optional(),
            "architecture": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionedPackageOut"])
    types["BigQueryDestinationIn"] = t.struct(
        {
            "partitionSpec": t.proxy(renames["PartitionSpecIn"]).optional(),
            "force": t.boolean().optional(),
            "dataset": t.string(),
            "table": t.string(),
            "separateTablesPerAssetType": t.boolean().optional(),
        }
    ).named(renames["BigQueryDestinationIn"])
    types["BigQueryDestinationOut"] = t.struct(
        {
            "partitionSpec": t.proxy(renames["PartitionSpecOut"]).optional(),
            "force": t.boolean().optional(),
            "dataset": t.string(),
            "table": t.string(),
            "separateTablesPerAssetType": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDestinationOut"])
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
    types["ExportAssetsRequestIn"] = t.struct(
        {
            "relationshipTypes": t.array(t.string()).optional(),
            "outputConfig": t.proxy(renames["OutputConfigIn"]),
            "contentType": t.string().optional(),
            "readTime": t.string().optional(),
            "assetTypes": t.array(t.string()).optional(),
        }
    ).named(renames["ExportAssetsRequestIn"])
    types["ExportAssetsRequestOut"] = t.struct(
        {
            "relationshipTypes": t.array(t.string()).optional(),
            "outputConfig": t.proxy(renames["OutputConfigOut"]),
            "contentType": t.string().optional(),
            "readTime": t.string().optional(),
            "assetTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportAssetsRequestOut"])
    types["IamPolicyAnalysisIn"] = t.struct(
        {
            "analysisResults": t.array(
                t.proxy(renames["IamPolicyAnalysisResultIn"])
            ).optional(),
            "nonCriticalErrors": t.array(
                t.proxy(renames["IamPolicyAnalysisStateIn"])
            ).optional(),
            "deniedAccesses": t.array(t.proxy(renames["DeniedAccessIn"])).optional(),
            "fullyExplored": t.boolean().optional(),
            "analysisQuery": t.proxy(renames["IamPolicyAnalysisQueryIn"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisIn"])
    types["IamPolicyAnalysisOut"] = t.struct(
        {
            "analysisResults": t.array(
                t.proxy(renames["IamPolicyAnalysisResultOut"])
            ).optional(),
            "nonCriticalErrors": t.array(
                t.proxy(renames["IamPolicyAnalysisStateOut"])
            ).optional(),
            "deniedAccesses": t.array(t.proxy(renames["DeniedAccessOut"])).optional(),
            "fullyExplored": t.boolean().optional(),
            "analysisQuery": t.proxy(renames["IamPolicyAnalysisQueryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["IamPolicyAnalysisQueryIn"] = t.struct(
        {
            "options": t.proxy(renames["OptionsIn"]).optional(),
            "identitySelector": t.proxy(renames["IdentitySelectorIn"]).optional(),
            "scope": t.string(),
            "conditionContext": t.proxy(renames["ConditionContextIn"]).optional(),
            "accessSelector": t.proxy(renames["AccessSelectorIn"]).optional(),
            "resourceSelector": t.proxy(renames["ResourceSelectorIn"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisQueryIn"])
    types["IamPolicyAnalysisQueryOut"] = t.struct(
        {
            "options": t.proxy(renames["OptionsOut"]).optional(),
            "identitySelector": t.proxy(renames["IdentitySelectorOut"]).optional(),
            "scope": t.string(),
            "conditionContext": t.proxy(renames["ConditionContextOut"]).optional(),
            "accessSelector": t.proxy(renames["AccessSelectorOut"]).optional(),
            "resourceSelector": t.proxy(renames["ResourceSelectorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisQueryOut"])
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
    types["GoogleIdentityAccesscontextmanagerV1AccessLevelIn"] = t.struct(
        {
            "description": t.string().optional(),
            "custom": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1CustomLevelIn"]
            ).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "basic": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1BasicLevelIn"]
            ).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1AccessLevelIn"])
    types["GoogleIdentityAccesscontextmanagerV1AccessLevelOut"] = t.struct(
        {
            "description": t.string().optional(),
            "custom": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1CustomLevelOut"]
            ).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "basic": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1BasicLevelOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1AccessLevelOut"])
    types[
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceIn"
    ] = t.struct(
        {
            "folders": t.array(t.string()).optional(),
            "project": t.string().optional(),
            "organization": t.string().optional(),
            "fullResourceName": t.string().optional(),
            "parent": t.string().optional(),
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
            "organization": t.string().optional(),
            "fullResourceName": t.string().optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceOut"
        ]
    )
    types["VersionedResourceIn"] = t.struct(
        {
            "resource": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["VersionedResourceIn"])
    types["VersionedResourceOut"] = t.struct(
        {
            "resource": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionedResourceOut"])
    types["InventoryIn"] = t.struct(
        {
            "osInfo": t.proxy(renames["OsInfoIn"]).optional(),
            "items": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["InventoryIn"])
    types["InventoryOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "osInfo": t.proxy(renames["OsInfoOut"]).optional(),
            "items": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryOut"])
    types["WindowsUpdateCategoryIn"] = t.struct(
        {"id": t.string().optional(), "name": t.string().optional()}
    ).named(renames["WindowsUpdateCategoryIn"])
    types["WindowsUpdateCategoryOut"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsUpdateCategoryOut"])
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
    types["GoogleCloudAssetV1DeniedAccessResourceIn"] = t.struct(
        {"fullResourceName": t.string().optional()}
    ).named(renames["GoogleCloudAssetV1DeniedAccessResourceIn"])
    types["GoogleCloudAssetV1DeniedAccessResourceOut"] = t.struct(
        {
            "fullResourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessResourceOut"])
    types["GoogleCloudAssetV1p7beta1ResourceIn"] = t.struct(
        {
            "version": t.string().optional(),
            "discoveryName": t.string().optional(),
            "resourceUrl": t.string().optional(),
            "location": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "parent": t.string().optional(),
            "discoveryDocumentUri": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1ResourceIn"])
    types["GoogleCloudAssetV1p7beta1ResourceOut"] = t.struct(
        {
            "version": t.string().optional(),
            "discoveryName": t.string().optional(),
            "resourceUrl": t.string().optional(),
            "location": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "parent": t.string().optional(),
            "discoveryDocumentUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1ResourceOut"])
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
    types["AnalyzeOrgPolicyGovernedAssetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "constraint": t.proxy(renames["AnalyzerOrgPolicyConstraintIn"]).optional(),
            "governedAssets": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["AnalyzeOrgPolicyGovernedAssetsResponseIn"])
    types["AnalyzeOrgPolicyGovernedAssetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "constraint": t.proxy(renames["AnalyzerOrgPolicyConstraintOut"]).optional(),
            "governedAssets": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeOrgPolicyGovernedAssetsResponseOut"])
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
    types["GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesIn"] = t.struct(
        {
            "allowedServices": t.array(t.string()).optional(),
            "enableRestriction": t.boolean().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesIn"])
    types["GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesOut"] = t.struct(
        {
            "allowedServices": t.array(t.string()).optional(),
            "enableRestriction": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesOut"])
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
    types["AnalyzeIamPolicyResponseIn"] = t.struct(
        {
            "mainAnalysis": t.proxy(renames["IamPolicyAnalysisIn"]).optional(),
            "serviceAccountImpersonationAnalysis": t.array(
                t.proxy(renames["IamPolicyAnalysisIn"])
            ).optional(),
            "fullyExplored": t.boolean().optional(),
        }
    ).named(renames["AnalyzeIamPolicyResponseIn"])
    types["AnalyzeIamPolicyResponseOut"] = t.struct(
        {
            "mainAnalysis": t.proxy(renames["IamPolicyAnalysisOut"]).optional(),
            "serviceAccountImpersonationAnalysis": t.array(
                t.proxy(renames["IamPolicyAnalysisOut"])
            ).optional(),
            "fullyExplored": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeIamPolicyResponseOut"])
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
    types["GoogleCloudAssetV1ConstraintIn"] = t.struct(
        {
            "constraintDefault": t.string().optional(),
            "listConstraint": t.proxy(
                renames["GoogleCloudAssetV1ListConstraintIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "booleanConstraint": t.proxy(
                renames["GoogleCloudAssetV1BooleanConstraintIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1ConstraintIn"])
    types["GoogleCloudAssetV1ConstraintOut"] = t.struct(
        {
            "constraintDefault": t.string().optional(),
            "listConstraint": t.proxy(
                renames["GoogleCloudAssetV1ListConstraintOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "booleanConstraint": t.proxy(
                renames["GoogleCloudAssetV1BooleanConstraintOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1ConstraintOut"])
    types["ItemIn"] = t.struct(
        {
            "installedPackage": t.proxy(renames["SoftwarePackageIn"]).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "id": t.string().optional(),
            "originType": t.string().optional(),
            "type": t.string().optional(),
            "availablePackage": t.proxy(renames["SoftwarePackageIn"]).optional(),
        }
    ).named(renames["ItemIn"])
    types["ItemOut"] = t.struct(
        {
            "installedPackage": t.proxy(renames["SoftwarePackageOut"]).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "id": t.string().optional(),
            "originType": t.string().optional(),
            "type": t.string().optional(),
            "availablePackage": t.proxy(renames["SoftwarePackageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemOut"])
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
    types["GoogleCloudAssetV1p7beta1RelationshipAttributesIn"] = t.struct(
        {
            "targetResourceType": t.string().optional(),
            "sourceResourceType": t.string().optional(),
            "type": t.string().optional(),
            "action": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1RelationshipAttributesIn"])
    types["GoogleCloudAssetV1p7beta1RelationshipAttributesOut"] = t.struct(
        {
            "targetResourceType": t.string().optional(),
            "sourceResourceType": t.string().optional(),
            "type": t.string().optional(),
            "action": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1RelationshipAttributesOut"])
    types["AnalyzeIamPolicyLongrunningMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AnalyzeIamPolicyLongrunningMetadataIn"])
    types["AnalyzeIamPolicyLongrunningMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeIamPolicyLongrunningMetadataOut"])
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
    types["RelatedAssetsIn"] = t.struct(
        {
            "relationshipAttributes": t.proxy(
                renames["RelationshipAttributesIn"]
            ).optional(),
            "assets": t.array(t.proxy(renames["RelatedAssetIn"])).optional(),
        }
    ).named(renames["RelatedAssetsIn"])
    types["RelatedAssetsOut"] = t.struct(
        {
            "relationshipAttributes": t.proxy(
                renames["RelationshipAttributesOut"]
            ).optional(),
            "assets": t.array(t.proxy(renames["RelatedAssetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelatedAssetsOut"])
    types["OsInfoIn"] = t.struct(
        {
            "architecture": t.string().optional(),
            "shortName": t.string().optional(),
            "version": t.string().optional(),
            "kernelRelease": t.string().optional(),
            "kernelVersion": t.string().optional(),
            "osconfigAgentVersion": t.string().optional(),
            "longName": t.string().optional(),
            "hostname": t.string().optional(),
        }
    ).named(renames["OsInfoIn"])
    types["OsInfoOut"] = t.struct(
        {
            "architecture": t.string().optional(),
            "shortName": t.string().optional(),
            "version": t.string().optional(),
            "kernelRelease": t.string().optional(),
            "kernelVersion": t.string().optional(),
            "osconfigAgentVersion": t.string().optional(),
            "longName": t.string().optional(),
            "hostname": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OsInfoOut"])
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
    types["ConditionContextIn"] = t.struct({"accessTime": t.string().optional()}).named(
        renames["ConditionContextIn"]
    )
    types["ConditionContextOut"] = t.struct(
        {
            "accessTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionContextOut"])
    types["TableSchemaIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["TableFieldSchemaIn"])).optional()}
    ).named(renames["TableSchemaIn"])
    types["TableSchemaOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["TableFieldSchemaOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableSchemaOut"])
    types["FeedOutputConfigIn"] = t.struct(
        {"pubsubDestination": t.proxy(renames["PubsubDestinationIn"]).optional()}
    ).named(renames["FeedOutputConfigIn"])
    types["FeedOutputConfigOut"] = t.struct(
        {
            "pubsubDestination": t.proxy(renames["PubsubDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeedOutputConfigOut"])
    types["SoftwarePackageIn"] = t.struct(
        {
            "zypperPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
            "googetPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
            "yumPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
            "zypperPatch": t.proxy(renames["ZypperPatchIn"]).optional(),
            "windowsApplication": t.proxy(renames["WindowsApplicationIn"]).optional(),
            "qfePackage": t.proxy(
                renames["WindowsQuickFixEngineeringPackageIn"]
            ).optional(),
            "wuaPackage": t.proxy(renames["WindowsUpdatePackageIn"]).optional(),
            "cosPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
            "aptPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
        }
    ).named(renames["SoftwarePackageIn"])
    types["SoftwarePackageOut"] = t.struct(
        {
            "zypperPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "googetPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "yumPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "zypperPatch": t.proxy(renames["ZypperPatchOut"]).optional(),
            "windowsApplication": t.proxy(renames["WindowsApplicationOut"]).optional(),
            "qfePackage": t.proxy(
                renames["WindowsQuickFixEngineeringPackageOut"]
            ).optional(),
            "wuaPackage": t.proxy(renames["WindowsUpdatePackageOut"]).optional(),
            "cosPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "aptPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SoftwarePackageOut"])
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
    types["QueryAssetsRequestIn"] = t.struct(
        {
            "timeout": t.string().optional(),
            "readTime": t.string().optional(),
            "outputConfig": t.proxy(renames["QueryAssetsOutputConfigIn"]).optional(),
            "pageSize": t.integer().optional(),
            "jobReference": t.string().optional(),
            "readTimeWindow": t.proxy(renames["TimeWindowIn"]).optional(),
            "pageToken": t.string().optional(),
            "statement": t.string().optional(),
        }
    ).named(renames["QueryAssetsRequestIn"])
    types["QueryAssetsRequestOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "readTime": t.string().optional(),
            "outputConfig": t.proxy(renames["QueryAssetsOutputConfigOut"]).optional(),
            "pageSize": t.integer().optional(),
            "jobReference": t.string().optional(),
            "readTimeWindow": t.proxy(renames["TimeWindowOut"]).optional(),
            "pageToken": t.string().optional(),
            "statement": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryAssetsRequestOut"])
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
    types["GoogleCloudOrgpolicyV1PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "restoreDefault": t.proxy(
                renames["GoogleCloudOrgpolicyV1RestoreDefaultIn"]
            ).optional(),
            "booleanPolicy": t.proxy(
                renames["GoogleCloudOrgpolicyV1BooleanPolicyIn"]
            ).optional(),
            "listPolicy": t.proxy(
                renames["GoogleCloudOrgpolicyV1ListPolicyIn"]
            ).optional(),
            "constraint": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1PolicyIn"])
    types["GoogleCloudOrgpolicyV1PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "restoreDefault": t.proxy(
                renames["GoogleCloudOrgpolicyV1RestoreDefaultOut"]
            ).optional(),
            "booleanPolicy": t.proxy(
                renames["GoogleCloudOrgpolicyV1BooleanPolicyOut"]
            ).optional(),
            "listPolicy": t.proxy(
                renames["GoogleCloudOrgpolicyV1ListPolicyOut"]
            ).optional(),
            "constraint": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1PolicyOut"])
    types["GoogleCloudAssetV1RuleIn"] = t.struct(
        {
            "values": t.proxy(renames["GoogleCloudAssetV1StringValuesIn"]).optional(),
            "allowAll": t.boolean().optional(),
            "enforce": t.boolean().optional(),
            "denyAll": t.boolean().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1RuleIn"])
    types["GoogleCloudAssetV1RuleOut"] = t.struct(
        {
            "values": t.proxy(renames["GoogleCloudAssetV1StringValuesOut"]).optional(),
            "allowAll": t.boolean().optional(),
            "enforce": t.boolean().optional(),
            "denyAll": t.boolean().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1RuleOut"])
    types[
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetIn"
    ] = t.struct(
        {
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyIn"]).optional(),
            "governedIamPolicy": t.proxy(
                renames[
                    "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyIn"
                ]
            ).optional(),
            "policyBundle": t.array(t.proxy(renames["AnalyzerOrgPolicyIn"])).optional(),
            "governedResource": t.proxy(
                renames[
                    "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceIn"
                ]
            ).optional(),
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
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyOut"]).optional(),
            "governedIamPolicy": t.proxy(
                renames[
                    "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyOut"
                ]
            ).optional(),
            "policyBundle": t.array(
                t.proxy(renames["AnalyzerOrgPolicyOut"])
            ).optional(),
            "governedResource": t.proxy(
                renames[
                    "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetOut"
        ]
    )
    types["GoogleIdentityAccesscontextmanagerV1ConditionIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "negate": t.boolean().optional(),
            "regions": t.array(t.string()).optional(),
            "ipSubnetworks": t.array(t.string()).optional(),
            "devicePolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1DevicePolicyIn"]
            ).optional(),
            "requiredAccessLevels": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ConditionIn"])
    types["GoogleIdentityAccesscontextmanagerV1ConditionOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "negate": t.boolean().optional(),
            "regions": t.array(t.string()).optional(),
            "ipSubnetworks": t.array(t.string()).optional(),
            "devicePolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1DevicePolicyOut"]
            ).optional(),
            "requiredAccessLevels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ConditionOut"])
    types["GoogleCloudAssetV1p7beta1AssetIn"] = t.struct(
        {
            "accessLevel": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessLevelIn"]
            ).optional(),
            "assetType": t.string().optional(),
            "ancestors": t.array(t.string()).optional(),
            "relatedAssets": t.proxy(
                renames["GoogleCloudAssetV1p7beta1RelatedAssetsIn"]
            ).optional(),
            "name": t.string().optional(),
            "accessPolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyIn"]
            ).optional(),
            "servicePerimeter": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn"]
            ).optional(),
            "orgPolicy": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV1PolicyIn"])
            ).optional(),
            "iamPolicy": t.proxy(renames["PolicyIn"]).optional(),
            "resource": t.proxy(
                renames["GoogleCloudAssetV1p7beta1ResourceIn"]
            ).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1AssetIn"])
    types["GoogleCloudAssetV1p7beta1AssetOut"] = t.struct(
        {
            "accessLevel": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessLevelOut"]
            ).optional(),
            "assetType": t.string().optional(),
            "ancestors": t.array(t.string()).optional(),
            "relatedAssets": t.proxy(
                renames["GoogleCloudAssetV1p7beta1RelatedAssetsOut"]
            ).optional(),
            "name": t.string().optional(),
            "accessPolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyOut"]
            ).optional(),
            "servicePerimeter": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut"]
            ).optional(),
            "orgPolicy": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV1PolicyOut"])
            ).optional(),
            "iamPolicy": t.proxy(renames["PolicyOut"]).optional(),
            "resource": t.proxy(
                renames["GoogleCloudAssetV1p7beta1ResourceOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1AssetOut"])
    types["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn"] = t.struct(
        {
            "restrictedServices": t.array(t.string()).optional(),
            "vpcAccessibleServices": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesIn"]
            ).optional(),
            "resources": t.array(t.string()).optional(),
            "ingressPolicies": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1IngressPolicyIn"])
            ).optional(),
            "egressPolicies": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1EgressPolicyIn"])
            ).optional(),
            "accessLevels": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn"])
    types["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut"] = t.struct(
        {
            "restrictedServices": t.array(t.string()).optional(),
            "vpcAccessibleServices": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesOut"]
            ).optional(),
            "resources": t.array(t.string()).optional(),
            "ingressPolicies": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1IngressPolicyOut"])
            ).optional(),
            "egressPolicies": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1EgressPolicyOut"])
            ).optional(),
            "accessLevels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut"])
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
    types["ResourceIn"] = t.struct(
        {
            "discoveryDocumentUri": t.string().optional(),
            "discoveryName": t.string().optional(),
            "version": t.string().optional(),
            "location": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "resourceUrl": t.string().optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "discoveryDocumentUri": t.string().optional(),
            "discoveryName": t.string().optional(),
            "version": t.string().optional(),
            "location": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "resourceUrl": t.string().optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
    types["MoveImpactIn"] = t.struct({"detail": t.string().optional()}).named(
        renames["MoveImpactIn"]
    )
    types["MoveImpactOut"] = t.struct(
        {
            "detail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveImpactOut"])
    types["PubsubDestinationIn"] = t.struct({"topic": t.string().optional()}).named(
        renames["PubsubDestinationIn"]
    )
    types["PubsubDestinationOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubDestinationOut"])
    types["GoogleCloudAssetV1BigQueryDestinationIn"] = t.struct(
        {
            "dataset": t.string(),
            "partitionKey": t.string().optional(),
            "writeDisposition": t.string().optional(),
            "tablePrefix": t.string(),
        }
    ).named(renames["GoogleCloudAssetV1BigQueryDestinationIn"])
    types["GoogleCloudAssetV1BigQueryDestinationOut"] = t.struct(
        {
            "dataset": t.string(),
            "partitionKey": t.string().optional(),
            "writeDisposition": t.string().optional(),
            "tablePrefix": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1BigQueryDestinationOut"])
    types["RelationshipAttributesIn"] = t.struct(
        {
            "type": t.string().optional(),
            "action": t.string().optional(),
            "sourceResourceType": t.string().optional(),
            "targetResourceType": t.string().optional(),
        }
    ).named(renames["RelationshipAttributesIn"])
    types["RelationshipAttributesOut"] = t.struct(
        {
            "type": t.string().optional(),
            "action": t.string().optional(),
            "sourceResourceType": t.string().optional(),
            "targetResourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationshipAttributesOut"])
    types["GoogleCloudAssetV1p7beta1RelatedAssetIn"] = t.struct(
        {
            "ancestors": t.array(t.string()).optional(),
            "assetType": t.string().optional(),
            "asset": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1RelatedAssetIn"])
    types["GoogleCloudAssetV1p7beta1RelatedAssetOut"] = t.struct(
        {
            "ancestors": t.array(t.string()).optional(),
            "assetType": t.string().optional(),
            "asset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1RelatedAssetOut"])
    types["GoogleIdentityAccesscontextmanagerV1EgressToIn"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1ApiOperationIn"])
            ).optional(),
            "resources": t.array(t.string()).optional(),
            "externalResources": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1EgressToIn"])
    types["GoogleIdentityAccesscontextmanagerV1EgressToOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1ApiOperationOut"])
            ).optional(),
            "resources": t.array(t.string()).optional(),
            "externalResources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1EgressToOut"])
    types["SavedQueryIn"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "content": t.proxy(renames["QueryContentIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SavedQueryIn"])
    types["SavedQueryOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "creator": t.string().optional(),
            "lastUpdater": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "content": t.proxy(renames["QueryContentOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SavedQueryOut"])
    types["ResourceSearchResultIn"] = t.struct(
        {
            "state": t.string().optional(),
            "tagValues": t.array(t.string()).optional(),
            "project": t.string().optional(),
            "updateTime": t.string().optional(),
            "assetType": t.string().optional(),
            "parentAssetType": t.string().optional(),
            "kmsKeys": t.array(t.string()).optional(),
            "versionedResources": t.array(
                t.proxy(renames["VersionedResourceIn"])
            ).optional(),
            "relationships": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "location": t.string().optional(),
            "additionalAttributes": t.struct({"_": t.string().optional()}).optional(),
            "folders": t.array(t.string()).optional(),
            "tagKeys": t.array(t.string()).optional(),
            "parentFullResourceName": t.string().optional(),
            "tagValueIds": t.array(t.string()).optional(),
            "attachedResources": t.array(
                t.proxy(renames["AttachedResourceIn"])
            ).optional(),
            "description": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "kmsKey": t.string().optional(),
            "organization": t.string().optional(),
        }
    ).named(renames["ResourceSearchResultIn"])
    types["ResourceSearchResultOut"] = t.struct(
        {
            "state": t.string().optional(),
            "tagValues": t.array(t.string()).optional(),
            "project": t.string().optional(),
            "updateTime": t.string().optional(),
            "assetType": t.string().optional(),
            "parentAssetType": t.string().optional(),
            "kmsKeys": t.array(t.string()).optional(),
            "versionedResources": t.array(
                t.proxy(renames["VersionedResourceOut"])
            ).optional(),
            "relationships": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "location": t.string().optional(),
            "additionalAttributes": t.struct({"_": t.string().optional()}).optional(),
            "folders": t.array(t.string()).optional(),
            "tagKeys": t.array(t.string()).optional(),
            "parentFullResourceName": t.string().optional(),
            "tagValueIds": t.array(t.string()).optional(),
            "attachedResources": t.array(
                t.proxy(renames["AttachedResourceOut"])
            ).optional(),
            "description": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "kmsKey": t.string().optional(),
            "organization": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceSearchResultOut"])
    types["GoogleIdentityAccesscontextmanagerV1MethodSelectorIn"] = t.struct(
        {"method": t.string().optional(), "permission": t.string().optional()}
    ).named(renames["GoogleIdentityAccesscontextmanagerV1MethodSelectorIn"])
    types["GoogleIdentityAccesscontextmanagerV1MethodSelectorOut"] = t.struct(
        {
            "method": t.string().optional(),
            "permission": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1MethodSelectorOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["AnalyzerOrgPolicyIn"] = t.struct(
        {
            "reset": t.boolean().optional(),
            "attachedResource": t.string().optional(),
            "rules": t.array(t.proxy(renames["GoogleCloudAssetV1RuleIn"])).optional(),
            "appliedResource": t.string().optional(),
            "inheritFromParent": t.boolean().optional(),
        }
    ).named(renames["AnalyzerOrgPolicyIn"])
    types["AnalyzerOrgPolicyOut"] = t.struct(
        {
            "reset": t.boolean().optional(),
            "attachedResource": t.string().optional(),
            "rules": t.array(t.proxy(renames["GoogleCloudAssetV1RuleOut"])).optional(),
            "appliedResource": t.string().optional(),
            "inheritFromParent": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzerOrgPolicyOut"])
    types["QueryAssetsResponseIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "queryResult": t.proxy(renames["QueryResultIn"]).optional(),
            "jobReference": t.string().optional(),
            "outputConfig": t.proxy(renames["QueryAssetsOutputConfigIn"]).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["QueryAssetsResponseIn"])
    types["QueryAssetsResponseOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "queryResult": t.proxy(renames["QueryResultOut"]).optional(),
            "jobReference": t.string().optional(),
            "outputConfig": t.proxy(renames["QueryAssetsOutputConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryAssetsResponseOut"])
    types["GoogleCloudAssetV1StringValuesIn"] = t.struct(
        {
            "allowedValues": t.array(t.string()).optional(),
            "deniedValues": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudAssetV1StringValuesIn"])
    types["GoogleCloudAssetV1StringValuesOut"] = t.struct(
        {
            "allowedValues": t.array(t.string()).optional(),
            "deniedValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1StringValuesOut"])
    types["OptionsIn"] = t.struct(
        {
            "includeDenyPolicyAnalysis": t.boolean().optional(),
            "outputResourceEdges": t.boolean().optional(),
            "expandResources": t.boolean().optional(),
            "outputGroupEdges": t.boolean().optional(),
            "expandRoles": t.boolean().optional(),
            "expandGroups": t.boolean().optional(),
            "analyzeServiceAccountImpersonation": t.boolean().optional(),
        }
    ).named(renames["OptionsIn"])
    types["OptionsOut"] = t.struct(
        {
            "includeDenyPolicyAnalysis": t.boolean().optional(),
            "outputResourceEdges": t.boolean().optional(),
            "expandResources": t.boolean().optional(),
            "outputGroupEdges": t.boolean().optional(),
            "expandRoles": t.boolean().optional(),
            "expandGroups": t.boolean().optional(),
            "analyzeServiceAccountImpersonation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionsOut"])
    types["PermissionsIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["PermissionsIn"])
    types["PermissionsOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionsOut"])
    types["GoogleCloudAssetV1GovernedContainerIn"] = t.struct(
        {
            "policyBundle": t.array(t.proxy(renames["AnalyzerOrgPolicyIn"])).optional(),
            "fullResourceName": t.string().optional(),
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyIn"]).optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1GovernedContainerIn"])
    types["GoogleCloudAssetV1GovernedContainerOut"] = t.struct(
        {
            "policyBundle": t.array(
                t.proxy(renames["AnalyzerOrgPolicyOut"])
            ).optional(),
            "fullResourceName": t.string().optional(),
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyOut"]).optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1GovernedContainerOut"])
    types["AnalyzeIamPolicyLongrunningResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AnalyzeIamPolicyLongrunningResponseIn"])
    types["AnalyzeIamPolicyLongrunningResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AnalyzeIamPolicyLongrunningResponseOut"])
    types["MoveAnalysisIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "displayName": t.string().optional(),
            "analysis": t.proxy(renames["MoveAnalysisResultIn"]).optional(),
        }
    ).named(renames["MoveAnalysisIn"])
    types["MoveAnalysisOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "displayName": t.string().optional(),
            "analysis": t.proxy(renames["MoveAnalysisResultOut"]).optional(),
        }
    ).named(renames["MoveAnalysisOut"])
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
    types["TableFieldSchemaIn"] = t.struct(
        {
            "field": t.string().optional(),
            "mode": t.string().optional(),
            "fields": t.array(t.proxy(renames["TableFieldSchemaIn"])).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["TableFieldSchemaIn"])
    types["TableFieldSchemaOut"] = t.struct(
        {
            "field": t.string().optional(),
            "mode": t.string().optional(),
            "fields": t.array(t.proxy(renames["TableFieldSchemaOut"])).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableFieldSchemaOut"])
    types["QueryResultIn"] = t.struct(
        {
            "rows": t.array(t.struct({"_": t.string().optional()})).optional(),
            "schema": t.proxy(renames["TableSchemaIn"]).optional(),
            "nextPageToken": t.string().optional(),
            "totalRows": t.string().optional(),
        }
    ).named(renames["QueryResultIn"])
    types["QueryResultOut"] = t.struct(
        {
            "rows": t.array(t.struct({"_": t.string().optional()})).optional(),
            "schema": t.proxy(renames["TableSchemaOut"]).optional(),
            "nextPageToken": t.string().optional(),
            "totalRows": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResultOut"])
    types["GoogleCloudAssetV1CustomConstraintIn"] = t.struct(
        {
            "actionType": t.string().optional(),
            "condition": t.string().optional(),
            "name": t.string().optional(),
            "resourceTypes": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "methodTypes": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudAssetV1CustomConstraintIn"])
    types["GoogleCloudAssetV1CustomConstraintOut"] = t.struct(
        {
            "actionType": t.string().optional(),
            "condition": t.string().optional(),
            "name": t.string().optional(),
            "resourceTypes": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "methodTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1CustomConstraintOut"])
    types["GoogleCloudAssetV1DeniedAccessAccessTupleIn"] = t.struct(
        {
            "resource": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessResourceIn"]
            ).optional(),
            "access": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessAccessIn"]
            ).optional(),
            "identity": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessIdentityIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessAccessTupleIn"])
    types["GoogleCloudAssetV1DeniedAccessAccessTupleOut"] = t.struct(
        {
            "resource": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessResourceOut"]
            ).optional(),
            "access": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessAccessOut"]
            ).optional(),
            "identity": t.proxy(
                renames["GoogleCloudAssetV1DeniedAccessIdentityOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessAccessTupleOut"])
    types["GoogleCloudAssetV1DeniedAccessIdentityIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["GoogleCloudAssetV1DeniedAccessIdentityIn"])
    types["GoogleCloudAssetV1DeniedAccessIdentityOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessIdentityOut"])
    types["IamPolicySearchResultIn"] = t.struct(
        {
            "resource": t.string().optional(),
            "folders": t.array(t.string()).optional(),
            "assetType": t.string().optional(),
            "explanation": t.proxy(renames["ExplanationIn"]).optional(),
            "project": t.string().optional(),
            "organization": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
        }
    ).named(renames["IamPolicySearchResultIn"])
    types["IamPolicySearchResultOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "folders": t.array(t.string()).optional(),
            "assetType": t.string().optional(),
            "explanation": t.proxy(renames["ExplanationOut"]).optional(),
            "project": t.string().optional(),
            "organization": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicySearchResultOut"])
    types["GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn"] = t.struct(
        {
            "description": t.string().optional(),
            "spec": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn"]
            ).optional(),
            "useExplicitDryRunSpec": t.boolean().optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "status": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn"]
            ).optional(),
            "perimeterType": t.string().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn"])
    types["GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut"] = t.struct(
        {
            "description": t.string().optional(),
            "spec": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut"]
            ).optional(),
            "useExplicitDryRunSpec": t.boolean().optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "status": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut"]
            ).optional(),
            "perimeterType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut"])
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
    types["UpdateFeedRequestIn"] = t.struct(
        {"feed": t.proxy(renames["FeedIn"]), "updateMask": t.string()}
    ).named(renames["UpdateFeedRequestIn"])
    types["UpdateFeedRequestOut"] = t.struct(
        {
            "feed": t.proxy(renames["FeedOut"]),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateFeedRequestOut"])
    types["ConditionEvaluationIn"] = t.struct(
        {"evaluationValue": t.string().optional()}
    ).named(renames["ConditionEvaluationIn"])
    types["ConditionEvaluationOut"] = t.struct(
        {
            "evaluationValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionEvaluationOut"])
    types["BatchGetAssetsHistoryResponseIn"] = t.struct(
        {"assets": t.array(t.proxy(renames["TemporalAssetIn"])).optional()}
    ).named(renames["BatchGetAssetsHistoryResponseIn"])
    types["BatchGetAssetsHistoryResponseOut"] = t.struct(
        {
            "assets": t.array(t.proxy(renames["TemporalAssetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetAssetsHistoryResponseOut"])
    types["GoogleIdentityAccesscontextmanagerV1DevicePolicyIn"] = t.struct(
        {
            "osConstraints": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1OsConstraintIn"])
            ).optional(),
            "requireAdminApproval": t.boolean().optional(),
            "allowedEncryptionStatuses": t.array(t.string()).optional(),
            "requireScreenlock": t.boolean().optional(),
            "allowedDeviceManagementLevels": t.array(t.string()).optional(),
            "requireCorpOwned": t.boolean().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1DevicePolicyIn"])
    types["GoogleIdentityAccesscontextmanagerV1DevicePolicyOut"] = t.struct(
        {
            "osConstraints": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1OsConstraintOut"])
            ).optional(),
            "requireAdminApproval": t.boolean().optional(),
            "allowedEncryptionStatuses": t.array(t.string()).optional(),
            "requireScreenlock": t.boolean().optional(),
            "allowedDeviceManagementLevels": t.array(t.string()).optional(),
            "requireCorpOwned": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1DevicePolicyOut"])
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
    types["GoogleIamV2DenyRuleIn"] = t.struct(
        {
            "deniedPrincipals": t.array(t.string()).optional(),
            "denialCondition": t.proxy(renames["ExprIn"]).optional(),
            "exceptionPermissions": t.array(t.string()).optional(),
            "deniedPermissions": t.array(t.string()).optional(),
            "exceptionPrincipals": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamV2DenyRuleIn"])
    types["GoogleIamV2DenyRuleOut"] = t.struct(
        {
            "deniedPrincipals": t.array(t.string()).optional(),
            "denialCondition": t.proxy(renames["ExprOut"]).optional(),
            "exceptionPermissions": t.array(t.string()).optional(),
            "deniedPermissions": t.array(t.string()).optional(),
            "exceptionPrincipals": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2DenyRuleOut"])
    types["ExplanationIn"] = t.struct(
        {"matchedPermissions": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ExplanationIn"])
    types["ExplanationOut"] = t.struct(
        {
            "matchedPermissions": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExplanationOut"])
    types[
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyIn"
    ] = t.struct(
        {
            "organization": t.string().optional(),
            "attachedResource": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "folders": t.array(t.string()).optional(),
            "project": t.string().optional(),
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
            "organization": t.string().optional(),
            "attachedResource": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "folders": t.array(t.string()).optional(),
            "project": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyOut"
        ]
    )
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
    types["AssetIn"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "resource": t.proxy(renames["ResourceIn"]).optional(),
            "iamPolicy": t.proxy(renames["PolicyIn"]).optional(),
            "servicePerimeter": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn"]
            ).optional(),
            "assetType": t.string().optional(),
            "orgPolicy": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV1PolicyIn"])
            ).optional(),
            "accessPolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyIn"]
            ).optional(),
            "accessLevel": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessLevelIn"]
            ).optional(),
            "relatedAsset": t.proxy(renames["RelatedAssetIn"]).optional(),
            "osInventory": t.proxy(renames["InventoryIn"]).optional(),
            "ancestors": t.array(t.string()).optional(),
            "relatedAssets": t.proxy(renames["RelatedAssetsIn"]).optional(),
        }
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "resource": t.proxy(renames["ResourceOut"]).optional(),
            "iamPolicy": t.proxy(renames["PolicyOut"]).optional(),
            "servicePerimeter": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut"]
            ).optional(),
            "assetType": t.string().optional(),
            "orgPolicy": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV1PolicyOut"])
            ).optional(),
            "accessPolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyOut"]
            ).optional(),
            "accessLevel": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessLevelOut"]
            ).optional(),
            "relatedAsset": t.proxy(renames["RelatedAssetOut"]).optional(),
            "osInventory": t.proxy(renames["InventoryOut"]).optional(),
            "ancestors": t.array(t.string()).optional(),
            "relatedAssets": t.proxy(renames["RelatedAssetsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
    types["GoogleIdentityAccesscontextmanagerV1CustomLevelIn"] = t.struct(
        {"expr": t.proxy(renames["ExprIn"])}
    ).named(renames["GoogleIdentityAccesscontextmanagerV1CustomLevelIn"])
    types["GoogleIdentityAccesscontextmanagerV1CustomLevelOut"] = t.struct(
        {
            "expr": t.proxy(renames["ExprOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1CustomLevelOut"])
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
    types["GoogleCloudOrgpolicyV1ListPolicyIn"] = t.struct(
        {
            "allValues": t.string().optional(),
            "inheritFromParent": t.boolean().optional(),
            "suggestedValue": t.string().optional(),
            "deniedValues": t.array(t.string()).optional(),
            "allowedValues": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1ListPolicyIn"])
    types["GoogleCloudOrgpolicyV1ListPolicyOut"] = t.struct(
        {
            "allValues": t.string().optional(),
            "inheritFromParent": t.boolean().optional(),
            "suggestedValue": t.string().optional(),
            "deniedValues": t.array(t.string()).optional(),
            "allowedValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1ListPolicyOut"])
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
    types["GoogleCloudOrgpolicyV1RestoreDefaultIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudOrgpolicyV1RestoreDefaultIn"])
    types["GoogleCloudOrgpolicyV1RestoreDefaultOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudOrgpolicyV1RestoreDefaultOut"])
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
    types["GoogleCloudAssetV1AccessControlListIn"] = t.struct(
        {
            "conditionEvaluation": t.proxy(renames["ConditionEvaluationIn"]).optional(),
            "resourceEdges": t.array(
                t.proxy(renames["GoogleCloudAssetV1EdgeIn"])
            ).optional(),
            "accesses": t.array(
                t.proxy(renames["GoogleCloudAssetV1AccessIn"])
            ).optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudAssetV1ResourceIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudAssetV1AccessControlListIn"])
    types["GoogleCloudAssetV1AccessControlListOut"] = t.struct(
        {
            "conditionEvaluation": t.proxy(
                renames["ConditionEvaluationOut"]
            ).optional(),
            "resourceEdges": t.array(
                t.proxy(renames["GoogleCloudAssetV1EdgeOut"])
            ).optional(),
            "accesses": t.array(
                t.proxy(renames["GoogleCloudAssetV1AccessOut"])
            ).optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudAssetV1ResourceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1AccessControlListOut"])
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
    types["GoogleIdentityAccesscontextmanagerV1AccessPolicyIn"] = t.struct(
        {
            "scopes": t.array(t.string()).optional(),
            "title": t.string(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "parent": t.string(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyIn"])
    types["GoogleIdentityAccesscontextmanagerV1AccessPolicyOut"] = t.struct(
        {
            "scopes": t.array(t.string()).optional(),
            "title": t.string(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "parent": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
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
    types["GoogleCloudAssetV1DeniedAccessDenyDetailIn"] = t.struct(
        {
            "denyRule": t.proxy(renames["GoogleIamV2DenyRuleIn"]).optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessResourceIn"])
            ).optional(),
            "identities": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessIdentityIn"])
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
            "resources": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessResourceOut"])
            ).optional(),
            "identities": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessIdentityOut"])
            ).optional(),
            "fullyDenied": t.boolean().optional(),
            "accesses": t.array(
                t.proxy(renames["GoogleCloudAssetV1DeniedAccessAccessOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessDenyDetailOut"])
    types["WindowsApplicationIn"] = t.struct(
        {
            "helpLink": t.string().optional(),
            "displayName": t.string().optional(),
            "publisher": t.string().optional(),
            "displayVersion": t.string().optional(),
            "installDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["WindowsApplicationIn"])
    types["WindowsApplicationOut"] = t.struct(
        {
            "helpLink": t.string().optional(),
            "displayName": t.string().optional(),
            "publisher": t.string().optional(),
            "displayVersion": t.string().optional(),
            "installDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsApplicationOut"])
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
    types["PartitionSpecIn"] = t.struct({"partitionKey": t.string().optional()}).named(
        renames["PartitionSpecIn"]
    )
    types["PartitionSpecOut"] = t.struct(
        {
            "partitionKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionSpecOut"])
    types["GoogleIdentityAccesscontextmanagerV1OsConstraintIn"] = t.struct(
        {
            "osType": t.string(),
            "minimumVersion": t.string().optional(),
            "requireVerifiedChromeOs": t.boolean().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1OsConstraintIn"])
    types["GoogleIdentityAccesscontextmanagerV1OsConstraintOut"] = t.struct(
        {
            "osType": t.string(),
            "minimumVersion": t.string().optional(),
            "requireVerifiedChromeOs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1OsConstraintOut"])
    types["TemporalAssetIn"] = t.struct(
        {
            "window": t.proxy(renames["TimeWindowIn"]).optional(),
            "deleted": t.boolean().optional(),
            "priorAsset": t.proxy(renames["AssetIn"]).optional(),
            "asset": t.proxy(renames["AssetIn"]).optional(),
            "priorAssetState": t.string().optional(),
        }
    ).named(renames["TemporalAssetIn"])
    types["TemporalAssetOut"] = t.struct(
        {
            "window": t.proxy(renames["TimeWindowOut"]).optional(),
            "deleted": t.boolean().optional(),
            "priorAsset": t.proxy(renames["AssetOut"]).optional(),
            "asset": t.proxy(renames["AssetOut"]).optional(),
            "priorAssetState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TemporalAssetOut"])
    types["IamPolicyAnalysisResultIn"] = t.struct(
        {
            "identityList": t.proxy(
                renames["GoogleCloudAssetV1IdentityListIn"]
            ).optional(),
            "fullyExplored": t.boolean().optional(),
            "accessControlLists": t.array(
                t.proxy(renames["GoogleCloudAssetV1AccessControlListIn"])
            ).optional(),
            "attachedResourceFullName": t.string().optional(),
            "iamBinding": t.proxy(renames["BindingIn"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisResultIn"])
    types["IamPolicyAnalysisResultOut"] = t.struct(
        {
            "identityList": t.proxy(
                renames["GoogleCloudAssetV1IdentityListOut"]
            ).optional(),
            "fullyExplored": t.boolean().optional(),
            "accessControlLists": t.array(
                t.proxy(renames["GoogleCloudAssetV1AccessControlListOut"])
            ).optional(),
            "attachedResourceFullName": t.string().optional(),
            "iamBinding": t.proxy(renames["BindingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisResultOut"])
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
    types["ResourceSelectorIn"] = t.struct({"fullResourceName": t.string()}).named(
        renames["ResourceSelectorIn"]
    )
    types["ResourceSelectorOut"] = t.struct(
        {
            "fullResourceName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceSelectorOut"])
    types["FeedIn"] = t.struct(
        {
            "assetTypes": t.array(t.string()).optional(),
            "assetNames": t.array(t.string()).optional(),
            "relationshipTypes": t.array(t.string()).optional(),
            "feedOutputConfig": t.proxy(renames["FeedOutputConfigIn"]),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "name": t.string(),
            "contentType": t.string().optional(),
        }
    ).named(renames["FeedIn"])
    types["FeedOut"] = t.struct(
        {
            "assetTypes": t.array(t.string()).optional(),
            "assetNames": t.array(t.string()).optional(),
            "relationshipTypes": t.array(t.string()).optional(),
            "feedOutputConfig": t.proxy(renames["FeedOutputConfigOut"]),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "name": t.string(),
            "contentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeedOut"])
    types["AttachedResourceIn"] = t.struct(
        {
            "assetType": t.string().optional(),
            "versionedResources": t.array(
                t.proxy(renames["VersionedResourceIn"])
            ).optional(),
        }
    ).named(renames["AttachedResourceIn"])
    types["AttachedResourceOut"] = t.struct(
        {
            "assetType": t.string().optional(),
            "versionedResources": t.array(
                t.proxy(renames["VersionedResourceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachedResourceOut"])
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["GoogleCloudOrgpolicyV1BooleanPolicyIn"] = t.struct(
        {"enforced": t.boolean().optional()}
    ).named(renames["GoogleCloudOrgpolicyV1BooleanPolicyIn"])
    types["GoogleCloudOrgpolicyV1BooleanPolicyOut"] = t.struct(
        {
            "enforced": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1BooleanPolicyOut"])
    types["GoogleCloudAssetV1GcsDestinationIn"] = t.struct({"uri": t.string()}).named(
        renames["GoogleCloudAssetV1GcsDestinationIn"]
    )
    types["GoogleCloudAssetV1GcsDestinationOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudAssetV1GcsDestinationOut"])
    types["AnalyzeMoveResponseIn"] = t.struct(
        {"moveAnalysis": t.array(t.proxy(renames["MoveAnalysisIn"])).optional()}
    ).named(renames["AnalyzeMoveResponseIn"])
    types["AnalyzeMoveResponseOut"] = t.struct(
        {
            "moveAnalysis": t.array(t.proxy(renames["MoveAnalysisOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeMoveResponseOut"])
    types["IdentitySelectorIn"] = t.struct({"identity": t.string()}).named(
        renames["IdentitySelectorIn"]
    )
    types["IdentitySelectorOut"] = t.struct(
        {"identity": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IdentitySelectorOut"])
    types["ZypperPatchIn"] = t.struct(
        {
            "category": t.string().optional(),
            "severity": t.string().optional(),
            "patchName": t.string().optional(),
            "summary": t.string().optional(),
        }
    ).named(renames["ZypperPatchIn"])
    types["ZypperPatchOut"] = t.struct(
        {
            "category": t.string().optional(),
            "severity": t.string().optional(),
            "patchName": t.string().optional(),
            "summary": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZypperPatchOut"])
    types["WindowsUpdatePackageIn"] = t.struct(
        {
            "kbArticleIds": t.array(t.string()).optional(),
            "updateId": t.string().optional(),
            "revisionNumber": t.integer().optional(),
            "lastDeploymentChangeTime": t.string().optional(),
            "description": t.string().optional(),
            "categories": t.array(
                t.proxy(renames["WindowsUpdateCategoryIn"])
            ).optional(),
            "title": t.string().optional(),
            "moreInfoUrls": t.array(t.string()).optional(),
            "supportUrl": t.string().optional(),
        }
    ).named(renames["WindowsUpdatePackageIn"])
    types["WindowsUpdatePackageOut"] = t.struct(
        {
            "kbArticleIds": t.array(t.string()).optional(),
            "updateId": t.string().optional(),
            "revisionNumber": t.integer().optional(),
            "lastDeploymentChangeTime": t.string().optional(),
            "description": t.string().optional(),
            "categories": t.array(
                t.proxy(renames["WindowsUpdateCategoryOut"])
            ).optional(),
            "title": t.string().optional(),
            "moreInfoUrls": t.array(t.string()).optional(),
            "supportUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsUpdatePackageOut"])
    types["ListFeedsResponseIn"] = t.struct(
        {"feeds": t.array(t.proxy(renames["FeedIn"])).optional()}
    ).named(renames["ListFeedsResponseIn"])
    types["ListFeedsResponseOut"] = t.struct(
        {
            "feeds": t.array(t.proxy(renames["FeedOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFeedsResponseOut"])
    types["GoogleCloudAssetV1DeniedAccessAccessIn"] = t.struct(
        {"permission": t.string().optional(), "role": t.string().optional()}
    ).named(renames["GoogleCloudAssetV1DeniedAccessAccessIn"])
    types["GoogleCloudAssetV1DeniedAccessAccessOut"] = t.struct(
        {
            "permission": t.string().optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1DeniedAccessAccessOut"])
    types["MoveAnalysisResultIn"] = t.struct(
        {
            "blockers": t.array(t.proxy(renames["MoveImpactIn"])).optional(),
            "warnings": t.array(t.proxy(renames["MoveImpactIn"])).optional(),
        }
    ).named(renames["MoveAnalysisResultIn"])
    types["MoveAnalysisResultOut"] = t.struct(
        {
            "blockers": t.array(t.proxy(renames["MoveImpactOut"])).optional(),
            "warnings": t.array(t.proxy(renames["MoveImpactOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveAnalysisResultOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["WindowsQuickFixEngineeringPackageIn"] = t.struct(
        {
            "description": t.string().optional(),
            "caption": t.string().optional(),
            "installTime": t.string().optional(),
            "hotFixId": t.string().optional(),
        }
    ).named(renames["WindowsQuickFixEngineeringPackageIn"])
    types["WindowsQuickFixEngineeringPackageOut"] = t.struct(
        {
            "description": t.string().optional(),
            "caption": t.string().optional(),
            "installTime": t.string().optional(),
            "hotFixId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsQuickFixEngineeringPackageOut"])
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
    types["GoogleCloudAssetV1BooleanConstraintIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudAssetV1BooleanConstraintIn"])
    types["GoogleCloudAssetV1BooleanConstraintOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudAssetV1BooleanConstraintOut"])
    types["AnalyzerOrgPolicyConstraintIn"] = t.struct(
        {
            "customConstraint": t.proxy(
                renames["GoogleCloudAssetV1CustomConstraintIn"]
            ).optional(),
            "googleDefinedConstraint": t.proxy(
                renames["GoogleCloudAssetV1ConstraintIn"]
            ).optional(),
        }
    ).named(renames["AnalyzerOrgPolicyConstraintIn"])
    types["AnalyzerOrgPolicyConstraintOut"] = t.struct(
        {
            "customConstraint": t.proxy(
                renames["GoogleCloudAssetV1CustomConstraintOut"]
            ).optional(),
            "googleDefinedConstraint": t.proxy(
                renames["GoogleCloudAssetV1ConstraintOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzerOrgPolicyConstraintOut"])
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
    types["RelatedAssetIn"] = t.struct(
        {
            "ancestors": t.array(t.string()).optional(),
            "relationshipType": t.string().optional(),
            "assetType": t.string().optional(),
            "asset": t.string().optional(),
        }
    ).named(renames["RelatedAssetIn"])
    types["RelatedAssetOut"] = t.struct(
        {
            "ancestors": t.array(t.string()).optional(),
            "relationshipType": t.string().optional(),
            "assetType": t.string().optional(),
            "asset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelatedAssetOut"])

    functions = {}
    functions["feedsList"] = cloudasset.delete(
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
            {"names": t.string(), "scope": t.string(), "auth": t.string().optional()}
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
    functions["v1AnalyzeIamPolicy"] = cloudasset.get(
        "v1/{scope}:analyzeOrgPolicyGovernedAssets",
        t.struct(
            {
                "filter": t.string().optional(),
                "scope": t.string(),
                "constraint": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeOrgPolicyGovernedAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeOrgPolicyGovernedContainers"] = cloudasset.get(
        "v1/{scope}:analyzeOrgPolicyGovernedAssets",
        t.struct(
            {
                "filter": t.string().optional(),
                "scope": t.string(),
                "constraint": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeOrgPolicyGovernedAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1SearchAllResources"] = cloudasset.get(
        "v1/{scope}:analyzeOrgPolicyGovernedAssets",
        t.struct(
            {
                "filter": t.string().optional(),
                "scope": t.string(),
                "constraint": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeOrgPolicyGovernedAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1ExportAssets"] = cloudasset.get(
        "v1/{scope}:analyzeOrgPolicyGovernedAssets",
        t.struct(
            {
                "filter": t.string().optional(),
                "scope": t.string(),
                "constraint": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeOrgPolicyGovernedAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeMove"] = cloudasset.get(
        "v1/{scope}:analyzeOrgPolicyGovernedAssets",
        t.struct(
            {
                "filter": t.string().optional(),
                "scope": t.string(),
                "constraint": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeOrgPolicyGovernedAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1BatchGetAssetsHistory"] = cloudasset.get(
        "v1/{scope}:analyzeOrgPolicyGovernedAssets",
        t.struct(
            {
                "filter": t.string().optional(),
                "scope": t.string(),
                "constraint": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeOrgPolicyGovernedAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1QueryAssets"] = cloudasset.get(
        "v1/{scope}:analyzeOrgPolicyGovernedAssets",
        t.struct(
            {
                "filter": t.string().optional(),
                "scope": t.string(),
                "constraint": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeOrgPolicyGovernedAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeIamPolicyLongrunning"] = cloudasset.get(
        "v1/{scope}:analyzeOrgPolicyGovernedAssets",
        t.struct(
            {
                "filter": t.string().optional(),
                "scope": t.string(),
                "constraint": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeOrgPolicyGovernedAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeOrgPolicies"] = cloudasset.get(
        "v1/{scope}:analyzeOrgPolicyGovernedAssets",
        t.struct(
            {
                "filter": t.string().optional(),
                "scope": t.string(),
                "constraint": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeOrgPolicyGovernedAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1SearchAllIamPolicies"] = cloudasset.get(
        "v1/{scope}:analyzeOrgPolicyGovernedAssets",
        t.struct(
            {
                "filter": t.string().optional(),
                "scope": t.string(),
                "constraint": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeOrgPolicyGovernedAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeOrgPolicyGovernedAssets"] = cloudasset.get(
        "v1/{scope}:analyzeOrgPolicyGovernedAssets",
        t.struct(
            {
                "filter": t.string().optional(),
                "scope": t.string(),
                "constraint": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeOrgPolicyGovernedAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["assetsList"] = cloudasset.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "contentType": t.string().optional(),
                "pageSize": t.integer().optional(),
                "readTime": t.string().optional(),
                "assetTypes": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "relationshipTypes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["savedQueriesPatch"] = cloudasset.post(
        "v1/{parent}/savedQueries",
        t.struct(
            {
                "parent": t.string(),
                "savedQueryId": t.string(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "content": t.proxy(renames["QueryContentIn"]).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["savedQueriesList"] = cloudasset.post(
        "v1/{parent}/savedQueries",
        t.struct(
            {
                "parent": t.string(),
                "savedQueryId": t.string(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "content": t.proxy(renames["QueryContentIn"]).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["savedQueriesGet"] = cloudasset.post(
        "v1/{parent}/savedQueries",
        t.struct(
            {
                "parent": t.string(),
                "savedQueryId": t.string(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "content": t.proxy(renames["QueryContentIn"]).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["savedQueriesDelete"] = cloudasset.post(
        "v1/{parent}/savedQueries",
        t.struct(
            {
                "parent": t.string(),
                "savedQueryId": t.string(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "content": t.proxy(renames["QueryContentIn"]).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["savedQueriesCreate"] = cloudasset.post(
        "v1/{parent}/savedQueries",
        t.struct(
            {
                "parent": t.string(),
                "savedQueryId": t.string(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "content": t.proxy(renames["QueryContentIn"]).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudasset",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
