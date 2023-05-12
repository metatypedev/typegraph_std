from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_healthcare() -> Import:
    healthcare = HTTPRuntime("https://healthcare.googleapis.com/")

    renames = {
        "ErrorResponse": "_healthcare_1_ErrorResponse",
        "ParsedDataIn": "_healthcare_2_ParsedDataIn",
        "ParsedDataOut": "_healthcare_3_ParsedDataOut",
        "FhirStoreMetricsIn": "_healthcare_4_FhirStoreMetricsIn",
        "FhirStoreMetricsOut": "_healthcare_5_FhirStoreMetricsOut",
        "SetIamPolicyRequestIn": "_healthcare_6_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_healthcare_7_SetIamPolicyRequestOut",
        "TestIamPermissionsRequestIn": "_healthcare_8_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_healthcare_9_TestIamPermissionsRequestOut",
        "DeidentifyDicomStoreRequestIn": "_healthcare_10_DeidentifyDicomStoreRequestIn",
        "DeidentifyDicomStoreRequestOut": "_healthcare_11_DeidentifyDicomStoreRequestOut",
        "Hl7TypesConfigIn": "_healthcare_12_Hl7TypesConfigIn",
        "Hl7TypesConfigOut": "_healthcare_13_Hl7TypesConfigOut",
        "InfoTypeTransformationIn": "_healthcare_14_InfoTypeTransformationIn",
        "InfoTypeTransformationOut": "_healthcare_15_InfoTypeTransformationOut",
        "CryptoHashConfigIn": "_healthcare_16_CryptoHashConfigIn",
        "CryptoHashConfigOut": "_healthcare_17_CryptoHashConfigOut",
        "EvaluateUserConsentsRequestIn": "_healthcare_18_EvaluateUserConsentsRequestIn",
        "EvaluateUserConsentsRequestOut": "_healthcare_19_EvaluateUserConsentsRequestOut",
        "ImportResourcesRequestIn": "_healthcare_20_ImportResourcesRequestIn",
        "ImportResourcesRequestOut": "_healthcare_21_ImportResourcesRequestOut",
        "SignatureIn": "_healthcare_22_SignatureIn",
        "SignatureOut": "_healthcare_23_SignatureOut",
        "GoogleCloudHealthcareV1DicomGcsSourceIn": "_healthcare_24_GoogleCloudHealthcareV1DicomGcsSourceIn",
        "GoogleCloudHealthcareV1DicomGcsSourceOut": "_healthcare_25_GoogleCloudHealthcareV1DicomGcsSourceOut",
        "KmsWrappedCryptoKeyIn": "_healthcare_26_KmsWrappedCryptoKeyIn",
        "KmsWrappedCryptoKeyOut": "_healthcare_27_KmsWrappedCryptoKeyOut",
        "ListMessagesResponseIn": "_healthcare_28_ListMessagesResponseIn",
        "ListMessagesResponseOut": "_healthcare_29_ListMessagesResponseOut",
        "ConsentEvaluationIn": "_healthcare_30_ConsentEvaluationIn",
        "ConsentEvaluationOut": "_healthcare_31_ConsentEvaluationOut",
        "ExprIn": "_healthcare_32_ExprIn",
        "ExprOut": "_healthcare_33_ExprOut",
        "EntityMentionIn": "_healthcare_34_EntityMentionIn",
        "EntityMentionOut": "_healthcare_35_EntityMentionOut",
        "CheckDataAccessRequestIn": "_healthcare_36_CheckDataAccessRequestIn",
        "CheckDataAccessRequestOut": "_healthcare_37_CheckDataAccessRequestOut",
        "ListDatasetsResponseIn": "_healthcare_38_ListDatasetsResponseIn",
        "ListDatasetsResponseOut": "_healthcare_39_ListDatasetsResponseOut",
        "OperationMetadataIn": "_healthcare_40_OperationMetadataIn",
        "OperationMetadataOut": "_healthcare_41_OperationMetadataOut",
        "SchematizedDataIn": "_healthcare_42_SchematizedDataIn",
        "SchematizedDataOut": "_healthcare_43_SchematizedDataOut",
        "CreateMessageRequestIn": "_healthcare_44_CreateMessageRequestIn",
        "CreateMessageRequestOut": "_healthcare_45_CreateMessageRequestOut",
        "Hl7SchemaConfigIn": "_healthcare_46_Hl7SchemaConfigIn",
        "Hl7SchemaConfigOut": "_healthcare_47_Hl7SchemaConfigOut",
        "EntityIn": "_healthcare_48_EntityIn",
        "EntityOut": "_healthcare_49_EntityOut",
        "AuditConfigIn": "_healthcare_50_AuditConfigIn",
        "AuditConfigOut": "_healthcare_51_AuditConfigOut",
        "GcsDestinationIn": "_healthcare_52_GcsDestinationIn",
        "GcsDestinationOut": "_healthcare_53_GcsDestinationOut",
        "DicomConfigIn": "_healthcare_54_DicomConfigIn",
        "DicomConfigOut": "_healthcare_55_DicomConfigOut",
        "StatusIn": "_healthcare_56_StatusIn",
        "StatusOut": "_healthcare_57_StatusOut",
        "EmptyIn": "_healthcare_58_EmptyIn",
        "EmptyOut": "_healthcare_59_EmptyOut",
        "FhirFilterIn": "_healthcare_60_FhirFilterIn",
        "FhirFilterOut": "_healthcare_61_FhirFilterOut",
        "ExportMessagesResponseIn": "_healthcare_62_ExportMessagesResponseIn",
        "ExportMessagesResponseOut": "_healthcare_63_ExportMessagesResponseOut",
        "ImportDicomDataResponseIn": "_healthcare_64_ImportDicomDataResponseIn",
        "ImportDicomDataResponseOut": "_healthcare_65_ImportDicomDataResponseOut",
        "RevokeConsentRequestIn": "_healthcare_66_RevokeConsentRequestIn",
        "RevokeConsentRequestOut": "_healthcare_67_RevokeConsentRequestOut",
        "NotificationConfigIn": "_healthcare_68_NotificationConfigIn",
        "NotificationConfigOut": "_healthcare_69_NotificationConfigOut",
        "SchemaConfigIn": "_healthcare_70_SchemaConfigIn",
        "SchemaConfigOut": "_healthcare_71_SchemaConfigOut",
        "DeidentifyFhirStoreRequestIn": "_healthcare_72_DeidentifyFhirStoreRequestIn",
        "DeidentifyFhirStoreRequestOut": "_healthcare_73_DeidentifyFhirStoreRequestOut",
        "ConsentStoreIn": "_healthcare_74_ConsentStoreIn",
        "ConsentStoreOut": "_healthcare_75_ConsentStoreOut",
        "GroupOrSegmentIn": "_healthcare_76_GroupOrSegmentIn",
        "GroupOrSegmentOut": "_healthcare_77_GroupOrSegmentOut",
        "GoogleCloudHealthcareV1DicomBigQueryDestinationIn": "_healthcare_78_GoogleCloudHealthcareV1DicomBigQueryDestinationIn",
        "GoogleCloudHealthcareV1DicomBigQueryDestinationOut": "_healthcare_79_GoogleCloudHealthcareV1DicomBigQueryDestinationOut",
        "ActivateConsentRequestIn": "_healthcare_80_ActivateConsentRequestIn",
        "ActivateConsentRequestOut": "_healthcare_81_ActivateConsentRequestOut",
        "ResultIn": "_healthcare_82_ResultIn",
        "ResultOut": "_healthcare_83_ResultOut",
        "ArchiveUserDataMappingResponseIn": "_healthcare_84_ArchiveUserDataMappingResponseIn",
        "ArchiveUserDataMappingResponseOut": "_healthcare_85_ArchiveUserDataMappingResponseOut",
        "AnalyzeEntitiesRequestIn": "_healthcare_86_AnalyzeEntitiesRequestIn",
        "AnalyzeEntitiesRequestOut": "_healthcare_87_AnalyzeEntitiesRequestOut",
        "MessageIn": "_healthcare_88_MessageIn",
        "MessageOut": "_healthcare_89_MessageOut",
        "StreamConfigIn": "_healthcare_90_StreamConfigIn",
        "StreamConfigOut": "_healthcare_91_StreamConfigOut",
        "GoogleCloudHealthcareV1FhirBigQueryDestinationIn": "_healthcare_92_GoogleCloudHealthcareV1FhirBigQueryDestinationIn",
        "GoogleCloudHealthcareV1FhirBigQueryDestinationOut": "_healthcare_93_GoogleCloudHealthcareV1FhirBigQueryDestinationOut",
        "Hl7V2StoreIn": "_healthcare_94_Hl7V2StoreIn",
        "Hl7V2StoreOut": "_healthcare_95_Hl7V2StoreOut",
        "TypeIn": "_healthcare_96_TypeIn",
        "TypeOut": "_healthcare_97_TypeOut",
        "ProgressCounterIn": "_healthcare_98_ProgressCounterIn",
        "ProgressCounterOut": "_healthcare_99_ProgressCounterOut",
        "SearchResourcesRequestIn": "_healthcare_100_SearchResourcesRequestIn",
        "SearchResourcesRequestOut": "_healthcare_101_SearchResourcesRequestOut",
        "FhirStoreIn": "_healthcare_102_FhirStoreIn",
        "FhirStoreOut": "_healthcare_103_FhirStoreOut",
        "ExportDicomDataResponseIn": "_healthcare_104_ExportDicomDataResponseIn",
        "ExportDicomDataResponseOut": "_healthcare_105_ExportDicomDataResponseOut",
        "VersionSourceIn": "_healthcare_106_VersionSourceIn",
        "VersionSourceOut": "_healthcare_107_VersionSourceOut",
        "ListFhirStoresResponseIn": "_healthcare_108_ListFhirStoresResponseIn",
        "ListFhirStoresResponseOut": "_healthcare_109_ListFhirStoresResponseOut",
        "SegmentIn": "_healthcare_110_SegmentIn",
        "SegmentOut": "_healthcare_111_SegmentOut",
        "DeidentifyDatasetRequestIn": "_healthcare_112_DeidentifyDatasetRequestIn",
        "DeidentifyDatasetRequestOut": "_healthcare_113_DeidentifyDatasetRequestOut",
        "TextSpanIn": "_healthcare_114_TextSpanIn",
        "TextSpanOut": "_healthcare_115_TextSpanOut",
        "TimePartitioningIn": "_healthcare_116_TimePartitioningIn",
        "TimePartitioningOut": "_healthcare_117_TimePartitioningOut",
        "FieldMetadataIn": "_healthcare_118_FieldMetadataIn",
        "FieldMetadataOut": "_healthcare_119_FieldMetadataOut",
        "TagFilterListIn": "_healthcare_120_TagFilterListIn",
        "TagFilterListOut": "_healthcare_121_TagFilterListOut",
        "DicomStoreIn": "_healthcare_122_DicomStoreIn",
        "DicomStoreOut": "_healthcare_123_DicomStoreOut",
        "ConsentListIn": "_healthcare_124_ConsentListIn",
        "ConsentListOut": "_healthcare_125_ConsentListOut",
        "LinkedEntityIn": "_healthcare_126_LinkedEntityIn",
        "LinkedEntityOut": "_healthcare_127_LinkedEntityOut",
        "ConsentIn": "_healthcare_128_ConsentIn",
        "ConsentOut": "_healthcare_129_ConsentOut",
        "GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryIn": "_healthcare_130_GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryIn",
        "GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryOut": "_healthcare_131_GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryOut",
        "ConsentArtifactIn": "_healthcare_132_ConsentArtifactIn",
        "ConsentArtifactOut": "_healthcare_133_ConsentArtifactOut",
        "Hl7V2NotificationConfigIn": "_healthcare_134_Hl7V2NotificationConfigIn",
        "Hl7V2NotificationConfigOut": "_healthcare_135_Hl7V2NotificationConfigOut",
        "ListUserDataMappingsResponseIn": "_healthcare_136_ListUserDataMappingsResponseIn",
        "ListUserDataMappingsResponseOut": "_healthcare_137_ListUserDataMappingsResponseOut",
        "CharacterMaskConfigIn": "_healthcare_138_CharacterMaskConfigIn",
        "CharacterMaskConfigOut": "_healthcare_139_CharacterMaskConfigOut",
        "BindingIn": "_healthcare_140_BindingIn",
        "BindingOut": "_healthcare_141_BindingOut",
        "FhirNotificationConfigIn": "_healthcare_142_FhirNotificationConfigIn",
        "FhirNotificationConfigOut": "_healthcare_143_FhirNotificationConfigOut",
        "GcsSourceIn": "_healthcare_144_GcsSourceIn",
        "GcsSourceOut": "_healthcare_145_GcsSourceOut",
        "ResourcesIn": "_healthcare_146_ResourcesIn",
        "ResourcesOut": "_healthcare_147_ResourcesOut",
        "GoogleCloudHealthcareV1DicomGcsDestinationIn": "_healthcare_148_GoogleCloudHealthcareV1DicomGcsDestinationIn",
        "GoogleCloudHealthcareV1DicomGcsDestinationOut": "_healthcare_149_GoogleCloudHealthcareV1DicomGcsDestinationOut",
        "ListHl7V2StoresResponseIn": "_healthcare_150_ListHl7V2StoresResponseIn",
        "ListHl7V2StoresResponseOut": "_healthcare_151_ListHl7V2StoresResponseOut",
        "ListConsentsResponseIn": "_healthcare_152_ListConsentsResponseIn",
        "ListConsentsResponseOut": "_healthcare_153_ListConsentsResponseOut",
        "ArchiveUserDataMappingRequestIn": "_healthcare_154_ArchiveUserDataMappingRequestIn",
        "ArchiveUserDataMappingRequestOut": "_healthcare_155_ArchiveUserDataMappingRequestOut",
        "LocationIn": "_healthcare_156_LocationIn",
        "LocationOut": "_healthcare_157_LocationOut",
        "SchemaPackageIn": "_healthcare_158_SchemaPackageIn",
        "SchemaPackageOut": "_healthcare_159_SchemaPackageOut",
        "DeidentifiedStoreDestinationIn": "_healthcare_160_DeidentifiedStoreDestinationIn",
        "DeidentifiedStoreDestinationOut": "_healthcare_161_DeidentifiedStoreDestinationOut",
        "GoogleCloudHealthcareV1ConsentPolicyIn": "_healthcare_162_GoogleCloudHealthcareV1ConsentPolicyIn",
        "GoogleCloudHealthcareV1ConsentPolicyOut": "_healthcare_163_GoogleCloudHealthcareV1ConsentPolicyOut",
        "HttpBodyIn": "_healthcare_164_HttpBodyIn",
        "HttpBodyOut": "_healthcare_165_HttpBodyOut",
        "IngestMessageRequestIn": "_healthcare_166_IngestMessageRequestIn",
        "IngestMessageRequestOut": "_healthcare_167_IngestMessageRequestOut",
        "AttributeDefinitionIn": "_healthcare_168_AttributeDefinitionIn",
        "AttributeDefinitionOut": "_healthcare_169_AttributeDefinitionOut",
        "IngestMessageResponseIn": "_healthcare_170_IngestMessageResponseIn",
        "IngestMessageResponseOut": "_healthcare_171_IngestMessageResponseOut",
        "ExportResourcesRequestIn": "_healthcare_172_ExportResourcesRequestIn",
        "ExportResourcesRequestOut": "_healthcare_173_ExportResourcesRequestOut",
        "ImportDicomDataRequestIn": "_healthcare_174_ImportDicomDataRequestIn",
        "ImportDicomDataRequestOut": "_healthcare_175_ImportDicomDataRequestOut",
        "TestIamPermissionsResponseIn": "_healthcare_176_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_healthcare_177_TestIamPermissionsResponseOut",
        "ImageConfigIn": "_healthcare_178_ImageConfigIn",
        "ImageConfigOut": "_healthcare_179_ImageConfigOut",
        "GoogleCloudHealthcareV1FhirGcsSourceIn": "_healthcare_180_GoogleCloudHealthcareV1FhirGcsSourceIn",
        "GoogleCloudHealthcareV1FhirGcsSourceOut": "_healthcare_181_GoogleCloudHealthcareV1FhirGcsSourceOut",
        "AuditLogConfigIn": "_healthcare_182_AuditLogConfigIn",
        "AuditLogConfigOut": "_healthcare_183_AuditLogConfigOut",
        "ListOperationsResponseIn": "_healthcare_184_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_healthcare_185_ListOperationsResponseOut",
        "RejectConsentRequestIn": "_healthcare_186_RejectConsentRequestIn",
        "RejectConsentRequestOut": "_healthcare_187_RejectConsentRequestOut",
        "ExportMessagesRequestIn": "_healthcare_188_ExportMessagesRequestIn",
        "ExportMessagesRequestOut": "_healthcare_189_ExportMessagesRequestOut",
        "ImportMessagesRequestIn": "_healthcare_190_ImportMessagesRequestIn",
        "ImportMessagesRequestOut": "_healthcare_191_ImportMessagesRequestOut",
        "ListConsentStoresResponseIn": "_healthcare_192_ListConsentStoresResponseIn",
        "ListConsentStoresResponseOut": "_healthcare_193_ListConsentStoresResponseOut",
        "PolicyIn": "_healthcare_194_PolicyIn",
        "PolicyOut": "_healthcare_195_PolicyOut",
        "ExportDicomDataRequestIn": "_healthcare_196_ExportDicomDataRequestIn",
        "ExportDicomDataRequestOut": "_healthcare_197_ExportDicomDataRequestOut",
        "AnalyzeEntitiesResponseIn": "_healthcare_198_AnalyzeEntitiesResponseIn",
        "AnalyzeEntitiesResponseOut": "_healthcare_199_AnalyzeEntitiesResponseOut",
        "ValidationConfigIn": "_healthcare_200_ValidationConfigIn",
        "ValidationConfigOut": "_healthcare_201_ValidationConfigOut",
        "DeidentifyConfigIn": "_healthcare_202_DeidentifyConfigIn",
        "DeidentifyConfigOut": "_healthcare_203_DeidentifyConfigOut",
        "EntityMentionRelationshipIn": "_healthcare_204_EntityMentionRelationshipIn",
        "EntityMentionRelationshipOut": "_healthcare_205_EntityMentionRelationshipOut",
        "RedactConfigIn": "_healthcare_206_RedactConfigIn",
        "RedactConfigOut": "_healthcare_207_RedactConfigOut",
        "ExportResourcesResponseIn": "_healthcare_208_ExportResourcesResponseIn",
        "ExportResourcesResponseOut": "_healthcare_209_ExportResourcesResponseOut",
        "FhirConfigIn": "_healthcare_210_FhirConfigIn",
        "FhirConfigOut": "_healthcare_211_FhirConfigOut",
        "AttributeIn": "_healthcare_212_AttributeIn",
        "AttributeOut": "_healthcare_213_AttributeOut",
        "CheckDataAccessResponseIn": "_healthcare_214_CheckDataAccessResponseIn",
        "CheckDataAccessResponseOut": "_healthcare_215_CheckDataAccessResponseOut",
        "DatasetIn": "_healthcare_216_DatasetIn",
        "DatasetOut": "_healthcare_217_DatasetOut",
        "GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryIn": "_healthcare_218_GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryIn",
        "GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryOut": "_healthcare_219_GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryOut",
        "TextConfigIn": "_healthcare_220_TextConfigIn",
        "TextConfigOut": "_healthcare_221_TextConfigOut",
        "DicomFilterConfigIn": "_healthcare_222_DicomFilterConfigIn",
        "DicomFilterConfigOut": "_healthcare_223_DicomFilterConfigOut",
        "ImportResourcesResponseIn": "_healthcare_224_ImportResourcesResponseIn",
        "ImportResourcesResponseOut": "_healthcare_225_ImportResourcesResponseOut",
        "GoogleCloudHealthcareV1ConsentGcsDestinationIn": "_healthcare_226_GoogleCloudHealthcareV1ConsentGcsDestinationIn",
        "GoogleCloudHealthcareV1ConsentGcsDestinationOut": "_healthcare_227_GoogleCloudHealthcareV1ConsentGcsDestinationOut",
        "EvaluateUserConsentsResponseIn": "_healthcare_228_EvaluateUserConsentsResponseIn",
        "EvaluateUserConsentsResponseOut": "_healthcare_229_EvaluateUserConsentsResponseOut",
        "ParserConfigIn": "_healthcare_230_ParserConfigIn",
        "ParserConfigOut": "_healthcare_231_ParserConfigOut",
        "OperationIn": "_healthcare_232_OperationIn",
        "OperationOut": "_healthcare_233_OperationOut",
        "ListConsentRevisionsResponseIn": "_healthcare_234_ListConsentRevisionsResponseIn",
        "ListConsentRevisionsResponseOut": "_healthcare_235_ListConsentRevisionsResponseOut",
        "CancelOperationRequestIn": "_healthcare_236_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_healthcare_237_CancelOperationRequestOut",
        "DeidentifySummaryIn": "_healthcare_238_DeidentifySummaryIn",
        "DeidentifySummaryOut": "_healthcare_239_DeidentifySummaryOut",
        "ReplaceWithInfoTypeConfigIn": "_healthcare_240_ReplaceWithInfoTypeConfigIn",
        "ReplaceWithInfoTypeConfigOut": "_healthcare_241_ReplaceWithInfoTypeConfigOut",
        "QueryAccessibleDataResponseIn": "_healthcare_242_QueryAccessibleDataResponseIn",
        "QueryAccessibleDataResponseOut": "_healthcare_243_QueryAccessibleDataResponseOut",
        "SchemaGroupIn": "_healthcare_244_SchemaGroupIn",
        "SchemaGroupOut": "_healthcare_245_SchemaGroupOut",
        "UserDataMappingIn": "_healthcare_246_UserDataMappingIn",
        "UserDataMappingOut": "_healthcare_247_UserDataMappingOut",
        "SchemaSegmentIn": "_healthcare_248_SchemaSegmentIn",
        "SchemaSegmentOut": "_healthcare_249_SchemaSegmentOut",
        "ListConsentArtifactsResponseIn": "_healthcare_250_ListConsentArtifactsResponseIn",
        "ListConsentArtifactsResponseOut": "_healthcare_251_ListConsentArtifactsResponseOut",
        "ListDicomStoresResponseIn": "_healthcare_252_ListDicomStoresResponseIn",
        "ListDicomStoresResponseOut": "_healthcare_253_ListDicomStoresResponseOut",
        "PatientIdIn": "_healthcare_254_PatientIdIn",
        "PatientIdOut": "_healthcare_255_PatientIdOut",
        "DateShiftConfigIn": "_healthcare_256_DateShiftConfigIn",
        "DateShiftConfigOut": "_healthcare_257_DateShiftConfigOut",
        "QueryAccessibleDataRequestIn": "_healthcare_258_QueryAccessibleDataRequestIn",
        "QueryAccessibleDataRequestOut": "_healthcare_259_QueryAccessibleDataRequestOut",
        "ImportMessagesResponseIn": "_healthcare_260_ImportMessagesResponseIn",
        "ImportMessagesResponseOut": "_healthcare_261_ImportMessagesResponseOut",
        "FhirStoreMetricIn": "_healthcare_262_FhirStoreMetricIn",
        "FhirStoreMetricOut": "_healthcare_263_FhirStoreMetricOut",
        "ImageIn": "_healthcare_264_ImageIn",
        "ImageOut": "_healthcare_265_ImageOut",
        "ListAttributeDefinitionsResponseIn": "_healthcare_266_ListAttributeDefinitionsResponseIn",
        "ListAttributeDefinitionsResponseOut": "_healthcare_267_ListAttributeDefinitionsResponseOut",
        "GoogleCloudHealthcareV1FhirGcsDestinationIn": "_healthcare_268_GoogleCloudHealthcareV1FhirGcsDestinationIn",
        "GoogleCloudHealthcareV1FhirGcsDestinationOut": "_healthcare_269_GoogleCloudHealthcareV1FhirGcsDestinationOut",
        "FeatureIn": "_healthcare_270_FeatureIn",
        "FeatureOut": "_healthcare_271_FeatureOut",
        "FieldIn": "_healthcare_272_FieldIn",
        "FieldOut": "_healthcare_273_FieldOut",
        "ListLocationsResponseIn": "_healthcare_274_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_healthcare_275_ListLocationsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ParsedDataIn"] = t.struct(
        {"segments": t.array(t.proxy(renames["SegmentIn"]))}
    ).named(renames["ParsedDataIn"])
    types["ParsedDataOut"] = t.struct(
        {
            "segments": t.array(t.proxy(renames["SegmentOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParsedDataOut"])
    types["FhirStoreMetricsIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metrics": t.array(t.proxy(renames["FhirStoreMetricIn"])).optional(),
        }
    ).named(renames["FhirStoreMetricsIn"])
    types["FhirStoreMetricsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metrics": t.array(t.proxy(renames["FhirStoreMetricOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FhirStoreMetricsOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["DeidentifyDicomStoreRequestIn"] = t.struct(
        {
            "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
            "destinationStore": t.string().optional(),
            "filterConfig": t.proxy(renames["DicomFilterConfigIn"]).optional(),
            "gcsConfigUri": t.string().optional(),
        }
    ).named(renames["DeidentifyDicomStoreRequestIn"])
    types["DeidentifyDicomStoreRequestOut"] = t.struct(
        {
            "config": t.proxy(renames["DeidentifyConfigOut"]).optional(),
            "destinationStore": t.string().optional(),
            "filterConfig": t.proxy(renames["DicomFilterConfigOut"]).optional(),
            "gcsConfigUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeidentifyDicomStoreRequestOut"])
    types["Hl7TypesConfigIn"] = t.struct(
        {
            "type": t.array(t.proxy(renames["TypeIn"])).optional(),
            "version": t.array(t.proxy(renames["VersionSourceIn"])).optional(),
        }
    ).named(renames["Hl7TypesConfigIn"])
    types["Hl7TypesConfigOut"] = t.struct(
        {
            "type": t.array(t.proxy(renames["TypeOut"])).optional(),
            "version": t.array(t.proxy(renames["VersionSourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Hl7TypesConfigOut"])
    types["InfoTypeTransformationIn"] = t.struct(
        {
            "cryptoHashConfig": t.proxy(renames["CryptoHashConfigIn"]).optional(),
            "dateShiftConfig": t.proxy(renames["DateShiftConfigIn"]).optional(),
            "characterMaskConfig": t.proxy(renames["CharacterMaskConfigIn"]).optional(),
            "redactConfig": t.proxy(renames["RedactConfigIn"]).optional(),
            "infoTypes": t.array(t.string()).optional(),
            "replaceWithInfoTypeConfig": t.proxy(
                renames["ReplaceWithInfoTypeConfigIn"]
            ).optional(),
        }
    ).named(renames["InfoTypeTransformationIn"])
    types["InfoTypeTransformationOut"] = t.struct(
        {
            "cryptoHashConfig": t.proxy(renames["CryptoHashConfigOut"]).optional(),
            "dateShiftConfig": t.proxy(renames["DateShiftConfigOut"]).optional(),
            "characterMaskConfig": t.proxy(
                renames["CharacterMaskConfigOut"]
            ).optional(),
            "redactConfig": t.proxy(renames["RedactConfigOut"]).optional(),
            "infoTypes": t.array(t.string()).optional(),
            "replaceWithInfoTypeConfig": t.proxy(
                renames["ReplaceWithInfoTypeConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InfoTypeTransformationOut"])
    types["CryptoHashConfigIn"] = t.struct(
        {
            "cryptoKey": t.string().optional(),
            "kmsWrapped": t.proxy(renames["KmsWrappedCryptoKeyIn"]).optional(),
        }
    ).named(renames["CryptoHashConfigIn"])
    types["CryptoHashConfigOut"] = t.struct(
        {
            "cryptoKey": t.string().optional(),
            "kmsWrapped": t.proxy(renames["KmsWrappedCryptoKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoHashConfigOut"])
    types["EvaluateUserConsentsRequestIn"] = t.struct(
        {
            "userId": t.string(),
            "pageSize": t.integer().optional(),
            "responseView": t.string().optional(),
            "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
            "pageToken": t.string().optional(),
            "consentList": t.proxy(renames["ConsentListIn"]).optional(),
            "requestAttributes": t.struct({"_": t.string().optional()}),
        }
    ).named(renames["EvaluateUserConsentsRequestIn"])
    types["EvaluateUserConsentsRequestOut"] = t.struct(
        {
            "userId": t.string(),
            "pageSize": t.integer().optional(),
            "responseView": t.string().optional(),
            "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
            "pageToken": t.string().optional(),
            "consentList": t.proxy(renames["ConsentListOut"]).optional(),
            "requestAttributes": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EvaluateUserConsentsRequestOut"])
    types["ImportResourcesRequestIn"] = t.struct(
        {
            "contentStructure": t.string().optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudHealthcareV1FhirGcsSourceIn"]
            ).optional(),
        }
    ).named(renames["ImportResourcesRequestIn"])
    types["ImportResourcesRequestOut"] = t.struct(
        {
            "contentStructure": t.string().optional(),
            "gcsSource": t.proxy(
                renames["GoogleCloudHealthcareV1FhirGcsSourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportResourcesRequestOut"])
    types["SignatureIn"] = t.struct(
        {
            "signatureTime": t.string().optional(),
            "userId": t.string(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SignatureIn"])
    types["SignatureOut"] = t.struct(
        {
            "signatureTime": t.string().optional(),
            "userId": t.string(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignatureOut"])
    types["GoogleCloudHealthcareV1DicomGcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1DicomGcsSourceIn"])
    types["GoogleCloudHealthcareV1DicomGcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1DicomGcsSourceOut"])
    types["KmsWrappedCryptoKeyIn"] = t.struct(
        {"cryptoKey": t.string(), "wrappedKey": t.string()}
    ).named(renames["KmsWrappedCryptoKeyIn"])
    types["KmsWrappedCryptoKeyOut"] = t.struct(
        {
            "cryptoKey": t.string(),
            "wrappedKey": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KmsWrappedCryptoKeyOut"])
    types["ListMessagesResponseIn"] = t.struct(
        {
            "hl7V2Messages": t.array(t.proxy(renames["MessageIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListMessagesResponseIn"])
    types["ListMessagesResponseOut"] = t.struct(
        {
            "hl7V2Messages": t.array(t.proxy(renames["MessageOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMessagesResponseOut"])
    types["ConsentEvaluationIn"] = t.struct(
        {"evaluationResult": t.string().optional()}
    ).named(renames["ConsentEvaluationIn"])
    types["ConsentEvaluationOut"] = t.struct(
        {
            "evaluationResult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentEvaluationOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["EntityMentionIn"] = t.struct(
        {
            "linkedEntities": t.array(t.proxy(renames["LinkedEntityIn"])).optional(),
            "certaintyAssessment": t.proxy(renames["FeatureIn"]).optional(),
            "confidence": t.number().optional(),
            "subject": t.proxy(renames["FeatureIn"]).optional(),
            "text": t.proxy(renames["TextSpanIn"]).optional(),
            "mentionId": t.string().optional(),
            "type": t.string().optional(),
            "temporalAssessment": t.proxy(renames["FeatureIn"]).optional(),
        }
    ).named(renames["EntityMentionIn"])
    types["EntityMentionOut"] = t.struct(
        {
            "linkedEntities": t.array(t.proxy(renames["LinkedEntityOut"])).optional(),
            "certaintyAssessment": t.proxy(renames["FeatureOut"]).optional(),
            "confidence": t.number().optional(),
            "subject": t.proxy(renames["FeatureOut"]).optional(),
            "text": t.proxy(renames["TextSpanOut"]).optional(),
            "mentionId": t.string().optional(),
            "type": t.string().optional(),
            "temporalAssessment": t.proxy(renames["FeatureOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityMentionOut"])
    types["CheckDataAccessRequestIn"] = t.struct(
        {
            "dataId": t.string(),
            "consentList": t.proxy(renames["ConsentListIn"]).optional(),
            "requestAttributes": t.struct({"_": t.string().optional()}).optional(),
            "responseView": t.string().optional(),
        }
    ).named(renames["CheckDataAccessRequestIn"])
    types["CheckDataAccessRequestOut"] = t.struct(
        {
            "dataId": t.string(),
            "consentList": t.proxy(renames["ConsentListOut"]).optional(),
            "requestAttributes": t.struct({"_": t.string().optional()}).optional(),
            "responseView": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckDataAccessRequestOut"])
    types["ListDatasetsResponseIn"] = t.struct(
        {
            "datasets": t.array(t.proxy(renames["DatasetIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDatasetsResponseIn"])
    types["ListDatasetsResponseOut"] = t.struct(
        {
            "datasets": t.array(t.proxy(renames["DatasetOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDatasetsResponseOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "cancelRequested": t.boolean().optional(),
            "apiMethodName": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "logsUrl": t.string().optional(),
            "counter": t.proxy(renames["ProgressCounterIn"]),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "cancelRequested": t.boolean().optional(),
            "apiMethodName": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "logsUrl": t.string().optional(),
            "counter": t.proxy(renames["ProgressCounterOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["SchematizedDataIn"] = t.struct(
        {"data": t.string().optional(), "error": t.string().optional()}
    ).named(renames["SchematizedDataIn"])
    types["SchematizedDataOut"] = t.struct(
        {
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchematizedDataOut"])
    types["CreateMessageRequestIn"] = t.struct(
        {"message": t.proxy(renames["MessageIn"]).optional()}
    ).named(renames["CreateMessageRequestIn"])
    types["CreateMessageRequestOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateMessageRequestOut"])
    types["Hl7SchemaConfigIn"] = t.struct(
        {
            "version": t.array(t.proxy(renames["VersionSourceIn"])).optional(),
            "messageSchemaConfigs": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["Hl7SchemaConfigIn"])
    types["Hl7SchemaConfigOut"] = t.struct(
        {
            "version": t.array(t.proxy(renames["VersionSourceOut"])).optional(),
            "messageSchemaConfigs": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Hl7SchemaConfigOut"])
    types["EntityIn"] = t.struct(
        {
            "entityId": t.string().optional(),
            "preferredTerm": t.string().optional(),
            "vocabularyCodes": t.array(t.string()).optional(),
        }
    ).named(renames["EntityIn"])
    types["EntityOut"] = t.struct(
        {
            "entityId": t.string().optional(),
            "preferredTerm": t.string().optional(),
            "vocabularyCodes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityOut"])
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
    types["GcsDestinationIn"] = t.struct(
        {
            "contentStructure": t.string().optional(),
            "uriPrefix": t.string().optional(),
            "messageView": t.string().optional(),
        }
    ).named(renames["GcsDestinationIn"])
    types["GcsDestinationOut"] = t.struct(
        {
            "contentStructure": t.string().optional(),
            "uriPrefix": t.string().optional(),
            "messageView": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsDestinationOut"])
    types["DicomConfigIn"] = t.struct(
        {
            "filterProfile": t.string().optional(),
            "removeList": t.proxy(renames["TagFilterListIn"]).optional(),
            "skipIdRedaction": t.boolean().optional(),
            "keepList": t.proxy(renames["TagFilterListIn"]).optional(),
        }
    ).named(renames["DicomConfigIn"])
    types["DicomConfigOut"] = t.struct(
        {
            "filterProfile": t.string().optional(),
            "removeList": t.proxy(renames["TagFilterListOut"]).optional(),
            "skipIdRedaction": t.boolean().optional(),
            "keepList": t.proxy(renames["TagFilterListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DicomConfigOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["FhirFilterIn"] = t.struct(
        {"resources": t.proxy(renames["ResourcesIn"]).optional()}
    ).named(renames["FhirFilterIn"])
    types["FhirFilterOut"] = t.struct(
        {
            "resources": t.proxy(renames["ResourcesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FhirFilterOut"])
    types["ExportMessagesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ExportMessagesResponseIn"]
    )
    types["ExportMessagesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExportMessagesResponseOut"])
    types["ImportDicomDataResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ImportDicomDataResponseIn"]
    )
    types["ImportDicomDataResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportDicomDataResponseOut"])
    types["RevokeConsentRequestIn"] = t.struct(
        {"consentArtifact": t.string().optional()}
    ).named(renames["RevokeConsentRequestIn"])
    types["RevokeConsentRequestOut"] = t.struct(
        {
            "consentArtifact": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevokeConsentRequestOut"])
    types["NotificationConfigIn"] = t.struct(
        {"pubsubTopic": t.string().optional()}
    ).named(renames["NotificationConfigIn"])
    types["NotificationConfigOut"] = t.struct(
        {
            "pubsubTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationConfigOut"])
    types["SchemaConfigIn"] = t.struct(
        {
            "recursiveStructureDepth": t.string().optional(),
            "lastUpdatedPartitionConfig": t.proxy(
                renames["TimePartitioningIn"]
            ).optional(),
            "schemaType": t.string().optional(),
        }
    ).named(renames["SchemaConfigIn"])
    types["SchemaConfigOut"] = t.struct(
        {
            "recursiveStructureDepth": t.string().optional(),
            "lastUpdatedPartitionConfig": t.proxy(
                renames["TimePartitioningOut"]
            ).optional(),
            "schemaType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaConfigOut"])
    types["DeidentifyFhirStoreRequestIn"] = t.struct(
        {
            "skipModifiedResources": t.boolean().optional(),
            "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
            "destinationStore": t.string().optional(),
            "resourceFilter": t.proxy(renames["FhirFilterIn"]).optional(),
            "gcsConfigUri": t.string().optional(),
        }
    ).named(renames["DeidentifyFhirStoreRequestIn"])
    types["DeidentifyFhirStoreRequestOut"] = t.struct(
        {
            "skipModifiedResources": t.boolean().optional(),
            "config": t.proxy(renames["DeidentifyConfigOut"]).optional(),
            "destinationStore": t.string().optional(),
            "resourceFilter": t.proxy(renames["FhirFilterOut"]).optional(),
            "gcsConfigUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeidentifyFhirStoreRequestOut"])
    types["ConsentStoreIn"] = t.struct(
        {
            "defaultConsentTtl": t.string().optional(),
            "enableConsentCreateOnUpdate": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ConsentStoreIn"])
    types["ConsentStoreOut"] = t.struct(
        {
            "defaultConsentTtl": t.string().optional(),
            "enableConsentCreateOnUpdate": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentStoreOut"])
    types["GroupOrSegmentIn"] = t.struct(
        {
            "group": t.proxy(renames["SchemaGroupIn"]),
            "segment": t.proxy(renames["SchemaSegmentIn"]),
        }
    ).named(renames["GroupOrSegmentIn"])
    types["GroupOrSegmentOut"] = t.struct(
        {
            "group": t.proxy(renames["SchemaGroupOut"]),
            "segment": t.proxy(renames["SchemaSegmentOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOrSegmentOut"])
    types["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"] = t.struct(
        {
            "tableUri": t.string().optional(),
            "writeDisposition": t.string().optional(),
            "force": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"])
    types["GoogleCloudHealthcareV1DicomBigQueryDestinationOut"] = t.struct(
        {
            "tableUri": t.string().optional(),
            "writeDisposition": t.string().optional(),
            "force": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1DicomBigQueryDestinationOut"])
    types["ActivateConsentRequestIn"] = t.struct(
        {
            "consentArtifact": t.string(),
            "ttl": t.string().optional(),
            "expireTime": t.string().optional(),
        }
    ).named(renames["ActivateConsentRequestIn"])
    types["ActivateConsentRequestOut"] = t.struct(
        {
            "consentArtifact": t.string(),
            "ttl": t.string().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivateConsentRequestOut"])
    types["ResultIn"] = t.struct(
        {
            "consentDetails": t.struct({"_": t.string().optional()}).optional(),
            "dataId": t.string().optional(),
            "consented": t.boolean().optional(),
        }
    ).named(renames["ResultIn"])
    types["ResultOut"] = t.struct(
        {
            "consentDetails": t.struct({"_": t.string().optional()}).optional(),
            "dataId": t.string().optional(),
            "consented": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultOut"])
    types["ArchiveUserDataMappingResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ArchiveUserDataMappingResponseIn"])
    types["ArchiveUserDataMappingResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ArchiveUserDataMappingResponseOut"])
    types["AnalyzeEntitiesRequestIn"] = t.struct(
        {
            "documentContent": t.string().optional(),
            "licensedVocabularies": t.array(t.string()).optional(),
        }
    ).named(renames["AnalyzeEntitiesRequestIn"])
    types["AnalyzeEntitiesRequestOut"] = t.struct(
        {
            "documentContent": t.string().optional(),
            "licensedVocabularies": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeEntitiesRequestOut"])
    types["MessageIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sendFacility": t.string().optional(),
            "patientIds": t.array(t.proxy(renames["PatientIdIn"])).optional(),
            "name": t.string().optional(),
            "sendTime": t.string().optional(),
            "data": t.string().optional(),
            "messageType": t.string().optional(),
            "schematizedData": t.proxy(renames["SchematizedDataIn"]).optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "parsedData": t.proxy(renames["ParsedDataOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sendFacility": t.string().optional(),
            "patientIds": t.array(t.proxy(renames["PatientIdOut"])).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "sendTime": t.string().optional(),
            "data": t.string().optional(),
            "messageType": t.string().optional(),
            "schematizedData": t.proxy(renames["SchematizedDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["StreamConfigIn"] = t.struct(
        {
            "bigqueryDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"]
            ).optional(),
            "resourceTypes": t.array(t.string()).optional(),
            "deidentifiedStoreDestination": t.proxy(
                renames["DeidentifiedStoreDestinationIn"]
            ).optional(),
        }
    ).named(renames["StreamConfigIn"])
    types["StreamConfigOut"] = t.struct(
        {
            "bigqueryDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirBigQueryDestinationOut"]
            ).optional(),
            "resourceTypes": t.array(t.string()).optional(),
            "deidentifiedStoreDestination": t.proxy(
                renames["DeidentifiedStoreDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamConfigOut"])
    types["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"] = t.struct(
        {
            "force": t.boolean().optional(),
            "datasetUri": t.string().optional(),
            "schemaConfig": t.proxy(renames["SchemaConfigIn"]).optional(),
            "writeDisposition": t.string().optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"])
    types["GoogleCloudHealthcareV1FhirBigQueryDestinationOut"] = t.struct(
        {
            "force": t.boolean().optional(),
            "datasetUri": t.string().optional(),
            "schemaConfig": t.proxy(renames["SchemaConfigOut"]).optional(),
            "writeDisposition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1FhirBigQueryDestinationOut"])
    types["Hl7V2StoreIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "rejectDuplicateMessage": t.boolean().optional(),
            "name": t.string().optional(),
            "notificationConfigs": t.array(
                t.proxy(renames["Hl7V2NotificationConfigIn"])
            ).optional(),
            "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
        }
    ).named(renames["Hl7V2StoreIn"])
    types["Hl7V2StoreOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "rejectDuplicateMessage": t.boolean().optional(),
            "name": t.string().optional(),
            "notificationConfigs": t.array(
                t.proxy(renames["Hl7V2NotificationConfigOut"])
            ).optional(),
            "parserConfig": t.proxy(renames["ParserConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Hl7V2StoreOut"])
    types["TypeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "primitive": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "primitive": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["ProgressCounterIn"] = t.struct(
        {
            "pending": t.string().optional(),
            "failure": t.string().optional(),
            "success": t.string().optional(),
        }
    ).named(renames["ProgressCounterIn"])
    types["ProgressCounterOut"] = t.struct(
        {
            "pending": t.string().optional(),
            "failure": t.string().optional(),
            "success": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProgressCounterOut"])
    types["SearchResourcesRequestIn"] = t.struct(
        {"resourceType": t.string().optional()}
    ).named(renames["SearchResourcesRequestIn"])
    types["SearchResourcesRequestOut"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResourcesRequestOut"])
    types["FhirStoreIn"] = t.struct(
        {
            "streamConfigs": t.array(t.proxy(renames["StreamConfigIn"])).optional(),
            "version": t.string().optional(),
            "notificationConfigs": t.array(
                t.proxy(renames["FhirNotificationConfigIn"])
            ).optional(),
            "disableReferentialIntegrity": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "validationConfig": t.proxy(renames["ValidationConfigIn"]).optional(),
            "enableUpdateCreate": t.boolean().optional(),
            "defaultSearchHandlingStrict": t.boolean().optional(),
            "complexDataTypeReferenceParsing": t.string().optional(),
            "disableResourceVersioning": t.boolean().optional(),
            "name": t.string().optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigIn"]).optional(),
        }
    ).named(renames["FhirStoreIn"])
    types["FhirStoreOut"] = t.struct(
        {
            "streamConfigs": t.array(t.proxy(renames["StreamConfigOut"])).optional(),
            "version": t.string().optional(),
            "notificationConfigs": t.array(
                t.proxy(renames["FhirNotificationConfigOut"])
            ).optional(),
            "disableReferentialIntegrity": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "validationConfig": t.proxy(renames["ValidationConfigOut"]).optional(),
            "enableUpdateCreate": t.boolean().optional(),
            "defaultSearchHandlingStrict": t.boolean().optional(),
            "complexDataTypeReferenceParsing": t.string().optional(),
            "disableResourceVersioning": t.boolean().optional(),
            "name": t.string().optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FhirStoreOut"])
    types["ExportDicomDataResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ExportDicomDataResponseIn"]
    )
    types["ExportDicomDataResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExportDicomDataResponseOut"])
    types["VersionSourceIn"] = t.struct(
        {"value": t.string().optional(), "mshField": t.string().optional()}
    ).named(renames["VersionSourceIn"])
    types["VersionSourceOut"] = t.struct(
        {
            "value": t.string().optional(),
            "mshField": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionSourceOut"])
    types["ListFhirStoresResponseIn"] = t.struct(
        {
            "fhirStores": t.array(t.proxy(renames["FhirStoreIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListFhirStoresResponseIn"])
    types["ListFhirStoresResponseOut"] = t.struct(
        {
            "fhirStores": t.array(t.proxy(renames["FhirStoreOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFhirStoresResponseOut"])
    types["SegmentIn"] = t.struct(
        {
            "segmentId": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "setId": t.string().optional(),
        }
    ).named(renames["SegmentIn"])
    types["SegmentOut"] = t.struct(
        {
            "segmentId": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "setId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentOut"])
    types["DeidentifyDatasetRequestIn"] = t.struct(
        {
            "gcsConfigUri": t.string().optional(),
            "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
            "destinationDataset": t.string().optional(),
        }
    ).named(renames["DeidentifyDatasetRequestIn"])
    types["DeidentifyDatasetRequestOut"] = t.struct(
        {
            "gcsConfigUri": t.string().optional(),
            "config": t.proxy(renames["DeidentifyConfigOut"]).optional(),
            "destinationDataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeidentifyDatasetRequestOut"])
    types["TextSpanIn"] = t.struct(
        {"content": t.string().optional(), "beginOffset": t.integer().optional()}
    ).named(renames["TextSpanIn"])
    types["TextSpanOut"] = t.struct(
        {
            "content": t.string().optional(),
            "beginOffset": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextSpanOut"])
    types["TimePartitioningIn"] = t.struct(
        {"expirationMs": t.string().optional(), "type": t.string().optional()}
    ).named(renames["TimePartitioningIn"])
    types["TimePartitioningOut"] = t.struct(
        {
            "expirationMs": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimePartitioningOut"])
    types["FieldMetadataIn"] = t.struct(
        {"action": t.string().optional(), "paths": t.array(t.string()).optional()}
    ).named(renames["FieldMetadataIn"])
    types["FieldMetadataOut"] = t.struct(
        {
            "action": t.string().optional(),
            "paths": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldMetadataOut"])
    types["TagFilterListIn"] = t.struct({"tags": t.array(t.string()).optional()}).named(
        renames["TagFilterListIn"]
    )
    types["TagFilterListOut"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagFilterListOut"])
    types["DicomStoreIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigIn"]).optional(),
        }
    ).named(renames["DicomStoreIn"])
    types["DicomStoreOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DicomStoreOut"])
    types["ConsentListIn"] = t.struct(
        {"consents": t.array(t.string()).optional()}
    ).named(renames["ConsentListIn"])
    types["ConsentListOut"] = t.struct(
        {
            "consents": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentListOut"])
    types["LinkedEntityIn"] = t.struct({"entityId": t.string().optional()}).named(
        renames["LinkedEntityIn"]
    )
    types["LinkedEntityOut"] = t.struct(
        {
            "entityId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedEntityOut"])
    types["ConsentIn"] = t.struct(
        {
            "policies": t.array(
                t.proxy(renames["GoogleCloudHealthcareV1ConsentPolicyIn"])
            ).optional(),
            "name": t.string().optional(),
            "consentArtifact": t.string(),
            "state": t.string(),
            "ttl": t.string().optional(),
            "expireTime": t.string().optional(),
            "userId": t.string(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ConsentIn"])
    types["ConsentOut"] = t.struct(
        {
            "policies": t.array(
                t.proxy(renames["GoogleCloudHealthcareV1ConsentPolicyOut"])
            ).optional(),
            "name": t.string().optional(),
            "consentArtifact": t.string(),
            "state": t.string(),
            "ttl": t.string().optional(),
            "expireTime": t.string().optional(),
            "revisionCreateTime": t.string().optional(),
            "revisionId": t.string().optional(),
            "userId": t.string(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentOut"])
    types["GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryIn"])
    types["GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryOut"])
    types["ConsentArtifactIn"] = t.struct(
        {
            "consentContentVersion": t.string().optional(),
            "guardianSignature": t.proxy(renames["SignatureIn"]).optional(),
            "witnessSignature": t.proxy(renames["SignatureIn"]).optional(),
            "consentContentScreenshots": t.array(
                t.proxy(renames["ImageIn"])
            ).optional(),
            "name": t.string().optional(),
            "userSignature": t.proxy(renames["SignatureIn"]).optional(),
            "userId": t.string(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ConsentArtifactIn"])
    types["ConsentArtifactOut"] = t.struct(
        {
            "consentContentVersion": t.string().optional(),
            "guardianSignature": t.proxy(renames["SignatureOut"]).optional(),
            "witnessSignature": t.proxy(renames["SignatureOut"]).optional(),
            "consentContentScreenshots": t.array(
                t.proxy(renames["ImageOut"])
            ).optional(),
            "name": t.string().optional(),
            "userSignature": t.proxy(renames["SignatureOut"]).optional(),
            "userId": t.string(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentArtifactOut"])
    types["Hl7V2NotificationConfigIn"] = t.struct(
        {"filter": t.string().optional(), "pubsubTopic": t.string().optional()}
    ).named(renames["Hl7V2NotificationConfigIn"])
    types["Hl7V2NotificationConfigOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "pubsubTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Hl7V2NotificationConfigOut"])
    types["ListUserDataMappingsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "userDataMappings": t.array(
                t.proxy(renames["UserDataMappingIn"])
            ).optional(),
        }
    ).named(renames["ListUserDataMappingsResponseIn"])
    types["ListUserDataMappingsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "userDataMappings": t.array(
                t.proxy(renames["UserDataMappingOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUserDataMappingsResponseOut"])
    types["CharacterMaskConfigIn"] = t.struct(
        {"maskingCharacter": t.string().optional()}
    ).named(renames["CharacterMaskConfigIn"])
    types["CharacterMaskConfigOut"] = t.struct(
        {
            "maskingCharacter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CharacterMaskConfigOut"])
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
    types["FhirNotificationConfigIn"] = t.struct(
        {
            "sendFullResource": t.boolean().optional(),
            "pubsubTopic": t.string().optional(),
            "sendPreviousResourceOnDelete": t.boolean().optional(),
        }
    ).named(renames["FhirNotificationConfigIn"])
    types["FhirNotificationConfigOut"] = t.struct(
        {
            "sendFullResource": t.boolean().optional(),
            "pubsubTopic": t.string().optional(),
            "sendPreviousResourceOnDelete": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FhirNotificationConfigOut"])
    types["GcsSourceIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["GcsSourceIn"]
    )
    types["GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsSourceOut"])
    types["ResourcesIn"] = t.struct(
        {"resources": t.array(t.string()).optional()}
    ).named(renames["ResourcesIn"])
    types["ResourcesOut"] = t.struct(
        {
            "resources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourcesOut"])
    types["GoogleCloudHealthcareV1DicomGcsDestinationIn"] = t.struct(
        {"mimeType": t.string().optional(), "uriPrefix": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1DicomGcsDestinationIn"])
    types["GoogleCloudHealthcareV1DicomGcsDestinationOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "uriPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1DicomGcsDestinationOut"])
    types["ListHl7V2StoresResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "hl7V2Stores": t.array(t.proxy(renames["Hl7V2StoreIn"])).optional(),
        }
    ).named(renames["ListHl7V2StoresResponseIn"])
    types["ListHl7V2StoresResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "hl7V2Stores": t.array(t.proxy(renames["Hl7V2StoreOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListHl7V2StoresResponseOut"])
    types["ListConsentsResponseIn"] = t.struct(
        {
            "consents": t.array(t.proxy(renames["ConsentIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListConsentsResponseIn"])
    types["ListConsentsResponseOut"] = t.struct(
        {
            "consents": t.array(t.proxy(renames["ConsentOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConsentsResponseOut"])
    types["ArchiveUserDataMappingRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ArchiveUserDataMappingRequestIn"])
    types["ArchiveUserDataMappingRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ArchiveUserDataMappingRequestOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["SchemaPackageIn"] = t.struct(
        {
            "unexpectedSegmentHandling": t.string().optional(),
            "schematizedParsingType": t.string().optional(),
            "types": t.array(t.proxy(renames["Hl7TypesConfigIn"])).optional(),
            "ignoreMinOccurs": t.boolean().optional(),
            "schemas": t.array(t.proxy(renames["Hl7SchemaConfigIn"])).optional(),
        }
    ).named(renames["SchemaPackageIn"])
    types["SchemaPackageOut"] = t.struct(
        {
            "unexpectedSegmentHandling": t.string().optional(),
            "schematizedParsingType": t.string().optional(),
            "types": t.array(t.proxy(renames["Hl7TypesConfigOut"])).optional(),
            "ignoreMinOccurs": t.boolean().optional(),
            "schemas": t.array(t.proxy(renames["Hl7SchemaConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaPackageOut"])
    types["DeidentifiedStoreDestinationIn"] = t.struct(
        {
            "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
            "store": t.string().optional(),
        }
    ).named(renames["DeidentifiedStoreDestinationIn"])
    types["DeidentifiedStoreDestinationOut"] = t.struct(
        {
            "config": t.proxy(renames["DeidentifyConfigOut"]).optional(),
            "store": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeidentifiedStoreDestinationOut"])
    types["GoogleCloudHealthcareV1ConsentPolicyIn"] = t.struct(
        {
            "authorizationRule": t.proxy(renames["ExprIn"]),
            "resourceAttributes": t.array(t.proxy(renames["AttributeIn"])).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1ConsentPolicyIn"])
    types["GoogleCloudHealthcareV1ConsentPolicyOut"] = t.struct(
        {
            "authorizationRule": t.proxy(renames["ExprOut"]),
            "resourceAttributes": t.array(t.proxy(renames["AttributeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1ConsentPolicyOut"])
    types["HttpBodyIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "data": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["HttpBodyIn"])
    types["HttpBodyOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "data": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpBodyOut"])
    types["IngestMessageRequestIn"] = t.struct(
        {"message": t.proxy(renames["MessageIn"]).optional()}
    ).named(renames["IngestMessageRequestIn"])
    types["IngestMessageRequestOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IngestMessageRequestOut"])
    types["AttributeDefinitionIn"] = t.struct(
        {
            "dataMappingDefaultValue": t.string().optional(),
            "name": t.string().optional(),
            "category": t.string(),
            "consentDefaultValues": t.array(t.string()).optional(),
            "allowedValues": t.array(t.string()),
            "description": t.string().optional(),
        }
    ).named(renames["AttributeDefinitionIn"])
    types["AttributeDefinitionOut"] = t.struct(
        {
            "dataMappingDefaultValue": t.string().optional(),
            "name": t.string().optional(),
            "category": t.string(),
            "consentDefaultValues": t.array(t.string()).optional(),
            "allowedValues": t.array(t.string()),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeDefinitionOut"])
    types["IngestMessageResponseIn"] = t.struct(
        {
            "message": t.proxy(renames["MessageIn"]).optional(),
            "hl7Ack": t.string().optional(),
        }
    ).named(renames["IngestMessageResponseIn"])
    types["IngestMessageResponseOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]).optional(),
            "hl7Ack": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IngestMessageResponseOut"])
    types["ExportResourcesRequestIn"] = t.struct(
        {
            "_type": t.string().optional(),
            "_since": t.string().optional(),
            "bigqueryDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"]
            ).optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"]
            ).optional(),
        }
    ).named(renames["ExportResourcesRequestIn"])
    types["ExportResourcesRequestOut"] = t.struct(
        {
            "_type": t.string().optional(),
            "_since": t.string().optional(),
            "bigqueryDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirBigQueryDestinationOut"]
            ).optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirGcsDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportResourcesRequestOut"])
    types["ImportDicomDataRequestIn"] = t.struct(
        {
            "gcsSource": t.proxy(
                renames["GoogleCloudHealthcareV1DicomGcsSourceIn"]
            ).optional()
        }
    ).named(renames["ImportDicomDataRequestIn"])
    types["ImportDicomDataRequestOut"] = t.struct(
        {
            "gcsSource": t.proxy(
                renames["GoogleCloudHealthcareV1DicomGcsSourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportDicomDataRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ImageConfigIn"] = t.struct(
        {"textRedactionMode": t.string().optional()}
    ).named(renames["ImageConfigIn"])
    types["ImageConfigOut"] = t.struct(
        {
            "textRedactionMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageConfigOut"])
    types["GoogleCloudHealthcareV1FhirGcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1FhirGcsSourceIn"])
    types["GoogleCloudHealthcareV1FhirGcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1FhirGcsSourceOut"])
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
    types["RejectConsentRequestIn"] = t.struct(
        {"consentArtifact": t.string().optional()}
    ).named(renames["RejectConsentRequestIn"])
    types["RejectConsentRequestOut"] = t.struct(
        {
            "consentArtifact": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RejectConsentRequestOut"])
    types["ExportMessagesRequestIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional(),
        }
    ).named(renames["ExportMessagesRequestIn"])
    types["ExportMessagesRequestOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportMessagesRequestOut"])
    types["ImportMessagesRequestIn"] = t.struct(
        {"gcsSource": t.proxy(renames["GcsSourceIn"]).optional()}
    ).named(renames["ImportMessagesRequestIn"])
    types["ImportMessagesRequestOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportMessagesRequestOut"])
    types["ListConsentStoresResponseIn"] = t.struct(
        {
            "consentStores": t.array(t.proxy(renames["ConsentStoreIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListConsentStoresResponseIn"])
    types["ListConsentStoresResponseOut"] = t.struct(
        {
            "consentStores": t.array(t.proxy(renames["ConsentStoreOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConsentStoresResponseOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ExportDicomDataRequestIn"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudHealthcareV1DicomGcsDestinationIn"]
            ).optional(),
            "bigqueryDestination": t.proxy(
                renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"]
            ).optional(),
        }
    ).named(renames["ExportDicomDataRequestIn"])
    types["ExportDicomDataRequestOut"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudHealthcareV1DicomGcsDestinationOut"]
            ).optional(),
            "bigqueryDestination": t.proxy(
                renames["GoogleCloudHealthcareV1DicomBigQueryDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportDicomDataRequestOut"])
    types["AnalyzeEntitiesResponseIn"] = t.struct(
        {
            "entities": t.array(t.proxy(renames["EntityIn"])).optional(),
            "relationships": t.array(
                t.proxy(renames["EntityMentionRelationshipIn"])
            ).optional(),
            "entityMentions": t.array(t.proxy(renames["EntityMentionIn"])).optional(),
        }
    ).named(renames["AnalyzeEntitiesResponseIn"])
    types["AnalyzeEntitiesResponseOut"] = t.struct(
        {
            "entities": t.array(t.proxy(renames["EntityOut"])).optional(),
            "relationships": t.array(
                t.proxy(renames["EntityMentionRelationshipOut"])
            ).optional(),
            "entityMentions": t.array(t.proxy(renames["EntityMentionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeEntitiesResponseOut"])
    types["ValidationConfigIn"] = t.struct(
        {
            "disableFhirpathValidation": t.boolean().optional(),
            "enabledImplementationGuides": t.array(t.string()).optional(),
            "disableReferenceTypeValidation": t.boolean().optional(),
            "disableProfileValidation": t.boolean().optional(),
            "disableRequiredFieldValidation": t.boolean().optional(),
        }
    ).named(renames["ValidationConfigIn"])
    types["ValidationConfigOut"] = t.struct(
        {
            "disableFhirpathValidation": t.boolean().optional(),
            "enabledImplementationGuides": t.array(t.string()).optional(),
            "disableReferenceTypeValidation": t.boolean().optional(),
            "disableProfileValidation": t.boolean().optional(),
            "disableRequiredFieldValidation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationConfigOut"])
    types["DeidentifyConfigIn"] = t.struct(
        {
            "text": t.proxy(renames["TextConfigIn"]).optional(),
            "fhir": t.proxy(renames["FhirConfigIn"]).optional(),
            "useRegionalDataProcessing": t.boolean().optional(),
            "image": t.proxy(renames["ImageConfigIn"]).optional(),
            "dicom": t.proxy(renames["DicomConfigIn"]).optional(),
        }
    ).named(renames["DeidentifyConfigIn"])
    types["DeidentifyConfigOut"] = t.struct(
        {
            "text": t.proxy(renames["TextConfigOut"]).optional(),
            "fhir": t.proxy(renames["FhirConfigOut"]).optional(),
            "useRegionalDataProcessing": t.boolean().optional(),
            "image": t.proxy(renames["ImageConfigOut"]).optional(),
            "dicom": t.proxy(renames["DicomConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeidentifyConfigOut"])
    types["EntityMentionRelationshipIn"] = t.struct(
        {
            "subjectId": t.string().optional(),
            "confidence": t.number().optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["EntityMentionRelationshipIn"])
    types["EntityMentionRelationshipOut"] = t.struct(
        {
            "subjectId": t.string().optional(),
            "confidence": t.number().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityMentionRelationshipOut"])
    types["RedactConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RedactConfigIn"]
    )
    types["RedactConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RedactConfigOut"])
    types["ExportResourcesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ExportResourcesResponseIn"]
    )
    types["ExportResourcesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExportResourcesResponseOut"])
    types["FhirConfigIn"] = t.struct(
        {
            "fieldMetadataList": t.array(
                t.proxy(renames["FieldMetadataIn"])
            ).optional(),
            "defaultKeepExtensions": t.boolean().optional(),
        }
    ).named(renames["FhirConfigIn"])
    types["FhirConfigOut"] = t.struct(
        {
            "fieldMetadataList": t.array(
                t.proxy(renames["FieldMetadataOut"])
            ).optional(),
            "defaultKeepExtensions": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FhirConfigOut"])
    types["AttributeIn"] = t.struct(
        {"attributeDefinitionId": t.string().optional(), "values": t.array(t.string())}
    ).named(renames["AttributeIn"])
    types["AttributeOut"] = t.struct(
        {
            "attributeDefinitionId": t.string().optional(),
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeOut"])
    types["CheckDataAccessResponseIn"] = t.struct(
        {
            "consentDetails": t.struct({"_": t.string().optional()}).optional(),
            "consented": t.boolean().optional(),
        }
    ).named(renames["CheckDataAccessResponseIn"])
    types["CheckDataAccessResponseOut"] = t.struct(
        {
            "consentDetails": t.struct({"_": t.string().optional()}).optional(),
            "consented": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckDataAccessResponseOut"])
    types["DatasetIn"] = t.struct(
        {"timeZone": t.string().optional(), "name": t.string().optional()}
    ).named(renames["DatasetIn"])
    types["DatasetOut"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetOut"])
    types["GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryIn"])
    types["GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryOut"])
    types["TextConfigIn"] = t.struct(
        {
            "additionalTransformations": t.array(
                t.proxy(renames["InfoTypeTransformationIn"])
            ).optional(),
            "excludeInfoTypes": t.array(t.string()).optional(),
            "transformations": t.array(
                t.proxy(renames["InfoTypeTransformationIn"])
            ).optional(),
        }
    ).named(renames["TextConfigIn"])
    types["TextConfigOut"] = t.struct(
        {
            "additionalTransformations": t.array(
                t.proxy(renames["InfoTypeTransformationOut"])
            ).optional(),
            "excludeInfoTypes": t.array(t.string()).optional(),
            "transformations": t.array(
                t.proxy(renames["InfoTypeTransformationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextConfigOut"])
    types["DicomFilterConfigIn"] = t.struct(
        {"resourcePathsGcsUri": t.string().optional()}
    ).named(renames["DicomFilterConfigIn"])
    types["DicomFilterConfigOut"] = t.struct(
        {
            "resourcePathsGcsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DicomFilterConfigOut"])
    types["ImportResourcesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ImportResourcesResponseIn"]
    )
    types["ImportResourcesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportResourcesResponseOut"])
    types["GoogleCloudHealthcareV1ConsentGcsDestinationIn"] = t.struct(
        {"uriPrefix": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1ConsentGcsDestinationIn"])
    types["GoogleCloudHealthcareV1ConsentGcsDestinationOut"] = t.struct(
        {
            "uriPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1ConsentGcsDestinationOut"])
    types["EvaluateUserConsentsResponseIn"] = t.struct(
        {
            "results": t.array(t.proxy(renames["ResultIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["EvaluateUserConsentsResponseIn"])
    types["EvaluateUserConsentsResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["ResultOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EvaluateUserConsentsResponseOut"])
    types["ParserConfigIn"] = t.struct(
        {
            "segmentTerminator": t.string().optional(),
            "allowNullHeader": t.boolean().optional(),
            "schema": t.proxy(renames["SchemaPackageIn"]).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["ParserConfigIn"])
    types["ParserConfigOut"] = t.struct(
        {
            "segmentTerminator": t.string().optional(),
            "allowNullHeader": t.boolean().optional(),
            "schema": t.proxy(renames["SchemaPackageOut"]).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParserConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ListConsentRevisionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "consents": t.array(t.proxy(renames["ConsentIn"])).optional(),
        }
    ).named(renames["ListConsentRevisionsResponseIn"])
    types["ListConsentRevisionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "consents": t.array(t.proxy(renames["ConsentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConsentRevisionsResponseOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["DeidentifySummaryIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeidentifySummaryIn"]
    )
    types["DeidentifySummaryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeidentifySummaryOut"])
    types["ReplaceWithInfoTypeConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReplaceWithInfoTypeConfigIn"]
    )
    types["ReplaceWithInfoTypeConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReplaceWithInfoTypeConfigOut"])
    types["QueryAccessibleDataResponseIn"] = t.struct(
        {"gcsUris": t.array(t.string()).optional()}
    ).named(renames["QueryAccessibleDataResponseIn"])
    types["QueryAccessibleDataResponseOut"] = t.struct(
        {
            "gcsUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryAccessibleDataResponseOut"])
    types["SchemaGroupIn"] = t.struct(
        {
            "maxOccurs": t.integer().optional(),
            "members": t.array(t.proxy(renames["GroupOrSegmentIn"])).optional(),
            "name": t.string().optional(),
            "minOccurs": t.integer().optional(),
            "choice": t.boolean().optional(),
        }
    ).named(renames["SchemaGroupIn"])
    types["SchemaGroupOut"] = t.struct(
        {
            "maxOccurs": t.integer().optional(),
            "members": t.array(t.proxy(renames["GroupOrSegmentOut"])).optional(),
            "name": t.string().optional(),
            "minOccurs": t.integer().optional(),
            "choice": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaGroupOut"])
    types["UserDataMappingIn"] = t.struct(
        {
            "dataId": t.string(),
            "name": t.string().optional(),
            "userId": t.string(),
            "resourceAttributes": t.array(t.proxy(renames["AttributeIn"])).optional(),
        }
    ).named(renames["UserDataMappingIn"])
    types["UserDataMappingOut"] = t.struct(
        {
            "dataId": t.string(),
            "archiveTime": t.string().optional(),
            "name": t.string().optional(),
            "userId": t.string(),
            "archived": t.boolean().optional(),
            "resourceAttributes": t.array(t.proxy(renames["AttributeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserDataMappingOut"])
    types["SchemaSegmentIn"] = t.struct(
        {
            "type": t.string().optional(),
            "minOccurs": t.integer().optional(),
            "maxOccurs": t.integer().optional(),
        }
    ).named(renames["SchemaSegmentIn"])
    types["SchemaSegmentOut"] = t.struct(
        {
            "type": t.string().optional(),
            "minOccurs": t.integer().optional(),
            "maxOccurs": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaSegmentOut"])
    types["ListConsentArtifactsResponseIn"] = t.struct(
        {
            "consentArtifacts": t.array(
                t.proxy(renames["ConsentArtifactIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListConsentArtifactsResponseIn"])
    types["ListConsentArtifactsResponseOut"] = t.struct(
        {
            "consentArtifacts": t.array(
                t.proxy(renames["ConsentArtifactOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConsentArtifactsResponseOut"])
    types["ListDicomStoresResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dicomStores": t.array(t.proxy(renames["DicomStoreIn"])).optional(),
        }
    ).named(renames["ListDicomStoresResponseIn"])
    types["ListDicomStoresResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dicomStores": t.array(t.proxy(renames["DicomStoreOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDicomStoresResponseOut"])
    types["PatientIdIn"] = t.struct(
        {"type": t.string().optional(), "value": t.string().optional()}
    ).named(renames["PatientIdIn"])
    types["PatientIdOut"] = t.struct(
        {
            "type": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatientIdOut"])
    types["DateShiftConfigIn"] = t.struct(
        {
            "kmsWrapped": t.proxy(renames["KmsWrappedCryptoKeyIn"]).optional(),
            "cryptoKey": t.string().optional(),
        }
    ).named(renames["DateShiftConfigIn"])
    types["DateShiftConfigOut"] = t.struct(
        {
            "kmsWrapped": t.proxy(renames["KmsWrappedCryptoKeyOut"]).optional(),
            "cryptoKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateShiftConfigOut"])
    types["QueryAccessibleDataRequestIn"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudHealthcareV1ConsentGcsDestinationIn"]
            ).optional(),
            "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
            "requestAttributes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["QueryAccessibleDataRequestIn"])
    types["QueryAccessibleDataRequestOut"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudHealthcareV1ConsentGcsDestinationOut"]
            ).optional(),
            "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
            "requestAttributes": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryAccessibleDataRequestOut"])
    types["ImportMessagesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ImportMessagesResponseIn"]
    )
    types["ImportMessagesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportMessagesResponseOut"])
    types["FhirStoreMetricIn"] = t.struct(
        {
            "structuredStorageSizeBytes": t.string().optional(),
            "count": t.string().optional(),
            "resourceType": t.string().optional(),
        }
    ).named(renames["FhirStoreMetricIn"])
    types["FhirStoreMetricOut"] = t.struct(
        {
            "structuredStorageSizeBytes": t.string().optional(),
            "count": t.string().optional(),
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FhirStoreMetricOut"])
    types["ImageIn"] = t.struct(
        {"rawBytes": t.string().optional(), "gcsUri": t.string().optional()}
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "rawBytes": t.string().optional(),
            "gcsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["ListAttributeDefinitionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "attributeDefinitions": t.array(
                t.proxy(renames["AttributeDefinitionIn"])
            ).optional(),
        }
    ).named(renames["ListAttributeDefinitionsResponseIn"])
    types["ListAttributeDefinitionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "attributeDefinitions": t.array(
                t.proxy(renames["AttributeDefinitionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAttributeDefinitionsResponseOut"])
    types["GoogleCloudHealthcareV1FhirGcsDestinationIn"] = t.struct(
        {"uriPrefix": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"])
    types["GoogleCloudHealthcareV1FhirGcsDestinationOut"] = t.struct(
        {
            "uriPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1FhirGcsDestinationOut"])
    types["FeatureIn"] = t.struct(
        {"confidence": t.number().optional(), "value": t.string().optional()}
    ).named(renames["FeatureIn"])
    types["FeatureOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureOut"])
    types["FieldIn"] = t.struct(
        {
            "type": t.string().optional(),
            "maxOccurs": t.integer().optional(),
            "minOccurs": t.integer().optional(),
            "name": t.string().optional(),
            "table": t.string().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "type": t.string().optional(),
            "maxOccurs": t.integer().optional(),
            "minOccurs": t.integer().optional(),
            "name": t.string().optional(),
            "table": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])

    functions = {}
    functions["projectsLocationsGet"] = healthcare.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = healthcare.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesNlpAnalyzeEntities"] = healthcare.post(
        "v1/{nlpService}:analyzeEntities",
        t.struct(
            {
                "nlpService": t.string().optional(),
                "documentContent": t.string().optional(),
                "licensedVocabularies": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeEntitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDelete"] = healthcare.post(
        "v1/{parent}/datasets",
        t.struct(
            {
                "datasetId": t.string().optional(),
                "parent": t.string().optional(),
                "timeZone": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsGetIamPolicy"] = healthcare.post(
        "v1/{parent}/datasets",
        t.struct(
            {
                "datasetId": t.string().optional(),
                "parent": t.string().optional(),
                "timeZone": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDeidentify"] = healthcare.post(
        "v1/{parent}/datasets",
        t.struct(
            {
                "datasetId": t.string().optional(),
                "parent": t.string().optional(),
                "timeZone": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsPatch"] = healthcare.post(
        "v1/{parent}/datasets",
        t.struct(
            {
                "datasetId": t.string().optional(),
                "parent": t.string().optional(),
                "timeZone": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsTestIamPermissions"] = healthcare.post(
        "v1/{parent}/datasets",
        t.struct(
            {
                "datasetId": t.string().optional(),
                "parent": t.string().optional(),
                "timeZone": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsSetIamPolicy"] = healthcare.post(
        "v1/{parent}/datasets",
        t.struct(
            {
                "datasetId": t.string().optional(),
                "parent": t.string().optional(),
                "timeZone": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsList"] = healthcare.post(
        "v1/{parent}/datasets",
        t.struct(
            {
                "datasetId": t.string().optional(),
                "parent": t.string().optional(),
                "timeZone": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsGet"] = healthcare.post(
        "v1/{parent}/datasets",
        t.struct(
            {
                "datasetId": t.string().optional(),
                "parent": t.string().optional(),
                "timeZone": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsCreate"] = healthcare.post(
        "v1/{parent}/datasets",
        t.struct(
            {
                "datasetId": t.string().optional(),
                "parent": t.string().optional(),
                "timeZone": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresGetIamPolicy"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomGcsDestinationIn"]
                ).optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresDeidentify"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomGcsDestinationIn"]
                ).optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresSetIamPolicy"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomGcsDestinationIn"]
                ).optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresImport"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomGcsDestinationIn"]
                ).optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresDelete"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomGcsDestinationIn"]
                ).optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresSearchForSeries"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomGcsDestinationIn"]
                ).optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresCreate"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomGcsDestinationIn"]
                ).optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresList"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomGcsDestinationIn"]
                ).optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresSearchForStudies"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomGcsDestinationIn"]
                ).optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresGet"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomGcsDestinationIn"]
                ).optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresStoreInstances"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomGcsDestinationIn"]
                ).optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresSearchForInstances"
    ] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomGcsDestinationIn"]
                ).optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresPatch"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomGcsDestinationIn"]
                ).optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresTestIamPermissions"
    ] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomGcsDestinationIn"]
                ).optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresExport"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomGcsDestinationIn"]
                ).optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesRetrieveStudy"
    ] = healthcare.get(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "dicomWebPath": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresStudiesDelete"] = healthcare.get(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "dicomWebPath": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesRetrieveMetadata"
    ] = healthcare.get(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "dicomWebPath": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesSearchForSeries"
    ] = healthcare.get(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "dicomWebPath": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesStoreInstances"
    ] = healthcare.get(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "dicomWebPath": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesSearchForInstances"
    ] = healthcare.get(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "dicomWebPath": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesSeriesRetrieveMetadata"
    ] = healthcare.get(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "parent": t.string().optional(),
                "dicomWebPath": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesSeriesSearchForInstances"
    ] = healthcare.get(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "parent": t.string().optional(),
                "dicomWebPath": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesSeriesDelete"
    ] = healthcare.get(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "parent": t.string().optional(),
                "dicomWebPath": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesSeriesRetrieveSeries"
    ] = healthcare.get(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "parent": t.string().optional(),
                "dicomWebPath": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesSeriesInstancesRetrieveInstance"
    ] = healthcare.delete(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "dicomWebPath": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesSeriesInstancesRetrieveMetadata"
    ] = healthcare.delete(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "dicomWebPath": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesSeriesInstancesRetrieveRendered"
    ] = healthcare.delete(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "dicomWebPath": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesSeriesInstancesDelete"
    ] = healthcare.delete(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "dicomWebPath": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesSeriesInstancesFramesRetrieveRendered"
    ] = healthcare.get(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "parent": t.string().optional(),
                "dicomWebPath": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesSeriesInstancesFramesRetrieveFrames"
    ] = healthcare.get(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "parent": t.string().optional(),
                "dicomWebPath": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresSetIamPolicy"] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresList"] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsHl7V2StoresTestIamPermissions"
    ] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresGet"] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresImport"] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresExport"] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresDelete"] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresCreate"] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresPatch"] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresGetIamPolicy"] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresMessagesIngest"] = healthcare.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresMessagesList"] = healthcare.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresMessagesDelete"] = healthcare.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresMessagesCreate"] = healthcare.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresMessagesPatch"] = healthcare.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresMessagesGet"] = healthcare.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresGetIamPolicy"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "_type": t.string().optional(),
                "_since": t.string().optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"]
                ).optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresCreate"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "_type": t.string().optional(),
                "_since": t.string().optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"]
                ).optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsFhirStoresTestIamPermissions"
    ] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "_type": t.string().optional(),
                "_since": t.string().optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"]
                ).optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsFhirStoresGetFHIRStoreMetrics"
    ] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "_type": t.string().optional(),
                "_since": t.string().optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"]
                ).optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresImport"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "_type": t.string().optional(),
                "_since": t.string().optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"]
                ).optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresSetIamPolicy"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "_type": t.string().optional(),
                "_since": t.string().optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"]
                ).optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresDelete"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "_type": t.string().optional(),
                "_since": t.string().optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"]
                ).optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresPatch"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "_type": t.string().optional(),
                "_since": t.string().optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"]
                ).optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresList"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "_type": t.string().optional(),
                "_since": t.string().optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"]
                ).optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresDeidentify"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "_type": t.string().optional(),
                "_since": t.string().optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"]
                ).optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresGet"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "_type": t.string().optional(),
                "_since": t.string().optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"]
                ).optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresExport"] = healthcare.post(
        "v1/{name}:export",
        t.struct(
            {
                "name": t.string().optional(),
                "_type": t.string().optional(),
                "_since": t.string().optional(),
                "bigqueryDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"]
                ).optional(),
                "gcsDestination": t.proxy(
                    renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsFhirStoresFhirPatient-everything"
    ] = healthcare.delete(
        "v1/{name}/$purge",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsFhirStoresFhirCapabilities"
    ] = healthcare.delete(
        "v1/{name}/$purge",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirSearch"] = healthcare.delete(
        "v1/{name}/$purge",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirDelete"] = healthcare.delete(
        "v1/{name}/$purge",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirRead"] = healthcare.delete(
        "v1/{name}/$purge",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirUpdate"] = healthcare.delete(
        "v1/{name}/$purge",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirCreate"] = healthcare.delete(
        "v1/{name}/$purge",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirSearch-type"] = healthcare.delete(
        "v1/{name}/$purge",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirHistory"] = healthcare.delete(
        "v1/{name}/$purge",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirPatch"] = healthcare.delete(
        "v1/{name}/$purge",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsFhirStoresFhirResource-validate"
    ] = healthcare.delete(
        "v1/{name}/$purge",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsFhirStoresFhirExecuteBundle"
    ] = healthcare.delete(
        "v1/{name}/$purge",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirVread"] = healthcare.delete(
        "v1/{name}/$purge",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsFhirStoresFhirResource-purge"
    ] = healthcare.delete(
        "v1/{name}/$purge",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresSetIamPolicy"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "defaultConsentTtl": t.string().optional(),
                "enableConsentCreateOnUpdate": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresTestIamPermissions"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "defaultConsentTtl": t.string().optional(),
                "enableConsentCreateOnUpdate": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresGet"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "defaultConsentTtl": t.string().optional(),
                "enableConsentCreateOnUpdate": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresQueryAccessibleData"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "defaultConsentTtl": t.string().optional(),
                "enableConsentCreateOnUpdate": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresEvaluateUserConsents"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "defaultConsentTtl": t.string().optional(),
                "enableConsentCreateOnUpdate": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresGetIamPolicy"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "defaultConsentTtl": t.string().optional(),
                "enableConsentCreateOnUpdate": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresCheckDataAccess"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "defaultConsentTtl": t.string().optional(),
                "enableConsentCreateOnUpdate": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresCreate"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "defaultConsentTtl": t.string().optional(),
                "enableConsentCreateOnUpdate": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresList"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "defaultConsentTtl": t.string().optional(),
                "enableConsentCreateOnUpdate": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresDelete"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "defaultConsentTtl": t.string().optional(),
                "enableConsentCreateOnUpdate": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresPatch"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "defaultConsentTtl": t.string().optional(),
                "enableConsentCreateOnUpdate": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsActivate"
    ] = healthcare.post(
        "v1/{name}:revoke",
        t.struct(
            {
                "name": t.string(),
                "consentArtifact": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsList"] = healthcare.post(
        "v1/{name}:revoke",
        t.struct(
            {
                "name": t.string(),
                "consentArtifact": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsDeleteRevision"
    ] = healthcare.post(
        "v1/{name}:revoke",
        t.struct(
            {
                "name": t.string(),
                "consentArtifact": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsListRevisions"
    ] = healthcare.post(
        "v1/{name}:revoke",
        t.struct(
            {
                "name": t.string(),
                "consentArtifact": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsGet"] = healthcare.post(
        "v1/{name}:revoke",
        t.struct(
            {
                "name": t.string(),
                "consentArtifact": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsPatch"] = healthcare.post(
        "v1/{name}:revoke",
        t.struct(
            {
                "name": t.string(),
                "consentArtifact": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsDelete"] = healthcare.post(
        "v1/{name}:revoke",
        t.struct(
            {
                "name": t.string(),
                "consentArtifact": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsReject"] = healthcare.post(
        "v1/{name}:revoke",
        t.struct(
            {
                "name": t.string(),
                "consentArtifact": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsCreate"] = healthcare.post(
        "v1/{name}:revoke",
        t.struct(
            {
                "name": t.string(),
                "consentArtifact": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsRevoke"] = healthcare.post(
        "v1/{name}:revoke",
        t.struct(
            {
                "name": t.string(),
                "consentArtifact": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsGet"
    ] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsArchive"
    ] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsList"
    ] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsCreate"
    ] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsPatch"
    ] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsDelete"
    ] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresAttributeDefinitionsDelete"
    ] = healthcare.get(
        "v1/{parent}/attributeDefinitions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttributeDefinitionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresAttributeDefinitionsCreate"
    ] = healthcare.get(
        "v1/{parent}/attributeDefinitions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttributeDefinitionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresAttributeDefinitionsPatch"
    ] = healthcare.get(
        "v1/{parent}/attributeDefinitions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttributeDefinitionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresAttributeDefinitionsGet"
    ] = healthcare.get(
        "v1/{parent}/attributeDefinitions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttributeDefinitionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresAttributeDefinitionsList"
    ] = healthcare.get(
        "v1/{parent}/attributeDefinitions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttributeDefinitionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentArtifactsDelete"
    ] = healthcare.post(
        "v1/{parent}/consentArtifacts",
        t.struct(
            {
                "parent": t.string(),
                "consentContentVersion": t.string().optional(),
                "guardianSignature": t.proxy(renames["SignatureIn"]).optional(),
                "witnessSignature": t.proxy(renames["SignatureIn"]).optional(),
                "consentContentScreenshots": t.array(
                    t.proxy(renames["ImageIn"])
                ).optional(),
                "name": t.string().optional(),
                "userSignature": t.proxy(renames["SignatureIn"]).optional(),
                "userId": t.string(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentArtifactsList"
    ] = healthcare.post(
        "v1/{parent}/consentArtifacts",
        t.struct(
            {
                "parent": t.string(),
                "consentContentVersion": t.string().optional(),
                "guardianSignature": t.proxy(renames["SignatureIn"]).optional(),
                "witnessSignature": t.proxy(renames["SignatureIn"]).optional(),
                "consentContentScreenshots": t.array(
                    t.proxy(renames["ImageIn"])
                ).optional(),
                "name": t.string().optional(),
                "userSignature": t.proxy(renames["SignatureIn"]).optional(),
                "userId": t.string(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentArtifactsGet"
    ] = healthcare.post(
        "v1/{parent}/consentArtifacts",
        t.struct(
            {
                "parent": t.string(),
                "consentContentVersion": t.string().optional(),
                "guardianSignature": t.proxy(renames["SignatureIn"]).optional(),
                "witnessSignature": t.proxy(renames["SignatureIn"]).optional(),
                "consentContentScreenshots": t.array(
                    t.proxy(renames["ImageIn"])
                ).optional(),
                "name": t.string().optional(),
                "userSignature": t.proxy(renames["SignatureIn"]).optional(),
                "userId": t.string(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentArtifactsCreate"
    ] = healthcare.post(
        "v1/{parent}/consentArtifacts",
        t.struct(
            {
                "parent": t.string(),
                "consentContentVersion": t.string().optional(),
                "guardianSignature": t.proxy(renames["SignatureIn"]).optional(),
                "witnessSignature": t.proxy(renames["SignatureIn"]).optional(),
                "consentContentScreenshots": t.array(
                    t.proxy(renames["ImageIn"])
                ).optional(),
                "name": t.string().optional(),
                "userSignature": t.proxy(renames["SignatureIn"]).optional(),
                "userId": t.string(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsOperationsCancel"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsOperationsList"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsOperationsGet"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="healthcare",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
