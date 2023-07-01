from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_cloudasset():
    cloudasset = HTTPRuntime("https://cloudasset.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudasset_1_ErrorResponse",
        "IamPolicyAnalysisQueryIn": "_cloudasset_2_IamPolicyAnalysisQueryIn",
        "IamPolicyAnalysisQueryOut": "_cloudasset_3_IamPolicyAnalysisQueryOut",
        "GoogleCloudAssetV1IdentityIn": "_cloudasset_4_GoogleCloudAssetV1IdentityIn",
        "GoogleCloudAssetV1IdentityOut": "_cloudasset_5_GoogleCloudAssetV1IdentityOut",
        "AnalyzerOrgPolicyIn": "_cloudasset_6_AnalyzerOrgPolicyIn",
        "AnalyzerOrgPolicyOut": "_cloudasset_7_AnalyzerOrgPolicyOut",
        "GoogleCloudAssetV1ResourceIn": "_cloudasset_8_GoogleCloudAssetV1ResourceIn",
        "GoogleCloudAssetV1ResourceOut": "_cloudasset_9_GoogleCloudAssetV1ResourceOut",
        "GoogleIdentityAccesscontextmanagerV1IngressSourceIn": "_cloudasset_10_GoogleIdentityAccesscontextmanagerV1IngressSourceIn",
        "GoogleIdentityAccesscontextmanagerV1IngressSourceOut": "_cloudasset_11_GoogleIdentityAccesscontextmanagerV1IngressSourceOut",
        "ResourceSearchResultIn": "_cloudasset_12_ResourceSearchResultIn",
        "ResourceSearchResultOut": "_cloudasset_13_ResourceSearchResultOut",
        "ZypperPatchIn": "_cloudasset_14_ZypperPatchIn",
        "ZypperPatchOut": "_cloudasset_15_ZypperPatchOut",
        "AttachedResourceIn": "_cloudasset_16_AttachedResourceIn",
        "AttachedResourceOut": "_cloudasset_17_AttachedResourceOut",
        "QueryResultIn": "_cloudasset_18_QueryResultIn",
        "QueryResultOut": "_cloudasset_19_QueryResultOut",
        "GoogleCloudOrgpolicyV1BooleanPolicyIn": "_cloudasset_20_GoogleCloudOrgpolicyV1BooleanPolicyIn",
        "GoogleCloudOrgpolicyV1BooleanPolicyOut": "_cloudasset_21_GoogleCloudOrgpolicyV1BooleanPolicyOut",
        "GoogleCloudAssetV1GovernedContainerIn": "_cloudasset_22_GoogleCloudAssetV1GovernedContainerIn",
        "GoogleCloudAssetV1GovernedContainerOut": "_cloudasset_23_GoogleCloudAssetV1GovernedContainerOut",
        "GoogleIdentityAccesscontextmanagerV1AccessLevelIn": "_cloudasset_24_GoogleIdentityAccesscontextmanagerV1AccessLevelIn",
        "GoogleIdentityAccesscontextmanagerV1AccessLevelOut": "_cloudasset_25_GoogleIdentityAccesscontextmanagerV1AccessLevelOut",
        "WindowsUpdatePackageIn": "_cloudasset_26_WindowsUpdatePackageIn",
        "WindowsUpdatePackageOut": "_cloudasset_27_WindowsUpdatePackageOut",
        "GoogleCloudAssetV1AccessControlListIn": "_cloudasset_28_GoogleCloudAssetV1AccessControlListIn",
        "GoogleCloudAssetV1AccessControlListOut": "_cloudasset_29_GoogleCloudAssetV1AccessControlListOut",
        "RelatedAssetIn": "_cloudasset_30_RelatedAssetIn",
        "RelatedAssetOut": "_cloudasset_31_RelatedAssetOut",
        "AnalyzeOrgPolicyGovernedContainersResponseIn": "_cloudasset_32_AnalyzeOrgPolicyGovernedContainersResponseIn",
        "AnalyzeOrgPolicyGovernedContainersResponseOut": "_cloudasset_33_AnalyzeOrgPolicyGovernedContainersResponseOut",
        "WindowsApplicationIn": "_cloudasset_34_WindowsApplicationIn",
        "WindowsApplicationOut": "_cloudasset_35_WindowsApplicationOut",
        "AnalyzerOrgPolicyConstraintIn": "_cloudasset_36_AnalyzerOrgPolicyConstraintIn",
        "AnalyzerOrgPolicyConstraintOut": "_cloudasset_37_AnalyzerOrgPolicyConstraintOut",
        "TimeWindowIn": "_cloudasset_38_TimeWindowIn",
        "TimeWindowOut": "_cloudasset_39_TimeWindowOut",
        "GoogleIdentityAccesscontextmanagerV1CustomLevelIn": "_cloudasset_40_GoogleIdentityAccesscontextmanagerV1CustomLevelIn",
        "GoogleIdentityAccesscontextmanagerV1CustomLevelOut": "_cloudasset_41_GoogleIdentityAccesscontextmanagerV1CustomLevelOut",
        "BatchGetEffectiveIamPoliciesResponseIn": "_cloudasset_42_BatchGetEffectiveIamPoliciesResponseIn",
        "BatchGetEffectiveIamPoliciesResponseOut": "_cloudasset_43_BatchGetEffectiveIamPoliciesResponseOut",
        "AnalyzeIamPolicyLongrunningRequestIn": "_cloudasset_44_AnalyzeIamPolicyLongrunningRequestIn",
        "AnalyzeIamPolicyLongrunningRequestOut": "_cloudasset_45_AnalyzeIamPolicyLongrunningRequestOut",
        "OrgPolicyResultIn": "_cloudasset_46_OrgPolicyResultIn",
        "OrgPolicyResultOut": "_cloudasset_47_OrgPolicyResultOut",
        "GoogleIdentityAccesscontextmanagerV1IngressPolicyIn": "_cloudasset_48_GoogleIdentityAccesscontextmanagerV1IngressPolicyIn",
        "GoogleIdentityAccesscontextmanagerV1IngressPolicyOut": "_cloudasset_49_GoogleIdentityAccesscontextmanagerV1IngressPolicyOut",
        "OperationIn": "_cloudasset_50_OperationIn",
        "OperationOut": "_cloudasset_51_OperationOut",
        "AnalyzeOrgPolicyGovernedAssetsResponseIn": "_cloudasset_52_AnalyzeOrgPolicyGovernedAssetsResponseIn",
        "AnalyzeOrgPolicyGovernedAssetsResponseOut": "_cloudasset_53_AnalyzeOrgPolicyGovernedAssetsResponseOut",
        "GoogleCloudAssetV1p7beta1RelatedAssetIn": "_cloudasset_54_GoogleCloudAssetV1p7beta1RelatedAssetIn",
        "GoogleCloudAssetV1p7beta1RelatedAssetOut": "_cloudasset_55_GoogleCloudAssetV1p7beta1RelatedAssetOut",
        "GoogleIdentityAccesscontextmanagerV1EgressToIn": "_cloudasset_56_GoogleIdentityAccesscontextmanagerV1EgressToIn",
        "GoogleIdentityAccesscontextmanagerV1EgressToOut": "_cloudasset_57_GoogleIdentityAccesscontextmanagerV1EgressToOut",
        "GoogleCloudAssetV1GcsDestinationIn": "_cloudasset_58_GoogleCloudAssetV1GcsDestinationIn",
        "GoogleCloudAssetV1GcsDestinationOut": "_cloudasset_59_GoogleCloudAssetV1GcsDestinationOut",
        "PartitionSpecIn": "_cloudasset_60_PartitionSpecIn",
        "PartitionSpecOut": "_cloudasset_61_PartitionSpecOut",
        "AuditConfigIn": "_cloudasset_62_AuditConfigIn",
        "AuditConfigOut": "_cloudasset_63_AuditConfigOut",
        "OptionsIn": "_cloudasset_64_OptionsIn",
        "OptionsOut": "_cloudasset_65_OptionsOut",
        "EmptyIn": "_cloudasset_66_EmptyIn",
        "EmptyOut": "_cloudasset_67_EmptyOut",
        "RelatedResourceIn": "_cloudasset_68_RelatedResourceIn",
        "RelatedResourceOut": "_cloudasset_69_RelatedResourceOut",
        "EffectiveIamPolicyIn": "_cloudasset_70_EffectiveIamPolicyIn",
        "EffectiveIamPolicyOut": "_cloudasset_71_EffectiveIamPolicyOut",
        "IamPolicyAnalysisIn": "_cloudasset_72_IamPolicyAnalysisIn",
        "IamPolicyAnalysisOut": "_cloudasset_73_IamPolicyAnalysisOut",
        "BatchGetAssetsHistoryResponseIn": "_cloudasset_74_BatchGetAssetsHistoryResponseIn",
        "BatchGetAssetsHistoryResponseOut": "_cloudasset_75_BatchGetAssetsHistoryResponseOut",
        "AnalyzeIamPolicyLongrunningMetadataIn": "_cloudasset_76_AnalyzeIamPolicyLongrunningMetadataIn",
        "AnalyzeIamPolicyLongrunningMetadataOut": "_cloudasset_77_AnalyzeIamPolicyLongrunningMetadataOut",
        "GoogleCloudAssetV1p7beta1AssetIn": "_cloudasset_78_GoogleCloudAssetV1p7beta1AssetIn",
        "GoogleCloudAssetV1p7beta1AssetOut": "_cloudasset_79_GoogleCloudAssetV1p7beta1AssetOut",
        "PolicyIn": "_cloudasset_80_PolicyIn",
        "PolicyOut": "_cloudasset_81_PolicyOut",
        "AuditLogConfigIn": "_cloudasset_82_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudasset_83_AuditLogConfigOut",
        "ResourceSelectorIn": "_cloudasset_84_ResourceSelectorIn",
        "ResourceSelectorOut": "_cloudasset_85_ResourceSelectorOut",
        "IdentitySelectorIn": "_cloudasset_86_IdentitySelectorIn",
        "IdentitySelectorOut": "_cloudasset_87_IdentitySelectorOut",
        "VersionedResourceIn": "_cloudasset_88_VersionedResourceIn",
        "VersionedResourceOut": "_cloudasset_89_VersionedResourceOut",
        "ListFeedsResponseIn": "_cloudasset_90_ListFeedsResponseIn",
        "ListFeedsResponseOut": "_cloudasset_91_ListFeedsResponseOut",
        "DateIn": "_cloudasset_92_DateIn",
        "DateOut": "_cloudasset_93_DateOut",
        "MoveAnalysisIn": "_cloudasset_94_MoveAnalysisIn",
        "MoveAnalysisOut": "_cloudasset_95_MoveAnalysisOut",
        "GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn": "_cloudasset_96_GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn",
        "GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut": "_cloudasset_97_GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut",
        "IamPolicySearchResultIn": "_cloudasset_98_IamPolicySearchResultIn",
        "IamPolicySearchResultOut": "_cloudasset_99_IamPolicySearchResultOut",
        "PolicyInfoIn": "_cloudasset_100_PolicyInfoIn",
        "PolicyInfoOut": "_cloudasset_101_PolicyInfoOut",
        "AssetIn": "_cloudasset_102_AssetIn",
        "AssetOut": "_cloudasset_103_AssetOut",
        "UpdateFeedRequestIn": "_cloudasset_104_UpdateFeedRequestIn",
        "UpdateFeedRequestOut": "_cloudasset_105_UpdateFeedRequestOut",
        "ExplanationIn": "_cloudasset_106_ExplanationIn",
        "ExplanationOut": "_cloudasset_107_ExplanationOut",
        "VersionedPackageIn": "_cloudasset_108_VersionedPackageIn",
        "VersionedPackageOut": "_cloudasset_109_VersionedPackageOut",
        "QueryAssetsOutputConfigIn": "_cloudasset_110_QueryAssetsOutputConfigIn",
        "QueryAssetsOutputConfigOut": "_cloudasset_111_QueryAssetsOutputConfigOut",
        "ListAssetsResponseIn": "_cloudasset_112_ListAssetsResponseIn",
        "ListAssetsResponseOut": "_cloudasset_113_ListAssetsResponseOut",
        "GoogleIdentityAccesscontextmanagerV1IngressFromIn": "_cloudasset_114_GoogleIdentityAccesscontextmanagerV1IngressFromIn",
        "GoogleIdentityAccesscontextmanagerV1IngressFromOut": "_cloudasset_115_GoogleIdentityAccesscontextmanagerV1IngressFromOut",
        "GoogleCloudAssetV1p7beta1RelatedAssetsIn": "_cloudasset_116_GoogleCloudAssetV1p7beta1RelatedAssetsIn",
        "GoogleCloudAssetV1p7beta1RelatedAssetsOut": "_cloudasset_117_GoogleCloudAssetV1p7beta1RelatedAssetsOut",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyIn": "_cloudasset_118_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyIn",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyOut": "_cloudasset_119_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyOut",
        "GoogleCloudAssetV1p7beta1RelationshipAttributesIn": "_cloudasset_120_GoogleCloudAssetV1p7beta1RelationshipAttributesIn",
        "GoogleCloudAssetV1p7beta1RelationshipAttributesOut": "_cloudasset_121_GoogleCloudAssetV1p7beta1RelationshipAttributesOut",
        "QueryAssetsResponseIn": "_cloudasset_122_QueryAssetsResponseIn",
        "QueryAssetsResponseOut": "_cloudasset_123_QueryAssetsResponseOut",
        "GoogleIdentityAccesscontextmanagerV1EgressFromIn": "_cloudasset_124_GoogleIdentityAccesscontextmanagerV1EgressFromIn",
        "GoogleIdentityAccesscontextmanagerV1EgressFromOut": "_cloudasset_125_GoogleIdentityAccesscontextmanagerV1EgressFromOut",
        "WindowsUpdateCategoryIn": "_cloudasset_126_WindowsUpdateCategoryIn",
        "WindowsUpdateCategoryOut": "_cloudasset_127_WindowsUpdateCategoryOut",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceIn": "_cloudasset_128_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceIn",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceOut": "_cloudasset_129_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceOut",
        "GoogleIdentityAccesscontextmanagerV1OsConstraintIn": "_cloudasset_130_GoogleIdentityAccesscontextmanagerV1OsConstraintIn",
        "GoogleIdentityAccesscontextmanagerV1OsConstraintOut": "_cloudasset_131_GoogleIdentityAccesscontextmanagerV1OsConstraintOut",
        "GoogleCloudAssetV1BooleanConstraintIn": "_cloudasset_132_GoogleCloudAssetV1BooleanConstraintIn",
        "GoogleCloudAssetV1BooleanConstraintOut": "_cloudasset_133_GoogleCloudAssetV1BooleanConstraintOut",
        "GoogleIdentityAccesscontextmanagerV1ConditionIn": "_cloudasset_134_GoogleIdentityAccesscontextmanagerV1ConditionIn",
        "GoogleIdentityAccesscontextmanagerV1ConditionOut": "_cloudasset_135_GoogleIdentityAccesscontextmanagerV1ConditionOut",
        "WindowsQuickFixEngineeringPackageIn": "_cloudasset_136_WindowsQuickFixEngineeringPackageIn",
        "WindowsQuickFixEngineeringPackageOut": "_cloudasset_137_WindowsQuickFixEngineeringPackageOut",
        "OutputConfigIn": "_cloudasset_138_OutputConfigIn",
        "OutputConfigOut": "_cloudasset_139_OutputConfigOut",
        "GoogleCloudAssetV1p7beta1ResourceIn": "_cloudasset_140_GoogleCloudAssetV1p7beta1ResourceIn",
        "GoogleCloudAssetV1p7beta1ResourceOut": "_cloudasset_141_GoogleCloudAssetV1p7beta1ResourceOut",
        "GoogleCloudAssetV1IdentityListIn": "_cloudasset_142_GoogleCloudAssetV1IdentityListIn",
        "GoogleCloudAssetV1IdentityListOut": "_cloudasset_143_GoogleCloudAssetV1IdentityListOut",
        "ConditionEvaluationIn": "_cloudasset_144_ConditionEvaluationIn",
        "ConditionEvaluationOut": "_cloudasset_145_ConditionEvaluationOut",
        "SoftwarePackageIn": "_cloudasset_146_SoftwarePackageIn",
        "SoftwarePackageOut": "_cloudasset_147_SoftwarePackageOut",
        "GoogleCloudAssetV1AccessIn": "_cloudasset_148_GoogleCloudAssetV1AccessIn",
        "GoogleCloudAssetV1AccessOut": "_cloudasset_149_GoogleCloudAssetV1AccessOut",
        "GoogleCloudAssetV1StringValuesIn": "_cloudasset_150_GoogleCloudAssetV1StringValuesIn",
        "GoogleCloudAssetV1StringValuesOut": "_cloudasset_151_GoogleCloudAssetV1StringValuesOut",
        "IamPolicyAnalysisStateIn": "_cloudasset_152_IamPolicyAnalysisStateIn",
        "IamPolicyAnalysisStateOut": "_cloudasset_153_IamPolicyAnalysisStateOut",
        "GoogleIdentityAccesscontextmanagerV1BasicLevelIn": "_cloudasset_154_GoogleIdentityAccesscontextmanagerV1BasicLevelIn",
        "GoogleIdentityAccesscontextmanagerV1BasicLevelOut": "_cloudasset_155_GoogleIdentityAccesscontextmanagerV1BasicLevelOut",
        "GoogleIdentityAccesscontextmanagerV1IngressToIn": "_cloudasset_156_GoogleIdentityAccesscontextmanagerV1IngressToIn",
        "GoogleIdentityAccesscontextmanagerV1IngressToOut": "_cloudasset_157_GoogleIdentityAccesscontextmanagerV1IngressToOut",
        "RelatedAssetsIn": "_cloudasset_158_RelatedAssetsIn",
        "RelatedAssetsOut": "_cloudasset_159_RelatedAssetsOut",
        "StatusIn": "_cloudasset_160_StatusIn",
        "StatusOut": "_cloudasset_161_StatusOut",
        "GoogleIdentityAccesscontextmanagerV1EgressPolicyIn": "_cloudasset_162_GoogleIdentityAccesscontextmanagerV1EgressPolicyIn",
        "GoogleIdentityAccesscontextmanagerV1EgressPolicyOut": "_cloudasset_163_GoogleIdentityAccesscontextmanagerV1EgressPolicyOut",
        "InventoryIn": "_cloudasset_164_InventoryIn",
        "InventoryOut": "_cloudasset_165_InventoryOut",
        "FeedIn": "_cloudasset_166_FeedIn",
        "FeedOut": "_cloudasset_167_FeedOut",
        "AccessSelectorIn": "_cloudasset_168_AccessSelectorIn",
        "AccessSelectorOut": "_cloudasset_169_AccessSelectorOut",
        "ExportAssetsRequestIn": "_cloudasset_170_ExportAssetsRequestIn",
        "ExportAssetsRequestOut": "_cloudasset_171_ExportAssetsRequestOut",
        "CreateFeedRequestIn": "_cloudasset_172_CreateFeedRequestIn",
        "CreateFeedRequestOut": "_cloudasset_173_CreateFeedRequestOut",
        "PermissionsIn": "_cloudasset_174_PermissionsIn",
        "PermissionsOut": "_cloudasset_175_PermissionsOut",
        "ResourceIn": "_cloudasset_176_ResourceIn",
        "ResourceOut": "_cloudasset_177_ResourceOut",
        "ListSavedQueriesResponseIn": "_cloudasset_178_ListSavedQueriesResponseIn",
        "ListSavedQueriesResponseOut": "_cloudasset_179_ListSavedQueriesResponseOut",
        "RelatedResourcesIn": "_cloudasset_180_RelatedResourcesIn",
        "RelatedResourcesOut": "_cloudasset_181_RelatedResourcesOut",
        "AnalyzeIamPolicyLongrunningResponseIn": "_cloudasset_182_AnalyzeIamPolicyLongrunningResponseIn",
        "AnalyzeIamPolicyLongrunningResponseOut": "_cloudasset_183_AnalyzeIamPolicyLongrunningResponseOut",
        "GcsDestinationIn": "_cloudasset_184_GcsDestinationIn",
        "GcsDestinationOut": "_cloudasset_185_GcsDestinationOut",
        "GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationIn": "_cloudasset_186_GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationIn",
        "GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationOut": "_cloudasset_187_GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationOut",
        "TemporalAssetIn": "_cloudasset_188_TemporalAssetIn",
        "TemporalAssetOut": "_cloudasset_189_TemporalAssetOut",
        "RelationshipAttributesIn": "_cloudasset_190_RelationshipAttributesIn",
        "RelationshipAttributesOut": "_cloudasset_191_RelationshipAttributesOut",
        "AnalyzeOrgPoliciesResponseIn": "_cloudasset_192_AnalyzeOrgPoliciesResponseIn",
        "AnalyzeOrgPoliciesResponseOut": "_cloudasset_193_AnalyzeOrgPoliciesResponseOut",
        "AnalyzeIamPolicyResponseIn": "_cloudasset_194_AnalyzeIamPolicyResponseIn",
        "AnalyzeIamPolicyResponseOut": "_cloudasset_195_AnalyzeIamPolicyResponseOut",
        "TableFieldSchemaIn": "_cloudasset_196_TableFieldSchemaIn",
        "TableFieldSchemaOut": "_cloudasset_197_TableFieldSchemaOut",
        "BindingIn": "_cloudasset_198_BindingIn",
        "BindingOut": "_cloudasset_199_BindingOut",
        "GoogleIdentityAccesscontextmanagerV1AccessPolicyIn": "_cloudasset_200_GoogleIdentityAccesscontextmanagerV1AccessPolicyIn",
        "GoogleIdentityAccesscontextmanagerV1AccessPolicyOut": "_cloudasset_201_GoogleIdentityAccesscontextmanagerV1AccessPolicyOut",
        "GoogleCloudOrgpolicyV1ListPolicyIn": "_cloudasset_202_GoogleCloudOrgpolicyV1ListPolicyIn",
        "GoogleCloudOrgpolicyV1ListPolicyOut": "_cloudasset_203_GoogleCloudOrgpolicyV1ListPolicyOut",
        "FeedOutputConfigIn": "_cloudasset_204_FeedOutputConfigIn",
        "FeedOutputConfigOut": "_cloudasset_205_FeedOutputConfigOut",
        "GoogleCloudAssetV1RuleIn": "_cloudasset_206_GoogleCloudAssetV1RuleIn",
        "GoogleCloudAssetV1RuleOut": "_cloudasset_207_GoogleCloudAssetV1RuleOut",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetIn": "_cloudasset_208_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetIn",
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetOut": "_cloudasset_209_GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetOut",
        "SearchAllIamPoliciesResponseIn": "_cloudasset_210_SearchAllIamPoliciesResponseIn",
        "SearchAllIamPoliciesResponseOut": "_cloudasset_211_SearchAllIamPoliciesResponseOut",
        "ConditionContextIn": "_cloudasset_212_ConditionContextIn",
        "ConditionContextOut": "_cloudasset_213_ConditionContextOut",
        "GoogleCloudAssetV1BigQueryDestinationIn": "_cloudasset_214_GoogleCloudAssetV1BigQueryDestinationIn",
        "GoogleCloudAssetV1BigQueryDestinationOut": "_cloudasset_215_GoogleCloudAssetV1BigQueryDestinationOut",
        "GoogleIdentityAccesscontextmanagerV1MethodSelectorIn": "_cloudasset_216_GoogleIdentityAccesscontextmanagerV1MethodSelectorIn",
        "GoogleIdentityAccesscontextmanagerV1MethodSelectorOut": "_cloudasset_217_GoogleIdentityAccesscontextmanagerV1MethodSelectorOut",
        "GoogleIdentityAccesscontextmanagerV1ApiOperationIn": "_cloudasset_218_GoogleIdentityAccesscontextmanagerV1ApiOperationIn",
        "GoogleIdentityAccesscontextmanagerV1ApiOperationOut": "_cloudasset_219_GoogleIdentityAccesscontextmanagerV1ApiOperationOut",
        "GoogleCloudAssetV1EdgeIn": "_cloudasset_220_GoogleCloudAssetV1EdgeIn",
        "GoogleCloudAssetV1EdgeOut": "_cloudasset_221_GoogleCloudAssetV1EdgeOut",
        "QueryContentIn": "_cloudasset_222_QueryContentIn",
        "QueryContentOut": "_cloudasset_223_QueryContentOut",
        "GoogleCloudOrgpolicyV1RestoreDefaultIn": "_cloudasset_224_GoogleCloudOrgpolicyV1RestoreDefaultIn",
        "GoogleCloudOrgpolicyV1RestoreDefaultOut": "_cloudasset_225_GoogleCloudOrgpolicyV1RestoreDefaultOut",
        "SearchAllResourcesResponseIn": "_cloudasset_226_SearchAllResourcesResponseIn",
        "SearchAllResourcesResponseOut": "_cloudasset_227_SearchAllResourcesResponseOut",
        "IamPolicyAnalysisOutputConfigIn": "_cloudasset_228_IamPolicyAnalysisOutputConfigIn",
        "IamPolicyAnalysisOutputConfigOut": "_cloudasset_229_IamPolicyAnalysisOutputConfigOut",
        "MoveImpactIn": "_cloudasset_230_MoveImpactIn",
        "MoveImpactOut": "_cloudasset_231_MoveImpactOut",
        "IamPolicyAnalysisResultIn": "_cloudasset_232_IamPolicyAnalysisResultIn",
        "IamPolicyAnalysisResultOut": "_cloudasset_233_IamPolicyAnalysisResultOut",
        "GoogleCloudAssetV1ListConstraintIn": "_cloudasset_234_GoogleCloudAssetV1ListConstraintIn",
        "GoogleCloudAssetV1ListConstraintOut": "_cloudasset_235_GoogleCloudAssetV1ListConstraintOut",
        "GoogleCloudAssetV1CustomConstraintIn": "_cloudasset_236_GoogleCloudAssetV1CustomConstraintIn",
        "GoogleCloudAssetV1CustomConstraintOut": "_cloudasset_237_GoogleCloudAssetV1CustomConstraintOut",
        "MoveAnalysisResultIn": "_cloudasset_238_MoveAnalysisResultIn",
        "MoveAnalysisResultOut": "_cloudasset_239_MoveAnalysisResultOut",
        "GoogleCloudAssetV1ConstraintIn": "_cloudasset_240_GoogleCloudAssetV1ConstraintIn",
        "GoogleCloudAssetV1ConstraintOut": "_cloudasset_241_GoogleCloudAssetV1ConstraintOut",
        "SavedQueryIn": "_cloudasset_242_SavedQueryIn",
        "SavedQueryOut": "_cloudasset_243_SavedQueryOut",
        "AnalyzeMoveResponseIn": "_cloudasset_244_AnalyzeMoveResponseIn",
        "AnalyzeMoveResponseOut": "_cloudasset_245_AnalyzeMoveResponseOut",
        "GoogleIdentityAccesscontextmanagerV1DevicePolicyIn": "_cloudasset_246_GoogleIdentityAccesscontextmanagerV1DevicePolicyIn",
        "GoogleIdentityAccesscontextmanagerV1DevicePolicyOut": "_cloudasset_247_GoogleIdentityAccesscontextmanagerV1DevicePolicyOut",
        "TableSchemaIn": "_cloudasset_248_TableSchemaIn",
        "TableSchemaOut": "_cloudasset_249_TableSchemaOut",
        "QueryAssetsRequestIn": "_cloudasset_250_QueryAssetsRequestIn",
        "QueryAssetsRequestOut": "_cloudasset_251_QueryAssetsRequestOut",
        "OsInfoIn": "_cloudasset_252_OsInfoIn",
        "OsInfoOut": "_cloudasset_253_OsInfoOut",
        "PubsubDestinationIn": "_cloudasset_254_PubsubDestinationIn",
        "PubsubDestinationOut": "_cloudasset_255_PubsubDestinationOut",
        "BigQueryDestinationIn": "_cloudasset_256_BigQueryDestinationIn",
        "BigQueryDestinationOut": "_cloudasset_257_BigQueryDestinationOut",
        "ItemIn": "_cloudasset_258_ItemIn",
        "ItemOut": "_cloudasset_259_ItemOut",
        "GoogleCloudOrgpolicyV1PolicyIn": "_cloudasset_260_GoogleCloudOrgpolicyV1PolicyIn",
        "GoogleCloudOrgpolicyV1PolicyOut": "_cloudasset_261_GoogleCloudOrgpolicyV1PolicyOut",
        "GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesIn": "_cloudasset_262_GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesIn",
        "GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesOut": "_cloudasset_263_GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesOut",
        "GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn": "_cloudasset_264_GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn",
        "GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut": "_cloudasset_265_GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut",
        "ExprIn": "_cloudasset_266_ExprIn",
        "ExprOut": "_cloudasset_267_ExprOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["IamPolicyAnalysisQueryIn"] = t.struct(
        {
            "scope": t.string(),
            "resourceSelector": t.proxy(renames["ResourceSelectorIn"]).optional(),
            "options": t.proxy(renames["OptionsIn"]).optional(),
            "conditionContext": t.proxy(renames["ConditionContextIn"]).optional(),
            "accessSelector": t.proxy(renames["AccessSelectorIn"]).optional(),
            "identitySelector": t.proxy(renames["IdentitySelectorIn"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisQueryIn"])
    types["IamPolicyAnalysisQueryOut"] = t.struct(
        {
            "scope": t.string(),
            "resourceSelector": t.proxy(renames["ResourceSelectorOut"]).optional(),
            "options": t.proxy(renames["OptionsOut"]).optional(),
            "conditionContext": t.proxy(renames["ConditionContextOut"]).optional(),
            "accessSelector": t.proxy(renames["AccessSelectorOut"]).optional(),
            "identitySelector": t.proxy(renames["IdentitySelectorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisQueryOut"])
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
    types["AnalyzerOrgPolicyIn"] = t.struct(
        {
            "inheritFromParent": t.boolean().optional(),
            "reset": t.boolean().optional(),
            "appliedResource": t.string().optional(),
            "rules": t.array(t.proxy(renames["GoogleCloudAssetV1RuleIn"])).optional(),
            "attachedResource": t.string().optional(),
        }
    ).named(renames["AnalyzerOrgPolicyIn"])
    types["AnalyzerOrgPolicyOut"] = t.struct(
        {
            "inheritFromParent": t.boolean().optional(),
            "reset": t.boolean().optional(),
            "appliedResource": t.string().optional(),
            "rules": t.array(t.proxy(renames["GoogleCloudAssetV1RuleOut"])).optional(),
            "attachedResource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzerOrgPolicyOut"])
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
    types["ResourceSearchResultIn"] = t.struct(
        {
            "attachedResources": t.array(
                t.proxy(renames["AttachedResourceIn"])
            ).optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "project": t.string().optional(),
            "createTime": t.string().optional(),
            "versionedResources": t.array(
                t.proxy(renames["VersionedResourceIn"])
            ).optional(),
            "updateTime": t.string().optional(),
            "tagValues": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "folders": t.array(t.string()).optional(),
            "relationships": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "kmsKey": t.string().optional(),
            "tagKeys": t.array(t.string()).optional(),
            "location": t.string().optional(),
            "additionalAttributes": t.struct({"_": t.string().optional()}).optional(),
            "assetType": t.string().optional(),
            "parentAssetType": t.string().optional(),
            "parentFullResourceName": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "kmsKeys": t.array(t.string()).optional(),
            "tagValueIds": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["ResourceSearchResultIn"])
    types["ResourceSearchResultOut"] = t.struct(
        {
            "attachedResources": t.array(
                t.proxy(renames["AttachedResourceOut"])
            ).optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "project": t.string().optional(),
            "createTime": t.string().optional(),
            "versionedResources": t.array(
                t.proxy(renames["VersionedResourceOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "tagValues": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "folders": t.array(t.string()).optional(),
            "relationships": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "kmsKey": t.string().optional(),
            "tagKeys": t.array(t.string()).optional(),
            "location": t.string().optional(),
            "additionalAttributes": t.struct({"_": t.string().optional()}).optional(),
            "assetType": t.string().optional(),
            "parentAssetType": t.string().optional(),
            "parentFullResourceName": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "kmsKeys": t.array(t.string()).optional(),
            "tagValueIds": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceSearchResultOut"])
    types["ZypperPatchIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "patchName": t.string().optional(),
            "summary": t.string().optional(),
            "category": t.string().optional(),
        }
    ).named(renames["ZypperPatchIn"])
    types["ZypperPatchOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "patchName": t.string().optional(),
            "summary": t.string().optional(),
            "category": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZypperPatchOut"])
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
    types["QueryResultIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rows": t.array(t.struct({"_": t.string().optional()})).optional(),
            "totalRows": t.string().optional(),
            "schema": t.proxy(renames["TableSchemaIn"]).optional(),
        }
    ).named(renames["QueryResultIn"])
    types["QueryResultOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rows": t.array(t.struct({"_": t.string().optional()})).optional(),
            "totalRows": t.string().optional(),
            "schema": t.proxy(renames["TableSchemaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResultOut"])
    types["GoogleCloudOrgpolicyV1BooleanPolicyIn"] = t.struct(
        {"enforced": t.boolean().optional()}
    ).named(renames["GoogleCloudOrgpolicyV1BooleanPolicyIn"])
    types["GoogleCloudOrgpolicyV1BooleanPolicyOut"] = t.struct(
        {
            "enforced": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1BooleanPolicyOut"])
    types["GoogleCloudAssetV1GovernedContainerIn"] = t.struct(
        {
            "policyBundle": t.array(t.proxy(renames["AnalyzerOrgPolicyIn"])).optional(),
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyIn"]).optional(),
            "parent": t.string().optional(),
            "fullResourceName": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1GovernedContainerIn"])
    types["GoogleCloudAssetV1GovernedContainerOut"] = t.struct(
        {
            "policyBundle": t.array(
                t.proxy(renames["AnalyzerOrgPolicyOut"])
            ).optional(),
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyOut"]).optional(),
            "parent": t.string().optional(),
            "fullResourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1GovernedContainerOut"])
    types["GoogleIdentityAccesscontextmanagerV1AccessLevelIn"] = t.struct(
        {
            "description": t.string().optional(),
            "basic": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1BasicLevelIn"]
            ).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "custom": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1CustomLevelIn"]
            ).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1AccessLevelIn"])
    types["GoogleIdentityAccesscontextmanagerV1AccessLevelOut"] = t.struct(
        {
            "description": t.string().optional(),
            "basic": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1BasicLevelOut"]
            ).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "custom": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1CustomLevelOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1AccessLevelOut"])
    types["WindowsUpdatePackageIn"] = t.struct(
        {
            "categories": t.array(
                t.proxy(renames["WindowsUpdateCategoryIn"])
            ).optional(),
            "supportUrl": t.string().optional(),
            "description": t.string().optional(),
            "moreInfoUrls": t.array(t.string()).optional(),
            "lastDeploymentChangeTime": t.string().optional(),
            "kbArticleIds": t.array(t.string()).optional(),
            "revisionNumber": t.integer().optional(),
            "title": t.string().optional(),
            "updateId": t.string().optional(),
        }
    ).named(renames["WindowsUpdatePackageIn"])
    types["WindowsUpdatePackageOut"] = t.struct(
        {
            "categories": t.array(
                t.proxy(renames["WindowsUpdateCategoryOut"])
            ).optional(),
            "supportUrl": t.string().optional(),
            "description": t.string().optional(),
            "moreInfoUrls": t.array(t.string()).optional(),
            "lastDeploymentChangeTime": t.string().optional(),
            "kbArticleIds": t.array(t.string()).optional(),
            "revisionNumber": t.integer().optional(),
            "title": t.string().optional(),
            "updateId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsUpdatePackageOut"])
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
    types["RelatedAssetIn"] = t.struct(
        {
            "asset": t.string().optional(),
            "relationshipType": t.string().optional(),
            "ancestors": t.array(t.string()).optional(),
            "assetType": t.string().optional(),
        }
    ).named(renames["RelatedAssetIn"])
    types["RelatedAssetOut"] = t.struct(
        {
            "asset": t.string().optional(),
            "relationshipType": t.string().optional(),
            "ancestors": t.array(t.string()).optional(),
            "assetType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelatedAssetOut"])
    types["AnalyzeOrgPolicyGovernedContainersResponseIn"] = t.struct(
        {
            "constraint": t.proxy(renames["AnalyzerOrgPolicyConstraintIn"]).optional(),
            "nextPageToken": t.string().optional(),
            "governedContainers": t.array(
                t.proxy(renames["GoogleCloudAssetV1GovernedContainerIn"])
            ).optional(),
        }
    ).named(renames["AnalyzeOrgPolicyGovernedContainersResponseIn"])
    types["AnalyzeOrgPolicyGovernedContainersResponseOut"] = t.struct(
        {
            "constraint": t.proxy(renames["AnalyzerOrgPolicyConstraintOut"]).optional(),
            "nextPageToken": t.string().optional(),
            "governedContainers": t.array(
                t.proxy(renames["GoogleCloudAssetV1GovernedContainerOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeOrgPolicyGovernedContainersResponseOut"])
    types["WindowsApplicationIn"] = t.struct(
        {
            "helpLink": t.string().optional(),
            "displayVersion": t.string().optional(),
            "publisher": t.string().optional(),
            "installDate": t.proxy(renames["DateIn"]).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["WindowsApplicationIn"])
    types["WindowsApplicationOut"] = t.struct(
        {
            "helpLink": t.string().optional(),
            "displayVersion": t.string().optional(),
            "publisher": t.string().optional(),
            "installDate": t.proxy(renames["DateOut"]).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsApplicationOut"])
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
    types["GoogleIdentityAccesscontextmanagerV1CustomLevelIn"] = t.struct(
        {"expr": t.proxy(renames["ExprIn"])}
    ).named(renames["GoogleIdentityAccesscontextmanagerV1CustomLevelIn"])
    types["GoogleIdentityAccesscontextmanagerV1CustomLevelOut"] = t.struct(
        {
            "expr": t.proxy(renames["ExprOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1CustomLevelOut"])
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
    types["OrgPolicyResultIn"] = t.struct(
        {
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyIn"]).optional(),
            "policyBundle": t.array(t.proxy(renames["AnalyzerOrgPolicyIn"])).optional(),
        }
    ).named(renames["OrgPolicyResultIn"])
    types["OrgPolicyResultOut"] = t.struct(
        {
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyOut"]).optional(),
            "policyBundle": t.array(
                t.proxy(renames["AnalyzerOrgPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrgPolicyResultOut"])
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
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["GoogleCloudAssetV1GcsDestinationIn"] = t.struct({"uri": t.string()}).named(
        renames["GoogleCloudAssetV1GcsDestinationIn"]
    )
    types["GoogleCloudAssetV1GcsDestinationOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudAssetV1GcsDestinationOut"])
    types["PartitionSpecIn"] = t.struct({"partitionKey": t.string().optional()}).named(
        renames["PartitionSpecIn"]
    )
    types["PartitionSpecOut"] = t.struct(
        {
            "partitionKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionSpecOut"])
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
    types["OptionsIn"] = t.struct(
        {
            "outputGroupEdges": t.boolean().optional(),
            "outputResourceEdges": t.boolean().optional(),
            "analyzeServiceAccountImpersonation": t.boolean().optional(),
            "expandGroups": t.boolean().optional(),
            "expandResources": t.boolean().optional(),
            "expandRoles": t.boolean().optional(),
        }
    ).named(renames["OptionsIn"])
    types["OptionsOut"] = t.struct(
        {
            "outputGroupEdges": t.boolean().optional(),
            "outputResourceEdges": t.boolean().optional(),
            "analyzeServiceAccountImpersonation": t.boolean().optional(),
            "expandGroups": t.boolean().optional(),
            "expandResources": t.boolean().optional(),
            "expandRoles": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionsOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["IamPolicyAnalysisIn"] = t.struct(
        {
            "fullyExplored": t.boolean().optional(),
            "analysisResults": t.array(
                t.proxy(renames["IamPolicyAnalysisResultIn"])
            ).optional(),
            "nonCriticalErrors": t.array(
                t.proxy(renames["IamPolicyAnalysisStateIn"])
            ).optional(),
            "analysisQuery": t.proxy(renames["IamPolicyAnalysisQueryIn"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisIn"])
    types["IamPolicyAnalysisOut"] = t.struct(
        {
            "fullyExplored": t.boolean().optional(),
            "analysisResults": t.array(
                t.proxy(renames["IamPolicyAnalysisResultOut"])
            ).optional(),
            "nonCriticalErrors": t.array(
                t.proxy(renames["IamPolicyAnalysisStateOut"])
            ).optional(),
            "analysisQuery": t.proxy(renames["IamPolicyAnalysisQueryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisOut"])
    types["BatchGetAssetsHistoryResponseIn"] = t.struct(
        {"assets": t.array(t.proxy(renames["TemporalAssetIn"])).optional()}
    ).named(renames["BatchGetAssetsHistoryResponseIn"])
    types["BatchGetAssetsHistoryResponseOut"] = t.struct(
        {
            "assets": t.array(t.proxy(renames["TemporalAssetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetAssetsHistoryResponseOut"])
    types["AnalyzeIamPolicyLongrunningMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AnalyzeIamPolicyLongrunningMetadataIn"])
    types["AnalyzeIamPolicyLongrunningMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeIamPolicyLongrunningMetadataOut"])
    types["GoogleCloudAssetV1p7beta1AssetIn"] = t.struct(
        {
            "ancestors": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "accessPolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyIn"]
            ).optional(),
            "orgPolicy": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV1PolicyIn"])
            ).optional(),
            "assetType": t.string().optional(),
            "iamPolicy": t.proxy(renames["PolicyIn"]).optional(),
            "name": t.string().optional(),
            "accessLevel": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessLevelIn"]
            ).optional(),
            "resource": t.proxy(
                renames["GoogleCloudAssetV1p7beta1ResourceIn"]
            ).optional(),
            "relatedAssets": t.proxy(
                renames["GoogleCloudAssetV1p7beta1RelatedAssetsIn"]
            ).optional(),
            "servicePerimeter": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1AssetIn"])
    types["GoogleCloudAssetV1p7beta1AssetOut"] = t.struct(
        {
            "ancestors": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "accessPolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyOut"]
            ).optional(),
            "orgPolicy": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV1PolicyOut"])
            ).optional(),
            "assetType": t.string().optional(),
            "iamPolicy": t.proxy(renames["PolicyOut"]).optional(),
            "name": t.string().optional(),
            "accessLevel": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessLevelOut"]
            ).optional(),
            "resource": t.proxy(
                renames["GoogleCloudAssetV1p7beta1ResourceOut"]
            ).optional(),
            "relatedAssets": t.proxy(
                renames["GoogleCloudAssetV1p7beta1RelatedAssetsOut"]
            ).optional(),
            "servicePerimeter": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1AssetOut"])
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["ResourceSelectorIn"] = t.struct({"fullResourceName": t.string()}).named(
        renames["ResourceSelectorIn"]
    )
    types["ResourceSelectorOut"] = t.struct(
        {
            "fullResourceName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceSelectorOut"])
    types["IdentitySelectorIn"] = t.struct({"identity": t.string()}).named(
        renames["IdentitySelectorIn"]
    )
    types["IdentitySelectorOut"] = t.struct(
        {"identity": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IdentitySelectorOut"])
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
    types["ListFeedsResponseIn"] = t.struct(
        {"feeds": t.array(t.proxy(renames["FeedIn"])).optional()}
    ).named(renames["ListFeedsResponseIn"])
    types["ListFeedsResponseOut"] = t.struct(
        {
            "feeds": t.array(t.proxy(renames["FeedOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFeedsResponseOut"])
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["MoveAnalysisIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "analysis": t.proxy(renames["MoveAnalysisResultIn"]).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["MoveAnalysisIn"])
    types["MoveAnalysisOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "analysis": t.proxy(renames["MoveAnalysisResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveAnalysisOut"])
    types["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn"] = t.struct(
        {
            "egressPolicies": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1EgressPolicyIn"])
            ).optional(),
            "restrictedServices": t.array(t.string()).optional(),
            "accessLevels": t.array(t.string()).optional(),
            "ingressPolicies": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1IngressPolicyIn"])
            ).optional(),
            "vpcAccessibleServices": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesIn"]
            ).optional(),
            "resources": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn"])
    types["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut"] = t.struct(
        {
            "egressPolicies": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1EgressPolicyOut"])
            ).optional(),
            "restrictedServices": t.array(t.string()).optional(),
            "accessLevels": t.array(t.string()).optional(),
            "ingressPolicies": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1IngressPolicyOut"])
            ).optional(),
            "vpcAccessibleServices": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1VpcAccessibleServicesOut"]
            ).optional(),
            "resources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut"])
    types["IamPolicySearchResultIn"] = t.struct(
        {
            "organization": t.string().optional(),
            "resource": t.string().optional(),
            "explanation": t.proxy(renames["ExplanationIn"]).optional(),
            "assetType": t.string().optional(),
            "project": t.string().optional(),
            "folders": t.array(t.string()).optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
        }
    ).named(renames["IamPolicySearchResultIn"])
    types["IamPolicySearchResultOut"] = t.struct(
        {
            "organization": t.string().optional(),
            "resource": t.string().optional(),
            "explanation": t.proxy(renames["ExplanationOut"]).optional(),
            "assetType": t.string().optional(),
            "project": t.string().optional(),
            "folders": t.array(t.string()).optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicySearchResultOut"])
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
            "relatedAsset": t.proxy(renames["RelatedAssetIn"]).optional(),
            "name": t.string().optional(),
            "iamPolicy": t.proxy(renames["PolicyIn"]).optional(),
            "resource": t.proxy(renames["ResourceIn"]).optional(),
            "orgPolicy": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV1PolicyIn"])
            ).optional(),
            "servicePerimeter": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn"]
            ).optional(),
            "accessPolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyIn"]
            ).optional(),
            "relatedAssets": t.proxy(renames["RelatedAssetsIn"]).optional(),
            "ancestors": t.array(t.string()).optional(),
            "assetType": t.string().optional(),
            "osInventory": t.proxy(renames["InventoryIn"]).optional(),
            "accessLevel": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessLevelIn"]
            ).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "relatedAsset": t.proxy(renames["RelatedAssetOut"]).optional(),
            "name": t.string().optional(),
            "iamPolicy": t.proxy(renames["PolicyOut"]).optional(),
            "resource": t.proxy(renames["ResourceOut"]).optional(),
            "orgPolicy": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV1PolicyOut"])
            ).optional(),
            "servicePerimeter": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut"]
            ).optional(),
            "accessPolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyOut"]
            ).optional(),
            "relatedAssets": t.proxy(renames["RelatedAssetsOut"]).optional(),
            "ancestors": t.array(t.string()).optional(),
            "assetType": t.string().optional(),
            "osInventory": t.proxy(renames["InventoryOut"]).optional(),
            "accessLevel": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1AccessLevelOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
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
    types["ExplanationIn"] = t.struct(
        {"matchedPermissions": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ExplanationIn"])
    types["ExplanationOut"] = t.struct(
        {
            "matchedPermissions": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExplanationOut"])
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
    types["ListAssetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetIn"])).optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["ListAssetsResponseIn"])
    types["ListAssetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetOut"])).optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssetsResponseOut"])
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
    types[
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyIn"
    ] = t.struct(
        {
            "organization": t.string().optional(),
            "project": t.string().optional(),
            "attachedResource": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "folders": t.array(t.string()).optional(),
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
            "project": t.string().optional(),
            "attachedResource": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "folders": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyOut"
        ]
    )
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
    types["QueryAssetsResponseIn"] = t.struct(
        {
            "outputConfig": t.proxy(renames["QueryAssetsOutputConfigIn"]).optional(),
            "jobReference": t.string().optional(),
            "queryResult": t.proxy(renames["QueryResultIn"]).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["QueryAssetsResponseIn"])
    types["QueryAssetsResponseOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["QueryAssetsOutputConfigOut"]).optional(),
            "jobReference": t.string().optional(),
            "queryResult": t.proxy(renames["QueryResultOut"]).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryAssetsResponseOut"])
    types["GoogleIdentityAccesscontextmanagerV1EgressFromIn"] = t.struct(
        {
            "identities": t.array(t.string()).optional(),
            "identityType": t.string().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1EgressFromIn"])
    types["GoogleIdentityAccesscontextmanagerV1EgressFromOut"] = t.struct(
        {
            "identities": t.array(t.string()).optional(),
            "identityType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1EgressFromOut"])
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
    types[
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceIn"
    ] = t.struct(
        {
            "parent": t.string().optional(),
            "folders": t.array(t.string()).optional(),
            "fullResourceName": t.string().optional(),
            "organization": t.string().optional(),
            "project": t.string().optional(),
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
            "parent": t.string().optional(),
            "folders": t.array(t.string()).optional(),
            "fullResourceName": t.string().optional(),
            "organization": t.string().optional(),
            "project": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResourceOut"
        ]
    )
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
    types["GoogleCloudAssetV1BooleanConstraintIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudAssetV1BooleanConstraintIn"])
    types["GoogleCloudAssetV1BooleanConstraintOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudAssetV1BooleanConstraintOut"])
    types["GoogleIdentityAccesscontextmanagerV1ConditionIn"] = t.struct(
        {
            "ipSubnetworks": t.array(t.string()).optional(),
            "negate": t.boolean().optional(),
            "requiredAccessLevels": t.array(t.string()).optional(),
            "devicePolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1DevicePolicyIn"]
            ).optional(),
            "regions": t.array(t.string()).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ConditionIn"])
    types["GoogleIdentityAccesscontextmanagerV1ConditionOut"] = t.struct(
        {
            "ipSubnetworks": t.array(t.string()).optional(),
            "negate": t.boolean().optional(),
            "requiredAccessLevels": t.array(t.string()).optional(),
            "devicePolicy": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1DevicePolicyOut"]
            ).optional(),
            "regions": t.array(t.string()).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ConditionOut"])
    types["WindowsQuickFixEngineeringPackageIn"] = t.struct(
        {
            "description": t.string().optional(),
            "caption": t.string().optional(),
            "hotFixId": t.string().optional(),
            "installTime": t.string().optional(),
        }
    ).named(renames["WindowsQuickFixEngineeringPackageIn"])
    types["WindowsQuickFixEngineeringPackageOut"] = t.struct(
        {
            "description": t.string().optional(),
            "caption": t.string().optional(),
            "hotFixId": t.string().optional(),
            "installTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsQuickFixEngineeringPackageOut"])
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
    types["GoogleCloudAssetV1p7beta1ResourceIn"] = t.struct(
        {
            "resourceUrl": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "discoveryDocumentUri": t.string().optional(),
            "version": t.string().optional(),
            "parent": t.string().optional(),
            "discoveryName": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1ResourceIn"])
    types["GoogleCloudAssetV1p7beta1ResourceOut"] = t.struct(
        {
            "resourceUrl": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "discoveryDocumentUri": t.string().optional(),
            "version": t.string().optional(),
            "parent": t.string().optional(),
            "discoveryName": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1p7beta1ResourceOut"])
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
    types["ConditionEvaluationIn"] = t.struct(
        {"evaluationValue": t.string().optional()}
    ).named(renames["ConditionEvaluationIn"])
    types["ConditionEvaluationOut"] = t.struct(
        {
            "evaluationValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionEvaluationOut"])
    types["SoftwarePackageIn"] = t.struct(
        {
            "cosPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
            "googetPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
            "yumPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
            "aptPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
            "zypperPatch": t.proxy(renames["ZypperPatchIn"]).optional(),
            "qfePackage": t.proxy(
                renames["WindowsQuickFixEngineeringPackageIn"]
            ).optional(),
            "zypperPackage": t.proxy(renames["VersionedPackageIn"]).optional(),
            "wuaPackage": t.proxy(renames["WindowsUpdatePackageIn"]).optional(),
            "windowsApplication": t.proxy(renames["WindowsApplicationIn"]).optional(),
        }
    ).named(renames["SoftwarePackageIn"])
    types["SoftwarePackageOut"] = t.struct(
        {
            "cosPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "googetPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "yumPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "aptPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "zypperPatch": t.proxy(renames["ZypperPatchOut"]).optional(),
            "qfePackage": t.proxy(
                renames["WindowsQuickFixEngineeringPackageOut"]
            ).optional(),
            "zypperPackage": t.proxy(renames["VersionedPackageOut"]).optional(),
            "wuaPackage": t.proxy(renames["WindowsUpdatePackageOut"]).optional(),
            "windowsApplication": t.proxy(renames["WindowsApplicationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SoftwarePackageOut"])
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
    types["GoogleIdentityAccesscontextmanagerV1BasicLevelIn"] = t.struct(
        {
            "combiningFunction": t.string().optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1ConditionIn"])
            ),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1BasicLevelIn"])
    types["GoogleIdentityAccesscontextmanagerV1BasicLevelOut"] = t.struct(
        {
            "combiningFunction": t.string().optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1ConditionOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1BasicLevelOut"])
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
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["InventoryIn"] = t.struct(
        {
            "osInfo": t.proxy(renames["OsInfoIn"]).optional(),
            "items": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["InventoryIn"])
    types["InventoryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "osInfo": t.proxy(renames["OsInfoOut"]).optional(),
            "items": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryOut"])
    types["FeedIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "relationshipTypes": t.array(t.string()).optional(),
            "assetNames": t.array(t.string()).optional(),
            "assetTypes": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "feedOutputConfig": t.proxy(renames["FeedOutputConfigIn"]),
            "name": t.string(),
        }
    ).named(renames["FeedIn"])
    types["FeedOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "relationshipTypes": t.array(t.string()).optional(),
            "assetNames": t.array(t.string()).optional(),
            "assetTypes": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "feedOutputConfig": t.proxy(renames["FeedOutputConfigOut"]),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeedOut"])
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
    types["ExportAssetsRequestIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "readTime": t.string().optional(),
            "assetTypes": t.array(t.string()).optional(),
            "outputConfig": t.proxy(renames["OutputConfigIn"]),
            "relationshipTypes": t.array(t.string()).optional(),
        }
    ).named(renames["ExportAssetsRequestIn"])
    types["ExportAssetsRequestOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "readTime": t.string().optional(),
            "assetTypes": t.array(t.string()).optional(),
            "outputConfig": t.proxy(renames["OutputConfigOut"]),
            "relationshipTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportAssetsRequestOut"])
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
    types["PermissionsIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["PermissionsIn"])
    types["PermissionsOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionsOut"])
    types["ResourceIn"] = t.struct(
        {
            "location": t.string().optional(),
            "discoveryDocumentUri": t.string().optional(),
            "parent": t.string().optional(),
            "discoveryName": t.string().optional(),
            "resourceUrl": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "location": t.string().optional(),
            "discoveryDocumentUri": t.string().optional(),
            "parent": t.string().optional(),
            "discoveryName": t.string().optional(),
            "resourceUrl": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
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
    types["AnalyzeIamPolicyLongrunningResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AnalyzeIamPolicyLongrunningResponseIn"])
    types["AnalyzeIamPolicyLongrunningResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AnalyzeIamPolicyLongrunningResponseOut"])
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
    types["GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationIn"] = t.struct(
        {
            "dataset": t.string(),
            "table": t.string(),
            "writeDisposition": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationIn"])
    types["GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationOut"] = t.struct(
        {
            "dataset": t.string(),
            "table": t.string(),
            "writeDisposition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestinationOut"])
    types["TemporalAssetIn"] = t.struct(
        {
            "priorAsset": t.proxy(renames["AssetIn"]).optional(),
            "asset": t.proxy(renames["AssetIn"]).optional(),
            "priorAssetState": t.string().optional(),
            "deleted": t.boolean().optional(),
            "window": t.proxy(renames["TimeWindowIn"]).optional(),
        }
    ).named(renames["TemporalAssetIn"])
    types["TemporalAssetOut"] = t.struct(
        {
            "priorAsset": t.proxy(renames["AssetOut"]).optional(),
            "asset": t.proxy(renames["AssetOut"]).optional(),
            "priorAssetState": t.string().optional(),
            "deleted": t.boolean().optional(),
            "window": t.proxy(renames["TimeWindowOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TemporalAssetOut"])
    types["RelationshipAttributesIn"] = t.struct(
        {
            "sourceResourceType": t.string().optional(),
            "action": t.string().optional(),
            "type": t.string().optional(),
            "targetResourceType": t.string().optional(),
        }
    ).named(renames["RelationshipAttributesIn"])
    types["RelationshipAttributesOut"] = t.struct(
        {
            "sourceResourceType": t.string().optional(),
            "action": t.string().optional(),
            "type": t.string().optional(),
            "targetResourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationshipAttributesOut"])
    types["AnalyzeOrgPoliciesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "orgPolicyResults": t.array(
                t.proxy(renames["OrgPolicyResultIn"])
            ).optional(),
            "constraint": t.proxy(renames["AnalyzerOrgPolicyConstraintIn"]).optional(),
        }
    ).named(renames["AnalyzeOrgPoliciesResponseIn"])
    types["AnalyzeOrgPoliciesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "orgPolicyResults": t.array(
                t.proxy(renames["OrgPolicyResultOut"])
            ).optional(),
            "constraint": t.proxy(renames["AnalyzerOrgPolicyConstraintOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeOrgPoliciesResponseOut"])
    types["AnalyzeIamPolicyResponseIn"] = t.struct(
        {
            "fullyExplored": t.boolean().optional(),
            "mainAnalysis": t.proxy(renames["IamPolicyAnalysisIn"]).optional(),
            "serviceAccountImpersonationAnalysis": t.array(
                t.proxy(renames["IamPolicyAnalysisIn"])
            ).optional(),
        }
    ).named(renames["AnalyzeIamPolicyResponseIn"])
    types["AnalyzeIamPolicyResponseOut"] = t.struct(
        {
            "fullyExplored": t.boolean().optional(),
            "mainAnalysis": t.proxy(renames["IamPolicyAnalysisOut"]).optional(),
            "serviceAccountImpersonationAnalysis": t.array(
                t.proxy(renames["IamPolicyAnalysisOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeIamPolicyResponseOut"])
    types["TableFieldSchemaIn"] = t.struct(
        {
            "type": t.string().optional(),
            "mode": t.string().optional(),
            "field": t.string().optional(),
            "fields": t.array(t.proxy(renames["TableFieldSchemaIn"])).optional(),
        }
    ).named(renames["TableFieldSchemaIn"])
    types["TableFieldSchemaOut"] = t.struct(
        {
            "type": t.string().optional(),
            "mode": t.string().optional(),
            "field": t.string().optional(),
            "fields": t.array(t.proxy(renames["TableFieldSchemaOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableFieldSchemaOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["GoogleIdentityAccesscontextmanagerV1AccessPolicyIn"] = t.struct(
        {
            "parent": t.string(),
            "title": t.string(),
            "name": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyIn"])
    types["GoogleIdentityAccesscontextmanagerV1AccessPolicyOut"] = t.struct(
        {
            "parent": t.string(),
            "title": t.string(),
            "name": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1AccessPolicyOut"])
    types["GoogleCloudOrgpolicyV1ListPolicyIn"] = t.struct(
        {
            "deniedValues": t.array(t.string()).optional(),
            "allValues": t.string().optional(),
            "suggestedValue": t.string().optional(),
            "inheritFromParent": t.boolean().optional(),
            "allowedValues": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1ListPolicyIn"])
    types["GoogleCloudOrgpolicyV1ListPolicyOut"] = t.struct(
        {
            "deniedValues": t.array(t.string()).optional(),
            "allValues": t.string().optional(),
            "suggestedValue": t.string().optional(),
            "inheritFromParent": t.boolean().optional(),
            "allowedValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1ListPolicyOut"])
    types["FeedOutputConfigIn"] = t.struct(
        {"pubsubDestination": t.proxy(renames["PubsubDestinationIn"]).optional()}
    ).named(renames["FeedOutputConfigIn"])
    types["FeedOutputConfigOut"] = t.struct(
        {
            "pubsubDestination": t.proxy(renames["PubsubDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeedOutputConfigOut"])
    types["GoogleCloudAssetV1RuleIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "enforce": t.boolean().optional(),
            "denyAll": t.boolean().optional(),
            "values": t.proxy(renames["GoogleCloudAssetV1StringValuesIn"]).optional(),
            "allowAll": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudAssetV1RuleIn"])
    types["GoogleCloudAssetV1RuleOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "enforce": t.boolean().optional(),
            "denyAll": t.boolean().optional(),
            "values": t.proxy(renames["GoogleCloudAssetV1StringValuesOut"]).optional(),
            "allowAll": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1RuleOut"])
    types[
        "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAssetIn"
    ] = t.struct(
        {
            "policyBundle": t.array(t.proxy(renames["AnalyzerOrgPolicyIn"])).optional(),
            "governedIamPolicy": t.proxy(
                renames[
                    "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyIn"
                ]
            ).optional(),
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyIn"]).optional(),
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
            "policyBundle": t.array(
                t.proxy(renames["AnalyzerOrgPolicyOut"])
            ).optional(),
            "governedIamPolicy": t.proxy(
                renames[
                    "GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicyOut"
                ]
            ).optional(),
            "consolidatedPolicy": t.proxy(renames["AnalyzerOrgPolicyOut"]).optional(),
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
    types["SearchAllIamPoliciesResponseIn"] = t.struct(
        {
            "results": t.array(t.proxy(renames["IamPolicySearchResultIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchAllIamPoliciesResponseIn"])
    types["SearchAllIamPoliciesResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["IamPolicySearchResultOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchAllIamPoliciesResponseOut"])
    types["ConditionContextIn"] = t.struct({"accessTime": t.string().optional()}).named(
        renames["ConditionContextIn"]
    )
    types["ConditionContextOut"] = t.struct(
        {
            "accessTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionContextOut"])
    types["GoogleCloudAssetV1BigQueryDestinationIn"] = t.struct(
        {
            "partitionKey": t.string().optional(),
            "dataset": t.string(),
            "writeDisposition": t.string().optional(),
            "tablePrefix": t.string(),
        }
    ).named(renames["GoogleCloudAssetV1BigQueryDestinationIn"])
    types["GoogleCloudAssetV1BigQueryDestinationOut"] = t.struct(
        {
            "partitionKey": t.string().optional(),
            "dataset": t.string(),
            "writeDisposition": t.string().optional(),
            "tablePrefix": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1BigQueryDestinationOut"])
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
    types["GoogleCloudOrgpolicyV1RestoreDefaultIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudOrgpolicyV1RestoreDefaultIn"])
    types["GoogleCloudOrgpolicyV1RestoreDefaultOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudOrgpolicyV1RestoreDefaultOut"])
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
    types["MoveImpactIn"] = t.struct({"detail": t.string().optional()}).named(
        renames["MoveImpactIn"]
    )
    types["MoveImpactOut"] = t.struct(
        {
            "detail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveImpactOut"])
    types["IamPolicyAnalysisResultIn"] = t.struct(
        {
            "identityList": t.proxy(
                renames["GoogleCloudAssetV1IdentityListIn"]
            ).optional(),
            "iamBinding": t.proxy(renames["BindingIn"]).optional(),
            "accessControlLists": t.array(
                t.proxy(renames["GoogleCloudAssetV1AccessControlListIn"])
            ).optional(),
            "fullyExplored": t.boolean().optional(),
            "attachedResourceFullName": t.string().optional(),
        }
    ).named(renames["IamPolicyAnalysisResultIn"])
    types["IamPolicyAnalysisResultOut"] = t.struct(
        {
            "identityList": t.proxy(
                renames["GoogleCloudAssetV1IdentityListOut"]
            ).optional(),
            "iamBinding": t.proxy(renames["BindingOut"]).optional(),
            "accessControlLists": t.array(
                t.proxy(renames["GoogleCloudAssetV1AccessControlListOut"])
            ).optional(),
            "fullyExplored": t.boolean().optional(),
            "attachedResourceFullName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyAnalysisResultOut"])
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
    types["GoogleCloudAssetV1CustomConstraintIn"] = t.struct(
        {
            "name": t.string().optional(),
            "resourceTypes": t.array(t.string()).optional(),
            "actionType": t.string().optional(),
            "condition": t.string().optional(),
            "description": t.string().optional(),
            "methodTypes": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1CustomConstraintIn"])
    types["GoogleCloudAssetV1CustomConstraintOut"] = t.struct(
        {
            "name": t.string().optional(),
            "resourceTypes": t.array(t.string()).optional(),
            "actionType": t.string().optional(),
            "condition": t.string().optional(),
            "description": t.string().optional(),
            "methodTypes": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1CustomConstraintOut"])
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
    types["GoogleCloudAssetV1ConstraintIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "booleanConstraint": t.proxy(
                renames["GoogleCloudAssetV1BooleanConstraintIn"]
            ).optional(),
            "listConstraint": t.proxy(
                renames["GoogleCloudAssetV1ListConstraintIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "constraintDefault": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssetV1ConstraintIn"])
    types["GoogleCloudAssetV1ConstraintOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "booleanConstraint": t.proxy(
                renames["GoogleCloudAssetV1BooleanConstraintOut"]
            ).optional(),
            "listConstraint": t.proxy(
                renames["GoogleCloudAssetV1ListConstraintOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "constraintDefault": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssetV1ConstraintOut"])
    types["SavedQueryIn"] = t.struct(
        {
            "description": t.string().optional(),
            "content": t.proxy(renames["QueryContentIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SavedQueryIn"])
    types["SavedQueryOut"] = t.struct(
        {
            "lastUpdater": t.string().optional(),
            "createTime": t.string().optional(),
            "creator": t.string().optional(),
            "description": t.string().optional(),
            "content": t.proxy(renames["QueryContentOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "lastUpdateTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SavedQueryOut"])
    types["AnalyzeMoveResponseIn"] = t.struct(
        {"moveAnalysis": t.array(t.proxy(renames["MoveAnalysisIn"])).optional()}
    ).named(renames["AnalyzeMoveResponseIn"])
    types["AnalyzeMoveResponseOut"] = t.struct(
        {
            "moveAnalysis": t.array(t.proxy(renames["MoveAnalysisOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeMoveResponseOut"])
    types["GoogleIdentityAccesscontextmanagerV1DevicePolicyIn"] = t.struct(
        {
            "osConstraints": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1OsConstraintIn"])
            ).optional(),
            "requireAdminApproval": t.boolean().optional(),
            "requireCorpOwned": t.boolean().optional(),
            "allowedEncryptionStatuses": t.array(t.string()).optional(),
            "requireScreenlock": t.boolean().optional(),
            "allowedDeviceManagementLevels": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1DevicePolicyIn"])
    types["GoogleIdentityAccesscontextmanagerV1DevicePolicyOut"] = t.struct(
        {
            "osConstraints": t.array(
                t.proxy(renames["GoogleIdentityAccesscontextmanagerV1OsConstraintOut"])
            ).optional(),
            "requireAdminApproval": t.boolean().optional(),
            "requireCorpOwned": t.boolean().optional(),
            "allowedEncryptionStatuses": t.array(t.string()).optional(),
            "requireScreenlock": t.boolean().optional(),
            "allowedDeviceManagementLevels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1DevicePolicyOut"])
    types["TableSchemaIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["TableFieldSchemaIn"])).optional()}
    ).named(renames["TableSchemaIn"])
    types["TableSchemaOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["TableFieldSchemaOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableSchemaOut"])
    types["QueryAssetsRequestIn"] = t.struct(
        {
            "readTimeWindow": t.proxy(renames["TimeWindowIn"]).optional(),
            "pageSize": t.integer().optional(),
            "outputConfig": t.proxy(renames["QueryAssetsOutputConfigIn"]).optional(),
            "readTime": t.string().optional(),
            "statement": t.string().optional(),
            "jobReference": t.string().optional(),
            "pageToken": t.string().optional(),
            "timeout": t.string().optional(),
        }
    ).named(renames["QueryAssetsRequestIn"])
    types["QueryAssetsRequestOut"] = t.struct(
        {
            "readTimeWindow": t.proxy(renames["TimeWindowOut"]).optional(),
            "pageSize": t.integer().optional(),
            "outputConfig": t.proxy(renames["QueryAssetsOutputConfigOut"]).optional(),
            "readTime": t.string().optional(),
            "statement": t.string().optional(),
            "jobReference": t.string().optional(),
            "pageToken": t.string().optional(),
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryAssetsRequestOut"])
    types["OsInfoIn"] = t.struct(
        {
            "kernelRelease": t.string().optional(),
            "version": t.string().optional(),
            "shortName": t.string().optional(),
            "hostname": t.string().optional(),
            "osconfigAgentVersion": t.string().optional(),
            "architecture": t.string().optional(),
            "kernelVersion": t.string().optional(),
            "longName": t.string().optional(),
        }
    ).named(renames["OsInfoIn"])
    types["OsInfoOut"] = t.struct(
        {
            "kernelRelease": t.string().optional(),
            "version": t.string().optional(),
            "shortName": t.string().optional(),
            "hostname": t.string().optional(),
            "osconfigAgentVersion": t.string().optional(),
            "architecture": t.string().optional(),
            "kernelVersion": t.string().optional(),
            "longName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OsInfoOut"])
    types["PubsubDestinationIn"] = t.struct({"topic": t.string().optional()}).named(
        renames["PubsubDestinationIn"]
    )
    types["PubsubDestinationOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubDestinationOut"])
    types["BigQueryDestinationIn"] = t.struct(
        {
            "dataset": t.string(),
            "partitionSpec": t.proxy(renames["PartitionSpecIn"]).optional(),
            "table": t.string(),
            "force": t.boolean().optional(),
            "separateTablesPerAssetType": t.boolean().optional(),
        }
    ).named(renames["BigQueryDestinationIn"])
    types["BigQueryDestinationOut"] = t.struct(
        {
            "dataset": t.string(),
            "partitionSpec": t.proxy(renames["PartitionSpecOut"]).optional(),
            "table": t.string(),
            "force": t.boolean().optional(),
            "separateTablesPerAssetType": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDestinationOut"])
    types["ItemIn"] = t.struct(
        {
            "type": t.string().optional(),
            "installedPackage": t.proxy(renames["SoftwarePackageIn"]).optional(),
            "originType": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "availablePackage": t.proxy(renames["SoftwarePackageIn"]).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["ItemIn"])
    types["ItemOut"] = t.struct(
        {
            "type": t.string().optional(),
            "installedPackage": t.proxy(renames["SoftwarePackageOut"]).optional(),
            "originType": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "availablePackage": t.proxy(renames["SoftwarePackageOut"]).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemOut"])
    types["GoogleCloudOrgpolicyV1PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "restoreDefault": t.proxy(
                renames["GoogleCloudOrgpolicyV1RestoreDefaultIn"]
            ).optional(),
            "version": t.integer().optional(),
            "booleanPolicy": t.proxy(
                renames["GoogleCloudOrgpolicyV1BooleanPolicyIn"]
            ).optional(),
            "listPolicy": t.proxy(
                renames["GoogleCloudOrgpolicyV1ListPolicyIn"]
            ).optional(),
            "updateTime": t.string().optional(),
            "constraint": t.string().optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1PolicyIn"])
    types["GoogleCloudOrgpolicyV1PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "restoreDefault": t.proxy(
                renames["GoogleCloudOrgpolicyV1RestoreDefaultOut"]
            ).optional(),
            "version": t.integer().optional(),
            "booleanPolicy": t.proxy(
                renames["GoogleCloudOrgpolicyV1BooleanPolicyOut"]
            ).optional(),
            "listPolicy": t.proxy(
                renames["GoogleCloudOrgpolicyV1ListPolicyOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "constraint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV1PolicyOut"])
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
    types["GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn"] = t.struct(
        {
            "perimeterType": t.string().optional(),
            "status": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn"]
            ).optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "spec": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigIn"]
            ).optional(),
            "useExplicitDryRunSpec": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterIn"])
    types["GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut"] = t.struct(
        {
            "perimeterType": t.string().optional(),
            "status": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut"]
            ).optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "spec": t.proxy(
                renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfigOut"]
            ).optional(),
            "useExplicitDryRunSpec": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityAccesscontextmanagerV1ServicePerimeterOut"])
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

    functions = {}
    functions["feedsGet"] = cloudasset.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "feed": t.proxy(renames["FeedIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FeedOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["feedsDelete"] = cloudasset.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "feed": t.proxy(renames["FeedIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FeedOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["feedsCreate"] = cloudasset.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "feed": t.proxy(renames["FeedIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FeedOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["feedsList"] = cloudasset.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "feed": t.proxy(renames["FeedIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FeedOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["feedsPatch"] = cloudasset.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "feed": t.proxy(renames["FeedIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FeedOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1ExportAssets"] = cloudasset.get(
        "v1/{scope}:searchAllResources",
        t.struct(
            {
                "query": t.string().optional(),
                "scope": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "assetTypes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchAllResourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeMove"] = cloudasset.get(
        "v1/{scope}:searchAllResources",
        t.struct(
            {
                "query": t.string().optional(),
                "scope": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "assetTypes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchAllResourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeIamPolicy"] = cloudasset.get(
        "v1/{scope}:searchAllResources",
        t.struct(
            {
                "query": t.string().optional(),
                "scope": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "assetTypes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchAllResourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1QueryAssets"] = cloudasset.get(
        "v1/{scope}:searchAllResources",
        t.struct(
            {
                "query": t.string().optional(),
                "scope": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "assetTypes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchAllResourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeOrgPolicyGovernedAssets"] = cloudasset.get(
        "v1/{scope}:searchAllResources",
        t.struct(
            {
                "query": t.string().optional(),
                "scope": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "assetTypes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchAllResourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1BatchGetAssetsHistory"] = cloudasset.get(
        "v1/{scope}:searchAllResources",
        t.struct(
            {
                "query": t.string().optional(),
                "scope": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "assetTypes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchAllResourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1SearchAllIamPolicies"] = cloudasset.get(
        "v1/{scope}:searchAllResources",
        t.struct(
            {
                "query": t.string().optional(),
                "scope": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "assetTypes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchAllResourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeIamPolicyLongrunning"] = cloudasset.get(
        "v1/{scope}:searchAllResources",
        t.struct(
            {
                "query": t.string().optional(),
                "scope": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "assetTypes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchAllResourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeOrgPolicies"] = cloudasset.get(
        "v1/{scope}:searchAllResources",
        t.struct(
            {
                "query": t.string().optional(),
                "scope": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "assetTypes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchAllResourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1AnalyzeOrgPolicyGovernedContainers"] = cloudasset.get(
        "v1/{scope}:searchAllResources",
        t.struct(
            {
                "query": t.string().optional(),
                "scope": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "assetTypes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchAllResourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1SearchAllResources"] = cloudasset.get(
        "v1/{scope}:searchAllResources",
        t.struct(
            {
                "query": t.string().optional(),
                "scope": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "assetTypes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchAllResourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["savedQueriesDelete"] = cloudasset.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "content": t.proxy(renames["QueryContentIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["savedQueriesCreate"] = cloudasset.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "content": t.proxy(renames["QueryContentIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["savedQueriesGet"] = cloudasset.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "content": t.proxy(renames["QueryContentIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["savedQueriesList"] = cloudasset.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "content": t.proxy(renames["QueryContentIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["savedQueriesPatch"] = cloudasset.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "content": t.proxy(renames["QueryContentIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SavedQueryOut"]),
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
                "pageToken": t.string().optional(),
                "contentType": t.string().optional(),
                "assetTypes": t.string().optional(),
                "pageSize": t.integer().optional(),
                "relationshipTypes": t.string().optional(),
                "readTime": t.string().optional(),
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
