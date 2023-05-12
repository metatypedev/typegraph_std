from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_datacatalog() -> Import:
    datacatalog = HTTPRuntime("https://datacatalog.googleapis.com/")

    renames = {
        "ErrorResponse": "_datacatalog_1_ErrorResponse",
        "GoogleCloudDatacatalogV1ContactsPersonIn": "_datacatalog_2_GoogleCloudDatacatalogV1ContactsPersonIn",
        "GoogleCloudDatacatalogV1ContactsPersonOut": "_datacatalog_3_GoogleCloudDatacatalogV1ContactsPersonOut",
        "GoogleCloudDatacatalogV1StoragePropertiesIn": "_datacatalog_4_GoogleCloudDatacatalogV1StoragePropertiesIn",
        "GoogleCloudDatacatalogV1StoragePropertiesOut": "_datacatalog_5_GoogleCloudDatacatalogV1StoragePropertiesOut",
        "GoogleCloudDatacatalogV1ViewSpecIn": "_datacatalog_6_GoogleCloudDatacatalogV1ViewSpecIn",
        "GoogleCloudDatacatalogV1ViewSpecOut": "_datacatalog_7_GoogleCloudDatacatalogV1ViewSpecOut",
        "GoogleCloudDatacatalogV1ImportEntriesResponseIn": "_datacatalog_8_GoogleCloudDatacatalogV1ImportEntriesResponseIn",
        "GoogleCloudDatacatalogV1ImportEntriesResponseOut": "_datacatalog_9_GoogleCloudDatacatalogV1ImportEntriesResponseOut",
        "GoogleCloudDatacatalogV1SchemaIn": "_datacatalog_10_GoogleCloudDatacatalogV1SchemaIn",
        "GoogleCloudDatacatalogV1SchemaOut": "_datacatalog_11_GoogleCloudDatacatalogV1SchemaOut",
        "GoogleCloudDatacatalogV1SearchCatalogResponseIn": "_datacatalog_12_GoogleCloudDatacatalogV1SearchCatalogResponseIn",
        "GoogleCloudDatacatalogV1SearchCatalogResponseOut": "_datacatalog_13_GoogleCloudDatacatalogV1SearchCatalogResponseOut",
        "GoogleCloudDatacatalogV1GcsFilesetSpecIn": "_datacatalog_14_GoogleCloudDatacatalogV1GcsFilesetSpecIn",
        "GoogleCloudDatacatalogV1GcsFilesetSpecOut": "_datacatalog_15_GoogleCloudDatacatalogV1GcsFilesetSpecOut",
        "GoogleCloudDatacatalogV1ListTaxonomiesResponseIn": "_datacatalog_16_GoogleCloudDatacatalogV1ListTaxonomiesResponseIn",
        "GoogleCloudDatacatalogV1ListTaxonomiesResponseOut": "_datacatalog_17_GoogleCloudDatacatalogV1ListTaxonomiesResponseOut",
        "GoogleCloudDatacatalogV1ReconcileTagsResponseIn": "_datacatalog_18_GoogleCloudDatacatalogV1ReconcileTagsResponseIn",
        "GoogleCloudDatacatalogV1ReconcileTagsResponseOut": "_datacatalog_19_GoogleCloudDatacatalogV1ReconcileTagsResponseOut",
        "GoogleCloudDatacatalogV1ListTagsResponseIn": "_datacatalog_20_GoogleCloudDatacatalogV1ListTagsResponseIn",
        "GoogleCloudDatacatalogV1ListTagsResponseOut": "_datacatalog_21_GoogleCloudDatacatalogV1ListTagsResponseOut",
        "GoogleCloudDatacatalogV1GcsFileSpecIn": "_datacatalog_22_GoogleCloudDatacatalogV1GcsFileSpecIn",
        "GoogleCloudDatacatalogV1GcsFileSpecOut": "_datacatalog_23_GoogleCloudDatacatalogV1GcsFileSpecOut",
        "GoogleCloudDatacatalogV1ColumnSchemaIn": "_datacatalog_24_GoogleCloudDatacatalogV1ColumnSchemaIn",
        "GoogleCloudDatacatalogV1ColumnSchemaOut": "_datacatalog_25_GoogleCloudDatacatalogV1ColumnSchemaOut",
        "GoogleCloudDatacatalogV1EntryOverviewIn": "_datacatalog_26_GoogleCloudDatacatalogV1EntryOverviewIn",
        "GoogleCloudDatacatalogV1EntryOverviewOut": "_datacatalog_27_GoogleCloudDatacatalogV1EntryOverviewOut",
        "StatusIn": "_datacatalog_28_StatusIn",
        "StatusOut": "_datacatalog_29_StatusOut",
        "GoogleCloudDatacatalogV1ReconcileTagsRequestIn": "_datacatalog_30_GoogleCloudDatacatalogV1ReconcileTagsRequestIn",
        "GoogleCloudDatacatalogV1ReconcileTagsRequestOut": "_datacatalog_31_GoogleCloudDatacatalogV1ReconcileTagsRequestOut",
        "GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn": "_datacatalog_32_GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn",
        "GoogleCloudDatacatalogV1CloudBigtableSystemSpecOut": "_datacatalog_33_GoogleCloudDatacatalogV1CloudBigtableSystemSpecOut",
        "GoogleCloudDatacatalogV1DataplexFilesetSpecIn": "_datacatalog_34_GoogleCloudDatacatalogV1DataplexFilesetSpecIn",
        "GoogleCloudDatacatalogV1DataplexFilesetSpecOut": "_datacatalog_35_GoogleCloudDatacatalogV1DataplexFilesetSpecOut",
        "GoogleCloudDatacatalogV1DumpItemIn": "_datacatalog_36_GoogleCloudDatacatalogV1DumpItemIn",
        "GoogleCloudDatacatalogV1DumpItemOut": "_datacatalog_37_GoogleCloudDatacatalogV1DumpItemOut",
        "GoogleCloudDatacatalogV1ReplaceTaxonomyRequestIn": "_datacatalog_38_GoogleCloudDatacatalogV1ReplaceTaxonomyRequestIn",
        "GoogleCloudDatacatalogV1ReplaceTaxonomyRequestOut": "_datacatalog_39_GoogleCloudDatacatalogV1ReplaceTaxonomyRequestOut",
        "GoogleCloudDatacatalogV1UsageSignalIn": "_datacatalog_40_GoogleCloudDatacatalogV1UsageSignalIn",
        "GoogleCloudDatacatalogV1UsageSignalOut": "_datacatalog_41_GoogleCloudDatacatalogV1UsageSignalOut",
        "GoogleCloudDatacatalogV1ReconcileTagsMetadataIn": "_datacatalog_42_GoogleCloudDatacatalogV1ReconcileTagsMetadataIn",
        "GoogleCloudDatacatalogV1ReconcileTagsMetadataOut": "_datacatalog_43_GoogleCloudDatacatalogV1ReconcileTagsMetadataOut",
        "GoogleCloudDatacatalogV1ServiceSpecIn": "_datacatalog_44_GoogleCloudDatacatalogV1ServiceSpecIn",
        "GoogleCloudDatacatalogV1ServiceSpecOut": "_datacatalog_45_GoogleCloudDatacatalogV1ServiceSpecOut",
        "GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueIn": "_datacatalog_46_GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueIn",
        "GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueOut": "_datacatalog_47_GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueOut",
        "GoogleCloudDatacatalogV1ListEntryGroupsResponseIn": "_datacatalog_48_GoogleCloudDatacatalogV1ListEntryGroupsResponseIn",
        "GoogleCloudDatacatalogV1ListEntryGroupsResponseOut": "_datacatalog_49_GoogleCloudDatacatalogV1ListEntryGroupsResponseOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaIn": "_datacatalog_50_GoogleCloudDatacatalogV1PhysicalSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaOut": "_datacatalog_51_GoogleCloudDatacatalogV1PhysicalSchemaOut",
        "GoogleCloudDatacatalogV1DataplexTableSpecIn": "_datacatalog_52_GoogleCloudDatacatalogV1DataplexTableSpecIn",
        "GoogleCloudDatacatalogV1DataplexTableSpecOut": "_datacatalog_53_GoogleCloudDatacatalogV1DataplexTableSpecOut",
        "GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequestIn": "_datacatalog_54_GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequestIn",
        "GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequestOut": "_datacatalog_55_GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequestOut",
        "GoogleCloudDatacatalogV1ExportTaxonomiesResponseIn": "_datacatalog_56_GoogleCloudDatacatalogV1ExportTaxonomiesResponseIn",
        "GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut": "_datacatalog_57_GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut",
        "GetIamPolicyRequestIn": "_datacatalog_58_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_datacatalog_59_GetIamPolicyRequestOut",
        "GoogleCloudDatacatalogV1SearchCatalogResultIn": "_datacatalog_60_GoogleCloudDatacatalogV1SearchCatalogResultIn",
        "GoogleCloudDatacatalogV1SearchCatalogResultOut": "_datacatalog_61_GoogleCloudDatacatalogV1SearchCatalogResultOut",
        "GoogleCloudDatacatalogV1TagTemplateIn": "_datacatalog_62_GoogleCloudDatacatalogV1TagTemplateIn",
        "GoogleCloudDatacatalogV1TagTemplateOut": "_datacatalog_63_GoogleCloudDatacatalogV1TagTemplateOut",
        "TestIamPermissionsResponseIn": "_datacatalog_64_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_datacatalog_65_TestIamPermissionsResponseOut",
        "GetPolicyOptionsIn": "_datacatalog_66_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_datacatalog_67_GetPolicyOptionsOut",
        "GoogleCloudDatacatalogV1UnstarEntryRequestIn": "_datacatalog_68_GoogleCloudDatacatalogV1UnstarEntryRequestIn",
        "GoogleCloudDatacatalogV1UnstarEntryRequestOut": "_datacatalog_69_GoogleCloudDatacatalogV1UnstarEntryRequestOut",
        "GoogleCloudDatacatalogV1EntryGroupIn": "_datacatalog_70_GoogleCloudDatacatalogV1EntryGroupIn",
        "GoogleCloudDatacatalogV1EntryGroupOut": "_datacatalog_71_GoogleCloudDatacatalogV1EntryGroupOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaIn": "_datacatalog_72_GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaOut": "_datacatalog_73_GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaOut",
        "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecIn": "_datacatalog_74_GoogleCloudDatacatalogV1CloudBigtableInstanceSpecIn",
        "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecOut": "_datacatalog_75_GoogleCloudDatacatalogV1CloudBigtableInstanceSpecOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaIn": "_datacatalog_76_GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaOut": "_datacatalog_77_GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaOut",
        "GoogleCloudDatacatalogV1BigQueryTableSpecIn": "_datacatalog_78_GoogleCloudDatacatalogV1BigQueryTableSpecIn",
        "GoogleCloudDatacatalogV1BigQueryTableSpecOut": "_datacatalog_79_GoogleCloudDatacatalogV1BigQueryTableSpecOut",
        "GoogleCloudDatacatalogV1SerializedTaxonomyIn": "_datacatalog_80_GoogleCloudDatacatalogV1SerializedTaxonomyIn",
        "GoogleCloudDatacatalogV1SerializedTaxonomyOut": "_datacatalog_81_GoogleCloudDatacatalogV1SerializedTaxonomyOut",
        "GoogleCloudDatacatalogV1TaggedEntryIn": "_datacatalog_82_GoogleCloudDatacatalogV1TaggedEntryIn",
        "GoogleCloudDatacatalogV1TaggedEntryOut": "_datacatalog_83_GoogleCloudDatacatalogV1TaggedEntryOut",
        "GoogleCloudDatacatalogV1FieldTypeIn": "_datacatalog_84_GoogleCloudDatacatalogV1FieldTypeIn",
        "GoogleCloudDatacatalogV1FieldTypeOut": "_datacatalog_85_GoogleCloudDatacatalogV1FieldTypeOut",
        "GoogleCloudDatacatalogV1EntryIn": "_datacatalog_86_GoogleCloudDatacatalogV1EntryIn",
        "GoogleCloudDatacatalogV1EntryOut": "_datacatalog_87_GoogleCloudDatacatalogV1EntryOut",
        "GoogleCloudDatacatalogV1TagTemplateFieldIn": "_datacatalog_88_GoogleCloudDatacatalogV1TagTemplateFieldIn",
        "GoogleCloudDatacatalogV1TagTemplateFieldOut": "_datacatalog_89_GoogleCloudDatacatalogV1TagTemplateFieldOut",
        "GoogleCloudDatacatalogV1TagIn": "_datacatalog_90_GoogleCloudDatacatalogV1TagIn",
        "GoogleCloudDatacatalogV1TagOut": "_datacatalog_91_GoogleCloudDatacatalogV1TagOut",
        "GoogleCloudDatacatalogV1FieldTypeEnumTypeIn": "_datacatalog_92_GoogleCloudDatacatalogV1FieldTypeEnumTypeIn",
        "GoogleCloudDatacatalogV1FieldTypeEnumTypeOut": "_datacatalog_93_GoogleCloudDatacatalogV1FieldTypeEnumTypeOut",
        "GoogleCloudDatacatalogV1ListPolicyTagsResponseIn": "_datacatalog_94_GoogleCloudDatacatalogV1ListPolicyTagsResponseIn",
        "GoogleCloudDatacatalogV1ListPolicyTagsResponseOut": "_datacatalog_95_GoogleCloudDatacatalogV1ListPolicyTagsResponseOut",
        "GoogleCloudDatacatalogV1StarEntryRequestIn": "_datacatalog_96_GoogleCloudDatacatalogV1StarEntryRequestIn",
        "GoogleCloudDatacatalogV1StarEntryRequestOut": "_datacatalog_97_GoogleCloudDatacatalogV1StarEntryRequestOut",
        "GoogleCloudDatacatalogV1PolicyTagIn": "_datacatalog_98_GoogleCloudDatacatalogV1PolicyTagIn",
        "GoogleCloudDatacatalogV1PolicyTagOut": "_datacatalog_99_GoogleCloudDatacatalogV1PolicyTagOut",
        "GoogleCloudDatacatalogV1SerializedPolicyTagIn": "_datacatalog_100_GoogleCloudDatacatalogV1SerializedPolicyTagIn",
        "GoogleCloudDatacatalogV1SerializedPolicyTagOut": "_datacatalog_101_GoogleCloudDatacatalogV1SerializedPolicyTagOut",
        "GoogleCloudDatacatalogV1DataplexExternalTableIn": "_datacatalog_102_GoogleCloudDatacatalogV1DataplexExternalTableIn",
        "GoogleCloudDatacatalogV1DataplexExternalTableOut": "_datacatalog_103_GoogleCloudDatacatalogV1DataplexExternalTableOut",
        "GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecIn": "_datacatalog_104_GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecIn",
        "GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecOut": "_datacatalog_105_GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecOut",
        "GoogleCloudDatacatalogV1UnstarEntryResponseIn": "_datacatalog_106_GoogleCloudDatacatalogV1UnstarEntryResponseIn",
        "GoogleCloudDatacatalogV1UnstarEntryResponseOut": "_datacatalog_107_GoogleCloudDatacatalogV1UnstarEntryResponseOut",
        "GoogleCloudDatacatalogV1DataplexSpecIn": "_datacatalog_108_GoogleCloudDatacatalogV1DataplexSpecIn",
        "GoogleCloudDatacatalogV1DataplexSpecOut": "_datacatalog_109_GoogleCloudDatacatalogV1DataplexSpecOut",
        "GoogleCloudDatacatalogV1TableSpecIn": "_datacatalog_110_GoogleCloudDatacatalogV1TableSpecIn",
        "GoogleCloudDatacatalogV1TableSpecOut": "_datacatalog_111_GoogleCloudDatacatalogV1TableSpecOut",
        "GoogleCloudDatacatalogV1ImportEntriesRequestIn": "_datacatalog_112_GoogleCloudDatacatalogV1ImportEntriesRequestIn",
        "GoogleCloudDatacatalogV1ImportEntriesRequestOut": "_datacatalog_113_GoogleCloudDatacatalogV1ImportEntriesRequestOut",
        "GoogleCloudDatacatalogV1DataSourceIn": "_datacatalog_114_GoogleCloudDatacatalogV1DataSourceIn",
        "GoogleCloudDatacatalogV1DataSourceOut": "_datacatalog_115_GoogleCloudDatacatalogV1DataSourceOut",
        "ListOperationsResponseIn": "_datacatalog_116_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_datacatalog_117_ListOperationsResponseOut",
        "ExprIn": "_datacatalog_118_ExprIn",
        "ExprOut": "_datacatalog_119_ExprOut",
        "GoogleCloudDatacatalogV1ContactsIn": "_datacatalog_120_GoogleCloudDatacatalogV1ContactsIn",
        "GoogleCloudDatacatalogV1ContactsOut": "_datacatalog_121_GoogleCloudDatacatalogV1ContactsOut",
        "GoogleCloudDatacatalogV1TaxonomyServiceIn": "_datacatalog_122_GoogleCloudDatacatalogV1TaxonomyServiceIn",
        "GoogleCloudDatacatalogV1TaxonomyServiceOut": "_datacatalog_123_GoogleCloudDatacatalogV1TaxonomyServiceOut",
        "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecIn": "_datacatalog_124_GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecIn",
        "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecOut": "_datacatalog_125_GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecOut",
        "GoogleCloudDatacatalogV1InlineSourceIn": "_datacatalog_126_GoogleCloudDatacatalogV1InlineSourceIn",
        "GoogleCloudDatacatalogV1InlineSourceOut": "_datacatalog_127_GoogleCloudDatacatalogV1InlineSourceOut",
        "GoogleCloudDatacatalogV1SearchCatalogRequestScopeIn": "_datacatalog_128_GoogleCloudDatacatalogV1SearchCatalogRequestScopeIn",
        "GoogleCloudDatacatalogV1SearchCatalogRequestScopeOut": "_datacatalog_129_GoogleCloudDatacatalogV1SearchCatalogRequestScopeOut",
        "GoogleCloudDatacatalogV1LookerSystemSpecIn": "_datacatalog_130_GoogleCloudDatacatalogV1LookerSystemSpecIn",
        "GoogleCloudDatacatalogV1LookerSystemSpecOut": "_datacatalog_131_GoogleCloudDatacatalogV1LookerSystemSpecOut",
        "SetIamPolicyRequestIn": "_datacatalog_132_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_datacatalog_133_SetIamPolicyRequestOut",
        "GoogleCloudDatacatalogV1ListEntriesResponseIn": "_datacatalog_134_GoogleCloudDatacatalogV1ListEntriesResponseIn",
        "GoogleCloudDatacatalogV1ListEntriesResponseOut": "_datacatalog_135_GoogleCloudDatacatalogV1ListEntriesResponseOut",
        "OperationIn": "_datacatalog_136_OperationIn",
        "OperationOut": "_datacatalog_137_OperationOut",
        "GoogleCloudDatacatalogV1SystemTimestampsIn": "_datacatalog_138_GoogleCloudDatacatalogV1SystemTimestampsIn",
        "GoogleCloudDatacatalogV1SystemTimestampsOut": "_datacatalog_139_GoogleCloudDatacatalogV1SystemTimestampsOut",
        "GoogleCloudDatacatalogV1RoutineSpecArgumentIn": "_datacatalog_140_GoogleCloudDatacatalogV1RoutineSpecArgumentIn",
        "GoogleCloudDatacatalogV1RoutineSpecArgumentOut": "_datacatalog_141_GoogleCloudDatacatalogV1RoutineSpecArgumentOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaIn": "_datacatalog_142_GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaOut": "_datacatalog_143_GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaOut",
        "GoogleCloudDatacatalogV1SearchCatalogRequestIn": "_datacatalog_144_GoogleCloudDatacatalogV1SearchCatalogRequestIn",
        "GoogleCloudDatacatalogV1SearchCatalogRequestOut": "_datacatalog_145_GoogleCloudDatacatalogV1SearchCatalogRequestOut",
        "GoogleCloudDatacatalogV1BigQueryDateShardedSpecIn": "_datacatalog_146_GoogleCloudDatacatalogV1BigQueryDateShardedSpecIn",
        "GoogleCloudDatacatalogV1BigQueryDateShardedSpecOut": "_datacatalog_147_GoogleCloudDatacatalogV1BigQueryDateShardedSpecOut",
        "GoogleCloudDatacatalogV1StarEntryResponseIn": "_datacatalog_148_GoogleCloudDatacatalogV1StarEntryResponseIn",
        "GoogleCloudDatacatalogV1StarEntryResponseOut": "_datacatalog_149_GoogleCloudDatacatalogV1StarEntryResponseOut",
        "GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn": "_datacatalog_150_GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn",
        "GoogleCloudDatacatalogV1SqlDatabaseSystemSpecOut": "_datacatalog_151_GoogleCloudDatacatalogV1SqlDatabaseSystemSpecOut",
        "GoogleCloudDatacatalogV1BusinessContextIn": "_datacatalog_152_GoogleCloudDatacatalogV1BusinessContextIn",
        "GoogleCloudDatacatalogV1BusinessContextOut": "_datacatalog_153_GoogleCloudDatacatalogV1BusinessContextOut",
        "GoogleCloudDatacatalogV1FilesetSpecIn": "_datacatalog_154_GoogleCloudDatacatalogV1FilesetSpecIn",
        "GoogleCloudDatacatalogV1FilesetSpecOut": "_datacatalog_155_GoogleCloudDatacatalogV1FilesetSpecOut",
        "GoogleCloudDatacatalogV1TagFieldEnumValueIn": "_datacatalog_156_GoogleCloudDatacatalogV1TagFieldEnumValueIn",
        "GoogleCloudDatacatalogV1TagFieldEnumValueOut": "_datacatalog_157_GoogleCloudDatacatalogV1TagFieldEnumValueOut",
        "GoogleCloudDatacatalogV1RoutineSpecIn": "_datacatalog_158_GoogleCloudDatacatalogV1RoutineSpecIn",
        "GoogleCloudDatacatalogV1RoutineSpecOut": "_datacatalog_159_GoogleCloudDatacatalogV1RoutineSpecOut",
        "GoogleCloudDatacatalogV1ImportTaxonomiesRequestIn": "_datacatalog_160_GoogleCloudDatacatalogV1ImportTaxonomiesRequestIn",
        "GoogleCloudDatacatalogV1ImportTaxonomiesRequestOut": "_datacatalog_161_GoogleCloudDatacatalogV1ImportTaxonomiesRequestOut",
        "GoogleCloudDatacatalogV1DatabaseTableSpecIn": "_datacatalog_162_GoogleCloudDatacatalogV1DatabaseTableSpecIn",
        "GoogleCloudDatacatalogV1DatabaseTableSpecOut": "_datacatalog_163_GoogleCloudDatacatalogV1DatabaseTableSpecOut",
        "GoogleCloudDatacatalogV1CrossRegionalSourceIn": "_datacatalog_164_GoogleCloudDatacatalogV1CrossRegionalSourceIn",
        "GoogleCloudDatacatalogV1CrossRegionalSourceOut": "_datacatalog_165_GoogleCloudDatacatalogV1CrossRegionalSourceOut",
        "GoogleCloudDatacatalogV1UsageStatsIn": "_datacatalog_166_GoogleCloudDatacatalogV1UsageStatsIn",
        "GoogleCloudDatacatalogV1UsageStatsOut": "_datacatalog_167_GoogleCloudDatacatalogV1UsageStatsOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaIn": "_datacatalog_168_GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaOut": "_datacatalog_169_GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaOut",
        "GoogleCloudDatacatalogV1ImportEntriesMetadataIn": "_datacatalog_170_GoogleCloudDatacatalogV1ImportEntriesMetadataIn",
        "GoogleCloudDatacatalogV1ImportEntriesMetadataOut": "_datacatalog_171_GoogleCloudDatacatalogV1ImportEntriesMetadataOut",
        "EmptyIn": "_datacatalog_172_EmptyIn",
        "EmptyOut": "_datacatalog_173_EmptyOut",
        "GoogleCloudDatacatalogV1ModifyEntryOverviewRequestIn": "_datacatalog_174_GoogleCloudDatacatalogV1ModifyEntryOverviewRequestIn",
        "GoogleCloudDatacatalogV1ModifyEntryOverviewRequestOut": "_datacatalog_175_GoogleCloudDatacatalogV1ModifyEntryOverviewRequestOut",
        "GoogleCloudDatacatalogV1ModifyEntryContactsRequestIn": "_datacatalog_176_GoogleCloudDatacatalogV1ModifyEntryContactsRequestIn",
        "GoogleCloudDatacatalogV1ModifyEntryContactsRequestOut": "_datacatalog_177_GoogleCloudDatacatalogV1ModifyEntryContactsRequestOut",
        "GoogleCloudDatacatalogV1TaxonomyIn": "_datacatalog_178_GoogleCloudDatacatalogV1TaxonomyIn",
        "GoogleCloudDatacatalogV1TaxonomyOut": "_datacatalog_179_GoogleCloudDatacatalogV1TaxonomyOut",
        "GoogleCloudDatacatalogV1ImportTaxonomiesResponseIn": "_datacatalog_180_GoogleCloudDatacatalogV1ImportTaxonomiesResponseIn",
        "GoogleCloudDatacatalogV1ImportTaxonomiesResponseOut": "_datacatalog_181_GoogleCloudDatacatalogV1ImportTaxonomiesResponseOut",
        "TestIamPermissionsRequestIn": "_datacatalog_182_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_datacatalog_183_TestIamPermissionsRequestOut",
        "PolicyIn": "_datacatalog_184_PolicyIn",
        "PolicyOut": "_datacatalog_185_PolicyOut",
        "GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestIn": "_datacatalog_186_GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestIn",
        "GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestOut": "_datacatalog_187_GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestOut",
        "GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecIn": "_datacatalog_188_GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecIn",
        "GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecOut": "_datacatalog_189_GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecOut",
        "GoogleCloudDatacatalogV1BigQueryConnectionSpecIn": "_datacatalog_190_GoogleCloudDatacatalogV1BigQueryConnectionSpecIn",
        "GoogleCloudDatacatalogV1BigQueryConnectionSpecOut": "_datacatalog_191_GoogleCloudDatacatalogV1BigQueryConnectionSpecOut",
        "GoogleCloudDatacatalogV1BigQueryRoutineSpecIn": "_datacatalog_192_GoogleCloudDatacatalogV1BigQueryRoutineSpecIn",
        "GoogleCloudDatacatalogV1BigQueryRoutineSpecOut": "_datacatalog_193_GoogleCloudDatacatalogV1BigQueryRoutineSpecOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaIn": "_datacatalog_194_GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaOut": "_datacatalog_195_GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaOut",
        "GoogleCloudDatacatalogV1TagFieldIn": "_datacatalog_196_GoogleCloudDatacatalogV1TagFieldIn",
        "GoogleCloudDatacatalogV1TagFieldOut": "_datacatalog_197_GoogleCloudDatacatalogV1TagFieldOut",
        "GoogleCloudDatacatalogV1PersonalDetailsIn": "_datacatalog_198_GoogleCloudDatacatalogV1PersonalDetailsIn",
        "GoogleCloudDatacatalogV1PersonalDetailsOut": "_datacatalog_199_GoogleCloudDatacatalogV1PersonalDetailsOut",
        "GoogleCloudDatacatalogV1DataSourceConnectionSpecIn": "_datacatalog_200_GoogleCloudDatacatalogV1DataSourceConnectionSpecIn",
        "GoogleCloudDatacatalogV1DataSourceConnectionSpecOut": "_datacatalog_201_GoogleCloudDatacatalogV1DataSourceConnectionSpecOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaIn": "_datacatalog_202_GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaOut": "_datacatalog_203_GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaOut",
        "GoogleCloudDatacatalogV1CommonUsageStatsIn": "_datacatalog_204_GoogleCloudDatacatalogV1CommonUsageStatsIn",
        "GoogleCloudDatacatalogV1CommonUsageStatsOut": "_datacatalog_205_GoogleCloudDatacatalogV1CommonUsageStatsOut",
        "BindingIn": "_datacatalog_206_BindingIn",
        "BindingOut": "_datacatalog_207_BindingOut",
        "GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecIn": "_datacatalog_208_GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecIn",
        "GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecOut": "_datacatalog_209_GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudDatacatalogV1ContactsPersonIn"] = t.struct(
        {"email": t.string().optional(), "designation": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1ContactsPersonIn"])
    types["GoogleCloudDatacatalogV1ContactsPersonOut"] = t.struct(
        {
            "email": t.string().optional(),
            "designation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ContactsPersonOut"])
    types["GoogleCloudDatacatalogV1StoragePropertiesIn"] = t.struct(
        {
            "filePattern": t.array(t.string()).optional(),
            "fileType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1StoragePropertiesIn"])
    types["GoogleCloudDatacatalogV1StoragePropertiesOut"] = t.struct(
        {
            "filePattern": t.array(t.string()).optional(),
            "fileType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1StoragePropertiesOut"])
    types["GoogleCloudDatacatalogV1ViewSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1ViewSpecIn"])
    types["GoogleCloudDatacatalogV1ViewSpecOut"] = t.struct(
        {
            "viewQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ViewSpecOut"])
    types["GoogleCloudDatacatalogV1ImportEntriesResponseIn"] = t.struct(
        {
            "upsertedEntriesCount": t.string().optional(),
            "deletedEntriesCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ImportEntriesResponseIn"])
    types["GoogleCloudDatacatalogV1ImportEntriesResponseOut"] = t.struct(
        {
            "upsertedEntriesCount": t.string().optional(),
            "deletedEntriesCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ImportEntriesResponseOut"])
    types["GoogleCloudDatacatalogV1SchemaIn"] = t.struct(
        {
            "columns": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1ColumnSchemaIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDatacatalogV1SchemaIn"])
    types["GoogleCloudDatacatalogV1SchemaOut"] = t.struct(
        {
            "columns": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1ColumnSchemaOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SchemaOut"])
    types["GoogleCloudDatacatalogV1SearchCatalogResponseIn"] = t.struct(
        {
            "results": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SearchCatalogResultIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogResponseIn"])
    types["GoogleCloudDatacatalogV1SearchCatalogResponseOut"] = t.struct(
        {
            "results": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SearchCatalogResultOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogResponseOut"])
    types["GoogleCloudDatacatalogV1GcsFilesetSpecIn"] = t.struct(
        {"filePatterns": t.array(t.string())}
    ).named(renames["GoogleCloudDatacatalogV1GcsFilesetSpecIn"])
    types["GoogleCloudDatacatalogV1GcsFilesetSpecOut"] = t.struct(
        {
            "filePatterns": t.array(t.string()),
            "sampleGcsFileSpecs": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1GcsFileSpecOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1GcsFilesetSpecOut"])
    types["GoogleCloudDatacatalogV1ListTaxonomiesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "taxonomies": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TaxonomyIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListTaxonomiesResponseIn"])
    types["GoogleCloudDatacatalogV1ListTaxonomiesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "taxonomies": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TaxonomyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListTaxonomiesResponseOut"])
    types["GoogleCloudDatacatalogV1ReconcileTagsResponseIn"] = t.struct(
        {
            "deletedTagsCount": t.string().optional(),
            "createdTagsCount": t.string().optional(),
            "updatedTagsCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ReconcileTagsResponseIn"])
    types["GoogleCloudDatacatalogV1ReconcileTagsResponseOut"] = t.struct(
        {
            "deletedTagsCount": t.string().optional(),
            "createdTagsCount": t.string().optional(),
            "updatedTagsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ReconcileTagsResponseOut"])
    types["GoogleCloudDatacatalogV1ListTagsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TagIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListTagsResponseIn"])
    types["GoogleCloudDatacatalogV1ListTagsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TagOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListTagsResponseOut"])
    types["GoogleCloudDatacatalogV1GcsFileSpecIn"] = t.struct(
        {"filePath": t.string()}
    ).named(renames["GoogleCloudDatacatalogV1GcsFileSpecIn"])
    types["GoogleCloudDatacatalogV1GcsFileSpecOut"] = t.struct(
        {
            "sizeBytes": t.string().optional(),
            "filePath": t.string(),
            "gcsTimestamps": t.proxy(
                renames["GoogleCloudDatacatalogV1SystemTimestampsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1GcsFileSpecOut"])
    types["GoogleCloudDatacatalogV1ColumnSchemaIn"] = t.struct(
        {
            "ordinalPosition": t.integer().optional(),
            "gcRule": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string(),
            "highestIndexingType": t.string().optional(),
            "subcolumns": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1ColumnSchemaIn"])
            ).optional(),
            "lookerColumnSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecIn"]
            ).optional(),
            "defaultValue": t.string().optional(),
            "column": t.string(),
            "mode": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ColumnSchemaIn"])
    types["GoogleCloudDatacatalogV1ColumnSchemaOut"] = t.struct(
        {
            "ordinalPosition": t.integer().optional(),
            "gcRule": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string(),
            "highestIndexingType": t.string().optional(),
            "subcolumns": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1ColumnSchemaOut"])
            ).optional(),
            "lookerColumnSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecOut"]
            ).optional(),
            "defaultValue": t.string().optional(),
            "column": t.string(),
            "mode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ColumnSchemaOut"])
    types["GoogleCloudDatacatalogV1EntryOverviewIn"] = t.struct(
        {"overview": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1EntryOverviewIn"])
    types["GoogleCloudDatacatalogV1EntryOverviewOut"] = t.struct(
        {
            "overview": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1EntryOverviewOut"])
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
    types["GoogleCloudDatacatalogV1ReconcileTagsRequestIn"] = t.struct(
        {
            "tags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TagIn"])
            ).optional(),
            "tagTemplate": t.string(),
            "forceDeleteMissing": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ReconcileTagsRequestIn"])
    types["GoogleCloudDatacatalogV1ReconcileTagsRequestOut"] = t.struct(
        {
            "tags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TagOut"])
            ).optional(),
            "tagTemplate": t.string(),
            "forceDeleteMissing": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ReconcileTagsRequestOut"])
    types["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"] = t.struct(
        {"instanceDisplayName": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"])
    types["GoogleCloudDatacatalogV1CloudBigtableSystemSpecOut"] = t.struct(
        {
            "instanceDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecOut"])
    types["GoogleCloudDatacatalogV1DataplexFilesetSpecIn"] = t.struct(
        {
            "dataplexSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DataplexSpecIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDatacatalogV1DataplexFilesetSpecIn"])
    types["GoogleCloudDatacatalogV1DataplexFilesetSpecOut"] = t.struct(
        {
            "dataplexSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DataplexSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataplexFilesetSpecOut"])
    types["GoogleCloudDatacatalogV1DumpItemIn"] = t.struct(
        {
            "taggedEntry": t.proxy(
                renames["GoogleCloudDatacatalogV1TaggedEntryIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDatacatalogV1DumpItemIn"])
    types["GoogleCloudDatacatalogV1DumpItemOut"] = t.struct(
        {
            "taggedEntry": t.proxy(
                renames["GoogleCloudDatacatalogV1TaggedEntryOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DumpItemOut"])
    types["GoogleCloudDatacatalogV1ReplaceTaxonomyRequestIn"] = t.struct(
        {
            "serializedTaxonomy": t.proxy(
                renames["GoogleCloudDatacatalogV1SerializedTaxonomyIn"]
            )
        }
    ).named(renames["GoogleCloudDatacatalogV1ReplaceTaxonomyRequestIn"])
    types["GoogleCloudDatacatalogV1ReplaceTaxonomyRequestOut"] = t.struct(
        {
            "serializedTaxonomy": t.proxy(
                renames["GoogleCloudDatacatalogV1SerializedTaxonomyOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ReplaceTaxonomyRequestOut"])
    types["GoogleCloudDatacatalogV1UsageSignalIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "favoriteCount": t.string().optional(),
            "commonUsageWithinTimeRange": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1UsageSignalIn"])
    types["GoogleCloudDatacatalogV1UsageSignalOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "favoriteCount": t.string().optional(),
            "commonUsageWithinTimeRange": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "usageWithinTimeRange": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1UsageSignalOut"])
    types["GoogleCloudDatacatalogV1ReconcileTagsMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "errors": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ReconcileTagsMetadataIn"])
    types["GoogleCloudDatacatalogV1ReconcileTagsMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "errors": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ReconcileTagsMetadataOut"])
    types["GoogleCloudDatacatalogV1ServiceSpecIn"] = t.struct(
        {
            "cloudBigtableInstanceSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1CloudBigtableInstanceSpecIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDatacatalogV1ServiceSpecIn"])
    types["GoogleCloudDatacatalogV1ServiceSpecOut"] = t.struct(
        {
            "cloudBigtableInstanceSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1CloudBigtableInstanceSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ServiceSpecOut"])
    types["GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueIn"] = t.struct(
        {"displayName": t.string()}
    ).named(renames["GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueIn"])
    types["GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueOut"] = t.struct(
        {
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueOut"])
    types["GoogleCloudDatacatalogV1ListEntryGroupsResponseIn"] = t.struct(
        {
            "entryGroups": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1EntryGroupIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListEntryGroupsResponseIn"])
    types["GoogleCloudDatacatalogV1ListEntryGroupsResponseOut"] = t.struct(
        {
            "entryGroups": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1EntryGroupOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListEntryGroupsResponseOut"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaIn"] = t.struct(
        {
            "thrift": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaIn"]
            ).optional(),
            "protobuf": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaIn"]
            ).optional(),
            "parquet": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaIn"]
            ).optional(),
            "avro": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaIn"]
            ).optional(),
            "csv": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaIn"]
            ).optional(),
            "orc": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaOut"] = t.struct(
        {
            "thrift": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaOut"]
            ).optional(),
            "protobuf": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaOut"]
            ).optional(),
            "parquet": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaOut"]
            ).optional(),
            "avro": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaOut"]
            ).optional(),
            "csv": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaOut"]
            ).optional(),
            "orc": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaOut"])
    types["GoogleCloudDatacatalogV1DataplexTableSpecIn"] = t.struct(
        {
            "externalTables": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1DataplexExternalTableIn"])
            ).optional(),
            "dataplexSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DataplexSpecIn"]
            ).optional(),
            "userManaged": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataplexTableSpecIn"])
    types["GoogleCloudDatacatalogV1DataplexTableSpecOut"] = t.struct(
        {
            "externalTables": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1DataplexExternalTableOut"])
            ).optional(),
            "dataplexSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DataplexSpecOut"]
            ).optional(),
            "userManaged": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataplexTableSpecOut"])
    types[
        "GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequestIn"
    ] = t.struct({"newEnumValueDisplayName": t.string()}).named(
        renames["GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequestIn"]
    )
    types[
        "GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequestOut"
    ] = t.struct(
        {
            "newEnumValueDisplayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequestOut"]
    )
    types["GoogleCloudDatacatalogV1ExportTaxonomiesResponseIn"] = t.struct(
        {
            "taxonomies": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SerializedTaxonomyIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDatacatalogV1ExportTaxonomiesResponseIn"])
    types["GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut"] = t.struct(
        {
            "taxonomies": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SerializedTaxonomyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["GoogleCloudDatacatalogV1SearchCatalogResultIn"] = t.struct(
        {
            "linkedResource": t.string().optional(),
            "searchResultType": t.string().optional(),
            "searchResultSubtype": t.string().optional(),
            "displayName": t.string().optional(),
            "userSpecifiedSystem": t.string().optional(),
            "relativeResourceName": t.string().optional(),
            "modifyTime": t.string().optional(),
            "fullyQualifiedName": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogResultIn"])
    types["GoogleCloudDatacatalogV1SearchCatalogResultOut"] = t.struct(
        {
            "linkedResource": t.string().optional(),
            "integratedSystem": t.string().optional(),
            "searchResultType": t.string().optional(),
            "searchResultSubtype": t.string().optional(),
            "displayName": t.string().optional(),
            "userSpecifiedSystem": t.string().optional(),
            "relativeResourceName": t.string().optional(),
            "modifyTime": t.string().optional(),
            "fullyQualifiedName": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogResultOut"])
    types["GoogleCloudDatacatalogV1TagTemplateIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}),
            "isPubliclyReadable": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagTemplateIn"])
    types["GoogleCloudDatacatalogV1TagTemplateOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}),
            "isPubliclyReadable": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagTemplateOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["GoogleCloudDatacatalogV1UnstarEntryRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1UnstarEntryRequestIn"])
    types["GoogleCloudDatacatalogV1UnstarEntryRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1UnstarEntryRequestOut"])
    types["GoogleCloudDatacatalogV1EntryGroupIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1EntryGroupIn"])
    types["GoogleCloudDatacatalogV1EntryGroupOut"] = t.struct(
        {
            "dataCatalogTimestamps": t.proxy(
                renames["GoogleCloudDatacatalogV1SystemTimestampsOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1EntryGroupOut"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaOut"])
    types["GoogleCloudDatacatalogV1CloudBigtableInstanceSpecIn"] = t.struct(
        {
            "cloudBigtableClusterSpecs": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudDatacatalogV1CloudBigtableInstanceSpecIn"])
    types["GoogleCloudDatacatalogV1CloudBigtableInstanceSpecOut"] = t.struct(
        {
            "cloudBigtableClusterSpecs": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1CloudBigtableInstanceSpecOut"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaOut"])
    types["GoogleCloudDatacatalogV1BigQueryTableSpecIn"] = t.struct(
        {
            "viewSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1ViewSpecIn"]
            ).optional(),
            "tableSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1TableSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1BigQueryTableSpecIn"])
    types["GoogleCloudDatacatalogV1BigQueryTableSpecOut"] = t.struct(
        {
            "viewSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1ViewSpecOut"]
            ).optional(),
            "tableSourceType": t.string().optional(),
            "tableSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1TableSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1BigQueryTableSpecOut"])
    types["GoogleCloudDatacatalogV1SerializedTaxonomyIn"] = t.struct(
        {
            "policyTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SerializedPolicyTagIn"])
            ).optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
            "activatedPolicyTypes": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SerializedTaxonomyIn"])
    types["GoogleCloudDatacatalogV1SerializedTaxonomyOut"] = t.struct(
        {
            "policyTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SerializedPolicyTagOut"])
            ).optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
            "activatedPolicyTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SerializedTaxonomyOut"])
    types["GoogleCloudDatacatalogV1TaggedEntryIn"] = t.struct(
        {
            "absentTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TagIn"])
            ).optional(),
            "presentTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TagIn"])
            ).optional(),
            "v1Entry": t.proxy(renames["GoogleCloudDatacatalogV1EntryIn"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TaggedEntryIn"])
    types["GoogleCloudDatacatalogV1TaggedEntryOut"] = t.struct(
        {
            "absentTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TagOut"])
            ).optional(),
            "presentTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TagOut"])
            ).optional(),
            "v1Entry": t.proxy(renames["GoogleCloudDatacatalogV1EntryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TaggedEntryOut"])
    types["GoogleCloudDatacatalogV1FieldTypeIn"] = t.struct(
        {
            "primitiveType": t.string().optional(),
            "enumType": t.proxy(
                renames["GoogleCloudDatacatalogV1FieldTypeEnumTypeIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1FieldTypeIn"])
    types["GoogleCloudDatacatalogV1FieldTypeOut"] = t.struct(
        {
            "primitiveType": t.string().optional(),
            "enumType": t.proxy(
                renames["GoogleCloudDatacatalogV1FieldTypeEnumTypeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1FieldTypeOut"])
    types["GoogleCloudDatacatalogV1EntryIn"] = t.struct(
        {
            "routineSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1RoutineSpecIn"]
            ).optional(),
            "lookerSystemSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1LookerSystemSpecIn"]
            ).optional(),
            "linkedResource": t.string().optional(),
            "type": t.string().optional(),
            "sourceSystemTimestamps": t.proxy(
                renames["GoogleCloudDatacatalogV1SystemTimestampsIn"]
            ).optional(),
            "schema": t.proxy(renames["GoogleCloudDatacatalogV1SchemaIn"]).optional(),
            "businessContext": t.proxy(
                renames["GoogleCloudDatacatalogV1BusinessContextIn"]
            ).optional(),
            "fullyQualifiedName": t.string().optional(),
            "description": t.string().optional(),
            "dataSourceConnectionSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecIn"]
            ).optional(),
            "userSpecifiedType": t.string().optional(),
            "cloudBigtableSystemSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serviceSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1ServiceSpecIn"]
            ).optional(),
            "sqlDatabaseSystemSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"]
            ).optional(),
            "userSpecifiedSystem": t.string().optional(),
            "usageSignal": t.proxy(
                renames["GoogleCloudDatacatalogV1UsageSignalIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "filesetSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1FilesetSpecIn"]
            ).optional(),
            "gcsFilesetSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1GcsFilesetSpecIn"]
            ).optional(),
            "databaseTableSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DatabaseTableSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1EntryIn"])
    types["GoogleCloudDatacatalogV1EntryOut"] = t.struct(
        {
            "routineSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1RoutineSpecOut"]
            ).optional(),
            "bigqueryTableSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1BigQueryTableSpecOut"]
            ).optional(),
            "bigqueryDateShardedSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1BigQueryDateShardedSpecOut"]
            ).optional(),
            "lookerSystemSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1LookerSystemSpecOut"]
            ).optional(),
            "personalDetails": t.proxy(
                renames["GoogleCloudDatacatalogV1PersonalDetailsOut"]
            ).optional(),
            "linkedResource": t.string().optional(),
            "type": t.string().optional(),
            "sourceSystemTimestamps": t.proxy(
                renames["GoogleCloudDatacatalogV1SystemTimestampsOut"]
            ).optional(),
            "dataSource": t.proxy(
                renames["GoogleCloudDatacatalogV1DataSourceOut"]
            ).optional(),
            "schema": t.proxy(renames["GoogleCloudDatacatalogV1SchemaOut"]).optional(),
            "businessContext": t.proxy(
                renames["GoogleCloudDatacatalogV1BusinessContextOut"]
            ).optional(),
            "fullyQualifiedName": t.string().optional(),
            "description": t.string().optional(),
            "dataSourceConnectionSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecOut"]
            ).optional(),
            "userSpecifiedType": t.string().optional(),
            "cloudBigtableSystemSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serviceSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1ServiceSpecOut"]
            ).optional(),
            "sqlDatabaseSystemSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecOut"]
            ).optional(),
            "userSpecifiedSystem": t.string().optional(),
            "integratedSystem": t.string().optional(),
            "usageSignal": t.proxy(
                renames["GoogleCloudDatacatalogV1UsageSignalOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "filesetSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1FilesetSpecOut"]
            ).optional(),
            "gcsFilesetSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1GcsFilesetSpecOut"]
            ).optional(),
            "databaseTableSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DatabaseTableSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1EntryOut"])
    types["GoogleCloudDatacatalogV1TagTemplateFieldIn"] = t.struct(
        {
            "type": t.proxy(renames["GoogleCloudDatacatalogV1FieldTypeIn"]),
            "order": t.integer().optional(),
            "description": t.string().optional(),
            "isRequired": t.boolean().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagTemplateFieldIn"])
    types["GoogleCloudDatacatalogV1TagTemplateFieldOut"] = t.struct(
        {
            "type": t.proxy(renames["GoogleCloudDatacatalogV1FieldTypeOut"]),
            "name": t.string().optional(),
            "order": t.integer().optional(),
            "description": t.string().optional(),
            "isRequired": t.boolean().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagTemplateFieldOut"])
    types["GoogleCloudDatacatalogV1TagIn"] = t.struct(
        {
            "fields": t.struct({"_": t.string().optional()}),
            "column": t.string().optional(),
            "template": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagIn"])
    types["GoogleCloudDatacatalogV1TagOut"] = t.struct(
        {
            "fields": t.struct({"_": t.string().optional()}),
            "column": t.string().optional(),
            "template": t.string(),
            "templateDisplayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagOut"])
    types["GoogleCloudDatacatalogV1FieldTypeEnumTypeIn"] = t.struct(
        {
            "allowedValues": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDatacatalogV1FieldTypeEnumTypeIn"])
    types["GoogleCloudDatacatalogV1FieldTypeEnumTypeOut"] = t.struct(
        {
            "allowedValues": t.array(
                t.proxy(
                    renames["GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1FieldTypeEnumTypeOut"])
    types["GoogleCloudDatacatalogV1ListPolicyTagsResponseIn"] = t.struct(
        {
            "policyTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListPolicyTagsResponseIn"])
    types["GoogleCloudDatacatalogV1ListPolicyTagsResponseOut"] = t.struct(
        {
            "policyTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListPolicyTagsResponseOut"])
    types["GoogleCloudDatacatalogV1StarEntryRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1StarEntryRequestIn"])
    types["GoogleCloudDatacatalogV1StarEntryRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1StarEntryRequestOut"])
    types["GoogleCloudDatacatalogV1PolicyTagIn"] = t.struct(
        {
            "description": t.string().optional(),
            "parentPolicyTag": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PolicyTagIn"])
    types["GoogleCloudDatacatalogV1PolicyTagOut"] = t.struct(
        {
            "childPolicyTags": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "parentPolicyTag": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PolicyTagOut"])
    types["GoogleCloudDatacatalogV1SerializedPolicyTagIn"] = t.struct(
        {
            "policyTag": t.string().optional(),
            "childPolicyTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SerializedPolicyTagIn"])
            ).optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SerializedPolicyTagIn"])
    types["GoogleCloudDatacatalogV1SerializedPolicyTagOut"] = t.struct(
        {
            "policyTag": t.string().optional(),
            "childPolicyTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SerializedPolicyTagOut"])
            ).optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SerializedPolicyTagOut"])
    types["GoogleCloudDatacatalogV1DataplexExternalTableIn"] = t.struct(
        {
            "googleCloudResource": t.string().optional(),
            "dataCatalogEntry": t.string().optional(),
            "fullyQualifiedName": t.string().optional(),
            "system": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataplexExternalTableIn"])
    types["GoogleCloudDatacatalogV1DataplexExternalTableOut"] = t.struct(
        {
            "googleCloudResource": t.string().optional(),
            "dataCatalogEntry": t.string().optional(),
            "fullyQualifiedName": t.string().optional(),
            "system": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataplexExternalTableOut"])
    types["GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecIn"] = t.struct(
        {
            "type": t.string().optional(),
            "instanceId": t.string().optional(),
            "database": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecIn"])
    types["GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecOut"] = t.struct(
        {
            "type": t.string().optional(),
            "instanceId": t.string().optional(),
            "database": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecOut"])
    types["GoogleCloudDatacatalogV1UnstarEntryResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1UnstarEntryResponseIn"])
    types["GoogleCloudDatacatalogV1UnstarEntryResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1UnstarEntryResponseOut"])
    types["GoogleCloudDatacatalogV1DataplexSpecIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "dataFormat": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaIn"]
            ).optional(),
            "compressionFormat": t.string().optional(),
            "asset": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataplexSpecIn"])
    types["GoogleCloudDatacatalogV1DataplexSpecOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "dataFormat": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaOut"]
            ).optional(),
            "compressionFormat": t.string().optional(),
            "asset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataplexSpecOut"])
    types["GoogleCloudDatacatalogV1TableSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1TableSpecIn"])
    types["GoogleCloudDatacatalogV1TableSpecOut"] = t.struct(
        {
            "groupedEntry": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TableSpecOut"])
    types["GoogleCloudDatacatalogV1ImportEntriesRequestIn"] = t.struct(
        {"gcsBucketPath": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1ImportEntriesRequestIn"])
    types["GoogleCloudDatacatalogV1ImportEntriesRequestOut"] = t.struct(
        {
            "gcsBucketPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ImportEntriesRequestOut"])
    types["GoogleCloudDatacatalogV1DataSourceIn"] = t.struct(
        {
            "resource": t.string().optional(),
            "service": t.string().optional(),
            "storageProperties": t.proxy(
                renames["GoogleCloudDatacatalogV1StoragePropertiesIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataSourceIn"])
    types["GoogleCloudDatacatalogV1DataSourceOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "service": t.string().optional(),
            "sourceEntry": t.string().optional(),
            "storageProperties": t.proxy(
                renames["GoogleCloudDatacatalogV1StoragePropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataSourceOut"])
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
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["GoogleCloudDatacatalogV1ContactsIn"] = t.struct(
        {
            "people": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1ContactsPersonIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDatacatalogV1ContactsIn"])
    types["GoogleCloudDatacatalogV1ContactsOut"] = t.struct(
        {
            "people": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1ContactsPersonOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ContactsOut"])
    types["GoogleCloudDatacatalogV1TaxonomyServiceIn"] = t.struct(
        {"identity": t.string().optional(), "name": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1TaxonomyServiceIn"])
    types["GoogleCloudDatacatalogV1TaxonomyServiceOut"] = t.struct(
        {
            "identity": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TaxonomyServiceOut"])
    types[
        "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecIn"
    ] = t.struct(
        {
            "linkedResource": t.string().optional(),
            "location": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecIn"
        ]
    )
    types[
        "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecOut"
    ] = t.struct(
        {
            "linkedResource": t.string().optional(),
            "location": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecOut"
        ]
    )
    types["GoogleCloudDatacatalogV1InlineSourceIn"] = t.struct(
        {
            "taxonomies": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SerializedTaxonomyIn"])
            )
        }
    ).named(renames["GoogleCloudDatacatalogV1InlineSourceIn"])
    types["GoogleCloudDatacatalogV1InlineSourceOut"] = t.struct(
        {
            "taxonomies": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SerializedTaxonomyOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1InlineSourceOut"])
    types["GoogleCloudDatacatalogV1SearchCatalogRequestScopeIn"] = t.struct(
        {
            "includePublicTagTemplates": t.boolean().optional(),
            "includeGcpPublicDatasets": t.boolean().optional(),
            "includeProjectIds": t.array(t.string()).optional(),
            "starredOnly": t.boolean().optional(),
            "includeOrgIds": t.array(t.string()).optional(),
            "restrictedLocations": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogRequestScopeIn"])
    types["GoogleCloudDatacatalogV1SearchCatalogRequestScopeOut"] = t.struct(
        {
            "includePublicTagTemplates": t.boolean().optional(),
            "includeGcpPublicDatasets": t.boolean().optional(),
            "includeProjectIds": t.array(t.string()).optional(),
            "starredOnly": t.boolean().optional(),
            "includeOrgIds": t.array(t.string()).optional(),
            "restrictedLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogRequestScopeOut"])
    types["GoogleCloudDatacatalogV1LookerSystemSpecIn"] = t.struct(
        {
            "parentViewId": t.string().optional(),
            "parentInstanceDisplayName": t.string().optional(),
            "parentModelId": t.string().optional(),
            "parentModelDisplayName": t.string().optional(),
            "parentViewDisplayName": t.string().optional(),
            "parentInstanceId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1LookerSystemSpecIn"])
    types["GoogleCloudDatacatalogV1LookerSystemSpecOut"] = t.struct(
        {
            "parentViewId": t.string().optional(),
            "parentInstanceDisplayName": t.string().optional(),
            "parentModelId": t.string().optional(),
            "parentModelDisplayName": t.string().optional(),
            "parentViewDisplayName": t.string().optional(),
            "parentInstanceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1LookerSystemSpecOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["GoogleCloudDatacatalogV1ListEntriesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1EntryIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListEntriesResponseIn"])
    types["GoogleCloudDatacatalogV1ListEntriesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1EntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListEntriesResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["GoogleCloudDatacatalogV1SystemTimestampsIn"] = t.struct(
        {"updateTime": t.string().optional(), "createTime": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1SystemTimestampsIn"])
    types["GoogleCloudDatacatalogV1SystemTimestampsOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "expireTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SystemTimestampsOut"])
    types["GoogleCloudDatacatalogV1RoutineSpecArgumentIn"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "mode": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1RoutineSpecArgumentIn"])
    types["GoogleCloudDatacatalogV1RoutineSpecArgumentOut"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "mode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1RoutineSpecArgumentOut"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaOut"])
    types["GoogleCloudDatacatalogV1SearchCatalogRequestIn"] = t.struct(
        {
            "query": t.string().optional(),
            "pageSize": t.integer().optional(),
            "scope": t.proxy(
                renames["GoogleCloudDatacatalogV1SearchCatalogRequestScopeIn"]
            ),
            "pageToken": t.string().optional(),
            "orderBy": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogRequestIn"])
    types["GoogleCloudDatacatalogV1SearchCatalogRequestOut"] = t.struct(
        {
            "query": t.string().optional(),
            "pageSize": t.integer().optional(),
            "scope": t.proxy(
                renames["GoogleCloudDatacatalogV1SearchCatalogRequestScopeOut"]
            ),
            "pageToken": t.string().optional(),
            "orderBy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogRequestOut"])
    types["GoogleCloudDatacatalogV1BigQueryDateShardedSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1BigQueryDateShardedSpecIn"])
    types["GoogleCloudDatacatalogV1BigQueryDateShardedSpecOut"] = t.struct(
        {
            "dataset": t.string().optional(),
            "shardCount": t.string().optional(),
            "tablePrefix": t.string().optional(),
            "latestShardResource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1BigQueryDateShardedSpecOut"])
    types["GoogleCloudDatacatalogV1StarEntryResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1StarEntryResponseIn"])
    types["GoogleCloudDatacatalogV1StarEntryResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1StarEntryResponseOut"])
    types["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"] = t.struct(
        {
            "sqlEngine": t.string().optional(),
            "instanceHost": t.string().optional(),
            "databaseVersion": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"])
    types["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecOut"] = t.struct(
        {
            "sqlEngine": t.string().optional(),
            "instanceHost": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecOut"])
    types["GoogleCloudDatacatalogV1BusinessContextIn"] = t.struct(
        {
            "contacts": t.proxy(
                renames["GoogleCloudDatacatalogV1ContactsIn"]
            ).optional(),
            "entryOverview": t.proxy(
                renames["GoogleCloudDatacatalogV1EntryOverviewIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1BusinessContextIn"])
    types["GoogleCloudDatacatalogV1BusinessContextOut"] = t.struct(
        {
            "contacts": t.proxy(
                renames["GoogleCloudDatacatalogV1ContactsOut"]
            ).optional(),
            "entryOverview": t.proxy(
                renames["GoogleCloudDatacatalogV1EntryOverviewOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1BusinessContextOut"])
    types["GoogleCloudDatacatalogV1FilesetSpecIn"] = t.struct(
        {
            "dataplexFileset": t.proxy(
                renames["GoogleCloudDatacatalogV1DataplexFilesetSpecIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDatacatalogV1FilesetSpecIn"])
    types["GoogleCloudDatacatalogV1FilesetSpecOut"] = t.struct(
        {
            "dataplexFileset": t.proxy(
                renames["GoogleCloudDatacatalogV1DataplexFilesetSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1FilesetSpecOut"])
    types["GoogleCloudDatacatalogV1TagFieldEnumValueIn"] = t.struct(
        {"displayName": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1TagFieldEnumValueIn"])
    types["GoogleCloudDatacatalogV1TagFieldEnumValueOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagFieldEnumValueOut"])
    types["GoogleCloudDatacatalogV1RoutineSpecIn"] = t.struct(
        {
            "returnType": t.string().optional(),
            "routineArguments": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1RoutineSpecArgumentIn"])
            ).optional(),
            "language": t.string().optional(),
            "bigqueryRoutineSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1BigQueryRoutineSpecIn"]
            ).optional(),
            "routineType": t.string().optional(),
            "definitionBody": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1RoutineSpecIn"])
    types["GoogleCloudDatacatalogV1RoutineSpecOut"] = t.struct(
        {
            "returnType": t.string().optional(),
            "routineArguments": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1RoutineSpecArgumentOut"])
            ).optional(),
            "language": t.string().optional(),
            "bigqueryRoutineSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1BigQueryRoutineSpecOut"]
            ).optional(),
            "routineType": t.string().optional(),
            "definitionBody": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1RoutineSpecOut"])
    types["GoogleCloudDatacatalogV1ImportTaxonomiesRequestIn"] = t.struct(
        {
            "inlineSource": t.proxy(
                renames["GoogleCloudDatacatalogV1InlineSourceIn"]
            ).optional(),
            "crossRegionalSource": t.proxy(
                renames["GoogleCloudDatacatalogV1CrossRegionalSourceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ImportTaxonomiesRequestIn"])
    types["GoogleCloudDatacatalogV1ImportTaxonomiesRequestOut"] = t.struct(
        {
            "inlineSource": t.proxy(
                renames["GoogleCloudDatacatalogV1InlineSourceOut"]
            ).optional(),
            "crossRegionalSource": t.proxy(
                renames["GoogleCloudDatacatalogV1CrossRegionalSourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ImportTaxonomiesRequestOut"])
    types["GoogleCloudDatacatalogV1DatabaseTableSpecIn"] = t.struct(
        {
            "type": t.string().optional(),
            "databaseViewSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DatabaseTableSpecIn"])
    types["GoogleCloudDatacatalogV1DatabaseTableSpecOut"] = t.struct(
        {
            "type": t.string().optional(),
            "databaseViewSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecOut"]
            ).optional(),
            "dataplexTable": t.proxy(
                renames["GoogleCloudDatacatalogV1DataplexTableSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DatabaseTableSpecOut"])
    types["GoogleCloudDatacatalogV1CrossRegionalSourceIn"] = t.struct(
        {"taxonomy": t.string()}
    ).named(renames["GoogleCloudDatacatalogV1CrossRegionalSourceIn"])
    types["GoogleCloudDatacatalogV1CrossRegionalSourceOut"] = t.struct(
        {"taxonomy": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1CrossRegionalSourceOut"])
    types["GoogleCloudDatacatalogV1UsageStatsIn"] = t.struct(
        {
            "totalFailures": t.number().optional(),
            "totalExecutionTimeForCompletionsMillis": t.number().optional(),
            "totalCancellations": t.number().optional(),
            "totalCompletions": t.number().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1UsageStatsIn"])
    types["GoogleCloudDatacatalogV1UsageStatsOut"] = t.struct(
        {
            "totalFailures": t.number().optional(),
            "totalExecutionTimeForCompletionsMillis": t.number().optional(),
            "totalCancellations": t.number().optional(),
            "totalCompletions": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1UsageStatsOut"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaOut"])
    types["GoogleCloudDatacatalogV1ImportEntriesMetadataIn"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["StatusIn"])).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ImportEntriesMetadataIn"])
    types["GoogleCloudDatacatalogV1ImportEntriesMetadataOut"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ImportEntriesMetadataOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoogleCloudDatacatalogV1ModifyEntryOverviewRequestIn"] = t.struct(
        {"entryOverview": t.proxy(renames["GoogleCloudDatacatalogV1EntryOverviewIn"])}
    ).named(renames["GoogleCloudDatacatalogV1ModifyEntryOverviewRequestIn"])
    types["GoogleCloudDatacatalogV1ModifyEntryOverviewRequestOut"] = t.struct(
        {
            "entryOverview": t.proxy(
                renames["GoogleCloudDatacatalogV1EntryOverviewOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ModifyEntryOverviewRequestOut"])
    types["GoogleCloudDatacatalogV1ModifyEntryContactsRequestIn"] = t.struct(
        {"contacts": t.proxy(renames["GoogleCloudDatacatalogV1ContactsIn"])}
    ).named(renames["GoogleCloudDatacatalogV1ModifyEntryContactsRequestIn"])
    types["GoogleCloudDatacatalogV1ModifyEntryContactsRequestOut"] = t.struct(
        {
            "contacts": t.proxy(renames["GoogleCloudDatacatalogV1ContactsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ModifyEntryContactsRequestOut"])
    types["GoogleCloudDatacatalogV1TaxonomyIn"] = t.struct(
        {
            "description": t.string().optional(),
            "displayName": t.string(),
            "activatedPolicyTypes": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TaxonomyIn"])
    types["GoogleCloudDatacatalogV1TaxonomyOut"] = t.struct(
        {
            "description": t.string().optional(),
            "displayName": t.string(),
            "service": t.proxy(
                renames["GoogleCloudDatacatalogV1TaxonomyServiceOut"]
            ).optional(),
            "taxonomyTimestamps": t.proxy(
                renames["GoogleCloudDatacatalogV1SystemTimestampsOut"]
            ).optional(),
            "policyTagCount": t.integer().optional(),
            "name": t.string().optional(),
            "activatedPolicyTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TaxonomyOut"])
    types["GoogleCloudDatacatalogV1ImportTaxonomiesResponseIn"] = t.struct(
        {
            "taxonomies": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TaxonomyIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDatacatalogV1ImportTaxonomiesResponseIn"])
    types["GoogleCloudDatacatalogV1ImportTaxonomiesResponseOut"] = t.struct(
        {
            "taxonomies": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TaxonomyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ImportTaxonomiesResponseOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestIn"] = t.struct(
        {"newTagTemplateFieldId": t.string()}
    ).named(renames["GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestIn"])
    types["GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestOut"] = t.struct(
        {
            "newTagTemplateFieldId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestOut"])
    types["GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecIn"])
    types["GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecOut"])
    types["GoogleCloudDatacatalogV1BigQueryConnectionSpecIn"] = t.struct(
        {
            "connectionType": t.string().optional(),
            "hasCredential": t.boolean().optional(),
            "cloudSql": t.proxy(
                renames["GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1BigQueryConnectionSpecIn"])
    types["GoogleCloudDatacatalogV1BigQueryConnectionSpecOut"] = t.struct(
        {
            "connectionType": t.string().optional(),
            "hasCredential": t.boolean().optional(),
            "cloudSql": t.proxy(
                renames["GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1BigQueryConnectionSpecOut"])
    types["GoogleCloudDatacatalogV1BigQueryRoutineSpecIn"] = t.struct(
        {"importedLibraries": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDatacatalogV1BigQueryRoutineSpecIn"])
    types["GoogleCloudDatacatalogV1BigQueryRoutineSpecOut"] = t.struct(
        {
            "importedLibraries": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1BigQueryRoutineSpecOut"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaOut"])
    types["GoogleCloudDatacatalogV1TagFieldIn"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "timestampValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "richtextValue": t.string().optional(),
            "enumValue": t.proxy(
                renames["GoogleCloudDatacatalogV1TagFieldEnumValueIn"]
            ).optional(),
            "boolValue": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagFieldIn"])
    types["GoogleCloudDatacatalogV1TagFieldOut"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "timestampValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "order": t.integer().optional(),
            "richtextValue": t.string().optional(),
            "enumValue": t.proxy(
                renames["GoogleCloudDatacatalogV1TagFieldEnumValueOut"]
            ).optional(),
            "boolValue": t.boolean().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagFieldOut"])
    types["GoogleCloudDatacatalogV1PersonalDetailsIn"] = t.struct(
        {"starred": t.boolean().optional(), "starTime": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PersonalDetailsIn"])
    types["GoogleCloudDatacatalogV1PersonalDetailsOut"] = t.struct(
        {
            "starred": t.boolean().optional(),
            "starTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PersonalDetailsOut"])
    types["GoogleCloudDatacatalogV1DataSourceConnectionSpecIn"] = t.struct(
        {
            "bigqueryConnectionSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1BigQueryConnectionSpecIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecIn"])
    types["GoogleCloudDatacatalogV1DataSourceConnectionSpecOut"] = t.struct(
        {
            "bigqueryConnectionSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1BigQueryConnectionSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecOut"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaOut"])
    types["GoogleCloudDatacatalogV1CommonUsageStatsIn"] = t.struct(
        {"viewCount": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1CommonUsageStatsIn"])
    types["GoogleCloudDatacatalogV1CommonUsageStatsOut"] = t.struct(
        {
            "viewCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1CommonUsageStatsOut"])
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
    types["GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecIn"] = t.struct(
        {
            "baseTable": t.string().optional(),
            "sqlQuery": t.string().optional(),
            "viewType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecIn"])
    types["GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecOut"] = t.struct(
        {
            "baseTable": t.string().optional(),
            "sqlQuery": t.string().optional(),
            "viewType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecOut"])

    functions = {}
    functions["entriesLookup"] = datacatalog.get(
        "v1/entries:lookup",
        t.struct(
            {
                "fullyQualifiedName": t.string().optional(),
                "sqlResource": t.string().optional(),
                "linkedResource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsGet"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsList"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsTestIamPermissions"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsSetIamPolicy"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsCreate"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsGetIamPolicy"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsDelete"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsPatch"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesUnstar"] = datacatalog.post(
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
    functions["projectsLocationsEntryGroupsEntriesGetIamPolicy"] = datacatalog.post(
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
    functions["projectsLocationsEntryGroupsEntriesDelete"] = datacatalog.post(
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
    functions[
        "projectsLocationsEntryGroupsEntriesModifyEntryOverview"
    ] = datacatalog.post(
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
    functions["projectsLocationsEntryGroupsEntriesPatch"] = datacatalog.post(
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
    functions["projectsLocationsEntryGroupsEntriesStar"] = datacatalog.post(
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
    functions["projectsLocationsEntryGroupsEntriesList"] = datacatalog.post(
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
    functions["projectsLocationsEntryGroupsEntriesCreate"] = datacatalog.post(
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
    functions["projectsLocationsEntryGroupsEntriesGet"] = datacatalog.post(
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
    functions["projectsLocationsEntryGroupsEntriesImport"] = datacatalog.post(
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
    functions[
        "projectsLocationsEntryGroupsEntriesModifyEntryContacts"
    ] = datacatalog.post(
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
    functions[
        "projectsLocationsEntryGroupsEntriesTestIamPermissions"
    ] = datacatalog.post(
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
    functions["projectsLocationsEntryGroupsEntriesTagsReconcile"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesTagsPatch"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesTagsList"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesTagsCreate"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesTagsDelete"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsTagsList"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsTagsPatch"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsTagsCreate"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsTagsDelete"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = datacatalog.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = datacatalog.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = datacatalog.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = datacatalog.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesList"] = datacatalog.get(
        "v1/{parent}/taxonomies:export",
        t.struct(
            {
                "taxonomies": t.string(),
                "parent": t.string(),
                "serializedTaxonomies": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesDelete"] = datacatalog.get(
        "v1/{parent}/taxonomies:export",
        t.struct(
            {
                "taxonomies": t.string(),
                "parent": t.string(),
                "serializedTaxonomies": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesGet"] = datacatalog.get(
        "v1/{parent}/taxonomies:export",
        t.struct(
            {
                "taxonomies": t.string(),
                "parent": t.string(),
                "serializedTaxonomies": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesSetIamPolicy"] = datacatalog.get(
        "v1/{parent}/taxonomies:export",
        t.struct(
            {
                "taxonomies": t.string(),
                "parent": t.string(),
                "serializedTaxonomies": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPatch"] = datacatalog.get(
        "v1/{parent}/taxonomies:export",
        t.struct(
            {
                "taxonomies": t.string(),
                "parent": t.string(),
                "serializedTaxonomies": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesImport"] = datacatalog.get(
        "v1/{parent}/taxonomies:export",
        t.struct(
            {
                "taxonomies": t.string(),
                "parent": t.string(),
                "serializedTaxonomies": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesTestIamPermissions"] = datacatalog.get(
        "v1/{parent}/taxonomies:export",
        t.struct(
            {
                "taxonomies": t.string(),
                "parent": t.string(),
                "serializedTaxonomies": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesCreate"] = datacatalog.get(
        "v1/{parent}/taxonomies:export",
        t.struct(
            {
                "taxonomies": t.string(),
                "parent": t.string(),
                "serializedTaxonomies": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesReplace"] = datacatalog.get(
        "v1/{parent}/taxonomies:export",
        t.struct(
            {
                "taxonomies": t.string(),
                "parent": t.string(),
                "serializedTaxonomies": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesGetIamPolicy"] = datacatalog.get(
        "v1/{parent}/taxonomies:export",
        t.struct(
            {
                "taxonomies": t.string(),
                "parent": t.string(),
                "serializedTaxonomies": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesExport"] = datacatalog.get(
        "v1/{parent}/taxonomies:export",
        t.struct(
            {
                "taxonomies": t.string(),
                "parent": t.string(),
                "serializedTaxonomies": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsPatch"] = datacatalog.post(
        "v1/{parent}/policyTags",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "parentPolicyTag": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsGetIamPolicy"] = datacatalog.post(
        "v1/{parent}/policyTags",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "parentPolicyTag": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsSetIamPolicy"] = datacatalog.post(
        "v1/{parent}/policyTags",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "parentPolicyTag": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsGet"] = datacatalog.post(
        "v1/{parent}/policyTags",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "parentPolicyTag": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsList"] = datacatalog.post(
        "v1/{parent}/policyTags",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "parentPolicyTag": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsDelete"] = datacatalog.post(
        "v1/{parent}/policyTags",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "parentPolicyTag": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsTaxonomiesPolicyTagsTestIamPermissions"
    ] = datacatalog.post(
        "v1/{parent}/policyTags",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "parentPolicyTag": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsCreate"] = datacatalog.post(
        "v1/{parent}/policyTags",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "parentPolicyTag": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesCreate"] = datacatalog.delete(
        "v1/{name}",
        t.struct(
            {"name": t.string(), "force": t.boolean(), "auth": t.string().optional()}
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesGet"] = datacatalog.delete(
        "v1/{name}",
        t.struct(
            {"name": t.string(), "force": t.boolean(), "auth": t.string().optional()}
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesTestIamPermissions"] = datacatalog.delete(
        "v1/{name}",
        t.struct(
            {"name": t.string(), "force": t.boolean(), "auth": t.string().optional()}
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesPatch"] = datacatalog.delete(
        "v1/{name}",
        t.struct(
            {"name": t.string(), "force": t.boolean(), "auth": t.string().optional()}
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesSetIamPolicy"] = datacatalog.delete(
        "v1/{name}",
        t.struct(
            {"name": t.string(), "force": t.boolean(), "auth": t.string().optional()}
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesGetIamPolicy"] = datacatalog.delete(
        "v1/{name}",
        t.struct(
            {"name": t.string(), "force": t.boolean(), "auth": t.string().optional()}
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesDelete"] = datacatalog.delete(
        "v1/{name}",
        t.struct(
            {"name": t.string(), "force": t.boolean(), "auth": t.string().optional()}
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesFieldsCreate"] = datacatalog.delete(
        "v1/{name}",
        t.struct(
            {"force": t.boolean(), "name": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesFieldsRename"] = datacatalog.delete(
        "v1/{name}",
        t.struct(
            {"force": t.boolean(), "name": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesFieldsPatch"] = datacatalog.delete(
        "v1/{name}",
        t.struct(
            {"force": t.boolean(), "name": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesFieldsDelete"] = datacatalog.delete(
        "v1/{name}",
        t.struct(
            {"force": t.boolean(), "name": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesFieldsEnumValuesRename"] = datacatalog.post(
        "v1/{name}:rename",
        t.struct(
            {
                "name": t.string(),
                "newEnumValueDisplayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TagTemplateFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["catalogSearch"] = datacatalog.post(
        "v1/catalog:search",
        t.struct(
            {
                "query": t.string().optional(),
                "pageSize": t.integer().optional(),
                "scope": t.proxy(
                    renames["GoogleCloudDatacatalogV1SearchCatalogRequestScopeIn"]
                ),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1SearchCatalogResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="datacatalog",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
