from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_cloudsearch():
    cloudsearch = HTTPRuntime("https://cloudsearch.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudsearch_1_ErrorResponse",
        "ResultDisplayLineIn": "_cloudsearch_2_ResultDisplayLineIn",
        "ResultDisplayLineOut": "_cloudsearch_3_ResultDisplayLineOut",
        "DriveTimeSpanRestrictIn": "_cloudsearch_4_DriveTimeSpanRestrictIn",
        "DriveTimeSpanRestrictOut": "_cloudsearch_5_DriveTimeSpanRestrictOut",
        "QueryCountByStatusIn": "_cloudsearch_6_QueryCountByStatusIn",
        "QueryCountByStatusOut": "_cloudsearch_7_QueryCountByStatusOut",
        "FacetOptionsIn": "_cloudsearch_8_FacetOptionsIn",
        "FacetOptionsOut": "_cloudsearch_9_FacetOptionsOut",
        "ErrorInfoIn": "_cloudsearch_10_ErrorInfoIn",
        "ErrorInfoOut": "_cloudsearch_11_ErrorInfoOut",
        "ResultDebugInfoIn": "_cloudsearch_12_ResultDebugInfoIn",
        "ResultDebugInfoOut": "_cloudsearch_13_ResultDebugInfoOut",
        "SuggestRequestIn": "_cloudsearch_14_SuggestRequestIn",
        "SuggestRequestOut": "_cloudsearch_15_SuggestRequestOut",
        "GetSearchApplicationSessionStatsResponseIn": "_cloudsearch_16_GetSearchApplicationSessionStatsResponseIn",
        "GetSearchApplicationSessionStatsResponseOut": "_cloudsearch_17_GetSearchApplicationSessionStatsResponseOut",
        "QueryOperatorIn": "_cloudsearch_18_QueryOperatorIn",
        "QueryOperatorOut": "_cloudsearch_19_QueryOperatorOut",
        "EnterpriseTopazSidekickMeetingNotesCardProtoIn": "_cloudsearch_20_EnterpriseTopazSidekickMeetingNotesCardProtoIn",
        "EnterpriseTopazSidekickMeetingNotesCardProtoOut": "_cloudsearch_21_EnterpriseTopazSidekickMeetingNotesCardProtoOut",
        "IntegerOperatorOptionsIn": "_cloudsearch_22_IntegerOperatorOptionsIn",
        "IntegerOperatorOptionsOut": "_cloudsearch_23_IntegerOperatorOptionsOut",
        "RepositoryErrorIn": "_cloudsearch_24_RepositoryErrorIn",
        "RepositoryErrorOut": "_cloudsearch_25_RepositoryErrorOut",
        "GoogleDocsMetadataIn": "_cloudsearch_26_GoogleDocsMetadataIn",
        "GoogleDocsMetadataOut": "_cloudsearch_27_GoogleDocsMetadataOut",
        "ResultCountsIn": "_cloudsearch_28_ResultCountsIn",
        "ResultCountsOut": "_cloudsearch_29_ResultCountsOut",
        "EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCardIn": "_cloudsearch_30_EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCardIn",
        "EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCardOut": "_cloudsearch_31_EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCardOut",
        "DebugOptionsIn": "_cloudsearch_32_DebugOptionsIn",
        "DebugOptionsOut": "_cloudsearch_33_DebugOptionsOut",
        "DisplayedPropertyIn": "_cloudsearch_34_DisplayedPropertyIn",
        "DisplayedPropertyOut": "_cloudsearch_35_DisplayedPropertyOut",
        "EnterpriseTopazSidekickAgendaItemIn": "_cloudsearch_36_EnterpriseTopazSidekickAgendaItemIn",
        "EnterpriseTopazSidekickAgendaItemOut": "_cloudsearch_37_EnterpriseTopazSidekickAgendaItemOut",
        "SafeUrlProtoIn": "_cloudsearch_38_SafeUrlProtoIn",
        "SafeUrlProtoOut": "_cloudsearch_39_SafeUrlProtoOut",
        "FreshnessOptionsIn": "_cloudsearch_40_FreshnessOptionsIn",
        "FreshnessOptionsOut": "_cloudsearch_41_FreshnessOptionsOut",
        "EnterpriseTopazSidekickScheduledMeetingIn": "_cloudsearch_42_EnterpriseTopazSidekickScheduledMeetingIn",
        "EnterpriseTopazSidekickScheduledMeetingOut": "_cloudsearch_43_EnterpriseTopazSidekickScheduledMeetingOut",
        "CheckAccessResponseIn": "_cloudsearch_44_CheckAccessResponseIn",
        "CheckAccessResponseOut": "_cloudsearch_45_CheckAccessResponseOut",
        "AuditLoggingSettingsIn": "_cloudsearch_46_AuditLoggingSettingsIn",
        "AuditLoggingSettingsOut": "_cloudsearch_47_AuditLoggingSettingsOut",
        "RequestOptionsIn": "_cloudsearch_48_RequestOptionsIn",
        "RequestOptionsOut": "_cloudsearch_49_RequestOptionsOut",
        "PropertyDisplayOptionsIn": "_cloudsearch_50_PropertyDisplayOptionsIn",
        "PropertyDisplayOptionsOut": "_cloudsearch_51_PropertyDisplayOptionsOut",
        "SourceConfigIn": "_cloudsearch_52_SourceConfigIn",
        "SourceConfigOut": "_cloudsearch_53_SourceConfigOut",
        "EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoIn": "_cloudsearch_54_EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoIn",
        "EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoOut": "_cloudsearch_55_EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoOut",
        "InteractionIn": "_cloudsearch_56_InteractionIn",
        "InteractionOut": "_cloudsearch_57_InteractionOut",
        "GetDataSourceIndexStatsResponseIn": "_cloudsearch_58_GetDataSourceIndexStatsResponseIn",
        "GetDataSourceIndexStatsResponseOut": "_cloudsearch_59_GetDataSourceIndexStatsResponseOut",
        "DateValuesIn": "_cloudsearch_60_DateValuesIn",
        "DateValuesOut": "_cloudsearch_61_DateValuesOut",
        "ItemStructuredDataIn": "_cloudsearch_62_ItemStructuredDataIn",
        "ItemStructuredDataOut": "_cloudsearch_63_ItemStructuredDataOut",
        "SourceCrowdingConfigIn": "_cloudsearch_64_SourceCrowdingConfigIn",
        "SourceCrowdingConfigOut": "_cloudsearch_65_SourceCrowdingConfigOut",
        "ItemContentIn": "_cloudsearch_66_ItemContentIn",
        "ItemContentOut": "_cloudsearch_67_ItemContentOut",
        "VPCSettingsIn": "_cloudsearch_68_VPCSettingsIn",
        "VPCSettingsOut": "_cloudsearch_69_VPCSettingsOut",
        "UploadItemRefIn": "_cloudsearch_70_UploadItemRefIn",
        "UploadItemRefOut": "_cloudsearch_71_UploadItemRefOut",
        "RemoveActivityResponseIn": "_cloudsearch_72_RemoveActivityResponseIn",
        "RemoveActivityResponseOut": "_cloudsearch_73_RemoveActivityResponseOut",
        "PeopleSuggestionIn": "_cloudsearch_74_PeopleSuggestionIn",
        "PeopleSuggestionOut": "_cloudsearch_75_PeopleSuggestionOut",
        "ResultDisplayMetadataIn": "_cloudsearch_76_ResultDisplayMetadataIn",
        "ResultDisplayMetadataOut": "_cloudsearch_77_ResultDisplayMetadataOut",
        "EnterpriseTopazFrontendTeamsLinkIn": "_cloudsearch_78_EnterpriseTopazFrontendTeamsLinkIn",
        "EnterpriseTopazFrontendTeamsLinkOut": "_cloudsearch_79_EnterpriseTopazFrontendTeamsLinkOut",
        "DataSourceIndexStatsIn": "_cloudsearch_80_DataSourceIndexStatsIn",
        "DataSourceIndexStatsOut": "_cloudsearch_81_DataSourceIndexStatsOut",
        "ItemCountByStatusIn": "_cloudsearch_82_ItemCountByStatusIn",
        "ItemCountByStatusOut": "_cloudsearch_83_ItemCountByStatusOut",
        "ResultDisplayFieldIn": "_cloudsearch_84_ResultDisplayFieldIn",
        "ResultDisplayFieldOut": "_cloudsearch_85_ResultDisplayFieldOut",
        "EnterpriseTopazSidekickPeopleAnswerPersonAnswerCardIn": "_cloudsearch_86_EnterpriseTopazSidekickPeopleAnswerPersonAnswerCardIn",
        "EnterpriseTopazSidekickPeopleAnswerPersonAnswerCardOut": "_cloudsearch_87_EnterpriseTopazSidekickPeopleAnswerPersonAnswerCardOut",
        "GetCustomerSearchApplicationStatsResponseIn": "_cloudsearch_88_GetCustomerSearchApplicationStatsResponseIn",
        "GetCustomerSearchApplicationStatsResponseOut": "_cloudsearch_89_GetCustomerSearchApplicationStatsResponseOut",
        "QueryInterpretationIn": "_cloudsearch_90_QueryInterpretationIn",
        "QueryInterpretationOut": "_cloudsearch_91_QueryInterpretationOut",
        "EnumValuesIn": "_cloudsearch_92_EnumValuesIn",
        "EnumValuesOut": "_cloudsearch_93_EnumValuesOut",
        "EnterpriseTopazSidekickCommonDocumentIn": "_cloudsearch_94_EnterpriseTopazSidekickCommonDocumentIn",
        "EnterpriseTopazSidekickCommonDocumentOut": "_cloudsearch_95_EnterpriseTopazSidekickCommonDocumentOut",
        "EnterpriseTopazSidekickConflictingEventsCardProtoIn": "_cloudsearch_96_EnterpriseTopazSidekickConflictingEventsCardProtoIn",
        "EnterpriseTopazSidekickConflictingEventsCardProtoOut": "_cloudsearch_97_EnterpriseTopazSidekickConflictingEventsCardProtoOut",
        "ObjectPropertyOptionsIn": "_cloudsearch_98_ObjectPropertyOptionsIn",
        "ObjectPropertyOptionsOut": "_cloudsearch_99_ObjectPropertyOptionsOut",
        "OperationIn": "_cloudsearch_100_OperationIn",
        "OperationOut": "_cloudsearch_101_OperationOut",
        "ObjectDefinitionIn": "_cloudsearch_102_ObjectDefinitionIn",
        "ObjectDefinitionOut": "_cloudsearch_103_ObjectDefinitionOut",
        "IdIn": "_cloudsearch_104_IdIn",
        "IdOut": "_cloudsearch_105_IdOut",
        "EnterpriseTopazSidekickPersonIn": "_cloudsearch_106_EnterpriseTopazSidekickPersonIn",
        "EnterpriseTopazSidekickPersonOut": "_cloudsearch_107_EnterpriseTopazSidekickPersonOut",
        "UpdateDataSourceRequestIn": "_cloudsearch_108_UpdateDataSourceRequestIn",
        "UpdateDataSourceRequestOut": "_cloudsearch_109_UpdateDataSourceRequestOut",
        "EnumOperatorOptionsIn": "_cloudsearch_110_EnumOperatorOptionsIn",
        "EnumOperatorOptionsOut": "_cloudsearch_111_EnumOperatorOptionsOut",
        "GetSearchApplicationUserStatsResponseIn": "_cloudsearch_112_GetSearchApplicationUserStatsResponseIn",
        "GetSearchApplicationUserStatsResponseOut": "_cloudsearch_113_GetSearchApplicationUserStatsResponseOut",
        "SearchQualityMetadataIn": "_cloudsearch_114_SearchQualityMetadataIn",
        "SearchQualityMetadataOut": "_cloudsearch_115_SearchQualityMetadataOut",
        "TimestampValuesIn": "_cloudsearch_116_TimestampValuesIn",
        "TimestampValuesOut": "_cloudsearch_117_TimestampValuesOut",
        "HtmlPropertyOptionsIn": "_cloudsearch_118_HtmlPropertyOptionsIn",
        "HtmlPropertyOptionsOut": "_cloudsearch_119_HtmlPropertyOptionsOut",
        "PeoplePromotionCardIn": "_cloudsearch_120_PeoplePromotionCardIn",
        "PeoplePromotionCardOut": "_cloudsearch_121_PeoplePromotionCardOut",
        "ItemMetadataIn": "_cloudsearch_122_ItemMetadataIn",
        "ItemMetadataOut": "_cloudsearch_123_ItemMetadataOut",
        "RetrievalImportanceIn": "_cloudsearch_124_RetrievalImportanceIn",
        "RetrievalImportanceOut": "_cloudsearch_125_RetrievalImportanceOut",
        "EnterpriseTopazSidekickNlpMetadataIn": "_cloudsearch_126_EnterpriseTopazSidekickNlpMetadataIn",
        "EnterpriseTopazSidekickNlpMetadataOut": "_cloudsearch_127_EnterpriseTopazSidekickNlpMetadataOut",
        "PhotoIn": "_cloudsearch_128_PhotoIn",
        "PhotoOut": "_cloudsearch_129_PhotoOut",
        "DataSourceRestrictionIn": "_cloudsearch_130_DataSourceRestrictionIn",
        "DataSourceRestrictionOut": "_cloudsearch_131_DataSourceRestrictionOut",
        "EnterpriseTopazSidekickAnswerSuggestedQueryCategoryIn": "_cloudsearch_132_EnterpriseTopazSidekickAnswerSuggestedQueryCategoryIn",
        "EnterpriseTopazSidekickAnswerSuggestedQueryCategoryOut": "_cloudsearch_133_EnterpriseTopazSidekickAnswerSuggestedQueryCategoryOut",
        "EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeaderIn": "_cloudsearch_134_EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeaderIn",
        "EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeaderOut": "_cloudsearch_135_EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeaderOut",
        "SearchResultIn": "_cloudsearch_136_SearchResultIn",
        "SearchResultOut": "_cloudsearch_137_SearchResultOut",
        "EnterpriseTopazSidekickRankingParamsIn": "_cloudsearch_138_EnterpriseTopazSidekickRankingParamsIn",
        "EnterpriseTopazSidekickRankingParamsOut": "_cloudsearch_139_EnterpriseTopazSidekickRankingParamsOut",
        "EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoDisambiguationPersonIn": "_cloudsearch_140_EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoDisambiguationPersonIn",
        "EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoDisambiguationPersonOut": "_cloudsearch_141_EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoDisambiguationPersonOut",
        "StatusIn": "_cloudsearch_142_StatusIn",
        "StatusOut": "_cloudsearch_143_StatusOut",
        "NameIn": "_cloudsearch_144_NameIn",
        "NameOut": "_cloudsearch_145_NameOut",
        "ObjectValuesIn": "_cloudsearch_146_ObjectValuesIn",
        "ObjectValuesOut": "_cloudsearch_147_ObjectValuesOut",
        "EmailAddressIn": "_cloudsearch_148_EmailAddressIn",
        "EmailAddressOut": "_cloudsearch_149_EmailAddressOut",
        "ListSearchApplicationsResponseIn": "_cloudsearch_150_ListSearchApplicationsResponseIn",
        "ListSearchApplicationsResponseOut": "_cloudsearch_151_ListSearchApplicationsResponseOut",
        "SearchResponseIn": "_cloudsearch_152_SearchResponseIn",
        "SearchResponseOut": "_cloudsearch_153_SearchResponseOut",
        "TextValuesIn": "_cloudsearch_154_TextValuesIn",
        "TextValuesOut": "_cloudsearch_155_TextValuesOut",
        "SearchApplicationIn": "_cloudsearch_156_SearchApplicationIn",
        "SearchApplicationOut": "_cloudsearch_157_SearchApplicationOut",
        "QueryInterpretationOptionsIn": "_cloudsearch_158_QueryInterpretationOptionsIn",
        "QueryInterpretationOptionsOut": "_cloudsearch_159_QueryInterpretationOptionsOut",
        "DoubleValuesIn": "_cloudsearch_160_DoubleValuesIn",
        "DoubleValuesOut": "_cloudsearch_161_DoubleValuesOut",
        "DateOperatorOptionsIn": "_cloudsearch_162_DateOperatorOptionsIn",
        "DateOperatorOptionsOut": "_cloudsearch_163_DateOperatorOptionsOut",
        "SearchItemsByViewUrlResponseIn": "_cloudsearch_164_SearchItemsByViewUrlResponseIn",
        "SearchItemsByViewUrlResponseOut": "_cloudsearch_165_SearchItemsByViewUrlResponseOut",
        "ResponseDebugInfoIn": "_cloudsearch_166_ResponseDebugInfoIn",
        "ResponseDebugInfoOut": "_cloudsearch_167_ResponseDebugInfoOut",
        "EnterpriseTopazSidekickCommonDebugInfoIn": "_cloudsearch_168_EnterpriseTopazSidekickCommonDebugInfoIn",
        "EnterpriseTopazSidekickCommonDebugInfoOut": "_cloudsearch_169_EnterpriseTopazSidekickCommonDebugInfoOut",
        "FieldViolationIn": "_cloudsearch_170_FieldViolationIn",
        "FieldViolationOut": "_cloudsearch_171_FieldViolationOut",
        "SnippetIn": "_cloudsearch_172_SnippetIn",
        "SnippetOut": "_cloudsearch_173_SnippetOut",
        "EnterpriseTopazSidekickCommonPersonIn": "_cloudsearch_174_EnterpriseTopazSidekickCommonPersonIn",
        "EnterpriseTopazSidekickCommonPersonOut": "_cloudsearch_175_EnterpriseTopazSidekickCommonPersonOut",
        "EnterpriseTopazSidekickMeetingNotesCardRequestIn": "_cloudsearch_176_EnterpriseTopazSidekickMeetingNotesCardRequestIn",
        "EnterpriseTopazSidekickMeetingNotesCardRequestOut": "_cloudsearch_177_EnterpriseTopazSidekickMeetingNotesCardRequestOut",
        "DatePropertyOptionsIn": "_cloudsearch_178_DatePropertyOptionsIn",
        "DatePropertyOptionsOut": "_cloudsearch_179_DatePropertyOptionsOut",
        "SearchApplicationSessionStatsIn": "_cloudsearch_180_SearchApplicationSessionStatsIn",
        "SearchApplicationSessionStatsOut": "_cloudsearch_181_SearchApplicationSessionStatsOut",
        "EnterpriseTopazSidekickCommonDocumentJustificationIn": "_cloudsearch_182_EnterpriseTopazSidekickCommonDocumentJustificationIn",
        "EnterpriseTopazSidekickCommonDocumentJustificationOut": "_cloudsearch_183_EnterpriseTopazSidekickCommonDocumentJustificationOut",
        "DoubleOperatorOptionsIn": "_cloudsearch_184_DoubleOperatorOptionsIn",
        "DoubleOperatorOptionsOut": "_cloudsearch_185_DoubleOperatorOptionsOut",
        "MatchRangeIn": "_cloudsearch_186_MatchRangeIn",
        "MatchRangeOut": "_cloudsearch_187_MatchRangeOut",
        "ValueIn": "_cloudsearch_188_ValueIn",
        "ValueOut": "_cloudsearch_189_ValueOut",
        "CompositeFilterIn": "_cloudsearch_190_CompositeFilterIn",
        "CompositeFilterOut": "_cloudsearch_191_CompositeFilterOut",
        "PropertyDefinitionIn": "_cloudsearch_192_PropertyDefinitionIn",
        "PropertyDefinitionOut": "_cloudsearch_193_PropertyDefinitionOut",
        "MapInfoIn": "_cloudsearch_194_MapInfoIn",
        "MapInfoOut": "_cloudsearch_195_MapInfoOut",
        "EnterpriseTopazSidekickRecentDocumentsCardProtoIn": "_cloudsearch_196_EnterpriseTopazSidekickRecentDocumentsCardProtoIn",
        "EnterpriseTopazSidekickRecentDocumentsCardProtoOut": "_cloudsearch_197_EnterpriseTopazSidekickRecentDocumentsCardProtoOut",
        "StructuredResultIn": "_cloudsearch_198_StructuredResultIn",
        "StructuredResultOut": "_cloudsearch_199_StructuredResultOut",
        "EnterpriseTopazSidekickAssistCardProtoIn": "_cloudsearch_200_EnterpriseTopazSidekickAssistCardProtoIn",
        "EnterpriseTopazSidekickAssistCardProtoOut": "_cloudsearch_201_EnterpriseTopazSidekickAssistCardProtoOut",
        "UnmappedIdentityIn": "_cloudsearch_202_UnmappedIdentityIn",
        "UnmappedIdentityOut": "_cloudsearch_203_UnmappedIdentityOut",
        "ContextIn": "_cloudsearch_204_ContextIn",
        "ContextOut": "_cloudsearch_205_ContextOut",
        "DateIn": "_cloudsearch_206_DateIn",
        "DateOut": "_cloudsearch_207_DateOut",
        "IndexItemOptionsIn": "_cloudsearch_208_IndexItemOptionsIn",
        "IndexItemOptionsOut": "_cloudsearch_209_IndexItemOptionsOut",
        "SearchRequestIn": "_cloudsearch_210_SearchRequestIn",
        "SearchRequestOut": "_cloudsearch_211_SearchRequestOut",
        "TimestampPropertyOptionsIn": "_cloudsearch_212_TimestampPropertyOptionsIn",
        "TimestampPropertyOptionsOut": "_cloudsearch_213_TimestampPropertyOptionsOut",
        "HtmlValuesIn": "_cloudsearch_214_HtmlValuesIn",
        "HtmlValuesOut": "_cloudsearch_215_HtmlValuesOut",
        "EnterpriseTopazSidekickAgendaGroupCardProtoIn": "_cloudsearch_216_EnterpriseTopazSidekickAgendaGroupCardProtoIn",
        "EnterpriseTopazSidekickAgendaGroupCardProtoOut": "_cloudsearch_217_EnterpriseTopazSidekickAgendaGroupCardProtoOut",
        "FacetBucketIn": "_cloudsearch_218_FacetBucketIn",
        "FacetBucketOut": "_cloudsearch_219_FacetBucketOut",
        "ValueFilterIn": "_cloudsearch_220_ValueFilterIn",
        "ValueFilterOut": "_cloudsearch_221_ValueFilterOut",
        "EnterpriseTopazSidekickDocumentGroupIn": "_cloudsearch_222_EnterpriseTopazSidekickDocumentGroupIn",
        "EnterpriseTopazSidekickDocumentGroupOut": "_cloudsearch_223_EnterpriseTopazSidekickDocumentGroupOut",
        "PollItemsResponseIn": "_cloudsearch_224_PollItemsResponseIn",
        "PollItemsResponseOut": "_cloudsearch_225_PollItemsResponseOut",
        "DataSourceIn": "_cloudsearch_226_DataSourceIn",
        "DataSourceOut": "_cloudsearch_227_DataSourceOut",
        "BackgroundColoredTextIn": "_cloudsearch_228_BackgroundColoredTextIn",
        "BackgroundColoredTextOut": "_cloudsearch_229_BackgroundColoredTextOut",
        "QueryActivityIn": "_cloudsearch_230_QueryActivityIn",
        "QueryActivityOut": "_cloudsearch_231_QueryActivityOut",
        "ErrorMessageIn": "_cloudsearch_232_ErrorMessageIn",
        "ErrorMessageOut": "_cloudsearch_233_ErrorMessageOut",
        "EnterpriseTopazSidekickGetAndKeepAheadCardProtoIn": "_cloudsearch_234_EnterpriseTopazSidekickGetAndKeepAheadCardProtoIn",
        "EnterpriseTopazSidekickGetAndKeepAheadCardProtoOut": "_cloudsearch_235_EnterpriseTopazSidekickGetAndKeepAheadCardProtoOut",
        "HtmlOperatorOptionsIn": "_cloudsearch_236_HtmlOperatorOptionsIn",
        "HtmlOperatorOptionsOut": "_cloudsearch_237_HtmlOperatorOptionsOut",
        "ListItemsResponseIn": "_cloudsearch_238_ListItemsResponseIn",
        "ListItemsResponseOut": "_cloudsearch_239_ListItemsResponseOut",
        "EnumValuePairIn": "_cloudsearch_240_EnumValuePairIn",
        "EnumValuePairOut": "_cloudsearch_241_EnumValuePairOut",
        "ListUnmappedIdentitiesResponseIn": "_cloudsearch_242_ListUnmappedIdentitiesResponseIn",
        "ListUnmappedIdentitiesResponseOut": "_cloudsearch_243_ListUnmappedIdentitiesResponseOut",
        "GetCustomerUserStatsResponseIn": "_cloudsearch_244_GetCustomerUserStatsResponseIn",
        "GetCustomerUserStatsResponseOut": "_cloudsearch_245_GetCustomerUserStatsResponseOut",
        "SpellResultIn": "_cloudsearch_246_SpellResultIn",
        "SpellResultOut": "_cloudsearch_247_SpellResultOut",
        "UpdateSchemaRequestIn": "_cloudsearch_248_UpdateSchemaRequestIn",
        "UpdateSchemaRequestOut": "_cloudsearch_249_UpdateSchemaRequestOut",
        "EnterpriseTopazSidekickDocumentPerCategoryListDocumentPerCategoryListEntryIn": "_cloudsearch_250_EnterpriseTopazSidekickDocumentPerCategoryListDocumentPerCategoryListEntryIn",
        "EnterpriseTopazSidekickDocumentPerCategoryListDocumentPerCategoryListEntryOut": "_cloudsearch_251_EnterpriseTopazSidekickDocumentPerCategoryListDocumentPerCategoryListEntryOut",
        "EnterpriseTopazSidekickPersonProfileCardRelatedPeopleIn": "_cloudsearch_252_EnterpriseTopazSidekickPersonProfileCardRelatedPeopleIn",
        "EnterpriseTopazSidekickPersonProfileCardRelatedPeopleOut": "_cloudsearch_253_EnterpriseTopazSidekickPersonProfileCardRelatedPeopleOut",
        "GetCustomerIndexStatsResponseIn": "_cloudsearch_254_GetCustomerIndexStatsResponseIn",
        "GetCustomerIndexStatsResponseOut": "_cloudsearch_255_GetCustomerIndexStatsResponseOut",
        "PersonIn": "_cloudsearch_256_PersonIn",
        "PersonOut": "_cloudsearch_257_PersonOut",
        "FilterIn": "_cloudsearch_258_FilterIn",
        "FilterOut": "_cloudsearch_259_FilterOut",
        "RemoveActivityRequestIn": "_cloudsearch_260_RemoveActivityRequestIn",
        "RemoveActivityRequestOut": "_cloudsearch_261_RemoveActivityRequestOut",
        "GSuitePrincipalIn": "_cloudsearch_262_GSuitePrincipalIn",
        "GSuitePrincipalOut": "_cloudsearch_263_GSuitePrincipalOut",
        "EnterpriseTopazSidekickTimeSlotIn": "_cloudsearch_264_EnterpriseTopazSidekickTimeSlotIn",
        "EnterpriseTopazSidekickTimeSlotOut": "_cloudsearch_265_EnterpriseTopazSidekickTimeSlotOut",
        "NamedPropertyIn": "_cloudsearch_266_NamedPropertyIn",
        "NamedPropertyOut": "_cloudsearch_267_NamedPropertyOut",
        "CustomerSettingsIn": "_cloudsearch_268_CustomerSettingsIn",
        "CustomerSettingsOut": "_cloudsearch_269_CustomerSettingsOut",
        "SortOptionsIn": "_cloudsearch_270_SortOptionsIn",
        "SortOptionsOut": "_cloudsearch_271_SortOptionsOut",
        "ScoringConfigIn": "_cloudsearch_272_ScoringConfigIn",
        "ScoringConfigOut": "_cloudsearch_273_ScoringConfigOut",
        "PushItemIn": "_cloudsearch_274_PushItemIn",
        "PushItemOut": "_cloudsearch_275_PushItemOut",
        "ListOperationsResponseIn": "_cloudsearch_276_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_cloudsearch_277_ListOperationsResponseOut",
        "AclInfoIn": "_cloudsearch_278_AclInfoIn",
        "AclInfoOut": "_cloudsearch_279_AclInfoOut",
        "ContextAttributeIn": "_cloudsearch_280_ContextAttributeIn",
        "ContextAttributeOut": "_cloudsearch_281_ContextAttributeOut",
        "SchemaIn": "_cloudsearch_282_SchemaIn",
        "SchemaOut": "_cloudsearch_283_SchemaOut",
        "CustomerSearchApplicationStatsIn": "_cloudsearch_284_CustomerSearchApplicationStatsIn",
        "CustomerSearchApplicationStatsOut": "_cloudsearch_285_CustomerSearchApplicationStatsOut",
        "CustomerUserStatsIn": "_cloudsearch_286_CustomerUserStatsIn",
        "CustomerUserStatsOut": "_cloudsearch_287_CustomerUserStatsOut",
        "IntegerPropertyOptionsIn": "_cloudsearch_288_IntegerPropertyOptionsIn",
        "IntegerPropertyOptionsOut": "_cloudsearch_289_IntegerPropertyOptionsOut",
        "EnterpriseTopazSidekickGetAndKeepAheadCardProtoDeclinedEventsIn": "_cloudsearch_290_EnterpriseTopazSidekickGetAndKeepAheadCardProtoDeclinedEventsIn",
        "EnterpriseTopazSidekickGetAndKeepAheadCardProtoDeclinedEventsOut": "_cloudsearch_291_EnterpriseTopazSidekickGetAndKeepAheadCardProtoDeclinedEventsOut",
        "IntegerFacetingOptionsIn": "_cloudsearch_292_IntegerFacetingOptionsIn",
        "IntegerFacetingOptionsOut": "_cloudsearch_293_IntegerFacetingOptionsOut",
        "QuerySuggestionIn": "_cloudsearch_294_QuerySuggestionIn",
        "QuerySuggestionOut": "_cloudsearch_295_QuerySuggestionOut",
        "EnumPropertyOptionsIn": "_cloudsearch_296_EnumPropertyOptionsIn",
        "EnumPropertyOptionsOut": "_cloudsearch_297_EnumPropertyOptionsOut",
        "IndexItemRequestIn": "_cloudsearch_298_IndexItemRequestIn",
        "IndexItemRequestOut": "_cloudsearch_299_IndexItemRequestOut",
        "MediaIn": "_cloudsearch_300_MediaIn",
        "MediaOut": "_cloudsearch_301_MediaOut",
        "ObjectOptionsIn": "_cloudsearch_302_ObjectOptionsIn",
        "ObjectOptionsOut": "_cloudsearch_303_ObjectOptionsOut",
        "EnterpriseTopazSidekickGapIn": "_cloudsearch_304_EnterpriseTopazSidekickGapIn",
        "EnterpriseTopazSidekickGapOut": "_cloudsearch_305_EnterpriseTopazSidekickGapOut",
        "TimestampOperatorOptionsIn": "_cloudsearch_306_TimestampOperatorOptionsIn",
        "TimestampOperatorOptionsOut": "_cloudsearch_307_TimestampOperatorOptionsOut",
        "PersonCoreIn": "_cloudsearch_308_PersonCoreIn",
        "PersonCoreOut": "_cloudsearch_309_PersonCoreOut",
        "PrincipalIn": "_cloudsearch_310_PrincipalIn",
        "PrincipalOut": "_cloudsearch_311_PrincipalOut",
        "ContentIn": "_cloudsearch_312_ContentIn",
        "ContentOut": "_cloudsearch_313_ContentOut",
        "SourceResultCountIn": "_cloudsearch_314_SourceResultCountIn",
        "SourceResultCountOut": "_cloudsearch_315_SourceResultCountOut",
        "GoogleDocsResultInfoIn": "_cloudsearch_316_GoogleDocsResultInfoIn",
        "GoogleDocsResultInfoOut": "_cloudsearch_317_GoogleDocsResultInfoOut",
        "TypeInfoIn": "_cloudsearch_318_TypeInfoIn",
        "TypeInfoOut": "_cloudsearch_319_TypeInfoOut",
        "ObjectDisplayOptionsIn": "_cloudsearch_320_ObjectDisplayOptionsIn",
        "ObjectDisplayOptionsOut": "_cloudsearch_321_ObjectDisplayOptionsOut",
        "VideoInfoIn": "_cloudsearch_322_VideoInfoIn",
        "VideoInfoOut": "_cloudsearch_323_VideoInfoOut",
        "GetSearchApplicationQueryStatsResponseIn": "_cloudsearch_324_GetSearchApplicationQueryStatsResponseIn",
        "GetSearchApplicationQueryStatsResponseOut": "_cloudsearch_325_GetSearchApplicationQueryStatsResponseOut",
        "EnterpriseTopazSidekickAnswerSuggestedQueryAnswerCardIn": "_cloudsearch_326_EnterpriseTopazSidekickAnswerSuggestedQueryAnswerCardIn",
        "EnterpriseTopazSidekickAnswerSuggestedQueryAnswerCardOut": "_cloudsearch_327_EnterpriseTopazSidekickAnswerSuggestedQueryAnswerCardOut",
        "EnterpriseTopazSidekickShareMeetingDocsCardProtoIn": "_cloudsearch_328_EnterpriseTopazSidekickShareMeetingDocsCardProtoIn",
        "EnterpriseTopazSidekickShareMeetingDocsCardProtoOut": "_cloudsearch_329_EnterpriseTopazSidekickShareMeetingDocsCardProtoOut",
        "DriveMimeTypeRestrictIn": "_cloudsearch_330_DriveMimeTypeRestrictIn",
        "DriveMimeTypeRestrictOut": "_cloudsearch_331_DriveMimeTypeRestrictOut",
        "EnterpriseTopazSidekickCommonDocumentDriveDocumentMetadataIn": "_cloudsearch_332_EnterpriseTopazSidekickCommonDocumentDriveDocumentMetadataIn",
        "EnterpriseTopazSidekickCommonDocumentDriveDocumentMetadataOut": "_cloudsearch_333_EnterpriseTopazSidekickCommonDocumentDriveDocumentMetadataOut",
        "PushItemRequestIn": "_cloudsearch_334_PushItemRequestIn",
        "PushItemRequestOut": "_cloudsearch_335_PushItemRequestOut",
        "EnterpriseTopazSidekickAnswerAnswerListLabeledAnswerIn": "_cloudsearch_336_EnterpriseTopazSidekickAnswerAnswerListLabeledAnswerIn",
        "EnterpriseTopazSidekickAnswerAnswerListLabeledAnswerOut": "_cloudsearch_337_EnterpriseTopazSidekickAnswerAnswerListLabeledAnswerOut",
        "DriveFollowUpRestrictIn": "_cloudsearch_338_DriveFollowUpRestrictIn",
        "DriveFollowUpRestrictOut": "_cloudsearch_339_DriveFollowUpRestrictOut",
        "QuerySourceIn": "_cloudsearch_340_QuerySourceIn",
        "QuerySourceOut": "_cloudsearch_341_QuerySourceOut",
        "StructuredDataObjectIn": "_cloudsearch_342_StructuredDataObjectIn",
        "StructuredDataObjectOut": "_cloudsearch_343_StructuredDataObjectOut",
        "PhoneNumberIn": "_cloudsearch_344_PhoneNumberIn",
        "PhoneNumberOut": "_cloudsearch_345_PhoneNumberOut",
        "EnterpriseTopazSidekickFindMeetingTimeCardProtoIn": "_cloudsearch_346_EnterpriseTopazSidekickFindMeetingTimeCardProtoIn",
        "EnterpriseTopazSidekickFindMeetingTimeCardProtoOut": "_cloudsearch_347_EnterpriseTopazSidekickFindMeetingTimeCardProtoOut",
        "EnterpriseTopazSidekickAgendaEntryIn": "_cloudsearch_348_EnterpriseTopazSidekickAgendaEntryIn",
        "EnterpriseTopazSidekickAgendaEntryOut": "_cloudsearch_349_EnterpriseTopazSidekickAgendaEntryOut",
        "ItemAclIn": "_cloudsearch_350_ItemAclIn",
        "ItemAclOut": "_cloudsearch_351_ItemAclOut",
        "EnterpriseTopazSidekickPeopleDisambiguationCardIn": "_cloudsearch_352_EnterpriseTopazSidekickPeopleDisambiguationCardIn",
        "EnterpriseTopazSidekickPeopleDisambiguationCardOut": "_cloudsearch_353_EnterpriseTopazSidekickPeopleDisambiguationCardOut",
        "UnreserveItemsRequestIn": "_cloudsearch_354_UnreserveItemsRequestIn",
        "UnreserveItemsRequestOut": "_cloudsearch_355_UnreserveItemsRequestOut",
        "SuggestResponseIn": "_cloudsearch_356_SuggestResponseIn",
        "SuggestResponseOut": "_cloudsearch_357_SuggestResponseOut",
        "EnterpriseTopazSidekickPersonProfileCardIn": "_cloudsearch_358_EnterpriseTopazSidekickPersonProfileCardIn",
        "EnterpriseTopazSidekickPersonProfileCardOut": "_cloudsearch_359_EnterpriseTopazSidekickPersonProfileCardOut",
        "DeleteQueueItemsRequestIn": "_cloudsearch_360_DeleteQueueItemsRequestIn",
        "DeleteQueueItemsRequestOut": "_cloudsearch_361_DeleteQueueItemsRequestOut",
        "TextOperatorOptionsIn": "_cloudsearch_362_TextOperatorOptionsIn",
        "TextOperatorOptionsOut": "_cloudsearch_363_TextOperatorOptionsOut",
        "SourceIn": "_cloudsearch_364_SourceIn",
        "SourceOut": "_cloudsearch_365_SourceOut",
        "StartUploadItemRequestIn": "_cloudsearch_366_StartUploadItemRequestIn",
        "StartUploadItemRequestOut": "_cloudsearch_367_StartUploadItemRequestOut",
        "ListQuerySourcesResponseIn": "_cloudsearch_368_ListQuerySourcesResponseIn",
        "ListQuerySourcesResponseOut": "_cloudsearch_369_ListQuerySourcesResponseOut",
        "SearchApplicationQueryStatsIn": "_cloudsearch_370_SearchApplicationQueryStatsIn",
        "SearchApplicationQueryStatsOut": "_cloudsearch_371_SearchApplicationQueryStatsOut",
        "EnterpriseTopazSidekickAnswerAnswerListIn": "_cloudsearch_372_EnterpriseTopazSidekickAnswerAnswerListIn",
        "EnterpriseTopazSidekickAnswerAnswerListOut": "_cloudsearch_373_EnterpriseTopazSidekickAnswerAnswerListOut",
        "MetadataIn": "_cloudsearch_374_MetadataIn",
        "MetadataOut": "_cloudsearch_375_MetadataOut",
        "FilterOptionsIn": "_cloudsearch_376_FilterOptionsIn",
        "FilterOptionsOut": "_cloudsearch_377_FilterOptionsOut",
        "ThirdPartyGenericCardIn": "_cloudsearch_378_ThirdPartyGenericCardIn",
        "ThirdPartyGenericCardOut": "_cloudsearch_379_ThirdPartyGenericCardOut",
        "ItemIn": "_cloudsearch_380_ItemIn",
        "ItemOut": "_cloudsearch_381_ItemOut",
        "CustomerSessionStatsIn": "_cloudsearch_382_CustomerSessionStatsIn",
        "CustomerSessionStatsOut": "_cloudsearch_383_CustomerSessionStatsOut",
        "ResetSearchApplicationRequestIn": "_cloudsearch_384_ResetSearchApplicationRequestIn",
        "ResetSearchApplicationRequestOut": "_cloudsearch_385_ResetSearchApplicationRequestOut",
        "UserActivityIn": "_cloudsearch_386_UserActivityIn",
        "UserActivityOut": "_cloudsearch_387_UserActivityOut",
        "EnterpriseTopazSidekickCardMetadataIn": "_cloudsearch_388_EnterpriseTopazSidekickCardMetadataIn",
        "EnterpriseTopazSidekickCardMetadataOut": "_cloudsearch_389_EnterpriseTopazSidekickCardMetadataOut",
        "SearchApplicationUserStatsIn": "_cloudsearch_390_SearchApplicationUserStatsIn",
        "SearchApplicationUserStatsOut": "_cloudsearch_391_SearchApplicationUserStatsOut",
        "EnterpriseTopazSidekickGenericAnswerCardIn": "_cloudsearch_392_EnterpriseTopazSidekickGenericAnswerCardIn",
        "EnterpriseTopazSidekickGenericAnswerCardOut": "_cloudsearch_393_EnterpriseTopazSidekickGenericAnswerCardOut",
        "EnterpriseTopazSidekickMeetingNotesCardErrorIn": "_cloudsearch_394_EnterpriseTopazSidekickMeetingNotesCardErrorIn",
        "EnterpriseTopazSidekickMeetingNotesCardErrorOut": "_cloudsearch_395_EnterpriseTopazSidekickMeetingNotesCardErrorOut",
        "ActionIn": "_cloudsearch_396_ActionIn",
        "ActionOut": "_cloudsearch_397_ActionOut",
        "EnterpriseTopazSidekickAgendaGroupCardProtoContextIn": "_cloudsearch_398_EnterpriseTopazSidekickAgendaGroupCardProtoContextIn",
        "EnterpriseTopazSidekickAgendaGroupCardProtoContextOut": "_cloudsearch_399_EnterpriseTopazSidekickAgendaGroupCardProtoContextOut",
        "ItemStatusIn": "_cloudsearch_400_ItemStatusIn",
        "ItemStatusOut": "_cloudsearch_401_ItemStatusOut",
        "BooleanPropertyOptionsIn": "_cloudsearch_402_BooleanPropertyOptionsIn",
        "BooleanPropertyOptionsOut": "_cloudsearch_403_BooleanPropertyOptionsOut",
        "EnterpriseTopazSidekickDocumentPerCategoryListIn": "_cloudsearch_404_EnterpriseTopazSidekickDocumentPerCategoryListIn",
        "EnterpriseTopazSidekickDocumentPerCategoryListOut": "_cloudsearch_405_EnterpriseTopazSidekickDocumentPerCategoryListOut",
        "TextPropertyOptionsIn": "_cloudsearch_406_TextPropertyOptionsIn",
        "TextPropertyOptionsOut": "_cloudsearch_407_TextPropertyOptionsOut",
        "CustomerQueryStatsIn": "_cloudsearch_408_CustomerQueryStatsIn",
        "CustomerQueryStatsOut": "_cloudsearch_409_CustomerQueryStatsOut",
        "DriveLocationRestrictIn": "_cloudsearch_410_DriveLocationRestrictIn",
        "DriveLocationRestrictOut": "_cloudsearch_411_DriveLocationRestrictOut",
        "ShareScopeIn": "_cloudsearch_412_ShareScopeIn",
        "ShareScopeOut": "_cloudsearch_413_ShareScopeOut",
        "CustomerIndexStatsIn": "_cloudsearch_414_CustomerIndexStatsIn",
        "CustomerIndexStatsOut": "_cloudsearch_415_CustomerIndexStatsOut",
        "MetalineIn": "_cloudsearch_416_MetalineIn",
        "MetalineOut": "_cloudsearch_417_MetalineOut",
        "QueryItemIn": "_cloudsearch_418_QueryItemIn",
        "QueryItemOut": "_cloudsearch_419_QueryItemOut",
        "MapTileIn": "_cloudsearch_420_MapTileIn",
        "MapTileOut": "_cloudsearch_421_MapTileOut",
        "EnterpriseTopazFrontendTeamsPersonCorePhoneNumberIn": "_cloudsearch_422_EnterpriseTopazFrontendTeamsPersonCorePhoneNumberIn",
        "EnterpriseTopazFrontendTeamsPersonCorePhoneNumberOut": "_cloudsearch_423_EnterpriseTopazFrontendTeamsPersonCorePhoneNumberOut",
        "InitializeCustomerRequestIn": "_cloudsearch_424_InitializeCustomerRequestIn",
        "InitializeCustomerRequestOut": "_cloudsearch_425_InitializeCustomerRequestOut",
        "SafeHtmlProtoIn": "_cloudsearch_426_SafeHtmlProtoIn",
        "SafeHtmlProtoOut": "_cloudsearch_427_SafeHtmlProtoOut",
        "IntegerValuesIn": "_cloudsearch_428_IntegerValuesIn",
        "IntegerValuesOut": "_cloudsearch_429_IntegerValuesOut",
        "ListDataSourceResponseIn": "_cloudsearch_430_ListDataSourceResponseIn",
        "ListDataSourceResponseOut": "_cloudsearch_431_ListDataSourceResponseOut",
        "PollItemsRequestIn": "_cloudsearch_432_PollItemsRequestIn",
        "PollItemsRequestOut": "_cloudsearch_433_PollItemsRequestOut",
        "QueryInterpretationConfigIn": "_cloudsearch_434_QueryInterpretationConfigIn",
        "QueryInterpretationConfigOut": "_cloudsearch_435_QueryInterpretationConfigOut",
        "RestrictItemIn": "_cloudsearch_436_RestrictItemIn",
        "RestrictItemOut": "_cloudsearch_437_RestrictItemOut",
        "ProcessingErrorIn": "_cloudsearch_438_ProcessingErrorIn",
        "ProcessingErrorOut": "_cloudsearch_439_ProcessingErrorOut",
        "GetCustomerQueryStatsResponseIn": "_cloudsearch_440_GetCustomerQueryStatsResponseIn",
        "GetCustomerQueryStatsResponseOut": "_cloudsearch_441_GetCustomerQueryStatsResponseOut",
        "BooleanOperatorOptionsIn": "_cloudsearch_442_BooleanOperatorOptionsIn",
        "BooleanOperatorOptionsOut": "_cloudsearch_443_BooleanOperatorOptionsOut",
        "SuggestResultIn": "_cloudsearch_444_SuggestResultIn",
        "SuggestResultOut": "_cloudsearch_445_SuggestResultOut",
        "EnterpriseTopazSidekickPersonalizedDocsCardProtoIn": "_cloudsearch_446_EnterpriseTopazSidekickPersonalizedDocsCardProtoIn",
        "EnterpriseTopazSidekickPersonalizedDocsCardProtoOut": "_cloudsearch_447_EnterpriseTopazSidekickPersonalizedDocsCardProtoOut",
        "GetCustomerSessionStatsResponseIn": "_cloudsearch_448_GetCustomerSessionStatsResponseIn",
        "GetCustomerSessionStatsResponseOut": "_cloudsearch_449_GetCustomerSessionStatsResponseOut",
        "EnterpriseTopazSidekickCommonPersonBirthdayIn": "_cloudsearch_450_EnterpriseTopazSidekickCommonPersonBirthdayIn",
        "EnterpriseTopazSidekickCommonPersonBirthdayOut": "_cloudsearch_451_EnterpriseTopazSidekickCommonPersonBirthdayOut",
        "SearchItemsByViewUrlRequestIn": "_cloudsearch_452_SearchItemsByViewUrlRequestIn",
        "SearchItemsByViewUrlRequestOut": "_cloudsearch_453_SearchItemsByViewUrlRequestOut",
        "SourceScoringConfigIn": "_cloudsearch_454_SourceScoringConfigIn",
        "SourceScoringConfigOut": "_cloudsearch_455_SourceScoringConfigOut",
        "DoublePropertyOptionsIn": "_cloudsearch_456_DoublePropertyOptionsIn",
        "DoublePropertyOptionsOut": "_cloudsearch_457_DoublePropertyOptionsOut",
        "ListItemNamesForUnmappedIdentityResponseIn": "_cloudsearch_458_ListItemNamesForUnmappedIdentityResponseIn",
        "ListItemNamesForUnmappedIdentityResponseOut": "_cloudsearch_459_ListItemNamesForUnmappedIdentityResponseOut",
        "FacetResultIn": "_cloudsearch_460_FacetResultIn",
        "FacetResultOut": "_cloudsearch_461_FacetResultOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ResultDisplayLineIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["ResultDisplayFieldIn"]))}
    ).named(renames["ResultDisplayLineIn"])
    types["ResultDisplayLineOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["ResultDisplayFieldOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultDisplayLineOut"])
    types["DriveTimeSpanRestrictIn"] = t.struct({"type": t.string()}).named(
        renames["DriveTimeSpanRestrictIn"]
    )
    types["DriveTimeSpanRestrictOut"] = t.struct(
        {"type": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveTimeSpanRestrictOut"])
    types["QueryCountByStatusIn"] = t.struct(
        {"count": t.string(), "statusCode": t.integer().optional()}
    ).named(renames["QueryCountByStatusIn"])
    types["QueryCountByStatusOut"] = t.struct(
        {
            "count": t.string(),
            "statusCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryCountByStatusOut"])
    types["FacetOptionsIn"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "objectType": t.string().optional(),
            "numFacetBuckets": t.integer().optional(),
            "sourceName": t.string().optional(),
            "integerFacetingOptions": t.proxy(
                renames["IntegerFacetingOptionsIn"]
            ).optional(),
        }
    ).named(renames["FacetOptionsIn"])
    types["FacetOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "objectType": t.string().optional(),
            "numFacetBuckets": t.integer().optional(),
            "sourceName": t.string().optional(),
            "integerFacetingOptions": t.proxy(
                renames["IntegerFacetingOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FacetOptionsOut"])
    types["ErrorInfoIn"] = t.struct(
        {"errorMessages": t.array(t.proxy(renames["ErrorMessageIn"]))}
    ).named(renames["ErrorInfoIn"])
    types["ErrorInfoOut"] = t.struct(
        {
            "errorMessages": t.array(t.proxy(renames["ErrorMessageOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorInfoOut"])
    types["ResultDebugInfoIn"] = t.struct(
        {"formattedDebugInfo": t.string().optional()}
    ).named(renames["ResultDebugInfoIn"])
    types["ResultDebugInfoOut"] = t.struct(
        {
            "formattedDebugInfo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultDebugInfoOut"])
    types["SuggestRequestIn"] = t.struct(
        {
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionIn"])
            ).optional(),
            "query": t.string().optional(),
        }
    ).named(renames["SuggestRequestIn"])
    types["SuggestRequestOut"] = t.struct(
        {
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionOut"])
            ).optional(),
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestRequestOut"])
    types["GetSearchApplicationSessionStatsResponseIn"] = t.struct(
        {"stats": t.array(t.proxy(renames["SearchApplicationSessionStatsIn"]))}
    ).named(renames["GetSearchApplicationSessionStatsResponseIn"])
    types["GetSearchApplicationSessionStatsResponseOut"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["SearchApplicationSessionStatsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetSearchApplicationSessionStatsResponseOut"])
    types["QueryOperatorIn"] = t.struct(
        {
            "greaterThanOperatorName": t.string().optional(),
            "isFacetable": t.boolean().optional(),
            "type": t.string().optional(),
            "isSortable": t.boolean().optional(),
            "operatorName": t.string().optional(),
            "objectType": t.string().optional(),
            "enumValues": t.array(t.string()).optional(),
            "isSuggestable": t.boolean().optional(),
            "isReturnable": t.boolean().optional(),
            "lessThanOperatorName": t.string().optional(),
            "displayName": t.string().optional(),
            "isRepeatable": t.boolean().optional(),
        }
    ).named(renames["QueryOperatorIn"])
    types["QueryOperatorOut"] = t.struct(
        {
            "greaterThanOperatorName": t.string().optional(),
            "isFacetable": t.boolean().optional(),
            "type": t.string().optional(),
            "isSortable": t.boolean().optional(),
            "operatorName": t.string().optional(),
            "objectType": t.string().optional(),
            "enumValues": t.array(t.string()).optional(),
            "isSuggestable": t.boolean().optional(),
            "isReturnable": t.boolean().optional(),
            "lessThanOperatorName": t.string().optional(),
            "displayName": t.string().optional(),
            "isRepeatable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryOperatorOut"])
    types["EnterpriseTopazSidekickMeetingNotesCardProtoIn"] = t.struct(
        {
            "event": t.proxy(
                renames["EnterpriseTopazSidekickAgendaEntryIn"]
            ).optional(),
            "title": t.string().optional(),
            "fileId": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["EnterpriseTopazSidekickMeetingNotesCardProtoIn"])
    types["EnterpriseTopazSidekickMeetingNotesCardProtoOut"] = t.struct(
        {
            "event": t.proxy(
                renames["EnterpriseTopazSidekickAgendaEntryOut"]
            ).optional(),
            "title": t.string().optional(),
            "fileId": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickMeetingNotesCardProtoOut"])
    types["IntegerOperatorOptionsIn"] = t.struct(
        {
            "greaterThanOperatorName": t.string().optional(),
            "operatorName": t.string().optional(),
            "lessThanOperatorName": t.string().optional(),
        }
    ).named(renames["IntegerOperatorOptionsIn"])
    types["IntegerOperatorOptionsOut"] = t.struct(
        {
            "greaterThanOperatorName": t.string().optional(),
            "operatorName": t.string().optional(),
            "lessThanOperatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerOperatorOptionsOut"])
    types["RepositoryErrorIn"] = t.struct(
        {
            "httpStatusCode": t.integer().optional(),
            "errorMessage": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["RepositoryErrorIn"])
    types["RepositoryErrorOut"] = t.struct(
        {
            "httpStatusCode": t.integer().optional(),
            "errorMessage": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepositoryErrorOut"])
    types["GoogleDocsMetadataIn"] = t.struct(
        {
            "numViewers": t.integer().optional(),
            "documentType": t.string().optional(),
            "resultInfo": t.proxy(renames["GoogleDocsResultInfoIn"]).optional(),
            "numSubscribers": t.integer().optional(),
            "lastContentModifiedTimestamp": t.string().optional(),
            "aclInfo": t.proxy(renames["AclInfoIn"]).optional(),
            "typeInfo": t.proxy(renames["TypeInfoIn"]).optional(),
            "fileExtension": t.string().optional(),
        }
    ).named(renames["GoogleDocsMetadataIn"])
    types["GoogleDocsMetadataOut"] = t.struct(
        {
            "numViewers": t.integer().optional(),
            "documentType": t.string().optional(),
            "resultInfo": t.proxy(renames["GoogleDocsResultInfoOut"]).optional(),
            "numSubscribers": t.integer().optional(),
            "lastContentModifiedTimestamp": t.string().optional(),
            "aclInfo": t.proxy(renames["AclInfoOut"]).optional(),
            "typeInfo": t.proxy(renames["TypeInfoOut"]).optional(),
            "fileExtension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDocsMetadataOut"])
    types["ResultCountsIn"] = t.struct(
        {
            "sourceResultCounts": t.array(
                t.proxy(renames["SourceResultCountIn"])
            ).optional()
        }
    ).named(renames["ResultCountsIn"])
    types["ResultCountsOut"] = t.struct(
        {
            "sourceResultCounts": t.array(
                t.proxy(renames["SourceResultCountOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultCountsOut"])
    types["EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCardIn"] = t.struct(
        {
            "subject": t.proxy(
                renames["EnterpriseTopazSidekickCommonPersonIn"]
            ).optional(),
            "statusMessage": t.string().optional(),
            "relatedPeople": t.array(
                t.proxy(renames["EnterpriseTopazSidekickCommonPersonIn"])
            ).optional(),
            "relationType": t.string().optional(),
            "header": t.proxy(
                renames["EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeaderIn"]
            ).optional(),
            "responseStatus": t.string().optional(),
            "disambiguationInfo": t.proxy(
                renames["EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCardIn"])
    types["EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCardOut"] = t.struct(
        {
            "subject": t.proxy(
                renames["EnterpriseTopazSidekickCommonPersonOut"]
            ).optional(),
            "statusMessage": t.string().optional(),
            "relatedPeople": t.array(
                t.proxy(renames["EnterpriseTopazSidekickCommonPersonOut"])
            ).optional(),
            "relationType": t.string().optional(),
            "header": t.proxy(
                renames["EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeaderOut"]
            ).optional(),
            "responseStatus": t.string().optional(),
            "disambiguationInfo": t.proxy(
                renames["EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCardOut"])
    types["DebugOptionsIn"] = t.struct(
        {"enableDebugging": t.boolean().optional()}
    ).named(renames["DebugOptionsIn"])
    types["DebugOptionsOut"] = t.struct(
        {
            "enableDebugging": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DebugOptionsOut"])
    types["DisplayedPropertyIn"] = t.struct(
        {"propertyName": t.string().optional()}
    ).named(renames["DisplayedPropertyIn"])
    types["DisplayedPropertyOut"] = t.struct(
        {
            "propertyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisplayedPropertyOut"])
    types["EnterpriseTopazSidekickAgendaItemIn"] = t.struct(
        {
            "gapBefore": t.proxy(renames["EnterpriseTopazSidekickGapIn"]),
            "conflictedGroup": t.proxy(
                renames["EnterpriseTopazSidekickConflictingEventsCardProtoIn"]
            ),
            "meeting": t.proxy(renames["EnterpriseTopazSidekickAgendaEntryIn"]),
        }
    ).named(renames["EnterpriseTopazSidekickAgendaItemIn"])
    types["EnterpriseTopazSidekickAgendaItemOut"] = t.struct(
        {
            "gapBefore": t.proxy(renames["EnterpriseTopazSidekickGapOut"]),
            "conflictedGroup": t.proxy(
                renames["EnterpriseTopazSidekickConflictingEventsCardProtoOut"]
            ),
            "meeting": t.proxy(renames["EnterpriseTopazSidekickAgendaEntryOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickAgendaItemOut"])
    types["SafeUrlProtoIn"] = t.struct(
        {"privateDoNotAccessOrElseSafeUrlWrappedValue": t.string().optional()}
    ).named(renames["SafeUrlProtoIn"])
    types["SafeUrlProtoOut"] = t.struct(
        {
            "privateDoNotAccessOrElseSafeUrlWrappedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SafeUrlProtoOut"])
    types["FreshnessOptionsIn"] = t.struct(
        {
            "freshnessProperty": t.string().optional(),
            "freshnessDuration": t.string().optional(),
        }
    ).named(renames["FreshnessOptionsIn"])
    types["FreshnessOptionsOut"] = t.struct(
        {
            "freshnessProperty": t.string().optional(),
            "freshnessDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreshnessOptionsOut"])
    types["EnterpriseTopazSidekickScheduledMeetingIn"] = t.struct(
        {
            "meetingTime": t.proxy(
                renames["EnterpriseTopazSidekickTimeSlotIn"]
            ).optional(),
            "meetingLocation": t.string().optional(),
            "meetingTitle": t.string().optional(),
        }
    ).named(renames["EnterpriseTopazSidekickScheduledMeetingIn"])
    types["EnterpriseTopazSidekickScheduledMeetingOut"] = t.struct(
        {
            "meetingTime": t.proxy(
                renames["EnterpriseTopazSidekickTimeSlotOut"]
            ).optional(),
            "meetingLocation": t.string().optional(),
            "meetingTitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickScheduledMeetingOut"])
    types["CheckAccessResponseIn"] = t.struct(
        {"hasAccess": t.boolean().optional()}
    ).named(renames["CheckAccessResponseIn"])
    types["CheckAccessResponseOut"] = t.struct(
        {
            "hasAccess": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckAccessResponseOut"])
    types["AuditLoggingSettingsIn"] = t.struct(
        {
            "project": t.string().optional(),
            "logDataReadActions": t.boolean().optional(),
            "logDataWriteActions": t.boolean().optional(),
            "logAdminReadActions": t.boolean().optional(),
        }
    ).named(renames["AuditLoggingSettingsIn"])
    types["AuditLoggingSettingsOut"] = t.struct(
        {
            "project": t.string().optional(),
            "logDataReadActions": t.boolean().optional(),
            "logDataWriteActions": t.boolean().optional(),
            "logAdminReadActions": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLoggingSettingsOut"])
    types["RequestOptionsIn"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "timeZone": t.string().optional(),
            "languageCode": t.string().optional(),
            "searchApplicationId": t.string().optional(),
        }
    ).named(renames["RequestOptionsIn"])
    types["RequestOptionsOut"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "timeZone": t.string().optional(),
            "languageCode": t.string().optional(),
            "searchApplicationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOptionsOut"])
    types["PropertyDisplayOptionsIn"] = t.struct(
        {"displayLabel": t.string().optional()}
    ).named(renames["PropertyDisplayOptionsIn"])
    types["PropertyDisplayOptionsOut"] = t.struct(
        {
            "displayLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyDisplayOptionsOut"])
    types["SourceConfigIn"] = t.struct(
        {
            "source": t.proxy(renames["SourceIn"]).optional(),
            "crowdingConfig": t.proxy(renames["SourceCrowdingConfigIn"]).optional(),
            "scoringConfig": t.proxy(renames["SourceScoringConfigIn"]).optional(),
        }
    ).named(renames["SourceConfigIn"])
    types["SourceConfigOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "crowdingConfig": t.proxy(renames["SourceCrowdingConfigOut"]).optional(),
            "scoringConfig": t.proxy(renames["SourceScoringConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceConfigOut"])
    types["EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoIn"] = t.struct(
        {
            "name": t.string().optional(),
            "disambiguation": t.array(
                t.proxy(
                    renames[
                        "EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoDisambiguationPersonIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoIn"])
    types["EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoOut"] = t.struct(
        {
            "name": t.string().optional(),
            "disambiguation": t.array(
                t.proxy(
                    renames[
                        "EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoDisambiguationPersonOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoOut"])
    types["InteractionIn"] = t.struct(
        {
            "principal": t.proxy(renames["PrincipalIn"]).optional(),
            "type": t.string(),
            "interactionTime": t.string().optional(),
        }
    ).named(renames["InteractionIn"])
    types["InteractionOut"] = t.struct(
        {
            "principal": t.proxy(renames["PrincipalOut"]).optional(),
            "type": t.string(),
            "interactionTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InteractionOut"])
    types["GetDataSourceIndexStatsResponseIn"] = t.struct(
        {
            "averageIndexedItemCount": t.string().optional(),
            "stats": t.array(t.proxy(renames["DataSourceIndexStatsIn"])).optional(),
        }
    ).named(renames["GetDataSourceIndexStatsResponseIn"])
    types["GetDataSourceIndexStatsResponseOut"] = t.struct(
        {
            "averageIndexedItemCount": t.string().optional(),
            "stats": t.array(t.proxy(renames["DataSourceIndexStatsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetDataSourceIndexStatsResponseOut"])
    types["DateValuesIn"] = t.struct(
        {"values": t.array(t.proxy(renames["DateIn"]))}
    ).named(renames["DateValuesIn"])
    types["DateValuesOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["DateOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateValuesOut"])
    types["ItemStructuredDataIn"] = t.struct(
        {
            "hash": t.string().optional(),
            "object": t.proxy(renames["StructuredDataObjectIn"]).optional(),
        }
    ).named(renames["ItemStructuredDataIn"])
    types["ItemStructuredDataOut"] = t.struct(
        {
            "hash": t.string().optional(),
            "object": t.proxy(renames["StructuredDataObjectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemStructuredDataOut"])
    types["SourceCrowdingConfigIn"] = t.struct(
        {"numSuggestions": t.integer().optional(), "numResults": t.integer().optional()}
    ).named(renames["SourceCrowdingConfigIn"])
    types["SourceCrowdingConfigOut"] = t.struct(
        {
            "numSuggestions": t.integer().optional(),
            "numResults": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceCrowdingConfigOut"])
    types["ItemContentIn"] = t.struct(
        {
            "contentDataRef": t.proxy(renames["UploadItemRefIn"]).optional(),
            "contentFormat": t.string(),
            "hash": t.string().optional(),
            "inlineContent": t.string().optional(),
        }
    ).named(renames["ItemContentIn"])
    types["ItemContentOut"] = t.struct(
        {
            "contentDataRef": t.proxy(renames["UploadItemRefOut"]).optional(),
            "contentFormat": t.string(),
            "hash": t.string().optional(),
            "inlineContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemContentOut"])
    types["VPCSettingsIn"] = t.struct({"project": t.string().optional()}).named(
        renames["VPCSettingsIn"]
    )
    types["VPCSettingsOut"] = t.struct(
        {
            "project": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VPCSettingsOut"])
    types["UploadItemRefIn"] = t.struct({"name": t.string().optional()}).named(
        renames["UploadItemRefIn"]
    )
    types["UploadItemRefOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadItemRefOut"])
    types["RemoveActivityResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemoveActivityResponseIn"]
    )
    types["RemoveActivityResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveActivityResponseOut"])
    types["PeopleSuggestionIn"] = t.struct(
        {"person": t.proxy(renames["PersonIn"]).optional()}
    ).named(renames["PeopleSuggestionIn"])
    types["PeopleSuggestionOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PeopleSuggestionOut"])
    types["ResultDisplayMetadataIn"] = t.struct(
        {
            "metalines": t.array(t.proxy(renames["ResultDisplayLineIn"])).optional(),
            "objectTypeLabel": t.string().optional(),
        }
    ).named(renames["ResultDisplayMetadataIn"])
    types["ResultDisplayMetadataOut"] = t.struct(
        {
            "metalines": t.array(t.proxy(renames["ResultDisplayLineOut"])).optional(),
            "objectTypeLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultDisplayMetadataOut"])
    types["EnterpriseTopazFrontendTeamsLinkIn"] = t.struct(
        {"url": t.proxy(renames["SafeUrlProtoIn"]), "type": t.string().optional()}
    ).named(renames["EnterpriseTopazFrontendTeamsLinkIn"])
    types["EnterpriseTopazFrontendTeamsLinkOut"] = t.struct(
        {
            "url": t.proxy(renames["SafeUrlProtoOut"]),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazFrontendTeamsLinkOut"])
    types["DataSourceIndexStatsIn"] = t.struct(
        {
            "date": t.proxy(renames["DateIn"]).optional(),
            "itemCountByStatus": t.array(
                t.proxy(renames["ItemCountByStatusIn"])
            ).optional(),
        }
    ).named(renames["DataSourceIndexStatsIn"])
    types["DataSourceIndexStatsOut"] = t.struct(
        {
            "date": t.proxy(renames["DateOut"]).optional(),
            "itemCountByStatus": t.array(
                t.proxy(renames["ItemCountByStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceIndexStatsOut"])
    types["ItemCountByStatusIn"] = t.struct(
        {
            "statusCode": t.string().optional(),
            "count": t.string().optional(),
            "indexedItemsCount": t.string().optional(),
        }
    ).named(renames["ItemCountByStatusIn"])
    types["ItemCountByStatusOut"] = t.struct(
        {
            "statusCode": t.string().optional(),
            "count": t.string().optional(),
            "indexedItemsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemCountByStatusOut"])
    types["ResultDisplayFieldIn"] = t.struct(
        {
            "property": t.proxy(renames["NamedPropertyIn"]).optional(),
            "label": t.string().optional(),
            "operatorName": t.string().optional(),
        }
    ).named(renames["ResultDisplayFieldIn"])
    types["ResultDisplayFieldOut"] = t.struct(
        {
            "property": t.proxy(renames["NamedPropertyOut"]).optional(),
            "label": t.string().optional(),
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultDisplayFieldOut"])
    types["EnterpriseTopazSidekickPeopleAnswerPersonAnswerCardIn"] = t.struct(
        {
            "answerText": t.proxy(
                renames["EnterpriseTopazSidekickAnswerAnswerListIn"]
            ).optional(),
            "answer": t.array(t.proxy(renames["SafeHtmlProtoIn"])).optional(),
            "responseStatus": t.string().optional(),
            "header": t.proxy(
                renames["EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeaderIn"]
            ).optional(),
            "disambiguationInfo": t.proxy(
                renames["EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoIn"]
            ).optional(),
            "statusMessage": t.string().optional(),
            "subject": t.proxy(
                renames["EnterpriseTopazSidekickCommonPersonIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickPeopleAnswerPersonAnswerCardIn"])
    types["EnterpriseTopazSidekickPeopleAnswerPersonAnswerCardOut"] = t.struct(
        {
            "answerText": t.proxy(
                renames["EnterpriseTopazSidekickAnswerAnswerListOut"]
            ).optional(),
            "answer": t.array(t.proxy(renames["SafeHtmlProtoOut"])).optional(),
            "responseStatus": t.string().optional(),
            "header": t.proxy(
                renames["EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeaderOut"]
            ).optional(),
            "disambiguationInfo": t.proxy(
                renames["EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoOut"]
            ).optional(),
            "statusMessage": t.string().optional(),
            "subject": t.proxy(
                renames["EnterpriseTopazSidekickCommonPersonOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickPeopleAnswerPersonAnswerCardOut"])
    types["GetCustomerSearchApplicationStatsResponseIn"] = t.struct(
        {
            "averageSearchApplicationCount": t.string().optional(),
            "stats": t.array(
                t.proxy(renames["CustomerSearchApplicationStatsIn"])
            ).optional(),
        }
    ).named(renames["GetCustomerSearchApplicationStatsResponseIn"])
    types["GetCustomerSearchApplicationStatsResponseOut"] = t.struct(
        {
            "averageSearchApplicationCount": t.string().optional(),
            "stats": t.array(
                t.proxy(renames["CustomerSearchApplicationStatsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetCustomerSearchApplicationStatsResponseOut"])
    types["QueryInterpretationIn"] = t.struct(
        {
            "interpretedQuery": t.string().optional(),
            "reason": t.string().optional(),
            "interpretationType": t.string(),
        }
    ).named(renames["QueryInterpretationIn"])
    types["QueryInterpretationOut"] = t.struct(
        {
            "interpretedQuery": t.string().optional(),
            "reason": t.string().optional(),
            "interpretationType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryInterpretationOut"])
    types["EnumValuesIn"] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames["EnumValuesIn"]
    )
    types["EnumValuesOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumValuesOut"])
    types["EnterpriseTopazSidekickCommonDocumentIn"] = t.struct(
        {
            "accessType": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "reason": t.string().optional(),
            "driveDocumentMetadata": t.proxy(
                renames["EnterpriseTopazSidekickCommonDocumentDriveDocumentMetadataIn"]
            ).optional(),
            "documentId": t.string().optional(),
            "justification": t.proxy(
                renames["EnterpriseTopazSidekickCommonDocumentJustificationIn"]
            ).optional(),
            "genericUrl": t.string().optional(),
            "provenance": t.string().optional(),
            "mimeType": t.string().optional(),
            "debugInfo": t.proxy(
                renames["EnterpriseTopazSidekickCommonDebugInfoIn"]
            ).optional(),
            "url": t.string().optional(),
            "snippet": t.string().optional(),
            "type": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["EnterpriseTopazSidekickCommonDocumentIn"])
    types["EnterpriseTopazSidekickCommonDocumentOut"] = t.struct(
        {
            "accessType": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "reason": t.string().optional(),
            "driveDocumentMetadata": t.proxy(
                renames["EnterpriseTopazSidekickCommonDocumentDriveDocumentMetadataOut"]
            ).optional(),
            "documentId": t.string().optional(),
            "justification": t.proxy(
                renames["EnterpriseTopazSidekickCommonDocumentJustificationOut"]
            ).optional(),
            "genericUrl": t.string().optional(),
            "provenance": t.string().optional(),
            "mimeType": t.string().optional(),
            "debugInfo": t.proxy(
                renames["EnterpriseTopazSidekickCommonDebugInfoOut"]
            ).optional(),
            "url": t.string().optional(),
            "snippet": t.string().optional(),
            "type": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickCommonDocumentOut"])
    types["EnterpriseTopazSidekickConflictingEventsCardProtoIn"] = t.struct(
        {
            "conflictingEvent": t.array(
                t.proxy(renames["EnterpriseTopazSidekickAgendaEntryIn"])
            ).optional(),
            "mainEvent": t.proxy(
                renames["EnterpriseTopazSidekickAgendaEntryIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickConflictingEventsCardProtoIn"])
    types["EnterpriseTopazSidekickConflictingEventsCardProtoOut"] = t.struct(
        {
            "conflictingEvent": t.array(
                t.proxy(renames["EnterpriseTopazSidekickAgendaEntryOut"])
            ).optional(),
            "mainEvent": t.proxy(
                renames["EnterpriseTopazSidekickAgendaEntryOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickConflictingEventsCardProtoOut"])
    types["ObjectPropertyOptionsIn"] = t.struct(
        {
            "subobjectProperties": t.array(
                t.proxy(renames["PropertyDefinitionIn"])
            ).optional()
        }
    ).named(renames["ObjectPropertyOptionsIn"])
    types["ObjectPropertyOptionsOut"] = t.struct(
        {
            "subobjectProperties": t.array(
                t.proxy(renames["PropertyDefinitionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectPropertyOptionsOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ObjectDefinitionIn"] = t.struct(
        {
            "propertyDefinitions": t.array(
                t.proxy(renames["PropertyDefinitionIn"])
            ).optional(),
            "name": t.string().optional(),
            "options": t.proxy(renames["ObjectOptionsIn"]).optional(),
        }
    ).named(renames["ObjectDefinitionIn"])
    types["ObjectDefinitionOut"] = t.struct(
        {
            "propertyDefinitions": t.array(
                t.proxy(renames["PropertyDefinitionOut"])
            ).optional(),
            "name": t.string().optional(),
            "options": t.proxy(renames["ObjectOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectDefinitionOut"])
    types["IdIn"] = t.struct(
        {
            "localId": t.string().optional(),
            "nameSpace": t.integer().optional(),
            "creatorUserId": t.string().optional(),
        }
    ).named(renames["IdIn"])
    types["IdOut"] = t.struct(
        {
            "localId": t.string().optional(),
            "nameSpace": t.integer().optional(),
            "creatorUserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdOut"])
    types["EnterpriseTopazSidekickPersonIn"] = t.struct(
        {
            "isGroup": t.boolean().optional(),
            "email": t.string().optional(),
            "gaiaId": t.string().optional(),
            "obfuscatedGaiaId": t.string().optional(),
            "attendingStatus": t.string().optional(),
            "affinityLevel": t.string().optional(),
            "photoUrl": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["EnterpriseTopazSidekickPersonIn"])
    types["EnterpriseTopazSidekickPersonOut"] = t.struct(
        {
            "isGroup": t.boolean().optional(),
            "email": t.string().optional(),
            "gaiaId": t.string().optional(),
            "obfuscatedGaiaId": t.string().optional(),
            "attendingStatus": t.string().optional(),
            "affinityLevel": t.string().optional(),
            "photoUrl": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickPersonOut"])
    types["UpdateDataSourceRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "source": t.proxy(renames["DataSourceIn"]),
        }
    ).named(renames["UpdateDataSourceRequestIn"])
    types["UpdateDataSourceRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "source": t.proxy(renames["DataSourceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDataSourceRequestOut"])
    types["EnumOperatorOptionsIn"] = t.struct(
        {"operatorName": t.string().optional()}
    ).named(renames["EnumOperatorOptionsIn"])
    types["EnumOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOperatorOptionsOut"])
    types["GetSearchApplicationUserStatsResponseIn"] = t.struct(
        {"stats": t.array(t.proxy(renames["SearchApplicationUserStatsIn"]))}
    ).named(renames["GetSearchApplicationUserStatsResponseIn"])
    types["GetSearchApplicationUserStatsResponseOut"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["SearchApplicationUserStatsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetSearchApplicationUserStatsResponseOut"])
    types["SearchQualityMetadataIn"] = t.struct(
        {"quality": t.number().optional()}
    ).named(renames["SearchQualityMetadataIn"])
    types["SearchQualityMetadataOut"] = t.struct(
        {
            "quality": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchQualityMetadataOut"])
    types["TimestampValuesIn"] = t.struct({"values": t.array(t.string())}).named(
        renames["TimestampValuesIn"]
    )
    types["TimestampValuesOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimestampValuesOut"])
    types["HtmlPropertyOptionsIn"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["HtmlOperatorOptionsIn"]).optional(),
            "retrievalImportance": t.proxy(renames["RetrievalImportanceIn"]).optional(),
        }
    ).named(renames["HtmlPropertyOptionsIn"])
    types["HtmlPropertyOptionsOut"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["HtmlOperatorOptionsOut"]).optional(),
            "retrievalImportance": t.proxy(
                renames["RetrievalImportanceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HtmlPropertyOptionsOut"])
    types["PeoplePromotionCardIn"] = t.struct(
        {"people": t.array(t.proxy(renames["PersonCoreIn"]))}
    ).named(renames["PeoplePromotionCardIn"])
    types["PeoplePromotionCardOut"] = t.struct(
        {
            "people": t.array(t.proxy(renames["PersonCoreOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PeoplePromotionCardOut"])
    types["ItemMetadataIn"] = t.struct(
        {
            "objectType": t.string().optional(),
            "hash": t.string().optional(),
            "keywords": t.array(t.string()).optional(),
            "searchQualityMetadata": t.proxy(
                renames["SearchQualityMetadataIn"]
            ).optional(),
            "title": t.string().optional(),
            "sourceRepositoryUrl": t.string().optional(),
            "interactions": t.array(t.proxy(renames["InteractionIn"])).optional(),
            "contentLanguage": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "mimeType": t.string().optional(),
            "contextAttributes": t.array(
                t.proxy(renames["ContextAttributeIn"])
            ).optional(),
            "containerName": t.string().optional(),
        }
    ).named(renames["ItemMetadataIn"])
    types["ItemMetadataOut"] = t.struct(
        {
            "objectType": t.string().optional(),
            "hash": t.string().optional(),
            "keywords": t.array(t.string()).optional(),
            "searchQualityMetadata": t.proxy(
                renames["SearchQualityMetadataOut"]
            ).optional(),
            "title": t.string().optional(),
            "sourceRepositoryUrl": t.string().optional(),
            "interactions": t.array(t.proxy(renames["InteractionOut"])).optional(),
            "contentLanguage": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "mimeType": t.string().optional(),
            "contextAttributes": t.array(
                t.proxy(renames["ContextAttributeOut"])
            ).optional(),
            "containerName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemMetadataOut"])
    types["RetrievalImportanceIn"] = t.struct(
        {"importance": t.string().optional()}
    ).named(renames["RetrievalImportanceIn"])
    types["RetrievalImportanceOut"] = t.struct(
        {
            "importance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetrievalImportanceOut"])
    types["EnterpriseTopazSidekickNlpMetadataIn"] = t.struct(
        {"confidence": t.number().optional()}
    ).named(renames["EnterpriseTopazSidekickNlpMetadataIn"])
    types["EnterpriseTopazSidekickNlpMetadataOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickNlpMetadataOut"])
    types["PhotoIn"] = t.struct({"url": t.string().optional()}).named(
        renames["PhotoIn"]
    )
    types["PhotoOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoOut"])
    types["DataSourceRestrictionIn"] = t.struct(
        {
            "filterOptions": t.array(t.proxy(renames["FilterOptionsIn"])).optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
        }
    ).named(renames["DataSourceRestrictionIn"])
    types["DataSourceRestrictionOut"] = t.struct(
        {
            "filterOptions": t.array(t.proxy(renames["FilterOptionsOut"])).optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceRestrictionOut"])
    types["EnterpriseTopazSidekickAnswerSuggestedQueryCategoryIn"] = t.struct(
        {
            "category": t.string().optional(),
            "query": t.array(t.string()).optional(),
            "isEnabled": t.boolean().optional(),
        }
    ).named(renames["EnterpriseTopazSidekickAnswerSuggestedQueryCategoryIn"])
    types["EnterpriseTopazSidekickAnswerSuggestedQueryCategoryOut"] = t.struct(
        {
            "category": t.string().optional(),
            "query": t.array(t.string()).optional(),
            "isEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickAnswerSuggestedQueryCategoryOut"])
    types["EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeaderIn"] = t.struct(
        {"title": t.string().optional()}
    ).named(renames["EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeaderIn"])
    types["EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeaderOut"] = t.struct(
        {
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickPeopleAnswerPeopleAnswerCardHeaderOut"])
    types["SearchResultIn"] = t.struct(
        {
            "url": t.string().optional(),
            "debugInfo": t.proxy(renames["ResultDebugInfoIn"]).optional(),
            "title": t.string().optional(),
            "snippet": t.proxy(renames["SnippetIn"]).optional(),
            "metadata": t.proxy(renames["MetadataIn"]).optional(),
            "clusteredResults": t.array(t.proxy(renames["SearchResultIn"])).optional(),
        }
    ).named(renames["SearchResultIn"])
    types["SearchResultOut"] = t.struct(
        {
            "url": t.string().optional(),
            "debugInfo": t.proxy(renames["ResultDebugInfoOut"]).optional(),
            "title": t.string().optional(),
            "snippet": t.proxy(renames["SnippetOut"]).optional(),
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "clusteredResults": t.array(t.proxy(renames["SearchResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResultOut"])
    types["EnterpriseTopazSidekickRankingParamsIn"] = t.struct(
        {
            "startTimeMs": t.string().optional(),
            "spanMs": t.string().optional(),
            "endTimeMs": t.string().optional(),
            "type": t.string().optional(),
            "priority": t.string().optional(),
            "score": t.number().optional(),
        }
    ).named(renames["EnterpriseTopazSidekickRankingParamsIn"])
    types["EnterpriseTopazSidekickRankingParamsOut"] = t.struct(
        {
            "startTimeMs": t.string().optional(),
            "spanMs": t.string().optional(),
            "endTimeMs": t.string().optional(),
            "type": t.string().optional(),
            "priority": t.string().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickRankingParamsOut"])
    types[
        "EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoDisambiguationPersonIn"
    ] = t.struct(
        {
            "person": t.proxy(
                renames["EnterpriseTopazSidekickCommonPersonIn"]
            ).optional(),
            "query": t.string().optional(),
        }
    ).named(
        renames[
            "EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoDisambiguationPersonIn"
        ]
    )
    types[
        "EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoDisambiguationPersonOut"
    ] = t.struct(
        {
            "person": t.proxy(
                renames["EnterpriseTopazSidekickCommonPersonOut"]
            ).optional(),
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "EnterpriseTopazSidekickPeopleAnswerDisambiguationInfoDisambiguationPersonOut"
        ]
    )
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
    types["NameIn"] = t.struct({"displayName": t.string().optional()}).named(
        renames["NameIn"]
    )
    types["NameOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NameOut"])
    types["ObjectValuesIn"] = t.struct(
        {"values": t.array(t.proxy(renames["StructuredDataObjectIn"]))}
    ).named(renames["ObjectValuesIn"])
    types["ObjectValuesOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["StructuredDataObjectOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectValuesOut"])
    types["EmailAddressIn"] = t.struct(
        {
            "emailUrl": t.string().optional(),
            "primary": t.boolean().optional(),
            "customType": t.string().optional(),
            "type": t.string().optional(),
            "emailAddress": t.string().optional(),
        }
    ).named(renames["EmailAddressIn"])
    types["EmailAddressOut"] = t.struct(
        {
            "emailUrl": t.string().optional(),
            "primary": t.boolean().optional(),
            "customType": t.string().optional(),
            "type": t.string().optional(),
            "emailAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmailAddressOut"])
    types["ListSearchApplicationsResponseIn"] = t.struct(
        {
            "searchApplications": t.array(t.proxy(renames["SearchApplicationIn"])),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSearchApplicationsResponseIn"])
    types["ListSearchApplicationsResponseOut"] = t.struct(
        {
            "searchApplications": t.array(t.proxy(renames["SearchApplicationOut"])),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSearchApplicationsResponseOut"])
    types["SearchResponseIn"] = t.struct(
        {
            "resultCountExact": t.string().optional(),
            "spellResults": t.array(t.proxy(renames["SpellResultIn"])).optional(),
            "queryInterpretation": t.proxy(renames["QueryInterpretationIn"]).optional(),
            "errorInfo": t.proxy(renames["ErrorInfoIn"]).optional(),
            "results": t.array(t.proxy(renames["SearchResultIn"])).optional(),
            "debugInfo": t.proxy(renames["ResponseDebugInfoIn"]).optional(),
            "resultCountEstimate": t.string().optional(),
            "resultCounts": t.proxy(renames["ResultCountsIn"]).optional(),
            "hasMoreResults": t.boolean().optional(),
            "structuredResults": t.array(
                t.proxy(renames["StructuredResultIn"])
            ).optional(),
            "facetResults": t.array(t.proxy(renames["FacetResultIn"])).optional(),
        }
    ).named(renames["SearchResponseIn"])
    types["SearchResponseOut"] = t.struct(
        {
            "resultCountExact": t.string().optional(),
            "spellResults": t.array(t.proxy(renames["SpellResultOut"])).optional(),
            "queryInterpretation": t.proxy(
                renames["QueryInterpretationOut"]
            ).optional(),
            "errorInfo": t.proxy(renames["ErrorInfoOut"]).optional(),
            "results": t.array(t.proxy(renames["SearchResultOut"])).optional(),
            "debugInfo": t.proxy(renames["ResponseDebugInfoOut"]).optional(),
            "resultCountEstimate": t.string().optional(),
            "resultCounts": t.proxy(renames["ResultCountsOut"]).optional(),
            "hasMoreResults": t.boolean().optional(),
            "structuredResults": t.array(
                t.proxy(renames["StructuredResultOut"])
            ).optional(),
            "facetResults": t.array(t.proxy(renames["FacetResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResponseOut"])
    types["TextValuesIn"] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames["TextValuesIn"]
    )
    types["TextValuesOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextValuesOut"])
    types["SearchApplicationIn"] = t.struct(
        {
            "enableAuditLog": t.boolean().optional(),
            "defaultSortOptions": t.proxy(renames["SortOptionsIn"]).optional(),
            "defaultFacetOptions": t.array(
                t.proxy(renames["FacetOptionsIn"])
            ).optional(),
            "displayName": t.string().optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionIn"])
            ).optional(),
            "name": t.string().optional(),
            "scoringConfig": t.proxy(renames["ScoringConfigIn"]).optional(),
            "sourceConfig": t.array(t.proxy(renames["SourceConfigIn"])).optional(),
            "returnResultThumbnailUrls": t.boolean().optional(),
            "queryInterpretationConfig": t.proxy(
                renames["QueryInterpretationConfigIn"]
            ).optional(),
        }
    ).named(renames["SearchApplicationIn"])
    types["SearchApplicationOut"] = t.struct(
        {
            "operationIds": t.array(t.string()).optional(),
            "enableAuditLog": t.boolean().optional(),
            "defaultSortOptions": t.proxy(renames["SortOptionsOut"]).optional(),
            "defaultFacetOptions": t.array(
                t.proxy(renames["FacetOptionsOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionOut"])
            ).optional(),
            "name": t.string().optional(),
            "scoringConfig": t.proxy(renames["ScoringConfigOut"]).optional(),
            "sourceConfig": t.array(t.proxy(renames["SourceConfigOut"])).optional(),
            "returnResultThumbnailUrls": t.boolean().optional(),
            "queryInterpretationConfig": t.proxy(
                renames["QueryInterpretationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchApplicationOut"])
    types["QueryInterpretationOptionsIn"] = t.struct(
        {
            "enableVerbatimMode": t.boolean().optional(),
            "disableNlInterpretation": t.boolean().optional(),
            "disableSupplementalResults": t.boolean().optional(),
        }
    ).named(renames["QueryInterpretationOptionsIn"])
    types["QueryInterpretationOptionsOut"] = t.struct(
        {
            "enableVerbatimMode": t.boolean().optional(),
            "disableNlInterpretation": t.boolean().optional(),
            "disableSupplementalResults": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryInterpretationOptionsOut"])
    types["DoubleValuesIn"] = t.struct({"values": t.array(t.number())}).named(
        renames["DoubleValuesIn"]
    )
    types["DoubleValuesOut"] = t.struct(
        {
            "values": t.array(t.number()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleValuesOut"])
    types["DateOperatorOptionsIn"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
            "lessThanOperatorName": t.string().optional(),
        }
    ).named(renames["DateOperatorOptionsIn"])
    types["DateOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
            "lessThanOperatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOperatorOptionsOut"])
    types["SearchItemsByViewUrlResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["ItemIn"])),
        }
    ).named(renames["SearchItemsByViewUrlResponseIn"])
    types["SearchItemsByViewUrlResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["ItemOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchItemsByViewUrlResponseOut"])
    types["ResponseDebugInfoIn"] = t.struct(
        {"formattedDebugInfo": t.string().optional()}
    ).named(renames["ResponseDebugInfoIn"])
    types["ResponseDebugInfoOut"] = t.struct(
        {
            "formattedDebugInfo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseDebugInfoOut"])
    types["EnterpriseTopazSidekickCommonDebugInfoIn"] = t.struct(
        {"message": t.string().optional()}
    ).named(renames["EnterpriseTopazSidekickCommonDebugInfoIn"])
    types["EnterpriseTopazSidekickCommonDebugInfoOut"] = t.struct(
        {
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickCommonDebugInfoOut"])
    types["FieldViolationIn"] = t.struct(
        {"description": t.string().optional(), "field": t.string().optional()}
    ).named(renames["FieldViolationIn"])
    types["FieldViolationOut"] = t.struct(
        {
            "description": t.string().optional(),
            "field": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldViolationOut"])
    types["SnippetIn"] = t.struct(
        {
            "snippet": t.string().optional(),
            "matchRanges": t.array(t.proxy(renames["MatchRangeIn"])).optional(),
        }
    ).named(renames["SnippetIn"])
    types["SnippetOut"] = t.struct(
        {
            "snippet": t.string().optional(),
            "matchRanges": t.array(t.proxy(renames["MatchRangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnippetOut"])
    types["EnterpriseTopazSidekickCommonPersonIn"] = t.struct(
        {
            "gaiaId": t.string().optional(),
            "streetAddress": t.string().optional(),
            "obfuscatedId": t.string().optional(),
            "deskLocation": t.string().optional(),
            "deskPhone": t.string().optional(),
            "fullAddress": t.string().optional(),
            "givenName": t.string().optional(),
            "photoUrl": t.string().optional(),
            "manager": t.proxy(
                renames["EnterpriseTopazSidekickCommonPersonIn"]
            ).optional(),
            "jobTitle": t.string().optional(),
            "birthday": t.proxy(
                renames["EnterpriseTopazSidekickCommonPersonBirthdayIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "department": t.string().optional(),
            "email": t.string().optional(),
            "cellPhone": t.string().optional(),
            "familyName": t.string().optional(),
        }
    ).named(renames["EnterpriseTopazSidekickCommonPersonIn"])
    types["EnterpriseTopazSidekickCommonPersonOut"] = t.struct(
        {
            "gaiaId": t.string().optional(),
            "streetAddress": t.string().optional(),
            "obfuscatedId": t.string().optional(),
            "deskLocation": t.string().optional(),
            "deskPhone": t.string().optional(),
            "fullAddress": t.string().optional(),
            "givenName": t.string().optional(),
            "photoUrl": t.string().optional(),
            "manager": t.proxy(
                renames["EnterpriseTopazSidekickCommonPersonOut"]
            ).optional(),
            "jobTitle": t.string().optional(),
            "birthday": t.proxy(
                renames["EnterpriseTopazSidekickCommonPersonBirthdayOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "department": t.string().optional(),
            "email": t.string().optional(),
            "cellPhone": t.string().optional(),
            "familyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickCommonPersonOut"])
    types["EnterpriseTopazSidekickMeetingNotesCardRequestIn"] = t.struct(
        {
            "canCreateFor": t.array(t.string()).optional(),
            "event": t.proxy(
                renames["EnterpriseTopazSidekickAgendaEntryIn"]
            ).optional(),
            "error": t.proxy(
                renames["EnterpriseTopazSidekickMeetingNotesCardErrorIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickMeetingNotesCardRequestIn"])
    types["EnterpriseTopazSidekickMeetingNotesCardRequestOut"] = t.struct(
        {
            "canCreateFor": t.array(t.string()).optional(),
            "event": t.proxy(
                renames["EnterpriseTopazSidekickAgendaEntryOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickMeetingNotesCardRequestOut"])
    types["DatePropertyOptionsIn"] = t.struct(
        {"operatorOptions": t.proxy(renames["DateOperatorOptionsIn"]).optional()}
    ).named(renames["DatePropertyOptionsIn"])
    types["DatePropertyOptionsOut"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["DateOperatorOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatePropertyOptionsOut"])
    types["SearchApplicationSessionStatsIn"] = t.struct(
        {
            "searchSessionsCount": t.string().optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["SearchApplicationSessionStatsIn"])
    types["SearchApplicationSessionStatsOut"] = t.struct(
        {
            "searchSessionsCount": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchApplicationSessionStatsOut"])
    types["EnterpriseTopazSidekickCommonDocumentJustificationIn"] = t.struct(
        {"reason": t.string().optional(), "justification": t.string().optional()}
    ).named(renames["EnterpriseTopazSidekickCommonDocumentJustificationIn"])
    types["EnterpriseTopazSidekickCommonDocumentJustificationOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "justification": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickCommonDocumentJustificationOut"])
    types["DoubleOperatorOptionsIn"] = t.struct(
        {"operatorName": t.string().optional()}
    ).named(renames["DoubleOperatorOptionsIn"])
    types["DoubleOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleOperatorOptionsOut"])
    types["MatchRangeIn"] = t.struct(
        {"end": t.integer().optional(), "start": t.integer().optional()}
    ).named(renames["MatchRangeIn"])
    types["MatchRangeOut"] = t.struct(
        {
            "end": t.integer().optional(),
            "start": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatchRangeOut"])
    types["ValueIn"] = t.struct(
        {
            "dateValue": t.proxy(renames["DateIn"]),
            "booleanValue": t.boolean(),
            "stringValue": t.string(),
            "doubleValue": t.number(),
            "timestampValue": t.string(),
            "integerValue": t.string(),
        }
    ).named(renames["ValueIn"])
    types["ValueOut"] = t.struct(
        {
            "dateValue": t.proxy(renames["DateOut"]),
            "booleanValue": t.boolean(),
            "stringValue": t.string(),
            "doubleValue": t.number(),
            "timestampValue": t.string(),
            "integerValue": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueOut"])
    types["CompositeFilterIn"] = t.struct(
        {
            "subFilters": t.array(t.proxy(renames["FilterIn"])).optional(),
            "logicOperator": t.string().optional(),
        }
    ).named(renames["CompositeFilterIn"])
    types["CompositeFilterOut"] = t.struct(
        {
            "subFilters": t.array(t.proxy(renames["FilterOut"])).optional(),
            "logicOperator": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompositeFilterOut"])
    types["PropertyDefinitionIn"] = t.struct(
        {
            "isReturnable": t.boolean().optional(),
            "isSuggestable": t.boolean().optional(),
            "objectPropertyOptions": t.proxy(renames["ObjectPropertyOptionsIn"]),
            "datePropertyOptions": t.proxy(renames["DatePropertyOptionsIn"]),
            "htmlPropertyOptions": t.proxy(renames["HtmlPropertyOptionsIn"]),
            "isFacetable": t.boolean().optional(),
            "isSortable": t.boolean().optional(),
            "enumPropertyOptions": t.proxy(renames["EnumPropertyOptionsIn"]),
            "integerPropertyOptions": t.proxy(renames["IntegerPropertyOptionsIn"]),
            "displayOptions": t.proxy(renames["PropertyDisplayOptionsIn"]).optional(),
            "isWildcardSearchable": t.boolean().optional(),
            "booleanPropertyOptions": t.proxy(renames["BooleanPropertyOptionsIn"]),
            "name": t.string().optional(),
            "timestampPropertyOptions": t.proxy(renames["TimestampPropertyOptionsIn"]),
            "textPropertyOptions": t.proxy(renames["TextPropertyOptionsIn"]),
            "doublePropertyOptions": t.proxy(renames["DoublePropertyOptionsIn"]),
            "isRepeatable": t.boolean().optional(),
        }
    ).named(renames["PropertyDefinitionIn"])
    types["PropertyDefinitionOut"] = t.struct(
        {
            "isReturnable": t.boolean().optional(),
            "isSuggestable": t.boolean().optional(),
            "objectPropertyOptions": t.proxy(renames["ObjectPropertyOptionsOut"]),
            "datePropertyOptions": t.proxy(renames["DatePropertyOptionsOut"]),
            "htmlPropertyOptions": t.proxy(renames["HtmlPropertyOptionsOut"]),
            "isFacetable": t.boolean().optional(),
            "isSortable": t.boolean().optional(),
            "enumPropertyOptions": t.proxy(renames["EnumPropertyOptionsOut"]),
            "integerPropertyOptions": t.proxy(renames["IntegerPropertyOptionsOut"]),
            "displayOptions": t.proxy(renames["PropertyDisplayOptionsOut"]).optional(),
            "isWildcardSearchable": t.boolean().optional(),
            "booleanPropertyOptions": t.proxy(renames["BooleanPropertyOptionsOut"]),
            "name": t.string().optional(),
            "timestampPropertyOptions": t.proxy(renames["TimestampPropertyOptionsOut"]),
            "textPropertyOptions": t.proxy(renames["TextPropertyOptionsOut"]),
            "doublePropertyOptions": t.proxy(renames["DoublePropertyOptionsOut"]),
            "isRepeatable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyDefinitionOut"])
    types["MapInfoIn"] = t.struct(
        {
            "zoom": t.integer().optional(),
            "locationUrl": t.proxy(renames["SafeUrlProtoIn"]).optional(),
            "lat": t.number().optional(),
            "mapTile": t.array(t.proxy(renames["MapTileIn"])).optional(),
            "long": t.number().optional(),
        }
    ).named(renames["MapInfoIn"])
    types["MapInfoOut"] = t.struct(
        {
            "zoom": t.integer().optional(),
            "locationUrl": t.proxy(renames["SafeUrlProtoOut"]).optional(),
            "lat": t.number().optional(),
            "mapTile": t.array(t.proxy(renames["MapTileOut"])).optional(),
            "long": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MapInfoOut"])
    types["EnterpriseTopazSidekickRecentDocumentsCardProtoIn"] = t.struct(
        {
            "document": t.array(
                t.proxy(renames["EnterpriseTopazSidekickCommonDocumentIn"])
            )
        }
    ).named(renames["EnterpriseTopazSidekickRecentDocumentsCardProtoIn"])
    types["EnterpriseTopazSidekickRecentDocumentsCardProtoOut"] = t.struct(
        {
            "document": t.array(
                t.proxy(renames["EnterpriseTopazSidekickCommonDocumentOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickRecentDocumentsCardProtoOut"])
    types["StructuredResultIn"] = t.struct(
        {"person": t.proxy(renames["PersonIn"]).optional()}
    ).named(renames["StructuredResultIn"])
    types["StructuredResultOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredResultOut"])
    types["EnterpriseTopazSidekickAssistCardProtoIn"] = t.struct(
        {
            "personAnswerCard": t.proxy(
                renames["EnterpriseTopazSidekickPeopleAnswerPersonAnswerCardIn"]
            ).optional(),
            "suggestedQueryAnswerCard": t.proxy(
                renames["EnterpriseTopazSidekickAnswerSuggestedQueryAnswerCardIn"]
            ).optional(),
            "peopleDisambiguationCard": t.proxy(
                renames["EnterpriseTopazSidekickPeopleDisambiguationCardIn"]
            ).optional(),
            "cardMetadata": t.proxy(
                renames["EnterpriseTopazSidekickCardMetadataIn"]
            ).optional(),
            "agendaGroupCardProto": t.proxy(
                renames["EnterpriseTopazSidekickAgendaGroupCardProtoIn"]
            ).optional(),
            "genericAnswerCard": t.proxy(
                renames["EnterpriseTopazSidekickGenericAnswerCardIn"]
            ).optional(),
            "meetingNotesCardRequest": t.proxy(
                renames["EnterpriseTopazSidekickMeetingNotesCardRequestIn"]
            ).optional(),
            "meeting": t.proxy(
                renames["EnterpriseTopazSidekickAgendaEntryIn"]
            ).optional(),
            "findMeetingTimeCard": t.proxy(
                renames["EnterpriseTopazSidekickFindMeetingTimeCardProtoIn"]
            ).optional(),
            "documentsWithMentions": t.proxy(
                renames["EnterpriseTopazSidekickDocumentPerCategoryListIn"]
            ).optional(),
            "documentListCard": t.proxy(
                renames["EnterpriseTopazSidekickDocumentPerCategoryListIn"]
            ).optional(),
            "shareMeetingDocsCard": t.proxy(
                renames["EnterpriseTopazSidekickShareMeetingDocsCardProtoIn"]
            ).optional(),
            "getAndKeepAheadCard": t.proxy(
                renames["EnterpriseTopazSidekickGetAndKeepAheadCardProtoIn"]
            ).optional(),
            "thirdPartyAnswerCard": t.proxy(
                renames["ThirdPartyGenericCardIn"]
            ).optional(),
            "workInProgressCardProto": t.proxy(
                renames["EnterpriseTopazSidekickRecentDocumentsCardProtoIn"]
            ).optional(),
            "relatedPeopleAnswerCard": t.proxy(
                renames["EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCardIn"]
            ).optional(),
            "meetingNotesCard": t.proxy(
                renames["EnterpriseTopazSidekickMeetingNotesCardProtoIn"]
            ).optional(),
            "personalizedDocsCard": t.proxy(
                renames["EnterpriseTopazSidekickPersonalizedDocsCardProtoIn"]
            ).optional(),
            "sharedDocuments": t.proxy(
                renames["EnterpriseTopazSidekickDocumentPerCategoryListIn"]
            ).optional(),
            "personProfileCard": t.proxy(
                renames["EnterpriseTopazSidekickPersonProfileCardIn"]
            ).optional(),
            "peoplePromotionCard": t.proxy(renames["PeoplePromotionCardIn"]).optional(),
            "cardType": t.string().optional(),
            "conflictingMeetingsCard": t.proxy(
                renames["EnterpriseTopazSidekickConflictingEventsCardProtoIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickAssistCardProtoIn"])
    types["EnterpriseTopazSidekickAssistCardProtoOut"] = t.struct(
        {
            "personAnswerCard": t.proxy(
                renames["EnterpriseTopazSidekickPeopleAnswerPersonAnswerCardOut"]
            ).optional(),
            "suggestedQueryAnswerCard": t.proxy(
                renames["EnterpriseTopazSidekickAnswerSuggestedQueryAnswerCardOut"]
            ).optional(),
            "peopleDisambiguationCard": t.proxy(
                renames["EnterpriseTopazSidekickPeopleDisambiguationCardOut"]
            ).optional(),
            "cardMetadata": t.proxy(
                renames["EnterpriseTopazSidekickCardMetadataOut"]
            ).optional(),
            "agendaGroupCardProto": t.proxy(
                renames["EnterpriseTopazSidekickAgendaGroupCardProtoOut"]
            ).optional(),
            "genericAnswerCard": t.proxy(
                renames["EnterpriseTopazSidekickGenericAnswerCardOut"]
            ).optional(),
            "meetingNotesCardRequest": t.proxy(
                renames["EnterpriseTopazSidekickMeetingNotesCardRequestOut"]
            ).optional(),
            "meeting": t.proxy(
                renames["EnterpriseTopazSidekickAgendaEntryOut"]
            ).optional(),
            "findMeetingTimeCard": t.proxy(
                renames["EnterpriseTopazSidekickFindMeetingTimeCardProtoOut"]
            ).optional(),
            "documentsWithMentions": t.proxy(
                renames["EnterpriseTopazSidekickDocumentPerCategoryListOut"]
            ).optional(),
            "documentListCard": t.proxy(
                renames["EnterpriseTopazSidekickDocumentPerCategoryListOut"]
            ).optional(),
            "shareMeetingDocsCard": t.proxy(
                renames["EnterpriseTopazSidekickShareMeetingDocsCardProtoOut"]
            ).optional(),
            "getAndKeepAheadCard": t.proxy(
                renames["EnterpriseTopazSidekickGetAndKeepAheadCardProtoOut"]
            ).optional(),
            "thirdPartyAnswerCard": t.proxy(
                renames["ThirdPartyGenericCardOut"]
            ).optional(),
            "workInProgressCardProto": t.proxy(
                renames["EnterpriseTopazSidekickRecentDocumentsCardProtoOut"]
            ).optional(),
            "relatedPeopleAnswerCard": t.proxy(
                renames["EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCardOut"]
            ).optional(),
            "meetingNotesCard": t.proxy(
                renames["EnterpriseTopazSidekickMeetingNotesCardProtoOut"]
            ).optional(),
            "personalizedDocsCard": t.proxy(
                renames["EnterpriseTopazSidekickPersonalizedDocsCardProtoOut"]
            ).optional(),
            "sharedDocuments": t.proxy(
                renames["EnterpriseTopazSidekickDocumentPerCategoryListOut"]
            ).optional(),
            "personProfileCard": t.proxy(
                renames["EnterpriseTopazSidekickPersonProfileCardOut"]
            ).optional(),
            "peoplePromotionCard": t.proxy(
                renames["PeoplePromotionCardOut"]
            ).optional(),
            "cardType": t.string().optional(),
            "conflictingMeetingsCard": t.proxy(
                renames["EnterpriseTopazSidekickConflictingEventsCardProtoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickAssistCardProtoOut"])
    types["UnmappedIdentityIn"] = t.struct(
        {
            "externalIdentity": t.proxy(renames["PrincipalIn"]).optional(),
            "resolutionStatusCode": t.string().optional(),
        }
    ).named(renames["UnmappedIdentityIn"])
    types["UnmappedIdentityOut"] = t.struct(
        {
            "externalIdentity": t.proxy(renames["PrincipalOut"]).optional(),
            "resolutionStatusCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnmappedIdentityOut"])
    types["ContextIn"] = t.struct(
        {
            "query": t.array(t.string()).optional(),
            "endDayOffsetSec": t.string().optional(),
            "endDateSec": t.string().optional(),
            "app": t.array(t.string()).optional(),
            "locale": t.array(t.string()).optional(),
            "startDayOffsetSec": t.string().optional(),
            "location": t.array(t.string()).optional(),
            "dayOfWeek": t.array(t.integer()).optional(),
            "startDateSec": t.string().optional(),
            "type": t.array(t.string()).optional(),
            "surface": t.array(t.string()).optional(),
        }
    ).named(renames["ContextIn"])
    types["ContextOut"] = t.struct(
        {
            "query": t.array(t.string()).optional(),
            "endDayOffsetSec": t.string().optional(),
            "endDateSec": t.string().optional(),
            "app": t.array(t.string()).optional(),
            "locale": t.array(t.string()).optional(),
            "startDayOffsetSec": t.string().optional(),
            "location": t.array(t.string()).optional(),
            "dayOfWeek": t.array(t.integer()).optional(),
            "startDateSec": t.string().optional(),
            "type": t.array(t.string()).optional(),
            "surface": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextOut"])
    types["DateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["IndexItemOptionsIn"] = t.struct(
        {"allowUnknownGsuitePrincipals": t.boolean().optional()}
    ).named(renames["IndexItemOptionsIn"])
    types["IndexItemOptionsOut"] = t.struct(
        {
            "allowUnknownGsuitePrincipals": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexItemOptionsOut"])
    types["SearchRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "facetOptions": t.array(t.proxy(renames["FacetOptionsIn"])),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionIn"])
            ).optional(),
            "queryInterpretationOptions": t.proxy(
                renames["QueryInterpretationOptionsIn"]
            ).optional(),
            "contextAttributes": t.array(
                t.proxy(renames["ContextAttributeIn"])
            ).optional(),
            "start": t.integer().optional(),
            "sortOptions": t.proxy(renames["SortOptionsIn"]).optional(),
            "query": t.string().optional(),
        }
    ).named(renames["SearchRequestIn"])
    types["SearchRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "facetOptions": t.array(t.proxy(renames["FacetOptionsOut"])),
            "dataSourceRestrictions": t.array(
                t.proxy(renames["DataSourceRestrictionOut"])
            ).optional(),
            "queryInterpretationOptions": t.proxy(
                renames["QueryInterpretationOptionsOut"]
            ).optional(),
            "contextAttributes": t.array(
                t.proxy(renames["ContextAttributeOut"])
            ).optional(),
            "start": t.integer().optional(),
            "sortOptions": t.proxy(renames["SortOptionsOut"]).optional(),
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchRequestOut"])
    types["TimestampPropertyOptionsIn"] = t.struct(
        {"operatorOptions": t.proxy(renames["TimestampOperatorOptionsIn"]).optional()}
    ).named(renames["TimestampPropertyOptionsIn"])
    types["TimestampPropertyOptionsOut"] = t.struct(
        {
            "operatorOptions": t.proxy(
                renames["TimestampOperatorOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimestampPropertyOptionsOut"])
    types["HtmlValuesIn"] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames["HtmlValuesIn"]
    )
    types["HtmlValuesOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HtmlValuesOut"])
    types["EnterpriseTopazSidekickAgendaGroupCardProtoIn"] = t.struct(
        {
            "context": t.proxy(
                renames["EnterpriseTopazSidekickAgendaGroupCardProtoContextIn"]
            ),
            "agendaItem": t.array(
                t.proxy(renames["EnterpriseTopazSidekickAgendaItemIn"])
            ),
            "currentAgendaItem": t.proxy(
                renames["EnterpriseTopazSidekickAgendaItemIn"]
            ),
        }
    ).named(renames["EnterpriseTopazSidekickAgendaGroupCardProtoIn"])
    types["EnterpriseTopazSidekickAgendaGroupCardProtoOut"] = t.struct(
        {
            "context": t.proxy(
                renames["EnterpriseTopazSidekickAgendaGroupCardProtoContextOut"]
            ),
            "agendaItem": t.array(
                t.proxy(renames["EnterpriseTopazSidekickAgendaItemOut"])
            ),
            "currentAgendaItem": t.proxy(
                renames["EnterpriseTopazSidekickAgendaItemOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickAgendaGroupCardProtoOut"])
    types["FacetBucketIn"] = t.struct(
        {
            "percentage": t.integer().optional(),
            "filter": t.proxy(renames["FilterIn"]).optional(),
            "value": t.proxy(renames["ValueIn"]),
            "count": t.integer().optional(),
        }
    ).named(renames["FacetBucketIn"])
    types["FacetBucketOut"] = t.struct(
        {
            "percentage": t.integer().optional(),
            "filter": t.proxy(renames["FilterOut"]).optional(),
            "value": t.proxy(renames["ValueOut"]),
            "count": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FacetBucketOut"])
    types["ValueFilterIn"] = t.struct(
        {
            "value": t.proxy(renames["ValueIn"]).optional(),
            "operatorName": t.string().optional(),
        }
    ).named(renames["ValueFilterIn"])
    types["ValueFilterOut"] = t.struct(
        {
            "value": t.proxy(renames["ValueOut"]).optional(),
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueFilterOut"])
    types["EnterpriseTopazSidekickDocumentGroupIn"] = t.struct(
        {
            "personalizedDocument": t.array(
                t.proxy(renames["EnterpriseTopazSidekickCommonDocumentIn"])
            ).optional(),
            "groupType": t.string().optional(),
        }
    ).named(renames["EnterpriseTopazSidekickDocumentGroupIn"])
    types["EnterpriseTopazSidekickDocumentGroupOut"] = t.struct(
        {
            "personalizedDocument": t.array(
                t.proxy(renames["EnterpriseTopazSidekickCommonDocumentOut"])
            ).optional(),
            "groupType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickDocumentGroupOut"])
    types["PollItemsResponseIn"] = t.struct(
        {"items": t.array(t.proxy(renames["ItemIn"])).optional()}
    ).named(renames["PollItemsResponseIn"])
    types["PollItemsResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ItemOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PollItemsResponseOut"])
    types["DataSourceIn"] = t.struct(
        {
            "operationIds": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "indexingServiceAccounts": t.array(t.string()).optional(),
            "itemsVisibility": t.array(
                t.proxy(renames["GSuitePrincipalIn"])
            ).optional(),
            "shortName": t.string().optional(),
            "disableServing": t.boolean().optional(),
            "disableModifications": t.boolean().optional(),
            "returnThumbnailUrls": t.boolean().optional(),
        }
    ).named(renames["DataSourceIn"])
    types["DataSourceOut"] = t.struct(
        {
            "operationIds": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "indexingServiceAccounts": t.array(t.string()).optional(),
            "itemsVisibility": t.array(
                t.proxy(renames["GSuitePrincipalOut"])
            ).optional(),
            "shortName": t.string().optional(),
            "disableServing": t.boolean().optional(),
            "disableModifications": t.boolean().optional(),
            "returnThumbnailUrls": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceOut"])
    types["BackgroundColoredTextIn"] = t.struct(
        {"backgroundColor": t.string().optional(), "text": t.string().optional()}
    ).named(renames["BackgroundColoredTextIn"])
    types["BackgroundColoredTextOut"] = t.struct(
        {
            "backgroundColor": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackgroundColoredTextOut"])
    types["QueryActivityIn"] = t.struct({"query": t.string().optional()}).named(
        renames["QueryActivityIn"]
    )
    types["QueryActivityOut"] = t.struct(
        {
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryActivityOut"])
    types["ErrorMessageIn"] = t.struct(
        {"source": t.proxy(renames["SourceIn"]), "errorMessage": t.string()}
    ).named(renames["ErrorMessageIn"])
    types["ErrorMessageOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]),
            "errorMessage": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorMessageOut"])
    types["EnterpriseTopazSidekickGetAndKeepAheadCardProtoIn"] = t.struct(
        {
            "mentionedDocuments": t.proxy(
                renames["EnterpriseTopazSidekickDocumentPerCategoryListIn"]
            ),
            "declinedEvents": t.proxy(
                renames[
                    "EnterpriseTopazSidekickGetAndKeepAheadCardProtoDeclinedEventsIn"
                ]
            ),
            "sharedDocuments": t.proxy(
                renames["EnterpriseTopazSidekickDocumentPerCategoryListIn"]
            ),
        }
    ).named(renames["EnterpriseTopazSidekickGetAndKeepAheadCardProtoIn"])
    types["EnterpriseTopazSidekickGetAndKeepAheadCardProtoOut"] = t.struct(
        {
            "mentionedDocuments": t.proxy(
                renames["EnterpriseTopazSidekickDocumentPerCategoryListOut"]
            ),
            "declinedEvents": t.proxy(
                renames[
                    "EnterpriseTopazSidekickGetAndKeepAheadCardProtoDeclinedEventsOut"
                ]
            ),
            "sharedDocuments": t.proxy(
                renames["EnterpriseTopazSidekickDocumentPerCategoryListOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickGetAndKeepAheadCardProtoOut"])
    types["HtmlOperatorOptionsIn"] = t.struct(
        {"operatorName": t.string().optional()}
    ).named(renames["HtmlOperatorOptionsIn"])
    types["HtmlOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HtmlOperatorOptionsOut"])
    types["ListItemsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["ItemIn"])),
        }
    ).named(renames["ListItemsResponseIn"])
    types["ListItemsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["ItemOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListItemsResponseOut"])
    types["EnumValuePairIn"] = t.struct(
        {"integerValue": t.integer().optional(), "stringValue": t.string().optional()}
    ).named(renames["EnumValuePairIn"])
    types["EnumValuePairOut"] = t.struct(
        {
            "integerValue": t.integer().optional(),
            "stringValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumValuePairOut"])
    types["ListUnmappedIdentitiesResponseIn"] = t.struct(
        {
            "unmappedIdentities": t.array(t.proxy(renames["UnmappedIdentityIn"])),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListUnmappedIdentitiesResponseIn"])
    types["ListUnmappedIdentitiesResponseOut"] = t.struct(
        {
            "unmappedIdentities": t.array(t.proxy(renames["UnmappedIdentityOut"])),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUnmappedIdentitiesResponseOut"])
    types["GetCustomerUserStatsResponseIn"] = t.struct(
        {"stats": t.array(t.proxy(renames["CustomerUserStatsIn"]))}
    ).named(renames["GetCustomerUserStatsResponseIn"])
    types["GetCustomerUserStatsResponseOut"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["CustomerUserStatsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetCustomerUserStatsResponseOut"])
    types["SpellResultIn"] = t.struct(
        {
            "suggestedQueryHtml": t.proxy(renames["SafeHtmlProtoIn"]).optional(),
            "suggestionType": t.string().optional(),
            "suggestedQuery": t.string().optional(),
        }
    ).named(renames["SpellResultIn"])
    types["SpellResultOut"] = t.struct(
        {
            "suggestedQueryHtml": t.proxy(renames["SafeHtmlProtoOut"]).optional(),
            "suggestionType": t.string().optional(),
            "suggestedQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpellResultOut"])
    types["UpdateSchemaRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "schema": t.proxy(renames["SchemaIn"]).optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
        }
    ).named(renames["UpdateSchemaRequestIn"])
    types["UpdateSchemaRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "schema": t.proxy(renames["SchemaOut"]).optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSchemaRequestOut"])
    types[
        "EnterpriseTopazSidekickDocumentPerCategoryListDocumentPerCategoryListEntryIn"
    ] = t.struct(
        {
            "rationale": t.string().optional(),
            "category": t.string(),
            "document": t.proxy(renames["EnterpriseTopazSidekickCommonDocumentIn"]),
        }
    ).named(
        renames[
            "EnterpriseTopazSidekickDocumentPerCategoryListDocumentPerCategoryListEntryIn"
        ]
    )
    types[
        "EnterpriseTopazSidekickDocumentPerCategoryListDocumentPerCategoryListEntryOut"
    ] = t.struct(
        {
            "rationale": t.string().optional(),
            "category": t.string(),
            "document": t.proxy(renames["EnterpriseTopazSidekickCommonDocumentOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "EnterpriseTopazSidekickDocumentPerCategoryListDocumentPerCategoryListEntryOut"
        ]
    )
    types["EnterpriseTopazSidekickPersonProfileCardRelatedPeopleIn"] = t.struct(
        {
            "relatedPerson": t.array(
                t.proxy(renames["EnterpriseTopazSidekickCommonPersonIn"])
            ).optional(),
            "relation": t.string().optional(),
        }
    ).named(renames["EnterpriseTopazSidekickPersonProfileCardRelatedPeopleIn"])
    types["EnterpriseTopazSidekickPersonProfileCardRelatedPeopleOut"] = t.struct(
        {
            "relatedPerson": t.array(
                t.proxy(renames["EnterpriseTopazSidekickCommonPersonOut"])
            ).optional(),
            "relation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickPersonProfileCardRelatedPeopleOut"])
    types["GetCustomerIndexStatsResponseIn"] = t.struct(
        {
            "averageIndexedItemCount": t.string().optional(),
            "stats": t.array(t.proxy(renames["CustomerIndexStatsIn"])).optional(),
        }
    ).named(renames["GetCustomerIndexStatsResponseIn"])
    types["GetCustomerIndexStatsResponseOut"] = t.struct(
        {
            "averageIndexedItemCount": t.string().optional(),
            "stats": t.array(t.proxy(renames["CustomerIndexStatsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetCustomerIndexStatsResponseOut"])
    types["PersonIn"] = t.struct(
        {
            "name": t.string().optional(),
            "emailAddresses": t.array(t.proxy(renames["EmailAddressIn"])).optional(),
            "obfuscatedId": t.string().optional(),
            "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
            "personNames": t.array(t.proxy(renames["NameIn"])).optional(),
            "photos": t.array(t.proxy(renames["PhotoIn"])).optional(),
        }
    ).named(renames["PersonIn"])
    types["PersonOut"] = t.struct(
        {
            "name": t.string().optional(),
            "emailAddresses": t.array(t.proxy(renames["EmailAddressOut"])).optional(),
            "obfuscatedId": t.string().optional(),
            "phoneNumbers": t.array(t.proxy(renames["PhoneNumberOut"])).optional(),
            "personNames": t.array(t.proxy(renames["NameOut"])).optional(),
            "photos": t.array(t.proxy(renames["PhotoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonOut"])
    types["FilterIn"] = t.struct(
        {
            "compositeFilter": t.proxy(renames["CompositeFilterIn"]),
            "valueFilter": t.proxy(renames["ValueFilterIn"]),
        }
    ).named(renames["FilterIn"])
    types["FilterOut"] = t.struct(
        {
            "compositeFilter": t.proxy(renames["CompositeFilterOut"]),
            "valueFilter": t.proxy(renames["ValueFilterOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])
    types["RemoveActivityRequestIn"] = t.struct(
        {
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "userActivity": t.proxy(renames["UserActivityIn"]).optional(),
        }
    ).named(renames["RemoveActivityRequestIn"])
    types["RemoveActivityRequestOut"] = t.struct(
        {
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "userActivity": t.proxy(renames["UserActivityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveActivityRequestOut"])
    types["GSuitePrincipalIn"] = t.struct(
        {
            "gsuiteUserEmail": t.string().optional(),
            "gsuiteGroupEmail": t.string().optional(),
            "gsuiteDomain": t.boolean().optional(),
        }
    ).named(renames["GSuitePrincipalIn"])
    types["GSuitePrincipalOut"] = t.struct(
        {
            "gsuiteUserEmail": t.string().optional(),
            "gsuiteGroupEmail": t.string().optional(),
            "gsuiteDomain": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GSuitePrincipalOut"])
    types["EnterpriseTopazSidekickTimeSlotIn"] = t.struct(
        {
            "endTimeInMillis": t.string().optional(),
            "startTimeHourAndMinute": t.string().optional(),
            "startTimeDay": t.string().optional(),
            "endTimeDay": t.string().optional(),
            "endTimeHourAndMinute": t.string().optional(),
            "startTimeInMillis": t.string().optional(),
        }
    ).named(renames["EnterpriseTopazSidekickTimeSlotIn"])
    types["EnterpriseTopazSidekickTimeSlotOut"] = t.struct(
        {
            "endTimeInMillis": t.string().optional(),
            "startTimeHourAndMinute": t.string().optional(),
            "startTimeDay": t.string().optional(),
            "endTimeDay": t.string().optional(),
            "endTimeHourAndMinute": t.string().optional(),
            "startTimeInMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickTimeSlotOut"])
    types["NamedPropertyIn"] = t.struct(
        {
            "objectValues": t.proxy(renames["ObjectValuesIn"]),
            "enumValues": t.proxy(renames["EnumValuesIn"]),
            "integerValues": t.proxy(renames["IntegerValuesIn"]),
            "timestampValues": t.proxy(renames["TimestampValuesIn"]),
            "name": t.string().optional(),
            "htmlValues": t.proxy(renames["HtmlValuesIn"]),
            "textValues": t.proxy(renames["TextValuesIn"]),
            "booleanValue": t.boolean(),
            "doubleValues": t.proxy(renames["DoubleValuesIn"]),
            "dateValues": t.proxy(renames["DateValuesIn"]),
        }
    ).named(renames["NamedPropertyIn"])
    types["NamedPropertyOut"] = t.struct(
        {
            "objectValues": t.proxy(renames["ObjectValuesOut"]),
            "enumValues": t.proxy(renames["EnumValuesOut"]),
            "integerValues": t.proxy(renames["IntegerValuesOut"]),
            "timestampValues": t.proxy(renames["TimestampValuesOut"]),
            "name": t.string().optional(),
            "htmlValues": t.proxy(renames["HtmlValuesOut"]),
            "textValues": t.proxy(renames["TextValuesOut"]),
            "booleanValue": t.boolean(),
            "doubleValues": t.proxy(renames["DoubleValuesOut"]),
            "dateValues": t.proxy(renames["DateValuesOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamedPropertyOut"])
    types["CustomerSettingsIn"] = t.struct(
        {
            "vpcSettings": t.proxy(renames["VPCSettingsIn"]).optional(),
            "auditLoggingSettings": t.proxy(
                renames["AuditLoggingSettingsIn"]
            ).optional(),
        }
    ).named(renames["CustomerSettingsIn"])
    types["CustomerSettingsOut"] = t.struct(
        {
            "vpcSettings": t.proxy(renames["VPCSettingsOut"]).optional(),
            "auditLoggingSettings": t.proxy(
                renames["AuditLoggingSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerSettingsOut"])
    types["SortOptionsIn"] = t.struct(
        {"operatorName": t.string().optional(), "sortOrder": t.string().optional()}
    ).named(renames["SortOptionsIn"])
    types["SortOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "sortOrder": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SortOptionsOut"])
    types["ScoringConfigIn"] = t.struct(
        {
            "disablePersonalization": t.boolean().optional(),
            "disableFreshness": t.boolean().optional(),
        }
    ).named(renames["ScoringConfigIn"])
    types["ScoringConfigOut"] = t.struct(
        {
            "disablePersonalization": t.boolean().optional(),
            "disableFreshness": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScoringConfigOut"])
    types["PushItemIn"] = t.struct(
        {
            "queue": t.string().optional(),
            "metadataHash": t.string().optional(),
            "contentHash": t.string().optional(),
            "repositoryError": t.proxy(renames["RepositoryErrorIn"]).optional(),
            "structuredDataHash": t.string().optional(),
            "payload": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["PushItemIn"])
    types["PushItemOut"] = t.struct(
        {
            "queue": t.string().optional(),
            "metadataHash": t.string().optional(),
            "contentHash": t.string().optional(),
            "repositoryError": t.proxy(renames["RepositoryErrorOut"]).optional(),
            "structuredDataHash": t.string().optional(),
            "payload": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PushItemOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["AclInfoIn"] = t.struct(
        {
            "usersCount": t.integer().optional(),
            "scope": t.string().optional(),
            "groupsCount": t.integer().optional(),
        }
    ).named(renames["AclInfoIn"])
    types["AclInfoOut"] = t.struct(
        {
            "usersCount": t.integer().optional(),
            "scope": t.string().optional(),
            "groupsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AclInfoOut"])
    types["ContextAttributeIn"] = t.struct(
        {"name": t.string().optional(), "values": t.array(t.string()).optional()}
    ).named(renames["ContextAttributeIn"])
    types["ContextAttributeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextAttributeOut"])
    types["SchemaIn"] = t.struct(
        {
            "operationIds": t.array(t.string()).optional(),
            "objectDefinitions": t.array(
                t.proxy(renames["ObjectDefinitionIn"])
            ).optional(),
        }
    ).named(renames["SchemaIn"])
    types["SchemaOut"] = t.struct(
        {
            "operationIds": t.array(t.string()).optional(),
            "objectDefinitions": t.array(
                t.proxy(renames["ObjectDefinitionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaOut"])
    types["CustomerSearchApplicationStatsIn"] = t.struct(
        {"count": t.string().optional(), "date": t.proxy(renames["DateIn"]).optional()}
    ).named(renames["CustomerSearchApplicationStatsIn"])
    types["CustomerSearchApplicationStatsOut"] = t.struct(
        {
            "count": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerSearchApplicationStatsOut"])
    types["CustomerUserStatsIn"] = t.struct(
        {
            "oneDayActiveUsersCount": t.string().optional(),
            "thirtyDaysActiveUsersCount": t.string().optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "sevenDaysActiveUsersCount": t.string().optional(),
        }
    ).named(renames["CustomerUserStatsIn"])
    types["CustomerUserStatsOut"] = t.struct(
        {
            "oneDayActiveUsersCount": t.string().optional(),
            "thirtyDaysActiveUsersCount": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "sevenDaysActiveUsersCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerUserStatsOut"])
    types["IntegerPropertyOptionsIn"] = t.struct(
        {
            "orderedRanking": t.string().optional(),
            "minimumValue": t.string().optional(),
            "operatorOptions": t.proxy(renames["IntegerOperatorOptionsIn"]).optional(),
            "integerFacetingOptions": t.proxy(
                renames["IntegerFacetingOptionsIn"]
            ).optional(),
            "maximumValue": t.string().optional(),
        }
    ).named(renames["IntegerPropertyOptionsIn"])
    types["IntegerPropertyOptionsOut"] = t.struct(
        {
            "orderedRanking": t.string().optional(),
            "minimumValue": t.string().optional(),
            "operatorOptions": t.proxy(renames["IntegerOperatorOptionsOut"]).optional(),
            "integerFacetingOptions": t.proxy(
                renames["IntegerFacetingOptionsOut"]
            ).optional(),
            "maximumValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerPropertyOptionsOut"])
    types["EnterpriseTopazSidekickGetAndKeepAheadCardProtoDeclinedEventsIn"] = t.struct(
        {"events": t.array(t.proxy(renames["EnterpriseTopazSidekickAgendaEntryIn"]))}
    ).named(renames["EnterpriseTopazSidekickGetAndKeepAheadCardProtoDeclinedEventsIn"])
    types[
        "EnterpriseTopazSidekickGetAndKeepAheadCardProtoDeclinedEventsOut"
    ] = t.struct(
        {
            "events": t.array(
                t.proxy(renames["EnterpriseTopazSidekickAgendaEntryOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["EnterpriseTopazSidekickGetAndKeepAheadCardProtoDeclinedEventsOut"]
    )
    types["IntegerFacetingOptionsIn"] = t.struct(
        {"integerBuckets": t.array(t.string()).optional()}
    ).named(renames["IntegerFacetingOptionsIn"])
    types["IntegerFacetingOptionsOut"] = t.struct(
        {
            "integerBuckets": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerFacetingOptionsOut"])
    types["QuerySuggestionIn"] = t.struct({"_": t.string().optional()}).named(
        renames["QuerySuggestionIn"]
    )
    types["QuerySuggestionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["QuerySuggestionOut"])
    types["EnumPropertyOptionsIn"] = t.struct(
        {
            "orderedRanking": t.string().optional(),
            "possibleValues": t.array(t.proxy(renames["EnumValuePairIn"])).optional(),
            "operatorOptions": t.proxy(renames["EnumOperatorOptionsIn"]).optional(),
        }
    ).named(renames["EnumPropertyOptionsIn"])
    types["EnumPropertyOptionsOut"] = t.struct(
        {
            "orderedRanking": t.string().optional(),
            "possibleValues": t.array(t.proxy(renames["EnumValuePairOut"])).optional(),
            "operatorOptions": t.proxy(renames["EnumOperatorOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumPropertyOptionsOut"])
    types["IndexItemRequestIn"] = t.struct(
        {
            "indexItemOptions": t.proxy(renames["IndexItemOptionsIn"]),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "item": t.proxy(renames["ItemIn"]).optional(),
            "mode": t.string(),
            "connectorName": t.string().optional(),
        }
    ).named(renames["IndexItemRequestIn"])
    types["IndexItemRequestOut"] = t.struct(
        {
            "indexItemOptions": t.proxy(renames["IndexItemOptionsOut"]),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "item": t.proxy(renames["ItemOut"]).optional(),
            "mode": t.string(),
            "connectorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexItemRequestOut"])
    types["MediaIn"] = t.struct({"resourceName": t.string().optional()}).named(
        renames["MediaIn"]
    )
    types["MediaOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaOut"])
    types["ObjectOptionsIn"] = t.struct(
        {
            "displayOptions": t.proxy(renames["ObjectDisplayOptionsIn"]).optional(),
            "freshnessOptions": t.proxy(renames["FreshnessOptionsIn"]).optional(),
            "suggestionFilteringOperators": t.array(t.string()).optional(),
        }
    ).named(renames["ObjectOptionsIn"])
    types["ObjectOptionsOut"] = t.struct(
        {
            "displayOptions": t.proxy(renames["ObjectDisplayOptionsOut"]).optional(),
            "freshnessOptions": t.proxy(renames["FreshnessOptionsOut"]).optional(),
            "suggestionFilteringOperators": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectOptionsOut"])
    types["EnterpriseTopazSidekickGapIn"] = t.struct(
        {
            "remainingTime": t.string(),
            "startTime": t.string().optional(),
            "endTimeMs": t.string(),
            "endTime": t.string().optional(),
            "displayRemainingTime": t.string().optional(),
            "startTimeMs": t.string(),
        }
    ).named(renames["EnterpriseTopazSidekickGapIn"])
    types["EnterpriseTopazSidekickGapOut"] = t.struct(
        {
            "remainingTime": t.string(),
            "startTime": t.string().optional(),
            "endTimeMs": t.string(),
            "endTime": t.string().optional(),
            "displayRemainingTime": t.string().optional(),
            "startTimeMs": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickGapOut"])
    types["TimestampOperatorOptionsIn"] = t.struct(
        {
            "lessThanOperatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
            "operatorName": t.string().optional(),
        }
    ).named(renames["TimestampOperatorOptionsIn"])
    types["TimestampOperatorOptionsOut"] = t.struct(
        {
            "lessThanOperatorName": t.string().optional(),
            "greaterThanOperatorName": t.string().optional(),
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimestampOperatorOptionsOut"])
    types["PersonCoreIn"] = t.struct(
        {
            "chatUrl": t.proxy(renames["SafeUrlProtoIn"]).optional(),
            "jobTitle": t.string().optional(),
            "postalAddress": t.string().optional(),
            "fingerprint": t.string().optional(),
            "name": t.string().optional(),
            "directReports": t.array(t.proxy(renames["PersonCoreIn"])).optional(),
            "phoneNumbers": t.array(
                t.proxy(renames["EnterpriseTopazFrontendTeamsPersonCorePhoneNumberIn"])
            ),
            "addressMeAs": t.string().optional(),
            "adminTo": t.array(t.proxy(renames["PersonCoreIn"])).optional(),
            "totalFteCount": t.string().optional(),
            "dottedLineReports": t.array(t.proxy(renames["PersonCoreIn"])).optional(),
            "birthday": t.proxy(renames["DateIn"]).optional(),
            "department": t.string().optional(),
            "personId": t.string().optional(),
            "photoUrl": t.proxy(renames["SafeUrlProtoIn"]).optional(),
            "dottedLineManagers": t.array(t.proxy(renames["PersonCoreIn"])).optional(),
            "ftePermille": t.string().optional(),
            "keywords": t.struct({"_": t.string().optional()}).optional(),
            "location": t.string().optional(),
            "totalDlrCount": t.integer().optional(),
            "totalDirectReportsCount": t.integer().optional(),
            "mission": t.string().optional(),
            "username": t.string().optional(),
            "waldoComeBackTime": t.string(),
            "keywordTypes": t.array(t.string()).optional(),
            "availabilityStatus": t.string(),
            "emails": t.array(t.string()).optional(),
            "gmailUrl": t.string(),
            "admins": t.array(t.proxy(renames["PersonCoreIn"])).optional(),
            "managers": t.array(t.proxy(renames["PersonCoreIn"])).optional(),
            "calendarUrl": t.proxy(renames["SafeUrlProtoIn"]).optional(),
            "links": t.array(
                t.proxy(renames["EnterpriseTopazFrontendTeamsLinkIn"])
            ).optional(),
            "employeeId": t.string().optional(),
            "officeLocation": t.string().optional(),
            "geoLocation": t.proxy(renames["MapInfoIn"]),
            "costCenter": t.string().optional(),
        }
    ).named(renames["PersonCoreIn"])
    types["PersonCoreOut"] = t.struct(
        {
            "chatUrl": t.proxy(renames["SafeUrlProtoOut"]).optional(),
            "jobTitle": t.string().optional(),
            "postalAddress": t.string().optional(),
            "fingerprint": t.string().optional(),
            "name": t.string().optional(),
            "directReports": t.array(t.proxy(renames["PersonCoreOut"])).optional(),
            "phoneNumbers": t.array(
                t.proxy(renames["EnterpriseTopazFrontendTeamsPersonCorePhoneNumberOut"])
            ),
            "addressMeAs": t.string().optional(),
            "adminTo": t.array(t.proxy(renames["PersonCoreOut"])).optional(),
            "totalFteCount": t.string().optional(),
            "dottedLineReports": t.array(t.proxy(renames["PersonCoreOut"])).optional(),
            "birthday": t.proxy(renames["DateOut"]).optional(),
            "department": t.string().optional(),
            "personId": t.string().optional(),
            "photoUrl": t.proxy(renames["SafeUrlProtoOut"]).optional(),
            "dottedLineManagers": t.array(t.proxy(renames["PersonCoreOut"])).optional(),
            "ftePermille": t.string().optional(),
            "keywords": t.struct({"_": t.string().optional()}).optional(),
            "location": t.string().optional(),
            "totalDlrCount": t.integer().optional(),
            "totalDirectReportsCount": t.integer().optional(),
            "mission": t.string().optional(),
            "username": t.string().optional(),
            "waldoComeBackTime": t.string(),
            "keywordTypes": t.array(t.string()).optional(),
            "availabilityStatus": t.string(),
            "emails": t.array(t.string()).optional(),
            "gmailUrl": t.string(),
            "admins": t.array(t.proxy(renames["PersonCoreOut"])).optional(),
            "managers": t.array(t.proxy(renames["PersonCoreOut"])).optional(),
            "calendarUrl": t.proxy(renames["SafeUrlProtoOut"]).optional(),
            "links": t.array(
                t.proxy(renames["EnterpriseTopazFrontendTeamsLinkOut"])
            ).optional(),
            "employeeId": t.string().optional(),
            "officeLocation": t.string().optional(),
            "geoLocation": t.proxy(renames["MapInfoOut"]),
            "costCenter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonCoreOut"])
    types["PrincipalIn"] = t.struct(
        {
            "gsuitePrincipal": t.proxy(renames["GSuitePrincipalIn"]).optional(),
            "userResourceName": t.string().optional(),
            "groupResourceName": t.string().optional(),
        }
    ).named(renames["PrincipalIn"])
    types["PrincipalOut"] = t.struct(
        {
            "gsuitePrincipal": t.proxy(renames["GSuitePrincipalOut"]).optional(),
            "userResourceName": t.string().optional(),
            "groupResourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrincipalOut"])
    types["ContentIn"] = t.struct(
        {
            "title": t.proxy(renames["BackgroundColoredTextIn"]).optional(),
            "subtitle": t.proxy(renames["BackgroundColoredTextIn"]).optional(),
            "description": t.proxy(renames["SafeHtmlProtoIn"]).optional(),
            "actions": t.array(t.proxy(renames["ActionIn"])).optional(),
        }
    ).named(renames["ContentIn"])
    types["ContentOut"] = t.struct(
        {
            "title": t.proxy(renames["BackgroundColoredTextOut"]).optional(),
            "subtitle": t.proxy(renames["BackgroundColoredTextOut"]).optional(),
            "description": t.proxy(renames["SafeHtmlProtoOut"]).optional(),
            "actions": t.array(t.proxy(renames["ActionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentOut"])
    types["SourceResultCountIn"] = t.struct(
        {
            "resultCountExact": t.string().optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
            "resultCountEstimate": t.string().optional(),
            "hasMoreResults": t.boolean().optional(),
        }
    ).named(renames["SourceResultCountIn"])
    types["SourceResultCountOut"] = t.struct(
        {
            "resultCountExact": t.string().optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "resultCountEstimate": t.string().optional(),
            "hasMoreResults": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceResultCountOut"])
    types["GoogleDocsResultInfoIn"] = t.struct(
        {
            "cosmoNameSpace": t.integer().optional(),
            "shareScope": t.proxy(renames["ShareScopeIn"]).optional(),
            "mimeType": t.string().optional(),
            "attachmentSha1": t.string().optional(),
            "cosmoId": t.proxy(renames["IdIn"]).optional(),
            "encryptedId": t.string().optional(),
        }
    ).named(renames["GoogleDocsResultInfoIn"])
    types["GoogleDocsResultInfoOut"] = t.struct(
        {
            "cosmoNameSpace": t.integer().optional(),
            "shareScope": t.proxy(renames["ShareScopeOut"]).optional(),
            "mimeType": t.string().optional(),
            "attachmentSha1": t.string().optional(),
            "cosmoId": t.proxy(renames["IdOut"]).optional(),
            "encryptedId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDocsResultInfoOut"])
    types["TypeInfoIn"] = t.struct(
        {"videoInfo": t.proxy(renames["VideoInfoIn"]).optional()}
    ).named(renames["TypeInfoIn"])
    types["TypeInfoOut"] = t.struct(
        {
            "videoInfo": t.proxy(renames["VideoInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeInfoOut"])
    types["ObjectDisplayOptionsIn"] = t.struct(
        {
            "metalines": t.array(t.proxy(renames["MetalineIn"])).optional(),
            "objectDisplayLabel": t.string().optional(),
        }
    ).named(renames["ObjectDisplayOptionsIn"])
    types["ObjectDisplayOptionsOut"] = t.struct(
        {
            "metalines": t.array(t.proxy(renames["MetalineOut"])).optional(),
            "objectDisplayLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectDisplayOptionsOut"])
    types["VideoInfoIn"] = t.struct({"duration": t.integer().optional()}).named(
        renames["VideoInfoIn"]
    )
    types["VideoInfoOut"] = t.struct(
        {
            "duration": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoInfoOut"])
    types["GetSearchApplicationQueryStatsResponseIn"] = t.struct(
        {
            "totalQueryCount": t.string().optional(),
            "stats": t.array(
                t.proxy(renames["SearchApplicationQueryStatsIn"])
            ).optional(),
        }
    ).named(renames["GetSearchApplicationQueryStatsResponseIn"])
    types["GetSearchApplicationQueryStatsResponseOut"] = t.struct(
        {
            "totalQueryCount": t.string().optional(),
            "stats": t.array(
                t.proxy(renames["SearchApplicationQueryStatsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetSearchApplicationQueryStatsResponseOut"])
    types["EnterpriseTopazSidekickAnswerSuggestedQueryAnswerCardIn"] = t.struct(
        {
            "suggestedQueryCategory": t.array(
                t.proxy(
                    renames["EnterpriseTopazSidekickAnswerSuggestedQueryCategoryIn"]
                )
            ).optional()
        }
    ).named(renames["EnterpriseTopazSidekickAnswerSuggestedQueryAnswerCardIn"])
    types["EnterpriseTopazSidekickAnswerSuggestedQueryAnswerCardOut"] = t.struct(
        {
            "suggestedQueryCategory": t.array(
                t.proxy(
                    renames["EnterpriseTopazSidekickAnswerSuggestedQueryCategoryOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickAnswerSuggestedQueryAnswerCardOut"])
    types["EnterpriseTopazSidekickShareMeetingDocsCardProtoIn"] = t.struct(
        {
            "document": t.array(
                t.proxy(renames["EnterpriseTopazSidekickCommonDocumentIn"])
            ).optional(),
            "event": t.proxy(
                renames["EnterpriseTopazSidekickAgendaEntryIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickShareMeetingDocsCardProtoIn"])
    types["EnterpriseTopazSidekickShareMeetingDocsCardProtoOut"] = t.struct(
        {
            "document": t.array(
                t.proxy(renames["EnterpriseTopazSidekickCommonDocumentOut"])
            ).optional(),
            "event": t.proxy(
                renames["EnterpriseTopazSidekickAgendaEntryOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickShareMeetingDocsCardProtoOut"])
    types["DriveMimeTypeRestrictIn"] = t.struct({"type": t.string()}).named(
        renames["DriveMimeTypeRestrictIn"]
    )
    types["DriveMimeTypeRestrictOut"] = t.struct(
        {"type": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveMimeTypeRestrictOut"])
    types["EnterpriseTopazSidekickCommonDocumentDriveDocumentMetadataIn"] = t.struct(
        {
            "lastUpdatedTimeMs": t.string().optional(),
            "isPrivate": t.boolean().optional(),
            "lastCommentTimeMs": t.string().optional(),
            "lastEditTimeMs": t.string().optional(),
            "scope": t.string().optional(),
            "lastModificationTimeMillis": t.string().optional(),
            "documentId": t.string().optional(),
            "lastViewTimeMs": t.string().optional(),
            "owner": t.proxy(
                renames["EnterpriseTopazSidekickCommonPersonIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickCommonDocumentDriveDocumentMetadataIn"])
    types["EnterpriseTopazSidekickCommonDocumentDriveDocumentMetadataOut"] = t.struct(
        {
            "lastUpdatedTimeMs": t.string().optional(),
            "isPrivate": t.boolean().optional(),
            "lastCommentTimeMs": t.string().optional(),
            "lastEditTimeMs": t.string().optional(),
            "scope": t.string().optional(),
            "lastModificationTimeMillis": t.string().optional(),
            "documentId": t.string().optional(),
            "lastViewTimeMs": t.string().optional(),
            "owner": t.proxy(
                renames["EnterpriseTopazSidekickCommonPersonOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickCommonDocumentDriveDocumentMetadataOut"])
    types["PushItemRequestIn"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "item": t.proxy(renames["PushItemIn"]).optional(),
            "connectorName": t.string().optional(),
        }
    ).named(renames["PushItemRequestIn"])
    types["PushItemRequestOut"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "item": t.proxy(renames["PushItemOut"]).optional(),
            "connectorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PushItemRequestOut"])
    types["EnterpriseTopazSidekickAnswerAnswerListLabeledAnswerIn"] = t.struct(
        {"answer": t.string().optional(), "label": t.string().optional()}
    ).named(renames["EnterpriseTopazSidekickAnswerAnswerListLabeledAnswerIn"])
    types["EnterpriseTopazSidekickAnswerAnswerListLabeledAnswerOut"] = t.struct(
        {
            "answer": t.string().optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickAnswerAnswerListLabeledAnswerOut"])
    types["DriveFollowUpRestrictIn"] = t.struct({"type": t.string()}).named(
        renames["DriveFollowUpRestrictIn"]
    )
    types["DriveFollowUpRestrictOut"] = t.struct(
        {"type": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveFollowUpRestrictOut"])
    types["QuerySourceIn"] = t.struct(
        {
            "source": t.proxy(renames["SourceIn"]).optional(),
            "operators": t.array(t.proxy(renames["QueryOperatorIn"])).optional(),
            "shortName": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["QuerySourceIn"])
    types["QuerySourceOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "operators": t.array(t.proxy(renames["QueryOperatorOut"])).optional(),
            "shortName": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuerySourceOut"])
    types["StructuredDataObjectIn"] = t.struct(
        {"properties": t.array(t.proxy(renames["NamedPropertyIn"])).optional()}
    ).named(renames["StructuredDataObjectIn"])
    types["StructuredDataObjectOut"] = t.struct(
        {
            "properties": t.array(t.proxy(renames["NamedPropertyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredDataObjectOut"])
    types["PhoneNumberIn"] = t.struct(
        {"type": t.string(), "phoneNumber": t.string().optional()}
    ).named(renames["PhoneNumberIn"])
    types["PhoneNumberOut"] = t.struct(
        {
            "type": t.string(),
            "phoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhoneNumberOut"])
    types["EnterpriseTopazSidekickFindMeetingTimeCardProtoIn"] = t.struct(
        {
            "requester": t.proxy(renames["EnterpriseTopazSidekickPersonIn"]).optional(),
            "timeBoundaries": t.proxy(
                renames["EnterpriseTopazSidekickTimeSlotIn"]
            ).optional(),
            "commonAvailableTimeSlots": t.array(
                t.proxy(renames["EnterpriseTopazSidekickTimeSlotIn"])
            ).optional(),
            "timezoneId": t.string().optional(),
            "invitees": t.array(
                t.proxy(renames["EnterpriseTopazSidekickPersonIn"])
            ).optional(),
            "scheduledMeeting": t.proxy(
                renames["EnterpriseTopazSidekickScheduledMeetingIn"]
            ).optional(),
            "skippedInvitees": t.array(
                t.proxy(renames["EnterpriseTopazSidekickPersonIn"])
            ).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickFindMeetingTimeCardProtoIn"])
    types["EnterpriseTopazSidekickFindMeetingTimeCardProtoOut"] = t.struct(
        {
            "requester": t.proxy(
                renames["EnterpriseTopazSidekickPersonOut"]
            ).optional(),
            "timeBoundaries": t.proxy(
                renames["EnterpriseTopazSidekickTimeSlotOut"]
            ).optional(),
            "commonAvailableTimeSlots": t.array(
                t.proxy(renames["EnterpriseTopazSidekickTimeSlotOut"])
            ).optional(),
            "timezoneId": t.string().optional(),
            "invitees": t.array(
                t.proxy(renames["EnterpriseTopazSidekickPersonOut"])
            ).optional(),
            "scheduledMeeting": t.proxy(
                renames["EnterpriseTopazSidekickScheduledMeetingOut"]
            ).optional(),
            "skippedInvitees": t.array(
                t.proxy(renames["EnterpriseTopazSidekickPersonOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickFindMeetingTimeCardProtoOut"])
    types["EnterpriseTopazSidekickAgendaEntryIn"] = t.struct(
        {
            "chronology": t.string().optional(),
            "startDate": t.string().optional(),
            "eventId": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "document": t.array(
                t.proxy(renames["EnterpriseTopazSidekickCommonDocumentIn"])
            ).optional(),
            "invitee": t.array(
                t.proxy(renames["EnterpriseTopazSidekickPersonIn"])
            ).optional(),
            "isAllDay": t.boolean().optional(),
            "endTimeMs": t.string().optional(),
            "startTime": t.string().optional(),
            "otherAttendeesExcluded": t.boolean().optional(),
            "endTime": t.string().optional(),
            "hangoutUrl": t.string().optional(),
            "showFullEventDetailsToUse": t.boolean().optional(),
            "lastModificationTimeMs": t.string().optional(),
            "guestsCanInviteOthers": t.boolean().optional(),
            "requesterIsOwner": t.boolean().optional(),
            "creator": t.proxy(renames["EnterpriseTopazSidekickPersonIn"]).optional(),
            "hangoutId": t.string().optional(),
            "location": t.string().optional(),
            "guestsCanSeeGuests": t.boolean().optional(),
            "endDate": t.string().optional(),
            "currentUserAttendingStatus": t.string().optional(),
            "startTimeMs": t.string().optional(),
            "timeZone": t.string().optional(),
            "notifyToUser": t.boolean().optional(),
            "agendaItemUrl": t.string().optional(),
            "guestsCanModify": t.boolean().optional(),
        }
    ).named(renames["EnterpriseTopazSidekickAgendaEntryIn"])
    types["EnterpriseTopazSidekickAgendaEntryOut"] = t.struct(
        {
            "chronology": t.string().optional(),
            "startDate": t.string().optional(),
            "eventId": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "document": t.array(
                t.proxy(renames["EnterpriseTopazSidekickCommonDocumentOut"])
            ).optional(),
            "invitee": t.array(
                t.proxy(renames["EnterpriseTopazSidekickPersonOut"])
            ).optional(),
            "isAllDay": t.boolean().optional(),
            "endTimeMs": t.string().optional(),
            "startTime": t.string().optional(),
            "otherAttendeesExcluded": t.boolean().optional(),
            "endTime": t.string().optional(),
            "hangoutUrl": t.string().optional(),
            "showFullEventDetailsToUse": t.boolean().optional(),
            "lastModificationTimeMs": t.string().optional(),
            "guestsCanInviteOthers": t.boolean().optional(),
            "requesterIsOwner": t.boolean().optional(),
            "creator": t.proxy(renames["EnterpriseTopazSidekickPersonOut"]).optional(),
            "hangoutId": t.string().optional(),
            "location": t.string().optional(),
            "guestsCanSeeGuests": t.boolean().optional(),
            "endDate": t.string().optional(),
            "currentUserAttendingStatus": t.string().optional(),
            "startTimeMs": t.string().optional(),
            "timeZone": t.string().optional(),
            "notifyToUser": t.boolean().optional(),
            "agendaItemUrl": t.string().optional(),
            "guestsCanModify": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickAgendaEntryOut"])
    types["ItemAclIn"] = t.struct(
        {
            "readers": t.array(t.proxy(renames["PrincipalIn"])).optional(),
            "aclInheritanceType": t.string().optional(),
            "owners": t.array(t.proxy(renames["PrincipalIn"])).optional(),
            "deniedReaders": t.array(t.proxy(renames["PrincipalIn"])).optional(),
            "inheritAclFrom": t.string().optional(),
        }
    ).named(renames["ItemAclIn"])
    types["ItemAclOut"] = t.struct(
        {
            "readers": t.array(t.proxy(renames["PrincipalOut"])).optional(),
            "aclInheritanceType": t.string().optional(),
            "owners": t.array(t.proxy(renames["PrincipalOut"])).optional(),
            "deniedReaders": t.array(t.proxy(renames["PrincipalOut"])).optional(),
            "inheritAclFrom": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemAclOut"])
    types["EnterpriseTopazSidekickPeopleDisambiguationCardIn"] = t.struct(
        {
            "person": t.array(
                t.proxy(renames["EnterpriseTopazSidekickCommonPersonIn"])
            ).optional()
        }
    ).named(renames["EnterpriseTopazSidekickPeopleDisambiguationCardIn"])
    types["EnterpriseTopazSidekickPeopleDisambiguationCardOut"] = t.struct(
        {
            "person": t.array(
                t.proxy(renames["EnterpriseTopazSidekickCommonPersonOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickPeopleDisambiguationCardOut"])
    types["UnreserveItemsRequestIn"] = t.struct(
        {
            "queue": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "connectorName": t.string().optional(),
        }
    ).named(renames["UnreserveItemsRequestIn"])
    types["UnreserveItemsRequestOut"] = t.struct(
        {
            "queue": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "connectorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnreserveItemsRequestOut"])
    types["SuggestResponseIn"] = t.struct(
        {"suggestResults": t.array(t.proxy(renames["SuggestResultIn"])).optional()}
    ).named(renames["SuggestResponseIn"])
    types["SuggestResponseOut"] = t.struct(
        {
            "suggestResults": t.array(t.proxy(renames["SuggestResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestResponseOut"])
    types["EnterpriseTopazSidekickPersonProfileCardIn"] = t.struct(
        {
            "relatedPeople": t.array(
                t.proxy(
                    renames["EnterpriseTopazSidekickPersonProfileCardRelatedPeopleIn"]
                )
            ),
            "subject": t.proxy(
                renames["EnterpriseTopazSidekickCommonPersonIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickPersonProfileCardIn"])
    types["EnterpriseTopazSidekickPersonProfileCardOut"] = t.struct(
        {
            "relatedPeople": t.array(
                t.proxy(
                    renames["EnterpriseTopazSidekickPersonProfileCardRelatedPeopleOut"]
                )
            ),
            "subject": t.proxy(
                renames["EnterpriseTopazSidekickCommonPersonOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickPersonProfileCardOut"])
    types["DeleteQueueItemsRequestIn"] = t.struct(
        {
            "connectorName": t.string().optional(),
            "queue": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
        }
    ).named(renames["DeleteQueueItemsRequestIn"])
    types["DeleteQueueItemsRequestOut"] = t.struct(
        {
            "connectorName": t.string().optional(),
            "queue": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteQueueItemsRequestOut"])
    types["TextOperatorOptionsIn"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "exactMatchWithOperator": t.boolean().optional(),
        }
    ).named(renames["TextOperatorOptionsIn"])
    types["TextOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "exactMatchWithOperator": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextOperatorOptionsOut"])
    types["SourceIn"] = t.struct(
        {"predefinedSource": t.string().optional(), "name": t.string().optional()}
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "predefinedSource": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["StartUploadItemRequestIn"] = t.struct(
        {
            "connectorName": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
        }
    ).named(renames["StartUploadItemRequestIn"])
    types["StartUploadItemRequestOut"] = t.struct(
        {
            "connectorName": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartUploadItemRequestOut"])
    types["ListQuerySourcesResponseIn"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["QuerySourceIn"])),
            "nextPageToken": t.string(),
        }
    ).named(renames["ListQuerySourcesResponseIn"])
    types["ListQuerySourcesResponseOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["QuerySourceOut"])),
            "nextPageToken": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListQuerySourcesResponseOut"])
    types["SearchApplicationQueryStatsIn"] = t.struct(
        {
            "date": t.proxy(renames["DateIn"]).optional(),
            "queryCountByStatus": t.array(t.proxy(renames["QueryCountByStatusIn"])),
        }
    ).named(renames["SearchApplicationQueryStatsIn"])
    types["SearchApplicationQueryStatsOut"] = t.struct(
        {
            "date": t.proxy(renames["DateOut"]).optional(),
            "queryCountByStatus": t.array(t.proxy(renames["QueryCountByStatusOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchApplicationQueryStatsOut"])
    types["EnterpriseTopazSidekickAnswerAnswerListIn"] = t.struct(
        {
            "type": t.string().optional(),
            "labeledAnswer": t.array(
                t.proxy(
                    renames["EnterpriseTopazSidekickAnswerAnswerListLabeledAnswerIn"]
                )
            ).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickAnswerAnswerListIn"])
    types["EnterpriseTopazSidekickAnswerAnswerListOut"] = t.struct(
        {
            "type": t.string().optional(),
            "labeledAnswer": t.array(
                t.proxy(
                    renames["EnterpriseTopazSidekickAnswerAnswerListLabeledAnswerOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickAnswerAnswerListOut"])
    types["MetadataIn"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["NamedPropertyIn"])).optional(),
            "mimeType": t.string().optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
            "displayOptions": t.proxy(renames["ResultDisplayMetadataIn"]).optional(),
            "createTime": t.string().optional(),
            "owner": t.proxy(renames["PersonIn"]).optional(),
            "thumbnailUrl": t.string().optional(),
            "updateTime": t.string().optional(),
            "objectType": t.string().optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["NamedPropertyOut"])).optional(),
            "mimeType": t.string().optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "displayOptions": t.proxy(renames["ResultDisplayMetadataOut"]).optional(),
            "createTime": t.string().optional(),
            "owner": t.proxy(renames["PersonOut"]).optional(),
            "thumbnailUrl": t.string().optional(),
            "updateTime": t.string().optional(),
            "objectType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["FilterOptionsIn"] = t.struct(
        {
            "filter": t.proxy(renames["FilterIn"]).optional(),
            "objectType": t.string().optional(),
        }
    ).named(renames["FilterOptionsIn"])
    types["FilterOptionsOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterOut"]).optional(),
            "objectType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOptionsOut"])
    types["ThirdPartyGenericCardIn"] = t.struct(
        {
            "isDismissible": t.boolean().optional(),
            "context": t.proxy(renames["ContextIn"]).optional(),
            "content": t.proxy(renames["ContentIn"]).optional(),
            "category": t.string().optional(),
            "cardId": t.string().optional(),
            "priority": t.integer().optional(),
        }
    ).named(renames["ThirdPartyGenericCardIn"])
    types["ThirdPartyGenericCardOut"] = t.struct(
        {
            "isDismissible": t.boolean().optional(),
            "context": t.proxy(renames["ContextOut"]).optional(),
            "content": t.proxy(renames["ContentOut"]).optional(),
            "category": t.string().optional(),
            "cardId": t.string().optional(),
            "priority": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyGenericCardOut"])
    types["ItemIn"] = t.struct(
        {
            "acl": t.proxy(renames["ItemAclIn"]).optional(),
            "status": t.proxy(renames["ItemStatusIn"]).optional(),
            "structuredData": t.proxy(renames["ItemStructuredDataIn"]).optional(),
            "itemType": t.string().optional(),
            "queue": t.string().optional(),
            "version": t.string(),
            "name": t.string().optional(),
            "payload": t.string().optional(),
            "metadata": t.proxy(renames["ItemMetadataIn"]).optional(),
            "content": t.proxy(renames["ItemContentIn"]).optional(),
        }
    ).named(renames["ItemIn"])
    types["ItemOut"] = t.struct(
        {
            "acl": t.proxy(renames["ItemAclOut"]).optional(),
            "status": t.proxy(renames["ItemStatusOut"]).optional(),
            "structuredData": t.proxy(renames["ItemStructuredDataOut"]).optional(),
            "itemType": t.string().optional(),
            "queue": t.string().optional(),
            "version": t.string(),
            "name": t.string().optional(),
            "payload": t.string().optional(),
            "metadata": t.proxy(renames["ItemMetadataOut"]).optional(),
            "content": t.proxy(renames["ItemContentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemOut"])
    types["CustomerSessionStatsIn"] = t.struct(
        {
            "searchSessionsCount": t.string().optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["CustomerSessionStatsIn"])
    types["CustomerSessionStatsOut"] = t.struct(
        {
            "searchSessionsCount": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerSessionStatsOut"])
    types["ResetSearchApplicationRequestIn"] = t.struct(
        {"debugOptions": t.proxy(renames["DebugOptionsIn"]).optional()}
    ).named(renames["ResetSearchApplicationRequestIn"])
    types["ResetSearchApplicationRequestOut"] = t.struct(
        {
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResetSearchApplicationRequestOut"])
    types["UserActivityIn"] = t.struct(
        {"queryActivity": t.proxy(renames["QueryActivityIn"]).optional()}
    ).named(renames["UserActivityIn"])
    types["UserActivityOut"] = t.struct(
        {
            "queryActivity": t.proxy(renames["QueryActivityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserActivityOut"])
    types["EnterpriseTopazSidekickCardMetadataIn"] = t.struct(
        {
            "cardCategory": t.string().optional(),
            "chronology": t.string().optional(),
            "nlpMetadata": t.proxy(
                renames["EnterpriseTopazSidekickNlpMetadataIn"]
            ).optional(),
            "renderMode": t.string().optional(),
            "debugInfo": t.string().optional(),
            "rankingParams": t.proxy(
                renames["EnterpriseTopazSidekickRankingParamsIn"]
            ).optional(),
            "cardId": t.string().optional(),
        }
    ).named(renames["EnterpriseTopazSidekickCardMetadataIn"])
    types["EnterpriseTopazSidekickCardMetadataOut"] = t.struct(
        {
            "cardCategory": t.string().optional(),
            "chronology": t.string().optional(),
            "nlpMetadata": t.proxy(
                renames["EnterpriseTopazSidekickNlpMetadataOut"]
            ).optional(),
            "renderMode": t.string().optional(),
            "debugInfo": t.string().optional(),
            "rankingParams": t.proxy(
                renames["EnterpriseTopazSidekickRankingParamsOut"]
            ).optional(),
            "cardId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickCardMetadataOut"])
    types["SearchApplicationUserStatsIn"] = t.struct(
        {
            "sevenDaysActiveUsersCount": t.string().optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "oneDayActiveUsersCount": t.string().optional(),
            "thirtyDaysActiveUsersCount": t.string().optional(),
        }
    ).named(renames["SearchApplicationUserStatsIn"])
    types["SearchApplicationUserStatsOut"] = t.struct(
        {
            "sevenDaysActiveUsersCount": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "oneDayActiveUsersCount": t.string().optional(),
            "thirtyDaysActiveUsersCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchApplicationUserStatsOut"])
    types["EnterpriseTopazSidekickGenericAnswerCardIn"] = t.struct(
        {"title": t.string().optional(), "answer": t.string().optional()}
    ).named(renames["EnterpriseTopazSidekickGenericAnswerCardIn"])
    types["EnterpriseTopazSidekickGenericAnswerCardOut"] = t.struct(
        {
            "title": t.string().optional(),
            "answer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickGenericAnswerCardOut"])
    types["EnterpriseTopazSidekickMeetingNotesCardErrorIn"] = t.struct(
        {
            "event": t.proxy(
                renames["EnterpriseTopazSidekickAgendaEntryIn"]
            ).optional(),
            "description": t.string().optional(),
            "reason": t.string().optional(),
        }
    ).named(renames["EnterpriseTopazSidekickMeetingNotesCardErrorIn"])
    types["EnterpriseTopazSidekickMeetingNotesCardErrorOut"] = t.struct(
        {
            "event": t.proxy(
                renames["EnterpriseTopazSidekickAgendaEntryOut"]
            ).optional(),
            "description": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickMeetingNotesCardErrorOut"])
    types["ActionIn"] = t.struct(
        {"title": t.string().optional(), "url": t.string().optional()}
    ).named(renames["ActionIn"])
    types["ActionOut"] = t.struct(
        {
            "title": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionOut"])
    types["EnterpriseTopazSidekickAgendaGroupCardProtoContextIn"] = t.struct(
        {
            "context": t.string().optional(),
            "date": t.string().optional(),
            "eventsRestrict": t.string().optional(),
        }
    ).named(renames["EnterpriseTopazSidekickAgendaGroupCardProtoContextIn"])
    types["EnterpriseTopazSidekickAgendaGroupCardProtoContextOut"] = t.struct(
        {
            "context": t.string().optional(),
            "date": t.string().optional(),
            "eventsRestrict": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickAgendaGroupCardProtoContextOut"])
    types["ItemStatusIn"] = t.struct(
        {
            "code": t.string().optional(),
            "repositoryErrors": t.array(
                t.proxy(renames["RepositoryErrorIn"])
            ).optional(),
            "processingErrors": t.array(
                t.proxy(renames["ProcessingErrorIn"])
            ).optional(),
        }
    ).named(renames["ItemStatusIn"])
    types["ItemStatusOut"] = t.struct(
        {
            "code": t.string().optional(),
            "repositoryErrors": t.array(
                t.proxy(renames["RepositoryErrorOut"])
            ).optional(),
            "processingErrors": t.array(
                t.proxy(renames["ProcessingErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemStatusOut"])
    types["BooleanPropertyOptionsIn"] = t.struct(
        {"operatorOptions": t.proxy(renames["BooleanOperatorOptionsIn"]).optional()}
    ).named(renames["BooleanPropertyOptionsIn"])
    types["BooleanPropertyOptionsOut"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["BooleanOperatorOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BooleanPropertyOptionsOut"])
    types["EnterpriseTopazSidekickDocumentPerCategoryListIn"] = t.struct(
        {
            "documents": t.array(
                t.proxy(
                    renames[
                        "EnterpriseTopazSidekickDocumentPerCategoryListDocumentPerCategoryListEntryIn"
                    ]
                )
            ),
            "listType": t.string(),
            "responseMessage": t.string().optional(),
            "helpMessage": t.string().optional(),
            "listTypeDescription": t.string().optional(),
        }
    ).named(renames["EnterpriseTopazSidekickDocumentPerCategoryListIn"])
    types["EnterpriseTopazSidekickDocumentPerCategoryListOut"] = t.struct(
        {
            "documents": t.array(
                t.proxy(
                    renames[
                        "EnterpriseTopazSidekickDocumentPerCategoryListDocumentPerCategoryListEntryOut"
                    ]
                )
            ),
            "listType": t.string(),
            "responseMessage": t.string().optional(),
            "helpMessage": t.string().optional(),
            "listTypeDescription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickDocumentPerCategoryListOut"])
    types["TextPropertyOptionsIn"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["TextOperatorOptionsIn"]).optional(),
            "retrievalImportance": t.proxy(renames["RetrievalImportanceIn"]).optional(),
        }
    ).named(renames["TextPropertyOptionsIn"])
    types["TextPropertyOptionsOut"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["TextOperatorOptionsOut"]).optional(),
            "retrievalImportance": t.proxy(
                renames["RetrievalImportanceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextPropertyOptionsOut"])
    types["CustomerQueryStatsIn"] = t.struct(
        {
            "queryCountByStatus": t.array(t.proxy(renames["QueryCountByStatusIn"])),
            "date": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["CustomerQueryStatsIn"])
    types["CustomerQueryStatsOut"] = t.struct(
        {
            "queryCountByStatus": t.array(t.proxy(renames["QueryCountByStatusOut"])),
            "date": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerQueryStatsOut"])
    types["DriveLocationRestrictIn"] = t.struct({"type": t.string()}).named(
        renames["DriveLocationRestrictIn"]
    )
    types["DriveLocationRestrictOut"] = t.struct(
        {"type": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DriveLocationRestrictOut"])
    types["ShareScopeIn"] = t.struct(
        {"domain": t.string().optional(), "scope": t.string().optional()}
    ).named(renames["ShareScopeIn"])
    types["ShareScopeOut"] = t.struct(
        {
            "domain": t.string().optional(),
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShareScopeOut"])
    types["CustomerIndexStatsIn"] = t.struct(
        {
            "itemCountByStatus": t.array(
                t.proxy(renames["ItemCountByStatusIn"])
            ).optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["CustomerIndexStatsIn"])
    types["CustomerIndexStatsOut"] = t.struct(
        {
            "itemCountByStatus": t.array(
                t.proxy(renames["ItemCountByStatusOut"])
            ).optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerIndexStatsOut"])
    types["MetalineIn"] = t.struct(
        {"properties": t.array(t.proxy(renames["DisplayedPropertyIn"])).optional()}
    ).named(renames["MetalineIn"])
    types["MetalineOut"] = t.struct(
        {
            "properties": t.array(t.proxy(renames["DisplayedPropertyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetalineOut"])
    types["QueryItemIn"] = t.struct({"isSynthetic": t.boolean().optional()}).named(
        renames["QueryItemIn"]
    )
    types["QueryItemOut"] = t.struct(
        {
            "isSynthetic": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryItemOut"])
    types["MapTileIn"] = t.struct(
        {
            "imageUrl": t.proxy(renames["SafeUrlProtoIn"]).optional(),
            "tileY": t.number().optional(),
            "tileX": t.number().optional(),
        }
    ).named(renames["MapTileIn"])
    types["MapTileOut"] = t.struct(
        {
            "imageUrl": t.proxy(renames["SafeUrlProtoOut"]).optional(),
            "tileY": t.number().optional(),
            "tileX": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MapTileOut"])
    types["EnterpriseTopazFrontendTeamsPersonCorePhoneNumberIn"] = t.struct(
        {
            "phoneUrl": t.proxy(renames["SafeUrlProtoIn"]).optional(),
            "phoneNumber": t.string().optional(),
            "type": t.string(),
        }
    ).named(renames["EnterpriseTopazFrontendTeamsPersonCorePhoneNumberIn"])
    types["EnterpriseTopazFrontendTeamsPersonCorePhoneNumberOut"] = t.struct(
        {
            "phoneUrl": t.proxy(renames["SafeUrlProtoOut"]).optional(),
            "phoneNumber": t.string().optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazFrontendTeamsPersonCorePhoneNumberOut"])
    types["InitializeCustomerRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["InitializeCustomerRequestIn"]
    )
    types["InitializeCustomerRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InitializeCustomerRequestOut"])
    types["SafeHtmlProtoIn"] = t.struct(
        {"privateDoNotAccessOrElseSafeHtmlWrappedValue": t.string().optional()}
    ).named(renames["SafeHtmlProtoIn"])
    types["SafeHtmlProtoOut"] = t.struct(
        {
            "privateDoNotAccessOrElseSafeHtmlWrappedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SafeHtmlProtoOut"])
    types["IntegerValuesIn"] = t.struct({"values": t.array(t.string())}).named(
        renames["IntegerValuesIn"]
    )
    types["IntegerValuesOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerValuesOut"])
    types["ListDataSourceResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sources": t.array(t.proxy(renames["DataSourceIn"])),
        }
    ).named(renames["ListDataSourceResponseIn"])
    types["ListDataSourceResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sources": t.array(t.proxy(renames["DataSourceOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDataSourceResponseOut"])
    types["PollItemsRequestIn"] = t.struct(
        {
            "statusCodes": t.array(t.string()).optional(),
            "queue": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "limit": t.integer().optional(),
            "connectorName": t.string().optional(),
        }
    ).named(renames["PollItemsRequestIn"])
    types["PollItemsRequestOut"] = t.struct(
        {
            "statusCodes": t.array(t.string()).optional(),
            "queue": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "limit": t.integer().optional(),
            "connectorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PollItemsRequestOut"])
    types["QueryInterpretationConfigIn"] = t.struct(
        {
            "forceDisableSupplementalResults": t.boolean().optional(),
            "forceVerbatimMode": t.boolean().optional(),
        }
    ).named(renames["QueryInterpretationConfigIn"])
    types["QueryInterpretationConfigOut"] = t.struct(
        {
            "forceDisableSupplementalResults": t.boolean().optional(),
            "forceVerbatimMode": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryInterpretationConfigOut"])
    types["RestrictItemIn"] = t.struct(
        {
            "driveLocationRestrict": t.proxy(renames["DriveLocationRestrictIn"]),
            "driveTimeSpanRestrict": t.proxy(renames["DriveTimeSpanRestrictIn"]),
            "driveMimeTypeRestrict": t.proxy(
                renames["DriveMimeTypeRestrictIn"]
            ).optional(),
            "searchOperator": t.string().optional(),
            "driveFollowUpRestrict": t.proxy(renames["DriveFollowUpRestrictIn"]),
        }
    ).named(renames["RestrictItemIn"])
    types["RestrictItemOut"] = t.struct(
        {
            "driveLocationRestrict": t.proxy(renames["DriveLocationRestrictOut"]),
            "driveTimeSpanRestrict": t.proxy(renames["DriveTimeSpanRestrictOut"]),
            "driveMimeTypeRestrict": t.proxy(
                renames["DriveMimeTypeRestrictOut"]
            ).optional(),
            "searchOperator": t.string().optional(),
            "driveFollowUpRestrict": t.proxy(renames["DriveFollowUpRestrictOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestrictItemOut"])
    types["ProcessingErrorIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "fieldViolations": t.array(t.proxy(renames["FieldViolationIn"])).optional(),
            "code": t.string().optional(),
        }
    ).named(renames["ProcessingErrorIn"])
    types["ProcessingErrorOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "fieldViolations": t.array(
                t.proxy(renames["FieldViolationOut"])
            ).optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProcessingErrorOut"])
    types["GetCustomerQueryStatsResponseIn"] = t.struct(
        {
            "totalQueryCount": t.string().optional(),
            "stats": t.array(t.proxy(renames["CustomerQueryStatsIn"])),
        }
    ).named(renames["GetCustomerQueryStatsResponseIn"])
    types["GetCustomerQueryStatsResponseOut"] = t.struct(
        {
            "totalQueryCount": t.string().optional(),
            "stats": t.array(t.proxy(renames["CustomerQueryStatsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetCustomerQueryStatsResponseOut"])
    types["BooleanOperatorOptionsIn"] = t.struct(
        {"operatorName": t.string().optional()}
    ).named(renames["BooleanOperatorOptionsIn"])
    types["BooleanOperatorOptionsOut"] = t.struct(
        {
            "operatorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BooleanOperatorOptionsOut"])
    types["SuggestResultIn"] = t.struct(
        {
            "source": t.proxy(renames["SourceIn"]).optional(),
            "querySuggestion": t.proxy(renames["QuerySuggestionIn"]).optional(),
            "suggestedQuery": t.string().optional(),
            "peopleSuggestion": t.proxy(renames["PeopleSuggestionIn"]).optional(),
        }
    ).named(renames["SuggestResultIn"])
    types["SuggestResultOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "querySuggestion": t.proxy(renames["QuerySuggestionOut"]).optional(),
            "suggestedQuery": t.string().optional(),
            "peopleSuggestion": t.proxy(renames["PeopleSuggestionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestResultOut"])
    types["EnterpriseTopazSidekickPersonalizedDocsCardProtoIn"] = t.struct(
        {
            "documentGroup": t.array(
                t.proxy(renames["EnterpriseTopazSidekickDocumentGroupIn"])
            ).optional()
        }
    ).named(renames["EnterpriseTopazSidekickPersonalizedDocsCardProtoIn"])
    types["EnterpriseTopazSidekickPersonalizedDocsCardProtoOut"] = t.struct(
        {
            "documentGroup": t.array(
                t.proxy(renames["EnterpriseTopazSidekickDocumentGroupOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickPersonalizedDocsCardProtoOut"])
    types["GetCustomerSessionStatsResponseIn"] = t.struct(
        {"stats": t.array(t.proxy(renames["CustomerSessionStatsIn"]))}
    ).named(renames["GetCustomerSessionStatsResponseIn"])
    types["GetCustomerSessionStatsResponseOut"] = t.struct(
        {
            "stats": t.array(t.proxy(renames["CustomerSessionStatsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetCustomerSessionStatsResponseOut"])
    types["EnterpriseTopazSidekickCommonPersonBirthdayIn"] = t.struct(
        {"value": t.string().optional()}
    ).named(renames["EnterpriseTopazSidekickCommonPersonBirthdayIn"])
    types["EnterpriseTopazSidekickCommonPersonBirthdayOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseTopazSidekickCommonPersonBirthdayOut"])
    types["SearchItemsByViewUrlRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "viewUrl": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
        }
    ).named(renames["SearchItemsByViewUrlRequestIn"])
    types["SearchItemsByViewUrlRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "viewUrl": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchItemsByViewUrlRequestOut"])
    types["SourceScoringConfigIn"] = t.struct(
        {"sourceImportance": t.string().optional()}
    ).named(renames["SourceScoringConfigIn"])
    types["SourceScoringConfigOut"] = t.struct(
        {
            "sourceImportance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceScoringConfigOut"])
    types["DoublePropertyOptionsIn"] = t.struct(
        {"operatorOptions": t.proxy(renames["DoubleOperatorOptionsIn"]).optional()}
    ).named(renames["DoublePropertyOptionsIn"])
    types["DoublePropertyOptionsOut"] = t.struct(
        {
            "operatorOptions": t.proxy(renames["DoubleOperatorOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoublePropertyOptionsOut"])
    types["ListItemNamesForUnmappedIdentityResponseIn"] = t.struct(
        {"nextPageToken": t.string().optional(), "itemNames": t.array(t.string())}
    ).named(renames["ListItemNamesForUnmappedIdentityResponseIn"])
    types["ListItemNamesForUnmappedIdentityResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "itemNames": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListItemNamesForUnmappedIdentityResponseOut"])
    types["FacetResultIn"] = t.struct(
        {
            "objectType": t.string().optional(),
            "sourceName": t.string().optional(),
            "operatorName": t.string().optional(),
            "buckets": t.array(t.proxy(renames["FacetBucketIn"])).optional(),
        }
    ).named(renames["FacetResultIn"])
    types["FacetResultOut"] = t.struct(
        {
            "objectType": t.string().optional(),
            "sourceName": t.string().optional(),
            "operatorName": t.string().optional(),
            "buckets": t.array(t.proxy(renames["FacetBucketOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FacetResultOut"])

    functions = {}
    functions["operationsGet"] = cloudsearch.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsLroList"] = cloudsearch.get(
        "v1/{name}/lro",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesUpdateSchema"] = cloudsearch.delete(
        "v1/indexing/{name}/schema",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesGetSchema"] = cloudsearch.delete(
        "v1/indexing/{name}/schema",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesDeleteSchema"] = cloudsearch.delete(
        "v1/indexing/{name}/schema",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsList"] = cloudsearch.post(
        "v1/indexing/{name}/items:deleteQueueItems",
        t.struct(
            {
                "name": t.string().optional(),
                "connectorName": t.string().optional(),
                "queue": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsUpload"] = cloudsearch.post(
        "v1/indexing/{name}/items:deleteQueueItems",
        t.struct(
            {
                "name": t.string().optional(),
                "connectorName": t.string().optional(),
                "queue": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsGet"] = cloudsearch.post(
        "v1/indexing/{name}/items:deleteQueueItems",
        t.struct(
            {
                "name": t.string().optional(),
                "connectorName": t.string().optional(),
                "queue": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsIndex"] = cloudsearch.post(
        "v1/indexing/{name}/items:deleteQueueItems",
        t.struct(
            {
                "name": t.string().optional(),
                "connectorName": t.string().optional(),
                "queue": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsPush"] = cloudsearch.post(
        "v1/indexing/{name}/items:deleteQueueItems",
        t.struct(
            {
                "name": t.string().optional(),
                "connectorName": t.string().optional(),
                "queue": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsPoll"] = cloudsearch.post(
        "v1/indexing/{name}/items:deleteQueueItems",
        t.struct(
            {
                "name": t.string().optional(),
                "connectorName": t.string().optional(),
                "queue": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsDelete"] = cloudsearch.post(
        "v1/indexing/{name}/items:deleteQueueItems",
        t.struct(
            {
                "name": t.string().optional(),
                "connectorName": t.string().optional(),
                "queue": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsUnreserve"] = cloudsearch.post(
        "v1/indexing/{name}/items:deleteQueueItems",
        t.struct(
            {
                "name": t.string().optional(),
                "connectorName": t.string().optional(),
                "queue": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["indexingDatasourcesItemsDeleteQueueItems"] = cloudsearch.post(
        "v1/indexing/{name}/items:deleteQueueItems",
        t.struct(
            {
                "name": t.string().optional(),
                "connectorName": t.string().optional(),
                "queue": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mediaUpload"] = cloudsearch.post(
        "v1/media/{resourceName}",
        t.struct(
            {"resourceName": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["MediaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["querySearch"] = cloudsearch.post(
        "v1/query/suggest",
        t.struct(
            {
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "dataSourceRestrictions": t.array(
                    t.proxy(renames["DataSourceRestrictionIn"])
                ).optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SuggestResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["queryRemoveActivity"] = cloudsearch.post(
        "v1/query/suggest",
        t.struct(
            {
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "dataSourceRestrictions": t.array(
                    t.proxy(renames["DataSourceRestrictionIn"])
                ).optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SuggestResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["querySuggest"] = cloudsearch.post(
        "v1/query/suggest",
        t.struct(
            {
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "dataSourceRestrictions": t.array(
                    t.proxy(renames["DataSourceRestrictionIn"])
                ).optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SuggestResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["querySourcesList"] = cloudsearch.get(
        "v1/query/sources",
        t.struct(
            {
                "requestOptions.timeZone": t.string().optional(),
                "requestOptions.debugOptions.enableDebugging": t.boolean().optional(),
                "requestOptions.searchApplicationId": t.string().optional(),
                "pageToken": t.string().optional(),
                "requestOptions.languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListQuerySourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1InitializeCustomer"] = cloudsearch.post(
        "v1:initializeCustomer",
        t.struct({"_": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsGetCustomer"] = cloudsearch.patch(
        "v1/settings/customer",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "vpcSettings": t.proxy(renames["VPCSettingsIn"]).optional(),
                "auditLoggingSettings": t.proxy(
                    renames["AuditLoggingSettingsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsUpdateCustomer"] = cloudsearch.patch(
        "v1/settings/customer",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "vpcSettings": t.proxy(renames["VPCSettingsIn"]).optional(),
                "auditLoggingSettings": t.proxy(
                    renames["AuditLoggingSettingsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesGet"] = cloudsearch.post(
        "v1/settings/datasources",
        t.struct(
            {
                "operationIds": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "displayName": t.string(),
                "indexingServiceAccounts": t.array(t.string()).optional(),
                "itemsVisibility": t.array(
                    t.proxy(renames["GSuitePrincipalIn"])
                ).optional(),
                "shortName": t.string().optional(),
                "disableServing": t.boolean().optional(),
                "disableModifications": t.boolean().optional(),
                "returnThumbnailUrls": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesDelete"] = cloudsearch.post(
        "v1/settings/datasources",
        t.struct(
            {
                "operationIds": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "displayName": t.string(),
                "indexingServiceAccounts": t.array(t.string()).optional(),
                "itemsVisibility": t.array(
                    t.proxy(renames["GSuitePrincipalIn"])
                ).optional(),
                "shortName": t.string().optional(),
                "disableServing": t.boolean().optional(),
                "disableModifications": t.boolean().optional(),
                "returnThumbnailUrls": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesList"] = cloudsearch.post(
        "v1/settings/datasources",
        t.struct(
            {
                "operationIds": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "displayName": t.string(),
                "indexingServiceAccounts": t.array(t.string()).optional(),
                "itemsVisibility": t.array(
                    t.proxy(renames["GSuitePrincipalIn"])
                ).optional(),
                "shortName": t.string().optional(),
                "disableServing": t.boolean().optional(),
                "disableModifications": t.boolean().optional(),
                "returnThumbnailUrls": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesPatch"] = cloudsearch.post(
        "v1/settings/datasources",
        t.struct(
            {
                "operationIds": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "displayName": t.string(),
                "indexingServiceAccounts": t.array(t.string()).optional(),
                "itemsVisibility": t.array(
                    t.proxy(renames["GSuitePrincipalIn"])
                ).optional(),
                "shortName": t.string().optional(),
                "disableServing": t.boolean().optional(),
                "disableModifications": t.boolean().optional(),
                "returnThumbnailUrls": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesUpdate"] = cloudsearch.post(
        "v1/settings/datasources",
        t.struct(
            {
                "operationIds": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "displayName": t.string(),
                "indexingServiceAccounts": t.array(t.string()).optional(),
                "itemsVisibility": t.array(
                    t.proxy(renames["GSuitePrincipalIn"])
                ).optional(),
                "shortName": t.string().optional(),
                "disableServing": t.boolean().optional(),
                "disableModifications": t.boolean().optional(),
                "returnThumbnailUrls": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsDatasourcesCreate"] = cloudsearch.post(
        "v1/settings/datasources",
        t.struct(
            {
                "operationIds": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "displayName": t.string(),
                "indexingServiceAccounts": t.array(t.string()).optional(),
                "itemsVisibility": t.array(
                    t.proxy(renames["GSuitePrincipalIn"])
                ).optional(),
                "shortName": t.string().optional(),
                "disableServing": t.boolean().optional(),
                "disableModifications": t.boolean().optional(),
                "returnThumbnailUrls": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsCreate"] = cloudsearch.post(
        "v1/settings/{name}:reset",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsUpdate"] = cloudsearch.post(
        "v1/settings/{name}:reset",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsList"] = cloudsearch.post(
        "v1/settings/{name}:reset",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsPatch"] = cloudsearch.post(
        "v1/settings/{name}:reset",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsGet"] = cloudsearch.post(
        "v1/settings/{name}:reset",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsDelete"] = cloudsearch.post(
        "v1/settings/{name}:reset",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsSearchapplicationsReset"] = cloudsearch.post(
        "v1/settings/{name}:reset",
        t.struct(
            {
                "name": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debugIdentitysourcesUnmappedidsList"] = cloudsearch.get(
        "v1/debug/{parent}/unmappedids",
        t.struct(
            {
                "resolutionStatusCode": t.string().optional(),
                "pageToken": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUnmappedIdentitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debugIdentitysourcesItemsListForunmappedidentity"] = cloudsearch.get(
        "v1/debug/{parent}/items:forunmappedidentity",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "userResourceName": t.string(),
                "pageSize": t.integer().optional(),
                "groupResourceName": t.string(),
                "parent": t.string().optional(),
                "debugOptions.enableDebugging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListItemNamesForUnmappedIdentityResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debugDatasourcesItemsCheckAccess"] = cloudsearch.post(
        "v1/debug/{name}/items:searchByViewUrl",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "viewUrl": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchItemsByViewUrlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debugDatasourcesItemsSearchByViewUrl"] = cloudsearch.post(
        "v1/debug/{name}/items:searchByViewUrl",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "viewUrl": t.string().optional(),
                "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchItemsByViewUrlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debugDatasourcesItemsUnmappedidsList"] = cloudsearch.get(
        "v1/debug/{parent}/unmappedids",
        t.struct(
            {
                "debugOptions.enableDebugging": t.boolean().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUnmappedIdentitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGetIndex"] = cloudsearch.get(
        "v1/stats/session",
        t.struct(
            {
                "fromDate.year": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerSessionStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGetUser"] = cloudsearch.get(
        "v1/stats/session",
        t.struct(
            {
                "fromDate.year": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerSessionStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGetQuery"] = cloudsearch.get(
        "v1/stats/session",
        t.struct(
            {
                "fromDate.year": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerSessionStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGetSearchapplication"] = cloudsearch.get(
        "v1/stats/session",
        t.struct(
            {
                "fromDate.year": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerSessionStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsGetSession"] = cloudsearch.get(
        "v1/stats/session",
        t.struct(
            {
                "fromDate.year": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetCustomerSessionStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsSessionSearchapplicationsGet"] = cloudsearch.get(
        "v1/stats/session/{name}",
        t.struct(
            {
                "toDate.day": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetSearchApplicationSessionStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsQuerySearchapplicationsGet"] = cloudsearch.get(
        "v1/stats/query/{name}",
        t.struct(
            {
                "fromDate.month": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "name": t.string().optional(),
                "fromDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetSearchApplicationQueryStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsUserSearchapplicationsGet"] = cloudsearch.get(
        "v1/stats/user/{name}",
        t.struct(
            {
                "toDate.year": t.integer().optional(),
                "name": t.string().optional(),
                "toDate.month": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "fromDate.month": t.integer().optional(),
                "fromDate.year": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetSearchApplicationUserStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statsIndexDatasourcesGet"] = cloudsearch.get(
        "v1/stats/index/{name}",
        t.struct(
            {
                "fromDate.month": t.integer().optional(),
                "fromDate.day": t.integer().optional(),
                "toDate.month": t.integer().optional(),
                "toDate.year": t.integer().optional(),
                "toDate.day": t.integer().optional(),
                "name": t.string().optional(),
                "fromDate.year": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetDataSourceIndexStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudsearch",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
