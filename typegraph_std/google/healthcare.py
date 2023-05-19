from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_healthcare() -> Import:
    healthcare = HTTPRuntime("https://healthcare.googleapis.com/")

    renames = {
        "ErrorResponse": "_healthcare_1_ErrorResponse",
        "CancelOperationRequestIn": "_healthcare_2_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_healthcare_3_CancelOperationRequestOut",
        "DeidentifyDicomStoreRequestIn": "_healthcare_4_DeidentifyDicomStoreRequestIn",
        "DeidentifyDicomStoreRequestOut": "_healthcare_5_DeidentifyDicomStoreRequestOut",
        "CreateMessageRequestIn": "_healthcare_6_CreateMessageRequestIn",
        "CreateMessageRequestOut": "_healthcare_7_CreateMessageRequestOut",
        "FhirStoreIn": "_healthcare_8_FhirStoreIn",
        "FhirStoreOut": "_healthcare_9_FhirStoreOut",
        "EvaluateUserConsentsResponseIn": "_healthcare_10_EvaluateUserConsentsResponseIn",
        "EvaluateUserConsentsResponseOut": "_healthcare_11_EvaluateUserConsentsResponseOut",
        "ReplaceWithInfoTypeConfigIn": "_healthcare_12_ReplaceWithInfoTypeConfigIn",
        "ReplaceWithInfoTypeConfigOut": "_healthcare_13_ReplaceWithInfoTypeConfigOut",
        "ResultIn": "_healthcare_14_ResultIn",
        "ResultOut": "_healthcare_15_ResultOut",
        "ListAttributeDefinitionsResponseIn": "_healthcare_16_ListAttributeDefinitionsResponseIn",
        "ListAttributeDefinitionsResponseOut": "_healthcare_17_ListAttributeDefinitionsResponseOut",
        "ProgressCounterIn": "_healthcare_18_ProgressCounterIn",
        "ProgressCounterOut": "_healthcare_19_ProgressCounterOut",
        "RejectConsentRequestIn": "_healthcare_20_RejectConsentRequestIn",
        "RejectConsentRequestOut": "_healthcare_21_RejectConsentRequestOut",
        "AttributeDefinitionIn": "_healthcare_22_AttributeDefinitionIn",
        "AttributeDefinitionOut": "_healthcare_23_AttributeDefinitionOut",
        "DicomFilterConfigIn": "_healthcare_24_DicomFilterConfigIn",
        "DicomFilterConfigOut": "_healthcare_25_DicomFilterConfigOut",
        "SchemaSegmentIn": "_healthcare_26_SchemaSegmentIn",
        "SchemaSegmentOut": "_healthcare_27_SchemaSegmentOut",
        "FhirFilterIn": "_healthcare_28_FhirFilterIn",
        "FhirFilterOut": "_healthcare_29_FhirFilterOut",
        "GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryIn": "_healthcare_30_GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryIn",
        "GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryOut": "_healthcare_31_GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryOut",
        "SchemaPackageIn": "_healthcare_32_SchemaPackageIn",
        "SchemaPackageOut": "_healthcare_33_SchemaPackageOut",
        "DeidentifyConfigIn": "_healthcare_34_DeidentifyConfigIn",
        "DeidentifyConfigOut": "_healthcare_35_DeidentifyConfigOut",
        "DicomStoreIn": "_healthcare_36_DicomStoreIn",
        "DicomStoreOut": "_healthcare_37_DicomStoreOut",
        "ResourcesIn": "_healthcare_38_ResourcesIn",
        "ResourcesOut": "_healthcare_39_ResourcesOut",
        "RevokeConsentRequestIn": "_healthcare_40_RevokeConsentRequestIn",
        "RevokeConsentRequestOut": "_healthcare_41_RevokeConsentRequestOut",
        "CharacterMaskConfigIn": "_healthcare_42_CharacterMaskConfigIn",
        "CharacterMaskConfigOut": "_healthcare_43_CharacterMaskConfigOut",
        "GoogleCloudHealthcareV1FhirGcsDestinationIn": "_healthcare_44_GoogleCloudHealthcareV1FhirGcsDestinationIn",
        "GoogleCloudHealthcareV1FhirGcsDestinationOut": "_healthcare_45_GoogleCloudHealthcareV1FhirGcsDestinationOut",
        "SchemaConfigIn": "_healthcare_46_SchemaConfigIn",
        "SchemaConfigOut": "_healthcare_47_SchemaConfigOut",
        "ImportMessagesRequestIn": "_healthcare_48_ImportMessagesRequestIn",
        "ImportMessagesRequestOut": "_healthcare_49_ImportMessagesRequestOut",
        "GoogleCloudHealthcareV1ConsentGcsDestinationIn": "_healthcare_50_GoogleCloudHealthcareV1ConsentGcsDestinationIn",
        "GoogleCloudHealthcareV1ConsentGcsDestinationOut": "_healthcare_51_GoogleCloudHealthcareV1ConsentGcsDestinationOut",
        "AuditConfigIn": "_healthcare_52_AuditConfigIn",
        "AuditConfigOut": "_healthcare_53_AuditConfigOut",
        "ImportDicomDataResponseIn": "_healthcare_54_ImportDicomDataResponseIn",
        "ImportDicomDataResponseOut": "_healthcare_55_ImportDicomDataResponseOut",
        "ParsedDataIn": "_healthcare_56_ParsedDataIn",
        "ParsedDataOut": "_healthcare_57_ParsedDataOut",
        "ListConsentsResponseIn": "_healthcare_58_ListConsentsResponseIn",
        "ListConsentsResponseOut": "_healthcare_59_ListConsentsResponseOut",
        "OperationMetadataIn": "_healthcare_60_OperationMetadataIn",
        "OperationMetadataOut": "_healthcare_61_OperationMetadataOut",
        "ExportDicomDataResponseIn": "_healthcare_62_ExportDicomDataResponseIn",
        "ExportDicomDataResponseOut": "_healthcare_63_ExportDicomDataResponseOut",
        "GcsSourceIn": "_healthcare_64_GcsSourceIn",
        "GcsSourceOut": "_healthcare_65_GcsSourceOut",
        "QueryAccessibleDataRequestIn": "_healthcare_66_QueryAccessibleDataRequestIn",
        "QueryAccessibleDataRequestOut": "_healthcare_67_QueryAccessibleDataRequestOut",
        "VersionSourceIn": "_healthcare_68_VersionSourceIn",
        "VersionSourceOut": "_healthcare_69_VersionSourceOut",
        "FhirStoreMetricsIn": "_healthcare_70_FhirStoreMetricsIn",
        "FhirStoreMetricsOut": "_healthcare_71_FhirStoreMetricsOut",
        "SchematizedDataIn": "_healthcare_72_SchematizedDataIn",
        "SchematizedDataOut": "_healthcare_73_SchematizedDataOut",
        "PatientIdIn": "_healthcare_74_PatientIdIn",
        "PatientIdOut": "_healthcare_75_PatientIdOut",
        "ActivateConsentRequestIn": "_healthcare_76_ActivateConsentRequestIn",
        "ActivateConsentRequestOut": "_healthcare_77_ActivateConsentRequestOut",
        "ListDicomStoresResponseIn": "_healthcare_78_ListDicomStoresResponseIn",
        "ListDicomStoresResponseOut": "_healthcare_79_ListDicomStoresResponseOut",
        "ConsentArtifactIn": "_healthcare_80_ConsentArtifactIn",
        "ConsentArtifactOut": "_healthcare_81_ConsentArtifactOut",
        "FieldIn": "_healthcare_82_FieldIn",
        "FieldOut": "_healthcare_83_FieldOut",
        "InfoTypeTransformationIn": "_healthcare_84_InfoTypeTransformationIn",
        "InfoTypeTransformationOut": "_healthcare_85_InfoTypeTransformationOut",
        "FeatureIn": "_healthcare_86_FeatureIn",
        "FeatureOut": "_healthcare_87_FeatureOut",
        "ImportResourcesRequestIn": "_healthcare_88_ImportResourcesRequestIn",
        "ImportResourcesRequestOut": "_healthcare_89_ImportResourcesRequestOut",
        "ListLocationsResponseIn": "_healthcare_90_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_healthcare_91_ListLocationsResponseOut",
        "ListFhirStoresResponseIn": "_healthcare_92_ListFhirStoresResponseIn",
        "ListFhirStoresResponseOut": "_healthcare_93_ListFhirStoresResponseOut",
        "NotificationConfigIn": "_healthcare_94_NotificationConfigIn",
        "NotificationConfigOut": "_healthcare_95_NotificationConfigOut",
        "ExportMessagesRequestIn": "_healthcare_96_ExportMessagesRequestIn",
        "ExportMessagesRequestOut": "_healthcare_97_ExportMessagesRequestOut",
        "GcsDestinationIn": "_healthcare_98_GcsDestinationIn",
        "GcsDestinationOut": "_healthcare_99_GcsDestinationOut",
        "EntityIn": "_healthcare_100_EntityIn",
        "EntityOut": "_healthcare_101_EntityOut",
        "GoogleCloudHealthcareV1FhirBigQueryDestinationIn": "_healthcare_102_GoogleCloudHealthcareV1FhirBigQueryDestinationIn",
        "GoogleCloudHealthcareV1FhirBigQueryDestinationOut": "_healthcare_103_GoogleCloudHealthcareV1FhirBigQueryDestinationOut",
        "SegmentIn": "_healthcare_104_SegmentIn",
        "SegmentOut": "_healthcare_105_SegmentOut",
        "DeidentifyFhirStoreRequestIn": "_healthcare_106_DeidentifyFhirStoreRequestIn",
        "DeidentifyFhirStoreRequestOut": "_healthcare_107_DeidentifyFhirStoreRequestOut",
        "FhirStoreMetricIn": "_healthcare_108_FhirStoreMetricIn",
        "FhirStoreMetricOut": "_healthcare_109_FhirStoreMetricOut",
        "ValidationConfigIn": "_healthcare_110_ValidationConfigIn",
        "ValidationConfigOut": "_healthcare_111_ValidationConfigOut",
        "EntityMentionIn": "_healthcare_112_EntityMentionIn",
        "EntityMentionOut": "_healthcare_113_EntityMentionOut",
        "Hl7TypesConfigIn": "_healthcare_114_Hl7TypesConfigIn",
        "Hl7TypesConfigOut": "_healthcare_115_Hl7TypesConfigOut",
        "ParserConfigIn": "_healthcare_116_ParserConfigIn",
        "ParserConfigOut": "_healthcare_117_ParserConfigOut",
        "SchemaGroupIn": "_healthcare_118_SchemaGroupIn",
        "SchemaGroupOut": "_healthcare_119_SchemaGroupOut",
        "CheckDataAccessResponseIn": "_healthcare_120_CheckDataAccessResponseIn",
        "CheckDataAccessResponseOut": "_healthcare_121_CheckDataAccessResponseOut",
        "SetIamPolicyRequestIn": "_healthcare_122_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_healthcare_123_SetIamPolicyRequestOut",
        "DeidentifiedStoreDestinationIn": "_healthcare_124_DeidentifiedStoreDestinationIn",
        "DeidentifiedStoreDestinationOut": "_healthcare_125_DeidentifiedStoreDestinationOut",
        "ListConsentArtifactsResponseIn": "_healthcare_126_ListConsentArtifactsResponseIn",
        "ListConsentArtifactsResponseOut": "_healthcare_127_ListConsentArtifactsResponseOut",
        "ConsentListIn": "_healthcare_128_ConsentListIn",
        "ConsentListOut": "_healthcare_129_ConsentListOut",
        "TextSpanIn": "_healthcare_130_TextSpanIn",
        "TextSpanOut": "_healthcare_131_TextSpanOut",
        "FhirConfigIn": "_healthcare_132_FhirConfigIn",
        "FhirConfigOut": "_healthcare_133_FhirConfigOut",
        "FhirNotificationConfigIn": "_healthcare_134_FhirNotificationConfigIn",
        "FhirNotificationConfigOut": "_healthcare_135_FhirNotificationConfigOut",
        "ImageIn": "_healthcare_136_ImageIn",
        "ImageOut": "_healthcare_137_ImageOut",
        "IngestMessageRequestIn": "_healthcare_138_IngestMessageRequestIn",
        "IngestMessageRequestOut": "_healthcare_139_IngestMessageRequestOut",
        "TagFilterListIn": "_healthcare_140_TagFilterListIn",
        "TagFilterListOut": "_healthcare_141_TagFilterListOut",
        "OperationIn": "_healthcare_142_OperationIn",
        "OperationOut": "_healthcare_143_OperationOut",
        "ArchiveUserDataMappingResponseIn": "_healthcare_144_ArchiveUserDataMappingResponseIn",
        "ArchiveUserDataMappingResponseOut": "_healthcare_145_ArchiveUserDataMappingResponseOut",
        "ExprIn": "_healthcare_146_ExprIn",
        "ExprOut": "_healthcare_147_ExprOut",
        "ListDatasetsResponseIn": "_healthcare_148_ListDatasetsResponseIn",
        "ListDatasetsResponseOut": "_healthcare_149_ListDatasetsResponseOut",
        "Hl7V2NotificationConfigIn": "_healthcare_150_Hl7V2NotificationConfigIn",
        "Hl7V2NotificationConfigOut": "_healthcare_151_Hl7V2NotificationConfigOut",
        "GroupOrSegmentIn": "_healthcare_152_GroupOrSegmentIn",
        "GroupOrSegmentOut": "_healthcare_153_GroupOrSegmentOut",
        "GoogleCloudHealthcareV1DicomBigQueryDestinationIn": "_healthcare_154_GoogleCloudHealthcareV1DicomBigQueryDestinationIn",
        "GoogleCloudHealthcareV1DicomBigQueryDestinationOut": "_healthcare_155_GoogleCloudHealthcareV1DicomBigQueryDestinationOut",
        "EmptyIn": "_healthcare_156_EmptyIn",
        "EmptyOut": "_healthcare_157_EmptyOut",
        "ListConsentStoresResponseIn": "_healthcare_158_ListConsentStoresResponseIn",
        "ListConsentStoresResponseOut": "_healthcare_159_ListConsentStoresResponseOut",
        "TimePartitioningIn": "_healthcare_160_TimePartitioningIn",
        "TimePartitioningOut": "_healthcare_161_TimePartitioningOut",
        "TextConfigIn": "_healthcare_162_TextConfigIn",
        "TextConfigOut": "_healthcare_163_TextConfigOut",
        "HttpBodyIn": "_healthcare_164_HttpBodyIn",
        "HttpBodyOut": "_healthcare_165_HttpBodyOut",
        "AnalyzeEntitiesRequestIn": "_healthcare_166_AnalyzeEntitiesRequestIn",
        "AnalyzeEntitiesRequestOut": "_healthcare_167_AnalyzeEntitiesRequestOut",
        "EntityMentionRelationshipIn": "_healthcare_168_EntityMentionRelationshipIn",
        "EntityMentionRelationshipOut": "_healthcare_169_EntityMentionRelationshipOut",
        "DateShiftConfigIn": "_healthcare_170_DateShiftConfigIn",
        "DateShiftConfigOut": "_healthcare_171_DateShiftConfigOut",
        "LocationIn": "_healthcare_172_LocationIn",
        "LocationOut": "_healthcare_173_LocationOut",
        "DicomConfigIn": "_healthcare_174_DicomConfigIn",
        "DicomConfigOut": "_healthcare_175_DicomConfigOut",
        "AttributeIn": "_healthcare_176_AttributeIn",
        "AttributeOut": "_healthcare_177_AttributeOut",
        "ExportResourcesResponseIn": "_healthcare_178_ExportResourcesResponseIn",
        "ExportResourcesResponseOut": "_healthcare_179_ExportResourcesResponseOut",
        "DeidentifySummaryIn": "_healthcare_180_DeidentifySummaryIn",
        "DeidentifySummaryOut": "_healthcare_181_DeidentifySummaryOut",
        "IngestMessageResponseIn": "_healthcare_182_IngestMessageResponseIn",
        "IngestMessageResponseOut": "_healthcare_183_IngestMessageResponseOut",
        "ListConsentRevisionsResponseIn": "_healthcare_184_ListConsentRevisionsResponseIn",
        "ListConsentRevisionsResponseOut": "_healthcare_185_ListConsentRevisionsResponseOut",
        "QueryAccessibleDataResponseIn": "_healthcare_186_QueryAccessibleDataResponseIn",
        "QueryAccessibleDataResponseOut": "_healthcare_187_QueryAccessibleDataResponseOut",
        "BindingIn": "_healthcare_188_BindingIn",
        "BindingOut": "_healthcare_189_BindingOut",
        "GoogleCloudHealthcareV1DicomGcsDestinationIn": "_healthcare_190_GoogleCloudHealthcareV1DicomGcsDestinationIn",
        "GoogleCloudHealthcareV1DicomGcsDestinationOut": "_healthcare_191_GoogleCloudHealthcareV1DicomGcsDestinationOut",
        "PolicyIn": "_healthcare_192_PolicyIn",
        "PolicyOut": "_healthcare_193_PolicyOut",
        "ImportResourcesResponseIn": "_healthcare_194_ImportResourcesResponseIn",
        "ImportResourcesResponseOut": "_healthcare_195_ImportResourcesResponseOut",
        "Hl7SchemaConfigIn": "_healthcare_196_Hl7SchemaConfigIn",
        "Hl7SchemaConfigOut": "_healthcare_197_Hl7SchemaConfigOut",
        "DeidentifyDatasetRequestIn": "_healthcare_198_DeidentifyDatasetRequestIn",
        "DeidentifyDatasetRequestOut": "_healthcare_199_DeidentifyDatasetRequestOut",
        "ArchiveUserDataMappingRequestIn": "_healthcare_200_ArchiveUserDataMappingRequestIn",
        "ArchiveUserDataMappingRequestOut": "_healthcare_201_ArchiveUserDataMappingRequestOut",
        "ImportMessagesResponseIn": "_healthcare_202_ImportMessagesResponseIn",
        "ImportMessagesResponseOut": "_healthcare_203_ImportMessagesResponseOut",
        "Hl7V2StoreIn": "_healthcare_204_Hl7V2StoreIn",
        "Hl7V2StoreOut": "_healthcare_205_Hl7V2StoreOut",
        "GoogleCloudHealthcareV1ConsentPolicyIn": "_healthcare_206_GoogleCloudHealthcareV1ConsentPolicyIn",
        "GoogleCloudHealthcareV1ConsentPolicyOut": "_healthcare_207_GoogleCloudHealthcareV1ConsentPolicyOut",
        "CheckDataAccessRequestIn": "_healthcare_208_CheckDataAccessRequestIn",
        "CheckDataAccessRequestOut": "_healthcare_209_CheckDataAccessRequestOut",
        "ImportDicomDataRequestIn": "_healthcare_210_ImportDicomDataRequestIn",
        "ImportDicomDataRequestOut": "_healthcare_211_ImportDicomDataRequestOut",
        "StatusIn": "_healthcare_212_StatusIn",
        "StatusOut": "_healthcare_213_StatusOut",
        "ConsentStoreIn": "_healthcare_214_ConsentStoreIn",
        "ConsentStoreOut": "_healthcare_215_ConsentStoreOut",
        "ConsentIn": "_healthcare_216_ConsentIn",
        "ConsentOut": "_healthcare_217_ConsentOut",
        "MessageIn": "_healthcare_218_MessageIn",
        "MessageOut": "_healthcare_219_MessageOut",
        "RedactConfigIn": "_healthcare_220_RedactConfigIn",
        "RedactConfigOut": "_healthcare_221_RedactConfigOut",
        "AuditLogConfigIn": "_healthcare_222_AuditLogConfigIn",
        "AuditLogConfigOut": "_healthcare_223_AuditLogConfigOut",
        "StreamConfigIn": "_healthcare_224_StreamConfigIn",
        "StreamConfigOut": "_healthcare_225_StreamConfigOut",
        "ExportDicomDataRequestIn": "_healthcare_226_ExportDicomDataRequestIn",
        "ExportDicomDataRequestOut": "_healthcare_227_ExportDicomDataRequestOut",
        "CryptoHashConfigIn": "_healthcare_228_CryptoHashConfigIn",
        "CryptoHashConfigOut": "_healthcare_229_CryptoHashConfigOut",
        "TypeIn": "_healthcare_230_TypeIn",
        "TypeOut": "_healthcare_231_TypeOut",
        "AnalyzeEntitiesResponseIn": "_healthcare_232_AnalyzeEntitiesResponseIn",
        "AnalyzeEntitiesResponseOut": "_healthcare_233_AnalyzeEntitiesResponseOut",
        "ExportResourcesRequestIn": "_healthcare_234_ExportResourcesRequestIn",
        "ExportResourcesRequestOut": "_healthcare_235_ExportResourcesRequestOut",
        "SignatureIn": "_healthcare_236_SignatureIn",
        "SignatureOut": "_healthcare_237_SignatureOut",
        "ListUserDataMappingsResponseIn": "_healthcare_238_ListUserDataMappingsResponseIn",
        "ListUserDataMappingsResponseOut": "_healthcare_239_ListUserDataMappingsResponseOut",
        "ListOperationsResponseIn": "_healthcare_240_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_healthcare_241_ListOperationsResponseOut",
        "KmsWrappedCryptoKeyIn": "_healthcare_242_KmsWrappedCryptoKeyIn",
        "KmsWrappedCryptoKeyOut": "_healthcare_243_KmsWrappedCryptoKeyOut",
        "UserDataMappingIn": "_healthcare_244_UserDataMappingIn",
        "UserDataMappingOut": "_healthcare_245_UserDataMappingOut",
        "DatasetIn": "_healthcare_246_DatasetIn",
        "DatasetOut": "_healthcare_247_DatasetOut",
        "GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryIn": "_healthcare_248_GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryIn",
        "GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryOut": "_healthcare_249_GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryOut",
        "TestIamPermissionsResponseIn": "_healthcare_250_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_healthcare_251_TestIamPermissionsResponseOut",
        "FieldMetadataIn": "_healthcare_252_FieldMetadataIn",
        "FieldMetadataOut": "_healthcare_253_FieldMetadataOut",
        "ExportMessagesResponseIn": "_healthcare_254_ExportMessagesResponseIn",
        "ExportMessagesResponseOut": "_healthcare_255_ExportMessagesResponseOut",
        "EvaluateUserConsentsRequestIn": "_healthcare_256_EvaluateUserConsentsRequestIn",
        "EvaluateUserConsentsRequestOut": "_healthcare_257_EvaluateUserConsentsRequestOut",
        "GoogleCloudHealthcareV1FhirGcsSourceIn": "_healthcare_258_GoogleCloudHealthcareV1FhirGcsSourceIn",
        "GoogleCloudHealthcareV1FhirGcsSourceOut": "_healthcare_259_GoogleCloudHealthcareV1FhirGcsSourceOut",
        "ConsentEvaluationIn": "_healthcare_260_ConsentEvaluationIn",
        "ConsentEvaluationOut": "_healthcare_261_ConsentEvaluationOut",
        "TestIamPermissionsRequestIn": "_healthcare_262_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_healthcare_263_TestIamPermissionsRequestOut",
        "GoogleCloudHealthcareV1DicomGcsSourceIn": "_healthcare_264_GoogleCloudHealthcareV1DicomGcsSourceIn",
        "GoogleCloudHealthcareV1DicomGcsSourceOut": "_healthcare_265_GoogleCloudHealthcareV1DicomGcsSourceOut",
        "ImageConfigIn": "_healthcare_266_ImageConfigIn",
        "ImageConfigOut": "_healthcare_267_ImageConfigOut",
        "ListHl7V2StoresResponseIn": "_healthcare_268_ListHl7V2StoresResponseIn",
        "ListHl7V2StoresResponseOut": "_healthcare_269_ListHl7V2StoresResponseOut",
        "SearchResourcesRequestIn": "_healthcare_270_SearchResourcesRequestIn",
        "SearchResourcesRequestOut": "_healthcare_271_SearchResourcesRequestOut",
        "LinkedEntityIn": "_healthcare_272_LinkedEntityIn",
        "LinkedEntityOut": "_healthcare_273_LinkedEntityOut",
        "ListMessagesResponseIn": "_healthcare_274_ListMessagesResponseIn",
        "ListMessagesResponseOut": "_healthcare_275_ListMessagesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["DeidentifyDicomStoreRequestIn"] = t.struct(
        {
            "gcsConfigUri": t.string().optional(),
            "destinationStore": t.string().optional(),
            "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
            "filterConfig": t.proxy(renames["DicomFilterConfigIn"]).optional(),
        }
    ).named(renames["DeidentifyDicomStoreRequestIn"])
    types["DeidentifyDicomStoreRequestOut"] = t.struct(
        {
            "gcsConfigUri": t.string().optional(),
            "destinationStore": t.string().optional(),
            "config": t.proxy(renames["DeidentifyConfigOut"]).optional(),
            "filterConfig": t.proxy(renames["DicomFilterConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeidentifyDicomStoreRequestOut"])
    types["CreateMessageRequestIn"] = t.struct(
        {"message": t.proxy(renames["MessageIn"]).optional()}
    ).named(renames["CreateMessageRequestIn"])
    types["CreateMessageRequestOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateMessageRequestOut"])
    types["FhirStoreIn"] = t.struct(
        {
            "notificationConfigs": t.array(
                t.proxy(renames["FhirNotificationConfigIn"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "defaultSearchHandlingStrict": t.boolean().optional(),
            "version": t.string().optional(),
            "disableResourceVersioning": t.boolean().optional(),
            "validationConfig": t.proxy(renames["ValidationConfigIn"]).optional(),
            "complexDataTypeReferenceParsing": t.string().optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigIn"]).optional(),
            "name": t.string().optional(),
            "enableUpdateCreate": t.boolean().optional(),
            "streamConfigs": t.array(t.proxy(renames["StreamConfigIn"])).optional(),
            "disableReferentialIntegrity": t.boolean().optional(),
        }
    ).named(renames["FhirStoreIn"])
    types["FhirStoreOut"] = t.struct(
        {
            "notificationConfigs": t.array(
                t.proxy(renames["FhirNotificationConfigOut"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "defaultSearchHandlingStrict": t.boolean().optional(),
            "version": t.string().optional(),
            "disableResourceVersioning": t.boolean().optional(),
            "validationConfig": t.proxy(renames["ValidationConfigOut"]).optional(),
            "complexDataTypeReferenceParsing": t.string().optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigOut"]).optional(),
            "name": t.string().optional(),
            "enableUpdateCreate": t.boolean().optional(),
            "streamConfigs": t.array(t.proxy(renames["StreamConfigOut"])).optional(),
            "disableReferentialIntegrity": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FhirStoreOut"])
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
    types["ReplaceWithInfoTypeConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReplaceWithInfoTypeConfigIn"]
    )
    types["ReplaceWithInfoTypeConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReplaceWithInfoTypeConfigOut"])
    types["ResultIn"] = t.struct(
        {
            "consented": t.boolean().optional(),
            "consentDetails": t.struct({"_": t.string().optional()}).optional(),
            "dataId": t.string().optional(),
        }
    ).named(renames["ResultIn"])
    types["ResultOut"] = t.struct(
        {
            "consented": t.boolean().optional(),
            "consentDetails": t.struct({"_": t.string().optional()}).optional(),
            "dataId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultOut"])
    types["ListAttributeDefinitionsResponseIn"] = t.struct(
        {
            "attributeDefinitions": t.array(
                t.proxy(renames["AttributeDefinitionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAttributeDefinitionsResponseIn"])
    types["ListAttributeDefinitionsResponseOut"] = t.struct(
        {
            "attributeDefinitions": t.array(
                t.proxy(renames["AttributeDefinitionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAttributeDefinitionsResponseOut"])
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
    types["RejectConsentRequestIn"] = t.struct(
        {"consentArtifact": t.string().optional()}
    ).named(renames["RejectConsentRequestIn"])
    types["RejectConsentRequestOut"] = t.struct(
        {
            "consentArtifact": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RejectConsentRequestOut"])
    types["AttributeDefinitionIn"] = t.struct(
        {
            "allowedValues": t.array(t.string()),
            "dataMappingDefaultValue": t.string().optional(),
            "category": t.string(),
            "description": t.string().optional(),
            "consentDefaultValues": t.array(t.string()).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AttributeDefinitionIn"])
    types["AttributeDefinitionOut"] = t.struct(
        {
            "allowedValues": t.array(t.string()),
            "dataMappingDefaultValue": t.string().optional(),
            "category": t.string(),
            "description": t.string().optional(),
            "consentDefaultValues": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeDefinitionOut"])
    types["DicomFilterConfigIn"] = t.struct(
        {"resourcePathsGcsUri": t.string().optional()}
    ).named(renames["DicomFilterConfigIn"])
    types["DicomFilterConfigOut"] = t.struct(
        {
            "resourcePathsGcsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DicomFilterConfigOut"])
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
    types["FhirFilterIn"] = t.struct(
        {"resources": t.proxy(renames["ResourcesIn"]).optional()}
    ).named(renames["FhirFilterIn"])
    types["FhirFilterOut"] = t.struct(
        {
            "resources": t.proxy(renames["ResourcesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FhirFilterOut"])
    types["GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryIn"])
    types["GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryOut"])
    types["SchemaPackageIn"] = t.struct(
        {
            "unexpectedSegmentHandling": t.string().optional(),
            "types": t.array(t.proxy(renames["Hl7TypesConfigIn"])).optional(),
            "schemas": t.array(t.proxy(renames["Hl7SchemaConfigIn"])).optional(),
            "schematizedParsingType": t.string().optional(),
            "ignoreMinOccurs": t.boolean().optional(),
        }
    ).named(renames["SchemaPackageIn"])
    types["SchemaPackageOut"] = t.struct(
        {
            "unexpectedSegmentHandling": t.string().optional(),
            "types": t.array(t.proxy(renames["Hl7TypesConfigOut"])).optional(),
            "schemas": t.array(t.proxy(renames["Hl7SchemaConfigOut"])).optional(),
            "schematizedParsingType": t.string().optional(),
            "ignoreMinOccurs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaPackageOut"])
    types["DeidentifyConfigIn"] = t.struct(
        {
            "useRegionalDataProcessing": t.boolean().optional(),
            "fhir": t.proxy(renames["FhirConfigIn"]).optional(),
            "image": t.proxy(renames["ImageConfigIn"]).optional(),
            "text": t.proxy(renames["TextConfigIn"]).optional(),
            "dicom": t.proxy(renames["DicomConfigIn"]).optional(),
        }
    ).named(renames["DeidentifyConfigIn"])
    types["DeidentifyConfigOut"] = t.struct(
        {
            "useRegionalDataProcessing": t.boolean().optional(),
            "fhir": t.proxy(renames["FhirConfigOut"]).optional(),
            "image": t.proxy(renames["ImageConfigOut"]).optional(),
            "text": t.proxy(renames["TextConfigOut"]).optional(),
            "dicom": t.proxy(renames["DicomConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeidentifyConfigOut"])
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
    types["ResourcesIn"] = t.struct(
        {"resources": t.array(t.string()).optional()}
    ).named(renames["ResourcesIn"])
    types["ResourcesOut"] = t.struct(
        {
            "resources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourcesOut"])
    types["RevokeConsentRequestIn"] = t.struct(
        {"consentArtifact": t.string().optional()}
    ).named(renames["RevokeConsentRequestIn"])
    types["RevokeConsentRequestOut"] = t.struct(
        {
            "consentArtifact": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevokeConsentRequestOut"])
    types["CharacterMaskConfigIn"] = t.struct(
        {"maskingCharacter": t.string().optional()}
    ).named(renames["CharacterMaskConfigIn"])
    types["CharacterMaskConfigOut"] = t.struct(
        {
            "maskingCharacter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CharacterMaskConfigOut"])
    types["GoogleCloudHealthcareV1FhirGcsDestinationIn"] = t.struct(
        {"uriPrefix": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"])
    types["GoogleCloudHealthcareV1FhirGcsDestinationOut"] = t.struct(
        {
            "uriPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1FhirGcsDestinationOut"])
    types["SchemaConfigIn"] = t.struct(
        {
            "schemaType": t.string().optional(),
            "lastUpdatedPartitionConfig": t.proxy(
                renames["TimePartitioningIn"]
            ).optional(),
            "recursiveStructureDepth": t.string().optional(),
        }
    ).named(renames["SchemaConfigIn"])
    types["SchemaConfigOut"] = t.struct(
        {
            "schemaType": t.string().optional(),
            "lastUpdatedPartitionConfig": t.proxy(
                renames["TimePartitioningOut"]
            ).optional(),
            "recursiveStructureDepth": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaConfigOut"])
    types["ImportMessagesRequestIn"] = t.struct(
        {"gcsSource": t.proxy(renames["GcsSourceIn"]).optional()}
    ).named(renames["ImportMessagesRequestIn"])
    types["ImportMessagesRequestOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportMessagesRequestOut"])
    types["GoogleCloudHealthcareV1ConsentGcsDestinationIn"] = t.struct(
        {"uriPrefix": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1ConsentGcsDestinationIn"])
    types["GoogleCloudHealthcareV1ConsentGcsDestinationOut"] = t.struct(
        {
            "uriPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1ConsentGcsDestinationOut"])
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
    types["ImportDicomDataResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ImportDicomDataResponseIn"]
    )
    types["ImportDicomDataResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportDicomDataResponseOut"])
    types["ParsedDataIn"] = t.struct(
        {"segments": t.array(t.proxy(renames["SegmentIn"]))}
    ).named(renames["ParsedDataIn"])
    types["ParsedDataOut"] = t.struct(
        {
            "segments": t.array(t.proxy(renames["SegmentOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParsedDataOut"])
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
    types["OperationMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "apiMethodName": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "counter": t.proxy(renames["ProgressCounterIn"]),
            "logsUrl": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "apiMethodName": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "counter": t.proxy(renames["ProgressCounterOut"]),
            "logsUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ExportDicomDataResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ExportDicomDataResponseIn"]
    )
    types["ExportDicomDataResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExportDicomDataResponseOut"])
    types["GcsSourceIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["GcsSourceIn"]
    )
    types["GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsSourceOut"])
    types["QueryAccessibleDataRequestIn"] = t.struct(
        {
            "requestAttributes": t.struct({"_": t.string().optional()}).optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudHealthcareV1ConsentGcsDestinationIn"]
            ).optional(),
            "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["QueryAccessibleDataRequestIn"])
    types["QueryAccessibleDataRequestOut"] = t.struct(
        {
            "requestAttributes": t.struct({"_": t.string().optional()}).optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudHealthcareV1ConsentGcsDestinationOut"]
            ).optional(),
            "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryAccessibleDataRequestOut"])
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
    types["FhirStoreMetricsIn"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["FhirStoreMetricIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["FhirStoreMetricsIn"])
    types["FhirStoreMetricsOut"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["FhirStoreMetricOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FhirStoreMetricsOut"])
    types["SchematizedDataIn"] = t.struct(
        {"error": t.string().optional(), "data": t.string().optional()}
    ).named(renames["SchematizedDataIn"])
    types["SchematizedDataOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "data": t.string().optional(),
        }
    ).named(renames["SchematizedDataOut"])
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
    types["ConsentArtifactIn"] = t.struct(
        {
            "userSignature": t.proxy(renames["SignatureIn"]).optional(),
            "consentContentVersion": t.string().optional(),
            "consentContentScreenshots": t.array(
                t.proxy(renames["ImageIn"])
            ).optional(),
            "name": t.string().optional(),
            "guardianSignature": t.proxy(renames["SignatureIn"]).optional(),
            "userId": t.string(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "witnessSignature": t.proxy(renames["SignatureIn"]).optional(),
        }
    ).named(renames["ConsentArtifactIn"])
    types["ConsentArtifactOut"] = t.struct(
        {
            "userSignature": t.proxy(renames["SignatureOut"]).optional(),
            "consentContentVersion": t.string().optional(),
            "consentContentScreenshots": t.array(
                t.proxy(renames["ImageOut"])
            ).optional(),
            "name": t.string().optional(),
            "guardianSignature": t.proxy(renames["SignatureOut"]).optional(),
            "userId": t.string(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "witnessSignature": t.proxy(renames["SignatureOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentArtifactOut"])
    types["FieldIn"] = t.struct(
        {
            "table": t.string().optional(),
            "minOccurs": t.integer().optional(),
            "type": t.string().optional(),
            "maxOccurs": t.integer().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "table": t.string().optional(),
            "minOccurs": t.integer().optional(),
            "type": t.string().optional(),
            "maxOccurs": t.integer().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["InfoTypeTransformationIn"] = t.struct(
        {
            "replaceWithInfoTypeConfig": t.proxy(
                renames["ReplaceWithInfoTypeConfigIn"]
            ).optional(),
            "infoTypes": t.array(t.string()).optional(),
            "redactConfig": t.proxy(renames["RedactConfigIn"]).optional(),
            "characterMaskConfig": t.proxy(renames["CharacterMaskConfigIn"]).optional(),
            "dateShiftConfig": t.proxy(renames["DateShiftConfigIn"]).optional(),
            "cryptoHashConfig": t.proxy(renames["CryptoHashConfigIn"]).optional(),
        }
    ).named(renames["InfoTypeTransformationIn"])
    types["InfoTypeTransformationOut"] = t.struct(
        {
            "replaceWithInfoTypeConfig": t.proxy(
                renames["ReplaceWithInfoTypeConfigOut"]
            ).optional(),
            "infoTypes": t.array(t.string()).optional(),
            "redactConfig": t.proxy(renames["RedactConfigOut"]).optional(),
            "characterMaskConfig": t.proxy(
                renames["CharacterMaskConfigOut"]
            ).optional(),
            "dateShiftConfig": t.proxy(renames["DateShiftConfigOut"]).optional(),
            "cryptoHashConfig": t.proxy(renames["CryptoHashConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InfoTypeTransformationOut"])
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
    types["ListFhirStoresResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "fhirStores": t.array(t.proxy(renames["FhirStoreIn"])).optional(),
        }
    ).named(renames["ListFhirStoresResponseIn"])
    types["ListFhirStoresResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "fhirStores": t.array(t.proxy(renames["FhirStoreOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFhirStoresResponseOut"])
    types["NotificationConfigIn"] = t.struct(
        {"pubsubTopic": t.string().optional()}
    ).named(renames["NotificationConfigIn"])
    types["NotificationConfigOut"] = t.struct(
        {
            "pubsubTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationConfigOut"])
    types["ExportMessagesRequestIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional(),
        }
    ).named(renames["ExportMessagesRequestIn"])
    types["ExportMessagesRequestOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportMessagesRequestOut"])
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
    types["EntityIn"] = t.struct(
        {
            "preferredTerm": t.string().optional(),
            "vocabularyCodes": t.array(t.string()).optional(),
            "entityId": t.string().optional(),
        }
    ).named(renames["EntityIn"])
    types["EntityOut"] = t.struct(
        {
            "preferredTerm": t.string().optional(),
            "vocabularyCodes": t.array(t.string()).optional(),
            "entityId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityOut"])
    types["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"] = t.struct(
        {
            "writeDisposition": t.string().optional(),
            "datasetUri": t.string().optional(),
            "schemaConfig": t.proxy(renames["SchemaConfigIn"]).optional(),
            "force": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"])
    types["GoogleCloudHealthcareV1FhirBigQueryDestinationOut"] = t.struct(
        {
            "writeDisposition": t.string().optional(),
            "datasetUri": t.string().optional(),
            "schemaConfig": t.proxy(renames["SchemaConfigOut"]).optional(),
            "force": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1FhirBigQueryDestinationOut"])
    types["SegmentIn"] = t.struct(
        {
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "setId": t.string().optional(),
            "segmentId": t.string().optional(),
        }
    ).named(renames["SegmentIn"])
    types["SegmentOut"] = t.struct(
        {
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "setId": t.string().optional(),
            "segmentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentOut"])
    types["DeidentifyFhirStoreRequestIn"] = t.struct(
        {
            "destinationStore": t.string().optional(),
            "gcsConfigUri": t.string().optional(),
            "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
            "resourceFilter": t.proxy(renames["FhirFilterIn"]).optional(),
            "skipModifiedResources": t.boolean().optional(),
        }
    ).named(renames["DeidentifyFhirStoreRequestIn"])
    types["DeidentifyFhirStoreRequestOut"] = t.struct(
        {
            "destinationStore": t.string().optional(),
            "gcsConfigUri": t.string().optional(),
            "config": t.proxy(renames["DeidentifyConfigOut"]).optional(),
            "resourceFilter": t.proxy(renames["FhirFilterOut"]).optional(),
            "skipModifiedResources": t.boolean().optional(),
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
    types["ValidationConfigIn"] = t.struct(
        {
            "disableProfileValidation": t.boolean().optional(),
            "enabledImplementationGuides": t.array(t.string()).optional(),
            "disableFhirpathValidation": t.boolean().optional(),
            "disableRequiredFieldValidation": t.boolean().optional(),
            "disableReferenceTypeValidation": t.boolean().optional(),
        }
    ).named(renames["ValidationConfigIn"])
    types["ValidationConfigOut"] = t.struct(
        {
            "disableProfileValidation": t.boolean().optional(),
            "enabledImplementationGuides": t.array(t.string()).optional(),
            "disableFhirpathValidation": t.boolean().optional(),
            "disableRequiredFieldValidation": t.boolean().optional(),
            "disableReferenceTypeValidation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationConfigOut"])
    types["EntityMentionIn"] = t.struct(
        {
            "linkedEntities": t.array(t.proxy(renames["LinkedEntityIn"])).optional(),
            "temporalAssessment": t.proxy(renames["FeatureIn"]).optional(),
            "mentionId": t.string().optional(),
            "type": t.string().optional(),
            "certaintyAssessment": t.proxy(renames["FeatureIn"]).optional(),
            "subject": t.proxy(renames["FeatureIn"]).optional(),
            "text": t.proxy(renames["TextSpanIn"]).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["EntityMentionIn"])
    types["EntityMentionOut"] = t.struct(
        {
            "linkedEntities": t.array(t.proxy(renames["LinkedEntityOut"])).optional(),
            "temporalAssessment": t.proxy(renames["FeatureOut"]).optional(),
            "mentionId": t.string().optional(),
            "type": t.string().optional(),
            "certaintyAssessment": t.proxy(renames["FeatureOut"]).optional(),
            "subject": t.proxy(renames["FeatureOut"]).optional(),
            "text": t.proxy(renames["TextSpanOut"]).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityMentionOut"])
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
    types["ParserConfigIn"] = t.struct(
        {
            "version": t.string().optional(),
            "segmentTerminator": t.string().optional(),
            "allowNullHeader": t.boolean().optional(),
            "schema": t.proxy(renames["SchemaPackageIn"]).optional(),
        }
    ).named(renames["ParserConfigIn"])
    types["ParserConfigOut"] = t.struct(
        {
            "version": t.string().optional(),
            "segmentTerminator": t.string().optional(),
            "allowNullHeader": t.boolean().optional(),
            "schema": t.proxy(renames["SchemaPackageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParserConfigOut"])
    types["SchemaGroupIn"] = t.struct(
        {
            "minOccurs": t.integer().optional(),
            "name": t.string().optional(),
            "members": t.array(t.proxy(renames["GroupOrSegmentIn"])).optional(),
            "maxOccurs": t.integer().optional(),
            "choice": t.boolean().optional(),
        }
    ).named(renames["SchemaGroupIn"])
    types["SchemaGroupOut"] = t.struct(
        {
            "minOccurs": t.integer().optional(),
            "name": t.string().optional(),
            "members": t.array(t.proxy(renames["GroupOrSegmentOut"])).optional(),
            "maxOccurs": t.integer().optional(),
            "choice": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaGroupOut"])
    types["CheckDataAccessResponseIn"] = t.struct(
        {
            "consented": t.boolean().optional(),
            "consentDetails": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CheckDataAccessResponseIn"])
    types["CheckDataAccessResponseOut"] = t.struct(
        {
            "consented": t.boolean().optional(),
            "consentDetails": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckDataAccessResponseOut"])
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
    types["DeidentifiedStoreDestinationIn"] = t.struct(
        {
            "store": t.string().optional(),
            "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
        }
    ).named(renames["DeidentifiedStoreDestinationIn"])
    types["DeidentifiedStoreDestinationOut"] = t.struct(
        {
            "store": t.string().optional(),
            "config": t.proxy(renames["DeidentifyConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeidentifiedStoreDestinationOut"])
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
    types["ConsentListIn"] = t.struct(
        {"consents": t.array(t.string()).optional()}
    ).named(renames["ConsentListIn"])
    types["ConsentListOut"] = t.struct(
        {
            "consents": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentListOut"])
    types["TextSpanIn"] = t.struct(
        {"beginOffset": t.integer().optional(), "content": t.string().optional()}
    ).named(renames["TextSpanIn"])
    types["TextSpanOut"] = t.struct(
        {
            "beginOffset": t.integer().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextSpanOut"])
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
    types["ImageIn"] = t.struct(
        {"gcsUri": t.string().optional(), "rawBytes": t.string().optional()}
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "gcsUri": t.string().optional(),
            "rawBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["IngestMessageRequestIn"] = t.struct(
        {"message": t.proxy(renames["MessageIn"]).optional()}
    ).named(renames["IngestMessageRequestIn"])
    types["IngestMessageRequestOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IngestMessageRequestOut"])
    types["TagFilterListIn"] = t.struct({"tags": t.array(t.string()).optional()}).named(
        renames["TagFilterListIn"]
    )
    types["TagFilterListOut"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagFilterListOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["ArchiveUserDataMappingResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ArchiveUserDataMappingResponseIn"])
    types["ArchiveUserDataMappingResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ArchiveUserDataMappingResponseOut"])
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
    types["Hl7V2NotificationConfigIn"] = t.struct(
        {"pubsubTopic": t.string().optional(), "filter": t.string().optional()}
    ).named(renames["Hl7V2NotificationConfigIn"])
    types["Hl7V2NotificationConfigOut"] = t.struct(
        {
            "pubsubTopic": t.string().optional(),
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Hl7V2NotificationConfigOut"])
    types["GroupOrSegmentIn"] = t.struct(
        {
            "segment": t.proxy(renames["SchemaSegmentIn"]),
            "group": t.proxy(renames["SchemaGroupIn"]),
        }
    ).named(renames["GroupOrSegmentIn"])
    types["GroupOrSegmentOut"] = t.struct(
        {
            "segment": t.proxy(renames["SchemaSegmentOut"]),
            "group": t.proxy(renames["SchemaGroupOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOrSegmentOut"])
    types["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"] = t.struct(
        {
            "force": t.boolean().optional(),
            "writeDisposition": t.string().optional(),
            "tableUri": t.string().optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1DicomBigQueryDestinationIn"])
    types["GoogleCloudHealthcareV1DicomBigQueryDestinationOut"] = t.struct(
        {
            "force": t.boolean().optional(),
            "writeDisposition": t.string().optional(),
            "tableUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1DicomBigQueryDestinationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["HttpBodyIn"] = t.struct(
        {
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "contentType": t.string().optional(),
            "data": t.string().optional(),
        }
    ).named(renames["HttpBodyIn"])
    types["HttpBodyOut"] = t.struct(
        {
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "contentType": t.string().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpBodyOut"])
    types["AnalyzeEntitiesRequestIn"] = t.struct(
        {
            "licensedVocabularies": t.array(t.string()).optional(),
            "documentContent": t.string().optional(),
        }
    ).named(renames["AnalyzeEntitiesRequestIn"])
    types["AnalyzeEntitiesRequestOut"] = t.struct(
        {
            "licensedVocabularies": t.array(t.string()).optional(),
            "documentContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeEntitiesRequestOut"])
    types["EntityMentionRelationshipIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "confidence": t.number().optional(),
            "subjectId": t.string().optional(),
        }
    ).named(renames["EntityMentionRelationshipIn"])
    types["EntityMentionRelationshipOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "confidence": t.number().optional(),
            "subjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityMentionRelationshipOut"])
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
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["DicomConfigIn"] = t.struct(
        {
            "keepList": t.proxy(renames["TagFilterListIn"]).optional(),
            "filterProfile": t.string().optional(),
            "removeList": t.proxy(renames["TagFilterListIn"]).optional(),
            "skipIdRedaction": t.boolean().optional(),
        }
    ).named(renames["DicomConfigIn"])
    types["DicomConfigOut"] = t.struct(
        {
            "keepList": t.proxy(renames["TagFilterListOut"]).optional(),
            "filterProfile": t.string().optional(),
            "removeList": t.proxy(renames["TagFilterListOut"]).optional(),
            "skipIdRedaction": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DicomConfigOut"])
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
    types["ExportResourcesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ExportResourcesResponseIn"]
    )
    types["ExportResourcesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExportResourcesResponseOut"])
    types["DeidentifySummaryIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeidentifySummaryIn"]
    )
    types["DeidentifySummaryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeidentifySummaryOut"])
    types["IngestMessageResponseIn"] = t.struct(
        {
            "hl7Ack": t.string().optional(),
            "message": t.proxy(renames["MessageIn"]).optional(),
        }
    ).named(renames["IngestMessageResponseIn"])
    types["IngestMessageResponseOut"] = t.struct(
        {
            "hl7Ack": t.string().optional(),
            "message": t.proxy(renames["MessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IngestMessageResponseOut"])
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
    types["QueryAccessibleDataResponseIn"] = t.struct(
        {"gcsUris": t.array(t.string()).optional()}
    ).named(renames["QueryAccessibleDataResponseIn"])
    types["QueryAccessibleDataResponseOut"] = t.struct(
        {
            "gcsUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryAccessibleDataResponseOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ImportResourcesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ImportResourcesResponseIn"]
    )
    types["ImportResourcesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportResourcesResponseOut"])
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
    types["DeidentifyDatasetRequestIn"] = t.struct(
        {
            "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
            "destinationDataset": t.string().optional(),
            "gcsConfigUri": t.string().optional(),
        }
    ).named(renames["DeidentifyDatasetRequestIn"])
    types["DeidentifyDatasetRequestOut"] = t.struct(
        {
            "config": t.proxy(renames["DeidentifyConfigOut"]).optional(),
            "destinationDataset": t.string().optional(),
            "gcsConfigUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeidentifyDatasetRequestOut"])
    types["ArchiveUserDataMappingRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ArchiveUserDataMappingRequestIn"])
    types["ArchiveUserDataMappingRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ArchiveUserDataMappingRequestOut"])
    types["ImportMessagesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ImportMessagesResponseIn"]
    )
    types["ImportMessagesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportMessagesResponseOut"])
    types["Hl7V2StoreIn"] = t.struct(
        {
            "name": t.string().optional(),
            "rejectDuplicateMessage": t.boolean().optional(),
            "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "notificationConfigs": t.array(
                t.proxy(renames["Hl7V2NotificationConfigIn"])
            ).optional(),
        }
    ).named(renames["Hl7V2StoreIn"])
    types["Hl7V2StoreOut"] = t.struct(
        {
            "name": t.string().optional(),
            "rejectDuplicateMessage": t.boolean().optional(),
            "parserConfig": t.proxy(renames["ParserConfigOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "notificationConfigs": t.array(
                t.proxy(renames["Hl7V2NotificationConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Hl7V2StoreOut"])
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
    types["CheckDataAccessRequestIn"] = t.struct(
        {
            "responseView": t.string().optional(),
            "requestAttributes": t.struct({"_": t.string().optional()}).optional(),
            "dataId": t.string(),
            "consentList": t.proxy(renames["ConsentListIn"]).optional(),
        }
    ).named(renames["CheckDataAccessRequestIn"])
    types["CheckDataAccessRequestOut"] = t.struct(
        {
            "responseView": t.string().optional(),
            "requestAttributes": t.struct({"_": t.string().optional()}).optional(),
            "dataId": t.string(),
            "consentList": t.proxy(renames["ConsentListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckDataAccessRequestOut"])
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
    types["ConsentStoreIn"] = t.struct(
        {
            "name": t.string().optional(),
            "defaultConsentTtl": t.string().optional(),
            "enableConsentCreateOnUpdate": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ConsentStoreIn"])
    types["ConsentStoreOut"] = t.struct(
        {
            "name": t.string().optional(),
            "defaultConsentTtl": t.string().optional(),
            "enableConsentCreateOnUpdate": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentStoreOut"])
    types["ConsentIn"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "userId": t.string(),
            "policies": t.array(
                t.proxy(renames["GoogleCloudHealthcareV1ConsentPolicyIn"])
            ).optional(),
            "ttl": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "consentArtifact": t.string(),
            "name": t.string().optional(),
            "state": t.string(),
        }
    ).named(renames["ConsentIn"])
    types["ConsentOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "expireTime": t.string().optional(),
            "userId": t.string(),
            "policies": t.array(
                t.proxy(renames["GoogleCloudHealthcareV1ConsentPolicyOut"])
            ).optional(),
            "revisionCreateTime": t.string().optional(),
            "ttl": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "consentArtifact": t.string(),
            "name": t.string().optional(),
            "state": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentOut"])
    types["MessageIn"] = t.struct(
        {
            "schematizedData": t.proxy(renames["SchematizedDataIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "messageType": t.string().optional(),
            "sendTime": t.string().optional(),
            "name": t.string().optional(),
            "data": t.string().optional(),
            "patientIds": t.array(t.proxy(renames["PatientIdIn"])).optional(),
            "sendFacility": t.string().optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "schematizedData": t.proxy(renames["SchematizedDataOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "messageType": t.string().optional(),
            "sendTime": t.string().optional(),
            "name": t.string().optional(),
            "data": t.string().optional(),
            "parsedData": t.proxy(renames["ParsedDataOut"]).optional(),
            "patientIds": t.array(t.proxy(renames["PatientIdOut"])).optional(),
            "sendFacility": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["RedactConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RedactConfigIn"]
    )
    types["RedactConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RedactConfigOut"])
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
    types["StreamConfigIn"] = t.struct(
        {
            "deidentifiedStoreDestination": t.proxy(
                renames["DeidentifiedStoreDestinationIn"]
            ).optional(),
            "resourceTypes": t.array(t.string()).optional(),
            "bigqueryDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"]
            ).optional(),
        }
    ).named(renames["StreamConfigIn"])
    types["StreamConfigOut"] = t.struct(
        {
            "deidentifiedStoreDestination": t.proxy(
                renames["DeidentifiedStoreDestinationOut"]
            ).optional(),
            "resourceTypes": t.array(t.string()).optional(),
            "bigqueryDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirBigQueryDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamConfigOut"])
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
    types["ExportResourcesRequestIn"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"]
            ).optional(),
            "bigqueryDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"]
            ).optional(),
            "_since": t.string().optional(),
            "_type": t.string().optional(),
        }
    ).named(renames["ExportResourcesRequestIn"])
    types["ExportResourcesRequestOut"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirGcsDestinationOut"]
            ).optional(),
            "bigqueryDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirBigQueryDestinationOut"]
            ).optional(),
            "_since": t.string().optional(),
            "_type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportResourcesRequestOut"])
    types["SignatureIn"] = t.struct(
        {
            "image": t.proxy(renames["ImageIn"]).optional(),
            "userId": t.string(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "signatureTime": t.string().optional(),
        }
    ).named(renames["SignatureIn"])
    types["SignatureOut"] = t.struct(
        {
            "image": t.proxy(renames["ImageOut"]).optional(),
            "userId": t.string(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "signatureTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignatureOut"])
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
    types["KmsWrappedCryptoKeyIn"] = t.struct(
        {"wrappedKey": t.string(), "cryptoKey": t.string()}
    ).named(renames["KmsWrappedCryptoKeyIn"])
    types["KmsWrappedCryptoKeyOut"] = t.struct(
        {
            "wrappedKey": t.string(),
            "cryptoKey": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KmsWrappedCryptoKeyOut"])
    types["UserDataMappingIn"] = t.struct(
        {
            "dataId": t.string(),
            "name": t.string().optional(),
            "resourceAttributes": t.array(t.proxy(renames["AttributeIn"])).optional(),
            "userId": t.string(),
        }
    ).named(renames["UserDataMappingIn"])
    types["UserDataMappingOut"] = t.struct(
        {
            "dataId": t.string(),
            "name": t.string().optional(),
            "archiveTime": t.string().optional(),
            "archived": t.boolean().optional(),
            "resourceAttributes": t.array(t.proxy(renames["AttributeOut"])).optional(),
            "userId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserDataMappingOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["ExportMessagesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ExportMessagesResponseIn"]
    )
    types["ExportMessagesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExportMessagesResponseOut"])
    types["EvaluateUserConsentsRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "userId": t.string(),
            "requestAttributes": t.struct({"_": t.string().optional()}),
            "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
            "consentList": t.proxy(renames["ConsentListIn"]).optional(),
            "responseView": t.string().optional(),
        }
    ).named(renames["EvaluateUserConsentsRequestIn"])
    types["EvaluateUserConsentsRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "userId": t.string(),
            "requestAttributes": t.struct({"_": t.string().optional()}),
            "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
            "consentList": t.proxy(renames["ConsentListOut"]).optional(),
            "responseView": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EvaluateUserConsentsRequestOut"])
    types["GoogleCloudHealthcareV1FhirGcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1FhirGcsSourceIn"])
    types["GoogleCloudHealthcareV1FhirGcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1FhirGcsSourceOut"])
    types["ConsentEvaluationIn"] = t.struct(
        {"evaluationResult": t.string().optional()}
    ).named(renames["ConsentEvaluationIn"])
    types["ConsentEvaluationOut"] = t.struct(
        {
            "evaluationResult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentEvaluationOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["GoogleCloudHealthcareV1DicomGcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1DicomGcsSourceIn"])
    types["GoogleCloudHealthcareV1DicomGcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1DicomGcsSourceOut"])
    types["ImageConfigIn"] = t.struct(
        {"textRedactionMode": t.string().optional()}
    ).named(renames["ImageConfigIn"])
    types["ImageConfigOut"] = t.struct(
        {
            "textRedactionMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageConfigOut"])
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
    types["SearchResourcesRequestIn"] = t.struct(
        {"resourceType": t.string().optional()}
    ).named(renames["SearchResourcesRequestIn"])
    types["SearchResourcesRequestOut"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResourcesRequestOut"])
    types["LinkedEntityIn"] = t.struct({"entityId": t.string().optional()}).named(
        renames["LinkedEntityIn"]
    )
    types["LinkedEntityOut"] = t.struct(
        {
            "entityId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedEntityOut"])
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

    functions = {}
    functions["projectsLocationsGet"] = healthcare.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDelete"] = healthcare.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsGetIamPolicy"] = healthcare.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsList"] = healthcare.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsCreate"] = healthcare.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsGet"] = healthcare.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsPatch"] = healthcare.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDeidentify"] = healthcare.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsTestIamPermissions"] = healthcare.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsSetIamPolicy"] = healthcare.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresDelete"] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresPatch"] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresList"] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresSetIamPolicy"] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresGet"] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresQueryAccessibleData"
    ] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresTestIamPermissions"
    ] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresCreate"] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresCheckDataAccess"] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresEvaluateUserConsents"
    ] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresGetIamPolicy"] = healthcare.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresAttributeDefinitionsList"
    ] = healthcare.post(
        "v1/{parent}/attributeDefinitions",
        t.struct(
            {
                "attributeDefinitionId": t.string(),
                "parent": t.string(),
                "allowedValues": t.array(t.string()),
                "dataMappingDefaultValue": t.string().optional(),
                "category": t.string(),
                "description": t.string().optional(),
                "consentDefaultValues": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttributeDefinitionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresAttributeDefinitionsPatch"
    ] = healthcare.post(
        "v1/{parent}/attributeDefinitions",
        t.struct(
            {
                "attributeDefinitionId": t.string(),
                "parent": t.string(),
                "allowedValues": t.array(t.string()),
                "dataMappingDefaultValue": t.string().optional(),
                "category": t.string(),
                "description": t.string().optional(),
                "consentDefaultValues": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttributeDefinitionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresAttributeDefinitionsDelete"
    ] = healthcare.post(
        "v1/{parent}/attributeDefinitions",
        t.struct(
            {
                "attributeDefinitionId": t.string(),
                "parent": t.string(),
                "allowedValues": t.array(t.string()),
                "dataMappingDefaultValue": t.string().optional(),
                "category": t.string(),
                "description": t.string().optional(),
                "consentDefaultValues": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttributeDefinitionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresAttributeDefinitionsGet"
    ] = healthcare.post(
        "v1/{parent}/attributeDefinitions",
        t.struct(
            {
                "attributeDefinitionId": t.string(),
                "parent": t.string(),
                "allowedValues": t.array(t.string()),
                "dataMappingDefaultValue": t.string().optional(),
                "category": t.string(),
                "description": t.string().optional(),
                "consentDefaultValues": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttributeDefinitionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresAttributeDefinitionsCreate"
    ] = healthcare.post(
        "v1/{parent}/attributeDefinitions",
        t.struct(
            {
                "attributeDefinitionId": t.string(),
                "parent": t.string(),
                "allowedValues": t.array(t.string()),
                "dataMappingDefaultValue": t.string().optional(),
                "category": t.string(),
                "description": t.string().optional(),
                "consentDefaultValues": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttributeDefinitionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentArtifactsList"
    ] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConsentArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentArtifactsDelete"
    ] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConsentArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentArtifactsCreate"
    ] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConsentArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentArtifactsGet"
    ] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConsentArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsDelete"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsListRevisions"
    ] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsList"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsDeleteRevision"
    ] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsPatch"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsReject"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsCreate"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsRevoke"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsActivate"
    ] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsGet"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsDelete"
    ] = healthcare.get(
        "v1/{parent}/userDataMappings",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUserDataMappingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsArchive"
    ] = healthcare.get(
        "v1/{parent}/userDataMappings",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUserDataMappingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsPatch"
    ] = healthcare.get(
        "v1/{parent}/userDataMappings",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUserDataMappingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsGet"
    ] = healthcare.get(
        "v1/{parent}/userDataMappings",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUserDataMappingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsCreate"
    ] = healthcare.get(
        "v1/{parent}/userDataMappings",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUserDataMappingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsList"
    ] = healthcare.get(
        "v1/{parent}/userDataMappings",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUserDataMappingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresCreate"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["FhirNotificationConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "defaultSearchHandlingStrict": t.boolean().optional(),
                "version": t.string().optional(),
                "disableResourceVersioning": t.boolean().optional(),
                "validationConfig": t.proxy(renames["ValidationConfigIn"]).optional(),
                "complexDataTypeReferenceParsing": t.string().optional(),
                "notificationConfig": t.proxy(
                    renames["NotificationConfigIn"]
                ).optional(),
                "enableUpdateCreate": t.boolean().optional(),
                "streamConfigs": t.array(t.proxy(renames["StreamConfigIn"])).optional(),
                "disableReferentialIntegrity": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresList"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["FhirNotificationConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "defaultSearchHandlingStrict": t.boolean().optional(),
                "version": t.string().optional(),
                "disableResourceVersioning": t.boolean().optional(),
                "validationConfig": t.proxy(renames["ValidationConfigIn"]).optional(),
                "complexDataTypeReferenceParsing": t.string().optional(),
                "notificationConfig": t.proxy(
                    renames["NotificationConfigIn"]
                ).optional(),
                "enableUpdateCreate": t.boolean().optional(),
                "streamConfigs": t.array(t.proxy(renames["StreamConfigIn"])).optional(),
                "disableReferentialIntegrity": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresExport"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["FhirNotificationConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "defaultSearchHandlingStrict": t.boolean().optional(),
                "version": t.string().optional(),
                "disableResourceVersioning": t.boolean().optional(),
                "validationConfig": t.proxy(renames["ValidationConfigIn"]).optional(),
                "complexDataTypeReferenceParsing": t.string().optional(),
                "notificationConfig": t.proxy(
                    renames["NotificationConfigIn"]
                ).optional(),
                "enableUpdateCreate": t.boolean().optional(),
                "streamConfigs": t.array(t.proxy(renames["StreamConfigIn"])).optional(),
                "disableReferentialIntegrity": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresDeidentify"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["FhirNotificationConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "defaultSearchHandlingStrict": t.boolean().optional(),
                "version": t.string().optional(),
                "disableResourceVersioning": t.boolean().optional(),
                "validationConfig": t.proxy(renames["ValidationConfigIn"]).optional(),
                "complexDataTypeReferenceParsing": t.string().optional(),
                "notificationConfig": t.proxy(
                    renames["NotificationConfigIn"]
                ).optional(),
                "enableUpdateCreate": t.boolean().optional(),
                "streamConfigs": t.array(t.proxy(renames["StreamConfigIn"])).optional(),
                "disableReferentialIntegrity": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsFhirStoresTestIamPermissions"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["FhirNotificationConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "defaultSearchHandlingStrict": t.boolean().optional(),
                "version": t.string().optional(),
                "disableResourceVersioning": t.boolean().optional(),
                "validationConfig": t.proxy(renames["ValidationConfigIn"]).optional(),
                "complexDataTypeReferenceParsing": t.string().optional(),
                "notificationConfig": t.proxy(
                    renames["NotificationConfigIn"]
                ).optional(),
                "enableUpdateCreate": t.boolean().optional(),
                "streamConfigs": t.array(t.proxy(renames["StreamConfigIn"])).optional(),
                "disableReferentialIntegrity": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresDelete"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["FhirNotificationConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "defaultSearchHandlingStrict": t.boolean().optional(),
                "version": t.string().optional(),
                "disableResourceVersioning": t.boolean().optional(),
                "validationConfig": t.proxy(renames["ValidationConfigIn"]).optional(),
                "complexDataTypeReferenceParsing": t.string().optional(),
                "notificationConfig": t.proxy(
                    renames["NotificationConfigIn"]
                ).optional(),
                "enableUpdateCreate": t.boolean().optional(),
                "streamConfigs": t.array(t.proxy(renames["StreamConfigIn"])).optional(),
                "disableReferentialIntegrity": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresGet"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["FhirNotificationConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "defaultSearchHandlingStrict": t.boolean().optional(),
                "version": t.string().optional(),
                "disableResourceVersioning": t.boolean().optional(),
                "validationConfig": t.proxy(renames["ValidationConfigIn"]).optional(),
                "complexDataTypeReferenceParsing": t.string().optional(),
                "notificationConfig": t.proxy(
                    renames["NotificationConfigIn"]
                ).optional(),
                "enableUpdateCreate": t.boolean().optional(),
                "streamConfigs": t.array(t.proxy(renames["StreamConfigIn"])).optional(),
                "disableReferentialIntegrity": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsFhirStoresGetFHIRStoreMetrics"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["FhirNotificationConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "defaultSearchHandlingStrict": t.boolean().optional(),
                "version": t.string().optional(),
                "disableResourceVersioning": t.boolean().optional(),
                "validationConfig": t.proxy(renames["ValidationConfigIn"]).optional(),
                "complexDataTypeReferenceParsing": t.string().optional(),
                "notificationConfig": t.proxy(
                    renames["NotificationConfigIn"]
                ).optional(),
                "enableUpdateCreate": t.boolean().optional(),
                "streamConfigs": t.array(t.proxy(renames["StreamConfigIn"])).optional(),
                "disableReferentialIntegrity": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresGetIamPolicy"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["FhirNotificationConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "defaultSearchHandlingStrict": t.boolean().optional(),
                "version": t.string().optional(),
                "disableResourceVersioning": t.boolean().optional(),
                "validationConfig": t.proxy(renames["ValidationConfigIn"]).optional(),
                "complexDataTypeReferenceParsing": t.string().optional(),
                "notificationConfig": t.proxy(
                    renames["NotificationConfigIn"]
                ).optional(),
                "enableUpdateCreate": t.boolean().optional(),
                "streamConfigs": t.array(t.proxy(renames["StreamConfigIn"])).optional(),
                "disableReferentialIntegrity": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresImport"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["FhirNotificationConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "defaultSearchHandlingStrict": t.boolean().optional(),
                "version": t.string().optional(),
                "disableResourceVersioning": t.boolean().optional(),
                "validationConfig": t.proxy(renames["ValidationConfigIn"]).optional(),
                "complexDataTypeReferenceParsing": t.string().optional(),
                "notificationConfig": t.proxy(
                    renames["NotificationConfigIn"]
                ).optional(),
                "enableUpdateCreate": t.boolean().optional(),
                "streamConfigs": t.array(t.proxy(renames["StreamConfigIn"])).optional(),
                "disableReferentialIntegrity": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresSetIamPolicy"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["FhirNotificationConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "defaultSearchHandlingStrict": t.boolean().optional(),
                "version": t.string().optional(),
                "disableResourceVersioning": t.boolean().optional(),
                "validationConfig": t.proxy(renames["ValidationConfigIn"]).optional(),
                "complexDataTypeReferenceParsing": t.string().optional(),
                "notificationConfig": t.proxy(
                    renames["NotificationConfigIn"]
                ).optional(),
                "enableUpdateCreate": t.boolean().optional(),
                "streamConfigs": t.array(t.proxy(renames["StreamConfigIn"])).optional(),
                "disableReferentialIntegrity": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresPatch"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["FhirNotificationConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "defaultSearchHandlingStrict": t.boolean().optional(),
                "version": t.string().optional(),
                "disableResourceVersioning": t.boolean().optional(),
                "validationConfig": t.proxy(renames["ValidationConfigIn"]).optional(),
                "complexDataTypeReferenceParsing": t.string().optional(),
                "notificationConfig": t.proxy(
                    renames["NotificationConfigIn"]
                ).optional(),
                "enableUpdateCreate": t.boolean().optional(),
                "streamConfigs": t.array(t.proxy(renames["StreamConfigIn"])).optional(),
                "disableReferentialIntegrity": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FhirStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirPatch"] = healthcare.get(
        "v1/{name}/fhir/metadata",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirCreate"] = healthcare.get(
        "v1/{name}/fhir/metadata",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsFhirStoresFhirResource-validate"
    ] = healthcare.get(
        "v1/{name}/fhir/metadata",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirExecuteBundle"] = healthcare.get(
        "v1/{name}/fhir/metadata",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirRead"] = healthcare.get(
        "v1/{name}/fhir/metadata",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirSearch"] = healthcare.get(
        "v1/{name}/fhir/metadata",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirVread"] = healthcare.get(
        "v1/{name}/fhir/metadata",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirResource-purge"] = healthcare.get(
        "v1/{name}/fhir/metadata",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsFhirStoresFhirPatient-everything"
    ] = healthcare.get(
        "v1/{name}/fhir/metadata",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirUpdate"] = healthcare.get(
        "v1/{name}/fhir/metadata",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirSearch-type"] = healthcare.get(
        "v1/{name}/fhir/metadata",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirHistory"] = healthcare.get(
        "v1/{name}/fhir/metadata",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirDelete"] = healthcare.get(
        "v1/{name}/fhir/metadata",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresFhirCapabilities"] = healthcare.get(
        "v1/{name}/fhir/metadata",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresImport"] = healthcare.get(
        "v1/{parent}/dicomStores",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDicomStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresTestIamPermissions"
    ] = healthcare.get(
        "v1/{parent}/dicomStores",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDicomStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresDeidentify"] = healthcare.get(
        "v1/{parent}/dicomStores",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDicomStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresCreate"] = healthcare.get(
        "v1/{parent}/dicomStores",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDicomStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresGet"] = healthcare.get(
        "v1/{parent}/dicomStores",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDicomStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresPatch"] = healthcare.get(
        "v1/{parent}/dicomStores",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDicomStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresStoreInstances"] = healthcare.get(
        "v1/{parent}/dicomStores",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDicomStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresDelete"] = healthcare.get(
        "v1/{parent}/dicomStores",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDicomStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresSetIamPolicy"] = healthcare.get(
        "v1/{parent}/dicomStores",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDicomStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresSearchForSeries"] = healthcare.get(
        "v1/{parent}/dicomStores",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDicomStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresGetIamPolicy"] = healthcare.get(
        "v1/{parent}/dicomStores",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDicomStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresExport"] = healthcare.get(
        "v1/{parent}/dicomStores",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDicomStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresSearchForInstances"
    ] = healthcare.get(
        "v1/{parent}/dicomStores",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDicomStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresSearchForStudies"] = healthcare.get(
        "v1/{parent}/dicomStores",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDicomStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresList"] = healthcare.get(
        "v1/{parent}/dicomStores",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDicomStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsDicomStoresStudiesRetrieveMetadata"
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
        "projectsLocationsDatasetsDicomStoresStudiesSearchForSeries"
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
        "projectsLocationsDatasetsDicomStoresStudiesStoreInstances"
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
        "projectsLocationsDatasetsDicomStoresStudiesSearchForInstances"
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
    functions["projectsLocationsDatasetsDicomStoresStudiesDelete"] = healthcare.get(
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
        "projectsLocationsDatasetsDicomStoresStudiesRetrieveStudy"
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
        "projectsLocationsDatasetsDicomStoresStudiesSeriesInstancesRetrieveRendered"
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
        "projectsLocationsDatasetsDicomStoresStudiesSeriesInstancesRetrieveMetadata"
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
        "projectsLocationsDatasetsDicomStoresStudiesSeriesInstancesDelete"
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
    functions["projectsLocationsDatasetsHl7V2StoresSetIamPolicy"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsHl7V2StoresTestIamPermissions"
    ] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresImport"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresPatch"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresCreate"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresExport"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresDelete"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresList"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresGetIamPolicy"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresGet"] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresMessagesList"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresMessagesCreate"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresMessagesGet"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresMessagesIngest"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresMessagesPatch"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresMessagesDelete"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsOperationsList"] = healthcare.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsOperationsGet"] = healthcare.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsOperationsCancel"] = healthcare.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesNlpAnalyzeEntities"] = healthcare.post(
        "v1/{nlpService}:analyzeEntities",
        t.struct(
            {
                "nlpService": t.string().optional(),
                "licensedVocabularies": t.array(t.string()).optional(),
                "documentContent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeEntitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="healthcare",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
