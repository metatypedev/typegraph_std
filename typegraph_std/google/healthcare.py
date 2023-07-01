from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_healthcare():
    healthcare = HTTPRuntime("https://healthcare.googleapis.com/")

    renames = {
        "ErrorResponse": "_healthcare_1_ErrorResponse",
        "LinkedEntityIn": "_healthcare_2_LinkedEntityIn",
        "LinkedEntityOut": "_healthcare_3_LinkedEntityOut",
        "ParsedDataIn": "_healthcare_4_ParsedDataIn",
        "ParsedDataOut": "_healthcare_5_ParsedDataOut",
        "ListDatasetsResponseIn": "_healthcare_6_ListDatasetsResponseIn",
        "ListDatasetsResponseOut": "_healthcare_7_ListDatasetsResponseOut",
        "GroupOrSegmentIn": "_healthcare_8_GroupOrSegmentIn",
        "GroupOrSegmentOut": "_healthcare_9_GroupOrSegmentOut",
        "CancelOperationRequestIn": "_healthcare_10_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_healthcare_11_CancelOperationRequestOut",
        "HttpBodyIn": "_healthcare_12_HttpBodyIn",
        "HttpBodyOut": "_healthcare_13_HttpBodyOut",
        "ConsentListIn": "_healthcare_14_ConsentListIn",
        "ConsentListOut": "_healthcare_15_ConsentListOut",
        "ListLocationsResponseIn": "_healthcare_16_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_healthcare_17_ListLocationsResponseOut",
        "GoogleCloudHealthcareV1FhirGcsSourceIn": "_healthcare_18_GoogleCloudHealthcareV1FhirGcsSourceIn",
        "GoogleCloudHealthcareV1FhirGcsSourceOut": "_healthcare_19_GoogleCloudHealthcareV1FhirGcsSourceOut",
        "ValidationConfigIn": "_healthcare_20_ValidationConfigIn",
        "ValidationConfigOut": "_healthcare_21_ValidationConfigOut",
        "CharacterMaskConfigIn": "_healthcare_22_CharacterMaskConfigIn",
        "CharacterMaskConfigOut": "_healthcare_23_CharacterMaskConfigOut",
        "CryptoHashConfigIn": "_healthcare_24_CryptoHashConfigIn",
        "CryptoHashConfigOut": "_healthcare_25_CryptoHashConfigOut",
        "DateShiftConfigIn": "_healthcare_26_DateShiftConfigIn",
        "DateShiftConfigOut": "_healthcare_27_DateShiftConfigOut",
        "ConsentArtifactIn": "_healthcare_28_ConsentArtifactIn",
        "ConsentArtifactOut": "_healthcare_29_ConsentArtifactOut",
        "ConsentEvaluationIn": "_healthcare_30_ConsentEvaluationIn",
        "ConsentEvaluationOut": "_healthcare_31_ConsentEvaluationOut",
        "AuditConfigIn": "_healthcare_32_AuditConfigIn",
        "AuditConfigOut": "_healthcare_33_AuditConfigOut",
        "ExportDicomDataRequestIn": "_healthcare_34_ExportDicomDataRequestIn",
        "ExportDicomDataRequestOut": "_healthcare_35_ExportDicomDataRequestOut",
        "EntityMentionIn": "_healthcare_36_EntityMentionIn",
        "EntityMentionOut": "_healthcare_37_EntityMentionOut",
        "TagFilterListIn": "_healthcare_38_TagFilterListIn",
        "TagFilterListOut": "_healthcare_39_TagFilterListOut",
        "BindingIn": "_healthcare_40_BindingIn",
        "BindingOut": "_healthcare_41_BindingOut",
        "ImportMessagesResponseIn": "_healthcare_42_ImportMessagesResponseIn",
        "ImportMessagesResponseOut": "_healthcare_43_ImportMessagesResponseOut",
        "ExportResourcesRequestIn": "_healthcare_44_ExportResourcesRequestIn",
        "ExportResourcesRequestOut": "_healthcare_45_ExportResourcesRequestOut",
        "FhirConfigIn": "_healthcare_46_FhirConfigIn",
        "FhirConfigOut": "_healthcare_47_FhirConfigOut",
        "ListConsentRevisionsResponseIn": "_healthcare_48_ListConsentRevisionsResponseIn",
        "ListConsentRevisionsResponseOut": "_healthcare_49_ListConsentRevisionsResponseOut",
        "PatientIdIn": "_healthcare_50_PatientIdIn",
        "PatientIdOut": "_healthcare_51_PatientIdOut",
        "TimePartitioningIn": "_healthcare_52_TimePartitioningIn",
        "TimePartitioningOut": "_healthcare_53_TimePartitioningOut",
        "RevokeConsentRequestIn": "_healthcare_54_RevokeConsentRequestIn",
        "RevokeConsentRequestOut": "_healthcare_55_RevokeConsentRequestOut",
        "FieldIn": "_healthcare_56_FieldIn",
        "FieldOut": "_healthcare_57_FieldOut",
        "FhirFilterIn": "_healthcare_58_FhirFilterIn",
        "FhirFilterOut": "_healthcare_59_FhirFilterOut",
        "GoogleCloudHealthcareV1FhirBigQueryDestinationIn": "_healthcare_60_GoogleCloudHealthcareV1FhirBigQueryDestinationIn",
        "GoogleCloudHealthcareV1FhirBigQueryDestinationOut": "_healthcare_61_GoogleCloudHealthcareV1FhirBigQueryDestinationOut",
        "EmptyIn": "_healthcare_62_EmptyIn",
        "EmptyOut": "_healthcare_63_EmptyOut",
        "GcsSourceIn": "_healthcare_64_GcsSourceIn",
        "GcsSourceOut": "_healthcare_65_GcsSourceOut",
        "ListUserDataMappingsResponseIn": "_healthcare_66_ListUserDataMappingsResponseIn",
        "ListUserDataMappingsResponseOut": "_healthcare_67_ListUserDataMappingsResponseOut",
        "ListFhirStoresResponseIn": "_healthcare_68_ListFhirStoresResponseIn",
        "ListFhirStoresResponseOut": "_healthcare_69_ListFhirStoresResponseOut",
        "GoogleCloudHealthcareV1DicomBigQueryDestinationIn": "_healthcare_70_GoogleCloudHealthcareV1DicomBigQueryDestinationIn",
        "GoogleCloudHealthcareV1DicomBigQueryDestinationOut": "_healthcare_71_GoogleCloudHealthcareV1DicomBigQueryDestinationOut",
        "ListOperationsResponseIn": "_healthcare_72_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_healthcare_73_ListOperationsResponseOut",
        "DeidentifyDatasetRequestIn": "_healthcare_74_DeidentifyDatasetRequestIn",
        "DeidentifyDatasetRequestOut": "_healthcare_75_DeidentifyDatasetRequestOut",
        "GoogleCloudHealthcareV1DicomGcsSourceIn": "_healthcare_76_GoogleCloudHealthcareV1DicomGcsSourceIn",
        "GoogleCloudHealthcareV1DicomGcsSourceOut": "_healthcare_77_GoogleCloudHealthcareV1DicomGcsSourceOut",
        "ActivateConsentRequestIn": "_healthcare_78_ActivateConsentRequestIn",
        "ActivateConsentRequestOut": "_healthcare_79_ActivateConsentRequestOut",
        "Hl7SchemaConfigIn": "_healthcare_80_Hl7SchemaConfigIn",
        "Hl7SchemaConfigOut": "_healthcare_81_Hl7SchemaConfigOut",
        "SchematizedDataIn": "_healthcare_82_SchematizedDataIn",
        "SchematizedDataOut": "_healthcare_83_SchematizedDataOut",
        "TestIamPermissionsResponseIn": "_healthcare_84_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_healthcare_85_TestIamPermissionsResponseOut",
        "ImportMessagesRequestIn": "_healthcare_86_ImportMessagesRequestIn",
        "ImportMessagesRequestOut": "_healthcare_87_ImportMessagesRequestOut",
        "Hl7V2StoreIn": "_healthcare_88_Hl7V2StoreIn",
        "Hl7V2StoreOut": "_healthcare_89_Hl7V2StoreOut",
        "MessageIn": "_healthcare_90_MessageIn",
        "MessageOut": "_healthcare_91_MessageOut",
        "LocationIn": "_healthcare_92_LocationIn",
        "LocationOut": "_healthcare_93_LocationOut",
        "FhirNotificationConfigIn": "_healthcare_94_FhirNotificationConfigIn",
        "FhirNotificationConfigOut": "_healthcare_95_FhirNotificationConfigOut",
        "SchemaGroupIn": "_healthcare_96_SchemaGroupIn",
        "SchemaGroupOut": "_healthcare_97_SchemaGroupOut",
        "Hl7TypesConfigIn": "_healthcare_98_Hl7TypesConfigIn",
        "Hl7TypesConfigOut": "_healthcare_99_Hl7TypesConfigOut",
        "EntityIn": "_healthcare_100_EntityIn",
        "EntityOut": "_healthcare_101_EntityOut",
        "CheckDataAccessRequestIn": "_healthcare_102_CheckDataAccessRequestIn",
        "CheckDataAccessRequestOut": "_healthcare_103_CheckDataAccessRequestOut",
        "DeidentifySummaryIn": "_healthcare_104_DeidentifySummaryIn",
        "DeidentifySummaryOut": "_healthcare_105_DeidentifySummaryOut",
        "DeidentifyFhirStoreRequestIn": "_healthcare_106_DeidentifyFhirStoreRequestIn",
        "DeidentifyFhirStoreRequestOut": "_healthcare_107_DeidentifyFhirStoreRequestOut",
        "FhirStoreMetricIn": "_healthcare_108_FhirStoreMetricIn",
        "FhirStoreMetricOut": "_healthcare_109_FhirStoreMetricOut",
        "GoogleCloudHealthcareV1ConsentPolicyIn": "_healthcare_110_GoogleCloudHealthcareV1ConsentPolicyIn",
        "GoogleCloudHealthcareV1ConsentPolicyOut": "_healthcare_111_GoogleCloudHealthcareV1ConsentPolicyOut",
        "Hl7V2NotificationConfigIn": "_healthcare_112_Hl7V2NotificationConfigIn",
        "Hl7V2NotificationConfigOut": "_healthcare_113_Hl7V2NotificationConfigOut",
        "KmsWrappedCryptoKeyIn": "_healthcare_114_KmsWrappedCryptoKeyIn",
        "KmsWrappedCryptoKeyOut": "_healthcare_115_KmsWrappedCryptoKeyOut",
        "DicomFilterConfigIn": "_healthcare_116_DicomFilterConfigIn",
        "DicomFilterConfigOut": "_healthcare_117_DicomFilterConfigOut",
        "ImageIn": "_healthcare_118_ImageIn",
        "ImageOut": "_healthcare_119_ImageOut",
        "ExportDicomDataResponseIn": "_healthcare_120_ExportDicomDataResponseIn",
        "ExportDicomDataResponseOut": "_healthcare_121_ExportDicomDataResponseOut",
        "DeidentifyConfigIn": "_healthcare_122_DeidentifyConfigIn",
        "DeidentifyConfigOut": "_healthcare_123_DeidentifyConfigOut",
        "ConsentStoreIn": "_healthcare_124_ConsentStoreIn",
        "ConsentStoreOut": "_healthcare_125_ConsentStoreOut",
        "EntityMentionRelationshipIn": "_healthcare_126_EntityMentionRelationshipIn",
        "EntityMentionRelationshipOut": "_healthcare_127_EntityMentionRelationshipOut",
        "InfoTypeTransformationIn": "_healthcare_128_InfoTypeTransformationIn",
        "InfoTypeTransformationOut": "_healthcare_129_InfoTypeTransformationOut",
        "QueryAccessibleDataResponseIn": "_healthcare_130_QueryAccessibleDataResponseIn",
        "QueryAccessibleDataResponseOut": "_healthcare_131_QueryAccessibleDataResponseOut",
        "FhirStoreMetricsIn": "_healthcare_132_FhirStoreMetricsIn",
        "FhirStoreMetricsOut": "_healthcare_133_FhirStoreMetricsOut",
        "ListConsentStoresResponseIn": "_healthcare_134_ListConsentStoresResponseIn",
        "ListConsentStoresResponseOut": "_healthcare_135_ListConsentStoresResponseOut",
        "DicomConfigIn": "_healthcare_136_DicomConfigIn",
        "DicomConfigOut": "_healthcare_137_DicomConfigOut",
        "DeidentifyDicomStoreRequestIn": "_healthcare_138_DeidentifyDicomStoreRequestIn",
        "DeidentifyDicomStoreRequestOut": "_healthcare_139_DeidentifyDicomStoreRequestOut",
        "GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryIn": "_healthcare_140_GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryIn",
        "GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryOut": "_healthcare_141_GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryOut",
        "GcsDestinationIn": "_healthcare_142_GcsDestinationIn",
        "GcsDestinationOut": "_healthcare_143_GcsDestinationOut",
        "ProgressCounterIn": "_healthcare_144_ProgressCounterIn",
        "ProgressCounterOut": "_healthcare_145_ProgressCounterOut",
        "ReplaceWithInfoTypeConfigIn": "_healthcare_146_ReplaceWithInfoTypeConfigIn",
        "ReplaceWithInfoTypeConfigOut": "_healthcare_147_ReplaceWithInfoTypeConfigOut",
        "GoogleCloudHealthcareV1ConsentGcsDestinationIn": "_healthcare_148_GoogleCloudHealthcareV1ConsentGcsDestinationIn",
        "GoogleCloudHealthcareV1ConsentGcsDestinationOut": "_healthcare_149_GoogleCloudHealthcareV1ConsentGcsDestinationOut",
        "CreateMessageRequestIn": "_healthcare_150_CreateMessageRequestIn",
        "CreateMessageRequestOut": "_healthcare_151_CreateMessageRequestOut",
        "FieldMetadataIn": "_healthcare_152_FieldMetadataIn",
        "FieldMetadataOut": "_healthcare_153_FieldMetadataOut",
        "ConsentIn": "_healthcare_154_ConsentIn",
        "ConsentOut": "_healthcare_155_ConsentOut",
        "ImportResourcesResponseIn": "_healthcare_156_ImportResourcesResponseIn",
        "ImportResourcesResponseOut": "_healthcare_157_ImportResourcesResponseOut",
        "StatusIn": "_healthcare_158_StatusIn",
        "StatusOut": "_healthcare_159_StatusOut",
        "AnalyzeEntitiesRequestIn": "_healthcare_160_AnalyzeEntitiesRequestIn",
        "AnalyzeEntitiesRequestOut": "_healthcare_161_AnalyzeEntitiesRequestOut",
        "ListConsentsResponseIn": "_healthcare_162_ListConsentsResponseIn",
        "ListConsentsResponseOut": "_healthcare_163_ListConsentsResponseOut",
        "PolicyIn": "_healthcare_164_PolicyIn",
        "PolicyOut": "_healthcare_165_PolicyOut",
        "ListDicomStoresResponseIn": "_healthcare_166_ListDicomStoresResponseIn",
        "ListDicomStoresResponseOut": "_healthcare_167_ListDicomStoresResponseOut",
        "OperationMetadataIn": "_healthcare_168_OperationMetadataIn",
        "OperationMetadataOut": "_healthcare_169_OperationMetadataOut",
        "FhirStoreIn": "_healthcare_170_FhirStoreIn",
        "FhirStoreOut": "_healthcare_171_FhirStoreOut",
        "FeatureIn": "_healthcare_172_FeatureIn",
        "FeatureOut": "_healthcare_173_FeatureOut",
        "ExprIn": "_healthcare_174_ExprIn",
        "ExprOut": "_healthcare_175_ExprOut",
        "SchemaPackageIn": "_healthcare_176_SchemaPackageIn",
        "SchemaPackageOut": "_healthcare_177_SchemaPackageOut",
        "CheckDataAccessResponseIn": "_healthcare_178_CheckDataAccessResponseIn",
        "CheckDataAccessResponseOut": "_healthcare_179_CheckDataAccessResponseOut",
        "IngestMessageResponseIn": "_healthcare_180_IngestMessageResponseIn",
        "IngestMessageResponseOut": "_healthcare_181_IngestMessageResponseOut",
        "DatasetIn": "_healthcare_182_DatasetIn",
        "DatasetOut": "_healthcare_183_DatasetOut",
        "SignatureIn": "_healthcare_184_SignatureIn",
        "SignatureOut": "_healthcare_185_SignatureOut",
        "RejectConsentRequestIn": "_healthcare_186_RejectConsentRequestIn",
        "RejectConsentRequestOut": "_healthcare_187_RejectConsentRequestOut",
        "TextConfigIn": "_healthcare_188_TextConfigIn",
        "TextConfigOut": "_healthcare_189_TextConfigOut",
        "OperationIn": "_healthcare_190_OperationIn",
        "OperationOut": "_healthcare_191_OperationOut",
        "QueryAccessibleDataRequestIn": "_healthcare_192_QueryAccessibleDataRequestIn",
        "QueryAccessibleDataRequestOut": "_healthcare_193_QueryAccessibleDataRequestOut",
        "AttributeIn": "_healthcare_194_AttributeIn",
        "AttributeOut": "_healthcare_195_AttributeOut",
        "ResourcesIn": "_healthcare_196_ResourcesIn",
        "ResourcesOut": "_healthcare_197_ResourcesOut",
        "ImageConfigIn": "_healthcare_198_ImageConfigIn",
        "ImageConfigOut": "_healthcare_199_ImageConfigOut",
        "GoogleCloudHealthcareV1DicomGcsDestinationIn": "_healthcare_200_GoogleCloudHealthcareV1DicomGcsDestinationIn",
        "GoogleCloudHealthcareV1DicomGcsDestinationOut": "_healthcare_201_GoogleCloudHealthcareV1DicomGcsDestinationOut",
        "ResultIn": "_healthcare_202_ResultIn",
        "ResultOut": "_healthcare_203_ResultOut",
        "ImportResourcesRequestIn": "_healthcare_204_ImportResourcesRequestIn",
        "ImportResourcesRequestOut": "_healthcare_205_ImportResourcesRequestOut",
        "GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryIn": "_healthcare_206_GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryIn",
        "GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryOut": "_healthcare_207_GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryOut",
        "AttributeDefinitionIn": "_healthcare_208_AttributeDefinitionIn",
        "AttributeDefinitionOut": "_healthcare_209_AttributeDefinitionOut",
        "StreamConfigIn": "_healthcare_210_StreamConfigIn",
        "StreamConfigOut": "_healthcare_211_StreamConfigOut",
        "SegmentIn": "_healthcare_212_SegmentIn",
        "SegmentOut": "_healthcare_213_SegmentOut",
        "ListAttributeDefinitionsResponseIn": "_healthcare_214_ListAttributeDefinitionsResponseIn",
        "ListAttributeDefinitionsResponseOut": "_healthcare_215_ListAttributeDefinitionsResponseOut",
        "AnalyzeEntitiesResponseIn": "_healthcare_216_AnalyzeEntitiesResponseIn",
        "AnalyzeEntitiesResponseOut": "_healthcare_217_AnalyzeEntitiesResponseOut",
        "SchemaConfigIn": "_healthcare_218_SchemaConfigIn",
        "SchemaConfigOut": "_healthcare_219_SchemaConfigOut",
        "ImportDicomDataRequestIn": "_healthcare_220_ImportDicomDataRequestIn",
        "ImportDicomDataRequestOut": "_healthcare_221_ImportDicomDataRequestOut",
        "TestIamPermissionsRequestIn": "_healthcare_222_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_healthcare_223_TestIamPermissionsRequestOut",
        "ArchiveUserDataMappingRequestIn": "_healthcare_224_ArchiveUserDataMappingRequestIn",
        "ArchiveUserDataMappingRequestOut": "_healthcare_225_ArchiveUserDataMappingRequestOut",
        "RedactConfigIn": "_healthcare_226_RedactConfigIn",
        "RedactConfigOut": "_healthcare_227_RedactConfigOut",
        "UserDataMappingIn": "_healthcare_228_UserDataMappingIn",
        "UserDataMappingOut": "_healthcare_229_UserDataMappingOut",
        "ParserConfigIn": "_healthcare_230_ParserConfigIn",
        "ParserConfigOut": "_healthcare_231_ParserConfigOut",
        "ImportDicomDataResponseIn": "_healthcare_232_ImportDicomDataResponseIn",
        "ImportDicomDataResponseOut": "_healthcare_233_ImportDicomDataResponseOut",
        "ListHl7V2StoresResponseIn": "_healthcare_234_ListHl7V2StoresResponseIn",
        "ListHl7V2StoresResponseOut": "_healthcare_235_ListHl7V2StoresResponseOut",
        "ListMessagesResponseIn": "_healthcare_236_ListMessagesResponseIn",
        "ListMessagesResponseOut": "_healthcare_237_ListMessagesResponseOut",
        "ArchiveUserDataMappingResponseIn": "_healthcare_238_ArchiveUserDataMappingResponseIn",
        "ArchiveUserDataMappingResponseOut": "_healthcare_239_ArchiveUserDataMappingResponseOut",
        "AuditLogConfigIn": "_healthcare_240_AuditLogConfigIn",
        "AuditLogConfigOut": "_healthcare_241_AuditLogConfigOut",
        "ExportMessagesResponseIn": "_healthcare_242_ExportMessagesResponseIn",
        "ExportMessagesResponseOut": "_healthcare_243_ExportMessagesResponseOut",
        "DeidentifiedStoreDestinationIn": "_healthcare_244_DeidentifiedStoreDestinationIn",
        "DeidentifiedStoreDestinationOut": "_healthcare_245_DeidentifiedStoreDestinationOut",
        "VersionSourceIn": "_healthcare_246_VersionSourceIn",
        "VersionSourceOut": "_healthcare_247_VersionSourceOut",
        "GoogleCloudHealthcareV1FhirGcsDestinationIn": "_healthcare_248_GoogleCloudHealthcareV1FhirGcsDestinationIn",
        "GoogleCloudHealthcareV1FhirGcsDestinationOut": "_healthcare_249_GoogleCloudHealthcareV1FhirGcsDestinationOut",
        "TypeIn": "_healthcare_250_TypeIn",
        "TypeOut": "_healthcare_251_TypeOut",
        "ExportResourcesResponseIn": "_healthcare_252_ExportResourcesResponseIn",
        "ExportResourcesResponseOut": "_healthcare_253_ExportResourcesResponseOut",
        "ExportMessagesRequestIn": "_healthcare_254_ExportMessagesRequestIn",
        "ExportMessagesRequestOut": "_healthcare_255_ExportMessagesRequestOut",
        "SearchResourcesRequestIn": "_healthcare_256_SearchResourcesRequestIn",
        "SearchResourcesRequestOut": "_healthcare_257_SearchResourcesRequestOut",
        "EvaluateUserConsentsResponseIn": "_healthcare_258_EvaluateUserConsentsResponseIn",
        "EvaluateUserConsentsResponseOut": "_healthcare_259_EvaluateUserConsentsResponseOut",
        "DicomStoreIn": "_healthcare_260_DicomStoreIn",
        "DicomStoreOut": "_healthcare_261_DicomStoreOut",
        "SchemaSegmentIn": "_healthcare_262_SchemaSegmentIn",
        "SchemaSegmentOut": "_healthcare_263_SchemaSegmentOut",
        "SetIamPolicyRequestIn": "_healthcare_264_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_healthcare_265_SetIamPolicyRequestOut",
        "NotificationConfigIn": "_healthcare_266_NotificationConfigIn",
        "NotificationConfigOut": "_healthcare_267_NotificationConfigOut",
        "TextSpanIn": "_healthcare_268_TextSpanIn",
        "TextSpanOut": "_healthcare_269_TextSpanOut",
        "IngestMessageRequestIn": "_healthcare_270_IngestMessageRequestIn",
        "IngestMessageRequestOut": "_healthcare_271_IngestMessageRequestOut",
        "ListConsentArtifactsResponseIn": "_healthcare_272_ListConsentArtifactsResponseIn",
        "ListConsentArtifactsResponseOut": "_healthcare_273_ListConsentArtifactsResponseOut",
        "EvaluateUserConsentsRequestIn": "_healthcare_274_EvaluateUserConsentsRequestIn",
        "EvaluateUserConsentsRequestOut": "_healthcare_275_EvaluateUserConsentsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LinkedEntityIn"] = t.struct({"entityId": t.string().optional()}).named(
        renames["LinkedEntityIn"]
    )
    types["LinkedEntityOut"] = t.struct(
        {
            "entityId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedEntityOut"])
    types["ParsedDataIn"] = t.struct(
        {"segments": t.array(t.proxy(renames["SegmentIn"]))}
    ).named(renames["ParsedDataIn"])
    types["ParsedDataOut"] = t.struct(
        {
            "segments": t.array(t.proxy(renames["SegmentOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParsedDataOut"])
    types["ListDatasetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "datasets": t.array(t.proxy(renames["DatasetIn"])).optional(),
        }
    ).named(renames["ListDatasetsResponseIn"])
    types["ListDatasetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "datasets": t.array(t.proxy(renames["DatasetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDatasetsResponseOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["HttpBodyIn"] = t.struct(
        {
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "data": t.string().optional(),
            "contentType": t.string().optional(),
        }
    ).named(renames["HttpBodyIn"])
    types["HttpBodyOut"] = t.struct(
        {
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "data": t.string().optional(),
            "contentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpBodyOut"])
    types["ConsentListIn"] = t.struct(
        {"consents": t.array(t.string()).optional()}
    ).named(renames["ConsentListIn"])
    types["ConsentListOut"] = t.struct(
        {
            "consents": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentListOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["GoogleCloudHealthcareV1FhirGcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1FhirGcsSourceIn"])
    types["GoogleCloudHealthcareV1FhirGcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1FhirGcsSourceOut"])
    types["ValidationConfigIn"] = t.struct(
        {
            "disableReferenceTypeValidation": t.boolean().optional(),
            "enabledImplementationGuides": t.array(t.string()).optional(),
            "disableFhirpathValidation": t.boolean().optional(),
            "disableProfileValidation": t.boolean().optional(),
            "disableRequiredFieldValidation": t.boolean().optional(),
        }
    ).named(renames["ValidationConfigIn"])
    types["ValidationConfigOut"] = t.struct(
        {
            "disableReferenceTypeValidation": t.boolean().optional(),
            "enabledImplementationGuides": t.array(t.string()).optional(),
            "disableFhirpathValidation": t.boolean().optional(),
            "disableProfileValidation": t.boolean().optional(),
            "disableRequiredFieldValidation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationConfigOut"])
    types["CharacterMaskConfigIn"] = t.struct(
        {"maskingCharacter": t.string().optional()}
    ).named(renames["CharacterMaskConfigIn"])
    types["CharacterMaskConfigOut"] = t.struct(
        {
            "maskingCharacter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CharacterMaskConfigOut"])
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
    types["DateShiftConfigIn"] = t.struct(
        {
            "cryptoKey": t.string().optional(),
            "kmsWrapped": t.proxy(renames["KmsWrappedCryptoKeyIn"]).optional(),
        }
    ).named(renames["DateShiftConfigIn"])
    types["DateShiftConfigOut"] = t.struct(
        {
            "cryptoKey": t.string().optional(),
            "kmsWrapped": t.proxy(renames["KmsWrappedCryptoKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateShiftConfigOut"])
    types["ConsentArtifactIn"] = t.struct(
        {
            "consentContentScreenshots": t.array(
                t.proxy(renames["ImageIn"])
            ).optional(),
            "witnessSignature": t.proxy(renames["SignatureIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "guardianSignature": t.proxy(renames["SignatureIn"]).optional(),
            "userId": t.string(),
            "userSignature": t.proxy(renames["SignatureIn"]).optional(),
            "consentContentVersion": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ConsentArtifactIn"])
    types["ConsentArtifactOut"] = t.struct(
        {
            "consentContentScreenshots": t.array(
                t.proxy(renames["ImageOut"])
            ).optional(),
            "witnessSignature": t.proxy(renames["SignatureOut"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "guardianSignature": t.proxy(renames["SignatureOut"]).optional(),
            "userId": t.string(),
            "userSignature": t.proxy(renames["SignatureOut"]).optional(),
            "consentContentVersion": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentArtifactOut"])
    types["ConsentEvaluationIn"] = t.struct(
        {"evaluationResult": t.string().optional()}
    ).named(renames["ConsentEvaluationIn"])
    types["ConsentEvaluationOut"] = t.struct(
        {
            "evaluationResult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentEvaluationOut"])
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
    types["EntityMentionIn"] = t.struct(
        {
            "type": t.string().optional(),
            "text": t.proxy(renames["TextSpanIn"]).optional(),
            "temporalAssessment": t.proxy(renames["FeatureIn"]).optional(),
            "subject": t.proxy(renames["FeatureIn"]).optional(),
            "linkedEntities": t.array(t.proxy(renames["LinkedEntityIn"])).optional(),
            "confidence": t.number().optional(),
            "certaintyAssessment": t.proxy(renames["FeatureIn"]).optional(),
            "mentionId": t.string().optional(),
        }
    ).named(renames["EntityMentionIn"])
    types["EntityMentionOut"] = t.struct(
        {
            "type": t.string().optional(),
            "text": t.proxy(renames["TextSpanOut"]).optional(),
            "temporalAssessment": t.proxy(renames["FeatureOut"]).optional(),
            "subject": t.proxy(renames["FeatureOut"]).optional(),
            "linkedEntities": t.array(t.proxy(renames["LinkedEntityOut"])).optional(),
            "confidence": t.number().optional(),
            "certaintyAssessment": t.proxy(renames["FeatureOut"]).optional(),
            "mentionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityMentionOut"])
    types["TagFilterListIn"] = t.struct({"tags": t.array(t.string()).optional()}).named(
        renames["TagFilterListIn"]
    )
    types["TagFilterListOut"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagFilterListOut"])
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
    types["ImportMessagesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ImportMessagesResponseIn"]
    )
    types["ImportMessagesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportMessagesResponseOut"])
    types["ExportResourcesRequestIn"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"]
            ).optional(),
            "_type": t.string().optional(),
            "_since": t.string().optional(),
            "bigqueryDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"]
            ).optional(),
        }
    ).named(renames["ExportResourcesRequestIn"])
    types["ExportResourcesRequestOut"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirGcsDestinationOut"]
            ).optional(),
            "_type": t.string().optional(),
            "_since": t.string().optional(),
            "bigqueryDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirBigQueryDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportResourcesRequestOut"])
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
    types["PatientIdIn"] = t.struct(
        {"value": t.string().optional(), "type": t.string().optional()}
    ).named(renames["PatientIdIn"])
    types["PatientIdOut"] = t.struct(
        {
            "value": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PatientIdOut"])
    types["TimePartitioningIn"] = t.struct(
        {"type": t.string().optional(), "expirationMs": t.string().optional()}
    ).named(renames["TimePartitioningIn"])
    types["TimePartitioningOut"] = t.struct(
        {
            "type": t.string().optional(),
            "expirationMs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimePartitioningOut"])
    types["RevokeConsentRequestIn"] = t.struct(
        {"consentArtifact": t.string().optional()}
    ).named(renames["RevokeConsentRequestIn"])
    types["RevokeConsentRequestOut"] = t.struct(
        {
            "consentArtifact": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevokeConsentRequestOut"])
    types["FieldIn"] = t.struct(
        {
            "table": t.string().optional(),
            "minOccurs": t.integer().optional(),
            "maxOccurs": t.integer().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "table": t.string().optional(),
            "minOccurs": t.integer().optional(),
            "maxOccurs": t.integer().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["FhirFilterIn"] = t.struct(
        {"resources": t.proxy(renames["ResourcesIn"]).optional()}
    ).named(renames["FhirFilterIn"])
    types["FhirFilterOut"] = t.struct(
        {
            "resources": t.proxy(renames["ResourcesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FhirFilterOut"])
    types["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"] = t.struct(
        {
            "force": t.boolean().optional(),
            "datasetUri": t.string().optional(),
            "writeDisposition": t.string().optional(),
            "schemaConfig": t.proxy(renames["SchemaConfigIn"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"])
    types["GoogleCloudHealthcareV1FhirBigQueryDestinationOut"] = t.struct(
        {
            "force": t.boolean().optional(),
            "datasetUri": t.string().optional(),
            "writeDisposition": t.string().optional(),
            "schemaConfig": t.proxy(renames["SchemaConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1FhirBigQueryDestinationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GcsSourceIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["GcsSourceIn"]
    )
    types["GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsSourceOut"])
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
    types["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"] = t.struct(
        {
            "force": t.boolean().optional(),
            "tableUri": t.string().optional(),
            "writeDisposition": t.string().optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"])
    types["GoogleCloudHealthcareV1DicomBigQueryDestinationOut"] = t.struct(
        {
            "force": t.boolean().optional(),
            "tableUri": t.string().optional(),
            "writeDisposition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1DicomBigQueryDestinationOut"])
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
    types["DeidentifyDatasetRequestIn"] = t.struct(
        {
            "destinationDataset": t.string().optional(),
            "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
            "gcsConfigUri": t.string().optional(),
        }
    ).named(renames["DeidentifyDatasetRequestIn"])
    types["DeidentifyDatasetRequestOut"] = t.struct(
        {
            "destinationDataset": t.string().optional(),
            "config": t.proxy(renames["DeidentifyConfigOut"]).optional(),
            "gcsConfigUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeidentifyDatasetRequestOut"])
    types["GoogleCloudHealthcareV1DicomGcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1DicomGcsSourceIn"])
    types["GoogleCloudHealthcareV1DicomGcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1DicomGcsSourceOut"])
    types["ActivateConsentRequestIn"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "consentArtifact": t.string(),
            "ttl": t.string().optional(),
        }
    ).named(renames["ActivateConsentRequestIn"])
    types["ActivateConsentRequestOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "consentArtifact": t.string(),
            "ttl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivateConsentRequestOut"])
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
    types["SchematizedDataIn"] = t.struct(
        {"data": t.string().optional(), "error": t.string().optional()}
    ).named(renames["SchematizedDataIn"])
    types["SchematizedDataOut"] = t.struct(
        {
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchematizedDataOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ImportMessagesRequestIn"] = t.struct(
        {"gcsSource": t.proxy(renames["GcsSourceIn"]).optional()}
    ).named(renames["ImportMessagesRequestIn"])
    types["ImportMessagesRequestOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportMessagesRequestOut"])
    types["Hl7V2StoreIn"] = t.struct(
        {
            "rejectDuplicateMessage": t.boolean().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
            "notificationConfigs": t.array(
                t.proxy(renames["Hl7V2NotificationConfigIn"])
            ).optional(),
        }
    ).named(renames["Hl7V2StoreIn"])
    types["Hl7V2StoreOut"] = t.struct(
        {
            "rejectDuplicateMessage": t.boolean().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "parserConfig": t.proxy(renames["ParserConfigOut"]).optional(),
            "notificationConfigs": t.array(
                t.proxy(renames["Hl7V2NotificationConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Hl7V2StoreOut"])
    types["MessageIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "schematizedData": t.proxy(renames["SchematizedDataIn"]).optional(),
            "data": t.string().optional(),
            "messageType": t.string().optional(),
            "sendFacility": t.string().optional(),
            "sendTime": t.string().optional(),
            "patientIds": t.array(t.proxy(renames["PatientIdIn"])).optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "schematizedData": t.proxy(renames["SchematizedDataOut"]).optional(),
            "data": t.string().optional(),
            "messageType": t.string().optional(),
            "sendFacility": t.string().optional(),
            "sendTime": t.string().optional(),
            "parsedData": t.proxy(renames["ParsedDataOut"]).optional(),
            "patientIds": t.array(t.proxy(renames["PatientIdOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["FhirNotificationConfigIn"] = t.struct(
        {
            "sendPreviousResourceOnDelete": t.boolean().optional(),
            "pubsubTopic": t.string().optional(),
            "sendFullResource": t.boolean().optional(),
        }
    ).named(renames["FhirNotificationConfigIn"])
    types["FhirNotificationConfigOut"] = t.struct(
        {
            "sendPreviousResourceOnDelete": t.boolean().optional(),
            "pubsubTopic": t.string().optional(),
            "sendFullResource": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FhirNotificationConfigOut"])
    types["SchemaGroupIn"] = t.struct(
        {
            "name": t.string().optional(),
            "maxOccurs": t.integer().optional(),
            "minOccurs": t.integer().optional(),
            "choice": t.boolean().optional(),
            "members": t.array(t.proxy(renames["GroupOrSegmentIn"])).optional(),
        }
    ).named(renames["SchemaGroupIn"])
    types["SchemaGroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "maxOccurs": t.integer().optional(),
            "minOccurs": t.integer().optional(),
            "choice": t.boolean().optional(),
            "members": t.array(t.proxy(renames["GroupOrSegmentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaGroupOut"])
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
    types["EntityIn"] = t.struct(
        {
            "vocabularyCodes": t.array(t.string()).optional(),
            "preferredTerm": t.string().optional(),
            "entityId": t.string().optional(),
        }
    ).named(renames["EntityIn"])
    types["EntityOut"] = t.struct(
        {
            "vocabularyCodes": t.array(t.string()).optional(),
            "preferredTerm": t.string().optional(),
            "entityId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityOut"])
    types["CheckDataAccessRequestIn"] = t.struct(
        {
            "requestAttributes": t.struct({"_": t.string().optional()}).optional(),
            "dataId": t.string(),
            "responseView": t.string().optional(),
            "consentList": t.proxy(renames["ConsentListIn"]).optional(),
        }
    ).named(renames["CheckDataAccessRequestIn"])
    types["CheckDataAccessRequestOut"] = t.struct(
        {
            "requestAttributes": t.struct({"_": t.string().optional()}).optional(),
            "dataId": t.string(),
            "responseView": t.string().optional(),
            "consentList": t.proxy(renames["ConsentListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckDataAccessRequestOut"])
    types["DeidentifySummaryIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeidentifySummaryIn"]
    )
    types["DeidentifySummaryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeidentifySummaryOut"])
    types["DeidentifyFhirStoreRequestIn"] = t.struct(
        {
            "gcsConfigUri": t.string().optional(),
            "skipModifiedResources": t.boolean().optional(),
            "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
            "destinationStore": t.string().optional(),
            "resourceFilter": t.proxy(renames["FhirFilterIn"]).optional(),
        }
    ).named(renames["DeidentifyFhirStoreRequestIn"])
    types["DeidentifyFhirStoreRequestOut"] = t.struct(
        {
            "gcsConfigUri": t.string().optional(),
            "skipModifiedResources": t.boolean().optional(),
            "config": t.proxy(renames["DeidentifyConfigOut"]).optional(),
            "destinationStore": t.string().optional(),
            "resourceFilter": t.proxy(renames["FhirFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeidentifyFhirStoreRequestOut"])
    types["FhirStoreMetricIn"] = t.struct(
        {
            "count": t.string().optional(),
            "structuredStorageSizeBytes": t.string().optional(),
            "resourceType": t.string().optional(),
        }
    ).named(renames["FhirStoreMetricIn"])
    types["FhirStoreMetricOut"] = t.struct(
        {
            "count": t.string().optional(),
            "structuredStorageSizeBytes": t.string().optional(),
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FhirStoreMetricOut"])
    types["GoogleCloudHealthcareV1ConsentPolicyIn"] = t.struct(
        {
            "resourceAttributes": t.array(t.proxy(renames["AttributeIn"])).optional(),
            "authorizationRule": t.proxy(renames["ExprIn"]),
        }
    ).named(renames["GoogleCloudHealthcareV1ConsentPolicyIn"])
    types["GoogleCloudHealthcareV1ConsentPolicyOut"] = t.struct(
        {
            "resourceAttributes": t.array(t.proxy(renames["AttributeOut"])).optional(),
            "authorizationRule": t.proxy(renames["ExprOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1ConsentPolicyOut"])
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
    types["DicomFilterConfigIn"] = t.struct(
        {"resourcePathsGcsUri": t.string().optional()}
    ).named(renames["DicomFilterConfigIn"])
    types["DicomFilterConfigOut"] = t.struct(
        {
            "resourcePathsGcsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DicomFilterConfigOut"])
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
    types["ExportDicomDataResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ExportDicomDataResponseIn"]
    )
    types["ExportDicomDataResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExportDicomDataResponseOut"])
    types["DeidentifyConfigIn"] = t.struct(
        {
            "text": t.proxy(renames["TextConfigIn"]).optional(),
            "image": t.proxy(renames["ImageConfigIn"]).optional(),
            "useRegionalDataProcessing": t.boolean().optional(),
            "dicom": t.proxy(renames["DicomConfigIn"]).optional(),
            "fhir": t.proxy(renames["FhirConfigIn"]).optional(),
        }
    ).named(renames["DeidentifyConfigIn"])
    types["DeidentifyConfigOut"] = t.struct(
        {
            "text": t.proxy(renames["TextConfigOut"]).optional(),
            "image": t.proxy(renames["ImageConfigOut"]).optional(),
            "useRegionalDataProcessing": t.boolean().optional(),
            "dicom": t.proxy(renames["DicomConfigOut"]).optional(),
            "fhir": t.proxy(renames["FhirConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeidentifyConfigOut"])
    types["ConsentStoreIn"] = t.struct(
        {
            "enableConsentCreateOnUpdate": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "defaultConsentTtl": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ConsentStoreIn"])
    types["ConsentStoreOut"] = t.struct(
        {
            "enableConsentCreateOnUpdate": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "defaultConsentTtl": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentStoreOut"])
    types["EntityMentionRelationshipIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "subjectId": t.string().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["EntityMentionRelationshipIn"])
    types["EntityMentionRelationshipOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "subjectId": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityMentionRelationshipOut"])
    types["InfoTypeTransformationIn"] = t.struct(
        {
            "redactConfig": t.proxy(renames["RedactConfigIn"]).optional(),
            "infoTypes": t.array(t.string()).optional(),
            "replaceWithInfoTypeConfig": t.proxy(
                renames["ReplaceWithInfoTypeConfigIn"]
            ).optional(),
            "characterMaskConfig": t.proxy(renames["CharacterMaskConfigIn"]).optional(),
            "cryptoHashConfig": t.proxy(renames["CryptoHashConfigIn"]).optional(),
            "dateShiftConfig": t.proxy(renames["DateShiftConfigIn"]).optional(),
        }
    ).named(renames["InfoTypeTransformationIn"])
    types["InfoTypeTransformationOut"] = t.struct(
        {
            "redactConfig": t.proxy(renames["RedactConfigOut"]).optional(),
            "infoTypes": t.array(t.string()).optional(),
            "replaceWithInfoTypeConfig": t.proxy(
                renames["ReplaceWithInfoTypeConfigOut"]
            ).optional(),
            "characterMaskConfig": t.proxy(
                renames["CharacterMaskConfigOut"]
            ).optional(),
            "cryptoHashConfig": t.proxy(renames["CryptoHashConfigOut"]).optional(),
            "dateShiftConfig": t.proxy(renames["DateShiftConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InfoTypeTransformationOut"])
    types["QueryAccessibleDataResponseIn"] = t.struct(
        {"gcsUris": t.array(t.string()).optional()}
    ).named(renames["QueryAccessibleDataResponseIn"])
    types["QueryAccessibleDataResponseOut"] = t.struct(
        {
            "gcsUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryAccessibleDataResponseOut"])
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
    types["ListConsentStoresResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "consentStores": t.array(t.proxy(renames["ConsentStoreIn"])).optional(),
        }
    ).named(renames["ListConsentStoresResponseIn"])
    types["ListConsentStoresResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "consentStores": t.array(t.proxy(renames["ConsentStoreOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConsentStoresResponseOut"])
    types["DicomConfigIn"] = t.struct(
        {
            "skipIdRedaction": t.boolean().optional(),
            "filterProfile": t.string().optional(),
            "removeList": t.proxy(renames["TagFilterListIn"]).optional(),
            "keepList": t.proxy(renames["TagFilterListIn"]).optional(),
        }
    ).named(renames["DicomConfigIn"])
    types["DicomConfigOut"] = t.struct(
        {
            "skipIdRedaction": t.boolean().optional(),
            "filterProfile": t.string().optional(),
            "removeList": t.proxy(renames["TagFilterListOut"]).optional(),
            "keepList": t.proxy(renames["TagFilterListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DicomConfigOut"])
    types["DeidentifyDicomStoreRequestIn"] = t.struct(
        {
            "filterConfig": t.proxy(renames["DicomFilterConfigIn"]).optional(),
            "gcsConfigUri": t.string().optional(),
            "destinationStore": t.string().optional(),
            "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
        }
    ).named(renames["DeidentifyDicomStoreRequestIn"])
    types["DeidentifyDicomStoreRequestOut"] = t.struct(
        {
            "filterConfig": t.proxy(renames["DicomFilterConfigOut"]).optional(),
            "gcsConfigUri": t.string().optional(),
            "destinationStore": t.string().optional(),
            "config": t.proxy(renames["DeidentifyConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeidentifyDicomStoreRequestOut"])
    types["GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryIn"])
    types["GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryOut"])
    types["GcsDestinationIn"] = t.struct(
        {
            "uriPrefix": t.string().optional(),
            "messageView": t.string().optional(),
            "contentStructure": t.string().optional(),
        }
    ).named(renames["GcsDestinationIn"])
    types["GcsDestinationOut"] = t.struct(
        {
            "uriPrefix": t.string().optional(),
            "messageView": t.string().optional(),
            "contentStructure": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsDestinationOut"])
    types["ProgressCounterIn"] = t.struct(
        {
            "failure": t.string().optional(),
            "success": t.string().optional(),
            "pending": t.string().optional(),
        }
    ).named(renames["ProgressCounterIn"])
    types["ProgressCounterOut"] = t.struct(
        {
            "failure": t.string().optional(),
            "success": t.string().optional(),
            "pending": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProgressCounterOut"])
    types["ReplaceWithInfoTypeConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReplaceWithInfoTypeConfigIn"]
    )
    types["ReplaceWithInfoTypeConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReplaceWithInfoTypeConfigOut"])
    types["GoogleCloudHealthcareV1ConsentGcsDestinationIn"] = t.struct(
        {"uriPrefix": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1ConsentGcsDestinationIn"])
    types["GoogleCloudHealthcareV1ConsentGcsDestinationOut"] = t.struct(
        {
            "uriPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1ConsentGcsDestinationOut"])
    types["CreateMessageRequestIn"] = t.struct(
        {"message": t.proxy(renames["MessageIn"]).optional()}
    ).named(renames["CreateMessageRequestIn"])
    types["CreateMessageRequestOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateMessageRequestOut"])
    types["FieldMetadataIn"] = t.struct(
        {"paths": t.array(t.string()).optional(), "action": t.string().optional()}
    ).named(renames["FieldMetadataIn"])
    types["FieldMetadataOut"] = t.struct(
        {
            "paths": t.array(t.string()).optional(),
            "action": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldMetadataOut"])
    types["ConsentIn"] = t.struct(
        {
            "policies": t.array(
                t.proxy(renames["GoogleCloudHealthcareV1ConsentPolicyIn"])
            ).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string(),
            "ttl": t.string().optional(),
            "consentArtifact": t.string(),
            "expireTime": t.string().optional(),
            "userId": t.string(),
        }
    ).named(renames["ConsentIn"])
    types["ConsentOut"] = t.struct(
        {
            "policies": t.array(
                t.proxy(renames["GoogleCloudHealthcareV1ConsentPolicyOut"])
            ).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string(),
            "revisionId": t.string().optional(),
            "ttl": t.string().optional(),
            "consentArtifact": t.string(),
            "revisionCreateTime": t.string().optional(),
            "expireTime": t.string().optional(),
            "userId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentOut"])
    types["ImportResourcesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ImportResourcesResponseIn"]
    )
    types["ImportResourcesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportResourcesResponseOut"])
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
    types["ListConsentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "consents": t.array(t.proxy(renames["ConsentIn"])).optional(),
        }
    ).named(renames["ListConsentsResponseIn"])
    types["ListConsentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "consents": t.array(t.proxy(renames["ConsentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConsentsResponseOut"])
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
    types["ListDicomStoresResponseIn"] = t.struct(
        {
            "dicomStores": t.array(t.proxy(renames["DicomStoreIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDicomStoresResponseIn"])
    types["ListDicomStoresResponseOut"] = t.struct(
        {
            "dicomStores": t.array(t.proxy(renames["DicomStoreOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDicomStoresResponseOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "cancelRequested": t.boolean().optional(),
            "endTime": t.string().optional(),
            "apiMethodName": t.string().optional(),
            "logsUrl": t.string().optional(),
            "counter": t.proxy(renames["ProgressCounterIn"]),
            "createTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "cancelRequested": t.boolean().optional(),
            "endTime": t.string().optional(),
            "apiMethodName": t.string().optional(),
            "logsUrl": t.string().optional(),
            "counter": t.proxy(renames["ProgressCounterOut"]),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["FhirStoreIn"] = t.struct(
        {
            "disableReferentialIntegrity": t.boolean().optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigIn"]).optional(),
            "disableResourceVersioning": t.boolean().optional(),
            "notificationConfigs": t.array(
                t.proxy(renames["FhirNotificationConfigIn"])
            ).optional(),
            "complexDataTypeReferenceParsing": t.string().optional(),
            "streamConfigs": t.array(t.proxy(renames["StreamConfigIn"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "defaultSearchHandlingStrict": t.boolean().optional(),
            "validationConfig": t.proxy(renames["ValidationConfigIn"]).optional(),
            "version": t.string().optional(),
            "name": t.string().optional(),
            "enableUpdateCreate": t.boolean().optional(),
        }
    ).named(renames["FhirStoreIn"])
    types["FhirStoreOut"] = t.struct(
        {
            "disableReferentialIntegrity": t.boolean().optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigOut"]).optional(),
            "disableResourceVersioning": t.boolean().optional(),
            "notificationConfigs": t.array(
                t.proxy(renames["FhirNotificationConfigOut"])
            ).optional(),
            "complexDataTypeReferenceParsing": t.string().optional(),
            "streamConfigs": t.array(t.proxy(renames["StreamConfigOut"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "defaultSearchHandlingStrict": t.boolean().optional(),
            "validationConfig": t.proxy(renames["ValidationConfigOut"]).optional(),
            "version": t.string().optional(),
            "name": t.string().optional(),
            "enableUpdateCreate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FhirStoreOut"])
    types["FeatureIn"] = t.struct(
        {"value": t.string().optional(), "confidence": t.number().optional()}
    ).named(renames["FeatureIn"])
    types["FeatureOut"] = t.struct(
        {
            "value": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["SchemaPackageIn"] = t.struct(
        {
            "schematizedParsingType": t.string().optional(),
            "unexpectedSegmentHandling": t.string().optional(),
            "schemas": t.array(t.proxy(renames["Hl7SchemaConfigIn"])).optional(),
            "types": t.array(t.proxy(renames["Hl7TypesConfigIn"])).optional(),
            "ignoreMinOccurs": t.boolean().optional(),
        }
    ).named(renames["SchemaPackageIn"])
    types["SchemaPackageOut"] = t.struct(
        {
            "schematizedParsingType": t.string().optional(),
            "unexpectedSegmentHandling": t.string().optional(),
            "schemas": t.array(t.proxy(renames["Hl7SchemaConfigOut"])).optional(),
            "types": t.array(t.proxy(renames["Hl7TypesConfigOut"])).optional(),
            "ignoreMinOccurs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaPackageOut"])
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
    types["SignatureIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "signatureTime": t.string().optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "userId": t.string(),
        }
    ).named(renames["SignatureIn"])
    types["SignatureOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "signatureTime": t.string().optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "userId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignatureOut"])
    types["RejectConsentRequestIn"] = t.struct(
        {"consentArtifact": t.string().optional()}
    ).named(renames["RejectConsentRequestIn"])
    types["RejectConsentRequestOut"] = t.struct(
        {
            "consentArtifact": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RejectConsentRequestOut"])
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
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["QueryAccessibleDataRequestIn"] = t.struct(
        {
            "requestAttributes": t.struct({"_": t.string().optional()}).optional(),
            "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudHealthcareV1ConsentGcsDestinationIn"]
            ).optional(),
        }
    ).named(renames["QueryAccessibleDataRequestIn"])
    types["QueryAccessibleDataRequestOut"] = t.struct(
        {
            "requestAttributes": t.struct({"_": t.string().optional()}).optional(),
            "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudHealthcareV1ConsentGcsDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryAccessibleDataRequestOut"])
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
    types["ResourcesIn"] = t.struct(
        {"resources": t.array(t.string()).optional()}
    ).named(renames["ResourcesIn"])
    types["ResourcesOut"] = t.struct(
        {
            "resources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourcesOut"])
    types["ImageConfigIn"] = t.struct(
        {"textRedactionMode": t.string().optional()}
    ).named(renames["ImageConfigIn"])
    types["ImageConfigOut"] = t.struct(
        {
            "textRedactionMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageConfigOut"])
    types["GoogleCloudHealthcareV1DicomGcsDestinationIn"] = t.struct(
        {"uriPrefix": t.string().optional(), "mimeType": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1DicomGcsDestinationIn"])
    types["GoogleCloudHealthcareV1DicomGcsDestinationOut"] = t.struct(
        {
            "uriPrefix": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1DicomGcsDestinationOut"])
    types["ResultIn"] = t.struct(
        {
            "consented": t.boolean().optional(),
            "dataId": t.string().optional(),
            "consentDetails": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ResultIn"])
    types["ResultOut"] = t.struct(
        {
            "consented": t.boolean().optional(),
            "dataId": t.string().optional(),
            "consentDetails": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultOut"])
    types["ImportResourcesRequestIn"] = t.struct(
        {
            "gcsSource": t.proxy(
                renames["GoogleCloudHealthcareV1FhirGcsSourceIn"]
            ).optional(),
            "contentStructure": t.string().optional(),
        }
    ).named(renames["ImportResourcesRequestIn"])
    types["ImportResourcesRequestOut"] = t.struct(
        {
            "gcsSource": t.proxy(
                renames["GoogleCloudHealthcareV1FhirGcsSourceOut"]
            ).optional(),
            "contentStructure": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportResourcesRequestOut"])
    types["GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryIn"])
    types["GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryOut"])
    types["AttributeDefinitionIn"] = t.struct(
        {
            "dataMappingDefaultValue": t.string().optional(),
            "consentDefaultValues": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "category": t.string(),
            "description": t.string().optional(),
            "allowedValues": t.array(t.string()),
        }
    ).named(renames["AttributeDefinitionIn"])
    types["AttributeDefinitionOut"] = t.struct(
        {
            "dataMappingDefaultValue": t.string().optional(),
            "consentDefaultValues": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "category": t.string(),
            "description": t.string().optional(),
            "allowedValues": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeDefinitionOut"])
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
    types["AnalyzeEntitiesResponseIn"] = t.struct(
        {
            "entityMentions": t.array(t.proxy(renames["EntityMentionIn"])).optional(),
            "entities": t.array(t.proxy(renames["EntityIn"])).optional(),
            "relationships": t.array(
                t.proxy(renames["EntityMentionRelationshipIn"])
            ).optional(),
        }
    ).named(renames["AnalyzeEntitiesResponseIn"])
    types["AnalyzeEntitiesResponseOut"] = t.struct(
        {
            "entityMentions": t.array(t.proxy(renames["EntityMentionOut"])).optional(),
            "entities": t.array(t.proxy(renames["EntityOut"])).optional(),
            "relationships": t.array(
                t.proxy(renames["EntityMentionRelationshipOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeEntitiesResponseOut"])
    types["SchemaConfigIn"] = t.struct(
        {
            "lastUpdatedPartitionConfig": t.proxy(
                renames["TimePartitioningIn"]
            ).optional(),
            "schemaType": t.string().optional(),
            "recursiveStructureDepth": t.string().optional(),
        }
    ).named(renames["SchemaConfigIn"])
    types["SchemaConfigOut"] = t.struct(
        {
            "lastUpdatedPartitionConfig": t.proxy(
                renames["TimePartitioningOut"]
            ).optional(),
            "schemaType": t.string().optional(),
            "recursiveStructureDepth": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaConfigOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ArchiveUserDataMappingRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ArchiveUserDataMappingRequestIn"])
    types["ArchiveUserDataMappingRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ArchiveUserDataMappingRequestOut"])
    types["RedactConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RedactConfigIn"]
    )
    types["RedactConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RedactConfigOut"])
    types["UserDataMappingIn"] = t.struct(
        {
            "userId": t.string(),
            "dataId": t.string(),
            "resourceAttributes": t.array(t.proxy(renames["AttributeIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["UserDataMappingIn"])
    types["UserDataMappingOut"] = t.struct(
        {
            "archiveTime": t.string().optional(),
            "userId": t.string(),
            "archived": t.boolean().optional(),
            "dataId": t.string(),
            "resourceAttributes": t.array(t.proxy(renames["AttributeOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserDataMappingOut"])
    types["ParserConfigIn"] = t.struct(
        {
            "version": t.string().optional(),
            "schema": t.proxy(renames["SchemaPackageIn"]).optional(),
            "allowNullHeader": t.boolean().optional(),
            "segmentTerminator": t.string().optional(),
        }
    ).named(renames["ParserConfigIn"])
    types["ParserConfigOut"] = t.struct(
        {
            "version": t.string().optional(),
            "schema": t.proxy(renames["SchemaPackageOut"]).optional(),
            "allowNullHeader": t.boolean().optional(),
            "segmentTerminator": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParserConfigOut"])
    types["ImportDicomDataResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ImportDicomDataResponseIn"]
    )
    types["ImportDicomDataResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportDicomDataResponseOut"])
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
    types["ListMessagesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "hl7V2Messages": t.array(t.proxy(renames["MessageIn"])).optional(),
        }
    ).named(renames["ListMessagesResponseIn"])
    types["ListMessagesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "hl7V2Messages": t.array(t.proxy(renames["MessageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMessagesResponseOut"])
    types["ArchiveUserDataMappingResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ArchiveUserDataMappingResponseIn"])
    types["ArchiveUserDataMappingResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ArchiveUserDataMappingResponseOut"])
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
    types["ExportMessagesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ExportMessagesResponseIn"]
    )
    types["ExportMessagesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExportMessagesResponseOut"])
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
    types["VersionSourceIn"] = t.struct(
        {"mshField": t.string().optional(), "value": t.string().optional()}
    ).named(renames["VersionSourceIn"])
    types["VersionSourceOut"] = t.struct(
        {
            "mshField": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionSourceOut"])
    types["GoogleCloudHealthcareV1FhirGcsDestinationIn"] = t.struct(
        {"uriPrefix": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"])
    types["GoogleCloudHealthcareV1FhirGcsDestinationOut"] = t.struct(
        {
            "uriPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1FhirGcsDestinationOut"])
    types["TypeIn"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
            "primitive": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "primitive": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["ExportResourcesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ExportResourcesResponseIn"]
    )
    types["ExportResourcesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExportResourcesResponseOut"])
    types["ExportMessagesRequestIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["ExportMessagesRequestIn"])
    types["ExportMessagesRequestOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportMessagesRequestOut"])
    types["SearchResourcesRequestIn"] = t.struct(
        {"resourceType": t.string().optional()}
    ).named(renames["SearchResourcesRequestIn"])
    types["SearchResourcesRequestOut"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResourcesRequestOut"])
    types["EvaluateUserConsentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "results": t.array(t.proxy(renames["ResultIn"])).optional(),
        }
    ).named(renames["EvaluateUserConsentsResponseIn"])
    types["EvaluateUserConsentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "results": t.array(t.proxy(renames["ResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EvaluateUserConsentsResponseOut"])
    types["DicomStoreIn"] = t.struct(
        {
            "notificationConfig": t.proxy(renames["NotificationConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DicomStoreIn"])
    types["DicomStoreOut"] = t.struct(
        {
            "notificationConfig": t.proxy(renames["NotificationConfigOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DicomStoreOut"])
    types["SchemaSegmentIn"] = t.struct(
        {
            "minOccurs": t.integer().optional(),
            "maxOccurs": t.integer().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["SchemaSegmentIn"])
    types["SchemaSegmentOut"] = t.struct(
        {
            "minOccurs": t.integer().optional(),
            "maxOccurs": t.integer().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaSegmentOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["NotificationConfigIn"] = t.struct(
        {"pubsubTopic": t.string().optional()}
    ).named(renames["NotificationConfigIn"])
    types["NotificationConfigOut"] = t.struct(
        {
            "pubsubTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationConfigOut"])
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
    types["IngestMessageRequestIn"] = t.struct(
        {"message": t.proxy(renames["MessageIn"]).optional()}
    ).named(renames["IngestMessageRequestIn"])
    types["IngestMessageRequestOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IngestMessageRequestOut"])
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
    types["EvaluateUserConsentsRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "requestAttributes": t.struct({"_": t.string().optional()}),
            "pageSize": t.integer().optional(),
            "responseView": t.string().optional(),
            "consentList": t.proxy(renames["ConsentListIn"]).optional(),
            "userId": t.string(),
            "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["EvaluateUserConsentsRequestIn"])
    types["EvaluateUserConsentsRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "requestAttributes": t.struct({"_": t.string().optional()}),
            "pageSize": t.integer().optional(),
            "responseView": t.string().optional(),
            "consentList": t.proxy(renames["ConsentListOut"]).optional(),
            "userId": t.string(),
            "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EvaluateUserConsentsRequestOut"])

    functions = {}
    functions["projectsLocationsList"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
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
    functions["projectsLocationsDatasetsGetIamPolicy"] = healthcare.post(
        "v1/{sourceDataset}:deidentify",
        t.struct(
            {
                "sourceDataset": t.string().optional(),
                "destinationDataset": t.string().optional(),
                "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
                "gcsConfigUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDelete"] = healthcare.post(
        "v1/{sourceDataset}:deidentify",
        t.struct(
            {
                "sourceDataset": t.string().optional(),
                "destinationDataset": t.string().optional(),
                "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
                "gcsConfigUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsTestIamPermissions"] = healthcare.post(
        "v1/{sourceDataset}:deidentify",
        t.struct(
            {
                "sourceDataset": t.string().optional(),
                "destinationDataset": t.string().optional(),
                "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
                "gcsConfigUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsGet"] = healthcare.post(
        "v1/{sourceDataset}:deidentify",
        t.struct(
            {
                "sourceDataset": t.string().optional(),
                "destinationDataset": t.string().optional(),
                "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
                "gcsConfigUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsSetIamPolicy"] = healthcare.post(
        "v1/{sourceDataset}:deidentify",
        t.struct(
            {
                "sourceDataset": t.string().optional(),
                "destinationDataset": t.string().optional(),
                "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
                "gcsConfigUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsPatch"] = healthcare.post(
        "v1/{sourceDataset}:deidentify",
        t.struct(
            {
                "sourceDataset": t.string().optional(),
                "destinationDataset": t.string().optional(),
                "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
                "gcsConfigUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsList"] = healthcare.post(
        "v1/{sourceDataset}:deidentify",
        t.struct(
            {
                "sourceDataset": t.string().optional(),
                "destinationDataset": t.string().optional(),
                "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
                "gcsConfigUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsCreate"] = healthcare.post(
        "v1/{sourceDataset}:deidentify",
        t.struct(
            {
                "sourceDataset": t.string().optional(),
                "destinationDataset": t.string().optional(),
                "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
                "gcsConfigUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDeidentify"] = healthcare.post(
        "v1/{sourceDataset}:deidentify",
        t.struct(
            {
                "sourceDataset": t.string().optional(),
                "destinationDataset": t.string().optional(),
                "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
                "gcsConfigUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresSearchForSeries"
    ] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresSetIamPolicy"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresList"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresDeidentify"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresExport"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresGet"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresImport"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresStoreInstances"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresTestIamPermissions"
    ] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresGetIamPolicy"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresPatch"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresCreate"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresSearchForStudies"
    ] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresSearchForInstances"
    ] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresDelete"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    ] = healthcare.delete(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "parent": t.string().optional(),
                "dicomWebPath": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesSeriesRetrieveSeries"
    ] = healthcare.delete(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "parent": t.string().optional(),
                "dicomWebPath": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesSeriesSearchForInstances"
    ] = healthcare.delete(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "parent": t.string().optional(),
                "dicomWebPath": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesSeriesDelete"
    ] = healthcare.delete(
        "v1/{parent}/dicomWeb/{dicomWebPath}",
        t.struct(
            {
                "parent": t.string().optional(),
                "dicomWebPath": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesSeriesInstancesDelete"
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
        "projectsLocationsDatasetsDicomStoresStudiesSeriesInstancesRetrieveRendered"
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
        "projectsLocationsDatasetsDicomStoresStudiesSeriesInstancesRetrieveInstance"
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
        "projectsLocationsDatasetsDicomStoresStudiesSeriesInstancesRetrieveMetadata"
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
        "projectsLocationsDatasetsDicomStoresStudiesSeriesInstancesFramesRetrieveFrames"
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
        "projectsLocationsDatasetsDicomStoresStudiesSeriesInstancesFramesRetrieveRendered"
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
    functions["projectsLocationsDatasetsOperationsCancel"] = healthcare.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsOperationsGet"] = healthcare.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsOperationsList"] = healthcare.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresSetIamPolicy"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresList"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresGet"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresImport"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresExport"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresCreate"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresDelete"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresGetIamPolicy"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsHl7V2StoresTestIamPermissions"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresPatch"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresMessagesCreate"] = healthcare.post(
        "v1/{parent}/messages:ingest",
        t.struct(
            {
                "parent": t.string().optional(),
                "message": t.proxy(renames["MessageIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IngestMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresMessagesGet"] = healthcare.post(
        "v1/{parent}/messages:ingest",
        t.struct(
            {
                "parent": t.string().optional(),
                "message": t.proxy(renames["MessageIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IngestMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresMessagesDelete"] = healthcare.post(
        "v1/{parent}/messages:ingest",
        t.struct(
            {
                "parent": t.string().optional(),
                "message": t.proxy(renames["MessageIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IngestMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresMessagesList"] = healthcare.post(
        "v1/{parent}/messages:ingest",
        t.struct(
            {
                "parent": t.string().optional(),
                "message": t.proxy(renames["MessageIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IngestMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresMessagesPatch"] = healthcare.post(
        "v1/{parent}/messages:ingest",
        t.struct(
            {
                "parent": t.string().optional(),
                "message": t.proxy(renames["MessageIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IngestMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresMessagesIngest"] = healthcare.post(
        "v1/{parent}/messages:ingest",
        t.struct(
            {
                "parent": t.string().optional(),
                "message": t.proxy(renames["MessageIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IngestMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresPatch"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresDelete"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresCreate"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresTestIamPermissions"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresExport"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresSetIamPolicy"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsFhirStoresGetFHIRStoreMetrics"
    ] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresImport"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresList"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresGetIamPolicy"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresDeidentify"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresGet"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsFhirStoresFhirPatient_everything"
    ] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirHistory"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirCapabilities"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirDelete"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirCreate"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirExecuteBundle"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirPatch"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirUpdate"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsFhirStoresFhirResource_validate"
    ] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirSearch"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirResource_purge"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirVread"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirSearch_type"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirRead"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresEvaluateUserConsents"
    ] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresSetIamPolicy"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresCheckDataAccess"
    ] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresTestIamPermissions"
    ] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresGetIamPolicy"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresCreate"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresList"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresPatch"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresQueryAccessibleData"
    ] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresGet"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresDelete"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsGet"] = healthcare.delete(
        "v1/{name}:deleteRevision",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsCreate"
    ] = healthcare.delete(
        "v1/{name}:deleteRevision",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsRevoke"
    ] = healthcare.delete(
        "v1/{name}:deleteRevision",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsReject"
    ] = healthcare.delete(
        "v1/{name}:deleteRevision",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsList"] = healthcare.delete(
        "v1/{name}:deleteRevision",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsPatch"
    ] = healthcare.delete(
        "v1/{name}:deleteRevision",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsListRevisions"
    ] = healthcare.delete(
        "v1/{name}:deleteRevision",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsDelete"
    ] = healthcare.delete(
        "v1/{name}:deleteRevision",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsActivate"
    ] = healthcare.delete(
        "v1/{name}:deleteRevision",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsDeleteRevision"
    ] = healthcare.delete(
        "v1/{name}:deleteRevision",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresAttributeDefinitionsDelete"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "dataMappingDefaultValue": t.string().optional(),
                "consentDefaultValues": t.array(t.string()).optional(),
                "category": t.string(),
                "description": t.string().optional(),
                "allowedValues": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttributeDefinitionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresAttributeDefinitionsList"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "dataMappingDefaultValue": t.string().optional(),
                "consentDefaultValues": t.array(t.string()).optional(),
                "category": t.string(),
                "description": t.string().optional(),
                "allowedValues": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttributeDefinitionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresAttributeDefinitionsGet"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "dataMappingDefaultValue": t.string().optional(),
                "consentDefaultValues": t.array(t.string()).optional(),
                "category": t.string(),
                "description": t.string().optional(),
                "allowedValues": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttributeDefinitionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresAttributeDefinitionsCreate"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "dataMappingDefaultValue": t.string().optional(),
                "consentDefaultValues": t.array(t.string()).optional(),
                "category": t.string(),
                "description": t.string().optional(),
                "allowedValues": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttributeDefinitionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresAttributeDefinitionsPatch"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "dataMappingDefaultValue": t.string().optional(),
                "consentDefaultValues": t.array(t.string()).optional(),
                "category": t.string(),
                "description": t.string().optional(),
                "allowedValues": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttributeDefinitionOut"]),
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
                "consentContentScreenshots": t.array(
                    t.proxy(renames["ImageIn"])
                ).optional(),
                "witnessSignature": t.proxy(renames["SignatureIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "guardianSignature": t.proxy(renames["SignatureIn"]).optional(),
                "userId": t.string(),
                "userSignature": t.proxy(renames["SignatureIn"]).optional(),
                "consentContentVersion": t.string().optional(),
                "name": t.string().optional(),
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
                "consentContentScreenshots": t.array(
                    t.proxy(renames["ImageIn"])
                ).optional(),
                "witnessSignature": t.proxy(renames["SignatureIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "guardianSignature": t.proxy(renames["SignatureIn"]).optional(),
                "userId": t.string(),
                "userSignature": t.proxy(renames["SignatureIn"]).optional(),
                "consentContentVersion": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentArtifactOut"]),
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
                "consentContentScreenshots": t.array(
                    t.proxy(renames["ImageIn"])
                ).optional(),
                "witnessSignature": t.proxy(renames["SignatureIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "guardianSignature": t.proxy(renames["SignatureIn"]).optional(),
                "userId": t.string(),
                "userSignature": t.proxy(renames["SignatureIn"]).optional(),
                "consentContentVersion": t.string().optional(),
                "name": t.string().optional(),
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
                "consentContentScreenshots": t.array(
                    t.proxy(renames["ImageIn"])
                ).optional(),
                "witnessSignature": t.proxy(renames["SignatureIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "guardianSignature": t.proxy(renames["SignatureIn"]).optional(),
                "userId": t.string(),
                "userSignature": t.proxy(renames["SignatureIn"]).optional(),
                "consentContentVersion": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsDelete"
    ] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["UserDataMappingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsCreate"
    ] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["UserDataMappingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsList"
    ] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["UserDataMappingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsArchive"
    ] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["UserDataMappingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsPatch"
    ] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["UserDataMappingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsGet"
    ] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["UserDataMappingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="healthcare",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
