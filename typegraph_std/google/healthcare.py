from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_healthcare() -> Import:
    healthcare = HTTPRuntime("https://healthcare.googleapis.com/")

    renames = {
        "ErrorResponse": "_healthcare_1_ErrorResponse",
        "ListMessagesResponseIn": "_healthcare_2_ListMessagesResponseIn",
        "ListMessagesResponseOut": "_healthcare_3_ListMessagesResponseOut",
        "LocationIn": "_healthcare_4_LocationIn",
        "LocationOut": "_healthcare_5_LocationOut",
        "InfoTypeTransformationIn": "_healthcare_6_InfoTypeTransformationIn",
        "InfoTypeTransformationOut": "_healthcare_7_InfoTypeTransformationOut",
        "GoogleCloudHealthcareV1FhirBigQueryDestinationIn": "_healthcare_8_GoogleCloudHealthcareV1FhirBigQueryDestinationIn",
        "GoogleCloudHealthcareV1FhirBigQueryDestinationOut": "_healthcare_9_GoogleCloudHealthcareV1FhirBigQueryDestinationOut",
        "TestIamPermissionsRequestIn": "_healthcare_10_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_healthcare_11_TestIamPermissionsRequestOut",
        "QueryAccessibleDataResponseIn": "_healthcare_12_QueryAccessibleDataResponseIn",
        "QueryAccessibleDataResponseOut": "_healthcare_13_QueryAccessibleDataResponseOut",
        "AttributeIn": "_healthcare_14_AttributeIn",
        "AttributeOut": "_healthcare_15_AttributeOut",
        "GoogleCloudHealthcareV1FhirGcsSourceIn": "_healthcare_16_GoogleCloudHealthcareV1FhirGcsSourceIn",
        "GoogleCloudHealthcareV1FhirGcsSourceOut": "_healthcare_17_GoogleCloudHealthcareV1FhirGcsSourceOut",
        "ArchiveUserDataMappingRequestIn": "_healthcare_18_ArchiveUserDataMappingRequestIn",
        "ArchiveUserDataMappingRequestOut": "_healthcare_19_ArchiveUserDataMappingRequestOut",
        "DicomFilterConfigIn": "_healthcare_20_DicomFilterConfigIn",
        "DicomFilterConfigOut": "_healthcare_21_DicomFilterConfigOut",
        "GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryIn": "_healthcare_22_GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryIn",
        "GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryOut": "_healthcare_23_GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryOut",
        "UserDataMappingIn": "_healthcare_24_UserDataMappingIn",
        "UserDataMappingOut": "_healthcare_25_UserDataMappingOut",
        "ProgressCounterIn": "_healthcare_26_ProgressCounterIn",
        "ProgressCounterOut": "_healthcare_27_ProgressCounterOut",
        "MessageIn": "_healthcare_28_MessageIn",
        "MessageOut": "_healthcare_29_MessageOut",
        "EmptyIn": "_healthcare_30_EmptyIn",
        "EmptyOut": "_healthcare_31_EmptyOut",
        "RejectConsentRequestIn": "_healthcare_32_RejectConsentRequestIn",
        "RejectConsentRequestOut": "_healthcare_33_RejectConsentRequestOut",
        "ParserConfigIn": "_healthcare_34_ParserConfigIn",
        "ParserConfigOut": "_healthcare_35_ParserConfigOut",
        "ImportResourcesRequestIn": "_healthcare_36_ImportResourcesRequestIn",
        "ImportResourcesRequestOut": "_healthcare_37_ImportResourcesRequestOut",
        "TextSpanIn": "_healthcare_38_TextSpanIn",
        "TextSpanOut": "_healthcare_39_TextSpanOut",
        "ImportMessagesRequestIn": "_healthcare_40_ImportMessagesRequestIn",
        "ImportMessagesRequestOut": "_healthcare_41_ImportMessagesRequestOut",
        "ListHl7V2StoresResponseIn": "_healthcare_42_ListHl7V2StoresResponseIn",
        "ListHl7V2StoresResponseOut": "_healthcare_43_ListHl7V2StoresResponseOut",
        "PatientIdIn": "_healthcare_44_PatientIdIn",
        "PatientIdOut": "_healthcare_45_PatientIdOut",
        "ListOperationsResponseIn": "_healthcare_46_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_healthcare_47_ListOperationsResponseOut",
        "CreateMessageRequestIn": "_healthcare_48_CreateMessageRequestIn",
        "CreateMessageRequestOut": "_healthcare_49_CreateMessageRequestOut",
        "HttpBodyIn": "_healthcare_50_HttpBodyIn",
        "HttpBodyOut": "_healthcare_51_HttpBodyOut",
        "Hl7SchemaConfigIn": "_healthcare_52_Hl7SchemaConfigIn",
        "Hl7SchemaConfigOut": "_healthcare_53_Hl7SchemaConfigOut",
        "ListUserDataMappingsResponseIn": "_healthcare_54_ListUserDataMappingsResponseIn",
        "ListUserDataMappingsResponseOut": "_healthcare_55_ListUserDataMappingsResponseOut",
        "AttributeDefinitionIn": "_healthcare_56_AttributeDefinitionIn",
        "AttributeDefinitionOut": "_healthcare_57_AttributeDefinitionOut",
        "IngestMessageResponseIn": "_healthcare_58_IngestMessageResponseIn",
        "IngestMessageResponseOut": "_healthcare_59_IngestMessageResponseOut",
        "DateShiftConfigIn": "_healthcare_60_DateShiftConfigIn",
        "DateShiftConfigOut": "_healthcare_61_DateShiftConfigOut",
        "ImportDicomDataRequestIn": "_healthcare_62_ImportDicomDataRequestIn",
        "ImportDicomDataRequestOut": "_healthcare_63_ImportDicomDataRequestOut",
        "TypeIn": "_healthcare_64_TypeIn",
        "TypeOut": "_healthcare_65_TypeOut",
        "ConsentEvaluationIn": "_healthcare_66_ConsentEvaluationIn",
        "ConsentEvaluationOut": "_healthcare_67_ConsentEvaluationOut",
        "DicomConfigIn": "_healthcare_68_DicomConfigIn",
        "DicomConfigOut": "_healthcare_69_DicomConfigOut",
        "OperationIn": "_healthcare_70_OperationIn",
        "OperationOut": "_healthcare_71_OperationOut",
        "ImportResourcesResponseIn": "_healthcare_72_ImportResourcesResponseIn",
        "ImportResourcesResponseOut": "_healthcare_73_ImportResourcesResponseOut",
        "FhirStoreIn": "_healthcare_74_FhirStoreIn",
        "FhirStoreOut": "_healthcare_75_FhirStoreOut",
        "SchemaPackageIn": "_healthcare_76_SchemaPackageIn",
        "SchemaPackageOut": "_healthcare_77_SchemaPackageOut",
        "ImportDicomDataResponseIn": "_healthcare_78_ImportDicomDataResponseIn",
        "ImportDicomDataResponseOut": "_healthcare_79_ImportDicomDataResponseOut",
        "SetIamPolicyRequestIn": "_healthcare_80_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_healthcare_81_SetIamPolicyRequestOut",
        "ExportResourcesRequestIn": "_healthcare_82_ExportResourcesRequestIn",
        "ExportResourcesRequestOut": "_healthcare_83_ExportResourcesRequestOut",
        "ResourcesIn": "_healthcare_84_ResourcesIn",
        "ResourcesOut": "_healthcare_85_ResourcesOut",
        "ConsentArtifactIn": "_healthcare_86_ConsentArtifactIn",
        "ConsentArtifactOut": "_healthcare_87_ConsentArtifactOut",
        "ExportDicomDataRequestIn": "_healthcare_88_ExportDicomDataRequestIn",
        "ExportDicomDataRequestOut": "_healthcare_89_ExportDicomDataRequestOut",
        "FieldIn": "_healthcare_90_FieldIn",
        "FieldOut": "_healthcare_91_FieldOut",
        "EntityIn": "_healthcare_92_EntityIn",
        "EntityOut": "_healthcare_93_EntityOut",
        "ReplaceWithInfoTypeConfigIn": "_healthcare_94_ReplaceWithInfoTypeConfigIn",
        "ReplaceWithInfoTypeConfigOut": "_healthcare_95_ReplaceWithInfoTypeConfigOut",
        "GcsSourceIn": "_healthcare_96_GcsSourceIn",
        "GcsSourceOut": "_healthcare_97_GcsSourceOut",
        "DeidentifySummaryIn": "_healthcare_98_DeidentifySummaryIn",
        "DeidentifySummaryOut": "_healthcare_99_DeidentifySummaryOut",
        "AuditConfigIn": "_healthcare_100_AuditConfigIn",
        "AuditConfigOut": "_healthcare_101_AuditConfigOut",
        "DeidentifyDicomStoreRequestIn": "_healthcare_102_DeidentifyDicomStoreRequestIn",
        "DeidentifyDicomStoreRequestOut": "_healthcare_103_DeidentifyDicomStoreRequestOut",
        "DeidentifyConfigIn": "_healthcare_104_DeidentifyConfigIn",
        "DeidentifyConfigOut": "_healthcare_105_DeidentifyConfigOut",
        "GoogleCloudHealthcareV1DicomBigQueryDestinationIn": "_healthcare_106_GoogleCloudHealthcareV1DicomBigQueryDestinationIn",
        "GoogleCloudHealthcareV1DicomBigQueryDestinationOut": "_healthcare_107_GoogleCloudHealthcareV1DicomBigQueryDestinationOut",
        "SignatureIn": "_healthcare_108_SignatureIn",
        "SignatureOut": "_healthcare_109_SignatureOut",
        "OperationMetadataIn": "_healthcare_110_OperationMetadataIn",
        "OperationMetadataOut": "_healthcare_111_OperationMetadataOut",
        "ImageIn": "_healthcare_112_ImageIn",
        "ImageOut": "_healthcare_113_ImageOut",
        "ExportResourcesResponseIn": "_healthcare_114_ExportResourcesResponseIn",
        "ExportResourcesResponseOut": "_healthcare_115_ExportResourcesResponseOut",
        "AnalyzeEntitiesRequestIn": "_healthcare_116_AnalyzeEntitiesRequestIn",
        "AnalyzeEntitiesRequestOut": "_healthcare_117_AnalyzeEntitiesRequestOut",
        "ParsedDataIn": "_healthcare_118_ParsedDataIn",
        "ParsedDataOut": "_healthcare_119_ParsedDataOut",
        "DeidentifyDatasetRequestIn": "_healthcare_120_DeidentifyDatasetRequestIn",
        "DeidentifyDatasetRequestOut": "_healthcare_121_DeidentifyDatasetRequestOut",
        "EvaluateUserConsentsResponseIn": "_healthcare_122_EvaluateUserConsentsResponseIn",
        "EvaluateUserConsentsResponseOut": "_healthcare_123_EvaluateUserConsentsResponseOut",
        "ExportMessagesResponseIn": "_healthcare_124_ExportMessagesResponseIn",
        "ExportMessagesResponseOut": "_healthcare_125_ExportMessagesResponseOut",
        "TestIamPermissionsResponseIn": "_healthcare_126_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_healthcare_127_TestIamPermissionsResponseOut",
        "GroupOrSegmentIn": "_healthcare_128_GroupOrSegmentIn",
        "GroupOrSegmentOut": "_healthcare_129_GroupOrSegmentOut",
        "CheckDataAccessRequestIn": "_healthcare_130_CheckDataAccessRequestIn",
        "CheckDataAccessRequestOut": "_healthcare_131_CheckDataAccessRequestOut",
        "SegmentIn": "_healthcare_132_SegmentIn",
        "SegmentOut": "_healthcare_133_SegmentOut",
        "GoogleCloudHealthcareV1DicomGcsSourceIn": "_healthcare_134_GoogleCloudHealthcareV1DicomGcsSourceIn",
        "GoogleCloudHealthcareV1DicomGcsSourceOut": "_healthcare_135_GoogleCloudHealthcareV1DicomGcsSourceOut",
        "VersionSourceIn": "_healthcare_136_VersionSourceIn",
        "VersionSourceOut": "_healthcare_137_VersionSourceOut",
        "BindingIn": "_healthcare_138_BindingIn",
        "BindingOut": "_healthcare_139_BindingOut",
        "FhirNotificationConfigIn": "_healthcare_140_FhirNotificationConfigIn",
        "FhirNotificationConfigOut": "_healthcare_141_FhirNotificationConfigOut",
        "CharacterMaskConfigIn": "_healthcare_142_CharacterMaskConfigIn",
        "CharacterMaskConfigOut": "_healthcare_143_CharacterMaskConfigOut",
        "CancelOperationRequestIn": "_healthcare_144_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_healthcare_145_CancelOperationRequestOut",
        "ListDicomStoresResponseIn": "_healthcare_146_ListDicomStoresResponseIn",
        "ListDicomStoresResponseOut": "_healthcare_147_ListDicomStoresResponseOut",
        "FhirStoreMetricsIn": "_healthcare_148_FhirStoreMetricsIn",
        "FhirStoreMetricsOut": "_healthcare_149_FhirStoreMetricsOut",
        "ListAttributeDefinitionsResponseIn": "_healthcare_150_ListAttributeDefinitionsResponseIn",
        "ListAttributeDefinitionsResponseOut": "_healthcare_151_ListAttributeDefinitionsResponseOut",
        "DeidentifiedStoreDestinationIn": "_healthcare_152_DeidentifiedStoreDestinationIn",
        "DeidentifiedStoreDestinationOut": "_healthcare_153_DeidentifiedStoreDestinationOut",
        "DatasetIn": "_healthcare_154_DatasetIn",
        "DatasetOut": "_healthcare_155_DatasetOut",
        "GcsDestinationIn": "_healthcare_156_GcsDestinationIn",
        "GcsDestinationOut": "_healthcare_157_GcsDestinationOut",
        "ResultIn": "_healthcare_158_ResultIn",
        "ResultOut": "_healthcare_159_ResultOut",
        "Hl7TypesConfigIn": "_healthcare_160_Hl7TypesConfigIn",
        "Hl7TypesConfigOut": "_healthcare_161_Hl7TypesConfigOut",
        "DeidentifyFhirStoreRequestIn": "_healthcare_162_DeidentifyFhirStoreRequestIn",
        "DeidentifyFhirStoreRequestOut": "_healthcare_163_DeidentifyFhirStoreRequestOut",
        "GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryIn": "_healthcare_164_GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryIn",
        "GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryOut": "_healthcare_165_GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryOut",
        "ListConsentRevisionsResponseIn": "_healthcare_166_ListConsentRevisionsResponseIn",
        "ListConsentRevisionsResponseOut": "_healthcare_167_ListConsentRevisionsResponseOut",
        "FieldMetadataIn": "_healthcare_168_FieldMetadataIn",
        "FieldMetadataOut": "_healthcare_169_FieldMetadataOut",
        "ConsentIn": "_healthcare_170_ConsentIn",
        "ConsentOut": "_healthcare_171_ConsentOut",
        "TextConfigIn": "_healthcare_172_TextConfigIn",
        "TextConfigOut": "_healthcare_173_TextConfigOut",
        "NotificationConfigIn": "_healthcare_174_NotificationConfigIn",
        "NotificationConfigOut": "_healthcare_175_NotificationConfigOut",
        "ImageConfigIn": "_healthcare_176_ImageConfigIn",
        "ImageConfigOut": "_healthcare_177_ImageConfigOut",
        "ConsentStoreIn": "_healthcare_178_ConsentStoreIn",
        "ConsentStoreOut": "_healthcare_179_ConsentStoreOut",
        "ExportDicomDataResponseIn": "_healthcare_180_ExportDicomDataResponseIn",
        "ExportDicomDataResponseOut": "_healthcare_181_ExportDicomDataResponseOut",
        "SchemaGroupIn": "_healthcare_182_SchemaGroupIn",
        "SchemaGroupOut": "_healthcare_183_SchemaGroupOut",
        "ConsentListIn": "_healthcare_184_ConsentListIn",
        "ConsentListOut": "_healthcare_185_ConsentListOut",
        "ListConsentStoresResponseIn": "_healthcare_186_ListConsentStoresResponseIn",
        "ListConsentStoresResponseOut": "_healthcare_187_ListConsentStoresResponseOut",
        "GoogleCloudHealthcareV1ConsentPolicyIn": "_healthcare_188_GoogleCloudHealthcareV1ConsentPolicyIn",
        "GoogleCloudHealthcareV1ConsentPolicyOut": "_healthcare_189_GoogleCloudHealthcareV1ConsentPolicyOut",
        "ImportMessagesResponseIn": "_healthcare_190_ImportMessagesResponseIn",
        "ImportMessagesResponseOut": "_healthcare_191_ImportMessagesResponseOut",
        "KmsWrappedCryptoKeyIn": "_healthcare_192_KmsWrappedCryptoKeyIn",
        "KmsWrappedCryptoKeyOut": "_healthcare_193_KmsWrappedCryptoKeyOut",
        "QueryAccessibleDataRequestIn": "_healthcare_194_QueryAccessibleDataRequestIn",
        "QueryAccessibleDataRequestOut": "_healthcare_195_QueryAccessibleDataRequestOut",
        "AuditLogConfigIn": "_healthcare_196_AuditLogConfigIn",
        "AuditLogConfigOut": "_healthcare_197_AuditLogConfigOut",
        "StatusIn": "_healthcare_198_StatusIn",
        "StatusOut": "_healthcare_199_StatusOut",
        "Hl7V2NotificationConfigIn": "_healthcare_200_Hl7V2NotificationConfigIn",
        "Hl7V2NotificationConfigOut": "_healthcare_201_Hl7V2NotificationConfigOut",
        "FhirConfigIn": "_healthcare_202_FhirConfigIn",
        "FhirConfigOut": "_healthcare_203_FhirConfigOut",
        "DicomStoreIn": "_healthcare_204_DicomStoreIn",
        "DicomStoreOut": "_healthcare_205_DicomStoreOut",
        "ExprIn": "_healthcare_206_ExprIn",
        "ExprOut": "_healthcare_207_ExprOut",
        "ListDatasetsResponseIn": "_healthcare_208_ListDatasetsResponseIn",
        "ListDatasetsResponseOut": "_healthcare_209_ListDatasetsResponseOut",
        "SchemaConfigIn": "_healthcare_210_SchemaConfigIn",
        "SchemaConfigOut": "_healthcare_211_SchemaConfigOut",
        "ListConsentsResponseIn": "_healthcare_212_ListConsentsResponseIn",
        "ListConsentsResponseOut": "_healthcare_213_ListConsentsResponseOut",
        "GoogleCloudHealthcareV1ConsentGcsDestinationIn": "_healthcare_214_GoogleCloudHealthcareV1ConsentGcsDestinationIn",
        "GoogleCloudHealthcareV1ConsentGcsDestinationOut": "_healthcare_215_GoogleCloudHealthcareV1ConsentGcsDestinationOut",
        "ListFhirStoresResponseIn": "_healthcare_216_ListFhirStoresResponseIn",
        "ListFhirStoresResponseOut": "_healthcare_217_ListFhirStoresResponseOut",
        "FhirFilterIn": "_healthcare_218_FhirFilterIn",
        "FhirFilterOut": "_healthcare_219_FhirFilterOut",
        "EntityMentionIn": "_healthcare_220_EntityMentionIn",
        "EntityMentionOut": "_healthcare_221_EntityMentionOut",
        "Hl7V2StoreIn": "_healthcare_222_Hl7V2StoreIn",
        "Hl7V2StoreOut": "_healthcare_223_Hl7V2StoreOut",
        "SearchResourcesRequestIn": "_healthcare_224_SearchResourcesRequestIn",
        "SearchResourcesRequestOut": "_healthcare_225_SearchResourcesRequestOut",
        "LinkedEntityIn": "_healthcare_226_LinkedEntityIn",
        "LinkedEntityOut": "_healthcare_227_LinkedEntityOut",
        "ArchiveUserDataMappingResponseIn": "_healthcare_228_ArchiveUserDataMappingResponseIn",
        "ArchiveUserDataMappingResponseOut": "_healthcare_229_ArchiveUserDataMappingResponseOut",
        "CryptoHashConfigIn": "_healthcare_230_CryptoHashConfigIn",
        "CryptoHashConfigOut": "_healthcare_231_CryptoHashConfigOut",
        "RedactConfigIn": "_healthcare_232_RedactConfigIn",
        "RedactConfigOut": "_healthcare_233_RedactConfigOut",
        "GoogleCloudHealthcareV1FhirGcsDestinationIn": "_healthcare_234_GoogleCloudHealthcareV1FhirGcsDestinationIn",
        "GoogleCloudHealthcareV1FhirGcsDestinationOut": "_healthcare_235_GoogleCloudHealthcareV1FhirGcsDestinationOut",
        "EvaluateUserConsentsRequestIn": "_healthcare_236_EvaluateUserConsentsRequestIn",
        "EvaluateUserConsentsRequestOut": "_healthcare_237_EvaluateUserConsentsRequestOut",
        "FeatureIn": "_healthcare_238_FeatureIn",
        "FeatureOut": "_healthcare_239_FeatureOut",
        "ValidationConfigIn": "_healthcare_240_ValidationConfigIn",
        "ValidationConfigOut": "_healthcare_241_ValidationConfigOut",
        "StreamConfigIn": "_healthcare_242_StreamConfigIn",
        "StreamConfigOut": "_healthcare_243_StreamConfigOut",
        "IngestMessageRequestIn": "_healthcare_244_IngestMessageRequestIn",
        "IngestMessageRequestOut": "_healthcare_245_IngestMessageRequestOut",
        "ListConsentArtifactsResponseIn": "_healthcare_246_ListConsentArtifactsResponseIn",
        "ListConsentArtifactsResponseOut": "_healthcare_247_ListConsentArtifactsResponseOut",
        "RevokeConsentRequestIn": "_healthcare_248_RevokeConsentRequestIn",
        "RevokeConsentRequestOut": "_healthcare_249_RevokeConsentRequestOut",
        "ActivateConsentRequestIn": "_healthcare_250_ActivateConsentRequestIn",
        "ActivateConsentRequestOut": "_healthcare_251_ActivateConsentRequestOut",
        "AnalyzeEntitiesResponseIn": "_healthcare_252_AnalyzeEntitiesResponseIn",
        "AnalyzeEntitiesResponseOut": "_healthcare_253_AnalyzeEntitiesResponseOut",
        "SchematizedDataIn": "_healthcare_254_SchematizedDataIn",
        "SchematizedDataOut": "_healthcare_255_SchematizedDataOut",
        "CheckDataAccessResponseIn": "_healthcare_256_CheckDataAccessResponseIn",
        "CheckDataAccessResponseOut": "_healthcare_257_CheckDataAccessResponseOut",
        "SchemaSegmentIn": "_healthcare_258_SchemaSegmentIn",
        "SchemaSegmentOut": "_healthcare_259_SchemaSegmentOut",
        "FhirStoreMetricIn": "_healthcare_260_FhirStoreMetricIn",
        "FhirStoreMetricOut": "_healthcare_261_FhirStoreMetricOut",
        "GoogleCloudHealthcareV1DicomGcsDestinationIn": "_healthcare_262_GoogleCloudHealthcareV1DicomGcsDestinationIn",
        "GoogleCloudHealthcareV1DicomGcsDestinationOut": "_healthcare_263_GoogleCloudHealthcareV1DicomGcsDestinationOut",
        "ListLocationsResponseIn": "_healthcare_264_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_healthcare_265_ListLocationsResponseOut",
        "PolicyIn": "_healthcare_266_PolicyIn",
        "PolicyOut": "_healthcare_267_PolicyOut",
        "EntityMentionRelationshipIn": "_healthcare_268_EntityMentionRelationshipIn",
        "EntityMentionRelationshipOut": "_healthcare_269_EntityMentionRelationshipOut",
        "TimePartitioningIn": "_healthcare_270_TimePartitioningIn",
        "TimePartitioningOut": "_healthcare_271_TimePartitioningOut",
        "ExportMessagesRequestIn": "_healthcare_272_ExportMessagesRequestIn",
        "ExportMessagesRequestOut": "_healthcare_273_ExportMessagesRequestOut",
        "TagFilterListIn": "_healthcare_274_TagFilterListIn",
        "TagFilterListOut": "_healthcare_275_TagFilterListOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["InfoTypeTransformationIn"] = t.struct(
        {
            "infoTypes": t.array(t.string()).optional(),
            "dateShiftConfig": t.proxy(renames["DateShiftConfigIn"]).optional(),
            "characterMaskConfig": t.proxy(renames["CharacterMaskConfigIn"]).optional(),
            "cryptoHashConfig": t.proxy(renames["CryptoHashConfigIn"]).optional(),
            "redactConfig": t.proxy(renames["RedactConfigIn"]).optional(),
            "replaceWithInfoTypeConfig": t.proxy(
                renames["ReplaceWithInfoTypeConfigIn"]
            ).optional(),
        }
    ).named(renames["InfoTypeTransformationIn"])
    types["InfoTypeTransformationOut"] = t.struct(
        {
            "infoTypes": t.array(t.string()).optional(),
            "dateShiftConfig": t.proxy(renames["DateShiftConfigOut"]).optional(),
            "characterMaskConfig": t.proxy(
                renames["CharacterMaskConfigOut"]
            ).optional(),
            "cryptoHashConfig": t.proxy(renames["CryptoHashConfigOut"]).optional(),
            "redactConfig": t.proxy(renames["RedactConfigOut"]).optional(),
            "replaceWithInfoTypeConfig": t.proxy(
                renames["ReplaceWithInfoTypeConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InfoTypeTransformationOut"])
    types["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"] = t.struct(
        {
            "force": t.boolean().optional(),
            "writeDisposition": t.string().optional(),
            "datasetUri": t.string().optional(),
            "schemaConfig": t.proxy(renames["SchemaConfigIn"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"])
    types["GoogleCloudHealthcareV1FhirBigQueryDestinationOut"] = t.struct(
        {
            "force": t.boolean().optional(),
            "writeDisposition": t.string().optional(),
            "datasetUri": t.string().optional(),
            "schemaConfig": t.proxy(renames["SchemaConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1FhirBigQueryDestinationOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["QueryAccessibleDataResponseIn"] = t.struct(
        {"gcsUris": t.array(t.string()).optional()}
    ).named(renames["QueryAccessibleDataResponseIn"])
    types["QueryAccessibleDataResponseOut"] = t.struct(
        {
            "gcsUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryAccessibleDataResponseOut"])
    types["AttributeIn"] = t.struct(
        {"values": t.array(t.string()), "attributeDefinitionId": t.string().optional()}
    ).named(renames["AttributeIn"])
    types["AttributeOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "attributeDefinitionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeOut"])
    types["GoogleCloudHealthcareV1FhirGcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1FhirGcsSourceIn"])
    types["GoogleCloudHealthcareV1FhirGcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1FhirGcsSourceOut"])
    types["ArchiveUserDataMappingRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ArchiveUserDataMappingRequestIn"])
    types["ArchiveUserDataMappingRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ArchiveUserDataMappingRequestOut"])
    types["DicomFilterConfigIn"] = t.struct(
        {"resourcePathsGcsUri": t.string().optional()}
    ).named(renames["DicomFilterConfigIn"])
    types["DicomFilterConfigOut"] = t.struct(
        {
            "resourcePathsGcsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DicomFilterConfigOut"])
    types["GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryIn"])
    types["GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummaryOut"])
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
            "userId": t.string(),
            "dataId": t.string(),
            "resourceAttributes": t.array(t.proxy(renames["AttributeOut"])).optional(),
            "archiveTime": t.string().optional(),
            "name": t.string().optional(),
            "archived": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserDataMappingOut"])
    types["ProgressCounterIn"] = t.struct(
        {
            "pending": t.string().optional(),
            "success": t.string().optional(),
            "failure": t.string().optional(),
        }
    ).named(renames["ProgressCounterIn"])
    types["ProgressCounterOut"] = t.struct(
        {
            "pending": t.string().optional(),
            "success": t.string().optional(),
            "failure": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProgressCounterOut"])
    types["MessageIn"] = t.struct(
        {
            "schematizedData": t.proxy(renames["SchematizedDataIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "patientIds": t.array(t.proxy(renames["PatientIdIn"])).optional(),
            "data": t.string().optional(),
            "messageType": t.string().optional(),
            "sendTime": t.string().optional(),
            "name": t.string().optional(),
            "sendFacility": t.string().optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "schematizedData": t.proxy(renames["SchematizedDataOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "patientIds": t.array(t.proxy(renames["PatientIdOut"])).optional(),
            "data": t.string().optional(),
            "parsedData": t.proxy(renames["ParsedDataOut"]).optional(),
            "messageType": t.string().optional(),
            "sendTime": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "sendFacility": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["RejectConsentRequestIn"] = t.struct(
        {"consentArtifact": t.string().optional()}
    ).named(renames["RejectConsentRequestIn"])
    types["RejectConsentRequestOut"] = t.struct(
        {
            "consentArtifact": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RejectConsentRequestOut"])
    types["ParserConfigIn"] = t.struct(
        {
            "allowNullHeader": t.boolean().optional(),
            "segmentTerminator": t.string().optional(),
            "schema": t.proxy(renames["SchemaPackageIn"]).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["ParserConfigIn"])
    types["ParserConfigOut"] = t.struct(
        {
            "allowNullHeader": t.boolean().optional(),
            "segmentTerminator": t.string().optional(),
            "schema": t.proxy(renames["SchemaPackageOut"]).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParserConfigOut"])
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
    types["ImportMessagesRequestIn"] = t.struct(
        {"gcsSource": t.proxy(renames["GcsSourceIn"]).optional()}
    ).named(renames["ImportMessagesRequestIn"])
    types["ImportMessagesRequestOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportMessagesRequestOut"])
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
    types["CreateMessageRequestIn"] = t.struct(
        {"message": t.proxy(renames["MessageIn"]).optional()}
    ).named(renames["CreateMessageRequestIn"])
    types["CreateMessageRequestOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateMessageRequestOut"])
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
    types["ListUserDataMappingsResponseIn"] = t.struct(
        {
            "userDataMappings": t.array(
                t.proxy(renames["UserDataMappingIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListUserDataMappingsResponseIn"])
    types["ListUserDataMappingsResponseOut"] = t.struct(
        {
            "userDataMappings": t.array(
                t.proxy(renames["UserDataMappingOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUserDataMappingsResponseOut"])
    types["AttributeDefinitionIn"] = t.struct(
        {
            "category": t.string(),
            "allowedValues": t.array(t.string()),
            "consentDefaultValues": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "dataMappingDefaultValue": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["AttributeDefinitionIn"])
    types["AttributeDefinitionOut"] = t.struct(
        {
            "category": t.string(),
            "allowedValues": t.array(t.string()),
            "consentDefaultValues": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "dataMappingDefaultValue": t.string().optional(),
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
    types["TypeIn"] = t.struct(
        {
            "primitive": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "primitive": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["ConsentEvaluationIn"] = t.struct(
        {"evaluationResult": t.string().optional()}
    ).named(renames["ConsentEvaluationIn"])
    types["ConsentEvaluationOut"] = t.struct(
        {
            "evaluationResult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentEvaluationOut"])
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
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["ImportResourcesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ImportResourcesResponseIn"]
    )
    types["ImportResourcesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportResourcesResponseOut"])
    types["FhirStoreIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigIn"]).optional(),
            "validationConfig": t.proxy(renames["ValidationConfigIn"]).optional(),
            "defaultSearchHandlingStrict": t.boolean().optional(),
            "disableReferentialIntegrity": t.boolean().optional(),
            "complexDataTypeReferenceParsing": t.string().optional(),
            "enableUpdateCreate": t.boolean().optional(),
            "disableResourceVersioning": t.boolean().optional(),
            "streamConfigs": t.array(t.proxy(renames["StreamConfigIn"])).optional(),
            "notificationConfigs": t.array(
                t.proxy(renames["FhirNotificationConfigIn"])
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["FhirStoreIn"])
    types["FhirStoreOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigOut"]).optional(),
            "validationConfig": t.proxy(renames["ValidationConfigOut"]).optional(),
            "defaultSearchHandlingStrict": t.boolean().optional(),
            "disableReferentialIntegrity": t.boolean().optional(),
            "complexDataTypeReferenceParsing": t.string().optional(),
            "enableUpdateCreate": t.boolean().optional(),
            "disableResourceVersioning": t.boolean().optional(),
            "streamConfigs": t.array(t.proxy(renames["StreamConfigOut"])).optional(),
            "notificationConfigs": t.array(
                t.proxy(renames["FhirNotificationConfigOut"])
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FhirStoreOut"])
    types["SchemaPackageIn"] = t.struct(
        {
            "types": t.array(t.proxy(renames["Hl7TypesConfigIn"])).optional(),
            "schemas": t.array(t.proxy(renames["Hl7SchemaConfigIn"])).optional(),
            "ignoreMinOccurs": t.boolean().optional(),
            "unexpectedSegmentHandling": t.string().optional(),
            "schematizedParsingType": t.string().optional(),
        }
    ).named(renames["SchemaPackageIn"])
    types["SchemaPackageOut"] = t.struct(
        {
            "types": t.array(t.proxy(renames["Hl7TypesConfigOut"])).optional(),
            "schemas": t.array(t.proxy(renames["Hl7SchemaConfigOut"])).optional(),
            "ignoreMinOccurs": t.boolean().optional(),
            "unexpectedSegmentHandling": t.string().optional(),
            "schematizedParsingType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaPackageOut"])
    types["ImportDicomDataResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ImportDicomDataResponseIn"]
    )
    types["ImportDicomDataResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportDicomDataResponseOut"])
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
    types["ExportResourcesRequestIn"] = t.struct(
        {
            "_since": t.string().optional(),
            "_type": t.string().optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"]
            ).optional(),
            "bigqueryDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirBigQueryDestinationIn"]
            ).optional(),
        }
    ).named(renames["ExportResourcesRequestIn"])
    types["ExportResourcesRequestOut"] = t.struct(
        {
            "_since": t.string().optional(),
            "_type": t.string().optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirGcsDestinationOut"]
            ).optional(),
            "bigqueryDestination": t.proxy(
                renames["GoogleCloudHealthcareV1FhirBigQueryDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportResourcesRequestOut"])
    types["ResourcesIn"] = t.struct(
        {"resources": t.array(t.string()).optional()}
    ).named(renames["ResourcesIn"])
    types["ResourcesOut"] = t.struct(
        {
            "resources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourcesOut"])
    types["ConsentArtifactIn"] = t.struct(
        {
            "witnessSignature": t.proxy(renames["SignatureIn"]).optional(),
            "consentContentScreenshots": t.array(
                t.proxy(renames["ImageIn"])
            ).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "guardianSignature": t.proxy(renames["SignatureIn"]).optional(),
            "userId": t.string(),
            "consentContentVersion": t.string().optional(),
            "userSignature": t.proxy(renames["SignatureIn"]).optional(),
        }
    ).named(renames["ConsentArtifactIn"])
    types["ConsentArtifactOut"] = t.struct(
        {
            "witnessSignature": t.proxy(renames["SignatureOut"]).optional(),
            "consentContentScreenshots": t.array(
                t.proxy(renames["ImageOut"])
            ).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "guardianSignature": t.proxy(renames["SignatureOut"]).optional(),
            "userId": t.string(),
            "consentContentVersion": t.string().optional(),
            "userSignature": t.proxy(renames["SignatureOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentArtifactOut"])
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
    types["FieldIn"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "maxOccurs": t.integer().optional(),
            "table": t.string().optional(),
            "minOccurs": t.integer().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "maxOccurs": t.integer().optional(),
            "table": t.string().optional(),
            "minOccurs": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
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
    types["ReplaceWithInfoTypeConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReplaceWithInfoTypeConfigIn"]
    )
    types["ReplaceWithInfoTypeConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReplaceWithInfoTypeConfigOut"])
    types["GcsSourceIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["GcsSourceIn"]
    )
    types["GcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsSourceOut"])
    types["DeidentifySummaryIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeidentifySummaryIn"]
    )
    types["DeidentifySummaryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeidentifySummaryOut"])
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
    types["DeidentifyDicomStoreRequestIn"] = t.struct(
        {
            "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
            "gcsConfigUri": t.string().optional(),
            "filterConfig": t.proxy(renames["DicomFilterConfigIn"]).optional(),
            "destinationStore": t.string().optional(),
        }
    ).named(renames["DeidentifyDicomStoreRequestIn"])
    types["DeidentifyDicomStoreRequestOut"] = t.struct(
        {
            "config": t.proxy(renames["DeidentifyConfigOut"]).optional(),
            "gcsConfigUri": t.string().optional(),
            "filterConfig": t.proxy(renames["DicomFilterConfigOut"]).optional(),
            "destinationStore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeidentifyDicomStoreRequestOut"])
    types["DeidentifyConfigIn"] = t.struct(
        {
            "fhir": t.proxy(renames["FhirConfigIn"]).optional(),
            "dicom": t.proxy(renames["DicomConfigIn"]).optional(),
            "image": t.proxy(renames["ImageConfigIn"]).optional(),
            "useRegionalDataProcessing": t.boolean().optional(),
            "text": t.proxy(renames["TextConfigIn"]).optional(),
        }
    ).named(renames["DeidentifyConfigIn"])
    types["DeidentifyConfigOut"] = t.struct(
        {
            "fhir": t.proxy(renames["FhirConfigOut"]).optional(),
            "dicom": t.proxy(renames["DicomConfigOut"]).optional(),
            "image": t.proxy(renames["ImageConfigOut"]).optional(),
            "useRegionalDataProcessing": t.boolean().optional(),
            "text": t.proxy(renames["TextConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeidentifyConfigOut"])
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
    types["SignatureIn"] = t.struct(
        {
            "userId": t.string(),
            "signatureTime": t.string().optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SignatureIn"])
    types["SignatureOut"] = t.struct(
        {
            "userId": t.string(),
            "signatureTime": t.string().optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignatureOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "counter": t.proxy(renames["ProgressCounterIn"]),
            "cancelRequested": t.boolean().optional(),
            "endTime": t.string().optional(),
            "logsUrl": t.string().optional(),
            "createTime": t.string().optional(),
            "apiMethodName": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "counter": t.proxy(renames["ProgressCounterOut"]),
            "cancelRequested": t.boolean().optional(),
            "endTime": t.string().optional(),
            "logsUrl": t.string().optional(),
            "createTime": t.string().optional(),
            "apiMethodName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["ExportResourcesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ExportResourcesResponseIn"]
    )
    types["ExportResourcesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExportResourcesResponseOut"])
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
    types["ParsedDataIn"] = t.struct(
        {"segments": t.array(t.proxy(renames["SegmentIn"]))}
    ).named(renames["ParsedDataIn"])
    types["ParsedDataOut"] = t.struct(
        {
            "segments": t.array(t.proxy(renames["SegmentOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParsedDataOut"])
    types["DeidentifyDatasetRequestIn"] = t.struct(
        {
            "destinationDataset": t.string().optional(),
            "gcsConfigUri": t.string().optional(),
            "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
        }
    ).named(renames["DeidentifyDatasetRequestIn"])
    types["DeidentifyDatasetRequestOut"] = t.struct(
        {
            "destinationDataset": t.string().optional(),
            "gcsConfigUri": t.string().optional(),
            "config": t.proxy(renames["DeidentifyConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeidentifyDatasetRequestOut"])
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
    types["ExportMessagesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ExportMessagesResponseIn"]
    )
    types["ExportMessagesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExportMessagesResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["CheckDataAccessRequestIn"] = t.struct(
        {
            "requestAttributes": t.struct({"_": t.string().optional()}).optional(),
            "consentList": t.proxy(renames["ConsentListIn"]).optional(),
            "dataId": t.string(),
            "responseView": t.string().optional(),
        }
    ).named(renames["CheckDataAccessRequestIn"])
    types["CheckDataAccessRequestOut"] = t.struct(
        {
            "requestAttributes": t.struct({"_": t.string().optional()}).optional(),
            "consentList": t.proxy(renames["ConsentListOut"]).optional(),
            "dataId": t.string(),
            "responseView": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckDataAccessRequestOut"])
    types["SegmentIn"] = t.struct(
        {
            "setId": t.string().optional(),
            "segmentId": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SegmentIn"])
    types["SegmentOut"] = t.struct(
        {
            "setId": t.string().optional(),
            "segmentId": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentOut"])
    types["GoogleCloudHealthcareV1DicomGcsSourceIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1DicomGcsSourceIn"])
    types["GoogleCloudHealthcareV1DicomGcsSourceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1DicomGcsSourceOut"])
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
    types["FhirNotificationConfigIn"] = t.struct(
        {
            "pubsubTopic": t.string().optional(),
            "sendFullResource": t.boolean().optional(),
            "sendPreviousResourceOnDelete": t.boolean().optional(),
        }
    ).named(renames["FhirNotificationConfigIn"])
    types["FhirNotificationConfigOut"] = t.struct(
        {
            "pubsubTopic": t.string().optional(),
            "sendFullResource": t.boolean().optional(),
            "sendPreviousResourceOnDelete": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FhirNotificationConfigOut"])
    types["CharacterMaskConfigIn"] = t.struct(
        {"maskingCharacter": t.string().optional()}
    ).named(renames["CharacterMaskConfigIn"])
    types["CharacterMaskConfigOut"] = t.struct(
        {
            "maskingCharacter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CharacterMaskConfigOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["DatasetIn"] = t.struct(
        {"name": t.string().optional(), "timeZone": t.string().optional()}
    ).named(renames["DatasetIn"])
    types["DatasetOut"] = t.struct(
        {
            "name": t.string().optional(),
            "timeZone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetOut"])
    types["GcsDestinationIn"] = t.struct(
        {
            "messageView": t.string().optional(),
            "uriPrefix": t.string().optional(),
            "contentStructure": t.string().optional(),
        }
    ).named(renames["GcsDestinationIn"])
    types["GcsDestinationOut"] = t.struct(
        {
            "messageView": t.string().optional(),
            "uriPrefix": t.string().optional(),
            "contentStructure": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsDestinationOut"])
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
    types["DeidentifyFhirStoreRequestIn"] = t.struct(
        {
            "resourceFilter": t.proxy(renames["FhirFilterIn"]).optional(),
            "gcsConfigUri": t.string().optional(),
            "skipModifiedResources": t.boolean().optional(),
            "config": t.proxy(renames["DeidentifyConfigIn"]).optional(),
            "destinationStore": t.string().optional(),
        }
    ).named(renames["DeidentifyFhirStoreRequestIn"])
    types["DeidentifyFhirStoreRequestOut"] = t.struct(
        {
            "resourceFilter": t.proxy(renames["FhirFilterOut"]).optional(),
            "gcsConfigUri": t.string().optional(),
            "skipModifiedResources": t.boolean().optional(),
            "config": t.proxy(renames["DeidentifyConfigOut"]).optional(),
            "destinationStore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeidentifyFhirStoreRequestOut"])
    types["GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryIn"])
    types["GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummaryOut"])
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
    types["ConsentIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string(),
            "policies": t.array(
                t.proxy(renames["GoogleCloudHealthcareV1ConsentPolicyIn"])
            ).optional(),
            "name": t.string().optional(),
            "userId": t.string(),
            "expireTime": t.string().optional(),
            "consentArtifact": t.string(),
            "ttl": t.string().optional(),
        }
    ).named(renames["ConsentIn"])
    types["ConsentOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string(),
            "policies": t.array(
                t.proxy(renames["GoogleCloudHealthcareV1ConsentPolicyOut"])
            ).optional(),
            "name": t.string().optional(),
            "revisionCreateTime": t.string().optional(),
            "userId": t.string(),
            "expireTime": t.string().optional(),
            "revisionId": t.string().optional(),
            "consentArtifact": t.string(),
            "ttl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentOut"])
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
    types["NotificationConfigIn"] = t.struct(
        {"pubsubTopic": t.string().optional()}
    ).named(renames["NotificationConfigIn"])
    types["NotificationConfigOut"] = t.struct(
        {
            "pubsubTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationConfigOut"])
    types["ImageConfigIn"] = t.struct(
        {"textRedactionMode": t.string().optional()}
    ).named(renames["ImageConfigIn"])
    types["ImageConfigOut"] = t.struct(
        {
            "textRedactionMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageConfigOut"])
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
    types["ExportDicomDataResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ExportDicomDataResponseIn"]
    )
    types["ExportDicomDataResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExportDicomDataResponseOut"])
    types["SchemaGroupIn"] = t.struct(
        {
            "name": t.string().optional(),
            "minOccurs": t.integer().optional(),
            "members": t.array(t.proxy(renames["GroupOrSegmentIn"])).optional(),
            "maxOccurs": t.integer().optional(),
            "choice": t.boolean().optional(),
        }
    ).named(renames["SchemaGroupIn"])
    types["SchemaGroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "minOccurs": t.integer().optional(),
            "members": t.array(t.proxy(renames["GroupOrSegmentOut"])).optional(),
            "maxOccurs": t.integer().optional(),
            "choice": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaGroupOut"])
    types["ConsentListIn"] = t.struct(
        {"consents": t.array(t.string()).optional()}
    ).named(renames["ConsentListIn"])
    types["ConsentListOut"] = t.struct(
        {
            "consents": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsentListOut"])
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
    types["ImportMessagesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ImportMessagesResponseIn"]
    )
    types["ImportMessagesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportMessagesResponseOut"])
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
    types["FhirConfigIn"] = t.struct(
        {
            "defaultKeepExtensions": t.boolean().optional(),
            "fieldMetadataList": t.array(
                t.proxy(renames["FieldMetadataIn"])
            ).optional(),
        }
    ).named(renames["FhirConfigIn"])
    types["FhirConfigOut"] = t.struct(
        {
            "defaultKeepExtensions": t.boolean().optional(),
            "fieldMetadataList": t.array(
                t.proxy(renames["FieldMetadataOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FhirConfigOut"])
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
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
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
    types["SchemaConfigIn"] = t.struct(
        {
            "lastUpdatedPartitionConfig": t.proxy(
                renames["TimePartitioningIn"]
            ).optional(),
            "recursiveStructureDepth": t.string().optional(),
            "schemaType": t.string().optional(),
        }
    ).named(renames["SchemaConfigIn"])
    types["SchemaConfigOut"] = t.struct(
        {
            "lastUpdatedPartitionConfig": t.proxy(
                renames["TimePartitioningOut"]
            ).optional(),
            "recursiveStructureDepth": t.string().optional(),
            "schemaType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaConfigOut"])
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
    types["GoogleCloudHealthcareV1ConsentGcsDestinationIn"] = t.struct(
        {"uriPrefix": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1ConsentGcsDestinationIn"])
    types["GoogleCloudHealthcareV1ConsentGcsDestinationOut"] = t.struct(
        {
            "uriPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1ConsentGcsDestinationOut"])
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
    types["FhirFilterIn"] = t.struct(
        {"resources": t.proxy(renames["ResourcesIn"]).optional()}
    ).named(renames["FhirFilterIn"])
    types["FhirFilterOut"] = t.struct(
        {
            "resources": t.proxy(renames["ResourcesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FhirFilterOut"])
    types["EntityMentionIn"] = t.struct(
        {
            "type": t.string().optional(),
            "confidence": t.number().optional(),
            "linkedEntities": t.array(t.proxy(renames["LinkedEntityIn"])).optional(),
            "mentionId": t.string().optional(),
            "subject": t.proxy(renames["FeatureIn"]).optional(),
            "temporalAssessment": t.proxy(renames["FeatureIn"]).optional(),
            "text": t.proxy(renames["TextSpanIn"]).optional(),
            "certaintyAssessment": t.proxy(renames["FeatureIn"]).optional(),
        }
    ).named(renames["EntityMentionIn"])
    types["EntityMentionOut"] = t.struct(
        {
            "type": t.string().optional(),
            "confidence": t.number().optional(),
            "linkedEntities": t.array(t.proxy(renames["LinkedEntityOut"])).optional(),
            "mentionId": t.string().optional(),
            "subject": t.proxy(renames["FeatureOut"]).optional(),
            "temporalAssessment": t.proxy(renames["FeatureOut"]).optional(),
            "text": t.proxy(renames["TextSpanOut"]).optional(),
            "certaintyAssessment": t.proxy(renames["FeatureOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityMentionOut"])
    types["Hl7V2StoreIn"] = t.struct(
        {
            "name": t.string().optional(),
            "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
            "notificationConfigs": t.array(
                t.proxy(renames["Hl7V2NotificationConfigIn"])
            ).optional(),
            "rejectDuplicateMessage": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["Hl7V2StoreIn"])
    types["Hl7V2StoreOut"] = t.struct(
        {
            "name": t.string().optional(),
            "parserConfig": t.proxy(renames["ParserConfigOut"]).optional(),
            "notificationConfigs": t.array(
                t.proxy(renames["Hl7V2NotificationConfigOut"])
            ).optional(),
            "rejectDuplicateMessage": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Hl7V2StoreOut"])
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
    types["ArchiveUserDataMappingResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ArchiveUserDataMappingResponseIn"])
    types["ArchiveUserDataMappingResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ArchiveUserDataMappingResponseOut"])
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
    types["RedactConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RedactConfigIn"]
    )
    types["RedactConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RedactConfigOut"])
    types["GoogleCloudHealthcareV1FhirGcsDestinationIn"] = t.struct(
        {"uriPrefix": t.string().optional()}
    ).named(renames["GoogleCloudHealthcareV1FhirGcsDestinationIn"])
    types["GoogleCloudHealthcareV1FhirGcsDestinationOut"] = t.struct(
        {
            "uriPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudHealthcareV1FhirGcsDestinationOut"])
    types["EvaluateUserConsentsRequestIn"] = t.struct(
        {
            "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
            "pageToken": t.string().optional(),
            "userId": t.string(),
            "pageSize": t.integer().optional(),
            "consentList": t.proxy(renames["ConsentListIn"]).optional(),
            "responseView": t.string().optional(),
            "requestAttributes": t.struct({"_": t.string().optional()}),
        }
    ).named(renames["EvaluateUserConsentsRequestIn"])
    types["EvaluateUserConsentsRequestOut"] = t.struct(
        {
            "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
            "pageToken": t.string().optional(),
            "userId": t.string(),
            "pageSize": t.integer().optional(),
            "consentList": t.proxy(renames["ConsentListOut"]).optional(),
            "responseView": t.string().optional(),
            "requestAttributes": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EvaluateUserConsentsRequestOut"])
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
    types["ValidationConfigIn"] = t.struct(
        {
            "disableRequiredFieldValidation": t.boolean().optional(),
            "disableProfileValidation": t.boolean().optional(),
            "disableReferenceTypeValidation": t.boolean().optional(),
            "enabledImplementationGuides": t.array(t.string()).optional(),
            "disableFhirpathValidation": t.boolean().optional(),
        }
    ).named(renames["ValidationConfigIn"])
    types["ValidationConfigOut"] = t.struct(
        {
            "disableRequiredFieldValidation": t.boolean().optional(),
            "disableProfileValidation": t.boolean().optional(),
            "disableReferenceTypeValidation": t.boolean().optional(),
            "enabledImplementationGuides": t.array(t.string()).optional(),
            "disableFhirpathValidation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationConfigOut"])
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
            "nextPageToken": t.string().optional(),
            "consentArtifacts": t.array(
                t.proxy(renames["ConsentArtifactIn"])
            ).optional(),
        }
    ).named(renames["ListConsentArtifactsResponseIn"])
    types["ListConsentArtifactsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "consentArtifacts": t.array(
                t.proxy(renames["ConsentArtifactOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConsentArtifactsResponseOut"])
    types["RevokeConsentRequestIn"] = t.struct(
        {"consentArtifact": t.string().optional()}
    ).named(renames["RevokeConsentRequestIn"])
    types["RevokeConsentRequestOut"] = t.struct(
        {
            "consentArtifact": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevokeConsentRequestOut"])
    types["ActivateConsentRequestIn"] = t.struct(
        {
            "ttl": t.string().optional(),
            "consentArtifact": t.string(),
            "expireTime": t.string().optional(),
        }
    ).named(renames["ActivateConsentRequestIn"])
    types["ActivateConsentRequestOut"] = t.struct(
        {
            "ttl": t.string().optional(),
            "consentArtifact": t.string(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivateConsentRequestOut"])
    types["AnalyzeEntitiesResponseIn"] = t.struct(
        {
            "relationships": t.array(
                t.proxy(renames["EntityMentionRelationshipIn"])
            ).optional(),
            "entities": t.array(t.proxy(renames["EntityIn"])).optional(),
            "entityMentions": t.array(t.proxy(renames["EntityMentionIn"])).optional(),
        }
    ).named(renames["AnalyzeEntitiesResponseIn"])
    types["AnalyzeEntitiesResponseOut"] = t.struct(
        {
            "relationships": t.array(
                t.proxy(renames["EntityMentionRelationshipOut"])
            ).optional(),
            "entities": t.array(t.proxy(renames["EntityOut"])).optional(),
            "entityMentions": t.array(t.proxy(renames["EntityMentionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeEntitiesResponseOut"])
    types["SchematizedDataIn"] = t.struct(
        {"data": t.string().optional(), "error": t.string().optional()}
    ).named(renames["SchematizedDataIn"])
    types["SchematizedDataOut"] = t.struct(
        {
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchematizedDataOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["ExportMessagesRequestIn"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["ExportMessagesRequestIn"])
    types["ExportMessagesRequestOut"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportMessagesRequestOut"])
    types["TagFilterListIn"] = t.struct({"tags": t.array(t.string()).optional()}).named(
        renames["TagFilterListIn"]
    )
    types["TagFilterListOut"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagFilterListOut"])

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
    functions["projectsLocationsDatasetsSetIamPolicy"] = healthcare.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsGet"] = healthcare.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsGetIamPolicy"] = healthcare.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsList"] = healthcare.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDelete"] = healthcare.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsCreate"] = healthcare.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDeidentify"] = healthcare.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsPatch"] = healthcare.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsTestIamPermissions"] = healthcare.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresExport"] = healthcare.get(
        "v1/{parent}/fhirStores",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFhirStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsFhirStoresGetFHIRStoreMetrics"
    ] = healthcare.get(
        "v1/{parent}/fhirStores",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFhirStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresPatch"] = healthcare.get(
        "v1/{parent}/fhirStores",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFhirStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresImport"] = healthcare.get(
        "v1/{parent}/fhirStores",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFhirStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresGet"] = healthcare.get(
        "v1/{parent}/fhirStores",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFhirStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresGetIamPolicy"] = healthcare.get(
        "v1/{parent}/fhirStores",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFhirStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresDeidentify"] = healthcare.get(
        "v1/{parent}/fhirStores",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFhirStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresCreate"] = healthcare.get(
        "v1/{parent}/fhirStores",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFhirStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresSetIamPolicy"] = healthcare.get(
        "v1/{parent}/fhirStores",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFhirStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresTestIamPermissions"] = healthcare.get(
        "v1/{parent}/fhirStores",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFhirStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresDelete"] = healthcare.get(
        "v1/{parent}/fhirStores",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFhirStoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsFhirStoresList"] = healthcare.get(
        "v1/{parent}/fhirStores",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFhirStoresResponseOut"]),
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
    functions["projectsLocationsDatasetsFhirStoresFhirRead"] = healthcare.delete(
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
    functions[
        "projectsLocationsDatasetsFhirStoresFhirResource-validate"
    ] = healthcare.delete(
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
    functions[
        "projectsLocationsDatasetsFhirStoresFhirPatient-everything"
    ] = healthcare.delete(
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
    functions["projectsLocationsDatasetsFhirStoresFhirDelete"] = healthcare.delete(
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
        "projectsLocationsDatasetsFhirStoresFhirCapabilities"
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
    functions["projectsLocationsDatasetsFhirStoresFhirUpdate"] = healthcare.delete(
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
    functions[
        "projectsLocationsDatasetsFhirStoresFhirResource-purge"
    ] = healthcare.delete(
        "v1/{name}/$purge",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
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
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
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
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
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
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
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
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
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
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
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
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["Hl7V2StoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsHl7V2StoresSetIamPolicy"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
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
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
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
                "parserConfig": t.proxy(renames["ParserConfigIn"]).optional(),
                "notificationConfigs": t.array(
                    t.proxy(renames["Hl7V2NotificationConfigIn"])
                ).optional(),
                "rejectDuplicateMessage": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["Hl7V2StoreOut"]),
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
    functions["projectsLocationsDatasetsHl7V2StoresMessagesPatch"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsLocationsDatasetsHl7V2StoresMessagesIngest"] = healthcare.delete(
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
    functions["projectsLocationsDatasetsHl7V2StoresMessagesDelete"] = healthcare.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsOperationsCancel"] = healthcare.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresSetIamPolicy"] = healthcare.post(
        "v1/{consentStore}:evaluateUserConsents",
        t.struct(
            {
                "consentStore": t.string(),
                "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "userId": t.string(),
                "pageSize": t.integer().optional(),
                "consentList": t.proxy(renames["ConsentListIn"]).optional(),
                "responseView": t.string().optional(),
                "requestAttributes": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EvaluateUserConsentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresTestIamPermissions"
    ] = healthcare.post(
        "v1/{consentStore}:evaluateUserConsents",
        t.struct(
            {
                "consentStore": t.string(),
                "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "userId": t.string(),
                "pageSize": t.integer().optional(),
                "consentList": t.proxy(renames["ConsentListIn"]).optional(),
                "responseView": t.string().optional(),
                "requestAttributes": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EvaluateUserConsentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresCreate"] = healthcare.post(
        "v1/{consentStore}:evaluateUserConsents",
        t.struct(
            {
                "consentStore": t.string(),
                "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "userId": t.string(),
                "pageSize": t.integer().optional(),
                "consentList": t.proxy(renames["ConsentListIn"]).optional(),
                "responseView": t.string().optional(),
                "requestAttributes": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EvaluateUserConsentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresGetIamPolicy"] = healthcare.post(
        "v1/{consentStore}:evaluateUserConsents",
        t.struct(
            {
                "consentStore": t.string(),
                "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "userId": t.string(),
                "pageSize": t.integer().optional(),
                "consentList": t.proxy(renames["ConsentListIn"]).optional(),
                "responseView": t.string().optional(),
                "requestAttributes": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EvaluateUserConsentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresGet"] = healthcare.post(
        "v1/{consentStore}:evaluateUserConsents",
        t.struct(
            {
                "consentStore": t.string(),
                "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "userId": t.string(),
                "pageSize": t.integer().optional(),
                "consentList": t.proxy(renames["ConsentListIn"]).optional(),
                "responseView": t.string().optional(),
                "requestAttributes": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EvaluateUserConsentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresCheckDataAccess"
    ] = healthcare.post(
        "v1/{consentStore}:evaluateUserConsents",
        t.struct(
            {
                "consentStore": t.string(),
                "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "userId": t.string(),
                "pageSize": t.integer().optional(),
                "consentList": t.proxy(renames["ConsentListIn"]).optional(),
                "responseView": t.string().optional(),
                "requestAttributes": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EvaluateUserConsentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresDelete"] = healthcare.post(
        "v1/{consentStore}:evaluateUserConsents",
        t.struct(
            {
                "consentStore": t.string(),
                "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "userId": t.string(),
                "pageSize": t.integer().optional(),
                "consentList": t.proxy(renames["ConsentListIn"]).optional(),
                "responseView": t.string().optional(),
                "requestAttributes": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EvaluateUserConsentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresList"] = healthcare.post(
        "v1/{consentStore}:evaluateUserConsents",
        t.struct(
            {
                "consentStore": t.string(),
                "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "userId": t.string(),
                "pageSize": t.integer().optional(),
                "consentList": t.proxy(renames["ConsentListIn"]).optional(),
                "responseView": t.string().optional(),
                "requestAttributes": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EvaluateUserConsentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresPatch"] = healthcare.post(
        "v1/{consentStore}:evaluateUserConsents",
        t.struct(
            {
                "consentStore": t.string(),
                "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "userId": t.string(),
                "pageSize": t.integer().optional(),
                "consentList": t.proxy(renames["ConsentListIn"]).optional(),
                "responseView": t.string().optional(),
                "requestAttributes": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EvaluateUserConsentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresQueryAccessibleData"
    ] = healthcare.post(
        "v1/{consentStore}:evaluateUserConsents",
        t.struct(
            {
                "consentStore": t.string(),
                "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "userId": t.string(),
                "pageSize": t.integer().optional(),
                "consentList": t.proxy(renames["ConsentListIn"]).optional(),
                "responseView": t.string().optional(),
                "requestAttributes": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EvaluateUserConsentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresEvaluateUserConsents"
    ] = healthcare.post(
        "v1/{consentStore}:evaluateUserConsents",
        t.struct(
            {
                "consentStore": t.string(),
                "resourceAttributes": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "userId": t.string(),
                "pageSize": t.integer().optional(),
                "consentList": t.proxy(renames["ConsentListIn"]).optional(),
                "responseView": t.string().optional(),
                "requestAttributes": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EvaluateUserConsentsResponseOut"]),
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
                "category": t.string(),
                "allowedValues": t.array(t.string()),
                "consentDefaultValues": t.array(t.string()).optional(),
                "dataMappingDefaultValue": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttributeDefinitionOut"]),
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
                "category": t.string(),
                "allowedValues": t.array(t.string()),
                "consentDefaultValues": t.array(t.string()).optional(),
                "dataMappingDefaultValue": t.string().optional(),
                "description": t.string().optional(),
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
                "category": t.string(),
                "allowedValues": t.array(t.string()),
                "consentDefaultValues": t.array(t.string()).optional(),
                "dataMappingDefaultValue": t.string().optional(),
                "description": t.string().optional(),
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
                "category": t.string(),
                "allowedValues": t.array(t.string()),
                "consentDefaultValues": t.array(t.string()).optional(),
                "dataMappingDefaultValue": t.string().optional(),
                "description": t.string().optional(),
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
                "category": t.string(),
                "allowedValues": t.array(t.string()),
                "consentDefaultValues": t.array(t.string()).optional(),
                "dataMappingDefaultValue": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttributeDefinitionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsReject"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "state": t.string(),
                "policies": t.array(
                    t.proxy(renames["GoogleCloudHealthcareV1ConsentPolicyIn"])
                ).optional(),
                "userId": t.string(),
                "expireTime": t.string().optional(),
                "consentArtifact": t.string(),
                "ttl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsList"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "state": t.string(),
                "policies": t.array(
                    t.proxy(renames["GoogleCloudHealthcareV1ConsentPolicyIn"])
                ).optional(),
                "userId": t.string(),
                "expireTime": t.string().optional(),
                "consentArtifact": t.string(),
                "ttl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsGet"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "state": t.string(),
                "policies": t.array(
                    t.proxy(renames["GoogleCloudHealthcareV1ConsentPolicyIn"])
                ).optional(),
                "userId": t.string(),
                "expireTime": t.string().optional(),
                "consentArtifact": t.string(),
                "ttl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsActivate"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "state": t.string(),
                "policies": t.array(
                    t.proxy(renames["GoogleCloudHealthcareV1ConsentPolicyIn"])
                ).optional(),
                "userId": t.string(),
                "expireTime": t.string().optional(),
                "consentArtifact": t.string(),
                "ttl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsDeleteRevision"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "state": t.string(),
                "policies": t.array(
                    t.proxy(renames["GoogleCloudHealthcareV1ConsentPolicyIn"])
                ).optional(),
                "userId": t.string(),
                "expireTime": t.string().optional(),
                "consentArtifact": t.string(),
                "ttl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsListRevisions"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "state": t.string(),
                "policies": t.array(
                    t.proxy(renames["GoogleCloudHealthcareV1ConsentPolicyIn"])
                ).optional(),
                "userId": t.string(),
                "expireTime": t.string().optional(),
                "consentArtifact": t.string(),
                "ttl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsCreate"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "state": t.string(),
                "policies": t.array(
                    t.proxy(renames["GoogleCloudHealthcareV1ConsentPolicyIn"])
                ).optional(),
                "userId": t.string(),
                "expireTime": t.string().optional(),
                "consentArtifact": t.string(),
                "ttl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsRevoke"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "state": t.string(),
                "policies": t.array(
                    t.proxy(renames["GoogleCloudHealthcareV1ConsentPolicyIn"])
                ).optional(),
                "userId": t.string(),
                "expireTime": t.string().optional(),
                "consentArtifact": t.string(),
                "ttl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresConsentsDelete"
    ] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "state": t.string(),
                "policies": t.array(
                    t.proxy(renames["GoogleCloudHealthcareV1ConsentPolicyIn"])
                ).optional(),
                "userId": t.string(),
                "expireTime": t.string().optional(),
                "consentArtifact": t.string(),
                "ttl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsConsentStoresConsentsPatch"] = healthcare.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "state": t.string(),
                "policies": t.array(
                    t.proxy(renames["GoogleCloudHealthcareV1ConsentPolicyIn"])
                ).optional(),
                "userId": t.string(),
                "expireTime": t.string().optional(),
                "consentArtifact": t.string(),
                "ttl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsList"
    ] = healthcare.post(
        "v1/{parent}/userDataMappings",
        t.struct(
            {
                "parent": t.string(),
                "userId": t.string(),
                "dataId": t.string(),
                "resourceAttributes": t.array(
                    t.proxy(renames["AttributeIn"])
                ).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserDataMappingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsDelete"
    ] = healthcare.post(
        "v1/{parent}/userDataMappings",
        t.struct(
            {
                "parent": t.string(),
                "userId": t.string(),
                "dataId": t.string(),
                "resourceAttributes": t.array(
                    t.proxy(renames["AttributeIn"])
                ).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserDataMappingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsPatch"
    ] = healthcare.post(
        "v1/{parent}/userDataMappings",
        t.struct(
            {
                "parent": t.string(),
                "userId": t.string(),
                "dataId": t.string(),
                "resourceAttributes": t.array(
                    t.proxy(renames["AttributeIn"])
                ).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserDataMappingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsGet"
    ] = healthcare.post(
        "v1/{parent}/userDataMappings",
        t.struct(
            {
                "parent": t.string(),
                "userId": t.string(),
                "dataId": t.string(),
                "resourceAttributes": t.array(
                    t.proxy(renames["AttributeIn"])
                ).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserDataMappingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsArchive"
    ] = healthcare.post(
        "v1/{parent}/userDataMappings",
        t.struct(
            {
                "parent": t.string(),
                "userId": t.string(),
                "dataId": t.string(),
                "resourceAttributes": t.array(
                    t.proxy(renames["AttributeIn"])
                ).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserDataMappingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDatasetsConsentStoresUserDataMappingsCreate"
    ] = healthcare.post(
        "v1/{parent}/userDataMappings",
        t.struct(
            {
                "parent": t.string(),
                "userId": t.string(),
                "dataId": t.string(),
                "resourceAttributes": t.array(
                    t.proxy(renames["AttributeIn"])
                ).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserDataMappingOut"]),
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
        "projectsLocationsDatasetsConsentStoresConsentArtifactsCreate"
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
        "projectsLocationsDatasetsConsentStoresConsentArtifactsGet"
    ] = healthcare.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConsentArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDatasetsDicomStoresDelete"] = healthcare.get(
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
        "projectsLocationsDatasetsDicomStoresTestIamPermissions"
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
    functions["projectsLocationsDatasetsDicomStoresExport"] = healthcare.get(
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
    functions["projectsLocationsDatasetsDicomStoresGetIamPolicy"] = healthcare.get(
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
    functions["projectsLocationsDatasetsDicomStoresGet"] = healthcare.get(
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
    functions["projectsLocationsDatasetsDicomStoresImport"] = healthcare.get(
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
    functions["projectsLocationsDatasetsDicomStoresCreate"] = healthcare.get(
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
        "projectsLocationsDatasetsDicomStoresSearchForInstances"
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
    functions["projectsLocationsDatasetsDicomStoresSearchForSeries"] = healthcare.get(
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
    functions["projectsLocationsDatasetsDicomStoresStoreInstances"] = healthcare.get(
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
    functions["projectsLocationsDatasetsDicomStoresSetIamPolicy"] = healthcare.get(
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
    functions["projectsLocationsDatasetsDicomStoresPatch"] = healthcare.get(
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
    functions["projectsLocationsDatasetsDicomStoresList"] = healthcare.get(
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
    functions["projectsLocationsDatasetsDicomStoresDeidentify"] = healthcare.get(
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
    functions["projectsLocationsDatasetsDicomStoresSearchForStudies"] = healthcare.get(
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
        "projectsLocationsDatasetsDicomStoresStudiesSeriesSearchForInstances"
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
        "projectsLocationsDatasetsDicomStoresStudiesSeriesDelete"
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
        "projectsLocationsDatasetsDicomStoresStudiesSeriesRetrieveSeries"
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
        importer="healthcare", renames=renames, types=types, functions=functions
    )
